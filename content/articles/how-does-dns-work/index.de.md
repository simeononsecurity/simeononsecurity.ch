---
title: "So funktioniert DNS: DNS-Root, Bedeutung und Fehlerbehebung"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Erfahre, wie DNS und DNS-Root funktionieren, welche Hierarchie und Auflösungsschritte sie nutzen und wie Caching und Fehlerbehebung helfen."
genre: ["DNS-Grundlagen", "DNS-Root", "Domänennamensystem", "DNS-Auflösung", "DNS-Hierarchie", "DNS-Zwischenspeicherung", "DNS-Fehlerbehebung", "DNS-Datensätze", "DNS-Verwaltung", "DNS-Befehle"]
tags: ["DNS", "DNS-Root", "Domänennamensystem", "DNS-Auflösung", "DNS-Hierarchie", "DNS-Zwischenspeicherung", "DNS-Datensätze", "DNS-Verwaltung", "DNS-Fehlerbehebung", "Netzwerke", "Internetinfrastruktur", "IP-Adressen", "Websitezugriff", "rekursive Abfrage", "autoritative Nameserver", "TTL", "Cachingmechanismen", "DNS-Cache leeren", "DNS-Root-Server", "Anycast-Weiterleitung", "ICANN", "DNS-Zusammenarbeit", "A-Eintrag", "AAAA-Eintrag", "CNAME-Eintrag", "MX-Eintrag", "TXT-Eintrag", "SRV-Eintrag", "NS-Eintrag", "PTR-Eintrag", "SOA-Eintrag", "DNS-Diagnosebefehle", "Windows", "macOS", "Linux", "Eingabeaufforderung", "Terminalprogramm"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Darstellung miteinander verbundener Computernetzwerke mit Domainnamen und IP-Adressen, die DNS und DNS-Root veranschaulichen."
coverCaption: "Entdecke DNS und beherrsche das Domänennamensystem"
---

## So funktionieren DNS und DNS-Root

### Einleitung

Das Domänennamensystem (DNS) ist ein wichtiger Teil der Internetinfrastruktur. Es ermöglicht den Zugriff auf Websites über Domainnamen statt IP-Adressen. DNS funktioniert wie ein Telefonbuch: Es übersetzt lesbare Domainnamen in IP-Adressen, die Computer verstehen. An der Spitze steht DNS-Root, ein hierarchisches und verteiltes System für die Namensauflösung. Dieser Artikel erklärt DNS, DNS-Root und die Einträge, die zu einer Domain gehören können.

{{< youtube id="mpQZVYPuDGU" >}}

## Das Domänennamensystem (DNS)

Das **Domänennamensystem (DNS)** ist ein dezentrales Namenssystem, das Domainnamen IP-Adressen zuordnet. Du erreichst Websites und andere Internetressourcen, indem du einen Domainnamen in den Browser eingibst. DNS erspart dir das Merken komplexer IP-Adressen.

### DNS-Hierarchie

DNS ist hierarchisch aufgebaut und besteht aus mehreren Ebenen. Oben liegt die Root-Zone, darunter folgen Top-Level-Domains (TLDs), Domains der zweiten Ebene und Subdomains. Jede Ebene ist Teil des vollständigen Domainnamens. Bei `www.example.com` ist „www“ die Subdomain, „example“ die Domain der zweiten Ebene und „com“ die TLD.

### DNS-Auflösung

Wenn du einen Domainnamen in den Browser eingibst, beginnt die DNS-Auflösung. Der Browser sendet eine DNS-Abfrage an einen DNS-Resolver, der meist vom Internetanbieter (ISP) bereitgestellt wird. Der Resolver durchläuft mehrere Schritte, um den Domainnamen aufzulösen und die zugehörige IP-Adresse zu ermitteln.

1. **Lokaler DNS-Cache**: Der Resolver prüft zuerst seinen lokalen Cache auf den angefragten Domainnamen und die IP-Adresse. Sind die Daten vorhanden, gibt er das Ergebnis sofort zurück.

2. **Rekursive Abfrage**: Fehlen die Daten im Cache, startet der Resolver eine rekursive Abfrage. Zuerst fragt er die DNS-Root-Server ab, die für die Zone „.“ (Punkt) zuständig sind. Die Root-Server nennen die IP-Adressen der TLD-Server für die angefragte Domain.

3. **TLD-Abfrage**: Der Resolver kontaktiert die im vorherigen Schritt genannten TLD-Server und fragt nach den IP-Adressen der autoritativen Nameserver für die Domain.

4. **Abfrage beim autoritativen Nameserver**: Der Resolver fragt die von den TLD-Servern genannten autoritativen Nameserver ab. Diese enthalten die autoritativen Einträge der Domain und antworten mit der zugehörigen IP-Adresse.

5. **Antwort an den Client**: Der Resolver erhält die IP-Adresse von den autoritativen Nameservern und sendet sie an den Browser zurück. Der Browser kann anschließend über diese Adresse eine Verbindung zum Webserver herstellen.

### DNS-Zwischenspeicherung

DNS-Resolver verwenden Caching, um die Leistung zu verbessern und DNS-Server zu entlasten. Nach einer Antwort speichert der Resolver die Zuordnung von Domainname und IP-Adresse lokal. Spätere Abfragen nach demselben Domainnamen können direkt aus dem Cache beantwortet werden.

Caching findet auf mehreren Ebenen statt, etwa beim lokalen Resolver, beim Resolver des Internetanbieters und auf Geräten wie Routern und Betriebssystemen. Der Time-to-Live-Wert (TTL) in der DNS-Antwort legt fest, wie lange ein Eintrag im Cache bleibt. Nach Ablauf der TTL entfernt der Resolver den Eintrag und fragt die Daten erneut ab.

#### Lokalen DNS-Cache leeren

Das Leeren des DNS-Caches hilft bei bestimmten DNS-Problemen und sorgt dafür, dass dein System aktuelle Einträge abruft. So leerst du den Cache unter verschiedenen Betriebssystemen:

##### Windows

So leerst du den DNS-Cache unter Windows:

1. Drücke `Win + R`, gib `cmd` ein und bestätige mit Enter, um die Eingabeaufforderung zu öffnen.

2. Gib den folgenden Befehl ein und drücke Enter:

```bash
ipconfig /flushdns
```

Der Befehl leert den Cache des DNS-Resolvers unter Windows.

##### macOS

So leerst du den DNS-Cache unter macOS:

1. Öffne das Terminalprogramm unter Programme > Dienstprogramme oder suche danach mit Spotlight.

2. Gib den folgenden Befehl ein und drücke Enter:

```bash
sudo killall -HUP mDNSResponder
```

Der Befehl startet mDNSResponder neu, den Prozess für die DNS-Auflösung unter macOS.

##### Linux

Der Ablauf zum Leeren des DNS-Caches hängt unter Linux von der Distribution und dem DNS-Resolver ab. Zwei gängige Methoden sind:

1. **Systeme mit systemd (z. B. Ubuntu, Fedora)**:

Öffne das Terminalprogramm und führe den folgenden Befehl mit Administratorrechten aus:

```bash
sudo systemd-resolve --flush-caches

```

Der Befehl leert den DNS-Cache auf Systemen, die systemd-resolved als Resolver verwenden.

2. **Systeme ohne systemd**:

Öffne das Terminalprogramm und führe den folgenden Befehl mit Administratorrechten aus:

```bash
sudo /etc/init.d/nscd restart

```

Der Befehl startet den Name Service Cache Daemon (nscd) neu, der DNS auf Linux-Distributionen ohne systemd zwischenspeichert.

Diese Schritte sind allgemeine Hinweise. Befehle und Methoden können je nach Betriebssystemversion abweichen. Das Leeren des DNS-Caches behebt manche DNS-Probleme, aber nicht alle Netzwerkverbindungsprobleme.

## So funktioniert das DNS-Root-System

Das DNS-Root-System ist ein grundlegender Teil der DNS-Infrastruktur. So arbeitet es:

### 1. Root-Zone und Root-Server

Das DNS-Root-System beginnt mit der **Root-Zone**, der obersten Ebene der DNS-Hierarchie. Die Root-Zone enthält Informationen zu den autoritativen Nameservern aller Top-Level-Domains (TLDs), etwa .com, .org, .net und Länder-TLDs wie .us und .uk.

Das DNS-Root-System besteht aus 13 Root-Servern mit den Bezeichnungen A bis M. Sie sind weltweit geografisch verteilt und bieten dadurch Redundanz und Zuverlässigkeit.

### 2. Anycast-Weiterleitung

Um das hohe DNS-Aufkommen zu bewältigen, verwenden die Root-Server **Anycast-Weiterleitung**. Dabei teilen sich mehrere Server dieselbe IP-Adresse, befinden sich aber an verschiedenen Orten. Die Netzbedingungen leiten Abfragen an einen passenden Server weiter und verteilen so die Last effizient.

Wenn ein Nutzer eine DNS-Abfrage startet, leitet Anycast sie an einen verfügbaren Root-Server in der Nähe. Die Netzwerkinfrastruktur wählt anhand der Netzbedingungen den kürzesten Pfad. Anycast verteilt die Last und hilft, Engpässe zu vermeiden.

### 3. Rekursive DNS-Resolver

Erhält ein DNS-Resolver eine Abfrage für einen Domainnamen, beginnt er mit der rekursiven Auflösung und kontaktiert einen Root-Server.

Der Root-Server antwortet mit einem Verweis auf die IP-Adressen der TLD-Nameserver für die angefragte TLD. Diese TLD-Server enthalten Informationen zu den autoritativen Nameservern der Domains innerhalb der TLD.

### 4. Verweise und autoritative Nameserver

Nach dem Verweis des Root-Servers kontaktiert der Resolver den zuständigen TLD-Nameserver.

Der TLD-Nameserver antwortet mit einem weiteren Verweis und nennt die IP-Adressen der autoritativen Nameserver für die angefragte Domain.

Der Resolver fragt anschließend bei den autoritativen Nameservern nach der IP-Adresse des Domainnamens.

### 5. Caching und TTL

Während der DNS-Auflösung verbessert Caching die Leistung und senkt die Belastung der DNS-Server. Resolver speichern Zuordnungen von Domainnamen zu IP-Adressen.

DNS-Datensätze werden für die durch den Time-to-Live-Wert (TTL) festgelegte Dauer zwischengespeichert. Die TTL gibt an, wie lange ein Eintrag gültig bleibt. Danach entfernt der Resolver den Cache-Eintrag und fragt die aktuelle IP-Adresse erneut ab.

### 6. Zusammenarbeit und Verwaltung

Das DNS-Root-System wird gemeinsam von der Internet Corporation for Assigned Names and Numbers (ICANN) und den Betreiber der Root-Server verwaltet.

ICANN beaufsichtigt die allgemeine Verwaltung und Koordination des DNS und arbeitet eng mit den Betreiber der Root-Server zusammen. Gemeinsam pflegen sie die Root-Zonendatei mit Informationen zu den 13 DNS-Root-Servern und den zugehörigen IP-Adressen.

Die Betreiber der Root-Server stellen den Betrieb und die Verfügbarkeit der Root-Server sicher. Damit tragen sie zur Stabilität und Widerstandsfähigkeit der DNS-Infrastruktur bei.

Das DNS-Root-System ist der Ausgangspunkt der DNS-Auflösung. Es ermöglicht die Zuordnung von Domainnamen zu IP-Adressen, damit Nutzer Websites und andere Internetressourcen effizient erreichen.

#### Die 13 DNS-Root-Server

Die 13 DNS-Root-Server sind mit den Buchstaben A bis M gekennzeichnet. Jeder Server wird an verschiedenen physischen Standorten betrieben, um Redundanz und Ausfallsicherheit zu gewährleisten. Sie bearbeiten Abfragen für die Root-Zone, darunter TLDs wie .com, .org, .net und Länder-TLDs wie .us und .uk.

#### ICANN und die Verwaltung von DNS-Root

Die Internet Corporation for Assigned Names and Numbers (**ICANN**) ist für die Verwaltung und Koordination des DNS sowie die Zuteilung von IP-Adressen zuständig. ICANN arbeitet mit den Betreiber der Root-Server an der Stabilität und Sicherheit von DNS-Root. Gemeinsam pflegen sie die Root-Zonendatei mit Informationen zu den 13 Root-Servern und ihren IP-Adressen.

______

## DNS-Eintragstypen und ihre Aufgaben

{{< youtube id="HnUDtycXSNE" >}}

DNS-Datensätze sind wichtige Bestandteile des Domänennamensystems (DNS). Sie enthalten verschiedene Informationen zu einem Domainnamen. Hier sind einige häufige Typen und ihre Aufgaben:

| Eintragstyp | Beschreibung | Beispiel |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Ordnet einem Domainnamen eine IPv4-Adresse zu. | `example.com     IN A 192.0.2.1` |
| AAAA | Ordnet einem Domainnamen eine IPv6-Adresse zu. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Ordnet einen Alias (kanonischen Namen) dem tatsächlichen Domainnamen zu. | `www.example.com IN CNAME example.com` |
| MX | Gibt die Mailserver an, die eingehende E-Mails für die Domain annehmen. | `example.com     IN MX 10 mail.example.com` |
| TXT | Speichert beliebigen Text, oft für SPF, DKIM oder die Domainprüfung. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Gibt die autoritativen Nameserver der Domain an. | `example.com     IN NS ns1.example.com` |
| SOA | Legt globale Eigenschaften der Zone fest (Start-of-Authority-Eintrag). | `example.com     IN SOA ns1.example.com` |
| SRV | Definiert den Standort eines bestimmten Domain-Dienstes. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Ordnet einer IP-Adresse einen Domainnamen zu (Reverse-DNS-Abfrage). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. A-Eintrag (Adresseneintrag)

Der **A-Eintrag** ordnet einem Domainnamen eine IPv4-Adresse zu. Er ist der einfachste und am häufigsten verwendete DNS-Eintrag. Wenn du einen Domainnamen im Browser eingibst, hilft der A-Eintrag, die IP-Adresse des Webservers zu finden, auf dem die Website liegt.

### 2. AAAA-Eintrag (IPv6-Adresseneintrag)

Der **AAAA-Eintrag** erfüllt denselben Zweck wie der A-Eintrag, ordnet dem Domainnamen aber eine IPv6-Adresse zu. Mit der Umstellung auf IPv6 werden AAAA-Einträge für Verbindungen über IPv6-Netze immer wichtiger.

### 3. CNAME-Eintrag (Eintrag für den kanonischen Namen)

Der **CNAME-Eintrag** erstellt einen Alias oder kanonischen Namen für eine Domain. Er wird verwendet, wenn eine Domain oder Subdomain auf eine andere Domain oder Subdomain zeigen soll. Du kannst zum Beispiel einen CNAME-Eintrag erstellen, der "www" auf "mywebsite.com" verweist.

### 4. MX-Eintrag (Mailserver-Eintrag)

Der **MX-Eintrag** gibt den Mailserver an, der eingehende Nachrichten für eine Domain annimmt. Er legt fest, an welchen Server E-Mails zugestellt werden. Mehrere MX-Einträge können Prioritätswerte haben, die die Reihenfolge festlegen, wenn der primäre Server nicht erreichbar ist.

### 5. TXT-Eintrag (Texteintrag)

Der **TXT-Eintrag** speichert Textinformationen zu einer Domain. Häufige Einsatzzwecke sind die Domainprüfung, SPF-Einträge (Sender Policy Framework) zur E-Mail-Authentifizierung sowie allgemeine Informationen oder Hinweise.

### 6. SRV-Eintrag (Diensteintrag)

Der **SRV-Eintrag** definiert den Standort eines bestimmten Dienstes oder einer Ressource innerhalb einer Domain. Er wird etwa für VoIP, Instant Messaging und andere Anwendungen verwendet, die bestimmte Server oder Dienste finden müssen.

### 7. NS-Eintrag (Nameserver-Eintrag)

Der **NS-Eintrag** gibt die autoritativen Nameserver für eine Domain an. Diese Server enthalten die DNS-Datensätze der Domain. Ein DNS-Resolver fragt NS-Einträge ab, um die zuständigen Nameserver zu finden.

### 8. PTR-Eintrag (Zeigereintrag)

Der **PTR-Eintrag** ordnet bei Reverse-DNS-Abfragen einer IP-Adresse einen Domainnamen zu. Er wird häufig verwendet, um die Identität eines Mailservers zu prüfen und Spam vorzubeugen. Reverse-DNS-Abfragen helfen dabei, die Echtheit eines E-Mail-Servers zu bestätigen.

### 9. SOA-Eintrag (Eintrag zum Zonenbeginn)

Der **SOA-Eintrag** enthält Verwaltungsinformationen zu einer Domain. Dazu gehören der primäre autoritative Nameserver, die Kontakt-E-Mail-Adresse des Domainadministrators und verschiedene Zeitparameter für die DNS-Datensätze.

Dies sind nur einige der vielen DNS-Eintragstypen. Jeder hat einen bestimmten Zweck und unterstützt die effiziente und korrekte Auflösung von Domainnamen zu den zugehörigen Ressourcen.

______

## DNS-Fehlerbehebungsbefehle für verschiedene Betriebssysteme

Bei DNS-Problemen helfen Diagnosebefehle, die Ursache zu ermitteln. Hier sind häufig verwendete Befehle für verschiedene Betriebssysteme:

### Windows

#### 1. `ipconfig /flushdns`

Dieser Befehl leert den DNS-Cache unter Windows und hilft bei veralteten oder falschen DNS-Datensätzen. Öffne die Eingabeaufforderung und führe den Befehl aus.

#### 2. `ipconfig /all`

`ipconfig /all` zeigt detaillierte Informationen zu den Netzwerkschnittstellen deines Windows-Systems, einschließlich der konfigurierten DNS-Server. So lässt sich prüfen, ob die richtigen Server verwendet werden.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Dieser Befehl startet mDNSResponder unter macOS neu, den Prozess für die DNS-Auflösung. Das kann DNS-Einstellungen aktualisieren und Probleme beheben. Öffne das Terminalprogramm und führe den Befehl mit Administratorrechten aus.

#### 2. `nslookup`

Mit `nslookup` kannst du DNS-Datensätze abfragen, die Namensauflösung testen und die Verbindung zu DNS-Servern prüfen. Öffne das Terminalprogramm und führe `nslookup` gefolgt vom Domainnamen oder der IP-Adresse aus, die du untersuchen möchtest.

### Linux

#### 1. `systemd-resolve --flush-caches`

Auf Linux-Systemen, die systemd als DNS-Resolver verwenden, leert `systemd-resolve --flush-caches` den DNS-Cache. Das kann Probleme durch veraltete Cache-Einträge beheben. Öffne das Terminalprogramm und führe den Befehl mit Administratorrechten aus.

#### 2. `dig`

`dig` ist ein vielseitiges DNS-Diagnosewerkzeug für Linux. Es zeigt ausführliche Informationen zu DNS-Abfragen, Antworten und Serverkonfigurationen. Mit `dig` kannst du bestimmte DNS-Datensätze abfragen, die Namensauflösung testen und DNS-Probleme untersuchen. Öffne das Terminalprogramm und führe `dig` gefolgt vom Domainnamen oder der IP-Adresse aus.

Diese Befehle helfen dabei, DNS-Probleme auf verschiedenen Betriebssystemen zu diagnostizieren und zu beheben. Sie geben Einblick in DNS-Konfigurationen, Servereinstellungen und Verbindungsprobleme.

Befehle und Optionen unterscheiden sich je nach Betriebssystemversion und Distribution. Lies die Dokumentation für deine Version, um Details zur Verwendung zu erhalten.
______


## Fazit

Das Domänennamensystem (DNS) und DNS-Root spielen eine wichtige Rolle für das Internet. DNS ermöglicht den Zugriff auf Websites über leicht verständliche Domainnamen. DNS-Root bildet die Grundlage der gesamten DNS-Hierarchie. Wenn du verstehst, wie beide funktionieren, kannst du das Web besser nutzen und die Infrastruktur hinter Onlineangeboten einordnen.

______

## Quellen

- [DNS auf Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [So funktioniert DNS bei Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Offizielle Website von ICANN](https://www.icann.org/)
- [Betreiber der Root-Server](https://www.root-servers.org/)
