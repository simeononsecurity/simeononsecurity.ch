---
title: "TrueNAS contra Unraid: quin sistema operatiu NAS és el millor?"
date: 2023-02-16
lastmod: 2026-11-13
toc: true
draft: false
description: "Compara TrueNas i Unraid pel disseny d'emmagatzematge, la facilitat d'ús, les funcions, la documentació, la comunitat i l'adequació a les càrregues de treball."
genre: ["Tecnologia", "Sistemes d'emmagatzematge", "Emmagatzematge connectat a la xarxa", "Gestió de dades", "Sistemes operatius NAS", "Comparació", "Protecció de dades", "Emmagatzematge domèstic", "Emmagatzematge empresarial", "Codi obert"]
tags: ["Unraid", "TrueNas", "Sistema operatiu NAS", "Comparació", "Facilitat d'ús", "Funcions", "Documentació", "Comunitat", "Codi obert", "Empreses", "Protecció de dades", "Rendiment", "Flexibilitat", "Fàcil d'utilitzar", "Aplicacions de tercers", "Emmagatzematge connectat a la xarxa", "Tecnologia RAID", "Gestió d'emmagatzematge", "OpenZFS", "Usuaris domèstics", "Model de preus", "Emmagatzematge al núvol", "Virtualització", "Centre de documentació", "Fòrum comunitari", "Protecció de dades avançada", "Sistema operatiu NAS madur", "Coneixements tècnics", "Professionals informàtics", "Unraid contra TrueNas", "Comparació de sistemes operatius NAS", "Emmagatzematge connectat a la xarxa", "Funcions d'Unraid", "Funcions de TrueNas", "Documentació d'Unraid", "Documentació de TrueNas", "Comunitat d'Unraid", "Comunitat de TrueNas", "Preus d'Unraid", "Cost de TrueNas", "Facilitat d'ús d'Unraid", "Facilitat d'ús de TrueNas", "Gestió d'emmagatzematge d'Unraid", "Protecció avançada de dades de TrueNas", "Aplicacions de tercers d'Unraid", "Emmagatzematge al núvol de TrueNas", "Virtualització d'Unraid", "Mercat empresarial de TrueNas", "RAID d'Unraid", "OpenZFS de TrueNas", "Usuaris domèstics d'Unraid", "TrueNas com a NAS madur", "Coneixements tècnics d'Unraid", "Professionals informàtics de TrueNas", "Rendiment d'Unraid", "Escalabilitat de TrueNas", "Assistència d'Unraid", "Sistema de fitxers de TrueNas", "Gestió de discos d'Unraid", "Expansió d'emmagatzematge de TrueNas", "sistema operatiu truenas", "truenas contra freenas contra unraid"]
cover: "/img/cover/Two_computer_servers_facing_each_other_one_blue_one_green.webp"
coverAlt: "Dos servidors enfrontats, un blau i un verd. Al costat blau, una persona porta casc i armilla de seguretat. Al costat verd, una persona seu al sofà."
coverCaption: "Tria el sistema operatiu NAS adequat per a les teves necessitats d'emmagatzematge."
---

Quan construeixes un sistema d'emmagatzematge connectat a la xarxa (NAS), **TrueNas i Unraid són dos dels sistemes operatius més coneguts per a ordinadors x86**. Tots dos ofereixen funcions potents per gestionar l'emmagatzematge. La diferència principal és com organitzen els discos.

Aquest article compara **TrueNas** i **Unraid** perquè puguis triar el sistema que s'ajusta a les teves necessitats.

## Visió general d'Unraid

**Unraid és un sistema operatiu NAS propietari desenvolupat per Lime Technology**, una empresa de programari de Califòrnia. Es va crear el 2005 i funciona amb Linux. El seu objectiu és facilitar l'ús de **RAID** eliminant les restriccions de mida, velocitat, marca i protocol dels discos. Això permet ampliar les matrius **RAID** amb facilitat i redueix el risc de perdre dades.

{{< youtube id="GIpf4DmJgcA" >}}

