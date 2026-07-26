# ts-static-website

TypeScript と Vite を使ったモダンな静的サイトサービスです。

## 構成

- `app/` - Vite アプリケーションのソースと静的ファイル
- `infra/` - インフラ構成（必要に応じて）
- `deploy.yml` - GitHub Pages デプロイ構成

## デプロイ

このサービスは `.github/workflows/deploy.yml` の deploy ワークフローからデプロイされます。

`services/ts-static-website/deploy.yml` には次の設定があります:

- `type: github-pages`
- `site_dir: dist`
- `build_command: npm install && npm run build`

`app/` で `npm install` した後に `npm run build` を実行すると、`dist/` に公開用ファイルが生成されます。

### 使い方

```bash
cd services/ts-static-website/app
npm install
npm run build
```
