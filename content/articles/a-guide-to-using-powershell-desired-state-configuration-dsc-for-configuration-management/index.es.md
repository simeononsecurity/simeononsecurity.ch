---
title: "PowerShell DSC: Guía de inicio"
date: 2023-04-02
toc: true
draft: false
description: "Explore el poder de PowerShell Desired State Configuration (DSC) para automatizar y gestionar las configuraciones del sistema para un entorno seguro y conforme."
tags: ["PowerShell", "DSC", "Gestión de la configuración", "Automatización", "Windows", "Administración del sistema", "Buenas prácticas", "Conformidad", "Seguridad", "Infraestructura", "DevOps", "Configuración del servidor", "Pruebas", "Git", "Control de las fuentes", "Normativa gubernamental", "NIST", "CIS", "Deriva de configuración", "Recursos personalizados"]
cover: "/img/cover/A_cartoon_image_of_a_confident_system_administrator.png"
coverAlt: "Una imagen de dibujos animados de un administrador de sistemas seguro de sí mismo con una capa de superhéroe, de pie junto a un bastidor de servidores bien organizado, sosteniendo un script DSC de PowerShell en una mano y un escudo con el logotipo de Windows en la otra, protegiendo los servidores de la deriva de la configuración y de las amenazas a la seguridad."
coverCaption: ""
---

**Guía de uso de la configuración de estados deseados (DSC) de PowerShell para la gestión de configuraciones**

______

## Introducción

PowerShell Desired State Configuration (**DSC**) es una herramienta potente y **esencial** para administradores de TI y profesionales de DevOps, que les permite automatizar el despliegue y la configuración de sistemas Windows y Linux. Este artículo proporciona una guía completa sobre el uso de PowerShell DSC para la gestión de la configuración, incluyendo las mejores prácticas, normas gubernamentales y referencias útiles.

______

## Primeros pasos con PowerShell Desired State Configuration

### ¿Qué es la configuración de estados deseados de PowerShell?

PowerShell Desired State Configuration (**DSC**) es un **lenguaje declarativo** integrado en PowerShell que permite a los administradores automatizar la configuración de sistemas, aplicaciones y servicios. Proporciona una forma **estandarizada y coherente** de gestionar las configuraciones y garantizar que los sistemas permanezcan en el estado deseado.

### Instalación de PowerShell DSC

Para empezar con PowerShell DSC, necesitará instalar el **Windows Management Framework (WMF)**. WMF es un paquete que incluye PowerShell, DSC y otras herramientas de gestión esenciales. Puedes descargar la última versión de WMF desde la página [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=54616)

______

## Creación y aplicación de configuraciones DSC

### Escribir Configuraciones DSC

Una configuración DSC es un **script PowerShell** que describe el estado deseado de un sistema. Consiste en uno o más **recursos DSC** que definen los ajustes y propiedades requeridos para los componentes del sistema. A continuación se muestra un ejemplo de una configuración DSC sencilla que instala el rol Servidor Web (IIS) en un servidor Windows:

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### Aplicación de configuraciones DSC
Una vez que haya escrito una configuración DSC, puede aplicarla a un sistema de destino utilizando el cmdlet **Start-DscConfiguration**. En primer lugar, compile el script de configuración ejecutándolo en PowerShell:

```powershell
InstallIIS
```

Esto generará un archivo **MOF** (Managed Object Format) que contiene la configuración compilada. A continuación, aplica la configuración al sistema de destino utilizando el siguiente comando:

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## Prácticas recomendadas para utilizar PowerShell DSC

### Modularice sus Configuraciones

Cree **configuraciones modulares y reutilizables** separando los distintos componentes de su infraestructura en **recursos DSC individuales**. Este enfoque le permite **mantener y escalar** fácilmente sus configuraciones a medida que crece su entorno.

### Use Source Control

Almacene siempre sus configuraciones DSC y recursos personalizados en un **sistema de control de fuentes** como Git. Esta práctica le permite realizar un seguimiento de los cambios, colaborar con su equipo y volver fácilmente a versiones anteriores de sus configuraciones cuando sea necesario.

### Pruebe sus configuraciones

**Las pruebas** son un aspecto crucial de la gestión de configuraciones. Antes de desplegar una configuración DSC, pruébela en un **entorno de no producción** para asegurarse de que funciona como se espera y no introduce ninguna consecuencia no deseada. También puede utilizar herramientas como [Pester](https://github.com/pester/Pester) para realizar pruebas automatizadas de sus configuraciones DSC.

______

## Normativa y directrices gubernamentales

### Directrices del NIST

El Instituto Nacional de Estándares y Tecnología (NIST) proporciona directrices para la gestión de la configuración de sistemas. En particular, el [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) publication contains a section (CM-2) sobre Configuraciones Base, que es relevante para el uso de DSC. Las directrices hacen hincapié en la importancia de mantener, supervisar y controlar los cambios en las configuraciones del sistema. PowerShell DSC puede ayudar a las organizaciones a cumplir estas directrices proporcionando una forma coherente y automatizada de gestionar las configuraciones del sistema.

### Ley Federal de Gestión de la Seguridad de la Información (FISMA)

Ley federal de gestión de la seguridad de la información [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) requiere que las agencias federales implementen un marco integral para garantizar la eficacia de sus controles de seguridad de la información. La gestión de la configuración es un componente clave del cumplimiento de FISMA, y PowerShell DSC puede desempeñar un papel esencial para ayudar a las organizaciones a cumplir estos requisitos.
______

## Conclusión

PowerShell Desired State Configuration (DSC) es una herramienta potente y flexible para automatizar el despliegue y la gestión de las configuraciones del sistema. Siguiendo las mejores prácticas y adhiriéndose a las normativas gubernamentales, puede asegurarse de que los sistemas de su organización permanezcan en el estado deseado mientras mantiene el cumplimiento. No olvide aprovechar los recursos proporcionados en este artículo para mejorar su comprensión de PowerShell DSC y mejorar sus procesos de gestión de la configuración.
______

## Referencias

- [PowerShell Desired State Configuration (DSC) official documentation](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - Security and Privacy Controls for Federal Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [Federal Information Security Management Act (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - PowerShell Testing Framework](https://github.com/pester/Pester)
- [A Beginner's Guide to Using Encryption for Data Protection](https://simeononsecurity.ch/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [Best Practices for Installing Security Patches on Windows](https://simeononsecurity.ch/articles/best-practices-for-installing-security-patches-on-windows/)




