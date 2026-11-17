---
title: "Test een herstelproef voor homelabback-ups met Restic"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Controleer of een homelabback-up bruikbare bestanden herstelt. Bepaal een hersteldoel, herstel met Restic naar een aparte locatie, controleer de gegevens en leg het resultaat vast."
genre: ["Homelab", "Back-up", "Noodherstel"]
tags: ["homelabback-up", "herstelproef", "Restic-herstel", "back-upcontrole", "hersteltest", "noodherstel", "RPO", "RTO", "back-uprepository", "Restic-controle", "NAS-back-up", "serverback-up", "VM-herstel", "bestandsherstel", "back-upversleuteling", "back-upbewaking", "herstelplan", "back-uptest", "externe back-up", "gegevensintegriteit"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Een homelabserver en NAS maken een back-up naar een aparte schijf, met een gecontroleerde herstelmap op een geïsoleerde testcomputer en een stopwatch."
coverCaption: "Herstel naar een aparte bestemming, controleer de gegevens en meet de benodigde tijd."
---

Een back-uptaak die als geslaagd wordt gemeld, bewijst niet dat je een bruikbaar bestand kunt herstellen. Een **herstelproef** test het traject van opgeslagen back-up naar werkende gegevens zonder je actieve bestanden te vervangen. Deze handleiding gebruikt Restic voor een voorbeeld op bestandsniveau en biedt een verslag dat je na wijzigingen aan je lab opnieuw kunt invullen.

<!--more-->

Restic is een back-upprogramma. Een **repository** is de beveiligde opslagruimte met back-upgegevens. Een **snapshot** is een opgeslagen back-uppunt.

## Belangrijkste punten

- **Kies een doel:** Bepaal welke bestanden of service je moet herstellen en stel een aanvaardbaar herstelpunt en tijdsduur vast.
- **Herstel apart:** Gebruik een lege testbestemming zodat de proef geen actieve gegevens overschrijft.
- **Controleer het resultaat:** Open herstelde bestanden, controleer waar mogelijk toepassingsgegevens en meet de verstreken tijd.
- **Leg fouten vast:** Noteer de snapshot-ID, ontbrekende onderdelen, rechten en herstelacties in je herstelplan.

## Voor je begint

Je hebt een werkende back-uprepository nodig, het wachtwoord of de sleutel ervan, voldoende vrije ruimte op de bestemming en leesrechten voor de back-up en testlocatie. Dit voorbeeld gaat ervan uit dat Restic is geïnstalleerd en dat de repository een recente bestandsback-up bevat. De [snelstartgids van Restic](https://restic.readthedocs.io/en/stable/010_introduction.html) beschrijft het maken van een repository en de eerste back-ups. De [3-2-1-back-upgids](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) van de site behandelt de plaatsing van kopieën. Het [homelab-overzicht](/articles/what-is-a-homelab-and-should-you-have-one/) bevat een korte checklist voor back-uptests.

Deze proef controleert bestanden in één snapshot. Een database, virtuele machine of toepassing heeft ook eigen herstelstappen nodig. Houd het testsysteem geïsoleerd als het starten van de herstelde service de actieve service kan hinderen. Een geslaagde bestandskopie bewijst niet dat elke service opstart.

> **Waarschuwing:** Herstel voor de eerste test niet naar een actieve locatie. Gebruik een lege testmap op een apart bestandssysteem of testhost. Zet het repositorywachtwoord niet in schermafbeeldingen, tickets of shellgeschiedenis.

## Bepaal het hersteldoel

Noteer wat je na een storing nodig hebt. Het **herstelpuntdoel (RPO)** is het tijdstip tot waarop gegevens na een onderbreking moeten worden hersteld. Het staat voor het maximale aanvaardbare gegevensverlies. Het **hersteltijddoel (RTO)** is hoelang de service niet beschikbaar mag zijn. NIST definieert beide in de [handleiding voor noodplanning](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Je doelen moeten rekening houden met hoe vaak gegevens veranderen en hoe lang herstel op jouw hardware duurt.

| Onderdeel | Voorbeeld van een doel | Vast te leggen |
|---|---|---|
| **Familiedocumenten** | Laatste nachtelijke back-up | Tijdstip van de laatste snapshot en geopende bestanden |
| **Configuratie van een thuisservice** | Laatste wijziging waarvan bekend is dat die werkte | Configuratieversie en vereiste geheimen |
| **Mediabibliotheek op netwerkopslag (NAS)** | Wekelijkse back-up | Afspelen van een voorbeeld en hersteltijd |

De doelen hierboven zijn voorbeelden, geen meetresultaten. Noteer in je herstelplan waar de back-up staat en hoe een bevoegd persoon het repositorywachtwoord of de versleutelingssleutel ophaalt. Zet geen geheime waarden in het plan of verslag. Bewaar geheimen via een beveiligde route die onafhankelijk is van de uitgevallen host. Een repository die overleeft terwijl het enige wachtwoord verloren gaat, is niet herstelbaar.

Kies voor deze proef een **kritieke set bestanden**. Voeg een klein bestand toe waarvan je weet dat het in de nieuwste snapshot hoort te staan. Noteer voor een service ook de configuratie, database-export, certificaten en toepassingsversie die nodig zijn om de service te starten. Controleer of je back-upmethode consistente toepassingsgegevens vastlegt voordat je vertrouwt op een bestandskopie van een draaiende database.

## Zoek een snapshot

Gebruik repositorytoegang die voor de herstelproef is goedgekeurd. Restic gebruikt tijdelijk een repositoryvergrendeling tijdens het lezen of wijzigen van back-upgegevens. De opdrachten hieronder gaan ervan uit dat de repository deze vergrendeling toestaat. Houd de actieve bron en testbestemming gescheiden. Vervang `/path/to/repository` door het echte pad van je Restic-repository en geef de snapshots weer:

```bash
restic -r /path/to/repository snapshots
```

Restic vraagt om het repositorywachtwoord als je het niet via een ingestelde geheimenvoorziening hebt aangeleverd. De [snapshotlijst](https://restic.readthedocs.io/en/stable/010_introduction.html) toont de ID, datum, host en bronpaden. Noteer de snapshot-ID en tijdstempel die je wilt testen. Vergelijk de tijdstempel met je RPO. Een recent taaklogboek vervangt deze controle niet, want de benodigde snapshot kan ouder zijn dan je denkt.

Stop de proef als de verwachte snapshot ontbreekt en onderzoek het back-upschema, de bronselectie en het repositorypad. Kies niet ongemerkt een oudere snapshot en meld niet dat het hersteldoel is gehaald.

## Herstel naar een lege testbestemming

Maak op een testbestandssysteem met voldoende ruimte voor de snapshot een **lege doelmap**. Gebruik als Restic-doel niet de oorspronkelijke bron, een aangekoppelde productieshare of een bestaande map met gegevens die je wilt bewaren. Vervang `SNAPSHOT_ID` en beide voorbeeldpaden voordat je de opdracht uitvoert:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

De [herstelgids van Restic](https://restic.readthedocs.io/en/stable/050_restore.html) beschrijft de snapshot-ID en het pad `--target`. De herstelde mappenstructuur behoudt het bronpad onder de doelmap. Zoek daarom de echte bestanden voordat je het resultaat beoordeelt. Als je alleen een kleine selectie nodig hebt, gebruik dan de gedocumenteerde [inclusiefilters voor herstel](https://restic.readthedocs.io/en/stable/050_restore.html) en noteer wat je hebt uitgesloten. Gebruik `--delete` niet tijdens een proef. Restic meldt dat deze optie bestanden op de bestemming verwijdert die niet in de snapshot voorkomen.

Start een timer wanneer het herstel begint. Stop de timer wanneer de vereiste bestanden aanwezig en bruikbaar zijn, niet zodra het commando voor het eerst voortgang toont. Noteer de repositorylocatie, netwerkverbinding, gegevensgrootte en testhost, omdat die omstandigheden later herstel beïnvloeden.

> **Verwacht resultaat:** De geselecteerde snapshot wordt naar een aparte bestemming hersteld zonder de actieve bron te wijzigen.

## Controleer gegevens en serviceherstel

Open enkele herstelde bestanden met de toepassing die ze normaal gebruikt. Neem een recent bestand, een ouder bestand en een bestand uit een geneste map. Vergelijk bekende groottes of checksums als je die voor de back-up hebt vastgelegd. Controleer op Linux eigenaar en rechten. Een bestand dat leesbaar is voor het testaccount kan nog steeds mislukken voor het serviceaccount.

Herstel een service naar een geïsoleerde testinstantie. Controleer de configuratie, vereiste geheimen, databaseconsistentie, het opstarten en een representatieve gebruikersactie. Een bestandsherstel zonder database of geheim is geen volledig serviceherstel. Start de testinstantie nooit met de actieve database of een productieadres zonder een gecontroleerd omschakelplan.

Voer na het terugzetten van het voorbeeld de Restic-repositorycontrole uit:

```bash
restic -r /path/to/repository check
```

Gebruik `check --read-data` tijdens een onderhoudsvenster om alle repositorygegevens te lezen. Restic waarschuwt dat deze opdracht de hele repository leest en veel gegevens van een externe backend kan downloaden. De [probleemoplossingsgids van Restic](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) beschrijft de controle en de kosten. Een schone controle geeft extra vertrouwen, maar vervangt niet het openen van herstelde bestanden of het starten van de service.

```bash
restic -r /path/to/repository check --read-data
```

Vergelijk de leeftijd van de snapshot met je RPO en de gemeten hersteltijd met je RTO. Als een van beide doelen niet wordt gehaald, is de proef mislukt, ook als Restic geen fout gaf. Pas de back-upfrequentie, opslaglocatie, bandbreedte of herstelprocedure aan en test opnieuw.

## Houd een herstelverslag bij

Schrijf na elke proef een kort verslag. De [back-upmaatregel SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) van NIST noemt het herstellen van steekproeven van systeemfuncties als manier om herstel te testen. Met een herhaalbaar verslag zie je of je plan verbetert.

| Veld | Vast te leggen resultaat |
|---|---|
| **Datum en uitvoerder** | Wanneer de proef plaatsvond en wie haar uitvoerde |
| **Repository en snapshot** | Locatie, ID, tijdstempel en bronpaden |
| **Hersteldoel** | Geteste bestanden of service, plus RPO en RTO |
| **Gemeten resultaat** | Leeftijd snapshot, hersteltijd en controles van bestanden of service |
| **Fouten** | Ontbrekende gegevens, sleuteltoegang, rechten, netwerk- of opstartproblemen |
| **Volgende actie** | Eigenaar, reparatie en datum van volgende test |

Zet het repositorywachtwoord, de herstelsleutel of gevoelige bestandsinhoud niet in het verslag. Bewaar ze in een beveiligde geheimenkluis en leg vast hoe een bevoegd persoon ze tijdens een storing ophaalt.

## Problemen oplossen

- **Wachtwoord ontbreekt:** Controleer de onafhankelijke route voor sleutelbeheer. Ga er niet van uit dat de uitgevallen host zijn eigen sleutel beschikbaar maakt.
- **Snapshot is te oud:** Controleer het schema, mislukte taken, bronpaden en of de verwachte host naar een andere repository heeft geback-upt.
- **Herstel duurt te lang:** Meet de leessnelheid van opslag, netwerkverbinding en gegevensvolume. Test een kleinere kritieke selectie en herzie daarna de RTO of het herstelontwerp.
- **Bestand bestaat, service werkt niet:** Controleer database-exports, toepassingsversie, eigenaar, rechten, certificaten en ontbrekende geheimen.
- **Repositorycontrole meldt fouten:** Bewaar de uitvoer en indien mogelijk een kopie van de repository. Volg de Restic-instructies voor [schadeonderzoek](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) voordat je reparaties probeert.
- **Test heeft actieve gegevens gewijzigd:** Stop de testservice, controleer de productiegegevens en verbeter het isolatieplan voordat je de proef herhaalt.

## Volgende stappen

Herhaal deze proef na wijzigingen aan back-upsoftware, opslag, versleutelingssleutels of kritieke services. Wissel in de loop van de tijd af tussen verschillende bestandensets en volledig serviceherstel. Bewaar een onafhankelijke back-up volgens je [3-2-1-plan](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). Het doel is een gemeten herstel dat je kunt herhalen wanneer de oorspronkelijke host verdwenen is.
