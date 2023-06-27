from requests import sessions




class tradingVeiwPublic():
	def __init__(self, cookie: str = None) -> None:
		sesh = sessions()
		self.sesh = sesh
		sesh.headers.update("""
			"cookie": "sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%2BjZNdIQ%3D",
			"Host": "scanner.tradingview.com",
			"Cookie": "cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={"analytics":true,"advertising":true}; _gid=GA1.2.704054866.1686337824; _sp_ses.cf1a=*; _gat_gtag_UA_24278967_1=1; _sp_id.cf1a=01cd3c5e-82a2-4585-aca3-85196c82d85e.1686022716.4.1686417372.1686337824.fad9316a-f9ea-4a0c-86da-59daaa7f08b3; _ga=GA1.1.1116477781.1686022716; _ga_YVVRYGL0E0=GS1.1.1686417069.4.1.1686417372.45.0.0",
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
		""")
    
	""" https://scanner.tradingview.com/ """
	def getGlobalData():
		pass


	def getCoinData():
		pass	


	def getStockData():
		pass

	"""https://www.tradingview.com/api/v1/"""
 
	def getStudyTemplates():
		pass

	def getCustomSymbolList():
		pass

	def getCustomSymbolListColored():
		pass

	def getBrokerPanelNews():
		pass

	"""
https://news-headlines.tradingview.com/v2/
https://pine-facade.tradingview.com/pine-facade/list
https://www.tradingview.com/pubscripts-library/editors-picks

	"""
	def getNews():
		pass

