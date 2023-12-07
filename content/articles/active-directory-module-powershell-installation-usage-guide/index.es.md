---
title: "Dominio de la administración de Active Directory con PowerShell: Guía de instalación y uso"
date: 2023-07-25
toc: true
draft: false
description: "Descubra cómo instalar y utilizar eficazmente el módulo Active Directory para PowerShell con el fin de agilizar las tareas de administración de Active Directory de Windows."
genre: ["Tecnología", "Windows", "PowerShell", "Directorio Activo", "Administración", "Scripting", "TI", "Automatización", "Servidor Windows", "Microsoft"]
tags: ["módulo de directorio activo para PowerShell", "módulo de importación active directory en PowerShell", "módulo de directorio activo para Windows PowerShell", "instalación de Active Directory PowerShell", "instalar active directory PowerShell", "PowerShell instalar módulo de directorio activo Windows 10", "instalar directorio activo módulo PowerShell Windows 10", "obtener el módulo PowerShell de active directory", "Administración AD", "Directorio Activo de Windows", "Cmdlets de PowerShell", "recuperar información de AD", "crear objetos AD", "modificar objetos AD", "gestionar la seguridad de AD", "Gestión de usuarios AD", "Gestión de grupos AD", "AD O gestión", "Secuencias de comandos PowerShell", "Administración de Windows Server", "Microsoft PowerShell", "automatizar las tareas de AD", "Instalación del módulo PowerShell", "Guía de administración de AD", "Gestión de Active Directory", "Gestión de la seguridad de AD", "Automatización PowerShell", "Comandos PowerShell de Active Directory", "Referencia de cmdlet PowerShell"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Imagen que representa una red de servidores interconectados e iconos de usuario, símbolo de la gestión y automatización de Active Directory."
coverCaption: "Libere el poder de la administración de Active Directory con PowerShell."
---

## Introducción

En el panorama digital actual, la administración y el mantenimiento de cuentas de usuario, grupos de seguridad y otros recursos en un entorno de Active Directory (AD) de Windows requieren procesos eficientes y optimizados. PowerShell, un potente lenguaje de scripting desarrollado por Microsoft, ofrece el módulo **Active Directory** para facilitar las tareas de administración de AD. Este módulo proporciona una amplia gama de cmdlets que permiten a los administradores automatizar diversas operaciones y gestionar AD de forma eficaz. En este artículo, exploraremos la instalación y el uso del módulo Active Directory para PowerShell.

## Instalación del módulo Active Directory para PowerShell

Para empezar a utilizar el módulo Active Directory para PowerShell, debe asegurarse de que está instalado en su sistema. El proceso de instalación puede variar en función del sistema operativo. Estos son los pasos para instalar el módulo en **Windows 10**, **Windows 11** y **Windows Server**:

### Windows 10 y Windows 11 - PowerShell
1. Abra **Windows PowerShell** con privilegios de administrador.
2. Ejecute el siguiente comando para instalar el módulo:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Espere a que finalice la instalación. Una vez finalizada, puede empezar a utilizar el módulo Active Directory.

### Windows Server
1. Abra **Windows PowerShell** con privilegios de administrador.
2. Ejecute el siguiente comando para instalar el módulo:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Espere a que finalice la instalación. Una vez finalizada, puede empezar a utilizar el módulo Active Directory.

### Sistemas desconectados

Los sistemas sin conexión son un poco más complicados. Existen algunos métodos, sin embargo el que recomendamos es mediante el uso del siguiente script:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importar el módulo Active Directory en PowerShell

Antes de poder utilizar el módulo Active Directory en PowerShell, es necesario importarlo a la sesión actual. Siga estos pasos para importar el módulo:

1. Inicie **Windows PowerShell** con derechos administrativos.
2. Ejecute el siguiente comando para importar el módulo:

```powershell
Import-Module ActiveDirectory
```

3. El módulo Active Directory se importará y ahora podrá acceder a sus cmdlets y funciones.

## Uso del módulo Active Directory para PowerShell

Con el módulo Active Directory importado, puede aprovechar su rico conjunto de cmdlets para realizar varias tareas administrativas. Exploremos algunos cmdlets de uso común y sus funcionalidades:

### Recuperación de información de Active Directory

Para administrar eficazmente un entorno de Active Directory (AD), es crucial recuperar información sobre varios objetos de AD, como usuarios, grupos y unidades organizativas (OU). PowerShell proporciona potentes cmdlets que simplifican el proceso de recuperación.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) Este cmdlet le permite recuperar información detallada sobre los usuarios de AD. Puede obtener atributos como nombre de usuario, nombre para mostrar, dirección de correo electrónico y más. Por ejemplo, para recuperar todos los usuarios cuyos nombres de usuario empiecen por "johndoe", puede ejecutar el siguiente comando:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Este comando devolverá una lista de objetos de usuario que coincidan con el filtro especificado.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) Con el cmdlet Get-ADGroup, puede obtener información sobre los grupos de AD. Proporciona acceso a detalles como el nombre del grupo, miembros, descripción y más. Por ejemplo, para recuperar todos los grupos de seguridad en el entorno de AD, puede ejecutar el siguiente comando:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Esto proporcionará una lista de grupos de seguridad en el Directorio Activo.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) El cmdlet Get-ADOrganizationalUnit se utiliza para recuperar información sobre las OU de AD. Permite acceder a propiedades como el nombre de la OU, la descripción, la OU padre, etc. Para obtener todas las OUs del dominio, puede utilizar el siguiente comando:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Ejecutando este comando se mostrará una lista de todas las OUs en el Directorio Activo.

