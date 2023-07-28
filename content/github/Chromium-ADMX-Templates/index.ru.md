---
title: "ChromiumADMX: Правильный шаблон ADMX для браузера Chromium"
date: 2020-07-25
---


Правильный шаблон ADMX для браузера Chromium

Компания Chromium не выпустила ADMX-шаблоны для браузера Chromium, которые могут быть установлены одновременно с шаблонами Google Chrome.
В связи с этим мы изменили ADMX-шаблоны Google Chrome, чтобы они отражали путь к реестру браузера Chromium, и поместили их в папку Google ADMX в GPO.

**Эти определения политики находятся в состоянии предварительной альфа-версии. Их следует использовать только для тестирования**.

## Загрузите необходимые файлы

**Скачайте необходимые файлы с сайта [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Примечания

Изменены определения политики Google Chrome в соответствии с:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Примечание:** Замените "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" на "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\".

**Примечание:** Не устанавливайте одновременно ADMX-шаблоны SOS'es Chromium и Brave Browser.

## Как установить

1.) Скопируйте все файлы, кроме readme.md, в папку "C:\Windows\PolicyDefinitions" и/или "\\\\domain.tld\domain\Policies\PolicyDefinitions".

2.) Прибыль?




