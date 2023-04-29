---
title: "Guía para principiantes: Uso de la línea de comandos de Linux para la ciberseguridad"
date: 2023-03-13
toc: true
draft: false
descripción: "Aprende a usar la línea de comandos de Linux para la ciberseguridad con comandos básicos y avanzados".
tags: ["Linux", "Línea de comandos", "Ciberseguridad", "Guía para principiantes", "Escaneo de red", "Pruebas de vulnerabilidad", "Análisis de malware", "Permisos", "Tráfico de red", "Estado de procesos", "Estadísticas de red", "Búsqueda de archivos", "Wireshark", "TCPDump", "Nmap", "Linux CLI", "Seguridad", "Pruebas de penetración", "Forense digital"].
cover: "/img/cover/A_cartoon_illustration_of_a_person_wearing_a_hoodie.png"
coverAlt: "Ilustración de dibujos animados de una persona que lleva una sudadera con capucha, sentada frente a la pantalla de un ordenador con la interfaz de línea de comandos de Linux visible y sosteniendo una lupa para representar el aspecto de la ciberseguridad."
coverCaption: ""
---

**Linux** es un sistema operativo versátil y seguro muy utilizado en el sector de la ciberseguridad debido a su naturaleza de código abierto. Sin embargo, puede resultar desalentador para los principiantes utilizar la interfaz de línea de comandos (CLI) de Linux para realizar tareas de ciberseguridad. Esta guía tiene como objetivo proporcionar a los principiantes una visión general de los comandos básicos y avanzados de la CLI de Linux que son útiles para fines de ciberseguridad.

## Comandos básicos de Linux para ciberseguridad

### Imprimir Directorio de Trabajo

El comando **pwd** (print working directory) se usa para mostrar el directorio de trabajo actual en el CLI. El directorio de trabajo es el directorio donde se encuentra actualmente en el sistema de archivos. El comando es útil para navegar por el sistema de archivos y comprender su ubicación en relación con otros directorios. Por ejemplo, si se encuentra en el directorio principal y desea navegar al directorio de documentos, puede utilizar los siguientes comandos:

```bash
$ pwd
/home/usuario
$ cd documentos
$ pwd
/home/usuario/documentos
```

En el ejemplo anterior, el primer comando muestra el directorio de trabajo actual, que es el directorio home. El segundo comando cambia el directorio al directorio de documentos, y el tercer comando imprime el directorio de trabajo actual, que ahora es el directorio de documentos.

### Lista

El comando **ls** se utiliza para listar el contenido de un directorio en la CLI. El comando muestra los nombres de los archivos y directorios en el directorio de trabajo actual. El comando es útil para identificar los archivos y directorios en una ubicación específica. Por ejemplo, si desea ver el contenido del directorio documents, puede utilizar el siguiente comando:

```bash
$ ls documentos
archivo1.txt archivo2.pdf archivo3.docx
```

En el ejemplo anterior, el comando muestra el contenido del directorio documents, que contiene tres archivos: file1.txt, file2.pdf y file3.docx. También puede utilizar el comando sin ningún argumento para listar el contenido del directorio de trabajo actual. Por ejemplo:

```bash
$ ls
Escritorio Documentos Descargas Música Imágenes Plantillas Públicas Vídeos
```

En el ejemplo anterior, el comando muestra el contenido del directorio principal, que contiene varios subdirectorios como Escritorio, Documentos, Descargas, etc.

### Cambiar directorio

El comando **cd** (cambiar directorio) se utiliza para cambiar el directorio de trabajo actual en la CLI. El comando le permite navegar a través del sistema de archivos y acceder a archivos en diferentes ubicaciones. Por ejemplo, si desea cambiar el directorio de trabajo actual al directorio de documentos, puede utilizar el siguiente comando:

```bash
$ cd documentos
```

En el ejemplo anterior, el comando cambia el directorio de trabajo actual al directorio de documentos, que se encuentra en el directorio de trabajo actual. También puede utilizar el comando con una ruta absoluta o relativa para cambiar el directorio de trabajo a un directorio que no se encuentre en el directorio de trabajo actual. Por ejemplo:

