---
title: "Cloudflare Tunnel und Access: Brauchst du beides?"
date: 2026-09-11
lastmod: 2026-11-09
toc: true
draft: false
description: "Verstehe den Unterschied zwischen Cloudflare Tunnel und Access, wähle den Schutz für ein Heim-Dashboard und veröffentliche keine private Anwendung ohne Authentifizierung."
genre: ["Netzwerksicherheit", "Selbsthosting", "Cloud-Sicherheit"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel und Access", "Cloudflare Zero Trust", "cloudflared", "selbst gehostete Anwendungen", "Homelab-Sicherheit", "Fernzugriff", "Identitätsanbieter", "Zugriffsrichtlinien", "Anwendungsauthentifizierung", "öffentlicher Hostname", "Ursprungsschutz", "ausgehender Tunnel", "Servicetoken", "Service Auth", "MFA", "privates Dashboard", "Reverse-Proxy", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Ein Heimserver verbindet sich über einen transparenten Durchgang mit einem Cloud-Gateway und einer separaten Identitätsprüfung."
coverCaption: ""
---

**Cloudflare Tunnel** verbindet deine Anwendung mit Cloudflare. **Cloudflare Access** steuert, wer sie erreichen darf. Für ein privates Heim-Dashboard, das über einen öffentlichen Hostnamen erreichbar ist, solltest du beides verwenden. Ein funktionierender Tunnel fügt allein keine Identitätsprüfung hinzu. Cloudflares [Anleitung zum Veröffentlichen von Anwendungen](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) erklärt diesen Unterschied.

## Wichtigste Erkenntnisse

- **Erkläre den Pfad:** Unterscheide Connector, Ursprung und Identitätsprüfung.
- **Richte eine Richtlinie ein:** Erlaube bestimmten Personen den Zugriff auf ein privates Dashboard.
- **Prüfe den Schutz:** Teste erlaubte, abgelehnte und alternative Zugriffswege.
- **Plane den Zugriff:** Dokumentiere getrennte Anforderungen für Besucher und Automatisierung.

## Vor dem Start

**Zielgruppe:** Betreiber eines Heimservers, die ein Browser-Dashboard schützen möchten. Das Beispiel setzt eine aktive Domain bei Cloudflare, eine funktionierende lokale Webanwendung und die Berechtigung zur Administration beider Systeme voraus. **Geschätzter Aufwand:** 20–30 Minuten für die Richtlinienübung nach der Einrichtung des Connectors. **Schwierigkeit:** Anfänger bis Mittelstufe.

**Leseweg:** Beginne mit den Produktrollen, verfolge eine Anfrage und richte dann eine kleine Richtlinie ein, die du überprüfst. Schreibe zum Abschluss eine Zugriffsspezifikation für deinen Dienst.

## Was die Produkte leisten

Der **Ursprung** ist der Server, auf dem deine Anwendung läuft. Der Connector **`cloudflared`** baut Verbindungen von deiner Infrastruktur zu Cloudflare auf. Deshalb benötigt der Ursprung keine öffentlich routbare IP-Adresse. Anfragen und Antworten laufen anschließend über die bestehende Verbindung. [Übersicht zu Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Frage | Tunnel | Access |
|---|---|---|
| **Wie erreicht Cloudflare meinen Server?** | Stellt die Verbindung her | Ersetzt nicht die Verbindung zum Ursprung |
| **Wer erhält Zugriff?** | Bietet allein keine Benutzeranmeldung | Prüft konfigurierte Zugriffsrichtlinien |
| **Was richte ich ein?** | Connector und Anwendungsroute | Anwendung, Identitätsanbieter und Richtlinien |
| **Was belegt der Erfolg?** | Der Ursprung ist über die Route erreichbar | Eine Anfrage hat die Richtlinie erfüllt |

Ein **Identitätsanbieter (IdP)** authentifiziert den Besucher. Eine **Access-Richtlinie** legt eine Aktion und passende Bedingungen fest. Allow lässt passende Benutzer zu. Bypass setzt die Access-Durchsetzung für passenden Datenverkehr aus. [Referenz zu Access-Richtlinien](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Verfolge eine Browseranfrage

Für **`dashboard.example.com`** sieht der logische Anfragepfad so aus:

```text
Browser -> Cloudflare Access -> tunnel connection -> cloudflared -> dashboard
               |
               +-> identity provider when authentication is needed
```

Der **Connector baut die Tunnelverbindung von deinem Netzwerk nach außen auf**. Browseranfragen laufen anschließend über diese bestehende Verbindung zum Ursprung. Eine ausgehende Verbindung, über die eingehende Anwendungsanfragen übertragen werden, ist der Hauptgrund, warum Tunnel ohne herkömmliche Portweiterleitung zum Ursprung funktioniert. [Verbindungsmodell von Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Berechtigungen innerhalb der Anwendung** sind eine weitere Entscheidung. Der Zugriff auf ein Dashboard legt nicht automatisch fest, wer Einstellungen ändern oder Daten löschen darf. Wenn die Anwendung Rollen für Betrachter und Administratoren bietet, richte sie getrennt ein und teste sie.

Zum Beispiel benötigt **ein Familienmitglied mit Leserechten** Zugriff auf den Sicherungsstatus, während du die Sicherungsziele ändern können musst. Halte diese Anforderungen fest, bevor du Identitäten auswählst. Zwei Personen, die dieselbe Access-Prüfung bestehen, sollten nicht automatisch dieselben Anwendungsrechte erhalten.

## Wann du beides brauchst

**Das Publikum bestimmt den Schutz.** Vergleiche diese Konfigurationen, bevor du eine Route veröffentlichst:

| Vorgesehenes Publikum | Empfohlene Konfiguration | Vor der Nutzung prüfen |
|---|---|---|
| **Alle Besucher einer öffentlichen Website** | Tunnel, falls er für die Verbindung zum Ursprung nötig ist | Die öffentliche Erreichbarkeit ist beabsichtigt |
| **Du und einige Familienmitglieder** | Tunnel plus Access | Nur die vorgesehenen Identitäten zulassen |
| **Ein bereits öffentlicher Ursprung** | Access mit getrenntem Ursprungsschutz | Direkter Ursprungszugriff darf die Prüfung nicht umgehen |
| **Ein geplanter Skriptlauf** | Tunnel plus eine Service-Auth-Richtlinie | Der Client unterstützt die Authentifizierungsmethode |

**Access ohne Tunnel** wird für einen bereits erreichbaren Ursprung unterstützt. Schütze auch alternative Wege zum Server. Cloudflare empfiehlt, zuerst die Access-Anwendung zu erstellen, wenn du eine neue Tunnelroute veröffentlichst. [Anforderungen für selbst gehostete Anwendungen](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Für ein privates Heim-Dashboard, das über einen öffentlichen Hostnamen erreichbar ist, solltest du mit Tunnel und Access beginnen.*

## Richte eine Dashboard-Richtlinie ein

Verwende diese **Beispielkonfiguration** für zwei vorgesehene Besucher. Ersetze beide Beispieladressen durch Identitäten, die du kontrollierst. Erstelle die Access-Anwendung, bevor du die öffentliche Tunnelroute hinzufügst.

1. **Anwendung:** Öffne Zero Trust → Access controls → Applications und erstelle eine selbst gehostete Anwendung mit öffentlichem Hostnamen.
2. **Hostname:** Gib den dedizierten Dashboard-Hostnamen ein. Lasse den Pfad für dieses Beispiel mit dem gesamten Hostnamen uneingeschränkt.
3. **Richtlinie:** Erstelle eine Allow-Richtlinie namens `Dashboard viewers`.
4. **Identitätsauswahl:** Füge eine Include-Regel mit Emails hinzu. Ersetze `alice@example.com` und `bob@example.com` durch die beiden vorgesehenen Adressen.
5. **Anmeldung:** Wähle den von den Besuchern verwendeten Identitätsanbieter und lege bewusst eine Sitzungsdauer fest.
6. **Route:** Speichere die Anwendung und verbinde den Hostnamen anschließend über deinen Tunnel mit dem Dashboard.

Der [offizielle Anwendungsablauf](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) beschreibt diese Einstellungen. **Erwartetes Ergebnis:** Ein neuer Besucher muss sich authentifizieren, bevor er die Anwendung erreicht. Führe den Test mit einer abgelehnten Identität unten aus, bevor du dich auf die Richtlinie verlässt.

## Verstehe die Richtlinienlogik

**Include** verbindet Alternativen mit OR. **Require** fügt notwendige Bedingungen mit AND hinzu. **Exclude** entfernt passende Benutzer. Eine weitere Include-Bedingung vergrößert die zugelassene Gruppe. [Semantik von Access-Regeln](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Richtlinienfragment | Logische Wirkung |
|---|---|
| **Include Alice or Bob** | Eine der genannten Identitäten genügt |
| **Include Alice, Include a country** | Auch Personen aus dem passenden Land erhalten Zugriff |
| **Include Alice, Require a country** | Alice muss zusätzlich die Länderbedingung erfüllen |

**Übung zur Richtlinienprüfung:** Deine Anforderung nennt nur Alice und Bob, doch ein Kollege fügt ein Land als weitere Include-Bedingung hinzu. Lehne die Änderung ab, weil dadurch eine zusätzliche Personengruppe zugelassen wird. Der geografische Standort belegt nicht, dass jemand zu deinem Haushalt gehört.

## Authentifiziere geplante Skripte

Ein **Servicetoken** enthält eine Client ID und ein Client Secret für automatisierte Anfragen. Konfiguriere die Anwendungsrichtlinie so, dass sie das Token über **Service Auth** akzeptiert. Ein Token ohne die passende Richtlinie gewährt keinen Anwendungszugriff. [Cloudflare-Servicetoken](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Bewahre das **Secret** für ein Sicherungsskript oder eine Überwachungsprüfung im geschützten Zugangsdatenspeicher des Tools auf. Verwende für jede Integration einen eigenen Tokennamen und ein bewusst gewähltes Ablaufdatum. Erneuere oder widerrufe das Token, wenn du die Integration stilllegst. Die Dokumentation zu Servicetoken beschreibt diese Schritte im Lebenszyklus.

**Prüfe die Client-Kompatibilität ausdrücklich.** Ein Tool, das eine API-Antwort erwartet, kann nicht unbedingt mit einer interaktiven Browseranmeldung umgehen. Prüfe vor der Richtlinienauswahl, ob es Anfrageheader oder eine andere unterstützte Authentifizierungsmethode verwendet.

## Prüfe Zugriffsentscheidungen

Verwende diese **Abnahmekriterien** für deine Bereitstellung:

| Prüfung | Zu dokumentierender Nachweis |
|---|---|
| **Abgemeldeter Besucher** | Access fängt eine Anfrage aus einer neuen Browsersitzung ab |
| **Erlaubte Identität** | Die vorgesehene Anwendung lädt nach der Anmeldung |
| **Abgelehnte Identität** | Ein nicht aufgeführtes Konto erhält keinen Anwendungszugriff |
| **Alternativer Weg** | Alte DNS-Namen und Ursprungsports bieten keinen unbeabsichtigten Zugriff |
| **Automatisierung** | Der freigegebene Client funktioniert, eine Anfrage ohne Zugangsdaten schlägt fehl |

**Ein sichtbarer Anmeldebildschirm** belegt nur, dass ein Zugriffsweg auf Authentifizierung getroffen ist. Teste auch den Ablehnungsfall und alternative Routen. Das sind empfohlene Prüfungen, keine Ergebnisse aus einer bereitgestellten Beispielumgebung.

## Prüfe die Grenze zum Ursprung

Ein **Ursprung, der Access-Identität vertraut**, sollte das signierte Anwendungstoken prüfen. Cloudflare leitet es im Header **`Cf-Access-Jwt-Assertion`** weiter. Das Vorhandensein eines Headers allein beweist seine Echtheit nicht. [Cloudflare-JWT-Validierung](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Ein **JSON Web Token (JWT)** enthält signierte Angaben. Verwende beim Einbinden der Access-Identität in einen Ursprung das dokumentierte Prüfverfahren einschließlich des erwarteten Ausstellers und der Zielgruppe der Anwendung. Ein Token zu decodieren und ein E-Mail-Feld auszulesen, ist keine ausreichende Prüfung.

**Issuer** bezeichnet die Stelle, die das Token ausstellt. **Audience** bezeichnet die vorgesehene Anwendung. Prüfe Gültigkeit und Ablaufzeit des Tokens mit einer unterstützten Prüfungsbibliothek, statt Signaturprüfungen selbst zu implementieren.

**Lege die Grenze ausdrücklich fest:** Bestimme, wo die Prüfung stattfindet und über welche Routen die Anwendung erreichbar ist. Eine alte Portweiterleitung oder ein alternativer Hostname verdient eine eigene Prüfung, auch nachdem der Haupthostname alle Browserprüfungen bestanden hat.

## Behebe Abweichungen in Richtlinien

| Beobachtung | Nächste Prüfung |
|---|---|
| **Ein unerwarteter Besucher kommt durch** | Include-Bedingungen, Bypass-Richtlinien und Hostname-Abdeckung prüfen |
| **Ein vorgesehener Besucher wird abgelehnt** | Angemeldete Identität mit den genauen Auswahlwerten vergleichen |
| **Ein Skript erhält eine Anmeldeseite** | Zugangsdaten und Service-Auth-Richtlinie prüfen |
| **Ein zugelassener Betrachter ändert Einstellungen** | Rollenvergabe in der Anwendung prüfen |

**Das Sitzungsverhalten** beeinflusst auch Wiederholungstests. Access bietet mehrere Sitzungsdauern, darunter Anwendungs- und globale Sitzungen. Notiere die Einstellung und verwende beim Test einer neuen Identität eine neue Sitzung. [Access-Sitzungsverwaltung](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Schreibe deine Zugriffsspezifikation

Erstelle eine **kurze Spezifikation**, bevor du einen weiteren Dienst hinzufügst:

```text
Dienst und Hostname:
Erlaubte menschliche Identitäten:
Erforderliche Anwendungsrollen:
Automatisierungszugangsdaten und Ablaufdatum:
Weitere Wege zum Ursprung:
Ort der Access-Token-Prüfung:
Testergebnis für erlaubte Identität:
Testergebnis für abgelehnte Identität:
```

**Abschlusskriterium:** Ein anderer Administrator sollte verstehen, wer Zugriff erhält, wie sich jeder Client authentifiziert und welcher Nachweis eine Ablehnung belegt. Wenn du später eine Überwachungsintegration hinzufügst, aktualisiere den Zugangsdateneintrag und wiederhole die Prüfung mit einer nicht authentifizierten Anfrage.

## Nächste Schritte

Folge der [Einrichtungsanleitung für Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) für den Connector und wende anschließend den [offiziellen Access-Anwendungsablauf](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) an. Lies bei einer Mobilfunkverbindung die [Grenzen der Portweiterleitung bei T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/), bevor du einen Fernzugriffspfad auswählst.
