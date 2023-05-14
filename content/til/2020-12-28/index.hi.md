---
title: "आज मैंने CVE-2020-17049 और Windows टोकन-आधारित सक्रियण के बारे में सीखा"
date: 2020-12-27
toc: true
draft: false
description: ""
tags: []
---

** शिमोनऑनसिक्योरिटी ने आज क्या सीखा और दिलचस्प पाया **

SimeonOnSecurity ने हाल ही में कंप्यूटर सुरक्षा के क्षेत्र में दो विषयों के बारे में सीखा: CVE-2020-17049, जिसे करबरोस ब्रॉन्ज़ बिट अटैक के रूप में भी जाना जाता है, और Windows टोकन-आधारित सक्रियण।

केर्बरोस ब्रॉन्ज बिट अटैक, जैसा कि नेटस्पी द्वारा ब्लॉग पोस्ट की एक श्रृंखला में और ट्रिमार्कसिक्योरिटी द्वारा एक पोस्ट में समझाया गया है, केर्बरोस प्रमाणीकरण प्रोटोकॉल में एक भेद्यता है। यह भेद्यता संभावित रूप से एक हमलावर को एक सक्रिय निर्देशिका से समझौता करने की अनुमति दे सकती है, जो कि एक संगठन के उपयोगकर्ताओं, कंप्यूटरों और अन्य संसाधनों के बारे में जानकारी के लिए एक केंद्रीय भंडार है। इस भेद्यता को दूर करने के लिए Kerberos S4U के परिनियोजन पर Microsoft समर्थन आलेख में चर्चा की गई है।

Windows टोकन-आधारित सक्रियण Windows उत्पादों को सक्रिय करने की एक विधि है, जैसा कि Microsoft प्रलेखन आलेख में वर्णित है। सक्रियण प्रक्रिया SLMGR.vbs स्क्रिप्ट के माध्यम से की जाती है, जैसा कि ss64.com पर एक व्यापक लेख में बताया गया है। Microsoft Technet पर एक फ़ोरम पोस्ट Windows 10 एंटरप्राइज़ टोकन आधारित सक्रियण के बारे में अधिक जानकारी प्रदान करता है।

## CVE-2020-17049 - करबरोस ब्रॉन्ज़ बिट अटैक:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## विंडोज टोकन-आधारित सक्रियण:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## रुचि के वीडियो:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
