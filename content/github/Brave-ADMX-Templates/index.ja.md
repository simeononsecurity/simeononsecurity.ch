---
title: "BraveADMX で Brave ブラウザ ポリシーを制御する - 修正された ADMX テンプレート"
date: 2020-07-25
---


Brave は企業として、純粋なレジストリをサポートされる唯一のオプションとして推している Brave ブラウザ サイト用の ADMX テンプレートをリリースできませんでした。
Brave Browser は Chromium をベースに構築されているため、すべてではないにしても、Chromium および Google Chrome ADMX テンプレートの同じポリシーのほとんどをサポートする必要があります。
これを念頭に置いて、Brave Browser のレジストリ パスを反映するように Google Chrome ADMX テンプレートを変更しました。最初にいくつかのトラブルシューティングとテストを行った後、テンプレートは機能するようです。

**これらのポリシー定義はプレアルファ版の状態です。これらはテスト目的のみに使用してください**

## 必要なファイルをダウンロードします。

**必要なファイルを次の場所からダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

＃＃ ノート

以下に従って Google Chrome ポリシー定義を変更しました。
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**注:** 「HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome」を「HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave」に置き換えました。

**注意:** SOS の Chromium テンプレートと Brave Browser ADMX テンプレートを同時にインストールしないでください。

＃＃ インストールする方法

1.) readme.md を除くすべてのファイルを「C:\Windows\PolicyDefinitions」および/または「\\\domain.tld\domain\Policies\PolicyDefinitions」にコピーします。

2.) 利益は？