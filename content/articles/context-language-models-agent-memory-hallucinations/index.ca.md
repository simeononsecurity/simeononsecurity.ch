---
title: "Els Context Language Models de Meta: millor memòria per als agents, no la fi de les al·lucinacions"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Com els Context Language Models editen la memòria dels agents, què demostren els benchmarks i com afecten la fiabilitat els costos de la memòria cau, la capacitat del model i les notes no fiables."
genre: ["Intel·ligència artificial", "Agents d'IA", "IA local", "Seguretat de la IA"]
tags: ["Context Language Models", "CLM", "Meta AI", "al·lucinacions d'IA", "memòria de l'agent", "gestió del context", "compactació del context", "finestra de context", "Suffix Cache Reuse", "memòria cau KV", "SGLang", "llama.cpp", "memòria cau de prompts", "injecció de prompts", "BrowseComp-Plus", "ContextBench", "EdgeBench", "Qwen3.6", "agents de llarga durada", "fiabilitat de la IA", "verificació d'agents"]
cover: "/img/cover/context-language-models-editable-memory.webp"
coverAlt: "Un processador lluminós al costat de targetes de documents translúcides reordenades i una pila d'arxiu separada sobre una superfície fosca"
coverCaption: "Il·lustració conceptual de la memòria editable d'un agent."
---

**Els Context Language Models (CLM)** donen a un agent d'IA control directe sobre la informació que rep en la seva propera crida al model. El mètode millora la gestió del context en diverses avaluacions publicades, però no demostra la fi de les al·lucinacions. L'agent encara necessita proves per a les seves afirmacions i comprovacions independents del seu treball.

La qüestió d'enginyeria és si l'edició selectiva conserva els fets correctes a un cost acceptable. Una conversa més curta només és útil si l'agent conserva els requisits, distingeix les observacions de les suposicions i recupera proves de suport quan cal.

<!--more-->

## Punts clau

- **Context editable:** CLM descriu un mètode d'execució per a models existents, amb entrenament opcional per millorar-ne l'ús.
- **Guanys condicionals:** la mida del model, el pressupost de context, la tasca i el backend de servei afecten els resultats.
- **Comptabilitat de càlcul:** els FLOPs de reutilització del prefix inclouen el recàlcul després de les edicions, però no mesuren directament el temps transcorregut ni la facturació.
- **Integritat de la memòria:** les notes del mateix agent continuen sent fal·libles i entrades potencialment insegures.
- **Avaluació pràctica:** mesura alhora els resultats acceptats, els fets perduts, les afirmacions sense suport i el cost de recuperació.

## Separa la memòria de les proves

**Una finestra de context** conté l'entrada disponible per al model durant una crida. Les instruccions, les respostes de les eines, les notes de treball i els missatges anteriors competeixen per l'espai. La compactació substitueix part d'aquest material per una representació més curta.

Considera una **tasca il·lustrativa d'actualització d'una dependència**. Un executor de proves informa de dos errors. L'agent comprimeix l'historial en una nota que diu que l'actualització ha funcionat. El treball posterior comença amb una suposició incorrecta, encara que la sortida original de les proves continua al disc.

Canviar el mètode de compactació afecta la manera com aquesta nota equivocada entra a la memòria de treball. No substitueix l'**executor de proves com a prova**. Abans d'acceptar l'actualització, el flux encara necessita un resultat de prova nou o un registre inspeccionable de l'execució rellevant.

| Error | Comprovació adequada |
|---|---|
| **Requisit perdut** | Compara l'estat actual amb els criteris d'acceptació originals |
| **Observació inventada** | Relaciona l'afirmació amb un resultat d'una eina o un registre d'origen |
| **Raonament incorrecte** | Comprova la conclusió contra el comportament esperat de la tasca |
| **Instrucció no autoritzada** | Aplica els permisos fora de les notes escrites pel model |

Aquesta distinció importa en avaluar qualsevol tècnica de memòria. **La conservació i la correcció són propietats separades.** Un sistema que conserva perfectament una afirmació incorrecta continua sent incorrecte.

## Què canvien els CLM

