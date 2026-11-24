---
title: "Kali Purple 2023.1: Updates und wichtige Funktionen"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "Rückblick auf Kali Purple 2023.1 mit den damaligen Funktionen, Werkzeugen und Verbesserungen sowie aktuellen Hinweisen für Sicherheitslabore."
tags: ["Kali Linux", "Kali Purple", "2023.1", "Ethisches Hacking", "Penetrationstests", "Cybersicherheit", "Werkzeuge", "Exploit-Framework", "Kali-ARM-Aktualisierungen", "Kali NetHunter", "Kali-Dokumentation", "Kernel-Unterstützung", "Bluetooth-Unterstützung", "LineageOS", "OneUI", "Radxa Zero", "Einplatinencomputer", "Kernel-Patches", "Beiträge der Community", "Kali Discord", "Linux-Aktualisierungen", "Distribution für ethisches Hacking", "neue Funktionen", "Verbesserungen", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "neue Tools und Pakete", "ARM-Geräteunterstützung", "Kali-Dokumentation", "staatliche Vorschriften"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Ein 3D-animierter Kali-Linux-Drache sitzt auf einem Schild und ist von Cybersecurity-Werkzeugen umgeben."
coverCaption: ""
---

**Kali Purple 2023.1: Ein Rückblick**

Kali Purple 2023.1 war die erste technische Vorschau auf die defensive Sicherheitsausrichtung von Kali. Sie ist nicht mehr die aktuelle Kali-Version. Dieser Artikel dokumentiert die ursprüngliche Veröffentlichung und verweist auf aktuelle Versionen, damit Sie die Paketversionen von 2023.1 nicht für aktuell halten.

## Aktueller Kali-Stand

In Kalis offizieller Versionsübersicht ist Kali 2026.2 als zweite Rolling-Release-Version des Jahres 2026 aufgeführt. Sie erschien am 29. Juni 2026 und verwendet Linux-Kernel 6.19 sowie Xfce 4.20.7. Die [Versionshinweise zu Kali 2026.2](https://www.kali.org/blog/kali-linux-2026-2-release/) nennen außerdem GNOME 50, KDE Plasma 6.6, den Wechsel von `sources.list` zu `sources.list.d/kali.source` und Änderungen beim Start virtueller Maschinen.

Kali Purple steht innerhalb von Kali für eine defensive und Purple-Team-Ausrichtung. Die Ankündigung von 2023.1 beschrieb eine technische Vorschau mit einer SOC-in-a-Box-Referenzarchitektur, defensiven Werkzeugen und Menükategorien nach dem NIST Cybersecurity Framework. Diese Angaben beschreiben den historischen Umfang. Wählen Sie für aktuelle Pakete in Kalis [Metapaket-Dokumentation](https://www.kali.org/docs/general-use/metapackages/) nur die Werkzeuggruppen aus, die Ihr Labor benötigt.

*Führen Sie offensive und defensive Sicherheitsübungen nur in einem isolierten, autorisierten Labor durch. Eine Kali-Installation erteilt keine Erlaubnis, Systeme zu testen, die Sie weder besitzen noch verwalten.*

______

## Kali Hintergrundbild und Desktop-Updates

Kali Purple 2023.1 führt ein **neues Standard-Hintergrundbild** namens Kali Sticker ein, das einen lila Hintergrund und verschiedene Kali-bezogene Sticker zeigt. Dieses neue Hintergrundbild wurde durch die Arbeit von /u/Albert-III- und TJ_Null inspiriert.

Zusätzlich zum neuen Hintergrundbild aktualisiert Kali Purple 2023.1 auch die drei wichtigsten Desktop-Umgebungen: **Xfce, KDE, und GNOME**. Diese Updates beinhalten neue Funktionen, Leistungsverbesserungen und Fehlerkorrekturen.

______

## Xfce 4.18

**Xfce 4.18** bringt mehrere bemerkenswerte Verbesserungen, darunter:

- Verbesserte Unterstützung für UI-Skalierung
- Aktualisierungen des Thunar-Dateimanagers
- Panel-Profile für einfache Anpassung

______

## KDE Plasma 5.27

Das **KDE Plasma 5.27** Update führt ein:

- Ein neues Fenster-Kachelsystem
- Ein eleganteres App-Thema
- Sauberere und besser nutzbare Werkzeuge und Widgets

______

## GNOME-Aktualisierungen

Für GNOME bringt Kali Purple 2023.1 einige Verbesserungen der Benutzerfreundlichkeit mit sich, wie z.B. die Möglichkeit, durch Drücken der F4-Taste schnell ein Terminal im aktuellen Ordner des Dateimanagers zu öffnen.

______

## Standard-Kernel-Einstellungen und bekannte Probleme

Kali Purple 2023.1 aktualisiert einige Kernel-Standardwerte für bessere Benutzerfreundlichkeit.

______

## Neue Tools und Pakete

Kali Purple 2023.1 ergänzt neue Werkzeuge und Pakete für **Penetrationstests** und **ethisches Hacking**. Dazu gehören:

- **Rizin 0.3.0**: Ein modernes Framework für Reverse Engineering
- **Ghidra 10.1**: Eine Open-Source-Suite für Software-Reverse-Engineering
- **Python 3.10**: Die neueste Version der Programmiersprache

Diese Werkzeuge und Aktualisierungen bestehender Pakete erweiterten die Vorschau 2023.1 für Sicherheitsexperten. Die Versionsnummern in diesem Abschnitt beziehen sich auf die Veröffentlichung 2023.1, nicht auf die in Kali 2026.2 enthaltenen Versionen.

______

## ARM-Geräte-Unterstützung

Kali Purple 2023.1 baut seine Unterstützung für ARM-Geräte weiter aus, indem es Kompatibilität für neue Geräte wie das **Radxa Zero** hinzufügt und die bestehende Unterstützung für Geräte wie das **LG V20** verbessert. Diese breite Unterstützung stellt sicher, dass Kali auf einer Vielzahl von Geräten verwendet werden kann, von kleinen Einplatinen-Computern bis hin zu leistungsstarken Smartphones.

______

## Dokumentation und Community

Das Kali-Team hat seine **Dokumentation** mit neuen Anleitungen, Tutorials und Tipps zur Fehlerbehebung aktualisiert, um Benutzern zu helfen, das Beste aus Kali Purple 2023.1 herauszuholen. Außerdem wurden mehrere Community-Mitglieder für ihre Beiträge zu Kali ausgezeichnet, was die Kraft der Open-Source-Zusammenarbeit und die Stärke der Kali-Community unterstreicht.

______

## Regierungsvorschriften

In diesem Artikel werden zwar keine spezifischen staatlichen Vorschriften für Ethical Hacking oder Penetrationstests behandelt, es ist jedoch wichtig zu wissen, dass diese Aktivitäten in vielen Ländern gesetzlich geregelt sind. Vergewissern Sie sich stets, dass Sie über die entsprechenden Genehmigungen verfügen und die geltenden Gesetze befolgen, wenn Sie Sicherheitsbewertungen durchführen. Wenn Sie mehr über einschlägige Vorschriften erfahren möchten, sollten Sie die folgenden Ressourcen besuchen:

- [The Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [The General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## Schlussfolgerung

**Kali Purple 2023.1** war ein funktionsreiches erstes Preview für die defensive Sicherheitsausrichtung von Kali. Die Vorschau ergänzte Werkzeuge, verbesserte die ARM-Unterstützung und erweiterte die Dokumentation. Prüfen Sie für aktuelle Installationen die Kali-Versionshinweise und wählen Sie passende Pakete für Ihr Labor. Halten Sie sich an geltende Vorschriften und testen Sie Systeme nur mit ausdrücklicher Genehmigung.

______

## Referenzen

1. [Offizielle Kali-Linux-Website](https://www.kali.org/)
2. [Kali-Linux-Dokumentation](https://www.kali.org/docs/)
3. [Kali-Linux-Downloads](https://www.kali.org/get-kali/)
4. [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## Zusätzliche Ressourcen

- [Offizielle Kali-Linux-Foren](https://forums.kali.org/)
- [Kali-Linux-Blog](https://www.kali.org/blog/)
- [Kali-Linux-Schulungen und Zertifizierung](https://www.offensive-security.com/)

______

## Update-Checkliste

- **Versionsverlauf prüfen.** Lesen Sie vor dem Herunterladen eines Images Kalis aktuellen [Versionsverlauf](https://www.kali.org/releases/).
- **Offizielle Images verwenden.** Laden Sie Images über [Get Kali](https://www.kali.org/get-kali/) herunter und prüfen Sie die veröffentlichten Prüfsummen.
- **Rolling-Installationen aktualisieren.** Folgen Sie Kalis aktueller [Update-Dokumentation](https://www.kali.org/docs/general-use/updating-kali/), statt das Repository-Beispiel von 2023.1 ungeprüft zu übernehmen.
- **Metapakete gezielt auswählen.** Ein Standard- oder Purple-Labor benötigt nicht jedes Kali-Paket.
- **Laborumfang dokumentieren.** Legen Sie autorisierte Systeme, Testzeiträume, Protokollierung und Bereinigung fest, bevor Sie Werkzeuge starten.
