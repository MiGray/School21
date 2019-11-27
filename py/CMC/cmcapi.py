'''import coinmarketcapapi
#import config
cmc = '04a9c206-662b-48f5-8140-ec161c90e1ac'
r = cmc.cryptocurrency_map(1)

print(r)
'''
import coinmarketcapapi

cmc = CoinMarketCapAPI('04a9c206-662b-48f5-8140-ec161c90e1ac', sandbox=True)
r = cmc.cryptocurrency_info(symbol='BTC')

print repr(r.data)