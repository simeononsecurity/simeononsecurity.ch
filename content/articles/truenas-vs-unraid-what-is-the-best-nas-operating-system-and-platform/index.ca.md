---
title: "Unraid vs TrueNas: quin sistema operatiu NAS és adequat per a vostè?"
date: 2023-02-16
toc: true
draft: false
description: "Una comparació completa d'Unraid i TrueNas, que inclou la seva facilitat d'ús, característiques, documentació i comunitat, per ajudar els usuaris a prendre una decisió informada sobre quin sistema operatiu NAS s'adapta millor a les seves necessitats."
tags: ["Unraid", "TrueNAS", "Sistema operatiu NAS", "Comparació", "Facilitat d'usuari", "Característiques", "Documentació", "Comunitat", "Codi obert", "Empresa", "Protecció de dades", "Rendiment", "Flexibilitat", "Fàcil d'usar", "Aplicacions de tercers", "Emmagatzematge connectat a la xarxa", "Tecnologia RAID", "Gestió d'emmagatzematge", "OpenZFS", "Usuaris domèstics", "Model de preus", "Emmagatzematge al núvol", "Virtualització", "Centre de documentació", "Fòrum comunitari", "Protecció de dades avançada", "Sistema operatiu NAS madur", "Experiència tècnica", "Professionals informàtics"]
cover: "/img/cover/Two_computer_servers_facing_each_other_one_blue_one_green.png"
coverAlt: "Dos servidors enfrontats, un blau i un altre verd. Al costat blau hi ha una persona que porta un casc i armilla de seguretat. Al costat verd una persona asseguda al sofà."
coverCaption: ""
---

Quan es tracta de **crear un sistema d'emmagatzematge connectat a la xarxa (NAS), dos dels sistemes operatius més coneguts per a ordinadors basats en x86 són TrueNas i Unraid**. Tots dos ofereixen funcions potents per gestionar un sistema NAS, però la seva diferència principal rau en el seu mètode de gestió d'emmagatzematge.

En aquest article, compararem TrueNas i Unraid per ajudar-vos a prendre la millor decisió per a les vostres necessitats.

## Visió general de Unraid

**Unraid és un sistema operatiu NAS propietari desenvolupat per Lime Technology**, una empresa de programari ubicada a Califòrnia. Es va establir l'any 2005 i s'executa a la plataforma Linux. L'objectiu d'Unraid és fer que la tecnologia RAID sigui més accessible eliminant les restriccions de mida, velocitat, marca i protocol del disc. Això permet una fàcil expansió de les matrius RAID i minimitza el risc de pèrdua de dades.

______

## Introducció a TrueNas

**TrueNas, abans conegut com FreeNas, és un sistema operatiu NAS de codi obert desenvolupat per iXsystems**, una empresa privada amb seu a San Jose, Califòrnia. Es va llançar el 2005 i està construït sobre FreeBSD i Linux. Els desenvolupadors de TrueNas es concentren en el mercat empresarial i la seva elecció del sistema de fitxers predeterminat (OpenZFS) reflecteix aquest enfocament.

______

## Cost

**Els usuaris domèstics que cerquen el millor sistema operatiu NAS solen tenir preocupacions pel cost**. En aquest sentit, TrueNas és un clar guanyador ja que és de codi obert i totalment gratuït, almenys per a TrueNas CORE, la versió adreçada a usuaris domèstics i aplicacions d'emmagatzematge no crítiques.

En canvi, Unraid no és gratuït, però utilitza un model de preus justos sense subscripcions ni comissions ocultes. Hi ha tres plans Unraid per triar, cadascun només difereix pel nombre de dispositius d'emmagatzematge que es poden connectar. El pla bàsic costa 59 dòlars, el pla Plus costa 89 dòlars i el pla Pro costa 129 dòlars.

______

## Facilitat d'usuari

**Unraid posa un gran èmfasi en la facilitat d'ús i la flexibilitat**. Disposa d'un sistema de gestió d'emmagatzematge únic que permet als usuaris barrejar i combinar diferents mides i tipus de disc i afegir o treure discs sense cap interrupció. També ofereix una interfície d'usuari senzilla i senzilla, que fa que fins i tot els usuaris no tècnics puguin configurar i gestionar un sistema NAS.

**TrueNas, en canvi, està orientat al mercat empresarial i requereix un coneixement més avançat per configurar-lo i gestionar**. La seva elecció del sistema de fitxers OpenZFS proporciona funcions avançades de protecció de dades, com ara instantànies, compressió de dades i suma de comprovació per garantir la integritat de les dades.

______

## Característiques

**TrueNas i Unraid ofereixen suport** per a recursos compartits de NFS, SMB per a Windows i AFP per a macOS i iOS. A més, TrueNas ofereix serveis iSCSI, LDAP, Active Directory i Kerberos. Unraid no ofereix aquests serveis, però sí que és compatible amb els contenidors Docker, donant accés als usuaris a una gran varietat d'aplicacions.

**TrueNas també té suport integrat per a serveis d'emmagatzematge al núvol** com Amazon S3, Google Cloud i Microsoft Azure, cosa que facilita el transport de dades al núvol. Els usuaris no atacats poden utilitzar solucions de tercers, però poden requerir una configuració i una configuració addicionals.

**La plataforma basada en Linux d'Unraid també permet la configuració de màquines virtuals** mitjançant KVM i assignant dispositius PCI/USB, com ara targetes gràfiques, a màquines virtuals. Això fa possible utilitzar el mateix ordinador tant per al centre multimèdia com per als jocs.

**TrueNas inclou la seva pròpia tecnologia de contenidors**, Jails, i la seva pròpia opció de virtualització, Bhyve. Tot i que TrueNas ofereix moltes de les aplicacions populars de tercers, com ara Plex, la selecció global de programari pot ser més petita en comparació amb Unraid.

______

## Documentació i comunitat

TrueNas té un centre de documentació complet, que cobreix tot, des de la configuració fins a les API i plataformes de maquinari. El lloc web Unraid té una secció de documentació menys extensa, però és més fàcil de navegar. Tanmateix, Unraid no té una pàgina d'assistència individual, però es recomana als usuaris que facin preguntes al fòrum oficial de la comunitat, que es descriu com a amigable, informatiu i útil.

TrueNas també té el seu propi fòrum oficial de la comunitat, però pot ser que no sigui tan acollidor per als principiants com el fòrum Unraid. Això es deu al fet que molts usuaris de TrueNas són professionals informàtics centrats en la gestió de l'emmagatzematge empresarial.

______

## Conclusió

Tant TrueNas com Unraid són sistemes operatius NAS potents i madurs, cadascun amb els seus propis punts forts i febles. TrueNas és ideal per a aquells amb coneixements avançats de gestió d'emmagatzematge i que volen les funcions avançades de protecció de dades d'OpenZFS. Unraid, d'altra banda, és millor per als usuaris domèstics que volen un sistema NAS flexible i fàcil d'utilitzar.

En resum:

**Pros de TrueNas:**
- Gratuït i de codi obert
- Protecció de dades avançada amb OpenZFS
- Gran actuació

**Contres de TrueNas:**
- Més difícil d'utilitzar
- Comunitat hostil

**Pros sense atac:**
- Fàcil d'usar
- Gran varietat d'aplicacions de tercers
- Comunitat amable

**Contres sense atac:**
- Rendiment limitat

En última instància, la decisió entre TrueNas i Unraid es reduirà a les vostres necessitats específiques i al vostre nivell d'experiència tècnica. Considereu els vostres requisits, compareu les característiques i els avantatges de cadascun i preneu una decisió informada.
