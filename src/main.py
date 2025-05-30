import config

if config.ENABLE_BLBE:
  from api_clients.bible_client import fetch_bible_verse
      
if config.ENABLE_KANYE:
  from api_clients.kanye_client import fetch_kanye_quotes

def main():
  if config.ENABLE_BLBE:
    verses = fetch_bible_verse(1, "")  
    for _, book, chapter, verse, text in verses:
      print(f"{book} {chapter}:{verse} - {text}")

  if config.ENABLE_KANYE:
      quotes = fetch_kanye_quotes(1)
      for quote in quotes:
        print(f"{quote}\n")
        
if __name__ == "__main__":
  main()
