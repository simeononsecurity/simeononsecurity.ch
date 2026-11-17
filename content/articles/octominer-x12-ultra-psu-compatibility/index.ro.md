---
title: "Compatibilitatea surselor Octominer X12 Ultra: test practic Chicony și LiteOn"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Un test cu cinci ventilatoare și trei surse pe un Octominer X12 Ultra a arătat că o sursă Chicony a pornit sistemul, în timp ce unitățile LiteOn testate au indicat culoarea chihlimbar și nu au pornit."
genre: ["Hardware pentru minare", "Hardware de calculator"]
tags: ["Octominer X12 Ultra", "sursă de alimentare pentru server", "compatibilitatea surselor", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Ilustrație abstractă cu trei surse de server într-un șasiu și indicatoare de stare verzi, chihlimbarii și gri"
coverCaption: ""
---

**Chicony R12-1K6P2A a pornit sistemul meu Octominer X12 Ultra cu cinci ventilatoare și trei surse.** Sursele LiteOn PS-2142-2L testate au afișat o lumină verde, au trecut la chihlimbar și nu au pornit sistemul. Rezultatul se aplică unității mele cu placa de alimentare **OCTOMINER (12PIN) 3x DPS1200 rev. 20**. O putere nominală similară sau o listă pentru o placă breakout X12 separată nu dovedește compatibilitatea cu o placă Octominer.

Șasiul s-a vândut ca **configurație de 3.600 W**, cu trei locașuri pentru surse. [Octominer listează o opțiune cu trei surse de 1.200 W](https://octominer.eu/product/octominer-x12-ultra-used/) pentru X12 Ultra, alături de alte configurații. Verifică eticheta și placa de alimentare din propriul echipament înainte să aplici aceste rezultate.

## Rezultatele testelor

| Sursă | Rezultat pe acest sistem |
|---|---|
| **Chicony R12-1K6P2A, 1.600 W** | A pornit sistemul în testul meu. Articolul nu a măsurat funcționarea la sarcină susținută sau în toate locașurile. |
| **LiteOn PS-2142-2L, 1.400 W** | Unitățile testate au luminat verde, apoi chihlimbar. Sistemul nu a pornit. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | Intrarea CA neobișnuită a îngreunat găsirea unui cablu potrivit. Nu am înregistrat rezultate de pornire sau sarcină pentru această sursă în testul de față. |
| **HP HSTNS-PD30, 1.200 W** | Testată pe același sistem. Nu a pornit sistemul. |
| **Alte surse HP Common Slot** | Kiturile Platinum Plus de 1.200 W și unitățile de 750 W HSTNS-PD22B, HSTNS-PL22B și HSTNS-PD18 testate nu au pornit acest sistem. Numerele exacte de model ale surselor din kituri nu au fost înregistrate. |

**Nu interpreta rezultatul LiteOn ca diagnostic de defecțiune pentru toate sursele PS-2142-2L.** Secvența observată indică o pornire eșuată în acest șasiu. Testul nu a izolat semnalul de activare, schimbul de telemetrie, pinout-ul plăcii sau o defecțiune a unei surse individuale. La fel, rezultatul Chicony dovedește o pornire reușită, nu o putere certificată de 4.800 W pentru șasiu și nici fiabilitatea pe termen lung.

## Ce model Chicony a pornit sistemul?

Modelul funcțional a fost **Chicony R12-1K6P2A**, listat și ca piesa **R1K6A002L** în [tabelul de compatibilitate Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). [Raportul de testare 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identifică o sursă de 1.600 W, cu valori nominale de **200-240 V CA**, 10 A și 50-60 Hz. Raportul a măsurat o eficiență de 94,19% la sarcină de jumătate, în condițiile de testare de 230 V. Aceste valori descriu sursa testată, nu întregul echipament de minare.

Valoarea de **200-240 V contează**. Nu presupune că acest model livrează puterea nominală de la o priză de 120 V. Potrivit unei [listări de piese pentru server pentru modelul exact](https://www.itcreations.com/product/142080), sursa testată are o intrare C14 standard. Folosește cabluri și echipamente de distribuție dimensionate pentru tensiunea și curentul de intrare.

Testul meu a confirmat o pornire reușită cu Chicony pe această placă specifică. Nu dovedește compatibilitatea cu toate reviziile X12 Ultra. Compară numărul complet al modelului și verifică eticheta sursei înainte să comanzi alte unități.

## De ce lista LiteOn m-a indus în eroare

**LiteOn PS-2142-2L** apare în [tabelul de compatibilitate pentru plăci breakout X12 al Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). [Raportul 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) identifică un model de 1.400 W. Aceste surse confirmă modelul și utilizarea listată cu **adaptorul X12 Parallel Miner**. Niciuna nu testează placa de alimentare OEM Octominer.

Unitățile mele PS-2142-2L au trecut de la **verde la chihlimbar** după introducere, iar sistemul nu a pornit. Lame de ieșire asemănătoare nu dovedesc același comportament la pornire, stare sau comunicare. Secvența LED nu dovedește, de una singură, ce diferență a provocat pornirea eșuată.

Același [tabel Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) grupează **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** și **Chicony R12-1K6P2A** în familia de adaptoare cu opt pini. **HP HSTNS-PD30** și mai multe surse HP Common Slot de 750 W apar în altă familie de adaptoare cu șase pini. Niciuna dintre sursele HP încercate nu a pornit sistemul. Tabelul descrie plăcile Parallel Miner, nu o listă de înlocuitori pentru placa **OCTOMINER (12PIN)**.

## Verifică alimentarea și cablurile

[Ghidul de depanare Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) spune că șasiul, singur, consumă până la **200 W când ventilatoarele rulează la viteză maximă**. Recomandă o rezervă de putere de cel puțin **10%** și avertizează să nu se depășească **90% din puterea nominală a surselor instalate**. Ia în calcul consumul GPU-urilor, șasiul și puterea reală a surselor la tensiunea ta CA.

**Eticheta de 1.600 W a fiecărei surse Chicony nu ridică configurația publicată a șasiului de la 3.600 W la 4.800 W.** Placa de alimentare, cablajul intern, conectorii, distribuția CA și răcirea limitează și ele sistemul. Nu am măsurat aceste limite pe această unitate. Păstrează sistemul în configurația documentată până când Octominer confirmă o valoare superioară pentru revizia exactă a plăcii.

Dell/Delta **D1200E-S0 / 0F37X3** a avut o altă problemă: intrarea CA de pe partea sursei necesita un cablu de împerechere mai rar. Într-o căutare anterioară, am identificat intrarea ca **LS-25** și conectorul de pe partea cablului ca **LS-26**, pe baza unității și a listărilor de cabluri. Verifică forma conectorului și marcajele electrice înainte să cumperi un cablu. O mufă C13 cu aspect familiar nu înlocuiește conectorul pereche corect.

## Verifică propriul X12

1. **Înregistrează hardware-ul exact.** Fotografiază etichetele șasiului și sursei, intrarea CA, lama de ieșire și revizia plăcii de alimentare. Numără ventilatoarele și locașurile surselor.
2. **Verifică alimentarea CA.** Compară valoarea de intrare a sursei cu valorile prizei, cablului și PDU-ului. Raportul Chicony R12-1K6P2A specifică 200-240 V CA.
3. **Testează o configurație minimă.** Oprește și deconectează toate alimentările CA înainte de a schimba o sursă, un GPU sau o conexiune PSON. [Ghidul Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) recomandă verificarea fixării sursei și a LED-urilor, a cablului PSON cu șase pini dintre placa de bază și placa de alimentare și testarea unei surse cu un GPU pentru izolarea problemei de pornire.
4. **Înregistrează rezultatul.** Notează modelul sursei, locașul, secvența LED-urilor, dacă placa și ventilatoarele au pornit și dacă sistemul a pornit complet. Repetă testul în alte locașuri numai după o oprire sigură.
5. **Măsoară înainte de a adăuga sarcină.** Verifică telemetria sursei și consumul de la priză la sarcina GPU planificată. Rezultatul de pornire din acest articol nu înlocuiește un test de sarcină.

## Concluzie

**Chicony R12-1K6P2A este singura sursă de schimb din comparație cu o pornire reușită raportată în X12 Ultra cu trei locașuri al meu.** Unitățile LiteOn PS-2142-2L testate au trecut de la verde la chihlimbar și nu au pornit. Nici sursele HP Common Slot testate nu au pornit sistemul. Tratează alte liste de surse ca piste de cercetare până când modelul exact și placa Octominer trec un test controlat de pornire și sarcină. Începe cu etichetele modelelor și revizia plăcii, apoi consultă recomandările de alimentare Octominer înainte să crești sarcina GPU.
