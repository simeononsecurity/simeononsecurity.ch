---
title: "Повышение безопасности системы с помощью команд Windows Defender PowerShell"
date: 2023-07-27
toc: true
draft: false
description: "Откройте для себя возможности команд Windows Defender PowerShell и узнайте, как повысить безопасность системы с помощью управления из командной строки."
genre: ["Защитник Windows", "Команды PowerShell", "безопасность системы", "управление из командной строки", "антивирус", "Операционные системы Windows", "защита от вредоносного ПО", "расширенные настройки безопасности", "автоматизация операций по обеспечению безопасности", "Windows PowerShell"]
tags: ["Технология", "Кибербезопасность", "Операционные системы", "Windows", "Средства командной строки", "Безопасность системы", "PowerShell", "Антивирус", "Защита от вредоносного ПО", "Скриптинг"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "Анимационная иллюстрация, изображающая щит, защищающий компьютерную систему от различных киберугроз."
coverCaption: "Повышение уровня безопасности системы с помощью команд Windows Defender PowerShell."
---

## Введение

Windows Defender, разработанный компанией Microsoft, представляет собой интегрированное антивирусное и защитное решение для операционных систем Windows. Он предлагает удобный интерфейс для эффективного управления настройками безопасности. Однако для опытных пользователей, предпочитающих управление из командной строки, Windows Defender предоставляет набор мощных команд PowerShell. В этой статье мы погрузимся в мир **команд Windows Defender PowerShell** и рассмотрим, как с их помощью можно повысить безопасность системы и обеспечить больший контроль над средой Windows.

## Возможности команд Windows Defender PowerShell

Команды Windows Defender PowerShell предоставляют пользователям возможность выполнять расширенные операции по обеспечению безопасности с помощью интерфейса командной строки. Эти команды предоставляют широкий спектр возможностей - от простых операций, таких как сканирование на наличие вредоносных программ, до сложных задач, таких как настройка дополнительных параметров безопасности. Используя PowerShell, пользователи могут автоматизировать операции безопасности, создавать пользовательские сценарии и легко интегрировать Windows Defender в существующие рабочие процессы.

## Начало работы с Windows Defender PowerShell

Чтобы получить доступ к командам Windows Defender PowerShell, необходимо открыть сеанс PowerShell с правами администратора. Вот как можно приступить к работе:

1. Нажмите `Win + X` и выберите в меню пункт **Windows PowerShell (Admin)**.
2. При появлении запроса нажмите **Да**, чтобы разрешить приложению вносить изменения в устройство.

После открытия сеанса PowerShell можно приступить к использованию команд Windows Defender PowerShell.

## Общие команды Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: Проверка состояния Защитника Windows

Сайт `Get-MpComputerStatus` Команда предоставляет обзор текущего состояния Windows Defender в системе, включая версию антивирусного движка, время последнего сканирования и состояние защиты в реальном времени. Выполнив эту команду, можно быстро оценить общее состояние Windows Defender и убедиться в его оптимальном функционировании.

Чтобы проверить состояние Windows Defender, откройте сеанс PowerShell с правами администратора и выполните следующую команду:

```powershell
Get-MpComputerStatus
```

Эта команда отобразит такую информацию, как:

- **AntivirusEngineVersion**: Номер версии антивирусного движка, используемого Windows Defender.
- **LastFullScanTime**: Дата и время последнего полного сканирования, выполненного Windows Defender.
- **LastQuickScanTime**: Дата и время последнего быстрого сканирования, выполненного Windows Defender.
- **RealTimeProtectionEnabled**: Указывает, включена или отключена защита в реальном времени.

Регулярный мониторинг состояния Защитника Windows с помощью `Get-MpComputerStatus` позволяет всегда быть в курсе уровня защиты системы от потенциальных угроз.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Сайт `Update-MpSignature` Команда позволяет вручную обновить антивирусные сигнатуры, используемые Защитником Windows. Антивирусные сигнатуры содержат важную информацию об известных вредоносных программах, что позволяет Защитнику Windows эффективно обнаруживать и блокировать угрозы. Выполнив эту команду, можно убедиться, что в системе установлены самые последние сигнатуры, обеспечивающие повышенную защиту от возникающих угроз.

Чтобы вручную обновить сигнатуры Windows Defender, откройте сеанс PowerShell с правами администратора и выполните следующую команду:

```powershell
Update-MpSignature
```
Эта команда запускает процесс обновления, в ходе которого **Windows Defender** подключается к **серверам Microsoft** для загрузки последних **антивирусных сигнатур**. После завершения обновления Защитник Windows будет располагать самой актуальной информацией об известных вредоносных программах, что повысит его способность выявлять и устранять угрозы.

Поддержание сигнатур Windows Defender в актуальном состоянии необходимо для обеспечения высокого уровня защиты от постоянно развивающегося спектра **вредоносных программ** и **киберугроз**. Регулярное обновление сигнатур с помощью `Update-MpSignature` вы убедитесь, что Windows Defender может эффективно защищать вашу систему.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Сайт `Set-MpPreference` Команда позволяет настраивать различные параметры **Windows Defender**, что позволяет адаптировать его поведение к конкретным требованиям безопасности. Эта команда обеспечивает гибкость при настройке таких параметров, как **защита в реальном времени**, **защита на основе облачных технологий** и **настройки системы сетевого контроля**.

Например, можно включить или отключить защиту в реальном времени с помощью команды `Set-MpPreference` команда. Защита в реальном времени активно отслеживает вредоносную активность системы и обеспечивает немедленное реагирование на угрозы. Чтобы включить защиту в реальном времени, выполните следующую команду:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Кроме того, с помощью этой команды можно настроить параметры облачной защиты. Облачная защита использует ресурсы "облака" для повышения эффективности обнаружения угроз и ускорения реакции на возникающие угрозы. Чтобы включить облачную защиту, выполните следующую команду:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Кроме того `Set-MpPreference` Команда позволяет настроить параметры системы сетевого контроля. Система сетевого контроля анализирует сетевой трафик на предмет подозрительной активности и потенциальных угроз. Для настройки параметров системы сетевого контроля выполните следующую команду:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Точная настройка этих параметров с помощью `Set-MpPreference` вы можете оптимизировать **Windows Defender** в соответствии с вашими конкретными потребностями в области безопасности и обеспечить надежную защиту от вредоносных программ и других вредоносных действий.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Сайт `Start-MpScan` является мощным инструментом для инициирования сканирования системы на наличие вредоносных программ, позволяющим проактивно выявлять и удалять вредоносные файлы. Эта команда обеспечивает гибкость при выполнении различных типов сканирования, включая **быстрое сканирование**, **полное сканирование** и **заказное сканирование** по определенным путям.

Чтобы выполнить **быстрое сканирование** с помощью команды `Start-MpScan` выполните следующую команду PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

Быстрое сканирование фокусируется на критических областях системы, где обычно обнаруживается вредоносное ПО, и позволяет оперативно оценить потенциальные угрозы.

Для более полного сканирования с проверкой всех файлов и каталогов системы можно запустить **полное сканирование**. Для выполнения полного сканирования выполните следующую команду `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

Полное сканирование обеспечивает тщательное обнаружение и удаление вредоносных программ из системы, однако его выполнение может занять больше времени по сравнению с быстрым сканированием.

В дополнение к предопределенным типам сканирования можно выбрать `Start-MpScan` Команда позволяет выполнять пользовательское сканирование, указывая конкретные пути или файлы для сканирования. Например, с помощью следующей команды можно просканировать определенный каталог в системе:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Эта команда инициирует пользовательское сканирование указанного каталога, позволяя нацелить определенные области системы на обнаружение вредоносного ПО.

Используя универсальные возможности команды `Start-MpScan` Команда позволяет планировать сканирование, автоматизировать процессы защиты и обеспечивать регулярное обнаружение и уничтожение вредоносных программ в системе.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Сайт `Get-MpThreatCatalog` команда является ценным ресурсом для получения подробной информации об известных угрозах и их атрибутах. Выполнив эту команду, можно получить доступ к полному каталогу угроз, включая данные об их серьезности, именах соответствующих файлов и рекомендуемые действия по их устранению.

Чтобы получить информацию о конкретных угрозах с помощью команды `Get-MpThreatCatalog` выполните следующие действия:

1. Откройте сеанс PowerShell с правами администратора.
2. Выполните следующую команду:

```powershell
   Get-MpThreatCatalog
```
Эта команда выводит список известных угроз с соответствующими сведениями о них.

Вывод `Get-MpThreatCatalog` команда включает в себя такую важную информацию, как:

- **ThreatID**: Уникальный идентификатор угрозы.
- **Severity**: Указывает уровень серьезности угрозы, от Low до Severe.
- **Name**: Название или описание угрозы.
- **Path**: Путь к файлу, связанному с угрозой.
- **RecommendedAction**: Содержит указания по рекомендуемым действиям для устранения угрозы.

Используя информацию, полученную из `Get-MpThreatCatalog` Вы можете получить ценные сведения о потенциальных угрозах и принять обоснованные решения о необходимых действиях по их устранению. Будь то изоляция, устранение или мониторинг конкретной угрозы, подробный каталог позволяет эффективно реагировать на инциденты безопасности.

Для получения дополнительной информации об использовании `Get-MpThreatCatalog` и интерпретации его результатов, обратитесь к официальной документации Microsoft.

Не теряйте бдительности и регулярно пользуйтесь программой `Get-MpThreatCatalog` команда, чтобы быть в курсе эволюции угроз и повысить безопасность своей системы.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Сайт `Add-MpPreference` Команда позволяет добавлять исключения в Windows Defender, что дает возможность настраивать поведение сканирования и защиты в реальном времени. Добавляя исключения, можно указать файлы, папки или процессы, которые Windows Defender должен игнорировать при сканировании или защите в реальном времени.

Чтобы добавить исключение с помощью `Add-MpPreference` необходимо указать путь или имя файла, папки или процесса, который нужно исключить. Вот пример добавления исключения для папки:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Эта команда обеспечивает пропуск сканирования указанной папки защитником Windows, уменьшая количество ненужных предупреждений и потенциальных прерываний рабочего процесса.

Исключения могут быть полезны в различных сценариях, например, для исключения доверенных приложений, сред разработки или определенных файлов, которые могут вызывать ложные срабатывания. Используя гибкие возможности `Add-MpPreference` вы можете точно настроить Защитник Windows в соответствии с вашими специфическими потребностями в области безопасности и оптимизировать его работу.

Эффективно защищать систему, сводя к минимуму количество ложных срабатываний и ненужных прерываний сканирования, можно с помощью мощных возможностей исключения, предоставляемых `Add-MpPreference`

## Заключение

Команды Windows Defender PowerShell представляют собой **надежный набор инструментов** для управления и повышения уровня безопасности системы Windows. Используя эти команды, можно *автоматизировать операции безопасности*, *конфигурировать расширенные параметры* и органично вписать Windows Defender в рабочие процессы. Независимо от того, являетесь ли вы **системным администратором** или **простым пользователем**, изучение возможностей команд Windows Defender PowerShell может значительно повысить уровень безопасности вашей системы.

Помните, что с большой силой приходит и большая ответственность. При использовании команд PowerShell следует соблюдать осторожность и убедиться в том, что вы понимаете их последствия, прежде чем выполнять их. Сочетание знаний и возможностей команд Windows Defender PowerShell позволит принять проактивные меры для защиты системы от новых угроз.

## Ссылки

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
