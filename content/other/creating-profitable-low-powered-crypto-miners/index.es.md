---
title: "Cree una caja de ingresos pasivos rentable con hardware de bajo consumo: una guía"
draft: false
toc: true
date: 2023-02-07
description: "Aprenda cómo configurar un criptominero de ingresos pasivos de baja potencia usando una Raspberry Pi o Intel NUC, y gane $10-$20 por mes por caja con esta guía"
tags: ["Construya una caja de ingresos pasivos rentable", "Hardware de bajo consumo", "Ingresos pasivos", "criptominero", "frambuesa pi", "NUC de Intel", "Guía", "Requisitos de hardware", "Instalación del sistema operativo", "Instalación de software", "Estibador", "Actualizaciones automáticas de contenedores Docker", "Servidor Ubuntu", "Escritorio Ubuntu", "raspbian", "Presupuesto", "USFF", "Diminuto", "Mini", "Microordenador", "Experiencia técnica", "GanarAplicación", "MÍSTICO", "Peer2Profit", "mielgain", "TraffMonitizer", "Torre de vigilancia", "mordiendo", "actualizaciones de linux", "ubuntu", "Debian", "CentOS", "RHEL", "actualizaciones sin conexión", "repositorio local", "cache", "configuración del servidor", "configuración del cliente", "apt-espejo", "debmirror", "crearrepo", "apt-cacher-ng", "yum-cron", "Actualizaciones del sistema Linux", "actualizaciones de paquetes sin conexión", "actualizaciones de software sin conexión", "repositorio de paquetes locales", "caché de paquetes locales", "actualizaciones de Linux sin conexión", "manejo de actualizaciones fuera de línea", "métodos de actualización fuera de línea", "mantenimiento del sistema fuera de línea", "actualizaciones del servidor linux", "Actualizaciones de clientes de Linux", "gestión de software fuera de línea", "gestión de paquetes fuera de línea", "actualizar estrategias", "Actualizaciones de seguridad de Linux"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "una placa de circuito verde con forma de caja con símbolos de conectividad a Internet como cables conectados a ella."
coverCaption: ""
---

**Construya una caja de ingresos pasivos rentable con hardware de bajo consumo: una guía**
Muchas personas en estos días se dedican a la criptominería y a los mineros de baja potencia, como los mineros de helio. Estos son geniales y todo, pero ya no ganan tanto y se centran en un tipo de ganancia. Hoy vamos a construir una caja de ingresos pasivos de baja potencia que gana entre $10 y $20 al mes por caja e IP residencial.

*Si tiene la capacidad de configurar esta caja en una red de invitados o, mejor aún, en una VLAN segregada, hágalo. Si bien este es un blog de seguridad, no podemos asumir las preocupaciones de seguridad y la tolerancia al riesgo de todos.*

## Requisitos de hardware:
Se requiere uno de los siguientes. Básicamente, solo necesitamos cualquier computadora eficiente y de baja potencia que podamos tener en nuestras manos. Cualquier Raspberry PI, Intel NUC o similar servirá. No tienen que ser tan poderosos. Sin embargo, le recomendaré que tenga al menos 32 g-64 g de almacenamiento, 4 g de RAM y al menos 2 subprocesos de CPU. Para esto, apuntaremos a un presupuesto de alrededor de $ 100- $ 200 para hardware, pero siéntase libre de aumentar si se adapta a sus necesidades. Nuestro objetivo de potencia es aprox. 25w promedio.
### Frambuesa Pi:
Es difícil conseguirlos en estos días, pero tienen un consumo de energía muy bajo y son bastante personalizables. Para obtener información sobre cómo instalar raspian en su Raspberry PI
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Núcleo Intel:
Gran variedad de modelos que hay. Siéntase libre de elegir uno más nuevo.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Cualquier USFF/Tiny/Mini/Micro PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Cualquier Mini PC con Intel N5100 o similar
Para el equivalente a Raspberry Pi de súper bajo consumo pero en la plataforma x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Instalación del sistema operativo:
No entraremos en los detalles técnicos de cómo instalar un sistema operativo aquí. Sin embargo, aquí hay algunos recursos excelentes para comenzar
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Instalación de software:
Esta va a ser una sección más larga. Vamos a configurar la ventana acoplable y luego, a través de la ventana acoplable, configuraremos las actualizaciones automáticas del contenedor de la ventana acoplable e instalaremos varios contenedores de la ventana acoplable. También asumimos que está utilizando el servidor ubuntu, sin embargo, los comandos para el servidor ubuntu, el escritorio ubuntu y raspbian deberían ser todos iguales.

*Para esta sección asumimos cierta experiencia técnica básica y que ya ha instalado su sistema operativo y sabe cómo ingresar a la terminal.*

### Instalando actualizaciones:
Primero queremos estar seguros de que tenemos nuestro sistema completamente actualizado:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Instalación de Docker:
Necesitamos desinstalar cualquier versión existente que venga preempaquetada con el sistema operativo e instalar la última desde el repositorio de Docker.
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

### Instalar Atalaya:
Este contenedor acoplable actualiza automáticamente todos sus contenedores acoplables a las imágenes más recientes en un intervalo regular y limpia las imágenes antiguas (obsoletas).
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Instalar Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping le ofrece la posibilidad de recibir pagos en Solana por proporcionar un nodo para que las empresas ejecuten pruebas de red livianas desde su red.
Esto promedia alrededor de 0,1 centavos por día por nodo. No sé mucho, pero tiene potencial y los pagos son fáciles.

#### Crea una cuenta:
Crea una cuenta en [bitping.com](https://bitping.com)

#### Instale el contenedor docker:
Paso 1. Ejecute estos comandos primero mientras lo guía a través de la configuración de su contenedor y le pide que inicie sesión.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Presiona CTRL+C en tu teclado para salir del contenedor después de iniciar sesión con tu cuenta de bitping.

Paso 2. Ejecute este comando para conservar el contenedor en segundo plano
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Instalar la aplicación Ganar:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

La aplicación Earn le permite compartir su Internet como un servicio VPN por una sorprendente cantidad de recompensas. Promedia alrededor de $ 5 por mes por nodo por IP residencial. Ofrece pagos a través de paypal y tarjetas de regalo de Amazon.

#### Crear una cuenta de la aplicación Earn:
Crea una cuenta en [earnapp.com](https://earnapp.com/i/c1dllee)
*Advertencia, requiere una cuenta de Google*

#### Instale la versión no docker de la aplicación para obtener su UUID:
Asegúrese de desinstalarlo después de obtener su UUID; de lo contrario, terminará ejecutándolo dos veces en el mismo host y sin actualizaciones automáticas.
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Instale el contenedor docker:
Modifique la cadena antes de pegarla en su terminal. Debe especificar el UUID de su aplicación de ingresos.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Videotutorial:
{{< youtube id="tt499o0OjGU" >}}

### Instalar Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain le permite compartir su Internet como un servicio VPN por una sorprendente cantidad de recompensas. Promedia alrededor de $ 5 por mes por nodo por IP residencial. Los pagos pueden ser complicados. Lea más antes de decidir usar este contenedor

#### Crear una cuenta de ganancia de miel:
Crea una cuenta en [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Instale el contenedor Docker:
Modifique la cadena con el correo electrónico, la contraseña y el nombre del dispositivo obvios antes de pegarlos en la terminal
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Instrucciones alternativas para Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Videotutorial:
{{< youtube id="Wd11M0nSy1k" >}}

### Instalar PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
La aplicación Pawns, nuevamente similar a las otras enumeradas aquí, ofrece pagarle por compartir su Internet. El pago mínimo es de $5. El pago promedio es de $0.50 por mes por nodo por IP.

#### Crear una cuenta de PawnsApp:
Crea una cuenta en [https://pawns.app](https://pawns.app/?r=2092882)

#### Instale el contenedor Docker:

Modifique lo siguiente con su correo electrónico, contraseña, nombre del dispositivo e identificación del dispositivo antes de copiar a su terminal.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Instalar Peer 2 Beneficio:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://p2pr.me/16538445386293aa3aaec4e)

Al igual que EarnApp y HoneyGain, Peer2Profit comparte su Internet con fines VPN y Scraping. Gana alrededor de $1 al mes por nodo por IP.
Ofrece una variedad de pagos que incluyen giros postales, BTC, LTC, LTC, MATIC, etc.

#### Crear una cuenta de ganancias Peer 2:
Crea una cuenta en [peer2profit.com](https://p2pr.me/16538445386293aa3aaec4e)

#### Instale el contenedor Docker:
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### Videotutorial:
{{< youtube id="J_rSV5N8aQk" >}}


### Instalar Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Similar a otras ofertas aquí. Pago mínimo de $20. Los pagos pueden ser complicados. Investigue por sí mismo para ver si desea utilizar este servicio. Los pagos promedian alrededor de $ 1 por nodo por caja al mes.

#### Crear una cuenta de Repocket:
Crea una cuenta en [repocket.co](https://link.repocket.co/raqc) y tome su clave api de su tablero.
#### Instale el contenedor Docker:
Modifique la siguiente línea con su correo electrónico y clave de API antes de pegarla en su terminal.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Videotutorial:
{{< youtube id="171gWknfAbY" >}}

### Instalar el monetizador de tráfico:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Al igual que EarnApp y HoneyGain, TraffMonetizer le paga por compartir su Internet. Promedia alrededor de $ 2 por mes por nodo por IP. Solo ofrece pagos en BTC.

#### Crea tu cuenta de monetizador de tráfico:
Crea tu cuenta en [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Una vez que ingrese al tablero, tome nota de su token de aplicación.

#### Instale el contenedor Docker:
Copie la siguiente cadena y agregue su token que obtuvo del tablero antes de pegarlo en su terminal.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Instalar Mysterium:
[Mysterium](https://www.mysterium.network/) es un servicio de webscraping y VPN descentralizado basado en las cadenas de bloques Etherium y Polygon.
Los pagos promedian entre $ 1 y $ 20 por mes, según múltiples factores por nodo por IP. Cuesta $1.XX configurar un nodo para la activación. Pagos en token MYST.


#### Instale el contenedor Docker:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Configure el contenedor Docker:
Vaya a http://"nodeip"/#/dashboard reemplazando "nodeip" con la dirección IP de su nodo. Puede encontrar esto escribiendo "ifconfig" en la terminal.

Haga clic en "iniciar configuración de nodo".

Pase la dirección de la billetera ERC20 en la que desea recibir recompensas y haga clic en "siguiente". Puede usar una dirección Ethereum estándar como una de sus direcciones MetaMask.

Escriba una contraseña que usará para acceder a este tablero de nodos en el futuro. SÍ marque la casilla de verificación para reclamar el nodo en su red.

Haga clic en el enlace "Consígalo aquí" y busque su clave API. Cópialo. Vuelve atrás y pégalo. Haga clic en "Guardar y continuar".

#### Reenvío de puertos:
No podemos describir cómo reenviar el puerto para el hardware específico de todos. Aquí hay algunos recursos para aprender a portar hacia adelante.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Reinicio automático de contenedores Docker en el arranque:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Configuraciones opcionales:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Aumente la seguridad bloqueando malware y rastreadores.
Fuerce todas las solicitudes de dns al malware de Cloudflares y dns de protección de seguimiento.
Además, bloquee las solicitudes de DNS/HTTPS.
*Si tiene un enrutador o un cortafuegos más avanzado en la red, incluso puede usar paquetes como snort/securita para crear reglas más avanzadas para bloquear direcciones IP que actúan mal, acceso a tor, torrents, tráfico p2p en general, etc. sugerido pero no requerido.*
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
Para un bloqueo ToR más avanzado, puede hacer lo siguiente:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## ¿Ganancia?