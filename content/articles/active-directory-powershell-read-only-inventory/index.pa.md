---
title: "PowerShell ਨਾਲ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੀ Active Directory ਸੂਚੀ ਬਣਾਓ"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "ਸੀਮਿਤ PowerShell ਪੁੱਛਗਿੱਛਾਂ ਨਾਲ Active Directory ਦੀਆਂ ਸੰਗਠਨਾਤਮਕ ਇਕਾਈਆਂ, ਵਰਤੋਂਕਾਰਾਂ ਅਤੇ ਕੰਪਿਊਟਰਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ। ਡਾਇਰੈਕਟਰੀ ਵਸਤੂਆਂ ਬਦਲੇ ਬਿਨਾਂ ਜਾਂਚਯੋਗ CSV ਫ਼ਾਈਲਾਂ ਨਿਰਯਾਤ ਕਰੋ।"
genre: ["Active Directory", "PowerShell", "ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ"]
tags: ["Active Directory ਸੂਚੀ", "PowerShell AD ਸੂਚੀ", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲਾ AD", "AD ਵਰਤੋਂਕਾਰ ਨਿਰਯਾਤ", "AD ਕੰਪਿਊਟਰ ਨਿਰਯਾਤ", "AD OU ਨਿਰਯਾਤ", "Export-Csv", "RSAT", "ਡਾਇਰੈਕਟਰੀ ਜਾਂਚ", "AD ਰਿਪੋਰਟਾਂ", "OU ਸੂਚੀ", "Windows Server", "PowerShell ਲਿਖਤ", "AD ਮੋਡੀਊਲ", "ਡਾਇਰੈਕਟਰੀ ਸਫ਼ਾਈ"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Active Directory ਦੇ ਰੁੱਖ ਤੋਂ ਵਰਤੋਂਕਾਰਾਂ, ਕੰਪਿਊਟਰਾਂ ਅਤੇ ਸੰਗਠਨਾਤਮਕ ਇਕਾਈਆਂ ਦੇ ਰਿਕਾਰਡ ਤਿੰਨ ਜਾਂਚ ਫ਼ਾਈਲਾਂ ਵੱਲ ਜਾਂਦੇ ਦਿਖਾਏ ਗਏ ਹਨ।"
coverCaption: "ਪੁੱਛਗਿੱਛ ਦਾ ਦਾਇਰਾ ਸੀਮਿਤ ਕਰੋ ਅਤੇ ਜਾਂਚ ਲਈ ਲੋੜੀਂਦੇ ਖੇਤਰ ਹੀ ਨਿਰਯਾਤ ਕਰੋ।"
---
Active Directory ਦੀ ਸਫ਼ਾਈ ਮੌਜੂਦਾ ਵਸਤੂਆਂ ਦੀ ਭਰੋਸੇਯੋਗ ਸੂਚੀ ਨਾਲ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ। ਇਹ **ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੀ ਸੂਚੀ** ਚੁਣੇ ਦਾਇਰੇ ਵਿੱਚ ਸੰਗਠਨਾਤਮਕ ਇਕਾਈਆਂ, ਵਰਤੋਂਕਾਰਾਂ ਅਤੇ ਕੰਪਿਊਟਰਾਂ ਦਾ ਵੇਰਵਾ ਇਕੱਠਾ ਕਰਦੀ ਹੈ। ਇਹ ਡਾਇਰੈਕਟਰੀ ਵਸਤੂਆਂ ਬਦਲੇ ਬਿਨਾਂ ਜਾਂਚ ਲਈ ਤਿੰਨ CSV (ਕੌਮੇ ਨਾਲ ਵੱਖ ਕੀਤੀਆਂ ਕਦਰਾਂ) ਫ਼ਾਈਲਾਂ ਨਿਰਯਾਤ ਕਰਦੀ ਹੈ। ਇਹ ਫ਼ਾਈਲਾਂ ਵੀ ਸੁਰੱਖਿਅਤ ਰੱਖੋ, ਕਿਉਂਕਿ ਨਾਂ ਅਤੇ ਜੰਤਰਾਂ ਦੇ ਵੇਰਵੇ ਤੁਹਾਡੇ ਮਾਹੌਲ ਦਾ ਕੁਝ ਹਿੱਸਾ ਦੱਸਦੇ ਹਨ।

<!--more-->

## ਮੁੱਖ ਗੱਲਾਂ

- **ਦਾਇਰਾ ਚੁਣੋ:** ਪੂਰੇ ਡੋਮੇਨ ਤੱਕ ਵਧਣ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਸੰਗਠਨਾਤਮਕ ਇਕਾਈ ਲਈ ਪੁੱਛਗਿੱਛ ਕਰੋ।
- **ਪੜ੍ਹਨ ਵਾਲੇ ਹੁਕਮ ਵਰਤੋ:** `Get-ADOrganizationalUnit`, `Get-ADUser` ਅਤੇ `Get-ADComputer` ਵਸਤੂਆਂ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ।
- **ਖੇਤਰ ਚੁਣੋ:** ਕੰਮ ਲਈ ਲੋੜੀਂਦੇ ਗੁਣ ਹੀ ਨਿਰਯਾਤ ਕਰੋ।
- **ਨਤੀਜਾ ਜਾਂਚੋ:** ਰਿਪੋਰਟ ਉੱਤੇ ਭਰੋਸਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਗਿਣਤੀ ਅਤੇ ਕੁਝ ਨਮੂਨਾ ਕਤਾਰਾਂ ਮਿਲਾਓ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

ਤੁਹਾਨੂੰ ਚੱਲਦਾ DNS ਅਤੇ ਡੋਮੇਨ ਕੰਟਰੋਲਰ ਤੱਕ ਨੈੱਟਵਰਕ ਪਹੁੰਚ ਵਾਲਾ Windows ਪ੍ਰਸ਼ਾਸਨ ਮੇਜ਼ਬਾਨ, PowerShell ਦਾ **ActiveDirectory** ਮੋਡੀਊਲ, ਚੁਣੀਆਂ ਵਸਤੂਆਂ ਪੜ੍ਹਨ ਲਈ ਮਨਜ਼ੂਰ ਖਾਤਾ ਅਤੇ CSV ਨਤੀਜਿਆਂ ਲਈ ਸੁਰੱਖਿਅਤ ਫੋਲਡਰ ਚਾਹੀਦਾ ਹੈ। Windows ਕਲਾਇੰਟ ਉੱਤੇ ਇਹ ਮੋਡੀਊਲ Remote Server Administration Tools (RSAT) ਦੇ Active Directory ਔਜ਼ਾਰਾਂ ਨਾਲ ਮਿਲਦਾ ਹੈ। [Active Directory ਮੋਡੀਊਲ ਗਾਈਡ](/articles/active-directory-module-powershell-installation-usage-guide/) ਇੰਸਟਾਲੇਸ਼ਨ ਸਮਝਾਉਂਦੀ ਹੈ। Microsoft ਮੋਡੀਊਲ ਦਾ [cmdlet ਹਵਾਲਾ](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) ਅਤੇ [RSAT ਇੰਸਟਾਲੇਸ਼ਨ ਦੇ ਵਿਕਲਪ](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools) ਦਿੰਦਾ ਹੈ। ਇਹ ਗਾਈਡ Windows PowerShell ਲਿਖਤ ਵਰਤਦੀ ਹੈ ਅਤੇ ਡਾਇਰੈਕਟਰੀ ਵਸਤੂਆਂ ਨਹੀਂ ਬਦਲਦੀ।

ਡਾਇਰੈਕਟਰੀ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ ਲਾਗੂ ਰਹਿੰਦੀਆਂ ਹਨ। Microsoft ਦੀ [ਵਿਸ਼ੇਸ਼ ਅਧਿਕਾਰ ਵਾਲੇ ਖਾਤਿਆਂ ਬਾਰੇ ਸਲਾਹ](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory) ਦੱਸਦੀ ਹੈ ਕਿ ਪਹੁੰਚ-ਨਿਯੰਤਰਣ ਸੂਚੀਆਂ ਅਕਸਰ ਪ੍ਰਮਾਣਿਤ ਵਰਤੋਂਕਾਰਾਂ ਨੂੰ ਆਮ ਜਾਣਕਾਰੀ ਪੜ੍ਹਨ ਦਿੰਦੀਆਂ ਹਨ ਅਤੇ ਸੰਵੇਦਨਸ਼ੀਲ ਖੇਤਰਾਂ ਤੇ ਤਬਦੀਲੀਆਂ ਰੋਕਦੀਆਂ ਹਨ। ਪਹਿਲਾਂ ਮਨਜ਼ੂਰ ਖਾਤਾ ਅਤੇ ਜਾਂਚ ਵਾਲੀ OU ਵਰਤੋ। ਸੂਚੀ ਚਲਾਉਣ ਲਈ Domain Admin ਅਧਿਕਾਰ ਨਾ ਵਧਾਓ।

> **ਚੇਤਾਵਨੀ:** CSV ਫ਼ਾਈਲਾਂ ਵਿੱਚ ਖਾਤਿਆਂ ਅਤੇ ਕੰਪਿਊਟਰਾਂ ਦੇ ਨਾਂ ਹੁੰਦੇ ਹਨ। ਉਹਨਾਂ ਨੂੰ ਮਨਜ਼ੂਰ ਥਾਂ ਰੱਖੋ, ਪਹੁੰਚ ਸੀਮਿਤ ਕਰੋ ਅਤੇ ਜਾਂਚ ਮਗਰੋਂ ਵਾਧੂ ਨਕਲਾਂ ਹਟਾਓ। ਕੱਚਾ ਨਿਰਯਾਤ ਪ੍ਰਕਾਸ਼ਿਤ ਨਾ ਕਰੋ ਅਤੇ ਉਸਨੂੰ ਜਨਤਕ Issue ਨਾਲ ਨਾ ਜੋੜੋ।

## ਖੋਜ ਅਧਾਰ ਚੁਣੋ

**ਸੰਗਠਨਾਤਮਕ ਇਕਾਈ (OU)** ਡਾਇਰੈਕਟਰੀ ਵਸਤੂਆਂ ਨੂੰ ਸਮੂਹਾਂ ਵਿੱਚ ਰੱਖਦੀ ਹੈ। ਇਸਦਾ **ਵੱਖਰਾ ਨਾਮ (DN)** ਡਾਇਰੈਕਟਰੀ ਰੁੱਖ ਵਿੱਚ ਇਸਦੀ ਥਾਂ ਦੱਸਦਾ ਹੈ। `-SearchBase` ਪੈਰਾਮੀਟਰ ਪੁੱਛਗਿੱਛ ਨੂੰ ਚੁਣੇ DN ਤੱਕ ਸੀਮਿਤ ਕਰਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਦਾਇਰਾ ਸੋਚ-ਸਮਝ ਕੇ ਨਾ ਚੁਣੋ, ਤਾਂ ਚੌੜਾ ਫ਼ਿਲਟਰ ਜਾਂਚ ਦੀ ਲੋੜ ਨਾਲੋਂ ਕਈ ਵੱਧ ਵਸਤੂਆਂ ਦੇ ਸਕਦਾ ਹੈ।

ਪਹਿਲਾਂ ਮੋਡੀਊਲ ਲੋਡ ਕਰੋ ਅਤੇ ਮੌਜੂਦਾ ਡੋਮੇਨ ਦਾ DN ਵੇਖੋ:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) ਅਤੇ ਇਸ ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੀ ਡੋਮੇਨ ਜਾਣਕਾਰੀ ਦਰਜ ਕਰਦਾ ਹੈ। ਖੋਜ ਅਧਾਰ ਚੁਣਨ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚ ਵਾਲੀ OU ਲੱਭੋ:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

