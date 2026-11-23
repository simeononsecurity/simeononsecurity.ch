---
title: "AI-cybersecurity in 2026: snel invoeren, later beveiligen"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-23
description: "Een beoordeling van AI-adoptie in cybersecurity, operationele hiaten, actuele richtlijnen en praktische beheersmaatregelen voor organisaties in 2026."
tags: ["AI-beveiliging", "AI-cybersecurity 2026", "promptinjectie", "AI-agenten", "MCP-beveiliging", "AI-toeleveringsketen", "schaduw-AI", "AI-red-teaming", "LLM-beveiliging", "AI-observability", "agentische AI", "AI-dreigingen", "AI-aanvallen", "modelbeveiliging", "AI-governance", "NIST AI 600-1", "OWASP LLM", "MITRE ATLAS", "AI-incidentrespons", "enterprise-AI-beveiliging", "AI-identiteit", "contextvergiftiging", "toolvergiftiging", "AI-autorisatie"]
cover: "/img/cover/state-of-ai-cybersecurity-2026.webp"
coverAlt: "Een illustratie van onderling verbonden AI-systemen als gloeiende knooppunten tegen een donkere achtergrond, met heldere verbindingslijnen en schaduwen die beveiligingskwetsbaarheden rond sommige knooppunten tonen."
coverCaption: ""
---

Organisaties hebben in 2023, 2024 en 2025 in hoog tempo AI-systemen ingevoerd. Defensieve richtlijnen, beveiligingstools en operationele werkwijzen konden dat tempo niet bijhouden. **Het resultaat in 2026 is een groot, slecht gemonitord aanvalsoppervlak dat verbonden is met echte bedrijfssystemen, terwijl de verdediging nog wordt opgebouwd.**

Ik wil precies uitleggen wat mij zorgen baart en waarom. Dit is geen algemene waarschuwing over AI-risico's. Het beschrijft hoe het daadwerkelijke aanvalsoppervlak eruitziet, waar de hiaten zijn vastgelegd en wat organisaties moeten aanpakken.

## Waarom deze kloof bestaat

De beveiliging van traditionele software ontwikkelde zich in ongeveer drie decennia. Tientallen jaren ervaring met incidentrespons, kwetsbaarheidsonderzoek, toolontwikkeling en moeizaam opgedane operationele kennis leverden de frameworks, producten en werkwijzen op waarop moderne beveiligingsprogramma's bouwen.

**Generatieve AI voor bedrijven bereikte in ongeveer twee jaar miljoenen productie-implementaties.**

De disciplines die softwarebeveiliging effectief maken, zoals dreigingsmodellering voor specifieke architecturen, geharde implementatiepatronen, volwassen draaiboeken voor incidentrespons en gevestigde audit- en observability-praktijken, kregen geen tijd om zich te ontwikkelen voordat organisaties AI op grote schaal invoerden. *De richtlijnen kwamen na de implementatie. De tools kwamen na de richtlijnen. De operationele expertise ontwikkelt zich nog steeds.*

Dit is geen verwijt. Het verklaart waarom de hiaten structureel zijn in plaats van toevallig.

## De vier lagen van AI-beveiliging

Veel verwarring in discussies over AI-beveiliging ontstaat doordat governancedocumenten, dreigingstaxonomieën, technische richtlijnen en operationele controles als hetzelfde worden behandeld. Dat zijn ze niet.

**Laag 1 is governance.** NIST AI RMF, ISO/IEC 42001 en de EU AI Act werken op organisatorisch en procesniveau. Ze beschrijven hoe organisaties AI-risico's beheren, toezicht structureren en verantwoording documenteren. Het zijn governanceframeworks, geen technische controles.

**Laag 2 is dreigingstaxonomie.** MITRE ATLAS documenteert vijandige tactieken tegen AI-systemen. De OWASP Top 10 for LLMs en de OWASP Agentic AI Top 10 sommen specifieke aanvalsklassen op. Deze documenten benoemen aanvallen. Ze schrijven geen verdediging voor.

