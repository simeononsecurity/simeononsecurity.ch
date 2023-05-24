---
title: "Guia Definitivo: Atualizações offline do Linux para Ubuntu Debian e CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Atualizações do Linux", "ubuntu", "Debian", "CentOS", "RHEL", "atualizações off-line", "repositório local", "cache", "configuração do servidor", "configuração do cliente", "apt-mirror", "debmirror", "criarrepo", "apt-cacher-ng", "yum-cron", "Atualizações do sistema Linux", "atualizações de pacotes off-line", "atualizações de software off-line", "repositório de pacotes local", "cache de pacote local", "atualizações off-line do Linux", "lidando com atualizações off-line", "métodos de atualização off-line", "manutenção do sistema off-line", "Atualizações do servidor Linux", "Atualizações do cliente Linux", "gerenciamento de software off-line", "gerenciamento de pacotes off-line", "estratégias de atualização", "Atualizações de segurança do Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Uma ilustração de desenho animado representando um servidor e vários dispositivos clientes trocando atualizações offline."
coverCaption: ""
---

**Melhores maneiras de lidar com a instalação de atualizações do Linux offline para Ubuntu/Debian e CentOS/RHEL**

As atualizações do Linux são essenciais para manter a segurança e a estabilidade do seu sistema. No entanto, em alguns cenários, você pode ter que lidar com ambientes off-line em que a conectividade com a Internet é limitada ou inexistente. Nesses casos, torna-se crucial ter uma estratégia adequada para instalar atualizações offline. Este artigo irá guiá-lo pelas **melhores maneiras de lidar com a instalação de atualizações do Linux para Ubuntu/Debian e CentOS/RHEL** em ambientes offline, focando especificamente no uso de um repositório ou cache local.

## Configurando um repositório local

Uma das maneiras mais eficazes de lidar com atualizações off-line é configurar um repositório local. Um repositório local contém todos os pacotes e atualizações de software necessários, permitindo que você atualize seu sistema sem uma conexão com a Internet. Veja como você pode configurar um repositório local para distribuições baseadas em Debian e Red Hat:

### Para Debian/Ubuntu

1. Comece configurando um **espelho de repositório Debian** em um servidor que tenha acesso à internet. Você pode usar ferramentas como [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) para criar um espelho local dos repositórios Debian ou Ubuntu oficiais.

#### Configurando um espelho do repositório Debian com apt-mirror:

```shell
# Install apt-mirror
sudo apt-get install apt-mirror

# Edit the apt-mirror configuration file
sudo nano /etc/apt/mirror.list

# Uncomment the deb line for the desired repository
# For example, uncomment the line for Ubuntu 20.04:
# deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse

# Specify the mirror location
# Modify the base_path to your desired location
set base_path /path/to/mirror

# Save and close the file

# Run apt-mirror to start the mirroring process
sudo apt-mirror

# Wait for the mirroring process to complete
```

#### Configurando um espelho do repositório Debian com debmirror:
```shell
# Install debmirror
sudo apt-get install debmirror

# Create a directory to store the mirror
sudo mkdir /path/to/mirror

# Run debmirror to start the mirroring process
# Replace <RELEASE> with the Debian or Ubuntu release and <MIRROR_URL> with the official repository URL
# For example, to mirror Ubuntu 20.04:
sudo debmirror --arch=amd64 --verbose --method=http --dist=<RELEASE> --root=<MIRROR_URL> /path/to/mirror

# Wait for the mirroring process to complete
```
#### Instruções do Cliente Debian

2. Configure seu repositório local editando o **`/etc/apt/sources.list` arquivo no sistema off-line. Substitua as URLs do repositório padrão pela URL do repositório local. Por exemplo, se seu repositório local estiver hospedado em `http://local-repo/ubuntu` atualizar o `sources.list` arquivo de acordo.

Exemplo `/etc/apt/sources.list` arquivo:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Assim que a configuração for atualizada, você pode executar o **`apt update` comando no sistema off-line para buscar as listas de pacotes do repositório local.

```shell
sudo apt update
```

4. Finalmente, você pode usar o **`apt upgrade` comando para instalar as atualizações disponíveis do repositório local.

```shell
sudo apt upgrade
```

### Para CentOS/RHEL

