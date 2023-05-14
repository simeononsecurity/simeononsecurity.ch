---
title: "Возьмите под свой контроль политики браузера Brave с помощью BraveADMX — модифицированные шаблоны ADMX"
date: 2020-07-25
---


Brave, как компания, не смогла выпустить шаблоны ADMX для смелого браузера, продвигающего чистые реестры как единственный поддерживаемый вариант.
Поскольку браузер Brave основан на Chromium, он должен поддерживать большинство, если не все, те же политики, что и шаблоны Chromium и Google Chrome ADMX.
Имея это в виду, мы изменили шаблоны Google Chrome ADMX, чтобы отразить путь реестра Brave Browser. После некоторого первоначального устранения неполадок и тестирования шаблоны, похоже, работают.

**Эти определения политик находятся в состоянии Pre-Alpha. Их следует использовать только в целях тестирования**

## Загрузите необходимые файлы.

** Загрузите необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Примечания

Изменены определения политики Google Chrome в соответствии с:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Примечание.** Заменено «HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome» на «HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave».

**Примечание.** Не устанавливайте одновременно шаблоны SOS Chromium и Brave Browser ADMX.

## Как установить

1.) Скопируйте все файлы, кроме readme.md, в "C:\Windows\PolicyDefinitions" и/или "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Прибыль?