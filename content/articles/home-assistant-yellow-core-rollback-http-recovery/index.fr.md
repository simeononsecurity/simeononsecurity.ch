---
title: 'Retour de Home Assistant Core 2026.11 à 2026.10.4 : corriger la version 3 du stockage HTTP'
date: 2026-11-15
lastmod: 2026-11-27
toc: true
draft: false
description: Corrigez l'erreur de version 3 du stockage HTTP après le retour de Home Assistant Core 2026.11 à 2026.10.4 sur
  Yellow. Comprend des commandes protégées et des résultats vérifiés.
genre:
- Domotique
- Dépannage
tags:
- Home Assistant Yellow
- Home Assistant OS
- Retour de Core 2026.11
- Core 2026.10.4
- Version 3 du stockage HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Illustration d'une carte informatique jaune, d'un lien de configuration rompu et d'un tableau de bord web rétabli
coverCaption: ''
---

Une mise à jour échouée de Home Assistant Core 2026.11 a ramené mon Yellow CM4 à la version 2026.10.4. Yellow restait accessible sur le réseau, mais ne servait plus le tableau de bord. Le retour en arrière a laissé un fichier de paramètres HTTP en version de stockage 3.1, alors que Core 2026.10.4 prend en charge la version 2.2. J'ai conservé le fichier, converti une copie avec des contrôles stricts, rétabli l'accès HTTP, puis mis Core à jour vers 2026.11.1.

<!--more-->

## Points essentiels

- **Confirmez l'incompatibilité.** Comparez l'erreur du journal Core avec la version installée et la version du stockage HTTP.
- **Conservez le fichier.** Gardez une copie intacte et une sauvegarde hors appareil avant la récupération.
- **Vérifiez le résultat.** Contrôlez l'état de Core, le point d'écoute enregistré, le tableau de bord et la version installée.

