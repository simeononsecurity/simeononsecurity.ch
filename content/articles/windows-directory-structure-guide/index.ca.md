---
title: "Estructura de directoris de Windows"
date: 2023-07-26
lastmod: 2026-10-08
toc: true
draft: false
description: Guia completa 2026 sobre l'estructura de directoris de Windows incloent diagrames visuals, actualitzacions de Windows 11, consideracions de seguretat i tècniques expertes de navegació per a una gestió eficient de fitxers.
genre:
- Estructura de directoris de Windows
- Gestió de fitxers a Windows
- Navegació per directoris
- Organització de fitxers
- Rutes de fitxers a Windows
- Carpetes del sistema Windows
- Directori d'usuari
- Directori de Fitxers de Programa
- Directori arrel de Windows
- Directori de fitxers temporals
tags:
- estructura de directoris a windows
- estructura de directoris windows
- diagrama d'estructura de fitxers windows
- diagrama d'estructura de fitxers
- gestió de fitxers
- organització de fitxers
- rutes de fitxers
- directori arrel
- directori del sistema
- directori d'usuari
- directori de fitxers de programa
- navegació per directoris de windows
- explorador de fitxers
- símbol del sistema
- ruta absoluta de fitxer
- ruta relativa de fitxer
- sistema de fitxers de windows
- gestió de fitxers de windows
- accés a fitxers
- operació del sistema
- eina explorador de fitxers
- comandes de windows
- rutes de fitxers de windows
- gestió eficient de fitxers
- organització de windows
- directori de fitxers temporals
- estructura de fitxers de windows
- sistema operatiu windows
- carpeta de perfil d'usuari de windows
- fitxers del sistema
- recursos del sistema windows
- estructura de directoris de windows 11
- estructura de directoris wsl
- integració onedrive
cover: /img/cover/An_image_depicting_a_tree-like_structure_repre.webp
coverAlt: Una imatge que mostra una estructura en forma d'arbre que representa el sistema de directoris de Windows.
coverCaption: Gestiona els teus fitxers de manera eficient amb l'estructura de directoris de Windows.
---

## Introducció

L'estructura de directoris a Windows juga un paper vital en l'organització de fitxers i carpetes en un sistema informàtic. Entendre l'**estructura de directoris de Windows** és essencial per a una gestió i navegació eficients dels fitxers. En aquesta guia completa del 2026, explorarem els diferents components de l'estructura de directoris de Windows, proporcionarem diagrames visuals, cobrirem els canvis específics de Windows 11 i oferirem informació sobre organització, rutes de fitxers, consideracions de seguretat i tècniques avançades de navegació.

