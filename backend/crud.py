from sqlalchemy.orm import Session
import models, schemas

# キャタクターの登録
def create_character(db: Session, character: schemas.Character): # ①
  db_character = models.Character(name=character.name) # ②
  db.add(db_character)
  db.commit() # ③
  db.refresh(db_character) # ④
  return db_character # ⑤

# ①引数でcharacter：schemas.Characterを受け取る
# ②character引数）をDBモデルの models.Characterに変換する（この場合、引数の値をモデルを元に特定の箇所に代入する）
# ③DBにコミットする
# ④DB上のデータを元にcharacterインスタンス character を更新する
# ⑤作成したDBモデルを返却する

# キャラクターの取得
def get_character(db: Session):
  return db.query(models.Character).all() # ①

# ①query メソッドを使ってデータベースに問い合わせを行い、all() を呼び出すと、クエリの結果として得られた全てのレコードがリスト形式で返されます。
# all() の役割: クエリ結果の全ての行をリストで返す。
# 結果がない場合: クエリが一致するレコードを持たない場合は、空のリスト [] が返されます。
# そのためget_characterのresponse_modelはlist[]で受け取る必要がある