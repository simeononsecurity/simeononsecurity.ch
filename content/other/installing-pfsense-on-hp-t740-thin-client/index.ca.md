---
title: "Execució de pfSense al client prim HP t740: consells i guia de resolució de problemes"
draft: false
toc: true
date: 2023-04-29
description: "Obteniu informació sobre com configurar pfSense a l'HP t740 Thin Client i com resoldre problemes potencials com ara la congelació i els problemes de detecció de SSD."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "client prim", "servidor de casa", "PPPoE", "FreeBSD", "indicador d'arrencada", "loader.conf.local", "nano editor", "Detecció de SSD", "SSD M.2", "Western Digital", "resolució de problemes", "postinstal·lació", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Un dibuix animat d'un mag fent un encanteri per arreglar un ordinador congelat, amb una bafarada que diu Problema resolt"
coverCaption: ""
---
 pfSense, OPNsense o HardenedBSD al client prim HP t740**

Si busqueu un dispositiu potent per executar pfSense, OPNsense o HardenedBSD, l'HP t740 Thin Client pot ser una opció adequada per a vosaltres.

## Més potència i servidor domèstic compacte

L'HP t740 Thin Client és un dispositiu compacte que es pot utilitzar com una potent caixa pfSense o un servidor domèstic compacte. Ofereix més potència que el t730 o el t620 Plus, cosa que el converteix en una opció adequada per executar PPPoE, especialment si teniu Internet de fibra. També pot oferir una ruta d'actualització a xarxes de 10 Gigabit.

## PS/2 es congela

Tanmateix, si teniu previst executar FreeBSD o els seus derivats com pfSense, OPNsense o HardenedBSD al metall nu (a diferència de l'interior d'ESXi o Proxmox), és possible que us trobeu amb un problema en què el sistema es bloquegi a l'arrencada amb el missatge. `atkbd0: [GIANT-LOCKED]` Afortunadament, aquest problema es pot resoldre introduint les ordres següents a l'indicador d'arrencada:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

* Tingueu en compte que heu de desactivar tots dos, en cas contrari, encara es bloquejarà a l'arrencada.*

Després d'instal·lar el sistema operatiu, obriu un shell posterior a la instal·lació i executeu l'ordre següent:

```bash
vi /boot/loader.conf.local
```
A continuació, afegeix aquestes dues línies:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persistir els canvis utilitzant VI
Per a aquells que no estiguin familiaritzats amb vi, podeu afegir la línia fent el següent:

Afegint les línies `hint.uart.0.disabled="1"` i `hint.uart.1.disabled="1"` fins al `/boot/loader.conf.local` El fitxer amb l'editor vi es pot fer amb els passos següents:

1. Obriu el terminal del vostre sistema FreeBSD.

2. Tipus `vi /boot/loader.conf.local` i premeu Intro per obrir el fitxer a l'editor vi.

3. Premeu el botó `i` tecla per entrar al mode d'inserció.

4. Mou el cursor a la part inferior del fitxer amb les tecles de fletxa.

5. Tipus `hint.uart.0.disabled="1"` sense cometes.

6. Premeu Intro per iniciar una línia nova.

7. Tipus `hint.uart.1.disabled="1"` sense cometes.

8. Premeu el botó `Esc` tecla per sortir del mode d'inserció.

9. Tipus `:wq` i premeu Intro per desar i sortir del fitxer.

Això afegirà les dues línies a `/boot/loader.conf.local` fitxer, que desactivarà els UART i solucionarà el problema de congelació durant l'arrencada en determinats dispositius "Thin Client" d'HP t740 quan executeu FreeBSD o els seus derivats com pfSense, OPNsense o HardenedBSD.

Això solucionarà el problema amb els reinicis i les actualitzacions de microprogramari a pfSense/OPNsense.

## SSD

Si utilitzeu l'HP M.2 eMMC, no es detectarà en una instal·lació de FreeBSD lista. En aquest cas, necessitareu un SSD M.2 de tercers. Qualsevol SSD M.2 pot funcionar, SATA o NVMe.

Si esteu buscant un SSD M.2 de tercers per al vostre client lleuger HP t740, us recomanem que tingueu en compte el [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Ambdues opcions són fiables i haurien de funcionar bé amb el vostre dispositiu. Si voleu aprofitar les dues ranures, necessitareu les dues. Sacrificiareu les velocitats de l'NVME, però obtindreu una mica de redundància que és tan important.

Tingueu en compte que l'autor d'aquest article ha executat correctament pfSense CE 2.5.2 i OPNsense 22.1 al seu t740 sense cap problema després de seguir els passos anteriors.

## Resolució de problemes i postinstal·lació

Després de la instal·lació, si trobeu cap problema amb l'edició de fitxers, podeu instal·lar l'editor nano mitjançant `pkg update` i `pkg install nano` Això us ajudarà a editar fitxers de text amb facilitat.

Per garantir que els canvis realitzats al `/boot/loader.conf.local` El fitxer persisteix en les actualitzacions de la versió de pfSense, heu d'afegir les línies següents a `/boot/loader.conf` i `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

No obstant això, de vegades l'edició de `/boot/loader.conf.local` El fitxer abans de reiniciar no soluciona el problema. En aquests casos, pot ser necessari afegir les línies següents al començament del primer arrencada:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Aquests passos haurien de resoldre la majoria dels problemes que poden sorgir durant i després del procés d'instal·lació.

### Referències:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)