ਨਤੀਜੇ ਵਿੱਚੋਂ ਸਹੀ DN ਨਕਲ ਕਰੋ। ਅਗਲੀਆਂ ਮਿਸਾਲਾਂ ਵਿੱਚ ਇਸ ਦਸਤਾਵੇਜ਼ੀ ਕਦਰ ਦੀ ਥਾਂ ਆਪਣੀ OU ਦਾ DN ਪਾਓ:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` ਦਸਤਾਵੇਜ਼ੀ ਮਿਸਾਲ ਵਾਲਾ ਡੋਮੇਨ ਹੈ। ਇਸਦਾ DN ਅਸਲ ਪੁੱਛਗਿੱਛ ਵਿੱਚ ਨਾ ਵਰਤੋ। ਜੇ ਜਾਣ-ਬੁੱਝ ਕੇ ਪੂਰੇ ਡੋਮੇਨ ਦੀ ਸੂਚੀ ਚਾਹੀਦੀ ਹੈ, ਤਾਂ `$SearchBase` ਨੂੰ ਡੋਮੇਨ ਦੇ DN ਉੱਤੇ ਰੱਖੋ ਅਤੇ ਰਿਪੋਰਟ ਵਿੱਚ ਵੱਡਾ ਦਾਇਰਾ ਦਰਜ ਕਰੋ। Microsoft ਦਾ [Get-ADOrganizationalUnit ਹਵਾਲਾ](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) `-Filter` ਅਤੇ `-SearchBase` ਸਮਝਾਉਂਦਾ ਹੈ।

## OU, ਵਰਤੋਂਕਾਰਾਂ ਅਤੇ ਕੰਪਿਊਟਰਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ

ਵਸਤੂਆਂ ਦੀ ਗਿਣਤੀ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ। ਇਸ ਨਾਲ ਗਲਤ ਖੋਜ ਅਧਾਰ ਜਾਂ ਅਣਚਾਹੇ ਖਾਲੀ ਨਤੀਜੇ ਦਾ ਜਲਦੀ ਪਤਾ ਲੱਗਦਾ ਹੈ:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` ਖੋਜ ਅਧਾਰ ਦੇ ਅੰਦਰ ਸਾਰੀਆਂ ਮਿਲਦੀਆਂ ਵਸਤੂਆਂ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ। Microsoft [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) ਅਤੇ [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) ਨੂੰ ਪ੍ਰਾਪਤੀ ਹੁਕਮਾਂ ਵਜੋਂ ਦਰਜ ਕਰਦਾ ਹੈ। ਸਿਫ਼ਰ ਗਿਣਤੀ ਸਹੀ ਵੀ ਹੋ ਸਕਦੀ ਹੈ, ਪਰ ਸੂਚੀ ਪੂਰੀ ਮੰਨਣ ਤੋਂ ਪਹਿਲਾਂ DN, ਇਜਾਜ਼ਤਾਂ ਅਤੇ ਨਿਸ਼ਾਨਾ ਡੋਮੇਨ ਜਾਂਚੋ।

