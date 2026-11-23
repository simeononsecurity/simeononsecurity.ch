---
title: "Proxmox VE 8 থেকে 9 আপগ্রেড নির্দেশিকা"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "পূর্বশর্ত যাচাই, হাতে করা ধাপ, স্বয়ংক্রিয়তা, পরিবর্তন এবং পুনরুদ্ধার নির্দেশনাসহ Proxmox VE 8 থেকে 9-এ আপগ্রেড করুন।"
genre: ["ভার্চুয়ালাইজেশন", "Linux প্রশাসন", "Proxmox", "সার্ভার ব্যবস্থাপনা", "ওপেন সোর্স", "হোমল্যাব"]
tags: ["Proxmox VE 9", "Proxmox আপগ্রেড", "PVE 8 থেকে 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "LVM আপগ্রেড", "ZFS আপগ্রেড", "NVIDIA vGPU", "cgroupv2", "Proxmox স্বয়ংক্রিয়তা", "bash আপগ্রেড স্ক্রিপ্ট", "Proxmox ক্লাস্টার আপগ্রেড", "ইন-প্লেস আপগ্রেড", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "আধুনিক সার্ভার কক্ষের পর্দায় ভার্চুয়াল মেশিনের উজ্জ্বল চিহ্ন দেখা যায়। এক প্রযুক্তিকর্মী গাঢ় নীল যন্ত্রপাতির মাঝে ল্যাপটপে কাজ করছেন, চারপাশে নীল, সবুজ ও বেগুনি আলো।"
coverCaption: "Proxmox VE 8 থেকে 9 আপগ্রেড: স্বয়ংক্রিয় সহায়ক স্ক্রিপ্ট দিয়ে ধাপে ধাপে ইন-প্লেস আপগ্রেড।"
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0 Debian 13 Trixie, kernel 6.14, QEMU 10, LXC 6 এবং ZFS 2.3 নিয়ে প্রকাশিত হয়েছে।** এই নির্দেশিকায় হাতে করা ইন-প্লেস আপগ্রেড এবং এমন একটি স্বয়ংক্রিয় Bash স্ক্রিপ্ট রয়েছে, যা আপনার কনফিগারেশন শনাক্ত করে ভাণ্ডার পরিবর্তন, পরিচিত সমস্যা ও প্রাথমিক যাচাই সামলায়।

## Proxmox VE 9-এ নতুন কী

Proxmox VE 9 (আগস্ট 2025-এ প্রকাশিত) একটি বড় সংস্করণ আপগ্রেড। প্রধান পরিবর্তনগুলো:

| উপাদান | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Debian ভিত্তি** | Bookworm (12) | Trixie (13) |
| **ডিফল্ট kernel** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 চালু করা সম্ভব ছিল) | শুধু cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) এ ডিফল্ট kernel 7.0, QEMU 11, LXC 7 এবং ZFS 2.4 রয়েছে। Ceph Tentacle হলো 9.2-এর ডিফল্ট, Squid-ও পাওয়া যায়। VE 8 Ceph ক্লাস্টার আপগ্রেড করার আগে Squid-এ যাওয়া আলাদা পূর্বশর্ত।

**PVE 9.0+ এর প্রধান নতুন বৈশিষ্ট্য:**
- volume chain-এর মাধ্যমে thick-provisioned LVM-এ VM snapshot (9.1-এ প্রযুক্তিগত preview থেকে production-এ উন্নীত)
- উচ্চ-প্রাপ্যতার সংযোগ-নিয়ম, যা HA group-এর স্থলাভিষিক্ত
- OpenFabric ও OSPF পূর্ণ-জাল Ceph নেটওয়ার্কের জন্য SDN নেটওয়ার্ক কাঠামো
- নতুন মোবাইল ওয়েব ইন্টারফেস (Rust/Yew)
- downtime ছাড়া ZFS RAIDZ যন্ত্র সম্প্রসারণ
- Cluster Resource Scheduler-এর মাধ্যমে dynamic ভারসাম্য বণ্টন (PVE 9.2)
- PVE 9.2-এ SDN নেটওয়ার্ক কাঠামো protocol হিসেবে WireGuard ও BGP
- Debian Trixie-র পরিবর্তনে `/tmp` এখন `tmpfs`; ফাইল নিয়মিত পরিষ্কার হয়

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Proxmox VE 8 ও VE 9-এর পাশাপাশি তুলনামূলক চিত্র, যেখানে kernel, QEMU, LXC, ZFS ও Ceph-এর সংস্করণ পরিবর্তন দেখানো হয়েছে" >}}

