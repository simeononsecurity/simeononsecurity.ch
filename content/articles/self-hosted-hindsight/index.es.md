---
title: "Hindsight autohospedado: memoria local para agentes y enrutamiento privado de modelos"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Caso de estudio de Hindsight autohospedado, rutas locales de Qwen observadas y trabajo de GPU por solicitud sin una suscripción a modelos alojados en las rutas inspeccionadas."
genre: ["IA local", "IA autohospedada", "Agentes de IA", "Infraestructura de IA", "Privacidad"]
tags: ["Hindsight", "Hindsight autohospedado", "memoria de agentes", "IA local", "LLM local", "Qwen3.5", "LiteLLM", "VPN privada", "gateway de modelos", "embeddings", "reevaluación", "planificación de GPU", "inferencia privada", "Docker", "bancos de memoria", "páginas de conocimiento", "enrutamiento de modelos locales"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Un servicio privado de memoria dirige tareas a servidores locales de modelos en CPU y GPU"
coverCaption: "La memoria, la recuperación y las rutas de modelos inspeccionadas se ejecutan en equipos propios"
---

**Nuestro servicio de memoria Hindsight se ejecuta en hardware que controlamos.** El motor de memoria, la base de datos, el modelo de embeddings y el reranker funcionan en un único despliegue autohospedado. Hindsight envía solicitudes de generación a un gateway privado. El backend compartido de Qwen que inspeccionamos y la ruta probada de actualización de páginas usan servidores locales de modelos, sin una suscripción a inferencia alojada.

Esto describe un despliegue operativo. **Autohospedado no significa desconectado.** La VPN usa un servicio externo de coordinación, y las imágenes de software y los pesos de los modelos requieren descargas. La afirmación se limita al procesamiento de memoria y a la inferencia del modelo, no a todas las conexiones de red de nuestros dispositivos ni de otras herramientas de agentes.

<!--more-->

## Puntos clave

- **Hindsight administra el flujo de memoria.** Un contenedor Docker sirve la API, los trabajadores y el plano de control. Un volumen persistente guarda los datos de los bancos.
- **Los modelos pequeños de recuperación permanecen locales.** Los embeddings y el reranking se ejecutan dentro del proceso Hindsight en la CPU.
- **Qwen genera texto.** Retain, Reflect y Consolidation solicitan el alias privado Qwen3.5-4B con el razonamiento desactivado y una salida acotada. El backend inspeccionado sirve el modelo localmente.
- **La actualización lenta de páginas recibe una GPU.** Un alias de modelo separado toma prestada una tarjeta para una solicitud en segundo plano y la libera al terminar.
- **El gateway oculta la ubicación física.** Hindsight elige un alias de modelo. Los servicios de enrutamiento privados seleccionan el endpoint de servicio.

## Define los límites antes de elegir modelos

**Hindsight es el motor de memoria, no el servidor de modelos.** La imagen Docker completa incluye modelos locales de embeddings y reranking, pero la generación de lenguaje necesita un endpoint. La [guía de instalación de Hindsight](https://hindsight.vectorize.io/developer/installation) explica esta separación y muestra servidores locales de llama.cpp, Ollama y vLLM como alternativas a proveedores alojados.

**La API de memoria permanece en la red privada.** El plano de control web se ejecuta en una interfaz local. Un volumen persistente conserva la base de datos integrada, así que recrear el contenedor no elimina los bancos. La autenticación protege la API y los bancos separados organizan el contexto de cada proyecto.

**El gateway de generación proporciona nombres de modelos estables.** Hindsight envía solicitudes compatibles con OpenAI a través del gateway privado y la VPN. El gateway las reenvía a endpoints locales. La ruta Qwen inspeccionada llega a un despliegue LiteLLM asociado a un servidor local de CPU. La [documentación del router LiteLLM](https://docs.litellm.ai/docs/routing) describe este patrón de alias. Otro router compatible con OpenAI puede cumplir la misma función.

{{< figure src="hindsight-private-request-path.webp" alt="Diagrama con agentes, un servicio Hindsight privado, modelos locales de recuperación, un gateway privado y servidores Qwen locales" caption="El diagrama omite nombres de host, direcciones, claves de acceso y etiquetas de los equipos físicos" >}}

[Abre el diagrama completo de la ruta de solicitud](hindsight-private-request-path.webp).

**También existe una API interna.** Hindsight llama a un gateway privado con el formato compatible con OpenAI. Las rutas inspeccionadas sirven la inferencia localmente. No auditamos todas las reglas de reserva del gateway, así que revisa su política antes de tratar el procesamiento local como garantía para cada solicitud.

## Asigna cada trabajo de memoria al cómputo adecuado

Las operaciones de Hindsight hacen trabajos distintos. **Retain** extrae hechos de material nuevo. **Recall** encuentra recuerdos relevantes. **Reflect** busca y redacta una respuesta sintetizada. **Consolidation** combina hechos relacionados. La **actualización de páginas de conocimiento** reconstruye un resumen vivo desde el banco.

| Operación | Ubicación del modelo | Motivo |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B a través del gateway privado | Extracción estructurada local con un presupuesto de salida limitado |
| **Recall** | Embeddings y reranking locales en CPU | La búsqueda no necesita una llamada a la API de generación |
| **Reflect** | Qwen3.5-4B a través del gateway privado | La síntesis necesita generación después de recuperar memoria |
| **Consolidation** | Qwen3.5-4B a través del gateway privado | Los lotes pequeños limitan respuestas estructuradas largas |
| **Actualización de páginas de conocimiento** | Ruta Qwen local dedicada en GPU | La síntesis grande en segundo plano superó el límite de tiempo de la ruta CPU |

*Deja las tareas pequeñas de recuperación en CPU y reserva la inferencia GPU para el trabajo largo que hayas medido.*

El contenedor Hindsight carga **BAAI/bge-small-en-v1.5** para embeddings y **hindsight-ai/hs-rerank-1** para reranking. Los registros de inicio confirman que ambos se ejecutan localmente en CPU. La [referencia de modelos de Hindsight](https://hindsight.vectorize.io/developer/models) documenta opciones locales y la ruta opcional del modelo de decisión.

Conservamos el modelo de embeddings existente porque cambiar el espacio de embeddings exige reconstruir los vectores guardados. El reranker ya se ejecuta localmente, así que un servicio de reranking alojado crearía un nuevo límite de datos sin resolver el tiempo de espera de generación observado. Una prueba local de **hs-decide-1-flash** produjo una respuesta Reflect correcta, pero terminó cerca del límite de tiempo de prueba. Los datos sintéticos de Consolidation no ejercitaron la ruta de decisión. Por eso el modelo de decisión no forma parte del enrutamiento de producción.

## Asigna una GPU al trabajo lento en segundo plano

**El nombre del modelo normal y el nombre del modelo de actualización son distintos.** Retain, Reflect y Consolidation usan el alias compartido de Qwen. La actualización de páginas en segundo plano usa un alias GPU específico del nodo con una sola llamada de modelo de lenguaje concurrente. Esto limita un trabajo largo de mantenimiento a una GPU por vez.

**Una reserva por solicitud limita el uso de GPU.** El grupo de GPU inicia un trabajador de modelo cuando llega una solicitud. El controlador reserva una tarjeta, atiende la solicitud, detiene el trabajador y libera la reserva. El diagrama omite el inventario físico de hosts.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagrama de una GPU reservada para actualizar una página en segundo plano y liberada cuando termina la solicitud" caption="Una reserva por solicitud asigna una GPU a la actualización de una página" >}}

[Abre el diagrama completo del ciclo de reserva de GPU](hindsight-gpu-lease-cycle.webp).

Esta separación surgió de un fallo que medimos. **Una actualización de página que priorizaba CPU alcanzó un límite de una hora.** Tras dirigir las actualizaciones en segundo plano al grupo local de GPU, cinco páginas que antes habían fallado se completaron en unos dos a seis minutos durante una recuperación. Estas cifras describen esas páginas y configuraciones. No son un benchmark general de rendimiento de Qwen.

## Corrige los valores predeterminados y los tiempos de espera

**Los límites de salida anteriores de Hindsight no encajaban con nuestro router local.** El router acepta hasta 8.192 tokens de salida y aplica 256 si la solicitud no especifica un límite. Un límite anterior de Retain de 64.000 tokens provocó HTTP 400. Los lotes de ocho hechos de Consolidation se detuvieron por longitud de salida, y Reflect necesitaba un límite explícito para evitar el fallback de 256 tokens del router.

**Hicimos explícitos los límites de cada trabajo.** El razonamiento de Qwen está desactivado para estas operaciones de memoria. Hindsight permite ahora cuatro llamadas LLM concurrentes en total, con un máximo de una llamada para la actualización de páginas en segundo plano. El tiempo de espera global de LLM es de 1.800 segundos con un reintento del modelo.

| Carga | Límite de salida o lote | Límites de llamada y operación |
| --- | --- | --- |
| **Retain** | 8.192 tokens de salida | Tiempo de espera general de llamada: 1.800 segundos |
| **Reflect** | 4.096 tokens de salida | 900 segundos por llamada, 3.600 segundos por operación |
| **Consolidation** | 4.096 tokens, cuatro hechos por llamada | 900 segundos por llamada, 14.400 segundos por operación |
| **Actualización de página** | Una llamada de modelo concurrente | 900 segundos por llamada, ruta GPU dedicada |

*Estos valores describen nuestro despliegue de noviembre de 2026 y su router local.*

**El tiempo de espera de una llamada y el límite total de una operación controlan etapas distintas.** Algunas llamadas válidas de Qwen superaron el antiguo tiempo de 300 segundos por llamada. Los límites más largos de operación permiten tareas de varias llamadas, mientras que los 900 segundos por llamada siguen limitando cada intento.

Durante la recuperación, varias tareas Retain terminaron con **1.042 a 2.076 tokens de salida**. Dos ejecuciones de Consolidation completaron **41 de 41** y **30 de 30** elementos. Más tarde, el vencimiento del límite de una actualización de página llevó a la ruta GPU separada descrita arriba. Estos resultados no demuestran fiabilidad a largo plazo.

## Qué sacrifica este diseño

**No pagar una factura de modelo alojado no significa que el costo sea cero.** El despliegue usa hardware propio, electricidad, almacenamiento, tiempo de mantenimiento y tiempo de GPU durante las actualizaciones de páginas. Cada decisión de ubicación intercambia capacidad por latencia o simplicidad operativa.

| Opción | Beneficio | Compromiso |
| --- | --- | --- |
| **Generación primero en CPU** | Mantiene disponible la GPU | Una actualización probada alcanzó el límite de una hora |
| **Actualización de páginas en GPU** | Cinco páginas terminaron en unos dos a seis minutos en una ejecución | Usa capacidad GPU y depende de la ruta dedicada |
| **Base de datos integrada** | Mantiene compacto el despliegue | Reduce el dominio de fallos y exige probar las copias de seguridad |

*Usa una ruta GPU de actualización cuando la latencia CPU medida supere tu ventana de mantenimiento.*

La [guía de instalación de Hindsight](https://hindsight.vectorize.io/developer/installation) recomienda PostgreSQL separado para despliegues de producción más grandes. **Nuestra base integrada necesita una ruta de copia de seguridad y recuperación probada** a medida que crece el banco.

**La inferencia privada es una propiedad de la ruta.** Revisa el proveedor Hindsight seleccionado, la asignación de modelos del gateway, las reglas de reserva, el proceso local del modelo, la retención de registros y el tráfico de salida. Los identificadores de seguimiento de Hindsight ayudan a correlacionar solicitudes, y Docker rota los registros del contenedor. Ninguna de las dos medidas demuestra que una solicitud posterior permaneció local. Una auditoría del gateway aporta la evidencia integral que falta.

## Recomendación

**Empieza con modelos locales de recuperación y límites explícitos de generación.** Coloca Hindsight, los modelos de embeddings y el reranker en equipos propios. Dirige la generación por un gateway privado compatible con OpenAI a través de una VPN. Mide cada operación antes de asignar CPU o GPU y reserva la ruta GPU para trabajos en segundo plano cuya latencia CPU supere tu ventana de mantenimiento.

*Revisa cada regla de reserva del gateway y prueba la recuperación del banco antes de tratar el despliegue como privado y resiliente.* La [guía de límites de privacidad de IA local](/articles/local-ai-privacy-boundary/) ofrece una lista inicial.

## Conclusión

**Este despliegue mantiene la memoria Hindsight y las rutas de inferencia inspeccionadas en equipos propios, sin una suscripción a modelos alojados.** La recuperación en CPU, las llamadas Qwen limitadas y la ruta GPU de actualización con una llamada atienden cargas distintas. Las recuperaciones completaron Retain, Consolidation y la actualización de páginas con estos ajustes. Las siguientes comprobaciones son auditar todos los fallbacks del gateway, probar las copias de seguridad y observar la fiabilidad durante más tiempo.
