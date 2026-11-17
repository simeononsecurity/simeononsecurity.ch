---
title: "Persoonlijke beveiligingschecklist 2026: waar begin je en wat sla je over"
date: 2026-09-30
lastmod: 2026-11-15
toc: true
draft: false
description: "Rangschik maatregelen voor persoonlijke beveiliging op basis van hun effect, van accountbescherming en back-ups tot privacy en accountherstel."
genre: ["Persoonlijke beveiliging", "Privacy", "Digitale hygiëne", "Accountbeveiliging", "Dreigingsmodellering", "Consumentenbeveiliging", "Wachtwoordbeheer", "Gegevensbescherming"]
tags: ["persoonlijke beveiligingschecklist", "digitale beveiligingschecklist", "privacychecklist 2026", "persoonlijke cybersecurity", "accountbeveiliging", "passkey instellen", "hardwarebeveiligingssleutel", "wachtwoordmanager instellen", "best practices voor 2fa", "phishingbestendigheid", "datalekbewaking", "meldingen over gegevenslekken", "kredietblokkade", "privacy van e-mailaliassen", "compartimentering", "dreigingsmodel", "volledige schijfversleuteling", "3-2-1-back-upstrategie", "browserbeveiliging", "trackers blokkeren", "DNS via HTTPS", "metadata verwijderen", "exif verwijderen", "bescherming tegen simwissel", "accountherstel", "back-upcodes", "diefstal van sessietokens", "infostealermalware", "prioriteiten voor persoonlijke beveiliging", "fouten in beveiligingshygiëne", "privacytools", "lokaal werkende beveiligingstools"]
cover: "/img/cover/personal-security-checklist-2026-tiered-structure.webp"
coverAlt: "Digitale illustratie op een donkere achtergrond van kleurige blokken in lagen die maatregelen voor persoonlijke beveiliging voorstellen. Elk blok staat voor een actie, zoals een wachtwoordmanager en tweestapsverificatie."
coverCaption: ""
ref: ["/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security", "/articles/bitwarden-and-keepassxc-vs-the-rest", "/checklists/password-security-checklist"]
---

**Elke gids voor persoonlijke beveiliging geeft je hetzelfde: een lange, vlakke lijst met honderden tips zonder rangorde.** Je krijgt het advies om WebRTC uit te schakelen, je canvasvingerafdruk te vervalsen en je user-agent te rouleren, in dezelfde adem als het advies om een wachtwoordmanager in te stellen en automatische updates in te schakelen.

*Die punten zijn niet even waardevol. Als je ze als gelijkwaardig behandelt, doen veel mensen de makkelijke dingen, slaan ze belangrijke acties over en blijven ze even kwetsbaar.*

Dit artikel houdt het onderwerp overeind en laat de valse gelijkwaardigheid vallen. Je krijgt hetzelfde advies, gerangschikt op hoeveel risico het wegneemt voor de benodigde inspanning, en een eerlijke blik op gewoonten die je beter kunt opgeven.

## Het korte antwoord

| Vraag | Kort antwoord |
|---|---|
| **Wat stopt de meeste aanvallen?** | Een wachtwoordmanager, phishingbestendige tweede factoren en snelle updates. Deze gewoonten pakken veelvoorkomende routes naar accountmisbruik aan, maar niet elke dreiging. |
| **Wat is vandaag de grootste verbetering?** | **Passkeys of een hardwarebeveiligingssleutel.** Beide zijn bestand tegen phishing bij het aanmelden, omdat je aanmeldgegeven je apparaat niet verlaat. Bescherm ook herstelmethoden en het apparaat zelf. |
| **Wat krijgt te veel aandacht?** | Complexe wachtwoorden die je onthoudt, schema's voor wachtwoordrotatie en de meeste aanpassingen aan browserfingerprints. |
| **Wat krijgt te weinig aandacht?** | Back-ups, het instellen van accountherstel en de fysieke beveiliging van je apparaten. |
| **Maakt de volgorde uit?** | Ja, meer dan volledigheid. **Niveau 1 vandaag doen is beter dan alle 300 punten ooit uitvoeren.** |
| **Hoe lang duurt Niveau 1?** | Eenmalig ongeveer twee uur. |

## Waarom volgorde belangrijker is dan volledigheid

Een uitgebreide checklist telt meestal enkele honderden punten en geeft elk punt een label als **Essentieel**, **Optioneel** of **Geavanceerd**. Zo'n label helpt bij het filteren, maar is geen goede vervanging voor een rangorde. Alle punten krijgen hetzelfde label, ongeacht hoeveel risico ze wegnemen.

**Mijn stelling: zelfs drie niveaus bieden te weinig onderscheid**, want "Essentieel" zet punten met sterk uiteenlopende risicoreductie op één hoop. Vergelijk twee punten die allebei als essentieel gelden:

