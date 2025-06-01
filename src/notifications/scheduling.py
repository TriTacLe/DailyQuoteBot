import os
import requests
from dotenv import load_dotenv
from src.script.quote_selector import get_random_quote
import time
import schedule

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TIME = os.getenv("TIME")

def send_quote():
  message = get_random_quote()
  url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
  except requests.RequestException as error:
    print(f"{error}")

def schedule_send_quote():
  schedule.every().day.at(f"{TIME}").do(send_quote)
  while True:
    schedule.run_pending()
    time.sleep(1)
  
if __name__ == "__main__":
  schedule_send_quote()