**Laag 3 is technische richtlijn.** Google SAIF, Microsoft AI SDL, OWASP AI Exchange en NIST AI 600-1 geven richtlijnen voor het veilig bouwen en implementeren van AI. NIST AI 600-1 is veel specifieker dan het basis-AI RMF en behandelt promptinjectie, datavergiftiging en informatiegevaren bij generatieve AI-implementaties.

**Laag 4 is operations.** Monitoring, incidentrespons, runtimecontroles, logging, minimale rechten, evaluatiepijplijnen en toegangsbeheer zijn operationele werkwijzen. Ze vereisen organisatorische processen, niet alleen documentatie.

*De meeste organisaties hebben onvolledige dekking op laag 3 en 4. Daar bevindt zich vrijwel al het operationele risico.*

## Wat er in productie draait

Enterprise-AI in 2026 bestaat uit meer dan chatbots. Productiesystemen omvatten:

- **RAG-systemen** die interne documentarchieven, wiki's, databases en klantgegevens ophalen
- **Ondersteuningsagenten voor klanten** met toegang tot accountgegevens en casemanagementsystemen
- **Interne productiviteitsassistenten** die zijn geïntegreerd met e-mail, agenda's, bestandssystemen en communicatieplatforms
- **Tools voor codebeoordeling en -generatie** met toegang tot broncoderepositories
- **Geautomatiseerde agenten** die geplande workflows uitvoeren met inloggegevens voor interne API's
- **Verwerkers van documenten, contracten en financiële gegevens**
- **AI-modellen in fraudedetectie, werving en beslissingen over toegangscontrole**

Elk systeem vormt een ander aanvalsoppervlak. Een RAG-systeem boven op je interne kennisbank is tegelijk een risico op informatielekken en een doelwit voor promptinjectie. **Een agent met e-mailtoegang en een blijvend inloggegeven is een autonoom proces met echte invloed op echte systemen.**

*Beveiligingsteams waren vaak niet betrokken bij het besluit deze systemen in te voeren. Ze ontdekken bestaande AI-implementaties geregeld via audits in plaats van tijdens ontwerpbeoordelingen.*

## AI staat nu aan beide kanten

**Dezelfde AI-mogelijkheden die je beveiligingsteam gebruikt, zijn beschikbaar voor aanvallers.**

**AI-ondersteunde ontwikkeling** verkort de tijd die nodig is om openbare kwetsbaarheidsmeldingen om te zetten in werkende proof-of-concepts en operationele tools. Iedereen die deze tools gebruikt, ook aanvallers, kan sneller van het lezen van een CVE naar werkende code gaan.

**AI-gegenereerde phishinginhoud** levert e-mails op met betere grammatica, overtuigender context en minder herkenbare fouten dan veel door mensen geschreven aanvallen. Opmaaksignalen en taalpatronen waarop gebruikers leerden letten, zijn minder betrouwbaar wanneer AI de inhoud maakt.

**Stemklonen voor vishingcampagnes** imiteert leidinggevenden en collega's tijdens live gesprekken. De drempel voor gerichte social engineering daalde doordat stemsynthetisatie beter werd en goedkoper toegankelijk raakte.

**Deepfakevideo voor CEO-fraude** is van theorie naar praktijk gegaan. Financiële fraude met AI-video's waarin leidinggevenden transacties goedkeuren, is sinds 2024 in meerdere sectoren gedocumenteerd. *Je bewustzijnstraining was bedoeld voor een ander dreigingsmodel.*

## Promptinjectie en contextvergiftiging

**Promptinjectie begrijpen is het begin van inzicht in de beveiliging van AI-systemen.**

Een taalmodel volgt instructies in zijn contextvenster. Dat venster omvat de systeemprompt, gespreksgeschiedenis, tooluitvoer en opgehaalde documenten. **Het model kan instructies van de applicatieontwikkelaar niet betrouwbaar onderscheiden van instructies die een aanvaller in verwerkte inhoud heeft geplaatst.** Dit vormt de kern van promptinjectie volgens OWASP.

