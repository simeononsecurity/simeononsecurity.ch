---
title: "ਜਵਾਬਦੇਹ STIG ਪਲੇਬੁੱਕ ਦੇ ਨਾਲ ਵਿੰਡੋਜ਼ ਦੀ ਪਾਲਣਾ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰੋ"
date: 2022-04-26
toc: true
draft: false
description: "ਵਿੰਡੋਜ਼ ਸਿਸਟਮਾਂ ਲਈ ਜਵਾਬਦੇਹ STIG ਪਲੇਬੁੱਕਸ ਦੇ ਨਾਲ ਆਪਣੀ ਸੁਰੱਖਿਆ ਦੀ ਪਾਲਣਾ ਨੂੰ ਸਟ੍ਰੀਮਲਾਈਨ ਕਰੋ।"
tags: ["ਆਟੋਮੇਸ਼ਨ", "ਵਿੰਡੋਜ਼ ਦੀ ਪਾਲਣਾ", "ਜਵਾਬਦੇਹ STIG ਪਲੇਬੁੱਕਸ", "ਵਿੰਡੋਜ਼ ਹਾਰਡਨਿੰਗ", "STIG ਸਕ੍ਰਿਪਟਾਂ", "STIG ਪਾਲਣਾ", "ਜਵਾਬਦੇਹ ਗਲੈਕਸੀ", "ਪਾਵਰਸ਼ੇਲ", "PowerShell ਸਕ੍ਰਿਪਟ", "ਵਿੰਡੋਜ਼ ਸਰਵਰ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ", ".NET", "ਫਾਇਰਫਾਕਸ", "ਓਰੇਕਲ ਜੇਆਰਈ 8", "ਅਡੋਬ ਰੀਡਰ ਡੀ.ਸੀ", "ਇੰਟਰਨੈੱਟ ਕਨੈਕਟੀਵਿਟੀ", "ਔਫਲਾਈਨ ਅਨੁਕੂਲਤਾ", "ਸੁਰੱਖਿਆ ਸਖ਼ਤ", "ਵਿੰਡੋਜ਼ ਸੁਰੱਖਿਆ"]
---


SimeonOnSecurity ਦੀਆਂ STIG ਸਕ੍ਰਿਪਟਾਂ ਲਈ ਜਵਾਬਦੇਹ ਪਲੇਬੁੱਕ

## ਨੋਟ:

- ਵਰਤਮਾਨ ਵਿੱਚ ਇੰਟਰਨੈਟ ਕਨੈਕਟੀਵਿਟੀ ਦੀ ਲੋੜ ਹੈ। (ਆਫਲਾਈਨ ਅਨੁਕੂਲਤਾ WIP)

## ਵਰਤੋਂ:

## ਇੰਸਟਾਲੇਸ਼ਨ:

-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

```bash
ansible-galaxy collection install simeononsecurity.windows_stigs
```

## ਦੇ ਅਧਾਰ ਤੇ:

-[simeononsecurity/STIG-Compliant-Domain-Prep](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)
-[simeononsecurity/Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[simeononsecurity/Standalone-Windows-Server-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-Server-STIG-Script)
-[simeononsecurity/Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[simeononsecurity/.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[simeononsecurity/FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[simeononsecurity/Oracle-JRE-8-STIG-Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
-[simeononsecurity/Adobe-Reader-DC-STIG-Script](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script)
