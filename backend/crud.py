from sqlalchemy.orm import Session
import models, schemas


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