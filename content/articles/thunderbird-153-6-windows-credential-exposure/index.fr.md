---
title: "Thunderbird 153.6 : exposition des identifiants NTLM sous Windows et mise à jour (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Deux failles graves de Thunderbird exposent des données d’authentification NTLM sous Windows lorsqu’un courriel piégé est affiché. Découvrez les deux voies, vérifiez votre version et limitez le SMB sortant pendant la mise à jour."
genre: ["Cybersécurité", "Sécurité des e-mails", "Sécurité Windows"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "mise à jour de sécurité Thunderbird", "vulnérabilité Thunderbird sous Windows", "fuite NTLM Thunderbird", "authentification SMB Thunderbird", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "pièce jointe de clé OpenPGP", "pièce jointe externe", "blocage du contenu distant", "URL mailbox", "chemin UNC étendu", "nom du compte Windows", "données d’authentification NTLM", "exposition d’identifiants SMB", "SMB sortant", "port TCP 445", "sécurité des e-mails", "client de messagerie Windows", "vérifier la version de Thunderbird", "mettre à jour Thunderbird", "relais NTLM", "craquage de mot de passe hors ligne"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla a corrigé deux **failles graves exposant des identifiants Windows** dans Thunderbird 153.6. L’affichage d’un courriel malveillant suffisait à déclencher l’une des requêtes réseau décrites dans [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). L’avis décrit une divulgation possible de données NTLM, pas une compromission avérée des identifiants de chaque destinataire.

<!--more-->

## À retenir

- **CVE-2026-118174** concernait une pièce jointe de clé OpenPGP hébergée à l’extérieur. L’affichage du message déclenchait une requête sans action de l’utilisateur, même lorsque le contenu distant était bloqué.
- **CVE-2026-118176** concernait une URL `mailbox:` spécialement formée avec un chemin UNC étendu. L’affichage du message établissait une connexion SMB vers un serveur choisi par l’expéditeur.
- **Mettez Thunderbird à jour sous Windows** et vérifiez la version installée. L’avis indique Thunderbird 153.6 comme version corrigée. Les notes de Thunderbird désignent la compilation 153.6.0esr correspondante.

## Ce que déclenche le courriel

**Les deux failles ont des points d’entrée différents.** D’après les descriptions de Mozilla, aucune ne nécessite que le destinataire clique sur un lien du courriel. Le risque pour les identifiants Windows dépend de l’arrivée d’une requête réseau sur un partage contrôlé par l’attaquant et de l’échange d’authentification qui s’ensuit. Mozilla ne signale pas d’exploitation active dans l’avis.

| Problème | Déclenchement à l’affichage du courriel | Risque pour les identifiants Windows |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird charge le contenu d’une pièce jointe de clé OpenPGP pour proposer l’importation de la clé. L’expéditeur la marque comme pièce jointe externe avec une URL choisie par l’attaquant. | Une URL de partage réseau expose les identifiants NTLM de l’utilisateur si la requête atteint le partage. |
| **CVE-2026-118176** | Un chemin UNC étendu contourne la restriction de Thunderbird sur les partages distants dans les URL `mailbox:`. | Thunderbird se connecte à un serveur SMB choisi par l’attaquant et divulgue le nom du compte Windows et des données d’authentification NTLM. |

Pour la voie de la **pièce jointe OpenPGP**, Mozilla précise que la requête contournait le blocage du contenu distant et ne nécessitait aucune action de l’utilisateur. Sur les systèmes autres que Windows, le problème permettait aussi une requête distante contraire au paramètre de contenu distant, mais Mozilla limite la fuite d’identifiants NTLM à Windows. Pour la voie de l’**URL `mailbox:`**, Mozilla indique que les autres systèmes d’exploitation ne sont pas concernés. Consultez les entrées [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) et [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**Les données d’authentification NTLM ne sont pas un mot de passe en clair.** Mozilla indique que les données divulguées par la voie SMB créent un risque de craquage de mots de passe hors ligne ou d’attaques par relais. La réception d’un message piégé ne prouve pas qu’une attaque a réussi. L’avis répertorie aussi d’autres failles de Thunderbird, dont des voies distinctes concernant l’agenda et RSS. Cet article traite les deux voies déclenchées par l’affichage d’un courriel, sans assimiler tous les problèmes de la version.

## Vérifier et mettre à jour Thunderbird

Le scénario concerné est **la lecture de courriels dans Thunderbird sous Windows** avant l’installation du correctif correspondant. L’avis de Mozilla désigne **Thunderbird 153.6** comme version corrigée, sans préciser la plage complète des versions antérieures concernées par ces deux problèmes. Les [notes de version 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) indiquent une version ESR publiée le 27 octobre 2026. Ne déduisez pas l’état du correctif d’un autre canal, fork ou paquet à partir du seul numéro de version.

1. Sous Windows, ouvrez **Help > About Thunderbird**. Lisez la version affichée dans la fenêtre About, qui recherche aussi les mises à jour. Les [instructions de mise à jour de Mozilla](https://support.mozilla.org/en-US/kb/updating-thunderbird) décrivent cette étape.
2. Si une mise à jour est disponible, laissez Thunderbird la télécharger, puis choisissez **Restart Thunderbird to Update**. Rouvrez **Help > About Thunderbird** et vérifiez la version installée après le redémarrage.
3. Pour la **branche 153 ESR**, comparez la version obtenue à **153.6.0esr** dans les notes de Thunderbird. Si votre organisation gère les mises à jour, demandez à l’administrateur de vérifier le correctif du fournisseur au lieu de supposer qu’il est déjà installé.

> **Précision sur la version :** les notes de 153.6.0esr confirment l’existence de cette version, tandis que MFSA 2026-122 associe les correctifs de sécurité à Thunderbird 153.6. Les notes ne décrivent pas séparément ces deux CVE. Consultez l’avis pour les détails des failles.

## Réduire l’exposition pendant la mise à jour

**Installez d’abord le correctif du fournisseur.** Désactiver le contenu distant ne suffit pas à arrêter CVE-2026-118174, car la requête décrite contournait ce paramètre. Le conseil « ne cliquez pas » ne suffit pas. Mozilla décrit des requêtes déclenchées par l’affichage du message.

En **défense en profondeur**, limitez le SMB sortant des postes Windows vers Internet, y compris le **port TCP 445**, sur le pare-feu de l’entreprise ou sur les appareils gérés. Les [recommandations de Microsoft sur le trafic SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) préconisent de bloquer le TCP 445 sortant vers Internet et de limiter l’accès aux serveurs de fichiers nécessaires. Recensez les partages requis avant d’appliquer une règle, surtout si votre environnement utilise un service de fichiers cloud ou des employés distants hors du périmètre. Ce contrôle réseau limite la voie SMB décrite, mais ne répare pas Thunderbird et ne règle pas tous les problèmes de requêtes distantes de l’avis.

Si un ordinateur Windows exécutant une ancienne version de Thunderbird a affiché un message suspect, **traitez l’exposition comme une question à examiner, pas comme une preuve de compromission**. Examinez avec l’équipe de sécurité les journaux disponibles de connexions SMB sortantes et d’authentification. L’avis du fournisseur ne fournit ni test d’exposition ni consigne générale de modifier tous les mots de passe.

## Sources

- [Mozilla Foundation Security Advisory 2026-122 : vulnérabilités corrigées dans Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Notes de version de Thunderbird Desktop : 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Assistance Mozilla : mettre Thunderbird à jour](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn : sécuriser le trafic SMB dans Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
