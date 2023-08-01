---
title: "Сегодня я узнала, как создать шоколадную упаковку"
date: 2022-05-23
toc: true
draft: false
description: "Сегодня я узнал больше об условных сигналах Ansible и управлении переменными"
genre: ["Автоматизация", "Управление пакетами Windows", "Создание пакета", "Управление пакетами", "Инфраструктура как код (IaC)", "Развертывание программного обеспечения Windows", "Упаковка программного обеспечения", "Автоматизация Windows", "Репозитории пакетов", "Инструменты Windows"]
tags: ["автоматизация", "Powershell", "Менеджер шоколадных пакетов", "Шоколад", "Choco", "создание пакета", "автоматизация упаковки", "Nuspec", "Nethor", "Менеджеры пакетов Windows", "МАК", "Инфраструктура как код", "Развертывание программного обеспечения Windows", "упаковка программного обеспечения", "управление репозиторием", "совместное использование пакетов", "Шоколадная документация", "учебное пособие", "публикация пакетов"]
---

**Что интересного узнал и нашел сегодня SimeonOnSecurity**.

Сегодня SimeonOnSecurity познакомился с процессом создания пакетов для менеджера пакетов Chocolatey. Chocolatey - это менеджер пакетов для Windows, который позволяет легко устанавливать, обновлять и управлять приложениями и инструментами. Создавая пакеты, SimeonOnSecurity может автоматизировать установку программ и делиться пакетами с другими участниками сообщества.

SimeonOnSecurity создал и обновил на GitHub два репозитория, связанных с созданием пакетов Chocolatey. Первый репозиторий, simeononsecurity/Chocolatey-Nethor, представляет собой пакет для Nethor. Второй репозиторий, simeononsecurity/chocolateypackages, представляет собой коллекцию пакетов, созданных SimeonOnSecurity для различных приложений и инструментов.

Для создания пакета SimeonOnSecurity использовал формат файла Nuspec, который предоставляет метаданные о пакете и его содержимом. В процессе создания пакета также использовались такие функции, как Install-ChocolateyInstallPackage и Install-ChocolateyPackage, для указания устанавливаемого программного обеспечения и всех необходимых зависимостей.

Для более глубокого понимания процесса создания и публикации пакетов Chocolatey SimeonOnSecurity также просмотрел несколько учебных ресурсов, включая официальную документацию по Chocolatey и учебное пособие от Top Bug Net.

В целом, сегодняшний опыт обучения позволил SimeonOnSecurity получить полное представление о процессе создания пакетов для менеджера пакетов Chocolatey, что облегчает автоматизацию установки программ и обмен пакетами с другими участниками сообщества.

## Repos Created/Updated:
- [simeononsecurity/Chocolatey-Nethor](https://github.com/simeononsecurity/Chocolatey-Nethor)
- [simeononsecurity/chocolateypackages](https://github.com/simeononsecurity/chocolateypackages)

## Учебные ресурсы:
- [Chocolatey - Create Packages](https://docs.chocolatey.org/en-us/create/create-packages#nuspec)
- [Chocolatey - Install-ChocolateyInstallPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateyinstallpackage)
- [Chocolatey - Install-ChocolateyPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateypackage)
- [Top Bug Net - Create and Publish Chocolatey Packages](https://www.topbug.net/blog/2012/07/02/a-simple-tutorial-create-and-publish-chocolatey-packages/)