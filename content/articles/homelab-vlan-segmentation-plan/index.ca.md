---
title: "Planifica i prova la segmentació VLAN d'un homelab"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Crea un pla VLAN per separar els dispositius de confiança, els servidors, els dispositius IoT i els convidats del teu homelab. Defineix el trànsit permès, configura la xarxa per etapes i prova l'aïllament."
genre: ["Homelab", "Seguretat de xarxa", "Xarxes"]
tags: ["VLAN d'homelab", "segmentació VLAN", "xarxa IoT", "xarxa de convidats", "tallafoc d'homelab", "encaminament entre VLAN", "802.1Q", "aïllament de xarxa", "prova VLAN", "VLAN de pfSense", "port d'accés", "port tronc", "regles del tallafoc", "seguretat d'homelab", "pla de xarxa", "subxarxa", "DHCP", "DNS", "commutador gestionable", "SSID sense fil"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Un encaminador i un commutador d'homelab separen portàtils, servidors, dispositius IoT i convidats en zones de xarxa protegides."
coverCaption: "Planifica els límits VLAN i després prova cada ruta permesa i bloquejada."
---

Un homelab sovint posa portàtils, servidors, càmeres i dispositius dels convidats en una sola xarxa. **La segmentació VLAN** distribueix aquests grups en xarxes separades. Un encaminador, un tallafoc o un commutador de capa 3 encamina el trànsit entre les xarxes. Les regles del tallafoc o les llistes de control d'accés del commutador regulen aquests fluxos encaminats. Aquesta guia t'ajuda a redactar el pla, fer un canvi cada vegada i provar-ne el resultat.

## Idees clau

- **Agrupa per nivell de confiança:** posa els dispositius d'administració, els servidors, els dispositius IoT i els convidats en xarxes separades si tenen necessitats d'accés diferents.
- **Anota les rutes permeses:** registra l'origen, la destinació, el servei i el motiu de cada connexió entre xarxes.
- **Configura totes dues capes:** els paràmetres VLAN del commutador i del punt d'accés assignen els dispositius a una xarxa. Les regles del tallafoc o les llistes de control d'accés del commutador controlen el trànsit encaminat.
- **Prova els dos resultats:** comprova una connexió permesa i una de bloquejada des de cada xarxa pertinent.

## Abans de començar

Necessites un encaminador o un tallafoc amb interfícies VLAN, o bé un commutador de capa 3 que admeti encaminament VLAN i llistes de control d'accés. Un commutador gestionable transporta les VLAN amb cable. També necessites un punt d'accés amb xarxes sense fil associades a VLAN si separes els clients sense fil. Mantén un dispositiu a la xarxa d'administració actual mentre canvies la configuració. Desa primer els paràmetres de l'encaminador, del commutador i del punt d'accés. Els passos següents fan servir un **pla il·lustratiu**, així que adapta les adreces i els ports al teu equipament.

Una **interfície VLAN** és la connexió de la passarel·la amb una VLAN. La passarel·la pot ser un encaminador, un tallafoc o un commutador de capa 3. Un **àmbit DHCP** és l'interval d'adreces que un servei DHCP ofereix als dispositius d'aquesta xarxa. Un **relé DHCP** reenvia les sol·licituds d'adreça d'una VLAN a un servidor DHCP d'una altra xarxa. Fes servir un relé quan la passarel·la no assigna adreces per a aquella VLAN i el servidor DHCP és en un altre lloc. La [guia de relé DHCP de Juniper](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) descriu aquesta ruta. Un **SSID** sense fil és el nom de la xarxa a la qual es connecten els clients. Si el teu equipament no té un commutador gestionable o un punt d'accés compatible amb VLAN, comença amb la xarxa de convidats integrada i comprova'n l'aïllament abans de comprar o canviar maquinari.

Si primer necessites els termes bàsics, llegeix [subxarxes i VLAN](/articles/networking-basics-what-are-subnets-and-vlans/). La [guia de segmentació de xarxa](/articles/how-to-perform-network-segmentation-for-improved-security/) del lloc tracta el concepte de seguretat més ampli. CISA descriu xarxes domèstiques separades per als convidats i els dispositius de l'Internet de les coses a les seves [recomanacions de seguretat per a llocs de treball federals mòbils](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Avís:** un canvi VLAN al port que transporta la connexió d'administració et pot deixar sense accés. Mantén l'accés físic i una via de recuperació coneguda fins que totes les xarxes superin les proves.

Abans de moure un cable, exporta la configuració de cada dispositiu i anota l'adreça IP d'administració actual, el port del commutador, el paràmetre VLAN i les credencials d'administració. Deixa un port d'administració funcional i un portàtil a la xarxa original. Si un canvi talla l'accés, torna a connectar el portàtil a aquell port, restaura el paràmetre o la configuració desada i confirma que l'antiga passarel·la respon abans de provar-ho de nou. Si la via d'administració del commutador no és accessible, segueix el procediment documentat de consola o recuperació local. No restableixis l'equip fins que sàpigues què esborra el restabliment.

## Inventaria els dispositius i els fluxos

Llista cada dispositiu, la seva adreça actual, el propietari i els serveis que necessita. Assigna una raó a cada dispositiu perquè accedeixi a una altra xarxa. Per exemple, un portàtil pot administrar un servidor, mentre que una càmera només pot necessitar accés a una gravadora i a un servidor DNS. Un telèfon de convidat necessita Internet, però no accés als servidors.

| Grup de dispositius | Exemples de dispositius | Accés necessari |
|---|---|---|
| **Administració** | Portàtil d'administració, gestió del commutador i del punt d'accés | Encaminador, commutador, punt d'accés, administració dels servidors |
| **Servidors** | Hipervisor, NAS, destinació de còpies de seguretat | Actualitzacions, DNS, trànsit d'aplicacions aprovat |
| **IoT** | Càmeres, endolls intel·ligents, dispositius multimèdia | DNS, servei horari, controlador o gravadora concrets |
| **Convidats** | Telèfons i portàtils de visitants | Internet, DNS, cap accés a subxarxes privades |

Anota les excepcions abans d'afegir regles. Les funcions de descoberta local, com ara enviar contingut a una pantalla, sovint depenen de trànsit multicast que de manera predeterminada no travessa una frontera encaminada. No obris tot el trànsit entre VLAN per resoldre un problema de descoberta. Identifica el protocol i afegeix l'excepció més limitada que admeti el sistema.

## Assigna VLAN i adreces

Assigna a cada grup un identificador VLAN i una subxarxa IP separada. Aquest **pla il·lustratiu** fa servir adreces reservades per a documentació i pressuposa que l'encaminador proporciona DHCP i DNS. No copiïs la taula a una xarxa activa sense comprovar si hi ha conflictes d'adreces.

| Xarxa | ID VLAN | Subxarxa | Passarel·la d'exemple |
|---|---:|---|---|
| **Administració** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Servidors** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Convidats** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Aquests rangs reservats per a documentació només il·lustren la disposició, tal com defineix la [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Fes servir adreces privades de la [RFC 1918](https://www.rfc-editor.org/info/rfc1918) al teu laboratori, amb una subxarxa no superposada per a cada VLAN. Anota al pla cada passarel·la real, l'interval DHCP, l'adreça DNS i la reserva de dispositius.

Els **ports d'accés** transporten la xarxa d'un dispositiu sense etiqueta VLAN. Els **ports troncals** transporten VLAN seleccionades amb etiqueta entre l'encaminador, el commutador i el punt d'accés. Configura el mateix ID VLAN i la mateixa opció nativa o sense etiqueta als dos extrems. La [guia VLAN de commutadors de Netgate](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) explica els ports troncals etiquetats, els ports d'accés sense etiqueta i els ID VLAN dels ports. Evita fer servir la VLAN 1 predeterminada per a l'administració quan el maquinari permeti una VLAN separada, tal com descriu la [guia de seguretat VLAN de Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/security.html).

El trànsit **natiu** o **sense etiqueta** en un tronc no duu etiqueta VLAN. Tots dos extrems l'han d'assignar a la mateixa VLAN, o un dispositiu podria quedar a la xarxa equivocada. Permet només les VLAN que necessiti l'enllaç. Desactiva els ports del commutador que no s'utilitzin o assigna'ls a una xarxa restringida. Netgate també desaconsella tractar una VLAN com una frontera de seguretat completa quan un atacant controla un port del commutador. Protegeix els ports físics i les credencials dels dispositius, a més del trànsit encaminat.

## Crea una matriu de trànsit

Una VLAN per si sola separa dominis de difusió. **L'encaminament entre VLAN** a l'encaminador o al commutador de capa 3 encara necessita regles d'accés. Decideix quin dispositiu encamina entre VLAN. Si un commutador de capa 3 encamina localment, el trànsit entre les seves VLAN pot no arribar mai al tallafoc de l'encaminador. Aplica llistes de control d'accés equivalents al commutador o encamina pel tallafoc, i després prova el punt real on s'apliquen les regles. Comprova el sentit de l'ACL del commutador i si manté l'estat de les connexions. Moltes ACL de commutador comproven els paquets per separat en cada sentit, de manera que una connexió permesa pot necessitar una regla limitada per al trànsit de retorn. La [guia ACL de Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) descriu el sentit de la interfície i l'ordre de coincidència dels paquets. Fes servir l'inventari de dispositius per registrar les connexions que vols permetre. Les entrades següents són exemples, no un conjunt universal de regles.

| Origen | Destinació | Servei | Decisió |
|---|---|---|---|
| **Administració** | Interfície d'administració del servidor | TCP 443 | Permetre als dispositius d'administració aprovats |
| **Administració** | Interfícies d'administració de l'encaminador, el commutador i el punt d'accés | Els ports d'administració documentats | Permetre als dispositius d'administració aprovats |
| **IoT** | Gravadora de càmeres | Port documentat de la gravadora | Permetre només si cal |
| **IoT** | DNS i servei horari aprovats | DNS i NTP | Permetre només als serveis triats |
| **IoT** | Subxarxa d'administració | Qualsevol | Denegar |
| **Convidats** | Subxarxes privades | Qualsevol | Denegar |
| **Convidats** | DNS i Internet | DNS, trànsit web | Permetre mitjançant el resolutor i la passarel·la aprovats |

Inclou també els serveis propis de l'encaminador al pla. Una regla que bloqueja l'accés d'IoT a altres VLAN encara pot deixar accessible la interfície administrativa de l'encaminador. Restringeix els serveis d'administració a la xarxa d'administració. Comença només amb les regles d'autorització necessàries i una denegació predeterminada per a la resta del trànsit encaminat. Revisa les regles d'autorització generals existents abans de suposar que la configuració predeterminada denega res. Les [pràctiques recomanades de tallafocs de Netgate](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) indiquen que la LAN predeterminada de pfSense conté una regla d'autorització. Si fas servir pfSense, la seva [metodologia de regles](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) explica que les regles d'interfície filtren el trànsit que hi entra i que les connexions permeses creen un estat per al trànsit de retorn.

La taula d'exemple cobreix IPv4. Si la xarxa fa servir IPv6, assigna un prefix i una política IPv6 a cada VLAN, inspecciona els anuncis de l'encaminador i prova també les rutes IPv6 permeses i denegades. Bloquejar IPv4 no demostra l'aïllament d'IPv6. Si no penses encaminar IPv6, comprova la configuració IPv6 de l'encaminador i les adreces dels clients en lloc de suposar que IPv6 no existeix. Netgate documenta el [comportament del tallafoc IPv6](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) i els [anuncis de l'encaminador](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Configura una xarxa cada vegada

1. Tria la passarel·la de la VLAN. Si l'encamina l'encaminador o el tallafoc, crea-hi una interfície VLAN i assigna-li l'adreça de passarel·la. Si l'encamina un commutador de capa 3, crea la interfície VLAN en aquell commutador. Configura un àmbit DHCP a la passarel·la o un relé DHCP cap al servidor DHCP existent. Confirma que es pot arribar a un resolutor DNS aprovat. La [guia de configuració VLAN de Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) enumera els passos d'interfície i servei per a una passarel·la pfSense.
2. Si l'encaminador és la passarel·la VLAN, afegeix-hi aquella VLAN al tronc entre l'encaminador i el commutador. Si la passarel·la és el commutador de capa 3, deixa que el commutador tingui l'adreça de passarel·la de la VLAN i encamina cap a l'encaminador o el tallafoc mitjançant una xarxa de trànsit separada o un enllaç ascendent encaminat. Configura una ruta predeterminada del commutador cap a l'encaminador ascendent. Configura a l'encaminador una ruta de retorn per a cada VLAN allotjada al commutador, passant pel mateix commutador. Comprova la política del tallafoc de l'encaminador i el NAT de sortida d'aquestes subxarxes d'origen si necessiten Internet. No creïs la mateixa adreça de passarel·la ni el mateix àmbit DHCP als dos dispositius. La [guia d'encaminament entre VLAN de Cisco](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) mostra passarel·les VLAN allotjades al commutador. Netgate documenta les [rutes de retorn](https://docs.netgate.com/pfsense/en/latest/routing/static.html) i el [NAT de sortida](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) per a xarxes darrere d'un encaminador intern. Afegeix la VLAN al tronc corresponent entre el commutador i el punt d'accés si els clients sense fil necessiten aquesta xarxa.
3. Assigna a la VLAN un port d'accés de prova o un SSID sense fil. Connecta un dispositiu de prova no crític a aquell port o SSID.
4. Afegeix les regles del tallafoc o les llistes de control d'accés del commutador previstes al dispositiu que encamina la VLAN. Comprova que la resta del trànsit encaminat quedi denegat. Comprova el sentit de l'ACL i el trànsit de retorn si el commutador no manté l'estat. Prova l'accés a cada passarel·la i interfície d'administració, a cada subxarxa local i a IPv6 si n'hi ha. Permet només les rutes de la matriu de trànsit. Limita l'administració a la xarxa d'administració. Revisa l'ordre de les regles i elimina o restringeix les regles generals d'autorització només després que la ruta d'administració de prova funcioni.
5. Confirma que el dispositiu de prova rep una adreça, una passarel·la i un servidor DNS de la subxarxa prevista. Després fes les comprovacions de connexió següents abans de moure més dispositius.

No moguis l'últim dispositiu d'administració fins que funcioni la ruta de substitució. Desa la configuració funcional després que cada xarxa superi les proves. Si DHCP, DNS o l'accés d'administració falla, torna a connectar el dispositiu de prova al port o SSID original, restaura el darrer canvi del commutador o de l'encaminador des de la configuració desada i torna a provar la xarxa original abans de continuar.

## Prova l'aïllament i l'accés

Fes servir un servei que controlis i que sàpigues que escolta a la destinació. Des d'un dispositiu de prova amb Windows, substitueix l'adreça i el port d'exemple per un servidor real i executa:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

El camp **`TcpTestSucceeded`** indica si s'ha completat una connexió TCP. La [referència Microsoft de Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) documenta els paràmetres `-ComputerName` i `-Port`. Una connexió fallida, per si sola, no demostra que una regla del tallafoc hagi funcionat. Pot ser que el servei estigui aturat o que el tallafoc de l'amfitrió rebutgi el trànsit. Comprova el servei de destinació i el registre del tallafoc de xarxa abans de treure'n conclusions.

Prova-ho des d'un dispositiu realment connectat a cada VLAN d'origen. Abans de cada prova, registra'n l'adreça d'origen, la passarel·la i el servidor DNS. Comprova una connexió permesa al servei previst, una connexió denegada a un servei intern fora de la matriu, una consulta DNS mitjançant el resolutor previst i l'accés a Internet quan estigui planificat. Per a una VLAN amb la passarel·la al commutador, comprova la ruta predeterminada del commutador, la ruta de retorn de l'encaminador i el camí de tornada des de la destinació si falla una connexió permesa. Repeteix les proves permeses i denegades amb adreces IPv6 si IPv6 és actiu. A pfSense, **Estat > Registres del sistema > Tallafoc** mostra les accions permeses i bloquejades enregistrades. La [guia de registres del tallafoc de Netgate](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) explica aquesta vista. Compara l'origen, la destinació, el port i la regla del registre amb la prova. Si la prova té èxit inesperadament, inspecciona les regles generals d'autorització i les entrades d'estat existents. Inicia una connexió nova després de canviar regles, ja que una connexió establerta pot continuar funcionant amb l'estat que ja té.

Per comprovar DNS a Windows, executa `nslookup example.com` i compara el servidor mostrat amb el resolutor previst. Després prova una consulta des d'un client convidat o IoT on DNS estigui restringit. Una consulta correcta no demostra per si sola que el client hagi fet servir el resolutor escollit, així que comprova el servidor que s'indica i un registre del tallafoc o del resolutor. Prova per separat l'accés directe a l'adreça d'administració de l'encaminador des d'un dispositiu IoT o de convidat com a cas que s'ha de denegar.

Els dispositius de la **mateixa VLAN** poden intercanviar trànsit sense passar pel tallafoc de l'encaminador. Si el punt d'accés ofereix aïllament local dels clients, prova'l per separat, i fes servir tallafocs d'amfitrió als servidors. Les proves del tallafoc entre VLAN no demostren l'aïllament dins d'una sola VLAN.

> **Resultat esperat:** cada dispositiu rep una adreça de la subxarxa prevista. Els serveis permesos funcionen. Els intents denegats coincideixen amb un bloqueig del tallafoc o amb un control equivalent documentat.

## Resolució de problemes

- **No hi ha adreça:** comprova la VLAN del port d'accés o de l'SSID, les etiquetes del tronc, l'àmbit DHCP i la interfície de passarel·la.
- **L'adreça funciona, però DNS falla:** comprova l'adreça del resolutor, la vinculació del servei de l'encaminador i la regla del tallafoc per al trànsit DNS.
- **Un dispositiu arriba inesperadament a una altra VLAN:** comprova les regles de l'encaminador, les regles generals d'autorització i si tots dos dispositius encara comparteixen una xarxa sense etiqueta.
- **No hi ha cap registre del tallafoc per al trànsit encaminat:** comprova si un commutador de capa 3 o una passarel·la alternativa ha encaminat la connexió abans que arribés al tallafoc.
- **Una VLAN amb la passarel·la al commutador arriba a xarxes locals, però no a Internet:** comprova la ruta predeterminada del commutador, les rutes de retorn de l'encaminador, la política del tallafoc i el NAT de sortida per a la subxarxa VLAN.
- **IPv4 es bloqueja, però la connexió funciona:** comprova les adreces IPv6, els anuncis de l'encaminador, les regles IPv6 i les entrades d'estat existents.
- **Una prova denegada caduca sense registre del tallafoc:** confirma que el servei de destinació està escoltant. Després inspecciona l'encaminament i la configuració dels registres. La [guia de resolució de problemes del tallafoc de Netgate](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) descriu les comprovacions dels registres i l'estat.
- **La transmissió o la descoberta deixa de funcionar:** identifica el protocol de descoberta i la ruta del controlador abans d'afegir una excepció limitada.

## Passos següents

Conserva l'inventari de dispositius i la matriu de trànsit amb el diagrama de xarxa. Revisa les regles quan afegeixis un servidor o un dispositiu IoT. Repeteix una prova de connexió permesa i una de denegada després de cada canvi de xarxa pertinent. Per als principis generals de disseny, torna a [segmentació de xarxa](/articles/how-to-perform-network-segmentation-for-improved-security/).
