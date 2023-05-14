---
title: "Protejați Windows de atacurile pe canale laterale de execuție speculativă"
date: 2020-06-18
toc: true
draft: false
description: "Aflați cum să vă protejați sistemul Windows împotriva atacurilor de execuție speculative pe canalul lateral cu scriptul de atenuare Microsoft și actualizările de firmware"
tags: ["Windows Spectre Meltdown Mitigation Script", "Execuție speculativă Atacurile pe canalul lateral", "Microsoft", "Intel", "AMD", "PRIN INTERMEDIUL", "BRAŢ", "Android", "Crom", "iOS", "macOS", "Injecție țintă de ramură", "Bounds Check Bypass", "Încărcare cache de date necinstite", "Ocolire speculativă a magazinului", "Eșantionarea datelor microarhitecturale", "CVE-uri", "Actualizări de firmware", "Depozitul GitHub", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Script simplu pentru a implementa protecții împotriva vulnerabilităților de execuție speculativă ale canalului lateral în sistemele Windows.**

Microsoft este conștient de o nouă clasă de vulnerabilități dezvăluite public care se numesc „atacuri pe canalul lateral de execuție speculativă” și care afectează multe procesoare moderne, inclusiv Intel, AMD, VIA și ARM.

**Notă:** Această problemă afectează și alte sisteme de operare, cum ar fi Android, Chrome, iOS și macOS. Prin urmare, sfătuim clienții să caute îndrumări de la acești furnizori.

Am lansat mai multe actualizări pentru a ajuta la atenuarea acestor vulnerabilități. De asemenea, am luat măsuri pentru a ne securiza serviciile cloud. Consultați secțiunile următoare pentru mai multe detalii.

Nu am primit încă nicio informație care să indice că aceste vulnerabilități au fost folosite pentru a ataca clienții. Lucrăm îndeaproape cu parteneri din industrie, inclusiv producători de cipuri, producători de hardware și furnizori de aplicații pentru a proteja clienții. Pentru a obține toate protecțiile disponibile, sunt necesare actualizări de firmware (microcod) și software. Aceasta include microcodul de la OEM-urile dispozitivelor și, în unele cazuri, actualizări ale software-ului antivirus.

**Acest articol abordează următoarele vulnerabilități:**
- CVE-2017-5715 – „Injecție țintă de sucursală”
- CVE-2017-5753 – „Bounds Check Bypass”
- CVE-2017-5754 – „Încărcare cache de date necinstite”
- CVE-2018-3639 – „Ocolirea magazinului speculativ”
- CVE-2018-11091 – „Microarchitectural Data Sampling Uncacheable Memory (MDSUM)”
- CVE-2018-12126 – „Eșantionarea datelor tampon de stocare microarhitecturale (MSBDS)”
- CVE-2018-12127 – „Eșantionarea datelor tampon de umplere microarhitecturală (MFBDS)”
- CVE-2018-12130 – „Eșantionarea datelor portului de încărcare microarhitecturală (MLPDS)”

**ACTUALIZAT ÎN 6 AUGUST 2019** Pe 6 august 2019, Intel a lansat detalii despre o vulnerabilitate de divulgare a informațiilor nucleului Windows. Această vulnerabilitate este o variantă a vulnerabilității de canal lateral de execuție speculativă Spectre Variant 1 și i s-a atribuit CVE-2019-1125.

**ACTUALIZAT ÎN 12 NOIEMBRIE 2019** Pe 12 noiembrie 2019, Intel a publicat un aviz tehnic despre vulnerabilitatea Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort căreia îi este atribuită CVE-2019-11135. Microsoft a lansat actualizări pentru a ajuta la atenuarea acestei vulnerabilități, iar protecțiile sistemului de operare sunt activate în mod implicit pentru edițiile Windows Client OS.

## Acțiuni recomandate
Clienții ar trebui să ia următoarele măsuri pentru a ajuta la protejarea împotriva vulnerabilităților:

- Aplicați toate actualizările disponibile ale sistemului de operare Windows, inclusiv actualizările lunare de securitate Windows.
- Aplicați actualizarea firmware-ului aplicabilă (microcod) furnizată de producătorul dispozitivului.
- Evaluați riscul pentru mediul dvs. pe baza informațiilor furnizate în avizele de securitate Microsoft: ADV180002, ADV180012, ADV190013 și a informațiilor furnizate în acest articol din baza de cunoștințe.
- Luați măsuri după cum este necesar utilizând avizele și informațiile cheie de registry care sunt furnizate în acest articol din baza de cunoștințe.

## Descărcați fișierele necesare:

Descărcați fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Cum se rulează scriptul:

**Scriptul poate fi lansat din descărcarea GitHub extrasă astfel:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
