---
title: "Automatyzacja zgodności z .NET STIG za pomocą skryptu PowerShell"
date: 2020-08-20
---
 .NET Framework STIG

Zastosowanie .NET STIG z pewnością nie jest proste. Dla wielu administratorów pełne wdrożenie na jednym systemie może zająć wiele godzin. Ten skrypt stosuje wymagane zmiany w rejestrze i modyfikuje plik machine.config, aby wdrożyć FIPS i inne kontrole zgodnie z wymaganiami.

## Uwagi:

Ten skrypt nie może i nigdy nie doprowadzi stiga .NET do 100% zgodności. W tej chwili, w obecnej postaci, jest w stanie wykonać około 75% kontroli i wraca do wszystkich poprzednich wersji .NET.

Ręczna interwencja jest wymagana dla każdej aplikacji .NET lub witryny IIS.

## Wymagania:
- [X] Windows 7, Windows Server 2008 lub nowszy
- X] Testowanie w swoim środowisku przed uruchomieniem na systemach produkcyjnych.

## STIGS/SRGs Applied:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Sources:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Pobierz wymagane pliki

Możesz pobrać wymagane pliki ze strony[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Jak uruchomić skrypt

**Skrypt można uruchomić z rozpakowanego pliku do pobrania z GitHuba w taki sposób:**.

## Jak uruchomić skrypt
### Manual Install:
W przypadku ręcznego pobrania, skrypt należy uruchomić z administracyjnego powershella w katalogu zawierającym wszystkie pliki z.[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Automatyczna instalacja:
Użyj tego one-linera, aby automatycznie pobrać, rozpakować wszystkie pliki pomocnicze i uruchomić najnowszą wersję skryptu.
```
iwr -useb 'https://simeononsecurity.com/scripts/sosdotnet.ps1'|iex
```
