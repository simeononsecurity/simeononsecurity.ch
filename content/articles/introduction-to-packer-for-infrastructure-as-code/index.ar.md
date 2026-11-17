---
title: "مقدمة إلى Packer للبنية التحتية كتعليمة برمجية"
date: 2023-05-04
lastmod: 2026-11-16
toc: true
draft: false
description: "تعرّف على استخدام Packer لإنشاء صور أجهزة سهلة الصيانة وآمنة."
tags: ["Packer", "البنية التحتية كتعليمة برمجية", "التطوير والعمليات", "الأتمتة", "الأمان", "قابلية التكرار", "قابلية التوسع", "متعدد المنصات", "التحكم بالإصدارات", "الحوسبة السحابية", "صور الأجهزة", "الافتراضية", "إدارة التهيئة", "التكامل المستمر", "التسليم المستمر", "تطوير البرمجيات", "أفضل الممارسات", "الاختبار", "مفتوح المصدر", "متعدد السحابات"]
cover: "/img/cover/A_cartoon-style_image_of_a_packer_creating_different_machines.webp"
coverAlt: "رسم كرتوني لأداة تغليف تنشئ صور أجهزة لمنصات متعددة، مع حاسوب محمول وسحب في الخلفية."
coverCaption: ""
---

**مقدمة إلى استخدام Packer في تطبيقات البنية التحتية كتعليمة برمجية**

**Packer** أداة شائعة لإنشاء **صور الأجهزة** أو **قوالب الأجهزة الافتراضية** التي تساعد على نشر بيئات متطابقة عبر منصات متعددة. تؤتمت الأداة إنشاء الصور لمنصات مثل **AWS وGoogle Cloud Platform وAzure وVMware**. أنشأت HashiCorp أداة Packer مفتوحة المصدر، وهي الشركة المطورة لأدوات شائعة مثل Vagrant وConsul وTerraform.

يقدم هذا المقال أداة Packer ويوضح كيفية استخدامها لإنشاء صور أجهزة لمنصات مختلفة. كما يناقش فوائدها وبعض أفضل ممارسات استخدامها.

## ما أداة Packer؟

تؤتمت Packer عملية إنشاء صور الأجهزة لمنصات مختلفة. وهي أداة مفتوحة المصدر أنشأتها HashiCorp، مطورة أدوات أخرى مثل Vagrant وConsul وTerraform.

يمكن للمطورين استخدام Packer لإنشاء صور أجهزة أو قوالب أجهزة افتراضية لمنصات مثل AWS وGoogle Cloud Platform وAzure وVMware. ثم يمكنهم استخدام هذه الصور لنشر بيئات متطابقة عبر منصات متعددة.

## فوائد استخدام Packer

يوفر استخدام Packer عدة فوائد:

- **قابلية التكرار**: ينشئ صور الأجهزة بالطريقة نفسها في كل مرة، ما يحقق الاتساق وإمكانية تكرار النتائج بين البيئات.
- **الأتمتة**: تؤتمت عملية إنشاء الصور، وتوفر الوقت وتقلل احتمال الخطأ البشري.
- **دعم منصات متعددة**: تسهل إنشاء صور أجهزة يمكن استخدامها في بيئات مختلفة.
- **التكامل مع أدوات أخرى**: تتكامل مع Ansible وChef وPuppet، ما يتيح إنشاء الصور بالأدوات التي تستخدمها بالفعل.
- **قابلية التوسع**: تنشئ صور أجهزة متعددة بالتوازي، ما يسهل توسيع عملية الإنشاء.

## البدء باستخدام Packer

للبدء، نزّل Packer وثبّته. يتوفر لأنظمة Windows وmacOS وLinux.

