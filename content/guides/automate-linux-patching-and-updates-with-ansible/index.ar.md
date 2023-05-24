---
title: "أتمتة تصحيح وتحديثات Linux باستخدام Ansible: دليل شامل"
date: 2023-05-28
toc: true
draft: false
description: "تعرف على كيفية أتمتة تصحيح وتحديثات Linux باستخدام Ansible ، والتي تغطي التوزيعات المختلفة وإرشادات الإعداد."
tags: ["ترقيع لينكس", "أتمتة أنسبل", "أتمتة التحديثات", "صيانة النظام", "أتمتة تكنولوجيا المعلومات", "إدارة التصحيح", "أمان Linux", "ديبيان", "أوبونتو", "RHEL", "جبال الألب", "استقرار النظام", "التخفيف من الضعف", "البنية التحتية لتكنولوجيا المعلومات", "أداة الأتمتة", "كتاب اللعب أنسبل", "تكوين المضيف", "تحديثات البرنامج", "الامتثال الأمني", "عمليات تكنولوجيا المعلومات", "تحديثات Linux", "أوبونتو", "ديبيان", "CentOS", "RHEL", "التحديثات في وضع عدم الاتصال", "المستودع المحلي", "مخبأ", "إعداد الخادم", "إعداد العميل", "مرآة مناسبة", "debmirror", "مبتدئ", "apt-cacher-ng", "يم كرون", "تحديثات نظام Linux", "تحديثات الحزمة في وضع عدم الاتصال", "تحديثات البرامج في وضع عدم الاتصال", "مستودع الحزم المحلي", "ذاكرة التخزين المؤقت للحزمة المحلية", "تحديثات Linux في وضع عدم الاتصال", "التعامل مع التحديثات في وضع عدم الاتصال", "طرق التحديث حاليا", "صيانة النظام حاليا", "تحديثات خادم Linux", "تحديثات عميل Linux", "إدارة البرامج في وضع عدم الاتصال", "إدارة الحزمة حاليا", "تحديث الاستراتيجيات", "تحديثات أمان Linux"]
cover: "/img/cover/A_colorful_cartoon-style_image_depicting_a_robot_applying_patches.png"
coverAlt: "صورة ملونة بأسلوب كرتوني تصور روبوتًا يطبق تصحيحات على مجموعة من خوادم Linux."
coverCaption: ""
---

** أتمتة Linux Patching and Updates مع Ansible **

في عالم اليوم سريع الخطى والمراعي للأمان ، ** الأتمتة ** يعد تصحيح أنظمة Linux وتحديثها أمرًا بالغ الأهمية لضمان استقرار النظام وتخفيف نقاط الضعف. مع توفر العديد من توزيعات Linux ، قد يكون من الصعب إدارة التحديثات عبر الأنظمة الأساسية المختلفة بكفاءة. لحسن الحظ ، توفر ** Ansible ** ، وهي أداة أتمتة قوية ، حلاً موحدًا لأتمتة التصحيح والتحديثات عبر توزيعات Linux المختلفة. في هذه المقالة ، سوف نستكشف كيفية استخدام Ansible لأتمتة عملية التصحيح والتحديث للتوزيعات الأخرى ** المستندة إلى Debian ، والمستندة إلى Ubuntu ، والقائمة على RHEL ، والمستندة إلى Alpine ** ، والتوزيعات الأخرى. سنقدم أيضًا مثالاً مفصلاً عن دليل التشغيل Ansible الذي يعالج تثبيت التصحيحات والتحديثات على توزيعات Linux المختلفة ، جنبًا إلى جنب مع إرشادات حول إعداد بيانات اعتماد Ansible وملفات المضيف لجميع الأنظمة المستهدفة.

## المتطلبات الأساسية

قبل الغوص في عملية الأتمتة ، دعنا نتأكد من توفر المتطلبات الأساسية اللازمة لدينا. وتشمل هذه:

1. ** التثبيت Ansible **: لاستخدام Ansible ، تحتاج إلى تثبيته على النظام الذي ستقوم من خلاله بتشغيل مهام الأتمتة. يمكنك متابعة وثائق Ansible الرسمية على [how to install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html) للحصول على تعليمات مفصلة.

2. ** تكوين المخزون **: إنشاء ملف جرد يسرد الأنظمة المستهدفة التي تريد إدارتها باستخدام Ansible. يجب أن يكون لكل نظام ** عنوان IP أو اسم المضيف ** المحدد. على سبيل المثال ، يمكنك إنشاء ملف مخزون باسم `hosts.ini` بالمحتوى التالي:

```ini
[debian]
debian-host ansible_host=<debian_ip_address>

[ubuntu]
ubuntu-host ansible_host=<ubuntu_ip_address>

[rhel]
rhel-host ansible_host=<rhel_ip_address>

[alpine]
alpine-host ansible_host=<alpine_ip_address>
```

يستبدل `<debian_ip_address>` `<ubuntu_ip_address>` `<rhel_ip_address>` و `<alpine_ip_address>` مع عناوين IP أو أسماء المضيف الخاصة بالأنظمة المستهدفة.

3. ** وصول SSH **: تأكد من أن لديك وصول SSH إلى الأنظمة المستهدفة باستخدام المصادقة القائمة على مفتاح SSH. سيسمح ذلك لـ Ansible بالاتصال الآمن بالأنظمة وأداء المهام الضرورية.

## Ansible Playbook للترقية والتحديث

لأتمتة عملية التصحيح والتحديث لتوزيعات Linux المختلفة ، يمكننا إنشاء دليل Ansible الذي يتعامل مع تثبيت التصحيحات والتحديثات على توزيعات مختلفة. فيما يلي مثال على دليل التشغيل:

