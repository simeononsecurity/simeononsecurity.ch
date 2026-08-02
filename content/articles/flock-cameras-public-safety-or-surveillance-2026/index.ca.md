---
title: "Càmeres Flock: Eina de Seguretat Pública o Màquina de Vigilància Sense Ordre Judicial?"
date: 2026-08-01
toc: true
draft: false
description: "Una anàlisi independent de les càmeres ALPR de Flock Safety: com funcionen realment, quines dades recullen més enllà de les matrícules, com l'intercanvi de dades crea una base de dades nacional oculta, i per què la qüestió de l'ordre judicial és el problema real."
genre: ["Privadesa", "Vigilància", "Llibertats Civils", "Tecnologia per a l'Aplicació de la Llei", "Drets Digitals"]
tags: ["Flock Safety", "ALPR", "lectors de matrícules", "vigilància", "privadesa", "vigilància sense ordre judicial", "anàlisi de comboi", "seguiment per Bluetooth", "seguiment TPMS", "intercanvi de dades", "càmeres Ring", "Quarta Esmena", "res a amagar", "precisió LPR", "acusació errònia", "MFA", "tecnologia per a l'aplicació de la llei", "llibertats civils", "minimització de dades", "DeFlock", "contravigilància", "seguretat pública", "vigilància policial", "drets a la privadesa", "Quarta Esmena", "vigilància digital", "vigilància massiva", "reconeixement de matrícules", "xarxes de càmeres", "retenció de dades"]
cover: "/img/cover/flock-cameras-public-safety-or-surveillance-2026.webp"
coverAlt: "Una cruïlla fosca il·luminada per una càmera de vigilància muntada en un pal, amb dades de matrícules superposades als cotxes que passen."
coverCaption: ""
canonical: "https://simeononsecurity.com/articles/flock-cameras-public-safety-or-surveillance-2026/"
---

**El debat sobre les càmeres de Flock Safety divideix les persones d'una manera que gairebé res més no ho fa en la política tecnològica. Els qui han tingut un cotxe robat tendeixen a estimar-les. Els qui estudien dret constitucional tendeixen a odiar-les. Ambdós reaccionen davant d'alguna cosa real.**

Aquesta és una anàlisi independent del que fan realment aquests sistemes, el que diu l'evidència sobre la seva precisió i ús indegut, i per què la pregunta més important no és si les càmeres poden fotografiar carrers públics — sinó si el govern hauria de construir una base de dades cercable i sense ordre judicial dels moviments de tothom.

{{< youtube id="fFuE2-xtq2w" >}}

*Aquest tema va generar un debat públic significatiu a mitjan 2026. El vídeo anterior cobreix una sèrie de perspectives i contraarguments dels espectadors que val la pena considerar juntament amb l'anàlisi aquí.*

______

## Per Què les Càmeres Flock Són Diferents del Vostre Telèfon

La defensa més comuna de les càmeres de Flock Safety és la següent: el vostre telèfon ja us segueix a tot arreu. La policia pot obtenir les vostres dades GPS amb una ordre judicial. Les càmeres Flock són menys precises que això. Llavors, per què preocupar-se?

L'argument és superficialment raonable i fonamentalment erroni.

**El vostre telèfon us segueix a vosaltres. Les càmeres Flock segueixen tothom.** Quan la policia obté les vostres dades de localització de torres de telefonia mòbil o l'historial GPS, necessiten una ordre judicial, un objectiu específic i causa probable. Quan un agent consulta la base de dades de Flock, no necessita res d'això. Pot cercar per número de matrícula, finestra temporal, ubicació o descripció del vehicle — sense ordre judicial, sense sospitós nomenat, sense cap sospita.

El resultat és una **vigilància massiva sense ordre judicial de tota una població**, no la vigilància dirigida d'un individu concret. La Quarta Esmena va ser dissenyada específicament per prevenir exactament aquest tipus de cerca general.

El seguiment de telèfons mòbils tampoc construeix un registre permanent i consultable de cada vehicle que va passar per cada encreuament de la vostra ciutat durant els últims 30 dies. Flock sí. Aquesta base de dades persistent i estructurada és el que la fa qualitativament diferent d'un policia que anota un número de matrícula o d'un negoci que instal·la una càmera de seguretat.

**Una fotografia no és un sistema de vigilància. Sí que ho és una base de dades cercable, amb marca de temps, de fotografies vinculades per la identitat del vehicle a través de centenars de càmeres.**

