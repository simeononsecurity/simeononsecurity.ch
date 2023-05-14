---
title: "Автоматизируйте соответствие FireFox STIG с помощью сценариев PowerShell"
date: 2020-08-15
---

Скрипт FireFox STIG

[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip) не самый простой из STIG для применения.
Этот сценарий реализует большинство необходимых политик FireFox. В будущем в этом скрипте будут применяться шаблоны FireFox ADMX и объекты групповой политики.

**Работа в процессе**

## Загрузите необходимые файлы

Скачайте необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/FireFox-STIG-Script)

## Как запустить скрипт


**Скрипт можно запустить из извлеченной загрузки GitHub следующим образом:**
```
.\sos-firefoxstig.ps1
```