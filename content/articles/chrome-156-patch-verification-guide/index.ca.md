---
title: "Actualització de seguretat de Chrome 156: verifica el pedaç d’octubre"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Comprova la versió de seguretat de Chrome 156 del 27 d’octubre a Windows, macOS, Linux i Android. Compara la compilació instal·lada, completa un reinici pendent i revisa per separat els dispositius gestionats."
genre: ["Navegadors", "Seguretat", "Gestió de pedaços"]
tags: ["Chrome 156", "actualització de seguretat de Chrome", "verificació del pedaç de Chrome", "comprovació de la versió de Chrome", "Chrome 156 per a Windows", "Chrome 156 per a macOS", "Chrome 156 per a Linux", "Chrome 156 per a Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "pedaços de navegador", "Chrome Enterprise Core", "navegadors gestionats", "seguretat de Chromium", "actualitzacions de navegador", "reinici de Chrome", "chrome://version", "chrome://settings/help", "actualització de Chrome per a Android", "actualitzacions de seguretat de Brave", "actualitzacions de seguretat d’Edge"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Il·lustració d’un cadenat i un escut que representen una actualització de seguretat, no una pantalla de versió de Chrome"
coverCaption: ""
---

**La versió de seguretat de Chrome del 27 d’octubre de 2026** inclou 52 correccions. Per comprovar la instal·lació, compara la versió completa amb la publicada per al teu sistema operatiu i reinicia Chrome per completar qualsevol actualització pendent. L’anunci d’una versió no demostra que el dispositiu hagi rebut l’actualització. ([Llançament de Chrome per a escriptori](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Quina versió hi hauries de veure?

Google va publicar aquestes versions del canal Stable el 27 d’octubre de 2026. L’anunci per a escriptori indica compilacions diferents per a Windows i macOS i per a Linux. El [llançament per a Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) indica una compilació pròpia i diu que les versions d’Android inclouen les mateixes correccions de seguretat que les versions d’escriptori corresponents, «llevat que s’indiqui el contrari».

| Plataforma | Compilació de l’anunci de Google del 27 d’octubre |
|---|---|
| **Windows** | 156.0.8078.73 o 156.0.8078.74 |
| **macOS** | 156.0.8078.73 o 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Fes servir aquesta taula per al llançament del 27 d’octubre, no com a versió objectiu permanent. Consulta el [canal actual de llançaments de Chrome](https://chromereleases.googleblog.com/) per veure les actualitzacions de seguretat posteriors.* Google va dir que el desplegament per a escriptori duraria «els pròxims dies o setmanes» i que la compilació d’Android arribaria a Google Play durant els dies següents. Si un dispositiu té una versió inferior a la indicada, cal comprovar-lo fins i tot durant un desplegament gradual. ([Avís per a escriptori](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [avís per a Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

La [llista de correccions de seguretat per a escriptori](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) classifica quatre errors notificats com a **Critical**: corrupció de memòria a FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), validació incorrecta de dades d’entrada a FileAPI CVE-2026-118331, validació incorrecta de dades d’entrada a Skia CVE-2026-118348 i use-after-free a Layout CVE-2026-118344. El mateix avís enumera altres CVE de nivell **High** i **Medium**. La xifra 52 indica les correccions de seguretat del llançament, no pas 52 informes d’explotació verificats de manera independent. ([Registre de NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**L’avís del llançament no afirma que s’estiguin explotant activament les vulnerabilitats enumerades.** L’advertiment tracta del moment de la divulgació: «L’accés als detalls dels errors i als enllaços pot continuar restringit fins que la majoria d’usuaris rebi una correcció». No interpretis la restricció d’accés als detalls com una prova d’explotació. ([Avís per a escriptori](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Comprova i completa l’actualització d’escriptori

1. Obre **`chrome://version`** a la instal·lació de Chrome que utilitzes. Anota la versió completa i el sistema operatiu, no només el número principal 156. Comprova per separat les finestres de Chrome d’un altre canal o d’una altra ubicació d’instal·lació.
2. Obre **`chrome://settings/help`** o selecciona **Més > Ajuda > Quant a Google Chrome**. Google explica que Chrome cerca actualitzacions en aquesta pàgina. Espera que acabi la comprovació. ([Instruccions de Google per actualitzar l’escriptori](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Selecciona **Reinicia** si la pàgina ho ofereix. Desa abans la feina pendent. Tanca les altres finestres de Chrome, torna a obrir el navegador i consulta de nou **`chrome://version`**. Compara amb la taula la versió que apareix després del reinici.
4. Si la versió encara és anterior a la compilació anunciada, torna a cercar actualitzacions disponibles. Si una organització gestiona el navegador o l’actualitzador mostra un error, contacta amb l’administrador. Que la baixada hagi acabat bé no demostra que hagi canviat la versió del navegador en execució.

> **Resultat esperat:** Després de reiniciar, la compilació Stable de Chrome en execució correspon a la versió de la plataforma de l’anunci del 27 d’octubre o a una versió posterior anunciada pel proveïdor. Un botó Reinicia pendent no demostra que l’actualització s’hagi completat.

A **Android**, obre Play Store > icona del perfil > Gestiona les aplicacions i el dispositiu, i actualitza Chrome a Actualitzacions disponibles si hi apareix. A Chrome, obre Més > Configuració > Quant a Chrome per veure la versió instal·lada. Compara-la amb la fila d’Android quan s’hagi completat l’actualització de l’aplicació. Aquests passos segueixen les [instruccions de Google per a Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Verifica les flotes gestionades

Per als navegadors inscrits, fes servir l’**informe de versions de Chrome** de la consola d’administració de Google per trobar compilacions antigues per sistema operatiu. Obre la vista Browser Versions, selecciona la unitat organitzativa pertinent, inspecciona la versió menor completa i exporta el CSV si necessites una llista de dispositius per gestionar. Google diu que l’informe inclou els navegadors que han enviat informes durant els 28 dies anteriors. També adverteix que pot haver-hi retards, sobretot en flotes grans. ([Consulta els detalls de la versió de Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Separa l’inventari informat de la verificació en directe.** Revisa l’hora de l’últim informe i el canal de cada dispositiu, i confirma les excepcions directament al navegador o amb l’inventari dels punts finals gestionats. Google compta separadament les instal·lacions diferents de Chrome, com ara Stable i Beta. Els informes de navegador requereixen inscripció i [informes de navegadors gestionats](https://support.google.com/chrome/a/answer/9301421?hl=en). Que una màquina no aparegui a l’informe no demostra que tingui el pedaç.

## Comprova per separat els navegadors derivats de Chromium

**La taula de versions de Chrome s’aplica a Google Chrome.** Microsoft Edge, Brave i altres navegadors basats en Chromium tenen paquets, números de llançament i calendaris d’actualització propis. L’anunci de Chrome no confirma l’estat dels seus pedaços. Comprova la versió instal·lada de cada navegador i el seu propi avís de seguretat o les notes de llançament per veure les correccions de Chromium pertinents. No comparis directament una versió d’Edge o Brave amb Chrome 156.0.8078.73 per declarar-la corregida.

Per a cada navegador derivat, anota el nom del producte, el canal, la compilació instal·lada, l’URL de l’avís del proveïdor i la compilació que el proveïdor indica com a corregida. Si el proveïdor no ha confirmat la correcció, marca l’estat com a **no verificat** i segueix les seves instruccions d’actualització. Registra Chrome i els derivats en files separades de l’inventari.

## Fonts i referències

- [Chrome Releases: actualització Stable Channel per a escriptori, 27 d’octubre de 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Compilacions d’escriptori, 52 correccions, CVE i text del proveïdor sobre la divulgació.
- [Chrome Releases: actualització de Chrome per a Android, 27 d’octubre de 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Compilació d’Android i excepció sobre les correccions d’escriptori corresponents.
- [Seguiment d’incidències de Chromium: consulta de correccions de seguretat M156](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Enllaç de l’avís per a escriptori. L’accés als detalls de cada incidència depèn de les restriccions de divulgació.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) i [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Descripcions de les vulnerabilitats i versions de Chrome afectades. Els nivells de gravetat anteriors segueixen l’avís de Google, no una puntuació CVSS de NVD.
- [Ajuda de Google Chrome: actualitzar Chrome als ordinadors](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) i [a Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Comprovació d’actualitzacions i passos del menú de versions.
- [Ajuda de Chrome Enterprise: consulta els detalls de la versió de Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en) i [activa els informes de navegadors gestionats](https://support.google.com/chrome/a/answer/9301421?hl=en). Requisits previs i límits dels informes de flota.
