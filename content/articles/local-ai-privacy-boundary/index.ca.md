---
title: "Privadesa de la IA local: què queda al vostre ordinador i què no"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Seguiu els prompts, fitxers de model, eines, registres, exposició de xarxa i costos d'energia abans d'escollir inferència local o un servei d'IA allotjat."
genre: ["IA local", "Privadesa", "IA autogestionada", "Ciberseguretat", "Economia de la IA"]
tags: ["local AI privacy", "local inference", "cloud AI", "AI data privacy", "self-hosted AI", "LLM privacy", "GPU ownership cost", "AI electricity cost", "RTX 5070", "Claude Haiku 5.5", "Ollama privacy", "llama.cpp", "AI security", "offline AI", "local language models", "prompt privacy", "AI threat model", "GPU break-even", "AI data boundary", "private AI"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Una estació de treball d'IA local connectada a un servei al núvol per rutes de dades visibles"
coverCaption: "Il·lustració de les rutes de dades d'IA local i allotjada"
---

**La IA local us ofereix un límit de dades més petit.** Un prompt processat per un runtime local queda al dispositiu quan el model, les eines, els registres i la ruta de xarxa són locals. Una GPU local no converteix l'ordinador en un sistema tancat.

Els runtimes de models, plugins d'eines, extensions del navegador, accés remot, API exposades i descàrregues de models defineixen el risc. El cost també importa. L'electricitat pot costar menys que els tokens allotjats, mentre que la propietat del maquinari allarga el punt d'equilibri complet.

Aquesta guia mapeja primer el límit de privadesa. Després comprova el cost amb preus actuals dels proveïdors, una hipòtesi de potència explícita i les xifres del vídeo proporcionat.

<!--more-->

La comparació de costos local i allotjat dona context a les fórmules següents. No copieu xifres de rendiment sense provar el mateix fitxer de model i runtime al vostre maquinari.

{{< youtube id="DmkuFpoMYmc" enable="true" title="Is local AI worth it? We did the math vs Claude Haiku 5.5" description="A local-versus-hosted AI cost comparison." >}}

El vídeo informa d'un runtime de 2 minuts i 31 segons. N'he verificat el títol i la durada a la pàgina de visualització. No he repetit la prova de maquinari. Les velocitats continuen sent mesures informades per la font.

## Resposta curta

- **Trieu inferència local per a una ruta de dades controlada.** Manteniu el servidor del model al dispositiu, lligueu-lo a loopback i limiteu l'accés a les eines.
- **Trieu inferència allotjada per a treball ocasional.** Eviteu despesa de maquinari quan la càrrega és petita o el model no encaixa al sistema.
- **Tracteu el cost local com dues xifres.** Separeu l'electricitat per hora activa de la propietat del maquinari.
- **Tracteu la privadesa com una propietat del sistema.** Un plugin que puja fitxers o una API local que escolta totes les interfícies elimina l'avantatge del model privat.

La inferència local ajuda amb text sensible, operació sense connexió, versions fixes i accés sense quota del proveïdor. Aquests avantatges no demostren respostes millors. Un model allotjat pot encaixar millor, acabar abans o requerir menys manteniment. Mesureu la càrrega abans de comprar maquinari.

## Seguiu la ruta de dades

| Component | Pregunta de privadesa | Evidència a recollir |
|---|---|---|
| **Servidor de model local** | El prompt queda a l'host? | Configuració del procés, adreça d'escolta i trànsit sortint |
| **Model al núvol** | Quins textos, fitxers i resultats d'eines surten de l'host? | Endpoint API, termes del proveïdor, registres i configuració del compte |
| **Mode núvol d'una app local** | El model seleccionat s'executa al dispositiu? | Identificador del model, proveïdor i connexió de xarxa |
| **Plugin d'eina** | El model rep fitxers, sortida de shell o contingut del navegador? | Llista d'eines, permisos i dades capturades |
| **Descàrrega de model** | Quin codi i pesos entren a l'host? | Repositori font, llicència, checksum i ruta de descàrrega |
| **Registres locals** | On persisteixen prompts i resultats? | Registres del runtime, historial shell, informes de fallada i còpies |

**Un model local elimina un proveïdor de la ruta del prompt.** Encara cal revisar la resta de la ruta.

## Local no vol dir privat per defecte

[La política de privadesa d'Ollama](https://ollama.com/privacy) afirma que Ollama no veu prompts ni dades quan el model funciona localment. La política separa l'operació local dels models allotjats al núvol. Un model al núvol crea un límit de servei encara que la mateixa aplicació iniciï tots dos modes.

[La documentació del servidor llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) mostra `127.0.0.1:8080` per defecte. Els exemples Docker també mostren `--host 0.0.0.0`, que exposa el servei a totes les interfícies. Una adreça de vinculació més ampla canvia el límit d'accés.

Comproveu l'adreça d'escolta abans d'enviar text sensible:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` o `localhost` limiten l'accés al mateix host en el cas normal. Una adreça LAN o `0.0.0.0` necessita una regla de tallafoc i un pla d'autenticació. No exposeu un endpoint de model a la xarxa sense provar tots dos.

Comproveu també el nom del model. La documentació del núvol d'Ollama descriu els models al núvol com una ruta separada. Una interfície local no demostra l'execució local.

Les [preguntes freqüents d'Ollama](https://docs.ollama.com/faq) documenten un mode només local. Establiu `disable_ollama_cloud` a `~/.ollama/server.json`, o establiu `OLLAMA_NO_CLOUD=1` abans de reiniciar el servei. Això elimina models al núvol i cerca web del runtime seleccionat. No limita altres aplicacions, eines del navegador, plugins ni l'accés de xarxa de l'host.

```json
{
  "disable_ollama_cloud": true
}
```

Verifiqueu la configuració després de reiniciar. Un runtime només local redueix una ruta. No crea un host privat.

## Calculeu el cost allotjat

Els preus dels tokens separen entrada i sortida. [Anthropic llista Claude Haiku 5.5 a $0.10 per milió de tokens d'entrada i $0.50 per milió de sortida fins a 100.000 tokens](https://www.anthropic.com/claude/haiku). Els prompts més grans usen les tarifes superiors indicades.

[La guia de tokens d'OpenAI](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) explica per què el recompte de paraules no és el recompte de tokens. També separa entrada, sortida, entrada en memòria cau i tokens de raonament. Useu els camps d'ús del proveïdor, no una estimació de paraules.

Per a una comparació simple, useu un milió de tokens generats i un milió d'entrada com a càrregues separades. Un agent de programació envia sovint context repetit i produeix una resposta petita. Una xifra combinada amaga la barreja de costos.

## Calculeu la potència local

[L'anunci de llançament de l'RTX 5070 de NVIDIA](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) va indicar un preu inicial de $549. [La pàgina de la família RTX 5070](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) llista 12 GB de memòria i 250 W de potència gràfica total per al disseny de referència Founders Edition. La pàgina encara mostrava $549 i la targeta sense estoc durant la revisió.

La xifra de potència de la GPU no és la potència de tot el sistema. Useu un mesurador a la paret. L'exemple assumeix **400 W de consum de tot el sistema**, amb GPU, processador, memòria, emmagatzematge, ventiladors i pèrdues de la font. És una hipòtesi de càlcul, no una mesura.

[La previsió de la U.S. Energy Information Administration](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) va usar 18,2 cèntims per kWh com a preu residencial mitjà de l'electricitat el 2026. La vostra tarifa canvia el resultat.

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

Amb 400 W i $0.182 per kWh, el sistema costa $0.0728 per hora activa.

| Velocitat de sortida | Temps per 1M tokens | Cost d'energia per 1M tokens |
|---:|---:|---:|
| **20 tokens per segon** | 13 hores 53 minuts | **$1.01** |
| **50 tokens per segon** | 5 hores 33 minuts | **$0.40** |
| **94 tokens per segon** | 2 hores 57 minuts | **$0.22** |

A 50 tokens de sortida per segon, la potència local costa menys que els $0.50 de sortida de Haiku 5.5. A 20 tokens costa més. El llindar és d'uns 40 tokens per segon amb aquestes hipòtesis.

El càlcul d'entrada usa la mateixa fórmula. A 2.650 tokens d'entrada per segon, un milió triga uns 6 minuts i 17 segons i costa aproximadament $0.008. A 1.000 tokens per segon costa $0.020.

La transcripció proporcionada informa de 94 tokens de sortida per segon i 2.650 d'entrada per al seu exemple RTX 5070. El càlcul coincideix amb 400 W. No hi ha registre de laboratori independent, hash del model, build del runtime, prompt ni lectura del mesurador. Tracteu aquestes velocitats com a referència, no com a garantia de compra.

## Punt d'equilibri dels canvis de maquinari

L'estalvi d'energia no paga el maquinari per si sol. Compareu la compra completa amb la diferència entre cost de sortida allotjat i cost variable local.

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

A 94 tokens de sortida per segon, l'estalvi arrodonit puja a uns $0.28 per milió. Recuperar una GPU de $549 requereix uns 2.000 milions de tokens. Ambdues xifres exclouen memòria, emmagatzematge, placa, font, refrigeració, manteniment i revenda.

El preu de llançament no és una oferta universal. La pàgina de NVIDIA mostrava el preu oficial sense estoc. Un anunci de $819 necessita verificació separada. Useu la factura real i la potència mesurada a la paret.

**El maquinari existent canvia la decisió.** Si la vostra estació ja té prou memòria i una GPU adequada, el maquinari és un cost enfonsat per a la tasca següent. Compareu potència, temps, qualitat, privadesa i manteniment. Si compreu el sistema complet, compareu-lo amb l'ús allotjat.

Per als detalls d'encaix del model, llegiu la [guia de models locals i context de GPU](/articles/local-ai-model-gpu-context-guide/) i la [guia de 16GB VRAM](/articles/is-16gb-vram-enough-local-llm/). Per a una configuració d'agent local, llegiu la [guia de Strata i OpenCode](/articles/strata-opencode-local-coding-agent-16gb/).

## Què ofereix la privadesa local

- **Ruta de dades més curta:** el prompt no ha d'arribar al proveïdor quan la inferència és local.
- **Operació sense connexió:** un model descarregat i un runtime local no necessiten una connexió activa per generar text.
- **Control de versions:** trieu el fitxer i la versió del runtime en lloc d'un canvi automàtic del proveïdor.
- **Control d'ús:** la inferència local evita el comptador al núvol per petició després de comptar maquinari i energia.
- **Control de xarxa:** el tallafoc i els controls de l'host defineixen qui arriba a l'endpoint.

Aquests guanys importen per al codi font, registres de clients, dissenys no publicats, notes privades i entorns desconnectats. La inferència local encara necessita xifratge de disc, actualitzacions, separació de comptes i eines restringides.

## Què no ofereix la privadesa local

- **Cap garantia de qualitat:** els models petits o quantitzats s'han de provar amb els vostres criteris d'acceptació.
- **Cap garantia de cadena de subministrament:** fitxers, runtimes, plugins i imatges necessiten fonts fiables i comprovacions d'integritat.
- **Cap host net:** malware, extensions, còpies, informes de fallada i administració remota continuen veient dades de l'host.
- **Cap endpoint segur:** un servidor lligat a totes les interfícies crea un servei nou que cal defensar.
- **Cap sistema gratuït:** electricitat, emmagatzematge, refrigeració, desgast i manteniment costen.

La [guia d'agent local de Strata](/articles/strata-opencode-local-coding-agent-16gb/) mostra per què memòria, context, eines i runtime entren en l'avaluació. La memòria de GPU sola no defineix el límit de privadesa ni de rendiment.

## Trieu el límit adequat

| Situació | Primera opció | Motiu |
|---|---|---|
| **Documents sensibles i PC compatible existent** | Inferència local | Mantenir prompts en un host controlat i evitar hardware nou |
| **Redacció genèrica ocasional** | API o xat allotjat | Pagar la càrrega petita i evitar manteniment |
| **Model avançat o eina cloud especialitzada** | Servei allotjat | El model o l'eina no existeix a l'host local |
| **Volum recurrent gran amb model local verificat** | Local o híbrid | Comparar energia, qualitat, temps de suport i preus |
| **Càrregues mixtes** | Routing híbrid | Mantenir tasques sensibles locals i enviar tasques aprovades al model allotjat |

**El routing híbrid necessita una regla explícita de classificació.** Marqueu les dades com només locals, aprovades per a processament allotjat o prohibides fins a revisió. No depengueu del nom del model ni de la icona de l'aplicació.

## Verifiqueu abans de confiar

1. **Anomeneu la ruta del model.** Registreu identificador, runtime, versió i font de descàrrega.
2. **Comproveu l'adreça de binding.** Confirmeu loopback llevat que hi hagi una necessitat documentada més ampla.
3. **Llisteu cada eina.** Reviseu accés a fitxers, shell, navegador, xarxa i plugins.
4. **Inspeccioneu la persistència.** Busqueu registres, sortides, fallades, còpies i directoris compartits.
5. **Proveu la xarxa.** Observeu connexions durant una prova sensible amb un prompt representatiu.
6. **Mesureu el sistema.** Registreu potència, velocitats, longitud de context i reintents.
7. **Proveu la feina acceptada.** Compareu tasques completades i esforç de revisió, no només tokens per segon.

La [guia d'IA local contra ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) tracta les diferències de capacitat. Useu aquesta llista al costat de la prova de qualitat.

## Referències

- [Video, Is local AI worth it? We did the math vs Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [NVIDIA Blackwell GeForce RTX 50 Series launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [NVIDIA GeForce RTX 5070 family specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [NVIDIA GeForce RTX 5070 product page](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, October 2026 Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Anthropic Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Ollama privacy policy](https://ollama.com/privacy)
- [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
