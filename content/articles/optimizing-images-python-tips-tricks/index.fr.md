---
title: "Optimiser des images avec Python"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Optimisez des images avec Python en les redimensionnant, en les compressant et en les convertissant avec des workflows Pillow reproductibles."
genre: ["Technologie", "Développement web", "Programmation Python", "Optimisation des images", "SEO", "Performances web", "Expérience utilisateur", "Développement logiciel", "Automatisation", "Programmation"]
tags: ["optimisation des images", "Python", "optimisation d’image", "développement web", "performances du site", "expérience utilisateur", "compression", "redimensionnement", "conversion de format", "traitement d’image", "bibliothèque Pillow", "bibliothèque Tinify", "automatisation", "script Python", "optimisation des performances web", "optimisation SEO", "développement logiciel", "conception web", "compression d’image", "réduction de taille de fichier", "chargement différé", "formats d’image", "format WebP", "intégration API", "workflow de développement", "exemple de code", "techniques d’optimisation d’image", "optimisation des performances", "tutoriel de programmation"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Illustration d’un script Python qui optimise des images, avec une loupe montrant une image compressée."
coverCaption: "Redimensionnez, compressez et améliorez des images avec Python."
---

**Introduction**

La taille des images influence la vitesse d’un site et l’expérience de ses visiteurs. Les fichiers volumineux peuvent ralentir le chargement et inciter les visiteurs à quitter la page. **Python** et sa bibliothèque Pillow permettent de réduire la taille des images et d’améliorer leur affichage sur le Web. Cet article présente des méthodes et des outils pratiques pour **optimiser les images** avec Python.

______

## Pourquoi optimiser les images

**L’optimisation** consiste à réduire la taille des fichiers sans dégrader visiblement les images. Elle présente plusieurs avantages :

1. **Chargement des pages plus rapide** : les images volumineuses ralentissent le site et nuisent au SEO et à l’expérience utilisateur.

2. **Moins de bande passante consommée** : les images optimisées utilisent moins de données, ce qui facilite l’accès au site avec une connexion limitée.

3. **Meilleure expérience mobile** : les connexions mobiles sont souvent plus lentes. L’optimisation aide les pages à s’afficher sans heurts sur les téléphones et les tablettes.

4. **Soutien au SEO** : les moteurs de recherche tiennent compte de la vitesse du site pour le classement. Les pages rapides peuvent obtenir de meilleurs résultats.

______

## Techniques d’optimisation des images

### **1. Compression des images**

La compression réduit la taille du fichier. La bibliothèque Python **Pillow** propose des méthodes et réglages simples qui permettent de trouver un équilibre entre taille du fichier et qualité de l’image. Installez Pillow avec pip :

```python
pip install Pillow
```

Voici un exemple de compression d’image :

```python
from PIL import Image

# Ouvrir une image
image = Image.open("input_image.jpg")

# Compresser et enregistrer l'image
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. Redimensionnement des images**

Adaptez les dimensions de l’image à l’espace où elle sera affichée. Une grande image réduite avec HTML ou CSS peut toujours ralentir le site, car le navigateur télécharge le fichier complet. Pillow simplifie le redimensionnement :

```python
from PIL import Image

# Ouvrir une image
image = Image.open("input_image.jpg")

# Redimensionner l'image
resized_image = image.resize((800, 600))

# Enregistrer l'image redimensionnée
resized_image.save("resized_image.jpg")
```

### **3. Conversion du format d’image**

La conversion vers un format plus efficace comme WebP réduit souvent la taille du fichier tout en conservant une bonne qualité. La plupart des navigateurs récents prennent WebP en charge, et Pillow sait enregistrer ce format :

```python
from PIL import Image

# Ouvrir une image
image = Image.open("input_image.jpg")

# Convertir l'image au format WebP
image.save("output_image.webp")
```

## Automatiser l’optimisation des images avec Python


### Exemple de script Python : utiliser l’API TinyPNG

L’automatisation fait gagner du temps, surtout lorsqu’il faut traiter de nombreuses images. Plusieurs bibliothèques Python permettent d’automatiser ces tâches. Tinify est un wrapper Python de l’API TinyPNG.

Tinify compresse et optimise les images avec des algorithmes avancés afin de réduire leur taille sans sacrifier leur qualité. Pour l’utiliser, créez un compte sur le site Tinify et obtenez une clé API.

Voici un exemple d’utilisation de **Tinify** pour compresser une image :

```python
import tinify

# Configurer Tinify avec votre clé API
tinify.key = "YOUR_API_KEY"

# Compresser l'image
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Exemple de script Python : optimiser les images d’un dossier

Le script suivant parcourt des images de différents types, comme JPEG et PNG, puis exporte des versions WebP optimisées :

```python
import os
from PIL import Image

# Fonction pour convertir une image au format WebP
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# Fonction pour parcourir les images d'un dossier et les convertir en WebP
def optimize_images(folder_path, output_folder, quality=85):
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_folder, exist_ok=True)
    
    # Parcourir chaque fichier du dossier
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Construire les chemins d'entrée et de sortie
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # Convertir l'image au format WebP
            convert_to_webp(input_path, output_path, quality=quality)

# Exemple d'utilisation
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

Cet exemple utilise la Python Imaging Library (PIL) pour ouvrir les images et les convertir en WebP. La fonction `convert_to_webp` reçoit le chemin de l’image d’entrée, le chemin de sortie et un paramètre de qualité facultatif, dont la valeur par défaut est 85. La fonction `optimize_images` parcourt les fichiers du dossier, vérifie leur extension, puis appelle `convert_to_webp`. Les images WebP optimisées sont enregistrées dans le dossier de sortie indiqué.

Adaptez les valeurs de `folder_path`, `output_folder` et `quality` à vos besoins.

## Conclusion

L’optimisation des images accélère les sites, améliore l’expérience utilisateur et soutient les performances dans les résultats de recherche. L’écosystème Python fournit des outils pour compresser les images, les redimensionner, convertir leur format et automatiser ces opérations. Pillow et Tinify traitent une image ou un lot d’images tout en conservant une qualité visuelle adaptée. Choisissez d’abord les dimensions et le niveau de qualité, puis appliquez les mêmes réglages à votre workflow.


## Références
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
