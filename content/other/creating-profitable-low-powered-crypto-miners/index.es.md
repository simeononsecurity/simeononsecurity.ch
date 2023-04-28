---
title: "Build a Profitable Passive Income Box with Low-Powered Hardware: A Guide"
draft: false
toc: true
date: 2023-02-07
description: "Learn how to set up a low-powered passive income crypto miner using a Raspberry Pi or Intel NUC, and earn $10-$20 per month per box with this guide"
tags: ["Build a Profitable Passive Income Box", "Low-Powered Hardware", "Passive Income", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Guide", "Hardware Requirements", "OS Installation", "Software Installation", "Docker", "Automatic Docker Container Updates", "Ubuntu Server", "Ubuntu Desktop", "Raspbian", "Budget", "USFF", "Tiny", "Mini", "Micro PC", "Technical Experience", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Watchtower", "Bitping"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "a green, circuit board shaped like a box with internet connectivity symbols as wires connected to it."
coverCaption: ""
---
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```
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
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```
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
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```
 **Construya una caja de ingresos pasivos rentables con hardware de bajo consumo: una guía** Muchas personas en estos días se dedican a la criptominería y a los mineros de baja potencia, como los mineros de helio. Estos son geniales y todo, pero ya no ganan tanto y se centran en un tipo de ganancia. Hoy vamos a construir una caja de ingresos pasivos de baja potencia que gana entre $10 y $20 al mes por caja e IP residencial.  *Si tiene la capacidad de configurar esta caja en una red de invitados o, mejor aún, en una VLAN segregada, hágalo. Si bien este es un blog de seguridad, no podemos asumir las preocupaciones de seguridad y la tolerancia al riesgo de todos.*  ## Requisitos de hardware: Se requiere uno de los siguientes. Básicamente, solo necesitamos cualquier computadora eficiente y de baja potencia que podamos tener en nuestras manos. Cualquier Raspberry PI, Intel NUC o similar. No tienen que ser tan poderosos. Sin embargo, le recomendaré que tenga al menos 32 g-64 g de almacenamiento, 4 g de RAM y al menos 2 subprocesos de CPU. Para esto, apuntaremos a un presupuesto de alrededor de $ 100- $ 200 para hardware, pero siéntase libre de aumentar si se adapta a sus necesidades. Nuestro objetivo de potencia es aprox. 25w promedio. ### Frambuesa Pi: Es difícil conseguirlos en estos días, pero tienen un consumo de energía muy bajo y son bastante personalizables. Para obtener información sobre cómo instalar raspian en su Raspberry PI - [Kit de bricolaje Raspberry Pi 4B Modelo B](https://amzn.to/3x72kv0) - [Kit de inicio GeeekPi Raspberry Pi 4 4GB](https://amzn.to/3jG2g2k) - [Kit de inicio GeeekPi Raspberry Pi 4 8GB](https://amzn.to/3DQisF6) ### Núcleo Intel: Gran variedad de modelos que hay. Siéntase libre de elegir uno más nuevo. - [Intel NUC 12 Pro](https://amzn.to/3JTzLc7) - [Intel NUC 8] (https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8) - [Intel NUC 6] (https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6) ### Cualquier USFF/Tiny/Mini/Micro PC: - [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642) - [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978) ### Cualquier Mini PC con Intel N5100 o similar Para el equivalente a Raspberry Pi de súper bajo consumo pero en la plataforma x64. - [Mini PC Beelink U59] (https://amzn.to/3YkFhcj) - [Miniordenador TRIGKEY](https://amzn.to/3XkbXkS)  ## Instalación del sistema operativo: No entraremos en los detalles técnicos de cómo instalar un sistema operativo aquí. Sin embargo, aquí hay algunos recursos excelentes para comenzar ### Raspbian: - [Primeros pasos](https://www.raspberrypi.com/documentation/computers/getting-started.html) - [El nuevo método para configurar Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns) ### Ubuntu: - [Instalar el escritorio de Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) - [Servidor Ubuntu - Instalación básica](https://ubuntu.com/server/docs/installation) - [Guía completa para principiantes de Ubuntu: descarga e instalación de Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)   ## Instalación de software: Esta va a ser una seccion mas larga. Vamos a configurar la ventana acoplable y luego, a través de la ventana acoplable, configuraremos las actualizaciones automáticas del contenedor de la ventana acoplable e instalaremos varios contenedores de la ventana acoplable. También asumimos que está utilizando el servidor ubuntu, sin embargo, los comandos para el servidor ubuntu, el escritorio ubuntu y raspbian pueden ser todos iguales.  *Para esta sección asumimos cierta experiencia técnica básica y que ya ha instalado su sistema operativo y sabe cómo ingresar a la terminal.*  ### Instalando actualizaciones: Primero queremos estar seguros de que tenemos nuestro sistema completamente actualizado:  ### Instalación de Docker: Necesitamos desinstalar cualquier versión existente que venga preempaquetada con el sistema operativo e instalar la última desde el repositorio de Docker.  ### Instalar Atalaya: Este contenedor acoplable actualiza automáticamente todos sus contenedores acoplables a las últimas imágenes en un intervalo regular y limpia las imágenes antiguas (obsoletas).  ### Instalar Bitping: [*Bitping es una solución de optimización del rendimiento y monitoreo de sitios web que proporciona monitoreo de usuarios reales en tiempo real y comentarios instantáneos sobre el tiempo de inactividad o el rendimiento degradado, con pruebas de estrés y evaluación comparativa, redireccionamiento dinámico y reaprovisionamiento impulsado por una capa de inteligencia de red distribuida e integración con flujos de trabajo existentes a través de webhooks.*](https://bitping.com)  Bitping le ofrece la posibilidad de recibir pagos en Solana por proporcionar un nodo para que las empresas ejecuten pruebas de red livianas desde su red. Esto promedia alrededor de 0,1 centavos por día por nodo. No sé mucho, pero tiene potencial y los pagos son fáciles.  #### Crea una cuenta: Crea una cuenta en [bitping.com](https://bitping.com)  #### Instale el contenedor docker: Paso 1. Ejecute estos comandos primero, ya que lo guiarán a través de la configuración de su contenedor y le pedirá que inicie sesión.  Presiona CTRL+C en tu teclado para salir del contenedor después de iniciar sesión con tu cuenta de bitping.  Paso 2. Ejecute este comando para conservar el contenedor en segundo plano   ### Instalar la aplicación Ganar: [*Aproveche el tiempo que sus dispositivos están inactivos cobrando por los recursos no utilizados de su dispositivo*](https://earnapp.com/i/c1dllee)  La aplicación Earn le permite compartir su Internet como un servicio VPN por una sorprendente cantidad de recompensas. Promedia alrededor de $ 5 por mes por nodo por IP residencial. Ofrece pagos a través de paypal y tarjetas de regalo de Amazon.  #### Crear una cuenta de la aplicación Ganar: Crea una cuenta en [earnapp.com](https://earnapp.com/i/c1dllee). *Advertencia, requiere una cuenta de Google*  #### Instale la versión no docker de la aplicación para obtener su UUID: Asegúrese de desinstalarlo después de obtener su UUID; de lo contrario, terminará ejecutándolo dos veces en el mismo host y sin actualizaciones automáticas. - [Instrucciones](https://help.earnapp.com/hc/en-us/articles/10261224561553-Instrucciones-de-instalacion)  #### Instale el contenedor docker: Modifique la cadena antes de pegarla en su terminal. Debe especificar el UUID de su aplicación de ingresos. #### Videotutorial: {{< id de youtube="tt499o0OjGU" >}}  ### Instalar Honey Gain: [*Ingresos pasivos: sin esfuerzo con Honeygain, puede ganar dinero simplemente compartiendo su Internet. Comience a ganar ahora.*](https://r.honeygain.me/DAVID07A75)  Honey Gain le permite compartir su Internet como un servicio VPN por una sorprendente cantidad de recompensas. Promedia alrededor de $ 5 por mes por nodo por IP residencial. Los pagos pueden ser complicados. Lea más antes de decidir usar este contenedor  #### Crear una cuenta de ganancia de miel: Cree una cuenta en [honeygain.com](https://r.honeygain.me/DAVID07A75)  #### Instale el contenedor Docker: Modifique la con el correo electrónico, la contraseña y el nombre del dispositivo cadena obvio antes de pegarlos en la terminal  #### Instrucciones alternativas para Raspberry Pi - [Cómo instalar Honeygain en una Raspberry Pi con sistema operativo Raspberry Pi estándar](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)  #### Videotutorial: {{< id de youtube="Wd11M0nSy1k" >}}  ### Instalar PawnsApp: [*Gane dinero pasivo en línea completando encuestas y compartiendo su Internet *](https://pawns.app/?r=sos) La aplicación Pawns, nuevamente similar a las otras enumeradas aquí, ofrece pagarle por compartir su Internet. El pago mínimo es de $5. El pago promedio es de $0.50 por mes por nodo por IP.  #### Crear una cuenta de PawnsApp: Crea una cuenta en [https://pawns.app](https://pawns.app/?r=sos)  #### Instale el contenedor Docker:  Modifique lo siguiente con su correo electrónico, contraseña, nombre del dispositivo e identificación del dispositivo antes de copiar a su terminal.  ### Instalar Peer 2 Beneficio: [*¡COMPARTE TU TRÁFICO Y GANANCIAS!*](https://p2pr.me/16538445386293aa3aaec4e)  Al igual que EarnApp y HoneyGain, Peer2Profit comparte su Internet confinado VPN y Scraping. Gana alrededor de $1 al mes por nodo por IP. Ofrece una variedad de pagos que incluyen giros postales, BTC, LTC, LTC, MATIC, etc.  #### Crear una cuenta de ganancias Peer 2: Cree una cuenta en [peer2profit.com](https://p2pr.me/16538445386293aa3aaec4e)  #### Instale el contenedor Docker: #### Videotutorial: {{< id de youtube="J_rSV5N8aQk" >}}   ### Instalar Repocket: [*Gana dinero por tu Internet no utilizado*](https://link.repocket.co/pyqL)  Similar a otras ofertas aquí. Pago mínimo de $20. Los pagos pueden ser complicados. Investigue por sí mismo para ver si desea utilizar este servicio. Los pagos promedian alrededor de $ 1 por nodo por caja al mes.  #### Crear una cuenta de Repocket: Cree una cuenta en [repocket.co](https://link.repocket.co/pyqL) y tome su clave de API desde su tablero. #### Instale el contenedor Docker: Modifique la siguiente línea con su correo electrónico y clave de API antes de pegarla en su terminal. #### Videotutorial: {{< id de youtube="171gWknfAbY" >}}  ### Instale el monetizador de trafico: [*Comparte su conexión a Internet y gana dinero en línea*](https://traffmonetizer.com/?aff=242022)  Al igual que EarnApp y HoneyGain, TraffMonetizer le paga por compartir su Internet. Promedia alrededor de $ 2 por mes por nodo por IP. Solo ofrece pagos en BTC.  #### Crea tu cuenta de monetizador de trafico: Crea tu cuenta en [https://traffmonetizer.com](https://traffmonetizer.com/?aff=242022) Una vez que ingrese al tablero, tome nota de su token de aplicación.  #### Instale el contenedor Docker: Copie la siguiente cadena y agregue su token que obtuvo del tablero antes de pegarlo en su terminal.   ### Instalar Mysterium: [Mysterium](https://www.mysterium.network/) es un servicio de webscraping y VPN descentralizado construido sobre las cadenas de bloques Etherium y Polygon. Los pagos promedian entre $ 1 y $ 20 por mes, según múltiples factores por nodo por IP. Cuesta $1.XX configurar un nodo para la activación. Pagos en token MYST.   #### Instale el contenedor Docker:  #### Configurar el contenedor Docker: Vaya a http://"nodeip"/#/dashboard reemplazando "nodeip" con la dirección IP de su nodo. Puede esto encontrar escribiendo "ifconfig" en la terminal.  Haga clic en "iniciar configuración de nodo".  Pase la dirección de la billetera ERC20 en la que desea recibir recompensas y haga clic en "siguiente". Puede usar una dirección Ethereum estándar como una de sus direcciones MetaMask.  Escriba una contraseña que usará para acceder a este tablero de nodos en el futuro. SÍ marque la casilla de verificación para reclamar el nodo en su red.  Haga clic en el enlace "Consígalo aquí" y busque su clave API. Cópialo. Vuelve atrás y pégalo. Haga clic en "Guardar y continuar".  #### Reenvío de puertos: No podemos describir cómo reenviar el puerto para el hardware específico de todos. Aquí hay algunos recursos para aprender a portar hacia adelante. - [PortForward.com](https://portforward.com/) - [Mysterium - Reenvío de puertos](https://docs.mysterium.network/troubleshooting/port-forwarding)   ### Reinicio automatico de contenedores Docker en el arranque:  ### Configuraciones opcionales: - [Actualizaciones y reinicios automáticos de Ubuntu](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/) - [Bloqueo del tráfico ToR en Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver) #### Aumente la seguridad bloqueando malware y rastreadores. Fuerce todas las solicitudes de dns al malware de Cloudflares y dns de protección de seguimiento. Además, bloquee las solicitudes de DNS/HTTPS. *Si tiene un enrutador o un cortafuegos más avanzado en la red, incluso puede usar paquetes como snort/securita para crear reglas más avanzadas para bloquear direcciones IP que actúan mal, acceso a tor, torrents, tráfico p2p en general, etc. sugerido pero no requerido.* Para un bloqueo ToR más avanzado, puede hacer lo siguiente:  ## ¿Ganancia?