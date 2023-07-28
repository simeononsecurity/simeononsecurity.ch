---
title: "Mastering Active Directory Administration with PowerShell: Руководство по установке и использованию"
date: 2023-07-25
toc: true
draft: false
description: "Узнайте, как эффективно установить и использовать модуль Active Directory для PowerShell, чтобы упростить задачи администрирования Windows Active Directory."
genre: ["Технология", "Windows", "PowerShell", "Active Directory", "Администрация", "Скриптинг", "IT", "Автоматизация", "Windows Server", "Microsoft"]
tags: ["модуль активного каталога для PowerShell", "модуль импорта active directory в PowerShell", "модуль активного каталога для Windows PowerShell", "установка Active Directory PowerShell", "установить активный каталог PowerShell", "PowerShell установка модуля активного каталога Windows 10", "установить активный каталог PowerShell-модуль Windows 10", "получить модуль PowerShell активного каталога", "Администрирование AD", "Windows Active Directory", "Команды PowerShell", "получение информации об AD", "создание объектов AD", "изменять объекты AD", "управление безопасностью AD", "Управление пользователями AD", "Управление группами AD", "Управление AD OR", "Сценарии PowerShell", "Администрирование Windows Server", "Microsoft PowerShell", "автоматизация задач AD", "Установка модуля PowerShell", "Руководство по администрированию AD", "Управление Active Directory", "Управление безопасностью AD", "Автоматизация с помощью PowerShell", "Команды Active Directory PowerShell", "Справочник команд PowerShell"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Изображение сети взаимосвязанных серверов и значков пользователей, символизирующее управление и автоматизацию Active Directory."
coverCaption: "Раскройте возможности администрирования Active Directory с помощью PowerShell."
---

## Введение

В условиях современной цифровой среды управление и поддержка учетных записей пользователей, групп безопасности и других ресурсов в среде Windows Active Directory (AD) требует эффективных и рациональных процессов. PowerShell, мощный язык сценариев, разработанный компанией Microsoft, предлагает модуль **Active Directory** для облегчения задач администрирования AD. Этот модуль предоставляет широкий набор команд, позволяющих администраторам автоматизировать различные операции и эффективно управлять AD. В этой статье мы рассмотрим установку и использование модуля Active Directory для PowerShell.

## Установка модуля Active Directory для PowerShell

Чтобы начать использовать модуль Active Directory для PowerShell, необходимо убедиться, что он установлен на вашей системе. Процесс установки может отличаться в зависимости от операционной системы. Ниже описаны шаги по установке модуля на **Windows 10**, **Windows 11** и **Windows Server**:

### Windows 10 и Windows 11 - PowerShell
1. Откройте **Windows PowerShell** с правами администратора.
2. Выполните следующую команду для установки модуля:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Дождитесь завершения установки. После завершения установки можно приступать к использованию модуля Active Directory.

### Windows Server
1. Откройте **Windows PowerShell** с правами администратора.
2. Выполните следующую команду для установки модуля:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Дождитесь завершения установки. После завершения установки можно приступать к использованию модуля Active Directory.

### Автономные системы

С автономными системами дело обстоит несколько сложнее. Существует несколько способов, однако мы рекомендуем использовать следующий сценарий:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Импорт модуля Active Directory в PowerShell

Прежде чем использовать модуль Active Directory в PowerShell, необходимо импортировать его в текущую сессию. Для импорта модуля выполните следующие действия:

1. Запустите **Windows PowerShell** с правами администратора.
2. Выполните следующую команду для импорта модуля:

```powershell
Import-Module ActiveDirectory
```

3. Модуль Active Directory будет импортирован, и теперь вы можете получить доступ к его командам и функциям.

## Использование модуля Active Directory для PowerShell

Импортировав модуль Active Directory, можно использовать богатый набор команд для выполнения различных административных задач. Давайте рассмотрим некоторые часто используемые команды и их функциональные возможности:

### Получение информации о Active Directory

Для эффективного управления средой Active Directory (AD) очень важно получать информацию о различных объектах AD, таких как пользователи, группы и организационные единицы (OU). PowerShell предоставляет мощные команды, которые упрощают процесс получения информации.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) Эта команда позволяет получить подробную информацию о пользователях AD. Вы можете получить такие атрибуты, как имя пользователя, отображаемое имя, адрес электронной почты и т.д. Например, для получения всех пользователей, чьи имена начинаются с "johndoe", можно выполнить следующую команду:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Эта команда вернет список пользовательских объектов, соответствующих указанному фильтру.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) С помощью команды Get-ADGroup можно получить информацию о группах AD. Она предоставляет доступ к таким сведениям, как имя группы, ее члены, описание и т.д. Например, чтобы получить все группы безопасности в среде AD, можно выполнить следующую команду:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  В результате будет получен список групп безопасности в Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) Команда Get-ADOrganizationalUnit используется для получения информации об OU AD. Она позволяет получить доступ к таким свойствам, как имя OU, описание, родительская OU и т.д. Чтобы получить все OU в домене, можно воспользоваться следующей командой:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Выполнение этой команды выводит список всех OU в Active Directory.

Используя эти мощные команды, вы можете легко получить конкретную информацию о пользователях, группах и OUs AD, что позволяет эффективно администрировать и управлять средой Active Directory.

{{< inarticle-dark >}}


Эти команды позволяют получать определенные атрибуты, фильтровать результаты и выполнять расширенные запросы для получения нужной информации.

### Создание и управление объектами Active Directory