ਹੁਣ ਕਨਸੋਲ ਵਿੱਚ ਕੁਝ ਕਤਾਰਾਂ ਦਾ ਪੂਰਵ-ਦ੍ਰਿਸ਼ ਵੇਖੋ। ਚੁਣੇ ਖੇਤਰ ਸੰਭਾਲੋ ਤਾਂ ਜੋ ਪੂਰਵ-ਦ੍ਰਿਸ਼ ਅਤੇ ਅਗਲਾ CSV ਨਿਰਯਾਤ ਇੱਕੋ ਕਾਲਮ ਵਰਤਣ:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

ਕੰਪਿਊਟਰਾਂ ਲਈ ਵਾਧੂ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਗੁਣ ਉਦੋਂ ਹੀ ਮੰਗੋ ਜਦੋਂ ਜਾਂਚ ਨੂੰ ਇਸਦੀ ਲੋੜ ਹੋਵੇ:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

`-Properties` ਪੈਰਾਮੀਟਰ ਉਹ ਗੁਣ ਮੰਗਦਾ ਹੈ ਜੋ ਹੁਕਮ ਦੇ ਮੂਲ ਸਮੂਹ ਵਿੱਚ ਨਹੀਂ ਹੁੰਦੇ। Microsoft ਇਸਨੂੰ [ਕੰਪਿਊਟਰ ਹੁਕਮ ਦੇ ਹਵਾਲੇ](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) ਵਿੱਚ ਸਮਝਾਉਂਦਾ ਹੈ। ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਦੇ ਨਾਂ ਨੂੰ ਡਾਇਰੈਕਟਰੀ ਜਾਣਕਾਰੀ ਮੰਨੋ, ਮੌਜੂਦਾ ਸਥਾਪਤ ਸੰਸਕਰਣ ਦਾ ਸਬੂਤ ਨਹੀਂ। ਕੰਪਿਊਟਰ ਵਸਤੂ ਪੁਰਾਣੀ ਹੋ ਸਕਦੀ ਹੈ ਜਾਂ ਇਸਦਾ ਗੁਣ ਹਾਲੇ ਅੱਪਡੇਟ ਨਾ ਹੋਇਆ ਹੋਵੇ।