1. Para configurar um repositório local para CentOS/RHEL, você precisa usar o [**`createrepo`**](https://linux.die.net/man/8/createrepo) ferramenta. Esta ferramenta cria os metadados necessários para um repositório local.

2. Crie um diretório para armazenar os arquivos do repositório em um servidor com acesso à internet. Por exemplo, você pode criar um diretório chamado **`local-repo`

3. Copie todos os arquivos e atualizações relevantes do pacote RPM para **`local-repo` diretório.

#### Configurando um repositório local com createrepo:

```shell
# Install the createrepo tool
sudo yum install createrepo

# Create a directory to store the repository files
sudo mkdir /path/to/local-repo

# Move or copy the RPM package files and updates to the local-repo directory

# Run the createrepo command to generate the necessary repository metadata
sudo createrepo /path/to/local-repo

# Update the repository metadata whenever new packages are added or removed
sudo createrepo --update /path/to/local-repo
```
4. Depois que os metadados do repositório são gerados, você pode transferir todo o `local-repo` diretório para o sistema off-line usando uma unidade USB ou qualquer outro meio.

5. No sistema off-line, crie um novo `.repo` arquivo no `/etc/yum.repos.d/` diretório. Forneça os detalhes de configuração necessários, como o `baseurl` apontando para o diretório do repositório local.

Por exemplo, crie um arquivo chamado `local.repo` no `/etc/yum.repos.d/` diretório e adicione o seguinte conteúdo:
```shell
sudo nano /etc/yum.repos.d/local.repo
```
```toml
[local]
name=Local Repository
baseurl=file:///path/to/local-repo
enabled=1
gpgcheck=0
```
6. Salve o arquivo e saia do editor.

7. Depois de configurar o repositório, você pode usar o comando yum update para instalar atualizações do repositório local.

```shell
sudo yum update
```

Este comando atualizará os pacotes no sistema usando os pacotes do repositório local.

Lembre-se de atualizar o repositório local executando o `createrepo` comando sempre que novos pacotes são adicionados ou removidos do repositório.

Observe que você precisará substituir `/path/to/local-repo` com o caminho real para o diretório onde você armazenou os arquivos do repositório.

## Configurando um Cache Local

Outra abordagem para lidar com atualizações offline é configurar um cache local. Um cache local armazena os pacotes e atualizações baixados, permitindo que você os distribua em vários sistemas sem a necessidade de downloads individuais. Você configuraria esse cache em um sistema on-line e, em seguida, moveria o diretório para um sistema off-line para permitir que outros sistemas acessassem os pacotes. Veja como você pode configurar um cache local para distribuições baseadas em Debian e Red Hat:

### Para Debian/Ubuntu

1. Instale e configure [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) um proxy de cache para pacotes Debian/Ubuntu. Você pode instalá-lo executando o comando **`sudo apt-get install apt-cacher-ng`

2. Uma vez instalado, edite o **`/etc/apt-cacher-ng/acng.conf` arquivo para configurar o comportamento de cache. Certifique-se de que **`PassThroughPattern` O parâmetro inclui as URLs de repositório necessárias.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Remova o comentário ou adicione as URLs de repositório necessárias ao parâmetro PassThroughPattern. Por exemplo, para incluir os repositórios do Ubuntu, adicione ou remova o comentário da seguinte linha:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Salve o arquivo e saia do editor.

3. Inicie o [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) serviço usando o comando **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. Nos sistemas off-line, configure o **`/etc/apt/apt.conf.d/02proxy` arquivo para apontar para o cache local. Use a seguinte linha: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Adicione a seguinte linha ao arquivo, substituindo <cache-server-ip> pelo endereço IP do servidor de cache:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Salve o arquivo e saia do editor

5. Agora, ao executar o **`apt update` e **`apt upgrade` comandos nos sistemas off-line, eles recuperarão os pacotes do cache local.

```shell
sudo apt update
sudo apt upgrade
```
Esses comandos irão buscar e instalar as atualizações do cache local, reduzindo a necessidade de acesso à internet nos sistemas off-line.

Observe que você precisará substituir **`<cache-server-ip>` com o endereço IP real da máquina onde o **apt-cacher-ng** está instalado.

### Para CentOS/RHEL

1. Para CentOS/RHEL, você pode usar [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) para configurar um cache local. Instale-o executando o comando **`sudo yum install yum-cron`

2. Edite o **`/etc/yum/yum-cron.conf` arquivo e configurar o **`download_only` parâmetro para **`yes` Isso garante que os pacotes sejam apenas baixados e não instalados automaticamente.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Inicie o [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) serviço usando o comando **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. Nos sistemas off-line, crie um diretório local para armazenar os pacotes baixados, por exemplo, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Copie os pacotes baixados do sistema online para o diretório de cache local.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Substituir `/path/to/local/cache` com o caminho para o diretório de cache local no sistema off-line.

6. Nos sistemas off-line, crie um novo **`.repo` arquivo no **`/etc/yum.repos.d/` diretório, apontando para o diretório de cache local.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Adicione o seguinte conteúdo ao arquivo, substituindo `<local-cache-path>` com o caminho para o diretório de cache local:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Salve o arquivo e saia do editor.

7. Finalmente, você pode usar o **`yum update` comando nos sistemas off-line para instalar atualizações do cache local.

```shell
sudo yum update
```

Este comando atualizará os pacotes nos sistemas off-line usando os pacotes do cache local.

Observe que você precisará substituir **`<local-cache-path>` com o caminho real para o diretório de cache local no sistema off-line.

______

## Conclusão

Lidar com atualizações do Linux em ambientes off-line pode ser desafiador, mas com a abordagem certa, você pode garantir que seus sistemas permaneçam atualizados e seguros. Neste artigo, discutimos as melhores maneiras de lidar com a instalação de atualizações offline para Ubuntu/Debian e CentOS/RHEL. Exploramos a configuração de um repositório local e um cache local, fornecendo instruções passo a passo para distribuições baseadas em Debian e Red Hat.

Seguindo esses métodos, você pode manter a segurança e a estabilidade de seus sistemas Linux, mesmo em ambientes off-line. Lembre-se de atualizar periodicamente seu repositório ou cache local para incluir as atualizações mais recentes.

______

## Referências

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
