from imaplib import Int2AP
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '50a609ad-76d0-4d59-9ec0-80fd678ecb41',
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

symbol1 = str(input("Firt Token Symbol: "))
value = float(input("How much?: "))
symbol2 = str(input("Segund Token Symbol: "))

def por(price1,input):
    por = price1*input 
    return por

parameters = {
  'symbol':symbol1,
#  'start':'1',
 # 'limit':'5',
  'convert':symbol2
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
  data1 = data["data"]
  token = data1[symbol1]
  quote1 = token["quote"]
  token2 = quote1[symbol2]
  price = token2["price"]
  print(price)
  x=por(price,value)
  print("{} {} = {} {}".format(value,symbol1,x,symbol2))
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

def por(price1,input):
    por = price1*input 
    return por