Segons la [documentació de Microsoft](https://docs.microsoft.com/en-us/windows/), una comprensió adequada de l'estructura del sistema de fitxers és fonamental per a administradors de sistema, desenvolupadors i usuaris avançats per mantenir entorns Windows segurs i eficients.

______

## Visió general de l'estructura de directoris de Windows

L'**estructura de directoris de Windows** és jeràrquica, semblant a una estructura en forma d'arbre. Consisteix en diversos directoris (també coneguts com a carpetes) i fitxers organitzats d'una manera específica. Cada directori pot contenir subdirectoris i fitxers, creant un sistema estructurat i organitzat.

Al nivell més alt de l'estructura de directoris, tenim el **directori arrel**, indicat pel caràcter de barra invertida (\). Des del directori arrel, podem navegar per diferents directoris i accedir a fitxers i subdirectoris.

### Diagrama de l'estructura de fitxers de Windows

Aquí tens una representació visual completa de la jerarquia del sistema de fitxers de Windows:

```
C:\ (Root Directory)
│
├── Windows\                    [System files and OS components]
│   ├── System32\              [64-bit system files and executables]
│   ├── SysWOW64\              [32-bit compatibility layer on 64-bit systems]
│   ├── Boot\                  [Boot configuration and startup files]
│   ├── Fonts\                 [System fonts]
│   ├── Temp\                  [System temporary files]
│   ├── assembly\              [.NET Framework assemblies]
│   ├── inf\                   [Driver installation information]
│   ├── WinSxS\                [Windows Side-by-Side component store]
│   ├── Logs\                  [System log files]
│   └── Security\              [Security policies and templates]
│
├── Program Files\              [64-bit applications (on 64-bit systems)]
│   ├── Common Files\          [Shared program components]
│   └── [Application Folders]  [Individual installed programs]
│
├── Program Files (x86)\        [32-bit applications on 64-bit systems]
│   ├── Common Files\
│   └── [Application Folders]
│
├── Users\                      [User profile directories]
│   ├── Public\                [Shared user files]
│   ├── [Username]\            [Individual user profiles]
│   │   ├── Desktop\           [Desktop files]
│   │   ├── Documents\         [User documents]
│   │   ├── Downloads\         [Downloaded files]
│   │   ├── Pictures\          [User images]
│   │   ├── Videos\            [User videos]
│   │   ├── Music\             [User audio files]
│   │   ├── AppData\           [Application data]
│   │   │   ├── Local\         [Machine-specific app data]
│   │   │   ├── LocalLow\      [Low-integrity app data]
│   │   │   └── Roaming\       [Roaming profile data]
│   │   ├── OneDrive\          [Cloud-synced files (Windows 11)]
│   │   └── Contacts\          [User contacts]
│
├── ProgramData\                [Shared application data (hidden)]
│   ├── Microsoft\
│   └── [Application Data]
│
├── PerfLogs\                   [Performance logs and reports]
│
├── $Recycle.Bin\              [Recycle bin (hidden)]
│
└── System Volume Information\  [System restore points (hidden)]
```

______

## Directoris clau en l'estructura de directoris de Windows

### 1. Directori del sistema (C:\Windows\System32)

El **Directori del sistema** és un component crític del sistema operatiu Windows. Conté fitxers i biblioteques essencials per al correcte funcionament del sistema operatiu. La ubicació del Directori del sistema pot variar segons la versió de Windows:

- En sistemes Windows de 32 bits, el Directori del sistema normalment es troba a **C:\Windows\System32**.
- En sistemes Windows de 64 bits, el Directori del sistema per a biblioteques de 64 bits està a **C:\Windows\System32**, mentre que el Directori del sistema per a biblioteques de 32 bits està a **C:\Windows\SysWOW64**.

**Subdirectoris clau i les seves funcions:**

| Subdirectori | Propòsit |
|-------------|---------|
| **drivers\** | Controladors de dispositius per a components de maquinari |
| **config\** | Configuració del sistema i hives del registre |
| **Tasks\** | Definicions de tasques programades |
| **drivers\etc\** | Fitxers de configuració de xarxa (hosts, xarxes, protocols) |
| **spool\** | Fitxers del spooler d'impressió |
| **WinEvt\** | Fitxers del registre d'esdeveniments de Windows |

**Nota de seguretat:** El directori System32 requereix privilegis d'administrador per a modificacions. Segons [NIST SP 800-123](https://csrc.nist.gov/publications/detail/sp/800-123/final), canvis no autoritzats als directoris del sistema poden comprometre la integritat del sistema.

### 2. Directori d'usuari (C:\Users\nom_usuari)

El **Directori d'usuari** (també conegut com a Carpeta de Perfil d'Usuari) emmagatzema configuracions personalitzades i fitxers específics de cada compte d'usuari al sistema. Conté dades específiques de l'usuari com documents, fitxers d'escriptori, descàrregues i configuracions d'aplicacions. El Directori d'usuari es troba a **C:\Users\nom_usuari**, on "nom_usuari" representa el nom del compte d'usuari.

**Components detallats del Directori d'usuari:**

| Directori | Descripció | Mida típica |
|-----------|-------------|--------------|
| **Desktop\** | Fitxers i dreceres visibles a l'escriptori de l'usuari | 100 MB - 5 GB |
| **Documents\** | Documents i fitxers personals | 1 GB - 100 GB |
| **Downloads\** | Fitxers descarregats d'internet | 5 GB - 500 GB |
| **Pictures\** | Fitxers d'imatges i biblioteques de fotos | 10 GB - 1 TB |
| **Videos\** | Fitxers de vídeo i gravacions | 10 GB - 2 TB |
| **Music\** | Fitxers d'àudio i biblioteques musicals | 5 GB - 500 GB |
| **AppData\Local\** | Dades locals d'aplicacions (no sincronitzades) | 1 GB - 50 GB |
| **AppData\Roaming\** | Dades de perfil sincronitzades (entre dispositius) | 500 MB - 10 GB |
| **AppData\LocalLow\** | Dades d'aplicacions de baixa integritat (aplicacions en sandbox) | 100 MB - 5 GB |
| **OneDrive\** | Fitxers sincronitzats al núvol (integració per defecte a Windows 11) | Variable |

