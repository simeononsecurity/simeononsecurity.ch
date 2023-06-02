---
title: "Discord Cyber Scenario Bot: verbeter cyberbeveiliging training en bewustzijn"
date: 2023-02-22
toc: true
draft: false
description: "Ontdek hoe de CyberScenarioBot uw cyberbeveiligingstraining en -bewustzijnsprogramma op Discord kan verbeteren door het aanbieden van quizzen, scenario's, leaderboard tracking en krachtige toolcommando's."
tags: ["Discord bot", "cyberbeveiligingstraining", "cyberbeveiligingsbewustzijn", "scenario bot", "quiz bot", "leaderboard", "gereedschapscommando's", "Docker", "Python", "geautomatiseerd testen", "Discord API", "documentatie voor ontwikkelaars", "bijdragend", "MIT-licentie", "CyberScenarioBot", "CyberSentinels", "de opleiding verbeteren", "bewustwordingsprogramma", "cyberbeveiligingsscenario's", "serveromgeving", "aangepaste commando's", "inzetten en beheren", "quizzen en scenario's", "gereedschapscommando's", "informatieopdrachten", "problemen en bijdragen", "Discord ontwikkelaar toepassing", "Discord.py documentatie", "werken met ontwikkelaars", "community Discord server"]
---


**CyberScenarioBot**

Discord Cyber Scenario, Quiz, en Cyber Awareness Training Bot.

