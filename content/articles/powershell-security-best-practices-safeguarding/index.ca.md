---
title: "10 bones pràctiques de seguretat de PowerShell per protegir els scripts"
date: 2023-07-25
lastmod: 2026-11-25
toc: true
draft: false
description: "Protegeix els scripts i les sessions de PowerShell amb controls d'execució, signatura de codi, gestió segura dels secrets, límits d'accés i registre."
genre: ["Bones pràctiques de seguretat de PowerShell", "Seguretat dels scripts", "Seguretat de les contrasenyes", "Seguretat informàtica", "Ciberseguretat", "Administració de Windows", "Automatització", "Programació segura", "Seguretat de xarxes", "Protecció de dades"]
tags: ["Bones pràctiques de seguretat de PowerShell", "Bones pràctiques per protegir les contrasenyes a PowerShell", "Bones pràctiques per protegir i utilitzar PowerShell", "Política d'execució de scripts", "Signatura de codi", "Control d'accés dels usuaris", "Seguretat de les contrasenyes", "Contrasenyes escrites al codi", "Contrasenyes segures", "Polítiques de canvi de contrasenyes", "Protecció dels scripts de PowerShell", "Protecció de contrasenyes a PowerShell", "Gestió de l'execució de scripts a PowerShell", "Protecció d'informació confidencial a PowerShell", "Millora de la seguretat de PowerShell"]
cover: "/img/cover/A_symbolic_illustration_showing_a_shield_prot.webp"
coverAlt: "Il·lustració simbòlica d'un escut que protegeix un script de PowerShell."
coverCaption: "Protegeix els scripts de PowerShell amb pràctiques de seguretat eficaces."
---

## Introducció

PowerShell és un llenguatge de scripting i un marc d'automatització potent desenvolupat per Microsoft. Ofereix moltes funcions perquè els administradors i desenvolupadors gestionin i automatitzin entorns Windows. Però, com passa amb qualsevol eina potent, cal seguir les **bones pràctiques de seguretat de PowerShell** per impedir-hi l'accés no autoritzat, protegir la informació confidencial i reduir el risc d'incidents de seguretat.

