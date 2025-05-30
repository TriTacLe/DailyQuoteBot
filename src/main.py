import config
import random
import logging

def _bible() -> str | None:
    from api_clients.bible_client import fetch_bible_verse
    for _, book, chapter, verse, text in fetch_bible_verse(1, ""):
        return (f"{book} {chapter}:{verse} – {text}")
    logging.info("_bible() called")
    
def _motivational() -> str | None:
    from api_clients.motivational_client import fetch_motivational_quotes
    for author, quote in fetch_motivational_quotes(1):
        return (f"{quote} – {author}")
    logging.info("_motivational() called")

def _kanye()-> str | None:
    from api_clients.kanye_client import fetch_kanye_quotes
    for quote in fetch_kanye_quotes(1):
        return(f"{quote}\n")
    logging.info("_kanye() called")

def select_random_quote():
    client_entry = [
        (config.ENABLE_BLBE,_bible),
        (config.ENABLE_KANYE,_kanye),
        (config.ENABLE_MOTIVATIONAL,_motivational),
    ]
      
    enabled = [func for status, func in client_entry if status]    
    if not enabled:
      logging.warning("No api clients enabled in the .env")
      return
    
    selected = random.choice(enabled)
    return selected
  
def get_random_quote() -> str | None:
  """_summary_
  Entry point for the application
  """
  quote_func = select_random_quote()
  if not quote_func:
    return None

  return quote_func()
  #print(f"{quote_func()}")
  
if __name__ == "__main__":
    get_random_quote()
