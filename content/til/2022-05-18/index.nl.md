---
title: "Vandaag heb ik meer geleerd over het maken en implementeren van WDAC-beleid"
date: 2022-05-18
toc: true
draft: false
description: "Vandaag heb ik meer geleerd over voorwaardelijk en variabel beheer van Ansible"
genre: ["Automatisering", "Windows Beveiliging", "Toepassingscontrole", "Windows Verdediger", "WDAC", "Powershell", "Bescherming tegen bedreigingen", "Windows Server 2019", "Bedrijfsbeveiliging", "Beleidsbeheer", "Beste praktijken voor beveiliging"]
tags: ["automatisering", "WDAC", "toepassingsbeheer", "Windows Defender Toepassingsbeheer", "Windows Verdediger", "Powershell", "Microsoft-documentatie", "WDAC-beleid maken", "beleidsinzet", "scriptgebaseerde inzet", "meerdere WDAC-beleidslijnen", "apparaten met vaste werklast", "vertrouwde toepassingen", "weigeringsbeleid", "beveiligingsprocedures", "beleidsbeheer", "bedrijfsbeveiliging", "bescherming tegen bedreigingen", "Windows server", "Windows beveiliging", "applicatie whitelisting"]
---

**Wat SimeonOnSecurity vandaag heeft geleerd en interessant vond**

Vandaag heeft SimeonOnSecurity zijn repository Windows-Defender-Application-Control-Hardening bijgewerkt en geleerd over Windows Defender Application Control (WDAC), een functie van Windows 10 Enterprise en Windows Server 2019 die beveiliging biedt door te controleren wat er op een apparaat wordt uitgevoerd.

SimeonOnSecurity dook in de Microsoft-documentatie over WDAC en ontdekte verschillende belangrijke bronnen voor het maken en implementeren van beleidsregels. Hij leerde over hoe je een WDAC-beleid maakt voor apparaten met een vaste werkbelasting met behulp van een referentiecomputer, hoe je WDAC-beleidsregels kunt implementeren met behulp van een script en hoe je meerdere beleidsregels kunt gebruiken voor verschillende scenario's.

Daarnaast heeft SimeonOnSecurity inzicht gekregen in de richtlijnen voor het maken van WDAC-weigerbeleid, waardoor hij het concept beter begrijpt om alleen vertrouwde applicaties toe te staan op een apparaat en alle andere applicaties te weigeren.

In het algemeen heeft SimeonOnSecurity's verkenning van Windows Defender Application Control zijn begrip van het belang van applicatiecontrole in moderne beveiligingspraktijken verder verstevigd.

## Repos bijgewerkt:
- [simeononsecurity/Windows-Defender-Application-Control-Hardening](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening)

## WDAC lezen:
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)
