---
title: "ChromiumADMX: правильный шаблон ADMX для браузера Chromium"
date: 2020-07-25
---


Правильный шаблон ADMX для браузера Chromium

Chromium как компания не выпустила шаблоны ADMX для браузера Chromium, которые можно было бы установить одновременно с шаблонами Google Chrome.
Имея это в виду, мы изменили шаблоны Google Chrome ADMX, чтобы они отражали путь реестра браузера Chromium, и поместили их в папку Google ADMX в GPO.

**Эти определения политик находятся в состоянии Pre-Alpha. Их следует использовать только в целях тестирования**

## Загрузите необходимые файлы

** Загрузите необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Примечания

Изменены определения политики Google Chrome в соответствии с:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Примечание.** Заменено «HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome» на «HKEY_LOCAL_MACHINE\Software\Policies\Chromium\».

**Примечание.** Не устанавливайте одновременно шаблоны SOS Chromium и Brave Browser ADMX.

## Как установить

1.) Скопируйте все файлы, кроме readme.md, в "C:\Windows\PolicyDefinitions" и/или "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Прибыль?




