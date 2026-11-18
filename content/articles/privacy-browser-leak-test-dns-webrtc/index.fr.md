---
title: "Tester les fuites DNS et WebRTC du navigateur avec un VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Vérifiez l’adresse IP publique, le résolveur DNS et les adresses WebRTC de votre navigateur avant et après la connexion au VPN. Interprétez les résultats et isolez les problèmes de routage."
genre: ["Confidentialité", "Navigateurs", "Réseaux"]
tags: ["test de fuite DNS", "test de fuite WebRTC", "test de fuite VPN", "test de confidentialité du navigateur", "fuite d’adresse IP", "DNS over HTTPS", "DNS sécurisé", "DNS de Firefox", "DNS sécurisé de Chrome", "candidats WebRTC", "tunnel VPN fractionné", "fuite IPv6", "test de résolveur", "confidentialité du navigateur", "confidentialité réseau", "dépannage VPN", "résolveur DNS", "candidats ICE", "adresse IP privée", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Une fenêtre de navigateur avec trois panneaux pour l’adresse IP publique, le DNS et les connexions pair à pair, ainsi qu’un tunnel plein et un chemin alternatif pointillé vers des serveurs distants."
coverCaption: "Comparez chaque chemin réseau avant et après la connexion au VPN."
---

L’icône de connexion à un **réseau privé virtuel (VPN)** ne prouve pas que toutes les requêtes du navigateur suivent le même chemin. Testez séparément votre **adresse IP publique**, votre **résolveur du Domain Name System (DNS)** et vos **adresses WebRTC**. Chaque résultat répond à une question différente. Ce guide propose une vérification reproductible et une méthode pour examiner un résultat inattendu.

<!--more-->

## Points clés

- **Comparez deux états :** Notez les mêmes résultats avant et après la connexion au VPN.
- **Lisez chaque résultat séparément :** Une adresse IP publique modifiée ne révèle pas où les requêtes DNS ont été envoyées.
- **Vérifiez les candidats WebRTC :** Repérez une adresse publique qui emprunte un chemin autre que celui prévu. Une adresse privée a une autre signification.
- **Modifiez un seul paramètre :** Recommencez le test après chaque réglage du VPN, du navigateur ou du DNS.

## Avant de commencer

Utilisez le navigateur et la connexion réseau que vous souhaitez protéger. Déterminez si le VPN doit couvrir tout l’appareil ou seulement certaines applications. Si votre VPN utilise un tunnel fractionné, notez si le navigateur testé passe par le tunnel. Gardez à portée de main la politique DNS du client VPN pour la comparaison.

Le **tunnel fractionné** fait passer certaines applications par le VPN, tandis que les autres utilisent le réseau normal.

Cette procédure utilise les pages [IP BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) et [WebRTC](https://browserleaks.com/webrtc). Le service voit votre adresse de connexion lorsque vous le consultez. Selon la description du test, son test DNS demande au navigateur de résoudre 50 noms aléatoires. Évitez tout test externe sur un réseau géré ou restreint sans autorisation. Ne saisissez pas d’identifiants, de noms d’hôtes internes ni d’historique de navigation privé sur un site de test.

> **Avertissement :** N’incluez pas vos adresses IP exactes dans des captures d’écran publiques ou des messages d’assistance. Notez si les adresses correspondent au chemin attendu par votre FAI ou votre VPN. Ne communiquez les valeurs réelles que par un canal d’assistance approuvé.

## Ce que montre chaque test

| Vérification | Élément à comparer | Ce que le résultat ne prouve pas |
|---|---|---|
| **IP publique** | Adresse vue par un site Web ordinaire | Quel résolveur a traité le DNS |
| **Résolveur DNS** | Serveurs observés lors de nouvelles recherches de noms | Où chaque application envoie ses requêtes DNS |
| **WebRTC** | Candidats de connexion locaux et publics | Quel candidat utilisera un appel ultérieur |

La page IP publique indique l’adresse utilisée pour sa requête Web. La page DNS déclenche de nouvelles recherches et indique les résolveurs qui les traitent. WebRTC, abréviation de Web Real-Time Communication, permet aux applications de navigateur d’établir des connexions pair à pair. La page WebRTC vérifie les adresses exposées pendant ces connexions. Un **candidat ICE** est une adresse réseau possible pour une connexion pair à pair. Une **sortie VPN** est l’adresse publique utilisée lorsque le trafic quitte le VPN. La [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) explique pourquoi les candidats WebRTC contiennent parfois des adresses autres que celle vue lors d’une requête Web ordinaire, notamment avec les tunnels fractionnés ou les proxys.

Un serveur DNS appartenant à votre fournisseur VPN, un résolveur distinct choisi dans le VPN ou un résolveur chiffré choisi dans le navigateur affichent des noms différents lors d’un test. Le nom d’un résolveur ne suffit pas à établir une fuite. Comparez-le à la politique que vous vouliez appliquer.

## Relever un état de référence

Déconnectez le VPN uniquement si votre situation permet un état de référence sans tunnel. Ouvrez les trois pages de test dans un profil de navigateur normal. Lancez le test DNS et attendez son résultat. Notez les éléments suivants sans publier d’adresses exactes :

| Champ | Note de référence |
|---|---|
| **Navigateur et version** | Nom, version et extensions de confidentialité utiles |
| **Réseau** | Wi-Fi domestique, point d’accès mobile ou autre réseau autorisé |
| **IPv4 et IPv6 publiques** | Indiquez si chacune appartient à votre connexion habituelle |
| **Résultat DNS** | Noms ou opérateurs des résolveurs affichés |
| **Résultat WebRTC** | Candidats publics, privés ou `.local` affichés |

Si vous ne pouvez pas déconnecter le VPN, commencez par le chemin VPN attendu et indiquez que l’état de référence sans tunnel n’est pas disponible. Ne déduisez pas l’adresse de votre FAI habituel d’une étiquette de localisation ou d’une carte. Les bases de données de localisation peuvent différer de l’opérateur réseau réel.

## Refaire le test avec le VPN

Connectez le VPN et vérifiez que le client indique que le tunnel fonctionne. Rechargez chaque page de test dans le **même profil de navigateur**. Relancez le test DNS pour générer de nouvelles recherches. Notez les résultats IPv4 et IPv6 lorsque le service les affiche.

Comparez les résultats dans cet ordre :

1. **IP publique :** La requête Web devrait afficher une adresse cohérente avec la sortie VPN ou le chemin que vous avez configuré volontairement. Si le navigateur devrait être dans le tunnel, une adresse FAI habituelle inchangée indique un problème de routage.
2. **DNS :** Comparez chaque résolveur affiché aux paramètres DNS du VPN et du navigateur. Un résolveur du FAI hors du tunnel prévu mérite une vérification. Un résolveur tiers nommé est attendu si vous l’avez choisi dans le navigateur.
3. **WebRTC :** Comparez le candidat WebRTC public à la sortie VPN et à l’IP publique de référence. L’apparition de l’IP publique du FAI dans WebRTC seulement pose problème si tout le trafic du navigateur devrait utiliser le VPN.
4. **Adresses privées :** Une adresse dans les [plages privées de la RFC 1918](https://www.rfc-editor.org/rfc/rfc1918), ou un candidat `.local`, diffère d’une adresse publique du FAI. Notez l’entrée locale et déterminez si le site devrait connaître cette adresse.

La [norme de gestion des adresses WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) décrit comment une application découvre d’autres adresses publiques ou privées au moyen des candidats ICE. La [conception des candidats hôtes mDNS de Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) remplace certaines adresses privées par des noms `.local`. Un résultat WebRTC vide est **non concluant** si JavaScript, l’API ou le serveur de test n’a pas fonctionné. Un résultat vide ne prouve pas une protection complète.

> **Résultat attendu :** La requête Web ordinaire du navigateur et les candidats WebRTC publics suivent le chemin choisi. Les résultats DNS correspondent à la politique du résolveur VPN ou du navigateur que vous avez notée.

## Examiner un écart DNS

Vérifiez d’abord si le navigateur choisit son propre résolveur. Les [paramètres DNS over HTTPS de Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) affichent l’état actif et le niveau de protection. La protection par défaut revient au résolveur système dans certaines conditions et tient compte des signaux réseau. Les niveaux Renforcé et Personnalisé utilisent un fournisseur choisi avec un mécanisme de secours. Le niveau Maximal avertit lorsque la résolution sécurisée échoue. L’état et la liste d’exceptions comptent davantage qu’un simple bouton.

Le [guide Secure DNS de Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) décrit le mode automatique et le fournisseur personnalisé. Le mode automatique revient à une recherche non chiffrée si la recherche sécurisée échoue. Un fournisseur personnalisé ne revient pas par défaut au mode non chiffré. Les appareils gérés et le contrôle parental peuvent limiter ce paramètre. Consultez l’interface actuelle du navigateur avant de modifier une politique gérée.

Si le résolveur du navigateur n’est pas en cause, comparez le paramètre DNS du client VPN, la liste des applications du tunnel fractionné, le résolveur du système d’exploitation et le chemin IPv6. Modifiez un seul élément, puis relancez le test DNS. Un test DNS de navigateur mesure le chemin de recherche du navigateur testé. Il ne montre pas comment une autre application résout les noms. Si votre réseau utilise le [filtrage DNS](/articles/nextdns-vs-adguard-ad-blocker-comparison/), testez un domaine que vous bloquez volontairement et un autre que vous autorisez. Une publicité absente ne prouve pas le chemin du résolveur.

## Examiner un écart WebRTC

Vérifiez si le navigateur est exclu du tunnel VPN ou utilise un proxy hors du chemin prévu. Recommencez le test après avoir corrigé le chemin. Ne désactivez pas IPv6 ou WebRTC pour répondre d’emblée à un seul résultat ambigu. La [norme WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) décrit le compromis entre l’exposition des adresses et les performances des appels directs. Restreindre les candidats ou imposer un proxy affecte les appels vidéo et d’autres connexions pair à pair.

Si votre navigateur ou votre VPN propose un réglage documenté de gestion des adresses WebRTC, lisez sa description actuelle et choisissez une politique adaptée à votre usage des appels. Vérifiez à nouveau le candidat public. Une adresse locale ne prouve pas à elle seule que l’adresse publique de votre FAI a quitté le VPN. Une adresse publique de votre FAI exposée, comparée à une adresse HTTP différente du VPN, constitue un signal plus fort.

## Garder une fiche de test

| Champ | Résultat à noter |
|---|---|
| **Date et navigateur** | Version, profil, extensions et réseau |
| **Chemin attendu** | VPN sur tout l’appareil, tunnel fractionné ou proxy du navigateur |
| **Avant et après** | Opérateur IP publique, opérateur DNS, candidat WebRTC public |
| **Écart** | Résultat contraire à la politique prévue |
| **Modification unique** | Paramètre modifié et raison |
| **Nouveau test** | Nouveau résultat et incertitude restante |

Refaites la vérification après une modification de la configuration du navigateur, du VPN ou du réseau. Un résultat satisfaisant concerne le navigateur, le profil, le réseau et le moment testés. Il ne prouve pas l’anonymat et ne couvre pas toutes les applications. Si vous choisissez encore un navigateur, consultez le [comparatif des navigateurs respectueux de la vie privée](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) pour comparer leurs fonctions, puis testez votre propre configuration.

## Étapes suivantes

Répétez le test après toute modification du navigateur, du VPN ou du réseau. Consultez le [comparatif des navigateurs respectueux de la vie privée](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) pour choisir un navigateur.