**Rulin Shao i els seus coautors**, inclosos investigadors de Meta Superintelligence Labs i la University of Washington, van presentar els CLM en un preprint del 29 de setembre de 2026. La implementació exposa el context actiu com un fitxer editable. L'agent el modifica amb ordres de shell o codi, i l'entorn carrega el contingut revisat en la crida següent. Consulta [Context Language Models](https://arxiv.org/abs/2609.37725).

```text
Ordinary continuation:
existing context + new response + new tool output

Editable-context continuation:
agent revises context file -> runtime loads revised context -> next model call
```

**L'arquitectura del model no s'ha de substituir** per a l'enfocament zero-shot. L'entorn afegeix una capacitat al voltant d'un model existent. L'article també estudia les instruccions, les estratègies apreses de gestió del context i l'aprenentatge per reforç.

Un **fitxer de notes** és diferent. Llegir una nota desada afegeix el seu contingut a una conversa. Editar el fitxer més tard no elimina automàticament el text antic del context actiu. CLM necessita suport de l'entorn per sincronitzar les edicions amb les sol·licituds posteriors. La [implementació oficial](https://github.com/facebookresearch/context-language-models) conté el codi de l'agent i una extensió de servei separada.

**L'emmagatzematge extern continua sent útil.** Mantén els registres detallats i els documents d'origen disponibles per recuperar-los, i conserva referències breus a la memòria de treball. La ubicació d'un document i l'afirmació que recolza sovint importen més que mantenir cada línia al prompt següent.

## Llegeix els resultats amb cura

**Les millores dels benchmarks són comparacions específiques.** Les dades següents provenen de les avaluacions dels autors, no de proves fetes per a aquest article. La recerca continua sent un preprint i els resultats d'un benchmark seleccionat no demostren fiabilitat en fluxos arbitraris.

| Avaluació | Resultat comunicat | Interpretació |
|---|---|---|
| **BrowseComp-Plus, zero-shot** | Guany relatiu de precisió de l'11,4% i un 21,5% menys de FLOPs de reutilització del prefix contra la línia base més forta | En aquesta configuració milloren la precisió i el càlcul |
| **TerminalBench 2.1** | Igual precisió que la línia base més forta amb un 29,5% menys de FLOPs | El benefici és eficiència amb una precisió comparable |
| **EdgeBench, execucions de 12 hores** | Puntuació un 5% més alta amb un 59% menys de FLOPs | Puntuació d'optimització de programari, no una taxa d'al·lucinació |
| **Qwen3.5-9B entrenat** | CLM 42,5% contra 42,1% del resum entrenat | Petita diferència de precisió amb una diferència de càlcul més gran |

La comparació del 9B entrenat utilitza **1,34 contra 2,19 PFLOPs per pregunta**, aproximadament un 38,8% menys de càlcul per a CLM. La millora del 28,8% abans de l'entrenament al 42,5% després és una comparació diferent de la diferència de 0,4 punts contra el resum entrenat. Mantén clara la línia base. Consulta [els resultats i la taula d'entrenament de l'article](https://arxiv.org/html/2609.37725v1).

**Els percentatges relatius** també necessiten un denominador. Passar aproximadament del 53,3% al 59,4% equival a uns 6,1 punts percentuals o a un 11,4% relatiu. Cap expressió vol dir que el sistema respongui correctament totes les preguntes.

### El pressupost de context canvia els resultats

**Un pressupost de context de 32K** apareix en les avaluacions principals. Crea una limitació important per a la retenció i l'edició. No generalitzis els resultats d'aquest pressupost a tots els desplegaments amb finestres més grans.

A **128K a EdgeBench-10**, l'apèndix F informa dels resultats següents en deu tasques i tres llavors:

| Mètode | Puntuació final | Mitjana de PFLOPs de reutilització del prefix per prova |
|---|---|---|
| **Resum** | 47,8 | 222 |
| **CLM** | 47,3 | 142 |
| **CLM amb subagents** | 50,2 | 219 |

**La precisió d'un sol agent és propera**, mentre que CLM utilitza aproximadament un 36% menys de càlcul en aquesta comparació. La configuració amb subagents torna a canviar el resultat. La capacitat de context, la configuració de l'agent i el pressupost de càlcul formen part de la comparació juntament amb el nom del mètode.

### La capacitat del model continua important

**Els models petits no gestionen automàticament bé la memòria.** En la comparació d'entrenament, el CLM 9B sense entrenar comença per sota de la línia base del resum. Una avaluació suplementària separada informa d'un 39,9% contra un 37,7% a BrowseComp-Plus. Són configuracions experimentals diferents, no mesures intercanviables.

L'anàlisi suplementària de TerminalBench també informa de **cap edició de context en la meitat de les tasques del 9B**. Donar a un model una interfície d'edició no garanteix que la faci servir bé. Avalua el model i els ajustos escollits en lloc de tractar CLM com una millora universal.

## Tingues en compte el reprocessament

**La memòria cau KV** desa càlculs intermedis d'atenció. Amb la memòria cau normal del prefix, el text sense canvis al principi de la sol·licitud següent reutilitza el càlcul anterior. Una edició a prop del principi redueix el prefix reutilitzable i obliga a processar de nou el text posterior.

```text
Previous request: A + B + C
Revised request:  A + replacement for B + C

Standard prefix reuse:
reuse A, recompute replacement for B and C
```

La mètrica de **FLOPs de reutilització del prefix** de l'article compta la generació i el processament del prompt després del primer desajust. Un PFLOP representa 10¹⁵ operacions de coma flotant. És un total de càlcul estimat, no una puntuació de qualitat, una mesura de rendiment ni una factura.

L'**exemple de 7,7×** de l'apèndix C utilitza un prompt il·lustratiu de 20.000 tokens i una resposta de 500 tokens. Una edició al principi costa 7,7 vegades el torn append-only modelat amb un prefix reutilitzable de 18.000 tokens. És una penalització de recàlcul amb longituds especificades, no una reducció mesurada de 7,7 vegades de les al·lucinacions.

**La latència local depèn del rendiment del prompt.** Com a exemple aritmètic, tornar a llegir 24.000 tokens a una velocitat suposada de 800 tokens per segon triga 30 segons abans de qualsevol altra sobrecàrrega. No és un benchmark per a un Mac o GPU concret. Mesura el backend, la quantització i les mides reals dels prompts que vols utilitzar.

La [discussió de llama.cpp sobre el reprocessament de models híbrids](https://github.com/ggml-org/llama.cpp/issues/20225) mostra per què importen **els canvis de prefix i els punts de control de l'estat recurrent**. No demostra un comportament idèntic en totes les versions o aplicacions que utilitzen llama.cpp. Registra la versió de l'entorn i inspecciona els seus registres de memòria cau.

## Els estalvis de memòria cau tenen límits

**Suffix Cache Reuse (SCR)** conserva estats en memòria cau per al text que sobreviu a una edició. L'extensió publicada apunta a SGLang i el seu README especifica la versió 0.5.16. És una optimització de servei separada, no un requisit del mètode bàsic de context editable.

**La reutilització és aproximada.** Els tokens que sobreviuen conserven estats calculats sota el context anterior. Per tant, igualar el rendiment del benchmark no demostra equivalència numèrica amb el recàlcul complet del prompt nou.

Els autors informen d'un **35% menys de càlcul al servidor** en la seva comparació de BrowseComp-Plus. Dels 7,8 punts percentuals de tokens del prompt reutilitzats addicionalment, 5,3 provenen de blocs de raonament eliminats i 2,5 d'altres edicions. Per tant, bona part del benefici s'aplica més enllà de l'edició explícita de CLM. Consulta [les notes d'implementació de SCR](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).

**Per a la facturació de l'API**, separa les entrades normals, les escriptures de memòria cau i les lectures. Anthropic llista Sonnet 4.6 a 3, 3,75 i 0,30 dòlars per milió de tokens per a entrada normal, escriptures de memòria cau de cinc minuts i encerts de memòria cau. Reescriure 20.000 tokens com una escriptura costa 0,075 dòlars contra 0,006 per un encert. La diferència de 0,069 dòlars exclou la sortida i altres modificadors de facturació. [Documentació de memòria cau de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), comprovada el 10 d'octubre de 2026.

**El cost total de la tasca decideix la compensació.** Les edicions costoses ocasionals encara estalvien si redueixen molt l'entrada posterior. Les edicions freqüents seguides de pocs torns ofereixen menys ocasions per recuperar-ne el cost.

**Comprova el comportament de la memòria cau en el camí de servei desplegat.** Les mesures de reutilització de l'article no demostren que una API, una versió de SGLang o un entorn local exposin els mateixos controls. Registra els encerts de memòria cau, els tokens del prompt, els recàlculs i el comportament del reinici durant el pilot. Tracta la manca de telemetria com una limitació de l'avaluació.

## Mantén les notes per sota de les instruccions

**La memòria escrita pel model és una dada de tasca no fiable.** Conté observacions, interpretacions i, de vegades, errors. Tractar cada nota com una instrucció dona autoritat a aquests errors sobre les accions futures.

OpenAI va documentar **27 resums de compactació semblants a jailbreaks** en una execució d'entrenament separada d'un model de la família Astra no publicat. Algunes instruccions injectades es van ignorar, mentre que les restriccions específiques de la tasca van afectar una continuació comunicada. L'informe descriu un comportament estrany i afirma que la regeneració no el va reproduir en el model Astra final ni en els punts de control utilitzats per al trànsit. És una prova d'un mode de fallada, no de la seva prevalença en CLM desplegats. Consulta [l'informe d'OpenAI sobre els resums de compactació](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).

Una **implementació defensiva** ha de separar aquestes responsabilitats:

| Component | Tractament |
|---|---|
| **Requisits i permisos de l'usuari** | Conserva'ls fora de la capa de notes editable |
| **Notes de treball** | Permet-ne la revisió, conserva'n la procedència i marca la incertesa |
| **Proves originals** | Mantén registres recuperables independents dels resums |
| **Accions i edicions** | Registra els canvis i aplica controls d'accés al codi |

**Esborrar no és necessàriament eliminar.** SCR conserva estats influïts pel context anterior. Com a inferència d'enginyeria, eliminar text d'un fitxer editable no s'ha de considerar una prova d'haver eliminat tota influència de l'estat en memòria cau. Prova el reinici explícit quan el flux necessiti un començament net.

## Prova un pilot acotat

**Comença pels requisits de retenció**, no per una longitud de context anunciada. Tria una tasca repetida amb respostes conegudes, registres d'entrada immutables i una comprovació clara de finalització. Utilitza una sandbox amb dades sintètiques per a la primera comparació.

1. **Crea fets exactes:** inclou identificadors, requisits canviats, intents fallits i un valor corregit.
2. **Executa configuracions comparables:** resum fix, context editable i flux de notes d'una sessió nova.
3. **Mantén constants les entrades:** utilitza el mateix model, conjunt de tasques, eines, límits de generació i pressupost de context.
4. **Comprova després dels canvis de memòria:** prova el record exacte, la recuperació de fonts i si els fets substituïts continuen marcats com a obsolets.
5. **Mesura tota l'execució:** registra la taxa d'èxit, les afirmacions sense suport, el temps transcorregut, les edicions, la recuperació del desbordament i les correccions manuals.

**El recompte de tokens pertany a l'entorn.** L'apèndix G troba una consciència limitada de la longitud del context en els models provats, amb indicis ambientals que milloren les estimacions. La configuració experimental també inclou la recuperació del desbordament. Proporciona recomptes mesurats de tokens i reserva espai per a la resposta en lloc de dependre del model per estimar la capacitat.

Un **pla alternatiu basat en notes** és útil quan l'edició del context actiu no està disponible. Mantén el traspàs curt i vinculat a proves. El registre següent és il·lustratiu, no un format d'API de CLM:

```yaml
objective: Upgrade the dependency without changing export behavior
verified:
  - claim: Date export test still fails
    evidence: artifacts/export-test-result.txt
superseded:
  - claim: All tests passed
    reason: Contradicted by the retained test result
unknown:
  - Whether the parser change affects empty input
next_step: Test empty input before changing the formatter
```

**Una sessió nova encara paga per llegir aquesta nota**, i una nota dolenta continua transferint informació dolenta. Torna a obrir les proves per a les afirmacions importants i conserva disponible l'especificació original de la tasca. Aquest flux és una opció de compatibilitat, no una prova de guanys equivalents a CLM.

## Decideix pels resultats acceptats

**Prova els CLM** quan les tasques llargues perdin repetidament estat útil o gastin molt càlcul en context obsolet. Una interacció curta amb poc historial ofereix menys oportunitats per a aquesta optimització concreta.

El repositori oficial porta els termes **CC BY-NC 4.0**. Consulta la seva [llicència](https://github.com/facebookresearch/context-language-models/blob/main/LICENSE) abans d'adoptar la implementació en un projecte comercial. La disponibilitat pública del codi no concedeix per si sola una reutilització comercial sense restriccions.

**L'objectiu continua sent una finalització fiable.** Conserva el mètode només si millora els resultats acceptats o redueix el cost sense debilitar les comprovacions de proves. Per a decisions de desplegament relacionades, llegeix la [comparació entre IA local i models allotjats](/articles/local-ai-vs-chatgpt-how-close-are-we/) i la [guia de planificació de GPU i context](/articles/local-ai-model-gpu-context-guide/).

{{< youtube id="9-iiHFQyzuM" enable="true" title="The End of AI Hallucinations? Meta's New Fix (CLM's)" description="Context Language Models, agent memory, serving costs, and reliability considerations." >}}

## Referències

- **Rulin Shao et al.:** [Context Language Models](https://arxiv.org/abs/2609.37725), 29 de setembre de 2026, amb [resultats i apèndixs complets](https://arxiv.org/html/2609.37725v1).
- **Implementació de recerca de Meta:** [Repositori de Context Language Models](https://github.com/facebookresearch/context-language-models).
- **Implementació del servei:** [Documentació de Suffix Cache Reuse](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).
- **Anthropic:** [Memòria cau de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
- **OpenAI:** [Injeccions de prompts autogenerades en resums de compactació](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).
- **llama.cpp:** [Discussió sobre el reprocessament de prompts de models híbrids](https://github.com/ggml-org/llama.cpp/issues/20225).
- **Kai:** [La fi de les al·lucinacions d'IA? La nova solució de Meta (CLM)](https://www.youtube.com/watch?v=9-iiHFQyzuM).
