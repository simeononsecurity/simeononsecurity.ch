---
title: "Prova l’aïllament de convidats i IoT en una xarxa Wi-Fi de malla"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Comprova si les xarxes de convidats i IoT de la teva Wi-Fi de malla bloquegen l’accés als dispositius de casa. Prova cada xarxa amb un servei actiu i registra’n els límits."
genre: ["Xarxes domèstiques", "Seguretat Wi-Fi", "Llars intel·ligents"]
tags: ["xarxa Wi-Fi de convidats en malla", "prova d’aïllament de xarxa de convidats", "aïllament de xarxa IoT", "seguretat Wi-Fi de malla", "aïllament de clients", "prova de Wi-Fi de convidats", "SSID IoT", "mode punt d’accés", "mode encaminador", "accés a LAN", "prova de xarxa local", "xarxa de convidats Deco", "xarxa de convidats Orbi", "xarxa de convidats ASUS", "Wi-Fi de convidats Google Nest", "Test-NetConnection", "prova de connectivitat TCP", "xarxa domèstica intel·ligent", "aïllament de clients sense fil", "segmentació de xarxa domèstica"]
cover: "/img/cover/mesh-wifi-guest-iot-isolation-test.webp"
coverAlt: "Una casa de dues plantes amb dos encaminadors de malla, telèfons de convidats, llums i càmeres IoT, i un escut que bloqueja el camí cap a un ordinador portàtil de confiança i un NAS."
coverCaption: "Prova separadament els camins entre convidats, IoT i la xarxa principal."
---

Un nom de Wi-Fi diferent no revela quins dispositius es comuniquen. Un sistema de malla pot tractar la **xarxa de convidats**, la **xarxa IoT** i l’**aïllament de clients sense fil** com a controls diferents. Aquesta guia t’ajuda a provar els camins als teus equips sense pressuposar que l’etiqueta del fabricant descriu la política aplicada.

<!--more-->

## Punts clau

- **Comprova primer que la destinació funciona:** accedeix a un servei conegut des de la xarxa principal abans de provar un camí bloquejat.
- **Prova cada límit:** l’accés de convidats a la xarxa principal, d’IoT a la principal i entre convidats respon preguntes diferents.
- **Registra la configuració:** el model, el microprogramari, el mode encaminador o punt d’accés i el node de malla connectat afecten la interpretació.
- **Torna a provar després dels canvis:** un resultat net només s’aplica als dispositius, servei, família d’adreces i configuració provats.

## Abans de començar

Reserva uns 20 minuts. Necessites un portàtil que es pugui connectar a les xarxes Wi-Fi principal, de convidats i IoT. També cal un dispositiu de confiança a la xarxa principal amb un **servei TCP obert conegut**, com ara la interfície web d’un NAS. Un servei TCP escolta en un port numerat, per exemple el port 443 d’una pàgina web d’un NAS. Fes servir un servei propi o que administris. Anota’n l’adreça local i el port, però no els publiquis. Mantén el servei en funcionament durant tota la prova.

Anota el model de malla, la versió del microprogramari, el mode operatiu i els paràmetres d’accés de convidats, accés IoT, dispositius compartits i aïllament de clients. Confirma el nom de Wi-Fi del portàtil després de cada canvi. Si la teva política habitual ho permet, desconnecta la VPN o el servidor intermediari per a aquesta prova del camí local i torna’ls a activar després. Una VPN canvia el camí que proves.

> **Avís:** prova només els teus dispositius o dispositius que tens permís per administrar. La pàgina d’inici de sessió de l’encaminador no substitueix un host de la xarxa principal, perquè l’accés a la passarel·la segueix regles diferents.

Una **xarxa d’àrea local (LAN)** és la teva xarxa domèstica privada. **IoT**, o Internet de les coses, inclou dispositius com càmeres, altaveus i endolls intel·ligents. L’**aïllament de clients** bloqueja el trànsit directe entre dispositius d’una mateixa xarxa Wi-Fi.

## Defineix el límit

Tria el resultat que vols abans de canviar cap paràmetre. L’accés a Internet i l’accés local són resultats separats.

