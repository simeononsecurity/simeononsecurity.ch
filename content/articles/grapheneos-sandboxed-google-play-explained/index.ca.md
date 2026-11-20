---
title: "Sandboxed Google Play a GrapheneOS, explicat"
date: 2026-09-11
lastmod: 2026-11-20
toc: true
draft: false
description: "Descobreix què canvia Sandboxed Google Play a GrapheneOS, quan és útil un perfil separat i com es relacionen els comptes, les notificacions i la compatibilitat de les aplicacions."
genre: ["Privadesa", "Seguretat mòbil", "Codi obert"]
tags: ["GrapheneOS", "Sandboxed Google Play", "Google Play services", "Google Play Store", "privadesa d’Android", "seguretat d’Android", "aïllament d’aplicacions", "compte de Google", "perfils de GrapheneOS", "perfil del propietari", "perfils d’usuari", "perfil de feina", "compatibilitat d’aplicacions", "notificacions push", "Firebase Cloud Messaging", "permisos d’aplicacions", "privadesa de Pixel", "instal·lació de Google Play", "privadesa mòbil", "GrapheneOS App Store"]
cover: "/img/cover/grapheneos-sandboxed-google-play-explained.webp"
coverAlt: "La pantalla d'un telèfon intel·ligent mostra aplicacions en compartiments transparents separats, inclòs un símbol de colors d'una botiga d'aplicacions."
coverCaption: ""
---

**Sandboxed Google Play** et permet instal·lar els components oficials de Google Play a GrapheneOS com a aplicacions normals. S'executen sense els privilegis del sistema que Google Play acostuma a rebre al sistema operatiu estàndard. La instal·lació és opcional. [Visió general de les funcions de GrapheneOS](https://grapheneos.org/features#sandboxed-google-play).

## Idees principals

- **Entén l'aïllament:** diferencia els permisos de les aplicacions de l'activitat dels comptes en línia.
- **Agrupa les dependències:** mantén al mateix perfil l'aplicació dependent i Play.
- **Prova el funcionament:** comprova les notificacions en segon pla i les tasques essencials.
- **Prepara un pla:** anota els perfils, comptes i requisits de les aplicacions que has triat.

## Abans de començar

**Públic:** persones usuàries de GrapheneOS que decideixen si instal·len Google Play i on el posen. **Requisits previs:** un dispositiu compatible amb GrapheneOS actualitzat i accés als comptes essencials. La instal·lació del sistema operatiu s'explica a la [guia d'instal·lació de GrapheneOS](/guides/how-to-install-graphine-os/).

**Temps estimat:** entre 20 i 30 minuts per fer l'inventari inicial d'aplicacions i les comprovacions, més l'ús diari habitual per valorar la fiabilitat de les notificacions. **Dificultat:** inicial. Comença amb una aplicació representativa abans de reorganitzar el telèfon.

## Què canvia amb l’aïllament

El **sandbox d'aplicacions** d'Android separa els recursos de les aplicacions mitjançant proteccions del sistema operatiu. Una aplicació no obté accés il·limitat als fitxers privats d'una altra. La protecció s'aplica tant al codi natiu com al que s'executa a l'entorn gestionat d'Android. [Documentació del sandbox d'aplicacions d'Android](https://source.android.com/docs/security/app-sandbox).

GrapheneOS afegeix una **capa de compatibilitat** perquè els components oficials de Play funcionin dins d'aquestes restriccions habituals. Les aplicacions del mateix perfil encara disposen de formes admeses de comunicar-se amb consentiment mutu. El sandbox limita els privilegis, però no impedeix tots els intercanvis intencionats entre aplicacions. [Disseny de Sandboxed Google Play](https://grapheneos.org/features#sandboxed-google-play).

| Aspecte | Significat pràctic |
|---|---|
| **Fitxers privats de les aplicacions** | Instal·lar Play no dona accés il·limitat a les dades d'altres aplicacions |
| **Permisos** | Revisa l'accés sol·licitat com ho faries amb qualsevol altra aplicació |
| **Funcions basades en Google** | Una aplicació que tria un servei de Google continua comunicant-s'hi |
| **Activitat del compte** | Iniciar sessió en un servei continua sent una decisió de privadesa separada |

**El sandbox i la privadesa del compte** responen preguntes diferents. El sandbox restringeix l'accés local. No esborra la informació que envies expressament a un servei en línia. Per exemple, iniciar sessió en una aplicació de compres continua identificant el teu compte davant de qui l'opera.

## Separa tres àmbits de privadesa

**L'accés local, l'ús de serveis i la identitat** són qüestions separades. Si una aplicació demana accés als contactes i iniciar sessió en un compte, revisa cada sol·licitud per separat:

| Decisió | Pregunta |
|---|---|
| **Permís local** | Aquesta funció necessita els meus contactes, el micròfon o la ubicació? |
| **Dependència d'un servei** | Quina funció depèn de serveis de Google Play? |
| **Identitat en línia** | Amb quin compte associo aquesta activitat? |

