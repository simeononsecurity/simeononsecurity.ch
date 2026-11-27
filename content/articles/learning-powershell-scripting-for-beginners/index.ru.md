---
title: "Сценарии PowerShell"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "Изучите основы сценариев PowerShell и автоматизируйте задачи с помощью этого пошагового руководства для начинающих: в нем рассматриваются командлеты, циклы, функции и многое другое."
genre: ["Технологии", "Программирование", "Автоматизация", "Windows", "Сценарии", "ИТ", "Административные задачи", "Управление компьютерами", "Разработка программного обеспечения", "Написание кода"]
tags: ["сценарии PowerShell", "автоматизация PowerShell", "сценарии Windows", "командлеты PowerShell", "модули PowerShell", "циклы PowerShell", "условные операторы PowerShell", "функции PowerShell", "рекомендации по PowerShell", "отладка PowerShell", "тестирование PowerShell", "переменные PowerShell", "PowerShell ISE", "PowerShell Remoting", "технологии Microsoft", "автоматизация ИТ", "управление компьютерами", "программирование для начинающих", "административные задачи", "идеи сценариев PowerShell", "автоматическое резервное копирование", "управление файлами", "сведения о системе", "управление пользователями", "установка программ", "настройка сети", "автоматизация безопасности", "планирование задач", "изменение реестра", "удаленное администрирование"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "Мультяшный персонаж держит сценарий перед компьютером с командной строкой PowerShell, показывая, что начинающим легко освоить написание сценариев PowerShell"
coverCaption: ""
---
**Сценарии PowerShell для начинающих**

PowerShell — это командная оболочка и язык сценариев, разработанные Microsoft. В нем есть множество команд и функций для управления различными аспектами Windows и других технологий Microsoft и их автоматизации. В этой статье мы рассмотрим основы сценариев PowerShell и дадим пошаговые инструкции для начала работы.

## Введение в PowerShell

**PowerShell** — командная оболочка, с помощью которой можно автоматизировать и управлять Windows и другими технологиями Microsoft. Она предоставляет обширный набор команд и функций для выполнения административных задач, например управления файлами и каталогами, настройки сети и администрирования системы. В PowerShell также есть язык сценариев для создания сложных сценариев и автоматизации повторяющихся задач.

## Начало работы с PowerShell

### Установка PowerShell

PowerShell предустановлен в большинстве версий Windows. Если у вас старая версия Windows или вам нужна более новая версия PowerShell, скачайте ее с сайта Microsoft. Чтобы скачать и установить PowerShell, выполните следующие действия:

1. Перейдите на [сайт Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) и выберите нужную версию.
2. Скачайте и запустите установочный файл.
3. Следуйте инструкциям на экране, чтобы завершить установку.

### Запуск PowerShell

После установки PowerShell запустите его так:

1. Откройте меню «Пуск» и введите «PowerShell» в строку поиска.
2. Выберите «Windows PowerShell» в результатах поиска.
3. PowerShell откроется в новом окне.

### Сценарии PowerShell в Visual Studio Code

Для более удобной работы со сценариями можно использовать популярную интегрированную среду разработки Visual Studio Code (VS Code). VS Code поддерживает подсветку синтаксиса, автодополнение кода, отладку и встроенный терминал, поэтому подходит для написания сценариев PowerShell. Чтобы начать работу в VS Code:

1. Установите Visual Studio Code с [официального сайта](https://code.visualstudio.com/).
2. В магазине расширений VS Code установите расширение «PowerShell» от Microsoft.
3. Откройте в VS Code файл сценария PowerShell (.ps1) и приступайте к работе.

### PowerShell для системного администрирования

PowerShell — универсальный инструмент для системного администрирования. Он упрощает задачи, которые иначе пришлось бы выполнять вручную: от коротких команд до сложных процессов автоматизации. Единая платформа для Windows, Linux и macOS дает администраторам согласованный набор инструментов для управления разными средами.

### Переход от командной строки к Windows PowerShell

Если вы знакомы с командной строкой и хотите перейти на Windows PowerShell, освоение может пройти легко. Сценарии Windows PowerShell опираются на понятия командной строки и добавляют более широкие возможности. Используйте уже имеющиеся знания и постепенно изучайте дополнительные функции и командлеты PowerShell.

### Основы PowerShell

PowerShell предоставляет интерфейс командной строки для взаимодействия с операционной системой. Команды в PowerShell называются командлетами и объединяются в модули. Чтобы просмотреть список модулей, используйте команду Get-Module:

```powershell
Get-Module
```

Чтобы просмотреть командлеты в модуле, используйте Get-Command:
```powershell
Get-Command -Module <module name>
```

Чтобы получить справку по командлету, используйте Get-Help:
```powershell
Get-Help <cmdlet name>
```

PowerShell также поддерживает псевдонимы — короткие имена командлетов. Чтобы просмотреть их список, используйте Get-Alias:
```powershell
Get-Alias
```

## Файлы сценариев и политика выполнения

Файлы сценариев PowerShell имеют расширение .ps1. Перед запуском сценариев может потребоваться настроить политику выполнения. Она определяет, можно ли запускать сценарии и какие их типы разрешены. Для настройки используйте командлет Set-ExecutionPolicy. Например, чтобы разрешить запуск сценариев:

```powershell
Set-ExecutionPolicy RemoteSigned
```

или (только для тестирования)

```powershell
Set-ExecutionPolicy Undefined
```

### Написание сценариев PowerShell

Сценарии PowerShell позволяют автоматизировать различные административные задачи. PowerShell поддерживает переменные, циклы, условные операторы и функции, поэтому подходит для автоматизации.

#### Переменные

Переменные хранят данные в сценариях PowerShell. Их имена начинаются со знака доллара ($). Чтобы присвоить переменной значение, используйте следующий синтаксис:
```powershell
$variable_name = value
```
Например:
```powershell
$name = "John"
```
#### Циклы

Циклы повторяют блок кода заданное число раз. PowerShell поддерживает следующие типы циклов:

- **Цикл For**: повторяет блок кода заданное число раз.
- **Цикл While**: повторяет блок, пока условие истинно.
- **Цикл Do-While**: выполняет блок как минимум один раз, затем повторяет его, пока условие истинно.
- **Цикл ForEach**: повторяет блок для каждого элемента коллекции.

Например, следующий код с помощью цикла For выводит числа от 1 до 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Условные операторы

Условные операторы

Условные операторы выполняют блок кода, если заданное условие истинно. PowerShell поддерживает следующие типы:

- **Оператор If**: выполняет блок, если условие истинно.
- **Оператор If-Else**: выполняет один блок, если условие истинно, и другой, если оно ложно.
- **Оператор Switch**: сравнивает значение с набором возможных вариантов и выполняет блок для первого совпадения.

Например, следующий код с помощью If проверяет, больше ли число 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "Число больше 5"
}
```
#### Функции

Функции — повторно используемые блоки кода для выполнения определенной задачи. Они принимают входные параметры и возвращают значения. PowerShell поддерживает следующие типы функций:

- **Блок сценария**: блок кода, который можно выполнить.
- **Расширенная функция**: функция с метаданными и проверкой параметров.

Например, следующий код определяет функцию для сложения двух чисел:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "Результат: $result"
```
### PowerShell ISE

PowerShell ISE (интегрированная среда сценариев) — графический интерфейс для написания сценариев PowerShell. В нем есть текстовый редактор, средства отладки и другие функции, упрощающие написание и тестирование сценариев. Чтобы открыть PowerShell ISE:

1. Откройте меню «Пуск» и введите «PowerShell ISE» в строку поиска.
2. Выберите «Windows PowerShell ISE» в результатах поиска.
3. PowerShell ISE откроется в новом окне.

### PowerShell Remoting

PowerShell Remoting позволяет запускать команды и сценарии PowerShell на удаленных компьютерах. Служба WinRM должна работать и на локальном, и на удаленном компьютере. Чтобы включить PowerShell Remoting:

1. Откройте командную строку PowerShell с правами администратора.
2. Выполните команду для включения PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. Выполните команду, чтобы добавить удаленный компьютер в список TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Перезапустите службу WinRM.
```powershell
Restart-Service WinRM
```

Чтобы выполнить команду PowerShell на удаленном компьютере, используйте командлет Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Модули PowerShell

Модули PowerShell — коллекции командлетов, функций и сценариев для определенных задач. Их можно устанавливать и администрировать через PowerShell Gallery — центральный репозиторий модулей PowerShell.

Чтобы установить модуль из PowerShell Gallery, используйте:
```powershell
Install-Module <module name>
```

Чтобы просмотреть установленные модули PowerShell, используйте Get-InstalledModule:
```powershell
Get-InstalledModule
```

### Рекомендации по написанию сценариев PowerShell

При написании **сценариев PowerShell** следуйте рекомендациям, чтобы они были **безопасными**, **надежными** и **удобными в сопровождении**. Вот несколько советов:

- **Выбирайте понятные имена переменных**: указывайте в именах назначение переменных.
- **Добавляйте комментарии**: поясняйте назначение кода.
- **Обрабатывайте ошибки**: корректно работайте с ошибками и исключениями. Конструкция `Try...Catch...Finally` в PowerShell позволяет перехватывать исключения и выполнять нужные действия. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Тщательно тестируйте сценарии**: проверяйте, что они работают как ожидается. Для написания и запуска модульных тестов можно использовать **Pester**, платформу тестирования PowerShell. [Документация Pester](https://pester.dev/)
- **Используйте функции и модули**: организуйте код и повышайте его повторное использование. Функции делят код на небольшие управляемые части, а модули позволяют упаковывать и распространять его. [О функциях](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [О модулях](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Не задавайте значения непосредственно в коде**: вместо этого используйте параметры или переменные. Так сценарии будут гибче и пригоднее для повторного использования. Передавайте параметры с помощью ключевого слова `param`. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Используйте подробный вывод**: показывайте дополнительные сведения о ходе выполнения сценария. Для вывода подробных сообщений используйте командлет `Write-Verbose`. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### Подробное описание рекомендаций для сценариев PowerShell

#### Обрабатывайте ошибки

Обработка ошибок важна, поскольку помогает сценариям PowerShell корректно работать с ошибками и исключениями. PowerShell предлагает несколько способов: операторы Try-Catch и Trap, а также параметр ErrorAction. Try-Catch перехватывает и обрабатывает исключения, Trap перехватывает и обрабатывает ошибки, а ErrorAction управляет реакцией сценария на ошибки.

Пример использования Try-Catch для обработки ошибки:
```powershell
try {
    # код, который может вызвать ошибку
}
catch {
    Write-Error "Произошла ошибка: $_"
}
```

#### Тщательно тестируйте сценарии

Тестирование сценариев PowerShell помогает убедиться, что они работают как ожидается. Такие средства и платформы, как Pester, позволяют писать и запускать тесты. Они помогают находить и изолировать проблемы в коде, а также проверять соответствие сценария требованиям.

Пример тестирования сценария PowerShell с помощью Pester:
```powershell
Describe "Мой сценарий PowerShell" {
    It "Выполняет задачу" {
        # код, который должен вернуть ожидаемый результат
        $result = Do-Something
        $result | Should -Be "ожидаемый результат"
    }
}
```

#### Используйте функции и модули

Функции и модули помогают организовать код и повторно использовать его. Функции объединяют код в повторно используемые блоки, а модули позволяют упаковывать и предоставлять код другим. Благодаря им сценарии становятся модульными, эффективными и удобными в сопровождении.

Пример функции PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "Запущено процессов: $count"
```

#### Не задавайте значения непосредственно в коде

Жестко заданные значения снижают гибкость сценария PowerShell и усложняют его сопровождение. Вместо этого используйте параметры или переменные, чтобы пользователь мог задавать значения во время выполнения. Так сценарий легче повторно использовать и адаптировать.

Пример параметра PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Здравствуйте, $name!"
```

#### Используйте подробный вывод

Подробный вывод предоставляет дополнительные сведения о ходе выполнения сценария и помогает при отладке и устранении неполадок. Командлет Write-Verbose выводит такие сведения в консоль, упрощая понимание и отладку сценариев.

Пример подробного вывода в PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Получаем список процессов..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "Запущено процессов: $count"
```

### Десять идей сценариев PowerShell для начинающих

Если вы только начинаете писать сценарии PowerShell, попробуйте эти десять идей:

- **Автоматическое резервное копирование**: создайте сценарий для копирования важных файлов и каталогов на внешний жесткий диск или в облачное хранилище. Для копирования используйте `Copy-Item`, а для запуска резервного копирования в фоновом режиме — `Start-Job`. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Управление файлами**: создайте сценарий, который сортирует файлы и каталоги по папкам в зависимости от типа, размера или других условий. Используйте `Get-ChildItem` для поиска файлов и `Move-Item` для перемещения в нужное место. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Сведения о системе**: создайте сценарий для сбора данных об использовании процессора и памяти, свободном месте на диске и настройках сети. Используйте `Get-WmiObject` для сбора сведений, а `Format-Table` или `Out-GridView` — для их отображения в удобном формате. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Управление пользователями**: создайте сценарий для автоматического добавления, изменения или удаления пользователей и групп Windows. Для пользователей используйте `New-LocalUser`, `Set-LocalUser` и `Remove-LocalUser`, а для групп — `New-LocalGroup`, `Add-LocalGroupMember` и `Remove-LocalGroup`. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Установка программ**: создайте сценарий для одновременной установки и настройки программ на нескольких компьютерах. Используйте `Invoke-Command` для запуска установочных команд на удаленных компьютерах. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Настройка сети**: создайте сценарий для автоматической настройки IP-адресов, масок подсети и шлюзов по умолчанию. Для настройки используйте `Set-NetIPAddress`, `Set-NetIPInterface` и `Set-DnsClientServerAddress`. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Безопасность**: создайте сценарий для аудита и мониторинга настроек безопасности с уведомлением об обнаруженных изменениях. Используйте `Get-AuditPolicy` для получения политик аудита и `Send-MailMessage` для отправки уведомлений по электронной почте. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Планирование задач**: создайте сценарий для планирования и автоматизации повторяющихся задач, например резервного копирования, обновлений и проверки системы. Используйте `Register-ScheduledTask` для создания задач и `Start-ScheduledTask` для их запуска. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Изменение реестра**: создайте сценарий для получения или изменения значений в определенных ключах реестра. Используйте `Get-ItemProperty` и `Set-ItemProperty`. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Удаленное администрирование**: создайте сценарий для удаленного администрирования компьютеров Windows, чтобы запускать команды и сценарии на удаленных машинах. Используйте `Enter-PSSession` или `Invoke-Command` для выполнения команд. [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Документация Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Начните с этих идей, чтобы получить практический опыт и расширить знания о сценариях PowerShell.

## Заключение

PowerShell — мощный инструмент для управления и автоматизации Windows и других технологий Microsoft. В этой статье мы рассмотрели основы сценариев для начинающих: установку и запуск PowerShell, командлеты, переменные, циклы, условные операторы и функции, а также PowerShell ISE, PowerShell Remoting и модули. Соблюдение рекомендаций помогает создавать безопасные, надежные и удобные в сопровождении сценарии. Практикуясь, вы освоите PowerShell и сможете легко автоматизировать различные административные задачи.