______

## Introducció a TrueNas

**TrueNas, abans conegut com a **FreeNas**, és un sistema operatiu NAS de codi obert desenvolupat per iXsystems**, una empresa privada amb seu a San Jose, Califòrnia. Es va llançar el 2005 i es basa en **FreeBSD** i Linux. Els desenvolupadors se centren en el mercat empresarial. L'ús d'**OpenZFS** com a sistema de fitxers predeterminat reflecteix aquest enfocament.

{{< youtube id="eex67WDeN04" >}}
______

## Cost

Els usuaris domèstics que busquen el millor [sistema operatiu NAS](https://simeononsecurity.com/articles/nas-os-comparison-best-storage-solution/) sovint tenen en compte el **cost**. En aquest aspecte, **TrueNas CORE és gratuït i de codi obert**[^1][^2]. És la versió adreçada a usuaris domèstics i a aplicacions d'emmagatzematge no crítiques.

**Unraid és de pagament**, però no té subscripcions ni comissions ocultes[^3]. Els tres plans només es diferencien pel nombre de dispositius d'emmagatzematge que s'hi poden connectar. El pla **Basic costa $59**[^4], el pla **Plus costa $89**[^5] i el pla **Pro costa $129**[^6].

[^1]: [TrueNas CORE](https://www.truenas.com/products/truenas-core/)
[^2]: [Documentació de TrueNas: primers passos](https://www.truenas.com/docs/hub/gettingstarted/intro/)
[^3]: [Preus d'Unraid](https://unraid.net/pricing)
[^4]: [Pla Unraid Basic](https://unraid.net/pricing/basic)
[^5]: [Pla Unraid Plus](https://unraid.net/pricing/plus)
[^6]: [Pla Unraid Pro](https://unraid.net/pricing/pro)

Són preus històrics de la publicació original. Consulta els [preus actuals d'**Unraid**](https://unraid.net/pricing) abans de comprar. Els límits de llicència, els noms dels plans i les funcions incloses poden canviar.

______

## Facilitat d'ús

**Unraid destaca per la facilitat d'ús i la flexibilitat**[^1]. El seu sistema de gestió permet combinar discos de mides i tipus diferents[^2]. També permet afegir o treure discos sense interrompre el sistema. La interfície és senzilla i accessible per a persones sense coneixements tècnics[^3].

**TrueNas s'adreça sobretot al mercat empresarial i requereix més coneixements per configurar-lo i gestionar-lo**[^4]. **OpenZFS** ofereix funcions avançades de protecció, com ara instantànies, compressió de dades i sumes de comprovació per garantir-ne la integritat[^5].

[^1]: [Funcions d'Unraid](https://unraid.net/product/features)
[^2]: [Gestió d'emmagatzematge d'Unraid](https://unraid.net/product/storage)
[^3]: [Interfície d'Unraid](https://unraid.net/product/ui)
[^4]: [Documentació de TrueNas: empreses](https://www.truenas.com/docs/hub/intro/enterprise/)
[^5]: [OpenZFS a TrueNas](https://www.truenas.com/docs/hub/storage/disks-zfs/)

______

## Funcions

Tots dos sistemes admeten **recursos compartits NFS**, **SMB** per a Windows i **AFP** per a macOS i iOS[^1][^2]. **TrueNas** també ofereix **iSCSI**, **LDAP**, **Active Directory** i **Kerberos**[^1]. **Unraid** es diferencia pel suport de contenidors **Docker**, que donen accés a moltes aplicacions[^2].

**TrueNas** incorpora suport per a serveis d'emmagatzematge al núvol com **Amazon S3**, **Google Cloud** i **Microsoft Azure**[^1]. **Unraid** no té suport natiu per al núvol, però es poden configurar solucions de tercers, que poden requerir passos addicionals[^2].

La plataforma Linux d'**Unraid** permet crear màquines virtuals amb **KVM** i assignar-hi dispositius **PCI/USB**, com ara targetes gràfiques. Així pots fer servir el mateix ordinador com a centre multimèdia i per jugar.

**TrueNas** ofereix la tecnologia de contenidors **Jails** i l'opció de virtualització **Bhyve**[^1]. Inclou aplicacions de tercers conegudes, com **Plex**, però la selecció general de programari pot ser més limitada que la d'**Unraid**.

[^1]: [Documentació de TrueNas: funcions](https://www.truenas.com/docs/hub/intro/features/)
[^2]: [Funcions d'Unraid](https://unraid.net/product/features)
______

## Documentació i comunitat

**TrueNas** disposa d'un **centre de documentació complet** amb informació sobre configuració, API i plataformes de maquinari[^1]. La documentació d'**Unraid** és menys extensa, però és fàcil de navegar[^2].

**Unraid** no té una pàgina d'assistència específica. Anima els usuaris a fer preguntes al seu fòrum oficial, conegut per ser amable, informatiu i útil[^2]. **TrueNas** també té un fòrum oficial[^1]. Les converses del fòrum de **TrueNas** poden centrar-se més en l'emmagatzematge empresarial i ser menys acollidores per als principiants.

[^1]: [Documentació de TrueNas](https://www.truenas.com/docs/)
[^2]: [Comunitat d'Unraid](https://forums.unraid.net/)

______

## Comprovacions per decidir l'emmagatzematge el 2026

**TrueNAS** és adequat si vols les funcions de ZFS, el control dels pools i un flux de treball centrat en l'emmagatzematge. **Unraid** és adequat si valores l'expansió amb discos variats i un ecosistema ampli d'aplicacions. La decisió depèn de la disposició dels discos, del valor de les dades i de les teves habilitats de recuperació.

Abans d'instal·lar-lo, respon aquestes preguntes:

- Pots substituir un disc avariat pel model i la capacitat que tens previst comprar?
- On desaràs les instantànies i les còpies de seguretat?
- Com recuperaràs el sistema si falla el dispositiu d'arrencada?
- Quines aplicacions necessiten accés privilegiat a l'emmagatzematge?
- Com provaràs una restauració completa?

Llegeix la [documentació d'emmagatzematge de **TrueNAS**](https://www.truenas.com/docs/scale/scaletutorials/), la [documentació d'**OpenZFS**](https://openzfs.github.io/openzfs-docs/) i la [documentació d'**Unraid**](https://docs.unraid.net/) abans de triar la disposició del pool. Un NAS millora la disponibilitat. Una còpia de seguretat separada protegeix contra esborrats, ransomware i pèrdua de maquinari.

## Conclusió

**TrueNas i **Unraid** són [sistemes operatius NAS](https://simeononsecurity.com/articles/nas-os-comparison-best-storage-solution/) potents i consolidats** que s'adapten a necessitats diferents. **TrueNas** és adequat per a qui té coneixements avançats de gestió d'emmagatzematge i vol la protecció de dades d'**OpenZFS**[^1]. **Unraid** ofereix un sistema NAS flexible i fàcil d'utilitzar per a usuaris domèstics[^2].

| Tema | TrueNAS | Unraid |
|---|---|---|
| Cost | Gratuït i de codi obert (TrueNAS CORE) | Sistema propietari amb plans Basic, Plus i Pro |
| Facilitat d'ús | Orientat a empreses, requereix coneixements avançats | Prioritza la facilitat d'ús i la flexibilitat |
| Funcions | NFS, SMB, AFP, iSCSI, LDAP, Active Directory, Kerberos i serveis al núvol | NFS, SMB, AFP, contenidors Docker i màquines virtuals amb KVM |
| Protecció de dades | Protecció avançada amb el sistema de fitxers OpenZFS | Combina discos de mides i tipus diferents |
| Aplicacions de tercers | Selecció limitada, amb Jails per a contenidors i Bhyve per a virtualització | Gran varietat d'aplicacions de tercers amb Docker |
| Documentació | Documentació completa i fòrum oficial | Documentació menys extensa i fòrum útil |
| Suport de la comunitat | Fòrum oficial per demanar ajuda i compartir coneixements | Fòrum oficial conegut per ser amable, informatiu i útil |

En resum:

### Avantatges de TrueNas
- Sistema operatiu **[NAS gratuït i de codi obert](https://simeononsecurity.com/articles/nas-os-comparison-best-storage-solution/)**.
- **Protecció de dades avançada amb OpenZFS**.
- **Bon rendiment per a l'emmagatzematge empresarial**.

### Inconvenients de TrueNas
- **És més difícil d'utilitzar per a persones sense coneixements tècnics.**
- **El fòrum de la comunitat pot ser poc acollidor per als principiants.**

### Avantatges d'Unraid
- **Configuració senzilla i fàcil d'utilitzar.**
- Accés a una **gran varietat d'aplicacions de tercers** mitjançant Docker.
- **Fòrum amable i informatiu.**

### Inconvenients d'Unraid
- **El rendiment pot ser inferior al de TrueNas.**

La decisió entre **TrueNas** i **Unraid** depèn de les teves necessitats i experiència tècnica. Compara les funcions i els avantatges segons els teus requisits abans de decidir.

[^1]: [Documentació de TrueNas](https://www.truenas.com/docs/)
[^2]: [Lloc web d'Unraid](https://unraid.net/)

## Cicle de vida actual de TrueNAS

La comparació original descriu **TrueNAS** CORE i **FreeBSD**. La [guia de migració de **TrueNAS**](https://www.truenas.com/docs/scale/26/gettingstarted/migrate/) identifica la versió 13.3-U1.2 com l'última de la sèrie CORE 13.3 i orienta els usuaris cap a Community Edition, basada en Linux. La [pàgina d'estat del programari](https://www.truenas.com/docs/softwarereleases/) mostra les versions compatibles.

| Pregunta | TrueNAS | Unraid |
|---|---|---|
| **Estat de la plataforma** | Confirma la versió actual de Community Edition o Enterprise abans de desplegar-la | Confirma la versió estable actual i les condicions de la llicència |
| **Model d'emmagatzematge** | El disseny dels vdev dels pools OpenZFS es decideix en crear el pool | Les matrius de paritat admeten discos de capacitats diferents dins dels límits documentats |
| **Límit d'expansió** | L'expansió del pool depèn del disseny dels vdev i del suport de la versió | Substituir discos i reconstruir la paritat requereix comprovar capacitat, temps i estat dels discos |
| **Límit de les aplicacions** | El suport d'aplicacions i contenidors depèn de la versió de TrueNAS | El suport de Docker i màquines virtuals depèn de la versió d'Unraid i del maquinari |

**La redundància no és una còpia de seguretat.** Fes servir una destinació de còpia independent i prova la restauració abans de desar-hi dades irrecuperables.

## Tria segons les necessitats de recuperació

Tria **TrueNAS amb OpenZFS** quan les sumes de comprovació, les instantànies, la replicació i un disseny planificat del pool siguin més importants que l'expansió fàcil disc per disc. Tria **Unraid** quan prioritzis créixer amb discos variats, allotjar aplicacions i començar amb una configuració senzilla. Són criteris per decidir, no afirmacions universals sobre el rendiment.

- Abans de desar dades, documenta el disseny del pool o de la matriu, les funcions dels discos, la capacitat útil i el procediment de substitució.
- Anota les dades de les aplicacions: els camins dels contenidors, els discos de les màquines virtuals, les bases de dades, els secrets i els muntatges externs.
- Anota la destinació de les còpies, el xifratge, la retenció i la ruta de xarxa.
- Prova de restaurar un fitxer, un conjunt de dades d'una aplicació i un recurs compartit complet.
- Registra també la ruta d'actualització, la versió següent compatible, el mètode de reversió i la finestra de manteniment.

La [guia de còpies de seguretat de CISA](https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf) descriu el model 3-2-1. Aplica'l a tots dos sistemes i prova la restauració després de canvis a l'emmagatzematge.
