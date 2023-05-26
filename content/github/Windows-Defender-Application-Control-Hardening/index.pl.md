---
title: "Kompletny poradnik jak wzmocnić system Windows za pomocą Windows Defender Application Control WDAC"
date: 2020-12-16
toc: true
draft: false
description: "Dowiedz się, jak używać Windows Defender Application Control WDAC do utwardzania systemu operacyjnego Windows za pomocą skryptów i narzędzi."
tags: ["Windows Defender Application Control WDAC Hardening", "PowerShell", "Skrypt PowerShell", "Automatyka", "Zgodność", "Blue-Team", "Windows Defender STIG Script", "Utwardzanie systemu Windows Defender", "Windows Defender STIG", "Obrońca STIG", "Windows Defender Exploit Protection WDEP", "Windows Defender Attack Surface Reduction ASR", "Windows Server 2016 2019", "Windows Server Core", "Zestaw narzędzi Microsoft WDAC", "Odświeżenie polityki CI", "Zalecane przez Microsoft zasady blokowania", "Zalecane przez Microsoft zasady blokowania sterowników", "Zasady XML", "Polityka BIN", "Polityka grupowa", "Microsoft Intune"]
---

**Harden Windows z Windows Defender Application Control WDAC**.

## Uwagi:
- Windows Server 2016/2019 lub cokolwiek przed wersją 1903 obsługuje tylko jedną politykę legacy w danym czasie.
- Edycja Windows Server Core wspiera WDAC, ale niektóre komponenty zależne od AppLockera nie będą działać.
- Prosimy o zapoznanie się z.[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) przed wdrożeniem, a nawet przetestowaniem.

## Lista skryptów i narzędzi, które ta kolekcja wykorzystuje:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Dodatkowe konfiguracje były rozważane od:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Explanation:

### XML vs. BIN:

- Po prostu, polityki **"XML "** są do zastosowania na maszynie lokalnie, a pliki **"BIN "** są do egzekwowania ich za pomocą albo[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) Podczas gdy w lokalnym wdrożeniu można używać polityk XML, BIN lub CIP, ogólnie rzecz biorąc, należy trzymać się XML, jeśli to możliwe, a zwłaszcza podczas audytu lub rozwiązywania problemów.

### Opisy polityk:

- **Polisy domyślne:**
  - Polityki "Domyślne" używają tylko domyślnych funkcji dostępnych w WDAC-Toolkit.
- **Recommended Policies:**
  - Zasady "Zalecane" wykorzystują funkcje domyślne, jak również zalecane przez Microsoft[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) zasady.
- **Audit Policies:**
  - Zasady "Audytu" rejestrują jedynie wyjątki od reguł. Służy to do testowania w środowisku, dzięki czemu można modyfikować zasady, aby dopasować je do potrzeb środowiska.
- **Wymuszone polityki:**
  - Zasady "Enforced" nie pozwalają na żadne wyjątki od reguł, aplikacje, sterowniki, dlls, itp. będą blokowane, jeśli nie będą zgodne.

### Dostępne polityki:

- **XML:**
  - **Audit Only:**
    -`WDAC_V1_Default_Audit_{version}.xml`
    -`WDAC_V1_Recommended_Audit_{version}.xml`
  - **Wykonane:**
    -`WDAC_V1_Default_Enforced_{version}.xml`
    -`WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN:**
  - **Audit Only:**
    -`WDAC_V1_Default_Audit_{version}.bin`
    -`WDAC_V1_Recommended_Audit_{version}.bin`
  - **Wykonane:**
    -`WDAC_V1_Default_Enforced_{version}.bin`
    -`WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP:**
  - **Audit Only:**
    -`WDAC_V1_Default_Audit\{uid}.cip`
    -`WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Wykonane:**
    -`WDAC_V1_Default_Enforced\{uid}.cip`
    -`WDAC_V1_Recommended_Enforced\{uid}.cip`

Zaktualizuj następującą linię w skrypcie, aby użyć polityki, którą chcesz lokalnie:

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

Alternatywnie, możesz użyć[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) do egzekwowania polityki WDAC.

## Audyt:

Dzienniki zdarzeń WDAC można przeglądać w przeglądarce zdarzeń pod:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Recommended Reading:

-[Argonsys - Deploying Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
-[Microsoft - Audit Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
-[Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
-[Microsoft - Deploy Windows Defender Application Control policies by using Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
-[Microsoft - Deploy Windows Defender Application Control policies by using Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
-[Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
-[Microsoft - Enforce Windows Defencer Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
-[Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
-[Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## Jak uruchomić skrypt:

### Manual Install:

W przypadku ręcznego pobrania, skrypt należy uruchomić z administracyjnego powershella w katalogu zawierającym wszystkie pliki z.[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
