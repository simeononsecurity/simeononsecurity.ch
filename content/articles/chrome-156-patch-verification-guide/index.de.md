---
title: "Chrome 156 Sicherheitsupdate: Oktober-Patch überprüfen"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Prüfe das Sicherheitsrelease von Chrome 156 vom 27. Oktober unter Windows, macOS, Linux und Android. Vergleiche den installierten Build, schließe einen ausstehenden Neustart ab und prüfe verwaltete Geräte separat."
genre: ["Browser", "Sicherheit", "Patch-Management"]
tags: ["Chrome 156", "Chrome-Sicherheitsupdate", "Chrome-Patch überprüfen", "Chrome-Version prüfen", "Chrome 156 für Windows", "Chrome 156 für macOS", "Chrome 156 für Linux", "Chrome 156 für Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "Browser-Patches", "Chrome Enterprise Core", "verwaltete Browser", "Chromium-Sicherheit", "Browser-Updates", "Chrome-Neustart", "chrome://version", "chrome://settings/help", "Chrome-Update für Android", "Brave-Sicherheitsupdates", "Edge-Sicherheitsupdates"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Abbildung eines Vorhängeschlosses und eines Schutzschilds als Symbol für ein Sicherheitsupdate, nicht für eine Chrome-Versionsanzeige"
coverCaption: ""
---

**Das Sicherheitsrelease von Chrome vom 27. Oktober 2026** enthält 52 Fehlerbehebungen. Vergleiche zur Prüfung deiner Installation die vollständige Versionsnummer mit dem Release für dein Betriebssystem. Starte Chrome anschließend neu, um ein ausstehendes Update abzuschließen. Eine angekündigte Version beweist nicht, dass dein Gerät das Update erhalten hat. ([Chrome-Desktop-Release](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Welche Version sollte angezeigt werden?

Google veröffentlichte diese Stable-Versionen am 27. Oktober 2026. Das Desktop-Release nennt eigene Builds für Windows und macOS sowie für Linux. Das [Android-Release](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) nennt seinen Build und weist darauf hin, dass Android-Releases dieselben Sicherheitskorrekturen wie die entsprechenden Desktop-Releases enthalten, „sofern nicht anders angegeben“.

| Plattform | Build aus Googles Ankündigung vom 27. Oktober |
|---|---|
| **Windows** | 156.0.8078.73 oder 156.0.8078.74 |
| **macOS** | 156.0.8078.73 oder 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Verwende diese Tabelle für das Release vom 27. Oktober, nicht als dauerhaftes Ziel. Spätere Sicherheitsupdates findest du im aktuellen [Chrome-Releases-Feed](https://chromereleases.googleblog.com/).* Google erklärte, dass der Desktop-Rollout „in den nächsten Tagen oder Wochen“ erfolgen und der Android-Build in den nächsten Tagen Google Play erreichen werde. Ein Gerät mit einer niedrigeren Version muss weiterhin geprüft werden, auch während eines gestaffelten Rollouts. ([Desktop-Mitteilung](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [Android-Mitteilung](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

Die [Liste der Desktop-Sicherheitskorrekturen](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) stuft vier gemeldete Fehler als **Critical** ein: Speicherbeschädigung in FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), fehlerhafte Eingabevalidierung in FileAPI CVE-2026-118331, fehlerhafte Eingabevalidierung in Skia CVE-2026-118348 und Use-after-free in Layout CVE-2026-118344. Dieselbe Mitteilung führt weitere CVEs mit den Einstufungen **High** und **Medium** auf. Die Zahl 52 bezeichnet die Sicherheitskorrekturen im Release, nicht 52 unabhängig bestätigte Exploit-Meldungen. ([NVD-Eintrag](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**Die Release-Mitteilung behauptet nicht, dass die aufgeführten Schwachstellen aktiv ausgenutzt werden.** Der Hinweis betrifft den Zeitpunkt der Offenlegung: „Der Zugriff auf Fehlerdetails und Links kann eingeschränkt bleiben, bis die Mehrheit der Nutzer ein Update erhalten hat.“ Behandle eingeschränkte Fehlerdetails nicht als Beleg für eine Ausnutzung. ([Desktop-Mitteilung](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Desktop-Update prüfen und abschließen

1. Öffne **`chrome://version`** in der Chrome-Installation, die du verwendest. Notiere die vollständige Version und das Betriebssystem, nicht nur die Hauptversionsnummer 156. Ein Chrome-Fenster aus einem anderen Kanal oder einer anderen Installation muss separat geprüft werden.
2. Öffne **`chrome://settings/help`** oder wähle **Mehr > Hilfe > Über Google Chrome**. Laut Google sucht Chrome auf dieser Seite nach Updates. Warte, bis die Prüfung abgeschlossen ist. ([Googles Desktop-Anleitung zum Update](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Wähle **Neu starten**, falls die Seite diese Option anbietet. Speichere vorher deine offene Arbeit. Schließe alle übrigen Chrome-Fenster, öffne den Browser erneut und prüfe **`chrome://version`** noch einmal. Vergleiche mit der Tabelle die Version nach dem Neustart.
4. Liegt die Version weiterhin unter dem angekündigten Build, suche erneut nach einem verfügbaren Update. Verwaltet eine Organisation den Browser oder meldet das Update-Programm einen Fehler, wende dich an die zuständige Administration. Ein erfolgreicher Download beweist nicht, dass sich die laufende Browserversion geändert hat.

> **Erwartetes Ergebnis:** Nach dem Neustart entspricht der laufende Stable-Build von Chrome der für die Plattform genannten Version aus der Mitteilung vom 27. Oktober oder einer später vom Anbieter angekündigten Version. Eine ausstehende Schaltfläche „Neu starten“ ist kein Nachweis für den Abschluss.

Öffne unter **Android** den Play Store > Profilsymbol > Apps und Gerät verwalten und aktualisiere Chrome unter „Updates verfügbar“, falls das Update angeboten wird. Öffne in Chrome Mehr > Einstellungen > Über Chrome, um die installierte Version anzuzeigen. Vergleiche sie nach Abschluss des App-Updates mit der Android-Zeile. Diese Menüpfade entsprechen [Googles Android-Anleitung](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Verwaltete Geräteflotten prüfen

Nutze für registrierte Browser den **Chrome-Versionsbericht** in der Google Admin-Konsole, um ältere Builds nach Betriebssystem zu finden. Öffne die Ansicht Browser Versions, wähle die passende Organisationseinheit, prüfe die vollständige Nebenversion und exportiere die CSV-Datei, wenn du eine Geräteliste benötigst. Laut Google enthält der Bericht Browser, die in den vergangenen 28 Tagen einen Bericht gesendet haben. Google weist auf mögliche Verzögerungen hin, besonders bei großen Flotten. ([Details zu Chrome-Versionen ansehen](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Trenne den gemeldeten Bestand von der Live-Prüfung.** Prüfe den Zeitpunkt des letzten Berichts und den Kanal jedes Geräts. Bestätige Ausreißer anschließend direkt im Browser oder über dein verwaltetes Endpoint-Inventar. Google zählt getrennte Chrome-Installationen wie Stable und Beta separat. Browserberichte erfordern die Registrierung und [Berichte für verwaltete Browser](https://support.google.com/chrome/a/answer/9301421?hl=en). Ein Gerät, das im Bericht fehlt, ist kein Beleg für einen installierten Patch.

## Chromium-Abkömmlinge separat prüfen

**Die Chrome-Versionsübersicht gilt für Google Chrome.** Microsoft Edge, Brave und andere Chromium-basierte Browser haben eigene Pakete, Release-Nummern und Update-Zeitpläne. Die Chrome-Ankündigung bestätigt ihren Patch-Status nicht. Prüfe bei jedem Browser die installierte Version und die eigene Sicherheitsmitteilung oder die Release Notes zu den relevanten Chromium-Korrekturen. Vergleiche eine Edge- oder Brave-Version nicht direkt mit Chrome 156.0.8078.73 und erkläre sie dadurch für gepatcht.

Notiere für jeden abgeleiteten Browser den Produktnamen, Kanal, installierten Build, die URL der Anbieter-Mitteilung und den vom Anbieter genannten korrigierten Build. Hat der Anbieter keine Korrektur bestätigt, markiere den Status als **nicht verifiziert** und folge den Update-Anweisungen des Anbieters. Führe Chrome und die abgeleiteten Browser in getrennten Inventarzeilen.

## Quellen und Verweise

- [Chrome Releases: Stable-Channel-Update für Desktop, 27. Oktober 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Desktop-Builds, 52 Korrekturen, CVEs und Formulierung des Anbieters zur Offenlegung.
- [Chrome Releases: Chrome-Update für Android, 27. Oktober 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Android-Build und Hinweis zu den entsprechenden Desktop-Korrekturen.
- [Chromium-Issue-Tracker: M156-Suche nach Sicherheitskorrekturen](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Verlinkt aus der Desktop-Mitteilung. Der Zugriff auf einzelne Fehlerdetails hängt von den Offenlegungsbeschränkungen ab.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) und [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Beschreibungen der Schwachstellen und betroffene Chrome-Versionen. Die obigen Schweregrade entsprechen der Mitteilung von Google, nicht einer NVD-CVSS-Bewertung.
- [Google Chrome-Hilfe: Chrome auf Computern aktualisieren](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) und [unter Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Update-Prüfung und Menüpfade für die Versionsanzeige.
- [Chrome Enterprise-Hilfe: Chrome-Versionsdetails ansehen](https://support.google.com/chrome/a/answer/10025748?hl=en) und [Berichte für verwaltete Browser aktivieren](https://support.google.com/chrome/a/answer/9301421?hl=en). Voraussetzungen und Grenzen der Flottenberichte.
