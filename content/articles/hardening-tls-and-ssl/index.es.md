---
title: "Refuerce la seguridad de su ordenador desactivando SSL y TLS 1.1 y anteriores"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "Desactive SSL y las versiones antiguas de TLS, manteniendo TLS 1.2 o posterior. El artículo cubre Schannel y .NET en Windows y los servicios de Linux."
tags: ['Refuerzo de la seguridad informática', 'Desactivación de SSL y TLS', 'Seguridad de los datos', 'POODLE', 'BEAST', 'Heartbleed', 'Editor del Registro de Windows', 'Configuración de OpenSSL en Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Un ordenador con un símbolo de candado que representa la seguridad de los datos"
coverCaption: ""
---

## Introducción:

Los ordenadores forman parte esencial de la vida diaria, y la necesidad de proteger los datos también ha aumentado. SSL (Secure Socket Layer) y TLS (Transport Layer Security) protegen los datos en tránsito. Las versiones antiguas ahora son vulnerables a ataques. Este artículo explica cómo desactivar SSL y TLS 1.0 y 1.1, manteniendo TLS 1.2 o TLS 1.3 disponible.

*TLS 1.2 no es un protocolo obsoleto. La base mínima actual es TLS 1.2 o posterior. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) define TLS 1.3, mientras que [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) declara obsoletos TLS 1.0 y TLS 1.1.*

### ¿Por qué desactivar SSL y TLS 1.1 y anteriores?

Las versiones antiguas de SSL y TLS son vulnerables a amenazas como POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) y Heartbleed. Estos ataques pueden exponer información sensible. Heartbleed afectó a implementaciones vulnerables de OpenSSL, no era una versión del protocolo. Aplique el parche a la biblioteca y cambie las credenciales expuestas.

La [guía actual de Microsoft sobre el Registro de Schannel](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) enumera ajustes de protocolo para las versiones de Windows compatibles. Microsoft recomienda usar Directiva de grupo u otras herramientas de administración compatibles cuando estén disponibles. Edite el Registro directamente solo cuando no exista un control mejor.

### Desactivar SSL y TLS 1.1 y anteriores en Windows:

En Windows, puede desactivar estos protocolos mediante el Registro. El script de PowerShell cambia los ajustes de Schannel para cliente y servidor. También configura .NET para usar los valores TLS predeterminados del sistema operativo y criptografía segura.

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
# There is no DTLS 1.1 protocol. RFC 8996 deprecates DTLS 1.0 and retains DTLS 1.2.

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

#### Desactivar SSL y TLS 1.1 y anteriores en Linux:

En Linux, la forma de desactivar protocolos antiguos depende de la aplicación y la biblioteca. Modificar `/etc/ssl/openssl.cnf` no sustituye la configuración de cada daemon ni de las bibliotecas TLS incluidas. Siga estos pasos:

1. Abra el terminal e inicie sesión como root.
2. Vaya al archivo de configuración de OpenSSL. Normalmente está en /etc/ssl/openssl.cnf.
3. Abra el archivo con un editor de texto como nano o vim.
4. Busque la directiva de protocolo del servicio y establezca TLS 1.2 como mínimo. La instrucción antigua `-TLSv1.2` desactivaba TLS 1.2. No la use como mínimo actual.
5. Guarde el archivo y cierre el editor.
6. Reinicie los servicios que usan OpenSSL, como Apache o Nginx, para aplicar los cambios.

## Conclusión:

Desactivar SSL y TLS 1.1 y anteriores refuerza la seguridad del ordenador y mantiene la compatibilidad con clientes TLS modernos. El ajuste correcto pertenece al servicio que negocia la conexión TLS. Pruebe cada aplicación, sin suponer que un único archivo de OpenSSL controla todos los daemons.

Desactivar estas versiones antiguas puede afectar a la compatibilidad con algunos sistemas heredados. Pruebe los cambios a fondo y compruebe que no tengan efectos adversos antes de aplicarlos por completo.

Proteja la información sensible y reduzca el riesgo de ataques. Compruebe qué protocolo negocia cada servicio y documente las excepciones temporales.

## Lista de verificación actual

- **Confirme el protocolo negociado.** Pruebe el cliente y el servidor con un escáner TLS o una prueba interna aprobada en ambos extremos de la conexión.
- **Mantenga TLS 1.2 activado.** Algunas aplicaciones antiguas aún lo necesitan. El soporte de TLS 1.3 depende del sistema operativo y la biblioteca.
- **Revise DTLS por separado.** RFC 8996 declara obsoleto DTLS 1.0. No define un protocolo DTLS 1.1.
- **Reinicie los servicios afectados.** Los ajustes de Schannel y de las aplicaciones suelen requerir reiniciar el servicio o el sistema.
- **Documente las excepciones.** Registre cada endpoint antiguo que necesite temporalmente un ajuste de compatibilidad y asigne una fecha para retirarlo.