## ਜਾਂਚਯੋਗ CSV ਫ਼ਾਈਲਾਂ ਨਿਰਯਾਤ ਕਰੋ

ਕਾਫ਼ੀ ਖਾਲੀ ਥਾਂ ਵਾਲਾ ਮਨਜ਼ੂਰ ਨਤੀਜਾ-ਫੋਲਡਰ ਚੁਣੋ। ਅਗਲੇ ਹੁਕਮ **ਸਥਾਨਕ CSV ਫ਼ਾਈਲਾਂ** ਲਿਖਦੇ ਹਨ ਅਤੇ ਡਾਇਰੈਕਟਰੀ ਵਸਤੂਆਂ ਨਹੀਂ ਬਦਲਦੇ। ਇਹਨਾਂ ਨੂੰ ਉਸ ਫੋਲਡਰ ਵਿੱਚ ਚਲਾਓ। `-NoClobber` ਮੌਜੂਦਾ ਫ਼ਾਈਲ ਉੱਤੇ ਲਿਖਣ ਤੋਂ ਰੋਕਦਾ ਹੈ। ਹਰ ਵਾਰ ਨਵਾਂ ਫੋਲਡਰ ਜਾਂ ਫ਼ਾਈਲ ਨਾਂ ਵਰਤੋ।

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

