from bots.FinancialAdvisorBot import FinancialAdvisorBot
from data_extractors.FromYoutube import get_transcript_for_video 
from dotenv import load_dotenv
from flask import Flask
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os

async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}! 👋",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update, context):
    await update.message.reply_text("Pasame un link de youtube y yo te lo analizo wachooo")

async def analyze_content(update, context):
    received_message = update.message.text
    transcript = get_transcript_for_video(received_message)
    bot = FinancialAdvisorBot(transcript)
    await update.message.reply_text('Analizando... 🤔')
    messages = bot.generate_analysis()
    for message in messages:
        print(message)
        await update.message.reply_text(message)

def main():
    load_dotenv()
    api_key = os.getenv("TELEGRAM_API_KEY")
    application = Application.builder().token(api_key).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze_content))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
