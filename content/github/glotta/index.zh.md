---
title: "雨果标记符文件翻译自动化脚本 - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta 是一款功能强大的命令行工具，可自动将雨果标记文件翻译成多种语言，让本地化变得轻而易举。"
tags: ["翻译自动化", "雨果标记", "本地化", "多语言内容", "命令行工具", "语言翻译", "语言本地化", "自动化脚本", "内容翻译", "多语言网站", "语言支持", "本地化工作流程", "翻译过程", "语言整合", "雨果静态网站生成器", "格洛塔", "语言文件", "翻译 API", "翻译提供商", "翻译服务", "语言管理", "多语种搜索引擎优化", "内容本地化", "网站全球化", "语言支持工具", "语言工作流程", "翻译效率", "定位效率", "自动翻译", "雨果多语言支持"]
---


## Glotta

将雨果标记文件内容翻译成其他语言的脚本。

#### 示例命令：

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### 输出示例：
```txt
========== glotta ============
dir: __fixtures__/simeon-usecase-dir/content/articles/a-beginners-guide-to-setting-up-a-secure-and-resilient-vpn-for-remote-workers
Input file(s):  [
  '__fixtures__/simeon-usecase-dir/content/articles/a-beginners-guide-to-setting-up-a-secure-and-resilient-vpn-for-remote-workers/index.en.md'
]
targetLanguageIds: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
force overwrite if file exists?: true
==============================

parsing input file...
translating text into...  es
writing new file...
translating text into...  ru
writing new file...
translating text into...  ro
writing new file...
translating text into...  pa
```

## 如何更改翻译 API 提供商

设置 `TRANSLATE_PROVIDER`环境变量为 `GOOGLE`或 `DEEPL`并确保设置您的 `DEEPL_AUTH_KEY`也是如此。
测试套件将依赖于这些环境变量，因此您可以通过运行 `npm test`

例如
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## 作者：

[1nf053c](https://github.com/1nf053c)

## Owner：

[simeononsecurity](https://github.com/simeononsecurity)

## 许可证

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
