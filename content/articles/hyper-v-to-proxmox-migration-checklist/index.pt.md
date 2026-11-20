---
title: "Migrar uma VM do Hyper-V para o Proxmox VE: checklist reversível"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Migre uma máquina virtual do Hyper-V para o Proxmox VE com uma exportação da origem desligada, firmware equivalente, importação de discos, teste de inicialização isolado e plano de reversão."
genre: ["Virtualização", "Administração de sistemas", "Laboratório doméstico"]
tags: ["Migração do Hyper-V para o Proxmox", "Migração do Hyper-V", "Migração do Proxmox VE", "Importação de VHDX", "qm disk import", "Corte de VM", "Exportação do Hyper-V", "VM Windows no Proxmox", "VirtIO no Proxmox", "Reversão de VM", "Migração UEFI", "Pontos de verificação do Hyper-V", "TPM virtual", "Recuperação do BitLocker", "Migração de laboratório doméstico"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Um disco atravessa uma ponte entre um rack de servidores azul e outro laranja, com uma rota de retorno separada e um escudo ao lado do destino."
coverCaption: "Mantenha a VM de origem disponível até que o novo convidado passe pelas verificações de corte."
---

Uma **exportação do Hyper-V** preserva os arquivos de uma máquina virtual, enquanto o Proxmox VE precisa de uma nova configuração de convidado e dos arquivos de disco virtual VHDX importados. Uma cópia bem-sucedida não comprova que o convidado inicializará ou atenderá aos usuários. Esta checklist migra uma VM por meio de uma exportação com a origem desligada, um teste de inicialização controlado e uma mudança com caminho de retorno definido.

<!--more-->

## Principais pontos

- **Registre a origem:** anote geração do firmware, caminhos dos discos, pontos de verificação, rede e criptografia antes de exportar.
- **Pare as gravações:** desligue a VM do Hyper-V antes da exportação final e mantenha-a desligada durante o teste no Proxmox.
- **Iguale a inicialização:** o Hyper-V de Geração 1 usa BIOS legado. A Geração 2 usa UEFI.
- **Valide o serviço:** verifique dados, acesso à rede, backups e integridade do convidado antes de retirar a origem.

## Antes de começar

Agende uma janela de manutenção e teste primeiro com uma VM descartável. Você precisa de acesso administrativo ao Hyper-V e ao Proxmox VE, armazenamento para a exportação e um backup verificado, separado da cópia de migração. Reserve tempo para transferir todos os discos virtuais e testar o aplicativo do convidado. O tamanho do disco e a velocidade de transferência determinam o tempo de indisponibilidade.

Este procedimento cobre uma VM convencional com discos virtuais. **VMs protegidas, discos de passagem direta, discos compartilhados, cargas em cluster e licenças vinculadas ao hardware** exigem planos específicos. Registre quem decide o corte e o horário limite para reverter. Não inicie as duas cópias na rede de produção com a mesma identidade de máquina.

| Dado da origem | Por que é necessário |
|---|---|
| **Geração e firmware da VM** | Selecionar SeaBIOS ou OVMF no Proxmox |
| **Estado e modelo do Secure Boot** | Igualar a política de inicialização e registrar chaves compatíveis |
| **Discos de inicialização e dados** | Importar todos os discos virtuais VHDX necessários na ordem correta |
| **Pontos de verificação e arquivos AVHDX** | Evitar tratar um disco diferencial como disco base independente |
| **IP, DNS, MAC e VLAN** | Restaurar conectividade sem duplicar uma identidade |
| **vTPM e BitLocker** | Preparar a recuperação antes de alterar o hardware virtual |
| **Serviços e verificações de dados** | Definir evidências de sucesso e reversão |

A Geração 1 usa BIOS legado. A Geração 2 usa a Interface de Firmware Extensível Unificada (UEFI). Um **arquivo AVHDX** é um disco diferencial do Hyper-V vinculado a um VHDX base. Um **vTPM** é um Trusted Platform Module virtual usado pelo BitLocker e por outros recursos. Uma **VLAN** é uma rede lógica separada transportada pelo hardware de rede compartilhado.

**SeaBIOS** fornece firmware BIOS legado. **OVMF** fornece firmware UEFI. **VirtIO** é uma interface rápida de dispositivo virtual que requer drivers no convidado. Um **initramfs** é o sistema de arquivos inicial do Linux que carrega drivers antes do sistema principal.

## Faça o inventário da máquina virtual no Hyper-V

Execute estes comandos somente de leitura em uma sessão elevada do PowerShell no host Hyper-V. São exemplos não testados. Antes de usá-los, confirme cada comando com o módulo Hyper-V instalado e o procedimento de mudanças. Digite o nome da VM quando solicitado:

```powershell
$vmName = Read-Host "Nome da VM do Hyper-V"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

O [módulo PowerShell do Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documenta estes comandos de inventário. Compare os caminhos dos discos com as configurações da VM e anote ISO, disco de dados, comutador virtual, endereço estático ou reserva DHCP conectados. Registre o sistema operacional e as versões do aplicativo do convidado. Verifique o backup restaurando uma cópia de teste ou consultando um resultado recente de restauração documentado. Uma cópia de arquivos sem teste de recuperação é uma evidência mais fraca.

Para uma VM de **Geração 2**, registre também o firmware e as configurações de segurança:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Registre o estado do **Secure Boot**, o modelo e a configuração de vTPM. A referência da Microsoft para [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) limita o comando à Geração 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) mostra a configuração de segurança da VM. Não execute **`Get-VMFirmware`** em um convidado de Geração 1. Um **endereço MAC** identifica uma interface de rede. **DNS** associa nomes a endereços. **DHCP** atribui configurações de rede. Um **disco EFI** armazena configurações UEFI.

**Resolva os pontos de verificação antes da exportação final.** A Microsoft informa que uma exportação do Hyper-V reúne arquivos de pontos de verificação e discos VHDX. Excluir um ponto de verificação pelo Hyper-V mescla seu disco diferencial. Nunca exclua um arquivo **`.avhdx`** no sistema de arquivos para apagar um ponto de verificação. Se a mesclagem falhar ou a cadeia de discos parecer incompleta, pare e siga as [orientações de recuperação de pontos de verificação da Microsoft](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). O [guia de pontos de verificação da Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) explica a exclusão e a mesclagem normais.

Para um convidado Windows com **BitLocker** ou **TPM virtual**, obtenha e verifique a chave de recuperação antes de alterar o hardware virtual. A [documentação de segurança da Geração 2 do Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) descreve a criptografia apoiada por vTPM. As [perguntas frequentes do BitLocker da Microsoft](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) explicam por que mudanças de inicialização acionam a recuperação. Um novo dispositivo TPM do Proxmox não reproduz o estado do TPM antigo. Guarde a chave fora da VM exportada.

## Exporte uma VM desligada

Desligue o convidado normalmente. Confirme que o Hyper-V mostra **Off** (desligada), não Saved (guardada). Aguarde a conclusão de qualquer mesclagem de pontos de verificação e exporte a VM para um local com espaço livre suficiente. No Hyper-V Manager, clique com o botão direito na VM, escolha **Export** (exportar) e selecione o destino. O equivalente em PowerShell é:

```powershell
$vmName = Read-Host "Nome da VM desligada do Hyper-V"
$exportPath = Read-Host "Diretório de destino da exportação"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Desligue a VM e aguarde o Hyper-V mostrar Off (desligada) antes de exportar." }
Export-VM -Name $vmName -Path $exportPath
```

O [guia de exportação da Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) diz que uma exportação inclui discos virtuais, configuração e arquivos de pontos de verificação. A referência de [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) define o comando. Confirme os arquivos de disco esperados e os tamanhos no destino. Preserve a VM de origem desligada e seu backup independente. **Não altere os arquivos exportados durante a importação.**

Transfira os arquivos VHDX para um caminho acessível pelo host Proxmox. Trate a exportação como dado confidencial do convidado. Use transporte criptografado, restrinja o acesso ao local de transferência e ao armazenamento de destino e remova cópias temporárias após a validação. Verifique o espaço disponível nos dois locais. Preserve uma exportação intacta para a reversão. Se houver arquivos **`.avhdx`** na exportação, não escolha um **`.vhdx`** base pelo nome presumindo que contém as gravações mais recentes. Resolva a cadeia de discos no Hyper-V antes de continuar.

## Crie a máquina virtual de destino no Proxmox

Crie uma VM nova na interface web do Proxmox com o tipo de sistema operacional, CPU e memória registrados anteriormente. Escolha um ID de VM novo e livre. Não instale um sistema operacional novo. Remova o disco vazio criado pelo assistente antes de importar o disco de origem. Na primeira inicialização, mantenha o adaptador de rede desconectado da bridge de produção ou conecte-o a uma rede de teste isolada.

| Origem Hyper-V | Destino Proxmox |
|---|---|
| **Geração 1, BIOS legado** | SeaBIOS |
| **Geração 2, UEFI** | OVMF com disco EFI e política Secure Boot equivalente |
| **Disco de inicialização Windows sem driver de armazenamento VirtIO** | Conecte inicialmente como SATA |
| **Windows com vTPM ou BitLocker** | Dispositivo novo de estado TPM quando necessário, chave de recuperação pronta antes da primeira inicialização |

O [guia de geração de VM da Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) relaciona a Geração 1 ao BIOS legado e a Geração 2 ao UEFI. A [documentação de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descreve SeaBIOS, OVMF e o disco EFI usado para manter configurações UEFI. **Iguale o modo de inicialização da origem.** Alterá-lo durante a migração cria outro problema de inicialização.

Para uma origem de Geração 2, mantenha o estado de **Secure Boot**. Confira o modelo de origem e selecione chaves inscritas compatíveis com o convidado. Os nomes de modelo do Hyper-V não são transferidos ao Proxmox. O disco EFI de 4 MB do Proxmox e a opção **Pre-Enroll keys** (pré-registro das chaves) fornecem chaves de Secure Boot e o ativam por padrão. Verifique a inicialização do destino antes do corte. A [referência de firmware da Microsoft](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) descreve a exigência do modelo de origem. A [documentação do disco EFI do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descreve as chaves do destino.

Antes de mudar as chaves EFI, confirme que a chave de recuperação está guardada e registre os IDs dos protetores atuais. Siga a documentação instalada do Proxmox VE e do OVMF para inscrever as chaves EFI. Confirme novamente a chave de recuperação e verifique `manage-bde -status` antes da primeira inicialização. Não suspenda, desative nem exclua protetores como etapa genérica de migração. Registre a versão do pacote de firmware, o estado e a versão do firmware Secure Boot e o estado do BitLocker.

Se a origem usar **vTPM**, adicione **TPM State** (estado do TPM) no painel Hardware (componentes) do Proxmox antes da primeira inicialização. Escolha a **versão 2.0**, salvo exigência documentada da versão 1.2 pelo convidado. Isso cria um estado de TPM novo, não uma cópia do vTPM do Hyper-V. Um convidado BitLocker precisa da chave de recuperação verificada na primeira inicialização. A [documentação TPM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descreve a ação Hardware (componentes) e as versões.

No Windows, comece com um disco de inicialização SATA, a menos que o convidado já tenha o driver de armazenamento VirtIO necessário. Depois de uma inicialização bem-sucedida, instale os drivers VirtIO compatíveis e altere um dispositivo virtual por vez. O Proxmox recomenda VirtIO SCSI pelo desempenho, mas um driver de inicialização ausente impede que o Windows acesse o disco do sistema. No Linux, verifique se o initramfs inclui o driver de armazenamento de destino antes de mudar o barramento. A [documentação de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descreve os controladores de disco.

## Importe e conecte discos

No host Proxmox, verifique o caminho VHDX copiado. O exemplo importa um disco para o ID de VM **230** em um armazenamento com ID **`local-lvm`**. Substitua os três valores pelos seus:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

A referência do Proxmox para [**`qm disk import`**](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) informa que a imagem de origem é importada como **disco não utilizado**. A [documentação de imagens do QEMU](https://www.qemu.org/docs/master/system/images) inclui VHDX entre os formatos de conversão aceitos. Importe separadamente cada disco de dados. Aguarde a conclusão de cada tarefa e compare os tamanhos importados com o inventário da origem.

No painel **Hardware** (componentes) da VM, conecte o disco de inicialização não usado como **SATA** para o primeiro boot do Windows. Conecte os discos de dados na ordem documentada. Em **Options > Boot Order** (opções > ordem de inicialização), selecione o disco de inicialização. Para um convidado de Geração 2, confirme **OVMF** e o disco EFI. Mantenha intactos os arquivos de importação e a VM de origem até a validação passar.

## Teste antes do corte

Inicie o convidado Proxmox na rede isolada. No console, confira a tela de inicialização, o login do sistema operacional, os volumes, os dados do aplicativo e os logs do serviço. Uma tela de login não comprova que a migração foi bem-sucedida. Faça as verificações registradas antes da exportação, inclusive uma transação representativa ou leitura de dados recentes.

Para um convidado BitLocker, desbloqueie-o com a chave de recuperação se solicitado. Após o início do Windows, verifique o estado de proteção do volume do sistema e os protetores em um prompt elevado:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

O [guia operacional do BitLocker da Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) documenta a inspeção de protetores e o backup da chave de recuperação. A saída contém material confidencial de recuperação. Não a cole em um chamado ou log público. Verifique o protetor previsto e guarde um método de recuperação atual conforme sua política. Reinicie o convidado e confirme que ele inicializa sem outro pedido de recuperação antes do corte. Pedidos repetidos indicam falha no teste de migração, não motivo para descartar a chave original.

| Teste | Condição de aprovação |
|---|---|
| **Inicialização e discos** | O convidado inicia e todos os volumes esperados são montados |
| **Secure Boot e BitLocker** | A política prevista se mantém e o convidado criptografado reinicia sem repetir a recuperação |
| **Aplicativo** | Uma leitura ou transação representativa funciona |
| **Rede** | Os pares necessários alcançam o convidado de teste nas portas previstas |
| **Recuperação** | O backup do Proxmox e o teste de restauração isolado funcionam antes de retirar a origem |
| **Operações** | Monitoramento, sincronização de horário, desligamento e agente do convidado funcionam como esperado |

Quando os testes do aplicativo passarem, altere o caminho ou endereço da rede de produção durante a janela de manutenção. Mantenha o Hyper-V desligado. Uma NIC virtual diferente pode exigir uma nova reserva DHCP ou a correção do endereço estático no convidado. De outro cliente, verifique DNS, regras de firewall e serviços dependentes. A [documentação de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descreve os dispositivos de rede e as opções do agente do convidado.

## Solucione problemas e reverta

| Sintoma | Primeira verificação |
|---|---|
| **Nenhum dispositivo de inicialização** | Ordem de boot, disco importado, modo BIOS ou UEFI e chaves Secure Boot |
| **Erro de armazenamento do Windows** | Conexão SATA e driver de armazenamento VirtIO ausente |
| **Pedido repetido de recuperação BitLocker** | Novo estado TPM, política Secure Boot, medições de inicialização e protetores |
| **Convidado inicia sem rede** | Nova NIC virtual, bridge, VLAN, reserva DHCP e endereço estático |
| **Dados antigos ou ausentes** | VHDX incorreto, exportação incompleta, cadeia de pontos de verificação ou disco de dados ausente |

Se um teste obrigatório falhar antes do prazo de reversão, pare a VM Proxmox e desconecte-a da rede de produção. Restaure o caminho de rede da origem e inicie a VM original do Hyper-V. **Nunca execute as duas cópias com a mesma identidade de produção.** Registre as gravações aceitas pela cópia Proxmox antes de voltar ao Hyper-V. Essas gravações precisam de recuperação ou conciliação separada porque não chegaram ao disco de origem.

Mantenha a VM de origem e a exportação até que o convidado Proxmox passe nos testes de serviço, em um novo backup e em uma restauração isolada, e conclua o período de observação acordado. A [comparação de virtualização do site](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) ajuda a escolher uma plataforma. O [guia de atualização do Proxmox VE 8 para 9](/articles/proxmox-ve-8-to-9-upgrade-guide/) cobre uma tarefa de manutenção posterior. **A migração termina quando a carga de trabalho e a recuperação funcionam no novo host, não quando a importação do disco acaba.**

## Próximas etapas

Mantenha a VM de origem e a exportação até que as verificações da carga de trabalho, do backup e da reversão passem durante o período de observação acordado. Antes de retirar a origem, consulte o [exercício de restauração de backup de VM no Proxmox](/articles/proxmox-vm-backup-restore-drill/).
