---
title: "Contournement du BGW-320 : Utilisation d'un COTS ONT des Açores - Un guide étape par étape"
draft: false
toc: true
date: 2023-04-30
description: "Apprenez à contourner le BGW-320 et à utiliser un COTS ONT fabriqué par Azores pour vous connecter au réseau de votre FAI grâce à ce guide facile à suivre."
tags: ["COTS ONT","BGW-320","Açores","fibre","réseau","XGS-PON",« Ethernet »,"IP passthrough","personnalisation","FAI","ont ID","Adresse Mac","identifiant de l'équipement","version d'images","Version matérielle","telnet","Demande CLI","interface graphique Web","configuration usine","problèmes de compatibilité"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un technicien de dessin animé tenant un COTS ONT avec un câble à fibre en arrière-plan."
coverCaption: ""
---

## Comment contourner le BGW-320 et utiliser un WAG-D20 des Açores

La plupart des utilisateurs de la fibre ont deux façons de se connecter à Internet : la fibre vers un ONT, l'Ethernet vers une passerelle ou la fibre directement vers la passerelle. Dans cet article, nous allons nous concentrer sur la manière de contourner le BGW-320 et d'utiliser un COTS ONT fabriqué par Azores.

### Aspects techniques

Le[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Accès à l'appareil

L'adresse IP par défaut de l'appareil est 192.168.1.1 et son adresse de passerelle a une faute de frappe d'usine utilisant une adresse IP publique, c'est-à-dire qu'elle affiche 192.162.1.1 au lieu de 192.168.1.1.

Une fois qu'il démarre, vous devez appuyer sur Entrée pour obtenir une invite de connexion sur l'interface série TTL (115200 8N1). Cet appareil dispose d'un système d'image A/B avec une partition superposée contenant tous les fichiers que vous personnalisez.
 
### Crédits

- `admin`/`ADMIN123!@#` - Connexion administrateur pour l'interface graphique Web
- `Invité`/`bienvenue` - Connexion invité
- `test`/`default` - Connexion usine

### Interface Ethernet

Connectez votre client au port Ethernet 10G et configurez-le avec une adresse dans le réseau 192.168.1.x/24 comme - 192.168.1.2/255.255.255.0.

Lors de l'exécution d'une analyse de port à partir de 1-65535, vous remarquerez certains ports ouverts :

- Ports `23` & `8009` - Telnet, nécessite une connexion, exécute l'application CLI.
- Port `10002` - Inconnu
- Port '80' - WebUI, seulement deux fonctions

### Personnalisation de l'ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Vient maintenant la partie importante, c'est-à-dire la modification de certaines informations sur l'appareil pour le rendre compatible avec le réseau de votre FAI.

Tout d'abord, récupérez les informations suivantes auprès de votre passerelle ISP ou ONT :

1. **ID ONT**
2. **Adresse MAC**
3. **Identifiant de l'équipement**
4. **Version d'images**
5. **Version matérielle**

Remarque : il s'agit des valeurs OMCI et non de celles de l'interface utilisateur Web.

Telnet à votre ONT personnel (telnet 192.168.1.1), connectez-vous en tant que **`test`** en utilisant le mot de passe **`default`** et exécutez la commande 'test' pour passer en mode de configuration d'usine.

Affichez les valeurs actuellement définies avec la commande 'show' :

- "montrer gpon mac"
- `montrer sn`
- "Afficher l'identifiant de l'équipement"

Une fois cela fait, personnalisez les paramètres avec les commandes suivantes en remplaçant x par les valeurs de votre appareil :

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <insert ONT ID here>`

Pour HUMAX :

- `Définir l'identifiant de l'équipement "iONT320500G"`
- `config ONU-G_Version "BGW320-500_2.1"`

Pour Nokia :

- `définir l'identifiant de l'équipement "iONT320505G"`
- `config ONU-G_Version "BGW320-505_2.2"`

Remarque : Les deux dernières commandes doivent être appliquées à partir de telnet connecté en tant qu'utilisateur **`test`**.

### Redémarrez et profitez du véritable relais IP

Après la personnalisation, redémarrez l'ONT et profitez d'un véritable relais IP.

### Dépannage et étapes supplémentaires
Pour plus d'informations sur ce sujet, veuillez consulter le[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusion

En suivant ces étapes, on peut contourner avec succès le BGW-320 et utiliser COTS ONT fabriqué par les Açores pour se connecter au réseau de leur FAI. Cependant, soyez prudent lors de la saisie des commandes et assurez-vous de remplacer correctement "x" par les valeurs de votre appareil, sinon vous risquez de rencontrer des problèmes de compatibilité pouvant entraîner des échecs de connexion.


