
import requests
import config
from prettytable import PrettyTable

key = config.key

api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?CMC_PRO_API_KEY='
api += key

raw_data = requests.get(api).json()
data = raw_data['data']
table = PrettyTable()

symbol_name = ["XZC","ETH", "BTG", "ETC", "CLO", "RVN", "ZEL", "BEAM", "CKB", "GRIN", "ETP", "ZCL", "BTCZ", "MOAC", "ZEC", "PIRL", "XMR", "EXP", "AE", "ZEN"]

for currency in data:
    id_number = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    rank = currency['rank']
    if symbol in symbol_name:
       table.add_row([rank,name, symbol,id_number])
table.field_names = ["Rank","Name","Symbol","ID"]
table.sortby = "Rank"
table.reversesort = False
print(table)
