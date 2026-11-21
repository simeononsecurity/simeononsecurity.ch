---
title: "Bones pràctiques de seguretat amb Python"
date: 2023-08-01
lastmod: 2026-11-20
toc: true
draft: false
description: "Aprèn les pràctiques essencials de seguretat amb Python per protegir el codi i les dades davant de possibles amenaces, preservar la informació i la integritat dels sistemes i generar confiança."
genre: ["Seguretat amb Python", "Seguretat del codi", "Protecció de dades", "Desenvolupament de programari", "Ciberseguretat", "Programació segura", "Desenvolupament web", "Privadesa de dades", "Seguretat d'aplicacions", "Seguretat informàtica"]
tags: ["seguretat amb Python", "bones pràctiques", "seguretat del codi", "protecció de dades", "integritat del sistema", "programació segura", "privadesa de dades", "seguretat d'aplicacions", "ciberseguretat", "desenvolupament web", "desenvolupament de programari", "programació Python", "programació segura", "xifratge de dades", "control d'accés basat en rols", "gestió segura de contrasenyes", "validació d'entrades", "prevenció d'injecció SQL", "seguretat de bases de dades", "gestió de dependències", "registre i supervisió", "formació de desenvolupadors", "intèrpret de Python", "documentació de seguretat de Python", "xifratge AES", "xifratge TLS", "OWASP", "NIST", "Snyk"]
cover: "/img/cover/An_illustration_of_a_shield_protecting_Python.webp"
coverAlt: "Il·lustració d'un escut que protegeix el codi i les dades de Python, símbol de les bones pràctiques de seguretat amb Python."
coverCaption: "Protegeix el codi i les dades de Python amb aquestes bones pràctiques."
---
**Bones pràctiques de seguretat amb Python: protecció del codi i les dades**

## Introducció

Python és un llenguatge de programació potent i versàtil que s'utilitza àmpliament en molts àmbits, com ara el desenvolupament web, l'anàlisi de dades i l'aprenentatge automàtic. Tot i això, com qualsevol altre programari, les aplicacions Python són susceptibles de patir vulnerabilitats de seguretat. En aquest article parlarem de les [**bones pràctiques de seguretat amb Python**](https://simeononsecurity.com/articles/secure-coding-standards-for-python/) per ajudar-te a protegir el codi i les dades davant de possibles amenaces.

______

## Per què és important la seguretat amb Python

Garantir la **seguretat de les aplicacions Python** és essencial per diversos motius:

1. **Protecció de dades**: les aplicacions Python sovint gestionen **dades sensibles**, com ara informació d'usuaris, registres financers o propietat intel·lectual. Una bretxa de seguretat pot provocar **robatori de dades** o **accés no autoritzat**, amb conseqüències greus.

2. **Integritat del sistema**: les vulnerabilitats del codi Python es poden explotar per obtenir **accés no autoritzat als sistemes**, **manipular dades** o **interrompre serveis**. Si apliques les **bones pràctiques de seguretat**, pots protegir la **integritat dels sistemes** i impedir activitats no autoritzades.

3. **Reputació i confiança**: les bretxes de seguretat no sols perjudiquen la teva organització, sinó que també **erosionen la confiança dels clients i usuaris**. Si dones prioritat a la seguretat, demostres el compromís de **protegir-ne els interessos i les dades** i reforces la reputació com a proveïdor fiable.

Les mesures de seguretat sòlides a les aplicacions Python ajuden a reduir els riscos i garanteixen la **confidencialitat, la integritat i la disponibilitat de les dades**. Has d'establir una **base de seguretat sòlida** per protegir-te de les **amenaces cibernètiques** i mantenir la confiança dels usuaris i les parts interessades.

______

## [Bones pràctiques de seguretat amb Python](https://simeononsecurity.com/articles/secure-coding-standards-for-python/)

Per millorar la seguretat de les aplicacions Python, segueix aquestes bones pràctiques:

### 1. Mantén l'intèrpret de Python actualitzat

Si actualitzes regularment l'**intèrpret de Python** a l'última versió estable, disposaràs dels **pegats de seguretat** i les **correccions d'errors** més recents. La comunitat de Python treballa activament per resoldre vulnerabilitats i publica actualitzacions per millorar la **seguretat i l'estabilitat** del llenguatge. Descarrega l'última versió al [lloc web de Python](https://www.python.org/downloads/).

