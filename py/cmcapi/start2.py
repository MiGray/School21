  
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
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    market_cap = currency['quote']['USD']['market_cap']
    hour_change = currency['quote']['USD']['percent_change_1h']
    day_change = currency['quote']['USD']['percent_change_24h']
    week_change = currency['quote']['USD']['percent_change_7d']
    price = currency['quote']['USD']['price']
    volume = currency['quote']['USD']['volume_24h']

    if hour_change is not None:
        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

    if day_change is not None:
        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

    if week_change is not None:
        if week_change > 0:
            week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

    if volume is not None:
        volume_string = '{:,}'.format(volume)

    if market_cap is not None:
        market_cap_string = '{:,}'.format(market_cap)

    if symbol in symbol_name:        
        table.add_row([rank, name + ' ( ' + symbol + ')', '$' + str(price), '$' + str(market_cap), 
            '$' + volume_string, str(hour_change), str(day_change), str(week_change)])

table.field_names = ["Rank","Name(Symbol)","Price","Market Cap", "Volume", "Hour Change", "Day Change", "Week Change"]
table.sortby = "Day Change"
table.reversesort = True
print(table)

    