*Directe promptinjectie* richt zich rechtstreeks op de invoer van het model. De gebruiker geeft tekst op die de systeeminstructies moet overschrijven.

*Indirecte promptinjectie* vormt een groter risico voor zakelijke implementaties. Je RAG-agent haalt een document uit de kennisbank op. In dat document staan instructies om een andere actie uit te voeren. Je samenvattingstool verwerkt een webpagina met verborgen aanwijzingen. Je supportbot leest een klantbijlage met instructies. De agent verwerkt die instructies en voert ze uit.

**Contextvergiftiging** is een bredere categorie. Aanvallers hoeven je model niet te compromitteren om je AI-systeem aan te vallen. Ze moeten schadelijke inhoud in de context van het model krijgen. Denk aan vergiftigde RAG-documenten, vergiftigde geheugenitems, kwaadaardig opgestelde e-mail die een agent verwerkt, adversariële pdf's en door aanvallers beheerde webpagina's die een browseragent bezoekt. *Dit verschilt van modelvergiftiging. Het model is in orde. De context niet.*

Verdediging in de diepte verkleint dit risico. Invoerfilters, uitvoervalidatie, tools met beperkte rechten, geïsoleerde uitvoering en menselijke goedkeuring voor ingrijpende acties helpen allemaal. **Geen van deze maatregelen sluit de aanvalsklasse uit.** OWASP, NIST, Anthropic, OpenAI en Microsoft bevelen gelaagde benaderingen aan omdat geen enkele controle op zichzelf volstaat.

*Ontwerp met de aanname dat promptinjectie bij een deel van de invoer zal slagen. Beperk de gevolgen daarop.*

## AI-agenten, bevoegdheidsgrenzen en het probleem van de impactomvang

Agenten verschillen operationeel op een cruciaal punt van chatbots: **ze voeren acties uit.**

Een agent die is gekoppeld aan je e-mail, GitHub, Jira, Slack, Salesforce, AWS en interne API's is een autonoom proces met toegang tot dezelfde systemen die je meest verbonden medewerkers gebruiken. **Een geslaagde promptinjectie tegen deze agent levert geen ongewenst tekstantwoord op. Ze veroorzaakt een ongewenste actie op een echt systeem.**

**De impactomvang van een compromittering hangt af van waartoe de agent toegang heeft.** Veel huidige agentimplementaties hebben veel meer toegang dan een afzonderlijke taak vereist. Een agent die een Jira-ticket moet lezen, hoort geen schrijftoegang tot de hoofdbranch van GitHub te hebben. Een agent die ondersteuningsverzoeken verwerkt, hoort geen inloggegevens voor het facturatiesysteem te bewaren.

**AI-autorisatie is een ander probleem dan gebruikersautorisatie.** Traditionele applicaties vragen of een gebruiker een actie mag uitvoeren. Agentarchitecturen moeten vragen of deze agent deze specifieke actie voor deze specifieke gebruiker op dit specifieke moment en op basis van de huidige context mag uitvoeren. De meeste huidige agentimplementaties doen dit niet.

**Toolvergiftiging** verschilt van promptinjectie. Een kwaadaardige of gecompromitteerde tool die aan een agent is gekoppeld, geeft beschrijvingen of gegevens terug die bedoeld zijn om het gedrag van de agent te veranderen. Onderzoekers behandelen toolvergiftiging steeds vaker als een afzonderlijke aanvalsklasse, vooral bij integraties op basis van MCP.

*Menselijke goedkeuringsprocessen moeten de laatste bescherming vormen voor ingrijpende acties van agenten. Organisaties ontdekken dat ook goedkeuringsmoeheid ontstaat. Wanneer agenten regelmatig routineacties ter goedkeuring voorleggen, keuren gebruikers die steeds vaker automatisch goed zonder het verzoek te controleren. De laatste bescherming wordt een formaliteit.*

## AI-identiteit is een beveiligingsprobleem voor bedrijven

**Agenten hebben inloggegevens.** OAuth-tokens, API-sleutels, serviceaccountgegevens en cloud-IAM-rollen komen allemaal voor in AI-agentimplementaties. Het zijn niet-menselijke identiteiten met echte toegang.