______

## Què Significa Realment l'"Anàlisi de Comboi"

Flock Safety comercialitza una funció anomenada **anàlisi de comboi** — la capacitat de seguir múltiples vehicles que viatgen junts com a grup. El llenguatge de màrqueting és neutre. Les implicacions no ho són.

L'anàlisi de comboi significa que Flock pot identificar quan dos o més vehicles específics es mouen junts, correlacionar els seus patrons de viatge al llarg del temps, i marcar quan un grup associat històricament es reuneix de nou. En un context d'aplicació de la llei, això podria significar seguir els organitzadors de protestes que condueixen als mateixos llocs, identificar quins cotxes assisteixen a reunions polítiques, o monitorar persones que es reuneixen regularment al mateix barri.

Cap d'aquestes persones necessita haver fet res il·legal perquè les seves associacions de comboi siguin registrades i emmagatzemades.

La funció té aplicacions legítimes — fer el seguiment dels vehicles d'una organització criminal sospitosa, per exemple. Però la mateixa funció aplicada a una base de dades sense requisit d'ordre judicial significa que es pot utilitzar amb qualsevol persona. És la infraestructura per a la vigilància política, tant si aquesta és la intenció avui com si no.

______

## Què Recullen les Càmeres Flock Més Enllà de les Matrícules

La matrícula és el punt de dades més visible, però no és l'únic. Aquí teniu el que diu l'evidència sobre la recollida de senyals més àmplia per part d'aquestes xarxes de càmeres.

### Detecció d'Adreces MAC de Bluetooth i WiFi

**Això és real, documentat, i freqüentment poc reportat.**

Molts desplegaments ALPR — no només Flock — inclouen capacitat d'escaneig WiFi i Bluetooth. Quan el WiFi o el Bluetooth del vostre telèfon estan activats i no connectats, emet **sol·licituds de sonda** que inclouen l'adreça MAC del vostre dispositiu. Una càmera amb una ràdio WiFi pot registrar passivament aquestes adreces juntament amb la lectura de la matrícula.

Això és enormement important: la vostra adreça MAC està vinculada a *vosaltres*, no al vostre cotxe. Si aneu en el vehicle d'algú altre, llogeu un cotxe o conduïu un cotxe manllevat, el vostre telèfon continua emetent la vostra identitat. L'anàlisi de comboi ara pot incloure les identitats a nivell de dispositiu de tots els passatgers, no només del conductor.

Fins i tot si el desplegament que us preocupa no ho fa actualment, sovint existeix la capacitat de maquinari i programari. La pregunta de quines dades es *recullen* i quines dades es *retenen* són preguntes separades, i auditar el compliment és efectivament impossible sense un requisit públic d'ordre judicial.

### Seguiment de Sensors TPMS

Els **sensors del Sistema de Monitoratge de Pressió dels Pneumàtics (TPMS)** transmeten un identificador únic en freqüències de ràdio UHF. Aquests identificadors no estan xifrats i s'emeten sempre que el pneumàtic roda. Els investigadors han demostrat que els detectors TPMS passius al costat de les carreteres poden registrar identitats de vehicles — i, a diferència de les matrícules, els identificadors TPMS no són visibles per al públic i no es poden canviar sense substituir els sensors.

Un identificador TPMS correspon a un conjunt específic de pneumàtics. Quan aquests pneumàtics estan muntats en un vehicle, l'identificador TPMS és funcionalment equivalent a una matrícula que no sabíeu que teníeu i que no podeu mostrar de manera diferent.

Aquesta no és una capacitat hipotètica futura. Els receptors RTL-SDR que poden registrar senyals TPMS costen al voltant de 40 dòlars. La barrera tècnica per desplegar el monitoratge TPMS passiu juntament amb una xarxa ALPR és molt baixa.

______

## El Problema Real: Fotografia versus Base de Dades

Fer una foto d'un cotxe en un carrer públic és legal. Un agent de policia que anota una matrícula és legal. La càmera de seguretat d'un veí que enregistra el trànsit és legal.

Cap d'aquestes activitats és el mateix que **construir una base de dades centralitzada, cercable i retinguda indefinidament de tots els moviments de vehicles a tota una ciutat**.

