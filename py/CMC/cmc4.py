
import requests
import config
from prettytable import PrettyTable

key = config.key

api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
api += key

raw_data = requests.get(api).json()
data = raw_data['data']

table = PrettyTable()

for currency in data:
    rank = currency['cmc_rank']
    name = currency['name']
    price = currency['quote']['USD']['price']
    market = currency['quote']['USD']['market_cap']
    id_number = currency['id']

    table.add_row([rank,name,price,market/1000000,id_number])
table.field_names = ["Rank","Name","Price","Market M$","ID"]
table.sortby = "Rank"
table.reversesort = False
print(table)