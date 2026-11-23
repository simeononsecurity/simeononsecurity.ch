---
title: "Guia de atualização do Proxmox VE 8 para 9"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Atualize o Proxmox VE 8 para 9 com verificações prévias, etapas manuais, automação, mudanças incompatíveis e orientações de recuperação."
genre: ["Virtualização", "Administração Linux", "Proxmox", "Gerenciamento de servidores", "Código aberto", "Laboratório doméstico"]
tags: ["Proxmox VE 9", "Atualização do Proxmox", "PVE 8 para 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Ceph no Proxmox", "proxmox-boot-tool", "grub-efi", "Atualização do LVM", "Atualização do ZFS", "NVIDIA vGPU", "cgroupv2", "Automação do Proxmox", "Script de atualização em Bash", "Atualização de cluster Proxmox", "Atualização no local", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Uma sala de servidores moderna com ícones luminosos de máquinas virtuais nas telas. Uma pessoa técnica trabalha em um notebook entre equipamentos azul-marinho com detalhes azuis, verdes e roxos."
coverCaption: "Atualização do Proxmox VE 8 para 9: etapas para atualizar no local com a ajuda de um script automatizado."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**O Proxmox VE 9.0 foi lançado com Debian 13 Trixie, kernel 6.14, QEMU 10, LXC 6 e ZFS 2.3.** Este guia apresenta o caminho manual de atualização no local e um script Bash automatizado que detecta sua configuração e trata mudanças nos repositórios, problemas conhecidos e todas as verificações prévias.

## Novidades no Proxmox VE 9

O Proxmox VE 9, lançado em agosto de 2025, é uma atualização de versão principal. Mudanças importantes:

| Componente | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Base Debian** | Bookworm (12) | Trixie (13) |
| **Kernel padrão** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 ainda é possível) | somente cgroupv2 |

O [Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) traz kernel 7.0, QEMU 11, LXC 7 e ZFS 2.4 por padrão. Ceph Tentacle é o padrão no 9.2, enquanto Squid continua disponível. Migrar para Squid antes de atualizar um cluster Ceph VE 8 é um pré-requisito separado.

**Os principais recursos novos do PVE 9.0 e posteriores incluem:**
- Snapshots de VMs em LVM com alocação integral por cadeias de volumes (prévia técnica, disponível para produção no 9.1)
- Regras de afinidade de alta disponibilidade substituindo grupos HA
- SDN Fabrics para redes Ceph em malha completa com OpenFabric e OSPF
- Nova interface web para dispositivos móveis (Rust/Yew)
- Expansão de dispositivos ZFS RAIDZ sem indisponibilidade
- Balanceamento dinâmico de carga com o Cluster Resource Scheduler (PVE 9.2)
- WireGuard e BGP como protocolos de fabric SDN (PVE 9.2)
- `/tmp` agora usa `tmpfs` (mudança do Debian Trixie, arquivos removidos periodicamente)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Diagrama comparativo do Proxmox VE 8 e VE 9 com mudanças de versão do kernel, QEMU, LXC, ZFS e Ceph" >}}

______

## Antes de começar: pré-requisitos

