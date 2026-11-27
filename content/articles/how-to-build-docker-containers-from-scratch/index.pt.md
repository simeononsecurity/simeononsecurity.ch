---
title: "Criando contêineres Docker eficientes e seguros"
date: 2023-02-24
lastmod: 2026-11-27
toc: true
draft: false
description: "Aprenda a criar contêineres Docker eficientes e seguros com boas práticas, dicas e instruções passo a passo neste guia abrangente."
tags: ["Docker", "contêineres", "conteinerização", "DevOps", "implantação", "portabilidade", "eficiência", "segurança", "boas práticas", "Dockerfile", "imagens-base", "variáveis de ambiente", "montagens de volume", "usuário root", "imagens atualizadas", "desenvolvimento de software", "imagens de contêiner", "Docker Hub", "orquestração de contêineres", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.webp"
coverAlt: "Imagem animada em 3D de um contêiner seguro e bem organizado com o logotipo do Docker, cercado por várias ferramentas e equipamentos relacionados à engenharia de software e ao DevOps."
coverCaption: ""
---

**Como criar contêineres Docker**

Docker é uma ferramenta poderosa que permite criar aplicações portáveis e fáceis de implantar. Neste guia, vamos abordar as etapas básicas para criar e compilar contêineres Docker. Também veremos boas práticas e dicas para manter seus contêineres Docker eficientes, seguros e fáceis de usar.

## Entendendo o Docker

Antes de começar a criar contêineres Docker, é importante entender o que é o Docker e como ele funciona.

Docker é uma ferramenta que permite empacotar uma aplicação e suas dependências em um contêiner que pode ser executado em qualquer sistema. O contêiner fica isolado do sistema hospedeiro e inclui tudo o que a aplicação precisa para funcionar, como código, ambiente de execução, ferramentas do sistema, bibliotecas e configurações.

Os contêineres são leves e fáceis de implantar, por isso são uma opção popular para criar e implantar aplicações. Com o Docker, você pode criar, gerenciar e executar contêineres por meio de uma interface de linha de comando simples.

## Criando uma imagem Docker

Para criar um contêiner Docker, primeiro é preciso criar uma imagem Docker. Uma imagem Docker é uma captura de um contêiner que inclui todos os arquivos, bibliotecas e dependências necessários para executar a aplicação.

Estas são as etapas básicas para criar uma imagem Docker:

1. **Criar um Dockerfile**
2. **Compilar a imagem**
3. **Executar o contêiner**

### Etapa 1: Criar um Dockerfile

A primeira etapa para criar uma imagem Docker é criar um Dockerfile. Um Dockerfile é um arquivo de texto que contém as instruções necessárias para compilar a imagem. Veja um exemplo simples de Dockerfile:

```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Vamos explicar este Dockerfile:

- `FROM ubuntu:latest` especifica a imagem-base do contêiner. Neste caso, estamos usando a versão mais recente do Ubuntu.
- `RUN apt-get update && apt-get install -y nginx` atualiza a lista de pacotes e instala o servidor web nginx.
- `COPY index.html /var/www/html/` copia o arquivo index.html para a raiz web do contêiner.
- `EXPOSE 80` expõe a porta 80 para o sistema hospedeiro.
- `CMD ["nginx", "-g", "daemon off;"]` inicia o servidor nginx e o mantém em primeiro plano.

### Etapa 2: Compilar a imagem

Depois de criar o Dockerfile, você pode compilar a imagem usando o comando `docker build`. Veja um exemplo:

```bash
docker run -d -p 80:80 my-nginx-image
```

Vamos explicar este comando:

- `docker run` diz ao Docker para executar um contêiner.
- `-d` executa o contêiner em modo desacoplado, ou seja, em segundo plano.
- `-p 80:80` mapeia a porta 80 do sistema hospedeiro para a porta 80 do contêiner.
- `my-nginx-image` especifica o nome da imagem Docker que será usada pelo contêiner.

## Boas práticas

Agora que você sabe como criar contêineres Docker, vamos ver algumas boas práticas para mantê-los eficientes, seguros e fáceis de usar.

### Use imagens-base pequenas

Para manter seus contêineres Docker pequenos e rápidos de implantar, prefira imagens-base pequenas que contenham somente as dependências necessárias para a aplicação. Por exemplo, em vez de usar um sistema operacional completo, como Ubuntu ou CentOS, você pode usar uma imagem menor, como Alpine Linux ou BusyBox.

### Minimize as camadas

Cada linha do Dockerfile cria uma nova camada na imagem Docker, e cada camada aumenta o tamanho da imagem. Para manter suas imagens Docker tão pequenas quanto possível, tente reduzir o número de camadas. Uma maneira de fazer isso é agrupar comandos semelhantes em uma única linha do Dockerfile. Por exemplo, em vez de usar dois comandos `RUN` separados para atualizar a lista de pacotes e instalar um pacote, você pode usar um único comando `RUN` para fazer as duas coisas ao mesmo tempo.

Exemplo:
```dockerfile
RUN apt update
RUN apt install apache -y
```
em vez de
```dockerfile
RUN apt update && apt install apache -y
```

### Use variáveis de ambiente

Usar variáveis de ambiente no Dockerfile em vez de valores fixos facilita a personalização do contêiner em tempo de execução e mantém o Dockerfile portável. Por exemplo, você pode usar variáveis de ambiente para especificar a porta em que a aplicação será executada ou o local de um arquivo de configuração.

Exemplo:
```bash
docker run -e PORT=3000 my-app
```
```Dockerfile
FROM node:14

# Define o diretório de trabalho
WORKDIR /app

# Copia package.json e yarn.lock para o contêiner
COPY package.json yarn.lock ./

# Instala as dependências
RUN yarn install --frozen-lockfile

# Copia o código da aplicação para o contêiner
COPY . .

# Expõe a porta da aplicação
EXPOSE $PORT

# Inicia a aplicação
CMD ["yarn", "start"]
```


### Use montagens de volume

As montagens de volume permitem compartilhar dados entre o sistema hospedeiro e o contêiner Docker. Isso facilita o gerenciamento dos dados e reduz o tamanho do contêiner Docker. Por exemplo, você pode montar um volume para compartilhar um arquivo de banco de dados entre o sistema hospedeiro e o contêiner.

Exemplo:
```bash
docker run -v /home/user/app/data:/app/data my-app
```

```Dockerfile
FROM node:14

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos package.json e yarn.lock para o contêiner
COPY package.json yarn.lock ./

# Instala as dependências
RUN yarn install --frozen-lockfile

# Copia o restante do código da aplicação para o contêiner
COPY . .

# Expõe a porta da aplicação
EXPOSE 3000

# Inicia a aplicação
CMD ["yarn", "start"]

# Monta um volume para os dados da aplicação
VOLUME ["/app/data"]
```

### Evite executar como root

Executar o contêiner Docker como usuário root pode representar um risco de segurança. Em vez disso, crie um novo usuário no Dockerfile e execute o contêiner com esse usuário. Por exemplo, você pode usar o comando `USER` no Dockerfile para criar um novo usuário e depois mudar para ele ao executar o contêiner.

Exemplo:
```Dockerfile
FROM node:14

# Cria um novo usuário para executar o contêiner
RUN useradd --user-group --create-home --shell /bin/false app

# Muda o diretório de trabalho para o diretório pessoal do usuário app
WORKDIR /home/app

# Instala as dependências como usuário app
COPY package.json yarn.lock ./
RUN chown -R app:app /home/app
USER app
RUN yarn install --frozen-lockfile --production

# Copia o código da aplicação como usuário app
COPY --chown=app:app . .

# Expõe a porta
EXPOSE 3000

# Inicia a aplicação como usuário app
CMD ["yarn", "start"]
```

### Mantenha as imagens atualizadas

Para garantir que seus contêineres Docker sejam seguros e livres de vulnerabilidades, é importante manter as imagens Docker atualizadas. Isso significa atualizar regularmente a imagem-base e as dependências usadas pela aplicação. Por exemplo, você pode usar os comandos `apt-get update` e `apt-get upgrade` no Dockerfile para manter o contêiner atualizado com os patches de segurança e as correções de bugs mais recentes.

Exemplo:
```Dockerfile
FROM ubuntu:latest

# Atualiza a lista de pacotes e instala atualizações de segurança
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Instala o servidor web nginx
RUN apt-get install -y nginx

# Copia o código da aplicação para o contêiner
COPY . /var/www/html/

# Expõe a porta 80 para o sistema hospedeiro
EXPOSE 80

# Inicia o servidor nginx
CMD ["nginx", "-g", "daemon off;"]

```
## Continue estudando
### Documentação do Docker
[Docker](https://www.docker.com/) é uma plataforma de código aberto para criar, distribuir e executar aplicações em contêineres. O site de documentação do Docker fornece informações detalhadas sobre como instalar, configurar e usar o Docker em vários sistemas operacionais e casos de uso. O site também contém informações sobre APIs do Docker, comandos do Docker CLI e dicas para solucionar problemas.

Algumas seções úteis da documentação do Docker incluem:

- [Primeiros passos com Docker](https://docs.docker.com/get-started/)
- [Referência do Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/)
- [Referência da API do Docker](https://docs.docker.com/engine/api/v1.41/)
- [Referência do Docker Compose](https://docs.docker.com/compose/compose-file/)
- [Referência do Dockerfile](https://docs.docker.com/engine/reference/builder/)

A documentação do Docker é um ótimo recurso para aprender a usar o Docker e solucionar problemas que você encontrar.

### Docker Hub

O [Docker Hub](https://hub.docker.com/) é um repositório baseado em nuvem que permite armazenar, compartilhar e gerenciar imagens Docker. Ele inclui repositórios públicos e privados, além de compilações e fluxos de trabalho automatizados. Você pode usar o Docker Hub para armazenar suas próprias imagens Docker e também encontrar imagens pré-compiladas para aplicações e ferramentas de software populares.

Alguns recursos úteis do Docker Hub incluem:

- [Pesquisar imagens Docker](https://hub.docker.com/search?type=image)
- [Armazenar e gerenciar imagens em repositórios](https://hub.docker.com/repositories)
- [Automatizar compilações e testes com fluxos de trabalho do Docker Hub](https://docs.docker.com/docker-hub/builds/)

O Docker Hub é uma ferramenta essencial para trabalhar com Docker e pode economizar bastante tempo e esforço ao gerenciar e compartilhar imagens.

## Conclusão

Docker é uma ferramenta poderosa que ajuda a tornar suas aplicações mais portáveis, eficientes e fáceis de implantar. Seguindo estas boas práticas e dicas, você pode criar contêineres Docker seguros, fáceis de usar e rápidos de implantar. Seja para criar uma nova aplicação ou migrar uma existente para o Docker, estas etapas ajudam você a começar a criar contêineres Docker.