El dret legal d'observar espais públics no s'estén automàticament al dret d'agregar aquestes observacions en una infraestructura de vigilància que funciona com una vigilància contínua de 30 dies de cada persona que condueix.

El Tribunal Suprem ha reconegut aquesta distinció. A *Carpenter v. United States* (2018), el Tribunal va dictaminar que, tot i que les dades de torres de telefonia mòbil consisteixen en registres ja proporcionats a un tercer, l'agregació d'aquestes dades al llarg del temps en un registre complet dels moviments d'una persona requereix una ordre judicial. El Tribunal va assenyalar explícitament que el seguiment generalitzat canvia el càlcul constitucional.

Les càmeres de Flock Safety estan fent exactament el que *Carpenter* advertia — a escala, automàticament, sense ordres judicials, sobre tota la població.

______

## Intercanvi de Dades i la Xarxa Nacional Oculta

Les xarxes individuals de càmeres Flock no estan aïllades. Les ciutats i els comtats estableixen **acords d'intercanvi de dades** amb jurisdiccions veïnes, el que significa que una consulta en una ciutat pot obtenir registres de dotzenes d'altres. Alguns d'aquests acords d'intercanvi són prou permissius que una sola agència pot accedir efectivament a una base de dades regional o quasi nacional.

**Així és com una xarxa local de càmeres es converteix en un sistema de vigilància nacional de facto sense que el Congrés mai hi hagi votat.**

L'intercanvi de dades és voluntari i legalment ambigu. No hi ha cap estatut federal que l'autoritzi. No hi ha límits estandarditzats de retenció de dades. No hi ha requisits d'auditoria obligatòria. I no hi ha cap mecanisme perquè un ciutadà pugui esbrinar si els moviments del seu vehicle han estat consultats.

DeFlock.org, que rastreja col·lectivament les ubicacions de les càmeres Flock, ha mapejat més de **124.000 desplegaments LPR sospitosos** arreu dels Estats Units. La cobertura en àrees urbanes i suburbanes és prou densa que conduir per la majoria de les ciutats americanes genera un registre de vigilància gairebé continu.

______

## Càmeres Ring, Flock, i Ordres Judicials

Flock Safety i Amazon Ring són productes diferents, però comparteixen una característica crítica: tots dos poden proporcionar a les forces de l'ordre accés a dades sense requerir una ordre judicial.

Ring va generar una controvèrsia significativa quan es va fer públic que Amazon havia donat imatges a agències de forces de l'ordre milers de vegades — en molts casos sense el coneixement o consentiment del propietari de la càmera. Amazon finalment va canviar algunes de les seves polítiques després de la pressió pública, però el marc legal subjacent no ha canviat.

Flock opera en un model similar. Les càmeres solen ser instal·lades per municipis o associacions de propietaris, però la infraestructura de dades és controlada per una empresa privada. Quan la policia sol·licita dades, les pot obtenir a través de disposicions d'accés d'emergència, portals de forces de l'ordre, o simplement pel fet que l'agència local ja té accés.

**L'absència d'un requisit d'ordre judicial no és un error en aquests sistemes. És el model de negoci.**

Les sol·licituds de registres públics (FOIA als EUA, FOI al Canadà) de vegades poden revelar quines agències han consultat els sistemes Flock, però moltes agències tracten els registres de consultes Flock com a registres d'investigació interna i en deneguen l'accés.

______

## Desmuntant "No Tinc Res a Amagar"

L'argument "res a amagar" és la resposta més comuna a les preocupacions sobre vigilància, i reflecteix una incomprensió genuïna del que és la privadesa.

**La privadesa no és per amagar la culpa. És per preservar l'autonomia.**

Les persones tenen interessos legítims de privadesa en activitats que no són criminals: assistir a reunions polítiques, visitar metges, anar a serveis religiosos, parlar amb periodistes, o simplement conduir on vulguin sense que es faci un registre permanent. El fet que totes aquestes activitats siguin legals no significa que el govern tingui un interès legítim en catalogar-les.

La història ofereix una resposta directa a "res a amagar." Els nord-americans d'origen japonès que van ser internats durant la Segona Guerra Mundial no eren criminals. Els activistes vigilats per COINTELPRO no eren criminals. Les persones en llistes de prohibició de volar que van resultar estar-hi per error burocràtic no eren criminals. Les dades que van permetre aquests abusos es van recollir amb exactament la mateixa lògica — seguretat pública, avaluació d'amenaces, aplicació eficient de la llei.

