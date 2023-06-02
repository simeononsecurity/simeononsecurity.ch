---
title: "Discord-Cyber-Szenario-Bot: Schulung und Sensibilisierung für Cybersicherheit verbessern"
date: 2023-02-22
toc: true
draft: false
description: "Entdecken Sie, wie der CyberScenarioBot Ihr Cybersicherheitstraining und -sensibilisierungsprogramm auf Discord verbessern kann. Er bietet Quiz, Szenarien, Leaderboard-Tracking und leistungsstarke Tool-Befehle."
tags: ["Diskord-Bot", "Cybersicherheitsschulung", "Bewusstsein für Cybersicherheit", "Szenario-Bot", "Quiz-Bot", "Bestenliste", "Werkzeugbefehle", "Docker", "Python", "automatisierte Prüfung", "Diskord-API", "Entwicklerdokumentation", "Beitrag", "MIT-Lizenz", "CyberScenarioBot", "CyberSentinels", "die Ausbildung verbessern", "Aufklärungsprogramm", "Cybersicherheitsszenarien", "Serverumgebung", "benutzerdefinierte Befehle", "einsetzen und verwalten", "Quiz und Szenarien", "Werkzeugbefehle", "Informationsbefehle", "Themen und Beiträge", "Discord-Entwickleranwendung", "Discord.py Dokumentation", "Zusammenarbeit mit Entwicklern", "Community-Discord-Server"]
---


**CyberScenarioBot**

Discord Cyber Scenario, Quiz und Cyber Awareness Training Bot.