نزّل Packer من الموقع الرسمي: [https://www.packer.io/downloads](https://www.packer.io/downloads)

بعد تثبيت Packer، يمكنك البدء بإنشاء صور أجهزة لمنصات مختلفة.

## إنشاء صورة جهاز باستخدام Packer

لإنشاء صورة جهاز، عرّف **قالبًا** يصف إعداداتها. يُكتب القالب بتنسيق JSON ويحدد الخطوات المطلوبة لإنشاء الصورة.

إليك مثالًا لقالب Packer ينشئ صورة جهاز على AWS:

```json
{
"builders": [{
"type": "amazon-ebs",
"access_key": "ACCESS_KEY",
"secret_key": "SECRET_KEY",
"region": "us-west-2",
"source_ami": "ami-0c55b159cbfafe1f0",
"instance_type": "t2.micro",
"ssh_username": "ubuntu",
"ami_name": "my-image-{{timestamp}}"
}]
}
```

في هذا المثال، يطلب القالب من Packer إنشاء صورة جهاز مدعومة بـAmazon EBS باستخدام صورة Ubuntu AMI. سيكون اسم الصورة الناتجة "my-image" مع إضافة طابع زمني في نهايته.

بعد تعريف قالب Packer، استخدم الأمر `packer build` لإنشاء صورة الجهاز:

```bash
$ packer build template.json
```

### صورة AWS AMI باستخدام Ansible Provisioner
يمكنك استخدام Ansible Provisioner مع Packer لإنشاء صورة جهاز AWS. إليك مثالًا لقالب Packer:

```json
{
  "builders": [{
    "type": "amazon-ebs",
    "access_key": "ACCESS_KEY",
    "secret_key": "SECRET_KEY",
    "region": "us-west-2",
    "source_ami": "ami-0c55b159cbfafe1f0",
    "instance_type": "t2.micro",
    "ssh_username": "ubuntu",
    "ami_name": "my-image-{{timestamp}}"
  }],
  "provisioners": [{
    "type": "ansible",
    "playbook_file": "playbook.yml"
  }]
}
```
ينشئ القالب في هذا المثال صورة جهاز AWS ويستخدم Ansible لتهيئتها. يحدد قسم `provisioners` ملف Ansible playbook المطلوب.

### صورة Google Cloud Platform
يمكنك أيضًا استخدام Packer لإنشاء صور على Google Cloud Platform. إليك مثالًا لقالب:
```json
{
  "builders": [{
    "type": "googlecompute",
    "project_id": "PROJECT_ID",
    "source_image_family": "ubuntu-1604-lts",
    "zone": "us-central1-f",
    "image_name": "my-image",
    "image_description": "صورتي المخصصة"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "echo 'Hello, World!' > /tmp/hello.txt"
    ]
  }]
}
```
ينشئ هذا القالب صورة على Google Cloud Platform ويستخدم shell provisioner لإضافة ملف. سيكون اسم الصورة الناتجة "my-image" ووصفها "صورتي المخصصة".

### VMware

```json
{
  "builders": [
    {
      "type": "vmware-iso",
      "iso_url": "https://releases.ubuntu.com/20.04.2/ubuntu-20.04.2-live-server-amd64.iso",
      "iso_checksum_type": "sha256",
      "iso_checksum": "a244fe4adcc2ad92d15c12e47ca4ea97fb5b5d67b1ba50880c9e420ae3f3c083",
      "guest_os_type": "ubuntu-64",
      "disk_size": 40960,
      "vm_name": "ubuntu-20.04.2-server-amd64",
      "ssh_username": "ubuntu",
      "ssh_password": "ubuntu",
      "ssh_port": 22,
      "ssh_wait_timeout": "60m",
      "shutdown_command": "sudo shutdown -P now",
      "vmx_data": {
        "memsize": "4096",
        "numvcpus": "2"
      }
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "sudo apt-get update",
        "sudo apt-get install -y nginx"
      ]
    }
  ]
}
```
في هذا المثال، ينشئ القالب صورة VMware باستخدام ملف Ubuntu Server ISO. ستحتوي الصورة الناتجة على ذاكرة RAM بسعة 4 GB، ومعالجي CPU، وقرص بسعة 40 GB. وستثبّت nginx، خادم الويب، أثناء التهيئة.

هذه مجرد أمثلة قليلة لما يمكنك فعله باستخدام Packer. يمكنك إنشاء صور أجهزة لمنصات كثيرة واستخدام أدوات provisioner متنوعة لتهيئتها.

## أفضل ممارسات استخدام Packer

اتبع أفضل الممارسات التالية عند استخدام Packer:

- **استخدم التحكم بالإصدارات**: خزّن قوالب Packer ضمن نظام التحكم بالإصدارات لتتبع التغييرات والتعاون.
- **أضف معاملات إلى قوالبك**: استخدم المتغيرات لتسهيل إعادة استخدام القوالب وصيانتها.
- **اختبر قوالبك**: تحقق من أنها تنشئ صور الأجهزة المتوقعة.
- **اتبع أفضل ممارسات الأمان**: احمِ البيئات الناتجة عند إنشاء صور الأجهزة.
- **أبقِ القوالب بسيطة**: تجنب القوالب المعقدة التي يصعب صيانتها وتصحيحها.
- **استخدم الأمر `packer init`**: ابدأ قالبًا جديدًا بالإعدادات المطلوبة.

## الخلاصة

Packer أداة مفيدة لإنشاء صور أجهزة لمنصات مختلفة. توفر قابلية التكرار والأتمتة ودعم منصات متعددة وقابلية التوسع. اتبع أفضل الممارسات لإنشاء صور أجهزة آمنة وسهلة الصيانة.

قدمنا في هذا المقال أداة Packer وشرحنا كيفية إنشاء صور أجهزة لمنصات مختلفة. كما ناقشنا فوائدها وبعض أفضل ممارسات استخدامها.

لمعرفة المزيد عن Packer، راجع [الوثائق الرسمية](https://www.packer.io/docs).
