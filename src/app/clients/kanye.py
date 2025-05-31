import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL_KANYE = os.getenv("BASE_URL_KANYE")

def fetch_kanye_quote_data() -> dict | None:
  url = f"{BASE_URL_KANYE}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
  except requests.RequestException as exception:
    print(f"Failed to retrieve data. Status: {response.status_code}, error: {exception}")
    return None

def fetch_kanye_quotes(total_quotes: int = 1) -> list[str] | None:
  all_quotes_lst = []
  for _ in range(total_quotes):
    data = fetch_kanye_quote_data()
    if not data or "quote" not in data:
      print("No quote in response")
      return None
    quote = f"{data["quote"]} - Kanye"
    all_quotes_lst.append(quote)
    
  return all_quotes_lst

if __name__ == "__main__":
  quotes = fetch_kanye_quotes(2)
  if quotes:
    for quote in quotes:
      print(f"{quote}\n")
