---
title: "الدليل النهائي: تحديثات Linux دون اتصال لـ Ubuntu Debian و CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["تحديثات Linux", "أوبونتو", "ديبيان", "CentOS", "RHEL", "التحديثات في وضع عدم الاتصال", "المستودع المحلي", "مخبأ", "إعداد الخادم", "إعداد العميل", "مرآة مناسبة", "debmirror", "مبتدئ", "apt-cacher-ng", "يم كرون", "تحديثات نظام Linux", "تحديثات الحزمة في وضع عدم الاتصال", "تحديثات البرامج في وضع عدم الاتصال", "مستودع الحزم المحلي", "ذاكرة التخزين المؤقت للحزمة المحلية", "تحديثات Linux في وضع عدم الاتصال", "التعامل مع التحديثات في وضع عدم الاتصال", "طرق التحديث حاليا", "صيانة النظام حاليا", "تحديثات خادم Linux", "تحديثات عميل Linux", "إدارة البرامج في وضع عدم الاتصال", "إدارة الحزمة حاليا", "تحديث الاستراتيجيات", "تحديثات أمان Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "رسم توضيحي للرسوم المتحركة يصور خادمًا وأجهزة عميل متعددة تتبادل التحديثات في وضع عدم الاتصال."
coverCaption: ""
---

** أفضل الطرق للتعامل مع تثبيت تحديثات Linux في وضع عدم الاتصال لـ Ubuntu / Debian و CentOS / RHEL **

تعد تحديثات Linux ضرورية للحفاظ على أمان واستقرار نظامك. ومع ذلك ، في بعض السيناريوهات ، قد تضطر إلى التعامل مع البيئات غير المتصلة بالإنترنت حيث يكون الاتصال بالإنترنت محدودًا أو غير موجود. في مثل هذه الحالات ، يصبح من الضروري أن يكون لديك إستراتيجية مناسبة لتثبيت التحديثات في وضع عدم الاتصال. ستوجهك هذه المقالة عبر ** أفضل الطرق للتعامل مع تثبيت تحديثات Linux لـ Ubuntu / Debian و CentOS / RHEL ** في البيئات غير المتصلة بالإنترنت ، مع التركيز بشكل خاص على استخدام مستودع محلي أو ذاكرة تخزين مؤقت.

## إنشاء مستودع محلي

يعد إعداد مستودع محلي من أكثر الطرق فعالية للتعامل مع التحديثات دون اتصال بالإنترنت. يحتوي المستودع المحلي على جميع حزم البرامج والتحديثات الضرورية ، مما يسمح لك بتحديث نظامك دون اتصال بالإنترنت. إليك كيفية إعداد مستودع محلي للتوزيعات المستندة إلى دبيان والتوزيعات القائمة على Red Hat:

### لـ Debian / Ubuntu

1. ابدأ بإعداد ** مرآة مستودع دبيان ** على خادم متصل بالإنترنت. يمكنك استخدام أدوات مثل [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) لإنشاء نسخة متطابقة محلية من مستودعات دبيان أو أوبونتو الرسمية.

#### إعداد مرآة مستودع دبيان مع apt-mirror:

```shell
# Install apt-mirror
sudo apt-get install apt-mirror

# Edit the apt-mirror configuration file
sudo nano /etc/apt/mirror.list

# Uncomment the deb line for the desired repository
# For example, uncomment the line for Ubuntu 20.04:
# deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse

# Specify the mirror location
# Modify the base_path to your desired location
set base_path /path/to/mirror

# Save and close the file

# Run apt-mirror to start the mirroring process
sudo apt-mirror

# Wait for the mirroring process to complete
```

#### إنشاء مرآة مستودع دبيان مع debmirror:
```shell
# Install debmirror
sudo apt-get install debmirror

# Create a directory to store the mirror
sudo mkdir /path/to/mirror

# Run debmirror to start the mirroring process
# Replace <RELEASE> with the Debian or Ubuntu release and <MIRROR_URL> with the official repository URL
# For example, to mirror Ubuntu 20.04:
sudo debmirror --arch=amd64 --verbose --method=http --dist=<RELEASE> --root=<MIRROR_URL> /path/to/mirror

# Wait for the mirroring process to complete
```
#### تعليمات عميل دبيان

2. تكوين المستودع المحلي الخاص بك عن طريق تحرير **`/etc/apt/sources.list` ملف على نظام غير متصل بالشبكة. استبدل عناوين URL للمستودع الافتراضي بعنوان URL للمستودع المحلي. على سبيل المثال ، إذا كان مستودعك المحلي مستضافًا في `http://local-repo/ubuntu` تحديث `sources.list` وفقًا لذلك.

