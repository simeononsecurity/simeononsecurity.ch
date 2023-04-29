---
title: "Endurece la seguridad de tu ordenador desactivando SSL y TLS 1.2 e inferiores"
date: 2023-02-08
toc: true
draft: false
description: "Este artículo analiza los pasos para mejorar la seguridad de los datos deshabilitando versiones antiguas de los protocolos SSL y TLS, vulnerables a ciberamenazas como POODLE, BEAST y Heartbleed, en sistemas Windows y Linux."
tags: ["Endurecimiento de la seguridad informática", "Deshabilitar SSL y TLS", "Seguridad de datos", "POODLE", "BEAST", "Heartbleed", "Editor del registro de Windows", "Configuración de OpenSSL en Linux", "Apache", "Nginx"]
cover: "/img/cover/Ordenador_con_un_símbolo_de_bloqueo_que_representa_la_seguridad_de_los_datos.png"
coverAlt: "Un ordenador con el símbolo de un candado que representa la seguridad de los datos"
coverCaption: ""
---
```powershell
Función Disable-Protocol {
    param (
        [Parámetro(Obligatorio=$true)]
        [cadena]$Protocolo
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocolo\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    Nuevo elemento -Ruta $RutaServidor -Forzar
    Nuevo-elemento -Ruta $RutaCliente -Forzar
    Set-ItemProperty -Ruta $RutaServidor -Forzar -Nombre Enabled -Tipo "DWORD" -Valor 0
    Set-ItemProperty -Ruta $RutaServidor -Force -Nombre DeshabilitadoPorDefecto -Tipo "DWORD" -Valor 1
    Set-ItemProperty -Ruta $RutaCliente -Force -Nombre Activado -Tipo "DWORD" -Valor 0
    Set-ItemProperty -Ruta $RutaCliente -Force -Nombre DesactivadoPorDefecto -Tipo "DWORD" -Valor 1
}
# Desactivar SSL v2
Disable-Protocol -Protocolo "SSL 2.0"
# Desactivar SSL v3
Desactivar-Protocolo -Protocolo "SSL 3.0" # Desactivar TLS 1.0
# Desactivar TLS 1.0
Desactivar-Protocolo -Protocolo "TLS 1.0" # Desactivar DTLS 1.0
# Desactivar DTLS 1.0
Desactivar-Protocolo -Protocolo "DTLS 1.0" # Desactivar TLS 1.1
# Desactivar TLS 1.1
Disable-Protocol -Protocolo "TLS 1.1" # Desactivar TLS 1.1
# Desactivar DTLS 1.1
Disable-Protocol -Protocol "DTLS 1.1" # Desactivar DTLS 1.1

function Set-NETStrongAuthentication {
    param(
        [cadena]$RegistryPath,
        [cadena]$Nombre,
        [cadena]$Tipo,
        [int]$Valor
    )
    Set-ItemProperty -Ruta $RegistryPath -Force -Nombre $Nombre -Tipo $Tipo -Valor $Valor
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version en $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

 ## Einführung:
 
 Los ordenadores son un aspecto muy importante de nuestra vida cotidiana, por lo que es muy importante mantener la seguridad de los datos. SSL (Secure Socket Layer) y TLS (Transport Layer Security) son protocolos ampliamente utilizados entre los distintos métodos de protección de datos durante la transmisión. Con el desarrollo de la tecnología, las versiones posteriores de estos protocolos serán aún más útiles para los ciberdelincuentes. En este artículo se describen los aspectos relacionados con la protección de los ordenadores mediante la activación de SSL y todas las versiones TLS 1.2 y posteriores, con el fin de garantizar la seguridad de los datos.
 
 ### Warum SSL und TLS 1.2 und darunter deaktivieren?
 
 Las versiones anteriores de SSL y TLS son responsables de varios problemas de seguridad, como POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) y Heartbleed. Estas amenazas pueden conducir a la ocultación de información sensible, si bien es posible que el uso de protocolos falsos resulte peligroso.
 
 ### Deaktivieren von SSL und TLS 1.2 und darunter in Windows:
 
 En Windows se puede activar la opción de desactivación de SSL y TLS 1.2 y más en el editor de registros. Aquí hay un Powershell-Skript, um die Aufgabe zu erfüllen:
 
 
 #### SSL und TLS 1.2 und darunter unter Linux deaktivieren:
 
 En Linux es posible activar SSL y TLS 1.2 y, más adelante, modificar los datos de configuración de OpenSSL. Estos son los siguientes puntos:
 
 1. 1. Abre el terminal y entra como root.
 2. 2. Navega hasta el directorio de configuración de OpenSSL. Normalmente se encuentra en /etc/ssl/openssl.cnf.
 3. 3. Abra el archivo con un editor de texto como nano o vim.
 4. Seleccione la opción SSLProtocol y establezca su valor en -TLSv1.2.
 5. 5. Introduzca los datos y cierre el editor de texto.
 6. 6. Inicie de nuevo los dispositivos que utilizan OpenSSL, como Apache o Nginx, para que se apliquen las modificaciones.
 
 ## Abschluss:
 
 Si desactiva SSL y todas las versiones TLS 1.2 y posteriores, podrá aumentar la seguridad de su ordenador y evitar posibles amenazas cibernéticas. Se trata de un proceso sencillo, que puede llevarse a cabo con un mínimo de esfuerzo, lo que lo convierte en un elemento clave para el mantenimiento de la seguridad de sus ordenadores. Mediante la aplicación de los criterios descritos en este artículo, podrá proteger sus datos y evitar riesgos cibernéticos, con lo que se reduce el riesgo de que se divulgue información confidencial.
 
 Es importante tener en cuenta que la desactivación de las versiones anteriores de los protocolos SSL y TLS no sólo puede mejorar la seguridad de su ordenador, sino también la compatibilidad con otros sistemas. Por lo tanto, es importante probar las modificaciones propuestas y asegurarse de que no afecten negativamente a su sistema antes de implementarlas por completo.
 
 Además, debe saber que la protección de su ordenador mediante SSL y todas las versiones TLS 1.2 y posteriores es un paso importante para garantizar la seguridad de la información confidencial y evitar ataques cibernéticos. Los puntos descritos en este artículo proporcionan una guía sencilla para la seguridad de sus ordenadores y ayudan a las personas y organizaciones a implementar las normas de seguridad necesarias.