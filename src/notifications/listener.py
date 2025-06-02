from typing import Final
import os 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes 
import logging
from src.script.quote_selector import get_random_quote

load_dotenv()
TELEGRAM_BOT_TOKEN: Final[str | None] = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_USERNAME: Final[str | None] = os.getenv("TELEGRAM_BOT_USERNAME")

async def quote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f"Quote command accessed. {update}")
  await update.message.reply_text(get_random_quote())
  
def handle_response(text: str | None)-> str | None:
  processed_text: str | None = text.lower()
  print(text)
  if "w" in processed_text:
    return get_random_quote()
  return get_random_quote()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type 
  text: str = update.message.text or ""
  print(text)
  
  # check if group chat or dms
  logging.info(f"User ({update.message.chat.id}) in {message_type}: '{text}'")
  
  response: str | None = None
  
  if message_type == "group":
    if TELEGRAM_BOT_USERNAME and TELEGRAM_BOT_TOKEN in text:
      new_text: str = text.replace(TELEGRAM_BOT_USERNAME, "").strip()
      response: str = handle_response(new_text)
    else:
      handle_response(text)
  else:
    response: str = handle_response(text)
    
  if not response:
    return 
  
  logging.info(f"bot:  {response}")
  print(f"bot:  {response}")
  await update.message.reply_text(response)
  
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  logging.error(f"Update {update} caused error: {context.error}")
  
def run_bot():
  logging.info(f"Starting the telegram bot")
  print(f"Starting the telegram bot")
  app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
  app.add_handler(CommandHandler("w", quote_command))
  app.add_handler(MessageHandler(filters.TEXT, handle_message))
  app.add_error_handler(error)
  
  logging.info("Polling now")
  print("Polling now")
  app.run_polling(poll_interval=1)
  
if __name__ == "__main__":
  run_bot()