---
title: "使用 Python 优化图像"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "使用 Python 调整图像尺寸、压缩图像并转换格式，通过可重复的 Pillow 流程完成优化。"
genre: ["技术", "Web 开发", "Python 编程", "图像优化", "SEO", "Web 性能", "用户体验", "软件开发", "自动化", "编程"]
tags: ["图像优化", "Python", "图像优化", "Web 开发", "网站性能", "用户体验", "压缩", "调整尺寸", "格式转换", "图像处理", "Pillow 库", "Tinify 库", "自动化", "Python 脚本", "Web 性能优化", "SEO 优化", "软件开发", "网页设计", "图像压缩", "减小文件大小", "延迟加载", "图像格式", "WebP 格式", "API 集成", "开发流程", "代码示例", "图像优化技术", "性能优化", "编程教程"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Python 脚本优化图像的插图，放大镜中显示一张压缩后的图像。"
coverCaption: "使用 Python 调整图像尺寸、压缩并优化图像。"
---

**简介**

图像文件大小会影响网站速度和访客体验。较大的图像文件会拖慢页面加载，也可能让访客离开。**Python** 和 Pillow 库能够缩小图像文件，并改善图像在网页中的显示。本文介绍使用 Python **优化图像**的实用方法和工具。

______

## 图像优化为何重要

**图像优化**是在不明显损害视觉质量的前提下降低文件大小。这样做有多项好处：

1. **页面加载更快**：较大的图像文件会拖慢网站，并影响 SEO 和用户体验。

2. **减少带宽消耗**：优化后的图像传输数据更少，网络条件有限的用户也更容易访问网站。

3. **改善移动端体验**：移动网络通常较慢。优化图像有助于页面在手机和平板上流畅显示。

4. **有助于 SEO**：搜索引擎会将网站速度纳入排名考量。加载更快的页面可能在搜索结果中获得更好的位置。

______

## 图像优化方法

### **1. 压缩图像**

压缩能够减小图像文件。Python 的 **Pillow** 库提供多种压缩算法和设置，便于在文件大小和图像质量之间取得平衡。使用 pip 安装 Pillow：

```python
pip install Pillow
```

压缩图像的示例：

```python
from PIL import Image

# 打开图像
image = Image.open("input_image.jpg")

# 压缩并保存图像
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. 调整图像尺寸**

根据图像在网站中的显示区域设置尺寸。即使用 HTML 或 CSS 缩小大图，浏览器仍会下载整个文件，因此页面可能依然变慢。Pillow 可直接调整图像尺寸：

```python
from PIL import Image

# 打开图像
image = Image.open("input_image.jpg")

# 调整图像大小
resized_image = image.resize((800, 600))

# 保存调整大小后的图像
resized_image.save("resized_image.jpg")
```

### **3. 转换图像格式**

转换为 WebP 等效率更高的格式，通常能在保持画质的同时减小文件。大多数现代浏览器都支持 WebP，Pillow 也能将图像保存为 WebP：

```python
from PIL import Image

# 打开图像
image = Image.open("input_image.jpg")

# 将图像转换为 WebP 格式
image.save("output_image.webp")
```

## 使用 Python 自动优化图像


### Python 脚本示例：使用 TinyPNG API

处理大量图像时，自动化能够节省时间和精力。Python 库可用于自动执行图像优化任务。Tinify 是 TinyPNG API 的 Python 封装。

Tinify 使用高级算法压缩和优化图像，在降低文件大小的同时保留画质。使用前，请在 Tinify 网站注册并获取 API 密钥。

使用 **Tinify** 压缩图像的示例：

```python
import tinify

# 使用 API 密钥配置 Tinify
tinify.key = "YOUR_API_KEY"

# 压缩图像
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Python 脚本示例：优化文件夹中的图像

下面的脚本处理 JPEG、PNG 等不同类型的图像，并导出优化后的 WebP 文件：

```python
import os
from PIL import Image

# 将图像转换为 WebP 格式的函数
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# 遍历文件夹中的图像并将其转换为 WebP 的函数
def optimize_images(folder_path, output_folder, quality=85):
    # 如果输出文件夹不存在，则创建它
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历文件夹中的每个文件
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # 构建输入和输出路径
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # 将图像转换为 WebP 格式
            convert_to_webp(input_path, output_path, quality=quality)

# 用法示例
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

此示例使用 Python Imaging Library (PIL) 打开图像并将其转换为 WebP。`convert_to_webp` 函数接收输入路径、输出路径和可选的质量参数，默认值为 85。`optimize_images` 函数遍历文件夹中的文件，检查文件扩展名是否符合条件，然后调用 `convert_to_webp`。优化后的 WebP 图像会保存到指定的输出文件夹。

根据需要调整 `folder_path`、`output_folder` 和 `quality` 的值。

## 结论

图像优化能够加快网站速度、改善用户体验，并提升页面在搜索结果中的表现。Python 生态提供了压缩图像、调整尺寸、转换格式和自动执行这些任务的工具。Pillow 和 Tinify 能够处理单张图像或一批图像，同时维持适用的视觉质量。先确定合适的尺寸和质量，再将这些设置应用到工作流程中。


## 参考资料
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
