---
title: "Ubiquiti UniFi Express : test d'une passerelle compacte avec point d'accès WiFi 6"
date: 2024-01-03
lastmod: 2026-11-08
toc: true
draft: false
description: "Test de UniFi Express, une passerelle compacte avec point d'accès WiFi 6 et gestion simplifiée."
genre: ["Tests techniques", "Solutions réseau", "Configuration d'un réseau domestique", "Appareils WiFi 6", "Présentation de UniFi Express", "Passerelle compacte", "Points d'accès sans fil", "Produits Ubiquiti", "Sécurité réseau", "Réseaux de petites entreprises"]
tags: ["UniFi Express", "WiFi 6", "Passerelle réseau", "Ubiquiti", "Point d'accès sans fil", "Test technique", "Sécurité réseau", "Réseaux domestiques", "Passerelle compacte", "Petite entreprise", "Appareil tout-en-un", "Réseau maillé", "Configuration d'appareil", "Connexion Internet", "Solutions Ubiquiti", "Processeur double cœur", "Couverture WiFi", "IDS/IPS", "Options VPN", "Pare-feu basé sur les applications", "UniFi OS", "Réseau maillé sans fil", "Extension du réseau", "Prise en charge de VLAN", "Informations techniques", "Limites de l'appareil", "Ubiquiti Networks", "Performances de routage", "Gestion réseau simplifiée"]
cover: "/img/cover/UniFi_Express_Connectivity.webp"
coverAlt: "Illustration symbolique de UniFi Express montrant son format compact et sa connectivité fluide, qui souligne son efficacité et son innovation"
coverCaption: "Simplifiez. Connectez. Innovez. UniFi Express, votre passerelle pour un réseau facile à gérer."
ref: ["/articles/the-ideal-ubiquiti-unifi-networking-setup-both-simple-and-advanced", "/articles/ubiquiti-unifi-good-for-home-use", "/articles/ubiquiti-unifi-vs-tp-link-omada"]
---
**Ubiquiti UniFi Express : une passerelle compacte et puissante pour les réseaux domestiques et les petites entreprises**

Dans un secteur des réseaux en évolution rapide, UniFi Express d'Ubiquiti se distingue par son format compact et son association d'une passerelle performante et d'un point d'accès WiFi 6. Ce test détaillé examine ses caractéristiques, ses fonctions et ses différences avec d'autres appareils, puis évalue son intérêt pour les réseaux domestiques et les petites entreprises.

## Présentation de UniFi Express

UniFi Express simplifie la gestion réseau en réunissant un pare-feu de nouvelle génération, des fonctions adaptées aux applications et un point d'accès WiFi 6 intégré dans un boîtier compact et élégant. Ce test examine ses capacités et ses limites, puis le compare aux autres passerelles UniFi.

{{< youtube id="VbIamWqXjAk" >}}

______

## Performances techniques : caractéristiques de UniFi Express

{{< figure src="sos-unifi-express.webp" alt="Ubiquiti UniFi Express" caption="Ubiquiti UniFi Express" link="https://amzn.to/418yMvj" >}}

UniFi Express intègre un processeur ARM Cortex-A53 à deux cœurs cadencé à 1 GHz et 1 Go de mémoire DDR3L. Son écran de 0,9 pouce affiche des informations en temps réel et complète ses caractéristiques techniques. Le débit maximal atteint 1 Gbit/s. Certaines limites sont à prendre en compte : les fonctions Suspicious Activity sont absentes et l'appareil ne prend en charge que 5 appareils UniFi.

- **Processeur :** ARM Cortex-A53 à deux cœurs, 1 GHz
- **Mémoire :** 1 Go DDR3L
- **Stockage flash intégré :** 10 Go
- **Écran :** 0,9 pouce
- **Débit SQM maximal :** 1 Gbit/s
- **Ports WAN :** 1x Gigabit RJ45
- **Ports LAN :** 1x Gigabit RJ45
- **Alimentation :** USB-C (5 V / 3 A)
- **Consommation maximale :** 10 W
- **Dimensions :** 98 x 98 x 30 mm

Ces caractéristiques techniques permettent d'évaluer les performances de UniFi Express dans différents environnements réseau.

______

## Fonctionnalités WiFi 6 : le point d'accès intégré

