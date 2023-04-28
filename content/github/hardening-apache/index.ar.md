---
title: "Secure Apache Web Server: A Comprehensive Guide for System Administrators"
date: 2020-07-27T10:15:03-07:00
draft: false
description: "Learn how to harden your Apache web server and ensure maximum security with this comprehensive guide for system administrators."
tags: ["Apache Web Server", "Security", "SSL Encryption", "ModSecurity", "OWASP Core Rule Set", "Self-Signed Certificate", "LetsEncrypt", "Certbot", "Firewall", "Configuration", "System Administration", "Web Application Security", "Best Practices", "Common Attacks", "HTTPS", "Web Server Hardening", "Ubuntu", "Debian", "CentOS", "RHEL"]
---
```
sudo apt-get update -y
```
``` 
sudo yum update -y
```
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
```
sudo nano /etc/modsecurity/modsecurity.conf
```
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
```
sudo systemctl restart apache2
```
```
sudo systemctl restart httpd.service
```
```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
```
sudo systemctl restart apache2
```
```
sudo systemctl restart httpd.service
```
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```
```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
```
sudo certbot --apache
```
```
sudo certbot certonly --apache
```
```
sudo certbot renew --dry-run
```

### مجموعة من التكوينات والنصوص منطقى النظام في تقوية خوادم الويب أباتشي.  بشكل آمن بشكل مدهش. تكوين أجود أفضل الأسعار قبل طرح Apache في بيئة الإنتاج. يمكنك استخدام مستودع GitHub هذا كنقطة انطلاق نحو تأمين مثيلات Apache.   ## تثبيت ModSecurity مع مجموعة القواعد الأساسية OWASP  ### الخطوة الأولى: تحديث المستودعات ** على Ubuntu / Debian: ** ** في CentOS / RHEL: **  ### الخطوة الثانية: تثبيت ModSecurity لـ Apache ** على Ubuntu / Debian: ** ** في CentOS / RHEL: **  ### الخطوة الثالثة: تكوين ModSecurity  يتم تكوينه افتراضيًا افتراضيًا. سيتعين عليك تحرير التكوين الأساسي الأساسي للخطوطة.  ** نسخ وإعادة تسمية الملف: ** ** قم بتغيير وضع الكشف عن طريق إعداد ملف التكوين: ** تغيير "DetectionOnly" إلى "تشغيل" إذا كنت تستخدم nano ، فقد تضغط على ** CTRL + X ** ، ثم ** Y ** و ** أدخل ** للحفظ والخروج.  ** أعد تشغيل أباتشي **  على Ubuntu \ Debian:  على CentOS \ RHEL: ### الخطوة 4: تنزيل وتثبيت مجموعة القواعد الأساسية لـ OWASP ModSecurity  ** أعد تشغيل أباتشي **  على Ubuntu \ Debian:  على CentOS \ RHEL: ### الخطوة 5: مواد قراءة إضافية  ** تعليمات التثبيت الإضافية: **  [تثبيت مجموعة القواعد الأساسية لـ OWASP ModSecurity] (https://owasp.org/www-project-modsecurity-core-rule-set/)   [تثبيت ModSecurity] (https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)   ## شهادات SSL  ### التوقيع الذاتي  اتباع التعليمات من [المحيط الرقمي] (https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)  بالنسبة لهذا البرنامج التعليمي ، أفترض أنك ستستخدم ملف ** example.com.conf ** من المستودع.  #### الخطوة الأولى: إنشاء شهادة SSL  ** املأ المشمول بشكل مناسب. أهم سطر هو الذي يطلب الاسم الشائع (مثل FQDN للخادم أو اسمك). تحتاج إلى إدخال اسم النطاق المرتبط بخادمك أو ، على الأرجح ، عنوان IP العام لخادمك. ** في حالة الاستخدام لشهادة الوصول إلى IP فقط في example.com.conf ، يرجى استخدام ** لجميع القيم ، يرجى ذلك ممكنًا.  #### تكوين سرية التامة التوجيهي    ### أتمتة مع LetsEncrypt و Certbot  متابعة البرنامج التعليمي من [Certbot] (https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)  #### الخطوة الأولى: تثبيت Certbot  ### الخطوة الثانية: اختر الطريقة التي تريدها لتشغيل Certbot  ##### زيادة الحرف على شهاداتك وتثبيتها ...  ##### الحصول على شهادة   #### الخطوة الثالثة: اختبار التجديد التلقائي      