Specifieke hiaten in huidige implementaties:

- **Inloggegevens van agenten zijn vaak langdurig geldig** en worden niet volgens een schema geroteerd dat vergelijkbaar is met serviceaccounts
- **Tokentoepassingen van agenten zijn vaak ruimer** dan nodig is voor de taken die ze uitvoeren
- Auditlogging van acties onder agentidentiteiten verschilt sterk per implementatie
- **Het lekken van inloggegevens via prompts** is een gedocumenteerd risico. Een agent die API-sleutels in context of uitvoer opneemt, stelt ze bloot aan iedereen die de uitvoer leest of het gesprek ophaalt.
- Agenten die via toolaanroepen extra inloggegevens verkrijgen, creëren **identiteitsketens die moeilijk te controleren zijn**

*Beheer agentidentiteiten zoals je bevoorrechte serviceaccounts beheert. Dat vergt nu bewuste inspanning, omdat de meeste tools voor identiteitsbeheer geen ingebouwde ondersteuning bieden voor patronen rond AI-agentidentiteiten.*

## Blijvend agentgeheugen creëert een aanvalsvlak op lange termijn

**Agenten met blijvend geheugen hebben een aanvalsoppervlak dat niet bestaat in stateless systemen.**

Een aanvaller die inhoud in het geheugen van een agent kan injecteren, bouwt een positie op die sessies overstijgt. *De aanval hoeft niet in één interactie te slagen. Invloed die dagen of weken in het geheugen is opgebouwd, vormt het toekomstige gedrag van de agent.* Dit heet soms een **aanval met lange horizon of slapende context**.

Voor dit specifieke risico bestaat weinig operationele richtlijn. Organisaties die agenten met blijvende geheugenopslag invoeren, moeten:

- **Geheugenopslag behandelen als waardevolle gegevens** die toegangscontroles vereisen
- **Geheugeninhoud valideren** voordat agenten erop handelen
- De mogelijkheid om de **geheugentoestand te controleren en terug te draaien** in de architectuur opnemen

## De modeltoeleveringsketen wordt niet behandeld als de softwaretoeleveringsketen

**Organisaties die vooraf getrainde modellen uit openbare repositories downloaden, accepteren uitvoerbare AI-artefacten van externe bronnen. De controle op deze downloads is doorgaans minder streng dan de controle die dezelfde organisaties toepassen op npm-, PyPI- of Maven-pakketten.**

Specifieke risico's in modelrepositories:

- **Modelbestanden in PyTorch-pickleformaat** voeren willekeurige Python-code uit tijdens het laden. Dit is misbruikt bij gedocumenteerde aanvallen op de toeleveringsketen. **SafeTensors** is speciaal ontworpen om dit risico aan te pakken. Gebruik het wanneer het beschikbaar is.
- Kwaadaardige modelladers die afhankelijkheden installeren of setupcode uitvoeren naast het model
- Modellen die zijn getraind op **vergiftigde datasets** en in specifieke contexten subtiel onjuiste uitvoer geven
- Modellen met **ingebouwde achterdeuren** die onder bepaalde triggercondities worden geactiveerd
- **Repositorynaamsquatting** om kwaadaardige modellen onder bekende namen aan te bieden

*Weinig organisaties houden een softwarestuklijst bij van hun AI-systemen.* De meeste kunnen niet vertellen met welk basismodel een productiesysteem is begonnen, welke versie van de trainingsgegevens voor fine-tuning is gebruikt of of de gewichten in productie overeenkomen met de laatst geëvalueerde gewichten. Die traceerbaarheid is een voorwaarde voor betekenisvolle beveiliging van de toeleveringsketen. Ze is tegenwoordig niet gebruikelijk.

## Schaduw-AI veroorzaakt ongecontroleerde gegevensstromen

**Persoonlijke AI-accounts voor consumenten zijn een route waarlangs gegevens zonder controles worden verplaatst.**

