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
    message = request.json['message']
    chat_id = message['chat']['id']
    text = message['text']

    if (text == '/start'):
        reply = 'Hola ' + message["from"]["first_name"] + '! 👋'
        reply_message(chat_id, reply)
        print('este es el chat iddddddddd ' + chat_id)
    else:
        reply_message(chat_id, 'Analizando... 🤔')
        transcript = get_transcript_for_video(text)
        if (transcript == '' || transcript == None):
            reply_message(chat_id, 'No se encontró información sobre este video. 😕')
        # bot = FinancialAdvisorBot(transcript)
        # messages = bot.generate_analysis()
        # for message in messages:
            # reply_message(chat_id, message)

    return '', 200

def reply_message(chat_id, message):
    requests.post(TELEGRAM_API_URL + 'sendMessage', {
        'chat_id': chat_id,
        'text': message 
    })
