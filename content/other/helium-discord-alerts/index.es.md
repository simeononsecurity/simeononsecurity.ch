---
title: "Setting up HDS: Helium Hotspot Activity and Reward Notifications on Discord"
draft: false
toc: true
date: 2022-02-27
description: "Learn how to set up HDS, a tool that sends Helium hotspot activity and reward notifications to your Discord channel, with this step-by-step guide."
tags: ['Helium Miner Discord Notifications', 'Discord', 'Discord Notifications', 'Helium Notifications', 'Helium Miner', 'HNT', 'Helium Blockchain', 'Virtual Private Server', 'Cron', 'Cron Jobs']
cover: "/img/cover/A_3D_animated_art_style_image_of_a_computer_screen_display.png"
coverAlt: "A 3D animated art style image of a computer screen displaying a Helium hotspot dashboard with notifications popping up on the screen. The image is surrounded by icons representing Linux, Ubuntu, VPS, VM, and Git. "
coverCaption: ""
---
```bash
sudo apt install git python python3-pip -y
git clone https://github.com/co8/hds
cd ~/hds
cp new-config.json config.json
cp new-activity_history.json activity_history.json
nano config.json
```
```json
{
  "hotspot": "112MWdscG3DjHTxdCrtuLk...",
  "discord_webhook": "https://discord.com/api/webhooks/87869..."
}
```
```bash
#cd ~/hds
#pip install -r requirements.txt
python -m pip install discord-webhook
```
```
*/5 * * * * cd ~/hds; python3 hds.py >> cron.log 2>&1
20 4 * * 0 cd ~/hds; rm cron.log; echo "cron.log cleared (weekly)" >> cron.log 2>&1
```
```
cd ~/hds
python3 hds.py
```
 **Configuración de HDS - Herramienta de estado de Discord de Hotspot** *Actividad de Helium Hotspot y notificaciones de recompensas enviadas a su canal Discord*  Reciba notificaciones de actividad y recompensas en el punto de acceso de Helium enviado directamente a su canal de Discord con la herramienta Hotspot Discord Status (HDS). La configuración requiere conocimientos básicos de Linux, un Ubuntu VPS o Ubuntu VM y un Helium Miner. El artículo proporciona instrucciones paso a paso sobre cómo crear el webhook de Discord requerido, encontrar el nombre y la dirección del punto de acceso de Helium, instalar el software requerido y configurar un trabajo cron. El artículo también incluye una prueba para verificar que su configuración funciona correctamente. Realice un seguimiento de sus recompensas de blockchain de Helium en tiempo real con HDS.  ## Requerido: - Conocimientos generales de Linux - Un Ubuntu VPS o Ubuntu VM - Un minero de helio - Copia del [Software HDS](https://github.com/co8/hds)  ## Configuración de una máquina virtual Linux: Asumiré que tiene algunas habilidades básicas de Linux y sabe cómo configurar un VPS o linux vm. Si necesita ayuda, consulte los siguientes recursos para crear un VPS de ubuntu por tan solo $5 al mes:  - [https://docs.digitalocean.com/products/droplets/how-to/create/](https://docs.digitalocean.com/products/droplets/how-to/create/)  - [https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/initial-server-setup -con-ubuntu-20-04)  ## Configuración de la herramienta Estado de Discord de Hotspot: ### Creando el webhook de Discord requerido:  - [Discord - Introducción a los webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)  ### Encontrar el nombre y la direccion del punto de acceso Helio requerido:  - [Punto de acceso](https://app.hotspotty.net/workspace/puntos de acceso)  - [Explorador de helio](https://explorer.helium.com/)  ### Instalación del software necesario: - Esto instalará el software y los archivos necesarios para configurar su implementación de HDS. Por último, abra el archivo ```config.json``` en el que deberá pegar la URL del webhook de Discord y la dirección de su punto de acceso. ex.:  - Ahora necesitamos instalar una dependencia ### Configuración del trabajo cron: - Ejecuta lo siguiente: ```crontab -e``` - Pegue lo siguiente en su archivo crontab:  ### Pruebe para ver si su configuración está funcionando: