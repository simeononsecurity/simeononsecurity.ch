---
title: "Bones pràctiques per reforçar la seguretat de Windows 10 i 11"
date: 2023-07-27
lastmod: 2026-11-26
toc: true
draft: false
description: "Descobreix estratègies eficaces per protegir els teus sistemes Windows 10 i Windows 11 amb tècniques de reforç i bones pràctiques completes."
genre: ["Reforç de Windows", "Seguretat de Windows", "Reforç de Windows 10", "Reforç de Windows 11", "Bones pràctiques de seguretat de Windows", "Consells de seguretat de Windows", "Directrius de seguretat de Windows", "Protecció dels sistemes operatius Windows", "Reforç del sistema Windows", "Mesures de seguretat de Windows"]
tags: ["Reforç de Windows", "Seguretat de Windows", "Windows 10", "Windows 11", "Seguretat del sistema operatiu", "Windows Defender", "Control de comptes d'usuari", "Xifratge BitLocker", "Configuració del tallafoc", "Polítiques d'AppLocker", "Actualitzacions de Windows", "Contrasenyes segures", "Còpies de seguretat de dades", "Windows Hello", "Secure Boot", "TPM", "Microsoft Defender Antivirus", "Windows Sandbox", "Microsoft Defender Application Guard", "Accés controlat a carpetes", "Bones pràctiques per protegir Windows 10 i Windows 11", "Com reforçar els sistemes operatius Windows", "Mesures de seguretat de Windows per a persones i organitzacions", "Millora de la seguretat dels sistemes Windows", "Protecció de dades amb el xifratge BitLocker", "Aïllament de sessions del navegador amb Microsoft Defender Application Guard", "Consells i directrius de seguretat per a Windows 10", "Implementació de les funcions de seguretat de Windows", "Protecció de Windows amb aïllament basat en maquinari", "Garantia de la integritat del sistema Windows"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.webp"
coverAlt: "Il·lustració de dibuixos animats d'un escut que protegeix un logotip de Windows de diverses ciberamenaces."
coverCaption: "Protegeix el teu entorn Windows amb tècniques de reforç eficaces."
---

## Introducció

Els sistemes operatius Windows són molt utilitzats per persones i organitzacions d'arreu del món. Per protegir-ne la seguretat i la integritat, aplica les **bones pràctiques de reforç de Windows**. El reforç consisteix a protegir el sistema operatiu reduint-ne la superfície d'atac i mitigant possibles vulnerabilitats. Aquest article repassa les millors pràctiques per reforçar tant **Windows 10** com el més recent **Windows 11**, amb recomanacions útils per millorar la seguretat del teu entorn Windows.

______

## Què és el reforç de Windows

El **reforç** de Windows és el procés d'enfortir la seguretat d'un sistema operatiu Windows. Consisteix a configurar diversos paràmetres i aplicar mesures de seguretat contra l'accés no autoritzat, el programari maliciós i altres amenaces. En reforçar el sistema, redueixes els riscos dels ciberatacs i protegeixes la confidencialitat, la integritat i la disponibilitat de les dades.

### [Reforç de Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

**Windows** 10 és un dels sistemes operatius més utilitzats arreu del món. Per reforçar el teu entorn Windows 10, aplica aquestes bones pràctiques:

#### 1. [**Activa Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender és una **solució antivirus robusta** inclosa amb Windows 10. Ofereix diverses funcions de seguretat per protegir el sistema de diferents tipus de **programari maliciós**, com ara **virus, programari espia i ransomware**. Si actives Windows Defender, milloraràs considerablement la seguretat de l'entorn Windows 10.

Per **activar** Windows Defender, segueix aquests passos:

- Obre l'aplicació **Seguretat de Windows** des de la icona de la barra de tasques o cerca «Seguretat de Windows» al menú Inici.
- A l'aplicació, fes clic a **«Protecció contra virus i amenaces»** al panell de navegació esquerre.
- A la secció **«Configuració de protecció contra virus i amenaces»**, fes clic a **«Administra la configuració»**.
- Comprova que el commutador de **«Protecció en temps real»** estigui **activat**. Així Windows Defender podrà analitzar i protegir activament el sistema en temps real.
- També pots personalitzar les opcions d'anàlisi i les exclusions amb **«Opcions d'anàlisi»** i **«Afegeix o suprimeix exclusions»**.

**Actualitza Windows Defender periòdicament** perquè disposi de les definicions de **programari maliciós** més recents i de les millores de seguretat. Microsoft publica actualitzacions periòdiques per afrontar noves amenaces i vulnerabilitats. Per actualitzar-lo, segueix aquests passos:

- **Obre** l'aplicació Seguretat de Windows.
- Ves a **«Protecció contra virus i amenaces»** al panell de navegació esquerre.
- A la secció **«Actualitzacions de protecció contra virus i amenaces»**, fes clic a **«Cerca actualitzacions»**.
- **Windows** cercarà les actualitzacions disponibles i les baixarà i instal·larà si cal.

Si actives Windows Defender i el mantens actualitzat, protegiràs de manera proactiva el sistema Windows 10 contra el programari maliciós i altres amenaces. També convé fer **anàlisis periòdiques del sistema** per detectar i eliminar possibles amenaces.

Windows Defender ofereix una bona protecció, però complementa-la amb **hàbits de navegació segurs**, actualitzacions regulars del programari i altres mesures de seguretat.

#### 2. [**Mantén Windows 10 actualitzat**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)

**Instal·lar** les **actualitzacions** de Windows periòdicament és essencial per **reforçar Windows 10**. Inclouen **pegats de seguretat**, correccions d'errors i millores de rendiment que ajuden a **corregir vulnerabilitats de seguretat** i a estabilitzar el sistema.

Microsoft publica **actualitzacions regulars** per resoldre problemes de seguretat descoberts recentment i millorar l'experiència d'ús. Si mantens el sistema actualitzat, tindràs les **millores de seguretat** més recents per defensar-te de les amenaces emergents.

Per **mantenir** Windows 10 actualitzat, segueix aquests passos:

1. **Activa les actualitzacions automàtiques**: per defecte, Windows 10 baixa i instal·la les actualitzacions automàticament. Així el sistema rep les actualitzacions necessàries sense intervenció manual. Per comprovar-ho:
   - Obre **Configuració** des del menú Inici amb la icona de l'engranatge.
   - Fes clic a **Actualització i seguretat**.
   - Al panell esquerre, fes clic a **Windows Update**.
   - Comprova que l'opció **«Automàtic»** estigui seleccionada a la configuració de Windows Update. Si no ho està, fes clic a **«Canvia les hores actives»** per triar quan Windows ha d'evitar instal·lar actualitzacions.

2. **Instal·la les actualitzacions manualment**: si vols controlar el procés, pots instal·lar-les tu mateix:
   - Ves a **Configuració > Actualització i seguretat > Windows Update**.
   - Fes clic a **«Cerca actualitzacions»** per veure si n'hi ha de disponibles.
   - Si n'hi ha, fes clic a **«Baixa»** i **«Instal·la»**.

Recorda **reiniciar el sistema periòdicament** després d'instal·lar actualitzacions. Algunes necessiten un reinici per aplicar els canvis del tot.

Si **mantens Windows 10 actualitzat**, reforçaràs la seguretat i obtindràs les funcions més recents, millores de rendiment i correccions de compatibilitat. És una mesura proactiva per mantenir el sistema resistent a possibles amenaces.

#### 3. [**Configura el Control de comptes d'usuari (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)

El **Control** de comptes d'usuari (UAC) és una funció de seguretat de Windows 10 que ajuda a impedir canvis no autoritzats al sistema demanant l'aprovació d'un administrador quan cal. Actua com a protecció davant del programari maliciós o dels usuaris que intenten fer canvis que afectin la seguretat o l'estabilitat del sistema.

Configurar el UAC al nivell adequat és essencial per **reforçar Windows 10**. Cal trobar un equilibri entre seguretat i facilitat d'ús perquè protegeixi el sistema sense interrupcions innecessàries.

Per **configurar** el UAC a Windows 10, segueix aquests passos:

1. Obre el **Tauler de control** escrivint «Tauler de control» a la barra de cerca i seleccionant-lo als resultats.
2. Al Tauler de control, fes clic a **«Comptes d'usuari»**.
3. Fes clic a **«Canvia la configuració del Control de comptes d'usuari»**.
4. Veuràs un control lliscant amb diferents nivells del UAC:
   - **«Notifica'm sempre»**: és el nivell de seguretat més alt. Demana confirmació per a qualsevol canvi al sistema, fins i tot per a tasques senzilles.
   - **«Notifica'm només quan les aplicacions intentin fer canvis a l'ordinador (per defecte)»**: és l'opció recomanada perquè equilibra seguretat i facilitat d'ús. Demana confirmació quan les aplicacions fan canvis, però no quan canvia la configuració de Windows.
   - **«Notifica'm només quan les aplicacions intentin fer canvis a l'ordinador (no atenuïs l'escriptori)»**: és semblant a l'opció anterior, però l'escriptori no s'atenua quan apareix un avís del UAC.
   - **«No m'avisis mai»**: és el nivell més baix i no demana confirmació per als canvis al sistema.
5. Mou el control lliscant fins al nivell de seguretat del UAC que vulguis.
6. Fes clic a **«D'acord»** per desar els canvis.

Es recomana mantenir el UAC activat i triar un nivell que equilibri la seguretat i la facilitat d'ús. Si el desactives del tot, el sistema queda més exposat als canvis no autoritzats i la seguretat se'n pot ressentir.

La configuració del UAC reforça el sistema Windows 10 perquè exigeix privilegis administratius per als canvis crítics, cosa que redueix el risc d'accés no autoritzat i d'infeccions de programari maliciós.

{{< figure src="windows-10-uac-bitlocker-security-overview.webp" alt="Diagrama que mostra els nivells del Control de comptes d'usuari de Windows 10 i el xifratge BitLocker protegint la integritat del sistema i les dades sensibles" >}}

#### 4. [**Fes servir contrasenyes segures**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)

Les contrasenyes segures són essencials per protegir el sistema Windows 10 contra l'accés no autoritzat. Les contrasenyes febles o fàcils d'endevinar exposen el sistema a atacs de força bruta i al trencament de contrasenyes.

Per assegurar-te que tots els comptes d'usuari del sistema Windows 10 tenen contrasenyes segures, segueix aquestes pràctiques:

1. **Complexitat**: anima els usuaris a crear contrasenyes complexes i difícils d'endevinar. Han de combinar majúscules, minúscules, números i caràcters especials. Evita les paraules habituals i els patrons previsibles.
2. **Longitud**: les contrasenyes llargues són més segures. Recomana'n de com a mínim 8 caràcters, i preferiblement més. Com més caràcters tenen, més costa desxifrar-les.
3. **Ús únic**: cada compte ha de tenir una contrasenya diferent. Reutilitzar-la en diversos comptes augmenta el risc d'una bretxa de seguretat.
4. **Evita la informació personal**: no facis servir noms, dates de naixement ni adreces. Els atacants poden obtenir o endevinar fàcilment aquestes dades.
5. **Gestors de contrasenyes**: valora l'ús d'un gestor per desar i administrar contrasenyes de manera segura. Pot generar contrasenyes fortes i úniques per a cada compte i desar-les en una base de dades xifrada.
6. **Canvia-les periòdicament**: anima els usuaris a canviar les contrasenyes de tant en tant. Defineix una política de caducitat i explica la importància d'actualitzar-les.

Les bones pràctiques de contrasenyes reforcen considerablement la seguretat del sistema Windows 10 i redueixen el risc d'accés no autoritzat o de filtracions de dades. Forma els usuaris periòdicament i ofereix recursos com ara comprovadors de robustesa i pautes per crear contrasenyes segures.

Per obtenir més informació, consulta aquest [l'article](https://simeononsecurity.com/articles/how-to-create-strong-passwords/), que tracta la seguretat de les contrasenyes i dona consells per crear-ne de segures i fàcils de recordar.

Les contrasenyes segures són una part fonamental de la seguretat del sistema. Prioritza-les per protegir les dades sensibles i la integritat de l'entorn Windows 10.

#### 5. [**Activa el xifratge BitLocker**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

Una de les maneres més eficaces de protegir les dades sensibles del sistema Windows 10 és activar el xifratge BitLocker. BitLocker xifra tot el disc perquè, si perds el dispositiu o te'l roben, les dades continuïn protegides i siguin inaccessibles per a persones no autoritzades.

Per activar BitLocker i protegir la informació sensible, segueix aquests passos:

1. **Comprova els requisits del sistema**: confirma que l'edició de Windows 10 admet BitLocker. Està disponible a les edicions Pro, Enterprise i Education.
2. **Activa BitLocker**: obre el Tauler de control i ves a la categoria **«Sistema i seguretat»**. Fes clic a **«Xifratge de la unitat BitLocker»**, tria les unitats que vols xifrar i segueix les instruccions.
3. **Tria les opcions de xifratge**: durant la configuració pots triar entre una contrasenya, una targeta intel·ligent o totes dues. Selecciona el mètode que s'ajusti als teus requisits de seguretat i preferències.
4. Desa una còpia de la clau de recuperació: desa-la en un lloc segur i separat del dispositiu. Et servirà si oblides la contrasenya o tens problemes per accedir a la unitat xifrada.
5. Administra els paràmetres de BitLocker: després d'activar-lo, pots personalitzar opcions com ara el desbloqueig automàtic d'unitats concretes o l'ús del TPM (mòdul de plataforma de confiança) per afegir-hi seguretat. Trobaràs aquests paràmetres a la interfície d'administració de BitLocker.

BitLocker afegeix una capa de protecció al sistema Windows 10. Encara que el dispositiu caigui en mans equivocades, les dades continuaran protegides i inaccessibles. Mantén la configuració de BitLocker actualitzada segons les bones pràctiques de seguretat.

Per obtenir instruccions detallades sobre com activar i administrar BitLocker, consulta la [documentació oficial de Microsoft](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview), que explica les funcions avançades i les opcions de configuració.

El xifratge BitLocker protegeix les dades sensibles i dona tranquil·litat en cas de pèrdua o robatori del dispositiu.

#### 6. **Desactiva els serveis i les funcions innecessaris**

Per millorar la seguretat del sistema Windows 10, revisa i desactiva els serveis i les funcions que no necessitis. Això redueix la superfície d'atac i les oportunitats d'explotació per part d'actors maliciosos.

Segueix aquests passos per desactivar serveis i funcions innecessaris:

1. **Identifica els serveis innecessaris**: obre la consola de serveis amb la combinació **Windows + R**, escriu **services.msc** i prem **Retorn**. Revisa la llista de serveis en execució i cerca per a què serveix cadascun. Decideix quins són imprescindibles per al funcionament del sistema.
2. **Desactiva els serveis innecessaris**: quan n'hagis identificat, fes clic amb el botó dret a cada servei i selecciona **«Propietats»**. A la finestra corresponent, canvia el **«Tipus d'inici»** a **«Desactivat»**. Així el servei no s'iniciarà automàticament quan arrenqui el sistema. Ves amb compte i desactiva només els serveis que no calen per al funcionament normal.
3. **Desactiva les funcions innecessàries**: Windows 10 també inclou funcions que potser no necessites. Obre el **Tauler de control**, ves a **Programes** o **Programes i característiques** i fes clic a **«Activa o desactiva les característiques de Windows»**. Desmarca les que no necessitis. Això redueix encara més la superfície d'atac i els recursos que consumeixen les funcions innecessàries.
4. **Revisa i actualitza la configuració periòdicament**: les necessitats del sistema poden canviar. Torna a revisar els serveis i les funcions activats i ajusta la configuració quan calgui.

Si desactives serveis i funcions innecessaris, redueixes les possibles vies d'entrada dels atacants i la superfície d'atac general del sistema Windows 10. Això millora la postura de seguretat i mitiga els riscos d'explotació.

{{< figure src="windows-10-firewall-applocker-attack-surface-reduction.webp" alt="Diagrama que mostra com les regles del tallafoc de Windows 10, les polítiques de control d'aplicacions d'AppLocker i la reducció de la superfície d'atac treballen juntes per bloquejar l'accés no autoritzat" >}}

Per obtenir més informació sobre la gestió de serveis i funcions a Windows 10, consulta aquest [article](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20), que ofereix instruccions detallades.

Ves amb compte quan desactivis serveis i funcions: si desactives components essencials, el sistema podria deixar de funcionar bé. Investiga la funció de cada servei o característica abans de canviar-ne la configuració.

#### 7. **Configura les regles del tallafoc**

El tallafoc integrat de Windows 10 és una defensa important contra el trànsit de xarxa no autoritzat. Si configures regles del tallafoc, controles quines connexions entrants i sortints es permeten i millores la seguretat del sistema.

Segueix aquests passos per configurar les regles del tallafoc a Windows 10:

1. **Accedeix a la configuració del tallafoc**: obre el **Tauler de control**, cerca **Tallafoc de Windows Defender** i obre el resultat. També pots fer clic amb el botó dret al botó **Inici**, seleccionar **Configuració** i anar a **Xarxa i Internet > Tallafoc de Windows**.
2. **Configura les regles d'entrada**: controlen les connexions de xarxa entrants. A la finestra del Tallafoc de Windows Defender, fes clic a **«Configuració avançada»**. A la finestra nova, selecciona **«Regles d'entrada»** i fes clic a **«Regla nova»**. Segueix les instruccions per permetre només les connexions entrants necessàries. Revisa quins serveis i aplicacions necessiten accés a la xarxa i crea les regles corresponents.
3. **Configura les regles de sortida**: controlen les connexions de xarxa sortints. Repeteix els passos anteriors, però selecciona **«Regles de sortida»**. Crea regles que permetin les connexions sortints de serveis i aplicacions essencials i bloquegin les connexions sospitoses o innecessàries.
4. **Revisa i actualitza les regles periòdicament**: comprova que s'ajusten als requisits del sistema. Si canvia l'entorn de xarxa o la manera d'utilitzar-lo, potser hauràs de modificar les regles o crear-ne de noves. Mantén-les actualitzades perquè el tallafoc sigui eficaç.

Si configures i mantens les regles del tallafoc, redueixes considerablement el risc d'accés no autoritzat a la xarxa i millores la seguretat del sistema Windows 10. També valora activar l'opció **«Mode furtiu»** perquè el sistema sigui menys visible per als atacants potencials.

Per obtenir instruccions detallades sobre la configuració de les regles, consulta la [documentació oficial de Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring).

Un tallafoc ben configurat és una part essencial d'una estratègia de seguretat completa. Fes-lo servir juntament amb altres mesures per protegir el sistema.

#### 8. [**Fes servir AppLocker**](https://github.com/simeononsecurity/AppLocker)

[AppLocker](https://simeononsecurity.com/github/applocker-hardening/) és una funció de Windows 10 que et permet controlar quines aplicacions s'executen al sistema. Les polítiques d'AppLocker poden restringir l'execució d'aplicacions no autoritzades o potencialment malicioses i millorar la seguretat de l'entorn Windows 10.

Segueix aquests passos per fer servir AppLocker:

1. **Accedeix a la configuració d'AppLocker**: obre l'**Editor de directives de grup local** amb la combinació **Windows + R**, escriu **gpedit.msc** i fes clic a **«D'acord»**. També pots cercar **Editor de directives de grup** al menú **Inici**.
2. **Configura les polítiques d'AppLocker**: a l'Editor de directives de grup local, ves a **Configuració de l'ordinador > Configuració de Windows > Configuració de seguretat > Polítiques de control d'aplicacions > AppLocker**. Aquí pots configurar polítiques per a **Regles d'executables**, **Regles de Windows Installer**, **Regles de scripts** i **Regles d'aplicacions empaquetades**.
3. **Crea regles d'AppLocker**: fes clic amb el botó dret a la carpeta de la política que vulguis, com ara **Regles d'executables**, i selecciona **«Crea una regla nova»**. Segueix les instruccions per especificar-ne les condicions i les excepcions. Pots basar les regles en la ruta del fitxer, el fabricant, el resum criptogràfic del fitxer o altres atributs, i així permetre o denegar l'execució.
4. **Prova i ajusta les polítiques**: prova les regles en un grup o sistema de prova i confirma que només s'executen les aplicacions autoritzades. Ajusta-les segons els resultats.
5. **Revisa i actualitza les polítiques periòdicament**: les aplicacions que fas servir poden canviar. Revisa les polítiques amb regularitat. Potser hauràs d'autoritzar aplicacions noves o retirar-ne d'obsoletes o arriscades. Mantén-les al dia per controlar les aplicacions amb eficàcia.

AppLocker ofereix un control detallat sobre l'execució d'aplicacions. Ajuda a impedir que s'executin programari no autoritzat o maliciós i redueix el risc d'infeccions, instal·lacions no autoritzades i altres incidents de seguretat.

Per obtenir més informació sobre les polítiques d'AppLocker, consulta la [documentació de Microsoft](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) o el nostre [repositori de GitHub d'AppLocker](https://github.com/simeononsecurity/AppLocker), amb recursos i exemples addicionals.

Revisa i actualitza les polítiques d'AppLocker regularment per adaptar-les als requisits de les aplicacions i a les amenaces noves. És una eina valuosa contra el programari no autoritzat i potencialment perjudicial.

#### 9. [**Fes còpies de seguretat de les dades periòdicament**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)

Fer **còpies** de seguretat de les dades amb regularitat és essencial per protegir-te de la pèrdua de dades causada per incidents de seguretat, fallades de maquinari o altres esdeveniments inesperats. Si les crees periòdicament i en comproves la integritat, podràs recuperar les dades importants en cas de desastre.

Segueix aquests passos per fer còpies de seguretat a Windows 10:

1. **Identifica les dades crítiques**: determina quins documents, fitxers personals, configuracions del sistema, paràmetres de les aplicacions i altres dades valuoses vols protegir.
2. **Tria una solució de còpia de seguretat**: selecciona una eina fiable que s'ajusti als teus requisits. Windows 10 inclou l'**Historial de fitxers** i **Còpia de seguretat i restauració de Windows**. També pots triar programari de tercers amb més funcions i flexibilitat.
3. **Defineix la freqüència**: decideix cada quant vols fer còpies segons la importància de les dades i la freqüència amb què canvien. Algunes necessiten còpies diàries; d'altres, setmanals o mensuals.
4. **Tria l'emmagatzematge**: desa les còpies en un disc dur extern, un dispositiu NAS, un servei al núvol o una combinació d'opcions. Comprova que el suport sigui segur i fiable.
5. **Configura les còpies**: especifica quines dades vols copiar, la destinació i altres opcions, com ara el xifratge o la compressió.
6. **Prova la restauració**: restaura periòdicament alguns fitxers de prova per comprovar que les còpies funcionen i que podràs recuperar les dades quan calgui.
7. **Supervisa i actualitza**: comprova que el procés s'executa com s'espera. Actualitza l'eina i ajusta la configuració quan canviïn les dades o els requisits.

Amb una rutina regular de còpies de seguretat, redueixes l'impacte de la pèrdua de dades i mantens la disponibilitat de la informació important. Desa les còpies en un lloc segur, separat de les dades originals. També valora aplicar la **regla de còpia de seguretat 3-2-1**: conserva almenys tres còpies de les dades, en dos tipus diferents de suport, i una còpia fora de les instal·lacions.

Per obtenir més informació, consulta l'article [Què és la regla de còpia de seguretat 3-2-1 i per què l'hauries d'aplicar](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). Hi trobaràs recomanacions per aplicar una estratègia de còpies de seguretat eficaç.

Les còpies periòdiques són essencials per protegir les dades i garantir-ne la disponibilitat davant d'esdeveniments imprevistos. Inclou-les en les mesures de reforç de Windows 10 per protegir la informació valuosa.

______

### [Reforç de Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 és l'última versió del sistema operatiu Windows i ofereix funcions millorades i més seguretat. Per reforçar l'entorn Windows 11, aplica aquestes bones pràctiques:

#### 1. **Secure Boot i TPM**

Secure Boot i TPM (mòdul de plataforma de confiança) són funcions de seguretat essencials de Windows 11. Ajuden a impedir l'accés no autoritzat i a garantir la integritat del sistema operatiu. Si actives Secure Boot i TPM, milloraràs la seguretat del dispositiu Windows 11.

Segueix aquests passos per activar Secure Boot i TPM al dispositiu Windows 11:

1. **Comprova la compatibilitat**: abans d'activar-los, confirma que el dispositiu admet Secure Boot i TPM. Comprova que el maquinari i el microprogramari del sistema compleixin els requisits.
2. **Accedeix a la configuració UEFI/BIOS**: reinicia el dispositiu i obre la configuració UEFI (interfície de microprogramari extensible unificada) o BIOS (sistema bàsic d'entrada/sortida). La tecla o combinació depèn del dispositiu. Sovint és Del, F2, F10 o Esc. Consulta la documentació del fabricant per obtenir instruccions precises.
3. **Activa Secure Boot**: a la configuració UEFI/BIOS, ves a les opcions de Secure Boot i activa'l. Així, durant l'arrencada només s'executaran sistemes operatius i components de confiança. Impedeix que es carregui programari no autoritzat o maliciós que pugui comprometre la seguretat.
4. **Activa TPM**: localitza les opcions del TPM a UEFI/BIOS i activa'l. El TPM és un xip dedicat a la placa base que ofereix funcions de seguretat basades en maquinari. Windows 11 en pot aprofitar les capacitats per protegir millor el sistema.
5. **Configura la seguretat del TPM**: segons el dispositiu i el microprogramari, potser podràs definir una contrasenya del TPM, activar les actualitzacions del microprogramari o ajustar altres paràmetres. Revisa les opcions disponibles i configura-les segons els requisits de seguretat.
6. **Desa i surt**: desa els canvis a UEFI/BIOS i surt de la configuració. El sistema es reiniciarà i aplicarà els paràmetres nous.

Si actives Secure Boot i TPM a Windows 11, milloraràs la postura de seguretat i reforçaràs la protecció del sistema operatiu i de les dades sensibles.

#### 2. [**Activa Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

**Windows 11** inclou una protecció antivirus integrada anomenada **Microsoft Defender Antivirus**. Ofereix protecció completa contra diversos tipus de **programari maliciós**, com ara virus, ransomware i programari espia. Si l'**actives** i l'**actualitzes regularment**, tindràs **detecció i prevenció d'amenaces en temps real**.

Segueix aquests passos per activar i actualitzar Microsoft Defender Antivirus:

1. **Comprova l'estat de l'antivirus**: obre l'aplicació **Seguretat de Windows** des del menú Inici. Ves a **«Protecció contra virus i amenaces»** i comprova l'estat de Microsoft Defender Antivirus. En una instal·lació nova de Windows 11, hauria d'estar activat per defecte.
2. **Activa la protecció en temps real**: a Seguretat de Windows, comprova que Microsoft Defender Antivirus tingui activada la protecció en temps real. Supervisa contínuament el sistema per detectar programari maliciós i altres activitats malicioses, amb **resposta immediata** i **bloqueig d'amenaces**. Si està desactivada, activa el commutador.
3. **Actualitza les definicions**: les **definicions de virus** s'han d'actualitzar sovint perquè l'antivirus detecti i bloquegi les amenaces més recents. A **«Protecció contra virus i amenaces»**, fes clic a **«Cerca actualitzacions»**. Això instal·la les **signatures** i les **capacitats de detecció** més recents.
4. **Programa anàlisis**: Microsoft Defender Antivirus et permet programar **anàlisis del sistema** per detectar i eliminar possibles amenaces. A **«Protecció contra virus i amenaces»**, selecciona **«Anàlisi ràpida»** o **«Anàlisi completa»**. També pots obrir **«Opcions d'anàlisi»** per personalitzar els paràmetres i programar anàlisis periòdiques.
5. **Configura altres paràmetres**: Microsoft Defender Antivirus inclou més funcions i opcions. A Seguretat de Windows, revisa seccions com **«Control d'aplicacions i navegador»**, **«Seguretat del dispositiu»** i **«Tallafoc i protecció de xarxa»** per personalitzar la protecció i activar funcions avançades.

Activar i actualitzar Microsoft Defender Antivirus periòdicament és essencial per mantenir una defensa sòlida contra el programari maliciós i altres amenaces. Segueix aquests passos i mantén-lo actualitzat per protegir el sistema Windows 11.

Encara que Microsoft Defender Antivirus ofereixi una protecció robusta, mantén **hàbits de navegació segurs**, ves amb compte quan **baixis fitxers** o **obris adjunts de correu electrònic**, i actualitza el **sistema operatiu i les aplicacions** per millorar la postura de seguretat.

{{< figure src="windows-11-secure-boot-tpm-defender-security-stack.webp" alt="Diagrama de la pila de seguretat de Windows 11, amb Secure Boot, la protecció de maquinari TPM, Microsoft Defender Antivirus i les capes de seguretat basada en virtualització" >}}

#### 3. **Aplica l'aïllament per maquinari per defecte**

Windows 11 aprofita funcions d'aïllament basades en maquinari com **Virtualization-based Security (VBS)** i **Hypervisor-protected Code Integrity (HVCI)** per millorar la seguretat i protegir components crítics del sistema.

Si actives i apliques aquestes funcions d'aïllament, establiràs límits de seguretat sòlids i mitigaràs diverses vies d'atac. Segueix aquests passos:

1. **Activa la tecnologia de virtualització**: comprova que el sistema sigui compatible amb la virtualització i que estigui activada a la configuració **BIOS** o al microprogramari **UEFI**. Els passos depenen del fabricant de la placa base o del microprogramari. Consulta la documentació del sistema o el lloc web del fabricant.
2. **Activa Virtualization-based Security (VBS)**: Windows 11 incorpora VBS, que fa servir la virtualització del maquinari per crear contenidors aïllats anomenats **Virtual Secure Mode (VSM)**. VSM proporciona un entorn d'execució segur per als components crítics i els protegeix d'atacs. Per activar VBS:
   - Prem **Windows + R** per obrir el quadre **Executa**.
   - Escriu **gpedit.msc** i prem **Retorn** per obrir l'Editor de directives de grup local.
   - Ves a **Configuració de l'ordinador -> Plantilles administratives -> Sistema -> Device Guard**.
   - Fes doble clic a la política **«Activa la seguretat basada en virtualització»**.
   - Selecciona **«Habilitada»** i fes clic a **«D'acord»**.

   Pot ser que VBS necessiti maquinari compatible i requisits específics del sistema. Consulta la **documentació oficial de Microsoft** per obtenir més informació.
3. **Activa Hypervisor-protected Code Integrity (HVCI)**: HVCI fa servir l'hipervisor per aplicar polítiques d'integritat del codi. Impedeix l'execució de codi no autoritzat i millora la postura de seguretat. Per activar HVCI:
   - Prem **Windows + R** per obrir Executa.
   - Escriu **msconfig** i prem **Retorn** per obrir la utilitat de configuració del sistema.
   - Ves a la pestanya **«Arrencada»**.
   - Fes clic a **«Opcions avançades»**.
   - Marca **«Activa Hypervisor-protected Code Integrity»**.
   - Fes clic a **«D'acord»** per desar els canvis i reinicia el sistema.

   HVCI requereix maquinari compatible i altres requisits del sistema. Consulta la **documentació oficial de Microsoft** per obtenir més informació.

L'aïllament per maquinari, com ara VBS i HVCI, millora considerablement la seguretat de Windows 11. Aquestes funcions protegeixen els components crítics del sistema contra atacs que intenten modificar o explotar el codi i la configuració.

Actualitza periòdicament el sistema amb els pegats de seguretat i les actualitzacions del microprogramari més recents per aprofitar les millores i mitigacions que ofereixen aquestes funcions.

La disponibilitat i els requisits de l'aïllament per maquinari depenen de la configuració del sistema i de l'edició de Windows 11. Consulta la documentació oficial de Microsoft i comprova la compatibilitat abans d'implementar aquestes funcions.

#### 4. [**Fes servir Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

**Windows Sandbox** et permet executar aplicacions no fiables o provar programari en un entorn aïllat, cosa que afegeix una capa de seguretat al sistema i redueix els riscos d'executar programes desconeguts.

Windows Sandbox crea un escriptori temporal lleuger, separat del sistema operatiu principal. Quan tanques Sandbox, es descarten tots els canvis que hi has fet i el sistema principal queda intacte.

Per fer servir Windows Sandbox, segueix aquests passos:

1. **Comprova els requisits del sistema**: confirma que el sistema compleixi els requisits per executar Windows Sandbox. En general, necessites una edició Windows 10 Pro o Enterprise i un processador amb la virtualització activada al microprogramari BIOS/UEFI. Consulta la [**documentació oficial de Microsoft**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) per veure els requisits concrets.
2. **Activa Windows Sandbox**: és una funció integrada a les edicions Windows 10 Pro i Enterprise. Per activar-la:
   - Prem **Windows + R** per obrir Executa.
   - Escriu **appwiz.cpl** i prem **Retorn** per obrir la finestra Programes i característiques.
   - Fes clic a **«Activa o desactiva les característiques de Windows»**, a l'esquerra.
   - Cerca **«Windows Sandbox»** a la llista de funcions.
   - Marca la casella que hi ha al costat i fes clic a **«D'acord»**.
   - Windows instal·larà els components necessaris. Potser hauràs de reiniciar el sistema perquè els canvis tinguin efecte.
3. **Inicia Windows Sandbox**: quan estigui activada, obre el menú **Inici**, cerca **«Windows Sandbox»** i selecciona l'aplicació. Sandbox s'obrirà en una finestra separada per executar aplicacions no fiables o provar programari en un entorn segur.
   - Obre el menú Inici i cerca Windows Sandbox.
   - Selecciona l'aplicació Windows Sandbox per obrir-la.
   - Sandbox s'obrirà en una finestra independent per oferir un entorn segur.

Les aplicacions que s'executen a Windows Sandbox queden aïllades i els canvis es descarten quan tanques l'entorn. Desa els fitxers o les dades fora de Sandbox si els vols conservar.

Windows Sandbox és útil per provar programari desconegut, obrir fitxers sospitosos o visitar llocs web potencialment arriscats. Conté les activitats malicioses o els canvis no desitjats dins de l'entorn aïllat i evita que afectin el sistema operatiu principal.

Si incorpores Windows Sandbox a les pràctiques de seguretat, reduiràs els riscos d'executar aplicacions no fiables i protegiràs el sistema d'amenaces potencials.

{{< figure src="windows-sandbox-application-guard-isolation-architecture.webp" alt="Diagrama que il·lustra com Windows Sandbox i Microsoft Defender Application Guard creen contenidors virtuals aïllats per protegir el sistema amfitrió d'aplicacions i sessions del navegador no fiables" >}}

Per obtenir més informació sobre Windows Sandbox i el seu ús, consulta la [**documentació oficial de Microsoft**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview).

#### 5. [**Implementa Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)

**Microsoft** Defender Application Guard és una funció de seguretat que aïlla les sessions del navegador Microsoft Edge del sistema operatiu subjacent. Si Edge s'executa en un entorn segur i aïllat, Application Guard ajuda a protegir el sistema contra atacs des del navegador i llocs web maliciosos.

Per implementar Microsoft Defender Application Guard i millorar la seguretat del navegador, segueix aquests passos:

1. **Comprova la compatibilitat**: confirma que el sistema compleixi els requisits per executar Microsoft Defender Application Guard. En general, necessites Windows 10 Pro o Enterprise, un processador compatible amb virtualització i almenys 8 GB de RAM. Consulta la [**documentació oficial de Microsoft**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) per veure els requisits concrets.
2. **Activa Application Guard**: és una funció opcional de Windows 10. Per activar-la:
   - Prem **Windows + R** per obrir Executa.
   - Escriu **appwiz.cpl** i prem **Retorn** per obrir Programes i característiques.
   - Fes clic a **«Activa o desactiva les característiques de Windows»**, a l'esquerra.
   - Cerca **«Microsoft Defender Application Guard»** a la llista.
   - Marca la casella del costat i fes clic a **«D'acord»**.
   - Windows instal·larà els components necessaris. Potser hauràs de reiniciar el sistema perquè els canvis s'apliquin.
3. **Configura Application Guard**: quan l'hagis activat, ajusta'n la configuració a les necessitats de seguretat. Pots definir el nivell d'aïllament i controlar com tracta els llocs web i els fitxers no fiables. Configura aquests paràmetres amb l'aplicació **Seguretat de Windows** o les polítiques de grup.
4. **Prova i verifica**: obre Microsoft Edge i visita un lloc web maliciós conegut o amb riscos potencials. Comprova que Application Guard aïlli correctament la sessió del navegador i impedeixi els atacs.

Microsoft Defender Application Guard afegeix una capa de protecció aïllant les sessions del navegador i confinant les amenaces potencials a un entorn segur. Això protegeix el sistema i les dades dels atacs des del navegador, com ara les baixades iniciades sense consentiment, els scripts maliciosos i les explotacions de vulnerabilitats de dia zero.

Per obtenir informació detallada sobre la configuració i l'ús de Microsoft Defender Application Guard, consulta la [**documentació oficial de Microsoft**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard).

#### 6. [**Activa Controlled Folder Access (accés controlat a les carpetes)**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

**Controlled Folder Access** (accés controlat a les carpetes) és una funció de seguretat de Windows 11 que protegeix les carpetes importants de canvis no autoritzats causats pel ransomware i altres programes maliciosos. Si l'actives i afegeixes les carpetes necessàries a la llista protegida, milloraràs la seguretat del sistema i evitaràs possibles pèrdues de dades.

Segueix aquests passos per activar Controlled Folder Access (accés controlat a les carpetes) i protegir les carpetes importants:

1. **Obre Seguretat de Windows**: prem la **tecla Windows**, escriu **«Seguretat de Windows»** i selecciona l'aplicació als resultats.
2. **Ves a la configuració de protecció contra virus i amenaces**: a l'aplicació Seguretat de Windows, fes clic a la pestanya **«Protecció contra virus i amenaces»** del menú esquerre.
3. **Configura Controlled Folder Access (accés controlat a les carpetes)**: a la secció **«Protecció contra ransomware»**, fes clic a **«Administra la protecció contra ransomware»** per obrir-ne la configuració.
4. **Activa Controlled Folder Access (accés controlat a les carpetes)**: posa el commutador en **«Activat»**. Windows avisarà que només les aplicacions de confiança podran accedir a les carpetes protegides.
5. **Afegeix carpetes protegides**: fes clic a **«Carpetes protegides»** i després a **«Afegeix una carpeta protegida»**. Tria les carpetes que vols protegir i fes clic a **«D'acord»**.
   - Es recomana protegir Documents, Imatges, Vídeos i altres directoris amb dades valuoses.
6. **Permet o bloqueja aplicacions**: per defecte, Controlled Folder Access (accés controlat a les carpetes) permet que les aplicacions de confiança accedeixin a les carpetes protegides. Pots canviar aquest comportament amb **«Permet que una aplicació utilitzi l’accés controlat a les carpetes»** i autoritzar o bloquejar aplicacions concretes.
7. **Supervisa i revisa**: Windows supervisarà i registrarà contínuament els intents d'accés de les aplicacions no autoritzades. Pots revisar els registres amb l'opció **«Revisa»**, a la secció **«Aplicacions bloquejades recentment»** de la configuració.

Controlled Folder Access (accés controlat a les carpetes) afegeix una capa de protecció a les carpetes importants, mitiga els canvis no autoritzats i redueix les pèrdues de dades causades pel ransomware. Revisa regularment la configuració per comprovar que les carpetes protegides s'ajusten als requisits de seguretat.

Per obtenir més informació sobre la configuració i l'ús de Controlled Folder Access (accés controlat a les carpetes), consulta la [**documentació oficial de Microsoft**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide).

#### 7. **Activa el manteniment automàtic de Windows**

Windows 11 inclou una funció anomenada Manteniment automàtic que ajuda a optimitzar i protegir el sistema amb tasques de manteniment periòdiques. Si l'actives, contribueixes a mantenir el sistema àgil i segur.

Segueix aquests passos per activar el Manteniment automàtic de Windows:

1. **Obre la configuració de Windows**: prem la **tecla Windows**, escriu **«Configuració»** i selecciona l'aplicació als resultats.
2. **Accedeix als paràmetres de manteniment**: a Configuració, fes clic a la categoria **«Sistema»** i selecciona **«Quant a»** al menú esquerre. Ves al final de la pàgina i fes clic a l'enllaç **«Informació del sistema»**.
3. **Obre la configuració de manteniment**: a la finestra Informació del sistema, fes clic a l'enllaç **«Manteniment»** del final de la pàgina.
4. **Activa el Manteniment automàtic**: posa en **«Activat»** el commutador del Manteniment automàtic.
5. **Configura els paràmetres**: per defecte, Windows programa les tasques de manteniment cada dia a les 2.00. Si vols un altre horari, fes clic a **«Canvia la configuració de manteniment»** i ajusta l'hora d'inici i la freqüència.
6. **Revisa altres paràmetres**: sota del commutador trobaràs opcions com **«Permet que el manteniment programat activi l'ordinador a l'hora prevista»** i **«Permet que el manteniment programat s'executi encara que l'ordinador funcioni amb bateria»**. Ajusta-les segons les teves preferències i requisits.
7. **Supervisa les tasques de manteniment**: quan l'activis, Windows executarà tasques en segon pla a l'hora prevista. Pots supervisar-les a la secció **«Manteniment»** de Seguretat de Windows o revisar els registres de manteniment al Visor d'esdeveniments.

El Manteniment automàtic ajuda a optimitzar i protegir el sistema amb tasques essencials periòdiques, com ara actualitzacions de programari, optimització del disc i anàlisis de seguretat. Així el sistema es manté en bon estat i ofereix una experiència més àgil i segura.

Per obtenir més informació sobre el Manteniment automàtic de Windows i les opcions de configuració, consulta la [**documentació oficial de Microsoft**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence).

______

## Ordre recomanat per reforçar la seguretat

Aplica els controls en un ordre que protegeixi primer l'accés i la recuperació:

1. Confirma l'edició i la compilació de Windows, l'estat de suport, les funcions de seguretat del maquinari i les opcions de recuperació.
2. Instal·la les actualitzacions de seguretat actuals i reinicia el sistema durant una finestra planificada.
3. Crea una còpia de seguretat provada i registra l'estat actual del tallafoc, Defender, BitLocker, els serveis i les polítiques locals.
4. Mantén el UAC activat, fes servir comptes d'administrador separats i exigeix MFA per a l'accés remot i al núvol quan estigui disponible.
5. Activa les proteccions de Defender, els perfils del tallafoc, Secure Boot, BitLocker i l'aïllament per maquinari quan l'edició i el maquinari ho admetin.
6. Prova les regles ASR, Controlled Folder Access (accés controlat a les carpetes), AppLocker i els canvis dels serveis en mode d'auditoria o en un entorn pilot abans de bloquejar aplicacions o desactivar serveis de manera generalitzada.
7. Centralitza els registres i revisa els inicis de sessió fallits, els canvis de polítiques, els esdeveniments de Defender i els bloquejos del tallafoc.
8. Reinicia l'ordinador, prova les aplicacions necessàries, verifica l'accés de recuperació i documenta l'estat final.

El [Security Compliance Toolkit de Microsoft](https://learn.microsoft.com/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10) ofereix línies de base versionades per a Windows 10, Windows 11 i Windows Server. Fes servir la línia de base corresponent com a punt de partida revisat. Microsoft adverteix que cal provar els canvis de les línies de base abans de desplegar-los en producció.

## Límit de suport de Windows 10

Microsoft va acabar el suport de Windows 10 versió 22H2 el 14 d'octubre de 2025. Després d'aquesta data, una instal·lació de Windows 10 reforçada no rep actualitzacions de seguretat per la via habitual, llevat que s'apliqui un acord de cicle de vida o d'actualitzacions de seguretat ampliades. Inclou la migració, la substitució o una excepció aprovada al pla de seguretat. El reforç no allarga el cicle de vida del producte. Consulta l'[avís de finalització del suport de Windows 10 de Microsoft](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).

## Reversió dels canvis en serveis i funcions

Abans de desactivar un servei, comprova'n les dependències i prova les càrregues de treball. No desactivis **RPC**, **Windows Update**, **Windows Event Log** ni cap altre servei perquè una llista genèrica l'etiqueti d'innecessari. El nom d'un servei no n'explica la funció al teu sistema.

Abans de fer un canvi, exporta la configuració del servei i registra'n els serveis dependents:

```powershell
$name = 'Spooler'
Get-CimInstance Win32_Service -Filter "Name='$name'" |
    Select-Object Name, DisplayName, State, StartMode, StartName, PathName |
    Export-Csv "C:\Temp\$name-before.csv" -NoTypeInformation
Get-Service -Name $name -DependentServices
Get-Service -Name $name -RequiredServices
```

Canvia un servei cada vegada. Prova **Manual** abans de **Desactivat** quan una càrrega de treball pugui iniciar el servei a demanda. Registra el tipus d'inici anterior. Després de provar-lo, revisa el comportament de les aplicacions, el Visor d'esdeveniments, Windows Update, la impressió, l'administració remota, l'accés VPN i les tasques programades.

Per revertir el canvi, restaura el tipus d'inici registrat i inicia el servei només després de comprovar-ne les dependències:

```powershell
Set-Service -Name $name -StartupType Manual
Start-Service -Name $name
Get-Service -Name $name
```

Per revertir un canvi de política més ampli, restaura la còpia de seguretat de GPO o del registre amb la mateixa eina que vas fer servir per crear-la. Conserva una via de recuperació fora de línia i les credencials d'un administrador local abans de fer canvis remots. Microsoft documenta la sintaxi de configuració de serveis a [`sc.exe config`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-config).

## Registre de validació dels controls

Per a cada canvi de reforç, registra el control, l'abast, el valor anterior, el valor nou, el resultat de la prova, els identificadors d'esdeveniment revisats, la persona responsable i l'ordre de reversió. Una aplicació bloquejada o una impressora que no funciona són incidències operatives, no proves que el control sigui erroni. Després de revisar les proves, ajusta l'abast, les exclusions o el grup de desplegament.

______

## Conclusió

**Aplicar** aquestes **bones pràctiques de reforç de Windows** és essencial per protegir els sistemes Windows. Si **actualitzes el sistema operatiu** periòdicament, corregiràs vulnerabilitats i milloraràs l'estabilitat. L'activació de funcions com l'**antivirus** i el **xifratge** afegeix protecció a les dades. Configurar uns **controls d'accés** adequats impedeix canvis no autoritzats i restringeix l'accés als recursos sensibles.

Aquestes bones pràctiques milloren la seguretat de l'**entorn Windows**, protegeixen les dades i mantenen la integritat de la **infraestructura digital**. Mantén-te al dia i revisa les mesures de seguretat periòdicament per anticipar-te a les amenaces potencials.

El **reforç de Windows** és un procés continu. Informa't de les actualitzacions i pràctiques de seguretat més recents. Si mantens una actitud proactiva i apliques aquestes mesures, mitigaràs els riscos de seguretat i protegiràs els sistemes Windows.

Per obtenir més informació sobre el reforç de Windows i les bones pràctiques, consulta fonts fiables com ara la **documentació de Microsoft**, els **fòrums de seguretat** i els **llocs web de ciberseguretat de confiança**.

______

## Referències:

- [Seguretat de Microsoft Windows](https://www.microsoft.com/en-us/security)
- [Publicació especial 800-171 de NIST: protecció de la informació no classificada controlada en sistemes i organitzacions no federals](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [Referència CIS per a Microsoft Windows 10](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [Referència CIS per a Microsoft Windows 11](https://www.cisecurity.org/benchmark/microsoft_windows_11/)
