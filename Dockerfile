FROM python:3.11-slim-bullseye

WORKDIR /discord-bot-hello

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]
