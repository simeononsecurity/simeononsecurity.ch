---
title: "Optimizar imágenes con Python"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Optimiza imágenes con Python mediante redimensionamiento, compresión, conversión de formato y flujos de trabajo reproducibles con Pillow."
genre: ["Tecnología", "Desarrollo web", "Programación en Python", "Optimización de imágenes", "SEO", "Rendimiento web", "Experiencia de usuario", "Desarrollo de software", "Automatización", "Programación"]
tags: ["optimización de imágenes", "Python", "optimización de imágenes", "desarrollo web", "rendimiento del sitio", "experiencia de usuario", "compresión", "redimensionamiento", "conversión de formato", "procesamiento de imágenes", "biblioteca Pillow", "biblioteca Tinify", "automatización", "script de Python", "optimización del rendimiento web", "optimización SEO", "desarrollo de software", "diseño web", "compresión de imágenes", "reducción del tamaño de archivo", "carga diferida", "formatos de imagen", "formato WebP", "integración de API", "flujo de trabajo de desarrollo", "ejemplo de código", "técnicas de optimización de imágenes", "optimización del rendimiento", "tutorial de programación"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Ilustración de un script de Python que optimiza imágenes, con una lupa que muestra una imagen comprimida."
coverCaption: "Redimensiona, comprime y mejora imágenes con Python."
---

**Introducción**

El tamaño de las imágenes influye en la velocidad de un sitio web y en la experiencia de sus visitantes. Los archivos grandes pueden ralentizar la carga y hacer que la gente abandone la página. **Python** y la biblioteca Pillow permiten reducir el tamaño de las imágenes y mejorar su presentación en la web. Este artículo explica métodos y herramientas prácticas para **optimizar imágenes** con Python.

______

## Por qué importa optimizar las imágenes

**La optimización** reduce el tamaño de los archivos sin perjudicar de forma visible la calidad de las imágenes. Esto ofrece varias ventajas:

1. **Páginas que cargan más rápido**: Las imágenes grandes ralentizan el sitio y afectan al SEO y a la experiencia de usuario.

2. **Menos consumo de ancho de banda**: Las imágenes optimizadas transmiten menos datos, por lo que el sitio es más accesible con conexiones limitadas.

3. **Mejor experiencia móvil**: Las conexiones móviles suelen ser más lentas. Optimizar las imágenes ayuda a que las páginas se vean con fluidez en teléfonos y tabletas.

4. **Apoyo al SEO**: Los motores de búsqueda tienen en cuenta la velocidad del sitio al ordenar los resultados. Las páginas rápidas pueden obtener una mejor posición.

______

## Técnicas para optimizar imágenes

### **1. Comprimir imágenes**

La compresión reduce el tamaño del archivo. La biblioteca **Pillow** de Python ofrece algoritmos y ajustes sencillos para equilibrar el tamaño y la calidad de la imagen. Instala Pillow con pip:

```python
pip install Pillow
```

Este es un ejemplo de compresión:

```python
from PIL import Image

# Abre una imagen
image = Image.open("input_image.jpg")

# Comprime y guarda la imagen
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. Cambiar el tamaño de las imágenes**

Adapta las dimensiones de la imagen al espacio donde aparecerá en el sitio. Una imagen grande reducida con HTML o CSS aún puede ralentizar la página, ya que el navegador descarga el archivo completo. Pillow facilita el redimensionamiento:

```python
from PIL import Image

# Abre una imagen
image = Image.open("input_image.jpg")

# Cambia el tamaño de la imagen
resized_image = image.resize((800, 600))

# Guarda la imagen redimensionada
resized_image.save("resized_image.jpg")
```

### **3. Convertir el formato de imagen**

Convertir imágenes a formatos más eficientes, como WebP, reduce el tamaño del archivo y mantiene una calidad adecuada. La mayoría de los navegadores modernos admiten WebP. Pillow permite guardar imágenes en ese formato:

```python
from PIL import Image

# Abre una imagen
image = Image.open("input_image.jpg")

# Convierte la imagen al formato WebP
image.save("output_image.webp")
```

## Automatizar la optimización de imágenes con Python


### Ejemplo de script de Python: usar la API de TinyPNG

La automatización ahorra tiempo y trabajo cuando se procesan muchas imágenes. Las bibliotecas de Python permiten automatizar estas tareas. Tinify es un wrapper de Python para la API de TinyPNG.

Tinify comprime y optimiza imágenes con algoritmos avanzados para reducir el tamaño de los archivos sin perder calidad. Para usarlo, crea una cuenta en el sitio de Tinify y obtén una clave API.

Este ejemplo usa **Tinify** para comprimir una imagen:

```python
import tinify

# Configura Tinify con tu clave de API
tinify.key = "YOUR_API_KEY"

# Comprime la imagen
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Ejemplo de script de Python: optimizar imágenes de una carpeta

El siguiente script procesa imágenes de distintos tipos, como JPEG y PNG, y exporta versiones WebP optimizadas:

```python
import os
from PIL import Image

# Función para convertir una imagen al formato WebP
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# Función para recorrer las imágenes de una carpeta y convertirlas a WebP
def optimize_images(folder_path, output_folder, quality=85):
    # Crea la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)
    
    # Recorre cada archivo de la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Construye las rutas de entrada y salida
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # Convierte la imagen al formato WebP
            convert_to_webp(input_path, output_path, quality=quality)

# Ejemplo de uso
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

El ejemplo utiliza Python Imaging Library (PIL) para abrir las imágenes y convertirlas a WebP. La función `convert_to_webp` recibe la ruta de entrada, la ruta de salida y un parámetro opcional de calidad cuyo valor predeterminado es 85. `optimize_images` recorre los archivos de la carpeta, comprueba sus extensiones y llama a `convert_to_webp`. Las imágenes WebP optimizadas se guardan en la carpeta de salida indicada.

Ajusta `folder_path`, `output_folder` y `quality` según tus necesidades.

## Conclusión

La optimización de imágenes acelera los sitios web, mejora la experiencia de usuario y favorece el rendimiento en los resultados de búsqueda. El ecosistema de Python ofrece herramientas para comprimir y redimensionar imágenes, cambiar su formato y automatizar estas tareas. Pillow y Tinify procesan una imagen o un lote y mantienen una calidad visual adecuada. Elige primero las dimensiones y el nivel de calidad, y aplica esos ajustes a tu flujo de trabajo.


## Referencias
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
