# syntax=docker/dockerfile:1
# check=skip=SecretsUsedInArgOrEnv

FROM python:3.11-alpine

ENV DB_HOST=localhost
ENV DB_PORT=15432
ENV DB_NAME=mydatabase
ENV DB_USER=myuser
ENV DB_PASSWORD=mypassword

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD flask --app app.app:app run --port 5001 --host 0.0.0.0