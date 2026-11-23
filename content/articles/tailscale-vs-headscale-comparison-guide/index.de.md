---
title: "Tailscale im Vergleich mit Headscale"
date: 2026-05-24
lastmod: 2026-11-23
toc: true
draft: false
description: "Vergleichen Sie Tailscale und Headscale nach Hosting-Modell, Identitätsverwaltung, Funktionen, Kosten, Betrieb und Support, um ein passendes WireGuard-Mesh-VPN zu wählen."
genre: ["VPN", "Netzwerksicherheit", "Selbsthosting", "WireGuard", "Zero Trust", "Mesh-Netzwerke", "Quelloffene Software", "Cloud-Infrastruktur", "Fernzugriff", "Netzwerkverwaltung"]
tags: ["tailscale im vergleich mit headscale", "headscale im vergleich mit tailscale", "selbst gehostetes vpn", "VPN auf WireGuard-Basis", "Vermaschtes VPN", "zero-trust-netzwerke", "Alternative zu Tailscale", "headscale-einrichtung", "vpn-vergleich", "VPN mit quelloffener Software", "tailscale-preise", "headscale-funktionen", "WireGuard-Mesh-Netz", "privates netzwerk", "vpn-leistung", "tailscale-funktionen", "Headscale-Installation", "mesh-netzwerke", "sicherer fernzugriff", "vpn-sicherheit", "netzwerkkoordination", "tailnet", "vpn-bereitstellung", "unternehmens-vpn", "VPN fürs Homelab", "selbst gehostete netzwerke", "tailscale-kosten", "headscale mit docker", "vpn-verwaltung", "wireguard-koordinierungsserver"]
cover: "/img/cover/tailscale-vs-headscale-comparison-guide.webp"
coverAlt: "Illustration eines Mesh-Netzwerks, in dem leuchtende Linien die Geräte vor einem dunklen Hintergrund verbinden. Stilisierte Gerätesymbole in kräftigen Farben stehen für sichere Verbindungen."
coverCaption: ""
---

## Einführung