ChatGPT Enterprise, Claude Enterprise en Microsoft Copilot voor M365 bieden contractuele bescherming voor klantgegevens. **Persoonlijke ChatGPT-, Claude- en Gemini-accounts en vergelijkbare consumentenaccounts bieden deze garanties niet standaard.**

Medewerkers die persoonlijke accounts gebruiken om werkdocumenten te verwerken, verplaatsen juridische strategieën, klantgegevens, broncode, financiële prognoses, personeelsbeslissingen en interne communicatie via kanalen die hun organisatie niet beheert. *Beveiligingsteams hebben vaak geen accuraat beeld van de omvang van deze activiteit of de betrokken gegevenscategorieën.*

Je DLP-controles detecteren geen gegevens die via een webbrowser naar een consumentendienst voor AI gaan. Je bewaarbeleid geldt niet voor gespreksgeschiedenis op een platform van derden. **Je wettelijke verplichtingen onder de AVG, HIPAA, SOX en sectorspecifieke regels veranderen niet doordat gegevens per ongeluk of via een browsertabblad zijn vertrokken.**

*De daadwerkelijke omvang vaststellen voordat je controles bouwt, is de noodzakelijke eerste stap. Je inschatting van dit probleem onderschat de werkelijkheid vrijwel zeker.*

## AI-systemen lekken gegevens op manieren die traditionele applicaties niet kennen

**Te veel ophalen met RAG** geeft documenten terug aan gebruikers die er geen toegang toe horen te hebben. Een medewerker stelt een vraag. De ophaalcomponent geeft een document uit een afgeschermd deel van de kennisbank terug. Het antwoord bevat informatie uit dat document. *De fout in de toegangscontrole ontstond in de ophaallaag, niet in de applicatielaag.* Veel RAG-implementaties zijn gebouwd zonder documentmachtigingen af te dwingen die overeenkomen met het bronsysteem.

**Het uitlekken van systeemprompts** onthult de operationele instructies in je AI-product. Behandel systeemprompts als vertrouwelijk. Het lekken van inloggegevens via prompts, waarbij agentgegevens in de modelcontext of uitvoer verschijnen, vormt doorgaans een ernstiger blootstelling dan alleen de inhoud van een systeemprompt.

**Fouten in de isolatie van multi-tenant AI** ontstaan wanneer fijn afgestemde modellen die met gegevens van meerdere klanten zijn getraind, informatie van de ene klant in de context van een andere tonen. Dit is een gedocumenteerde risicocategorie voor AI-producten van multi-tenant SaaS-diensten.

**Modelmemorisatie** zorgt ervoor dat modellen inhoud uit trainingsgegevens letterlijk reproduceren. Het risico verdwijnt niet, vooral niet bij modellen die zijn fijn afgestemd op kleine of onvoldoende ontdubbelde privédatasets. Organisaties die op gevoelige interne gegevens finetunen, moeten het memorisatierisico beoordelen voor hun specifieke aanpak en gegevens.

## Organisaties missen zichtbaarheid tijdens inferentie

Traditionele beveiligingsprogramma's hebben uitgebreide logdekking van hun infrastructuur. **De meeste AI-implementaties hebben geen gelijkwaardige dekking voor hun AI-componenten.**

Monitoring van een geïmplementeerd taalmodel of agent vereist andere telemetrie dan monitoring van een applicatieserver. Organisaties moeten verzamelen:

- **Prompt- en uitvoerinhoud** in een vorm die geschikt is voor beleidscontrole en anomaliedetectie
- **Toolaanroeplogs** voor agenten, inclusief toolnamen, argumenten en antwoorden
- **Ophaallogs** voor RAG-systemen, inclusief zoekopdrachten, teruggegeven documenten en beslissingen over toegangscontrole
- **Classificatiesignalen** voor jailbreak- en injectiepogingen
- **Monitoring van uitvoerconsistentie** om gedragsverschuivingen tussen modelversies te detecteren
- **Latentiepatronen** die kunnen wijzen op pogingen om de context vol te stoppen

