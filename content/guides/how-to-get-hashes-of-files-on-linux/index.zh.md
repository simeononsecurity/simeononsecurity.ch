---
title: "Linux 文件哈希值：使用内置工具获取 SHA256、MD5 和 SHA1 哈希值的指南"
draft: false
toc: true
date: 2023-05-25
description: "了解如何使用内置工具在 Linux 上获取文件的 SHA256、MD5 和 SHA1 哈希值，确保数据完整性和文件真实性。"
tags: ["Linux 文件哈希值", "SHA256 哈希值", "MD5 哈希值", "SHA1 哈希值", "Linux 命令行", "文件完整性", "数据验证", "Linux 安全", "内置工具", "文件验证", "数据真实性", "文件散列算法", "Linux 系统管理", "命令行工具", "文件校验和", "Linux 实用工具", "文件完整性检查", "数据完整性验证", "文件散列示例", "Linux 哈希命令", "文件散列方法", "Linux 安全措施", "Linux 数据保护", "Linux 文件管理", "Linux 文件验证", "Linux 文件完整性", "数据安全", "Linux 数据验证", "Linux 系统安全", "文件散列技术", "文件完整性保证", "安全文件验证", "Linux 数据完整性"]
cover: "/img/cover/A_digital_representation_of_file_hashes_being_calculated.png"
coverAlt: "Linux 终端屏幕上正在计算文件哈希值的数字表示，象征着数据的完整性和安全性。"
coverCaption: ""
---

**指南：使用内置工具获取 Linux 上文件的哈希值**

## 简介

在 Linux 系统中，获取文件哈希值对于确保数据完整性和验证文件真实性至关重要。文件哈希值作为唯一标识符，允许用户检测篡改企图并验证数据完整性。在本综合指南中，我们将探讨如何使用内置工具获取 Linux 上文件的 **SHA256**、**MD5** 和 **SHA1** 哈希值。请按照逐步说明，通过具体示例进行学习。

______

## 使用内置工具在 Linux 上获取哈希值

Linux 提供了多种内置工具，用户无需安装其他软件即可计算文件哈希值。我们将探讨三种广泛使用的哈希算法：**SHA256**、**MD5** 和 **SHA1**。

### 获取 SHA256 哈希值

要在 Linux 上获取文件的**SHA256 哈希值**，可以使用 `sha256sum`命令。打开终端并导航到文件所在的目录。然后执行以下命令：

```bash
sha256sum file_path
```
更换 `file_path`文件的实际路径。

### 获取 MD5 和 SHA1 哈希值
您还可以获取 `MD5`和 `SHA1 hashes`在 Linux 系统上，使用类似的命令可以查看文件的内容：

- 要获取 `MD5 hash`

```bash
md5sum file_path
```

- 要获得 `SHA1 hash`

```bash
sha1sum file_path
```
更换 `file_path`这两条命令中都包含文件路径。

## 示例
让我们以具体实例来说明使用 Linux 内置工具获取哈希值的过程。

{{< youtube id="3aX9zK88X9M" >}}

#### 示例 1：获取 SHA256 哈希值
假设您有一个名为 `document.pdf`目录中的 `/home/user/docs`要获得 `SHA256 hash`在 Linux 上，执行以下命令即可获得该文件：

```bash
sha256sum /home/user/docs/document.pdf
```

输出将显示 `SHA256 hash`文件的值。

### 示例 2：获取 MD5 哈希值

假设有一个名为 `image.jpg`目录中存储的 `/home/user/pictures`要获得 `MD5 hash`在 Linux 上，运行以下命令即可获取该文件：

```bash
md5sum /home/user/pictures/image.jpg
```

终端将显示 `MD5 hash`文件的值。

## 示例 3：获取 SHA1 哈希值

假设有一个名为 `data.txt`目录中的 `/home/user/files`要获得 `SHA1 hash`在 Linux 上，执行以下命令即可获得该文件：

```bash
sha1sum /home/user/files/data.txt
```
输出将显示 `SHA1 hash`文件的值。

## 结论
在 Linux 上使用内置工具获取文件哈希值是确保数据完整性和验证文件真实性的一种简单而强大的方法。按照本指南中提供的说明，你就可以在 Linux 系统上自信地计算文件的 SHA256、MD5 和 SHA1 哈希值。

## 参考资料

1. [sha256sum - Linux man page](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - Linux man page](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - Linux man page](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
