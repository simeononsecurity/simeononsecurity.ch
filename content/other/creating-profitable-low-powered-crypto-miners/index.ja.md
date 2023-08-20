---
title: "低電力ハードウェアを使用して収益性の高い受動的収入ボックスを構築する: ガイド"
draft: false
toc: true
date: 2023-02-07
description: "このガイドでは、Raspberry Pi または Intel NUC を使用して低電力受動的収入暗号マイナーをセットアップし、1 ボックスあたり月額 10 ～ 20 ドルを稼ぐ方法を学びます"
tags: ["収益性の高い受動的所得ボックスを構築する", "低電力ハードウェア", "不労所得", "クリプトマイナー", "ラズベリーパイ", "インテル NUC", "ガイド", "ハードウェア要件", "OSのインストール", "ソフトウェアのインストール", "ドッカー", "Dockerコンテナの自動更新", "Ubuntuサーバー", "Ubuntuデスクトップ", "ラズビアン", "バジェット", "USFF", "小さい", "ミニ", "マイクロPC", "技術経験", "稼ぐアプリ", "ミスト", "ピアツープロフィット", "ハニーゲイン", "TraffMonitizer", "ものみの塔", "噛む", "Linuxのアップデート", "Ubuntu", "デビアン", "CentOS", "RHEL", "オフラインアップデート", "ローカルリポジトリ", "キャッシュ", "サーバーのセットアップ", "クライアントのセットアップ", "適切なミラー", "デブミラー", "リポジトリの作成", "apt-cacher-ng", "ヤムクロン", "Linux システムのアップデート", "オフラインパッケージのアップデート", "オフラインソフトウェアアップデート", "ローカルパッケージリポジトリ", "ローカルパッケージキャッシュ", "オフライン Linux アップデート", "オフラインアップデートの処理", "オフラインアップデート方法", "オフラインでのシステムメンテナンス", "Linuxサーバーのアップデート", "Linuxクライアントのアップデート", "オフラインのソフトウェア管理", "オフラインパッケージ管理", "戦略を更新する", "Linuxのセキュリティアップデート"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "ボックスのような形をした緑色の回路基板で、そこに接続されたワイヤとしてインターネット接続のシンボルが表示されます。"
coverCaption: ""
---

**低電力ハードウェアを使用して収益性の高い受動的収入ボックスを構築する: ガイド**
最近では多くの人が仮想通貨マイニングやヘリウムマイナーなどの低出力マイナーに夢中になっています。これらはすべて素晴らしいものですが、もうそれほど多くの収入は得られず、1 つの種類の収入に集中しています。今日は、ボックスと住宅用 IP ごとに月に 10 ～ 20 ドルの収益を得る、低消費電力の受動的収入ボックスを構築します。

*このボックスをゲスト ネットワーク上に設定できる場合、またはさらに良いのは分離された VLAN 上に設定できる場合は、そうしてください。これはセキュリティに関するブログではありますが、すべての人のセキュリティ上の懸念やリスク許容度を想定することはできません。*

## ハードウェア要件:
次のいずれかが必要です。基本的に必要なのは、入手可能な効率的で低消費電力のコンピューターだけです。 Raspberry PI、Intel NUC、または同様のもので十分です。それほど強力である必要はありません。ただし、少なくとも 32g ～ 64g のストレージ、4g の RAM、少なくとも 2 つの CPU スレッドを搭載することをお勧めします。このため、ハードウェアの予算は約 100 ドルから 200 ドルを目標としますが、ニーズに合う場合は自由に予算を上げても構いません。私たちのパワー目標はおよそです。平均25w。
### ラズベリーパイ:
最近では入手するのが難しいですが、超低消費電力で、かなりカスタマイズ可能です。 Raspberry PI に Raspian をインストールする方法については、
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### インテル Nuc:
多種多様なモデルが揃っています。自由に新しいものを選択してください。
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### USFF/小型/ミニ/マイクロ PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Intel N5100 または同等のミニ PC
超低消費電力の Raspberry Pi と同等ですが、x64 プラットフォーム用。
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## OSのインストール:
ここでは、オペレーティング システムのインストール方法の技術的な詳細については説明しません。ただし、開始するための優れたリソースがいくつかあります
### ラズビアン:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


＃＃ ソフトウェアのインストール：
これは長いセクションになります。 Docker をセットアップし、Docker を通じて Docker コンテナーの自動更新をセットアップし、複数の Docker コンテナーをインストールします。また、ubuntu サーバーを使用していることを前提としていますが、ubuntu サーバー、ubuntu デスクトップ、および raspbian のコマンドはすべて同じである必要があります。

*このセクションでは、ある程度の基本的な技術経験があり、オペレーティング システムがすでにインストールされており、端末にアクセスする方法を知っていることを前提としています。*

### アップデートのインストール:
まず、システムが完全に最新であることを確認する必要があります。
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Docker のインストール:
OS にあらかじめパッケージ化されている既存のバージョンをアンインストールし、Docker のリポジトリ自体から最新バージョンをインストールする必要があります。
```bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Watchtower をインストールします。
この Docker コンテナは、すべての Docker コンテナを定期的に最新のイメージに自動的に更新し、古い (失効した) イメージをクリーンアップします。
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Bitping をインストールします。
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping を使用すると、企業がネットワークから軽量のネットワーク テストを実行するためのノードを提供することで、Solana で支払いを受けることができます。
これは、ノードごとに 1 日あたり平均約 0.1 セントになります。私が知っていることはあまりありませんが、可能性はあり、支払いも簡単です。

＃＃＃＃ アカウントを作成する：
でアカウントを作成してください [bitping.com](https://bitping.com)

#### Docker コンテナをインストールします。
ステップ 1. コンテナーのセットアップ手順が案内され、サインインを求められるため、最初にこれらのコマンドを実行します。
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

bitping アカウントでサインインした後、キーボードの CTRL+C を押してコンテナをエスケープします。

ステップ 2. このコマンドを実行して、コンテナーをバックグラウンドで永続化します。
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### 獲得アプリをインストール:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/GCL9QzB5)

Earn アプリを使用すると、VPN サービスとしてインターネットを共有して、驚くほどの報酬を得ることができます。住宅用 IP ごとにノードごとに月平均約 5 ドルかかります。 PayPal および Amazon ギフトカードによる支払いを提供します。

#### 獲得アプリアカウントを作成します:
でアカウントを作成してください [earnapp.com](https://earnapp.com/i/GCL9QzB5)
*警告、Google アカウントが必要です*

#### 非 Docker バージョンのアプリをインストールして、UUID を取得します。
UUID を取得した後は必ずアンインストールしてください。そうしないと、同じホスト上で自動更新が行われずに 2 回実行することになります。
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Docker コンテナをインストールします。
端末に貼り付ける前に文字列を変更してください。獲得アプリの UUID を指定する必要があります。
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### ビデオチュートリアル:
{{< youtube id="tt499o0OjGU" >}}

### ハニーゲインをインストールします。
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain を使用すると、VPN サービスとしてインターネットを共有して、驚くほどの報酬を得ることができます。住宅用 IP ごとにノードごとに月平均約 5 ドルかかります。支払いは複雑になる場合があります。このコンテナの使用を決定する前に、さらに読んでください。

#### ハニーゲインアカウントを作成します:
でアカウントを作成してください [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Docker コンテナをインストールします。
端末に貼り付ける前に、明らかな電子メール、パスワード、デバイス名で文字列を変更します。
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Raspberry Pi の代替手順
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### ビデオチュートリアル:
{{< youtube id="Wd11M0nSy1k" >}}

### PawnsApp をインストールします。
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
Pawns アプリは、ここにリストされている他のアプリと同様に、インターネットの共有に対して料金を支払うことを提供します。最低支払額は 5 ドルです。平均支払い額は、IP ごとのノードごとに月額 0.50 ドルです。

#### PawnsApp アカウントを作成します:
でアカウントを作成してください [https://pawns.app](https://pawns.app/?r=2092882)

#### Docker コンテナをインストールします。

端末にコピーする前に、電子メール、パスワード、デバイス名、デバイス ID を使用して以下を変更します。
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### リポケットをインストールします。
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

ここでの他の製品と同様です。最低 20 ドルの支払い。支払いは複雑になる場合があります。このサービスを使用するかどうかは、自分で調べてください。ペイアウトは、ノードごと、ボックスごとに月平均約 1 ドルです。

#### リポケットアカウントを作成します:
でアカウントを作成してください [repocket.co](https://link.repocket.co/raqc) ダッシュボードから API キーを取得します。
#### Docker コンテナをインストールします。
端末に貼り付ける前に、次の行を電子メールと API キーで変更します。
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### ビデオチュートリアル:
{{< youtube id="171gWknfAbY" >}}

### Traff Monetizer をインストールします。
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

EarnApp や HoneyGain と同様に、TraffMonetizer はインターネットの共有に対して料金を支払います。 IP ごとにノードごとに月平均約 2 ドルかかります。 BTCでの支払いのみを提供します。

#### Traff Monetizer アカウントを作成します。
でアカウントを作成してください [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
ダッシュボードに入ったら、アプリケーション トークンをメモします。

#### Docker コンテナをインストールします。
次の文字列をコピーし、ターミナルに貼り付ける前に、ダッシュボードから取得したトークンを追加します。

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### ミステリウムをインストールします。
[Mysterium](https://www.mysterium.network/) は、Ethereum および Polygon ブロックチェーン上に構築された分散型 VPN およびウェブスクレイピング サービスです。
IP ごとのノードごとの複数の要因に応じて、支払いは月あたり平均 1 ドルから 20 ドルになります。アクティブ化用にノードをセットアップするには 1.XX ドルかかります。 MYSTトークンでの支払い。


#### Docker コンテナをインストールします。
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Docker コンテナをセットアップします。
「nodeip」をノードの IP アドレスに置き換えて、http://"nodeip"/#/dashboard に移動します。これは、ターミナルに「ifconfig」と入力すると見つかります。

「ノードセットアップの開始」をクリックします。

報酬を受け取りたいERC20ウォレットのアドレスを入力し、「次へ」をクリックします。 MetaMask アドレスの 1 つと同様に、標準の Ethereum アドレスを使用できます。

今後このノード ダッシュボードにアクセスするために使用するパスワードを入力します。ネットワーク内のノードを要求するには、チェックボックスをオンにしてください。

「Get it here」リンクをクリックして API キーを見つけます。コピーしてください。戻って貼り付けます。 「保存して続行」をクリックします。

#### ポート転送:
すべてのユーザー固有のハードウェアにポートフォワードする方法を説明することはできません。ポートフォワードの方法を学ぶためのリソースをいくつか紹介します。
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### 起動時に Docker コンテナを自動再起動:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### オプションの構成:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### マルウェアやトラッカーをブロックしてセキュリティを強化します。
すべての DNS リクエストを Cloudflares マルウェアおよび追跡保護 DNS に強制します。
また、DNS/HTTPS リクエストをブロックします。
*ネットワーク上により高度なルーターまたはファイアウォールがある場合は、snort/securita などのパッケージを使用して、既知の不正行為 IP、Tor アクセス、トレント、P2P トラフィック一般などをブロックするためのより高度なルールを作成することもできます。これは非常に効果的です。推奨されていますが、必須ではありません。*
```bash
# Allow ssh still
sudo ufw allow 22
# Allow dns out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp
# Redirect all dns back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2
# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP
# Block Default ToR Ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp
# Block Torrents
sudo ufw deny out 6881/tcp
sudo ufw deny out 6881/udp
sudo ufw deny out 6882-6999/tcp
sudo ufw deny out 6882-6999/udp
iptables -A FORWARD -m string --algo bm --string "BitTorrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "BitTorrent protocol" -j DROP
iptables -A FORWARD -m string --algo bm --string "peer_id=" -j DROP
iptables -A FORWARD -m string --algo bm --string ".torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce.php?passkey=" -j DROP
iptables -A FORWARD -m string --algo bm --string "torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce" -j DROP
iptables -A FORWARD -m string --algo bm --string "info_hash" -j DROP
# Save the Changes and Enable the Firewall
sudo iptables-save
sudo ufw enable
```
より高度な ToR ブロックを行うには、次の操作を実行できます。
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

＃＃ 利益？