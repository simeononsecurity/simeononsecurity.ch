---
title: "Tarjetas Virtuales de Privacy.com: Cómo Funciona la Privacidad en los Pagos"
date: 2023-09-03
lastmod: 2026-10-08
toc: true
draft: false
description: Qué se almacena en una tarjeta de pago, por qué la banda magnética es la parte más débil, qué ve un comerciante cuando pagas con un número virtual y cómo funcionan en la práctica los tipos y límites de tarjetas de Privacy.com.
genre:
- Seguridad en Pagos
- Privacidad Digital
- Tarjetas Virtuales
- Privacidad Financiera
- Prevención de Fraudes
- Seguridad del Consumidor
tags:
- privacy.com
- tarjetas virtuales
- tarjetas de débito virtuales
- tarjetas de un solo uso
- tarjetas bloqueadas por comerciante
- tarjetas bloqueadas por categoría
- tokenización
- token de red
- PAN
- CVV
- skimming de tarjetas
- banda magnética
- pista 1
- pista 2
- seguridad de tarjetas de pago
- fraude con tarjetas de crédito
- gestión de suscripciones
- límites de gasto
- PCI DSS
- SOC 2
- fraude sin presencia de tarjeta
- privacidad financiera
- privacidad en pagos
- número de tarjeta virtual
- tarjeta enmascarada
- controles de tarjeta
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: Una ilustración digital que muestra una tarjeta virtual protegida con un escudo que protege un símbolo de candado, representando la seguridad y privacidad que ofrecen las tarjetas de débito virtuales.
coverCaption: Protege, Controla y Asegura Tus Transacciones en Línea.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Una tarjeta virtual hace una cosa específica: cambia lo que el comerciante recibe, no lo que tu banco sabe.** Este es todo el mecanismo, y entenderlo explica tanto la protección que obtienes como la que no.

La mayoría de las coberturas tratan las tarjetas virtuales como una herramienta general de privacidad y omiten el detalle técnico. Este artículo cubre qué se almacena en una tarjeta, por qué la banda magnética es el punto débil y cómo se comportan en la práctica los tipos de tarjetas de Privacy.com.

*El beneficio práctico es limitado y real: un número robado se vuelve inútil para un ladrón, porque solo funciona en el comerciante para el que fue emitido.*

## La Respuesta Corta

| Pregunta | Respuesta Corta |
|---|---|
| **¿Qué cambia una tarjeta virtual?** | El número que el comerciante almacena. Tus datos reales nunca les llegan |
| **¿Es privada la transacción?** | No. Tu banco, la red y el emisor aún la ven |
| **¿Qué evita que una brecha te perjudique?** | Un número bloqueado por comerciante o de un solo uso, que falla en cualquier otro lugar |
| **¿Cuál es la parte más débil de una tarjeta física?** | La banda magnética, que almacena los datos completos de la pista sin cifrar |
| **¿Construye crédito?** | No. Estas no son cuentas de crédito y no se realiza consulta crediticia |
| **¿Quién califica para Privacy.com?** | Ciudadanos o residentes legales de EE.UU., mayores de 18 años, con cuenta corriente en banco o cooperativa de crédito de EE.UU. |

## Qué Hay en una Tarjeta de Pago

**Tres cosas autorizan una transacción sin presencia de tarjeta: el número de cuenta principal, la fecha de expiración y el valor de verificación.**

| Elemento | Longitud | Origen |
|---|---|---|
| **Número de Cuenta Principal (PAN)** | Hasta 19 dígitos | El emisor, con dígitos iniciales que identifican el esquema y banco |
| **Expiración** | Cuatro dígitos en formato MM/AA | El emisor |
| **CVV o CVC** | Tres o cuatro dígitos | Derivado del PAN, expiración y una clave que solo el emisor posee |
| **Nombre del titular** | Hasta 26 caracteres | Aparece solo en la Pista 1 de la banda magnética |

**El PAN no es una cadena aleatoria.** El primer dígito identifica el esquema, los siguientes varios identifican el banco emisor y el resto identifica la cuenta. La estructura permite verificar la plausibilidad del número sin contactar a nadie, y por eso el dígito de control Luhn detecta un solo dígito transpuesto.

**El CVV es lo que prueba que alguien tuvo físicamente la tarjeta** cuando fue emitida. No se almacena en la banda magnética, que es exactamente por qué un skimmer que copia la banda nunca lo obtiene.

