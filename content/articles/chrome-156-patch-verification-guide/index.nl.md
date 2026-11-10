---
title: "Chrome 156-beveiligingsupdate: controleer de patch van oktober"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Controleer de Chrome 156-beveiligingsrelease van 27 oktober op Windows, macOS, Linux en Android. Vergelijk de geïnstalleerde build, voltooi een openstaande herstart en controleer beheerde apparaten afzonderlijk."
genre: ["Browsers", "Beveiliging", "Patchbeheer"]
tags: ["Chrome 156", "Chrome-beveiligingsupdate", "Chrome-patch controleren", "Chrome-versie controleren", "Chrome 156 voor Windows", "Chrome 156 voor macOS", "Chrome 156 voor Linux", "Chrome 156 voor Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "browserpatches", "Chrome Enterprise Core", "beheerde browsers", "Chromium-beveiliging", "browserupdates", "Chrome herstarten", "chrome://version", "chrome://settings/help", "Chrome-update voor Android", "Brave-beveiligingsupdates", "Edge-beveiligingsupdates"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Illustratie van een hangslot en schild als symbool voor een beveiligingsupdate, niet voor een Chrome-versiescherm"
coverCaption: ""
---

**De Chrome-beveiligingsrelease van 27 oktober 2026** bevat 52 oplossingen. Vergelijk de volledige versie met de release voor je besturingssysteem en herstart Chrome om een openstaande update af te ronden. Een aangekondigde versie bewijst niet dat je apparaat de update heeft ontvangen. ([Chrome-release voor desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Welke versie hoort zichtbaar te zijn?

Google publiceerde deze Stable-kanaalversies op 27 oktober 2026. De desktoprelease noemt aparte builds voor Windows en macOS en voor Linux. De [Android-release](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) noemt een eigen build en zegt dat Android-releases dezelfde beveiligingsoplossingen bevatten als de overeenkomstige desktopreleases, „tenzij anders vermeld”.

| Platform | Build uit de Google-aankondiging van 27 oktober |
|---|---|
| **Windows** | 156.0.8078.73 of 156.0.8078.74 |
| **macOS** | 156.0.8078.73 of 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Gebruik deze tabel voor de release van 27 oktober, niet als permanent versiedoel. Raadpleeg de actuele [Chrome Releases-feed](https://chromereleases.googleblog.com/) voor latere beveiligingsupdates.* Google zei dat de desktopuitrol „de komende dagen of weken” zou duren en dat de Android-build binnen enkele dagen via Google Play beschikbaar zou komen. Ook tijdens een gefaseerde uitrol moet je een apparaat controleren als de versie lager is dan in de tabel. ([Desktopmelding](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [Android-melding](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

De [lijst met beveiligingsoplossingen voor desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) classificeert vier gemelde fouten als **Critical**: geheugenbeschadiging in FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), onjuiste invoervalidatie in FileAPI CVE-2026-118331, onjuiste invoervalidatie in Skia CVE-2026-118348 en use-after-free in Layout CVE-2026-118344. Dezelfde melding vermeldt meer CVE's met de classificaties **High** en **Medium**. Het getal 52 staat voor de beveiligingsoplossingen in deze release, niet voor 52 onafhankelijk bevestigde exploitmeldingen. ([NVD-vermelding](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**De releasemelding beweert niet dat de genoemde kwetsbaarheden actief worden misbruikt.** De waarschuwing gaat over het moment van openbaarmaking: „Toegang tot bugdetails en links kan beperkt blijven totdat de meeste gebruikers een oplossing hebben ontvangen.” Beschouw beperkte toegang tot bugdetails niet als bewijs van misbruik. ([Desktopmelding](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Controleer en voltooi de desktopupdate

1. Open **`chrome://version`** in de Chrome-installatie die je gebruikt. Noteer de volledige versie en het besturingssysteem, niet alleen het hoofdversienummer 156. Controleer een Chrome-venster van een ander kanaal of een andere installatie afzonderlijk.
2. Open **`chrome://settings/help`** of kies **Meer > Help > Over Google Chrome**. Google zegt dat Chrome op deze pagina naar updates zoekt. Wacht tot de controle is voltooid. ([Google-instructies voor desktopupdates](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Kies **Opnieuw starten** als de pagina die optie toont. Sla eerst je openstaande werk op. Sluit alle andere Chrome-vensters, open de browser opnieuw en controleer **`chrome://version`** nogmaals. Vergelijk de versie na de herstart met de platformtabel.
4. Is de versie nog lager dan de aangekondigde build, controleer dan opnieuw op updates. Beheert een organisatie de browser of meldt het updateprogramma een fout, neem dan contact op met de beheerder. Een geslaagde download bewijst niet dat de actieve browserversie is gewijzigd.

> **Verwacht resultaat:** Na de herstart voldoet de actieve Stable-build van Chrome aan de platformversie in de aankondiging van 27 oktober of aan een later door de leverancier aangekondigde versie. Een knop Opnieuw starten die nog wacht, is geen bewijs dat de update is voltooid.

Open op **Android** Play Store > profielpictogram > Apps en apparaat beheren. Werk Chrome bij onder Updates beschikbaar als de update daar staat. Open in Chrome Meer > Instellingen > Over Chrome om de geïnstalleerde versie te bekijken. Vergelijk die versie met de Android-rij nadat de app-update is voltooid. Deze menupaden volgen de [Android-instructies van Google](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Beheerde browserparken controleren

Gebruik voor ingeschreven browsers het **Chrome-versierapport** in de Google Admin-console om oudere builds per besturingssysteem te vinden. Open de weergave Browser Versions, selecteer de relevante organisatie-eenheid, controleer het volledige subversienummer en exporteer het CSV-bestand als je een werklijst per apparaat nodig hebt. Volgens Google bevat het rapport browsers die in de afgelopen 28 dagen hebben gerapporteerd. Google waarschuwt voor mogelijke vertraging, vooral bij grote parken. ([Chrome-versiegegevens bekijken](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Houd gerapporteerde inventaris apart van liveverificatie.** Controleer de tijd van de laatste rapportage en het kanaal van elk apparaat. Bevestig afwijkingen daarna rechtstreeks in de browser of via je inventaris van beheerde endpoints. Google telt afzonderlijke Chrome-installaties, zoals Stable en Beta, apart. Browserrapportage vereist inschrijving en [rapportage van beheerde browsers](https://support.google.com/chrome/a/answer/9301421?hl=en). Dat een apparaat ontbreekt in het rapport bewijst niet dat het is bijgewerkt.

## Chromium-afgeleiden apart controleren

**De Chrome-versietabel geldt voor Google Chrome.** Microsoft Edge, Brave en andere op Chromium gebaseerde browsers hebben eigen pakketten, releasenummers en updateschema's. De Chrome-aankondiging bevestigt hun patchstatus niet. Controleer de geïnstalleerde versie van elke browser en de eigen beveiligingsmelding of releasenotities voor de relevante Chromium-oplossingen. Vergelijk een Edge- of Brave-versie niet rechtstreeks met Chrome 156.0.8078.73 om te concluderen dat deze is bijgewerkt.

Noteer voor elke afgeleide browser de productnaam, het kanaal, de geïnstalleerde build, de URL van de leveranciersmelding en de build die volgens de leverancier is opgelost. Heeft de leverancier geen oplossing bevestigd, markeer de status dan als **niet geverifieerd** en volg de update-instructies van die leverancier. Houd Chrome en afgeleide browsers in aparte inventarisregels.

## Bronnen en verwijzingen

- [Chrome Releases: Stable Channel-update voor desktop, 27 oktober 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Desktopbuilds, 52 oplossingen, CVE's en tekst over openbaarmaking van de leverancier.
- [Chrome Releases: Chrome-update voor Android, 27 oktober 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Android-build en voorbehoud over overeenkomstige desktopoplossingen.
- [Chromium-issue-tracker: zoekopdracht naar M156-beveiligingsoplossingen](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Link uit de desktopmelding. Toegang tot afzonderlijke foutdetails hangt af van openbaarmakingsbeperkingen.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) en [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Beschrijvingen van kwetsbaarheden en getroffen Chrome-versies. De bovenstaande ernstniveaus volgen de Google-melding, niet een NVD-CVSS-beoordeling.
- [Google Chrome Help: Chrome op computers updaten](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) en [op Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Updatecontrole en menupaden om de versie te bekijken.
- [Chrome Enterprise Help: Chrome-versiegegevens bekijken](https://support.google.com/chrome/a/answer/10025748?hl=en) en [rapportage van beheerde browsers inschakelen](https://support.google.com/chrome/a/answer/9301421?hl=en). Vereisten en beperkingen van rapportages over browserparken.
