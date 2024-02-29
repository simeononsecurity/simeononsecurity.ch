---
title: "Создайте прибыльную коробку пассивного дохода с помощью маломощного оборудования: руководство"
draft: false
toc: true
date: 2023-02-07
description: "Узнайте, как настроить маломощный крипто-майнер с пассивным доходом, используя Raspberry Pi или Intel NUC, и зарабатывать от 10 до 20 долларов в месяц за коробку с помощью этого руководства"
tags: ["Создайте прибыльную коробку пассивного дохода", "Маломощное оборудование", "Пассивный доход", "Крипто майнер", "Raspberry Pi", "Интел НУК", "Гид", "Требования к оборудованию", "Установка ОС", "Установка программы", "Докер", "Автоматические обновления контейнеров Docker", "Сервер Ubuntu", "Рабочий стол Ubuntu", "малина", "Бюджет", "USFF", "Крошечный", "Мини", "Микро ПК", "Технический опыт", "EarnApp", "МИСТ", "Peer2Прибыль", "МедГейн", "TraffMonitizer", "Сторожевая башня", "Битпинг", "Обновления Linux", "Убунту", "Дебиан", "CentOS", "РЕЛ", "автономные обновления", "локальный репозиторий", "тайник", "настройка сервера", "настройка клиента", "подходящее зеркало", "debmirror", "создать репозиторий", "apt-cacher-нг", "ням-крон", "Обновления системы Linux", "автономные обновления пакетов", "автономные обновления программного обеспечения", "локальный репозиторий пакетов", "локальный кэш пакетов", "автономные обновления Linux", "обработка автономных обновлений", "автономные способы обновления", "автономное обслуживание системы", "Обновления сервера Linux", "Обновления клиента Linux", "автономное управление программным обеспечением", "автономное управление пакетами", "обновить стратегии", "Обновления безопасности Linux"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "зеленая печатная плата в форме коробки с символами подключения к Интернету в виде проводов, подключенных к ней."
coverCaption: ""
---

**Создайте прибыльную коробку пассивного дохода с помощью маломощного оборудования: руководство**
В наши дни многие люди занимаются майнингом криптовалют и маломощными майнерами, такими как майнеры гелия. Это здорово и все такое, но они больше не зарабатывают так много, и они сосредоточены на одном виде заработка. Сегодня мы собираемся создать маломощную коробку с пассивным доходом, которая зарабатывает от 10 до 20 долларов в месяц за коробку и жилой IP.

*Если у вас есть возможность настроить это устройство в гостевой сети или, что еще лучше, в отдельной VLAN, сделайте это. Хотя это блог по безопасности, мы не можем исходить из того, что все обеспокоены безопасностью и терпимостью к рискам.*

## Аппаратные требования:
Требуется одно из следующих действий. По сути, нам просто нужен любой эффективный и маломощный компьютер, который мы сможем достать. Подойдет любой Raspberry PI, Intel NUC или аналогичный. Они не должны быть такими мощными. Однако я рекомендую вам иметь не менее 32-64 г памяти, 4 г оперативной памяти и не менее 2 потоков процессора. Для этого мы будем ориентироваться на бюджет около 100-200 долларов на оборудование, но вы можете увеличить его, если это соответствует вашим потребностям. Наша целевая мощность составляет ок. 25 Вт в среднем.
### Raspberry Pi:
В наши дни их трудно достать, но они очень маломощные и вполне настраиваемые. Для получения информации о том, как установить raspian на ваш Raspberry PI
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
Там большое разнообразие моделей. Не стесняйтесь выбирать более новый.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Любой USFF/Tiny/Mini/Micro PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Любой мини-ПК с процессором Intel N5100 или аналогичным
Для супернизкого энергопотребления эквивалентен Raspberry Pi, но на платформе x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Установка ОС:
Мы не будем вдаваться в технические подробности установки операционной системы. Однако вот несколько отличных ресурсов, с которых можно начать
### Распбиан:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Убунту:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Установка программы:
Это будет более длинный раздел. Мы собираемся настроить докер, а затем через докер мы настроим автоматические обновления контейнеров докеров и установим несколько контейнеров докеров. Мы также предполагаем, что вы используете сервер ubuntu, однако команды для сервера ubuntu, рабочего стола ubuntu и raspbian должны быть одинаковыми.

*В этом разделе мы предполагаем, что у вас есть базовый технический опыт и что вы уже установили свою операционную систему, а также знаете, как войти в терминал.*

### Установка обновлений:
Сначала мы хотим убедиться, что наша система полностью обновлена:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Установка Докера:
Нам нужно удалить все существующие версии, которые поставляются вместе с ОС, и самостоятельно установить последнюю версию из репозитория Docker.
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

### Установите Сторожевую Башню:
Этот док-контейнер автоматически обновляет все ваши док-контейнеры до последних образов через регулярные промежутки времени и очищает старые (устаревшие) образы.
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Установить битпинг:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping предлагает вам возможность получать оплату в Solana за предоставление узла для предприятий, чтобы выполнять легкие сетевые тесты из вашей сети.
В среднем это около 0,1 цента в день на узел. Я не так много знаю, но у него есть потенциал, и выплаты просты.

#### Завести аккаунт:
Создайте учетную запись на [bitping.com](https://bitping.com)

#### Установите докер-контейнер:
Шаг 1. Сначала запустите эти команды, поскольку они проведут вас через настройку вашего контейнера и попросят вас войти в систему.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Нажмите CTRL+C на клавиатуре, чтобы выйти из контейнера после входа в свою учетную запись Bitping.

Шаг 2. Запустите эту команду, чтобы сохранить контейнер в фоновом режиме.
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Установите приложение для заработка:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/GCL9QzB5)

Приложение Earn позволяет вам делиться своим интернетом в качестве VPN-сервиса за удивительное количество вознаграждений. В среднем около 5 долларов США в месяц за узел на один резидентный IP-адрес. Предлагает выплаты с помощью подарочных карт PayPal и Amazon.

#### Создайте учетную запись приложения Earn:
Создайте учетную запись на [earnapp.com](https://earnapp.com/i/GCL9QzB5)
*Внимание, требуется учетная запись Google*

#### Установите версию приложения без докера, чтобы получить свой UUID:
Обязательно удалите его после получения своего UUID, иначе вы запустите его дважды на одном хосте и без автоматических обновлений.
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Установите докер-контейнер:
Измените строку перед вставкой в терминал. Вам нужно указать UUID вашего приложения для заработка.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Видеоурок:
{{< youtube id="tt499o0OjGU" >}}

### Установите Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/HONEY9149D)

Honey Gain позволяет вам делиться своим интернетом в качестве VPN-сервиса за удивительное количество вознаграждений. В среднем около 5 долларов США в месяц за узел на один резидентный IP-адрес. Выплаты могут быть сложными. Прочтите его подробнее, прежде чем принять решение об использовании этого контейнера.

#### Создайте учетную запись Honey Gain:
Создайте учетную запись на [honeygain.com](https://r.honeygain.me/HONEY9149D)

#### Установите контейнер Docker:
Измените строку с очевидным адресом электронной почты, паролем и именем устройства перед вставкой в терминал.
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Альтернативные инструкции для Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Видеоурок:
{{< youtube id="Wd11M0nSy1k" >}}

### Установите PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=sos)
Приложение Pawns, опять же похожее на другие, перечисленные здесь, предлагает платить вам за то, что вы делитесь своим интернетом. Минимальная выплата составляет 5 долларов. Средняя выплата составляет 0,50 доллара США в месяц за узел на IP.

#### Создайте учетную запись PawnsApp:
Создайте учетную запись на [https://pawns.app](https://pawns.app/?r=sos)

#### Установите контейнер Docker:

Измените следующее, указав свой адрес электронной почты, пароль, имя устройства и идентификатор устройства, прежде чем копировать на свой терминал.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Установите Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Аналогично другим предложениям здесь. Минимальная выплата 20 долларов. Выплаты могут быть сложными. Узнайте сами, хотите ли вы воспользоваться этой услугой. Выплаты в среднем составляют около 1 доллара за узел на коробку в месяц.

#### Создайте учетную запись Repocket:
Создайте учетную запись на [repocket.co](https://link.repocket.co/raqc) и возьмите свой ключ API с панели управления.
#### Установите контейнер Docker:
Измените следующую строку, указав свой адрес электронной почты и ключ API, прежде чем вставлять в терминал.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Видеоурок:
{{< youtube id="171gWknfAbY" >}}

### Установите монетизатор трафика:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Подобно EarnApp и HoneyGain, TraffMonetizer платит вам за то, что вы делитесь своим интернетом. В среднем около 2 долларов в месяц за узел на IP. Предлагает выплаты только в BTC.

#### Создайте учетную запись для монетизации трафика:
Создайте свою учетную запись на [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Как только вы попадете на панель инструментов, запишите свой токен приложения.

#### Установите контейнер Docker:
Скопируйте следующую строку и добавьте свой токен, который вы получили с панели управления, прежде чем вставлять в свой терминал.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli_v2 start accept --token
```

### Установите Мистериум:
[Mysterium](https://www.mysterium.network/) — это децентрализованный сервис VPN и веб-скрейпинга, построенный на блокчейнах Etherium и Polygon.
Платежи в среднем составляют от 1 до 20 долларов в месяц в зависимости от множества факторов на узел на IP. Стоимость настройки узла для активации составляет 1,XX долларов США. Выплаты в токенах MYST.


#### Установите контейнер Docker:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Настройте контейнер Docker:
Перейдите на http://"nodeip"/#/dashboard, заменив "nodeip" на IP-адрес вашего узла. Вы можете найти это, набрав «ifconfig» в терминале.

Нажмите «Начать настройку узла».

Вставьте адрес кошелька ERC20, на который вы хотите получить вознаграждение, и нажмите «Далее». Вы можете использовать стандартный адрес Ethereum, например, один из ваших адресов MetaMask.

Введите пароль, который вы будете использовать для доступа к этой панели управления узлом в будущем. НЕОБХОДИМО установить флажок, чтобы заявить права на узел в вашей сети.

Нажмите ссылку «Получить здесь» и найдите свой ключ API. Скопируйте это. Вернитесь и вставьте его. Нажмите «Сохранить и продолжить».

#### Перенаправление порта:
Мы не можем описать как портировать форвард для каждого конкретного железа. Вот некоторые ресурсы, чтобы узнать, как выполнить перенос.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Автоматический перезапуск контейнеров Docker при загрузке:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Дополнительные конфигурации:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Повысьте безопасность, заблокировав вредоносное ПО и трекеры.
Направляйте все DNS-запросы к вредоносному ПО Cloudflares и отслеживайте DNS-защиту.
Также заблокируйте запросы DNS/HTTPS.
* Если у вас есть более продвинутый маршрутизатор или брандмауэр в сети, вы даже можете использовать такие пакеты, как snort/securita, для создания более сложных правил для блокировки известных недействующих IP-адресов, доступа к tor, торрентам, p2p-трафику в целом и т. д. Это очень важно. рекомендуется, но не требуется.*
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
Для более сложной блокировки ToR вы можете сделать следующее:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Выгода?