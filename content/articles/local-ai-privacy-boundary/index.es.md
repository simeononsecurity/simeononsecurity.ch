---
title: "Privacidad de la IA local: qué permanece en su ordenador y qué no"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Trace prompts, archivos de modelos, herramientas, registros, exposición de red y costes de energía antes de elegir inferencia local o un servicio de IA alojado."
genre: ["IA local", "Privacidad", "IA autoalojada", "Ciberseguridad", "Economía de la IA"]
tags: ["local AI privacy", "local inference", "cloud AI", "AI data privacy", "self-hosted AI", "LLM privacy", "GPU ownership cost", "AI electricity cost", "RTX 5070", "Claude Haiku 5.5", "Ollama privacy", "llama.cpp", "AI security", "offline AI", "local language models", "prompt privacy", "AI threat model", "GPU break-even", "AI data boundary", "private AI"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Una estación de trabajo de IA local conectada a un servicio en la nube mediante rutas de datos visibles"
coverCaption: "Ilustración de las rutas de datos de IA local y alojada"
---

**La IA local le ofrece un límite de datos más pequeño.** Un prompt procesado por un runtime local permanece en su dispositivo cuando el modelo, las herramientas, los registros y la ruta de red son locales. Una GPU local no convierte un ordenador en un sistema sellado.

Los runtimes de modelos, plugins de herramientas, extensiones del navegador, acceso remoto, API expuestas y descargas de modelos determinan el riesgo. El coste también importa. La electricidad puede costar menos que un precio de tokens alojado, mientras que el hardware retrasa mucho el punto de equilibrio completo.

Esta guía traza primero el límite de privacidad. Después comprueba el coste con precios actuales de proveedores, una hipótesis explícita de potencia y las cifras del vídeo proporcionado.

<!--more-->

Esta comparación de costes local y alojado proporciona contexto para las fórmulas siguientes. No copie cifras de rendimiento sin probar el mismo archivo de modelo y runtime en su hardware.

{{< youtube id="DmkuFpoMYmc" enable="true" title="Is local AI worth it? We did the math vs Claude Haiku 5.5" description="A local-versus-hosted AI cost comparison." >}}

El vídeo informa de un runtime de 2 minutos y 31 segundos. Verifiqué su título y duración mediante la página de visualización. No repetí la prueba de hardware. Sus velocidades siguen siendo medidas informadas por la fuente.

## La respuesta corta

- **Elija inferencia local para una ruta de datos controlada.** Mantenga el servidor del modelo en el dispositivo, enlácelo a loopback y limite el acceso a herramientas.
- **Elija inferencia alojada para trabajos ocasionales.** Evite gastar en hardware cuando la carga sea pequeña o el modelo preferido no quepa en su sistema.
- **Trate el coste local como dos cifras.** Separe la electricidad por hora activa de la propiedad del hardware.
- **Trate la privacidad como una propiedad del sistema.** Un plugin que sube archivos o una API local que escucha en todas las interfaces elimina el beneficio del modelo privado.

La inferencia local ayuda con texto sensible, trabajo sin conexión, versiones fijas de modelos y acceso sin cuota del proveedor. Estos beneficios no demuestran mejores respuestas. Un modelo alojado puede adaptarse mejor, terminar antes o necesitar menos mantenimiento. Mida la carga antes de comprar hardware.

## Trace la ruta de datos

| Componente | Pregunta de privacidad | Evidencia que debe recoger |
|---|---|---|
| **Servidor de modelo local** | ¿El prompt permanece en el host? | Configuración del proceso, dirección de escucha y tráfico saliente |
| **Modelo en la nube** | ¿Qué texto, archivos y resultados salen del host? | Endpoint API, términos del proveedor, registros y ajustes de cuenta |
| **Modo nube en una app local** | ¿El modelo seleccionado se ejecuta en el dispositivo? | Identificador del modelo, proveedor y conexión de red |
| **Plugin de herramienta** | ¿El modelo recibe archivos, salida de shell o contenido del navegador? | Lista de herramientas, permisos y datos capturados |
| **Descarga del modelo** | ¿Qué código y pesos entran en el host? | Repositorio fuente, licencia, checksum y ruta de descarga |
| **Registros locales** | ¿Dónde persisten los prompts y resultados? | Registros del runtime, historial shell, informes de fallos y copias |

**Un modelo local elimina un proveedor de la ruta del prompt.** Aún debe revisar el resto de la ruta.

## Local no significa privado por defecto

[La política de privacidad de Ollama](https://ollama.com/privacy) afirma que Ollama no ve prompts ni datos cuando un modelo funciona localmente. La política separa la operación local de los modelos alojados en la nube. Un modelo en la nube crea un límite de servicio aunque la misma aplicación ejecute ambos modos.

[La documentación del servidor de llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) muestra `127.0.0.1:8080` como valor predeterminado. Sus ejemplos Docker también muestran `--host 0.0.0.0`, que expone el servicio en todas las interfaces. Una dirección de enlace más amplia cambia el límite de acceso.

Compruebe la dirección de escucha antes de enviar texto sensible:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` o `localhost` limitan el acceso al mismo host en el caso normal. Una dirección LAN o `0.0.0.0` exige una regla de firewall y un plan de autenticación. No exponga un endpoint de modelo a la red sin probar ambos.

Compruebe también el nombre del modelo seleccionado. La documentación cloud de Ollama describe sus modelos cloud como una ruta de servicio separada. Una interfaz local no demuestra ejecución local.

Las [preguntas frecuentes de Ollama](https://docs.ollama.com/faq) documentan un modo solo local. Configure `disable_ollama_cloud` en `~/.ollama/server.json`, o configure `OLLAMA_NO_CLOUD=1` antes de reiniciar el servicio. Esto elimina los modelos cloud de Ollama y la búsqueda web del runtime seleccionado. No restringe otras aplicaciones, herramientas del navegador, plugins ni el acceso de red del host.

```json
{
  "disable_ollama_cloud": true
}
```

Verifique el ajuste después de reiniciar. Un runtime solo local estrecha una ruta. No establece un host privado.

## Calcule el coste alojado

Los precios de tokens separan entrada y salida. [Anthropic lista Claude Haiku 5.5 a $0.10 por millón de tokens de entrada y $0.50 por millón de salida para prompts de hasta 100.000 tokens](https://www.anthropic.com/claude/haiku). Los prompts mayores usan las tarifas superiores indicadas.

[La guía de tokens de OpenAI](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) explica por qué el número de palabras no equivale al de tokens. También separa tokens de entrada, salida, entrada en caché y razonamiento. Use los campos de uso del proveedor, no una estimación de palabras.

Para una comparación simple, use un millón de tokens generados y un millón de entrada como cargas separadas. Un agente de programación suele enviar contexto repetido y producir una respuesta menor. Una cifra combinada oculta la mezcla de costes.

## Calcule la potencia local

[El anuncio de lanzamiento de la RTX 5070 de NVIDIA](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) indicó un precio inicial de $549. [La página de la familia RTX 5070](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) lista 12 GB de memoria y 250 W de potencia gráfica total para el diseño de referencia Founders Edition. Durante esta revisión, la página del producto mostraba $549 y la tarjeta sin existencias.

La cifra de potencia de la GPU no es la potencia de todo el sistema. Use un medidor en la pared. El ejemplo supone **400 W de consumo de todo el sistema**, incluida GPU, procesador, memoria, almacenamiento, ventiladores y pérdidas de la fuente. Es una hipótesis para el cálculo, no un resultado medido.

[La previsión de la U.S. Energy Information Administration](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) usó 18,2 centavos por kilovatio-hora como precio residencial medio de la electricidad en 2026. Su tarifa cambia el resultado.

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

Con 400 W y $0.182 por kilovatio-hora, el sistema cuesta $0.0728 por hora activa.

| Velocidad de salida | Tiempo para 1M tokens | Coste de energía para 1M tokens |
|---:|---:|---:|
| **20 tokens por segundo** | 13 horas 53 minutos | **$1.01** |
| **50 tokens por segundo** | 5 horas 33 minutos | **$0.40** |
| **94 tokens por segundo** | 2 horas 57 minutos | **$0.22** |

A 50 tokens de salida por segundo, la energía local cuesta menos que el precio de salida de Haiku 5.5 de $0.50. A 20 tokens cuesta más. El umbral de velocidad es de unos 40 tokens por segundo con estas hipótesis.

El cálculo de entrada usa la misma fórmula. A 2.650 tokens de entrada por segundo, un millón tarda unos 6 minutos y 17 segundos y cuesta unos $0.008 de energía. A 1.000 tokens por segundo, el mismo trabajo cuesta unos $0.020.

La transcripción proporcionada informa de 94 tokens de salida por segundo y 2.650 de entrada para su ejemplo con RTX 5070. La aritmética coincide con esas cifras bajo el supuesto de 400 W. La transcripción no ofrece un registro de laboratorio independiente, hash del modelo, build del runtime, prompt ni lectura del medidor. Trate las velocidades como referencia, no como garantía de compra.

## Punto de equilibrio de los cambios de hardware

El ahorro de energía no paga el hardware por sí solo. Compare la compra completa con la diferencia entre el coste de salida alojado y el coste variable local.

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

A 94 tokens de salida por segundo, el ahorro redondeado sube a unos $0.28 por millón. Recuperar una GPU de $549 exige unos 2.000 millones de tokens de salida. Ambas cifras excluyen memoria del sistema, almacenamiento, placa base, fuente, refrigeración, mantenimiento y reventa.

El precio de lanzamiento no es una cotización universal. La página actual de NVIDIA mostraba el precio oficial sin existencias. Una oferta de $819 de un vendedor exige verificación separada. Use su factura real y la potencia medida en la pared.

**El hardware existente cambia la decisión.** Si su estación ya tiene memoria suficiente y una GPU adecuada, el coste de hardware está hundido para la siguiente tarea. Compare potencia, tiempo, calidad, privacidad y mantenimiento. Si compra un sistema completo, compare el sistema entero con el uso alojado.

Para detalles de compatibilidad del modelo, lea la [guía de modelos de IA local y contexto de GPU](/articles/local-ai-model-gpu-context-guide/) y la [guía de tamaño de 16GB VRAM](/articles/is-16gb-vram-enough-local-llm/). Para una configuración local de agente de programación, lea la [guía de Strata y OpenCode](/articles/strata-opencode-local-coding-agent-16gb/).

## Qué ofrece la privacidad local

- **Una ruta de datos más corta:** el prompt no necesita llegar al proveedor cuando la inferencia es local.
- **Operación sin conexión:** un modelo descargado y un runtime local no necesitan una conexión activa para generar texto.
- **Control de versiones:** usted elige el archivo del modelo y la versión del runtime, en lugar de recibir un cambio automático del proveedor.
- **Control de uso:** la inferencia local evita un contador cloud por petición después de contabilizar hardware y energía.
- **Control de política de red:** el firewall y los controles del host determinan quién llega al endpoint.

Estos beneficios importan para código fuente, registros de clientes, diseños no publicados, notas privadas y entornos desconectados. La inferencia local aún exige cifrado de disco, actualizaciones, separación de cuentas y herramientas limitadas.

## Qué no ofrece la privacidad local

- **No ofrece garantía de calidad:** los modelos pequeños o cuantizados deben probarse con sus criterios reales de aceptación.
- **No ofrece garantía de cadena de suministro:** archivos de modelos, runtimes, plugins e imágenes de contenedor necesitan fuentes confiables y comprobaciones de integridad.
- **No ofrece un host limpio:** malware, extensiones, copias, informes de fallos y administración remota siguen viendo datos del host.
- **No ofrece un endpoint seguro:** un servidor enlazado a todas las interfaces crea un servicio nuevo que debe defender.
- **No ofrece un sistema gratis:** electricidad, almacenamiento, refrigeración, desgaste y mantenimiento tienen coste.

La [guía de agente local de Strata](/articles/strata-opencode-local-coding-agent-16gb/) muestra por qué memoria del sistema, contexto, acceso a herramientas y ajustes del runtime forman parte de la evaluación. La memoria de GPU por sí sola no define el límite de privacidad ni de rendimiento.

## Elija el límite adecuado

| Situación | Primera opción | Motivo |
|---|---|---|
| **Documentos sensibles y PC compatible existente** | Inferencia local | Mantener prompts en un host controlado y evitar hardware nuevo |
| **Redacción genérica ocasional** | API o chat alojado | Pagar la carga pequeña y evitar mantenimiento |
| **Modelo avanzado o herramienta cloud especializada** | Servicio alojado | El modelo o herramienta necesarios no están en el host local |
| **Gran volumen recurrente con modelo local verificado** | Local o híbrido | Comparar potencia, calidad, tiempo de soporte y precio del proveedor |
| **Cargas mixtas** | Enrutamiento híbrido | Mantener tareas sensibles locales y enviar tareas genéricas aprobadas a un modelo alojado |

**El enrutamiento híbrido necesita una regla explícita de clasificación.** Marque los datos como solo locales, aprobados para procesamiento alojado o prohibidos hasta revisión. No confíe en el nombre del modelo ni en el icono de la aplicación para aplicar la regla.

## Verifique antes de confiar

1. **Nombre la ruta del modelo.** Registre identificador, runtime, versión y fuente de descarga.
2. **Compruebe la dirección de enlace.** Confirme que el servidor escucha en loopback salvo que exista una necesidad documentada de una ruta más amplia.
3. **Enumere todas las herramientas.** Revise acceso a archivos, shell, navegador, red y plugins.
4. **Inspeccione la persistencia.** Busque registros de prompts, resultados, fallos, copias y directorios compartidos.
5. **Pruebe la red.** Observe conexiones durante una prueba sensible con un prompt representativo.
6. **Mida el sistema.** Registre potencia, velocidad de salida, velocidad de entrada, longitud de contexto y reintentos.
7. **Pruebe el trabajo aceptado.** Compare tareas completadas y esfuerzo de revisión, no solo tokens por segundo.

La [guía de IA local frente a ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) cubre las diferencias de capacidad. Use esta lista de privacidad junto con la prueba de calidad.

## Referencias

- [Video, Is local AI worth it? We did the math vs Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [NVIDIA Blackwell GeForce RTX 50 Series launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [NVIDIA GeForce RTX 5070 family specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [NVIDIA GeForce RTX 5070 product page](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, October 2026 Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Anthropic Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Ollama privacy policy](https://ollama.com/privacy)
- [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
