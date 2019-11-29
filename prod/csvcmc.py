from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import json
import config
import csv
import datetime

now = datetime.datetime.now()

FILENAME = "/home/mi/cmc/cmc" + now.isoformat() + ".csv"

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.key,
}

session = Session()
session.headers.update(headers)


response = session.get(url, params=parameters)
data = json.loads(response.text)
collumns = ["ID", "Rank", "Name", "Symbol", "Slug", "Market_pairs", "Added", 
        "Tags", "Max_supply", "Circulating_supply", "Last_updated", 
        "Platform", "Price", "Volume", "Market_cap", "Hour_change", "Day_change", "Week_change", "Last_updated_quote"]
        
with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(collumns)

for currency in data['data']:
    id_coin = currency['id']
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    slug = currency['slug']
    market_pairs = currency['num_market_pairs']
    added = currency['date_added']
    tags = currency['tags']
    max_supply = currency['max_supply']
    circulating_supply = currency['circulating_supply']
    last_updated = currency['last_updated']
    platform = currency['platform']
    price = currency['quote']['USD']['price']
    volume = currency['quote']['USD']['volume_24h']
    market_cap = currency['quote']['USD']['market_cap']
    hour_change = currency['quote']['USD']['percent_change_1h']
    day_change = currency['quote']['USD']['percent_change_24h']
    week_change = currency['quote']['USD']['percent_change_7d']
    last_updated_quote = currency['quote']['USD']['last_updated']
        
    csv_data = [id_coin, rank, name, symbol, slug, market_pairs, added, 
        tags, max_supply, circulating_supply, last_updated, 
        platform, price, volume, market_cap, hour_change, day_change, week_change, last_updated_quote]
    
    with open( FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(csv_data)