______

## শুরু করার আগে: পূর্বশর্ত

**ভাণ্ডার পরিবর্তনের আগে সব শর্ত পূরণ করুন।** [সরকারি upgrade wiki-র পূর্বশর্ত তালিকা](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites) দেখুন।

### 1. অন্তত Proxmox VE 8.4

```bash
pveversion
```

আউটপুটে `pve-manager/8.4.x` বা তার নতুন সংস্করণ থাকতে হবে। না থাকলে চালান:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph-কে Squid (19.x) সংস্করণে আনুন, শুধু সমন্বিত অবকাঠামো ব্যবস্থায়

```bash
ceph --version
```

আউটপুটে সংস্করণ 19.x (Squid) দেখাতে হবে। Reef (18.x) বা Quincy (17.x) থাকলে আগে Ceph আপগ্রেড করুন। প্রতিবার একটি করে বড় সংস্করণে এগোন:

- Quincy (17) → Reef (18) → Squid (19)

*সব Ceph node-এ Squid না চলা পর্যন্ত PVE 9 আপগ্রেড শুরু করবেন না।*

### 3. একই node-এ Proxmox ব্যাকআপ সার্ভার

PBS 3.4 ও PVE 8.4 একই node ব্যবহার করলে [একসঙ্গে ইনস্টল করার নির্দেশনা](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) মেনে দুই আপগ্রেডকে একটি APT operation-এ সমন্বয় করুন। ব্যাকআপ পুনরুদ্ধার করা যায় কি না যাচাই করুন এবং ভাণ্ডার বদলানোর আগে `pve8to9 --full` ও `pbs3to4 --full` চালান। রিপোর্ট করা সমস্যা আগে সমাধান করুন।

### 4. প্রবেশাধিকার

- **অগ্রাধিকার দিন**: IPMI, iKVM বা সরাসরি keyboard দিয়ে console-এ প্রবেশাধিকার রাখুন। service restart হলে SSH সংযোগ বিচ্ছিন্ন হবে।
- **SSH**: সংযোগ বিচ্ছিন্ন হলেও আপগ্রেড চালু রাখতে `tmux` বা `screen` ব্যবহার করুন:
  ```bash
  tmux new -s upgrade
  ```

### 5. ডিস্কের ফাঁকা জায়গা

```bash
df -h /
```

কমপক্ষে **5 GB ফাঁকা** রাখুন, 10 GB বা বেশি হলে ভালো।

### 6. যাচাই করা ব্যাকআপ

এগোনোর আগে সব VM ও container বাইরের storage-এ ব্যাকআপ করুন। পুনরুদ্ধার পরীক্ষা করুন। কার্যকর ব্যাকআপ থাকা বাধ্যতামূলক।

______

## যে পরিবর্তনগুলো জানা দরকার

আপগ্রেডের আগে এগুলো পড়ুন। কয়েকটির জন্য আপগ্রেডের আগে বা পরে ব্যবস্থা নিতে হবে।

### cgroup V1 আর নেই

PVE 9 পুরনো cgroupv1 পরিবেশ একেবারেই সমর্থন করে না। আগে এটি চালু করে থাকলে:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

কমান্ডটি কিছু দেখালে, আপগ্রেডের আগে `/etc/default/grub` থেকে কার্নেল নির্দেশক সরিয়ে `update-grub` চালান।

**container-এর প্রভাব**: systemd 230 বা তার পুরনো সংস্করণে চলা container (CentOS 7, Ubuntu 16.04) PVE 9-এ চালু হবে না। PVE 9-এ যাওয়ার আগে সেসব workload স্থানান্তর করুন। Proxmox VE 8.4-এর বিক্রেতা-সমর্থন 2026 সালের আগস্টে শেষ হয়েছে।

### HA group-এর অবসান

