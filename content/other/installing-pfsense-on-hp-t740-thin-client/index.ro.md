---
title: "Rularea pfSense pe clientul subțire HP t740: sfaturi și ghid de depanare"
draft: false
toc: true
date: 2023-04-29
description: "Aflați cum să configurați pfSense pe clientul subțire HP t740 și cum să remediați problemele potențiale precum înghețarea și problemele de detectare a SSD-ului."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "client slab", "serverul de acasă", "PPPoE", "FreeBSD", "prompt de pornire", "loader.conf.local", "nano editor", "Detectare SSD", "SSD M.2", "Western Digital", "depanare", "post-instalare", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Un desen animat cu un vrăjitor care aruncă o vrajă pentru a repara un computer înghețat, cu un balon care spune Problema rezolvată"
coverCaption: ""
---
 pfSense, OPNsense sau HardenedBSD pe clientul subțire HP t740**

Dacă sunteți în căutarea unui dispozitiv puternic pentru a rula pfSense, OPNsense sau HardenedBSD, HP t740 Thin Client ar putea fi o alegere potrivită pentru dvs.

## Mai multă putere și compact Home Server

Clientul subțire HP t740 este un dispozitiv compact care poate fi folosit ca o cutie pfSense puternică sau un server compact de acasă. Oferă mai multă putere decât t730 sau t620 Plus, ceea ce îl face o alegere potrivită pentru rularea PPPoE, mai ales dacă aveți internet Fiber. De asemenea, poate oferi o cale de upgrade la rețeaua de 10 Gigabit.

## PS/2 îngheață

Cu toate acestea, dacă intenționați să rulați FreeBSD sau derivatele sale precum pfSense, OPNsense sau HardenedBSD pe bare metal (spre deosebire de ESXi sau Proxmox), este posibil să întâmpinați o problemă în care sistemul se blochează la pornire cu mesajul `atkbd0: [GIANT-LOCKED]` Din fericire, această problemă poate fi rezolvată prin introducerea următoarelor comenzi la promptul de pornire:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Rețineți că trebuie să le dezactivați pe ambele, altfel se va bloca în continuare la pornire.*

După ce instalați sistemul de operare, deschideți un shell post-instalare și rulați următoarea comandă:

```bash
vi /boot/loader.conf.local
```
Apoi, adăugați aceste două rânduri:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persista modificări folosind VI
Pentru cei care nu sunt familiarizați cu vi, puteți adăuga linia făcând următoarele:

Adăugarea liniilor `hint.uart.0.disabled="1"` și `hint.uart.1.disabled="1"` la `/boot/loader.conf.local` fișier folosind editorul vi se poate face cu următorii pași:

1. Deschideți terminalul de pe sistemul dumneavoastră FreeBSD.

2. Tastați `vi /boot/loader.conf.local` și apăsați Enter pentru a deschide fișierul în editorul vi.

3. Apăsați butonul `i` tasta pentru a intra în modul de inserare.

4. Mutați cursorul în partea de jos a fișierului folosind tastele săgeți.

5. Tastați `hint.uart.0.disabled="1"` fără ghilimele.

6. Apăsaţi Enter pentru a începe o nouă linie.

7. Tastați `hint.uart.1.disabled="1"` fără ghilimele.

8. Apăsați butonul `Esc` tasta pentru a ieși din modul de inserare.

9. Tastați `:wq` și apăsați Enter pentru a salva și a ieși din fișier.

Acest lucru va adăuga cele două linii la `/boot/loader.conf.local` fișier, care va dezactiva UART-urile și va rezolva problema de înghețare în timpul pornirii pe anumite dispozitive HP t740 „Thin Client” atunci când rulează FreeBSD sau derivatele sale, cum ar fi pfSense, OPNsense sau HardenedBSD.

Acest lucru va rezolva problema prin reporniri și upgrade-uri de firmware pe pfSense/OPNsense.

## SSD

Dacă utilizați HP M.2 eMMC, acesta nu va fi detectat într-o instalare FreeBSD disponibilă. În acest caz, veți avea nevoie de un SSD M.2 terță parte. Orice SSD M.2 poate funcționa, SATA sau NVMe.

Dacă sunteți în căutarea unui SSD M.2 terță parte pentru clientul dvs. subțire HP t740, vă recomandăm să luați în considerare [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Ambele opțiuni sunt fiabile și ar trebui să funcționeze bine cu dispozitivul dvs. Dacă doriți să profitați de ambele sloturi, veți avea nevoie de ambele. Vei sacrifica vitezele NVME, dar vei câștiga o oarecare redundanță care este atât de importantă.

Rețineți că autorul acestui articol a rulat cu succes pfSense CE 2.5.2 și OPNsense 22.1 pe t740-ul lor fără probleme, după ce a urmat pașii de mai sus.

## Depanare și post-instalare

După instalare, dacă întâmpinați probleme cu editarea fișierelor, puteți instala editorul nano folosind `pkg update` și `pkg install nano` Acest lucru vă va ajuta să editați fișierele text cu ușurință.

Pentru a se asigura că modificările aduse `/boot/loader.conf.local` fișierul persistă în actualizările versiunii pfSense, trebuie să adăugați următoarele linii la `/boot/loader.conf` și `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

Cu toate acestea, uneori editarea `/boot/loader.conf.local` fișierul înainte de repornire nu rezolvă problema. În astfel de cazuri, poate fi necesar să adăugați următoarele linii la începutul primei porniri:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Acești pași ar trebui să rezolve majoritatea problemelor care pot apărea în timpul și după procesul de instalare.

### Referințe:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)