---
name: github-pages-ts-static-site
description: GitHub Pages へ TypeScript + Vite ベースの静的サイトをデプロイするためのスキル。GitHub Actions の workflow_dispatch による手動デプロイを前提とし、`services/ts-static-website/app` をビルドして `dist/` を公開する構成を扱う。
---

# GitHub Pages TypeScript/Vite 静的サイト運用スキル

## このスキルの前提

- サイトは `services/ts-static-website/app` に Vite + TypeScript で構築される
- ビルド後の出力は `services/ts-static-website/dist` に置かれる
- デプロイは `.github/workflows/deploy.yml` から行う
- 実行時には `PAGES_TOKEN` のような Pages 有効化可能なトークンが必要になる場合がある

## ディレクトリ構成

```
services/ts-static-website/
├── app/
│   ├── index.html
│   ├── style.css
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── src/
│       └── main.ts
├── deploy.yml
├── README.md
└── .ai/
    └── SKILL.md
```

## このスキルの用途

- `ts-static-website` の新規構築
- Vite/TypeScript のビルド設定の修正
- GitHub Pages 用デプロイワークフローの調整
- `dist/` の公開先とビルドフローの整合性確認

## ワークフロー

1. `services/ts-static-website/deploy.yml` を読み込む
2. `build_command` が指定されていれば実行する
3. `services/${{ inputs.service }}/${{ steps.cfg.outputs.site_dir }}` を GitHub Pages へアップロードする
4. `actions/deploy-pages@v4` で公開を完了する

## 重要なポイント

- GitHub Pages は同じリポジトリ内で `static-website` と `ts-static-website` を同時に公開できない。どちらか一方が最終公開コンテンツになる
- `ts-static-website` をデプロイすると `https://hgssnk.github.io/static-website/` の内容が上書きされる
- `tsconfig.json` と `vite.config.ts` の `base` 設定は、Pages のサブパス公開に適した値にする必要がある
- `deploy.yml` の `working-directory` や `build_command` はサービスルートを基準に構成する

## よくある修正対象

- `deploy.yml` の `service` 選択肢に `ts-static-website` を追加
- `services/ts-static-website/deploy.yml` に `build_command` を定義
- `vite.config.ts` に `base: './'` を設定
- `README.md` に公開先を明記

## 使い方例

- 新規サイトを追加するとき: `services/ts-static-website/app` を編集し、`services/ts-static-website/deploy.yml` を整備する
- デプロイ先を確認するとき: `README.md` の公開先 URL をユーザーに伝える
- デプロイエラーが出たとき: `PAGES_TOKEN` の権限と`workflow_dispatch`の設定をまず疑う
