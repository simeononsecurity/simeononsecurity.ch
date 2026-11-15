---
title: "Prova de restauració d’una VM Proxmox: comprova que el sistema convidat funciona"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Prova una còpia de seguretat d’una VM Proxmox amb una restauració aïllada. Comprova els discos inclosos, el mode de còpia, les dades del convidat, l’estat del servei i el temps de recuperació sense tocar la producció."
genre: ["Virtualització", "Còpia de seguretat i recuperació", "Laboratori domèstic"]
tags: ["prova de restauració Proxmox", "còpia de seguretat de VM Proxmox", "exercici de restauració Proxmox", "qmrestore", "vzdump", "verificació de Proxmox Backup Server", "còpia per snapshot Proxmox", "prova de recuperació de VM", "RPO i RTO de còpia", "restauració aïllada de VM", "mode de còpia Proxmox", "còpia amb agent convidat"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Una còpia passa d’una VM de producció taronja per un magatzem fins a una VM de prova aïllada blava. S’hi comproven discos, serveis i temps."
coverCaption: "Una tasca de còpia completada és el principi d’una prova de recuperació."
---

Una tasca de còpia verda indica que Proxmox ha escrit una còpia de seguretat. No mostra si el convidat arrenca, si les dades són recents o si el servei principal funciona. **Restaura una còpia amb un ID de VM nou en una xarxa aïllada.** El resultat aporta proves de recuperació abans que una interrupció t’obligui a fer la prova.

<!--more-->

Aquest exercici cobreix una **màquina virtual de Proxmox VE**. Els contenidors tenen unes regles de còpia diferents, sobretot per als muntatges bind i de dispositius. La [prova de còpia i restauració del laboratori domèstic](/articles/homelab-backup-restore-drill/) del lloc tracta una recuperació de fitxers més àmplia. Aquí provaràs una còpia d’una VM Proxmox i la seva càrrega de treball.

Un **convidat** és el sistema operatiu que s’executa dins d’una màquina virtual. Els **muntatges bind** i els **muntatges de dispositius** exposen recursos de l’amfitrió al convidat. Prova aquests recursos amb un pla de recuperació separat.

## Idees clau

- **Defineix primer què vol dir tenir èxit:** tria una dada, una comprovació del servei i un temps de recuperació acceptable.
- **Comprova la cobertura:** una còpia d’una VM omet els discos marcats **No backup** i no recrea serveis externs ni dades excloses.
- **Restaura per separat:** fes servir un ID de VM lliure i mantén la xarxa restaurada aïllada de producció.
- **Registra les proves:** mesura l’antiguitat de la còpia, el temps de restauració, l’arrencada, la presència dels discos i una comprovació real de l’aplicació.

## Abans de començar

Tria una VM de la qual sigui segur provar la còpia. Necessites accés d’administrador a Proxmox, una còpia completada en emmagatzematge de fitxers o a Proxmox Backup Server (PBS), prou espai per a una segona VM i un bridge aïllat o un dispositiu de xarxa desconnectat. Un bridge aïllat és una xarxa virtual de Proxmox sense ruta cap a la LAN de producció. Si no en tens, fes servir un adaptador desconnectat o una VLAN de prova. Mantén en marxa la VM de producció. Reserva un ID de VM nou, com ara **920**, després de comprovar que cap altre convidat l’utilitza. Reserva prou temps per a una restauració completa i una prova de la càrrega de treball.

Escriu els criteris d’aprovació abans de restaurar. Per a un servidor de fitxers, tria un fitxer recent i la seva suma de comprovació o el contingut esperat. Per a una base de dades, tria una consulta segura de només lectura i un registre escrit abans de la còpia. Per a un servei web, tria una comprovació local de salut i una pàgina representativa. Anota la data més recent acceptable de les dades, el teu **objectiu de punt de recuperació (RPO)**, i el temps permès per recuperar el servei, el teu **objectiu de temps de recuperació (RTO)**. Una pantalla d’arrencada per si sola no satisfà aquestes comprovacions.

| Dada registrada | Exemple de prova |
|---|---|
| **Punt de còpia** | Hora del snapshot i darrera dada esperada |
| **Objectiu de recuperació** | ID de VM lliure, emmagatzematge de destinació, bridge aïllat |
| **Prova de càrrega** | Inici de sessió, muntatge del volum i lectura de l’aplicació |
| **Límit de temps** | Hora d’inici i final de la restauració i comprovació del servei |

No connectis el convidat restaurat a la xarxa de producció abans de revisar-ne el nom, l’adreça IP, l’adreça MAC, les tasques programades i les integracions externes. Una identitat copiada podria entrar en conflicte amb la VM activa o enviar feines duplicades.

## Comprova què cobreix la còpia

**Abast de les versions:** aquests exemples no es van executar durant la preparació de l’article. Abans de provar, registra la sortida de `pveversion --verbose`. Fes servir documentació que correspongui a la versió instal·lada de Proxmox VE. Anota el backend d’emmagatzematge, el tipus de convidat i la sortida de les ordres al registre de la prova.

En un node Proxmox, l’ordre de només lectura següent mostra la configuració de la VM d’origen. Substitueix **120** per l’ID de la VM d’origen:

```bash
qm config 120
```

Llista tots els discos virtuals i la seva opció de còpia. La [documentació de Proxmox sobre discos de VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) explica que l’opció **No backup** exclou un disc de la còpia de la VM. Comprova si les dades de l’aplicació són en un disc exclòs, un muntatge de l’amfitrió, maquinari passat directament o un servei remot. Anota’n el procediment de recuperació separat. Una prova d’arrencada de la VM no demostra que les dades excloses estiguin protegides.

Comprova la marca de temps, la mida, el registre de la tasca i la ubicació d’emmagatzematge de la còpia més recent. A la interfície de Proxmox, obre la vista **Backups** de l’emmagatzematge de còpies o la pestanya **Backup** de la VM. Confirma que la tasca ha acabat sense errors. La [documentació de còpies de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) distingeix els fitxers de còpia normals de l’emmagatzematge PBS, que conserva blocs i metadades deduplicats.

| Mode de còpia | Comportament de la VM | Decisió per a aquesta prova |
|---|---|---|
| **Snapshot** | Fa una còpia d’una VM en execució amb poca interrupció. Les escriptures del convidat comporten un petit risc d’incoherència. | Adequat per a proves rutinàries si la càrrega tolera aquest punt de recuperació. |
| **Stop** | Atura el convidat quan comença la còpia i ofereix la coherència més alta. | Fes-lo servir quan la càrrega necessiti un tancament net i la interrupció sigui acceptable. |
| **Suspend** | Suspèn el convidat abans del mode snapshot i afegeix interrupció sense un benefici general de coherència. | No triïs suspend per defecte com a millora de snapshot. |

Aquestes compensacions provenen de la [referència de modes de còpia de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Un **QEMU Guest Agent** és un servei dins del convidat que permet a Proxmox demanar accions com congelar i descongelar el sistema de fitxers. Un convidat en marxa amb l’agent activat i en bon estat admet aquestes accions durant una còpia snapshot. Congelar el sistema de fitxers millora la coherència, però no substitueix una comprovació de recuperació específica de la base de dades. Anota el mode real i l’estat de l’agent en lloc de donar per fet que una tasca programada fa servir la configuració que prefereixes.

## Crea o selecciona un punt de recuperació

Fes servir una còpia programada recent i correcta si la prova tracta la recuperació habitual. Si necessites una còpia nova puntual, obre la pestanya **Backup** de la VM, tria **Backup now**, defineix l’emmagatzematge de destinació i el mode i espera que el registre de la tasca indiqui que ha acabat bé. Des d’un shell de Proxmox, aquest exemple fa una còpia de la VM **120** a l’ID d’emmagatzematge **backup-nfs** en mode snapshot:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Substitueix tots dos ID pels teus. Executa l’ordre només després de confirmar que l’emmagatzematge accepta còpies i té prou espai. La [referència de Proxmox per a `vzdump`](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) documenta les opcions de mode i emmagatzematge. Comprova el registre de la tasca quan l’ordre acabi. No tractis una còpia antiga com un punt de recuperació actual només perquè el nom del fitxer sembli recent.

Si la destinació és **PBS**, executa o inspecciona una tasca de verificació per al datastore seleccionat. La [documentació de verificació de PBS](https://pbs.proxmox.com/docs/maintenance.html) explica com verificar la integritat de les dades i programar comprovacions repetides. La verificació troba blocs de còpia malmesos. **Una verificació correcta no demostra que funcioni un sistema operatiu restaurat, una aplicació o una dependència externa.** Continua amb la prova de restauració encara que la verificació sigui correcta.

## Restaura en una VM aïllada

A la interfície de Proxmox, selecciona la còpia a la vista **Backups** de l’emmagatzematge i tria **Restore**. Introdueix un ID de VM lliure i l’emmagatzematge de destinació previst. Deixa desactivat **Start after restore**. Revisa l’opció per generar una adreça MAC nova. La [sinopsi oficial de `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) defineix un ID de VM únic, la selecció de l’emmagatzematge, `--unique` per generar una adreça Ethernet aleatòria i el comportament per defecte de no iniciar la VM restaurada.

Per a un arxiu `vzdump` basat en fitxer, aquesta ordre de shell mostra el patró equivalent. Substitueix la ruta de l’arxiu, el nou ID de VM i l’ID d’emmagatzematge pels valors del teu entorn:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

La [descripció de restauració de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) diu que, sense emmagatzematge de destinació, la restauració prova d’utilitzar l’emmagatzematge original. Defineix **`--storage`** si l’emmagatzematge antic no existeix al node de prova. No facis servir **`--force`** en una prova. L’opció permet sobreescriure una VM existent, mentre que aquest procediment exigeix un ID lliure. Les còpies PBS també es restauren des de la interfície de Proxmox. Selecciona l’entrada d’emmagatzematge del snapshot de PBS en lloc de tractar-lo com un fitxer `.vma.zst` local.

Abans del primer arrencament, inspecciona totes les interfícies de xarxa restaurades, incloses les secundàries i les passades directament. Una **adreça MAC** identifica una interfície de xarxa. **DNS** associa noms amb adreces. **DHCP** assigna la configuració de xarxa. Una **VLAN** és una xarxa lògica transportada per maquinari compartit. Un **TPM virtual** desa l’estat de seguretat del convidat. Desconnecta totes les interfícies o connecta-les només a un segment de prova aïllat. Confirma que no es pugui accedir a cap ruta de producció, ruta DNS, servei DHCP, xarxa de gestió o integració externa. Si la càrrega necessita un altre servei de prova, prepara’n una còpia a la xarxa aïllada. Compara amb l’origen les assignacions de disc, el firmware, els requisits del TPM virtual i els dispositius especials. Els discos externs, els dispositius passats directament i els secrets desats fora de la VM necessiten plans separats.

## Prova el convidat i la càrrega de treball

Inicia la VM restaurada i fes servir primer la consola. Comprova que el sistema operatiu arrenca, que es munten tots els volums esperats, que el rellotge és correcte i que l’aplicació s’inicia. Després executa el criteri d’aprovació que havies escrit. Compara una dada coneguda amb el valor i la marca de temps anteriors a la còpia. Una pantalla d’inici de sessió o un procés en execució no demostra, per si sol, que el servei tingui les dades correctes.

| Prova | Criteri d’aprovació |
|---|---|
| **Arrencada** | El convidat arriba a una sessió normal sense mode de reparació ni sol·licituds de recuperació repetides. |
| **Discos** | Tots els discos inclosos a la còpia apareixen, es munten i contenen les dades esperades. |
| **Servei** | Una petició local representativa o una lectura funciona. |
| **Punt de recuperació** | Les dades restaurades compleixen l’RPO registrat. |
| **Temps de recuperació** | La restauració, l’arrencada i la validació del servei compleixen l’RTO registrat. |
| **Aïllament** | Cap adreça, tasca o integració de producció rep trànsit duplicat. |

Mantén aïllat el convidat restaurat mentre revises les tasques programades, els hooks de notificació, els agents de còpia i les credencials de l’aplicació. No facis cap prova que enviï missatges reals a clients o escrigui en serveis de producció. Si falla una comprovació, anota l’etapa exacta. Distingeix **error d’integritat de la còpia**, **error d’arrencada de la VM**, **dades que falten** i **error de l’aplicació**. Cadascun requereix una correcció diferent.

| Tipus d’error | Prova de confirmació | Primera correcció | Nova prova |
|---|---|---|---|
| **Integritat de la còpia** | La tasca de verificació o restauració informa de dades malmeses | Tria un altre punt de recuperació verificat i revisa l’estat de l’emmagatzematge | Repeteix la verificació i la restauració |
| **Arrencada de la VM** | La consola mostra errors de firmware, disc o recuperació | Compara firmware, assignació de disc i ordre d’arrencada amb l’origen | Arrenca la còpia aïllada i registra el resultat de la consola |
| **Dades que falten** | No hi ha el fitxer, volum o registre esperat | Revisa discos exclosos, muntatges, snapshots i dependències externes | Repeteix la comprovació del fitxer o dada indicats |
| **Aplicació** | El convidat arrenca, però falla la comprovació del servei | Revisa els registres del servei, les credencials, les dependències i els passos de recuperació | Torna a executar la mateixa comprovació local de salut i la prova de càrrega |

Proxmox ofereix la [restauració de fitxers individuals per a còpies PBS](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Fes-la servir per provar una ruta de recuperació de fitxers si la càrrega ho necessita. Un fitxer recuperat no substitueix l’arrencada completa de la VM ni la prova del servei. Proxmox també ofereix restauració en viu des de PBS. La documentació indica que una restauració en viu fallida deixa la VM en un estat indefinit. Per a aquesta prova planificada, fes servir una restauració normal completada.

## Registra el resultat i tanca la prova

Registra l’ID de la VM d’origen, l’emmagatzematge de la còpia, la marca de temps, el mode, el nou ID de VM, l’emmagatzematge de destinació, l’aïllament de xarxa, les hores d’inici i final de la restauració, la prova de l’aplicació, la marca de temps de les dades i les comprovacions fallides. Compara el punt i el temps de recuperació mesurats amb els objectius. Un error només aporta proves útils si canvies el pla de còpies i repeteixes la prova.

Atura la VM restaurada quan acabi la prova. Elimina’n la còpia de prova només després de desar el resultat i comprova que la VM de producció continuï funcionant com s’espera. Conserva la còpia segons la política de retenció habitual. No canviïs la retenció només per superar una prova.

Repeteix la prova després de canvis importants a l’emmagatzematge, al convidat o a la configuració de còpies. Alterna les VM importants, incloses les que tenen discos exclosos o dependències externes. La [guia de migració d’Hyper-V a Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) fa servir aquesta prova abans de retirar una VM d’origen. **Una còpia útil té una ruta de restauració coneguda, una càrrega provada i un punt de recuperació mesurat.**

## Passos següents

Repeteix l’exercici després de canvis a l’emmagatzematge, al convidat o a les còpies. Consulta la [prova de còpia i restauració del laboratori domèstic](/articles/homelab-backup-restore-drill/) per recuperar fitxers.
