FROM python:3.11-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "/app/start.sh" ]
