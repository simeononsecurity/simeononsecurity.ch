---
title: "Com crear un llac de dades al núvol segur i conforme"
date: 2023-04-16
lastmod: 2026-11-07
toc: true
draft: false
description: "Aprèn les millors pràctiques de seguretat i compliment normatiu en planificar, crear i gestionar llacs de dades al núvol."
tags: ["llac de dades", "seguretat al núvol", "normativa de compliment", "controls d'accés", "xifratge", "AWS", "Azure", "HIPAA", "GDPR", "supervisió", "aplicació de pedaços", "ciberseguretat", "solució SIEM", "equips de suport informàtic", "panorama d'amenaces", "migració al núvol", "governança del núvol"]
cover: "/img/cover/a-guide-to-building-a-secure-and-compliant-cloud-based-data-lake.webp"
coverAlt: "Il·lustració digital d’un llac de dades al núvol amb fluxos de dades blaus i verds intensos, envoltat d’elements de seguretat abstractes sobre un fons fosc."
coverCaption: ""
---

**Guia per crear un llac de dades al núvol segur i conforme**

Un llac de dades al núvol és una eina útil per emmagatzemar i analitzar conjunts de dades grans. Tanmateix, presenta reptes de seguretat específics que cal abordar per complir les normatives governamentals. En aquesta guia parlarem de les millors pràctiques per crear un llac de dades al núvol segur i conforme.

## Planificar el llac de dades

Abans de crear un llac de dades, **és essencial preparar un pla que tingui en compte els requisits de seguretat i compliment normatiu de la teva organització**. Comença amb un marc de treball que segueixi estàndards del sector, com ara el Reglament general de protecció de dades (GDPR) o la Health Insurance Portability and Accountability Act (HIPAA).

Tria un proveïdor de núvol adequat, amb experiència demostrada en solucions segures que compleixin aquestes normatives. Alguns dels proveïdors més populars són Amazon Web Services (AWS), Microsoft Azure i Google Cloud Platform.

**Defineix també controls d’accés clars** per als usuaris, els rols i els permisos. Inclou-hi els membres de l’equip intern i també els proveïdors o socis externs que necessitin accés puntualment.

## Crear el llac de dades

Quan creïs el llac de dades, **incorpora el xifratge i els controls d’accés des del disseny** en totes les fases del moviment de dades cap al llac, dins del llac i des del llac. Els processos d’ingesta haurien de xifrar les dades en trànsit i en repòs sempre que sigui possible. Aplica bones pràctiques, com ara els protocols de seguretat de la capa de transport al client d’ingesta o protocols de xarxa, per exemple, el protocol de transferència segura de fitxers (SFTP) o un servei Apache Kafka gestionat.

Els clients o les aplicacions d’ingesta que copien dades de sistemes diferents haurien de seguir polítiques d’accés basades en el principi del mínim privilegi. Concedeix només els permisos necessaris per copiar la informació pertinent d’una font externa.

Pel que fa a l’emmagatzematge, tria plataformes que admetin el xifratge en repòs o que ofereixin funcions criptogràfiques avançades, com ara la gestió de claus i el xifratge del costat del servidor amb claus controlades pel client (CMK).

**És essencial controlar estrictament l’accés a les dades**. Solucions com AWS Identity and Access Management o Azure Active Directory permeten controlar els permisos tant a nivell d’objecte com al pla de gestió.

## Supervisar i gestionar el llac de dades

Una **supervisió acurada de la infraestructura del llac de dades ajuda a identificar mancances de seguretat** i activitats sospitoses. **Registra totes les activitats relacionades amb el llac de dades** en un compte d’auditoria separat per impedir que els atacants esborrin o manipulin els registres. Això permet detectar ràpidament activitats sospitoses, com ara l’escaneig de ports, els atacs de denegació de servei distribuïts (DDoS), els atacs de força bruta o els atacs a través de la xarxa.

Fes servir una solució de gestió d’esdeveniments i informació de seguretat (SIEM), com les que inclouen AWS CloudTrail o Azure Monitor, per centralitzar els registres, automatitzar les alertes i fer anàlisis avançades.

Assegura’t també de **reparar regularment els components crítics**. El model de suport hauria d’incloure actualitzacions dels paquets de programari dels sistemes subjacents, com ara sistemes operatius, bases de dades, servidors web i biblioteques de tercers, perquè equips de suport tècnic qualificats corregeixin les vulnerabilitats conegudes.

## Seguir l’evolució del panorama d’amenaces

**La vigilància constant és essencial per mantenir els llacs de dades al núvol segurs i conformes.** El panorama de seguretat canvia ràpidament, per això els controls de seguretat al núvol s’han d’adaptar de pressa a les noves amenaces.

Si vols complir normatives concretes sobre l’emmagatzematge de dades, fes auditories de compliment i genera informes periòdics amb els serveis corresponents.

## Conclusió

Crear un llac de dades al núvol ofereix avantatges importants, però també augmenta les exigències de seguretat i compliment normatiu. Les millors pràctiques del sector, com ara el xifratge en repòs i en trànsit, els controls d’accés amb gestió d’identitats i accessos (IAM), la supervisió mitjançant registres avançats i l’aplicació contínua de pedaços, t’ajudaran a crear un llac de dades al núvol segur i conforme.

Amb controls adequats de migració al núvol i governança, la teva organització podrà aprofitar els serveis al núvol i mantenir alhora la seguretat i el compliment normatiu.

_______

## Referències

1. [Guia per fer servir el xifratge AWS EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
2. [Microsoft: visió general de HIPAA](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
3. [Què és SIEM?](https://www.varonis.com/blog/what-is-siem)
4. [AWS: mètodes d’ingesta de dades](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-ingestion-methods.html)
5. [Estàndards i especificacions d’implementació de la regla de seguretat HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)
