---
title: "Handleiding voor beginners: Linux Command Line gebruiken voor cyberbeveiliging"
date: 2023-03-13
toc: true
draft: false
description: "Leer hoe u de Linux-opdrachtregel kunt gebruiken voor cyberbeveiliging met basis- en geavanceerde commando's."
tags: ["Linux", "Opdrachtregel", "Cyberbeveiliging", "Gids voor beginners", "Scannen van het netwerk", "Kwetsbaarheidstesten", "Analyse van malware", "Machtigingen", "Netwerkverkeer", "Processtatus", "Netwerkstatistieken", "Bestanden zoeken", "Wireshark", "TCPDump", "Nmap", "Linux CLI", "Beveiliging", "Penetratie testen", "Digitaal Forensisch Onderzoek"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_wearing_a_hoodie.png"
coverAlt: "Een cartoonillustratie van een persoon met een capuchon op, zittend voor een computerscherm waarop de Linux-opdrachtregelinterface zichtbaar is, en met een vergrootglas in de hand om het aspect cyberbeveiliging weer te geven."
coverCaption: ""
---

**Linux** is een veelzijdig en veilig besturingssysteem dat veel wordt gebruikt in de cyberbeveiligingsindustrie vanwege zijn open-source karakter. Het kan echter ontmoedigend zijn voor beginners om de Linux command line interface (CLI) te gebruiken om cybersecurity-taken uit te voeren. Deze gids is bedoeld om beginners een overzicht te geven van basis- en geavanceerde Linux CLI-commando's die nuttig zijn voor cyberbeveiligingsdoeleinden.

## Linux basiscommando's voor cyberbeveiliging

### Werkmap afdrukken

Het **pwd** (print working directory) commando wordt gebruikt om de huidige werkdirectory in de CLI weer te geven. De werkdirectory is de directory waar u zich momenteel bevindt in het bestandssysteem. Het commando is handig om door het bestandssysteem te navigeren en inzicht te krijgen in uw locatie ten opzichte van andere mappen. Als u zich bijvoorbeeld in de thuismap bevindt en u wilt naar de documentenmap navigeren, kunt u de volgende commando's gebruiken:

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

In het bovenstaande voorbeeld drukt het eerste commando de huidige werkdirectory af, die de thuismap is. Het tweede commando verandert de map in de map documenten, en het derde commando drukt de huidige werkmap af, die nu de map documenten is.

### Lijst

Het **ls** commando wordt gebruikt om de inhoud van een directory in de CLI op te sommen. Het commando toont de namen van de bestanden en mappen in de huidige werkmap. Het commando is handig voor het identificeren van de bestanden en mappen op een specifieke locatie. Als u bijvoorbeeld de inhoud van de map documenten wilt zien, kunt u het volgende commando gebruiken:

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

In het bovenstaande voorbeeld toont het commando de inhoud van de map documents, die drie bestanden bevat: file1.txt, file2.pdf, en file3.docx. U kunt het commando ook zonder argumenten gebruiken om de inhoud van de huidige werkdirectory te tonen. Bijvoorbeeld:

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

In het bovenstaande voorbeeld toont het commando de inhoud van de thuismap, die verschillende submappen bevat zoals Bureaublad, Documenten, Downloads, enzovoort.

### Directory wijzigen

Het **cd** (change directory) commando wordt gebruikt om de huidige werkdirectory in de CLI te wijzigen. Met dit commando kunt u door het bestandssysteem navigeren en bestanden op verschillende locaties openen. Als u bijvoorbeeld de huidige werkdirectory wilt veranderen in de documenten-directory, kunt u het volgende commando gebruiken:

```bash
$ cd documents
```

In het bovenstaande voorbeeld verandert het commando de huidige werkmap in de documentenmap, die zich in de huidige werkmap bevindt. U kunt de opdracht ook gebruiken met een absoluut of relatief pad om de werkdirectory te wijzigen in een directory die zich niet in de huidige werkdirectory bevindt. Bijvoorbeeld:

```bash
$ cd /usr/local/bin
```

In het bovenstaande voorbeeld verandert het commando de huidige werkmap in de map /usr/local/bin, wat een absoluut pad is. U kunt ook een relatief pad gebruiken om de werkdirectory te wijzigen. Bijvoorbeeld:

```bash
$ cd ../..
```


In het bovenstaande voorbeeld verandert het commando de huidige werkdirectory twee niveaus hoger dan de huidige werkdirectory. De ".." notatie staat voor de bovenliggende map, en u kunt deze gebruiken om omhoog te navigeren in de mapstructuur.


### Aaneenschakelen

Het **cat** (concatenate) commando wordt gebruikt om de inhoud van een bestand in de CLI weer te geven. Het commando is handig voor het bekijken van de inhoud van op tekst gebaseerde bestanden zoals logbestanden of configuratiebestanden. Als u bijvoorbeeld de inhoud van een bestand met de naam "file1.txt" wilt bekijken, kunt u het volgende commando gebruiken:

```bash
$ cat file1.txt
```

In het bovenstaande voorbeeld toont het commando de inhoud van het bestand "file1.txt". U kunt het commando ook gebruiken om meerdere bestanden aan elkaar te rijgen en de inhoud ervan in de CLI weer te geven. Bijvoorbeeld:

```bash
$ cat file1.txt file2.txt file3.txt
```


In het bovenstaande voorbeeld toont het commando de inhoud van drie bestanden: file1.txt, file2.txt, en file3.txt. U kunt de opdracht ook gebruiken met jokertekens om alle bestanden die aan een specifiek patroon voldoen aan elkaar te rijgen. Bijvoorbeeld:

```bash
$ cat *.txt
```

In het bovenstaande voorbeeld toont het commando de inhoud van alle bestanden met de extensie ".txt" in de huidige werkdirectory. Dit commando is handig om snel de inhoud van meerdere bestanden te bekijken zonder ze afzonderlijk te openen.


### Wereldwijde regelmatige expressie afdrukken

Met de opdracht **grep** (global regular expression print) kunt u in de CLI zoeken naar specifieke tekenreeksen of patronen in een bestand of een reeks bestanden. Het commando is handig voor het identificeren van patronen in logbestanden of het zoeken naar specifieke informatie in configuratiebestanden. Als u bijvoorbeeld wilt zoeken naar alle voorkomens van het woord "error" in een bestand met de naam "logfile.txt", kunt u het volgende commando gebruiken:

```bash
$ grep "error" logfile.txt
```

In het bovenstaande voorbeeld zoekt het commando naar alle voorkomens van het woord "error" in het bestand "logfile.txt" en toont de overeenkomende regels in de CLI. U kunt het commando ook gebruiken met reguliere expressies om te zoeken naar meer complexe patronen. Als u bijvoorbeeld wilt zoeken naar alle regels die een woord bevatten dat begint met "p" en eindigt met "y", kunt u het volgende commando gebruiken:

```bash
$ grep "p.*y" logfile.txt
```

In het bovenstaande voorbeeld zoekt de opdracht naar alle regels die een woord bevatten dat begint met "p" en eindigt met "y" in het bestand "logfile.txt". De reguliere uitdrukking "p.*y" komt overeen met elke tekenreeks die begint met "p" en eindigt met "y", met een willekeurig aantal tekens ertussen. Dit commando is handig voor het vinden van patronen in logbestanden die kunnen helpen bij het identificeren van beveiligingsrisico's of prestatieproblemen.


### Wijzig modus

Het **chmod** (change mode) commando wordt gebruikt om de rechten van een bestand of map in de CLI te wijzigen. Het commando is essentieel voor het beveiligen van bestanden en mappen en het controleren wie er toegang toe heeft. Machtigingen worden weergegeven door drie cijfers die respectievelijk overeenkomen met de eigenaar, groep en anderen. De cijfers worden berekend op basis van de volgende formule:

```
4 = read
2 = write
1 = execute
```

Als u bijvoorbeeld de eigenaar lees- en schrijfrechten wilt geven en de groep en anderen alleen-lezen rechten op een bestand met de naam "file1.txt", kunt u het volgende commando gebruiken:

```bash
$ chmod 644 file1.txt
```

In het bovenstaande voorbeeld stelt het commando de rechten van het bestand "file1.txt" in op 644. Het eerste cijfer (6) staat voor de machtigingen voor de eigenaar, namelijk lezen en schrijven (4 + 2 = 6). Het tweede cijfer (4) staat voor de machtigingen voor de groep, die alleen-lezen is. Het derde cijfer (4) staat voor de rechten voor anderen, die ook alleen-lezen zijn.

U kunt het commando ook met letters gebruiken om de rechten te wijzigen. Als u bijvoorbeeld de eigenaar en de groep lees- en schrijfrechten wilt geven en anderen geen rechten op een bestand met de naam "file2.txt", kunt u het volgende commando gebruiken:

```bash
$ chmod ug=rw,o= file2.txt
```

In het bovenstaande voorbeeld stelt het commando de rechten van het bestand "file2.txt" in op ug=rw,o=, waarbij "ug" staat voor de eigenaar en de groep, "r" voor leesrechten en "w" voor schrijfrechten. Het teken "=" betekent "stel de toestemmingen in op", en "o=" betekent "verwijder alle toestemmingen voor anderen". Dit commando is handig om de toegang tot gevoelige bestanden en mappen te controleren en ongeautoriseerde toegang te voorkomen.


## Geavanceerde Linux commando's voor cyberbeveiliging

### Network Mapper

Het **nmap** commando is een krachtig netwerkscanhulpmiddel in de CLI dat kan worden gebruikt om hosts en diensten op een netwerk en mogelijke kwetsbaarheden te identificeren. Het commando kan een reeks scantechnieken uitvoeren, waaronder host discovery, port scanning en operating system detection.

Een van de meest eenvoudige toepassingen van nmap is het scannen van een enkel IP-adres of host. Om bijvoorbeeld een enkel IP-adres (192.168.1.1) te scannen op open poorten, kunt u het volgende commando gebruiken:

```bash
$ nmap 192.168.1.1
```

Het bovenstaande commando voert een TCP SYN-scan uit tegen het doel-IP en geeft een lijst met open poorten. De uitvoer toont de open poorten samen met de dienst die op elke poort draait, de status van de poort (open/gesloten), en soms aanvullende informatie zoals het besturingssysteem dat op het doel draait.

Nmap kan ook worden gebruikt om meerdere hosts of IP-adressen tegelijk te scannen. Om bijvoorbeeld een reeks IP-adressen (192.168.1.1-255) te scannen op open poorten, kunt u het volgende commando gebruiken:

```bash
$ nmap 192.168.1.1-255
```

Het bovenstaande commando scant alle IP-adressen in het bereik en geeft de open poorten en diensten voor elk doel.

Naast basis host discovery en port scanning, kan nmap ook meer geavanceerde scans uitvoeren zoals service en versie detectie, OS detectie en vulnerability scanning. Deze scans kunnen nuttig zijn om potentiële beveiligingsproblemen op een netwerk te identificeren en het te beveiligen tegen mogelijke aanvallen.

### TCP-pakketdumper

Het **tcpdump** commando wordt gebruikt om netwerkverkeer vast te leggen en te analyseren in de CLI, waardoor het nuttig is voor het oplossen van netwerkproblemen, het analyseren van netwerkgedrag en het identificeren van potentiële veiligheidsbedreigingen. Het commando vangt pakketten in real-time op en kan pakketten filteren op basis van verschillende criteria, zoals bron of bestemming IP-adres, protocol en poort.

Een van de meest eenvoudige toepassingen van tcpdump is het vastleggen van al het netwerkverkeer op een specifieke interface. Om bijvoorbeeld al het verkeer op de interface eth0 vast te leggen, kunt u het volgende commando gebruiken:

```bash
$ sudo tcpdump -i eth0
```

Het bovenstaande commando vangt alle pakketten op de interface eth0 op en toont ze in real-time in de CLI. De uitvoer toont het bron- en doel-IP adres, het protocol en andere informatie over elk pakket.

Tcpdump kan ook gebruikt worden om pakketten te filteren op basis van verscheidene criteria. Om bijvoorbeeld alle pakketten vast te leggen die van of naar een specifiek IP-adres worden gestuurd, kunt u het volgende commando gebruiken:

```bash
$ sudo tcpdump host 192.168.1.1
```

Het bovenstaande commando vangt alle pakketten op die naar of van het IP-adres 192.168.1.1 worden verzonden en geeft ze in real-time weer in de CLI. U kunt ook pakketten filteren op basis van het protocol (bijv. TCP, UDP), het poortnummer of andere criteria.

Naast het vastleggen van pakketten in real-time, kan tcpdump ook worden gebruikt om pakketten vast te leggen in een bestand voor latere analyse. Om bijvoorbeeld alle pakketten op de interface eth0 vast te leggen en op te slaan in een bestand met de naam "capture.pcap", kan het volgende commando worden gebruikt:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

Het bovenstaande commando vangt alle pakketten op de interface eth0 op en slaat ze op in het bestand "capture.pcap" in pcap-formaat, dat later kan worden geanalyseerd met hulpmiddelen zoals Wireshark. Dit commando is nuttig voor het analyseren van netwerkgedrag en het identificeren van potentiële veiligheidsbedreigingen.

### Processtatus

De opdracht **ps** geeft in de CLI informatie weer over lopende processen op een Linux-systeem, wat nuttig is voor het identificeren van verdachte processen die mogelijk op een systeem draaien en de veiligheid ervan in gevaar kunnen brengen. Het commando kan een breed scala aan informatie over draaiende processen weergeven, waaronder hun proces-ID (PID), gebruiker, CPU- en geheugengebruik en opdrachtnaam.

Een van de meest eenvoudige toepassingen van ps is het weergeven van een lijst van alle draaiende processen op een systeem. Om bijvoorbeeld een lijst weer te geven van alle processen die op het systeem draaien, kunt u het volgende commando gebruiken:

```bash
$ ps aux
```

Het bovenstaande commando toont een lijst van alle draaiende processen op het systeem, samen met hun PID, gebruiker, CPU- en geheugengebruik en opdrachtnaam. Dit commando is handig om een algemeen beeld te krijgen van de processen die op een systeem draaien en om verdachte processen te identificeren.

Ps kan ook worden gebruikt om informatie weer te geven over een specifiek proces of een reeks processen. Om bijvoorbeeld informatie over een proces met een specifieke PID (bijvoorbeeld PID 1234) weer te geven, kunt u het volgende commando gebruiken:

```bash
$ ps -p 1234
```

Het bovenstaande commando toont informatie over het proces met PID 1234, inclusief de gebruiker, het CPU- en geheugengebruik en de opdrachtnaam. U kunt ook informatie over een reeks processen weergeven door meerdere PID's op te geven.

Naast het weergeven van informatie over lopende processen, kan ps ook worden gebruikt om de status van processen in real-time te controleren. Om bijvoorbeeld het CPU- en geheugengebruik van een specifiek proces (bijvoorbeeld PID 1234) in real-time te monitoren, kunt u het volgende commando gebruiken:

```bash
$ ps -p 1234 -o %cpu,%mem
```

Het bovenstaande commando toont het CPU- en geheugengebruik van het proces met PID 1234 in real-time, waarbij de uitvoer elke seconde wordt bijgewerkt. Dit commando is handig om de prestaties van kritieke processen te controleren en potentiële prestatieproblemen op te sporen.

### Netwerkstatistieken

De opdracht **netstat** toont informatie over actieve netwerkverbindingen op een Linux-systeem in de CLI, waardoor het nuttig is voor het identificeren van ongeautoriseerde netwerkverbindingen en potentiële veiligheidsbedreigingen. Het commando kan een breed scala aan informatie over actieve netwerkverbindingen weergeven, waaronder de lokale en externe adressen, het gebruikte protocol (bijv. TCP, UDP) en de status van de verbinding.

Een van de meest eenvoudige toepassingen van netstat is het weergeven van een lijst van alle actieve netwerkverbindingen op een systeem. Om bijvoorbeeld een lijst van alle actieve netwerkverbindingen weer te geven, kan het volgende commando gebruikt worden:

```bash
$ netstat -a
```


Het bovenstaande commando toont een lijst van alle actieve netwerkverbindingen op het systeem, samen met hun lokale en externe adressen, het gebruikte protocol en de status van de verbinding. Dit commando is handig om een algemeen beeld te krijgen van de actieve netwerkverbindingen op een systeem en om ongeautoriseerde verbindingen te identificeren.

Netstat kan ook worden gebruikt om informatie over netwerkverbindingen voor een specifiek protocol (bijvoorbeeld TCP) weer te geven. Om bijvoorbeeld een lijst van alle actieve TCP-verbindingen op het systeem weer te geven, kunt u het volgende commando gebruiken:

```bash
$ netstat -at
```

Het bovenstaande commando toont een lijst van alle actieve TCP-verbindingen op het systeem, samen met hun lokale en remote adressen, en de status van de verbinding.

Naast informatie over actieve netwerkverbindingen kan netstat ook worden gebruikt om netwerkstatistieken voor een specifiek protocol (bijvoorbeeld TCP) weer te geven. Om bijvoorbeeld statistieken over alle TCP-verbindingen op het systeem weer te geven, kan het volgende commando gebruikt worden:

```bash
$ netstat -st
```

Het bovenstaande commando toont statistieken over alle TCP-verbindingen op het systeem, inclusief het aantal actieve verbindingen, het aantal verbindingen in elke status en het aantal fouten dat is opgetreden. Dit commando is nuttig om de algemene gezondheid van het netwerk te controleren en potentiële prestatieproblemen op te sporen.


### Bestanden zoeken

Het **find** commando wordt gebruikt om bestanden en mappen op een Linux systeem te zoeken in de CLI, waardoor het handig is om specifieke bestanden en mappen te vinden die verborgen of moeilijk te vinden zijn. Het commando zoekt naar bestanden en mappen op basis van een groot aantal criteria, waaronder hun naam, grootte, wijzigingstijd en rechten.

Een van de meest elementaire toepassingen van find is het zoeken naar bestanden en mappen op naam. Om bijvoorbeeld te zoeken naar alle bestanden in de huidige directory en zijn submappen met de naam "example.txt", kunt u het volgende commando gebruiken:

```bash
$ find . -name example.txt
```

Het bovenstaande commando zoekt naar alle bestanden in de huidige directory en de submappen daarvan met de naam "example.txt", en geeft het volledige pad ervan weer.

Zoeken kan ook worden gebruikt om bestanden en mappen te zoeken op basis van hun grootte. Om bijvoorbeeld te zoeken naar alle bestanden in de huidige directory en zijn submappen die groter zijn dan 1 MB, kunt u het volgende commando gebruiken:

```bash
$ find . -size +1M
```

Het bovenstaande commando zoekt naar alle bestanden in de huidige directory en de submappen daarvan die groter zijn dan 1 MB, en toont het volledige pad.

Naast het zoeken naar bestanden en mappen op naam en grootte, kan find ook worden gebruikt om bestanden en mappen te zoeken op basis van hun wijzigingstijd en machtigingen. Om bijvoorbeeld te zoeken naar alle bestanden in de huidige directory en zijn submappen die in de afgelopen 7 dagen zijn gewijzigd, kunt u het volgende commando gebruiken:

```bash
$ find . -mtime -7
```

Het bovenstaande commando zoekt naar alle bestanden in de huidige directory en de submappen daarvan die in de afgelopen 7 dagen zijn gewijzigd, en toont het volledige pad.

In het algemeen is het commando find een krachtig hulpmiddel voor het zoeken naar bestanden en mappen op een Linux-systeem op basis van een groot aantal criteria, waardoor het nuttig is voor een groot aantal taken, waaronder systeembeheer en cyberbeveiliging.

______

Het gebruik van de Linux-opdrachtregel voor cyberbeveiliging kan voor beginners overweldigend zijn. Met de basis- en geavanceerde commando's die in deze gids worden beschreven, kunt u echter beginnen met het gebruik van de Linux CLI in uw voordeel bij cybersecurity. Denk eraan voorzichtig te zijn met het uitvoeren van commando's en goed te begrijpen wat elk commando doet voordat u het gebruikt.

Voor meer informatie over het gebruik van Linux voor cyberbeveiliging kunt u de ** downloaden[Kali Linux](https://www.kali.org/downloads/) besturingssysteem, dat speciaal is ontworpen voor penetratietesten en digitaal forensisch onderzoek.

## Conclusie

Concluderend, de Linux command line interface is een krachtig hulpmiddel voor cybersecurity professionals, maar het kan ontmoedigend zijn voor beginners. Door de basis- en geavanceerde commando's uit deze gids te leren, kunt u de Linux CLI in uw voordeel gebruiken bij cyberbeveiliging. Denk eraan altijd voorzichtig te zijn bij het uitvoeren van commando's en goed te begrijpen wat elk commando doet voordat u het gebruikt. Met oefening en ervaring kunt u zich bekwamen in het gebruik van de Linux-opdrachtregel en uw cyberbeveiligingsvaardigheden naar een hoger niveau tillen.