---
title: "Proxmox VE 8 से 9 अपग्रेड गाइड"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Proxmox VE 8 को 9 में अपग्रेड करने के लिए पूर्व-जांच, मैनुअल चरण, स्वचालन, असंगत बदलाव और रिकवरी निर्देश पाएं।"
genre: ["वर्चुअलाइजेशन", "Linux प्रशासन", "Proxmox", "सर्वर प्रबंधन", "ओपन सोर्स", "होम लैब"]
tags: ["Proxmox VE 9", "Proxmox अपग्रेड", "PVE 8 से 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "LVM अपग्रेड", "ZFS अपग्रेड", "NVIDIA vGPU", "cgroupv2", "Proxmox स्वचालन", "Bash अपग्रेड स्क्रिप्ट", "Proxmox क्लस्टर अपग्रेड", "इन-प्लेस अपग्रेड", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "एक आधुनिक सर्वर कक्ष, जिसकी स्क्रीन पर वर्चुअल मशीन के चमकते आइकन हैं। गहरे नीले उपकरणों के बीच एक तकनीशियन लैपटॉप पर काम कर रहा है और आसपास नीले, हरे तथा बैंगनी रंग की रोशनी है।"
coverCaption: "Proxmox VE 8 से 9 अपग्रेड: स्वचालित सहायक स्क्रिप्ट से इन-प्लेस अपग्रेड के चरण।"
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0, Debian 13 Trixie, kernel 6.14, QEMU 10, LXC 6 और ZFS 2.3 के साथ जारी हुआ।** यह गाइड मैनुअल इन-प्लेस अपग्रेड और एक स्वचालित Bash स्क्रिप्ट, दोनों बताती है। स्क्रिप्ट कॉन्फ़िगरेशन पहचानकर repository बदलावों, ज्ञात समस्याओं और सभी पूर्व-जांचों को संभालती है।

## Proxmox VE 9 में नया क्या है

Proxmox VE 9 अगस्त 2025 में जारी हुआ और यह प्रमुख संस्करण अपग्रेड है। मुख्य बदलाव:

| घटक | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Debian आधार** | Bookworm (12) | Trixie (13) |
| **डिफ़ॉल्ट kernel** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 अब भी संभव) | केवल cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) डिफ़ॉल्ट रूप से kernel 7.0, QEMU 11, LXC 7 और ZFS 2.4 के साथ आता है। Ceph Tentacle 9.2 का डिफ़ॉल्ट है, जबकि Squid उपलब्ध रहता है। VE 8 Ceph क्लस्टर अपग्रेड करने से पहले Squid पर जाना अलग पूर्व-शर्त है।

**PVE 9.0 और बाद के प्रमुख नए फीचर:**
- वॉल्यूम शृंखलाएँ के ज़रिए मोटी आवंटन वाली LVM पर VM snapshots (तकनीकी पूर्वावलोकन, 9.1 से production में)
- HA groups के स्थान पर high-availability affinity नियम
- OpenFabric और OSPF पूर्ण-मेष Ceph नेटवर्क के लिए SDN Fabrics
- नया mobile वेब इंटरफ़ेस (Rust/Yew)
- बिना downtime के ZFS RAIDZ devices का विस्तार
- Cluster Resource Scheduler से गतिशील लोड संतुलन (PVE 9.2)
- SDN नेटवर्क प्रोटोकॉल के रूप में WireGuard और BGP (PVE 9.2)
- `/tmp` अब `tmpfs` है (Debian Trixie बदलाव, फ़ाइलें समय-समय पर साफ़ होती हैं)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Proxmox VE 8 और VE 9 की तुलना, जिसमें kernel, QEMU, LXC, ZFS और Ceph संस्करणों के बदलाव दिखते हैं" >}}

______

## शुरू करने से पहले: पूर्व-शर्तें

**Repositories बदलने से पहले इन सभी शर्तों को पूरा करना ज़रूरी है।** [आधिकारिक अपग्रेड Wiki की prerequisites सूची](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites) देखें।

### 1. कम से कम Proxmox VE 8.4 होना चाहिए

```bash
pveversion
```

आउटपुट में `pve-manager/8.4.x` या नया संस्करण दिखना चाहिए। अन्यथा चलाएँ:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph Squid (19.x) पर होना चाहिए, केवल hyper-converged वातावरण के लिए

