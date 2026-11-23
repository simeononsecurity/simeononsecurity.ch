---
title: "Guia d’actualització de Proxmox VE 8 a 9"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Actualitza Proxmox VE 8 a 9 amb comprovacions prèvies, passos manuals, automatització, canvis incompatibles i orientació per recuperar el sistema."
genre: ["Virtualització", "Administració de Linux", "Proxmox", "Administració de servidors", "Programari lliure", "Laboratori domèstic"]
tags: ["Proxmox VE 9", "Actualització de Proxmox", "PVE 8 a 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Ceph de Proxmox", "proxmox-boot-tool", "grub-efi", "Actualització de LVM", "Actualització de ZFS", "NVIDIA vGPU", "cgroupv2", "Automatització de Proxmox", "Script d’actualització Bash", "Actualització de clúster Proxmox", "Actualització in-place", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Una sala de servidors moderna amb icones lluminoses de màquines virtuals a les pantalles. Un tècnic treballa amb un portàtil entre equips blau marí amb accents blaus, verds i violetes."
coverCaption: "Actualització de Proxmox VE 8 a 9: passos per actualitzar in-place amb l’ajuda d’un script automatitzat."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0 es va publicar amb Debian 13 Trixie, el kernel 6.14, QEMU 10, LXC 6 i ZFS 2.3.** Aquesta guia explica tant el procés manual d’actualització in-place com un script Bash automatitzat que detecta la configuració i gestiona els canvis als dipòsits, els problemes coneguts i totes les comprovacions prèvies.

## Novetats de Proxmox VE 9

Proxmox VE 9, publicat l’agost de 2025, és una actualització de versió principal. Canvis destacats:

| Peça | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Base de Debian** | Bookworm (12) | Trixie (13) |
| **Kernel per defecte** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 encara possible) | només cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) inclou per defecte el kernel 7.0, QEMU 11, LXC 7 i ZFS 2.4. Ceph Tentacle és la versió per defecte a 9.2, però Squid continua disponible. Passar a Squid abans d’actualitzar un clúster Ceph VE 8 és un requisit previ independent.

**Les funcions principals noves de PVE 9.0 i posteriors inclouen:**
- Instantànies de VM a LVM amb assignació completa mitjançant cadenes de volums (vista prèvia tècnica, disponible en producció des de 9.1)
- Regles d’afinitat d’alta disponibilitat que substitueixen els grups HA
- SDN Fabrics per a xarxes Ceph de malla completa amb OpenFabric i OSPF
- Interfície web nova per a mòbils (Rust/Yew)
- Ampliació de dispositius ZFS RAIDZ sense interrupció
- Equilibri dinàmic de càrrega amb el Cluster Resource Scheduler (PVE 9.2)
- WireGuard i BGP com a protocols SDN fabric (PVE 9.2)
- `/tmp` ara és `tmpfs` (canvi de Debian Trixie; els fitxers s’esborren periòdicament)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Comparació de Proxmox VE 8 i VE 9 amb canvis de versió del kernel, QEMU, LXC, ZFS i Ceph" >}}

______

## Abans de començar: requisits previs