Utilizando estos potentes cmdlets, puede recuperar fácilmente información específica sobre usuarios, grupos y OUs de AD, permitiendo una administración y gestión eficientes de su entorno de Active Directory.


Estos cmdlets permiten recuperar atributos específicos, filtrar resultados y realizar consultas avanzadas para obtener la información deseada.

### Creación y gestión de objetos de Active Directory

Al trabajar con Active Directory (AD), el módulo Active Directory en PowerShell ofrece poderosos cmdlets para crear y administrar objetos AD. Exploremos algunos cmdlets esenciales para crear usuarios, grupos y unidades organizativas (OU) de AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) Este cmdlet le permite crear un nuevo usuario AD. Puede especificar atributos como el nombre de usuario, la contraseña, la dirección de correo electrónico, etc. Por ejemplo, para crear un nuevo usuario con el nombre de usuario "john.doe" y el nombre para mostrar "John Doe", puede utilizar el siguiente comando:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Este comando creará un nuevo usuario en el Directorio Activo.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) El cmdlet New-ADGroup permite crear un nuevo grupo AD. Puede establecer propiedades como el nombre del grupo, la descripción, el ámbito del grupo, etc. Para crear un nuevo grupo llamado "Marketing" con una descripción, puede ejecutar el siguiente comando:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Este comando creará un nuevo grupo en el Directorio Activo.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) Con el cmdlet New-ADOrganizationalUnit, puede crear una nueva OU de AD. Puede especificar propiedades como el nombre de la OU, la OU padre y más. Por ejemplo, para crear una nueva OU llamada "Ventas" bajo la OU "Departamentos", puede ejecutar el siguiente comando:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Este comando creará una nueva OU en la jerarquía de Active Directory.

Aprovechando estos cmdlets, puede crear fácilmente nuevos usuarios, grupos y OUs de AD con las propiedades y configuraciones deseadas, permitiendo una gestión eficiente de su entorno de Active Directory.


### Modificación de objetos de Active Directory

