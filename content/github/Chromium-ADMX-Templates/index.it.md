---
title: "ChromiumADMX: modello ADMX appropriato per il browser Chromium"
date: 2020-07-25
---


Modello ADMX corretto per il browser Chromium

Chromium, in quanto azienda, non è riuscita a rilasciare i modelli ADMX per il browser Chromium che potrebbero essere installati contemporaneamente ai modelli di Google Chrome.
Con questo in mente, abbiamo modificato i modelli ADMX di Google Chrome in modo che riflettano il percorso di registro del browser Chromium e li abbiamo inseriti in tantum nella cartella ADMX di Google nell'oggetto Criteri di gruppo.

**Queste definizioni dei criteri sono in uno stato pre-alfa. Dovrebbero essere utilizzati solo a scopo di test**

## Scarica i file richiesti

**Scarica i file richiesti dal file[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Appunti

Definizioni dei criteri di Google Chrome modificate in base a:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Nota:** sostituito "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" con "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\"

**Nota:** non installare i modelli Chromium e Brave Browser ADMX di SOS contemporaneamente.

## Come installare

1.) Copia tutti i file tranne readme.md in "C:\Windows\PolicyDefinitions" e/o "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Profitto?




