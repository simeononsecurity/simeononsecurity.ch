---
title: "Consells d’informàtica de camp: més enllà del mini centre de dades"
date: 2026-08-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Guia pràctica d’informàtica de camp sobre recanvis, documentació, ESD, microprogramari, mitjans d’arrencada, llicències, seguretat física, viatges i assegurances."
genre: ["Informàtica de camp", "Informàtica a la perifèria", "Operacions d’IT", "Recuperació davant desastres", "Maquinari", "Bones pràctiques"]
tags: ["kit d’informàtica de camp", "recanvis per a servidors", "bossa d’emergència d’IT", "documentació de camp", "protecció ESD al camp", "gestió del microprogramari", "cables de recanvi", "joc d’eines per a desplegaments d’IT", "seguretat física d’IT", "viatjar amb maquinari de servidor", "controls aeroportuaris i maquinari", "llista de comprovació d’informàtica de camp", "consells per a desplegaments a la perifèria", "kit de recuperació davant desastres", "notes d’informàtica de camp", "adaptador d’alimentació de recanvi", "etiquetadora per a IT", "centre de dades portàtil", "consells d’IT expedicionària", "desplegament ràpid d’IT", "ANSI ESD S20.20", "assegurança d’equipament d’IT", "assegurança cibernètica per a desplegaments de camp", "llicències de programari fora de línia", "verificació de sumes de comprovació del microprogramari", "integritat dels mitjans d’arrencada", "risc del microprogramari a la cadena de subministrament"]
cover: "/img/cover/field-it-deployment-spares-kit.webp"
coverAlt: "Components de recanvi d’IT ordenats, com ara cables Ethernet, cargols, separadors, brides i bosses antiestàtiques, amb una estora portàtil i una polsera al fons."
coverCaption: ""
ref: ["/articles/field-deployable-edge-compute-hardware-and-enclosure-selection", "/articles/field-deployable-power-and-environmental-resilience", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes", "/recommendations/edc", "/articles/cyber-insurance_-what-you-need-to-know-before-you-buy"]
---

**Els problemes que interrompen un desplegament de camp poques vegades són els que algú havia previst.** Un SAI ben dimensionat i una caixa adequada no salvaran la missió si ningú porta un cable Ethernet de recanvi o anota on es guarden les credencials d’administració. *Aquesta quarta i última part reuneix hàbits, equips i lliçons útils més enllà de la informàtica compacta a la perifèria. Una bona disciplina de camp s’aplica a gairebé qualsevol feina pràctica d’IT.*

**Aquesta és la quarta part d’una sèrie de quatre** sobre servidors i equips de xarxa compactes i de desplegament ràpid. [La primera part](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) tractava les caixes i la computació. [La segona part](/articles/field-deployable-power-and-environmental-resilience/) tractava l’alimentació i la protecció ambiental. [La tercera part](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/) tractava la connectivitat i la seguretat.

______

## Prepareu un kit de recanvis

**Un desplegament sense recanvis pot malbaratar un viatge per culpa d’un sol cable avariat.** El kit no ha de ser gran. Ha de cobrir les peces amb més probabilitats de fallar o perdre’s.

- Porteu **un cable de connexió de recanvi de cada llargada utilitzada**. Un cable defectuós és una avaria freqüent i fàcil d’evitar.
- Afegiu **un mòdul SFP de recanvi** si la instal·lació fa servir fibra o transceptors de coure 10G. Són petits, es perden fàcilment i costa substituir-los al camp.
- Porteu **un adaptador d’alimentació o connector de CC de recanvi** per a cada tensió de la caixa.
- Tingueu **un petit assortiment de cargols, separadors i brides**. El cargol que cau dins la caixa a les onze de la nit no es torna a trobar.

*Reompliu el kit just després d’un desplegament, no abans del següent.* Entre «ja ho faré més tard» i el proper viatge és quan desapareix un recanvi.

## Deseu la documentació amb el maquinari

**Un diagrama de xarxa guardat només al portàtil d’algú a l’oficina no ajuda la persona que és davant de la caixa al camp.**

- **Imprimiu una fitxa de referència plastificada** amb adreces IP, la ubicació de les credencials d’administració, mai les credencials mateixes, i un esquema bàsic de resolució de problemes. Fixeu-la a l’interior de la tapa.
- **Etiqueteu cada port i cable** amb la seva connexió. No depengueu només dels colors. Qualsevol persona de l’equip podrà seguir el cable sense trucar-vos.
- **Deseu una còpia en paper de tot el que calgui per iniciar la connectivitat**, com ara la configuració VPN o el procediment inicial per restablir la contrasenya d’administració. Guardeu-la en un lloc independent que no depengui d’una connexió a Internet que ja funcioni.

*Una estratègia documental que pressuposa que la xarxa ja funciona no és un pla d’arrencada. Falla just quan més es necessita.*

## Eviteu l’ESD i manipuleu les peces amb cura

**Les descàrregues electroestàtiques no tenen en compte la pressa ni un terra polsegós utilitzat en lloc d’una estora antiestàtica.** L’aire sec i la roba sintètica augmenten el risc d’ESD al camp respecte d’una oficina climatitzada.

- **Porteu una polsera i una estora antiestàtica portàtil** al kit. Feu-les servir quan canvieu discs o memòria al camp.
- **Toqueu el xassís de la caixa abans de manipular components interns** si no teniu una bona corretja de terra. És la precaució mínima.
- **Deseu els recanvis en bosses antiestàtiques**, no solts en una butxaca de la caixa, encara que sigui per poc temps entre desplegaments.

**Els programes formals de control d’ESD segueixen [ANSI/ESD S20.20](https://www.esda.org/standards/standard-development-process/published-standards/ansiesd-s20-20/), la norma del sector per protegir l’electrònica de les descàrregues electroestàtiques.** Un kit de camp personal no necessita un programa certificat. Les pràctiques bàsiques, com ara la connexió a terra, les polseres i l’embalatge dissipador, també s’adapten a un petit kit de recanvis.

## Controleu el microprogramari i la configuració

**El maquinari de camp és el pitjor lloc per trobar un error de microprogramari o un canvi de configuració no provat.**

- **Actualitzeu i proveu el microprogramari abans del desplegament**, mai al camp, on una actualització fallida pot deixar un dispositiu inservible sense una recuperació fàcil.
- **Deseu una còpia de seguretat de configuració coneguda com a funcional** per a cada dispositiu, fora de la caixa. Així, un restabliment de fàbrica al camp serà una opció de recuperació i no un desastre.
- **Congeleu la configuració quan comenci la missió.** No canvieu paràmetres durant el desplegament, tret que alguna cosa estigui realment espatllada.

{{< figure src="field-it-go-bag-contents-laid-out.webp" alt="Vista superior d’una bossa d’IT de camp oberta amb cables de recanvi etiquetats, tornavisos, polsera ESD, etiquetadora i fitxa de referència plastificada" >}}

## Porteu eines personals

Un kit de desplegament de camp és diferent d’un joc d’eines personal d’ús diari, però s’assemblen més del que sembla. **Un kit personal ben equipat cobreix les mancances habituals del kit compartit de l’equip.**

- **Una eina multiús compacta o un joc petit de tornavisos** serveix per a la fixació estranya per a la qual el kit de l’equip no té la punta adequada.
- **Un frontal o una llanterna petita** és més important al camp que a l’oficina. Els armaris d’equipament i l’interior dels vehicles rarament tenen bona il·luminació.
- **Una bateria portàtil** manté els telèfons i portàtils de comunicació i documentació encesos, independentment de l’alimentació del desplegament.
- La nostra [guia d’equipament diari (EDC)](/recommendations/edc/) tracta eines generals, ganivets, llanternes i bosses útils més enllà de l’IT de camp.

*Això no substitueix el kit de recanvis compartit de l’equip. Cobreix els objectes petits que sovint no entren a la llista oficial.*

## Planifiqueu els viatges i la duana

**Transportar maquinari de xarxa i ordinadors a través de fronteres o controls de seguretat planteja qüestions que no apareixen amb una bossa de portàtil normal.**

- **Consulteu les normes de les companyies aèries i de duanes sobre bateries de liti** abans d’empaquetar bateries d’SAI o bateries externes grans. Molts transportistes limiten els watts hora a l’equipatge facturat i de mà.
- **Porteu un inventari senzill de l’equipament** amb números de sèrie i valors aproximats. Agilitza les declaracions duaneres i les reclamacions a l’assegurança si hi ha pèrdues o danys.
- **Fotografieu la caixa empaquetada abans de cada viatge.** Una foto datada del contingut i l’estat és útil per a l’assegurança i per saber què ha canviat entre desplegaments.
- **Investigueu les restriccions d’importació i exportació de maquinari amb capacitat de xifratge** als països de l’itinerari. Les normes varien i canvien.

## Planifiqueu l’assegurança i les pèrdues

**Una caixa de camp acabarà caient, mullant-se o sent robada. La pregunta és si aquell dia perdreu només el maquinari o també la missió.** Incloeu l’assegurança a la mateixa llista que els cables de recanvi.

- **Confirmeu si l’assegurança empresarial general cobreix l’equipament en trànsit i al camp.** Moltes pòlisses estàndard exclouen els equips fora de l’empresa o limiten el pagament a molt menys que el cost de substitució.
- **L’assegurança cibernètica i l’assegurança d’equipament són pòlisses diferents.** La cibernètica acostuma a cobrir filtracions de dades i resposta a incidents, no la substitució física d’una caixa robada. Considereu totes dues si teniu els dos tipus de risc.
- **Manteniu actualitzat l’inventari de l’equipament i adjunteu-lo a la pòlissa.** Després d’una pèrdua, tindreu els números de sèrie i valors a punt sense haver-los de reconstruir de memòria.

La nostra [guia d’assegurança cibernètica](/articles/cyber-insurance_-what-you-need-to-know-before-you-buy/) explica què sol cobrir una pòlissa i què en queda exclòs. La informació sobre pèrdua de dades també s’aplica a l’IT de camp, tot i que la guia no es va escriure específicament per a aquest cas.

## Gestioneu les llicències fora de línia

**Un servidor de llicències que ha de connectar-se per validar-les esdevé un problema quan el node perd la connexió ascendent.** Les llicències del programari de camp necessiten la mateixa planificació fora de línia que la resta de la sèrie.

- **Activeu els modes de llicència fora de línia i genereu els fitxers d’activació necessaris abans de sortir**, no en arribar a un lloc sense connectivitat.
- **Anoteu les dates de caducitat a la fitxa plastificada esmentada abans.** Una llicència que caduca durant el desplegament equival a una avaria de maquinari.
- **Preferiu eines de codi obert quan compleixin els requisits de la missió.** El programari sense dependència d’un servidor de llicències elimina tota una categoria de problemes de camp.

*Proveu al banc el comportament fora de línia de cada eina amb llicència abans del primer desplegament real.* Descobrir que una eina redueix funcions o bloqueja l’accés sense connexió és una sorpresa desagradable.

## Verifiqueu el microprogramari i els mitjans d’arrencada

**Una imatge de microprogramari o una memòria USB d’arrencada obtinguda d’un enllaç no fiable, o guardada un any sense verificar dins un kit compartit, introdueix riscos de cadena de subministrament a cada desplegament.**

- **Verifiqueu les sumes de comprovació o signatures criptogràfiques de cada imatge de microprogramari i instal·lador del sistema operatiu** abans d’escriure’ls en un mitjà. Compareu el valor amb el publicat al lloc oficial del proveïdor.
- **Deseu les imatges fiables i verificades al mateix kit de recanvis**, no només en un portàtil de l’oficina. La recuperació al camp no dependrà de tornar-les a descarregar.
- **Torneu a verificar periòdicament les sumes de comprovació de les imatges emmagatzemades durant molt temps.** La memòria flaix pot corrompre una imatge sense avisar.

*Una recuperació de camp amb una imatge no verificada pot substituir un problema per un de pitjor.* Verificar una suma de comprovació triga trenta segons i confirma el fitxer abans que arribi al maquinari de producció.

## Eviteu avaries amb hàbits senzills

Alguns hàbits no encaixen exactament en maquinari, energia o connectivitat, però apareixen sovint en les revisions posteriors a desplegaments de camp de tota mena.

- **Proveu tot el kit abans de sortir del taller**, no només cada component per separat. Les peces poden funcionar soles i fallar un cop muntades.
- **Assigneu una persona responsable de la caixa durant el desplegament**, fins i tot en un equip gran. Així res no queda entre dues responsabilitats.
- **Feu una revisió després de cada desplegament** i anoteu què s’ha espatllat, què faltava i què ha anat bé mentre els detalls siguin recents.
- **Canvieu les bateries de recanvi i els consumibles segons un calendari**, no només quan apareguin descarregats. Un recanvi esgotat no és cap recanvi.

*La majoria d’aquests hàbits s’apliquen molt més enllà de l’edge computing. Serveixen per a qualsevol equipament que surti d’un entorn controlat i hagi de funcionar bé en arribar, sense un pla alternatiu.*

## Llista de comprovació d’informàtica de camp

- [ ] Kit de recanvis reposat just després de l’últim desplegament
- [ ] Fitxa plastificada d’arrencada i resolució de problemes fixada dins la tapa
- [ ] Polsera ESD i bosses antiestàtiques incloses i utilitzades a cada intervenció
- [ ] Microprogramari actualitzat i provat abans de sortir, configuració congelada durant la missió
- [ ] Sumes de comprovació del microprogramari i mitjans d’arrencada comparades amb les del proveïdor
- [ ] Llicències de programari activades fora de línia i dates de caducitat anotades
- [ ] Mancances del kit personal cobertes amb eina multiús, llum i bateria independent
- [ ] Capacitat de les bateries en watts hora i inventari duaner revisats abans de creuar una frontera
- [ ] Cobertura de l’assegurança d’equipament confirmada per pèrdues fora de l’empresa i en trànsit
- [ ] Revisió posterior al desplegament completada i arxivada per al viatge següent

## Tancament de la sèrie

Un mini centre de dades desplegable és un sistema, no una sola compra. **Trieu bé la caixa i l’ordinador, protegiu l’alimentació i l’entorn, assegureu la connectivitat i l’accés, i prepareu també els detalls que no apareixen a les especificacions.** Si ometeu un d’aquests quatre pilars, fins i tot un projecte ben finançat pot fallar al camp.

- [Part u: selecció de maquinari i caixa](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/)
- [Part dos: alimentació i resiliència ambiental](/articles/field-deployable-power-and-environmental-resilience/)
- [Part tres: connectivitat i seguretat de dades per a nodes de perifèria](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/)
- [Part quatre: consells d’informàtica de camp més enllà del mini centre de dades](/articles/field-it-tidbits-beyond-the-mini-datacenter/) (aquesta pàgina)

Si el següent pas del kit és muntar un tallafoc pfSense mòbil, la nostra [configuració pfSense 10G econòmica amb HP t740](/guides/budget-friendly-10g-pfsense-build-hp-t740/) ofereix un punt de partida concret i provat. Per triar maquinari de laboratori domèstic útil tant en un banc com en un kit de camp, consulteu [El millor maquinari per a un homelab](/articles/ultimate-tech-homelab-guide/).
