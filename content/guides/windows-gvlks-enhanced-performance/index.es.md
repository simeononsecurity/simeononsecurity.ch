---
title: "Windows GVLKs: Desbloquear el poder de las claves de licencia para mejorar el rendimiento"
date: 2023-09-09
toc: true
draft: false
description: "Descubra cómo las GVLK de Windows revolucionan el rendimiento. Explore las mejores claves de licencia y aumente la productividad de su sistema sin esfuerzo."
genre: ["Tecnología", "Software", "Productividad", "Sistemas operativos", "Microsoft", "Windows", "Licencias", "Gestión de claves", "Soluciones informáticas", "Mejora"]
tags: ["GVLK de Windows", "Claves de licencia", "Productividad", "Rendimiento del sistema", "Gestión de claves", "Sistemas operativos", "Servidor Windows", "Windows 10", "Soluciones informáticas", "Software", "Canal de servicios a largo plazo", "LTSC", "Subdivisión de Servicios a Largo Plazo", "LTSB", "Rendimiento mejorado", "Microsoft", "Gestión informática", "Claves de activación", "Cliente de KMS", "Lista GVLK", "Ediciones Windows", "Activación de la licencia", "Clave de producto cliente", "Servidor 2019", "Servidor 2016", "Windows 11 Pro", "Windows 10 para empresas", "Windows LTSB 2016", "Administradores de TI"]
cover: "/img/cover/windows_gvlks_unlocked.png"
coverAlt: "Una colorida ilustración de dibujos animados de una llave abriendo una puerta que representa el poder de las GVLK para liberar todo el potencial de Windows."
coverCaption: "Libere el potencial de Windows con los GVLK"
---

## Cómo instalar una clave de producto (GVLK) para Windows y Windows Server

Si está convirtiendo un equipo de un host KMS, MAK o edición comercial de Windows a un cliente KMS, debe instalar la clave de producto correspondiente, también conocida como GVLK (Generic Volume License Key). Las GVLK se utilizan para la activación por volumen con Key Management Services (KMS). He aquí una guía paso a paso sobre cómo instalar una GVLK en su sistema Windows o Windows Server.

## Script de instalación automatizada de GLVK