L'un des principaux atouts de UniFi Express est son point d'accès WiFi 6 intégré. Il ne prend pas en charge la bande 6 GHz (WiFi 6E), mais fournit un débit élevé sur les bandes 2,4 GHz et 5 GHz. Sa couverture d'environ 140 m² (1 500 ft²) assure une connexion fiable dans cette zone.

- **Puissance d'émission à 2,4 GHz :** 22 dBm
- **Puissance d'émission à 5 GHz :** 25 dBm
- **MIMO :** 2 x 2 (DL/UL MU-MIMO)
- **Débit à 2,4 GHz :** 573,5 Mbit/s
- **Débit à 5 GHz :** 2,4 Gbit/s
- **Clients simultanés :** plus de 60

UniFi Express peut aussi servir de point d'accès maillé, ce qui facilite l'extension du réseau.

______

## UniFi Express face aux autres passerelles

{{< figure src="sos-unifi-express-vs-unifi-gateway-lite.webp" alt="Ubiquiti UniFi Express comparé à Ubiquiti UniFi Gateway Lite" caption="Ubiquiti UniFi Express comparé à Ubiquiti UniFi Gateway Lite" link="https://amzn.to/3uPFKta" >}}

La comparaison entre UniFi Express, UniFi Gateway Lite, UniFi Dream Router (UDR) et UniFi Dream Machine Pro (UDM Pro/SE) permet de choisir la passerelle adaptée aux besoins du réseau.

### UniFi Express

