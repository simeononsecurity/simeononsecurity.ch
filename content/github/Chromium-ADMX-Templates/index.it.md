---
title: "ChromiumADMX: Modello ADMX corretto per il browser Chromium"
date: 2020-07-25
---


Modello ADMX corretto per il browser Chromium

Chromium, come azienda, non ha rilasciato modelli ADMX per il browser Chromium che possono essere installati contemporaneamente ai modelli di Google Chrome.
Per questo motivo, abbiamo modificato i modelli ADMX di Google Chrome per riflettere il percorso del registro di Chromium Browser e li abbiamo inseriti nella cartella Google ADMX in GPO.

**Queste definizioni di criteri sono in uno stato pre-alfa. Devono essere utilizzate solo a scopo di test**

## Scaricare i file necessari

**Scaricare i file necessari dal sito [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Note

Modificate le Definizioni dei criteri di Google Chrome in base a:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Nota:** Sostituito "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" con "HKEY_LOCAL_MACHINE\Software\Policies\Chromium".

**Nota:** Non installare contemporaneamente i modelli ADMX di SOS Chromium e Brave Browser.

## Come installare

1.) Copiare tutti i file, tranne il file readme.md, in "C:\Windows\PolicyDefinitions" e/o "\\domain.tld\domain\Policies\PolicyDefinitions".

2.) Profitto?




