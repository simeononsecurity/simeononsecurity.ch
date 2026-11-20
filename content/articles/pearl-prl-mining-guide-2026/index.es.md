---
title: "Minería de Pearl (PRL) en 2026: configuración, rentabilidad y utilidad de la red"
date: 2026-09-22
lastmod: 2026-11-19
toc: true
draft: false
description: "Configura la minería de Pearl PRL con SRBMiner, revisa la prueba de trabajo útil, estima los márgenes y evalúa la utilidad práctica de la red."
genre: ["Criptomonedas", "Minería con GPU", "Computación de IA", "DePIN", "Tecnología de cadena de bloques", "Linux", "Laboratorio doméstico", "Equipo"]
tags: ["minería de Pearl", "minería de PRL", "Pearl PRL", "prueba de trabajo útil", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "pool de minería de Pearl", "LuckyPool Pearl", "minería con GPU 2026", "cripto y computación de IA", "Pearl Research Labs", "minería combinada de Nockchain", "minería combinada de Nock", "minería de RTX 3070", "configurar SRBMiner", "equipo de minería Linux", "servicio de minería systemd", "minería con multiplicación de matrices", "minero vLLM", "billetera Pearl", "dirección prl1", "rentabilidad de la minería", "minería de computación de IA", "guía de minería de criptomonedas", "minería con NVIDIA", "ajustes de overclock para minería"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Ilustración de un equipo moderno de minería con GPU que calcula multiplicaciones de matrices para la blockchain Pearl, con flujos de datos dinámicos y colores intensos sobre un fondo oscuro."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl es la primera cadena de prueba de trabajo útil que alcanza una escala de producción real, y recompensa a los mineros por multiplicar matrices en vez de calcular hashes.** La red principal se lanzó el **27 de abril de 2026** y, en pocas semanas, provocó una fiebre de minería con GPU basada en la promesa de proteger una blockchain mientras produce capacidad de cómputo para IA en el mismo proceso.

*La afirmación es técnicamente real y su viabilidad económica no está demostrada. La diferencia entre ambas cosas es toda la historia.*

Esta guía explica cómo minar PRL, qué calcula el programa de minería, por qué los márgenes se redujeron tan rápido después del lanzamiento y si la red produce algo de valor.

**Al terminar:** tendrás una billetera, un minero verificado, un consumo eléctrico medido y un cálculo de rentabilidad basado en tu tarifa. Trata las estimaciones de los pools y los ingresos iniciales como observaciones de una fecha concreta, no como garantía de compra.

## Respuesta breve

**Pearl es un logro técnico auténtico rodeado por el problema económico que afronta la minería de cada moneda nueva.**

| Pregunta | Respuesta breve |
|---|---|
| **¿Qué es?** | Una blockchain L1 derivada de Bitcoin y protegida mediante prueba de trabajo útil. Los mineros multiplican matrices con ruido en vez de calcular SHA-256 |
| **¿Cómo se mina?** | SRBMiner-MULTI con `--algorithm pearlhash` conectado a un pool, o el minero vLLM de Pearl conectado a tu propio nodo |
| **¿Por qué fue rentable?** | Durante unas semanas, las emisiones iniciales superaron la dificultad. Después, la dificultad las alcanzó |
| **¿Sigue siendo rentable?** | Depende del hardware y la ventana se estrecha. Consulta la sección sobre márgenes |
| **¿La red es útil?** | **El mecanismo sí. El mercado todavía no.** Consulta la conclusión |

**Lo más importante antes de montar un equipo para esto:** las notas de la versión 3.6.8 del propio desarrollador del minero dicen que una próxima actualización de Pearl dejará las GPU de consumo «prácticamente inútiles» para minar. No lo afirma un crítico externo. Lo dice quien desarrolla el minero.

## Qué es Pearl

Pearl es una blockchain L1 desarrollada por **Pearl Research Labs**. Su propio repositorio la describe así:

> "Pearl es una blockchain L1 basada en el protocolo de prueba de trabajo útil, donde la minería se realiza como subproducto de multiplicaciones arbitrarias de matrices."

El repositorio incluye un nodo completo, un servicio de billetera, un cliente ligero SPV, un sistema de pruebas de conocimiento cero y un minero para GPU. Usa la **licencia ISC**, una licencia permisiva. La infraestructura de la cadena deriva de proyectos Bitcoin probados: **btcd** para el nodo, **btcwallet** para la billetera y **neutrino** para el cliente ligero.

**El diseño toma elementos de Bitcoin de forma deliberada**, incluso una oferta máxima de **2.100 millones de PRL**, exactamente cien veces los 21 millones de Bitcoin, con una recompensa por bloque decreciente y bloques de unos dos minutos.

*La infraestructura es conservadora a propósito. La novedad está por completo en la función de trabajo.*

### Qué significa la prueba de trabajo útil

La prueba de trabajo útil es una idea antigua con pocos éxitos. La propuesta siempre ha sido sustituir los cálculos de hash deliberadamente inútiles de Bitcoin por cálculos que también produzcan algo valioso. Casi todos los intentos anteriores fallaron por la misma razón: el trabajo «útil» no era útil o no se podía verificar con suficiente eficiencia como para proteger una cadena.

Pearl implementa esta idea con una rutina llamada **NoisyGEMM**. En la práctica, el minero calcula multiplicaciones de matrices con ruido en una GPU, convierte el resultado en un compromiso mediante un hash y envuelve el trabajo en una **prueba de conocimiento cero** para que la red lo verifique a bajo coste.

El esquema se basa en un artículo de criptografía de 2025, **"Proofs of Useful Work from Arbitrary Matrix Multiplication"**, de Komargodski, Schen y Weinstein. El artículo afirma que el coste adicional es de aproximadamente **1 + o(1) frente a una multiplicación de matrices ingenua**. Esta afirmación sostiene todo el proyecto. Si proteger la cadena añade casi ningún coste al cálculo subyacente, producir ese cálculo resulta casi gratis.

**La propuesta ofrece dos resultados por uno: una pasada de GPU, dos resultados.**

Esta afirmación distingue a Pearl de una década de conceptos fallidos de PoUW. La mayoría no tenía un límite de este tipo.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Diagrama de cómo Pearl convierte una multiplicación de matrices en una GPU en un compromiso hash y una prueba de conocimiento cero que la cadena verifica a bajo coste" >}}

### Qué calcula el minero

Hay dos métodos y no son equivalentes.

**El método oficial** viene en el repositorio de Pearl. Tiene dos componentes: `pearl-gateway`, que conecta con tu nodo, y `vllm-miner`, que realiza el cálculo en la GPU mediante vLLM. La pasarela se comunica por JSON-RPC con un nodo `pearld` local y ofrece una interfaz de minería mediante un socket Unix o el puerto TCP 8337.

**El método con pool** es el que usa la mayoría. SRBMiner-MULTI implementa el algoritmo `pearlhash` de Pearl y lo configuras para conectarse a un pool.

La diferencia importa para evaluar la utilidad. **El minero oficial carga un modelo de lenguaje real.** El ejemplo de la documentación de Pearl ejecuta `pearl-ai/Llama-3.3-70B-Instruct-pearl` en Docker con acceso a la GPU. Este modelo de 70.000 millones de parámetros procesa inferencias mientras la misma operación protege la cadena.

*Producir inferencias es una capacidad real. Producir inferencias que nadie compra es un centro de costes con una blockchain conectada. Mantén separadas ambas ideas.*

## Por qué fue rentable y por qué cambió

La rentabilidad inicial de Pearl no era un misterio ni dependía de la IA. Seguía la curva de emisiones habitual de una moneda nueva.

| Cuándo | Qué ocurrió |
|---|---|
| **27 de abril de 2026** | Lanzamiento de la red principal |
| **Finales de mayo de 2026** | Comienza la fiebre de minería con GPU, cinco semanas después del lanzamiento |
| **Junio de 2026** | Los ingresos diarios estimados de una RTX 5090 **se reducen aproximadamente a la mitad** al subir la dificultad |
| **De mediados a finales de 2026** | El software de minería mejora mucho su eficiencia y compensa parte de la caída |

El mecanismo de compresión es sencillo:

1. **Las emisiones iniciales son altas y la dificultad es baja.** Los primeros mineros reciben recompensas muy elevadas por unidad de tasa de hash.
2. **Las recompensas atraen más tasa de hash.** Más GPU se conectan a la red.
3. **La dificultad aumenta para ajustarse.** La recompensa por GPU disminuye.

Pearl añade otra presión a la baja porque la recompensa por bloque disminuye por diseño. **Los ingresos tienen dos motivos para caer y la dificultad solo uno para subir.**

### La fuerza compensatoria: eficiencia del programa

Los márgenes no cayeron por igual porque el software de minería se volvió más rápido. El registro de cambios de pearlhash en SRBMiner muestra la mejora:

| Versión | Cambio en Pearlhash |
|---|---|
| **3.6.1** | Añadió compatibilidad con B300. Se informaron unos **706 TH/s a 920 W** con B300 SXM6 y `--gpu-cclock 1600` |
| **3.6.2** | Mejoras para H100, H200 y la serie 4000 |
| **3.6.8** | Mejoró la tasa de hash, sobre todo en la serie 3000 |
| **3.6.9** | **Grandes mejoras de eficiencia.** La misma tasa de hash o una mayor con mucho menos consumo en la mayoría de arquitecturas |

**Para quien mina en casa, la electricidad es el principal coste operativo.** Una versión que mantiene la tasa de hash y reduce el consumo mejora el margen directamente, sin cambios en el precio del token ni en la dificultad de la red. Por eso un equipo que apenas era rentable en junio parece razonable en septiembre con el mismo hardware.

*Las mejoras de eficiencia ayudan de verdad, pero su efecto es temporal porque todos los demás también las aprovechan y aumentan la dificultad.*

## La bifurcación blanda con penalización por rango

La noche del **6 de agosto de 2026**, se activó una bifurcación blanda en Pearl alrededor de las **02:00 UTC, bloque 96251**. Muchos mineros se enteraron a la mañana siguiente, cuando cayó su tasa de hash.

El protocolo de Pearl tiene un parámetro de **rango de ruido**. Un rango más alto facilitaba ganar un premio mayor con la misma cantidad de trabajo. **Algunos mineros operaban deliberadamente con rangos altos y obtenían una tasa de hash efectiva y recompensas desproporcionadas.** El equipo investigó lo que describió como optimizaciones anómalas de minería y respondió con un mecanismo de penalización.

| Cambio de regla | Efecto |
|---|---|
| **Rango mínimo permitido** | 128 |
| **Límite del premio mayor** | Ahora se escala según la fórmula `128 / rank` |
| **Ventaja de los rangos altos** | Eliminada por completo |

**Impacto en los mineros:**

- Minar por encima del rango 128 costó a esos operadores **entre el 50 % y el 87,5 % de la tasa de hash efectiva**
- Minar en el rango 128 o por debajo apenas tuvo coste

Quien empiece ahora debe tener presentes dos lecciones.

**Tu tasa de hash depende del software y las reglas de la red, no solo de la GPU.** Una configuración que dio buenos resultados en julio no medía lo que el operador suponía.

**Actualiza el minero cuando cambie la red.** Las versiones antiguas pierden mucha eficiencia o dejan de funcionar correctamente con las reglas nuevas. El software de los pools se actualizó antes de la bifurcación, incluidas PearlFortune v2.1.0 y Krig (Kryptex) v1.1.0, junto con mineros como Tw-pearl-miner v3.3.0 y Wildrig 0.49.8.

*Una bifurcación blanda que reduce una recompensa hasta un 87,5 % demuestra con claridad por qué debes seguir los anuncios del proyecto, no solo el panel de pagos.*

## Dos formas de minar Pearl

| | Minería en pool | Minero oficial vLLM |
|---|---|---|
| **Software** | SRBMiner-MULTI | `pearl-gateway` y `vllm-miner` |
| **Algoritmo** | `pearlhash` | NoisyGEMM mediante vLLM |
| **¿Requiere un nodo?** | No | **Sí, un `pearld` sincronizado** |
| **Pago** | Pool, PPLNS o en solitario | Directo a tu dirección de minería |
| **Ejecuta un modelo real** | No | **Sí, por ejemplo Llama-3.3-70B-Instruct** |
| **Dificultad de configuración** | Baja | Alta, requiere CUDA Toolkit y Python 3.12 |
| **Ideal para** | Empezar a aportar tasa de hash rápidamente | Aportar capacidad de cómputo a la red directamente |

**Empieza con la minería en pool.** No requiere nodo, sincronización ni descarga de modelos, y te permite aportar tasa de hash y recibir pagos en minutos. Pasa al minero oficial solo si quieres procesar inferencias o ejecutar un nodo.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Diagrama que compara la minería de Pearl en un pool con SRBMiner frente al minero oficial vLLM, e indica los componentes de nodo, pasarela e inferencia de cada método" >}}

## Equipo para GPU de consumo

Pearl destaca por lo que no exige. Hashrate Index indicó que el hardware necesario es **inusualmente modesto: poca RAM, poco almacenamiento y CPU, y sin las costosas redes multifibra que necesita un clúster real de entrenamiento.** Un analista lo describió como «una gran forma de aprovechar equipos existentes».

Este es su atractivo real. **Las GPU que ya tienes, incluso las más antiguas, generan algún ingreso.**

| Tipo de GPU | Observación |
|---|---|
| **RTX 5090 y 4090** | Mayor ingreso por tarjeta. En estas categorías se midió la reducción inicial de ingresos a la mitad |
| **Serie RTX 3000** | La mejora de tasa de hash de la versión 3.6.8 se dirigió específicamente a esta serie. Sigue siendo viable y la eficiencia importa más que la velocidad bruta |
| **Aceleradores de centros de datos** | Se añadieron H100, H200 y B300 y recibieron mejoras durante 2026. Aquí se dirige la competencia por la tasa de hash |
| **Tarjetas antiguas o con poca VRAM** | Rentabilidad marginal. Consulta una calculadora de rentabilidad actualizada antes de montar nada |

**Todas las versiones de 2026 siguen el mismo patrón.** Primero se añadieron y mejoraron los aceleradores de gama alta, porque allí cada unidad de tasa de hash aporta más. Las GPU de consumo recibieron atención cuando aún había margen para mejorar la serie 3000.

*Ajustar la eficiencia genera más ingresos que perseguir la velocidad de reloj. Es lo contrario de lo que enseñan muchas guías de minería.*

## Configuración en Linux

Para minar en un pool necesitas cuatro cosas: el ejecutable de SRBMiner, una dirección de billetera Pearl, un servidor de pool y un servicio que lo mantenga en ejecución.

### Primero crea una dirección de billetera

Las direcciones de minería de Pearl empiezan por **`prl1`**. La billetera oficial es **Oyster**, el servicio de billetera HD del repositorio de Pearl, que ofrece interfaces JSON-RPC y gRPC. Genera desde allí una dirección de minería **Taproot**.

No omitas este paso ni reutilices una dirección de otra cadena. **Si envías recompensas a una dirección que no controlas, las pierdes.**

### Pools, puertos y minería combinada

El pool más grande de Pearl es LuckyPool, que ofrece puertos según la tasa de hash esperada:

| Puerto | Dificultad inicial | Tasa de hash recomendada |
|---|---|---|
| **3360** | 2M | Menos de 500 TH/s |
| **3361** | 4M | De 500 a 1000 TH/s |
| **3362** | 8M | Más de 1000 TH/s |

Elige el puerto que corresponda a la tasa de hash real de tu equipo. **Una sola GPU de consumo debe usar el puerto 3360.** Conectar un equipo pequeño a un puerto de alta dificultad crea largos intervalos entre participaciones y más variación, sin ninguna ventaja.

Conviene conocer dos funciones de los pools:

- **Minería en solitario** funciona en cualquier puerto si antepones `solo:` a la dirección de la billetera. Si encuentras un bloque, recibes toda la recompensa. Si no, no recibes nada. Con la tasa de hash de una GPU de consumo, tendrás que esperar mucho.
- **La minería combinada de Nockchain** genera NOCK junto con PRL usando la misma tasa de hash. Añade `+NOCK_ADDRESS` a tu dirección de Pearl. El pool paga NOCK en la propia Nockchain, por lo que una dirección de token envuelto que empiece por `0x` no puede recibirlo. **Tu minero debe admitir la minería combinada. Sin esa función, seguirá minando Pearl con normalidad.**

El pool publica servidores en `luckypool.io` y servidores de ruta en `lproute.com`. Si tu red bloquea el tráfico directo de minería, conserva el puerto y cambia el dominio.

## Guion de instalación funcional

El siguiente script configura SRBMiner como servicio systemd en Debian o Ubuntu. Detecta todas las GPU, aplica opciones de overclock por tarjeta, verifica la descarga con el MD5 publicado, crea la unidad y una política de logrotate y reinicia el servicio.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- configura SRBMiner (Pearl / PRL) como servicio systemd.
# Ejecutar: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... añade +NOCK_ADDRESS para minar en combinación
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Ajustes para GPU RTX 3070. MCORE fija el reloj de memoria de forma absoluta, muy por debajo de
# frecuencia de fábrica de 7001 MHz. Es una reducción deliberada para mejorar la eficiencia, no
# un overclock de rendimiento. Usa "" para desactivar cualquier opción.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

Conviene explicar el bloque de ajustes porque a primera vista parece incorrecto. **`MCORE=5001` está por debajo del reloj de memoria de fábrica de una 3070.** Es intencional. Pearl recompensa la eficiencia de memoria, y reducir el reloj de memoria baja el consumo más que la tasa de hash. **No copies cifras de overclock de una fila de una base de datos sin comprobar qué GPU se usó en la prueba.** Es frecuente que la medición corresponda a una tarjeta distinta de la tuya.

```bash
[ "$(id -u)" -eq 0 ] || { echo "ejecuta como root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "falta nvidia-smi; instala primero el controlador"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== GPU NVIDIA detectadas: $GPU_N =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Crea un conjunto de opciones de overclock por cada GPU detectada
OC=""
for i in $(seq 0 $((GPU_N - 1))); do
    [ -n "$COFFSET" ] && OC="$OC --gpu-coffset$i $COFFSET"
    [ -n "$CCLOCK" ]  && OC="$OC --gpu-cclock$i $CCLOCK"
    [ -n "$MCLOCK" ]  && OC="$OC --gpu-mclock$i $MCLOCK"
    [ -n "$PLIMIT" ]  && OC="$OC --gpu-plimit$i $PLIMIT"
    [ -n "$FAN" ]     && OC="$OC --gpu-fan$i $FAN"
done
THERMAL_ARG=""
[ -n "$THERMAL" ] && THERMAL_ARG=" --shutdown-temperature $THERMAL"

# Descarga y verifica la versión
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Detén el servicio antes de sustituir el ejecutable. El proceso mantiene abierto el archivo.
systemctl stop "$SVC" 2>/dev/null || true
tar -xzf "$TMP/$STEM.tar.gz" -C "$TMP"
SRC=$(find "$TMP" -maxdepth 1 -type d -name 'SRBMiner-Multi-*' | head -1)
mkdir -p "$MINER_DIR"
[ -f "$MINER_DIR/SRBMiner-MULTI" ] && \
    cp -a "$MINER_DIR/SRBMiner-MULTI" "$MINER_DIR/SRBMiner-MULTI.bak-$(date +%F-%H%M%S)"
cp -a "$SRC"/. "$MINER_DIR"/
chown -R root:root "$MINER_DIR"
chmod 755 "$MINER_DIR/SRBMiner-MULTI"
```

**Verifica el MD5 antes de ejecutar cualquier binario de minería.** Las versiones publican hashes por archivo, y el minero se ejecuta con privilegios de root y accede a tu GPU. Si omites la verificación, confías en una descarga que no has inspeccionado.

Dos detalles operativos de la unidad de servicio:

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Minero Pearl (PRL) SRBMiner v$SRB_VERSION - $WORKER
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$MINER_DIR
ExecStart=$MINER_DIR/SRBMiner-MULTI --algorithm $ALGO --pool $POOL --wallet $WALLET --worker $WORKER --disable-cpu --gpu-reset-oc$OC$THERMAL_ARG --api-enable --api-port 21550 --api-rig-name $WORKER
Restart=always
RestartSec=10
StandardOutput=append:$LOG
StandardError=append:$LOG
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
```

- **`--disable-cpu`** evita que el minero use la CPU, algo importante si el equipo también realiza otras tareas.
- **`--shutdown-temperature 88`** detiene el minero si falla un ventilador, en vez de sobrecalentar la tarjeta.
- **`--gpu-reset-oc`** borra los ajustes de reloj anteriores antes de aplicar los tuyos y evita que sigan activos valores obsoletos.
- **`Restart=always` con `RestartSec=10`** permite recuperarse de fallos del controlador, habituales en equipos con varias GPU.
- **`--api-enable` abre un puerto de supervisión.** Confirma en qué interfaz escucha el puerto 21550 y no lo expongas a una red que no sea de confianza. El endpoint de supervisión no necesita ser accesible desde fuera del equipo.

Configura también la rotación de registros, porque los archivos de minería crecen sin límite:

```bash
cat >/etc/logrotate.d/pearl-miner <<EOF
$LOG {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
EOF

systemctl daemon-reload
systemctl enable "$SVC" >/dev/null 2>&1 || true
systemctl restart "$SVC"
```

*`copytruncate` importa en este caso. SRBMiner mantiene abierto el registro. Si la rotación cambia el nombre del archivo, el minero escribe en un inodo eliminado y el disco se llena igualmente.*

Consulta el progreso con una muestra filtrada en vez de leer el registro sin filtrar:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Qué ha salido mal

**Una guía de minería de Pearl debe empezar por los problemas, porque todos afectan a tus pagos.** Cuatro cosas salieron mal entre julio y septiembre de 2026.

### El mercado depende de una sola bolsa

El **23 de julio de 2026**, PRL marcó un mínimo histórico de **0,1399 $**, frente a unos **87 centavos** en junio. Cayó **un 24,2 % en un día** y **un 26,7 % en una semana**, mientras el mercado cripto general subió cerca de un 2 % en el mismo periodo.

La causa no fueron las noticias. Fue la falta de profundidad del mercado.

- **El 95,17 % de todo el volumen declarado** se concentró en **una sola bolsa, SafeTrade**, que no tiene una puntuación de confianza de CoinGecko. Un par PRL/USDT representó **738.399 $ de unos 775.000 $** negociados en 24 horas.
- Ambos pares de SafeTrade registraban **0,00 $ de profundidad en el libro de órdenes**.

*Una orden de venta corriente mueve un mercado así en porcentajes de dos cifras. Es una característica estructural del token, no una condición temporal.*

La distribución de la oferta agrava el problema:

| Métrica | Valor |
|---|---|
| **Capitalización de mercado** | 55,7 millones de dólares |
| **Valoración totalmente diluida** | 458,6 millones de dólares |
| **Proporción** | Más de 8 veces |
| **Oferta circulante** | 255 millones de 2.100 millones, menos del **13 %** |

**Un token valorado en un libro de órdenes poco profundo, con el 87 % de la oferta bloqueada o aún sin emitir, admite una amplia gama de precios plausibles.** Planifica qué hacer con los pagos y no trates el precio al contado como una estimación fiable de ingresos.

### Un servicio de minería sufrió un ataque

Una incidencia abierta el **18 de septiembre de 2026** informa que la billetera Pearl 2.0.5 «todavía tenía suspendidos los envíos y las recepciones tras el ataque a su pool de hacía un mes».

**Léelo dos veces, porque contiene dos hechos.** Un pool de Pearl sufrió un ataque alrededor de **agosto de 2026** y la billetera oficial respondió suspendiendo las transferencias. La suspensión seguía vigente un mes después.

El pool que elijas retiene tus pagos. Revisa su historial de incidentes antes de conectar tu equipo.

### El sitio del proyecto no está disponible

Al redactar este artículo, **pearlresearch.ai no llega a ningún servidor.** Todos los resolutores públicos devuelven una ruta nula, `0.0.0.0`, para el dominio raíz y subdominios como `compute` y `explorer`. El registro del dominio indica `ACTIVE`, así que se trata de un estado DNS deliberado y no de un dominio vencido.

**Hay tres enlaces habituales en una guía de minería que no funcionan**, incluido el explorador de bloques. Mining Pool Stats aún los publica y por eso los lectores terminan intentando abrir una dirección que nunca carga.

Usa **[el explorador de bloques PRL](https://prlscan.com)** en su lugar. Confirmé que la página funciona.

### El programa todavía tiene errores abiertos

El rastreador público de incidencias mostraba problemas sin resolver a finales de septiembre de 2026. La creación de incidencias está restringida, por lo que esta vista es parcial.

| Incidencia | Fecha | Consecuencia |
|---|---|---|
| **Código RPC de la billetera de escritorio inactivo** | 22 sep. | La billetera no se conecta a un nodo |
| **La red de prueba no puede sincronizar desde cero**, los nodos se bloquean en la altura 36760 | 22 sep. | Hay un defecto que impide la sincronización |
| **Envíos y recepciones de la billetera siguen suspendidos** tras el ataque al pool | 18 sep. | Las transferencias están afectadas |
| **La versión para macOS ARM64 tiene una firma de código no válida** | 17 sep. | No se ejecuta sin omitir Gatekeeper |
| **El modo de poda elimina certificados necesarios para verificar encabezados** | 30 ago. | Defecto de validación |
| **El nodo se bloquea indefinidamente si ningún par conectado puede sincronizar** | 30 ago. | Sincronización inestable |
| **pearl-gemm falla en RTX 5070**: funcionan los kernels de hash, pero fallan los de GEMM | 31 ago. | Las GPU de consumo más recientes no son compatibles |

*La incidencia de la RTX 5070 importa si pensabas comprar una tarjeta actual. La arquitectura de consumo más nueva no funcionaba con el método GEMM oficial.*

**En conjunto:** el software de minería recibe mantenimiento activo, mientras que la experiencia de usuario y el mercado son los puntos débiles. SRBMiner publicó la versión 3.6.9 con grandes mejoras de eficiencia el día anterior a esas quejas sobre la billetera.

## ¿Es útil la red?

Esta pregunta merece una respuesta cuidadosa porque muchas publicaciones usan «trabajo útil» para hablar de dos cosas. **Describe un mecanismo de consenso y una afirmación económica, y las respuestas para cada una son muy distintas.**

### Utilidad funcional: parcial

**La cadena funciona. El producto que la rodea todavía no funciona por completo.**

Lo que sí funciona:

- **La red principal se lanzó el 27 de abril de 2026** y desde entonces produce bloques.
- **El conjunto de componentes es completo y real**: un nodo, una billetera, un cliente ligero SPV, un sistema de pruebas de conocimiento cero y un minero para GPU, todo en un repositorio.
- **La infraestructura está probada a nivel de código.** El nodo, la billetera y el cliente ligero derivan de **btcd**, **btcwallet** y **neutrino**, proyectos Bitcoin con años de pruebas frente a atacantes.
- **El código refleja un esfuerzo serio.** Tiene 315 estrellas, 76 bifurcaciones, más de 6.800 confirmaciones y un rastreador público donde los colaboradores presentan informes de errores detallados.
- **La minería funciona.** SRBMiner publicó 247 versiones y optimizó `pearlhash` repetidamente. Hay varios pools activos. La minería combinada de Nockchain funciona.

Lo que no funciona:

- **Las transferencias están suspendidas en la billetera oficial** tras el ataque al pool.
- **La billetera de escritorio no logra conectarse a un nodo**, según su propio rastreador a finales de septiembre.
- **La lógica de sincronización tiene defectos bloqueantes** tanto en la red de prueba como en la principal.
- **El sitio del proyecto no está disponible.**
- **Las GPU de consumo más recientes fallan con el método GEMM.**

**La conclusión honesta es que Pearl funciona en la capa de protocolo y no es fiable como producto.** Esto interesa a quien estudia la prueba de trabajo útil. Es una advertencia para quien espera minar y cobrar con fiabilidad.

### Utilidad técnica: el mecanismo sí, el mercado no

La respuesta honesta se divide en dos. Confundir ambas partes es el error de la mayoría de los análisis.

**El mecanismo sí es novedoso.** La rutina NoisyGEMM de Pearl calcula multiplicaciones de matrices con ruido en una GPU, convierte el resultado en un compromiso mediante un hash y envuelve el trabajo en una prueba de conocimiento cero para mantener bajo el coste de verificación. La construcción se basa en un artículo real, "Proofs of Useful Work from Arbitrary Matrix Multiplication", de Komargodski, Schen y Weinstein, que afirma un coste adicional aproximado de **1 + o(1)** frente a una multiplicación de matrices ingenua.

**Si se cumple ese límite, la cadena se protege con un coste casi nulo sobre el cálculo subyacente.** Eso es lo que no consiguieron los intentos anteriores de PoUW. Las matemáticas no son un adorno.

**El mercado de este cómputo no está establecido.** Hashrate Index lo resumió así: «hoy la mayor parte del trabajo útil consiste en inferencias que nadie compró, por lo que la mayor parte de la minería actual es una prueba de trabajo con forma de IA». Es una descripción justa. El cómputo tiene la forma adecuada, pero nadie paga por la mayoría.

La excepción importa y es real. Pearl firmó una alianza exclusiva con **Together AI**, que puso en producción un endpoint de inferencia con tecnología Pearl a precio reducido. Es el primer cliente y por eso el proyecto merece más crédito que una moneda promedio con marca de IA.

**Un cliente demuestra el concepto, pero no constituye un mercado.**

### Utilidad práctica: por ahora, con una ventana que se cierra

Para quien mina, la situación práctica es mixta y limitada en el tiempo.

**A favor de Pearl:**

- Las GPU existentes, incluso las antiguas, generan ingresos porque los requisitos de hardware son modestos
- Las mejoras continuas del minero elevan directamente el margen en el hardware que ya tienes
- La minería combinada con Nockchain añade una segunda fuente de ingresos con la misma tasa de hash
- Un coste adicional casi nulo significa que la cadena no consume electricidad en cálculos de hash inútiles

**En contra:**

- **La recompensa por bloque disminuye por diseño.** Sigue el modelo de Bitcoin y las emisiones bajan tanto si sube el precio como si no.
- **La dificultad solo aumenta.** Los ingresos por GPU solo pueden ir en una dirección.
- **La liquidez es escasa.** Hashrate Index señala que conviene vigilar si PRL obtiene liquidez fuera de las bolsas pequeñas. La poca liquidez implica diferenciales mayores y peores precios de venta reales.
- **La actualización del protocolo.** Las notas de SRBMiner 3.6.8 dicen que una próxima actualización de Pearl dejará las GPU de consumo «prácticamente inútiles». Tómalo en serio. Lo afirma el desarrollador, que se beneficia si la gente sigue minando.

## Conclusión

**Pearl es la implementación más creíble de prueba de trabajo útil hasta la fecha, pero todavía no ha demostrado que su trabajo sea útil en términos económicos.**

Cuatro afirmaciones, ordenadas por grado de certeza:

1. **El mecanismo de consenso funciona y la afirmación criptográfica es real.** Pearl resolvió el problema técnico difícil: hacer que PoUW sea barato de verificar. Es una contribución real, independientemente de lo que ocurra con el token.

2. **El cómputo es una promesa, no un producto.** Producir inferencias no equivale a venderlas. Hoy hay un único acuerdo de pago frente a una red llena de tasa de hash especulativa. El ciclo está diseñado, pero no está en marcha.

3. **La ventana para minar con GPU de consumo se estrecha y el protocolo la cerrará.** Una recompensa decreciente, una dificultad creciente, una actualización anunciada que elimina la viabilidad de las GPU de consumo y una bifurcación blanda que ya redujo hasta un 87,5 % la tasa de hash de algunos mineros convierten esto en una oportunidad con fecha de caducidad, no en una fuente de ingresos.

4. **El riesgo real está en la operación y el mercado, no en la criptografía.** Un pool atacado, las transferencias suspendidas de la billetera, un sitio inaccesible, errores de sincronización sin resolver y el 95 % del volumen concentrado en una bolsa sin profundidad de órdenes determinan si la minería paga. El protocolo es la parte que funciona.

*La forma más directa de decirlo: Pearl resolvió el problema difícil, pero aún no el que parece fácil. Demostrar que una multiplicación de matrices es útil es criptografía. Encontrar quién compre el resultado es ventas.*

**Si quieres minar, considéralo un uso a corto plazo del hardware que ya tienes.** No compres GPU para Pearl. No montes un equipo suponiendo que las cifras actuales se mantendrán, porque el calendario de emisiones y las propias notas del desarrollador del minero dicen lo contrario.

**Si quieres entender la prueba de trabajo útil, Pearl es la implementación más importante que debes estudiar ahora.** Es la primera que alcanza una escala real. Las pruebas de los próximos dos años mostrarán si el «trabajo útil» es un componente fundamental o un fracaso recurrente con mejor criptografía.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Diagrama que evalúa la prueba de trabajo útil de Pearl en tres ejes: alta madurez funcional, mecanismo técnico sólido pero mercado de pago no demostrado y viabilidad práctica de minería limitada en el tiempo" >}}

## Puntos clave

- **Pearl es una blockchain L1 derivada de Bitcoin y protegida mediante prueba de trabajo útil.** Los mineros multiplican matrices con ruido en vez de calcular hashes. La red principal se lanzó el **27 de abril de 2026**.
- **Puedes minar de dos formas:** SRBMiner con `--algorithm pearlhash` conectado a un pool, o el `vllm-miner` de Pearl conectado a un nodo sincronizado.
- **La rentabilidad inicial se debió a las emisiones del lanzamiento**, no a la demanda de IA. Los ingresos diarios estimados de una RTX 5090 se redujeron aproximadamente a la mitad pocas semanas después de la fiebre.
- **Las mejoras de eficiencia del minero compensaron parte de la caída.** La versión 3.6.9 ofreció la misma tasa de hash o una mayor con mucho menos consumo.
- **La bifurcación blanda con penalización por rango del 6 de agosto de 2026 redujo entre un 50 % y un 87,5 % la tasa de hash efectiva** de los mineros por encima del rango 128. Actualiza el minero cuando cambien las reglas de la red.
- **El token depende de una sola bolsa.** SafeTrade concentró el 95,17 % del volumen y no tenía profundidad en el libro de órdenes. Menos del 13 % de la oferta está en circulación.
- **Un pool sufrió un ataque alrededor de agosto de 2026**, y la billetera oficial aún mantenía las transferencias suspendidas un mes después.
- **El sitio del proyecto no resuelve el dominio.** Usa `prlscan.com` para explorar bloques.
- **Ajusta la eficiencia, no la velocidad de reloj.** Pearl recompensa la eficiencia de memoria y reducir su reloj baja el consumo más de lo que reduce la tasa de hash.
- **Usa el puerto 3360 con una sola GPU de consumo** y añade `+NOCK_ADDRESS` para minar Nockchain en combinación.
- **Verifica el MD5** de cualquier descarga del minero antes de ejecutarla como root.
- **Mina con hardware que ya tengas.** La cadena funciona a nivel de protocolo, no es fiable como producto y el mercado de cómputo de pago depende de una sola alianza.

## Próximos pasos

1. **Lee el repositorio de origen** del nodo, la billetera y el minero oficial vLLM: **[Repositorio Pearl Research Labs](https://github.com/pearl-research-labs/pearl)**
2. **Consulta el registro de cambios del minero antes de ajustar nada**, porque la eficiencia cambia entre versiones: **[Versiones de SRBMiner-MULTI](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Elige un puerto de pool** que corresponda a tu tasa de hash medida: **[LuckyPool para Pearl](https://pearl.luckypool.io)**
4. **Compara la distribución de tasa de hash de los pools** antes de decidir: **[Estadísticas de pools de minería de Pearl](https://miningpoolstats.stream/pearl)**
5. **Calcula primero tu coste eléctrico**, porque determina la rentabilidad: **[Cómo montar un equipo rentable de ingresos pasivos](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Aplica las pautas de ajuste para varias GPU** de nuestra otra guía de minería con trabajo útil: **[Minar Spacemesh con varias GPU de forma eficiente](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Artículos relacionados

| Artículo | Contenido |
|---|---|
| **[Minar Spacemesh con varias GPU de forma eficiente](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Ajuste de varias GPU y gestión de energía en otra blockchain de trabajo útil |
| **[Cómo montar un equipo rentable de ingresos pasivos](/other/creating-profitable-low-powered-crypto-miners/)** | Dimensionar el hardware de minería según el coste eléctrico antes de comprar |
| **[IA local en 2026: un modelo 27B supera a Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Qué hacen las mismas GPU con inferencia local en vez de minería |
| **[Minar Verus en Android: guía sencilla para minar con un teléfono](/other/mine-verus-on-android-guide/)** | Minería con CPU en hardware que ya tienes |

## Referencias

1. [Pearl Research Labs: monorepositorio de red](https://github.com/pearl-research-labs/pearl)
2. [Incidencias abiertas del repositorio Pearl](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): cómo la computación matricial se convierte en minería y cómputo de IA - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Activación de la bifurcación blanda con penalización por rango en Pearl (PRL) - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl alcanza un nuevo mínimo histórico; el 95 % del volumen se concentra en una bolsa sin profundidad - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [Versiones de SRBMiner-MULTI - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool: pool de minería combinada de Pearl y Nock](https://pearl.luckypool.io)
8. [Estadísticas de pools de minería: Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [Explorador de bloques PRL: prlscan.com](https://prlscan.com)

**Nota sobre el dominio oficial:** `pearlresearch.ai` y los subdominios `compute` y `explorer` devuelven una ruta nula en el momento de redactar el artículo. Se omiten deliberadamente para no publicar enlaces inactivos y se remite al lector a `prlscan.com` para explorar bloques.
