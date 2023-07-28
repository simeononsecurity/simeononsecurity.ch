---
title: "ChromiumADMX: Geeignete ADMX-Vorlage für Chromium-Browser"
date: 2020-07-25
---


Geeignete ADMX-Vorlage für den Chromium-Browser

Das Unternehmen Chromium hat es versäumt, ADMX-Vorlagen für den Chromium-Browser zu veröffentlichen, die gleichzeitig mit den Google Chrome-Vorlagen installiert werden können.
Aus diesem Grund haben wir die ADMX-Vorlagen für Google Chrome so geändert, dass sie den Registrierungspfad des Chromium-Browsers widerspiegeln, und in Tandum im Google ADMX-Ordner im GPO abgelegt.

**Diese Richtliniendefinitionen befinden sich in einem Pre-Alpha-Stadium. Sie sollten nur zu Testzwecken verwendet werden**

## Download der erforderlichen Dateien

**Laden Sie die erforderlichen Dateien von der Seite [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Anmerkungen

Geänderte Google Chrome Policy Definitions gemäß:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Hinweis:** Ersetzte "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" durch "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\"

**Hinweis:** Installieren Sie SOS'es Chromium und Brave Browser ADMX-Vorlagen nicht gleichzeitig.

## So wird installiert

1.) Kopieren Sie alle Dateien außer readme.md nach "C:\Windows\PolicyDefinitions" und/oder "\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Gewinn?




