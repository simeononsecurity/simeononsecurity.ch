---
title: "Эффективное сканирование на вирусы с помощью модулей VirusTotal PowerShell"
date: 2020-11-24
toc: true
draft: false
description: "Выполняйте эффективное сканирование на вирусы с помощью модулей VirusTotal PowerShell, автоматизируя взаимодействие с VirusTotal API и оптимизируя рабочий процесс безопасности."
tags: ["Модули PowerShell", "PowerShell", "Автоматизация", "VirusTotal", "Проверка на вирусы", "Сканирование домена", "API-ключ", "Вирустотал API", "Страница разработчиков VirusTotal", "Системное администрирование", "Рабочий процесс безопасности", "Эффективное сканирование на вирусы", "Загрузить и установить", "Репозиторий GitHub", "Примеры использования API"]
---
 коллекция модулей PowerShell для взаимодействия с API VirusTotal

**Примечания:**
- Вам понадобится ключ API VirusTotal, который можно найти на[Shodan Account](https://www.virustotal.com/gui/)
- Примеры API, используемых в модулях, можно найти на[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Загрузить и установить
- Скачать модули с[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Установить все модули
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```