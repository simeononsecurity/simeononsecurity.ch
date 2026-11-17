---
title: "Optimitzar imatges amb Python"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Optimitza imatges amb Python canviant-ne la mida, comprimint-les i convertint-ne el format amb processos reproduïbles de Pillow."
genre: ["Tecnologia", "Desenvolupament web", "Programació Python", "Optimització d’imatges", "SEO", "Rendiment web", "Experiència d’usuari", "Desenvolupament de programari", "Automatització", "Programació"]
tags: ["optimització d’imatges", "Python", "optimització d’imatge", "desenvolupament web", "rendiment del lloc web", "experiència d’usuari", "compressió", "canvi de mida", "conversió de format", "processament d’imatges", "biblioteca Pillow", "biblioteca Tinify", "automatització", "script Python", "optimització del rendiment web", "optimització SEO", "desenvolupament de programari", "disseny web", "compressió d’imatges", "reducció de la mida dels fitxers", "càrrega diferida", "formats d’imatge", "format WebP", "integració d’API", "flux de desenvolupament", "exemple de codi", "tècniques d’optimització d’imatges", "optimització del rendiment", "tutorial de programació"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Il·lustració d’un script Python que optimitza imatges, amb una lupa que mostra una imatge comprimida."
coverCaption: "Canvia la mida, comprimeix i millora imatges amb Python."
---

**Introducció**

La mida dels fitxers d’imatge influeix en la velocitat d’un lloc web i en l’experiència dels visitants. Els fitxers grans poden alentir la càrrega i fer que la gent abandoni la pàgina. **Python** i la biblioteca Pillow ajuden a reduir els fitxers i a millorar-ne la visualització al web. Aquest article presenta mètodes i eines pràctics per **optimitzar imatges** amb Python.

______

## Per què és important optimitzar les imatges

**L’optimització d’imatges** redueix la mida dels fitxers sense perjudicar de manera visible la qualitat. Té diversos avantatges:

1. **Les pàgines carreguen més de pressa**: els fitxers d’imatge grans alenteixen el lloc i afecten el SEO i l’experiència d’usuari.

2. **Es consumeix menys ample de banda**: les imatges optimitzades transfereixen menys dades i faciliten l’accés amb connexions limitades.

3. **Millor experiència mòbil**: les connexions mòbils sovint són més lentes. Optimitzar les imatges ajuda les pàgines a mostrar-se amb fluïdesa en telèfons i tauletes.

4. **Suport al SEO**: els cercadors tenen en compte la velocitat del lloc a l’hora de classificar-lo. Les pàgines ràpides poden ocupar millors posicions als resultats.

______

## Tècniques per optimitzar imatges

### **1. Comprimir imatges**

La compressió redueix la mida dels fitxers. La biblioteca **Pillow** de Python ofereix mètodes i opcions per equilibrar la mida i la qualitat de la imatge. Instal·la Pillow amb pip:

```python
pip install Pillow
```

Exemple per comprimir una imatge:

```python
from PIL import Image

# Obre una imatge
image = Image.open("input_image.jpg")

# Comprimeix i desa la imatge
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. Canviar la mida de les imatges**

Ajusta les dimensions de la imatge a l’espai on es mostrarà al lloc web. Encara que HTML o CSS redueixin una imatge gran, el lloc pot continuar carregant lentament perquè el navegador descarrega el fitxer complet. Pillow facilita el canvi de mida:

```python
from PIL import Image

# Obre una imatge
image = Image.open("input_image.jpg")

# Redimensiona la imatge
resized_image = image.resize((800, 600))

# Desa la imatge redimensionada
resized_image.save("resized_image.jpg")
```

### **3. Convertir el format de les imatges**

La conversió a formats més eficients, com WebP, pot reduir la mida del fitxer mantenint una qualitat adequada. La majoria dels navegadors moderns admeten WebP, i Pillow permet desar-hi imatges:

```python
from PIL import Image

# Obre una imatge
image = Image.open("input_image.jpg")

# Converteix la imatge al format WebP
image.save("output_image.webp")
```

## Automatitzar l’optimització d’imatges amb Python


### Exemple d’script Python: utilitzar l’API de TinyPNG

L’automatització estalvia temps i feina quan es processen moltes imatges. Les biblioteques Python permeten automatitzar aquestes tasques. Tinify és un wrapper de Python per a l’API de TinyPNG.

Tinify comprimeix i optimitza imatges amb algorismes avançats per reduir-ne la mida sense perdre qualitat. Per fer-lo servir, registra’t al lloc web de Tinify i obtén una clau API.

Exemple de compressió d’una imatge amb **Tinify**:

```python
import tinify

# Configura Tinify amb la teva clau d'API
tinify.key = "YOUR_API_KEY"

# Comprimeix la imatge
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Exemple d’script Python: optimitzar imatges d’una carpeta

L’script següent processa diversos tipus d’imatge, com JPEG i PNG, i exporta fitxers WebP optimitzats:

```python
import os
from PIL import Image

# Funció per convertir una imatge al format WebP
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# Funció per recórrer les imatges d'una carpeta i convertir-les a WebP
def optimize_images(folder_path, output_folder, quality=85):
    # Crea la carpeta de sortida si no existeix
    os.makedirs(output_folder, exist_ok=True)
    
    # Recorre cada fitxer de la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Construeix els camins d'entrada i sortida
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # Converteix la imatge al format WebP
            convert_to_webp(input_path, output_path, quality=quality)

# Exemple d'ús
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

L’exemple fa servir Python Imaging Library (PIL) per obrir imatges i convertir-les a WebP. La funció `convert_to_webp` rep el camí d’entrada, el camí de sortida i un paràmetre opcional de qualitat, amb valor per defecte 85. `optimize_images` recorre els fitxers de la carpeta, comprova les extensions admeses i crida `convert_to_webp`. Les imatges WebP optimitzades es desen a la carpeta de sortida indicada.

Adapta `folder_path`, `output_folder` i `quality` a les teves necessitats.

## Conclusió

L’optimització d’imatges accelera els llocs web, millora l’experiència d’usuari i afavoreix el rendiment als resultats de cerca. L’ecosistema Python ofereix eines per comprimir i redimensionar imatges, convertir formats i automatitzar aquestes tasques. Pillow i Tinify processen imatges individuals o lots i mantenen una qualitat visual adequada. Primer tria les dimensions i la qualitat, i després aplica aquests valors al teu flux de treball.


## Referències
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
