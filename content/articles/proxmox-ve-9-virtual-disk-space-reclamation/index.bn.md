---
title: "Proxmox VE 9: ভার্চুয়াল ডিস্কের ব্যবহার কমিয়ে জায়গা ফেরত নিন"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Proxmox VE 9-এ VM ও LXC কনটেইনারের স্টোরেজ ব্যবহার কমান। ফরম্যাট ও ব্যাকএন্ড তুলনা করুন, discard চালু করুন, trim চালান এবং জায়গা ফেরত নেওয়ার আগে snapshot পরীক্ষা করুন।"
genre: ["ভার্চুয়ালাইজেশন", "Linux প্রশাসন", "Proxmox VE প্ল্যাটফর্ম", "স্টোরেজ", "হোম ল্যাব"]
tags: ["Proxmox VE 9 ডিস্কের জায়গা", "Proxmox-এর পাতলা বরাদ্দ", "Proxmox discard বিজ্ঞপ্তি", "Proxmox TRIM কমান্ড", "Proxmox-এ Windows ReTrim", "Proxmox-এ Linux fstrim", "Proxmox LXC ডিস্ক ব্যবহার", "Proxmox-এ LVM পাতলা বরাদ্দ", "Proxmox-এ ZFS sparse zvol", "Proxmox Ceph RBD ব্লক ডিভাইস", "Proxmox qcow2 ফরম্যাট", "Proxmox raw ডিস্ক", "Proxmox snapshot", "ভার্চুয়াল ডিস্কের জায়গা ফেরত", "Proxmox স্টোরেজের ধরন", "VirtIO SCSI নিয়ন্ত্রক", "Proxmox zero-write শনাক্তকরণ", "Proxmox ব্যাকআপ স্টোরেজ"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "তীর দিয়ে যুক্ত দুটি ব্লক-গ্রিড ভার্চুয়াল ডিস্কের ব্যবহৃত ব্লক এবং স্টোরেজ পুলের খালি ক্ষমতা দেখায়।"
coverCaption: "গেস্ট থেকে ফাইল মুছে ফেলা, discard পাঠানো এবং স্টোরেজে জায়গা ফেরত পাওয়া আলাদা ধাপ।"
---

**গেস্টের ফাইল সিস্টেম ছোট হলেই Proxmox-এ স্টোরেজ ব্যবহার কমে না।** হোস্টে জায়গা খালি করতে পাতলা বরাদ্দ সমর্থিত ডিস্ক, VM-এর জন্য কার্যকর discard পথ এবং স্ন্যাপশট-এ আটকে থাকা ব্লকমুক্ত ব্যাকএন্ড দরকার। এই নির্দেশিকায় Proxmox VE 9 VM ও LXC কনটেইনারের সেটিং এবং পরীক্ষা বর্ণনা করা হয়েছে।

<!--more-->

## মূল কথা

- **আগে ব্যাকিং স্টোরেজ বাছুন।** ভার্চুয়াল ডিস্কের ঘোষিত আকার হোস্টে বরাদ্দ জায়গা থেকে আলাদা হবে কেবল তখনই, যখন ইমেজ ফরম্যাট বা ব্যাকএন্ড পাতলা বরাদ্দ সমর্থন করে।
- **VM-এ discard চালু করে গেস্টের ভেতরে trim চালান।** Windows ReTrim এবং Linux `fstrim` ভার্চুয়াল ডিস্ক দিয়ে অব্যবহৃত ব্লকের অনুরোধ পাঠায়।
- **স্ন্যাপশট এবং ব্যাকআপ আলাদা করে পরীক্ষা করুন।** কোনো স্ন্যাপশট-এ উল্লেখ থাকলে পুরোনো ব্লক বরাদ্দ থাকে। ব্যাকআপ ফাইল এবং PBS তথ্য খণ্ড নিজস্ব retention নিয়ম মেনে চলে।
- **LXC মাউন্ট-কে ধরন অনুযায়ী দেখুন।** পরিচালিত rootfs ও মাউন্ট-point ভলিউম, bind মাউন্ট এবং device মাউন্ট-এর মালিকানা ও ব্যাকআপ আচরণ আলাদা।

## শুরু করার আগে

আপনার দরকার **Proxmox VE 9 প্রশাসক প্রবেশাধিকার**, প্রতিটি প্রভাবিত গেস্টের যাচাইকৃত ব্যাকআপ এবং কাজের জন্য পুল-এ যথেষ্ট খালি জায়গা। সেটিং বদলানোর আগে গেস্ট ID, ডিস্ক বাস, ভলিউম ID, স্টোরেজ ID, স্ন্যাপশট এবং বর্তমান বরাদ্দ লিখে রাখুন। পুনরুদ্ধার যাচাই করতে [VM পুনরুদ্ধার অনুশীলন](/articles/proxmox-vm-backup-restore-drill/) ব্যবহার করুন।

**আনুমানিক সময়:** প্রতি গেস্টে ২০–৬০ মিনিট, বড় trim বা পরিষ্কারের অতিরিক্ত সময় বাদে। **কঠিনতা:** মাঝারি। কম ঝুঁকির একটি VM দিয়ে শুরু করে আগে ও পরের স্টোরেজ ব্যবহার তুলনা করুন।

> **সতর্কতা:** পাতলা পুল পূর্ণ হলে গেস্টে I/O ত্রুটি হয় এবং ফাইল সিস্টেম নষ্ট হওয়ার ঝুঁকি থাকে। পুল-এর খালি ডেটা ও মেটাডেটা জায়গা না দেখে অতিরিক্ত ক্ষমতা বরাদ্দ করবেন না। [Proxmox স্টোরেজ ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## বরাদ্দের ধাপগুলো অনুসরণ করুন

**মুছে ফেলা**, **discard** এবং **জায়গা ফেরত পাওয়া** আলাদা স্তরে ঘটে। গেস্ট ফাইল মুছে ফাইল সিস্টেমের ব্লক খালি চিহ্নিত করে। ফাইল সিস্টেম সেসব ব্লকের জন্য TRIM বা UNMAP পাঠায়। ভার্চুয়াল ডিস্কে discard চালু থাকলে QEMU অনুরোধটি এগিয়ে দেয়। ফরম্যাট ও পুল সমর্থন করলে ব্যাকএন্ড ভৌত বরাদ্দ ছেড়ে দেয়। [Proxmox VM ডিস্ক ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| স্তর | কী পরীক্ষা করবেন | উপযোগী প্রমাণ |
|---|---|---|
| **গেস্ট ফাইল** | ফাইল সিস্টেমের খালি জায়গা | Windows ভলিউম-এর বৈশিষ্ট্য বা Linux `df -h` |
| **ভার্চুয়াল ডিস্ক** | বাস, discard, SSD অনুকরণ, ইমেজ ফরম্যাট | VM-এর **Hardware** ট্যাব বা `qm config VMID` |
| **PVE ভলিউম** | মালিক এবং কনফিগার করা আকার | স্টোরেজের **Content** ট্যাব বা `pvesm list STORAGE_ID` |
| **স্টোরেজ পুল** | খালি ডেটা, মেটাডেটা এবং আটকে থাকা ব্লক | `pvesm status` ও ব্যাকএন্ডভিত্তিক টুল |

**১০০ GiB ভার্চুয়াল ডিস্ক ক্ষমতার সীমা, ১০০ GiB বরাদ্দের নিশ্চয়তা নয়।** আবার গেস্টে ২০ GiB ব্যবহার দেখালেও হোস্টে ২০ GiB ব্যবহারের প্রমাণ হয় না। মেটাডেটা, স্ন্যাপশট, ব্যাকআপ কপি এবং আগে লেখা ব্লক হিসাব বদলে দেয়। [Proxmox স্টোরেজ ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## ডিস্ক ফরম্যাট তুলনা করুন

**কোন ইমেজ ফরম্যাট Proxmox দেবে তা স্টোরেজ ব্যাকএন্ড ঠিক করে।** ZFS zvol এবং Ceph RBD ভার্চুয়াল raw ডিস্ক ব্যবহার করে। LVM সাধারণত raw ব্যবহার করে, তবে Proxmox VE 9-এর নিচে বর্ণিত ভলিউম-chain ব্যতিক্রম আছে। directory এবং NFS-এর মতো ফাইল ব্যাকএন্ড raw বা qcow2 সমর্থন করে। Raw নিজে পাতলা বরাদ্দ বা স্ন্যাপশট দেয় না। অন্তর্নিহিত স্টোরেজকে এসব সুবিধা দিতে হয়। Qcow2 ইমেজ স্তরে লেখার সময় কপি করে বরাদ্দ এবং স্ন্যাপশট দেয়। [Proxmox VM ডিস্ক ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| ফরম্যাট | বরাদ্দের পদ্ধতি | জায়গার বিনিময় |
|---|---|---|
| **ফাইল স্টোরেজে qcow2** | লেখার সময় qcow2 cluster বরাদ্দ করে | ইমেজ মেটাডেটা এবং স্ন্যাপশট chain জায়গা নেয় |
| **ফাইল স্টোরেজে raw ফাইল** | সমর্থন থাকলে ফাইল সিস্টেমের sparse-ফাইল আচরণ | Raw একা পাতলা বরাদ্দ বা স্ন্যাপশট দেয় না |
| **Raw ব্লক ভলিউম** | পাতলা বরাদ্দের LVM, ZFS, Ceph RBD বা অন্য ব্যাকিং স্টোরেজ | পুল বরাদ্দ ও স্ন্যাপশট ব্যাকএন্ডের ওপর নির্ভর করে |

**Proxmox VE 9 মোটা LVM-এ স্ন্যাপশট-এর বিশেষ মোড আছে।** `snapshot-as-volume-chain` মোটা LVM যৌক্তিক ভলিউম-এর মধ্যে qcow2 ভিত্তি সম্পর্ক ব্যবহার করে। এটি qcow2-এর অভ্যন্তরীণ স্ন্যাপশট ব্যবহার করে না। বিকল্পটি শুধু নতুন VM ডিস্কে কাজ করে এবং বর্তমান Proxmox ডকুমেন্টেশনে প্রযুক্তিগত preview হিসেবে আছে। PVE প্রতিটি স্ন্যাপশট-কে পুরো বরাদ্দ দেখায়। SAN-এ প্রকৃত বরাদ্দ কম হবে কেবল যদি ব্যাকিং স্টোরেজ পাতলা বরাদ্দ ও discard সমর্থন করে। [Proxmox LVM স্টোরেজ ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**শুধু `.raw` extension দেখে ডিস্ক convert করবেন না।** আগে স্টোরেজ plugin এবং বরাদ্দ করা ব্লক পরীক্ষা করুন। `local-lvm`-এর raw ডিস্কের বরাদ্দ সাধারণ directory স্টোরেজের পুরোপুরি বরাদ্দ raw ফাইলের মতো নয়।

## স্টোরেজের ধরন তুলনা করুন

Proxmox **ফাইল স্টোরেজ** এবং **ব্লক স্টোরেজ** আলাদা রাখে। স্টোরেজ plugin স্ন্যাপশট, clone, ভাগাভাগি এবং প্রতিটি পুল-এ গ্রহণযোগ্য content-এর ধরনও নিয়ন্ত্রণ করে। কোনো ফরম্যাট বা বৈশিষ্ট্যের ওপর নির্ভর করার আগে **Datacenter > স্টোরেজ**-এর entry পরীক্ষা করুন। [Proxmox স্টোরেজ ধরন তালিকা](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| স্টোরেজ | VM ডিস্কের আচরণ | জায়গা ফেরত যাচাই |
|---|---|---|
| **Directory, ext4, XFS** | Raw বা qcow2 ফাইল | `du`-তে বরাদ্দ byte-এর সঙ্গে ইমেজের ভার্চুয়াল আকার তুলনা করুন। অন্য স্টোরেজ স্তর স্ন্যাপশট দিলে সেগুলো পরীক্ষা করুন। |
| **NFS, CIFS** | ভাগ করা স্টোরেজে raw বা qcow2 ফাইল | সার্ভারে বরাদ্দ জায়গা দেখুন। গেস্ট trim-এর ফল সার্ভারে জায়গা কমার প্রমাণ নয়। |
| **LVM-এর পাতলা বরাদ্দ (`local-lvm`)** | শুধু স্থানীয় পাতলা raw যৌক্তিক ভলিউম | `lvs` দিয়ে পাতলা পুল-এর ডেটা ও মেটাডেটা শতাংশ দেখুন। |
| **LVM thick** | Raw LV বা VE 9 qcow2 ভলিউম chain | গেস্টে ফাইল মুছলে স্থির LV reservation কমে না। SAN-এর পাতলা বরাদ্দ আলাদা পরীক্ষা করুন। |
| **ZFS ভলিউম (`local-zfs`)** | Raw zvol বা container subvolume | `sparse`, dataset বৈশিষ্ট্য, পুল ব্যবহার ও স্ন্যাপশট পরীক্ষা করুন। |
| **Ceph RBD** | ভাগ করা স্টোরেজে পাতলা `raw RBD` ইমেজ | Ceph পুল-এর ক্ষমতা, ইমেজ ব্যবহার, স্ন্যাপশট ও discard পরীক্ষা করুন। |
| **Btrfs** | Raw ইমেজ-এর জন্য Btrfs subvolume-সহ ফাইলভিত্তিক ভলিউম | PVE Btrfs plugin-কে প্রযুক্তিগত preview ধরুন এবং স্ন্যাপশট ও ফাইল সিস্টেম ব্যবহার দেখুন। |

**অন্য স্টোরেজ plugin-এর কাজ আলাদা।** CephFS ভাগ করা ফাইল স্টোরেজ দেয়। iSCSI এবং Fibre Channel ভাগ করা ব্লক ডিভাইস দেয়, যেগুলো প্রায়ই LVM দিয়ে VM ভলিউম-এ ভাগ করা হয়। `ZFS over iSCSI` দূরবর্তী ZFS-ভিত্তিক ব্লক স্টোরেজ ব্যবহার করে। Proxmox ব্যাকআপ সার্ভার (PBS) ব্যাকআপ রাখে, সক্রিয় VM ডিস্ক নয়। `images`, `rootdir`, `backup` বা `iso` ডেটা রাখার আগে চালু **Content** ধরন পরীক্ষা করুন। [Proxmox স্টোরেজ ধরন তালিকা](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ফাইল স্টোরেজের বরাদ্দ flag ডিস্ক তৈরির সময় গুরুত্বপূর্ণ।** সমর্থন থাকলে স্টোরেজ-level `format` `raw`, `qcow2` বা `vmdk` বেছে নেয়। Raw ও qcow2 ফাইলে `preallocation` হিসেবে `off`, `metadata`, `falloc` বা `full` নেওয়া যায়। ডিফল্ট `metadata`, যা raw-এর জন্য `off` হিসেবে ধরা হয়। `full` আগেই ফাইলের জায়গা reserve করে, তাই শুরুতে কম জায়গা লাগার সুবিধা থাকে না। বড় ডিস্ক তৈরির আগে স্টোরেজ কনফিগারেশন দেখুন। `shared` flag শুধু আগে থেকে থাকা ভাগ করা প্রবেশাধিকার ঘোষণা করে। এটি স্থানীয় স্টোরেজ ভাগ করা করে না। [Proxmox-এর সাধারণ স্টোরেজ বৈশিষ্ট্য](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` পাতলা zvol তৈরির স্টোরেজ সেটিং।** Sparse zvol না হলে, কনফিগার করা ভলিউম আচরণ অনুযায়ী জায়গা reserve হয়। বিদ্যমান ব্যবস্থা বদলানোর আগে প্রকৃত স্টোরেজ কনফিগারেশন ও পুল পরীক্ষা করুন। [Proxmox ZFS স্টোরেজ ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory স্টোরেজে দ্বিতীয়বার যাচাই দরকার।** qcow2 ফাইলের যৌক্তিক দৈর্ঘ্য গেস্টের দেখা ভার্চুয়াল ধারণক্ষমতা নয়। `du -h` ইমেজে বরাদ্দ ফাইল সিস্টেম ব্লক দেখায়। `ls -lh` ফাইলের যৌক্তিক দৈর্ঘ্য দেখায়। বন্ধ VM-এর জন্য `qemu-img info` ভার্চুয়াল ধারণক্ষমতা এবং হোস্টের ডিস্ক আকার জানায়। NFS-এ শেষ সিদ্ধান্তের জন্য সার্ভারের হিসাব ব্যবহার করুন। [QEMU `qemu-img` রেফারেন্স](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS-এ আরেকটি বরাদ্দ সীমা আছে।** qcow2 নিজের ফাইলে খালি cluster পুনরায় ব্যবহার করলেই NFS সার্ভার ফাইলের ব্লক ছেড়ে দেয় না। Hole punching-এর জন্য client, আলোচিত protocol, সার্ভার এবং সার্ভার-এর ফাইল সিস্টেমের সমর্থন লাগে। NFSv4.2-এ `DEALLOCATE` সংজ্ঞায়িত, কিন্তু সংস্করণ নম্বর একা সার্ভার জায়গা ফেরত দিয়েছে প্রমাণ করে না। আলোচিত NFS মাউন্ট পরীক্ষা করে সার্ভারে বরাদ্দ মাপুন। [NFSv4.2 `DEALLOCATE` নির্দেশনা](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## VM ডিস্কের flag সেট করুন

Proxmox ইন্টারফেসে **VM > Hardware > Hard ডিস্ক > Edit** খুলুন। ডিস্কের bus এবং advanced বিকল্প দেখুন। নিচের flag-গুলো বরাদ্দে প্রভাব ফেলে বা কোনো optimization কাজে লাগবে কি না বোঝায়। [অফিশিয়াল `qm` বিকল্প নির্দেশিকা](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)-এ bus অনুযায়ী সমর্থন দেওয়া আছে।

| Bus | জায়গা-সংক্রান্ত বাছাই |
|---|---|
| **IDE** | পুরোনো সিস্টেমের সঙ্গে সামঞ্জস্য। গেস্টে নতুন ড্রাইভার না থাকলেই ব্যবহার করুন। |
| **SATA** | ব্যাপকভাবে সমর্থিত emulation। জায়গা ফেরতের ওপর নির্ভর করার আগে গেস্ট trim ও ডিস্ক বিকল্প যাচাই করুন। |
| **VirtIO SCSI-সহ SCSI** | discard এবং প্রতি-ডিস্ক সেটিংয়ের পছন্দের আধুনিক পথ। Windows-এ VirtIO ড্রাইভার দরকার। |
| **VirtIO ব্লক** | Paravirtualized ডিস্ক। Linux discard-এর জন্য kernel 5.0 বা নতুন চাই। SSD অনুকরণ নেই। |

| সেটিং | প্রভাব | নির্দেশনা |
|---|---|---|
| **discard চালু (`on`)** | গেস্ট TRIM বা UNMAP এগিয়ে দেয় | সমর্থিত পাতলা backend-এ গেস্ট থেকে জায়গা ফেরানোর জন্য দরকার। ডিফল্ট `ignore` এগিয়ে দেওয়া আটকায়। |
| **SSD অনুকরণ `ssd=1`** | গেস্টকে ডিস্ক SSD হিসেবে দেখায় | কিছু গেস্ট trim পাঠাতে এই পরিচয় চায়। এতে ভৌত স্টোরেজ দ্রুত হয় না। VirtIO ব্লক-এ flag নেই। |
| **শূন্য লেখা শনাক্তকরণ `detect_zeroes=1`** | শূন্য লেখার শনাক্ত করে অনুকূল করার চেষ্টা | ঐচ্ছিক I/O optimization। গেস্ট trim-এর বিকল্প নয় এবং জায়গা ফেরার নিশ্চয়তা দেয় না। |
| **Bus: SCSI / VirtIO `SCSI single`** | VirtIO নিয়ন্ত্রক দিয়ে SCSI ডিস্ক দেয় | আধুনিক Windows ও Linux গেস্টের জন্য ব্যবহারিক পছন্দ। Windows VirtIO ড্রাইভার ইনস্টল করুন। |
| **Bus: VirtIO ব্লক** | VirtIO ব্লক ডিভাইস ব্যবহার করে | Linux discard-এর জন্য kernel 5.0 বা নতুন চাই। SSD অনুকরণ নেই। |
| **I/O thread `iothread=1`** | ড্রাইভ I/O আলাদা thread-এ দেয় | VirtIO ব্লক বা VirtIO `SCSI single` controller-এ SCSI-এর সঙ্গে ব্যবহার করুন। এটি কর্মক্ষমতার সেটিং, জায়গা ফেরানোর সুইচ নয়। |
| **ক্যাশ ও AIO** | I/O buffering এবং asynchronous I/O বদলায় | workload ও backend অনুযায়ী ঠিক করুন। কোনোটিই ডিস্ক ছোট করে না। |
| **ব্যাকআপ `backup=0`** | VM ব্যাকআপ থেকে ডিস্ক বাদ দেয় | ব্যাকআপের পরিধি কমায় এবং VM recovery থেকে ডিস্কের ডেটা সরায়। আলাদা ব্যাকআপ নথিভুক্ত করুন। |
| **Replicate `replicate=0`** | স্টোরেজ replication থেকে ডিস্ক বাদ দেয় | replicated ডেটা কমায় এবং replica থেকে ডিস্ক বাদ দেয়। |

**অন্য drive বিকল্প আচরণ বোঝায়, জায়গা ফেরানো নয়।** একাধিক ইমেজ ফরম্যাটের backend-এ ডিস্ক বরাদ্দের সময় `format` প্রযোজ্য। `size` ভার্চুয়াল ধারণক্ষমতা, বরাদ্দ byte নয়। `ro=1` ডিস্ককে শুধু-পাঠযোগ্য করে। `snapshot=1` QEMU-এর অস্থায়ী স্ন্যাপশট মোড চালু করে, যা VM বন্ধ হলে ডিস্ক পরিবর্তন বাতিল করে। এটি Proxmox VM স্ন্যাপশট-এ ডিস্ক যোগ করার সুইচ নয়। স্থায়ী ডেটায় এটি এড়িয়ে চলুন। `backup=0` বা `replicate=0` ব্যবহারের আগে পুনরুদ্ধার কভারেজ পরীক্ষা করুন। [Proxmox VM ডিস্ক বিকল্প](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**বিদ্যমান drive-এর ওপর সংক্ষিপ্ত `qm set --scsi0` string পেস্ট করবেন না।** **`qm config VMID`** দেখে সম্পাদনার সময় পুরো ভলিউম ID এবং আগের বিকল্প বজায় রাখুন। সংক্ষিপ্ত ড্রাইভ বরাদ্দ অন্য ডিস্ক সেটিং মুছে দিতে পারে। প্রতিবার পরিবর্তনের পর ইন্টারফেসে সেভ করা বিকল্প পরীক্ষা করুন।

```bash
qm config 100
pvesm status
```

`100` উদাহরণ VM ID। **নতুন** 64 GiB SCSI ডিস্কের ক্ষেত্রে, বিদ্যমান VM-এ **VirtIO `SCSI single`** controller এবং গেস্টে দরকারি ড্রাইভার থাকলে, এই কমান্ড বরাদ্দ syntax দেখায়। নিজের VM ID ও স্টোরেজ ID বসান।

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**উদাহরণ চালানোর আগে `scsi0` আগে থেকেই আছে কি না দেখুন।** কমান্ড-টি ওই slot বদলায়। বিদ্যমান ডিস্কে সঠিক বিকল্পের স্ট্রিং অক্ষত রাখা সহজ হলে ইন্টারফেস ব্যবহার করুন। [Proxmox `qm` কমান্ড নির্দেশিকা](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) দেখুন।

## অতিথি সিস্টেমের ফাইল পরিষ্কার করুন

**আগে গেস্টের ফাইল মুছে জায়গা খালি করুন।** Windows স্টোরেজ সেটিং, অস্থায়ী ফাইল, পুরোনো installer, application ক্যাশ এবং রিসাইকেল বিন পরীক্ষা করুন। Database ও container runtime তাদের নিজস্ব ইন্টারফেস দিয়ে পরিষ্কার করুন। শুধু বরাদ্দ কমাতে সক্রিয় অ্যাপ্লিকেশনের ডেটা মুছলে ডেটা হারানোর ঝুঁকি থাকে।

**নিশ্চিত করুন ভলিউম discard-সমর্থিত ভার্চুয়াল ডিস্ক ব্যবহার করে**, তারপর Windows VM-এ উচ্চ অনুমতিসহ PowerShell সেশন চালু করুন:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` মানে Windows রিপোর্ট করা ফাইল সিস্টেমে delete notification চালু করেছে। **ReTrim** বর্তমানে অব্যবহৃত ভলিউম অঞ্চলের trim অনুরোধ আবার পাঠায়। কমান্ড সফল হওয়া মানে গেস্ট অপারেশন পাঠিয়েছে, হোস্ট কত byte ফেরত পেয়েছে তা নয়। কাজ শেষে হোস্ট পরীক্ষা করুন। [Microsoft `Optimize-Volume` নির্দেশিকা](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) এবং [Proxmox VM ডিস্ক ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**QEMU গেস্ট এজেন্ট-কে TRIM ভেবে ভুল করবেন না।** Agent গেস্ট নিয়ন্ত্রণ এবং ব্যাকআপ সামঞ্জস্যের সুবিধা দেয়। ফাইল সিস্টেমের delete notification ভার্চুয়াল ডিস্ক পথ দিয়ে যায়। শুধু agent ইনস্টল করলে ব্লক ফেরত আসে না। [Proxmox VM গেস্ট এজেন্ট ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## অতিথি ফাইল সিস্টেমের অব্যবহৃত ব্লক চিহ্নিত করুন

**Trim-এর আগে ব্লক পথ এবং ফাইল সিস্টেম পরীক্ষা করুন।** আধুনিক distribution প্রায়ই নিয়মিত `fstrim.timer` চালায়। এর অবস্থা দেখে অপ্রয়োজনীয় গেস্ট ডেটা মুছুন, তারপর mounted ফাইল সিস্টেম trim করুন।

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** দৃশ্যমান ব্লক ডিভাইস-এর discard-এর গ্রানুলারিটি ও সীমা জানায়। **`fstrim -av`** সমর্থিত mounted ফাইল সিস্টেম trim করে এবং পাঠানো range জানায়। পাঠানো byte পুল-এ ফেরত byte-এর সমান নয়। Encrypted, LVM, RAID এবং অন্য স্তরযুক্ত device-এর প্রতিটি স্তরে discard সমর্থন দরকার। [Red Hat-এর অব্যবহৃত ব্লক নির্দেশিকা](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

নির্ধারিত trim বা ভেবে নেওয়া অনলাইন discard নীতি ব্যবহার করুন। **স্টোরেজ পথ পরীক্ষা না করে প্রতিটি ফাইল সিস্টেমে সারাক্ষণ `discard` চালু করবেন না।** গেস্টে trim-এর পর PVE ভলিউম ও পুল পরীক্ষা করুন। মুছে ফেলা record ফাইলে জায়গা নিলে database বা service-এর নিজস্ব compact করার নিয়ম পরীক্ষা করুন।

## কন্টেইনার স্টোরেজের নিয়ম আলাদা করুন

**LXC root ফাইল সিস্টেমের জন্য VM-এর মতো emulated ডিস্ক বাস ব্যবহার করে না।** `pct config CTID` দিয়ে শুরু করে প্রতিটি `rootfs` ও `mpN` entry শনাক্ত করুন। Proxmox স্টোরেজ-backed মাউন্ট, bind মাউন্ট এবং device মাউন্ট আলাদা করে। কনটেইনারের ভেতরে দৃশ্যমান পথ থেকে বোঝা যায় না কোন হোস্ট ভলিউম ব্লকের মালিক। [Proxmox কনটেইনার মাউন্ট পয়েন্ট](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

**পরিচালিত rootfs বা মাউন্ট পয়েন্ট** হলে কনটেইনার বা তার application থেকে ফাইল মুছে হোস্টে ব্যাকিং ভলিউম ও স্ন্যাপশট পরীক্ষা করুন। **CT-এর ওপর VM `qm` discard কমান্ড চালাবেন না।** ZFS subvolume-এ স্ন্যাপশট মুছে ফেলা ব্লক ধরে রাখে। directory ও পাতলা বরাদ্দের LVM স্টোরেজে কনফিগার করা CT আকার নয়, প্রকৃত ব্যাকএন্ড বরাদ্দ দেখুন।

ব্যাকিং স্টোরেজ discard সমর্থন করলে CT পরিষ্কারের পর **Proxmox হোস্টে `pct fstrim` চালান।** Proxmox CT rootfs ও যোগ্য পরিচালিত মাউন্ট পয়েন্ট trim করে। এটি bind মাউন্ট এবং শুধুমাত্র-পঠন মাউন্ট point বাদ দেয়। শুধু rootfs trim করতে `--ignore-mountpoints` দিন। আগে ও পরে স্টোরেজ ব্যবহার তুলনা করুন। [Proxmox `pct fstrim` নির্দেশিকা](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

এই কমান্ড-গুলো উদাহরণ CT ID `101`-এর **বিকল্প পরিধি** দেখায়। আপনার স্টোরেজ বিন্যাস অনুযায়ী একটি পরিধি চালান। স্ন্যাপশট পুরোনো ব্লক ধরে রাখলে সফল trim থেকেও একই পরিমাণ byte ফেরত আসবে এমন নিশ্চয়তা নেই।

**Proxmox bind মাউন্ট বা device মাউন্ট পরিচালনা করে না।** সেগুলোর উৎস ডেটা হোস্ট বা বাইরের device-এ থাকে। Container `vzdump` ব্যাকআপ সেগুলোর content বাদ দেয়। স্টোরেজ-সমর্থিত অতিরিক্ত মাউন্ট পয়েন্ট-ও ডিফল্টভাবে বাদ থাকে, যদি না `backup` বিকল্প সেগুলো অন্তর্ভুক্ত করে। পরিষ্কারের আগে প্রকৃত ব্যাকআপ নীতি দেখুন। [Proxmox ব্যাকআপ ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Nested Docker হলে Docker পরিষ্কার কমান্ড চালানোর আগে প্রকৃত স্টোরেজ-মালিকের কাছে ইমেজ স্তর, ভলিউম এবং log পরীক্ষা করুন। [LXC-তে Docker নির্ভরযোগ্যতা গাইড](/articles/docker-in-lxc-proxmox-reliability/) মাউন্ট ও ব্যাকআপ-এর সীমা ব্যাখ্যা করে। Container ইমেজ মুছলে স্থায়ী ভলিউম ডিফল্টভাবে মুছে যায় না।

## হোস্ট সঠিকভাবে মাপুন

**পরিষ্কারের আগে ও পরে একই মাপ নথিভুক্ত করুন।** পুল-এর খালি জায়গাই চূড়ান্ত ক্ষমতার সূচক। কোন গেস্টের কারণে ব্যবহার বেড়েছে, তা খুঁজতে ভলিউম-স্তরের মাপ ব্যবহার করুন।

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** পরিচালিত ভলিউম এবং কনফিগার করা আকারের তালিকা দেয়। পাতলা স্টোরেজে এটি বরাদ্দ byte মাপে না। **Directory স্টোরেজ**-এর জন্য নির্দিষ্ট মাউন্ট পথ এবং পরিচিত একটি ইমেজ ফাইল পরীক্ষা করুন। **Datacenter > স্টোরেজ** ও VM কনফিগারেশন-এর পথ বসান।

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**বন্ধ VM**-এর ক্ষেত্রে ফাইল না বদলে ইমেজের ভার্চুয়াল ধারণক্ষমতা ও হোস্ট বরাদ্দ তুলনা করুন:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**পাতলা বরাদ্দের LVM**-এর জন্য পুল-এর ডেটা এবং মেটাডেটা দেখুন:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

**ZFS**-এ সক্রিয় dataset ডেটা এবং স্ন্যাপশট-এ আটকে থাকা ডেটা আলাদা করুন:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** dataset-এর সব স্ন্যাপশট আটকে রাখা ব্লক দেখায়। স্ন্যাপশট-এর `used` মান যোগ করা যায় না, কারণ স্ন্যাপশট ব্লক ভাগ করে। কোনো ফাইল মুছে দিলেও তার ব্লকের উল্লেখ থাকা সব স্ন্যাপশট retention নীতি অনুযায়ী মেয়াদোত্তীর্ণ বা মুছে না যাওয়া পর্যন্ত পুল ব্যবহার অপরিবর্তিত থাকতে পারে। [OpenZFS স্ন্যাপশট ও clone](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

**Ceph RBD**-এর জন্য Ceph কমান্ড চালানোর আগে Proxmox ভলিউম ID মিলিয়ে নিন। **`qm config VMID`**-এ `STORAGE_ID:IMAGE` দেখা যায়। **Datacenter > স্টোরেজ**-এ RBD এন্ট্রি খুলে **পুল** এবং ঐচ্ছিক **namespace** বের করুন। স্টোরেজ ID ও পুল name এক নাও হতে পারে। পুল ও ইমেজ-এর মান দিয়ে `POOL/IMAGE` বানান। নির্দিষ্ট Ceph cluster-এর জন্য কনফিগার করা এবং বৈধ credential থাকা client-এ কমান্ড চালান। [Proxmox RBD স্টোরেজ ডকুমেন্টেশন](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** ইমেজ-এর provisioned ও প্রকৃত ব্যবহার, সংশ্লিষ্ট স্ন্যাপশট-সহ, জানায়। `fast-diff` ইমেজ বৈশিষ্ট্য না থাকলে সম্ভাব্য object খুঁজতে OSD-কে জিজ্ঞাসা করে এবং বেশি কাজ লাগে। **`ceph df`** পুল ও ক্লাস্টারের ধারণক্ষমতা দেখায়। Replication, ত্রুটি-সংশোধন কোডিং এবং স্ন্যাপশট ক্লাস্টারের কাঁচা ব্যবহার ব্যবহার বদলায়, তাই ইমেজ byte ও পুল byte আলাদা হয়। [Ceph RBD কমান্ড নির্দেশিকা](https://docs.ceph.com/en/squid/man/8/rbd/) এবং [Ceph পুল ব্যবহার নির্দেশিকা](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

RBD স্টোরেজ-এ namespace থাকলে প্রতিটি `rbd` কমান্ড-এ **`--namespace NAMESPACE`** যোগ করুন। Proxmox স্টোরেজ entry-তে কনফিগার করা namespace ব্যবহার করুন, Proxmox স্টোরেজ ID নয়।

## স্ন্যাপশট ও ব্যাকআপের হিসাব রাখুন

**স্ন্যাপশট ব্লকের পুরোনো সংস্করণ ধরে রাখে।** Trim-এর পর ব্যবহার না কমলে VM বা CT-এর **স্ন্যাপশটগুলো** ট্যাব এবং ব্যাকএন্ডের স্ন্যাপশট তালিকা দেখুন। মোছার আগে মালিকানা ও নির্ভরতা যাচাই করুন। ব্যাকআপ আলাদা কপি এবং ব্যাকআপ স্টোরেজের retention অনুসরণ করে, গেস্টের বর্তমান `df` নয়।

**PBS-এ পুনরাবৃত্তি অপসারণ হিসাব বদলায়।** Datastore-এ ব্যাকআপের মধ্যে ভাগ করা chunk থাকে। Pruning ব্যাকআপ স্ন্যাপশটের মেটাডেটা সরায়। Grace period পেরিয়ে অব্যবহৃত ডেটা পরিষ্কার পরে উল্লেখহীন chunk মুছে দেয়। ব্যাকআপের জায়গা ফিরে পাওয়ার দাবি করার আগে দুই কাজই পরীক্ষা করুন। [PBS রক্ষণাবেক্ষণ ডকুমেন্টেশন](https://pbs.proxmox.com/docs/maintenance.html)

> **সতর্কতা:** শুধু নাম দেখে Proxmox-পরিচালিত ভলিউম ফাইল, zvol বা স্ন্যাপশট কখনও মুছবেন না। আগে গেস্ট এবং retention নীতি শনাক্ত করুন। স্টোরেজ পরিষ্কারে ব্যাকআপ ও rollback পথ অক্ষত থাকতে হবে।

## সিস্টেম বন্ধ করে ডিস্ক ইমেজ পুনর্নির্মাণ

**সাধারণ গেস্ট trim এবং ব্যাকএন্ড পথ qcow2 বরাদ্দ সমস্যা না মেটালে তবেই বন্ধ অবস্থায় conversion করুন।** VM বন্ধ করুন, ব্যাকআপ যাচাই করুন, সব স্ন্যাপশট ও backing-chain সম্পর্ক চিহ্নিত করুন এবং আলাদা গন্তব্য ইমেজ লিখুন। অন্য কোনো প্রক্রিয়া যে ইমেজ ব্যবহার করছে, QEMU সেটি বদলাতে নিষেধ করে। [QEMU `qemu-img` ডকুমেন্টেশন](https://www.qemu.org/docs/master/tools/qemu-img.html)

**ডিস্কে স্ন্যাপশট থাকলে বা পরিচালিত ব্লক স্টোরেজ-এ থাকলে Proxmox-পরিচালিত move অথবা ব্যাকআপ ও পুনরুদ্ধার পদ্ধতি বেছে নিন।** PVE-র মালিকানাধীন ইমেজ-এ একা `qemu-img convert` চালালে VM কনফিগারেশন, ভলিউম মালিকানা বা স্ন্যাপশট নির্দেশিকা নিজে থেকে বদলায় না। মুছে যাওয়া ফাইল ফেরত পেতে `qemu-img resize --shrink` ব্যবহার করবেন না। Partition ও ফাইল সিস্টেম আগে না ছোট করলে গেস্টের দৃশ্যমান ধারণক্ষমতা কমানো ডেটা কেটে দিতে পারে।

## জায়গা ফেরত না এলে সমস্যা খুঁজুন

| লক্ষণ | সম্ভাব্য পরীক্ষা | পরের পদক্ষেপ |
|---|---|---|
| **গেস্ট `df` কমে, হোস্ট একই থাকে** | VM discard পতাকা, গেস্ট trim, স্ন্যাপশট | সম্পূর্ণ discard পথ ও আটকে থাকা স্ন্যাপশট যাচাই করুন। |
| **`fstrim` অসমর্থিত বলে** | গেস্ট ডিস্ক বাস, stacked ব্লক ডিভাইস, backend | `lsblk -D`, গেস্ট kernel এবং মাঝের প্রতিটি স্তর পরীক্ষা করুন। |
| **Windows ReTrim শেষ, হোস্ট একই থাকে** | ব্যাকএন্ডের বরাদ্দ, স্ন্যাপশট, সার্ভারের হিসাব | ভলিউম ও পুল তুলনা করুন। নিশ্চিত করুন ডিস্ক পাতলা বরাদ্দের স্টোরেজ ব্যবহার করে। |
| **`ls -lh` ও `du -h` আলাদা হয়** | Sparse বা qcow2 ফাইল | বরাদ্দ ফাইল সিস্টেম ব্লকের জন্য `du` ব্যবহার করুন। |
| **LVM পাতলা পুল বেশি ভরা থাকে** | ডেটা, মেটাডেটা, স্ন্যাপশট | কিছু মোছার আগে `lvs` এবং PVE স্ন্যাপশট দেখুন। |
| **ZFS পুল বেশি ভরা থাকে** | স্ন্যাপশট-এ আটকানো ব্লক ও reservation | `usedbysnapshots`, zvol সেটিং এবং পুলের ধারণক্ষমতা পরীক্ষা করুন। |
| **CT `df` ও পুল মেলে না** | Bind মাউন্ট, মাউন্ট পয়েন্ট, স্ন্যাপশট | `rootfs` ও প্রতিটি `mpN`-কে হোস্টের মালিকের সঙ্গে মেলান। |

**পেছনে চলা কাজ শেষ হলে আবার পরীক্ষা করুন।** Trim, স্ন্যাপশট মোছা বা backend অব্যবহৃত ডেটা পরিষ্কার-এর পর স্টোরেজের হিসাব দেরিতে বদলাতে পারে। মাপা পুল খালি জায়গা শুরুর মানের সঙ্গে তুলনা করুন। গেস্ট কমান্ড-এর প্রস্থান কোড দেখেই সফলতা ধরে নেবেন না।

## পরের ধাপ

**প্রতি গেস্টের জন্য স্টোরেজ রেকর্ড রাখুন:** ভার্চুয়াল আকার, বরাদ্দ byte, backend, bus, discard পতাকা, স্ন্যাপশট সংখ্যা, ব্যাকআপ কভারেজ এবং পুল-এর খালি জায়গা। একটি VM বেছে সমর্থিত discard পথ চালু করুন, গেস্টে trim চালান এবং নথিভুক্ত মান তুলনা করুন। প্রথম VM-এর ফল ব্যাকএন্ডের প্রত্যাশিত আচরণের সঙ্গে মিললেই পরেরটিতে করুন।

আরও বিস্তৃত পুনরুদ্ধার পরিকল্পনার জন্য [Proxmox ব্যাকআপ ও পুনরুদ্ধার drill](/articles/proxmox-vm-backup-restore-drill/) এবং [Proxmox VE 8 থেকে 9 upgrade নির্দেশিকা](/articles/proxmox-ve-8-to-9-upgrade-guide/) দেখুন।

## উৎস

- [Proxmox VE স্টোরেজ প্রশাসন](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), স্টোরেজ ধরন, পাতলা বরাদ্দ ও ক্ষমতার ঝুঁকি।
- [Proxmox VE LVM স্টোরেজ](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), VE 9 স্ন্যাপশট ভলিউম chain ও বরাদ্দ।
- [Proxmox VE RBD স্টোরেজ](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), পুল ও namespace কনফিগারেশন।
- [Proxmox VE ভার্চুয়াল মেশিন](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), ডিস্ক bus, ফরম্যাট, discard ও গেস্ট এজেন্ট।
- [Proxmox VE VM ডিস্ক বিকল্প](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), bus অনুযায়ী flag।
- [Proxmox VE কনটেইনার](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), root ফাইল সিস্টেম ও মাউন্ট-point মালিকানা।
- [Proxmox VE কনটেইনার কমান্ড](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), হোস্ট থেকে কনটেইনার trim।
- [Proxmox VE ব্যাকআপ ও পুনরুদ্ধার](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), VM ও CT ব্যাকআপ কভারেজ।
- [Microsoft Optimize-ভলিউম নির্দেশিকা](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), Windows ReTrim-এর বিন্যাস।
- [Red Hat অব্যবহৃত ব্লক নির্দেশিকা](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), Linux `fstrim` আচরণ।
- [OpenZFS স্ন্যাপশট ও clone](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), স্ন্যাপশট-এ আটকে থাকা ব্লক।
- [Ceph RBD কমান্ড নির্দেশিকা](https://docs.ceph.com/en/squid/man/8/rbd/), ইমেজ ব্যবহার ও স্ন্যাপশট।
- [NFSv4.2 নির্দিষ্টকরণ](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), সার্ভার পাশে জায়গা ছাড়া।
- [PBS রক্ষণাবেক্ষণ ডকুমেন্টেশন](https://pbs.proxmox.com/docs/maintenance.html), pruning ও অব্যবহৃত ডেটা পরিষ্কার।
- [QEMU ডিস্ক-ইমেজ সরঞ্জাম](https://www.qemu.org/docs/master/tools/qemu-img.html), বন্ধ অবস্থায় ইমেজ conversion-এর নিরাপত্তা।
