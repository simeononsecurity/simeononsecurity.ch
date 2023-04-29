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

 ## Introducción:
 
 Los ordenadores se han convertido en un aspecto crucial de nuestra vida cotidiana, y con ello, la necesidad de seguridad de los datos ha aumentado considerablemente. Entre los distintos métodos utilizados para proteger los datos en tránsito, SSL (Secure Socket Layer) y TLS (Transport Layer Security) son los protocolos más utilizados. Sin embargo, a medida que la tecnología evoluciona, las versiones anteriores de estos protocolos se vuelven vulnerables a los ciberataques. En este artículo hablaremos de las medidas a seguir para reactivar los ordenadores desactivando SSL y todas las versiones TLS 1.2 e inferiores para garantizar la seguridad de los datos.
 
 ### ¿Por qué desactivar SSL y TLS 1.2 e inferior?
 
 Las versiones antiguas de SSL y TLS son vulnerables a varias amenazas de seguridad como POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) y Heartbleed. Estos ataques pueden llevar a la exposición de información sensible, lo que hace crucial desactivar el uso de protocolos obsoletos.
 
 ### Désactivation de SSL et TLS 1.2 et inférieur sous Windows :
 
 En Windows, el proceso de desactivación de SSL y TLS 1.2 e inferior puede realizarse a través del editor de registro. Aquí tienes un script powershell para hacerlo:
 
 
 #### Desactivación de SSL y TLS 1.2 e inferior en Linux :
 
 En Linux, el proceso de desactivación de SSL y TLS 1.2 e inferior puede realizarse modificando el archivo de configuración OpenSSL. Estos son los pasos a seguir:
 
 1. Abre el terminal y conéctate como root.
 2. Accede al archivo de configuración de OpenSSL. En general, se encuentra en /etc/ssl/openssl.cnf.
 3. Ouvrez le fichier à l'aide d'un éditeur de texte tel que nano ou vim.
 4. Localiza la directiva SSLProtocol y define su valor en -TLSv1.2.
 5. Registra el archivo y ejecuta el editor de texto.
 6. Vuelva a marcar los servicios que utilicen OpenSSL, como Apache o Nginx, para que las modificaciones surtan efecto.
 
 ## Conclusión:
 
 Al desactivar SSL y todas las versiones 1.2 e inferiores de TLS, puedes reforzar la seguridad de tu ordenador y proteger la información sensible frente a ciberamenazas potenciales. Se trata de un proceso sencillo que puede llevarse a cabo con un esfuerzo mínimo, lo que constituye un aspecto esencial del mantenimiento de la seguridad de su ordenador. Poniendo en práctica las medidas descritas en este artículo, podrás proteger tus datos y prevenir los ciberataques, reduciendo así el riesgo de exposición de información sensible.
 
 Es importante tener en cuenta que si bien la desactivación de las versiones antiguas de los protocolos SSL y TLS puede mejorar la seguridad de tu ordenador, también puede afectar a la compatibilidad con algunos sistemas más antiguos. Por lo tanto, es esencial que pruebe minuciosamente las modificaciones realizadas y se asegure de que no tienen ningún impacto negativo en su sistema antes de llevarlas a cabo.
 
 En conclusión, reforzar su ordenador desactivando SSL y todas las versiones 1.2 e inferiores de TLS es una medida crítica para mantener la seguridad de la información sensible y prevenir los ciberataques. Las medidas descritas en este artículo proporcionan una guía sencilla para proteger su ordenador, lo que permite a particulares y organizaciones aplicar fácilmente las medidas de seguridad necesarias.