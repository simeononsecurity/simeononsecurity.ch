---
title: "Thunderbird 153.6: Expunerea datelor de autentificare NTLM în Windows și actualizarea (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Două vulnerabilități grave din Thunderbird pot expune datele de autentificare NTLM din Windows la afișarea unui e-mail special conceput. Află cum funcționează cele două căi, verifică versiunea și limitează traficul SMB de ieșire în timpul actualizării."
genre: ["Securitate cibernetică", "Securitatea e-mailului", "Securitatea Windows"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "actualizare de securitate Thunderbird", "vulnerabilitate Thunderbird în Windows", "expunere NTLM Thunderbird", "autentificare SMB Thunderbird", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "atașament cu cheie OpenPGP", "atașament extern", "blocarea conținutului la distanță", "URL mailbox", "cale UNC cu lungime extinsă", "numele contului Windows", "date de autentificare NTLM", "expunerea acreditărilor SMB", "SMB de ieșire", "portul TCP 445", "securitatea e-mailului", "client de e-mail Windows", "verificarea versiunii Thunderbird", "actualizare Thunderbird", "releu NTLM", "spargerea offline a parolelor"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla a remediat două **vulnerabilități grave care expuneau datele de autentificare Windows** în Thunderbird 153.6. Afișarea unui e-mail creat cu rea intenție putea declanșa una dintre solicitările de rețea descrise în [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). Buletinul descrie o posibilă expunere a datelor NTLM, nu compromiterea confirmată a datelor fiecărui destinatar.

<!--more-->

## Idei principale

- **CVE-2026-118174** implica un atașament cu cheie OpenPGP găzduit extern. Afișarea mesajului declanșa o solicitare fără intervenția utilizatorului, chiar și când conținutul la distanță era blocat.
- **CVE-2026-118176** implica un URL `mailbox:` special formatat, care folosea o cale UNC cu lungime extinsă. Afișarea mesajului declanșa o conexiune SMB la un server ales de expeditor.
- **Actualizează Thunderbird pe Windows** și verifică versiunea instalată. Buletinul indică Thunderbird 153.6 ca versiune remediată. Notele de lansare Thunderbird identifică versiunea ESR corespunzătoare, 153.6.0esr.

## Ce declanșează e-mailul

**Cele două vulnerabilități au puncte de intrare diferite.** Conform descrierilor Mozilla, în niciun caz destinatarul nu trebuie să acceseze un link din e-mail. Riscul pentru datele de autentificare Windows depinde de atingerea unei partajări controlate de atacator de către solicitarea de rețea și de efectuarea schimbului de autentificare care urmează. Mozilla nu raportează exploatarea activă în buletin.

| Problemă | Declanșator la afișarea e-mailului | Risc pentru datele de autentificare Windows |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird încarcă conținutul unui atașament cu cheie OpenPGP pentru a oferi importul cheii. Expeditorul îl marchează drept atașament extern, cu un URL ales de atacator. | Un URL către o partajare de rețea expune datele NTLM ale utilizatorului dacă solicitarea ajunge la partajare. |
| **CVE-2026-118176** | O cale UNC cu lungime extinsă ocolește restricția Thunderbird privind partajările la distanță în URL-urile `mailbox:`. | Thunderbird se conectează la un server SMB ales de atacator și dezvăluie numele contului Windows și datele de autentificare NTLM. |

Pentru calea prin **atașamentul OpenPGP**, Mozilla afirmă explicit că solicitarea a ocolit blocarea conținutului la distanță și nu a necesitat intervenția utilizatorului. Pe sisteme non-Windows, problema permitea totuși o solicitare la distanță contrară setării pentru conținut la distanță, dar Mozilla limitează expunerea datelor NTLM la Windows. Pentru calea prin URL-ul **`mailbox:`**, Mozilla afirmă că celelalte sisteme de operare nu sunt afectate. Consultă intrările individuale pentru [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) și [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**Datele de autentificare NTLM nu sunt o parolă în text simplu.** Mozilla spune că datele dezvăluite prin calea SMB prezintă riscul spargerii offline a parolelor sau al atacurilor de tip relay. Simpla primire a unui mesaj creat cu rea intenție nu dovedește că atacul a reușit. Buletinul listează și alte vulnerabilități Thunderbird, inclusiv căi separate prin calendar și RSS. Acest ghid tratează cele două căi declanșate la afișarea e-mailului, fără să considere identice toate problemele din versiune.

## Verifică și actualizează Thunderbird

Fluxul afectat este **citirea e-mailurilor în Thunderbird pe Windows** înainte de aplicarea remedierii relevante. Mozilla indică **Thunderbird 153.6** ca versiune remediată, fără să specifice intervalul complet al celor mai vechi versiuni afectate de aceste două probleme. [Notele de lansare pentru 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) identifică o versiune ESR lansată pe 27 octombrie 2026. Nu deduce starea remedierii unui alt canal, fork sau pachet refăcut doar din eticheta versiunii.

1. În Windows, deschide **Help > About Thunderbird**. Citește versiunea afișată în fereastra About, care verifică și actualizările. [Instrucțiunile Mozilla pentru actualizare](https://support.mozilla.org/en-US/kb/updating-thunderbird) descriu această cale.
2. Dacă există o actualizare, lasă Thunderbird să o descarce, apoi selectează **Restart Thunderbird to Update**. După repornire, deschide din nou **Help > About Thunderbird** și confirmă versiunea instalată.
3. Pentru **linia 153 ESR**, compară versiunea rezultată cu **153.6.0esr** din notele de lansare Thunderbird. Dacă organizația ta gestionează actualizările, cere administratorului să verifice remedierea furnizorului în loc să presupui că actualizarea este deja instalată.

> **Notă despre versiune:** Notele de lansare pentru 153.6.0esr confirmă existența acestei versiuni. MFSA 2026-122 asociază remedierile de securitate cu Thunderbird 153.6. Notele nu descriu separat aceste două CVE. Consultă buletinul pentru detaliile vulnerabilităților.

## Redu expunerea în timpul actualizării

**Instalează mai întâi remedierea furnizorului.** Dezactivarea conținutului la distanță nu oprește singură CVE-2026-118174, deoarece solicitarea descrisă ocolea această setare. Recomandarea „nu da clic” nu este suficientă. Mozilla descrie solicitări declanșate de afișarea mesajului.

Ca **măsură suplimentară de apărare**, limitează traficul SMB de ieșire de la clienții Windows către internet, inclusiv **portul TCP 445**, la firewallul companiei sau pe dispozitivele gestionate. [Recomandările Microsoft privind traficul SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) sugerează blocarea traficului TCP 445 de ieșire către internet și limitarea accesului la serverele de fișiere necesare. Inventariază partajările necesare înainte să impui o regulă, mai ales dacă mediul folosește un serviciu de fișiere în cloud sau include angajați la distanță, în afara perimetrului. Acest control de rețea limitează calea SMB descrisă, dar nu repară Thunderbird și nu rezolvă toate problemele cu solicitări la distanță menționate în buletin.

Dacă un computer Windows cu o versiune veche de Thunderbird a afișat un mesaj suspect, **tratează expunerea ca pe o situație de investigat, nu ca pe o dovadă de compromitere**. Verifică împreună cu echipa de securitate jurnalele disponibile pentru conexiuni SMB de ieșire și autentificare. Buletinul furnizorului nu include un test de expunere și nici o recomandare generală de schimbare a tuturor parolelor.

## Surse

- [Mozilla Foundation Security Advisory 2026-122: vulnerabilități de securitate remediate în Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Note de lansare Thunderbird Desktop: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support: actualizarea Thunderbird la cea mai recentă versiune](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: securizarea traficului SMB în Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
