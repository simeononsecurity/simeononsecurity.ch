---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Aprenda a gerar um código de convite e ingressar na plataforma online HackTheBox para testar e aprimorar suas habilidades em testes de penetração e segurança cibernética no Windows e no Linux."
tags: ["HackTheBox", "Desafio de convite", "Teste de penetração", "Cíber segurança", "janelas", "Linux", "Plataforma Online", "POST HTTP", "Código de convite", "Base64 codificado", "Powershell", "Linux Bash", "Decodificação Base64", "Geração de código de convite", "Programação", "Desenvolvimento web", "Tecnologia", "Segurança de TI", "Treinamento de TI"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Uma tela de desenho animado mostrando o site do HackTheBox com uma porta do cofre sendo destrancada com uma chave, revelando um troféu ou medalha, com um fundo de paisagem urbana no esquema de cores do logotipo do HackTheBox (azul e branco)."
coverCaption: ""
---
 instruções passo a passo para concluir o desafio de convite HackTheBox no Windows ou Linux. Aprenda a gerar um código de convite e ingressar na plataforma online para testar e aprimorar suas habilidades em testes de penetração e segurança cibernética. O artigo apresenta soluções simples e avançadas, facilitando para usuários de todos os níveis concluir o desafio e obter acesso à plataforma.

______

## O que é Hack the Box?

HackTheBox é uma plataforma online para testar e aprimorar suas habilidades em testes de penetração e segurança cibernética.

## Como você entra no Hack the box ?

Para criar uma conta no HackTheBox (HTB), você deve completar o desafio do convite ou hackear a si mesmo. Não se preocupe, embora não seja difícil e este artigo o ajudará a concluir o desafio.

Primeiro, vá para o [HackTheBox Website](https://hackthebox.eu) e clique no botão juntar.

Você será presenteado com uma caixa pedindo claramente um código de convite.

Você pode ver claramente uma caixa de texto solicitando um código de convite.

Pressione ***"F12"*** no teclado ou ***"Ctrl + Shift + I"*** para abrir as ferramentas de desenvolvedor do navegador.

Na guia "Elementos", você encontrará um script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Revendo o javascript e a função makeInviteCode, você descobrirá que precisa enviar um **HTTP POST** para **/api/invite/generate** para obter um código de convite.

Você pode fazer o seguinte para obter o código de convite codificado em Base64:

### Solução:

#### Simples:
- **Janelas**: ```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Que irá gerar o seguinte conteúdo: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

Se você pegar o código de convite codificado para [base64decode.org](https://www.base64decode.org/) você receberá seu código de convite!

#### Avançado (Imprima instantaneamente o código de convite):
 - **Janelas**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Nota**: Você precisará instalar o [jq](https://stedolan.github.io/jq/download/) pacote.

______

### Código de convite Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


