---
title: "Jugando con la red Helium: Explotación de vulnerabilidades con MiddleMan y Chirp Stack Packet Multiplexer"
date: 2023-02-18
toc: true
draft: false
description: "Aprenda a jugar con la red Helium mediante la explotación de vulnerabilidades con MiddleMan y Chirp Stack Packet Multiplexer, así como los riesgos y las consecuencias de hacerlo."
tags: ["red de helio", "Prueba de cobertura", "Intermediario", "Multiplexor de paquetes Chirp Stack", "juego de azar", "explotando vulnerabilidades", "Red LoRaWAN", "criptomoneda", "cadena de bloques", "red descentralizada", "Puntos calientes", "suplantación de identidad", "infiel", "actividad ilegal", "sanciones", "integridad de la red", "recompensas", "actores maliciosos", "Seguridad de la red", "anfitriones legítimos"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "Una representación caricaturesca de un grupo de personas que explotan un globo de helio con una imagen de una puerta de enlace LoRaWAN y MiddleMan o Chirp Stack Packet Multiplexer en el fondo."
coverCaption: ""
---

**Descargo de responsabilidad**:
Es importante tener en cuenta que jugar en la red de Helium es una actividad ilegal y poco ética que la comunidad de Helium y la comunidad más amplia de criptomonedas y blockchain desaprueban enérgicamente. Jugar con la red socava la integridad de la red y daña a los hosts legítimos que brindan una cobertura valiosa a la red.

Además, si bien el uso de MiddleMan y Chirp Stack Packet Multiplexer para explotar vulnerabilidades en la red de Helium puede ser motivo de preocupación, es importante tener en cuenta que Helium solo puede solucionar estos problemas mediante la introducción de puertas de enlace seguras. Esto requeriría reemplazar todos los puntos de acceso en la red, lo cual es una tarea importante y puede no ser factible. Como resultado, la comunidad de Helium debe permanecer atenta y proactiva para abordar los desafíos que plantean los juegos en la red.

También vale la pena señalar que el equipo de Helium ha estado al tanto del problema durante algún tiempo y ha tomado medidas para solucionarlo, pero se requieren más acciones para resolver el problema. La comunidad pide que se tomen medidas reales para abordar estas vulnerabilidades y garantizar que la red pueda continuar escalando y creciendo de manera segura y confiable.

Al escribir este artículo, esperamos generar conciencia sobre el problema de los juegos en la red Helium y el uso de MiddleMan y Chirp Stack Packet Multiplexer para explotar vulnerabilidades en el sistema. Creemos que al arrojar luz sobre este problema y brindarle más publicidad, la comunidad de Helium y la comunidad más amplia de blockchain y criptomonedas pueden unirse para abordar el problema y trabajar hacia una red más segura y confiable.

Además, al resaltar este problema, esperamos alentar al equipo de Helium a tomar medidas más decisivas para abordar las vulnerabilidades en la red e implementar medidas de seguridad más sólidas para evitar juegos en el futuro. Creemos que es importante que el equipo de Helium sea transparente sobre sus esfuerzos para abordar este problema y se comunique con la comunidad sobre su progreso en la solución de estas vulnerabilidades.

Finalmente, al brindar más publicidad a este problema, esperamos fomentar una mayor concienciación y educación sobre los riesgos y las consecuencias de los juegos en la red Helium. Es importante que los usuarios comprendan la importancia del comportamiento ético en la red y el daño potencial que pueden causar los juegos. Al trabajar juntos para abordar estos problemas, podemos ayudar a garantizar el crecimiento y el éxito continuos de la red Helium.

En resumen, ni la comunidad ni nosotros aprobamos jugar en la red Helium, y alentamos a los usuarios a actuar de manera ética y legal cuando participen en la red. Si bien existen vulnerabilidades en la red que pueden explotarse, es importante mantenerse alerta y proactivo para abordar estos problemas y trabajar para lograr una red más segura y confiable para todos los usuarios.

## Cómo jugar con la red Helium con MiddleMan y Chirp Stack Packet Multiplexer
La red Helium es una red LoRaWAN® descentralizada que compensa a quienes alojan puntos de acceso físicos al recompensarlos con tokens Helium, o $HNT. Este sistema se conoce como Prueba de Cobertura (PoC). A medida que la red ha crecido y ha aumentado la conciencia de este proyecto, ha habido un número cada vez mayor de tramposos que explotan el protocolo y los mecanismos de recompensa. En este artículo, discutiremos cómo jugar con la red Helium utilizando MiddleMan y Chirp Stack Packet Multiplexer.

## Comprender el problema de los juegos en red de helio
La red Helium se basa en la Prueba de cobertura para garantizar que los puntos de acceso brinden cobertura donde se necesita. Sin embargo, este sistema es vulnerable a los juegos, la suplantación de identidad, la piratería y otros tipos de mal comportamiento que pueden dañar la red. El problema de los juegos en la red Helium le está costando a los hosts legítimos miles de $HNT por mes. Helium, Inc, junto con DeWi, tomó medidas agresivas a principios de 2022 para ayudar a eliminar este problema.

## Hardware necesario
- [Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
- [Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
- [Raspberry Pi](https://amzn.to/3KjFCYp)
- [Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## Uso de MiddleMan para jugar con la red Helium
Una forma de jugar con la red Helium es usar MiddleMan. MiddleMan es una herramienta de software que se puede usar para crear un punto de acceso falso que parece estar brindando cobertura en una ubicación específica. Al usar MiddleMan, un usuario puede crear un punto de acceso falso que recibirá recompensas por brindar cobertura en un área en particular, aunque el punto de acceso no esté ubicado físicamente en esa área.

Para usar MiddleMan, un usuario debe instalar el software y crear un punto de acceso falso. Luego, el usuario puede configurar el punto de acceso para informar su ubicación a la red Helium utilizando una herramienta de suplantación de GPS. La red Helium creerá que el punto de acceso falso proporciona cobertura en la ubicación especificada y recompensará al usuario con $HNT.

Configuraría su puerta de enlace lorawan para que apunte a este software y manipule los valores para que todos los PoC recibidos se consideren válidos. El uso del reenviador semtech es uno de los diversos estándares en la comunidad LoraWAN. Solucionar el problema de la manipulación requeriría reinventar la rueda e implementar su propio protocolo desde cero. Cosas como las sumas de verificación y el cifrado evitarían que esto suceda. Pero también dificultaría que los proveedores con hardware diferente creen puntos de acceso. Sin mencionar que es un caso de uso compatible tener un minero de helio y múltiples puertas de enlace lora para una mejor cobertura. Aunque esto es más un problema de nivel empresarial.

 - [helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## Uso del multiplexor de paquetes Chirp Stack para jugar con la red Helium
Otra forma de jugar con la red Helium es usando Chirp Stack Packet Multiplexer. Chirp Stack Packet Multiplexer es una herramienta que se puede usar para crear un punto de acceso virtual que puede recibir paquetes de varios puntos de acceso físicos. Al usar Chirp Stack Packet Multiplexer, un usuario puede crear un punto de acceso virtual que recibe paquetes de puntos de acceso físicos en múltiples ubicaciones, lo que aumentará las recompensas obtenidas.

Para usar Chirp Stack Packet Multiplexer, un usuario debe instalar el software y configurarlo para recibir paquetes de puntos de acceso físicos o puertas de enlace lorawan en múltiples ubicaciones. El punto de acceso recibirá los paquetes e informará su ubicación a la red Helium, que recompensará al usuario con $HNT.

Esto permite la entrada de múltiples reenviadores y la salida de múltiples puertas de enlace. Hay casos de uso legítimos para este software en la comunidad LoraWAN, pero usarlo en helio es un área gris en el mejor de los casos. Depende de cómo lo uses y también de cuál sea tu intención.

Configurar este requiere algunos archivos de configuración. Pero se puede hacer en 5 minutos o menos.
- [chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## Riesgos y consecuencias de jugar con la red Helium
Jugar en la red Helium es una actividad arriesgada e ilegal que puede tener graves consecuencias. Helium, Inc, junto con DeWi, está trabajando activamente para detectar y prevenir juegos en la red, y los usuarios que sean sorprendidos jugando en la red serán penalizados.

Las sanciones por jugar en la red Helium pueden incluir la pérdida de acceso a la red, la prohibición permanente de los puntos de acceso y la pérdida de cualquier $HNT que se ganó a través del juego. Además, jugar con la red Helium socava la integridad de la red y daña a los hosts legítimos que brindan una cobertura valiosa a la red.

## Conclusión
Si bien la red Helium brinda oportunidades para que los hosts de puntos de acceso legítimos ganen recompensas a través de la Prueba de cobertura, también presenta un objetivo atractivo para los actores maliciosos que buscan jugar con el sistema. El uso de MiddleMan y Chirp Stack Packet Multiplexer, aunque Helium Inc. o la comunidad en general no lo aprueban, es un ejemplo de cómo algunos malos actores están explotando las vulnerabilidades en la red para obtener recompensas a expensas de otros.

Es importante que la comunidad de Helium continúe trabajando en conjunto para identificar y abordar el juego en la red, ya que amenaza la integridad del sistema y socava los esfuerzos de los hosts legítimos. Esto puede incluir esfuerzos para desarrollar e implementar medidas de detección y prevención más sofisticadas, así como aumentar la conciencia y la educación sobre los riesgos y las consecuencias de los juegos en la red.

En última instancia, el éxito de la red Helium depende de la voluntad de sus partes interesadas de trabajar juntas para construir un sistema seguro, confiable y digno de confianza que brinde un valor real a sus usuarios. Manteniéndose alerta y proactiva para abordar los desafíos que plantean los juegos, la comunidad puede ayudar a garantizar que la red de Helium continúe creciendo y evolucionando en una dirección positiva.