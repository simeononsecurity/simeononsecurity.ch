---
title: "Aumente la seguridad de las máquinas virtuales con vTPM: Guía paso a paso"
date: 2023-09-02
toc: true
draft: false
description: "Mejore la seguridad de las máquinas virtuales utilizando vTPM con nuestra completa guía paso a paso, que proporciona atestación de la plataforma y compatibilidad con el cifrado BitLocker."
genre: ["Ciberseguridad", "Virtualización", "VMware", "vSphere", "Seguridad", "Módulo de plataforma de confianza", "vTPM", "Invitado OS", "Cifrado", "Plataforma de certificación"]
tags: ["Módulo de plataforma virtual de confianza", "Guía vTPM", "Seguridad de máquinas virtuales mejorada", "Plataforma de certificación", "Cifrado BitLocker", "VMware vSphere", "Seguridad de la virtualización", "Ciberseguridad", "Protección del SO invitado", "Hardware VM", "TPM 2.0", "Arranque seguro", "Operaciones criptográficas", "Buenas prácticas de seguridad de máquinas virtuales", "Servidor vCenter", "Hosts ESXi", "Firmware EFI", "Proveedor clave", "Documentación de VMware", "Servidor Windows", "Windows 7", "Sistema operativo Linux", "Configuración segura de máquinas virtuales", "Seguridad", "Cliente vSphere", "Chip virtual", "Protección de datos", "Detección de manipulaciones", "Verificación de la integridad de la máquina virtual", "Seguridad de VMware"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "Ilustración simbólica que muestra una máquina virtual con un candado brillante, que representa la seguridad mejorada a través de vTPM."
coverCaption: "Desbloquee una seguridad de máquinas virtuales sin precedentes"
---

## Habilitar el módulo de plataforma virtual de confianza para una máquina virtual existente

Virtual Trusted Platform Module (vTPM) es una característica de seguridad crítica que mejora la seguridad de los sistemas operativos invitados que se ejecutan en máquinas virtuales. Este artículo le guiará a través del proceso de añadir un vTPM a una máquina virtual existente en un entorno VMware vSphere, proporcionando instrucciones paso a paso y consideraciones importantes para asegurar una implementación sin problemas.

______

## Prerrequisitos

Antes de proceder a añadir un vTPM a su máquina virtual, asegúrese de que cumple los siguientes prerrequisitos:

1. **Entorno vSphere con proveedor de claves:** Asegúrese de que su entorno vSphere está configurado para un proveedor de claves. Este paso es crucial para gestionar las operaciones criptográficas de forma segura. Consulte la [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html) para obtener información detallada.

2. **Verifique que su sistema operativo invitado es compatible con vTPM. VMware vTPM es compatible con TPM 2.0 y soporta Windows Server 2008 y posteriores, Windows 7 y posteriores, y varias distribuciones de Linux.

3. **Estado de la máquina virtual:** Asegúrese de que la máquina virtual que desea modificar está apagada antes de proceder con la adición de vTPM.

4. **Los hosts ESXi de su entorno deben ejecutar ESXi 6.7 o posterior para SO huésped Windows o ESXi 7.0 Update 2 para SO huésped Linux.

5. **Firmware EFI:** La máquina virtual debe utilizar firmware EFI para ser compatible con vTPM.

6. **Privilegios requeridos:** Compruebe que dispone de los privilegios necesarios para las operaciones criptográficas para añadir y gestionar la vTPM. Los privilegios requeridos incluyen:
   - Operaciones criptográficas.Clone
   - Operaciones criptográficas.Encrypt
   - Operaciones criptográficas.Cifrar nuevo
   - Operaciones criptográficas.Migrate
   - Operaciones criptográficas.Register VM



## Añadir Módulo de Plataforma Virtual de Confianza (vTPM)

Siga estos pasos para añadir un vTPM a su máquina virtual existente:

1. **Conéctese a vCenter Server:** Inicie vSphere Client e inicie sesión en vCenter Server.

2. **Abra Virtual Machine Settings:** Localice la máquina virtual que desea modificar en el inventario de la parte izquierda de vSphere Client. Haga clic con el botón derecho en el nombre de la máquina virtual y seleccione "Edit Settings".

3. **Agregar Trusted Platform Module:** En el cuadro de diálogo "Edit Settings", haga clic en el botón "Add New Device". De la lista de tipos de dispositivos, seleccione "Trusted Platform Module" (vTPM).

4. **Confirme la selección:** Pulse el botón "Aceptar" para añadir el dispositivo vTPM a la máquina virtual.

5. 5. **Verificar la adición:** Tras añadir correctamente el vTPM, la pestaña Resumen de la máquina virtual incluirá ahora "Virtual Trusted Platform Module" en el panel Hardware de la máquina virtual.

______

## Ventajas de Virtual Trusted Platform Module (vTPM)

Habilitar un vTPM para su máquina virtual ofrece varios beneficios significativos:

1. **Seguridad mejorada:** El vTPM crea un chip TPM 2.0 virtualizado para la máquina virtual, proporcionando características de seguridad basadas en hardware como arranque seguro y operaciones criptográficas. Esto refuerza la postura de seguridad del sistema operativo invitado.

2. **Atestación de Plataforma:** vTPM permite a la máquina virtual generar una medida criptográfica de su propio estado, permitiendo la atestación de plataforma. Esta característica ayuda a verificar la integridad de la máquina virtual, asegurando que no ha sido manipulada.

3. **Si está ejecutando un sistema operativo invitado Windows, la activación de vTPM es un requisito previo para utilizar el cifrado BitLocker en los discos de la máquina virtual. Esto añade una capa adicional de protección de datos.



## Conclusión

La implementación de un módulo de plataforma virtual de confianza (vTPM) para una máquina virtual existente es un paso crucial para reforzar la seguridad de su infraestructura virtualizada. Siguiendo el procedimiento descrito y asegurándose de que se cumplen todos los requisitos previos, puede habilitar funciones de seguridad mejoradas, atestación de plataforma y compatibilidad con cifrado BitLocker para sus sistemas operativos invitados.

Recuerde consultar la documentación oficial de VMware para obtener detalles específicos relacionados con su versión y configuración de vSphere.

______

## Referencias

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