*Inspecciona todo esto tú mismo con el **[Decodificador y Codificador de Banda Magnética](/magnetic-stripe-decoder/)**, que analiza la Pista 1 y la Pista 2, decodifica los dígitos del código de servicio y vuelve a codificar el resultado. Funciona completamente en tu navegador, lo cual es importante porque este es el contenido completo de una tarjeta de pago.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagrama que muestra los elementos de una tarjeta de pago incluyendo el número de cuenta principal, fecha de expiración, CVV y las tres pistas de la banda magnética con lo que cada una contiene" >}}

## Por Qué la Banda Magnética Es el Punto Débil

**La banda almacena datos de cuenta en texto plano, y cualquier lector compatible los lee.**

Una banda magnética tiene hasta tres pistas. La Pista 1 lleva el PAN, el nombre del titular, la expiración y un código de servicio de tres dígitos, y es la única pista que contiene texto alfabético. La Pista 2 lleva el PAN, expiración y código de servicio en una codificación numérica más densa, y **la Pista 2 es la que casi todos los terminales punto de venta leen.** La Pista 3 es prácticamente no usada por las redes principales y a menudo ni siquiera está presente en la tarjeta.

El código de servicio es importante porque describe el uso permitido de la tarjeta. El dígito uno cubre reglas de intercambio, el dos el manejo de autorizaciones y el tres el rango de servicios. Una tarjeta codificada `201` permite intercambio internacional, no necesita ruta especial de autorización y no tiene restricciones de servicio.

La historia explica por qué la banda duró tanto. En 1969 un ingeniero de IBM llamado Forrest Parry intentó pegar cinta magnética a una tarjeta plástica y no logró que se adhiriera sin dañarla. Su esposa sugirió usar una plancha de ropa, y el calor unió la cinta a la tarjeta. La improvisación se convirtió en estándar por más de medio siglo.

Dos desarrollos están terminando con esto:

| Hito | Estado |
|---|---|
| **Mastercard anunció la eliminación de la banda** | Para 2033, ninguna tarjeta Mastercard de crédito o débito la tendrá |
| **Europa** | Las bandas comenzaron a desaparecer de las tarjetas Mastercard en 2024 |
| **Estados Unidos** | Los bancos dejarán de emitirlas a partir de 2027 |

*La banda fue reemplazada por chip y pagos sin contacto porque copiarla no requiere más habilidad que tener un lector. Nuestra **[herramienta de banda magnética](/magnetic-stripe-decoder/)** muestra cuán pocos datos se necesitan para reconstruir una pista funcional.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagrama de una banda magnética mostrando la posición física de las pistas uno, dos y tres, con el diseño de campos de cada pista incluyendo centinelas, PAN, nombre, expiración y código de servicio" >}}

## Cómo Leer Datos de la Pista

**Una cadena de banda magnética es una secuencia de campos, no un segundo número de tarjeta.** El lector encuentra el centinela de inicio, separa campos, lee la expiración y el código de servicio, luego verifica el centinela de fin y el LRC.

| Pista | Inicio | Campos principales | Fin | Conjunto de caracteres |
|---|---|---|---|---|
| **Pista 1** | `%` | Código de formato, PAN, nombre, fecha de expiración, código de servicio, datos discrecionales | `?` más LRC | ALFA de seis bits, por lo que lleva letras |
| **Pista 2** | `;` | PAN, fecha de expiración, código de servicio, datos discrecionales | `?` más LRC | BCD de cuatro bits, por lo que lleva dígitos y un pequeño conjunto de puntuación |

Los centinelas opcionales identifican los límites físicos del registro. Un decodificador a menudo los omite cuando muestra los campos, pero un codificador físico necesita el formato completo del registro esperado por el lector.

### Ejemplo de Pista 1

Este es un ejemplo sintético. Usa el PAN de prueba estándar de la herramienta y un nombre falso, fecha de expiración, código de servicio y datos discrecionales. No es una tarjeta de Privacy.com y no es un dato de pago válido.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Léalo de izquierda a derecha:

