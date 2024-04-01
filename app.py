from dotenv import load_dotenv
from flask import Flask, request
import os
import requests

app = Flask(__name__)

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/"

@app.route(f'/{TELEGRAM_API_KEY}', methods=['POST'])
def respond():
    reply = None
    chat_id = request.json['message']['chat']['id']
    text = request.json['message']['text']

    if (text == '/start'):
        reply = 'Hi there! I am a bot. Try me!
    else:
        reply = text # echo by default

    response = requests.post(TELEGRAM_API_URL + 'sendMessage', {
        'chat_id': chat_id,
        'text': text
    })
    return '', 200
