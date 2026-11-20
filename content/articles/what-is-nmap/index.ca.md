---
title: "Nmap: guia d’escaneig de xarxes i detecció de serveis"
date: 2023-06-13
lastmod: 2026-11-20
toc: true
draft: false
description: "Descobriu com utilitzar Nmap per escanejar xarxes i ports, detectar serveis i identificar sistemes operatius per avaluar la seguretat de la xarxa."
tags: ["nmap", "escaneig de xarxes", "avaluació de seguretat", "escaneig de ports", "detecció de serveis", "detecció del sistema operatiu", "motor de scripts de Nmap", "pirateria ètica", "seguretat de xarxes", "infraestructura de xarxa", "detecció de vulnerabilitats", "escaneig ping", "escaneig TCP SYN", "permís", "legalitat", "impacte a la xarxa", "escaneig dirigit", "protecció de dades", "CFAA", "GDPR", "mapatge de xarxes", "reconeixement de xarxes", "eines de seguretat de xarxa", "ciberseguretat", "eina de codi obert", "eina de línia d’ordres", "descobriment d’amfitrions", "intel·ligència de xarxa", "recollida d’informació", "vulnerabilitats de xarxa", "entorn de xarxa segur"]
cover: "/img/cover/Network_Security_Concept_with_Nmap_Scanning_Tools_in_a_3D.webp"
coverAlt: "Concepte de seguretat de xarxa amb eines d’escaneig Nmap en estil d’animació 3D."
coverCaption: ""
---

