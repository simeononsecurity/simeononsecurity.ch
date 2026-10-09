---
title: "Vollständiger Leitfaden zur Härtung von Windows mit Windows Defender..."
date: 2020-12-16
toc: true
draft: false
description: Erfahren Sie, wie Sie Windows Defender Application Control WDAC verwenden, um Ihr Windows-Betriebssystem mit Skripten und Tools zu härten.
tags:
- Windows Defender Application Control WDAC Härtung
- PowerShell
- PowerShell-Skript
- Automatisierung
- Compliance
- Blue-Team
- Windows Defender STIG-Skript
- Windows Defender Härtung
- Windows Defender STIG
- Defender STIG
- Windows Defender Exploit Protection WDEP
- Windows Defender Attack Surface Reduction ASR
- Windows Server 2016 2019
- Windows Server Core
- Microsoft WDAC-Toolkit
- CI-Richtlinie aktualisieren
- Von Microsoft empfohlene Blockierregeln
- Von Microsoft empfohlene Treiber-Blockierregeln
- XML-Richtlinien
- BIN-Richtlinien
- Gruppenrichtlinie
- Microsoft Intune
cover: /img/cover/Windows-Defender-Application-Control-Hardening.webp
coverAlt: Eine Illustration eines futuristischen Serverraums mit leuchtenden Bildschirmen, die XML- und BIN-Dateistrukturen im Zusammenhang mit Windows Defender Application Control zeigen. Der dunkle Hintergrund verstärkt die lebendigen Farben.
coverCaption: ''
lastmod: 2026-10-08
---

**Windows mit Windows Defender Application Control WDAC härten**

## Hinweise:
- Windows Server 2016/2019 oder alle Versionen vor 1903 unterstützen jeweils nur eine einzelne Legacy-Richtlinie.
- Die Windows Server Core Edition unterstützt [WDAC](https://simeononsecurity.com/til/2022-05-18/), aber einige Komponenten, die von AppLocker abhängen, funktionieren nicht.
- Bitte lesen Sie die [Empfohlene Lektüre](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading), bevor Sie implementieren oder testen.

## Eine Liste der Skripte und Tools, die diese Sammlung verwendet:

- [MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
- [Microsoft - CI-Richtlinie aktualisieren](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Zusätzliche Konfigurationen wurden berücksichtigt von:

- [Microsoft - Empfohlene Blockierregeln](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Empfohlene Treiber-Blockierregeln](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Erklärung:

### XML vs. BIN:

- Einfach gesagt sind die **"XML"**-Richtlinien für die lokale Anwendung auf einem Gerät gedacht, während die **"BIN"**-Dateien zur Durchsetzung über [Gruppenrichtlinie](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) oder [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) verwendet werden. Obwohl Sie XML-, BIN- oder CIP-Richtlinien lokal einsetzen können, sollten Sie im Allgemeinen XML bevorzugen, besonders beim Auditieren oder bei der Fehlersuche.

### Richtlinienbeschreibungen:

- **Standardrichtlinien**
  - Die "Standard" Richtlinien verwenden nur die Standardfunktionen des WDAC-Toolkits.
- **Empfohlene Richtlinien**
  - Die "Empfohlenen" Richtlinien verwenden die Standardfunktionen sowie von Microsoft empfohlene [Blockierungen](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) und [Treiberblockierungen](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules).
- **Audit-Richtlinien**
  - Die "Audit" Richtlinien protokollieren nur Ausnahmen von den Regeln. Dies dient zum Testen in Ihrer Umgebung. So können Sie die Richtlinien nach Belieben anpassen, um den Anforderungen Ihrer Umgebung zu entsprechen.
- **Durchgesetzte Richtlinien**
  - Die "Durchgesetzten" Richtlinien erlauben keine Ausnahmen von den Regeln. Anwendungen, Treiber, DLLs usw. werden blockiert, wenn sie nicht konform sind.

### Verfügbare Richtlinien:

- **XML:**
  - **Nur Audit:**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **Durchgesetzt:**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN:**
  - **Nur Audit:**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **Durchgesetzt:**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP:**
  - **Nur Audit:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Durchgesetzt:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Aktualisieren Sie die folgende Zeile im Skript, um die gewünschte Richtlinie lokal zu verwenden:

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

Alternativ können Sie [Gruppenrichtlinie](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) oder [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) verwenden, um die WDAC-Richtlinien durchzusetzen.

## Auditierung:

Sie können die WDAC-Ereignisprotokolle im Ereignisanzeige unter folgendem Pfad einsehen:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Empfohlene Lektüre:

- [Argonsys - Bereitstellung der Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Auditieren von Windows Defender Application Control Richtlinien](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Erstellen einer WDAC-Richtlinie für Geräte mit festem Arbeitsaufkommen anhand eines Referenzcomputers](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Bereitstellen von Windows Defender Application Control Richtlinien mit Gruppenrichtlinie](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Bereitstellen von Windows Defender Application Control Richtlinien mit Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Bereitstellen von WDAC-Richtlinien per Skript](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Durchsetzen von Windows Defender Application Control Richtlinien](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Anleitung zum Erstellen von WDAC-Deny-Richtlinien](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Verwendung mehrerer Windows Defender Application Control Richtlinien](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## So führen Sie das Skript aus:

### Manuelle Installation:

Wenn Sie das Skript manuell heruntergeladen haben, muss es aus einer administrativen PowerShell im Verzeichnis gestartet werden, das alle Dateien aus dem [GitHub-Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip) enthält.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
