---
title: "Discord Cyber Scenario Bot: Wzmocnienie szkoleń i świadomości w zakresie cyberbezpieczeństwa"
date: 2023-02-22
toc: true
draft: false
description: "Odkryj, w jaki sposób CyberScenarioBot może podnieść poziom szkolenia w zakresie cyberbezpieczeństwa i programu podnoszenia świadomości na Discordzie, oferując quizy, scenariusze, śledzenie w tabeli liderów i potężne polecenia narzędziowe."
tags: ["Bot Discorda", "szkolenie w zakresie cyberbezpieczeństwa", "świadomość cyberbezpieczeństwa", "bot scenariusza", "bot quizowy", "tabela liderów", "polecenia narzędzi", "Docker", "Python", "testowanie automatyczne", "Discord API", "dokumentacja deweloperska", "wnoszący wkład", "Licencja MIT", "CyberScenarioBot", "CyberSentinels", "usprawnienie szkolenia", "program uświadamiający", "scenariusze cyberbezpieczeństwa", "środowisko serwera", "niestandardowe polecenia", "wdrażanie i zarządzanie", "quizy i scenariusze", "polecenia narzędzi", "polecenia informacyjne", "kwestie i wkład", "Aplikacja deweloperska Discord", "Dokumentacja Discord.py", "współpraca z deweloperami", "Społecznościowy serwer Discord"]
---


**CyberScenarioBot**

Discord Cyber Scenario, Quiz i Cyber Awareness Training Bot.

