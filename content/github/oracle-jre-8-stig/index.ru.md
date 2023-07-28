---
title: "Автоматизация соответствия Oracle JRE 8 STIG с помощью сценария Powershell"
date: 2020-08-05
---


СТИГи для Oracle JRE не так просты, они требуют от администраторов изучения документации по JAVA и создания конфигурационных файлов java, в то время как большинство администраторов привыкли обходиться исключительно СТИГами с помощью групповой политики.

## Загрузите необходимые файлы

Загрузите необходимые файлы с сайта [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## Применяемые СТИГи/СРГ:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Источники:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Как запустить скрипт

**Сценарий может быть запущен из извлеченной на GitHub загрузки следующим образом:**

```
.\sos-install-java-config.ps1
```
