---
title: "Dimensiona un SAI per al teu homelab i prova l’apagada automàtica"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Mesura el consum del teu homelab, compara els límits en watts i VA del SAI, comprova l’autonomia amb la teva càrrega i prova una apagada correcta abans de confiar en la bateria."
genre: ["Laboratori domèstic", "Protecció elèctrica", "Administració de sistemes"]
tags: ["SAI per a homelab", "dimensionament del SAI", "autonomia del SAI", "apagada automàtica", "Network UPS Tools", "watts del SAI", "VA del SAI", "factor de potència", "reserva amb bateria", "apagada del servidor", "apagada del NAS", "tall elèctric", "prova del SAI", "corba d’autonomia", "mesurador de potència", "monitoratge del SAI", "canvi de bateria", "protecció contra sobretensions", "apagada ordenada", "energia de l’homelab"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Un SAI de l’homelab alimenta un servidor, un NAS, un encaminador i un commutador sobre una línia temporal des del tall elèctric fins a l’apagada."
coverCaption: "Mesura la càrrega, comprova l’autonomia i prova l’apagada abans que se’n vagi el corrent."
---

Un **SAI**, o sistema d’alimentació ininterrompuda, dona temps a l’homelab per desar la feina i apagar els sistemes durant un tall elèctric. L’etiqueta, per si sola, no indica quant de temps funcionaran els servidors. Necessites la càrrega dels equips, els límits en watts i VA del SAI, una estimació d’autonomia per a aquesta càrrega i un procés d’apagada provat.

## Idees clau

- **Mesura la càrrega:** Anota els watts normals i màxims de cada dispositiu que vulguis mantenir alimentat amb bateria.
- **Comprova tots dos valors:** El SAI ha de satisfer les necessitats en watts i VA dels equips connectats.
- **Consulta la corba d’autonomia:** L’autonomia depèn de la càrrega i de l’estat de la bateria. Fes servir una estimació específica del model.
- **Prova l’aturada:** Comprova que el senyal del SAI arriba a cada amfitrió i que tots s’aturen abans que s’esgoti la bateria.

## Abans de començar

Necessites un mesurador de potència adequat a la xarxa elèctrica local, una llista dels dispositius i adaptadors d’alimentació, i accés a les especificacions i a la corba d’autonomia dels models de SAI que consideres. Per provar l’apagada automàtica també et cal una connexió USB o de gestió de xarxa compatible i programari per a cada amfitrió. Reserva temps per mesurar la càrrega normal, observar una càrrega alta i fer una prova de manteniment planificada. És una tasca intermèdia d’homelab perquè una prova completa d’apagada interromp els serveis.

La [guia de protectors contra sobretensions](/articles/protecting-your-tech_-the-best-surge-protectors/) del lloc tracta la protecció contra sobretensions. El [recull de models de SAI](/articles/best-ups-models-for-uninterrupted-connectivity/) presenta productes. Aquesta guia explica com dimensionar i comprovar la teva càrrega. Tant la [guia de dimensionament de SAI d’Eaton](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html) com la [guia de compra de Schneider Electric](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) distingeixen la potència de sortida de l’autonomia de la bateria.

> **Avís:** Fes servir només les preses i les càrregues que aprovi el fabricant del SAI. Mantén la prova dins de la capacitat nominal del SAI. Una prova real d’apagada atura el laboratori connectat.

## Mesura què ha de continuar encès

Decideix quins dispositius han de funcionar fins a l’apagada. Inclou l’hipervisor, l’emmagatzematge, el commutador de xarxa i l’encaminador si algun amfitrió necessita xarxa per rebre el senyal d’apagada. Deixa els monitors, les impressores i altres càrregues opcionals fora de les preses amb bateria, tret que el teu pla les necessiti.

Mesura a la presa el grup de dispositius previst per funcionar amb bateria. Anota els **watts normals** i el valor més alt observat durant una activitat representativa, com ara arrencar amfitrions o màquines virtuals. L’etiqueta d’una font d’alimentació indica la capacitat, no el consum mesurat del sistema. Tot i això, consulta les etiquetes dels dispositius per veure els límits d’entrada i de corrent d’arrencada. Anota les condicions de mesura al full de treball.

| Dispositiu | Watts normals | Pic observat en watts | Presa amb bateria? |
|---|---:|---:|---|
| **Encaminador i commutador** | 30 | 35 | Sí |
| **NAS** | 60 | 90 | Sí |
| **Servidor petit** | 90 | 135 | Sí |
| **Total il·lustratiu** | **180** | **260** | Tres dispositius |

Els valors anteriors són **il·lustratius**, no mesures d’un laboratori concret. La càrrega canvia segons els discos, les GPU, els ajustos d’alimentació i els equips connectats. Torna-la a mesurar després de canvis importants de maquinari.

## Compara la potència activa amb la potència aparent

Els **watts** descriuen la potència real que fan servir els equips. Els **voltamperes (VA)** descriuen la potència aparent. La relació depèn del **factor de potència**: els watts dividits pel factor de potència donen VA. Eaton ho explica a la seva [guia de dimensionament](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). No interpretis una etiqueta de 1000 VA com si fossin 1000 watts. Comprova la potència en watts específica del SAI.

Per al pic il·lustratiu de 260 W, un marge de capacitat del 25% dona **325 W**. Schneider Electric recomana una potència de sortida aproximadament [entre un 20% i un 25% superior a la càrrega](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Tria un SAI amb una potència contínua en watts superior al pic previst més el marge. Si coneixes el factor de potència combinat, divideix els watts màxims per aquest factor per estimar els VA màxims i aplica també el marge triat als VA. Si no, utilitza un mesurador adequat o el selector del fabricant per determinar els VA necessaris i el marge. No t’inventis un factor de potència si no l’has mesurat.

El marge de capacitat no determina l’autonomia. Un SAI amb un límit alt de watts però una bateria petita pot alimentar la càrrega poca estona. Abans de triar un model, comprova les preses, el tipus d’endoll, la tensió d’entrada, la interfície de comunicació i les opcions de canvi de bateria.

## Fixa un objectiu d’autonomia

Anota quant de temps necessita el laboratori per aturar-se de manera segura. Inclou el temps perquè l’avís d’apagada arribi als amfitrions, s’aturin les màquines virtuals, l’emmagatzematge acabi les escriptures i el SAI talli la sortida. Afegeix marge per a una apagada lenta i una bateria envellida. Un laboratori que ha de resistir talls breus necessita un objectiu diferent d’un que només s’ha d’apagar correctament.

Com a **exemple**, imagina que una apagada provada dura 6 minuts i tries 5 minuts de reserva. Necessites com a mínim 11 minuts d’autonomia amb la càrrega prevista. És un exemple de planificació, no un llindar universal. Compara l’objectiu amb la corba o el selector del model candidat a la teva **càrrega normal i màxima mesurada**, i torna a comprovar el resultat a mesura que envelleix la bateria. El [selector de SAI de Schneider Electric](https://www.se.com/us/en/work/products/tools/ups-selector/) basa l’autonomia en la càrrega introduïda i les especificacions del model. Eaton també remet a dades d’autonomia específiques a la seva [guia de SAI d’escriptori](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Copia aquest **full de treball** per al teu laboratori. Omple les files dels dispositius amb les lectures del mesurador. Suma els watts normals i màxims, afegeix el marge triat al total màxim i aplica el mateix marge als VA màxims mesurats o calculats. Compara tots dos resultats amb un SAI candidat. Si fas servir el selector del fabricant, anota el resultat de dimensionament en VA i el marge. Estima l’autonomia amb la corba del model. Durant la prova, completa les files de temps i recuperació.

| Camp | El teu resultat |
|---|---|
| **Dispositius i preses amb bateria** | Noms dels dispositius i presa assignada a cadascun |
| **Watts normals per dispositiu i total** | Valors mesurats i suma |
| **Watts màxims per dispositiu i total** | Valors més alts observats i suma |
| **Factor de potència mesurat o especificat** | Valor i font, o «desconegut» |
| **VA màxims mesurats o calculats** | Watts màxims dividits pel factor de potència combinat, si el coneixes |
| **Marge de capacitat** | Percentatge triat i watts/VA després del marge |
| **Valors del SAI candidat** | Model, watts i VA de sortida i límits de les preses |
| **Objectiu i estimació de la corba** | Minuts necessaris i estimació del model per a la teva càrrega |
| **Hores d’avís i apagada** | Hora de l’avís de bateria i aturada de l’últim amfitrió |
| **Resultat de recuperació** | Arrencada dels amfitrions, emmagatzematge, aplicacions i monitoratge |

Si desconeixes el factor de potència, fes servir l’eina del fabricant o mesura la potència aparent amb un mesurador adequat. No informis d’un valor VA calculat amb un factor suposat. El full només és complet quan el model compleix els dos límits de sortida i l’autonomia estimada supera l’objectiu d’apagada.

> **Resultat esperat:** El full identifica els dispositius connectats, les càrregues mesurades, els límits en watts i VA del SAI, l’objectiu d’autonomia i l’estimació específica del model.

## Planifica l’apagada automàtica

Un SAI manté els equips encesos temporalment. L’amfitrió encara necessita un **senyal d’apagada**. Comprova si el SAI ofereix USB, una targeta de gestió de xarxa o una altra interfície compatible. Verifica que cada amfitrió que s’ha d’aturar tingui una ruta de monitoratge compatible. Eaton indica que molts models admeten comunicació USB o de xarxa per a una [apagada ordenada d’un NAS o servidor](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

En un laboratori Linux amb **Network UPS Tools (NUT)**, el controlador llegeix el SAI, `upsd` comparteix l’estat i `upsmon` inicia l’apagada de l’amfitrió quan l’alimentació és crítica. Un amfitrió connectat directament a un SAI USB o sèrie normalment executa el controlador, `upsd` i `upsmon` en mode **Primary**. Els altres amfitrions executen `upsmon` en mode **Secondary** contra aquest servidor. Un SAI gestionat per xarxa necessita un controlador compatible i una configuració Primary específica del model. La [guia de topologia de NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) explica aquests rols. Configura l’encaminador i el commutador perquè els amfitrions de monitoratge continuïn connectats amb bateria. Limita l’ordre d’apagada i els permisos als administradors.

Abans de provar l’apagada, comprova que el controlador informa de l’estat actual. Substitueix `myupsname` pel nom del SAI a la configuració de NUT:

```bash
upsc myupsname@localhost ups.status
```

La [guia de configuració de NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) espera `OL` amb alimentació normal de xarxa i explica `OB` per al funcionament amb bateria. Executa la comprovació en cada amfitrió que supervisa el SAI i indica el nom correcte del servidor als clients remots. Una lectura antiga o absent vol dir que cal reparar la ruta del senyal abans de provar l’apagada.

Anota l’**ordre d’apagada**. Per exemple, atura primer les màquines virtuals d’aplicacions, després els clients d’emmagatzematge i finalment l’hipervisor i el NAS. Comprova que cada servei i sistema de fitxers es recupera quan torna el corrent. Una aturada correcta de l’amfitrió sense una recuperació sana de les aplicacions no és un resultat complet.

## Prova sense fer suposicions

Comença amb una **simulació** a l’amfitrió que té configurat el controlador del SAI. NUT documenta `upsdrvctl -t shutdown` com una vista prèvia de la seqüència d’aturada del controlador; no invoca els controladors ni talla l’alimentació:

```bash
upsdrvctl -t shutdown
```

Aquesta **simulació del controlador** no demostra que l’avís d’un tall arribi a cada amfitrió. Revisa tots els serveis de monitoratge i els seus registres. En una finestra de manteniment, la [guia de NUT per provar l’apagada](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) descriu una prova forçada amb `upsmon -c fsd` a l’amfitrió NUT primari. Aquesta **prova FSD** inicia una seqüència real d’apagada. La marca FSD continua activa fins que es reinicia `upsd`. Quan els sistemes tornin, comprova que `upsd` s’hagi reiniciat i que l’estat ja no mostri FSD abans de tornar a confiar en el monitoratge. Llegeix el [manual actual d’upsmon](https://networkupstools.org/docs/man/upsmon.html), prepara una via de recuperació i fes la prova només després de desar la feina i avisar els usuaris del laboratori.

Per a una **prova controlada de l’esdeveniment de bateria**, segueix primer el procediment del fabricant del SAI amb càrregues no crítiques. La prova amb poca càrrega comprova que arriba el senyal, però no demostra l’autonomia del laboratori. Més endavant, durant una finestra de manteniment, prova una càrrega de bateria representativa de la prevista. Algú ha de vigilar el SAI i poder restablir el corrent si el marge disminueix. Anota la càrrega que mostra el SAI, l’hora en què indica que funciona amb bateria, quan comença a apagar-se cada amfitrió i quan s’atura l’últim. Confirma que la bateria no s’esgota abans que s’aturin els amfitrions. Quan torna el corrent, revisa l’arrencada dels amfitrions, l’estat de les aplicacions, la integritat de l’emmagatzematge i el monitoratge. Segons NUT, la seqüència és correcta quan el sistema operatiu s’atura abans que s’acabi la bateria i reprèn el funcionament quan torna el corrent.

| Comprovació | Què cal anotar |
|---|---|
| **Ruta del senyal** | Esdeveniment del SAI visible a cada amfitrió de monitoratge |
| **Temps d’apagada** | L’últim amfitrió s’ha aturat abans d’esgotar la bateria |
| **Recuperació** | Amfitrions, emmagatzematge i aplicacions s’inicien bé |
| **Capacitat** | La càrrega del SAI es manté dins dels límits en watts i VA |

## Resolució de problemes

- **Alarma de sobrecàrrega del SAI:** Treu les càrregues opcionals. Compara la càrrega màxima mesurada amb tots dos límits del SAI i els límits de les preses del model.
- **Autonomia més curta del previst:** Comprova la càrrega actual, l’edat de la bateria, les dades del model i els últims resultats de prova. No extrapolis linealment a partir només dels VA.
- **Un amfitrió continua encès:** Comprova el servei de monitoratge, la ruta de xarxa, els permisos d’apagada i els registres.
- **Els amfitrions s’aturen però no tornen:** Revisa el comportament de la sortida del SAI quan torna el corrent, l’opció del firmware per recuperar l’alimentació i les [consideracions de NUT sobre curses d’alimentació](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **La simulació funciona però la prova de tall falla:** La vista prèvia del controlador comprova una part més limitada. Examina el lliurament de l’esdeveniment i l’ordre real d’apagada.

## Passos següents

Desa el full amb l’inventari de l’homelab. Torna a mesurar la càrrega quan afegeixis maquinari i repeteix la prova d’apagada després de canvis al SAI, al programari de monitoratge, a la política d’arrencada dels amfitrions o a la pila d’emmagatzematge. Revisa per separat el pla de còpia de seguretat i restauració. La bateria protegeix el període d’apagada, mentre que una [còpia de seguretat de l’homelab provada](/articles/what-is-a-homelab-and-should-you-have-one/) protegeix les dades d’altres fallades.
