---
title: "Gaming the Helium Network: Exploiting Vulnerabilities with MiddleMan and Chirp Stack Packet Multiplexer"
date: 2023-02-18
toc: true
draft: false
description: "Apprenez à déjouer le réseau Helium en exploitant les vulnérabilités avec MiddleMan et Chirp Stack Packet Multiplexer, ainsi que les risques et les conséquences de le faire."
tags: ["Réseau Hélium","Preuve de couverture","Intermédiaire","Multiplexeur de paquets de pile de Chirp","jeu","exploiter les vulnérabilités","Réseau LoRaWAN","crypto-monnaie","chaîne de blocs","réseau décentralisé","points chauds","usurpation d'identité","tricherie","activité illégale","pénalités","l'intégrité du réseau","récompenses","acteurs malveillants","sécurité Internet","hôtes légitimes"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "Une représentation caricaturale d'un groupe d'individus exploitant un ballon à hélium avec une image d'une passerelle LoRaWAN® et d'un multiplexeur MiddleMan ou Chirp Stack Packet en arrière-plan."
coverCaption: ""
---

**Clause de non-responsabilité**
Il est important de noter que le jeu sur le réseau Helium est une activité illégale et contraire à l'éthique qui est fortement désapprouvée par la communauté Helium et la communauté plus large de la crypto-monnaie et de la blockchain. Le jeu sur le réseau compromet l'intégrité du réseau et nuit aux hôtes légitimes qui fournissent une couverture précieuse au réseau.

De plus, bien que l'utilisation de MiddleMan et de Chirp Stack Packet Multiplexer pour exploiter les vulnérabilités du réseau Helium puisse être une source de préoccupation, il est important de noter que ces problèmes ne peuvent être résolus par Helium qu'en introduisant des passerelles sécurisées. Cela nécessiterait le remplacement de tous les points d'accès sur le réseau, ce qui est une entreprise importante et peut ne pas être réalisable. En conséquence, la communauté Helium doit rester vigilante et proactive pour relever les défis posés par les jeux sur le réseau.

Il convient également de noter que l'équipe Helium est consciente du problème depuis un certain temps et a pris des mesures pour y remédier, mais d'autres mesures sont nécessaires pour résoudre le problème. La communauté demande que des mesures concrètes soient prises pour remédier à ces vulnérabilités et pour garantir que le réseau puisse continuer à évoluer et à se développer de manière sécurisée et digne de confiance.

En écrivant cet article, nous espérons sensibiliser à la question des jeux sur le réseau Helium et à l'utilisation de MiddleMan et Chirp Stack Packet Multiplexer pour exploiter les vulnérabilités du système. Nous pensons qu'en faisant la lumière sur ce problème et en y apportant plus de publicité, la communauté Helium et la communauté plus large de la blockchain et de la crypto-monnaie peuvent se réunir pour résoudre le problème et travailler à un réseau plus sûr et plus fiable.

De plus, en mettant en évidence ce problème, nous espérons encourager l'équipe Helium à prendre des mesures plus décisives pour remédier aux vulnérabilités du réseau et à mettre en œuvre des mesures de sécurité plus robustes pour empêcher les jeux à l'avenir. Nous pensons qu'il est important pour l'équipe Helium d'être transparente sur ses efforts pour résoudre ce problème et de communiquer avec la communauté sur ses progrès dans la résolution de ces vulnérabilités.

Enfin, en apportant plus de publicité à ce problème, nous espérons encourager une plus grande sensibilisation et éducation sur les risques et les conséquences du jeu sur le réseau Helium. Il est important que les utilisateurs comprennent l'importance d'un comportement éthique sur le réseau et les dommages potentiels qui peuvent être causés par les jeux. En travaillant ensemble pour résoudre ces problèmes, nous pouvons contribuer à assurer la croissance et le succès continus du réseau Helium.

En résumé, jouer sur le réseau Helium n'est pas toléré par la communauté ou par nous, et nous encourageons les utilisateurs à agir de manière éthique et légale lorsqu'ils participent au réseau. Bien qu'il existe des vulnérabilités dans le réseau qui peuvent être exploitées, il est important de rester vigilant et proactif pour résoudre ces problèmes et de travailler à un réseau plus sûr et plus fiable pour tous les utilisateurs.

# Comment jouer au réseau Helium avec MiddleMan et Chirp Stack Packet Multiplexer
Le réseau Helium est un réseau LoRaWAN® décentralisé qui compense ceux qui hébergent des hotspots physiques en les récompensant avec des jetons Helium, ou $HNT. Ce système est connu sous le nom de Proof-of-Coverage (PoC). Au fur et à mesure que le réseau s'est développé et que la sensibilisation à ce projet a augmenté, il y a eu un nombre croissant de tricheurs qui exploitent le protocole et les mécanismes de récompense. Dans cet article, nous verrons comment jouer au réseau Helium en utilisant MiddleMan et Chirp Stack Packet Multiplexer.

## Comprendre le problème du jeu en réseau Helium
Le réseau Helium s'appuie sur la preuve de couverture pour s'assurer que les hotspots fournissent une couverture là où elle est nécessaire. Cependant, ce système est vulnérable aux jeux, à l'usurpation d'identité, au piratage et à d'autres types de mauvais comportements qui peuvent endommager le réseau. Le problème de jeu sur le réseau Helium coûte aux hôtes légitimes des milliers de $HNT par mois. Helium, Inc, avec DeWi, a pris des mesures agressives au début de 2022 pour aider à éliminer ce problème.

## Matériel requis
-[Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
-[Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
-[Raspberry Pi](https://amzn.to/3KjFCYp)
-[Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## Utilisation de MiddleMan pour jouer au réseau Helium
Une façon de jouer au réseau Helium consiste à utiliser MiddleMan. MiddleMan est un outil logiciel qui peut être utilisé pour créer un faux point d'accès qui semble fournir une couverture à un endroit spécifique. En utilisant MiddleMan, un utilisateur peut créer un faux point d'accès qui recevra des récompenses pour fournir une couverture dans une zone particulière, même si le point d'accès n'est pas physiquement situé dans cette zone.

Pour utiliser MiddleMan, un utilisateur doit installer le logiciel et créer un faux hotspot. L'utilisateur peut ensuite configurer le point d'accès pour signaler sa position au réseau Helium à l'aide d'un outil d'usurpation GPS. Le réseau Helium croira que le faux point d'accès fournit une couverture à l'emplacement spécifié et récompensera l'utilisateur avec $HNT.

Vous configurez votre passerelle lorawan pour pointer vers ce logiciel et il manipule les valeurs afin que tous les PoC reçus soient considérés comme valides. L'utilisation du transitaire semtech est l'un des différents standards de la communauté LoraWAN. Résoudre le problème de manipulation nécessiterait de réinventer la roue et de mettre en œuvre leur propre protocole à partir de zéro. Des choses comme les sommes de contrôle et le cryptage empêcheraient que cela se produise. Mais il serait également plus difficile pour les fournisseurs de matériel différent de créer des points d'accès. Sans oublier que c'est un cas d'utilisation pris en charge d'avoir un mineur d'hélium et plusieurs passerelles lora pour une meilleure couverture. Bien qu'il s'agisse davantage d'un problème au niveau de l'entreprise.

 -[helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## Utilisation du multiplexeur de paquets Chirp Stack pour jouer au réseau Helium
Une autre façon de jouer au réseau Helium consiste à utiliser Chirp Stack Packet Multiplexer. Chirp Stack Packet Multiplexer est un outil qui peut être utilisé pour créer un point d'accès virtuel pouvant recevoir des paquets de plusieurs points d'accès physiques. En utilisant Chirp Stack Packet Multiplexer, un utilisateur peut créer un point d'accès virtuel qui reçoit des paquets de points d'accès physiques à plusieurs endroits, ce qui augmentera les récompenses gagnées.

Pour utiliser Chirp Stack Packet Multiplexer, un utilisateur doit installer le logiciel et le configurer pour recevoir des paquets de points d'accès physiques ou de passerelles lorawan à plusieurs endroits. Le point d'accès recevra les paquets et signalera son emplacement au réseau Helium, qui récompensera l'utilisateur avec $HNT.

Cela permet plusieurs transitaires entrants et plusieurs passerelles sortantes. Il existe des cas d'utilisation légitimes de ce logiciel dans la communauté LoraWAN, mais son utilisation dans l'hélium est au mieux une zone grise. Cela dépend de la façon dont vous l'utilisez et aussi de votre intention.

La configuration de celui-ci nécessite certains fichiers de configuration. Mais cela peut être fait en 5 minutes ou moins.
-[chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## Risques et conséquences du jeu sur le réseau Helium
Jouer sur le réseau Helium est une activité risquée et illégale qui peut avoir de graves conséquences. Helium, Inc, avec DeWi, travaille activement pour détecter et empêcher les jeux sur le réseau, et les utilisateurs surpris en train de jouer sur le réseau seront pénalisés.

Les pénalités pour les jeux sur le réseau Helium peuvent inclure la perte de l'accès au réseau, l'interdiction permanente des points d'accès et la perte de tout $HNT gagné grâce au jeu. De plus, jouer sur le réseau Helium compromet l'intégrité du réseau et nuit aux hôtes légitimes qui fournissent une couverture précieuse au réseau.

## Conclusion
Bien que le réseau Helium offre aux hôtes de points d'accès légitimes la possibilité de gagner des récompenses grâce à la preuve de couverture, il présente également une cible attrayante pour les acteurs malveillants qui cherchent à déjouer le système. L'utilisation de MiddleMan et de Chirp Stack Packet Multiplexer, bien qu'elle ne soit pas tolérée par Helium Inc. ou la communauté au sens large, est un exemple de la façon dont certains mauvais acteurs exploitent les vulnérabilités du réseau pour récolter des bénéfices aux dépens des autres.

Il est important que la communauté Helium continue de travailler ensemble pour identifier et traiter les jeux sur le réseau, car ils menacent l'intégrité du système et sapent les efforts des hôtes légitimes. Cela peut inclure des efforts pour développer et mettre en œuvre des mesures de détection et de prévention plus sophistiquées, ainsi qu'une sensibilisation et une éducation accrues sur les risques et les conséquences des jeux sur le réseau.

En fin de compte, le succès du réseau Helium dépend de la volonté de ses parties prenantes de travailler ensemble pour construire un système sécurisé, fiable et digne de confiance qui apporte une réelle valeur à ses utilisateurs. En restant vigilante et proactive face aux défis posés par les jeux, la communauté peut aider à garantir que le réseau Helium continue de croître et d'évoluer dans une direction positive.