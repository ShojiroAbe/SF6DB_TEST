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

## 自動対話型の API ドキュメント(Swagger UI)

`http://localhost:8000/docs`# SF6DB_TEST