Mantenir l'intèrpret de Python actualitzat et permet beneficiar-te de les **millores de seguretat més recents**, que resolen vulnerabilitats conegudes. Aquestes actualitzacions estan pensades per **reduir els riscos** i protegir les aplicacions davant d'atacs potencials. També et permeten aprofitar les noves funcions i millores de les versions recents de Python.

Per exemple, si fas servir Python 3.7 i es descobreix una vulnerabilitat de seguretat crítica, la comunitat de Python publicarà un pegat específic per corregir-la. Si actualitzes l'intèrpret a una versió més recent, com ara Python 3.9, el codi queda protegit davant dels problemes de seguretat coneguts.

Actualitzar l'intèrpret de Python és senzill. Ves a la [pàgina de baixades de Python](https://www.python.org/downloads/) i tria l'instal·lador adequat per al sistema operatiu. Segueix les instruccions d'instal·lació per actualitzar l'intèrpret a l'última versió.

Comprova periòdicament si hi ha actualitzacions i converteix l'actualització regular de l'intèrpret de Python en una bona pràctica per anticipar-te als possibles riscos de seguretat.

### 2. Aplica pràctiques de programació segura

Les **pràctiques de programació segura** redueixen la probabilitat d'introduir vulnerabilitats de seguretat al codi Python. Si les segueixes, pots reforçar la **postura de seguretat** de les aplicacions i protegir-les davant de vectors d'atac habituals. Aquestes són algunes pràctiques clau:

- **Validació d'entrades**: **valida totes les entrades dels usuaris** per impedir **atacs d'injecció** i altres problemes de seguretat relacionats amb les entrades. Aplica tècniques com ara **llistes d'autorització**, **neteja de les entrades** i **consultes parametritzades** per garantir que les dades de l'usuari s'hagin validat i siguin segures. Per exemple, quan acceptis dades d'un formulari web, valida-les i neteja-les abans de processar-les o desar-les en una base de dades. Això ajuda a evitar que codi maliciós o entrades inesperades comprometin l'aplicació.

- **Evita la injecció de codi**: no executis mai **codi proporcionat per l'usuari** sense validar-lo i netejar-lo adequadament. Els **atacs d'injecció de codi** es produeixen quan un atacant aconsegueix injectar i executar codi arbitrari dins del context de l'aplicació. Per impedir-ho, avalua i valida amb cura qualsevol codi que proporcionin els usuaris abans d'executar-lo. Fes servir pràctiques de programació segura i biblioteques que protegeixin de les vulnerabilitats d'injecció de codi.

- **Gestió segura de contrasenyes**: gestiona les contrasenyes de manera segura. **Calcula el hash i afegeix sal a les contrasenyes** amb **algorismes de hash** adequats i **tècniques d'estirament de claus**. Es desaconsella fermament desar contrasenyes en text pla perquè exposa els usuaris a riscos importants. En canvi, **desa només els hashes de les contrasenyes** i protegeix-ne l'emmagatzematge. Fes servir algorismes de hash forts com **bcrypt** o **Argon2** i valora afegir-hi **salt** i **pepper** per reforçar encara més la seguretat. Una gestió segura de contrasenyes protegeix les credencials dels usuaris fins i tot si la base de dades queda compromesa.

Les pràctiques de programació segura no es limiten a aquests exemples. Mantén-te alerta i segueix les últimes directrius i recomanacions de seguretat perquè el codi Python continuï sent segur.

### 3. Implementa el control d'accés basat en rols (RBAC)

El **control d'accés basat en rols (RBAC)** és un model de seguretat potent que restringeix l'accés als recursos segons els rols assignats als usuaris. Si implementes RBAC a les aplicacions Python, garanteixes que **els usuaris només tinguin els privilegis necessaris** per fer les tasques assignades, **redueixes el risc d'accés no autoritzat** i **limites la superfície d'atac**.

En RBAC, cada usuari té assignat un o més rols, i cada rol està associat a permisos i drets d'accés concrets. Per exemple, una aplicació web pot tenir rols com ara **administrador**, **usuari** i **convidat**. El rol d'**administrador** pot tenir accés complet a totes les funcions, el d'**usuari** pot tenir accés limitat i el de **convidat** pot tenir accés mínim o només de lectura.

Implementar RBAC inclou diversos passos:

