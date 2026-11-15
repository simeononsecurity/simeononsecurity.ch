---
title: "Test de restaurare a unei VM Proxmox: verifică dacă sistemul invitat funcționează"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Testează o copie de siguranță a unei VM Proxmox printr-o restaurare izolată. Verifică discurile incluse, modul de backup, datele invitatului, starea serviciului și timpul de recuperare fără să atingi producția."
genre: ["Virtualizare", "Copie de siguranță și recuperare", "Laborator de acasă"]
tags: ["test de restaurare Proxmox", "copie de siguranță VM Proxmox", "exercițiu de restaurare Proxmox", "qmrestore", "vzdump", "verificarea Proxmox Backup Server", "backup snapshot Proxmox", "test de recuperare VM", "RPO și RTO pentru backup", "restaurare VM izolată", "mod de backup Proxmox", "backup cu agent invitat"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "O copie de siguranță trece de la o VM de producție portocalie printr-un seif de stocare la o VM de test izolată, albastră. Sunt verificate discurile, serviciile și durata."
coverCaption: "Finalizarea unei sarcini de backup este începutul unui test de recuperare."
---

O sarcină de backup verde arată că Proxmox a scris o copie de siguranță. Nu arată dacă invitatul pornește, dacă datele sunt recente sau dacă funcționează serviciul principal. **Restaurează o copie cu un ID nou de VM într-o rețea izolată.** Rezultatul oferă dovezi despre recuperare înainte ca o întrerupere să te oblige să faci testul.

<!--more-->

Acest exercițiu acoperă o **mașină virtuală Proxmox VE**. Containerele au alte reguli de backup, mai ales pentru montări bind și montări de dispozitive. [Testul de backup și restaurare pentru laboratorul de acasă](/articles/homelab-backup-restore-drill/) de pe site acoperă recuperarea mai amplă a fișierelor. Aici vei testa o copie Proxmox a unei VM și sarcina ei de lucru.

Un **invitat** este sistemul de operare care rulează într-o mașină virtuală. **Montările bind** și **montările de dispozitive** expun resursele gazdei către invitat. Testează aceste resurse printr-un plan de recuperare separat.

## Idei principale

- **Definește mai întâi succesul:** alege un element de date, o verificare a serviciului și un timp de recuperare acceptabil.
- **Verifică acoperirea:** copia unei VM omite discurile marcate **No backup** și nu recreează servicii externe sau date excluse.
- **Restaurează separat:** folosește un ID de VM neutilizat și păstrează rețeaua restaurată izolată de producție.
- **Înregistrează dovezile:** măsoară vechimea copiei, timpul de restaurare, pornirea, prezența discurilor și o verificare reală a aplicației.

## Înainte să începi

Alege o VM a cărei copie poate fi testată în siguranță. Ai nevoie de acces de administrator la Proxmox, o copie completă pe un sistem de fișiere sau pe Proxmox Backup Server (PBS), spațiu suficient pentru o a doua VM și un bridge izolat sau un dispozitiv de rețea deconectat. Un bridge izolat este o rețea virtuală Proxmox fără rută către LAN-ul de producție. Dacă nu ai unul, folosește un adaptor deconectat sau un VLAN de test. Lasă VM-ul de producție pornit. Rezervă un ID nou pentru VM, de exemplu **920**, după ce verifici dacă alt invitat îl folosește. Alocă suficient timp pentru o restaurare completă și un test al sarcinii de lucru.

Scrie criteriile de reușită înainte de restaurare. Pentru un server de fișiere, alege un fișier recent și suma de control sau conținutul așteptat. Pentru o bază de date, alege o interogare sigură numai pentru citire și o înregistrare scrisă înainte de copie. Pentru un serviciu web, alege o verificare locală de sănătate și o pagină reprezentativă. Notează cea mai recentă dată acceptabilă a datelor, **obiectivul punctului de recuperare (RPO)**, și timpul permis pentru reluarea serviciului, **obiectivul timpului de recuperare (RTO)**. Un ecran de pornire nu îndeplinește singur aceste verificări.

| Element înregistrat | Exemplu de dovadă |
|---|---|
| **Punctul copiei** | Ora snapshotului și ultimul element de date așteptat |
| **Ținta recuperării** | ID de VM neutilizat, spațiu de stocare țintă, bridge izolat |
| **Testul sarcinii** | Autentificare, montare de volum și citire din aplicație |
| **Limită de timp** | Ora de început și de sfârșit a restaurării și verificării serviciului |

Nu conecta invitatul restaurat la rețeaua de producție înainte să-i verifici numele, adresa IP, adresa MAC, sarcinile programate și integrările externe. O identitate copiată poate intra în conflict cu VM-ul activ sau poate trimite sarcini duplicate.

## Verifică ce acoperă copia

**Domeniul versiunilor:** aceste exemple nu au fost executate în timpul pregătirii articolului. Înregistrează rezultatul `pveversion --verbose` înainte de test. Folosește documentația corespunzătoare versiunii Proxmox VE instalate. Notează backendul de stocare, tipul invitatului și rezultatul comenzilor în raportul exercițiului.

Pe un nod Proxmox, următoarea comandă numai pentru citire afișează configurația VM-ului sursă. Înlocuiește **120** cu ID-ul VM-ului sursă:

```bash
qm config 120
```

Listează fiecare disc virtual și setarea lui de backup. [Documentația Proxmox despre discurile VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) precizează că opțiunea **No backup** exclude un disc din copia VM. Verifică dacă datele aplicației se află pe un disc exclus, o montare a gazdei, hardware transmis direct sau un serviciu la distanță. Notează procedura separată de recuperare. Un test de pornire a VM-ului nu dovedește protejarea datelor excluse.

Verifică marcajul temporal, dimensiunea, jurnalul sarcinii și locația de stocare a celei mai recente copii. În interfața Proxmox, deschide vizualizarea **Backups** a spațiului de stocare pentru copii sau fila **Backup** a VM-ului. Confirmă că sarcina s-a încheiat fără erori. [Documentația Proxmox despre backup](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) diferențiază fișierele obișnuite de backup de stocarea PBS, care păstrează blocuri și metadate deduplicate.

| Mod de backup | Comportamentul VM-ului | Decizia pentru acest exercițiu |
|---|---|---|
| **Snapshot** | Face backup unei VM pornite cu întrerupere redusă. Scrierile invitatului implică un risc mic de inconsistență. | Potrivit pentru teste obișnuite dacă sarcina tolerează acest punct de recuperare. |
| **Stop** | Oprește invitatul la începutul backupului și oferă cea mai bună consistență. | Folosește-l când sarcina cere o oprire curată și timpul de nefuncționare este acceptabil. |
| **Suspend** | Suspendă invitatul înainte de modul snapshot și adaugă întrerupere fără un beneficiu general de consistență. | Nu alege suspend implicit ca îmbunătățire față de snapshot. |

Aceste compromisuri sunt descrise în [referința Proxmox pentru modurile de backup](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Un **QEMU Guest Agent** este un serviciu din invitat care permite Proxmox să solicite acțiuni precum înghețarea și dezghețarea sistemului de fișiere. Un invitat pornit, cu agentul activat și funcțional, acceptă aceste acțiuni în timpul backupului snapshot. Înghețarea sistemului de fișiere îmbunătățește consistența, dar nu înlocuiește verificarea recuperării specifice bazei de date. Notează modul real și starea agentului în loc să presupui că o sarcină programată folosește setările preferate.

## Creează sau selectează un punct de recuperare

Folosește o copie programată recentă și reușită dacă exercițiul testează recuperarea obișnuită. Dacă ai nevoie de o copie nouă, unică, deschide fila **Backup** a VM-ului, alege **Backup now**, setează spațiul de stocare țintă și modul și așteaptă ca jurnalul sarcinii să indice succesul. Dintr-un shell Proxmox, exemplul face backup VM-ului **120** în spațiul cu ID-ul **backup-nfs**, în modul snapshot:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Înlocuiește ambele ID-uri cu ale tale. Execută comanda numai după ce confirmi că spațiul de stocare acceptă copii și are destul loc. [Referința Proxmox pentru `vzdump`](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) documentează opțiunile de mod și stocare. Verifică jurnalul sarcinii după terminarea comenzii. Nu considera o copie veche drept punct actual de recuperare doar pentru că numele fișierului pare recent.

Dacă ținta este **PBS**, rulează sau inspectează o sarcină de verificare pentru depozitul de date ales. [Documentația PBS despre verificare](https://pbs.proxmox.com/docs/maintenance.html) explică verificarea integrității datelor de backup și programarea controalelor repetate. Verificarea găsește blocurile de backup deteriorate. **O verificare reușită nu dovedește că funcționează un sistem de operare restaurat, o aplicație sau o dependență externă.** Continuă exercițiul de restaurare chiar și după un rezultat bun.

## Restaurează pe o VM izolată

În interfața Proxmox, selectează copia din vizualizarea **Backups** a spațiului și alege **Restore**. Introdu un ID de VM neutilizat și spațiul de stocare țintă dorit. Lasă **Start after restore** dezactivat. Verifică opțiunea de generare a unei adrese MAC noi. [Sintaxa oficială `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) definește un ID unic de VM, alegerea stocării, `--unique` pentru o adresă Ethernet aleatorie și comportamentul implicit care nu pornește VM-ul restaurat.

Pentru o arhivă `vzdump` bazată pe fișier, această comandă shell arată modelul echivalent. Înlocuiește calea arhivei, noul ID de VM și ID-ul stocării cu valorile mediului tău:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

[Descrierea Proxmox despre restaurare](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) spune că restaurarea fără o stocare țintă încearcă să folosească stocarea originală. Setează **`--storage`** dacă stocarea veche nu există pe nodul de test. Nu folosi **`--force`** pentru un exercițiu. Opțiunea permite suprascrierea unei VM existente, iar procedura cere un ID neutilizat. Copiile PBS se restaurează și prin interfața Proxmox. Selectează intrarea de stocare a snapshotului PBS, nu trata snapshotul ca pe un fișier local `.vma.zst`.

Înainte de prima pornire, verifică fiecare interfață de rețea restaurată, inclusiv interfețele secundare și transmise direct. O **adresă MAC** identifică o interfață de rețea. **DNS** asociază numele cu adresele. **DHCP** atribuie setările de rețea. Un **VLAN** este o rețea logică transportată prin hardware partajat. Un **TPM virtual** păstrează starea de securitate a invitatului. Deconectează fiecare interfață sau conecteaz-o numai la un segment de test izolat. Confirmă că nu mai este accesibilă nicio rută de producție, cale DNS, serviciu DHCP, rețea de administrare sau integrare externă. Dacă sarcina are nevoie de alt serviciu de test, furnizează o copie pe rețeaua izolată. Compară cu sursa mapările discurilor, firmware-ul, cerințele TPM-ului virtual și dispozitivele speciale. Discurile externe, dispozitivele transmise direct și secretele păstrate în afara VM-ului necesită planuri separate.

## Testează invitatul și sarcina de lucru

Pornește VM-ul restaurat și folosește mai întâi consola. Confirmă că sistemul de operare pornește, toate volumele așteptate sunt montate, ceasul este corect și aplicația pornește. Apoi rulează criteriul de reușită stabilit anterior. Compară un element de date cunoscut cu valoarea și marcajul temporal de dinaintea backupului. Un ecran de autentificare sau un proces activ nu arată singur că serviciul conține datele corecte.

| Test | Condiție de reușită |
|---|---|
| **Pornire** | Invitatul ajunge la o autentificare normală fără mod de reparare sau solicitări repetate de recuperare. |
| **Discuri** | Fiecare disc inclus în copie apare, se montează și conține datele așteptate. |
| **Serviciu** | O solicitare locală reprezentativă sau o citire reușește. |
| **Punct de recuperare** | Datele restaurate respectă RPO-ul înregistrat. |
| **Timp de recuperare** | Restaurarea, pornirea și validarea serviciului respectă RTO-ul înregistrat. |
| **Izolare** | Nicio adresă, sarcină sau integrare de producție nu primește trafic duplicat. |

Păstrează invitatul restaurat izolat cât timp verifici sarcinile programate, hookurile de notificare, agenții de backup și acreditările aplicației. Nu rula un test care trimite mesaje reale clienților sau scrie în servicii de producție. Dacă o verificare eșuează, notează etapa exactă. Separă **eșecul integrității copiei**, **eșecul pornirii VM-ului**, **datele lipsă** și **eșecul aplicației**. Fiecare indică altă remediere.

| Categoria erorii | Dovada confirmării | Prima corecție | Retestare |
|---|---|---|---|
| **Integritatea copiei** | Sarcina de verificare sau restaurare raportează date deteriorate | Alege alt punct de recuperare verificat și controlează starea stocării | Repetă verificarea și restaurarea |
| **Pornirea VM-ului** | Consola afișează erori de firmware, disc sau recuperare | Compară firmware-ul, maparea discurilor și ordinea de pornire cu sursa | Pornește copia izolată și notează rezultatul consolei |
| **Date lipsă** | Lipsește fișierul, volumul sau înregistrarea așteptată | Verifică discurile excluse, montările, snapshoturile și dependențele externe | Repetă verificarea fișierului sau datelor indicate |
| **Aplicație** | Invitatul pornește, dar verificarea serviciului eșuează | Controlează jurnalele serviciului, acreditările, dependențele și pașii de recuperare | Rulează aceeași verificare locală și același test al sarcinii |

Proxmox oferă [restaurarea unui singur fișier pentru copiile PBS](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Folosește-o ca să testezi o cale de recuperare a fișierelor dacă sarcina ta are nevoie de una. Un fișier recuperat nu înlocuiește pornirea completă a VM-ului și testul serviciului. Proxmox oferă și restaurare live din PBS. Documentația spune că un eșec al restaurării live lasă VM-ul într-o stare nedefinită. Pentru acest exercițiu planificat, folosește o restaurare normală și completă.

## Înregistrează rezultatul și încheie exercițiul

Înregistrează ID-ul VM-ului sursă, stocarea copiei, marcajul temporal al backupului, modul, noul ID de VM, stocarea țintă, izolarea rețelei, orele de început și de sfârșit ale restaurării, testul aplicației, marcajul temporal al datelor și verificările eșuate. Compară punctul și timpul de recuperare măsurate cu obiectivele. Un eșec oferă dovezi utile numai dacă modifici planul de backup și repeți exercițiul.

Oprește VM-ul restaurat când testarea se termină. Șterge copia de test numai după ce ai salvat rezultatul și ai verificat că VM-ul de producție funcționează în continuare cum trebuie. Păstrează copia după politica obișnuită de retenție. Nu schimba retenția doar pentru ca un exercițiu să reușească.

Repetă testul după modificări majore ale stocării, invitatului sau configurației de backup. Alternează VM-urile importante, inclusiv invitații cu discuri excluse sau dependențe externe. [Ghidul de migrare de la Hyper-V la Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) folosește această dovadă de recuperare înainte de retragerea unei VM sursă. **O copie de siguranță utilă are o cale de restaurare cunoscută, o sarcină testată și un punct de recuperare măsurat.**

## Pașii următori

Repetă exercițiul după modificări ale stocării, invitatului sau backupului. Consultă [testul de backup și restaurare pentru laboratorul de acasă](/articles/homelab-backup-restore-drill/) pentru recuperarea fișierelor.