**Você precisa atender a todos estes requisitos antes de alterar os repositórios.** Consulte a lista completa na [wiki oficial de atualização, seção de pré-requisitos](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Proxmox VE 8.4 ou posterior

```bash
pveversion
```

A saída precisa mostrar `pve-manager/8.4.x` ou posterior. Caso contrário:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph precisa estar no Squid (19.x), somente em ambientes hiperconvergentes

```bash
ceph --version
```

A saída precisa mostrar a versão 19.x (Squid). Se você usa Reef (18.x) ou Quincy (17.x), atualize o Ceph primeiro. O caminho avança uma versão por vez:

- Quincy (17) → Reef (18) → Squid (19)

*Não inicie a atualização para PVE 9 até todos os nós Ceph usarem Squid.*

### 3. Proxmox Backup Server instalado no mesmo nó

Se PBS 3.4 e PVE 8.4 compartilham um nó, siga as [instruções de instalação conjunta](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) e coordene as duas atualizações em uma única operação APT. Confirme que os backups podem ser restaurados e execute `pve8to9 --full` e `pbs3to4 --full` antes de mudar os repositórios. Resolva os problemas antes de prosseguir.

### 4. Requisitos de acesso

- **Preferencial**: acesso ao console por IPMI, iKVM ou teclado físico. A sessão SSH cairá quando os serviços reiniciarem.
- **SSH**: use `tmux` ou `screen` para manter a atualização se a conexão cair:
  ```bash
  tmux new -s upgrade
  ```

### 5. Espaço em disco

```bash
df -h /
```

Reserve **pelo menos 5 GB livres**, de preferência 10 GB ou mais.

### 6. Backups válidos

Faça backup de todas as VMs e dos contêineres em armazenamento externo antes de prosseguir. Teste uma restauração. Um backup válido é obrigatório.

______

## Mudanças incompatíveis que você precisa conhecer

Leia estes pontos antes da atualização. Vários exigem uma ação antes ou depois.

### O cgroup V1 foi removido

O PVE 9 não oferece suporte ao ambiente legado cgroupv1. Se você o habilitou anteriormente:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Se houver qualquer saída, remova o parâmetro do kernel de `/etc/default/grub` e execute `update-grub` antes da atualização.

**Impacto nos contêineres**: contêineres com systemd 230 ou anterior (CentOS 7, Ubuntu 16.04) não iniciarão no PVE 9. Migre essas cargas de trabalho antes. O suporte do fornecedor ao Proxmox VE 8.4 terminou em agosto de 2026.

### Grupos HA obsoletos

Regras HA substituem os grupos HA. A migração ocorre automaticamente quando todos os nós do cluster estiverem no PVE 9. Não é necessário agir manualmente, mas verifique após atualizar o último nó.

### Privilégio VM.Monitor removido

Funções personalizadas que referenciam `VM.Monitor` precisam ser atualizadas. Use `Sys.Audit` para acesso básico ao monitor KVM. O script `pve8to9` detecta as funções afetadas.

### Novo privilégio: VM.Replicate

Criar ou editar trabalhos de replicação de armazenamento agora exige `VM.Replicate` em `/vms/<vmid>`. Ajuste as funções personalizadas se necessário.

### Contêineres LXC privilegiados exigem Sys.Modify

Criar novos contêineres privilegiados agora exige `Sys.Modify`. Restaurar no local um contêiner privilegiado existente não exige.

### systemd-sysctl não lê mais /etc/sysctl.conf

Configurações personalizadas em `/etc/sysctl.conf` serão ignoradas silenciosamente após a atualização. Mova-as para `/etc/sysctl.d/<NN>-name.conf` antes de reiniciar.

```bash
# Confira o conteúdo de sysctl.conf
grep -v '^\s*#\|\s*$' /etc/sysctl.conf
```

### /tmp agora usa tmpfs

O Debian Trixie monta `/tmp` como tmpfs (até 50% da RAM). O sistema limpa os arquivos periodicamente. Para arquivos temporários grandes, use `/var/tmp` ou um ponto de montagem dedicado.

### Compatibilidade do Veeam Backup and Restore {#veeam-backup-broken-for-qemu-machine-version--100}

Confira as compilações do [Veeam Backup & Replication e do plug-in para Proxmox](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html) antes da atualização. Os requisitos atuais listam suporte a Proxmox VE 8.2 até 9.2 em hosts x86-64 instalados com a ISO oficial. Versões anteriores do Veeam têm faixas próprias de suporte.

As [limitações atuais do Veeam](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) permitem backups de VMs em armazenamento baseado em LVM com Snapshots as Volume Chains (SAVC) ativado. Isso não torna o SAVC um local compatível para arquivos de worker do Veeam nem para um destino de Instant Recovery. Um problema separado de [restauração na KB4773](https://www.veeam.com/kb4773) afeta tipos de máquina QEMU anteriores ao 10 com discos QCOW2 restaurados em armazenamento SAVC no PVE 9. Use um destino sem SAVC ou restaure o disco como RAW conforme a documentação. Essas são soluções para restauração, não motivos para fixar o tipo de máquina em toda a frota. Teste um backup e uma restauração no armazenamento pretendido antes de depender da atualização.

### Nomes das interfaces de rede podem mudar

O kernel 6.14 reconhece mais recursos de NIC que o 6.8. Algumas NICs recebem sufixos adicionais. A ferramenta `pve-network-interface-pinning` fixa todas as interfaces em nomes estáveis `nicX` antes da atualização:

```bash
pve-network-interface-pinning --help
```

______

## Opção A: atualização manual no local

Siga as etapas oficiais em [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Etapa 1: execute a lista pve8to9

```bash
pve8to9 --full
```

Resolva todos os itens `FAIL` antes de continuar. Execute novamente após cada correção.

### Etapa 2: migre as VMs em execução (se estiver em um cluster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Etapa 3: atualize completamente o PVE 8

```bash
apt update && apt dist-upgrade
pveversion   # precisa mostrar 8.4.1 ou posterior
```

### Etapa 4: atualize os repositórios base do Debian

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Comente ou remova as linhas de repositório Bookworm que restarem.

### Etapa 5: adicione o repositório de pacotes PVE 9

**Enterprise (exige assinatura):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Sem assinatura:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Confirme com `apt update && apt policy` que o novo repositório aparece sem erros. Depois remova ou comente o antigo arquivo `.list`.

### Etapa 6: atualize o repositório Ceph (somente em ambiente hiperconvergente)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Para instalações sem assinatura, use `http://download.proxmox.com/debian/ceph-squid` com `pve-no-subscription`.

### Etapa 7: atualize o índice de pacotes

```bash
apt update
```

Confirme que não há erros.

### Etapa 8: execute a atualização da distribuição

```bash
apt dist-upgrade
```

O processo leva de 5 a mais de 60 minutos, conforme a velocidade do armazenamento. Durante a atualização:

- **`/etc/issue`**: mantenha a versão atual (seguro)
- **`/etc/lvm/lvm.conf`**: instale a versão do mantenedor (recomendado)
- **`/etc/ssh/sshd_config`**: instale a versão do mantenedor se você não a personalizou
- **`/etc/default/grub`**: mantenha a versão atual se você a personalizou
- **`/etc/chrony/chrony.conf`**: instale a versão do mantenedor se não estiver personalizada

### Etapa 9: reinicie

```bash
reboot
```

Mesmo que o kernel 6.14 já estivesse instalado opcionalmente no PVE 8, é necessário reiniciar: ele é reconstruído com as toolchains do PVE 9.

### Etapa 10: tarefas após a atualização

```bash
# Limpe o cache do navegador: Ctrl+Shift+R (ou ⌘+Alt+R no macOS)
# Confira todos os nós do cluster:
pvesh get /nodes

# Em clusters, os grupos HA migram automaticamente para regras HA após todos os nós estarem no PVE 9
journalctl -eu pve-ha-crm  # confira se há erros
```

______

## Opção B: script automatizado (pve8to9-upgrade.sh)

O processo manual tem muitas etapas condicionais que variam conforme a configuração. O script `pve8to9-upgrade.sh` automatiza todas elas.

**Código-fonte do script:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### O que o script faz

O script trata automaticamente a atualização completa, incluindo:

| Detecção | Ação |
|-----------|--------|
| Repositórios Enterprise ou sem assinatura | Usa o tipo de repositório **ativado no momento**; não ativa Enterprise em nós sem assinatura |
| Versão do Ceph | Bloqueia se encontrar Quincy ou Reef e mostra o guia passo a passo de atualização do Ceph |
| Tipo de repositório Ceph | Cria um novo `ceph.sources` compatível com o tipo existente |
| Driver NVIDIA vGPU | Bloqueia se o driver for anterior a 570.158.02 (mínimo GRID 18.3) |
| Passthrough de GPU NVIDIA | Emite aviso e cria lembrete para teste após a atualização |
| Repositórios CUDA | Altera `debian12` para `debian13` nos caminhos URI |
| Metapacote systemd-boot | Remove o pacote (corrige o bug Debian #1110177 que interrompe dist-upgrade) |
| Configurações personalizadas de `sysctl.conf` | Migra para `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| Impasse de FRR no post-up | Corrige `/etc/network/interfaces` antes da reinicialização |
| `systemd-journald-audit.socket` | Desativa para impedir inundação de logs durante a atualização |
| Problema GRUB em UEFI + LVM | Instala `grub-efi-amd64` e grava um guia rápido em `/root/` |
| Repositórios de terceiros para `bookworm` | Comenta-os e lembra você de atualizá-los |
| Conflito de `linux-image-amd64` | Remove o pacote se estiver presente |
| Ativação automática de LVM | Executa o script de migração antes e depois do upgrade |
| Servidor de Backup Proxmox | Executa `pbs3to4 --full` e atualiza os repositórios PBS para Trixie |
| Raiz ZFS | Detecta e registra a condição (não requer ação especial) |

Todas as mudanças são registradas em `/var/log/pve8to9-upgrade-<timestamp>.log`. Os backups dos repositórios APT são gravados em `/root/pve8to9-apt-backups/`, nunca como arquivos `.bak` em `/etc/apt/sources.list.d/`, o que causaria erros “invalid extension” na interface web.

### Instalação e uso

```bash
# Baixe o script
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Torne-o executável
chmod +x pve8to9-upgrade.sh

# Revise antes de executar (leia sempre scripts antes de executá-los como root)
less pve8to9-upgrade.sh
```

**Modos de execução:**

```bash
# Modo interativo completo (recomendado)
./pve8to9-upgrade.sh

# Aprova automaticamente correções seguras e não destrutivas
./pve8to9-upgrade.sh --yes

# Simulação: mostra cada mudança sem aplicá-la
./pve8to9-upgrade.sh --dry-run

# Ignora a verificação preliminar pve8to9 --full (não recomendado)
./pve8to9-upgrade.sh --skip-preflight
```

*Execute em `tmux` ou `screen` quando estiver conectado por SSH.*

### Exemplo da saída do script

O script mostra um resumo da configuração antes de pedir confirmação:

```
══════════════════════════════════════════
  RESUMO da configuração detectada
══════════════════════════════════════════

  PVE version      : pve-manager/8.4.3/...
  Debian           : bookworm
  Subscription     : true (status: Active)
  PVE repo type    : enterprise  (enterprise was active: true)
  Ceph             : YES (v19.2.3, enterprise repos)
  ZFS root         : false
  UEFI boot        : true
  LVM root         : true
  NVIDIA           : NO
  CUDA repos       : NO
  systemd-boot     : meta=true efi=true
  sysctl.conf      : custom=false (0 lines)
  cgroupv1         : false (must be false for PVE 9)
  FRR post-up      : false (broken pattern)
  LVM autoact.     : false
  PBS co-install   : NO
  3rd-party bookwm : none
```

### Verificações de segurança que bloqueiam o script

O script **se recusará a continuar** se qualquer condição abaixo for verdadeira:

- cgroup V1 estiver explicitamente ativado na linha de comando do kernel
- Ceph ainda estiver em Quincy (17.x) ou Reef (18.x); o script mostra os comandos de atualização do Ceph
- O driver NVIDIA vGPU for anterior à versão 570 (GRID 18.3)
- A versão PVE for anterior à 8.4

Para cada problema bloqueador, o script imprime os comandos exatos para resolvê-lo antes de executá-lo novamente.

______

## Problemas conhecidos na atualização

### O GRUB não inicia pelo LVM no modo UEFI

**Afeta**: sistemas com raiz no LVM e inicialização UEFI, atualizados do PVE 7.x

```bash
# Correção (execute no sistema ativo após a atualização):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

O script `pve8to9-upgrade.sh` detecta UEFI+LVM e instala o pacote automaticamente. Também grava um guia de recuperação em `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Se o nó já estiver parado** em `grub rescue>` ou mostrar “disk 'lvmid/...' not found”:

1. Inicialize pela ISO do PVE → Advanced → **Rescue Boot**
2. Ou siga a seção LVM de [Recuperação de falha do Grub](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) na wiki oficial

### O metapacote systemd-boot interrompe dist-upgrade

O metapacote `systemd-boot` era instalado automaticamente em sistemas com ISO do PVE 8.1–8.4. No Trixie, seus hooks executam durante a atualização de outros pacotes e podem interromper `dist-upgrade` se a ESP não estiver montada (Bug Debian #1110177).

```bash
# Remova-o antes de dist-upgrade:
apt remove systemd-boot
# NÃO remova systemd-boot-efi nem systemd-boot-tools; esses devem permanecer
```

O script `pve8to9-upgrade.sh` cuida disso automaticamente e explica o motivo.

### Passthrough PCI às vezes falha com o kernel 6.14

Alguns usuários relatam que VMs com PCI passthrough não iniciam com o kernel 6.14. Se isso ocorrer:

```bash
# Fixe temporariamente o kernel antigo:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Malha completa Ceph trava na reinicialização

Se `/etc/network/interfaces` contiver:

```
post-up /usr/bin/systemctl restart frr.service
```

Altere para:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Faça isso **antes de reiniciar**. O script detecta e corrige esse padrão.

### O thin pool LVM precisa de reparo

Em alguns sistemas após a atualização:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Corrija com:

```bash
lvconvert --repair pve/data
```

### Versão mínima do driver NVIDIA vGPU

O driver precisa ser pelo menos **570.158.02** (GRID 18.3) antes da atualização. Drivers anteriores são incompatíveis com o kernel 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Ordem de atualização do cluster

Atualize os nós um de cada vez. Confirme que cada nó está saudável antes de iniciar o próximo.

```bash
# Confira a saúde do cluster antes de atualizar cada nó:
pvecm status
ceph -s   # se o Ceph estiver implantado
```

**Regras de migração durante atualizações parciais:**

- VM/CT do PVE 8 para PVE 9: sempre funciona
- VM/CT do PVE 9 para PVE 8: geralmente não há suporte

Depois que todos os nós estiverem no PVE 9, os grupos HA migram automaticamente para regras de afinidade HA. Confira erros:

```bash
journalctl -eu pve-ha-crm
```

______

## Solução de problemas

### A atualização trava / “proxmox-ve would be removed”

Se aparecer:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Um ou mais pacotes não podem ser atualizados porque ainda há um repositório Bookworm configurado. Localize entradas restantes:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Comente-as e execute:

```bash
apt update && apt dist-upgrade
```

Se o processo tiver sido concluído parcialmente:

```bash
apt -f install
```

### Falha ao inicializar após atualizar o ZFS

Se você usa ZFS como raiz com inicialização BIOS legada, consulte [ZFS: trocar Legacy-Boot por Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). O `proxmox-boot-tool` precisa gerenciar a inicialização em sistemas ZFS, e não o GRUB diretamente, para suportar atualizações de recursos ZFS.

______

## Lista de verificação após a atualização

Após reiniciar cada nó:

- [ ] Limpe o cache do navegador (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` mostra 9.x
- [ ] `uname -r` mostra 6.14.x ou posterior
- [ ] Todas as VMs e os CTs iniciam corretamente
- [ ] Saúde do Ceph: `ceph -s` mostra HEALTH_OK
- [ ] Se UEFI+LVM: confirme que `grubx64.efi` tem data de modificação recente
- [ ] Se houver passthrough NVIDIA: teste uma VM que não seja de produção
- [ ] Atualize os repositórios de terceiros comentados durante a atualização
- [ ] Mova as configurações personalizadas de `/etc/sysctl.conf` para `/etc/sysctl.d/`

______

## Verificação após a atualização

Após atualizar, confira a configuração dos repositórios, o quórum do cluster, o estado do armazenamento, a inicialização dos convidados, os backups, as regras de firewall e o acesso de gerenciamento. Analise os logs do sistema antes de declarar a atualização concluída. Teste a restauração de um convidado em outro host quando o cluster permitir.

Use o [guia de administração atual do Proxmox VE](https://pve.proxmox.com/pve-docs/) e as [notas de versão](https://pve.proxmox.com/wiki/Roadmap) para consultar comandos específicos da versão. Não copie um comando de uma versão antiga sem conferir a versão de destino e o estado dos backups.

## Referências

1. [Oficial: atualização do Proxmox VE de 8 para 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Oficial: atualização de 8 para 9, pré-requisitos](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Script automatizado pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Problemas conhecidos do Proxmox VE 9.0 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Recuperação de falha do Grub, erro LVM “disk not found”](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: trocar Legacy-Boot por Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Guia de atualização do Ceph Reef para Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Fixação de interfaces de rede do Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Notas de versão do Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
