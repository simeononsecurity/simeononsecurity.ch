---
title: "Kali Purple 2023.1: actualizări și funcții esențiale"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "O trecere în revistă a funcțiilor, instrumentelor și îmbunătățirilor istorice din Kali Purple 2023.1, cu referințe actuale pentru laboratoarele de securitate."
tags: ["Kali Linux", "Kali Purple", "2023.1", "hacking etic", "testare de penetrare", "securitate cibernetică", "instrumente", "cadru de exploatare", "actualizări Kali ARM", "Kali NetHunter", "documentația Kali", "suport pentru kernel", "suport Bluetooth", "LineageOS", "OneUI", "Radxa Zero", "computer cu o singură placă", "corecții kernel", "contribuții ale comunității", "Kali Discord", "actualizări Linux", "distribuție pentru hacking etic", "funcții noi", "îmbunătățiri", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "instrumente și pachete noi", "suport pentru dispozitive ARM", "documentația Kali", "reglementări guvernamentale"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Un dragon tridimensional Kali Linux stă pe un scut, înconjurat de instrumente de securitate cibernetică."
coverCaption: ""
---

**Kali Purple 2023.1: o recenzie**

**Kali Purple 2023.1** a fost prima previzualizare tehnică a direcției defensive de securitate din Kali. Nu mai este cea mai recentă versiune Kali. Articolul consemnează lansarea inițială și adaugă referințe actuale, astfel încât versiunile pachetelor din 2023.1 să nu fie confundate cu cele curente.

## Starea actuală a Kali

Istoricul oficial al lansărilor Kali indică Kali 2026.2, publicată la 29 iunie 2026, drept a doua versiune rolling din 2026. Aceasta folosește kernelul Linux 6.19 și Xfce 4.20.7. [Notele de lansare Kali 2026.2](https://www.kali.org/blog/kali-linux-2026-2-release/) descriu și GNOME 50, KDE Plasma 6.6, trecerea de la `sources.list` la `sources.list.d/kali.source` și modificările de pornire a mașinilor virtuale.

Kali Purple reprezintă direcția defensivă și purple-team din Kali. Anunțul din 2023.1 descria o previzualizare tehnică, cu o arhitectură de referință SOC-in-a-box, instrumente defensive și categorii de meniu bazate pe NIST Cybersecurity Framework. Aceste detalii țin de contextul istoric. Pentru alegerea pachetelor actuale, consultă [documentația metapachetelor Kali](https://www.kali.org/docs/general-use/metapackages/) și selectează doar grupurile de instrumente necesare laboratorului tău.

*Desfășoară fiecare exercițiu ofensiv sau defensiv într-un laborator izolat și autorizat. Instalarea Kali nu îți dă permisiunea să testezi sisteme pe care nu le deții și nu le administrezi.*

______

## Imaginea de fundal și actualizările desktopului Kali

Kali Purple 2023.1 introduce **o nouă imagine de fundal implicită**, Kali Sticker, cu fundal violet și diverse autocolante legate de Kali. Imaginea a fost inspirată de lucrările lui /u/Albert-III- și TJ_Null.

Pe lângă imaginea nouă, Kali Purple 2023.1 actualizează și cele trei medii desktop principale: **Xfce, KDE și GNOME**. Actualizările includ funcții noi, îmbunătățiri de performanță și remedieri de erori.

______

## Xfce 4.18

**Xfce 4.18** aduce mai multe îmbunătățiri notabile, printre care:

- Suport îmbunătățit pentru scalarea interfeței
- Actualizări ale managerului de fișiere Thunar
- Profiluri de panou pentru personalizare ușoară

______

## KDE Plasma 5.27

Actualizarea **KDE Plasma 5.27** aduce:

- Un nou sistem de aranjare a ferestrelor în mozaic
- O temă de aplicații mai elegantă
- Instrumente și widgeturi mai clare și mai ușor de folosit

______

## Actualizări GNOME

În GNOME, Kali Purple 2023.1 îmbunătățește ușurința de utilizare. De exemplu, poți deschide rapid un terminal în dosarul curent al managerului de fișiere apăsând F4.

______

## Setări implicite ale kernelului și probleme cunoscute

Kali Purple 2023.1 actualizează unele valori implicite ale kernelului pentru a îmbunătăți ușurința de utilizare.

______

## Instrumente și pachete noi

Kali Purple 2023.1 adaugă instrumente și pachete care îi extind capacitățile de **testare a penetrării** și **hacking etic**. Printre noutăți se numără:

- **Rizin 0.3.0**: Un cadru modern de inginerie inversă
- **Ghidra 10.1**: O suită open source de inginerie inversă software
- **Python 3.10**: Cea mai recentă versiune a limbajului popular de programare

Aceste instrumente și actualizările pachetelor existente au extins previzualizarea 2023.1 pentru profesioniștii în securitate. Versiunile din această secțiune se referă la lansarea 2023.1, nu la cele incluse în Kali 2026.2.

______

## Suport pentru dispozitive ARM

Kali Purple 2023.1 continuă să extindă suportul pentru dispozitive ARM. Adaugă compatibilitate cu dispozitive noi precum **Radxa Zero** și îmbunătățește suportul existent pentru modele precum **LG V20**. Astfel, Kali poate fi folosit pe hardware variat, de la computere mici cu o singură placă la smartphone-uri puternice.

______

## Documentație și comunitate

Echipa Kali a actualizat **documentația** cu ghiduri, tutoriale și sfaturi de depanare, pentru a-i ajuta pe utilizatori să folosească mai bine Kali Purple 2023.1. Echipa a recunoscut și mai mulți membri ai comunității pentru contribuțiile lor, evidențiind valoarea colaborării open source și a comunității Kali.

______

## Reglementări guvernamentale

Acest articol nu tratează reglementări guvernamentale specifice pentru hacking etic sau testare de penetrare. Totuși, aceste activități sunt reglementate în multe jurisdicții. Obține întotdeauna permisiunile necesare și respectă legile aplicabile când efectuezi evaluări de securitate. Pentru detalii, consultă:

- [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [Regulamentul general privind protecția datelor (GDPR)](https://gdpr.eu/)

______

## Concluzie

Kali Purple 2023.1 a fost prima previzualizare a direcției defensive de securitate din Kali. A extins setul de instrumente, a îmbunătățit suportul ARM și a completat documentația. Pentru o instalare actuală, consultă notele de lansare Kali și alege pachetele potrivite laboratorului tău. Respectă regulile aplicabile și testează sisteme numai cu permisiune explicită.

______

## Referințe

1. [Site-ul oficial Kali Linux](https://www.kali.org/)
2. [Documentația Kali Linux](https://www.kali.org/docs/)
3. [Descărcări Kali Linux](https://www.kali.org/get-kali/)
4. [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [Regulamentul general privind protecția datelor (GDPR)](https://gdpr.eu/)

______

## Resurse suplimentare

- [Forumurile oficiale Kali Linux](https://forums.kali.org/)
- [Blogul Kali Linux](https://www.kali.org/blog/)
- [Instruire și certificare Kali Linux](https://www.offensive-security.com/)

______

## Listă de verificare pentru actualizare

- **Consultă istoricul lansărilor.** Citește [istoricul actual al lansărilor Kali](https://www.kali.org/releases/) înainte de a descărca o imagine.
- **Folosește imagini oficiale.** Descarcă-le din [Get Kali](https://www.kali.org/get-kali/) și verifică sumele de control publicate.
- **Actualizează instalările rolling.** Urmează [documentația actuală de actualizare Kali](https://www.kali.org/docs/general-use/updating-kali/) în loc să copiezi fără verificare exemplul de depozit din 2023.1.
- **Alege metapachetele cu grijă.** Un laborator standard sau Purple nu are nevoie de toate pachetele Kali.
- **Definește domeniul laboratorului.** Notează sistemele autorizate, intervalele de testare, jurnalizarea și curățarea înainte de a porni instrumentele.
