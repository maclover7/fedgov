import json
import pandas as pd
import requests

def get_items(item_class, page):
  req = requests.get("https://api.doge.gov/savings/%s?sort_by=savings&sort_order=desc&per_page=500&page=%i" % (item_class, page))
  req = req.json()
  return [req['result'][item_class], req['meta']['pages']]

def save_items(item_class):
  first_page = get_items(item_class, 1)
  dfs = [pd.DataFrame(first_page[0])]

  for page in range(2, first_page[1] + 1):
    dfs.append(pd.DataFrame(get_items(item_class, page)[0]))

  pd.concat(dfs).to_csv("data/%s.csv" % (item_class), index=False)

for item_class in ["contracts", "grants", "leases"]:
  save_items(item_class)