```bash
ceph --version
```

आउटपुट में 19.x (Squid) दिखना चाहिए। यदि Reef (18.x) या Quincy (17.x) है, तो पहले Ceph अपग्रेड करें। हर बार एक प्रमुख संस्करण आगे बढ़ें:

- Quincy (17) → Reef (18) → Squid (19)

*सभी Ceph नोड पर Squid चलने तक PVE 9 अपग्रेड शुरू न करें।*

### 3. उसी node पर Proxmox Backup Server इंस्टॉल हो

यदि PBS 3.4 और PVE 8.4 एक node साझा करते हैं, तो [साथ-साथ इंस्टॉलेशन निर्देश](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) अपनाएँ और दोनों अपग्रेड एक APT कार्रवाई में समन्वित करें। Restore योग्य backups सत्यापित करें और repositories बदलने से पहले `pve8to9 --full` तथा `pbs3to4 --full` चलाएँ। रिपोर्ट की गई समस्याएँ हल करें।

### 4. पहुँच की आवश्यकताएँ

- **पसंदीदा**: IPMI, iKVM या भौतिक keyboard से कंसोल पहुँच। Services restart होते समय SSH सत्र टूटेगा।
- **SSH**: connection टूटने पर अपग्रेड जारी रखने के लिए `tmux` या `screen` इस्तेमाल करें:
  ```bash
  tmux new -s upgrade
  ```

### 5. डिस्क स्थान

```bash
df -h /
```

कम से कम **5 GB खाली** रखें, आदर्शतः 10 GB या अधिक।

### 6. मान्य backups

आगे बढ़ने से पहले सभी VMs और containers को बाहरी स्टोरेज पर backup करें। Restore जाँचें। मान्य backup अनिवार्य है।

______

## वे असंगत बदलाव जिन्हें जानना ज़रूरी है

अपग्रेड से पहले पढ़ें। कुछ बदलावों के लिए पहले या बाद में कार्रवाई करनी होगी।

### cgroup V1 हट गया है

PVE 9 पुराने cgroupv1 वातावरण का समर्थन नहीं करता। यदि आपने पहले इसे सक्षम किया था:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

यदि कुछ भी लौटे, तो अपग्रेड से पहले `/etc/default/grub` से kernel पैरामीटर हटाएँ और `update-grub` चलाएँ।

**Containers पर असर**: systemd 230 या पुराने संस्करण वाले containers (CentOS 7, Ubuntu 16.04) PVE 9 में शुरू नहीं होंगे। अपग्रेड से पहले उन्हें migrate करें। Proxmox VE 8.4 का vendor समर्थन अगस्त 2026 में समाप्त हुआ।

### HA groups अप्रचलित हैं

HA rules, HA groups की जगह लेते हैं। सभी क्लस्टर नोड PVE 9 पर आने के बाद migration अपने आप होता है। मैनुअल कार्रवाई नहीं चाहिए, लेकिन आख़िरी node अपग्रेड होने पर जाँचें।

### VM.Monitor privilege हटा दिया गया

`VM.Monitor` का उपयोग करने वाली कस्टम भूमिकाएँ अपडेट करनी होंगी। बुनियादी KVM मॉनिटर पहुँच के लिए `Sys.Audit` इस्तेमाल करें। `pve8to9` प्रभावित roles पहचानता है।

### नया privilege: VM.Replicate

Storage प्रतिलिपि कार्य बनाने या संपादित करने के लिए अब `/vms/<vmid>` पर `VM.Replicate` चाहिए। ज़रूरत के अनुसार कस्टम भूमिकाएँ बदलें।

### Privileged LXC containers को Sys.Modify चाहिए

नए विशेषाधिकार प्राप्त कंटेनर बनाने के लिए अब `Sys.Modify` चाहिए। मौजूदा विशेषाधिकार प्राप्त कंटेनर को in-place restore करने के लिए नहीं।

### systemd-sysctl अब /etc/sysctl.conf नहीं पढ़ता

अपग्रेड के बाद `/etc/sysctl.conf` की कस्टम सेटिंग्स बिना सूचना के अनदेखी होंगी। Reboot से पहले उन्हें `/etc/sysctl.d/<NN>-name.conf` में ले जाएँ।