Microsoft ਦਾ [Export-Csv ਹਵਾਲਾ](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) `-NoTypeInformation`, `-Encoding` ਅਤੇ `-NoClobber` ਸਮਝਾਉਂਦਾ ਹੈ। ਹਰ CSV ਨੂੰ ਲਿਖਤ ਸੰਪਾਦਕ ਜਾਂ ਮਨਜ਼ੂਰ ਸਾਰਣੀ-ਸਾਧਨ ਵਿੱਚ ਖੋਲ੍ਹੋ। ਸਿਰਲੇਖ, ਕੁਝ ਕਤਾਰਾਂ ਅਤੇ ਪਹਿਲਾਂ ਗਿਣੇ ਰਿਕਾਰਡਾਂ ਦੀ ਗਿਣਤੀ ਜਾਂਚੋ। ਅਸਫਲ ਹੁਕਮ ਜਾਂ ਸਿਫ਼ਰ ਬਾਈਟ ਵਾਲੀ ਫ਼ਾਈਲ ਪੂਰੀ ਰਿਪੋਰਟ ਦਾ ਸਬੂਤ ਨਹੀਂ ਹੈ।

> **ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** ਚੁਣੇ ਡਾਇਰੈਕਟਰੀ ਦਾਇਰੇ ਦੇ OU, ਵਰਤੋਂਕਾਰਾਂ ਅਤੇ ਕੰਪਿਊਟਰਾਂ ਦੇ ਰਿਕਾਰਡਾਂ ਵਾਲੀਆਂ ਤਿੰਨ CSV ਫ਼ਾਈਲਾਂ ਹਨ। ਕਤਾਰਾਂ ਦੀ ਗਿਣਤੀ ਅਤੇ ਨਮੂਨਾ ਕਦਰਾਂ ਚੁਣੇ ਦਾਇਰੇ ਨਾਲ ਮਿਲਦੀਆਂ ਹਨ।

## ਵਸਤੂਆਂ ਬਦਲੇ ਬਿਨਾਂ ਜਾਂਚੋ

