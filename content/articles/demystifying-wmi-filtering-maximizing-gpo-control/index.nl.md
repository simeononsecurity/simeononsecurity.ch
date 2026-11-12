---
title: "WMI-filtering begrijpen"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Leer hoe je met WMI-filtering Group Policy Objects (GPO's) op de juiste computers toepast, met praktische voorbeelden en aanbevolen werkwijzen."
genre: ["Windows-beheer", "Groepsbeleid", "Systeembeheer", "Netwerkbeheer", "IT-infrastructuur", "Beleidsbeheer", "IT-governance", "IT-automatisering", "Active Directory", "Beveiligingsnaleving"]
tags: ["WMI-filtering", "GPO", "Group Policy Objects", "WMI-filters", "beleidsdoelen", "WMI-query's", "Windows Management Instrumentation", "GPO-beheer", "Group Policy Management Console", "WMI Query Language", "beleidsuitvoering", "WQL", "beleid verfijnen", "beleidsbeheer", "systeembronnen", "voorbeelden van beleidsdoelen", "systeembeheer", "netwerkbeheer", "IT-infrastructuurbeheer", "IT-automatisering", "Active Directory-beheer", "beveiligingsnaleving", "technieken voor beleidsbeheer", "aanbevolen werkwijzen voor beleidsbeheer", "beleidsfiltering", "GPO-beheerstrategieën", "GPO-beveiliging", "voordelen van WMI-filtering", "WMI-filtering implementeren", "aanbevolen werkwijzen voor WMI-filters"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Illustratie van een vergrootglas dat op een filterpictogram is gericht en GPO-doelselectie met WMI-filtering weergeeft."
coverCaption: "Gebruik WMI-filtering om GPO-beleid efficiënt op de juiste doelen toe te passen."
---

## Inleiding

In Group Policy Objects (GPO's) bepaalt [**WMI-filtering**](https://simeononsecurity.com/github/wmi-filters/) op welke computers of gebruikers beleid wordt toegepast, op basis van resultaten van WMI-query's (Windows Management Instrumentation). Beheerders kunnen zo de beleidsdoelen verfijnen en beleid alleen op de bedoelde systemen toepassen. Dit artikel bespreekt WMI-filtering, de werking ervan binnen GPO's, het maken van [WMI-filters](https://simeononsecurity.com/github/wmi-filters/) en praktische voorbeelden.

## [Wat is WMI-filtering?](https://simeononsecurity.com/github/wmi-filters/)

[**WMI-filtering**](https://simeononsecurity.com/github/wmi-filters/) past filters op GPO's toe op basis van de resultaten van WMI-query's. WMI is een beheerinfrastructuur die in Windows is ingebouwd. Beheerders kunnen er beheergegevens mee ophalen en programmatisch met systeembronnen werken. Met WMI-filtering kunnen zij GPO's dynamisch richten op systemen die aan bepaalde querycriteria voldoen.

WMI-filters worden geschreven in de WMI Query Language (WQL), een subset van SQL (Structured Query Language). Ze zijn doorgaans gebaseerd op eigenschappen en waarden in een WMI-naamruimte. Beheerders kunnen voorwaarden, logische operatoren en naamruimten combineren om complexe query's te maken die specifieke computers of gebruikers selecteren.

## Hoe werkt WMI-filtering in GPO's?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Stroomschema waarin een WMI-filter aan een Group Policy Object een WQL-query als True of False beoordeelt om te bepalen of de GPO op een doelcomputer wordt toegepast" >}}

Met **WMI-filtering** kunnen beheerders GPO's selectief toepassen op basis van de beoordeling van **WMI-query's**. Wanneer je een **WMI-filter** aan een GPO koppelt, bepaalt het resultaat **True** of **False** of de GPO wordt toegepast.

WMI-filters gebruiken de **WMI Query Language (WQL)**, een subset van SQL. Met WQL kun je complexe query's opstellen die verschillende **eigenschappen** en **waarden** in een **WMI-naamruimte** meenemen. Zo kun je specifieke computers of gebruikers selecteren.

Een organisatie wil bijvoorbeeld een GPO alleen toepassen op computers met Windows 10. Daarvoor kan een WMI-filter de eigenschap **OperatingSystem** van de klasse **Win32_OperatingSystem** controleren. De query kan er zo uitzien:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

De query controleert of de versie van het besturingssysteem met "10." begint, wat Windows 10 aanduidt. Als de query **True** oplevert, wordt de GPO op de doelcomputer toegepast. Anders gebeurt dat niet.

WMI-filtering ondersteunt ook voorwaarden en logische operatoren zoals **AND**, **OR** en **NOT**. Beheerders kunnen verschillende eigenschappen en waarden combineren om GPO-toepassing nauwkeuriger te sturen.

Daarnaast bieden verschillende **WMI-naamruimten** toegang tot specifieke sets WMI-klassen en -eigenschappen. Daarmee kun je GPO's richten op hardwareconfiguraties, geïnstalleerde software, netwerkinstellingen en andere criteria.

Raadpleeg de Microsoft-documentatie over [WMI-filtering voor groepsbeleid](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo) voor meer informatie over WMI-filters en -query's.

WMI-filtering helpt beheerders GPO's op basis van dynamische voorwaarden af te stemmen op computers of gebruikers en zo de IT-omgeving beter te beheren.

## WMI-filters voor GPO's maken

Volg deze stappen om een WMI-filter voor een GPO te maken:

1. Open op een Windows-computer die lid is van het domein de **Group Policy Management Console** (GPMC).

2. Vouw het domein uit en open het knooppunt **WMI Filters**.

3. Klik met de rechtermuisknop op **WMI Filters** en selecteer **New**.

4. Geef het filter een duidelijke naam en voer de WMI-query in het veld **Query** in. Gebruik de WQL-syntaxis.

5. Klik op **OK** om het WMI-filter op te slaan.

Na het maken kun je het filter aan een of meer GPO's koppelen. Zo koppel je het aan een GPO:

1. Klik met de rechtermuisknop op de gewenste GPO en selecteer **Properties**.

2. Open in het eigenschappenvenster van de GPO het tabblad **WMI Filtering**.

3. Selecteer het gewenste WMI-filter in de lijst.

4. Klik op **OK** om de wijzigingen op te slaan.

Door WMI-filters aan GPO's te koppelen, stem je de beleidsuitvoering nauwkeurig af op de resultaten van WMI-query's.

## Hoeveel WMI-filters kun je voor een GPO instellen?

Beheerders kunnen **meerdere WMI-filters** voor een GPO instellen om beleid nauwkeurig op doelen af te stemmen. Er geldt geen specifiek maximum voor het aantal filters dat aan één GPO kan worden gekoppeld, waardoor complexe combinaties mogelijk zijn.

Houd wel rekening met de invloed van het aantal filters op de verwerkingstijd van GPO's. Hoe meer filters er zijn, hoe langer het beoordelen en toepassen van GPO's kan duren. Beperk het aantal daarom tot een redelijk niveau om beleid efficiënt toe te passen.

Stel dat een organisatie een GPO alleen wil toepassen op computers met Windows 10 waarop een bepaald programma is geïnstalleerd. Dan kunnen twee afzonderlijke WMI-filters worden gemaakt: een voor het **besturingssysteem** en een voor de **software-installatie**. Samen selecteren ze de juiste computers.

Zoek een balans tussen voldoende filters voor de gewenste doelselectie en een aanvaardbare verwerkingstijd. Beoordeel vooraf de complexiteit van de omgeving, het aantal computers of gebruikers en de mogelijke invloed op de prestaties.

Meerdere WMI-filters helpen de doelselectie van GPO's te verbeteren en houden de verwerking en het beheer van de IT-omgeving efficiënt.

## Praktische voorbeelden van WMI-filtering in GPO's

WMI-filtering maakt gerichte toepassing van GPO's mogelijk. Enkele voorbeelden:

1. **Specifieke besturingssystemen selecteren**: maak een filter dat de OS-versie controleert om een GPO alleen op **Windows 10**-computers toe te passen. Bijvoorbeeld `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. Hiermee selecteer je Windows 10-computers.

2. **Verschillend beleid voor desktops en laptops**: gebruik twee WMI-filters als je voor desktops en laptops ander beleid hebt. Het ene filter kan desktops herkennen aan hardwarekenmerken, bijvoorbeeld `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, en het andere laptops. Zo krijgt elk apparaattype passend beleid.

3. **Beleid selecteren op basis van schijfruimte**: maak een filter dat beschikbare schijfruimte controleert om resource-intensief beleid niet toe te passen op computers met weinig ruimte. De query `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` sluit bijvoorbeeld computers met minder dan 10 GB vrije ruimte uit.

Deze voorbeelden tonen de flexibiliteit van **WMI-filtering** in GPO's. Beheerders kunnen beleidsuitvoering op specifieke criteria richten.

## Conclusie

WMI-filtering is een nuttige functie van Group Policy Objects. Beheerders kunnen beleid selectief toepassen op basis van de resultaten van WMI-query's. WMI-filters richten beleid nauwkeurig op bepaalde computers of gebruikers, voor efficiënter en beter beheersbaar beleid. Dit artikel besprak het concept, de werking in GPO's, het maken van filters en praktische voorbeelden.

Door WMI-filtering in je GPO-beheer op te nemen, verbeter je de nauwkeurigheid en zorg je dat beleid alleen op de bedoelde doelen wordt toegepast.

## Referenties

- [Microsoft Docs: WMI-filters voor de GPO maken](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: groepsbeleid](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Group Policy Management Console](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
