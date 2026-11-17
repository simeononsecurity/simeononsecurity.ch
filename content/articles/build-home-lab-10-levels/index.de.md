---
title: "Ein Homelab in 10 Stufen aufbauen, von Pi-hole bis lokaler KI"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Baue ein Homelab in zehn praktischen Stufen auf, von netzwerkweiter DNS-Filterung bis lokaler KI, mit Hardware, Kosten, Fähigkeiten und Kompromissen pro Stufe."
genre: ["Homelab", "Self-Hosting", "Lokale KI", "Heimnetzwerke"]
tags: ["Homelab", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "lokale KI", "Stromverbrauch"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Ein Homelab wächst von einem kleinen Raspberry Pi und Router zu Speicher, Servern, Netzwerkausrüstung und einem lokalen KI-Arbeitsplatz."
coverCaption: ""
---

Ein Homelab in 10 Stufen aufbauen, von Pi-hole bis lokaler KI
=============================================================

Ein **Homelab** ist eine Sammlung von Computern und Diensten, die du selbst betreibst, um alltägliche Probleme zu lösen und den Betrieb echter Systeme zu lernen. Du kannst Werbung blockieren, Licht automatisieren, Familienmedien speichern oder virtuelle Maschinen testen. **Beginne mit einer nützlichen Aufgabe.** Ergänze Hardware, wenn eine echte Grenze auftritt.

Dieser Leitfaden führt von einem kleinen Raspberry Pi mit Pi-hole bis zu einem Server mit lokalen KI-Modellen. **Jede Stufe erweitert die Möglichkeiten und bringt neue Verantwortung.** Die Kostenschätzungen beruhen auf einem beispielhaften Stromverbrauch und einem Strompreis von $0.15 pro Kilowattstunde. Prüfe deinen örtlichen Tarif und miss deine Geräte, bevor du mehr kaufst.

## Stufe 1: Werbung im gesamten Heimnetz blockieren

Installiere [Pi-hole](https://docs.pi-hole.net/) auf einem Raspberry Pi oder einem anderen kleinen Linux-Computer. Pi-hole arbeitet als **DNS-Sinkhole**. Fragt ein Gerät die Adresse einer Domain auf einer Sperrliste ab, liefert Pi-hole kein nutzbares Ziel zurück. Browser, Telefon und Smart-TV verwenden denselben Filter, wenn dein Router oder DHCP-Server die Clients auf Pi-hole verweist.

**DNS-Filterung** wirkt auch außerhalb von Webbrowsern, etwa bei manchen Anzeigen in Apps und vernetzten Fernsehern. Inhalte innerhalb einer Seite bleiben ungefiltert. Anzeigen, die von derselben Domain wie eine Website oder App stammen, werden daher durchgelassen. Eine Sperrliste verhindert manchmal, dass eine Anmeldung, ein Video oder ein Bezahlvorgang lädt. Prüfe das Abfrageprotokoll von Pi-hole, erlaube bei Bedarf die betreffende Domain und halte für einen Ausfall einen alternativen DNS-Plan bereit.

Der Stromverbrauch ist gering. Für ein Gerät mit 8 Watt, das einen ganzen Monat läuft, lautet die Schätzung: 8 W × 24 Stunden × 30 Tage ÷ 1.000 × $0.15 = **etwa $0.86 pro Monat**. Miss das komplette Netzteil an der Steckdose. Ein zweiter Computer, USB-Laufwerk oder ineffizienter Adapter verändert den Gesamtwert.

**Du lernst:** DNS, DHCP, Sperrlisten und grundlegende Linux-Wartung.

## Stufe 2: Smartgeräte lokal automatisieren

Ergänze [Home Assistant](https://www.home-assistant.io/). Das System bündelt kompatible Smartgeräte und Automatisierungen. Plane, dass das Licht zur Schlafenszeit ausgeht. Schalte einen Ventilator ein, wenn ein Temperatursensor einen Sollwert überschreitet. Lass dich benachrichtigen, wenn ein Lecksensor Wasser erkennt. **Diese kleinen Automatisierungen bringen sofort einen Nutzen.**

**Lokale Steuerung** hält viele Automatisierungen in deinem Zuhause am Laufen, wenn ein externer Dienst oder die Internetverbindung ausfällt. Das Verhalten hängt vom Gerät ab. Einige Produkte benötigen für die Einrichtung und Fernfunktionen weiterhin ein Herstellerkonto, einen Clouddienst oder eine Internetverbindung. Prüfe vor dem Kauf die Anforderungen der Integration.

**Sichere Home Assistant** und bewahre eine Kopie außerhalb des Hosts auf. Dokumentiere Integrationen und Wiederherstellungsschritte. Eine defekte SD-Karte oder ein ausgefallener Mini-PC sollte deine Konfiguration nicht löschen.

**Du lernst:** Geräteintegrationen, Auslöser, Bedingungen und die Wiederherstellung aus Backups.

## Stufe 3: Mehrere Dienste auf einem Mini-PC betreiben

Ein **gebrauchter Business-Mini-PC** bietet oft erweiterbaren Arbeitsspeicher, austauschbaren Speicher und nützliche Anschlüsse zu einem niedrigen Gebrauchtpreis. Ein Mini-PC mit Intel N100 verbraucht oft weniger Strom und benötigt wenig Platz. Intel beschreibt den N100 als Prozessor mit vier Kernen, vier Threads, einer TDP von 6 Watt und Unterstützung für bis zu 16 GB Arbeitsspeicher. Die Prozessorangabe entspricht nicht dem Stromverbrauch des gesamten Systems an der Steckdose. Vergleiche den konkreten Computer, Arbeitsspeicher, Speicher, Garantie und Netzwerkanschlüsse.

Installiere Linux und verwende [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/), um getrennte Dienste als **Container** auszuführen. Ein Container bündelt eine Anwendung und ihre Abhängigkeiten, teilt aber den Kernel des Hostbetriebssystems. Du kannst etwa einen Passwortmanager wie das von der Community gepflegte Projekt Vaultwarden und einen Verfügbarkeitsmonitor wie Uptime Kuma betreiben. **Behandle den Passwortmanager als sensiblen Dienst:** Begrenze den Zugriff, nutze starke Authentifizierung, installiere Updates und bewahre ein verschlüsseltes Backup auf.

**Container ersetzen weder Updates noch Backups.** Lege für jeden Dienst einen festen Speicherort fest und dokumentiere die Wiederherstellung. Auch ein kleiner Mini-PC hat Grenzen. Mehrere Datenbanken, Medienkonvertierungen oder große Anwendungen können Arbeitsspeicher, Speicherplatz oder CPU-Zeit aufbrauchen.

**Du lernst:** Linux-Administration, Container, Volumes, Updates und die Wiederherstellung von Diensten.

## Stufe 4: Eine Medienbibliothek zu Hause aufbauen

[Jellyfin](https://jellyfin.org/docs/) ist ein Open-Source-Medienserver. [Plex](https://support.plex.tv/) bietet ein ausgereiftes Client-Ökosystem und optionale kontobasierte Funktionen. Beide ordnen persönliche Bibliotheken und streamen Medien an unterstützte Clients. **Wähle nach deinen Clients**, dem Fernzugriffsmodell, der Hardwareunterstützung und den benötigten Funktionen.

**Dein Speicherbedarf** hängt von Größe und Qualität der Sammlung ab. Beginne nur dann mit einem einzelnen Laufwerk, wenn du bereits einen separaten Backupplan hast. Verwende einheitliche Ordnernamen und Metadaten, damit der Server Filme und Folgen korrekt zuordnet.

**Direktwiedergabe** sendet eine kompatible Datei an den Client, ohne den Videostream zu ändern. **Transkodierung** wandelt Audio oder Video um, wenn Client, Verbindung, Untertitel oder Qualitätseinstellung ein anderes Format erfordern. Transkodierung belastet den Server zusätzlich. Teste deine Geräte und dein Netzwerk, bevor du eine GPU oder eine stärkere CPU kaufst. **Lass einen eigenen Medienserver weg**, wenn alle Clients deine Dateien direkt abspielen und ein Host ausreicht.

**Du lernst:** Medienformate, Speicherplanung, Netzwerkdurchsatz und Lasttests.

## Stufe 5: Speicherredundanz und ein separates Backup ergänzen

Ein NAS mit zwei Laufwerken und **gespiegeltem Speicher** schreibt Daten auf beide Laufwerke. Fällt eines aus, enthält das andere eine aktuelle Kopie, während du das defekte Laufwerk ersetzt und den Spiegel neu aufbaust. Spiegelung sichert die Verfügbarkeit bei einem Laufwerksausfall. **Ein Spiegel stellt keine** gelöschte Datei wieder her, macht keine Ransomware-Verschlüsselung rückgängig und schützt nicht vor Diebstahl, Feuer oder einem Stromereignis, das beide Laufwerke beschädigt.

Bewahre ein **separates Backup** auf einem anderen Gerät oder an einem anderen Standort auf. Sichere wichtige Dokumente, Fotos, Konfigurationsexporte und Dienstdaten. Nutze einen Backupplan und bewahre Versionen auf, damit versehentliche Änderungen nicht alle intakten Kopien überschreiben.

**Teste eine Wiederherstellung.** Wähle einige Dateien aus, stelle sie in einem separaten Ordner wieder her und öffne sie. Stelle bei einem Dienst dessen Daten in einer Testinstanz wieder her oder dokumentiere die Schritte und prüfe jede Datei. Ein Backup, das du nie wiederhergestellt hast, ist eine Annahme und kein Wiederherstellungsplan.

**Du lernst:** Dateisysteme, Laufwerktausch, Backuprotation und Wiederherstellungstests.

## Stufe 6: Virtualisierung mit einem kleinen Proxmox-Cluster lernen

[Proxmox VE](https://pve.proxmox.com/pve-docs/) betreibt virtuelle Maschinen und Container auf Serverhardware. Mehrere Mini-PCs in einem **Cluster** bieten eine gemeinsame Verwaltungsansicht und Gelegenheit, Nodes, Speicher und Migration kennenzulernen. Ein Cluster ist eine Gruppe von Servern, die für die Zusammenarbeit eingerichtet wurden. Ihre Mitglieder fassen den Arbeitsspeicher nicht zu einem großen Pool zusammen. **Hohe Verfügbarkeit erfordert** zusätzliche Planung und geeigneten gemeinsamen oder replizierten Speicher.

Ein **Snapshot** hält den Zustand einer virtuellen Maschine zu einem bestimmten Zeitpunkt fest. So kannst du nach einer Änderung im Lab zu einem früheren Zustand zurückkehren. Snapshots hängen meist vom ursprünglichen Speicher ab. Sie sind keine unabhängigen Backups. **Kopiere wichtige Daten auf ein separates Backupziel** und teste die Wiederherstellung.

Jeder Node erhöht Stromverbrauch, Zahl der Netzwerkanschlüsse und Kabel sowie den Updateaufwand. Drei kleine Computer bedeuten auch drei Systeme, die du patchen und untersuchen musst. Ein einzelner Mini-PC mit einigen virtuellen Maschinen vermittelt viele Grundlagen zu geringeren Kosten. **Füge Nodes hinzu, wenn** Experimente Isolation erfordern oder du Clusterbetrieb üben willst.

**Du lernst:** virtuelle Maschinen, Speicherpools, Snapshots, Clusterzugehörigkeit und Node-Wartung.

## Stufe 7: Privaten Fernzugriff und Netztrennung ergänzen

[Tailscale](https://tailscale.com/kb/) verbindet deine zugelassenen Geräte über ein privates Netzwerk. So erreichst du unterwegs ausgewählte Dienste zu Hause. **Beschränke den Zugriff** auf die Geräte und Dienste, die jede Person benötigt. Schütze Konten mit Mehr-Faktor-Authentifizierung und prüfe alte Geräte und Schlüssel.

Ein verwaltbarer Switch oder Router mit **VLAN-Unterstützung** trennt Gerätegruppen. Platziere smarte Steckdosen und andere Geräte mit geringem Vertrauensniveau in einem anderen Netzwerk als Computer mit persönlichen Dateien. Lege Speicher in ein Netzwerk, das nur Systeme mit Zugriffsbedarf erreichen. Segmentierung begrenzt, welche Geräte miteinander kommunizieren. Halte auch Updates, starke Passwörter und Zugriffsregeln ein.

**Setze Admin-Oberflächen nicht direkt dem öffentlichen Internet aus**, es sei denn, du kennst die Authentifizierungs-, Patch- und Firewallanforderungen des Dienstes. Auch ein privates Zugriffswerkzeug braucht sorgfältige Konto- und Gerätekontrolle.

**Du lernst:** privaten Zugriff, identitätsbasierte Berechtigungen, VLANs, Firewallregeln und Vertrauensgrenzen für Geräte.

## Stufe 8: Einen Enterprise-Server ergänzen

Wechsle zu einem größeren Server, wenn du nachweislich mehr CPU-Kerne, Arbeitsspeicher, Laufwerksschächte, PCIe-Steckplätze oder Netzwerkkapazität brauchst. Ältere Enterprise-Server kosten gebraucht oft weniger, doch ihre Lüfter sind laut und **die Leerlaufleistung liegt je nach Modell und installierten Teilen bei etwa 100 bis 160 Watt**. Behandle diese Spanne als Schätzung, nicht als Spezifikation.

Berechne vor dem Kauf die jährlichen Stromkosten:

`gemessene Watt ÷ 1.000 × 24 × 365 × Strompreis pro kWh`

Bei 120 Watt und $0.15 pro kWh beträgt die Schätzung 1.051 kWh im Jahr oder etwa **$158 pro Jahr**. Miss den konkreten Server im Leerlauf und bei typischer Auslastung. Berücksichtige Laufwerke, Kühlung und USV.

Prüfe Gehäusetiefe, Laufwerkskompatibilität, Lautstärke, Lüftersteuerung, Netzteil und Erweiterungskarten. Ein Server, der dein Platz- oder Strombudget überschreitet, ist kein praktisches Upgrade.

**Du lernst:** Serverhardware, Fernverwaltung, Erweiterung, Kühlung und Schätzungen der Betriebskosten.

## Stufe 9: Strom messen und das Lab passend dimensionieren

Miss jeden Computer mit einem **Steckdosen-Energiekostenmessgerät** im Leerlauf und während normaler Arbeit. Liste die größten Verbraucher auf. Prüfe die Energieeinstellungen im BIOS, entferne ungenutzte Karten und Laufwerke und verlagere Alltagsdienste zurück auf effiziente Mini-PCs, wenn Enterprise-Hardware unnötig ist.

Betreibe den großen Server nur, wenn eine Arbeitslast seine Kapazität benötigt. Wenn du einen Wake-on-LAN-Zeitplan oder Fernsteuerung der Stromversorgung nutzt, dokumentiere die Wiederherstellung bei Netzwerk- oder Stromausfällen. Führe eine **Liste der Dienstabhängigkeiten**, damit ein Herunterfahren nicht Speicher oder Netzwerk unterbricht, die andere Systeme benötigen.

Ein Rack ordnet Geräte und Luftstrom, wenn Rackhardware den Platz rechtfertigt. Eine USV überbrückt kurze Stromausfälle und gibt Systemen Zeit für ein sauberes Herunterfahren. Beides kostet Anschaffung, Platz und laufend Strom. **Miss den Verbrauch** und rechne den Batteriewechsel in das langfristige Budget ein.

**Du lernst:** Energiemessung, Energiemanagement, Zuordnung von Abhängigkeiten und Kapazitätsplanung.

## Stufe 10: KI-Modelle lokal ausführen

[Ollama](https://docs.ollama.com/) lädt unterstützte Sprachmodelle herunter und führt sie auf deinem Computer aus. **Lokale Inferenz** hält Prompts und Antworten auf Hardware, die du kontrollierst, wenn du ein lokales Modell und eine lokale Anwendung verwendest. Prüfe, ob der gesamte Softwarepfad lokal bleibt. Eine verbundene Anwendung, Telemetriefunktion oder Cloudmodelloption sendet Daten aus deinem Netzwerk.

Die Hardwareanforderungen hängen von Modellgröße, Quantisierung, Kontextlänge und gewünschter Geschwindigkeit ab. **Systemspeicher oder GPU-Speicher muss** Modellgewichte und Arbeitskontext aufnehmen. Kleine Computer führen kleinere Modelle aus. Größere Modelle und längere Kontexte erfordern mehr Speicher und oft eine leistungsfähige GPU. Miss den Stromverbrauch während der Inferenz. Ein System mit GPU verbraucht oft deutlich mehr Strom als ein Mini-PC im Leerlauf.

Lokale Modelle eignen sich für Aufgaben wie Entwürfe, Zusammenfassungen privater Notizen und einfache Klassifizierung, wenn ihre Qualität deinen Anforderungen entspricht. Sie liefern falsche Antworten, und kleinere Modelle haben oft Schwierigkeiten mit komplexem Schlussfolgern oder aktuellen Fakten. Cloudmodelle schneiden bei bestimmten Aufgaben manchmal besser ab. **Vergleiche Qualität, Datenschutz, Latenz, Kosten und Stromverbrauch**, bevor du entscheidest, wo eine Arbeitslast läuft.

**Du lernst:** Modellspeicher, Quantisierung, Inferenz, Datenschutzgrenzen und Bewertung von Arbeitslasten.

## Die zehn Stufen vergleichen

**Kosten sind Schätzungen, keine Angebote.** Hardwarepreise unterscheiden sich je nach Region, Zustand und Speicherkonfiguration. Schätze die Stromkosten mit `Watt ÷ 1.000 × Stunden × Tage × Preis pro kWh`. Miss möglichst an der Steckdose und rechne Leerlaufstunden ein, da viele Heimserver rund um die Uhr laufen.

### Fähigkeiten und Hardware

| Stufe | Neue Fähigkeit | Typische Hardware |
|---|---|---|
| **1** | DNS-Filterung im Netzwerk | Raspberry Pi oder kleiner Linux-Host |
| **2** | Lokale Geräteautomatisierung | Pi oder Mini-PC, kompatible Geräte |
| **3** | Mehrere selbst gehostete Apps | Gebrauchter Business-Mini-PC oder N100-System |
| **4** | Persönliches Medienstreaming | Mini-PC plus Medienspeicher |
| **5** | Toleranz bei Laufwerksausfall und Wiederherstellung | NAS mit zwei Laufwerken plus separates Backup |
| **6** | Virtuelles Serverlab | Mindestens zwei Mini-PCs |
| **7** | Privater Zugriff und Segmentierung | Tailscale, verwalteter Router oder Switch |
| **8** | Hohe Kapazität und Erweiterbarkeit | Enterprise-Server |
| **9** | Geringerer Energieverbrauch des Labs | Strommessgerät, optimierte Systeme |
| **10** | Lokale Modellinferenz | PC mit viel Speicher, optionale GPU |

### Fähigkeiten, Kosten und Kompromisse

| Stufe | Gelernte Fähigkeiten | Laufende Kostenschätzung | Wichtigster Kompromiss |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Etwa $1/Monat bei 8 W und $0.15/kWh | Einige Anzeigen bleiben, Fehlblockierungen müssen geprüft werden |
| **2** | Integrationen, Auslöser, Backups | Hoststrom plus Gerätekosten | Kompatibilität und Backupaufwand |
| **3** | Docker, Updates, Speicher | Abhängig vom gemessenen Systemverbrauch | CPU-, Speicher- und Laufwerksgrenzen |
| **4** | Formate, Organisation, Transkodierung | Speicher und Serverstrom | Transkodierung braucht manchmal stärkere Hardware |
| **5** | Spiegelung, Aufbewahrung, Wiederherstellung | NAS-Strom, Laufwerke, Backupziel | Ein Spiegel ist kein Backup |
| **6** | Proxmox, VMs, Cluster | Jeder Node erhöht Stromverbrauch und Aufwand | Mehr Nodes bedeuten mehr Wartung |
| **7** | Zugriffsregeln, VLANs, Firewall | Netzwerkgeräte und Dienstkosten | Fehlkonfigurierte Regeln legen Dienste offen |
| **8** | Hardware, Kühlung, Fernverwaltung | Je nach Server, anhand des Messwerts berechnen | Lärm, Wärme und Leerlaufleistung |
| **9** | Messung, Zeitplanung, Dimensionierung | Einmalige Messgeräte, Ersparnis variiert | Zeitpläne ergänzen Betriebsschritte |
| **10** | Modelle bereitstellen und bewerten | Rechenstrom und Speicher | Qualität und Geschwindigkeit hängen von Hardware ab |

## Das nächste sinnvolle Upgrade wählen

**Höre auf der Stufe auf, die deinen aktuellen Bedarf deckt.** Pi-hole und ein Mini-PC reichen möglicherweise für deine Dienste. Ein NAS ist sinnvoll, wenn du gemeinsamen Speicher und einen getesteten Wiederherstellungsplan brauchst. Ergänze Cluster oder Enterprise-Server, wenn eine Arbeitslast oder ein Lernziel das rechtfertigt.

Notiere **den Datenspeicherort jedes Dienstes, den Updateprozess und die Wiederherstellungsschritte.** Teste Backups, bevor du weitere Geräte hinzufügst. Lass dich beim nächsten Kauf von der nächsten echten Einschränkung leiten.

## Quellen

- [Pi-hole-Dokumentation](https://docs.pi-hole.net/)
- [Home-Assistant-Dokumentation](https://www.home-assistant.io/docs/)
- [Technische Daten des Intel Processor N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: Was ist ein Container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Jellyfin-Dokumentation](https://jellyfin.org/docs/)
- [Plex-Support](https://support.plex.tv/)
- [Proxmox-VE-Dokumentation](https://pve.proxmox.com/pve-docs/)
- [Tailscale-Dokumentation](https://tailscale.com/kb/)
- [Ollama-Dokumentation](https://docs.ollama.com/)
