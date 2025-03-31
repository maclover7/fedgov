import json
import requests

def get_items(item_class, page):
  req = requests.get("https://api.doge.gov/savings/%s?sort_by=savings&sort_order=desc&per_page=100&page=%i" % (item_class, page))
  req = req.json()
  return [req['result'][item_class], req['meta']['pages']]

def save_items(item_class):
  results = []
  first_page = get_items(item_class, 1)
  results.extend(first_page[0])

  for page in range(2, first_page[1] + 1):
    results.extend(get_items(item_class, page)[0])

  with open("data/%s.json" % (item_class), "w") as f:
    json.dump(results, f)

for item_class in ["contracts", "grants", "leases"]:
  save_items(item_class)