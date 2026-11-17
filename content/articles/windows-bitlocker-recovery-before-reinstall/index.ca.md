---
title: "Troba la clau de recuperació de BitLocker abans de reinstal·lar Windows"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Troba i verifica la clau de recuperació de BitLocker correcta, protegeix-ne una còpia independent i tria la via adequada de recuperació o reinstal·lació de Windows abans d'esborrar una unitat."
genre: ["Seguretat de Windows", "Recuperació de dades", "Administració de sistemes"]
tags: ["clau de recuperació de BitLocker", "reinstal·lar Windows 11", "reinstal·lar Windows 10", "xifratge del dispositiu", "ID de clau de recuperació", "clau de recuperació del compte Microsoft", "clau del compte laboral o escolar", "còpia de seguretat de la clau", "unitat xifrada", "instal·lació neta", "recuperació de Windows", "còpia de BitLocker", "clau de recuperació de 48 dígits", "mitjà d'instal·lació de Windows", "còpia de dades", "xifratge de la unitat", "llista de verificació de recuperació", "instal·lació de Windows", "resolució de problemes de BitLocker", "preparació per reinstal·lar"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Un portàtil amb una unitat bloquejada, una targeta separada amb la clau de recuperació, una còpia USB i una llista de recuperació marcada."
coverCaption: "Verifica la clau de recuperació abans d'esborrar la unitat."
---

Una instal·lació neta de Windows esborra la unitat seleccionada. Si la unitat antiga fa servir **BitLocker** o **Xifratge del dispositiu**, troba la clau de recuperació i copia els fitxers abans de començar. La clau permet accedir a les dades antigues xifrades. Una instal·lació nova de Windows no restaura els fitxers esborrats de la unitat.

<!--more-->

## Idees clau

- **Troba la clau correcta:** compara l'ID que mostra Windows amb la clau del compte, d'una impressió o d'una còpia USB.
- **Comprova l'accés:** revisa la còpia, compara l'ID i desbloqueja la unitat abans d'esborrar particions.
- **Protegeix la còpia:** desa la clau de 48 dígits separada de l'ordinador i del USB d'instal·lació.
- **Tria la via adequada:** fes servir les opcions de recuperació si necessites la instal·lació antiga. Tria una instal·lació neta només després de verificar una còpia independent dels fitxers.

## Abans de començar

Necessites accés a l'ordinador afectat, un segon dispositiu per comprovar el compte o la còpia, i una unitat externa o emmagatzematge al núvol de confiança per als fitxers importants. **Temps:** trobar la clau depèn de l'accés al compte. Copiar els fitxers depèn del volum de dades. **Dificultat:** bàsica per comprovar el compte i intermèdia per als instruments de recuperació. Aquesta guia tracta la preparació i les decisions de recuperació per a Windows 10 i Windows 11. La [guia d'instal·lació neta de Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) explica els mitjans i la configuració.

*El suport estàndard de Windows 10 va acabar el 14 d'octubre de 2025. Planifica instal·lar una versió compatible de Windows 11 si el dispositiu compleix els requisits. Microsoft detalla el [cicle de vida de Windows 10 i les opcions de suport ampliat](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Avís:** no suprimeixis una partició per resoldre una petició de recuperació de BitLocker si encara necessites fitxers de la instal·lació antiga. Microsoft diu que un restabliment sense la clau de recuperació elimina aquests fitxers. Consulta les [indicacions de Microsoft sobre la clau de recuperació](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Comprova si el xifratge està actiu

**Xifratge del dispositiu** i **BitLocker** xifren una unitat perquè algú sense les credencials adequades no en pugui llegir el contingut. Si Windows encara s'inicia, a Windows 11 obre **Configuració > Privadesa i seguretat > Xifratge del dispositiu**. A les edicions amb gestió de BitLocker, cerca **Gestiona BitLocker** al menú Inici. Anota la lletra de la unitat xifrada i el compte utilitzat per configurar el dispositiu. En un dispositiu laboral o escolar gestionat, sovint l'organització conserva la clau.

També pots comprovar-ne l'estat des de la línia d'ordres. Cerca **Símbol del sistema** al menú Inici, selecciona **Executa com a administrador** i introdueix aquestes ordres. Canvia `C:` si Windows utilitza una altra lletra. Un **protector** és un mètode que Windows fa servir per desbloquejar una unitat xifrada.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

La primera ordre mostra l'estat del xifratge, la protecció i el bloqueig. La segona llista els tipus i els ID dels protectors i pot mostrar la contrasenya de recuperació. Microsoft documenta aquestes comprovacions a la [guia d'operacions de BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) i a la [referència de l'ordre d'estat](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **No enganxis la sortida en una petició d'ajuda ni la comparteixis en una captura de pantalla.** Si el dispositiu ja està bloquejat, fes servir l'ID de la pantalla de recuperació. Els vuit primers dígits ajuden a triar la clau correcta.

## On trobar la clau de recuperació de BitLocker

L'**ID de la clau de recuperació** identifica una clau desada. La **clau de recuperació** és el número independent de 48 dígits que introdueixes per desbloquejar la unitat. No escriguis l'ID al camp de contrasenya de recuperació.

| Dispositiu o còpia | On cercar |
|---|---|
| **Compte personal de Microsoft** | Des d'un segon dispositiu, inicia la sessió al [portal de claus de recuperació de Microsoft](https://aka.ms/myrecoverykey). Compara l'ID abans d'utilitzar la clau de 48 dígits. |
| **Dispositiu laboral o escolar** | Comprova el compte de l'organització al [portal de Microsoft per a comptes laborals o escolars](https://aka.ms/aadrecoverykey), o consulta l'equip de TI. |
| **Impressió o còpia USB** | Troba el full o el fitxer de text creat en activar el xifratge. Compara'n l'ID amb el de la pantalla. |

Microsoft enumera aquestes ubicacions a [Troba la clau de recuperació de BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Comença per la clau amb l'ID que coincideix amb la petició. Una clau d'un altre dispositiu o d'un protector suprimit pot no desbloquejar aquest volum. Si una altra persona va configurar el dispositiu, pot tenir la clau al seu compte.

## Crea una còpia separada de la clau

Si Windows encara s'inicia en una edició Pro, Enterprise o Education, cerca **Gestiona BitLocker**. Selecciona **Fes una còpia de seguretat de la clau de recuperació** al costat de la unitat xifrada. Microsoft permet desar-la en un compte, una unitat USB, un fitxer de text o una impressió. Si tries un fitxer o USB, desa'l només en un mitjà xifrat amb control d'accés i separat de l'ordinador. No facis servir una ubicació sense xifrar. [Fes una còpia de seguretat de la clau de recuperació de BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key) explica la interfície i les opcions actuals.

A Windows Home no hi ha **Gestiona BitLocker**. A Windows 11 comprova **Configuració > Privadesa i seguretat > Xifratge del dispositiu** i verifica la clau al compte Microsoft utilitzat durant la configuració. Microsoft explica que [Xifratge del dispositiu](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) desa la clau al compte Microsoft o laboral vinculat quan s'activa. Desa una còpia protegida independent si la configuració ofereix una opció d'exportació.

Obre una còpia digital des d'un segon dispositiu. Compara una impressió amb l'entrada del compte o la pantalla de recuperació. Fes coincidir l'**ID de la clau de recuperació** amb el de la pantalla o la llista de protectors. Comprova que hi hagi els 48 dígits de la clau corresponent. Desa la còpia impresa o extraïble lluny de l'ordinador xifrat. Qui tingui l'ordinador i la clau podria esquivar la protecció, adverteix Microsoft a les [indicacions de còpia](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). No adjuntis la clau a un tiquet d'assistència.

> **Resultat esperat:** tens una clau de recuperació coincident disponible fora de l'ordinador.

## Desbloqueja un ordinador que no s'inicia

Si apareix la **pantalla de recuperació de BitLocker**, introdueix la clau de 48 dígits que coincideix amb l'ID. Si Windows s'inicia, copia els fitxers abans de modificar particions. Si la clau desbloqueja la unitat però Windows continua sense iniciar-se, obre l'[entorn de recuperació de Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) i prova **Reparació d'inici** abans de restablir-lo. Algunes eines de recuperació necessiten la clau mentre la unitat està xifrada.

Per copiar fitxers amb les eines de recuperació, obre **Resolució de problemes > Opcions avançades > Símbol del sistema** a l'entorn de recuperació de Windows. Fes servir `manage-bde -status` i `dir` per identificar el volum xifrat de Windows i una unitat externa separada per a la còpia. **Les lletres poden diferir de les del Windows habitual.** No copiïs al USB d'instal·lació ni a la unitat d'origen xifrada.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

Les lletres són exemples. Després d'identificar els volums correctes, desbloqueja el volum de Windows amb la clau corresponent. Substitueix la lletra i el marcador per valors teus. Escriu localment la clau real de 48 dígits. No publiquis ni comparteixis la sortida.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

L'opció documentada `-recoverypassword` rep la clau de 48 dígits com a argument d'ordre. Això exposa la clau a l'historial del shell, a les transcripcions i a la inspecció de processos. Fes servir la pantalla de recuperació de Windows si vols introduir la clau sense un argument de línia d'ordres. Si has desat un fitxer de clau `.bek` separat, `-recoverykey <path-to-external-bek>` evita que hagis d'escriure els 48 dígits. Mantén la clau fora de captures i tiquets.

Microsoft documenta l'[ordre de desbloqueig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). Les [indicacions de recuperació](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) també descriuen com copiar fitxers d'usuari a una altra unitat després de desbloquejar-la. Per copiar com a exemple la carpeta Documents, confirma el nom del compte de Windows i la lletra de la unitat externa, i substitueix els dos camins:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

Les opcions **`/S /E`** inclouen subcarpetes, també les buides. **`/I`** tracta la destinació com una carpeta, **`/H`** inclou fitxers ocults i **`/V`** comprova cada fitxer escrit. Microsoft les documenta a la [referència de xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Repeteix-ho amb altres carpetes necessàries. Obre els fitxers copiats en un altre dispositiu abans d'esborrar la unitat de Windows. Si no pots identificar els volums o la còpia falla, atura't i consulta un especialista de confiança en recuperació.

## Decideix si cal reinstal·lar

**Una còpia de la clau no és una còpia dels fitxers.** Segueix aquest ordre abans de triar una via de reinstal·lació:

1. Identifica la unitat xifrada i l'ID de la seva clau de recuperació.
2. Recupera la clau coincident de 48 dígits del compte, la impressió o la còpia USB.
3. Si la unitat està bloquejada, desbloqueja-la des de la pantalla o les eines de recuperació.
4. Copia Escriptori, Documents, Imatges i altres carpetes locals a una unitat externa o al núvol de confiança. Inclou exportacions del navegador, dades d'aplicacions i dades de llicència si cal.
5. Obre uns quants fitxers copiats des d'un segon dispositiu.
6. Tria reparació, restabliment o reinstal·lació només després de comprovar la còpia.

> **Resultat esperat:** la clau correcta i els fitxers importants són accessibles fora de la instal·lació antiga de Windows.

Microsoft enumera [les opcions de recuperació de Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows), amb efectes diferents en els fitxers i les aplicacions. Moltes opcions de l'entorn de recuperació de Windows exigeixen la clau si BitLocker protegeix la unitat. Si el volum hi està bloquejat, **Conserva els meus fitxers** no el desbloqueja sense la clau.

**Reparació d'inici** i **Restauració del sistema** intenten reparar la instal·lació existent. **Restableix aquest PC** ofereix **Conserva els meus fitxers**, però elimina aplicacions i configuració. **Suprimeix-ho tot** esborra fitxers personals. Iniciar **`setup.exe` des d'una sessió de Windows activa** ofereix una reinstal·lació al mateix lloc amb opcions per conservar dades. Seleccionar **Instal·la Windows** després d'arrencar des del USB inicia una instal·lació neta que elimina fitxers, aplicacions i configuració de la instal·lació seleccionada. El mateix mitjà també ofereix una via de reparació. Llegeix l'opció i comprova el disc de destinació abans de confirmar. Microsoft explica les dues vies a les [instruccions de reinstal·lació](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Situació | Acció següent |
|---|---|
| **Windows s'inicia i necessites els fitxers** | Fes una còpia dels fitxers, verifica la clau i després tria reparació o reinstal·lació. |
| **Windows demana la clau** | Compara l'ID de la pantalla amb una clau desada abans de modificar la unitat. |
| **No hi ha clau coincident ni còpia dels fitxers** | Atura't abans d'esborrar la unitat. Revisa tots els comptes, impressions, còpies USB i consulta l'equip de TI. |
| **Els fitxers són copiats i vols començar de nou** | Segueix les [instruccions de reinstal·lació de Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) i tria amb cura el disc de destinació. |

Microsoft diu que el suport no pot recrear una clau perduda. Si no la trobes, deixa de modificar el microprogramari i revisa totes les ubicacions de còpia. Demana ajuda a l'administrador si és un dispositiu gestionat. Un restabliment sense la clau necessària elimina els fitxers antics. Una instal·lació neta també elimina fitxers personals, aplicacions, personalitzacions del dispositiu i configuració de la instal·lació seleccionada. Pren la decisió després de comprovar la còpia.

## Resolució de problemes

- **La clau no funciona:** torna a comprovar l'ID i el compte. Un dispositiu pot tenir diverses claus desades.
- **No hi ha Gestiona BitLocker:** Windows Home fa servir Xifratge del dispositiu en dispositius compatibles. Comprova Configuració i el compte Microsoft de la configuració.
- **Hi ha diverses claus en un compte:** compara els vuit primers dígits de l'ID de la pantalla amb les entrades desades. No triïs només pel nom del dispositiu.
- **La clau desbloqueja la unitat però Windows no s'inicia:** prova Reparació d'inici a l'entorn de recuperació de Windows. Copia fitxers accessibles abans de restablir o fer una instal·lació neta.
- **La clau la guarda l'empresa o l'escola:** contacta amb l'administrador abans de restablir o reinstal·lar el dispositiu.
- **El fitxer de la clau és a l'ordinador bloquejat:** cerca un compte separat, una impressió o una còpia extraïble. Una còpia només a la unitat xifrada no ajuda mentre està bloquejada.
- **La petició ha aparegut després d'un canvi del microprogramari:** anota el canvi i no en facis més. Troba la clau coincident o contacta amb l'administrador.

## Passos següents

Després de verificar la clau i els fitxers, segueix la [guia d'instal·lació neta de Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) si s'ajusta al teu objectiu. Quan Windows s'iniciï, comprova **Configuració > Privadesa i seguretat > Xifratge del dispositiu** o cerca **Gestiona BitLocker**. A Pro, Enterprise o Education, selecciona **Fes una còpia de seguretat de la clau de recuperació**. A Home, verifica que el compte vinculat contingui la clau actual i desa una còpia separada si Windows permet exportar-la. No donis per fet que la clau antiga serveix per a una instal·lació nova xifrada.
