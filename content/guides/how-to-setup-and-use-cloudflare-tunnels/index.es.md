---
title: "Configuración de túneles de Cloudflare: Optimice y proteja su tráfico de red"
draft: false
toc: true
date: 2023-05-26
description: "Aprenda a configurar los túneles de Cloudflare para agilizar y proteger el tráfico de su red, mejorando el rendimiento y la seguridad."
tags: ["Túneles Cloudflare", "Seguridad de las redes", "Rendimiento del sitio web", "Servidor proxy", "Tráfico web", "Configuración de la red", "Servidor Ubuntu", "Cuenta Cloudflare", "Autenticación", "Creación de túneles", "Enrutamiento del tráfico", "Registros DNS", "Conexión segura", "Alojamiento web", "Servicio proxy", "Protección de redes", "Optimización del rendimiento", "Integración de Cloudflare", "Configuración del servidor", "Cifrado del tráfico", "Gestión del tráfico de red", "Alojamiento web seguro", "Seguridad del sitio web", "Configuración de Ubuntu", "Tecnología de túneles", "Servicios de Cloudflare", "Rendimiento de la red", "Seguridad web", "Seguridad del servidor", "Gestión del tráfico", "Proxy de Cloudflare"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "Ilustración que muestra un túnel de red que conecta un servidor local con el logotipo de Cloudflare, simbolizando el tráfico de red seguro y optimizado."
coverCaption: ""
---

**Guía para configurar túneles de Cloudflare**

## Introducción
Los túneles de Cloudflare proporcionan una forma segura de alojar sitios web estableciendo una conexión directa entre su red local y Cloudflare. Esta guía le guiará a través del proceso de configuración de los túneles de Cloudflare para mejorar la seguridad y el rendimiento de su sitio web.

______

## ¿Por qué túneles de Cloudflare?
Los túneles de Cloudflare ofrecen varias ventajas, como la reducción de los vectores de ataque y la simplificación de las configuraciones de red. Al utilizar Cloudflare como proxy, puede cerrar los puertos externos y asegurarse de que todo el tráfico pasa a través de la red segura de Cloudflare. Esto proporciona una capa adicional de protección para su sitio web.

______

## Requisitos previos
Antes de configurar los túneles de Cloudflare, asegúrese de tener lo siguiente:

1. Una cuenta de Cloudflare activa.
2. Un servidor que ejecute Ubuntu.

______

## Paso 1: Instalación
Para empezar, necesita instalar el paquete Cloudflare Tunnels en su servidor Ubuntu. Siga estos pasos:

1. Abre el terminal en tu servidor Ubuntu.
2. Descargue la última versión del paquete Cloudflare Tunnels ejecutando el siguiente comando:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Paso 2: Autenticación
A continuación, debe autenticar su cuenta de Cloudflare con el servicio de túneles de Cloudflare. Siga estos pasos:

1. Ejecute el siguiente comando en el terminal:

```shell
cloudflared tunnel login
```

2. Haga clic en el sitio que desea utilizar con su túnel para completar el proceso de autenticación.

## Paso 3: Creación de un túnel

Ahora es el momento de crear su túnel Cloudflare. Siga estos pasos:

1. Ejecute el siguiente comando en el terminal para crear un túnel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Elija un nombre para su túnel que sea memorable y descriptivo. Tenga en cuenta que el nombre del túnel no se puede cambiar más tarde.

3.Después de crear el túnel, se le proporcionará información importante, incluyendo el UUID de su túnel. Anote este UUID ya que será necesario para la configuración posterior.

4. Para ver una lista de todos los túneles activos, utilice el comando:

```shell
cloudflared tunnel list
```

Esto mostrará los nombres y UUIDs de sus túneles.

### Paso 4: Configurar el Túnel

Para configurar su túnel y comenzar a enrutar el tráfico, siga estos pasos:

1. Navegue hasta el directorio de túneles de Cloudflare de su servidor. La ubicación predeterminada es `/etc/cloudflared`

2. En este directorio, cree un nuevo archivo llamado `config.yml` utilizando un editor de texto de su elección.

3. 3. Rellene el archivo config.yml con el siguiente contenido:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Asegúrese de sustituir `<your_tunnels_uuid>` con el UUID de tu túnel, y actualiza la ruta al archivo de credenciales si es necesario.

## Paso 5: Enrutamiento del tráfico

Para especificar los servicios internos que desea servir a través de su túnel, siga estos pasos:

1. `Open the ` de nuevo.

2. Añada los parámetros de entrada al archivo para definir los servicios que desea enrutar a través de Cloudflare. Por ejemplo:

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

Sustituir `<your_tunnels_uuid>` con el UUID de tu túnel, y actualiza el nombre de host y los detalles del servicio según tu configuración.

3. 3. Guarde el archivo config.yml.


## Paso 6: Creación de registros DNS

Para crear registros DNS para el nombre de host y los servicios de su túnel, siga estos pasos:

1. Abre el terminal.

2. Utilice el siguiente comando para crear un registro DNS:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Sustituir `<UUID or NAME of tunnel>` con el UUID o nombre de su túnel, y `<hostname>` con el nombre de host deseado para su servicio.

3. Por ejemplo, para crear un registro DNS para ejemplo.com, ejecute el comando:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Tenga en cuenta que los cambios se reflejarán en la sección DNS de su panel de control de Cloudflare.

## Paso 7: Iniciar el túnel

Para probar e iniciar su túnel de Cloudflare, siga estos pasos:

1. Abra el terminal.

2. Ejecute el siguiente comando para iniciar el túnel:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Sustituir `<UUID or NAME of tunnel>` con el UUID o nombre de tu túnel.

3. Cloudflared configurará tu túnel y mostrará información sobre su estado. Una vez que el túnel esté funcionando correctamente, puedes proceder al siguiente paso.

4. Para prevenir que el tunel se cierre cuando salgas de la terminal, necesitas ejecutar Cloudflared como un servicio systemd. Usa el siguiente comando:

```shell
cloudflared --config /path/to/config.yml service install
```

Sustituir `/path/to/config.yml` con la ruta a su `config.yml` archivo.

## Conclusión

En esta guía, hemos cubierto los pasos para configurar los túneles de Cloudflare en Ubuntu. Siguiendo estas instrucciones, puede mejorar la seguridad y el rendimiento de su sitio web aprovechando la red de Cloudflare. Recuerde supervisar regularmente sus túneles y ajustar la configuración según sea necesario.

Si tiene algún problema o necesita más ayuda, consulte la sección [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## Referencias
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)