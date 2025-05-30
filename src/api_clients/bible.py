import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL_BIBLE = os.getenv("BASE_URL_BIBLE")

def get_verse_data(testament: str = ""):
  """
  testament is OT or NT
  """
  prefix = f"/{testament.upper()}" if testament else ""
  url = f"{BASE_URL_BIBLE}/data/web/random{prefix}"
  try:
    response = requests.get(url)
    if response.status_code == 200:
      #print(f"response ok: {response.ok}")
      return response.json()
  except requests.RequestException as exception:
    print(f"Failed to retrieve data. Status: {response.status_code}, error: {exception}")
    return None

def get_random_verse(total_verse: int = 1, testament: str = ""):
  all_verses_lst = []
  for _ in range(total_verse):
    data = get_verse_data(testament)
    if not data or "random_verse" not in data:
      print("No verse returned from get_verse_data()")
      break

    random_verse = data["random_verse"]
    
    verse_entry = [
      random_verse,  
      random_verse["book"],
      random_verse["chapter"],
      random_verse["verse"],
      random_verse["text"]
    ]

    all_verses_lst.append(verse_entry)
  return all_verses_lst

if __name__ == "__main__":
  verses = get_random_verse(1, "")
  
  if verses:
    for i in range(len(verses)):
      random_verse_dict, book, chapter, verse, text = verses[i]
      print(f"{book} {chapter}:{verse} - {text}")

