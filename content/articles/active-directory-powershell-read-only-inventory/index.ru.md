---
title: "Создание инвентаризации Active Directory только для чтения с помощью PowerShell"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Соберите сведения об OU, пользователях и компьютерах Active Directory с помощью ограниченных запросов PowerShell. Экспортируйте проверяемые CSV-файлы, не изменяя объекты каталога."
genre: ["Active Directory", "PowerShell", "Системное администрирование"]
tags: ["Инвентаризация Active Directory", "Инвентаризация AD с PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "AD только для чтения", "Экспорт пользователей AD", "Экспорт компьютеров AD", "Экспорт OU AD", "Export-Csv", "RSAT", "Аудит каталога", "Отчеты AD", "Инвентаризация OU", "Windows Server", "Скрипт PowerShell", "Модуль AD", "Гигиена каталога"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Дерево Active Directory, из которого сведения о пользователях, компьютерах и подразделениях поступают в три файла для проверки."
coverCaption: "Ограничьте область запроса и экспортируйте только поля, необходимые для проверки."
---
Очистка Active Directory начинается с достоверного списка существующих объектов. Эта **инвентаризация только для чтения** собирает сведения об организационных подразделениях, пользователях и компьютерах в выбранной области. Она экспортирует три CSV-файла для проверки, не изменяя объекты каталога. Эти файлы все равно нужно защищать, поскольку имена и сведения об устройствах раскрывают часть данных о вашей среде.

<!--more-->

## Главное

- **Выберите область:** сначала запросите одно организационное подразделение и только потом расширяйте область до всего домена.
- **Используйте команды чтения:** `Get-ADOrganizationalUnit`, `Get-ADUser` и `Get-ADComputer` извлекают объекты.
- **Выберите поля:** экспортируйте только свойства, нужные для задачи.
- **Проверьте результат:** сравните количество записей и несколько примеров, прежде чем полагаться на отчет.

## Перед началом

Вам нужен административный компьютер Windows с рабочими DNS и сетевым доступом к контроллеру домена, модуль PowerShell **ActiveDirectory**, учетная запись с разрешением на чтение выбранных объектов и защищенная папка для CSV-файлов. На клиентском компьютере Windows модуль устанавливается вместе с инструментами Active Directory из Remote Server Administration Tools (RSAT). Установка описана в [руководстве по модулю Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/). Microsoft публикует [справочник командлетов](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) и [варианты установки RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). В руководстве используется синтаксис Windows PowerShell, а объекты каталога не изменяются.

Права доступа к каталогу по-прежнему действуют. Microsoft объясняет в [рекомендациях по привилегированным учетным записям](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), что списки управления доступом часто разрешают аутентифицированным пользователям читать общие сведения, ограничивая доступ к конфиденциальным полям и изменениям. Сначала используйте утвержденную учетную запись и тестовую OU. Не повышайте права до Domain Admin ради успешной инвентаризации.

> **Предупреждение:** CSV-файлы содержат имена учетных записей и компьютеров. Сохраните их в утвержденном месте, ограничьте доступ и удалите лишние копии после проверки. Не публикуйте исходный экспорт и не прикрепляйте его к общедоступной задаче.

## Выбор базы поиска

**Организационное подразделение (OU)** объединяет объекты каталога. Его **distinguished name (DN)** определяет положение в дереве каталога. Параметр `-SearchBase` ограничивает запрос выбранным DN. Без четко заданной области широкий фильтр может вернуть намного больше объектов, чем нужно для проверки.

Сначала загрузите модуль и просмотрите DN текущего домена:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft описывает [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) и сведения о домене, которые он возвращает. Найдите нужную OU до выбора базы поиска:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Скопируйте точный DN из результата. В следующих примерах замените это справочное значение на DN своей OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` — домен для документации. Не копируйте его DN в рабочий запрос. Если вам намеренно нужна инвентаризация всего домена, задайте `$SearchBase` равным DN домена и укажите в отчете расширенную область. В [справочнике Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) Microsoft описаны `-Filter` и `-SearchBase`.

## Инвентаризация OU, пользователей и компьютеров

Начните с подсчета объектов. Это быстрый способ обнаружить неверную базу поиска или неожиданно пустой результат:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` означает, что выбираются все подходящие объекты в пределах базы поиска. Microsoft описывает [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) и [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) как команды чтения. Нулевой результат может быть корректным, но перед тем как считать инвентаризацию полной, проверьте DN, разрешения и целевой домен.

Теперь просмотрите несколько строк в консоли. Сохраните выбранные поля, чтобы предварительный просмотр и последующий экспорт CSV использовали одни и те же столбцы:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Запрашивайте дополнительное свойство операционной системы для компьютеров только тогда, когда оно нужно для проверки:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

Параметр `-Properties` запрашивает свойства за пределами стандартного набора командлета. Microsoft описывает его в [справочнике командлета для компьютеров](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer). Рассматривайте названия операционных систем как данные каталога, а не как подтверждение текущей установленной версии. Объект компьютера может быть устаревшим, а его атрибут — еще не обновленным.

## Экспорт проверяемых CSV-файлов

Выберите утвержденную папку для вывода с достаточным свободным местом. Следующие команды записывают **локальные CSV-файлы** и не меняют объекты каталога. Запустите их в этой папке. Параметр `-NoClobber` не позволяет перезаписать существующий файл. Для каждого запуска используйте новую папку или имя файла.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

В [справочнике Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) Microsoft объясняет параметры `-NoTypeInformation`, `-Encoding` и `-NoClobber`. Откройте каждый CSV-файл в текстовом редакторе или утвержденной программе для работы с таблицами. Проверьте заголовок, несколько строк и количество записей по предыдущим подсчетам. Ошибка команды или файл нулевого размера не подтверждают полноту отчета.

> **Ожидаемый результат:** у вас есть три CSV-файла с записями OU, пользователей и компьютеров в выбранной области. Число строк и примеры записей соответствуют выбранной области каталога.

## Проверка без изменения объектов

Используйте инвентаризацию для ответов на конкретные вопросы: какая OU отвечает за компьютер? Какие учетные записи пользователей отключены? Для каких имен устройств нужно найти владельца? Записывайте выводы в отдельной заметке. Значение `Enabled` само по себе не показывает, нужна ли учетная запись. Не удаляйте и не отключайте объект только на основании экспорта.

Для регулярного отчета записывайте дату запроса, домен, DN OU, выбранные свойства, оператора и расположение CSV-файла. При сравнении двух экспортов убедитесь, что в обоих использовались одинаковые область и поля. Иначе различие может объясняться самим запросом, а не изменением каталога.

Это **инвентаризация**, а не аудит привилегированных учетных записей и не отчет об активности входов. Microsoft отмечает, что свойства и разрешения Active Directory различаются в зависимости от объекта и среды. Перед действиями проверьте атрибут операционной системы или отображаемое имя у владельца системы. Более широкие меры безопасности описаны в [руководстве по безопасности Active Directory](/articles/active-directory-security-best-practices/).

## Устранение неполадок

- **Модуль не импортируется:** убедитесь, что на компьютере установлены инструменты Active Directory из RSAT или средства администрирования Windows Server. Следуйте [руководству по настройке модуля](/articles/active-directory-module-powershell-installation-usage-guide/).
- **Запрос не возвращает объекты:** проверьте точный DN, текущий домен, содержимое OU и права чтения. Прежде чем расширять область, проверьте небольшую известную OU.
- **Поле пустое:** убедитесь, что атрибут существует и учетная запись может его читать. Не заполняйте пустые поля догадками.
- **При экспорте сообщается, что файл уже существует:** параметр `-NoClobber` защитил предыдущий отчет. Выберите новое имя файла или папку и запустите команду повторно.
- **Количество отличается от ожиданий:** проверьте, не находятся ли пользователи или компьютеры в другой OU, не менялась ли область и не изменился ли каталог во время запроса.

## Дальнейшие шаги

Храните исходные CSV-файлы в защищенном месте в течение согласованного периода проверки. Передавайте только те поля, которые нужны проверяющему. После подтверждения результатов владельцами планируйте изменения по обычной процедуре утверждения и отката. После утвержденных изменений повторите ту же инвентаризацию с прежней областью, чтобы подтвердить результат.