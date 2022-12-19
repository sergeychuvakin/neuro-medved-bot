FROM python:3.8

WORKDIR /app

RUN addgroup --gid 1024 medved && \
    adduser --disabled-password --home /home/medved --ingroup medved medved --gecos ""

COPY ./models/gpt3_medium_medved_9.pt /app/models/gpt3_medium_medved_9.pt

COPY ./*.py ./requirements.txt /app/

RUN apt-get update -y && apt-get upgrade -y && \
    python -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python pre-load-to-docker.py

USER medved

ARG token

ENV TG_TOKEN=${token}

CMD ["python", "20221217_neuro_medv_bot.py"]