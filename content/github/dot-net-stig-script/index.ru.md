---
title: "Автоматизируйте соответствие .NET STIG с помощью сценария PowerShell"
date: 2020-08-20
---
 .NET Framework STIG

Применение .NET STIG определенно не простое дело. Многим администраторам может потребоваться несколько часов для полной реализации в одной системе. Этот сценарий вносит необходимые изменения в реестр и модифицирует файл machine.config для реализации FIPS и других элементов управления по мере необходимости.

## Примечания:

Этот скрипт не может и никогда не сможет обеспечить 100% соответствие стигу .NET. Прямо сейчас, как есть, он может завершить примерно 75% проверок и вернуться и завершить соответствующие проверки для всех предыдущих версий .NET.

Ручное вмешательство требуется для любого приложения .NET или сайта IIS.

## Требования:
- [X] Windows 7, Windows Server 2008 или новее
- [X] Тестирование в вашей среде перед запуском в производственных системах.

## Применены STIGS/SRG:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Источники:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Загрузите необходимые файлы

Вы можете скачать необходимые файлы с[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Как запустить скрипт

**Скрипт можно запустить из извлеченной загрузки GitHub следующим образом:**

## Как запустить скрипт
### Ручная установка:
При ручной загрузке скрипт необходимо запускать из административной оболочки в каталоге, содержащем все файлы из[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Automated Install:
Use this one-liner to automatically download, unzip all supporting files, and run the latest version of the script.
```
iwr -useb 'https://simeononsecurity.ch/scripts/sosdotnet.ps1'|iex
```
