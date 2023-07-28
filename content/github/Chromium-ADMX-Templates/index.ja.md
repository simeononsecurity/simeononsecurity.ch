---
title: "ChromiumADMX：Chromiumブラウザ用の適切なADMXテンプレート"
date: 2020-07-25
---


Chromiumブラウザ用の適切なADMXテンプレート

Chromium社は、Google Chromeのテンプレートと同時にインストールできるChromium Browser用のADMXテンプレートをリリースしていません。
そのため、Google ChromeのADMXテンプレートを修正し、Chromiumブラウザのレジストリパスを反映させ、GPOのGoogle ADMXフォルダに配置しました。

**これらのポリシー定義はプレアルファ版です。テスト目的でのみ使用してください。

## 必要なファイルのダウンロード

**必要なファイルを下記からダウンロードしてください。 [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## ノート

Google Chromeのポリシー定義を修正しました：
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**"HKEY_LOCAL_MACHINE_SoftwarePoliciesGoogleChrome "を "HKEY_LOCAL_MACHINE_SoftwarePoliciesChromium "に置き換えた。

**注意：*** SOS'es ChromiumとBrave Browser ADMXテンプレートを同時にインストールしないでください。

## インストール方法

1.)readme.md以外のファイルを "C:⇄WindowsPolicyDefinitions "と"⇄domain.tld⇄PolicyDefinitions "にコピーする。

2.)利益？