| Segmento | Valor | Significado |
|---|---|---|
| **Centinela de inicio** | `%` | Comienzo del registro de Pista 1 |
| **Código de formato** | `B` | Formato de tarjeta financiera B |
| **PAN** | `4111111111111111` | Número de cuenta principal sintético |
| **Separador de campo** | `^` | Fin del PAN y comienzo del nombre |
| **Nombre** | `TEST/USER` | Apellido, separador, nombre |
| **Separador de campo** | `^` | Fin del nombre y comienzo de campos de transacción |
| **Fecha de expiración** | `2912` | Diciembre 2029 en formato AAMM |
| **Código de servicio** | `501` | Intercambio nacional, procesamiento normal, sin restricciones |
| **Datos discrecionales** | `0000000` | Relleno definido por el emisor en este ejemplo |
| **Centinela de fin** | `?` | Fin de datos de Pista 1 antes del LRC |

El registro codificado real también lleva un carácter LRC después del centinela de fin cuando el lector lo espera. La forma de texto visible es útil para estudiar la estructura. La representación a nivel de bits también lleva paridad impar para cada carácter.

### Ejemplo de Pista 2

La Pista 2 elimina el nombre y el código de formato. Los mismos valores sintéticos se convierten en:

```text
;4111111111111111=291250100000000?
```

| Segmento | Valor | Significado |
|---|---|---|
| **Centinela de inicio** | `;` | Comienzo del registro de Pista 2 |
| **PAN** | `4111111111111111` | Número de cuenta principal sintético |
| **Separador** | `=` | Fin del PAN y comienzo de campos de transacción |
| **Fecha de expiración** | `2912` | Diciembre 2029 en formato AAMM |
| **Código de servicio** | `501` | Mismo código de servicio sintético que Pista 1 |
| **Datos discrecionales** | `0000000` | Relleno definido por el emisor en este ejemplo |
| **Centinela de fin** | `?` | Fin de datos de Pista 2 antes del LRC |

**La Pista 2 es más corta porque no tiene el nombre del titular.** Muchos terminales leen la Pista 2 para transacciones ordinarias con deslizamiento, mientras que la Pista 1 proporciona el campo de nombre cuando un lector lo solicita.

### Dígitos del Código de Servicio

**Los tres dígitos del código de servicio describen el comportamiento del terminal y la autorización.** No contienen el CVV, y cambiarlos en una tarjeta real sin autorización del emisor produce una credencial de pago malformada o engañosa.

| Dígito | Valores | Qué describe |
|---|---|---|
| **Primero** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Reglas de intercambio y preferencia de chip |
| **Segundo** | `0`, `1`, `2`, `4` | Ruta de autorización |
| **Tercero** | `0` hasta `7` | Restricciones de PIN, efectivo, bienes y servicios |

**El primer dígito** cubre intercambio y preferencia de chip:

| Valor | Significado |
|---|---|
| `0` | Uso nacional |
| `1` | Intercambio internacional permitido |
| `2` | Intercambio internacional, usar IC (chip) cuando sea posible |
| `5` | Solo intercambio nacional excepto bajo acuerdo bilateral |
| `6` | Solo intercambio nacional excepto bajo acuerdo bilateral, usar IC cuando sea posible |
| `7` | Sin intercambio excepto bajo acuerdo bilateral (circuito cerrado) |
| `9` | Prueba |

**El segundo dígito** cubre el manejo de autorización:

| Valor | Significado |
|---|---|
| `0` | Autorización normal |
| `1` | Autorización normal |
| `2` | Contactar al emisor por medios en línea |
| `4` | Contactar al emisor por medios en línea excepto bajo acuerdo bilateral |

**El tercer dígito** cubre restricciones de servicio:

| Valor | Significado |
|---|---|
| `0` | Sin restricciones, se requiere PIN |
| `1` | Sin restricciones |
| `2` | Solo bienes y servicios (no efectivo) |
| `3` | Solo cajero automático, se requiere PIN |
| `4` | Solo efectivo |
| `5` | Solo bienes y servicios (no efectivo), se requiere PIN |
| `6` | Sin restricciones, usar PIN cuando sea posible |
| `7` | Solo bienes y servicios (no efectivo), usar PIN cuando sea posible |

Por ejemplo, `201` significa intercambio internacional con uso de chip cuando sea posible, procesamiento normal de autorización y sin restricciones de servicio. El decodificador expone cada dígito por separado para que no tengas que memorizar la tabla.

### LRC y Paridad

**El LRC es un carácter de verificación, no otro campo para inventar.** El codificador aplica XOR al valor de datos de cada carácter desde el centinela de inicio hasta el centinela de fin. Convierte el resultado de nuevo al rango de caracteres imprimibles de la pista y reporta los bits de paridad impar codificados por separado.

