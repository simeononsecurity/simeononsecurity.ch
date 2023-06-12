---
title: "Directrices de codificación segura para Ansible: Buenas prácticas"
date: 2023-03-02
toc: true
draft: false
description: "Aprenda las mejores prácticas para escribir código seguro con Ansible, una popular herramienta para la gestión de la configuración y el despliegue."
tags: ["Codificación segura", "Ansible", "Gestión de la configuración", "Despliegue", "Principio del menor privilegio", "Bóveda Ansible", "Contraseñas seguras", "Control de acceso", "Sistema de control de versiones", "Protocolos de comunicación seguros", "SSH", "WinRM", "Certificados TLS", "Sanear la entrada del usuario", "Validación de las entradas", "Tratamiento de errores", "Prácticas de codificación seguras", "Inyección de código", "Directrices de codificación segura", "Seguridad de las infraestructuras", "Directrices de codificación segura para Ansible", "Buenas prácticas para un código seguro con Ansible", "Gestión segura de la configuración con Ansible", "Prácticas de despliegue seguro con Ansible", "Principio de mínimo privilegio en Ansible", "Uso de Ansible Vault para un código seguro", "Creación de contraseñas seguras en Ansible", "Control de acceso en Ansible", "Sistema de control de versiones para los playbooks de Ansible", "Protocolos de comunicación segura en Ansible", "Seguridad SSH en Ansible", "Seguridad WinRM en Ansible", "Certificados TLS en Ansible", "Saneamiento de entradas de usuario en Ansible", "Validación de entradas en Ansible", "Gestión de errores en Ansible", "Prácticas de codificación segura en Ansible", "Prevención de la inyección de código en Ansible", "Directrices de codificación segura para infraestructuras gestionadas por Ansible", "Protección de la infraestructura de Ansible"]
cover: "/img/cover/A_cartoon_image_of_a_castle_protected_by_a_shield.png"
coverAlt: " Una imagen de dibujos animados de un castillo protegido por un escudo, que representa las medidas de seguridad establecidas para la infraestructura gestionada por Ansible."
coverCaption: ""
---

A medida que las organizaciones avanzan hacia la automatización, **Ansible** se ha convertido en una opción popular para la **gestión de la configuración** y el **despliegue**. Sin embargo, como cualquier software, Ansible no es inmune a las vulnerabilidades de seguridad. Escribir **código seguro** es crucial para garantizar la seguridad y fiabilidad de la infraestructura gestionada por Ansible. Este artículo proporciona **guías** para escribir **código seguro** usando Ansible.

## Entendiendo la seguridad de Ansible

Antes de entrar en las directrices, es importante entender las características de seguridad de Ansible. Ansible proporciona **encriptación** para la comunicación entre los nodos de control y los nodos administrados. Ansible también proporciona **almacenamiento seguro** de **secretos** y otra información sensible usando la **bóveda**. Adicionalmente, Ansible tiene un **mecanismo sandboxing** para proteger contra la ejecución de código potencialmente malicioso.

Sin embargo, estas características de seguridad no eximen a los desarrolladores de escribir código seguro. Adherirse a las siguientes directrices ayudará a los desarrolladores a escribir código seguro que complemente las características de seguridad integradas de Ansible.

## Directriz 1: Use la última versión de Ansible

Ansible se actualiza constantemente para corregir vulnerabilidades y errores de seguridad. Utilizar la última versión de Ansible garantiza que los desarrolladores tengan acceso a las últimas correcciones y mejoras de seguridad.

Los desarrolladores deben comprobar regularmente si hay actualizaciones e instalarlas lo antes posible. También pueden suscribirse a la lista de correo Ansible Security Announcements para recibir notificaciones sobre actualizaciones de seguridad. Actualizar a la última versión de Ansible es un paso sencillo que puede mejorar significativamente la seguridad de la infraestructura gestionada por Ansible.

## Directriz 2: Sigue el Principio de Mínimo Privilegio

