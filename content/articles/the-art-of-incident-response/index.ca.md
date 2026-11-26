---
title: "L’art de respondre als incidents"
date: 2023-02-19
lastmod: 2026-10-11
toc: true
draft: false
description: "Apreneu les pràctiques recomanades per respondre als incidents segons NIST SP 800-61 Rev. 2 i consulteu exemples reals d’estratègies eficaces."
tags: ["resposta als incidents", "ciberseguretat", "NIST", "pràctiques recomanades", "intel·ligència d’amenaces", "comunicació", "anàlisi posterior a l’incident", "Equifax", "NotPetya", "SolarWinds", "Colonial Pipeline", "Microsoft Exchange Server", "vulnerabilitats", "detecció d’intrusions", "contenció", "recuperació", "preparació", "ciberatacs", "ciberdelicte", "incidents de seguretat"]
cover: "/img/cover/An_illustrated_image_of_a_team_of_cybersecurity_professionals.webp"
coverAlt: "Il·lustració d’un equip de professionals de la ciberseguretat que col·laboren per respondre a un incident de seguretat, amb una icona d’alerta vermella al fons que indica la urgència de la situació. "
coverCaption: ""
---

**L’art de respondre als incidents: pràctiques recomanades i exemples reals**

La resposta als incidents és un component clau de la postura de ciberseguretat d’una organització. Una resposta eficaç ajuda a minimitzar l’impacte dels incidents de seguretat i a reduir el temps de recuperació. El National Institute of Standards and Technology (NIST) ha desenvolupat un marc de resposta als incidents conegut com a NIST SP 800-61 Rev. 2. En aquest article expliquem les pràctiques recomanades que proposa i suggerim algunes millores a l’estàndard.

## Pràctiques recomanades per respondre als incidents

NIST SP 800-61 Rev. 2 ofereix un marc amb quatre fases: preparació, detecció i anàlisi, contenció, eradicació i recuperació. Aquestes són algunes pràctiques recomanades per a cada fase del procés:

### Fase de preparació

- Elaboreu un pla de resposta als incidents que defineixi els rols i les responsabilitats de l’equip, els procediments per informar dels incidents i gestionar-los, i els canals de comunicació amb tercers.
- Formeu l’equip de resposta sobre el pla, inclosos els procediments per detectar incidents, informar-ne i respondre-hi.
- Elaboreu i manteniu una llista dels actius i les dades crítics, amb la ubicació, la propietat i el nivell de sensibilitat de cadascun.

### Fase de detecció i anàlisi

- Superviseu la xarxa i els sistemes per detectar activitat sospitosa i anomalies.
- Feu servir sistemes de detecció i prevenció d’intrusions per detectar i impedir atacs.
- Investigueu l’activitat sospitosa per determinar si és un incident real.

### Fase de contenció

- Aïlleu els sistemes i les xarxes afectats per evitar que l’incident s’estengui.
- Recolliu i preserveu proves per analitzar-les i per a possibles procediments legals.
- Identifiqueu i conteniu la causa arrel de l’incident.

### Fase d’eradicació i recuperació

- Elimineu el programari maliciós o un altre codi nociu dels sistemes afectats.
- Restaureu els sistemes i les dades a partir de còpies de seguretat.
- Apliqueu pegats a les vulnerabilitats que s’hagin explotat durant l’incident.

## Millores de NIST SP 800-61 Rev. 2

{{< figure src="nist-sp-800-61-incident-response-lifecycle-improvements.webp" alt="Diagrama del cicle de resposta als incidents de NIST SP 800-61 Rev. 2 amb millores proposades: integració de la intel·ligència d’amenaces, protocols de comunicació i anàlisi posterior a l’incident" >}}

NIST SP 800-61 Rev. 2 proporciona un marc útil, però hi ha aspectes que es podrien millorar. Aquestes són algunes propostes:

### 1. Integrar la intel·ligència d’amenaces

En un entorn de ciberseguretat que canvia ràpidament, les organitzacions han d’avançar-se als actors d’amenaces. Integrar **intel·ligència d’amenaces** en els processos de resposta és una manera proactiva de detectar, respondre i mitigar incidents de seguretat amb eficàcia.

La intel·ligència d’amenaces consisteix a recollir i analitzar informació sobre les tàctiques, les tècniques i els procediments (TTP) que fan servir els actors d’amenaces. Aquestes dades valuoses provenen de fonts diverses, com ara la **intel·ligència de fonts obertes**, els **fòrums de la web fosca** i els **canals comercials d’intel·ligència d’amenaces**. Amb aquesta informació, les organitzacions poden reforçar la seva capacitat de resposta.

Un dels principals avantatges d’integrar aquesta intel·ligència és poder detectar i prevenir amenaces de manera proactiva. Per exemple, si se sap que un actor fa servir un tipus concret de programari maliciós o d’explotació, l’organització pot identificar i contrarestar l’amenaça abans que causi danys. Estar al corrent dels **indicadors de compromís (IOC)** també permet respondre ràpidament als incidents.