ਸੂਚੀ ਨਾਲ ਖਾਸ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲੱਭੋ: ਕਿਹੜੀ OU ਕਿਸੇ ਕੰਪਿਊਟਰ ਦੀ ਜ਼ਿੰਮੇਵਾਰੀ ਲੈਂਦੀ ਹੈ? ਕਿਹੜੇ ਵਰਤੋਂਕਾਰ ਖਾਤੇ ਬੰਦ ਹਨ? ਕਿਹੜੇ ਜੰਤਰਾਂ ਦੇ ਨਾਂ ਲਈ ਮਾਲਕ ਲੱਭਣਾ ਹੈ? ਨਤੀਜੇ ਵੱਖਰੀ ਜਾਂਚ-ਟਿੱਪਣੀ ਵਿੱਚ ਲਿਖੋ। `Enabled` ਕਦਰ ਤੋਂ ਇਹ ਨਾ ਮੰਨੋ ਕਿ ਖਾਤਾ ਹਾਲੇ ਲੋੜੀਂਦਾ ਹੈ। ਸਿਰਫ਼ ਨਿਰਯਾਤ ਦੇ ਆਧਾਰ ਉੱਤੇ ਕੋਈ ਵਸਤੂ ਨਾ ਮਿਟਾਓ ਅਤੇ ਨਾ ਬੰਦ ਕਰੋ।

ਨਿਯਮਤ ਰਿਪੋਰਟ ਲਈ ਪੁੱਛਗਿੱਛ ਦੀ ਤਾਰੀਖ, ਡੋਮੇਨ, OU ਦਾ DN, ਚੁਣੇ ਗੁਣ, ਚਲਾਉਣ ਵਾਲਾ ਵਿਅਕਤੀ ਅਤੇ CSV ਦੀ ਥਾਂ ਲਿਖੋ। ਦੋ ਨਿਰਯਾਤਾਂ ਦੀ ਤੁਲਨਾ ਵੇਲੇ ਪੱਕਾ ਕਰੋ ਕਿ ਦੋਹਾਂ ਵਿੱਚ ਇੱਕੋ ਦਾਇਰਾ ਅਤੇ ਖੇਤਰ ਹਨ। ਨਹੀਂ ਤਾਂ ਫ਼ਰਕ ਅਸਲ ਡਾਇਰੈਕਟਰੀ ਤਬਦੀਲੀ ਦੀ ਥਾਂ ਪੁੱਛਗਿੱਛ ਕਾਰਨ ਹੋ ਸਕਦਾ ਹੈ।

ਇਹ **ਸੂਚੀ** ਹੈ, ਵਿਸ਼ੇਸ਼ ਅਧਿਕਾਰ ਵਾਲੇ ਖਾਤਿਆਂ ਦੀ ਜਾਂਚ ਜਾਂ ਲਾਗਇਨ ਗਤੀਵਿਧੀ ਦੀ ਰਿਪੋਰਟ ਨਹੀਂ। Microsoft ਦੱਸਦਾ ਹੈ ਕਿ Active Directory ਦੇ ਗੁਣ ਅਤੇ ਇਜਾਜ਼ਤਾਂ ਵਸਤੂ ਅਤੇ ਮਾਹੌਲ ਅਨੁਸਾਰ ਬਦਲਦੀਆਂ ਹਨ। ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਦੇ ਗੁਣ ਜਾਂ ਦਿਖਾਏ ਨਾਂ ਉੱਤੇ ਕਾਰਵਾਈ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਸਿਸਟਮ ਮਾਲਕ ਨਾਲ ਜਾਂਚੋ। ਵਿਆਪਕ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ ਲਈ [Active Directory ਸੁਰੱਖਿਆ ਗਾਈਡ](/articles/active-directory-security-best-practices/) ਵੇਖੋ।

## ਸਮੱਸਿਆ ਹੱਲ