1. **Identifica els rols**: analitza les funcions de l'aplicació i determina els diferents rols que poden tenir els usuaris. Considera els permisos i privilegis específics de cada rol.

2. **Assigna els rols**: assigna rols als usuaris segons les responsabilitats i el nivell d'accés que necessiten. Pots fer-ho amb sistemes de gestió d'usuaris o bases de dades.

3. **Defineix els permisos**: especifica els permisos associats a cada rol. Per exemple, un administrador pot crear, llegir, actualitzar i suprimir registres, mentre que un usuari pot tenir només permisos de lectura i actualització.

4. **Fes complir RBAC**: implementa mecanismes RBAC a l'aplicació Python. Pots utilitzar **decoradors**, **programari intermediari** o **biblioteques de control d'accés** per comprovar el rol de l'usuari i verificar-ne els permisos abans de permetre-li accedir a recursos concrets.

Amb RBAC estableixes un **sistema de control d'accés granular** que dona als usuaris el nivell d'accés adequat segons els seus rols. Això ajuda a impedir accions no autoritzades i limita els danys potencials si hi ha una bretxa de seguretat.

Per obtenir més informació sobre la implementació de RBAC amb Python, consulta la [documentació oficial de seguretat de Python](https://docs.python.org/3/library/security.html) o explora biblioteques i marcs de Python que ofereixen funcions RBAC, com ara **Flask-Security**, **Django Guardian** o **Pyramid Authorization**.

### 4. Protegeix les dades sensibles

Quan gestionis **dades sensibles** a les aplicacions Python, has d'aplicar tècniques de xifratge fortes per **protegir-ne la confidencialitat i la integritat**. Si fas servir algorismes i protocols de xifratge consolidats com **AES (estàndard de xifratge avançat, Advanced Encryption Standard)** i **TLS (seguretat de la capa de transport, Transport Layer Security)**, pots xifrar les dades tant quan estan emmagatzemades com quan es transmeten.

El **xifratge** transforma les dades en un format il·legible, anomenat text xifrat, mitjançant algorismes de xifratge i claus criptogràfiques. Només les parts autoritzades que tenen les claus de desxifratge corresponents poden desxifrar el text xifrat i accedir a les dades originals.

Aquests són alguns exemples de protecció de dades sensibles amb Python:

- **Xifratge de dades**: fes servir algorismes com AES per xifrar les dades sensibles abans de desar-les en bases de dades o altres sistemes d'emmagatzematge. Així, encara que algú hi accedeixi sense autorització, les dades continuen sent il·legibles i no es poden utilitzar.

- **Xifratge TLS**: quan transmetis dades sensibles per xarxes, per exemple durant crides a API o l'autenticació d'usuaris, utilitza **xifratge TLS** per establir connexions segures i xifrades. TLS xifra les dades intercanviades entre un client i un servidor, i evita que s'interceptin o es manipulin.

El xifratge de les dades sensibles afegeix una capa de seguretat a les aplicacions Python. Redueix considerablement el risc de bretxes de dades i d'accés no autoritzat a informació sensible.

Per saber més sobre el xifratge amb Python i com implementar-lo correctament, consulta biblioteques i documentació pertinents, com ara la biblioteca **Python Cryptography** i l'[RFC oficial de TLS](https://tools.ietf.org/html/rfc5246) per entendre el protocol TLS.

Recorda que el xifratge només és un aspecte de la protecció de dades sensibles. També és igual d'important aplicar pràctiques d'**emmagatzematge segur**, **controls d'accés** i **gestió segura de claus** per protegir les dades de manera integral.

### 5. Protegeix l'accés a les bases de dades

Si l'aplicació Python interactua amb bases de dades, segueix **pràctiques de seguretat** per protegir-te de possibles vulnerabilitats. Tingues en compte aquestes bones pràctiques:

- **Utilitza instruccions preparades**: quan executis consultes a la base de dades, fes servir **instruccions preparades** o **consultes parametritzades** per impedir **atacs d'injecció SQL**. Les instruccions preparades separen el codi SQL de les dades de l'usuari i redueixen el risc d'accés no autoritzat a la base de dades. A Python, pots utilitzar biblioteques com **SQLAlchemy** o **psycopg2** per implementar instruccions preparades i protegir-te de les vulnerabilitats d'injecció SQL.

- **Aplica el principi de privilegi mínim**: assegura't que l'**usuari de la base de dades** associat a l'aplicació Python tingui **només els privilegis necessaris** per a les seves funcions. Si segueixes el principi de **privilegi mínim**, restringeixes les capacitats de l'usuari a les que necessita i limites l'impacte potencial d'una connexió compromesa. Per exemple, si l'aplicació només necessita accés de lectura a determinades taules, dona a l'usuari de la base de dades permisos de només lectura per a aquestes taules, no accés complet a tota la base de dades.

Les instruccions preparades i el principi de privilegi mínim reforcen la seguretat de l'accés a la base de dades i redueixen els riscos dels vectors d'atac habituals. També és important seguir les últimes directrius de seguretat i bones pràctiques dels proveïdors de bases de dades i de la documentació pertinent.

Per obtenir més informació sobre l'accés segur a bases de dades amb Python, consulta la documentació de biblioteques populars: **SQLAlchemy** per treballar amb bases de dades relacionals, **psycopg2** per a PostgreSQL o la documentació específica del sistema de gestió de bases de dades que hagis triat.

Protegir l'accés a la base de dades és essencial per **protegir les dades** i mantenir la **integritat** de les aplicacions Python.

### 6. Actualitza les dependències regularment

Els projectes Python solen dependre de **biblioteques i marcs de tercers** per ampliar les funcions i simplificar el desenvolupament. Tot i això, has d'**actualitzar regularment aquestes dependències** per mantenir la seguretat i l'estabilitat del projecte.

**Si estàs atent a l'actualització de les dependències**, pots aprofitar els **pegats de seguretat** i les **correccions d'errors** que publiquen els mantenidors de les biblioteques. Així redueixes el risc de vulnerabilitats i t'assegures que el projecte utilitzi les últimes versions estables.

Per gestionar les dependències amb eficàcia, considera aquestes pràctiques:

- **Fes seguiment de les vulnerabilitats**: estigues al cas de les **vulnerabilitats notificades** a les dependències del projecte. Llocs web com [Snyk](https://snyk.io/) ofereixen bases de dades i eines que t'ajuden a identificar-les i resoldre-les. Si les supervises regularment, podràs actualitzar o substituir a temps les dependències afectades.

- **Actualitza les dependències de seguida**: quan es publiquin pegats o actualitzacions de seguretat per a les dependències, **instal·la'ls aviat**. Retardar les actualitzacions augmenta el risc d'explotació, perquè els atacants poden apuntar a vulnerabilitats conegudes de versions obsoletes.

- **Automatitza la gestió de dependències**: valora **eines** com **Pipenv** o **Conda** per automatitzar la instal·lació, el control de versions i les actualitzacions de dependències. Aquestes eines simplifiquen la gestió i ajuden a aplicar les actualitzacions de manera coherent en diferents entorns.

Mantenir les dependències actualitzades és una tasca contínua. Estableix un **calendari regular** per revisar-les i actualitzar-les, i posa la seguretat al primer lloc. Amb una actitud proactiva i vigilant, pots reduir considerablement el risc de vulnerabilitats als projectes Python.

### 7. Activa el registre i la supervisió

Per millorar la seguretat de les aplicacions Python, implementa **mecanismes complets de registre i supervisió**. El registre permet seguir esdeveniments i activitats de l'aplicació, mentre que la supervisió ofereix visibilitat en temps real del comportament del sistema i facilita la detecció i la investigació d'incidents de seguretat.

Amb el **registre**, pots capturar informació rellevant sobre l'execució de l'aplicació, com ara **errors**, **avisos** i **activitats dels usuaris**. Un registre ben configurat ajuda a detectar i depurar problemes i a **seguir esdeveniments relacionats amb la seguretat**. Per exemple, pots registrar intents d'autenticació, accessos a recursos sensibles o activitats sospitoses que indiquin una bretxa de seguretat.

La **supervisió** et permet observar el **comportament de l'aplicació en temps d'execució** i detectar **anomalies** o **patrons relacionats amb la seguretat**. Pots fer-ho amb eines i serveis que ofereixen **supervisió en temps real**, **agregació de registres** i **alertes**. Serveis com **AWS CloudWatch**, **Datadog** o **Prometheus** es poden integrar amb les aplicacions Python.

El registre i la supervisió et permeten:

- **Detectar incidents de seguretat**: les entrades del registre i les dades de supervisió ajuden a identificar incidents o activitats sospitoses perquè puguis respondre-hi ràpidament i amb eficàcia.

- **Investigar bretxes**: quan es produeix un incident, els registres i les dades de supervisió aporten informació valuosa per a la **investigació posterior a l'incident** i l'**anàlisi forense**.

- **Millorar la postura de seguretat**: l'anàlisi de registres i dades de supervisió permet conèixer l'**eficàcia de les mesures de seguretat**, detectar possibles vulnerabilitats i prendre mesures proactives per reforçar la seguretat de l'aplicació.

Configura adequadament el registre i la supervisió, equilibrant el nivell de detall amb el possible impacte en el rendiment i l'emmagatzematge. També és essencial revisar i analitzar regularment els registres i les dades de supervisió per identificar i resoldre problemes de seguretat de manera proactiva.

Les **solucions de gestió de registres** i les **eines de supervisió** t'ajuden a anticipar-te a les possibles amenaces i a protegir les aplicacions Python amb eficàcia.

### 8. Forma i capacita els desenvolupadors

Per reforçar les **bones pràctiques de seguretat amb Python**, inverteix en la **formació dels desenvolupadors Python**. Si els proporciones els coneixements i les habilitats necessaris, ajudes l'equip a escriure **codi segur** i a detectar possibles problemes de seguretat en una fase primerenca del cicle de desenvolupament.

Aquests són alguns passos per promoure la formació dels desenvolupadors:

- **Programes de conscienciació en seguretat**: organitza regularment **programes per ensenyar** als desenvolupadors les **vulnerabilitats habituals** i les pràctiques de **programació segura**. Poden incloure tallers, seminaris web o sessions de formació en línia adaptades al desenvolupament d'aplicacions Python.

- **Directrius de programació segura**: estableix **directrius específiques** per al desenvolupament amb Python, amb pràctiques i patrons de codi recomanats per reduir vulnerabilitats comunes. Poden tractar la **validació d'entrades**, l'**autenticació segura**, el **xifratge de dades** i la **gestió segura d'informació sensible**.

- **Revisions de codi i programació en parella**: fomenta la col·laboració i l'aprenentatge mitjançant les **revisions de codi** i la **programació en parella**. En revisar el codi plegats, els desenvolupadors comparteixen coneixements, detecten debilitats i proposen millores. Això ajuda a mantenir la qualitat del codi i el compliment de les pràctiques de programació segura.

- **Eines centrades en la seguretat**: integra eines de seguretat, com les d'**anàlisi estàtica de codi**, al flux de desenvolupament. Poden detectar automàticament problemes potencials, patrons de programació insegurs i vulnerabilitats a la base de codi. Per analitzar la seguretat del codi Python, pots explorar eines com **Bandit** o **Pylint**.

- **Aprenentatge continu**: anima els desenvolupadors a mantenir-se al dia de les **tendències** i **bones pràctiques** de seguretat i de les amenaces emergents a l'ecosistema Python. Poden assistir a conferències i seminaris web de seguretat o seguir fonts fiables com la comunitat **OWASP (projecte obert de seguretat d’aplicacions web, Open Web Application Security Project)**.

Invertir en la formació dels desenvolupadors crea una base sòlida per desenvolupar aplicacions Python segures. Promoure una mentalitat centrada en la seguretat ajuda a evitar incidents, reduir vulnerabilitats i garantir la seguretat general del programari.

Recorda que la **seguretat és un procés continu**. La formació permanent és necessària per seguir el ritme de les amenaces canviants i mantenir els estàndards de seguretat més alts en els projectes Python.

______

## Guia ràpida de bones pràctiques de seguretat amb Python

Aquesta guia resumeix les **bones pràctiques de seguretat amb Python** d'aquest article:

1. **Mantén l'intèrpret de Python actualitzat** a l'última versió estable per beneficiar-te dels pegats de seguretat i les correccions d'errors. Descarrega-la al [lloc web de Python - baixades](https://www.python.org/downloads/).

2. **Segueix pràctiques de programació segura**: **valida les entrades** per impedir atacs d'injecció, **evita la injecció de codi** validant i netejant el codi proporcionat pels usuaris, i **gestiona les contrasenyes de manera segura** amb algorismes de hash i mètodes d'emmagatzematge adequats.

3. **Implementa el control d'accés basat en rols (RBAC)** per impedir accessos no autoritzats. RBAC assigna rols als usuaris segons les seves responsabilitats i els concedeix els privilegis corresponents. Consulta la documentació [NIST - control d’accés basat en rols](https://csrc.nist.gov/projects/role-based-access-control) per obtenir més informació.

4. **Protegeix les dades sensibles** amb **tècniques de xifratge fortes**. Utilitza algorismes consolidats com **AES (estàndard de xifratge avançat, Advanced Encryption Standard)** i assegura't que la informació sensible s'emmagatzemi i es transmeti de manera segura. Consulta la [pàgina d'AES a la Viquipèdia](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) per obtenir-ne més informació.

5. **Protegeix l'accés a les bases de dades** amb **instruccions preparades** per impedir atacs d'injecció SQL i amb el **principi de privilegi mínim** per restringir els permisos dels usuaris de la base de dades. Aquestes pràctiques redueixen el risc d'accés no autoritzat a dades sensibles. Aprèn més sobre les **instruccions preparades** a la [documentació de SQLAlchemy](https://www.sqlalchemy.org) i sobre el **privilegi mínim** a la [guia de control d'accés d'OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html).

6. **Actualitza les dependències regularment** per corregir vulnerabilitats i aprofitar les correccions d'errors. Eines com [Snyk - plataforma de seguretat de codi obert](https://snyk.io/) poden ajudar-te a detectar vulnerabilitats a les dependències del projecte.

7. **Activa el registre i la supervisió** per detectar i investigar incidents de seguretat. El registre captura informació sobre els esdeveniments de l'aplicació, mentre que la supervisió dona visibilitat en temps real del comportament del sistema. Pots utilitzar serveis com **AWS CloudWatch**, **Datadog** o **Prometheus**.

8. **Forma els desenvolupadors** en pràctiques de programació segura i vulnerabilitats habituals. Promou programes de conscienciació, estableix directrius segures i fomenta les revisions de codi i la programació en parella. Explora eines com **Bandit** o **Pylint** per a l'anàlisi estàtica de codi.

Per consultar una guia més completa sobre la seguretat de Python, visita la [documentació oficial de Python](https://docs.python.org).

______

## Conclusió

Protegir el codi i les dades de Python davant de vulnerabilitats de seguretat hauria de ser una prioritat per a qualsevol desenvolupador o organització. Si segueixes les bones pràctiques d'aquest article, podràs reduir el risc de bretxes i garantir la integritat i la confidencialitat de les aplicacions. Estigues al dia de les amenaces, aplica pràctiques de programació segura i dona prioritat a la seguretat durant tot el cicle de desenvolupament.

Recorda que protegir les aplicacions Python és un procés continu. Actualitza el codi regularment, informa't de les amenaces emergents i millora contínuament les pràctiques de seguretat per avançar-te als possibles atacants.

______

## Referències

1. Lloc web de Python - baixades: [Enllaç](https://www.python.org/downloads/)
2. NIST - control d’accés basat en rols: [Enllaç](https://csrc.nist.gov/projects/role-based-access-control)
3. TLS - seguretat de la capa de transport (Transport Layer Security): [Enllaç](https://tools.ietf.org/html/rfc5246)
4. Snyk - plataforma de seguretat de codi obert: [Enllaç](https://snyk.io/)
5. Documentació oficial de Python: [Enllaç](https://docs.python.org)
6. OWASP - Open Web Application Security Project: [Enllaç](https://owasp.org)
7. NIST - National Institute of Standards and Technology: [Enllaç](https://www.nist.gov)
8. Bleach: [Enllaç](https://bleach.readthedocs.io)
9. html5lib: [Enllaç](https://html5lib.readthedocs.io)
10. SQLAlchemy: [Enllaç](https://www.sqlalchemy.org)
11. psycopg2: [Enllaç](https://www.psycopg.org)
12. bcrypt: [Enllaç](https://pypi.org/project/bcrypt/)
13. Argon2: [Enllaç](https://argon2-cffi.readthedocs.io)
14. AES - Advanced Encryption Standard: [Enllaç](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
15. RSA - RSA (cryptosystem): [Enllaç](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
16. Pipenv: [Enllaç](https://pipenv.pypa.io)
17. Conda: [Enllaç](https://conda.io)
