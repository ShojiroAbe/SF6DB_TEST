from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

MYSQL_DATABASE_URL = "mysql://user:user-pass@mysql:3306/mydb"

engine = create_engine(MYSQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# クラスを返す関数 declarative_base() を使用
# このクラスを継承して、各データベースモデルやクラス（ORMモデル）を作成します