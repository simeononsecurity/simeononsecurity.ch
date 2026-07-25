---
title: "ATS Resume Improver: optimizador de currículum de IA gratuito, autoalojable y sin envío de datos"
date: 2026-07-22
toc: true
draft: false
description: "ATS Resume Improver es un optimizador de currículum de código abierto y del lado del cliente que admite OpenAI, Anthropic Claude y modelos Ollama locales. Analice, puntúe, compare palabras clave, optimice y exporte su currículum sin que sus datos salgan del navegador."
genre: ["Herramientas de carrera", "Proyectos de código abierto", "Inteligencia artificial", "Tecnología de privacidad", "Herramientas para desarrolladores", "Búsqueda de empleo", "Productividad"]
tags: ["ATS Resume Improver", "optimización ATS", "escáner de currículum", "currículum con IA", "currículum OpenAI", "currículum Claude", "Ollama IA local", "autoalojado", "privacidad primero", "herramientas de búsqueda de empleo", "análisis de brechas de palabras clave", "carta de presentación", "puntuación de currículum", "React", "TypeScript", "Docker", "Vite", "código abierto", "exportar PDF", "exportar DOCX", "analizador de currículum", "herramientas de carrera", "preparación para entrevistas", "estimador de salario", "detección de tipo de currículum", "puntuación ATS", "herramienta de currículum gratuita", "GitHub", "sin recopilación de datos"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Un portátil moderno en un escritorio que muestra una interfaz colorida de optimización de currículum con gráficas, sobre un fondo azul marino profundo."
coverCaption: "ATS Resume Improver — análisis de currículum 100% del lado del cliente y optimización con IA sin recopilación de datos."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Gratuito, de código abierto y autoalojable. Su currículum nunca toca un servidor a menos que use un proveedor de IA. Y aun así, va directamente al proveedor de IA, no a nosotros.**

## ¿Qué es ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** es un optimizador de currículum de código abierto basado en navegador que analiza su currículum frente a una descripción de trabajo y le ayuda a cerrar la brecha entre lo que tiene y lo que los sistemas de seguimiento de candidatos realmente puntúan. Construido con React 19, Vite y TypeScript, todo el **pipeline de análisis y puntuación se ejecuta dentro de su navegador** sin servidor backend.

El código fuente está en **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**. Puede usar la versión alojada, desplegar la suya propia en Vercel/Netlify/Cloudflare/GitHub Pages con un clic, o iniciarlo localmente con Docker.

### El problema de privacidad que resuelve

La mayoría de los servicios de optimización de currículum cargan su currículum en sus servidores, ejecutan puntuaciones propietarias y retienen sus datos. ATS Resume Improver adopta el enfoque opuesto.

| Modo | Qué sale de su dispositivo |
|------|------------------------|
| **Sin clave de IA** | Nada — 100% local, se ejecuta en su navegador |
| **OpenAI / Anthropic** | El texto del currículum y la descripción del trabajo van directamente a la API del proveedor de IA con su clave, sin servidor intermediario |
| **Ollama (local)** | Nada — el modelo se ejecuta en su propia máquina |

**Las claves API se almacenan solo en memoria** y desaparecen cuando cierra la pestaña. Sin análisis, sin seguimiento, sin cookies.

______

## Funciones principales

### Lo que funciona sin clave de IA

No necesita una clave API para obtener valor real. El modo sin clave incluye:

- **Carga de currículum** — PDF, DOCX, TXT o Markdown
- **Extracción de texto ATS** — muestra exactamente lo que un ATS analiza de su archivo, incluyendo lo que se pierde en el formato
- **Detección del tipo de currículum** — identifica automáticamente cuál de los 7 perfiles coincide con su currículum y adapta el orden de las secciones
- **Detección de secciones y advertencias de formato** — señala secciones faltantes y formatos hostiles para los analizadores
- **Puntuación ATS (0–100)** con un desglose en 5 dimensiones
- **Análisis de brechas de palabras clave** — concordancia de cadenas basada en reglas frente a la descripción del trabajo
- **Optimización ATS determinista** — reestructuración local basada en reglas
- **Visor de diferencias antes/después** — vea exactamente qué cambió
- **Exportación profesional a PDF, DOCX, TXT y Markdown**

### Lo que desbloquea la IA

Conecte OpenAI, Anthropic Claude o Ollama local y la herramienta se actualiza a:

- **Análisis semántico de palabras clave** — entiende el contexto, no solo las coincidencias de cadenas. Muestra la fuerza de coincidencia (Fuerte/Moderado/Parcial), la ubicación de la coincidencia ("encontrado en Habilidades y 3 trabajos"), la importancia por palabra clave (Crítico/Alto/Medio/Bajo) y un resumen narrativo de IA de 2-3 oraciones
- **Optimización de currículum con IA** — reescritura completa con prompts de mejores prácticas ATS
- **Exportaciones mejoradas por IA** — PDF/DOCX formateados por la IA antes de la descarga
- **Generación de carta de presentación** — con reglas de humanización que eliminan las señales reveladoras de la IA
- **Predictor de preguntas de entrevista** — basado en la descripción del trabajo
- **Estimador de rango salarial**

______

## Detección del tipo de currículum

La aplicación clasifica automáticamente su currículum en uno de 7 perfiles y ajusta el orden de las secciones para que coincida con las expectativas de los reclutadores y los ATS para esa etapa de carrera:

| Perfil | Ideal para | Prioridad de secciones |
|---------|----------|-----------------|
| 🏢 **Profesional experimentado** | 5+ años, carrera lineal | Experiencia → Habilidades → Educación |
| 🌱 **Nivel intermedio** | 2–5 años | Experiencia → Habilidades → Educación |
| 🎓 **Nivel inicial** | 0–2 años | Habilidades → Educación → Proyectos → Experiencia |
| 🎒 **Estudiante / Recién graduado** | Aún matriculado | Educación → Proyectos → Habilidades → Experiencia |
| 🔬 **Académico / Investigador** | Doctorado, publicaciones | Educación → Investigación → Publicaciones → Experiencia |
| 📜 **Con peso en certificaciones** | Las certificaciones superan al título | Certificaciones → Habilidades → Experiencia → Educación |
| 🔄 **Cambio de carrera** | Brecha o pivot detectado | Resumen → Habilidades transferibles → Educación → Experiencia |

*El orden de las secciones se aplica de manera uniforme en la optimización, exportaciones PDF, DOCX, TXT y Markdown, no solo en pantalla.*

______

## Análisis semántico de palabras clave con IA

Aquí es donde la herramienta se separa de los simples contadores de palabras clave. Cuando se configura un proveedor de IA, el análisis de brechas de palabras clave pasa de la simple concordancia de cadenas al razonamiento semántico:

| Dimensión | Sin IA | Con IA |
|-----------|-----------|---------|
| **Método de coincidencia** | Solo cadena exacta | Comprensión semántica del contexto |
| **Fuerza de coincidencia** | — | Calificaciones Fuerte / Moderado / Parcial |
| **Contexto de coincidencia** | — | "encontrado en Habilidades y 3 trabajos" |
| **Importancia de brechas** | Todas las brechas tratadas igual | Crítico / Alto / Medio / Bajo |
| **Sugerencias** | Consejos genéricos | Sugerencias accionables por palabra clave |
| **Cobertura %** | Basada en recuento de cadenas | Ponderada semánticamente |
| **Resumen** | — | Narrativo de IA de 2-3 oraciones |

*El análisis local basado en reglas se ejecuta al instante. Los resultados de IA lo enriquecen de forma asíncrona mientras usted revisa.*

______

## Proveedores de IA admitidos

Todas las llamadas de IA incluyen prompts de mejores prácticas ATS derivados de las directrices de Harvard OCS y Columbia CCE.

### OpenAI

| Modelo | Ideal para |
|-------|----------|
| **GPT-4.1 mini** (predeterminado) | El más inteligente, rápido y asequible — recomendado |
| GPT-4o mini | Rápido y asequible clásico |
| GPT-4.1 | Último GPT-4.1 — seguimiento de instrucciones preciso |
| GPT-4o | Alta calidad, insignia |
| GPT-4 Turbo | Gran ventana de contexto |
| GPT-3.5 Turbo | El más rápido y barato |

**Costo estimado**: ~$0,002–0,05 por análisis de currículum.

### Anthropic Claude

| Modelo | Ideal para |
|-------|----------|
| **Claude Sonnet 4.5** (predeterminado) | Rápido e inteligente — recomendado |
| Claude Opus 4.5 | El más capaz — mejor para tareas complejas |
| Claude Haiku 4.5 | El más rápido y barato |
| Claude 3.5 Sonnet | Confiable y bien probado |
| Claude 3.5 Haiku | Rápido y asequible v3.5 |

### Ollama (local / autoalojado)

No se requiere clave API. Ejecute el modelo en su propio hardware. Configure `OLLAMA_ORIGINS=*` para permitir el acceso del navegador.

| Modelo | Notas |
|-------|-------|
| **Llama 3.3** (predeterminado) | Último Meta Llama — recomendado |
| Llama 3.2 | Meta Llama 3.2 |
| Mistral 7B | Rápido y capaz |
| Mixtral 8x7B | Mezcla de expertos |
| Qwen 2.5 | Alibaba Qwen 2.5 |
| DeepSeek R1 | Modelo de razonamiento sólido |
| Phi-4 | Microsoft Phi-4 |
| Gemma 3 | Google Gemma 3 |

Ejecutar Ollama localmente pone la herramienta completamente fuera de línea. Nada sale de su máquina.

______

## Humanización de la carta de presentación

El generador de cartas de presentación aplica una guía de estilo deliberada para eliminar las señales reveladoras del texto generado por IA :

- **Sin guiones largos** — la señal reveladora de IA más fuerte, eliminada por completo
- **Más de 50 palabras y frases prohibidas**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, etc.
- **Sin markdown en el cuerpo de la carta** — sin asteriscos en negrita, hashtags ni puntos y coma
- **Voz activa por defecto** — pasiva solo cuando el actor genuinamente no importa
- **Contracciones requeridas**: "I've", "I'm", "it's"
- **Longitud de oraciones variada** — oraciones cortas y directas mezcladas con más largas
- **Sin introducciones de relleno** — "Es importante señalar que X" → simplemente diga X
- **Detalle concreto de la oferta de trabajo en el párrafo 1** — demuestra que la carta no es una plantilla

*El resultado se lee como si lo hubiera escrito un humano, porque las reglas obligan al modelo a escribir como uno.*

______

## Opciones de autoalojamiento

### Versión alojada (sin configuración)

Use la aplicación en vivo en **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)** — sin cuenta, sin registro, sin tarjeta de crédito.

