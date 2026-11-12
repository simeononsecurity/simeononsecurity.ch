---
title: "Planifier et tester la segmentation VLAN d'un homelab"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Élaborez un plan VLAN pour les appareils de confiance, les serveurs, l'IoT et les visiteurs. Cartographiez les flux autorisés, configurez le réseau par étapes et vérifiez l'isolation."
genre: ["Homelab", "Sécurité réseau", "Réseaux"]
tags: ["VLAN homelab", "segmentation VLAN", "réseau IoT", "réseau invité", "pare-feu homelab", "routage inter-VLAN", "802.1Q", "isolation réseau", "test VLAN", "VLAN pfSense", "port d'accès", "port trunk", "règles de pare-feu", "sécurité homelab", "plan réseau", "sous-réseau", "DHCP", "DNS", "commutateur administrable", "SSID sans fil"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Un routeur et un commutateur de homelab séparent les ordinateurs portables, serveurs, appareils IoT et visiteurs en zones réseau protégées."
coverCaption: "Planifiez les limites des VLAN, puis testez chaque chemin autorisé et bloqué."
---

Dans un homelab, les ordinateurs portables, serveurs, caméras et appareils des visiteurs partagent souvent le même réseau. La **segmentation VLAN** répartit ces groupes sur des réseaux distincts. Un routeur, un pare-feu ou un commutateur de couche 3 achemine le trafic entre eux. Les règles du pare-feu ou les listes de contrôle d'accès du commutateur encadrent ces flux routés. Ce guide vous aide à préparer un plan, appliquer une modification à la fois et vérifier le résultat.

## À retenir

- **Groupez selon le niveau de confiance :** placez les appareils d'administration, les serveurs, les appareils IoT et les visiteurs sur des réseaux séparés lorsque leurs besoins d'accès diffèrent.
- **Notez les chemins autorisés :** pour chaque liaison entre réseaux, consignez la source, la destination, le service et le motif.
- **Configurez les deux couches :** les paramètres du commutateur et du point d'accès placent les appareils dans les VLAN. Les règles du pare-feu ou les listes de contrôle d'accès du commutateur contrôlent le trafic routé.
- **Testez les deux résultats :** vérifiez une connexion autorisée et une connexion refusée depuis chaque réseau concerné.

## Avant de commencer

Il vous faut un routeur ou un pare-feu avec des interfaces VLAN, ou un commutateur de couche 3 prenant en charge le routage VLAN et les listes de contrôle d'accès. Un commutateur administrable transporte les VLAN filaires. Si vous séparez les clients sans fil, il vous faut aussi un point d'accès avec des réseaux Wi-Fi associés aux VLAN. Gardez un appareil sur le réseau d'administration actuel pendant la modification de la configuration. Enregistrez d'abord les paramètres du routeur, du commutateur et du point d'accès. Les étapes ci-dessous utilisent un **plan illustratif**. Adaptez les adresses et les ports à votre matériel.

Une **interface VLAN** est la connexion de la passerelle à un VLAN. La passerelle peut être un routeur, un pare-feu ou un commutateur de couche 3. Une **étendue DHCP** est la plage d'adresses qu'un service DHCP propose aux appareils du réseau. Un **relais DHCP** transmet les demandes d'adresse d'un VLAN à un serveur DHCP situé sur un autre réseau. Utilisez un relais si la passerelle ne fournit pas d'adresses à ce VLAN et si le serveur DHCP se trouve ailleurs. Le [guide Juniper du relais DHCP](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) décrit ce chemin. Un **SSID** sans fil est le nom du réseau que les clients rejoignent. Si votre matériel ne comporte ni commutateur administrable ni point d'accès compatible VLAN, commencez par son réseau invité intégré et vérifiez son isolation avant d'acheter ou de remplacer du matériel.

Si vous avez besoin des notions de base, lisez [sous-réseaux et VLAN](/articles/networking-basics-what-are-subnets-and-vlans/). Le [guide de segmentation réseau](/articles/how-to-perform-network-segmentation-for-improved-security/) du site présente le concept de sécurité plus général. CISA décrit des réseaux domestiques séparés pour les visiteurs et les appareils de l'Internet des objets dans ses recommandations [Federal Mobile Workplace Security](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Avertissement :** Modifier le VLAN du port qui transporte votre connexion d'administration risque de vous couper l'accès. Gardez un accès physique et une méthode de récupération connue jusqu'à ce que chaque réseau passe ses tests.

Avant de déplacer un câble, exportez la configuration de chaque appareil et notez l'adresse IP d'administration actuelle, le port du commutateur, le paramètre VLAN et le compte administrateur. Laissez un port d'administration connu et un ordinateur portable sur le réseau d'origine. Si une modification interrompt l'accès, reconnectez l'ordinateur à ce port, restaurez le paramètre ou la configuration enregistrée et vérifiez que l'ancienne passerelle répond avant de réessayer. Si le commutateur n'a aucun chemin d'administration accessible, utilisez sa console ou la procédure de récupération locale documentée. Ne réinitialisez pas le matériel avant de savoir ce que la réinitialisation efface.

## Inventorier les appareils et flux

Listez chaque appareil, son adresse actuelle, son propriétaire et les services dont il a besoin. Donnez à chaque appareil une raison d'accéder à un autre réseau. Un ordinateur portable peut, par exemple, administrer un serveur, tandis qu'une caméra n'a besoin que d'un enregistreur et d'un serveur DNS. Un téléphone invité a besoin d'Internet, mais pas d'accéder aux serveurs.

| Groupe d'appareils | Exemples | Accès requis |
|---|---|---|
| **Administration** | Ordinateur de l'administrateur, interfaces d'administration du commutateur et du point d'accès | Administration du routeur, du commutateur, du point d'accès et des serveurs |
| **Serveurs** | Hyperviseur, NAS, cible de sauvegarde | Mises à jour, DNS, trafic applicatif autorisé |
| **IoT** | Caméras, prises intelligentes, appareils multimédias | DNS, service horaire, contrôleur ou enregistreur précis |
| **Visiteurs** | Téléphones et ordinateurs portables des visiteurs | Internet, DNS, aucun sous-réseau privé |

Notez les exceptions avant d'ajouter des règles. Les fonctions de découverte locale, comme la diffusion vers un écran, dépendent souvent du trafic multicast qui ne traverse pas par défaut une limite routée. N'ouvrez pas tout le trafic entre VLAN pour résoudre un seul problème de découverte. Identifiez le protocole et ajoutez l'exception prise en charge la plus restreinte.

## Attribuer les VLAN et adresses

Attribuez à chaque groupe un identifiant VLAN et un sous-réseau IP distinct. Ce **plan illustratif** utilise des adresses réservées à la documentation et suppose que le routeur fournit DHCP et DNS. Ne copiez pas le tableau dans un réseau actif sans vérifier les conflits d'adresses.

| Réseau | ID VLAN | Sous-réseau | Exemple de passerelle |
|---|---:|---|---|
| **Administration** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Serveurs** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Visiteurs** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Ces plages réservées à la documentation illustrent uniquement l'organisation, conformément à la [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Pour votre lab réel, utilisez des adresses privées de la [RFC 1918](https://www.rfc-editor.org/info/rfc1918), avec un sous-réseau sans chevauchement pour chaque VLAN. Consignez dans votre plan chaque passerelle réelle, pool DHCP, adresse DNS et réservation d'appareil.

Les **ports d'accès** transportent le réseau d'un appareil sans balise VLAN. Les **ports trunk** transportent certains VLAN balisés entre le routeur, le commutateur et le point d'accès. Faites correspondre l'ID VLAN et le paramètre native ou untagged aux deux extrémités. Le [guide des commutateurs VLAN de Netgate](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) explique les trunks balisés, les ports d'accès non balisés et les ID VLAN des ports. Évitez d'utiliser le VLAN 1 par défaut pour l'administration si votre matériel permet un VLAN séparé, comme l'explique le [guide de sécurité VLAN](https://docs.netgate.com/pfsense/en/latest/vlan/security.html) de Netgate.

Le trafic **native** ou **untagged** sur un trunk n'a pas de balise VLAN. Les deux extrémités doivent l'affecter au même VLAN, sinon un appareil risque d'aboutir sur le mauvais réseau. N'autorisez que les VLAN nécessaires sur la liaison. Désactivez les ports inutilisés du commutateur ou affectez-les à un réseau restreint. Netgate déconseille aussi de considérer un VLAN comme une limite de sécurité complète si un attaquant contrôle un port du commutateur. Protégez les ports physiques et les identifiants des appareils, ainsi que le trafic routé.

## Créer une matrice de trafic

Un VLAN sépare à lui seul les domaines de diffusion. Le **routage inter-VLAN** du routeur ou du commutateur de couche 3 nécessite encore des règles d'accès. Déterminez quel appareil achemine le trafic entre les VLAN. Si un commutateur de couche 3 route localement, le trafic entre ses VLAN peut ne jamais atteindre le pare-feu du routeur. Appliquez des listes de contrôle d'accès équivalentes sur le commutateur ou faites passer le trafic par le pare-feu, puis testez au point d'application réel. Vérifiez le sens de l'ACL du commutateur et la prise en charge de l'état des connexions. De nombreuses ACL de commutateur évaluent les paquets séparément dans chaque sens. Une connexion autorisée peut donc nécessiter une règle limitée pour le trafic de retour. Le [guide Cisco des ACL](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) explique le sens des interfaces et l'ordre des correspondances de paquets. Appuyez-vous sur l'inventaire des appareils pour noter les connexions à autoriser. Les entrées suivantes sont des exemples, pas un ensemble de règles universel.

| Source | Destination | Service | Décision |
|---|---|---|---|
| **Administration** | Interface d'administration du serveur | TCP 443 | Autoriser les appareils d'administration approuvés |
| **Administration** | Interfaces d'administration du routeur, commutateur et point d'accès | Ports d'administration documentés | Autoriser les appareils d'administration approuvés |
| **IoT** | Enregistreur des caméras | Port documenté de l'enregistreur | Autoriser uniquement si nécessaire |
| **IoT** | Service DNS et horaire approuvé | DNS et NTP | Autoriser uniquement vers les services choisis |
| **IoT** | Sous-réseau d'administration | Tous | Refuser |
| **Visiteurs** | Sous-réseaux privés | Tous | Refuser |
| **Visiteurs** | DNS et Internet | DNS, trafic Web | Autoriser via le résolveur et la passerelle approuvés |

Incluez les services propres au routeur dans le plan. Une règle qui bloque l'accès IoT aux autres VLAN peut quand même laisser l'interface d'administration du routeur accessible. Réservez les services d'administration au réseau d'administration. Commencez par les seules règles d'autorisation nécessaires et un refus par défaut pour le reste du trafic routé. Vérifiez les règles d'autorisation générales existantes avant de supposer que les valeurs par défaut bloquent tout. Les [bonnes pratiques du pare-feu](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) de Netgate indiquent qu'un LAN pfSense par défaut comprend une règle d'autorisation. Si vous utilisez pfSense, sa [méthodologie des règles](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) précise que les règles d'interface filtrent le trafic entrant sur cette interface et que les connexions autorisées créent un état pour le trafic de retour.

Le tableau d'exemple concerne IPv4. Si votre réseau utilise IPv6, attribuez un préfixe et une politique IPv6 à chaque VLAN, examinez les annonces de routeur et testez aussi les chemins IPv6 autorisés et refusés. Un blocage IPv4 ne prouve pas l'isolation IPv6. Si vous ne comptez pas router IPv6, vérifiez les paramètres IPv6 du routeur et les adresses des clients au lieu de supposer qu'IPv6 est absent. Netgate documente le [fonctionnement du pare-feu IPv6](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) et les [annonces de routeur](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Configurer un réseau à la fois

1. Choisissez la passerelle du VLAN. Si le routeur ou le pare-feu assure le routage, créez-y une interface VLAN et attribuez-lui l'adresse de passerelle. Si le routage revient au commutateur de couche 3, créez l'interface VLAN sur ce commutateur. Configurez une étendue DHCP sur la passerelle ou un relais DHCP vers votre serveur DHCP existant. Vérifiez que le résolveur DNS approuvé est accessible. Le [guide de configuration VLAN de Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) détaille les étapes d'interface et de service pour une passerelle pfSense.
2. Si le routeur est la passerelle VLAN, ajoutez ce VLAN au trunk routeur-commutateur. Si le commutateur de couche 3 est la passerelle, laissez-le gérer l'adresse de passerelle du VLAN et acheminez le trafic vers le routeur ou le pare-feu par un réseau de transit distinct ou une liaison montante routée. Ajoutez au commutateur une route par défaut vers le routeur amont. Ajoutez au routeur une route de retour pour chaque VLAN dont la passerelle est sur le commutateur. Vérifiez la politique du pare-feu du routeur et le NAT sortant de ces sous-réseaux s'ils ont besoin d'Internet. Ne créez pas la même adresse de passerelle ni la même étendue DHCP sur les deux appareils. Ajoutez le VLAN au trunk commutateur-point d'accès concerné si les clients Wi-Fi en ont besoin. Le [guide Cisco du routage inter-VLAN](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) montre des passerelles VLAN portées par un commutateur. Netgate documente les [routes de retour](https://docs.netgate.com/pfsense/en/latest/routing/static.html) et le [NAT sortant](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) pour les réseaux derrière un routeur interne.
3. Attribuez un port d'accès de test ou un SSID sans fil au VLAN. Connectez à ce port ou SSID un appareil de test non critique.
4. Ajoutez les règles de pare-feu ou les ACL du commutateur prévues sur l'appareil qui route le VLAN. Vérifiez que le reste du trafic routé est refusé. Vérifiez le sens de l'ACL et le trafic de retour si le commutateur ne suit pas l'état. Testez l'accès à chaque passerelle, interface d'administration, sous-réseau local et à IPv6 le cas échéant. N'autorisez que les chemins de votre matrice. Réservez l'administration au réseau de gestion. Vérifiez l'ordre des règles et ne supprimez ou réduisez les règles d'autorisation générales existantes qu'après avoir confirmé le fonctionnement du chemin de gestion.
5. Vérifiez que l'appareil de test reçoit une adresse, une passerelle et un serveur DNS du sous-réseau prévu. Effectuez ensuite les tests de connexion ci-dessous avant de déplacer d'autres appareils.

Ne déplacez pas le dernier appareil d'administration avant que son chemin de remplacement fonctionne. Enregistrez la configuration fonctionnelle après la réussite des tests de chaque réseau. Si DHCP, DNS ou l'accès d'administration échoue, replacez l'appareil de test sur le port ou le SSID d'origine, restaurez la dernière modification du commutateur ou du routeur à partir de la configuration enregistrée, puis retestez le réseau d'origine avant de poursuivre.

## Tester l'isolation et l'accès

Utilisez un service que vous contrôlez et dont vous savez qu'il écoute sur la destination. Sur un appareil Windows de test, remplacez l'adresse et le port d'exemple par ceux d'un vrai serveur, puis exécutez :

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

Le champ **`TcpTestSucceeded`** indique si une connexion TCP a abouti. La [référence Microsoft de Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) décrit les paramètres `-ComputerName` et `-Port`. Un échec de connexion ne prouve pas à lui seul qu'une règle de pare-feu a fonctionné. Le service peut être arrêté ou le pare-feu de l'hôte peut rejeter le trafic. Vérifiez le service de destination et le journal du pare-feu réseau avant de conclure.

Testez depuis un appareil réellement connecté à chaque VLAN source. Avant chaque test, notez son adresse source, sa passerelle et son serveur DNS. Vérifiez une connexion autorisée au service prévu, une connexion refusée vers un service interne hors de la matrice, une résolution DNS via le résolveur prévu et l'accès à Internet si celui-ci est prévu. Pour un VLAN dont la passerelle se trouve sur un commutateur, vérifiez la route par défaut du commutateur, la route de retour du routeur et le chemin de retour depuis la destination lorsqu'une connexion autorisée échoue. Si IPv6 est actif, répétez les tests autorisés et refusés avec des adresses IPv6. Dans pfSense, **Status > System Logs > Firewall** affiche les actions autorisées ou bloquées qui ont été journalisées. Le [guide Netgate des journaux de pare-feu](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) décrit cette vue. Comparez la source, la destination, le port et la règle du journal avec votre test. Si le test réussit de façon inattendue, examinez les règles générales et les entrées d'état existantes. Après une modification des règles, ouvrez une nouvelle connexion, car une connexion établie peut continuer grâce à son état existant.

Pour vérifier DNS sous Windows, exécutez `nslookup example.com` et comparez le serveur affiché au résolveur prévu. Essayez ensuite une résolution depuis un client invité ou IoT dont l'accès DNS est limité. Une résolution réussie ne prouve pas que le client a utilisé le résolveur choisi. Vérifiez le serveur signalé et un journal du pare-feu ou du résolveur. Testez séparément l'accès direct à l'adresse d'administration du routeur depuis un appareil IoT ou invité comme cas de refus.

Les appareils du **même VLAN** peuvent échanger du trafic sans passer par le pare-feu du routeur. Testez séparément l'isolation des clients locaux si votre point d'accès la propose et utilisez des pare-feu hôte sur les serveurs. Les tests de pare-feu inter-VLAN ne prouvent pas l'isolation au sein d'un même VLAN.

> **Résultat attendu :** chaque appareil reçoit une adresse de son sous-réseau prévu. Les services autorisés fonctionnent. Les tentatives refusées correspondent à un blocage du pare-feu ou à un contrôle équivalent documenté.

## Dépannage

- **Aucune adresse :** vérifiez le VLAN du port d'accès ou du SSID, les balises du trunk, l'étendue DHCP et l'interface de passerelle.
- **L'adresse fonctionne, mais pas DNS :** vérifiez l'adresse du résolveur, la liaison du service sur le routeur et la règle de pare-feu pour DNS.
- **Un appareil atteint un autre VLAN de façon inattendue :** vérifiez les règles du routeur, les règles générales d'autorisation et si les deux appareils partagent encore un réseau non balisé.
- **Aucune entrée du journal de pare-feu pour le trafic routé :** vérifiez si un commutateur de couche 3 ou une autre passerelle a routé la connexion avant qu'elle n'atteigne le pare-feu.
- **Un VLAN dont la passerelle est sur le commutateur atteint les réseaux locaux, mais pas Internet :** vérifiez la route par défaut du commutateur, les routes de retour du routeur, la politique du pare-feu et le NAT sortant du sous-réseau VLAN.
- **IPv4 est bloqué, mais la connexion fonctionne :** vérifiez les adresses IPv6, les annonces de routeur, les règles IPv6 et les entrées d'état existantes.
- **Un test refusé expire sans entrée dans le journal du pare-feu :** confirmez que le service de destination écoute. Vérifiez ensuite le routage et les paramètres de journalisation. Le [guide Netgate de dépannage du pare-feu](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) décrit les vérifications des journaux et des états.
- **La diffusion ou la découverte ne fonctionne plus :** identifiez le protocole de découverte et le chemin du contrôleur avant d'ajouter une exception ciblée.

## Étapes suivantes

Conservez l'inventaire des appareils et la matrice de trafic avec votre schéma réseau. Révisez les règles lorsque vous ajoutez un serveur ou un appareil IoT. Après chaque modification réseau pertinente, répétez un test de connexion autorisée et un test de connexion refusée. Pour les principes de conception plus généraux, consultez la [segmentation réseau](/articles/how-to-perform-network-segmentation-for-improved-security/).
