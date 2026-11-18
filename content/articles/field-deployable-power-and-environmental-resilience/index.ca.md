---
title: "Alimentació i resiliència ambiental per a desplegaments de camp"
date: 2026-08-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Planifica l'alimentació i la protecció ambiental per a la informàtica edge de camp. Aprèn a dimensionar un SAI i a gestionar plaques solars, bateries, sincronització horària, classificacions de protecció, connexió a terra i sobretensions."
genre: ["Informàtica edge", "TI de camp", "Sistemes d'alimentació", "Maquinari", "Recuperació davant desastres", "Informàtica robusta", "Xarxes"]
tags: ["dimensionament del SAI", "alimentació de camp", "alimentació DC per a servidors", "alimentació solar per a servidors", "grau IP de la caixa", "grau NEMA", "protecció contra sobretensions", "connexió a terra d'electrònica", "alimentació de servidors fora de xarxa", "alimentació de centres de dades portàtils", "càlcul d'autonomia de bateria", "alimentació de servidor de 12V", "alimentació DC de 48V", "alimentació informàtica amb generador", "sistema d'alimentació resistent", "alimentació de nodes edge", "alimentació per a recuperació davant desastres", "servidor desplegable de camp", "resiliència ambiental", "alimentació d'expedició", "bateria LiFePO4", "fosfat de ferro i liti", "USB Power Delivery", "comparació de químies de bateria", "Network UPS Tools NUT", "supervisió del SAI amb SNMP", "sincronització horària NTP", "rellotge sincronitzat amb GPS"]
cover: "/img/cover/field-deployable-power-environmental-resilience-solar-ups.webp"
coverAlt: "Il·lustració d'un servidor resistent instal·lat a l'exterior, amb plaques solars que carreguen un banc de bateries i gràfics digitals de gestió de l'energia sobre un fons fosc."
coverCaption: ""
ref: ["/articles/field-deployable-edge-compute-hardware-and-enclosure-selection", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes", "/articles/field-it-tidbits-beyond-the-mini-datacenter", "/articles/the-role-of-ecc-memory-in-mitigating-data-corruption"]
---

**Un servidor desplegat al camp només és tan fiable com la seva font d'alimentació.** La millor caixa i l'ordinador més ràpid no serveixen quan el lloc es queda sense corrent i res no assumeix la càrrega. *La planificació elèctrica forma part del muntatge. És la part amb més probabilitats de fallar primer.*

Aquest és **el segon article d'una sèrie de quatre parts** sobre servidors compactes i equips de xarxa de desplegament ràpid. [La primera part](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) tractava les caixes i la computació. Aquesta part explica com mantenir els equips alimentats i protegits de la calor, la pols, l'aigua i els problemes elèctrics. [La tercera part](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/) tracta la connectivitat i la seguretat de les dades. [La quarta part](/articles/field-it-tidbits-beyond-the-mini-datacenter/) recull els detalls més petits.

______

## Dimensionar un SAI per a ús de camp

Un **SAI (sistema d'alimentació ininterrompuda)** cobreix el període entre una fallada elèctrica i l'aturada dels equips o l'entrada en servei d'una font de reserva. El dimensionament per a ús de camp comença amb un càlcul senzill.

1. Suma la **potència de tots els dispositius** de la caixa, com ara l'ordinador, el commutador, el punt d'accés i l'emmagatzematge.
2. Multiplica el total per **1,5 a 1,6** per deixar marge per al corrent d'arrencada.
3. Divideix la capacitat nominal del SAI en **watt-hora** per la potència total de la càrrega per estimar l'autonomia en hores.

*La capacitat de la bateria disminueix amb l'edat i la temperatura. Considera l'autonomia del fabricant com el millor cas, no com una garantia.* Preveu menys autonomia real, sobretot en entorns càlids, on les bateries perden capacitat més de pressa.

**[Schneider Electric / APC](https://www.apc.com/) publica orientacions detallades sobre el dimensionament dels SAI i el comportament de les bateries.** La seva regla principal també s'aplica a les instal·lacions de camp: connecta el SAI directament a la presa de paret o a la sortida del generador, mai a una regleta amb protecció contra sobretensions. Connecta les preses addicionals que necessitis a una PDU separada després del SAI.

| Tipus de SAI | Adequat per a | Compromís |
|---|---|---|
| **SAI line-interactive** | La majoria de muntatges amb xarxa elèctrica o generador | Temps breu de transferència quan falla el corrent, normalment inferior a 10 ms |
| **SAI en línia de doble conversió** | Equips sensibles amb alimentació inestable o soroll elèctric | Més pesant i car per watt |
| **Bateria DC amb inversor integrat** | Muntatges molt compactes on no hi cap un SAI tradicional | Menys eficiència en convertir de DC a AC i tornar a DC |

## Alimentació DC: prescindeix de l'inversor

Cada conversió d'AC a DC malgasta energia en forma de calor. **Alimentar directament amb DC els equips que ho admeten elimina una etapa de conversió i un punt de fallada.**

- **Els sistemes de 12 V** s'adapten als muntatges petits, com ara ordinadors d'una sola placa, thin clients i commutadors petits. També coincideixen amb la tensió habitual de les bateries d'automòbil i marines.
- **Els sistemes de 48 V** s'adapten als muntatges més grans i coincideixen amb l'estàndard de tensió de les centrals de telecomunicacions. Per això, sovint hi ha equips DC de telecomunicacions de segona mà a baix preu.
- Molts **commutadors de xarxa i punts d'accés** ja accepten PoE o entrada DC. Consulta la fitxa tècnica abans de donar per fet que necessites un inversor.

*Un muntatge natiu en DC funciona més estona amb la mateixa capacitat de bateria que un muntatge AC amb inversor, perquè desapareixen les pèrdues de l'inversor.*

## Alimentació híbrida amb plaques solars i generador

Per a desplegaments més llargs que l'autonomia d'un sol paquet de bateries, combina un banc de bateries amb una font de càrrega.

- **Les plaques solars portàtils amb controlador de càrrega** funcionen bé per carregar durant el dia i consumir bateria a la nit en llocs amb sol fiable.
- **Un generador inverter petit** permet recarregar ràpidament sense dependre del temps, però afegeix la logística del combustible i fa soroll. És un problema seriós en desplegaments discrets o sensibles al soroll.
- **Un muntatge híbrid**, amb l'energia solar com a font principal i el generador com a reserva, cobreix els dies en què el mal temps redueix la producció solar.

*Dimensiona el banc de bateries per a almenys un dia complet d'autonomia sense cap font de càrrega.* Un pla que depèn de sol ininterromput o de subministrament garantit de combustible no és resilient.

{{< figure src="field-power-hybrid-solar-battery-generator.webp" alt="Diagrama on una placa solar i un generador carreguen un banc central de bateries, que alimenta una caixa compacta de servidor mitjançant un bloc de distribució DC i AC" >}}

## Química de les bateries per a ús de camp

No totes les bateries són adequades per a una caixa sotmesa a sacsejades, calor i fred. **La química de la bateria importa tant com els watt-hora indicats a l'etiqueta.**

| Química | Adequada per a | Compromís |
|---|---|---|
| **LiFePO4 (fosfat de ferro i liti)** | La majoria de muntatges de camp, vida útil llarga en cicles i fallada més segura | Més pes per watt-hora que altres químies de liti |
| **Ió de liti (NMC/NCA)** | Muntatges sensibles al pes on cada gram compta | Menys tolerància a la calor i a les descàrregues profundes, vida útil més curta |
| **Plom-àcid segellada (AGM/gel)** | Muntatges de baix cost o solució provisional amb material disponible | Pesant, menys capacitat útil i vida útil més curta de les tres |

**[La comparació de químies de bateries secundàries de Battery University](https://www.batteryuniversity.com/article/bu-107-comparison-table-of-secondary-batteries) explica amb més detall els compromisos entre vida en cicles i energia específica.** *La LiFePO4 destaca perquè tolera la calor, el maltractament i la descàrrega completa molt millor que les altres dues químies, justament el perfil que pot afrontar una caixa de camp.*

La calor perjudica qualsevol química. **[La recerca de Battery University sobre la pèrdua de capacitat de les bateries d'ió de liti](https://www.batteryuniversity.com/article/bu-808b-what-causes-li-ion-to-die) documenta pèrdues reals molt superiors a les dades de laboratori quan hi intervenen la calor i les càrregues ràpides.** Per això, aquesta sèrie recomana preveure una autonomia inferior a la nominal en climes càlids.

## Alimentar dispositius amb USB-C PD

Molts thin clients, punts d'accés i perifèrics d'un muntatge compacte ja accepten alimentació per **USB-C segons l'especificació [USB Power Delivery (USB PD)](https://www.usb.org/document-library/usb-power-delivery)**, cosa que simplifica el kit de camp.

- **Una bateria externa USB PD substitueix diversos adaptadors específics**, i redueix els cables i adaptadors que portes a la caixa.
- **Confirma la potència que negocia el dispositiu en la pràctica**, no només la potència màxima del cable. Una font PD insuficient pot alentir el dispositiu o no carregar-lo sota càrrega sense un avís clar.
- **Porta un cable PD adequat per a la potència màxima del kit.** Un cable econòmic només de càrrega, amb una capacitat de 60 W, limita un dispositiu de 100 W sense cap avís evident.

*USB-C PD no substitueix el dimensionament del SAI i del banc de bateries descrit abans. És una capa pràctica per a perifèrics petits, no l'arquitectura d'alimentació principal de la caixa.*

## Supervisa el SAI en lloc d'endevinar

**Un SAI que ha passat a bateria fa una hora no protegeix res si ningú se n'adona fins que la bateria s'esgota.** La majoria d'unitats comuniquen l'estat per USB o amb una targeta de xarxa. Un muntatge de camp ha de llegir aquest estat.

- **[Network UPS Tools (NUT)](https://networkupstools.org/) és un projecte de codi obert compatible amb més de mil models de SAI** i proporciona eines comunes de supervisió i control, independentment del protocol del fabricant.
- **Activa l'aturada automàtica i ordenada de l'ordinador quan la bateria arribi a un llindar definit.** No deixis que el SAI s'esgoti i talli l'alimentació d'un sistema de fitxers actiu.
- **Registra les tendències de salut i autonomia de la bateria**, no només el percentatge de càrrega actual. Una bateria que perd capacitat a poc a poc no dona cap senyal clar fins que falla.

*Un SAI sense supervisió és una bateria amb una data de caducitat desconeguda.* Configurar NUT o l'eina equivalent del fabricant ocupa una tarda i elimina aquesta incertesa en els desplegaments futurs.

## Sincronització horària sense internet

**L'hora exacta importa més al camp del que molts muntatges preveuen.** Afecta la correlació dels registres, la validesa dels certificats, les connexions de túnels xifrats i qualsevol evidència amb marca de temps que generi el desplegament.

- **Un servidor NTP local dins la caixa**, sincronitzat amb un receptor GPS o una font stratum 1 quan hi ha internet, manté tots els dispositius amb la mateixa hora fins i tot durant les interrupcions de connectivitat.
- **Els rellotges sincronitzats per GPS funcionen sense internet**, cosa important per als escenaris de xarxa mallada i de connexió de reserva per satèl·lit tractats més endavant.
- **Un rellotge desajustat només uns minuts pot impedir la validació dels certificats TLS i les connexions VPN.** Una fallada aparent de xarxa pot ser un problema horari que ningú no comprova.

**L'[especificació NTP versió 4, RFC 5905](https://www.ietf.org/rfc/rfc5905.txt), defineix el protocol que implementa la majoria d'aquestes eines.** La descoberta dinàmica de servidors permet que un petit servidor NTP dins la caixa serveixi tots els altres dispositius amb poca configuració.

## Classificacions ambientals IP i NEMA

Dos sistemes indiquen si una caixa o un dispositiu pot suportar l'entorn previst. **Cap dels dos és sinònim de «resistent». Tots dos fan servir valors específics i comprovables.**

El **[codi IP (Ingress Protection)](https://en.wikipedia.org/wiki/IP_Code)**, definit per la norma IEC 60529, fa servir dos dígits: el primer indica la protecció contra partícules sòlides, com la pols, i el segon contra líquids, com l'aigua.

| Grau IP | Significat |
|---|---|
| **IP54** | Protegit contra la pols i les esquitxades d'aigua des de qualsevol direcció |
| **IP65** | Estanc a la pols i protegit contra dolls d'aigua a baixa pressió |
| **IP67** | Estanc a la pols i protegit contra immersió temporal fins a 1 metre |
| **IP68** | Estanc a la pols i protegit contra immersió contínua a més d'1 metre, segons la profunditat i durada indicades pel fabricant |

El **[sistema NEMA de classificació de caixes](https://en.wikipedia.org/wiki/NEMA_enclosure_types)**, habitual en equips industrials nord-americans, fa servir números de tipus en lloc de parelles de dígits. **NEMA 3R** és adequat per a l'exposició general a la intempèrie. **NEMA 4X** afegeix protecció contra l'aigua i la corrosió per a entorns costaners o de rentat. **NEMA 6P** cobreix la immersió temporal.

*Tria el grau segons l'amenaça real del lloc, no segons el número més alt disponible.* Una caixa IP68 per a un desplegament al desert sense exposició a l'aigua malgasta diners que aprofitaries millor en refrigeració o capacitat de bateria.

## Temperatura, vibració i humitat

A més de la pols i l'aigua, tres factors ambientals fan malbé discretament l'electrònica de camp.

- **Les temperatures extremes** escurcen la vida de les bateries i limiten o apaguen els ordinadors. Consulta el rang de funcionament de cada component, no només el de la caixa.
- **La vibració** afluixa connectors i fatiga les unions de soldadura durant els trajectes repetits. Els suports aïllants de goma entre la safata de computació i la caixa absorbeixen les vibracions abans que arribin al maquinari.
- **La humitat i la condensació** apareixen quan una caixa passa d'un vehicle fred a aire càlid i humit. Amb un canvi gran de temperatura, deixa la caixa tancada uns minuts perquè s'aclimati abans d'obrir-la. Considera posar un petit dessecant dins les caixes segellades.

## Connexió a terra i protecció contra sobretensions

Les fonts d'alimentació de camp, especialment els generadors, són més sorolloses i menys previsibles que la xarxa elèctrica. **En un lloc de camp no hi ha cap electricista de l'edifici per evitar que una sobretensió o una fallada de terra arribi als teus equips.**

- **Estableix una connexió a terra adequada** per a la caixa i els rails metàl·lics abans de connectar l'alimentació. Fes servir una piqueta de terra o la connexió a terra del xassís del vehicle, segons el cas.
- **Fes servir un protector contra sobretensions adequat a la font d'alimentació real**, perquè els generadors poden produir pics diferents dels d'una xarxa neta.
- **Mantén el SAI entre la font d'alimentació bruta i els equips**, no a l'inrevés, perquè la seva protecció contra sobretensions rebi primer l'alimentació més irregular.

*Ometre la connexió a terra per estalviar cinc minuts de muntatge posa en risc tot el maquinari de la caixa.*

## Llista de comprovació d'alimentació i entorn

- [ ] SAI o banc de bateries dimensionat amb un marge d'1,5 a 1,6 sobre la potència total
- [ ] Almenys un dia complet d'autonomia sense font de càrrega
- [ ] Grau IP o NEMA de la caixa ajustat a l'amenaça real del lloc
- [ ] Rang de temperatura comprovat per a cada component, no només per a la caixa
- [ ] Aïllament de vibracions per a transports llargs o fora de carretera
- [ ] Connexió a terra establerta abans de connectar el generador o l'alimentació de camp

## Passos següents

Amb l'alimentació i la protecció ambiental cobertes, la pregunta següent és com es connecta el desplegament amb l'exterior i manté les dades segures. Continua amb [la part tres: connectivitat i seguretat de dades per a nodes edge](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/).

Si encara no l'has llegida, [la primera part: selecció de maquinari i caixa](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) tracta les decisions sobre l'ordinador i la caixa que ha de respectar aquest pla d'alimentació. [La quarta part](/articles/field-it-tidbits-beyond-the-mini-datacenter/) tracta detalls menors que complementen tot l'anterior.
