---
title: "Автоматизируйте активацию Windows KMS с помощью сценария GLVK"
date: 2020-12-18
toc: true
draft: false
description: "Упростите процесс активации Windows 10 KMS с помощью сценария автоматической установки GLVK от SimeonOnSecurity и узнайте больше о клиентских ключах KMS и GLVK из рекомендованной Microsoft литературы."
tags: ["Активация Windows", "Ключи клиента KMS", "ГЛВК", "Обновления Windows", "Согласие", "Сценарий PowerShell", "Служба управления ключами", "Корпоративное лицензирование", "Корпоративная активация", "Сервер управления ключами", "Автоматизация", "Продукты Майкрософт", "Операционная система", "Программное обеспечение", "Корпоративные среды", "Административный PowerShell", "Репозиторий GitHub", "Скрипты", "Информационная безопасность", "СимеонОнСекьюрити"]
---

Сценарий автоматической установки GLVK для активации KMS

## Рекомендуемое чтение:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Как запустить скрипт:
### Ручная установка:
При ручной загрузке скрипт необходимо запускать из административной оболочки в каталоге, содержащем все файлы из[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
