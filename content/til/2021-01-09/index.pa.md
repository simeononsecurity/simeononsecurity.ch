---
title: "ਅੱਜ ਮੈਂ XFS ਡੇਟਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਰਿਕਵਰੀ ਬਾਰੇ ਸਿੱਖਿਆ"
date: 2021-01-09
toc: true
draft: false
description: ""
tags: []
---

**SimeonOnSecurity ਨੇ ਅੱਜ ਇਸ ਬਾਰੇ ਕੀ ਸਿੱਖਿਆ ਅਤੇ ਦਿਲਚਸਪ ਪਾਇਆ**

SimeonOnSecurity ਤਕਨੀਕੀ ਜਗਤ ਵਿੱਚ ਨਵੀਨਤਮ ਵਿਕਾਸ ਨਾਲ ਜੁੜੀ ਹੋਈ ਹੈ। ਅੱਜ, ਉਸਨੇ XFS ਅਤੇ ਫਾਈਲ ਸਿਸਟਮਾਂ ਦਾ ਬੈਕਅੱਪ ਲੈਣ ਅਤੇ ਰੀਸਟੋਰ ਕਰਨ ਲਈ ਇਸ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਬਾਰੇ ਸਿੱਖਿਆ। ਉਸਨੇ Red Hat ਵੈੱਬਸਾਈਟ 'ਤੇ XFS ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਪ੍ਰਕਿਰਿਆ ਅਤੇ ਵਧੀਆ ਅਭਿਆਸਾਂ ਦਾ ਵੇਰਵਾ ਦੇਣ ਵਾਲਾ ਇੱਕ ਜਾਣਕਾਰੀ ਭਰਪੂਰ ਲੇਖ ਪਾਇਆ।

SimeonOnSecurity ਨੇ GitHub 'ਤੇ ਆਪਣੀ Shodan_PS ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਵੀ ਅੱਪਡੇਟ ਕੀਤਾ, ਜਿਸ ਵਿੱਚ ਇੰਟਰਨੈੱਟ ਨਾਲ ਜੁੜੀਆਂ ਡਿਵਾਈਸਾਂ ਲਈ ਪ੍ਰਸਿੱਧ ਖੋਜ ਇੰਜਣ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਉਪਯੋਗੀ ਸਕ੍ਰਿਪਟਾਂ ਸ਼ਾਮਲ ਹਨ।

ਵਿਡੀਓ ਸਮਗਰੀ ਦੇ ਸੰਦਰਭ ਵਿੱਚ, SimeonOnSecurity ਨੇ ਕਈ ਵਿਡੀਓਜ਼ ਦੇਖੇ ਜੋ ਉਸਦੀ ਦਿਲਚਸਪੀ ਨੂੰ ਵਧਾਉਂਦੇ ਹਨ। ਡੇਵਜ਼ ਗੈਰਾਜ ਦੁਆਰਾ ਪਹਿਲੀ ਵੀਡੀਓ, "ਵਿੰਡੋਜ਼ ਜ਼ਿਪਫੋਲਡਰ ਦਾ ਗੁਪਤ ਇਤਿਹਾਸ", ਵਿੰਡੋਜ਼ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਵਿੱਚ ਸੰਕੁਚਨ ਫਾਰਮੈਟ ਦੇ ਇਤਿਹਾਸ ਅਤੇ ਵਿਕਾਸ ਦੀ ਖੋਜ ਕਰਦਾ ਹੈ। ਡਿਸਟ੍ਰੋਟਿਊਬ ਦੁਆਰਾ ਇੱਕ ਹੋਰ ਵੀਡੀਓ, "12 ਲੀਨਕਸ ਐਪਸ ਹਰ ਕਿਸੇ ਨੂੰ ਇਸ ਬਾਰੇ ਪਤਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ", ਲੀਨਕਸ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਉਪਲਬਧ ਕੁਝ ਸਭ ਤੋਂ ਉਪਯੋਗੀ ਅਤੇ ਬਹੁਮੁਖੀ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਉਜਾਗਰ ਕਰਦਾ ਹੈ।

ਇਸ ਤੋਂ ਇਲਾਵਾ, SimeonOnSecurity ਨੇ ਗਾਰਡੀਨਰ ਬ੍ਰਾਇਨਟ ਦੁਆਰਾ PHP 8 ਦੀਆਂ ਗੇਮ-ਬਦਲਣ ਵਾਲੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਬਾਰੇ ਚਰਚਾ ਕਰਦੇ ਹੋਏ ਇੱਕ ਵੀਡੀਓ ਦੇਖਿਆ ਅਤੇ ਲਿਨਸ ਟੈਕ ਟਿਪਸ ਦੁਆਰਾ ਇੱਕ ਹੋਰ ਵੀਡੀਓ ਜੋ ਉਸਨੇ ਹੁਣ ਤੱਕ ਖਰਚ ਕੀਤੇ ਸਭ ਤੋਂ ਮਾੜੇ ਪੈਸੇ ਬਾਰੇ ਹੈ। ਅੰਤ ਵਿੱਚ, ਜ਼ੈਕ ਫ੍ਰੀਡਮੈਨ ਦੇ ਵੀਡੀਓ, "2021 ਵਿੱਚ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟਾਂ ਨੂੰ ਪੂਰਾ ਕਰੋ - ਥ੍ਰੀ ਕਾਮਨ ਸੈਂਸ ਰਣਨੀਤੀਆਂ," ਨੇ ਪ੍ਰੋਜੈਕਟਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਅਤੇ ਕੇਂਦਰਿਤ ਰਹਿਣ ਲਈ ਕੁਝ ਵਿਹਾਰਕ ਸੁਝਾਅ ਦਿੱਤੇ ਹਨ।

ਕੁੱਲ ਮਿਲਾ ਕੇ, SimeonOnSecurity ਟੈਕਨਾਲੋਜੀ ਦੇ ਨਵੀਨਤਮ ਵਿਕਾਸ ਨਾਲ ਰੁੱਝੀ ਹੋਈ ਹੈ ਅਤੇ ਸੂਚਿਤ ਕਰਦੀ ਹੈ ਅਤੇ ਇਸ ਤੋਂ ਸਿੱਖਣ ਲਈ ਹਮੇਸ਼ਾਂ ਨਵੀਂ ਅਤੇ ਦਿਲਚਸਪ ਸਮੱਗਰੀ ਦੀ ਭਾਲ ਵਿੱਚ ਰਹਿੰਦੀ ਹੈ।

## XFS:
-[RedHat - 3.7. Backing Up and Restoring XFS File Systems](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/xfsbackuprestore)

## ਅੱਪਡੇਟ ਕੀਤੇ ਰਿਪੋਜ਼:
-[SimeonOnSecurity - Shodan_PS](https://github.com/simeononsecurity/Shodan_PS)

## ਦਿਲਚਸਪੀ ਵਾਲੇ ਵੀਡੀਓ:
-[Dave's Garage - The Secret History of Windows ZIPFolders](https://www.youtube.com/watch?v=aQUtUQ_L8Yk)
-[DistroTube - The 12 Linux Apps Everyone Should Know About](https://www.youtube.com/watch?v=6chA0L_AT6k)
-[Gardiner Bryant - The GAMECHANGING features of PHP 8!](https://www.youtube.com/watch?v=f_cwnwaEwaY)
-[Linus Tech Tips - The WORST Money I've Ever Spent](https://www.youtube.com/watch?v=sLM_vO4d2Jg)
-[Zack Freedman - FINISH YOUR PROJECTS in 2021 - Three Common Sense Strategies](https://www.youtube.com/watch?v=L1j93RnIxEo)
