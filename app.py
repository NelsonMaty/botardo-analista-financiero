from dotenv import load_dotenv
from flask import Flask, request
import os
import requests

app = Flask(__name__)

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/"

@app.route(f'/{TELEGRAM_API_KEY}', methods=['POST'])
def respond():
    update = request.json
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    send_message(chat_id, text)
    return '', 200


def send_message(chat_id, text):
    data = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(TELEGRAM_API_URL + 'sendMessage', data=data)
    return response.json()
