---
title: "Entendre el filtratge WMI"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Aprèn a utilitzar el filtratge WMI per aplicar els objectes de directiva de grup (GPO) als equips adequats, amb exemples pràctics i bones pràctiques."
genre: ["Administració del Windows", "Directiva de grup", "Administració de sistemes", "Gestió de xarxes", "Infraestructura de TI", "Gestió de polítiques", "Governança de TI", "Automatització de TI", "Active Directory", "Compliment de seguretat"]
tags: ["filtratge WMI", "GPO", "objectes de directiva de grup", "filtres WMI", "selecció de polítiques", "consultes WMI", "Windows Management Instrumentation", "control de GPO", "Consola d'administració de directives de grup", "llenguatge de consultes WMI", "aplicació de polítiques", "WQL", "ajust de polítiques", "gestió de polítiques", "recursos del sistema", "exemples de selecció de polítiques", "administració de sistemes", "gestió de xarxes", "gestió d'infraestructura de TI", "automatització de TI", "administració d'Active Directory", "compliment de seguretat", "tècniques de control de polítiques", "bones pràctiques de gestió de polítiques", "filtratge de polítiques", "estratègies de control de GPO", "seguretat de GPO", "avantatges del filtratge WMI", "implementació del filtratge WMI", "bones pràctiques dels filtres WMI"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Il·lustració d'una lupa enfocada en una icona de filtre, que representa la selecció de GPO amb el filtratge WMI."
coverCaption: "Utilitza el filtratge WMI per adreçar les polítiques GPO de manera eficient."
---

## Introducció

En els objectes de directiva de grup (GPO), el [**filtratge WMI**](https://simeononsecurity.com/github/wmi-filters/) controla quins ordinadors o usuaris reben les polítiques segons els resultats de consultes WMI (Windows Management Instrumentation). Això permet als administradors afinar la selecció i aplicar polítiques només als destinataris previstos. Aquest article explica el filtratge WMI, com funciona amb les GPO, com crear [filtres WMI](https://simeononsecurity.com/github/wmi-filters/) i n'ofereix exemples pràctics.

## [Què és el filtratge WMI?](https://simeononsecurity.com/github/wmi-filters/)

El [**filtratge WMI**](https://simeononsecurity.com/github/wmi-filters/) aplica filtres a les GPO segons els resultats de consultes WMI. WMI és una infraestructura de gestió integrada als sistemes operatius Windows. Permet recuperar dades de gestió i interactuar programàticament amb els recursos del sistema. Amb el filtratge WMI, els administradors poden seleccionar dinàmicament les GPO segons els criteris definits a les consultes.

Els filtres WMI s'escriuen amb el llenguatge de consultes WMI (WQL), un subconjunt de SQL (Structured Query Language). Normalment es basen en propietats i valors disponibles en un espai de noms WMI. Els administradors poden combinar condicions, operadors lògics i espais de noms per crear consultes que seleccionin ordinadors o usuaris específics.

## Com funciona el filtratge WMI a les GPO?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Diagrama de flux que mostra un filtre WMI associat a un objecte de directiva de grup que avalua una consulta WQL com a True o False per decidir si la GPO s'aplica a l'ordinador de destinació" >}}

El **filtratge WMI** permet aplicar GPO de manera selectiva segons l'avaluació de **consultes WMI**. Quan associes un **filtre WMI** a una GPO, el resultat **True** o **False** determina si la GPO s'aplica.

Els filtres utilitzen el **llenguatge de consultes WMI (WQL)**, un subconjunt de SQL. Amb WQL es poden crear consultes complexes que considerin diverses **propietats** i **valors** disponibles en un **espai de noms WMI**. Això permet seleccionar ordinadors o usuaris concrets.

Per exemple, una organització pot voler aplicar una GPO només als ordinadors que executen Windows 10. Pot crear un filtre que comprovi la propietat **OperatingSystem** de la classe **Win32_OperatingSystem**. La consulta WMI podria ser:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

La consulta comprova si la versió del sistema operatiu comença per «10.», cosa que indica Windows 10. Si el resultat és **True**, la GPO s'aplica a l'ordinador de destinació. En cas contrari, no s'aplica.

El filtratge WMI també admet condicions i operadors lògics com **AND**, **OR** i **NOT**. Els administradors poden combinar diverses propietats i valors per controlar millor l'aplicació de les GPO.

També es poden utilitzar diferents **espais de noms WMI** per accedir a conjunts concrets de classes i propietats WMI. Això permet seleccionar GPO segons la configuració del maquinari, el programari instal·lat, els paràmetres de xarxa i altres criteris.

Per obtenir més informació sobre la creació de filtres i consultes WMI, consulta la documentació de Microsoft sobre el [filtratge WMI per a la directiva de grup](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

El filtratge WMI ajuda els administradors a adaptar l'aplicació de GPO a ordinadors o usuaris segons condicions dinàmiques i a gestionar millor l'entorn de TI.

## Crear filtres WMI per a GPO

Per crear un filtre WMI per a una GPO, segueix aquests passos:

1. Obre la **Consola d'administració de directives de grup** (GPMC) en un ordinador Windows unit al domini.

2. Desplega el domini i ves al node **WMI Filters**.

3. Fes clic amb el botó dret a **WMI Filters** i selecciona **New**.

4. Dona un nom descriptiu al filtre i introdueix la consulta WMI al camp **Query**. Fes servir la sintaxi WQL.

5. Fes clic a **OK** per desar el filtre WMI.

Un cop creat, el filtre es pot associar a una o més GPO. Per associar-lo a una GPO:

1. Fes clic amb el botó dret a la GPO desitjada i selecciona **Properties**.

2. A la finestra de propietats de la GPO, obre la pestanya **WMI Filtering**.

3. Selecciona el filtre WMI desitjat de la llista.

4. Fes clic a **OK** per desar els canvis.

Associar filtres WMI a les GPO permet controlar amb precisió on s'apliquen les polítiques segons els resultats de les consultes WMI.

## Quants filtres WMI es poden configurar per a una GPO?

Els administradors poden configurar **diversos filtres WMI** per a una GPO per aconseguir una selecció precisa. No hi ha un límit específic en el nombre de filtres associats a una GPO, així que es poden crear combinacions complexes.

Tot i això, cal tenir en compte l'efecte del nombre de filtres en el temps de processament de les GPO. Com més filtres hi hagi, més temps pot caldre per avaluar i aplicar les GPO. Per mantenir l'eficiència, convé limitar-ne el nombre a una quantitat raonable.

Per exemple, una organització pot voler aplicar una GPO només a ordinadors que executen Windows 10 i tenen instal·lat un programari específic. Pot crear dos filtres WMI separats: un per al **sistema operatiu** i un altre per a la **instal·lació del programari**. Junts seleccionen els ordinadors desitjats.

Cal equilibrar els filtres necessaris per complir els requisits de selecció amb el temps de processament. Abans de decidir quants filtres configurar, avalua la complexitat de l'entorn, el nombre d'ordinadors o usuaris i els possibles efectes en el rendiment.

La possibilitat de configurar diversos filtres WMI ajuda a optimitzar la selecció de GPO i a mantenir eficients el processament i la gestió de l'entorn de TI.

## Exemples pràctics de filtratge WMI a les GPO

El filtratge WMI ofereix solucions pràctiques per aplicar polítiques als destinataris previstos. Aquí tens alguns exemples:

1. **Seleccionar sistemes operatius concrets**: per aplicar una GPO només als ordinadors amb **Windows 10**, crea un filtre que comprovi la versió del sistema operatiu, per exemple `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. Així selecciones els ordinadors Windows 10.

2. **Polítiques diferents per a ordinadors de sobretaula i portàtils**: si necessites polítiques diferents per tipus de dispositiu, utilitza dos filtres WMI. Un pot identificar els ordinadors de sobretaula mitjançant atributs de maquinari, com ara `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, i l'altre pot distingir els portàtils. D'aquesta manera, cada tipus rep les polítiques adequades.

3. **Selecció segons l'espai de disc**: per evitar polítiques que consumeixen molts recursos en ordinadors amb poc espai, crea un filtre que comprovi l'espai lliure. Per exemple, la consulta `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` exclou els ordinadors amb menys de 10 GB lliures.

Aquests exemples mostren la flexibilitat del **filtratge WMI** a les GPO i permeten als administradors seleccionar les polítiques segons criteris específics.

## Conclusió

El filtratge WMI és una funció útil dels objectes de directiva de grup. Permet als administradors aplicar polítiques selectivament segons els resultats de consultes WMI. Els filtres dirigeixen les polítiques a ordinadors o usuaris concrets i fan que la gestió sigui més eficient i controlada. Aquest article ha explicat el concepte, el funcionament a les GPO, la creació de filtres i alguns exemples pràctics.

Si incorpores el filtratge WMI a la gestió de GPO, milloraràs la precisió de l'aplicació de les polítiques i t'asseguraràs que arribin només als destinataris previstos.

## Referències

- [Microsoft Docs: Crear filtres WMI per a la GPO](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Directiva de grup](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Consola d'administració de directives de grup](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
