from src.data_extractors.FromYoutube import get_transcript_for_video 
from src.bots.FinancialAdvisorBot import FinancialAdvisorBot
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
    message = request.json['message']
    chat_id = message['chat']['id']
    text = message['text']

    if (text == '/start'):
        reply = 'Hola ' + message["from"]["first_name"] + '! 👋'
    else:
        transcript = get_transcript_for_video(received_message)
        bot = FinancialAdvisorBot(transcript)
        reply_message(chat_id, 'Analizando... 🤔')
        messages = bot.generate_analysis()
        for message in messages:
            reply_message(chat_id, message)

    return '', 200

def reply_message(chat_id, message):
    requests.post(TELEGRAM_API_URL + 'sendMessage', {
        'chat_id': chat_id,
        'text': reply
    })