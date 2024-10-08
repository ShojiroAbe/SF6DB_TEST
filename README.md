## dockerの復習と用語メモ

参考：
https://qiita.com/shimada_slj/items/3580b0426fa6b73e4638

### Dockerfileとは

Dockerfileとは、Dockerイメージを作成するためのテキストファイルです。
Dockerfile内には、基本となるOS、インストールする必要があるソフトウェア、コピーするファイル・ディレクトリ、開くポート、実行するコマンドなど、新しいDockerイメージを作成するために必要な指示が含まれています。
Dockerfileの書き方としては、「FROM」,「RUN」,「CMD」などのインストラクションに引数を記述し、作成します。

参考：
https://qiita.com/gon0821/items/f9e3bcbb6cb01d4ef7fa

## コンテナの立ち上げ方

`docker-compose up -d`

## コンテナ立ち上げ及びビルド
コンテナがビルドされていない場合に自動的にビルドを行うことができます。
ビルドされていない場合や変更があった場合にもビルドされてコンテナが立ち上がります。

`docker-compose up -d --build`

## 自動対話型の API ドキュメント(Swagger UI)

`http://localhost:8000/docs`# SF6DB_TEST

### git　追加手順
`git add .`
`git commit -m "コミットメッセージ"`
`git push`

## SWR データ取得のための React Hooks ライブラリ
https://swr.vercel.app/ja
インストール：
https://swr.vercel.app/ja/docs/getting-started

## Compose における起動順と停止順の制御（例：wait-for-it.sh）
他にもマイグレーション方法などがある

参考URL：
初回起動時にコケる!? Docker Composeで解決するrails db:migrateの自動化
https://qiita.com/besmero628/items/d94e968d0d26d780e6cf
Compose における起動順と停止順の制御
https://docs.docker.jp/compose/startup-order.html