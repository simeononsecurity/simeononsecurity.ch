---
title: "Crea un inventari d’Active Directory de només lectura amb PowerShell"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Fes un inventari de les unitats organitzatives, els usuaris i els ordinadors d’Active Directory amb consultes PowerShell acotades. Exporta fitxers CSV revisables sense modificar els objectes del directori."
genre: ["Active Directory", "PowerShell", "Administració de sistemes"]
tags: ["Inventari d’Active Directory", "Inventari d’AD amb PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "AD de només lectura", "Exportació d’usuaris d’AD", "Exportació d’ordinadors d’AD", "Exportació d’OU d’AD", "Export-Csv", "RSAT", "Auditoria del directori", "Informes d’AD", "Inventari d’OU", "Windows Server", "Script de PowerShell", "Mòdul d’AD", "Higiene del directori"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Arbre d’Active Directory amb registres d’usuaris, ordinadors i unitats organitzatives que desemboquen en tres fitxers de revisió."
coverCaption: "Limita l’abast de la consulta i exporta només els camps necessaris per revisar-la."
---
La neteja d’Active Directory comença amb una llista fiable dels objectes existents. Aquest **inventari de només lectura** recull unitats organitzatives, usuaris i ordinadors d’un abast triat. Exporta tres fitxers CSV (valors separats per comes) per revisar-los sense modificar els objectes del directori. Tot i així, protegeix aquests fitxers, perquè els noms i els detalls dels dispositius revelen part del teu entorn.

<!--more-->

## Idees clau

- **Tria l’abast:** consulta una unitat organitzativa abans d’ampliar la cerca a tot el domini.
- **Fes servir ordres de lectura:** `Get-ADOrganizationalUnit`, `Get-ADUser` i `Get-ADComputer` recuperen objectes.
- **Tria els camps:** exporta només les propietats necessàries per a la tasca.
- **Comprova el resultat:** compara el recompte i algunes files de mostra abans de confiar en l’informe.

## Abans de començar

Necessites un host d’administració Windows amb DNS operatiu i accés de xarxa a un controlador de domini, el mòdul PowerShell **ActiveDirectory**, un compte autoritzat a llegir els objectes triats i una carpeta protegida per als CSV. En un client Windows, el mòdul forma part de les eines d’Active Directory de Remote Server Administration Tools (RSAT). La [guia del mòdul d’Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) n’explica la instal·lació. Microsoft publica la [referència de cmdlets](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) del mòdul i les [opcions d’instal·lació de RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Aquesta guia fa servir la sintaxi de Windows PowerShell i no modifica objectes del directori.

Els permisos del directori continuen vigents. A la [guia sobre comptes privilegiats](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), Microsoft explica que les llistes de control d’accés sovint permeten als usuaris autenticats llegir informació general, però restringeixen els camps sensibles i els canvis. Comença amb un compte aprovat i una OU de prova. No augmentis els permisos a Domain Admin per fer que l’inventari funcioni.

> **Avís:** els fitxers CSV contenen noms de comptes i d’ordinadors. Desa’ls en una ubicació aprovada, limita’n l’accés i elimina les còpies addicionals després de revisar-los. No publiquis una exportació sense filtrar ni l’adjuntis a un issue públic.

## Tria la base de cerca

Una **unitat organitzativa (OU)** agrupa objectes del directori. El seu **nom distingit (DN)** n’indica la posició a l’arbre del directori. El paràmetre `-SearchBase` limita la consulta al DN triat. Sense un abast definit expressament, un filtre ampli pot retornar molts més objectes dels que necessites revisar.

Primer carrega el mòdul i consulta el DN del domini actual:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft documenta [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) i la informació del domini que retorna el cmdlet. Troba l’OU que vols revisar abans de definir la base de cerca:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Copia el DN exacte del resultat. Als exemples següents, substitueix aquest valor de documentació pel DN de la teva OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` és un domini d’exemple per a la documentació. No en copiïs el DN en una consulta real. Si necessites deliberadament un inventari de tot el domini, assigna el DN del domini a `$SearchBase` i registra aquest abast més ampli a l’informe. La [referència de Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) de Microsoft documenta `-Filter` i `-SearchBase`.

## Fes inventari d’OU, usuaris i ordinadors

Comença comptant els objectes. Això ajuda a detectar ràpidament una base de cerca incorrecta o un resultat buit inesperat:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` recupera tots els objectes coincidents dins de la base de cerca. Microsoft documenta [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) i [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) com a ordres de recuperació. Un recompte de zero pot ser correcte, però comprova el DN, els permisos i el domini de destinació abans de considerar complet l’inventari.

Ara previsualitza algunes files a la consola. Desa els camps triats perquè la previsualització i l’exportació CSV posterior facin servir les mateixes columnes:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

En el cas dels ordinadors, demana la propietat addicional del sistema operatiu només si la revisió la necessita:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

El paràmetre `-Properties` demana propietats que no formen part del conjunt predeterminat del cmdlet. Microsoft ho documenta a la [referència del cmdlet d’ordinadors](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer). Tracta els noms de sistema operatiu com a dades del directori, no com a prova de la versió instal·lada actualment. Un objecte d’ordinador pot ser obsolet o potser encara no s’ha actualitzat l’atribut.

## Exporta CSV revisables

Tria una carpeta de sortida aprovada amb prou espai. Les ordres següents escriuen **fitxers CSV locals** i no modifiquen els objectes del directori. Executa-les dins d’aquesta carpeta. `-NoClobber` impedeix sobreescriure fitxers existents. Fes servir una carpeta o un nom de fitxer nou a cada execució.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

La [referència d’Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) de Microsoft explica `-NoTypeInformation`, `-Encoding` i `-NoClobber`. Obre cada CSV en un editor de text o un full de càlcul aprovat. Comprova la capçalera, algunes files i el nombre de registres comparat amb el recompte anterior. Una ordre fallida o un fitxer de zero bytes no demostra que l’informe sigui complet.

> **Resultat esperat:** tens tres fitxers CSV amb registres d’OU, usuaris i ordinadors de l’abast triat. El nombre de files i els valors de mostra coincideixen amb l’abast seleccionat del directori.

## Revisa sense modificar objectes

Fes servir l’inventari per respondre preguntes concretes: quina OU és responsable d’un ordinador? Quins comptes d’usuari estan desactivats? Quins noms de dispositiu necessiten un responsable? Anota les conclusions en una nota de revisió separada. No dedueixis del valor `Enabled` que un compte encara sigui necessari. No eliminis ni desactivis cap objecte basant-te només en una exportació.

En els informes periòdics, registra la data de la consulta, el domini, el DN de l’OU, les propietats triades, l’operador i la ubicació del CSV. Si compares dues exportacions, confirma que fan servir el mateix abast i els mateixos camps. Altrament, la diferència pot venir de la consulta i no d’un canvi real al directori.

Això és un **inventari**, no una auditoria de comptes privilegiats ni un informe d’activitat d’inici de sessió. Microsoft indica que les propietats i els permisos d’Active Directory varien segons l’objecte i l’entorn. Verifica amb el responsable del sistema un atribut de sistema operatiu o un nom de visualització abans d’actuar-hi. La [guia de seguretat d’Active Directory](/articles/active-directory-security-best-practices/) tracta controls més amplis.

## Resolució de problemes

- **El mòdul no s’importa:** confirma que l’host té instal·lades les eines d’Active Directory de RSAT o les eines d’administració de Windows Server. Segueix la [guia de configuració del mòdul](/articles/active-directory-module-powershell-installation-usage-guide/).
- **La consulta no retorna objectes:** comprova el DN exacte, el domini actual, el contingut de l’OU i els permisos de lectura. Prova primer una OU petita coneguda abans d’ampliar l’abast.
- **Una propietat és buida:** confirma que l’atribut existeix i que el teu compte el pot llegir. No omplis els camps absents amb conjectures.
- **L’exportació indica que el fitxer ja existeix:** `-NoClobber` ha protegit l’informe anterior. Tria un nom de fitxer o una carpeta nous i torna a executar l’ordre.
- **El recompte no coincideix amb les expectatives:** comprova si hi ha usuaris o ordinadors en una altra OU, si ha canviat l’abast i si el directori ha canviat durant la consulta.

## Passos següents

Conserva els CSV bruts en una ubicació protegida durant el període de revisió acordat. Comparteix només els camps que necessita el revisor. Quan els responsables confirmin les conclusions, planifica els canvis segons el procediment habitual d’aprovació i reversió. Després dels canvis aprovats, repeteix el mateix inventari amb el mateix abast per confirmar el resultat.