```bash
$ cd /usr/local/bin
```

En el ejemplo anterior, el comando cambia el directorio de trabajo actual al directorio /usr/local/bin, que es una ruta absoluta. Alternativamente, puede utilizar una ruta relativa para cambiar el directorio de trabajo. Por ejemplo:

```bash
$ cd ../..
```


En el ejemplo anterior, el comando cambia el directorio de trabajo actual dos niveles por encima del directorio de trabajo actual. La notación ".." representa el directorio padre, y puedes usarla para navegar hacia arriba en el árbol de directorios.


### Concatenar

El comando **cat** (concatenar) se utiliza para mostrar el contenido de un archivo en la CLI. El comando es útil para ver el contenido de archivos basados en texto como archivos de registro o archivos de configuración. Por ejemplo, si desea ver el contenido de un archivo llamado "archivo1.txt", puede utilizar el siguiente comando:

```bash
$ cat fichero1.txt
```

En el ejemplo anterior, el comando muestra el contenido del archivo "archivo1.txt". También puede utilizar el comando para concatenar varios archivos y mostrar su contenido en la CLI. Por ejemplo

```bash
$ cat archivo1.txt archivo2.txt archivo3.txt
```


En el ejemplo anterior, el comando muestra el contenido de tres archivos: archivo1.txt, archivo2.txt y archivo3.txt. También puede utilizar el comando con comodines para concatenar todos los archivos que coincidan con un patrón específico. Por ejemplo:

```bash
$ cat *.txt
```

En el ejemplo anterior, el comando muestra el contenido de todos los archivos que tienen una extensión ".txt" en el directorio de trabajo actual. Este comando es útil para ver rápidamente el contenido de varios archivos sin abrirlos individualmente.


### Impresión global de expresiones regulares

El comando **grep** (impresión global de expresiones regulares) se utiliza para buscar cadenas o patrones específicos en un archivo o conjunto de archivos en la CLI. El comando es útil para identificar patrones en archivos de registro o buscar información específica en archivos de configuración. Por ejemplo, si desea buscar todas las apariciones de la palabra "error" en un archivo denominado "logfile.txt", puede utilizar el siguiente comando:

```bash
$ grep "error" logfile.txt
```

En el ejemplo anterior, el comando busca todas las apariciones de la palabra "error" en el archivo "logfile.txt" y muestra las líneas coincidentes en la CLI. También puede utilizar el comando con expresiones regulares para buscar patrones más complejos. Por ejemplo, si desea buscar todas las líneas que contengan una palabra que empiece por "p" y termine por "y", puede utilizar el siguiente comando:

```bash
$ grep "p.*y" logfile.txt
```

En el ejemplo anterior, el comando busca todas las líneas que contengan una palabra que empiece por "p" y termine por "y" en el archivo "logfile.txt". La expresión regular "p.*y" coincide con cualquier cadena que empiece por "p" y termine por "y", con cualquier número de caracteres intermedios. Este comando es útil para encontrar patrones en archivos de registro que pueden ayudar a identificar amenazas de seguridad o problemas de rendimiento.


### Cambiar modo

El comando **chmod** (change mode) se utiliza para cambiar los permisos de un archivo o directorio en el CLI. El comando es esencial para asegurar archivos y directorios y controlar quién tiene acceso a ellos. Los permisos están representados por tres dígitos que corresponden al propietario, grupo y otros, respectivamente. Los dígitos se calculan a partir de la siguiente fórmula:

```
4 = lectura
2 = escritura
1 = ejecutar
```

Por ejemplo, si quieres dar al propietario permisos de lectura y escritura y al grupo y otros permisos de sólo lectura a un fichero llamado "fichero1.txt", puedes usar el siguiente comando:

```bash
$ chmod 644 archivo1.txt
```

