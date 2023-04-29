---
title: "PowerShell DSC: Guía de inicio"
date: 2023-04-02
toc: true
draft: false
descripción: "Explora el poder de PowerShell Desired State Configuration (DSC) para automatizar y gestionar las configuraciones del sistema para un entorno seguro y compatible."
tags: ["PowerShell", "DSC", "Configuration Management", "Automation", "Windows", "System Administration", "Best Practices", "Compliance", "Security", "Infrastructure", "DevOps", "Server Configuration", "Testing", "Git", "Source Control", "Government Regulations", "NIST", "CIS", "Configuration Drift", "Custom Resources"]
cover: "/img/cover/A_cartoon_image_of_a_confident_system_administrator.png"
coverAlt: "Una imagen de dibujos animados de un administrador de sistemas seguro de sí mismo con una capa de superhéroe, de pie junto a un rack de servidores bien organizado, sosteniendo un script DSC de PowerShell en una mano y un escudo con el logotipo de Windows en la otra, protegiendo los servidores de la desviación de la configuración y las amenazas de seguridad."
coverCaption: ""
---
```powershell
Configuración InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Nodo 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Presente
            Name = 'Servidor Web
        }
    }
}
```
```powershell
InstallIIS
```
``powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```


 **Una guía para el uso de la Configuración de Estado Deseada (DSC) de PowerShell para la administración de configuraciones**.
 
 ______
 
 ## Introducción
 
 PowerShell Desired State Configuration (**DSC**) es una herramienta ligera y **esencial** para administradores de TI y expertos en DevOps, con la que pueden automatizar la creación y configuración de sistemas Windows y Linux. Este artículo contiene una guía completa sobre el uso de PowerShell DSC para la administración de configuraciones, incluyendo métodos conocidos, referencias útiles y recomendaciones.
 
 ______
 
 ## Erste Schritte mit der gewünschten PowerShell-Zustandskonfiguration
 
 ### ¿Qué es la configuración de estado deseado de PowerShell?
 
 La Configuración de Estado Deseado de PowerShell (**DSC**) es un **lenguaje descriptivo** de PowerShell, con el que los administradores pueden automatizar la configuración de sistemas, aplicaciones y dispositivos integrados. Ofrece una posibilidad **estándar y consistente** de realizar configuraciones y garantizar que los sistemas se encuentran en el estado deseado.
 
 ### Instalación de PowerShell DSC
 
 Para comenzar con PowerShell DSC, debe instalar **Windows Management Framework (WMF)**. WMF es un paquete que contiene PowerShell, DSC y otras herramientas de administración importantes. Puede descargar la última versión de WMF en [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=54616).
 
 ______
 
 ## Erstellen und Anwenden von DSC-Konfigurationen
 
 ### Schreiben von DSC-Konfigurationen
 
 Una Configuración DSC es un **Script PowerShell** que define el estado deseado de un Sistema. Se basa en uno o varios **Recursos DSC**, que definen las configuraciones y características necesarias para los componentes del sistema. Este es un ejemplo de una configuración DSC fácil de instalar, que combina la función de servidor web (IIS) en un servidor Windows:
 
 ### Anwenden von DSC-Konfigurationen
 Si ha creado una configuración DSC, puede utilizar SIE SIE con el comando **Start-DscConfiguration** en un sistema. Comience a compilar la configuración de los scripts mientras la ejecuta en PowerShell:
 
 
 A continuación, se generará un archivo **MOF** (Managed Object Format) que contiene la configuración compilada. Como primer paso, seleccione la configuración con el siguiente icono en el sistema:
 
 
 ## Best Practices für die Verwendung von PowerShell DSC
 
 ### Modularize Sie Ihre Konfigurationen
 
 Establezca configuraciones **modulares y con capacidad de modificación**, para poder integrar los distintos componentes de su infraestructura en **recursos DSC independientes**. Con este método, podrá **configurar y desconfigurar** fácilmente su entorno.
 
 ###Quellcodeverwaltung verwenden
 
 Guarde sus configuraciones DSC y los recursos definidos por el usuario en un **sistema de gestión de versiones** como Git. De este modo, podrá realizar cambios en su SIE, colaborar con su equipo y, sin problemas, volver a las versiones originales de sus configuraciones.
 
 ### Pruebe su configuración
 
 **Las pruebas son un aspecto importante de la gestión de la configuración. Pruebe una configuración DSC antes de guardarla en una **Configuración de No Conformidad** para asegurarse de que funciona tal y como se ha configurado y de que no tiene efectos no deseados. También puede utilizar herramientas como [Pester](https://github.com/pester/Pester) para comprobar automáticamente la configuración de su DSC.
 
 ______
 
 ## Reglas y directrices de seguridad
 
 ### NIST-Richtlinien
 
 El Instituto Nacional de Estándares y Tecnología (NIST) ofrece directrices para la gestión de la configuración de sistemas. En particular, la publicación [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) incluye un capítulo (CM-2) sobre configuraciones básicas, que es relevante para el uso de DSC. Las directrices se refieren a la importancia de la gestión, supervisión y control de los cambios en la configuración del sistema. PowerShell DSC puede ayudar a las empresas en el uso de estas directrices, ya que ofrece una forma automatizada y consistente de gestionar las configuraciones del sistema.
 
 ### Bundesgesetz über das Informationssicherheitsmanagement (FISMA) (Ley federal de gestión de la seguridad de la información)
 
 La Ley Federal de Gestión de la Seguridad de la Información [FISMA] (https://www.dhs.gov/cisa/federal-information-security-modernization-act) exige a las autoridades federales la aplicación de una serie de normas para mejorar la eficacia de sus controles de seguridad de la información. La gestión de la configuración es uno de los componentes clave del cumplimiento de la FISMA, y PowerShell DSC puede desempeñar un papel importante para ayudar a las organizaciones a cumplir estos requisitos.
 ______
 
 ## Inicio
 
 PowerShell Desired State Configuration (DSC) es una herramienta flexible y fácil de usar para automatizar la creación y gestión de configuraciones del sistema. Si se aplican las mejores prácticas y se cumplen las directrices, podrá asegurarse de que el sistema de su empresa se encuentra en el estado deseado y de que se cumplen las directrices al mismo tiempo. No se olvide de utilizar los recursos descritos en este artículo para mejorar su uso de PowerShell DSC y sus procesos de configuración y administración.
 ______
 
 ## Verweise
 
 - Documentación oficial sobre la configuración de estado deseado (DSC) de PowerShell](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
 - NIST SP 800-53 - Sicherheits- und Datenschutzkontrollen für föderale Informationssysteme und Organisationen] (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
 - Ley Federal de Gestión de la Seguridad de la Información (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
 - Pester - Marco de pruebas PowerShell] (https://github.com/pester/Pester)
 - Anfängerleitfaden zur Verwendung von Verschlüsselung zum Datenschutz](https://simeononsecurity.ch/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
 - Mejores prácticas para la instalación de parches de seguridad en Windows](https://simeononsecurity.ch/articles/best-practices-for-installing-security-patches-on-windows/)
 
 
 
 