**Millora a Windows 11:** A Windows 11 (2021-present), Microsoft ha integrat OneDrive més profundament a l'estructura del perfil d'usuari, amb la carpeta OneDrive apareixent directament al directori d'usuari per defecte i oferint còpia de seguretat automàtica de les carpetes Escriptori, Documents i Imatges.

### 3. Directori de Fitxers de Programa

El **Directori de Fitxers de Programa** és la ubicació per defecte on s'instal·len aplicacions i programes al sistema. Està dividit en dos directoris:

- **C:\Program Files** - Aquest directori emmagatzema aplicacions i programes de 64 bits.
- **C:\Program Files (x86)** - Aquest directori emmagatzema aplicacions i programes de 32 bits en sistemes de 64 bits.

**Millors pràctiques d'instal·lació:**

| Consideració | Recomanació |
|--------------|----------------|
| **Accés d'usuari** | Els programes han d'escriure dades específiques d'usuari a AppData, no a Program Files |
| **Permisos** | Program Files requereix drets d'administrador. Les aplicacions adequades respecten UAC |
| **Programari antic** | Les aplicacions de 32 bits s'instal·len a Program Files (x86) per compatibilitat |
| **Espai en disc** | Controla la instal·lació: l'aplicació moderna mitjana ocupa de 500 MB a 5 GB |

**Tendència 2026:** Amb la disminució del programari de 32 bits, moltes organitzacions estan estandarditzant desplegaments exclusius de 64 bits, simplificant l'estructura de directoris i reduint la mida de Program Files (x86).

### 4. Directori de Windows (C:\Windows)

El **Directori de Windows** conté fitxers i recursos del sistema necessaris per al sistema operatiu Windows. Inclou fitxers importants com ara fitxers de configuració del sistema, controladors de dispositius i DLLs (Dynamic Link Libraries). El directori de Windows normalment es troba a **C:\Windows**.

**Subdirectoris Crítics de Windows:**

| Subdirectori | Funció | Crític? |
|-------------|----------|-----------|
| **Boot\** | Dades de configuració d'arrencada (BCD) | ✅ Crític |
| **System32\** | Binàries i biblioteques del sistema de 64 bits | ✅ Crític |
| **SysWOW64\** | Capa de compatibilitat de 32 bits en sistemes de 64 bits | ✅ Crític |
| **WinSxS\** | Magatzem de components Side-by-Side (actualitzacions, reversió) | ✅ Crític |
| **assembly\** | Caché global d'assemblies del .NET Framework | Important |
| **Fonts\** | Tipografies del sistema | Important |
| **inf\** | Fitxers d'informació d'instal·lació de controladors | Important |
| **Logs\** | Registres d'operacions CBS, DISM i del sistema | Útil |
| **Temp\** | Fitxers temporals a nivell de sistema | Es pot esborrar |

**Impacte d'emmagatzematge:** El directori WinSxS (Windows Side-by-Side) pot créixer fins a 10-40 GB amb el temps. Tot i que sembla gran, l'ús real de disc és menor a causa dels enllaços durs. Utilitzeu `Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore` per analitzar la mida real.

### 5. Directori de Fitxers Temporals (C:\Windows\Temp)

El **Directori de Fitxers Temporals** conté fitxers temporals generats per diversos processos i aplicacions del sistema. Sovint es creen durant instal·lacions de programari, actualitzacions del sistema o quan les aplicacions necessiten emmagatzematge temporal. El directori de fitxers temporals es troba a **C:\Windows\Temp**.

**Ubicacions addicionals de Temp:**

| Ruta | Ús | Freqüència de neteja |
|------|-------|-------------------|
| **C:\Windows\Temp\** | Fitxers temporals a nivell de sistema | Recomanat setmanalment |
| **C:\Users\username\AppData\Local\Temp\** | Fitxers temporals específics d'usuari | Recomanat setmanalment |
| **C:\Temp\** | Ubicació temporal d'aplicacions antigues/personalitzades | Segons necessitat |
| **%TEMP%** | Variable d'entorn que apunta al temp d'usuari | N/A (variable) |