El **principio de mínimo privilegio** es un principio fundamental de seguridad que se aplica a Ansible. Este principio establece que un usuario sólo debe tener el nivel mínimo de acceso necesario para realizar su función de trabajo. Este principio también se aplica a Ansible. Los desarrolladores deben dar a los nodos administrados el nivel mínimo de acceso requerido para realizar las tareas necesarias.

Por ejemplo, si un playbook sólo requiere acceso de lectura a un archivo específico, los desarrolladores sólo deben conceder acceso de lectura al archivo y no acceso de escritura o ejecución. Los desarrolladores también deben limitar el número de usuarios con acceso a Ansible. El acceso debe limitarse a los usuarios autorizados que necesiten gestionar la infraestructura mediante Ansible.

Ansible proporciona varios mecanismos para implementar el principio de mínimo privilegio, como el método `become` directiva. En `become` permite a los desarrolladores ejecutar tareas con privilegios de otro usuario, como por ejemplo `sudo` Los desarrolladores deben utilizar `become` sólo cuando sea necesario y proporcionar únicamente el nivel de privilegios necesario.

Aplicando el principio del mínimo privilegio, los desarrolladores pueden limitar el daño potencial causado por un atacante en caso de violación de la seguridad. Esta directriz puede mejorar significativamente la seguridad de la infraestructura gestionada por Ansible.

## Directriz 3: Usar Ansible Vault para información sensible

Información sensible como contraseñas, claves API y certificados no deben ser almacenados en texto plano en los playbooks de Ansible. Almacenar información sensible en texto plano puede comprometer la seguridad de la infraestructura gestionada por Ansible. Ansible proporciona la **Bóveda** para almacenar información sensible de forma segura.

Vault cifra la información confidencial con una contraseña o un archivo de claves. Los desarrolladores pueden utilizar el `ansible-vault` para crear un nuevo archivo cifrado, editar un archivo cifrado existente o ver un archivo cifrado. El comando `ansible-vault` también puede utilizarse para cifrar o descifrar variables individuales. Por ejemplo, para crear un nuevo archivo cifrado, los desarrolladores pueden utilizar el siguiente comando:

```bash
ansible-vault create secret.yml
```

Este comando creará un nuevo archivo encriptado llamado `secret.yml` Los desarrolladores pueden editar este archivo utilizando la función `ansible-vault edit` comando. Se les pedirá que introduzcan la contraseña de la Bóveda.

Los desarrolladores también deben asegurarse de que las contraseñas y los archivos de claves se almacenan de forma segura. Las contraseñas y los archivos de claves no deben almacenarse en texto plano. Deben almacenarse en un lugar seguro, como un gestor de contraseñas o un servidor de archivos seguro.

Utilizar el Vault para almacenar información sensible es un paso crucial para asegurar la infraestructura gestionada por Ansible. Siguiendo esta directriz, los desarrolladores pueden asegurarse de que la información confidencial no se expone en texto plano y sólo es accesible para los usuarios autorizados.

## Directriz 4: Utilice contraseñas seguras

Las contraseñas utilizadas para la autenticación deben ser **fuertes** y **únicas**. El uso de contraseñas débiles o comunes puede comprometer la seguridad de la infraestructura gestionada por Ansible. Los desarrolladores también deben evitar el uso de contraseñas predeterminadas o contraseñas hardcoding en playbooks. Las contraseñas deben almacenarse de forma segura utilizando Vault.

Una contraseña segura debe tener un mínimo de 12 caracteres y contener una combinación de letras mayúsculas y minúsculas, números y caracteres especiales. Los desarrolladores también deben evitar el uso de información fácil de adivinar, como nombres o cumpleaños, en las contraseñas. Pueden utilizar un gestor de contraseñas para generar contraseñas fuertes y únicas.

Las contraseñas utilizadas en los playbooks deben almacenarse en formato cifrado utilizando Vault. Los desarrolladores también deben evitar codificar las contraseñas en los libros de jugadas. En su lugar, deben utilizar variables para almacenar las contraseñas y hacer referencia a ellas en los libros de jugadas. Por ejemplo, los desarrolladores pueden definir una variable denominada `db_password` en un archivo encriptado separado y referenciarlo en el playbook usando la siguiente sintaxis:
```yml
db_password: "{{ vault_db_password }}"
```

