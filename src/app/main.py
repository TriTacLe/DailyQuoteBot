import os 
from app.notifications.notifier import run_bot
import logging

def main():
  """_summary_
  Entrypoint of the application
  starts the telegram bot
  """
  try:
    logging.info("Starting telegram bot")
    run_bot()
  except:
    logging.error(f"error")
  
if __name__ == "__main__":
  main()