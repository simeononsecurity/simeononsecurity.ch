---
title: "Pythonで画像を最適化する"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Pythonで画像をリサイズ、圧縮、形式変換し、Pillowを使った再現可能な処理手順を構築します。"
genre: ["テクノロジー", "ウェブ開発", "Pythonプログラミング", "画像最適化", "SEO", "ウェブパフォーマンス", "ユーザー体験", "ソフトウェア開発", "自動化", "プログラミング"]
tags: ["画像最適化", "Python", "画像の最適化", "ウェブ開発", "サイトのパフォーマンス", "ユーザー体験", "圧縮", "リサイズ", "形式変換", "画像処理", "Pillowライブラリ", "Tinifyライブラリ", "自動化", "Pythonスクリプト", "ウェブパフォーマンス最適化", "SEO最適化", "ソフトウェア開発", "ウェブデザイン", "画像圧縮", "ファイルサイズ削減", "遅延読み込み", "画像形式", "WebP形式", "API連携", "開発ワークフロー", "コード例", "画像最適化の手法", "パフォーマンス最適化", "プログラミングチュートリアル"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Pythonスクリプトで画像を最適化するイラスト。拡大鏡に圧縮後の画像が映っている。"
coverCaption: "Pythonで画像をリサイズ、圧縮し、改善する。"
---

**はじめに**

画像のファイルサイズは、ウェブサイトの表示速度と訪問者の使いやすさに影響します。大きな画像はページの読み込みを遅らせ、訪問者がページを離れる原因になります。**Python**とPillowを使うと画像ファイルを小さくし、ウェブでの表示を改善できます。この記事では、Pythonで**画像を最適化する**方法とツールを紹介します。

______

## 画像の最適化が重要な理由

画像の見た目を保ちながらファイルサイズを小さくする処理が**画像最適化**です。主な利点は次のとおりです。

1. **ページの読み込みが速くなる**: 大きな画像ファイルはサイトを遅くし、SEOとユーザー体験に影響します。

2. **通信量を減らせる**: 最適化した画像は転送データが少なく、通信量に制限のある環境からもサイトを利用しやすくなります。

3. **モバイルで表示しやすい**: モバイル回線は遅い場合があります。画像を最適化すると、スマートフォンやタブレットでページを滑らかに表示できます。

4. **SEOを支援する**: 検索エンジンは順位付けでサイトの速度を考慮します。読み込みの速いページは検索結果で上位に表示される可能性があります。

______

## 画像を最適化する方法

### **1. 画像を圧縮する**

圧縮すると画像ファイルのサイズを小さくできます。Pythonの**Pillow**には複数の圧縮方法と設定があり、ファイルサイズと画質のバランスを調整できます。pipでPillowをインストールします。

```python
pip install Pillow
```

画像を圧縮するコード例です。

```python
from PIL import Image

# 画像を開く
image = Image.open("input_image.jpg")

# 画像を圧縮して保存
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. 画像をリサイズする**

サイト上で表示する領域に合わせて画像の寸法を調整します。HTMLやCSSで大きな画像を小さく表示しても、ブラウザーは元ファイル全体をダウンロードするため、表示が遅くなる場合があります。Pillowなら画像を簡単にリサイズできます。

```python
from PIL import Image

# 画像を開く
image = Image.open("input_image.jpg")

# 画像のサイズを変更
resized_image = image.resize((800, 600))

# サイズ変更した画像を保存
resized_image.save("resized_image.jpg")
```

### **3. 画像形式を変換する**

WebPのような効率的な形式へ変換すると、画質を保ちながらファイルサイズを減らせます。現在の多くのブラウザーはWebPに対応しており、PillowからWebP形式で保存できます。

```python
from PIL import Image

# 画像を開く
image = Image.open("input_image.jpg")

# 画像を WebP 形式に変換
image.save("output_image.webp")
```

## Pythonで画像最適化を自動化する


### Pythonスクリプト例: TinyPNG APIを使う

多数の画像を扱う場合、自動化すると時間と作業量を減らせます。Pythonのライブラリを使って画像最適化を自動化できます。TinifyはTinyPNG API用のPythonラッパーです。

Tinifyは高度なアルゴリズムで画像を圧縮し、画質を保ちながらファイルサイズを減らします。利用するにはTinifyのサイトで登録し、APIキーを取得します。

**Tinify**で画像を圧縮する例です。

```python
import tinify

# API キーを使って Tinify を設定
tinify.key = "YOUR_API_KEY"

# 画像を圧縮
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Pythonスクリプト例: フォルダー内の画像を最適化する

次のスクリプトはJPEGやPNGなど複数の形式の画像を読み込み、最適化したWebP画像を出力します。

```python
import os
from PIL import Image

# 画像を WebP 形式に変換する関数
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# フォルダー内の画像を順に処理して WebP に変換する関数
def optimize_images(folder_path, output_folder, quality=85):
    # 出力フォルダーがなければ作成
    os.makedirs(output_folder, exist_ok=True)
    
    # フォルダー内の各ファイルを処理
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # 入力パスと出力パスを作成
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # 画像を WebP 形式に変換
            convert_to_webp(input_path, output_path, quality=quality)

# 使用例
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

この例ではPython Imaging Library (PIL)で画像を開き、WebPに変換します。`convert_to_webp`関数は入力画像のパス、出力先のパス、任意の品質値を受け取ります。品質の既定値は85です。`optimize_images`関数はフォルダー内のファイルを順に確認し、対象の拡張子を判定してから`convert_to_webp`を呼び出します。最適化したWebP画像は指定した出力フォルダーに保存されます。

用途に合わせて`folder_path`、`output_folder`、`quality`の値を調整してください。

## まとめ

画像を最適化するとサイトの表示が速くなり、ユーザー体験と検索結果でのパフォーマンスを改善できます。Pythonには画像の圧縮、リサイズ、形式変換、自動処理に使えるライブラリがあります。PillowとTinifyは、適切な画質を保ちながら一枚または複数の画像ファイルを小さくできます。まず画像の寸法と品質を決め、その設定を処理手順に適用してください。


## 参考資料
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
