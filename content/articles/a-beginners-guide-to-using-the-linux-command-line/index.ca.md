---
title: "Guia per a principiants: utilitzar la línia d’ordres de Linux en ciberseguretat"
date: 2023-03-13
lastmod: 2026-11-22
toc: true
draft: false
description: "Aprèn a utilitzar la línia d’ordres de Linux en ciberseguretat amb ordres bàsiques i avançades."
tags: ["Linux", "Línia d’ordres", "Ciberseguretat", "Guia per a principiants", "Escaneig de xarxes", "Proves de vulnerabilitats", "Anàlisi de programari maliciós", "Permisos", "Trànsit de xarxa", "Estat dels processos", "Estadístiques de xarxa", "Cerca de fitxers", "Wireshark", "TCPDump", "Nmap", "CLI de Linux", "Seguretat", "Proves de penetració", "Anàlisi forense digital"]
cover: "/img/cover/a-beginners-guide-to-using-the-linux-command-line.webp"
coverAlt: "Il·lustració d’una pantalla amb ordres verdes de Linux sobre un fons fosc, envoltada de cadenats digitals i línies de xarxa."
coverCaption: ""
---

**Linux** és un sistema operatiu versàtil i segur, molt utilitzat en ciberseguretat perquè és de codi obert. Tot i això, als principiants els pot resultar difícil fer servir la interfície de línia d’ordres de Linux (CLI) per a tasques de ciberseguretat. Aquesta guia presenta ordres bàsiques i avançades de la CLI de Linux útils per a la ciberseguretat.

## Ordres bàsiques de Linux per a la ciberseguretat

### Mostrar el directori de treball

L’ordre **pwd** (mostra el directori de treball) mostra el directori de treball actual a la CLI. És el directori on et trobes dins del sistema de fitxers. L’ordre ajuda a navegar pel sistema i a saber on ets respecte dels altres directoris. Per exemple, si ets al directori personal i vols anar al directori de documents, fes servir aquestes ordres:

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

A l’exemple anterior, la primera ordre mostra el directori de treball actual, que és el directori personal. La segona canvia al directori de documents. La tercera mostra el nou directori de treball.

### Llistar el contingut

L’ordre **ls** mostra el contingut d’un directori a la CLI. Indica els noms dels fitxers i directoris del directori actual. Serveix per identificar què hi ha en una ubicació concreta. Per veure el contingut del directori de documents, fes servir aquesta ordre:

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

A l’exemple anterior, l’ordre llista el contingut del directori de documents, que conté tres fitxers: file1.txt, file2.pdf i file3.docx. També pots executar l’ordre sense arguments per llistar el contingut del directori actual. Per exemple:

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

A l’exemple anterior, l’ordre llista el contingut del directori personal, que inclou directoris com Desktop, Documents i Downloads.

### Canviar de directori

L’ordre **cd** (canvia de directori) canvia el directori de treball actual a la CLI. Et permet recórrer el sistema de fitxers i accedir a fitxers d’altres ubicacions. Per passar al directori de documents, fes servir aquesta ordre:

```bash
$ cd documents
```

A l’exemple anterior, l’ordre passa al directori de documents que hi ha dins del directori actual. També pots fer servir un camí absolut o relatiu per accedir a un directori que no sigui dins del directori actual. Per exemple:

```bash
$ cd /usr/local/bin
```

A l’exemple anterior, l’ordre passa a /usr/local/bin amb un camí absolut. També pots fer servir un camí relatiu. Per exemple:

```bash
$ cd ../..
```

A l’exemple anterior, l’ordre puja dos nivells des del directori actual. La notació ".." representa el directori pare i permet pujar per l’arbre de directoris.

### Concatenar fitxers

L’ordre **cat** (concatenate) mostra el contingut d’un fitxer a la CLI. Serveix per consultar fitxers de text, com ara registres o fitxers de configuració. Per veure el contingut d’un fitxer anomenat "file1.txt", fes servir aquesta ordre:

```bash
$ cat file1.txt
```

