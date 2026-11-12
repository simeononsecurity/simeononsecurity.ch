---
title: "Pourquoi le filtrage DNS est contourné : vérifier le chemin du résolveur"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Déterminez pourquoi un appareil ou un navigateur ignore votre filtre DNS. Comparez les requêtes directes et normales, consultez les journaux, puis vérifiez le DNS chiffré, le VPN, IPv6 et le routeur."
genre: ["Réseaux domestiques", "DNS", "Confidentialité"]
tags: ["contournement du filtrage DNS", "contourner Pi-hole", "journal des requêtes DNS", "DNS sécurisé du navigateur", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "DNS du VPN", "DNS IPv6", "DNS DHCP du routeur", "Resolve-DnsName", "dépannage DNS", "test du filtre DNS", "dépannage NextDNS", "dépannage AdGuard DNS"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "Le chemin DNS bleu d’un ordinateur portable traverse un filtre et s’arrête à un symbole de blocage, tandis que le chemin orange du navigateur atteint un autre résolveur."
coverCaption: "Suivez le chemin de la requête avant de modifier la règle du filtre."
---

Vous avez configuré un résolveur filtrant, mais un appareil atteint toujours un domaine que votre politique bloque. La cause peut être la règle, l’attribution du Domain Name System (DNS) à l’appareil, un résolveur chiffré du navigateur ou un VPN. **Testez le chemin avant de modifier les paramètres.** Une requête directe vers le filtre répond à une autre question qu’une requête normale de l’appareil.

<!--more-->

## Points clés

- **Vérifiez d’abord la règle :** Confirmez que le filtre reçoit et bloque un domaine de test sans danger.
- **Suivez chaque couche :** Le routeur, le système d’exploitation, le navigateur, le VPN et les paramètres mobiles influencent tous le routage DNS.
- **Utilisez des requêtes nouvelles :** Faites correspondre un nouveau nom d’hôte et son heure au journal des requêtes du filtre.
- **Indiquez la limite :** Une requête observée prouve un chemin, pas le comportement de chaque application ou appareil.

## Avant de commencer

Prévoyez environ 20 minutes. Vous avez besoin d’accéder au journal des requêtes du résolveur filtrant, d’un appareil concerné et d’un relevé des paramètres DNS du routeur. Les exemples utilisent un ordinateur portable Windows et **Pi-hole**, mais la même comparaison fonctionne avec tout résolveur qui fournit des journaux par client. Identifiez d’abord l’adresse exacte du filtre. Ne publiez pas d’adresses privées de clients, de journaux de requêtes ou de règles dans un rapport public.

Choisissez un **domaine de test inoffensif** déjà bloqué par votre politique. Vous pouvez aussi ajouter temporairement une règle de refus exacte pour un domaine que vous contrôlez dans un profil de test. Notez la règle et supprimez-la après le test. N’utilisez pas un domaine malveillant actif comme sonde. Une page bloquée donne un indice, mais le journal du résolveur fournit une preuve plus solide du chemin.

| Couche | Question |
|---|---|
| **Filtre** | Une requête directe atteint-elle le résolveur prévu et correspond-elle à la règle ? |
| **Appareil** | Quels serveurs DNS le réseau attribue-t-il ? |
| **Navigateur ou application** | Ce client utilise-t-il le résolveur de l’appareil ou un chemin distinct ? |
| **VPN ou relais** | Un tunnel actif change-t-il la destination des requêtes ? |

## Prouver que le filtre fonctionne

Ouvrez le journal des requêtes du résolveur. Interrogez directement le filtre pour le domaine bloqué choisi. Sous Windows, utilisez PowerShell et saisissez l’adresse du filtre et le domaine de test lorsque le programme les demande :

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

La [référence Microsoft de **`Resolve-DnsName`**](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) décrit **`-Server`** comme une requête adressée au résolveur indiqué. Recherchez la requête dans le journal du filtre et vérifiez la réponse et la règle correspondante. La [documentation Pi-hole sur les requêtes et journaux](https://docs.pi-hole.net/main/pihole-command/) décrit ses outils locaux. Si la requête directe est autorisée, corrigez la règle ou l’affectation du groupe client avant d’enquêter sur un contournement. Si elle n’atteint pas le filtre, vérifiez l’adresse, le service et le chemin réseau.

**Ce test direct ne prouve pas que l’ordinateur portable utilise normalement le filtre.** L’option **`-Server`** remplace le résolveur par défaut pour cette requête. Cette distinction évite un faux résultat positif courant.

## Suivre le chemin de l’appareil

Utilisez un nouveau nom d’hôte pour éviter une entrée DNS mise en cache. L’exemple suivant envoie une requête directement au filtre et une autre selon la sélection normale du résolveur de l’ordinateur portable. Les noms sont différents afin de reconnaître chaque entrée de journal. Une réponse **NXDOMAIN** signifie que le serveur DNS indique que le nom d’hôte n’existe pas. C’est normal si le nom aléatoire n’est pas utilisé. Ici, c’est la présence de la requête dans le journal du filtre qui compte.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Recherchez les deux noms exacts dans le journal du filtre et notez l’heure et le client indiqué. Si **`direct-`** apparaît mais pas **`default-`**, examinez les serveurs DNS attribués à l’ordinateur portable. Sous Windows, **`Get-DnsClientServerAddress`** affiche les adresses des serveurs DNS par interface. Vérifiez l’adaptateur Wi-Fi ou Ethernet actif, et non un adaptateur déconnecté. La [référence du client DNS de Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) décrit cette commande en lecture seule.

Laissez les erreurs visibles pendant le premier test. Une erreur ou un délai d’attente nécessite un diagnostic distinct et ne signifie pas la même chose qu’une entrée absente du journal.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Comparez les lignes IPv4 et IPv6. **DHCP** attribue des paramètres réseau tels que les serveurs DNS. **IPv6** est la famille d’adresses Internet Protocol la plus récente et utilise des adresses de 128 bits. Un bail IPv4 peut désigner le filtre, tandis que les annonces IPv6 du routeur fournissent un autre serveur DNS. Vérifiez les annonces **DHCP** et **DNS IPv6** du routeur, puis renouvelez le bail réseau de l’appareil après une correction. Le [guide Pi-hole après installation](https://docs.pi-hole.net/main/post-install/) explique comment DHCP dirige les clients vers Pi-hole. Son [exemple de routeur](https://docs.pi-hole.net/routers/fritzbox/) traite des annonces DNS IPv6.

Si le journal indique le **routeur** comme client, celui-ci transmet peut-être les requêtes pour le compte des appareils. Le journal prouve alors que le routeur a atteint le filtre, mais pas quel appareil a lancé la requête. Vérifiez la conception du transfert du routeur avant de considérer l’identité du client comme une donnée manquante.

## Vérifier le DNS du navigateur

Une requête en ligne de commande teste le chemin du résolveur de l’appareil. Un navigateur peut plutôt utiliser le **DNS over HTTPS (DoH)**. Ouvrez le même domaine de test bloqué dans le navigateur et recherchez une requête correspondante dans le journal du filtre. Videz le cache DNS du navigateur ou utilisez un nouveau nom d’hôte couvert par une règle de test si des résultats en cache faussent la comparaison.

Dans **Chrome sur ordinateur**, ouvrez **Paramètres > Confidentialité et sécurité > Sécurité > Utiliser un DNS sécurisé**. L’[aide Google Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) indique que le mode automatique utilise le fournisseur actuel et revient à une recherche non chiffrée en cas d’échec. Un fournisseur personnalisé sélectionné n’effectue pas le même repli. Notez le mode et le fournisseur avant toute modification.

Dans **Firefox**, ouvrez **Paramètres > Vie privée et sécurité > DNS via HTTPS**. Le [guide Mozilla des niveaux de protection](https://support.mozilla.org/en-US/kb/dns-over-https) distingue les modes Par défaut, Renforcé, Maximal, Personnalisé et Désactivé. La [présentation de DoH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) explique quand un résolveur de navigateur contourne un filtre DNS local. Recommencez après une seule modification contrôlée, puis restaurez le paramètre de confidentialité souhaité.

**Ne qualifiez pas automatiquement chaque requête absente du navigateur de contournement.** Le navigateur peut réutiliser des données en cache, joindre une adresse déjà connue ou utiliser un proxy. Comparez un nouveau nom, une plage horaire correspondante et le paramètre de résolveur du navigateur avant de conclure sur la destination de la requête.

## Vérifier les chemins mobiles et VPN

Sous **Android**, examinez **Paramètres > Réseau et Internet > DNS privé**. Le nom d’hôte d’un fournisseur sélectionne un service DNS privé distinct du DNS annoncé par le routeur. Les [paramètres réseau Android de Google](https://support.google.com/android/answer/9654714?hl=en) décrivent les choix Désactivé, Automatique et Nom d’hôte du fournisseur. Pour obtenir un résultat local contrôlé, testez en Wi-Fi avec les données mobiles désactivées, puis restaurez votre réglage habituel.

Sur les **appareils Apple**, vérifiez si **iCloud Private Relay** est actif pour le réseau et si Safari utilise le chemin attendu. Apple indique que [Private Relay protège la navigation Safari et les informations DNS](https://support.apple.com/en-gb/102602). Ses [commandes réseau](https://support.apple.com/en-ie/102022) décrivent le traitement par réseau lorsqu’un filtre entre en conflit avec Private Relay. Ne généralisez pas un résultat Safari à toutes les applications de l’appareil.

Un **VPN** peut fournir son propre résolveur DNS ou envoyer les requêtes dans le tunnel. Notez si le VPN est connecté, ses paramètres DNS et sa politique de tunnel fractionné. Comparez le même test avec le VPN activé et désactivé uniquement si votre politique de sécurité l’autorise. Un résultat différent révèle une différence de chemin. À lui seul, il ne prouve ni fuite ni défaut du filtre.

## Interpréter les résultats

| Observation | Vérification suivante probable |
|---|---|
| **Requête directe absente du journal du filtre** | Adresse du filtre, service DNS, journalisation ou accessibilité réseau |
| **Requête directe autorisée** | Règle de refus exacte, stratégie de groupe ou priorité des règles |
| **Requête directe journalisée, requête normale absente** | DHCP, DNS statique de l’appareil, DNS IPv6 ou résolveur VPN |
| **Requête normale journalisée, requête du navigateur absente** | DoH du navigateur, cache, proxy ou relais |
| **Les deux requêtes sont journalisées et bloquées, mais le site s’ouvre** | Autre nom d’hôte, contenu en cache, adresse directe ou chemin de l’application |

**L’absence d’entrées est ambiguë** si la journalisation est désactivée, si le routeur transmet pour le client ou si le test réutilise des données en cache. Recommencez avec un nouveau nom d’hôte et vérifiez l’heure de la requête avant de modifier le pare-feu. Bloquer le DNS classique vers des résolveurs externes n’oblige pas un navigateur chiffré ou un VPN à utiliser votre filtre. Le [guide Pi-hole pour OPNsense](https://docs.pi-hole.net/routers/opnsense/) présente le blocage du DNS externe comme un contrôle réseau facultatif. Les règles de l’appareil et la configuration du navigateur restent des contrôles distincts.

## Corriger et retester

Modifiez une seule couche à la fois. Corrigez les annonces DHCP ou DNS IPv6, retirez un résolveur statique involontaire, sélectionnez le fournisseur DNS souhaité dans le navigateur ou adaptez la politique DNS du VPN. N’affaiblissez pas en silence le DNS chiffré ou la protection du relais sur tous les appareils pour résoudre un seul échec. Notez l’appareil source, l’interface, l’adresse du filtre, le nom interrogé, l’heure, la réponse, le client indiqué dans le journal, le mode du navigateur, l’état du VPN et la modification effectuée.

Après chaque modification, répétez les tests **direct**, **normal** et **navigateur**. Utilisez un nouveau nom d’hôte à chaque essai. Si un appareil dispose de plusieurs profils réseau, testez-les séparément. La [comparaison des résolveurs DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) aide à choisir un service. Le [test de fuite du navigateur](/articles/privacy-browser-leak-test-dns-webrtc/) répond à une autre question : quelles informations réseau quittent votre configuration de navigateur et de VPN ? **Un résultat fiable exige une règle vérifiée et un chemin client vérifié.**

## Étapes suivantes

Répétez les tests direct, normal et navigateur après chaque modification contrôlée. Consultez la [comparaison des résolveurs DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) pour choisir un service de filtrage.