```bash
# sysctl.conf में मौजूद सामग्री जाँचें
grep -v '^\s*#\|\s*$' /etc/sysctl.conf
```

### /tmp अब tmpfs है

Debian Trixie `/tmp` को tmpfs के रूप में mount करता है (RAM का अधिकतम 50%)। चलते सिस्टम में फ़ाइलें समय-समय पर साफ़ होती हैं। बड़ी अस्थायी फ़ाइलें के लिए `/var/tmp` या अलग mount इस्तेमाल करें।

### Veeam बैकअप और पुनर्स्थापना संगतता {#veeam-backup-broken-for-qemu-machine-version--100}

अपग्रेड से पहले [Veeam Backup & Replication और Proxmox plugin builds](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html) जाँचें। मौजूदा requirements में आधिकारिक Proxmox ISO से इंस्टॉल x86-64 hosts पर Proxmox VE 8.2 से 9.2 सूचीबद्ध हैं। पुराने Veeam संस्करण की support range अलग होती हैं।

मौजूदा [Veeam सीमाएँ](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) Snapshots as Volume Chains (SAVC) सक्षम LVM storage पर VM backups का समर्थन करती हैं। इससे SAVC, Veeam कार्यकर्ता फ़ाइलें या Instant रिकवरी गंतव्य के लिए समर्थित जगह नहीं बन जाता। अलग [KB4773 restore समस्या](https://www.veeam.com/kb4773), PVE 9 पर SAVC स्टोरेज में restore की गई QCOW2 डिस्क वाली QEMU 10 से पुरानी मशीन प्रकार को प्रभावित करता है। SAVC रहित destination लें या दस्तावेज़ के अनुसार disk को RAW के रूप में restore करें। ये restore उपाय हैं, पूरे fleet में मशीन प्रकार pin करने का कारण नहीं। अपग्रेड पर निर्भर होने से पहले लक्षित storage पर backup और restore जाँचें।

### Network interface नाम बदल सकते हैं

Kernel 6.14, 6.8 से अधिक NIC सुविधाएँ पहचानता है। कुछ NIC के नाम में अतिरिक्त suffix आते हैं। अपग्रेड से पहले `pve-network-interface-pinning` tool सभी interfaces को स्थिर `nicX` नाम दे सकता है:

```bash
pve-network-interface-pinning --help
```

______

## विकल्प A: मैनुअल इन-प्लेस अपग्रेड

[आधिकारिक pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9) चरण अपनाएँ।

### चरण 1: pve8to9 जाँच सूची चलाएँ

```bash
pve8to9 --full
```

आगे बढ़ने से पहले हर `FAIL` हल करें। हर सुधार के बाद दोबारा चलाएँ।

### चरण 2: चल रही VMs migrate करें (यदि cluster में हों)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### चरण 3: PVE 8 को पूरा अपडेट करें

```bash
apt update && apt dist-upgrade
pveversion   # 8.4.1 या नया संस्करण दिखना चाहिए
```

### चरण 4: Debian आधार भंडार अपडेट करें

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Bookworm वाली बाकी repository पंक्तियाँ comment या remove करें।

### चरण 5: PVE 9 पैकेज भंडार जोड़ें

**Enterprise (subscription आवश्यक):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Subscription के बिना:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

`apt update && apt policy` से जाँचें कि नई repository बिना त्रुटि दिखती है। फिर पुरानी `.list` file हटाएँ या comment करें।

### चरण 6: Ceph भंडार अपडेट करें (केवल hyper-converged वातावरण में)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Subscription रहित setup के लिए `http://download.proxmox.com/debian/ceph-squid` और `pve-no-subscription` इस्तेमाल करें।

### चरण 7: पैकेज सूचकांक refresh करें

```bash
apt update
```

त्रुटियाँ न होने की पुष्टि करें।

### चरण 8: dist-upgrade चलाएँ

```bash
apt dist-upgrade
```

Storage speed के अनुसार इसमें 5 से 60+ मिनट लगते हैं। अपग्रेड के दौरान:

- **`/etc/issue`**: मौजूदा version रखें (सुरक्षित)
- **`/etc/lvm/lvm.conf`**: maintainer संस्करण इंस्टॉल करें (अनुशंसित)
- **`/etc/ssh/sshd_config`**: यदि customize नहीं की, तो maintainer संस्करण लें
- **`/etc/default/grub`**: customize की हो, तो मौजूदा version रखें
- **`/etc/chrony/chrony.conf`**: customize न हो, तो maintainer संस्करण लें

### चरण 9: reboot करें

```bash
reboot
```

PVE 8 में kernel 6.14 opt-in के रूप में पहले से इंस्टॉल हो तब भी reboot ज़रूरी है, क्योंकि kernel PVE 9 toolchains से दोबारा बनाया जाता है।

### चरण 10: अपग्रेड के बाद के कदम

```bash
# Browser cache साफ़ करें: Ctrl+Shift+R (macOS पर ⌘+Alt+R)
# Cluster के सभी nodes जाँचें:
pvesh get /nodes

# सभी nodes PVE 9 पर आने के बाद HA groups, HA rules में अपने आप migrate होते हैं
journalctl -eu pve-ha-crm  # errors जाँचें
```

______

## विकल्प B: स्वचालित script (pve8to9-upgrade.sh)

मैनुअल प्रक्रिया में configuration के अनुसार कई conditional चरण हैं। `pve8to9-upgrade.sh` script उन्हें स्वचालित करती है।

**स्क्रिप्ट स्रोत:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Script क्या करती है

Script पूरा अपग्रेड स्वचालित रूप से संभालती है, जिसमें शामिल हैं:

| पहचान | कार्रवाई |
|-----------|--------|
| Enterprise या बिना सदस्यता वाले भंडार | जो प्रकार **वास्तव में सक्षम** था वही लेती है; no-subscription nodes पर Enterprise सक्षम नहीं करती |
| Ceph संस्करण | Quincy या Reef होने पर रोकती है और Ceph अपग्रेड गाइड दिखाती है |
| Ceph भंडार प्रकार | मौजूदा प्रकार से मेल खाती नई `ceph.sources` लिखती है |
| NVIDIA vGPU ड्राइवर | 570.158.02 से पुराना होने पर रोकती है (GRID 18.3 न्यूनतम) |
| NVIDIA GPU पासथ्रू | चेतावनी देती है और अपग्रेड बाद परीक्षण अनुस्मारक बनाती है |
| CUDA भंडार | URI पथ में `debian12` को `debian13` करती है |
| systemd-boot मेटापैकेज | हटाती है (Debian बग #1110177 ठीक करती है जो dist-upgrade रोकता है) |
| `sysctl.conf` कस्टम सेटिंग्स | `/etc/sysctl.d/99-pve8to9-migrated.conf` में migrate करती है |
| FRR post-up गतिरोध | reboot से पहले `/etc/network/interfaces` ठीक करती है |
| `systemd-journald-audit.socket` | लॉग बाढ़ रोकने के लिए disable करती है |
| UEFI + LVM GRUB समस्या | `grub-efi-amd64` install करती है और `/root/` में cheat-sheet लिखती है |
| तृतीय-पक्ष `bookworm` repository | comment करके update करने का reminder देती है |
| `linux-image-amd64` conflict | मौजूद होने पर हटाती है |
| LVM स्वतः सक्रियण | स्थानांतरण स्क्रिप्ट, अपग्रेड से पहले और बाद चलाती है |
| Proxmox बैकअप सर्वर | `pbs3to4 --full` चलाकर PBS भंडार को Trixie पर अपडेट करती है |
| ZFS मूल फ़ाइल सिस्टम | पहचानकर नोट करती है (विशेष कार्रवाई नहीं) |

सभी बदलाव `/var/log/pve8to9-upgrade-<timestamp>.log` में दर्ज होते हैं। APT भंडार बैकअप `/root/pve8to9-apt-backups/` में लिखे जाते हैं, `/etc/apt/sources.list.d/` में `.bak` के रूप में कभी नहीं (वेब UI में “invalid extension” (अमान्य एक्सटेंशन) त्रुटि आएगी)।

### इंस्टॉलेशन और उपयोग

```bash
# Script डाउनलोड करें
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Executable बनाएँ
chmod +x pve8to9-upgrade.sh

# चलाने से पहले समीक्षा करें (root के रूप में चलाने से पहले script पढ़ें)
less pve8to9-upgrade.sh
```

**चलाने के मोड:**

```bash
# पूर्ण interactive mode (अनुशंसित)
./pve8to9-upgrade.sh

# सभी सुरक्षित, non-destructive fixes को स्वतः स्वीकृत करें
./pve8to9-upgrade.sh --yes

# Dry run: बदलाव दिखाएँ, लागू न करें
./pve8to9-upgrade.sh --dry-run

# pve8to9 --full पूर्व-जांच छोड़ें (अनुशंसित नहीं)
./pve8to9-upgrade.sh --skip-preflight
```

*SSH से जुड़ने पर `tmux` या `screen` में चलाएँ।*

### Script output कैसा दिखता है

आगे बढ़ने से पहले script कॉन्फ़िगरेशन सारांश दिखाती है:

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

### Script की blocking safety checks

इनमें से कोई भी स्थिति हो तो script **आगे बढ़ने से मना करती है**:

- Kernel command line में cgroup V1 स्पष्ट रूप से सक्षम है
- Ceph अब भी Quincy (17.x) या Reef (18.x) है; script सटीक Ceph अपग्रेड कमांड दिखाती है
- NVIDIA vGPU ड्राइवर version 570 (GRID 18.3) से पुराना है
- PVE संस्करण 8.4 से पुराना है

हर अवरुद्ध करने वाली समस्या के लिए script सुधार कर फिर चलाने की सटीक commands दिखाती है।

______

## ज्ञात अपग्रेड समस्याएँ

### UEFI मोड में GRUB LVM से boot नहीं करता

**प्रभावित**: PVE 7.x से अपग्रेड किए गए, UEFI में boot होने वाले LVM-root सिस्टम

```bash
# सुधार (अपग्रेड के बाद चालू सिस्टम पर चलाएँ):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

`pve8to9-upgrade.sh` UEFI+LVM पहचानकर package अपने आप इंस्टॉल करती है। यह `/root/GRUB-RECOVERY-CHEATSHEET.txt` में रिकवरी cheat-sheet भी लिखती है।

**यदि node `grub rescue>` पर अटक गया हो** या “disk 'lvmid/...' not found” (डिस्क नहीं मिली) दिखाए:

1. PVE ISO से boot करें → Advanced → **Rescue Boot**
2. या आधिकारिक Wiki का [Recover From Grub Failure — LVM अनुभाग](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) अपनाएँ

### systemd-boot मेटापैकेज dist-upgrade रोकता है

PVE 8.1–8.4 ISO वाले सभी सिस्टमों में `systemd-boot` meta-package स्वतः इंस्टॉल हुआ था। Trixie में इसके hooks दूसरे packages अपग्रेड होने पर चलते हैं और ESP mount न हो तो `dist-upgrade` बीच में रोक सकते हैं (Debian Bug #1110177)।

```bash
# dist-upgrade से पहले हटाएँ:
apt remove systemd-boot
# systemd-boot-efi या systemd-boot-tools न हटाएँ; वे बने रहने चाहिए
```

`pve8to9-upgrade.sh` इसे अपने आप संभालती है और कारण बताती है।

### Kernel 6.14 में PCI पासथ्रू कभी-कभी विफल

कुछ उपयोगकर्ताओं ने बताया कि PCI पासथ्रू वाली VMs kernel 6.14 पर शुरू नहीं होतीं। प्रभावित हों तो:

```bash
# पुराने kernel को अस्थायी रूप से pin करें:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Ceph full-mesh setup reboot पर deadlock होता है

यदि `/etc/network/interfaces` में यह हो:

```
post-up /usr/bin/systemctl restart frr.service
```

इसे इससे बदलें:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

यह **reboot से पहले** करें। Script इस pattern को अपने आप पहचानकर ठीक करती है।

### LVM thin pool की मरम्मत चाहिए

अपग्रेड के बाद कुछ सिस्टम यह दिखा सकते हैं:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

इसे ठीक करें:

```bash
lvconvert --repair pve/data
```

### NVIDIA vGPU ड्राइवर का न्यूनतम संस्करण

अपग्रेड से पहले driver कम से कम **570.158.02** (GRID 18.3) होना चाहिए। पुराने drivers kernel 6.x के अनुकूल नहीं हैं।

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Cluster upgrade क्रम

Nodes को एक-एक करके अपग्रेड करें। अगला शुरू करने से पहले हर node स्वस्थ है, यह सत्यापित करें।

```bash
# प्रत्येक node upgrade से पहले cluster health जाँचें:
pvecm status
ceph -s   # यदि Ceph deployed है
```

**आंशिक अपग्रेड के दौरान migration नियम:**

- PVE 8 से PVE 9 की VM/CT: हमेशा काम करता है
- PVE 9 से PVE 8 की VM/CT: सामान्यतः समर्थित नहीं

सभी nodes PVE 9 पर होने के बाद HA groups, HA affinity नियम में अपने आप migrate होते हैं। errors देखें:

```bash
journalctl -eu pve-ha-crm
```

______

## समस्या निवारण

### अपग्रेड रुक जाए: `proxmox-ve` पैकेज हटाने की चेतावनी

यदि यह दिखे:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

एक या अधिक packages अपग्रेड नहीं हो रहे क्योंकि कोई Bookworm repository अब भी configured है। बची हुई entries खोजें:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

उन्हें comment करें, फिर चलाएँ:

```bash
apt update && apt dist-upgrade
```

यदि प्रक्रिया आंशिक रूप से पूरी हुई:

```bash
apt -f install
```

### ZFS अपग्रेड के बाद boot विफल

यदि पुराना BIOS बूट के साथ ZFS मूल फ़ाइल सिस्टम है, तो [ZFS: Switch Legacy-Boot to Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool) देखें। ZFS सिस्टम पर boot का प्रबंधन `proxmox-boot-tool` को करना चाहिए, सीधे GRUB को नहीं, ताकि ZFS सुविधा अपग्रेड के बाद boot बना रहे।

______

## अपग्रेड के बाद checklist

हर node reboot होने के बाद:

- [ ] Browser cache साफ़ करें (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` में 9.x दिखे
- [ ] `uname -r` में 6.14.x या नया दिखे
- [ ] सभी VMs और CTs सही शुरू हों
- [ ] Ceph स्वास्थ्य: `ceph -s` में HEALTH_OK आए
- [ ] UEFI+LVM हो तो `grubx64.efi` का mtime नया हो
- [ ] NVIDIA पासथ्रू हो तो non-production VM जाँचें
- [ ] अपग्रेड के दौरान comment की गई तृतीय-पक्ष भंडार अपडेट करें
- [ ] `/etc/sysctl.conf` की कस्टम सेटिंग्स `/etc/sysctl.d/` में ले जाएँ

______

## अपग्रेड के बाद सत्यापन

अपग्रेड के बाद repository कॉन्फ़िगरेशन, क्लस्टर quorum, storage स्थिति, अतिथि बूट, backups, फ़ायरवॉल नियम और प्रबंधन पहुँच जाँचें। Upgrade पूरा घोषित करने से पहले सिस्टम लॉग देखें। Cluster अनुमति दे तो अलग host पर एक अतिथि पुनर्स्थापना जाँचें।

Version-specific commands के लिए मौजूदा [Proxmox VE प्रशासन गाइड](https://pve.proxmox.com/pve-docs/) और [रिलीज़ नोट्स](https://pve.proxmox.com/wiki/Roadmap) देखें। Target version और backup स्थिति जाँचे बिना पुराने release की command copy न करें।

## संदर्भ

1. [आधिकारिक: Proxmox VE 8 से 9 अपग्रेड](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [आधिकारिक: 8 से 9 अपग्रेड — पूर्व-शर्तें](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [pve8to9-upgrade.sh automation script](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Proxmox VE 9.0 ज्ञात समस्याएँ (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [LVM के कारण GRUB boot failure से recovery, “disk not found” (डिस्क नहीं मिली) त्रुटि](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: Legacy-Boot से Proxmox Boot Tool पर जाएँ](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph Reef से Squid अपग्रेड मार्गदर्शिका](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmox network interface pinning](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Debian 13 Trixie रिलीज़ नोट्स](https://www.debian.org/releases/trixie/releasenotes)