*Veel organisaties die in 2023 en 2024 AI invoerden, hebben HTTP-statuscodes en latentiemetingen. De telemetrie die nodig is om een AI-beveiligingsincident te detecteren of onderzoeken, ontbreekt vaak. Vóór een incident is het te laat om dat te ontdekken.*

## AI-incidentrespons heeft eigen draaiboeken nodig

**Je bestaande draaiboeken voor incidentrespons behandelen endpoints, netwerken, applicaties en identiteit. Ze behandelen geen AI-specifieke scenario's.**

Vragen die je incidentresponsteam krijgt en waar huidige draaiboeken geen antwoord op geven:

- Hoe stel je vast of een model tijdens een fine-tuningrun is vergiftigd?
- Hoe bepaal je de impactomvang van een geslaagde indirecte injectie tegen een agent met schrijftoegang tot meerdere systemen?
- Hoe beoordeel je of trainings- of fine-tuninggegevens zijn buitgemaakt tijdens een compromittering van de toeleveringsketen?
- Hoe stel je een **gedragsbaseline** voor een model vast om met gedrag na een incident te vergelijken?
- Hoe reageer je wanneer een modelupdate van een externe aanbieder gedrag introduceert dat opzettelijk lijkt in plaats van onbedoeld?
- Hoe stel je vast of de **geheugenopslag van een agent in de loop van de tijd is gemanipuleerd**?

*Deze scenario's vereisen voorbereiding voordat ze zich voordoen. De telemetrie moet aanwezig zijn vóór het incident. Je moet baselines van modelgedrag vastleggen voordat je ze nodig hebt voor vergelijking.*

## Evaluatiepijplijnen worden standaardpraktijk in engineering

AI-beveiliging steunt steeds meer op **gestructureerde evaluatie vóór implementatie** in plaats van alleen monitoring na implementatie.

Beveiligingsevaluatie vóór implementatie omvat:

- **Tests op promptinjectie** met gevestigde injectiedatasets en je specifieke gebruikssituatie
- **Jailbreak-benchmarktests** met gepubliceerde verzamelingen adversariële prompts
- **Beoordeling van adversariële robuustheid** voor modellen die ingrijpende beslissingen nemen
- **Regressietests** tussen modelversies om gedragsveranderingen vast te stellen
- **Beleidsevaluatie** aan de hand van gedocumenteerde eisen voor aanvaardbaar gebruik
- **Red-teamingoefeningen** door mensen die specifieke verdedigingen proberen te doorbreken

NIST, CISA, Anthropic, OpenAI, Microsoft en Google verwachten dit steeds vaker bij implementaties met een hoog risico. *Minimale evaluatiepijplijnen bouwen vóór implementaties met grote gevolgen is haalbaarder dan de meeste organisaties denken.* OWASP AI Exchange en de gepubliceerde evaluatieframeworks van grote AI-aanbieders zijn goede uitgangspunten.

## Je inventaris van AI-activa is waarschijnlijk onvolledig

Traditioneel activabeheer omvat servers, endpoints, applicaties en netwerkapparaten. **AI-systemen introduceren categorieën activa die de meeste inventarissen nog niet bijhouden.**

Een inventaris van AI-systemen moet bevatten:

- Elk **geïmplementeerd model**, inclusief basismodellen, fijn afgestemde varianten en embeddingmodellen
- Alle **prompts en systeeminstructies** die in productie actief zijn
- Elke **agent** in je omgeving en de tools waartoe die toegang heeft
- Alle **RAG-indexen**, inclusief hun gegevensbronnen en de toegangscontroles die bij het ophalen worden afgedwongen
- Alle **vectordatabases** en hun inhoud
- Elke **MCP-server of gelijkwaardig integratieframework** dat met een agent is verbonden
- **Externe AI-diensten** die je applicaties aanroepen, inclusief de gegevens die naar elke dienst gaan

*Je kunt niet beheren wat je niet hebt geïnventariseerd. De meeste organisaties die in 2026 aan AI-beveiliging werken, ontdekken activa waarvan ze niet wisten dat ze bestonden.*

## Waar de verdediging daadwerkelijk staat

