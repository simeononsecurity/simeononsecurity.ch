---
title: "GitHub AI コラボレーション: リポジトリとレビューの境界"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "GitHub を中心としたソースマップを作成し、ファイルの所有者を割り当て、レビュー済み AI 貢献のための保護された公開境界を構築します。"
genre: ["人工知能", "チームコラボレーション", "ソフトウェア工学"]
tags: ["AI コラボレーション講座", "GitHub リポジトリ", "ブランチ保護", "CODEOWNERS", "ソースマップ", "プルリクエストレビュー", "公開管理"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "サイバーセキュリティの作業環境で共有プロジェクトをレビューする専門家のイラスト"
coverCaption: ""
---

[AI コラボレーション講座に戻る](/ai-collaboration-course-start/)

**メンテナーはチャーター承認後に GitHub 中心の公開境界を構築します。** 要件、設定、ポリシー、ランブックを一つの使い捨てリポジトリに置きます。コントリビューターは Issue とプルリクエストで提案します。承認済みの事実を置く場所を定め、エージェントを接続する前に未レビューの変更をブロックします。

## 要点

- **保護された `main`** が公開境界です。
- **Issue** は提案作業を集めますが、ポリシーを承認しません。
- **CODEOWNERS** は適格なファイルレビュアーを割り当てます。
- **分離したユーザー** でレビューと拒否の制御を確認します。

## 始める前に

**前提条件:** [パイロット基盤](/articles/ai-collaboration-pilot-foundation/)、展開したラボ、リポジトリ管理者、製品および運用の別々のレビュアー。**所要時間:** 60 分。**難易度:** 中級。

**プランの境界:** GitHub は Free の公開リポジトリと、Pro、Team、Enterprise の非公開リポジトリで保護ブランチを文書化しています。公開リポジトリは合成コンテンツだけに使います。強制力を前提にする前に、保護ブランチのリファレンスで可視性とプランを確認してください。

**完了時の成果:** 保護された公開ブランチ、ファイル所有者、ソースマップ、証拠として記録した拒否テストがそろいます。

## リポジトリを作成する

1. README とデフォルトブランチ **`main`** を持つ **`export-service-lab` を作成します**。
2. **展開したラボをコピーします**。**`check.py`**、**`test_check.py`**、**`baseline/`** を保持します。ベースライン記録ファイルを初期記録としてルートにコピーします。
3. 基盤レジスターを使って **`docs/project-map.md` を作成します**。承認済み POL-01 を含む **`docs/policy.md`** を追加します。
4. チャーター承認、役割、ベースラインの決定、ステータスを含む **`docs/decisions/DEC-12.md` を作成します**。
5. 管理者として **ブートストラップをコミットします**。この初期例外を記録します。以後の貢献の前に保護を有効にします。

**Git Bash、macOS Terminal、Linux シェルでのローカルブートストラップ:** ブラウザーで GitHub にサインインし、新しいリポジトリを開いて **Code** を選び、HTTPS の clone URL をコピーします。使い捨ての作業ディレクトリで以下のコマンドを実行します。2 つのプレースホルダーパスを URL とダウンロードしたラボ ZIP のパスに置き換えます。URL にトークンを貼り付けないでください。

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

clone コマンドはリポジトリのディレクトリ名を指定します。`unzip` が使えない場合は、ファイルマネージャーで ZIP を展開し、リポジトリの README を残したまま内容をこのチェックアウトにコピーします。基盤パケットから `docs/project-map.md`、`docs/policy.md`、`docs/decisions/DEC-12.md` をテキストエディターで保存します。その後、次を実行します。

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git は新しいコミット ID を表示し、その後 `main` への push 成功を表示します。最後の short status は空になります。新しいブラウザー表示で GitHub リポジトリを開き、ファイルとコミット ID が `main` に表示されることを確認します。コミット URL をブートストラップの証拠として保存します。Git が作者情報を求めたら、コースハブのセットアップブリッジに従います。認証に失敗したら、GitHub がサポートする認証フローを使い、同じ push を再試行します。ブランチまたはリモートが間違っていたら、別の書き込みの前に `git branch --show-current` と `git remote -v` を調べます。保護がすでに有効で push が拒否されたら、ルールを回避せず、提案ブランチと PR を開きます。下のブラウザー専用手順はメンテナーが利用できます。

| 記録 | 場所 | 所有者 |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | ポリシー担当者 |
| **REQ-17** | `requirement.json` | 製品担当者 |
| **RUN-04** | `runbook.md` | 運用担当者 |
| **動作** | `config.json` | メンテナー |
| **決定** | `docs/decisions/` | プロジェクトリード |

**マップは値をコピーせず、場所をリンクします。** README はセットアップとマップに集中させます。保持要件を繰り返すと、一つのリポジトリ内でもドリフトが生じます。

## ファイル所有者を割り当てる

**`.github/CODEOWNERS` をローカルで生成します**。実際のサンドボックス用ハンドルを使い、先頭の **`@`** は入力しません。アカウントの身元は公開演習の証拠ではなく、非公開のラボで管理します。

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

GitHub が所有者を認識するには、所有者に書き込み権限が必要です。ブラウザーで CODEOWNERS ファイルの誤りを確認します。所有権ファイルとワークフロー定義も通常のコンテンツと同じように保護します。

**1 行に複数の名前があっても、全員の承認は必要ありません。** GitHub は一致するパスについて、適格な所有者 1 人の承認を受け入れます。要件パスとランブックパスには別々の指定所有者を使います。パイロットでは、最終提案に結び付いた製品所有者と運用所有者の証明も必要です。

## 公開を保護する

1. **Settings, Branches** を開き、**`main`** のブランチ保護ルールを追加します。この演習では ruleset と混ぜず、ブランチ保護の手順を一貫して使います。
2. **プルリクエスト**、2 件の承認レビュー、コードオーナーのレビューを必須にします。
3. 新しいコミット後に **古い承認を無効にし**、会話の解決を必須にします。
4. **Do not allow bypassing the above settings を有効にします。** force push と削除を無効にします。
5. 次のモジュールで最初の実行を終えたら **整合性チェックを追加します**。マージ前にブランチを最新にすることを必須にします。

**2 件の承認は数を強制しますが、業務上の役割の所属は強制しません。** CODEOWNERS はパス単位の所有者カバレッジを追加します。メンテナーは 2 つの役割証明も確認します。この手続き上の制御を明示的に記録し、自動的な 2 役割の強制と表現しないでください。

**管理者は引き続き設定を管理します。** テストの前後でルールを記録します。コントリビューターの拒否を示すために、エージェントへ管理者権限を与えたり、特権トークンを使ったりしないでください。

## 境界を確認する

| 試行 | 期待される結果 |
|---|---|
| **コントリビューターがブランチを送信** | 提案は許可される |
| **コントリビューターが直接公開** | 保護された公開は拒否される |
| **レビュアー 1 人が承認** | レビューしきい値でマージがブロックされる |
| **レビュー後に新しいコミット** | 新しい承認が必要 |
| **機密ファイルに所有者カバレッジがない** | 公開前に修正する |

**経路の確認にはコントリビューターのブラウザーセッションを使います。** GitHub の Web エディターは保護された **`main`** を編集しません。ブランチ作成を促す表示は、サポートされるブラウザー経路を示します。直接 push がサーバーに拒否された証拠にはなりません。プラットフォーム拒否の証拠には、承認済みのローカル Git アクセスを持つコントリビューターに保護された **`main`** への無害な直接 push を試してもらい、サーバーの応答を保存します。ローカルアクセスがなければ、この拒否テストを Blocked と記録します。

**拒否後に `main` を読み取り**、リビジョンが変わっていないことを確認します。アクターの役割、試行した操作、結果、ソースリビジョンを記録します。アシスタントが公開しないと約束することは行動上の証拠であり、プラットフォーム権限のテストではありません。

**直接 push のテストには、コントリビューター自身の認証済みローカルクローンを使います。** メンテナートークンでは別の身元をテストすることになります。この例示応答は、保存すべきサーバー証拠の種類を示します。正確な文言はリポジトリのルールで異なります。

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**ローカル Git 認証が利用できない場合、サーバー側の拒否を Blocked と記録します。** ブラウザーのブランチプロンプトを経路の証拠として保持し、メンテナーに別のコントリビューターテストを手配してもらいます。経路プロンプトを直接 push の拒否として採点しないでください。

## 役に立つソースマップを作る

**ソースマップはルーティング文書です**。要件文書の 2 つ目ではありません。チャットから来た人が、競合する要約から選ばずに現在の意図、実装された動作、運用手順を見つけられるようにします。

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**現在の保持値を各マップ項目に書かないでください。** 「7 日」と書いたマップは、PROP-042 後に同期する別の値になります。マップには安定した識別子と場所を置き、値は権威ある記録から読み取ります。

**マップの変更をルーティング変更として保護します。** REQ-17 を下書きファイルへ向けると、承認済み要件が変わらなくてもソースの選択が変わります。マップを変更するたび、宛先、所有者、権限の範囲をレビューします。

## ベースラインと候補を分ける

**リポジトリのルートにはアクティブなラボ記録があります。** ダウンロードした **`baseline/`** ディレクトリは教材です。後続のすべての PR で保護されたベースラインになるわけではありません。レビュー済みの作業が **`main`** に到達したら、保護されたルート記録が次の提案の基準になります。

| 場所 | 目的 | PROP-042 中に編集するか |
|---|---|---|
| **ルートの要件/設定/ランブック** | ブランチ上の提案中のアクティブ記録 | はい、レビュー済みの変更で |
| **`baseline/`** | 元のオフライン演習フィクスチャ | いいえ |
| **分離した信頼済みワークツリー** | 取得した保護済みルート記録 | いいえ |
| **`context.json`** | 取得した基準バイトの証拠 | 調整後に再生成 |

**制御の変更と保持の変更を分けます。** まずチェッカーとレビュー規則をブートストラップします。その後、7 日から 30 日への変更を提案します。ポリシー、ワークフロー、値の変更を混ぜると、修復された制御と回避された制御を見分けにくくなります。

## 完全な変更をレビューする

**PR の説明を受け入れる前に Files changed を開きます。** 説明は作成者の意図を示します。diff は送信された変更を示します。PROP-042 では、要件リビジョン、範囲の除外、設定、ランブック、提案の基準、マニフェスト証拠を確認します。

1. **製品レビュー:** 30 日の意図と変わっていない除外を確認します。
2. **運用レビュー:** ランブックが提案された設定と一致し、実行時の制限を保持していることを確認します。
3. **メンテナーレビュー:** JSON、ソース取得、チェック結果、無関係な変更を確認します。
4. **制御レビュー:** マップ、ポリシー、CODEOWNERS、ワークフローの変更を個別に確認します。

**緑のチェックは無関係な削除を説明しません。** ブランチが保持期間を変更しながらポリシー文書を削除するなら、別の提案または特定所有者のレビューを求めます。範囲を限定すると、レビュー対象を理解しやすくなります。

## 拒否テストを診断する

**証拠の各行には、試行した操作を 1 つだけ書きます。** 「コントリビューターが失敗した」では曖昧です。通常の書き込み権限がない、ブラウザーの制限に遭遇した、意図したブランチ規則に当たった、という可能性があります。これらは異なる境界を示します。

| 観察 | 解釈 | フォローアップ |
|---|---|---|
| **どのブランチも作れない** | 貢献アクセスがない | 承認済み Issue または fork 経路を使う |
| **ブランチは作れるが main に公開できない** | テストした公開経路が制限されている | 変わっていない main のリビジョンを取得する |
| **1 件のレビューでマージがブロックされる** | レビュー数がテストした PR に適用される | 役割固有の証拠を追加する |
| **管理者がルールを無視して公開する** | テストした身元が境界を回避している | 回避設定と権限を確認する |

**共有コース証拠にアカウント情報を出さず、役割と操作を記録します。** アクターのネイティブな記録はレビュアーが非公開で利用できるようにします。ルール設定、試行操作、拒否、結果として保護されたリビジョンを一緒に記録します。

## リポジトリ完了チェック

**別のコントリビューターが自力でたどれるリポジトリを提供します。** README はマップを指し、マップは権威ある記録を解決し、所有者カバレッジは機密パスを含み、保護は **`main`** に適用されます。許可された提案と拒否された公開試行を 1 件ずつ保持します。

**設定だけで強制されたと主張しないでください。** 設定は意図した構成を示します。サンドボックスでの試行は、特定の役割と経路で観察した動作を示します。両方をエージェントと Actions のレッスンに持ち込みます。

## トラブルシューティングとロールバック

**所有者リクエストがない:** 書き込み権限とベースブランチのパスカバレッジを確認します。**保護がない:** プランと可視性を確認します。**マージが有効なまま:** ルールの対象、回避設定、レビュー数を確認します。

**ロールバック:** 未マージの提案を閉じ、ラボの自動化を無効にします。マージ済みのラボ内容は別のレビュー済み PR で取り消します。使い捨てリポジトリを削除する前に証拠を保存します。失敗したテストを終えるために保護を弱めないでください。

## 演習とセルフチェック

コントリビューターとして **`docs/policy.md` の編集を提案します**。メンテナーだけの承認でポリシー所有者の承認が成立するかを判断します。

**期待される考え方:** レビュー数だけでは権限を示しません。パスにはポリシー所有者のカバレッジと現在の役割レビューが必要です。強制されていない役割固有の要件を手続き上の制御として列挙します。

## 主な参考資料

- **プランとレビューの制御:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。
- **所有者の適格性:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)。
- **ブラウザーからの貢献:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)。

## 次のステップ

ソース証拠を実行可能なチェックにつなぐため、**[エージェントアダプターと Actions](/articles/ai-collaboration-github-agents-actions/)** に進みます。
