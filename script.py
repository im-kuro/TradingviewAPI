from requests import sessions



session = sessions.session()

link = "https://scanner.tradingview.com/"
endpoint = "/crypto/scan"

payload = {
   "columns":[
      "base_currency_desc",
      "base_currency_logoid",
      "type",
      "market_cap_calc",
      "exchange",
      "typespecs"
   ],
    "ignore_unknown_fields":"false",
   "options":{
      "lang":"en"
   },
  	"range":[
      0,
      1
   ],
   "markets":[
      "coin"
   ],
   "preset":"coin_market_cap_rank"
}

x = session.get(link + endpoint, params=payload)

for coin in x.json()["data"]:
	print(coin)
