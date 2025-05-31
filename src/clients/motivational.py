import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL_MOTIVATIONAL = os.getenv("BASE_URL_MOTIVATIONAL")

def fetch_motivational_quotes_data() -> dict | None:
  url = f"{BASE_URL_MOTIVATIONAL}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
  except requests.RequestException as exception:
    print(f"Failed to retrieve data. Status: {response.status_code}, error: {exception}")
    return None

def fetch_motivational_quotes(total_quotes: int = 1) -> list[str] | None:
  all_quotes = []
  for _ in range(total_quotes):
    data_dict = fetch_motivational_quotes_data()
    data = data_dict["data"]
    quote_entry = [
      data["author"],
      data["quote"],
    ]
    all_quotes.append(quote_entry)
  
  return all_quotes

if __name__ == "__main__":
  quotes = fetch_motivational_quotes(1)
  if quotes:
    for quote in range(len(quotes)):
      author, quote = quotes[quote]
      #print(f"{quote}")
      print(f"{quote} - {author}")

