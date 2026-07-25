---
title: "ATS Resume Improver : optimiseur de CV IA gratuit, auto-hébergeable, sans envoi de données"
date: 2026-07-22
toc: true
draft: false
description: "ATS Resume Improver est un optimiseur de CV open source côté client supportant OpenAI, Anthropic Claude et les modèles Ollama locaux. Analysez, notez, comparez les mots-clés, optimisez et exportez votre CV sans que vos données ne quittent le navigateur."
genre: ["Outils de carrière", "Projets open source", "Intelligence artificielle", "Technologie de confidentialité", "Outils développeurs", "Recherche d'emploi", "Productivité"]
tags: ["ATS Resume Improver", "optimisation ATS", "scanner de CV", "CV IA", "CV OpenAI", "CV Claude", "Ollama IA locale", "auto-hébergé", "confidentialité d'abord", "outils recherche d'emploi", "analyse d'écart de mots-clés", "lettre de motivation", "score CV", "React", "TypeScript", "Docker", "Vite", "open source", "export PDF", "export DOCX", "parser CV", "outils carrière", "préparation entretien", "estimateur salaire", "détection type CV", "score ATS", "outil CV gratuit", "GitHub", "sans collecte de données"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Un ordinateur portable moderne sur un bureau affichant une interface colorée d'optimisation de CV avec des graphiques, sur un fond bleu marine profond."
coverCaption: "ATS Resume Improver — analyse de CV 100% côté client et optimisation IA sans collecte de données."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Gratuit, open source et auto-hébergeable. Votre CV ne touche aucun serveur sauf si vous utilisez un fournisseur IA. Et même dans ce cas, il va directement chez le fournisseur IA, pas chez nous.**

## Qu'est-ce que ATS Resume Improver ?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** est un optimiseur de CV open source basé sur navigateur qui analyse votre CV par rapport à une description de poste et vous aide à combler l'écart entre ce que vous avez et ce que les systèmes de suivi des candidatures notent réellement. Construit avec React 19, Vite et TypeScript, l'intégralité du **pipeline d'analyse et de notation tourne dans votre navigateur** sans serveur backend.

Le code source est sur **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**. Vous pouvez utiliser la version hébergée, déployer votre propre instance sur Vercel/Netlify/Cloudflare/GitHub Pages en un clic, ou le lancer localement avec Docker.

### Le problème de confidentialité qu'il résout

La plupart des services d'optimisation de CV téléchargent votre CV sur leurs serveurs, effectuent une notation propriétaire et conservent vos données. ATS Resume Improver adopte l'approche inverse.

| Mode | Ce qui quitte votre appareil |
|------|------------------------|
| **Sans clé IA** | Rien — 100% local, tourne dans votre navigateur |
| **OpenAI / Anthropic** | Texte du CV + description de poste vont directement à l'API du fournisseur IA avec votre clé — pas de serveur intermédiaire |
| **Ollama (local)** | Rien — le modèle tourne sur votre propre machine |

**Les clés API sont stockées en mémoire uniquement** et disparaissent quand vous fermez l'onglet. Pas d'analytique, pas de tracking, pas de cookies.

______

## Fonctionnalités principales

### Ce qui fonctionne sans clé IA

Vous n'avez pas besoin de clé API pour obtenir une vraie valeur. Le mode sans clé inclut :

- **Upload de CV** — PDF, DOCX, TXT ou Markdown
- **Extraction de texte ATS** — montre exactement ce qu'un ATS parse dans votre fichier, y compris ce qui est perdu dans la mise en forme
- **Détection du type de CV** — identifie automatiquement lequel des 7 profils correspond à votre CV et adapte l'ordre des sections
- **Détection des sections et avertissements de format** — signale les sections manquantes et les formats hostiles aux parsers
- **Score ATS (0–100)** avec une décomposition en 5 dimensions
- **Analyse d'écart de mots-clés** — correspondance de chaînes basée sur des règles avec la description de poste
- **Optimisation ATS déterministe** — restructuration locale basée sur des règles
- **Visualiseur de différences avant/après** — voyez exactement ce qui a changé
- **Export professionnel PDF, DOCX, TXT et Markdown**

### Ce que l'IA débloque

Connectez OpenAI, Anthropic Claude ou Ollama local et l'outil passe à :

- **Analyse sémantique de mots-clés** — comprend le contexte, pas seulement les correspondances de chaînes. Affiche la force de correspondance (Fort/Modéré/Partiel), la localisation ("trouvé dans Compétences et 3 postes"), l'importance par mot-clé (Critique/Élevé/Moyen/Faible) et un résumé narratif IA de 2-3 phrases
- **Optimisation IA du CV** — réécriture complète par IA avec des prompts de bonnes pratiques ATS
- **Exports améliorés par IA** — PDF/DOCX formatés par l'IA avant le téléchargement
- **Génération de lettre de motivation** — avec des règles de humanisation qui éliminent les signes révélateurs de l'IA
- **Prédicteur de questions d'entretien** — basé sur la description de poste
- **Estimateur de fourchette salariale**

______

## Détection du type de CV

L'application classe automatiquement votre CV dans l'un des 7 profils et adapte l'ordre des sections aux attentes des recruteurs et des ATS pour ce stade de carrière :

| Profil | Idéal pour | Priorité des sections |
|---------|----------|-----------------|
| 🏢 **Professionnel expérimenté** | 5+ ans, carrière linéaire | Expérience → Compétences → Formation |
| 🌱 **Niveau intermédiaire** | 2–5 ans | Expérience → Compétences → Formation |
| 🎓 **Débutant** | 0–2 ans | Compétences → Formation → Projets → Expérience |
| 🎒 **Étudiant / Jeune diplômé** | Encore inscrit | Formation → Projets → Compétences → Expérience |
| 🔬 **Universitaire / Chercheur** | Doctorat, publications | Formation → Recherche → Publications → Expérience |
| 📜 **Axé certifications** | Les certifs surpassent le diplôme | Certifications → Compétences → Expérience → Formation |
| 🔄 **Reconversion** | Écart ou pivot détecté | Résumé → Compétences transférables → Formation → Expérience |

*L'ordre des sections s'applique de manière cohérente dans l'optimisation, les exports PDF, DOCX, TXT et Markdown — pas seulement à l'écran.*

______

## Analyse sémantique IA des mots-clés

C'est là que l'outil se distingue des simples compteurs de mots-clés. Quand un fournisseur IA est configuré, l'analyse d'écart de mots-clés passe du simple filtrage de chaînes au raisonnement sémantique :

| Dimension | Sans IA | Avec IA |
|-----------|-----------|---------|
| **Méthode de correspondance** | Correspondance de chaîne exacte uniquement | Compréhension sémantique du contexte |
| **Force de correspondance** | — | Évaluations Fort / Modéré / Partiel |
| **Contexte de correspondance** | — | "trouvé dans Compétences et 3 postes" |
| **Importance des écarts** | Tous les écarts traités également | Critique / Élevé / Moyen / Faible |
| **Suggestions** | Conseils génériques | Suggestions actionnables par mot-clé |
| **Couverture %** | Basée sur le nombre de chaînes | Pondérée sémantiquement |
| **Résumé** | — | Narratif IA de 2-3 phrases |

*L'analyse locale basée sur des règles tourne instantanément. Les résultats IA l'enrichissent de manière asynchrone pendant que vous examinez.*

______

## Fournisseurs IA supportés

Tous les appels IA incluent des prompts de bonnes pratiques ATS dérivés des directives Harvard OCS et Columbia CCE.

### OpenAI

| Modèle | Idéal pour |
|-------|----------|
| **GPT-4.1 mini** (défaut) | Plus intelligent, rapide et abordable — recommandé |
| GPT-4o mini | Rapide et abordable classique |
| GPT-4.1 | Dernier GPT-4.1 — suivi d'instructions précis |
| GPT-4o | Qualité élevée, phare |
| GPT-4 Turbo | Grande fenêtre de contexte |
| GPT-3.5 Turbo | Le plus rapide et le moins cher |

**Coût estimé** : ~0,002 à 0,05 $ par analyse de CV.

### Anthropic Claude

| Modèle | Idéal pour |
|-------|----------|
| **Claude Sonnet 4.5** (défaut) | Rapide et intelligent — recommandé |
| Claude Opus 4.5 | Le plus capable — meilleur pour les tâches complexes |
| Claude Haiku 4.5 | Le plus rapide et le moins cher |
| Claude 3.5 Sonnet | Fiable et bien testé |
| Claude 3.5 Haiku | Rapide et abordable v3.5 |

### Ollama (local / auto-hébergé)

Pas de clé API nécessaire. Exécutez le modèle sur votre propre matériel. Définissez `OLLAMA_ORIGINS=*` pour autoriser l'accès navigateur.

| Modèle | Notes |
|-------|-------|
| **Llama 3.3** (défaut) | Dernier Meta Llama — recommandé |
| Llama 3.2 | Meta Llama 3.2 |
| Mistral 7B | Rapide et capable |
| Mixtral 8x7B | Mélange d'experts |
| Qwen 2.5 | Alibaba Qwen 2.5 |
| DeepSeek R1 | Modèle de raisonnement robuste |
| Phi-4 | Microsoft Phi-4 |
| Gemma 3 | Google Gemma 3 |

Exécuter Ollama localement met l'outil entièrement hors ligne. Rien ne quitte votre machine.

______

## Humanisation de la lettre de motivation

Le générateur de lettre de motivation applique un guide de style délibéré pour éliminer les signes révélateurs du texte généré par IA :

- **Pas de tirets longs** — le signe révélateur IA le plus fort, supprimé entièrement
- **50+ mots et expressions interdits** : leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, etc.
- **Pas de markdown dans le corps de la lettre** — pas d'astérisques gras, de hashtags ou de points-virgules
- **Voix active par défaut** — passif uniquement quand l'acteur n'a genuinement pas d'importance
- **Contractions obligatoires** : "I've", "I'm", "it's"
- **Longueur de phrases variée** — phrases courtes et percutantes mélangées avec des plus longues
- **Pas d'ouvertures de remplissage** — "Il est important de noter que X" → dites simplement X
- **Détail concret de l'offre d'emploi au paragraphe 1** — prouve que la lettre n'a pas été générée depuis un modèle

*Le résultat se lit comme si un humain l'avait écrit, parce que les règles forcent le modèle à écrire comme un humain.*

______

## Options d'auto-hébergement

### Version hébergée (sans configuration)

Utilisez l'application en direct sur **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)** — pas de compte, pas d'inscription, pas de carte de crédit.

### Déploiement cloud en un clic

| Plateforme | Lien |
|----------|------|
| **Vercel** | Déploiement en un clic depuis le dépôt |
| **Cloudflare Pages** | Déploiement en un clic |
| **Netlify** | Déploiement en un clic |
| **GitHub Pages** | Fork → Paramètres → Pages → GitHub Actions → auto-déploiement |

### Développement local

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (recommandé pour les environnements reproductibles)

```bash
# Développement — rechargement à chaud sur http://localhost:5173
make docker-dev

# Production — nginx sur http://localhost:8080
make docker-prod

# Dev + Ollama ensemble (pile IA locale complète)
make docker-dev-with-ollama
```

### Pile Ollama entièrement hors ligne

```bash
# Démarrer le conteneur Ollama (modèles persistants entre les redémarrages)
make ollama

# Télécharger un modèle
make ollama-pull MODEL=llama3.2

# Démarrer l'application dev + Ollama côte à côte
make docker-dev-with-ollama
```

Ouvrez ensuite l'application, allez dans le panneau de clé API, sélectionnez **Ollama (Local)**, définissez l'URL sur `http://localhost:11434` et choisissez un modèle. Aucune donnée ne quitte votre machine.

______

## Questions fréquentes

### L'outil stocke-t-il mon CV ?

Non. L'application est entièrement côté client. Rien n'est persisté sur un serveur. Les données de session vivent en mémoire du navigateur et disparaissent quand vous fermez l'onglet.

### Mon CV a un score faible — dois-je paniquer ?

Les scores ATS sont directionnels, pas passe/échoue. Un score de 60 ne signifie pas qu'un ATS vous rejettera. Cela signifie qu'il y a des écarts mesurables entre votre CV et la description de poste analysée.

### Puis-je l'utiliser avec plusieurs descriptions de poste ?

Oui. Collez une nouvelle description de poste à tout moment. L'analyse de mots-clés et l'optimisation se relanceront par rapport à la nouvelle offre. Chaque analyse est indépendante.

### L'intégration Ollama est-elle vraiment hors ligne ?

Oui, si Ollama tourne sur votre machine locale ou sur une machine de votre réseau local. L'application envoie du texte à votre instance Ollama via HTTP. Rien ne va vers un service externe.

______

## Feuille de route du projet

Fonctionnalités en développement ou prévues :

- Historique des versions de CV via IndexedDB
- Optimiseur de profil LinkedIn
- Support du fournisseur Google Gemini
- Modèles Ollama supplémentaires

Le projet est sous licence MIT et accueille les pull requests. Ouvrez d'abord une issue pour les changements importants.

______

## Conclusion

**ATS Resume Improver** comble un vrai manque : un outil qui effectue une analyse sérieuse de CV sans courtiser vos données à quiconque. Le mode sans clé vous donne un retour immédiat et actionnable sur le format et la couverture des mots-clés. Ajouter une clé IA fait progresser l'analyse vers le raisonnement sémantique, la rédaction de lettre de motivation et la préparation aux entretiens — pour des centimes par analyse ou complètement gratuit avec Ollama.

La version hébergée en direct est sur **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**. Le code source complet est sur **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**.

______

## Références

1. [ATS Resume Improver — outil en direct](https://atsresumeimprover.netlify.app/)
2. [ATS Resume Improver — dépôt GitHub](https://github.com/simeononsecurity/ats-resume-improver)
3. [Conseils et astuces CV — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — Meilleur prompt IA pour humaniser l'écriture IA](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [Documentation API OpenAI](https://platform.openai.com/docs/)
6. [Documentation API Anthropic Claude](https://docs.anthropic.com/)
7. [Ollama — serveur LLM local](https://ollama.com/)
