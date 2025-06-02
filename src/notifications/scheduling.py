# src/script/scheduler.py
import os
import schedule
import time
import requests
from dotenv import load_dotenv
from src.script.quote_selector import get_random_quote

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TIME = os.getenv("TIME")

# Hardcoded for testing
TIME_LOCAL_1 = "19:25"
TIME_LOCAL_2 = "19:26"
TIME_UTC_1 = "22:25"
TIME_UTC_2 = "22:26"

def send_quote(schedule_time: str):
  print("schedule_time()")
  message = f"{get_random_quote()} (time: {schedule_time})"
  url = (
    f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
    f"/sendMessage?chat_id={TELEGRAM_CHAT_ID}"
    f"&text={message}"
  )
  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
  except requests.RequestException as error:
    print(f"{error}")

def setup_daily_quotes() -> None:
  print("setyp_daily_quotes()")
  schedule.clear()
  main_time = os.getenv("TIME")
  if main_time:
    schedule.every().day.at(main_time).do(send_quote, main_time)

  setup_tests_times()

def setup_tests_times() -> None:
  schedule.every().day.at(TIME_UTC_1).do(send_quote, TIME_UTC_1)
  schedule.every().day.at(TIME_LOCAL_1).do(send_quote, TIME_LOCAL_1)
  schedule.every().day.at(TIME_UTC_2).do(send_quote, TIME_UTC_2)
  schedule.every().day.at(TIME_LOCAL_2).do(send_quote, TIME_LOCAL_2)  

def run_scheduler() -> None:
  print("Started run_scheduler()")
  setup_daily_quotes()
  while True:
    time.sleep(1)
    schedule.run_pending()

if __name__ == "__main__":
  run_scheduler()
