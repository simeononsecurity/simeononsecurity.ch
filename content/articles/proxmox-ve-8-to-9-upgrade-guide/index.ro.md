---
title: "Ghid de upgrade Proxmox VE 8 la 9"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Actualizează Proxmox VE 8 la 9 cu verificări preliminare, pași manuali, automatizare, modificări incompatibile și îndrumări de recuperare."
genre: ["Virtualizare", "Administrare Linux", "Proxmox", "Administrarea serverelor", "Sursă deschisă", "Laborator de acasă"]
tags: ["Proxmox VE 9", "Upgrade Proxmox", "PVE 8 la 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Ceph Proxmox", "proxmox-boot-tool", "grub-efi", "Upgrade LVM", "Upgrade ZFS", "NVIDIA vGPU", "cgroupv2", "Automatizare Proxmox", "Script Bash de upgrade", "Upgrade cluster Proxmox", "Upgrade in-place", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "O sală modernă de servere, cu pictograme luminoase pentru mașini virtuale pe ecrane. Un tehnician lucrează la un laptop printre echipamente bleumarin cu accente albastre, verzi și mov."
coverCaption: "Upgrade Proxmox VE 8 la 9: pași pentru actualizare in-place cu ajutorul unui script automatizat."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0 a fost lansat cu Debian 13 Trixie, kernel 6.14, QEMU 10, LXC 6 și ZFS 2.3.** Ghidul prezintă actualizarea manuală in-place și un script Bash automatizat care detectează configurația și gestionează modificările depozitelor, problemele cunoscute și verificările preliminare.

## Noutăți în Proxmox VE 9

Proxmox VE 9, lansat în august 2025, este un upgrade major. Modificări importante:

| Componentă | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Bază Debian** | Bookworm (12) | Trixie (13) |
| **Kernel implicit** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 încă posibil) | numai cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) include implicit kernel 7.0, QEMU 11, LXC 7 și ZFS 2.4. Ceph Tentacle este implicit în 9.2, iar Squid rămâne disponibil. Migrarea la Squid înainte de upgrade-ul unui cluster Ceph VE 8 este o cerință separată.

**Funcțiile principale noi din PVE 9.0 și versiunile ulterioare:**
- Snapshot-uri VM pe LVM cu alocare completă, prin lanțuri de volume (previzualizare tehnică, disponibilă pentru producție din 9.1)
- Reguli de afinitate High Availability în locul grupurilor HA
- SDN Fabrics pentru rețele Ceph full-mesh cu OpenFabric și OSPF
- Interfață web mobilă nouă (Rust/Yew)
- Extindere ZFS RAIDZ fără întrerupere
- Echilibrare dinamică prin Cluster Resource Scheduler (PVE 9.2)
- WireGuard și BGP ca protocoale SDN fabric (PVE 9.2)
- `/tmp` este acum `tmpfs` (schimbare Debian Trixie; fișierele se curăță periodic)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Comparație Proxmox VE 8 și VE 9 cu versiunile kernelului, QEMU, LXC, ZFS și Ceph" >}}

______

## Înainte să începi: condiții preliminare

