---
title: "Open WebUI v0.12.4: llista de comprovació per a l’actualització i el control d’accés 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Fes una còpia de seguretat i actualitza Open WebUI a la versió v0.12.4. Després, prova la compartició de xats, els permisos d'exportació, les concessions de recursos, els comptes i l'accés a la xarxa."
genre: ["IA autoallotjada", "Ciberseguretat", "Administració de sistemes"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "actualització d'Open WebUI", "seguretat d'Open WebUI", "control d'accés d'Open WebUI", "IA autoallotjada", "actualització de Docker", "actualització de pip", "còpia de seguretat d'Open WebUI", "permisos d'Open WebUI", "rols d'Open WebUI", "grups d'Open WebUI", "permís d'exportació de xats", "xats compartits", "xats arxivats", "accés a la base de coneixement", "accés als models", "permisos d'eines", "seguretat de les claus API", "seguretat del compte d'administrador", "desactivar els registres", "autenticació del proxy invers", "accés VPN", "fixar la imatge del contenidor"]
---

**Open WebUI v0.12.4 inclou correccions de seguretat que els mantenidors encara no han detallat.** Les notes de la versió recomanen actualitzar les instal·lacions aviat i indiquen que publicaran avisos quan s'assignin CVE. Els canvis de compartició de xats i permisos que s'esmenten a continuació són els elements visibles a les notes de la versió, no una llista completa de les correccions de seguretat encara no divulgades. [Notes de la versió d'Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Punts clau

- **Fes una còpia de seguretat primer.** Conserva una còpia recuperable del volum de dades o de la base de dades i de les pujades abans de canviar l'aplicació.
- **Fixa la versió oficial.** Fes servir `ghcr.io/open-webui/open-webui:v0.12.4` per a la imatge Docker estàndard o `open-webui==0.12.4` per a pip.
- **Prova els permisos amb rols d'usuari reals.** Un botó ocult no demostra que l'API faci una comprovació d'autorització.
- **Mantén privat l'accés.** Exigeix autenticació a l'aplicació i limita l'accés a la xarxa mitjançant una VPN o un proxy invers autenticat.

## Abans d'actualitzar

**Prerequisits:** identifica el mètode d'instal·lació actual, la variant de la imatge del contenidor, la ubicació de les dades persistents, la base de dades externa, el proxy invers i el proveïdor d'autenticació. Programa una finestra d'interrupció i conserva la configuració actual del contenidor o la definició del servei. Reserva temps per provar una restauració en una instància separada. Les ordres següents són patrons documentats pel proveïdor i adaptats a aquesta versió fixada. No són el resultat d'una actualització real feta per a aquesta guia. [Actualitzar Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Fes inventari de l'emmagatzematge.** A la configuració Docker estàndard, `open-webui` es munta a `/app/backend/data`. Anota els muntatges vinculats, la base de dades externa, l'emmagatzematge d'objectes i les variables d'entorn personalitzades. Amb pip, localitza el directori de dades actiu de l'aplicació i la base de dades abans de canviar l'entorn. No donis per fet que una exportació de xat és una còpia de seguretat completa.
2. **Fes la còpia amb les escriptures aturades.** Atura l'aplicació o crea una instantània coherent de la base de dades. Després, copia el volum, qualsevol base de dades externa i les pujades a un emmagatzematge separat. El proveïdor documenta un arxiu del volum Docker. Adapta el nom del volum i la ruta de còpia al teu desplegament. Comprova que l'arxiu s'obre i assaja una restauració en una instància separada abans de confiar-hi. [Còpia de seguretat i restauració](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Llegeix les notes de la versió i la guia de migració.** Les notes de v0.12.4 no enumeren les correccions de seguretat pendents ni indiquen les versions afectades. No assignis cap CVE a aquestes correccions ni donis per fet que totes les versions anteriors a v0.12.4 estan afectades per una fallada concreta. La guia d'actualització adverteix de migracions de base de dades unidireccionals i de rèpliques amb versions barrejades. Si diversos treballadors o rèpliques comparteixen una base de dades, atura'ls alhora i segueix el [procediment de migració per a rèpliques múltiples](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Pot ser que una reversió necessiti la còpia de la base de dades anterior a l'actualització.

## Actualitza el paquet instal·lat

**Docker, procediment del proveïdor adaptat a una etiqueta fixada:** després de fer la còpia, baixa la imatge estàndard oficial i torna a crear el contenidor amb el *mateix* volum persistent, configuració i `WEBUI_SECRET_KEY`. L'exemple pressuposa el volum amb nom predeterminat i un proxy vinculat localment com a destinació. No enganxis la clau real a l'historial del shell. Proporciona-la mitjançant el mecanisme existent d'entorn protegit o de gestió de secrets. Conserva les opcions de GPU, Ollama, xarxa personalitzada, base de dades i altres de la instal·lació actual. [Actualitzar Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Etiquetes oficials de les imatges](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Comprova `./open-webui.env` abans d'executar-ho:** el fitxer ja ha d'existir, tenir permisos restrictius i contenir el teu `WEBUI_SECRET_KEY` actual i la configuració necessària. L'enllaç loopback és adequat per a un proxy al mateix host, no pas per a un proxy en una altra màquina. Amb Compose, canvia només la imatge del servei a l'etiqueta fixada i, tot seguit, executa `docker compose pull open-webui` i `docker compose up -d open-webui` dins del projecte existent. Mantén el mateix volum i la mateixa configuració d'entorn. Són ordres suggerides, no una migració provada de la teva instal·lació.

**pip, procediment del proveïdor amb versió fixa:** a l'entorn virtual existent, atura el servei, instal·la la versió exacta del paquet i reinicia'l amb el mateix directori de dades i entorn. Evita un segon entorn Python o una base de dades buida. La instrucció general del proveïdor fa servir `pip install -U open-webui`. La restricció de versió següent fixa aquesta llista a v0.12.4. [Actualitzar Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Inici ràpid](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Verifica el servei en execució, no només el paquet instal·lat.** Consulta la versió d'inici a `docker logs open-webui` o als registres del servei pip i compara-la amb la versió que mostra l'aplicació després d'iniciar sessió. La guia d'actualització del proveïdor recomana revisar els registres del contenidor i carregar la pàgina d'inici de sessió. Si la interfície mostra recursos antics, força l'actualització del navegador. Si l'inici informa d'un error de migració, mantén el servei fora de línia fins que en trobis la causa. No instal·lis un binari antic sobre una base de dades migrada sense comprovar les necessitats de restauració. [Comprovacions posteriors a l'actualització](https://docs.openwebui.com/getting-started/updating/)

## Comprova l'accés després de reiniciar

**Comportament indicat pel proveïdor:** v0.12.4 amaga Exporta la carpeta, Exporta els xats arxivats i Copia el xat als usuaris sense **Allow Chat Export**. També amaga els controls d'accés de models, prompts, eines, coneixement, habilitats, notes i carpetes als usuaris sense el permís de compartició corresponent. Els visitants d'una carpeta compartida deixen de rebre actualitzacions de xat en directe quan el propietari arxiva un xat. Els visitants d'un enllaç compartit deixen de rebre-les quan el propietari deixa de compartir tots els xats. Els controls ocults són un comportament de la interfície, no una prova d'una correcció al servidor per a una vulnerabilitat no especificada. [Notes de la versió](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Verificació recomanada per a l'operador:** amb un compte de prova sense permisos d'exportació ni de compartició, comprova que no apareguin les accions indicades. Amb un compte autoritzat, confirma que les accions previstes continuen funcionant. Crea un xat de prova no sensible en una carpeta compartida, consulta'l des d'un altre compte, arxiva'l com a propietari i confirma que l'altre usuari deixa de rebre actualitzacions noves. Repeteix-ho amb un enllaç compartit i **Unshare All Chats**. Torna a revisar les concessions desades i els enllaços antics. No donis per fet que el contingut arxivat o les còpies històriques s'han esborrat.

| Àrea de revisió | Què cal verificar |
|---|---|
| **Rols i grups** | Elimina membres i assignacions d'administrador obsolets. Comprova els permisos efectius d'un usuari que s'acaba d'aprovar i d'un usuari restringit. |
| **Models i eines** | Revisa les concessions d'accés de cada model, les eines adjuntes, els permisos per crear eines i les credencials del proveïdor. Prova-ho amb un compte que no sigui administrador. |
| **Coneixement i fitxers** | Inspecciona els col·laboradors de la base de coneixement, les concessions de recursos, els fitxers adjunts i la configuració de compartició. Comprova un compte al qual s'ha retirat l'accés. |
| **Xats i exportacions** | Revisa les carpetes compartides, els enllaços, els xats arxivats i les assignacions d'Allow Chat Export. Revoca els enllaços innecessaris. |

Aquestes comprovacions d'inventari són **recomanacions per a l'operador**, no noves garanties de v0.12.4. La [guia de reforç de seguretat](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) del proveïdor documenta rols per nivells, grups, concessions per recurs, permisos de l'espai de treball, claus API i ubicació de xarxa.

## Tanca les mancances dels comptes i de la xarxa

- **Registre, configuració del proveïdor:** desactiva el registre obert quan un administrador o proveïdor d'identitat crea els comptes. Comprova `ENABLE_SIGNUP` i els paràmetres persistents d'administrador amb la [guia de reforç de seguretat](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Mantén restrictives les normes d'aprovació per a comptes nous.
- **Claus API, revisió de l'operador:** inventaria les claus emeses, elimina les que no s'utilitzen i limita la creació i l'accés als endpoints als rols i rutes necessaris. Segons la guia del proveïdor, una clau actua amb els permisos de qui l'ha creat. Mantén les claus fora dels exemples i dels registres de l'aplicació.
- **Administradors, revisió de l'operador:** elimina comptes d'administrador abandonats, exigeix controls d'inici de sessió sòlids, revisa la disponibilitat de MFA i investiga canvis inesperats als comptes. Prova el procés de recuperació del compte abans de desactivar un administrador redundant.
- **Límit de xarxa, guia del proveïdor:** posa el servei darrere d'una VPN, un proxy d'accés o un proxy invers amb autenticació i una llista d'adreces IP permeses. No l'exposis públicament sense autenticació. Evita `WEBUI_AUTH=False` en un servei accessible. Un proxy invers sense autenticació pròpia no substitueix l'inici de sessió de l'aplicació. [Reforçar Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Abast:** aquesta llista s'aplica a la versió oficial d'Open WebUI i als mètodes d'instal·lació estàndard documentats. No verifica forks, imatges derivades ni paquets de tercers. Les notes de v0.12.4 no indiquen explotació activa. Consulta els [avisos de seguretat del projecte](https://github.com/open-webui/open-webui/security/advisories) per a divulgacions posteriors i les seves pròpies versions afectades i corregides. No atribueixis a v0.12.4 la correcció d'un avís anterior sense llegir-ne l'interval de versions.

## Fonts i referències

- [Notes de la versió d'Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Avisos de seguretat d'Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Actualitzar Open WebUI, incloent-hi còpies, reversions i migracions](https://docs.openwebui.com/getting-started/updating/)
- [Inici ràpid d'Open WebUI i etiquetes oficials de les imatges](https://docs.openwebui.com/getting-started/quick-start/)
- [Reforçar Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Actualitzacions i migracions per a rèpliques múltiples](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)
