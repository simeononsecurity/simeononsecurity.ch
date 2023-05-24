---
title: "Best practice per la gestione dell'origine dell'ora nei domini Windows e nei computer autonomi"
draft: false
toc: true
date: 2023-05-23
description: "Scopri come impostare e gestire in modo efficace le origini dell'ora nei domini Windows e nei computer autonomi per garantire un'accurata sincronizzazione dell'ora ed evitare potenziali problemi."
tags: ["fonti temporali", "Dominio Windows", "macchine autonome", "sincronizzazione dell'ora", "cronometraggio accurato", "Server NTP", "controller di dominio", "Servizio ora di Windows", "errori di autenticazione", "incoerenze del file di registro", "problemi di replica", "configurazione dell'origine dell'ora", "gestione delle sorgenti orarie", "Sincronizzazione dell'ora di Windows", "migliori pratiche di cronometraggio", "configurazione dell'origine dell'ora", "sincronizzare l'ora del sistema", "Sincronizzazione dell'ora del dominio di Windows", "sincronizzazione dell'ora della macchina autonoma", "selezione della sorgente dell'ora", "risoluzione dei problemi relativi all'origine dell'ora", "errori di origine dell'ora", "problemi relativi all'origine dell'ora", "comandi di configurazione dell'origine dell'ora", "istruzioni per l'impostazione dell'origine dell'ora", "problemi di sincronizzazione dell'ora", "conseguenze della perdita di tempo", "prevenzione della deriva temporale", "risoluzione dell'errore di sincronizzazione dell'ora", "risoluzione dei problemi di sincronizzazione dell'ora", "gestione dell'origine dell'ora nei domini Windows", "gestione delle origini dell'ora in macchine Windows autonome", "prevenire perdite di tempo in ambienti Windows", "conseguenze degli errori di sincronizzazione dell'ora", "migliori pratiche per un cronometraggio accurato"]
cover: "/img/cover/An_image_depicting_a_clock_being_synchronized_with_a_domain.png"
coverAlt: "Un'immagine che raffigura un orologio sincronizzato con un controller di dominio e una macchina autonoma, che simboleggia la gestione dell'origine dell'ora e la sincronizzazione dell'ora accurata negli ambienti Windows."
coverCaption: ""
---

**Come impostare e gestire le origini dell'ora in un dominio Windows e su macchine Windows autonome**

La sincronizzazione dell'ora è fondamentale per mantenere timestamp accurati e garantire il corretto funzionamento dei sistemi in un dominio Windows o macchine Windows autonome. In questo articolo verranno illustrate le procedure consigliate per l'impostazione e la gestione delle origini dell'ora in entrambi gli scenari, evidenziando l'importanza dei membri del dominio che puntano ai controller di dominio. Esploreremo anche diverse opzioni per le fonti di tempo, sottolineando l'uso di pool NTP esterni o server di tempo basati su GPS per una precisione ottimale.

______

## Impostazione delle origini dell'ora in un dominio Windows

In un dominio Windows, è essenziale disporre di una sincronizzazione dell'ora coerente tra tutti i membri del dominio. La procedura consigliata consiste nel configurare i controller di dominio come origine dell'ora principale per i membri del dominio. In questo modo, ti assicuri che tutti i sistemi all'interno del dominio abbiano l'ora sincronizzata, che è fondamentale per l'autenticazione, la registrazione e varie operazioni del dominio.

### Opzioni di origine dell'ora per i controller di dominio

I controller di dominio possono ottenere l'ora da fonti diverse, tra cui l'orologio del BIOS, VMware Tools (in ambienti virtualizzati) o time server esterni. Sebbene l'utilizzo dell'orologio del BIOS o di VMware Tools possa essere conveniente, si consiglia di utilizzare una **sorgente strato 0 o 1** come un pool NTP esterno o un time server basato su GPS per una maggiore precisione.

#### Pool NTP esterni

