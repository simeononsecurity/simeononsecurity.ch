---
title: "9 projectes de skills d'agents d'IA per a recerca, disseny i desenvolupament"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara nou projectes de skills d'agents segons el flux de treball, el suport de l'amfitrió, les dependències i el cost. Aprèn a instal·lar, inspeccionar i provar les skills que necessites."
genre: ["Intel·ligència artificial", "Eines per a desenvolupadors", "Desenvolupament de programari"]
tags: ["AI agent skills", "Codex skills", "Claude Code skills", "last30days", "Impeccable", "gstack", "Superpowers", "Claude Video", "Humanizer", "NVIDIA SkillSpector", "HyperFrames", "Remotion", "SKILL.md", "fluxos de treball d'agents", "instal·lació de skills", "seguretat de skills", "recerca d'IA", "disseny frontend", "generació de vídeo", "fluxos de desenvolupament", "personalització d'agents"]
cover: "/img/cover/agent-skill-workflow-library.webp"
coverAlt: "Targetes d'instruccions d'ivori en una safata al costat d'una lupa, mostres de color i un petit rodet de pel·lícula sobre un escriptori fosc"
coverCaption: "Il·lustració conceptual d'una biblioteca de skills d'agents específica per a tasques."
---

**Instal·la una skill d'agent per millorar una tasca repetible.** Investigar discussions actuals, revisar el disseny d'una interfície i renderitzar un vídeo requereix procediments i dependències diferents. Una skill útil aporta les instruccions, el material de referència o els scripts que falten per a una d'aquestes feines.

**Nou projectes mereixen consideració:** last30days, Humanizer, Impeccable, Superpowers, gstack, Claude Video, Remotion, HyperFrames i NVIDIA SkillSpector. Alguns són paquets d'instruccions, alguns inclouen eines executables i alguns són frameworks amb skills complementàries. Aquesta guia compara els seus rols documentats i ofereix una manera pràctica de triar, instal·lar i avaluar les skills necessàries.

**Instantània de la documentació: 10 d'octubre de 2026.** Les recomanacions reflecteixen la documentació dels projectes i la inspecció del codi font, no un benchmark comparatiu de la qualitat de sortida. Una instal·lació gratuïta no demostra que la inferència, el renderitzat, l'accés a dades o l'ús comercial siguin gratuïts.

<!--more-->

## Idees clau

- **Comença amb una feina recurrent:** tria una skill amb una sortida clara i una comprovació d'acceptació.
- **Separa les skills dels runtimes:** instal·lar instruccions no instal·la tots els executables necessaris.
- **Comprova l'amfitrió:** una integració funcional amb Claude Code no demostra un comportament idèntic a Codex o Cowork.
- **Inspecciona permisos i dependències:** els comandos de paquets, els hooks, els serveis externs i les credencials requereixen una revisió separada.
- **Personalitza després de provar:** mantén la política del projecte com a autoritat i conserva un registre de les versions upstream.

## Tria segons el lliurable

| Sortida necessària | Projecte per avaluar | Primera comprovació |
|---|---|---|
| **Brief de discussions actuals** | last30days | Quines fonts han retornat proves útils? |
| **Prosa editada** | Humanizer | Han sobreviscut el significat i l'atribució? |
| **Interfície millorada** | Impeccable | Funciona la interacció revisada? |
| **Canvi planificat i provat** | Superpowers | El procés encaixa amb la complexitat de la tasca? |
| **Flux de revisió i QA** | gstack | Quines funcions funcionen al teu amfitrió d'agents? |
| **Observacions de vídeo** | Claude Video / Watch | Les afirmacions tenen suport en fotogrames o àudio? |
| **Composició de vídeo React** | Remotion skills | El vídeo exportat coincideix amb la previsualització? |
| **Composició de vídeo HTML** | HyperFrames skills | L'animació és determinista en cercar una posició? |
| **Informe d'inspecció de skill** | SkillSpector | L'anàlisi és completa i què s'ha marcat? |

**Una skill és diferent d'un agent harness.** Una skill aporta orientació específica i de vegades scripts. L'harness decideix com l'agent carrega instruccions, crida eines i aplica permisos. La nostra [comparació d'agent harnesses](/articles/best-ai-agent-harnesses/) cobreix aquests sistemes que els envolten.

