---
title: "Vind je BitLocker-herstelsleutel vóór je Windows opnieuw installeert"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Zoek en controleer de juiste BitLocker-herstelsleutel, beveilig een aparte reservekopie en kies de juiste Windows-herstel- of herinstallatieroute voordat je een schijf wist."
genre: ["Windows-beveiliging", "Gegevensherstel", "Systeembeheer"]
tags: ["BitLocker-herstelsleutel", "Windows 11 opnieuw installeren", "Windows 10 opnieuw installeren", "apparaatversleuteling", "herstelsleutel-ID", "herstelsleutel van Microsoft-account", "herstelsleutel werk- of schoolaccount", "herstelsleutel back-uppen", "versleutelde schijf", "schone installatie", "Windows-herstel", "BitLocker-back-up", "48-cijferige herstelsleutel", "Windows-installatiemedium", "gegevensback-up", "schijfversleuteling", "herstelchecklist", "Windows-installatie", "BitLocker-problemen oplossen", "voorbereiding op herinstallatie"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Een laptop met een vergrendelde schijf, een aparte kaart met herstelsleutel, een USB-back-up en een afgevinkte herstelchecklist."
coverCaption: "Controleer de herstelsleutel voordat je de schijf wist."
---

Een schone Windows-installatie wist de geselecteerde schijf. Als de oude schijf **BitLocker** of **Apparaatversleuteling** gebruikt, zoek dan eerst de herstelsleutel en kopieer je bestanden. De sleutel geeft toegang tot de oude versleutelde gegevens. Een nieuwe Windows-installatie zet gewiste bestanden niet terug.

<!--more-->

## Belangrijkste punten

- **Vind de juiste sleutel:** vergelijk de herstelsleutel-ID van Windows met de sleutel in je account, op papier of op een USB-back-up.
- **Test de toegang:** controleer de back-up, vergelijk de ID en ontgrendel een vergrendelde schijf voordat je partities wist.
- **Beveilig de back-up:** bewaar de 48-cijferige sleutel apart van de computer en installatie-USB.
- **Kies de juiste route:** gebruik herstelopties als je de oude installatie nodig hebt. Kies pas voor een schone installatie nadat je een aparte kopie van je bestanden hebt gecontroleerd.

## Voordat je begint

Je hebt toegang nodig tot de betreffende computer, een tweede apparaat om je account of back-up te controleren en een externe schijf of vertrouwde cloudopslag voor belangrijke bestanden. **Tijd:** de sleutel opzoeken hangt af van je accounttoegang. Bestanden kopiëren hangt af van de hoeveelheid gegevens. **Moeilijkheid:** eenvoudig voor accountcontrole, gemiddeld voor herstelprogramma's. Deze gids behandelt de voorbereiding en herstelkeuzes voor Windows 10 en Windows 11. De [gids voor een schone Windows-installatie](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) behandelt installatiemedia en de installatie.

*De standaardondersteuning voor Windows 10 eindigde op 14 oktober 2025. Plan een ondersteunde Windows 11-installatie als je apparaat aan de vereisten voldoet. Microsoft beschrijft de [levenscyclus van Windows 10 en opties voor uitgebreide ondersteuning](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Waarschuwing:** verwijder geen partitie om een BitLocker-herstelprompt op te lossen als je nog bestanden van de oude installatie nodig hebt. Microsoft zegt dat een reset zonder herstelsleutel die bestanden verwijdert. Zie [Microsofts uitleg over herstelsleutels](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Controleer of versleuteling actief is

**Apparaatversleuteling** en **BitLocker** versleutelen een schijf zodat iemand zonder de juiste gegevens de inhoud niet kan lezen. Als Windows nog start, open je in Windows 11 **Instellingen > Privacy en beveiliging > Apparaatversleuteling**. Zoek op edities met BitLocker-beheer in Start naar **BitLocker beheren**. Noteer de stationsletter van de versleutelde schijf en het account waarmee het apparaat is ingesteld. Bij een beheerd werk- of schoolapparaat bewaart je organisatie de sleutel vaak.

Je kunt de status ook via de opdrachtregel controleren. Zoek in Start naar **Opdrachtprompt**, kies **Als administrator uitvoeren** en voer deze opdrachten uit. Vervang `C:` als Windows een andere stationsletter gebruikt. Een **protector** is een methode waarmee Windows een versleutelde schijf ontgrendelt.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

De eerste opdracht toont de versleuteling, beveiliging en vergrendelingsstatus. De tweede toont protectortypen en ID's en kan het herstelwachtwoord weergeven. Microsoft documenteert beide controles in de [BitLocker-handleiding voor beheer](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) en de [referentie voor de statusopdracht](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **Plak de uitvoer niet in een hulpvraag en deel geen schermafbeelding ervan.** Is het apparaat al vergrendeld, gebruik dan de ID op het herstelscherm. De eerste acht cijfers van de ID helpen je de juiste sleutel te kiezen.

## Waar vind je de BitLocker-herstelsleutel?

De **herstelsleutel-ID** wijst een opgeslagen sleutel aan. De **herstelsleutel** is het aparte getal van 48 cijfers dat je invoert om de schijf te ontgrendelen. Vul de ID niet in bij het veld voor het herstelwachtwoord.

| Apparaat of back-up | Waar zoeken |
|---|---|
| **Persoonlijk Microsoft-account** | Meld je op een tweede apparaat aan via [Microsofts route voor herstelsleutels](https://aka.ms/myrecoverykey). Vergelijk de ID voordat je de sleutel van 48 cijfers gebruikt. |
| **Werk- of schoolapparaat** | Controleer je organisatieaccount via [Microsofts route voor werk- of schoolaccounts](https://aka.ms/aadrecoverykey), of vraag het aan je IT-team. |
| **Afdruk of USB-back-up** | Zoek de afdruk of het tekstbestand dat bij het inschakelen van versleuteling is gemaakt. Vergelijk de sleutel-ID met die op het scherm. |

Microsoft noemt deze locaties bij [De BitLocker-herstelsleutel vinden](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Begin met de sleutel waarvan de ID overeenkomt met de prompt. Een sleutel van een ander apparaat of een verwijderde protector ontgrendelt dit volume mogelijk niet. Als iemand anders het apparaat heeft ingesteld, kan de sleutel volgens Microsoft in diens account staan.

## Maak een aparte back-up van de sleutel

Als Windows nog start op een Pro-, Enterprise- of Education-editie, zoek je naar **BitLocker beheren**. Kies naast de versleutelde schijf **Back-up maken van je herstelsleutel**. Microsoft biedt een back-up naar een account, USB-schijf, tekstbestand of afdruk. Bewaar een tekstbestand of USB alleen op versleutelde media met toegangscontrole, apart van de computer. Gebruik geen onversleutelde locatie. Lees [Een back-up maken van je BitLocker-herstelsleutel](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key) voor de huidige interface en opties.

In Windows Home ontbreekt **BitLocker beheren**. Controleer in Windows 11 **Instellingen > Privacy en beveiliging > Apparaatversleuteling** en verifieer de sleutel in het Microsoft-account dat bij de installatie is gebruikt. Microsoft legt uit dat [Apparaatversleuteling](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) de sleutel bij activering in het gekoppelde Microsoft- of werkaccount opslaat. Bewaar een aparte beveiligde kopie als je installatie een exportmethode biedt.

Open een digitale back-up op een tweede apparaat. Vergelijk een papieren afdruk met het account of het herstelscherm. Vergelijk de **herstelsleutel-ID** met die op het herstelscherm of in de lijst met protectors. Controleer of alle 48 cijfers van de bijbehorende sleutel aanwezig zijn. Bewaar een afdruk of verwijderbare kopie uit de buurt van de versleutelde computer. Iemand die zowel de computer als de sleutel steelt, kan de schijfbeveiliging omzeilen, waarschuwt Microsoft in de [back-upinstructies](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). Voeg de sleutel niet toe aan een supportticket.

> **Verwacht resultaat:** je hebt een overeenkomende herstelsleutel buiten de computer beschikbaar.

## Ontgrendel een pc die niet opstart

Verschijnt het **BitLocker-herstelscherm**, voer dan de 48-cijferige sleutel in die bij de ID hoort. Start Windows daarna, kopieer je bestanden voordat je partities wijzigt. Ontgrendelt de sleutel de schijf maar start Windows nog steeds niet, gebruik dan de [Windows-herstelomgeving](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) en probeer **Opstartherstel** voordat je een reset uitvoert. Sommige herstelprogramma's vragen om de sleutel zolang de schijf versleuteld is.

Voor een bestandsback-up vanuit herstelprogramma's open je **Problemen oplossen > Geavanceerde opties > Opdrachtprompt** in de Windows-herstelomgeving. Gebruik `manage-bde -status` en `dir` om het versleutelde Windows-volume en een aparte externe back-upschijf te vinden. **Stationsletters kunnen afwijken van de normale Windows-letters.** Kopieer niet naar de installatie-USB of de versleutelde bronschijf.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

De letters zijn voorbeelden. Ontgrendel het Windows-volume met de overeenkomende sleutel nadat je de juiste volumes hebt gevonden. Vervang de voorbeeldletter en tijdelijke waarde door je eigen gegevens. Typ de echte sleutel van 48 cijfers lokaal. Publiceer of deel de uitvoer niet.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

De optie `-recoverypassword` neemt de sleutel van 48 cijfers als argument. Daardoor kan de sleutel in de shellgeschiedenis, transcripties en procesinspectie terechtkomen. Gebruik het Windows-herstelscherm als je de sleutel zonder opdrachtregelargument wilt invoeren. Heb je een aparte `.bek`-sleutelbestand opgeslagen, dan vermijdt `-recoverykey <path-to-external-bek>` het intypen van de 48 cijfers. Houd de sleutel buiten schermafbeeldingen en supporttickets.

Microsoft documenteert de [ontgrendelopdracht](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). De [herstelrichtlijnen](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) beschrijven ook hoe je gebruikersbestanden na ontgrendeling naar een andere schijf kopieert. Voor een voorbeeld van het kopiëren van Documenten controleer je eerst de accountnaam en externe stationsletter. Vervang daarna beide paden:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

De opties **`/S /E`** nemen submappen mee, ook lege. **`/I`** behandelt de bestemming als map, **`/H`** neemt verborgen bestanden mee en **`/V`** controleert elk geschreven bestand. Microsoft documenteert deze opties in de [xcopy-referentie](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Herhaal dit voor andere benodigde mappen. Open gekopieerde bestanden op een ander apparaat voordat je de Windows-schijf wist. Lukt het niet om volumes te herkennen of mislukt het kopiëren, stop dan en schakel een vertrouwde herstelspecialist in.

## Beslis of je opnieuw installeert

**Een back-up van de sleutel is geen bestandsback-up.** Volg deze volgorde voordat je een herinstallatieroute kiest:

1. Identificeer de versleutelde schijf en de bijbehorende herstelsleutel-ID.
2. Haal de overeenkomende sleutel van 48 cijfers op uit je account, afdruk of USB-back-up.
3. Ontgrendel een vergrendelde schijf via het herstelscherm of herstelprogramma.
4. Kopieer Bureaublad, Documenten, Afbeeldingen en andere lokale mappen naar een externe schijf of vertrouwde cloudopslag. Neem zo nodig browserexports, toepassingsgegevens en licentiegegevens mee.
5. Open enkele gekopieerde bestanden vanaf een tweede apparaat.
6. Kies pas een reparatie-, reset- of herinstallatiemethode nadat je de back-up hebt gecontroleerd.

> **Verwacht resultaat:** je hebt buiten de oude Windows-installatie toegang tot de passende sleutel en belangrijke bestanden.

Microsoft beschrijft [Windows-herstelopties](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows) en hun verschillende gevolgen voor bestanden en apps. Veel opties in de Windows-herstelomgeving vragen om de sleutel als BitLocker de schijf beschermt. Is het volume daar vergrendeld, dan ontgrendelt **Mijn bestanden behouden** het niet zonder sleutel.

**Opstartherstel** en **Systeemherstel** proberen de bestaande installatie te repareren. **Deze pc opnieuw instellen** heeft een optie **Mijn bestanden behouden**, maar verwijdert apps en instellingen. **Alles verwijderen** wist persoonlijke bestanden. Als je **`setup.exe` vanuit een actieve Windows-sessie start**, kun je opnieuw installeren en opties kiezen om gegevens te behouden. **Windows installeren** starten vanaf installatie-USB volgt een schone installatieroute die bestanden, apps en instellingen van de geselecteerde Windows-installatie verwijdert. Hetzelfde medium biedt ook een reparatieroute. Lees de weergegeven optie en doelschijf voordat je een reset of installatie bevestigt. Microsoft legt beide routes uit in de [herinstallatie-instructies](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Situatie | Volgende stap |
|---|---|
| **Windows start en je hebt de bestanden nodig** | Maak een bestandsback-up, controleer de herstelsleutel en kies daarna een reparatie- of herinstallatiemethode. |
| **Windows vraagt om de sleutel** | Vergelijk de ID op het scherm met een opgeslagen sleutel voordat je de schijf wijzigt. |
| **Geen overeenkomende sleutel en geen bestandsback-up** | Stop voordat je de schijf wist. Controleer elk account, elke afdruk en USB-back-up, en vraag je IT-team. |
| **Bestanden zijn geback-upt en je wilt opnieuw beginnen** | Volg Microsofts [herinstallatie-instructies](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) en kies zorgvuldig de gewenste doelschijf. |

Microsoft zegt dat supportmedewerkers een verloren herstelsleutel niet kunnen reconstrueren. Vind je de sleutel niet, wijzig dan geen firmware-instellingen meer en controleer alle back-uplocaties. Vraag bij een beheerd apparaat hulp aan de beheerder. Een reset zonder benodigde sleutel verwijdert de oude bestanden. Een schone installatie verwijdert ook persoonlijke bestanden, apps, apparaataanpassingen en instellingen van de geselecteerde installatie. Maak die keuze bewust nadat je de back-up hebt gecontroleerd.

## Problemen oplossen

- **De sleutel werkt niet:** controleer opnieuw de sleutel-ID en het account. Een apparaat kan meer dan één opgeslagen herstelsleutel hebben.
- **BitLocker beheren ontbreekt:** Windows Home gebruikt op geschikte apparaten Apparaatversleuteling. Controleer Instellingen en het Microsoft-account dat bij de installatie is gebruikt.
- **Er staan meerdere sleutels in één account:** vergelijk de eerste acht cijfers van de ID op het herstelscherm met de opgeslagen items. Kies geen sleutel alleen op basis van een apparaatnaam.
- **De sleutel ontgrendelt de schijf, maar Windows start niet:** probeer Opstartherstel vanuit de Windows-herstelomgeving. Maak een back-up van toegankelijke bestanden voordat je reset of opnieuw installeert.
- **Werk of school bewaart de sleutel:** neem vóór een reset of herinstallatie contact op met de apparaatbeheerder.
- **Het sleutelbestand staat op de vergrendelde computer:** zoek naar een apart account, een afdruk of verwijderbare back-up. Een kopie die alleen op de versleutelde schijf staat helpt niet zolang die vergrendeld is.
- **De herstelprompt verscheen na een firmwarewijziging:** noteer de wijziging en voer geen verdere firmwarewijzigingen uit. Zoek de passende sleutel of neem contact op met de beheerder.

## Volgende stappen

Nadat je de sleutel en bestanden hebt gecontroleerd, volg je de [gids voor een schone Windows-installatie](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) als dat bij je doel past. Controleer na het starten van Windows **Instellingen > Privacy en beveiliging > Apparaatversleuteling** of zoek naar **BitLocker beheren**. Kies op Pro, Enterprise of Education **Back-up maken van je herstelsleutel** in BitLocker beheren. Controleer op Home of het gekoppelde account de huidige sleutel bevat en bewaar een aparte kopie als Windows een exportoptie biedt. Ga er niet van uit dat de oude sleutel bij een nieuw versleutelde installatie hoort.