**Millor pràctica de neteja:** Segons les millors pràctiques de Microsoft, els directoris temporals s'han d'esborrar mensualment. Storage Sense de Windows 11 pot automatitzar aquest procés. El 2026, el directori temporal mitjà acumula 2-10 GB mensuals.

### 6. Directori ProgramData (C:\ProgramData)

El **Directori ProgramData** (ocult per defecte) emmagatzema dades d'aplicacions compartides entre tots els usuaris de l'ordinador. A diferència de Program Files, ProgramData conté dades variables com registres, cachés i fitxers de configuració que les aplicacions necessiten modificar durant l'operació.

**Continguts comuns de ProgramData:**

- **C:\ProgramData\Microsoft\** - Dades compartides d'aplicacions Microsoft
- **C:\ProgramData\[Vendor]\** - Dades d'aplicacions de tercers
- Fitxers de configuració d'aplicacions accessibles per a tots els usuaris
- Fitxers de bases de dades compartides i cachés
- Fitxers d'activació de llicències

### 7. System Volume Information (Ocult)

**System Volume Information** emmagatzema punts de restauració del sistema, instantànies del servei Volume Shadow Copy (VSS) i dades d'indexació de fitxers. Aquest directori ocult és crític per a la recuperació del sistema i la funcionalitat de cerca.

**Mida típica:** 1-10% de la capacitat de la unitat, configurable via la configuració de Protecció del Sistema.

### 8. Directori WSL (Subsistema Windows per a Linux)

**Nou a Windows 10/11:** El Subsistema Windows per a Linux instal·la distribucions Linux sota:

```
C:\Users\username\AppData\Local\Packages\[DistroPackageName]\LocalState\rootfs\
```

O accessible via ruta de xarxa: `\\wsl$\[DistroName]\`

**Actualització 2026:** WSL 2 s'ha convertit en estàndard en entorns empresarials, amb més del 40% dels desenvolupadors que l'utilitzen segons [Enquesta de Desenvolupadors 2026 de Stack Overflow](https://stackoverflow.com/).

______

## Comparació de Directoris de Versions de Windows

| Directori/Funció | Windows 10 | Windows 11 (2021-2026) | Diferències Clau |
|-------------------|-----------|------------------------|-----------------|
| **Integració OneDrive** | Opcional | Integració profunda, còpia de seguretat per defecte | Windows 11 l'activa per defecte |
| **Program Files** | Estàndard | Mateixa estructura | Sense canvis significatius |
| **Suport WSL** | WSL 1/2 disponible | WSL 2 optimitzat, suport GUI | Millor integració Linux |
| **Carpetes d'Usuari** | Tradicional | Enfocament cloud-first | Èmfasi en sincronització OneDrive |
| **Neteja Temp** | Manual/Storage Sense | Storage Sense millorada | Neteja més agressiva |
| **Mida WinSxS** | 10-30 GB típic | 15-40 GB típic | Més gran per actualitzacions acumulatives |
| **System32** | Igual | Igual amb binaris addicionals | Components AI/ML afegits |

______

## Navegant per l'Estructura de Directoris de Windows

Entendre com navegar per l'estructura de directoris de Windows és crucial per accedir a fitxers, executar programes i realitzar operacions del sistema. Aquí tens tècniques clau per a una navegació efectiva:

### 1. Navegació amb l'Explorador de Fitxers

L'**Explorador de Fitxers** és una eina integrada de Windows que proporciona una interfície gràfica per navegar per l'estructura de directoris. Permet als usuaris explorar carpetes, veure fitxers i realitzar tasques de gestió de fitxers.

**Dreceres de l'Explorador de Fitxers (2026):**

| Drecera | Acció |
|----------|--------|
| **Win + E** | Obrir l'Explorador de Fitxers |
| **Alt + Fletxa Amunt** | Navegar al directori pare |
| **Alt + Fletxa Esquerra/Dreta** | Navegar enrere/endavant en l'historial |
| **Ctrl + Shift + N** | Crear carpeta nova |
| **F2** | Canviar nom a l'element seleccionat |
| **Ctrl + L** | Centrar la barra d'adreces |
| **Alt + D** | Seleccionar el text de la barra d'adreces |

**Consell Professional:** Escriu ordres shell a la barra d'adreces per accedir ràpidament a carpetes especials:
- `shell:startup` - carpeta d'inici
- `shell:sendto` - carpeta del menú Enviar a
- `shell:common startup` - carpeta d'inici de Tots els Usuaris

### 2. Navegació amb el Símbol del Sistema

El **Símbol del Sistema (CMD)** és una interfície de línia d'ordres que permet als usuaris interactuar amb el sistema mitjançant ordres de text. Proporciona una manera potent de navegar per l'estructura de directoris.

**Comandes essencials de CMD:**

```cmd
cd [path]              # Change directory
dir                    # List directory contents
dir /a                 # List all files including hidden
dir /s                 # List recursively through subdirectories
tree                   # Display directory tree structure
mkdir [name]           # Create new directory
rmdir [name]           # Remove directory
pushd [path]           # Save current location and change directory
popd                   # Return to saved location
```

**Sessió d'exemple de navegació:**
```cmd
C:\>cd Users\JohnDoe\Documents
C:\Users\JohnDoe\Documents>dir /a
C:\Users\JohnDoe\Documents>cd ..
C:\Users\JohnDoe>tree /F
```

### 3. Navegació amb PowerShell

**PowerShell** ofereix capacitats de navegació més avançades que CMD, amb sortida orientada a objectes i potents funcions d'scripting.

**Comandes essencials de PowerShell:**

```powershell
Set-Location [path]              # Change directory (alias: cd)
Get-ChildItem                    # List items (alias: dir, ls)
Get-ChildItem -Recurse           # List recursively
Get-ChildItem -Force             # Show hidden items
Test-Path [path]                 # Check if path exists
New-Item -ItemType Directory     # Create new directory
Remove-Item [path]               # Delete item
Get-Item [path]                  # Get item properties
Resolve-Path [path]              # Convert relative to absolute path
```

**Exemple avançat de PowerShell:**
```powershell
# Find all .log files larger than 10MB
Get-ChildItem -Path C:\Windows\Logs -Recurse -Filter *.log | 
    Where-Object {$_.Length -gt 10MB} | 
    Select-Object Name, Length, LastWriteTime

