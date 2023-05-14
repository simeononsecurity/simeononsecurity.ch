---
title: "Optimitzeu les actualitzacions de Windows amb l'automatització mitjançant Chocolatey, PSWindowsUpdate i scripts d'inici"
date: 2020-07-22
---
 Actualitzacions de Windows amb Chocolatey, PSWindowsUpdate i scripts d'inici**

En l'entorn empresarial de ritme ràpid actual, el temps és essencial per als administradors de sistemes. L'actualització de les màquines Windows, un aspecte crític de l'administració de sistemes, pot ser una tasca molt llarga que pot trigar fins a una setmana, tenint en compte prou sistemes. Tanmateix, amb una mica d'ajuda de Chocolatey, PSWindowsUpdates i Startup Scripts, ara és possible implementar actualitzacions amb tan sols un sol reinici de cada màquina, reduint significativament la quantitat de temps necessari per realitzar les actualitzacions.

## Racionalització de les actualitzacions de Windows amb l'automatització

Les actualitzacions de Windows són fonamentals per mantenir l'estabilitat i la seguretat de les màquines Windows. Realitzar actualitzacions en un gran nombre de màquines pot ser una tasca que requereix molt de temps, especialment per als administradors de sistemes amb recursos limitats. Tanmateix, amb l'ús d'eines d'automatització com Chocolatey, PSWindowsUpdate i Scripts d'inici, aquest procés es pot racionalitzar per permetre als administradors realitzar actualitzacions amb el mínim esforç.

### Xocolatada

[Chocolatey](https://chocolatey.org/) és un gestor de paquets per a Windows que es pot utilitzar per automatitzar la instal·lació de programari en màquines Windows. És similar a apt-get a Ubuntu o homebrew a macOS, i es pot utilitzar per instal·lar i gestionar una àmplia gamma de paquets de programari. Chocolatey es pot utilitzar per instal·lar paquets en silenci, el que significa que es poden instal·lar sense la intervenció de l'usuari.

### Actualització de PSWindows

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) és un mòdul de PowerShell que es pot utilitzar per automatitzar la instal·lació d'actualitzacions de Windows. Proporciona cmdlets que es poden utilitzar per instal·lar, desinstal·lar i llistar les actualitzacions de Windows. PSWindowsUpdate és una eina potent que es pot utilitzar per gestionar les actualitzacions de Windows en diverses màquines, la qual cosa la fa ideal per als administradors de sistemes que necessiten gestionar un gran nombre de màquines.

### Scripts d'inici

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) són scripts que es poden utilitzar per automatitzar tasques que s'han de realitzar quan una màquina s'engega o s'apaga. Aquests scripts es poden utilitzar per realitzar tasques com ara instal·lar programari, configurar paràmetres i gestionar les actualitzacions de Windows.

## Automatització de les actualitzacions de Windows amb un sol reinici

Per automatitzar les actualitzacions de Windows mitjançant Chocolatey, PSWindowsUpdate i Scripts d'inici, els administradors poden seguir la guia pas a pas a continuació.

### Configuració de l'script d'apagada
Baixeu tots els fitxers de suport des de[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Obriu l'Editor de polítiques de grup local prement **"Win + R"** i escrivint **"gpedit.msc"** seguit de **"Ctrl + Maj + Retorn"**.
2. Navegueu a Ordinador **Configuració\Configuració de Windows\Scripts (Inici/Apagat)**.
3. Al panell de resultats, feu doble clic a Tanca.
4. Seleccioneu la pestanya PowerShell.
5. Al quadre de diàleg Propietats de tancament, feu clic a Afegeix.
6. Al quadre Nom de l'script, escriviu el camí de l'script o feu clic a Navega per cercar "*chocoautomatewindowsupdates.ps1*" a la carpeta compartida Netlogon del controlador de domini.
7. Reinicieu.

Ara, tot el que ha de fer un administrador és reiniciar l'ordinador per realitzar actualitzacions de Windows.

### Entendre el guió

L'script utilitzat per automatitzar les actualitzacions de Windows es titula "*chocoautomatewindowsupdates.ps1*". Realitza les següents tasques:

1. Instal·la el gestor de paquets Chocolatey.
2. Activa un parell de canvis de configuració preferits de Chocolatey.
3. Actualitza tots els paquets de Chocolatey instal·lats.
4. Instal·la el mòdul PowerShell PSWindowsUpdate.
5. Afegeix el gestor de serveis de Windows Update.
6. Instal·la totes les actualitzacions de Windows disponibles.
7. Instal·la els controladors que faltin o les actualitzacions necessàries per les actualitzacions instal·lades anteriorment.

### Avantatges de l'automatització de les actualitzacions de Windows

L'automatització de les actualitzacions de Windows amb Chocolatey, PSWindowsUpdate i Scripts d'inici té diversos avantatges per als administradors del sistema. Aquests beneficis inclouen:

- **Estalvi de temps**: l'automatització de les actualitzacions de Windows redueix significativament el temps necessari per realitzar les actualitzacions. Els administradors ja no han d'instal·lar manualment les actualitzacions a cada màquina.
- **Coherència**: l'automatització de les actualitzacions de Windows garanteix que les actualitzacions s'instal·lin de manera coherent a totes les màquines. Això redueix la probabilitat d'errors i vulnerabilitats de seguretat.
- **Gestió centralitzada**: l'automatització de les actualitzacions de Windows permet als administradors gestionar les actualitzacions des d'una ubicació central, facilitant el seguiment de quines actualitzacions s'han instal·lat i quines màquines necessiten actualitzacions.
- **Seguretat augmentada**: l'automatització de les actualitzacions de Windows garanteix que les màquines es mantinguin al dia amb els darrers pedaços de seguretat, reduint el risc d'infraccions de seguretat.

### Conclusió

L'automatització de les actualitzacions de Windows amb Chocolatey, PSWindowsUpdate i Scripts d'inici és una eina potent que pot estalviar molt de temps i esforç als administradors del sistema. Permet que les actualitzacions s'instal·lin de manera coherent i eficient, assegurant que les màquines estiguin al dia amb els darrers pedaços de seguretat. Seguint els passos descrits en aquest tutorial, els administradors poden automatitzar les actualitzacions de Windows amb un sol reinici, fent que el procés d'actualització de les màquines Windows sigui molt més ràpid i senzill.
