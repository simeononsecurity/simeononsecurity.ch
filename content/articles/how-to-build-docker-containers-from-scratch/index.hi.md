---
title: "Building Efficient and Secure Docker Containers: A Guide for Beginners"
date: 2023-02-24
toc: true
draft: false
description: "Learn how to create efficient and secure Docker containers using best practices, tips, and step-by-step instructions in this comprehensive guide."
tags: ["docker", "containers", "containerization", "devops", "deployment", "portability", "efficiency", "security", "best practices", "Dockerfile", "base images", "environment variables", "volume mounts", "root user", "up-to-date images", "software development", "container images", "Docker Hub", "container orchestration", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.png"
coverAlt: "A 3D animated image of a secure, well-organized container with the Docker logo on it, surrounded by various tools and equipment related to software engineering and DevOps."
coverCaption: ""
---
```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```
```bash
docker run -d -p 80:80 my-nginx-image
```
```dockerfile
RUN apt update 
RUN apt install apache -y
```
```dockerfile
RUN apt update && apt install apache -y
```
```bash
docker run -e PORT=3000 my-app
```
```Dockerfile
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and yarn.lock to the container
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the application code to the container
COPY . .

# Expose the application port
EXPOSE $PORT

# Start the application
CMD ["yarn", "start"]
```
```bash
docker run -v /home/user/app/data:/app/data my-app
```
```Dockerfile
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the package.json and yarn.lock files to the container
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the rest of the application code to the container
COPY . .

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["yarn", "start"]

# Mount a volume for the application data
VOLUME ["/app/data"]
```
```Dockerfile
FROM node:14

# Create a new user to run the container
RUN useradd --user-group --create-home --shell /bin/false app

# Change the working directory to the app user's home directory
WORKDIR /home/app

# Install dependencies as the app user
COPY package.json yarn.lock ./
RUN chown -R app:app /home/app
USER app
RUN yarn install --frozen-lockfile --production

# Copy the application code as the app user
COPY --chown=app:app . .

# Expose the port
EXPOSE 3000

# Start the application as the app user
CMD ["yarn", "start"]
```
```Dockerfile
FROM ubuntu:latest

# Update the package list and install security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install the nginx web server
RUN apt-get install -y nginx

# Copy the application code to the container
COPY . /var/www/html/

# Expose port 80 to the host system
EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]

```

  **डॉकर कंटेनर कैसे बनाएं** डॉकर एक शक्तिशाली उपकरण है जिसका उपयोग पोर्टेबल और आसानी से परिनियोजन योग्य ऐप बनाने के लिए किया जा सकता है। इस गाइड में, हम डॉकटर कंटेनर बनाने और रूपरेखाओं को कवर करने के लिए तैयार करेंगे। हम यह सुनिश्चित करने के लिए कुछ व्यावहारिक और अटकल पर भी जा सकते हैं कि आपका डॉकटर कंटेनर कुशल, सुरक्षित और उपयोग में आसान है। ## डॉकटर को चुनें इससे पहले कि हम डॉकटर कंटेनर बनाना शुरू करें, यह महत्वपूर्ण है कि डॉकर क्या है और यह कैसे काम करता है। डॉकर एक उपकरण है जो आपको एक ऐप और उसके लिंक को एक कंटेनर में पैकेज करने की अनुमति देता है जो किसी भी सिस्टम पर चल सकता है। कंटेनर को होस्ट सिस्टम से अलग किया जाता है और इसमें कोड, ब्लॉक सिस्टम, लाइब्रेरी और रिकॉर्डिंग सहित चैनल को चलाने के लिए कुछ शामिल करने की आवश्यकता है। क्लोजर लॉक होते हैं और रुक जाते हैं, जिससे वे मियाद हो जाते हैं और फिर से शुरू होने के लिए एक लोकप्रिय विकल्प बन जाते हैं। डॉकर के साथ, आप सरल कमांड-लाइन साथी के साथ कंटेनर बना सकते हैं, आपका कर सकते हैं और चला सकते हैं। ## एक डॉकटर इमेज का निर्माण डॉकटर कंटेनर बनाने के लिए आपको सबसे पहले डॉकर इमेज बनाने की जरूरत है। एक डॉकटर इमेज एक कंटेनर का एक ऐसा है जिसमें किसी को चलाने के लिए आवश्यक सभी फाइल्स, लाइब्रेरी और अटैचमेंट शामिल हैं। डॉकटर इमेज बनाने के लिए यहां दिए गए कदम दिए गए हैं: 1. **डॉकरफाइल बनाएं** 2. **इमेज मेकिंग** 3. **कंटेनर प्ले** ### चरण 1: एक डॉकर फाइल बनाएं डॉकर इमेज बनाने के लिए पहला कदम डॉकरफाइल बनाना है। Dockerfile एक टेक्स्ट फ़ाइल है जिसमें इमेज बनाने के लिए निर्देश दिए जाने चाहिए। यहाँ एक सामान्य दस्तावेज़ का उदाहरण दिया गया है: आइए इस डॉकरफ़ाइल को तोड़ दें: - `उबंटू से: आधुनिक कंटेनर के लिए उपयोग करने के लिए रूटिंग छवि निर्दिष्ट करता है। इस स्थिति में, हम Ubuntu के नवीनतम संस्करण का उपयोग कर रहे हैं। - `RUN apt-get update && apt-get install -y nginx` पैकेज सूची को अपडेट करता है और nginx वेब सर्वर को स्थापित करता है। - `कॉपी index.html /var/www/html/` index.html फ़ाइल को कंटेनर के वेब रूट पर कॉपी करता है। - `EXPOSE 80` पोर्ट 80 को होस्ट सिस्टम के सामने उजागर करता है। - `CMD ["nginx", "-g", "Deman of;"] nginx सर्वर शुरू करता है और इसे अग्रभूमि में चलाता है। ### चरण 2: छवि निर्माण करें डॉकरफाइल बनाने के बाद, आप `डॉकर बिल्ड` कमांड का उपयोग करके छवि बना सकते हैं। यहाँ एक उदाहरण है: आइए इस आदेश को तोड़ दें: - `डॉकर रन` डॉकटर को एक कंटेनर लाइव के लिए स्टेटस है। - `-d` कंटेनर को अलग-अलग मोड में रखता है, जिसका अर्थ है कि बैकअप में रहता है। - `-p 80:80` होस्ट सिस्टम पर पोर्ट 80 को कंटेनर में पोर्ट 80 पर आता है। - `my-nginx-image` कंटेनर के लिए उपयोग करने के लिए डॉकर छवि का नाम निर्दिष्ट करता है। ##सर्वोत्तम परंपराएं अब जब आप जानते हैं कि डॉकर कंटेनर बनाए जाते हैं, तो यह सुनिश्चित करने के लिए कि आपका डॉकटर कंटेनर कुशल, सुरक्षित और उपयोग में आसान है, कुछ घंटों पर ध्यान दें। ### कार्यक्षेत्र का उपयोग करें अपने चलने वाले डॉकटर कंटेनर को छोटा और तुरंत लगाने के लिए, छोटे का उपयोग करना सबसे अच्छा है, जिसमें केवल आपके आवेदन की पहचान शामिल है। उदाहरण के लिए, सौ या सेंटोस जैसे पूर्ण विकसित ऑपरेटिंग सिस्टम का उपयोग करने के बजाय, आप अल्पाइन लिंक या बिजीबॉक्स जैसी छोटी छवि का उपयोग कर सकते हैं। ###सकी कम करें आपका डॉकर फ़ाइल की प्रत्येक पंक्ति आपकी डॉकर छवि में एक नई परत बनाती है, और प्रत्येक परत छवि के आकार में जुड़ जाती है। अपने डॉकर को आप में छोटा रखने के लिए, आपको अपनी छवि में परतों की संख्या को कम करने का प्रयास करना चाहिए। ऐसा करने का एक तरीका यह है कि आप अपने Dockerfile में समान कमांड को एक साथ एक लाइन में समूहित करें। उदाहरण के लिए, पैकेज सूची को अपडेट करने और पैकेज बनाने के लिए दो अलग `रन` कमांड का उपयोग करने के बजाय, आप एक ही समय में दोनों करने के लिए एक `रन` कमांड का उपयोग कर सकते हैं। पूर्व: वि ### पर्यावरण चर का प्रयोग करें हार्डकोडिंग धारणा के बजाय आपके डॉकर आने में पर्यावरण चर का उपयोग करना आपके कंटेनर को पहचानना आसान बनाता है और यह सुनिश्चित करता है कि आपका डॉकर ऐक्सेस पोर्टेबल है। उदाहरण के लिए, आप पर्यावरण चर का उपयोग उस पोर्ट को निर्दिष्ट करने के लिए कर सकते हैं जिस पर आपका ऐप चलता है या पाठ का क्षेत्र। पूर्व: ###वालुम पर्वत का उपयोग करें वॉल्यूम आपके होस्ट सिस्टम और आपके डॉकर कंटेनर के बीच डेटा साझा करने का एक तरीका है। इससे डेटा आपका आसान हो जाता है और आपके डॉकटर कंटेनर के आकार कम हो जाते हैं। उदाहरण के लिए, आप अपने होस्ट सिस्टम और अपने कंटेनर के बीच डेटाबेस फ़ाइल साझा करने के लिए वॉल्यूम माउंट का उपयोग कर सकते हैं। पूर्व: ### जड़ के रूप में लाइक्स से बचें आपका डॉकटर कंटेनर उपयोगकर्ता रूट के रूप में जोखिम जोखिम में शामिल हो सकता है। इसके बजाय, आपको अपनी डॉकरफाइल में एक नया उपयोगकर्ता बनाना चाहिए और उस उपयोगकर्ता के रूप में कंटेनर बनाना चाहिए। उदाहरण के लिए, आप एक नया प्रयोक्ता बनाने के लिए अपने डॉकरफाइल में `USER` कमांड का उपयोग कर सकते हैं और फिर क्लोजर रन टाइम उस उपयोगकर्ता पर स्विच कर सकते हैं। पूर्व: ### निवेश को अपडेट करें यह सुनिश्चित करने के लिए कि आपका डॉकटर कंटेनर सुरक्षित है और कमजोरियों से मुक्त है, यह महत्वपूर्ण है कि आप अपने डॉकटर कंटेनर को सूचित करते रहें। इसका मतलब यह है कि नियमित रूप से आधार वाली इमेज और किसी अटैचमेंट को अपडेट करने पर आपका आवेदन समाप्त हो जाता है। उदाहरण के लिए, आप अपने कंटेनर को नवीनतम सुरक्षा पैच और बग फिक्स के साथ अपडेट रखने के लिए अपने Dockerfile में `apt-get update` और` apt-get upgrade` कमांड का उपयोग कर सकते हैं। पूर्व: ## आगे अपने अध्ययन ### दस्तावेज़ीकरण [Docker](https://www.docker.com/) कंटेनर में पहेली बनाने, बनाने और सीखने के लिए एक ओपन- आईटी प्लैटैट फॉर्म है। डॉकर निष्कर्ष वेबसाइट विभिन्न प्रकार के ऑपरेटिंग सिस्टम और उपयोग के मामलों के लिए डॉकर को स्थापित करने, व्यंजक करने और उपयोग करने के बारे में विस्तृत जानकारी प्रदान करती है। वेबसाइट में डॉकटर डॉकटर, डॉकटर सीएलआई कमांड और ब्रीचिंग की समस्या को रोकने वाली जानकारी भी शामिल है। डॉकर निष्कर्ष के कुछ उपयोगी संक्षिप्तीकरण में शामिल हैं: - [डॉकर के साथ शुरुआत करें](https://docs.docker.com/get-started/) - [डॉकर सीएलआई संदर्भ] (https://docs.docker.com) /engine/reference/commandline/cli/) - [डॉकर अनुक्रमण संदर्भ] (https://docs.docker.com/engine/api/v1.41/) - [डॉकर-रचना संदर्भ] (https://docs. docker.com/compose/compose-file/) - [डॉकरफाइल संदर्भ] (https://docs.docker.com/engine/reference/builder/) डॉकर का उपयोग करने का तरीका सीखें और आपके सामने आने वाले किसी भी समस्या के लिए रोकथाम के लिए डॉकर निष्कर्ष एक बेहतरीन संसाधन है। ### डॉकर हब [डॉकर हब](https://hub.docker.com/) एक क्लाउड-आधारित रिपॉजिटरी है जो आपको डॉकर एक्सपोजर को स्टोर करने, साझा करने और आपकी अनुमति देता है। डॉकर हब में सार्वजनिक और निजी रिपॉजिटरी के साथ-साथ स्वचालित बिल और फाइलिंग शामिल हैं। आप डॉकर हब का उपयोग अपने स्वयं के डॉकर कार्यों को आर्काइव करने के साथ-साथ लोकप्रिय टैग और टूल के लिए पूर्व-निर्मित पृष्ठों को देखने के लिए कर सकते हैं। डॉकर हब की कुछ क्रियात्मक बातों में शामिल हैं: - [डॉक्टर निवेश के लिए शेयर](https://hub.docker.com/search?type=image) - [रिपॉजिटरी में डॉकर निवेश को स्टोर करें और अपना](https: //hub.docker.com/repositories) - [डॉकर हब झटके के साथ स्वचालित निर्माण और परीक्षण] (https://docs.docker.com/docker-hub/builds/) डॉकर के साथ काम करने के लिए डॉकर हब एक आवश्यक उपकरण है, और जब डॉकर पाठ्यक्रमों को आपके करने और साझा करने की बात आती है तो यह आपका बहुत समय और प्रयास बचा सकता है। ## निष्कर्ष डॉकर एक शक्तिशाली उपकरण है जो आपके विज़न को अधिक पोर्टेबल, कुशल और स्थिर करने में आसान बनाने में मदद कर सकता है। इन प्रामाणिक और स्टेक पालन करके, आप डॉकर कंटेनर बना सकते हैं जो सुरक्षित, उपयोग में आसान और तेजी से रुके जा सकते हैं।चाहे आप एक नया अपना बना रहे हों या किसी मौजूदा एक को डॉकर में माइग्रेट कर रहे हों, ये कदम आपको डॉकटर कंटेनर बनाने में मदद करेगा।