**Has de complir tots aquests requisits abans de modificar els dipòsits.** Consulta la llista completa a la [wiki oficial d’actualització, apartat de requisits previs](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Proxmox VE 8.4 com a mínim

```bash
pveversion
```

La sortida ha de mostrar `pve-manager/8.4.x` o posterior. Si no:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph ha de ser Squid (19.x), només en entorns hiperconvergents

```bash
ceph --version
```

La sortida ha de mostrar la versió 19.x (Squid). Si fas servir Reef (18.x) o Quincy (17.x), actualitza Ceph primer. El camí avança d’una versió principal cada vegada:

- Quincy (17) → Reef (18) → Squid (19)

*No comencis l’actualització a PVE 9 fins que tots els nodes Ceph funcionin amb Squid.*

### 3. Proxmox Backup Server instal·lat al mateix node

Si PBS 3.4 i PVE 8.4 comparteixen node, segueix les [instruccions d’instal·lació conjunta](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) i coordina les dues actualitzacions en una operació APT. Verifica que les còpies de seguretat es poden restaurar i executa `pve8to9 --full` i `pbs3to4 --full` abans de canviar els dipòsits. Resol els problemes informats abans de continuar.

### 4. Requisits d’accés

- **Preferible**: accés a la consola per IPMI, iKVM o teclat físic. La sessió SSH caurà quan es reiniciïn els serveis.
- **SSH**: fes servir `tmux` o `screen` perquè l’actualització continuï si es talla la connexió:
  ```bash
  tmux new -s upgrade
  ```

### 5. Espai de disc

```bash
df -h /
```

Calen **5 GB lliures com a mínim**, idealment 10 GB o més.

### 6. Còpies de seguretat vàlides

Abans de continuar, fes còpies de totes les VM i els contenidors a un emmagatzematge extern. Prova una restauració. Una còpia vàlida és obligatòria.

______

## Canvis incompatibles que has de conèixer

Llegeix-los abans d’actualitzar. Alguns requereixen una acció prèvia o posterior.

### cgroup V1 ja no hi és

PVE 9 no admet en absolut l’entorn antic cgroupv1. Si l’havies activat:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Si hi ha qualsevol sortida, elimina el paràmetre del kernel de `/etc/default/grub` i executa `update-grub` abans de l’actualització.

**Impacte en contenidors**: els contenidors amb systemd 230 o anterior (CentOS 7, Ubuntu 16.04) no s’iniciaran a PVE 9. Migra aquestes càrregues abans. El suport del proveïdor per a Proxmox VE 8.4 va acabar l’agost de 2026.

### Grups HA obsolets

Les regles HA substitueixen els grups HA. La migració es fa automàticament quan tots els nodes del clúster són a PVE 9. No cal una acció manual, però verifica el resultat després d’actualitzar l’últim node.

### S’ha eliminat el privilegi VM.Monitor

Els rols personalitzats que fan servir `VM.Monitor` s’han d’actualitzar. Fes servir `Sys.Audit` per a l’accés bàsic al monitor KVM. L’script `pve8to9` detecta els rols afectats.

### Privilegi nou: VM.Replicate

Crear o editar tasques de rèplica d’emmagatzematge ara requereix `VM.Replicate` a `/vms/<vmid>`. Ajusta els rols personalitzats si cal.

### Els contenidors LXC privilegiats necessiten Sys.Modify

Crear contenidors privilegiats nous ara requereix `Sys.Modify`. Restaurar in-place un contenidor privilegiat existent no ho requereix.

### systemd-sysctl ja no llegeix /etc/sysctl.conf

Després de l’actualització, les opcions personalitzades de `/etc/sysctl.conf` s’ignoraran sense avís. Abans de reiniciar, mou-les a `/etc/sysctl.d/<NN>-name.conf`.

```bash
# Comprova el contingut de sysctl.conf
grep -v '^\s*#\|\s*$' /etc/sysctl.conf
```

### /tmp ara és tmpfs

Debian Trixie munta `/tmp` com a tmpfs (fins al 50% de la RAM). El sistema esborra fitxers periòdicament. Si hi guardes fitxers temporals grans, trasllada’ls a `/var/tmp` o a un punt de muntatge dedicat.

### Compatibilitat de Veeam Backup and Restore {#veeam-backup-broken-for-qemu-machine-version--100}

Abans d’actualitzar, comprova les versions de [Veeam Backup & Replication i del connector de Proxmox](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html). Els requisits actuals inclouen Proxmox VE 8.2 a 9.2 en amfitrions x86-64 instal·lats amb la ISO oficial de Proxmox. Les versions antigues de Veeam tenen els seus propis intervals de suport.

Les [limitacions actuals de Veeam](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) permeten còpies de VM en emmagatzematge LVM amb Snapshots as Volume Chains (SAVC) activat. Això no converteix SAVC en una ubicació compatible per als fitxers worker de Veeam ni en una destinació d’Instant Recovery. Un problema separat de [restauració a KB4773](https://www.veeam.com/kb4773) afecta tipus de màquina QEMU anteriors a 10 amb discs QCOW2 restaurats a emmagatzematge SAVC a PVE 9. Fes servir una destinació sense SAVC o restaura el disc com a RAW segons la documentació. Són solucions de restauració, no motius per fixar el tipus de màquina a tota la flota. Abans de dependre de l’actualització, prova una còpia i una restauració a l’emmagatzematge previst.

### Els noms de les interfícies de xarxa poden canviar

El kernel 6.14 reconeix més funcions NIC que el 6.8. Algunes NIC reben sufixos addicionals. L’eina `pve-network-interface-pinning` pot fixar totes les interfícies a noms estables `nicX` abans de l’actualització:

```bash
pve-network-interface-pinning --help
```

______

## Opció A: actualització manual in-place

Segueix els passos oficials de [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Pas 1: executa la llista pve8to9

```bash
pve8to9 --full
```

Resol tots els elements `FAIL` abans de continuar. Torna a executar-la després de cada correcció.

### Pas 2: migra les VM en execució (si ets en un clúster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Pas 3: actualitza completament PVE 8

```bash
apt update && apt dist-upgrade
pveversion   # ha de mostrar 8.4.1 o posterior
```

### Pas 4: actualitza els dipòsits base de Debian

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Comenta o elimina les línies de dipòsit Bookworm que quedin.

### Pas 5: afegeix el dipòsit de paquets PVE 9

**Enterprise (requereix subscripció):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Sense subscripció:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Amb `apt update && apt policy`, verifica que el nou dipòsit aparegui sense errors. Després elimina o comenta l’antic fitxer `.list`.

### Pas 6: actualitza el dipòsit Ceph (només en entorns hiperconvergents)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

En configuracions sense subscripció, fes servir `http://download.proxmox.com/debian/ceph-squid` amb `pve-no-subscription`.

### Pas 7: actualitza l’índex de paquets

```bash
apt update
```

Verifica que no hi hagi errors.

### Pas 8: executa dist-upgrade

```bash
apt dist-upgrade
```

Pot trigar de 5 a més de 60 minuts segons la velocitat de l’emmagatzematge. Durant l’actualització:

- **`/etc/issue`**: conserva la versió actual (segur)
- **`/etc/lvm/lvm.conf`**: instal·la la versió del mantenidor (recomanat)
- **`/etc/ssh/sshd_config`**: instal·la la versió del mantenidor si no l’has personalitzat
- **`/etc/default/grub`**: conserva la versió actual si l’has personalitzat
- **`/etc/chrony/chrony.conf`**: instal·la la versió del mantenidor si no està personalitzada

### Pas 9: reinicia

```bash
reboot
```

Encara que el kernel 6.14 ja estigués instal·lat opcionalment a PVE 8, cal reiniciar: es reconstrueix amb les toolchains de PVE 9.

### Pas 10: passos posteriors a l’actualització

```bash
# Esborra la memòria cau del navegador: Ctrl+Shift+R (o ⌘+Alt+R a macOS)
# Comprova tots els nodes del clúster:
pvesh get /nodes

# Als clústers, els grups HA migren a regles HA quan tots els nodes són a PVE 9
journalctl -eu pve-ha-crm  # comprova si hi ha errors
```

______

## Opció B: script automatitzat (pve8to9-upgrade.sh)

El procés manual té molts passos condicionals segons la configuració. L’script `pve8to9-upgrade.sh` els automatitza.

**Codi font de l’script:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Què fa l’script

L’script gestiona automàticament l’actualització completa, incloent-hi:

| Detecció | Acció |
|-----------|--------|
| Dipòsits Enterprise o sense subscripció | Fa servir el tipus de dipòsit **realment activat**; no activa Enterprise en nodes sense subscripció |
| Versió Ceph | Bloqueja Quincy o Reef i mostra la guia d’actualització Ceph pas a pas |
| Tipus de dipòsit Ceph | Escriu un `ceph.sources` nou que coincideix amb el tipus existent |
| Controlador NVIDIA vGPU | Bloqueja versions anteriors a 570.158.02 (mínim GRID 18.3) |
| NVIDIA GPU passthrough | Avisa i genera un recordatori per provar-ho després de l’actualització |
| Dipòsits CUDA | Canvia `debian12` per `debian13` als camins URI |
| Metapaquet systemd-boot | Elimina el paquet (corregeix el bug Debian #1110177 que avorta dist-upgrade) |
| Opcions personalitzades de `sysctl.conf` | Les trasllada a `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| Bloqueig FRR post-up | Corregeix `/etc/network/interfaces` abans de reiniciar |
| `systemd-journald-audit.socket` | El desactiva per evitar una allau de registres |
| Problema GRUB amb UEFI + LVM | Instal·la `grub-efi-amd64` i escriu una guia ràpida a `/root/` |
| Dipòsits `bookworm` de tercers | Els comenta i recorda que cal actualitzar-los |
| Conflicte `linux-image-amd64` | Elimina el paquet si hi és |
| Activació automàtica LVM | Executa l’script de migració abans i després |
| Servidor de còpies de seguretat Proxmox | Executa la comprovació `pbs3to4 --full` i actualitza els dipòsits PBS per a Trixie |
| Arrel ZFS | Detecta i confirma la situació (no cal cap acció especial) |

Tots els canvis es registren a `/var/log/pve8to9-upgrade-<timestamp>.log`. Les còpies dels dipòsits APT es guarden a `/root/pve8to9-apt-backups/`, mai com a `.bak` dins `/etc/apt/sources.list.d/`, ja que la interfície web mostraria l’error “invalid extension”.

### Instal·lació i ús

```bash
# Baixa l’script
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Fes-lo executable
chmod +x pve8to9-upgrade.sh

# Revisa’l abans d’executar-lo (llegeix sempre els scripts abans de fer-los servir com a root)
less pve8to9-upgrade.sh
```

**Modes d’execució:**

```bash
# Mode interactiu complet (recomanat)
./pve8to9-upgrade.sh

# Aprova automàticament les correccions segures i no destructives
./pve8to9-upgrade.sh --yes

# Simulació: mostra els canvis sense aplicar-los
./pve8to9-upgrade.sh --dry-run

# Omet la comprovació prèvia pve8to9 --full (no recomanat)
./pve8to9-upgrade.sh --skip-preflight
```

*Executa’l dins `tmux` o `screen` si et connectes per SSH.*

### Exemple de sortida de l’script

L’script mostra un resum de configuració abans de demanar que continuïs:

```
══════════════════════════════════════════
  RESUM de la configuració detectada
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

### Comprovacions de seguretat que bloquegen l’script

L’script **es nega a continuar** si es compleix qualsevol d’aquestes condicions:

- cgroup V1 està activat explícitament a la línia d’ordres del kernel
- Ceph continua a Quincy (17.x) o Reef (18.x); es mostren les ordres exactes per actualitzar-lo
- El controlador NVIDIA vGPU és anterior a la versió 570 (GRID 18.3)
- La versió PVE és anterior a 8.4

Per a cada problema bloquejant, l’script mostra les ordres exactes per resoldre’l abans de tornar-lo a executar.

______

## Problemes coneguts durant l’actualització

### GRUB no arrenca des de LVM en mode UEFI

**Afecta**: sistemes amb arrel a LVM, arrencada UEFI i actualitzats des de PVE 7.x

```bash
# Solució (executa-la al sistema actiu després de l’actualització):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

L’script `pve8to9-upgrade.sh` detecta UEFI+LVM i instal·la el paquet automàticament. També escriu una guia de recuperació a `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Si el node ja està aturat** a `grub rescue>` o mostra “disk 'lvmid/...' not found”:

1. Arrenca des de la ISO PVE → Advanced → **Rescue Boot**
2. O segueix l’apartat LVM de [Recuperar-se d’una fallada de Grub](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) a la wiki oficial

### El metapaquet systemd-boot avorta dist-upgrade

El metapaquet `systemd-boot` s’instal·lava automàticament als sistemes amb ISO PVE 8.1–8.4. A Trixie, conté hooks que s’executen quan s’actualitzen altres paquets i poden avortar `dist-upgrade` si l’ESP no està muntada (Bug Debian #1110177).

```bash
# Elimina’l abans de dist-upgrade:
apt remove systemd-boot
# NO eliminis systemd-boot-efi ni systemd-boot-tools; s’han de conservar
```

L’script `pve8to9-upgrade.sh` ho gestiona automàticament i n’explica el motiu.

### PCI passthrough pot fallar amb el kernel 6.14

Alguns usuaris informen que les VM amb PCI passthrough no s’inicien amb el kernel 6.14. Si t’afecta:

```bash
# Fixa temporalment el kernel antic:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Les configuracions Ceph full-mesh es bloquegen en reiniciar

Si `/etc/network/interfaces` conté:

```
post-up /usr/bin/systemctl restart frr.service
```

Canvia-ho per:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Fes-ho **abans de reiniciar**. L’script detecta i corregeix aquest patró.

### El thin pool LVM necessita reparació

Després de l’actualització, alguns sistemes mostren:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Solució:

```bash
lvconvert --repair pve/data
```

### Versió mínima del controlador NVIDIA vGPU

Abans d’actualitzar, el controlador ha de ser com a mínim **570.158.02** (GRID 18.3). Els controladors anteriors són incompatibles amb el kernel 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Ordre d’actualització del clúster

Actualitza els nodes d’un en un. Comprova que cada node estigui sa abans de començar el següent.

```bash
# Comprova l’estat del clúster abans d’actualitzar cada node:
pvecm status
ceph -s   # si s’ha desplegat Ceph
```

**Regles de migració durant les actualitzacions parcials:**

- VM/CT de PVE 8 a PVE 9: sempre funciona
- VM/CT de PVE 9 a PVE 8: generalment no està admès

Quan tots els nodes siguin a PVE 9, els grups HA migren automàticament a regles d’afinitat HA. Comprova si hi ha errors:

```bash
journalctl -eu pve-ha-crm
```

______

## Resolució de problemes

### L’actualització s’encalla / “proxmox-ve would be removed”

Si veus:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Un o més paquets no es poden actualitzar perquè encara hi ha un dipòsit Bookworm configurat. Cerca entrades sobrants:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Comenta-les i executa:

```bash
apt update && apt dist-upgrade
```

Si el procés s’ha completat parcialment:

```bash
apt -f install
```

### No arrenca després de l’actualització ZFS

Si fas servir ZFS com a arrel amb arrencada BIOS antiga, consulta [ZFS: canviar Legacy-Boot per Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). En sistemes ZFS, `proxmox-boot-tool` ha de gestionar l’arrencada, no GRUB directament, per suportar actualitzacions de funcions ZFS.

______

## Llista de comprovació posterior a l’actualització

Després de reiniciar cada node:

- [ ] Esborra la memòria cau del navegador (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` mostra 9.x
- [ ] `uname -r` mostra 6.14.x o posterior
- [ ] Totes les VM i els CT s’inicien correctament
- [ ] Estat de Ceph: `ceph -s` mostra HEALTH_OK
- [ ] Amb UEFI+LVM: comprova que `grubx64.efi` tingui una data de modificació recent
- [ ] Amb NVIDIA passthrough: prova una VM que no sigui de producció
- [ ] Actualitza els dipòsits de tercers comentats durant l’actualització
- [ ] Mou les opcions personalitzades de `/etc/sysctl.conf` a `/etc/sysctl.d/`

______

## Verificació posterior a l’actualització

Després d’actualitzar, comprova la configuració dels dipòsits, el quòrum del clúster, l’estat de l’emmagatzematge, l’arrencada dels sistemes convidats, les còpies de seguretat, les regles del tallafoc i l’accés de gestió. Revisa els registres del sistema abans de declarar l’actualització acabada. Si el clúster ho permet, prova la restauració d’un convidat en un altre amfitrió.

Fes servir la [guia d’administració actual de Proxmox VE](https://pve.proxmox.com/pve-docs/) i les [notes de versió](https://pve.proxmox.com/wiki/Roadmap) per a les ordres específiques de cada versió. No copiïs una ordre d’una versió antiga sense comprovar la versió de destinació i l’estat de les còpies.

## Referències

1. [Oficial: actualitzar Proxmox VE de 8 a 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Oficial: actualització de 8 a 9 — requisits previs](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Script d’automatització pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Problemes coneguts de Proxmox VE 9.0 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Recuperar-se d’una fallada de Grub — error LVM “disk not found”](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: canviar Legacy-Boot per Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Guia d’actualització de Ceph Reef a Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Fixació d’interfícies de xarxa de Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Notes de la versió Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