[**Què és Nmap i com s’utilitza?**](https://nmap.org/download.html)

[Nmap](https://nmap.org/download.html) (Network Mapper (mapador de xarxes)) és una eina de codi obert potent i versàtil per escanejar xarxes i descobrir amfitrions i serveis en una xarxa informàtica. Proporciona informació valuosa sobre la infraestructura de xarxa i ajuda a avaluar-ne la seguretat. Aquest article explica els conceptes bàsics de Nmap, les seves funcions i com utilitzar-lo amb eficàcia.

{{< youtube id="KVHSGWgVw-E" >}}

## Entendre Nmap

Nmap és una eina de línia d’ordres que funciona en diversos sistemes operatius, com ara Windows, Linux i macOS. Utilitza paquets IP en brut per determinar quins amfitrions hi ha disponibles en una xarxa, quins serveis ofereixen, quins sistemes operatius executen i altra informació útil.

Les seves nombroses funcions permeten a administradors de xarxa, professionals de seguretat i hackers ètics recopilar informació valuosa sobre una xarxa. Inclou:

1. **Descobriment d’amfitrions**: Nmap escaneja un interval d’adreces IP o una subxarxa concreta per trobar amfitrions actius. Utilitza tècniques com les sol·licituds d’eco ICMP, els escaneigs TCP SYN i les sol·licituds ARP.

2. **Escaneig de ports**: Nmap escaneja els ports oberts d’un amfitrió objectiu amb tècniques TCP SYN, connexió TCP, UDP i altres. Això mostra quins serveis s’executen i són accessibles.

3. **Detecció de serveis**: En examinar el trànsit i analitzar les respostes, Nmap identifica serveis als ports oberts. En alguns casos també en detecta la versió, informació útil per entendre les possibles vulnerabilitats.

4. **Detecció del sistema operatiu**: Nmap utilitza tècniques d’empremta digital per identificar el sistema operatiu d’un amfitrió objectiu. Analitza protocols i respostes de xarxa per fer-ne una estimació raonada.

5. **Scripts**: Nmap admet el motor de scripts de Nmap (NSE), que automatitza tasques i escaneigs avançats. El NSE inclou scripts per detectar vulnerabilitats, descobrir xarxes i més.

## Instal·lar Nmap

Per utilitzar Nmap, instal·leu-lo al vostre sistema. El procés depèn del sistema operatiu.

### Windows

Descarregueu Nmap des del lloc web oficial: [https://nmap.org/download.html](https://nmap.org/download.html). Trieu l’instal·lador adequat i seguiu l’assistent d’instal·lació.

### Linux

A la majoria de distribucions Linux, instal·leu Nmap amb el gestor de paquets. Obriu un terminal i executeu:

```shell
sudo apt-get install nmap
```
Substituïu apt-get pel gestor de paquets de la vostra distribució, si cal.

### macOS

A macOS, podeu instal·lar Nmap amb el gestor de paquets Homebrew. Obriu un terminal i executeu:

```shell
brew install nmap
```

## Escanejar amb Nmap

Un cop instal·lat Nmap, podeu escanejar la vostra xarxa per recopilar informació. Aquestes són algunes tècniques habituals:

1. **Escaneig ping**: La manera més senzilla de comprovar si els amfitrions estan connectats és fer un escaneig ping. Executeu:

```shell
nmap -sn <target>
```
Substituïu `<target>` per l’adreça IP o la subxarxa objectiu.

2. **Escaneig TCP SYN**: Aquest escaneig identifica els ports TCP oberts d’un amfitrió objectiu. Executeu:

```shell
nmap -sS <target>
```
Substituïu `<target>` per l’adreça IP o el nom d’amfitrió objectiu.

3. **Detecció de serveis i versions**: Per identificar els serveis dels ports oberts i les seves versions, executeu:

```shell
nmap -sV <target>
```

Substituïu `<target>` per l’adreça IP o el nom d’amfitrió objectiu.

4. **Detecció del sistema operatiu**: Per identificar el sistema operatiu d’un amfitrió objectiu, executeu:

```shell
nmap -O <target>
```
Substituïu `<target>` per l’adreça IP o el nom d’amfitrió objectiu.

Aquests són només alguns exemples de les opcions d’escaneig de Nmap. Consulteu la documentació oficial de Nmap per trobar tècniques i opcions més avançades.

## Bones pràctiques i consideracions

Quan utilitzeu Nmap, tingueu presents aquestes pràctiques i consideracions:

1. **Permís i legalitat**: Abans d’escanejar una xarxa, assegureu-vos que teniu autorització. L’escaneig no autoritzat pot ser il·legal i infringir normes com la Computer Fraud and Abuse Act (CFAA) dels Estats Units. Obteniu el permís del propietari de la xarxa o compliu les normes de la vostra jurisdicció.

2. **Impacte a la xarxa**: Els escaneigs de Nmap poden generar molt trànsit, sobretot els intensius. Tingueu en compte l’efecte sobre el rendiment i programeu-los en períodes de poc trànsit.

3. **Escaneig dirigit**: Eviteu escanejar xarxes indiscriminadament. Centreu-vos en objectius concrets i definiu l’abast de l’escaneig. Això redueix les interrupcions innecessàries i les alertes de seguretat.

4. **Protecció de dades**: Eviteu exposar informació sensible quan escanegeu xarxes. No recopileu ni deseu informació personal identificable (PII) ni dades confidencials. Compliu les normes de protecció de dades aplicables, com el Reglament general de protecció de dades (GDPR).

## Conclusió

Nmap és una eina d’escaneig de xarxes molt utilitzada que ofereix informació valuosa sobre la infraestructura i la seguretat de la xarxa. Si en compreneu els conceptes bàsics i seguiu les bones pràctiques, els administradors i professionals de seguretat podran avaluar vulnerabilitats, identificar riscos i mantenir un entorn de xarxa segur.

## Referències:

- Lloc web oficial de Nmap: [https://nmap.org/](https://nmap.org/)
- Baixada de Nmap: [https://nmap.org/download.html](https://nmap.org/download.html)
- Documentació oficial de Nmap: [https://nmap.org/book/man.html](https://nmap.org/book/man.html)
- Computer Fraud and Abuse Act (CFAA): [https://www.law.cornell.edu/uscode/text/18/part-I/chapter-47](https://www.law.cornell.edu/uscode/text/18/part-I/chapter-47)
- Reglament general de protecció de dades (GDPR): [https://gdpr.eu/](https://gdpr.eu/)
