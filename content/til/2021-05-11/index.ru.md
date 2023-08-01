---
title: "Сегодня я узнал о Auditpol, Sysmon и конфигурациях Sysmon"
date: 2021-05-11
toc: true
draft: false
description: ""
genre: ["PowerShell", "Автоматизация", "Sysmon", "Конфигурации", "Безопасность Windows", "Мониторинг событий", "Администрирование Windows", "Аудит безопасности", "Охота за угрозами", "Анализ вредоносного ПО"]
tags: ["PowerShell", "Автоматизация", "Sysmon", "Конфигурации", "SwiftOnSecurity", "Безопасность Windows", "Мониторинг событий", "Аудиторский полюс", "Политика аудита Windows", "Automate-Sysmon", "Windows-Audit-Policy", "Начало работы с Sysmon", "Шпаргалки по археологии вредоносного ПО", "Microsoft Sysinternals", "Конфигурации Sysmon", "Команды Auditpol", "Резервное копирование Auditpol", "Auditpol Clear", "Список полюсов аудита", "Восстановление аудитпола", "Sysmon-Modular", "Средства администрирования Windows", "Ведение журнала безопасности", "Обнаружение угроз", "Ведение журнала событий", "Мониторинг безопасности", "Передовые методы обеспечения безопасности Windows", "Решения для автоматизации", "Методы аудита безопасности"]
---

**Что интересного узнал и нашел сегодня SimeonOnSecurity**.

Сегодня SimeonOnSecurity узнал и обнаружил несколько интересных вещей, связанных с безопасностью Windows и мониторингом событий.

Во-первых, были обнаружены два новых и обновленных репозитория. Репозиторий Automate-Sysmon предоставляет решение для автоматизации установки, настройки и управления Sysmon, популярным инструментом для мониторинга и протоколирования системной активности в системах Windows. Репозиторий Windows-Audit-Policy предназначен для автоматизации настройки политик аудита Windows, которые управляют аудитом различных событий, связанных с безопасностью, в системах Windows.

SimeonOnSecurity также нашел несколько обучающих ресурсов, связанных с безопасностью Windows и мониторингом событий. Статья Getting Started With Sysmon содержит исчерпывающее представление о Sysmon, включая его возможности, преимущества и способы эффективного использования. Шпаргалки по археологии вредоносного ПО содержат краткую и практичную информацию по различным темам, связанным с анализом вредоносного ПО и поиском угроз. Документация Microsoft Sysinternals - Sysmon содержит информацию о возможностях и использовании Sysmon. Репозиторий sysmon-config предоставляет набор предварительно настроенных правил Sysmon, которые можно использовать в качестве отправной точки для настройки конфигурации Sysmon.

Наконец, SimeonOnSecurity нашел несколько ресурсов, связанных с инструментом командной строки политики аудита Windows (auditpol). Документы auditpol backup, auditpol clear, auditpol list и auditpol restore содержат информацию о том, как использовать эти команды для управления политикой аудита Windows. Документ auditpol содержит полный обзор инструмента auditpol и его возможностей. Наконец, репозиторий sysmon-modular предоставляет модульный подход к настройке Sysmon, который может быть полезен для крупных организаций со сложными требованиями к безопасности.

## Новые/обновленные репозитории:

- [simeononsecurity/Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
- [simeononsecurity/Windows-Audit-Policy](https://github.com/simeononsecurity/Windows-Audit-Policy)

## Учебные ресурсы:

- [BHIS - Getting Started With Sysmon](https://www.blackhillsinfosec.com/getting-started-with-sysmon/)
- [Malware Archaeology Cheat Sheets](https://www.malwarearchaeology.com/cheat-sheets)
- [Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config)
- [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
- [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
- [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)
- [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
- [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
- [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular)