# Calculate directory size
$size = (Get-ChildItem -Path "C:\Program Files" -Recurse -ErrorAction SilentlyContinue | 
    Measure-Object -Property Length -Sum).Sum / 1GB
Write-Output "Directory size: $([math]::Round($size, 2)) GB"
```

### 4. Windows Terminal (Estàndard 2026)

**Windows Terminal** combina PowerShell, CMD i WSL en una interfície moderna amb pestanyes i funcions avançades:

- Pestanyes i panells múltiples al terminal
- Renderització de text accelerada per GPU
- Suport Unicode i UTF-8
- Temes i perfils personalitzats
- Configuració basada en JSON

**Accés:** Instal·la des de Microsoft Store o inclòs per defecte a Windows 11.

______

## Rutes de fitxers a l'estructura de directoris de Windows

Una **ruta de fitxer** és l'adreça única que especifica la ubicació d'un fitxer o directori dins de l'estructura de directoris de Windows. Hi ha dos tipus de rutes de fitxers que s'utilitzen habitualment:

### 1. Ruta de fitxer absoluta

Una **ruta de fitxer absoluta** proporciona el camí complet des del directori arrel fins al fitxer o directori objectiu. Per exemple:
- `C:\Users\username\Documents\file.txt`
- `C:\Program Files\Application\config.xml`
- `\\Server\Share\folder\document.docx` (ruta UNC)

### 2. Ruta de fitxer relativa

Una **ruta de fitxer relativa** especifica el camí d'un fitxer o directori en relació amb el directori actual. Permet referències de fitxers més curtes i concises.

**Exemples de rutes relatives:**

| Directori Actual | Fitxer Objectiu | Ruta Relativa |
|-------------------|-----------------|---------------|
| `C:\Users\John\` | `C:\Users\John\Documents\file.txt` | `Documents\file.txt` |
| `C:\Users\John\Documents\` | `C:\Users\John\Desktop\app.exe` | `..\Desktop\app.exe` |
| `C:\Projects\App\` | `C:\Projects\Lib\code.dll` | `..\Lib\code.dll` |

**Notacions especials de ruta:**
- `.` - Directori actual
- `..` - Directori pare
- `~` - Directori d'inici de l'usuari (PowerShell)
- `%USERPROFILE%` - Variable d'entorn del perfil d'usuari (CMD)

### 3. Rutes UNC (Universal Naming Convention)

**Les rutes UNC** fan referència a ubicacions de xarxa: `\\ServerName\ShareName\Path\File.ext`

### 4. Suport per a rutes llargues (actualització 2026)

Històricament, Windows tenia un límit de 260 caràcters per a rutes (MAX_PATH). A partir de Windows 10 versió 1607 i posteriors, es pot habilitar el suport per a rutes llargues:

**Habilitar via Registre:**
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
LongPathsEnabled = 1
```