Esta sintaxis hará referencia al `db_password` del archivo encriptado y desencriptarlo usando la Bóveda.

Utilizando contraseñas seguras y almacenándolas de forma segura, los desarrolladores pueden evitar el acceso no autorizado a la infraestructura gestionada por Ansible. Esta pauta es un paso sencillo que puede mejorar significativamente la seguridad de la infraestructura gestionada por Ansible.


## Directriz 5: Limitar el acceso a los Playbooks

El acceso a los playbooks de Ansible debe estar limitado a usuarios autorizados. Los desarrolladores deberían usar un **sistema de control de versiones** como **Git** para gestionar los playbooks. Git proporciona **control de acceso** y **funciones de auditoría** que pueden ayudar a hacer cumplir las políticas de seguridad.

## Directriz 6: Utilizar protocolos de comunicación seguros

Ansible soporta varios protocolos de comunicación, incluyendo SSH y WinRM. SSH es el protocolo recomendado para hosts Linux y macOS. WinRM es el protocolo recomendado para hosts Windows. Los desarrolladores deben asegurarse de que la comunicación entre los nodos de control y los nodos gestionados está **encriptada**.

SSH es un protocolo de comunicación seguro que cifra la comunicación entre los nodos de control y los nodos gestionados. Los desarrolladores deben utilizar claves SSH seguras para la autenticación. Las claves SSH deben tener una longitud mínima de 2048 bits. Los desarrolladores también deben desactivar la autenticación por contraseña para SSH.

WinRM es un protocolo de comunicación seguro que cifra la comunicación entre los nodos de control y los nodos gestionados. Los desarrolladores deben utilizar WinRM sobre HTTPS para garantizar que la comunicación esté cifrada. También deben utilizar certificados fuertes para la autenticación.

Los desarrolladores también deben asegurarse de que los certificados TLS utilizados para la comunicación HTTPS son válidos y no han caducado. Pueden utilizar herramientas como `openssl` para generar y gestionar certificados TLS.

El uso de protocolos de comunicación seguros es un paso crucial para asegurar la infraestructura gestionada por Ansible. Siguiendo esta pauta, los desarrolladores pueden garantizar que la comunicación entre los nodos de control y los nodos gestionados esté cifrada y sea segura.

## Directriz 7: Verificar identidades de host

Los desarrolladores deben verificar las identidades de los nodos gestionados antes de permitirles conectarse a los nodos de control. Ansible proporciona varios mecanismos para verificar las identidades de los hosts, incluyendo **huellas digitales de claves SSH** y **certificados TLS**. Los desarrolladores también deben asegurarse de que las configuraciones de SSH y TLS están actualizadas y son seguras.

Las huellas digitales de claves SSH son identificadores únicos de claves SSH utilizadas por los nodos gestionados para la autenticación. Los desarrolladores deben verificar las huellas digitales de las claves SSH de los nodos gestionados antes de permitirles conectarse a los nodos de control. Pueden utilizar el `ssh-keygen` para generar huellas dactilares de claves SSH y compararlas con las huellas dactilares proporcionadas por los nodos gestionados.

Los nodos gestionados utilizan certificados TLS para autenticarse ante los nodos de control. Los desarrolladores deben asegurarse de que los certificados TLS utilizados por los nodos gestionados son válidos y no han caducado. También deben asegurarse de que los nodos de control confían en los certificados TLS utilizados por los nodos gestionados.

Los desarrolladores también deben asegurarse de que las configuraciones de SSH y TLS están actualizadas y son seguras. Las configuraciones SSH y TLS deben utilizar algoritmos de cifrado y autenticación seguros. También deben configurarse para rechazar cifrados y protocolos débiles.

Verificar las identidades de los nodos gestionados es un paso crucial para asegurar la infraestructura gestionada por Ansible. Siguiendo esta directriz, los desarrolladores pueden evitar los ataques man-in-the-middle y asegurarse de que sólo los nodos gestionados autorizados pueden conectarse a los nodos de control.

## Directriz 8: Desinfectar la entrada del usuario

