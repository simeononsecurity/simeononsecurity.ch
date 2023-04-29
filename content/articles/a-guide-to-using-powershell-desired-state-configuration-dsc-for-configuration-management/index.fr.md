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


 **Guía de uso de PowerShell Desired State Configuration (DSC) para la gestión de la configuración**.
 
 ______
 
 ## Introducción
 
 PowerShell Desired State Configuration (**DSC**) es una herramienta potente y **esencial** para administradores informáticos y profesionales DevOps, que les permite automatizar el despliegue y la configuración de sistemas Windows y Linux. Este artículo ofrece una guía completa sobre el uso de PowerShell DSC para la gestión de la configuración, incluyendo las mejores prácticas, las regulaciones gubernamentales y referencias útiles.
 
 ______
 
 ## Primeros pasos con la configuración del estado deseado de PowerShell
 
 ### ¿Qué es la configuración de estado deseada de PowerShell?
 
 PowerShell Desired State Configuration (**DSC**) es un **langage declarativo** integrado en PowerShell que permite a los administradores automatizar la configuración de sistemas, aplicaciones y servicios. Proporciona una forma **estándar y coherente** de realizar las configuraciones y garantizar que los sistemas permanecen en el estado deseado.
 
 ### Instalación de PowerShell DSC
 
 Para trabajar con PowerShell DSC, debes instalar **Windows Management Framework (WMF)**. WMF es un paquete que incluye PowerShell, DSC y otras herramientas de gestión esenciales. Puedes descargar la última versión de WMF desde el [Centro de descarga de Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=54616).
 
 ______
 
 ## Creación y aplicación de configuraciones DSC
 
 ### Écrire des configurations DSC
 
 Una configuración DSC es un **script PowerShell** que describe el estado deseado de un sistema. Se compone de una o varias **fuentes DSC** que muestran los parámetros y propiedades que necesitan los componentes del sistema. Vea un ejemplo de configuración DSC simple que instala el rol de servidor Web (IIS) sobre un servidor Windows :
 
 ### Aplicación de configuraciones DSC
 Una vez que haya escrito una configuración DSC, puede aplicarla a un sistema cible con la ayuda del applet de comando **Start-DscConfiguration**. Comience compilando el script de configuración y ejecutándolo en PowerShell :
 
 
 Esto generará un archivo **MOF** (Managed Object Format) que contiene la configuración compilada. A continuación, aplique la configuración al sistema con ayuda del siguiente comando:
 
 
 ## Buenas prácticas para el uso de PowerShell DSC
 
 ### Modularice sus configuraciones
 
 Cree configuraciones **modulares y reutilizables** separando los diferentes componentes de su infraestructura en **fuentes DSC individuales**. Este enfoque le permite **mantener y evaluar** fácilmente sus configuraciones a medida que evoluciona su entorno.
 
 ### Utilizar el control de código fuente
 
 Guarda siempre tus configuraciones DSC y tus recursos personalizados en un **sistema de control de código fuente** como Git. Esta práctica te permite seguir las modificaciones, colaborar con tu equipo y volver fácilmente a las versiones anteriores de tus configuraciones en caso de necesidad.
 
 ### Pruebe su configuración
 
 El **test** es un aspecto crucial de la gestión de la configuración. Antes de admitir una configuración DSC, pruébala en un **entorno de no producción** para asegurarte de que funciona según lo previsto y de que no tiene ninguna consecuencia inesperada. También puedes utilizar herramientas como [Pester](https://github.com/pester/Pester) para probar automáticamente tus configuraciones DSC.
 
 ______
 
 ## Reglamentos y directivas gubernamentales
 
 ### Directivas NIST
 
 El Instituto Nacional de Estándares y Tecnología (NIST) proporciona directrices para la gestión de la configuración del sistema. En particular, la publicación [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) contiene una sección (CM-2) sobre las configuraciones de base, que es pertinente para el uso de DSC. Las directrices subrayan la importancia del mantenimiento, la vigilancia y el control de las modificaciones mejoradas en las configuraciones del sistema. PowerShell DSC puede ayudar a las organizaciones a cumplir estas directivas proporcionando una forma coherente y automática de gestionar las configuraciones del sistema.
 
 ### Ley Federal de Gestión de la Seguridad de la Información (FISMA)
 
 La ley federal sobre la gestión de la seguridad de la información [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) exige que las agencias federales pongan en marcha un marco completo para garantizar la eficacia de sus controles de seguridad de la información. La gestión de la configuración es un elemento clave de la conformidad FISMA, y PowerShell DSC puede desempeñar un papel esencial para ayudar a las organizaciones a responder a estas exigencias.
 ______
 
 ## Conclusión
 
 PowerShell Desired State Configuration (DSC) es una herramienta potente y flexible para automatizar el despliegue y la gestión de configuraciones de sistemas. Siguiendo las mejores prácticas y cumpliendo con las regulaciones gubernamentales, puede asegurarse de que los sistemas de su organización permanezcan en el estado deseado manteniendo la conformidad. No deje de utilizar parte de los recursos proporcionados en este artículo para mejorar su comprensión de PowerShell DSC y mejorar sus procesos de gestión de la configuración.
 ______
 
 ## Referencias
 
 - Documentación oficial de la configuración del estado deseado de PowerShell (DSC)](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
 - NIST SP 800-53 - Contrôles de sécurité et de confidentialité pour les systèmes d'information fédéraux et les organisations] (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
 - Ley federal sobre la gestión de la seguridad de la información (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
 - Pester - Marco de pruebas PowerShell](https://github.com/pester/Pester)
 - Guía del principiante sobre el uso del cifrado para la protección de datos](https://simeononsecurity.ch/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
 - Buenas prácticas para la instalación de correctivos de seguridad en Windows](https://simeononsecurity.ch/articles/best-practices-for-installing-security-patches-on-windows/)
 
 
 
 
