---
title: "دليل ترقية Proxmox VE من الإصدار 8 إلى 9"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "رقِّ Proxmox VE من الإصدار 8 إلى 9 باستخدام فحوصات المتطلبات المسبقة والخطوات اليدوية والأتمتة، مع مراجعة التغييرات غير المتوافقة وإرشادات الاسترداد."
genre: ["الافتراضية", "إدارة Linux", "افتراضية Proxmox", "إدارة الخوادم", "برمجيات مفتوحة المصدر", "مختبر منزلي"]
tags: ["Proxmox VE، الإصدار 9", "ترقية Proxmox", "PVE من 8 إلى 9", "Debian Trixie", "Debian، الإصدار 13", "apt dist-upgrade", "pve8to9", "Ceph على Proxmox", "proxmox-boot-tool", "grub-efi", "ترقية LVM", "ترقية ZFS", "NVIDIA vGPU", "cgroupv2", "أتمتة Proxmox", "نص ترقية Bash", "ترقية مجموعة Proxmox", "ترقية في المكان", "pve8to9-upgrade.sh", "Proxmox VE، الإصدار 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "غرفة خوادم حديثة تعرض شاشاتها رموزًا مضيئة تمثل الأجهزة الافتراضية. يعمل فني على حاسوب محمول وسط معدات زرقاء داكنة بلمسات زرقاء وخضراء وبنفسجية زاهية."
coverCaption: "ترقية Proxmox VE من الإصدار 8 إلى 9: خطوات الترقية في المكان بمساعدة نص آلي."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**صدر Proxmox VE 9.0 مع Debian 13 Trixie والنواة 6.14 وQEMU 10 وLXC 6 وZFS 2.3.** يشرح هذا الدليل مسار الترقية اليدوية في المكان، كما يشرح نص Bash آليًا يكتشف إعدادك ويتعامل مع تغييرات المستودعات والمشكلات المعروفة والفحوصات الأولية.

## الجديد في Proxmox VE 9

Proxmox VE 9، الذي صدر في أغسطس 2025، ترقية رئيسية. تشمل التغييرات الأساسية:

| المكوّن | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **قاعدة Debian** | Bookworm (12) | Trixie (13) |
| **النواة الافتراضية** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (ما زال v1 ممكنًا) | cgroupv2 فقط |

يتضمن [Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) النواة 7.0 وQEMU 11 وLXC 7 وZFS 2.4 افتراضيًا. إصدار Ceph الافتراضي في 9.2 هو Tentacle، مع استمرار إتاحة Squid. الانتقال إلى Squid قبل ترقية مجموعة Ceph تعمل على VE 8 متطلب منفصل.

**تشمل الميزات الجديدة الرئيسية في PVE 9.0 وما بعده:**
- لقطات الأجهزة الافتراضية على LVM ذي التخصيص الكامل عبر سلاسل وحدات التخزين (معاينة تقنية ثم تشغيل إنتاجي في 9.1)
- قواعد التقارب للتوافر العالي بدلًا من مجموعات HA
- SDN Fabrics لشبكات Ceph كاملة الترابط باستخدام OpenFabric وOSPF
- واجهة ويب جديدة للأجهزة المحمولة (Rust/Yew)
- توسيع أجهزة ZFS RAIDZ دون توقف
- موازنة تحميل ديناميكية باستخدام Cluster Resource Scheduler (PVE 9.2)
- WireGuard وBGP كبروتوكولين لشبكات SDN (PVE 9.2)
- أصبح `/tmp` من نوع `tmpfs` (تغيير في Debian Trixie، وتُحذف الملفات دوريًا)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="رسم مقارنة بين Proxmox VE 8 وVE 9 يوضح تغييرات إصدارات النواة وQEMU وLXC وZFS وCeph" >}}

______

## قبل البدء: المتطلبات

