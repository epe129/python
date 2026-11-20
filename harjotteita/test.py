# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#   'start':'1',
#   'limit':'10',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': '',
# }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = response.json()
#   for crypto in data["data"]:
#     name = crypto["name"]
#     symbol = crypto["symbol"]
#     price = crypto["quote"]["USD"]["price"]
#     if name == "Bitcoin" or name == "XRP" or name == "Ethereum" or name == "Solana":
#         print(f"{name} ({symbol}): ${price:.2f}")

# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)

# import requests
# import xmltodict
# from xml.etree import ElementTree
# import json

# x = requests.get('https://www.is.fi/rss/tuoreimmat.xml')

# # dict_data = xmltodict.parse(x.text)

# # pretty_json = json.dumps(dict_data, indent=4, ensure_ascii=False)

# data = xmltodict.parse(x.text)  # tämä on dict

# for item in data["rss"]["channel"]["item"]:
#     print(item["description"])

# # for item in data["rss"]["channel"]["item"]: 
# #     print(item["title"])


