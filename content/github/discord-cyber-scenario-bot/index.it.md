---
title: "Discord Cyber Scenario Bot: migliorare la formazione e la consapevolezza della cybersecurity"
date: 2023-02-22
toc: true
draft: false
description: "Scoprite come CyberScenarioBot può elevare il vostro programma di formazione e sensibilizzazione sulla cybersicurezza su Discord, offrendo quiz, scenari, monitoraggio delle classifiche e potenti strumenti di comando."
tags: ["Bot di discordia", "formazione sulla cybersicurezza", "consapevolezza della cybersicurezza", "scenario bot", "quiz bot", "classifica", "comandi dello strumento", "Docker", "Pitone", "test automatizzati", "API Discord", "documentazione per sviluppatori", "contribuendo", "MIT license", "CyberScenarioBot", "CyberSentinelle", "migliorare la formazione", "programma di sensibilizzazione", "scenari di cybersicurezza", "ambiente server", "comandi personalizzati", "distribuire e gestire", "quiz e scenari", "comandi dello strumento", "comandi informativi", "temi e contributi", "Applicazione per sviluppatori Discord", "Documentazione Discord.py", "lavorare con gli sviluppatori", "server Discord della comunità"]
---


**CyberScenarioBot**

Discord Cyber Scenario, Quiz e Bot di formazione sulla consapevolezza informatica.

È possibile passare a [🚀 Quick Start](#quick-start) per aggiungere `CyberScenarioBot` al vostro server.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Introduzione

Questo bot può essere utile in un programma di formazione o di sensibilizzazione sulla cybersicurezza, in cui gli utenti possono essere esposti a vari scenari di cybersicurezza e imparare a prevenirli o a rispondervi. Utilizzando un bot Discord, gli scenari possono essere facilmente condivisi con gli utenti in un ambiente server e il bot può essere personalizzato per includere comandi o funzionalità aggiuntive, se necessario. Inoltre, il bot può essere eseguito in un container Docker, rendendolo facile da distribuire e gestire in vari ambienti.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀 Avvio rapido

### Come eseguire:
#### Python:
Se si utilizza un sistema basato su Unix, aprire un terminale e navigare nella directory in cui si trova lo script bot.py. Quindi, eseguire il seguente comando:
```bash
export BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
export GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes and leaderboard)"
export LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
export CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
export APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
export NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
export SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
export QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
Se si utilizza un sistema basato su Windows, è necessario utilizzare un comando leggermente diverso per impostare la variabile d'ambiente. Ecco un esempio di comando che dovrebbe funzionare su Windows:
```shell
set BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
set GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes)"
set LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
set APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
set NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
set SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
set QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
#### Docker:
Quando si esegue il contenitore Docker, è possibile passare la variabile d'ambiente BOT_TOKEN utilizzando il flag -e come segue:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Per eseguire il bot in background:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Per eseguire il bot in background con tutti i prompt e i ruoli programmati:
```bash
docker run -td --name scenario-bot \
-e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" \
-e GUILD_ID="INSERT YOUR GUILD ID HERE" \
-e LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE" \
-e LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE" \
-e CHANNEL_ID="INSERT YOUR CHANNEL ID HERE" \
-e APLUSROLE="INSERT YOUR A+ ROLE ID HERE" \
-e NETPLUSROLE="INSERT YOUR NET+ ROLE ID HERE" \
-e SECPLUSROLE="INSERT YOUR SEC+ ROLE ID HERE" \
-e QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE" \
simeononsecurity/discord-cyber-scenario-bot:latest
```

## Caratteristiche
### **Comandi disponibili**
*Prefisso del comando: '!', '/'*****

### 📝 **Comandi per quiz e scenari**
- **Aplus**: Risponde al prompt relativo ad A+ di CompTIA.
- **Bluescenario**: Risponde con uno scenario della squadra blu.
- **CCNA**: Risponde con la richiesta di scelta multipla CCNA di Cisco.
- **CEH**: Risponde con il prompt a scelta multipla CEH di EC-Council.
- **CISSP**: Risponde con la richiesta di scelta multipla CISSP di ISC2.
- **Linuxplus**: Risponde con il prompt a scelta multipla di Linux+ di CompTIA.
- **Netplus**: Risponde con il prompt relativo a Network+ di CompTIA.
- **Quiz**: Risponde con una domanda casuale di sensibilizzazione sulla sicurezza informatica.
- **Redscenario**: Risponde con uno scenario redteam.
- **Secplus**: Risponde con una domanda relativa a Security+ di CompTIA.

#### 💯🎯 **Leaderboard**
*Le domande a scelta multipla sono ponderate in modo dinamico, come negli esami reali, in base alle risposte corrette o errate*.

- Traccia i tuoi progressi nel tempo e vedi come ti confronti con gli altri nel tuo server.
- *Vedete i punteggi per ogni categoria di quiz e quelli complessivi*.

