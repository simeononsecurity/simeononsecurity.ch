---
title: "Proxmox VM-hersteltest: bewijs dat de gastmachine werkt"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Test een Proxmox VM-back-up met een geïsoleerd herstel. Controleer schijfdekking, back-upmodus, gastgegevens, servicestatus en hersteltijd zonder productie aan te raken."
genre: ["Virtualisatie", "Back-up en herstel", "Homelab"]
tags: ["Proxmox-hersteltest", "Proxmox VM-back-up", "Proxmox-herstelproef", "qmrestore", "vzdump", "Proxmox Backup Server-controle", "Proxmox-snapshotback-up", "VM-hersteltest", "RPO en RTO van back-ups", "geïsoleerd VM-herstel", "Proxmox-back-upmodus", "back-up met gastagent"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Een back-up gaat van een oranje productie-VM via een opslagkluis naar een blauwe, geïsoleerde test-VM. De schijven, diensten en tijd worden gecontroleerd."
coverCaption: "Een afgeronde back-uptaak is het begin van een hersteltest."
---

Een groene back-uptaak laat zien dat Proxmox een back-up heeft geschreven. De taak laat niet zien of de gast start, de gegevens actueel zijn of de belangrijkste dienst werkt. **Herstel een kopie met een nieuw VM-ID op een geïsoleerd netwerk.** Het resultaat levert bewijs voor herstel voordat een storing je dwingt om te testen.

<!--more-->

Deze proef behandelt één **Proxmox VE-virtuele machine**. Voor containers gelden andere back-upregels, vooral voor bind- en apparaatkoppelingen. De [back-up- en hersteltest voor een homelab](/articles/homelab-backup-restore-drill/) op deze site behandelt uitgebreider bestandsherstel. Hier test je een Proxmox VM-back-up en de bijbehorende werklast.

Een **gast** is het besturingssysteem dat in een virtuele machine draait. **Bindkoppelingen** en **apparaatkoppelingen** geven de gast toegang tot hostbronnen. Test die bronnen met een apart herstelplan.

## Belangrijkste punten

- **Bepaal eerst wanneer de test slaagt:** kies een gegevensitem, een dienstcontrole en een aanvaardbare hersteltijd.
- **Controleer de dekking:** een VM-back-up slaat schijven met **No backup** over en herstelt geen externe diensten of uitgesloten gegevens.
- **Herstel apart:** gebruik een ongebruikt VM-ID en houd het herstelde netwerk gescheiden van productie.
- **Leg bewijs vast:** meet de ouderdom van de back-up, de hersteltijd, het opstarten, aanwezige schijven en een echte toepassingscontrole.

## Voordat je begint

Kies een VM waarvan je de back-up veilig kunt testen. Je hebt Proxmox-beheertoegang nodig, een voltooide back-up op bestandsopslag of Proxmox Backup Server (PBS), genoeg ruimte voor een tweede VM en een geïsoleerde bridge of een losgekoppeld netwerkapparaat. Een geïsoleerde bridge is een virtueel Proxmox-netwerk zonder route naar het productielan. Gebruik een losgekoppelde adapter of test-VLAN als je die bridge niet hebt. Laat de productie-VM draaien. Reserveer een nieuw VM-ID, bijvoorbeeld **920**, nadat je hebt gecontroleerd of een andere gast dat ID gebruikt. Plan genoeg tijd in voor een volledig herstel en een werklasttest.

Schrijf de slaagvoorwaarden op voordat je herstelt. Kies voor een bestandsserver een recent bestand en de verwachte controlesom of inhoud. Kies voor een database een veilige alleen-lezenquery en een record dat vóór de back-up is geschreven. Kies voor een webdienst een lokale statuscontrole en een representatieve pagina. Noteer de meest recente aanvaardbare gegevensdatum, je **Recovery Point Objective (RPO)**, en de tijd waarbinnen de dienst moet herstellen, je **Recovery Time Objective (RTO)**. Alleen een opstartscherm voldoet niet aan deze controles.

| Vastlegging | Voorbeeldbewijs |
|---|---|
| **Back-uppunt** | Tijdstip van de snapshot en het laatste verwachte gegevensitem |
| **Hersteldoel** | Ongebruikt VM-ID, doelopslag en geïsoleerde bridge |
| **Werklasttest** | Aanmelden, volume koppelen en gegevens uit de toepassing lezen |
| **Tijdslimiet** | Begin- en eindtijd van het herstel en de dienstcontrole |

Verbind de herstelde gast pas met het productienetwerk nadat je de naam, het IP-adres, MAC-adres, geplande taken en externe koppelingen hebt gecontroleerd. Een gekopieerde identiteit kan conflicteren met de actieve VM of dubbel werk versturen.

## Controleer wat de back-up bevat

**Versieomvang:** deze voorbeelden zijn niet uitgevoerd tijdens het schrijven van het artikel. Noteer vóór het testen de uitvoer van `pveversion --verbose`. Gebruik documentatie voor de geïnstalleerde Proxmox VE-versie. Noteer de opslagbackend, het gasttype en de opdrachtuitvoer in het testverslag.

Op een Proxmox-knooppunt toont de volgende alleen-lezenopdracht de configuratie van de bron-VM. Vervang **120** door het VM-ID van je bron:

```bash
qm config 120
```

Noteer elke virtuele schijf en de bijbehorende back-upinstelling. De [Proxmox-documentatie over VM-schijven](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) vermeldt dat de optie **No backup** een schijf uitsluit van de VM-back-up. Controleer of toepassingsgegevens op een uitgesloten schijf, hostkoppeling, rechtstreeks doorgegeven hardware of externe dienst staan. Noteer daarvoor de afzonderlijke herstelprocedure. Een VM-opstarttest bewijst niet dat uitgesloten gegevens zijn beveiligd.

Controleer het tijdstip, de grootte, het taaklogboek en de opslaglocatie van de nieuwste back-up. Open in de Proxmox-interface de weergave **Backups** van de back-upopslag of het tabblad **Backup** van de VM. Bevestig dat de taak zonder fouten is voltooid. De [Proxmox-back-updocumentatie](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) maakt onderscheid tussen gewone back-upbestanden en PBS-opslag, die ontdubbelde blokken en metagegevens bewaart.

| Back-upmodus | VM-gedrag | Keuze voor deze proef |
|---|---|---|
| **Snapshot** | Maakt een back-up van een draaiende VM met weinig onderbreking. Schrijfacties van de gast veroorzaken een klein consistentierisico. | Geschikt voor routinetests wanneer de werklast dit herstelpunt aankan. |
| **Stop** | Sluit de gast af bij het begin van de back-up en biedt de sterkste consistentie. | Gebruik deze modus wanneer de werklast een nette afsluiting vereist en de onderbreking aanvaardbaar is. |
| **Suspend** | Pauzeert de gast vóór snapshotmodus en veroorzaakt extra onderbreking zonder algemeen consistentievoordeel. | Kies suspend niet standaard als verbetering ten opzichte van snapshot. |

Deze afwegingen komen uit de [Proxmox-referentie voor back-upmodi](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Een **QEMU Guest Agent** is een dienst in de gast waarmee Proxmox acties kan aanvragen, zoals het bevriezen en hervatten van het bestandssysteem. Een draaiende gast met een ingeschakelde, gezonde agent ondersteunt die acties tijdens een snapshotback-up. Het bevriezen van het bestandssysteem verbetert de consistentie, maar vervangt geen databasespecifieke herstelcontrole. Noteer de daadwerkelijke modus en de status van de agent. Ga er niet van uit dat een geplande taak je voorkeursinstellingen gebruikt.

## Maak een herstelpunt of selecteer er een

Gebruik een recente, geslaagde geplande back-up als de proef routineherstel test. Als je een nieuwe eenmalige back-up nodig hebt, open je het tabblad **Backup** van de VM, kies je **Backup now**, stel je de doelopslag en modus in en wacht je tot het taaklogboek succes meldt. Deze opdracht maakt vanuit een Proxmox-shell in snapshotmodus een back-up van VM **120** naar opslag-ID **backup-nfs**:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Vervang beide ID's door je eigen waarden. Voer de opdracht pas uit nadat je hebt bevestigd dat de opslag back-ups accepteert en voldoende ruimte heeft. De [Proxmox-referentie voor `vzdump`](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) beschrijft de modus- en opslagopties. Controleer het taaklogboek nadat de opdracht is voltooid. Beschouw een oude back-up niet als actueel herstelpunt alleen omdat de bestandsnaam recent lijkt.

Als het doel **PBS** is, voer je voor de geselecteerde datastore een verificatietaak uit of controleer je die. De [PBS-verificatiedocumentatie](https://pbs.proxmox.com/docs/maintenance.html) legt uit hoe je de integriteit van back-upgegevens verifieert en herhaalde controles plant. Verificatie vindt beschadigde back-upblokken. **Een geslaagde verificatie bewijst niet dat een hersteld besturingssysteem, een toepassing of een externe afhankelijkheid werkt.** Ga ook na een goed verificatieresultaat door met de herstelproef.

## Herstel naar een geïsoleerde VM

Selecteer in de Proxmox-interface de back-up in de weergave **Backups** van de opslag en kies **Restore**. Voer een ongebruikt VM-ID en de beoogde doelopslag in. Laat **Start after restore** uitgeschakeld. Controleer de optie voor een nieuw MAC-adres. De officiële [samenvatting van `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) beschrijft een uniek VM-ID, de opslagkeuze, `--unique` voor een willekeurig Ethernet-adres en de standaardinstelling waarbij de herstelde VM niet wordt gestart.

Voor een bestandsgebaseerd `vzdump`-archief toont deze shellopdracht het overeenkomstige patroon. Vervang het archiefpad, het nieuwe VM-ID en het opslag-ID door waarden uit je omgeving:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

De [Proxmox-beschrijving van herstel](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) vermeldt dat een herstel zonder doelopslag de oorspronkelijke opslag probeert te gebruiken. Stel **`--storage`** in wanneer de oude opslag niet op het testknooppunt bestaat. Gebruik **`--force`** niet voor een proef. Die optie staat overschrijven van een bestaande VM toe, terwijl deze procedure een ongebruikt ID vereist. PBS-back-ups herstel je ook via de Proxmox-interface. Selecteer de PBS-snapshot in de opslag in plaats van die als lokaal `.vma.zst`-bestand te behandelen.

Controleer vóór de eerste start iedere herstelde netwerkinterface, ook secundaire en rechtstreeks doorgegeven interfaces. Een **MAC-adres** identificeert een netwerkinterface. **DNS** koppelt namen aan adressen. **DHCP** wijst netwerkinstellingen toe. Een **VLAN** is een logisch netwerk dat over gedeelde hardware loopt. Een **virtuele TPM** bewaart beveiligingsstatus voor een gast. Koppel elke interface los of verbind deze uitsluitend met een geïsoleerd testsegment. Bevestig dat geen productieroute, DNS-pad, DHCP-dienst, beheernetwerk of externe integratie bereikbaar blijft. Als de werklast een andere testdienst nodig heeft, plaats je een testkopie op het geïsoleerde netwerk. Vergelijk schijfkoppelingen, firmware, vereisten voor de virtuele TPM en speciale apparaten met de bron. Externe schijven, rechtstreeks doorgegeven apparaten en geheimen buiten de VM vragen om afzonderlijke plannen.

## Proef de gast en werklast

Start de herstelde VM en gebruik eerst de console. Controleer of het besturingssysteem start, alle verwachte volumes zijn gekoppeld, de klok klopt en de toepassing start. Voer daarna de eerder genoteerde slaagvoorwaarde uit. Vergelijk een bekend gegevensitem met de waarde en het tijdstip van vóór de back-up. Een aanmeldprompt of draaiend proces toont op zichzelf niet dat de dienst de juiste gegevens bevat.

| Proef | Slaagvoorwaarde |
|---|---|
| **Opstarten** | De gast bereikt een normale aanmelding zonder herstelmodus of herhaalde herstelprompts. |
| **Schijven** | Iedere opgenomen schijf verschijnt, wordt gekoppeld en bevat de verwachte gegevens. |
| **Dienst** | Een representatief lokaal verzoek of een lokale lezing slaagt. |
| **Herstelpunt** | De herstelde gegevens voldoen aan het vastgelegde RPO. |
| **Hersteltijd** | Herstel, opstarten en dienstvalidatie voldoen aan het vastgelegde RTO. |
| **Isolatie** | Geen productieadres, taak of integratie ontvangt dubbel verkeer. |

Houd de herstelde gast geïsoleerd terwijl je geplande taken, meldingshooks, back-upagents en toepassingsreferenties inspecteert. Voer geen test uit die echte klantberichten stuurt of naar productiediensten schrijft. Noteer bij een mislukte controle de exacte stap. Maak onderscheid tussen **back-upintegriteitsfout**, **VM-opstartfout**, **ontbrekende gegevens** en **toepassingsfout**. Elke categorie vraagt om een andere oplossing.

| Foutcategorie | Bevestigend bewijs | Eerste oplossing | Hertest |
|---|---|---|---|
| **Back-upintegriteit** | De verificatie- of hersteltaak meldt beschadigde gegevens | Selecteer een ander geverifieerd herstelpunt en controleer de opslagstatus | Herhaal verificatie en herstel |
| **VM-opstart** | De console meldt firmware-, schijf- of herstelfouten | Vergelijk firmware, schijfkoppeling en opstartvolgorde met de bron | Start de geïsoleerde kopie en leg het console-resultaat vast |
| **Ontbrekende gegevens** | Verwacht bestand, volume of databaserecord ontbreekt | Controleer uitgesloten schijven, koppelingen, snapshots en externe afhankelijkheden | Herhaal de genoemde bestands- of gegevenscontrole |
| **Toepassing** | De gast start, maar de dienstcontrole mislukt | Controleer dienstlogboeken, referenties, afhankelijkheden en herstelstappen | Voer dezelfde lokale statuscontrole en werklasttest opnieuw uit |

Proxmox biedt [herstel van afzonderlijke bestanden voor PBS-back-ups](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Gebruik dit om een bestandsherstelpad te testen wanneer je werklast dat nodig heeft. Een hersteld bestand vervangt geen volledige VM-opstart en diensttest. Proxmox biedt ook liveherstel vanuit PBS. De documentatie vermeldt dat een VM in een ongedefinieerde toestand achterblijft als liveherstel mislukt. Gebruik voor deze geplande proef daarom een normale voltooide herstelactie.

## Leg het resultaat vast en sluit de proef af

Noteer het bron-VM-ID, de back-upopslag, het back-uptijdstip, de modus, het nieuwe VM-ID, de doelopslag, netwerkisolatie, de begin- en eindtijd van het herstel, de toepassingscontrole, het gegevenstijdstip en alle mislukte controles. Vergelijk het gemeten herstelpunt en de hersteltijd met je doelen. Een fout levert alleen nuttig bewijs op als je het back-upplan aanpast en de proef herhaalt.

Schakel de herstelde VM uit wanneer de test klaar is. Verwijder de testkopie pas nadat je het resultaat hebt opgeslagen en hebt gecontroleerd dat de productie-VM nog werkt. Bewaar de back-up volgens je normale bewaarbeleid. Pas de bewaartermijn niet aan om één proef te laten slagen.

Herhaal de test na grote wijzigingen aan opslag, gast of back-upconfiguratie. Wissel belangrijke VM's af, waaronder gasten met uitgesloten schijven of externe afhankelijkheden. De [migratiegids van Hyper-V naar Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) gebruikt dit herstelbewijs voordat een bron-VM buiten gebruik wordt gesteld. **Een bruikbare back-up heeft een bekend herstelpad, een geteste werklast en een gemeten herstelpunt.**

## Volgende stappen

Herhaal de proef na wijzigingen aan opslag, gast of back-up. Bekijk de [back-up- en hersteltest voor een homelab](/articles/homelab-backup-restore-drill/) voor bestandsherstel.
