---
title: "Millora la seguretat i la privadesa"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "Mantén-te segur a Internet. Aprèn per què cal reforçar Windows i eliminar programari innecessari per millorar la seguretat i la privadesa."
tags: ["Reforç de Windows", "Eliminació de programari innecessari de Windows", "Millora de la seguretat", "Privadesa", "Atacs cibernètics", "Seguretat del sistema operatiu", "Sistema operatiu Windows", "Privadesa de les dades", "Ciberdelinqüents", "Superfície d'atac", "Vulnerabilitats", "Actualitzacions de seguretat", "Mecanismes d'autenticació", "Programari no desitjat", "Millora del rendiment", "Recollida de dades", "Autenticació en dos passos", "Programari antivirus", "Programari antimalware", "Informació sensible", "Guia completa"]
cover: "/img/cover/debloat-windows-for-improved-privacy-and-security.webp"
coverAlt: "Il·lustració d'una pantalla d'ordinador amb una barra de progrés per reforçar Windows i eliminar programari innecessari, envoltada d'elements digitals abstractes de seguretat sobre un fons fosc."
coverCaption: ""
---

**Windows** és el sistema operatiu més utilitzat del món, cosa que el converteix en un objectiu habitual dels ciberdelinqüents. Per protegir les teves dades i la privadesa, has d'aplicar mesures de seguretat per **reforçar el sistema i eliminar-ne el programari innecessari**. Aquesta guia explica per què cal reforçar Windows i fer-ne la desbrossada, i com aquestes accions poden millorar la seguretat i la privadesa generals.

