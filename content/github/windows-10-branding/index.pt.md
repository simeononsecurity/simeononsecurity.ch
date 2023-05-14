---
title: "Branding automatizado para sistemas Windows - controle facilmente a área de trabalho, a tela de bloqueio e muito mais"
date: 2020-08-14
---


Muitas organizações precisam ou desejam controlar a marca de um sistema Windows.
Isso inclui o papel de parede da área de trabalho, o avatar do usuário, a tela de bloqueio do Windows e, às vezes, o logotipo do OEM.
No Windows 10, Windows Server 2016 e Windows Server 2019, isso não é particularmente fácil.
Mas, com o auxílio do script vinculado, podemos automatizá-lo parcialmente e tornar o processo muito mais fácil.

## Baixe os arquivos necessários

**Baixe os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Como configurar os arquivos de marca

- [X] Substitua todas as imagens pelas imagens de sua marca
  - [X] logotipo OEM deve ser 95x95 ou 120x20 e no formato ".bmp"
  - [X] Gere a imagem do usuário junto com as variantes 32x32, 40x40, 48x48, 192x192.
  - [X] Gera ou copia a imagem do usuário para a imagem do convidado.

## Como executar o script
```
.\sos-copybranding.ps1
```

## Este script utiliza a seguinte ferramenta:

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