مثال `/etc/apt/sources.list` ملف:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. بمجرد تحديث التكوين ، يمكنك تشغيل **`apt update` الأمر على النظام غير المتصل لجلب قوائم الحزم من المستودع المحلي.

```shell
sudo apt update
```

4. أخيرًا ، يمكنك استخدام **`apt upgrade` الأمر لتثبيت التحديثات المتاحة من المستودع المحلي.

```shell
sudo apt upgrade
```

### لـ CentOS / RHEL

1. لإعداد مستودع محلي لـ CentOS / RHEL ، تحتاج إلى استخدام ملف [**`createrepo`**](https://linux.die.net/man/8/createrepo) أداة. تقوم هذه الأداة بإنشاء البيانات الأولية الضرورية لمستودع محلي.

2. قم بإنشاء دليل لتخزين ملفات المستودع على خادم متصل بالإنترنت. على سبيل المثال ، يمكنك إنشاء دليل يسمى **`local-repo`

3. انسخ جميع ملفات حزمة RPM ذات الصلة والتحديثات إلى **`local-repo` الدليل.

#### إنشاء مستودع محلي باستخدام coreepo:

```shell
# Install the createrepo tool
sudo yum install createrepo

# Create a directory to store the repository files
sudo mkdir /path/to/local-repo

# Move or copy the RPM package files and updates to the local-repo directory

# Run the createrepo command to generate the necessary repository metadata
sudo createrepo /path/to/local-repo

# Update the repository metadata whenever new packages are added or removed
sudo createrepo --update /path/to/local-repo
```
4. بمجرد إنشاء البيانات الوصفية للمستودع ، يمكنك نقل البيانات الوصفية بالكامل `local-repo` الدليل إلى النظام غير المتصل باستخدام محرك أقراص USB أو أي وسيلة أخرى.

5. في النظام غير المتصل بالإنترنت ، قم بإنشاء ملف `.repo` ملف في `/etc/yum.repos.d/` الدليل. قم بتوفير تفاصيل التكوين الضرورية ، مثل ملف `baseurl` مشيرا إلى دليل المستودع المحلي.

على سبيل المثال ، قم بإنشاء ملف يسمى `local.repo` في ال `/etc/yum.repos.d/` الدليل وإضافة المحتوى التالي:
```shell
sudo nano /etc/yum.repos.d/local.repo
```
```toml
[local]
name=Local Repository
baseurl=file:///path/to/local-repo
enabled=1
gpgcheck=0
```
6. احفظ الملف واخرج من المحرر.

7. بعد تكوين المستودع ، يمكنك استخدام الأمر yum update لتثبيت التحديثات من المستودع المحلي.

```shell
sudo yum update
```

سيقوم هذا الأمر بتحديث الحزم على النظام باستخدام الحزم من المستودع المحلي.

تذكر تحديث المستودع المحلي عن طريق تشغيل ملف `createrepo` الأمر عند إضافة حزم جديدة أو إزالتها من المستودع.

يرجى ملاحظة أنك ستحتاج إلى استبدال `/path/to/local-repo` بالمسار الفعلي للدليل حيث قمت بتخزين ملفات المستودع.

## إعداد مخبأ محلي

هناك طريقة أخرى للتعامل مع التحديثات في وضع عدم الاتصال وهي إعداد ذاكرة تخزين مؤقت محلية. تخزن ذاكرة التخزين المؤقت المحلية الحزم والتحديثات التي تم تنزيلها ، مما يسمح لك بتوزيعها عبر أنظمة متعددة دون الحاجة إلى تنزيلات فردية. يمكنك تعيين ذاكرة التخزين المؤقت هذه على نظام عبر الإنترنت ، ثم نقل الدليل إلى نظام غير متصل بالإنترنت للسماح للأنظمة الأخرى بالوصول إلى الحزم. إليك كيفية إعداد ذاكرة تخزين مؤقت محلية للتوزيعات المستندة إلى Debian والتوزيعات المستندة إلى Red Hat:

### لـ Debian / Ubuntu

1. التثبيت والتكوين [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) وكيل تخزين مؤقت لحزم دبيان / أوبونتو. يمكنك تثبيته عن طريق تشغيل الأمر **`sudo apt-get install apt-cacher-ng`

2. بمجرد التثبيت ، قم بتحرير **`/etc/apt-cacher-ng/acng.conf` ملف لتكوين سلوك التخزين المؤقت. تأكد من أن **`PassThroughPattern` تتضمن المعلمة عناوين URL للمستودع الضرورية.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
قم بإلغاء التعليق أو إضافة عناوين URL للمستودع الضرورية إلى المعامل PassThroughPattern. على سبيل المثال ، لتضمين مستودعات Ubuntu ، قم بإضافة السطر التالي أو إلغاء التعليق عليه:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
حفظ الملف وإنهاء المحرر.

3. ابدأ [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) الخدمة باستخدام الأمر **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. في الأنظمة غير المتصلة بالإنترنت ، قم بتكوين **`/etc/apt/apt.conf.d/02proxy` ملف للإشارة إلى ذاكرة التخزين المؤقت المحلية. استخدم السطر التالي: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
أضف السطر التالي إلى الملف ، مع استبدال <cache-server-ip> بعنوان IP لخادم ذاكرة التخزين المؤقت:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
حفظ الملف وإنهاء المحرر

5. الآن ، عند تشغيل **`apt update` و **`apt upgrade` الأوامر الموجودة على الأنظمة غير المتصلة بالإنترنت ، فسوف يستردون الحزم من ذاكرة التخزين المؤقت المحلية.

```shell
sudo apt update
sudo apt upgrade
```
ستقوم هذه الأوامر بجلب التحديثات وتثبيتها من ذاكرة التخزين المؤقت المحلية ، مما يقلل الحاجة إلى الوصول إلى الإنترنت على الأنظمة غير المتصلة بالإنترنت.

يرجى ملاحظة أنك ستحتاج إلى استبدال **`<cache-server-ip>` بعنوان IP الفعلي للجهاز حيث تم تثبيت ** apt-cacher-ng **.

### لـ CentOS / RHEL

1. بالنسبة إلى CentOS / RHEL ، يمكنك استخدام ملفات [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) لإعداد ذاكرة تخزين مؤقت محلية. قم بتثبيته عن طريق تشغيل الأمر **`sudo yum install yum-cron`

2. تحرير **`/etc/yum/yum-cron.conf` ملف وتكوين **`download_only` المعلمة **`yes` يضمن ذلك تنزيل الحزم فقط وعدم تثبيتها تلقائيًا.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. ابدأ [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) الخدمة باستخدام الأمر **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. في الأنظمة غير المتصلة بالإنترنت ، أنشئ دليلًا محليًا لتخزين الحزم التي تم تنزيلها ، على سبيل المثال ، **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. انسخ الحزم التي تم تنزيلها من النظام عبر الإنترنت إلى دليل التخزين المؤقت المحلي.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

يستبدل `/path/to/local/cache` مع المسار إلى دليل التخزين المؤقت المحلي على النظام غير المتصل.

6. في الأنظمة غير المتصلة بالإنترنت ، قم بإنشاء ** جديد`.repo` ملف في **`/etc/yum.repos.d/` الدليل ، مشيرًا إلى دليل ذاكرة التخزين المؤقت المحلي.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
أضف المحتوى التالي إلى الملف ، مع استبدال `<local-cache-path>` بالمسار إلى دليل ذاكرة التخزين المؤقت المحلي:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
حفظ الملف وإنهاء المحرر.

7. أخيرًا ، يمكنك استخدام **`yum update` الأمر على الأنظمة غير المتصلة بالإنترنت لتثبيت التحديثات من ذاكرة التخزين المؤقت المحلية.

```shell
sudo yum update
```

سيقوم هذا الأمر بتحديث الحزم على الأنظمة غير المتصلة باستخدام الحزم من ذاكرة التخزين المؤقت المحلية.

يرجى ملاحظة أنك ستحتاج إلى استبدال **`<local-cache-path>` مع المسار الفعلي إلى دليل التخزين المؤقت المحلي على النظام غير المتصل.

______

## خاتمة

قد يكون التعامل مع تحديثات Linux في البيئات غير المتصلة بالإنترنت أمرًا صعبًا ، ولكن باستخدام النهج الصحيح ، يمكنك ضمان أن تظل أنظمتك محدثة وآمنة. في هذه المقالة ، ناقشنا أفضل الطرق للتعامل مع تثبيت التحديثات في وضع عدم الاتصال لـ Ubuntu / Debian و CentOS / RHEL. استكشفنا إنشاء مستودع محلي وإعداد ذاكرة تخزين مؤقت محلية ، وتقديم إرشادات خطوة بخطوة للتوزيعات المستندة إلى دبيان والتوزيعات المستندة إلى Red Hat.

باتباع هذه الطرق ، يمكنك الحفاظ على أمان واستقرار أنظمة Linux الخاصة بك ، حتى في البيئات غير المتصلة بالإنترنت. تذكر تحديث المستودع المحلي أو ذاكرة التخزين المؤقت بشكل دوري لتضمين آخر التحديثات.

______

## مراجع

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
