---
title: "Proxmox VE 9: वर्चुअल डिस्क का उपयोग घटाएँ और जगह वापस पाएँ"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Proxmox VE 9 में VM और LXC कंटेनरों की स्टोरेज खपत घटाएँ। फ़ॉर्मैट और बैकएंड की तुलना करें, discard सक्षम करें, trim चलाएँ और जगह वापस पाने से पहले snapshots जाँचें।"
genre: ["वर्चुअलाइजेशन", "Linux प्रशासन", "Proxmox VE प्लेटफ़ॉर्म", "स्टोरेज", "घरेलू लैब"]
tags: ["Proxmox VE 9 डिस्क स्पेस", "Proxmox में पतला आवंटन", "Proxmox discard सूचना", "Proxmox TRIM कमांड", "Proxmox पर Windows ReTrim", "Proxmox पर Linux में fstrim", "Proxmox LXC डिस्क उपयोग", "Proxmox LVM पतला आवंटन", "Proxmox ZFS sparse zvol", "Proxmox Ceph RBD ब्लॉक डिवाइस", "Proxmox qcow2 फ़ॉर्मेट", "Proxmox raw डिस्क", "Proxmox स्नैपशॉट", "वर्चुअल डिस्क स्थान की रिकवरी", "Proxmox स्टोरेज प्रकार", "VirtIO SCSI नियंत्रक", "Proxmox शून्य लिखने की पहचान", "Proxmox बैकअप स्टोरेज"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "तीर से जुड़ी दो ब्लॉक ग्रिड वर्चुअल डिस्क के उपयोग किए गए ब्लॉक और स्टोरेज पूल की खाली क्षमता दिखाती हैं।"
coverCaption: "गेस्ट में फ़ाइलें हटाना, discard भेजना और स्टोरेज में जगह लौटना अलग-अलग चरण हैं।"
---

**गेस्ट फ़ाइल सिस्टम छोटा होने से Proxmox पर स्टोरेज उपयोग हमेशा कम नहीं होता।** होस्ट पर जगह खाली करने के लिए पतला आवंटन समर्थित डिस्क, VM के लिए काम करने वाला discard पथ और स्नैपशॉट द्वारा रोके गए ब्लॉकों से मुक्त बैकएंड चाहिए। यह मार्गदर्शिका Proxmox VE 9 VM और LXC कंटेनरों की सेटिंग और जाँच बताती है।

<!--more-->

## मुख्य बातें

- **पहले बैकिंग स्टोरेज चुनें।** वर्चुअल डिस्क का बताया गया आकार होस्ट पर आवंटित जगह से तभी अलग होता है, जब इमेज फ़ॉर्मैट या बैकएंड पतला आवंटन समर्थित करे।
- **VM पर discard चालू करें, फिर गेस्ट के भीतर trim चलाएँ।** Windows ReTrim और Linux `fstrim` वर्चुअल डिस्क के ज़रिए खाली ब्लॉकों के अनुरोध भेजते हैं।
- **स्नैपशॉट और बैकअप अलग-अलग जाँचें।** किसी स्नैपशॉट में संदर्भित पुराने ब्लॉक तब तक आवंटित रहते हैं। बैकअप फ़ाइलें और PBS डेटा खंड अपनी retention नीति से चलते हैं।
- **LXC माउंट को उनके प्रकार के अनुसार देखें।** प्रबंधित rootfs और माउंट-point वॉल्यूम, bind माउंट और device माउंट का स्वामित्व और बैकअप व्यवहार अलग होता है।

## शुरू करने से पहले

आपको **Proxmox VE 9 का प्रशासक एक्सेस**, हर प्रभावित गेस्ट का सत्यापित बैकअप और प्रक्रिया के लिए पूल में पर्याप्त खाली जगह चाहिए। सेटिंग बदलने से पहले गेस्ट ID, डिस्क बस, वॉल्यूम ID, स्टोरेज ID, स्नैपशॉट और वर्तमान आवंटन लिखें। रिकवरी जाँचने के लिए [VM पुनर्प्राप्ति अभ्यास](/articles/proxmox-vm-backup-restore-drill/) चलाएँ।

**अनुमानित समय:** हर गेस्ट के लिए 20 से 60 मिनट, और बड़ी trim या सफ़ाई प्रक्रिया के लिए अतिरिक्त समय। **कठिनाई:** मध्यम। कम जोखिम वाली एक VM से शुरू करें और पहले तथा बाद का स्टोरेज उपयोग तुलना करें।

> **चेतावनी:** पूरा पतला पूल गेस्ट में I/O त्रुटियाँ पैदा करता है और फ़ाइल सिस्टम को नुकसान पहुँचा सकता है। पूल की खाली डेटा और मेटाडेटा जगह देखे बिना उपलब्ध क्षमता से अधिक आवंटन न करें। [Proxmox स्टोरेज दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## आवंटन की शृंखला समझें

**हटाना**, **discard** और **जगह लौटना** अलग-अलग परतों पर होता है। गेस्ट फ़ाइल हटाकर फ़ाइल सिस्टम ब्लॉकों को खाली चिह्नित करता है। फ़ाइल सिस्टम उन ब्लॉकों के लिए TRIM या UNMAP भेजता है। वर्चुअल डिस्क पर discard सक्षम हो तो QEMU अनुरोध आगे भेजता है। फ़ॉर्मैट और पूल समर्थित हों तो बैकएंड भौतिक आवंटन मुक्त करता है। [Proxmox VM डिस्क दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| परत | क्या जाँचें | उपयोगी प्रमाण |
|---|---|---|
| **गेस्ट फ़ाइलें** | फ़ाइल सिस्टम की खाली जगह | Windows वॉल्यूम गुण या Linux `df -h` |
| **वर्चुअल डिस्क** | बस, discard, SSD अनुकरण, इमेज फ़ॉर्मैट | VM का **Hardware** टैब या `qm config VMID` |
| **PVE वॉल्यूम** | मालिक और कॉन्फ़िगर आकार | स्टोरेज का **Content** टैब या `pvesm list STORAGE_ID` |
| **स्टोरेज पूल** | खाली डेटा और मेटाडेटा, रोके गए ब्लॉक | `pvesm status` और बैकएंड के टूल |

**100 GiB की वर्चुअल डिस्क क्षमता सीमा है, 100 GiB आवंटित होने की गारंटी नहीं।** इसी तरह गेस्ट का 20 GiB उपयोग दिखाना यह साबित नहीं करता कि होस्ट भी 20 GiB उपयोग कर रहा है। मेटाडेटा, स्नैपशॉट, बैकअप प्रतियाँ और पहले लिखे ब्लॉक आँकड़ा बदलते हैं। [Proxmox स्टोरेज दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## डिस्क फ़ॉर्मैट की तुलना करें

**स्टोरेज बैकएंड तय करता है कि Proxmox कौन से इमेज फ़ॉर्मैट देता है।** ZFS zvol और Ceph RBD वर्चुअल raw डिस्क इस्तेमाल करते हैं। LVM सामान्यतः raw इस्तेमाल करता है, सिवाय Proxmox VE 9 की नीचे बताई गई वॉल्यूम-chain सुविधा के। directory और NFS जैसे फ़ाइल बैकएंड raw या qcow2 समर्थित करते हैं। Raw अपने आप पतला आवंटन या स्नैपशॉट नहीं देता। यह सुविधा नीचे की स्टोरेज परत से मिलनी चाहिए। Qcow2 इमेज परत में copy-on-write आवंटन और स्नैपशॉट देता है। [Proxmox VM डिस्क दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| फ़ॉर्मैट | आवंटन तरीका | जगह का समझौता |
|---|---|---|
| **फ़ाइल स्टोरेज पर qcow2** | लिखे जाने पर qcow2 clusters आवंटित करता है | इमेज मेटाडेटा और स्नैपशॉट chains जगह लेते हैं |
| **फ़ाइल स्टोरेज पर raw फ़ाइल** | समर्थित होने पर sparse-फ़ाइल व्यवहार | Raw अकेले पतला आवंटन या स्नैपशॉट नहीं देता |
| **Raw ब्लॉक वॉल्यूम** | पतले आवंटन वाला LVM, ZFS, Ceph RBD या अन्य बैकिंग स्टोरेज | पूल आवंटन और स्नैपशॉट बैकएंड पर निर्भर हैं |

**Proxmox VE 9 मोटा LVM में स्नैपशॉट का खास मोड है।** `snapshot-as-volume-chain` मोटा LVM तार्किक वॉल्यूम के बीच qcow2 आधार संबंध उपयोग करता है। यह qcow2 आंतरिक स्नैपशॉट नहीं उपयोग करता। विकल्प केवल नई VM डिस्क पर लागू होता है और मौजूदा Proxmox दस्तावेज़ में तकनीकी preview है। PVE हर स्नैपशॉट को पूरा आवंटित दिखाता है। SAN पर वास्तविक आवंटन तभी कम होता है, जब बैकिंग स्टोरेज पतला आवंटन और discard समर्थित करे। [Proxmox LVM स्टोरेज दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**सिर्फ `.raw` extension के कारण डिस्क को convert न करें।** पहले स्टोरेज plugin और आवंटित ब्लॉक जाँचें। `local-lvm` की raw डिस्क का आवंटन सामान्य directory स्टोरेज की पूरी तरह आवंटित raw फ़ाइल से अलग है।

## स्टोरेज प्रकारों की तुलना करें

Proxmox **फ़ाइल स्टोरेज** और **ब्लॉक स्टोरेज** को अलग रखता है। स्टोरेज plugin स्नैपशॉट, clones, sharing और हर पूल के स्वीकार्य content प्रकार भी तय करता है। किसी फ़ॉर्मैट या सुविधा पर निर्भर होने से पहले **Datacenter > स्टोरेज** में प्रविष्टि देखें। [Proxmox स्टोरेज प्रकार तालिका](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| स्टोरेज | VM डिस्क व्यवहार | रिकवरी जाँच |
|---|---|---|
| **Directory, ext4, XFS** | Raw या qcow2 फ़ाइलें | `du` के आवंटित bytes की इमेज की वर्चुअल आकार से तुलना करें। यदि दूसरी परत स्नैपशॉट देती है तो उन्हें जाँचें। |
| **NFS, CIFS** | साझा स्टोरेज पर raw या qcow2 फ़ाइलें | सर्वर पर आवंटित जगह जाँचें। गेस्ट trim से सर्वर पर जगह घटने का प्रमाण नहीं मिलता। |
| **LVM का पतला आवंटन (`local-lvm`)** | केवल स्थानीय पतला raw तार्किक वॉल्यूम | `lvs` से पतला पूल के डेटा और मेटाडेटा प्रतिशत देखें। |
| **LVM thick** | Raw LVs या VE 9 qcow2 वॉल्यूम chains | गेस्ट में फ़ाइलें हटाने से स्थिर LV आरक्षण कम नहीं होता। SAN का पतला आवंटन अलग से जाँचें। |
| **ZFS स्टोरेज (`local-zfs`)** | raw zvol या कंटेनर उपखंड | `sparse`, dataset गुण, पूल उपयोग और स्नैपशॉट जाँचें। |
| **Ceph RBD** | साझा स्टोरेज पर पतला `raw RBD` इमेज | Ceph पूल क्षमता, इमेज उपयोग, स्नैपशॉट और discard जाँचें। |
| **Btrfs** | Raw images के लिए Btrfs उपखंड वाले फ़ाइल-backed वॉल्यूम | PVE के Btrfs प्लगइन को तकनीकी preview मानें और स्नैपशॉट तथा फ़ाइल सिस्टम उपयोग जाँचें। |

**अन्य स्टोरेज plugins के काम अलग हैं।** CephFS साझा फ़ाइल स्टोरेज देता है। iSCSI और Fibre Channel साझा ब्लॉक devices देते हैं, जिन्हें अक्सर LVM से VM वॉल्यूम में बाँटा जाता है। iSCSI पर ZFS दूरस्थ ZFS-आधारित ब्लॉक स्टोरेज देता है। Proxmox बैकअप सर्वर (PBS) बैकअप रखता है, सक्रिय VM डिस्क नहीं। `images`, `rootdir`, `backup` या `iso` डेटा रखने से पहले सक्षम **Content** प्रकार जाँचें। [Proxmox स्टोरेज प्रकार तालिका](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**फ़ाइल स्टोरेज के आवंटन flags डिस्क बनाते समय मायने रखते हैं।** स्टोरेज का `format` विकल्प समर्थित होने पर `raw`, `qcow2` या `vmdk` चुनता है। Raw और qcow2 फ़ाइलों के `preallocation` में `off`, `metadata`, `falloc` या `full` स्वीकार होते हैं। डिफ़ॉल्ट `metadata` है, जिसे raw के लिए `off` माना जाता है। `full` फ़ाइल की जगह पहले से आरक्षित करता है, इसलिए शुरुआती footprint छोटा नहीं रहता। बड़ी डिस्क बनाने से पहले स्टोरेज कॉन्फ़िगरेशन देखें। `shared` flag केवल मौजूदा साझा पहुँच घोषित करता है। यह स्थानीय स्टोरेज को साझा नहीं बनाता। [Proxmox की सामान्य स्टोरेज विशेषताएँ](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` पतला zvol बनाने की स्टोरेज सेटिंग है।** Sparse zvol के बिना, वॉल्यूम व्यवहार के अनुसार निर्माण क्षमता आरक्षित करता है। मौजूदा तैनाती बदलने से पहले स्टोरेज कॉन्फ़िगरेशन और पूल की जाँच करें। [Proxmox ZFS स्टोरेज दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory स्टोरेज की दूसरी जाँच जरूरी है।** qcow2 फ़ाइल की तार्किक लंबाई, गेस्ट को दिखने वाली वर्चुअल क्षमता नहीं होती। `du -h` इमेज को आवंटित फ़ाइल सिस्टम ब्लॉक बताता है। `ls -lh` फ़ाइल की तार्किक लंबाई दिखाता है। बंद VM के लिए `qemu-img info` वर्चुअल क्षमता और होस्ट डिस्क आकार बताता है। NFS पर अंतिम क्षमता निर्णय के लिए सर्वर के आँकड़े लें। [QEMU `qemu-img` संदर्भ](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS की एक और आवंटन सीमा है।** qcow2 का अपनी फ़ाइल में खाली cluster दोबारा उपयोग करना यह नहीं बताता कि NFS सर्वर फ़ाइल के ब्लॉक छोड़ रहा है। खाली ब्लॉक मुक्त करना के लिए client, सहमत प्रोटोकॉल, सर्वर और उसके फ़ाइल सिस्टम का समर्थन चाहिए। NFSv4.2 में `DEALLOCATE` परिभाषित है, लेकिन संस्करण संख्या यह प्रमाणित नहीं करता कि सर्वर ने जगह लौटाई। Negotiated NFS माउंट जाँचें और सर्वर पर आवंटन मापें। [NFSv4.2 `DEALLOCATE` विनिर्देश](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## VM डिस्क विकल्प तय करें

Proxmox इंटरफ़ेस में **VM > Hardware > Hard डिस्क > Edit** खोलें। डिस्क बस और advanced विकल्प देखें। ये flags आवंटन बदलते हैं या बताते हैं कि कोई अनुकूलन उपयोगी है या नहीं। [आधिकारिक `qm` विकल्प संदर्भ](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) बस के अनुसार उपलब्धता बताता है।

| बस | जगह से जुड़ा विकल्प |
|---|---|
| **IDE** | पुराने सिस्टमों के साथ संगतता। केवल तब इस्तेमाल करें जब गेस्ट के पास नया ड्राइवर न हो। |
| **SATA** | व्यापक रूप से समर्थित emulation। रिकवरी पर निर्भर होने से पहले गेस्ट trim और डिस्क विकल्प जाँचें। |
| **VirtIO SCSI के साथ SCSI** | discard और प्रति-डिस्क सेटिंग के लिए पसंदीदा आधुनिक रास्ता। Windows को VirtIO ड्राइवर चाहिए। |
| **VirtIO ब्लॉक** | Paravirtualized डिस्क। Linux का discard संकेत के लिए kernel 5.0 या नया चाहिए। SSD अनुकरण उपलब्ध नहीं। |

| सेटिंग | असर | सुझाव |
|---|---|---|
| **discard चालू (`on`)** | गेस्ट TRIM या UNMAP आगे भेजता है | समर्थित पतला backend पर गेस्ट से जगह लौटाने के लिए जरूरी। डिफ़ॉल्ट `ignore` forwarding रोकता है। |
| **SSD अनुकरण `ssd=1`** | गेस्ट को डिस्क SSD के रूप में दिखाता है | कुछ गेस्ट trim भेजने से पहले यह पहचान चाहते हैं। इससे भौतिक स्टोरेज तेज़ नहीं होता। VirtIO ब्लॉक में यह flag नहीं है। |
| **शून्य लेखन पहचान `detect_zeroes=1`** | शून्य लिखने का पता लगाकर अनुकूलित करने की कोशिश | वैकल्पिक I/O अनुकूलन। गेस्ट trim का विकल्प नहीं और जगह लौटने की गारंटी नहीं। |
| **Bus: SCSI / VirtIO SCSI सिंगल** | VirtIO नियंत्रक से SCSI डिस्क देता है | आधुनिक Windows और Linux गेस्ट के लिए अच्छा default। Windows VirtIO ड्राइवर इंस्टॉल करें। |
| **Bus: VirtIO ब्लॉक** | VirtIO ब्लॉक डिवाइस उपयोग करता है | Linux का discard संकेत के लिए kernel 5.0 या नया चाहिए। SSD अनुकरण नहीं है। |
| **I/O thread `iothread=1`** | ड्राइव I/O अलग thread को देता है | VirtIO ब्लॉक या VirtIO SCSI सिंगल नियंत्रक पर SCSI के साथ उपयोग करें। यह प्रदर्शन सेटिंग है, रिकवरी स्विच नहीं। |
| **कैश और AIO** | I/O buffering और asynchronous I/O बदलते हैं | Workload और backend के अनुसार सेट करें। इनमें से कोई डिस्क का आकार कम नहीं करता। |
| **बैकअप `backup=0`** | डिस्क को VM बैकअप से बाहर रखता है | बैकअप का दायरा घटाता है और डिस्क डेटा को VM recovery से हटाता है। अलग बैकअप दर्ज करें। |
| **Replicate `replicate=0`** | डिस्क को स्टोरेज replication से बाहर रखता है | Replicated डेटा घटाता है और डिस्क को replica से हटाता है। |

**दूसरे drive विकल्प व्यवहार बताते हैं, जगह लौटाना नहीं।** `format` कई इमेज फ़ॉर्मैट वाले backend पर डिस्क बनाते समय लागू होता है। `size` वर्चुअल क्षमता है, आवंटित bytes नहीं। `ro=1` डिस्क को केवल-पढ़ने योग्य बनाता है। `snapshot=1` QEMU का अस्थायी स्नैपशॉट मोड चालू करता है, जो VM बंद होने पर डिस्क परिवर्तन छोड़ देता है। यह Proxmox VM स्नैपशॉट में डिस्क शामिल करने का switch नहीं है। स्थायी डेटा पर इसका उपयोग न करें। `backup=0` या `replicate=0` से पहले पुनर्प्राप्ति कवरेज जाँचें। [Proxmox VM डिस्क विकल्प](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**किसी मौजूदा drive पर छोटा `qm set --scsi0` string paste न करें।** **`qm config VMID`** देखें और संशोधन करते समय पूरा वॉल्यूम ID तथा मौजूदा विकल्प बनाए रखें। छोटा ड्राइव आवंटन दूसरी प्रति-डिस्क सेटिंग हटा सकता है। हर बदलाव के बाद इंटरफ़ेस में सहेजे गए विकल्प जाँचें।

```bash
qm config 100
pvesm status
```

`100` उदाहरण VM ID है। मौजूदा VM पर **नई** 64 GiB SCSI डिस्क बनाने के लिए, जिसका controller **VirtIO SCSI सिंगल** हो और गेस्ट में आवश्यक ड्राइवर हो, यह कमांड आवंटन syntax दिखाता है। VM ID और स्टोरेज ID अपने मान से बदलें।

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**उदाहरण से पहले जाँचें कि `scsi0` पहले से मौजूद तो नहीं।** यह कमांड उस slot को बदलता है। मौजूदा डिस्क पर, यदि सटीक विकल्प string बचाना आसान हो तो इंटरफ़ेस इस्तेमाल करें। [Proxmox `qm` कमांड संदर्भ](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) देखें।

## गेस्ट सिस्टम की फ़ाइलें साफ़ करें

**पहले गेस्ट फ़ाइलें खाली करें।** Windows स्टोरेज सेटिंग, अस्थायी फ़ाइलें, पुराने installers, एप्लिकेशन कैश और रीसायकल बिन जाँचें। Database और container runtime को उनके अपने इंटरफ़ेस से साफ़ करें। केवल आवंटन कम करने के लिए सक्रिय एप्लिकेशन का डेटा हटाने से डेटा हानि हो सकती है।

**पुष्टि करें कि वॉल्यूम discard-सक्षम वर्चुअल डिस्क इस्तेमाल करता है**, फिर Windows VM में व्यवस्थापक PowerShell सत्र खोलें:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` बताता है कि Windows ने रिपोर्ट किए गए फ़ाइल सिस्टम के लिए हटाने की सूचनाएँ सक्षम की हैं। **ReTrim** वर्तमान में खाली वॉल्यूम क्षेत्रों के trim अनुरोध फिर भेजता है। सफल कमांड यह पुष्टि करता है कि गेस्ट ने ऑपरेशन भेजा, यह नहीं कि होस्ट ने कितने bytes वापस पाए। काम पूरा होने पर होस्ट जाँचें। [Microsoft `Optimize-Volume` cmdlet दस्तावेज़](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) और [Proxmox VM डिस्क दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**QEMU गेस्ट एजेंट को TRIM न समझें।** Agent गेस्ट नियंत्रण और बैकअप-संगति सुविधाएँ देता है। फ़ाइल सिस्टम की हटाने की सूचनाएँ वर्चुअल डिस्क पथ से जाती हैं। केवल agent इंस्टॉल करने से ब्लॉक वापस नहीं मिलते। [Proxmox VM गेस्ट एजेंट दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## फ़ाइल सिस्टम के खाली ब्लॉक चिह्नित करें

**Trim से पहले ब्लॉक पथ और फ़ाइल सिस्टम जाँचें।** आधुनिक distribution अक्सर `fstrim.timer` नियमित रूप से चलाता है। उसका status देखें, फिर अनावश्यक गेस्ट डेटा हटाने के बाद mounted फ़ाइल सिस्टम trim करें।

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** दिखाई देने वाले ब्लॉक devices की discard दानेदारता और limits बताता है। **`fstrim -av`** समर्थित mounted फ़ाइल सिस्टम trim करता है और भेजी गई ranges बताता है। भेजे गए bytes, पूल को लौटे bytes के बराबर नहीं होते। Encrypted, LVM, RAID और अन्य स्तरीकृत डिवाइस को हर परत पर discard समर्थन चाहिए। [Red Hat unused-ब्लॉक मार्गदर्शन](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Scheduled trim या सोच-समझकर ऑनलाइन discard नीति अपनाएँ। **स्टोरेज पथ जाँचने के बजाय हर फ़ाइल सिस्टम पर लगातार `discard` सक्षम न करें।** गेस्ट trim के बाद PVE वॉल्यूम और पूल देखें। यदि हटाए रिकॉर्ड फ़ाइलों में जगह लेते रहें, तो database या service की compact करने की नीति देखें।

## कंटेनर स्टोरेज के नियम अलग जाँचें

**LXC में root फ़ाइल सिस्टम के लिए VM जैसा emulated डिस्क बस नहीं होता।** `pct config CTID` से शुरू करें और हर `rootfs` तथा `mpN` प्रविष्टि पहचानें। Proxmox स्टोरेज-backed माउंट, bind माउंट और device माउंट अलग करता है। कंटेनर में दिखने वाला पथ यह नहीं बताता कि ब्लॉकों का मालिक कौन सा होस्ट वॉल्यूम है। [Proxmox कंटेनर माउंट पॉइंट](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

**प्रबंधित rootfs या माउंट पॉइंट** के लिए कंटेनर या उसके application से फ़ाइलें हटाएँ, फिर होस्ट पर बैकिंग वॉल्यूम और स्नैपशॉट देखें। **CT पर VM के `qm` discard कमांड न चलाएँ।** ZFS subvolume में स्नैपशॉट हटाए ब्लॉक रोकते हैं। directory और पतले आवंटन वाला LVM स्टोरेज में कॉन्फ़िगर किया CT आकार नहीं, वास्तविक backend आवंटन देखें।

यदि बैकिंग स्टोरेज discard समर्थित करता है, तो CT साफ़ करने के बाद **Proxmox होस्ट पर `pct fstrim` चलाएँ।** Proxmox CT rootfs और योग्य प्रबंधित माउंट पॉइंट trim करता है। यह bind माउंट और केवल-पढ़ने वाला माउंट points छोड़ देता है। केवल rootfs trim करने के लिए `--ignore-mountpoints` उपयोग करें। पहले और बाद का स्टोरेज उपयोग तुलना करें। [Proxmox `pct fstrim` संदर्भ](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

ये कमांड उदाहरण CT ID `101` के लिए **वैकल्पिक दायरे** दिखाते हैं। अपने स्टोरेज लेआउट के अनुसार एक दायरा चलाएँ। सफल trim भी समान bytes लौटने की गारंटी नहीं देता, क्योंकि स्नैपशॉट पुराने ब्लॉक रोक सकते हैं।

**Proxmox bind माउंट और device माउंट प्रबंधित नहीं करता।** उनका स्रोत डेटा होस्ट या बाहरी device पर रहता है। कंटेनर के `vzdump` बैकअप इनकी सामग्री शामिल नहीं करते। स्टोरेज-backed अतिरिक्त माउंट पॉइंट भी डिफ़ॉल्ट रूप से बाहर रहते हैं, जब तक उनका `backup` विकल्प उन्हें शामिल न करे। साफ़ करने से पहले वास्तविक बैकअप नीति जाँचें। [Proxmox बैकअप दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Nested Docker के लिए Docker सफ़ाई कमांड चलाने से पहले वास्तविक स्टोरेज मालिक में इमेज layers, वॉल्यूम और logs देखें। [LXC में Docker विश्वसनीयता मार्गदर्शिका](/articles/docker-in-lxc-proxmox-reliability/) माउंट और बैकअप सीमाएँ बताती है। Container इमेज हटाने से स्थायी वॉल्यूम डिफ़ॉल्ट रूप से नहीं हटता।

## होस्ट को सही तरीके से मापें

**सफ़ाई से पहले और बाद में एक जैसे माप दर्ज करें।** पूल की खाली जगह अंतिम क्षमता संकेत है। किस गेस्ट से वृद्धि हुई, यह पता लगाने के लिए वॉल्यूम स्तर के आँकड़े देखें।

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** प्रबंधित वॉल्यूम और कॉन्फ़िगर आकार की सूची देता है। यह पतला स्टोरेज पर आवंटित bytes नहीं मापता। **Directory स्टोरेज** में सटीक mounted पथ और एक ज्ञात इमेज फ़ाइल देखें। **Datacenter > स्टोरेज** और VM config के पथ भरें।

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**बंद VM** के लिए फ़ाइल बदले बिना इमेज की वर्चुअल क्षमता और होस्ट आवंटन तुलना करें:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**पतले आवंटन वाला LVM** के लिए पूल का डेटा और मेटाडेटा देखें:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

**ZFS** में सक्रिय डेटासेट डेटा और स्नैपशॉट द्वारा रोके गए डेटा अलग देखें:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** dataset के सभी स्नैपशॉट द्वारा रोके गए ब्लॉक बताता है। स्नैपशॉट `used` आँकड़े जोड़ने योग्य नहीं हैं, क्योंकि स्नैपशॉट ब्लॉक साझा करते हैं। हटाई फ़ाइल के ब्लॉक संदर्भित करने वाले सभी स्नैपशॉट retention नीति के अनुसार expire या हटने तक पूल उपयोग स्थिर रह सकता है। [OpenZFS स्नैपशॉट और clones](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

**Ceph RBD** के लिए Ceph कमांड चलाने से पहले Proxmox वॉल्यूम ID को map करें। **`qm config VMID`** में `STORAGE_ID:IMAGE` दिखता है। **पूल** और वैकल्पिक **namespace** जानने के लिए **Datacenter > स्टोरेज** में RBD प्रविष्टि खोलें। स्टोरेज ID और पूल name अलग हो सकते हैं। पूल तथा इमेज मानों से `POOL/IMAGE` बनाएँ। इन कमांड को लक्षित Ceph क्लस्टर के लिए कॉन्फ़िगर client और वैध credentials से चलाएँ। [Proxmox RBD स्टोरेज दस्तावेज़](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** इमेज का provisioned और वास्तविक उपयोग, संबंधित स्नैपशॉट सहित, बताता है। `fast-diff` इमेज सुविधा न हो तो संभावित objects के लिए OSDs से query करता है और अधिक काम लेता है। **`ceph df`** पूल और cluster क्षमता दिखाता है। Replication, इरेज़र कोडिंग और स्नैपशॉट क्लस्टर का raw उपयोग उपयोग बदलते हैं, इसलिए इमेज bytes और पूल bytes अलग होते हैं। [Ceph RBD कमांड संदर्भ](https://docs.ceph.com/en/squid/man/8/rbd/) और [Ceph पूल उपयोग मार्गदर्शन](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

RBD स्टोरेज namespace उपयोग करे तो हर `rbd` कमांड में **`--namespace NAMESPACE`** जोड़ें। Proxmox स्टोरेज प्रविष्टि में कॉन्फ़िगर namespace लें, Proxmox स्टोरेज ID नहीं।

## प्रतिलिपि बिंदुओं और बैकअप का हिसाब रखें

**स्नैपशॉट ब्लॉकों के पुराने संस्करण बचाते हैं।** Trim के बाद उपयोग न घटे तो VM या CT का **स्नैपशॉट** टैब और backend की स्नैपशॉट सूची देखें। हटाने से पहले मालिकाना और निर्भरताएँ जाँचें। बैकअप अलग प्रति है और बैकअप स्टोरेज की retention से चलता है, गेस्ट के वर्तमान `df` से नहीं।

**PBS डुप्लिकेट डेटा हटाना गणना बदलती है।** उसके datastore में कई बैकअप द्वारा साझा chunks होते हैं। Pruning बैकअप स्नैपशॉट मेटाडेटा हटाता है। बाद में बेकार डेटा की सफ़ाई प्रतीक्षा अवधि के बाद बिना संदर्भ वाले chunks हटाता है। बैकअप क्षमता लौटने का दावा करने से पहले दोनों tasks जाँचें। [PBS रखरखाव दस्तावेज़](https://pbs.proxmox.com/docs/maintenance.html)

> **चेतावनी:** Proxmox-प्रबंधित वॉल्यूम फ़ाइल, zvol या स्नैपशॉट को केवल नाम देखकर कभी न हटाएँ। पहले गेस्ट और retention नीति पहचानें। स्टोरेज सफ़ाई में बैकअप और rollback का रास्ता बचा रहना चाहिए।

## VM बंद करके डिस्क इमेज दोबारा बनाएँ

**बंद अवस्था में conversion केवल तभी करें, जब सामान्य गेस्ट trim और backend पथ qcow2 आवंटन समस्या हल न करें।** VM बंद करें, बैकअप सत्यापित करें, स्नैपशॉट तथा backing-chain संबंध पहचानें और अलग लक्ष्य इमेज लिखें। QEMU किसी दूसरे प्रक्रिया द्वारा उपयोग की जा रही इमेज बदलने से मना करता है। [QEMU `qemu-img` दस्तावेज़](https://www.qemu.org/docs/master/tools/qemu-img.html)

**डिस्क पर स्नैपशॉट हों या वह प्रबंधित ब्लॉक स्टोरेज पर हो, तो Proxmox-प्रबंधित move या बैकअप और पुनर्प्राप्ति प्रक्रिया चुनें।** PVE-owned इमेज पर अकेला `qemu-img convert` VM config, वॉल्यूम स्वामित्व या स्नैपशॉट references स्वयं नहीं बदलता। हटाई फ़ाइलें वापस पाने के लिए `qemu-img resize --shrink` न चलाएँ। गेस्ट को दिखने वाली क्षमता घटाने से डेटा truncate हो सकता है, यदि partitions और filesystems पहले छोटे न किए गए हों।

## जगह वापस न मिलने पर जाँचें

| लक्षण | संभावित जाँच | अगला कदम |
|---|---|---|
| **गेस्ट का `df` घटे, होस्ट समान रहे** | VM discard फ़्लैग, गेस्ट trim, स्नैपशॉट | पूरा discard पथ और रोके गए स्नैपशॉट सत्यापित करें। |
| **`fstrim` असमर्थित बताए** | गेस्ट डिस्क बस, stacked ब्लॉक devices, backend | `lsblk -D`, गेस्ट kernel और हर बीच की परत देखें। |
| **Windows ReTrim पूरा हो, होस्ट समान रहे** | बैकएंड में आवंटन, प्रतिलिपि बिंदु, सर्वर के आँकड़े | वॉल्यूम और पूल तुलना करें। पुष्टि करें कि डिस्क पतला स्टोरेज पर है। |
| **`ls -lh` और `du -h` अलग हों** | Sparse या qcow2 फ़ाइल | फ़ाइल सिस्टम के आवंटित ब्लॉकों के लिए `du` उपयोग करें। |
| **LVM पतला पूल ऊँचा रहे** | डेटा, मेटाडेटा, स्नैपशॉट | कुछ हटाने से पहले `lvs` और PVE स्नैपशॉट देखें। |
| **ZFS पूल ऊँचा रहे** | स्नैपशॉट-held ब्लॉक और reservations | `usedbysnapshots`, zvol सेटिंग और पूल क्षमता जाँचें। |
| **CT `df` और पूल अलग हों** | Bind माउंट, माउंट पॉइंट, स्नैपशॉट | `rootfs` और हर `mpN` को उसके होस्ट मालिक से जोड़ें। |

**Background काम पूरा होने पर फिर जाँचें।** Trim, स्नैपशॉट हटाने या backend बेकार डेटा की सफ़ाई के बाद स्टोरेज आँकड़े अपडेट होने में समय लग सकता है। मापी गई खाली पूल जगह की शुरुआती मान से तुलना करें। केवल गेस्ट कमांड के निकास कोड से सफलता न मानें।

## अगले कदम

**हर गेस्ट के लिए स्टोरेज रिकॉर्ड बनाएँ:** वर्चुअल आकार, आवंटित bytes, backend, bus, discard फ़्लैग, स्नैपशॉट संख्या, बैकअप coverage और पूल की खाली जगह। एक VM चुनें, समर्थित discard पथ सक्रिय करें, गेस्ट में trim चलाएँ और दर्ज मानों की तुलना करें। पहली VM का परिणाम backend के अपेक्षित व्यवहार से मेल खाए तभी आगे दोहराएँ।

व्यापक रिकवरी योजना के लिए [Proxmox बैकअप और पुनर्प्राप्ति drill](/articles/proxmox-vm-backup-restore-drill/) और [Proxmox VE 8 से 9 upgrade मार्गदर्शिका](/articles/proxmox-ve-8-to-9-upgrade-guide/) देखें।

## स्रोत

- [Proxmox VE स्टोरेज प्रशासन](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), स्टोरेज प्रकार, पतला आवंटन और क्षमता जोखिम।
- [Proxmox VE LVM स्टोरेज](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), VE 9 स्नैपशॉट वॉल्यूम chains और आवंटन।
- [Proxmox VE RBD स्टोरेज](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), पूल और namespace कॉन्फ़िगरेशन।
- [Proxmox VE वर्चुअल मशीनें](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), डिस्क बस, फ़ॉर्मैट, discard और गेस्ट एजेंट।
- [Proxmox VE VM डिस्क विकल्प](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), बस-विशिष्ट flags।
- [Proxmox VE कंटेनर](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), root फ़ाइल सिस्टम और माउंट-point स्वामित्व।
- [Proxmox VE कंटेनर कमांड](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), होस्ट से कंटेनर trim।
- [Proxmox VE बैकअप और पुनर्प्राप्ति](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), VM और CT बैकअप कवरेज।
- [Microsoft Optimize-वॉल्यूम संदर्भ](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), Windows ReTrim का सिंटैक्स।
- [Red Hat unused-ब्लॉक मार्गदर्शन](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), Linux `fstrim` व्यवहार।
- [OpenZFS स्नैपशॉट और clones](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), स्नैपशॉट द्वारा रोके गए ब्लॉक।
- [Ceph RBD कमांड संदर्भ](https://docs.ceph.com/en/squid/man/8/rbd/), इमेज उपयोग और स्नैपशॉट।
- [NFSv4.2 विनिर्देश](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), सर्वर पर जगह लौटाना।
- [PBS रखरखाव दस्तावेज़](https://pbs.proxmox.com/docs/maintenance.html), pruning और बेकार डेटा की सफ़ाई।
- [QEMU डिस्क-इमेज utility](https://www.qemu.org/docs/master/tools/qemu-img.html), बंद अवस्था में इमेज conversion सुरक्षा।
