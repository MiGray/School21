import json 
import requests 

r = requests.get('https://api.coinmarketcap.com/v2/ticker/1')
print(r)
#for coin in r.json():
#    print()