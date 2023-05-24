---
title: "Use ChatGPT em seu terminal (Bash, PowerShell, Python): uma introdução à ferramenta CLI ChatGPT para desenvolvedores"
date: 2023-02-07
toc: true
draft: false
description: "Aprenda a usar o modelo ChatGPT da OpenAI por meio da conveniente interface de linha de comando (CLI) para geração de texto e resposta a perguntas com facilidade."
tags: ["ChatGPT", "OpenAI", "Interface da Linha de comando", "CLI", "geração de texto", "pergunta respondendo", "kit de ferramentas do desenvolvedor", "gerenciador de pacotes pip", "Python 3.5", "PowerShell", "bash"]
cover: "/img/cover/A_developer_sitting_at_their_computer_typing.png"
coverAlt: "Um desenvolvedor sentado em seu computador, digitando em seu teclado com a CLI do ChatGPT aberta em seu terminal."
coverCaption: ""
---

O modelo **ChatGPT**, desenvolvido pela OpenAI, **é um modelo de linguagem de ponta** capaz de gerar texto semelhante ao humano. Para desenvolvedores, o ChatGPT CLI (Command Line Interface) fornece uma maneira conveniente de interagir com o modelo ChatGPT por meio da linha de comando. Com o ChatGPT CLI, os desenvolvedores podem facilmente gerar texto, texto completo ou responder a perguntas usando os recursos avançados do modelo.

A instalação do ChatGPT CLI é fácil e requer apenas o Python 3.5 ou posterior instalado na máquina do desenvolvedor. O gerenciador de pacotes pip pode ser utilizado para instalar o ChatGPT CLI executando o seguinte comando:

**Linux:**
```bash

pip install chatgpt requests readline

```

**Windows PowerShell**
```powershell

pip install chatgpt requests pyreadline3

```

Uma vez instalado, os desenvolvedores podem usar o ChatGPT CLI para gerar texto ou responder a perguntas com facilidade. Por exemplo, para gerar texto com base em um prompt, os desenvolvedores podem usar o seguinte comando:

```bash
chatgpt generate --prompt "What is the purpose of existence?"
```

Ou, para responder a uma pergunta:

```bash
chatgpt answer --question "What is the capital of France?"
```

A CLI do ChatGPT também pode ser utilizada com scripts básicos:

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

Este script produzirá o texto com base no prompt e exibirá o texto gerado no console.

Além da geração de texto e resposta a perguntas, o ChatGPT CLI oferece várias outras opções, como especificar o comprimento do texto gerado, ajustar a temperatura da saída e escolher o número de respostas a serem geradas.

O **ChatGPT CLI é uma adição valiosa ao kit de ferramentas de qualquer desenvolvedor**, fornecendo uma maneira simples e direta de interagir com o modelo avançado do ChatGPT. Seja gerando texto para um chatbot, completando texto para um editor de texto ou respondendo a perguntas para um sistema de perguntas e respostas, o ChatGPT CLI pode ajudar os desenvolvedores a atingir seus objetivos com facilidade.