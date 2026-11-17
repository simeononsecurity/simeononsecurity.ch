---
title: "USV für das Homelab dimensionieren und automatische Abschaltung testen"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Messen Sie die Leistungsaufnahme im Homelab, vergleichen Sie die Watt- und VA-Grenzen einer USV, prüfen Sie die Laufzeit bei Ihrer Last und testen Sie eine saubere Abschaltung, bevor Sie sich auf die Batterie verlassen."
genre: ["Heimlabor", "Stromversorgungsschutz", "Systemadministration"]
tags: ["Homelab-USV", "USV dimensionieren", "USV-Laufzeit", "automatische Abschaltung", "Network UPS Tools", "USV-Watt", "USV-VA", "Leistungsfaktor", "Batteriepuffer", "Serverabschaltung", "NAS-Abschaltung", "Stromausfall", "USV-Test", "Laufzeitkurve", "Leistungsmessgerät", "USV-Überwachung", "Batteriewechsel", "Überspannungsschutz", "geordnete Abschaltung", "Homelab-Stromversorgung"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Eine USV im Homelab versorgt Server, NAS, Router und Switch über einer Zeitleiste vom Stromausfall bis zur Abschaltung."
coverCaption: "Messen Sie die Last, prüfen Sie die Laufzeit und testen Sie die Abschaltung vor einem Stromausfall."
---

Eine **USV** (unterbrechungsfreie Stromversorgung) verschafft einem Homelab bei einem Stromausfall Zeit, Arbeit zu speichern und Systeme herunterzufahren. Das Typenschild sagt allein nicht, wie lange Ihre Server laufen. Sie benötigen die Last der Geräte, die Watt- und VA-Grenzen der USV, eine Laufzeitschätzung für diese Last und einen getesteten Abschaltweg.

## Wichtigste Punkte

- **Messen Sie die Last:** Notieren Sie normale und hohe Wattwerte für jedes Gerät, das an der Batterie bleiben soll.
- **Prüfen Sie beide Nennwerte:** Die USV muss die Watt- und VA-Anforderungen der angeschlossenen Geräte erfüllen.
- **Lesen Sie die Laufzeitkurve:** Die Laufzeit hängt von Last und Batteriezustand ab. Verwenden Sie eine modellspezifische Schätzung.
- **Testen Sie den Abschaltweg:** Prüfen Sie, ob das USV-Signal jeden Host erreicht und die Hosts anhalten, bevor die Batterie leer ist.

## Vor dem Start

Sie benötigen ein für Ihre Netzversorgung geeignetes Leistungsmessgerät, eine Liste der Geräte und Netzteile sowie Zugriff auf technische Daten und Laufzeitdiagramm jedes vorgesehenen USV-Modells. Für einen automatischen Abschalttest brauchen Sie außerdem eine unterstützte USB- oder Netzwerkverwaltungsverbindung und passende Software für jeden Host. Planen Sie Zeit für eine Messung bei normaler Last, eine Beobachtung unter hoher Last und einen geplanten Wartungstest ein. Diese Aufgabe richtet sich an fortgeschrittene Homelab-Nutzer, denn ein vollständiger Abschalttest unterbricht Dienste.

Der [Leitfaden zu Überspannungsschutzgeräten](/articles/protecting-your-tech_-the-best-surge-protectors/) der Website behandelt den Schutz vor Überspannungen. Die [Übersicht zu USV-Modellen](/articles/best-ups-models-for-uninterrupted-connectivity/) listet Produkte auf. Dieser Leitfaden behandelt die Dimensionierung und Prüfung Ihrer eigenen Last. Sowohl Eatons [Leitfaden zur USV-Dimensionierung](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html) als auch Schneiders [USV-Kaufberatung](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) unterscheiden zwischen Ausgangsleistung und Batterielaufzeit.

> **Warnung:** Verwenden Sie nur die vom USV-Hersteller zugelassenen Ausgänge und Lasten. Bleiben Sie beim Test innerhalb der Nennleistung der USV. Ein echter Abschalttest stoppt das angeschlossene Lab.

## Ermitteln, was weiterläuft

Entscheiden Sie, welche Geräte bis zur Abschaltung laufen müssen. Berücksichtigen Sie den Hypervisor, das Speichergerät, den Netzwerk-Switch und den Router, falls ein Host Netzwerkzugriff benötigt, um ein Abschaltsignal zu empfangen. Lassen Sie Bildschirme, Drucker und andere optionale Verbraucher an den batteriegestützten Ausgängen weg, sofern Ihr Plan sie nicht benötigt.

Messen Sie die vorgesehene Gruppe batteriegestützter Geräte an der Steckdose. Notieren Sie die **Watt bei normaler Last** und den höchsten beobachteten Wattwert bei typischen Arbeiten, etwa beim Starten von Hosts oder virtuellen Maschinen. Das Typenschild eines Netzteils gibt dessen Kapazität an, nicht die gemessene Leistungsaufnahme des Systems. Prüfen Sie dennoch auf jedem Geräteetikett die Eingangs- und Einschaltstromgrenzen. Halten Sie die Messbedingungen in Ihrem Arbeitsblatt fest.

| Gerät | Watt bei normaler Last | Beobachtete Spitzenlast in Watt | Batterieausgang? |
|---|---:|---:|---|
| **Router und Switch** | 30 | 35 | Ja |
| **NAS** | 60 | 90 | Ja |
| **Kleiner Server** | 90 | 135 | Ja |
| **Beispielsumme** | **180** | **260** | Drei Geräte |

Die Werte oben sind **Beispiele** und keine Messwerte eines bestimmten Labs. Ihre Last ändert sich durch Laufwerke, GPUs, Energieeinstellungen und angeschlossene Geräte. Messen Sie nach größeren Hardwareänderungen erneut.

## Watt und VA vergleichen

**Watt** beschreiben die Wirkleistung der Geräte. **Voltampere (VA)** beschreiben die Scheinleistung. Das Verhältnis hängt vom **Leistungsfaktor** ab: Watt geteilt durch den Leistungsfaktor ergibt VA. Eaton erläutert diese Berechnung in seinem [Dimensionierungsleitfaden](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). Behandeln Sie eine Angabe von 1000 VA nicht wie 1000 Watt. Prüfen Sie die separate Watt-Nennleistung der USV.

Bei der beispielhaften Spitzenlast von 260 W ergeben 25 % Leistungsreserve **325 W**. Schneider Electric empfiehlt eine Ausgangsleistung von etwa [20 % bis 25 % über der Last](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Wählen Sie eine USV, deren Dauer-Wattwert die geplante Spitzenlast einschließlich Reserve übersteigt. Wenn Sie den kombinierten Leistungsfaktor kennen, teilen Sie die Spitzenleistung in Watt durch diesen Wert, um die Spitzenlast in VA zu schätzen, und addieren Sie auch dort Ihre gewählte Reserve. Verwenden Sie andernfalls ein geeignetes Messgerät oder den Auswahlrechner des Herstellers für VA-Anforderung und Reserve. Erfinden Sie keinen Leistungsfaktor, wenn Sie ihn nicht gemessen haben.

Eine Leistungsreserve garantiert keine Laufzeit. Eine USV mit hoher Wattgrenze, aber kleiner Batterie kann die Last nur kurz versorgen. Prüfen Sie vor der Wahl eines Modells die Ausgänge, den Steckertyp, die Eingangsspannung, die Kommunikationsschnittstelle und den Weg zum Batteriewechsel.

## Laufzeitziel festlegen

Notieren Sie, wie lange das Lab für einen sicheren Stopp benötigt. Berücksichtigen Sie die Zeit, bis Hosts eine Abschaltmeldung erhalten, virtuelle Maschinen stoppen, Speicher Schreibvorgänge abschließt und die USV die Ausgabe abschaltet. Planen Sie Reserve für einen langsamen Abschaltvorgang und eine ältere Batterie ein. Ein Lab, das kurze Ausfälle überbrücken soll, braucht ein anderes Ziel als eines, das nur geordnet herunterfahren muss.

Nehmen wir als **Beispiel** an, ein getesteter Abschaltvorgang dauert 6 Minuten und Sie planen 5 Minuten Reserve ein. Dann sind bei der erwarteten Last mindestens 11 Minuten Laufzeit erforderlich. Das ist ein Planungsbeispiel, kein allgemeiner Grenzwert. Vergleichen Sie das Ziel mit dem Laufzeitdiagramm oder Auswahlrechner des jeweiligen Modells bei Ihrer **gemessenen normalen und hohen Last** und prüfen Sie den Wert erneut, wenn die Batterie altert. Schneiders [USV-Auswahlrechner](https://www.se.com/us/en/work/products/tools/ups-selector/) berechnet die Laufzeit anhand der eingegebenen Last und der Modellspezifikationen. Eaton verweist in seiner [Desktop-USV-Kaufberatung](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html) ebenfalls auf modellspezifische Laufzeitdaten.

Kopieren Sie dieses **Arbeitsblatt** für Ihr Lab. Tragen Sie die Gerätezeilen anhand Ihrer Leistungsmessungen ein. Addieren Sie die normalen und hohen Wattwerte, rechnen Sie Ihre gewählte Reserve auf die hohe Gesamtlast auf und wenden Sie dieselbe Reserve auf die gemessene oder berechnete Spitzenlast in VA an. Vergleichen Sie beide Ergebnisse mit einer geeigneten USV. Wenn Sie stattdessen einen Herstellerauswahlrechner verwenden, notieren Sie dessen VA-Ergebnis und die Reserve. Verwenden Sie für die Laufzeitschätzung das Diagramm des Modells. Ergänzen Sie Zeit- und Wiederherstellungswerte während des Tests.

| Feld | Ihr Ergebnis |
|---|---|
| **Geräte und Batterieausgänge** | Gerätenamen und zugewiesener Ausgang |
| **Watt je Gerät und insgesamt bei normaler Last** | Messwerte und Summe |
| **Watt je Gerät und insgesamt bei hoher Last** | Höchste beobachtete Werte und Summe |
| **Gemessener oder angegebener Leistungsfaktor** | Wert und Quelle oder „unbekannt“ |
| **Gemessene oder berechnete Spitzenlast in VA** | Spitzenleistung in Watt geteilt durch den kombinierten Leistungsfaktor, falls bekannt |
| **Leistungsreserve** | Gewählter Prozentsatz, Watt und VA nach Reserve |
| **Nennwerte der vorgesehenen USV** | Modell, Ausgangsleistung in Watt und VA sowie Ausgangsgrenzen |
| **Laufzeitziel und Diagrammwert** | Benötigte Minuten und Modellschätzung für Ihre Last |
| **Alarm- und Abschaltzeiten** | Zeitpunkt des Batteriewarnsignals und des letzten angehaltenen Hosts |
| **Ergebnis der Wiederherstellung** | Hoststart, Speicher, Anwendungen und Überwachung |

Wenn der Leistungsfaktor unbekannt ist, verwenden Sie den Auswahlrechner des Herstellers oder messen Sie die Scheinleistung mit einem geeigneten Gerät. Geben Sie keinen berechneten VA-Wert an, der auf einem geratenen Faktor beruht. Das Arbeitsblatt ist erst vollständig, wenn das Modell beide Ausgangsgrenzen erfüllt und seine Laufzeitschätzung Ihr Abschaltziel übersteigt.

> **Erwartetes Ergebnis:** Ihr Arbeitsblatt nennt die angeschlossenen Geräte, gemessene Lasten, Watt- und VA-Grenzen der USV, das Laufzeitziel und eine modellspezifische Laufzeitschätzung.

## Automatische Abschaltung planen

Eine USV versorgt Geräte vorübergehend mit Strom. Der Host benötigt weiterhin ein **Abschaltsignal**. Prüfen Sie, ob Ihre USV USB, eine Netzwerkverwaltungskarte oder eine andere unterstützte Schnittstelle bereitstellt. Prüfen Sie, ob jeder anzuhaltende Host über einen kompatiblen Überwachungspfad verfügt. Eaton weist darauf hin, dass viele Modelle USB- oder Netzwerkkommunikation für ein [geordnetes Herunterfahren von NAS oder Server](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html) unterstützen.

In einem Linux-Lab mit **Network UPS Tools (NUT)** liest der USV-Treiber das Gerät aus, `upsd` stellt dessen Status bereit und `upsmon` löst die Host-Abschaltung aus, wenn die Stromversorgung kritisch wird. Ein direkt per USB oder serieller Schnittstelle verbundener Host führt normalerweise Treiber, `upsd` und `upsmon` im **Primary-Modus** aus. Andere Hosts führen `upsmon` im **Secondary-Modus** gegen diesen Server aus. Eine netzwerkverwaltete USV braucht einen kompatiblen Treiber und eine modellspezifische Primary-Konfiguration. Der [NUT-Topologie-Leitfaden](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) erläutert diese Rollen. Konfigurieren Sie Router und Switch so, dass Überwachungs-Hosts bei Batteriebetrieb verbunden bleiben. Beschränken Sie den Abschaltbefehl und dessen Berechtigungen auf Administratoren.

Prüfen Sie vor einem Abschalttest, ob der Treiber einen aktuellen Status meldet. Ersetzen Sie `myupsname` durch den USV-Namen in Ihrer NUT-Konfiguration:

```bash
upsc myupsname@localhost ups.status
```

NUTs [Konfigurationsleitfaden](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) erwartet bei normaler Netzversorgung `OL` und erläutert `OB` für Batteriebetrieb. Führen Sie die Statusprüfung auf jedem Host aus, der die USV überwacht, und verwenden Sie bei entfernten Clients den richtigen Servernamen. Ein veralteter oder fehlender Messwert bedeutet, dass der Signalweg vor einem Abschalttest repariert werden muss.

Notieren Sie die **Abschaltreihenfolge**. Stoppen Sie zum Beispiel zuerst Anwendungs-VMs, danach Speicher-Clients und zuletzt Hypervisor und NAS. Prüfen Sie, ob sich jeder Dienst und jedes Dateisystem nach Rückkehr der Stromversorgung normal erholt. Ein erfolgreicher Host-Stopp ohne gesunde Anwendungserholung ist kein vollständiges Ergebnis.

## Ohne Raten testen

Beginnen Sie mit einem **Probelauf** auf dem Host, auf dem der USV-Treiber konfiguriert ist. NUT dokumentiert `upsdrvctl -t shutdown` als Vorschau der Treiber-Abschaltsequenz. Dabei werden weder die Treiber aufgerufen noch die Stromversorgung abgeschaltet:

```bash
upsdrvctl -t shutdown
```

Dieser **Treiber-Probelauf** beweist nicht, dass eine Ausfallmeldung jeden Host erreicht. Prüfen Sie jeden Überwachungsdienst und dessen Protokolle. In einem Wartungsfenster beschreibt NUTs [Anleitung zum Testen der Abschaltung](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) einen erzwungenen Abschalttest mit `upsmon -c fsd` auf dem primären NUT-Host. Dieser **FSD-Test** startet eine echte Abschaltsequenz. Das FSD-Flag bleibt gesetzt, bis `upsd` neu gestartet wird. Prüfen Sie nach dem Systemstart, ob `upsd` neu gestartet wurde und der Status kein FSD mehr anzeigt, bevor Sie sich wieder auf die Überwachung verlassen. Lesen Sie das aktuelle [upsmon-Handbuch](https://networkupstools.org/docs/man/upsmon.html), bereiten Sie einen Wiederherstellungsweg vor und führen Sie den Test erst aus, nachdem Sie Arbeit gespeichert und Lab-Nutzer informiert haben.

Führen Sie für einen kontrollierten **Batterieereignistest** zunächst das Testverfahren des USV-Herstellers mit unkritischen Lasten aus. Dieser Test bei niedriger Last prüft die Signalübertragung, beweist aber nicht die Laufzeit für Ihr Lab. Testen Sie später in einem Wartungsfenster mit einer repräsentativen geplanten Batterielast. Eine Person sollte die USV überwachen und die Netzversorgung wiederherstellen können, falls die Reserve schrumpft. Notieren Sie die von der USV angezeigte Last, den Zeitpunkt der Batteriemeldung, den Beginn jeder Host-Abschaltung und den Zeitpunkt, an dem der letzte Host anhält. Prüfen Sie, dass die USV ihre Batterie nicht erschöpft, bevor die Hosts stoppen. Kontrollieren Sie nach Rückkehr der Netzversorgung Hoststart, Anwendungszustand, Speicherintegrität und Überwachungsstatus. Laut NUT ist eine Sequenz erfolgreich, wenn das Betriebssystem vor dem Ende der Batterielaufzeit stoppt und den Betrieb nach Rückkehr der Versorgung wieder aufnimmt.

| Prüfung | Ergebnis notieren |
|---|---|
| **Signalweg** | USV-Ereignis ist auf jedem Überwachungs-Host sichtbar |
| **Abschaltzeitpunkt** | Letzter Host stoppt, bevor die Batterie erschöpft ist |
| **Wiederherstellung** | Hosts, Speicher und Anwendungen starten ordnungsgemäß |
| **Kapazität** | USV-Last bleibt innerhalb der Watt- und VA-Grenzen |

## Fehlerbehebung

- **Überlastalarm der USV:** Entfernen Sie optionale Verbraucher. Vergleichen Sie die gemessene Spitzenlast mit beiden USV-Nennwerten und den Ausgangsgrenzen des Modells.
- **Laufzeit kürzer als erwartet:** Prüfen Sie aktuelle Last, Batteriealter, modellspezifische Laufzeitdaten und jüngste Batterietests. Leiten Sie die Laufzeit nicht allein aus VA linear ab.
- **Ein Host bleibt eingeschaltet:** Prüfen Sie dessen Überwachungsdienst, Netzwerkweg, Abschaltberechtigungen und Protokolle.
- **Hosts stoppen, starten aber nicht wieder:** Prüfen Sie das Neustartverhalten des USV-Ausgangs, die Firmware-Einstellung zur Rückkehr der Versorgung und NUTs dokumentierte [Überlegungen zu Stromversorgungsrennen](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **Der Probelauf klappt, der Ausfalltest aber nicht:** Die Treibervorschau prüft nur einen Teil des Ablaufs. Prüfen Sie die Ereignisübertragung und die tatsächliche Abschaltreihenfolge der Hosts.

## Nächste Schritte

Bewahren Sie das Arbeitsblatt zusammen mit Ihrem Homelab-Inventar auf. Prüfen Sie die Last nach dem Hinzufügen von Hardware erneut und wiederholen Sie den Abschalttest nach Änderungen an USV, Überwachungssoftware, Host-Startverhalten oder Speicher-Stack. Prüfen Sie Ihren Sicherungs- und Wiederherstellungsplan separat. Die Batterie sichert das Abschaltfenster ab, während ein [getestetes Homelab-Backup](/articles/what-is-a-homelab-and-should-you-have-one/) Ihre Daten bei anderen Ausfällen schützt.