**Trebuie să îndeplinești toate condițiile înainte să modifici depozitele.** Consultă [lista de precondiții din wiki-ul oficial de upgrade](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Proxmox VE 8.4 sau o versiune mai nouă

```bash
pveversion
```

Rezultatul trebuie să afișeze `pve-manager/8.4.x` sau o versiune mai nouă. Altfel:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph trebuie să fie la Squid (19.x), numai în medii hiperconvergente

```bash
ceph --version
```

Rezultatul trebuie să indice versiunea 19.x (Squid). Dacă folosești Reef (18.x) sau Quincy (17.x), actualizează mai întâi Ceph. Avansează câte o versiune:

- Quincy (17) → Reef (18) → Squid (19)

*Nu începe upgrade-ul PVE 9 până când toate nodurile Ceph rulează Squid.*

### 3. Proxmox Backup Server instalat pe același nod

Dacă PBS 3.4 și PVE 8.4 folosesc același nod, urmează [instrucțiunile de instalare alăturată](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) și coordonează ambele upgrade-uri într-o operațiune APT. Confirmă că backup-urile se pot restaura și rulează `pve8to9 --full` și `pbs3to4 --full` înainte să schimbi depozitele. Rezolvă problemele raportate înainte să continui.

### 4. Cerințe de acces

- **Preferat**: acces la consolă prin IPMI, iKVM sau tastatură fizică; sesiunea SSH va cădea când repornesc serviciile.
- **SSH**: folosește `tmux` sau `screen` pentru ca upgrade-ul să continue dacă se întrerupe conexiunea:
  ```bash
  tmux new -s upgrade
  ```

### 5. Spațiu pe disc

```bash
df -h /
```

Ai nevoie de **cel puțin 5 GB liberi**, de preferat 10 GB sau mai mult.

### 6. Backup-uri valide

Fă backup tuturor VM-urilor și containerelor pe stocare externă înainte să continui. Testează restaurarea. Un backup valid este obligatoriu.

______

## Modificări incompatibile pe care trebuie să le cunoști

Citește aceste informații înainte de upgrade. Unele cer acțiuni înainte sau după actualizare.

### cgroup V1 a fost eliminat

PVE 9 nu mai acceptă mediul vechi cgroupv1. Dacă l-ai activat anterior:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Dacă apare orice rezultat, elimină parametrul kernelului din `/etc/default/grub` și rulează `update-grub` înainte de upgrade.

**Impact asupra containerelor**: containerele cu systemd 230 sau mai vechi (CentOS 7, Ubuntu 16.04) nu vor porni în PVE 9. Migrează aceste sarcini înainte. Suportul furnizorului pentru Proxmox VE 8.4 s-a încheiat în august 2026.

### Grupurile HA sunt depreciate

Regulile HA înlocuiesc grupurile HA și migrarea are loc automat după ce toate nodurile clusterului ajung la PVE 9. Nu este necesară acțiune manuală; verifică rezultatul după actualizarea ultimului nod.

### Privilegiul VM.Monitor a fost eliminat

Rolurile personalizate care folosesc `VM.Monitor` trebuie actualizate. Folosește `Sys.Audit` pentru acces de bază la monitorul KVM. Scriptul `pve8to9` detectează rolurile afectate.

### Privilegiu nou: VM.Replicate

Crearea sau editarea sarcinilor de replicare a stocării necesită acum `VM.Replicate` pe `/vms/<vmid>`. Ajustează rolurile personalizate dacă e nevoie.

### Containerele LXC privilegiate necesită Sys.Modify

Crearea de containere privilegiate noi necesită `Sys.Modify`. Restaurarea in-place a unui container privilegiat existent nu necesită acest privilegiu.

### systemd-sysctl nu mai citește /etc/sysctl.conf

Setările personalizate din `/etc/sysctl.conf` vor fi ignorate după upgrade. Mută-le în `/etc/sysctl.d/<NN>-name.conf` înainte să repornești.

```bash
# Verifică ce se află în sysctl.conf
grep -v '^\s*#\|\s*$' /etc/sysctl.conf
```

### /tmp este acum tmpfs

Debian Trixie montează `/tmp` ca tmpfs, până la 50% din RAM. Sistemul curăță fișierele periodic. Pentru fișiere temporare mari, folosește `/var/tmp` sau un punct de montare dedicat.

### Compatibilitatea Veeam Backup and Restore {#veeam-backup-broken-for-qemu-machine-version--100}

Verifică versiunile [Veeam Backup & Replication și ale pluginului Proxmox](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html) înainte de upgrade. Cerințele actuale listează suport pentru Proxmox VE 8.2 până la 9.2 pe gazde x86-64 instalate cu ISO-ul oficial Proxmox. Versiunile Veeam mai vechi au intervale proprii de suport.

[Limitările actuale Veeam](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) permit backup-uri VM pe stocare LVM cu Snapshots as Volume Chains (SAVC) activat. Asta nu face din SAVC o locație acceptată pentru fișiere worker Veeam sau destinație Instant Recovery. Problema separată de [restaurare KB4773](https://www.veeam.com/kb4773) afectează tipurile de mașină QEMU mai vechi decât 10, cu discuri QCOW2 restaurate pe stocare SAVC în PVE 9. Folosește o destinație fără SAVC sau restaurează discul ca RAW, conform documentației. Acestea sunt soluții de restaurare, nu motive să fixezi tipul mașinii pe întregul parc. Testează backup-ul și restaurarea pe stocarea dorită înainte să te bazezi pe upgrade.

### Numele interfețelor de rețea se pot schimba

Kernelul 6.14 recunoaște mai multe funcții NIC decât 6.8. Unele NIC-uri primesc sufixe suplimentare în nume. Instrumentul `pve-network-interface-pinning` poate fixa interfețele la nume stabile `nicX` înainte de upgrade:

```bash
pve-network-interface-pinning --help
```

______

## Opțiunea A: upgrade manual in-place

Urmează pașii oficiali de pe [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Pasul 1: rulează lista pve8to9

```bash
pve8to9 --full
```

Rezolvă toate elementele `FAIL` înainte să continui. Rulează din nou după fiecare remediere.

### Pasul 2: migrează VM-urile active (dacă ești într-un cluster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Pasul 3: actualizează complet PVE 8

```bash
apt update && apt dist-upgrade
pveversion   # trebuie să afișeze 8.4.1 sau o versiune mai nouă
```

### Pasul 4: actualizează depozitele de bază Debian

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Comentează sau elimină toate liniile de depozit Bookworm rămase.

### Pasul 5: adaugă depozitul de pachete PVE 9

**Enterprise (necesită abonament):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Fără abonament:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Verifică prin `apt update && apt policy` că noul depozit apare fără erori. Apoi elimină sau comentează vechiul fișier `.list`.

### Pasul 6: actualizează depozitul Ceph (numai în medii hiperconvergente)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Pentru configurații fără abonament, folosește `http://download.proxmox.com/debian/ceph-squid` cu `pve-no-subscription`.

### Pasul 7: reîmprospătează indexul de pachete

```bash
apt update
```

Verifică să nu existe erori.

### Pasul 8: rulează dist-upgrade

```bash
apt dist-upgrade
```

Operațiunea durează între 5 și peste 60 de minute, în funcție de viteza stocării. În timpul upgrade-ului:

- **`/etc/issue`**: păstrează versiunea actuală (sigur)
- **`/etc/lvm/lvm.conf`**: instalează versiunea administratorului de pachete (recomandat)
- **`/etc/ssh/sshd_config`**: instalează versiunea administratorului dacă nu ai personalizat-o
- **`/etc/default/grub`**: păstrează versiunea actuală dacă ai personalizat-o
- **`/etc/chrony/chrony.conf`**: instalează versiunea administratorului dacă nu este personalizată

### Pasul 9: repornește

```bash
reboot
```

Chiar dacă kernelul 6.14 era instalat opțional în PVE 8, repornirea este necesară: kernelul este reconstruit cu toolchain-ul PVE 9.

### Pasul 10: pași după upgrade

```bash
# Golește memoria cache a browserului: Ctrl+Shift+R (sau ⌘+Alt+R pe macOS)
# Verifică toate nodurile clusterului:
pvesh get /nodes

# În clustere, grupurile HA migrează la reguli HA după ce toate nodurile sunt pe PVE 9
journalctl -eu pve-ha-crm  # verifică erorile
```

______

## Opțiunea B: script automatizat (pve8to9-upgrade.sh)

Procesul manual are mulți pași condiționali care depind de configurație. Scriptul `pve8to9-upgrade.sh` îi automatizează.

**Sursa scriptului:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Ce face scriptul

Scriptul gestionează automat întregul upgrade, inclusiv:

| Detectare | Acțiune |
|-----------|--------|
| Depozite Enterprise sau fără abonament | Folosește tipul **activat efectiv**, fără să activeze Enterprise pe noduri fără abonament |
| Versiune Ceph | Blochează dacă găsește Quincy sau Reef și afișează ghidul pas cu pas de upgrade Ceph |
| Tip depozit Ceph | Scrie un `ceph.sources` nou potrivit tipului existent |
| Driver NVIDIA vGPU | Blochează dacă driverul este mai vechi decât 570.158.02 (minim GRID 18.3) |
| GPU NVIDIA passthrough | Avertizează și creează memento de testare după upgrade |
| Depozite CUDA | Actualizează `debian12` la `debian13` în căile URI |
| Metapachet systemd-boot | Îl elimină (corectează bug-ul Debian #1110177 care oprește dist-upgrade) |
| Setări `sysctl.conf` personalizate | Le mută în `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| Blocare FRR post-up | Repară `/etc/network/interfaces` înainte de repornire |
| `systemd-journald-audit.socket` | Îl dezactivează pentru a preveni inundarea jurnalelor |
| Problemă GRUB cu UEFI + LVM | Instalează `grub-efi-amd64` și scrie o fișă de ajutor în `/root/` |
| Depozite terțe `bookworm` | Le comentează și amintește să le actualizezi |
| Conflict `linux-image-amd64` | Elimină pachetul dacă este prezent |
| Activare automată LVM | Rulează scriptul de migrare înainte și după upgrade |
| Serverul de backup Proxmox | Rulează `pbs3to4 --full` și actualizează depozitele PBS pentru Trixie |
| Root ZFS | Detectează și confirmă situația (fără acțiune specială) |

Toate schimbările sunt înregistrate în `/var/log/pve8to9-upgrade-<timestamp>.log`. Backup-urile depozitelor APT sunt scrise în `/root/pve8to9-apt-backups/`, niciodată ca `.bak` în `/etc/apt/sources.list.d/`, deoarece interfața web ar raporta „invalid extension”.

### Instalare și utilizare

```bash
# Descarcă scriptul
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Fă-l executabil
chmod +x pve8to9-upgrade.sh

# Revizuiește-l înainte de rulare (citește scripturile înainte să le rulezi ca root)
less pve8to9-upgrade.sh
```

**Moduri de rulare:**

```bash
# Mod interactiv complet (recomandat)
./pve8to9-upgrade.sh

# Aprobă automat corecțiile sigure și nedistructive
./pve8to9-upgrade.sh --yes

# Simulare: afișează schimbările fără să le aplice
./pve8to9-upgrade.sh --dry-run

# Omite verificarea preliminară pve8to9 --full (nerecomandat)
./pve8to9-upgrade.sh --skip-preflight
```

*Rulează în `tmux` sau `screen` dacă te conectezi prin SSH.*

### Cum arată ieșirea scriptului

Scriptul prezintă rezumatul configurației înainte să ceară confirmarea:

```
══════════════════════════════════════════
  REZUMATUL configurației detectate
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

### Verificări de siguranță care blochează scriptul

Scriptul **refuză să continue** dacă:
- cgroup V1 este activat explicit în linia de comandă a kernelului
- Ceph rulează încă Quincy (17.x) sau Reef (18.x), cu afișarea comenzilor exacte de upgrade Ceph
- Driverul NVIDIA vGPU este anterior versiunii 570 (GRID 18.3)
- Versiunea PVE este mai veche decât 8.4

Pentru fiecare problemă blocantă, scriptul afișează comenzile exacte de remediere înainte de o nouă rulare.

______

## Probleme cunoscute la upgrade

### GRUB nu pornește de pe LVM în modul UEFI

**Afectează**: sisteme cu root pe LVM, pornite cu UEFI și actualizate de la PVE 7.x

```bash
# Remediere (rulează pe sistemul activ după upgrade):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

Scriptul `pve8to9-upgrade.sh` detectează UEFI+LVM și instalează automat pachetul. Scrie și un ghid de recuperare în `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Dacă nodul este blocat** la `grub rescue>` sau „disk 'lvmid/...' not found”:

1. Pornește de pe ISO PVE → Advanced → **Rescue Boot**
2. Sau urmează secțiunea LVM din [Recuperarea după eșecul Grub](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) în wiki-ul oficial

### Metapachetul systemd-boot întrerupe dist-upgrade

Metapachetul `systemd-boot` era instalat automat pe toate sistemele cu ISO PVE 8.1–8.4. În Trixie are hook-uri care rulează la upgrade-ul altor pachete și pot întrerupe `dist-upgrade` dacă ESP nu este montată (Bug Debian #1110177).

```bash
# Elimină-l înainte de dist-upgrade:
apt remove systemd-boot
# NU elimina systemd-boot-efi sau systemd-boot-tools; acestea rămân
```

Scriptul `pve8to9-upgrade.sh` gestionează automat problema și explică de ce.

### PCI passthrough poate eșua cu kernelul 6.14

Unii utilizatori raportează că VM-urile cu PCI passthrough nu pornesc pe kernelul 6.14. Dacă ești afectat:

```bash
# Fixează temporar kernelul vechi:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Configurațiile Ceph full-mesh se blochează la repornire

Dacă `/etc/network/interfaces` conține:

```
post-up /usr/bin/systemctl restart frr.service
```

Schimbă-l în:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Fă asta **înainte de repornire**. Scriptul detectează și repară automat tiparul.

### Thin pool LVM necesită reparare

După upgrade, unele sisteme pot afișa:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Remediază cu:

```bash
lvconvert --repair pve/data
```

### Versiunea minimă a driverului NVIDIA vGPU

Driverul trebuie să fie cel puțin **570.158.02** (GRID 18.3) înainte de upgrade. Versiunile mai vechi sunt incompatibile cu kernelul 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Ordinea upgrade-ului clusterului

Actualizează nodurile pe rând. Verifică dacă fiecare nod este sănătos înainte să începi următorul.

```bash
# Verifică starea clusterului înainte de fiecare upgrade de nod:
pvecm status
ceph -s   # dacă este implementat Ceph
```

**Reguli de migrare pe durata upgrade-ului parțial:**

- VM/CT din PVE 8 → PVE 9: funcționează întotdeauna
- VM/CT din PVE 9 → PVE 8: în general nu este acceptat

După ce toate nodurile sunt la PVE 9, grupurile HA migrează automat la reguli de afinitate HA. Verifică erorile:

```bash
journalctl -eu pve-ha-crm
```

______

## Depanare

### Upgrade-ul se blochează / „proxmox-ve would be removed”

Dacă apare:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Unul sau mai multe pachete nu pot fi actualizate deoarece a rămas configurat un depozit Bookworm. Găsește intrările rămase:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Comentează-le, apoi rulează:

```bash
apt update && apt dist-upgrade
```

Dacă upgrade-ul s-a încheiat parțial:

```bash
apt -f install
```

### Nu pornește după upgrade-ul ZFS

Dacă folosești ZFS ca root cu pornire BIOS veche, consultă [ZFS: trecerea de la Legacy-Boot la Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). Pe sistemele ZFS, `proxmox-boot-tool` trebuie să gestioneze pornirea, nu GRUB direct, pentru a suporta upgrade-urile funcțiilor ZFS.

______

## Listă de verificare după upgrade

După repornirea fiecărui nod:

- [ ] Golește cache-ul browserului (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` afișează 9.x
- [ ] `uname -r` afișează 6.14.x sau o versiune mai recentă
- [ ] Toate VM-urile și CT-urile pornesc corect
- [ ] Starea Ceph: `ceph -s` afișează HEALTH_OK
- [ ] Dacă folosești UEFI+LVM: verifică dacă `grubx64.efi` are o dată recentă de modificare
- [ ] Dacă folosești NVIDIA passthrough: testează o VM non-producție
- [ ] Actualizează depozitele terțe comentate în timpul upgrade-ului
- [ ] Mută setările personalizate din `/etc/sysctl.conf` în `/etc/sysctl.d/`

______

## Verificare după upgrade

După upgrade, verifică depozitele, cvorumul clusterului, stocarea, pornirea sistemelor invitate, backup-urile, regulile firewall și accesul de administrare. Analizează jurnalele sistemului înainte să declari upgrade-ul încheiat. Testează restaurarea unei mașini invitate pe altă gazdă când clusterul permite.

Folosește [ghidul curent de administrare Proxmox VE](https://pve.proxmox.com/pve-docs/) și [notele de lansare](https://pve.proxmox.com/wiki/Roadmap) pentru comenzile specifice versiunii. Nu copia o comandă dintr-o versiune veche fără să verifici versiunea țintă și starea backup-urilor.

## Referințe

1. [Oficial: upgrade Proxmox VE de la 8 la 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Oficial: upgrade de la 8 la 9 — condiții preliminare](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Script automatizat pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Probleme cunoscute Proxmox VE 9.0 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Recuperare după eșecul Grub — eroarea LVM „disk not found”](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: trecerea de la Legacy-Boot la Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ghid de upgrade Ceph Reef la Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Fixarea interfețelor de rețea Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Note de lansare Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