| Camí | Pregunta | Exemple de resultat esperat |
|---|---|---|
| **Convidats a la LAN principal** | Es pot arribar a un ordinador o NAS? | Bloquejat, llevat que triïs una excepció |
| **IoT a la LAN principal** | Es pot arribar als dispositius privats? | Depèn del producte i de la política |
| **Entre convidats** | Es poden comunicar dos convidats? | Depèn de l’aïllament de clients |
| **Convidats a un dispositiu compartit** | Es pot fer servir una impressora o pantalla compartida? | Només permès si és intencionat |
| **Convidats a Internet** | Es pot accedir a un lloc públic normal? | Permès si la política de convidats inclou Internet |

Aquestes files són proves diferents. La [guia d’aïllament de dispositius Deco](https://www.tp-link.com/us/support/faq/3968/) de TP-Link diu que els dispositius aïllats conserven l’accés a Internet i la comunicació amb altres dispositius aïllats, però no poden accedir als dispositius de la xarxa principal. La [guia d’aïllament AP](https://www.asus.com/us/support/faq/1044821/) d’ASUS descriu un control entre parells sense fil i assenyala que un camí per un encaminador cablejat anterior queda fora del seu abast. **Un camí bloquejat no demostra que tots els altres límits també funcionin.**

## Revisa els paràmetres de la malla

Busca la funció que controla el límit que vols provar. Els noms dels menús i la disponibilitat varien segons el model i el microprogramari.

| Paràmetre de malla | Què cal comprovar |
|---|---|
| **Xarxa de convidats TP-Link Deco** | El [mode encaminador aïlla convidats de la xarxa principal](https://www.tp-link.com/us/support/faq/1460/). En mode punt d’accés, comprova **Allow Local Access**. |
| **Perfil de convidats ASUS** | [Access Intranet](https://www.asus.com/uk/support/faq/1009857/) controla l’accés a la xarxa principal en perfils compatibles. |
| **Wi-Fi de convidats Google Nest** | Revisa la llista de [dispositius compartits](https://support.google.com/googlehome/answer/6327302?hl=en) abans d’esperar que una impressora o pantalla quedi oculta. |
| **Xarxa IoT o aïllament de dispositius** | Comprova si el producte ofereix un control d’aïllament separat. Un nom de Wi-Fi IoT no defineix la regla d’accés. |

A Deco, l’[aïllament de dispositius](https://www.tp-link.com/us/support/faq/3968/) requereix compatibilitat a la unitat principal i a les unitats satèl·lit. Anota quin node dona servei al portàtil de prova. Si no hi ha una funció, consulta la documentació del model i el microprogramari exactes en lloc de pressuposar que l’aplicació d’un altre propietari mostra la mateixa configuració.

## Estableix un control positiu

Connecta el portàtil Windows de prova al **Wi-Fi principal**. Confirma que el servei escollit hi funciona. Si fas servir PowerShell, introdueix l’adreça de l’host de la xarxa principal i el seu port obert conegut quan se’t demani:

```powershell
$targetAddress = Read-Host "Main-network test host address"
$targetPort = [int](Read-Host "Known open TCP port")
Test-NetConnection -ComputerName $targetAddress -Port $targetPort
```

La [documentació de Test-NetConnection de Microsoft](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) defineix `-ComputerName` i `-Port` com una prova d’un host i servei TCP concrets. Registra `TcpTestSucceeded`. Primer confirma `True`, abans d’interpretar un `False` posterior. Si falla la prova a la xarxa principal, el problema apunta al servei, l’adreça, el tallafoc de l’host o la configuració del portàtil. Arregla primer la prova principal.

Si fas servir un telèfon o un altre sistema operatiu, obre el mateix servei al navegador o a l’aplicació. Conserva el mateix servei i l’adreça de destinació exacta en canviar de Wi-Fi. Una llista de descobriment de dispositius és una prova més feble, perquè el trànsit de descobriment i l’accés TCP directe segueixen camins diferents.

## Prova l’accés de convidats i IoT

Connecta el mateix portàtil al **Wi-Fi de convidats**. Confirma el nom de Wi-Fi. Obre un lloc web públic si la teva política de convidats inclou Internet. Torna a executar la mateixa ordre `Test-NetConnection` sense canviar `$targetAddress` ni `$targetPort`. Registra’n el resultat.

Torna a la xarxa principal i confirma que el servei encara retorna `True`. Si ara falla la prova principal, el resultat de convidats no és concloent. Després, connecta el mateix portàtil al **Wi-Fi IoT**, si el sistema permet connectar-hi un portàtil, i repeteix la prova. No pressuposïs que el resultat IoT coincidirà amb el de convidats. Si IoT arriba a la xarxa principal, el servei TCP local triat era accessible des de la xarxa IoT amb aquesta configuració.

Si vols aïllar els convidats entre ells, fes servir dos dispositius que controlis a la xarxa de convidats. Des d’un, prova un servei conegut de l’altre. Registra-ho per separat de l’accés de convidats a la xarxa principal. Si vols que funcioni una impressora o pantalla compartida, prova també aquesta excepció. El control al núvol d’un dispositiu intel·ligent no demostra un camí local directe.

Repeteix la prova de convidats a la xarxa principal a prop de cada node de malla. Confirma a l’aplicació quin node dona servei, si ho indica. **IPv6** és la família d’adreces més nova del Protocol d’Internet i fa servir adreces de 128 bits. Si l’host principal admet IPv6 i el control positiu principal funciona amb IPv6, repeteix la prova amb la mateixa família d’adreces des de les xarxes Wi-Fi de convidats i IoT. Una prova només amb IPv4 no cobreix un camí IPv6.

## Interpreta una discrepància

| Observació | Comprovació següent |
|---|---|
| **Fallen tant la xarxa principal com la de convidats** | Revisa el servei de destinació, l’adreça, el port i el tallafoc de l’host. No s’ha demostrat l’aïllament. |
| **Funcionen la xarxa principal i la de convidats** | Revisa l’accés local de convidats, les excepcions de dispositius compartits i el mode encaminador o punt d’accés. |
| **La principal funciona i convidats falla** | Registra les proves per a aquesta destinació i camí TCP. Prova els altres camins que demana la política. |
| **Convidats bloquejat, IoT funciona** | Comprova si la xarxa IoT és una xarxa de compatibilitat sense una regla d’aïllament equivalent. |
| **Convidats a la principal bloquejat, convidats entre ells funciona** | Revisa separadament l’aïllament de clients sense fil. |

Un **ping** fallit no resol la qüestió TCP. El tallafoc d’un host pot bloquejar el ping i acceptar el servei que has triat. Un test TCP fallit també és limitat: no informa sobre altres ports, dispositius, IPv6 ni excepcions per a dispositius compartits. Tracta una discrepància com un motiu per revisar la regla configurada i repetir una prova controlada.

## Corregeix i registra el resultat

Canvia un sol control cada vegada. En un Deco en mode punt d’accés, revisa **Allow Local Access**. En un perfil de convidats ASUS, revisa **Access Intranet**. A Google Nest Wifi, elimina un element no previst de **Shared devices**. Si necessites control local de la llar intel·ligent, decideix quin dispositiu ha d’accedir a quin servei abans d’afegir una excepció. Una **VLAN** és una xarxa lògica transportada sobre maquinari compartit. El [pla de segmentació VLAN](/articles/homelab-vlan-segmentation-plan/) del lloc tracta les xarxes gestionades quan una malla de consum no ofereix la regla d’accés necessària.

Registra el model de malla, el microprogramari, el mode, el node, el nom Wi-Fi, el dispositiu d’origen, el servei de destinació, la família d’adreces, el resultat previst i l’obtingut, i l’únic canvi efectuat. No publiquis adreces privades ni contrasenyes de xarxa. Repeteix les proves després d’actualitzar el microprogramari, canviar de node o passar entre els modes encaminador i punt d’accés.

Si encara tries equipament, compara les funcions a la [guia de compra de Wi-Fi de malla](/articles/best-wifi-mesh-system-for-consumers/). Després aplica aquest procediment a la xarxa instal·lada. **Una etiqueta o un interruptor de l’aplicació és una afirmació. Un control positiu i una prova repetida en les mateixes condicions aporten proves del camí concret que t’interessa.**

## Passos següents

Repeteix les proves d’aïllament després de canvis de microprogramari, nodes o mode operatiu. Fes servir el [pla de segmentació VLAN](/articles/homelab-vlan-segmentation-plan/) si els controls de malla no compleixen el límit necessari.