HA group-এর বদলে HA rule এসেছে। ক্লাস্টারের সব node PVE 9-এ গেলে সেগুলো স্বয়ংক্রিয়ভাবে স্থানান্তরিত হয়। হাতে কিছু করতে হয় না, তবে শেষ node আপগ্রেডের পর যাচাই করুন।

### VM.Monitor privilege সরানো হয়েছে

`VM.Monitor` ব্যবহার করা custom role হালনাগাদ করতে হবে। সাধারণ KVM পর্যবেক্ষণ access-এর জন্য `Sys.Audit` ব্যবহার করুন। `pve8to9` script প্রভাবিত role শনাক্ত করে।

### নতুন privilege: VM.Replicate

এখন স্টোরেজ প্রতিলিপি job তৈরি বা সম্পাদনা করতে `/vms/<vmid>`-এ `VM.Replicate` দরকার। প্রয়োজনে custom role বদলান।

### বিশেষ অধিকারপ্রাপ্ত LXC container-এ Sys.Modify দরকার

নতুন বিশেষ অধিকারপ্রাপ্ত container তৈরি করতে এখন `Sys.Modify` দরকার। আগে থেকে থাকা বিশেষ অধিকারপ্রাপ্ত container ইন-প্লেস পুনরুদ্ধার করতে এটি দরকার হয় না।

### systemd-sysctl আর /etc/sysctl.conf পড়ে না

আপগ্রেডের পর `/etc/sysctl.conf`-এর custom setting নীরবে উপেক্ষা করা হবে। reboot-এর আগে সেগুলো `/etc/sysctl.d/<NN>-name.conf`-এ সরান।

```bash
# sysctl.conf-এ কী আছে দেখুন
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp এখন tmpfs

Debian Trixie `/tmp`-কে tmpfs হিসেবে mount করে (RAM-এর সর্বোচ্চ 50%)। system চলার সময় ফাইল নিয়মিত পরিষ্কার হয়। বড় অস্থায়ী ফাইল `/tmp`-এ রাখলে কাজটি `/var/tmp` বা আলাদা mount-এ সরান।

### Veeam ব্যাকআপ ও পুনরুদ্ধারের সামঞ্জস্য {#veeam-ব্যাকআপ-broken-for-qemu-machine-version--100}

আপগ্রেডের আগে আপনার [Veeam ব্যাকআপ & Replication এবং Proxmox plugin build](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html) পরীক্ষা করুন। বর্তমান শর্তে সরকারি Proxmox ISO দিয়ে ইনস্টল করা x86-64 host-এ Proxmox VE 8.2 থেকে 9.2 তালিকাভুক্ত আছে। পুরনো Veeam build-এর সমর্থন-সীমা আলাদা।

বর্তমান [Veeam সীমাবদ্ধতা](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) Snapshots as Volume Chains (SAVC) চালু থাকা LVM storage থেকে VM ব্যাকআপ সমর্থন করে। এতে SAVC-কে Veeam কর্মী file বা Instant Recovery গন্তব্য হিসেবে সমর্থিত বলা হয় না। আলাদা [KB4773 পুনরুদ্ধার সমস্যা](https://www.veeam.com/kb4773) PVE 9-এ SAVC storage-এ পুনরুদ্ধার করা QCOW2 disk-সহ 10-এর আগের QEMU যন্ত্র type-কে প্রভাবিত করে। SAVC নেই এমন গন্তব্য ব্যবহার করুন অথবা নথি অনুযায়ী disk-কে RAW হিসেবে পুনরুদ্ধার করুন। এগুলো পুনরুদ্ধার-এর বিকল্প পদ্ধতি, পুরো fleet-এ যন্ত্রের ধরন আটকে রাখার কারণ নয়। নির্ভর করার আগে নির্ধারিত storage-এ ব্যাকআপ ও পুনরুদ্ধার পরীক্ষা করুন।

### নেটওয়ার্ক interface-এর নাম বদলাতে পারে

Kernel 6.14, 6.8-এর তুলনায় বেশি NIC বৈশিষ্ট্য শনাক্ত করে। কিছু NIC-এর নামের শেষে অতিরিক্ত suffix যুক্ত হয়। আপগ্রেডের আগে `pve-network-interface-pinning` tool সব interface-কে স্থিতিশীল `nicX` নামে স্থির করতে পারে:

```bash
pve-network-interface-pinning --help
```

______

## বিকল্প A: হাতে ইন-প্লেস আপগ্রেড

[pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)-এর সরকারি ধাপগুলো অনুসরণ করুন।

### ধাপ 1: pve8to9 যাচাই তালিকা চালান

```bash
pve8to9 --full
```

এগোনোর আগে প্রতিটি `FAIL` সমাধান করুন। প্রতিটি সমাধানের পর আবার চালান।

### ধাপ 2: চলমান VM স্থানান্তর করুন (ক্লাস্টার হলে)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### ধাপ 3: PVE 8 সম্পূর্ণ হালনাগাদ করুন

```bash
apt update && apt dist-upgrade
# 8.4.1 বা নতুন সংস্করণ দেখাতে হবে
```

### ধাপ 4: Debian ভিত্তি ভাণ্ডার হালনাগাদ করুন

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Bookworm-নির্দিষ্ট বাকি ভাণ্ডার line-গুলো comment করে দিন বা সরান।

### ধাপ 5: PVE 9 প্যাকেজ ভাণ্ডার যোগ করুন

**Enterprise (subscription দরকার):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**No-subscription:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

`apt update && apt policy` দিয়ে যাচাই করুন নতুন ভাণ্ডার error ছাড়া দেখা যায় কি না। এরপর পুরনো `.list` file সরান বা comment করুন।

### ধাপ 6: Ceph প্যাকেজ ভাণ্ডার হালনাগাদ করুন (শুধু সমন্বিত অবকাঠামো ব্যবস্থায়)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

No-subscription ব্যবস্থায় `pve-no-subscription` সহ `http://download.proxmox.com/debian/ceph-squid` ব্যবহার করুন।