La Pista 1 usa un conjunto de caracteres ALFA de seis bits. Su valor de datos es el código ASCII menos `0x20`. La Pista 2 usa un conjunto de caracteres BCD de cuatro bits. Su valor de datos es el nibble bajo del código ASCII. Aplicar el mapeo de Pista 1 a Pista 2 produce un LRC incorrecto.

La opción del decodificador **Incluir LRC calculado** añade el carácter LRC imprimible a la salida. Su desglose también muestra el patrón de bits LRC con paridad impar. Úsalo para aprender cómo un lector verifica el registro, no para eludir los controles del emisor.

## Escritura de Tarjetas Sintéticas para Pruebas

**Usa el decodificador para escribir cadenas de prueba, no tarjetas de pago reales.** La herramienta acepta campos, reconstruye Pista 1 y Pista 2, añade centinelas opcionales y calcula el LRC. Se ejecuta localmente en el navegador.

1. Abra el **[Decodificador y Codificador de Banda Magnética](/magnetic-stripe-decoder/)**.
2. Seleccione **Cargar tarjeta de prueba**. Esto llena la herramienta con el PAN sintético `4111111111111111`, el nombre `TEST/USER`, la fecha de expiración `2912`, el código de servicio `201` y datos discrecionales de prueba.
3. Active **Incluir centinelas de inicio y fin** para mostrar los límites físicos del registro.
4. Active **Incluir LRC calculado** para añadir el carácter de verificación calculado.
5. Active **Dividir datos discrecionales en PVKI, PVV y CVV** solo para ver cómo se muestra un campo sintético de nueve dígitos. Esas etiquetas son convenciones del emisor, no un diseño universal de la Pista 1 o Pista 2.
6. Cambie el nombre, la fecha de expiración, el código de servicio o los datos discrecionales sintéticos. La salida se actualiza mientras escribe.
7. Compare los campos decodificados con las cadenas generadas. Limpie los campos cuando termine.

Para un ejercicio sintético de la Pista 1, use:

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

Para un ejercicio sintético de la Pista 2, use el mismo PAN, fecha de expiración, código de servicio y un campo discrecional numérico. La cadena generada de la Pista 2 omite el nombre porque la Pista 2 no tiene campo de nombre.

**No copie un PAN, fecha de expiración, CVV o valor discrecional real de Privacy.com en una tarjeta escribible.** Privacy.com describe su producto como números de tarjeta virtuales creados a través de su sitio web o aplicación. Su página oficial no presenta el servicio como un sistema para escribir bandas magnéticas, y un número de tarjeta virtual no es prueba de un registro físico autorizado por el emisor. Una tarjeta de prueba escribible que contenga una credencial real crea un instrumento de pago duplicado y viola los términos del emisor o las reglas de pago.

El límite seguro es simple: use la muestra sintética incorporada en la herramienta, use una tarjeta de laboratorio con valores ficticios y use una tarjeta física aprobada por el emisor cuando necesite pagar en persona. No intente convertir una tarjeta virtual de Privacy.com en una tarjeta física para deslizar.

## Lo que Cambia una Tarjeta Virtual

**Una tarjeta virtual es un segundo número que se interpone delante del primero.**

Cuando paga con una tarjeta virtual, el comerciante recibe un número, una fecha de expiración y un CVV pertenecientes a la tarjeta virtual. Su PAN real nunca les llega. Prácticamente, el cambio se nota después de una brecha:

| Escenario | Con Su Tarjeta Real | Con una Tarjeta Virtual Bloqueada para el Comerciante |
|---|---|---|
| **Base de datos del comerciante filtrada** | El número es válido en todos los lugares donde se acepta | El número falla en todos los demás comerciantes |
| **Suscripción que canceló** | Los cargos continúan hasta que los dispute | Cierra la tarjeta y el cargo falla |
| **Prueba que se convierte silenciosamente** | Cargo no deseado en su estado de cuenta | El límite o cierre lo detiene |
| **Detalles de la tarjeta vendidos en un foro** | Usable para fraude sin presencia de tarjeta | Usable solo en un comerciante, si acaso |

**Lo que no cambia importa igual.** Su banco aún ve la transacción. La red de tarjetas aún la procesa. El emisor aún tiene su identidad, porque las reglas contra el lavado de dinero requieren verificación. **Una tarjeta virtual reduce la exposición del lado del comerciante. No es una forma de gastar anónimamente.**

