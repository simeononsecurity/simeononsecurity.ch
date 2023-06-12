---
title: "Refuerce la seguridad de su ordenador desactivando SSL y TLS 1.2 e inferiores"
date: 2023-02-08
toc: true
draft: false
description: "En este artículo se analizan los pasos para mejorar la seguridad de los datos desactivando las versiones antiguas de los protocolos SSL y TLS, vulnerables a ciberamenazas como POODLE, BEAST y Heartbleed, en sistemas Windows y Linux."
tags: ["Refuerzo de la seguridad informática", "Desactivación de SSL y TLS", "Seguridad de los datos", "POODLE", "BESTIA", "Heartbleed", "Editor del registro de Windows", "Configuración de OpenSSL en Linux", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "Un ordenador con el símbolo de un candado que representa la seguridad de los datos"
coverCaption: ""
---

## Introducción:

Los ordenadores se han convertido en un aspecto crucial de nuestra vida cotidiana y, con ello, la necesidad de seguridad de los datos ha crecido sustancialmente. Entre los diversos métodos utilizados para proteger los datos en tránsito, SSL (Secure Socket Layer) y TLS (Transport Layer Security) son protocolos muy utilizados. Sin embargo, a medida que la tecnología evoluciona, las versiones más antiguas de estos protocolos se están volviendo vulnerables a los ciberataques. En este artículo, vamos a discutir los pasos para endurecer los ordenadores mediante la desactivación de SSL y todas las versiones TLS 1.2 e inferiores para mantener los datos seguros.

### ¿Por qué desactivar SSL y TLS 1.2 e inferiores?

Las versiones antiguas de SSL y TLS son vulnerables a varias amenazas de seguridad como POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) y Heartbleed. Estos ataques pueden llevar a la exposición de información sensible, por lo que es crucial desactivar el uso de protocolos obsoletos.

### Deshabilitar SSL y TLS 1.2 e inferiores en Windows:

En Windows, el proceso de deshabilitar SSL y TLS 1.2 e inferiores se puede realizar a través del editor del registro. Aquí hay un script de powershell para realizar la tarea:

```powershell
Function Disable-Protocol {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Protocol
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    New-Item -Path $ServerPath -Force
    New-Item -Path $ClientPath -Force
    Set-ItemProperty -Path $ServerPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ServerPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
    Set-ItemProperty -Path $ClientPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ClientPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
}
# Disable SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Disable SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Disable TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Disable DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Disable TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# Disable DTLS 1.1
Disable-Protocol -Protocol "DTLS 1.1"

function Set-NETStrongAuthentication {
    param(
        [string]$RegistryPath,
        [string]$Name,
        [string]$Type,
        [int]$Value
    )
    Set-ItemProperty -Path $RegistryPath -Force -Name $Name -Type $Type -Value $Value
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version in $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

#### Desactivación de SSL y TLS 1.2 e inferiores en Linux:

En Linux, el proceso de deshabilitar SSL y TLS 1.2 e inferiores se puede conseguir modificando el fichero de configuración de OpenSSL. Estos son los pasos a seguir:

1. Abre el terminal e inicia sesión como root.
2. Navegue hasta el archivo de configuración de OpenSSL. Normalmente, se encuentra en /etc/ssl/openssl.cnf.
3. Abre el archivo utilizando un editor de texto como nano o vim.
4. Localice la directiva SSLProtocol y establezca su valor en -TLSv1.2.
5. Guarde el archivo y cierre el editor de texto.
6. 6. Reinicie los servicios que utilizan OpenSSL, como Apache o Nginx, para que los cambios surtan efecto.

## Conclusión:

Desactivando SSL y todas las versiones TLS 1.2 e inferiores, puedes reforzar la seguridad de tu equipo y proteger la información sensible de posibles ciberamenazas. Se trata de un proceso sencillo que puede llevarse a cabo con el mínimo esfuerzo, por lo que es un aspecto crítico para mantener la seguridad de tu ordenador. Al poner en práctica los pasos descritos en este artículo, puede mantener sus datos seguros y prevenir los ataques cibernéticos, reduciendo así el riesgo de que la información sensible quede expuesta.

Es importante tener en cuenta que, aunque deshabilitar estas versiones antiguas de los protocolos SSL y TLS puede mejorar la seguridad de tu ordenador, también puede afectar a la compatibilidad con algunos sistemas antiguos. Por lo tanto, es esencial probar a fondo los cambios realizados y asegurarse de que no hay impactos adversos en su sistema antes de implementarlos completamente.

En conclusión, reforzar su ordenador deshabilitando SSL y todas las versiones TLS 1.2 e inferiores es un paso fundamental para mantener la seguridad de la información confidencial y prevenir los ciberataques. Los pasos descritos en este artículo proporcionan una guía sencilla para proteger su ordenador, facilitando a particulares y organizaciones la aplicación de las medidas de seguridad necesarias.