**Exemple pràctic:** un compte de compres ja conté la teva adreça de lliurament. Moure'n l'aplicació a un altre perfil no canvia l'adreça que conserva el comerç. Denegar l'accés als contactes respon una altra pregunta sobre les dades disponibles al telèfon.

**Objectiu de privadesa:** anota quina exposició concreta vols reduir. «Evitar que aquesta aplicació accedeixi als meus contactes personals» es pot comprovar. «Fer anònim aquest compte» requereix decisions que van més enllà de triar un perfil.

## Perfil del propietari o perfil separat?

**Instal·lar al perfil del propietari** és una opció senzilla i admesa. Google Play continua aïllat en aquest perfil. Un perfil d'usuari o de feina separat et permet triar quin grup d'aplicacions tindrà Play disponible. [Indicacions d'instal·lació de GrapheneOS](https://grapheneos.org/usage#sandboxed-google-play-installation).

| Prioritat | Configuració inicial | Compromís |
|---|---|---|
| **Ús diari senzill** | Mantén les aplicacions necessàries i Play al perfil del Propietari | Play està disponible per a les aplicacions que cooperen dins d'aquest perfil |
| **Separar les aplicacions dependents de Google** | Instal·la-les juntes en un altre perfil | Més gestió de perfils |
| **Evitar els serveis de Google** | Comença sense Play | Revisa les dependències de cada aplicació |

**La ubicació del perfil** importa més que instal·lar el mateix component a tot arreu. Les preguntes freqüents de GrapheneOS expliquen que Play es limita als perfils seleccionats. Moltes aplicacions funcionen sense Play o només el necessiten per a una part de les seves funcions. [Preguntes freqüents sobre els serveis de Google](https://grapheneos.org/faq#google-services).

*Fes servir un perfil separat quan la disponibilitat selectiva de Play resolgui una necessitat concreta que hagis identificat.*

## Entén l'activitat dels perfils

**Un perfil d'usuari secundari** té les seves pròpies instàncies d'aplicacions i les seves pròpies dades. Canviar a un altre usuari i acabar la sessió de l'usuari anterior són accions diferents. **Acaba la sessió** atura les aplicacions del perfil secundari i retorna el seu emmagatzematge xifrat al repòs. [Preguntes freqüents de GrapheneOS sobre xifratge i perfils](https://grapheneos.org/faq#encryption).

**El reenviament de notificacions** pot mostrar a l'usuari actiu les notificacions d'un usuari que funciona en segon pla. No manté activa una sessió acabada. [Funcions dels perfils d'usuari de GrapheneOS](https://grapheneos.org/features).

| Estat del perfil | Condició de lliurament |
|---|---|
| **Actiu** | Prova el lliurament dins d'aquest perfil |
| **En segon pla** | Comprova el reenviament a l'usuari actiu |
| **Sessió acabada** | Les aplicacions d'aquest perfil estan aturades |

Per a **una aplicació de missatgeria d'ús diari**, decideix si és essencial rebre missatges mentre fas servir el perfil del Propietari. Una configuració que exigeix acabar sovint les sessions entra en conflicte amb el lliurament continu en segon pla. Valora aquest compromís abans de moure l'historial principal de converses.

## Instal·lació i comptes

Obre la **GrapheneOS App Store** integrada, selecciona **Google Play services** i instal·la'l. També s'instal·larà la Play Store que en depèn. Deixa que l'App Store gestioni aquests components. Exclou serveis de Google Play de l'optimització de la bateria perquè les funcions en segon pla, com les notificacions push, siguin fiables. [Instruccions oficials d'instal·lació](https://grapheneos.org/usage#sandboxed-google-play-installation).

**Iniciar sessió amb un compte de Google** és opcional per a les funcions que no depenen d'un compte. Per instal·lar aplicacions a través de la Play Store, cal iniciar sessió. Les instal·lacions antigues també inclouen Google Services Framework, que el projecte recomana conservar. Segueix les instruccions actuals, no una llista antiga de tres paquets.

## Prova primer una aplicació

Fes servir una **aplicació representativa de baix risc** per comprovar la configuració de perfils prevista. Durant la prova, mantén disponibles els mètodes actuals de recuperació del compte.

1. **Tria un perfil:** decideix on anirà l'aplicació abans d'instal·lar-ne les dependències.
2. **Instal·la Play:** segueix en aquest perfil els passos oficials anteriors.
3. **Instal·la l'aplicació:** utilitza una font de distribució fiable i acaba la configuració inicial.
4. **Revisa les sol·licituds:** concedeix els permisos adequats a la funció que proves.
5. **Prova una funció:** envia un missatge, obre un mapa o fes una altra acció reversible.
6. **Anota el resultat:** registra les versions de l'aplicació i del sistema, el perfil i l'operació exacta.

**Prova esperada:** una descripció repetible, com ara «ha arribat un missatge de prova amb la pantalla bloquejada i el perfil actiu». No anotis només «funciona», perquè no especifica la funció ni les condicions provades.

## Diagnostica la manca de notificacions

Les **notificacions push** depenen de com s'ha implementat l'aplicació. Algunes mantenen la seva pròpia connexió en segon pla. D'altres depenen de Firebase Cloud Messaging de Google. Que una aplicació s'obri no demostra que les notificacions arribin després de bloquejar el telèfon. [Preguntes freqüents de GrapheneOS sobre notificacions](https://grapheneos.org/faq#notifications).

**Comprova les condicions de lliurament** abans de canviar els permisos de diverses aplicacions:

| Símptoma | Com acotar la investigació |
|---|---|
| **Els missatges apareixen només després d'obrir l'aplicació** | Revisa el mètode de lliurament en segon pla i els ajustos de bateria |
| **El lliurament només funciona al perfil de l'aplicació** | Revisa l'activitat del perfil i el reenviament de notificacions |
| **No arriba res després d'Acaba la sessió** | Inicia el perfil secundari abans de tornar a provar |
| **La notificació arriba sense so** | Revisa el canal de notificacions i els ajustos de so de l'aplicació |

Els **canals de notificació** agrupen el comportament de les notificacions d'una aplicació, incloent-hi la importància i el so. Android posa controls dels canals a disposició de l'usuari. [Documentació d'Android sobre canals de notificació](https://developer.android.com/develop/ui/compose/notifications/channels).

**Repeteix la prova canviant una sola condició cada vegada:** mantén iguals el dispositiu emissor i el tipus de missatge mentre canvies l'estat del perfil receptor. Anota «actiu», «en segon pla» o «sessió acabada» amb cada resultat. Això permet distingir un problema del cicle de vida del perfil d'un problema de configuració de notificacions.

## Avalua els fluxos de treball essencials

Abans de confiar en una configuració nova, fes una breu **prova d'acceptació personal**:

| Flux de treball | Comprovació al dispositiu |
|---|---|
| **Missatgeria** | Rep un missatge amb la pantalla bloquejada |
| **Accés al compte** | Inicia sessió i completa el segon factor requerit |
| **Banca o pagaments** | Prova la funció exacta que necessites, incloses les comprovacions del dispositiu |
| **Navegació** | Obtén la ubicació amb els permisos que has triat |

**Que una aplicació s'obri** només és la primera comprovació. Quan resolguis problemes, anota les versions de l'aplicació i GrapheneOS, i l'operació que ha fallat. Aquest article ofereix un marc de decisió, no una llista de compatibilitat provada.

**Decisió de migració:** conserva l'antic mètode d'accés fins que totes les operacions essencials hagin superat la prova. Una aplicació de missatgeria i una de banca necessiten criteris d'acceptació diferents. Rebre un missatge no informa sobre les comprovacions del compte o del dispositiu d'una altra aplicació.

**Torna a comprovar-ho després d'actualitzar GrapheneOS o les aplicacions.** La ubicació del perfil, els permisos, els canals de notificació i l'estat de la sessió continuen definint la prova. Anota la versió amb cada resultat perquè un canvi en les notificacions o en l'inici de sessió no es converteixi en una conclusió de privadesa sense fonament.

Per a **un inici de sessió de feina**, prova tota la seqüència i el segon factor requerit. En una aplicació de viatges, prova la funció que preveus fer servir fora de casa. Tria accions representatives sense fer compres innecessàries ni canviar la seguretat del compte.

## Prepara el teu pla d'aplicacions

Completa aquest **inventari** per a les cinc aplicacions més importants. Les files són suggeriments de comprovació, no afirmacions de compatibilitat de productes concrets:

| Categoria d'aplicació | Requisit per anotar | Prova per recollir |
|---|---|---|
| **Missatgeria** | Lliurament en segon pla i perfil triat | Prova amb la pantalla bloquejada i el perfil en segon pla |
| **Accés a la feina** | Inici de sessió necessari i segon factor | Inici de sessió completat |
| **Navegació** | Permís d'ubicació i necessitats sense connexió | Una ruta en les condicions previstes |
| **Banca** | Operacions essencials compatibles | Resultats de cada funció necessària |
| **Compres** | Accés al compte i a les dades locals | Revisió de permisos i ús normal del compte |

**Anota una decisió** per a cada fila: perfil triat, dependència de Play, requisit del compte, permisos aprovats i alternativa. Mantén com a desconegudes les dependències que no hagis comprovat. Així evitaràs instal·lar components addicionals només perquè una altra aplicació els necessitava.

**Exercici de revisió:** una aplicació funciona mentre el perfil secundari és actiu, però deixa de rebre missatges després d'acabar la sessió. Primer reinicia el perfil i torna-la a provar. Donar accés als contactes no resoldria una sessió aturada.

**Criteri de finalització:** el teu pla explica per què cada aplicació és al perfil triat i quina prova justifica confiar-hi. Torna a revisar-ne la fila després d'una actualització que en canviï el comportament.

## Passos següents

Si encara no has instal·lat el sistema operatiu, consulta la [guia d'instal·lació de GrapheneOS](/guides/how-to-install-graphine-os/). Després tria una configuració de perfils i prova les aplicacions essencials abans d'afegir-ne més o canviar permisos generals.
