---
title: "OT-, ICS- und SPS-Cybersicherheit ist ein Problem, das die Industrie nicht ehrlich lösen kann"
draft: false
toc: true
date: 2026-06-26
description: "Eine professionelle Einschätzung, warum OT-, ICS- und SPS-Cybersicherheitsanleitungen mit dem tatsächlichen Problem nicht Schritt halten können. Die Systeme wurden nie für eine Absicherung ausgelegt. Compliance mit schriftlichen Standards ist nicht dasselbe wie Sicherheit."
tags: ["OT-Sicherheit", "ICS-Sicherheit", "SPS-Sicherheit", "IoT-Sicherheit", "industrielle Cybersicherheit", "SCADA-Sicherheit", "NIST 800-82", "IEC 62443", "NERC CIP", "Betriebstechnologie", "kritische Infrastruktur", "Analogsensoren", "Air Gap", "Legacy-Systeme", "Cybersicherheitsmeinung", "industrielle Steuerungssysteme", "SCADA", "Stuxnet", "Steuerungssystemsicherheit", "cyber-physische Sicherheit", "Lieferkettensicherheit", "OT-Lieferkette"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Eine Illustration, die einen Kontrast zwischen einer alten speicherprogrammierbaren Steuerung (SPS) mit Analogfunktionen auf einer Seite und einer modernen cybersicherheitsfähigen Steuerung mit digitalen Schnittstellen auf der anderen zeigt, vor dunklem Hintergrund."
coverCaption: ""
---

Ich habe genug Zeit in industriellen Umgebungen verbracht, um das offen zu sagen: **Die meisten OT-, ICS- und SPS-Cybersicherheitsprogramme sind Theater**. Sie produzieren Compliance-Dokumentation. Sie produzieren keine Sicherheit. Die Lücke zwischen beiden ist dort, wo kritische Infrastruktur getroffen wird.

Das ist kein Angriff auf die Menschen, die Standards schreiben. **NIST SP 800-82 Rev 3**, **IEC 62443** und **NERC CIP** sind technisch fundierte Dokumente. Das Problem ist nicht die Anleitung. *Das Problem ist, worauf die Anleitung angewendet wird.*

## Die Systeme wurden gebaut, um zu funktionieren, nicht um gesichert zu werden

**SPSen, SCADA-Systeme, verteilte Steuerungssysteme (DCS) und Legacy-Industrial-IoT-Hardware** wurden für eine einzige Sache entwickelt: zuverlässig sehr lange zu laufen. **Verfügbarkeit war das einzige Designziel, das es wert war, diskutiert zu werden.** Vertraulichkeit, Integrität, Authentifizierung und Protokollierung waren keine Anforderungen. In vielen Fällen waren sie nicht einmal Konzepte auf dem Tisch, als diese Systeme entwickelt wurden.

NIST SP 800-82 Rev 3 (2023) ist diesbezüglich ehrlich. Es beschreibt OT-Umgebungen als solche mit *"einzigartigen Leistungs-, Zuverlässigkeits- und Sicherheitsanforderungen"*, bei denen *"Sicherheit den Systembetrieb nicht beeinträchtigen darf."* Lesen Sie das nochmal. **Das primäre Sicherheitsleit-Dokument für Betriebstechnologie erkennt explizit an, dass Sicherheit an zweiter Stelle steht.** Das ist kein Fehler im Dokument. Es ist eine genaue Beschreibung der Umgebung.

Sie können keine rollenbasierte Zugangskontrolle auf eine SPS anwenden, die kein Konzept von Benutzerrollen hat. Sie können keine Firmware auf Hardware patchen, deren Hersteller nicht mehr existiert. **Legacy-Serienprotokolle, Modbus RTU und Profibus DP unter ihnen, bieten keine native Authentifizierung.** Sie übertragen Befehle und Daten an wen auch immer fragt. Es gibt keine Überprüfung, wer fragt.

*Die Anleitung ist solide. Die Systeme sind oft nicht in der Lage, sie zu empfangen.* Das sind nicht dieselben Probleme.

## Es gibt zwei vollständig unterschiedliche Kategorien von OT-Systemen

**Legacy-SPSen aus den 1980ern bis Anfang der 2000er Jahre** wurden für isolierten, nur physischen Betrieb entwickelt. Sie laufen auf proprietären Betriebssystemen. Sie werden oft von Ingenieur-Workstations verwaltet, die auch Unternehmensnetzwerke berühren. Ihre Konfigurationen werden in Formaten gespeichert, die keine Integritätsprüfung haben. Diese Systeme stellen einen erheblichen Teil der eingesetzten Infrastruktur in Wasseraufbereitung, Energieerzeugung, Fertigung und Transport dar.

**Moderne sicherheitsfähige Steuerungen sind anders.** Siemens, Schneider, Rockwell, Beckhoff und Phoenix Contact liefern jetzt Plattformen mit sicherem Boot, signierter Firmware, rollenbasierter Zugangskontrolle, TPM-gestützter Identität und verschlüsselter Kommunikation. EtherNet/IP CIP Security, PROFINET Security Class und OPC UA mit Authentifizierung existieren als Liefermerkmale auf aktueller Hardware.

Ich lehne moderne OT-Sicherheitstechnik nicht ab. Fortschritte sind real. **Das Problem ist, dass die meiste eingesetzte Basis nicht modern ist.** Wenn Menschen "OT-Cybersicherheit" sagen, beschreiben sie meistens jemanden, der versucht, eine 20 Jahre alte programmierbare Steuerung mit einem 2023 geschriebenen Cybersicherheitsrahmenwerk zu sichern. Das ist die Lücke, über die ich spreche.

## Was tatsächlich funktioniert

**Physische Sicherheit und Netzwerkisolierung sind die zuverlässigsten verfügbaren Kontrollen für Legacy-OT-Umgebungen.** Jedes große ICS-Sicherheitsrahmenwerk sagt dasselbe. IEC 62443 organisiert OT-Umgebungen in Sicherheitszonen mit definierten Leitungen. Die Absicht ist, laterale Bewegung durch kontrollierte Grenzen zu führen, statt über ein flaches Netzwerk zu gleiten.

Netzwerkisolierung reduziert die netzwerkbasierte Angriffsfläche erheblich. Sie eliminiert nicht alle Risiken. Wechselmedien, Insider-Zugang, Wartungs-Laptops, temporäre Ingenieurverbindungen und Lieferkettenangriffe stellen alle dokumentierte Eingangswege in Systeme ohne Netzwerkexposition dar. **Stuxnet**, das über infizierte USB-Sticks die luftgeschützte iranische Zentrifugenanlage erreichte, ist das kanonische Beispiel. *Netzwerkisolierung ist notwendig. Sie ist nicht ausreichend.*

**Menschlich-in-der-Schleife-Überwachung physischer Prozessparameter** bleibt einer der zuverlässigsten verfügbaren Erkennungsmechanismen. Ein ausgebildeter Bediener, der Druck, Temperatur und Fluss in Echtzeit beobachtet, wird Dinge bemerken, die kein Intrusion-Detection-System sehen wird, weil das IDS nicht überprüfen kann, ob der digitale Wert der physischen Realität entspricht.

Kontrollen, die Risiken im richtigen Kontext reduzieren:

- **Datendioden** erlauben Telemetrie nach außen, ohne eingehende Verbindungen zuzulassen
- **Anwendungs-Whitelisting** auf HMI-Workstations beschränkt, was auf Rechnern mit Zugang zu Steuerungssystemen ausgeführt wird
- **Passive Anomalie-Erkennungsplattformen** von Claroty, Dragos und Nozomi analysieren Datenverkehr ohne Steuerungspfad-Kommunikation zu berühren
- **Netzwerksegmentierung** zwischen OT-Zonen verlangsamt laterale Bewegung, ohne vollständige Air Gaps zu erfordern
- **Zero-Trust-Prinzipien**, auf die NIST SP 800-82 Rev 3 verweist, fügen einigen modernen OT-Architekturen Pro-Session-Verifizierungsanforderungen hinzu

*Keine davon löst die zugrundeliegenden Designbeschränkungen. Sie reduzieren Risiken an den Rändern von Systemen, die nie dafür gebaut wurden.*

## Analogsignale können nicht authentifiziert werden

**4-20mA-Stromschleifen, 0-10V-Signale, Thermoelementausgänge und RTD-Messwerte werden als variierende elektrische Signale übertragen.** Im physischen Signal gibt es keinen Mechanismus zur Verifikation der Authentizität. Wer das richtige Signal auf die Leitung legt, wird geglaubt.

Stuxnet hat das konkret gemacht. Der Angriff manipulierte SPS-Logik auf dem Siemens S7, während er gleichzeitig zuvor aufgezeichnete normale Prozessdaten an Bedienerschnittstellen zurückspielte. **Die Bediener schauten auf Bildschirme, die normale Messwerte zeigten, während die Zentrifugen über ihre Betriebsgrenzen hinaus angetrieben wurden.** Die Täuschung hielt lange genug an, um physischen Schaden zu verursachen, der als Geräteausfall und nicht als Angriff erschien.

Elektromagnetische Interferenzen von Stromkabeln, Frequenzumrichtern, Blitzen und unsachgemäßer Erdung korrumpieren Analogmessungen im normalen Betrieb. IEC 61000 existiert deswegen. Industrieinstallationen verwenden abgeschirmte Verkabelung, ordentliche Erdung, Filterung und physische Trennung, um damit umzugehen.

Moderne intelligente Feldgeräte wandeln Analogmessungen intern in digitale Form um, bevor sie über HART-IP, WirelessHART, EtherNet/IP CIP Security oder OPC UA übertragen werden. Für moderne Hardware sind authentifizierte digitale Kommunikation auf Geräteebene verfügbar. **Der analoge 4-20mA-Draht, der einen Legacy-Transmitter mit einem Legacy-SPS-Eingang verbindet, trägt keine Authentifizierung und wird es nie tun.** Für einen erheblichen Teil der eingesetzten Instrumentierung ist das noch der verwendete Draht.

## Sensorvalidierung ist eine Sicherheitskontrolle, keine Cybersicherheitskontrolle

Prozesstechnische Sicherheitssysteme führen **redundante Sensor-Abstimmung** durch. Eine 2-von-3-Anordnung mit zwei Sensoren, die 230 PSI lesen, und einem, der 14 PSI liest, kennzeichnet den Ausreißer. Dies bietet begrenzte Resilienz gegen Einzel-Sensor-Manipulation. *Es ist eine Sicherheits-Ingenieurs-Kontrolle, keine Cybersicherheitskontrolle.*

Standard-SPSen haben keine kryptografische Validierung für ihre Analogeingänge. Ein Signalgenerator, der auf die Schleife injiziert wird, ist vom legitimen Transmitter nicht zu unterscheiden. Die SPS liest den Strom und handelt entsprechend.

**Sicherheitsinstrumentierte Systeme sollten die unabhängige letzte Verteidigungslinie sein.** Im Jahr 2017 zielte **TRITON** (auch bekannt als **TRISIS**) auf Schneider Electric Triconex SIS-Einheiten mit dem spezifischen Ziel, diese Schicht zu deaktivieren. Die Angreifer erreichten das Sicherheitssystem über das Ingenieur-Workstation-Netzwerk. *Die Unabhängigkeit der Schicht hing von Netzwerktrennung ab, die nicht aufrechterhalten worden war.*

IEC 62443-3-3, IEC 62443-4-2 und die Koordination mit funktionaler Sicherheit unter IEC 61511 spiegeln diese Lektion jetzt wider. **TRITON hat in der Praxis demonstriert, was unabhängige Analyse in der Theorie argumentiert hatte:** Ein Angreifer, der das Sicherheitssystem neutralisiert, bevor er den Gefahrenzustand auslöst, entfernt die letzte Kontrolle, die physische Konsequenzen verhindert.

## Ihre Lieferkette ist der Vektor, den Sie wahrscheinlich ignorieren

**Die meisten OT-Sicherheitsprogramme konzentrieren sich auf Netzwerkarchitektur. Die meisten OT-Kompromittierungen in den letzten Jahren haben Eingangspunkte genutzt, die Netzwerkarchitektur nicht stoppt.**

OT-Lieferketten-Risiken umfassen:

- **Firmware-Integrität vor der Installation** — ob Hardware mit nicht verifizierter Firmware aus der Fabrik oder dem Händler ankommt
- **Remote-Access-Sitzungen von Anbietern**, die als dauerhafte Exposition an Standorten verbleiben, die auf Herstellerunterstützung angewiesen sind
- **Ingenieur-Workstations**, die sowohl mit dem Unternehmensnetzwerk als auch dem OT-Netzwerk verbunden sind, oft wegen betrieblicher Bequemlichkeit
- Das Fehlen von **Software-Stücklisten (SBOMs)** für die meisten Legacy-OT-Deployments, was Software-Komponenten-Tracking weitgehend unmöglich macht
- **Wartungsunternehmer**, die Laptops und USB-Sticks in betrieblich isolierte Umgebungen einbringen
- **Signierter Firmware-Update-Support**, den die meisten älteren Plattformen nicht haben

*Wenn Sie intern einen Air Gap haben, Ihr Gerätehersteller aber ein dauerhaftes Remote-Access-Portal in Ihr Ingenieursnetzwerk aufrechterhält, haben Sie keinen Air Gap. Sie haben eine Lücke mit einer Tür darin, die jemand anderes kontrolliert.*

## Legacy-Systeme zu härten kostet mehr als es sollte

Jedes SPS-Programm ist speziell für einen bestimmten Prozess geschrieben. Die Logik, die das Druckstoßkontrollsystem einer Raffinerie betreibt, unterscheidet sich vollständig von der Logik, die eine Wasseraufbereitungschlorsierungssequenz oder einen Turbinengouverneur betreibt. Das ist keine Wahl. Physische Prozesse sind unterschiedlich.

**Das Härten von Legacy-OT-Systemen kostet häufig mehr als erwartet** wegen der Ingenieurvalidierungsanforderungen, notwendiger Ausfallzeiten, Anbietersupporteinschränkungen, Dokumentationslücken und Testzyklen, die die anfänglichen Schätzungen überschreiten. In einigen Fällen mit Hardware ohne Anbietersupport nähern sich die Härtungskosten den Austauschkosten des Systems oder überschreiten sie.

**NERC CIP-Compliance für Massenelektriksystem-Cyber-Assets kostet einzelne Versorgungsunternehmen Millionen Dollar pro Jahr.** Eine Befragung von 2019 der American Public Power Association dokumentierte Compliance-Kosten in einem weiten Bereich, wobei kleinere Versorgungsunternehmen unverhältnismäßige Belastungen im Verhältnis zu ihrer Größe berichteten. Viele Wassersysteme und kleinere Versorgungsunternehmen fallen außerhalb der NERC CIP-Anforderungen und haben keine vergleichbare Compliance-Verpflichtung.

## Die Systeme sollten ersetzt werden

**Das Ersetzen von Legacy-OT-Systemen ist die richtige Antwort.** Bei großen Anlagen bedeutet das Zehnmillionen Dollars, verlängerte Übergangszeiten und das Risiko, komplexes Betriebswissen während der Migration falsch zu kodieren. Das sind reale Kosten und reale Risiken.

Was Industrieleitlinien tatsächlich empfehlen, durch CISA und ICS-CERT, ist das Anwenden kompensierender Kontrollen, während die Ersatzplanung voranschreitet. Das ist eine rationale Reaktion auf die Einschränkungen. *Einfach erklärt: Es erkennt an, dass vollständige Sicherheit auf Legacy-Ausrüstung nicht erreichbar ist, also werden die Kontrollen angewendet, die passen, und eine eventuelle Ersetzung geplant.*

**Die praktische Realität ist, dass viele dieser Systeme für Jahrzehnte in Betrieb bleiben werden.** Das ist ein Finanzierungs- und Politikproblem. Die technische Gemeinschaft war klar darüber, was zu tun ist. Die Betriebsbudgets und Ersatzpläne haben nicht Schritt gehalten.

## Netzwerkkonnektivität zu OT-Systemen hinzuzufügen macht Dinge oft schlimmer

Viele Organisationen haben Remote-Zugang und Überwachungsfähigkeiten zu OT-Umgebungen hinzugefügt, die ursprünglich isoliert waren. Das operative Argument ist unkompliziert: Fernüberwachung reduziert die Reaktionszeit, und Anbietersupport ist mit einer Remote-Verbindung schneller. **Die Sicherheitskonsequenz ist, dass isolierte Systeme ohne Remote-Angriffsfläche jetzt eine haben.**

Der **Wasseraufbereitungsvorfall von Oldsmar 2021** geschah über eine TeamViewer-Remote-Zugriffsverbindung. Der Angreifer änderte die Natronlaugedosierungseinstellungen über ein legitimes, für Bequemlichkeit hinzugefügtes Remote-Access-Tool. Der **Colonial-Pipeline-Vorfall von 2021** begann mit einer IT-Netzwerkkompromittierung. Der Betreiber schaltete OT-Pipeline-Operationen proaktiv ab, weil er nicht bestätigen konnte, dass das OT-Netzwerk nicht betroffen war. *Der Angriff durchbrach das OT-Netzwerk nicht direkt. Die Unsicherheit darüber, ob er es hatte, verursachte den Shutdown.*

Das Hinzufügen von Netzwerkkonnektivität zu Legacy-OT-Systemen aus operativem Nutzen heraus, ohne diese Konnektivität auf geeignete Standards zu konstruieren, **produziert in vielen Fällen mehr Risiko als der Nutzen rechtfertigt**.

## Compliance mit schriftlichen Standards ist nicht Sicherheit

NIST SP 800-82 Rev 3, IEC 62443 und NERC CIP beschreiben die richtigen Kontrollen für das, was diese Systeme sind. Ich lehne sie nicht ab. Ich weise darauf hin, was sie explizit sagen: **Nicht jedes OT-System kann jede Kontrolle implementieren.** Die Rahmenwerke verwenden abgestufte Sicherheitsstufen und kompensierende Kontrollbestimmungen genau deswegen, weil die Systeme, auf die sie angewendet werden, häufig die vollen Anforderungen nicht erfüllen können.

Die Lücke zwischen dem, was die Standards beschreiben, und was ein bestimmtes Legacy-Deployment erreichen kann, ist kein Dokumentationsfehler. Die Systeme unterstützen die Kontrollen nicht. Die Anleitung erkennt das an. **Ein konformes Audit-Ergebnis bei Legacy-OT zu erreichen bedeutet nicht, dass die Umgebung sicher ist.** Es bedeutet, dass Sie dokumentiert haben, welche kompensierenden Kontrollen vorhanden sind, und ein Prüfer hat sie akzeptiert.

**Wenn jemand Ihnen sagt, dass das Erfüllen von Compliance-Anforderungen Ihre OT-Umgebung sicher macht, sagen sie etwas, das die Rahmenwerke, auf die sie sich beziehen, nicht unterstützen.**

## Was Sie mit Legacy-OT tun sollten

Wenn Sie Legacy-OT-Umgebungen betreiben:

- **Behandeln Sie Netzwerkisolierung als Ihre primäre Kontrolle** und auditieren Sie alles, was die OT-Grenze überquert
- **Geben Sie Ihren Ingenieur-Workstations einen eigenen Härtungsplan.** Sie berühren beide Welten und sind häufig der Eingangspunkt
- **Kontrollieren und protokollieren Sie alle Wechselmedien** in OT-Bereichen
- **Auditieren Sie Anbieter-Remote-Zugang** und schließen Sie jede Sitzung, die nicht aktiv genutzt wird
- Implementieren Sie redundante Sensorüberwachung, wo das Prozessdesign es erlaubt
- **Erstellen Sie einen Ersatzplan mit echten Kostenschätzungen**, auch wenn der Ersatz Jahre entfernt ist
- **Hören Sie auf, Compliance-Audit-Abschluss als Sicherheitsmeilenstein zu behandeln**

Wenn Sie neue OT-Systeme beschaffen:

- **Schreiben Sie Sicherheitsanforderungen in die Beschaffungsspezifikation**, bevor Anbieter antworten
- Wählen Sie Plattformen mit dokumentierter Unterstützung für authentifizierte Kommunikation, signierte Firmware-Updates und rollenbasierte Zugangskontrolle
- **Gestalten Sie IT/OT-Grenzen als explizite Leitungen gemäß IEC 62443**, nicht als vage "halte sie getrennt"-Politik
- **Verlangen Sie SBOMs für OT-Softwarekomponenten** als Vertragslieferung

Die Industrie hat das Problem gut dokumentiert. Die Standards sind technisch genau. *Die Systeme im Feld können häufig nicht empfangen, was die Standards vorschreiben.* Das offen anzuerkennen ist der Ausgangspunkt für Entscheidungen darüber, wie das verbleibende Risiko gemanagt werden soll.

## Referenzen

- NIST SP 800-82 Rev 3: Guide to Operational Technology (OT) Security (2023)
- IEC 62443: Industrial Automation and Control Systems Security series
- IEC 62443-3-3: System security requirements and security levels
- IEC 62443-4-2: Technical security requirements for IACS components
- IEC 61511: Functional Safety for Safety Instrumented Systems
- NERC CIP: Critical Infrastructure Protection standards for the bulk electric system
- IEC 61000: Electromagnetic Compatibility standards
- CISA ICS-CERT Advisories and Best Practices
- MITRE ATT&CK for ICS framework
- Stuxnet technical analysis, Langner Communications, 2011
- TRITON/TRISIS technical analysis, Dragos, 2017
- Oldsmar Water Treatment incident review, CISA, 2021
- American Public Power Association NERC CIP Compliance Cost Survey, 2019
