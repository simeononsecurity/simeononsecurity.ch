---
title: "Ansible के साथ स्वचालित लिनक्स पैचिंग और अपडेट: एक व्यापक गाइड"
date: 2023-05-28
toc: true
draft: false
description: "विभिन्न वितरणों और सेटअप निर्देशों को कवर करते हुए, Ansible का उपयोग करके लिनक्स पैचिंग और अपडेट को स्वचालित करना सीखें।"
tags: ["लिनक्स पैचिंग", "उत्तरदायी स्वचालन", "स्वचालित अद्यतन", "प्रणाली रखरखाव", "आईटी स्वचालन", "पैच प्रबंधन", "लिनक्स सुरक्षा", "डेबियन", "उबंटू", "आरएचईएल", "अल्पाइन", "प्रणाली की स्थिरता", "भेद्यता शमन", "सूचना प्रौद्योगिकी की आधारभूत संरचना", "स्वचालन उपकरण", "अन्सिबल प्लेबुक", "मेजबान विन्यास", "सॉफ्टवेयर अपडेट", "सुरक्षा अनुपालन", "आईटी संचालन", "लिनक्स अद्यतन", "उबंटू", "डेबियन", "Centos", "आरएचईएल", "ऑफ़लाइन अद्यतन", "स्थानीय भंडार", "कैश", "सर्वर सेटअप", "क्लाइंट सेटअप", "apt-दर्पण", "demirror", "createrepo", "apt-cacher-एनजी", "यम-क्रोन", "लिनक्स सिस्टम अपडेट", "ऑफ़लाइन पैकेज अद्यतन", "ऑफ़लाइन सॉफ़्टवेयर अद्यतन", "स्थानीय पैकेज भंडार", "स्थानीय पैकेज कैश", "ऑफ़लाइन लिनक्स अद्यतन", "ऑफ़लाइन अद्यतनों को संभालना", "ऑफ़लाइन अद्यतन तरीके", "ऑफ़लाइन सिस्टम रखरखाव", "लिनक्स सर्वर अपडेट", "लिनक्स क्लाइंट अपडेट", "ऑफ़लाइन सॉफ्टवेयर प्रबंधन", "ऑफ़लाइन पैकेज प्रबंधन", "अद्यतन रणनीतियों", "लिनक्स सुरक्षा अद्यतन"]
cover: "/img/cover/A_colorful_cartoon-style_image_depicting_a_robot_applying_patches.png"
coverAlt: "एक रंगीन, कार्टून-शैली की छवि जिसमें एक रोबोट को दर्शाया गया है जो Linux सर्वरों के समूह में पैच लगा रहा है।"
coverCaption: ""
---

** स्वचालित लिनक्स पैचिंग और अपडेट को Ansible के साथ **

आज की तेज़-तर्रार और सुरक्षा-सचेत दुनिया में, **स्वचालित** लिनक्स सिस्टम की पैचिंग और अपडेटिंग सिस्टम की स्थिरता सुनिश्चित करने और कमजोरियों को कम करने के लिए महत्वपूर्ण है। बड़ी संख्या में Linux वितरण उपलब्ध होने के साथ, विभिन्न प्लेटफार्मों पर अपडेट को कुशलतापूर्वक प्रबंधित करना चुनौतीपूर्ण हो सकता है। सौभाग्य से, **Ansible**, एक शक्तिशाली ऑटोमेशन टूल, विभिन्न Linux वितरणों में पैचिंग और अपडेट को स्वचालित करने के लिए एक एकीकृत समाधान प्रदान करता है। इस लेख में, हम यह पता लगाएंगे कि **डेबियन-आधारित, उबंटू-आधारित, आरएचईएल-आधारित, एल्पाइन-आधारित**, और अन्य वितरणों के लिए पैचिंग और अद्यतन करने की प्रक्रिया को स्वचालित करने के लिए एंसिबल का उपयोग कैसे किया जाए। हम एक विस्तृत अन्सिबल प्लेबुक उदाहरण भी प्रदान करेंगे जो सभी लक्षित सिस्टमों के लिए अन्सिबल क्रेडेंशियल्स और होस्ट फ़ाइलों को सेट करने के निर्देशों के साथ-साथ विभिन्न लिनक्स डिस्ट्रोस पर पैच और अपडेट स्थापित करने को संभालता है।

