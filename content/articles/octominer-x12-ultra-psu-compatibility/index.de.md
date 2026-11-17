---
title: "Octominer X12 Ultra Netzteil-Kompatibilität: Chicony- und LiteOn-Praxistest"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Ein Test mit fünf Lüftern und drei Netzteilen im Octominer X12 Ultra zeigte: Ein Chicony-Netzteil startete das System, getestete LiteOn-Geräte zeigten dagegen Gelb und starteten nicht."
genre: ["Kryptowährungs-Mining-Ausrüstung", "Rechnerhardware"]
tags: ["Octominer X12 Ultra", "Server-Netzteil", "Netzteil-Kompatibilität", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Abstrakte Darstellung von drei Servernetzteilen in einem Gehäuse mit grünen, gelben und grauen Statusanzeigen"
coverCaption: ""
---

**Das Chicony R12-1K6P2A startete meinen Octominer X12 Ultra mit fünf Lüftern und drei Netzteilen.** Die getesteten LiteOn-PS-2142-2L-Netzteile leuchteten zunächst grün, wechselten zu Gelb und starteten das System nicht. Das Ergebnis gilt für mein Gerät mit einer **OCTOMINER (12PIN) 3x DPS1200 rev. 20**-Stromversorgungsplatine. Gleiche Wattzahl oder eine Liste für ein separates X12-Breakout-Board belegen keine Kompatibilität mit einer Octominer-Platine.

Das Gehäuse wurde als **3.600-W-Konfiguration** mit drei Netzteil-Schächten verkauft. [Octominer führt eine Option mit drei Netzteilen zu je 1.200 W auf](https://octominer.eu/product/octominer-x12-ultra-used/), neben weiteren Konfigurationen. Prüfen Sie das Etikett und die Stromversorgungsplatine Ihres eigenen Systems, bevor Sie diese Ergebnisse übertragen.

## Testergebnisse

| Netzteil | Ergebnis in diesem System |
|---|---|
| **Chicony R12-1K6P2A, 1.600 W** | Startete das System in meinem Test. Dauerlast und Betrieb in jedem Schacht wurden für diesen Artikel nicht gemessen. |
| **LiteOn PS-2142-2L, 1.400 W** | Getestete Geräte leuchteten erst grün, dann gelb. Das System startete nicht. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | Der ungewöhnliche Netzeingang erschwerte die Suche nach einem passenden Kabel. Für dieses Netzteil liegt in diesem Test kein Start- oder Lastresultat vor. |
| **HP HSTNS-PD30, 1.200 W** | Im selben System getestet. Das System startete nicht. |
| **Weitere HP-Common-Slot-Geräte** | Die getesteten 1.200-W-Platinum-Plus-Kits und 750-W-Modelle HSTNS-PD22B, HSTNS-PL22B und HSTNS-PD18 starteten das System nicht. Die genauen Netzteil-Modellnummern der Kits wurden nicht erfasst. |

**Deuten Sie das LiteOn-Ergebnis nicht als Fehlerdiagnose für jedes PS-2142-2L.** Die beobachtete Abfolge zeigt einen fehlgeschlagenen Start in diesem Gehäuse. Der Test isolierte weder das Einschalt-Signal noch Telemetrie, Pinbelegung der Platine oder einen Defekt eines einzelnen Netzteils. Ebenso belegt das Chicony-Ergebnis einen erfolgreichen Start, aber weder eine zertifizierte Gehäuseleistung von 4.800 W noch Langzeitzuverlässigkeit.

## Welches Chicony startete das System?

Das erfolgreiche Modell war **Chicony R12-1K6P2A**, in der [Kompatibilitätstabelle von Parallel Miner auch als Teil **R1K6A002L** aufgeführt](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Der [80-PLUS-Prüfbericht](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) nennt ein 1.600-W-Netzteil mit **200 bis 240 V AC**, 10 A und 50 bis 60 Hz. Unter den Prüfbedingungen bei 230 V maß der Bericht bei halber Last einen Wirkungsgrad von 94,19 %. Diese Werte beschreiben das geprüfte Netzteil, nicht das komplette Mining-System.

Die Nennspannung von **200 bis 240 V ist wichtig**. Gehen Sie nicht davon aus, dass dieses Modell seine Nennleistung an einer 120-V-Steckdose liefert. Laut einer [Ersatzteilliste für genau dieses Modell](https://www.itcreations.com/product/142080) besitzt das getestete Netzteil einen normalen C14-Eingang. Verwenden Sie Kabel und Stromverteilung, die für Eingangsspannung und Stromstärke ausgelegt sind.

Mein Test belegte einen erfolgreichen Start mit dem Chicony an dieser bestimmten Platine. Er belegt keine Kompatibilität mit jeder X12-Ultra-Revision. Vergleichen Sie die vollständige Modellnummer und prüfen Sie das Netzteil-Etikett, bevor Sie weitere Geräte bestellen.

## Warum die LiteOn-Liste irreführte

Das **LiteOn PS-2142-2L** steht in der [Kompatibilitätstabelle für X12-Breakout-Boards von Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Sein [80-PLUS-Bericht](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) nennt ein 1.400-W-Modell. Diese Quellen belegen das Modell und seine aufgeführte Verwendung mit dem **X12-Adapter von Parallel Miner**. Keine der Quellen prüft die originale Octominer-Stromversorgungsplatine.

Meine PS-2142-2L-Geräte wechselten nach dem Einsetzen von **Grün zu Gelb**, und das System startete nicht. Ähnlich aussehende Ausgangskontakte belegen kein gleiches Start-, Status- oder Kommunikationsverhalten. Die LED-Abfolge allein beweist nicht, welcher Unterschied den fehlgeschlagenen Start verursachte.

Dieselbe [Tabelle von Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) ordnet **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** und **Chicony R12-1K6P2A** einer Acht-Pin-Adapterfamilie zu. **HP HSTNS-PD30** und mehrere 750-W-HP-Common-Slot-Netzteile stehen in einer anderen Familie mit Sechs-Pin-Adapter. Keines der getesteten HP-Geräte startete dieses System. Die Tabelle beschreibt Parallel-Miner-Platinen, keine Ersatzteilliste für die **OCTOMINER (12PIN)**-Platine.

## Stromversorgung und Verkabelung prüfen

Der [Fehlerbehebungsleitfaden für den Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) gibt an, dass das Gehäuse allein bei Lüftern auf voller Drehzahl bis zu **200 W** verbraucht. Er empfiehlt mindestens **10 % Leistungsreserve** und warnt davor, mehr als **90 % der Nennleistung der installierten Netzteile** zu nutzen. Berücksichtigen Sie GPU-Leistung, Gehäuse und die tatsächliche Netzteilleistung bei Ihrer Wechselspannung.

**Ein 1.600-W-Etikett auf jedem Chicony-Netzteil erhöht die veröffentlichte 3.600-W-Gehäusekonfiguration nicht auf 4.800 W.** Auch Stromversorgungsplatine, interne Kabel, Anschlüsse, Wechselstromverteilung und Kühlung begrenzen das System. Ich habe diese Grenzen an diesem Gerät nicht gemessen. Halten Sie das System innerhalb der dokumentierten Konfiguration, bis Octominer eine höhere Leistung für genau diese Platinenrevision bestätigt.

Beim Dell/Delta **D1200E-S0 / 0F37X3** trat ein anderes Problem auf: Der netzteilseitige Netzeingang erforderte ein selteneres passendes Kabel. Bei einer früheren Suche identifizierte ich den Eingang anhand des Geräts und der Kabelangebote als **LS-25** und den Kabelstecker als **LS-26**. Prüfen Sie Steckerform und elektrische Angaben vor dem Kauf eines Kabels. Ein ähnlich aussehender C13-Stecker ersetzt nicht den passenden Gegenstecker.

## Eigenen X12 prüfen

1. **Genaue Hardware erfassen.** Fotografieren Sie Gehäuseetikett, Netzteil-Etikett, Netzeingang, Ausgangskontakt und Revision der Stromversorgungsplatine. Zählen Sie Lüfter und Netzteilschächte.
2. **Wechselstromversorgung prüfen.** Vergleichen Sie die Eingangsnennwerte des Netzteils mit den Nennwerten von Steckdose, Kabel und PDU. Der Bericht für das Chicony R12-1K6P2A nennt 200 bis 240 V AC.
3. **Minimalkonfiguration testen.** Fahren Sie das System herunter und trennen Sie alle Wechselstromzuführungen, bevor Sie Netzteil, GPU oder PSON-Verbindung ändern. [Octominers Leitfaden](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) empfiehlt, Sitz und LEDs des Netzteils, das Sechs-Pin-PSON-Kabel zwischen Mainboard und Stromversorgungsplatine sowie ein Netzteil mit einer GPU zu prüfen, um ein Startproblem einzugrenzen.
4. **Ergebnis protokollieren.** Notieren Sie Netzteilmodell, Schacht, LED-Abfolge, Start der Platine und Lüfter sowie den Systemstart. Wiederholen Sie den Test an anderen Schächten erst nach einem sicheren Herunterfahren.
5. **Vor zusätzlicher Last messen.** Prüfen Sie Netzteil-Telemetrie und Leistungsaufnahme an der Steckdose unter der geplanten GPU-Last. Der Starttest in diesem Artikel ersetzt keinen Lasttest.

## Fazit

**Chicony R12-1K6P2A ist in diesem Vergleich das einzige Ersatznetzteil mit dokumentiertem erfolgreichem Start in meinem X12 Ultra mit drei Schächten.** Die getesteten LiteOn-PS-2142-2L-Geräte wechselten von Grün zu Gelb und starteten nicht. Auch die getesteten HP-Common-Slot-Geräte starteten das System nicht. Behandeln Sie andere Netzteillisten als Recherchehinweise, bis genaues Netzteilmodell und Octominer-Stromversorgungsplatine einen kontrollierten Start- und Lasttest bestehen. Beginnen Sie mit den Modell-Etiketten und der Platinenrevision. Prüfen Sie Octominers Stromversorgungshinweise, bevor Sie die GPU-Last erhöhen.