*La distinción confunde a la gente constantemente. Si su modelo de amenaza incluye al emisor o a la red, una tarjeta virtual no cambia nada al respecto.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagrama que muestra un número de tarjeta virtual que va al comerciante mientras el número real de la tarjeta permanece entre el titular y el banco emisor" >}}

## Los Tres Tipos de Objeto con Forma de Tarjeta

La terminología se usa de forma inconsistente, y la diferencia importa cuando elige qué entregar a un comerciante.

| Tipo | Número de Tarjeta | Versión Física | Uso Típico |
|---|---|---|---|
| **Tarjeta digital** | Igual que su tarjeta física | Sí | Añadir su tarjeta existente a una billetera móvil |
| **Tarjeta virtual** | Diferente de cualquier tarjeta física | No | Compras en línea, suscripciones, comerciantes ocasionales |
| **Tarjeta digital-primero** | Diferente, con una tarjeta física vinculada opcional | Opcional | Cuentas fintech donde la tarjeta física no lleva detalles impresos |

**Una billetera móvil usa un mecanismo completamente distinto.** Cuando añade una tarjeta a una billetera, esta almacena un token específico del dispositivo en lugar de su PAN, y el comerciante recibe el token. Esto se llama tokenización, y es por eso que pagar con un teléfono es más seguro que entregar la tarjeta física incluso sin una tarjeta virtual.

*La tokenización de red y las tarjetas virtuales resuelven partes superpuestas del mismo problema. La tokenización protege el número en tránsito y en reposo. Una tarjeta virtual lo protege de lo que el comerciante retiene después.*

## Tipos de Tarjetas Privacy.com

**Privacy.com ofrece cuatro comportamientos de tarjeta, y no son intercambiables.**

| Tipo de Tarjeta | Comportamiento | Mejor Para |
|---|---|---|
| **De un solo uso** | Se cierra automáticamente después de una transacción | Compras únicas y comerciantes desconocidos |
| **Bloqueada para comerciante** | Se bloquea al primer comerciante que la use y falla en otros | Compras en línea diarias |
| **Bloqueada por categoría** | Restringida a una categoría de gasto | Contener toda una clase de gasto |
| **En todas partes** | Tarjeta física con el mismo modelo de protección | Compras en persona |

**El bloqueo por comerciante es el mecanismo que aporta la mayor parte del valor.** Una tarjeta bloqueada falla en cualquier comerciante que no sea el primero que la usó, lo que significa que una brecha en ese comerciante produce un número inútil en otros lugares.

**El uso único es la opción más fuerte donde aplica.** Una tarjeta que se cierra tras un cargo no puede ser reutilizada y elimina la necesidad de recordar cerrarla después.

Dos detalles operativos que vale la pena conocer:

- **Las tarjetas compartidas se bloquean al primer comerciante con el que se usan**, por lo que compartir una con un familiar o empleado sigue llevando la restricción de comerciante.
- **Una tarjeta se pausa en lugar de cerrarse.** Pausar es reversible, lo que es útil cuando quiere detener una suscripción temporalmente sin perder los detalles de la tarjeta.

## Límites y Controles de Gasto

**Cada tarjeta tiene un límite de gasto, que es un control separado del bloqueo por comerciante.**

| Control | Qué Previene |
|---|---|
| **Límite por transacción** | Un cargo único mayor al autorizado |
| **Límite mensual** | Cargos acumulados durante un período de facturación |
| **Pausa** | Cualquier cargo, de forma reversible |
| **Cierre** | Cualquier cargo futuro, de forma permanente |

**Establezca tanto un límite por transacción como un límite mensual en cualquier tarjeta vinculada a una suscripción.** Un comerciante que suba silenciosamente su precio choca con el límite en lugar de con su saldo, y usted lo nota por un cargo fallido en lugar de una línea faltante en el estado de cuenta.

*Nuestro módulo **[Seguridad Financiera Personal](/personal-security-course/personal-finance/)** coloca esto junto con las congelaciones de crédito y la tokenización de tarjetas como los tres controles que limitan lo que un solo comerciante comprometido puede alcanzar.*

## Planes y lo que Cada Uno Desbloquea

Privacy.com ofrece un nivel gratuito junto con tres planes de pago. Los precios y los límites de funciones cambian, así que confirme los términos actuales antes de suscribirse.