## पूर्वापेक्षाएँ

स्वचालन प्रक्रिया में गोता लगाने से पहले, आइए सुनिश्चित करें कि हमारे पास आवश्यक पूर्वापेक्षाएँ हैं। इसमे शामिल है:

1. **अन्सिबल इंस्टालेशन**: अन्सिबल का उपयोग करने के लिए, आपको इसे उस सिस्टम पर इंस्टॉल करना होगा जिससे आप ऑटोमेशन कार्यों को चलाएंगे। आप पर आधिकारिक Ansible प्रलेखन का पालन कर सकते हैं [how to install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html) विस्तृत निर्देशों के लिए।

2. **इन्वेंट्री कॉन्फिगरेशन**: एक इन्वेंट्री फाइल बनाएं जो उन लक्ष्य प्रणालियों को सूचीबद्ध करती है जिन्हें आप Ansible के साथ प्रबंधित करना चाहते हैं। प्रत्येक सिस्टम का अपना **आईपी पता या होस्टनाम** निर्दिष्ट होना चाहिए। उदाहरण के लिए, आप नाम की एक इन्वेंट्री फ़ाइल बना सकते हैं `hosts.ini` निम्नलिखित सामग्री के साथ:

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

बदलना `<debian_ip_address>` `<ubuntu_ip_address>` `<rhel_ip_address>` और `<alpine_ip_address>` लक्ष्य सिस्टम के संबंधित आईपी पते या होस्टनाम के साथ।

3. **SSH एक्सेस**: सुनिश्चित करें कि आपके पास SSH कुंजी-आधारित प्रमाणीकरण का उपयोग करके लक्ष्य सिस्टम तक SSH की पहुंच है। यह Ansible को सिस्टम से सुरक्षित रूप से जुड़ने और आवश्यक कार्य करने की अनुमति देगा।

## पैचिंग और अपडेट करने के लिए अन्सिबल प्लेबुक

विभिन्न लिनक्स वितरणों के लिए पैचिंग और अद्यतन करने की प्रक्रिया को स्वचालित करने के लिए, हम एक Ansible प्लेबुक बना सकते हैं जो विभिन्न डिस्ट्रोज़ पर पैच और अपडेट स्थापित करने को संभालती है। नीचे एक उदाहरण प्लेबुक है:

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

उपरोक्त प्लेबुक में:

- द `hosts` लाइन प्रत्येक कार्य के लिए लक्ष्य प्रणालियों को निर्दिष्ट करती है। प्लेबुक इसके तहत समूहीकृत सिस्टम पर चलेगी `debian` `ubuntu` `rhel` और `alpine`
- द `become: yes` कथन प्लेबुक को व्यवस्थापकीय विशेषाधिकारों के साथ चलाने की अनुमति देता है।
- पहला कार्य डेबियन-आधारित और उबंटू-आधारित सिस्टम का उपयोग करके अद्यतन करता है `apt` मापांक।
- दूसरा कार्य आरएचईएल-आधारित सिस्टम का उपयोग कर अद्यतन करता है `yum` मापांक।
- तीसरा कार्य अल्पाइन-आधारित सिस्टम का उपयोग कर अद्यतन करता है `apk` मापांक।

ध्यान दें कि उपयुक्त सिस्टम को लक्षित करने के लिए समूह के नाम के आधार पर कार्य अनुकूलित हैं।

## अन्सिबल क्रेडेंशियल्स और होस्ट फाइल्स को सेट करना

लक्षित सिस्टम के लिए Ansible क्रेडेंशियल्स और होस्ट फ़ाइलों को कॉन्फ़िगर करने के लिए, इन चरणों का पालन करें:

