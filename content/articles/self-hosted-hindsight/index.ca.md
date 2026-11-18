---
title: "Hindsight autohostat: memòria local d’agents i encaminament privat de models"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Un estudi de cas de Hindsight autohostat, les rutes locals de Qwen observades i el treball de GPU per petició sense subscripció a models allotjats en les rutes inspeccionades."
genre: ["IA local", "IA autohostada", "Agents d’IA", "Infraestructura d’IA", "Privadesa"]
tags: ["Hindsight", "Hindsight autohostat", "memòria d’agents", "IA local", "LLM local", "Qwen3.5", "LiteLLM", "VPN privada", "passarel·la de models", "incrustacions", "rerànquing", "planificació de GPU", "inferència privada", "Docker", "bancs de memòria", "pàgines de coneixement", "encaminament de models locals"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Un servei de memòria privada encamina les tasques a servidors locals de models amb CPU i GPU"
coverCaption: "La memòria, la recuperació i les rutes de models inspeccionades s’executen en equips propis"
---

**El nostre servei de memòria Hindsight s’executa en maquinari que controlem.** El motor de memòria, la base de dades, el model d’incrustacions i el rerànquer s’executen en un únic desplegament autohostat. Hindsight envia les peticions de generació a una passarel·la privada. El backend Qwen compartit que vam inspeccionar i la ruta de refresc de pàgines provada utilitzen servidors locals de models, sense subscripció d’inferència allotjada.

Això descriu un desplegament funcional. **Autohostat no vol dir que funcioni sense connexió.** La VPN utilitza un servei extern de coordinació, i les imatges de programari i els pesos dels models s’han de descarregar. La afirmació es limita al processament de memòria i a la inferència del model, no a totes les connexions de xarxa dels nostres dispositius ni de les altres eines d’agents.

<!--more-->

## Punts clau

- **Hindsight gestiona el flux de memòria.** Un contenidor Docker serveix l’API, els treballadors i el pla de control; un volum persistent conserva les dades dels bancs.
- **Els models petits de recuperació es mantenen locals.** Les incrustacions i el rerànquer s’executen dins del procés Hindsight a la CPU.
- **Qwen genera text.** Retain, Reflect i Consolidation demanen l’àlies privat Qwen3.5-4B amb el raonament desactivat i una sortida limitada. El backend inspeccionat serveix el model localment.
- **El refresc lent de pàgines rep una GPU.** Un àlies de model separat lloga una targeta per a una petició en segon pla i l’allibera quan acaba.
- **La passarel·la amaga on s’executa físicament el model.** Hindsight tria un àlies de model. Els serveis d’encaminament privats trien el punt de servei.

## Delimita l’abast abans de triar models

**Hindsight és el motor de memòria, no el servidor de models.** La imatge Docker completa inclou models locals d’incrustació i rerànquing, però la generació lingüística necessita un endpoint. La [guia d’instal·lació de Hindsight](https://hindsight.vectorize.io/developer/installation) explica aquesta separació i mostra servidors locals llama.cpp, Ollama i vLLM com a alternatives als proveïdors allotjats.

**L’API de memòria es manté a la xarxa privada.** El pla de control web funciona en una interfície local. Un volum persistent conserva la base de dades incrustada, de manera que recrear el contenidor no elimina els bancs. L’autenticació protegeix l’API i els bancs separats organitzen el context dels projectes.

**La passarel·la de generació ofereix noms de models estables.** Hindsight envia peticions compatibles amb OpenAI a través de la passarel·la privada i la VPN. La passarel·la les reenvia a endpoints locals. La ruta Qwen inspeccionada arriba a un desplegament LiteLLM associat a un servidor local amb CPU. La [documentació de l’encaminador LiteLLM](https://docs.litellm.ai/docs/routing) descriu aquest patró d’àlies. Un altre encaminador compatible amb OpenAI pot fer la mateixa funció.

{{< figure src="hindsight-private-request-path.webp" alt="Diagrama amb agents, un servei Hindsight privat, models locals de recuperació, una passarel·la privada i servidors Qwen locals" caption="El diagrama omet noms d’amfitrió, adreces, claus d’accés i etiquetes dels equips físics" >}}

[Obre el diagrama complet del recorregut de la petició](hindsight-private-request-path.webp).

**També hi ha una API interna.** Hindsight crida una passarel·la privada amb el format compatible amb OpenAI. Les rutes inspeccionades serveixen la inferència localment. No vam auditar totes les regles de reserva de la passarel·la. Revisa’n la política abans de tractar el processament local com una garantia per a totes les peticions.

## Assigna cada tasca de memòria al recurs adequat

Les operacions de Hindsight fan feines diferents. **Retain** extreu fets de material nou. **Recall** troba records rellevants. **Reflect** cerca i redacta una resposta sintetitzada. **Consolidation** combina fets relacionats. El **refresc de pàgines de coneixement** reconstrueix un resum viu del banc.

| Operació | Ubicació del model | Motiu |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B mitjançant la passarel·la privada | Extracció estructurada local amb un pressupost de sortida limitat |
| **Recall** | Incrustació i rerànquing locals a la CPU | La cerca no necessita una crida a l’API de generació |
| **Reflect** | Qwen3.5-4B mitjançant la passarel·la privada | La síntesi necessita generació després de recuperar memòries |
| **Consolidation** | Qwen3.5-4B mitjançant la passarel·la privada | Els lots petits limiten les respostes estructurades llargues |
| **Refresc de pàgina de coneixement** | Ruta Qwen local dedicada a GPU | La síntesi de fons gran superava el límit de temps de la ruta CPU |

*Deixa les tasques petites de recuperació a la CPU i reserva la inferència GPU per a feines llargues que hagis mesurat.*

El contenidor Hindsight carrega **BAAI/bge-small-en-v1.5** per a les incrustacions i **hindsight-ai/hs-rerank-1** per al rerànquing. Els registres d’inici confirmen que tots dos s’executen localment a la CPU. La [referència de models Hindsight](https://hindsight.vectorize.io/developer/models) documenta les opcions locals i la ruta opcional del model de decisió.

Vam conservar el model d’incrustacions existent perquè canviar l’espai d’incrustacions exigeix reconstruir els vectors desats. El rerànquer ja s’executa localment, així que un servei de rerànquing allotjat afegiria un límit de dades sense resoldre el temps d’espera de generació observat. Una prova local de **hs-decide-1-flash** va produir una resposta Reflect correcta, però va acabar a prop del límit de temps de la prova. Les dades sintètiques de Consolidation no van exercitar la ruta de decisió. Per això el model de decisió no forma part de l’encaminament de producció.

## Assigna una GPU a la feina lenta de fons

**El nom del model habitual i el nom del model de refresc són diferents.** Retain, Reflect i Consolidation utilitzen l’àlies Qwen compartit. El refresc de pàgines en segon pla utilitza un àlies GPU específic del node amb una sola crida de model de llenguatge concurrent. Això limita una feina de manteniment llarga a una GPU cada vegada.

**Una reserva per petició limita l’ús de GPU.** El conjunt de GPU inicia un treballador de model quan arriba una petició. El controlador reserva una targeta, serveix la petició, atura el treballador i allibera la reserva. El diagrama omet l’inventari físic dels amfitrions.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagrama que mostra una GPU reservada per refrescar una pàgina en segon pla i alliberada quan acaba la petició" caption="Un lloguer per petició reserva una GPU per refrescar una pàgina" >}}

[Obre el diagrama complet del cicle de lloguer de GPU](hindsight-gpu-lease-cycle.webp).

Aquesta separació va sorgir d’una fallada mesurada. **Un refresc de pàgina primer a CPU va arribar al límit d’una hora.** Després d’encaminar els refrescos de fons al conjunt local de GPU, cinc pàgines que havien fallat abans es van completar en uns dos a sis minuts en una recuperació. Aquestes xifres descriuen aquelles pàgines i configuracions. No són una prova general de rendiment de Qwen.

## Corregeix els valors predeterminats i els temps d’espera

**Els antics límits de sortida de Hindsight no s’ajustaven al nostre encaminador local.** L’encaminador accepta fins a 8.192 tokens de sortida i n’aplica 256 quan la petició no especifica cap límit. Un límit Retain anterior de 64.000 tokens va provocar HTTP 400. Els lots de vuit fets de Consolidation es van aturar per longitud de sortida, i Reflect necessitava un límit explícit per evitar el valor predeterminat de 256 de l’encaminador.

**Vam fer explícits els límits per a cada feina.** El raonament Qwen està desactivat per a aquestes operacions de memòria. Hindsight ara permet quatre crides LLM concurrents en total, amb un màxim d’una crida concurrent per al refresc de pàgines en segon pla. El temps d’espera global LLM és de 1.800 segons amb un únic reintent del model.

| Càrrega | Límit de sortida o lot | Límits de crida i operació |
| --- | --- | --- |
| **Retain** | 8.192 tokens de sortida | Temps d’espera general de 1.800 segons |
| **Reflect** | 4.096 tokens de sortida | 900 segons per crida, 3.600 segons per operació |
| **Consolidation** | 4.096 tokens, quatre fets per crida | 900 segons per crida, 14.400 segons per operació |
| **Refresc de pàgina** | Una crida de model concurrent | 900 segons per crida, ruta GPU dedicada |

*Aquests valors descriuen el nostre desplegament de novembre de 2026 i l’encaminador local.*

**El temps d’espera d’una crida i el límit total d’una operació controlen fases diferents.** Algunes crides Qwen vàlides superaven l’antic límit de 300 segons per crida. Els límits més llargs de l’operació permeten treball amb diverses crides, mentre que els 900 segons per crida continuen limitant cada intent.

En la recuperació, diverses tasques Retain van acabar amb **1.042 a 2.076 tokens de sortida**. Dues execucions de Consolidation van completar **41 de 41** i **30 de 30** elements. Més tard, un refresc de pàgina va esgotar el límit de temps i va motivar la ruta GPU separada descrita abans. Aquests resultats no demostren fiabilitat a llarg termini.

## Què sacrifica aquest disseny

**No pagar per un model allotjat no vol dir que el cost sigui zero.** El desplegament utilitza maquinari propi, electricitat, emmagatzematge, temps de manteniment i temps de GPU durant els refrescos. Cada ubicació intercanvia capacitat per latència o simplicitat operativa.

| Opció | Avantatge | Compromís |
| --- | --- | --- |
| **Generació primer a CPU** | Manté disponible la GPU | Un refresc de pàgina provat va arribar al límit d’una hora |
| **Refresc de pàgina amb GPU** | Cinc pàgines van acabar en uns dos a sis minuts en una execució | Utilitza GPU i depèn de la ruta dedicada |
| **Base de dades incrustada** | Manté compacte el desplegament | Redueix l’abast de fallada i exigeix provar les còpies de seguretat |

*Utilitza una ruta GPU de refresc quan la latència CPU mesurada superi la finestra de manteniment.*

La [guia d’instal·lació de Hindsight](https://hindsight.vectorize.io/developer/installation) recomana PostgreSQL separat per a desplegaments de producció més grans. **La nostra base incrustada necessita una ruta de còpia de seguretat i recuperació provada** a mesura que creix el banc.

**La inferència privada és una propietat de la ruta.** Revisa el proveïdor Hindsight seleccionat, el mapa de models de la passarel·la, les regles de reserva, el procés local del model, la retenció de registres i el trànsit de sortida. Els identificadors de seguiment de Hindsight ajuden a correlacionar peticions, i Docker rota els registres del contenidor. Cap d’aquestes mesures demostra que una petició posterior s’hagi mantingut local. Una auditoria de la passarel·la aporta la prova integral que falta.

## Recomanació

**Comença amb models locals de recuperació i límits explícits de generació.** Col·loca Hindsight, els models d’incrustació i el rerànquer en equips propis. Encamin­a la generació a través d’una passarel·la privada compatible amb OpenAI per una VPN. Mesura cada operació abans d’assignar CPU o GPU, i reserva la ruta GPU per a feines de fons la latència CPU de les quals superi la finestra de manteniment.

*Revisa cada ruta de reserva de la passarel·la i prova la recuperació del banc abans de considerar privat i resilient el desplegament.* La [guia del límit de privadesa de la IA local](/articles/local-ai-privacy-boundary/) ofereix una llista inicial.

## Conclusió

**Aquest desplegament manté la memòria Hindsight i les rutes d’inferència inspeccionades en equips propis, sense subscripció a models allotjats.** La recuperació CPU, les crides Qwen limitades i la ruta GPU de refresc amb una crida resolen càrregues diferents. Les recuperacions van completar Retain, Consolidation i el refresc de pàgines amb aquests valors. Les comprovacions següents són auditar totes les reserves de la passarel·la, provar les còpies de seguretat i observar la fiabilitat durant més temps.
