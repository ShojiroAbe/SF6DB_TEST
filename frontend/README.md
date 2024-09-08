# フロントエンド（React,Next.js）メモ

## Next.js開発者「Vercel」のDockerfileの例
https://github.com/vercel/next.js/blob/canary/examples/with-docker/Dockerfile

依存関係のインストール (deps ステージ)
ビルドプロセス (builder ステージ)
実行環境の準備 (runner ステージ)

これには複数のビルドプロセスで構成された高度な構成のため、本開発（勉強）には特に必要ない

本件で環境構築に使用した参考サイト
How to use Next.js with Docker and Docker compose a beginner's guide
https://geshan.com.np/blog/2023/01/nextjs-docker/

## docker-compose up --build
このコマンドは、コンテナを起動する際に 必ずイメージを再ビルド します。
もし Dockerfile に変更があったり、ファイルが追加・変更された場合、これを使うとその変更を反映した状態でコンテナが起動します。
再ビルドするので、時間がかかることがあります。

### 使うべきタイミング:
Dockerfile の変更があった場合
docker-compose.yml の変更があった場合
新しい依存関係を追加した場合（package.json などの依存関係ファイルが更新された場合）

※
docker-compose up --build　で立ち上がらないけど
docker compose -f "docker-compose.yml" up -d --build frontend
ならfront立ち上がる

-----------------------------------------------------------

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
