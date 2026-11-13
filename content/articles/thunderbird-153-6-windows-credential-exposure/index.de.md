---
title: "Thunderbird 153.6: Offenlegung von NTLM-Anmeldedaten unter Windows und Update (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Zwei schwerwiegende Thunderbird-Schwachstellen legen NTLM-Authentifizierungsdaten unter Windows offen, wenn eine präparierte E-Mail angezeigt wird. Erfahre mehr über beide Wege, prüfe deine Version und begrenze ausgehendes SMB während des Updates."
genre: ["Cybersicherheit", "E-Mail-Sicherheit", "Windows-Sicherheit"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "Thunderbird-Sicherheitsupdate", "Thunderbird-Schwachstelle unter Windows", "Thunderbird-NTLM-Offenlegung", "Thunderbird-SMB-Authentifizierung", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "OpenPGP-Schlüsselanhang", "externer Anhang", "Blockieren externer Inhalte", "mailbox-URL", "erweiterter UNC-Pfad", "Windows-Kontoname", "NTLM-Authentifizierungsdaten", "Offenlegung von SMB-Anmeldedaten", "ausgehendes SMB", "TCP-Port 445", "E-Mail-Sicherheit", "Windows-Mailclient", "Thunderbird-Version prüfen", "Thunderbird aktualisieren", "NTLM-Relay", "Offline-Passwortknacken"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla hat zwei **schwerwiegende Schwachstellen zur Offenlegung von Windows-Anmeldedaten** in Thunderbird 153.6 behoben. Das Anzeigen einer präparierten E-Mail genügte, um eine der in [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/) beschriebenen Netzwerkanfragen auszulösen. Der Hinweis beschreibt eine mögliche Offenlegung von NTLM-Daten, keinen bestätigten Zugriff auf die Anmeldedaten jedes Empfängers.

<!--more-->

## Die wichtigsten Punkte

- **CVE-2026-118174** betraf einen extern gehosteten OpenPGP-Schlüsselanhang. Beim Anzeigen der Nachricht wurde ohne Benutzeraktion eine Anfrage ausgelöst, selbst wenn externe Inhalte blockiert waren.
- **CVE-2026-118176** betraf eine speziell präparierte `mailbox:`-URL mit einem erweiterten UNC-Pfad. Beim Anzeigen der Nachricht wurde eine SMB-Verbindung zu einem vom Absender gewählten Server aufgebaut.
- **Aktualisiere Thunderbird unter Windows** und prüfe die installierte Version. Der Hinweis nennt Thunderbird 153.6 als korrigierte Version. Die Thunderbird-Versionshinweise nennen den zugehörigen Build 153.6.0esr.

## Was die E-Mail auslöst

**Die beiden Schwachstellen haben unterschiedliche Einstiegspunkte.** Laut den Beschreibungen von Mozilla muss der Empfänger bei keiner davon auf einen Link in der E-Mail klicken. Das Risiko für Windows-Anmeldedaten hängt davon ab, ob eine Netzwerkanfrage eine vom Angreifer kontrollierte Freigabe erreicht und der anschließende Authentifizierungsaustausch stattfindet. Mozilla meldet in dem Hinweis keine aktive Ausnutzung.

| Problem | Auslöser beim Anzeigen der E-Mail | Risiko für Windows-Anmeldedaten |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird lädt den Inhalt eines OpenPGP-Schlüsselanhangs, um den Schlüsselimport anzubieten. Der Absender markiert ihn als externen Anhang mit einer vom Angreifer gewählten URL. | Eine URL zu einer Netzwerkfreigabe legt die NTLM-Anmeldedaten des Benutzers offen, wenn die Anfrage die Freigabe erreicht. |
| **CVE-2026-118176** | Ein erweiterter UNC-Pfad umgeht Thunderbirds Beschränkung für externe Freigaben in `mailbox:`-URLs. | Thunderbird verbindet sich mit einem vom Angreifer gewählten SMB-Server und gibt den Windows-Kontonamen sowie NTLM-Authentifizierungsdaten preis. |

Beim **OpenPGP-Anhang** sagt Mozilla ausdrücklich, dass die Anfrage die Sperre externer Inhalte umging und keine Benutzeraktion erforderte. Auf anderen Systemen als Windows ermöglichte das Problem ebenfalls eine externe Anfrage entgegen der Einstellung für externe Inhalte. Mozilla beschränkt die Offenlegung von NTLM-Anmeldedaten jedoch auf Windows. Beim **`mailbox:`-URL**-Weg sind laut Mozilla andere Betriebssysteme nicht betroffen. Siehe die einzelnen Einträge zu [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) und [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**NTLM-Authentifizierungsdaten sind kein Klartextpasswort.** Laut Mozilla bergen die über den SMB-Weg offengelegten Daten das Risiko von Offline-Passwortknacken oder Relay-Angriffen. Allein der Empfang einer präparierten Nachricht belegt keinen erfolgreichen Angriff. Der Hinweis führt auch andere Thunderbird-Schwachstellen auf, darunter separate Kalender- und RSS-Wege. Dieser Artikel behandelt die beiden Wege beim Anzeigen einer E-Mail und setzt nicht alle Probleme der Version gleich.

## Thunderbird prüfen und aktualisieren

Betroffen ist das **Lesen von E-Mails in Thunderbird unter Windows**, bevor die jeweilige Korrektur installiert wurde. Mozilla nennt **Thunderbird 153.6** als korrigierte Version, gibt für diese beiden Probleme aber keinen vollständigen Bereich der ältesten betroffenen Versionen an. Die [Versionshinweise zu 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) nennen einen ESR-Build, der am 27. Oktober 2026 veröffentlicht wurde. Leite den Patchstatus eines anderen Kanals, Forks oder neu gepackten Builds nicht allein aus dessen Versionsbezeichnung ab.

1. Öffne unter Windows **Help > About Thunderbird**. Lies die im About-Fenster angezeigte Version ab. Das Fenster sucht auch nach Updates. Mozillas [Update-Anleitung](https://support.mozilla.org/en-US/kb/updating-thunderbird) beschreibt diesen Weg.
2. Wenn ein Update verfügbar ist, lass Thunderbird es herunterladen und wähle **Restart Thunderbird to Update**. Öffne danach erneut **Help > About Thunderbird** und prüfe die installierte Version.
3. Vergleiche bei der **153-ESR-Reihe** die Version mit **153.6.0esr** in den Thunderbird-Versionshinweisen. Wenn deine Organisation Updates verwaltet, bitte die zuständige Administration, die Korrektur des Herstellers zu prüfen, statt von einem bereits installierten Update auszugehen.

> **Versionshinweis:** Die Versionshinweise zu 153.6.0esr bestätigen, dass der Build veröffentlicht wurde. MFSA 2026-122 ordnet die Sicherheitskorrekturen Thunderbird 153.6 zu. Die Versionshinweise beschreiben diese beiden CVEs nicht einzeln. Nutze den Sicherheitshinweis für die Schwachstellendetails.

## Risiko während des Updates senken

**Installiere zuerst die Korrektur des Herstellers.** Externe Inhalte zu deaktivieren stoppt CVE-2026-118174 allein nicht, da die beschriebene Anfrage die Einstellung umging. Die Empfehlung „nicht klicken“ reicht nicht aus. Mozilla beschreibt Anfragen, die beim Anzeigen der Nachricht ausgelöst werden.

Als **zusätzliche Schutzmaßnahme** solltest du ausgehendes SMB von Windows-Clients ins Internet einschließlich **TCP-Port 445** an der Unternehmensfirewall oder auf verwalteten Endgeräten einschränken. Microsofts [Hinweise zum SMB-Datenverkehr](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) empfehlen, ausgehendes TCP 445 ins Internet zu blockieren und den Zugriff auf erforderliche Dateiserver zu begrenzen. Erfasse benötigte Freigaben, bevor du eine Regel durchsetzt, besonders wenn deine Umgebung einen Cloud-Dateidienst oder externe Mitarbeitende nutzt. Diese Netzwerkkontrolle begrenzt den beschriebenen SMB-Weg, repariert Thunderbird aber nicht und behebt auch nicht jedes Problem mit externen Anfragen im Hinweis.

Wenn ein Windows-Gerät mit einer älteren Thunderbird-Version eine verdächtige Nachricht angezeigt hat, **behandle die Offenlegung als Frage zur Untersuchung, nicht als Beweis für eine Kompromittierung**. Prüfe gemeinsam mit dem Sicherheitsteam verfügbare Protokolle zu ausgehenden SMB-Verbindungen und Authentifizierungen. Der Herstellerhinweis enthält weder einen Expositionstest noch eine pauschale Anweisung, alle Passwörter zu ändern.

## Quellen

- [Mozilla Foundation Security Advisory 2026-122: In Thunderbird 153.6 behobene Sicherheitslücken](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Thunderbird Desktop-Versionshinweise: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support: Thunderbird auf die neueste Version aktualisieren](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: SMB-Datenverkehr in Windows Server absichern](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