A l’exemple anterior, l’ordre mostra el contingut de "file1.txt". També la pots fer servir per concatenar diversos fitxers i mostrar-ne el contingut a la CLI. Per exemple:

```bash
$ cat file1.txt file2.txt file3.txt
```

A l’exemple anterior, l’ordre mostra el contingut de tres fitxers: file1.txt, file2.pdf i file3.docx. També pots fer servir comodins per concatenar tots els fitxers que coincideixin amb un patró. Per exemple:

```bash
$ cat *.txt
```

A l’exemple anterior, l’ordre mostra el contingut de tots els fitxers amb l’extensió ".txt" del directori actual. Això permet consultar diversos fitxers ràpidament sense obrir-los un per un.

### Cercar amb expressions regulars

L’ordre **grep** (impressió d’expressions regulars globals) cerca cadenes o patrons concrets en un fitxer o conjunt de fitxers des de la CLI. Serveix per trobar patrons als registres o informació concreta als fitxers de configuració. Per trobar totes les aparicions de la paraula "error" en un fitxer anomenat "logfile.txt", fes servir aquesta ordre:

```bash
$ grep "error" logfile.txt
```

A l’exemple anterior, l’ordre cerca totes les aparicions de "error" a "logfile.txt" i mostra les línies coincidents. També pots fer servir expressions regulars per cercar patrons més complexos. Per trobar línies amb una paraula que comença amb "p" i acaba amb "y", fes servir aquesta ordre:

```bash
$ grep "p.*y" logfile.txt
```

A l’exemple anterior, l’ordre cerca a "logfile.txt" línies amb una paraula que comença amb "p" i acaba amb "y". L’expressió regular "p.*y" coincideix amb qualsevol cadena que comenci amb "p" i acabi amb "y", amb qualsevol nombre de caràcters entremig. Aquesta ordre ajuda a trobar patrons als registres que poden indicar amenaces de seguretat o problemes de rendiment.

### Canviar els permisos

L’ordre **chmod** (canvia el mode) canvia els permisos d’un fitxer o directori des de la CLI. És essencial per protegir fitxers i directoris i controlar qui hi pot accedir. Tres dígits representen, respectivament, els permisos del propietari, del grup i de la resta d’usuaris. Els valors es calculen així:

```
4 = llegir
2 = escriure
1 = executar
```

Per exemple, per donar permisos de lectura i escriptura al propietari i només de lectura al grup i a la resta d’usuaris en un fitxer anomenat "file1.txt", fes servir aquesta ordre:

```bash
$ chmod 644 file1.txt
```

A l’exemple anterior, l’ordre estableix els permisos de "file1.txt" en 644. El primer dígit (6) representa lectura i escriptura per al propietari (4 + 2 = 6). El segon dígit (4) dona només lectura al grup. El tercer dígit (4) també dona només lectura a la resta d’usuaris.

També pots fer servir lletres per canviar els permisos. Per donar lectura i escriptura al propietari i al grup, i retirar tots els permisos a la resta d’usuaris en "file2.txt", fes servir aquesta ordre:

```bash
$ chmod ug=rw,o= file2.txt
```

A l’exemple anterior, l’ordre estableix els permisos de "file2.txt" en ug=rw,o=. "ug" representa el propietari i el grup, "r" representa lectura i "w" representa escriptura. El signe "=" vol dir que s’estableixen els permisos indicats, i "o=" retira tots els permisos a la resta d’usuaris. Aquesta ordre ajuda a controlar l’accés a fitxers i directoris sensibles i a impedir accessos no autoritzats.

## Ordres avançades de Linux per a la ciberseguretat

{{< figure src="linux-cli-advanced-security-commands-overview.webp" alt="Diagrama d’un terminal Linux amb nmap, netstat i find per escanejar xarxes, supervisar processos i investigar fitxers en tasques de ciberseguretat" >}}

### Mapatge de xarxes

L’ordre **nmap** és una eina potent d’escaneig de xarxes a la CLI. Permet identificar hosts i serveis d’una xarxa, així com possibles vulnerabilitats. Inclou diverses tècniques, com ara descobrir hosts, escanejar ports i detectar sistemes operatius.

