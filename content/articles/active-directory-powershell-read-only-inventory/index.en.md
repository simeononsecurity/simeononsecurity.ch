---
title: "Build a Read-Only Active Directory Inventory With PowerShell"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Inventory Active Directory OUs, users, and computers with scoped PowerShell queries. Export reviewable CSV files without changing directory objects."
genre: ["Active Directory", "PowerShell", "System Administration"]
tags: ["Active Directory inventory", "PowerShell AD inventory", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "read only AD", "AD user export", "AD computer export", "AD OU export", "Export-Csv", "RSAT", "directory audit", "AD reporting", "OU inventory", "Windows Server", "PowerShell script", "AD module", "directory hygiene"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "An Active Directory tree with user, computer, and organizational unit records flowing to three review files."
coverCaption: "Scope the query, then export only the fields needed for review."
---

An Active Directory cleanup starts with a trustworthy list of what exists. This **read-only inventory** gathers organizational units, users, and computers from one chosen scope. It exports three CSV files for review without changing directory objects. You still need to protect those files because names and device details reveal part of your environment.

## Key Takeaways

- **Choose a scope:** Query one organizational unit before expanding to a whole domain.
- **Use read commands:** `Get-ADOrganizationalUnit`, `Get-ADUser`, and `Get-ADComputer` retrieve objects.
- **Select fields:** Export only the properties needed for the task.
- **Check the output:** Compare counts and sample rows before relying on a report.

## Before You Begin

You need a domain-connected Windows administration host with the **ActiveDirectory** PowerShell module, an account approved to read the selected objects, and a protected folder for CSV output. The site's [Active Directory module guide](/articles/active-directory-module-powershell-installation-usage-guide/) covers installation. Microsoft lists the module's [cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/activedirectory/). This guide uses Windows PowerShell syntax and avoids changes to directory objects.

Directory permissions still apply. Microsoft explains that object access control lists often give authenticated users read access to general information while restricting sensitive fields and changes in its [privileged accounts guidance](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory). Use an approved account and a test OU first. Do not elevate to Domain Admin to make an inventory succeed.

> **Warning:** The CSV files contain account and computer names. Save them to an approved location, limit access, and remove extra copies after review. Do not publish a raw export or attach one to a public issue.

## Choose the Search Base

An **organizational unit (OU)** groups directory objects. Its **distinguished name (DN)** identifies its position in the directory tree. The `-SearchBase` parameter limits a query to a chosen DN. Without a deliberate scope, a broad filter might return far more objects than your review needs.

First load the module and inspect the current domain DN:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft documents [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) and its domain output. Find the OU you intend to review before setting the search base:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Copy the exact DN from the result. For the remaining examples, replace this documentation value with your OU's DN:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` is a documentation domain. Do not copy its DN into a live query. If you intentionally need a domain-wide inventory, set `$SearchBase` to the domain DN and record that broader scope in the report. Microsoft's [Get-ADOrganizationalUnit reference](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) documents `-Filter` and `-SearchBase`.

## Inventory OUs, Users, and Computers

Start with counts. They give you a quick way to catch a wrong search base or unexpected empty result:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` means all matching objects within the search base. Microsoft documents [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) and [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) as retrieval commands. A zero count might be legitimate, but check the DN, permissions, and target domain before treating it as a complete inventory.

Now preview a few rows in the console. The command below selects only fields that help identify and group an object:

```powershell
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -First 10 Name, SamAccountName, Enabled, DistinguishedName
```

For computers, request the extra operating system field only when your review needs it:

```powershell
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -First 10 Name, DNSHostName, OperatingSystem, Enabled, DistinguishedName
```

The `-Properties` parameter requests properties outside the cmdlet's default set. Microsoft's [computer cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) documents it. Treat operating system names as directory data, not proof of the current installed version. A computer object might be stale or its attribute might not have updated.

## Export a Reviewable CSV

Choose an approved output folder with enough space. The following commands write **local CSV files** and leave directory objects unchanged. Run them in that folder. `-NoClobber` prevents an existing file from being overwritten. Use a new folder or filename for each run.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object Name, SamAccountName, Enabled, DistinguishedName |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object Name, DNSHostName, OperatingSystem, Enabled, DistinguishedName |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Microsoft's [Export-Csv reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) explains `-NoTypeInformation`, `-Encoding`, and `-NoClobber`. Open each CSV in a text editor or approved spreadsheet tool. Check its header, a few rows, and the number of records against the earlier counts. A failed command or a zero-byte file does not establish a complete report.

> **Expected Result:** You have three scoped CSV files with OU, user, and computer records. Their row counts and sample entries match the selected directory scope.

## Review Without Changing Objects

Use the inventory to ask specific questions: Which OU owns a computer? Which users are disabled? Which device names need an owner? Record findings in a separate review note. Do not equate an `Enabled` value with whether an account is still needed. Do not delete or disable an object based on an export alone.

For a recurring report, record the query date, domain, OU DN, selected properties, operator, and CSV location. If you compare two exports, confirm that both used the same scope and fields. Otherwise a difference might come from the query rather than an actual directory change.

This is an **inventory**, not a privileged-account audit or a login-activity report. Microsoft notes that Active Directory properties and permissions vary by object and environment. An operating system attribute or display name should be verified with the system owner before you act on it. The site's [Active Directory security guide](/articles/active-directory-security-best-practices/) covers the broader security controls.

## Troubleshooting

- **Module will not import:** Confirm RSAT or the AD DS administration tools are installed on the host. Follow the [module setup guide](/articles/active-directory-module-powershell-installation-usage-guide/).
- **Query returns no objects:** Check the exact DN, current domain, OU contents, and read permissions. Try a known small OU before broadening scope.
- **A property is blank:** Confirm that the attribute exists and that your account can read it. Do not fill missing fields with guesses.
- **Export says the file exists:** `-NoClobber` protected the earlier report. Choose a new filename or folder and rerun.
- **Counts differ from expectations:** Check whether users or computers sit in another OU, whether your scope changed, and whether the directory changed during the query.

## Next Steps

Keep the raw CSV in a protected location for the agreed review period. Share only the fields the reviewer needs. After owners verify findings, plan changes through your normal approval and rollback process. Repeat the same scoped inventory after the approved changes to confirm the result.
