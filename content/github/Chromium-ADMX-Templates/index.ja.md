---
title: "ChromiumADMX: Chromium ブラウザ用の適切な ADMX テンプレート"
date: 2020-07-25
---


Chromium ブラウザ用の適切な ADMX テンプレート

Chromium は企業として、Google Chrome テンプレートと同時にインストールされる可能性がある Chromium ブラウザ用の ADMX テンプレートをリリースできませんでした。
これを念頭に置いて、Chromium ブラウザのレジストリ パスを反映するように Google Chrome ADMX テンプレートを変更し、GPO の Google ADMX フォルダーに並べて配置しました。

**これらのポリシー定義はプレアルファ版の状態です。これらはテスト目的のみに使用してください**

## 必要なファイルをダウンロードします

**必要なファイルを次の場所からダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

＃＃ ノート

以下に従って Google Chrome ポリシー定義を変更しました。
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**注:** 「HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome」を「HKEY_LOCAL_MACHINE\Software\Policies\Chromium\」に置き換えます。

**注意:** SOS の Chromium テンプレートと Brave Browser ADMX テンプレートを同時にインストールしないでください。

＃＃ インストールする方法

1.) readme.md を除くすべてのファイルを「C:\Windows\PolicyDefinitions」および/または「\\\domain.tld\domain\Policies\PolicyDefinitions」にコピーします。

2.) 利益は？