Un ús bàsic de nmap és escanejar una adreça IP o un host. Per buscar ports oberts a l’adreça IP 192.168.1.1, fes servir aquesta ordre:

```bash
$ nmap 192.168.1.1
```

L’ordre anterior executa un escaneig TCP SYN contra la IP objectiu i retorna una llista de ports oberts. La sortida mostra els ports oberts, el servei de cada port i el seu estat (obert o tancat). De vegades també inclou informació addicional, com el sistema operatiu de l’objectiu.

Nmap també pot escanejar diversos hosts o adreces IP alhora. Per buscar ports oberts en un rang d’IP (192.168.1.1-255), fes servir aquesta ordre:

```bash
$ nmap 192.168.1.1-255
```

L’ordre anterior escaneja totes les adreces IP del rang i mostra els ports i serveis oberts de cada objectiu.

A més de descobrir hosts i escanejar ports, nmap pot detectar serveis i versions, identificar sistemes operatius i buscar vulnerabilitats. Aquests escanejos ajuden a trobar possibles debilitats d’una xarxa i a protegir-la dels atacs.

### Capturador de paquets TCP

L’ordre **tcpdump** captura i analitza el trànsit de xarxa des de la CLI. Serveix per resoldre problemes de xarxa, analitzar-ne el comportament i detectar possibles amenaces. Captura paquets en temps real i els pot filtrar segons criteris com l’adreça IP d’origen o de destinació, el protocol i el port.

Un ús bàsic de tcpdump és capturar tot el trànsit d’una interfície concreta. Per capturar el trànsit d’eth0, fes servir aquesta ordre:

```bash
$ sudo tcpdump -i eth0
```

L’ordre anterior captura tots els paquets d’eth0 i els mostra en temps real a la CLI. La sortida indica les adreces IP d’origen i destinació, el protocol i altra informació de cada paquet.

Tcpdump també filtra paquets segons diversos criteris. Per capturar tots els paquets enviats a una adreça IP concreta o rebuts d’aquesta adreça, fes servir aquesta ordre:

```bash
$ sudo tcpdump host 192.168.1.1
```

L’ordre anterior captura els paquets enviats a l’adreça IP 192.168.1.1 o rebuts d’aquesta adreça i els mostra en temps real. També pots filtrar per protocol (com TCP o UDP), número de port o altres criteris.

Tcpdump també pot desar paquets en un fitxer per analitzar-los més endavant. Per capturar tot el trànsit d’eth0 i desar-lo a "capture.pcap", fes servir aquesta ordre:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

L’ordre anterior captura els paquets d’eth0 i els desa en format pcap a "capture.pcap". Després es poden analitzar amb eines com Wireshark. Això ajuda a estudiar el comportament de la xarxa i detectar possibles amenaces.

### Estat dels processos

L’ordre **ps** mostra informació sobre els processos que s’executen en un sistema Linux des de la CLI. Serveix per detectar processos sospitosos que podrien comprometre la seguretat del sistema. Pot mostrar l’identificador del procés (PID), l’usuari, l’ús de CPU i memòria i el nom de l’ordre.

Un ús bàsic de ps és mostrar tots els processos en execució. Per fer-ho, fes servir aquesta ordre:

```bash
$ ps aux
```

L’ordre anterior mostra tots els processos en execució amb el PID, l’usuari, l’ús de CPU i memòria i el nom de l’ordre. Aquesta visió general ajuda a identificar processos sospitosos.

Ps també mostra informació d’un procés o grup concret. Per consultar un procés amb un PID específic, com ara 1234, fes servir aquesta ordre:

```bash
$ ps -p 1234
```

L’ordre anterior mostra la informació del procés amb PID 1234, inclosos l’usuari, l’ús de CPU i memòria i el nom de l’ordre. També pots indicar diversos PID per consultar un grup de processos.

Ps també pot supervisar l’estat dels processos en temps real. Per seguir l’ús de CPU i memòria d’un procés, com el PID 1234, fes servir aquesta ordre:

