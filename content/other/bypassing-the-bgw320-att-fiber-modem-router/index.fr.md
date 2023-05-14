---
title: "Contourner le BGW-320 : Utilisation d'un ONT COTS Azores - Guide étape par étape"
draft: false
toc: true
date: 2023-04-30
description: "Apprenez à contourner le BGW-320 et à utiliser un ONT COTS fabriqué par Azores pour vous connecter au réseau de votre FAI grâce à ce guide facile à suivre."
tags: ["COTS ONT", "BGW-320", "Açores", "fibre", "réseau", "XGS-PON", "Ethernet", "Passage IP", "personnalisation", "FAI", "ont ID", "Adresse MAC", "ID de l'équipement", "image version", "version du matériel", "telnet", "Application CLI", "interface graphique web", "mode de configuration d'usine", "problèmes de compatibilité"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un technicien en dessin animé tenant un ONT COTS avec un câble en fibre optique en arrière-plan."
coverCaption: ""
---

## Comment contourner le BGW-320 et utiliser un Azores WAG-D20

La plupart des utilisateurs de fibre optique ont deux façons de se connecter à l'internet - la fibre vers un ONT, l'Ethernet vers une passerelle ou la fibre directement vers la passerelle. Dans cet article, nous allons nous concentrer sur la manière de contourner le BGW-320 et d'utiliser un ONT COTS fabriqué par Azores.

### Aspects techniques

Les[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Accès au dispositif

L'adresse IP par défaut de l'appareil est 192.168.1.1 et son adresse de passerelle comporte une faute de frappe d'usine utilisant une adresse IP publique, c'est-à-dire qu'elle indique 192.162.1.1 au lieu de 192.168.1.1.

Une fois qu'il a démarré, vous devez appuyer sur la touche Entrée pour obtenir une invite de connexion sur l'interface série TTL (115200 8N1). Cet appareil dispose d'un système d'image A/B avec une partition superposée contenant tous les fichiers que vous personnalisez.
 
### Références

-`admin``ADMIN123!@#` - Connexion de l'administrateur pour l'interface graphique web
-`Guest``welcome` - Guest login
-`test``default` - Connexion à l'usine

### Interface Ethernet

Connectez votre client au port Ethernet 10G et configurez-le avec une adresse dans le réseau 192.168.1.x/24 comme - 192.168.1.2/255.255.255.0.

En effectuant un balayage des ports de 1 à 65535, vous remarquerez que certains ports sont ouverts :

- Ports`23` &`8009` - Telnet, nécessite une connexion, exécute l'application CLI.
- Port`10002` - Inconnu
- Port`80` - WebUI, seulement deux fonctions

### Personnaliser l'ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Maintenant vient la partie importante, c'est-à-dire la modification de certaines informations sur l'appareil pour le rendre compatible avec le réseau de votre fournisseur d'accès.

Tout d'abord, récupérez les informations suivantes de la passerelle ou de l'ONT de votre FAI :

1. **ONT ID**
2. **Adresse MAC**
3. **Identification de l'équipement**
4. **Version de l'image**
5. **Version du matériel**

Remarque : il s'agit des valeurs de l'OMCI et non de celles de l'interface web.

Telnet à votre ONT personnel (telnet 192.168.1.1), login comme **`test` l'utilisation de la **`default` et exécutez la commande "test" pour passer en mode de configuration d'usine.

Affichez les valeurs actuellement définies à l'aide de la commande "show" :

-`show gpon mac`
-`show sn`
-`show equipment id`

Une fois cela fait, personnalisez les paramètres à l'aide des commandes suivantes en remplaçant x par les valeurs de votre appareil :

-`set gpon mac xx:xx:xx:xx:xx:xx`
-`set sn <insert ONT ID here>`

Pour HUMAX :

-`set equipment id “iONT320500G”`
-`config ONU-G_Version "BGW320-500_2.1”`

Pour Nokia :

-`set equipment id “iONT320505G”`
-`config ONU-G_Version "BGW320-505_2.2”`

Note : Les deux dernières commandes doivent être appliquées à partir de telnet en tant que **.`test` l'utilisateur.

### Redémarrez et profitez d'un véritable IP Passthrough

Après la personnalisation, redémarrez l'ONT et profitez du véritable IP Passthrough.

### Dépannage et étapes supplémentaires
Pour plus d'informations sur ce sujet, veuillez consulter la page[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusion

En suivant ces étapes, il est possible de contourner le BGW-320 et d'utiliser l'ONT COTS fabriqué par Azores pour se connecter au réseau de son fournisseur d'accès. Cependant, soyez prudent lorsque vous entrez les commandes et assurez-vous de remplacer 'x' par les valeurs de votre appareil correctement, sinon vous risquez de rencontrer des problèmes de compatibilité qui peuvent entraîner des échecs de connexion.