Możesz przejść do [🚀 Quick Start](#quick-start) dodać `CyberScenarioBot` na serwer.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Wprowadzenie

Ten bot może być przydatny w szkoleniu w zakresie cyberbezpieczeństwa lub programie uświadamiającym, w którym użytkownicy mogą być narażeni na różne scenariusze cyberbezpieczeństwa i dowiedzieć się, jak im zapobiegać lub reagować na nie. Korzystając z bota Discord, scenariusze można łatwo udostępniać użytkownikom w środowisku serwerowym, a bota można dostosować, aby zawierał dodatkowe polecenia lub funkcje w razie potrzeby. Ponadto bota można uruchomić w kontenerze Docker, co ułatwia jego wdrażanie i zarządzanie w różnych środowiskach.

[See the bot in action](https://discord.io/cybersentinels)

## 🚀 Szybki start

### Jak uruchomić:
#### Python:
Zakładając, że korzystasz z systemu Unix, otwórz terminal i przejdź do katalogu, w którym znajduje się skrypt bot.py. Następnie uruchom następujące polecenie:
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
Zauważ, że jeśli używasz systemu opartego na Windows, będziesz musiał użyć nieco innego polecenia, aby ustawić zmienną środowiskową. Oto przykładowe polecenie, które powinno działać w systemie Windows:
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
Podczas uruchamiania kontenera Docker można przekazać zmienną środowiskową BOT_TOKEN za pomocą flagi -e w następujący sposób:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Aby uruchomić bota w tle:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Aby uruchomić bota w tle ze wszystkimi zaplanowanymi monitami i rolami:
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

## Funkcje
**Dostępne polecenia**
Prefiks polecenia: '!', '/'*****

### 📝 **Komendy quizów i scenariuszy**
- **Aplus**: Odpowiada na pytania związane z CompTIA A+.
- **Bluescenario**: Odpowiedzi ze scenariuszem niebieskiego zespołu.
- **CCNA**: Odpowiedzi z podpowiedzią wielokrotnego wyboru Cisco CCNA.
- **CEH**: Odpowiedzi z monitem wielokrotnego wyboru CEH firmy EC-Council.
- **CISSP**: Odpowiada na pytanie wielokrotnego wyboru ISC2 CISSP.
- **Linuxplus**: Odpowiada z monitem wielokrotnego wyboru CompTIA Linux+.
- **Netplus**: Odpowiedzi z monitem związanym z CompTIA Network+.
- **Quiz**: Odpowiedzi z losowym pytaniem dotyczącym świadomości cyberbezpieczeństwa.
- **Redscenario**: Odpowiedzi ze scenariuszem redteam.
- **Secplus**: Odpowiedzi z pytaniami związanymi z CompTIA Security+.

#### 💯🎯 **Leaderboard**.
*Pytania wielokrotnego wyboru są dynamicznie ważone, podobnie jak na prawdziwych egzaminach, w zależności od tego, czy udzielono na nie poprawnej czy niepoprawnej odpowiedzi.

- Śledź swoje postępy w czasie i zobacz, jak wypadasz na tle innych osób na serwerze.
- Zobacz wyniki dla każdej kategorii quizu, a także ogólnie*

### 🛠️ **Komendy narzędzi**
- Dns**: Pobiera `domain name` i zwraca rekordy A, AAAA, NS, TXT itp.
- **Hash**: Pobiera `1 of 4 supported algos` oraz `string` i wyprowadza odpowiedni hash.
- **Ping**: Pobiera plik `IP address` i zwraca komunikat o powodzeniu i średnim opóźnieniu lub komunikat o niepowodzeniu.
- **Phonelookup**: Przyjmuje wartość `phone number` i wyświetla przewoźnika oraz lokalizację.
- **Shodanip**: Pobiera plik `IP address` i wysyła przydatne informacje z https://internetdb.shodan.io/.
- **Subnet**: Pobiera `IP address` oraz `Subnet Mask` i wyświetla zakres, użyteczne adresy IP, adres bramy, adres rozgłoszeniowy i liczbę obsługiwanych hostów.
- **Whois**: Pobiera `domain name` i wyświetla informacje whois domeny.

### ℹ️ **Komendy informacyjne**
- Polecenia**: Odpowiedzi z tą wiadomością.
- **Socials**: Odpowiedzi z różnych kont społecznościowych i stron internetowych bota.

### ⚙️ **Łatwa konfiguracja**
- Zobacz [🚀 Quick Start](#🚀-quick-start)

## Nadchodzące funkcje

Te funkcje mają zaplanowaną datę wdrożenia, ale śledzimy je i chcielibyśmy [contributions](#contributing) dla nich.

- Zaawansowane funkcje tabeli wyników, w tym rankingi tygodniowe i miesięczne.
- Konfigurowalne podpowiedzi i quizy dostosowane do konkretnych potrzeb szkoleniowych w zakresie cyberbezpieczeństwa.
- Zaawansowane raporty i analizy do śledzenia postępów i wydajności użytkowników.

## Użycie

CyberScenarioBot oferuje różne polecenia i funkcje w celu ulepszenia programu szkoleniowego i uświadamiającego w zakresie cyberbezpieczeństwa. Oto kilka typowych przypadków użycia:

1. **Quizy i scenariusze**: Użyj funkcji `/quiz` aby uzyskać losowe pytanie dotyczące świadomości cyberbezpieczeństwa. Używaj poleceń takich jak `/aplus` `/netplus` `/secplus` aby uzyskać dostęp do określonych monitów związanych z certyfikatami CompTIA. Użyj poleceń takich jak `/bluescenario` oraz `/redscenario` aby uzyskać odpowiednio scenariusze drużyny niebieskiej i czerwonej.

2. **Leaderboard**: Śledź postępy użytkowników i porównuj wyniki z innymi na swoim serwerze, odpowiadając na pytania quizowe i certyfikacyjne.

3. **Tool Commands**: Wykorzystanie różnych poleceń narzędziowych do wykonywania zadań związanych z DNS, haszowaniem, pingowaniem, wyszukiwaniem numeru telefonu, wyszukiwaniem IP Shodan, obliczaniem podsieci i wyszukiwaniem domeny WHOIS. Używaj poleceń takich jak `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` oraz `/whois` po którym następują odpowiednie argumenty.

4. **Komendy informacyjne**: Użyj polecenia `/commands` aby uzyskać listę dostępnych poleceń. Użyj polecenia `/socials` aby uzyskać informacje o kontach i stronach internetowych bota w mediach społecznościowych.

Zachęcamy do odkrywania i eksperymentowania z dostępnymi poleceniami, aby ulepszyć szkolenie w zakresie cyberbezpieczeństwa i zaangażować członków serwera.

## Problemy

Jeśli użytkownicy napotkają jakiekolwiek problemy lub mają sugestie dotyczące ulepszeń, mogą otworzyć zgłoszenie GitHub, aby je zgłosić. Zachęcamy użytkowników do podawania szczegółowych informacji na temat problemu i kroków do jego odtworzenia.

Aby otworzyć zgłoszenie, wykonaj następujące kroki:

1. Przejdź do zakładki Problemy w repozytorium GitHub projektu: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Kliknij przycisk "Nowy numer".
3. Podaj opisowy tytuł i jasny opis sprawy.
4. Dołącz wszelkie istotne dzienniki, zrzuty ekranu lub fragmenty kodu, aby pomóc w rozwiązywaniu problemów.
5. Prześlij zgłoszenie i czekaj na dalszą komunikację od opiekunów projektu.

## Wkład

Z zadowoleniem przyjmujemy każdy wkład.
Ten projekt miał być wysiłkiem rozwojowym i edukacyjnym podejmowanym przez [the CyberSentinels club](https://cybersentinels.org) Chętnie pomożemy i odpowiemy na wszelkie pytania.

### Zautomatyzowane testowanie w Pythonie

To repozytorium zawiera zautomatyzowane testowanie, możesz zobaczyć przykłady, jak to zaimplementować [here](https://github.com/CyberSentinels/penguin-pie)

### Discord API i dokumentacja dla deweloperów

Do testowania zmian i wdrażania funkcji będziesz potrzebować kilku rzeczy.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Współpraca z deweloperami

Wysiłki związane z rozwojem gry można omawiać na serwerze discord społeczności [here](https://discord.io/cybersentinels)
  
## Licencja

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
