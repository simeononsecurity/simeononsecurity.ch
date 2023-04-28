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

### अपाचे वेब सर्वर को सख्त करने में सिस्टम रिकॉर्डिंग की सहायता के लिए उदाहरण और स्क्रिप्ट का संग्रह।  बॉक्स से बाहर अपाचे आश्चर्यजनक रूप से असुरक्षित है। अपाचे के उत्पादन में रोल आउट करने से पहले कई सुनिश्चित और सुरक्षा को नाम देने के रूप में शामिल किया गया है। आप इस GitHub रिपॉजिटरी को अपने अपाचे उदाहरण को सुरक्षित करने के लिए एक शुरुआती बिंदु के रूप में उपयोग कर सकते हैं।   ## OWASP कोर रूल सेट के साथ ModSecurity समावेश करना  ### चरण 1: रिपॉजिटरी अपडेट करें **उबंटू/डेबियन पर:** ** सेंटोस/आरएचईएल पर:**  ### चरण 2: Apache के लिए ModSecurity व्यवस्था करना **उबंटू/डेबियन पर:** ** सेंटोस/आरएचईएल पर:**  ### चरण 3: तौर-तरीकों को विष दें  डिफ़ॉल्ट रूप से ModSecurity को केवल Microsoft रीडिज़ेट से चालू करने के लिए भेजा जाता है। लेबल का पता लगाने और ब्लॉक करने के लिए हमें निर्दिष्ट करने के लिए दस्तावेज़ को चिपकाने का अधिकार होगा।  ** फ़ाइल की प्रतिलिपि बनाएँ और उसका नाम बदलें:** **कॉन्फ़िगरेशन फ़ाइल को अनुमान करके मोडसिक्योरिटी डिटेक्शन मोड बदलाव:** "डिटेक्शन ऑनली" को "ऑन" में बदल दें यदि आप लिंक का उपयोग कर रहे हैं तो आप जैम और खाली हो जाने के लिए **CTRL+X**, फिर **Y** और **Enter** दबा सकते हैं।  **अपाचे को बेशक करें**  बैंकॉक \ डेबियन पर:  CentOS\ RHEL पर: ### चरण 4: OWASP ModSecurity कोर नियम सेट को डाउनलोड करें और दर्ज करें  **अपाचे को बेशक करें**  बैंकॉक \ डेबियन पर:  CentOS\ RHEL पर: ### चरण 5: अतिरिक्त पठन सामग्री  **अधिक निर्देश:**  [OWASP ModSecurity कोर नियम सेट करें](https://owasp.org/www-project-modsecurity-core-नियम-सेट/)   [मॉडसिक्योरिटी रिकॉर्ड बनाएं] (https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)   ## एसएसएल सत्यापन  ### स्वहस्ताक्षरित  [डिजिटल महासागर] के निर्देश का पालन करना )  इस ट्यूटोरियल के लिए, मुझे लगता है कि आप रिपॉजिटरी से **example.com.conf** फ़ाइल का उपयोग कर रहे हैं।  #### चरण 1: एसएसएल प्रमाणन बनाएं  **संकेतों को उचित रूप से भरें। वह सबसे महत्वपूर्ण पंक्ति है जो सामान्य नाम (जैसे सर्वर FQDN या आपका नाम) का अनुरोध करता है। आपको अपने सब्सक्राइबर से लिया गया डोमेन नाम या, अधिक रिपोर्ट है, आपके सर्वर की सार्वजनिक आईपी पता लगाना होगा।** अगर example.com.conf में केवल IP ऐक्सेक्स के लिए सब्सक्राइबर का उपयोग किया जा रहा है, तो कृपया सभी ल्यूक के लिए **"NA"** का उपयोग करें, जहां संभव हो।  #### सीक्रेसी के लिए बिल्कुल सही    ### LetsEncrypt और Certbot के साथ ऑटोमेट करें  [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html) ट्यूटोरियल के बाद  #### चरण 1: प्राधिकरण स्थापित करें  ### चरण 2: चुनें कि आप Certbot को कैसे बढ़ाना चाहते हैं  ##### या तो अपना प्रमाणपत्र प्राप्त करें और नामांकन करें...  ##### या, बस एक प्रमाण पत्र प्राप्त करें   #### चरण 3: स्वचालित नवीनीकरण का परीक्षण करें      