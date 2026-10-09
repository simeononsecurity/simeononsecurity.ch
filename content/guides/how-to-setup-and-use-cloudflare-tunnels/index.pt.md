---
title: "Configurando Túneis Cloudflare"
draft: false
toc: true
date: 2023-05-26
description: Aprenda como configurar Túneis Cloudflare para simplificar e proteger o tráfego da sua rede, melhorando o desempenho e a segurança.
tags:
- Túneis Cloudflare
- Segurança de Rede
- Desempenho de Website
- Servidor Proxy
- Tráfego Web
- Configuração de Rede
- Servidor Ubuntu
- Conta Cloudflare
- Autenticação
- Criação de Túnel
- Roteamento de Tráfego
- Registros DNS
- Conexão Segura
- Hospedagem de Website
- Serviço Proxy
- Proteção de Rede
- Otimização de Desempenho
- Integração Cloudflare
- Configuração do Servidor
- Criptografia de Tráfego
- Gerenciamento de Tráfego de Rede
- Hospedagem Web Segura
- Segurança de Website
- Configuração Ubuntu
- Tecnologia de Tunelamento
- Serviços Cloudflare
- Desempenho de Rede
- Segurança Web
- Segurança do Servidor
- Gerenciamento de Tráfego
- Proxy Cloudflare
cover: /img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.webp
coverAlt: Uma ilustração mostrando um túnel de rede conectando um servidor local ao logo da Cloudflare, simbolizando o tráfego de rede seguro e simplificado.
coverCaption: ''
lastmod: 2026-10-08
---

**Um Guia para Configurar Túneis Cloudflare**

## Introdução
Os Túneis Cloudflare fornecem uma forma segura de hospedar websites estabelecendo uma conexão direta entre sua rede local e a Cloudflare. Este guia irá orientá-lo no processo de configuração dos Túneis Cloudflare para melhorar a segurança e o desempenho do seu website.

______

## Por que usar Túneis Cloudflare?
Os Túneis Cloudflare oferecem vários benefícios, incluindo a redução de vetores de ataque e a simplificação das configurações de rede. Ao usar a Cloudflare como proxy, você pode fechar portas externas e garantir que todo o tráfego passe pela rede segura da Cloudflare. Isso fornece uma camada adicional de proteção para seu website.

______

## Pré-requisitos
Antes de configurar os Túneis Cloudflare, certifique-se de ter o seguinte:

1. Uma conta Cloudflare ativa.
2. Um servidor rodando Ubuntu.

______

## Passo 1: Instalação
Para começar, você precisa instalar o pacote dos Túneis Cloudflare no seu servidor Ubuntu. Siga estes passos:

1. Abra o terminal no seu servidor Ubuntu.
2. Baixe a versão mais recente do pacote dos Túneis Cloudflare executando o seguinte comando:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Passo 2: Autenticação
Em seguida, você precisa autenticar sua conta Cloudflare com o serviço dos Túneis Cloudflare. Siga estes passos:

1. Execute o seguinte comando no terminal:

```shell
cloudflared tunnel login
```

2. Clique no site que deseja usar com seu túnel para completar o processo de autenticação.

## Passo 3: Criando um Túnel

Agora é hora de criar seu Túnel Cloudflare. Siga estes passos:

1. Execute o seguinte comando no terminal para criar um túnel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Escolha um nome para seu túnel que seja memorável e descritivo. Note que o nome do túnel não pode ser alterado depois.

3. Após criar o túnel, você receberá informações importantes, incluindo o UUID do seu túnel. Anote este UUID pois será necessário para configurações futuras.

4. Para ver uma lista de todos os túneis ativos, use o comando:

```shell
cloudflared tunnel list
```

Isso exibirá os nomes e UUIDs dos seus túneis.

### Passo 4: Configurando o Túnel

Para configurar seu túnel e começar a rotear o tráfego, siga estes passos:

1. Navegue até o diretório dos Túneis Cloudflare no seu servidor. O local padrão é `/etc/cloudflared`.

2. Dentro deste diretório, crie um novo arquivo chamado `config.yml` usando um editor de texto de sua preferência.

3. Preencha o arquivo config.yml com o seguinte conteúdo:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Certifique-se de substituir `<your_tunnels_uuid>` pelo UUID do seu túnel e atualize o caminho para o arquivo de credenciais se necessário.

## Passo 5: Roteando o Tráfego

Para especificar os serviços internos que deseja servir através do seu túnel, siga estes passos:

1. Abra novamente o arquivo `Open the `config.yml`.

2. Adicione os parâmetros ingress ao arquivo para definir os serviços que deseja rotear pela Cloudflare. Por exemplo:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Substitua `<your_tunnels_uuid>` pelo UUID do seu túnel e atualize o hostname e os detalhes do serviço conforme sua configuração.

3. Salve o arquivo config.yml.


## Passo 6: Criando Registros DNS

Para criar registros DNS para o hostname e serviços do seu túnel, siga estes passos:

1. Abra o terminal.

2. Use o seguinte comando para criar um registro DNS:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Substitua `<UUID or NAME of tunnel>` pelo UUID ou nome do seu túnel, e `<hostname>` pelo hostname desejado para seu serviço.

3. Por exemplo, para criar um registro DNS para example.com, execute o comando:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Observe que as alterações serão refletidas na seção DNS do seu painel Cloudflare.

## Passo 7: Iniciando o Túnel

Para testar e iniciar seu Túnel Cloudflare, siga estes passos:

1. Abra o terminal.

2. Execute o seguinte comando para iniciar o túnel:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Substitua `<UUID or NAME of tunnel>` pelo UUID ou nome do seu túnel.

3. O Cloudflared agora configurará seu túnel e exibirá informações sobre seu status. Uma vez que o túnel esteja ativo e funcionando, você pode prosseguir para o próximo passo.

4. Para evitar que o túnel feche quando você sair do terminal, você precisa executar o Cloudflared como um serviço systemd. Use o seguinte comando:

```shell
cloudflared --config /path/to/config.yml service install
```

Substitua `/path/to/config.yml` pelo caminho para seu arquivo `config.yml`.

## Conclusão

Neste guia, cobrimos os passos para configurar Túneis Cloudflare no Ubuntu. Seguindo estas instruções, você pode melhorar a segurança e o desempenho do seu website usando a rede da Cloudflare. Lembre-se de monitorar regularmente seus túneis e ajustar a configuração conforme necessário.

Se você encontrar algum problema ou precisar de mais assistência, consulte a [documentação oficial dos Túneis Cloudflare](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/).


## Referências
- [Documentação dos Túneis Cloudflare](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Repositório GitHub dos Túneis Cloudflare](https://github.com/cloudflare/cloudflared)
- [tcude - Como Configurar Túneis Cloudflare no Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)
