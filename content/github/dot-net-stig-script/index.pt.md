---
title: "Automatize a conformidade do .NET STIG com o script PowerShell"
date: 2020-08-20
---
 o .NET Framework STIG

A aplicação do .NET STIG definitivamente não é simples. Para muitos administradores, pode levar horas para implementar totalmente em um único sistema. Este script aplica as alterações de registro necessárias e modifica o arquivo machine.config para implementar o FIPS e outros controles conforme necessário.

## Notas:

Este script não pode e nunca fará com que o .NET stig atinja 100% de conformidade. No momento, como está, ele deve concluir cerca de 75% das verificações e voltar e concluir as verificações aplicáveis em todas as versões anteriores do .NET.

A intervenção manual é necessária para qualquer aplicativo .NET ou site IIS.

## Requisitos:
- [X] Windows 7, Windows Server 2008 ou mais recente
- [X] Teste em seu ambiente antes de executar em sistemas de produção.

## STIGS/SRGs aplicados:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Fontes:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Baixe os arquivos necessários

Você pode baixar os arquivos necessários do[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Como executar o script

**O script pode ser iniciado a partir do download extraído do GitHub assim:**

## Como executar o script
### Instalação manual:
Se baixado manualmente, o script deve ser iniciado a partir de um powershell administrativo no diretório que contém todos os arquivos do[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Automated Install:
Use this one-liner to automatically download, unzip all supporting files, and run the latest version of the script.
```
iwr -useb 'https://simeononsecurity.com/scripts/sosdotnet.ps1'|iex
```
