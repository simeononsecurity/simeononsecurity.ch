---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "招待コードを生成し、HackTheBox オンライン プラットフォームに参加して、Windows と Linux の両方で侵入テストとサイバーセキュリティのスキルをテストして向上させる方法を学びます。"
tags: ["ハックザボックス", "チャレンジを招待する", "侵入テスト", "サイバーセキュリティ", "ウィンドウズ", "Linux", "オンラインプラットフォーム", "HTTPポスト", "招待コード", "Base64エンコード", "パワーシェル", "Linuxバッシュ", "Base64 デコード", "コード生成の招待", "プログラミング", "ウェブ開発", "テクノロジー", "ITセキュリティ", "ITトレーニング"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "HackTheBox のロゴの配色 (青と白) の街並みの背景に、キーで金庫室のドアがロック解除され、トロフィーまたはメダルが現れる HackTheBox Web サイトを示す漫画のコンピューター画面。"
coverCaption: ""
---
 Windows または Linux で HackTheBox 招待チャレンジを完了するためのステップバイステップの手順。招待コードを生成し、オンライン プラットフォームに参加して、侵入テストとサイバー セキュリティのスキルをテストして向上させる方法を学びます。この記事では、シンプルなソリューションと高度なソリューションの両方を紹介しており、あらゆるレベルのユーザーが簡単にチャレンジを完了してプラットフォームにアクセスできるようにしています。

______

## ハック・ザ・ボックスとは何ですか?

HackTheBox は、侵入テストとサイバー セキュリティのスキルをテストし、向上させるためのオンライン プラットフォームです。

## Hack the box に参加するにはどうすればよいですか?

HackTheBox (HTB) でアカウントを作成するには、招待チャレンジを完了するか、自分自身をハッキングして侵入する必要があります。難しいことではありませんので、心配しないでください。この記事はチャレンジを完了するのに役立ちます。

まず、に行きます[HackTheBox Website](https://hackthebox.eu) そして参加ボタンをクリックしてください。

招待コードを要求するボックスが明確に表示されます。

招待コードの入力を求めるテキスト ボックスがはっきりと見えます。

キーボードの ***「F12」*** または ***「Ctrl + Shift + I」*** を押して、ブラウザの開発者ツールを開きます。

[要素] タブにスクリプトがあります **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

JavaScript と makeInviteCode 関数を確認すると、招待コードを取得するには **HTTP POST** を **/api/invite/generate** に送信する必要があることがわかります。

Base64 でエンコードされた招待コードを取得するには、次の手順を実行します。

＃＃＃ 解決：

＃＃＃＃ 単純：
- **ウィンドウズ**：```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Which will generate the following content: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

If you take the encoded invite code to [base64decode.org](https://www.base64decode.org/), you'll get your invite code!

#### Advanced (Instantly print out invite code):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Note**: You'll need to install the [jq](https://stedolan.github.io/jq/download/) package.

______

### Invite Code Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


