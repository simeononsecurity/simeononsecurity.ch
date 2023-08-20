---
title: "Crie uma caixa de renda passiva lucrativa com hardware de baixa potência: um guia"
draft: false
toc: true
date: 2023-02-07
description: "Aprenda a configurar um minerador de criptografia de renda passiva de baixa potência usando um Raspberry Pi ou Intel NUC e ganhe $ 10- $ 20 por mês por caixa com este guia"
tags: ["Construa uma caixa de renda passiva lucrativa", "Hardware de baixa potência", "Renda passiva", "Cripto Minerador", "Raspberry Pi", "Intel NUC", "Guia", "Requisitos de hardware", "Instalação do sistema operacional", "Instalação de software", "Docker", "Atualizações automáticas de contêineres do Docker", "Servidor Ubuntu", "Área de Trabalho do Ubuntu", "raspbian", "Orçamento", "USFF", "Pequeno", "mini", "Micro PC", "Experiência Técnica", "EarnApp", "MEU", "Peer2Profit", "HoneyGain", "Monitor de Tráfego", "Torre de vigia", "Mordendo", "Atualizações do Linux", "ubuntu", "Debian", "CentOS", "RHEL", "atualizações off-line", "repositório local", "cache", "configuração do servidor", "configuração do cliente", "apt-mirror", "debmirror", "criarrepo", "apt-cacher-ng", "yum-cron", "Atualizações do sistema Linux", "atualizações de pacotes off-line", "atualizações de software off-line", "repositório de pacotes local", "cache de pacote local", "atualizações off-line do Linux", "lidando com atualizações off-line", "métodos de atualização off-line", "manutenção do sistema off-line", "Atualizações do servidor Linux", "Atualizações do cliente Linux", "gerenciamento de software off-line", "gerenciamento de pacotes off-line", "estratégias de atualização", "Atualizações de segurança do Linux"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "uma placa de circuito verde em forma de caixa com símbolos de conectividade com a Internet como fios conectados a ela."
coverCaption: ""
---

**Construa uma caixa de renda passiva lucrativa com hardware de baixa potência: um guia**
Muitas pessoas hoje em dia estão em mineração de criptografia e mineradores de baixa potência, como mineradores de hélio. Estes são ótimos e tudo, mas eles não ganham mais tanto e estão focados em um tipo de ganho. Hoje vamos construir uma caixa de renda passiva de baixa potência que ganha entre US$ 10 e US$ 20 por mês por caixa e IP residencial.

*Se você puder configurar esta caixa em uma rede de convidados ou, melhor ainda, em uma VLAN segregada, faça-o. Embora este seja um blog de segurança, não podemos assumir as preocupações de segurança e a tolerância a riscos de todos.*

## Requisitos de hardware:
Um dos itens a seguir é necessário. Basicamente, só precisamos de qualquer computador eficiente e de baixa potência que possamos colocar em nossas mãos. Qualquer Raspberry PI, Intel NUC ou similar serve. Eles não precisam ser tão poderosos. No entanto, recomendo que você tenha pelo menos 32g-64g de armazenamento, 4g de RAM e pelo menos 2 threads de CPU. Para isso, visaremos um orçamento de cerca de US$ 100 a US$ 200 para hardware, mas fique à vontade para aumentar mais se atender às suas necessidades. Nosso alvo de energia é aprox. 25w em média.
### Raspberry Pi:
Difícil de conseguir hoje em dia, mas eles são de baixo consumo de energia e são bastante personalizáveis. Para obter informações sobre como instalar o raspian no seu Raspberry PI
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
Grande variedade de modelos lá fora. Sinta-se à vontade para escolher um mais novo.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Qualquer USFF/Tiny/Mini/Micro PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Qualquer Mini PC com Intel N5100 ou similar
Para o equivalente ao Raspberry Pi de super baixa potência, mas na plataforma x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Instalação do sistema operacional:
Não entraremos em detalhes técnicos de como instalar um sistema operacional aqui. No entanto, aqui estão alguns ótimos recursos para você começar
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Instalação de software:
Esta será uma seção mais longa. Vamos configurar o docker e, por meio do docker, configuraremos as atualizações automáticas do contêiner docker e instalaremos vários contêineres docker. Também presumimos que você esteja usando o servidor ubuntu, no entanto, os comandos para servidor ubuntu, desktop ubuntu e raspbian devem ser todos iguais.

*Para esta seção, assumimos alguma experiência técnica básica e que você já instalou seu sistema operacional, bem como sabe como entrar no terminal.*

### Instalando atualizações:
Primeiro, queremos ter certeza de que temos nosso sistema totalmente atualizado:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Instalando o Docker:
Precisamos desinstalar todas as versões existentes que vêm pré-empacotadas com o sistema operacional e instalar as mais recentes do próprio repositório do Docker.
```bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Instale o Watchtower:
Este contêiner docker atualiza automaticamente todos os seus contêineres docker para as imagens mais recentes em um intervalo regular e limpa as imagens antigas (obsoletas).
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Instale o Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping oferece a você a capacidade de ser pago em Solana por fornecer um nó para empresas executarem testes de rede leves a partir de sua rede.
Isso dá uma média de cerca de 0,1 centavos por dia por nó. Não sei muito, mas tem potencial e os pagamentos são fáceis.

#### Crie a sua conta aqui:
Crie uma conta em [bitping.com](https://bitping.com)

#### Instale o contêiner docker:
Etapa 1. Execute esses comandos primeiro enquanto ele orienta você na configuração do contêiner e solicita que você faça login.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Pressione CTRL+C no teclado para sair do contêiner após fazer login com sua conta bitping.

Etapa 2. Execute este comando para manter o contêiner em segundo plano
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Instale o aplicativo Earn:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

O aplicativo Earn permite que você compartilhe sua internet como um serviço VPN por uma quantidade surpreendente de recompensas. Média de cerca de US$ 5 por mês por nó por IP residencial. Oferece pagamentos via paypal e cartões-presente da Amazon.

#### Crie uma conta de aplicativo de ganhos:
Crie uma conta em [earnapp.com](https://earnapp.com/i/c1dllee)
*Aviso, requer uma conta do Google*

#### Instale a versão não docker do aplicativo para obter seu UUID:
Certifique-se de desinstalar depois de obter seu UUID, caso contrário, você acabará executando-o duas vezes no mesmo host e sem atualizações automáticas
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Instale o contêiner docker:
Modifique a string antes de colar em seu terminal. Você precisa especificar o UUID do seu aplicativo de ganho.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Vídeo tutorial:
{{< youtube id="tt499o0OjGU" >}}

### Instale o Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

O Honey Gain permite que você compartilhe sua internet como um serviço VPN por uma quantidade surpreendente de recompensas. Média de cerca de US$ 5 por mês por nó por IP residencial. Os pagamentos podem ser complicados. Leia mais antes de decidir usar este contêiner

#### Crie uma conta Honey Gain:
Crie uma conta em [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Instale o Docker Container:
Modifique a string com o e-mail, senha e nome do dispositivo óbvios antes de colar no terminal
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Instruções alternativas para Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Vídeo tutorial:
{{< youtube id="Wd11M0nSy1k" >}}

### Instale PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
O aplicativo Pawns, novamente semelhante aos outros listados aqui, oferece pagamento por compartilhar sua internet. O pagamento mínimo é de $ 5. O pagamento médio é de US$ 0,50 por mês por nó por IP.

#### Crie uma conta PawnsApp:
Crie uma conta em [https://pawns.app](https://pawns.app/?r=2092882)

#### Instale o Docker Container:

Modifique o seguinte com seu e-mail, senha, nome do dispositivo e ID do dispositivo antes de copiar para o seu terminal.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Instale o Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Semelhante a outras ofertas aqui. Pagamento mínimo de $ 20. Os pagamentos podem ser complicados. Pesquise por si mesmo para ver se deseja usar este serviço. Os pagamentos são em média de US$ 1 por nó por caixa por mês.

#### Crie uma conta Repocket:
Crie uma conta em [repocket.co](https://link.repocket.co/raqc) e pegue sua chave de API no seu painel.
#### Instale o Docker Container:
Modifique a linha a seguir com seu e-mail e chave de API antes de colar em seu terminal.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Vídeo tutorial:
{{< youtube id="171gWknfAbY" >}}

### Instale o Monetizador de Tráfego:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Semelhante ao EarnApp e ao HoneyGain, o TraffMonetizer paga para você compartilhar sua internet. Média de cerca de US $ 2 por mês por nó por IP. Oferece apenas pagamentos em BTC.

#### Crie sua Conta Monetizadora de Tráfego:
Crie sua conta em [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Depois de entrar no painel, anote o token do aplicativo.

#### Instale o Docker Container:
Copie a string a seguir e anexe seu token que você obteve do painel antes de colar em seu terminal.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Instale o Mysterium:
[Mysterium](https://www.mysterium.network/) é um serviço descentralizado de VPN e webscraping construído nas blockchains Etherium e Polygon.
Os pagamentos variam em média de US$ 1 a US$ 20 por mês, dependendo de vários fatores por nó por IP. Custa $ 1,XX para configurar um nó para ativação. Pagamentos em token MYST.


#### Instale o Docker Container:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Configure o Docker Container:
Acesse http://"nodeip"/#/dashboard substituindo "nodeip" pelo endereço IP do seu nó. Você pode encontrar isso digitando "ifconfig" no terminal.

Clique em “iniciar configuração do nó”.

Passe o endereço da carteira ERC20 na qual você deseja receber recompensas e clique em “próximo”. Você pode usar um endereço Ethereum padrão como um de seus endereços MetaMask.

Digite uma senha que você usará para acessar este painel do nó no futuro. Marque a caixa de seleção para reivindicar o nó em sua rede.

Clique no link “Get it here” e encontre sua chave de API. Copie. Volte e cole. Clique em “Salvar e continuar”.

#### Encaminhamento de porta:
Não podemos descrever como encaminhar a porta para o hardware específico de todos. Aqui estão alguns recursos para aprender como encaminhar a porta.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Reiniciar automaticamente os contêineres do Docker na inicialização:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Configurações Opcionais:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Aumente a segurança bloqueando malware e rastreadores.
Forçar todas as solicitações de DNS para malware Cloudflares e rastrear DNS de proteção.
Além disso, bloqueie as solicitações de DNS/HTTPS.
*Se você tiver um roteador ou firewall mais avançado na rede, pode até usar pacotes como snort/securita para criar regras mais avançadas para bloquear IPs conhecidos de má ação, acesso tor, torrents, tráfego p2p em geral, etc. sugerido, mas não obrigatório.*
```bash
# Allow ssh still
sudo ufw allow 22
# Allow dns out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp
# Redirect all dns back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2
# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP
# Block Default ToR Ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp
# Block Torrents
sudo ufw deny out 6881/tcp
sudo ufw deny out 6881/udp
sudo ufw deny out 6882-6999/tcp
sudo ufw deny out 6882-6999/udp
iptables -A FORWARD -m string --algo bm --string "BitTorrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "BitTorrent protocol" -j DROP
iptables -A FORWARD -m string --algo bm --string "peer_id=" -j DROP
iptables -A FORWARD -m string --algo bm --string ".torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce.php?passkey=" -j DROP
iptables -A FORWARD -m string --algo bm --string "torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce" -j DROP
iptables -A FORWARD -m string --algo bm --string "info_hash" -j DROP
# Save the Changes and Enable the Firewall
sudo iptables-save
sudo ufw enable
```
Para um bloqueio de ToR mais avançado, você pode fazer o seguinte:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Lucro?