---
title: "AIコラボレーション・キャップストーン: GitHub、Confluence、Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "GitHub-first と Confluence/Jira のワークフローで合成保持期間の変更を実施し、失敗の証拠と独立レビューを用意します。"
genre: ["人工知能", "チームコラボレーション", "ソフトウェア工学"]
tags: ["AIコラボレーションコース", "保持期間の提案", "GitHubレビュー", "Confluence Jiraワークフロー", "失敗マトリクス", "独立受け入れ"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "サイバーセキュリティの作業空間で共有プロジェクトをレビューする専門家のイラスト"
coverCaption: ""
---

[AIコラボレーションコースに戻る](/ai-collaboration-course-start/)

**PROP-042 を2回実施します。** 1回目は GitHub-first、2回目は GitHub と Confluence/Jira を使います。あなたが変更を提案し、別の担当者がレビューし、権限を持つ公開担当者が適用します。前のレッスン後に分離した合成サンドボックスを使います。キャップストーンでは、アシスタントの文章品質ではなく、却下、復旧、独立した引き継ぎを含む手順全体をテストします。

## 要点

- **1つの共有変更**で、2つの権限モデルを比較します。
- **否定テスト**は、成功した配信と同じほど重要です。
- **証拠パッケージ**は独立レビューを支えます。
- **ラボ完了**は本番展開の許可ではありません。

## 始める前に

**前提条件:** 先行する[コースモジュール](/ai-collaboration-course-start/)、承認済みのサンドボックスアクセス、別々のレビュー担当者。**計画時間:** 複数セッションで8から12時間。独立レビューの時間は別です。実時間はアカウント設定と修復作業に左右されます。**難易度:** 上級。

**必要な成果物:** 憲章、マップ、ポリシー、アダプター、ベースライン、マニフェスト、固定した提案、所有者レビュー、台帳、復旧記録、引き継ぎ。計画に依存する権限が欠けている場合は完了をブロックします。合格と仮定してはいけません。

**テスト前に、トラックごとに証拠ディレクトリを1つ用意します。** レビュー担当者はチャットの要約に頼らず、実行者、ソースのリビジョン、試行した操作、観測結果、最終状態を特定できる必要があります。

## 2つのベースラインを確立する

1. **分離した実行を作成します。** 名前は GitHub-first と Mixed にします。リビジョンとレビューを分けます。
2. **7日間のベースラインを復元します。** 各トラックの承認済み手順を使い、得られたリビジョンを記録します。
3. **拒否制御を確認します。** 投稿者アカウントと除外ユーザーアカウントを使います。
4. **現在のコンテキストを記録します。** アダプターとポリシーが一致することを確認します。
5. **範囲を宣言します。** 30日間の合成エクスポート保持とし、実データ、バックアップ、法的保全を除外します。

**PROP-042 は相関ラベルであり、再利用できる承認ではありません。** 実行ごとに固有の固定リビジョンとソース証拠が必要です。レポートに実行IDを入れます。

## GitHub-first で配信する

**GitHub のレッスンに従って Issue と候補 PR を開きます。** 要件、設定、提案、ランブックを一緒に変更します。保護されたベースを記録し、信頼できるチェックを実行し、最終コミットでプロダクトと運用のレビューを取得します。

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**サンドボックスから実際の参照を入れます。** この概要は想定される対応関係であり、完了した証拠ではありません。メンテナーはレビュー後にのみマージし、その後 **`main`** を独立して読み直します。最終記録をリンクしてから Issue を閉じます。

## Mixed トラックを配信する

**Confluence のバージョンを読み、Jira の提案を固定します。** 2人の所有者レビューを取得します。配信待ちの要件を公開し、設定をマージし、ランブックを公開し、Done にする前にすべてのシステムを読み直します。

**各公開を記録します。** ページバージョン、コミット、または遷移の証拠を残します。リポジトリ内の要件コピーはスナップショットです。ローカルチェッカーは Confluence の現在の権限を証明しません。

| 比較 | GitHub-first | Mixed ワークプレース |
|---|---|---|
| **要件** | 保護されたリポジトリのレビュー | Confluence 所有者がレビューした公開 |
| **調整** | Issue/PR | 固定された Jira 提案 |
| **公開単位** | リポジトリのマージ | 個別ページの書き込みとマージ |
| **鮮度** | 保護されたコミット | ページバージョンとコミット |
| **復旧** | レビュー済みの revert/補償 | 台帳に基づく補償 |

**所有権の要件でワークフローを選びます。** GitHub-first はシステム間の調整を減らします。Mixed は作業場所を保ち、公開とアクセスのチェックを追加します。

## 失敗マトリクスを実行する

| ケース | 注入 | 必要な観測証拠 |
|---|---|---|
| **承認済み変更** | レビュー済みの30日提案を送る | 一貫した読み戻しとレビュー |
| **古いコンテキスト** | 記録後にソースを変更する | 拒否、調整、再承認 |
| **権限外の書き込み** | 投稿者が公開する | 拒否とリビジョン不変 |
| **競合** | Jira は60、Confluence は7とする | ブロックと所有者の調整 |
| **部分公開** | 1回の書き込み後に中断する | 保留台帳と復旧 |
| **アクセス拒否** | タスクの読み取り権限を外す | 保護テキストも公開もない |
| **復旧** | 承認済みの完了またはバックアウト | 新しいレビュー済みリビジョン |
| **引き継ぎ** | 新しいセッションにマップと台帳だけ渡す | 新しい読み取りと正しい次の操作 |

**システム間の競合は Mixed に属します。** GitHub-first では、承認済みファイルと異なる Issue 説明をテストします。他の該当ケースは両トラックで実行します。ローカルバリデーターの失敗は、ライブの権限証拠の代わりになりません。

| ケースと証拠ファイル | GitHub-first の実行 | Mixed の実行 |
|---|---|---|
| **承認済み変更** `01-approved-change.md` | レビュー済み PR と読み戻し | レビュー済みページ、マージ、台帳 |
| **古いコンテキスト** `02-stale-context.md` | 記録後に保護ベースを変更 | 記録後に権限ページを変更 |
| **権限外の書き込み** `03-unauthorized-write.md` | 投稿者の直接 push を拒否 | ページ編集と遷移を拒否 |
| **競合** `04-conflict.md` | Issue が承認済みファイルと異なる | Jira の文章が Confluence と異なる |
| **部分公開** `05-partial-publication.md` | マージまたは読み戻し前に停止 | ページ書き込み後に停止 |
| **アクセス拒否** `06-access-denial.md` | 保護されたリポジトリソースを渡さない | 制限ページからユーザーを除外 |
| **復旧** `07-recovery.md` | レビュー済みの revert または完了 | 台帳に基づく補償 |
| **引き継ぎ** `08-handoff.md` | 新セッションが保護ファイルを読む | 新セッションが対応するページと台帳を読む |

**各ファイルをテスト前に作成します。** 期待結果、観測結果、実行者の役割、初期と最終のリビジョン、ネイティブ証拠の参照、レビュー担当者の判断を記録します。ブラウザ経路のプロンプトは直接 push の拒否を証明しません。2つのトラックのディレクトリを分けます。

**期待結果と観測結果を分けます。** 各ケースに実行ID、役割、初期リビジョン、試行操作、期待、観測、結果リビジョン、レビュー判断を記録します。共有レポートから資格情報とアカウント識別子を削除します。

## 完了を評価する

**合格には、該当する各行の観測証拠**と独立した受け入れが必要です。レビュー担当者は権限、ソースの鮮度、役割レビュー、部分公開、引き継ぎの再構成、整合性ログを確認します。

**権限外の公開、拒否されたテキストのモデル到達、変更されたベースの無言上書きがあれば即時に失敗です。** 修正した制御が再テストに合格するまで作業をブロックします。失敗を平均して有利な点数にしません。

**完了とブロックのケース、拒否した古い提案、拒否された書き込み、復旧、レビュー時間を測定します。** 提案された結果は観測されるまで期待結果です。付属する10個のユニットテストは整合性を対象にし、ライブテナントの安全性を対象にしません。

## 2つの実行を計画する

**トラック間で承認を再利用しません。** 変更値は同じでも、ソースの場所、取得したリビジョン、権限、公開順序は異なります。各実行に固有の証拠ディレクトリとレビュー・パケットを用意します。

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**これらの名前は整理例です。** 提供されたアーカイブファイルではありません。実際の証拠は承認済みサンドボックスに非公開で保存します。共有提出物は役割ラベルと編集済み参照を使い、レビュー担当者はネイティブ記録へのアクセスを保持します。

**失敗を実行する前にテスト観察者を決めます。** 投稿者が操作を試します。観察者が初期状態、結果、最終状態を記録します。レビュー担当者は後で証拠が主張を支えるか判断します。独立受け入れを示唆せず、役割の重複を開示します。

## 失敗を分離して実行する

**ケース間で検証済みのレビュー状態へ戻します。** ソースのずれ、アクセス取り消し、ランブックの不一致を同時に注入すると、どの制御が提案を拒否したのか分からなくなります。1回の実行につき1つの失敗にすると、結果の理由を追跡できます。

1. **初期状態を記録します。** ソースリビジョン、設定、配信状態、実行者の役割。
2. **1つの合成注入を適用します。** 承認済みのテスト経路で関連する条件を1つ変更します。
3. **範囲を限定した操作を試します。** 検証、読み取り、公開、引き継ぎ。
4. **観測を記録します。** 実際の出力とソースの結果状態。
5. **レビューを通して修復します。** 制御を戻す前に失敗証拠を保存します。
6. **成功ケースを繰り返します。** 修正後のワークフローが許可された作業を配信できることを確認します。

**計画した失敗も失敗の観測です。** 権限外の公開を、制御を調べる意図があったから成功テストと呼んではいけません。テストは欠陥を見つけることに成功しましたが、公開境界は失敗しており、修復が必要です。

## 混合結果を解釈する

**説明用の証拠パッケージ:** ローカル整合性は合格し、プロダクトと運用が固定パッケージをレビューし、要件公開は成功し、ランブック編集権限は拒否されました。設定はまだマージされていません。Jira は Blocked のままです。

| 主張 | 判定 | 理由 |
|---|---|---|
| **候補記録は一致する** | ローカルチェックで支持 | 提供された記録は比較に合格 |
| **所有者は意図と運用を受け入れた** | ネイティブの固定レビューが必要 | 役割ラベルだけでは不十分 |
| **30日配信が完了した** | 未支持 | 必要な公開手順が保留中 |
| **すべての役割で権限境界が機能する** | 未支持 | 拒否された操作の範囲が限定的 |
| **復旧担当者が行動すべき** | 次の手順として支持 | 部分配信にはレビュー済み判断が必要 |

**期待される判断:** 実行を未完了のままにし、現在のソースを確認し、適切な所有者の判断を求めます。権限を弱めたり、スナップショットチェックをライブ公開の証拠と説明して完了扱いにしません。

## 独立した読者とレビューする

**レビュー担当者には結論だけでなく、出来事を再構成してもらいます。** 承認済みベースライン、固定提案、所有者の判断、結果リビジョン、失敗した試行、修復、残るギャップを、あなたの説明なしに見つけられる必要があります。

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**要件を個別に採点します。** 証拠参照とともに Supported、Failed、Blocked、Not run を使います。整合性、承認、権限、復旧、引き継ぎは別々の要件です。ローカルテストがすべて緑でも、ライブの公開境界の失敗を埋め合わせません。

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported は、該当するすべてのケースで観測証拠をレビュー担当者が確認したことを意味します。** 観測された制御失敗には Failed、アクセスまたは制御の不足には Blocked、未実行のケースには Not run を記録します。各ネイティブ参照を名前付き証拠ファイルに残します。

**コース合格条件:** GitHub-first と Mixed の両トラックを完了します。各トラックで、上記の該当する8ケースすべてが Supported でなければなりません。Failed の境界やネイティブな読み戻しの欠落はトラックをブロックします。有料プランやテストIDがない場合は、推測した合格ではなく Blocked です。1つのトラックだけ完了した場合は、コース完了ではなく文書化した部分結果です。

**編集済みモデルパッケージ、説明用のみ:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

説明用の参照をすべて、サンドボックスで観測した成果物に置き換えます。Mixed についても固有のソースバージョンとレビューでパッケージ全体を繰り返します。レビュー担当者は Mixed パッケージにコピーされた GitHub 承認があれば拒否します。

## 範囲を限定した判断を書く

**有用な締めの判断は、制限のない展開ではなく次のパイロットを示します。** 同じ役割と直接参照経路で別の合成エクスポート設定を選び、実データと自動公開を範囲外にする例があります。

| 判断要素 | 必須の詳細 |
|---|---|
| **範囲** | 次の1つの変更と明示的な除外 |
| **証拠** | 支持されたケースと未解決の失敗 |
| **制御** | プラットフォーム強制要件と手続き要件を分離 |
| **所有者** | 残るギャップごとの責任役割 |
| **実行時ギャップ** | 未テストの削除または展開動作 |
| **停止条件** | 欠けたアクセス、変わった権限、権限外の公開 |

**完了チェック:** 2つの実行パッケージが独立した再構成に耐え、該当する失敗ケースに観測証拠があり、未解決の制御が見える状態です。GitHub トラックだけが完了した場合、Mixed も同じ動作をすると仮定せず、部分的なコース完了として報告します。

## トラブルシューティングとバックアウト

**成功経路だけの証拠:** 拒否と中断のテストを再実行します。**役割の重複:** 開示して別ユーザーで再実行します。**計画上の制御不足:** 停止し、承認済みサンドボックスを取得します。

**バックアウト:** レビュー済み PR と Confluence 編集でベースラインを戻し、一時的な統合を取り消し、Jira の証拠をアーカイブし、証拠保持後に所有者が承認した合成クリーンアップを行います。復旧履歴を保持します。

## ロールアウト判断を作成する

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**期待される判断:** 合成環境での成功は、別の範囲限定パイロットを支えます。本番には、実データ、展開、プロバイダーの取り扱い、実行時動作について別の承認が必要です。アシスタントの成功した回答は、展開の許可ではありません。

## 主な参照

- **リポジトリ制御:** [保護されたブランチ](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。
- **ワークプレースアクセス:** [Confluence の権限](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/)。
- **配信制御:** [Jira 権限スキーム](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/)。

## 次のステップ

**[コースハブ](/ai-collaboration-course-start/)に戻り、欠けている制御を確認します。** 次のパイロットを選ぶ前に、実装を[フレームワーク記事](/articles/one-source-many-tools-ai-collaboration-framework/)と比較します。
