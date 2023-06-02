---
title: "Hugo Markdownファイル用翻訳自動化スクリプト - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glottaは、Hugoのマークダウンファイルの多言語への翻訳を自動化し、ローカライズを容易にする強力なコマンドラインツールです。"
tags: ["トランスレーションオートメーション", "ヒューゴマークダウン", "ローカライズ", "多言語コンテンツ", "コマンドラインツール", "言語翻訳", "言語ローカライズ", "オートメーションスクリプト", "内容翻訳", "多言語ウェブサイト", "言語サポート", "ローカライゼーションワークフロー", "翻訳プロセス", "言語統合", "Hugo静的サイトジェネレーター", "グロッタ", "言語ファイル", "翻訳API", "翻訳業者", "翻訳サービス", "言語運用", "多言語SEO", "コンテンツローカライゼーション", "ウェブサイトのグローバル化", "言語支援ツール", "言語ワークフロー", "翻訳効率", "ローカライズ効率", "機械翻訳", "ヒューゴの多言語対応"]
---


## Glotta

Hugoのマークダウンファイルの内容を他言語に翻訳するスクリプトです。

#### コマンドの例

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### 出力例です：
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

## Translation API Providerを変更する方法

を設定します。 `TRANSLATE_PROVIDER`のどちらかに環境変数を設定します。 `GOOGLE`または `DEEPL`を必ずセットしてください。 `DEEPL_AUTH_KEY`と同じです。
テストスイートはこれらのenv変数に依存しているので、以下を実行して統合をテストすることができます。 `npm test`

例えば、こんな感じです：
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Author：

[1nf053c](https://github.com/1nf053c)

## オーナーです：

[simeononsecurity](https://github.com/simeononsecurity)

#ライセンス

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