**Correctif pour ce cas précis :** [Conservez le fichier HTTP](#preserve-recovery-options), [créez et validez un candidat en version 2.2](#apply-the-tested-fix-for-version-31), [installez-le après l'arrêt de Core](#apply-the-tested-fix-for-version-31), puis [vérifiez le résultat de la mise à jour](#verify-the-update-outcome). La conversion vérifie les champs d'origine et s'arrête s'ils diffèrent. Ne l'appliquez pas à un fichier HTTP non inspecté.

## Avant de commencer

Vous avez besoin d'un accès physique à un Yellow CM4, d'un câble de données USB-C, d'une console série fonctionnelle et d'une sauvegarde exploitable ou d'une configuration conservée. La procédure manuelle exige un accès au shell de l'hôte et un examen attentif du JSON. Prévoyez au moins 30 minutes pour le diagnostic et la réparation. Le démarrage de Core et la restauration d'une sauvegarde prennent plus de temps sur les grandes installations.

## Reconnaître la panne

L'erreur déterminante apparaissait dans le journal Core :

```text
Storage file http has version 3 which is newer than the max supported version 2
```

L'ancienne version de Core ne pouvait pas charger `http`. L'interface et les autres composants dépendant de HTTP étaient également en panne. Un bail du routeur et une page Observer fonctionnelle ne prouvaient pas que le tableau de bord était accessible. [Le problème Home Assistant Core no 190583](https://github.com/home-assistant/core/issues/190583) documente la même panne après retour arrière sur plusieurs installations, dont Yellow. [Mon commentaire sur ce problème](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) consigne la récupération testée sur ce Yellow et l'état final de Core.

**Cause de la panne web :** Core 2026.11 a écrit `.storage/http` au format 3.1. Le retour arrière a rétabli Core 2026.10.4 sans restaurer un fichier HTTP compatible. Core 2026.10.4 refuse la version de stockage 3. Le profil `intermediate_v6` enregistré sur ce Yellow ne correspond pas non plus à l'ancien schéma. La cause de l'échec de la première mise à jour et du retour arrière est inconnue. Au 2026-11-15, le problème lié était ouvert et la discussion ne contenait aucun correctif confirmé par les mainteneurs.

Vérifiez la version installée de Core et le stockage HTTP avant de modifier des fichiers :

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

La sortie suivante correspond à ce cas, après suppression des horodatages et des détails privés :

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

Les commandes de récupération ci-dessous comparent le point d'écoute enregistré par Supervisor au fichier HTTP sans afficher aucune des deux valeurs. En cas de différence, vérifiez le point d'écoute réel de Core avant de modifier les fichiers.

| Indice | Signification |
| --- | --- |
| Core prend en charge la version de stockage 2, le fichier indique la version 3 | L'ancienne version ne peut pas charger les paramètres HTTP enregistrés |
| Le fichier HTTP et la liste Supervisor indiquent des points d'écoute différents | Vérifiez le point d'écoute réel de Core avant d'attribuer la panne |
| La page d'accueil répond, mais Core reste à l'état STARTING | La réponse de l'interface ne prouve pas la fin du démarrage |

## Conservez les moyens de récupération {#preserve-recovery-options}

Conservez une sauvegarde exploitable hors de Yellow avant toute nouvelle mise à jour. [Le guide de sauvegarde de Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) décrit les emplacements cloud et hors appareil. Une sauvegarde chiffrée nécessite sa clé de récupération. N'effacez pas le disque de données NVMe pendant le diagnostic de cette incompatibilité de stockage.

Copiez le fichier HTTP avant de le modifier :

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Arrêtez-vous si la commande échoue. Ne modifiez pas une ancienne copie de récupération portant le même nom. Choisissez un nouveau nom et répétez la vérification avant de poursuivre.

Si le tableau de bord est inaccessible, utilisez la console série de Yellow. [Le guide Nabu Casa pour Linux et macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) montre le branchement USB-C et l'emplacement de l'UART JP1. Suivez les instructions CM4 adaptées à votre matériel.

## Appliquer le correctif éprouvé pour le format 3.1 {#apply-the-tested-fix-for-version-31}

La meilleure option consiste à utiliser un fichier HTTP compatible antérieur à la mise à jour. Restaurez la sauvegarde selon la procédure documentée de Home Assistant lorsqu'une restauration complète est appropriée. Si vous extrayez un seul fichier, confirmez sa version de stockage et son point d'écoute enregistré avant de remplacer le fichier actif. Les commandes suivantes constituent le correctif direct testé sur ce Yellow en l'absence de fichier HTTP compatible.

[La solution de contournement initiale du problème](https://github.com/home-assistant/core/issues/190583) déplace `.storage/http` et laisse l'ancienne version de Core créer un nouveau fichier. Un [rapport ultérieur sur Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) montre un point d'écoute différent dans le fichier recréé. Vérifiez le nouveau fichier et `ha core info` avant de conclure que l'interface web est réparée.

Mon installation ne comportait aucun bloc YAML `http:`, aucune configuration HTTP en attente, ni certificat ou clé TLS dans les paramètres stables. Le profil enregistré était `intermediate_v6`. Dans ce cas limité, j'ai créé un candidat distinct en version 2.2 et conservé le point d'écoute existant :

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

Toutes les commandes précédentes doivent réussir avant le remplacement du fichier actif. Si `jq` échoue, inspectez le candidat avant de le supprimer et de réessayer. [Le code source HTTP de Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) définit la version de stockage 2.2 et accepte le profil `intermediate`. [Le code source de Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) utilise la version 3.1 et des noms de profils versionnés. J'ai également validé le candidat avec `HTTP_STORAGE_SCHEMA` de l'ancienne version de Core installée avant de l'installer.

Exécutez la vérification du schéma de l'ancienne version installée de Core tant que son conteneur fonctionne :

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schéma accepté")
'
```

Arrêtez-vous si le schéma rejette le candidat. Cette étape ne valide pas toutes les intégrations ni les formes non testées du stockage HTTP.

La vérification du schéma a affiché `Schéma accepté` pour ce candidat. Tout autre résultat met fin à cette procédure de récupération.

Cette conversion manuelle a été testée pour les champs indiqués. Un fichier contenant des paramètres TLS, des mandataires de confiance ou une configuration en attente nécessite son propre examen. Modifier uniquement le numéro de version principal laisse un profil que l'ancienne version de Core refuse.

Supervisor avait une tâche Core active et a rejeté `ha core stop` dans mon cas. J'ai arrêté le conteneur Core depuis la console de l'hôte, installé le candidat validé, puis redémarré le conteneur :

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

Si une commande échoue après l'arrêt, examinez le fichier HTTP actif avant d'exécuter `docker start homeassistant`. Un fichier modifié nécessite un nouveau candidat fondé sur son contenu actuel. La page HTTP est revenue après cette étape. Une réponse HTTP ne prouvait pas à elle seule que Core avait fini de démarrer. J'ai donc vérifié l'état de Supervisor avant de considérer le système comme rétabli.

Sur ce Yellow, `docker inspect -f '{{.State.Status}}' homeassistant` a ensuite affiché `running`. Vérifiez `ha core info` et le tableau de bord avant de demander une nouvelle mise à jour.

## Vérifier le résultat de la mise à jour {#verify-the-update-outcome}

Après le retour de l'accès HTTP, j'ai mis Core à jour vers 2026.11.1. Pour demander cette version :

```bash
ha core update --version 2026.11.1
```

La commande a signalé un échec après un long démarrage. Supervisor a ensuite enregistré Core à l'état RUNNING et `Successfully started Home Assistant 2026.11.1`. Une vérification d'état a montré que la version installée était à jour, que le fichier HTTP avait migré de nouveau vers la version 3.1 et que le conteneur n'avait pas redémarré pendant l'observation. Le tableau de bord authentifié s'est chargé. **Vérifiez l'état obtenu même si la commande de mise à jour signale un échec.**

Sur votre système, vérifiez la version, l'état de Supervisor et celui du conteneur après toute mise à jour longue :

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

Dans ce cas, les première et troisième commandes ont produit les résultats assainis suivants :

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Ouvrez ensuite le tableau de bord à votre adresse locale habituelle et confirmez le chargement des états en direct. Conservez le fichier HTTP enregistré jusqu'à ce qu'une sauvegarde ultérieure soit terminée et que le fonctionnement normal soit vérifié.

Les éléments observés sur mon Yellow n'ont pas établi la cause de l'échec initial de la mise à jour. Le message d'échec de la tâche suivante n'en indiquait pas non plus la cause. Une version installée et un tableau de bord fonctionnel prouvent mieux l'état obtenu que le seul message CLI, mais aucun des deux n'explique pourquoi Supervisor a marqué la tâche comme échouée.

## Étapes suivantes

Si l'erreur du stockage HTTP persiste, examinez le fichier conservé et restaurez une sauvegarde compatible ou exécutez une version de Core capable de lire sa version de stockage. Restaurer le fichier conservé en version 3 sous l'ancienne version de Core reproduit la panne. Si Core atteint RUNNING mais que certains appareils restent indisponibles, examinez ces intégrations séparément. Conservez la copie de récupération et la sauvegarde cloud jusqu'à la fin de la prochaine sauvegarde et tant que le tableau de bord reste réactif.
