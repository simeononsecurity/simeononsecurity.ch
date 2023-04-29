---
title: "Beginner's Guide: Using Linux Command Line for Cybersecurity"
date: 2023-03-13
toc: true
draft: false
description: "Learn how to use Linux command line for cybersecurity with basic and advanced commands."
tags: ["Linux", "Command Line", "Cybersecurity", "Beginner's Guide", "Network Scanning", "Vulnerability Testing", "Malware Analysis", "Permissions", "Network Traffic", "Process Status", "Network Statistics", "File Search", "Wireshark", "TCPDump", "Nmap", "Linux CLI", "Security", "Penetration Testing", "Digital Forensics"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_wearing_a_hoodie.png"
coverAlt: "A cartoon illustration of a person wearing a hoodie, sitting in front of a computer screen with the Linux command line interface visible, and holding a magnifying glass to represent the cybersecurity aspect."
coverCaption: ""
---
```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```
```bash
$ ls documents
file1.txt file2.pdf file3.docx
```
```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```
```bash
$ cd documents
```
```bash
$ cd /usr/local/bin
```
```bash
$ cd ../..
```
```bash
$ cat file1.txt
```
```bash
$ cat file1.txt file2.txt file3.txt
```
```bash
$ cat *.txt
```
```bash
$ grep "error" logfile.txt
```
```bash
$ grep "p.*y" logfile.txt
```
```
4 = read
2 = write
1 = execute
```
```bash
$ chmod 644 file1.txt
```
```bash
$ chmod ug=rw,o= file2.txt
```
```bash
$ nmap 192.168.1.1
```
```bash
$ nmap 192.168.1.1-255
```
```bash
$ sudo tcpdump -i eth0
```
```bash
$ sudo tcpdump host 192.168.1.1
```
```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```
```bash
$ ps aux
```
```bash
$ ps -p 1234
```
```bash
$ ps -p 1234 -o %cpu,%mem
```
```bash
$ netstat -a
```
```bash
$ netstat -at
```
```bash
$ netstat -st
```
```bash
$ find . -name example.txt
```
```bash
$ find . -size +1M
```
```bash
$ find . -mtime -7
```
  **Linux** es un sistema operativo versátil y seguro que se usa mucho en la industria de la ciberseguridad debido a su naturaleza de código abierto. Sin embargo, puede ser desalentador para los principiantes usar la interfaz de línea de comandos (CLI) de Linux para realizar tareas de ciberseguridad. Esta guía tiene como objetivo proporcionar a los principiantes una descripción general de los comandos CLI de Linux básicos y avanzados que son útiles para fines de ciberseguridad. ## Comandos básicos de Linux para ciberseguridad ### Imprimir directorio de trabajo El comando **pwd** (directorio de trabajo de impresión) se usa para mostrar el directorio de trabajo actual en la CLI. El directorio de trabajo es el directorio donde se encuentra actualmente en el sistema de archivos. El comando es útil para navegar por el sistema de archivos y comprender su ubicación en relación con otros directorios. Por ejemplo, si está en el directorio de inicio y desea navegar en el directorio de documentos, puede usar los siguientes comandos: En el ejemplo anterior, el primer comando imprime el directorio de trabajo actual, que es el directorio de inicio. El segundo comando cambia el directorio al directorio de documentos y el tercer comando imprime el directorio de trabajo actual, que ahora es el directorio de documentos. ### lista El comando **ls** se usa para enumerar el contenido de un directorio en la CLI. El comando muestra los nombres de los archivos y directorios en el directorio de trabajo actual. El comando es útil para identificar los archivos y directorios en una ubicación específica. Por ejemplo, si desea ver el contenido del directorio de documentos, puede usar el siguiente comando: En el ejemplo anterior, el comando enumera el contenido del directorio de documentos, que contiene tres archivos: archivo1.txt, archivo2.pdf y archivo3.docx . También puede usar el comando sin ningún argumento para enumerar el contenido del directorio de trabajo actual. Por ejemplo: En el ejemplo anterior, el comando enumera el contenido del directorio de inicio, que contiene varios subdirectorios, como Escritorio, Documentos, Descargas, etc. ### Cambio de directorio El comando **cd** (cambiar directorio) se usa para cambiar el directorio de trabajo actual en la CLI. El comando le permite navegar por el sistema de archivos y acceder a archivos en diferentes horarios. Por ejemplo, si desea cambiar el directorio de trabajo actual al directorio de documentos, puede usar el siguiente comando: En el ejemplo anterior, el comando cambia el directorio de trabajo actual al directorio de documentos, que se encuentra en el directorio de trabajo actual. También puede usar el comando con una ruta absoluta o relativa para cambiar el directorio de trabajo a un directorio que no se encuentra en el directorio de trabajo real. Por ejemplo: En el ejemplo anterior, el comando cambia el directorio de trabajo actual al directorio /usr/local/bin, que es una ruta absoluta. Alternativamente, puede usar una ruta relativa para cambiar el directorio de trabajo. Por ejemplo: En el ejemplo anterior, el comando cambia el directorio de trabajo actual dos niveles por encima del directorio de trabajo actual. La notación ".." representa el directorio principal y puede usarla para navegar hacia arriba en el árbol de directorios. ### Concatenar El comando **cat** (concatenar) se usa para mostrar el contenido de un archivo en la CLI. El comando es útil para ver el contenido de archivos basado en texto, como archivos de registro o archivos de configuración. Por ejemplo, si desea ver el contenido de un archivo llamado "archivo1.txt", puede usar el siguiente comando: En el ejemplo anterior, el comando muestra el contenido del archivo "file1.txt". También puede usar el comando para concatenar varios archivos y mostrar su contenido en la CLI. Por ejemplo: En el ejemplo anterior, el comando muestra el contenido de tres archivos: archivo1.txt, archivo2.txt y archivo3.txt. También puede usar el comando con comodines para concatenar todos los archivos que coinciden con un patrón específico. Por ejemplo: En el ejemplo anterior, el comando muestra el contenido de todos los archivos que tienen una extensión ".txt" en el directorio de trabajo actual. Este comando es útil para ver rápidamente el contenido de varios archivos sin abrirlos individualmente. ### Impresión de expresiones regulares globales El comando **grep** (impresión de expresión regular global) se usa para buscar cadenas o patrones específicos en un archivo o conjunto de archivos en la CLI. El comando es útil para identificar patrones en archivos de registro o buscar información específica en archivos de configuración. Por ejemplo, si desea buscar todas las apariciones de la palabra "error" en un archivo llamado "logfile.txt", puede usar el siguiente comando: En el ejemplo anterior, el comando busca todas las apariciones de la palabra "error" en el archivo "logfile.txt" y muestra las líneas coincidentes en la CLI. También puede usar el comando con expresiones regulares para buscar patrones más complejos. Por ejemplo, si desea buscar todas las líneas que contienen una palabra que comienza con "p" y termina con "y", puede usar el siguiente comando: En el ejemplo anterior, el comando busca todas las líneas que contienen una palabra que comienza con "p" y termina con "y" en el archivo "logfile.txt". La expresión regular "p.*y" coincide con cualquier cadena que comience con "p" y termine con "y", con cualquier número de caracteres intermedios. Este comando es útil para encontrar patrones en los archivos de registro que pueden ayudar a identificar amenazas de seguridad o problemas de rendimiento. ### Modo de cambio El comando **chmod** (modo de cambio) se usa para cambiar los permisos de un archivo o directorio en la CLI. El comando es esencial para asegurar archivos y directorios y controlar quién tiene acceso a ellos. Los permisos están representados por tres dígitos que corresponden al propietario, grupo y otros, respectivamente. Los dígitos se calculan en base a la siguiente fórmula: Por ejemplo, si desea otorgar al propietario permisos de lectura y escritura y al grupo y a otros permisos de lectura en solitario para un archivo llamado "archivo1.txt", puede usar el siguiente comando: En el ejemplo anterior, el comando establece los permisos del archivo "file1.txt" en 644. El primer dígito (6) representa los permisos para el propietario, que son de lectura y escritura (4 + 2 = 6). El segundo dígito (4) representa los permisos para el grupo, que es de lectura en solitario. El tercer dígito (4) representa los permisos para otros, que también es de lectura en solitario. También puede usar el comando con letras para cambiar los permisos. Por ejemplo, si desea otorgar al propietario y al grupo permisos de lectura y escritura y a otros ningún permiso para un archivo llamado "archivo2.txt", puede usar el siguiente comando: En el ejemplo anterior, el comando establece los permisos del archivo "file2 .txt" en ug=rw,o=, donde "ug" representa el propietario y el grupo, "r" representa el permiso de lectura y "w" representa el permiso de escritura. . El signo "=" significa "establecer los permisos para" y "o=" significa "eliminar todos los permisos para otros". Este comando es útil para controlar el acceso a archivos y directorios confidenciales y evitar el acceso no autorizado. ## Comandos avanzados de Linux para ciberseguridad ### Mapeador de rojo El comando **nmap** es una poderosa herramienta de escaneo de red en la CLI que se puede usar para identificar hosts y servicios en una red, así como también posibles vulnerabilidades . El comando puede realizar una variedad de técnicas de escaneo, incluido el descubrimiento de hosts, el escaneo de puertos y la detección del sistema operativo. Uno de los usos más básicos de nmap es escanear una sola dirección IP o host. Por ejemplo, para escanear una sola dirección IP (192.168.1.1) en busca de puertos abiertos, puede usar el siguiente comando: El comando anterior ejecutará un escaneo TCP SYN contra la IP de destino y devolverá una lista de puertos abiertos. El resultado muestra los puertos abiertos junto con el servicio que se ejecuta en cada puerto, el estado del puerto (abierto/cerrado) y, a veces, información adicional, como el sistema operativo que se ejecuta en el destino. Nmap también se puede usar para escanear múltiples hosts o direcciones IP a la vez. Por ejemplo, para escanear un rango de direcciones IP (192.168.1.1-255) en busca de puertos abiertos, puede usar el siguiente comando: El comando anterior escaneará todas las direcciones IP en el rango y devolverá los puertos y servicios abiertos para cada objetivo . Además del descubrimiento básico de hosts y el escaneo de puertos, nmap también puede realizar escaneos más avanzados, como detección de servicios y versiones, detección de sistemas operativos y escaneo de vulnerabilidades. Estos escaneos pueden ser útiles para identificar posibles vulnerabilidades de seguridad en una red y protegerla de posibles ataques. ### Descargador de paquetes TCP El comando **tcpdump** se usa para capturar y analizar el tráfico de red en la CLI, lo que lo hace útil para solucionar problemas de red, analizar el comportamiento de la red e identificar posibles amenazas de seguridad. El comando captura paquetes en tiempo real y puede filtrarlos según varios criterios, como la dirección IP, el protocolo y el puerto de origen o destino. Uno de los usos más básicos de tcpdump es capturar todo el tráfico de red en una interfaz específica. Por ejemplo, para capturar todo el tráfico en la interfaz eth0, puede usar el siguiente comando: El comando anterior capturará todos los paquetes en la interfaz eth0 y los mostrará en tiempo real en la CLI. La salida mostrará las direcciones IP de origen y destino, el protocolo y otra información sobre cada paquete. Tcpdump también se puede usar para filtrar paquetes según varios criterios. Por ejemplo, para capturar todos los paquetes enviados hacia o desde una dirección IP específica, puede usar el siguiente comando: El comando anterior capturará todos los paquetes enviados hacia o desde la dirección IP 192.168.1.1 y los mostrará en tiempo real en la CLI. También puede filtrar paquetes según el protocolo (por ejemplo, TCP, UDP), el número de puerto u otros criterios. Además de capturar paquetes en tiempo real, tcpdump también se puede usar para capturar paquetes en un archivo para su análisis posterior. Por ejemplo, para capturar todos los paquetes en la interfaz eth0 y guardarlos en un archivo llamado "capture.pcap", puede usar el siguiente comando: El comando anterior capturará todos los paquetes en la interfaz eth0 y los guardará en el archivo "capture. pcap" en formato pcap, que se puede analizar más tarde con herramientas como Wireshark. Este comando es útil para analizar el comportamiento de la red e identificar posibles amenazas a la seguridad. ### Estado del proceso El comando **ps** muestra información sobre procesos en ejecución en un sistema Linux en la CLI, lo cual es útil para identificar procesos sospechosos que pueden estar ejecutándose en un sistema y pueden dañar su seguridad. El comando puede mostrar una amplia gama de información sobre los procesos en ejecución, incluida su ID de proceso (PID), el usuario, el uso de CPU y memoria, y el nombre del comando. Uno de los usos más básicos de ps es mostrar una lista de todos los procesos en ejecución en un sistema. Por ejemplo, para mostrar una lista de todos los procesos que se ejecutan en el sistema, puede usar el siguiente comando: El comando anterior muestra una lista de todos los procesos en ejecucion en el sistema, junto con su PID, usuario, uso de CPU y memoria, y nombre del comando. Este comando es útil para obtener una vista general de los procesos que se ejecutan en un sistema e identificar cualquier proceso sospechoso que pueda estar ejecutándose. Ps también se puede usar para mostrar información sobre un proceso específico o un conjunto de procesos. Por ejemplo, para mostrar información sobre un proceso con un PID específico (por ejemplo, PID 1234), puede usar el siguiente comando: El comando anterior muestra información sobre el proceso con PID 1234, incluido su usuario, el uso de CPU y memoria, y el nombre del comando. También puede mostrar información sobre un conjunto de procesos especificando varios PID. Además de mostrar información sobre procesos en ejecución, ps también se puede usar para monitorear el estado de los procesos en tiempo real. Por ejemplo, para monitorear el uso de CPU y memoria de un proceso específico (p. ej., PID 1234) en tiempo real, puede usar el siguiente comando: El comando anterior muestra el uso de CPU y memoria del proceso con PID 1234 en tiempo real, actualizando la salida cada segundo. Este comando es útil para monitorear el rendimiento de procesos críticos e identificar posibles cuellos de botella en el rendimiento. ### Estadísticas de la red El comando **netstat** muestra sobre conexiones de red activas en un sistema Linux en la CLI, lo que lo hace útil para identificar conexiones de red no autorizadas y posibles amenazas a la seguridad. El comando puede mostrar una amplia gama de información sobre las conexiones de red activas, incluidas las direcciones locales y remotas, el protocolo utilizado (por ejemplo, TCP, UDP) y el estado de la conexión. Uno de los usos más básicos de netstat es mostrar una lista de todas las conexiones de red activas en un sistema. Por ejemplo, para mostrar una lista de todas las conexiones de red activas, puede usar el siguiente comando: El comando anterior muestra una lista de todas las conexiones de red activas en el sistema, junto con sus direcciones locales y remotas, el protocolo utilizado y the state of the connection. Este comando es útil para obtener una vista general de las conexiones de red activas en un sistema e identificar cualquier conexión no autorizada. Netstat también se puede usar para mostrar información sobre las conexiones de red para un protocolo específico (por ejemplo, TCP). Por ejemplo, para mostrar una lista de todas las conexiones TCP activas en el sistema, puede usar el siguiente comando: El comando anterior muestra una lista de todas las conexiones TCP activas en el sistema, junto con sus direcciones locales y remotas, y el estado de la conexion. Además de mostrar información sobre conexiones de red activas, netstat también se puede usar para mostrar estadísticas de red para un protocolo específico (por ejemplo, TCP). Por ejemplo, para mostrar estadísticas sobre todas las conexiones TCP en el sistema, puede usar el siguiente comando: El comando anterior muestra estadísticas sobre todas las conexiones TCP en el sistema, incluida la cantidad de conexiones activas, la cantidad de conexiones en cada estado y la cantidad de errores que se han producido. Este comando es útil para monitorear el estado general de la red e identificar posibles problemas de rendimiento. ### Buscar archivos El comando **buscar** se usa para buscar archivos y directorios en un sistema Linux en la CLI, lo que lo hace útil para ubicar archivos y directorios específicos que pueden estar ocultos o ser difíciles de encontrar. El comando busca archivos y directorios en función de una amplia gama de criterios, incluidos su nombre, tamaño, tiempo de modificación y permisos. Uno de los usos más básicos de find es buscar archivos y directorios por nombre. Por ejemplo, para buscar todos los archivos en el directorio actual y sus subdirectorios que tienen el nombre "ejemplo.txt", puede usar el siguiente comando: El comando anterior buscará todos los archivos en el directorio actual y sus subdirectorios que tienen el nombre " ejemplo.txt" y muestra su ruta completa. Buscar también se puede usar para buscar archivos y directorios según su tamaño. Por ejemplo, para buscar todos los archivos en el directorio actual y sus subdirectorios que tienen más de 1 MB, puede usar el siguiente comando: El comando anterior buscará todos los archivos en el directorio actual y sus subdirectorios que tienen más de 1 MB, y mostrar su ruta completa. Además de buscar archivos y directorios por nombre y tamaño, buscar también se puede usar para buscar archivos y directorios en función de su tiempo de modificación y permisos. Por ejemplo, para buscar todos los archivos en el directorio actual y sus subdirectorios que fueron modificados. en los últimos 7 días, puede usar el siguiente comando: El comando anterior buscará todos los archivos en el directorio actual y sus subdirectorios que se modificaron en los últimos 7 días, y mostrará su ruta completa. En general, el comando de búsqueda es una herramienta poderosa para buscar archivos y directorios en un sistema Linux según una amplia gama de criterios, lo que lo hace útil para una variedad de tareas, incluida la administración del sistema y la ciberseguridad. ______ El uso de la línea de comandos de Linux para la ciberseguridad puede resultar abrumador para los principiantes. Sin embargo, con los comandos básicos y avanzados descritos en esta guía, puede comenzar a utilizar la CLI de Linux para su ventaja en ciberseguridad. Recuerde tener cuidado al ejecutar comandos y comprender a fondo lo que hace cada comando antes de usarlo. Para obtener más información sobre el uso de Linux para la ciberseguridad, descargue el sistema operativo **[Kali Linux](https://www.kali.org/downloads/)**, que está diseñado específicamente para pruebas de penetración y análisis forense digital. ## Conclusión En conclusión, la interfaz de línea de comandos de Linux es una herramienta poderosa para los profesionales de la ciberseguridad, pero puede ser abrumadora para los principiantes. Al aprender los comandos básicos y avanzados descritos en esta guía, puede comenzar a usar la CLI de Linux para su ventaja en ciberseguridad. Recuerde siempre tener cuidado al ejecutar comandos y comprender a fondo lo que hace cada comando antes de usarlo. Con práctica y experiencia, puede dominar el uso de la línea de comandos de Linux y llevar sus habilidades de ciberseguridad al siguiente nivel.