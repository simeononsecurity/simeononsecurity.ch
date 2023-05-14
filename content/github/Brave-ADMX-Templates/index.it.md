---
title: "Assumi il controllo delle policy di Brave Browser con BraveADMX - Modelli ADMX modificati"
date: 2020-07-25
---


Brave, come azienda, non è riuscita a rilasciare i modelli ADMX per il coraggioso sito del browser spingendo i registri puri come unica opzione supportata.
Poiché Brave Browser è basato su Chromium, dovrebbe supportare la maggior parte, se non tutte, le stesse politiche dei modelli Chromium e Google Chrome ADMX.
Con questo in mente, abbiamo modificato i modelli ADMX di Google Chrome per riflettere il percorso del registro di Brave Browser. Dopo alcuni test e risoluzione dei problemi iniziali, i modelli sembrano funzionare.

**Queste definizioni dei criteri sono in uno stato pre-alpha. Dovrebbero essere utilizzati solo a scopo di test**

## Scarica i file richiesti.

**Scarica i file richiesti dal file[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Appunti

Definizioni dei criteri di Google Chrome modificate in base a:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Nota:** Sostituito "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" con "HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave"

**Nota:** non installare i modelli Chromium e Brave Browser ADMX di SOS contemporaneamente.

## Come installare

1.) Copia tutti i file tranne readme.md in "C:\Windows\PolicyDefinitions" e/o "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Profitto?