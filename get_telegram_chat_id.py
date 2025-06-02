import os
import requests
from dotenv import load_dotenv
# run in terminal:
# python get_telegram_chat_id.py

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def get_chat_id(index: int = 0) -> dict | None:
  """_summary_
  Remember to send a message to the bot right before running this script or you get error
  Asign the return value of this method to "TELEGRAM_CHAT_ID" in .env
  Returns:
      _type_: str
  """
  url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
  response = requests.get(url)
  data = response.json()
  updates = data.get("result", [])
  last_update = updates[index]
  chat_id = last_update["message"]["from"]["id"]
  return chat_id

if __name__ == "__main__":
  """_summary_
  parameter param is dict index
  """
  param = -1
  print(f"{get_chat_id(param)}")
  