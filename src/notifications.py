from typing import Final
import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import main 

load_dotenv()
from main import get_random_quote

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_USERNAME = os.getenv("TELEGRAM_BOT_USERNAME")

# Commands
async def quote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(get_random_quote())
  
# Responses
def handle_response(text: str | None)-> str | None:
  processed_text: str = text.lower()
  if "w" in processed_text:
    return get_random_quote()
  return get_random_quote()

# Messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type 
  text: str = update.message.text
  
  print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")
  
  if message_type == "group":
    if TELEGRAM_BOT_USERNAME in text:
      new_text: str = text.replace(TELEGRAM_BOT_USERNAME, "").strip()
      response: str = handle_response(new_text)
    else:
      handle_response(text)
  else:
    response: str = handle_response(text)
  
  if not response:
    return 
  
  print(f"bot:  {response}")
  await update.message.reply_text(response)
  
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f"Update {update} caused error: {context.error}")
  
if __name__ == "__main__":
  print(f"Starting the telegram bot")
  app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
  
  # Command
  app.add_handler(CommandHandler("w", quote_command))
  
  # Message
  app.add_handler(MessageHandler(filters.TEXT, handle_message))
  
  # Error
  app.add_error_handler(error)
  
  # Polling
  print("Polling now")
  app.run_polling(poll_interval=3)