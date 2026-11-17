---
title: "Otimizar imagens com Python"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Otimize imagens com Python por meio de redimensionamento, compressão, conversão de formato e fluxos de trabalho repetíveis com Pillow."
genre: ["Tecnologia", "Desenvolvimento web", "Programação Python", "Otimização de imagens", "SEO", "Desempenho web", "Experiência do usuário", "Desenvolvimento de software", "Automação", "Programação"]
tags: ["otimização de imagens", "Python", "otimização de imagem", "desenvolvimento web", "desempenho do site", "experiência do usuário", "compressão", "redimensionamento", "conversão de formato", "processamento de imagem", "biblioteca Pillow", "biblioteca Tinify", "automação", "script Python", "otimização de desempenho web", "otimização SEO", "desenvolvimento de software", "web design", "compressão de imagem", "redução do tamanho do arquivo", "carregamento lento", "formatos de imagem", "formato WebP", "integração de API", "fluxo de desenvolvimento", "exemplo de código", "técnicas de otimização de imagem", "otimização de desempenho", "tutorial de programação"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Ilustração de um script Python otimizando imagens, com uma lupa que mostra uma imagem comprimida."
coverCaption: "Redimensione, comprima e melhore imagens com Python."
---

**Introdução**

O tamanho das imagens afeta a velocidade de um site e a experiência dos visitantes. Arquivos grandes podem atrasar o carregamento e levar as pessoas a sair da página. **Python** e a biblioteca Pillow ajudam a reduzir os arquivos e melhorar a exibição na web. Este artigo apresenta métodos e ferramentas práticos para **otimizar imagens** com Python.

______

## Por que otimizar imagens

**A otimização** reduz o tamanho dos arquivos sem prejudicar de forma perceptível a qualidade visual. Isso traz vários benefícios:

1. **Páginas carregam mais rápido**: arquivos de imagem grandes deixam o site lento e afetam o SEO e a experiência do usuário.

2. **Menos largura de banda**: imagens otimizadas transferem menos dados, o que facilita o acesso ao site em conexões limitadas.

3. **Melhor experiência em dispositivos móveis**: conexões móveis costumam ser mais lentas. A otimização ajuda as páginas a carregar bem em celulares e tablets.

4. **Apoio ao SEO**: mecanismos de busca consideram a velocidade do site na classificação. Páginas rápidas podem alcançar posições melhores nos resultados.

______

## Técnicas de otimização de imagens

### **1. Comprimir imagens**

A compressão reduz o tamanho do arquivo. A biblioteca **Pillow** para Python oferece vários métodos e configurações para equilibrar tamanho e qualidade da imagem. Instale Pillow com pip:

```python
pip install Pillow
```

Exemplo de compressão de imagem:

```python
from PIL import Image

# Abra uma imagem
image = Image.open("input_image.jpg")

# Compacte e salve a imagem
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. Redimensionar imagens**

Ajuste as dimensões da imagem ao espaço em que ela aparecerá no site. Uma imagem grande reduzida com HTML ou CSS ainda pode deixar o site lento, pois o navegador baixa o arquivo completo. Pillow facilita o redimensionamento:

```python
from PIL import Image

# Abra uma imagem
image = Image.open("input_image.jpg")

# Redimensione a imagem
resized_image = image.resize((800, 600))

# Salve a imagem redimensionada
resized_image.save("resized_image.jpg")
```

### **3. Converter o formato da imagem**

Converter para formatos mais eficientes, como WebP, reduz o arquivo e mantém uma qualidade adequada. A maioria dos navegadores modernos oferece suporte a WebP. Pillow permite salvar imagens nesse formato:

```python
from PIL import Image

# Abra uma imagem
image = Image.open("input_image.jpg")

# Converta a imagem para o formato WebP
image.save("output_image.webp")
```

## Automatizar a otimização de imagens com Python


### Exemplo de script Python: usar a API TinyPNG

A automação economiza tempo e trabalho ao processar muitas imagens. As bibliotecas Python permitem automatizar essas tarefas. Tinify é um wrapper Python para a API TinyPNG.

Tinify comprime e otimiza imagens com algoritmos avançados, reduzindo o tamanho dos arquivos sem prejudicar a qualidade. Para usar a ferramenta, crie uma conta no site da Tinify e obtenha uma chave de API.

Veja como usar **Tinify** para comprimir uma imagem:

```python
import tinify

# Configure o Tinify com sua chave de API
tinify.key = "YOUR_API_KEY"

# Compacte a imagem
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Exemplo de script Python: otimizar imagens em uma pasta

O script a seguir processa vários tipos de imagem, como JPEG e PNG, e exporta arquivos WebP otimizados:

```python
import os
from PIL import Image

# Função para converter uma imagem para o formato WebP
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# Função para percorrer as imagens de uma pasta e convertê-las para WebP
def optimize_images(folder_path, output_folder, quality=85):
    # Crie a pasta de saída se ela não existir
    os.makedirs(output_folder, exist_ok=True)
    
    # Percorra cada arquivo da pasta
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Monte os caminhos de entrada e saída
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # Converta a imagem para o formato WebP
            convert_to_webp(input_path, output_path, quality=quality)

# Exemplo de uso
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

O exemplo usa Python Imaging Library (PIL) para abrir imagens e convertê-las para WebP. A função `convert_to_webp` recebe o caminho do arquivo de entrada, o caminho de saída e um parâmetro opcional de qualidade, cujo valor padrão é 85. `optimize_images` percorre os arquivos da pasta, verifica as extensões válidas e chama `convert_to_webp`. As imagens WebP otimizadas são salvas na pasta de saída indicada.

Ajuste `folder_path`, `output_folder` e `quality` conforme sua necessidade.

## Conclusão

A otimização de imagens acelera sites, melhora a experiência do usuário e ajuda no desempenho dos resultados de busca. O ecossistema Python oferece ferramentas para comprimir e redimensionar imagens, converter formatos e automatizar essas tarefas. Pillow e Tinify processam uma imagem ou um conjunto delas e mantêm uma qualidade visual adequada. Primeiro escolha as dimensões e a qualidade, depois aplique as mesmas configurações ao seu fluxo de trabalho.


## Referências
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
