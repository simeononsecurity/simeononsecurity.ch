---
title: "Test DNS- en WebRTC-lekken in je browser met een VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Controleer het openbare IP-adres, de DNS-resolver en WebRTC-adressen van je browser voor en na het verbinden met een VPN. Interpreteer de resultaten en onderzoek routeringsproblemen."
genre: ["Privacy", "Browsers", "Netwerken"]
tags: ["DNS-lektest", "WebRTC-lektest", "VPN-lektest", "browserprivacytest", "IP-adreslek", "DNS over HTTPS", "veilige DNS", "Firefox DNS", "Chrome veilige DNS", "WebRTC-kandidaten", "VPN split tunneling", "IPv6-lek", "resolvertest", "browserprivacy", "netwerkprivacy", "VPN-problemen oplossen", "DNS-resolver", "ICE-kandidaten", "privé-IP-adres", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Browservenster met drie panelen voor openbaar IP, DNS en peerverbindingen, plus een doorlopende tunnel en een gestippelde alternatieve route naar externe servers."
coverCaption: "Vergelijk elke netwerkroute voor en na het verbinden met je VPN."
---

Het verbindingspictogram van een virtueel privénetwerk (VPN) bewijst niet dat elk browserverzoek dezelfde route volgt. Test je **openbare IP-adres**, **resolver van het Domain Name System (DNS)** en **WebRTC-adressen** afzonderlijk. Elk resultaat beantwoordt een andere vraag. Deze gids biedt een herhaalbare controle en een manier om onverwachte resultaten te onderzoeken.

<!--more-->

## Belangrijkste punten

- **Vergelijk twee situaties:** Leg dezelfde tests vast voor en na het verbinden met je VPN.
- **Beoordeel elk resultaat apart:** Een gewijzigd openbaar IP-adres toont niet waar DNS-query's naartoe gingen.
- **Controleer WebRTC-kandidaten:** Zoek naar een openbaar adres buiten de bedoelde route. Een privé-adres heeft een andere betekenis.
- **Wijzig één instelling tegelijk:** Test opnieuw na elke wijziging aan VPN, browser of DNS.

## Voordat je begint

Gebruik de browser en netwerkverbinding die je wilt beveiligen. Bepaal of de VPN het hele apparaat of alleen bepaalde apps moet omvatten. Als je VPN split tunneling gebruikt, noteer dan of de testbrowser door de tunnel gaat. Houd het DNS-beleid van de VPN-client bij de hand.

**Split tunneling** stuurt sommige apps via de VPN en andere apps via het normale netwerk.

Deze procedure gebruikt de pagina's [IP van BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) en [WebRTC](https://browserleaks.com/webrtc). De dienst ziet je verbindingsadres wanneer je de pagina bezoekt. Volgens de testbeschrijving vraagt de DNS-test de browser om 50 willekeurige namen op te zoeken. Voer zonder toestemming geen externe test uit op een beheerd of beperkt netwerk. Vul geen inloggegevens, interne hostnamen of privé-browsegegevens in op een testsite.

> **Waarschuwing:** Zet exacte IP-adressen niet in openbare schermafbeeldingen of supportberichten. Noteer of de adressen overeenkomen met de verwachte route van je internetprovider of VPN. Deel de werkelijke waarden alleen via een goedgekeurd supportkanaal.

## Wat elke test laat zien

| Controle | Wat je vergelijkt | Wat de uitslag niet bewijst |
|---|---|---|
| **Openbaar IP** | Adres dat een gewone website ziet | Welke resolver DNS heeft afgehandeld |
| **DNS-resolver** | Servers die bij nieuwe naamopvragingen worden waargenomen | Waar elke app DNS naartoe stuurt |
| **WebRTC** | Lokale en openbare verbindingskandidaten | Welke kandidaat een later gesprek gebruikt |

De pagina voor openbare IP-adressen meldt het adres van het webverzoek. De DNS-pagina start nieuwe opvragingen en toont de resolvers die ze afhandelen. WebRTC, een afkorting van Web Real-Time Communication, laat browserapps peerverbindingen maken. De WebRTC-pagina controleert welke adressen tijdens die verbindingen zichtbaar worden. Een **ICE-kandidaat** is een mogelijk netwerkadres voor een peerverbinding. Een **VPN-uitgang** is het openbare adres dat verkeer gebruikt nadat het de VPN verlaat. [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) legt uit waarom WebRTC-kandidaten soms andere adressen bevatten dan een gewoon webverzoek, vooral bij split tunnels of proxy's.

Een DNS-server van je VPN-aanbieder, een andere resolver die je binnen de VPN hebt gekozen, of een versleutelde resolver die de browser selecteert, geeft verschillende namen weer. De naam van de resolver alleen wijst geen lek aan. Vergelijk de naam met het beleid dat je wilde gebruiken.

## Leg een beginsituatie vast

Verbreek de VPN alleen als je situatie een uitgangsmeting zonder tunnel toelaat. Open de drie testpagina's in een normaal browserprofiel. Voer de DNS-test uit en wacht op het resultaat. Noteer deze gegevens zonder exacte adressen openbaar te maken:

| Veld | Beginsituatie |
|---|---|
| **Browser en versie** | Naam, versie en relevante privacy-extensies |
| **Netwerk** | Wifi thuis, mobiele hotspot of een ander goedgekeurd netwerk |
| **Openbare IPv4 en IPv6** | Of elk adres bij je gewone verbinding hoort |
| **DNS-resultaat** | Getoonde namen of beheerders van resolvers |
| **WebRTC-resultaat** | Getoonde openbare, privé- of `.local`-kandidaten |

Als je de VPN niet kunt verbreken, begin dan met de verwachte VPN-route en markeer de beginsituatie zonder tunnel als niet beschikbaar. Leid je gewone provideradres niet af uit een locatielabel of kaart. Locatiedatabases kunnen afwijken van de werkelijke netwerkbeheerder.

## Herhaal de test met de VPN verbonden

Verbind met de VPN en controleer of de client een actieve tunnel meldt. Laad elke testpagina opnieuw in **hetzelfde browserprofiel**. Voer de DNS-test nogmaals uit om nieuwe opvragingen te maken. Noteer IPv4- en IPv6-resultaten als de dienst ze toont.

Vergelijk de resultaten in deze volgorde:

1. **Openbaar IP:** Het webverzoek hoort een adres te tonen dat overeenkomt met de VPN-uitgang of de route die je bewust hebt ingesteld. Als de browser in de tunnel hoort, duidt het gewone provideradres op een routeringsprobleem.
2. **DNS:** Vergelijk elke getoonde resolver met de DNS-instellingen van de VPN en browser. Onderzoek een resolver van je internetprovider buiten de verwachte tunnel. Een benoemde externe resolver is normaal als je die bewust in de browser hebt geselecteerd.
3. **WebRTC:** Vergelijk de openbare WebRTC-kandidaat met de VPN-uitgang en het openbare basis-IP. Als al het browserverkeer via de VPN hoort te lopen, verdient een normaal provideradres dat alleen in WebRTC verschijnt nader onderzoek.
4. **Privéadressen:** Een adres uit de [privébereiken van RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) of een `.local`-kandidaat verschilt van een openbaar provideradres. Noteer de lokale waarde en bepaal of de website deze hoort te kennen.

De [WebRTC IP-verwerkingsstandaard](https://datatracker.ietf.org/doc/html/rfc8828) beschrijft hoe een app via ICE-kandidaatdetectie andere openbare of privé-adressen leert. Het ontwerp voor [mDNS-hostkandidaten van Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) vervangt sommige privé-adressen door `.local`-namen. Een leeg WebRTC-resultaat is **onbeslist** als JavaScript, de API of de testserver niet werkte. Een leeg resultaat bewijst geen volledige bescherming.

> **Verwacht resultaat:** Het gewone webverzoek van de browser en openbare WebRTC-kandidaten volgen de gekozen route. De DNS-resultaten komen overeen met het VPN- of browserresolverbeleid dat je hebt genoteerd.

## Onderzoek een DNS-afwijking

Controleer eerst of de browser zelf een resolver kiest. De [DNS over HTTPS-instellingen van Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) tonen de actieve status en het beschermingsniveau. Standaardbescherming valt onder bepaalde voorwaarden terug op de systeemresolver en houdt rekening met netwerksignalen. De niveaus Verhoogd en Aangepast gebruiken een gekozen aanbieder met terugvalgedrag. Maximale bescherming waarschuwt wanneer beveiligde naamomzetting mislukt. De status en uitzonderingenlijst zijn belangrijker dan alleen een schakelaar.

De [gids voor Secure DNS van Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) beschrijft de automatische modus en een aangepaste aanbieder. In de automatische modus volgt een onversleutelde opvraging als beveiligde naamomzetting mislukt. Een aangepaste aanbieder schakelt niet standaard terug naar onversleutelde modus. Beheerde apparaten en ouderlijk toezicht beperken deze instelling. Bekijk de huidige browserinterface voordat je een beheerd beleid wijzigt.

Als de browserresolver niet de oorzaak is, vergelijk dan de DNS-instelling van de VPN-client, de lijst met apps voor split tunneling, de systeemresolver en de IPv6-route. Wijzig één onderdeel en herhaal de DNS-test. Een browser-DNS-test meet de opvragingsroute van die browser. De uitslag zegt niet hoe een andere app namen omzet. Als je netwerk [DNS-filtering](/articles/nextdns-vs-adguard-ad-blocker-comparison/) gebruikt, test dan een domein dat je bewust blokkeert en een domein dat je toestaat. Zie het ontbreken van een advertentie niet als bewijs van de resolverroute.

## Onderzoek een WebRTC-afwijking

Controleer of de browser buiten de VPN-tunnel valt of een proxy buiten de bedoelde route gebruikt. Herstel de route en test opnieuw. Schakel IPv6 of WebRTC niet uit als eerste reactie op één onduidelijke uitslag. De [WebRTC-standaard](https://datatracker.ietf.org/doc/html/rfc8828) beschrijft de afweging tussen adresblootstelling en prestaties van directe gesprekken. Kandidaten beperken of een proxy afdwingen beïnvloedt videogesprekken en andere peerverbindingen.

Als je browser of VPN een gedocumenteerde instelling voor WebRTC-IP-verwerking biedt, lees dan de huidige beschrijving en kies een beleid dat past bij je gebruik van gesprekken. Test de openbare kandidaat opnieuw. Een lokaal adres alleen bewijst niet dat je openbare provideradres buiten de VPN kwam. Een zichtbaar openbaar provideradres naast een ander VPN-HTTP-adres is een sterker signaal.

## Bewaar een testverslag

| Veld | Vast te leggen resultaat |
|---|---|
| **Datum en browser** | Versie, profiel, extensies en netwerk |
| **Verwachte route** | VPN voor het hele apparaat, split tunnel of browserproxy |
| **Voor en na** | Beheerder van openbaar IP, DNS-beheerder en openbare WebRTC-kandidaat |
| **Afwijking** | Welk resultaat niet overeenkwam met het bedoelde beleid |
| **Eén wijziging** | Gewijzigde instelling en reden |
| **Hertest** | Nieuw resultaat en resterende onzekerheid |

Herhaal de controle na wijzigingen aan de browser-, VPN- of netwerkconfiguratie. Een goede uitslag geldt voor de geteste browser, het profiel, het netwerk en het moment. Ze bewijst geen anonimiteit en dekt niet elke app. Als je nog een browser kiest, bekijk dan de [vergelijking van privacybrowsers](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) voor functies en voer deze test daarna op je eigen configuratie uit.

## Volgende stappen

Herhaal de test na wijzigingen aan de browser, VPN of het netwerk. Gebruik de [vergelijking van privacybrowsers](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) bij je keuze.
