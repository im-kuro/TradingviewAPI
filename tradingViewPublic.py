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
			
			"Host": "www.tradingview.com",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
			"Accept": "*/*",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate",
			"Referer": "https://www.tradingview.com/chart/lf4zb40L/?symbol=BLACKBULL%3ASPX500",
			"X-Language": "en",
			"X-Requested-With": "XMLHttpRequest",
			"Dnt": "1",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-origin",
			"Te": "trailers"
		})
		if cookie != None:
			print(cookie)
			self.sesh.headers.update({
			"cookie": f"sessionid={cookie['sessionid']}; sessionid_sign={cookie['sessionid_sign']};",
			"Host": "www.tradingview.com",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
			"Accept": "*/*",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate",
			"Referer": "https://www.tradingview.com/chart/lf4zb40L/?symbol=BLACKBULL%3ASPX500",
			"X-Language": "en",
			"X-Requested-With": "XMLHttpRequest",
			"Dnt": "1",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-origin",
			"Te": "trailers"
		})
		self.request = self.sesh.request
    
    
    
    
    
    
    
	""" https://scanner.tradingview.com/ """
	def getGlobalData(self, ticker: str = None) -> json: # working
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
		self.sesh.headers.clear()
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
			if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
			elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
			else: return {"error": "unknown error", "status": req.status_code, "response": req.text}




	
	def getCoinData(self, market: str, preset: str) -> json: # working
		data = {
				"columns":[
					"base_currency_desc",
					"base_currency_logoid",
					"type",
					"market_cap_calc",
					"exchange",
					"typespecs"
				],
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
			
		self.sesh.headers.clear()
		req = self.sesh.post("https://scanner.tradingview.com/coin/scan", data=json.dumps(data))
		reqJson = req.json()
		if req.status_code == 200:
			pharsedData = {
				"baseCurrencyDesc": req.json()["data"],
	
				
			}

			return pharsedData
		else:
			if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
			elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
			else: return {"error": "unknown error", "status": req.status_code, "response": req.text}



   
	"""https://www.tradingview.com/api/v1/"""
 

	def getCustomSymbolList(self, symboID: str = None) -> json: # working
		req = self.sesh.get(f"https://www.tradingview.com/api/v1/symbols_list/custom/{symboID}")

		reqJson = req.json()
		if req.status_code == 200:
			return reqJson
		else:
			if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
			elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
			else: return {"error": "unknown error", "status": req.status_code, "response": req.text}
   
   
	def getActiveSymbols(self) -> json: # working
		req = self.sesh.get(f"https://www.tradingview.com/api/v1/symbols_list/active")
		reqJson = req.json()
		if req.status_code == 200:
			return reqJson
		if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
		elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
		else: return {"error": "unknown error", "status": req.status_code, "response": req.text}


	def getCustomSymbolListColored(self) -> json: # working
		
		req = self.sesh.get(f"https://www.tradingview.com/api/v1/symbols_list/colored")

		reqJson = req.json()
		if req.status_code == 200:
			return reqJson
		else:
			return {"error": reqJson["error"], "status": req.status_code, "response": req.text}



	def getBrokerPanelNews(self) -> json: #
		self.sesh.headers.clear()
		req = self.sesh.get(f"https://www.tradingview.com/api/v1/brokers/trading_panel")

		reqJson = req.json()
		if req.status_code == 200:
			return reqJson
		else:
			if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
			elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
			else: return {"error": "unknown error", "status": req.status_code, "response": req.text}
	"""
https://news-headlines.tradingview.com/v2/
https://pine-facade.tradingview.com/pine-facade/list
https://www.tradingview.com/pubscripts-library/editors-picks

	"""
	def getNews(self, category: str = None, lang: str = "en") -> json: # working
		self.sesh.headers.clear()
		self.sesh.params = {
			"category": category,
			"client": "overview",
			"lang": lang
		}
		req = self.sesh.get(f"https://news-headlines.tradingview.com/v2/headlines")

		reqJson = req.json()
		if req.status_code == 200:
			return reqJson
		else:
			if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
			elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
			else: return {"error": "unknown error", "status": req.status_code, "response": req.text}


	def getIndicators(self, filter: str = "standard") -> json: # working
		self.sesh.headers.clear()
		self.sesh.params = {
			"filter": filter
		}
		req = self.sesh.get(f"https://pine-facade.tradingview.com/pine-facade/list")

		reqJson = req.json()
		if req.status_code == 200:
			return reqJson
		else:
			if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
			elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
			else: return {"error": "unknown error", "status": req.status_code, "response": req.text}


	def getPopularIndicators(self) -> json:
		self.sesh.headers.clear()

		req = self.sesh.get(f"https://www.tradingview.com/pubscripts-library/editors-picks")

		reqJson = req.json()
		if req.status_code == 200:
			return reqJson
		else:
			if reqJson["detail"]: return {"detail": reqJson["detail"], "status": req.status_code, "response": req.text}
			elif reqJson["error"]: return {"error": reqJson["error"], "status": req.status_code, "response": req.text}
			else: return {"error": "unknown error", "status": req.status_code, "response": req.text}
