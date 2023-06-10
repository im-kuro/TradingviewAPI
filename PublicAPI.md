

# Here are all the public endpoint with limited access to data and functionality.



[x] - https://scanner.tradingview.com/
## Scanner Endpoints
- POST /global/scan
- POST /coin/scan
- POST /america/scan



[x] - https://www.tradingview.com/api/v1/
## API Endpoints
- GET /study-templates
- GET /symbols_list/custom/
- GET /symbols_list/active
- GET /symbols_list/colored



[x] - https://news-headlines.tradingview.com/v2/
## News Endpoints
- GET /headlines
-
-



FORMAT

### REQ TYPE - ENDPOINT
- payload
- payload breakdown
- response


## Endpoints documentation


### POST /america/scan


- payload
{
   "columns":[
      "description",
      "logoid",
      "type"
   ],
   "ignore_unknown_fields":false,
   "options":{
      "lang":"en"
   },
   "range":[
      0,
      6
   ],
   "markets":[
      "america"
   ],
   "preset":"volume_leaders"
}


columns = the data you want to get back
options = extra options
range = amount you want to return (0,6) = 6 results
markets = the market you want to scan
preset = the preset you want to use (volume_leaders, unusual_volume, gainers, losers)


- Response

{
   "totalCount":4848,
   "data":[
      {
         "s":"AMEX:TMBR",
         "d":[
            "Timber Pharmaceuticals, Inc.",
            "timber-pharmaceuticals",
            "stock"
         ]
      }
   ],
   "params":{
      "america":{
         "symbols":{
            "query":{
               "types":[
                  "stock",
                  "fund",
                  "dr",
                  "structured"
               ]
            }
         },
         "filter":[
            {
               "left":"exchange",
               "operation":"in_range",
               "right":[
                  "AMEX",
                  "NASDAQ",
                  "NYSE"
               ]
            },
            {
               "left":"is_primary",
               "operation":"equal",
               "right":true
            },
            {
               "left":"typespecs",
               "operation":"has",
               "right":"common"
            },
            {
               "left":"typespecs",
               "operation":"has_none_of",
               "right":"preferred"
            },
            {
               "left":"type",
               "operation":"equal",
               "right":"stock"
            },
            {
               "left":"active_symbol",
               "operation":"equal",
               "right":true
            }
         ],
         "sort":{
            "sortBy":"relative_volume_10d_calc",
            "sortOrder":"desc",
            "nullsFirst":false
         },
         "options":{
            "lang":"en"
         }
      }
   }
}







### POST /coin/scan

#### payload

{
   "columns":[
      "base_currency_desc",
      "base_currency_logoid",
      "type",
      "market_cap_calc",
      "exchange",
      "typespecs"
   ],
   "ignore_unknown_fields":false,
   "options":{
      "lang":"en"
   },
   "range":[
      0,
      9
   ],
   "markets":[
      "coin"
   ],
   "preset":"coin_market_cap_rank"
}

columns = the data you want to get back
options = extra options
range = amount you want to return (0,9) = 9 results
markets = the market you want to scan
preset = the preset you want to use (volume_leaders, unusual_volume, gainers, losers)



#### response


{
	"totalCount": 749,
	"data": [
		{
			"s": "CRYPTO:BTCUSD",
			"d": [
				"Bitcoin",
				"crypto/XTVCBTC",
				"spot",
				499283284255.42,
				"CRYPTO",
				[
					"crypto",
					"cryptoasset",
					"synthetic"
				]
			]
		},
		{
			"s": "CRYPTO:ETHUSD",
			"d": [
				"Ethereum",
				"crypto/XTVCETH",
				"spot",
				217863806667.2324,
				"CRYPTO",
				[
					"crypto",
					"cryptoasset",
					"synthetic"
				]
			]
		},
		{
			"s": "CRYPTO:USDTUSD",
			"d": [
				"Tether",
				"crypto/XTVCUSDT",
				"spot",
				83311157336.59897,
				"CRYPTO",
				[
					"crypto",
					"cryptoasset",
					"synthetic"
				]
			]
		},
}




















