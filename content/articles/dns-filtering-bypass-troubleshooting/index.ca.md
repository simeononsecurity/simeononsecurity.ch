---
title: "Per què s’eludeix el filtre DNS: comprova la ruta del resolutor"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Esbrina per què un dispositiu o navegador se salta el filtre DNS. Compara les consultes directes i normals, revisa els registres i comprova el DNS xifrat, la VPN, IPv6 i el router."
genre: ["Xarxes domèstiques", "DNS", "Privadesa"]
tags: ["eludir el filtre DNS", "eludir Pi-hole", "registre de consultes DNS", "DNS segur del navegador", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "DNS de la VPN", "DNS IPv6", "DHCP DNS del router", "Resolve-DnsName", "resolució de problemes DNS", "prova del filtre DNS", "resolució de problemes NextDNS", "resolució de problemes AdGuard DNS"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "La ruta DNS blava d’un portàtil travessa un filtre i s’atura en un símbol de bloqueig, mentre que la ruta taronja del navegador arriba a un altre resolutor."
coverCaption: "Segueix la ruta de la consulta abans de modificar la regla del filtre."
---

Has configurat un resolutor de filtratge, però un dispositiu encara arriba a un domini que la teva política bloqueja. La causa pot ser la regla, l’assignació del Domain Name System (DNS) del dispositiu, un resolutor xifrat del navegador o una VPN. **Comprova la ruta abans de canviar la configuració.** Una consulta directa al filtre respon una pregunta diferent d’una consulta normal del dispositiu.

<!--more-->

## Idees clau

- **Comprova primer la regla:** Confirma que el filtre rep i bloqueja un domini de prova segur.
- **Segueix cada capa:** El router, el sistema operatiu, el navegador, la VPN i la configuració mòbil afecten l’encaminament DNS.
- **Fes consultes noves:** Relaciona un nom d’amfitrió nou i l’hora amb el registre de consultes del filtre.
- **Indica el límit:** Una consulta observada demostra una ruta, no el comportament de totes les aplicacions i dispositius.

## Abans de començar

Reserva uns 20 minuts. Necessites accés al registre de consultes del resolutor de filtratge, un dispositiu amb el problema i un registre de la configuració DNS del router. Els exemples fan servir un portàtil Windows i **Pi-hole**, però la mateixa comparació funciona amb qualsevol resolutor que ofereixi registres per client. Identifica primer l’adreça exacta del filtre. No publiquis adreces privades de clients, registres de consultes ni regles de política.

Tria un **domini de prova inofensiu** que la teva política ja bloquegi. També pots afegir temporalment una regla de rebuig exacta per a un domini que controlis en un perfil de prova. Anota la regla i elimina-la després de la prova. No facis servir un domini de programari maliciós actiu com a sonda. Una pàgina bloquejada és un símptoma útil, però el registre del resolutor aporta proves més sòlides de la ruta.

| Capa | Pregunta |
|---|---|
| **Filtre** | Una consulta directa arriba al resolutor previst i coincideix amb la regla? |
| **Dispositiu** | Quins servidors DNS assigna la xarxa? |
| **Navegador o aplicació** | Aquest client fa servir el resolutor del dispositiu o una ruta separada? |
| **VPN o relay** | Un túnel actiu canvia la destinació de les consultes? |

## Demostra que el filtre funciona

Obre el registre de consultes del resolutor. Consulta directament al filtre el domini bloquejat escollit. A Windows, utilitza PowerShell i introdueix l’adreça del filtre i el domini de prova quan se’t demanin:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

La [referència de Microsoft de **`Resolve-DnsName`**](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) defineix **`-Server`** com una consulta al resolutor indicat. Cerca la consulta al registre del filtre i comprova la resposta i la regla coincident. La [documentació de Pi-hole sobre consultes i registres](https://docs.pi-hole.net/main/pihole-command/) descriu les eines de consulta locals. Si la consulta directa s’accepta, corregeix la regla o l’assignació del grup de clients abans d’investigar una elusió. Si no arriba al filtre, comprova l’adreça, el servei i la ruta de xarxa.

**Aquesta prova directa no demostra que el portàtil faci servir el filtre habitualment.** L’opció **`-Server`** substitueix el resolutor predeterminat per a aquesta consulta. Aquesta distinció evita un fals positiu freqüent.

## Segueix la ruta del dispositiu

Utilitza un nom d’amfitrió nou per evitar una entrada DNS anterior a la memòria cau. L’exemple següent envia una consulta directament al filtre i una altra mitjançant la selecció normal de resolutor del portàtil. Els noms són diferents perquè puguis identificar l’entrada de registre de cada ruta. Una resposta **NXDOMAIN** vol dir que el servidor DNS informa que el nom d’amfitrió no existeix. És normal si no s’utilitza el nom aleatori. Aquí importa si la consulta apareix al registre del filtre.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Cerca els dos noms exactes al registre del filtre i anota l’hora i el client indicat. Si apareix **`direct-`** però no **`default-`**, inspecciona els servidors DNS assignats al portàtil. A Windows, **`Get-DnsClientServerAddress`** mostra les adreces dels servidors DNS per interfície. Comprova l’adaptador Wi-Fi o Ethernet actiu, no un de desconnectat. La [referència del client DNS de Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) descriu aquesta ordre només de lectura.

Deixa els errors visibles durant la primera prova. Un error o un temps d’espera esgotat requereix un diagnòstic separat i no és el mateix que l’absència d’una entrada al registre.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Compara les files IPv4 i IPv6. **DHCP** assigna configuracions de xarxa com ara servidors DNS. **IPv6** és la família més nova d’adreces d’Internet Protocol i utilitza adreces de 128 bits. Una concessió IPv4 pot indicar el filtre mentre els anuncis IPv6 del router proporcionen un altre servidor DNS. Comprova els anuncis **DHCP** i **DNS IPv6** del router, i renova la concessió de xarxa del dispositiu després d’una correcció. La [guia posterior a la instal·lació de Pi-hole](https://docs.pi-hole.net/main/post-install/) explica com DHCP dirigeix els clients a Pi-hole. El seu [exemple de router](https://docs.pi-hole.net/routers/fritzbox/) tracta els anuncis DNS IPv6.

Si el registre mostra el **router** com a client, pot ser que el router reenviï les consultes en nom dels dispositius. Aleshores, el registre del filtre demostra que el router hi ha arribat, no quin dispositiu ha iniciat la consulta. Confirma el disseny de reenviament del router abans de considerar que la identitat del client és una dada absent.

## Comprova el DNS del navegador

Una consulta de línia d’ordres prova la ruta del resolutor del dispositiu. Un navegador pot fer servir **DNS over HTTPS (DoH)** en lloc d’això. Obre el mateix domini de prova bloquejat al navegador i observa si apareix una consulta corresponent al registre del filtre. Buida la memòria cau DNS del navegador o utilitza un nom d’amfitrió nou cobert per una regla de prova si els resultats emmagatzemats dificulten la comparació.

A **Chrome en un ordinador**, obre **Configuració > Privadesa i seguretat > Seguretat > Utilitza DNS segur**. L’[ajuda de Google Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) diu que el mode automàtic fa servir el proveïdor actual i torna a les consultes sense xifrar si falla. Un proveïdor personalitzat seleccionat no torna enrere de la mateixa manera. Anota el mode i el proveïdor seleccionats abans de canviar la configuració.

A **Firefox**, obre **Configuració > Privadesa i seguretat > DNS a través d’HTTPS**. La [guia de Mozilla sobre nivells de protecció](https://support.mozilla.org/en-US/kb/dns-over-https) distingeix els modes Predeterminat, Augmentat, Màxim, Personalitzat i Desactivat. La [descripció de DoH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) explica quan un resolutor del navegador eludeix un filtre DNS local. Torna a provar després d’un únic canvi controlat i després restaura la configuració de privadesa desitjada.

**No qualifiquis cada consulta absent del navegador d’elusió.** El navegador pot reutilitzar dades de la memòria cau, arribar a una adreça coneguda o fer servir un servidor intermediari. Compara un nom nou, una finestra horària corresponent i la configuració del resolutor del navegador abans de concloure on ha anat la consulta.

## Comprova les rutes mòbils i de VPN

A **Android**, revisa **Configuració > Xarxa i Internet > DNS privat**. El nom d’amfitrió d’un proveïdor selecciona un servei DNS privat diferent del DNS anunciat pel router. La [configuració de xarxa d’Android de Google](https://support.google.com/android/answer/9654714?hl=en) descriu les opcions Desactivat, Automàtic i Nom d’amfitrió del proveïdor. Per obtenir un resultat local controlat, prova per Wi-Fi amb les dades mòbils desactivades i després restaura la configuració habitual.

A **dispositius Apple**, comprova si **iCloud Private Relay** està actiu per a la xarxa i si Safari utilitza la ruta esperada. Apple diu que [Private Relay protegeix la navegació de Safari i la informació DNS](https://support.apple.com/en-gb/102602). Els seus [controls de xarxa](https://support.apple.com/en-ie/102022) descriuen el tractament per xarxa quan el filtratge entra en conflicte amb Private Relay. No generalitzis un resultat de Safari a totes les aplicacions del dispositiu.

Una **VPN** pot proporcionar el seu propi resolutor DNS o enviar consultes pel túnel. Anota si la VPN està connectada, la seva configuració DNS i la política de túnel dividit. Compara la mateixa prova amb la VPN activada i desactivada només si la teva política de seguretat ho permet. Un resultat diferent identifica una ruta distinta. Per si sol, no demostra una filtració ni un defecte del filtre.

## Interpreta els resultats

| Evidència | Comprovació següent probable |
|---|---|
| **La consulta directa no apareix al registre del filtre** | Adreça del filtre, servei DNS, registre o accessibilitat de xarxa |
| **La consulta directa s’accepta** | Regla de rebuig exacta, política de grup o prioritat de regles |
| **Consulta directa registrada, consulta normal absent** | DHCP, DNS estàtic del dispositiu, DNS IPv6 o resolutor VPN |
| **Consulta normal registrada, consulta del navegador absent** | DoH del navegador, memòria cau, proxy o relay |
| **Totes dues s’enregistren i es bloquegen, però el lloc es carrega** | Un altre nom d’amfitrió, contingut en memòria cau, adreça directa o ruta de l’aplicació |

**L’absència de registres és ambigua** si el registre està desactivat, el router reenvia en nom del client o la prova reutilitza dades desades. Repeteix-la amb un nom nou i comprova l’hora abans de canviar les regles del tallafoc. Bloquejar DNS sense xifrar cap a resolutors externs no obliga un navegador xifrat o una VPN a fer servir el filtre. La [guia Pi-hole per a OPNsense](https://docs.pi-hole.net/routers/opnsense/) presenta el bloqueig de DNS extern com un control de xarxa opcional. La política del dispositiu i la configuració del navegador continuen sent controls separats.

## Corregeix i torna-ho a provar

Canvia una capa cada vegada. Corregeix els anuncis DHCP o DNS IPv6, elimina un resolutor estàtic no previst, selecciona el proveïdor DNS desitjat al navegador o ajusta la política DNS de la VPN. No debilitís en silenci el DNS xifrat ni la protecció relay de tots els dispositius per resoldre una sola prova fallida. Anota el dispositiu d’origen, la interfície, l’adreça del filtre, el nom consultat, l’hora, la resposta, el client del registre, el mode del navegador, l’estat de la VPN i el canvi fet.

Després de cada canvi, repeteix les proves **directa**, **normal** i **del navegador**. Fes servir un nom d’amfitrió nou a cada execució. Si un dispositiu té diversos perfils de xarxa, prova’ls per separat. La [comparació de resolutors DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) ajuda a triar un servei. La [prova de fuites del navegador](/articles/privacy-browser-leak-test-dns-webrtc/) respon una pregunta diferent: quina informació de xarxa surt de la configuració del navegador i de la VPN. **Un resultat fiable del filtre requereix una regla verificada i una ruta de client verificada.**

## Passos següents

Repeteix les proves directa, normal i del navegador després de cada canvi controlat. Consulta la [comparació de resolutors DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) quan triïs un servei de filtratge.