- **2FA inschakelen** verwijdert een hele categorie accountovernames.
- **WebRTC uitschakelen** voorkomt lokale IP-blootstelling, iets wat voor een kleine groep gebruikers van belang is.

Beide horen op een volledige lijst. Slechts één hoort bij je eerste uur.

**Het juiste ordeningsprincipe is een verhouding.** Rangschik elke actie op het risico dat ze wegneemt gedeeld door de inspanning die ze kost. Werk daarna van boven naar beneden. Dat ziet er zo uit:

| Niveau | Doel | Inspanning | Houdt tegen |
|---|---|---|---|
| **1. Stop de aanval** | Sluit de paden die aanvallers vandaag gebruiken | ~2 uur | Diefstal van inloggegevens, phishing, malware, apparaatdiefstal |
| **2. Beperk de schade** | Verklein de impact wanneer iets misgaat | ~1 uur | Enkelvoudige storingspunten, buitensluiting van accounts, identiteitsfraude |
| **3. Verklein blootstelling** | Verklein je digitale voetafdruk | Doorlopend | Profilering, tracking, gerichte social engineering |
| **4. Fysiek en menselijk** | Dek de laag af die software niet bereikt | ~30 minuten | Inbeslagname van apparaten, meekijken, telefonische phishing |

*Werk naar beneden. Sla Niveau 1 niet over om direct met Niveau 3 te beginnen, alleen omdat dat interessanter lijkt.*
{{< figure src="personal-security-tiers-ranked-by-impact.webp" alt="Diagram van vier niveaus met persoonlijke beveiligingsmaatregelen, gerangschikt op weggenomen risico en benodigde inspanning, van aanvallen stoppen tot fysieke en menselijke maatregelen" >}}

## Niveau 1: Blokkeer aanvallen

Vijf punten kosten samen ongeveer twee uur en pakken de routes aan die aanvallers gebruiken.

### 1. Een wachtwoordmanager met overal unieke wachtwoorden

**Credential stuffing is de belangrijkste methode voor accountovernames**, en werkt omdat mensen wachtwoorden hergebruiken. Als een website gegevens lekt, proberen aanvallers die gegevens automatisch en op grote schaal op andere sites.

Een wachtwoordmanager pakt de oorzaak aan en voorkomt dat je per ongeluk hergebruikt. De manager maakt voor elk account een apart wachtwoord met hoge entropie en vult het voor je in.

Een belangrijk detail dat veel advies overslaat: **het wachtwoord van je manager is nu het enige storingspunt**. Het moet lang zijn en je moet het onthouden. Dit is het enige wachtwoord dat je nergens anders opslaat. Een wachtwoordzin van vijf of zes willekeurige woorden is sterker dan een korte complexe tekenreeks en veel makkelijker te onthouden.

Er zijn twee geschikte architecturen:

| Aanpak | Sterk punt | Afweging |
|---|---|---|
| **Gesynchroniseerd via de cloud** (Bitwarden en vergelijkbare diensten) | Handig, synchroniseert tussen apparaten en is makkelijk te herstellen | Je vertrouwt de versleuteling en beschikbaarheid van de leverancier |
| **Offline op basis van bestanden** (KeePassXC en vergelijkbare software) | Volledige controle, geen afhankelijkheid van een leverancier | Je beheert zelf de back-ups en synchronisatie |

*Kies een van beide. Het verschil tussen beide opties is veel kleiner dan het verschil tussen wel of geen manager gebruiken.*

