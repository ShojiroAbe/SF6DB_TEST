# FastAPI
# ここから引用：https://fastapi.tiangolo.com/ja/deployment/docker/#fastapi
FROM python:3.9

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# wait-for-it.shをダウンロードして実行権限を付与
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY ./backend .

CMD ["/wait-for-it.sh", "mysql:3306", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]