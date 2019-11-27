
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
    rank = currency['rank']
    name = currency['name']
    symbol = currency['symbol']
    #price = currency['quote']['USD']['price']
    #market = currency['quote']['USD']['market_cap']
    id_number = currency['id']
    api2 = 'https://api.coinmarketcap.com/v2/ticker/'    
	api2 += str(id_number)
	raw_data2 = requests.get(api2).json()
	data2 = raw_data2['data']
	price = data2['quotes']['USD']['price']
    if symbol in symbol_name:
    	table.add_row([rank,name, symbol, price])
table.field_names = ["Rank","Name","Symbol","Price"]
table.sortby = "Rank"
table.reversesort = False
print(table)