# static-website

GitHub Pages で公開される静的サイトです。

公開先:
https://hgssnk.github.io/static-website/

## 構成

- `app/` - 公開対象の静的コンテンツ
- `infra/` - インフラ構成（必要に応じて）
- `.ai/` - AIコンテキスト・ドキュメント
- `deploy.yml` - デプロイ構成

## デプロイ

このサービスは `.github/workflows/deploy.yml` から GitHub Pages にデプロイされます。

必要な設定:
- `services/static-website/deploy.yml` に `type: github-pages` と `site_dir: app` が設定されていること
- リポジトリの `Settings > Secrets and variables > Actions` に `PAGES_TOKEN` を登録し、Pages を有効化できる権限を持ったトークンを設定すること
