from requests import sessions
import json



class tradingVeiwPublic():
	def __init__(self, cookie: json = None) -> None:
		"""setup the session for the class

		Args:
			cookie (json, optional): json data waith cookie info. Defaults to None.
   
		example:
			cookie = {"sessionid": "scio378w087nt0873tn0","sessionid_sign": "onf8yv09p8dyn-9s7ntd7tnv9-343"}
		"""
		
		self.sesh = sessions.Session()
		self.sesh.headers.update({
			"Host": "scanner.tradingview.com",
			"Cookie": "cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={'analytics':true,'advertising':true}; _gid=GA1.2.704054866.1686337824; _sp_ses.cf1a=*; _gat_gtag_UA_24278967_1=1; _sp_id.cf1a=01cd3c5e-82a2-4585-aca3-85196c82d85e.1686022716.4.1686417372.1686337824.fad9316a-f9ea-4a0c-86da-59daaa7f08b3; _ga=GA1.1.1116477781.1686022716; _ga_YVVRYGL0E0=GS1.1.1686417069.4.1.1686417372.45.0.0",
			"Content-Length": "240",
			"Sec-Ch-Ua": "",
			"Sec-Ch-Ua-Platform": "",
			"Sec-Ch-Ua-Mobile": "?0",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
			"Content-Type": "text/plain;charset=UTF-8",
			"Accept": "*/*",
			"Origin": "https://www.tradingview.com",
			"Sec-Fetch-Site": "same-site",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Dest": "empty",
			"Referer": "https://www.tradingview.com/",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "en-US,en;q=0.9"
		})
		if cookie != None:
			self.sesh.cookies.update({f"""    
           "cookie": "sessionid={cookie["sessionid"]}; sessionid_sign={cookie["sessionid_sign"]};"
        """})
		self.request = self.sesh.request
    
    
    
    
    
    
    
	""" https://scanner.tradingview.com/ """
	def getGlobalData(self, ticker: str = None) -> json:
		data = {
			"columns":[
				"price_52_week_high",
				"price_52_week_low",
				"sector",
				"country",
				"Low.1M",
				"High.1M",
				"Perf.W",
				"Perf.1M",
				"Perf.3M",
				"Perf.6M",
				"Perf.Y",
				"Perf.YTD",
				"Recommend.All",
				"average_volume_10d_calc"
			],
			"range":[
				0,
				9
			],
			"symbols":{
				"tickers":[
					ticker
				]
				}
			}
			
		req = self.sesh.post("https://scanner.tradingview.com/global/scan", data=json.dumps(data))
		reqJson = req.json()
		if req.status_code == 200:
			pharsedData = {
				"52WeekHigh": req.json()["data"][0]["d"][0],
				"52WeekLow": req.json()["data"][0]["d"][1],
				"sector": req.json()["data"][0]["d"][2],
				"country": req.json()["data"][0]["d"][3],
				"Low1M": req.json()["data"][0]["d"][4],
				"High1M": req.json()["data"][0]["d"][5],
				"PerfW": req.json()["data"][0]["d"][6],
				"Perf1M": req.json()["data"][0]["d"][7],
				"Perf3M": req.json()["data"][0]["d"][8],
				"Perf6M": req.json()["data"][0]["d"][9],
				"PerfY": req.json()["data"][0]["d"][10],
				"PerfYTD": req.json()["data"][0]["d"][11],
				"RecommendAll": req.json()["data"][0]["d"][12],
				"averageVolume10dCalc": req.json()["data"][0]["d"][13]
			}

			return pharsedData
		else:
			return {"error": reqJson["error"], "status": req.status_code}





	
	def getCoinData(self, market: str, preset: str) -> json:
		data = {
				"columns":[
					"base_currency_desc",
					"base_currency_logoid",
					"type",
					"market_cap_calc",
					"exchange",
					"typespecs"
				],
				"ignore_unknown_fields":"true",
				"options":{
					"lang":"en"
				},
				"range":[
					0,
					999
				],
				"markets":[
					market
				],
				"preset":preset
				}
			
			
		req = self.sesh.post("https://scanner.tradingview.com/coin/scan", data=json.dumps(data))
		reqJson = req.json()
		if req.status_code == 200:
			pharsedData = {
				"baseCurrencyDesc": req.json()["data"],
	
				
			}

			return pharsedData
		else:
			return {"error": reqJson["error"], "status": req.status_code}





	def getStockData(self, market: str, preset: str) -> json:
		data = {
				"columns":[
					"description",
					"logoid",
					"type"
				],
				"ignore_unknown_fields":"true",
				"options":{
					"lang":"en"
				},
				"range":[
					0,
					999
				],
				"markets":[
					market
				],
				"preset":preset
				}
			
			
		req = self.sesh.post("https://scanner.tradingview.com/coin/scan", data=json.dumps(data))
		reqJson = req.json()
		if req.status_code == 200:
			pharsedData = {
				"baseCurrencyDesc": req.json()["data"][0]["d"][0],
				"baseCurrencyLogoid": req.json()["data"][0]["d"][1],
				"type": req.json()["data"][0]["d"][2],
				"marketCapCalc": req.json()["data"][0]["d"][3],
				"exchange": req.json()["data"][0]["d"][4],
				"typespecs": req.json()["data"][0]["d"][5]
				
			}

			return pharsedData
		else:
			return {"error": reqJson["error"], "status": req.status_code}
			
	"""https://www.tradingview.com/api/v1/"""
 
	def getStudyTemplates(self):
			
		req = self.sesh.post("https://scanner.tradingview.com/coin/scan")
		reqJson = req.json()
		if req.status_code == 200:

			return reqJson
		else:
			return {"error": reqJson["error"], "status": req.status_code}

	def getCustomSymbolList(self):
		pass

	def getCustomSymbolListColored(self):
		pass

	def getBrokerPanelNews(self):
		pass

	"""
https://news-headlines.tradingview.com/v2/
https://pine-facade.tradingview.com/pine-facade/list
https://www.tradingview.com/pubscripts-library/editors-picks

	"""
	def getNews(self):
		pass

