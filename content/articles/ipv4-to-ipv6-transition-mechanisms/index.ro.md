---
title: "Mecanisme de tranziție de la IPv4 la IPv6: un ghid complet"
date: 2023-02-18
lastmod: 2026-11-12
toc: true
draft: false
description: "Află care sunt mecanismele folosite pentru tranziția de la IPv4 la IPv6 în acest ghid complet."
tags: ["IPv4", "IPv6", "rețelistică", "mecanisme de tranziție", "stivă duală", "NAT64", "DNS64", "tunelare IPv6", "ISATAP", "6to4", "DS-Lite", "MAP-T", "migrare IPv6", "protocoale de rețea", "protocolul internet", "arhitectură de rețea", "rutare", "subnetare", "adresare"]
cover: "/img/cover/A_cartoon_image_of_a_person_standing_at_a_crossroads.webp"
coverAlt: "Ilustrație cu o persoană la o răscruce și un indicator cu direcțiile IPv4 și IPv6, care reprezintă alegerea și tranziția dintre cele două protocoale."
coverCaption: ""
---
**Mecanisme de tranziție de la IPv4 la IPv6**

Pe măsură ce cresc numărul dispozitivelor conectate și traficul de internet, lumea rămâne fără adrese IPv4 disponibile. IPv6 a fost introdus pentru a rezolva această problemă și a fost adoptat de multe rețele, însă tranziția este încă în curs. Acest articol prezintă mecanismele care pot fi folosite pentru migrarea de la IPv4 la IPv6.

## Introducere

**IPv4** este formatul inițial al adreselor IP și este folosit încă de la începuturile internetului. Utilizează adrese pe 32 de biți și poate susține până la 4,3 miliarde de adrese unice. Odată cu creșterea numărului de dispozitive conectate, această capacitate s-a dovedit insuficientă. În schimb, **IPv6** folosește adrese pe 128 de biți și poate susține un număr aproape infinit de adrese unice. Tranziția la IPv6 este necesară pentru ca internetul să continue să crească și să evolueze.

## Mecanisme de tranziție

### Stivă duală

Cea mai simplă metodă este rularea IPv4 și IPv6 în aceeași rețea. Aceasta se numește **stivă duală (Dual Stack)**. Într-o astfel de rețea, ambele protocoale sunt activate pe dispozitivele de rețea, care pot comunica folosind oricare dintre ele. Abordarea permite migrarea treptată la IPv6 și menține conectivitatea în timpul tranziției.

### Tunelare

**Tunelarea** înseamnă încapsularea pachetelor IPv6 în pachete IPv4 pentru a le transporta printr-o rețea IPv4. Mecanismul conectează segmente IPv6 separate de o rețea IPv4. Pachetul IPv6 este încapsulat într-un pachet IPv4, iar rețeaua IPv4 îl rutează până la celălalt capăt al tunelului. Acolo, pachetul IPv6 este decapsulat și livrat la destinație.

### Traducere

**Traducerea** facilitează comunicarea dintre rețelele IPv4 și IPv6. Există două tipuri: Network Address Translation-Protocol Translation (NAT-PT) și Address Family Transition Router (AFTR). **NAT-PT** traduce pachetele IPv6 în pachete IPv4 și invers, iar **AFTR** oferă conectivitate IPv6 gazdelor care folosesc numai IPv4.

### 6rd

**IPv6 Rapid Deployment (6rd)** este un mecanism pentru implementarea rapidă a IPv6 într-o rețea IPv4. În 6rd, un prefix IPv6 este încapsulat într-un pachet IPv4 și trimis prin rețeaua IPv4. La celălalt capăt, pachetul IPv6 este decapsulat și livrat la destinație. Mecanismul este util furnizorilor de servicii care doresc să implementeze IPv6 rapid și eficient.

### DS-Lite

**Dual-Stack Lite (DS-Lite)** oferă conectivitate IPv6 rețelelor care folosesc numai IPv4. În DS-Lite, un pachet IPv6 este încapsulat într-un pachet IPv4 și trimis prin rețeaua IPv4. La celălalt capăt, pachetul IPv6 este decapsulat și livrat la destinație. Mecanismul permite migrarea treptată la IPv6 fără a întrerupe conectivitatea IPv4.

### NAT64

**NAT64** oferă conectivitate IPv6 gazdelor care folosesc numai IPv4. Un pachet IPv6 este tradus într-un pachet IPv4, care poate fi trimis printr-o rețea IPv4. La celălalt capăt, pachetul IPv4 este tradus din nou într-un pachet IPv6 și livrat la destinație. Mecanismul este util pentru conectarea gazdelor care nu pot fi actualizate pentru a accepta IPv6.

______

Tranziția la IPv6 este necesară pentru ca internetul să continue să crească și să evolueze. Migrarea este în curs, iar pentru tranziție sunt disponibile mai multe mecanisme