En aquest article analitzarem les [**bones pràctiques de seguretat de PowerShell**](https://simeononsecurity.com/articles/secure-coding-standards-for-powershell/), centrades en la seguretat dels scripts i les contrasenyes. Aplicar-les t'ajudarà a protegir els scripts i les contrasenyes de PowerShell i a reduir la possibilitat d'activitats malicioses i de filtracions de dades.

## Entendre la seguretat de PowerShell

La seguretat de PowerShell consisteix a protegir els scripts, gestionar els controls d'accés i protegir informació confidencial, com ara contrasenyes i credencials. Les bones pràctiques de seguretat de PowerShell cobreixen diversos àmbits clau, com ara **l'execució de scripts**, **la signatura de codi**, **el control d'accés dels usuaris** i **la gestió de contrasenyes**.

## Bones pràctiques per executar scripts

Pel que fa a **l'execució de scripts**, segueix aquestes pràctiques:

1. **Activa la política d'execució de scripts**: PowerShell té una política d'execució que controla quins tipus de scripts es poden executar en un sistema. Configurar-la en mode restringit o RemoteSigned ajuda a impedir l'execució de scripts maliciosos. Utilitza el cmdlet `Set-ExecutionPolicy` per configurar-la.

2. **Signa els scripts**: La signatura de codi afegeix una capa de seguretat que verifica la integritat i l'autenticitat dels scripts. Si els signes amb un certificat digital, pots comprovar que no s'han modificat i que provenen d'una font de confiança. Per exemple, pots utilitzar el cmdlet **Sign-Script** per signar scripts de PowerShell.

3. **Activa el registre dels scripts**: Activa el registre per fer un seguiment de l'execució dels scripts de PowerShell. El registre ajuda a identificar possibles incidents de seguretat, detectar activitats no autoritzades i investigar vulneracions. PowerShell inclou el cmdlet `Start-Transcript` per registrar l'activitat dels scripts. Amb aquest cmdlet pots desar la sortida dels scripts, inclosos els errors i els avisos, en un fitxer de registre per analitzar-la més endavant.

Aquestes pràctiques d'execució de scripts reforcen la seguretat de l'entorn PowerShell i ajuden a impedir que s'executin scripts maliciosos o no autoritzats.

## Bones pràctiques per signar codi

La signatura de codi té un paper important a l'hora de garantir la integritat i l'autenticitat dels scripts de PowerShell. Segueix aquestes pràctiques:

1. **Obtén un certificat de signatura de codi**: Adquireix un certificat de signatura de codi d'una autoritat de certificació (CA) de confiança per signar els scripts. El certificat confirma que provenen d'una font de confiança i que no s'han modificat. Per exemple, pots obtenir un certificat de signatura de codi de **DigiCert** o **GlobalSign**.

2. **Signa tots els scripts**: Signa tots els scripts de PowerShell, inclosos els d'ús intern. Això estableix una pràctica de seguretat coherent i impedeix que s'executin scripts no autoritzats o modificats. Per signar-ne un, utilitza el cmdlet **Set-AuthenticodeSignature** i indica el camí del certificat de signatura de codi.

3. **Verifica els certificats de signatura de codi**: Abans d'executar un script signat, verifica el certificat utilitzat per signar-lo. PowerShell inclou el cmdlet `Get-AuthenticodeSignature` per comprovar-ne la signatura i validar-ne l'autenticitat. Utilitza'l per confirmar que l'script que vols executar està signat per una font de confiança.

Aquestes pràctiques reforcen la seguretat dels scripts de PowerShell i ajuden a garantir que provenen d'una font de confiança i que no s'han modificat.

## Bones pràctiques per controlar l'accés dels usuaris

El control d'accés dels usuaris és essencial per gestionar qui pot executar scripts de PowerShell i fer tasques administratives. Tingues en compte aquestes pràctiques:

1. **Limita els privilegis administratius**: Restringeix els privilegis administratius als usuaris que els necessiten. Aplicar el principi de privilegis mínims redueix el risc d'execucions no autoritzades de scripts i de danys accidentals. Per exemple, concedeix privilegis administratius només als comptes que els necessitin, com els dels administradors informàtics o de sistemes.

2. **Implementa el control d'accés basat en rols (RBAC)**: RBAC permet definir rols específics i assignar-hi usuaris segons les seves responsabilitats. Així, cada usuari només té accés a les funcions de PowerShell que necessita per fer la seva feina. Per exemple, pots crear rols com ara «Usuari de PowerShell» i «Administrador de PowerShell» i assignar-hi els usuaris corresponents.

3. **Revisa periòdicament els permisos dels usuaris**: Revisa i audita els permisos dels usuaris de manera periòdica per comprovar que els drets d'accés s'ajusten a les necessitats actuals. Elimina els permisos innecessaris per reduir la superfície d'atac i els possibles riscos de seguretat. Revisar i actualitzar els permisos sovint ajuda a evitar que els usuaris tinguin més privilegis dels necessaris. PowerShell inclou cmdlets com ara `Get-Acl` i `Set-Acl` per gestionar i auditar els permisos.

Aplicar aquestes pràctiques de control d'accés redueix el risc d'accés no autoritzat i ajuda a mantenir segur l'entorn PowerShell.

## Bones pràctiques per protegir les contrasenyes

Les contrasenyes són un aspecte essencial de la seguretat de PowerShell, sobretot quan es gestionen credencials i autenticació. Segueix aquestes pràctiques per reforçar la **seguretat de les contrasenyes**:

1. **Evita escriure contrasenyes directament al codi**: En lloc d'incloure contrasenyes als scripts, considera altres mètodes d'autenticació, com ara **Windows Credential Manager** o **Azure Key Vault**. Aquestes solucions permeten desar i recuperar contrasenyes de manera segura sense exposar-les en text clar. Per exemple, pots utilitzar els cmdlets del **Credential Manager** de PowerShell per interactuar amb Windows Credential Manager.

2. **Utilitza contrasenyes segures i complexes**: Assegura't que les contrasenyes dels comptes administratius o de servei siguin segures i complexes. Fomenta la combinació de lletres majúscules i minúscules, números i caràcters especials. Evita les contrasenyes habituals i els patrons previsibles. Considera utilitzar un **gestor de contrasenyes** per generar i desar contrasenyes segures.

3. **Aplica polítiques de canvi de contrasenyes**: Exigeix que els comptes de servei i els usuaris amb privilegis canviïn les contrasenyes periòdicament. Canviar-les sovint redueix el risc que les credencials quedin compromeses i que s'hi accedeixi sense autorització. Per exemple, estableix una política que exigeixi canviar cada 90 dies les contrasenyes dels comptes amb privilegis.

Aquestes pràctiques reforcen la seguretat de l'entorn PowerShell i ajuden a protegir-lo de l'accés no autoritzat i de les filtracions de dades.

______

## Conclusió

Protegir els scripts i les contrasenyes de PowerShell és essencial per mantenir la integritat i la confidencialitat dels sistemes. Si segueixes les **bones pràctiques de seguretat de PowerShell**, com ara activar la política d'execució de scripts, signar el codi, controlar l'accés dels usuaris i protegir les contrasenyes, pots millorar considerablement la seguretat de l'entorn PowerShell.

Recorda que la seguretat de PowerShell és un procés continu. Mantén-te al dia de les recomanacions i directrius de seguretat més recents de Microsoft i de les normatives governamentals pertinents, com ara el **marc de ciberseguretat del NIST** i la **norma ISO/IEC 27001**. Aquests marcs ofereixen orientacions útils perquè les organitzacions estableixin i mantinguin pràctiques eficaces de ciberseguretat.

Si apliques aquestes pràctiques i et mantens alerta, pots reduir els riscos de l'ús de scripts de PowerShell i protegir els sistemes i la informació confidencial. Informa't de les novetats, revisa i actualitza periòdicament les mesures de seguretat i protegeix proactivament l'entorn PowerShell.

## Referències

- [Documentació de Microsoft PowerShell](https://docs.microsoft.com/powershell/)
- [Marc de ciberseguretat del NIST](https://www.nist.gov/cyberframework)
- [Gestió de la seguretat de la informació segons la ISO/IEC 27001](https://www.iso.org/isoiec-27001-information-security.html)