| Plan | Precio | Añadidos Notables |
|---|---|---|
| **Personal (gratis)** | $0 | Tarjetas virtuales, bloqueo por comerciante, límites de gasto, sin comisión en transacciones nacionales |
| **Plus** | $5/mes | Tarjetas por categoría, notas en tarjetas para organizar gastos |
| **Pro** | $10/mes | Reembolso en compras calificadas, tarjetas físicas Everywhere |
| **Premium** | $25/mes | Todo lo de Pro, con límite mensual de creación de tarjetas aumentado a 60 |

**El nivel gratuito cubre el beneficio principal de seguridad.** El bloqueo por comerciante, las tarjetas de un solo uso y los límites de gasto son los mecanismos que reducen la exposición, y están disponibles sin costo. Los niveles de pago añaden organización y conveniencia más que protección adicional.

**Las comisiones por transacciones en el extranjero varían según el nivel.** El nivel gratuito cobra 3% en transacciones extranjeras con un mínimo de $0.50, mientras que los niveles de pago no cobran.

## Lo que Privacy.com No Hace

**Ser claro sobre los límites es más útil que una lista de funciones.**

| Limitación | Detalle |
|---|---|
| **No te hace anónimo** | Tu identidad se verifica al registrarte y el emisor la mantiene |
| **No oculta la transacción a tu banco** | Tu banco ve la transferencia de fondos y la red ve el cargo |
| **No construye historial crediticio** | No son cuentas de crédito y no se realiza consulta crediticia |
| **Es solo para EE.UU.** | Requiere ciudadanía o residencia legal en EE.UU. y cuenta bancaria o de crédito en EE.UU. |
| **Requiere verificación de identidad** | Los controles KYC son obligatorios bajo reglas contra el lavado de dinero |
| **No cubre todos los comerciantes** | Algunos comerciantes bloquean rangos de tarjetas prepago y virtuales |

**El punto del bloqueo por comerciante importa en la práctica.** Algunos servicios de suscripción y aerolíneas rechazan rangos de tarjetas que asocian con tarjetas virtuales o prepago, y ninguna configuración soluciona el problema. Mantenga una tarjeta real disponible como respaldo para esos casos.

*El resumen honesto: una tarjeta virtual es un control de contención para la exposición al comerciante, no una herramienta de anonimato. Si necesita anonimato, es un problema diferente con herramientas diferentes.*

## Quién Emite la Tarjeta y Por Qué Importa

**Una tarjeta virtual sigue siendo una tarjeta real, emitida por un banco real, bajo una licencia de esquema real.**

| Detalle | Valor |
|---|---|
| **Banco emisor** | Patriot Bank, N.A., Miembro FDIC |
| **Licencias de esquema** | Mastercard y Visa |
| **Dónde se acepta** | En cualquier lugar donde se acepten Mastercard y Visa |
| **Financiamiento** | Transferido desde tu cuenta corriente vinculada en EE.UU. |

**Por eso la protección es genuina.** La tarjeta tiene las mismas protecciones del esquema que cualquier otro producto Mastercard o Visa, lo que significa que aplican los derechos de contracargo y los procesos de disputa por fraude normalmente. No es una tarjeta de regalo ni un crédito cerrado de tienda.

Dos certificaciones merecen ser nombradas porque son verificables de forma independiente y no solo afirmaciones de marketing:

- **Cumplimiento PCI-DSS**, que es el estándar de la industria de tarjetas de pago para manejar datos del titular de la tarjeta
- **SOC 2 Tipo II**, que es un informe auditado que cubre controles de seguridad durante un período de tiempo en lugar de una afirmación puntual

**Sobre el modelo de negocio:** la empresa declara que gana el intercambio de los comerciantes y no vende datos de clientes a anunciantes o terceros. Este es el mismo modelo de ingresos que cualquier otro emisor de tarjetas, lo cual es importante entender en lugar de considerarlo inusual.

*La razón práctica para verificar el banco emisor es la confirmación. Cualquiera puede decir que opera un programa de tarjetas, y el nombre del emisor en la tarjeta es lo que confirmas con el banco nombrado en la documentación.*

Inspeccione el esquema y banco desde el prefijo PAN usando el **[Decodificador de Banda Magnética](/magnetic-stripe-decoder/)**, que reporta el rango principal del esquema y valida el dígito de control Luhn.