### Despliegue en la nube con un clic

| Plataforma | Enlace |
|----------|------|
| **Vercel** | Despliegue con un clic desde el repositorio |
| **Cloudflare Pages** | Despliegue con un clic |
| **Netlify** | Despliegue con un clic |
| **GitHub Pages** | Bifurcar → Configuración → Pages → GitHub Actions → despliegue automático |

### Desarrollo local

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (recomendado para entornos reproducibles)

```bash
# Desarrollo — recarga en caliente en http://localhost:5173
make docker-dev

# Producción — nginx en http://localhost:8080
make docker-prod

# Dev + Ollama juntos (pila de IA local completa)
make docker-dev-with-ollama
```

### Pila Ollama completamente fuera de línea

```bash
# Iniciar el contenedor Ollama (modelos persistentes entre reinicios)
make ollama

# Descargar un modelo
make ollama-pull MODEL=llama3.2

# Iniciar la aplicación dev + Ollama lado a lado
make docker-dev-with-ollama
```

Luego abra la aplicación, vaya al panel de claves API, seleccione **Ollama (Local)**, configure la URL a `http://localhost:11434` y elija un modelo. Ningún dato sale de su máquina.

______

## Preguntas frecuentes

### ¿La herramienta almacena mi currículum?

No. La aplicación es completamente del lado del cliente. Nada se guarda en ningún servidor. Los datos de sesión viven en la memoria del navegador y desaparecen cuando cierra la pestaña.

