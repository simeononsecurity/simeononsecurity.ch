---
title: "WMI フィルタリングを理解する"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "WMI フィルタリングを使ってグループ ポリシー オブジェクト（GPO）の適用先を調整する方法を、実例とベストプラクティスとともに紹介します。"
genre: ["Windows 管理", "グループ ポリシー", "システム管理", "ネットワーク管理", "IT インフラストラクチャ", "ポリシー管理", "IT ガバナンス", "IT 自動化", "Active Directory", "セキュリティ コンプライアンス"]
tags: ["WMI フィルタリング", "GPO", "グループ ポリシー オブジェクト", "WMI フィルター", "ポリシーの適用対象", "WMI クエリ", "Windows Management Instrumentation", "GPO 制御", "グループ ポリシー管理コンソール", "WMI Query Language", "ポリシー適用", "WQL", "ポリシーの調整", "ポリシー管理", "システム リソース", "ポリシー対象の例", "システム管理", "ネットワーク管理", "IT インフラ管理", "IT 自動化", "Active Directory 管理", "セキュリティ コンプライアンス", "ポリシー制御手法", "ポリシー管理のベストプラクティス", "ポリシー フィルタリング", "GPO 制御戦略", "GPO セキュリティ", "WMI フィルタリングの利点", "WMI フィルタリングの実装", "WMI フィルターのベストプラクティス"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "フィルター アイコンに焦点を合わせた拡大鏡のイラスト。WMI フィルタリングによる GPO の適用対象選択を表します。"
coverCaption: "WMI フィルタリングで GPO の適用対象を効率よく絞り込みましょう。"
---

## はじめに

グループ ポリシー オブジェクト（GPO）では、[**WMI フィルタリング**](https://simeononsecurity.com/github/wmi-filters/)を使って、WMI（Windows Management Instrumentation）クエリの結果に基づき、ポリシーを適用するコンピューターやユーザーを制御できます。管理者は適用対象を細かく調整し、意図した対象にだけポリシーを適用できます。この記事では、WMI フィルタリングの概要、GPO での動作、[WMI フィルター](https://simeononsecurity.com/github/wmi-filters/)の作成方法、実用例を説明します。

## [WMI フィルタリングとは](https://simeononsecurity.com/github/wmi-filters/)

[**WMI フィルタリング**](https://simeononsecurity.com/github/wmi-filters/)とは、WMI クエリの結果を条件として GPO にフィルターを適用する仕組みです。WMI は Windows に組み込まれた管理インフラストラクチャで、管理情報の取得やシステム リソースとのプログラムによるやり取りを可能にします。WMI フィルタリングを使うと、クエリで定義した条件に応じて GPO の適用先を動的に決められます。

WMI フィルターは、SQL（Structured Query Language）のサブセットである WMI Query Language（WQL）で記述します。通常、WMI 名前空間にあるプロパティと値を条件にします。管理者は条件、論理演算子、名前空間を組み合わせ、特定のコンピューターやユーザーを対象とするクエリを作成できます。

## GPO での WMI フィルタリングの動作

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="GPO に関連付けた WMI フィルターが WQL クエリを True または False と評価し、対象コンピューターに GPO を適用するか決める流れ図" >}}

グループ ポリシーでは、**WMI フィルタリング**によって **WMI クエリ**の評価結果に応じて GPO を選択的に適用できます。GPO に **WMI フィルター**を関連付けると、結果が **True** か **False** かによって GPO の適用が決まります。

WMI フィルターは、SQL のサブセットである **WMI Query Language（WQL）**を使います。WQL では **WMI 名前空間**にあるさまざまな**プロパティ**と**値**を条件にした複雑なクエリを作成できます。これにより、特定のコンピューターやユーザーを対象にできます。

たとえば、組織が Windows 10 を実行するコンピューターだけに GPO を適用したい場合、**Win32_OperatingSystem** クラスの **OperatingSystem** プロパティを確認する WMI フィルターを作成できます。クエリの例を示します。

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

このクエリは、OS のバージョンが「10.」で始まるか確認します。これは Windows 10 を示します。結果が **True** なら、対象コンピューターに GPO が適用されます。そうでなければ適用されません。

WMI フィルタリングでは **AND**、**OR**、**NOT** などの条件や論理演算子も使用できます。複数のプロパティと値を組み合わせることで、GPO の適用をさらに細かく制御できます。

異なる **WMI 名前空間**を使うと、特定の WMI クラスやプロパティの集合にアクセスできます。ハードウェア構成、インストール済みソフトウェア、ネットワーク設定など、さまざまな条件に基づいて GPO を適用できます。

WMI フィルターやクエリの作成については、Microsoft の[グループ ポリシーの WMI フィルタリング](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)のドキュメントを参照してください。

このように、WMI フィルタリングを使うと、変化する条件に応じて特定のコンピューターやユーザーに GPO を適用し、IT 環境をより適切に管理できます。

## GPO 用の WMI フィルターを作成する

GPO 用の WMI フィルターを作成する手順は次のとおりです。

1. ドメインに参加している Windows コンピューターで、**グループ ポリシー管理コンソール**（GPMC）を開きます。

2. ドメインを展開し、**WMI フィルター**ノードを開きます。

3. **WMI フィルター**を右クリックして、**新規**を選択します。

4. フィルターに分かりやすい名前を付け、**クエリ**欄に WQL 構文の WMI クエリを入力します。

5. **OK** をクリックしてフィルターを保存します。

作成したフィルターは、1 つ以上の GPO に関連付けられます。関連付けるには、次の手順を行います。

1. 対象の GPO を右クリックして、**プロパティ**を選択します。

2. GPO のプロパティ ウィンドウで、**WMI フィルタリング**タブを開きます。

3. 一覧から目的の WMI フィルターを選択します。

4. **OK** をクリックして変更を保存します。

WMI フィルターを GPO に関連付けると、WMI クエリの結果に基づいてポリシーの適用対象を正確に制御できます。

## 1 つの GPO に設定できる WMI フィルターの数

管理者は、細かなポリシー対象指定のために、1 つの GPO に**複数の WMI フィルター**を設定できます。1 つの GPO に関連付けるフィルターの具体的な上限は定められていないため、複雑な組み合わせも作れます。

ただし、フィルターの数が GPO の処理時間に与える影響を考慮してください。フィルターが増えるほど、GPO の評価や適用に時間がかかる場合があります。効率を保つため、フィルターの数は適切な範囲にします。

たとえば、Windows 10 を実行し、特定のソフトウェアがインストールされたコンピューターだけに GPO を適用したいとします。この場合、**OS**用と**ソフトウェアのインストール**用に 2 つの WMI フィルターを作成し、組み合わせて対象を絞れます。

必要な対象条件と処理時間のバランスを取ることが重要です。フィルター数を決める前に、環境の複雑さ、コンピューターやユーザーの数、性能への影響を評価してください。

複数の WMI フィルターを使うことで GPO の対象指定を最適化しつつ、IT 環境の処理と管理を効率よく保てます。

## GPO での WMI フィルタリングの実用例

WMI フィルタリングを使うと、GPO を必要な対象に適用できます。例を紹介します。

1. **特定の OS を対象にする**：**Windows 10** コンピューターだけに GPO を適用するには、OS のバージョンを確認するフィルターを作成します。例：`"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`。これで Windows 10 のコンピューターを対象にできます。

2. **デスクトップとノート PC で異なるポリシーを適用する**：機器の種類によってポリシーを分ける場合は、2 つの WMI フィルターを使います。一方は `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"` のようなハードウェア属性でデスクトップを識別し、もう一方はノート PC を識別します。それぞれに適したポリシーを適用できます。

3. **ディスク空き容量に応じて適用する**：空き容量が少ないコンピューターに負荷の高いポリシーを適用しないよう、空き容量を確認するフィルターを作ります。たとえば `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` は、空き容量が 10 GB 未満のコンピューターを除外します。

これらの例は、GPO における **WMI フィルタリング**の柔軟性を示しています。管理者は条件に基づいてポリシーの適用対象を指定できます。

## まとめ

WMI フィルタリングは、グループ ポリシー オブジェクトの便利な機能です。WMI クエリの結果に基づいて、特定のコンピューターやユーザーにだけポリシーを適用できます。これにより、より効率的で制御しやすいポリシー管理が可能になります。この記事では、WMI フィルタリングの概要、GPO での動作、フィルターの作成方法、実例を説明しました。

GPO 管理に WMI フィルタリングを取り入れると、意図した対象にだけポリシーを適用でき、適用精度を高められます。

## 参考資料

- [Microsoft Docs：GPO 用 WMI フィルターを作成する](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs：about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs：グループ ポリシー](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs：グループ ポリシー管理コンソール](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