- **ਮੋਡੀਊਲ ਲੋਡ ਨਹੀਂ ਹੁੰਦਾ:** ਪੱਕਾ ਕਰੋ ਕਿ ਮੇਜ਼ਬਾਨ ਉੱਤੇ RSAT ਦੇ Active Directory ਔਜ਼ਾਰ ਜਾਂ Windows Server ਪ੍ਰਸ਼ਾਸਨ ਔਜ਼ਾਰ ਸਥਾਪਤ ਹਨ। [ਮੋਡੀਊਲ ਸੈੱਟਅੱਪ ਗਾਈਡ](/articles/active-directory-module-powershell-installation-usage-guide/) ਵੇਖੋ।
- **ਪੁੱਛਗਿੱਛ ਕੋਈ ਵਸਤੂ ਨਹੀਂ ਦਿੰਦੀ:** ਸਹੀ DN, ਮੌਜੂਦਾ ਡੋਮੇਨ, OU ਦੀ ਸਮੱਗਰੀ ਅਤੇ ਪੜ੍ਹਨ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ ਜਾਂਚੋ। ਦਾਇਰਾ ਵਧਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਜਾਣੀ-ਪਛਾਣੀ ਛੋਟੀ OU ਅਜ਼ਮਾਓ।
- **ਕੋਈ ਗੁਣ ਖਾਲੀ ਹੈ:** ਜਾਂਚੋ ਕਿ ਗੁਣ ਮੌਜੂਦ ਹੈ ਅਤੇ ਤੁਹਾਡਾ ਖਾਤਾ ਇਸਨੂੰ ਪੜ੍ਹ ਸਕਦਾ ਹੈ। ਛੁੱਟੇ ਖੇਤਰਾਂ ਨੂੰ ਅਟਕਲ ਨਾਲ ਨਾ ਭਰੋ।
- **ਨਿਰਯਾਤ ਦੱਸਦਾ ਹੈ ਕਿ ਫ਼ਾਈਲ ਪਹਿਲਾਂ ਮੌਜੂਦ ਹੈ:** `-NoClobber` ਨੇ ਪਿਛਲੀ ਰਿਪੋਰਟ ਬਚਾਈ। ਨਵਾਂ ਫ਼ਾਈਲ ਨਾਂ ਜਾਂ ਫੋਲਡਰ ਚੁਣ ਕੇ ਹੁਕਮ ਦੁਬਾਰਾ ਚਲਾਓ।
- **ਗਿਣਤੀ ਉਮੀਦ ਨਾਲ ਨਹੀਂ ਮਿਲਦੀ:** ਜਾਂਚੋ ਕਿ ਵਰਤੋਂਕਾਰ ਜਾਂ ਕੰਪਿਊਟਰ ਹੋਰ OU ਵਿੱਚ ਤਾਂ ਨਹੀਂ, ਦਾਇਰਾ ਬਦਲਿਆ ਤਾਂ ਨਹੀਂ, ਜਾਂ ਪੁੱਛਗਿੱਛ ਦੌਰਾਨ ਡਾਇਰੈਕਟਰੀ ਬਦਲੀ ਤਾਂ ਨਹੀਂ।

## ਅਗਲੇ ਕਦਮ

ਕੱਚੀਆਂ CSV ਫ਼ਾਈਲਾਂ ਸਹਿਮਤ ਜਾਂਚ-ਮਿਆਦ ਲਈ ਸੁਰੱਖਿਅਤ ਥਾਂ ਰੱਖੋ। ਜਾਂਚਕਰਤਾ ਨੂੰ ਲੋੜੀਂਦੇ ਖੇਤਰ ਹੀ ਸਾਂਝੇ ਕਰੋ। ਜ਼ਿੰਮੇਵਾਰ ਲੋਕ ਨਤੀਜਿਆਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਮਗਰੋਂ ਆਪਣੇ ਆਮ ਮਨਜ਼ੂਰੀ ਅਤੇ ਵਾਪਸੀ ਦੇ ਢੰਗ ਅਨੁਸਾਰ ਤਬਦੀਲੀਆਂ ਦੀ ਯੋਜਨਾ ਬਣਾਓ। ਮਨਜ਼ੂਰ ਤਬਦੀਲੀਆਂ ਮਗਰੋਂ ਨਤੀਜਾ ਪੱਕਾ ਕਰਨ ਲਈ ਉਸੇ ਦਾਇਰੇ ਵਿੱਚ ਉਹੀ ਸੂਚੀ ਮੁੜ ਚਲਾਓ।