import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

response = requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/setWebhook",
    json={'url': f"{WEBHOOK_URL}/{TELEGRAM_API_KEY}"}
)

print(response.text)