Hi ha diverses maneres d’integrar la intel·ligència d’amenaces en els processos de resposta. Les organitzacions es poden subscriure a **canals comercials d’intel·ligència d’amenaces** amb informació en temps real sobre amenaces i vulnerabilitats conegudes. També poden fer servir **intel·ligència de fonts obertes** per obtenir informació sobre els actors i les seves TTP. Per automatitzar més el procés, les **plataformes d’intel·ligència d’amenaces** simplifiquen la recollida i l’anàlisi d’aquesta informació.

Per exemple, el ciberatac contra la xarxa elèctrica d’Ucraïna el 2015 va demostrar la importància d’aquesta intel·ligència. L’atac, atribuït a l’actor SandWorm, va fer servir programari maliciós personalitzat contra sistemes de control industrial (ICS). SandWorm no era conegut fins aleshores, però els investigadors de ciberseguretat van analitzar l’atac i van identificar **IOC** per detectar i mitigar futurs atacs d’aquest actor.

Integrar intel·ligència d’amenaces també contribueix a millorar la ciberseguretat a llarg termini. En analitzar patrons i tendències, les organitzacions poden detectar vulnerabilitats a la seva infraestructura de seguretat i reforçar les defenses en conseqüència.

Així, la intel·ligència d’amenaces ajuda les organitzacions a defensar-se proactivament de les amenaces emergents, a millorar la detecció i resposta als incidents i a mantenir una postura de ciberseguretat cada vegada millor.
### 2. Destacar la importància de la comunicació

La **comunicació eficaç** és essencial per a una estratègia de resposta als incidents reeixida. Per garantir una resposta cohesionada i coordinada, les organitzacions han d’establir prèviament **canals de comunicació** i procediments que facilitin actualitzacions oportunes i l’intercanvi d’informació entre les parts interessades.

El **pla de resposta als incidents** guia la comunicació durant un incident. Assigna les persones responsables de comunicar-se amb les parts internes i externes, com ara l’**alta direcció**, l’**assessorament jurídic**, les **forces de l’ordre** i els **clients**. Les actualitzacions periòdiques i informatives mantenen les parts interessades al corrent perquè puguin prendre decisions informades i actuar adequadament.

Per exemple, durant un **atac de ransomware**, la comunicació eficaç és clau per coordinar la resposta. La comunicació interna de l’equip distribueix informació actualitzada i manté tothom alineat amb un objectiu comú. La comunicació externa amb l’alta direcció explica l’impacte de l’incident en l’organització i aporta les actualitzacions necessàries. Col·laborar amb les **forces de l’ordre** facilita la notificació de l’incident i l’obtenció d’orientació experta.

El pla també destaca la importància de **documentar** totes les comunicacions relacionades amb l’incident. Els registres de trucades, correus electrònics i altres comunicacions són documents útils. També es documenten les decisions preses durant la resposta, cosa que afavoreix la transparència i la rendició de comptes.

La comunicació eficaç continua després de la resposta, durant l’anàlisi posterior a l’incident. S’informa les parts interessades de les **lliçons apreses** i de les millores previstes per reforçar futures respostes.

Quan el pla prioritza la comunicació, l’organització crea un entorn col·laboratiu on les parts interessades estan informades i participen activament durant tot el procés. Això redueix l’impacte dels incidents i el temps de recuperació, i fa que la postura de seguretat sigui més resilient.

### 3. Oferir orientació per a l’anàlisi posterior a l’incident

L’**anàlisi posterior a l’incident** és un pas clau del cicle de resposta. Permet a les organitzacions aprendre dels incidents i millorar les pràctiques de seguretat. Consisteix a examinar a fons l’incident i la resposta per identificar les **lliçons apreses** i els aspectes que cal millorar.

L’anàlisi ha de començar poc després de resoldre l’incident. L’**equip de resposta** recull les dades pertinents i documenta acuradament l’incident i la resposta. Això inclou crear una cronologia detallada, registrar les mesures preses durant la resposta i preservar totes les comunicacions relacionades.

Un cop recollides les dades inicials, l’equip fa una **anàlisi de la causa arrel** per determinar l’origen de l’incident. Això implica revisar els **registres**, examinar les configuracions dels sistemes i avaluar vulnerabilitats. L’anàlisi revela mancances en el procés de resposta i permet formular recomanacions i millores.

Després, l’equip elabora un **informe posterior a l’incident** que en resumeix els fets, descriu les mesures de resposta, identifica la causa arrel i proposa millores. L’informe s’ha de compartir amb l’**alta direcció**, l’equip de resposta i altres parts interessades pertinents perquè l’organització n’aprengui.

La **filtració de dades d’Equifax** del 2017 és un exemple destacat de la importància d’aquesta anàlisi. Després de la filtració, Equifax va fer una anàlisi aprofundida per identificar lliçons i aspectes que calia millorar. L’anàlisi va remarcar la necessitat de millorar els processos de **gestió de pegats** i els canals de comunicació durant els incidents.