El script debe lanzarse desde un powershell administrativo en el directorio que contiene todos los archivos del archivo [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

## Instalación manual Pasos de activación

### Requisitos previos

Antes de continuar, asegúrese de que dispone de una clave de producto válida y legal para su versión y edición de Windows. El uso de claves de producto no autorizadas o pirateadas va en contra de los términos de servicio de Microsoft y puede acarrear consecuencias legales.

### Pasos de la instalación

1. **Abra un Símbolo del sistema administrativo:** Haga clic con el botón derecho del ratón en el botón "Inicio" y seleccione "Terminal de Windows (Admin)" o "Símbolo del sistema (Admin)." Si usas Windows 11 o Windows 10, puedes buscar "Símbolo del sistema", hacer clic con el botón derecho y elegir "Ejecutar como administrador."

2. **Localice la clave de producto adecuada (GVLK):** Busque la GVLK para su versión y edición de Windows o Windows Server en la siguiente lista:

   - *Windows Server 2022:*
     - Windows Server 2022 Datacenter: WX4NM-KYWYW-QJJR4-XV3QB-6VM33
     - Windows Server 2022 Datacenter Azure Edition: NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
     - Windows Server 2022 Standard: VDYBN-27WPP-V4HQT-9VMD4-VMK7H

   - *Windows Server 2019:*
     - Windows Server 2019 Datacenter: WMDGN-G9PQG-XVVXX-R3X43-63DFG
     - Windows Server 2019 Standard: N69G4-B89J2-4G8F4-WWYCC-J464C
     - Windows Server 2019 Essentials: WVDHN-86M7X-466P6-VHXV7-YY726

   - *Windows Server 2016:*
     - Windows Server 2016 Datacenter: CB7KF-BWN84-R7R2Y-793K2-8XDDG
     - Windows Server 2016 Standard: WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
     - Windows Server 2016 Essentials: JCKRF-N37P4-C2D82-9YXRT-4M63B

   - [Click Here to See the Others](#complete-list-of-generic-volume-license-keys-gvlk)

3. **Instalar la clave de producto (GVLK):** En el símbolo del sistema administrativo, escriba el siguiente comando, sustituyendo `<product key>` con el GVLK correspondiente:
```sh
slmgr /ipk <product key>
```

Por ejemplo, para instalar el GVLK para Windows Server 2022 Datacenter edition, el comando sería:

```sh
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33
```

4. **Después de introducir el comando, pulse Intro. El sistema intentará instalar la clave de producto especificada.

5. 5. **Mensaje de confirmación:** Si la instalación se realiza correctamente, aparecerá un mensaje de confirmación indicando que se ha instalado la clave de producto.

Si no ves un mensaje de confirmación o quieres forzar a windows a que intente la activación siguiente usando la clave, prueba los siguientes comandos:

```sh
slmgr /ato
slmgr /dlv
```

## Notas importantes

- Asegúrese siempre de que está utilizando una clave de producto válida y legal para su versión y edición de Windows.
- El comando "slmgr" se ocupa de las licencias y la activación, así que utilícelo con precaución.
- Para Windows 11 y Windows 10, consulte las tablas originales para obtener la lista completa de GVLK para las distintas ediciones.

Recuerda seguir las directrices de licencias y los términos de servicio de Microsoft para mantenerte conforme y legal.

*Exención de responsabilidad: Este artículo tiene únicamente fines informativos. El uso de las claves de producto debe cumplir las condiciones de licencia de Microsoft, y cualquier uso indebido es responsabilidad del usuario.


## Lista completa de claves genéricas de licencia por volumen (GVLK)

En las tablas siguientes encontrará las claves genéricas de licencia por volumen (GVLK) para cada versión y edición de Windows. El *LTSC* significa Long-Term Servicing Channel, y *LTSB* representa Long-Term Servicing Branch. Consulte las tablas siguientes para ver las GVLK:

### Windows Server (versiones LTSC)

#### Windows Server 2022

| Edición del sistema operativo | Clave de producto del cliente KMS
|--------------------------------|-------------------------------|
| Windows Server 2022 Datacenter: WX4NM-KYWYW-QJJR4-XV3QB-6VM33
| Windows Server 2022 Datacenter Edición Azure NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
| Windows Server 2022 Standard VDYBN-27WPP-V4HQT-9VMD4-VMK7H

#### Windows Server 2019

| Edición del sistema operativo Clave de producto del cliente KMS
|--------------------------------|-------------------------------|
| Windows Server 2019 Datacenter: WMDGN-G9PQG-XVVXX-R3X43-63DFG
| Windows Server 2019 Standard: N69G4-B89J2-4G8F4-WWYCC-J464C
| Windows Server 2019 Essentials: WVDHN-86M7X-466P6-VHXV7-YY726

#### Windows Server 2016

| Edición del sistema operativo Clave de producto de cliente KMS
|--------------------------------|-------------------------------|
| Windows Server 2016 Datacenter CB7KF-BWN84-R7R2Y-793K2-8XDDG
| Windows Server 2016 Standard WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
| Windows Server 2016 Essentials JCKRF-N37P4-C2D82-9YXRT-4M63B

### Windows Server (versiones semestrales del canal)

#### Windows Server, versiones 20H2, 2004, 1909, 1903 y 1809

| Edición del sistema operativo | Clave de producto del cliente KMS
|---------------------------|-------------------------------|
| Windows Server Datacenter 6NMRW-2C8FM-D24W7-TQWMY-CWH2D
| Windows Server Standard N2KJX-J94YW-TQVFB-DG9YT-724CC

### Windows 11 y Windows 10 (versiones del Canal Semianual)

| Edición del sistema operativo | Clave de producto del cliente KMS | .
|-----------------------------------|-------------------------------|
| Windows 11 Pro Windows 10 Pro W269N-WFGWX-YVC9B-4J6C9-T83GX
| Windows 11 Pro N Windows 10 Pro N MH37W-N47XK-V7XM9-C7227-GCQG9
| Windows 11 Pro para estaciones de trabajo Windows 10 Pro para estaciones de trabajo NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J
| Windows 11 Pro para estaciones de trabajo N Windows 10 Pro para estaciones de trabajo N 9FNHH-K3HBT-3W4TD-6383H-6XYWF
| Windows 11 Pro Education Windows 10 Pro Education 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y
| Windows 11 Pro Education N Windows 10 Pro Education N YVWGF-BXNMC-HTQYQ-CPQ99-66QFC
| Windows 11 Education NW6C2-QMPVW-D7KK-3GKT6-VCFB2
| Windows 11 Education N Windows 10 Education N 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ
| Windows 11 Enterprise: Windows 10 Enterprise: NPPR9-FWDCX-D2C8J-H872K-2YT43
| Windows 11 Enterprise N Windows 10 Enterprise N DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4
| Windows 11 Enterprise G Windows 10 Enterprise G YYVX9-NTFWV-6MDM3-9PT4T-4M68B
| Windows 11 Enterprise G N Windows 10 Enterprise G N 44RPN-FTY23-9VTTB-MP9BX-T84FV

### Windows 10 (versiones LTSC/LTSB)

#### Windows 10 LTSC 2021 y 2019

| Edición del sistema operativo | Clave de producto del cliente KMS
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSC 2021 Windows 10 Enterprise LTSC 2019 M7XTQ-FN8P6-TTKYV-9D4CC-J462D
| Windows 10 Enterprise N LTSC 2021 Windows 10 Enterprise N LTSC 2019 92NFX-8DJQP-P6BBQ-THF9C-7CG2H

#### Windows 10 LTSB 2016

| Edición del sistema operativo Clave de producto del cliente KMS
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSB 2016 DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ
| Windows 10 Enterprise N LTSB 2016 QFFDN-GRT3P-VKWWX-X7T3R-8B639

#### Windows 10 LTSB 2015

| Edición del sistema operativo Clave de producto del cliente KMS
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise 2015 LTSB WNMTR-4C88C-JK8YV-HQ7T2-76DF9
| Windows 10 Enterprise 2015 LTSB N 2F77B-TNFGY-69QQF-B8YKP-D69TJ

### Versiones anteriores de Windows Server

#### Windows Server, versión 1803

| Edición del sistema operativo | Clave de producto del cliente KMS
|---------------------------|-------------------------------|
| Windows Server Datacenter 2HXDN-KRXHB-GPYC7-YCKFJ-7FVDG
| Windows Server Standard PTXN8-JFHJM-4WC78-MPCBR-9W4KR

#### Windows Server, versión 1709

| Edición del sistema operativo Clave de producto del cliente KMS
|---------------------------|-------------------------------|
| Windows Server Datacenter 6Y6KB-N82V8-D8CQV-23MJW-BWTG6
| Windows Server Standard DPCNP-XQFKJ-BJF7R-FRC8D-GF6G4

#### Windows Server 2012 R2

| Edición del sistema operativo Clave de producto del cliente KMS
|----------------------------------------|-------------------------------|
| Windows Server 2012 R2 Standard D2N9P-3P6X9-2R39C-7RTCD-MDVJX
| Windows Server 2012 R2 Datacenter W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9
| Windows Server 2012 R2 Essentials KNC87-3J2TX-XB4WP-VCPJV-M4FWM

#### Windows Server 2012

| Edición del sistema operativo Clave de producto del cliente KMS
|-----------------------------------------|-------------------------------|
| Windows Server 2012 BN3D2-R7TKB-3YPBD-8DRP2-27GG4
| Windows Server 2012 N 8N2M2-HWPGY-7PGT9-HGDD8-GVGGY
| Windows Server 2012 en un solo idioma 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ
| Windows Server 2012 Country Specific 4K36P-JN4VD-GDC6V-KDT89-DYFKP
| Windows Server 2012 Standard XC9B7-NBPP2-83J2H-RHMBY-92BT4
| Windows Server 2012 MultiPoint Standard HM7DN-YVMH3-46JC3-XYTG7-CYQJJ
| Windows Server 2012 MultiPoint Premium XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G
| Windows Server 2012 Datacenter 48HP8-DN98B-MYWDG-T2DCC-8W83P

#### Windows Server 2008 R2

| Edición del sistema operativo Clave de producto del cliente KMS
|--------------------------------------------------|-------------------------------|
| Windows Server 2008 R2 Web 6TPJF-RBVHG-WBW2R-86QPH-6RTM4
| Windows Server 2008 R2 HPC edition TT8MH-CG224-D3D7Q-498W2-9QCTX
| Windows Server 2008 R2 Standard YC6KT-GKW9T-YTKYR-T4X34-R7VHC
| Windows Server 2008 R2 Enterprise 489J6-VHDMP-X63PK-3K798-CPX3Y
| Windows Server 2008 R2 Datacenter 74YFP-3QFB3-KQT8W-PMXWJ-7M648
| Windows Server 2008 R2 para sistemas basados en Itanium GT63C-RJFQ3-4GMB6-BRFB9-CB83V

#### Windows Server 2008

| Edición del sistema operativo Clave de producto del cliente KMS
|------------------------------------------------|-------------------------------|
| Windows Web Server 2008: WYR28-R7TFJ-3X2YQ-YCY4H-M249D
| Windows Server 2008 Standard TM24T-X9RMF-VWXK6-X8JC9-BFGM2
| Windows Server 2008 Standard sin Hyper-V W7VD6-7JFBR-RX26B-YKQ3Y-6FFFJ
| Windows Server 2008 Enterprise: YQGMW-MPWTJ-34KDK-48M3W-X4Q6V
| Windows Server 2008 Enterprise sin Hyper-V 39BXF-X8Q23-P2WWT-38T2F-G3FPG
| Windows Server 2008 HPC RCTX3-KWVHP-BR6TB-RB6DM-6X7HP
| Windows Server 2008 Datacenter 7M67G-PC374-GR742-YH8V4-TCBY3
| Windows Server 2008 Datacenter sin Hyper-V 22XQ2-VRXRG-P8D42-K34TD-G3QQC
| Windows Server 2008 para sistemas basados en Itanium 4DWFP-JF3DJ-B7DTH-78FJB-PDRHK

### Versiones anteriores de Windows

#### Windows 8.1

| Edición del sistema operativo | Clave de producto del cliente KMS |
|--------------------------|-------------------------------|
| Windows 8.1 Pro GCRJD-8NW9H-F2CDX-CCM8D-9D6T9
| Windows 8.1 Pro N HMCNV-VVBFX-7HMBH-CTY9B-B4FXY
| Windows 8.1 Enterprise MHF9N-XY6XB-WVXMC-BTDCT-MKKG7
| Windows 8.1 Enterprise N TT4HM-HN7YT-62K67-RGRQJ-JFFXW

#### Windows 8

| Edición del sistema operativo Clave de producto del cliente KMS
|--------------------------|-------------------------------|
| Windows 8 Pro NG4HW-VH26C-733KW-K6F98-J8CK4
| Windows 8 Pro N XCVCF-2NXM9-723PB-MHCB7-2RYQQ
| Windows 8 Enterprise 32JNW-9KQ84-P47T8-D8GGY-CWCK7
| Windows 8 Enterprise N JMNMF-RHW7P-DMY6X-RF3DR-X2BQT

#### Windows 7

| Edición del sistema operativo Clave de producto del cliente KMS
|--------------------------|-------------------------------|
| Windows 7 Professional FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4
| Windows 7 Professional N MRPKT-YTG23-K7D7T-X2JMM-QY7MG
| Windows 7 Professional E W82YF-2Q76Y-63HXB-FGJG9-GF7QX
| Windows 7 Enterprise 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH
| Windows 7 Enterprise N YDRBP-3D83W-TY26F-D46B2-XCKRJ
| Windows 7 Enterprise E C29WB-22CC8-VJ326-GHFJW-H9DH4

#### Windows Vista

| Edición del sistema operativo Clave de producto del cliente KMS
|--------------------------|-------------------------------|
|Windows Vista Business: YFKBB-PQJJV-G996G-VWGXY-2V3X8
|Windows Vista Business N HMBQG-8H2RH-C77VX-27R82-VMQBT
|Windows Vista Enterprise VKK3X-68KWM-X2YGT-QR4M6-4BWMV
|Windows Vista Enterprise N VTC42-BM838-43QHV-84HX6-XJXKV

## Referencias
- [Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)