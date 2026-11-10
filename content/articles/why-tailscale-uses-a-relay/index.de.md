---
title: "Warum Tailscale ein Relay verwendet: direkte Verbindungen, DERP und Peer-Relays"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Erfahre, warum Tailscale ein Relay verwendet, wie du die Ausgaben von status und netcheck liest und wann eine DERP- oder Peer-Relay-Verbindung untersucht werden sollte."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "Tailscale-Relay", "DERP", "Tailscale Peer Relay", "Direktverbindung", "WireGuard", "NAT-Traversal", "schwieriges NAT", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "VPN-Leistung", "Fernzugriff", "Tailnet", "Homelab-Netzwerk", "Relay-Latenz", "Ende-zu-Ende-Verschlüsselung"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Zwei Laptops auf getrennten Inseln tauschen verschlüsselte Pakete über ein zentrales Relay aus, während ein direkter Pfad unterbrochen ist."
coverCaption: ""
---

**Tailscale verwendet ein Relay**, wenn Geräte keine direkte Verbindung hergestellt haben. Eine kurze DERP-Verbindung beim Start ist normal. Eine dauerhafte Nutzung eines Relays weist häufig auf NAT- oder Firewallbedingungen hin, die den Pfad zwischen den Geräten beeinflussen. Direkte, DERP- und Peer-Relay-Verbindungen behalten alle die Ende-zu-Ende-Verschlüsselung von WireGuard bei. [Tailscale-Verbindungstypen](https://tailscale.com/docs/reference/connection-types).

## Wichtigste Erkenntnisse

- **Erkenne den Pfad:** Unterscheide zwischen direkten Verbindungen, DERP und Peer-Relays.
- **Sammle Belege:** Führe peer-spezifische Tests und Netzwerkprüfungen auf beiden Seiten aus.
- **Analysiere das Muster:** Vergleiche Gerätepaare und Netzwerkbedingungen.
- **Wähle eine Änderung:** Begründe sie mit einer gemessenen Arbeitslast und einem erneuten Test.

## Bevor du beginnst

**Voraussetzungen:** zwei registrierte Geräte, die online sind, sowie ein Terminal mit der Tailscale-Befehlszeilenschnittstelle, der **CLI**. Administratorzugriff ist nur erforderlich, wenn die Untersuchung zu Konfigurationsänderungen führt.

**Geschätzter Aufwand:** fünf Minuten für grundlegende Prüfungen, danach 15–20 Minuten für die Vergleichsübung. **Schwierigkeitsgrad:** Anfänger bei der Beobachtung, mittleres Niveau bei Netzwerkänderungen. Definiere zuerst das Problem, etwa eine langsame Sicherung oder eine verzögerte Terminalreaktion.

## Direkte Verbindungen, DERP und Peer-Relay

Ein **Tailnet** ist dein Tailscale-Netzwerk. Seine Geräte versuchen, eine direkte UDP-Verbindung herzustellen. Wenn der direkte Pfad fehlschlägt, stehen Relays zur Verfügung. Tailscale prüft seine Verbindungsoptionen regelmäßig erneut. [Verbindungsaufbau](https://tailscale.com/docs/reference/connection-types).

| Pfad | Verkehrsweg | Typische Bedeutung |
|---|---|---|
| **Direkt** | Zwischen den beiden Geräten | Normalerweise der bevorzugte Pfad für gute Leistung |
| **DERP-Relay** | Über die Relay-Infrastruktur von Tailscale | Fügt einen Vermittler hinzu, wenn direkter Zugriff fehlschlägt |
| **Peer-Relay** | Über ein konfiguriertes Gerät in deinem Tailnet | Eine alternative Relay-Option unter deiner Verwaltung |

Die **DERP-Leistung** hängt teilweise vom zusätzlichen Weg und von der gemeinsam genutzten Dienstkapazität ab. Tailscale dokumentiert Durchsatzgrenzen, damit DERP-Ressourcen fair geteilt werden. Es gibt keine universelle Relay-Geschwindigkeit, mit der sich die Dauer eines Dateitransfers vorhersagen lässt. [Probleme mit der Tailscale-Leistung beheben](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Die Verbindungsanbahnung verstehen

**NAT-Traversal** bezeichnet den Vorgang, bei dem ein nutzbarer Pfad durch Geräte hergestellt wird, die Adressen übersetzen. Tailscale beginnt die Kommunikation über DERP und handelt gleichzeitig einen direkten Pfad aus. Wenn direkte Konnektivität fehlschlägt, bietet ein verfügbares, konfiguriertes Peer-Relay eine weitere Option. Tailscale prüft die Optionen im Zeitverlauf erneut. [Verbindungsaufbau](https://tailscale.com/docs/reference/connection-types).

**Schwieriges NAT** beschreibt ein Mapping-Verhalten, das Traversal erschwert. Die Bedingungen an beiden Enden sind wichtig. Zwei Geräte hinter verschiedenen Routern verhalten sich nicht zwangsläufig gleich, auch wenn beide Netzwerke private Adressen verwenden. [Gerätekonnektivität](https://tailscale.com/docs/reference/device-connectivity).

Bei **einem mobilen Laptop** kann sich der Pfad zu deinem Heimserver ändern, wenn du vom heimischen WLAN in ein Hotelnetz wechselst. Notiere das während der Beobachtung verwendete Netzwerk. Eine direkte Verbindung von gestern sagt nichts über den heutigen Pfad aus.

## Aktuelle Verbindung prüfen

Ersetze **`home-server`** durch den Tailscale-Namen oder die Adresse deines Peers:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** prüft die Konnektivität zum benannten Peer. **`tailscale status`** listet Peers und Verbindungsdetails auf. **`tailscale netcheck`** meldet Bedingungen auf dem Gerät, auf dem du den Befehl ausführst. Die [Tailscale-CLI-Referenz](https://tailscale.com/docs/reference/tailscale-cli) beschreibt diese Befehle.

| Ausgabeindikator | Bedeutung |
|---|---|
| **`direct`** | Der Datenverkehr zu diesem Peer verwendet einen direkten Pfad |
| **`relay`** | Der Datenverkehr zu diesem Peer läuft über DERP |
| **`peer-relay`** | Der Datenverkehr verwendet ein konfiguriertes Peer-Relay |
| **Ein anfänglicher DERP-Pong** | Prüfe weitere Ergebnisse, bevor du entscheidest, dass der Pfad weiterhin über ein Relay lief |

Diese Bezeichnungen stammen aus der [Dokumentation zu Verbindungstypen](https://tailscale.com/docs/reference/connection-types). **Erzeuge zuerst Datenverkehr** und prüfe danach den gewünschten Peer. Die Befehle oben sind Beispiele und keine aufgezeichneten Benchmark-Ergebnisse.

## Einen Pfadwechsel interpretieren

Diese **veranschaulichende Abfolge** lässt Adressen und Zeitangaben aus, damit der Verbindungswechsel im Mittelpunkt steht:

```text
Erste Antwort:      über DERP
Spätere Antwort:    über einen direkten Endpunkt
Status danach:      direkt
```

**Interpretation:** Während dieser Beobachtung war die Aushandlung erfolgreich. Die erste Antwort allein hätte zu einer falschen Diagnose geführt. Wenn spätere Antworten und der Status weiterhin ein Relay anzeigen, notiere für dieses Gerätepaar und diesen Testzeitraum eine dauerhafte Relay-Verbindung.

**Umfang des Tests:** Ein erfolgreicher Tailscale-Ping bestätigt die Peer-Konnektivität für diesen Test. Er beweist nicht, dass dein Dashboard, Dateidienst oder SSH-Daemon Anwendungsdatenverkehr annimmt. Teste die fehlerhafte Anwendung separat, bevor du das Problem als gelöst bezeichnest.

## Was netcheck aussagt

Führe **`tailscale netcheck` auf beiden Geräten aus**. Vergleiche diese Felder mit der [Referenz zur Gerätekonnektivität](https://tailscale.com/docs/reference/device-connectivity):

| Feld | Aussage |
|---|---|
| **`UDP`** | Ob der Test ausgehende UDP-Konnektivität beobachtet hat |
| **`MappingVariesByDestIP`** | Wechselnde externe Mappings können auf schwieriges NAT-Traversal hindeuten |
| **`IPv6`** | Ob dieses Gerät nutzbare IPv6-Konnektivität hat |
| **`PortMapping`** | Ob ein unterstützter Port-Mapping-Mechanismus verfügbar ist |

**Ein einzelnes Feld liefert kein endgültiges Urteil.** Ein verfügbarer Mapping-Mechanismus beweist nicht, dass ein bestimmter Peer-Pfad funktioniert. Ein Relay-Label zeigt auch nicht, welcher Router die Ursache ist. Vergleiche beide Endpunkte und die tatsächlichen Ping-Ergebnisse.

**Provider-NAT** ist relevant, wenn die vorgelagerte Adressübersetzung außerhalb deiner Kontrolle liegt, wie in unserer Erklärung zur [Portweiterleitung bei T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) beschrieben. Gehe nicht davon aus, dass jede Verbindung hinter Provider-NAT dasselbe Traversal-Verhalten zeigt.

## Drei Gerätepaare vergleichen

Verwende, sofern verfügbar, ein **drittes registriertes Gerät**, um mehr Belege zu sammeln. Das folgende Muster ist hypothetisch und kein Messergebnis:

| Gerätepaare | Beobachteter Pfad |
|---|---|
| **Laptop zu Heimserver** | DERP |
| **Laptop zu einem anderen Server** | Direkt |
| **Heimserver zu einem anderen Server** | DERP |

**Arbeitshypothese:** Untersuche zuerst das Netzwerk des Heimservers, da beide beobachteten Pfade mit diesem Gerät über ein Relay liefen. Das ist ein Hinweis, kein Beweis. Jedes Paar handelt seine Verbindung unabhängig aus, und der Vergleichsserver hat eigene Netzwerkbedingungen.

**Nächste Beobachtung:** Sammle netcheck-Ausgaben auf allen drei Geräten und wiederhole den Test vom Laptop zum Heimserver über ein anderes Netzwerk, das du kontrollierst. Wenn sich der Pfad ändert, notiere genau, welches Netzwerk gewechselt hat. Schreibe das Ergebnis nicht einer bestimmten Firewall-Einstellung zu, bevor du sie getestet hast.

**Übung:** Die Verbindung vom Laptop zum Heimserver ist direkt, aber ein Dateitransfer bleibt langsam. Eine Relay-Erklärung passt nicht mehr zu dieser Beobachtung. Prüfe die zugrunde liegende Upload-Verbindung, Serverlast, Speichersystem und das Verhalten der Anwendung, bevor du Relay-Einstellungen änderst.

## Eine gezielte Änderung wählen

Beginne mit einem **Vergleichstest** über ein anderes Netzwerk, das du kontrollierst. Wird derselbe Peer dort direkt erreichbar, hast du einen nützlichen Hinweis auf den ursprünglichen Netzwerkpfad. Prüfe UDP-Beschränkungen und NAT-Konfiguration, bevor du nicht damit zusammenhängende DNS- oder Anwendungseinstellungen änderst.

**Ändere eine Variable**, wiederhole die Prüfungen und miss dieselbe Arbeitslast. Notiere Übertragungsrichtung, Dateigröße, verstrichene Zeit und Verbindungstyp. So unterscheidest du einen verbesserten Pfad von einer unabhängigen Änderung der Server- oder Speicherauslastung.

**Firewalländerungen** sollten den plattformspezifischen Empfehlungen und den gesammelten Belegen folgen. Das Öffnen eines Anwendungsports zum öffentlichen Internet verbessert für sich genommen nicht den Transportpfad von Tailscale. Beschränke Änderungen auf den erforderlichen Datenverkehr und das Netzwerk, das du verwaltest. [Tailscale-Empfehlungen für Firewalls](https://tailscale.com/docs/integrations/firewalls).

| Befund | Zu prüfende Änderung |
|---|---|
| **UDP-Test schlägt fehl** | Prüfe ausgehende UDP-Beschränkungen in diesem Netzwerk |
| **Mapping variiert je nach Ziel** | Prüfe das NAT-Verhalten auf Geräten, die du verwaltest |
| **Direkter Pfad, langsame Anwendung** | Untersuche den Host, die zugrunde liegende Verbindung und die Arbeitslast |
| **Relay funktioniert, Nutzung ist akzeptabel** | Behalte die Einrichtung bei und dokumentiere den Ausgangswert |

*Bevorzuge eine gemessene Verbesserung, statt Einstellungen nur zum Entfernen des Relay-Labels zu ändern.*

## Ein Peer-Relay bewerten

Ein **Peer-Relay** benötigt einen geeigneten Host, einen erreichbaren UDP-Port und eine Zugriffsrichtlinie, die seine Nutzung erlaubt. Sowohl das Relay als auch die teilnehmenden Clients benötigen Tailscale 1.86 oder höher. Prüfe unterstützte Hostplattformen, bevor du ein Gerät dafür einsetzt. [Anforderungen an Peer-Relays](https://tailscale.com/docs/features/peer-relay).

**Der Standort bestimmt den Nutzen.** Ein Gerät hinter derselben nicht erreichbaren Netzwerkgrenze hilft anderen Peers erst, wenn der Relay-Port erreichbar ist.

**Wartungsaufwand:** Jemand muss das Relay online, aktuell und ausreichend leistungsfähig halten. Bei gelegentlicher Administration und akzeptabler Latenz solltest du diesen Aufwand mit dem gemessenen Nutzen vergleichen. Bei wiederholten großen Transfers misst du die Arbeitslast über das vorgesehene Relay, bevor du es einführst.

## Gemeinsame Verkehrsauswirkungen prüfen

**Gebündelter Datenverkehr** verdient Aufmerksamkeit, wenn ein Subnetzrouter oder Exit-Node mehrere Arbeitslasten über DERP leitet. Tailscale dokumentiert Fälle, in denen hoher Relay-Datenverkehr latenzempfindlichen Datenverkehr auf derselben Verbindung verzögert. [Probleme mit schwierigem NAT beheben](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Vergleichsübung:** Beobachte deine interaktive Sitzung vor, während und nach einer großen Sicherung. Lass das Endgeräte-Paar unverändert und notiere jedes Mal den Pfad. Verzögerungen während des Transfers rechtfertigen eine Untersuchung der gemeinsamen Auslastung, belegen aber nicht deren genaue Ursache.

**Wähle den nächsten Test** anhand der Beobachtung. Prüfe Link-Auslastung und Hostlast. Bewerte anschließend einen direkten Pfad oder eine Trennung latenzempfindlicher Dienste, sofern die Topologie dies zulässt. Behandle ein DNS-Symptom nicht automatisch als Beweis für einen DNS-Konfigurationsfehler.

## Ist ein Relay ein Exit-Node?

Ein **Exit-Node** leitet den allgemeinen Internetverkehr eines Clients über ein ausgewähltes Gerät im Tailnet. Ein Relay transportiert Datenverkehr zwischen Tailscale-Peers. Die Auswahl eines Exit-Nodes garantiert keine direkte Verbindung zu diesem Gerät. [Dokumentation zu Exit-Nodes](https://tailscale.com/docs/features/exit-nodes).

## Einen Diagnosebericht erstellen

Bewahre für das tatsächliche Problem einen **kurzen Vorher-Nachher-Bericht** auf:

```text
Datum und Tailscale-Versionen:
Quell- und Zielgeräte:
Von jedem Gerät verwendete Netzwerke:
Anfängliche und stabile Verbindungspfade:
Netcheck-Beobachtungen auf beiden Seiten:
Arbeitslast, Richtung und Dauer:
Einzelne getestete Änderung:
Ergebnis des erneuten Tests:
Entscheidung, die Änderung zu behalten oder zurückzusetzen:
```

**Abschlusskriterium:** Der Bericht verknüpft ein konkretes Symptom mit Beobachtungen, einer Hypothese und einem gemessenen erneuten Test. „Das Relay ist verschwunden“ ist unvollständig, wenn die Anwendung weiterhin langsam ist. „Die Sicherung erfüllt über DERP die Zeitvorgabe“ ist ein gültiges Ergebnis, wenn die Vorgabe klar formuliert ist.

**Verwende `tailscale netcheck` als Beleg, nicht als Urteil.** Der Befehl beschreibt das Netzwerk aus Sicht eines einzelnen Geräts. Der stabile Pfad gehört zu einem Gerätepaar und einer Arbeitslast. Erfasse beide Endpunkte, die letzte Zeile von `tailscale status` und die Anwendungsmessung, bevor du Firewall- oder NAT-Einstellungen änderst.

## Nächste Schritte

Notiere den Pfad zu deinem wichtigen Peer und teste die Arbeitslast, bevor du Netzwerkeinstellungen änderst. Für die separate Frage, wer deine Koordinationsinfrastruktur betreibt, lies [Tailscale und Headscale im Vergleich](/articles/tailscale-vs-headscale-comparison-guide/).