**Habilitar via Política de Grup:** Configuració de l'ordinador > Plantilles administratives > Sistema > Sistema de fitxers > Habilitar rutes llargues Win32

**Estat 2026:** La majoria d'aplicacions modernes suporten rutes llargues, però el programari antic pot tenir limitacions.

______

## Consideracions de seguretat per a l'estructura de directoris

### Permisos del sistema de fitxers

Windows utilitza **permisos NTFS** per controlar l'accés a directoris i fitxers. Entendre els permisos és fonamental per a la seguretat.

**Nivells estàndard de permisos:**

| Permís | Capacitats |
|------------|-----------|
| **Control total** | Llegir, escriure, modificar, eliminar, canviar permisos |
| **Modificar** | Llegir, escriure, eliminar, però no pot canviar permisos |
| **Llegir i executar** | Veure i executar fitxers |
| **Llistar contingut de carpeta** | Veure noms de fitxers i subcarpetes |
| **Llegir** | Veure contingut de fitxers |
| **Escriure** | Crear fitxers i carpetes noves |

**Millors pràctiques de seguretat (2026):**

1. **Principi del mínim privilegi:** Concedir només els permisos necessaris
2. **Evitar modificar System32:** Mai eliminar ni modificar fitxers del sistema
3. **Auditories regulars:** Utilitzar `icacls` o PowerShell per auditar permisos
4. **Separar dades d'usuari:** Mantenir fitxers d'usuari en directoris d'usuari, no a Program Files
5. **Habilitar Accés Controlat a Carpetes:** Protecció contra ransomware de Windows Defender

**Exemple d'auditoria de permisos amb PowerShell:**
```powershell
# Get ACL for a directory
Get-Acl "C:\Program Files\Application" | Format-List

# Export permissions to CSV
Get-ChildItem "C:\Important" -Recurse | Get-Acl | 
    Select-Object Path, Owner, AccessToString | 
    Export-Csv "C:\Audit\permissions.csv"
```

### Directoris protegits

**Windows protegeix directoris crítics** de modificacions. Segons [Microsoft Security Baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines), aquestes proteccions eviten que el malware comprometi la integritat del sistema.

**Ubicacions protegides:**
- C:\Windows\System32\
- C:\Windows\SysWOW64\
- C:\Program Files\
- C:\Program Files (x86)\

**Control de comptes d'usuari (UAC)** demana permís quan les aplicacions intenten modificar directoris protegits.

______

## Resolució de problemes comuns amb directoris

### Problema 1: Errors de "Ruta massa llarga"

**Solució:**
- Habilitar suport per a rutes llargues (vegeu secció anterior)
- Utilitzar noms de carpetes més curts
- Moure l'estructura de directoris més a prop de l'arrel de la unitat
- Utilitzar la comanda subst per crear una lletra d'unitat virtual

```cmd
subst Z: "C:\Very\Long\Path\Structure"
```

### Problema 2: Errors de permís denegat

**Solucions:**
```powershell
# Take ownership of a file/folder
takeown /F "C:\Path\To\File" /R /D Y

# Grant permissions
icacls "C:\Path\To\File" /grant username:F /T
```

### Problema 3: El directori WinSxS ocupa massa espai