```bash
$ ps -p 1234 -o %cpu,%mem
```

L’ordre anterior mostra l’ús de CPU i memòria del procés amb PID 1234 i actualitza la sortida cada segon. Serveix per supervisar processos importants i detectar possibles colls d’ampolla de rendiment.

### Estadístiques de xarxa

L’ordre **netstat** mostra les connexions de xarxa actives d’un sistema Linux des de la CLI. Serveix per detectar connexions no autoritzades i possibles amenaces de seguretat. Pot mostrar adreces locals i remotes, el protocol utilitzat (com TCP o UDP) i l’estat de la connexió.

Un ús bàsic de netstat és mostrar totes les connexions de xarxa actives. Fes servir aquesta ordre:

```bash
$ netstat -a
```

L’ordre anterior mostra les connexions actives, amb les adreces locals i remotes, el protocol i l’estat. Aquesta visió general ajuda a detectar connexions no autoritzades.

Netstat també mostra connexions d’un protocol concret, com TCP. Per llistar totes les connexions TCP actives, fes servir aquesta ordre:

```bash
$ netstat -at
```

L’ordre anterior mostra les connexions TCP actives, les adreces locals i remotes i l’estat de cada connexió.

Netstat també mostra estadístiques d’un protocol concret. Per consultar les estadístiques de totes les connexions TCP, fes servir aquesta ordre:

```bash
$ netstat -st
```

L’ordre anterior mostra les estadístiques de les connexions TCP, com el nombre de connexions actives, les connexions en cada estat i el nombre d’errors. Serveix per supervisar l’estat general de la xarxa i detectar possibles problemes de rendiment.

### Cercar fitxers

L’ordre **find** cerca fitxers i directoris en un sistema Linux des de la CLI. Serveix per localitzar elements ocults o difícils de trobar. Permet cercar segons diversos criteris, com el nom, la mida, l’hora de modificació i els permisos.

Un ús bàsic de find és cercar pel nom. Per trobar tots els fitxers anomenats "example.txt" al directori actual i als seus subdirectoris, fes servir aquesta ordre:

```bash
$ find . -name example.txt
```

L’ordre anterior cerca els fitxers anomenats "example.txt" al directori actual i als seus subdirectoris i en mostra el camí complet.

Find també pot cercar per mida. Per trobar fitxers de més d’1 MB al directori actual i als subdirectoris, fes servir aquesta ordre:

```bash
$ find . -size +1M
```

L’ordre anterior cerca fitxers de més d’1 MB al directori actual i als seus subdirectoris i en mostra els camins complets.

A més del nom i la mida, find pot cercar segons l’hora de modificació i els permisos. Per trobar fitxers modificats durant els darrers set dies, fes servir aquesta ordre:

```bash
$ find . -mtime -7
```

L’ordre anterior cerca fitxers modificats durant els darrers set dies al directori actual i als seus subdirectoris i en mostra els camins complets.

Find és una eina potent per cercar fitxers i directoris segons diversos criteris. Serveix per a tasques d’administració de sistemes i ciberseguretat.

______

Fer servir la línia d’ordres de Linux per a ciberseguretat pot semblar aclaparador als principiants. Les ordres bàsiques i avançades d’aquesta guia t’ajudaran a aprofitar la CLI. Ves amb compte en executar ordres i entén què fa cadascuna abans de fer-la servir.

Per aprendre més sobre Linux en ciberseguretat, descarrega el sistema operatiu **[Kali Linux](https://www.kali.org/downloads/)**, dissenyat específicament per a proves de penetració i anàlisi forense digital.

## Conclusió

La interfície de línia d’ordres de Linux és una eina potent per als professionals de la ciberseguretat, però pot semblar difícil als principiants. Aprèn les ordres bàsiques i avançades d’aquesta guia per aprofitar la CLI. Ves sempre amb compte i entén què fa cada ordre abans d’executar-la. Amb pràctica i experiència, dominaràs la línia d’ordres de Linux i milloraràs les teves habilitats de ciberseguretat.