### ধাপ 7: প্যাকেজ সূচি নতুন করে নিন

```bash
apt update
```

কোনো error নেই যাচাই করুন।

### ধাপ 8: dist-upgrade চালান

```bash
apt dist-upgrade
```

Storage speed অনুযায়ী এতে 5–60 মিনিট বা আরও বেশি লাগতে পারে। আপগ্রেড চলার সময়:

- **`/etc/issue`**: বর্তমান সংস্করণ রাখুন (নিরাপদ)
- **`/etc/lvm/lvm.conf`**: maintainer-এর সংস্করণ ইনস্টল করুন (প্রস্তাবিত)
- **`/etc/ssh/sshd_config`**: নিজে পরিবর্তন না করলে maintainer-এর সংস্করণ ইনস্টল করুন
- **`/etc/default/grub`**: নিজে পরিবর্তন করলে বর্তমান সংস্করণ রাখুন
- **`/etc/chrony/chrony.conf`**: নিজে পরিবর্তন না করলে maintainer-এর সংস্করণ ইনস্টল করুন

### ধাপ 9: reboot করুন

```bash
reboot
```

PVE 8-এ বিকল্প হিসেবে kernel 6.14 আগে থেকেই ইনস্টল থাকলেও reboot দরকার। PVE 9 toolchain দিয়ে kernel আবার তৈরি হয়।

### ধাপ 10: আপগ্রেড-পরবর্তী কাজ

```bash
# browser cache পরিষ্কার করুন: Ctrl+Shift+R (macOS-এ ⌘+Alt+R)
# ক্লাস্টারের সব node যাচাই করুন:
pvesh get /nodes

# ক্লাস্টারের সব node PVE 9-এ গেলে HA group স্বয়ংক্রিয়ভাবে HA rule-এ যায়
 # error আছে কি না যাচাই করুন
```

______

## বিকল্প B: স্বয়ংক্রিয় script (pve8to9-upgrade.sh)

হাতে করা প্রক্রিয়ায় কনফিগারেশনভেদে অনেক শর্তসাপেক্ষ ধাপ আছে। `pve8to9-upgrade.sh` script সেগুলো স্বয়ংক্রিয়ভাবে করে।

**Script-এর উৎস:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Script কী করে

Script সম্পূর্ণ আপগ্রেড প্রক্রিয়া স্বয়ংক্রিয়ভাবে সামলায়, যার মধ্যে রয়েছে:

