---
title: "Browser-DNS- und WebRTC-Lecks mit einem VPN testen"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Prüfe die öffentliche IP-Adresse, den DNS-Resolver und die WebRTC-Adressen deines Browsers vor und nach der VPN-Verbindung. Werte die Ergebnisse aus und grenze Routingprobleme ein."
genre: ["Datenschutz", "Browser", "Netzwerke"]
tags: ["DNS-Leak-Test", "WebRTC-Leak-Test", "VPN-Leak-Test", "Browser-Datenschutztest", "IP-Adressleck", "DNS over HTTPS", "sicheres DNS", "Firefox-DNS", "Chrome Secure DNS", "WebRTC-Kandidaten", "VPN-Split-Tunneling", "IPv6-Leck", "Resolver-Test", "Browser-Datenschutz", "Netzwerkdatenschutz", "VPN-Fehlerbehebung", "DNS-Resolver", "ICE-Kandidaten", "private IP-Adresse", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Ein Browserfenster mit drei Bereichen für öffentliche IP, DNS und Peer-Verbindungen sowie einem durchgezogenen Tunnel und einem gestrichelten Alternativpfad zu entfernten Servern."
coverCaption: "Vergleiche jeden Netzwerkpfad vor und nach der VPN-Verbindung."
---

Das Verbindungssymbol eines **Virtual Private Network (VPN)** beweist nicht, dass jede Browseranfrage denselben Weg nimmt. Prüfe deine **öffentliche IP-Adresse**, deinen **Resolver des Domain Name System (DNS)** und deine **WebRTC-Adressen** getrennt. Jedes Ergebnis beantwortet eine andere Frage. Diese Anleitung bietet eine wiederholbare Prüfung und zeigt, wie du ein unerwartetes Ergebnis untersuchst.

<!--more-->

## Wichtigste Erkenntnisse

- **Vergleiche zwei Zustände:** Notiere dieselben Testergebnisse vor und nach der VPN-Verbindung.
- **Werte jedes Ergebnis einzeln aus:** Eine geänderte öffentliche IP zeigt nicht, wohin DNS-Anfragen gingen.
- **Prüfe WebRTC-Kandidaten:** Achte auf eine öffentliche Adresse außerhalb des vorgesehenen Pfads. Eine private Adresse bedeutet etwas anderes.
- **Ändere eine Einstellung:** Wiederhole den Test nach jeder Anpassung an VPN, Browser oder DNS.

## Vorbereitung

Verwende den Browser und die Netzwerkverbindung, die du schützen möchtest. Kläre, ob das VPN das ganze Gerät oder nur ausgewählte Apps abdecken soll. Wenn dein VPN Split-Tunneling nutzt, notiere, ob der Testbrowser durch den Tunnel läuft. Halte die DNS-Richtlinie des VPN-Clients zum Vergleich bereit.

**Split-Tunneling** leitet ausgewählte Apps durch das VPN, während andere Apps das normale Netzwerk verwenden.

Dieses Verfahren nutzt die Seiten [BrowserLeaks IP](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) und [WebRTC](https://browserleaks.com/webrtc). Der Dienst sieht beim Aufruf deine Verbindungsadresse. Laut Testbeschreibung lässt der DNS-Test den Browser 50 zufällige Namen auflösen. Führe keinen externen Test in einem verwalteten oder eingeschränkten Netzwerk ohne Genehmigung aus. Gib auf einer Testseite keine Zugangsdaten, internen Hostnamen oder privaten Browserverläufe ein.

> **Warnung:** Zeige deine genauen IP-Adressen nicht in öffentlichen Screenshots oder Supportbeiträgen. Notiere, ob die Adressen zu deinem erwarteten ISP- oder VPN-Pfad passen. Teile tatsächliche Werte nur über einen genehmigten Supportkanal.

## Ergebnisse der Tests

| Prüfung | Was du vergleichst | Was das Ergebnis nicht beweist |
|---|---|---|
| **Öffentliche IP** | Adresse, die eine normale Website sieht | Welcher Resolver DNS verarbeitet hat |
| **DNS-Resolver** | Server bei neuen Namensabfragen | Wohin jede App DNS sendet |
| **WebRTC** | Lokale und öffentliche Verbindungskandidaten | Welchen Kandidaten ein späterer Anruf nutzt |

Die Seite für öffentliche IP-Adressen meldet die Adresse der Webanfrage. Die DNS-Seite löst neue Namen auf und meldet die dafür verwendeten Resolver. WebRTC steht für Web Real-Time Communication und ermöglicht Browser-Apps Peer-Verbindungen. Die WebRTC-Seite prüft Adressen, die bei diesen Verbindungen sichtbar werden. Ein **ICE-Kandidat** ist eine mögliche Netzwerkadresse für eine Peer-Verbindung. Ein **VPN-Ausgang** ist die öffentliche Adresse, die der Datenverkehr nach dem Verlassen des VPN nutzt. Die [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) erklärt, warum WebRTC-Kandidaten manchmal weitere Adressen enthalten, die bei einer normalen Webanfrage nicht sichtbar sind. Das kommt besonders bei Split-Tunneln oder Proxys vor.

Ein DNS-Server deines VPN-Anbieters, ein innerhalb des VPN gewählter separater Resolver oder ein im Browser gewählter verschlüsselter Resolver zeigen im Test unterschiedliche Namen. Ein Resolvername allein belegt kein Leck. Vergleiche ihn mit der gewünschten Richtlinie.

## Ausgangswerte erfassen

Trenne die VPN-Verbindung nur, wenn ein ungetunnelter Ausgangstest für dich infrage kommt. Öffne alle drei Testseiten in einem normalen Browserprofil. Führe den DNS-Test aus und warte auf das Ergebnis. Notiere Folgendes, ohne genaue Adressen zu veröffentlichen:

| Feld | Ausgangsnotiz |
|---|---|
| **Browser und Version** | Name, Version und relevante Datenschutz-Erweiterungen |
| **Netzwerk** | Heim-WLAN, mobiler Hotspot oder ein anderes freigegebenes Netzwerk |
| **Öffentliche IPv4 und IPv6** | Ob die jeweilige Adresse zu deiner normalen Verbindung gehört |
| **DNS-Ergebnis** | Angezeigte Resolvernamen oder Betreiber |
| **WebRTC-Ergebnis** | Angezeigte öffentliche, private oder `.local`-Kandidaten |

Wenn du das VPN nicht trennen kannst, beginne mit dem erwarteten VPN-Pfad und kennzeichne den ungetunnelten Ausgangstest als nicht verfügbar. Leite die normale ISP-Adresse nicht aus einem Standortnamen oder einer Karte ab. Standortdatenbanken weichen mitunter vom tatsächlichen Netzbetreiber ab.

## Mit verbundenem VPN testen

Verbinde das VPN und prüfe, ob der Client einen funktionierenden Tunnel meldet. Lade jede Testseite im **selben Browserprofil** neu. Führe den DNS-Test erneut aus, damit neue Namensabfragen entstehen. Notiere IPv4- und IPv6-Ergebnisse, sofern der Dienst sie meldet.

Vergleiche die Ergebnisse in dieser Reihenfolge:

1. **Öffentliche IP:** Die Webanfrage sollte eine Adresse zeigen, die zum VPN-Ausgang oder zum bewusst eingerichteten Pfad passt. Sollte der Browser durch den Tunnel laufen, weist eine unveränderte normale ISP-Adresse auf ein Routingproblem hin.
2. **DNS:** Vergleiche jeden gemeldeten Resolver mit den DNS-Einstellungen von VPN und Browser. Ein ISP-Resolver außerhalb des vorgesehenen Tunnels erfordert eine Untersuchung. Ein benannter Drittanbieter-Resolver ist zu erwarten, wenn du ihn im Browser bewusst ausgewählt hast.
3. **WebRTC:** Vergleiche den öffentlichen WebRTC-Kandidaten mit dem VPN-Ausgang und der öffentlichen Ausgangs-IP. Wenn der gesamte Browserverkehr durch das VPN laufen soll, ist die normale öffentliche ISP-Adresse, die nur bei WebRTC erscheint, ein Anlass zur Prüfung.
4. **Private Adressen:** Eine Adresse aus den [privaten Bereichen der RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) oder ein `.local`-Kandidat unterscheidet sich von einer öffentlichen ISP-Adresse. Notiere den lokalen Eintrag und prüfe, ob die Website diese Adresse erfahren soll.

Der [WebRTC-Standard zur Adressverarbeitung](https://datatracker.ietf.org/doc/html/rfc8828) beschreibt, wie eine App über ICE-Kandidaten weitere öffentliche oder private Adressen erkennt. Das [mDNS-Hostkandidaten-Design von Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) ersetzt einige private Adressen durch `.local`-Namen. Ein leeres WebRTC-Ergebnis ist **nicht aussagekräftig**, wenn JavaScript, die API oder der Testserver nicht funktioniert hat. Ein leeres Ergebnis beweist keinen vollständigen Schutz.

> **Erwartetes Ergebnis:** Die normale Webanfrage deines Browsers und öffentliche WebRTC-Kandidaten folgen dem gewählten Pfad. DNS-Ergebnisse entsprechen der notierten DNS-Richtlinie von VPN oder Browser.

## DNS-Abweichungen untersuchen

Prüfe zuerst, ob der Browser einen eigenen Resolver verwendet. Die [DNS-over-HTTPS-Einstellungen von Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) zeigen den aktiven Status und die Schutzstufe. Der Standardschutz wechselt unter bestimmten Bedingungen zum Systemresolver und beachtet Netzwerksignale. Erhöhter und benutzerdefinierter Schutz nutzen einen gewählten Anbieter mit Ausweichverhalten. Der maximale Schutz warnt, wenn die sichere Auflösung fehlschlägt. Status und Ausnahmeliste sind aussagekräftiger als ein einzelner Schalter.

Der [Secure-DNS-Leitfaden von Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) beschreibt den automatischen Modus und einen benutzerdefinierten Anbieter. Der automatische Modus wechselt bei einem Fehler der sicheren Abfrage zu einer unverschlüsselten Abfrage. Ein benutzerdefinierter Anbieter wechselt nicht standardmäßig in den unverschlüsselten Modus. Verwaltete Geräte und Jugendschutz können diese Einstellung einschränken. Prüfe die aktuelle Browseroberfläche, bevor du eine verwaltete Richtlinie änderst.

Wenn der Browserresolver nicht die Ursache ist, vergleiche die DNS-Einstellung des VPN-Clients, die App-Liste des Split-Tunnels, den Resolver des Betriebssystems und die IPv6-Route. Ändere einen Punkt und wiederhole den DNS-Test. Ein Browser-DNS-Test misst den Namensauflösungspfad des getesteten Browsers. Er zeigt nicht, wie eine andere App Namen auflöst. Wenn dein Netzwerk [DNS-Filterung](/articles/nextdns-vs-adguard-ad-blocker-comparison/) nutzt, teste eine absichtlich blockierte und eine erlaubte Domain. Eine fehlende Anzeige beweist nicht, welchen Resolver der Browser verwendet.

## WebRTC-Abweichungen untersuchen

Prüfe, ob der Browser vom VPN-Tunnel ausgeschlossen ist oder einen Proxy außerhalb des vorgesehenen Pfads verwendet. Wiederhole den Test nach einer Korrektur des Pfads. Deaktiviere IPv6 oder WebRTC nicht als erste Reaktion auf ein einzelnes unklareres Ergebnis. Der [WebRTC-Standard](https://datatracker.ietf.org/doc/html/rfc8828) beschreibt den Zielkonflikt zwischen Adressfreigabe und direkter Anrufleistung. Eingeschränkte Kandidaten oder ein erzwungener Proxy wirken sich auf Videoanrufe und andere Peer-Verbindungen aus.

Wenn dein Browser oder VPN eine dokumentierte Einstellung zur WebRTC-IP-Behandlung bietet, lies die aktuelle Beschreibung und wähle eine Richtlinie, die zu deiner Nutzung von Anrufen passt. Prüfe den öffentlichen Kandidaten erneut. Eine lokale Adresse allein beweist nicht, dass deine öffentliche ISP-Adresse das VPN verlassen hat. Eine sichtbare öffentliche ISP-Adresse im Vergleich zu einer anderen VPN-HTTP-Adresse ist ein stärkeres Signal.

## Testergebnisse festhalten

| Feld | Einzutragendes Ergebnis |
|---|---|
| **Datum und Browser** | Version, Profil, Erweiterungen und Netzwerk |
| **Erwarteter Pfad** | VPN für das ganze Gerät, Split-Tunnel oder Browserproxy |
| **Vorher und nachher** | Betreiber der öffentlichen IP, DNS-Betreiber, öffentlicher WebRTC-Kandidat |
| **Abweichung** | Ergebnis, das der vorgesehenen Richtlinie widerspricht |
| **Einzelne Änderung** | Geänderte Einstellung und Grund |
| **Wiederholungstest** | Neues Ergebnis und verbleibende Unsicherheit |

Wiederhole die Prüfung nach Änderungen an Browser-, VPN- oder Netzwerkkonfiguration. Ein unauffälliges Ergebnis gilt für den getesteten Browser, das Profil, Netzwerk und den Zeitpunkt. Es beweist keine Anonymität und deckt nicht alle Apps ab. Wenn du noch einen Browser auswählst, nutze den [Vergleich datenschutzfreundlicher Browser](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) für die Funktionen und teste dann deine eigene Einrichtung.

## Nächste Schritte

Wiederhole den Test nach Änderungen an Browser, VPN oder Netzwerk. Nutze den [Vergleich datenschutzfreundlicher Browser](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/), wenn du einen Browser auswählst.
