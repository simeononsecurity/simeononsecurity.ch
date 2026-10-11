---
title: "IA local contra ChatGPT: fins a quin punt ens hi acostem?"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara la IA local amb ChatGPT i Claude amb puntuacions de referència, estimacions de memòria, velocitat de servei i verificació d'agents. Inclou escenaris amb RTX 5090, DGX Spark i Mac Studio."
genre: ["IA local", "Intel·ligència artificial", "Maquinari d'IA", "Eines per a desenvolupadors"]
tags: ["IA local contra ChatGPT", "IA local contra Claude", "LLM local", "agents d'IA", "pesos oberts", "Qwen3.8 27B", "GLM-5.3", "GPT-6 Astra", "Claude Opus 5.5", "RTX 5090", "DGX Spark", "Mac Studio", "quantització", "cau KV", "memòria unificada", "VRAM", "Artificial Analysis", "verificació d'agents", "inferència local", "IA híbrida", "agents de codi", "benchmarks d'IA"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Una estació de treball connectada per un camí lluminós amb un núvol abstracte de punts de xarxa sobre un fons fosc"
coverCaption: "Il·lustració conceptual de la IA local i allotjada."
---

La **IA local** és una opció pràctica per a tasques delimitades amb comprovacions clares. Per substituir el treball que dones a ChatGPT o Claude, han d'encaixar la capacitat del model, la memòria disponible i un agent capaç d'inspeccionar i verificar el resultat.

Un model que cap a la teva estació de treball encara necessita eines adequades i prou velocitat per repetir intents. Aquest article separa resultats de benchmarks, estimacions de memòria i proves de tasques completades.

<!--more-->

## Idees principals

- **Capacitat:** les puntuacions de referència descriuen configuracions concretes, no la teva compilació local quantitzada.
- **Memòria:** reserva espai per als pesos, la cau de context i la sobrecàrrega d'execució.
- **Velocitat:** repetir una conversa d'agent mesura el servei, no la correcció.
- **Verificació:** un agent necessita comprovacions adaptades al resultat demanat.
- **Selecció:** compara tasques repetides, temps de reparació i cost total abans de comprar maquinari.

## Llegeix les puntuacions en context

L'**Artificial Analysis Intelligence Index** agrupa diverses avaluacions en una puntuació de referència. El [rànquing de models](https://artificialanalysis.ai/leaderboards/models) i els resultats de maquinari local mostren aquestes entrades comprovades el 6 d'octubre de 2026.

| Model i configuració | Puntuació de l'índex | Desplegament en aquesta comparació |
|---|---|---|
| **Qwen3.8 27B, xhigh** | 34 | Pesos descarregables |
| **GLM-5.3, max** | 45 | Pesos descarregables |
| **GPT-6 Astra, max** | 53 | Servei allotjat |
| **Claude Opus 5.5, max amb fallback** | 58 | Servei allotjat |

Els **punts de l'índex** no són percentatges d'intel·ligència ni d'èxit. Una diferència de 13 punts entre GLM i Claude no demostra una diferència del 13 % en els teus resultats de codi. La configuració de raonament també importa.

La [metodologia d'avaluació publicada](https://artificialanalysis.ai/methodology/intelligence-benchmarking) descriu la prova. Algunes avaluacions inclouen eines i infraestructura d'agents. No traslladis directament la puntuació a una còpia local comprimida que funciona amb una altra aplicació.

**ChatGPT i Claude són productes**, mentre que aquesta taula compara models subjacents. La subscripció, el model, les eines i el context de la tasca creen diferències addicionals. Prova primer una tasca repetida amb la configuració completa.

## Pressuposta tota la sol·licitud

L'**ajust de memòria** té tres parts. Els pesos emmagatzemen paràmetres apresos. La memòria cau de claus i valors, o **cau KV**, conserva dades d'atenció durant la inferència. Els buffers d'execució consumeixen l'espai restant.

```text
Memòria necessària = pesos residents + cau de context + reserva d'execució
Memòria disponible = capacitat física - reserva del sistema operatiu i les aplicacions
```

La **quantització** redueix la precisió d'emmagatzematge dels pesos. Una precisió menor redueix la memòria, però la qualitat depèn del model i de la compilació. La precisió de la cau és independent. Un fitxer Q4 no demostra una cau de quatre bits.

Per a 27.000 milions de paràmetres, 16 bits requereixen uns 50,3 GiB, 8 bits uns 25,1 GiB i 4 bits uns 12,6 GiB. Les **mides publicades dels fitxers** també reflecteixen metadades, empaquetament i precisió mixta. Planifica amb els fitxers exactes.

La [fitxa de Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) i la [fitxa de GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) descriuen arquitectures diferents. Un **model de barreja d'experts** activa només part dels paràmetres per token, però els pesos restants encara requereixen emmagatzematge. L'offload canvia la ubicació i la latència, no elimina els pesos.

## Comença pels fitxers publicats

La **mida de descàrrega** és un punt de partida més concret que el nombre de paràmetres. Les compilacions publicades de Qwen i GLM d'Unsloth mostren l'efecte de la quantització.

| Compilació quantitzada | Mida publicada, GB decimals | GiB aproximats |
|---|---|---|
| **Qwen3.8 27B Q4_0** | 16.1 | 15.0 |
| **Qwen3.8 27B Q8_0** | 29.0 | 27.0 |
| **GLM-5.3 UD-Q4_K_XL** | 467 | 434.9 |
| **GLM-5.3 UD-IQ2_M** | 239 | 222.6 |

**Fonts dels fitxers:** [Qwen Q4_0](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-Q4_0.gguf), [Qwen Q8_0](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-Q8_0.gguf), [fragments GLM UD-Q4_K_XL](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main/UD-Q4_K_XL) i [fragments GLM UD-IQ2_M](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main/UD-IQ2_M). Són llistats arrodonits comprovats el 6 d'octubre de 2026. Les conversions a GiB divideixen els bytes decimals per 2³⁰.

Aquestes són **mides dels fitxers de pesos**, no mesures de memòria resident total. La càrrega, les cau, els buffers temporals i altres components afecten el procés. No comparis 29 GB amb una assignació de 30 GiB sense convertir les unitats.

## El context canvia l'ajust

La **cau d'atenció de Qwen** ofereix un exemple calculat. La seva [configuració publicada](https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/config.json) especifica 64 capes, atenció completa en una de cada quatre capes, quatre caps de clau-valor i una dimensió de cap de 256.

```text
Bytes KV per token amb atenció completa:
16 capes × 4 caps KV × 256 dimensions × 2 (K i V) × 2 bytes
= 65.536 bytes

8.192 tokens  = 0,5 GiB
32.768 tokens = 2,0 GiB
```

Aquest **component de cau calculat** suposa claus i valors de 16 bits per a una seqüència. Exclou l'estat d'atenció lineal, els buffers d'execució, la sobrecàrrega de l'assignador i els components opcionals de visió o descodificació especulativa. També necessiten reserva.

Per a un **pressupost de planificació il·lustratiu**, afegeix 3–5 GiB per a les assignacions restants a les mides de pesos arrodonides. Substitueix la hipòtesi per mesures del teu entorn.

| Compilació i context | Rang calculat de planificació |
|---|---|
| **Qwen Q4_0, 8K** | 18.5–20.5 GiB |
| **Qwen Q8_0, 8K** | 30.5–32.5 GiB |
| **Qwen Q8_0, 32K** | 32.0–34.0 GiB |

Una **assignació utilitzable de 30 GiB** deixa marge per a l'exemple Q4, mentre que els escenaris Q8 la superen amb aquestes hipòtesis. Un prompt curt que funciona no prova capacitat per a una sessió de codi llarga.

Les **sol·licituds simultànies** afegeixen una dimensió. Ollama documenta el creixement de memòria de context amb sol·licituds paral·leles i controls separats de precisió de cau. La cau Q8 usa aproximadament la meitat de memòria F16 i Q4 aproximadament una quarta part, amb compromisos de qualitat segons el model. Consulta les [preguntes freqüents d'Ollama](https://docs.ollama.com/faq).

## Ajusta el maquinari a l'assignació

Una **RTX 5090** ofereix 32 GB de memòria gràfica dedicada. Un DGX Spark amb 128 GB usa memòria compartida. Artificial Analysis documenta les dues configuracions. Més capacitat permet assignacions grans, però no prova la velocitat de servei.

| Escenari de maquinari | Conseqüència pràctica |
|---|---|
| **RTX 5090, 32 GB** | Qwen Q4 deixa més marge de context que Q8 |
| **DGX Spark, 128 GB** | Espai per a qualsevol compilació de Qwen, amb sobrecàrrega d'execució |
| **Mac Studio, 256 GB** | Els pesos grans són candidats, subjectes als límits d'execució i assignació |

**GLM UD-Q4_K_XL** supera les tres capacitats abans d'afegir una cau. El conjunt de pesos IQ2 d'uns 222,6 GiB també supera un sistema de 128 GB. En un Mac de 256 GB, la viabilitat depèn de l'assignació accessible per a la GPU i de la reserva restant. Les [especificacions d'Apple](https://www.apple.com/mac-studio/specs/) descriuen opcions de maquinari, no una assignació d'inferència garantida.

Un **pressupost hipotètic de 240 GiB utilitzables** deixa uns 17,4 GiB després dels pesos IQ2. Amb 192 GiB, els pesos sols ja fallen. Cap xifra prova reserva del sistema, cau comprimida, rendiment útil ni qualitat IQ2 acceptable. Exigeix una configuració d'execució demostrada abans de comprar.

## La velocitat és un resultat separat

El **benchmark d'inferència local d'Artificial Analysis** repeteix una càrrega registrada de 168 torns de model. Els seus [resultats de portàtils i estacions de treball](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations/) mostren aquests temps per a les configuracions Qwen3.8 27B provades.

| Sistema | Temps de reproducció del servei |
|---|---|
| **DGX Spark, 128 GB** | 24,2 minuts |
| **RTX 5090** | 4,9 minuts |
| **Mac Studio, 256 GB** | Sense resultat en aquesta comparació |

El resultat RTX tarda aproximadament una cinquena part del temps de Spark. **Les configuracions de servei importen**, per tant no és una proporció universal. Les compilacions provades també difereixen dels exemples GGUF.

El **temps de reproducció** exclou l'execució d'eines i força longituds de resposta enregistrades. No avalua si les respostes resolen la tasca original. Una mesura de MacBook tampoc prova el rendiment del Mac Studio.

## Dona feedback a l'agent

Un **sistema d'execució d'agents** proporciona eines, context, un bucle d'acció i verificació. Un model escriu o tria accions dins d'aquest sistema. Per exportar un CSV, cal llegir fitxers, canviar codi, executar proves i rebre els errors.

Considera una **tasca d'exportació il·lustrativa**, no un experiment mesurat. L'agent crea una descàrrega amb un format de data incorrecte. Una revisió visual no ho detecta. Una prova obre el fitxer i compara les dates amb el format requerit. L'agent rep el fallada, canvia el formatador i repeteix la prova.

| Component absent | Fallada probable |
|---|---|
| **Context rellevant** | Edita un fitxer no relacionat |
| **Eines d'execució** | Descriu una solució sense aplicar-la |
| **Pas de verificació** | S'atura després de codi plausible |
| **Feedback d'errors** | Repeteix un enfocament fallit |

**LangChain informa** d'un canvi del 52,8 % al 66,5 % a Terminal Bench 2.0 mantenint GPT-5.2-Codex fix. El seu [informe d'enginyeria d'agents](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) descriu orientació de verificació, context d'entorn, detecció d'edicions repetides i canvis del pressupost de raonament.

Aquesta és **evidència informada pel proveïdor**, no una prova que un model local petit iguali un model de frontera. La conclusió limitada és que la selecció del model sola no explica els resultats de l'agent. LangChain també informa de pitjors resultats amb raonament màxim permanent per temps d'espera.

## Ajusta les comprovacions al treball

Una **comprovació aprovada** només demostra el que cobreix. Una prova CSV de noms de columnes deixa sense provar dates, cometes, Unicode i control d'accés. Defineix el resultat demanat abans de decidir com verificar-lo.

| Tasca | Evidència útil de finalització |
|---|---|
| **Canvi de codi** | Proves rellevants i inspecció del comportament resultant |
| **Resposta de recerca** | Fonts que donen suport a cada afirmació |
| **Reserva o reemborsament** | Estat correcte i política aplicable |
| **Exportació de document** | Sortida analitzada amb els camps i formats sol·licitats |

L'**estudi τ-bench** avalua agents que interactuen amb eines, usuaris i regles de domini. El seu [article de recerca](https://arxiv.org/abs/2406.12045) compara l'estat final de la base de dades amb el resultat esperat. Un text de confirmació fluid no basta per a una transacció.

## Local no vol dir fora de línia

La **inferència local** controla on funciona el model. L'aplicació encara determina on viatgen documents, cerques, traces i resultats d'eines. Un model de codi local connectat a cerca remota o eines del núvol és un sistema connectat.

Ollama afirma que no rep prompts ni respostes en execució local i documenta com desactivar les funcions del núvol. És una **afirmació específica de l'entorn d'execució**, no una garantia de privadesa per a tot agent connectat. Verifica l'endpoint i cada integració a la [documentació d'execució](https://docs.ollama.com/faq).

| Ruta de dades | Què cal comprovar |
|---|---|
| **Endpoint d'inferència** | Procés local, servidor remot o fallback automàtic |
| **Cerca i recuperació** | Consultes i fragments enviats externament |
| **Connexions d'eines** | Fitxers i registres exposats a cada servei |
| **Registres i traces** | Ubicació, contingut retingut i accés |

Un **flux híbrid** necessita una regla explícita de traspàs. Mantén local l'extracció de documents privats i envia només resultats agregats aprovats per a l'anàlisi allotjada. Revisa el material sortint. Un resum encara conté informació sensible si conserva noms, dades de clients o troballes confidencials.

## Prova abans de comprar

**Tria una tasca repetida** amb una condició final clara. Compara la configuració local amb el producte allotjat que uses, incloses les eines. Dona a tots dos les mateixes entrades i criteris d'acceptació i repeteix la tasca amb diversos exemples.

1. **Registra la configuració:** fitxer del model, quantització, versió del backend, límit de context i raonament.
2. **Defineix l'èxit:** artefacte esperat, comportament requerit i efectes secundaris prohibits.
3. **Mesura la finalització:** temps, comprovacions superades, intents fallits i reparacions manuals.
4. **Inclou el cost de propietat:** maquinari, electricitat, tarifes d'API, manteniment i temps.
5. **Classifica les fallades:** raonament, memòria, latència, context absent o verificació absent.

La **inferència local** encaixa quan la qualitat i la latència compleixen els requisits. Un model allotjat és útil quan redueix fallades o revisió. Un flux híbrid assigna tasques després de definir quines dades poden sortir de la màquina.

## Compta el cost per resultat acceptat

El **temps de reparació humana** sovint canvia l'economia. Una resposta local ràpida que necessita deu minuts de correcció consumeix més temps que una resposta lenta que supera la revisió. Compta els resultats acceptats amb la despesa d'inferència.

```text
Cost per tasca acceptada =
(assignació de maquinari + electricitat + tarifes del servei + manteniment + temps de revisió)
÷ tasques acceptades
```

**Cost de revisió il·lustratiu:** a 30 dòlars per hora, vuit minuts de correcció costen 4 dòlars per tasca. Cent tasques consumeixen 400 dòlars de revisió. Són exemples aritmètics, no taxes mesurades de fallada.

**Compara resultats equivalents.** Inclou els intents rebutjats en temps i cost. Amb maquinari propi, reparteix la compra durant un període i volum realistes. Amb un servei allotjat, inclou la subscripció o API i la revisió necessària.

Per al maquinari, continua amb la [guia de models locals, GPU i context](/articles/local-ai-model-gpu-context-guide/). Per capacitat i preus, llegeix la [comparació de memòria del DGX Spark](/articles/dgx-spark-64gb-memory-crisis-2027/). Tria la configuració més petita que compleixi qualitat, velocitat i requisits de dades.

## Vídeo de referència

{{< youtube id="siZ3f_06k8M" enable="true" title="IA local contra ChatGPT: fins a quin punt ens hi acostem?" description="Models d'IA locals i allotjats, requisits de memòria, rendiment del servei i verificació d'agents." >}}

## Referències

- **AI Mechanics:** [IA local contra ChatGPT: fins a quin punt ens hi acostem?](https://www.youtube.com/watch?v=siZ3f_06k8M).
- **Artificial Analysis:** [resultats de models](https://artificialanalysis.ai/leaderboards/models), [metodologia](https://artificialanalysis.ai/methodology/intelligence-benchmarking) i [resultats d'inferència local](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations/).
- **Editors de models:** [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) i [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3).
- **Unsloth:** [compilacions Qwen GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main) i [compilacions GLM GGUF](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main).
- **Ollama:** [documentació d'execució, memòria i privadesa](https://docs.ollama.com/faq).
- **LangChain:** [resultats d'enginyeria d'agents](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering).
- **τ-bench:** [recerca d'avaluació d'agents, eines i usuaris](https://arxiv.org/abs/2406.12045).
