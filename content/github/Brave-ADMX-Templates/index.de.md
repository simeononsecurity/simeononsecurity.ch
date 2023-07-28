---
title: "Übernehmen Sie die Kontrolle über Brave-Browser-Richtlinien mit BraveADMX - Modifizierte ADMX-Vorlagen"
date: 2020-07-25
---


Das Unternehmen Brave hat es versäumt, ADMX-Vorlagen für den Brave-Browser zu veröffentlichen, so dass reine Registrierungen die einzige unterstützte Option sind.
Da der Brave-Browser auf Chromium aufbaut, sollte er die meisten, wenn nicht sogar alle Richtlinien der Chromium- und Google Chrome-ADMX-Vorlagen unterstützen.
Aus diesem Grund haben wir die Google Chrome ADMX-Vorlagen so geändert, dass sie den Registry-Pfad des Brave Browsers widerspiegeln. Nach einigen anfänglichen Fehlersuchen und Tests scheinen die Vorlagen zu funktionieren.

**Diese Policy-Definitionen befinden sich in einem Pre-Alpha-Stadium. Sie sollten nur zu Testzwecken verwendet werden**.

## Laden Sie die erforderlichen Dateien herunter.

**Downloaden Sie die erforderlichen Dateien von der [GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Anmerkungen

Geänderte Google Chrome Policy Definitions gemäß:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Hinweis:** Ersetzte "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" durch "HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave"

**Hinweis:** Installieren Sie SOS'es Chromium- und Brave-Browser-ADMX-Vorlagen nicht zur gleichen Zeit.

## Wie man installiert

1.) Kopieren Sie alle Dateien außer readme.md nach "C:\Windows\PolicyDefinitions" und/oder "\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Gewinn?