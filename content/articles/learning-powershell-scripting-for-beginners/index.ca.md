---
title: "Scripts amb PowerShell"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "Aprèn els conceptes bàsics dels scripts amb PowerShell i automatitza tasques amb aquesta guia pas a pas per a principiants, que tracta cmdlets, bucles, funcions i molt més."
genre: ["Tecnologia", "Programació", "Automatització", "Windows", "Scripts", "TI", "Tasques administratives", "Gestió d'ordinadors", "Desenvolupament de programari", "Programació"]
tags: ["scripts amb PowerShell", "automatització amb PowerShell", "scripts per a Windows", "cmdlets de PowerShell", "mòduls de PowerShell", "bucles de PowerShell", "condicionals de PowerShell", "funcions de PowerShell", "bones pràctiques de PowerShell", "depuració de PowerShell", "proves de PowerShell", "variables de PowerShell", "PowerShell ISE", "PowerShell Remoting", "tecnologies de Microsoft", "automatització de TI", "gestió d'ordinadors", "programació per a principiants", "tasques administratives", "idees de scripts amb PowerShell", "còpies de seguretat automatitzades", "gestió de fitxers", "informació del sistema", "gestió d'usuaris", "instal·lació de programari", "configuració de xarxa", "automatització de la seguretat", "planificació de tasques", "manipulació del registre", "administració remota"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "Un personatge de dibuixos animats sosté un script davant d'un ordinador amb el símbol del sistema del PowerShell, que mostra com n'és de fàcil aprendre'n els scripts per a principiants"
coverCaption: ""
---
**Aprèn a crear scripts amb PowerShell: guia per a principiants**

PowerShell és un intèrpret d'ordres de línia d'ordres i un llenguatge de scripts desenvolupats per Microsoft. Ofereix una gran varietat d'ordres i funcions per gestionar i automatitzar diversos aspectes del sistema operatiu Windows i altres tecnologies de Microsoft. En aquest article expliquem els conceptes bàsics dels scripts amb PowerShell i oferim una guia pas a pas per començar.

## Introducció al PowerShell

**PowerShell** és un intèrpret d'ordres de línia d'ordres que permet automatitzar i gestionar Windows i altres tecnologies de Microsoft. Inclou un conjunt complet d'ordres i funcions per fer diverses tasques administratives, com ara gestionar fitxers i directoris, configurar la xarxa i administrar el sistema. També admet un llenguatge de scripts amb què es poden crear scripts complexos i automatitzar tasques repetitives.

## Comença a fer servir PowerShell

### Instal·la PowerShell

PowerShell ve preinstal·lat a la majoria de versions de Windows. Si fas servir una versió antiga de Windows o necessites una versió més recent de PowerShell, la pots baixar del lloc web de Microsoft. Per baixar-lo i instal·lar-lo, segueix aquests passos:

1. Ves al [lloc web de Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) i tria la versió que vols instal·lar.
2. Baixa el fitxer d'instal·lació i executa'l.
3. Segueix les instruccions en pantalla per completar la instal·lació.

### Inicia PowerShell

Quan hagis instal·lat PowerShell, inicia'l amb aquests passos:

1. Obre el menú Inici i escriu "PowerShell" al quadre de cerca.
2. Selecciona "Windows PowerShell" als resultats de cerca.
3. PowerShell s'obrirà en una finestra nova.

### Scripts amb PowerShell al Visual Studio Code

Per gaudir d'una experiència de creació de scripts millorada, pots fer servir Visual Studio Code (VS Code), un entorn de desenvolupament integrat (IDE) molt popular. VS Code inclou ressaltat de sintaxi, compleció de codi, depuració i un terminal integrat, unes funcions que el converteixen en una bona opció per crear scripts amb PowerShell. Segueix aquests passos per començar a fer-ho al VS Code:

1. Instal·la Visual Studio Code des del [lloc web oficial](https://code.visualstudio.com/).
2. Instal·la l'extensió "PowerShell" de Microsoft des del mercat d'extensions del VS Code.
3. Obre un fitxer de script del PowerShell (.ps1) al VS Code i comença a programar.

### PowerShell per a l'administració de sistemes

PowerShell és una eina versàtil per a les tasques d'administració de sistemes. Des d'ordres d'una sola línia fins a fluxos d'automatització complexos, simplifica tasques que altrament requeririen intervenció manual. Ofereix una plataforma de scripts unificada per a Windows, Linux i macOS, amb un conjunt d'eines coherent per administrar entorns diferents.

### Del símbol del sistema al Windows PowerShell

Si coneixes el símbol del sistema i vols passar al Windows PowerShell, la transició et pot resultar senzilla. Els scripts del Windows PowerShell parteixen dels conceptes del símbol del sistema i ofereixen capacitats més avançades. Pots aprofitar els coneixements que ja tens i explorar a poc a poc les funcions addicionals i els cmdlets que ofereix PowerShell.

### Conceptes bàsics del PowerShell

PowerShell ofereix una interfície de línia d'ordres per interactuar amb el sistema operatiu. Les seves ordres s'anomenen cmdlets i s'organitzen en mòduls. Per veure els mòduls disponibles, fes servir Get-Module:

```powershell
Get-Module
```

Per veure els cmdlets disponibles en un mòdul, fes servir Get-Command:
```powershell
Get-Command -Module <module name>
```

Per obtenir ajuda sobre un cmdlet, fes servir Get-Help:
```powershell
Get-Help <cmdlet name>
```

PowerShell també admet àlies, que són noms més curts per als cmdlets. Per veure els àlies disponibles, fes servir Get-Alias:
```powershell
Get-Alias
```

## Fitxers de script i política d'execució

Els fitxers de script del PowerShell tenen l'extensió .ps1. Abans d'executar-los, potser hauràs de definir la política d'execució, que determina si es poden executar scripts i quins tipus s'hi permeten. Per definir-la, fes servir el cmdlet Set-ExecutionPolicy. Per exemple, per permetre l'execució de scripts, fes servir:

```powershell
Set-ExecutionPolicy RemoteSigned
```

o (només per fer proves)

```powershell
Set-ExecutionPolicy Undefined
```

### Scripts amb PowerShell

Els scripts amb PowerShell permeten automatitzar diverses tasques administratives. Admeten variables, bucles, condicionals i funcions, de manera que PowerShell és una eina útil per automatitzar tasques.

#### Variables

Les variables emmagatzemen dades als scripts del PowerShell. Els noms de variable comencen amb el signe del dòlar ($). Per assignar un valor a una variable, fes servir aquesta sintaxi:
```powershell
$variable_name = value
```
Per exemple:
```powershell
$name = "John"
```
#### Bucles

Els bucles repeteixen un bloc de codi un nombre determinat de vegades. PowerShell admet aquests tipus de bucle:

- **Bucle For**: repeteix un bloc de codi un nombre concret de vegades.
- **Bucle While**: repeteix un bloc mentre una condició sigui certa.
- **Bucle Do-While**: executa un bloc com a mínim una vegada i després el repeteix mentre una condició sigui certa.
- **Bucle ForEach**: repeteix un bloc per a cada element d'una col·lecció.

Per exemple, el codi següent fa servir un bucle For per mostrar els nombres de l'1 al 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Condicionals

Condicionals

Els condicionals executen un bloc de codi si es compleix una condició. PowerShell admet aquests tipus:

- **Instrucció If**: executa un bloc si es compleix una condició.
- **Instrucció If-Else**: executa un bloc si la condició es compleix i un altre si no es compleix.
- **Instrucció Switch**: compara un valor amb diverses opcions i executa el bloc de la primera coincidència.

Per exemple, el codi següent fa servir If per comprovar si un nombre és superior a 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "El nombre és superior a 5"
}
```
#### Funcions

Les funcions són blocs de codi reutilitzables que fan una tasca concreta. Reben paràmetres d'entrada i retornen valors. PowerShell admet aquests tipus de funció:

- **Bloc de script**: un bloc de codi que es pot executar.
- **Funció avançada**: una funció amb metadades i validació de paràmetres.

Per exemple, el codi següent defineix una funció que suma dos nombres:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "El resultat és $result"
```
### PowerShell ISE

PowerShell ISE (entorn integrat de scripts) és una interfície gràfica per crear scripts amb PowerShell. Inclou un editor de text complet, eines de depuració i altres funcions que faciliten l'escriptura i la prova de scripts. Per obrir-lo, segueix aquests passos:

1. Obre el menú Inici i escriu "PowerShell ISE" al quadre de cerca.
2. Selecciona "Windows PowerShell ISE" als resultats.
3. PowerShell ISE s'obrirà en una finestra nova.

### PowerShell Remoting

PowerShell Remoting permet executar ordres i scripts del PowerShell en ordinadors remots. Cal que el servei WinRM s'executi tant a l'ordinador local com al remot. Per activar PowerShell Remoting, segueix aquests passos:

1. Obre un indicador del PowerShell amb privilegis d'administrador.
2. Executa aquesta ordre per activar PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. Executa aquesta ordre per afegir l'ordinador remot a la llista TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Reinicia el servei WinRM.
```powershell
Restart-Service WinRM
```

Per executar una ordre del PowerShell en un ordinador remot, fes servir el cmdlet Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Mòduls del PowerShell

Els mòduls del PowerShell són col·leccions de cmdlets, funcions i scripts dissenyats per a tasques concretes. Es poden instal·lar i administrar amb PowerShell Gallery, un repositori central de mòduls del PowerShell.

Per instal·lar-hi un mòdul, fes servir aquesta ordre:
```powershell
Install-Module <module name>
```

Per veure els mòduls instal·lats, fes servir Get-InstalledModule:
```powershell
Get-InstalledModule
```

### Bones pràctiques per crear scripts amb PowerShell

Quan escriguis **scripts amb PowerShell**, segueix bones pràctiques perquè siguin **segurs**, **fiables** i **fàcils de mantenir**. Tingues en compte aquestes recomanacions:

- **Fes servir noms de variable descriptius**: tria noms que n'indiquin clarament la finalitat.
- **Afegeix comentaris**: explica la finalitat del codi.
- **Gestiona els errors**: tracta els errors i les excepcions de manera adequada. L'estructura `Try...Catch...Finally` del PowerShell permet gestionar excepcions i prendre les mesures apropiades. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Prova els scripts a fons**: comprova que funcionin com s'espera. Pots fer servir **Pester**, un marc de proves per al PowerShell, per escriure i executar proves unitàries. [Documentació de Pester](https://pester.dev/)
- **Fes servir funcions i mòduls**: organitza el codi i millora'n la reutilització. Les funcions permeten dividir el codi en parts petites i manejables; els mòduls serveixen per empaquetar-lo i distribuir-lo. [Informació sobre les funcions](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [Informació sobre els mòduls](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Evita fixar valors al codi**: fes servir paràmetres o variables perquè els scripts siguin més flexibles i reutilitzables. Passa paràmetres als scripts amb la paraula clau `param`. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Fes servir la sortida detallada**: mostra informació addicional sobre el progrés de l'script amb el cmdlet `Write-Verbose`. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### Desenvolupament de les bones pràctiques per als scripts del PowerShell

#### Gestiona els errors

La gestió d'errors és essencial perquè els scripts puguin tractar errors i excepcions. PowerShell ofereix diverses opcions: les instruccions Try-Catch i Trap, i el paràmetre ErrorAction. Try-Catch captura i gestiona excepcions; Trap captura i gestiona errors; ErrorAction controla com el script respon als errors.

Aquest és un exemple d'ús de Try-Catch per gestionar un error:
```powershell
try {
    # codi que pot generar un error
}
catch {
    Write-Error "S'ha produït un error: $_"
}
```

#### Prova els scripts a fons

És essencial provar els scripts del PowerShell per comprovar que funcionin com s'espera. Eines i marcs com Pester permeten escriure i executar proves, localitzar problemes al codi i comprovar que l'script compleixi els requisits.

Aquest exemple fa servir Pester per provar un script del PowerShell:
```powershell
Describe "El meu script del PowerShell" {
    It "Fa una operació" {
        # codi que hauria de retornar el resultat esperat
        $result = Do-Something
        $result | Should -Be "resultat esperat"
    }
}
```

#### Fes servir funcions i mòduls

Les funcions i els mòduls ajuden a organitzar i reutilitzar el codi. Les funcions agrupen el codi en blocs reutilitzables i els mòduls permeten empaquetar-lo i compartir-lo. Així, els scripts són més modulars, eficients i fàcils de mantenir.

Aquest és un exemple d'ús d'una funció al PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "Hi ha $count processos en execució."
```

#### Evita fixar valors al codi

Els valors fixos redueixen la flexibilitat i dificulten el manteniment d'un script del PowerShell. En comptes d'això, fes servir paràmetres o variables perquè els usuaris puguin introduir valors quan executin l'script. Això facilita la reutilització i l'adaptació a les circumstàncies.

Aquest és un exemple d'ús d'un paràmetre al PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Hola, $name!"
```

#### Fes servir la sortida detallada

La sortida detallada aporta informació sobre el progrés de l'script i pot ajudar a depurar-lo i resoldre problemes. El cmdlet Write-Verbose envia informació detallada a la consola i fa que els scripts siguin més informatius i fàcils de depurar.

Aquest és un exemple de sortida detallada al PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "S'estan obtenint els processos..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "Hi ha $count processos en execució."
```

### Deu idees de scripts del PowerShell per a principiants

Si comences a crear scripts amb PowerShell, prova aquestes deu idees:

- **Còpies de seguretat automatitzades**: crea un script que copiï fitxers i directoris importants a un disc extern o a un servei d'emmagatzematge al núvol. Fes servir `Copy-Item` per copiar fitxers i `Start-Job` per executar la còpia en segon pla. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Gestió de fitxers**: crea un script que organitzi fitxers i directoris en carpetes segons el tipus, la mida o altres criteris. Fes servir `Get-ChildItem` per trobar fitxers i `Move-Item` per moure'ls al lloc desitjat. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Informació del sistema**: crea un script que recuperi dades com l'ús de la CPU i la memòria, l'espai en disc i la configuració de xarxa, i les mostri en un format fàcil de llegir. Fes servir `Get-WmiObject` per obtenir informació i `Format-Table` o `Out-GridView` per donar-li format. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Gestió d'usuaris**: crea un script per afegir, modificar o suprimir usuaris i grups locals de Windows. Fes servir `New-LocalUser`, `Set-LocalUser` i `Remove-LocalUser` per gestionar usuaris, i `New-LocalGroup`, `Add-LocalGroupMember` i `Remove-LocalGroup` per als grups. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Instal·lació de programari**: crea un script que instal·li i configuri programari en diversos ordinadors alhora. Fes servir `Invoke-Command` per executar ordres d'instal·lació als equips remots. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Configuració de xarxa**: crea un script per automatitzar la configuració d'adreces IP, màscares de subxarxa i passarel·les predeterminades. Fes servir `Set-NetIPAddress`, `Set-NetIPInterface` i `Set-DnsClientServerAddress` per configurar la xarxa. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Seguretat**: crea un script que auditi i supervisi la configuració de seguretat i avisi si detecta canvis. Fes servir `Get-AuditPolicy` per obtenir les polítiques d'auditoria i `Send-MailMessage` per enviar notificacions per correu electrònic. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Planificació de tasques**: crea un script per planificar i automatitzar tasques recurrents, com ara còpies de seguretat, actualitzacions i anàlisis del sistema. Fes servir `Register-ScheduledTask` per crear tasques planificades i `Start-ScheduledTask` per executar-les. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Manipulació del registre**: crea un script per modificar o consultar valors de claus concretes del registre. Fes servir `Get-ItemProperty` i `Set-ItemProperty` per interactuar-hi. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Administració remota**: crea un script per activar l'administració remota d'ordinadors Windows i permetre que els usuaris executin ordres i scripts en equips remots. Fes servir `Enter-PSSession` o `Invoke-Command` per executar ordres en equips remots. [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Documentació de Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Explora aquestes idees per adquirir experiència pràctica i ampliar els teus coneixements sobre scripts amb PowerShell.

## Conclusió

PowerShell és una eina potent per gestionar i automatitzar Windows i altres tecnologies de Microsoft. En aquest article hem explicat els conceptes bàsics dels scripts per a principiants: instal·lació i inici, cmdlets, variables, bucles, condicionals i funcions, a més de PowerShell ISE, PowerShell Remoting i els mòduls. Les bones pràctiques ajuden a crear scripts segurs, fiables i fàcils de mantenir. Amb pràctica, podràs dominar PowerShell i automatitzar diverses tasques administratives.
