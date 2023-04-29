---
title: "Guía para principiantes: Uso de la línea de comandos de Linux para la ciberseguridad"
date: 2023-03-13
toc: true
draft: false
descripción: "Aprende a usar la línea de comandos de Linux para ciberseguridad con comandos básicos y avanzados".
tags: ["Linux", "Línea de comandos", "Ciberseguridad", "Guía para principiantes", "Escaneo de red", "Pruebas de vulnerabilidad", "Análisis de malware", "Permisos", "Tráfico de red", "Estado de procesos", "Estadísticas de red", "Búsqueda de archivos", "Wireshark", "TCPDump", "Nmap", "Linux CLI", "Seguridad", "Pruebas de penetración", "Forense digital"].
cover: "/img/cover/A_cartoon_illustration_of_a_person_wearing_a_hoodie.png"
coverAlt: "Ilustración de dibujos animados de una persona que lleva una sudadera con capucha, sentada frente a la pantalla de un ordenador con la interfaz de línea de comandos de Linux visible y sosteniendo una lupa para representar el aspecto de la ciberseguridad."
coverCaption: ""
---
```bash
$ pwd
/home/usuario
$ cd documentos
$ pwd
/home/usuario/documentos
```
```bash
$ ls documentos
archivo1.txt archivo2.pdf archivo3.docx
```
Bash
$ ls
Escritorio Documentos Descargas Música Imágenes Público Plantillas Vídeos
```
``bash
$ cd documentos
```
Bash
$ cd /usr/local/bin
```
Bash
$ cd ../..
```
```bash
$ cat archivo1.txt
```
```bash
$ cat fichero1.txt fichero2.txt fichero3.txt
```
``bash
$ cat *.txt
```
```bash
$ grep "error" logfile.txt
```
```bash
$ grep "p.*y" logfile.txt
```
```
4 = leer
2 = escribir
1 = ejecutar
```
```bash
$ chmod 644 archivo1.txt
```
```bash
$ chmod ug=rw,o= archivo2.txt
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
``bash
$ netstat -a
```
```bash
$ netstat -at
```
```bash
$ netstat -st
```
```bash
$ find . -nombre ejemplo.txt
```
```bash
$ find . -tamaño +1M
```
``bash
$ find . -mtime -7
```
  **Linux** es un sistema operativo potente y fácil de usar que, gracias a su naturaleza de código abierto, está muy presente en la industria cibernética. Sin embargo, para los principiantes es muy importante utilizar la interfaz de usuario de Linux (CLI) para realizar tareas de seguridad cibernética. Este manual proporcionará a los usuarios una visión general de las funciones inteligentes y mejoradas de Linux-CLI, que son útiles para las aplicaciones de seguridad cibernética. ## Grundlegende Linux-Befehle für Cybersicherheit ### Arbeitsverzeichnis drucken Der Befehl **pwd** (Arbeitsverzeichnis drucken) WIRD used, um das aktuelle Arbeitsverzeichnis in der CLI-Anzeige. El índice de tareas es el índice en el que se encuentra el sistema de dates. La función es útil para navegar por el sistema de dates y conocer su posición en relación con otras clasificaciones. Si, por ejemplo, se encuentra en la página de inicio y desea navegar por la página de documentos, SIE puede utilizar las siguientes funciones: Por ejemplo, Beispiel is. El segundo valor cambia la descripción en el índice de documentos, y el tercero muestra el índice de actividades actual, que ahora es el índice de documentos. ### Aufführen Der Befehl **ls** WIRD used, um den Inhalt eines Verzeichnisses in der CLI aufzulisten. La palabra clave muestra los nombres de los datos y las descripciones de la lista actual de tareas. Este campo es necesario para identificar los datos y las referencias en un lugar distinto. Si SIE desea, por ejemplo, visualizar el contenido de un documento, puede utilizar el siguiente código: Por ejemplo, el campo muestra el contenido de la ficha del documento, que contiene tres datos: Datei1.txt, Datei2.pdf y Datei3.docx. También puede utilizar el campo sin argumentos para ver el contenido de los documentos de trabajo actuales. Por ejemplo: En este ejemplo se muestra el contenido de la ficha Base, que contiene varias fichas como Escritorio, Documentos, Descargas, etc. ### Ändere die Richtung Der Befehl **cd** (change directory) WIRD used, um das aktuelle Arbeitsverzeichnis in der CLI zu ändern. Con esta palabra puede navegar por el sistema de dates y acceder a datos de diferentes lugares. Si, por ejemplo, desea introducir el nombre actual de la empresa en el registro de documentos, puede introducir el siguiente campo: Por ejemplo, el nombre actual de la empresa en el registro de documentos, que se encuentra en el nombre actual de la empresa. También puede utilizar un campo absoluto o relativo para añadir la ficha de actividad a una ficha que no esté incluida en la ficha de actividad actual. Por ejemplo: En el ejemplo anterior, el error cambia el directorio actual de tareas al directorio /usr/local/bin, que es un error absoluto. Alternativamente, puede utilizar un campo relativo para cambiar el índice de tareas. Por ejemplo: En el ejemplo anterior, el valor de la ficha de trabajo actual es dos veces mayor que el de la ficha de trabajo actual. La anotación ".." indica la tabla de tareas actual y puede utilizarse para navegar por la tabla de tareas. ### Verketten Der Befehl **cat** (concatenate) WIRD used, um den Inhalt Einer Datei in der CLI anzeigen. Este campo es necesario para visualizar datos basados en texto, como datos de protocolo o de configuración. Si, por ejemplo, desea visualizar el contenido de un archivo con el nombre "archivo1.txt", puede utilizar el siguiente campo: El ejemplo muestra el valor de la entrada "archivo1.txt". También puede utilizar el campo para obtener varios archivos y mostrar su contenido en la CLI. Por ejemplo: En este ejemplo se muestra el valor de tres archivos: archivo1.txt, archivo2.txt y archivo3.txt. También puede utilizar el cuadro de diálogo con indicadores de posición, para ver todos los datos que contenga una misma lista. Por ejemplo: En este ejemplo se muestra la entrada de todos los datos con la extensión ".txt" en el directorio actual de tareas. Este campo es útil para visualizar rápidamente el contenido de varios archivos, sin tener que rellenarlos uno a uno. ### Drucken mit globalen Ausdrücken Der Befehl **grep** (Global Regular Expression Print) WIRD used, um nach bestimmten Zeichenfolgen oder Mustern in einer Datei oder einem Satz von Dateien in der CLI zu suchen. El resultado no es necesario para identificar los campos de los archivos de protocolo o para obtener información de los archivos de configuración. Si SIE, por ejemplo, quiere encontrar un "error" en un archivo llamado "logfile.txt", puede utilizar el siguiente campo: Im Beispiel sucht der Befehl nach allen Vorkommen des Wortes "error" in der Datei "logfile.txt". ". ". ". " y muestra los valores de error en la CLI. También puede utilizar el campo con pulsaciones regulares para cumplir con los requisitos más complejos. Si, por ejemplo, SIE desea utilizar todas las posiciones que contienen una palabra que comienza con "p" y termina con "y", SIE puede utilizar el siguiente valor: Por ejemplo, el resultado en la date "logfile.txt" en todas las zonas que contienen una palabra que comienza con "p" y termina con "y". El carácter "p.*y" se aplica a todas las secuencias que comienzan con "p" y terminan con "y", con un gran número de secuencias entre ellas. Este resultado es útil para encontrar datos en protocolos que puedan ayudar a identificar problemas de seguridad o de funcionamiento. ### Modus ändern La palabra **chmod** (Modus ändern) se utiliza para cambiar los parámetros de un archivo o una tabla en la CLI. Este campo es importante para garantizar la seguridad y el control de los datos y las fichas de usuario. Los derechos de acceso se definen mediante tres marcadores, que sólo pueden ser utilizados por el usuario, el grupo y otras personas. Die Ziffern werden nach nachfolgender Formel berechnet: Si SIE erteilen beispielsweise dem Eigentümer Lese- und Schreibberechtigungen und der Gruppe und anderen nur Leseberechtigungen für eine Datei mit dem Namen "file1.txt", can SIE den following use: Im Beispiel setzt der Befehl die Berechtigungen der Datei "file1.txt" auf 644. La primera cifra (6) indica las características de lectura y escritura para el usuario (4 + 2 = 6). El segundo marcador (4) indica las responsabilidades del grupo que ha sido seleccionado. El segundo marcador (4) indica las opciones para otros grupos, que también están seleccionados. También puede utilizar el botón con las teclas para cambiar las opciones. Si, por ejemplo, el usuario, el grupo de usuarios y otros usuarios no tienen ninguna contraseña para un archivo con el nombre "archivo2.txt", puede utilizar la siguiente contraseña: En el primer ejemplo, el campo define las opciones del archivo "file2.txt" como ug=rw,o=, donde "ug" indica el nombre del usuario y del grupo, "r" indica la opción de lectura y "w" indica la opción de escritura. El símbolo "=" significa "las opciones están disponibles" y "o=" significa "todas las opciones están disponibles para otros". Este valor es necesario para controlar el acceso a datos verticales y verificaciones y para evitar el acceso no autorizado. ## Erweiterte Linux-Befehle für Cybersicherheit ### Netzwerk-Mapper El código **nmap** es una herramienta muy útil para escanear redes en la CLI, con la que se pueden identificar hosts y un dominio en la red, así como posibles conexiones. El resultado puede ser una serie de técnicas de escaneo, entre las que se incluyen el escaneo de host, el escaneo de puertos y el escaneo de sistemas operativos. Una de las aplicaciones principales de nmap es el escaneo de una dirección IP o un host. Para escanear, por ejemplo, una dirección IP (192.168.1.1) en puertos libres, SIE puede utilizar el siguiente comando: El anterior realiza un escaneo TCP-SYN de la IP de destino y obtiene una lista de los puertos desactivados. La tabla muestra los puertos desconectados junto con el nombre de dominio, el estado de cada puerto (desconectado/desconectado) e información adicional como el sistema de la empresa que está conectado a la red. Nmap también puede usarse para escanear varios hosts o direcciones IP a la vez. Para escanear, por ejemplo, un grupo de direcciones IP (192.168.1.1-255) en puertos libres, puede utilizar el siguiente campo: Esta opción escanea todas las direcciones IP de la zona y muestra los puertos y dispositivos disponibles para cada zona. Además del escaneo simple de host y el escaneo de puertos, nmap también puede realizar escaneos adicionales, como por ejemplo, escaneo de direcciones y versiones, escaneo de sistemas de bibliotecas y escaneo de etiquetas. Estos escaneos pueden ser útiles para identificar posibles fallos de seguridad en una red y protegerla de posibles ataques. ### TCP-Paket-Dumper Der Befehl **tcpdump** WIRD verwendet, um den Netzwerkverkehr in der CLI zu erfassen und zu analysieren, war ihn für die Fehlerbehebung bei Netzwerkproblemen, die Analyse des Netzwerkverhaltens und die Identifizierung potenzieller Sicherheitsbedrohungen nützlich. La función de filtrado de paquetes en tiempo real permite filtrar paquetes basándose en varios criterios, como la dirección IP, el protocolo y el puerto. Uno de los usos más comunes de tcpdump es la captura de datos de red en un punto distinto. Para obtener, por ejemplo, el tráfico de datos actual de la conexión eth0, el SIE puede utilizar el siguiente valor: Este campo muestra todos los paquetes de la red eth0 y los muestra en tiempo real en la CLI. La tabla muestra las direcciones IP de origen y destino, el protocolo y otra información de cada paquete. Tcpdump también puede usarse para filtrar paquetes según distintos criterios. Para obtener, por ejemplo, todos los paquetes que se envían a una dirección IP diferente o que se envían desde una dirección IP diferente, SIE puede utilizar el siguiente campo: Este campo muestra todos los paquetes que se envían a la dirección IP 192.168.1.1 o desde ella, y los muestra en tiempo real en la CLI. También puede filtrar paquetes basándose en el protocolo (p. ej. TCP, UDP), el número de puerto u otros criterios. Además de la captura de paquetes en tiempo real, tcpdump también puede ser utilizado para la captura de paquetes en una base de datos para su posterior análisis. Por ejemplo, para capturar todos los paquetes de la conexión eth0 y guardarlos en un archivo llamado "capture.pcap", puede utilizar el siguiente campo: La primera captura todos los paquetes de la conexión eth0 y los guarda en el archivo "capture .pcap" en formato pcap, que luego puede ser analizado con herramientas como Wireshark. Este resultado es útil para analizar la red e identificar posibles problemas de seguridad. ### Prozessstatus Der Befehl **ps** zeigt Informationen über laufende Prozesse auf Linux-System in der CLI an, was nützlich ist, um verdächtige Prozesse zu identifizieren, die möglicherweise auf einem System ausgeführt werden und möglicherweise dessen Sicherheit gefährden. El indicador puede mostrar una gran cantidad de información sobre los procesos en curso, como su ID de proceso (PID), la duración de la batería, la CPU y la velocidad, así como el nombre del proceso. Una de las principales aplicaciones del ps es la visualización de una lista de todos los procesos en curso en un sistema. Para visualizar, por ejemplo, una lista de todos los procesos que se están ejecutando en el sistema, SIE puede utilizar el siguiente campo: Este valor muestra una lista de todos los procesos en ejecución en el sistema, junto con su PID, duración de los parámetros, de la CPU y de la velocidad, y el nombre del proceso. Este valor es necesario para obtener una visión general de los procesos estériles que se están ejecutando en un sistema, y para identificar los procesos residuales que pueden estar ejecutándose. Ps también puede utilizarse para obtener información sobre un proceso específico o una serie de procesos. Para obtener, por ejemplo, información sobre un proceso con un PID distinto (p. ej. PID 1234), SIE puede utilizar el siguiente campo: El resultado muestra información sobre un proceso con el PID 1234, como por ejemplo el nombre del usuario, la duración de la CPU y del procesador y el nombre del proceso. También puede ver información de una serie de procesos, aunque no tenga varios PIDs. Además de la visualización de la información de los procesos en curso, ps también puede mostrar el estado actual de los procesos. Para comprobar, por ejemplo, la duración de la CPU y de la velocidad de un proceso determinado (p. ej. PID 1234) en tiempo real, el SIE puede mostrar el siguiente mensaje: La siguiente muestra la duración de la CPU y de la velocidad del proceso con el PID 1234 en tiempo real y actualiza la configuración cada semana. Este resultado es útil para superar el rendimiento de procesos críticos e identificar posibles problemas de rendimiento. ### Netzwerkstatistik El campo **netstat** muestra información sobre las conexiones de red activas en el sistema Linux en la CLI y es útil para identificar conexiones de red no detectadas y posibles problemas de seguridad. El mensaje puede mostrar una gran cantidad de información sobre las conexiones de red activas, incluyendo las direcciones locales y las más lejanas, los protocolos utilizados (p. ej. TCP, UDP) y el estado de la conexión. Una de las aplicaciones más comunes de netstat es la visualización de una lista de todas las conexiones de red activas en un sistema. Para obtener, por ejemplo, una lista de todas las conexiones de red activas, puede utilizar SIE: El resultado muestra una lista de todas las conexiones de red activas en el sistema junto con sus direcciones locales y remotas, el protocolo utilizado y el estado de la conexión. Este valor es útil para obtener una visión general de las conexiones de red activas en un sistema y para identificar conexiones no válidas. Netstat también puede usarse para obtener información sobre las conexiones de red de un protocolo específico (por ejemplo, TCP). Para ver, por ejemplo, una lista de todas las conexiones TCP activas en el sistema, SIE puede utilizar el siguiente campo: Esta opción muestra una lista de todas las conexiones TCP activas en el sistema junto con sus direcciones locales y lejanas y el estado de la conexión. También se puede utilizar netstat para obtener información sobre las conexiones de red activas, con el fin de obtener estadísticas de red para un protocolo específico (por ejemplo, TCP). Para obtener, por ejemplo, estadísticas sobre todas las conexiones TCP del sistema, puede utilizar el SIE con el siguiente valor: El siguiente valor muestra las estadísticas de todas las conexiones TCP del sistema, incluyendo el número de conexiones activas, el número de conexiones en cada estado y el número de errores detectados. Este error es necesario para comprobar el estado de la red e identificar posibles problemas de funcionamiento. ### Dateien suchen Der Befehl **find** WIRD used, um auf Linux-System in der CLI nach Dateien und Verzeichnissen zu suchen, wodurch er nützlich ist, um bestimmte Dateien und ein Verzeichnisse zu finden, sterben möglicherweise versteckt oder schwer zu finden sind. El resultado se obtiene mediante una serie de criterios basados en datos y referencias, como el nombre, el tamaño, la antigüedad y las características. Una de las principales aplicaciones de Buscar es la búsqueda de datos y fichas por nombre. Para buscar, por ejemplo, todos los datos de la lista actual y sus equivalentes que tengan el nombre "ejemplo.txt", puede utilizar el siguiente campo: El resultado busca todos los datos de la lista actual y sus equivalentes con el nombre "ejemplo.txt" y muestra su campo completo. Find también se puede utilizar para buscar datos y archivos basándose en su tamaño. Para buscar, por ejemplo, todos los datos de la lista actual y sus equivalentes que pesen más de 1 MB, puede utilizar el siguiente campo: El resultado obtenido muestra todos los datos de la lista actual y sus archivos no almacenados que pesen más de 1 MB, así como su campo completo. Además de la búsqueda de datos y fichas por nombre y tamaño, también se puede utilizar para buscar datos y fichas en función de su antigüedad y sus derechos. Por ejemplo, para buscar todos los datos de la lista actual y sus referencias anteriores que se hayan modificado en los últimos 7 días, el SIE puede obtener el siguiente valor: El resultado corresponde a todos los datos de la lista actual y a sus referencias, que han cambiado en los últimos 7 días, y muestra su posición completa. Además, Find-Befehl es una herramienta de búsqueda de datos y archivos en un sistema Linux basada en una serie de criterios, lo que la hace útil para una gran variedad de tareas, como la administración de sistemas y la seguridad cibernética. ______ El uso de la interfaz Linux para la seguridad cibernética puede resultar difícil para los principiantes. Con los ejemplos básicos y ampliados descritos en este manual puede comenzar a utilizar Linux-CLI para su seguridad cibernética. Por favor, tenga en cuenta que cuando se utilicen los comandos, debe tener en cuenta las funciones de cada uno de ellos antes de utilizarlos. Para obtener más información sobre el uso de Linux para la seguridad cibernética, consulte el sistema operativo **[Kali Linux](https://www.kali.org/downloads/)**, desarrollado especialmente para pruebas de penetración y detección digital. ## Fazit Zusammenfassend lässt sich sagen, dass die Linux-Befehlszeilenschnittstelle ein leistungsstarkes Tool für Cybersicherheitsexperten ist, für Anfänger jedoch entmutigend sein kann. Si aprende los conceptos básicos y ampliados que se describen en este manual, podrá utilizar la herramienta Linux-Befehlszeilenschnittstelle como su herramienta para la seguridad cibernética. Tenga en cuenta que la utilización de las funciones requiere una visión general y que las funciones de cada una de las funciones se deben conocer antes de utilizarlas. Con la experiencia y el conocimiento adquiridos, podrá mejorar su experiencia con Linux y llevar su ciberseguridad a la siguiente fase.