De verdedigingstools, frameworks en werkwijzen voor AI-beveiliging ontwikkelen zich actief en betekenisvol. Het vakgebied staat nog aan het begin, maar ontwikkelt zich.

**NIST AI 600-1** breidt het basis-AI RMF voor generatieve AI uit met veel specifiekere operationele richtlijnen. Organisaties met AI-complianceprogramma's horen AI 600-1 te lezen, niet alleen het basisframework.

**MITRE ATLAS** biedt documentatie van vijandige TTP's voor AI-systemen in ATT&CK-formaat. Dreigingsmodellering vóór implementatie op basis van ATLAS levert preciezere beveiligingseisen op dan alleen werken met governanceframeworks.

**OWASP LLM Top 10** en **OWASP Agentic AI Top 10** bieden momenteel de meest operationeel specifieke openbare richtlijnen. Beide zijn voor vakmensen direct bruikbaarder dan de meeste formele lesprogramma's.

**AI-red-teaming** vóór implementatie wordt voor risicovolle implementaties steeds vaker verwacht door NIST, CISA en grote AI-aanbieders. De externe markt voor AI-red-teaming bestaat al en groeit voor organisaties zonder eigen capaciteit.

AI-specifieke beveiligingsproducten voor monitoring, guardrails, autorisatie en afdwinging van runtimebeleid bevinden zich in een vroege commerciële fase. *Deze categorie bestaat en is het beoordelen waard. Omdat de markt jong is, gaan marketingclaims vaak verder dan aangetoonde mogelijkheden. Beoordeel producten aan de hand van je specifieke implementatiearchitectuur, niet aan de hand van scenario's die leveranciers beschrijven.*

## Wat je moet doen

**Inventariseer wat is geïmplementeerd.** Weet wat er draait, welke gegevens het raadpleegt, welke inloggegevens het heeft, welke tools het aanroept en welke acties het uitvoert. Dit is een voorwaarde voor al het andere.

**Behandel AI-agenten als bevoorrechte accounts.** Pas minimale rechten toe. Beperk inloggegevens tot de minimale toegang die elke taak vereist. Controleer welke toegang elke agent heeft en verwijder wat niet nodig is.

**Implementeer AI-specifieke observability vóór de implementatie**, niet na een incident. Logging van prompts en uitvoer, toolaanroepen en opgehaalde gegevens vormt de minimale telemetrie voor beveiligingsanalyse.

**Beoordeel je blootstelling aan schaduw-AI.** Breng in kaart welke AI-diensten medewerkers voor hun werk gebruiken. Bepaal welke gegevenscategorieën via persoonlijke accounts lopen. Baseer beleid en controles op de bevindingen.

**Dwing documentniveau-toegangscontroles af in RAG-systemen.** Als je ophaallaag de toegangsregels van de bronsystemen niet afdwingt, los dit dan op voordat een onbevoegde gebruiker een afgeschermd document te zien krijgt.

**Controleer je modeltoeleveringsketen.** Documenteer elk gebruikt basismodel. Geef de voorkeur aan SafeTensors boven pickleformaten. Pas op modelartefacten dezelfde controle op de toeleveringsketen toe als op softwareafhankelijkheden.

**Beheer agentidentiteiten.** Beheer OAuth-tokens en API-sleutels van agenten met dezelfde levenscyclus, controle van scopes en rotatiepraktijken als voor bevoorrechte serviceaccounts.

**Bouw nu draaiboeken voor AI-incidentrespons.** Bepaal vóór een incident hoe je AI-specifieke scenario's onderzoekt, welk bewijs je nodig hebt en welke responsopties beschikbaar zijn.

**Voer evaluaties uit voordat je AI inzet in situaties met grote gevolgen.** Begin met beschikbare openbare frameworks als je geen interne tools hebt.

*Behandel naleving van governance niet als een beveiligingsstatus. Governanceframeworks beschrijven processen en risicobeheer. Ze beschrijven geen technisch verdedigbare systemen. Je hebt beide nodig.*

## Referenties

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL
- CISA Guidance on AI Cybersecurity, 2024
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- SafeTensors format documentation, Hugging Face
