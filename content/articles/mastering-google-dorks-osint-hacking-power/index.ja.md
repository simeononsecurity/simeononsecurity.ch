---
title: "Google Dorksを使いこなす"
date: 2023-12-04
lastmod: 2026-11-14
toc: true
draft: false
description: "許可を得たOSINTでGoogle検索演算子を使う方法を、クエリ例、調査範囲の制限、防御目的の報告手順とともに紹介します。"
genre: ["SEO", "サイバーセキュリティ", "オンライン検索", "Google Dorks", "オープンソースインテリジェンス", "ハッキング手法", "デジタルスキル", "ウェブ検索", "インターネットセキュリティ", "データ発見"]
tags: ["Google Dorks", "検索演算子", "オンライン検索", "サイバーセキュリティ", "オープンソースインテリジェンス", "ハッキング手法", "高度な検索", "ウェブ検索", "効率的な検索", "デジタルスキル", "データ発見", "オンラインリサーチ", "Google Hacking", "情報検索", "簡単な検索", "キーワード最適化", "OSINT", "ハッキングツール", "インターネットセキュリティ", "データプライバシー", "オンライン調査", "ウェブクエリ", "デジタルフォレンジック", "倫理的ハッキング", "情報セキュリティ", "オンラインプライバシー", "脆弱性スキャン", "データ分析", "ハッカー向けツール"]
cover: "/img/cover/cartoon-magnifying-glass-uncovering-data.webp"
coverAlt: "漫画風の虫眼鏡が隠れたデジタルデータを見つけています。"
coverCaption: "Google Dorksでデジタル調査のスキルを磨きましょう。"
canonical: ""
---

**ハッカーとOSINTのためのGoogle Dorks**

サイバーセキュリティやオンライン調査では、適切なツールと手法が大きな違いを生みます。Google Dorksは、ハッカーにもオープンソースインテリジェンス（OSINT）に携わる専門家にも役立ちます。このガイドでは、Google Dorksとは何か、どのように使われるか、ハッキングやOSINTでどんな意味を持つかを説明します。

## はじめに

**Google DorksはGoogle HackingやGoogle Dorkingとも呼ばれる、専用の検索クエリです**。Google検索の機能を活用し、通常の検索では見つからないことがある特定の情報や脆弱性を探します。クエリを細かく指定することで、さまざまな目的に役立つデータを見つけられます。

### Google Dorksの基本

使い方を見る前に、基本的な演算子を確認しましょう。

- **intitle:** タイトルに指定した語を含むページを検索します。
- **inurl:** URLに指定した語を含むページを検索します。
- **filetype:** ファイル形式で結果を絞り込みます。
- **site:** 特定のウェブサイトまたはドメインに検索対象を限定します。
- **cache:** ウェブページのキャッシュ版を取得します。
- **link:** 指定したURLへリンクするウェブページを探します。
- **related:** 指定したURLに関連するウェブページを表示します。

## ハッカーのためのGoogle Dorks

{{< youtube id="u_gOnwWEXiA" >}}

### 脆弱性を見つける

**ハッカーはGoogle Dorksを使って、ウェブサイトやアプリケーションの脆弱性を探します**。クエリを工夫すると、ディレクトリが公開されたサイト、開放ポート、保護されていないファイルを見つけられます。たとえば `inurl:admin/login` は、セキュリティの弱いログインページを示し、不正アクセスにつながる可能性があります。

### 公開されたデバイスを特定する

**Google Dorksはインターネット上に公開されたデバイスの特定にも使えます**。`intitle:"webcamXP 5"` のようなクエリは、認証なしでアクセスできるウェブカメラを見つける手がかりになります。これはプライバシーとセキュリティ上の懸念につながります。こうした発見は、機器の所有者がデバイスを保護する必要性を示しています。

### 情報を収集する

**OSINTの専門家はGoogle Dorksを情報収集に活用します**。組織、従業員、潜在的なセキュリティ上の弱点に関する情報を探せます。`site:example.com filetype:pdf` のようなクエリは、特定の組織に関係するPDF文書を見つけ、機密情報が含まれている可能性を明らかにします。

## OSINTで使うGoogle Dorks

{{< youtube id="61WnPi7k6Yk" >}}

### オンライン上の存在を調べる

**OSINTアナリストはGoogle Dorksで対象のオンライン上の存在を調べます**。個人や組織に関する情報を検索すると、プロフィールを作成し、潜在的な脅威を見つける手がかりになります。`site:linkedin.com "John Doe"` は、個人の職歴を把握する助けになります。Michael Bazzellの著書[Open Source Intelligence Techniques](https://amzn.to/3LMZHq7)には、役立つOSINTのヒントが数多くあります。詳しく学びたい方におすすめします。

### 脅威アクターを調査する

**OSINTは脅威アクターやサイバー犯罪者の調査で重要な役割を果たします**。アナリストはGoogle Dorksを使って、ハッカーが活動について話し合うオンラインフォーラム、チャットログなどの情報源を探せます。これらは、法執行機関やサイバーセキュリティの専門家が脅威を特定し、被害を抑える助けになります。

## OSINTの倫理的な範囲

OSINTによる収集は、合法的な目的と公開情報に限定してください。アカウントや文書を個人に結び付ける前に、その本人であることを確認してください。より少ない情報で目的を達成できる場合は、機微な個人データを集めないでください。他の確認者が結果を再現できるよう、情報源のURL、アクセス日、確度に関するメモを保存してください。

防御目的で情報を開示する場合は、公開されているセキュリティ窓口を通じて資産の所有者に連絡してください。露出を確認するために必要な範囲を超えて調査しないでください。[Google Searchヘルプ](https://support.google.com/websearch/answer/2466433)では、対応する演算子が説明されています。[CISAの脆弱性開示ガイダンス](https://www.cisa.gov/vulnerability-disclosure-policy)では、公開された問題をより安全に報告する方法が紹介されています。

## まとめ

Google Dorksは、ハッカーにもOSINTの専門家にも役立つ強力な検索クエリです。悪用される可能性がある一方、脆弱性の発見や情報収集にも活用できます。セキュリティとデジタル調査を支えるため、Google Dorksは責任を持って倫理的に使ってください。

## 参考資料

1. [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
2. [Google検索演算子: 検索エンジンを使いこなす](https://support.google.com/websearch/answer/2466433)
3. [Open Source Intelligence Techniques by Michael Bazzell](https://amzn.to/3LMZHq7)
4. [Google Search Operators: A Complete Guide](https://ahrefs.com/blog/google-advanced-search-operators/)
