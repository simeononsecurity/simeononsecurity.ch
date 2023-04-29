---
title: "Construyendo contenedores Docker eficientes y seguros: Guía para principiantes"
date: 2023-02-24
toc: true
draft: false
descripción: "Aprende a crear contenedores Docker eficientes y seguros utilizando las mejores prácticas, consejos e instrucciones paso a paso en esta completa guía."
tags: ["docker", "containers", "containerization", "devops", "deployment", "portability", "efficiency", "security", "best practices", "Dockerfile", "base images", "environment variables", "volume mounts", "root user", "up-to-date images", "software development", "container images", "Docker Hub", "container orchestration", "Kubernetes"].
cover: "/img/cover/A_3D_imagen_animada_de_un_contenedor_seguro_bien_organizado.png"
coverAlt: "Imagen animada en 3D de un contenedor seguro y bien organizado con el logotipo de Docker sobre él, rodeado de diversas herramientas y equipos relacionados con la ingeniería de software y DevOps."
coverCaption: ""
---
```bash
FROM ubuntu:latest
EJECUTAR apt-get update && apt-get install -y nginx
COPIAR index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```
```bash
docker run -d -p 80:80 my-nginx-image
```
``dockerfile
RUN apt update
RUN apt install apache -y
```
archivo apcker
RUN apt update && apt install apache -y
```
``bash
docker run -e PORT=3000 my-app
```
``Dockerfile
DESDE nodo:14

# Establecer el directorio de trabajo
directorio de trabajo /app

# Copiar package.json y yarn.lock al contenedor
COPIAR package.json yarn.lock ./

# Instalar dependencias
EJECUTAR yarn install --frozen-lockfile

# Copiar el código de la aplicación al contenedor
COPIAR . .

# Exponer el puerto de la aplicación
EXPONER $PUERTO

# Iniciar la aplicación
CMD ["yarn", "start"]
```
```bash
docker run -v /home/user/app/data:/app/data my-app
```
```Dockerfile
DESDE nodo:14

# Establecer el directorio de trabajo
directorio de trabajo /app

# Copia los ficheros package.json y yarn.lock al contenedor
COPIAR package.json yarn.lock ./

# Instale las dependencias
EJECUTAR yarn install --frozen-lockfile

# Copiar el resto del código de la aplicación al contenedor
COPIAR . .

# Exponer el puerto de la aplicación
EXPONER 3000

# Iniciar la aplicación
CMD ["yarn", "start"]

# Montar un volumen para los datos de la aplicación
VOLUMEN ["/app/data"]
```
```Dockerfile
DESDE nodo:14

# Crear un nuevo usuario para ejecutar el contenedor
RUN useradd --user-group --create-home --shell /bin/false app

# Cambia el directorio de trabajo al directorio home del usuario app
WORKDIR /home/app

# Instalar dependencias como usuario de app
COPIAR package.json yarn.lock ./
EJECUTAR chown -R app:app /home/app
USUARIO app
EJECUTAR yarn install --frozen-lockfile --production

# Copiar el código de la aplicación como usuario de app
COPIAR --chown=app:app . .

# Exponer el puerto
EXPONER 3000

# Iniciar la aplicación como usuario
CMD ["yarn", "start"]
```
```Dockerfile
FROM ubuntu:latest

# Actualizar la lista de paquetes e instalar las actualizaciones de seguridad
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Instalar el servidor web nginx
RUN apt-get install -y nginx

# Copia el código de la aplicación al contenedor
COPIAR . /var/www/html/

# Exponer el puerto 80 al sistema anfitrión
EXPONER 80

# Iniciar el servidor nginx
CMD ["nginx", "-g", "daemon off;"]

```


 ** كيفية بناء حاويات Docker **
 
 أداة التشغيل القوية يمكن استخدامها لتطبيقات البيع بالتجزئة محمولة وقابلة للنشر بسهولة. في هذا الدليل ، سنغطي الخطوات الأساسية لبيع وبناء حاويات. الحصول على بعض المعلومات على صور موثوقة.
 
 ## فهم عامل ميناء
 
 قبل أن نبدأ في بناء حاويات Docker ، من المهم أن نفهم ما هو Docker وكيف يعمل.
 
 حزم حزم حزم وتبعياته في حزم حزم وحزمه. الحاوية معزولة عن النظام المضيف كل ما يلزم ، بما في ذلك الكود ووقت التشغيل والأعدادات والمكتبات والإعدادات.
 
 طباعة ، جاهزة ، جاهزة ، جاهزة Docker ، حيث يمكنك إنشاء وإدارتها في واجهة سطر أوامر.
 
 ## بناء صورة عامل ميناء
 
 إنشاء صورة Docker. صورة Docker هي لقطة لحاوية جميع الملفات والمكتبات والاعتماديات لتشغيل التطبيق.
 
 فيما يلي خطوات البيع بالتجزئة
 
 1. ** إنشاء Dockerfile **
 2. ** بناء الصورة **
 3. ** تشغيل الحاوية **
 
 ### الخطوة الأولى: إنشاء ملف Dockerfile
 
 الخطوة الأولى لبناء صورة Docker هي إنشاء Dockerfile. تعليمات. فيما يلي مثال على ملف Dockerfile بسيط:
 
 
 ملف عامل هذا:
 
 - يحدّد "FROM ubuntu: latest" الصورة الأساسية المراد لفكرة للحاوية. في هذه الحالة ، حالة ، أحدث إصدار من Ubuntu.
 - يقوم `RUN apt-get update && apt-get install -y nginx` بتحديث قائمة الحزم وتثبيت خادم الويب nginx.
 - نسخ `` COPY index.html / var / www / html / `ملف index.html إلى الويب الخاص بالحاوية.
 - يعرض "EXPONER 80" المنفذ 80 المضيف.
 - `CMD [" nginx "،" -g "،" daemon off ؛ "]
 
 ### الخطوة الثانية: بناء الصورة
 
 بعد إنشاء ملف Dockerfile ، تم إنشاء الصورة باستخدام عامل ميناء. هذا المثال:
 
 
 لنفصل هذا الأمر:
 
 - "Docker run" يخبر Docker يتيح حاوية.
 - "-d" يشغل الحاوية في وضع منفصل ، مما يعني أنه تعمل في الخلفية.
 - "-p 80: 80" يعين المنفذ 80 على المضيف للمنفذ 80 في الحاوية.
 - "يحدد صورة nginx" اسم صورة Docker لاستخدامها في الحاوية.
 
 ## أفضل الممارسات
 
 بعد أن رسالتك أفضل الجامعات.
 
 ### استخدام الصور الأساسية الصغيرة
 
 استخدام صور أساسية صغيرة الحجم فقط على التبعيات التي يحتاجها تطبيقك. على سبيل المثال ، استخدام نظام تشغيل كامل مثل Ubuntu أو CentOS ، يمكنك استخدام صورة أصغر مثل Alpine Linux أو BusyBox.
 
 ### تصغير الطبقات
 
 ينشئ كل سطر في Dockerfile طبقة جديدة في صورة Docker ، ويضيف كل طبقة إلى حجم الصورة. حاول تقليل عدد الطبقات في صورتك. مجموعة من العمل الجماعي في مجموعة الأوامر المتشددة في سطر واحد بك. مثال على سبيل المثال ، استخدام أمرين في نفس الوقت.
 
 السابق:
 ضد
 
 ### استخدام متغيرات البيئة
 
 استخدام متغيرات البيئة في Dockerfile الخاص بك بدلاً من قيم التشغيل يجعل من السهل السهل الحاوية الخاصة بتشغيل التشغيل ويضمن أن Dockerfile الخاص قابل للنقل. على سبيل المثال ، استخدام استخدام متغيرات البيئة المحيطة التي تعمل على تطبيق التطبيق أو موقع التكوين.
 
 السابق:
 
 
 ### استخدام حوامل الصوت
 
 ذاكرة التخزين الخاصة بك. هذا يجعل من السهل إدارة البيانات ويقلل من حجم حاوية Docker الخاصة بك. على سبيل المثال ، استخدام استخدام وحدة تخزين قاعدة بيانات بين نظامك وحاويتك.
 
 السابق:
 
 
 ### تجنب الجري كجذر
 
 يمكن أن يؤدي إلى تشغيل Docker كمستخدم أساسي إلى مخاطر أمنية. إنشاء مستخدم جديد في الحاوية. استخدام الأمر استخدام الأمر `USER` في ملف Dockerfile الخاص بستخدام الأمر استخدام الأمر.
 
 السابق:
 
 ### تحديث الصور باستمرار
 
 التأكد من أن التأكد من أن تكون آمنة وخالية من نقاط الضعف ، من المهم أن تقوم بتحديث الصور الخاصة بك. هذا يعني تحديث الصورة الأساسي وأي تبعيات يعتمد عليها تطبيقك. المثال ، استخدام الأمرين "apt-get update" و "apt-get Upgrade" في Dockerfile الخاص لتحديث الحاوية مع أحدث تصحيحات وإصلاحات وإصلاحات وإصلاحات الأخطاء.
 
 السابق:
 ## مزيد من دراساتك
 ### توثيق عامل السفن
 [Docker] (https://www.docker.com/) هو نظام أساسي مفتوح المصدر ، تطبيقات وشحنها وتشغيلها في. يوفر موقع وثائق وثائق مفصلة مفصلة حول كيفية تثبيت Docker وتكوينه واستخدامه لمجموعة متنوعة من أنظمة التشغيل وحالات الاستخدام. موقع الويب أيضًا معلومات حول واجهات برمجة تطبيقات Docker وأوامر Docker CLI ونصائح حول استكشاف وحل المشكلات.
 
 تتضمن بعض الأقسام لوثائق Docker ما يلي:
 
 - [ابدأ مع Docker] (https://docs.docker.com/get-started/)
 - [مرجع Docker CLI] (https://docs.docker.com/engine/reference/commandline/cli/)
 - [مرجع Docker API] (https://docs.docker.com/engine/api/v1.41/)
 - [مرجع Docker-Compose] (https://docs.docker.com/compose/compose-file/)
 - [مرجع Dockerfile] (https://docs.docker.com/engine/reference/builder/)
 
 تعد وثائق مصدرًا مصدرًا رائعًا لتعلم كيفية استخدام Docker ولا تواجه مشكلة في مواجهة صعوبات.
 
 ### Docker Hub
 [Docker Hub] (https://hub.docker.com/) هو مستودع مستند إلى السحاب يتيح لك تخزين صور Docker ومشاركتها وإدارتها. Docker Hub المستودعات العامة والعاملة ، بالإضافة إلى إنشاء سير العمل ومهام العمل. يمكنك استخدام استخدام Docker Hub في صور Docker الخاصة بك ، وركبت على صور مسبقة الصنع لتطبيقات التطبيقات الشائعة.
 
 أو ما يلي:
 
 - [البحث عن صور عامل ميناء] (https://hub.docker.com/search؟type=image)
 - [تخزين وإدارة صور Docker في المستودعات] (https://hub.docker.com/repositories)
 - [أتمتةات والاختبار باستخدام مهام سير عمل Docker Hub] (https://docs.docker.com/docker-hub/builds/)
 
 Docker Hub هي أداة أساسية للعمل مع Docker ، ويمكن أن توفر الكثير من الوقت والجهد عندما يتعلق الأمر بالأمر ومساعدة صور Docker.
 
 
 ## خاتمة
 
 Docker هي أداة قوية يمكن أن تساعد في جعل تطبيقاتك أكثر قابلية للنقل وبدء التشغيل في النشر. أفضل الممارسات والنصائح ، يمكنك إنشاء حاويات آمنة الاستخدام وسريعة النشر. سواء كنت تنشئ إنشاءًا جديدًا أو تقوم بترحيل تطبيق موجود إلى Docker ، ستساعدك هذه الخطوات على البدء في إنشاء حاويات Docker.
 