**NIST SP 800-61 Rev. 2** ofereix orientació útil per a l’anàlisi posterior, incloent-hi la identificació de la causa arrel, la documentació de l’incident i la resposta, i les recomanacions de millora. Seguir aquestes pràctiques ajuda a perfeccionar els processos amb el temps.

Una anàlisi posterior completa és fonamental per crear resiliència i millorar la capacitat de resposta. Ajuda les organitzacions a aprendre dels incidents, corregir debilitats i reforçar la postura de seguretat davant incidents futurs.

## Exemples reals de resposta als incidents

### 1. Filtració de dades d’Equifax

El 2017, Equifax va patir una filtració de dades massiva que va afectar més de 143 milions de clients. L’incident va ser causat per una vulnerabilitat dels sistemes informàtics de l’empresa. El pla de resposta d’Equifax era insuficient i la companyia no va detectar la filtració durant diversos mesos. La causa va ser una vulnerabilitat en un paquet de programari de codi obert que Equifax feia servir.

Un cop detectada la filtració, Equifax va prendre mesures per contenir i mitigar l’incident. Va desactivar els sistemes afectats i va contractar una empresa externa de forense digital per investigar-lo. La investigació va concloure que la filtració es devia a no haver aplicat un pegat per a una vulnerabilitat coneguda del paquet de codi obert.

Equifax va corregir i va superar l’incident implantant nous controls de seguretat, oferint monitoratge de crèdit gratuït als clients afectats i pagant milions de dòlars en acords i multes.

### 2. Atac de ransomware NotPetya

El 2017, l’atac de ransomware NotPetya va afectar empreses de tot el món i va causar danys de milers de milions de dòlars. Es va propagar mitjançant una actualització d’un paquet de comptabilitat popular. Va combinar vulnerabilitats conegudes i programari maliciós personalitzat per propagar-se per les xarxes i xifrar dades.

Les organitzacions amb plans de resposta eficaços van poder detectar i contenir ràpidament l’atac. Per exemple, la naviliera Maersk va aïllar els sistemes infectats i va restablir les operacions en pocs dies. Moltes altres organitzacions no estaven preparades i van patir danys importants.

### 3. Atac a la cadena de subministrament de SolarWinds

El 2020, un atac a la cadena de subministrament de SolarWinds, proveïdor de programari, va afectar diversos organismes governamentals i organitzacions privades. Un grup patrocinat per un estat va inserir programari maliciós en una actualització del producte Orion de SolarWinds.

Les organitzacions amb plans eficaços van poder identificar i contenir l’atac ràpidament. Per exemple, l’Agència de Ciberseguretat i Seguretat de les Infraestructures (CISA) del Departament de Seguretat Nacional dels EUA va emetre una directiva d’emergència perquè les agències federals desconnectessin els productes Orion afectats. Les organitzacions privades també van identificar i eliminar sistemes afectats.

### 4. Atac de ransomware a Colonial Pipeline

El maig del 2021, Colonial Pipeline, un operador important de canonades de combustible dels Estats Units, va patir un atac de ransomware que va aturar temporalment la seva infraestructura. L’atac el va dur a terme el grup de ciberdelinqüents DarkSide.

El pla de resposta de Colonial Pipeline li va permetre identificar i contenir ràpidament l’atac. L’empresa va aturar la canonada per precaució, va contractar una empresa externa de forense digital i es va comunicar amb organismes federals i altres parts interessades per coordinar la resposta.

### 5. Vulnerabilitat de Microsoft Exchange Server

A principis del 2021, es van descobrir diverses vulnerabilitats de dia zero a Microsoft Exchange Server, una plataforma popular de correu electrònic i col·laboració. Les vulnerabilitats permetien als atacants accedir a dades sensibles dels sistemes afectats i robar-les.

Les organitzacions amb plans de resposta eficaços van poder identificar i corregir ràpidament les vulnerabilitats. Microsoft va publicar pegats i va recomanar aplicar-los immediatament. Tot i això, moltes organitzacions van trigar a actualitzar els sistemes i van continuar exposades a atacs.

## Conclusió

Els exemples reals **demostren la importància de planificar i preparar bé la resposta als incidents**. Si segueixen les **pràctiques recomanades** i **milloren contínuament els processos de resposta**, les organitzacions estaran **més preparades per respondre als incidents de seguretat** i **protegir els seus actius i dades**. Els casos d’aquest article —la **filtració de dades d’Equifax**, l’**atac de ransomware NotPetya**, l’**atac a la cadena de subministrament de SolarWinds**, l’**atac de ransomware a Colonial Pipeline** i la **vulnerabilitat de Microsoft Exchange Server**— mostren la **naturalesa canviant de les amenaces cibernètiques** i la importància de mantenir una **estratègia de resposta proactiva i eficaç**.
lastmod: 2026-10-11
