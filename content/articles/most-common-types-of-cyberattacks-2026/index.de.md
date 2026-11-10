---
title: "Die häufigsten Arten von Cyberangriffen und wie Verteidiger sie erkennen"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Lernen Sie die häufigsten Arten von Cyberangriffen kennen, erkennen Sie ihre Spuren in Protokollen und Telemetriedaten und üben Sie die Erkennung in einem Sicherheitslabor zu Hause."
genre: ["Cybersicherheit", "Bedrohungserkennung", "Blue Team", "Sicherheitsbetrieb", "Berufliche Entwicklung"]
tags: ["Arten von Cyberangriffen", "Malware", "Ransomware", "Phishing", "Spear-Phishing", "Social Engineering", "Spoofing", "identitätsbasierte Angriffe", "Credential Stuffing", "Password Spraying", "SQL-Injection", "Cross-Site-Scripting", "Angriff auf die Lieferkette", "Insider-Bedrohung", "DNS-Tunneling", "IoT-Angriffe", "KI-gestützte Angriffe", "Denial-of-Service", "Detection Engineering", "SOC-Analyst", "Blue Team", "Heimlabor", "Protokollanalyse", "Reaktion auf Sicherheitsvorfälle", "MITRE ATT&CK", "Karriere in der Cybersicherheit", "Threat Hunting", "Security Operations Center", "Telemetrie", "Alarm-Triage"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Eine digitale Illustration mit farbigen abstrakten Symbolen für verschiedene Arten von Cyberangriffen wie Ransomware, Phishing und Denial-of-Service vor dunklem Hintergrund."
coverCaption: ""
---

Ein **Angriffstyp** ist eine Technik-Kategorie und kein einzelnes Werkzeug. Ransomware, Phishing und Credential Stuffing bezeichnen Methoden, die ein Angreifer mit geringfügigen Variationen wiederholt gegen viele Ziele einsetzt. Wenn Sie diese Kategorien kennen, erhalten Sie ein gedankliches Verzeichnis der Warnmeldungen, denen Sie in einem Sicherheitsteam begegnen.

*Einzelne Malware-Familien tauchen auf und verschwinden innerhalb weniger Monate. Die folgenden Angriffskategorien sind seit Jahren stabil, und jede hinterlässt eine erkennbare Spur in der Endpoint-, Identitäts-, Netzwerk- oder E-Mail-Telemetrie.*

<!--more-->

## Wichtigste Erkenntnisse

- **Lernen Sie das Muster, nicht die Nutzlast.** Angriffskategorien ändern sich viel langsamer als einzelne Werkzeuge.
- **Jede Kategorie hinterlässt Spuren.** Die Erkennungsarbeit beginnt mit der Frage, welche Telemetrie die Aktivität erfasst.
- **Reproduzieren Sie einen Angriff, um ihn zu verstehen.** Ein Heimlabor macht aus einer abstrakten Kategorie eine aufgezeichnete Beobachtung.
- **Dokumentieren Sie Ihre Ergebnisse.** Eine kurze Untersuchungsnotiz belegt Ihre Arbeit und erklärt die Beweise.

## Die Angriffstypen im Überblick

Die Tabelle enthält Kategorien, denen Sicherheitsteams besonders häufig begegnen. Die folgenden Abschnitte beschreiben jede Kategorie, ihre gängigen Varianten und die Daten, die Verteidiger zu ihrer Erkennung untersuchen.

| Angriffstyp | Wirkung |
|---|---|
| **Malware** | Führt Schadsoftware wie Ransomware, Spyware und Trojaner aus |
| **Denial-of-Service** | Überflutet einen Dienst mit Datenverkehr, bis legitime Nutzer keinen Zugriff mehr haben |
| **Phishing** | Täuscht eine Person, damit sie Zugangsdaten preisgibt oder eine schädliche Datei ausführt |
| **Spoofing** | Gibt einen Angreifer als vertrauenswürdiges System, einen Absender oder eine Adresse aus |
| **Identitätsbasierte Angriffe** | Missbrauchen gestohlene oder gefälschte Zugangsdaten, um als gültiger Nutzer aufzutreten |
| **Code-Injection** | Fügt schädlichen Code in eine Anwendung ein und verändert so deren Verhalten |
| **Angriffe auf die Lieferkette** | Kompromittieren einen vertrauenswürdigen Anbieter, eine Bibliothek oder einen Update-Kanal |
| **Social Engineering** | Manipuliert eine Person zu einer unsicheren Handlung |
| **Insider-Bedrohungen** | Missbrauchen Zugriffsrechte eines aktuellen oder ehemaligen Mitarbeiters |
| **DNS-Tunneling** | Kodiert Daten in DNS-Abfragen, um Kontrollen zu umgehen |
| **IoT-Angriffe** | Greifen vernetzte Geräte an, um ins Netzwerk vorzudringen, zu spionieren oder einem Botnetz beizutreten |
| **KI-gestützte Angriffe** | Nutzen maschinelles Lernen, um Inhalte zu erstellen, Personen zu imitieren oder Filter zu umgehen |

**Hinweis zum Umfang:** Diese Kategorien überschneiden sich. Eine Phishing-E-Mail verbreitet oft Malware, und auf einen erfolgreichen Zugangsdaten-Diebstahl folgt häufig ein identitätsbasierter Angriff. Betrachten Sie die Liste als verschiedene Blickwinkel und nicht als starre Einteilungen.

______

## Malware

**Malware** umfasst jedes Programm, das ein System schädigen, kontrollieren oder zu Geld machen soll. Der Begriff umfasst Ransomware, dateilose Malware, Spyware, Adware, Trojaner, Würmer, Rootkits, Keylogger und Botnetze.

| Untertyp | Verhalten |
|---|---|
| **Ransomware** | Verschlüsselt Dateien und verlangt eine Zahlung für den Entschlüsselungsschlüssel |
| **Dateilose Malware** | Nutzt integrierte Systemwerkzeuge und schreibt nur wenig auf die Festplatte |
| **Spyware** | Sammelt unbemerkt Daten über Aktivitäten |
| **Trojaner** | Gibt sich als legitime Software aus, um ausgeführt zu werden |
| **Wurm** | Kopiert sich ohne Zutun eines Nutzers auf andere Hosts |
| **Rootkit** | Versteckt sich im Betriebssystem, um dauerhaft die Kontrolle zu behalten |

**Wo die Beweise liegen:** Endpoint-Detection-and-Response-Werkzeuge, kurz **EDR**, erfassen Prozessbäume, Befehlszeilen, Dateischreibvorgänge und Änderungen an der Registrierung. Auch ein dateiloser Angriff erzeugt Prozess- und Skripttelemetrie, weil das Betriebssystem die missbrauchten Werkzeuge weiterhin startet.

______

## Denial-of-Service

**Ein Denial-of-Service-Angriff (DoS)** überflutet ein Ziel mit Anfragen, bis legitime Nutzer keinen Zugriff mehr haben. **Ein verteilter Denial-of-Service-Angriff (DDoS)** nutzt dieselbe Methode gleichzeitig von vielen Systemen aus. Dadurch lässt sich der Datenverkehr viel schwerer anhand der Quelladresse filtern.

| Merkmal | DoS | DDoS |
|---|---|---|
| **Ursprung** | Ein System | Viele Systeme |
| **Schwierigkeit der Abwehr** | Mittel | Hoch, weil sich die Quellen über viele Netzwerke verteilen |
| **Typische Auswirkung** | Verlust der Verfügbarkeit | Verlust der Verfügbarkeit in größerem Umfang |

**Wo die Beweise liegen:** Verkehrsvolumen im Vergleich zur Baseline, Verbindungen pro Quelle, sprunghafte Anstiege der Anfragerate und Veränderungen der Fehlerrate. Die Verfügbarkeitsüberwachung schlägt oft Alarm, bevor das Sicherheitsteam den Vorfall bemerkt.

______

## Phishing

**Phishing** nutzt E-Mails, Textnachrichten, Telefonanrufe oder soziale Medien, um eine Person zur Preisgabe von Zugangsdaten oder zum Öffnen eines schädlichen Anhangs zu bewegen. Die Kategorie unterscheidet sich nach Ziel und Kanal.

| Variante | Ziel und Kanal |
|---|---|
| **Spear-Phishing** | Eine bestimmte Person oder ein Team, meist per E-Mail |
| **Whaling** | Führungskräfte, oft mit dem Ziel, Geld oder Daten zu bewegen |
| **Smishing** | Betrügerische Textnachrichten |
| **Vishing** | Betrügerische Anrufe oder Sprachnachrichten |

**Wo die Beweise liegen:** Protokolle des E-Mail-Gateways, Ergebnisse der URL-Analyse, Anhangsanalysen und Meldungen von Nutzern. Die Meldung eines aufmerksamen Mitarbeiters gehört zu den wertvollsten Signalen auf dieser Liste.

______

## Spoofing

**Spoofing** verbirgt einen Angreifer hinter einer vertrauenswürdigen Identität, damit das Ziel eine Verbindung, Nachricht oder Adresse akzeptiert. Die Tarnung verschafft Zeit und umgeht Prüfungen, die auf Vertrauen beruhen.

| Typ | Was gefälscht wird |
|---|---|
| **Domain-Spoofing** | Eine ähnliche Website oder E-Mail-Domain, die eine echte Marke imitiert |
| **E-Mail-Spoofing** | Die Absenderadresse einer Nachricht |
| **ARP-Spoofing** | Eine lokale Netzwerkadresse, um Datenverkehr zwischen zwei Hosts abzufangen |

**Wo die Beweise liegen:** SPF-, DKIM- und DMARC-Ergebnisse in E-Mail-Kopfzeilen, das Alter einer Domain, Zertifikatsabweichungen und Warnungen vor doppelten Adressen im lokalen Netzwerk.

______

## Identitätsbasierte Angriffe

**Identitätsbasierte Angriffe** nutzen ein gültiges Konto statt einer Softwareschwachstelle. Der Angreifer verfügt über funktionierende Zugangsdaten. Daher ähnelt die Aktivität einer normalen Nutzung und geht im Hintergrund unter. Diese Kategorie verursacht einen großen Teil der Warnmeldungen, die ein **Security Operations Center (SOC)** täglich bearbeitet.

*Wenn Sie eine Kategorie im Heimlabor üben, wählen Sie diese. Die Signale sind aussagekräftig, die Übungen lassen sich wiederholen und die Einrichtung bleibt überschaubar.*

| Technik | Ablauf |
|---|---|
| **Kerberoasting** | Fordert ein Service-Ticket an und knackt anschließend das verschlüsselte Passwort offline |
| **Man-in-the-Middle (MITM)** | Schaltet sich zwischen zwei Parteien, um eine Sitzung mitzulesen oder zu verändern |
| **Pass-the-Hash** | Verwendet einen gestohlenen Passwort-Hash erneut, um eine neue Sitzung zu öffnen |
| **Golden Ticket** | Fälscht ein Kerberos-Ticket-Granting-Ticket für weitreichenden Domänenzugriff |
| **Silver Ticket** | Fälscht ein Service-Ticket für einen einzelnen Dienst |
| **Abgreifen von Zugangsdaten** | Sammelt Benutzernamen und Passwörter in großer Zahl |
| **Credential Stuffing** | Probiert dieselben Zugangsdaten bei vielen nicht zusammengehörigen Websites erneut aus |
| **Password Spraying** | Probiert ein häufiges Passwort bei vielen Konten aus |
| **Brute Force** | Probiert viele Passwörter bei einem Konto aus |
| **Downgrade** | Erzwingt eine schwächere Protokollversion für eine Verbindung |

**Wo die Beweise liegen:** Anmeldeprotokolle, fehlgeschlagene Authentifizierungen, Token-Anomalien, Warnungen vor unmöglichen Reisen und Erkennungen von Identitätsrisiken. **Adversary-in-the-Middle-Phishing (AiTM)** gehört ebenfalls hierher, weil der Angreifer ein aktives Sitzungstoken statt eines Passworts stiehlt. Die spätere Wiederverwendung von unbekannter Infrastruktur löst dann die Erkennung von Identitätsrisiken aus.

______

## Code-Injection

**Code-Injection** fügt von einem Angreifer kontrollierten Code in eine verwundbare Anwendung ein, damit die Anwendung ihn im normalen Betrieb ausführt. Die Anwendung und nicht der Angreifer führt die schädliche Aktion aus.

| Typ | Ziel |
|---|---|
| **SQL-Injection** | Eine Datenbankabfrage, die aus ungeprüften Eingaben erstellt wurde |
| **Cross-Site-Scripting (XSS)** | Eine Webseite, die ein Besucherscript im Browser ausführt |
| **Malvertising** | Ein legitimer Werbeplatz, der mit schädlichem Code gefüllt ist |
| **Data Poisoning** | Ein Trainingsdatensatz für ein KI- oder Machine-Learning-Modell |

**Wo die Beweise liegen:** Webanwendungsprotokolle, Datenbankabfragen, Berichte der Content Security Policy und Anfragemuster, die von der normalen Anwendungsnutzung abweichen.

______

## Angriffe auf die Lieferkette

**Ein Angriff auf die Lieferkette** zielt auf einen vertrauenswürdigen Drittanbieter, dessen Produkt oder Dienst viele Kunden erreicht. **Ein Software-Lieferkettenangriff** fügt schädlichen Code in eine Anwendung, Bibliothek oder Aktualisierung ein, sodass alle Nutzer des Produkts ihn erhalten. **Ein Hardware-Lieferkettenangriff** kompromittiert eine physische Komponente vor dem Versand.

*Moderne Software ist auf Bibliotheken von Drittanbietern angewiesen. Eine einzige kompromittierte Abhängigkeit erreicht deshalb weit mehr Nutzer als der ursprüngliche Anbieter.*

**Wo die Beweise liegen:** Software-Composition-Analysis, Build-Pipeline-Protokolle, unerwartete ausgehende Verbindungen von einem vertrauenswürdigen Update und Integritätsprüfungen ausgelieferter Artefakte.

______

## Social Engineering

**Social Engineering** nutzt psychischen Druck, um eine Person zu einer unsicheren Handlung zu bewegen. Der Angreifer setzt auf Autorität, Dringlichkeit, Angst, Geld oder Vertrauen.

| Technik | Vorgehen |
|---|---|
| **Pretexting** | Erfindet eine glaubwürdige Situation, um Vertrauen zu gewinnen |
| **Business Email Compromise (BEC)** | Gibt sich als vertrauenswürdiger Kollege aus, um eine Zahlung umzuleiten oder Daten zu erhalten |
| **Desinformation** | Verbreitet über soziale Medien und Bots falsche Erzählungen |
| **Quid pro quo** | Bietet eine Belohnung im Austausch gegen Informationen oder Zugriff |
| **Honeytrap** | Baut eine falsche Beziehung auf, um Geld, Daten oder Zugriff zu erhalten |
| **Tailgating** | Folgt einem Mitarbeiter durch eine gesicherte Tür |

**Wo die Beweise liegen:** Ergebnisse der E-Mail-Authentifizierung, ungewöhnliche Anfragen zur Änderung von Zahlungen, Helpdesk-Aufzeichnungen und Protokolle physischer Zutritte.

______

## Insider-Bedrohungen

**Eine Insider-Bedrohung** ist der Missbrauch von Zugriffsrechten durch einen aktuellen oder ehemaligen Mitarbeiter, Auftragnehmer oder Partner. Manche handeln absichtlich, weil sie Geld wollen oder verärgert sind. Andere handeln fahrlässig, etwa wenn sie Zugangsdaten in einem gemeinsam genutzten Dokument hinterlassen.

*Fahrlässige Insider kommen in Vorfallberichten häufiger vor als böswillige. Für beide gilt dieselbe Erkennungskontrolle: Vergleichen Sie Zugriffe mit einer rollenbezogenen Baseline.*

**Wo die Beweise liegen:** Volumen der Datenübertragungen, Aktivitäten außerhalb der üblichen Arbeitszeiten, Änderungen von Berechtigungen und Massendownloads aus sensiblen Repositories.

______

## DNS-Tunneling

**DNS-Tunneling** kodiert Daten in DNS-Abfragen und -Antworten. Fast jedes Netzwerk erlaubt DNS. Daher schleust diese Technik Daten an Kontrollen vorbei, die den Webverkehr prüfen sollen.

*Bei der Erkennung zählen Volumen und Form. Ein einzelner Host mit Tausenden Abfragen an eine Domain weicht deutlich von der normalen Baseline ab. Ungewöhnlich lange Subdomains deuten auf eine kodierte Nutzlast hin.*

**Wo die Beweise liegen:** DNS-Abfrageprotokolle, Abfragelänge und -volumen pro Host, ungewöhnliche Datensatztypen wie TXT und Anfragen an erst wenige Tage zuvor registrierte Domains.

______

## IoT-Angriffe

**Ein IoT-Angriff** zielt auf ein vernetztes Gerät wie eine Kamera, einen Drucker, ein Thermostat oder einen Sensor. Schwache Standardpasswörter und seltene Firmware-Updates machen solche Geräte zu einem häufigen Einstiegspunkt. Nach einer Kompromittierung tritt ein Gerät einem Botnetz bei, gibt Daten preis oder wird zum Zugang in das größere Netzwerk.

*Der Ausbau von 5G bringt viele vernetzte Geräte hinzu. Jedes neue Gerät ist ein weiteres Ziel mit einem langen Patch-Zyklus.*

**Wo die Beweise liegen:** Geräteinventar, Muster ausgehender Verbindungen, ungewöhnliche Datenübertragungen eines Geräts mit fester Aufgabe und abweichende Firmware-Versionen innerhalb einer Geräteflotte.

______

## KI-gestützte Angriffe

**KI-gestützte Angriffe** setzen maschinelles Lernen aufseiten des Angreifers ein.

| Technik | Verwendung |
|---|---|
| **Adversariale KI/ML** | Manipuliert Trainingsdaten oder Eingaben, um ein Modell irrezuführen |
| **Dark AI** | Setzt KI und maschinelles Lernen gezielt zum Ausnutzen von Schwachstellen ein |
| **Deepfake** | Erzeugt realistische gefälschte Audio-, Video- oder Bildinhalte |
| **KI-generiertes Social Engineering** | Führt überzeugende Chat- oder Sprachgespräche in großem Umfang |

*Ein Deepfake-Anruf oder ein flüssiger Phishing-Chat erhöht die Glaubwürdigkeit eines alten Tricks. Die zugrunde liegende Technik bleibt vertraut. Deshalb sind auf Verhalten beruhende Erkennungsfähigkeiten länger nützlich als Fähigkeiten, die an ein einzelnes Werkzeug gebunden sind.*

**Wo die Beweise liegen:** Herkunftssignale für Inhalte, Verifizierung über einen zweiten Kanal bei Geld- oder Zugriffsanfragen und Verhaltensanomalien bei Änderungen an Identitäten und Zahlungen.

______

## Angriffe der passenden Telemetrie zuordnen

Jede Kategorie speist eine andere Datenquelle. Die Tabelle ordnet sie einander zu und bietet einen Einstieg in die Erkennungsarbeit.

| Angriffstyp | Zentrale Telemetrie |
|---|---|
| **Malware** | EDR-Prozess-, Datei- und Registrierungsdaten |
| **Denial-of-Service** | Netzwerkfluss- und Verfügbarkeitsüberwachung |
| **Phishing** | E-Mail-Gateway- und URL-Analyseprotokolle |
| **Spoofing** | E-Mail-Authentifizierungs- und Netzwerkadressdaten |
| **Identitätsbasiert** | Anmelde- und Identitätsschutzprotokolle |
| **Code-Injection** | Webanwendungs- und Datenbankabfrageprotokolle |
| **Lieferkette** | Build-Pipeline und Abhängigkeitsinventar |
| **Social Engineering** | E-Mail-, Helpdesk- und Zutrittsprotokolle |
| **Insider-Bedrohung** | Datenzugriffs- und Übertragungsprotokolle |
| **DNS-Tunneling** | DNS-Abfrageprotokolle |
| **IoT** | Geräteinventar und ausgehende Netzwerkflüsse |
| **KI-gestützt** | Protokolle zu Identitäten, Zahlungen und Herkunft von Inhalten |

*Beginnen Sie die Erkennungsarbeit bei der Telemetriespalte. Eine nützliche Regel entsteht aus einer bekannten Datenquelle und einem bekannten Verhalten, nicht aus einem Werkzeugnamen.*

**Kategorien überschneiden sich während eines Vorfalls.** Eine Phishing-Nachricht kann zu gestohlenen Zugangsdaten, ausgeführter Malware und einem identitätsbasierten Eindringen führen. Kennzeichnen Sie die Technik des ersten Zugriffs und halten Sie spätere Verhaltensweisen getrennt fest. So entstehen aus einem Ereignis nicht vier voneinander unabhängige Warnmeldungen, und Ihre Untersuchung erhält eine klarere Zeitleiste.

______

## Üben Sie die Erkennung im Labor

Eine Kategorie bleibt abstrakt, bis Sie sie beobachten. In einem Heimlabor können Sie Aktivitäten erzeugen, Telemetriedaten sammeln und eine Warnmeldung mit dem Rohdatensatz vergleichen. Das [Karrierevideo zum Aufbau eines Security Operations Center](https://www.youtube.com/watch?v=s3g8o7Np1_g) zeigt den vollständigen Aufbau, mit dem Sie vor einer Einstellung Berufserfahrung sammeln.

{{< youtube id="s3g8o7Np1_g" >}}

Beginnen Sie mit der Identitätskategorie. Erstellen Sie einen Testbenutzer, aktivieren Sie die Anmeldeprotokollierung und führen Sie eine Reihe fehlgeschlagener und erfolgreicher Anmeldungen durch. Lesen Sie anschließend den Anmeldedatensatz und notieren Sie die Felder, die normale Nutzung von der Übung unterscheiden.

**Eine wiederholbare Übung:**

1. **Wählen Sie eine Kategorie** aus der Telemetrietabelle oben.
2. **Reproduzieren Sie eine harmlose Variante** der Aktivität auf Ihrem eigenen Testsystem oder -konto.
3. **Sammeln Sie die Telemetrie**, die bei der Kategorie entsteht.
4. **Formulieren Sie die Erkennungsidee** als Regel, gespeicherte Suche oder Abfrage.
5. **Testen Sie die Regel** mit der Übung und prüfen Sie, ob sie beim vorgesehenen Verhalten auslöst.
6. **Dokumentieren Sie die Grenzen** der Regel und die Aktivitäten, die sie übersieht.

Der [Microsoft-SOC-Home-Lab-Leitfaden](/articles/microsoft-soc-home-lab-2026/) beschreibt den Aufbau der Umgebung im Detail: Lizenzen, Netzwerksegmentierung, Protokollerfassung und Tests von Identitätskontrollen. Der [Mad-Hat-Cyber-Range-Leitfaden](https://madhat.io/pages/cyber-range-guide) erweitert dieselbe Idee um eine workshopgeeignete Umgebung mit Übungen zu Angriff, Erkennung und Abwehr.

Ordnen Sie das beobachtete Verhalten der passenden [MITRE-ATT&CK-Technik](https://attack.mitre.org/) zu, damit Sie eine einheitliche Begriffswelt verwenden. Betrachten Sie die Zuordnung als Hilfsmittel für Analysten und nicht als Attributionsbeweis. Bewahren Sie das Rohereignis, die Abfrage, die Regelversion und bekannte Erkennungslücken mit dem Übungsdatensatz auf.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Lesen Sie den Microsoft-SOC-Home-Lab-Leitfaden
{{< /centerbutton >}}

______

## Nächste Schritte

Beginnen Sie mit einer Kategorie und einer Übung. Nehmen Sie eine zweite Kategorie hinzu, nachdem Sie die erste abgeschlossen und dokumentiert haben. Ziel ist eine gründliche Untersuchung, keine Werkzeug-Checkliste.

- **[Microsoft-SOC-Home-Lab-Leitfaden](/articles/microsoft-soc-home-lab-2026/)** richtet die Umgebung für diese Übungen ein.
- **[Ein IT-Heimlabor aufbauen](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** beschreibt die Infrastruktur unter einem Sicherheitslabor.
- **[Tipps zum Schreiben eines IT-Lebenslaufs](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** zeigt, wie Sie ein dokumentiertes Labor als praktische Erfahrung darstellen.
- **[Die fünf wichtigsten Cyberangriffsvektoren und Gegenmaßnahmen](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** grenzt die Liste auf die am häufigsten beobachteten Vektoren ein.

**Quellenmaterial:** Die Angriffskategorien und ihre Untertypen folgen Kurt Bakers [Übersicht von CrowdStrike zu häufigen Cyberangriffen](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/). Produkt- und Referenzlinks verweisen auf Microsoft-Dokumentation.
