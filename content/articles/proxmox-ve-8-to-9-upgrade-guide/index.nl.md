---
title: "Handleiding voor de upgrade van Proxmox VE 8 naar 9"
date: 2026-07-22
lastmod: 2026-11-22
toc: true
draft: false
description: "Upgrade Proxmox VE 8 naar 9 met controles vooraf, handmatige stappen, automatisering, ingrijpende wijzigingen en hersteladvies."
genre: ["Virtualisatie", "Linux-beheer", "Proxmox", "Serverbeheer", "Opensourcesoftware", "Thuislab"]
tags: ["Proxmox VE 9", "Proxmox-upgrade", "PVE 8 naar 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "LVM-upgrade", "ZFS-upgrade", "NVIDIA vGPU", "cgroupv2", "Proxmox-automatisering", "Bash-upgradescript", "Proxmox-clusterupgrade", "upgrade op locatie", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Een moderne serverruimte met oplichtende pictogrammen van virtuele machines op schermen. Een technicus werkt op een laptop tussen donkerblauwe apparatuur met blauwe, groene en paarse accenten."
coverCaption: "Proxmox VE 8 naar 9 upgraden: stapsgewijze upgrade op locatie met een geautomatiseerd hulpscript."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0 verscheen op Debian 13 Trixie met kernel 6.14, QEMU 10, LXC 6 en ZFS 2.3.** Deze handleiding behandelt zowel de handmatige upgrade op locatie als een Bash-script dat je configuratie detecteert en repositorywijzigingen, bekende problemen en controles vooraf afhandelt.

## Nieuw in Proxmox VE 9

Proxmox VE 9 (uitgebracht in augustus 2025) is een grote versie-upgrade. De belangrijkste wijzigingen:

| Onderdeel | PVE 8 | PVE 9.0 |
|---|---|---|
| **Debian-basis** | Bookworm (12) | Trixie (13) |
| **Standaardkernel** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 nog mogelijk) | alleen cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) gebruikt standaard kernel 7.0 en bevat QEMU 11, LXC 7 en ZFS 2.4. Ceph Tentacle is de standaard in 9.2, terwijl Squid beschikbaar blijft. Ceph in een VE 8-cluster vóór de upgrade naar Squid brengen is een aparte voorwaarde.

**Belangrijke nieuwe functies in PVE 9.0+:**
- VM-snapshots op dik toegewezen LVM via volumeketens (technische preview, productie in 9.1)
- HA-affiniteitsregels vervangen HA-groepen
- SDN Fabrics voor OpenFabric- en OSPF-full-mesh-Ceph-netwerken
- Nieuwe mobiele webinterface (Rust/Yew)
- ZFS RAIDZ-apparaten uitbreiden zonder uitval
- Dynamische load balancing met de Cluster Resource Scheduler (PVE 9.2)
- WireGuard en BGP als SDN-fabricprotocollen (PVE 9.2)
- `/tmp` is nu `tmpfs` (wijziging in Debian Trixie, bestanden worden periodiek opgeschoond)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Vergelijkingsdiagram van Proxmox VE 8 en VE 9 met de versiewijzigingen voor kernel, QEMU, LXC, ZFS en Ceph" >}}

______

## Voor je begint: vereisten

