---
title: "Open WebUI v0.12.4: checklist voor upgrades en toegangsbeheer 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Maak een back-up en upgrade Open WebUI naar v0.12.4. Test daarna chatdeling, exportrechten, resourcetoegang, accounts en netwerktoegang."
genre: ["Zelf gehoste AI", "Cyberbeveiliging", "Systeembeheer"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "Open WebUI-upgrade", "Open WebUI-beveiliging", "Open WebUI-toegangsbeheer", "zelf gehoste AI", "Docker-upgrade", "pip-upgrade", "Open WebUI-back-up", "Open WebUI-rechten", "Open WebUI-rollen", "Open WebUI-groepen", "chat-exportrecht", "gedeelde chats", "gearchiveerde chats", "toegang tot kennisbank", "modeltoegang", "toolrechten", "API-sleutelbeveiliging", "beveiliging van beheerdersaccount", "registratie uitschakelen", "reverse-proxyauthenticatie", "VPN-toegang", "containerimage vastzetten"]
---

**Open WebUI v0.12.4 bevat beveiligingsoplossingen die de beheerders nog niet nader hebben toegelicht.** De releaseopmerkingen adviseren om installaties snel bij te werken en zeggen dat beveiligingsadviezen volgen zodra CVE's zijn toegewezen. De hieronder genoemde wijzigingen voor chatdeling en rechten zijn de zichtbare punten in de releaseopmerkingen. Ze vormen geen volledige lijst van de nog niet openbaar gemaakte beveiligingsoplossingen. [Releaseopmerkingen Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Belangrijkste punten

- **Maak eerst een back-up.** Bewaar een herstelbare kopie van het datavolume of de database en uploads voordat je de applicatie wijzigt.
- **Zet de officiële release vast.** Gebruik `ghcr.io/open-webui/open-webui:v0.12.4` voor de standaard Docker-image of `open-webui==0.12.4` voor pip.
- **Test rechten met echte gebruikersrollen.** Een verborgen knop bewijst niet dat de API autorisatie controleert.
- **Houd toegang privé.** Vereis applicatieauthenticatie en beperk netwerktoegang via een VPN of een geauthenticeerde reverse proxy.

## Voordat je upgradet

