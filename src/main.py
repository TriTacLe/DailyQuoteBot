from src.notifications.listener import run_bot
from src.notifications.scheduling import schedule_send_quote
import logging

def main():
  """_summary_
  Entrypoint of the application
  starts the telegram bot
  """
  try:
    logging.info("Starting telegram bot: schedule_send_quote() and run_bot()")
    print("Starting telegram bot: schedule_send_quote() and run_bot()")
    schedule_send_quote()
    #run_bot()
  except Exception as exception:
    logging.error(f"errrrror: {exception}")
    print(f"errrrror: {exception}")
  
if __name__ == "__main__":
  main()