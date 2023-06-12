
# Here are all the public misc endpoints that have no known/useful api functionality.



## Misc/Non api
[X] - https://quotes.tradingview.com/quote_cache_http/snapshot
- POST /quote_cache_http/snapshot
-
-









FORMAT

### REQ TYPE - ENDPOINT
- payload
- payload breakdown
- response


## Endpoints documentation






### POST /quote_cache_http/snapshot

- paylaod

[
   "BLACKBULL:SPX500"
]

for each symbol in the array it will return a response


- response

[
	{
		"symbol": "BLACKBULL:SPX500",
		"s": "ok",
		"data": {
			"current_session": "out_of_session",
			"type": "index",
			"update_mode": "streaming",
			"original_name": "BLACKBULL:SPX500",
			"short_name": "SPX500",
			"pro_name": "BLACKBULL:SPX500",
			"description": "SPX500",
			"local_description": null,
			"language": null,
			"fractional": false,
			"pricescale": 100,
			"minmov": 1,
			"minmove2": 0,
			"symbol_status": "realtime",
			"lp": 4301.6999999999998181,
			"chp": 0.19000000000000000222,
			"ch": 8.0,
			"lp_time": 1686344334,
			"logoid": "indices/s-and-p-500",
			"currency-logoid": null,
			"base-currency-logoid": null
		}
	}

]

- query params

https://quotes.tradingview.com/quote_cache_http/snapshot?fields=current_session,type,update_mode,original_name,short_name,pro_name,description,local_description,language,fractional,pricescale,minmov,minmove2,symbol_status,lp,chp,ch,lp_time,logoid,currency-logoid,base-currency-logoid,rtc,rch,rchp