```yaml
---
- name: Patching and Updating Linux Systems
  hosts: all
  become: yes

  tasks:
    - name: Update Debian-based Systems
      when: ansible_os_family == 'Debian'
      apt:
        update_cache: yes
        upgrade: dist

    - name: Update RHEL-based Systems
      when: ansible_os_family == 'RedHat'
      yum:
        name: '*'
        state: latest

    - name: Update Alpine-based Systems
      when: ansible_os_family == 'Alpine'
      apk:
        update_cache: yes
        upgrade: yes
```

في الدليل أعلاه:

- ال `hosts` يحدد السطر الأنظمة المستهدفة لكل مهمة. سيتم تشغيل دليل التشغيل على الأنظمة المجمعة ضمن `debian` `ubuntu` `rhel` و `alpine`
- ال `become: yes` يسمح بيان قواعد اللعبة بالعمل بامتيازات إدارية.
- تقوم المهمة الأولى بتحديث الأنظمة المستندة إلى Debian و Ubuntu باستخدام `apt` وحدة.
- تقوم المهمة الثانية بتحديث الأنظمة القائمة على RHEL باستخدام `yum` وحدة.
- المهمة الثالثة هي تحديث الأنظمة القائمة على جبال الألب باستخدام `apk` وحدة.

لاحظ أن المهام مشروطة بناءً على أسماء المجموعات لاستهداف الأنظمة المناسبة.

## إعداد أوراق اعتماد Ansible وملفات المضيف

لتكوين بيانات اعتماد Ansible وملفات المضيف للأنظمة المستهدفة ، اتبع الخطوات التالية:

1. أنشئ ملف ** Ansible Vault ** لتخزين المعلومات الحساسة مثل بيانات اعتماد SSH. يمكنك استخدام الأمر التالي لإنشاء ملف قبو:
```shell
ansible-vault create credentials.yml
```
2. تحديث ملف الجرد (`hosts.ini` باستخدام بيانات اعتماد SSH المناسبة لكل نظام مستهدف. على سبيل المثال:
```ini
[debian]
debian-host ansible_host=<debian_ip_address> ansible_user=<debian_username> ansible_ssh_pass=<debian_ssh_password>

[ubuntu]
ubuntu-host ansible_host=<ubuntu_ip_address> ansible_user=<ubuntu_username> ansible_ssh_pass=<ubuntu_ssh_password>

[rhel]
rhel-host ansible_host=<rhel_ip_address> ansible_user=<rhel_username> ansible_ssh_pass=<rhel_ssh_password>

[alpine]
alpine-host ansible_host=<alpine_ip_address> ansible_user=<alpine_username> ansible_ssh_pass=<alpine_ssh_password>
```

يستبدل `<debian_ip_address>` `<ubuntu_ip_address>` `<rhel_ip_address>` و `<alpine_ip_address>` مع عناوين IP الخاصة بالأنظمة المستهدفة. أيضا ، استبدل `<debian_username>` `<ubuntu_username>` `<rhel_username>` و `<alpine_username>` بأسماء مستخدمي SSH المناسبة لكل نظام. أخيرًا ، استبدل `<debian_ssh_password>` `<ubuntu_ssh_password>` `<rhel_ssh_password>` و `<alpine_ssh_password>` بكلمات مرور SSH المقابلة.

3. تشفير ملف hosts.ini باستخدام Ansible Vault:
   
```shell
ansible-vault encrypt hosts.ini
```

أدخل كلمة مرور المخزن عندما يُطلب منك ذلك.

من خلال الخطوات المذكورة أعلاه ، قمت بإعداد بيانات الاعتماد Ansible الضرورية وملفات المضيف لجميع الأنظمة المستهدفة

## تشغيل الكتيب
لتشغيل دليل التشغيل وأتمتة عملية التصحيح والتحديث ، اتبع الخطوات التالية:

1. افتح Terminal وانتقل إلى الدليل حيث يوجد لديك ملف playbook وملف الجرد المشفر.

2. قم بتشغيل الأمر التالي لتنفيذ دليل التشغيل ، مع توفير كلمة مرور المخزن عندما يُطلب منك ذلك:

```shell
ansible-playbook -i hosts.ini playbook.yml --ask-vault-pass
```

3. سوف يتصل Ansible بالأنظمة المستهدفة ، واستخدام بيانات الاعتماد المقدمة ، وتنفيذ المهام المحددة ، وتحديث الأنظمة وفقًا لذلك.

تهانينا! لقد نجحت في أتمتة التصحيح والتحديث لتوزيعات Linux المختلفة باستخدام Ansible. باستخدام كتاب التشغيل Ansible والإعداد المناسب لبيانات الاعتماد وملفات المضيف ، يمكنك الآن إدارة عملية التصحيح والتحديث بكفاءة عبر بنية Linux الأساسية.

## خاتمة

تعمل أتمتة التصحيح والتحديث لأنظمة Linux باستخدام Ansible على تبسيط العملية وتبسيطها ، مما يسمح لمسؤولي النظام بإدارة التحديثات بكفاءة عبر توزيعات Linux المختلفة. باتباع الإرشادات الواردة في هذه المقالة ، تعلمت كيفية إنشاء دليل Ansible الذي يتعامل مع تثبيت التصحيحات والتحديثات على توزيعات Linux المختلفة. بالإضافة إلى ذلك ، قمت بإعداد بيانات اعتماد Ansible وملفات المضيف لاستهداف الأنظمة المطلوبة. احتضن قوة الأتمتة واستمتع بمزايا بنية Linux الأساسية الأكثر أمانًا وصيانتها جيدًا.

## مراجع

1. [Ansible Documentation](https://docs.ansible.com/)
2. [Official Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