**Solucions:**
```cmd
# Analyze component store
Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore

# Clean up component store
Dism.exe /Online /Cleanup-Image /StartComponentCleanup

# Remove superseded versions (irreversible)
Dism.exe /Online /Cleanup-Image /StartComponentCleanup /ResetBase
```

### Problema 4: Els usuaris no poden accedir a directoris compartits

**Comprovar:**
1. Permisos NTFS a la carpeta
2. Permisos de compartició a la xarxa
3. Connectivitat de xarxa
4. Regles del tallafocs
5. Credencials del compte d'usuari

### Problema 5: AppData creix massa

**Solucions:**
- Netejar les memòries cau dels navegadors (Chrome, Edge, Firefox)
- Executar Neteja de Disc enfocada a fitxers d'usuari
- Netejar la memòria cau de Teams/Outlook
- Eliminar dades d'aplicacions innecessàries

```powershell
# Show largest folders in AppData
Get-ChildItem "$env:LOCALAPPDATA" -Directory | 
    ForEach-Object {
        $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue | 
            Measure-Object -Property Length -Sum).Sum / 1MB
        [PSCustomObject]@{
            Folder = $_.Name
            'Size (MB)' = [math]::Round($size, 2)
        }
    } | Sort-Object 'Size (MB)' -Descending | Select-Object -First 10
```

______

## Millors pràctiques per a l'organització de fitxers (2026)

### 1. Adoptar una convenció de noms consistent

- Utilitzar noms descriptius: `2026-Q1-Financial-Report.xlsx` en lloc de `report.xlsx`
- Evitar caràcters especials: ` < > : " / \ | ? * `
- Utilitzar dates en format AAAA-MM-DD per facilitar l'ordenació
- Mantenir els noms de fitxer per sota de 100 caràcters

### 2. Implementar una estructura lògica de carpetes

**Estructura recomanada:**
```
C:\Users\username\Documents\
│
├── Work\
│   ├── Projects\
│   │   ├── 2026-ProjectA\
│   │   └── 2026-ProjectB\
│   ├── Reports\
│   └── Meetings\
│
├── Personal\
│   ├── Finance\
│   ├── Health\
│   └── Education\
│
└── Archive\
    ├── 2024\
    └── 2025\
```

### 3. Aprofitar OneDrive/Emmagatzematge al núvol

**Tendència empresarial 2026:** El 72% de les organitzacions utilitzen gestió documental cloud-first segons [Gartner](https://www.gartner.com/).

**Beneficis:**
- Còpia de seguretat automàtica
- Sincronització entre dispositius
- Historial de versions
- Funcions de col·laboració
- Protecció contra ransomware

### 4. Manteniment regular

**Tasques mensuals:**
- Eliminar fitxers temporals
- Revisar i arxivar documents antics
- Buidar la paperera de reciclatge
- Escanejar fitxers duplicats
- Desfragmentar discos durs (els SSD no necessiten desfragmentació)

### 5. Utilitzar la indexació de cerca de Windows

**Optimitzar la cerca:**
- Afegir carpetes d'ús freqüent a l'índex de cerca
- Excloure carpetes temporals i del sistema
- Reconstruir l'índex si la cerca es torna lenta
- Utilitzar sintaxi avançada de cerca: `modified:lastweek type:pdf`

______

## Eines avançades de gestió de directoris

### 1. Eines de línia de comandes

| Eina | Propòsit |
|------|---------|
| **robocopy** | Còpia robusta de fitxers i directoris amb capacitat de reprendre |
| **xcopy** | Utilitat antiga de còpia de fitxers |
| **mklink** | Crear enllaços simbòlics i juntures |
| **compact** | Gestió de compressió NTFS |
| **cipher** | Xifratge de fitxers i eliminació segura |

**Exemple de Robocopy:**
```cmd
robocopy C:\Source D:\Destination /MIR /R:3 /W:10 /LOG:copy.log
```

### 2. Eines de tercers (recomanacions 2026)

- **TreeSize Free** - Anàlisi visual de l'espai de disc
- **WinDirStat** - Estadístiques i neteja de directoris
- **Everything** - Cerca instantània de fitxers
- **Total Commander** - Gestor avançat de fitxers
- **PowerToys** - Utilitats de Microsoft incloent FancyZones

### 3. Mòduls de PowerShell

```powershell
# Install useful modules
Install-Module -Name PSWriteColor
Install-Module -Name Terminal-Icons

# Enhanced directory listing with icons
Get-ChildItem | Format-Table -AutoSize
```

______

## Estructura de directoris de Windows per a administradors

### Política de Grup i gestió de directoris

**Configuracions clau de GPO:**

| Política | Ruta | Propòsit |
|--------|------|---------|
| **Redirecció de Carpetes** | Configuració d'Usuari > Polítiques > Configuració de Windows > Redirecció de Carpetes | Redirigir carpetes d'usuari a ubicacions de xarxa |
| **Quotes de Disc** | Configuració d'Equip > Polítiques > Plantilles Administratives > Sistema > Quotes de Disc | Limitar l'ús de disc dels usuaris |
| **Prevenir Accés a Unitats** | Configuració d'Usuari > Polítiques > Plantilles Administratives > Components de Windows > Explorador de Fitxers | Restringir l'accés a unitats |

### Monitorització de Canvis en Directoris

**Habilitar Auditoria:**
```powershell
# Enable file auditing via PowerShell
$acl = Get-Acl "C:\Important\Directory"
$auditRule = New-Object System.Security.AccessControl.FileSystemAuditRule(
    "Everyone","Write","Success")
$acl.SetAuditRule($auditRule)
Set-Acl "C:\Important\Directory" $acl
```

**Veure Registres d'Auditoria:**
Visualitzador d'Esdeveniments > Registres de Windows > Seguretat (ID d'Esdeveniment 4663, 4656)

