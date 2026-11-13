---
title: "Thunderbird 153.6: exposició de credencials NTLM al Windows i com actualitzar-lo (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Dues vulnerabilitats greus de Thunderbird exposen dades d’autenticació NTLM al Windows quan es mostra un correu preparat expressament. Coneix els dos vectors, comprova la versió i limita l’SMB sortint mentre actualitzes."
genre: ["Ciberseguretat", "Seguretat del correu electrònic", "Seguretat del Windows"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "actualització de seguretat de Thunderbird", "vulnerabilitat de Thunderbird al Windows", "filtració NTLM de Thunderbird", "autenticació SMB de Thunderbird", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "adjunt de clau OpenPGP", "adjunt extern", "bloqueig de contingut remot", "URL mailbox", "camí UNC ampliat", "nom del compte del Windows", "dades d’autenticació NTLM", "exposició de credencials SMB", "SMB sortint", "port TCP 445", "seguretat del correu electrònic", "client de correu del Windows", "comprovació de versió de Thunderbird", "actualització de Thunderbird", "retransmissió NTLM", "cracking de contrasenyes fora de línia"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla ha corregit dues **vulnerabilitats greus d’exposició de credencials del Windows** a Thunderbird 153.6. N’hi havia prou de mostrar un correu maliciós per activar qualsevol de les sol·licituds de xarxa descrites a [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). L’avís descriu una possible divulgació de NTLM, no una vulneració confirmada de les credencials de tots els destinataris.

<!--more-->

## Idees clau

- **CVE-2026-118174** afectava un adjunt de clau OpenPGP allotjat externament. Mostrar el missatge provocava una sol·licitud sense cap acció de l’usuari, fins i tot amb el contingut remot bloquejat.
- **CVE-2026-118176** afectava una URL `mailbox:` especialment formada que feia servir un camí UNC ampliat. Mostrar el missatge provocava una connexió SMB a un servidor escollit pel remitent.
- **Actualitza Thunderbird al Windows** i verifica la versió instal·lada. L’avís indica que Thunderbird 153.6 és la versió corregida. Les notes de versió de Thunderbird identifiquen la compilació 153.6.0esr corresponent.

## Què activa el correu?

**Les dues vulnerabilitats tenen vectors d’entrada diferents.** Segons les descripcions de Mozilla, cap no requereix que el destinatari faci clic en un enllaç del correu. El risc per a les credencials del Windows depèn que una sol·licitud de xarxa arribi a un recurs compartit controlat per l’atacant i que s’hi produeixi l’intercanvi d’autenticació resultant. Mozilla no informa d’una explotació activa a l’avís.

| Problema | Què s’activa quan es mostra el correu | Risc per a les credencials del Windows |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird carrega el contingut d’un adjunt de clau OpenPGP per oferir la importació de la clau. El remitent el marca com a adjunt extern amb una URL escollida per l’atacant. | Una URL d’un recurs compartit de xarxa exposa les credencials NTLM de l’usuari si la sol·licitud arriba al recurs. |
| **CVE-2026-118176** | Un camí UNC ampliat esquiva la restricció de Thunderbird sobre recursos remots a les URL `mailbox:`. | Thunderbird es connecta a un servidor SMB escollit per l’atacant i divulga el nom del compte del Windows i les dades d’autenticació NTLM. |

Per al vector de l’**adjunt OpenPGP**, Mozilla afirma explícitament que la sol·licitud esquivava el bloqueig de contingut remot i no requeria cap acció de l’usuari. En sistemes diferents del Windows, el problema també permetia una sol·licitud remota contrària a la configuració de contingut remot, però Mozilla limita la filtració de credencials NTLM al Windows. Pel vector de la **URL `mailbox:`**, Mozilla diu que els altres sistemes operatius no estan afectats. Consulta les entrades de [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) i [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**Les dades d’autenticació NTLM no són una contrasenya en text pla.** Mozilla diu que les dades divulgades pel vector SMB comporten risc de trencament de contrasenyes fora de línia o d’atacs de retransmissió. Rebre un missatge preparat no demostra que un atac hagi tingut èxit. L’avís també enumera altres vulnerabilitats de Thunderbird, inclosos vectors diferents de calendari i RSS. Aquest article tracta els dos vectors d’exposició en mostrar el correu descrits aquí, sense tractar totes les vulnerabilitats de la versió com si fossin idèntiques.

## Comprova i actualitza Thunderbird

El flux afectat és **llegir correu amb Thunderbird al Windows** abans d’instal·lar la correcció corresponent. L’avís de Mozilla identifica **Thunderbird 153.6** com a versió corregida, però no especifica tot l’interval de versions afectades més antigues per a aquests dos problemes. Les [notes de versió de 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) indiquen una compilació ESR publicada el 27 d’octubre de 2026. No dedueixis l’estat del pegat d’un altre canal, fork o paquet a partir només del número de versió.

1. Al Windows, obre **Help > About Thunderbird**. Consulta la versió que mostra la finestra About, que també comprova si hi ha actualitzacions. Les [instruccions d’actualització de Mozilla](https://support.mozilla.org/en-US/kb/updating-thunderbird) descriuen aquest pas.
2. Si hi ha una actualització disponible, deixa que Thunderbird la baixi i selecciona **Restart Thunderbird to Update**. Torna a obrir **Help > About Thunderbird** i confirma la versió instal·lada després del reinici.
3. Per a la **línia 153 ESR**, compara la versió resultant amb **153.6.0esr** a les notes de versió de Thunderbird. Si la teva organització gestiona les actualitzacions, demana a l’administrador que verifiqui la correcció del proveïdor en lloc de suposar que ja està instal·lada.

> **Avís sobre la versió:** Les notes de 153.6.0esr confirmen que la versió existeix, mentre que MFSA 2026-122 vincula les correccions de seguretat a Thunderbird 153.6. Les notes de versió no descriuen cadascuna d’aquestes dues CVE individualment. Fes servir l’avís per als detalls de les vulnerabilitats.

## Redueix l’exposició mentre actualitzes

**Instal·la primer la correcció del proveïdor.** Desactivar el contingut remot per si sol no atura CVE-2026-118174, perquè la sol·licitud descrita esquivava aquesta configuració. No consideris suficient el consell de «no fer clic». Mozilla descriu sol·licituds activades en mostrar el missatge.

Com a **defensa en profunditat**, restringeix l’SMB sortint dels clients Windows cap a Internet, inclòs el **port TCP 445**, al tallafoc corporatiu o als dispositius gestionats. Les [recomanacions de Microsoft sobre el trànsit SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) aconsellen bloquejar el TCP 445 sortint a Internet i limitar l’accés als servidors de fitxers necessaris. Inventaria els recursos compartits necessaris abans d’aplicar una regla, sobretot si l’entorn fa servir un servei de fitxers al núvol o té treballadors remots fora del perímetre. Aquest control de xarxa limita el vector SMB descrit, però no repara Thunderbird ni resol tots els problemes de sol·licituds remotes de l’avís.

Si un ordinador Windows amb una versió antiga de Thunderbird va mostrar un missatge sospitós, **tracta l’exposició com una qüestió per investigar, no com una prova de compromís**. Revisa amb l’equip de seguretat els registres disponibles de connexions SMB sortints i d’autenticació. L’avís del proveïdor no ofereix una prova d’exposició ni una instrucció general per canviar totes les contrasenyes.

## Fonts

- [Mozilla Foundation Security Advisory 2026-122: vulnerabilitats de seguretat corregides a Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Notes de versió de Thunderbird Desktop: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Suport de Mozilla: actualitza Thunderbird a l’última versió](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: protegeix el trànsit SMB al Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
