---
title: "Scenariul cibernetic Discord Bot: Îmbunătățiți formarea și conștientizarea securității cibernetice"
date: 2023-02-22
toc: true
draft: false
description: "Descoperiți modul în care CyberScenarioBot vă poate îmbunătăți programul de instruire și conștientizare în domeniul securității cibernetice pe Discord, oferind teste, scenarii, urmărire a clasamentului și comenzi puternice de instrumente."
tags: ["Discord bot", "formare în domeniul securității cibernetice", "conștientizarea securității cibernetice", "scenariu bot", "test bot", "clasament", "comenzi de instrumente", "Docker", "Python", "testare automată", "API Discord", "documentația dezvoltatorului", "contribuind", "Licență MIT", "CyberScenarioBot", "CyberSentinels", "îmbunătățirea formării", "program de conștientizare", "scenarii de securitate cibernetică", "mediul serverului", "comenzi personalizate", "să implementeze și să gestioneze", "teste și scenarii", "comenzi de instrumente", "comenzi informative", "probleme și contribuții", "Aplicație pentru dezvoltator Discord", "Documentație Discord.py", "colaborarea cu dezvoltatorii", "serverul Discord al comunității"]
---


**CyberScenarioBot**

Scenariu cibernetic Discord, chestionar și robot de formare a conștientizării cibernetice.

