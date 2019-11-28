 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
parameters = {
  'id':'1,1027'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)