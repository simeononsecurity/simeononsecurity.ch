---
title: "Thunderbird 153.6: Windows NTLM-gegevenslek en hoe je bijwerkt (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Twee ernstige Thunderbird-kwetsbaarheden kunnen NTLM-authenticatiegegevens lekken wanneer je een speciaal gemaakte e-mail weergeeft. Lees hoe beide routes werken, controleer je versie en beperk uitgaand SMB-verkeer tijdens het bijwerken."
genre: ["Cyberbeveiliging", "E-mailbeveiliging", "Windows-beveiliging"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "Thunderbird-beveiligingsupdate", "Thunderbird-kwetsbaarheid voor Windows", "Thunderbird NTLM-lek", "Thunderbird SMB-authenticatie", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "OpenPGP-sleutelbijlage", "externe bijlage", "blokkeren van externe inhoud", "mailbox-URL", "UNC-pad met uitgebreide lengte", "Windows-accountnaam", "NTLM-authenticatiegegevens", "SMB-gegevenslek", "uitgaand SMB", "TCP-poort 445", "e-mailbeveiliging", "Windows-e-mailclient", "Thunderbird-versie controleren", "Thunderbird bijwerken", "NTLM-relay", "offline wachtwoordkraken"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla heeft in Thunderbird 153.6 twee **ernstige kwetsbaarheden verholpen die Windows-inloggegevens bloot konden leggen**. Het weergeven van een speciaal gemaakte e-mail kon al een van de netwerkverzoeken activeren die in [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/) worden beschreven. Het advies noemt mogelijke blootstelling van NTLM-gegevens, geen bevestigde inbreuk op de inloggegevens van elke ontvanger.

<!--more-->

## Belangrijkste punten

- **CVE-2026-118174** betrof een extern gehoste OpenPGP-sleutelbijlage. Het weergeven van het bericht startte een verzoek zonder gebruikersactie, zelfs wanneer externe inhoud was geblokkeerd.
- **CVE-2026-118176** betrof een speciaal gevormde `mailbox:`-URL met een UNC-pad met uitgebreide lengte. Het weergeven van het bericht startte een SMB-verbinding naar een server die de afzender had gekozen.
- **Werk Thunderbird op Windows bij** en controleer de geïnstalleerde versie. Het advies noemt Thunderbird 153.6 als de versie met de oplossing. De releaseopmerkingen van Thunderbird noemen de bijbehorende build 153.6.0esr.

## Wat de e-mail activeert

**De twee kwetsbaarheden hebben verschillende ingangen.** Volgens Mozilla hoeft de ontvanger bij geen van beide op een link in de e-mail te klikken. Het risico voor Windows-inloggegevens hangt ervan af of een netwerkverzoek een door een aanvaller beheerde share bereikt en de daaropvolgende authenticatie-uitwisseling plaatsvindt. Mozilla meldt geen actieve uitbuiting in het advies.

| Probleem | Activering wanneer de e-mail wordt weergegeven | Risico voor Windows-inloggegevens |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird laadt de inhoud van een OpenPGP-sleutelbijlage om imports van de sleutel aan te bieden. De afzender markeert deze als externe bijlage met een URL die de aanvaller heeft gekozen. | Een URL naar een netwerkshare lekt de NTLM-gegevens van de gebruiker als het verzoek de share bereikt. |
| **CVE-2026-118176** | Een UNC-pad met uitgebreide lengte omzeilt Thunderbirds beperking op externe shares in `mailbox:`-URL's. | Thunderbird maakt verbinding met een SMB-server die de aanvaller heeft gekozen en geeft de Windows-accountnaam en NTLM-authenticatiegegevens vrij. |

Voor de route via de **OpenPGP-bijlage** zegt Mozilla uitdrukkelijk dat het verzoek de blokkering van externe inhoud omzeilde en geen gebruikersactie vereiste. Ook op andere systemen dan Windows was een extern verzoek mogelijk, tegen de instelling voor externe inhoud in, maar Mozilla beperkt het lekken van NTLM-inloggegevens tot Windows. Voor de route via de **`mailbox:`-URL** zegt Mozilla dat andere besturingssystemen geen gevolgen ondervinden. Zie de afzonderlijke vermeldingen voor [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) en [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**NTLM-authenticatiegegevens zijn geen wachtwoord in platte tekst.** Volgens Mozilla brengen de via de SMB-route vrijgegeven gegevens risico op offline wachtwoordkraken of relay-aanvallen met zich mee. Alleen een speciaal gemaakt bericht ontvangen bewijst niet dat een aanval is geslaagd. Het advies vermeldt ook andere Thunderbird-kwetsbaarheden, waaronder afzonderlijke routes via agenda en RSS. Dit artikel behandelt de twee routes die optreden bij het weergeven van e-mail en stelt niet alle problemen in de release gelijk.

## Thunderbird controleren en bijwerken

De kwetsbare handeling is **e-mail lezen in Thunderbird op Windows** voordat de relevante oplossing is geïnstalleerd. Mozilla noemt **Thunderbird 153.6** als de versie met de oplossing, maar geeft voor deze twee problemen geen volledig bereik van de oudste getroffen versies. De [releaseopmerkingen voor 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) vermelden een ESR-build die op 27 oktober 2026 is uitgebracht. Leid de patchstatus van een ander kanaal, een fork of een opnieuw verpakte build niet alleen af uit het versielabel.

1. Open op Windows **Help > About Thunderbird**. Lees de versie in het venster About af. Dit venster controleert ook op updates. De [update-instructies van Mozilla](https://support.mozilla.org/en-US/kb/updating-thunderbird) beschrijven deze stappen.
2. Laat Thunderbird de update downloaden als er een beschikbaar is en kies daarna **Restart Thunderbird to Update**. Open na de herstart opnieuw **Help > About Thunderbird** en controleer de geïnstalleerde versie.
3. Vergelijk bij de **153 ESR-lijn** de resulterende versie met **153.6.0esr** in de Thunderbird-releaseopmerkingen. Als je organisatie updates beheert, vraag de beheerder dan de oplossing van de leverancier te controleren in plaats van aan te nemen dat de update al is geïnstalleerd.

> **Versieopmerking:** De releaseopmerkingen voor 153.6.0esr bevestigen dat deze release bestaat. MFSA 2026-122 koppelt de beveiligingsoplossingen aan Thunderbird 153.6. De releaseopmerkingen beschrijven deze twee CVE's niet afzonderlijk. Raadpleeg het advies voor de details van de kwetsbaarheden.

## Risico beperken tijdens het bijwerken

**Installeer eerst de oplossing van de leverancier.** Alleen externe inhoud uitschakelen stopt CVE-2026-118174 niet, omdat het beschreven verzoek die instelling omzeilde. Advies om "niet te klikken" volstaat niet. Mozilla beschrijft verzoeken die door het weergeven van het bericht worden gestart.

Beperk als **extra beveiligingslaag** uitgaand SMB-verkeer van Windows-clients naar internet, waaronder **TCP-poort 445**, op de bedrijfsfirewall of beheerde eindpunten. De [richtlijnen van Microsoft voor SMB-verkeer](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) adviseren uitgaand TCP 445 naar internet te blokkeren en toegang tot vereiste bestandsservers te beperken. Breng benodigde shares in kaart voordat je een regel afdwingt, vooral wanneer je omgeving een clouddienst voor bestanden of externe medewerkers buiten de perimeter gebruikt. Deze netwerkmaatregel beperkt de beschreven SMB-route, maar repareert Thunderbird niet en verhelpt niet elk probleem met externe verzoeken uit het advies.

Als een Windows-computer met een oudere Thunderbird-build een verdacht bericht heeft weergegeven, **beschouw blootstelling dan als een vraag om te onderzoeken, niet als bewijs van een inbreuk**. Bekijk met je beveiligingsteam de beschikbare logboeken voor uitgaande SMB-verbindingen en authenticatie. Het leveranciersadvies bevat geen blootstellingstest en geen algemene instructie om alle wachtwoorden te wijzigen.

## Bronnen

- [Mozilla Foundation Security Advisory 2026-122: beveiligingsproblemen verholpen in Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Thunderbird Desktop-releaseopmerkingen: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support: Thunderbird bijwerken naar de nieuwste versie](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: SMB-verkeer in Windows Server beveiligen](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
