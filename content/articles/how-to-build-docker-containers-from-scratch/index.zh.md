---
title: "构建高效且安全的 Docker 容器"
date: 2023-02-24
lastmod: 2026-11-27
toc: true
draft: false
description: "本指南通过最佳实践、实用建议和分步说明，帮助你构建高效、安全的 Docker 容器。"
tags: ["Docker", "容器", "容器化", "DevOps", "部署", "可移植性", "效率", "安全", "最佳实践", "Dockerfile", "基础镜像", "环境变量", "卷挂载", "root 用户", "更新后的镜像", "软件开发", "容器镜像", "Docker Hub", "容器编排", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.webp"
coverAlt: "一幅 3D 动画图，展示带有 Docker 标志、布局整齐且安全的容器，周围摆放着与软件工程和 DevOps 相关的工具和设备。"
coverCaption: ""
---

**如何构建 Docker 容器**

Docker 是一款功能强大的工具，可用于创建易于移植和部署的应用程序。本指南介绍创建和构建 Docker 容器的基本步骤，也会说明一些最佳实践和建议，帮助你打造高效、安全且易于使用的 Docker 容器。

## 了解 Docker

开始构建 Docker 容器之前，先了解 Docker 是什么以及它如何工作。

Docker 可以将应用程序及其依赖项打包到一个容器中，并在任何系统上运行。容器与宿主系统隔离，其中包含运行应用程序所需的一切，包括代码、运行时、系统工具、库和设置。

容器轻量且易于部署，因此常用于构建和部署应用程序。借助 Docker，你可以通过简单的命令行界面创建、管理和运行容器。

## 构建 Docker 镜像

要构建 Docker 容器，首先需要创建 Docker 镜像。Docker 镜像是容器的一个快照，其中包含运行应用程序所需的全部文件、库和依赖项。

创建 Docker 镜像的基本步骤如下：

1. **创建 Dockerfile**
2. **构建镜像**
3. **运行容器**

### 步骤 1：创建 Dockerfile

构建 Docker 镜像的第一步是创建 Dockerfile。Dockerfile 是包含镜像构建指令的文本文件。下面是一个简单的 Dockerfile 示例：

```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

下面逐项说明这个 Dockerfile：

- `FROM ubuntu:latest` 指定容器使用的基础镜像。本例使用 Ubuntu 的最新版本。
- `RUN apt-get update && apt-get install -y nginx` 更新软件包列表并安装 nginx Web 服务器。
- `COPY index.html /var/www/html/` 将 index.html 文件复制到容器的 Web 根目录。
- `EXPOSE 80` 将 80 端口声明为供宿主系统访问。
- `CMD ["nginx", "-g", "daemon off;"]` 启动 nginx 服务器并让它在前台运行。

### 步骤 2：构建镜像

创建 Dockerfile 后，可以使用 `docker build` 命令构建镜像。示例如下：

```bash
docker run -d -p 80:80 my-nginx-image
```

下面说明这个命令：

- `docker run` 告诉 Docker 启动一个容器。
- `-d` 以分离模式运行容器，也就是在后台运行。
- `-p 80:80` 将宿主系统的 80 端口映射到容器内的 80 端口。
- `my-nginx-image` 指定容器要使用的 Docker 镜像名称。

## 最佳实践

了解如何构建 Docker 容器后，下面介绍一些最佳实践，帮助你保持容器高效、安全且易于使用。

### 使用较小的基础镜像

要让 Docker 容器体积小、部署快，最好选择只包含应用程序所需依赖项的较小基础镜像。例如，与 Ubuntu 或 CentOS 等完整操作系统相比，可以使用 Alpine Linux 或 BusyBox 等较小的镜像。

### 减少镜像层数

Dockerfile 中的每一行都会在 Docker 镜像中创建一个新层，每一层都会增加镜像体积。为了尽可能缩小 Docker 镜像，应尽量减少层数。一种做法是在 Dockerfile 中将相似的命令合并到同一行。例如，更新软件包列表和安装软件包时，可以用一个 `RUN` 命令完成，而不是使用两个单独的 `RUN` 命令。

例如：
```dockerfile
RUN apt update
RUN apt install apache -y
```
而不是
```dockerfile
RUN apt update && apt install apache -y
```

### 使用环境变量

在 Dockerfile 中使用环境变量，而不是把值写死，可以更方便地在运行时自定义容器，并让 Dockerfile 更具可移植性。例如，可以使用环境变量指定应用程序运行的端口或配置文件的位置。

例如：
```bash
docker run -e PORT=3000 my-app
```
```Dockerfile
FROM node:14

# 设置工作目录
WORKDIR /app

# 将 package.json 和 yarn.lock 复制到容器
COPY package.json yarn.lock ./

# 安装依赖项
RUN yarn install --frozen-lockfile

# 将应用程序代码复制到容器
COPY . .

# 声明应用程序端口
EXPOSE $PORT

# 启动应用程序
CMD ["yarn", "start"]
```


### 使用卷挂载

卷挂载可以在宿主系统和 Docker 容器之间共享数据。这有助于管理数据，也能减小 Docker 容器的体积。例如，可以挂载一个卷，在宿主系统和容器之间共享数据库文件。

例如：
```bash
docker run -v /home/user/app/data:/app/data my-app
```

```Dockerfile
FROM node:14

# 设置工作目录
WORKDIR /app

# 将 package.json 和 yarn.lock 文件复制到容器
COPY package.json yarn.lock ./

# 安装依赖项
RUN yarn install --frozen-lockfile

# 将应用程序的其余代码复制到容器
COPY . .

# 声明应用程序端口
EXPOSE 3000

# 启动应用程序
CMD ["yarn", "start"]

# 为应用程序数据挂载卷
VOLUME ["/app/data"]
```

### 避免以 root 身份运行

以 root 用户身份运行 Docker 容器可能带来安全风险。应在 Dockerfile 中创建一个新用户，并使用该用户运行容器。例如，可以在 Dockerfile 中使用 `USER` 指令创建新用户，然后在启动容器时切换到该用户。

例如：
```Dockerfile
FROM node:14

# 创建一个用于运行容器的新用户
RUN useradd --user-group --create-home --shell /bin/false app

# 将工作目录切换到 app 用户的主目录
WORKDIR /home/app

# 以 app 用户身份安装依赖项
COPY package.json yarn.lock ./
RUN chown -R app:app /home/app
USER app
RUN yarn install --frozen-lockfile --production

# 以 app 用户身份复制应用程序代码
COPY --chown=app:app . .

# 声明端口
EXPOSE 3000

# 以 app 用户身份启动应用程序
CMD ["yarn", "start"]
```

### 保持镜像更新

为了确保 Docker 容器安全且不含已知漏洞，应及时更新 Docker 镜像。这意味着定期更新基础镜像以及应用程序依赖项。例如，可以在 Dockerfile 中使用 `apt-get update` 和 `apt-get upgrade` 命令，让容器获得最新的安全补丁和错误修复。

例如：
```Dockerfile
FROM ubuntu:latest

# 更新软件包列表并安装安全更新
RUN apt-get update && apt-get upgrade -y && apt-get clean

# 安装 nginx Web 服务器
RUN apt-get install -y nginx

# 将应用程序代码复制到容器
COPY . /var/www/html/

# 向宿主系统声明 80 端口
EXPOSE 80

# 启动 nginx 服务器
CMD ["nginx", "-g", "daemon off;"]

```
## 继续学习
### Docker 文档
[Docker](https://www.docker.com/) 是一个开源平台，用于构建、交付和运行容器化应用程序。Docker 文档网站详细介绍了如何在各种操作系统和使用场景中安装、配置和使用 Docker。网站还提供 Docker API、Docker CLI 命令和故障排查方面的信息。

Docker 文档中的一些实用章节包括：

- [开始使用 Docker](https://docs.docker.com/get-started/)
- [Docker CLI 参考](https://docs.docker.com/engine/reference/commandline/cli/)
- [Docker API 参考](https://docs.docker.com/engine/api/v1.41/)
- [Docker Compose 参考](https://docs.docker.com/compose/compose-file/)
- [Dockerfile 参考](https://docs.docker.com/engine/reference/builder/)

Docker 文档是学习 Docker 用法以及排查问题的实用资源。

### Docker Hub

[Docker Hub](https://hub.docker.com/) 是一个基于云的仓库，可用于存储、共享和管理 Docker 镜像。它提供公共和私有仓库，以及自动构建和工作流。你可以在 Docker Hub 中存储自己的 Docker 镜像，也可以查找热门软件应用程序和工具的预构建镜像。

Docker Hub 的一些实用功能包括：

- [搜索 Docker 镜像](https://hub.docker.com/search?type=image)
- [在仓库中存储和管理镜像](https://hub.docker.com/repositories)
- [使用 Docker Hub 工作流自动执行构建和测试](https://docs.docker.com/docker-hub/builds/)

Docker Hub 是使用 Docker 的重要工具，在管理和共享镜像时可以节省大量时间和精力。

## 结论

Docker 是一款强大的工具，可以让应用程序更易移植、更高效，也更容易部署。遵循这些最佳实践和建议，你可以构建安全、易用且部署迅速的 Docker 容器。无论是构建新应用程序，还是将现有应用程序迁移到 Docker，这些步骤都能帮助你开始构建 Docker 容器。
