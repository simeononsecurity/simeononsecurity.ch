---
title: "Guida completa: Hashes di file in Windows con PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Imparate a ottenere gli hash dei file su Windows utilizzando PowerShell, compresi SHA256, MD5 e SHA1, con istruzioni ed esempi passo dopo passo."
tags: ["hash dei file", "PowerShell", "hash SHA256", "hash MD5", "hash SHA1", "integrità dei file", "autenticazione dei dati", "file verification", "algoritmi di hashing", "Sistema operativo Windows", "linguaggio di scripting", "shell a riga di comando", "sicurezza dei dati", "medicina legale digitale", "sicurezza informatica", "calcolo dell'hash", "manomissione dei file", "data integrity", "autenticità del file", "Sicurezza di Windows", "identificazione del file", "difesa informatica", "sicurezza dei file", "protezione dei dati", "data verification", "convalida dei file", "Windows PowerShell", "generazione di hash", "algoritmi di hash", "funzioni hash"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "Illustrazione a fumetti che mostra un file con il simbolo di un lucchetto e una lente di ingrandimento, a rappresentare la verifica e la sicurezza dell'hash dei file."
coverCaption: ""
---

**Come ottenere gli hash dei file in Windows utilizzando PowerShell**

Nell'ambito della sicurezza informatica, l'ottenimento degli hash dei file è un passo fondamentale per garantire l'integrità dei dati e verificare l'autenticità dei file. Gli hash sono identificatori unici generati per i file, che consentono agli utenti di rilevare i tentativi di manomissione e di convalidare l'integrità dei dati. In questa guida completa, esploreremo il processo per ottenere gli hash **SHA256**, **MD5** e **SHA1** dei file su Windows utilizzando il potente linguaggio di scripting **PowerShell**. Seguite le istruzioni passo-passo e fate un'immersione profonda in esempi specifici. Iniziamo!

______

## Ottenere hash su Windows con PowerShell

PowerShell, un versatile linguaggio di scripting e una shell a riga di comando per Windows, offre il cmdlet **Get-FileHash**, che consente agli utenti di calcolare l'hash di un file senza alcuno sforzo.

### Ottenere l'hash SHA256

Per ottenere l'hash **SHA256** di un file utilizzando PowerShell, seguite questi semplici passaggi:

1. Avviare PowerShell aprendo il **menu Start**, cercando **PowerShell** e selezionando **Windows PowerShell**.
2. Navigare nella directory in cui si trova il file. Utilizzare il comando `cd` seguito dal percorso della directory.
3. Eseguite il seguente comando per ottenere l'hash SHA256 del file:
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### Ottenere gli hash MD5 e SHA1
È possibile ottenere anche gli hash `MD5` e `SHA1` hash di un file utilizzando PowerShell. Utilizzate i seguenti comandi:

- Per ottenere i dati `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- Per ottenere il `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

Ricordate di sostituire "file_path" con il percorso del vostro file in entrambi i comandi.

## Esempi
Vediamo alcuni esempi specifici per illustrare il processo di ottenimento degli hash con PowerShell su Windows.

{{< youtube id="UrHhsF1q3rU" >}}

### Esempio 1: Ottenere l'hash SHA256
Immaginate di avere un file chiamato `document.pdf` che si trova nella directory `C:\Files` Per ottenere il `SHA256 hash` di questo file utilizzando PowerShell, eseguite il seguente comando:

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

L'output mostrerà il valore hash SHA256 del file.

### Esempio 2: Ottenere l'hash MD5

Si supponga di possedere un file chiamato `image.jpg` memorizzati nella directory `C:\Photos` Per ottenere il `MD5 hash` di questo file utilizzando PowerShell, eseguite il seguente comando:

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

Il terminale visualizzerà il valore hash MD5 del file.

### Esempio 3: Ottenere l'hash SHA1

Si consideri uno scenario in cui si ha un file chiamato `data.txt` che si trova nella directory `C:\Documents` Per ottenere il `SHA1 hash` di questo file utilizzando PowerShell, eseguite il seguente comando:

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

L'output mostrerà il valore hash SHA1 del file.