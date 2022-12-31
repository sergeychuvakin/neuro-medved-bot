FROM python:3.8

WORKDIR /app

RUN addgroup --gid 1024 medved && \
    adduser --disabled-password --home /home/medved --ingroup medved medved --gecos ""

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update -y && apt-get upgrade -y && \
    python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./*.py /app/
EXPOSE 5000

# ENTRYPOINT python add_cache.py
CMD python model_endpoint.py