При работе с Active Directory (AD) модуль Active Directory в PowerShell предлагает мощные команды для создания и управления объектами AD. Рассмотрим некоторые важные команды для создания пользователей, групп и организационных единиц (OU) AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) Эта команда позволяет создать нового пользователя AD. Вы можете указать такие атрибуты, как имя пользователя, пароль, адрес электронной почты и т.д. Например, для создания нового пользователя с именем пользователя "john.doe" и отображаемым именем "John Doe" можно использовать следующую команду:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Эта команда создаст нового пользователя в Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) Команда New-ADGroup позволяет создать новую группу AD. При этом можно задать такие свойства, как имя группы, описание, область действия группы и т.д. Чтобы создать новую группу с именем "Маркетинг" и описанием, можно выполнить следующую команду:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Эта команда создаст новую группу в Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) С помощью команды New-ADOrganizationalUnit можно создать новое подразделение AD OU. При этом можно указать такие свойства, как имя OU, родительское OU и т.д. Например, чтобы создать новую OU с именем "Sales" в OU "Departments", можно выполнить следующую команду:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Эта команда создаст новую OU в иерархии Active Directory.

Используя эти команды, можно легко создавать новых пользователей, группы и OU AD с необходимыми свойствами и конфигурациями, что позволяет эффективно управлять средой Active Directory.

{{< inarticle-dark >}}


### Изменение объектов Active Directory

Когда необходимо изменить свойства и атрибуты существующих объектов Active Directory (AD), модуль Active Directory в PowerShell предоставляет несколько полезных команд. Давайте рассмотрим эти команды для изменения пользователей, групп и организационных единиц (OU) AD.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) Команда Set-ADUser позволяет изменять свойства пользователя AD. Можно обновить такие атрибуты, как отображаемое имя, адрес электронной почты, номер телефона и т.д. Например, чтобы изменить номер телефона пользователя с именем "john.doe", можно воспользоваться следующей командой:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Эта команда изменит телефонный номер указанного пользователя в Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) С помощью команды Set-ADGroup можно изменять свойства группы AD. Можно обновить такие атрибуты, как описание группы, членство в ней, область действия группы и т.д. Чтобы изменить описание группы с именем "Marketing" на "Marketing Team", можно выполнить следующую команду:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Эта команда обновляет описание указанной группы в Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) Команда Set-ADOrganizationalUnit позволяет изменять свойства AD OU. Можно изменить такие атрибуты, как имя OU, описание и т.д. Например, чтобы изменить описание OU с именем "Sales" на "Sales Department", можно выполнить следующую команду:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Эта команда обновляет описание указанного OU в иерархии Active Directory.

Используя эти команды, вы можете легко изменять свойства и атрибуты объектов AD, внося необходимые обновления и корректировки в соответствии с требованиями вашей организации.

{{< inarticle-dark >}}


### Управление безопасностью Active Directory

Помимо управления и администрирования объектов Active Directory (AD), модуль Active Directory в PowerShell содержит команды, специально разработанные для работы с аспектами безопасности AD. Эти команды позволяют администраторам эффективно управлять доступом пользователей, членством в группах и задачами, связанными с паролями, в среде AD.

Ниже приведены некоторые часто используемые команды, связанные с безопасностью:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) Эта команда позволяет добавить членов в группу AD. Указав группу AD и учетные записи пользователей или группы, которые необходимо добавить, можно легко управлять контролем доступа. Например, чтобы добавить пользователя с именем "JohnDoe" в группу "Managers", можно воспользоваться следующей командой:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) С помощью этой команды можно удалить членов группы AD. Указав группу AD и учетные записи пользователей или группы, которые необходимо удалить, можно эффективно управлять членством в группах. Например, чтобы удалить пользователя с именем "JaneSmith" из группы "Developers", можно воспользоваться следующей командой:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) Эта команда позволяет задать пароль для пользователя AD. Указав учетную запись пользователя и задав новый пароль, можно обеспечить соблюдение политик паролей и надежную аутентификацию пользователей. Ниже приведен пример установки нового пароля для пользователя с именем "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Используя эти команды, связанные с безопасностью, администраторы могут эффективно управлять доступом пользователей, членством в группах и политиками паролей в среде Active Directory.

## Пример сценария модуля Active Directory для PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Заключение

В заключение следует отметить, что модуль **Active Directory для PowerShell** - это мощный инструмент, позволяющий эффективно и удобно управлять Windows Active Directory. Установив и импортировав модуль, вы получаете доступ к обширному набору **компонентов**, упрощающих выполнение различных задач, связанных с AD.

С помощью модуля Active Directory можно выполнять широкий спектр операций, таких как получение информации об объектах AD, создание новых объектов, изменение свойств и управление безопасностью. Этот модуль позволяет администраторам автоматизировать административные задачи, оптимизировать рабочие процессы и обеспечить бесперебойное функционирование среды Active Directory.

Используя **PowerShell** и модуль **Active Directory**, вы сможете расширить свои возможности по администрированию AD и повысить эффективность процессов управления AD. Независимо от того, являетесь ли вы системным администратором, ИТ-специалистом или менеджером Active Directory, модуль Active Directory предоставляет вам необходимые инструменты для эффективного управления инфраструктурой AD.

Воспользуйтесь возможностями **PowerShell** и модуля **Active Directory**, чтобы упростить задачи администрирования AD, повысить производительность и поддерживать безопасную и хорошо организованную среду Active Directory.

{{< inarticle-dark >}}

## Ссылки

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