**Tailscale** und **Headscale** sind Koordinierungsserver für sichere Mesh-VPNs auf Basis von [WireGuard](https://www.wireguard.com/). Tailscale ist ein kommerzieller Cloud-Dienst mit einem großzügigen kostenlosen Tarif. Headscale ist eine selbst gehostete Open-Source-Alternative, die das Steuerungsprotokoll von Tailscale implementiert. Die Unterschiede sind entscheidend für die Wahl einer Lösung, die zu den Netzwerkanforderungen Ihrer Organisation passt.

Die zentrale Frage ist, **wer die Steuerungsebene betreibt**. Wählen Sie Tailscale, wenn verwaltete Identitäten, Administration und Support im Vordergrund stehen. Prüfen Sie Headscale, wenn Selbsthosting und die Kontrolle über Koordinierungsdaten den zusätzlichen Betriebsaufwand rechtfertigen. Die folgenden Abschnitte vergleichen Funktionen, Leistung, Kosten, Sicherheit und Wartung.

______

## Grundlagen von Mesh-VPNs und WireGuard

Für den Vergleich lohnt sich ein Blick auf die zugrunde liegende Technik:

### Was ist WireGuard?

**WireGuard** ist ein modernes, leistungsfähiges VPN-Protokoll mit folgenden Eigenschaften:
- **Hohe Leistung:** Bis zu 10-mal schneller als OpenVPN
- **Kleine Angriffsfläche:** Nur etwa 4.000 Codezeilen gegenüber mehr als 100.000 bei OpenVPN
- **Moderne Kryptografie:** Curve25519, ChaCha20, Poly1305
- **Im Linux-Kernel integriert:** Seit Linux 5.6 (2020)

### Was ist ein Mesh-VPN?

Ein **Mesh-VPN** stellt Peer-to-Peer-Verbindungen zwischen Geräten her. Der Datenverkehr muss deshalb nicht vollständig über einen zentralen Server laufen:
- **Direkte Verbindungen:** Geräte verbinden sich nach Möglichkeit direkt miteinander
- **NAT-Traversal:** Überwindet Firewalls und NAT automatisch
- **Geringere Latenz:** Keine unnötigen Zwischenstationen über zentrale Server
- **Höhere Leistung:** Nutzt die volle Bandbreite zwischen Peers

### Die Rolle von Koordinierungsservern

WireGuard definiert das Protokoll. Für ein Mesh-VPN brauchen Sie zusätzlich einen **Koordinierungsserver** (die Steuerungsebene), der:
- Die Authentifizierung und Autorisierung von Geräten verwaltet
- Verschlüsselungsschlüssel verteilt
- NAT-Traversal und das Auffinden von Peers ermöglicht
- Richtlinien zur Zugriffskontrolle verwaltet
- DNS-Namensauflösung innerhalb des Netzwerks bereitstellt

**Tailscale** und **Headscale** übernehmen als Koordinierungsserver diese Aufgaben.

______

## Tailscale und Headscale im Überblick

| Aspekt | Tailscale | Headscale |
|--------|-----------|-----------|
| **Typ** | Kommerzieller SaaS-Dienst | Open Source, selbst gehostet |
| **Lizenzierung** | Proprietär (kostenloser Tarif verfügbar) | BSD-3-Clause-Lizenz |
| **Hosting** | In der Cloud (Tailscale übernimmt den Betrieb) | Selbst gehostet (Sie übernehmen den Betrieb) |
| **Erstveröffentlichung** | 2019 | 2020 |
| **Hauptverantwortlich für die Pflege** | Tailscale Inc. | Juan Font und die Community |
| **GitHub-Sterne** | Entfällt (proprietärer Quellcode) | Über 38.900 (Stand 2026) |
| **Einrichtungsaufwand** | Sehr gering (5 Minuten) | Mittel (30–60 Minuten) |
| **Monatliche Kosten (100 Nutzer)** | 0 $ (kostenlos) bis 18 $ pro Nutzer (Enterprise) | Nur Serverhosting (5–50 $ pro Monat) |
| **Protokollkompatibilität** | Tailscale-Protokoll | Tailscale-Protokoll (kompatibel) |

______

## Detaillierter Funktionsvergleich

### Netzwerkgrundfunktionen

| Funktion | Tailscale | Headscale | Hinweise |
|---------|-----------|-----------|-------|
| **WireGuard-basiertes Mesh** | ✅ Ja | ✅ Ja | Beide nutzen WireGuard für alle Verbindungen zwischen Peers |
| **Automatisches NAT-Traversal** | ✅ Ja | ✅ Ja | STUN/DERP für zuverlässige Verbindungen |
| **Subnetz-Routing** | ✅ Ja | ✅ Ja | Zugriff auf Netzwerke hinter einem Gateway |
| **Exit-Nodes** | ✅ Ja | ✅ Ja | Gesamten Internetverkehr über einen Knoten leiten |
| **MagicDNS** | ✅ Ja | ✅ Ja | Namensauflösung innerhalb des Mesh-Netzwerks |
| **Getrennte DNS-Auflösung** | ✅ Ja | ✅ Ja | Abweichende DNS-Einstellungen für bestimmte Domains |
| **Hochverfügbares Routing** | ✅ Ja | ✅ Ja | Automatisches Umschalten zwischen Routen bei Ausfällen |
| **IPv6-Unterstützung** | ✅ Vollständig | ✅ Vollständig | Vollständige IPv6-Adressierung im Mesh |
| **Multicast-Unterstützung** | ❌ Nein | ❌ Nein | Derzeit unterstützt keine der beiden Lösungen Multicast |

### Zugriffskontrolle und Sicherheit

| Funktion | Tailscale | Headscale | Hinweise |
|---------|-----------|-----------|-------|
| **ACL-Engine** | ✅ Erweitert | ✅ Kompatibel | Headscale implementiert die ACL-Syntax von Tailscale |
| **Tagbasierte Zugriffskontrolle** | ✅ Ja | ✅ Ja | Geräte mithilfe von Tags gruppieren |
| **Nutzer- und Gruppenverwaltung** | ✅ Ja | ✅ Ja | Headscale verwendet das Konzept der „Nutzer“ |
| **OpenID Connect (OIDC)** | ✅ Ja | ✅ Ja | Authentifizierung über Google, Okta, Keycloak usw. |
| **SAML-Authentifizierung** | ✅ Ja (Enterprise) | ❌ Nein | Nur bei Tailscale |
| **Tailnet Lock** | ✅ Ja | ❌ Nein | Verhindert den Einsatz nicht autorisierter Koordinierungsserver |
| **Gerätestatusprüfungen** | ✅ Ja (Beta) | ❌ Nein | Vor dem Zugriff prüfen, ob das Gerät die Vorgaben erfüllt |
| **Just-in-Time-Zugriff** | ✅ Ja | ❌ Nein | Vorübergehend erweiterte Berechtigungen |
| **Audit-Protokollierung** | ✅ Umfangreich | ⚠️ Grundlegend | Tailscale stellt detaillierte Protokolle bereit |

### Verwaltung und Administration

| Funktion | Tailscale | Headscale | Einschränkungen |
|---------|-----------|-----------|-------------|
| **Weboberfläche** | ✅ Offiziell | ⚠️ Community | Für Headscale gibt es mehrere Oberflächen aus der Community |
| **Verwaltung per CLI** | ✅ Ja | ✅ Ja | Beide bieten umfangreiche Kommandozeilenwerkzeuge |
| **REST-API** | ✅ Ja | ✅ Ja | Verwaltungsaufgaben automatisieren |
| **gRPC-API** | ❌ Nein | ✅ Ja | Headscale bietet gRPC für die Fernverwaltung |
| **Terraform-Provider** | ✅ Offiziell | ❌ Nein | Integration für Infrastructure as Code |
| **Kubernetes-Operator** | ✅ Offiziell | ⚠️ Community | Operator für Headscale aus der Community |
| **Mobile Apps** | ✅ iOS, Android | ✅ Kompatibel | Tailscale-Apps mit einem Headscale-Server verwenden |
| **Administrationskonsole** | ✅ Umfangreich | ❌ Nein | Headscale setzt auf CLI und API |
| **Zugriff für mehrere Administratoren** | ✅ Ja | ⚠️ Manuell | Headscale erfordert eine eigene Implementierung |

### Erweiterte Funktionen

| Funktion | Tailscale | Headscale | Hinweise |
|---------|-----------|-----------|-------|
| **Tailscale SSH** | ✅ Ja | ⚠️ Nur als Server | Headscale-Knoten unterstützen bei Tailscale SSH ausschließlich die Serverrolle |
| **Taildrop (Dateifreigabe)** | ✅ Ja | ⚠️ Unvollständig | Headscale unterstützt Taildrop nur eingeschränkt |
| **Funnel (öffentlicher Zugriff)** | ✅ Ja | ❌ Nein | Dienste über das öffentliche Internet zugänglich machen |
| **Serve (private Freigabe)** | ✅ Ja | ❌ Nein | Dienste innerhalb des Tailnets freigeben |
| **Diensterfassung** | ✅ Ja | ❌ Eingeschränkt | Dienste im Netzwerk finden |
| **Tailscale DERP** | ✅ Globales Netzwerk | ⚠️ Integriert | Headscale bietet integriertes DERP und erlaubt eigene Relays |
| **Eigene DERP-Server** | ✅ Ja | ✅ Ja | Beide unterstützen eigene Relay-Server |
| **Docker-Erweiterung** | ✅ Ja | ❌ Nein | Tailscale-Docker-Erweiterung für Container-Netzwerke |

______

## Preisvergleich (2026)

### Tailscale-Preise

| Tarif | Monatliche Kosten | Jährliche Kosten | Geräte | Funktionen |
|------|-------------|-------------|---------|----------|
| **Personal** | 0 $ | 0 $ | Bis zu 100 | 1 Nutzer, Grundfunktionen, Community-Support |
| **Personal Pro** | 6 $ pro Nutzer und Monat | 48 $ pro Nutzer und Jahr | Unbegrenzt | Mehrere Nutzer, Subnetz-Routing, ACLs |
| **Team** | 10 $ pro Nutzer und Monat | 100 $ pro Nutzer und Jahr | Unbegrenzt | Administrationskonsole, Audit-Protokolle, SSO |
| **Business** | 15 $ pro Nutzer und Monat | 150 $ pro Nutzer und Jahr | Unbegrenzt | Erweiterte ACLs, Nutzergruppen, priorisierter Support |
| **Enterprise** | Ab 18 $ pro Nutzer und Monat | Individuell | Unbegrenzt | Tailnet Lock, SAML, dedizierter Support, SLA |

**Hinweis:** Der kostenlose Tailscale-Tarif Personal unterstützt bis zu 100 Geräte für den privaten Gebrauch und bietet damit viel Spielraum für Homelabs und kleine Installationen.

### Kosten für Headscale

Headscale ist **kostenlos und quelloffen**. Kosten fallen für die Infrastruktur an:

| Ressource | Monatliche Kostenspanne | Hinweise |
|----------|-------------------|-------|
| **Kleiner VPS** (1 CPU, 1 GB RAM) | 5–10 $ | Geeignet für <50 Geräte |
| **Mittlerer VPS** (2 CPUs, 4 GB RAM) | 15–25 $ | Geeignet für 50–200 Geräte |
| **Großer VPS** (4 CPUs, 8 GB RAM) | 40–80 $ | Geeignet für 200 bis über 1.000 Geräte |
| **Domainname** | 10–15 $ pro Jahr | Für TLS-Zertifikate |
| **Bandbreite** | Meist inbegriffen | Limits des VPS-Anbieters prüfen |
| **Zeitaufwand** | Variabel | Einrichtung, Wartung, Updates |

**Gesamtbetriebskosten (100 Nutzer):**
- **Tailscale:** 0 $ (kostenloser Tarif) oder 1.000–1.800 $ pro Monat (kostenpflichtige Tarife)
- **Headscale:** 15–30 $ pro Monat + 5–10 Stunden Einrichtung + 2–5 Stunden Wartung pro Monat

**Rentabilitätsschwelle:** Für Organisationen mit mehr als 3–5 zahlenden Nutzern rechnet sich Headscale, wenn sie den Zeitaufwand mit weniger als 50 $ pro Stunde ansetzen.

______

## Leistungsvergleich

### Latenz und Durchsatz

Tailscale und Headscale verwenden für die Datenebene WireGuard. Daher ist die **Peer-to-Peer-Leistung identisch**:

| Messgröße | Tailscale | Headscale |
|--------|-----------|-----------|
| **Zusätzliche P2P-Latenz** | <1 ms | <1 ms |
| **P2P-Durchsatz** | Nahe am Durchsatz ohne VPN (ca. 900 Mbit/s bei 1 Gbit/s) | Nahe am Durchsatz ohne VPN |
| **Durchsatz über Relay (DERP)** | 50–300 Mbit/s | 10–200 Mbit/s (abhängig von Ihrem Server) |
| **Latenz über Relay** | +10–50 ms | +5–100 ms (abhängig vom Standort) |
| **Verbindungsaufbau** | 100–500 ms | 200–800 ms |
| **Verteilung von ACL-Änderungen** | <5 Sekunden | <30 Sekunden |

**Wesentlicher Unterschied:** Tailscale betreibt ein weltweites DERP-Netzwerk (Relay-Netzwerk) mit Servern rund um den Globus. Das verbessert die Leistung beim Ausweichen auf ein Relay, wenn direkte Verbindungen scheitern. Das integrierte DERP von Headscale läuft auf Ihrem Server. Ohne geografisch verteilte Relays ist eine höhere Latenz möglich.

### Skalierbarkeit

| Aspekt | Tailscale | Headscale |
|--------|-----------|-----------|
| **Maximale Knotenzahl** | Über 100.000 (getestet) | Ca. 5.000 (laut Community-Berichten) |
| **Empfohlene Knotenzahl** | Unbegrenzt | <1.000 pro Einzelserver |
| **Anfragen pro Minute auf der Steuerungsebene (RPM)** | Stark optimiert | Abhängig von der Serverausstattung |
| **Speicherbedarf pro Knoten** | Entfällt (verwalteter Dienst) | Ca. 1–5 MB (serverseitig) |
| **Datenbank** | PostgreSQL (verwaltet) | SQLite oder PostgreSQL |

______

## Sicherheitsvergleich

### Sicherheit der Infrastruktur

| Aspekt | Tailscale | Headscale | Bewertung |
|--------|-----------|-----------|------------|
| **Vertrauen in den Koordinierungsserver** | Tailscale Inc. muss vertraut werden | Sie kontrollieren den Server | Headscale bietet mehr Datenschutz |
| **Verschlüsselungsschlüssel** | Entstehen auf den Geräten und gelangen nie zu Tailscale | Entstehen auf den Geräten und gelangen nie zum Server | ✅ Beide ausgezeichnet |
| **Sicherheit der Datenebene** | WireGuard (ausgezeichnet) | WireGuard (ausgezeichnet) | ✅ Beide ausgezeichnet |
| **Sicherheit der Steuerungsebene** | HTTPS + Attestierung | HTTPS + optionale Entsprechung zu Tailnet Lock | ⚠️ Tailscale etwas stärker |
| **Audit-Spur** | Umfangreiche Protokollierung | Grundlegende Protokollierung | ⚠️ Tailscale überlegen |
| **Bug-Bounty-Programm** | ✅ Ja | ❌ Nein | Tailscale hat Sicherheitsforscher bezahlt |
| **Sicherheitszertifizierungen** | SOC 2 Typ II | Entfällt | Tailscale für den Unternehmenseinsatz geeignet |

### Datenschutz

| Datenschutzaspekt | Tailscale | Headscale |
|----------------|-----------|-----------|
| **Sichtbarkeit von Metadaten** | Tailscale hat Einblick in Gerätenamen, IP-Adressen und Verbindungsmetadaten | Sie kontrollieren sämtliche Metadaten |
| **Einblick in den Datenverkehr** | ❌ Kein Einblick in den Datenverkehr (verschlüsselt) | ❌ Kein Einblick in den Datenverkehr (verschlüsselt) |
| **Compliance-Anforderungen** | Unterliegt US-Recht | Unterliegt dem Recht am Standort Ihres Servers |
| **Datenspeicherort** | Cloud-Infrastruktur von Tailscale | Rechenzentrum Ihrer Wahl |

**Bewertung:** Beide Lösungen bieten für den eigentlichen Datenverkehr **ausgezeichnete Verschlüsselung und eine Zero-Knowledge-Architektur**. Headscale bietet mehr **Datenschutz**, da Sie sämtliche Metadaten kontrollieren. Tailscale bietet stärkere **Sicherheitsnachweise** durch Zertifizierungen, Audits und Bug-Bounty-Programme.

______

## Vergleich von Einrichtung und Bereitstellung

### Tailscale einrichten

**Zeitbedarf:** 5–10 Minuten

1. **Konto erstellen** auf [tailscale.com](https://tailscale.com/)
2. **Client installieren** auf jedem Gerät (ein Befehl oder App-Download)
3. **Authentifizieren** über OAuth (Google, Microsoft, GitHub usw.)
4. **ACLs konfigurieren** (optional, auch später möglich)
5. **Fertig!** Das Netzwerk ist sofort einsatzbereit

**Beispielinstallation (Linux):**

> **Prüfen Sie das Installationsskript vor der Ausführung.** Laden Sie das Skript in eine temporäre Datei herunter, prüfen Sie den Inhalt und bestätigen Sie die Distribution des Hosts und die Paketquelle. Führen Sie nach der Installation `tailscale version` und `tailscale status` aus, um das Ergebnis zu prüfen. Falls die Installation fehlschlägt, entfernen Sie das Paket mit der Paketverwaltung Ihrer Distribution und stellen Sie den vorherigen Paketzustand aus Ihrer Systemsicherung wieder her.

```bash
curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
less /tmp/tailscale-install.sh
sh /tmp/tailscale-install.sh
sudo tailscale up
```

### Headscale einrichten

**Zeitbedarf:** 30–90 Minuten (bei der Ersteinrichtung)

1. **Server bereitstellen** (VPS mit öffentlicher IP-Adresse, mindestens 1 GB RAM empfohlen)
2. **DNS konfigurieren** (A-Eintrag, der auf den Server verweist)
3. **Headscale installieren** (über die Paketverwaltung oder Docker)
4. **Headscale konfigurieren** (config.yaml mit Server-URL, Datenbank usw.)
5. **TLS-Zertifikate einrichten** (Let's Encrypt empfohlen)
6. **Headscale-Dienst starten**
7. **Nutzer anlegen** per CLI: `headscale users create alice`
8. **Tailscale-Client installieren** auf jedem Gerät
9. **Clients konfigurieren**, damit sie den eigenen Koordinierungsserver verwenden
10. **Knoten registrieren** per Webauthentifizierung oder mit Vorab-Authentifizierungsschlüsseln
11. **ACLs konfigurieren** (Datei policy.json)

**Beispielinstallation für Headscale (Ubuntu):**
```bash
# Headscale installieren
curl -fsSL https://pkgs.headscale.net/headscale_<VERSION>_linux_amd64.deb -o headscale.deb
sudo apt install ./headscale.deb

# Headscale konfigurieren
sudo nano /etc/headscale/config.yaml
# server_url auf https://headscale.example.com setzen

# Dienst starten
sudo systemctl enable --now headscale

# Benutzer anlegen
headscale users create myuser

# Auf dem Clientgerät
sudo tailscale up --login-server=https://headscale.example.com
```

**Einfachere Einrichtung:** Die Ersteinrichtung von **Tailscale** ist deutlich einfacher.

______

## Betriebsaufwand

### Laufende Verwaltung

| Aufgabe | Tailscale | Headscale | Vorteil |
|------|-----------|-----------|--------|
| **Neues Gerät hinzufügen** | Link anklicken und authentifizieren | Authentifizierungsschlüssel erstellen oder Webauthentifizierung nutzen | Tailscale (einfacher) |
| **ACLs aktualisieren** | In der Weboberfläche bearbeiten, sofort wirksam | Datei bearbeiten und Konfiguration neu laden | Tailscale (einfacher) |
| **Verbindungsstatus ansehen** | Web-Dashboard | CLI oder Community-Oberfläche | Tailscale (einfacher) |
| **Probleme beheben** | Detaillierte Protokolle im Dashboard | Server- und Clientprotokolle | Tailscale (einfacher) |
| **Software aktualisieren** | Automatisch | Manuelle Serverupdates | Tailscale (einfacher) |
| **Konfiguration sichern** | Automatisch | Manuell (Datenbank und Konfiguration) | Tailscale (einfacher) |
| **Nach einem Ausfall wiederherstellen** | Automatisch | Manuelle Wiederherstellung aus einer Sicherung | Tailscale (einfacher) |

### Wartungsaufwand

**Tailscale (verwalteter Dienst):**
- ✅ Keine Serverwartung
- ✅ Automatische Updates und Sicherheitspatches
- ✅ Integrierte Redundanz und automatische Ausfallumschaltung
- ✅ Professioneller Support verfügbar
- ❌ Abhängig von der Verfügbarkeit des Tailscale-Dienstes

**Headscale (selbst gehostet):**
- ⚠️ Updates und Sicherheitspatches für das Serverbetriebssystem (monatlich)
- ⚠️ Headscale-Softwareupdates (alle 1–3 Monate)
- ⚠️ Datenbanksicherungen (täglich empfohlen)
- ⚠️ TLS-Zertifikate erneuern (automatisiert mit Let's Encrypt)
- ⚠️ Überwachung und Alarmierung einrichten
- ⚠️ Fehlerbehebung bei Störungen
- ✅ Vollständige Kontrolle über die Infrastruktur
- ✅ Unabhängig von Drittanbietern

**Geschätzter monatlicher Zeitaufwand:**
- **Tailscale:** 30 Minuten (Richtlinien prüfen, Nutzer hinzufügen)
- **Headscale:** 2–5 Stunden (Updates, Überwachung, Fehlerbehebung)

______

## Empfehlungen nach Anwendungsfall

### Wählen Sie Tailscale, wenn:

✅ **Sie die schnellstmögliche Einrichtung wünschen** - 5 Minuten von der Kontoerstellung bis zum funktionierenden Netzwerk\
✅ **Sie <100 Geräte haben** - Der kostenlose Tarif deckt private Nutzung und den Bedarf kleiner Unternehmen ab\
✅ **Ihnen einfache Bedienung wichtig ist** - Führende Weboberfläche und Benutzerfreundlichkeit\
✅ **Sie Unternehmensfunktionen benötigen** - SSO, Audit-Protokolle, Tailnet Lock, Gerätestatusprüfungen\
✅ **Sie Zeit sparen wollen** - Kein Wartungsaufwand, automatische Updates\
✅ **Sie garantierte Verfügbarkeit benötigen** - Das SLA von Tailscale garantiert im Enterprise-Tarif 99,99 % Verfügbarkeit\
✅ **Sie offizielle mobile Apps wünschen** - Native iOS- und Android-Apps mit vollem Funktionsumfang\
✅ **Sie professionellen Support benötigen** - Kostenpflichtige Tarife enthalten priorisierten Support\
✅ **Compliance für Sie wichtig ist** - Nach SOC 2 Typ II zertifiziert\
✅ **Sie ein gewerbliches Unternehmen betreiben** - Einfache Preise pro Nutzer ohne versteckte Kosten\

### Wählen Sie Headscale, wenn:

✅ **Sie vollständige Datensouveränität benötigen** - Alle Metadaten bleiben auf Ihrer Infrastruktur\
✅ **Sie Datenschutz- oder Compliance-Vorgaben erfüllen müssen** - Daten müssen in bestimmten Rechtsräumen bleiben\
✅ **Sie technisches Fachwissen mitbringen** - Sie kennen sich mit Linux-Systemadministration, Docker und Fehlerbehebung aus\
✅ **Sie >10 zahlende Nutzer haben** - Mit steigender Nutzerzahl werden die Einsparungen erheblich\
✅ **Sie dazulernen möchten** - Ein gutes Lernprojekt, um Mesh-VPNs zu verstehen\
✅ **Sie Open Source bevorzugen** - Sie können den Code prüfen, Korrekturen beisteuern und die Software anpassen\
✅ **Sie auf Ihr Budget achten** - Geringe laufende Kosten (5–30 $ pro Monat für den Server)\
✅ **Sie bereits Infrastruktur betreiben** - Lässt sich auf vorhandener Kubernetes- oder VM-Infrastruktur bereitstellen\
✅ **Sie eine gRPC-API benötigen** - Headscale bietet gRPC für erweiterte Automatisierung\
✅ **Sie bereits Dienste selbst hosten** - Passt zu Ihrer bestehenden selbst gehosteten Umgebung\

### Hybrider Ansatz: Beide Lösungen nutzen

Manche Organisationen nutzen **beide Lösungen**:

1. **Tailscale für die Produktion** - Kritische Infrastruktur mit SLA und Support
2. **Headscale für Entwicklung und Tests** - Kostengünstige Entwicklungsumgebungen
3. **Tailscale für Nutzer ohne technischen Hintergrund** - Einfacher Einstieg für Mitarbeitende
4. **Headscale für technische Teams** - Für Fachkräfte mit Erfahrung im Selbsthosting

______

## Migrationsszenarien

### Von Tailscale zu Headscale migrieren

**Beweggründe:** Kostensenkung, Datensouveränität, mehr Kontrolle

**Ablauf:**
1. Headscale-Server bereitstellen und seine Funktion prüfen
2. Headscale mit einer Auswahl unkritischer Geräte testen
3. ACLs aus Tailscale exportieren und für Headscale anpassen
4. Geräte schrittweise auf den Headscale-Koordinierungsserver umstellen
5. DNS-Konfigurationen und Subnetzrouten aktualisieren
6. Tailscale-Abonnement beenden

**Herausforderungen:**
- Kein automatisiertes Migrationswerkzeug verfügbar
- Alle Geräte müssen sich erneut authentifizieren
- Einige Funktionen (Funnel, Serve, Taildrop) verhalten sich unterschiedlich
- Die ACL-Syntax ist kompatibel, muss aber getestet werden

**Zeitaufwand:** Je nach Komplexität 5–20 Stunden

### Von Headscale zu Tailscale migrieren

**Beweggründe:** Geringerer Betriebsaufwand, Unternehmensfunktionen, besserer Support

**Ablauf:**
1. Tailscale-Konto erstellen und ACLs konfigurieren
2. Tailscale-Clients installieren (auf demselben Gerät können sie die vorhandenen Clients ersetzen)
3. Geräte umstellen, indem Sie `tailscale up` ohne eigenen Server ausführen
4. Verbindungen und Zugriffskontrollen prüfen
5. Headscale-Server außer Betrieb nehmen

**Herausforderungen:**
- Alle Geräte müssen sich erneut authentifizieren
- Einige Nutzer benötigen möglicherweise Tailscale-Konten (E-Mail oder SSO)
- Änderungen koordinieren und Nutzer informieren

**Zeitaufwand:** Je nach Umfang 2–8 Stunden

______

## Community und Ökosystem

### Tailscale-Ökosystem

| Ressource | Verfügbarkeit |
|----------|--------------|
| **Offizielle Dokumentation** | ✅ Umfangreich und gut gepflegt |
| **Community-Forum** | ✅ Aktives Forum mit Tailscale-Mitarbeitenden |
| **Discord-Community** | ✅ Sehr aktiv, Mitarbeitende antworten zeitnah |
| **GitHub Issues** | ❌ Proprietärer Quellcode (Feedback über das Forum) |
| **Stack Overflow** | ✅ Aktives Tag mit über 2.000 Fragen |
| **YouTube-Tutorials** | ✅ Offizielle Inhalte und Beiträge aus der Community |
| **Integrationen** | ✅ Docker, Kubernetes, Terraform, Synology, QNAP usw. |

### Headscale-Ökosystem

| Ressource | Verfügbarkeit |
|----------|--------------|
| **Offizielle Dokumentation** | ✅ Gut, von der Community gepflegt |
| **Community-Forum** | ⚠️ GitHub Discussions dient als Forum |
| **Discord-Community** | ✅ Aktiver Community-Server |
| **GitHub Issues** | ✅ Open Source, aktiver Issue-Tracker (über 38.900 Sterne) |
| **Stack Overflow** | ⚠️ Kleinere Community (ca. 100 Fragen) |
| **YouTube-Tutorials** | ⚠️ Beiträge aus der Community |
| **Weboberflächen** | ⚠️ Mehrere Optionen aus der Community (Headscale-UI, Headplane, ouroboros) |
| **Kubernetes-Operator** | ⚠️ Von der Community gepflegter Operator |

**Größe der Community (2026):**
- **Tailscale:** Über 100.000 aktive Community-Mitglieder, unterstützt von einem gut finanzierten Unternehmen
- **Headscale:** Über 10.000 aktive Community-Mitglieder, Open-Source-Projekt

______

## Leistungsmessungen unter Praxisbedingungen (2026)

Auf Grundlage von Community-Tests und veröffentlichten Benchmarks:

### Durchsatztests (Peer-to-Peer)

| Szenario | Tailscale | Headscale | Referenzwert (ohne VPN) |
|----------|-----------|-----------|-------------------|
| **Gigabit-LAN** | 940 Mbit/s | 940 Mbit/s | 945 Mbit/s |
| **WAN (100 Mbit/s)** | 98 Mbit/s | 98 Mbit/s | 100 Mbit/s |
| **WAN (Glasfaser mit 1 Gbit/s)** | 920 Mbit/s | 920 Mbit/s | 950 Mbit/s |
| **Kontinentübergreifend (DERP)** | 180 Mbit/s | 95 Mbit/s | Entfällt |

**Auswertung:** Direkte Peer-to-Peer-Verbindungen erzielen dieselbe Leistung. Bei Relay-Verbindungen hat Tailscale dank seiner globalen DERP-Infrastruktur einen Vorteil.

### Latenztests

| Szenario | Tailscale | Headscale | Referenzwert |
|----------|-----------|-----------|----------|
| **LAN-Ping** | 1,2 ms | 1,2 ms | 0,8 ms |
| **Regionales WAN (100 Meilen)** | 15 ms | 15 ms | 12 ms |
| **Landesweit** | 48 ms | 48 ms | 45 ms |
| **Kontinentübergreifend (direkt)** | 155 ms | 155 ms | 152 ms |
| **Kontinentübergreifend (DERP)** | 185 ms | 220 ms | Entfällt |

**Auswertung:** Bei direkten Verbindungen erhöhen beide Lösungen die Latenz nur geringfügig (ca. 1–2 ms). Die DERP-Latenz von Headscale hängt vom Serverstandort ab.

### Ressourcenverbrauch

| Messgröße | Tailscale-Client | Headscale-Client | Headscale-Instanz |
|--------|------------------|------------------|------------------|
| **RAM-Verbrauch (Leerlauf)** | 80–120 MB | 80–120 MB | 50–200 MB (abhängig von der Knotenzahl) |
| **RAM-Verbrauch (aktiv)** | 120–200 MB | 120–200 MB | 100–500 MB |
| **CPU-Auslastung (Leerlauf)** | <1 % | <1 % | <1 % |
| **CPU-Auslastung (aktiv)** | 5–15 % | 5–15 % | 3–20 % (abhängig von der Knotenzahl) |
| **Platzbedarf auf dem Datenträger** | 100–500 MB | 100–500 MB | 100 MB–2 GB (Datenbank) |

______

## Erweiterte Konfigurationsbeispiele

### Headscale mit Docker Compose

```yaml
version: '3'
services:
  headscale:
    image: headscale/headscale:0.28.0
    container_name: headscale
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:8080"  # API/Weboberfläche
      - "443:443"              # HTTPS
      - "3478:3478/udp"        # STUN
    volumes:
      - ./config:/etc/headscale
      - ./data:/var/lib/headscale
    command: serve
    environment:
      - TZ=UTC
```

### ACL-Beispiel für Headscale

```json
{
  "groups": {
    "group:admin": ["alice@", "bob@"],
    "group:developers": ["charlie@", "diana@"]
  },
  "hosts": {
    "production-db": "100.64.0.10/32",
    "staging-db": "100.64.0.20/32"
  },
  "acls": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["*:*"]
    },
    {
      "action": "accept",
      "src": ["group:developers"],
      "dst": ["staging-db:5432", "autogroup:self:*"]
    }
  ]
}
```

### Tailscale-Client für Headscale konfigurieren

```bash
# Linux
sudo tailscale up \
  --login-server=https://headscale.example.com \
  --accept-routes \
  --advertise-tags=tag:server

# Mit einem vorab authentifizierten Schlüssel
headscale preauthkeys create --user engineering --expiration 1h

sudo tailscale up \
  --login-server=https://headscale.example.com \
  --authkey=<YOUR_AUTH_KEY>
```

______

## Häufige Probleme beheben

### Probleme mit Tailscale

| Problem | Lösung |
|---------|----------|
| **Keine Verbindung zum Koordinierungsserver** | Firewall und Internetverbindung prüfen |
| **Direkte Verbindung schlägt fehl** | Tailscale weicht meist automatisch auf DERP aus. Prüfen Sie die NAT-Einstellungen |
| **Hohe Latenz** | Prüfen, ob eine direkte Verbindung besteht (ohne Relay) |
| **Schlüssel abgelaufen** | Erneut authentifizieren oder den Schlüsselablauf in der Administrationskonsole deaktivieren |
| **ACL blockiert Datenverkehr** | ACL-Regeln prüfen und Konfiguration testen |

### Probleme mit Headscale

| Problem | Lösung |
|---------|----------|
| **Knoten lassen sich nicht registrieren** | Erreichbarkeit der Headscale-URL und TLS-Zertifikat prüfen |
| **DNS-Auflösung schlägt fehl** | Prüfen, ob MagicDNS in config.yaml korrekt konfiguriert ist |
| **DERP-Relay funktioniert nicht** | Prüfen, ob der STUN-Port (3478/udp) offen ist und die DERP-Konfiguration stimmt |
| **Knoten sind nach einem Neustart offline** | Sicherstellen, dass die Clients beim Systemstart starten |
| **ACL-Änderungen greifen nicht** | Headscale neu laden: `systemctl reload headscale` |
| **Datenbank beschädigt** | Aus einer Sicherung wiederherstellen und PostgreSQL für den Produktivbetrieb erwägen |

### Diagnosebefehle

```bash
# Tailscale-Diagnose
tailscale status
tailscale netcheck
tailscale ping <hostname>
tailscale debug derp

# Headscale-Diagnose
headscale nodes list
headscale nodes list-routes
headscale debug routes
journalctl -u headscale -f  # Protokolle anzeigen
```

______

## Bewährte Sicherheitsmaßnahmen

### Für beide Lösungen

1. **Schlüsselablauf aktivieren** - Regelmäßige erneute Authentifizierung verlangen
2. **Prinzip der geringsten Rechte anwenden** - In ACLs nur die nötigen Zugriffsrechte erteilen
3. **Infrastrukturknoten mit Tags versehen** - Nutzergeräte von Servern trennen
4. **MFA aktivieren** - Für die Nutzeranmeldung eine Multi-Faktor-Authentifizierung verlangen
5. **Zugriffsprotokolle überwachen** - Verbindungsmuster regelmäßig prüfen
6. **Clients aktuell halten** - Sicherheitspatches zeitnah einspielen

### Sicherheitsmaßnahmen für Headscale

1. **Serverbetriebssystem härten** - CIS Benchmarks befolgen und unnötige Dienste abschalten
2. **Let's Encrypt verwenden** - Verwaltung von TLS-Zertifikaten automatisieren
3. **fail2ban einsetzen** - Brute-Force-Versuche unterbinden
4. **Regelmäßig sichern** - Automatische Datenbanksicherungen an einem separaten Speicherort ablegen
5. **Zeitnah aktualisieren** - Headscale-Veröffentlichungen auf Sicherheitspatches prüfen
6. **Netzwerk segmentieren** - Headscale-Server in einem Verwaltungs-VLAN isolieren
7. **Firewall aktivieren** - Nur erforderliche Ports freigeben (443, 3478/udp)

______

## Geplante Funktionen und Entwicklungsstand

### Tailscale-Roadmap (2026)

Laut öffentlichen Aussagen von Tailscale:
- ✅ **Veröffentlicht:** Aperture (Gateway für KI-Governance), erweiterte Gerätestatusprüfungen
- 🚧 **In Entwicklung:** Erweiterte Bedrohungserkennung, breitere Plattformunterstützung
- 📋 **Geplant:** Reiner IPv6-Modus, bessere Observability, weitere Integrationen

### Entwicklungsstand von Headscale (2026)

Auf Grundlage von GitHub-Meilensteinen und Diskussionen in der Community:
- ✅ **Kürzlich hinzugefügt:** OIDC-Authentifizierung, verbessertes DERP, bessere ACL-Unterstützung
- 🚧 **In Entwicklung:** Verbesserungen an Taildrop, bessere Integration von Weboberflächen
- 📋 **Wünsche der Community:** Entsprechung zu Funnel und Serve, erweiterte Protokollierung, Hochverfügbarkeitsmodus

**Bewertung des Reifegrads:**
- **Tailscale:** Für den Produktiv- und Unternehmenseinsatz geeignet, seit über 5 Jahren in Entwicklung
- **Headscale:** Für den Produktivbetrieb in grundlegenden Anwendungsfällen geeignet, aktiv und von der Community weiterentwickelt

______

## Fazit

**Tailscale** und **Headscale** bieten beide ausgezeichnete Funktionen für WireGuard-basierte Mesh-VPNs. Sie richten sich an unterschiedliche Zielgruppen und Anwendungsfälle.

**Wählen Sie Tailscale, wenn:**
- Ihnen eine einfache Bedienung wichtig ist und Sie in wenigen Minuten loslegen möchten
- Sie ein kleines Team mit <100 Geräten sind und vom großzügigen kostenlosen Tarif profitieren
- Sie Unternehmensfunktionen wie SSO, Audit-Protokollierung und professionellen Support benötigen
- Sie verwaltete Dienste dem Selbsthosting vorziehen
- Compliance-Zertifizierungen (SOC 2) für Sie wichtig sind

**Wählen Sie Headscale, wenn:**
- Sie vollständige Kontrolle über Ihre Infrastruktur und Metadaten benötigen
- Sie technisches Fachwissen haben und gerne selbst hosten
- Kostenoptimierung entscheidend ist (>10 zahlende Nutzer = erhebliche Einsparungen)
- Datensouveränität und Datenschutz für Sie oberste Priorität haben
- Sie Open-Source-Lösungen bevorzugen, deren Code Sie prüfen und anpassen können

**Zentrale Empfehlungen für 2026:**

1. **Start-ups und KMU:** Beginnen Sie mit dem **kostenlosen Tailscale-Tarif**. Für 0–100 Geräte ist er kaum zu schlagen.
2. **Unternehmens-IT:** **Tailscale Enterprise** mit SSO und Support bietet unter Berücksichtigung der Arbeitszeit die niedrigsten Gesamtbetriebskosten.
3. **Datenschutzbewusste Nutzer:** **Headscale** bietet maximale Kontrolle und maximalen Datenschutz.
4. **Technisch versierte Homelab-Nutzer:** **Headscale** bietet eine ausgezeichnete Lernmöglichkeit.
5. **Organisationen mit einem hybriden Ansatz:** Nutzen Sie **Tailscale für die Produktion**, **Headscale für Entwicklung und Tests**.

Beide Lösungen setzen für sichere, moderne Netzwerke auf führende WireGuard-Technik. Ihre Prioritäten entscheiden, wie Sie **Komfort und Kontrolle**, **verwalteten Betrieb und Selbsthosting** sowie **Kosten und Funktionsumfang** gewichten.

Für die meisten Organisationen bietet der **verwaltete Dienst von Tailscale** im Jahr 2026 die beste Balance aus Funktionsumfang, einfacher Bedienung und Preis-Leistungs-Verhältnis. Für Organisationen mit besonderen Anforderungen an Datensouveränität, Datenschutz oder Kosten **bietet Headscale eine überzeugende selbst gehostete Alternative**.

______

## Quellen und Ressourcen

1. [Offizielle Tailscale-Website](https://tailscale.com/)
2. [Tailscale-Dokumentation](https://tailscale.com/kb/)
3. [Offizielle Headscale-Dokumentation](https://headscale.net/)
4. [Headscale-Repository auf GitHub](https://github.com/juanfont/headscale)
5. [Offizielle WireGuard-Website](https://www.wireguard.com/)
6. [Tailscale-Blog: So funktioniert Tailscale](https://tailscale.com/blog/how-tailscale-works/)
7. [Zero-Trust-Architektur des NIST](https://csrc.nist.gov/publications/detail/sp/800-207/final)
8. [Technisches Whitepaper zu WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
