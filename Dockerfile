FROM python:3.8

WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y && \
    python -m pip install --upgrade pip

COPY ./models /app/models

COPY ./*.py ./requirements.txt /app/

RUN pip install -r requirements.txt

USER medved

ARG token

ENV TG_TOKEN=${token}

CMD ["python", "20221217_neuro_medv_bot.py"]