FROM python:3.8

WORKDIR /app

RUN addgroup --gid 1024 medved && \
    adduser --disabled-password --home /home/medved --ingroup medved medved --gecos ""

COPY ./*.py ./requirements.txt /app/

RUN apt-get update -y && apt-get upgrade -y && \
    python -m pip install --upgrade pip && \
    pip install -r requirements.txt
    