### 🛠️ **Comandi degli strumenti**
- **Dns**: Inserisce un file `domain name` e restituisce i record A, AAAA, NS, TXT, ecc.
- **Hash**: Prende in considerazione `1 of 4 supported algos` e un `string` e produce un hash corrispondente.
- **Ping**: Riceve un file `IP address` e restituisce un messaggio di successo e una latenza media o un messaggio di fallimento.
- **Phonelookup**: Riceve un file `phone number` e fornisce il vettore e la posizione.
- **Shodanip**: Riceve un `IP address` e produce informazioni utili da https://internetdb.shodan.io/.
- **Sottorete**: Riceve un file `IP address` e un `Subnet Mask` e fornisce l'intervallo, gli IP utilizzabili, l'indirizzo del gateway, l'indirizzo di broadcast e il numero di host supportati.
- **Whois**: Riceve un `domain name` e fornisce informazioni sul Whois del dominio.

### ℹ️ **Comandi informativi**
- Comandi**: Risponde con questo messaggio.
- **Socials**: Risponde con i vari account e siti web dei social media del bot.

### ⚙️ **Facile configurazione**
- *Vedi [🚀 Quick Start](#🚀-quick-start)

## Funzionalità in arrivo

Queste funzionalità hanno una data di implementazione pianificata, ma le stiamo monitorando e ci piacerebbe che [contributions](#contributing) per loro.

- Funzionalità avanzate di leaderboard, tra cui classifiche settimanali e mensili.
- Richieste e quiz personalizzabili per soddisfare le esigenze specifiche di formazione sulla cybersicurezza.
- Reportistica e analisi avanzate per monitorare i progressi e le prestazioni degli utenti.

## Utilizzo

CyberScenarioBot offre diversi comandi e funzioni per migliorare il vostro programma di formazione e sensibilizzazione sulla cybersicurezza. Ecco alcuni casi d'uso comuni:

1. **Quiz e scenari**: Utilizzate il `/quiz` per ottenere una domanda casuale sulla consapevolezza della cybersicurezza. Usate comandi come `/aplus` `/netplus` `/secplus` per accedere a richieste specifiche relative alle certificazioni CompTIA. Utilizzare comandi come `/bluescenario` e `/redscenario` per ottenere rispettivamente gli scenari della squadra blu e della squadra rossa.

2. **Leaderboard**: Tenete traccia dei progressi degli utenti e confrontate i punteggi con quelli degli altri utenti del vostro server rispondendo ai quiz e alle domande di certificazione.

3. **Comandi degli strumenti**: Utilizzate i vari comandi dello strumento per eseguire operazioni relative a DNS, hashing, ping, ricerca di numeri di telefono, ricerca IP Shodan, calcolo delle sottoreti e ricerca WHOIS dei domini. Utilizzare comandi come `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` e `/whois` seguito dagli argomenti appropriati.

4. **Comandi informativi**: Utilizzare il comando `/commands` per ottenere un elenco dei comandi disponibili. Utilizzare il comando `/socials` per ottenere informazioni sugli account dei social media e sui siti web del bot.

Sentitevi liberi di esplorare e sperimentare i comandi disponibili per migliorare la formazione sulla sicurezza informatica e coinvolgere i membri del server.

## Problemi

Se gli utenti riscontrano problemi o hanno suggerimenti per miglioramenti, possono aprire un problema su GitHub per segnalarli. Incoraggiate gli utenti a fornire informazioni dettagliate sul problema e sui passaggi per riprodurlo.

Per aprire un problema, seguire i seguenti passaggi:

1. Andate alla scheda Issues del repository GitHub del progetto: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Fare clic sul pulsante "Nuova emissione".
3. Indicare un titolo descrittivo e una descrizione chiara del problema.
4. Includere eventuali registri, schermate o frammenti di codice pertinenti per facilitare la risoluzione del problema.
5. Inviare il problema e attendere ulteriori comunicazioni da parte dei manutentori del progetto.

## Contribuire

Accogliamo con favore tutti i contributi.
Questo progetto è stato concepito come uno sforzo di sviluppo e di apprendimento da parte di [the CyberSentinels club](https://cybersentinels.org) e saremo lieti di aiutarvi a contribuire e di rispondere alle vostre domande.

### Test automatizzati su Python

Questo repo include test automatizzati, si possono vedere esempi su come implementarli [here](https://github.com/CyberSentinels/penguin-pie)

### API Discord e documentazione per gli sviluppatori

Per testare le modifiche e implementare le funzionalità, sono necessari alcuni elementi.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Lavorare con gli sviluppatori

È possibile discutere degli sforzi di sviluppo nel server discord della comunità [here](https://discord.gg/CYVe2CyrXk)
  
## Licenza

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