Sie können überspringen zu [🚀 Quick Start](#quick-start) zum Hinzufügen `CyberScenarioBot` auf Ihren Server zu übertragen.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Einleitung

Dieser Bot kann in einem Schulungs- oder Sensibilisierungsprogramm für Cybersicherheit nützlich sein, bei dem die Benutzer verschiedenen Cybersicherheitsszenarien ausgesetzt werden und lernen, wie sie diese verhindern oder darauf reagieren können. Durch die Verwendung eines Discord-Bots können die Szenarien leicht mit Benutzern in einer Serverumgebung geteilt werden, und der Bot kann nach Bedarf um zusätzliche Befehle oder Funktionen erweitert werden. Außerdem kann der Bot in einem Docker-Container ausgeführt werden, was die Bereitstellung und Verwaltung in verschiedenen Umgebungen erleichtert.

[See the bot in action](https://discord.io/cybersentinels)

## 🚀 Schnellstart

### Wie man es ausführt:
#### Python:
Wenn Sie ein Unix-basiertes System verwenden, öffnen Sie ein Terminal und wechseln Sie in das Verzeichnis, in dem sich das Skript bot.py befindet. Führen Sie dann den folgenden Befehl aus:
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
Wenn Sie ein Windows-basiertes System verwenden, müssen Sie einen etwas anderen Befehl verwenden, um die Umgebungsvariable zu setzen. Hier ist ein Beispielbefehl, der unter Windows funktionieren sollte:
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
Wenn Sie den Docker-Container ausführen, können Sie die Umgebungsvariable BOT_TOKEN mit dem Flag -e wie folgt übergeben:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Um den Bot im Hintergrund laufen zu lassen:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Um den Bot im Hintergrund mit allen geplanten Aufforderungen und Rollen laufen zu lassen:
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

## Funktionen
### **Vorhandene Befehle**
*Befehlspräfix: '!', '/'*****

### 📝 **Quiz- und Szenario-Befehle**
- **Aplus**: Antwortet mit der A+-bezogenen Aufforderung von CompTIA.
- **Bluescenario**: Antwortet mit einem Blue-Team-Szenario.
- **CCNA**: Antwortet mit der CCNA-Multiple-Choice-Aufforderung von Cisco.
- **CEH**: Antwortet mit der CEH-Multiple-Choice-Aufforderung von EC-Council.
- **CISSP**: Antwortet mit der CISSP-Multiple-Choice-Aufforderung von ISC2.
- **Linuxplus**: Antwortet mit der Linux+-Multiple-Choice-Abfrage von CompTIA.
- Netplus**: Antwortet mit der Network+-bezogenen Aufforderung von CompTIA.
- **Quiz**: Antwortet mit einer zufälligen Cyber Security Awareness-Frage.
- Rotes Szenario**: Antwortet mit einem Redteam-Szenario.
- **Secplus**: Antwortet mit einer CompTIA Security+-bezogenen Frage.

#### 💯🎯 **Leaderboard**
*Multiple-Choice-Fragen werden ähnlich wie bei den echten Prüfungen dynamisch gewichtet, je nachdem, ob sie richtig oder falsch beantwortet werden*.

- Verfolgen Sie Ihren Fortschritt im Laufe der Zeit und sehen Sie, wie Sie im Vergleich zu anderen auf Ihrem Server abschneiden.
- Ergebnisse für jede Quiz-Kategorie und für die Gesamtwertung*

### 🛠️ **Tool-Befehle**
- **Dns**: Nimmt eine `domain name` und liefert A-, AAAA-, NS-, TXT- usw. Datensätze.
- **Hash**: Nimmt auf `1 of 4 supported algos` und eine `string` und gibt einen entsprechenden Hashwert aus.
- **Ping**: Nimmt eine `IP address` und kehrt mit einer Erfolgsmeldung und der durchschnittlichen Latenzzeit oder einer Fehlermeldung zurück.
- **Phonelookup**: Nimmt eine `phone number` und gibt den Träger und den Standort aus.
- **Shodanip**: Nimmt eine `IP address` und gibt nützliche Informationen von https://internetdb.shodan.io/ aus.
- **Teilnetz**: Nimmt ein `IP address` und eine `Subnet Mask` und gibt den Bereich, die nutzbaren IPs, die Gateway-Adresse, die Broadcast-Adresse und die Anzahl der unterstützten Hosts aus.
- **Whois**: Nimmt eine `domain name` und gibt Domain-Whois-Informationen aus.

### ℹ️ **Informationsbefehle**
- **Befehle**: Antwortet mit dieser Nachricht.
- **Socials**: Antwortet mit den verschiedenen Social-Media-Konten und Websites des Bot.

### ⚙️ **Einfache Einrichtung**
- *Siehe [🚀 Quick Start](#🚀-quick-start)

## Kommende Funktionen

Diese Funktionen haben ein geplantes Implementierungsdatum, aber wir verfolgen sie und würden uns freuen [contributions](#contributing) für sie.

- Erweiterte Ranglistenfunktionen, einschließlich wöchentlicher und monatlicher Ranglisten.
- Individuell anpassbare Aufforderungen und Quizze, um den spezifischen Schulungsanforderungen im Bereich Cybersicherheit gerecht zu werden.
- Erweiterte Berichte und Analysen zur Verfolgung von Fortschritt und Leistung der Benutzer.

## Verwendung

Der CyberScenarioBot bietet verschiedene Befehle und Funktionen, um Ihr Programm zur Schulung und Sensibilisierung für Cybersicherheit zu verbessern. Hier sind einige häufige Anwendungsfälle:

1. **Quizzes und Szenarien**: Verwenden Sie den `/quiz` um eine zufällige Frage zum Thema Cybersicherheit zu erhalten. Verwenden Sie Befehle wie `/aplus` `/netplus` `/secplus` um auf spezifische Eingabeaufforderungen zuzugreifen, die sich auf CompTIA-Zertifizierungen beziehen. Verwenden Sie Befehle wie `/bluescenario` und `/redscenario` um Szenarien für das blaue bzw. rote Team zu erhalten.

2. **Leaderboard**: Verfolgen Sie den Fortschritt der Benutzer und vergleichen Sie die Ergebnisse mit anderen auf Ihrem Server, indem Sie die Quiz- und Zertifizierungsfragen beantworten.

3. **Tool-Befehle**: Verwenden Sie verschiedene Tool-Befehle, um Aufgaben im Zusammenhang mit DNS, Hashing, Ping, Telefonnummernabfrage, Shodan-IP-Suche, Subnetzberechnungen und WHOIS-Domänenabfrage durchzuführen. Verwenden Sie Befehle wie `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` und `/whois` gefolgt von den entsprechenden Argumenten.

4. **Informative Befehle**: Verwenden Sie die `/commands` um eine Liste der verfügbaren Befehle zu erhalten. Verwenden Sie den `/socials` Befehl, um Informationen über die Social-Media-Konten und Websites des Bots zu erhalten.

Experimentieren Sie ruhig mit den verfügbaren Befehlen, um Ihre Cybersicherheitsschulung zu verbessern und Ihre Servermitglieder einzubinden.

## Probleme

Wenn Benutzer auf Probleme stoßen oder Verbesserungsvorschläge haben, können sie einen GitHub-Problembericht erstellen, um sie zu melden. Ermutigen Sie die Benutzer, detaillierte Informationen über das Problem und die Schritte zur Reproduktion des Problems anzugeben.

Führen Sie die folgenden Schritte aus, um einen Fehler zu melden:

1. Gehen Sie zur Registerkarte "Probleme" im GitHub-Repository des Projekts: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Klicken Sie auf die Schaltfläche "Neue Ausgabe".
3. Geben Sie einen aussagekräftigen Titel und eine klare Beschreibung des Problems an.
4. Fügen Sie alle relevanten Protokolle, Screenshots oder Codeschnipsel hinzu, die bei der Fehlersuche helfen.
5. Reichen Sie das Problem ein und warten Sie auf weitere Mitteilungen von den Projektbetreuern.

## Beitragen

Wir begrüßen alle Beiträge.
Dieses Projekt ist als ein Entwicklungs- und Lernprojekt gedacht, das von [the CyberSentinels club](https://cybersentinels.org) und wir helfen Ihnen gerne dabei, Ihren Beitrag zu leisten und beantworten alle Ihre Fragen.

### Automatisierte Python-Tests

Dieses Repo enthält automatisierte Tests, Sie können Beispiele sehen, wie man das implementiert [here](https://github.com/CyberSentinels/penguin-pie)

### Discord API und Entwicklerdokumentation

Um Änderungen zu testen und Funktionen zu implementieren, benötigen Sie einige Dinge.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Zusammenarbeit mit den Entwicklern

Sie können die Entwicklungsarbeiten auf dem Community-Discord-Server diskutieren [here](https://discord.io/cybersentinels)
  
## Lizenz

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
