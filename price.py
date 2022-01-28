#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'BTC',
#  'start':'1',
 # 'limit':'5',
  'convert':'ALICE'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '50a609ad-76d0-4d59-9ec0-80fd678ecb41',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(type(data))
  #print(data.keys())
#  print(data.values())
  print(type(data["data"]))
  datav=data["data"]
  btc = datav["BTC"]
  btckeys = btc.keys()
  quote1 = btc["quote"]
  usd=quote1["ALICE"]
  price1 = usd["price"]
  print("price: {}".format(price1) )
  #print("quote: {} ".format(quote))
  #print("quote type: {}".format(type(quote)))
#  print("btc keys: {}".format(keys))1
 # keyData = datav.keys()

  valuesData = datav.values()
 # print("key: {}".format(keyData))
 # print("value: {}".format(valuesData))

#  print("data: {}".format(data["data"]))
#  print("status: {}".format(data["status"]))
#  print("price:{}".format)

# print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)