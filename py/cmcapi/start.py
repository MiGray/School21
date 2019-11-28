  
 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from prettytable import PrettyTable
from colorama import Fore, Back, Style

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  #'id': '1'
  #'symbol':'ETH,BTG,ETC,CLO,RVN,ZEL,BEAM,CKB,GRIN,ETP,ZCL,BTCZ,MOAC,ZEC,PIRL,XMR,EXP,AE,ZEN'
  'start':'1',
  'limit':'2200',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.key,
}

session = Session()
session.headers.update(headers)
table = PrettyTable()

symbol_name = ["XZC","ETH", "BTG", "ETC", "CLO", "RVN", "ZEL", "BEAM", "CKB", "GRIN", "ETP", "ZCL", "BTCZ", "MOAC", "ZEC", "PIRL", "XMR", "EXP", "AE", "ZEN"]

response = session.get(url, params=parameters)
data = json.loads(response.text)
for currency in data['data']:
    id_number = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    rank = currency['cmc_rank']
    price = currency['quote']['USD']['price']
    market = currency['quote']['USD']['market_cap']
    if symbol in symbol_name:
        table.add_row([rank,name,symbol,price,market,id_number])
table.field_names = ["Rank","Name","Symbol","Price","Market M$","ID"]
table.sortby = "Name"
table.reversesort = False
print(table)
