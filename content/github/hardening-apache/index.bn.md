---
title: "সিকিউর অ্যাপাচি ওয়েব সার্ভার: সিস্টেম অ্যাডমিনিস্ট্রেটরদের জন্য একটি ব্যাপক গাইড"
date: 2020-07-27
---
 Apache ওয়েব সার্ভারকে শক্ত করতে সিস্টেম অ্যাডমিনিস্ট্রেটরদের সাহায্য করার জন্য উদাহরণ কনফিগারেশন এবং স্ক্রিপ্টের একটি সংগ্রহ।

অ্যাপাচি, বক্সের বাইরে, আশ্চর্যজনকভাবে নিরাপত্তাহীন। প্রোডাকশন এনভায়রনমেন্টে Apache রোল আউট করার আগে অনেক সেরা অনুশীলন এবং নিরাপত্তা কনফিগারেশন ম্যানুয়ালি কনফিগার করতে হবে। আপনি আপনার Apache দৃষ্টান্ত সুরক্ষিত করার জন্য একটি সূচনা পয়েন্ট হিসাবে এই GitHub সংগ্রহস্থল ব্যবহার করতে পারেন।


## OWASP মূল নিয়ম সেট সহ ModSecurity ইনস্টল করা

### ধাপ 1: সংগ্রহস্থল আপডেট করুন
**উবুন্টু/ডেবিয়ানে:**
```
sudo apt-get update -y
```
**On CentOS/RHEL:**
``` 
sudo yum update -y
```

### Step 2: Installing ModSecurity for Apache
**On Ubuntu/ Debian:**
```
sudo apt-get install -y libapache2-modsecurity
sudo systemctl restart apache2
```
**On CentOS/RHEL:**
``` 
sudo yum install -y mod_security
sudo systemctl restart httpd.service
```

### Step 3: Configure ModSecurity

ModSecurity by default is only configured to log events from the default rules. We'll have to edit the configuration file to modify the rules to detect and block malicious traffic.

**Copy and rename the file:**
```
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
**Change the ModSecurity detection mode by editing the configuration file:**
```
sudo nano /etc/modsecurity/modsecurity.conf
```
Change "DetectionOnly" to "On"
```
SecRuleEngine DetectionOnly
```
```
SecRuleEngine On
```
If you're using nano you may hit **CTRL+X**, then **Y** and **Enter** to save and exit.

**Restart Apache**

On Ubuntu\ Debian:
```
sudo systemctl restart apache2
```

On CentOS\ RHEL:
```
sudo systemctl restart httpd.service
```
### Step 4: Downloading and Installing OWASP ModSecurity Core Rule Set

```
cd /apache/conf
wget https://github.com/coreruleset/coreruleset/archive/v3.3.0.tar.gz
tar -xvzf v3.3.0.tar.gz
sudo ln -s coreruleset-3.3.0 /apache/conf/crs
cp crs/crs-setup.conf.example crs/crs-setup.conf
rm v3.3.0.tar.gz
```
**Restart Apache**

On Ubuntu\ Debian:
```
sudo systemctl restart apache2
```

On CentOS\ RHEL:
```
sudo systemctl restart httpd.service
```
### Step 5: Additional Reading Material

**Additional installation instructions:**

[Install OWASP ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/)


[Install ModSecurity](https://phoenixnap.com/kb/setup-configure-modsecurity-on-apache)


## SSL Certificates

### Self Signed

Following the instructions from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04)

For this tutorial, I'm assuming you're going to be using the **example.com.conf** file from the repository.

#### Step 1: Create the SSL certificate
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
```

**Fill out the prompts appropriately. The most important line is the one that requests the Common Name (e.g. server FQDN or YOUR name). You need to enter the domain name associated with your server or, more likely, your server’s public IP address.**
If using for the IP access only certificate in the example.com.conf please use **"NA"** for all values where posible.

#### Perfect Forward Secrecy Configuration
```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
```



### Automate with LetsEncrypt and Certbot

Following the tutorial from [Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache.html)

#### Step 1: Install Certbot

```
sudo apt-get update -y
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-apache
```
### Step 2: Choose how you'd like to run Certbot

##### Either get and install your certificates... 
```
sudo certbot --apache
```

##### Or, just get a certificate 

```
sudo certbot certonly --apache
```

#### Step 3: Test automatic renewal

```
sudo certbot renew --dry-run
```





