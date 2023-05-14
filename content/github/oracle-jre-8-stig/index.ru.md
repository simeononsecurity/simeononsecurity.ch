---
title: "Автоматизация соответствия Oracle JRE 8 STIG с помощью скрипта Powershell"
date: 2020-08-05
---


STIG Oracle JRE не так просты, требуя от администраторов изучения документации JAVA и создания файлов конфигурации Java, в то время как большинство администраторов привыкли использовать только STIG с помощью групповой политики.

## Загрузите необходимые файлы

Скачайте необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## Применены STIGS/SRG:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Источники:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Как запустить скрипт

**Скрипт можно запустить из извлеченной загрузки GitHub следующим образом:**

```
.\sos-install-java-config.ps1
```
