---
title: "クリーンなWindows ISOをダウンロードし、スクラッチからインストールする方法"
date: 2023-02-20
toc: true
draft: false
description: "このステップバイステップガイドで、クリーンなWindows ISOファイルをダウンロードし、ゼロからWindowsをインストールする方法を学びましょう。"
tags: ["ウィンドウズ10", "ウィンドウズ11", "ISOファイル", "クリーンインストール", "メディアクリエイトツール", "ブータブルUSB", "インストールメディア", "バイオス", "UEFIファームウェア", "カスタムインストール", "プロダクトキー", "64ビットシステム", "32ビットシステム", "ルーファス", "イムグバーン", "CDBurnerXP", "ハッシュカルク", "MD5 & SHA チェックサムユーティリティ", "システムタイプ"]
cover: "/img/cover/A_cartoon_image_of_a_person_holding_a_USB_stick.png"
coverAlt: "Windowsのロゴとチェックマークが描かれたUSBメモリを持った人が、Windowsのロゴが描かれたパソコンの画面の前に立っている漫画のイメージです。"
coverCaption: ""
---

**クリーンなWindows 10または11のISOをダウンロードし、Windowsをスクラッチからインストールする方法**。

新しいコンピューターに Windows をインストールする予定がある場合、または発生している問題を取り除くためにクリーンインストールを行いたい場合、クリーンな Windows ISO ファイルをダウンロードすることが不可欠な最初のステップとなります。この記事では、クリーンなWindows 10または11のISOをダウンロードする手順を説明し、インストールプロセスについて案内します。

## パート1：クリーンな Windows ISO ファイルをダウンロードする

### ステップ 1: システムの種類を確認する

クリーンなWindows ISOをダウンロードするための最初のステップは、システムの種類を確認することです。32ビットシステムか64ビットシステムかを知る必要があり、これによってダウンロードするISOファイルが決定されるからです。

Windows 10 でシステムの種類を確認するには、次の手順に従います：

1.スタートメニューを開き、"設定 "をクリックします。
2."システム "をクリックします。
3."バージョン情報 "をクリックします。
4.デバイスの仕様」の「システムタイプ」の項目を確認します。

32ビットシステムの場合、Windowsの32ビット版をダウンロードする必要があります。64ビットシステムの場合、32ビット版と64ビット版のどちらをダウンロードしても構いませんが、より良いパフォーマンスを得るために64ビット版をお勧めします。

### ステップ2：メディア作成ツールのダウンロード

クリーンなWindows ISOをダウンロードするために、MicrosoftのMedia Creation Toolを使用します。以下の手順でMicrosoftのウェブサイトから直接ダウンロードすることができます：