**Vereisten:** bepaal de huidige installatiemethode, de containerimagevariant, de locatie van persistente gegevens, de externe database, de reverse proxy en de authenticatieprovider. Plan een onderhoudsvenster en bewaar de bestaande containerconfiguratie of service-definitie. Plan tijd voor een hersteltest op een aparte instantie. De onderstaande opdrachten zijn door de leverancier gedocumenteerde voorbeelden, aangepast aan deze vastgezette versie. Ze zijn niet het resultaat van een live upgrade voor deze handleiding. [Open WebUI bijwerken](https://docs.openwebui.com/getting-started/updating/)

1. **Inventariseer de opslag.** In de standaard Docker-configuratie wordt `open-webui` gekoppeld aan `/app/backend/data`. Noteer bind mounts, de externe database, objectopslag en aangepaste omgevingsvariabelen. Zoek bij pip het actieve datadirectory en de database voordat je de omgeving wijzigt. Ga er niet van uit dat een chat-export een volledige back-up is.
2. **Maak een back-up terwijl schrijfbewerkingen zijn gestopt.** Stop de applicatie of maak een database-snapshot die consistent blijft. Kopieer daarna het volume, externe databases en uploads naar aparte opslag. De leverancier documenteert een archief van een Docker-volume. Pas de volumenaam en het back-uppad aan je installatie aan. Controleer of het archief opent en oefen een herstel op een aparte instantie voordat je erop vertrouwt. [Back-up en herstel](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Lees de releaseopmerkingen en migratie-instructies.** De opmerkingen bij v0.12.4 noemen de openstaande beveiligingsoplossingen niet en geven geen reeks getroffen versies. Wijs die oplossingen geen CVE toe en neem niet aan dat iedere versie vóór v0.12.4 door één specifieke fout wordt getroffen. De updategids waarschuwt voor eenrichtingsmigraties van databases en replica's met verschillende versies. Als meerdere workers of replica's één database delen, stop ze dan tegelijk en volg de [migratieprocedure voor meerdere replica's](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Voor een rollback heb je mogelijk de databaseback-up van vóór de upgrade nodig.

## Werk het geïnstalleerde pakket bij

**Docker, procedure van de leverancier aangepast aan een vastgezette tag:** haal na de back-up de officiële standaardimage op en maak de container opnieuw met hetzelfde persistente volume, dezelfde configuratie en dezelfde `WEBUI_SECRET_KEY`. Dit voorbeeld gaat uit van het standaard benoemde volume en een lokaal gekoppelde proxy-upstream. Plak je echte sleutel niet in de shellgeschiedenis. Lever de sleutel aan via je bestaande beveiligde omgevingsmechanisme of geheimenbeheer. Behoud de GPU-, Ollama-, aangepaste netwerk-, database- en andere opties van je huidige installatie. [Open WebUI bijwerken](https://docs.openwebui.com/getting-started/updating/) · [Officiële imagetags](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Controleer `./open-webui.env` voordat je de opdracht uitvoert:** het bestand moet al bestaan, beperkte bestandsrechten hebben en je bestaande `WEBUI_SECRET_KEY` en vereiste configuratie bevatten. De loopback-koppeling past bij een proxy op dezelfde host, niet bij een proxy op een andere machine. Wijzig bij Compose alleen de service-image naar de vastgezette tag. Voer vervolgens `docker compose pull open-webui` en `docker compose up -d open-webui` uit in het bestaande project. Behoud hetzelfde volume en dezelfde omgevingsconfiguratie. Dit zijn voorgestelde opdrachten, geen geteste migratie van jouw installatie.

**pip, updateprocedure van de leverancier met een vaste versie:** stop in de bestaande virtuele omgeving de service, installeer exact deze pakketversie en start de service opnieuw met dezelfde gegevensmap en omgeving. Gebruik geen tweede Python-omgeving of nieuwe lege database. De algemene update-instructie van de leverancier gebruikt `pip install -U open-webui`. De versiebeperking hieronder zet deze checklist vast op v0.12.4. [Open WebUI bijwerken](https://docs.openwebui.com/getting-started/updating/) · [Snelstart](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Controleer de draaiende service, niet alleen het geïnstalleerde pakket.** Bekijk de startversie in `docker logs open-webui` of de pip-servicelogboeken en vergelijk die na het aanmelden met de versie die de applicatie weergeeft. De updategids van de leverancier adviseert om de containerlogboeken te controleren en de aanmeldpagina te laden. Als de interface verouderde resources toont, vernieuw de browser geforceerd. Als het opstarten een migratiefout meldt, houd de service dan offline tot je de oorzaak hebt vastgesteld. Zet geen oude binary terug op een gemigreerde database zonder de herstelvereisten te controleren. [Controles na de update](https://docs.openwebui.com/getting-started/updating/)

## Controleer toegang na de herstart

**Gedrag volgens de leverancier:** v0.12.4 verbergt Map exporteren, Exporteren van gearchiveerde chats en Chats kopiëren voor gebruikers zonder **Allow Chat Export**. De toegangscontroles voor modellen, prompts, tools, kennis, vaardigheden, notities en mappen zijn ook verborgen voor gebruikers zonder de bijbehorende deelrechten. Kijkers van een gedeelde map ontvangen geen live chatupdates meer nadat de eigenaar een chat archiveert. Kijkers van een deellink ontvangen geen live updates meer nadat de eigenaar het delen van alle chats heeft beëindigd. Verborgen bedieningselementen zijn gedrag van de interface, geen bewijs van een serveroplossing voor een niet nader genoemde kwetsbaarheid. [Releaseopmerkingen](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Aanbevolen controle voor beheerders:** controleer met een testaccount zonder export- en deelrechten of de genoemde acties ontbreken. Bevestig met een account dat de rechten heeft dat de bedoelde acties nog werken. Maak een niet-gevoelige testchat in een gedeelde map, open die vanuit een ander account, archiveer de chat als eigenaar en controleer of nieuwe updates de kijker niet meer bereiken. Herhaal dit met een deellink en **Unshare All Chats**. Controleer opgeslagen toegangsrechten en oude links opnieuw. Ga er niet van uit dat gearchiveerde inhoud of historische kopieën zijn verwijderd.

| Controlegebied | Wat je controleert |
|---|---|
| **Rollen en groepen** | Verwijder verouderde leden en beheerdersrollen. Controleer de effectieve rechten van een pas goedgekeurde gebruiker en een gebruiker met beperkingen. |
| **Modellen en tools** | Controleer toegangsrechten per model, gekoppelde tools, rechten om tools te maken en inloggegevens van providers. Test met een niet-beheerdersaccount. |
| **Kennis en bestanden** | Bekijk bijdragers aan de kennisbank, resourcerechten, bijlagen en deelinstellingen. Controleer een account waarvan de toegang is ingetrokken. |
| **Chats en exports** | Controleer gedeelde mappen, deellinks, gearchiveerde chats en toewijzingen van Allow Chat Export. Trek ongebruikte links in. |

Deze inventariscontroles zijn **aanbevelingen voor beheerders**, geen nieuwe garanties van v0.12.4. De [verhardingsgids](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) van de leverancier beschrijft gelaagde rollen, groepen, rechten per resource, werkruimtemachtigingen, API-sleutels en netwerkplaatsing.

## Dicht hiaten in accounts en netwerk

- **Registratie, instelling van de leverancier:** schakel open registratie uit als een beheerder of identiteitsprovider accounts aanmaakt. Controleer `ENABLE_SIGNUP` en permanente beheerinstellingen aan de hand van de [verhardingsgids](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Houd de goedkeuringsregels voor nieuwe accounts streng.
- **API-sleutels, controle door beheerder:** inventariseer uitgegeven sleutels, verwijder ongebruikte sleutels en beperk het maken ervan en toegang tot endpoints tot de benodigde rollen en routes. Volgens de verhardingsgids van de leverancier werkt een sleutel met de rechten van de maker. Zet sleutels niet in artikelvoorbeelden of applicatielogboeken.
- **Beheerders, controle door beheerder:** verwijder verlaten beheerdersaccounts, verplicht sterke aanmeldcontroles, controleer of MFA beschikbaar is en onderzoek onverwachte accountwijzigingen. Test accountherstel voordat je een overbodige beheerder uitschakelt.
- **Netwerkgrens, richtlijn van de leverancier:** plaats de service achter een VPN, toegangsproxy of reverse proxy met authenticatie en een IP-allowlist. Stel de service niet publiek beschikbaar zonder authenticatie. Vermijd `WEBUI_AUTH=False` op een bereikbare service. Een reverse proxy zonder eigen authenticatie vervangt de aanmelding van de applicatie niet. [Open WebUI beveiligen](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Reikwijdte:** deze checklist geldt voor de officiële Open WebUI-release en de gedocumenteerde standaardinstallaties. De checklist controleert geen forks, afgeleide images of pakketten van derden. De opmerkingen bij v0.12.4 melden geen actieve uitbuiting. Raadpleeg de [beveiligingsadviezen van het project](https://github.com/open-webui/open-webui/security/advisories) voor latere bekendmakingen en de eigen getroffen en opgeloste versies. Schrijf een eerdere beveiligingsoplossing niet aan v0.12.4 toe zonder het versiegebied te lezen.

## Bronnen en verwijzingen

- [Releaseopmerkingen Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Beveiligingsadviezen Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Open WebUI bijwerken, met back-up, rollback en migraties](https://docs.openwebui.com/getting-started/updating/)
- [Open WebUI-snelstart en officiële imagetags](https://docs.openwebui.com/getting-started/quick-start/)
- [Open WebUI beveiligen](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Updates en migraties voor meerdere replica's](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)
