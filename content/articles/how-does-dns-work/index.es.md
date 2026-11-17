---
title: "Cómo funciona DNS: DNS raíz, importancia y solución de problemas"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Conoce el funcionamiento de DNS y DNS raíz, su jerarquía, el proceso de resolución, el almacenamiento en caché y el diagnóstico."
genre: ["Fundamentos de DNS", "DNS raíz", "Sistema de nombres de dominio", "Resolución DNS", "Jerarquía DNS", "Caché DNS", "Solución de problemas de DNS", "Registros DNS", "Administración de DNS", "Comandos DNS"]
tags: ["DNS", "DNS raíz", "Sistema de nombres de dominio", "Resolución DNS", "Jerarquía DNS", "Caché DNS", "Registros DNS", "Administración de DNS", "Solución de problemas de DNS", "redes", "infraestructura de Internet", "direcciones IP", "acceso a sitios web", "consulta recursiva", "servidores de nombres autoritativos", "TTL", "mecanismos de caché", "borrar caché DNS", "servidores raíz de DNS", "enrutamiento anycast", "ICANN", "colaboración de DNS", "registro A", "registro AAAA", "registro CNAME", "registro MX", "registro TXT", "registro SRV", "registro NS", "registro PTR", "registro SOA", "comandos de diagnóstico DNS", "Windows", "macOS", "Linux", "Símbolo del sistema", "terminal del sistema"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Imagen de redes informáticas interconectadas con nombres de dominio y direcciones IP, que representa el funcionamiento de DNS y DNS raíz."
coverCaption: "Conoce DNS y domina el sistema de nombres de dominio"
---

## Cómo funcionan DNS y DNS raíz

### Introducción

El Domain Name System (DNS) es una parte esencial de la infraestructura de Internet. Permite acceder a sitios web con nombres de dominio en lugar de direcciones IP. Funciona como una guía telefónica que convierte nombres legibles por las personas en direcciones IP que entienden los equipos. DNS raíz es el núcleo jerárquico y distribuido que participa en la resolución de nombres. En este artículo explicamos cómo funcionan DNS, DNS raíz y los registros que puede tener un dominio.

{{< youtube id="mpQZVYPuDGU" >}}

## El Domain Name System (DNS)

El **Domain Name System (DNS)** es un sistema descentralizado que asocia nombres de dominio con direcciones IP. Permite acceder a sitios web y otros recursos de Internet con solo escribir un nombre en el navegador. DNS evita que tengas que memorizar direcciones IP complejas.

### Jerarquía DNS

DNS funciona en una estructura jerárquica con varios niveles. En la parte superior está la zona raíz, seguida de los dominios de nivel superior (TLD), los dominios de segundo nivel y los subdominios. Cada nivel forma parte del nombre completo. En `www.example.com`, "www" es el subdominio, "example" es el dominio de segundo nivel y "com" es el TLD.

### Proceso de resolución DNS

Cuando escribes un nombre de dominio en el navegador, comienza la resolución DNS. El navegador envía una consulta a un solucionador DNS, que suele proporcionar el proveedor de Internet (ISP). El solucionador sigue varios pasos para resolver el nombre y obtener la dirección IP correspondiente.

1. **Caché DNS local**: el solucionador primero busca el nombre de dominio y la dirección IP solicitados en su caché local. Si encuentra los datos, devuelve el resultado sin más consultas.

2. **Consulta recursiva**: si los datos no están en la caché, el solucionador inicia una consulta recursiva. Primero contacta con los servidores raíz de DNS, responsables de la zona "." (punto). Estos servidores devuelven las direcciones IP de los servidores TLD del dominio solicitado.

3. **Consulta TLD**: el solucionador contacta con los servidores TLD identificados en el paso anterior y solicita las direcciones IP de los servidores de nombres autoritativos del dominio.

4. **Consulta al servidor de nombres autoritativo**: el solucionador consulta los servidores autoritativos indicados por los servidores TLD. Estos contienen los registros autoritativos del dominio y responden con la dirección IP asociada al nombre.

5. **Respuesta al cliente**: el solucionador recibe la dirección IP de los servidores autoritativos y la devuelve al navegador. El navegador puede conectarse al servidor web mediante esa dirección.

### Caché DNS

Los solucionadores DNS usan caché para mejorar el rendimiento y reducir la carga en los servidores DNS. Tras recibir una respuesta, guardan localmente la asociación entre el nombre de dominio y la dirección IP. Las siguientes consultas del mismo nombre pueden resolverse directamente desde la caché.

La caché funciona en varios niveles: el solucionador local, el del ISP y dispositivos como routers y sistemas operativos. El valor Time-to-Live (TTL) de la respuesta DNS determina cuánto tiempo se conserva un registro. Cuando vence el TTL, el solucionador elimina el registro y realiza una nueva consulta.

#### Borrar la caché DNS local

Borrar la caché DNS ayuda a resolver algunos problemas y permite que el sistema obtenga registros actualizados. Estos son los pasos para distintos sistemas operativos:

##### Windows

Para borrar la caché DNS en Windows:

1. Pulsa `Win + R`, escribe `cmd` y presiona Enter para abrir el Símbolo del sistema.

2. Escribe el siguiente comando y presiona Enter:

```bash
ipconfig /flushdns
```

Este comando vacía la caché del solucionador DNS de Windows.

##### macOS

Para borrar la caché DNS en macOS:

1. Abre Terminal desde Aplicaciones > Utilidades o búscalo con Spotlight.

2. Escribe el siguiente comando en Terminal y presiona Enter:

```bash
sudo killall -HUP mDNSResponder
```

El comando reinicia el proceso mDNSResponder, responsable de la resolución DNS en macOS.

##### Linux

El método para borrar la caché DNS en Linux depende de la distribución y el solucionador utilizado. Aquí tienes dos opciones comunes:

1. **Sistemas basados en systemd (como Ubuntu y Fedora)**:

Abre Terminal y ejecuta el siguiente comando con privilegios de administrador:

```bash
sudo systemd-resolve --flush-caches

```

El comando vacía la caché DNS en sistemas que usan systemd-resolved como solucionador.

2. **Sistemas sin systemd**:

Abre Terminal y ejecuta el siguiente comando con privilegios de administrador:

```bash
sudo /etc/init.d/nscd restart

```

El comando reinicia Name Service Cache Daemon (nscd), responsable de la caché DNS en distribuciones Linux sin systemd.

Estos pasos son orientativos. Los comandos y métodos pueden variar según la versión del sistema operativo. Borrar la caché DNS resuelve algunos problemas, pero no todos los problemas de conexión de red.

## Cómo funciona el sistema DNS raíz

El sistema DNS raíz es una parte fundamental de la infraestructura DNS. Así funciona:

### 1. Zona raíz y servidores raíz

El sistema DNS raíz comienza en la **zona raíz**, la parte superior de la jerarquía DNS. Contiene información sobre los servidores de nombres autoritativos de todos los dominios de nivel superior (TLD), como .com, .org, .net y los dominios territoriales como .us y .uk.

El sistema DNS raíz consta de 13 servidores raíz, identificados con letras de la A a la M. Se distribuyen geográficamente por todo el mundo para ofrecer redundancia y confiabilidad.

### 2. Enrutamiento anycast

Para gestionar el gran volumen de tráfico DNS, los servidores raíz usan **enrutamiento anycast**. Varios servidores comparten una dirección IP, aunque estén ubicados en distintos lugares. Según las condiciones de red, las consultas se dirigen al servidor adecuado para distribuir la carga.

Cuando una persona inicia una consulta DNS, anycast la dirige al servidor raíz disponible más cercano. La infraestructura de red selecciona la ruta más corta según las condiciones de red. Anycast distribuye la carga y ayuda a evitar cuellos de botella.

### 3. Solucionadores DNS recursivos

Cuando un solucionador DNS recibe una consulta para un nombre de dominio, inicia la resolución recursiva y contacta con uno de los servidores raíz.

El servidor raíz responde con una referencia a las direcciones IP de los servidores de nombres TLD responsables del TLD solicitado. Esos servidores contienen información sobre los servidores autoritativos de los dominios dentro de dicho TLD.

### 4. Referencias y servidores de nombres autoritativos

Tras recibir la referencia del servidor raíz, el solucionador contacta con el servidor de nombres TLD correspondiente.

El servidor TLD responde con otra referencia que contiene las direcciones IP de los servidores de nombres autoritativos del dominio solicitado.

Después, el solucionador solicita a esos servidores la dirección IP asociada al nombre de dominio.

### 5. Caché y TTL

Durante la resolución DNS, la caché mejora el rendimiento y reduce la carga de los servidores. Los solucionadores guardan las asociaciones de nombres de dominio y direcciones IP.

Los registros DNS se almacenan durante el periodo definido por Time-to-Live (TTL). El TTL indica cuánto tiempo sigue siendo válido un registro. Cuando vence, el solucionador elimina el registro y vuelve a consultar para obtener la dirección IP actualizada.

### 6. Colaboración y administración

El sistema DNS raíz se administra mediante la colaboración entre Internet Corporation for Assigned Names and Numbers (ICANN) y los operadores de servidores raíz.

ICANN supervisa la administración y coordinación general de DNS y trabaja con los operadores de servidores raíz. Juntos mantienen el archivo de la zona raíz, que contiene información de los 13 servidores DNS raíz y sus direcciones IP.

Los operadores de servidores raíz garantizan el funcionamiento y la disponibilidad de los servidores raíz. Así contribuyen a la estabilidad y resiliencia de toda la infraestructura DNS.

El sistema DNS raíz es el punto de partida de la resolución DNS. Permite asociar nombres de dominio con direcciones IP y facilita el acceso a sitios y recursos de Internet.

#### Los 13 servidores DNS raíz

Los 13 servidores DNS raíz se identifican con letras de la A a la M. Cada servidor opera desde diferentes ubicaciones físicas para ofrecer redundancia y tolerancia a fallos. Procesan consultas de la zona raíz, incluidos los TLD .com, .org, .net y los dominios territoriales .us y .uk.

#### ICANN y la administración de DNS raíz

Internet Corporation for Assigned Names and Numbers (**ICANN**) administra y coordina DNS y la asignación de direcciones IP. Trabaja con los operadores de servidores raíz para mantener la estabilidad y seguridad de DNS raíz. Juntos conservan el archivo de zona raíz con datos de los 13 servidores raíz y sus direcciones IP.

______

## Tipos de registros DNS y sus funciones

{{< youtube id="HnUDtycXSNE" >}}

Los registros DNS son componentes esenciales del Domain Name System (DNS) y proporcionan distintos tipos de información asociados a un dominio. Estos son algunos tipos comunes y sus funciones:

| Tipo de registro | Descripción | Ejemplo |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Asocia un nombre de dominio con una dirección IPv4. | `example.com     IN A 192.0.2.1` |
| AAAA | Asocia un nombre de dominio con una dirección IPv6. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Asocia un alias (nombre canónico) con el nombre de dominio real. | `www.example.com IN CNAME example.com` |
| MX | Indica los servidores de correo que reciben mensajes para el dominio. | `example.com     IN MX 10 mail.example.com` |
| TXT | Guarda texto arbitrario, a menudo para SPF, DKIM o verificar el dominio. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Indica los servidores de nombres autoritativos del dominio. | `example.com     IN NS ns1.example.com` |
| SOA | Define propiedades globales de la zona (registro start of authority). | `example.com     IN SOA ns1.example.com` |
| SRV | Define la ubicación de un servicio específico del dominio. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Asocia una dirección IP con un nombre de dominio (búsqueda DNS inversa). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. Registro A (registro de dirección)

El **registro A** asocia un nombre de dominio con una dirección IPv4. Es el tipo de registro DNS más básico y común. Permite que el navegador encuentre la dirección IP del servidor web que aloja el sitio.

### 2. Registro AAAA (registro de dirección IPv6)

El **registro AAAA** cumple la misma función que el registro A, pero asocia el dominio con una dirección IPv6. Con la transición a IPv6, estos registros cobran importancia para la conectividad en redes IPv6.

### 3. Registro CNAME (registro de nombre canónico)

El **registro CNAME** crea un alias o nombre canónico para un dominio. Se usa cuando quieres que un dominio o subdominio apunte a otro. Por ejemplo, puedes crear un CNAME que dirija "www" a "mywebsite.com".

### 4. Registro MX (registro de intercambio de correo)

El **registro MX** especifica el servidor de correo que recibe los mensajes del dominio. Puedes definir varios registros con valores de prioridad que establecen el orden de los intentos cuando el servidor principal no está disponible.

### 5. Registro TXT (registro de texto)

El **registro TXT** almacena información de texto asociada a un dominio. Se utiliza para verificar dominios, publicar registros SPF (Sender Policy Framework) para autenticar el correo y guardar información o notas generales.

### 6. Registro SRV (registro de servicio)

El **registro SRV** define la ubicación de un servicio o recurso específico de un dominio. Se usa en VoIP, mensajería instantánea y otras aplicaciones que necesitan localizar servidores o servicios concretos.

### 7. Registro NS (registro de servidor de nombres)

El **registro NS** especifica los servidores de nombres autoritativos de un dominio. Estos servidores guardan sus registros DNS. El solucionador consulta los registros NS para encontrar los servidores autoritativos.

### 8. Registro PTR (registro de puntero)

El **registro PTR** asocia una dirección IP con un nombre de dominio en las búsquedas DNS inversas. Se utiliza para comprobar la identidad de servidores de correo y ayudar a prevenir el spam. Las búsquedas inversas ayudan a validar la autenticidad de un servidor de correo.

### 9. Registro SOA (registro de inicio de autoridad)

El **registro SOA** contiene información administrativa del dominio, como el servidor de nombres autoritativo principal, el correo del administrador y varios parámetros de tiempo de los registros DNS.

Estos son algunos de los muchos tipos de registros DNS. Cada uno tiene una función concreta para resolver nombres de dominio en los recursos asociados de forma precisa y eficiente.

______

## Comandos de diagnóstico DNS para distintos sistemas operativos

Cuando hay problemas de DNS, los comandos de diagnóstico ayudan a encontrar la causa. Estos son algunos comandos habituales por sistema operativo:

### Windows

#### 1. `ipconfig /flushdns`

Este comando borra la caché DNS de Windows y puede resolver problemas relacionados con registros obsoletos o incorrectos. Abre el Símbolo del sistema y ejecútalo.

#### 2. `ipconfig /all`

`ipconfig /all` muestra información detallada sobre las interfaces de red de Windows, incluidos los servidores DNS configurados. Ayuda a comprobar si se usan los servidores correctos.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Este comando reinicia mDNSResponder en macOS, el proceso responsable de la resolución DNS. Puede actualizar la configuración DNS y ayudar a resolver problemas. Abre Terminal y ejecútalo con privilegios de administrador.

#### 2. `nslookup`

El comando `nslookup` permite consultar registros DNS, probar la resolución y comprobar la conexión con servidores DNS. Abre Terminal y ejecuta `nslookup` seguido del nombre de dominio o la dirección IP que quieres investigar.

### Linux

#### 1. `systemd-resolve --flush-caches`

En sistemas Linux que usan systemd como solucionador DNS, `systemd-resolve --flush-caches` borra la caché DNS. Puede solucionar problemas provocados por entradas antiguas. Abre Terminal y ejecuta el comando con privilegios de administrador.

#### 2. `dig`

`dig` es una herramienta versátil de diagnóstico DNS disponible en Linux. Muestra información detallada sobre consultas, respuestas y configuración de los servidores DNS. Usa `dig` para consultar registros específicos, probar la resolución y diagnosticar problemas. Abre Terminal y ejecuta `dig` seguido del dominio o la dirección IP que quieres investigar.

Estos comandos ayudan a diagnosticar y resolver problemas DNS en distintos sistemas operativos. Permiten revisar la configuración DNS, los servidores usados y los problemas de conectividad.

Los comandos y sus opciones pueden variar según la versión del sistema operativo y la distribución. Consulta la documentación de tu versión para conocer los detalles de uso.
______


## Conclusión

El Domain Name System (DNS) y DNS raíz cumplen funciones esenciales en Internet. DNS permite acceder a sitios con nombres de dominio fáciles de recordar, y DNS raíz es la base de toda la jerarquía DNS. Entender cómo funcionan ayuda a navegar por la Web y a comprender la infraestructura de los servicios en línea.

______

## Referencias

- [DNS en Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Cómo funciona DNS, según Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Sitio oficial de ICANN](https://www.icann.org/)
- [operadores de servidores raíz](https://www.root-servers.org/)
