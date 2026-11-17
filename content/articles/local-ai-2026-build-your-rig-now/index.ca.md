---
title: "IA local el 2026: un model 27B supera Sonnet 4.6 mentre es tanca la finestra per comprar maquinari"
date: 2026-09-22
lastmod: 2026-11-15
toc: true
draft: false
description: "Planifica un ordinador d'IA local per al 2026 segons la mida del model, la VRAM, l'amplada de banda de memòria, el consum, el cost i les opcions d'actualització."
genre: ["IA local", "IA autoallotjada", "Models de codi obert", "Maquinari d'IA", "Aprenentatge automàtic", "Quantització", "Laboratori domèstic", "Privadesa", "Economia de la IA", "Maquinari de consum"]
tags: ["IA local", "executar llm localment", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "quantització ternària", "1,58 bits", "quantització llm", "claude sonnet 4.6", "sonnet 4.6 vs model local", "pesos oberts", "model moe", "barreja d'experts", "ollama", "llama.cpp", "rtx 5090", "vram", "inferència local", "preus gpu 2026", "escassetat de dram", "preus de la memòria", "muntar ordinador d'IA", "IA per a laboratori domèstic", "cost de subscripció d'IA", "openrouter", "artificial analysis", "guia de compra de gpu", "llm autoallotjat", "IA que preserva la privadesa", "maquinari d'IA 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Espai de treball d'alta tecnologia amb una targeta gràfica i diverses pantalles il·luminades que mostren proves i visualitzacions d'IA sobre un fons blau marí fosc."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Un model descarregable que cap en una sola targeta gràfica de consum ja supera un model d'API de primera línia en l'índex agregat d'intel·ligència.** Qwen3.8 27B és un model obert de visió i llenguatge publicat l'agost del 2026. La seva versió reempaquetada en ternari, Bonsai 2 27B, comprimeix els mateixos pesos fins a 5.53 GiB. Junts marquen el moment en què la inferència local deixa de ser una concessió per a aficionats i es converteix en una alternativa real a una API de pagament.

*La finestra per comprar maquinari es tanca de pressa. Els preus de la memòria són els pitjors de les últimes dues dècades i també encareixen les targetes gràfiques.*

Aquest article presenta els resultats de les proves, què són els dos models, on encara perd el model obert i per què els pròxims dotze mesos no són un bon moment per esperar.

**Què obtindràs:** tria un model i una capacitat de memòria segons la teva càrrega de treball. Abans de comprar, compara el cost del maquinari i de l'electricitat, la mida del context i el rendiment mesurat. La comparació de proves no prediu la qualitat per a les teves tasques ni el preu futur de la GPU.

## Resposta breu

**La diferència d'intel·ligència entre un model local 27B i una API de pagament propera als models de primera línia s'ha tancat. Els avantatges restants del model de pagament són més estrets del que suggereix la diferència de preu.**

Han canviat tres coses alhora:

- **Els models oberts 27B han assolit puntuacions properes a les líders.** Qwen3.8 27B obté 33.7 a l'Intelligence Index, davant de 30.1 per a Sonnet 4.6, amb la mateixa bateria d'avaluació.
- **La quantització ternària ha retallat la memòria necessària en aproximadament dos terços.** Bonsai 2 27B executa el model 27B complet en **5.53 GiB**, una capacitat que ofereixen targetes de pocs centenars de dòlars.
- **L'oferta de memòria ha anat a pitjor.** Els preus contractuals de la DRAM convencional van pujar **del 90 al 95 per cent** respecte del trimestre anterior a començament del 2026, el salt trimestral més gran que ha registrat TrendForce. Les GPU de nova generació s'han ajornat fins al 2028.

*Comprar o muntar l'equip ara és l'opció barata. No és un argument de venda, és el que indiquen les dades d'oferta.*

## Mira la prova amb una sola GPU

La afirmació anterior mereix una demostració, no una taula. Bijan Bowen va provar Bonsai 2 27B en un equip amb una sola GPU i es va preguntar si és el millor model disponible avui per a una targeta.

{{< youtube id="OA5cICIzD-c" enable="true" title="Primera prova de Bonsai 2 27B: és el MILLOR model d'IA per a una sola GPU?" description="Primera mirada a l'execució del model ternari Bonsai 2 27B en una GPU de consum, amb velocitat, qualitat i comparació amb les alternatives." >}}

*Fixa't en la qualitat de les respostes, no en les tokens per segon. La velocitat és el més fàcil de millorar.*

## Dos noms, un model

Els dos models que cal entendre aquí no competeixen. **Són els mateixos pesos amb dues precisions diferents.**

| | Qwen3.8 27B | Bonsai 2 27B ternari |
|---|---|---|
| **Què és** | El model original de Qwen amb pesos oberts | Reempaquetament ternari de Qwen3.8-27B fet per Prism ML |
| **Pesos al disc** | **18 GB** | **5.53 GiB** (PTQ1_0) o **6.70 GiB** (PQ2_0) |
| **Paràmetres** | 27B dens | 26.90B, la mateixa arquitectura |
| **Context** | 256K | 262,144 tokens |
| **Visió** | Sí, nativa | Sí, paquet de projector CLIP separat |
| **Crides a eines** | Sí | Sí |
| **Llicència** | Apache 2.0 | Apache 2.0 |
| **Entorn d'execució** | Ollama, llama.cpp, MLX | **Només el fork de llama.cpp de Prism ML** |

La pàgina de la biblioteca Ollama per a `qwen3.8` indica que el model 27B ocupa **18 GB** i admet context de 256K, visió i crides a eines. També hi ha una compilació MLX independent per a Apple Silicon. La versió ternària d'Ollama és una còpia dels paquets GGUF Apache-2.0 de Prism ML, republicats amb els mateixos checksums.

**Per tant, la pregunta pràctica no és quin model triar.** És quanta memòria vols gastar per a la mateixa intel·ligència. La versió ternària n'utilitza aproximadament un terç i cedeix ben poc.

{{< figure src="local-ai-architecture-comparison.webp" alt="Diagrama que compara la memòria del mateix model 27B: 18 GB en precisió estàndard i 5.53 GiB amb pesos ternaris; tots dos caben en una GPU de consum" >}}

## Comparació de les proves

Artificial Analysis avalua els dos models amb la mateixa bateria. Llegeix-ne els resultats fila per fila en lloc de resumir-los, perquè cada model guanya en àmbits diferents.

| Prova | Qwen3.8 27B | Claude Sonnet 4.6 | Líder |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Obert |
| **Coding Index** | **68.1** | 63.0 | Obert |
| **Agentic Index** | **45.8** | 31.8 | Obert |
| **GPQA Diamond** | **90.5%** | 87.5% | Obert |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Obert |
| **AA-LCR (context llarg)** | **82.0%** | 80.0% | Obert |
| **GDPval-AA** | **45.4%** | 36.0% | Obert |
| **CritPt (física de recerca)** | **5.4%** | 3.1% | Obert |
| **Taxa sense al·lucinacions** | **69.7%** | 51.6% | Obert |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **Precisió AA-Omniscience** | 15.6% | **40.9%** | Sonnet |

*El model obert lidera nou d'onze files comparables, incloent-hi tots els índexs agregats.*

### On lidera el model obert

Els tres índexs agregats expliquen el resultat principal. **Intel·ligència: 33.7 contra 30.1; programació: 68.1 contra 63.0; agents: 45.8 contra 31.8.** La diferència és més gran a l'índex d'agents. Això importa sobretot si executes fluxos de treball automatitzats de diversos passos en lloc d'enviar sol·licituds individuals.

Com a context percentil, Artificial Analysis situa Qwen3.8 27B **per sobre del 86 per cent dels models** a l'índex d'agents i del 76 per cent en programació. Sonnet 4.6 queda al 68 i al 72 per cent, respectivament. En raonament científic de nivell de postgrau, el model obert obté **90.5 per cent** a GPQA Diamond.

### On Sonnet 4.6 encara lidera

Dos resultats afavoreixen l'altre costat, i cap no és menor.

**AA-Omniscience mesura si un model contesta bé preguntes de coneixement a la primera. Sonnet 4.6 obté un 40.9 per cent, davant del 15.6 per cent.** És una diferència àmplia en fiabilitat factual i l'argument individual més fort per pagar un model de gamma alta.

La fila sense al·lucinacions s'ha de llegir amb cura. El 69.7 per cent de Qwen davant del 51.6 per cent de Sonnet sembla una victòria clara, i ho és si es mira de manera aïllada. Però la mètrica indica quina part de les respostes *incorrectes* evita inventar informació. Un model menys precís produeix més respostes incorrectes, de manera que els percentatges descriuen grups diferents i no es poden comparar directament. **Llegeix primer la fila de precisió.**

Sonnet també guanya SciCode amb un 50.1 per cent davant del 46.6 per cent, i publica resultats de dues proves que no apareixen a la fitxa del model obert: IFBench i Terminal-Bench Hard. No es poden comparar.

### Dues reserves honestes

**Les dates de publicació estan separades per sis mesos.** Sonnet 4.6 es va publicar el febrer del 2026. Qwen3.8 27B es va publicar l'agost del 2026. No és una comparació equivalent entre un model capdavanter de febrer i un model obert d'agost.

**Sonnet 4.6 ja no és el model capdavanter d'Anthropic.** Sonnet 5 i Opus 5 ara estan per damunt seu a la gamma. El model obert 27B ha atrapat un model insígnia de mitjan 2026, no el millor actual. Dir el contrari és llegir massa enllà de la taula.

*Les proves mesuren resultats en proves. L'única puntuació important és la que obté la teva pròpia càrrega de treball.*

## Què canvien els pesos ternaris

Bonsai 2 no és un model més petit. És el mateix model 26.90B amb una precisió numèrica molt inferior, i les metadades GGUF publicades mostren clarament el compromís.

| Propietat | Valor |
|---|---|
| **Arquitectura** | `qwen35`, atenció híbrida amb atenció completa cada quatre capes i capes d'espai d'estats |
| **Paràmetres** | 26.90B |
| **Blocs** | 64 |
| **Amplada de l'embedding** | 5120 |
| **Atenció** | 24 caps de consulta, 4 caps KV, longitud clau/valor 256 |
| **Context** | 262,144 tokens, base RoPE 1e7 |
| **Format dels pesos** | Ternari, grup de 128. PQ2_0 a 2.13 bits per pes, PTQ1_0 a 1.75 |
| **Torre de visió** | CLIP, 460.73M paràmetres, inclosa en un paquet de projector separat |
| **Llicència** | Apache 2.0 |

**Els pesos ternaris assignen a cada paràmetre un de tres valors en lloc de setze.** Aquesta compressió és el centre de l'explicació i fa possible que un model 27B complet ocupi 5.53 GiB en lloc de 18 GB.

### Rendiment mesurat

Mesurat amb `llama-bench` en una RTX 5090 de 32 GB, totes les capes descarregades a la GPU, flash attention activada, mitjana de tres execucions:

| Paquet | Pesos | Prefill (pp512) | Decodificació (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 completa el prefill **2.03 vegades més de pressa** que PTQ1_0, mentre que la decodificació empata estadísticament. Per això PQ2_0 és l'opció predeterminada més raonable. PTQ1_0 és útil quan importen els últims 1.2 GiB. Amb `llama-server` i context de 65K, la decodificació es va mantenir a **136.5 tok/s** en una única sol·licitud de transmissió.

**La velocitat de decodificació és la xifra que notes en l'ús diari.** 135 tokens per segon supera amb comoditat la velocitat de lectura. La latència no és el motiu per executar inferència local, perquè una API allotjada ja és prou ràpida. Els motius són el cost, la privadesa i el control.

### El parany que ningú esmenta

**L'Ollama estàndard no pot carregar aquests fitxers.** Els nuclis ternaris són al fork de llama.cpp de Prism ML. La verificació amb Ollama 0.34.2 fa fallar la càrrega amb `unsupported tensor "output.weight" size overflows`. L'entorn d'execució reconeix l'arquitectura `qwen35`, però les biblioteques no contenen `pq2_0` ni `ptq1_0`, ni un entorn d'execució per a l'activació Hadamard.

Hi ha un segon parany que convé conèixer abans de perdre-hi una tarda. **El paquet F16 d'aquesta família sembla una alternativa segura, però no ho és.** Els seus tensors són F16 i F32 normals, de manera que s'analitza i es carrega sense error, però després genera text incoherent. Els pesos són en una base girada indicada a les metadades `prism.hadamard.*`; l'entorn d'execució ha d'aplicar-hi la rotació corresponent o produirà resultats absurds. Amb 50.1 GiB, el paquet F16 tampoc no es pot descarregar del tot a una targeta de 32 GB.

*Llegeix la fitxa del model abans de baixar-lo. Un mirall comunitari no és una compilació compatible, i la pàgina ho diu clarament.*

## L'onada MoE que hi ha al darrere

Els models densos 27B són només la meitat de la història. Els models de barreja d'experts activen una petita part dels seus paràmetres per fitxa, cosa que torna a canviar els costos.

| Tipus de model | Total / actius | Context | Nota |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Germà amb pesos oberts de Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, barreja d'experts dispersa i híbrida |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Pesos oberts, pensat per a agents de programació sempre actius |

**Qwen3 Coder Next és el model que convé seguir per al treball local.** Té 80B paràmetres totals i només n'activa 3B per fitxa, i està orientat a agents sempre actius en entorns CLI i IDE. Un model que activa 3B paràmetres genera a la velocitat d'un model 3B, però aprofita la capacitat emmagatzemada de 80B. Les notes del projecte afirmen que el rendiment és comparable al de models que fan servir entre 10 i 20 vegades més càlcul actiu.

*El model dens 27B és l'opció segura avui. La corba d'eficiència encara canvia en els models dispersos.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Gràfic que mostra la diferència entre un model dens 27B que activa tots els paràmetres per fitxa i un model de barreja d'experts dispers que només n'activa 3.000 milions de 80.000 milions" >}}

## La finestra del maquinari es tanca

Aquesta part de la història té una data límit.

La inferència local es va abaratir just quan la memòria que necessita començava a encarir-se. Les dues tendències xoquen i l'efecte ja es veu als preus de venda al detall.

### Què ha passat amb els preus de la memòria

**Els preus contractuals de la DRAM convencional van pujar entre un 90 i un 95 per cent intertrimestral el primer trimestre del 2026**, l'augment trimestral més gran que ha registrat TrendForce. La memòria flash NAND va pujar entre un 55 i un 60 per cent en el mateix període.

La pressió no es va afluixar. Les dades de TrendForce indiquen un altre augment de **58 a 63 per cent** per a la DRAM i de 70 a 75 per cent per a la NAND el segon trimestre. Fins i tot la moderació del tercer trimestre, amb la DRAM amunt entre un 13 i un 18 per cent i la NAND entre un 10 i un 15 per cent, suma inflació a dos trimestres rècord en lloc de ser un alleujament.

La causa és estructural, no cíclica. Els centres de dades d'IA absorbeixen capacitat de memòria que abans servia telèfons, portàtils i consoles, i els fabricants prioritzen les comandes amb més marge. Els analistes que segueixen l'oferta de mòduls preveuen que el subministrament de xips DRAM als fabricants de mòduls caurà més d'un 70 per cent el 2027.

**El conseller delegat d'Intel va quantificar el problema.** Al AI Infrastructure Summit de Santa Clara del 15 de setembre del 2026, Lip-Bu Tan va dir que els preus de la memòria ja s'havien multiplicat «per cinc, sis i set» respecte dels nivells anteriors. Va advertir que la memòria ja representa entre el 70 i el 80 per cent de la llista de materials d'un portàtil barat. En una altra ocasió va dir que no hi haurà alleujament fins al 2028.

*El reportatge independent que compara el preu per àrea de les oblies DRAM i les oblies de lògica avançada inclou una reserva important. Els preus al comptat no són contractuals, i el mercat al comptat de DDR5 és tan reduït que la comparació és indicativa, no definitiva. La tendència general no es discuteix.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Gràfic de l'augment trimestral dels preus contractuals de DRAM durant el 2026: pujada del 90 al 95 per cent el primer trimestre i moderació al 13 al 18 per cent el tercer" >}}

### Què ha fet a les targetes gràfiques

La memòria és una part important del cost dels components d'una targeta gràfica, per tant els preus de DRAM passen directament als preus de GPU.

| Targeta | Començament del 2025 | Setembre del 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **més de $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | uns $830 | **més de $1,037** |

Els augments van arribar en onades coordinades durant el 2026, no com a pujades aïllades. Nvidia va apujar els preus al gener, una altra vegada al maig específicament per a la RTX 5090 i de nou més endavant l'any. AMD va seguir-la a l'agost amb un augment d'almenys un 10 per cent en algunes targetes Radeon i kits de memòria GDDR6, atribuït directament al cost de la memòria.

**La pròxima generació s'ha ajornat en lloc d'arribar al mercat.** Ara s'espera que la sèrie RTX 60 de Nvidia arribi el 2028, ometent tot el 2027 per manca de memòria.

*La targeta que compris avui no competeix amb una targeta més barata l'any que ve. Competeix amb una versió més cara d'ella mateixa.*

## Per què esperar surt més car

El consell habitual sobre maquinari és esperar la pròxima generació. En un mercat amb restriccions de subministrament de memòria, aquest consell et perjudica.

Tres punts ho expliquen.

**Els preus ja han pujat i continuen pujant.** Un salt del 90 al 95 per cent en els preus contractuals de DRAM en un trimestre no és un repunt que s'inverteixi el trimestre següent. TrendForce preveu que encara augmentin el tercer trimestre, no que baixin, i el conseller delegat d'Intel situa l'alleujament el 2028.

**No hi ha cap producte del 2027 per esperar.** Si les GPU de consum de pròxima generació s'ajornen al 2028, l'estratègia d'espera s'allarga dos anys. És la major part d'un cicle d'actualització de maquinari perduda sense resultat.

**Els models ja són prou bons.** Això és el que va canviar el 2026. Fa dos anys, el maquinari local oferia una experiència clarament inferior. Avui, els mateixos diners compren un model 27B a 135 tokens per segon amb un context de 262K, que supera un model d'API premium en l'índex agregat d'intel·ligència.

*Si esperaves que els models locals milloressin, ja no cal esperar. Si esperes que el maquinari s'abarateixi, les dades d'oferta indiquen que esperaràs fins al 2028.*

## Què muntar

És senzill adaptar el maquinari als models anteriors, perquè els pesos ternaris han reduït els requisits.

| Nivell | Memòria | Què executa amb comoditat |
|---|---|---|
| **Inicial** | 8 a 12 GB de VRAM | Ternari 27B de 5.53 a 6.70 GiB, amb marge per al context |
| **Pràctic** | 16 a 24 GB de VRAM | Qwen3.8 27B complet de 18 GB, o el paquet ternari amb context llarg |
| **Còmode** | 32 GB de VRAM | Ternari 27B amb tot el context 262K, o MoE 80B amb 3B d'actius |
| **Memòria unificada** | 64 a 128 GB | Models MoE dispersos més grans en Apple Silicon o un escriptori de memòria unificada |

Algunes observacions pràctiques importen més que la taula:

- **Compra memòria, no la GPU insígnia.** El paquet ternari de 5.53 GiB fa que el nivell inicial sigui realment útil. A preus del 2026, és més útil gastar la diferència en RAM i emmagatzematge que perseguir una targeta de gamma alta.
- **Els sistemes de memòria unificada són una opció de valor.** Una màquina amb almenys 64 GB de memòria compartida executa models dispersos més grans per una fracció del cost d'una targeta dedicada de la mateixa capacitat.
- **El consum i la refrigeració compten.** Un ordinador que fa inferència durant hores es comporta diferent d'un que executa proves uns minuts.
- **Executa el paquet ternari al costat d'un model més petit.** Un model 3B respon les preguntes ràpides i el 27B s'encarrega de les difícils.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Baixa Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Quan els models de gamma alta encara es justifiquen

L'argument per a la gamma alta és real, però més limitat del que suggereix el màrqueting.

**La resposta honesta és la fiabilitat factual.** La precisió AA-Omniscience de Sonnet 4.6 és del 40.9 per cent, davant del 15.6 per cent del model obert 27B. Quan una resposta incorrecta costa un client, un diagnòstic o una posició legal, una diferència de 25 punts d'exactitud importa més que qualsevol índex agregat.

**Les cadenes llargues d'agents són el segon motiu.** Sonnet 4.6 obté un 53.0 per cent a Terminal-Bench Hard i un 75.7 per cent a τ²-Bench Telecom, que mesuren l'ús sostingut d'eines i el comportament d'agents en diverses interaccions. La fitxa del model obert no dona resultats comparables, i l'absència no anima.

**El tercer motiu és operatiu.** Una API allotjada no exigeix actualitzar controladors, gestionar peculiaritats de quantització, seguir un fork de llama.cpp ni entendre una base de pesos girada. Una altra persona gestiona el temps de servei i rep l'avís a les tres de la matinada.

### La pregunta que val la pena fer

Quin lloc ocupa la gamma premium fora de les empreses?

**Encara serveix per a treballs que exigeixen coneixement fiable.** Recerca, anàlisi legal, qüestions mèdiques, modelatge financer i qualsevol tasca on una resposta errònia i segura sigui cara. És una categoria real, i la diferència de precisió és un motiu real per pagar.

**En el treball generatiu, la justificació s'esvaeix de pressa.** Redactar, resumir, refactoritzar codi, reformatar dades, classificar documents i executar fluxos automatitzats són tasques en què es verifica el resultat abans de confiar-hi. La diferència de precisió costa poc quan una persona o una bateria de proves comprova el resultat. En aquestes càrregues, és difícil defensar pagar per token un índex de 30.1 quan un índex de 33.7 s'executa sense cost addicional en el maquinari que ja tens.

**La decisió ha passat de la capacitat a les conseqüències.** Fa dos anys es preguntava si un model local podia fer la feina. Avui es pregunta quant costa un error i com detectar-lo.

*El suplement empresarial compra fiabilitat, compliment normatiu i el torn de guàrdia d'una altra persona. La resta paga una diferència que deixa d'importar quan s'executa una bateria de proves.*

## Conclusions clau

- **Un model local 27B ara supera Claude Sonnet 4.6 a l'índex agregat d'intel·ligència**, 33.7 contra 30.1, i lidera en programació, tasques d'agents, context llarg i raonament científic de postgrau.
- **Sonnet 4.6 encara guanya en precisió factual**, 40.9 contra 15.6 per cent a AA-Omniscience, l'argument més fort que queda per a la gamma alta.
- **La quantització ternària fa que això sigui pràctic.** Bonsai 2 27B executa el mateix model 26.90B en 5.53 GiB en lloc de 18 GB, i tots dos tenen llicència Apache 2.0.
- **L'Ollama estàndard no pot executar els paquets ternaris.** Necessiten el fork de llama.cpp de Prism ML, i l'alternativa F16 genera silenciosament resultats incoherents en lloc de fallar.
- **La velocitat mesurada de decodificació és de 135 tokens per segon** en una RTX 5090, molt superior a la velocitat de lectura.
- **Els preus de la memòria són el motiu per actuar ara.** Els contractes de DRAM van pujar entre un 90 i un 95 per cent en un trimestre del 2026 i les GPU de consum de nova generació s'han ajornat al 2028.
- **La RTX 5090 ha passat de $1,999 a més de $5,000** en menys de dos anys, i la resta de nivells també s'han encarit.

## Passos següents

1. **Baixa el model i prova'l amb la teva càrrega de treball**: **[Ternary Bonsai 2 27B a Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. **Obtén els pesos originals** a precisió completa si tens prou memòria: **[Qwen3.8 a Ollama](https://ollama.com/library/qwen3.8)**
3. **Prova el model abans de construir res** amb el punt final gratuït allotjat: **[Qwen3.8 27B gratis a OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Compara'l amb l'opció de pagament amb els mateixos prompts**: **[Claude Sonnet 4.6 a OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Dimensiona l'equip per al nivell que necessites** amb la taula de memòria i compra la memòria abans que la targeta gràfica.
6. **Si tens una Raspberry Pi sense ús**, comprova si pot executar alguna cosa més petita: **[Quins models d'IA funcionen en una Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Articles relacionats

| Article | Què explica |
|---|---|
| **[Quins models d'IA funcionen en una Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)** | El límit inferior de la inferència local i què poden executar de debò les plaques petites |
| **[Com crear un assistent d'IA que preserva la privadesa per a Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un assistent local en maquinari fora de la xarxa, on la privadesa no és opcional |
| **[El paper de la memòria ECC per reduir la corrupció de dades](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | Per què la qualitat de memòria importa més quan hi viu un model gran |
| **[Què és un laboratori domèstic i n'hauries de tenir un?](/articles/what-is-a-homelab-and-should-you-have-one/)** | Com planificar l'espai, l'energia i la refrigeració per a equips que s'escalfen |

## Referències

1. [Ternary Bonsai 2 27B - mirall del model d'Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - biblioteca de models d'Ollama](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (gratuït) - proves i preus d'OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - proves i preus d'OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Primera prova de Bonsai 2 27B: és el millor model d'IA per a una sola GPU? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - avaluacions independents de models](https://artificialanalysis.ai/)
7. [TrendForce - previsions de preus contractuals de DRAM i NAND](https://www.trendforce.com/)
8. [Els xips de memòria ja són més cars que els de càlcul per àrea - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [L'alleujament per a les GPU s'ajorna al 2028 després d'una pujada rècord del 95% de la DRAM - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Tan d'Intel: la memòria s'ha multiplicat per 7, sense alleujament fins al 2028 - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Fork de llama.cpp de Prism ML - nuclis ternaris](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - pesos originals](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