Cuando se trata de modificar las propiedades y atributos de objetos existentes de Active Directory (AD), el módulo de Active Directory en PowerShell proporciona varios cmdlets útiles. Exploremos estos cmdlets para modificar usuarios, grupos y unidades organizativas (OU) de AD.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) El cmdlet Set-ADUser permite modificar las propiedades de un usuario de AD. Puede actualizar atributos como el nombre para mostrar, la dirección de correo electrónico o el número de teléfono, entre otros. Por ejemplo, para cambiar el número de teléfono de un usuario con el nombre de usuario "john.doe", puede utilizar el siguiente comando:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Este comando modificará el número de teléfono del usuario especificado en el Directorio Activo.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) Con el cmdlet Set-ADGroup, puede modificar las propiedades de un grupo de AD. Puede actualizar atributos como la descripción del grupo, la pertenencia, el ámbito del grupo, etc. Para cambiar la descripción de un grupo denominado "Marketing" a "Equipo de Marketing", puede ejecutar el siguiente comando:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Este comando actualizará la descripción del grupo especificado en el Directorio Activo.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) El cmdlet Set-ADOrganizationalUnit permite modificar las propiedades de una OU de AD. Puede cambiar atributos como el nombre de la OU, la descripción, etc. Por ejemplo, para modificar la descripción de una OU llamada "Ventas" a "Departamento de Ventas", puede ejecutar el siguiente comando:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Este comando actualizará la descripción de la OU especificada en la jerarquía de Active Directory.

Utilizando estos cmdlets, puede modificar fácilmente las propiedades y atributos de los objetos de AD, realizando las actualizaciones y ajustes necesarios para satisfacer los requisitos de su organización.


### Managing Active Directory Security

Además de gestionar y administrar objetos de Active Directory (AD), el módulo Active Directory de PowerShell proporciona cmdlets específicamente diseñados para gestionar aspectos de AD relacionados con la seguridad. Estos cmdlets permiten a los administradores gestionar eficazmente el acceso de usuarios, la pertenencia a grupos y las tareas relacionadas con contraseñas dentro del entorno AD.

Éstos son algunos de los cmdlets relacionados con la seguridad más utilizados:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) Este cmdlet le permite añadir miembros a un grupo AD. Especificando el grupo AD y las cuentas de usuario o grupos que desea añadir, puede gestionar fácilmente el control de acceso. Por ejemplo, para añadir un usuario llamado "JohnDoe" al grupo "Managers", puede utilizar el siguiente comando:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) Con este cmdlet, puede eliminar miembros de un grupo de AD. Especificando el grupo de AD y las cuentas de usuario o grupos que desea eliminar, puede gestionar eficazmente la pertenencia a grupos. Por ejemplo, para eliminar un usuario llamado "JaneSmith" del grupo "Desarrolladores", puede utilizar el siguiente comando:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) Este cmdlet le permite establecer la contraseña de un usuario de AD. Al especificar la cuenta de usuario y proporcionar una nueva contraseña, puede aplicar políticas de contraseñas y garantizar una autenticación de usuario segura. A continuación se muestra un ejemplo de configuración de una nueva contraseña para un usuario llamado "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Utilizando estos cmdlets relacionados con la seguridad, los administradores pueden gestionar eficazmente el acceso de los usuarios, la pertenencia a grupos y las políticas de contraseñas en el entorno de Active Directory.

## Ejemplo de script de módulo de Active Directory para PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Conclusión

En conclusión, el módulo **Active Directory para PowerShell** es una potente herramienta que permite una gestión eficaz y cómoda de Windows Active Directory. Al instalar e importar el módulo, tendrá acceso a un completo conjunto de **cmdlets** que simplifican diversas tareas relacionadas con AD.

Con el módulo Active Directory, puede realizar una amplia gama de operaciones, como recuperar información sobre objetos AD, crear nuevos objetos, modificar propiedades y gestionar la seguridad. Este módulo permite a los administradores automatizar las tareas administrativas, agilizar los flujos de trabajo y garantizar el buen funcionamiento de los entornos de Active Directory.

Al aprovechar **PowerShell** y el módulo **Active Directory**, puede mejorar sus capacidades de administración de AD y mejorar la eficiencia de los procesos de administración de AD. Tanto si es administrador de sistemas, profesional de TI o gestor de Active Directory, el módulo Active Directory le proporciona las herramientas necesarias para gestionar eficazmente su infraestructura de AD.

Aproveche la potencia de **PowerShell** y el **módulo Active Directory** para agilizar sus tareas de administración de AD, aumentar la productividad y mantener un entorno Active Directory seguro y bien organizado.

## Referencias

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