[**UniFi Express**](https://amzn.to/418yMvj) est une passerelle tout-en-un compacte et puissante avec point d'accès WiFi 6. Il exécute l'application UniFi Network, offre un débit de routage de 1 Gbit/s, intègre un point d'accès et coûte 149 $. Il ne propose pas la détection des menaces IDS et IPS.

### UniFi Gateway Lite

[**UniFi Gateway Lite**](https://amzn.to/3uPFKta) succède à UniFi Security Gateway et nécessite une console supplémentaire pour la gestion. La passerelle coûte 129 $ et offre, comme UniFi Express, un débit de routage de 1 Gbit/s, mais sans point d'accès intégré. Elle prend en charge la détection des menaces IDS et IPS pour une protection avancée.

### UniFi Dream Router (UDR)

[**UniFi Dream Router (UDR)**](https://amzn.to/41rpBq9) est conçu pour les particuliers et réunit plusieurs fonctions dans un seul appareil. Il possède un processeur ARM Cortex-A53 à deux cœurs cadencé à 1 GHz, 2 Go de mémoire et un débit de routage de 1 Gbit/s. UDR exécute UniFi Network et UniFi Protect et prend en charge la détection IDS et IPS. Pour 199 $, il comprend aussi un point d'accès intégré, ce qui le rend adapté à un réseau domestique complet.

### UniFi Dream Machine Pro (UDM Pro/SE)

[**UniFi Dream Machine Pro (UDM Pro/SE)**](https://amzn.to/3uP1tS1) est une solution destinée aux entreprises. Cette passerelle possède un processeur Arm Cortex-A57 à deux cœurs cadencé à 1,7 GHz, 4 Go de RAM et un débit de routage de 10 Gbit/s. Elle prend en charge UniFi Network et UniFi Protect, la détection des menaces IDS et IPS et plusieurs ports PoE. Elle convient aux réseaux de plus grande taille. Son prix varie de 379 à 499 $. Elle offre de nombreuses fonctions pour les installations complexes.

### Choisir la bonne passerelle

Pour choisir entre ces passerelles, évaluez les besoins de votre réseau. UniFi Express convient si vous recherchez une gestion simple, un format compact et une protection de base contre les menaces. UniFi Gateway Lite est plus adaptée si la détection avancée des menaces est prioritaire. UniFi Dream Router cible les particuliers et UniFi Dream Machine Pro/SE les entreprises, avec des fonctions pour les réseaux plus étendus.

______

## Configurer UniFi Express : une mise en route simple

UniFi Express confirme sa réputation de produit prêt à l'emploi lors de la configuration. Branchez-le à Internet via le port WAN et lancez l'application UniFi Network sur votre téléphone pour démarrer la configuration simplifiée. Un compte Ubiquiti est nécessaire pour associer l'appareil à son interface logicielle conviviale.

### Configuration initiale

1. Connectez UniFi Express à Internet.
2. Ouvrez l'application UniFi Network sur votre téléphone.
3. Suivez les instructions à l'écran, attribuez un nom à UniFi Express et configurez le réseau sans fil.
4. Connectez-vous au nouveau réseau sans fil lorsque l'application vous y invite.

La simplicité de la configuration fait de UniFi Express un bon choix pour les personnes qui privilégient la facilité sans renoncer aux fonctionnalités.

#### Configurer UniFi Network

Il est préférable de modifier les paramètres réseau dans l'application UniFi Network accessible depuis un navigateur. Connectez-vous à l'adresse IP de la passerelle ou sur [https://unifi.ui.com](https://unifi.ui.com) pour accéder aux paramètres. La vidéo ci-dessous montre la configuration complète des appareils Ubiquiti UniFi.

{{< youtube id="bWJNZvXXgf8" >}}

______

## UniFi Express comme point d'accès maillé : plus de possibilités

En plus de son rôle de passerelle autonome, UniFi Express peut servir de point d'accès maillé dans un réseau existant. Vous pouvez utiliser une liaison montante filaire ou sans fil. L'appareil s'intègre facilement et offre de la souplesse.

- **Appareils pris en charge :** 4 autres appareils UniFi Network
- **Deux ports utilisables en LAN :** oui, en mode maillé
- **Compatibilité maillée :** tous les points d'accès UniFi de 2e génération ou ultérieurs
- **Prise en charge des VLAN :** indisponible sur les ports LAN/WAN
- **Passerelle pour CloudKey :** non, UniFi Gateway Lite est nécessaire

Cette souplesse permet à UniFi Express de fonctionner comme point d'accès et d'étendre le réseau lorsque les besoins évoluent.

______

## Foire aux questions

{{< youtube id="0A7a9_6ZgCU" >}}

1. **Combien d'appareils UniFi Express (UX) prend-il en charge ?**
   - UniFi Express peut gérer 4 autres appareils UniFi Network.

2. **Peut-on utiliser les deux ports comme ports LAN en mode maillé ?**
   - Oui. Lorsque UniFi Express est connecté à un réseau maillé, les deux ports peuvent servir de ports LAN.

3. **UX peut-il créer un réseau maillé avec les points d'accès UniFi classiques ?**
   - Oui. UX est compatible avec tous les points d'accès UniFi de 2e génération ou ultérieurs.

4. **Les ports LAN/WAN prennent-ils en charge les VLAN ?**
   - Il n'est pas possible d'attribuer des VLAN aux ports LAN ou WAN.

5. **UniFi Express peut-il servir de passerelle pour un CloudKey ?**
   - Non. Si vous utilisez un CloudKey, UX peut uniquement servir de point d'accès. UniFi Gateway Lite est alors nécessaire.

______

## En résumé

UniFi Express est une passerelle Cloud d'entrée de gamme intéressante, surtout pour les réseaux domestiques simples et les petits bureaux. Le nombre d'appareils pris en charge est limité et IDS/IPS est absent, mais son format compact et son point d'accès intégré en font une solution tout-en-un intéressante. Si les besoins réseau évoluent, UniFi Express peut continuer à servir de point d'accès.

______

## Références

1. [Page produit Ubiquiti UniFi Express](https://store.ui.com/us/en/pro/category/all-unifi-cloud-gateways/products/ux)
2. [Page produit Ubiquiti UniFi Gateway Lite](https://store.ui.com/us/en/products/uxg-lite)
3. [Documentation Ubiquiti](https://help.ui.com/hc/en-us)
4. [Application UniFi Network](https://apps.apple.com/us/app/unifi/id1057750338) (iOS)
5. [Application UniFi Network](https://play.google.com/store/apps/details?id=com.ubnt.easyunifi&hl=en_US&gl=US) (Android)
6. [Mises à jour UniFi OS](https://community.ui.com/releases)
7. [Test de UniFi Express par LazyAdmin](https://lazyadmin.nl/home-network/unifi-express-review/#:~:text=The%20UniFi%20Express%20is%20really,takes%20a%20couple%20of%20minutes.)