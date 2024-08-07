---
title: "Защита Windows от спекулятивных атак по побочным каналам"
date: 2020-06-18
toc: true
draft: false
description: "Узнайте, как защитить свою систему Windows от спекулятивных атак по сторонним каналам с помощью сценария смягчения последствий Microsoft и обновлений встроенного ПО."
tags: ["Сценарий предотвращения аварийного восстановления Windows Spectre", "Спекулятивные атаки по побочным каналам", "Майкрософт", "Интел", "AMD", "С ПОМОЩЬЮ", "РУКА", "Андроид", "Хром", "iOS", "macOS", "Внедрение целевых ветвей", "Обход проверки границ", "Мошенническая загрузка кэша данных", "Спекулятивный обход магазина", "Микроархитектурная выборка данных", "CVE", "Обновления прошивки", "Репозиторий GitHub", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Простой сценарий для реализации защиты от уязвимостей второстепенных каналов спекулятивного выполнения в системах Windows.**

Microsoft известно о новом публично раскрытом классе уязвимостей, которые называются «атаки со спекулятивным выполнением по сторонним каналам» и затрагивают многие современные процессоры, включая Intel, AMD, VIA и ARM.

**Примечание.** Эта проблема также затрагивает другие операционные системы, такие как Android, Chrome, iOS и macOS. Поэтому мы советуем клиентам обращаться за рекомендациями к этим поставщикам.

Мы выпустили несколько обновлений, помогающих устранить эти уязвимости. Мы также приняли меры для защиты наших облачных сервисов. Дополнительные сведения см. в следующих разделах.

Мы еще не получили никакой информации, указывающей на то, что эти уязвимости использовались для атак на клиентов. Мы тесно сотрудничаем с отраслевыми партнерами, включая производителей микросхем, OEM-производителей оборудования и поставщиков приложений, чтобы защитить клиентов. Для получения всех доступных средств защиты требуются обновления прошивки (микрокода) и программного обеспечения. Это включает в себя микрокод от OEM-производителей устройств и, в некоторых случаях, обновления антивирусного программного обеспечения.

**В этой статье рассматриваются следующие уязвимости:**
- CVE-2017-5715 – «Внедрение целевой ветви»
- CVE-2017-5753 – «Обход проверки границ»
- CVE-2017-5754 – «Мошенническая загрузка кэша данных».
- CVE-2018-3639 – «Спекулятивный обход магазина»
- CVE-2018-11091 — «Микроархитектурная выборка данных из некэшируемой памяти (MDSUM)»
- CVE-2018-12126 — «Выборка данных буфера хранилища микроархитектуры (MSBDS)»
- CVE-2018-12127 – «Микроархитектурная выборка данных буфера заполнения (MFBDS)»
- CVE-2018-12130 — «Микроархитектурная выборка данных порта загрузки (MLPDS)»

**ОБНОВЛЕНО 6 АВГУСТА 2019 ГОДА** 6 августа 2019 года корпорация Intel опубликовала подробную информацию об уязвимости раскрытия информации ядра Windows. Эта уязвимость представляет собой разновидность уязвимости побочного канала спекулятивного выполнения Spectre Variant 1 и получила код CVE-2019-1125.

**ОБНОВЛЕНО 12 НОЯБРЯ 2019 г.** 12 ноября 2019 г. корпорация Intel опубликовала технические рекомендации по уязвимости асинхронного прерывания транзакций в модулях Intel® Transactional Synchronization Extensions (Intel® TSX), которой присвоен код CVE-2019-11135. Корпорация Майкрософт выпустила обновления, помогающие устранить эту уязвимость, а средства защиты ОС включены по умолчанию для клиентских ОС Windows.

## Рекомендуемые действия
Клиенты должны предпринять следующие действия для защиты от уязвимостей:

- Примените все доступные обновления операционной системы Windows, включая ежемесячные обновления безопасности Windows.
- Примените применимое обновление встроенного ПО (микрокода), предоставленное производителем устройства.
- Оцените риск для вашей среды на основе информации, предоставленной Microsoft Security Advisors: ADV180002, ADV180012, ADV190013 и информации, представленной в этой статье базы знаний.
- Примите необходимые меры, используя рекомендации и сведения о разделе реестра, приведенные в этой статье базы знаний.

## Загрузите необходимые файлы:

Скачайте необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Как запустить скрипт:

**Скрипт можно запустить из извлеченной загрузки GitHub следующим образом:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
