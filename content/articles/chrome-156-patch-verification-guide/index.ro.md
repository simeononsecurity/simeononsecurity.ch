---
title: "Actualizare de securitate Chrome 156: verifică patch-ul din octombrie"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Verifică versiunea de securitate Chrome 156 din 27 octombrie pe Windows, macOS, Linux și Android. Compară buildul instalat, finalizează repornirea în așteptare și verifică separat dispozitivele gestionate."
genre: ["Browsere", "Securitate", "Gestionarea patch-urilor"]
tags: ["Chrome 156", "actualizare de securitate Chrome", "verificarea patch-ului Chrome", "verificarea versiunii Chrome", "Chrome 156 pentru Windows", "Chrome 156 pentru macOS", "Chrome 156 pentru Linux", "Chrome 156 pentru Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "patch-uri pentru browsere", "Chrome Enterprise Core", "browsere gestionate", "securitatea Chromium", "actualizări de browser", "repornirea Chrome", "chrome://version", "chrome://settings/help", "actualizare Chrome pentru Android", "actualizări de securitate Brave", "actualizări de securitate Edge"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Ilustrație cu un lacăt și un scut care simbolizează o actualizare de securitate, nu un ecran cu versiunea Chrome"
coverCaption: ""
---

**Versiunea de securitate Chrome din 27 octombrie 2026** include 52 de remedieri. Pentru a verifica instalarea, compară versiunea completă cu versiunea publicată pentru sistemul tău de operare, apoi repornește Chrome pentru a finaliza orice actualizare în așteptare. Anunțarea unei versiuni nu dovedește că dispozitivul tău a primit actualizarea. ([Lansarea Chrome pentru desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Ce versiune ar trebui să vezi?

Google a publicat aceste versiuni ale canalului Stable pe 27 octombrie 2026. Lansarea pentru desktop enumeră builduri separate pentru Windows și macOS, respectiv Linux. [Lansarea pentru Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) indică propriul build și precizează că versiunile Android conțin aceleași remedieri de securitate ca versiunile desktop corespunzătoare, „dacă nu se menționează altceva”.

| Platformă | Buildul din anunțul Google din 27 octombrie |
|---|---|
| **Windows** | 156.0.8078.73 sau 156.0.8078.74 |
| **macOS** | 156.0.8078.73 sau 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Folosește acest tabel pentru lansarea din 27 octombrie, nu ca versiune-țintă permanentă. Consultă [fluxul actual al lansărilor Chrome](https://chromereleases.googleblog.com/) pentru actualizările de securitate ulterioare.* Google a spus că implementarea pe desktop va dura „următoarele zile sau săptămâni”, iar buildul Android va ajunge în Google Play în următoarele zile. Un dispozitiv cu o versiune mai veche decât cea din tabel trebuie verificat și în timpul unei implementări etapizate. ([Notificare pentru desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [notificare pentru Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

[Lista remedierilor de securitate pentru desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) clasifică patru probleme raportate drept **Critical**: coruperea memoriei în FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), validarea incorectă a intrărilor în FileAPI CVE-2026-118331, validarea incorectă a intrărilor în Skia CVE-2026-118348 și use-after-free în Layout CVE-2026-118344. Aceeași notificare enumeră și alte CVE de nivel **High** și **Medium**. Cifra 52 reprezintă remedierile de securitate din versiune, nu 52 de rapoarte de exploatare verificate independent. ([Înregistrarea NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**Notificarea lansării nu afirmă că vulnerabilitățile enumerate sunt exploatate activ.** Avertismentul se referă la momentul divulgării: „Accesul la detaliile problemelor și la linkuri poate rămâne restricționat până când majoritatea utilizatorilor primesc o remediere.” Nu considera accesul restricționat la detalii drept dovadă de exploatare. ([Notificare pentru desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Verifică și finalizează actualizarea desktop

1. Deschide **`chrome://version`** în instalarea Chrome pe care o folosești. Notează versiunea completă și sistemul de operare, nu doar numărul major 156. Verifică separat o fereastră Chrome din alt canal sau din altă instalare.
2. Deschide **`chrome://settings/help`** sau selectează **Mai multe > Ajutor > Despre Google Chrome**. Google spune că Chrome caută actualizări pe această pagină. Așteaptă terminarea verificării. ([Instrucțiunile Google pentru actualizarea desktop](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Selectează **Relansează** dacă pagina oferă opțiunea. Salvează mai întâi lucrul nefinalizat. Închide celelalte ferestre Chrome, redeschide browserul și verifică din nou **`chrome://version`**. Compară cu tabelul versiunea afișată după repornire.
4. Dacă versiunea este încă mai veche decât buildul anunțat, verifică din nou dacă există o actualizare. Dacă o organizație gestionează browserul sau programul de actualizare raportează o eroare, contactează administratorul. O descărcare reușită nu dovedește că versiunea browserului aflat în execuție s-a schimbat.

> **Rezultat așteptat:** După repornire, buildul Chrome Stable aflat în execuție corespunde versiunii platformei din notificarea din 27 octombrie sau unei versiuni ulterioare anunțate de furnizor. Un buton Relansează care încă așteaptă nu dovedește finalizarea actualizării.

Pe **Android**, deschide Play Store > pictograma profilului > Gestionează aplicațiile și dispozitivul, apoi actualizează Chrome în secțiunea Actualizări disponibile dacă apare. În Chrome, deschide Mai multe > Setări > Despre Chrome pentru a vedea versiunea instalată. Compar-o cu rândul Android după finalizarea actualizării aplicației. Aceste căi din meniu urmează [instrucțiunile Google pentru Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Verifică flotele gestionate

Pentru browserele înscrise, folosește **raportul versiunilor Chrome** din consola de administrare Google pentru a găsi builduri mai vechi în funcție de sistemul de operare. Deschide vizualizarea Browser Versions, selectează unitatea organizațională relevantă, inspectează versiunea minoră completă și exportă fișierul CSV dacă ai nevoie de o listă de lucru pe dispozitive. Google spune că raportul include browserele care au trimis rapoarte în ultimele 28 de zile. Menționează posibile întârzieri, mai ales în flotele mari. ([Vezi detalii despre versiunile Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Separă inventarul raportat de verificarea în timp real.** Verifică ora ultimului raport și canalul fiecărui dispozitiv, apoi confirmă excepțiile direct în browser sau prin inventarul endpointurilor gestionate. Google numără separat instalările distincte de Chrome, precum Stable și Beta. Raportarea browserelor necesită înscrierea și activarea [raportării browserelor gestionate](https://support.google.com/chrome/a/answer/9301421?hl=en). Absența unui calculator din raport nu dovedește că are patch-ul instalat.

## Verifică separat browserele derivate din Chromium

**Tabelul versiunilor Chrome se aplică browserului Google Chrome.** Microsoft Edge, Brave și alte browsere bazate pe Chromium au propriile pachete, numere de lansare și programe de actualizare. Anunțul Chrome nu confirmă starea patch-urilor lor. Verifică versiunea instalată a fiecărui browser și propriul aviz de securitate sau notele de lansare pentru remedierile Chromium relevante. Nu compara direct o versiune Edge sau Brave cu numărul Chrome 156.0.8078.73 pentru a declara că este corectată.

Pentru fiecare browser derivat, notează numele produsului, canalul, buildul instalat, URL-ul avizului furnizorului și buildul pe care furnizorul îl indică drept corectat. Dacă furnizorul nu a confirmat o remediere, marchează starea **neverificată** și urmează instrucțiunile de actualizare ale furnizorului respectiv. Păstrează rezultatele pentru Chrome și derivate în rânduri separate din inventar.

## Surse și referințe

- [Chrome Releases: actualizarea Stable Channel pentru desktop, 27 octombrie 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Builduri desktop, 52 de remedieri, CVE și formularea furnizorului despre divulgare.
- [Chrome Releases: actualizarea Chrome pentru Android, 27 octombrie 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Buildul Android și rezerva privind remedierile corespunzătoare pentru desktop.
- [Trackerul de probleme Chromium: căutare de remedieri de securitate M156](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Link din anunțul pentru desktop. Accesul la detaliile fiecărei probleme depinde de restricțiile de divulgare.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) și [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Descrieri ale vulnerabilităților și versiunile Chrome afectate. Nivelurile de severitate de mai sus urmează notificarea Google, nu o evaluare CVSS NVD.
- [Ajutor Google Chrome: actualizează Chrome pe computere](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) și [pe Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Verificarea actualizărilor și căile din meniu pentru versiune.
- [Ajutor Chrome Enterprise: vezi detalii despre versiunea Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en) și [activează raportarea browserelor gestionate](https://support.google.com/chrome/a/answer/9301421?hl=en). Cerințe preliminare și limite pentru raportarea flotei.
