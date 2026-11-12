---
title: "Warum DNS-Filter umgangen werden: Den Resolverpfad prüfen"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Finde heraus, warum ein Gerät oder Browser deinen DNS-Filter umgeht. Vergleiche direkte und normale Abfragen, prüfe Protokolle sowie verschlüsseltes DNS, VPN, IPv6 und Routereinstellungen."
genre: ["Heimnetzwerke", "DNS", "Datenschutz"]
tags: ["DNS-Filter umgehen", "Pi-hole umgehen", "DNS-Abfrageprotokoll", "sicheres Browser-DNS", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "VPN-DNS", "IPv6-DNS", "Router-DHCP-DNS", "Resolve-DnsName", "DNS-Fehlerbehebung", "DNS-Filtertest", "NextDNS-Fehlerbehebung", "AdGuard-DNS-Fehlerbehebung"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "Der blaue DNS-Pfad eines Laptops läuft durch einen Filter und endet an einem Sperrsymbol, während ein orangefarbener Browserpfad einen anderen Resolver erreicht."
coverCaption: "Verfolge den Abfragepfad, bevor du die Filterregel änderst."
---

Du hast einen filternden Resolver eingerichtet, doch ein Gerät erreicht weiterhin eine Domain, die laut Richtlinie gesperrt sein sollte. Ursache können die Regel, die Zuweisung des Domain Name System (DNS) am Gerät, ein verschlüsselter Browserresolver oder ein VPN sein. **Prüfe den Pfad, bevor du Einstellungen änderst.** Eine direkte Abfrage an den Filter beantwortet eine andere Frage als eine normale Geräteabfrage.

<!--more-->

## Wichtigste Erkenntnisse

- **Prüfe zuerst die Regel:** Bestätige, dass der Filter eine harmlose Testdomain empfängt und blockiert.
- **Verfolge jede Ebene:** Router, Betriebssystem, Browser, VPN und mobile Einstellungen beeinflussen die DNS-Weiterleitung.
- **Nutze neue Abfragen:** Ordne einen neuen Hostnamen und Zeitstempel dem Abfrageprotokoll des Filters zu.
- **Benenne die Grenze:** Eine beobachtete Abfrage belegt einen Pfad, nicht das Verhalten jeder App oder jedes Geräts.

## Vorbereitung

Plane etwa 20 Minuten ein. Du brauchst Zugriff auf das Abfrageprotokoll des Filterresolvers, ein betroffenes Gerät und eine Aufzeichnung der DNS-Einstellungen des Routers. Die Beispiele verwenden einen Windows-Laptop und **Pi-hole**, aber derselbe Vergleich funktioniert mit jedem Resolver, der Abfragen je Client protokolliert. Ermittle zuerst die genaue Filteradresse. Veröffentliche keine privaten Clientadressen, Abfrageprotokolle oder Richtlinienregeln.

Wähle eine **harmlose Testdomain**, die deine Richtlinie bereits blockiert. Alternativ kannst du in einem Testprofil vorübergehend eine exakte Sperrregel für eine von dir kontrollierte Domain einrichten. Notiere die Regel und entferne sie nach dem Test. Nutze keine aktive Malware-Domain als Testziel. Eine blockierte Seite ist ein nützliches Symptom, aber das Resolverprotokoll liefert einen besseren Nachweis für den Pfad.

| Ebene | Frage |
|---|---|
| **Filter** | Erreicht eine direkte Abfrage den vorgesehenen Resolver und greift die Regel? |
| **Gerät** | Welche DNS-Server weist das Netzwerk zu? |
| **Browser oder App** | Nutzt der Client den Resolver des Geräts oder einen eigenen Pfad? |
| **VPN oder Relay** | Ändert ein aktiver Tunnel das Ziel der Abfragen? |

## Filterfunktion nachweisen

Öffne das Abfrageprotokoll deines Resolvers. Frage die ausgewählte blockierte Domain direkt beim Filter ab. Verwende unter Windows PowerShell und gib bei der Eingabeaufforderung Filteradresse und Testdomain an:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

Die [Microsoft-Referenz zu **`Resolve-DnsName`**](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) beschreibt **`-Server`** als Abfrage an den angegebenen Resolver. Suche die Abfrage im Filterprotokoll und prüfe Antwort sowie passende Regel. Die [Pi-hole-Dokumentation zu Abfragen und Protokollen](https://docs.pi-hole.net/main/pihole-command/) beschreibt lokale Abfragewerkzeuge. Wird die direkte Abfrage zugelassen, korrigiere zuerst die Regel oder die Gruppenzuweisung des Clients. Erreicht die Abfrage den Filter nicht, prüfe Adresse, Dienst und Netzwerkpfad.

**Dieser direkte Test beweist nicht, dass der Laptop den Filter normalerweise nutzt.** Die Option **`-Server`** überschreibt für diese Abfrage den Standardresolver. Diese Unterscheidung verhindert einen häufigen falsch positiven Test.

## Gerätepfad verfolgen

Nutze einen neuen Hostnamen, damit kein vorheriger DNS-Cacheeintrag greift. Das folgende Beispiel sendet eine Abfrage direkt an den Filter und eine weitere über die normale Resolverauswahl des Laptops. Die Namen unterscheiden sich, damit du den jeweiligen Protokolleintrag dem Pfad zuordnen kannst. Eine Antwort **NXDOMAIN** bedeutet, dass der DNS-Server meldet, der Hostname existiere nicht. Das ist normal, wenn der zufällige Name nicht verwendet wird. Entscheidend ist, ob die Abfrage im Filterprotokoll erscheint.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Suche beide exakten Namen im Filterprotokoll und notiere Zeit sowie gemeldeten Client. Erscheint **`direct-`**, aber nicht **`default-`**, prüfe die dem Laptop zugewiesenen DNS-Server. Unter Windows zeigt **`Get-DnsClientServerAddress`** DNS-Serveradressen je Schnittstelle. Prüfe den aktiven WLAN- oder Ethernetadapter, nicht einen getrennten Adapter. Die [Microsoft-Referenz zum DNS-Client](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) beschreibt diesen schreibgeschützten Befehl.

Lass Fehler beim ersten Test sichtbar. Ein Fehler oder Timeout braucht eine eigene Diagnose und ist von einem fehlenden Protokolleintrag zu unterscheiden.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Vergleiche IPv4- und IPv6-Zeilen. **DHCP** weist Netzwerkeinstellungen wie DNS-Server zu. **IPv6** ist die neuere Internet-Protocol-Adressfamilie mit 128-Bit-Adressen. Eine IPv4-Lease kann den Filter nennen, während IPv6-Routeranzeigen einen anderen DNS-Server bereitstellen. Prüfe die **DHCP-** und **IPv6-DNS-Anzeigen** des Routers und erneuere nach einer Korrektur die Netzwerklease des Geräts. Der [Pi-hole-Leitfaden nach der Installation](https://docs.pi-hole.net/main/post-install/) erklärt, wie DHCP Clients auf Pi-hole verweist. Das [Routerbeispiel](https://docs.pi-hole.net/routers/fritzbox/) behandelt IPv6-DNS-Anzeigen.

Zeigt das Protokoll den **Router** als Client, leitet der Router Abfragen möglicherweise stellvertretend für Geräte weiter. Das Filterprotokoll belegt dann, dass der Router den Filter erreicht hat, aber nicht, welches Gerät die Abfrage ausgelöst hat. Prüfe die Weiterleitungsarchitektur des Routers, bevor du die fehlende Clientidentität als Datenlücke wertest.

## Browser-DNS prüfen

Eine Abfrage über die Befehlszeile testet den Resolverpfad des Geräts. Ein Browser kann stattdessen **DNS over HTTPS (DoH)** nutzen. Öffne dieselbe blockierte Testdomain im Browser und beobachte, ob eine passende Abfrage im Filterprotokoll erscheint. Leere den DNS-Cache des Browsers oder nutze einen neuen Hostnamen mit einer Testregel, wenn gecachte Ergebnisse den Vergleich stören.

Öffne in **Chrome auf einem Computer** **Einstellungen > Datenschutz und Sicherheit > Sicherheit > Sicheres DNS verwenden**. Laut der [Chrome-Hilfe von Google](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) nutzt der automatische Modus den aktuellen Anbieter und wechselt bei einem Fehler auf unverschlüsselte Abfragen zurück. Ein ausgewählter benutzerdefinierter Anbieter wechselt nicht auf dieselbe Weise zurück. Notiere Modus und Anbieter, bevor du die Einstellung änderst.

Öffne in **Firefox** **Einstellungen > Datenschutz & Sicherheit > DNS über HTTPS**. Der [Mozilla-Leitfaden zu Schutzstufen](https://support.mozilla.org/en-US/kb/dns-over-https) unterscheidet die Modi Standard, Erhöht, Maximal, Benutzerdefiniert und Aus. Die [DoH-Übersicht](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) erklärt, wann ein Browserresolver einen lokalen DNS-Filter umgeht. Teste nach einer kontrollierten Einstellungsänderung erneut und stelle dann deine gewünschte Datenschutzeinstellung wieder her.

**Werte nicht jede fehlende Browserabfrage als Umgehung.** Der Browser kann gecachte Daten wiederverwenden, eine bereits bekannte Adresse erreichen oder einen Proxy nutzen. Vergleiche einen neuen Namen, ein passendes Zeitfenster und die Resolvereinstellung des Browsers, bevor du den Weg der Abfrage bestimmst.

## Mobile und VPN-Pfade prüfen

Prüfe unter **Android** **Einstellungen > Netzwerk & Internet > Privates DNS**. Ein Anbieterhostname wählt einen privaten DNS-Dienst, der sich vom DNS des Routers unterscheidet. Die [Android-Netzwerkeinstellungen von Google](https://support.google.com/android/answer/9654714?hl=en) beschreiben die Optionen Aus, Automatisch und Anbieterhostname. Teste für ein kontrolliertes lokales Ergebnis über WLAN bei ausgeschalteten Mobilfunkdaten und stelle danach deine normale Einstellung wieder her.

Prüfe auf **Apple-Geräten**, ob **iCloud Private Relay** für das Netzwerk aktiv ist und Safari den erwarteten Pfad nutzt. Apple zufolge [schützt Private Relay Safari-Verkehr und DNS-Informationen](https://support.apple.com/en-gb/102602). Die [Netzwerksteuerungen](https://support.apple.com/en-ie/102022) beschreiben die Behandlung pro Netzwerk, wenn Filterung mit Private Relay kollidiert. Übertrage ein Safari-Ergebnis nicht auf jede App des Geräts.

Ein **VPN** kann einen eigenen DNS-Resolver bereitstellen oder Abfragen durch den Tunnel leiten. Notiere, ob das VPN verbunden ist, welche DNS-Einstellungen gelten und wie die Split-Tunnel-Richtlinie aussieht. Vergleiche denselben Test nur dann mit ein- und ausgeschaltetem VPN, wenn deine Sicherheitsrichtlinie dies zulässt. Ein anderes Ergebnis zeigt einen anderen Pfad. Es beweist allein weder ein Leck noch einen Filterfehler.

## Ergebnisse einordnen

| Nachweis | Wahrscheinliche nächste Prüfung |
|---|---|
| **Direkte Abfrage fehlt im Filterprotokoll** | Filteradresse, DNS-Dienst, Protokollierung oder Netzwerkerreichbarkeit |
| **Direkte Abfrage wird zugelassen** | Exakte Sperrregel, Gruppenrichtlinie oder Regelpriorität |
| **Direkte Abfrage protokolliert, Standardabfrage fehlt** | DHCP, statisches Geräte-DNS, IPv6-DNS oder VPN-Resolver |
| **Standardabfrage protokolliert, Browserabfrage fehlt** | Browser-DoH, Browsercache, Proxy oder Relay |
| **Beide protokolliert und blockiert, Website lädt dennoch** | Anderer Hostname, gecachte Inhalte, direkte Adresse oder App-Pfad |

**Fehlende Protokolleinträge sind mehrdeutig**, wenn die Protokollierung ausgeschaltet ist, der Router für den Client weiterleitet oder der Test gecachte Daten nutzt. Wiederhole den Test mit einem neuen Hostnamen und prüfe die Abfragezeit, bevor du Firewallregeln änderst. Das Blockieren von unverschlüsseltem DNS zu externen Resolvern zwingt einen verschlüsselten Browser oder ein VPN nicht dazu, deinen Filter zu nutzen. Der [Pi-hole-Leitfaden für OPNsense](https://docs.pi-hole.net/routers/opnsense/) zeigt das Blockieren externer DNS-Abfragen als optionale Netzwerkkontrolle. Geräte- und Browsereinstellungen bleiben getrennte Kontrollen.

## Beheben und erneut testen

Ändere jeweils nur eine Ebene. Korrigiere DHCP- oder IPv6-DNS-Anzeigen, entferne einen unbeabsichtigten statischen Resolver, wähle den vorgesehenen Browser-DNS-Anbieter oder passe die DNS-Richtlinie des VPN an. Schwäche verschlüsseltes DNS oder Relay-Schutz nicht stillschweigend auf allen Geräten ab, um einen fehlgeschlagenen Einzeltest zu beheben. Notiere Quellgerät, Schnittstelle, Filteradresse, abgefragten Namen, Zeit, Antwort, Client im Protokoll, Browsermodus, VPN-Status und die Änderung.

Wiederhole nach jeder Änderung die **direkten**, **normalen** und **Browser-Tests**. Nutze für jeden Durchlauf einen neuen Hostnamen. Hat ein Gerät mehrere Netzwerkprofile, teste jedes einzeln. Der [DNS-Resolververgleich](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) hilft bei der Auswahl eines Dienstes. Der [Browser-Lecktest](/articles/privacy-browser-leak-test-dns-webrtc/) beantwortet eine andere Frage: Welche Netzwerkinformationen verlassen deine Browser- und VPN-Konfiguration? **Ein zuverlässiges Filterergebnis braucht eine überprüfte Regel und einen überprüften Clientpfad.**

## Nächste Schritte

Wiederhole die direkten, normalen und Browser-Tests nach jeder kontrollierten Änderung. Sieh dir den [DNS-Resolververgleich](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) an, wenn du einen Filterdienst auswählst.
