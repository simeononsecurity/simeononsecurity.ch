---
title: "Per què Tailscale fa servir un relé: connexions directes, DERP i relés entre iguals"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Descobreix per què Tailscale fa servir un relé, com llegir la sortida de status i netcheck i quan cal investigar una connexió DERP o de relé entre iguals."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "relé Tailscale", "DERP", "relé entre iguals de Tailscale", "connexió directa", "WireGuard", "traversal de NAT", "NAT difícil", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "rendiment VPN", "accés remot", "tailnet", "xarxa domèstica", "latència del relé", "xifratge d'extrem a extrem"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Dos portàtils en illes separades intercanvien paquets xifrats a través d'un relé central mentre una ruta directa està interrompuda."
coverCaption: ""
---

**Tailscale fa servir un relé** quan els dispositius no han establert una connexió directa. Una connexió DERP breu durant l'inici és normal. L'ús persistent d'un relé sovint reflecteix condicions de NAT o del tallafoc que afecten la ruta entre els dispositius. Les connexions directes, DERP i de relé entre iguals mantenen totes el xifratge d'extrem a extrem de WireGuard. [Tipus de connexió de Tailscale](https://tailscale.com/docs/reference/connection-types).

## Idees clau

- **Reconeix la ruta:** distingeix les connexions directes, DERP i els relés entre iguals.
- **Recull proves:** executa sondes per al peer i comprovacions de xarxa als dos extrems.
- **Analitza el patró:** compara parelles de dispositius i condicions de xarxa.
- **Tria un canvi:** justifica'l amb una càrrega de treball mesurada i una nova prova.

## Abans de començar

**Requisits previs:** dos dispositius registrats i connectats, i un terminal amb la interfície de línia d'ordres de Tailscale, o **CLI**. Només necessites accés d'administració si la investigació porta a canviar la configuració.

**Temps estimat:** cinc minuts per a les comprovacions bàsiques, seguits de 15–20 minuts per a l'exercici de comparació. **Dificultat:** principiant per observar i intermèdia per fer canvis de xarxa. Defineix primer el problema, per exemple una còpia de seguretat lenta o una resposta retardada del terminal.

## Connexió directa, DERP i relé entre iguals

Un **tailnet** és la teva xarxa de Tailscale. Els dispositius intenten establir connectivitat UDP directa. Hi ha relés disponibles quan falla la ruta directa. Tailscale torna a comprovar les opcions de connexió periòdicament. [Establiment de la connexió](https://tailscale.com/docs/reference/connection-types).

| Ruta | Recorregut del trànsit | Implicació habitual |
|---|---|---|
| **Directa** | Entre els dos dispositius | Normalment és la ruta preferida pel rendiment |
| **Relé DERP** | A través de la infraestructura de relés de Tailscale | Afegeix un intermediari quan falla l'accés directe |
| **Relé entre iguals** | A través d'un dispositiu configurat al teu tailnet | Una alternativa que administres tu |

El **rendiment de DERP** depèn en part de la ruta addicional i de la capacitat compartida del servei. Tailscale documenta límits de cabal per compartir els recursos DERP de manera justa. No hi ha una velocitat universal del relé que permeti predir la durada d'una transferència de fitxers. [Resolució de problemes de rendiment de Tailscale](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Entén la negociació de la connexió

El **traversal de NAT** és el procés per establir una ruta utilitzable a través de dispositius que tradueixen adreces. Tailscale inicia la comunicació mitjançant DERP mentre negocia una ruta directa. Si falla la connectivitat directa, un relé entre iguals configurat i disponible ofereix una altra opció. Tailscale torna a comprovar les opcions amb el temps. [Establiment de la connexió](https://tailscale.com/docs/reference/connection-types).

**NAT difícil** descriu un comportament d'assignació que complica el traversal. Les condicions als dos extrems són importants. Dos dispositius darrere d'encaminadors diferents no necessàriament es comporten igual, encara que totes dues xarxes facin servir adreces privades. [Connectivitat dels dispositius](https://tailscale.com/docs/reference/device-connectivity).

Per a **un portàtil que es desplaça**, la ruta al servidor de casa pot canviar quan passes de la Wi-Fi de casa a la xarxa d'un hotel. Anota quina xarxa feies servir durant l'observació. Una connexió directa d'ahir no demostra quina és la ruta d'avui.

## Comprova la connexió actual

Substitueix **`home-server`** pel nom de Tailscale o l'adreça del peer:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** comprova la connectivitat amb el peer indicat. **`tailscale status`** mostra els peers i els detalls de les connexions. **`tailscale netcheck`** informa de les condicions de xarxa del dispositiu on s'executa l'ordre. La [referència de la CLI de Tailscale](https://tailscale.com/docs/reference/tailscale-cli) documenta aquestes ordres.

| Indicador de sortida | Interpretació |
|---|---|
| **`direct`** | El trànsit cap a aquest peer fa servir una ruta directa |
| **`relay`** | El trànsit cap a aquest peer passa per DERP |
| **`peer-relay`** | El trànsit fa servir un relé entre iguals configurat |
| **Un primer pong de DERP** | Revisa els resultats posteriors abans de decidir que la ruta continua passant pel relé |

Aquestes etiquetes provenen de la [documentació dels tipus de connexió](https://tailscale.com/docs/reference/connection-types). **Primer genera trànsit** i després inspecciona el peer que t'interessa. Les ordres anteriors són exemples, no resultats enregistrats d'una prova de rendiment.

## Interpreta un canvi de ruta

Aquesta **seqüència il·lustrativa** omet les adreces i els temps per centrar-se en el canvi de connexió:

```text
Primera resposta:    mitjançant DERP
Resposta posterior:  mitjançant un endpoint directe
Estat posterior:     directe
```

**Interpretació:** la negociació ha funcionat durant aquesta observació. La primera resposta, tota sola, hauria portat a un diagnòstic erroni. Si les respostes posteriors i l'estat continuen indicant un relé, anota l'ús persistent del relé per a aquesta parella de dispositius i període de prova.

**Abast de la sonda:** un ping de Tailscale correcte confirma la connectivitat amb el peer per a aquella sonda. No demostra que el tauler, el servei de fitxers o el dimoni SSH acceptin trànsit de l'aplicació. Prova per separat l'aplicació que falla abans de dir que el problema està resolt.

## Què indica netcheck

Executa **`tailscale netcheck` als dos dispositius**. Compara aquests camps amb la [referència de connectivitat dels dispositius](https://tailscale.com/docs/reference/device-connectivity):

| Camp | Interpretació útil |
|---|---|
| **`UDP`** | Si la sonda ha observat connectivitat UDP de sortida |
| **`MappingVariesByDestIP`** | Les assignacions externes variables poden indicar un traversal de NAT difícil |
| **`IPv6`** | Si el dispositiu té connectivitat IPv6 utilitzable |
| **`PortMapping`** | Si hi ha un mecanisme d'assignació de ports compatible |

**Un sol camp no permet dictaminar.** La disponibilitat d'un mecanisme d'assignació no demostra que funcioni la ruta fins a un peer concret. Una etiqueta de relé tampoc identifica quin encaminador ha provocat el problema. Compara tots dos extrems i els resultats reals dels ping.

El **NAT de l'operador** és rellevant quan la traducció d'adreces de la xarxa superior queda fora del teu control, tal com expliquem a l'article sobre el [reenviament de ports de T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). No donis per fet que totes les connexions darrere del NAT d'un operador es comporten igual.

## Compara tres parelles de dispositius

Si en tens un, fes servir un **tercer dispositiu registrat** per obtenir més proves. El patró següent és hipotètic, no és un resultat mesurat:

| Parella de dispositius | Ruta observada |
|---|---|
| **Portàtil cap al servidor de casa** | DERP |
| **Portàtil cap a un altre servidor** | Directa |
| **Servidor de casa cap a un altre servidor** | DERP |

**Hipòtesi de treball:** investiga primer la xarxa del servidor de casa, perquè les dues rutes observades on participa han continuat fent servir un relé. És una pista, no una prova. Cada parella negocia separadament i el servidor de comparació té les seves pròpies condicions de xarxa.

**Observació següent:** recull la sortida de netcheck als tres dispositius i repeteix la prova entre el portàtil i el servidor de casa des d'una altra xarxa que controlis. Si la ruta canvia, anota exactament quina xarxa ha canviat. No atribueixis el resultat a una regla concreta del tallafoc abans de provar-la.

**Exercici:** la connexió entre el portàtil i el servidor de casa és directa, però la transferència de fitxers continua sent lenta. Aquesta observació ja no encaixa amb una explicació basada en un relé. Abans de canviar-ne la configuració, comprova la connexió de pujada subjacent, la càrrega del servidor, l'emmagatzematge i el comportament de l'aplicació.

## Tria un canvi específic

Comença amb una **prova comparativa** en una altra xarxa que controlis. Si el mateix peer es connecta directament, tens proves útils sobre la ruta de xarxa original. Revisa les restriccions UDP i la configuració de NAT abans de canviar ajustos de DNS o de l'aplicació que no hi estan relacionats.

**Canvia una sola variable**, repeteix les comprovacions i mesura la mateixa càrrega de treball. Anota el sentit de la transferència, la mida del fitxer, el temps transcorregut i el tipus de connexió. Així podràs distingir la millora de la ruta d'un canvi independent en la càrrega del servidor o de l'emmagatzematge.

Els **canvis del tallafoc** han de seguir les recomanacions específiques de la plataforma i basar-se en les proves recollides. Obrir un port d'aplicació a Internet públic no millora per si sol la ruta de transport de Tailscale. Limita els canvis al trànsit necessari i a la xarxa que administres. [Recomanacions de tallafoc de Tailscale](https://tailscale.com/docs/integrations/firewalls).

| Troballa | Canvi que val la pena avaluar |
|---|---|
| **La sonda UDP falla** | Revisa les restriccions UDP de sortida d'aquesta xarxa |
| **L'assignació varia segons la destinació** | Revisa el comportament de NAT als equips que administres |
| **Ruta directa, aplicació lenta** | Investiga l'amfitrió, la connexió subjacent i la càrrega de treball |
| **El relé funciona i l'experiència és acceptable** | Mantén la configuració i documenta el valor de referència |

*Prioritza una millora mesurada abans que canviar la configuració només per eliminar l'etiqueta de relé.*

## Avalua un relé entre iguals

Un **relé entre iguals** necessita un amfitrió adequat, un port UDP accessible i una política d'accés que n'autoritzi l'ús. Tant el relé com els clients participants necessiten Tailscale 1.86 o posterior. Revisa les plataformes d'amfitrió compatibles abans d'assignar-hi un dispositiu. [Requisits dels relés entre iguals](https://tailscale.com/docs/features/peer-relay).

**La ubicació en determina la utilitat.** Un dispositiu darrere del mateix límit de xarxa inaccessible no ajudarà els altres peers fins que es pugui arribar al port del relé.

**Cost de manteniment:** algú ha de mantenir el relé en línia, actualitzat i amb recursos suficients. Si administres la xarxa de tant en tant i la latència és acceptable, compara aquesta càrrega amb el benefici mesurat. Si fas transferències grans sovint, mesura la càrrega de treball a través del relé proposat abans d'adoptar-lo.

## Comprova els efectes del trànsit compartit

El **trànsit agregat** mereix atenció quan un encaminador de subxarxa o un node de sortida transporta diverses càrregues de treball mitjançant DERP. Tailscale documenta casos en què un gran volum de trànsit retransmès retarda el trànsit sensible a la latència que comparteix la connexió. [Resolució de problemes de NAT difícil](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Exercici de comparació:** observa la sessió interactiva abans, durant i després d'una còpia de seguretat gran. Mantén fixa la parella de punts finals i anota la ruta cada vegada. Els retards que apareixen durant la transferència justifiquen investigar la càrrega compartida, però no en demostren la causa exacta.

**Tria la prova següent** a partir de l'observació. Comprova la saturació de l'enllaç i la càrrega de l'amfitrió. Després, avalua una ruta directa o la separació de serveis sensibles a la latència si la topologia ho permet. No tractis un símptoma de DNS com una prova automàtica d'un error de configuració de DNS.

## Un relé és un node de sortida?

Un **node de sortida** encamina el trànsit general d'Internet d'un client a través d'un dispositiu seleccionat del tailnet. Un relé transporta trànsit entre peers de Tailscale. Triar un node de sortida no garanteix una ruta directa fins a aquest dispositiu. [Documentació dels nodes de sortida](https://tailscale.com/docs/features/exit-nodes).

## Crea un registre de diagnòstic

Desa un **registre breu d'abans i després** per al problema real:

```text
Data i versions de Tailscale:
Dispositius d'origen i de destinació:
Xarxes que fa servir cada dispositiu:
Rutes inicial i estabilitzada de la connexió:
Observacions de netcheck als dos extrems:
Càrrega de treball, sentit i temps transcorregut:
Canvi únic provat:
Resultat de la nova prova:
Decisió de mantenir o revertir el canvi:
```

**Criteri de finalització:** el registre vincula un símptoma concret amb observacions, una hipòtesi i una nova prova mesurada. «El relé ha desaparegut» és incomplet si l'aplicació continua sent lenta. «La còpia de seguretat compleix el temps requerit mitjançant DERP» és un resultat vàlid si el requisit és explícit.

**Fes servir `tailscale netcheck` com a prova, no com a veredicte.** L'ordre descriu la xarxa que veu un únic dispositiu. La ruta establerta correspon a una parella de dispositius i a una càrrega de treball. Abans de canviar la configuració del tallafoc o de NAT, registra tots dos extrems, l'última línia de `tailscale status` i la mesura de l'aplicació.

## Passos següents

Anota la ruta fins al peer important i prova la càrrega de treball abans de canviar la configuració de xarxa. Per a la pregunta separada sobre qui opera la infraestructura de coordinació, llegeix [Tailscale i Headscale](/articles/tailscale-vs-headscale-comparison-guide/).