I pool NTP esterni sono fonti affidabili e distribuite a livello globale per la sincronizzazione dell'ora. Sono costituiti da un gran numero di server NTP gestiti da organizzazioni e istituzioni in tutto il mondo. Configurando i controller di dominio per la sincronizzazione con i pool NTP esterni, è possibile garantire un cronometraggio accurato all'interno del dominio Windows.

Per configurare i controller di dominio in modo che utilizzino un pool NTP esterno, attenersi alla seguente procedura:

1. Aprire un prompt dei comandi con privilegi elevati nel controller di dominio.
2. Eseguire il seguente comando:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"pool.ntp.org" /reliable:yes /update
```

Questo comando configura il controller di dominio per la sincronizzazione con il pool NTP pool.ntp.org. Modificare il comando per utilizzare un pool NTP diverso o più origini, se lo si desidera.

3. Riavvia il servizio Ora di Windows per applicare le modifiche:

```shell
net stop w32time && net start w32time
```


#### Time server basati su GPS

Un'altra opzione per i controller di dominio consiste nell'utilizzare time server basati su GPS. Questi server si basano sui segnali GPS per fornire informazioni sull'ora altamente accurate. Impostando un time server basato su GPS ospitato localmente e configurando i controller di dominio per la sincronizzazione con esso, è possibile ottenere una sincronizzazione dell'ora precisa all'interno del dominio Windows.

### Configurazione dei membri del dominio

I membri del dominio, come i computer client e altri server, devono essere configurati per sincronizzare l'ora con i controller di dominio. Ciò garantisce che tutti i sistemi nel dominio rimangano sincronizzati ed eviti qualsiasi problema relativo al tempo.

Per configurare i membri del dominio in modo che sincronizzino l'ora con i controller di dominio, in genere non sono necessari passaggi aggiuntivi. Per impostazione predefinita, i membri del dominio sincronizzano automaticamente l'ora con i controller di dominio.

______

## Impostazione delle origini dell'ora su macchine Windows autonome

Sulle macchine Windows autonome che non fanno parte di un dominio, il processo di impostazione delle origini dell'ora può variare a seconda della versione di Windows e delle impostazioni internazionali. Per impostazione predefinita, le macchine Windows autonome in genere utilizzano **time.windows.com** come origine dell'ora principale. Tuttavia, vale la pena notare che il comportamento predefinito può essere modificato.

### Modifica dell'origine dell'ora su macchine autonome

Se desideri modificare l'origine dell'ora su un computer Windows autonomo, puoi seguire questi passaggi:

1. Aprire un prompt dei comandi con privilegi elevati sulla macchina.
2. Eseguire il seguente comando per configurare il server NTP:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" /update
```

Questo comando imposta time.windows.com come origine dell'ora per il computer autonomo. Modificare il comando per utilizzare un'origine dell'ora diversa, se lo si desidera.

3. Riavvia il servizio Ora di Windows per rendere effettive le modifiche:

```shell
net stop w32time && net start w32time
```


Eseguendo questi comandi, è possibile configurare una macchina Windows autonoma per sincronizzare l'ora con l'origine dell'ora desiderata.

______

## Conclusione

La corretta sincronizzazione dell'ora è vitale sia per i domini Windows che per le macchine autonome. In un dominio Windows, è fondamentale configurare i membri del dominio in modo che facciano riferimento ai controller di dominio per la sincronizzazione dell'ora. I controller di dominio possono ottenere l'ora da varie fonti, con l'utilizzo di pool NTP esterni o server dell'ora basati su GPS come pratica consigliata per una maggiore precisione.

Nei computer Windows autonomi, l'origine dell'ora predefinita è in genere time.windows.com. Tuttavia, è possibile modificare l'origine dell'ora utilizzando i comandi forniti.

Seguendo queste procedure consigliate e configurando le origini dell'ora appropriate, garantisci un cronometraggio accurato, un'autenticazione affidabile e una registrazione coerente all'interno del tuo ambiente Windows.

______

## Riferimenti

- [Microsoft Docs: How the Windows Time Service Works](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/how-the-windows-time-service-works)
- [Microsoft Docs: Windows Time Service Tools and Settings](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [NTP Pool Project](https://www.ntppool.org/)
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)

