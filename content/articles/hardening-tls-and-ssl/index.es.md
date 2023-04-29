---
title: "Hardening Your Computer's Security by Disabling SSL and TLS 1.2 and Below"
date: 2023-02-08
toc: true
draft: false
description: "This article discusses the steps to improve data security by disabling older versions of SSL and TLS protocols, which are vulnerable to cyber threats such as POODLE, BEAST, and Heartbleed, in Windows and Linux systems."
tags: ["Hardening computer security", "Disabling SSL and TLS", "Data security", "POODLE", "BEAST", "Heartbleed", "Windows registry editor", "Linux OpenSSL configuration", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "A computer with a padlock symbol representing data security"
coverCaption: ""
---
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
 ## Introducción:  Las computadoras se han convertido en un aspecto crucial de nuestra vida diaria y, con eso, la necesidad de seguridad de los datos ha crecido sustancialmente. Entre los diversos métodos utilizados para proteger los datos en tránsito, SSL (Secure Socket Layer) y TLS (Transport Layer Security) son protocolos muy utilizados. Sin embargo, a medida que la tecnología evoluciona, las versiones anteriores de estos protocolos se vuelven vulnerables a los ataques cibernéticos. En este artículo, discutiremos los pasos para fortalecer las computadoras al deshabilitar SSL y todas las versiones de TLS 1.2 e inferiores para mantener los datos seguros.  ### ¿Por qué deshabilitar SSL y TLS 1.2 y versiones anteriores?  Las versiones anteriores de SSL y TLS son vulnerables a varias amenazas de seguridad, como POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) y Heartbleed. Estos ataques pueden conducir a la exposición de información confidencial, por lo que es crucial deshabilitar el uso de protocolos obsoletos.  ### Deshabilitar SSL y TLS 1.2 y anteriores en Windows:  En Windows, el proceso de deshabilitar SSL y TLS 1.2 y anteriores se puede lograr a través del editor de registro. Aquí hay un script de PowerShell para realizar la tarea:   #### Deshabilitar SSL y TLS 1.2 y anteriores en Linux:  En Linux, el proceso de deshabilitar SSL y TLS 1.2 y anteriores se puede lograr modificando el archivo de configuración de OpenSSL. Estos son los pasos a seguir:  1. Abra la terminal e inicie sesión como root. 2. Navegue hasta el archivo de configuración de OpenSSL. Por lo general, se encuentra en /etc/ssl/openssl.cnf. 3. Abra el archivo con un editor de texto como nano o vim. 4. Localice la directiva SSLProtocol y establezca su valor en -TLSv1.2. 5. Guarde el archivo y cierre el editor de texto. 6. Reinicie los servicios que usan OpenSSL, como Apache o Nginx, para que los cambios surtan efecto.  ## Conclusión:  Al deshabilitar SSL y todas las versiones 1.2 e inferiores de TLS, puede fortalecer la seguridad de su computadora y proteger la información confidencial de posibles amenazas cibernéticas. Es un proceso simple que se puede lograr con un mínimo esfuerzo, lo que lo convierte en un aspecto crítico para mantener la seguridad de su computadora. Al implementar los pasos descritos en este artículo, puede mantener sus datos seguros y evitar ataques cibernéticos, lo que reduce el riesgo de exposición de información confidencial.  Es importante tener en cuenta que si bien deshabilitar estas versiones anteriores de los protocolos SSL y TLS puede mejorar la seguridad de su computadora, también puede afectar la compatibilidad con algunos sistemas más antiguos. Por lo tanto, es esencial probar exhaustivamente los cambios realizados y asegurarse de que no haya impactos adversos en su sistema antes de implementarlos por completo.  En conclusión, fortalecer su computadora al deshabilitar SSL y todas las versiones de TLS 1.2 e inferiores es un paso fundamental para mantener la seguridad de la información confidencial y prevenir ataques cibernéticos. Los pasos descritos en este artículo brindan una guía sencilla para proteger su computadora, lo que facilita que las personas y las organizaciones implementen las medidas de seguridad necesarias.