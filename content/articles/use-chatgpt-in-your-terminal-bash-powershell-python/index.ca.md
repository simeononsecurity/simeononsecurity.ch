---
title: "Utilitzeu ChatGPT al vostre terminal (Bash, PowerShell, Python): una introducció a l'eina CLI de ChatGPT per a desenvolupadors"
date: 2023-02-07
toc: true
draft: false
description: "Apreneu a utilitzar el model ChatGPT d'OpenAI mitjançant la còmoda interfície de línia d'ordres (CLI) per generar text i respondre preguntes amb facilitat."
tags: ["ChatGPT", "OpenAI", "Interfície de línia d'ordres", "CLI", "generació de textos", "resposta a la pregunta", "conjunt d'eines per a desenvolupadors", "gestor de paquets pip", "Python 3.5", "PowerShell", "Bash"]
cover: "/img/cover/A_developer_sitting_at_their_computer_typing.png"
coverAlt: "Un desenvolupador assegut al seu ordinador, escrivint al seu teclat amb la CLI de ChatGPT oberta al seu terminal."
coverCaption: ""
---

El model **ChatGPT**, desenvolupat per OpenAI, **és un model de llenguatge d'avantguarda** capaç de generar text semblant a l'ésser humà. Per als desenvolupadors, la ChatGPT CLI (Command Line Interface) ofereix una manera còmoda d'interactuar amb el model ChatGPT mitjançant la línia d'ordres. Amb la CLI de ChatGPT, els desenvolupadors poden generar text, text complet o respondre preguntes sense esforç mitjançant les capacitats avançades del model.

La instal·lació de la CLI de ChatGPT és senzilla i només requereix que Python 3.5 o posterior estigui instal·lat a la màquina del desenvolupador. El gestor de paquets pip es pot utilitzar per instal·lar la CLI de ChatGPT executant l'ordre següent:

**Linux:**
```bash

pip install chatgpt requests readline

```

**Windows PowerShell**
```powershell

pip install chatgpt requests pyreadline3

```

Un cop instal·lats, els desenvolupadors poden utilitzar la CLI de ChatGPT per generar text o respondre preguntes amb facilitat. Per exemple, per generar text basat en un indicador, els desenvolupadors poden utilitzar l'ordre següent:

```bash
chatgpt generate --prompt "What is the purpose of existence?"
```

O, per respondre una pregunta:

```bash
chatgpt answer --question "What is the capital of France?"
```

La CLI de ChatGPT també es pot utilitzar amb scripts bàsics:

**Linux:**
```bash
prompt="What is the meaning of life?"
answer=$(chatgpt generate --prompt "$prompt")
echo "$answer"
```

**Windows PowerShell:**
```powershell
$prompt = "What is the meaning of life?"
$answer = chatgpt generate --prompt $prompt
Write-Host $answer
```

Aquest script produirà el text basat en la sol·licitud i mostrarà el text generat a la consola.

A més de la generació de text i la resposta de preguntes, la CLI de ChatGPT ofereix altres opcions, com ara especificar la longitud del text generat, ajustar la temperatura de la sortida i triar el nombre de respostes a generar.

La **ChatGPT CLI és una addició valuosa al conjunt d'eines de qualsevol desenvolupador**, proporcionant una manera senzilla i directa d'interactuar amb el model avançat de ChatGPT. Ja sigui per generar text per a un chatbot, completar text per a un editor de text o respondre preguntes per a un sistema de preguntes i respostes, la CLI de ChatGPT pot ajudar els desenvolupadors a assolir els seus objectius amb facilitat.