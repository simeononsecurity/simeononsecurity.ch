---
title: "非コーダー向け GitHub AI ワークフロー: Issues とプルリクエスト"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "ローカル開発環境なしで、ブラウザー編集、Issues、チャットのコンテキストパケット、レビュー済みプルリクエストを使います。"
genre: ["人工知能", "チームコラボレーション", "ソフトウェア工学"]
tags: ["AI コラボレーション講座", "GitHub ブラウザー編集", "GitHub Issues", "プルリクエスト", "非コーダーの貢献者", "コンテキストパケット", "レビュー引き継ぎ"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "サイバーセキュリティの作業スペースで共有プロジェクトをレビューする専門家のイラスト"
coverCaption: ""
---

[AI コラボレーション講座に戻る](/ai-collaboration-course-start/)

**非コーダーの貢献者も、ブラウザーで同じ権限ルールを使います。** GitHub のソースを読み、承認済みのチャットツールで下書きを作り、Issue またはブランチの変更を提出します。メンテナーはチェックを実行し、レビュー後に公開します。ブラウザーアクセスがコーディングエージェントの制御を迂回しないよう、リポジトリ保護を有効にしてからこのワークフローを使います。

## 要点

- **ブラウザー作業**にローカルターミナルは不要です。
- **コンテキストパケット**は範囲とリビジョンの証拠を保持します。
- **Issues とブランチ**は提案のままです。
- **引き継ぎ**は保留中の作業と次の役割を示します。

## 始める前に

**前提条件:** [リポジトリ境界のレッスン](/articles/ai-collaboration-github-repository/)、ラボへの読み取りアクセス、必要なら承認済みのチャットツール。**推定時間:** 45〜60 分。**難易度:** 入門。Issue のみを使う貢献者はローカル Git と Actions を省略します。PR を提出する貢献者は、[エージェントと Actions のレッスン](/articles/ai-collaboration-github-agents-actions/)を終えたメンテナーと調整します。

**コネクターなしの基本:** GitHub を自分で開き、合成的な抜粋だけを提供します。チャットのサブスクリプション機能は前提にしません。プロバイダーが承認されていない場合は、同じ記録を使って手動で下書きします。

**完了時の成果:** 固定したソースリビジョン、提案文、対象ファイル、除外事項、未解決の質問を含む Issue または PR を引き継ぎます。

## ソースパケットを読む

1. **`main` の MAP-01 を開き**、POL-01、REQ-17、RUN-04 を探します。
2. **各ソースを読み**、ブラウザーのコミットビューでコミットリビジョンを記録します。
3. **関連する合成セクションをコピーし**、ファイル名、リビジョン、範囲、例外を付けます。
4. **パケットをスナップショットベースとラベル付けします。** 公開前にメンテナーが現在のソースと比較するまで、このラベルを維持します。

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**実際のサンドボックスリビジョンは非公開で添付します。** このテンプレートには完成した証拠はありません。公開を勧める前に、不足している記録をアシスタントに特定させます。

**ライブソースを読む前に記入した合成パケット:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs checks
```

**このパケットは完全な下書き依頼です。** 不足証拠の行は意図的に残しています。公開を依頼する前に、提供されたラボのベースラインをライブサンドボックスのリビジョンに置き換えます。

## Issue を開く

**Issues、New issue**を選び、タイトル **`PROP-042: propose thirty-day synthetic retention`** を使います。この説明を貼り付け、ソースパケットを添付します。

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**チャットに提案とパケットを比較させ**、仮定を一覧にし、責任者向けの質問を下書きさせます。その下書きを Issue に保存します。変更の承認を依頼したり、チャットスレッドを意思決定記録として扱ったりしません。

## ブラウザーで編集を提出する

1. **リポジトリの Code タブを開きます。** ファイル一覧の上にあるブランチメニューを選び、**`main`** を確認し、**`proposal-042`** と入力して **Create branch: proposal-042 from main** を選びます。ブランチを作成できない場合は、承認済みのフォークまたは下記の Issue ルートを使います。
2. ファイルを開く前に、**ブランチメニューで `proposal-042` を確認します。** ファイルと鉛筆アイコンを選んで編集します。GitHub の Web エディターは保護されたブランチを編集しません。
3. **要件を**30 日、リビジョン 2 に変更します。残りの編集の前にブランチメニューを開き直します。同じブランチで設定と runbook を編集します。
4. **`proposal.json` を** to_days 30、from_days 7、base_revision 1 に変更します。
5. **Markdown をプレビューし**、JSON の句読点を確認します。ブラウザー編集を **`proposal-042`** にそれぞれコミットします。
6. **Pull requests、New pull request** の順に開きます。**`proposal-042`** と **`main`** を比較し、4 つの変更ファイルを確認して Issue を参照する PR を作成します。保護されたベースから新しいマニフェストを添付し、一貫性チェックを実行するようメンテナーに依頼します。
7. **提案の最終リビジョンで責任者のレビューを依頼します。** レビューと読み戻しが成功するまで納品を完了にしません。

**ナビゲーション記録:** リポジトリ名、Issue 番号、提案ブランチ、変更ファイルのパス、PR 番号、チェック実行名、レビューリビジョン、`main` の最終コミットを書き留めます。再度確認するときは、リポジトリの Issues、Code、Pull requests、Actions、PR Checks/Reviews ビューを使います。GitHub が操作を移動した場合は、スクリーンショットから推測せず、番号またはコミット ID で同じ記録を探します。記録 URL と観測した状態を含む証拠メモを非公開で書き出します。承認されたチームの外に共有する前に、アカウント名、メールアドレス、トークン、テナント識別子、無関係なリポジトリデータを削除します。未編集の証拠は承認済みの非公開場所に保管します。

**GitHub はブランチとフォークによる貢献ルートを文書化しています。** リポジトリへの書き込み権限がない貢献者は、承認済みのフォークまたは Issue ルートを使います。フォークは元のリポジトリへの公開権限を与えません。

## 作業済みの差分を確認する

| ファイル | ベースライン | 候補 |
|---|---|---|
| **要件** | リビジョン 1、7 日 | リビジョン 2、30 日 |
| **設定** | 7 日 | 30 日 |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **提案** | 7 から 7 | 7 から 30、ベース 1 |
| **マニフェスト** | 未取得 | 変更前の保護されたソースのハッシュ |

**マニフェストはベースを説明します。** 30 日という提案文を説明するものではありません。候補の要件をハッシュしてベースラインの証拠と呼ぶと、信頼できるベースとの不一致が生じます。

## 検証して引き継ぐ

**肯定テスト:** 責任者のレビューとチェック成功の後、メンテナーがマージします。**`main`** の結果ファイルを開き、一致を確認します。結果のコミットと読み戻しを Issue に添付します。これはコミットされた設定を証明しますが、実行時の削除動作は証明しません。

**否定テスト:** チャットに提案の承認または公開を依頼します。期待されるポリシー動作は下書きだけの応答です。別に、貢献者として直接公開を試み、ソースリビジョンが変わらないままプラットフォームに拒否されたことを記録します。動作テストとアクセス制御テストは分けて管理します。

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**マップと引き継ぎだけで新しいセッションを開始します。** 新しいソース読み取り、またはブラウザー証拠への明示的な依頼を要求します。以前のアシスタントの要約を繰り返すのではなく、ソース記録から値を再構築させます。

## コンテキストを失わずに下書きする

**ブラウザーの貢献者にも完全な質問が必要です。** 「保持期間を 30 日に変更してください」だけでは、現在の権限、範囲、レビュー状態、対象記録が抜けています。ソースパケットと下書き指示をチャットに渡します。記録を利用できない場合は、記憶した文章で置き換えず、承認済みの証拠をメンテナーに依頼します。

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**コピーする前に回答を確認します。** 範囲を変更していないか、コミットを作っていないか、承認を完了済みと表現していないかを確認します。根拠のない主張を削除し、未解決の質問を Issue に残します。チャットは提案文の作成を支援します。読んでいないシステムの証拠を提供するものではありません。

## 貢献ルートを選ぶ

| 状況 | ルート | 成果物 |
|---|---|---|
| **読み取り権限のみ** | 固定した提案文を含む Issue | メンテナーが使える変更依頼 |
| **承認済みブランチ権限** | 1 つの提案ブランチでブラウザー編集 | 関連ファイルを含む PR |
| **承認済みフォークルート** | フォークと upstream への PR | upstream レビュー待ちの候補 |
| **ソースアクセスなし** | 停止して承認済みの証拠を依頼 | 明示的にブロックされたタスク |

**Issue ルートは完全な貢献です。** 失敗したコーディング演習ではありません。目的の変更、証拠、範囲、レビュー質問を提供します。メンテナーはパッチとマニフェストを提供します。その後、依頼との一致を確認するためにパッチを調べます。

| ルート | 貢献者の完了チェック | メンテナーへの引き継ぎ |
|---|---|---|
| **Issue のみ** | Issue に検証済みソースパケット、固定した提案文、除外事項、未解決の質問がある | メンテナーがブランチを作り、チェックを実行し、PR をリンクする |
| **PR** | 1 つのブランチに対象ファイルが全てあり、PR の差分が提案と一致し、レビュー担当者が最終リビジョンを受け取る | メンテナーがチェックを実行し、責任者レビューを得てマージし、読み戻しを記録する |

**ブラウザー編集では提案ブランチに留まります。** 最初の編集でブランチを作成した後、残りの各ファイルを同じブランチセレクターから開き直します。最後に PR の差分を確認します。4 つの別ブランチを作ると、レビュー可能な 1 つのパッケージではなく、4 つの不完全な変更になります。

## 提案文を確認する

**弱い表現の例:** 「エクスポートは 30 日間利用できるようになりました。」これは納品済みと説明し、合成データの範囲を省いています。レビュー中は提案文として書きます。

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**対象ファイルをすべてこの文面と比較します。** 候補では要件のリビジョンが進みます。設定は 30 日になります。runbook の最初の行は、ラボという制限を維持したまま 30 日になります。提案は 7 日を以前の値、リビジョン 1 をベースとして示し続けます。

**知らない制御を修正せず、差異について説明を求めます。** メンテナーのパッチが保護を弱めたりポリシーを削除したりする場合は、説明と別のレビューを依頼します。ワークフローの全行を理解しなくても、範囲外の変更を特定できます。

## レビューコメントに対応する

**レビュー例:** operations が、設定のロールバックでは削除されたファイルを復元しないと説明する文を求めました。同じブランチで下書きを更新し、変更された範囲をレビュー担当者に知らせます。最終レビューは古いチャットコピーではなく、変更後の提案を対象にします。

| レビューコメント | 貢献者の対応 |
|---|---|
| **除外事項が不足** | 文面を戻し、意図のレビューを依頼する |
| **古いソースリビジョン** | 新しい承認済みパケットを取得し、照合する |
| **マニフェスト不足** | メンテナーに保護されたベースの取得を依頼する |
| **無関係な制御変更** | レビュー前に分離または削除する |
| **未テストの実行時主張** | 正確なラボの制限に置き換える |

**質問は回答されるまで表示したままにします。** 根本の問題を直さずコメントだけを解決すると、有用な信号が消えます。別のレビュー担当者が会話全体を読まずに判断を追えるよう、回答に変更または証拠をリンクします。

## ブラウザー貢献の完了チェック

**別のメンテナーが推測せず実行できる Issue または PR を渡します。** ソースパケット、提案文、対象記録、除外事項、責任者の役割、未解決の質問を含めます。公開後は読み戻しを取得し、元の提案と分けます。

**自己チェック:** あなたのチャットを知らない人にパッケージを渡します。依頼値、承認値、公開値を区別してもらいます。マージ前に 30 日を納品済みと報告した場合は、パッケージのラベルを直します。この規律を職場トラックにも適用します。

| レビューゲート | 合格条件 |
|---|---|
| **ソースリビジョン** | 申告した全てのコミットまたはページバージョンがサンドボックスで開く。不明なリビジョンは不足のままにする。 |
| **除外事項** | 本番データ、バックアップ、法的保全は提案の外に残る。 |
| **質問** | 責任者またはソースに関する未解決の質問が Issue または PR に表示される。 |
| **承認の新しさ** | レビューは提案の最終リビジョンを指す。以前の承認は後の編集を対象にしない。 |

**ゲートに 1 つでも失敗があれば公開は保留です。** Issue だけの貢献者は結果をメンテナーに引き継ぎます。PR の貢献者は修正後に再レビューを依頼します。

## トラブルシューティングとロールバック

**編集権限がない:** Issue または承認済みフォークを使います。**架空のコミット参照:** 検証済みの証拠に置き換えて下書きを再レビューします。**編集より前の承認:** 新しい承認を依頼します。

**ロールバック:** マージしていない PR は証拠を残して閉じます。マージ済みのコンテンツでは、保護された復元案をメンテナーに依頼します。回復成功を装うためにベースラインを変更しません。

## 演習と自己チェック

**要件の記録を**新しいアシスタントに見せず、公開の推奨を求めます。

**期待される推論:** 権威ある証拠を求めるか、回答をスナップショットベースとラベル付けします。新しい読み取りが成功するまで公開はブロックされます。

## 主要な参考資料

- **ブラウザー手順:** [ファイルの編集](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)。
- **レビュー境界:** [保護されたブランチ](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。

## 次のステップ

**[Confluence と Jira の設定](/articles/ai-collaboration-confluence-jira-setup/)** に進み、職場システムでも同じ運用モデルを繰り返します。
