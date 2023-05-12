---
title: "ਅੱਜ ਮੈਂ CVE-2020-17049 ਅਤੇ ਵਿੰਡੋਜ਼ ਟੋਕਨ-ਅਧਾਰਿਤ ਐਕਟੀਵੇਸ਼ਨ ਬਾਰੇ ਸਿੱਖਿਆ"
date: 2020-12-27
toc: true
draft: false
---

**SimeonOnSecurity ਨੇ ਅੱਜ ਇਸ ਬਾਰੇ ਕੀ ਸਿੱਖਿਆ ਅਤੇ ਦਿਲਚਸਪ ਪਾਇਆ**

SimeonOnSecurity ਨੇ ਹਾਲ ਹੀ ਵਿੱਚ ਕੰਪਿਊਟਰ ਸੁਰੱਖਿਆ ਦੇ ਖੇਤਰ ਵਿੱਚ ਦੋ ਵਿਸ਼ਿਆਂ ਬਾਰੇ ਸਿੱਖਿਆ ਹੈ: CVE-2020-17049, ਜਿਸਨੂੰ ਕਰਬਰੋਸ ਬ੍ਰਾਂਜ਼ ਬਿਟ ਅਟੈਕ ਵੀ ਕਿਹਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਵਿੰਡੋਜ਼ ਟੋਕਨ-ਆਧਾਰਿਤ ਐਕਟੀਵੇਸ਼ਨ।

Kerberos Bronze Bit Attack, ਜਿਵੇਂ ਕਿ Netspi ਦੁਆਰਾ ਬਲੌਗ ਪੋਸਟਾਂ ਦੀ ਇੱਕ ਲੜੀ ਵਿੱਚ ਅਤੇ Trimarcsecurity ਦੁਆਰਾ ਇੱਕ ਪੋਸਟ ਵਿੱਚ ਦੱਸਿਆ ਗਿਆ ਹੈ, Kerberos ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰੋਟੋਕੋਲ ਵਿੱਚ ਇੱਕ ਕਮਜ਼ੋਰੀ ਹੈ। ਇਹ ਕਮਜ਼ੋਰੀ ਸੰਭਾਵੀ ਤੌਰ 'ਤੇ ਹਮਲਾਵਰ ਨੂੰ ਇੱਕ ਐਕਟਿਵ ਡਾਇਰੈਕਟਰੀ ਨਾਲ ਸਮਝੌਤਾ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਦੇ ਸਕਦੀ ਹੈ, ਜੋ ਕਿ ਇੱਕ ਸੰਗਠਨ ਦੇ ਉਪਭੋਗਤਾਵਾਂ, ਕੰਪਿਊਟਰਾਂ ਅਤੇ ਹੋਰ ਸਰੋਤਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ ਇੱਕ ਕੇਂਦਰੀ ਭੰਡਾਰ ਹੈ। ਇਸ ਕਮਜ਼ੋਰੀ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ Kerberos S4U ਤਬਦੀਲੀਆਂ ਦੀ ਤੈਨਾਤੀ ਬਾਰੇ Microsoft ਸਹਾਇਤਾ ਲੇਖ ਵਿੱਚ ਚਰਚਾ ਕੀਤੀ ਗਈ ਹੈ।

ਵਿੰਡੋਜ਼ ਟੋਕਨ-ਅਧਾਰਿਤ ਐਕਟੀਵੇਸ਼ਨ ਵਿੰਡੋਜ਼ ਉਤਪਾਦਾਂ ਨੂੰ ਸਰਗਰਮ ਕਰਨ ਦਾ ਇੱਕ ਤਰੀਕਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਇੱਕ Microsoft ਦਸਤਾਵੇਜ਼ ਲੇਖ ਵਿੱਚ ਦੱਸਿਆ ਗਿਆ ਹੈ। ਐਕਟੀਵੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ SLMGR.vbs ਸਕ੍ਰਿਪਟ ਦੁਆਰਾ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ss64.com 'ਤੇ ਇੱਕ ਵਿਆਪਕ ਲੇਖ ਵਿੱਚ ਦੱਸਿਆ ਗਿਆ ਹੈ। Microsoft Technet 'ਤੇ ਇੱਕ ਫੋਰਮ ਪੋਸਟ ਵਿੰਡੋਜ਼ 10 ਐਂਟਰਪ੍ਰਾਈਜ਼ ਟੋਕਨ ਅਧਾਰਤ ਐਕਟੀਵੇਸ਼ਨ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ।

## CVE-2020-17049 - ਕਰਬੇਰੋਸ ਕਾਂਸੀ ਦਾ ਬਿੱਟ ਹਮਲਾ:
-[CVE-2020-17049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-17049)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Practical Exploitation](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-attack/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Theory](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-theory/)
-[CVE-2020-17049: Kerberos Bronze Bit Attack – Overview](https://blog.netspi.com/cve-2020-17049-kerberos-bronze-bit-overview/)
-[Kerberos Bronze Bit Attack (CVE-2020-17049) Scenarios to Potentially Compromise Active Directory](https://www.hub.trimarcsecurity.com/post/leveraging-the-kerberos-bronze-bit-attack-cve-2020-17049-scenarios-to-compromise-active-directory)
-[Managing deployment of Kerberos S4U changes for CVE-2020-17049](https://support.microsoft.com/en-us/help/4598347/managing-deployment-of-kerberos-s4u-changes-for-cve-2020-17049)

## ਵਿੰਡੋਜ਼ ਟੋਕਨ-ਅਧਾਰਿਤ ਐਕਟੀਵੇਸ਼ਨ:
-[Plan for volume activation](https://docs.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client)
-[SLMGR.vbs](https://ss64.com/nt/slmgr.html)
-[Windows 10 Enterprise Token Based Activation](https://social.technet.microsoft.com/Forums/windows/en-US/8c4c0841-af1b-4c14-91f8-31128fc08bf5/windows-10-enterprise-token-based-activation?forum=win10itprosetup)

## ਦਿਲਚਸਪੀ ਦੇ ਵੀਡੀਓ:
-[Fungible F1 DPU Powered Storage Hands-on at Fungible HQ](https://www.youtube.com/watch?v=NjhTTMNGBBw&t)
-[Heavy gaming on Raspberry Pi 400](https://www.youtube.com/watch?v=Ag53sdLXsFk)
-[Inside a 32x100GbE Switch and its Big Flaw](https://www.youtube.com/watch?v=fkc2pFFGCtE)
-[Mastering Chaos - A Netflix Guide to Microservices](https://www.youtube.com/watch?v=CZ3wIuvmHeM)
-[Sony brings OFFICIAL DualSense support to Linux!](https://www.youtube.com/watch?v=YSgbcJrnZzE)
-[Will Microsoft turn Windows 10 into a yet another Linux distro?](https://www.youtube.com/watch?v=vdycbruoZ9s)
