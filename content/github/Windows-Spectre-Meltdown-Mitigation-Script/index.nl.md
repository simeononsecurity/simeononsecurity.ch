---
title: "Windows beschermen tegen speculatieve executieaanvallen via zijkanalen"
date: 2020-06-18
toc: true
draft: false
description: "Leer hoe u uw Windows-systeem kunt beschermen tegen speculatieve zijkanaalaanvallen met het mitigatiescript en de firmware-updates van Microsoft."
tags: ["Windows Spectre Meltdown Mitigation Script", "Speculatieve uitvoering Zijkanaalaanvallen", "Microsoft", "Intel", "AMD", "VIA", "ARM", "Android", "Chroom", "iOS", "macOS", "Tak Doel Injectie", "Bounds Check Bypass", "Rogue Data Cache Load", "Speculatieve opslagomleiding", "Microarchitecturale gegevensbemonstering", "CVE's", "Firmware-updates", "GitHub archief", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Simpel script om bescherming te bieden tegen speculatieve uitvoering van zijkanalen in Windows-systemen.**

Microsoft is op de hoogte van een nieuwe, openbaar gemaakte klasse van kwetsbaarheden die "speculatieve uitvoering via zijkanalen" worden genoemd en die veel moderne processoren treffen, waaronder Intel, AMD, VIA en ARM.

**Noot:** Dit probleem treft ook andere besturingssystemen, zoals Android, Chrome, iOS en macOS. Daarom adviseren wij klanten advies in te winnen bij die leveranciers.

We hebben verschillende updates uitgebracht om deze kwetsbaarheden te verhelpen. We hebben ook maatregelen genomen om onze clouddiensten te beveiligen. Zie de volgende secties voor meer details.

We hebben nog geen informatie ontvangen die erop wijst dat deze kwetsbaarheden zijn gebruikt om klanten aan te vallen. We werken nauw samen met industriële partners, waaronder chipfabrikanten, OEM's van hardware en leveranciers van toepassingen, om klanten te beschermen. Om alle beschikbare bescherming te krijgen, zijn firmware (microcode) en software-updates nodig. Dit omvat microcode van OEM-apparaten en, in sommige gevallen, updates van antivirussoftware.

**Dit artikel behandelt de volgende kwetsbaarheden:**
- CVE-2017-5715 - "Branch Target Injection".
- CVE-2017-5753 - "Bounds Check Bypass".
- CVE-2017-5754 - "Rogue Data Cache Load".
- CVE-2018-3639 - "Speculative Store Bypass".
- CVE-2018-11091 - "Microarchitectural Data Sampling Uncacheable Memory (MDSUM)".
- CVE-2018-12126 - "Microarchitectural Store Buffer Data Sampling (MSBDS)".
- CVE-2018-12127 - "Microarchitectural Fill Buffer Data Sampling (MFBDS)".
- CVE-2018-12130 - "Microarchitectural Load Port Data Sampling (MLPDS)".

**UPDATED ON AUGUST 6, 2019** Op 6 augustus 2019 heeft Intel details vrijgegeven over een kwetsbaarheid in de Windows kernel die informatie openbaar maakt. Deze kwetsbaarheid is een variant van de Spectre Variant 1 speculatieve executie side channel kwetsbaarheid en is toegewezen aan CVE-2019-1125.

**Uitgevoerd op 12 november 2019** Op 12 november 2019 heeft Intel een technische waarschuwing gepubliceerd over het Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort kwetsbaarheid die is toegewezen aan CVE-2019-11135. Microsoft heeft updates uitgebracht om deze kwetsbaarheid te helpen verminderen en de OS-beschermingen zijn standaard ingeschakeld voor Windows Client OS Editions.

## Aanbevolen acties
Klanten moeten de volgende acties ondernemen om zich tegen de kwetsbaarheden te beschermen:

- Pas alle beschikbare Windows-besturingssysteemupdates toe, inclusief de maandelijkse Windows-beveiligingsupdates.
- Pas de toepasselijke firmware-update (microcode) toe die door de fabrikant van het apparaat wordt geleverd.
- Evalueer het risico voor uw omgeving op basis van de informatie in de Microsoft Security Advisories: ADV180002, ADV180012, ADV190013 en de informatie in dit Knowledge Base-artikel.
- Neem de nodige maatregelen aan de hand van de adviezen en de informatie over de registersleutel in dit kennisbankartikel.

## Download de vereiste bestanden:

Download de vereiste bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Hoe voer je het script uit:

**Het script kan worden gelanceerd vanaf de uitgepakte GitHub-download als volgt:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