## Cómo Usar Bien las Tarjetas Virtuales

**Los controles solo ayudan si los configuras.** Seis hábitos aportan la mayor parte del beneficio.

1. **Bloquee cada tarjeta a un comerciante** a menos que haya una razón para no hacerlo. El bloqueo es lo que hace inútil un número filtrado.
2. **Use tarjetas de un solo uso para todo lo desconocido**, incluyendo pruebas y compras puntuales en sitios pequeños.
3. **Establezca ambos límites de gasto** en tarjetas de suscripción, para que un aumento de precio falle en lugar de cobrar.
4. **Nombre cada tarjeta con el nombre del comerciante**, para que la lista de transacciones sea legible y un cargo inesperado destaque.
5. **Pausa en lugar de cerrar** cuando planee reanudar un servicio, y cierre cuando no lo hará.
6. **Mantenga una tarjeta real para comerciantes que rechazan rangos virtuales**, para que un bloqueo en el pago no se convierta en emergencia.

> **Error común: tratar una tarjeta virtual como sustituto de revisar tus estados.** El bloqueo por comerciante detiene una clase de daño. No detecta una cuenta comprometida en tu banco, una transferencia no autorizada o un cargo fraudulento en la tarjeta real detrás de ella.

## Puntos Clave

- **Una tarjeta virtual cambia el número que almacena el comerciante.** Tu PAN real nunca les llega, que es el mecanismo completo.
- **No hace la transacción privada.** Tu banco, la red y el emisor aún la ven, y la verificación de identidad es obligatoria.
- **El bloqueo por comerciante es la función de mayor valor**, porque un número filtrado falla en todas partes.
- **El nivel gratuito incluye los controles de seguridad.** Los planes pagos añaden organización y conveniencia más que protección.
- **La banda magnética almacena datos de la tarjeta en texto plano** y será eliminada para 2033, con bancos de EE.UU. deteniendo la emisión en 2027.
- **El CVV no está en la banda**, por eso un skimmer que copia las pistas carece de lo que muchos comerciantes en línea requieren.
- **Algunos comerciantes rechazan rangos de tarjetas virtuales.** Mantenga una tarjeta real como respaldo.
- **Verifique el banco emisor** en lugar de confiar en una afirmación del programa de tarjetas, y revise el prefijo PAN usted mismo.

## Próximos Pasos

1. **Inspecciona los datos de la pista de tu propia tarjeta** y observa exactamente qué contiene la banda magnética: **[Decodificador y codificador de banda magnética](/magnetic-stripe-decoder/)**
2. **Congela tu crédito** si aún no lo has hecho, que es el control más fuerte contra el fraude de nuevas cuentas: **[Seguridad financiera personal](/personal-security-course/personal-finance/)**
3. **Aplica la disciplina de priorización** para decidir cuánto esfuerzo merece esta situación para ti: **[Lista de verificación de seguridad personal priorizada](/articles/personal-security-checklist-prioritized-2026/)**
4. **Revisa los planes y términos actuales de Privacy.com** antes de suscribirte: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Verifica si tus datos ya aparecen en una filtración** antes de asumir que no te afecta: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Lee la lista de verificación de seguridad de pagos** para la contraparte organizacional: **[Lista de verificación de respuesta a incidentes](/checklists/incident-response-checklist/)**

## Referencias

1. [Privacy.com - qué son las tarjetas virtuales, bloqueo de comerciantes y límites de gasto](https://www.privacy.com/virtual-card)
2. [Tarjeta digital - Wikipedia, cubriendo tarjetas digitales versus virtuales, pistas de banda magnética, códigos de servicio, paridad y LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - tarjetas de identificación, tarjetas de transacciones financieras, estructura de datos de las pistas 1 y 2](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - diseño detallado del campo de pista, incluyendo centinelas y códigos de servicio](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [Consejo de Normas de Seguridad PCI - requisitos del entorno de datos del titular de la tarjeta](https://www.pcisecuritystandards.org/)
6. [Oficina de Protección Financiera del Consumidor - informes y puntajes de crédito](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [Codificación de datos ANSI/ISO ALPHA, el conjunto de caracteres de la Pista 1 y tabla de paridad](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [Caracteres ISO para tarjetas magnéticas, conjuntos de la Pista 1 y Pista 2 lado a lado](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Lectura de datos de tarjetas magnéticas, un recorrido práctico con un escaneo en vivo de tarjeta](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)