## Què és el reforç de Windows?
El reforç de Windows és el procés de protegir un sistema operatiu Windows reduint-ne la superfície d'atac i les vulnerabilitats. Això s'aconsegueix **desactivant o eliminant funcions i serveis innecessaris**, aplicant actualitzacions de seguretat i utilitzant [contrasenyes segures](https://simeononsecurity.com/articles/how-to-create-strong-passwords/) i mecanismes d'autenticació.

## Per què és important reforçar Windows?
El reforç de Windows ajuda a protegir contra els atacs cibernètics perquè **redueix el nombre de vies d'atac potencials**. Sovint, els ciberdelinqüents exploten vulnerabilitats del sistema operatiu o de les aplicacions per accedir a un sistema o robar dades sensibles. Si reforces el sistema, pots **reduir les superfícies d'atac** i dificultar que els atacants comprometin les teves dades o la privadesa.

## Què vol dir eliminar programari innecessari de Windows?
Eliminar programari innecessari de Windows és el procés de **treure programari i serveis innecessaris o no desitjats** d'un sistema operatiu Windows. Això pot **millorar el rendiment i l'estabilitat** del sistema i augmentar la privadesa en reduir les dades que Microsoft i altres programes de tercers recullen i emmagatzemen.

## Per què és important eliminar programari innecessari de Windows?
Eliminar programari innecessari d'un sistema Windows ajuda a **reduir la superfície d'atac i augmentar la privadesa**. Molts programes i serveis no desitjats recullen dades sobre els teus hàbits d'ús i informació personal, que es poden vendre o fer servir per a publicitat dirigida. Si elimines aquestes funcions innecessàries, pots **reduir la quantitat de dades que es recullen i emmagatzemen** i millorar la privadesa i la seguretat.

______

## Com reforçar Windows i eliminar-ne el programari innecessari?
Pots seguir aquests passos per reforçar el sistema Windows i eliminar-ne el programari innecessari:

1. **Instal·la les actualitzacions**: mantén el sistema al dia instal·lant les actualitzacions de seguretat quan estiguin disponibles. Això ajuda a corregir vulnerabilitats i evita que els ciberdelinqüents les explotin.

2. **Desactiva els serveis innecessaris**: molts serveis que s'executen en segon pla es poden **desactivar per reduir la superfície d'atac i millorar el rendiment**. Alguns exemples són el servei de cua d'impressió, el servei de registre remot i el servei de crida a procediment remot (RPC).

3. **Elimina el programari innecessari**: **desinstal·la qualsevol programa que ja no utilitzis o necessitis**, perquè pot reduir el rendiment i crear vulnerabilitats de seguretat.

4. **Fes servir contrasenyes segures**: utilitza **contrasenyes segures i úniques** per a tots els comptes i activa l'**autenticació de dos factors** sempre que sigui possible.

5. **Fes servir programari antivirus i antimalware**: instal·la i actualitza regularment **programari antivirus i antimalware** per protegir-te dels atacs cibernètics.

## Un ordre més segur per eliminar components

Eliminar components canvia les aplicacions instal·lades, les tasques programades, els serveis, les polítiques i la configuració de recollida de dades. Tracta cada canvi com una modificació de configuració, no com una cursa de neteja.

1. Anota l'edició i la compilació de Windows, les aplicacions instal·lades, les entrades d'inici, els serveis, les tasques programades i la configuració de privadesa actual.
2. Crea una còpia de seguretat provada i confirma que tens una via de recuperació amb un administrador local.
3. Desinstal·la les aplicacions que no fas servir des de Configuració o amb el desinstal·lador compatible del proveïdor.
4. Abans de canviar un servei, revisa'n la funció, les dependències, el mode d'inici, el compte i la càrrega de treball.
5. Prova en mode d'auditoria les funcions de reducció de superfície d'atac de Defender abans d'activar el bloqueig. Revisa els esdeveniments i afegeix només regles d'excepció específiques després de provar-les.
6. Revisa les funcions opcionals de Windows i les tasques programades segons qui les gestiona i amb quin propòsit. No eliminis un component només perquè el nom et sigui desconegut.
7. Reinicia i prova l'inici de sessió, la xarxa, la impressió, les actualitzacions, les còpies de seguretat, la VPN, les eines d'accessibilitat i les aplicacions de feina.
8. Mantén un registre dels canvis i restaura un element cada vegada si una prova falla.

Microsoft documenta el mode d'auditoria de les funcions de reducció de superfície d'atac, inclòs l'accés controlat a les carpetes. El mode d'auditoria registra els bloquejos previstos sense aplicar-los. Consulta la [descripció general de Microsoft sobre la reducció de la superfície d'atac](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-overview?view=o365-worldwide).

## Revisió i reversió dels serveis

Cal matisar els exemples originals. **La crida a procediment remot (RPC) és compatible amb molts components de Windows i no s'ha de desactivar com a mesura genèrica de privadesa**. La decisió sobre la cua d'impressió depèn de la funció de l'equip. Un servidor d'impressió la necessita. En un ordinador sense necessitat d'imprimir, també cal provar les dependències i les aplicacions abans de fer un canvi. El registre remot també és compatible amb algunes eines d'administració.

Registra l'estat actual abans de canviar un servei:

```powershell
$name = 'Spooler'
Get-CimInstance Win32_Service -Filter "Name='$name'" |
    Select-Object Name, State, StartMode, StartName, PathName |
    Export-Csv "C:\Temp\$name-before.csv" -NoTypeInformation
Get-Service -Name $name -RequiredServices
Get-Service -Name $name -DependentServices
```

Fes servir **Manual** abans que **Disabled** si Windows o una aplicació necessita activar el servei quan ho demani. Prova el sistema després de cada canvi. Per revertir-lo, utilitza el mode d'inici registrat i revisa el Visor d'esdeveniments:

```powershell
Set-Service -Name $name -StartupType Manual
Start-Service -Name $name
Get-Service -Name $name
```

No executis en un sistema de producció cap script no revisat per eliminar components innecessaris. Guarda la versió de l'script, la configuració exportada, els valors originals dels serveis i el registre de la clau de recuperació amb la sol·licitud de canvi.

## Límits de la privadesa

Eliminar una aplicació no demostra que Windows o una altra aplicació instal·lada hagi deixat d'enviar telemetria. La configuració de privadesa, el compte, la política de diagnòstic, els permisos de les aplicacions, els controls de xarxa i les condicions del proveïdor afecten els fluxos de dades. Verifica qualsevol canvi de privadesa amb la documentació del producte i proves de la xarxa local o dels esdeveniments.

El suport estàndard de Windows 10 també va acabar el 14 d'octubre de 2025. Una instal·lació de Windows 10 sense programari innecessari encara necessita una via d'actualització compatible o una excepció aprovada del cicle de vida. Consulta l'[avís de Microsoft sobre la fi del suport de Windows 10](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).

______

En resum, reforçar Windows i eliminar-ne el programari innecessari són passos importants per millorar la seguretat i la privadesa. Si redueixes la superfície d'atac i la quantitat de dades recollides i emmagatzemades, pots protegir la informació sensible i reduir el risc d'atacs cibernètics. **Aplica aquests passos avui i mantén el sistema Windows segur i protegit**.