U kunt naar [🚀 Quick Start](#quick-start) toevoegen `CyberScenarioBot` naar uw server.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Introductie

Deze bot kan nuttig zijn in een cyberbeveiliging training of bewustwordingsprogramma, waar gebruikers kunnen worden blootgesteld aan verschillende cyberbeveiliging scenario's en leren hoe te voorkomen of te reageren op hen. Door het gebruik van een Discord bot, kunnen de scenario's gemakkelijk worden gedeeld met gebruikers in een server-omgeving, en de bot kan worden aangepast om extra commando's of functionaliteit op te nemen als dat nodig is. Bovendien kan de bot worden uitgevoerd in een Docker-container, waardoor hij gemakkelijk kan worden ingezet en beheerd in verschillende omgevingen.

[See the bot in action](https://discord.io/cybersentinels)

## 🚀 Quick Start

### Hoe uit te voeren:
#### Python:
Aangenomen dat u een Unix-systeem gebruikt, opent u een terminal en navigeert u naar de map waar het script bot.py staat. Voer dan het volgende commando uit:
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
Als u een op Windows gebaseerd systeem gebruikt, moet u een iets ander commando gebruiken om de omgevingsvariabele in te stellen. Hier is een voorbeeldcommando dat zou moeten werken onder Windows:
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
Wanneer u de Docker-container uitvoert, kunt u de BOT_TOKEN omgevingsvariabele doorgeven met de -e vlag als volgt:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Om de bot op de achtergrond te laten draaien:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Om de bot op de achtergrond te laten draaien met alle geplande prompts en rollen:
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

## Features
### Beschikbare commando's
*Commando voorvoegsel: '!', '/'*****

### 📝 **Quiz en Scenario opdrachten**
- **Aplus**: Antwoorden met CompTIA's A+ gerelateerde prompt.
- **Bluescenario**: Antwoorden met een blauw team scenario.
- **CCNA**: Antwoorden met Cisco's CCNA multiple choice prompt.
- **CEH**: Antwoorden met EC-Council's CEH multiple choice prompt.
- **CISSP**: Antwoorden met ISC2's CISSP multiple choice prompt.
- Linuxplus**: Antwoorden met CompTIA's Linux+ meerkeuze prompt.
- **Netplus**: Antwoorden met CompTIA's Network+ gerelateerde prompt.
- **Quiz**: Antwoorden met een willekeurige Cyber Security Awareness Vraag.
- **Redscenario**: Antwoorden met een redteam scenario.
- **Secplus**: Antwoorden met CompTIA's Security+ gerelateerde prompt.

#### 💯🎯 **Leaderboard**.
*Meerkeuzevragen worden dynamisch gewogen, net als bij de echte examens, op basis van het juiste of onjuiste antwoord*.

- *Volg uw vooruitgang in de tijd en zie hoe u zich verhoudt tot anderen in uw server*.
- *Zie scores voor elke testcategorie en in het algemeen*

### 🛠️ **Tool Commando's**
- **Dns**: Neemt een `domain name` en geeft A, AAAA, NS, TXT, etc. records terug.
- **Hash**: Neemt op in `1 of 4 supported algos` en een `string` en voert een overeenkomstige hash uit.
- **Ping**: Neemt een `IP address` en retourneert met een succesbericht en gemiddelde latentie of een foutbericht.
- **Phonelookup**: Neemt een `phone number` en geeft de drager en locatie door.
- **Shodanip**: Neemt een `IP address` en voert nuttige informatie uit van https://internetdb.shodan.io/.
- **Subnet**: Neemt een `IP address` en een `Subnet Mask` en geeft het bereik, de bruikbare IP's, het gateway-adres, het broadcast-adres en het aantal ondersteunde hosts.
- **Whois**: Neemt een `domain name` en voert domein whois informatie uit.

### ℹ️ **Informatieve commando's**
- **Commando's**: Antwoorden met dit bericht.
- **Socialen**: Antwoordt met de verschillende bot social media accounts en websites.

### ⚙️ **Eenvoudige installatie**
- *Zie [🚀 Quick Start](#🚀-quick-start)

## Upcoming Features

Deze functies hebben een geplande datum van implementatie, maar we volgen ze en we zouden graag [contributions](#contributing) voor hen.

- Geavanceerde leaderboard functies, inclusief wekelijkse en maandelijkse ranglijsten.
- Aanpasbare prompts en quizzen om tegemoet te komen aan specifieke cyberbeveiliging trainingsbehoeften.
- Geavanceerde rapportage en analyses voor het bijhouden van de voortgang en prestaties van gebruikers.

## Gebruik

De CyberScenarioBot biedt verschillende commando's en functies om uw cyberbeveiligingstraining en bewustwordingsprogramma te verbeteren. Hier zijn enkele veelvoorkomende gebruikssituaties:

1. **Quizzen en scenario's**: Gebruik de `/quiz` commando om een willekeurige cyberbeveiligingsvraag te krijgen. Gebruik commando's als `/aplus` `/netplus` `/secplus` om toegang te krijgen tot specifieke vragen over CompTIA-certificaten. Gebruik commando's als `/bluescenario` en `/redscenario` om respectievelijk blauw team en rood team scenario's te krijgen.

2. **Leaderboard**: Houd de voortgang van de gebruikers bij en vergelijk scores met anderen in uw server door de quiz en certificeringsvragen te beantwoorden.

3. **Tool Commands**: Gebruik verschillende tool commando's om taken uit te voeren met betrekking tot DNS, hashing, ping, telefoonnummer opzoeken, Shodan IP zoeken, subnet berekeningen, en domein WHOIS opzoeken. Gebruik commando's als `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` en `/whois` gevolgd door de juiste argumenten.

4. **Informatieve commando's**: Gebruik de `/commands` commando om een lijst van beschikbare commando's te krijgen. Gebruik de `/socials` commando om informatie te krijgen over de social media accounts en websites van de bot.

Voel je vrij om te verkennen en te experimenteren met de beschikbare commando's om je cyberbeveiligingstraining te verbeteren en je serverleden te betrekken.

## Issues

Als gebruikers problemen tegenkomen of suggesties hebben voor verbeteringen, kunnen ze een GitHub issue openen om ze te melden. Moedig gebruikers aan om gedetailleerde informatie over het probleem en de stappen om het te reproduceren te verstrekken.

Volg deze stappen om een issue te openen:

1. Ga naar de Issues tab op de GitHub repository van het project: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Klik op de knop "Nieuwe uitgave".
3. Geef een beschrijvende titel en een duidelijke beschrijving van de kwestie.
4. Voeg alle relevante logboeken, screenshots of stukjes code toe om te helpen bij het oplossen van problemen.
5. Dien het probleem in en wacht op verdere communicatie van de projectbeheerders.

## Bijdragen

We verwelkomen alle bijdragen.
Dit project was bedoeld als een ontwikkelings- en leerinspanning door [the CyberSentinels club](https://cybersentinels.org) en we helpen u graag om bij te dragen en eventuele vragen te beantwoorden.

### Geautomatiseerde Python Testen

Deze repo bevat geautomatiseerd testen, u kunt voorbeelden zien hoe dat te implementeren [here](https://github.com/CyberSentinels/penguin-pie)

### Discord API en Documentatie voor Ontwikkelaars

Voor het testen van veranderingen en het implementeren van functies heb je een paar dingen nodig.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Werken met de ontwikkelaars

U kunt ontwikkelingsinspanningen bespreken in de community discord server [here](https://discord.io/cybersentinels)
  
## License

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
