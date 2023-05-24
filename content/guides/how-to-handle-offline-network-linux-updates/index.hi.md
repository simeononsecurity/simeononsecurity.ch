---
title: "अल्टीमेट गाइड: उबंटू डेबियन और सेंटोस आरएचईएल के लिए ऑफलाइन लिनक्स अपडेट"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["लिनक्स अद्यतन", "उबंटू", "डेबियन", "Centos", "आरएचईएल", "ऑफ़लाइन अद्यतन", "स्थानीय भंडार", "कैश", "सर्वर सेटअप", "क्लाइंट सेटअप", "apt-दर्पण", "demirror", "createrepo", "apt-cacher-एनजी", "यम-क्रोन", "लिनक्स सिस्टम अपडेट", "ऑफ़लाइन पैकेज अद्यतन", "ऑफ़लाइन सॉफ़्टवेयर अद्यतन", "स्थानीय पैकेज भंडार", "स्थानीय पैकेज कैश", "ऑफ़लाइन लिनक्स अद्यतन", "ऑफ़लाइन अद्यतनों को संभालना", "ऑफ़लाइन अद्यतन तरीके", "ऑफ़लाइन सिस्टम रखरखाव", "लिनक्स सर्वर अपडेट", "लिनक्स क्लाइंट अपडेट", "ऑफ़लाइन सॉफ्टवेयर प्रबंधन", "ऑफ़लाइन पैकेज प्रबंधन", "अद्यतन रणनीतियों", "लिनक्स सुरक्षा अद्यतन"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "एक कार्टून चित्रण एक सर्वर और कई क्लाइंट डिवाइसों को ऑफ़लाइन अद्यतनों का आदान-प्रदान करते हुए दर्शाता है।"
coverCaption: ""
---

** उबंटू/डेबियन और सेंटोस/आरएचईएल के लिए ऑफ़लाइन लिनक्स अपडेट इंस्टॉल करने के सर्वोत्तम तरीके **

Linux अद्यतन आपके सिस्टम की सुरक्षा और स्थिरता बनाए रखने के लिए आवश्यक हैं। हालाँकि, कुछ परिदृश्यों में, आपको ऑफ़लाइन वातावरण से निपटना पड़ सकता है जहाँ इंटरनेट कनेक्टिविटी सीमित या गैर-मौजूद है। ऐसे मामलों में, अद्यतनों को ऑफ़लाइन स्थापित करने के लिए एक उचित रणनीति का होना महत्वपूर्ण हो जाता है। यह आलेख विशेष रूप से एक स्थानीय रिपॉजिटरी या कैश का उपयोग करने पर ध्यान केंद्रित करते हुए, ऑफ़लाइन वातावरण में उबंटू/डेबियन और सेंटोस/आरएचईएल** के लिए लिनक्स अपडेट स्थापित करने के सर्वोत्तम तरीकों के माध्यम से आपका मार्गदर्शन करेगा।

## एक स्थानीय भंडार की स्थापना

ऑफ़लाइन अपडेट को संभालने के सबसे प्रभावी तरीकों में से एक स्थानीय रिपॉजिटरी स्थापित करना है। एक स्थानीय रिपॉजिटरी में सभी आवश्यक सॉफ़्टवेयर पैकेज और अपडेट होते हैं, जिससे आप बिना इंटरनेट कनेक्शन के अपने सिस्टम को अपडेट कर सकते हैं। यहां बताया गया है कि आप डेबियन-आधारित और रेड हैट-आधारित वितरण दोनों के लिए एक स्थानीय रिपॉजिटरी कैसे सेट कर सकते हैं:

### डेबियन/उबंटू के लिए

1. इंटरनेट एक्सेस वाले सर्वर पर ** डेबियन रिपॉजिटरी मिरर ** सेट करके प्रारंभ करें। जैसे टूल्स का इस्तेमाल कर सकते हैं [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) आधिकारिक डेबियन या उबंटू रिपॉजिटरी का एक स्थानीय दर्पण बनाने के लिए।

#### एप्ट-मिरर के साथ डेबियन रिपॉजिटरी मिरर की स्थापना:

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

#### डेबियन रिपॉजिटरी मिरर को डेमिरर के साथ सेट करना:
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
#### डेबियन क्लाइंट निर्देश

2. ** संपादित करके अपने स्थानीय रिपॉजिटरी को कॉन्फ़िगर करें`/etc/apt/sources.list` ऑफ़लाइन सिस्टम पर फ़ाइल। डिफ़ॉल्ट रिपॉजिटरी URL को स्थानीय रिपॉजिटरी URL से बदलें। उदाहरण के लिए, यदि आपकी स्थानीय रिपॉजिटरी को होस्ट किया गया है `http://local-repo/ubuntu` अद्यतन करें `sources.list` तदनुसार फाइल करें।

उदाहरण `/etc/apt/sources.list` फ़ाइल:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. कॉन्फ़िगरेशन अपडेट होने के बाद, आप ** चला सकते हैं`apt update` स्थानीय रिपॉजिटरी से पैकेज सूची लाने के लिए ऑफलाइन सिस्टम पर कमांड।

```shell
sudo apt update
```

4. अंत में, आप ** का उपयोग कर सकते हैं`apt upgrade` स्थानीय रिपॉजिटरी से उपलब्ध अद्यतनों को स्थापित करने की आज्ञा।

```shell
sudo apt upgrade
```

### CentOS/RHEL के लिए

1. CentOS/RHEL के लिए एक स्थानीय भंडार स्थापित करने के लिए, आपको इसका उपयोग करने की आवश्यकता है [**`createrepo`**](https://linux.die.net/man/8/createrepo) औजार। यह टूल स्थानीय रिपॉजिटरी के लिए आवश्यक मेटाडेटा बनाता है।

2. इंटरनेट एक्सेस वाले सर्वर पर रिपॉजिटरी फाइलों को स्टोर करने के लिए एक डायरेक्टरी बनाएं। उदाहरण के लिए, आप ** नामक एक निर्देशिका बना सकते हैं`local-repo`

3. सभी प्रासंगिक RPM संकुल फाइलों और अद्यतनों को ** में कॉपी करें`local-repo` निर्देशिका।

#### createrepo के साथ एक स्थानीय रिपॉजिटरी की स्थापना:

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
4. रिपॉजिटरी मेटाडेटा उत्पन्न होने के बाद, आप संपूर्ण को स्थानांतरित कर सकते हैं `local-repo` USB ड्राइव या किसी अन्य माध्यम का उपयोग करके ऑफ़लाइन सिस्टम के लिए निर्देशिका।

5. ऑफ़लाइन सिस्टम पर, एक नया बनाएँ `.repo` फ़ाइल में `/etc/yum.repos.d/` निर्देशिका। आवश्यक कॉन्फ़िगरेशन विवरण प्रदान करें, जैसे कि `baseurl` स्थानीय भंडार निर्देशिका की ओर इशारा करते हुए।

उदाहरण के लिए, नामक एक फ़ाइल बनाएँ `local.repo` में `/etc/yum.repos.d/` निर्देशिका और निम्नलिखित सामग्री जोड़ें:
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
6. फ़ाइल सहेजें और संपादक से बाहर निकलें।

7. रिपॉजिटरी को कॉन्फ़िगर करने के बाद, आप स्थानीय रिपॉजिटरी से अपडेट इंस्टॉल करने के लिए यम अपडेट कमांड का उपयोग कर सकते हैं।

```shell
sudo yum update
```

यह कमांड स्थानीय रिपॉजिटरी से संकुल का उपयोग करके सिस्टम पर संकुल को अद्यतन करेगा।

चलाकर स्थानीय रिपॉजिटरी को अपडेट करना याद रखें `createrepo` कमांड जब भी नए पैकेज रिपॉजिटरी से जोड़े या निकाले जाते हैं।

कृपया ध्यान दें कि आपको बदलने की आवश्यकता होगी `/path/to/local-repo` उस निर्देशिका के वास्तविक पथ के साथ जहाँ आपने रिपॉजिटरी फ़ाइलों को संग्रहीत किया है।

## एक स्थानीय कैश की स्थापना

ऑफ़लाइन अपडेट को संभालने का एक अन्य तरीका स्थानीय कैश सेट करना है। एक स्थानीय कैश डाउनलोड किए गए पैकेज और अपडेट को स्टोर करता है, जिससे आप अलग-अलग डाउनलोड की आवश्यकता के बिना उन्हें कई सिस्टम में वितरित कर सकते हैं। आप इस कैशे को एक ऑनलाइन सिस्टम पर सेट करेंगे, फिर निर्देशिका को एक ऐसे सिस्टम में ले जाएंगे जो अन्य सिस्टम को संकुल तक पहुंचने की अनुमति देने के लिए ऑफ़लाइन है। यहां बताया गया है कि आप डेबियन-आधारित और रेड हैट-आधारित वितरण दोनों के लिए स्थानीय कैश कैसे सेट कर सकते हैं:

### डेबियन/उबंटू के लिए

1. स्थापित करें और कॉन्फ़िगर करें [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) डेबियन/उबंटू पैकेज के लिए एक कैशिंग प्रॉक्सी। आप इसे ** कमांड चलाकर इंस्टॉल कर सकते हैं`sudo apt-get install apt-cacher-ng`

2. एक बार इंस्टॉल हो जाने पर, संपादित करें **`/etc/apt-cacher-ng/acng.conf` कैशिंग व्यवहार को कॉन्फ़िगर करने के लिए फ़ाइल। सुनिश्चित करें कि **`PassThroughPattern` पैरामीटर में आवश्यक रिपॉजिटरी URL शामिल हैं।

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
PassThroughPattern पैरामीटर में आवश्यक रिपॉजिटरी URL को हटा दें या जोड़ें। उदाहरण के लिए, उबंटू रिपॉजिटरी को शामिल करने के लिए, निम्न पंक्ति को जोड़ें या अनकमेंट करें:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
फ़ाइल सहेजें और संपादक से बाहर निकलें।

3. प्रारंभ करें [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) आदेश का उपयोग कर सेवा **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. ऑफ़लाइन सिस्टम पर, ** को कॉन्फ़िगर करें`/etc/apt/apt.conf.d/02proxy` फ़ाइल स्थानीय कैश को इंगित करने के लिए। निम्नलिखित पंक्ति का प्रयोग करें: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
कैश सर्वर के आईपी पते के साथ <कैश-सर्वर-आईपी> को बदलकर फ़ाइल में निम्न पंक्ति जोड़ें:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
फ़ाइल सहेजें और संपादक से बाहर निकलें

5. अब, जब आप ** चलाते हैं`apt update` और **`apt upgrade` ऑफ़लाइन सिस्टम पर आदेश, वे संकुल को स्थानीय कैश से पुनर्प्राप्त करेंगे।

```shell
sudo apt update
sudo apt upgrade
```
ये आदेश ऑफ़लाइन सिस्टम पर इंटरनेट एक्सेस की आवश्यकता को कम करते हुए, स्थानीय कैश से अपडेट प्राप्त और स्थापित करेंगे।

कृपया ध्यान दें कि आपको ** को बदलने की आवश्यकता होगी`<cache-server-ip>` मशीन के वास्तविक आईपी पते के साथ जहां **apt-cacher-ng** स्थापित है।

### CentOS/RHEL के लिए

1. CentOS/RHEL के लिए, आप उपयोग कर सकते हैं [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) एक स्थानीय कैश स्थापित करने के लिए। कमांड चलाकर इसे इंस्टॉल करें **`sudo yum install yum-cron`

2. संपादित करें **`/etc/yum/yum-cron.conf` फ़ाइल और कॉन्फ़िगर करें **`download_only` ** के लिए पैरामीटर`yes` यह सुनिश्चित करता है कि पैकेज केवल डाउनलोड किए गए हैं और स्वचालित रूप से इंस्टॉल नहीं किए गए हैं।

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. प्रारंभ करें [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) आदेश का उपयोग कर सेवा **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. ऑफ़लाइन सिस्टम पर, डाउनलोड किए गए पैकेजों को संग्रहीत करने के लिए एक स्थानीय निर्देशिका बनाएँ, उदाहरण के लिए, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. डाउनलोड किए गए पैकेजों को ऑनलाइन सिस्टम से स्थानीय कैश निर्देशिका में कॉपी करें।

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

बदलना `/path/to/local/cache` ऑफ़लाइन सिस्टम पर स्थानीय कैश निर्देशिका के पथ के साथ।

6. ऑफ़लाइन सिस्टम पर, एक नया ** बनाएँ`.repo` फ़ाइल में **`/etc/yum.repos.d/` निर्देशिका, स्थानीय कैश निर्देशिका की ओर इशारा करते हुए।

```bash
sudo nano /etc/yum.repos.d/local.repo
```
फ़ाइल में निम्न सामग्री जोड़ें, प्रतिस्थापित करना `<local-cache-path>` स्थानीय कैश निर्देशिका के पथ के साथ:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
फ़ाइल सहेजें और संपादक से बाहर निकलें।

7. अंत में, आप ** का उपयोग कर सकते हैं`yum update` स्थानीय कैश से अद्यतन स्थापित करने के लिए ऑफ़लाइन सिस्टम पर आदेश।

```shell
sudo yum update
```

यह आदेश स्थानीय कैश से संकुल का उपयोग करके ऑफ़लाइन सिस्टम पर संकुल को अद्यतन करेगा।

कृपया ध्यान दें कि आपको ** को बदलने की आवश्यकता होगी`<local-cache-path>` ऑफ़लाइन सिस्टम पर स्थानीय कैश निर्देशिका के वास्तविक पथ के साथ।

______

## निष्कर्ष

ऑफ़लाइन वातावरण में लिनक्स अपडेट को संभालना चुनौतीपूर्ण हो सकता है, लेकिन सही दृष्टिकोण से, आप यह सुनिश्चित कर सकते हैं कि आपका सिस्टम अद्यतित और सुरक्षित रहे। इस लेख में, हमने Ubuntu/Debian और CentOS/RHEL के लिए ऑफ़लाइन अपडेट इंस्टॉल करने के सर्वोत्तम तरीकों पर चर्चा की। हमने डेबियन-आधारित और रेड हैट-आधारित वितरण दोनों के लिए चरण-दर-चरण निर्देश प्रदान करते हुए एक स्थानीय रिपॉजिटरी की स्थापना और एक स्थानीय कैश की स्थापना की खोज की।

इन तरीकों का पालन करके, आप अपने लिनक्स सिस्टम की सुरक्षा और स्थिरता को ऑफ़लाइन वातावरण में भी बनाए रख सकते हैं। नवीनतम अपडेट शामिल करने के लिए समय-समय पर अपने स्थानीय रिपॉजिटरी या कैश को अपडेट करना याद रखें।

______

## संदर्भ

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