| শনাক্তকরণ | কাজ |
|-----------|--------|
| Enterprise বা no-subscription ভাণ্ডার | আগে **সক্রিয় ছিল** এমন ভাণ্ডার type ব্যবহার করে, no-subscription node-এ enterprise চালু করে না |
| Ceph সংস্করণ | Quincy বা Reef হলে থামায়, ধাপে ধাপে Ceph আপগ্রেড নির্দেশনা দেখায় |
| Ceph প্যাকেজ ভাণ্ডার type | বর্তমান ভাণ্ডার type অনুযায়ী নতুন `ceph.sources` লেখে |
| NVIDIA vGPU চালক | চালক < 570.158.02 হলে থামায় (GRID 18.3-এর ন্যূনতম সংস্করণ) |
| NVIDIA GPU সরাসরি সংযোগ | সতর্ক করে, আপগ্রেড-পরবর্তী পরীক্ষার স্মারক তৈরি করে |
| CUDA ভাণ্ডার | URI path-এ `debian12` → `debian13` বদলায় |
| systemd-boot অতিরিক্ত প্যাকেজ | এটি সরায় (dist-upgrade বন্ধ করা Debian-এর ত্রুটি #1110177 সমাধান করে) |
| `sysctl.conf`-এর custom setting | `/etc/sysctl.d/99-pve8to9-migrated.conf`-এ স্থানান্তর করে |
| FRR post-up অচলাবস্থা | reboot-এর আগে `/etc/network/interfaces` ঠিক করে |
| `systemd-journald-audit.socket` | আপগ্রেডে log flood ঠেকাতে বন্ধ করে |
| UEFI + LVM-ভিত্তিক GRUB সমস্যা | `grub-efi-amd64` ইনস্টল করে এবং `/root/`-এ নির্দেশিকা লেখে |
| তৃতীয় পক্ষের `bookworm` ভাণ্ডার | হালনাগাদের স্মারকসহ comment করে |
| `linux-image-amd64` সংঘাত | থাকলে সরিয়ে দেয় |
| LVM স্বয়ংক্রিয় সক্রিয়করণ | আপগ্রেডের আগে ও পরে স্থানান্তর স্ক্রিপ্ট চালায় |
| Proxmox ব্যাকআপ সার্ভার | `pbs3to4 --full` যাচাই চালায়, Trixie-এর জন্য PBS ভাণ্ডার হালনাগাদ করে |
| ZFS-এর মূল পার্টিশন | শনাক্ত করে ও নথিবদ্ধ করে (বিশেষ ব্যবস্থা লাগে না) |

সব পরিবর্তন `/var/log/pve8to9-upgrade-<timestamp>.log`-এ নথিবদ্ধ হয়। APT ভাণ্ডার ব্যাকআপ `/root/pve8to9-apt-backups/`-এ লেখা হয়। `/etc/apt/sources.list.d/`-এ `.bak` হিসেবে কখনও রাখবেন না, এতে web UI-তে "invalid extension" (এক্সটেনশনটি অবৈধ) error হবে.

### ইনস্টলেশন ও ব্যবহার

```bash
# script ডাউনলোড করুন
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# executable করুন
chmod +x pve8to9-upgrade.sh

# চালানোর আগে পড়ুন (root হিসেবে চালানোর আগে সবসময় script পড়ুন)
less pve8to9-upgrade.sh
```

**চালানোর ধরন:**

```bash
# সম্পূর্ণ interactive mode (প্রস্তাবিত)
./pve8to9-upgrade.sh

# নিরাপদ, ধ্বংসাত্মক নয় এমন সব সংশোধন স্বয়ংক্রিয়ভাবে অনুমোদন করুন
./pve8to9-upgrade.sh --yes

# dry run: কোনো পরিবর্তন প্রয়োগ না করে সব দেখান
./pve8to9-upgrade.sh --dry-run

# pve8to9 --full প্রাথমিক যাচাই এড়িয়ে যান (প্রস্তাবিত নয়)
./pve8to9-upgrade.sh --skip-preflight
```

*SSH দিয়ে যুক্ত হলে `tmux` বা `screen`-এর মধ্যে চালান।*

### Script-এর output দেখতে কেমন

এগোনোর আগে script কনফিগারেশনের সারাংশ দেখায়:

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

### Script-এর বাধ্যতামূলক নিরাপত্তা যাচাই

নিচের যেকোনো শর্ত সত্য হলে script **চালিয়ে যেতে অস্বীকার করবে**:

- kernel command line-এ cgroup V1 স্পষ্টভাবে চালু আছে
- Ceph এখনও Quincy (17.x) বা Reef (18.x); সঠিক Ceph আপগ্রেড command দেখায়
- NVIDIA vGPU চালক 570 (GRID 18.3)-এর নিচে
- PVE সংস্করণ 8.4-এর নিচে

প্রতিটি বাধার ক্ষেত্রে script আবার চালানোর আগে ঠিক করার command দেখায়।

______

## পরিচিত আপগ্রেড সমস্যা

### UEFI mode-এ LVM থেকে GRUB boot হয় না

**প্রভাবিত হয়**: PVE 7.x থেকে আপগ্রেড করা, UEFI mode-এ boot করা এবং LVM-এ root থাকা system

```bash
# সমাধান (আপগ্রেডের পর চালু system-এ চালান):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

`pve8to9-upgrade.sh` script UEFI+LVM শনাক্ত করে নিজেই এটি ইনস্টল করে। এটি `/root/GRUB-RECOVERY-CHEATSHEET.txt`-এ পুনরুদ্ধার নির্দেশিকাও লেখে।

**node ইতিমধ্যে আটকে গেলে** `grub rescue>` অথবা "disk 'lvmid/...' not found" (ডিস্ক পাওয়া যায়নি) বার্তায়:

1. PVE ISO থেকে boot করুন → Advanced → **Rescue Boot**
2. অথবা সরকারি wiki-র [GRUB failure থেকে পুনরুদ্ধার, LVM অংশ](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) অনুসরণ করুন

### systemd-boot অতিরিক্ত প্যাকেজ dist-upgrade থামায়

PVE 8.1–8.4 ISO দিয়ে ইনস্টল করা সব system-এ `systemd-boot` meta-package স্বয়ংক্রিয়ভাবে ইনস্টল হয়েছিল। Trixie-তে এর hook অন্য package upgrade-এর সময় চলে এবং ESP mount না থাকলে মাঝপথে `dist-upgrade` থামাতে পারে (Debian-এর ত্রুটি #1110177)।

```bash
# dist-upgrade-এর আগে এটি সরান:
apt remove systemd-boot
# systemd-boot-efi বা systemd-boot-tools সরাবেন না, এগুলো থাকবে
```

`pve8to9-upgrade.sh` script এটি স্বয়ংক্রিয়ভাবে সামলায় এবং কারণ বিস্তারিত ব্যাখ্যা করে।

### Kernel 6.14-এ PCI সরাসরি সংযোগ মাঝে মাঝে কাজ করে না

কিছু ব্যবহারকারী জানিয়েছেন, PCI সরাসরি সংযোগ-সহ VM kernel 6.14-এ চালু হয় না। আপনার ক্ষেত্রে হলে:

```bash
# সাময়িকভাবে পুরনো kernel pin করুন:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### reboot-এর সময় Ceph full-mesh setup আটকে যায়

আপনার `/etc/network/interfaces`-এ এটি থাকলে:

```
post-up /usr/bin/systemctl restart frr.service
```

এটি বদলে লিখুন:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

reboot-এর **আগে** এটি করুন। Script নিজে থেকে এই pattern শনাক্ত করে ঠিক করে।

### LVM thin pool মেরামত দরকার

কিছু system-এ আপগ্রেডের পর:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

সমাধান:

```bash
lvconvert --repair pve/data
```

### NVIDIA vGPU-র ন্যূনতম চালক সংস্করণ

আপগ্রেডের আগে অন্তত **চালক 570.158.02** (GRID 18.3) থাকতে হবে। পুরনো চালক kernel 6.x-এর সঙ্গে সামঞ্জস্যপূর্ণ নয়।

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## ক্লাস্টার আপগ্রেডের ক্রম

একবারে একটি node আপগ্রেড করুন। পরেরটি শুরুর আগে প্রতিটি node সুস্থ আছে যাচাই করুন।

```bash
# প্রতিটি node আপগ্রেডের আগে cluster health যাচাই করুন:
pvecm status
# Ceph চালু থাকলে
```

**আংশিক আপগ্রেডের সময় migration নিয়ম:**

- PVE 8 থেকে PVE 9-এ VM/CT: সবসময় কাজ করে
- PVE 9 থেকে PVE 8-এ VM/CT: সাধারণত সমর্থিত নয়

সব node PVE 9-এ যাওয়ার পর HA group স্বয়ংক্রিয়ভাবে HA affinity rule-এ রূপান্তরিত হয়। error দেখুন:

```bash
journalctl -eu pve-ha-crm
```

______

## সমস্যা সমাধান

### আপগ্রেড থেমে গেলে

এটি দেখলে:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

এক বা একাধিক package আপগ্রেড করা যাচ্ছে না, কারণ এখনও Bookworm ভাণ্ডার কনফিগার করা আছে। অবশিষ্ট Bookworm entry খুঁজুন:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

সেগুলো comment করে এরপর চালান:

```bash
apt update && apt dist-upgrade
```

আংশিকভাবে শেষ হলে:

```bash
apt -f install
```

### ZFS আপগ্রেডের পর boot ব্যর্থ

পুরনো BIOS boot-সহ ZFS-এর মূল পার্টিশন ব্যবহার করলে [ZFS: Legacy-Boot থেকে Proxmox Boot Tool-এ যান](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool) দেখুন। ZFS বৈশিষ্ট্য আপগ্রেডের পরও boot ঠিক রাখতে ZFS system-এ GRUB নয়, `proxmox-boot-tool`-কে boot পরিচালনা করতে হবে।

______

## আপগ্রেড-পরবর্তী যাচাই তালিকা

প্রতিটি node reboot করার পর:

- [ ] browser-এর cache পরিষ্কার করুন (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion`-এ 9.x দেখায়
- [ ] `uname -r`-এ 6.14.x বা নতুন সংস্করণ দেখায়
- [ ] সব VM ও CT সঠিকভাবে চালু হয়
- [ ] Ceph-এর স্বাস্থ্য: `ceph -s`-এ HEALTH_OK দেখায়
- [ ] UEFI+LVM হলে: `grubx64.efi`-এর mtime সাম্প্রতিক যাচাই করুন
- [ ] NVIDIA GPU সরাসরি সংযোগ থাকলে: non-production VM পরীক্ষা করুন
- [ ] আপগ্রেডে comment করা তৃতীয় পক্ষের ভাণ্ডার হালনাগাদ করুন
- [ ] `/etc/sysctl.conf`-এর custom setting `/etc/sysctl.d/`-এ সরান

______

## আপগ্রেড-পরবর্তী যাচাই

আপগ্রেডের পর ভাণ্ডার কনফিগারেশন, ক্লাস্টারের ঐকমত্য, storage অবস্থা, অতিথি system চালু হওয়া, ব্যাকআপ, firewall rule এবং ব্যবস্থাপনা প্রবেশাধিকার পরীক্ষা করুন। আপগ্রেড সম্পন্ন বলার আগে system log পর্যালোচনা করুন। ক্লাস্টার সমর্থন করলে আলাদা host-এ একটি অতিথি system পুনরুদ্ধার পরীক্ষা করুন।

সংস্করণ-নির্দিষ্ট command-এর জন্য বর্তমান [Proxmox VE প্রশাসন নির্দেশিকা](https://pve.proxmox.com/pve-docs/) ও [release note](https://pve.proxmox.com/wiki/Roadmap) দেখুন। target সংস্করণ ও ব্যাকআপ অবস্থা যাচাই না করে পুরনো release-এর command ব্যবহার করবেন না।

## তথ্যসূত্র

1. [সরকারি: Proxmox VE 8 থেকে 9 আপগ্রেড](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [সরকারি: 8 থেকে 9 আপগ্রেডের পূর্বশর্ত](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [pve8to9-upgrade.sh স্বয়ংক্রিয় script](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Proxmox VE 9.0-এর পরিচিত সমস্যা (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [GRUB failure থেকে পুনরুদ্ধার, LVM "disk not found" (ডিস্ক পাওয়া যায়নি) error](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: Legacy-Boot থেকে Proxmox Boot Tool-এ যান](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph Reef থেকে Squid আপগ্রেড নির্দেশিকা](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmox Network Interface Pinning](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Debian 13 Trixie release note](https://www.debian.org/releases/trixie/releasenotes)