**La infraestructura de vigilància construïda avui serà utilitzada per qui tingui el poder demà.** La pregunta de si el govern actual és de confiança és irrellevant. La pregunta és si us sentiríeu còmodes que el govern futur més advers imaginable tingués accés a un registre permanent de tots els llocs on heu conduït durant l'última dècada.

______

## Quan el Reconeixement de Matrícules s'Equivoca

Els sistemes ALPR no són perfectament precisos, i les conseqüències d'un error són greus.

Els errors de reconeixement de matrícules cauen en diverses categories:

- **Caràcters mal llegits** — lletres i números que semblen similars amb mala il·luminació o a alta velocitat (0/O, 1/I, 8/B, M/N/H)
- **Lectures parcials** — matrícules brutes, obstruïdes o danyades que només coincideixen parcialment
- **Errors de base de dades** — matrícules marcades com a robades que ja han estat eliminades
- **Col·lisions de matrícules regionals** — dos estats o països poden emetre la mateixa combinació de matrícula, i un encert en una matrícula de Califòrnia pot marcar incorrectament un vehicle d'un estat amb la mateixa cadena alfanumèrica

Els exemples del món real documenten tots aquests casos. Persones han tingut armes apuntant-los durant parades de trànsit perquè el seu vehicle va ser incorrectament associat a un cotxe robat. Persones han rebut factures de peatge de carreteres per les quals mai han conduit. Una persona que conduïa un Hyundai blau cel va rebre una factura de peatge d'una Harley-Davidson conduïda per algú amb una matrícula que diferia en dues lletres.

**La taxa d'errors multiplicada pel volum de lectures produeix un nombre significatiu de persones reals que seran marcades, aturades, registrades o pitjor incorrectament.**

Com que la majoria d'aquestes consultes es fan sense ordres judicials, no hi ha cap control judicial sobre la precisió de les dades subjacents abans de prendre cap acció.

______

## Fallades de Seguretat: MFA i Credencials Compartides

Les pràctiques de seguretat de Flock Safety han estat públicament criticades en múltiples aspectes:

- **Sense autenticació multifactor obligatòria** per als comptes de forces de l'ordre en molts desplegaments
- **Credencials d'inici de sessió compartides** entre múltiples agents en algunes agències
- **Sense temps d'espera de sessió automàtic** en algunes configuracions
- **Sense alertes quan s'accedeix als comptes des de llocs o horaris inusuals**

No són detalls d'implementació menors. Signifiquen que una sola credencial compromesa — obtinguda per phishing, enginyeria social, o simplement la reutilització de contrasenyes — podria donar a un atacant accés per consultar una xarxa Flock regional que cobreixi milions de lectures de matrícules.

Per a les víctimes de violència domèstica, les víctimes d'assetjament, o els periodistes, l'existència d'una base de dades compartida i amb seguretat mínima dels moviments dels seus vehicles no és una preocupació abstracta. És un risc directe per a la seguretat física.

L'argument que "les càmeres són només dades públiques" ignora el requisit de seguretat per a la *capa de base de dades* que agrega aquestes dades. Fins i tot si cada fotografia individual és legal de prendre, la base de dades agregada requereix una protecció més forta que una contrasenya compartida.

______

## Podria Dissenyar-se Millor el Sistema?

**Els controls tècnics sols no són suficients, però val la pena considerar-los.**

S'han discutit diverses propostes per fer que els sistemes ALPR siguin més difícils d'abusar:

**Minimització de dades per disseny**: En lloc d'emmagatzemar imatges completes de matrícules amb marques de temps i coordenades GPS, el sistema podria emmagatzemar un **hash criptogràfic** de la matrícula juntament amb la ubicació i el temps aproximats. Una consulta de les forces de l'ordre confirmaria si una matrícula específica es va veure en una àrea específica en una finestra de temps específica, però no podria recuperar una llista de tots els llocs on s'ha vist aquella matrícula. Això limita la utilitat per a les expedicions de pesca generals tot preservant la capacitat de respondre preguntes d'investigació dirigides.

**Retenció limitada en el temps**: Les matrícules no associades a cap investigació oberta podrien ser eliminades automàticament després de 24-72 hores en lloc de ser retingudes durant 30 dies o més. La majoria dels usos investigatius legítims requereixen dades en temps quasi real. La retenció a llarg termini crea un risc desproporcionat per a les llibertats civils.

