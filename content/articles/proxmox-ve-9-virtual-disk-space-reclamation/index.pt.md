---
title: "Proxmox VE 9: reduza o uso dos discos virtuais e recupere espaço"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Reduza o armazenamento usado por VMs e contêineres LXC no Proxmox VE 9. Compare formatos e backends, ative discard, execute trim e verifique snapshots antes de recuperar espaço."
genre: ["Virtualização", "Administração Linux", "plataforma Proxmox VE", "Armazenamento", "Laboratório doméstico"]
tags: ["espaço em disco Proxmox VE 9", "alocação dinâmica Proxmox", "notificações discard Proxmox", "comando TRIM Proxmox", "Windows ReTrim no Proxmox", "Linux fstrim no Proxmox", "uso de disco LXC Proxmox", "alocação dinâmica LVM Proxmox", "zvol esparso ZFS Proxmox", "dispositivos de bloco Ceph RBD Proxmox", "formato qcow2 Proxmox", "disco raw Proxmox", "instantâneos Proxmox", "recuperação de espaço de disco virtual", "tipos de armazenamento Proxmox", "controlador VirtIO SCSI", "detecção de gravações zero Proxmox", "armazenamento de backups Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Duas grades de blocos ligadas por uma seta mostram os blocos usados de um disco virtual e a capacidade livre de um pool de armazenamento."
coverCaption: "Excluir dados do guest, enviar discard e recuperar espaço são etapas distintas."
---

**Um sistema de arquivos menor no guest nem sempre reduz o espaço usado no Proxmox.** Para liberar espaço no host, o disco precisa oferecer suporte a thin provisioning, a rota de discard da VM deve funcionar e o armazenamento de apoio não pode reter blocos por causa de snapshots. Este guia apresenta configurações e verificações para VMs e contêineres LXC no Proxmox VE 9.

<!--more-->

## Principais pontos

- **Escolha primeiro o armazenamento de apoio.** O tamanho informado de um disco virtual só difere do espaço alocado no host quando o formato da imagem ou o backend aceita thin provisioning.
- **Ative discard na VM e depois execute trim no guest.** Windows ReTrim e Linux `fstrim` enviam solicitações de blocos não usados pelo disco virtual.
- **Verifique snapshots e backups separadamente.** Blocos antigos continuam alocados enquanto um snapshot apontar para eles. Arquivos de backup e chunks PBS seguem regras próprias de retenção.
- **Classifique os mounts LXC pelo tipo.** Volumes rootfs e pontos de montagem gerenciados, bind mounts e mounts de dispositivos têm proprietários e comportamentos de backup diferentes.

## Antes de começar

Você precisa de **acesso de administrador ao Proxmox VE 9**, um backup verificado de cada guest afetado e espaço livre suficiente no pool para a operação. Antes de alterar configurações, anote o ID do guest, o barramento do disco, o ID do volume, o ID do armazenamento, os snapshots e a alocação atual. Use o [teste de restauração de VM](/articles/proxmox-vm-backup-restore-drill/) para testar a recuperação.

**Tempo estimado:** 20 a 60 minutos por guest, além de qualquer trim ou limpeza extensa. **Dificuldade:** Intermediária. Comece com uma VM de baixo risco e compare o uso do armazenamento antes e depois.

> **Aviso:** Um thin pool cheio causa erros de E/S nos guests e pode danificar sistemas de arquivos. Não superaloque a capacidade sem monitorar o espaço livre de dados e metadados do pool. [Documentação de armazenamento do Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Siga a cadeia de alocação

**Exclusão**, **discard** e **recuperação** ocorrem em camadas diferentes. O guest exclui um arquivo e marca os blocos do sistema de arquivos como livres. O sistema de arquivos envia TRIM ou UNMAP para esses blocos. O QEMU encaminha a solicitação quando discard está ativado no disco virtual. O backend libera a alocação física se o formato e o pool aceitarem a operação. [Documentação de discos de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Camada | O que verificar | Evidência útil |
|---|---|---|
| **Arquivos do guest** | Espaço livre do sistema de arquivos | Propriedades do volume no Windows ou Linux `df -h` |
| **Disco virtual** | Barramento, discard, emulação SSD, formato da imagem | Guia **Hardware** da VM ou `qm config VMID` |
| **Volume PVE** | Proprietário e tamanho configurado | Guia **Content** do armazenamento ou `pvesm list STORAGE_ID` |
| **Pool de armazenamento** | Dados e metadados livres, blocos retidos | `pvesm status` e ferramentas específicas do backend |

**Um disco virtual de 100 GiB define um limite de capacidade, não garante 100 GiB alocados.** Por outro lado, um guest que informa 20 GiB em uso não prova que o host usa 20 GiB. Metadados, snapshots, cópias de backup e blocos gravados anteriormente alteram o valor. [Documentação de armazenamento do Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Avalie os formatos dos arquivos de disco

**O backend de armazenamento determina quais formatos de imagem o Proxmox oferece.** zvols ZFS e Ceph RBD usam discos virtuais raw. O LVM normalmente usa raw, com uma exceção de cadeia de volumes do Proxmox VE 9 descrita abaixo. Backends de arquivos, como directory e NFS, aceitam raw ou qcow2. Raw não fornece thin provisioning ou snapshots por si só. O armazenamento subjacente precisa oferecer esses recursos. Qcow2 fornece alocação copy-on-write e snapshots na camada da imagem. [Documentação de discos de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Formato | Mecanismo de alocação | Compromisso de espaço |
|---|---|---|
| **qcow2 em armazenamento de arquivos** | Qcow2 aloca clusters conforme são gravados | Metadados da imagem e cadeias de snapshots ocupam espaço |
| **arquivo raw em armazenamento de arquivos** | Comportamento de arquivo esparso do sistema de arquivos, quando aceito | Raw sozinho não oferece thin provisioning ou snapshots |
| **volume de bloco raw** | LVM thin, ZFS, Ceph RBD ou outro armazenamento subjacente | Alocação do pool e snapshots dependem do backend |

**O Proxmox VE 9 thick LVM tem um modo especial de snapshot.** `snapshot-as-volume-chain` usa relações de backing qcow2 entre volumes lógicos thick LVM. Ele não usa snapshots internos do qcow2. A opção afeta apenas novos discos de VM e continua como prévia tecnológica na documentação atual do Proxmox. O PVE mostra cada snapshot como totalmente alocado. A alocação real na SAN só é menor quando o armazenamento de apoio aceita thin provisioning e discard. [Documentação de armazenamento LVM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Não converta um disco apenas porque a extensão é `.raw`.** Primeiro verifique o plugin de armazenamento e os blocos alocados. Um disco raw em `local-lvm` tem comportamento de alocação diferente de um arquivo raw totalmente alocado em armazenamento directory comum.

## Avalie as categorias de armazenamento

O Proxmox separa **armazenamento de arquivos** de **armazenamento de blocos**. O plugin também controla snapshots, clones, compartilhamento e os tipos de conteúdo aceitos em cada pool. Verifique a entrada **Datacenter > Storage** antes de depender de um formato ou recurso. [Tabela de tipos de armazenamento do Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Armazenamento | Comportamento do disco de VM | Verificação de recuperação |
|---|---|---|
| **Directory, ext4, XFS** | Arquivos raw ou qcow2 | Compare os bytes alocados por `du` com o tamanho virtual da imagem. Verifique snapshots se outra camada fornecer esse recurso. |
| **NFS, CIFS** | Arquivos raw ou qcow2 em armazenamento compartilhado | Verifique o espaço alocado no servidor. O trim do guest não prova que o servidor liberou espaço. |
| **LVM com alocação dinâmica (`local-lvm`)** | Volumes lógicos raw thin, somente local | Acompanhe com `lvs` os percentuais de dados e metadados do thin pool. |
| **LVM thick** | LVs raw ou cadeias de volumes qcow2 do VE 9 | Excluir arquivos no guest não reduz a reserva fixa do LV. Verifique separadamente a alocação thin da SAN. |
| **Armazenamento ZFS (`local-zfs`)** | zvols raw ou subvolumes de contêiner | Verifique `sparse`, propriedades do dataset, uso do pool e snapshots. |
| **Ceph RBD** | Imagens RBD raw thin em armazenamento compartilhado | Verifique a capacidade do pool Ceph, o uso da imagem, snapshots e discard. |
| **Btrfs** | Volumes baseados em arquivos com subvolumes Btrfs para imagens raw | Trate o plugin Btrfs do PVE como prévia tecnológica e examine snapshots e uso do sistema de arquivos. |

**Outros plugins de armazenamento têm funções diferentes.** CephFS oferece armazenamento de arquivos compartilhado. iSCSI e Fibre Channel expõem dispositivos de bloco compartilhados, muitas vezes divididos em volumes de VM com LVM. ZFS over iSCSI usa armazenamento remoto de blocos baseado em ZFS. O Proxmox Backup Server (PBS) guarda backups, não discos de VM ativos. Verifique os tipos de **Content** habilitados antes de colocar dados `images`, `rootdir`, `backup` ou `iso` nesse armazenamento. [Tabela de tipos de armazenamento do Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**As opções de alocação do armazenamento de arquivos importam ao criar o disco.** O valor `format` do armazenamento escolhe `raw`, `qcow2` ou `vmdk` quando aceitos. `preallocation` para arquivos raw e qcow2 aceita `off`, `metadata`, `falloc` ou `full`. O padrão é `metadata`, tratado como `off` para raw. `full` reserva o espaço do arquivo antecipadamente e elimina a pequena ocupação inicial habitual. Verifique a configuração antes de criar um disco grande. A opção `shared` apenas declara um acesso compartilhado já existente. Ela não torna o armazenamento local compartilhado. [Propriedades comuns do armazenamento Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` é a configuração de armazenamento para criar zvols thin.** Sem zvols sparse, a criação reserva capacidade de acordo com o comportamento configurado do volume. Confira a configuração real do armazenamento e do pool antes de alterar uma instalação existente. [Documentação de armazenamento ZFS do Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**O armazenamento directory exige uma segunda verificação.** O tamanho lógico de um arquivo qcow2 não é a capacidade virtual vista pelo guest. `du -h` informa os blocos do sistema de arquivos alocados à imagem. `ls -lh` mostra o tamanho lógico do arquivo. Para uma VM parada, `qemu-img info` informa a capacidade virtual e o tamanho no host. No NFS, use a contabilização do servidor para decisões finais de capacidade. [Referência do QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**O NFS tem outro limite de alocação.** O qcow2 reutilizar um cluster vazio dentro do próprio arquivo não significa que o servidor NFS libere blocos do arquivo. A liberação de buracos exige suporte do cliente, do protocolo negociado, do servidor e do sistema de arquivos do servidor. O NFSv4.2 define `DEALLOCATE`, mas o número da versão não prova que o servidor devolveu espaço. Verifique a montagem NFS negociada e meça a alocação no servidor. [Especificação NFSv4.2 `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Configure as opções do disco virtual

Na interface do Proxmox, abra **VM > Hardware > Hard Disk > Edit**. Verifique o barramento do disco e as opções avançadas. As opções abaixo afetam a alocação ou determinam se uma otimização ajuda. A [referência oficial de opções `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) lista a disponibilidade por barramento.

| Barramento | Opção relacionada ao espaço |
|---|---|
| **IDE** | Compatibilidade legada. Use apenas se o guest não tiver um driver mais recente. |
| **SATA** | Emulação amplamente compatível. Verifique trim no guest e as opções do disco antes de confiar na recuperação. |
| **SCSI com VirtIO SCSI** | Caminho moderno preferido para discard e opções por disco. O Windows precisa do driver VirtIO. |
| **VirtIO Block** | Disco paravirtualizado. Discard no Linux requer kernel 5.0 ou posterior. Não há emulação SSD. |

| Configuração | Efeito | Orientação |
|---|---|---|
| **Encaminhar discard (`on`)** | Encaminha TRIM ou UNMAP do guest | Necessário para recuperação iniciada pelo guest em backend thin compatível. O padrão `ignore` bloqueia o encaminhamento. |
| **Emulação SSD `ssd=1`** | Apresenta o disco ao guest como SSD | Alguns guests precisam dessa identidade para emitir trim. A opção não acelera o armazenamento físico. VirtIO Block não oferece esse indicador. |
| **Detect zeroes `detect_zeroes=1`** | Detecta e tenta otimizar gravações de zeros | Otimização opcional de E/S. Não substitui trim nem garante espaço recuperado. |
| **Barramento: SCSI / VirtIO SCSI single** | Expõe um disco SCSI pelo controlador VirtIO | Padrão prático para guests modernos Windows e Linux. Instale os drivers VirtIO do Windows. |
| **Barramento: VirtIO Block** | Usa o dispositivo de bloco VirtIO | Discard no Linux requer kernel 5.0 ou posterior. Não há emulação SSD. |
| **Thread de E/S `iothread=1`** | Atribui a E/S do disco a outra thread | Use com VirtIO Block ou SCSI em controlador VirtIO SCSI single. É configuração de desempenho, não de recuperação. |
| **Cache e AIO** | Alteram o buffer de E/S e a E/S assíncrona | Ajuste conforme a carga e o backend. Nenhuma das opções reduz um disco. |
| **Backup `backup=0`** | Exclui o disco dos backups de VM | Reduz o escopo do backup e remove os dados da recuperação da VM. Documente outro backup. |
| **Replicação `replicate=0`** | Exclui o disco da replicação de armazenamento | Reduz os dados replicados e exclui o disco da réplica. |

**Outras opções da unidade descrevem comportamento, não recuperação.** `format` se aplica ao alocar um disco em backend com vários formatos de imagem. `size` é a capacidade virtual, não os bytes alocados. `ro=1` torna o disco somente leitura. `snapshot=1` ativa o modo de snapshot temporário do QEMU, que descarta alterações quando a VM desliga. Não é a opção para incluir um disco nos snapshots de VM do Proxmox. Evite-a para dados persistentes. Verifique a cobertura de recuperação antes de usar `backup=0` ou `replicate=0`. [Opções de disco de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Não cole uma linha abreviada `qm set --scsi0` sobre uma unidade existente.** Verifique **`qm config VMID`** e preserve o ID completo do volume e as opções existentes ao editar. Uma atribuição abreviada pode eliminar outras opções por disco. Na interface, confira as opções salvas após cada alteração.

```bash
qm config 100
pvesm status
```

`100` é um ID de VM de exemplo. Para um disco SCSI **novo** de 64 GiB em uma VM existente cujo controlador seja **VirtIO SCSI single** e cujo guest tenha o driver necessário, este comando mostra a sintaxe de alocação. Substitua os IDs da VM e do armazenamento pelos seus valores.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Verifique se `scsi0` já existe antes de usar o exemplo.** O comando altera esse slot. Para um disco existente, use a interface se for mais fácil preservar a string exata de opções. Consulte a [referência do comando `qm` do Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Limpe os arquivos do sistema convidado

**Libere primeiro arquivos do guest.** Confira as configurações de Armazenamento do Windows, arquivos temporários, instaladores antigos, caches de aplicativos e a lixeira. Limpe bancos de dados e runtimes de contêiner pela interface própria. Excluir dados ativos de aplicativos apenas para reduzir alocação traz risco de perda de dados.

**Confirme que o volume usa um disco virtual compatível com discard** e inicie uma sessão elevada do PowerShell na VM Windows:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` indica que o Windows habilitou notificações de exclusão para o sistema de arquivos informado. **ReTrim** reenvia solicitações trim para regiões do volume atualmente não usadas. O comando concluído com sucesso confirma que o guest enviou a operação, não quantos bytes o host recuperou. Confira o host quando o trabalho terminar. [Referência Microsoft `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) e [documentação de discos de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Não confunda o QEMU guest agent com TRIM.** O agente oferece controle do guest e recursos de consistência de backup. Notificações de exclusão do sistema de arquivos trafegam pelo disco virtual. Instalar apenas o agente não recupera blocos. [Documentação do guest agent de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Marque os blocos não utilizados do sistema de arquivos

**Verifique o caminho de blocos e o sistema de arquivos antes de executar trim.** Uma distribuição moderna costuma executar `fstrim.timer` periodicamente. Consulte o estado e depois aplique trim aos sistemas de arquivos montados após excluir dados desnecessários do guest.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** informa a granularidade e os limites de discard dos dispositivos de bloco visíveis. **`fstrim -av`** aplica trim aos sistemas de arquivos montados compatíveis e informa os intervalos enviados. Bytes enviados não equivalem a bytes devolvidos ao pool. Dispositivos criptografados, LVM, RAID e outras camadas precisam aceitar discard em cada nível. [Orientação da Red Hat sobre blocos não usados](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Use trim agendado ou uma política online de discard deliberada. **Não habilite `discard` contínuo em todos os sistemas de arquivos para evitar verificar o caminho de armazenamento.** Após o trim no guest, inspecione o volume e o pool PVE. Se registros excluídos ainda ocuparem arquivos, verifique a política de compactação do banco de dados ou serviço.

## Verifique separadamente o armazenamento dos contêineres

**O LXC não tem um barramento de disco VM emulado para o sistema de arquivos raiz.** Comece com `pct config CTID` e identifique todas as entradas `rootfs` e `mpN`. O Proxmox define mounts apoiados por armazenamento, bind mounts e mounts de dispositivos. Um caminho visível dentro do contêiner não mostra qual volume do host possui seus blocos. [Pontos de montagem de contêineres Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Para um **rootfs ou ponto de montagem gerenciado**, remova arquivos pelo contêiner ou aplicativo e depois verifique no host o volume de apoio e seus snapshots. **Não execute comandos `qm` de discard de VM em um CT.** Em subvolumes ZFS, snapshots retêm blocos excluídos. Em armazenamento directory e LVM thin, verifique a alocação real do backend, não o tamanho configurado do CT.

Execute **`pct fstrim` no host Proxmox** após limpar o CT quando o armazenamento de apoio aceitar discard. O Proxmox aplica trim ao rootfs do CT e aos pontos de montagem gerenciados compatíveis. Ele ignora bind mounts e pontos somente leitura. Use `--ignore-mountpoints` para aplicar trim apenas ao rootfs. Compare o uso do armazenamento antes e depois. [Referência Proxmox `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

Os comandos mostram **escopos alternativos** para o ID de CT de exemplo `101`. Escolha o escopo adequado ao layout do armazenamento. Um trim bem-sucedido não garante a mesma quantidade de bytes liberados se snapshots retiverem blocos antigos.

**Bind mounts e mounts de dispositivos não são gerenciados pelo Proxmox.** Os dados de origem permanecem no host ou em dispositivo externo. Backups `vzdump` do contêiner excluem esses conteúdos. Pontos de montagem adicionais apoiados por armazenamento também ficam excluídos por padrão, a menos que a opção `backup` os inclua. Verifique a política real de backup antes da limpeza. [Documentação de backup do Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Para Docker aninhado, inspecione camadas de imagem, volumes e logs dentro do verdadeiro proprietário do armazenamento antes de executar comandos de limpeza Docker. O [guia de confiabilidade do Docker em LXC](/articles/docker-in-lxc-proxmox-reliability/) explica limites de montagem e backup. Excluir uma imagem de contêiner não remove um volume persistente por padrão.

## Meça o servidor corretamente

**Registre as mesmas medidas antes e depois da limpeza.** O espaço livre do pool é o indicador final de capacidade. Use medidas por volume para encontrar o guest responsável pelo aumento.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventaria volumes gerenciados e tamanhos configurados. Ele não mede bytes alocados em armazenamento thin. Para armazenamento **directory**, inspecione o caminho montado exato e um arquivo de imagem conhecido. Substitua os caminhos pelos valores de **Datacenter > Storage** e da configuração da VM.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Para uma VM **parada**, compare a capacidade virtual e a alocação no host sem alterar o arquivo:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Para **LVM thin**, acompanhe dados e metadados do pool:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Para **ZFS**, separe os dados ativos do dataset dos dados retidos por snapshots:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** informa os blocos retidos por todos os snapshots de um dataset. Os valores `used` dos snapshots não podem ser somados porque eles compartilham blocos. Um arquivo excluído pode deixar o uso do pool igual até que cada snapshot que referencie seus blocos expire ou seja removido conforme a política de retenção. [Snapshots e clones OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Para **Ceph RBD**, mapeie o ID do volume Proxmox antes de executar comandos Ceph. **`qm config VMID`** mostra `STORAGE_ID:IMAGE`. Abra a entrada RBD em **Datacenter > Storage** para encontrar o **pool** e o **namespace** opcional. O ID do armazenamento pode ser diferente do nome do pool. Monte `POOL/IMAGE` com os valores do pool e da imagem. Execute os comandos em um cliente configurado para o cluster Ceph pretendido e com credenciais válidas. [Documentação de armazenamento RBD do Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** informa o uso provisionado e real da imagem, incluindo snapshots associados. Sem o recurso de imagem `fast-diff`, consulta os OSDs em busca de objetos possíveis e exige mais trabalho. **`ceph df`** mostra a capacidade do pool e do cluster. Replicação, codificação de apagamento e snapshots alteram o uso bruto do cluster, portanto os bytes da imagem e do pool diferem. [Referência de comandos Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/) e [orientação sobre uso de pools Ceph](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Se o armazenamento RBD usar namespace, adicione **`--namespace NAMESPACE`** a cada comando `rbd`. Use o namespace configurado na entrada de armazenamento do Proxmox, não o ID do armazenamento.

## Considere instantâneos e cópias de segurança

**Snapshots preservam versões anteriores dos blocos.** Se o uso não cair após trim, examine a guia **Snapshots** da VM ou do CT e o inventário de snapshots do backend. Verifique proprietário e dependências antes de excluir algum. Um backup é uma cópia separada e segue a retenção do armazenamento de backup, não o `df` atual do guest.

**A deduplicação do PBS altera a contabilização.** O datastore contém chunks compartilhados entre backups. O pruning remove metadados de snapshots de backup. Depois, o garbage collection remove chunks sem referência, após um período de espera. Verifique ambas as tarefas antes de afirmar que a capacidade de backup foi recuperada. [Documentação de manutenção do PBS](https://pbs.proxmox.com/docs/maintenance.html)

> **Aviso:** Nunca exclua um arquivo de volume gerenciado pelo Proxmox, zvol ou snapshot com base apenas no nome. Identifique primeiro o guest e a política de retenção. Uma limpeza de armazenamento deve preservar o backup e o caminho de reversão.

## Reconstrua o arquivo de disco com a VM desligada

**Use conversão offline apenas quando trim normal do guest e o caminho do backend não resolverem um problema de alocação qcow2.** Desligue a VM, verifique o backup, identifique relações entre snapshots e cadeias de backing e grave em uma imagem de destino separada. O QEMU alerta para não alterar uma imagem usada por outro processo. [Documentação QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Prefira uma migração gerenciada pelo Proxmox ou o fluxo de backup e restauração** quando o disco tiver snapshots ou estiver em armazenamento de blocos gerenciado. Um `qemu-img convert` independente em uma imagem pertencente ao PVE não atualiza por conta própria a configuração da VM, o proprietário do volume ou as referências a snapshots. Não use `qemu-img resize --shrink` para recuperar arquivos excluídos. Reduzir a capacidade visível pelo guest pode truncar dados se partições e sistemas de arquivos não forem reduzidos antes.

## Solucione uma recuperação malsucedida

| Sintoma | Verificação provável | Próxima ação |
|---|---|---|
| **`df` do guest cai, host fica igual** | Flag discard da VM, trim do guest, snapshots | Verifique todo o caminho discard e os snapshots retidos. |
| **`fstrim` informa não suportado** | Barramento do disco, dispositivos em camadas, backend | Inspecione `lsblk -D`, kernel do guest e cada camada intermediária. |
| **Windows ReTrim termina, host fica igual** | Alocação do backend, snapshots, contabilização do servidor | Compare volume e pool. Confirme que o disco usa armazenamento thin. |
| **`ls -lh` e `du -h` diferem** | Arquivo esparso ou qcow2 | Use `du` para os blocos alocados do sistema de arquivos. |
| **Thin pool LVM continua alto** | Dados, metadados, snapshots | Verifique `lvs` e snapshots do PVE antes de qualquer remoção. |
| **Pool ZFS continua alto** | Blocos retidos por snapshots e reservas | Verifique `usedbysnapshots`, configurações do zvol e capacidade do pool. |
| **`df` do CT e pool divergem** | Bind mounts, pontos de montagem, snapshots | Relacione `rootfs` e cada `mpN` ao proprietário no host. |

**Verifique novamente quando as tarefas em segundo plano terminarem.** A contabilização do armazenamento pode atrasar após trim, exclusão de snapshot ou garbage collection do backend. Compare o espaço livre medido no pool com o valor inicial. Não deduza sucesso apenas pelo código de saída de um comando do guest.

## Próximas etapas

**Crie um registro de armazenamento por guest:** tamanho virtual, bytes alocados, backend, barramento, flag discard, quantidade de snapshots, cobertura de backup e espaço livre do pool. Escolha uma VM, ative o caminho discard compatível, aplique trim no guest e compare os valores registrados. Repita somente se o resultado da primeira VM corresponder ao comportamento esperado do backend.

Para planejar a recuperação de forma mais ampla, siga o [teste de backup e restauração do Proxmox](/articles/proxmox-vm-backup-restore-drill/) e o [guia de atualização do Proxmox VE 8 para 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Fontes

- [Administração de armazenamento do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), tipos de armazenamento, thin provisioning e riscos de capacidade.
- [Armazenamento LVM do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), cadeias de volumes snapshot do VE 9 e alocação.
- [Armazenamento RBD do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), configuração de pools e namespaces.
- [Máquinas virtuais do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), barramentos, formatos, discard e guest agent.
- [Opções de disco VM do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), flags por barramento.
- [Contêineres do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), sistemas de arquivos raiz e propriedade dos pontos de montagem.
- [Comandos de contêiner do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim do contêiner no host.
- [Backup e restauração do Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), cobertura de backup de VM e CT.
- [documentação da Microsoft para `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), sintaxe ReTrim do Windows.
- [Orientação da Red Hat sobre blocos não usados](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), comportamento do Linux `fstrim`.
- [Snapshots e clones OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), blocos retidos por snapshots.
- [Referência de comandos Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/), uso de imagens e snapshots.
- [Especificação NFSv4.2](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), desalocação de espaço no servidor.
- [Documentação de manutenção do PBS](https://pbs.proxmox.com/docs/maintenance.html), pruning e garbage collection.
- [Utilitário de imagem de disco QEMU](https://www.qemu.org/docs/master/tools/qemu-img.html), segurança de conversão offline.
