---
title: "Miner Pearl (PRL) en 2026 : configuration, rentabilité et utilité de la chaîne"
date: 2026-09-22
lastmod: 2026-11-19
toc: true
draft: false
description: "Configurez le minage de Pearl PRL avec SRBMiner, examinez la preuve de travail utile, estimez les marges et évaluez l’utilité pratique de la chaîne."
genre: ["Cryptomonnaies", "Minage GPU", "Calcul IA", "DePIN", "Blockchain", "Linux", "Laboratoire à domicile", "Matériel"]
tags: ["minage Pearl", "minage PRL", "Pearl PRL", "preuve de travail utile", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "pool de minage Pearl", "LuckyPool Pearl", "minage GPU 2026", "crypto et calcul IA", "Pearl Research Labs", "minage combiné Nockchain", "minage combiné Nock", "minage RTX 3070", "configurer SRBMiner", "rig de minage Linux", "service de minage systemd", "minage par multiplication matricielle", "mineur vLLM", "portefeuille Pearl", "adresse prl1", "rentabilité du minage", "minage de calcul IA", "guide de minage crypto", "minage NVIDIA", "réglages d’overclocking pour le minage"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Illustration d’un rig de minage GPU moderne qui effectue des multiplications matricielles pour la blockchain Pearl, avec des flux de données dynamiques et des couleurs vives sur fond sombre."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl est la première chaîne de preuve de travail utile à atteindre une véritable échelle de production, et elle rémunère les mineurs pour des multiplications matricielles plutôt que pour le hachage.** Le réseau principal a été lancé le **27 avril 2026**. En quelques semaines, la promesse de sécuriser une blockchain tout en produisant du calcul pour l’IA dans la même opération a déclenché une ruée vers le minage GPU.

*La promesse est techniquement réelle, mais sa viabilité économique n’est pas démontrée. Toute l’histoire tient dans l’écart entre les deux.*

Ce guide explique comment miner du PRL, ce que calcule le mineur, pourquoi les marges se sont rapidement réduites après le lancement et si la chaîne produit une valeur réelle.

**À la fin du guide :** vous aurez un portefeuille, un mineur vérifié, une consommation électrique mesurée et un calcul de rentabilité fondé sur votre tarif. Considérez les estimations des pools et les revenus du lancement comme des observations datées, pas comme une garantie d’achat.

## Réponse rapide

**Pearl est une véritable réussite technique confrontée au problème économique du minage que connaît chaque nouvelle cryptomonnaie.**

| Sujet | Réponse rapide |
|---|---|
| **Qu’est-ce que Pearl ?** | Une blockchain L1 dérivée de Bitcoin et sécurisée par la preuve de travail utile. Les mineurs effectuent des multiplications matricielles bruitées plutôt que SHA-256 |
| **Comment la miner ?** | Avec SRBMiner-MULTI et `--algorithm pearlhash` sur un pool, ou avec le mineur vLLM de Pearl sur votre propre nœud |
| **Pourquoi était-elle rentable ?** | Pendant quelques semaines, les émissions du lancement ont dépassé la difficulté, puis celle-ci a rattrapé son retard |
| **Est-elle toujours rentable ?** | Cela dépend du matériel et la fenêtre se réduit. Consultez la section sur les marges |
| **La chaîne est-elle utile ?** | **Le mécanisme l’est, pas encore le marché.** Consultez le verdict |

**Le point le plus important avant de construire un rig :** les notes de version 3.6.8 du développeur du mineur indiquent qu’une prochaine mise à jour de Pearl rendra les GPU grand public « quasiment inutiles » pour le minage. Ce n’est pas l’avis d’un critique extérieur, mais celui de la personne qui développe le mineur.

## Ce qu’est Pearl

Pearl est une blockchain L1 développée par **Pearl Research Labs**. Son propre dépôt la décrit ainsi :

> "Pearl est une blockchain L1 fondée sur le protocole de preuve de travail utile, où le minage résulte de multiplications matricielles arbitraires."

Le dépôt comprend un nœud complet, un service de portefeuille, un client léger SPV, un système de preuve à divulgation nulle de connaissance et un mineur GPU. Le projet utilise la **licence ISC**, une licence permissive. L’infrastructure de la chaîne provient de projets Bitcoin éprouvés : **btcd** pour le nœud, **btcwallet** pour le portefeuille et **neutrino** pour le client léger.

**La conception reprend délibérément des éléments de Bitcoin**, jusqu’à une offre maximale de **2,1 milliards de PRL**, soit exactement cent fois les 21 millions de Bitcoin, avec une récompense de bloc décroissante et des blocs d’environ deux minutes.

*L’infrastructure est volontairement classique. La nouveauté réside entièrement dans la fonction de travail.*

### La preuve de travail utile expliquée

La preuve de travail utile est une vieille idée au bilan médiocre. Le principe consiste depuis toujours à remplacer le hachage volontairement énergivore de Bitcoin par un calcul qui produit aussi quelque chose de valeur. Presque toutes les tentatives précédentes ont échoué pour la même raison : le travail « utile » ne l’était pas, ou ne pouvait pas être vérifié à moindre coût pour sécuriser une chaîne.

Pearl applique cette idée avec une routine appelée **NoisyGEMM**. En pratique, un mineur effectue des multiplications matricielles bruitées sur un GPU, hache le résultat pour créer un engagement, puis enveloppe le travail dans une **preuve à divulgation nulle de connaissance** afin que la chaîne puisse le vérifier à peu de frais.

Le système s’appuie sur un article de cryptographie publié en 2025, **"Proofs of Useful Work from Arbitrary Matrix Multiplication"**, par Komargodski, Schen et Weinstein. L’article annonce un surcoût d’environ **1 + o(1) par rapport à une multiplication matricielle naïve**. C’est l’affirmation centrale du projet. Si la sécurisation de la chaîne n’ajoute presque rien au calcul sous-jacent, produire ce calcul revient presque à le faire gratuitement.

**La promesse : deux résultats pour une seule opération GPU.**

Cette affirmation distingue Pearl d’une décennie de concepts PoUW qui ont échoué. La plupart ne disposaient pas d’une telle borne.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Schéma montrant comment la preuve de travail utile de Pearl transforme une multiplication matricielle GPU en engagement par hachage et preuve à divulgation nulle de connaissance vérifiés à peu de frais par la chaîne" >}}

### Ce que calcule réellement le mineur

Il existe deux méthodes, qui ne sont pas équivalentes.

**La méthode officielle** se trouve dans le dépôt de Pearl. Elle comprend deux composants : `pearl-gateway`, qui relie votre nœud, et `vllm-miner`, qui effectue le calcul GPU avec vLLM. La passerelle communique en JSON-RPC avec un nœud local `pearld` et expose une interface de minage sur un socket Unix ou le port TCP 8337.

**La méthode par pool** est la plus courante. SRBMiner-MULTI implémente l’algorithme `pearlhash` de Pearl et vous le configurez pour rejoindre un pool.

Cette différence compte pour évaluer l’utilité. **Le mineur officiel charge un véritable modèle de langage.** L’exemple de la documentation Pearl exécute `pearl-ai/Llama-3.3-70B-Instruct-pearl` dans Docker avec accès au GPU. Ce modèle de 70 milliards de paramètres effectue des inférences pendant que la même opération sécurise la chaîne.

*Produire des inférences est une véritable capacité. Produire des inférences que personne n’achète revient à ajouter une blockchain à un centre de coûts. Gardez ces deux idées distinctes.*

## Pourquoi le minage était rentable et pourquoi cela a changé

La rentabilité initiale de Pearl n’avait rien de mystérieux ni de lié à l’IA. Elle suivait la courbe d’émission classique d’une nouvelle cryptomonnaie.

| Période | Événement |
|---|---|
| **27 avril 2026** | Lancement du réseau principal |
| **Fin mai 2026** | Début de la ruée vers le minage GPU, cinq semaines après le lancement |
| **Juin 2026** | Les revenus journaliers estimés d’une RTX 5090 **sont divisés à peu près par deux** avec la hausse de la difficulté |
| **Mi à fin 2026** | Les gains d’efficacité du logiciel de minage compensent en partie la baisse |

Le mécanisme de compression est simple :

1. **Les émissions de lancement sont élevées et la difficulté est faible.** Les premiers mineurs obtiennent des récompenses disproportionnées par unité de taux de hachage.
2. **Ces récompenses attirent du taux de hachage.** Davantage de GPU rejoignent la chaîne.
3. **La difficulté augmente pour s’ajuster.** La récompense par GPU diminue.

Pearl ajoute une seconde pression à la baisse, car la récompense de bloc diminue par conception. **Les revenus ont deux raisons de baisser, tandis que la difficulté n’a qu’une raison de monter.**

### Le facteur compensatoire : l’efficacité logicielle

Les marges n’ont pas chuté de façon uniforme, car les mineurs sont devenus plus rapides. Le journal des modifications de pearlhash dans SRBMiner suit cette évolution :

| Version | Modification de Pearlhash |
|---|---|
| **3.6.1** | Ajout de la prise en charge du B300. Le B300 SXM6 a atteint environ **706 TH/s à 920 W** avec `--gpu-cclock 1600` |
| **3.6.2** | Améliorations pour les séries H100, H200 et 4000 |
| **3.6.8** | Amélioration du taux de hachage, surtout sur la série 3000 |
| **3.6.9** | **Fortes améliorations d’efficacité.** Taux de hachage identique ou supérieur avec beaucoup moins de puissance sur la plupart des architectures |

**Pour le minage à domicile, l’électricité est le principal coût d’exploitation.** Une version qui maintient le taux de hachage tout en réduisant la consommation améliore directement la marge, sans changement du prix du jeton ni de la difficulté. Voilà pourquoi un rig à peine rentable en juin peut sembler raisonnable en septembre avec le même matériel.

*Les gains d’efficacité sont un avantage réel, mais temporaire, car tous les autres mineurs en profitent aussi et font grimper la difficulté.*

## Le soft fork de pénalisation du rang

Dans la nuit du **6 août 2026**, un soft fork s’est activé sur Pearl vers **02:00 UTC, au bloc 96251**. De nombreux mineurs l’ont découvert le lendemain matin en constatant une baisse de leur taux de hachage.

Le protocole Pearl comporte un paramètre de **rang de bruit**. Un rang supérieur facilitait le gain d’un jackpot pour une quantité de travail identique. **Certains mineurs utilisaient volontairement des rangs élevés pour obtenir un taux de hachage effectif et des récompenses disproportionnés.** L’équipe a enquêté sur ces optimisations anormales et instauré un mécanisme de pénalité.

| Changement de règle | Effet |
|---|---|
| **Rang minimal autorisé** | 128 |
| **Limite du jackpot** | Désormais calculée avec la formule `128 / rank` |
| **Avantage des rangs élevés** | Entièrement supprimé |

**Impact sur les mineurs :**

- Miner au-dessus du rang 128 a coûté aux opérateurs **50 à 87,5 % de leur taux de hachage effectif**
- Miner au rang 128 ou en dessous n’a presque rien coûté

Deux leçons s’appliquent à toute personne qui commence aujourd’hui.

**Votre taux de hachage dépend du logiciel et des règles du réseau, pas seulement du GPU.** Une configuration performante en juillet ne mesurait pas ce que l’opérateur croyait mesurer.

**Mettez le mineur à jour quand le réseau change.** Les anciennes versions perdent beaucoup en efficacité ou fonctionnent mal avec les nouvelles règles. Les logiciels de pool ont été mis à jour avant le fork, notamment PearlFortune v2.1.0 et Krig (Kryptex) v1.1.0, ainsi que des mineurs comme Tw-pearl-miner v3.3.0 et Wildrig 0.49.8.

*Une mise à jour qui réduit une récompense jusqu’à 87,5 % montre clairement pourquoi il faut suivre les annonces du projet au lieu de consulter uniquement un tableau de paiements.*

## Les deux méthodes pour miner Pearl

| | Minage par pool | Mineur officiel vLLM |
|---|---|---|
| **Logiciel** | SRBMiner-MULTI | `pearl-gateway` et `vllm-miner` |
| **Algorithme** | `pearlhash` | NoisyGEMM avec vLLM |
| **Nœud requis** | Non | **Oui, un `pearld` synchronisé** |
| **Paiement** | Pool, PPLNS ou solo | Directement à votre adresse de minage |
| **Exécute un vrai modèle** | Non | **Oui, par exemple Llama-3.3-70B-Instruct** |
| **Effort de configuration** | Faible | Élevé, nécessite CUDA Toolkit et Python 3.12 |
| **Idéal pour** | Obtenir rapidement du taux de hachage sur le réseau | Fournir directement de la puissance de calcul au réseau |

**Commencez par le minage par pool.** Il ne nécessite ni nœud, ni synchronisation, ni téléchargement de modèle, et vous apporte du taux de hachage ainsi qu’une adresse de paiement en quelques minutes. Passez au mineur officiel uniquement si vous souhaitez fournir des inférences ou exploiter un nœud.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Comparaison du minage Pearl par pool avec SRBMiner et du mineur vLLM officiel, montrant les composants de nœud, de passerelle et d’inférence requis par chaque méthode" >}}

## Matériel pour les GPU grand public

Pearl se distingue par ce qu’elle ne demande pas. Hashrate Index décrit des besoins **particulièrement modestes : peu de RAM, de stockage et de CPU, sans le réseau multifibre coûteux d’un vrai cluster d’entraînement.** Un analyste y voit « une excellente façon d’utiliser du matériel disponible ».

C’est son attrait concret. **Les GPU que vous possédez déjà, même anciens, rapportent quelque chose.**

| Catégorie de GPU | Observation |
|---|---|
| **RTX 5090 et 4090** | Revenus les plus élevés par carte. C’est dans ces catégories que la division initiale des revenus par deux a été mesurée |
| **Série RTX 3000** | Ciblée par l’amélioration de taux de hachage de la version 3.6.8. Elle reste viable, mais l’efficacité compte plus que la vitesse brute |
| **Accélérateurs de centre de données** | Les H100, H200 et B300 ont été ajoutés et améliorés en 2026. C’est là que se dirige la course au taux de hachage |
| **Cartes anciennes ou à faible VRAM** | Rentabilité marginale. Consultez un calculateur de rentabilité à jour avant d’acheter quoi que ce soit |

**La tendance de chaque version de 2026 est identique.** Les accélérateurs haut de gamme ont été ajoutés et améliorés en premier, car leur taux de hachage vaut davantage. Les cartes grand public ont été optimisées quand la série 3000 disposait encore d’une marge de progression.

*Optimiser l’efficacité rapporte plus que rechercher la fréquence maximale. C’est le contraire de ce qu’enseignent la plupart des guides de minage.*

## Configuration sous Linux

Le minage par pool nécessite quatre éléments : le binaire SRBMiner, une adresse de portefeuille Pearl, un serveur de pool et un service qui maintient le processus en cours.

### Créez d’abord une adresse de portefeuille

Les adresses de minage Pearl commencent par **`prl1`**. Le portefeuille officiel est **Oyster**, le service de portefeuille HD du dépôt Pearl, qui expose des interfaces JSON-RPC et gRPC. Générez une adresse de minage **Taproot** avec ce service.

Ne sautez pas cette étape et ne réutilisez pas une adresse d’une autre chaîne. **Les récompenses envoyées à une adresse que vous ne contrôlez pas sont perdues.**

### Pools, ports et minage combiné

Le plus grand pool Pearl est LuckyPool. Ses ports sont répartis selon le taux de hachage attendu :

| Port | Difficulté de départ | Taux de hachage conseillé |
|---|---|---|
| **3360** | 2M | Moins de 500 TH/s |
| **3361** | 4M | De 500 à 1 000 TH/s |
| **3362** | 8M | Plus de 1 000 TH/s |

Choisissez un port adapté au taux de hachage réel de votre rig. **Un GPU grand public seul doit utiliser le port 3360.** Un petit rig sur un port à haute difficulté attend longtemps entre les parts et subit une variance plus forte, sans aucun avantage.

Deux fonctionnalités des pools méritent d’être connues :

- **Le minage solo** fonctionne sur n’importe quel port en ajoutant `solo:` devant l’adresse du portefeuille. Vous gardez toute la récompense si vous trouvez un bloc et ne gagnez rien autrement. Avec un taux de hachage grand public, l’attente sera longue.
- **Le minage combiné Nockchain** rapporte du NOCK en plus du PRL pour le même taux de hachage. Ajoutez `+NOCK_ADDRESS` à votre adresse Pearl. Le pool verse le NOCK sur Nockchain elle-même, donc une adresse de jeton enveloppé commençant par `0x` ne peut pas le recevoir. **Votre mineur doit prendre en charge le minage combiné. Sans cette fonction, il continue à miner Pearl normalement.**

Le pool publie des serveurs sur `luckypool.io` et des serveurs relais sur `lproute.com`. Si votre réseau bloque le trafic direct de minage, gardez le port et changez le domaine.

## Un script d’installation fonctionnel

Le script ci-dessous installe SRBMiner comme service systemd sur Debian ou Ubuntu. Il détecte tous les GPU, applique des paramètres d’overclocking par carte, vérifie le téléchargement avec le MD5 publié, crée l’unité et une règle logrotate, puis redémarre le service.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- configure SRBMiner (Pearl / PRL) comme service systemd.
# Exécution : sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... ajoutez +NOCK_ADDRESS pour le minage combiné
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Réglages pour RTX 3070. MCORE verrouille la fréquence mémoire à une valeur absolue, bien inférieure à la
# fréquence d’origine de 7001 MHz. Il s’agit d’une sous-fréquence volontaire pour réduire la consommation, pas d’un
# overclocking destiné aux performances. Utilisez "" pour désactiver une option.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

Le bloc de réglage mérite une explication, car il semble erroné au premier abord. **`MCORE=5001` est inférieur à la fréquence mémoire d’origine d’une 3070.** C’est intentionnel. Pearl récompense l’efficacité mémoire, et réduire sa fréquence diminue la consommation davantage que le taux de hachage. **Ne reprenez pas les valeurs d’overclocking d’une ligne de base de données sans vérifier le GPU utilisé pour la mesure.** Les résultats concernent souvent une autre carte que la vôtre.

```bash
[ "$(id -u)" -eq 0 ] || { echo "exécutez en tant que root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "nvidia-smi absent : installez d’abord le pilote"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== $GPU_N GPU NVIDIA détecté(s) =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Créez un ensemble de paramètres d’overclocking pour chaque GPU détecté
OC=""
for i in $(seq 0 $((GPU_N - 1))); do
    [ -n "$COFFSET" ] && OC="$OC --gpu-coffset$i $COFFSET"
    [ -n "$CCLOCK" ]  && OC="$OC --gpu-cclock$i $CCLOCK"
    [ -n "$MCLOCK" ]  && OC="$OC --gpu-mclock$i $MCLOCK"
    [ -n "$PLIMIT" ]  && OC="$OC --gpu-plimit$i $PLIMIT"
    [ -n "$FAN" ]     && OC="$OC --gpu-fan$i $FAN"
done
THERMAL_ARG=""
[ -n "$THERMAL" ] && THERMAL_ARG=" --shutdown-temperature $THERMAL"

# Télécharger et vérifier la version
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Arrêter le service avant de remplacer le binaire : le processus garde le fichier ouvert
systemctl stop "$SVC" 2>/dev/null || true
tar -xzf "$TMP/$STEM.tar.gz" -C "$TMP"
SRC=$(find "$TMP" -maxdepth 1 -type d -name 'SRBMiner-Multi-*' | head -1)
mkdir -p "$MINER_DIR"
[ -f "$MINER_DIR/SRBMiner-MULTI" ] && \
    cp -a "$MINER_DIR/SRBMiner-MULTI" "$MINER_DIR/SRBMiner-MULTI.bak-$(date +%F-%H%M%S)"
cp -a "$SRC"/. "$MINER_DIR"/
chown -R root:root "$MINER_DIR"
chmod 755 "$MINER_DIR/SRBMiner-MULTI"
```

**Vérifiez le MD5 avant d’exécuter un binaire de minage.** Les versions publient une empreinte pour chaque fichier, et le mineur s’exécute avec les privilèges root tout en accédant au GPU. Sans vérification, vous faites confiance à un téléchargement que vous n’avez pas contrôlé.

Deux détails opérationnels de l’unité de service :

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Mineur Pearl (PRL) SRBMiner v$SRB_VERSION - $WORKER
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$MINER_DIR
ExecStart=$MINER_DIR/SRBMiner-MULTI --algorithm $ALGO --pool $POOL --wallet $WALLET --worker $WORKER --disable-cpu --gpu-reset-oc$OC$THERMAL_ARG --api-enable --api-port 21550 --api-rig-name $WORKER
Restart=always
RestartSec=10
StandardOutput=append:$LOG
StandardError=append:$LOG
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
```

- **`--disable-cpu`** empêche le mineur d’utiliser le processeur, ce qui compte si la machine effectue d’autres tâches.
- **`--shutdown-temperature 88`** arrête le mineur en cas de panne d’un ventilateur, au lieu de laisser la carte surchauffer.
- **`--gpu-reset-oc`** efface les anciennes fréquences avant d’appliquer les vôtres et évite de conserver des réglages périmés.
- **`Restart=always` avec `RestartSec=10`** permet de survivre aux incidents de pilote, fréquents sur les rigs multi-GPU.
- **`--api-enable` ouvre un port de supervision.** Vérifiez l’interface sur laquelle écoute le port 21550 et ne l’exposez pas à un réseau non fiable. Le point de supervision d’un rig n’a pas besoin d’être accessible depuis l’extérieur.

Configurez enfin la rotation des journaux, car les fichiers de minage grossissent sans limite :

```bash
cat >/etc/logrotate.d/pearl-miner <<EOF
$LOG {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
EOF

systemctl daemon-reload
systemctl enable "$SVC" >/dev/null 2>&1 || true
systemctl restart "$SVC"
```

*`copytruncate` est important ici. SRBMiner garde le journal ouvert. Si la rotation renomme le fichier, le mineur continue d’écrire dans un inode supprimé et le disque se remplit quand même.*

Suivez la progression avec un extrait filtré plutôt qu’avec le journal brut :

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Les problèmes rencontrés

**Un guide de minage Pearl doit commencer par les problèmes, car ils affectent tous vos paiements.** Quatre incidents se sont produits entre juillet et septembre 2026.

### Un marché concentré sur une seule plateforme

Le **23 juillet 2026**, le PRL a atteint un plus bas historique de **0,1399 $**, contre environ **0,87 $** en juin. Il a chuté de **24,2 % en une journée** et de **26,7 % sur la semaine**, tandis que le marché crypto au sens large progressait d’environ 2 % sur la même période.

La cause n’était pas une nouvelle. C’était le manque de profondeur.

- **95,17 % du volume déclaré** se trouvait sur **une seule plateforme, SafeTrade**, qui n’a pas de score de confiance CoinGecko. Une seule paire PRL/USDT représentait **738 399 $ sur environ 775 000 $** échangés en 24 heures.
- Les deux paires SafeTrade affichaient une **profondeur du carnet d’ordres de 0,00 $**.

*Un ordre de vente ordinaire déplace un marché comme celui-ci de plusieurs dizaines de pour cent. C’est une caractéristique structurelle du jeton, pas une situation temporaire.*

La répartition de l’offre amplifie le problème :

| Indicateur | Valeur |
|---|---|
| **Capitalisation boursière** | 55,7 millions de dollars |
| **Valorisation entièrement diluée** | 458,6 millions de dollars |
| **Ratio** | Plus de 8 fois |
| **Offre en circulation** | 255 millions sur 2,1 milliards, moins de **13 %** |

**Un jeton coté sur un carnet d’ordres peu profond, avec 87 % de l’offre verrouillée ou non émise, admet une vaste gamme de prix plausibles.** Planifiez l’utilisation de vos paiements et ne prenez pas le prix au comptant pour une estimation fiable des revenus.

### Un pool a été piraté

Un ticket ouvert le **18 septembre 2026** indique que le portefeuille Pearl 2.0.5 « suspendait toujours les envois et les réceptions après le piratage de son pool, survenu un mois auparavant ».

**Relisez cette phrase : elle contient deux faits.** Un pool Pearl a été compromis vers **août 2026**, et le portefeuille officiel a suspendu les transferts en réponse. La suspension était toujours en vigueur un mois plus tard.

Le pool choisi détient vos paiements. Vérifiez son historique d’incidents avant d’y connecter un rig.

### Le site du projet est inaccessible

Au moment de la rédaction, **pearlresearch.ai ne mène à aucun serveur.** Tous les résolveurs publics renvoient une route nulle, `0.0.0.0`, pour le domaine principal et ses sous-domaines, notamment `compute` et `explorer`. L’enregistrement du domaine indique `ACTIVE` : il s’agit donc d’un état DNS délibéré, pas d’une expiration.

**Trois liens qu’un guide de minage proposerait normalement sont morts**, dont celui de l’explorateur de blocs. Mining Pool Stats les répertorie toujours, ce qui pousse les lecteurs à chercher une adresse qui ne charge jamais.

Utilisez plutôt **[l’explorateur de blocs PRL](https://prlscan.com)**. J’ai confirmé que la page fonctionne.

### Le logiciel comporte encore des bogues ouverts

Le suivi public des problèmes faisait état de défauts non résolus fin septembre 2026. La création de tickets est restreinte, donc cette vue est partielle.

| Problème | Date | Conséquence |
|---|---|---|
| **Code RPC du portefeuille de bureau inactif** | 22 sept. | Le portefeuille ne peut pas joindre un nœud |
| **Le réseau de test ne peut pas se synchroniser depuis zéro**, les nœuds se bloquent à la hauteur 36760 | 22 sept. | Défaut bloquant de synchronisation |
| **Envoi et réception du portefeuille toujours suspendus** après le piratage du pool | 18 sept. | Les transferts sont affectés |
| **La version macOS ARM64 a une signature de code invalide** | 17 sept. | Elle ne démarre pas sans contourner Gatekeeper |
| **Le mode d’élagage supprime les certificats nécessaires à la vérification des en-têtes** | 30 août | Défaut de validation |
| **Le nœud se bloque indéfiniment lorsqu’aucun pair connecté ne peut synchroniser** | 30 août | Synchronisation fragile |
| **pearl-gemm échoue sur la RTX 5070** : les noyaux de hachage fonctionnent, ceux de GEMM échouent | 31 août | Les dernières cartes grand public ne sont pas prises en charge |

*Le cas de la RTX 5070 mérite votre attention si vous comptiez acheter une carte récente. L’architecture grand public la plus récente ne fonctionnait pas avec la méthode GEMM officielle.*

**En résumé :** le logiciel de minage est activement maintenu, tandis que les couches destinées aux utilisateurs et au marché sont les points faibles. SRBMiner a publié la version 3.6.9 et ses grands gains d’efficacité la veille des plaintes sur le portefeuille.

## La chaîne est-elle utile ?

Cette question mérite une réponse nuancée, car la plupart des articles utilisent « travail utile » pour désigner deux choses. **L’expression décrit à la fois un mécanisme de consensus et une promesse économique, et les réponses sont très différentes.**

### Utilité fonctionnelle : partielle

**La chaîne fonctionne. Le produit qui l’entoure n’est pas entièrement opérationnel.**

Ce qui fonctionne :

- **Le réseau principal a été lancé le 27 avril 2026** et produit des blocs depuis.
- **La pile logicielle complète existe** : un nœud, un service de portefeuille, un client léger SPV, un système de preuve à divulgation nulle de connaissance et un mineur GPU dans un même dépôt.
- **L’infrastructure est éprouvée au niveau du code.** Le nœud, le portefeuille et le client léger dérivent de **btcd**, **btcwallet** et **neutrino**, des projets Bitcoin soumis à des années de tests adversariaux.
- **La base de code témoigne d’un effort sérieux.** Elle compte 315 étoiles, 76 forks, plus de 6 800 commits et un suivi public où les contributeurs déposent des rapports de bogue précis.
- **Le minage fonctionne.** SRBMiner a publié 247 versions et optimisé `pearlhash` à plusieurs reprises. Plusieurs pools tournent. Le minage combiné de Nockchain fonctionne.

Ce qui ne fonctionne pas :

- **Les transferts sont suspendus dans le portefeuille officiel** depuis le piratage du pool.
- **Le portefeuille de bureau ne peut pas joindre un nœud**, selon son propre suivi fin septembre.
- **La synchronisation présente des défauts bloquants** sur le réseau de test comme sur le réseau principal.
- **Le site du projet est inaccessible.**
- **Les GPU grand public les plus récents échouent sur la voie GEMM.**

**La conclusion honnête est que Pearl fonctionne au niveau du protocole mais reste peu fiable comme produit.** Cela intéresse les personnes qui étudient la preuve de travail utile. C’est un avertissement pour celles qui s’attendent à miner et à être payées de façon fiable.

### Utilité technique : le mécanisme oui, le marché non

La réponse honnête se divise en deux. Confondre les deux volets est l’erreur de la plupart des analyses.

**Le mécanisme est vraiment novateur.** NoisyGEMM effectue des multiplications matricielles bruitées sur GPU, hache le résultat pour créer un engagement et enveloppe le travail dans une preuve à divulgation nulle de connaissance pour maintenir une vérification peu coûteuse. Le procédé s’appuie sur l’article "Proofs of Useful Work from Arbitrary Matrix Multiplication" de Komargodski, Schen et Weinstein, qui annonce un surcoût d’environ **1 + o(1)** par rapport à une multiplication matricielle naïve.

**Si cette borne tient, la chaîne se sécurise à un coût presque nul au-delà du calcul sous-jacent.** C’est ce qu’aucune tentative précédente de PoUW n’a réussi à faire. Les mathématiques ne sont pas décoratives.

**Le marché n’est pas établi.** Hashrate Index l’a formulé ainsi : « aujourd’hui, la plupart des travaux utiles consistent en des inférences que personne n’a achetées, ce qui donne à l’essentiel du minage actuel la forme d’une preuve de travail pour l’IA ». C’est un résumé juste. Le calcul correspond au besoin, mais personne ne paie pour l’essentiel.

L’exception est importante et bien réelle. Pearl a conclu un partenariat exclusif avec **Together AI**, qui a mis en production un point d’accès d’inférence Pearl à prix réduit. C’est son premier client et la raison pour laquelle le projet mérite davantage de crédit que la cryptomonnaie IA moyenne.

**Un client prouve un concept, pas l’existence d’un marché.**

### Utilité pratique : pour l’instant, mais la fenêtre se referme

Pour un mineur, la situation pratique est mitigée et limitée dans le temps.

**Ce qui joue en faveur de Pearl :**

- Les GPU existants génèrent des revenus, même les anciens, car les exigences matérielles sont faibles
- Les progrès d’efficacité du mineur améliorent directement la marge du matériel que vous possédez déjà
- Le minage combiné avec Nockchain ajoute une seconde source de revenus pour le même taux de hachage
- Un surcoût presque nul évite à la chaîne de gaspiller votre électricité dans des calculs de hachage inutiles

**Ce qui joue contre :**

- **La récompense de bloc baisse par conception.** C’est le modèle de Bitcoin et les émissions diminuent, quel que soit le prix.
- **La difficulté ne fait qu’augmenter.** Les revenus par GPU n’ont qu’une direction possible.
- **La liquidité est faible.** Hashrate Index indique qu’il faut surveiller la capacité du PRL à attirer des liquidités au-delà des petites plateformes. Une faible liquidité élargit les écarts et dégrade les prix réellement obtenus.
- **La mise à niveau du protocole.** Les notes SRBMiner 3.6.8 annoncent qu’une future mise à jour de Pearl rendra les GPU grand public « quasiment inutiles ». Prenez cela au sérieux : cela vient du développeur, qui a intérêt à ce que les gens continuent de miner.

## Verdict

**Pearl est l’implémentation de preuve de travail utile la plus crédible à ce jour, mais elle n’a pas démontré l’utilité économique de son travail.**

Quatre affirmations, par ordre de certitude :

1. **Le mécanisme de consensus fonctionne et l’affirmation cryptographique est réelle.** Pearl a résolu le problème technique difficile : rendre PoUW peu coûteux à vérifier. C’est une véritable contribution, quel que soit l’avenir du jeton.

2. **Le calcul est une promesse, pas un produit.** Produire des inférences ne signifie pas les vendre. Aujourd’hui, un partenariat rémunéré fait face à un réseau rempli de taux de hachage spéculatifs. La boucle est conçue, mais elle ne tourne pas.

3. **La fenêtre de minage GPU grand public se réduit et le protocole la fermera.** La baisse des récompenses, la hausse de la difficulté, une mise à jour annoncée qui élimine la viabilité des GPU grand public et un soft fork qui a déjà fait perdre jusqu’à 87,5 % à certains mineurs forment une occasion limitée dans le temps, pas une source de revenus.

4. **Les vrais risques sont opérationnels et liés au marché, pas à la cryptographie.** Un pool piraté, les transferts suspendus du portefeuille, un site inaccessible, des défauts de synchronisation non résolus et 95 % du volume sur une plateforme sans profondeur de carnet d’ordres déterminent si le minage rapporte. Le protocole est la partie qui fonctionne.

*Pour le dire simplement : Pearl a résolu le problème difficile, pas encore celui qui paraît facile. Prouver l’utilité d’une multiplication matricielle relève de la cryptographie. Trouver un acheteur pour le résultat relève de la vente.*

**Si vous voulez miner, considérez cela comme un usage à court terme du matériel que vous possédez déjà.** N’achetez pas de GPU pour Pearl. Ne construisez pas de rig en supposant que les chiffres actuels dureront, car le calendrier des émissions et les notes du développeur du mineur disent le contraire.

**Si vous voulez comprendre la preuve de travail utile, Pearl est l’implémentation la plus importante à étudier aujourd’hui.** C’est la première à avoir atteint une véritable échelle. Les preuves des deux prochaines années montreront si le « travail utile » est une véritable primitive ou un nouvel échec récurrent doté d’une meilleure cryptographie.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Évaluation de la preuve de travail utile de Pearl selon trois axes : maturité fonctionnelle élevée, mécanisme technique solide mais marché payant non démontré, et viabilité pratique du minage limitée dans le temps" >}}

## À retenir

- **Pearl est une blockchain L1 dérivée de Bitcoin et sécurisée par la preuve de travail utile.** Les mineurs effectuent des multiplications matricielles bruitées plutôt que du hachage. Le réseau principal a été lancé le **27 avril 2026**.
- **Deux méthodes permettent de miner :** SRBMiner avec `--algorithm pearlhash` sur un pool, ou `vllm-miner` de Pearl sur un nœud synchronisé.
- **La rentabilité initiale venait de la courbe d’émissions du lancement**, pas de la demande en IA. Les revenus journaliers estimés d’une RTX 5090 ont été divisés par deux quelques semaines après la ruée.
- **Les gains d’efficacité du mineur ont compensé une partie de la baisse.** La version 3.6.9 a livré un taux de hachage identique ou supérieur avec beaucoup moins de puissance.
- **Le soft fork de pénalisation du rang du 6 août 2026 a réduit de 50 à 87,5 % le taux de hachage effectif** des mineurs au-dessus du rang 128. Mettez votre mineur à jour lorsque les règles changent.
- **Le jeton dépend d’une seule plateforme.** SafeTrade concentrait 95,17 % du volume et n’affichait aucune profondeur de carnet d’ordres. Moins de 13 % de l’offre est en circulation.
- **Un pool a été piraté vers août 2026**, et les transferts du portefeuille officiel étaient encore suspendus un mois après.
- **Le domaine du site du projet ne répond pas.** Utilisez `prlscan.com` pour explorer les blocs.
- **Optimisez l’efficacité, pas la fréquence.** Pearl récompense l’efficacité mémoire, et réduire la fréquence mémoire diminue la consommation davantage que le taux de hachage.
- **Utilisez le port 3360 avec un seul GPU grand public** et ajoutez `+NOCK_ADDRESS` pour miner Nockchain en parallèle.
- **Vérifiez le MD5** de tout téléchargement du mineur avant de l’exécuter en root.
- **Mine avec le matériel que vous possédez déjà.** La chaîne fonctionne au niveau du protocole, reste peu fiable comme produit et ne dispose que d’un seul partenariat pour vendre son calcul.

## Étapes suivantes

1. **Consultez le dépôt source** du nœud, du portefeuille et du mineur officiel vLLM : **[Dépôt Pearl Research Labs](https://github.com/pearl-research-labs/pearl)**
2. **Consultez le journal des modifications avant tout réglage**, car l’efficacité varie selon la version : **[Versions SRBMiner-MULTI](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Choisissez un port de pool** adapté à votre taux de hachage mesuré : **[LuckyPool pour Pearl](https://pearl.luckypool.io)**
4. **Comparez la répartition du taux de hachage entre les pools** avant de choisir : **[Statistiques des pools de minage Pearl](https://miningpoolstats.stream/pearl)**
5. **Calculez d’abord votre coût électrique**, car il détermine la rentabilité : **[Construire un boîtier rentable pour un revenu passif](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Appliquez les règles de réglage multi-GPU** de notre autre guide sur le minage à travail utile : **[Miner efficacement Spacemesh avec plusieurs GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Articles associés

| Article | Sujet |
|---|---|
| **[Miner efficacement Spacemesh avec plusieurs GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Réglage multi-GPU et gestion de l’énergie sur une autre chaîne à travail utile |
| **[Construire un boîtier rentable pour un revenu passif](/other/creating-profitable-low-powered-crypto-miners/)** | Dimensionner le matériel de minage selon le coût électrique avant l’achat |
| **[IA locale en 2026 : un modèle 27B bat Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Utilisation des mêmes GPU pour l’inférence locale plutôt que le minage |
| **[Miner Verus sur Android : guide facile pour miner avec un smartphone](/other/mine-verus-on-android-guide/)** | Minage CPU avec le matériel que vous possédez déjà |

## Références

1. [Pearl Research Labs : monorepo du réseau](https://github.com/pearl-research-labs/pearl)
2. [Problèmes ouverts dans le dépôt Pearl](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL) : comment les mathématiques matricielles deviennent calcul IA et minage - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Activation du soft fork de pénalisation du rang sur le réseau Pearl (PRL) - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl atteint un nouveau plus bas historique : 95 % du volume sur une plateforme sans profondeur - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [Versions SRBMiner-Multi - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool : pool de minage combiné Pearl et Nock](https://pearl.luckypool.io)
8. [Statistiques des pools de minage : Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [Explorateur de blocs PRL - prlscan.com](https://prlscan.com)

**Note sur le domaine officiel :** `pearlresearch.ai` et ses sous-domaines `compute` et `explorer` renvoient une route nulle au moment de la rédaction. L’article les omet délibérément plutôt que de publier des liens morts et renvoie vers `prlscan.com` pour l’exploration des blocs.
