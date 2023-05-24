---
title: "HackTheBox - チャレンジ - 暗号化 - 弱い RSA"
draft: false
description: "自動 RSA 攻撃ツール RsaCtfTool を使用して、HackTheBox Weak RSA Crypto チャレンジを簡単に解決する方法を学びます。"
tags: ["ハックザボックス", "課題", "暗号", "弱い RSA", "RsaCtfツール", "HTB 弱い RSA 暗号", "簡単チャレンジ", "RSA暗号", "flag.enc", "key.pub", "OpenSSL パッケージ", "自動化されたRSA攻撃ツール", "Pythonスクリプト", "RsaCtfツール", "Python3", "公開鍵", "暗号化解除ファイル", "フラグの例"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "マントとマスクをかぶった漫画のハッカーが、HTB のロゴが付いた金庫室のドアの前に立ち、成功を象徴する緑色の背景と上の吹き出し内の旗が付いたツール (レンチやドライバーなど) を持っています。彼らの頭。"
coverCaption: ""
---
 HTB Weak RSA Crypto チャレンジを簡単に実行できます。 RSA 暗号に基づくこの簡単な課題では、RsaCtfTool などの自動化された RSA 攻撃ツールを使用する必要があります。簡単なコマンドでフラグを取得し、HackTheBox チャレンジで暗号化スキルを高めましょう。

______

## 提供されるファイル:

**次のファイルが提供されます:**
- flag.enc
- key.pub

## ウォークスルー:

一見すると、公開キーを使用してフラグを復号できると思われるでしょう。
そのために、OpenSSL パッケージを使用してフラグを復号化する場合があります。
今回は少し異なり、OpenSSL パッケージがこの課題では機能しないことがわかります。

自動化された RSA 攻撃ツールを使用します。一般的な Python スクリプトは次のとおりです。 [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
簡単に言うと、このツールは自動的にフラグを簡単に見つけます。

______

### フラグの例:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
