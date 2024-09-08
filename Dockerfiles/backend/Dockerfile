# FastAPI
# ここから引用：https://fastapi.tiangolo.com/ja/deployment/docker/#fastapi
FROM python:3.9

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./backend .

CMD ["/wait-for-it.sh", "mysql:3306", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]