Los desarrolladores deberían desinfectar la entrada del usuario para prevenir la **inyección de código** y otras vulnerabilidades de seguridad. Los desarrolladores también deberían usar **entrada validada** siempre que sea posible para reducir el riesgo de vulnerabilidades de seguridad.

## Directriz 9: Siga prácticas de codificación seguras

Los desarrolladores deberían seguir **prácticas de codificación seguras** tales como **validación de entrada**, **manejo de errores**, y **sanitización** de entrada. Los desarrolladores también deben seguir **directrices de codificación segura** para el lenguaje de programación utilizado en Ansible.

Los desarrolladores deben desinfectar la entrada del usuario para prevenir la **inyección de código** y otras vulnerabilidades de seguridad. La inyección de código es un tipo de ataque en el que un atacante inyecta código malicioso en una aplicación aprovechando vulnerabilidades en la entrada del usuario. Los desarrolladores también deben utilizar entradas validadas siempre que sea posible para reducir el riesgo de vulnerabilidades de seguridad.

Los desarrolladores pueden utilizar el `regex_replace` en Ansible para desinfectar la entrada del usuario. La dirección `regex_replace` permite a los programadores sustituir patrones de cadenas por otros patrones. Por ejemplo, para sustituir todos los caracteres no alfanuméricos de una cadena por una cadena vacía, los desarrolladores pueden utilizar el código siguiente:

```yaml
- name: Sanitize user input
  vars:
    user_input: "Hello! This is a string with non-alphanumeric characters."
    sanitized_input: "{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}"
  debug:
    var: sanitized_input
```
En este ejemplo, el `regex_replace` se utiliza para reemplazar todos los caracteres no alfanuméricos de los campos `user_input` con una cadena vacía. La entrada depurada se almacena en el archivo `sanitized_input` variable.

Los desarrolladores también pueden utilizar la validación de entradas para reducir el riesgo de vulnerabilidades de seguridad. La validación de entrada implica comprobar la entrada del usuario para asegurarse de que cumple ciertos criterios. Por ejemplo, los desarrolladores pueden validar la entrada del usuario para asegurarse de que sólo contiene caracteres alfanuméricos. La validación de entrada puede implementarse utilizando condicionales Ansible y expresiones regulares.

Al desinfectar la entrada del usuario y utilizar entradas validadas, los desarrolladores pueden evitar la inyección de código y otras vulnerabilidades de seguridad en los libros de ejecución de Ansible. Esta directriz es un paso sencillo que puede mejorar significativamente la seguridad de la infraestructura gestionada por Ansible.
______

## Conclusión

Ansible es una potente herramienta para la gestión de la configuración y el despliegue, pero es importante escribir código seguro para garantizar la seguridad y fiabilidad de la infraestructura gestionada por Ansible. Seguir las directrices proporcionadas en este artículo ayudará a los desarrolladores a escribir código seguro que complemente las funciones de seguridad integradas en Ansible.

Recuerde usar siempre la última versión de Ansible, seguir el principio de mínimo privilegio, usar Ansible Vault para información sensible, usar contraseñas seguras, limitar el acceso a los playbooks, usar protocolos de comunicación seguros, verificar las identidades de los hosts, desinfectar las entradas de los usuarios y seguir prácticas de codificación seguras. Estas directrices ayudarán a los desarrolladores a escribir código seguro y a mantener su infraestructura a salvo de vulnerabilidades de seguridad.

Siguiendo estas directrices, las organizaciones pueden garantizar que su infraestructura gestionada por Ansible sea segura y fiable. Con un código seguro y las funciones de seguridad integradas de Ansible, las organizaciones pueden aprovechar las ventajas de la automatización sin sacrificar la seguridad.

## Referencias

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Vault Documentation](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
- [Git Documentation](https://git-scm.com/doc)
- [OpenSSH Documentation](https://www.openssh.com/)
- [Transport Layer Security (TLS) Documentation](https://tools.ietf.org/html/rfc8446)
- [OWASP Code Injection Documentation](https://owasp.org/www-community/attacks/Code_Injection)
