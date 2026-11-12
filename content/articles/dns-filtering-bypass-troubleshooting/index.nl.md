---
title: "Waarom DNS-filtering wordt omzeild: test het resolverpad"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Achterhaal waarom een apparaat of browser je DNS-filter overslaat. Vergelijk directe en normale queries, controleer logs en bekijk versleutelde DNS, VPN, IPv6 en routerinstellingen."
genre: ["Thuisnetwerken", "DNS", "Privacy"]
tags: ["DNS-filtering omzeilen", "Pi-hole omzeilen", "DNS-querylog", "beveiligde DNS in browser", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "VPN-DNS", "IPv6-DNS", "router-DHCP-DNS", "Resolve-DnsName", "DNS-probleemoplossing", "DNS-filtertest", "NextDNS-probleemoplossing", "AdGuard-DNS-probleemoplossing"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "Het blauwe DNS-pad van een laptop loopt door een filter en stopt bij een blokkeersymbool, terwijl een oranje browserpad een andere resolver bereikt."
coverCaption: "Volg het querypad voordat je de filterregel wijzigt."
---

Je hebt een filterende resolver ingesteld, maar één apparaat bereikt nog steeds een domein dat volgens je beleid wordt geblokkeerd. De oorzaak kan de regel zijn, de Domain Name System (DNS)-toewijzing van het apparaat, een versleutelde resolver in de browser of een VPN. **Test het pad voordat je instellingen wijzigt.** Een directe query naar het filter beantwoordt een andere vraag dan een gewone query vanaf het apparaat.

<!--more-->

## Belangrijkste punten

- **Controleer eerst de regel:** Bevestig dat het filter een veilig testdomein ontvangt en blokkeert.
- **Volg elke laag:** Router, besturingssysteem, browser, VPN en mobiele instellingen beïnvloeden elk de DNS-routering.
- **Gebruik nieuwe queries:** Koppel een nieuwe hostnaam en tijdstip aan het querylog van het filter.
- **Benoem de beperking:** Eén waargenomen query bewijst één pad, niet dat elke app of elk apparaat hetzelfde doet.

## Voorbereiding

Trek ongeveer 20 minuten uit. Je hebt toegang nodig tot het querylog van de filterresolver, één apparaat met het probleem en de DNS-instellingen van de router. De voorbeelden gebruiken een Windows-laptop en **Pi-hole**, maar dezelfde vergelijking werkt met elke resolver die querylogs per client biedt. Zoek eerst het exacte adres van het filter op. Deel geen privé-clientadressen, querylogs of beleidsregels in een openbaar rapport.

Kies een **onschadelijk testdomein** dat je beleid al blokkeert. Je kunt ook tijdelijk een exacte weigerregel toevoegen voor een domein dat je beheert in een testprofiel. Noteer de regel en verwijder hem na de test. Gebruik geen actief malwaredomein als test. Een geblokkeerde pagina is een nuttig symptoom, maar het resolverlog levert sterker bewijs over het pad.

| Laag | Vraag |
|---|---|
| **Filter** | Bereikt een directe query de bedoelde resolver en komt deze overeen met de regel? |
| **Apparaat** | Welke DNS-servers wijst het netwerk toe? |
| **Browser of app** | Gebruikt deze client de resolver van het apparaat of een apart pad? |
| **VPN of relay** | Verandert een actieve tunnel de bestemming van queries? |

## Bewijs dat het filter werkt

Open het querylog van je resolver. Vraag het gekozen geblokkeerde domein rechtstreeks op bij het filter. Gebruik op Windows PowerShell en voer het filteradres en testdomein in wanneer daarom wordt gevraagd:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

De [referentie voor **`Resolve-DnsName`** van Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) beschrijft **`-Server`** als een query naar de opgegeven resolver. Zoek de query in het filterlog en controleer het antwoord en de bijpassende regel. De [query- en loggingdocumentatie van Pi-hole](https://docs.pi-hole.net/main/pihole-command/) beschrijft de lokale querytools. Als de directe query wordt toegestaan, herstel dan eerst de regel of de groepskoppeling van de client. Als de query het filter niet bereikt, controleer dan het adres, de service en het netwerkpad.

**Deze directe test bewijst niet dat de laptop het filter normaal gebruikt.** De optie **`-Server`** overschrijft voor deze query de standaardresolver. Dit onderscheid voorkomt een veelvoorkomende onterechte geslaagde test.

## Volg het apparaatpad

Gebruik een nieuwe hostnaam om een eerder DNS-cache-item te vermijden. Het volgende voorbeeld stuurt één query rechtstreeks naar het filter en een tweede via de normale resolverselectie van de laptop. De namen verschillen, zodat je weet welke logregel bij welk pad hoort. Een antwoord **NXDOMAIN** betekent dat de DNS-server meldt dat de hostnaam niet bestaat. Dat antwoord is normaal als de willekeurige naam niet wordt gebruikt. Hier telt of de query in het filterlog verschijnt.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Zoek beide exacte namen op in het filterlog en noteer de tijd en de gemelde client. Als **`direct-`** verschijnt maar **`default-`** niet, controleer dan de DNS-servers die aan de laptop zijn toegewezen. Op Windows toont **`Get-DnsClientServerAddress`** DNS-serveradressen per interface. Controleer de actieve wifi- of ethernetadapter, niet een losgekoppelde adapter. De [DNS-clientreferentie van Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) beschrijft deze alleen-lezen opdracht.

Laat fouten zichtbaar bij de eerste test. Een fout of time-out vraagt om een afzonderlijke diagnose en is iets anders dan een ontbrekende logregel.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Veeg de IPv4- en IPv6-regels na. **DHCP** wijst netwerkinstellingen toe, waaronder DNS-servers. **IPv6** is de nieuwere Internet Protocol-adresfamilie met adressen van 128 bits. Een IPv4-lease kan het filter aanwijzen terwijl IPv6-routeradvertenties een andere DNS-server doorgeven. Controleer de **DHCP**- en **IPv6-DNS**-advertenties van de router en vernieuw daarna de netwerklease van het apparaat. De [installatiehandleiding van Pi-hole](https://docs.pi-hole.net/main/post-install/) legt uit hoe DHCP clients naar Pi-hole verwijst. Het [routervoorbeeld](https://docs.pi-hole.net/routers/fritzbox/) behandelt IPv6-DNS-advertenties.

Als het log de **router** als client toont, stuurt de router mogelijk namens apparaten queries door. Het filterlog bewijst dan dat de router het filter bereikte, niet welk apparaat de query startte. Bevestig de doorstuurinrichting van de router voordat je ontbrekende clientidentiteit als ontbrekende gegevens beschouwt.

## Controleer browser-DNS

Een opdrachtregelquery test het resolverpad van het apparaat. Een browser kan in plaats daarvan **DNS over HTTPS (DoH)** gebruiken. Open hetzelfde geblokkeerde testdomein in de browser en controleer het filterlog op een bijbehorende query. Wis de DNS-cache van de browser of gebruik een nieuwe hostnaam onder een testregel wanneer gecachte resultaten de vergelijking vertroebelen.

Open op **Chrome op een computer** **Instellingen > Privacy en beveiliging > Beveiliging > Beveiligde DNS gebruiken**. Volgens de [Chrome-help van Google](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) gebruikt de automatische modus de huidige provider en valt deze bij een storing terug op onversleutelde opvragingen. Een gekozen aangepaste provider valt niet op dezelfde manier terug. Noteer de gekozen modus en provider voordat je iets wijzigt.

Open in **Firefox** **Instellingen > Privacy & Beveiliging > DNS over HTTPS**. De [handleiding voor beschermingsniveaus van Mozilla](https://support.mozilla.org/en-US/kb/dns-over-https) onderscheidt de modi Standaard, Verhoogd, Maximaal, Aangepast en Uit. Het [DoH-overzicht](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) legt uit wanneer een browserresolver een lokaal DNS-filter omzeilt. Test opnieuw na één gecontroleerde wijziging en herstel daarna de gewenste privacyinstelling.

**Noem elke ontbrekende browserquery niet meteen een omzeiling.** De browser kan gegevens uit de cache hergebruiken, een al bekend adres bereiken of een proxy gebruiken. Vergelijk een nieuwe naam, een passend tijdvenster en de browserinstelling voor de resolver voordat je concludeert waar de query naartoe ging.

## Mobiele en VPN-paden controleren

Controleer op **Android** **Instellingen > Netwerk en internet > Privé-DNS**. Een providerhostnaam selecteert een privé-DNS-service die afwijkt van DNS die je router adverteert. De [netwerkinstellingen van Android van Google](https://support.google.com/android/answer/9654714?hl=en) beschrijven de opties Uit, Automatisch en Providerhostnaam. Test via wifi met mobiele data uitgeschakeld voor een gecontroleerd lokaal resultaat en herstel daarna je normale instelling.

Controleer op **Apple-apparaten** of **iCloud Private Relay** actief is voor het netwerk en of Safari het verwachte pad gebruikt. Apple meldt dat [Private Relay Safari-verkeer en DNS-informatie beschermt](https://support.apple.com/en-gb/102602). De [netwerkbedieningselementen](https://support.apple.com/en-ie/102022) beschrijven de afhandeling per netwerk wanneer filtering conflicteert met Private Relay. Trek een Safari-resultaat niet door naar elke app op het apparaat.

Een **VPN** kan zijn eigen DNS-resolver aanbieden of queries door de tunnel sturen. Noteer of de VPN verbonden is, welke DNS-instellingen actief zijn en wat het split-tunnelbeleid doet. Vergelijk dezelfde test met de VPN aan en uit, alleen als je beveiligingsbeleid dit toestaat. Een gewijzigd resultaat wijst op een ander pad. Dat resultaat alleen bewijst geen lek of filterfout.

## Resultaten interpreteren

| Bewijs | Waarschijnlijke volgende controle |
|---|---|
| **Directe query ontbreekt in filterlog** | Filteradres, DNS-service, logging of netwerkbereikbaarheid |
| **Directe query toegestaan** | Exacte weigerregel, groepsbeleid of regelprioriteit |
| **Direct gelogd, standaard ontbreekt** | DHCP, statische DNS op apparaat, IPv6-DNS of VPN-resolver |
| **Standaard gelogd, browser ontbreekt** | Browser-DoH, browsercache, proxy of relay |
| **Beide gelogd en geblokkeerd, site laadt toch** | Andere hostnaam, gecachte inhoud, direct adres of app-pad |

**Ontbrekende logregels zijn dubbelzinnig** als logging uitstaat, de router namens de client doorstuurt of de test gecachte gegevens hergebruikt. Herhaal de test met een nieuwe hostnaam en controleer de querytijd voordat je firewallregels wijzigt. Het blokkeren van gewone DNS naar externe resolvers dwingt een versleutelde browser of VPN niet om je filter te gebruiken. De [OPNsense-handleiding van Pi-hole](https://docs.pi-hole.net/routers/opnsense/) presenteert het blokkeren van externe DNS als een optionele netwerkmaatregel. Apparaatbeleid en browserconfiguratie blijven afzonderlijke maatregelen.

## Oplossen en opnieuw testen

Wijzig één laag tegelijk. Corrigeer DHCP- of IPv6-DNS-advertenties, verwijder een onbedoelde statische resolver, kies de gewenste browser-DNS-provider of pas het DNS-beleid van de VPN aan. Verzwak versleutelde DNS of relaybescherming niet stilzwijgend op elk apparaat om één mislukte test op te lossen. Noteer het bronapparaat, de interface, het filteradres, de opgevraagde naam, het tijdstip, het antwoord, de client in het log, de browsermodus, de VPN-status en de wijziging.

Herhaal de **directe**, **standaard-** en **browsertests** na elke wijziging. Gebruik voor elke run een nieuwe hostnaam. Test elk netwerkprofiel afzonderlijk als een apparaat er meerdere heeft. De [DNS-resolververgelijking](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) helpt bij het kiezen van een service. De [browserlekkagetest](/articles/privacy-browser-leak-test-dns-webrtc/) beantwoordt een andere vraag: welke netwerkinformatie je browser- en VPN-inrichting verlaat. **Een betrouwbaar filterresultaat vereist een gecontroleerde regel en een gecontroleerd clientpad.**

## Volgende stappen

Herhaal de directe, standaard- en browsertests na elke gecontroleerde wijziging. Bekijk de [DNS-resolververgelijking](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) wanneer je een filterservice kiest.