### Mi currículum obtuvo una puntuación baja. ¿Debo preocuparme?

Las puntuaciones ATS son indicativas, no de aprobado/reprobado. Una puntuación de 60 no significa que un ATS lo rechace. Significa que hay brechas medibles entre su currículum y la descripción de trabajo analizada.

### ¿Puedo usarlo con múltiples descripciones de trabajo?

Sí. Pegue una nueva descripción de trabajo en cualquier momento. El análisis de palabras clave y la optimización se volverán a ejecutar contra la nueva oferta. Cada análisis es independiente.

### ¿La integración con Ollama es realmente fuera de línea?

Sí, si Ollama se ejecuta en su máquina local o en una máquina de su red local. La aplicación envía texto a su instancia de Ollama a través de HTTP. Nada va a ningún servicio externo.

______

## Hoja de ruta del proyecto

Funciones en desarrollo o planificadas:

- Historial de versiones del currículum mediante IndexedDB
- Optimizador de perfil de LinkedIn
- Soporte para el proveedor Google Gemini
- Modelos adicionales de Ollama

El proyecto tiene licencia MIT y acepta solicitudes de extracción. Abra un problema primero para cambios importantes.

______

## Conclusión

**ATS Resume Improver** llena una brecha real: una herramienta que realiza un análisis serio de currículum sin ceder sus datos a nadie. El modo sin clave le da retroalimentación inmediata y accionable sobre el formato y la cobertura de palabras clave. Agregar una clave de IA actualiza el análisis a razonamiento semántico, redacción de cartas de presentación y preparación para entrevistas, todo por centavos por análisis o completamente gratis con Ollama.

La versión alojada en vivo está en **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**. El código fuente completo está en **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**.

______

## Referencias

1. [ATS Resume Improver — herramienta en vivo](https://atsresumeimprover.netlify.app/)
2. [ATS Resume Improver — repositorio GitHub](https://github.com/simeononsecurity/ats-resume-improver)
3. [Consejos y trucos para el currículum — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — Mejor prompt de IA para humanizar la escritura IA](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [Documentación de la API de OpenAI](https://platform.openai.com/docs/)
6. [Documentación de la API de Anthropic Claude](https://docs.anthropic.com/)
7. [Ollama — servidor LLM local](https://ollama.com/)