**يجب استيفاء كل هذه المتطلبات قبل تعديل المستودعات.** راجع قائمة التحقق الكاملة في [ويكي الترقية الرسمي، قسم المتطلبات](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. يلزم Proxmox VE 8.4 أو أحدث

```bash
pveversion
```

يجب أن يعرض الناتج `pve-manager/8.4.x` أو إصدارًا أحدث. وإلا:

```bash
apt update && apt dist-upgrade
```

### 2. يجب أن يعمل Ceph بإصدار Squid (19.x)، للتكوين فائق التقارب فقط

```bash
ceph --version
```

يجب أن يعرض الناتج الإصدار 19.x (Squid). إذا كنت تستخدم Reef (18.x) أو Quincy (17.x)، فرَقِّ Ceph أولًا. انتقل بين الإصدارات خطوة واحدة في كل مرة:

- Quincy (17) → Reef (18) → Squid (19)

*لا تبدأ ترقية PVE 9 حتى تعمل جميع عقد Ceph بإصدار Squid.*

### 3. تثبيت Proxmox Backup Server على العقدة نفسها

إذا كان PBS 3.4 وPVE 8.4 على العقدة نفسها، فاتبع [تعليمات التثبيت المشترك](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) ونسّق الترقيتين في عملية APT واحدة. تحقق من إمكانية استعادة النسخ الاحتياطية وشغّل `pve8to9 --full` و`pbs3to4 --full` قبل تغيير المستودعات. عالج المشكلات التي تظهر قبل المتابعة.

### 4. متطلبات الوصول

- **مستحسن**: الوصول إلى وحدة التحكم عبر IPMI أو iKVM أو لوحة مفاتيح فعلية. سينقطع اتصال SSH عند إعادة تشغيل الخدمات.
- **SSH**: استخدم `tmux` أو `screen` لمواصلة الترقية إذا انقطع الاتصال:
  ```bash
  tmux new -s upgrade
  ```

### 5. مساحة القرص

```bash
df -h /
```

يلزم توفر **5 GB على الأقل**، ويُفضّل 10 GB أو أكثر.

### 6. نسخ احتياطية صالحة

انسخ جميع الأجهزة الافتراضية والحاويات إلى وحدة تخزين خارجية قبل المتابعة. اختبر الاستعادة. النسخة الاحتياطية الصالحة إلزامية.

______

## تغييرات غير متوافقة يجب معرفتها

اقرأ هذه النقاط قبل الترقية. يتطلب بعضها إجراءً قبل الترقية أو بعدها.

### لم يعد cgroup V1 مدعومًا

لا يدعم PVE 9 بيئة cgroupv1 القديمة مطلقًا. إذا سبق لك تمكينها:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

إذا أعاد الأمر أي نتيجة، فأزل معلمة النواة من `/etc/default/grub` وشغّل `update-grub` قبل الترقية.

**التأثير على الحاويات**: لن تعمل الحاويات التي تستخدم systemd 230 أو أقدم (CentOS 7 وUbuntu 16.04) على PVE 9. انقل أعباء العمل هذه قبل الانتقال إلى PVE 9. انتهى دعم المورّد لـ Proxmox VE 8.4 في أغسطس 2026.

### مجموعات HA مهملة

تحل قواعد HA محل مجموعات HA. وتُرحّل تلقائيًا بعد انتقال جميع عقد المجموعة إلى PVE 9. لا يلزم إجراء يدوي، لكن تحقق بعد ترقية العقدة الأخيرة.

### إزالة امتياز VM.Monitor

حدّث الأدوار المخصصة التي تشير إلى `VM.Monitor`. استخدم `Sys.Audit` للوصول الأساسي إلى مراقب KVM. يكتشف نص `pve8to9` الأدوار المتأثرة.

### امتياز جديد: VM.Replicate

يتطلب إنشاء مهام نسخ التخزين أو تعديلها الآن امتياز `VM.Replicate` على `/vms/<vmid>`. عدّل الأدوار المخصصة إذا لزم الأمر.

### تتطلب حاويات LXC ذات الامتيازات Sys.Modify

يتطلب إنشاء حاويات جديدة ذات امتيازات الآن `Sys.Modify`. ولا يتطلب استعادة حاوية ذات امتيازات موجودة في مكانها هذا الامتياز.

### لم يعد systemd-sysctl يقرأ /etc/sysctl.conf

سيتم تجاهل أي إعدادات مخصصة في `/etc/sysctl.conf` بصمت بعد الترقية. انقلها إلى `/etc/sysctl.d/<NN>-name.conf` قبل إعادة التشغيل.

```bash
# تحقق مما يوجد في sysctl.conf
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### أصبح /tmp من نوع tmpfs

يربط Debian Trixie `/tmp` بنظام tmpfs، حتى 50% من الذاكرة. وتُحذف الملفات دوريًا أثناء تشغيل النظام. إذا استخدمت `/tmp` للملفات المؤقتة الكبيرة، فانقل العمل إلى `/var/tmp` أو نقطة ربط مخصصة.

### التوافق مع النسخ الاحتياطي والاستعادة باستخدام Veeam {#veeam-backup-broken-for-qemu-machine-version--100}

تحقق من [إصدارات Veeam Backup & Replication وملحق Proxmox](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html) قبل الترقية. تسرد المتطلبات الحالية دعم Proxmox VE من 8.2 إلى 9.2 على مضيفات x86-64 المثبتة باستخدام ISO الرسمي لـ Proxmox. للإصدارات الأقدم من Veeam نطاقات دعم خاصة بها.

تدعم [قيود Veeam الحالية](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) نسخ الأجهزة الافتراضية احتياطيًا من وحدة تخزين مبنية على LVM مع تمكين Snapshots as Volume Chains (SAVC). ولا يعني ذلك دعم SAVC لتخزين ملفات عمال Veeam أو كوجهة Instant Recovery. تؤثر مشكلة استعادة منفصلة في [KB4773](https://www.veeam.com/kb4773) في أنواع أجهزة QEMU الأقدم من 10 مع أقراص QCOW2 المستعادة إلى تخزين SAVC في PVE 9. استخدم وجهة لا تستخدم SAVC أو استعد القرص بصيغة RAW وفقًا للتوثيق. هذه حلول بديلة للاستعادة وليست سببًا لتثبيت نوع الجهاز في كل بيئتك. اختبر النسخ الاحتياطي والاستعادة على وحدة التخزين المقصودة قبل الاعتماد على الترقية.

### قد تتغير أسماء واجهات الشبكة

تتعرف النواة 6.14 على ميزات NIC أكثر من 6.8. وقد تحصل بعض بطاقات الشبكة على لاحقات إضافية في أسمائها. يمكن لأداة `pve-network-interface-pinning` تثبيت أسماء `nicX` مستقرة لجميع الواجهات قبل الترقية:

```bash
pve-network-interface-pinning --help
```

______

## الخيار A: ترقية يدوية في المكان

اتبع الخطوات الرسمية في [دليل ترقية Proxmox VE](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### الخطوة 1: شغّل قائمة فحص pve8to9

```bash
pve8to9 --full
```

عالج كل بند `FAIL` قبل المتابعة. أعد الفحص بعد كل إصلاح.

### الخطوة 2: انقل الأجهزة الافتراضية قيد التشغيل، إذا كانت العقدة ضمن مجموعة

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### الخطوة 3: حدّث PVE 8 بالكامل

```bash
apt update && apt dist-upgrade
pveversion   # يجب أن يعرض 8.4.1 أو أحدث
```

### الخطوة 4: حدّث مستودعات Debian الأساسية

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

علّق أو أزل أي أسطر مستودعات خاصة بـ Bookworm ما زالت موجودة.

### الخطوة 5: أضف مستودع حزم PVE 9

**Enterprise (يتطلب اشتراكًا):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**دون اشتراك:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

تحقق باستخدام `apt update && apt policy` من ظهور المستودع الجديد دون أخطاء. ثم أزل الملف القديم بامتداد `.list` أو علّق محتواه.

### الخطوة 6: حدّث مستودع Ceph، للتكوين فائق التقارب فقط

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

في إعدادات دون اشتراك، استخدم `http://download.proxmox.com/debian/ceph-squid` مع `pve-no-subscription`.

### الخطوة 7: حدّث فهرس الحزم

```bash
apt update
```

تحقق من عدم وجود أخطاء.

### الخطوة 8: نفّذ dist-upgrade

```bash
apt dist-upgrade
```

يستغرق ذلك من 5 دقائق إلى أكثر من 60 دقيقة حسب سرعة وحدة التخزين. أثناء الترقية:

- **`/etc/issue`**: احتفظ بالإصدار الحالي (آمن)
- **`/etc/lvm/lvm.conf`**: ثبّت إصدار مشرف الحزمة (مستحسن)
- **`/etc/ssh/sshd_config`**: ثبّت إصدار مشرف الحزمة إذا لم تخصص الملف
- **`/etc/default/grub`**: احتفظ بالإصدار الحالي إذا خصصت الملف
- **`/etc/chrony/chrony.conf`**: ثبّت إصدار مشرف الحزمة إذا لم تخصص الملف

### الخطوة 9: أعد التشغيل

```bash
reboot
```

يلزم إعادة التشغيل حتى إذا سبق تثبيت النواة 6.14 كخيار في PVE 8، إذ يعاد بناؤها باستخدام أدوات PVE 9.

### الخطوة 10: إجراءات ما بعد الترقية

```bash
# امسح ذاكرة التخزين المؤقت للمتصفح: Ctrl+Shift+R (أو ⌘+Alt+R على macOS)
# تحقق من جميع عقد المجموعة:
pvesh get /nodes

# في المجموعات: تنتقل مجموعات HA تلقائيًا إلى قواعد HA بعد ترقية جميع العقد إلى PVE 9
journalctl -eu pve-ha-crm  # تحقق من الأخطاء
```

______

## الخيار B: نص آلي (pve8to9-upgrade.sh)

تتضمن العملية اليدوية خطوات مشروطة كثيرة تختلف حسب الإعداد. يؤتمت نص `pve8to9-upgrade.sh` هذه الخطوات كلها.

**مصدر النص:** [مستودع Gist للنص](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### ما الذي يفعله النص

يتعامل النص تلقائيًا مع الترقية كاملة، بما في ذلك:

| ما يكتشفه | الإجراء |
|-----------|--------|
| مستودعات Enterprise أو المستودعات دون اشتراك | يستخدم نوع المستودع **المفعّل حاليًا** ولا يفعّل Enterprise على العقد دون اشتراك |
| إصدار Ceph | يتوقف عند Quincy أو Reef، ويعرض دليل ترقية Ceph خطوة بخطوة |
| نوع مستودع Ceph | يكتب `ceph.sources` جديدًا يطابق نوع المستودع الحالي |
| برنامج تشغيل NVIDIA vGPU | يتوقف إذا كان الإصدار أقدم من 570 (الحد الأدنى لـ GRID 18.3) |
| تمرير وحدة معالجة الرسومات من NVIDIA إلى آلة افتراضية | يحذّر وينشئ تذكيرًا للاختبار بعد الترقية |
| مستودعات CUDA | يحدّث `debian12` إلى `debian13` في مسارات URI |
| حزمة systemd-boot الوصفية | يزيلها (ويعالج خطأ Debian #1110177 الذي يوقف dist-upgrade) |
| إعدادات sysctl.conf المخصصة | ينقلها إلى `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| توقف FRR بعد التشغيل | يصلح `/etc/network/interfaces` قبل إعادة التشغيل |
| `systemd-journald-audit.socket` | يعطّله لتجنب إغراق السجلات أثناء الترقية |
| مشكلة GRUB مع UEFI وLVM | يثبّت `grub-efi-amd64` ويكتب ورقة استرداد في `/root/` |
| مستودعات `bookworm` التابعة لجهات خارجية | يعلّقها ويضيف تذكيرًا بتحديثها |
| تعارض `linux-image-amd64` | يزيل الحزمة إذا كانت مثبتة |
| التنشيط التلقائي لـ LVM | يشغّل نص الترحيل قبل الترقية وبعدها |
| خادم النسخ الاحتياطي من Proxmox | ينفذ فحص `pbs3to4 --full` ويحدّث مستودعات PBS لـ Trixie |
| ZFS كنظام ملفات جذر | يكتشف الإعداد ويؤكده؛ لا يلزم إجراء خاص |

تُسجّل التغييرات كلها في `/var/log/pve8to9-upgrade-<timestamp>.log`. تُحفظ نسخ مستودعات APT الاحتياطية في `/root/pve8to9-apt-backups/`. لا تنسخها بامتداد `.bak` داخل `/etc/apt/sources.list.d/`، لأن واجهة الويب ستعرض خطأ "invalid extension" (امتداد غير صالح).

### التثبيت والاستخدام

```bash
# نزّل النص
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# اجعله قابلًا للتنفيذ
chmod +x pve8to9-upgrade.sh

# راجعه قبل التشغيل (اقرأ دائمًا النصوص قبل تشغيلها بصلاحيات root)
less pve8to9-upgrade.sh
```

**أوضاع التشغيل:**

```bash
# الوضع التفاعلي الكامل (موصى به)
./pve8to9-upgrade.sh

# وافق تلقائيًا على الإصلاحات الآمنة وغير المدمرة
./pve8to9-upgrade.sh --yes

# تشغيل تجريبي: اعرض كل تغيير دون تطبيقه
./pve8to9-upgrade.sh --dry-run

# تخطَّ الفحص الأولي pve8to9 --full (غير موصى به)
./pve8to9-upgrade.sh --skip-preflight
```

*شغّله داخل `tmux` أو `screen` إذا كنت متصلًا عبر SSH.*

### مثال على ناتج النص

يعرض النص ملخصًا للإعداد المكتشف قبل أن يطلب منك المتابعة:

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

### فحوصات السلامة التي توقف النص

**سيرفض النص المتابعة** إذا تحقق أي مما يلي:

- تم تمكين cgroup V1 صراحةً في سطر أوامر النواة
- ما زال Ceph على Quincy (17.x) أو Reef (18.x)، وسيعرض أوامر ترقية Ceph المطلوبة
- إصدار برنامج تشغيل NVIDIA vGPU أقدم من 570 (GRID 18.3)
- إصدار PVE أقدم من 8.4

يعرض النص الأوامر الدقيقة لمعالجة كل مشكلة مانعة قبل إعادة الفحص.

______

## مشكلات ترقية معروفة

### فشل GRUB في الإقلاع من LVM في وضع UEFI

**ينطبق على** الأنظمة ذات الجذر على LVM، والإقلاع عبر UEFI، والتي تمت ترقيتها من PVE 7.x.

```bash
# الإصلاح (شغّله على النظام النشط بعد الترقية):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

يكتشف نص `pve8to9-upgrade.sh` UEFI مع LVM ويثبّت الحزمة تلقائيًا. كما يكتب ورقة استرداد في `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**إذا كانت العقدة متوقفة بالفعل** عند `grub rescue>` أو رسالة "disk 'lvmid/...' not found" (القرص غير موجود):

1. أقلع من ISO الخاص بـ PVE ثم اختر Advanced → **Rescue Boot**
2. أو اتبع [خطوات استرداد GRUB لـ LVM](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) في الويكي الرسمي

### توقف الحزمة الوصفية systemd-boot عملية dist-upgrade

ثُبّتت الحزمة الوصفية `systemd-boot` تلقائيًا في جميع أنظمة PVE 8.1–8.4 المثبتة من ISO. تحتوي في Trixie على معالجات تعمل عند ترقية حزم أخرى، وقد توقف `dist-upgrade` في منتصفه إذا لم يكن ESP مربوطًا (خطأ Debian #1110177).

```bash
# أزلها قبل dist-upgrade:
apt remove systemd-boot
# لا تزل systemd-boot-efi أو systemd-boot-tools، فهما يجب أن يبقيا
```

يعالج نص `pve8to9-upgrade.sh` هذا تلقائيًا ويشرح السبب بالتفصيل.

### قد يتعطل التمرير المباشر لأجهزة PCI أحيانًا مع النواة 6.14

أبلغ بعض المستخدمين عن تعذر تشغيل الأجهزة الافتراضية التي تستخدم التمرير المباشر لأجهزة PCI على النواة 6.14. إذا واجهت ذلك:

```bash
# ثبّت النواة القديمة مؤقتًا:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### تتسبب إعدادات Ceph كاملة الترابط في توقف عند إعادة التشغيل

إذا احتوى `/etc/network/interfaces` على:

```
post-up /usr/bin/systemctl restart frr.service
```

غيّره إلى:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

نفّذ ذلك **قبل إعادة التشغيل**. يكتشف النص هذا النمط ويصلحه تلقائيًا.

### تتطلب LVM thin pool إصلاحًا

بعد الترقية، تظهر الرسالة التالية في بعض الأنظمة:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

الإصلاح:

```bash
lvconvert --repair pve/data
```

### الحد الأدنى لإصدار برنامج تشغيل NVIDIA vGPU

يلزم برنامج التشغيل **570.158.02** على الأقل (GRID 18.3) قبل الترقية. برامج التشغيل الأقدم غير متوافقة مع النواة 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## ترتيب ترقية المجموعة

رقِّ العقد واحدة تلو الأخرى. تحقق من سلامة كل عقدة قبل بدء ترقية التالية.

```bash
# تحقق من سلامة المجموعة قبل ترقية كل عقدة:
pvecm status
ceph -s   # إذا كان Ceph مستخدمًا
```

**قواعد الترحيل أثناء الترقية الجزئية:**

- نقل VM/CT من PVE 8 إلى PVE 9: يعمل دائمًا
- نقل VM/CT من PVE 9 إلى PVE 8: غير مدعوم عمومًا

بعد انتقال جميع العقد إلى PVE 9، تُنقل مجموعات HA تلقائيًا إلى قواعد تقارب HA. تحقق من الأخطاء:

```bash
journalctl -eu pve-ha-crm
```

______

## استكشاف الأخطاء وإصلاحها

### توقف الترقية: محاولة إزالة الحزمة الأساسية `proxmox-ve`

إذا ظهر:

```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

لا يمكن ترقية حزمة واحدة أو أكثر لأن مستودع Bookworm ما زال مضبوطًا. اعثر على إدخالات Bookworm المتبقية:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

علّقها ثم نفّذ:

```bash
apt update && apt dist-upgrade
```

إذا اكتملت العملية جزئيًا:

```bash
apt -f install
```

### فشل الإقلاع بعد ترقية ZFS

إذا استخدمت ZFS كنظام ملفات جذر مع إقلاع BIOS قديم، فراجع [ZFS: الانتقال من Legacy-Boot إلى Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). يجب أن يدير `proxmox-boot-tool` الإقلاع في أنظمة ZFS، لا GRUB مباشرة، لضمان استمرار الإقلاع بعد ترقيات ميزات ZFS.

______

## قائمة التحقق بعد الترقية

بعد إعادة تشغيل كل عقدة:

- [ ] امسح ذاكرة المتصفح (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] يعرض `pveversion` الإصدار 9.x
- [ ] يعرض `uname -r` الإصدار 6.14.x أو أحدث
- [ ] تبدأ جميع الأجهزة الافتراضية والحاويات على نحو صحيح
- [ ] صحة Ceph: يعرض `ceph -s` الحالة HEALTH_OK
- [ ] عند استخدام UEFI وLVM: تحقق من حداثة وقت تعديل `grubx64.efi`
- [ ] عند تمرير وحدة GPU من NVIDIA مباشرة إلى VM: اختبر VM غير إنتاجية
- [ ] حدّث مستودعات الجهات الخارجية التي عُلّقت أثناء الترقية
- [ ] انقل إعدادات `/etc/sysctl.conf` المخصصة إلى `/etc/sysctl.d/`

## التحقق بعد الترقية

بعد الترقية، تحقق من إعدادات المستودعات ونصاب المجموعة وحالة التخزين وإقلاع الأجهزة الضيفة والنسخ الاحتياطية وقواعد جدار الحماية وإمكانية الإدارة. راجع سجلات النظام قبل إعلان اكتمال الترقية. اختبر استعادة جهاز ضيف واحد على مضيف منفصل إذا كانت المجموعة تدعم ذلك.

استخدم [دليل إدارة Proxmox VE](https://pve.proxmox.com/pve-docs/) و[ملاحظات الإصدار](https://pve.proxmox.com/wiki/Roadmap) الحالية للأوامر الخاصة بكل إصدار. لا تنسخ أمرًا من إصدار قديم دون التحقق من الإصدار المستهدف وحالة النسخ الاحتياطية.

## المراجع

1. [رسمي: ترقية Proxmox VE من 8 إلى 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [رسمي: الترقية من 8 إلى 9، المتطلبات](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [نص أتمتة pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [المشكلات المعروفة في Proxmox VE 9.0 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [استعادة GRUB من فشل الإقلاع بسبب LVM، خطأ "disk not found" (القرص غير موجود)](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: الانتقال من Legacy-Boot إلى Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [دليل ترقية Ceph من Reef إلى Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [تثبيت أسماء واجهات شبكة Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [ملاحظات إصدار Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
