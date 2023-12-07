---
title: "Precarga HSTS Cómo mejorar la seguridad de los sitios web: Guía paso a paso"
date: 2023-08-20
toc: true
draft: false
description: "Aprenda a mejorar la seguridad de los sitios web y la confianza de los usuarios precargando la configuración HSTS en Chrome y Firefox. Sigue nuestra guía paso a paso para una implementación perfecta."
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "Ilustración en estilo de dibujos animados de un sitio web protegido con un candado, que representa una mayor seguridad y protección contra las ciberamenazas."
coverCaption: "Refuerce la defensa de su sitio web, adopte la precarga HSTS."
---

## **Mejore la seguridad de su sitio web con la precarga HSTS: Guía paso a paso**

HTTP Strict Transport Security (HSTS) es un **mecanismo de seguridad crucial** que garantiza que los sitios web apliquen conexiones HTTPS para **proteger a los usuarios de posibles amenazas a la seguridad**. Al precargar la configuración HSTS en Chrome y Firefox, puedes **mejorar la seguridad de los sitios web** y generar **confianza en los usuarios**. En esta completa guía, te guiaremos a través de los **pasos esenciales** para precargar con éxito la configuración HSTS y te proporcionaremos **recomendaciones útiles** para optimizar la seguridad.

______

### Comprender la precarga HSTS

**La precarga HSTS es el proceso de enviar el dominio de su sitio web a las listas de precarga de los principales navegadores. Una vez añadido, estos navegadores **aplicarán automáticamente conexiones HTTPS** para su dominio y todos los subdominios. Esto garantiza que los usuarios siempre accedan a su sitio web de forma segura, reduciendo el riesgo de **ataques de intermediario** y escuchas no autorizadas. Para más detalles sobre la precarga HSTS, puede consultar la página oficial [documentation](https://hstspreload.org/)

______

______

### **Requisitos de presentación**

Antes de enviar su dominio para la precarga HSTS, asegúrese de que su sitio web cumple los siguientes **requisitos esenciales**:

1. **Certificado válido**: Su sitio web debe servir un **certificado SSL o TLS válido** para permitir **conexiones HTTPS seguras**.

2. **Redirección HTTP a HTTPS**: Asegúrese de que todas las **solicitudes HTTP son redirigidas** a sus **contrapartes HTTPS** cuando su sitio web escucha en el puerto 80.

3. 3. **HTTPS para todos los subdominios**: Todos los subdominios de su sitio web deben **soportar conexiones HTTPS** para poder optar a la precarga HSTS.

4. **Cabecera HSTS en el dominio base**: Incluya un **encabezado HSTS** en su dominio base para solicitudes HTTPS con la siguiente configuración:
   - `max-age` debe ser **al menos 31536000 segundos** (1 año).
   - El `includeSubDomains` para incluir todos los subdominios.
   - La directiva `preload` para solicitar la inclusión en la lista de precarga.

He aquí un ejemplo de cabecera HSTS válida:

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

### **Cómo precargar la configuración HSTS**

Si su sitio web está **comprometido con HTTPS** y cumple los requisitos anteriores, siga estos **pasos cruciales** para precargar correctamente su configuración HSTS:

1. **Examine los subdominios**: Asegúrese de que todos los **subdominios de su sitio web** funcionan correctamente sobre HTTPS para proporcionar una experiencia de navegación fluida a los usuarios.

2. 2. **Aumento gradual**: Para probar y solucionar cualquier problema potencial, añada la cabecera **HSTS** a sus respuestas HTTPS con un **low `max-age` (por ejemplo, 300 segundos). Aumente gradualmente el `max-age` valor por etapas:
   - 5 minutos: `max-age=300; includeSubDomains`
   - Una semana: `max-age=604800; includeSubDomains`
   - 1 mes: `max-age=2592000; includeSubDomains`

3. **Supervisar las métricas**: Durante cada etapa, **supervise de cerca las métricas de su sitio web**, incluidos el tráfico y los ingresos, para identificar y abordar cualquier problema antes de pasar a la siguiente etapa.

4. **Aumentar la antigüedad máxima a 2 años**: Una vez que esté **seguro de que no hay más problemas**, establezca la edad máxima en 2 años. `max-age` a **2 años (63072000 segundos)** y añada el `preload` a la cabecera HSTS:
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5. **Envíe su sitio web**: Después de aplicar los 2 años `max-age` envíe su sitio** a la lista de precarga HSTS mediante el formulario disponible en [hstspreload.org](https://hstspreload.org/) Tenga en cuenta que la inclusión en la lista de precarga puede tardar varios meses en llegar a los usuarios con una actualización de Chrome.
______

### **Opt-In para la precarga HSTS: Empoderando a los Operadores de Sitios**

Apoyar la precarga HSTS es una **excelente práctica de seguridad** que mejora la protección del sitio web. Sin embargo, debe ser una decisión **opt-in** para los operadores del sitio. Si proporciona **consejos de configuraciónHTTPS** u ofrece una opción para activar HSTS, **evite incluir la opción `preload` por defecto**. Este enfoque evita la inclusión involuntaria en la lista de precarga, lo que puede provocar dificultades para acceder a determinados subdominios.

Para garantizar una experiencia sin problemas, **informe a los operadores del sitio** sobre las **consecuencias a largo plazo** de la precarga y haga hincapié en la **importancia de cumplir todos los requisitos** antes de habilitar HSTS para su dominio.

______

### **Eliminación de la lista de precarga: Una decisión deliberada**

La inclusión en la lista de precarga es una **decisión permanente** que no puede deshacerse fácilmente. Sin embargo, si encuentra **razones técnicas o de coste** de peso que impidan la compatibilidad con HTTPS para determinados subdominios, tiene la opción de solicitar la **eliminación de la lista de precarga de Chrome** a través de la función [removal form](https://hstspreload.org/removal/)

Asegúrate de haber evaluado cuidadosamente las implicaciones antes de tomar esta importante decisión.
______

______

### **Una navegación más segura comienza con la precarga HSTS**

En conclusión, precargar su configuración HSTS en Chrome y Firefox es un **paso proactivo** hacia una experiencia de navegación web más segura para sus usuarios. Al **reforzar las conexiones HTTPS**, usted **protege los datos confidenciales** y genera **confianza** entre sus visitantes. Siga las **directrices** mencionadas anteriormente para **precargar la configuración HSTS** correctamente y disfrutar de una **mayor seguridad del sitio web**.

______

### Referencias

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)