En el ejemplo anterior, el comando establece los permisos del archivo "archivo1.txt" en 644. El primer dígito (6) representa los permisos del propietario, que son de lectura y escritura (4 + 2 = 6). El primer dígito (6) representa los permisos para el propietario, que son de lectura y escritura (4 + 2 = 6). El segundo dígito (4) representa los permisos para el grupo, que son de sólo lectura. El tercer dígito (4) representa los permisos para otros, que también son de sólo lectura.

También puedes utilizar el comando con letras para cambiar los permisos. Por ejemplo, si quieres dar al propietario y al grupo permisos de lectura y escritura y a los demás ningún permiso para un archivo llamado "archivo2.txt", puedes utilizar el siguiente comando:

```bash
$ chmod ug=rw,o= archivo2.txt
```

En el ejemplo anterior, el comando establece los permisos del archivo "archivo2.txt" en ug=rw,o=, donde "ug" representa el propietario y el grupo, "r" representa el permiso de lectura y "w" representa el permiso de escritura. El signo "=" significa "establecer los permisos a", y "o=" significa "eliminar todos los permisos para los demás". Este comando es útil para controlar el acceso a archivos y directorios sensibles y evitar accesos no autorizados.


## Comandos avanzados de Linux para ciberseguridad

### Mapeador de Red

El comando **nmap** es una poderosa herramienta de escaneo de red en la CLI que puede ser usada para identificar hosts y servicios en una red, así como vulnerabilidades potenciales. El comando puede realizar un rango de técnicas de escaneo, incluyendo descubrimiento de hosts, escaneo de puertos y detección de sistemas operativos.

Uno de los usos más básicos de nmap es escanear una única dirección IP o host. Por ejemplo, para escanear una única dirección IP (192.168.1.1) en busca de puertos abiertos, puede utilizar el siguiente comando:

```bash
$ nmap 192.168.1.1
```

El comando anterior ejecutará un escaneo TCP SYN contra la IP objetivo y devolverá una lista de puertos abiertos. La salida mostrará los puertos abiertos junto con el servicio que se está ejecutando en cada puerto, el estado del puerto (abierto/cerrado) y, a veces, información adicional como el sistema operativo que se ejecuta en el objetivo.

Nmap también puede utilizarse para escanear múltiples hosts o direcciones IP a la vez. Por ejemplo, para escanear un rango de direcciones IP (192.168.1.1-255) en busca de puertos abiertos, puede utilizar la siguiente orden:

```bash
$ nmap 192.168.1.1-255
```

El comando anterior escaneará todas las direcciones IP del rango y devolverá los puertos y servicios abiertos para cada objetivo.

Además del descubrimiento básico de hosts y el escaneo de puertos, nmap también puede realizar escaneos más avanzados como la detección de servicios y versiones, la detección de sistemas operativos y el escaneo de vulnerabilidades. Estos escaneos pueden ser útiles para identificar posibles vulnerabilidades de seguridad en una red y protegerla de posibles ataques.

### Volcado de paquetes TCP

El comando **tcpdump** se utiliza para capturar y analizar el tráfico de red en la CLI, por lo que es útil para solucionar problemas de red, analizar el comportamiento de la red e identificar posibles amenazas a la seguridad. El comando captura paquetes en tiempo real y puede filtrar paquetes basándose en varios criterios, como dirección IP de origen o destino, protocolo y puerto.

Uno de los usos más básicos de tcpdump es capturar todo el tráfico de red en una interfaz específica. Por ejemplo, para capturar todo el tráfico en la interfaz eth0, puede utilizar el siguiente comando:

```bash
$ sudo tcpdump -i eth0
```

El comando anterior capturará todos los paquetes en la interfaz eth0 y los mostrará en tiempo real en la CLI. La salida mostrará las direcciones IP de origen y destino, el protocolo y otra información sobre cada paquete.

Tcpdump también puede ser usado para filtrar paquetes basados en varios criterios. Por ejemplo, para capturar todos los paquetes enviados a o desde una dirección IP específica, puede utilizar el siguiente comando:

```bash
$ sudo tcpdump host 192.168.1.1
```