**Una carpeta de skill tampoc és una instal·lació de plugin.** Els plugins de vegades registren hooks o eines addicionals que una còpia manual de carpeta no inclou. Llegeix les instruccions del teu amfitrió i del mode d'instal·lació abans d'assumir un comportament equivalent.

## Recerca i escriptura

### last30days

**Utilitza last30days per investigar discussions recents.** El [projecte](https://github.com/mvanhorn/last30days-skill) combina fonts com Reddit, Hacker News, YouTube, X i el web. La cobertura disponible depèn de les fonts seleccionades, les eines instal·lades, l'autenticació i l'accés del proveïdor. El mode preflight descriu l'accés previst i escriu els resultats sense iniciar la recerca.

**Demana un rastre de proves.** Un resultat útil inclou dates, enllaços, queixes recurrents i desacords. Una font no disponible ha d'aparèixer com una mancança de cobertura. Els recomptes d'interacció descriuen l'activitat entre les publicacions recollides, no una enquesta representativa de tots els usuaris.

**Tasca il·lustrativa:** investiga errors d'instal·lació recurrents d'una biblioteca publicada fa poc. Agrupa els informes per versió i sistema operatiu, i verifica després les solucions proposades amb el gestor d'incidències o la documentació de la biblioteca. No tractis una solució popular com una solució admesa pel projecte upstream.

### Humanizer

**Utilitza Humanizer com a passada d'edició.** La [skill](https://github.com/blader/humanizer) tracta contrastos repetitius, introduccions artificials, afirmacions inflades i altres hàbits d'escriptura. Accepta mostres de veu i pretén conservar el significat subjacent.

**Dona les restriccions juntament amb l'esborrany.** Identifica l'audiència, els fets que han de romandre i les citacions que han de continuar vinculades. Després d'editar, compara les afirmacions factuals amb l'original. Un ritme millor no valida una estadística sense suport.

| Comprovació d'escriptura | Resultat aprovat |
|---|---|
| **Significat** | Les mateixes afirmacions, qualificacions i abast |
| **Fonts** | L'atribució continua a prop dels resultats manllevats |
| **Veu** | Coincideix amb el lector previst i els exemples proporcionats |
| **Originalitat** | Afegeix raonament independent en lloc de dissimular prosa copiada |

**Utilitza aquests projectes en etapes diferents.** last30days recull material per a la investigació. Humanizer edita l'expressió. Cap dels dos substitueix la verificació de fonts o l'autoria independent.

## Treball d'interfície i desenvolupament

### Impeccable

**Utilitza Impeccable per a un treball de disseny concret.** El seu [lloc web](https://impeccable.style/) i el seu [repositori](https://github.com/pbakaus/impeccable) documenten un flux de disseny amb crítica, tipografia, maquetació, claredat, moviment i poliment. Comença amb un problema d'usuari específic en lloc de demanar una pàgina vagament més impressionant.

**Brief il·lustratiu:** fes que una pàgina de configuració de subscripció sigui més fàcil d'escanejar sense amagar la cancel·lació ni canviar la navegació amb teclat. Demana primer una crítica i implementa després els canvis escollits. Comprova al final la maquetació mòbil, l'ordre de focus, el contrast i el compliment de la tasca original.

**El mode d'instal·lació importa.** Les instruccions actuals de Codex distingeixen la skill d'un hook de disseny local del projecte. La confiança en el hook requereix la seva pròpia aprovació a Codex. Copiar una carpeta de skill no demostra que hi hagi un hook actiu.

### Superpowers

**Utilitza Superpowers per a un procés de desenvolupament estructurat.** El seu [repositori](https://github.com/obra/superpowers) empaqueta fluxos per a brainstorming, planificació, proves, depuració i revisió. També documenta la instal·lació específica de l'amfitrió, inclòs Codex.

**Adapta el procés a l'encàrrec.** Una funcionalitat que inclou emmagatzematge de dades, UI i proves es beneficia d'un pla explícit. Una correcció ortogràfica necessita molta menys cerimònia. Defineix l'abast autoritzat perquè un flux general no converteixi una petició petita en feina adjacent.

**Les instruccions del projecte continuen vigents.** El mètode de proves, l'enfocament de worktree o el patró de delegació preferit per una skill han d'encaixar amb el repositori i la petició de l'usuari. Instal·lar una metodologia no autoritza totes les accions que descriu.

### gstack

**Utilitza gstack per a un flux d'enginyeria més ampli amb eines executables.** La seva [documentació](https://github.com/garrytan/gstack) inclou skills de planificació, revisió, QA del navegador, investigació i lliurament. La instal·lació construeix eines de suport, no només copia prosa.

**El suport de Codex encara és experimental.** El projecte distingeix les funcions de seguretat imposades pels hooks de Claude Code del comportament orientatiu a Codex. No assumeixis que una comanda amb el mateix nom ofereix la mateixa aplicació entre amfitrions.

**Regla de selecció:** prova Superpowers quan falti un procés de desenvolupament repetible. Prova gstack quan les seves eines de revisió o navegador resolguin una necessitat actual. Si tots dos estan instal·lats, tria un flux principal per tasca i usa l'altre per a una contribució definida.

| Problema de desenvolupament | Tasca d'avaluació útil |
|---|---|
| **Abast poc clar** | Produeix un pla acotat amb criteris d'acceptació |
| **Implementació fràgil** | Corregeix una regressió preparada i conserva el comportament existent |
| **Interacció trencada** | Reprodueix el problema del navegador i conserva proves |
| **Fluxos en conflicte** | Confirma que només el procés escollit dirigeix la tasca |

## Evidència i producció de vídeo

### Claude Video / Watch

**Utilitza Claude Video per recollir proves d'un vídeo.** Malgrat el nom del repositori, la [skill Watch](https://github.com/bradautomates/claude-video) admet agents locals com Codex. La ruta local utilitza baixades, fotogrames mostrejats i subtítols o transcripció. Una ruta Gemini separada envia el vídeo per analitzar-lo quan està configurada.

**Comprova el suport actual de l'amfitrió.** El README indica que Claude Chat i Cowork no tenen suport. L'execució local necessita eines multimèdia com FFmpeg i yt-dlp, i els llocs web individuals també imposen límits d'accés.

**Separa les afirmacions visuals de les d'àudio.** Una transcripció dona suport a les paraules pronunciades. Els fotogrames donen suport als detalls visibles en els moments mostrejats. Cap dels dos demostra un esdeveniment no visible entre mostres. Demana marques de temps i observacions pendents en lloc d'afirmar sense matisos que has entès tota la gravació.

### Remotion

**Utilitza Remotion per a composicions de vídeo escrites en React.** El [repositori del framework](https://github.com/remotion-dev/remotion) apunta a una [col·lecció separada d'agent skills](https://www.remotion.dev/docs/ai/skills). La col·lecció cobreix la creació de projectes, markup, mapes, subtítols, Studio i renderitzat. Instal·lar la col·lecció no crea un projecte de vídeo ni instal·la totes les dependències del projecte.

**Comprova la llicència per separat de la baixada de la skill.** La [pàgina de preus de Remotion](https://www.remotion.dev/docs/license/pricing) enumera una llicència gratuïta per a particulars i empreses de fins a tres persones, amb llicència empresarial per a organitzacions més grans i col·laboracions especificades. Revisa les condicions actuals per al teu cas.

### HyperFrames

**Utilitza HyperFrames per a composicions de vídeo basades en HTML.** El seu [repositori](https://github.com/heygen-com/hyperframes) descriu el renderitzat d'HTML, CSS, mitjans i animació cercable a MP4. Les skills publicades guien la composició, la previsualització, la validació i el renderitzat.

**Comença pel conjunt bàsic documentat.** Les instruccions actuals distingeixen les skills bàsiques de la col·lecció publicada més gran i de les skills internes del repositori. Instal·lar cada carpeta sense criteri afegeix instruccions no relacionades i fa més difícil el manteniment.

| Flux de vídeo | Comprovació d'acceptació important |
|---|---|
| **Watch** | Les observacions amb marca de temps coincideixen amb els mitjans inspeccionats |
| **Remotion** | L'exportació final conserva temps, tipografies, àudio i maquetació |
| **HyperFrames** | Cercar un fotograma produeix l'estat visual previst |

**Tria mitjançant una mostra controlada.** Dona a Remotion i HyperFrames el mateix brief, actius, durada i dimensions de sortida. Per exemple, anima un procediment de manteniment de tres passos amb subtítols i un diagrama. Compara els fitxers exportats, l'esforç d'edició i els errors de renderitzat. Una sola demo atractiva no demostra un guanyador general.

## Inspecciona amb SkillSpector

```bash
skillspector scan ./downloaded-skill --no-llm --format json --output report.json
```

**NVIDIA SkillSpector és un escàner, no una skill de vídeo o escriptura.** El [projecte](https://github.com/NVIDIA/SkillSpector) documenta comprovacions estàtiques i anàlisi opcional assistida per model per a paquets de skills d'agents. La comanda anterior pressuposa que el CLI ja està instal·lat i escaneja una carpeta local sense executar la skill objectiu.

**Llegeix conjuntament els resultats i la cobertura.** Inspecciona els fitxers marcats i el codi del voltant, i registra després quines comprovacions s'han completat. Un escaneig incomplet no s'ha de convertir en un veredicte net. Un encert de paraula clau també necessita context: un token de mapa públic documentat per un proveïdor no és el mateix que codi que recull credencials no relacionades.

**Estàtic no vol dir completament fora de línia.** Segons el projecte, els noms i versions de dependències encara van a OSV per buscar vulnerabilitats amb **`--no-llm`**. En activar l'anàlisi del model, el contingut dels fitxers elegibles també s'envia al proveïdor configurat. Tria el mode adequat per al material revisat.

**Utilitza l'informe com a prova per decidir.** Explica si cada troballa és necessària per a la tasca indicada, quines dades surten de la màquina i quina autoritat concedeix el runtime. Una puntuació baixa no demostra seguretat i la reputació no resol una troballa sense explicar.

## Instal·la el paquet correcte

**Identifica primer la distribució canònica de la skill.** El framework Remotion i les seves skills viuen en repositoris diferents. Claude Video exposa una skill anomenada Watch. SkillSpector s'instal·la com a CLI, amb la integració de l'agent per separat. Aquestes distincions expliquen per què clonar un projecte no sempre és suficient.

**Les comandes següents provenen de la documentació actual d'instal·lació dels projectes.** Executa només la comanda del projecte escollit. El runner de paquets baixa i executa codi d'instal·lació, així que inspecciona el projecte upstream i tria l'abast abans d'executar-lo.

```bash
# Humanizer: user-wide Codex installation
npx skills add blader/humanizer --global --agent codex

# last30days: user-wide Codex installation
npx skills add mvanhorn/last30days-skill -g -a codex

# Remotion: official skill collection, not the framework repository
npx skills add remotion-dev/skills
```

**La tercera comanda obre el flux d'instal·lació.** Selecciona l'agent i l'abast previstos en lloc d'assumir que els valors per defecte coincideixen amb les comandes explícites anteriors. Els instal·ladors de plugins i les instal·lacions de carpetes independents també tenen mecanismes d'actualització diferents.

**Conserva les instal·lacions existents.** Abans de substituir una skill, comprova la versió, els canvis locals i el gestor. Evita conservar diverses còpies en conflicte a les ubicacions d'usuari, projecte i plugin si l'amfitrió no documenta com les resol.

| Estat d'instal·lació | Què estableix |
|---|---|
| **Fitxers presents** | Existeixen instruccions i actius referenciats |
| **L'amfitrió descobreix la skill** | L'agent reconeix el nom i la descripció |
| **Dependències preparades** | Els executables i paquets necessaris estan disponibles |
| **Tasca verificada** | Un resultat representatiu supera comprovacions independents |

**Verifica cada etapa en ordre.** Una còpia correcta de la carpeta és una comprovació d'instal·lació, no una prova que funcionin el navegador, la baixada, la transcripció o el renderitzat. Mantén la configuració opcional del proveïdor separada de la instal·lació bàsica i no desis credencials als fitxers de skill.

**Registra l'amfitrió i la revisió de cada prova.** Anota si la skill funciona amb Claude Code, Codex, Cowork o un altre amfitrió. Desa el commit upstream o la versió del paquet amb el resultat d'acceptació. Uns noms de skill semblants no demostren descobriment, hooks, permisos o accés a eines idèntics.

## Prova abans de personalitzar

**Utilitza una tasca desada com a línia base.** Executa-la sense la skill nova i després amb la skill, mantenint constants el model, l'entrada, les eines i els criteris d'acceptació quan sigui possible. Registra els errors i les correccions humanes juntament amb el resultat final.

```yaml
# Illustrative evaluation record, not a skill configuration schema
job: "review a settings page"
input: "same source revision and test data"
variants:
  - "agent without the selected skill"
  - "same agent with the selected skill"
acceptance:
  - "required actions remain visible"
  - "keyboard navigation works"
  - "mobile layout remains usable"
record:
  - "skill source and revision"
  - "model and enabled tools"
  - "completed checks and retained evidence"
  - "elapsed time and manual corrections"
  - "external service usage"
```

**Personalitza l'error repetit, no tot el paquet.** Si els resums de recerca perden proves discrepants, afegeix un requisit per conservar les fonts dissidents. Si un pas de disseny canvia colors establerts, apunta'l als tokens de disseny. Si els subtítols desborden, afegeix una comprovació de resolució d'exportació.

**Mantén traçables les addicions locals.** Registra la revisió upstream, els teus canvis i la tasca que els ha motivat. Les actualitzacions mereixen una altra prova perquè els triggers, scripts o dependències nous modifiquen el flux que havies avaluat.

**Vigila les instruccions que se solapen.** Les suites de desenvolupament, les skills de disseny i els editors de prosa expressen preferències. Les regles del repositori i la petició de l'usuari han de resoldre els conflictes. Una skill d'estil no ha d'eliminar etiquetes d'accessibilitat, citacions o termes tècnics només per variar la redacció.

## Construeix una biblioteca útil

**Comença amb la feina que repeteixes més.** Un escriptor pot provar last30days i Humanizer. Un desenvolupador frontend pot començar amb Impeccable i un flux de desenvolupament. Un productor de vídeo ha de triar un framework de producció i afegir Watch quan l'anàlisi del vídeo font formi part de la feina.

**Pressuposta l'operació per separat de la instal·lació.** Tingues en compte les crides al model, els proveïdors de cerca opcionals, la transcripció, la generació multimèdia, la infraestructura de renderitzat i les llicències aplicables. Un repositori gratuït només respon una part del cost.

**Abans de la primera prova:** prepara l'accés aprovat al model, un projecte d'un sol ús o una entrada de mostra i criteris d'acceptació escrits. Les skills d'instruccions bàsiques són accessibles per a principiants. Les eines de navegador, les dependències multimèdia i el renderitzat al núvol requereixen més preparació. Dedica una primera hora a una prova acotada i repeteix-la amb entrades representatives abans de fer habitual el flux.

**Conserva les skills amb valor demostrat.** Mantén les que redueixen passos oblidats o l'esforç de revisió, i elimina còpies duplicades que introdueixen comportaments en conflicte. Revisa la compatibilitat de l'amfitrió i les dependències quan canviï l'entorn de l'agent.

{{< youtube id="3fdb_giOrLo" enable="true" title="9 Free AI Agent Skills You NEED to Install Now" >}}

## Referències

- [last30days: skill de recerca i instal·lació](https://github.com/mvanhorn/last30days-skill)
- [Humanizer: skill d'escriptura](https://github.com/blader/humanizer)
- [Impeccable: flux de disseny](https://impeccable.style/)
- [Impeccable: repositori i configuració específica de l'amfitrió](https://github.com/pbakaus/impeccable)
- [Superpowers: skills de desenvolupament](https://github.com/obra/superpowers)
- [gstack: eines d'enginyeria i suport de l'amfitrió](https://github.com/garrytan/gstack)
- [Claude Video: skill Watch i requisits del runtime](https://github.com/bradautomates/claude-video)
- [Remotion: framework de vídeo React](https://github.com/remotion-dev/remotion)
- [Remotion: skills d'agents](https://www.remotion.dev/docs/ai/skills)
- [Remotion: llicència i preus](https://www.remotion.dev/docs/license/pricing)
- [HyperFrames: framework i distribució de skills](https://github.com/heygen-com/hyperframes)
- [NVIDIA SkillSpector: comportament de l'escàner i gestió de dades](https://github.com/NVIDIA/SkillSpector)
- [Futurepedia: 9 skills d'agents d'IA gratuïtes que necessites instal·lar](https://www.youtube.com/watch?v=3fdb_giOrLo)
