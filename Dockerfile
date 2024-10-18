FROM python:3.10-slim

WORKDIR /app

COPY ./src /app

COPY ./requirements.txt /app

VOLUME app/keys

VOLUME app/cyphers

VOLUME app/packages

RUN pip install --cache-dir /app/packages -r requirements.txt

CMD ["python", "app.py"]