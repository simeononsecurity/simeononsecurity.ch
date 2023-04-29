---
title: "PowerShell DSC: Guía de inicio"
date: 2023-04-02
toc: true
draft: false
descripción: "Explora el poder de PowerShell Desired State Configuration (DSC) para automatizar y gestionar las configuraciones del sistema para un entorno seguro y compatible."
tags: ["PowerShell", "DSC", "Configuration Management", "Automation", "Windows", "System Administration", "Best Practices", "Compliance", "Security", "Infrastructure", "DevOps", "Server Configuration", "Testing", "Git", "Source Control", "Government Regulations", "NIST", "CIS", "Configuration Drift", "Custom Resources"]
cover: "/img/cover/A_cartoon_image_of_a_confident_system_administrator.png"
coverAlt: "Una imagen de dibujos animados de un administrador de sistemas seguro de sí mismo con una capa de superhéroe, de pie junto a un rack de servidores bien organizado, sosteniendo un script DSC de PowerShell en una mano y un escudo con el logotipo de Windows en la otra, protegiendo los servidores de la desviación de la configuración y las amenazas de seguridad."
coverCaption: ""
---
```powershell
Configuración InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Nodo 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Presente
            Name = 'Servidor Web
        }
    }
}
```
```powershell
InstallIIS
```
``powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```


 **कॉन्फ़िगरेशन प्रबंधन के लिए PowerShell क्रिएट स्टेट लुक्स (DSC) का उपयोग करने के लिए एक आकार**
 
 ______
 
 ## परिचय
 
 PowerShell crear Estado (**DSC**) TI व्यवस्थापन और DevOps पेशेवरों के लिए एक शक्तिशाली और **आवश्यक उपकरण** है, जो उन्हें और लिंक सिस्टम की फिर से शुरू और चालू करने की अनुमति देता है। यह दस्तावेज़ प्रबंधन के लिए PowerShell DSC का उपयोग करने के लिए एक विकल्प प्रदान करता है, जिसमें सर्वोत्तम अभ्यास, सरकारी नियम और उपयोगी संदर्भ शामिल हैं।
 
 ______
 
 ## PowerShell छद्म राज्य के साथ शुरू करना
 
 ### PowerShell क्रिएट स्टेट सक्सेस क्या है?
 
 PowerShell crear estado (**DSC**) PowerShell में निर्मित एक **घोषणात्मक भाषा** है जो व्यवस्थापन को एप और सेवाओं के प्रबंधन में सक्षम बनाता है। यह आपके परिदृश्य को करने के लिए एक **मानकीकरण और दृष्टिकोण** तरीका प्रदान करता है और सुनिश्चित करता है कि व्यवस्था की स्थिति में रहे।
 
 ### पावरशेल डीसी रिकॉर्ड बना रहा है
 
 PowerShell DSC के साथ आरंभ करने के लिए, आपको **Windows Management Framework (WMF)** कनेक्ट करना होगा। WMF एक पैकेज है जिसमें PowerShell, DSC और अन्य आवश्यक प्रबंधन उपकरण शामिल हैं। आप WMF का नवीनतम संस्करण [Microsoft डाउनलोड सेंटर](https://www.microsoft.com/en-us/download/details.aspx?id=54616) से डाउनलोड कर सकते हैं।
 
 ______
 
 ## डीएससी फर्जी बनाना और लागू करना
 
 ### डीएससी रिकॉर्ड बनाना
 
 DSC एक **पॉवरशेल स्क्रिप्ट** है जो किसी सिस्टम की स्थिति का वर्णन करता है। इसमें एक या अधिक **डीएससी संसाधन** होते हैं जो सिस्टम के लिए आवश्यक होते हैं और परिभाषा को परिभाषित करते हैं। यहाँ सरल DSC का एक उदाहरण दिया गया है जो विज़ुअल सेवर (IIS) की भूमिका स्थापित करता है:
 
 ### डीएससी फर्जीवाड़ा करना
 एक बार जब आप डीएससी लेख लिखते हैं, तो आप इसे **Start-DscConfiguration** cmdlet का उपयोग करके लक्षित कर सकते हैं। सबसे पहले, स्क्रिप्ट को PowerShell में चालाकी करें:
 
 
 यह एक **MOF** फ़ाइल (प्रबंधित कनेक्शन स्वरूप) शीर्षक जिसमें निवेश शामिल है। अगले, निम्नलिखित कमांड का उपयोग करके लक्ष्य प्रणाली में अपलोड करें:
 
 
 ## PowerShell DSC का उपयोग करने के लिए सर्वोत्तम अभ्यास
 
 ### अपने योग को करें
 
 अपने तरीके के विभिन्न घटकों को **व्यक्तिगत डीएससी दृश्यों** में अलग करके **मॉडलूर और फिर से देखें: देखें**दृश्य बनाएं। जैसे-जैसे आपकी बढ़ती जा रही है, यह दृष्टिकोण आपको आसानी से **रखरखाव और स्कैन** करने की अनुमति देता है।
 
 ###स्रोत नियंत्रण का प्रयोग करें
 
 अपने DSC और कस्टम संसाधनों को हमेशा **स्रोत नियंत्रण प्रणाली** जैसे Git में आर्काइव करें। यह प्रयोग आपको अपनी टीम के साथ सहयोग करने और ज़रूरतों पर आसानी से अपने पिछले संस्करणों पर वापस जाने में बनाता है।
 
 ### अपने पाठकों का परीक्षण करें
 
 ** एक्सक्लूसिव** दृश्य प्रबंधन का एक महत्वपूर्ण पहलू है। DSC कार्रवाई को लागू करने से पहले **गैर-उत्पादन माहौल** पर इसका परीक्षण करें ताकि यह सुनिश्चित हो सके कि यह प्रतिबद्धता के अनुरूप काम करता है और कोई भी अप्रत्याशित परिणाम नहीं देता है। आप अपने डीएससी पाठकों के लिए स्वचालित परीक्षण के लिए [पेस्टर] (https://github.com/pester/Pester) जैसे टूल का भी उपयोग कर सकते हैं।
 
 ______
 
 ## सरकारी सूचना और निर्देश
 
 ### एनआईएसटी निर्देश
 
 राष्ट्रीय मानक और प्रौद्योगिकी संस्थान (एनआईएसटी) व्यवस्था प्रबंधन के लिए दिशानिर्देश प्रदान करता है। विशेष रूप से, [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) प्रकाशन में आधार रेखा पर एक खंड (CM-2) शामिल है , जो डीएससी के उपयोग के लिए प्रासंगिक है। डायरेक्ट्री सिस्टम में प्रॉक्सी को बनाए रखना, निगरानी और नियंत्रण करने का महत्व अधिक दिया जाता है। PowerShell DSC सिस्टम आपके प्रदर्शन के लिए एक संगति और स्वचालित तरीका प्रदान करके घटकों को इन गतिविधियों के पालन में मदद कर सकता है।
 
 ### संघीय सूचना सुरक्षा प्रबंधन अधिनियम (FISMA)
 
 संघीय सूचना सुरक्षा प्रबंधन अधिनियम [FISMA](https://www.dhs.gov/cisa/federal-सूचना-सुरक्षा-आधुनिकीकरण-अधिनियम) संघीय सूचना सुरक्षा नियंत्रणों की सुनिश्चितता के लिए एक व्यापक रूपरेखा लागू करने की आवश्यकता है। सक्सेक्स प्रबंधन FISMA पूर्ति का एक प्रमुख घटक है, और PowerShell DSC संगठनों की इन आवश्यकताओं को पूरा करने में मदद करने में एक आवश्यक भूमिका निभा सकता है।
 ______
 
 ## निष्कर्ष
 
 PowerShell क्रिएट स्टेट (DSC) सिस्टम रीडर्स को फिर से चालू करने और प्रबंधन को चालू करने के लिए एक शक्तिशाली और लचीला उपकरण है। नियमों का पालन करके और सरकार की अपेक्षाओं का पालन करके, आप यह सुनिश्चित कर सकते हैं कि अनुपालन बनाए रखते हुए आपके संगठन के सिस्टम की स्थिति में बने रहें। PowerShell DSC की अपनी समझ बढ़ाने और अपने पंजीकरण प्रबंधन को बेहतर बनाने के लिए इस लेख में दिए गए संसाधनों का लाभ नहीं लेना चाहिए।
 ______
 
 ## संबंध
 
 - [PowerShell स्टेट स्टेट्स (DSC) आधिकारिक दस्तावेज़ीकरण](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
 - [एनआईएसटी एसपी 800-53 - संघीय सूचना प्रणाली और संगठनों के लिए सुरक्षा और गोपनीयता नियंत्रण](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
 - [संघीय सूचना सुरक्षा प्रबंधन अधिनियम (FISMA)](https://www.dhs.gov/cisa/federal-सूचना-सुरक्षा-आधुनिकीकरण-कार्य)
 - [पेस्टर - पॉवरशेल परीक्षण फ़्रेम] (https://github.com/pester/Pester)
 - [डेटा सुरक्षा के लिए दांव लगाने के लिए शुरुआती गाइड]
 - [विंडोज़ पर सुरक्षा स्थापित करने के लिए सर्वोत्तम प्रयोग](https://simeonsecurity.ch/articles/best-practices-for-installing-security-patches-on-windows/)
 
 
 
 
