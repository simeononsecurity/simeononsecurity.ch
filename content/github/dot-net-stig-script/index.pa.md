---
title: "PowerShell ਸਕ੍ਰਿਪਟ ਦੇ ਨਾਲ .NET STIG ਪਾਲਣਾ ਨੂੰ ਸਵੈਚਾਲਤ ਕਰੋ"
date: 2020-08-20
---
 .NET ਫਰੇਮਵਰਕ STIG

.NET STIG ਨੂੰ ਲਾਗੂ ਕਰਨਾ ਯਕੀਨੀ ਤੌਰ 'ਤੇ ਸਿੱਧਾ ਨਹੀਂ ਹੈ। ਬਹੁਤ ਸਾਰੇ ਪ੍ਰਸ਼ਾਸਕਾਂ ਲਈ ਇੱਕ ਸਿੰਗਲ ਸਿਸਟਮ 'ਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਲਾਗੂ ਕਰਨ ਵਿੱਚ ਘੰਟੇ ਲੱਗ ਸਕਦੇ ਹਨ। ਇਹ ਸਕ੍ਰਿਪਟ ਲੋੜੀਂਦੀਆਂ ਰਜਿਸਟਰੀ ਤਬਦੀਲੀਆਂ ਨੂੰ ਲਾਗੂ ਕਰਦੀ ਹੈ ਅਤੇ ਲੋੜ ਅਨੁਸਾਰ FIPS ਅਤੇ ਹੋਰ ਨਿਯੰਤਰਣਾਂ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ machine.config ਫਾਈਲ ਨੂੰ ਸੋਧਦੀ ਹੈ।

## ਨੋਟ:

ਇਹ ਸਕ੍ਰਿਪਟ 100% ਅਨੁਪਾਲਨ ਲਈ .NET ਸਟੈਗ ਪ੍ਰਾਪਤ ਨਹੀਂ ਕਰ ਸਕਦੀ ਹੈ ਅਤੇ ਨਾ ਹੀ ਕਰੇਗੀ। ਇਸ ਸਮੇਂ, ਜਿਵੇਂ ਕਿ, ਇਹ ਲਗਭਗ 75% ਚੈਕਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਖੜ੍ਹਾ ਹੈ ਅਤੇ ਵਾਪਸ ਜਾ ਕੇ ਸਾਰੇ ਪਿਛਲੇ .NET ਸੰਸਕਰਣਾਂ 'ਤੇ ਲਾਗੂ ਜਾਂਚਾਂ ਨੂੰ ਪੂਰਾ ਕਰਦਾ ਹੈ।

ਕਿਸੇ ਵੀ .NET ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ IIS ਸਾਈਟ ਲਈ ਦਸਤੀ ਦਖਲ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

## ਲੋੜਾਂ:
- [X] ਵਿੰਡੋਜ਼ 7, ਵਿੰਡੋਜ਼ ਸਰਵਰ 2008 ਜਾਂ ਨਵਾਂ
- [X] ਉਤਪਾਦਨ ਪ੍ਰਣਾਲੀਆਂ 'ਤੇ ਚੱਲਣ ਤੋਂ ਪਹਿਲਾਂ ਤੁਹਾਡੇ ਵਾਤਾਵਰਣ ਵਿੱਚ ਟੈਸਟ ਕਰਨਾ।

## STIGS/SRGs ਲਾਗੂ:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## ਸਰੋਤ:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਉਨਲੋਡ ਕਰੋ

ਤੁਸੀਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਉਨਲੋਡ ਕਰ ਸਕਦੇ ਹੋ[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ

**ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਐਕਸਟਰੈਕਟ ਕੀਤੇ GitHub ਡਾਊਨਲੋਡ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:**

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ
### ਦਸਤੀ ਸਥਾਪਨਾ:
ਜੇਕਰ ਮੈਨੂਅਲੀ ਡਾਉਨਲੋਡ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਸਕ੍ਰਿਪਟ ਨੂੰ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ ਪ੍ਰਬੰਧਕੀ ਪਾਵਰਸ਼ੇਲ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਹਨ।[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
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
