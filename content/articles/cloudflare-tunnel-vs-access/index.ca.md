---
title: "Cloudflare Tunnel i Access: necessites tots dos?"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Entén les diferències entre Cloudflare Tunnel i Access, tria la protecció d'un tauler domèstic i evita publicar una aplicació privada sense autenticació."
genre: ["Seguretat de xarxa", "Allotjament propi", "Seguretat al núvol"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel i Access", "Cloudflare Zero Trust", "cloudflared", "aplicacions autoallotjades", "seguretat del homelab", "accés remot", "proveïdor d'identitat", "polítiques d'accés", "autenticació d'aplicacions", "nom d'amfitrió públic", "protecció de l'origen", "túnel de sortida", "tokens de servei", "Service Auth", "MFA", "tauler privat", "proxy invers", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Un servidor domèstic es connecta a una passarel·la al núvol per un pas transparent amb un punt de verificació d'identitat separat."
coverCaption: ""
---

**Cloudflare Tunnel** connecta l'aplicació amb Cloudflare. **Cloudflare Access** controla qui hi pot accedir. Per a un tauler domèstic privat exposat amb un nom d'amfitrió públic, fes servir tots dos. Un túnel funcional no afegeix per si sol una verificació d'identitat. La [guia de Cloudflare per publicar aplicacions](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) explica la diferència.

## Idees clau

- **Explica la ruta:** diferencia el connector, l'origen i la verificació d'identitat.
- **Configura una política:** permet l'accés de persones concretes a un tauler privat.
- **Avalua la protecció:** prova les rutes permeses, denegades i alternatives.
- **Dissenya l'accés:** documenta per separat els requisits dels visitants i de l'automatització.

## Abans de començar

**Públic:** propietaris de servidors domèstics que volen protegir un tauler de navegador. L'exemple pressuposa un domini actiu a Cloudflare, una aplicació web local funcional i permís per administrar tots dos. **Esforç estimat:** 20–30 minuts per a l'exercici de política després de configurar el connector. **Dificultat:** de principiant a intermèdia.

**Ordre de lectura:** comença pels rols dels productes, segueix una petició i configura i revisa una política petita. Acaba redactant una especificació d'accés per al teu servei.

## Què fa cada producte

L'**origen** és el servidor que executa l'aplicació. El connector **`cloudflared`** inicia connexions des de la teva infraestructura cap a Cloudflare. Per tant, l'origen no necessita una adreça IP pública i encaminable. Les peticions i les respostes viatgen per la connexió establerta. [Visió general de Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Pregunta | Tunnel | Access |
|---|---|---|
| **Com arriba Cloudflare al meu servidor?** | Estableix la connexió | No substitueix la connectivitat amb l'origen |
| **Qui obté accés?** | Per si sol no proporciona un inici de sessió | Avalua les polítiques d'accés configurades |
| **Què configuro?** | Connector i ruta de l'aplicació | Aplicació, proveïdor d'identitat i polítiques |
| **Què demostra l'èxit?** | Es pot arribar a l'origen per la ruta | Una petició ha complert la política configurada |

Un **proveïdor d'identitat (IdP)** autentica el visitant. Una **política d'Access** defineix una acció i els criteris de coincidència. Allow admet els usuaris coincidents. Bypass desactiva l'aplicació d'Access per al trànsit coincident. [Referència de polítiques d'Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Segueix una petició del navegador

Per a **`dashboard.example.com`**, la ruta lògica és:

```text
Navegador -> Cloudflare Access -> connexió del túnel -> cloudflared -> tauler
                     |
                     +-> proveïdor d’identitat quan calgui autenticar-se
```

El **connector inicia la connexió de túnel de sortida** des de la teva xarxa. Després, les peticions del navegador arriben a l'origen per aquesta connexió establerta. Una connexió de sortida que transporta peticions entrants de l'aplicació és la raó principal per la qual Tunnel funciona sense reenviar un port convencional de l'origen. [Model de connexió de Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Els permisos de l'aplicació** són una altra decisió. L'accés a un tauler no determina automàticament qui pot canviar-ne la configuració o esborrar-ne les dades. Si l'aplicació té rols de consulta i d'administració, configura'ls i prova'ls per separat.

Per exemple, **un familiar amb accés de consulta** ha de poder veure l'estat de les còpies de seguretat, mentre que tu has de poder canviar-ne les destinacions. Anota aquests requisits abans de triar identitats. Dues persones que superen la mateixa comprovació d'Access no haurien de rebre automàticament els mateixos privilegis a l'aplicació.

## Quan necessites tots dos

**El públic determina la protecció.** Compara aquestes configuracions abans de publicar una ruta:

| Públic previst | Configuració suggerida | Revisa-ho abans d'usar-la |
|---|---|---|
| **Qualsevol persona que llegeixi un lloc públic** | Tunnel si cal per connectar amb l'origen | L'exposició pública és intencionada |
| **Tu i alguns familiars** | Tunnel i Access | Permet només les identitats previstes |
| **Un origen públic existent** | Access amb protecció separada de l'origen | L'accés directe a l'origen no ha d'evitar la comprovació |
| **Un script programat** | Tunnel i una política Service Auth | El client admet el mètode d'autenticació |

**Access sense Tunnel** funciona amb un origen que ja és accessible. Protegeix també les rutes alternatives al servidor. Cloudflare recomana crear primer l'aplicació d'Access quan publiques una ruta de túnel nova. [Requisits d'aplicacions autoallotjades](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Per a un tauler domèstic privat accessible mitjançant un nom d'amfitrió públic, comença amb Tunnel i Access.*

## Configura una política per al tauler

Fes servir aquesta **configuració guiada** per a dos visitants previstos. Substitueix les dues adreces d'exemple per identitats que controlis. Crea l'aplicació d'Access abans d'afegir la ruta pública del túnel.

1. **Aplicació:** obre Zero Trust → Access controls → Applications i crea una aplicació autoallotjada amb un nom d'amfitrió públic.
2. **Nom d'amfitrió:** introdueix el nom dedicat al tauler. Deixa la ruta sense restriccions en aquest exemple per a tot el nom d'amfitrió.
3. **Política:** crea una política Allow anomenada `Dashboard viewers`.
4. **Selector d'identitat:** afegeix una regla Include amb Emails. Substitueix `alice@example.com` i `bob@example.com` per les dues adreces previstes.
5. **Inici de sessió:** selecciona el proveïdor d'identitat que fan servir els visitants i tria una durada de sessió deliberada.
6. **Ruta:** desa l'aplicació i connecta el nom d'amfitrió al tauler mitjançant el túnel.

El [flux oficial de configuració d'aplicacions](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) documenta aquests paràmetres. **Resultat esperat:** un visitant nou s'ha d'autenticar abans d'arribar a l'aplicació. Completa la prova d'identitat denegada següent abans de confiar en la política.

## Interpreta la lògica de les regles

**Include** combina alternatives amb OR. **Require** afegeix condicions obligatòries amb AND. **Exclude** elimina els usuaris coincidents. Afegir una altra condició Include amplia el grup admès. [Semàntica de les regles d'Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Fragment de política | Efecte lògic |
|---|---|
| **Include Alice or Bob** | Una de les identitats indicades és suficient |
| **Include Alice, Include a country** | També s'admeten persones del país coincident |
| **Include Alice, Require a country** | Alice també ha de complir la condició del país |

**Exercici de revisió:** el requisit només anomena Alice i Bob, però un company afegeix un país com a altra condició Include. Rebutja el canvi perquè admet un grup addicional. La geografia no demostra que algú formi part de la teva llar.

## Autentica scripts programats

Un **token de servei** conté un Client ID i un Client Secret per a peticions automatitzades. Configura la política de l'aplicació perquè accepti el token mitjançant **Service Auth**. Crear un token sense la política corresponent no dona accés a l'aplicació. [Tokens de servei de Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Per a un script de còpia de seguretat o una comprovació de monitoratge, desa el **secret** a l'emmagatzematge protegit de credencials de l'eina. Assigna a cada integració un nom de token diferent i una data de caducitat deliberada. Rota o revoca el token quan retiris la integració. La documentació dels tokens de servei descriu aquestes operacions del cicle de vida.

**Comprova explícitament la compatibilitat del client.** Una eina que espera una resposta d'API no necessàriament pot gestionar un inici de sessió interactiu al navegador. Abans de triar la política, confirma que admeti capçaleres de petició o un altre mètode d'autenticació compatible.

## Prova les decisions d'accés

Fes servir aquests **controls d'acceptació** per al desplegament:

| Control | Evidència que cal registrar |
|---|---|
| **Visitant sense iniciar sessió** | Access intercepta una petició d'una sessió de navegador nova |
| **Identitat permesa** | L'aplicació prevista es carrega després d'iniciar sessió |
| **Identitat denegada** | Un compte no inclòs no accedeix a l'aplicació |
| **Ruta alternativa** | Els noms DNS antics i els ports de l'origen no ofereixen accés imprevist |
| **Automatització** | El client aprovat funciona i una petició sense credencial falla |

**Una pantalla d'inici de sessió visible** només demostra que una ruta ha trobat autenticació. Prova també el cas denegat i les rutes alternatives. Són comprovacions suggerides, no resultats d'un exemple desplegat.

## Comprova el límit de l'origen

Un **origen que confia en la identitat d'Access** ha de validar el token d'aplicació signat. Cloudflare l'envia a la capçalera **`Cf-Access-Jwt-Assertion`**. La presència de la capçalera no en demostra l'autenticitat. [Validació JWT de Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Un **JSON Web Token (JWT)** conté afirmacions signades. Quan integris la identitat d'Access amb un origen, fes servir el mètode de validació documentat, incloent-hi l'emissor esperat i l'audiència de l'aplicació. Descodificar un token i llegir-ne el camp de correu electrònic no és una validació suficient.

**Issuer** identifica l'autoritat que emet el token. **Audience** identifica l'aplicació prevista. Comprova la validesa i la caducitat amb una biblioteca de validació compatible, en lloc d'implementar des de zero les comprovacions de signatura.

**Defineix clarament el límit:** identifica on es produeix la validació i quines rutes arriben a l'aplicació. Una antiga redirecció de port o un nom d'amfitrió alternatiu requereix una revisió pròpia, encara que el nom principal superi totes les proves del navegador.

## Resol discrepàncies de polítiques

| Observació | Comprovació següent |
|---|---|
| **Un visitant inesperat hi accedeix** | Revisa les condicions Include, les polítiques Bypass i la cobertura del nom d'amfitrió |
| **Es denega l'accés a un visitant previst** | Compara la identitat autenticada amb els valors exactes del selector |
| **Un script rep una pàgina d'inici de sessió** | Revisa la credencial i la política Service Auth |
| **Un visitant admès canvia la configuració** | Revisa els rols assignats per la mateixa aplicació |

**El comportament de les sessions** també afecta les proves repetides. Access té diverses durades de sessió, incloses les sessions d'aplicació i les globals. Anota la configuració i fes servir una sessió nova quan provis una identitat diferent. [Gestió de sessions d'Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Escriu l'especificació d'accés

Prepara una **especificació breu** abans d'afegir un altre servei:

```text
Servei i nom d'amfitrió:
Identitats humanes permeses:
Rols necessaris de l'aplicació:
Credencial d'automatització i caducitat:
Altres rutes cap a l'origen:
Lloc on es validen els tokens d'Access:
Resultat de la prova amb identitat permesa:
Resultat de la prova amb identitat denegada:
```

**Criteri de compleció:** un altre administrador ha d'entendre qui obté accés, com s'autentica cada client i quina evidència demostra la denegació. Si més endavant afegeixes una integració de monitoratge, actualitza'n la credencial i repeteix la comprovació de la petició sense autenticació.

## Passos següents

Segueix la [guia de configuració de Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) per configurar el connector i aplica després el [flux oficial de configuració de l'aplicació Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). Si tens connexió mòbil, consulta les [limitacions de reenviament de ports de T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) abans de triar l'accés remot.
