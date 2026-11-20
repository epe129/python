import json
import requests
from bs4 import BeautifulSoup
from bs2json import BS2Json

response = requests.get("https://www.is.fi/rss/tuoreimmat.xml")
response.raise_for_status()

soup = BeautifulSoup(response.content, "xml")
converter = BS2Json(soup)
result = converter.convert()
r = json.dumps(result, ensure_ascii=False, indent=2)

for c in result["rss"]["channel"]["children"]:
    item = c.get("item")
    if not item:
        continue
    for child in item.get("children", []):
        if isinstance(child, dict) and "link" in child:
            print(child)
            break