Bekijk onze vergelijking **[Beste wachtwoordmanagers 2026: Bitwarden versus KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** en de gids **[Sterke wachtwoorden maken in 2026](/articles/how-to-create-strong-passwords/)**.

### 2. Phishingbestendige tweede factoren

Tweede factoren zijn niet onderling uitwisselbaar. Ze verschillen sterk in de aanvallen waartegen ze helpen.

| Methode | Stopt credential stuffing | Stopt phishing | Stopt diefstal van sessietokens |
|---|---|---|---|
| **Sms-codes** | Ja | Gedeeltelijk, via simwissel | Nee |
| **Codes uit een authenticator-app** | Ja | Gedeeltelijk, via realtime doorsturen | Nee |
| **Pushgoedkeuring** | Ja | Zwak, via meldingsbombardementen | Nee |
| **Passkeys of hardwarebeveiligingssleutel** | Ja | **Ja** | Ja |

**Passkeys en FIDO2-hardwarebeveiligingssleutels zijn de enige opties op de lijst die phishing tegenhouden.** Dat komt door de opzet, niet door een kleine verbetering: het aanmeldgegeven is aan de oorsprong gebonden, zodat een lookalike-domein niets bruikbaars ontvangt. Het slachtoffer krijgt geen code die het aan een aanvaller kan voorlezen.

Een verwante dreiging verdient een naam, omdat die methoden ondermijnt die mensen veilig achten. **Infostealermalware steelt nu rechtstreeks browsercookies**, waardoor een aanvaller een aangemelde sessie kan hergebruiken zonder wachtwoord of tweede factor. Daarom is de laatste kolom belangrijk en is **Niveau 1, punt 3, onmisbaar**.

*Prioriteit binnen dit punt: gebruik passkeys als ze beschikbaar zijn, een hardwarebeveiligingssleutel voor e-mail en financiën, een authenticator-app voor de rest en sms alleen als niets beters beschikbaar is.*

{{< figure src="phishing-resistant-second-factor-comparison.webp" alt="Diagram dat sms-codes, authenticator-apps, pushgoedkeuring en passkeys vergelijkt voor credential stuffing, phishing en diefstal van sessietokens. Passkeys houden alle drie tegen." >}}

Genereer en controleer tijdgebaseerde codes lokaal met onze **[TOTP- en HOTP-generator](/totp-generator/)**. De tool leest een Base32-geheim of een `otpauth://`-URI en draait volledig in je browser.

### 3. Overal automatisch bijwerken

**De meeste succesvolle inbraken misbruiken een kwetsbaarheid waarvoor al een patch bestaat.** Aanvallers leven van vertraging bij updates.

Je hoeft niet beter je best te doen met updates. Verwijder de beslissing door automatische updates op elke laag in te schakelen:

- **Besturingssysteem**: Windows Update, Software-update op macOS of unattended-upgrades op Linux
- **Browsers**: laat automatische updates aanstaan en herstart wanneer daarom wordt gevraagd. Een wachtende herstart betekent dat de browser nog niet is gepatcht.
- **Telefoon**: schakel automatische updates van apps in, niet alleen updates van het besturingssysteem
- **Router**: dit is de laag die mensen vergeten, terwijl die vanaf het internet bereikbaar is

**Een browser die wacht op een herstart draait kwetsbare code.** Deze ene gewoonte neemt meer blootstelling weg dan de meeste punten uit Niveau 3 samen.

*Onze analyse van kernel escapes in **[Containers zijn niet langer een beveiligingsgrens](/articles/containers-no-longer-security-boundary-2026/)** laat zien hoe belangrijk het patchvenster is bij een aanval met privilege-escalatie.*

### 4. Apparaatversleuteling en een echt vergrendelscherm

**Volledige schijfversleuteling maakt van een gestolen apparaat een hardwareverlies in plaats van een datalek.** Zonder versleuteling kan iedereen met je laptop of telefoon alle inhoud lezen, ook je wachtwoordkluis en actieve sessietokens.

Elk gangbaar platform biedt versleuteling, maar op sommige staat die niet standaard aan:

| Platform | Functie | Controleren |
|---|---|---|
| **Windows** | BitLocker of Device Encryption | Instellingen, Privacy en beveiliging, Apparaatversleuteling |
| **macOS** | FileVault | Systeeminstellingen, Privacy en beveiliging, FileVault |
| **Linux** | LUKS | Bevestig bij de installatie dat de root- en home-volumes versleuteld zijn |
| **iOS en Android** | Standaard aan zodra een toegangscode is ingesteld | Stel een toegangscode in en bevestig dat versleuteling actief is |

Naast versleuteling gelden twee regels:

- **Gebruik een wachtwoordzin of lange pincode, geen code van vier cijfers.** E-mail- en financiële accounts verdienen de sterkste telefoonvergrendeling, omdat de toegangscode al het andere op het apparaat beschermt.
- **Geef de voorkeur aan een pincode boven biometrie als je risico loopt op juridische dwang.** Biometrie is handig en moeilijk te vergeten. In sommige rechtsgebieden gelden andere beschermingen voor afgedwongen vingerafdrukken of gezichten dan voor afgedwongen kennis.

### 5. Back-ups, één keer getest

**Ransomware en hardwarestoringen eindigen hetzelfde, en een back-up is de enige maatregel die tegen beide helpt.** Mensen slaan dit punt vaak over en krijgen daar later het meeste spijt van.

De standaard is **3-2-1**: drie kopieën op twee soorten media, waarvan één buiten de locatie. Voor een individu betekent dit:

- **Eén lokale kopie** voor snel herstel
- **Eén versleutelde kopie buiten de locatie** tegen ransomware en brand
- **Eén offline kopie of een beschrijfbare kopie** voor het geval ransomware je gesynchroniseerde opslag bereikt

*Dit laatste punt is het belangrijkst en wordt het minst vaak uitgevoerd. Gesynchroniseerde opslag is geen back-up. Ransomware en onbedoelde verwijdering worden ook gesynchroniseerd.*

**Test minstens één keer een herstel.** Een back-up die je nooit hebt hersteld, is een hypothese.

## Niveau 2: Beperk de schade

Niveau 1 gaat ervan uit dat niets misgaat. Niveau 2 gaat ervan uit dat er iets misgaat en beperkt de gevolgen.

### 6. Gebruik je e-mailadres niet steeds opnieuw

**Je e-mailadres is de koppelingssleutel tussen alle databases die ooit zijn gelekt.** Eén adres overal gebruiken betekent dat één datalek met de rest kan worden gekoppeld. Het geeft social engineers bovendien een bevestigd startpunt.

**Aliassen lossen beide problemen op.** Maak voor elke dienst een uniek adres, zodat het adres zelf een label wordt:

| Voordeel | Waarom dit telt |
|---|---|
| **Bron van een lek achterhalen** | Als spam op één alias binnenkomt, weet je welke dienst je adres heeft gelekt of verkocht |
| **Direct blokkeren** | Schakel één alias uit zonder je echte inbox aan te passen |
| **Minder koppeling** | Verschillende adressen voorkomen dat accounts in één profiel worden samengevoegd |
| **Phishing herkennen** | Mail aan een alias die je niet meer gebruikt, is duidelijk frauduleus |

**Subadressering** (`you+service@example.com`) is een zwakkere variant. Je ontdekt ermee wie je adres lekte, maar het toont tegelijk je echte adres. Het voorkomt dus niet dat accounts worden gekoppeld.

*Als je een domein hebt, levert een catch-all-aliassysteem dit gratis. Anders doen speciale aliasproviders hetzelfde.*

### 7. Accountherstel is het echte aanvalsoppervlak

**Aanvallers slaan de voordeur steeds vaker over en richten zich op herstel.** Herstel moet werken na verlies van een apparaat en mag niet de zwakste schakel worden.

Stel deze zaken in, op volgorde:

- **Bewaar back-upcodes offline.** Print ze of bewaar ze op versleutelde media. Houd ze **gescheiden van je wachtwoordmanager**, zodat een inbraak in de ene niet ook de andere blootlegt.
- **Geef de voorkeur aan herstelsleutels boven beveiligingsvragen.** Antwoorden op vragen over de meisjesnaam van je moeder of je eerste auto zijn vaak openbaar.
- **Geef valse antwoorden als een site beveiligingsvragen afdwingt.** Sla ze bij het account op in je manager.
- **Registreer waar mogelijk een tweede apparaat of sleutel**, zodat één storing je niet buitensluit.
- **Verwijder verouderde herstelcontacten en telefoonnummers**, want een oud nummer is nu van iemand anders.

> **Waarschuwing: verlies van je tweede factor zonder herstelcodes betekent vaak dat je account voorgoed verloren is. Supportteams herstellen de toegang tot een goed beveiligd account meestal niet.** Stel herstel in wanneer je de tweede factor inschakelt.

{{< figure src="three-two-one-backup-strategy-diagram.webp" alt="Diagram van het 3-2-1-back-upmodel met drie gegevenskopieën op twee soorten media en een offline kopie die beschermt tegen ransomware en onbedoelde verwijdering" >}}

### 8. Krijg vroeg bericht over datalekken

**De waarde van een melding over een datalek hangt helemaal af van de timing.** Je wilt een lek ontdekken zolang het wachtwoord ergens nog geldig is.

- **Have I Been Pwned** stuurt waarschuwingen als je adres in een nieuwe dataset verschijnt. De dienst biedt ook meldingen voor een volledig domein als je dat bezit en aliassen gebruikt.
- **Je wachtwoordmanager geeft een beter signaal**, want die weet welke kluisvermeldingen bij een gemelde dienst horen en markeert ze rechtstreeks.

*De nuttige aanpak is kort: ontvang een waarschuwing, wijzig het wachtwoord van het betrokken account en wijzig het overal waar je het oude wachtwoord hergebruikte. Dit is het voordeel van punt 1 uit Niveau 1: unieke wachtwoorden maken die tweede stap overbodig.*

### 9. Bevries je kredietregistratie voordat je dit nodig hebt

**Een kredietbevriezing is de sterkste beschikbare bescherming tegen identiteitsfraude bij het openen van nieuwe accounts**, en kost niets. Kredietverstrekkers kunnen je dossier dan niet opvragen om accounts op jouw naam te openen.

In de Verenigde Staten kun je de bevriezing aanvragen bij elk van de drie grote kredietbureaus. Je kunt de bevriezing tijdelijk en omkeerbaar opheffen voor een legitieme aanvraag. Volg deze stappen:

1. **Bevries je dossier bij alle drie de bureaus**, niet bij één. Elk bureau heeft een apart dossier.
2. **Bewaar de pincodes voor het opheffen** in je wachtwoordmanager.
3. **Hef de blokkade tijdelijk op** wanneer je krediet aanvraagt en zet die daarna weer aan.

*Doe dit voordat je het nodig hebt. Het proces tijdens fraude ontdekken, terwijl je ook accounts betwist, is het slechtste moment om het te leren.*

## Niveau 3: Verklein blootstelling

Niveau 3 verkleint je digitale voetafdruk. Dat is belangrijk, maar dit staat onder de punten hierboven omdat het accountovernames niet tegenhoudt.

### 10. Beveilig je webbrowser

**De meeste blootstelling van persoonlijke gegevens gebeurt in de browser**, en twee aanpassingen pakken het grootste deel aan:

- **Installeer een contentblocker.** Advertenties en trackers verzamelen de meeste gegevens op het web. Ze blokkeren verwijdert zowel tracking als een groot deel van het aanvalsoppervlak. Kies één betrouwbare blocker in plaats van meerdere.
- **Houd alleen de extensies die je gebruikt.** **Extensies lezen en wijzigen pagina-inhoud**, waardoor een verlaten of kwaadaardige extensie rechtstreeks toegang tot je sessies kan geven. Bekijk de lijst elk kwartaal.

*Browserfingerprints willekeurig maken is nuttig om te begrijpen, maar zelden een prioriteit. Het levert niet niets op, maar minder dan punten 1 tot en met 5, en het breekt websites.*

Bekijk de volledige bespreking in **[Beste privacybrowsers 2026: LibreWolf versus Brave en Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.

### 11. Versleutel domeinnaamopvragingen

**Gewone DNS is niet versleuteld en kan worden bekeken. Je netwerkbeheerder en anderen op het netwerkpad zien daardoor elk domein dat je opvraagt.** DNS-over-HTTPS of DNS-over-TLS versleutelt de opvraag.

Er zijn twee kanttekeningen:

- **DoH verplaatst vertrouwen in plaats van het weg te nemen.** Je DNS-resolver ziet nu je aanvragen in plaats van je internetprovider. Kies daarom een resolver met een gepubliceerde privacyverklaring. Alleen het protocol is niet genoeg.
- **DoH omzeilt netwerkfilters**, waaronder ouderlijk toezicht en bedrijfscontroles waarop veel mensen vertrouwen.

*Een echte beveiligingswinst naast privacy: versleutelde DNS maakt DNS-spoofing op onbetrouwbare netwerken geen praktisch aanvalspad meer.*

### 12. Verwijder metagegevens voordat je deelt

**Foto's bevatten meer dan pixels.** De meeste telefooncamera's voegen EXIF-gegevens toe, waaronder GPS-coördinaten, tijdstempels en apparaat-ID's.

**Dit is belangrijker voor documenten dan voor foto's.** Een gedeelde PDF of Office-bestand bevat vaak nog auteursnamen, bewerkingsgeschiedenis en interne bestandspaden. Zo lekken interne documenten informatie over een organisatie.

Onze **[EXIF-weergave](/exif-viewer/)** leest metadata van een afbeelding lokaal, zodat je ziet welke gegevens een foto prijsgeeft zonder die te uploaden. De **[URL-ontleder](/url-parser/)** doet hetzelfde voor links en toont trackingparameters en inloggegevens in het authority-gedeelte voordat je de URL in een chat plakt.

## Niveau 4: Fysiek en menselijk

Dit tier kost ongeveer dertig minuten en behandelt wat geen softwaremaatregel bereikt.

### 13. Beheer je apparaten fysiek

- **Vergrendel overal het scherm** en stel een korte time-out in. Een ontgrendelde laptop betekent dat alle accounts volledig zijn overgenomen.
- **Laat apparaten nooit zichtbaar in een voertuig liggen.** Zo voorkom je diefstal en het verlies van gegevens.
- **Gebruik een privacyscherm** in openbare ruimtes, zodat de meeste mensen niet op je scherm kunnen meekijken.
- **Controleer openbare oplaadpunten** voordat je een apparaat aansluit. Gebruik liever een kabel die alleen stroom levert of je eigen wandadapter dan een onbekende USB-poort.

### 14. Controleer personen, niet berichten

**Phishing via stem en video ondermijnt nu de aanname dat een vertrouwde stem de identiteit bevestigt.** Gekloonde stemmen op basis van enkele seconden openbare audio zijn inmiddels gebruikelijk. Het verzoek bevat meestal haast en een vraag om geld of inloggegevens.

Controleer de identiteit via een ander kanaal:

1. **Hang op en bel terug** naar een nummer dat je al kende, niet naar een nummer van de beller.
2. **Zie haast als een signaal, niet als reden.** Druk om direct te handelen is het mechanisme van de aanval, geen bijkomstigheid.
3. **Spreek een verificatiezin af** met familieleden die iemand zou kunnen imiteren.
4. **Maak nooit geld over op basis van alleen een telefoontje of spraakbericht.**

*Dit levert binnen Niveau 4 de meeste winst op en kost niets.*

### 15. Documenten en weggooien

- **Versnipper of scherm documenten af** waarop rekeningnummers, identificatienummers of medische gegevens staan.
- **Zet een watermerk op documenten** die je voor een bepaald doel deelt. Vermeld de ontvanger en datum. Het kost niets en helpt een lek te traceren.
- **Meld je af bij people-searchsites** en houd er rekening mee dat dit opnieuw nodig is, omdat vermeldingen terugkeren.
- **Bekijk openbare registers** en vraag waar mogelijk om verwijdering.

*Onze **[Checklist voor fysieke beveiliging](/checklists/physical-security-checklist/)** behandelt deze laag uitgebreider.*

## Wat de meeste mensen verkeerd om doen

Acht gewoonten die je beter kunt afleren, met de reden waarom ze blijven bestaan en wat je in plaats daarvan kunt doen.

| Gewoonte | Waarom die blijft bestaan | Doe dit in plaats daarvan |
|---|---|---|
| **Korte, complexe wachtwoorden onthouden** | Jarenlang gold dit als advies | Gebruik een manager en een lange wachtwoordzin voor de kluis |
| **Wachtwoorden volgens een schema rouleren** | Verouderd nalevingsbeleid | Wijzig ze bij een melding van een datalek of vermoedelijke inbraak, niet volgens de kalender |
| **SMS gebruiken voor belangrijke accounts** | Het is de standaardoptie | Gebruik passkeys of een hardwaresleutel voor e-mail, financiën en identiteitsaccounts |
| **2FA-codes opslaan in dezelfde manager als wachtwoorden** | Gemak | Bewaar de twee apart, zodat één inbraak niet beide factoren oplevert |
| **Gesynchroniseerde cloudopslag als back-up behandelen** | Het ziet eruit als een back-up | Voeg een offline kopie of een beschrijfbare kopie toe |
| **Een perfecte browserfingerprint najagen** | Je kunt die meten, dus voelt het als actie | Doe eerst punten 1 tot en met 5 |
| **Beveiligingsvragen eerlijk beantwoorden** | Het lijkt verplicht | Gebruik valse antwoorden en sla die op in je manager |
| **Aannemen dat HTTPS veilig betekent** | Het hangslot stelt gerust | Controleer de domeinnaam, want de meeste phishingsites hebben geldige certificaten |

Het patroon bij alle acht: **elk punt valt op en is meetbaar, daarom trekt het aandacht. Toch komt elk punt na een maatregel met meer opbrengst.** Wie browserfingerprints optimaliseert voordat die een wachtwoordmanager instelt, heeft de volgorde omgedraaid.

> **Veelgemaakte fout: wachtwoordmanagers riskant vinden omdat ze geheimen samenbrengen.** Ze concentreren inderdaad risico. Het alternatief is wachtwoorden hergebruiken op tientallen sites. Risico concentreren onder je eigen controle is beter dan het zonder controle verspreiden.

## Beveilig je gegevens zonder ze af te staan

Een praktisch probleem speelt door dit hele onderwerp heen. **De tools die je helpen accounts te beveiligen, vragen vaak om dezelfde geheimen die je probeert te beschermen.**

Een wachtwoordsterktecontrole die je wachtwoord naar een server stuurt, is een risico. Een hashcalculator die je bestand uploadt, ondermijnt het doel. Een certificaattool die je hostnaam opvraagt, vertelt een derde partij welke sites je beheert.

**Elke tool hieronder draait volledig in je browser**, zonder upload en zonder account. Dit is een uitgesproken beleid op deze site. De uitzonderingen staan openlijk vermeld.

**Controleer de grens zelf:** verbreek de netwerkverbinding, open de tool en bekijk het netwerkpaneel van de browser terwijl je een testwaarde verwerkt. Een claim over lokale verwerking beschrijft het bedoelde ontwerp. Beoordeel ook je browserextensies en de versie van de tool.

| Taak | Tool | Wat de tool doet |
|---|---|---|
| **Een sterk wachtwoord maken** | **[Wachtwoordgenerator](/password-generator/)** | `crypto.getRandomValues` met afwijzingssampling om modulovertekening te voorkomen, plus de entropie van je gekozen instellingen |
| **De sterkte van een wachtwoord controleren** | **[Wachtwoordsterkte controleren](/password-checker/)** | Beoordeelt een kandidaat lokaal, inclusief herkenning van patronen en hergebruik |
| **Een tweede factor instellen** | **[TOTP- en HOTP-generator](/totp-generator/)** | Leest een Base32-geheim of `otpauth://`-URI en controleert codes binnen tijdvensters |
| **Het certificaat van een site bekijken** | **[SSL-certificaatinformatie](/ssl-certificate-info/)** | Onderwerp, geldigheid, sleutelsterkte, SAN's en waarschuwingen over zwakke algoritmen |
| **Een certificaatketen controleren** | **[SSL-ketentester](/ssl-chain-tester/)** | Sorteert de keten en controleert elke handtekening, waaronder ontbrekende tussenliggende certificaten |
| **Een download of bestand controleren** | **[Hashcalculator](/hash-calculator/)** | MD5 tot en met SHA-512 om integriteit te controleren met een gepubliceerde digest |
| **Unieke ID's genereren** | **[UUID-codegenerator](/uuid-generator/)** | UUID's versie 4 met de juiste versie- en variantbits |
| **Een verdachte link inspecteren** | **[URL-ontleder](/url-parser/)** | Decodeert het pad, vermeldt parameters en markeert inloggegevens in het authority-gedeelte |
| **Metadata van een foto controleren** | **[EXIF-weergave](/exif-viewer/)** | Toont locatie-, tijd- en apparaatgegevens in de foto |
| **Codering of versleuteling meten** | **[Entropie-analyse](/entropy-analyzer/)** | Shannon-entropie om repetitieve gegevens te onderscheiden van gecodeerde of versleutelde gegevens |
| **Een indicator veilig neutraliseren** | **[IOC veilig maken en herstellen](/ioc-defang-refang/)** | Maakt URL's en adressen onschadelijk wanneer je ze deelt |

*Het principe achter de tabel: als een tool een geheim nodig heeft, moet die draaien op de plek waar het geheim staat. Bekijk **[Alle tools](/tools/)** voor de volledige lijst en de paar tools die netwerkverzoeken doen, met uitleg waarom.*

## Je dreigingsmodel bepalen

**De juiste checklist hangt af van de tegenstander waartegen je jezelf beschermt.** Als je die vraag overslaat, besteed je moeite aan de verkeerde zaken.

| Jouw situatie | Realistische tegenstander | Focuspunten |
|---|---|---|
| **De meeste personen** | Opportunistische criminelen, automatisch credential stuffing en willekeurige phishing | Tiers 1 en 2 plus apparaten die je meedraagt |
| **Bekend persoon of openbare functie** | Gerichte phishing, doxxing en pogingen om accounts over te nemen | Voeg compartimentering en aliassen toe en overweeg je sociale voetafdruk te bewaken |
| **Journalist, activist of juridisch risico** | Overheid of goed gefinancierde tegenstanders, inbeslagname van apparaten | Voeg Tor en aparte apparaten toe, plus operationele discipline bij het scheiden van identiteiten |
| **Eigenaar van een klein bedrijf** | Overname van zakelijke e-mail, factuurfraude en omleiding van betalingen | Verifieer elke betaling via een ander kanaal |
| **Technisch professional** | Aanvallen op de toeleveringsketen, diefstal van inloggegevens en aanvallen via afhankelijkheden | Voeg hardwaresleutels, code-ondertekening en scheiding van werk- en privé-identiteit toe |

**De eerlijke lezing van de tabel.** Voor de meeste mensen ligt het grootste deel van het realistische risico in Niveau 1 en 2. De geavanceerde maatregelen zijn erg belangrijk voor wie ze nodig heeft. Toch voeren mensen ze vaak uit zonder dat ze voor hen nodig zijn.

*In **[Je eigen persoonlijke dreigingsmodel maken](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** lees je hoe je deze beoordeling zelf opstelt.*

## Belangrijkste punten

- **Volgorde gaat boven volledigheid.** De vijf punten in Niveau 1 nemen meer realistisch risico weg dan alle 300 punten van een uitgebreide lijst willekeurig uitvoeren.
- **Passkeys en hardwaresleutels zijn de enige tweede factoren die phishing tegenhouden**, omdat het aanmeldgegeven aan de oorsprong gebonden is en je apparaat niet verlaat.
- **Infostealermalware steelt sessiecookies direct**, daarom is diefstal van sessietokens de reden dat een zwakke tweede factor op zichzelf niet volstaat.
- **Versleuteling maakt van een gestolen apparaat hardwareverlies** in plaats van een datalek. Controleer of versleuteling aanstaat, want niet overal is dit standaard ingeschakeld.
- **Gesynchroniseerde opslag is geen back-up.** Voeg een offline kopie of een beschrijfbare kopie toe en test één keer een herstel.
- **Accountherstel is het nieuwe aanvalsoppervlak.** Bewaar back-upcodes offline en gescheiden van de wachtwoordmanager.
- **Aliassen verbreken de koppeling** tussen gelekte databases waarin je adres staat.
- **Veel geoptimaliseerde beveiligingstips leveren weinig op.** Aanpassingen aan fingerprints en user-agent staan ver onder een wachtwoordmanager en automatische updates.
- **De juiste checklist hangt af van je tegenstander.** Geavanceerde maatregelen zijn erg belangrijk voor wie ze nodig heeft en worden vaak gebruikt door mensen die ze niet nodig hebben.

## Volgende stappen

1. **Voer Niveau 1 vandaag uit.** Dat duurt ongeveer twee uur: een wachtwoordmanager, een phishingbestendige tweede factor, automatische updates, apparaatversleuteling en één back-up waarvan je herstel hebt getest.
2. **Bekijk een communitychecklist** met honderden punten uit twaalf categorieën: **[Persoonlijke beveiligingschecklist](https://github.com/Lissy93/personal-security-checklist)**.
3. **Gebruik de interactieve versie** om op dreigingsmodel te filteren en voortgang bij te houden: **[Interactieve verdediging](https://digital-defense.io)**.
4. **Gebruik de organisatorische checklists op deze site** voor professionele tegenhangers van dit artikel. Ze omvatten **[Wachtwoordbeveiliging](/checklists/password-security-checklist/)**, **[Bewustwording van phishing](/checklists/phishing-awareness-checklist/)**, **[Back-up en herstel van gegevens](/checklists/data-backup-recovery-checklist/)**, **[Beveiliging van mobiele apparaten](/checklists/mobile-device-security-checklist/)** en **[Beveiliging van sociale media](/checklists/social-media-security-checklist/)**.
5. **Kies je wachtwoordmanager** met de architectuurvergelijking **[Bitwarden versus KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**.
6. **Verbeter je browser** in plaats van een zwakkere browser te optimaliseren: **[LibreWolf versus Brave en Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.
7. **Bescherm je betaalgegevens** met virtuele kaartnummers: **[Virtuele kaarten van Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)**.
8. **Gebruik de tools lokaal**, begin met de **[Wachtwoordgenerator](/password-generator/)** en de **[TOTP-codegenerator](/totp-generator/)**.

## Gerelateerde artikelen

| Artikel | Wat het behandelt |
|---|---|
| **[Je eigen persoonlijke dreigingsmodel maken](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** | De beoordeling die bepaalt welke tier bij je past |
| **[Beste wachtwoordmanagers 2026: Bitwarden versus KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** | Kiezen tussen een cloudgesynchroniseerde en een offline kluisarchitectuur |
| **[Sterke wachtwoorden maken in 2026](/articles/how-to-create-strong-passwords/)** | Entropie, wachtwoordzinnen en waarom lengte beter werkt dan symbolen vervangen |
| **[Gids voor multifactorauthenticatie](/articles/what-are-the-diferent-kinds-of-factors-in-mfa/)** | De factorindeling achter de vergelijking van tweede factoren hierboven |
| **[Beste privacybrowsers 2026: LibreWolf versus Brave en Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)** | Browserbeveiliging voor Niveau 3 |
| **[Smartwatchopties met privacy voorop](/articles/smartwatches-for-privacy-and-security-enthusiasts/)** | Dezelfde rangordelogica toepassen op draagbare apparaten |
| **[Virtuele kaarten van Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)** | Blootstelling van betaalgegevens beperken, als aanvulling op kredietbevriezing |

## Bronnen

1. [Persoonlijke beveiligingschecklist, een communitychecklist van Alicia Sykes](https://github.com/Lissy93/personal-security-checklist)
2. [Persoonlijke beveiligingschecklist, de volledige checklist](https://github.com/Lissy93/personal-security-checklist/blob/HEAD/CHECKLIST.md)
3. [De interactieve versie van de digitale verdediging](https://digital-defense.io)
4. [Awesome Privacy, lijst van software die privacy respecteert](https://github.com/lissy93/awesome-privacy)
5. [Have I Been Pwned, meldingen over datalekken](https://haveibeenpwned.com)
6. [FIDO Alliance, specificaties voor passkeys en FIDO2](https://fidoalliance.org/passkeys/)
7. [Use Plaintext Email, e-mail instellen met platte tekst](https://useplaintext.email/)
8. [Consumer Financial Protection Bureau, kredietrapporten en scores](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
9. [FTC, consumententips over identiteitsdiefstal](https://consumer.ftc.gov/identity-theft-and-online-security)
10. [Passkeys.dev, communitybron over de implementatie van passkeys](https://passkeys.dev/)
