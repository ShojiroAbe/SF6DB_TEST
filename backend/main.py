from os import name
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
from database import SessionLocal, engine
import models, schemas, crud

# Swaggerのメタデータ設定方法
# https://fastapi.tiangolo.com/ja/tutorial/metadata/
tags_metadata = [
    {
        "name": "Character",
        "description": "キャラクター管理API",
    }
]

app = FastAPI(
    title="キャラクター管理API",
    description="このAPIはストリートファイター6のキャラクター管理を行うためのAPIです。",
    openapi_tags=tags_metadata
)

# models.pyのテーブル定義をデータベースに反映
models.Base.metadata.create_all(bind=engine)

# セッションを作成する関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# キャラクター登録
@app.post("/regist/character", tags=["Character"], summary="キャラクターの登録")
def regist_character(character: schemas.Character, db: Session=Depends(get_db)):
    """
    キャラクター名をデータベースに登録するためのエンドポイントです。

    - **name**: 登録するキャラクターの名前
    """
    
    # TODO 重複チェック的なの入れたい

    return crud.create_character(db, character)

# キャラクター取得（全て、個々）

@app.get(path="/")
def read_root():
    return {"Hello": "World"}

@app.get(path="/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# テーブル取得
@app.get(path="/getdb")
def test_db_connection():
    with engine.connect() as connection:
        result = connection.execute(statement=text(text="SHOW TABLES;"))
        tables = result.fetchall()
    return {"tables": tables}

# with engine.connect() as connection:
# 役割: SQLAlchemyの engine オブジェクトを使ってデータベース接続を開きます。
# engine.connect(): データベースへの接続を確立します。
# with 文: コンテキストマネージャを使って、接続が自動的にクローズされるようにしています。接続の開始から終了までの範囲をこのブロックで管理します。

# result = connection.execute(text("SHOW TABLES;"))
# 役割: データベースに対してSQLクエリを実行します。
# connection.execute(): データベースに対してクエリを実行します。
# text("SHOW TABLES;"): 実行するクエリをSQL文として書いています。SHOW TABLES; は、MySQLで現在のデータベースに存在する全テーブルをリストするクエリです。

# tables = result.fetchall()
# 役割: クエリの結果をすべて取得します。
# result.fetchall(): クエリ結果からすべての行を取得し、それをリストとして返します。このリストにはテーブル名が含まれます。

# return {"tables": tables}
# 役割: 取得したテーブル名のリストを辞書形式でJSONレスポンスとして返します。
# {"tables": tables}: tables にはクエリ結果が入っており、それを tables というキーでレスポンスに含めています。このデータは、ブラウザやAPIクライアントでJSON形式で表示されます。

# metadata は、Base クラスに関連するすべてのテーブル定義（モデルクラス）を含むメタデータオブジェクトです。これにより、データベースに存在するべきテーブル構造を理解し、管理することができます。

# create_all メソッドは、metadata に登録されているすべてのテーブルをデータベースに作成するメソッドです

# 引数の bind=engine は、どのデータベースエンジンに対してこの操作を行うかを指定しています。engine はデータベース接続情報を持つオブジェクトで、database.py ファイル内で create_engine 関数を使って設定されています。