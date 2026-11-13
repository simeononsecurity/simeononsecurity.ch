---
title: "Ottimizzare le immagini con Python"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Ottimizza le immagini con Python ridimensionandole, comprimendole e convertendole con flussi di lavoro Pillow ripetibili."
genre: ["Tecnologia", "Sviluppo web", "Programmazione Python", "Ottimizzazione delle immagini", "SEO", "Prestazioni web", "Esperienza utente", "Sviluppo software", "Automazione", "Programmazione"]
tags: ["ottimizzazione delle immagini", "Python", "ottimizzazione immagini", "sviluppo web", "prestazioni del sito", "esperienza utente", "compressione", "ridimensionamento", "conversione formato", "elaborazione immagini", "libreria Pillow", "libreria Tinify", "automazione", "script Python", "ottimizzazione prestazioni web", "ottimizzazione SEO", "sviluppo software", "web design", "compressione immagini", "riduzione dimensione file", "caricamento differito", "formati immagine", "formato WebP", "integrazione API", "flusso di sviluppo", "esempio di codice", "tecniche di ottimizzazione immagini", "ottimizzazione prestazioni", "tutorial di programmazione"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Illustrazione di uno script Python che ottimizza immagini, con una lente che mostra un’immagine compressa."
coverCaption: "Ridimensiona, comprimi e migliora le immagini con Python."
---

**Introduzione**

La dimensione delle immagini influisce sulla velocità di un sito e sull’esperienza dei visitatori. I file grandi possono rallentare il caricamento e spingere le persone ad abbandonare la pagina. **Python** e la libreria Pillow aiutano a ridurre le dimensioni dei file e a migliorare la visualizzazione sul Web. Questo articolo presenta metodi e strumenti pratici per **ottimizzare le immagini** con Python.

______

## Perché l’ottimizzazione delle immagini è importante

**Ottimizzare un’immagine** significa ridurne il file senza compromettere in modo visibile la qualità. I vantaggi includono:

1. **Pagine più veloci**: i file immagine grandi rallentano il sito e incidono su SEO ed esperienza utente.

2. **Meno larghezza di banda**: le immagini ottimizzate trasferiscono meno dati e facilitano l’accesso con connessioni limitate.

3. **Migliore esperienza mobile**: le connessioni mobili spesso sono più lente. Immagini ottimizzate aiutano le pagine a caricarsi senza intoppi su telefoni e tablet.

4. **Supporto alla SEO**: i motori di ricerca considerano la velocità del sito nel posizionamento. Le pagine rapide possono ottenere una posizione migliore.

______

## Tecniche di ottimizzazione delle immagini

### **1. Compressione delle immagini**

La compressione riduce le dimensioni del file. **Pillow**, una libreria Python, offre metodi e impostazioni semplici per bilanciare dimensioni e qualità. Installa Pillow con pip:

```python
pip install Pillow
```

Ecco un esempio di compressione:

```python
from PIL import Image

# Apri un'immagine
image = Image.open("input_image.jpg")

# Comprimi e salva l'immagine
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. Ridimensionamento delle immagini**

Adatta le dimensioni dell’immagine allo spazio in cui apparirà sul sito. Anche se HTML o CSS riducono un’immagine grande, il browser scarica comunque il file completo e la pagina può rallentare. Pillow semplifica il ridimensionamento:

```python
from PIL import Image

# Apri un'immagine
image = Image.open("input_image.jpg")

# Ridimensiona l'immagine
resized_image = image.resize((800, 600))

# Salva l'immagine ridimensionata
resized_image.save("resized_image.jpg")
```

### **3. Conversione del formato immagine**

Convertire le immagini in formati più efficienti come WebP riduce spesso le dimensioni mantenendo una buona qualità. La maggior parte dei browser moderni supporta WebP. Pillow permette di salvare le immagini in questo formato:

```python
from PIL import Image

# Apri un'immagine
image = Image.open("input_image.jpg")

# Converti l'immagine nel formato WebP
image.save("output_image.webp")
```

## Automatizzare l’ottimizzazione delle immagini con Python


### Esempio di script Python: usare l’API TinyPNG

L’automazione riduce tempo e lavoro quando si elaborano molte immagini. Le librerie Python permettono di automatizzare queste operazioni. Tinify è un wrapper Python per l’API TinyPNG.

Tinify comprime e ottimizza le immagini con algoritmi avanzati, riducendo le dimensioni dei file e mantenendo la qualità. Per usarlo, crea un account sul sito Tinify e richiedi una chiave API.

Ecco come usare **Tinify** per comprimere un’immagine:

```python
import tinify

# Configura Tinify con la tua chiave API
tinify.key = "YOUR_API_KEY"

# Comprimi l'immagine
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Esempio di script Python: ottimizzare le immagini in una cartella

Lo script seguente elabora immagini di vari tipi, come JPEG e PNG, e salva versioni WebP ottimizzate:

```python
import os
from PIL import Image

# Funzione per convertire un'immagine nel formato WebP
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# Funzione per scorrere le immagini di una cartella e convertirle in WebP
def optimize_images(folder_path, output_folder, quality=85):
    # Crea la cartella di output se non esiste
    os.makedirs(output_folder, exist_ok=True)
    
    # Scorri ogni file nella cartella
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Crea i percorsi di input e output
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # Converti l'immagine nel formato WebP
            convert_to_webp(input_path, output_path, quality=quality)

# Esempio d'uso
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

L’esempio usa Python Imaging Library (PIL) per aprire le immagini e convertirle in WebP. La funzione `convert_to_webp` riceve il percorso di input, il percorso di output e un parametro di qualità facoltativo, con valore predefinito 85. `optimize_images` scorre i file della cartella, controlla le estensioni valide e chiama `convert_to_webp`. Le immagini WebP ottimizzate vengono salvate nella cartella di output indicata.

Adatta `folder_path`, `output_folder` e `quality` alle tue esigenze.

## Conclusione

L’ottimizzazione delle immagini velocizza i siti, migliora l’esperienza utente e sostiene le prestazioni nei risultati di ricerca. L’ecosistema Python offre strumenti per comprimere e ridimensionare immagini, convertirne il formato e automatizzare queste operazioni. Pillow e Tinify elaborano una singola immagine o un gruppo di file mantenendo una qualità visiva adeguata. Scegli prima le dimensioni e il livello di qualità, poi applica le stesse impostazioni al tuo flusso di lavoro.


## Riferimenti
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