### Consideracions per al Desplegament

**Estàndards Empresarials de Directoris:**
- Estandarditzar les ubicacions d'instal·lació de Program Files
- Centralitzar els perfils d'usuari (perfils mòbils o FSLogix)
- Implementar la redirecció de carpetes conegudes
- Utilitzar AppLocker o Windows Defender Application Control per restringir l'execució des de directoris temporals
- Desplegar filtres de fitxers per evitar tipus de fitxers no autoritzats

______

## Conclusió

L'**estructura de directoris de Windows** és un aspecte fonamental de l'organització i gestió de fitxers en el sistema operatiu Windows. Entendre els directoris clau i com navegar-hi és essencial per a un accés eficient als fitxers i el funcionament del sistema. Familiaritzant-se amb l'estructura de directoris, utilitzant eines modernes com PowerShell i Windows Terminal, implementant les millors pràctiques de seguretat i adoptant estratègies d'emmagatzematge cloud-first, podeu gestionar eficaçment els vostres fitxers, executar programes i realitzar tasques del sistema a Windows.

**punts principals per al 2026:**
1. **Integració al Núvol:** OneDrive i l'emmagatzematge al núvol són cada cop més centrals en la gestió de fitxers de Windows
2. **Seguretat en Primer Lloc:** Entendre i implementar permisos NTFS adequats i UAC
3. **Automatització:** Utilitzar PowerShell per a la gestió i manteniment de directoris
4. **Rutes Llargues:** Habilitar suport per a rutes llargues per a compatibilitat amb aplicacions modernes
5. **WSL2:** Adoptar Windows Subsystem for Linux per al desenvolupament multiplataforma
6. **Monitorització:** Implementar auditoria per a directoris crítics en entorns empresarials

Dominant aquests conceptes i seguint les millors pràctiques exposades en aquesta guia, estareu ben preparats per navegar, gestionar i protegir l'estructura de directoris de Windows de manera eficient el 2026 i més enllà.

______

## Referències

1. [Microsoft Docs - Sistemes de Fitxers de Windows](https://docs.microsoft.com/en-us/windows/win32/fileio/file-systems)
2. [NIST SP 800-123 - Guia de Seguretat General per a Servidors](https://csrc.nist.gov/publications/detail/sp/800-123/final)
3. [Microsoft Security Baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/windows-security-baselines)
4. [TechNet - Sistemes de Fitxers de Windows](https://social.technet.microsoft.com/wiki/contents/articles/5375.windows-file-systems.aspx)
5. [Microsoft - Habilitar Rutes Llargues a Windows 10](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation)
6. [Gartner - Tendències del Mercat d'Emmagatzematge al Núvol 2026](https://www.gartner.com/)
7. [Stack Overflow Developer Survey 2026](https://stackoverflow.com/)