**Je moet aan al deze voorwaarden voldoen voordat je repositories wijzigt.** Bekijk de volledige lijst met [vereisten in de officiële upgradewiki](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Minimaal Proxmox VE 8.4

```bash
pveversion
```

De uitvoer moet `pve-manager/8.4.x` of hoger tonen. Zo niet:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph moet op Squid (19.x) staan, alleen voor hypergeconvergeerde clusters

```bash
ceph --version
```

De uitvoer moet versie 19.x (Squid) tonen. Gebruik je Reef (18.x) of Quincy (17.x), upgrade Ceph dan eerst. Upgrade altijd stap voor stap:

- Quincy (17) → Reef (18) → Squid (19)

*Ga pas verder met PVE 9 als alle Ceph-knooppunten Squid gebruiken.*

### 3. Proxmox Backup Server samen geïnstalleerd

Staan PBS 3.4 en PVE 8.4 op dezelfde node, volg dan de [instructies voor co-installatie](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) en coördineer beide upgrades in één APT-bewerking. Controleer of back-ups herstelbaar zijn en voer zowel `pve8to9 --full` als `pbs3to4 --full` uit voordat je repositories wijzigt. Los gemelde problemen eerst op.

### 4. Toegangsvereisten

- **Voorkeur**: consoletoegang via IPMI, iKVM of een fysiek toetsenbord. De SSH-sessie valt weg wanneer services opnieuw starten.
- **SSH**: gebruik `tmux` of `screen`, zodat de upgrade doorgaat als de verbinding wegvalt:
  ```bash
  tmux new -s upgrade
  ```

### 5. Schijfruimte

```bash
df -h /
```

Houd minimaal **5 GB vrij**, liefst 10 GB of meer.

### 6. Geldige back-ups

Maak vóór je verdergaat back-ups van alle VM's en containers naar externe opslag. Test een herstel. Een geldige back-up is verplicht.

______

## Ingrijpende wijzigingen die je moet kennen

Lees dit vóór de upgrade. Voor meerdere wijzigingen moet je vooraf of achteraf actie ondernemen.

### cgroup V1 is verwijderd

PVE 9 ondersteunt de oude cgroupv1-omgeving niet meer. Heb je deze eerder ingeschakeld?

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Als dit uitvoer oplevert, verwijder dan de kernelparameter uit `/etc/default/grub` en voer vóór de upgrade `update-grub` uit.

**Gevolgen voor containers**: Containers met systemd 230 of ouder (CentOS 7, Ubuntu 16.04) starten niet op PVE 9. Migreer die workloads eerst. De ondersteuning door de leverancier voor Proxmox VE 8.4 eindigde in augustus 2026.

### HA-groepen zijn verouderd

HA-regels vervangen HA-groepen. Ze worden automatisch gemigreerd zodra alle clusterknooppunten PVE 9 gebruiken. Je hoeft niets handmatig te doen, maar controleer de migratie na de upgrade van het laatste knooppunt.

### VM.Monitor-bevoegdheid verwijderd

Aangepaste rollen met `VM.Monitor` moeten worden aangepast. Gebruik `Sys.Audit` voor basistoegang tot de KVM-monitor. Het script `pve8to9` vindt getroffen rollen.

### Nieuwe bevoegdheid: VM.Replicate

Voor het maken of bewerken van opslagreplicatietaken is nu `VM.Replicate` op `/vms/<vmid>` nodig. Pas aangepaste rollen zo nodig aan.

### Bevoorrechte LXC-containers vereisen Sys.Modify

Voor het maken van nieuwe bevoorrechte containers is nu `Sys.Modify` nodig. Een bestaande bevoorrechte container op dezelfde plek herstellen vereist dat niet.

### systemd-sysctl leest /etc/sysctl.conf niet meer

Aangepaste instellingen in `/etc/sysctl.conf` worden na de upgrade stilzwijgend genegeerd. Verplaats ze vóór de herstart naar `/etc/sysctl.d/<NN>-naam.conf`.

```bash
# Controleer wat er in sysctl.conf staat
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp is nu tmpfs

Debian Trixie koppelt `/tmp` als `tmpfs` (tot 50% van RAM). Bestanden worden periodiek verwijderd terwijl het systeem draait. Gebruik je `/tmp` voor grote tijdelijke bestanden, verplaats die dan naar `/var/tmp` of een apart bestandssysteem.

### Compatibiliteit van Veeam-back-ups en herstel {#veeam-backup-broken-for-qemu-machine-version--100}

Controleer vóór de upgrade je [Veeam Backup & Replication- en Proxmox-plug-inversies](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html). De huidige vereisten noemen Proxmox VE 8.2 tot en met 9.2 op x86-64-hosts die met de officiële Proxmox-ISO zijn geïnstalleerd. Oudere Veeam-versies hebben eigen ondersteuningsbereiken.

De actuele [Veeam-beperkingen](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) ondersteunen VM-back-ups op LVM-opslag als Snapshots as Volume Chains (SAVC) is ingeschakeld. Dat maakt SAVC geen ondersteunde locatie voor Veeam-workerbestanden of als bestemming voor Instant Recovery. Een afzonderlijk [herstelprobleem in KB4773](https://www.veeam.com/kb4773) treft QEMU-machinetypen van vóór versie 10 met QCOW2-schijven die op PVE 9 naar SAVC-opslag worden hersteld. Gebruik een bestemming zonder SAVC of herstel de schijf als RAW, zoals gedocumenteerd. Dit zijn tijdelijke oplossingen voor herstel, geen reden om het machinetype voor je hele omgeving vast te zetten. Test eerst een back-up en herstel op de beoogde opslag.

### Netwerkinterfacenamen kunnen veranderen

Kernel 6.14 herkent meer NIC-functies dan kernel 6.8. Sommige NIC's krijgen extra achtervoegsels in hun naam. Met `pve-network-interface-pinning` kun je vóór de upgrade alle interfaces vastzetten op stabiele `nicX`-namen:

```bash
pve-network-interface-pinning --help
```

______

## Optie A: handmatige upgrade op locatie

Volg de officiële stappen in de [upgradehandleiding van Proxmox](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Stap 1: voer de pve8to9-controle uit

```bash
pve8to9 --full
```

Los alle `FAIL`-meldingen op voordat je verdergaat. Voer de controle na elke oplossing opnieuw uit.

### Stap 2: migreer actieve VM's weg (bij een cluster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Stap 3: werk PVE 8 volledig bij

```bash
apt update && apt dist-upgrade
pveversion   # moet 8.4.1 of hoger tonen
```

### Stap 4: werk de Debian-basisrepositories bij

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Commentarieer resterende regels voor Bookworm-repositories uit of verwijder ze.

### Stap 5: voeg de PVE 9-pakketrepository toe

**Enterprise (abonnement vereist):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Geen abonnement:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Controleer met `apt update && apt policy` of de nieuwe repository zonder fouten verschijnt. Verwijder of commentarieer daarna het oude `.list`-bestand uit.

### Stap 6: werk de Ceph-repository bij (alleen hypergeconvergeerd)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Gebruik voor een installatie zonder abonnement `http://download.proxmox.com/debian/ceph-squid` met `pve-no-subscription`.

### Stap 7: vernieuw de pakketindex

```bash
apt update
```

Controleer op fouten.

### Stap 8: voer de dist-upgrade uit

```bash
apt dist-upgrade
```

Dit duurt 5 tot 60 minuten of langer, afhankelijk van de opslagsnelheid. Tijdens de upgrade:

- **`/etc/issue`**: behoud je huidige versie (veilig)
- **`/etc/lvm/lvm.conf`**: installeer de versie van de pakketbeheerder (aanbevolen)
- **`/etc/ssh/sshd_config`**: installeer de versie van de pakketbeheerder als je het bestand niet hebt aangepast
- **`/etc/default/grub`**: behoud je huidige versie als je die hebt aangepast
- **`/etc/chrony/chrony.conf`**: installeer de versie van de pakketbeheerder als je het bestand niet hebt aangepast

### Stap 9: herstart

```bash
reboot
```

Ook als kernel 6.14 al als optionele kernel op PVE 8 was geïnstalleerd, blijft een herstart nodig. De kernel wordt opnieuw gebouwd met de PVE 9-toolchains.

### Stap 10: stappen na de upgrade

```bash
# Wis de browsercache: Ctrl+Shift+R (of ⌘+Alt+R op macOS)
# Controleer alle nodes in het cluster:
pvesh get /nodes

# In clusters migreren HA-groepen naar HA-regels zodra alle nodes PVE 9 gebruiken
journalctl -eu pve-ha-crm  # controleer op fouten
```

______

## Optie B: automatisch script (pve8to9-upgrade.sh)

Het handmatige proces bevat veel stappen die per configuratie verschillen. Het script `pve8to9-upgrade.sh` automatiseert ze.

**Broncode van het script:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Wat het script doet

Het script voert de volledige upgrade automatisch uit, waaronder:

| Detectie | Actie |
|---|---|
| Enterprise- of repository zonder abonnement | Gebruikt het repo-type dat **actief was ingeschakeld**; schakelt Enterprise niet in op nodes zonder abonnement |
| Ceph-versie | Stopt bij Quincy of Reef en toont de stapsgewijze Ceph-upgradehandleiding |
| Ceph-repo-type | Maakt `ceph.sources` aan met het bestaande repo-type |
| NVIDIA vGPU-stuurprogramma | Stopt bij versie lager dan 570.158.02 (GRID 18.3 minimum) |
| NVIDIA GPU-passthrough | Waarschuwt en maakt een herinnering voor een test na de upgrade |
| CUDA-repositories | Wijzigt `debian12` naar `debian13` in URI-paden |
| systemd-boot-metapakket | Verwijdert het om Debian-bug #1110177 te voorkomen, die de dist-upgrade afbreekt |
| Aangepaste instellingen in `sysctl.conf` | Verplaatst ze naar `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| FRR-deadlock na starten | Past `/etc/network/interfaces` vóór de herstart aan |
| `systemd-journald-audit.socket` | Schakelt de socket uit om logspam tijdens de upgrade te voorkomen |
| UEFI + LVM-probleem met grub | Installeert `grub-efi-amd64` en schrijft een spiekbrief naar `/root/` |
| Repositories van derden voor `bookworm` | Commentarieert ze uit met een herinnering om ze bij te werken |
| Conflict met `linux-image-amd64` | Verwijdert het pakket als het aanwezig is |
| Automatische LVM-activering | Voert het migratiescript vóór en na de upgrade uit |
| Proxmox-reservekopieserver (PBS) | Voert `pbs3to4 --full` uit en werkt PBS-repositories bij voor Trixie |
| ZFS-root | Detecteert en bevestigt dit; extra actie is niet nodig |

Alle wijzigingen komen in `/var/log/pve8to9-upgrade-<timestamp>.log`. Back-ups van APT-repositories komen in `/root/pve8to9-apt-backups/`, nooit als `.bak` in `/etc/apt/sources.list.d/`. Dat zou in de webinterface fouten over een ongeldige extensie veroorzaken.

### Installatie en gebruik

```bash
# Download het script
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \\
  -o pve8to9-upgrade.sh

# Maak het uitvoerbaar
chmod +x pve8to9-upgrade.sh

# Lees het script vóór uitvoering (lees scripts altijd voordat je ze als root uitvoert)
less pve8to9-upgrade.sh
```

**Uitvoermodi:**

```bash
# Volledig interactieve modus (aanbevolen)
./pve8to9-upgrade.sh

# Keur veilige, niet-destructieve reparaties automatisch goed
./pve8to9-upgrade.sh --yes

# Proefrun: toon elke wijziging zonder deze toe te passen
./pve8to9-upgrade.sh --dry-run

# Sla de volledige pve8to9-controle vooraf over (niet aanbevolen)
./pve8to9-upgrade.sh --skip-preflight
```

```
══════════════════════════════════════════
  SUMMARY of detected configuration
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

*Voer het script in `tmux` of `screen` uit als je via SSH verbonden bent.*

### Zo ziet de scriptuitvoer eruit

Het script vat de gedetecteerde configuratie samen voordat het om bevestiging vraagt:

### Blokkerende veiligheidscontroles van het script

Het script **weigert verder te gaan** als een van deze situaties geldt:

- cgroup V1 is expliciet ingeschakeld in de kernelcommandoregel
- Ceph staat nog op Quincy (17.x) of Reef (18.x); het script toont de exacte upgradeopdrachten voor Ceph
- het NVIDIA vGPU-stuurprogramma is ouder dan versie 570 (GRID 18.3)
- PVE is ouder dan 8.4

Bij elke blokkerende situatie geeft het script de exacte opdrachten om het probleem op te lossen voordat je het opnieuw uitvoert.

______

## Bekende upgradeproblemen

### GRUB start niet op vanaf LVM in UEFI-modus

**Geldt voor**: systemen met root op LVM, die in UEFI-modus opstarten en vanaf PVE 7.x zijn geüpgraded.

```bash
# Herstel (voer dit na de upgrade op het actieve systeem uit):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

Het script `pve8to9-upgrade.sh` detecteert UEFI+LVM en installeert dit automatisch. Ook schrijft het een herstelspiekbrief naar `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Staat de node al vast** bij `grub rescue>` of "disk 'lvmid/...' not found":

1. Start de PVE-ISO op → Advanced → **Rescue Boot**
2. Volg anders het [LVM-gedeelte over herstel van GRUB-fouten](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) in de officiële wiki.

### systemd-boot-metapakket breekt dist-upgrade af

Het `systemd-boot`-metapakket werd automatisch geïnstalleerd op systemen met PVE 8.1–8.4-ISO's. In Trixie bevat het hooks die bij upgrades van andere pakketten worden uitgevoerd en de `dist-upgrade` kunnen afbreken als de ESP niet is gekoppeld (Debian-bug #1110177).

```bash
# Verwijder het vóór de dist-upgrade:
apt remove systemd-boot
# Verwijder systemd-boot-efi of systemd-boot-tools NIET; die blijven staan
```

Het script `pve8to9-upgrade.sh` handelt dit automatisch af en legt de reden uit.

### PCI-passthrough werkt soms niet met kernel 6.14

Sommige gebruikers melden dat VM's met PCI-passthrough niet starten met kernel 6.14. Word je getroffen?

```bash
# Zet de oude kernel tijdelijk vast:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Ceph-full-mesh-configuraties lopen vast bij herstart

Staat dit in `/etc/network/interfaces`?

```
post-up /usr/bin/systemctl restart frr.service
```

Vervang het door:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Doe dit **vóór je herstart**. Het script detecteert en repareert dit patroon automatisch.

### LVM-thinpool moet worden hersteld

Sommige systemen melden dit na de upgrade:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Herstel de pool met:

```bash
lvconvert --repair pve/data
```

### Minimale versie van NVIDIA vGPU-stuurprogramma

Vóór de upgrade is minimaal **stuurprogrammaversie 570.158.02** (GRID 18.3) vereist. Oudere stuurprogramma's zijn niet compatibel met kernel 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Upgradevolgorde voor clusters

Upgrade nodes één voor één. Controleer of elke node gezond is voordat je de volgende start.

```bash
# Controleer de clusterstatus vóór de upgrade van elke node:
pvecm status
ceph -s   # alleen als Ceph is geïmplementeerd
```

**Migratieregels tijdens gedeeltelijke upgrades:**

- VM/CT van PVE 8 → PVE 9: werkt altijd
- VM/CT van PVE 9 → PVE 8: wordt doorgaans niet ondersteund

Nadat alle nodes PVE 9 gebruiken, worden HA-groepen automatisch gemigreerd naar HA-affiniteitsregels. Controleer op fouten:

```bash
journalctl -eu pve-ha-crm
```

______

## Problemen oplossen

### Upgrade loopt vast / "proxmox-ve zou worden verwijderd"

Zie je dit?

```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Een of meer pakketten kunnen niet worden geüpgraded omdat er nog een Bookworm-repository is geconfigureerd. Zoek achtergebleven Bookworm-vermeldingen:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Commentarieer deze vermeldingen uit en voer daarna uit:

```bash
apt update && apt dist-upgrade
```

Is de upgrade gedeeltelijk voltooid?

```bash
apt -f install
```

### Opstarten mislukt na ZFS-upgrade

Gebruik je ZFS als root met een oudere BIOS-opstartmethode, bekijk dan [ZFS: overstappen van Legacy Boot naar Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). Op ZFS-systemen moet `proxmox-boot-tool` het opstartproces beheren, niet GRUB rechtstreeks. Zo blijft opstarten werken na ZFS-functie-upgrades.

______

## Controlelijst na de upgrade

Herstart je elke node, controleer dan:

- [ ] Wis de browsercache (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` toont 9.x
- [ ] `uname -r` toont 6.14.x of hoger
- [ ] Alle VM's en CT's starten correct
- [ ] Ceph-status: `ceph -s` toont HEALTH_OK
- [ ] Bij UEFI+LVM: controleer of `grubx64.efi` een recente wijzigingsdatum heeft
- [ ] Bij NVIDIA-passthrough: test een niet-productie-VM
- [ ] Werk repositories van derden bij die tijdens de upgrade zijn uitgecommentarieerd
- [ ] Verplaats aangepaste instellingen uit `/etc/sysctl.conf` naar `/etc/sysctl.d/`

______

## Verificatie na de upgrade

Controleer na de upgrade de repositoryconfiguratie, quorum van het cluster, opslagstatus, het opstarten van gasten, back-ups, firewallregels en beheertoegang. Bekijk de systeemlogs voordat je de upgrade afgerond verklaart. Test zo mogelijk het herstel van één guest op een aparte host.

Gebruik de actuele [beheerhandleiding voor Proxmox VE](https://pve.proxmox.com/pve-docs/) en de [releaseopmerkingen](https://pve.proxmox.com/wiki/Roadmap) voor opdrachten die bij jouw versie horen. Neem geen opdracht uit een oudere release over zonder de doelversie en back-upstatus te controleren.

## Bronnen

1. [Officieel: upgrade van Proxmox VE 8 naar 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Officieel: upgrade van 8 naar 9, vereisten](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Automatiseringsscript pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Bekende problemen in Proxmox VE 9.0 (roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [GRUB-fout herstellen: LVM-fout "disk not found"](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: overstappen van Legacy Boot naar Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph-upgradehandleiding van Reef naar Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmox Network Interface Pinning](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Releaseopmerkingen van Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
