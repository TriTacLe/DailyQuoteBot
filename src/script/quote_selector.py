import random
import logging
from config import ENABLE_BLBE, ENABLE_KANYE, ENABLE_MOTIVATIONAL

def _bible() -> str | None:
    logging.info("_bible() called")
    from clients.bible import fetch_bible_verse
    for _, book, chapter, verse, text in fetch_bible_verse(1, ""):
        return (f"{book} {chapter}:{verse} – {text}")
    return None
    
def _motivational() -> str | None:
    logging.info("_motivational() called")
    from clients.motivational import fetch_motivational_quotes
    for author, quote in fetch_motivational_quotes(1):
        return (f"{quote} – {author}")
    return None

def _kanye()-> str | None:
    logging.info("_kanye() called")
    from clients.kanye import fetch_kanye_quotes
    for quote in fetch_kanye_quotes(1):
        return(f"{quote}\n")
    return None

def select_random_quote():
    client_entry = [
        (ENABLE_BLBE,_bible),
        (ENABLE_KANYE,_kanye),
        (ENABLE_MOTIVATIONAL,_motivational),
    ]
    # List comprehension!!!!!!!
    enabled = [func for status, func in client_entry if status]    
    if not enabled:
      logging.warning("No api clients enabled in the .env")
      return
    return random.choice(enabled)
  
def get_random_quote() -> str | None:
  quote_func = select_random_quote()
  if not quote_func:
    return None
  return quote_func()

if __name__ == "__main__":
    result =get_random_quote()
    print(result)
