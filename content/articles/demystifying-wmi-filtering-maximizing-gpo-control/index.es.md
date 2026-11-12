---
title: "Entender el filtrado WMI"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Aprende a usar el filtrado WMI para mejorar la selección de destinos de los objetos de directiva de grupo (GPO), con ejemplos prácticos y buenas prácticas."
genre: ["Administración de Windows", "Directiva de grupo", "Administración de sistemas", "Gestión de redes", "Infraestructura de TI", "Gestión de directivas", "Gobernanza de TI", "Automatización de TI", "Active Directory", "Cumplimiento de seguridad"]
tags: ["filtrado WMI", "GPO", "objetos de directiva de grupo", "filtros WMI", "selección de directivas", "consultas WMI", "Windows Management Instrumentation", "control de GPO", "Consola de administración de directivas de grupo", "Lenguaje de consulta WMI", "aplicación de directivas", "WQL", "ajuste preciso de directivas", "gestión de directivas", "recursos del sistema", "ejemplos de selección de directivas", "administración de sistemas", "gestión de redes", "gestión de infraestructura de TI", "automatización de TI", "administración de Active Directory", "cumplimiento de seguridad", "técnicas de control de directivas", "buenas prácticas de gestión de directivas", "filtrado de directivas", "estrategias de control de GPO", "seguridad de GPO", "ventajas del filtrado WMI", "implementación del filtrado WMI", "buenas prácticas de filtrado WMI"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Ilustración de una lupa enfocada en un icono de filtro, que representa la selección precisa de GPO mediante el filtrado WMI."
coverCaption: "Usa el filtrado WMI para seleccionar las directivas de GPO con eficacia."
---

## Introducción

En los objetos de directiva de grupo (GPO), el [**filtrado WMI**](https://simeononsecurity.com/github/wmi-filters/) controla qué equipos o usuarios reciben las directivas según los resultados de consultas WMI (Windows Management Instrumentation). Esta función ayuda a los administradores a ajustar la selección y aplicar las directivas solo a los destinos previstos. En este artículo veremos qué es el filtrado WMI, cómo funciona con las GPO, cómo crear [filtros WMI](https://simeononsecurity.com/github/wmi-filters/) y algunos ejemplos prácticos.

## [¿Qué es el filtrado WMI?](https://simeononsecurity.com/github/wmi-filters/)

El [**filtrado WMI**](https://simeononsecurity.com/github/wmi-filters/) aplica filtros a las GPO según los resultados de consultas WMI. WMI es una infraestructura de administración integrada en los sistemas operativos Windows. Permite recuperar datos de administración e interactuar de forma programática con los recursos del sistema. Con el filtrado WMI, los administradores pueden seleccionar dinámicamente las GPO según criterios definidos en las consultas.

Los filtros WMI se escriben con el Lenguaje de consulta WMI (WQL), un subconjunto de SQL (Structured Query Language). Suelen basarse en propiedades y valores disponibles en un espacio de nombres WMI. Los administradores pueden combinar condiciones, operadores lógicos y espacios de nombres para crear consultas que seleccionen equipos o usuarios concretos.

## ¿Cómo funciona el filtrado WMI en las GPO?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Diagrama de flujo donde un filtro WMI asociado a un objeto de directiva de grupo evalúa una consulta WQL como True o False para decidir si la GPO se aplica al equipo de destino" >}}

En la directiva de grupo, el **filtrado WMI** permite aplicar GPO de forma selectiva según la evaluación de **consultas WMI**. Al asociar un **filtro WMI** a una GPO, el resultado **True** o **False** del filtro determina si se aplica la GPO.

Los filtros WMI se crean con el **Lenguaje de consulta WMI (WQL)**, un subconjunto de SQL (Structured Query Language). WQL permite formular consultas complejas que consideran distintas **propiedades** y **valores** disponibles en el **espacio de nombres WMI**. Así se pueden seleccionar equipos o usuarios concretos.

Por ejemplo, una organización puede querer aplicar una GPO solo a los equipos que ejecutan Windows 10. Puede crear un filtro WMI que compruebe la propiedad **OperatingSystem** de la clase **Win32_OperatingSystem**. La consulta podría ser:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

La consulta comprueba si la versión del sistema operativo empieza por «10.», lo que indica Windows 10. Si el resultado es **True**, la GPO se aplica al equipo de destino. De lo contrario, no se aplica.

El filtrado WMI también admite condiciones y operadores lógicos como **AND**, **OR** y **NOT**. Los administradores pueden combinar varias propiedades y valores para controlar con mayor precisión la aplicación de las GPO.

También es posible usar distintos **espacios de nombres WMI** para acceder a conjuntos concretos de clases y propiedades WMI. Esta flexibilidad permite seleccionar GPO según la configuración del hardware, el software instalado, los ajustes de red y otros criterios.

Para obtener más información sobre cómo crear filtros WMI y construir consultas, consulta la documentación de Microsoft sobre el [filtrado WMI para la directiva de grupo](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

El filtrado WMI permite adaptar la aplicación de GPO a equipos o usuarios según condiciones dinámicas y mejorar la administración del entorno de TI.

## Crear filtros WMI para GPO

Sigue estos pasos para crear un filtro WMI para una GPO:

1. Abre la **Consola de administración de directivas de grupo** (GPMC) en un equipo Windows unido al dominio.

2. Expande el dominio y ve al nodo **Filtros WMI**.

3. Haz clic con el botón derecho en **Filtros WMI** y selecciona **Nuevo**.

4. Asigna un nombre descriptivo al filtro e introduce la consulta WMI en el campo **Consulta**. Usa la sintaxis WQL.

5. Haz clic en **Aceptar** para guardar el filtro WMI.

Una vez creado, el filtro se puede asociar a una o varias GPO. Para asociarlo a una GPO:

1. Haz clic con el botón derecho en la GPO deseada y selecciona **Propiedades**.

2. En la ventana de propiedades de la GPO, abre la pestaña **Filtrado WMI**.

3. Selecciona el filtro WMI deseado en la lista.

4. Haz clic en **Aceptar** para guardar los cambios.

Al asociar filtros WMI a las GPO, puedes seleccionar con precisión dónde se aplican las directivas según los resultados de las consultas WMI.

## ¿Cuántos filtros WMI se pueden configurar para una GPO?

Los administradores pueden configurar **varios filtros WMI** para una GPO y así seleccionar con precisión los destinos de las directivas. No existe un límite específico para el número de filtros asociados a una GPO, por lo que es posible crear combinaciones complejas.

Sin embargo, debes tener en cuenta el efecto que tiene el número de filtros en el tiempo de procesamiento de las GPO. Cuantos más filtros haya, más tiempo puede tardar su evaluación y aplicación. Para que las directivas se apliquen con eficiencia, conviene mantener un número razonable de filtros.

Por ejemplo, una organización puede querer aplicar una GPO solo a equipos con Windows 10 que tengan instalado un programa específico. Puede crear dos filtros WMI independientes: uno para el **sistema operativo** y otro para la **instalación del software**. Al combinarlos, selecciona los equipos deseados.

Hay que equilibrar la cantidad de filtros necesaria para cumplir los requisitos de selección con el tiempo de procesamiento. Antes de decidir cuántos configurar, los administradores deben evaluar la complejidad del entorno, el número de equipos o usuarios y el posible impacto en el rendimiento.

La posibilidad de configurar varios filtros WMI ayuda a optimizar la selección de GPO y, al mismo tiempo, mantener una administración y un procesamiento eficientes.

## Ejemplos prácticos de filtrado WMI en GPO

El filtrado WMI permite aplicar directivas de forma selectiva. Estos son algunos ejemplos:

1. **Seleccionar sistemas operativos concretos**: para aplicar una GPO solo a equipos con **Windows 10**, crea un filtro que compruebe la versión del sistema operativo, por ejemplo `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. Así seleccionas equipos Windows 10.

2. **Usar directivas distintas para equipos de escritorio y portátiles**: si las directivas varían según el tipo de equipo, usa dos filtros WMI. Uno puede identificar equipos de escritorio mediante atributos de hardware, como `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, y el otro puede identificar portátiles. Así cada tipo de equipo recibe las directivas adecuadas.

3. **Seleccionar directivas según el espacio en disco**: para evitar directivas que consumen muchos recursos en equipos con poco espacio, crea un filtro que compruebe el espacio disponible. Por ejemplo, la consulta `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` excluye los equipos con menos de 10 GB libres.

Estos ejemplos muestran la flexibilidad del **filtrado WMI** en las GPO. Los administradores pueden seleccionar la aplicación de directivas según criterios específicos.

## Conclusión

El filtrado WMI es una función útil de los objetos de directiva de grupo. Permite a los administradores aplicar directivas de forma selectiva según los resultados de consultas WMI. Los filtros WMI ayudan a seleccionar equipos o usuarios concretos y a administrar las directivas de forma más eficiente y controlada. En este artículo vimos el concepto, su funcionamiento con las GPO, cómo crear filtros y algunos ejemplos prácticos.

Al incorporar el filtrado WMI a la administración de GPO, mejoras la precisión de la aplicación de directivas y te aseguras de que solo se apliquen a los destinos previstos.

## Referencias

- [Microsoft Docs: Crear filtros WMI para la GPO](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Directiva de grupo](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Consola de administración de directivas de grupo](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
