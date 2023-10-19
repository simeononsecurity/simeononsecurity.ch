---
title: "Усовершенствование Windows и серверных систем: Руководство по настройке пользовательского брендинга"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Брендинг Windows", "Брендинг сервера", "индивидуальный брендинг", "настройка системы", "настройка брендинга", "Windows 10", "Сервер 2016", "Сервер 2019", "Сервер 2022", "пользовательский опыт", "руководство по настройке системы", "персонализация", "брендинг системы", "Настройка Windows", "Настройка сервера", "Логотип OEM", "изображение пользователя", "изображение гостя", "сценарий брендинга", "Microsoft Security Compliance Toolkit", "Настройка брендинга Windows", "Настройка брендинга сервера", "руководство по брендингу", "персонализированный брендинг", "учебник по настройке системы", "Настройка системы Windows", "Настройка серверной системы", "брендинговые изображения", "лучшие практики брендинга", "Советы по настройке Windows", "Методы настройки сервера"]
---

**Настройка брендинга на системах Windows 10 и Server 2016/2019/2022**.

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## Как настроить файлы брендинга
- [X] Замените все изображения на изображения вашего брендинга
  - [X] Логотип производителя должен иметь размер 95x95 или 120x20 и формат ".bmp".
  - [X] Сгенерировать пользовательское изображение с вариантами 32x32, 40x40, 48x48, 192x192.
  - [X] Сгенерировать или скопировать пользовательский образ для гостевого образа.
  
## В данном скрипте используется следующий инструмент:
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Как запустить скрипт
### Установка вручную:
При ручной загрузке скрипт должен быть запущен из административного powershell в директории, содержащей все файлы из каталога [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Автоматическая установка:
Скрипт может быть запущен из распакованной загрузки с GitHub следующим образом:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosbranding.ps1'|iex
```

