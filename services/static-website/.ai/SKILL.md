---
name: github-pages-static-site
description: GitHub Pagesでプレーンな静的サイト(HTML/CSS/JS、ビルド不要)を新規構築・公開し、公開後のコンテンツ更新や再デプロイも行うためのスキル。ユーザーが「サイトを作って公開したい」「GitHub Pagesにデプロイして」「ページの内容を更新して」「静的サイトをGitHubで公開したい」のように言った場合、Netlify/Vercelや静的サイトジェネレータ(Hugo/Jekyll/Astro等)の指定がなければ必ずこのスキルを使うこと。このスキルはGitHub Actionsのworkflow_dispatch(手動実行)によるデプロイを前提としており、pushしただけでは公開されない点が最重要の注意事項。
---

# GitHub Pages 静的サイト運用スキル

## このスキルが前提とする構成

- サイトの中身はプレーンなHTML/CSS/JS。ビルドステップは持たない
- デプロイはGitHub Actionsのワークフローで行が、**push時の自動デプロイではなく、workflow_dispatchによる手動実行**
- リポジトリ内の`site/`フォルダの中身をそのまま配信する

この前提を選んでいる理由: pushのたびに勝手に公開されると、作業途中の内容が意図せず外部に出てしまうことがある。手動実行にしておけば「確認してから公開する」というワンクッションを挟める。

## ディレクトリ構成(このスキルが作るリポジトリの形)

```
repo/
├── site/
│   ├── index.html
│   ├── style.css
│   └── (画像などの静的アセット)
├── .github/
│   └── workflows/
│       └── deploy.yml
└── .nojekyll
```

`.nojekyll`は必須。これが無いとGitHub Pages側でJekyll処理が走り、`_`で始まるファイルやフォルダが無視されてしまう。

## ワークフロー1: 新規サイトを立ち上げる

1. `scripts/scaffold_site.sh <対象ディレクリ>` を実行し、上記のディレクトリ構成を生成する
2. `assets/templates/index.html` と `assets/templates/style.css` を元に、ユーザーの要望に合わせて内容を書き換える
3. `git init` してGitHubにリポジトリを作成し、push する(まだGitHubリポジトリが無い場合は `gh repo create` の利用も検討)
4. リポジトリの Settings > Pages で、Source を **「GitHub Actions」** に変更する。この手順の詳細は `references/setup_guide.md` を参照
5. 初回公開のために `scripts/trigger_deploy.sh <owner/repo> [branch]` を実行し、ワークフローを手動実行する
6. `gh run watch` などでデプロイの完了を確認し、公開URLをユーザーに伝える

## ワークフロー2: 既存サイトのコンテンツを更新する

1. `site/` 配下のファイルを編集する
2. commit して push する
3. **ここが最重要**: pushしただけではサイトは更新されない。`scripts/trigger_deploy.sh <owner/repo> [branch]` を実行して手動でデプロイをトリガーする
4. デプロイが終わるまでユーザーに「公開までもう一手順ある」ことを明確に伝える。うっかり「pushしたので反映されているはずです」と言わないこと

## カスタムドメインを使いたい場合

`site/CNAME` ファイルにドメイン名を1行だけ書いて配置する。DNS側の設定(CNAMEレコード等)はユーザー側の作業になるため、その旨も案内する。

## トラブルシューティング

反映されない・404になる等の相談を受けたら、まず以下を疑う:

- Settings > Pages の Source が「GitHub Actions」になっているか(Deploy from a branchのままだと今回の構成は動かない)
- `.nojekyll` が `site/` の外(リポジトリのルート、または配信対象のアーティファクトのルート)に正しく置かれているか
- ワークフローがそもそも実行されたか(`gh run list` 確認)
- ワークフローの`permissions`に `pages: write` と `id-token: write` が入っているか

より詳しい手順は `references/setup_guide.md` を参照すること。