**Requisits d'ordre judicial amb revisió judicial**: El control més important és legal en lloc de tècnic. Requerir una ordre judicial per a qualsevol consulta de l'historial de la matrícula d'una persona nomenada no impediria els usos d'emergència (les excepcions de circumstàncies exigents ja existeixen en la llei) però impediria la mineria de dades rutinària sense ordre judicial que actualment no té cap control.

**Registre d'auditoria amb transparència pública**: Cada consulta hauria de ser registrada, aquests registres haurien de ser auditables per organismes de supervisió, i les estadístiques agregades haurien de ser informades públicament.

Aquestes mesures no farien que ALPR fos lliure de riscos, però reduirien dramàticament el potencial d'abús rutinari tot preservant la utilitat investigativa que valoren els defensors.

______

## El Debat No Ha de Ser Tot o Res

La discussió sobre les càmeres Flock sovint es col·lapsa en dues posicions extremes: les càmeres són eines essencials de lluita contra el crim i qualsevol crítica ajuda els criminals, o les càmeres són un estat de vigilància inconstitucional i han de ser eliminades immediatament.

Ambdues posicions són errònies, i la polarització dificulta tenir la conversa que realment importa.

**Les càmeres poden fotografiar carrers públics. Les dades han de ser regulades per la llei.**

La tecnologia no desapareixerà. Les aplicacions legítimes de seguretat pública són reals. Però el model de desplegament actual — en el qual una empresa privada construeix i controla una base de dades de vigilància quasi nacional que les forces de l'ordre poden consultar sense ordre judicial — és constitucionalment sospitós i històricament perillós.

El camí endavant no és destruir les càmeres. És requerir ordres judicials per a cerques individuals, establir finestres curtes de retenció de dades, prohibir l'intercanvi de dades obert sense justificació específica del cas, i crear mecanismes d'auditoria i supervisió aplicables.

Aquesta és una resposta avorrida i procedimental. No genera indignació en cap dels dos bàndols. Però és l'única resposta que pren seriosament tant la seguretat pública com la llibertat constitucional.

______

## Articles Relacionats

| Article | Què Aprendreu |
|---------|------------------|
| **[Vigilància per Càmeres Flock Safety: Prevalença, Preocupacions de Privadesa i Estratègies de Protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Anàlisi completa de la xarxa Flock, casos documentats d'abús i passos pràctics de protecció |
| **[Flock Finder: Mapa de Totes les Càmeres Flock Sospitoses al Vostre Voltant](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Com utilitzar l'eina de codi obert per visualitzar més de 40.000 càmeres sospitoses utilitzant dades WiGLE |
| **[Guia de Maquinari de Detecció Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Construïu o compreu un dispositiu basat en ESP32 per detectar càmeres Flock en temps real |
| **[Com Flashejar Rayhunter en Dispositius de Detecció d'IMSI Catcher](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detecteu stingrays i IMSI catchers — l'equivalent cel·lular del seguiment ALPR |
| **[Comparació de Dispositius Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Trieu el maquinari adequat per a un kit d'eines de contravigilància complet |

______

## Referències

1. [Carpenter v. United States, 585 U.S. 296 (2018)](https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf)
2. [ACLU — Lectors Automàtics de Matrícules](https://www.aclu.org/news/by-issue/automatic-license-plate-readers)
3. [Electronic Frontier Foundation — Què és ALPR?](https://www.eff.org/pages/what-alpr)
4. [DeFlock](https://deflock.org/)
5. [Mapa Interactiu de DeFlock](https://maps.deflock.org/)
6. [Lloc Oficial de Flock Safety](https://www.flocksafety.com/)
7. [Vulnerabilitats de Seguretat i Privadesa de les Xarxes Sense Fil dels Cotxes: Un Estudi de Cas del Sistema de Monitoratge de Pressió dels Pneumàtics](https://www.winlab.rutgers.edu/~gruteser/papers/xu_tpms10.pdf)
8. [FBI Vault — COINTELPRO](https://vault.fbi.gov/cointel-pro)
9. [MuckRock — Flock Safety](https://www.muckrock.com/tags/flock-safety/)
10. [Flock Finder GitHub](https://github.com/simeononsecurity/flock-finder)
11. [Mapa Interactiu de Flock Finder](https://simeononsecurity.github.io/flock-finder/)