1.にアクセスします。[Microsoft Windows 10 download page](https://www.microsoft.com/en-us/software-download/windows10)
2."Windows10インストールメディアの作成 "の項目までスクロールし、"今すぐツールをダウンロード "をクリックします。
3.ファイルをパソコンに保存してください。

Windows 11をダウンロードする場合も、手順は同様です。メディア作成ツールは、以下のサイトからダウンロードできます。[Microsoft Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11)をクリックし、同じ手順で操作してください。

### ステップ3：メディア作成ツールの実行

メディア作成ツールのダウンロードが完了したら、パソコンでメディア作成ツールを実行します。現在お使いのPCをアップグレードするか、インストールメディアを作成するかを聞かれます。インストールメディアを作成する」を選択し、"次へ "をクリックします。

### ステップ4：言語、エディション、アーキテクチャを選択する

次のステップは、言語、エディション、アーキテクチャを選択することです。言語オプションは現在の言語のままでも構いませんが、お好みで別の言語を選択することもできます。

エディションは、インストールするWindowsのバージョンを選択します。Windows 10 HomeとWindows 10 Pro、またはWindows 11 HomeとWindows 11 Proのいずれかを選択することになります。

アーキテクチャは、ステップ1で決定したシステムの種類を選択します。64ビットシステムの場合、パフォーマンスを向上させるために64ビット版の選択をお勧めします。

### ステップ5：メディアの種類を選択する

次のステップは、メディアの種類を選択することです。ブート可能なUSBドライブを作成するか、ISOファイルをダウンロードすることができます。

ブート可能なUSBドライブを作成する場合は、8GB以上の空き容量のあるUSBドライブが必要です。メディア作成ツールは、自動的にドライブをフォーマットし、必要なファイルをコピーします。

ISOファイルをダウンロードする場合は、Media Creation Toolがファイルをダウンロードし、コンピューターに保存します。その後、サードパーティ製のツールを使用して、ブート可能なUSBドライブを作成したり、ISOをDVDに書き込んだりすることができます。

### ステップ6：ISOファイルをダウンロードする

ISOファイルのダウンロードを選択した場合、メディアクリエイトツールはファイルのダウンロードを開始します。インターネット接続の速度により、ダウンロードに時間がかかる場合があります。

ダウンロードが完了すると、ツールがファイルを検証し、クリーンなISOであることを確認します。

### ステップ7：ISOファイルを検証する

ISOファイルの検証は、ダウンロードしたファイルがクリーンで変更されていないことを確認するために不可欠なステップです。ファイルを検証するには、次のようなツールを使用します。[HashCalc](https://www.slavasoft.com/hashcalc/) or [MD5 & SHA Checksum Utility](https://raylin.wordpress.com/downloads/md5-sha-1-checksum-utility/)

検証ツールのダウンロードとインストールが完了したら、検証ツールを開き、ダウンロードしたISOファイルを選択します。ツールはファイルのハッシュ値を計算し、WindowsのダウンロードページでMicrosoftが提供するハッシュ値と比較します。ハッシュ値が一致すれば、そのISOファイルはクリーンであり、Windowsのインストールに使用することができます。

## パート2：クリーンなISOからWindowsをインストールする

クリーンな Windows ISO ファイルを入手したら、それを使って Windows をコンピュータにインストールすることができます。以下はその手順です：

### ステップ1：インストールメディアを作成する

ISOファイルからWindowsをインストールする前に、インストールメディアを作成する必要があります。ブート可能なUSBドライブまたはDVDを使用することでこれを行うことができます。

ブート可能なUSBドライブを作成するには、以下のようなツールを使用します。[Rufus](https://rufus.ie/) or [Windows USB/DVD Download Tool](https://www.microsoft.com/en-us/download/windows-usb-dvd-download-tool)USBドライブを接続し、ツールを開き、指示に従って起動可能なドライブを作成するだけです。

DVDを使用したい場合は、以下のようなツールを使用することができます。[ImgBurn](https://www.imgburn.com/) or [CDBurnerXP](https://cdburnerxp.se/en/home)DVDを挿入し、ツールを開き、指示に従ってISOファイルをDVDに書き込みます。

### ステップ2：インストールメディアから起動する

インストールメディアを作成したら、そのメディアからコンピュータを起動する必要があります。これを行うには、コンピュータのBIOSまたはUEFIファームウェアの起動順序を変更する必要があるかもしれません。

BIOSまたはUEFIファームウェアに入るには、コンピュータを再起動し、画面に表示されるキーを押してください。これは通常、F2、F10、またはDelです。BIOSまたはUEFIファームウェアに入ったら、「Boot」メニューを探し、インストールメディアがリストの一番上に来るように起動順序を変更します。

### ステップ3：Windowsのインストール

コンピュータがインストールメディアから起動すると、Windowsのセットアップ画面が表示されます。指示に従って、Windowsをコンピュータにインストールします。

言語、タイムゾーン、キーボードレイアウトを選択するように指示されます。次に、プロダクトキーの入力を求められます。プロダクトキーをお持ちでない場合は、「プロダクトキーを持っていません」を選択して、インストールを続行します。インストールが完了したら、後でWindowsをアクティベートすることができます。

次に、インストールの種類を選択するように指示されます。クリーンインストールを行う場合は、「カスタム」オプションを選択します。

次に、Windowsをインストールするパーティションを選択するように指示されます。新しいコンピュータやハードディスクが空っぽのコンピュータにWindowsをインストールする場合、未割り当ての領域が表示されます。未割り当ての領域を選択し、「次へ」をクリックすると、新しいパーティションが作成され、Windowsがインストールされます。

インストールが完了すると、Windowsが再起動し、ユーザーアカウントを設定するように指示されます。

## まとめ

クリーンな Windows ISO をダウンロードし、ゼロから Windows をインストールするのは大変に思えるかもしれませんが、誰でもできる簡単なプロセスです。このガイドのステップに従うことで、クリーンなWindowsを確実に手に入れることができます。

