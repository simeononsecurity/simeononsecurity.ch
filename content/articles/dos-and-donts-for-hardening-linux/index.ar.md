---
title: "Qué hacer y qué no hacer esencial para endurecer tu sistema Linux"
date: 2023-02-28
toc: true
draft: false
description: "Aprende lo esencial que debes y no debes hacer para endurecer tu sistema Linux, incluyendo actualizaciones, uso de cortafuegos, habilitación de SELinux o AppArmor, configuración de políticas de contraseñas y monitorización de registros del sistema."
tags: ["seguridad Linux", "endurecimiento del sistema", "cortafuegos", "SELinux", "AppArmor", "política de contraseñas", "actualizaciones del sistema", "registros del sistema", "módulos de seguridad", "políticas de control de acceso", "ciberseguridad", "seguridad del sistema", "seguridad de la red", "gestión de vulnerabilidades", "buenas prácticas de seguridad", "seguridad informática", "seguridad de la información", "actualizaciones de software", "acceso root", "gestor de contraseñas"].
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Un candado de dibujos animados sosteniendo un escudo con la palabra Linux en él, mientras una flecha rebota en el escudo".
coverCaption: ""
---
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade

```
```bash
sudo yum update
```
Bash
sudo yum autoremove
```
```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```
```bash
sudo ufw allow http
```
Bash
sudo ufw deny from <dirección_ip>
```
Bash
sudo ufw delete <número_de_regla>
```
```bash
sudo ufw status
```
```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```
```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```
```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<dirección_ip>" reject'
sudo firewall-cmd --reload
```
Bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```
Bash
sudo firewall-cmd --list-all
```
Bash
sestatus
```
Bash
sudo yum install selinux-policy selinux-policy-targeted
```
```bash
sudo nano /etc/selinux/config
```
```
SELINUX=forzar
```
Bash
sudo apparmor_status
```
```bash
sudo apt-get install apparmor
```
```bash
sudo nano /etc/default/grub
```
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```
```bash
sudo update-grub
```
```bash
sudo apt-get install libpam-pwquality
```
```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```
``bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```
```bash
sudo journalctl
```
Bash
sudo journalctl -u sshd
```
Bash
sudo journalctl --since "hace 1 hora"
```


 
 Linux هو نظام تشغيل شائع يستخدمه الشركات العربية على حد سواء. نظام المساعدة في نظام نظام المساعدة في نظام المساعدة في نظام المساعدة
 
 ## افعل:
 
 ### حافظ على نظامك محدثًا
 
 يعد تحديث نظام [Linux] (https://simeononsecurity.ch/articles/how-do-i-learn-linux/) محدثًا أمرًا ضروريًا للحفاظ على أمانه. تساعد التحديثات الأمنية والأخطاء في التثبيت. فيما يلي بعض الأمثلة حول كيفية تحديث نظام Linux باستخدام مدير الحزم ** apt-get ** أو ** yum **:
 
 #### تحديث Ubuntu باستخدام apt-get
 
 تحديث نظام أوبونتو الخاص بك ** apt-get ** ، افتح نافذة طرفية واكتب:
 
 تحميل أحدث تنزيلات أخبار الحزم من مستودعات حزم Ubuntu. ما هو الحال بالنسبة لتصحيح الأمر؟
 
 
 تحميل هذا إلى تنزيل وتثبيت أي تحديثات متوفرة لنظامك.
 
 ### تحديث CentOS باستخدام yum
 
 تحديث نظام CentOS الخاص بك ** yum ** ، افتح نافذة طرفية واكتب:
 
 
 تحميل هذا إلى تنزيل وتثبيت أي تحديثات متوفرة لنظامك. حذفت أيضًا في استخدام الأمر التالي لتنظيف حزم قديمة أو غير مذبة:
 
 
 هذا إلى نظامك.
 
 تؤكد أن تتحقق بانتظام من التحديثات وتثبيتها على نظام Linux لديك ضمان أمانه واستقراره.
 
 
 ### استخدام جدار حماية
 
 يعد جدارًا إجراءً أمنيًا أساسيًا لأي نظام Linux ، حيث يساعد في الحماية من الوصول إليه والتهديدات الإلكترونية الأخرى. فيما يلي كيفية استخدام جدار الحماية ** ufw ** على نظام Linux الخاص بك:
 
 #### تثبيت وتمكين ufw للأنظمة المستندة إلى أوبونتو
 
 لتثبيت وتمكين ** ufw ** ، افتح نافذة طرفية واكتب:
 
 
 نص بحركة مرور HTTP (المنفذ 80):
 
 
 لحظر حركة المرور للرسائل من عنوان IP محدد:
 
 
 لحذف قاعدة:
 
 يمكنك عرض قواعد ** ufw ** الحالية عن طريق كتابة:
 
 
 
 سيعرض هذه القواعد الحالية وحالتها.
 
 مراجعة قواعد ** ufw **
 
 
 #### تثبيت وتمكين جدار الحماية للأنظمة القائمة على CentOS
 
 لتثبيت وتمكين جدار الحماية
 
 
 تم هذا إلى تثبيت ** جدار ** وتمكينه على نظامك.
 
 #### تكوين قواعد جدار الحماية للأنظمة المستندة إلى CentOS
 
 تمكين ** فاير وولد ** ، يمكنك تكوين قواعده بحركة عقربات الحظر ، أو حظرها. بعضها ببعض:
 
 حركة بحركة مرور SSH للرسائل (المنفذ 22):
 
 
 نص بحركة مرور HTTP (المنفذ 80):
 
 
 لحظر حركة المرور للرسائل من عنوان IP محدد:
 
 
 لحذف قاعدة:
 
 
 يمكنك عرض قواعد ** جدار الحماية ** الحالية عن طريق كتابة:
 
 
 سيعرض هذه القواعد الحالية وحالتها.
 
 مراجعة قواعد ** جدار الحماية ** تأكدها للتأكد من أن نظامك
 
 ### تمكين SELinux أو AppArmor
 
 SELinux (Linux المحسن بالأمان) و AppArmor وحدتا أمان يمكن استخدامهما لفرض سياسات التحكم في الوصول إلى أنظمة Linux. بشكل افتراضي ، تأتي معظم توزيعات Linux الحديثة مع تثبيت SELinux أو AppArmor ، ويمكن الوصول إليه وتهيئتها لتحسين أمان نظامك.
 
 #### تمكين SELinux للأنظمة القائمة على CentOS
 
 تم فتح أمر أمر تشغيل SELinux على نظام الأمر ، الأمر التالي:
 
 
 ، بداياته ، الأمر التالي:
 
 
 توزيعات SELinux ، تحتاج إلى تحرير ملف ** / etc / selinux / config ** وتعيين متغير ** SELINUX ** على ** فرض **:
 
 ** تغيير SELINUX = فرض **
 
 احفظ الملف واخرج منه باستخدام CTRL + X و Y ثم أدخل ، أعد تشغيل نظامك.
 
 #### تمكين AppArmor للأنظمة المستندة إلى Ubuntu
 
 فتح ، إصدار ، بإصدار الأمر ، بإصدار الأمر التالي:
 
 
 يتم تثبيت تثبيت AppArmor ، حيث تم تثبيت هذا النمط.
 
 زيادة AppArmor ، تحتاج إلى تحرير ملف ** / etc / default / grub ** رابط المعلمة ** security = apparmor ** إلى متغير ** GRUB_CMDLINE_LINUX **:
 
 ** أضف الأمان = apparmor **
 
 احفظ الملف واخرج منه ، باستخدام CTRL + X و Y ، أدخل قم بعملية الأمر لتحديث أداة تكوين نظام التشغيل:
 
 
 أخيرًا ، أعد تشغيل نظامك.
 
 تمكين SELinux أو AppArmor ، يمكنك تكوين سياسات لتقييديد امتيازات العمليات وتقييد وصولهم إلى النظام الأساسي. فرص العمل لهجوم تعزيز الأمان لعامك.
 
 
 ### تكوين سياسات كلمات المرور
 
 يعد تكوين سياسات كلمات المرور خطوة مهمة في نظام Linux الخاص بك. هناك حالات معينة في حالة آمنة ومحكمة. فيما يلي كيفية تكوين سياسات كلمات المرور على نظام Linux الخاص بك:
 
 #### تكوين سياسات كلمات المرور على Ubuntu
 
 لتكوين سياسات كلمات المرور على Ubuntu ، يمكنك استخدام وحدة ** pam_pwquality **. توفر الوحدة مجموعة من اختبارات القوة التي يمكن استخدامها لفرضرض سياسات كلمة المرور. لتثبيت وحدة ** pam_pwquality ** ، افتح نافذة طرفية واكتب:
 
 
 تثبيت الوحدة ، يمكنك تكوين إعدادات طريق تحرير ملف ** / etc / pam.d / Common-password **. على سبيل المثال ، لفرض حد أدنى من الوجود ، يمكنك إضافة السطر التالي إلى الملف:
 
 
 يمكنك أيضًا تكوين إعدادات أخرى ، مثل الحد الأقصى لعمر كلمة المرور ، عن طريق إضافة سطور إلى الملف.
 
 #### تكوين سياسات كلمات المرور على CentOS
 
 لتكوين سياسات كلمات المرور على CentOS ، يمكنك استخدام أداة ** authconfig **. توفر هذه المساحة مجموعة من الخيارات التي يمكن لفكرة لتكوين سياسات كلمات المرور. المثال ، المثال ، المثال ، طويل. وقت طويل ، الحرف الأول ، الحرف الأول ، الحرف الأول
 
 
 هذا تحديث ملفات النظام ** / etc / بام ظام. d / system-auth ** و ** / etc / pam.d / password-auth ** الخاصة بالنفعرض سياسات كلمات المرور.
 
 مراجعة ويكيبيديا
 
 
 ### مراقبة نظام التنظيم الخاص بك
 
 نظام Linux الخاص بالإدارة تسجل النشاط ، محاولة تسجيل الأخطاء والأخطاء والأحداث والأحداث ،
 
 #### استخدام الأمر Journalctl
 
 في معظم توزيعات Linux الحديثة ، استخدام الأمر ** journalctl ** يوفر هذا الأمر مجموعة متنوعة من الخيارات التي يمكن لفكرة إدخالات البحث.
 
 لعرض جميع إدخالات السجل ، ما عليك سوى الأمر ، الأمر التالي:
 
 
 سيعرض هذا جميع إدخالات السجل ، أحدث الإدخالات في الأسفل.
 
 لتصفية إدخالات السجل حسب وحدة معينة ، مثل خدمة أو عملية ، يمكنك استخدام الخيار ** - u ** متبوعًا باسم الوحدة. على سبيل المثال ، لعرض إدخالات السجل لخدمة ** sshd ** ، يمكنك تشغيل الأمر التالي:
 
 
 لتصفية إدخالات السجل حسب نوع المنظمة ، يمكنك استخدام الخيار ** - منذ ** و ** - حتى **
 
 
 #### استخدام أداة إدارة السجل
 
 بالنسبة للأنظمة الأكبر أو الأكثر تعقيدًا ؛ توفر توفر إمكانية الوصول إلى مجموعة الحلول الأمنية في الوقت الحالي.
 
 أقدم برامج إدارة نظام Linux ما يلي:
 
 - ** Logwatch **: أداة بسيطة لتحليل j jan jan janّح j
 - ** Logrotate **: أداة تعمل بتدوير ملفات السجل وضغطها على مساحة القرص
 - ** Pila ELK **: قاعدة بيانات مفتوحة مفتوحة المصدر
 
 وراجع مراجعة النظام السابق.
 
 ______
 
 ## لا تفعل:
 
 ### استخدم كلمات مرور ضعيفة
 
 يعتبر نظام لينكس عرضة للهجمات. يمكن استخدام الكلمات الرئيسية لاستخدامها في ممارسة الجنس. من المهم استخدام كلمات مرور قوية وفريدة من نوعها يصعب تخمينها.
 
 يمكنك إنشاء كلمات مرور قوية في الأحرف الكبيرة والصغيرة والأرقام والأحرف الخاصة. تستخدم أيضًا استخدام [مدير كلمات المرور] (https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) تجارة كلمات مرور معقدة وتخزينها بشكل آمن. يمكن أن يساعدك في [مديرو كلمات المرور] (https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) على تذكر كلمات المرور الخاصة بك وتجنب استخدام نفس استخدام كلمة المرور لحسابات متعددة.
 
 ### السماح بالوصول إلى SSH root
 
 يمكن السماح بالوصول إلى SSH root. استخدام حساب مستخدم لحساب الدخول إلى نظامك ثم إجراء عمليات تسجيل الدخول إلى الامتيازات التجارية ** sudo **. تقييد هذا الحد من عائدات بيع قطع الغيار.
 
 ### تثبيت البرامج غير المحفوظة
 
 يمكن أن يؤدي يؤدي إلى تثبيت البرامج على القرص المضغوط لنظام Linux الخاص بك ، مما يجعله أكثر عرضة للهجمات. من المهم فقط أن تعلق على البرامج التي تعلقها بالنظام. يساعد في تقليل مخاطره.
 
 ### استخدام برامج قديمة
 
 قد يؤدي استخدام برامج قديمة إلى ظهورك. من ناحية أخرى ، برجاء إصدار إصدارات من البرنامج. يساعد هذا في تصحيح الثغرات الأمنية المعروفة نظامك من يساعده
 
 ______
 
 ## خاتمة
 
 في الختام ، يعد تقوية نظام Linux ، أمر مهم لحماية أمانه وحماية البيانات التي يحتفظ بها. في ضوء المقالة ، تم اتخاذ خطوات مهمة في هذا المقال تذكر تحديث نظامك ، واستخدامه ، وتكوينه ، وتكوين سياسات كلمات المرور ، وتسجيل النظام. تجنب استخدام كلمات مرور ضعيفة ، وتعطيل البرامج المرفقة ، والسماح بالوصول إلى SSH الجذر ، وتثبيت البرامج غير الزراعية ، واستخدام المبردات القديمة. وضع وضع جيد لوضع نظام Linux.
 
 ## مراجع:
 
 - [دليل تعزيز Linux الخاص بمركز أمان الإنترنت] (https://www.cisecurity.org/cis-hardened-images/)
 - [دليل أمان Red Hat Enterprise Linux] (https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
 - [وثائق أمان Ubuntu] (https://ubuntu.com/security)
 - [Wiki de seguridad de Linux] (https://en.wikibooks.org/wiki/Linux_Security)