Puteți sări la [🚀 Quick Start](#quick-start) pentru a adăuga `CyberScenarioBot` pe serverul dvs. acum.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Introducere

Acest robot poate fi util în cadrul unui program de formare sau de conștientizare în domeniul securității cibernetice, în care utilizatorii pot fi expuși la diverse scenarii de securitate cibernetică și pot învăța cum să le prevină sau să le răspundă. Prin utilizarea unui bot Discord, scenariile pot fi ușor partajate cu utilizatorii într-un mediu de server, iar botul poate fi personalizat pentru a include comenzi sau funcționalități suplimentare, după cum este necesar. În plus, botul poate fi rulat într-un container Docker, ceea ce îl face ușor de implementat și de gestionat în diverse medii.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀 Start rapid

### Cum se execută:
#### Python:
Presupunând că folosiți un sistem bazat pe Unix, deschideți un terminal și navigați în directorul în care se află scriptul bot.py. Apoi, rulați următoarea comandă:
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
Rețineți că, dacă utilizați un sistem bazat pe Windows, va trebui să utilizați o comandă ușor diferită pentru a seta variabila de mediu. Iată un exemplu de comandă care ar trebui să funcționeze pe Windows:
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
La rularea containerului Docker, puteți introduce variabila de mediu BOT_TOKEN folosind steagul -e, după cum urmează:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Pentru a rula robotul în fundal:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Pentru a rula robotul în fundal cu toate solicitările și rolurile programate:
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

## Caracteristici
### **Comenzi disponibile**
*Prefixul comenzii: '!', '/'*****

### 📝 **Comandă pentru chestionare și scenarii**
- **Aplus**: Răspunde cu promptul legat de CompTIA A+.
- **Bluescenario**: Răspunde cu un scenariu al echipei albastre.
- **CCNA**: Răspunde cu răspunsul cu alegere multiplă al Cisco CCNA.
- **CEH**: Răspunde cu răspunsul cu alegere multiplă CEH al EC-Council.
- **CISSP**: Răspunde la întrebarea cu alegere multiplă CISSP de la ISC2.
- **Linuxplus**: Răspunde la întrebarea cu alegere multiplă Linux+ de la CompTIA.
- **Netplus**: Răspunde la întrebarea referitoare la CompTIA Network+.
- **Quiz**: Răspunde cu o întrebare aleatorie de conștientizare a securității cibernetice.
- **Redscenario**: Răspunde cu un scenariu redteam.
- **Secplus**: Răspunde cu o întrebare legată de CompTIA Security+.

#### 💯🎯🎯 **Leaderboard**
*Întrebările cu alegere multiplă sunt ponderate dinamic, similar cu examenele reale, în funcție de răspunsul corect sau incorect*.

- *Să vă urmăriți progresul în timp și să vedeți cum vă comparați cu ceilalți din serverul dvs.
- *Vezi scorurile pentru fiecare categorie de teste, precum și cele generale*

### 🛠️ **Comandă de instrumente**
- **Dns**: Preia un `domain name` și returnează înregistrări A, AAAA, NS, TXT etc.
- **Hash**: Primește `1 of 4 supported algos` și un `string` și produce un hash corespunzător.
- **Ping**: Primește un fișier `IP address` și se întoarce cu un mesaj de succes și cu o latență medie sau cu un mesaj de eșec.
- **Phonelookup**: Primește un fișier `phone number` și emite purtătorul și locația.
- **Shodanip**: Primește un `IP address` și furnizează informații utile de pe https://internetdb.shodan.io/.
- **Subnet**: Primește un `IP address` și un `Subnet Mask` și afișează intervalul, IP-urile utilizabile, adresa Gateway, adresa de difuzare și numărul de gazde acceptate.
- **Whois**: Primește un `domain name` și produce informații whois despre domenii.

### ℹ️ **Comandă informațională**
- **Comande**: Răspunde cu acest mesaj.
- **Comunicări**: Răspunde cu diferitele conturi de socializare și site-uri web ale botului.

### ⚙️ **Configurare ușoară**
- *Vezi [🚀 Quick Start](#🚀-quick-start)

## Caracteristici viitoare

Aceste caracteristici au o dată planificată de implementare, dar le urmărim și ne-ar plăcea să le urmărim [contributions](#contributing) pentru ei.

- Funcții avansate de clasament, inclusiv clasamente săptămânale și lunare.
- Întrebări și chestionare personalizabile pentru a răspunde nevoilor specifice de formare în domeniul securității cibernetice.
- Rapoarte și analize avansate pentru urmărirea progresului și a performanțelor utilizatorilor.

## Utilizare

CyberScenarioBot oferă diverse comenzi și caracteristici pentru a vă îmbunătăți programul de instruire și conștientizare în domeniul securității cibernetice. Iată câteva cazuri comune de utilizare:

1. **Chestionare și scenarii**: Utilizați `/quiz` pentru a primi o întrebare aleatorie de conștientizare a securității cibernetice. Utilizați comenzi precum `/aplus` `/netplus` `/secplus` pentru a accesa solicitări specifice legate de certificările CompTIA. Utilizați comenzi precum `/bluescenario` și `/redscenario` pentru a obține scenariile echipei albastre și, respectiv, echipei roșii.

2. **Liderboard**: Țineți evidența progresului utilizatorilor și comparați scorurile cu ale altora din serverul dvs. răspunzând la întrebările de testare și certificare.

3. **Comandă de instrumente**: Utilizați diverse comenzi de instrumente pentru a efectua sarcini legate de DNS, hashing, ping, căutarea numerelor de telefon, căutarea Shodan IP, calcularea subrețelelor și căutarea WHOIS a domeniului. Utilizați comenzi precum `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` și `/whois` urmată de argumentele corespunzătoare.

4. **Comandă informațională**: Folosiți butonul `/commands` pentru a obține o listă a comenzilor disponibile. Utilizați comanda `/socials` pentru a obține informații despre conturile de socializare și site-urile web ale robotului.

Nu ezitați să explorați și să experimentați cu comenzile disponibile pentru a vă îmbunătăți instruirea în domeniul securității cibernetice și pentru a implica membrii serverului dvs.

## Probleme

Dacă utilizatorii întâmpină probleme sau au sugestii de îmbunătățire, pot deschide o problemă GitHub pentru a le raporta. Încurajați utilizatorii să furnizeze informații detaliate despre problemă și pașii pentru a o reproduce.

Pentru a deschide o problemă, urmați acești pași:

1. Accesați fila Issues (Probleme) din depozitul GitHub al proiectului: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Dați clic pe butonul "New Issue".
3. Furnizați un titlu descriptiv și o descriere clară a problemei.
4. Includeți orice jurnale, capturi de ecran sau fragmente de cod relevante pentru a vă ajuta la depanare.
5. Trimiteți problema și așteptați o comunicare ulterioară din partea responsabililor de proiect.

## Contribuție

Salutăm toate contribuțiile.
Acest proiect a fost conceput ca un efort de dezvoltare și învățare de către [the CyberSentinels club](https://cybersentinels.org) și ne-ar face plăcere să vă ajutăm să contribuiți și să vă răspundem la orice întrebare pe care o aveți.

### Testare automată Python

Acest repo include testarea automată, puteți vedea exemple despre cum să implementați asta [here](https://github.com/CyberSentinels/penguin-pie)

### Discord API și documentația pentru dezvoltatori

Pentru testarea modificărilor și implementarea funcțiilor, veți avea nevoie de câteva lucruri.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Lucrul cu dezvoltatorii

Puteți discuta eforturile de dezvoltare pe serverul discord al comunității [here](https://discord.gg/CYVe2CyrXk)
  
## Licență

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
