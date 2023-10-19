---
title: "Buenas prácticas básicas de Windows Hardening para asegurar Windows 10 y Windows 11"
date: 2023-07-27
toc: true
draft: false
description: "Descubra estrategias eficaces para mejorar la seguridad de sus sistemas Windows 10 y Windows 11 mediante técnicas de refuerzo completas y prácticas recomendadas."
genre: ["Endurecimiento de Windows", "Seguridad de Windows", "Endurecimiento de Windows 10", "Endurecimiento de Windows 11", "Buenas prácticas de seguridad en Windows", "Consejos de seguridad para Windows", "Directrices de seguridad de Windows", "Protección de los sistemas operativos Windows", "Refuerzo del sistema Windows", "Medidas de seguridad de Windows"]
tags: ["Endurecimiento de Windows", "Seguridad de Windows", "Windows 10", "Windows 11", "seguridad del sistema operativo", "Windows Defender", "Control de cuentas de usuario", "Cifrado BitLocker", "configuración del cortafuegos", "Políticas de AppLocker", "Actualizaciones de Windows", "contraseñas seguras", "copia de seguridad de datos", "Windows Hello", "Arranque seguro", "TPM", "Antivirus Microsoft Defender", "Windows Sandbox", "Protección de aplicaciones de Microsoft Defender", "Acceso controlado a carpetas", "Prácticas recomendadas para proteger Windows 10 y Windows 11", "Cómo reforzar los sistemas operativos Windows", "Medidas de seguridad de Windows para particulares y organizaciones", "Mejora de la seguridad del sistema Windows", "Protección de datos con cifrado BitLocker", "Aislamiento de sesiones de navegador con Microsoft Defender Application Guard", "Consejos y directrices de seguridad de Windows 10", "Implementación de las funciones de seguridad de Windows", "Protección de Windows mediante aislamiento basado en hardware", "Garantizar la integridad del sistema Windows"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.png"
coverAlt: "Ilustración de dibujos animados de un escudo que protege el logotipo de Windows de diversas ciberamenazas."
coverCaption: "Asegure su fortaleza de Windows con técnicas eficaces de endurecimiento."
---

## Introducción

Los sistemas operativos Windows son ampliamente utilizados por particulares y organizaciones de todo el mundo. Para garantizar la seguridad e integridad de estos sistemas, es esencial implementar **las mejores prácticas de hardening de Windows**. El endurecimiento implica asegurar el sistema operativo reduciendo su superficie de ataque y mitigando las vulnerabilidades potenciales. Este artículo explorará las mejores prácticas para el hardening de los sistemas operativos **Windows 10** y el más reciente **Windows 11**, proporcionando información valiosa para mejorar la seguridad de su entorno Windows.

______

## Entendiendo el Fortalecimiento de Windows

Windows Hardening es el proceso de reforzar la seguridad de un sistema operativo Windows. Implica configurar varios parámetros e implementar medidas de seguridad para proteger contra el acceso no autorizado, el malware y otras amenazas. Al reforzar su sistema Windows, puede minimizar los riesgos asociados a los ciberataques y garantizar la confidencialidad, integridad y disponibilidad de sus datos.

### [Hardening Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 10 es uno de los sistemas operativos más utilizados en todo el mundo. Para reforzar su entorno Windows 10, tenga en cuenta las siguientes prácticas recomendadas:

#### 1. [**Enable Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender es una **solución antivirus robusta** incluida con Windows 10. Ofrece una serie de funciones de seguridad para proteger su sistema de varios tipos de **malware**, incluidos **virus, spyware y ransomware**. Al activar Windows Defender, puede mejorar significativamente la seguridad de su entorno Windows 10.

Para habilitar Windows Defender, siga estos pasos:

- Abre la app **Seguridad de Windows** haciendo clic en el icono de Seguridad de Windows en la barra de tareas o buscando "Seguridad de Windows" en el menú Inicio.
- En la aplicación Seguridad de Windows, haz clic en "**Protección contra virus y amenazas**" en el panel de navegación izquierdo.
- Haga clic en "**Administrar configuración**" en la sección "Configuración de protección contra virus y amenazas".
- Asegúrese de que el interruptor "**Protección en tiempo real**" está en "**Activado**". Esto permite a Windows Defender escanear activamente y proteger su sistema en tiempo real.
- Además, puede personalizar las opciones de análisis y las exclusiones haciendo clic en "**Opciones de análisis**" y "**Agregar o eliminar exclusiones**", respectivamente.

Es fundamental **actualizar periódicamente** Windows Defender para asegurarse de que cuenta con las últimas **definiciones de malware** y **mejoras de seguridad**. Microsoft publica actualizaciones periódicas para hacer frente a nuevas amenazas y vulnerabilidades. Para actualizar Windows Defender, puede seguir estos pasos:

- Abre la aplicación Seguridad de Windows.
- Ve a "**Protección contra virus y amenazas**" en el panel de navegación izquierdo.
- Haz clic en "**Comprobar actualizaciones**" en la sección "Actualizaciones de protección frente a virus y amenazas".
- Windows buscará actualizaciones disponibles y las descargará o instalará si es necesario.

Al habilitar y mantener Windows Defender actualizado, puedes proteger proactivamente tu sistema Windows 10 contra malware y otras amenazas de seguridad. También se recomienda realizar **escaneos regulares del sistema** utilizando Windows Defender para garantizar la detección y eliminación de cualquier amenaza potencial.

Recuerde que, aunque Windows Defender proporciona un sólido nivel de protección, es esencial complementarlo con **hábitos de navegación seguros**, **actualizaciones regulares de software** y otras medidas de seguridad para mantener un entorno Windows 10 seguro.

#### 2. [**Keep Windows 10 Updated**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)
La instalación periódica de actualizaciones de Windows es un aspecto crítico del **endurecimiento de Windows 10**. Estas actualizaciones incluyen **parches de seguridad**, correcciones de errores y mejoras de rendimiento que ayudan a **corregir vulnerabilidades de seguridad** y mejorar la estabilidad del sistema.

Microsoft publica **actualizaciones periódicas** para Windows 10 con el fin de solucionar problemas de seguridad recién descubiertos y mejorar la experiencia general del usuario. Al mantener su sistema actualizado, se asegura de que su sistema operativo cuenta con las últimas **mejoras de seguridad** para defenderse de las amenazas emergentes.

Para mantener Windows 10 actualizado, puede seguir estos pasos:

1. **Habilitar actualizaciones automáticas**: Por defecto, Windows 10 está configurado para descargar e instalar actualizaciones automáticamente. Esto asegura que tu sistema reciba las actualizaciones necesarias sin intervención manual. Para comprobar si las actualizaciones automáticas están habilitadas, sigue estos pasos:
   - Ve a **Configuración** haciendo clic en el menú Inicio y seleccionando el icono de engranaje.
   - Haga clic en **Actualización y seguridad**.
   - En el panel de navegación izquierdo, haga clic en **Windows Update**.
   - Asegúrese de que la opción **"Automático "** está seleccionada en **"Configuración de Windows Update "**. Si no está seleccionada, haga clic en el enlace **"Cambiar horas activas "** para personalizar las horas activas durante las cuales Windows debe evitar la instalación de actualizaciones.

2. **Instalar actualizaciones manualmente**: Si prefieres tener más control sobre el proceso de actualización, puedes instalar manualmente las actualizaciones en tu sistema Windows 10. A continuación te explicamos cómo:
   - Ve a **Configuración** > **Actualización y seguridad** > **Windows Update**.
   - Haz clic en **"Buscar actualizaciones "** para ver si hay actualizaciones disponibles para tu sistema.
   - Si se encuentran actualizaciones, haga clic en **"Descargar "** e **"Instalar "** para iniciar el proceso de instalación.

Es esencial hacer hincapié en la importancia de **reiniciar regularmente su sistema** después de instalar actualizaciones. Algunas actualizaciones pueden requerir un reinicio del sistema para aplicar completamente los cambios y asegurar su efectividad.

Al **mantener su sistema Windows 10 actualizado**, no solo mejora su seguridad, sino que también se beneficia de las últimas funciones, mejoras de rendimiento y correcciones de compatibilidad. Es una medida proactiva para garantizar que su sistema sigue siendo resistente frente a posibles amenazas de seguridad.

#### 3. [**Configure User Account Control (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)
El Control de cuentas de usuario (UAC) es una función de seguridad de Windows 10 que ayuda a evitar cambios no autorizados en el sistema solicitando la aprobación del administrador cuando es necesario. Actúa como protección frente a software malicioso o usuarios no autorizados que intentan realizar cambios que podrían afectar a la seguridad o estabilidad del sistema.

Configurar los ajustes de UAC a un nivel apropiado es crucial para **endurecer Windows 10**. Se trata de encontrar un equilibrio entre la seguridad y la facilidad de uso para garantizar que UAC protege eficazmente su sistema sin causar interrupciones innecesarias.

Para configurar los ajustes de UAC en Windows 10, puedes seguir estos pasos:

1. Abre el **Panel de control** escribiendo "Panel de control" en la barra de búsqueda y seleccionándolo en los resultados de la búsqueda.

2. En el Panel de control, haz clic en **"Cuentas de usuario "**.

3. 3. Pulsa en **"Cambiar configuración de Control de cuentas de usuario "**.

4. Verás un control deslizante con diferentes niveles de configuración de UAC. Estas son las opciones disponibles:
   - **"Notificar siempre "**: Este es el nivel más alto de seguridad UAC donde se te pide consentimiento para cualquier cambio en el sistema, incluso para tareas simples.
   - Notificarme sólo cuando las aplicaciones intentan hacer cambios en mi ordenador (por defecto)": Esta es la configuración recomendada que proporciona un equilibrio entre seguridad y usabilidad. Se te pedirá consentimiento cuando las aplicaciones realicen cambios, pero no para los cambios en la configuración de Windows.
   - Notificarme sólo cuando las aplicaciones intentan hacer cambios en mi ordenador (no atenuar mi escritorio) "**: Similar a la opción anterior, pero el escritorio no se oscurece cuando aparece el aviso UAC.
   - Nunca notificar "**: Este es el nivel más bajo de seguridad del UAC, en el que no se te solicita ningún cambio en el sistema.

5. Elige el nivel de seguridad UAC que se adapte a tus necesidades moviendo el control deslizante a la posición deseada.

6. Pulsa sobre **"Aceptar "** para guardar los cambios.

Se recomienda mantener el UAC activado y configurado a un nivel que proporcione un equilibrio adecuado entre seguridad y usabilidad. Deshabilitar UAC por completo puede dejar tu sistema más vulnerable a cambios no autorizados y comprometer potencialmente su seguridad.

Al configurar los ajustes de UAC, mejora la seguridad de su sistema Windows 10 al garantizar que se requieren privilegios administrativos para realizar cambios críticos en el sistema, lo que reduce el riesgo de acceso no autorizado e infecciones de malware.

#### 4. [**Use Strong Passwords**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)
El uso de contraseñas seguras es esencial para mantener la seguridad de su sistema Windows 10 y protegerlo contra el acceso no autorizado. Las contraseñas débiles o fáciles de adivinar pueden hacer que tu sistema sea vulnerable a ataques, como los ataques de fuerza bruta o el descifrado de contraseñas.

Para asegurarte de que todas las cuentas de usuario de tu sistema Windows 10 tienen contraseñas seguras, sigue estas prácticas recomendadas para contraseñas:

1. **Complejidad**: Anima a los usuarios a crear contraseñas que sean complejas y no fáciles de adivinar. Una contraseña segura debe incluir una combinación de letras mayúsculas y minúsculas, números y caracteres especiales. Evite utilizar palabras comunes o patrones predecibles.

2. **Longitud**: Las contraseñas más largas suelen ser más seguras. Anima a los usuarios a crear contraseñas de al menos 8 caracteres, pero preferiblemente más largas. Cuantos más caracteres tenga una contraseña, más difícil será descifrarla.

3. **Unicidad**: Cada cuenta de usuario debe tener una contraseña única. Utilizar la misma contraseña para varias cuentas aumenta el riesgo de una brecha de seguridad. Anima a los usuarios a utilizar contraseñas diferentes para cuentas diferentes.

4. **Evite la información personal**: Aconseje a los usuarios que no utilicen información personal como nombres, fechas de nacimiento o direcciones en sus contraseñas. Esta información puede ser fácilmente obtenida o adivinada por los atacantes.

5. **Gestores de contraseñas**: Considera la posibilidad de utilizar un gestor de contraseñas para almacenarlas y gestionarlas de forma segura. Los gestores de contraseñas pueden generar contraseñas fuertes y únicas para cada cuenta y almacenarlas en una base de datos encriptada.

6. **Cambiar contraseñas periódicamente**: Anime a los usuarios a cambiar periódicamente sus contraseñas para mantener la seguridad. Establezca una política de caducidad de contraseñas y eduque a los usuarios sobre la importancia de actualizarlas periódicamente.

Al implementar prácticas de contraseñas seguras, mejorará significativamente la seguridad de su sistema Windows 10 y reducirá el riesgo de accesos no autorizados o violaciones de datos. Eduque regularmente a los usuarios sobre la seguridad de las contraseñas y proporcione recursos, como medidores de solidez de contraseñas o directrices de creación de contraseñas, para ayudarles a crear contraseñas seguras.

Para obtener información más detallada sobre la creación de contraseñas seguras y las mejores prácticas, puede consultar este enlace [article](https://simeononsecurity.com/articles/how-to-create-strong-passwords/) Proporciona orientación exhaustiva sobre la seguridad de las contraseñas y ofrece consejos para crear contraseñas seguras y fáciles de recordar.

Recuerde que el uso de contraseñas seguras es un aspecto fundamental de la seguridad del sistema y debe priorizarse para proteger los datos confidenciales y garantizar la integridad de su entorno Windows 10.

#### 5. [**Enable BitLocker Encryption**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
Una de las formas más eficaces de proteger los datos confidenciales de su sistema Windows 10 es activar el cifrado BitLocker. BitLocker proporciona cifrado de todo el disco, lo que garantiza que, aunque pierdas o te roben el dispositivo, tus datos permanecerán seguros e inaccesibles para personas no autorizadas.

Para habilitar el cifrado BitLocker y proteger su información confidencial, siga estos pasos:

1. **Compruebe los requisitos del sistema**: Asegúrese de que su edición de Windows 10 es compatible con el cifrado BitLocker. BitLocker está disponible en las ediciones Pro, Enterprise y Education de Windows 10.

2. **Habilite BitLocker**: Abra el Panel de control y navegue hasta la categoría "Sistema y seguridad". Haga clic en "Cifrado de unidad BitLocker" y seleccione la(s) unidad(es) que desea cifrar. Siga las instrucciones que aparecen en pantalla para iniciar el proceso de cifrado.

3. **Elija las opciones de cifrado**: Durante la configuración de BitLocker, tendrá la opción de elegir entre diferentes métodos de cifrado, como el uso de una contraseña, una tarjeta inteligente o ambos. Seleccione el método adecuado en función de sus requisitos y preferencias de seguridad.

4. **Clave de Recuperación de Copia de Seguridad**: Es crucial hacer una copia de seguridad de la clave de recuperación de BitLocker. Esta clave actúa como un mecanismo de seguridad en caso de que olvide la contraseña o tenga algún problema para acceder a la unidad cifrada. Guarde la clave de recuperación en un lugar seguro y separado de su dispositivo.

5. **Administrar la configuración de BitLocker**: Después de habilitar BitLocker, puedes personalizar ajustes adicionales, como el desbloqueo automático para unidades específicas o configurar el uso de TPM (Trusted Platform Module) para mayor seguridad. Se puede acceder a estos ajustes a través de la interfaz de gestión de BitLocker.

Al activar el cifrado BitLocker, añades una capa adicional de protección a tu sistema Windows 10, garantizando que incluso si tu dispositivo cae en las manos equivocadas, tus datos permanezcan seguros e inaccesibles. Es importante actualizar y mantener regularmente la configuración de BitLocker para estar al día con las mejores prácticas de seguridad.

Para obtener información más detallada sobre la activación y gestión del cifrado BitLocker, puede consultar la página oficial [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) Proporciona una guía completa sobre el cifrado BitLocker, incluidas las funciones avanzadas y las opciones de configuración.

Recuerde que activar el cifrado BitLocker le ayuda a salvaguardar sus datos confidenciales y le proporciona la tranquilidad de saber que su información está segura incluso en caso de pérdida o robo.

#### 6. **Desactivar servicios y características innecesarias**
Para mejorar la seguridad de su sistema Windows 10, es esencial revisar y desactivar los servicios y características innecesarios. Al hacerlo, se reduce la superficie de ataque y se minimiza el potencial de explotación por parte de actores maliciosos.

Estos son los pasos para deshabilitar servicios y características innecesarios en su sistema Windows 10:

1. **Identifique los servicios innecesarios**: Empieza por identificar los servicios que se están ejecutando en tu sistema. Abre la consola de administración de "Servicios" pulsando **tecla de Windows + R**, escribiendo **services.msc** y pulsando **Intro**. Revisa la lista de servicios e investiga su finalidad para determinar cuáles son esenciales para el funcionamiento de tu sistema.

2. **Desactiva los servicios innecesarios**: Una vez identificados los servicios innecesarios, haz clic con el botón derecho del ratón sobre cada servicio y selecciona **Propiedades**. En la ventana Propiedades, cambie el **Tipo de inicio** a **Desactivado**. Esto evita que el servicio se inicie automáticamente al arrancar el sistema. Tenga cuidado y asegúrese de que sólo desactiva los servicios que no son necesarios para el funcionamiento normal del sistema.

3. **Desactivar características innecesarias**: Además de los servicios, Windows 10 también incluye varias características que pueden no ser necesarias para su sistema. Abra el **Panel de control**, navegue hasta **Programas** o **Programas y características**, y haga clic en **Activar o desactivar características de Windows**. Desactive las funciones que no necesite. Este paso ayuda a reducir aún más la superficie de ataque y minimiza los recursos consumidos por funciones innecesarias.

4. **Revisar y actualizar periódicamente**: Es crucial revisar regularmente la lista de servicios y características habilitadas en tu sistema Windows 10. A medida que los requisitos de su sistema cambian con el tiempo, es posible que tenga que volver a evaluar los servicios y características que son necesarios. Mantente alerta y actualiza tu configuración según sea necesario.

Al deshabilitar los servicios y características innecesarios, limitas los posibles puntos de entrada para los atacantes y reduces la superficie de ataque general de tu sistema Windows 10. Esta práctica mejora la postura de seguridad de su sistema y mitiga el riesgo de explotación.

Para obtener más información sobre la administración de servicios y características en Windows 10, puede consultar lo siguiente [article](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20) para obtener información detallada.

Recuerde, es crucial tener precaución cuando deshabilite servicios y características, ya que deshabilitar componentes esenciales puede afectar negativamente a la funcionalidad de su sistema. Investigue y comprenda siempre el propósito de un servicio o función antes de realizar cualquier cambio.

#### 7. **Implementar reglas de cortafuegos**
El cortafuegos integrado en Windows 10 actúa como una línea de defensa crucial contra el tráfico de red no autorizado. Mediante la configuración de reglas de firewall, puede controlar qué conexiones entrantes y salientes están permitidas, mejorando así la seguridad de su sistema.

Siga estos pasos para implementar reglas de firewall en su sistema Windows 10:

1. **Acceder a la configuración del cortafuegos**: Para acceder a la configuración del firewall, abra el **Panel de control**, busque **Windows Defender Firewall** y haga clic en el resultado correspondiente. Como alternativa, puede hacer clic con el botón derecho en el botón **Inicio**, seleccionar **Configuración** y navegar hasta **Red e Internet > Firewall de Windows**.

2. **Configurar reglas de entrada**: Las reglas de entrada controlan las conexiones de red entrantes a su sistema. Haz clic en **Configuración avanzada** en la ventana del Firewall de Windows Defender. En la nueva ventana, seleccione **Reglas de entrada** y haga clic en **Nueva regla**. Siga las instrucciones que aparecen en pantalla para crear reglas que sólo permitan las conexiones entrantes necesarias. Tenga en cuenta los servicios y aplicaciones que requieren acceso a la red y cree las reglas en consecuencia.

3. **Configurar reglas de salida**: Las reglas de salida controlan las conexiones de red salientes de su sistema. Siga los mismos pasos que arriba pero seleccione **Reglas de salida** en su lugar. Cree reglas para permitir conexiones salientes para servicios y aplicaciones esenciales y bloquear conexiones sospechosas o innecesarias.

4. **Revisar y actualizar periódicamente**: Es importante revisar y actualizar periódicamente las reglas de su cortafuegos para asegurarse de que se ajustan a los requisitos de su sistema. A medida que cambien su entorno de red y sus patrones de uso, puede que necesite modificar o crear nuevas reglas. Manténgase alerta y actualice sus reglas para mantener una configuración de cortafuegos eficaz.

Al implementar y mantener reglas de firewall, puede reducir significativamente el riesgo de acceso no autorizado a la red y mejorar la seguridad de su sistema Windows 10. Además, considere la posibilidad de activar la opción **Modo oculto** en la configuración del cortafuegos para que su sistema sea menos visible para los posibles atacantes.

Para obtener información más detallada sobre la configuración de las reglas del cortafuegos en Windows 10, puede consultar la publicación oficial [Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring) para obtener instrucciones paso a paso.

Recuerde que un cortafuegos bien configurado es un componente esencial de una estrategia de seguridad integral, pero debe utilizarse junto con otras medidas de seguridad para proporcionar una protección sólida a su sistema.

#### 8. [**Use AppLocker**](https://github.com/simeononsecurity/AppLocker)
AppLocker es una potente característica de Windows 10 que te permite controlar qué aplicaciones pueden ejecutarse en tu sistema. Mediante la implementación de políticas de AppLocker, puede restringir la ejecución de aplicaciones no autorizadas o potencialmente maliciosas, mejorando la seguridad de su entorno Windows 10.

Siga estos pasos para utilizar AppLocker en su sistema Windows 10:

1. **Acceder a la configuración de AppLocker**: Para acceder a la configuración de AppLocker, abre el **Editor de directivas de grupo locales** pulsando **tecla de Windows + R**, escribiendo **gpedit.msc** y haciendo clic en **OK**. También puede buscar **Editor de directivas de grupo** en el menú **Inicio**.

2. 2. **Configure las políticas de AppLocker**: En el Editor de directivas de grupo local, vaya a **Configuración del equipo > Configuración de Windows > Configuración de seguridad > Directivas de control de aplicaciones > AppLocker**. Aquí, puede configurar varias políticas como **Reglas ejecutables**, **Reglas del instalador de Windows**, **Reglas de scripts** y **Reglas de aplicaciones empaquetadas**.

3. **Crear reglas de AppLocker**: Para crear una regla de AppLocker, haga clic con el botón derecho del ratón en la carpeta de políticas deseada (por ejemplo, **Reglas ejecutables**) y seleccione **Crear nueva regla**. Siga las instrucciones en pantalla para especificar las condiciones y excepciones de la regla. Puede crear reglas basadas en la ruta del archivo, el editor, el hash del archivo u otros atributos para permitir o denegar la ejecución de la aplicación.

4. **Pruebe y refine las políticas**: Después de crear las reglas de AppLocker, es importante probarlas para asegurarse de que funcionan según lo previsto. Implemente las políticas en un grupo o sistema de prueba y verifique que sólo se permite la ejecución de las aplicaciones autorizadas. Realice los ajustes necesarios en las reglas basándose en los resultados de las pruebas.

5. **Revisión y actualización periódicas**: A medida que su entorno de aplicaciones evoluciona, es crucial revisar y actualizar regularmente sus políticas de AppLocker. Las nuevas aplicaciones pueden requerir permiso para ejecutarse, mientras que otras pueden quedar obsoletas o plantear riesgos de seguridad. Sea proactivo y mantenga sus políticas actualizadas para conservar un mecanismo eficaz de control de aplicaciones.

AppLocker proporciona un control granular sobre la ejecución de aplicaciones, ayudándole a evitar que software no autorizado o malicioso se ejecute en su sistema Windows 10. Mediante el uso de AppLocker, puede reducir el riesgo de infecciones de malware, instalaciones de software no autorizadas y otros incidentes de seguridad.

Para obtener información más detallada sobre la aplicación de las políticas de AppLocker, puede consultar el documento oficial [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) or visit our [AppLocker GitHub repository](https://github.com/simeononsecurity/AppLocker) para obtener más recursos y ejemplos.

Recuerde revisar y actualizar periódicamente sus directivas de AppLocker para adaptarse a los requisitos cambiantes de las aplicaciones y a las amenazas de seguridad emergentes. AppLocker es una herramienta valiosa en su defensa contra aplicaciones no autorizadas y potencialmente dañinas en su sistema Windows 10.

#### 9. [**Regularly Backup Your Data**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)
Realizar copias de seguridad de sus datos con regularidad es una práctica esencial para protegerse contra la pérdida de datos causada por incidentes de seguridad, fallos de hardware u otros imprevistos. Al crear copias de seguridad periódicas y verificar su integridad, puede asegurarse de que sus datos importantes permanezcan seguros y puedan restaurarse en caso de desastre.

Siga estos pasos para realizar copias de seguridad periódicas de sus datos en un sistema Windows 10:

1. **Identifique los datos críticos**: Comience por identificar los datos que son críticos y de los que es necesario hacer una copia de seguridad. Esto puede incluir documentos importantes, archivos personales, configuraciones del sistema, ajustes de aplicaciones y cualquier otro dato que considere valioso.

2. **Elija una solución de copia de seguridad**: Seleccione una solución de copia de seguridad confiable que cumpla con sus requisitos. Windows 10 ofrece herramientas de copia de seguridad integradas como **Historial de archivos** y **Windows Backup and Restore**. Como alternativa, puede optar por un software de copia de seguridad de terceros que ofrezca funciones adicionales y flexibilidad.

3. **Defina la frecuencia de las copias de seguridad**: Determina con qué frecuencia quieres realizar copias de seguridad en función de la criticidad de tus datos y la frecuencia de los cambios. Algunos datos pueden requerir copias de seguridad diarias, mientras que otros pueden realizarse semanal o mensualmente.

4. **Seleccione el almacenamiento de las copias de seguridad**: Elige un medio de almacenamiento adecuado para guardar tus copias de seguridad. Puede tratarse de discos duros externos, dispositivos de almacenamiento conectados a la red (NAS), servicios de almacenamiento en la nube o una combinación de varias opciones de almacenamiento. Asegúrate de que el medio de almacenamiento es seguro y fiable.

5. **Configurar los ajustes de copia de seguridad**: Configure la solución de copia de seguridad según sus preferencias. Especifique los datos de los que se realizará la copia de seguridad, el destino de la copia de seguridad y cualquier configuración adicional, como el cifrado o la compresión.

6. **Realice restauraciones de prueba**: Pruebe regularmente el proceso de restauración realizando restauraciones de prueba a partir de sus copias de seguridad. Esto garantiza que sus copias de seguridad funcionan correctamente y que puede recuperar sus datos con éxito cuando sea necesario.

7. **Supervisar y actualizar**: Supervise regularmente el proceso de copia de seguridad para asegurarse de que funciona como se espera. Actualice su solución de copia de seguridad y ajuste la configuración de la copia de seguridad a medida que cambien sus datos y requisitos.

Siguiendo estos pasos y respetando una rutina regular de copias de seguridad, puede minimizar el impacto de la pérdida de datos y mantener la disponibilidad de su información importante. Recuerde almacenar sus copias de seguridad de forma segura, lejos de los datos originales, y considere la posibilidad de aplicar la regla de las copias de seguridad **3-2-1**, consistente en tener al menos tres copias de sus datos, almacenadas en dos soportes de almacenamiento diferentes, con una copia almacenada fuera de las instalaciones.

Para obtener información más detallada sobre las mejores prácticas de copia de seguridad y la regla **3-2-1**, puede consultar el artículo en [What is the 3-2-1 Backup Rule and Why You Should Use It](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) Ofrece valiosas ideas y recomendaciones para aplicar una estrategia eficaz de copias de seguridad.

Recuerde que las copias de seguridad periódicas son cruciales para salvaguardar sus datos y garantizar su disponibilidad en caso de imprevistos. Haga de las copias de seguridad una parte integral de sus esfuerzos de refuerzo de Windows 10 para proteger su valiosa información.

______

{{< inarticle-dark >}}


### [Hardening Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 es la última versión del sistema operativo Windows, que ofrece funciones mejoradas y una mayor seguridad. Para reforzar su entorno Windows 11, tenga en cuenta las siguientes prácticas recomendadas:

#### 1. **Arranque seguro y TPM**
Secure Boot y TPM (Trusted Platform Module) son características de seguridad esenciales disponibles en Windows 11 que ayudan a proteger contra el acceso no autorizado y garantizar la integridad del sistema operativo. Activando Secure Boot y TPM, puedes mejorar la seguridad de tu sistema Windows 11.

Siga estos pasos para habilitar Secure Boot y TPM en su dispositivo Windows 11:

1. **Comprobar compatibilidad**: Antes de habilitar Secure Boot y TPM, asegúrese de que su dispositivo es compatible con estas funciones. Compruebe que el hardware y el firmware de su sistema cumplen los requisitos para la funcionalidad Secure Boot y TPM.

2. **Acceda a la configuración UEFI/BIOS**: Reinicia tu dispositivo Windows 11 y accede a la configuración UEFI (Unified Extensible Firmware Interface) o BIOS (Basic Input/Output System). La tecla o combinación de teclas específica para acceder a estos ajustes puede variar en función del dispositivo. Algunas teclas comunes son Supr, F2, F10 o Esc. Consulta la documentación de tu dispositivo o la página web del fabricante para obtener instrucciones detalladas.

3. **Habilite el arranque seguro**: Una vez en la configuración UEFI/BIOS, navega hasta la configuración de Arranque Seguro. Habilite el arranque seguro para garantizar que sólo los sistemas operativos y componentes de confianza puedan ejecutarse durante el proceso de arranque. Esto evita la carga de software no autorizado o malicioso que pueda comprometer la seguridad del sistema.

4. **Habilitar TPM**: Localiza la configuración del TPM en la UEFI/BIOS y habilita el TPM. TPM es un microchip dedicado en la placa base del dispositivo que proporciona características de seguridad basadas en hardware. Habilitar TPM permite a Windows 11 aprovechar sus capacidades para mejorar la seguridad del sistema.

5. **Configurar seguridad TPM**: Después de habilitar TPM, puede tener opciones adicionales para configurar sus ajustes de seguridad. Dependiendo de su dispositivo y firmware, es posible que pueda establecer una contraseña de TPM, habilitar las actualizaciones de firmware de TPM o ajustar otras configuraciones relacionadas. Revise las opciones disponibles y configúrelas en función de sus requisitos de seguridad.

6. **Guardar y Salir**: Una vez que haya habilitado el Arranque Seguro y el TPM y haya realizado las configuraciones necesarias, guarde los cambios en la configuración UEFI/BIOS y salga. El sistema se reiniciará y la nueva configuración surtirá efecto.

Habilitar Secure Boot y TPM en Windows 11 ayuda a proteger tu dispositivo de modificaciones no autorizadas, rootkits y otras amenazas de seguridad. Estas características establecen una base de confianza para el sistema operativo y contribuyen a un entorno informático más seguro.

Tenga en cuenta que la disponibilidad y los pasos específicos para habilitar Secure Boot y TPM pueden variar en función del fabricante y la versión de firmware de su dispositivo. Se recomienda consultar la documentación del dispositivo o el sitio web del fabricante para obtener instrucciones precisas adaptadas a su sistema.

Al habilitar Secure Boot y TPM en su dispositivo Windows 11, mejora la postura de seguridad general y refuerza la protección de su sistema operativo y datos confidenciales.

#### 2. [**Enable Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Windows 11 viene con una protección antivirus integrada llamada **Microsoft Defender Antivirus**. Ofrece seguridad completa contra varios tipos de **malware**, incluidos virus, ransomware y spyware. Al **activar** y **actualizar periódicamente** Microsoft Defender Antivirus, puede garantizar **la detección y prevención de amenazas en tiempo real** en su sistema Windows 11.

Sigue estos pasos para activar y actualizar Microsoft Defender Antivirus en tu dispositivo Windows 11:

1. **Comprueba el estado del antivirus**: En primer lugar, comprueba el estado de Microsoft Defender Antivirus en tu sistema. Abre la aplicación **Windows Security** haciendo clic en el menú Inicio, buscando "Windows Security" y seleccionando la aplicación en los resultados de la búsqueda. Una vez abierta la aplicación, ve a la sección **"Protección contra virus y amenazas "** para comprobar el estado de Microsoft Defender Antivirus. Debería estar **activado** por defecto en una instalación nueva de Windows 11.

2. 2. **Habilitar la protección en tiempo real**: En la aplicación Seguridad de Windows, asegúrate de que **la protección en tiempo real** está activada para Microsoft Defender Antivirus. La protección en tiempo real supervisa continuamente su sistema en busca de malware y otras actividades maliciosas, proporcionando **respuesta inmediata** y **bloqueando amenazas** en tiempo real. Si la protección en tiempo real no está activada, haga clic en el **conmutador** para activarla.

3. **Actualizar definiciones**: La actualización periódica de las **definiciones de virus** es crucial para garantizar que Microsoft Defender Antivirus pueda detectar y proteger frente a las amenazas más recientes. En la aplicación Seguridad de Windows, vaya a la sección **"Protección contra virus y amenazas "** y haga clic en el botón **"Buscar actualizaciones "** para actualizar las definiciones del antivirus. Este proceso garantiza que tu sistema esté equipado con las **firmas** y **capacidades de detección** más recientes.

4. **Programar análisis**: Microsoft Defender Antivirus le permite programar **escaneos del sistema** regulares para detectar y eliminar proactivamente cualquier amenaza potencial. En la aplicación Seguridad de Windows, ve a la sección **"Protección contra virus y amenazas "** y haz clic en la opción **"Análisis rápido "** o **"Análisis completo "** para iniciar un análisis. También puedes hacer clic en el enlace **"Opciones de análisis "** para personalizar la configuración del análisis y programar análisis periódicos según tus preferencias.

5. **Configurar opciones adicionales**: Microsoft Defender Antivirus proporciona opciones y características adicionales que puede configurar en función de sus requisitos de seguridad. En la aplicación Seguridad de Windows, explora las distintas secciones como **"Control de aplicaciones y navegadores", "Seguridad de dispositivos "** y **"Firewall y protección de red "** para personalizar la configuración del antivirus y aprovechar las funciones de protección avanzadas.

Habilitar y actualizar regularmente Microsoft Defender Antivirus en Windows 11 es esencial para mantener una fuerte defensa contra el malware y otras amenazas de seguridad. Siguiendo estos pasos y manteniendo Microsoft Defender Antivirus actualizado, puedes asegurarte de que tu sistema Windows 11 está bien protegido.

Tenga en cuenta que, aunque Microsoft Defender Antivirus proporciona una protección sólida, siempre se recomienda practicar **hábitos de navegación seguros**, tener cuidado al **descargar archivos** o **abrir archivos adjuntos de correo electrónico**, y mantener su **sistema operativo y aplicaciones actualizados** para mejorar aún más su postura de seguridad general.

#### 3. **Aplique el aislamiento basado en hardware por defecto**
Windows 11 aprovecha las características de aislamiento basadas en hardware como **Seguridad basada en virtualización (VBS)** e **Integridad de código protegida por hipervisor (HVCI)** para proporcionar una mayor seguridad y proteger los componentes críticos del sistema.

Al habilitar y aplicar estas funciones predeterminadas de aislamiento basado en hardware, puede establecer límites de seguridad sólidos y mitigar varios vectores de ataque. A continuación se indican algunos pasos clave para garantizar una configuración adecuada:

1. **Habilitar la tecnología de virtualización**: En primer lugar, debe comprobar si su sistema es compatible con la tecnología de virtualización y asegurarse de que está activada en la configuración de **BIOS** o **firmware UEFI** del sistema. Los pasos para acceder y habilitar la tecnología de virtualización pueden variar en función del fabricante de la placa base o del firmware. Consulte la documentación del sistema o el sitio web del fabricante para obtener instrucciones específicas.

2. **Habilite la seguridad basada en virtualización (VBS)**: Windows 11 incorpora VBS, que utiliza las capacidades de virtualización del hardware para crear contenedores aislados denominados **Virtual Secure Mode (VSM)**. VSM proporciona un entorno de ejecución seguro para los componentes críticos del sistema, protegiéndolos de posibles ataques. Para habilitar VBS, siga estos pasos:

   - Pulse la **tecla de Windows + R** para abrir el cuadro de diálogo Ejecutar.
   - Escriba "**gpedit.msc**" y pulse **Intro** para abrir el Editor de directivas de grupo locales.
   - Vaya a **Configuración del equipo -> Plantillas administrativas -> Sistema -> Device Guard**.
   - Haga doble clic en la política **"Activar seguridad basada en virtualización "**.
   - Seleccione **"Activado "** y pulse **Aceptar** para aplicar los cambios.

   Habilitar VBS puede requerir hardware compatible y ciertos requisitos del sistema. Consulte la **documentación oficial de Microsoft** para obtener más información.

3. **Habilitar la integridad de código protegida por hipervisor (HVCI)**: HVCI es una característica que utiliza el hipervisor para hacer cumplir las políticas de integridad del código, evitando la ejecución de código no autorizado y mejorando la postura general de seguridad. Para activar HVCI, siga estos pasos:

   - Pulse la **tecla de Windows + R** para abrir el cuadro de diálogo Ejecutar.
   - Escriba "**msconfig**" y pulse **Intro** para abrir la utilidad de Configuración del Sistema.
   - Vaya a la pestaña **"Arranque "**.
   - Haga clic en **"Opciones avanzadas "**.
   - Marque la opción **"Activar integridad de código protegida por hipervisor "**.
   - Haga clic en **Aceptar** para guardar los cambios y reiniciar el sistema.

   Habilitar HVCI requiere hardware compatible y ciertos requisitos del sistema. Consulte la **documentación oficial de Microsoft** para más detalles.

Al aplicar las características predeterminadas de aislamiento basado en hardware, como VBS y HVCI, puede mejorar significativamente la postura de seguridad de su sistema Windows 11. Estas características ayudan a proteger los componentes críticos del sistema de varios tipos de amenazas. Estas características ayudan a proteger los componentes críticos del sistema de varios ataques, incluyendo aquellos que intentan modificar o explotar el código y las configuraciones del sistema.

Asegúrese de actualizar periódicamente su sistema con los últimos parches de seguridad y actualizaciones de firmware para beneficiarse de las mejoras de seguridad y mitigaciones más actualizadas que ofrecen estas características de aislamiento basadas en hardware.

Tenga en cuenta que la disponibilidad y los requisitos de las funciones de aislamiento basadas en hardware pueden variar en función de la configuración de su sistema y de la edición de Windows 11. Se recomienda consultar la **documentación oficial de Microsoft** y realizar comprobaciones de compatibilidad para garantizar la correcta implementación de estas funciones de seguridad.

#### 4. [**Use Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)
**Windows Sandbox** es una valiosa herramienta que le permite ejecutar aplicaciones no fiables o software de prueba en un entorno aislado, proporcionando una capa adicional de seguridad para su sistema. Mediante el uso de Windows Sandbox, puede mitigar los riesgos potenciales asociados con la ejecución de programas no confiables.

Windows Sandbox crea un entorno de escritorio ligero y temporal que está completamente separado de su sistema operativo principal. Cualquier cambio realizado dentro del Sandbox se descarta una vez que lo cierras, asegurando que tu sistema principal no se vea afectado.

Para utilizar Windows Sandbox, siga estos pasos:

1. **Compruebe los requisitos del sistema**: Antes de continuar, asegúrate de que tu sistema cumple los requisitos para ejecutar Windows Sandbox. Por lo general, necesitas una edición Windows 10 Pro o Enterprise y un procesador con capacidades de virtualización habilitadas en el firmware BIOS/UEFI. Consulta la página oficial de [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) para conocer los requisitos específicos del sistema.

2. **Habilitar Windows Sandbox**: Windows Sandbox es una característica integrada en las ediciones Pro y Enterprise de Windows 10. Para habilitar Windows Sandbox, siga estos pasos:

   - Pulsa la **tecla Windows + R** para abrir el cuadro de diálogo Ejecutar.
   - Escribe "**appwiz.cpl**" y pulsa **Intro** para abrir la ventana Programas y características.
   - Haz clic en **"Activar o desactivar características de Windows "** en la parte izquierda.
   - Desplázate hacia abajo y localiza **"Windows Sandbox "** en la lista de características.
   - Marca la casilla junto a **"Windows Sandbox "** y haz clic en **Aceptar** para activarlo.
   - Windows instalará los componentes necesarios y es posible que tengas que reiniciar el sistema para que los cambios surtan efecto.

3. 3. **Inicie Windows Sandbox**: Una vez que Windows Sandbox está habilitado, puede iniciarlo siguiendo estos pasos:

   - Abre el menú **Inicio** y busca **"Windows Sandbox "**.
   - Haz clic en la aplicación **"Windows Sandbox "** para abrirla.
   - El Sandbox se iniciará en una ventana independiente, proporcionándote un entorno seguro para ejecutar aplicaciones no fiables o software de prueba.

Mientras ejecutas aplicaciones en Windows Sandbox, ten en cuenta que el entorno Sandbox está aislado y diseñado para descartar cualquier cambio realizado en su interior. Por lo tanto, es crucial que guardes tus archivos o datos fuera del Sandbox si necesitas conservarlos.

El entorno de pruebas de Windows es una herramienta eficaz para probar software desconocido, abrir archivos sospechosos o explorar sitios web potencialmente peligrosos. Añade una capa extra de protección asegurando que cualquier actividad maliciosa o cambios no deseados queden confinados dentro del Sandbox y no afecten a tu sistema operativo principal.

Al incorporar Windows Sandbox a sus prácticas de seguridad, puede reducir significativamente los riesgos asociados con la ejecución de aplicaciones no confiables, protegiendo su sistema de amenazas potenciales.

Para obtener más información sobre Windows Sandbox y su uso, consulte la página oficial [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

#### 5. [**Implement Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)
Microsoft Defender Application Guard es una potente función de seguridad que aísla las sesiones del navegador Microsoft Edge del sistema operativo subyacente. Al ejecutar Edge en un entorno seguro y aislado, Application Guard ayuda a proteger el sistema frente a ataques basados en el navegador y sitios web maliciosos.

Para implementar Microsoft Defender Application Guard y mejorar la seguridad de su navegador, siga estos pasos:

1. **Comprobar compatibilidad**: Antes de continuar, asegúrese de que su sistema cumple los requisitos para ejecutar Microsoft Defender Application Guard. Por lo general, necesita una edición Windows 10 Pro o Enterprise, un procesador compatible con capacidades de virtualización y al menos 8 GB de RAM. Consulte la página oficial de [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) para conocer los requisitos específicos del sistema.

2. **Activar Application Guard**: Application Guard está disponible como una característica opcional en Windows 10. Para habilitar Microsoft Defender Application Guard, siga estos pasos:

   - Pulsa la **tecla de Windows + R** para abrir el cuadro de diálogo Ejecutar.
   - Escribe "**appwiz.cpl**" y pulsa **Intro** para abrir la ventana Programas y características.
   - Haz clic en **"Activar o desactivar características de Windows "** en la parte izquierda.
   - Desplázate hacia abajo y localiza **"Microsoft Defender Application Guard "** en la lista de características.
   - Marca la casilla junto a **"Microsoft Defender Application Guard "** y haz clic en **Aceptar** para activarlo.
   - Windows instalará los componentes necesarios y es posible que tengas que reiniciar el sistema para que los cambios surtan efecto.

3. **Configurar Application Guard**: Una vez habilitado Application Guard, puede configurar sus parámetros para adaptarlos a sus necesidades de seguridad. Application Guard te permite definir el nivel de aislamiento y controlar cómo gestiona los sitios web y archivos que no son de confianza. Puedes ajustar esta configuración a través de la aplicación **Windows Security** o la configuración de la directiva de grupo.

4. **Probar y verificar**: Después de habilitar y configurar Microsoft Defender Application Guard, es esencial probar y verificar su funcionalidad. Abra Microsoft Edge y visite un sitio web malicioso conocido o un sitio con riesgos potenciales para comprobar si Application Guard aísla correctamente la sesión del navegador y evita posibles ataques.

Al implementar Microsoft Defender Application Guard, agrega una capa adicional de protección a su sistema al aislar las sesiones del navegador y contener cualquier amenaza potencial dentro del entorno seguro. Esto ayuda a proteger el sistema y los datos de ataques basados en el navegador, como descargas no autorizadas, scripts maliciosos y exploits de día cero.

Para obtener información más detallada sobre la configuración y utilización de Microsoft Defender Application Guard, consulte la página oficial [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard)

#### 6. [**Controlled Folder Access**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
El Acceso controlado a carpetas es una potente función de seguridad disponible en Windows 11 que ayuda a proteger las carpetas importantes de cambios no autorizados por ransomware y otros programas maliciosos. Activando el Acceso controlado a carpetas y añadiendo las carpetas necesarias a la lista protegida, puede mejorar la seguridad de su sistema y evitar posibles pérdidas de datos.

Para implementar el Acceso controlado a carpetas y proteger sus carpetas importantes, siga estos pasos:

1. **Abra Seguridad de Windows**: Pulse la **tecla Windows** de su teclado, escriba "**Windows Security**" y seleccione la aplicación **Windows Security** en los resultados de la búsqueda.

2. 2. **Desplácese hasta Configuración de protección frente a virus y amenazas**: En la aplicación Seguridad de Windows, haz clic en la pestaña **"Protección frente a virus y amenazas "** del menú de la izquierda.

3. **Configurar el acceso controlado a carpetas**: En la sección **"Protección contra ransomware "**, haz clic en **"Administrar protección contra ransomware "** para acceder a la configuración del Acceso controlado a carpetas.

4. 4. **Activar el Acceso controlado a carpetas**: En la configuración de Acceso controlado a carpetas, activa el interruptor a **"Activado "** para activar la función. Windows mostrará una advertencia acerca de permitir que sólo las aplicaciones de confianza accedan a las carpetas protegidas.

5. **Agregar carpetas protegidas**: Para especificar qué carpetas deben protegerse, haz clic en **"Carpetas protegidas "** y selecciona **"Añadir una carpeta protegida "**. Elija las carpetas que desea proteger y haga clic en **"Aceptar "**.

   - Se recomienda añadir carpetas importantes como Documentos, Imágenes, Vídeos y cualquier otro directorio que contenga datos valiosos.

6. **Permitir o Bloquear Aplicaciones**: Por defecto, el Acceso Controlado a Carpetas permite a las aplicaciones de confianza acceder a las carpetas protegidas. Sin embargo, puedes personalizar este comportamiento haciendo clic en **"Permitir una aplicación a través del Acceso controlado a carpetas "**. Desde ahí, puedes permitir o bloquear que aplicaciones específicas accedan a las carpetas protegidas.

7. **Monitorizar y revisar**: Tras habilitar el Acceso controlado a carpetas, Windows supervisará y registrará continuamente cualquier intento de acceso a las carpetas protegidas por parte de aplicaciones no autorizadas. Puedes revisar estos registros haciendo clic en **"Revisar "** en la sección **"Aplicaciones bloqueadas recientemente "** de la configuración de Acceso controlado a carpetas.

Al implementar el Acceso Controlado a Carpetas, añades una capa extra de protección a tus carpetas importantes, mitigando el riesgo de cambios no autorizados y la potencial pérdida de datos causada por ataques de ransomware. Revise periódicamente la configuración del Acceso controlado a carpetas para asegurarse de que las carpetas protegidas se ajustan a sus requisitos de seguridad.

Para obtener información más detallada sobre la configuración y el uso del Acceso controlado a carpetas, consulte el documento oficial [**Microsoft documentation**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide)


#### 7. **Habilitar el Mantenimiento Automático de Windows**
Windows 11 incluye una práctica función llamada Mantenimiento automático que ayuda a mantener el sistema optimizado y protegido mediante la realización de tareas de mantenimiento periódicas. Al habilitar el Mantenimiento automático, te aseguras de que tu sistema funcione sin problemas y siga siendo seguro.

Para habilitar el Mantenimiento automático de Windows, siga estos pasos:

1. **Abre la Configuración de Windows**: Pulsa la **tecla Windows** del teclado, escribe "**Configuración**" y selecciona la aplicación **Configuración** de los resultados de la búsqueda.

2. **Acceder a los Ajustes de Mantenimiento**: En la aplicación Configuración, haz clic en la categoría **"Sistema "** y selecciona **"Acerca de "** en el menú de la izquierda. Desplázate hasta el final de la página y haz clic en el enlace **"Información del sistema "**.

3. **Abrir Configuración de mantenimiento**: En la ventana Información del sistema, haz clic en el enlace **"Mantenimiento "** situado en la parte inferior de la página.

4. 4. **Activar el mantenimiento automático**: En los ajustes de mantenimiento, cambie el interruptor situado junto a **"Mantenimiento automático "** a la posición **"Activado "**.

5. 5. **Configurar las opciones de mantenimiento**: Por defecto, Windows programará automáticamente las tareas de mantenimiento para que se ejecuten diariamente a las 2:00 AM. Si prefiere un horario diferente, haga clic en **"Cambiar configuración de mantenimiento "** y personalice las opciones deseadas, como la hora de inicio del mantenimiento y la frecuencia de las tareas de mantenimiento.

6. **Ver ajustes adicionales**: Debajo del conmutador de Mantenimiento automático, puedes encontrar ajustes adicionales relacionados con el mantenimiento, como **"Permitir que el mantenimiento programado despierte mi ordenador a la hora programada "** y **"Permitir que el mantenimiento programado se ejecute incluso cuando estoy con batería "**. Ajusta estas opciones según tus preferencias y necesidades.

7. **Supervisar las actividades de mantenimiento**: Una vez activado el Mantenimiento Automático, Windows realizará automáticamente tareas de mantenimiento en segundo plano a la hora programada. Puede supervisar estas actividades comprobando la sección **"Mantenimiento "** en la aplicación **"Seguridad de Windows "** o revisando los registros de **"Mantenimiento "** en el Visor de sucesos.

Activar el Mantenimiento Automático de Windows asegura que tu sistema se mantiene optimizado y protegido realizando regularmente tareas de mantenimiento esenciales como actualizaciones de software, optimización de disco y escaneos de seguridad. Al mantener su sistema en buen estado, puede disfrutar de una experiencia informática más fluida y segura.

Para obtener información más detallada sobre el Mantenimiento automático de Windows y sus opciones de configuración, consulte la página oficial [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence)

______

{{< inarticle-dark >}}

## Conclusión

Implementar estas **mejores prácticas de hardening de Windows** es esencial para garantizar la seguridad de sus sistemas Windows. Al **actualizar regularmente su sistema operativo**, puede parchear vulnerabilidades de seguridad y mejorar la estabilidad del sistema. Habilitar funciones de seguridad como **antivirus** y **cifrado** añade una capa adicional de protección a sus datos. Configurar **controles de acceso** adecuados ayuda a evitar cambios no autorizados y restringe el acceso a recursos sensibles.

Siguiendo estas buenas prácticas, puede mejorar la seguridad de su **entorno Windows**, proteger sus datos y mantener la integridad de su **infraestructura digital**. Es importante mantenerse **proactivo** y revisar y actualizar periódicamente sus medidas de seguridad para adelantarse a las posibles amenazas.

Recuerde que el **endurecimiento de Windows** es un proceso continuo, y es esencial mantenerse informado sobre las últimas actualizaciones y prácticas de seguridad. Si se mantiene proactivo y aplica estas prácticas recomendadas, podrá mitigar eficazmente los riesgos de seguridad y garantizar la seguridad de sus sistemas Windows.

Para obtener más información sobre el refuerzo de Windows y las prácticas recomendadas, consulte fuentes fiables como **la documentación de Microsoft**, **foros de seguridad** y **sitios web de ciberseguridad** de confianza.

______

## Referencias:

- [Microsoft Windows Security](https://www.microsoft.com/en-us/security)
- [NIST Special Publication 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [CIS Microsoft Windows 10 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [CIS Microsoft Windows 11 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_11/)