El comando anterior capturará todos los paquetes enviados a o desde la dirección IP 192.168.1.1 y los mostrará en tiempo real en la CLI. También puede filtrar paquetes basándose en el protocolo (por ejemplo, TCP, UDP), el número de puerto u otros criterios.

Además de capturar paquetes en tiempo real, tcpdump también se puede utilizar para capturar paquetes a un archivo para su posterior análisis. Por ejemplo, para capturar todos los paquetes en la interfaz eth0 y guardarlos en un archivo llamado "capture.pcap", puede utilizar el siguiente comando:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

El comando anterior capturará todos los paquetes en la interfaz eth0 y los guardará en el archivo "capture.pcap" en formato pcap, que puede ser analizado posteriormente con herramientas como Wireshark. Este comando es útil para analizar el comportamiento de la red e identificar posibles amenazas a la seguridad.

### Estado del Proceso

El comando **ps** muestra información sobre los procesos en ejecución en un sistema Linux en la CLI, lo cual es útil para identificar procesos sospechosos que puedan estar ejecutándose en un sistema y potencialmente comprometer su seguridad. El comando puede mostrar un amplio rango de información sobre procesos en ejecución, incluyendo su ID de proceso (PID), usuario, uso de CPU y memoria, y nombre de comando.

Uno de los usos más básicos de ps es mostrar una lista de todos los procesos en ejecución en un sistema. Por ejemplo, para mostrar una lista de todos los procesos que se están ejecutando en el sistema, puede utilizar el siguiente comando:

```bash
$ ps aux
```

El comando anterior mostrará una lista de todos los procesos en ejecución en el sistema, junto con su PID, usuario, uso de CPU y memoria, y nombre del comando. Este comando es útil para obtener una visión general de los procesos que se ejecutan en un sistema e identificar cualquier proceso sospechoso que pueda estar ejecutándose.

Ps también se puede utilizar para mostrar información sobre un proceso específico o un conjunto de procesos. Por ejemplo, para mostrar información sobre un proceso con un PID específico (por ejemplo, PID 1234), puede utilizar el siguiente comando:

```bash
$ ps -p 1234
```

El comando anterior mostrará información sobre el proceso con PID 1234, incluyendo su usuario, uso de CPU y memoria, y nombre del comando. También puede mostrar información sobre un conjunto de procesos especificando varios PID.

Además de mostrar información sobre procesos en ejecución, ps también puede utilizarse para monitorizar el estado de los procesos en tiempo real. Por ejemplo, para monitorizar el uso de CPU y memoria de un proceso específico (por ejemplo, PID 1234) en tiempo real, puede utilizar el siguiente comando:

```bash
$ ps -p 1234 -o %cpu,%mem
```

El comando anterior mostrará el uso de CPU y memoria del proceso con PID 1234 en tiempo real, actualizando la salida cada segundo. Este comando es útil para monitorizar el rendimiento de procesos críticos e identificar posibles cuellos de botella en el rendimiento.

### Estadísticas de Red

El comando **netstat** muestra información sobre conexiones de red activas en un sistema Linux en la CLI, haciéndolo útil para identificar conexiones de red no autorizadas y potenciales amenazas de seguridad. El comando puede mostrar una amplia gama de información acerca de las conexiones de red activas, incluyendo las direcciones locales y remotas, el protocolo utilizado (por ejemplo, TCP, UDP), y el estado de la conexión.

Uno de los usos más básicos de netstat es mostrar una lista de todas las conexiones de red activas en un sistema. Por ejemplo, para mostrar una lista de todas las conexiones de red activas, puede utilizar el siguiente comando:

```bash
$ netstat -a
```


El comando anterior mostrará una lista de todas las conexiones de red activas en el sistema, junto con sus direcciones locales y remotas, el protocolo utilizado y el estado de la conexión. Este comando es útil para obtener una visión general de las conexiones de red activas en un sistema e identificar cualquier conexión no autorizada.

Netstat también se puede utilizar para mostrar información sobre conexiones de red para un protocolo específico (por ejemplo, TCP). Por ejemplo, para mostrar una lista de todas las conexiones TCP activas en el sistema, puede utilizar el siguiente comando:

```bash
$ netstat -at
```

El comando anterior mostrará una lista de todas las conexiones TCP activas en el sistema, junto con sus direcciones locales y remotas, y el estado de la conexión.

Además de mostrar información sobre las conexiones de red activas, netstat también se puede utilizar para mostrar estadísticas de red para un protocolo específico (por ejemplo, TCP). Por ejemplo, para mostrar estadísticas sobre todas las conexiones TCP del sistema, puede utilizar el siguiente comando:

```bash
$ netstat -st
```

El comando anterior mostrará estadísticas sobre todas las conexiones TCP del sistema, incluyendo el número de conexiones activas, el número de conexiones en cada estado y el número de errores que se han producido. Este comando es útil para monitorizar la salud general de la red e identificar posibles problemas de rendimiento.


### Buscar archivos

El comando **find** es usado para buscar archivos y directorios en un sistema Linux en el CLI, haciéndolo útil para localizar archivos y directorios específicos que pueden estar ocultos o ser difíciles de encontrar. El comando busca archivos y directorios basados en un amplio rango de criterios, incluyendo su nombre, tamaño, tiempo de modificación y permisos.

Uno de los usos más básicos de find es buscar archivos y directorios por su nombre. Por ejemplo, para buscar todos los archivos en el directorio actual y sus subdirectorios que tengan el nombre "ejemplo.txt", puede utilizar el siguiente comando:

```bash
$ find . -nombreejemplo.txt
```

El comando anterior buscará todos los archivos en el directorio actual y sus subdirectorios que tengan el nombre "ejemplo.txt", y mostrará su ruta completa.

Find también puede utilizarse para buscar archivos y directorios en función de su tamaño. Por ejemplo, para buscar todos los archivos del directorio actual y sus subdirectorios que tengan un tamaño superior a 1 MB, puede utilizar el siguiente comando:

```bash
$ find . -tamaño +1M
```

El comando anterior buscará todos los archivos del directorio actual y sus subdirectorios que tengan un tamaño superior a 1 MB, y mostrará su ruta completa.

Además de buscar archivos y directorios por nombre y tamaño, find también puede utilizarse para buscar archivos y directorios en función de su hora de modificación y permisos. Por ejemplo, para buscar todos los archivos del directorio actual y sus subdirectorios que se modificaron en los últimos 7 días, puede utilizar el siguiente comando:

```bash
$ find . -mtime -7
```

El comando anterior buscará todos los archivos del directorio actual y sus subdirectorios que hayan sido modificados en los últimos 7 días, y mostrará su ruta completa.

En general, el comando find es una poderosa herramienta para buscar archivos y directorios en un sistema Linux basándose en una amplia gama de criterios, haciéndolo útil para una variedad de tareas, incluyendo la administración de sistemas y la ciberseguridad.

______

Utilizar la línea de comandos de Linux para la ciberseguridad puede resultar abrumador para los principiantes. Sin embargo, con los comandos básicos y avanzados descritos en esta guía, puedes empezar a utilizar la CLI de Linux para tu ventaja en ciberseguridad. Recuerde tener precaución cuando ejecute comandos y entender bien lo que hace cada comando antes de usarlo.

Para aprender más sobre el uso de Linux para la ciberseguridad, echa un vistazo a la descarga del sistema operativo **[Kali Linux](https://www.kali.org/downloads/)**, que está diseñado específicamente para pruebas de penetración y forense digital.

## Conclusión

En conclusión, la interfaz de línea de comandos de Linux es una herramienta poderosa para los profesionales de la ciberseguridad, pero puede ser desalentadora para los principiantes. Aprendiendo los comandos básicos y avanzados descritos en esta guía, puedes empezar a usar la CLI de Linux para tu ventaja en ciberseguridad. Recuerda que siempre debes tener cuidado al ejecutar comandos y comprender a fondo lo que hace cada comando antes de usarlo. Con la práctica y la experiencia, puedes llegar a ser competente en el uso de la línea de comandos de Linux y llevar tus habilidades de ciberseguridad al siguiente nivel.