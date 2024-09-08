# ==================================================
# 開発のレイヤー
# ==================================================
FROM node:18-alpine AS dev
WORKDIR /app/frontend

COPY ./frontend .

CMD ["npm", "run", "dev"]

# ==================================================
# パッケージのインストールのレイヤー
# ==================================================
FROM node:18-alpine AS deps
WORKDIR /base

COPY package.json package-lock.json ./
RUN  npm install --production

# ==================================================
# アプリのビルドレイヤー
# ==================================================
FROM node:18-alpine AS builder
WORKDIR /app/frontend
COPY --from=deps /app/frontend/node_modules ./node_modules
COPY . .

RUN npm run build

# ==================================================
# アプリの実行レイヤー
# ==================================================
FROM node:18-alpine AS runner
WORKDIR /app/frontend

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder --chown=nextjs:nodejs /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

USER nextjs

EXPOSE 3000

ENV PORT 3000

CMD ["npm", "start"]

# 参考サイト
# Next.jsのDockerfileを作成する
# https://note.com/minato_kame/n/n04cbd62e4e6f
# 【Node.js/Next.js】Cloud Runで動作する軽量なDockerを構築してみた
# https://zenn.dev/kazumax4395/articles/427cc791f6145b

# **AS XXX**は、このステージにXXXという名前を付けることで、後のステージでこの結果を参照できるようにしています。

# Dockerfileで依存関係のインストール、ビルドプロセス、実行環境の準備をステージごとに分ける理由は、主に以下の3つの利点によります。

# 1. イメージサイズの最適化
# マルチステージビルドを使うことで、最終的なイメージに不要なものを含めず、軽量なイメージを作成できます。
# depsステージでインストールされた開発用の依存関係（例えば、ビルドに必要なもの）は、実行環境には不要です。そのため、依存関係やビルドに関連するファイルは最終イメージに含まれません。
# builderステージでは、アプリケーションのビルドに必要なツールやソースコードが含まれますが、これも実行環境では不要です。最終的なrunnerステージには、ビルドされたアプリケーションの必要な成果物のみが含まれます。
# これにより、プロダクション環境で使用されるイメージが小さくなり、起動時間の短縮やリソースの節約に繋がります。