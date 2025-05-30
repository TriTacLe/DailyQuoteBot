import config
import random
import logging

def _bible():
    from api_clients.bible_client import fetch_bible_verse
    for _, book, chapter, verse, text in fetch_bible_verse(1, ""):
        print(f"{book} {chapter}:{verse} – {text}")
    logging.info("_bible() called")
    
def _motivational():
    from api_clients.motivational_client import fetch_motivational_quotes
    for author, quote in fetch_motivational_quotes(1):
        print(f"{quote} – {author}")
    logging.info("_motivational() called")

def _kanye():
    from api_clients.kanye_client import fetch_kanye_quotes
    for quote in fetch_kanye_quotes(1):
        print(f"{quote}\n")
    logging.info("_kanye() called")

def main():
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
    selected()
    
if __name__ == "__main__":
    main()