1. SSH क्रेडेंशियल्स जैसी संवेदनशील जानकारी को स्टोर करने के लिए एक **Ansible Vault** फ़ाइल बनाएं। वॉल्ट फ़ाइल बनाने के लिए आप निम्न आदेश का उपयोग कर सकते हैं:
```shell
ansible-vault create credentials.yml
```
2. इन्वेंट्री फ़ाइल को अपडेट करें (`hosts.ini` प्रत्येक लक्ष्य प्रणाली के लिए उपयुक्त SSH क्रेडेंशियल्स के साथ। उदाहरण के लिए:
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

बदलना `<debian_ip_address>` `<ubuntu_ip_address>` `<rhel_ip_address>` और `<alpine_ip_address>` लक्ष्य सिस्टम के संबंधित आईपी पते के साथ। साथ ही, बदलें `<debian_username>` `<ubuntu_username>` `<rhel_username>` और `<alpine_username>` प्रत्येक सिस्टम के लिए उपयुक्त SSH उपयोक्तानाम के साथ। अंत में, बदलें `<debian_ssh_password>` `<ubuntu_ssh_password>` `<rhel_ssh_password>` और `<alpine_ssh_password>` इसी SSH पासवर्ड के साथ।

3. Ansible Vault का उपयोग करके host.ini फ़ाइल को एन्क्रिप्ट करें:
   
```shell
ansible-vault encrypt hosts.ini
```

संकेत मिलने पर वॉल्ट पासवर्ड प्रदान करें।

उपरोक्त चरणों के साथ, आपने सभी लक्षित प्रणालियों के लिए आवश्यक Ansible क्रेडेंशियल्स और होस्ट फ़ाइलों को सेट किया है

## प्लेबुक चलाना
मार्गदर्शिका चलाने और पैचिंग और अद्यतन करने की प्रक्रिया को स्वचालित करने के लिए, इन चरणों का पालन करें:

1. एक टर्मिनल खोलें और उस निर्देशिका पर नेविगेट करें जहां आपके पास प्लेबुक फ़ाइल और एन्क्रिप्ट की गई इन्वेंट्री फ़ाइल है।

2. संकेत मिलने पर वॉल्ट पासवर्ड प्रदान करते हुए, प्लेबुक को निष्पादित करने के लिए निम्न कमांड चलाएँ:

```shell
ansible-playbook -i hosts.ini playbook.yml --ask-vault-pass
```

3. Ansible लक्ष्य सिस्टम से जुड़ जाएगा, प्रदान किए गए क्रेडेंशियल्स का उपयोग करेगा, और निर्दिष्ट कार्यों को निष्पादित करेगा, तदनुसार सिस्टम को अपडेट करेगा।

बधाई हो! आपने Ansible का उपयोग करके विभिन्न लिनक्स वितरणों के पैचिंग और अपडेट को सफलतापूर्वक स्वचालित कर दिया है। अन्सिबल प्लेबुक और क्रेडेंशियल्स और होस्ट फ़ाइलों के उचित सेटअप के साथ, अब आप अपने लिनक्स इन्फ्रास्ट्रक्चर में पैचिंग और अपडेटिंग प्रक्रिया को कुशलतापूर्वक प्रबंधित कर सकते हैं।

## निष्कर्ष

अन्सिबल के साथ लिनक्स सिस्टम के पैचिंग और अपडेट को स्वचालित करना प्रक्रिया को सरल और सुव्यवस्थित करता है, जिससे सिस्टम प्रशासकों को विभिन्न लिनक्स वितरणों में अद्यतनों को कुशलतापूर्वक प्रबंधित करने की अनुमति मिलती है। इस लेख में दिए गए निर्देशों का पालन करके, आपने सीखा है कि एक अन्सिबल प्लेबुक कैसे बनाई जाती है जो विभिन्न लिनक्स डिस्ट्रोस पर पैच और अपडेट इंस्टॉल करने को संभालती है। इसके अतिरिक्त, आपने वांछित सिस्टम को लक्षित करने के लिए Ansible क्रेडेंशियल्स और होस्ट फ़ाइलों को सेट किया है। स्वचालन की शक्ति को अपनाएं और एक अधिक सुरक्षित और अच्छी तरह से बनाए गए लिनक्स बुनियादी ढांचे के लाभों का आनंद लें।

## संदर्भ

1. [Ansible Documentation](https://docs.ansible.com/)
2. [Official Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
