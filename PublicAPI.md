

# Here are all the public endpoint with limited access to data and functionality.
(most of this was written by chatGPT lmao so if you see a issue lmk)

Please note the trading veiw api is very limited. This is just a list of all the endpoints i could find and wrote docs for. If you find more please make 
a pull request or dm me on discord


https://scanner.tradingview.com/
## Scanner Endpoints
scanner enpoints are mainly for getting data about the market
- POST [/global/scan](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#get-global-market-data)
- POST [/coin/scan](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#get-cryptocurrency-data)
- POST [/america/scan](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#get-american-stocks)

https://www.tradingview.com/api/v1/
## API Endpoints
api endpoints are mainly for getting data about the user or their settings itself
- GET [/study-templates](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#study-templates)
- GET [/symbols_list/custom](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#get-your-custom-symbols-list)
- GET [/symbols_list/colored](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#get-symbiol-list-colors)
- GET [/brokers/trading_panel](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#get-brokers-trading-panel)



https://news-headlines.tradingview.com/v2/
https://pine-facade.tradingview.com/pine-facade/list
https://www.tradingview.com/pubscripts-library/editors-picks
## Misc Endpoints
Misc endpoints are mainly for random things that i see no use for but are still there
- GET [/headlines](https://github.com/im-kuro/TradingviewAPI/blob/main/PublicAPI.md#get-news-headlines)
- GET [/pine-facade/list](https://github.com/im-kuro/TradingveiwAPI/blob/main/PublicAPI.md#)
- GET [/pubscripts-library/editors-picks](https://github.com/im-kuro/TradingveiwAPI/blob/main/PublicAPI.md#)
- GET [/quote_cache_http/snapshot](https://github.com/im-kuro/TradingveiwAPI/blob/main/PublicAPI.md#Get-symbol-data)
- GET [/conversation-status]()
- GET [/notifications-data]()
- GET [/drawing-templates/LineToolHorzRay]()





## Endpoints documentation

- Please note some requests do not need headers. in fact, im sure most public endpoints dont need headers so have fun with that.

---
## Get global market data
### Request

The request should be made using the following parameters:

- **URL:** `https://scanner.tradingview.com/global/scan`
- **Method:** POST

#### Headers

```http
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Content-Length: 240
Content-Type: text/plain;charset=UTF-8
Cookie: cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={"analytics":true,"advertising":true}; _gid=; _sp_ses.cf1a=*; _gat_gtag_UA_24278967_1=1; _sp_id.cf1a=; _ga=; _ga_YVVRYGL0E0=;
Host: scanner.tradingview.com
Origin: https://www.tradingview.com
Referer: https://www.tradingview.com/
Sec-Ch-Ua: 
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: ""
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36
```

#### Data

The request body should contain the following JSON data:

```json
{
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
      3
   ],
   "symbols":{
      "tickers":[
         "SP:SPX"
      ]
   }
}
```

The `columns` field specifies the data fields you want to retrieve for each stock symbol. In the example above, the requested fields include the 52-week high and low prices, sector, country, 1-month low and high prices, weekly performance, 1-month performance, 3-month performance, 6-month performance, yearly performance, year-to-date performance, recommendation, and average volume.

The `range` field specifies the range of data you want to retrieve. In the example above, it is set to `[0, 3]`, which means you want to retrieve data for the first 3 symbols found.

The `symbols` field contains the list of stock symbols you want to scan for. In the example above, it scans for the symbol "SP:SPX".

### Response

The API will respond with a JSON object containing the requested data. Here's an example response:

```json
{
	"totalCount": 1,
	"data": [
		{
			"s": "SP:SPX",
			"d": [
				4375.37,
				3491.58,
				null,
				null,
				4103.98,
				4375.37,
				2.31777381,
				5.60100905,
				12.73234728,
				10.40756675,
				13.86579472,
				13.41840349,
				0.52622378,
				2445100000
			]
		}
	]
}
```

The `totalCount` field indicates the total number of symbols found in the scan. In this example, it is set to 1.

The `data` field contains an array of objects, where each object represents a stock symbol and its corresponding data. In the example above, the data for the symbol "SP:SPX" is provided.

#### Python Example

Here's an example Python code snippet to parse the response and extract the data:

```python
import requests
import json

url = "https://scanner.tradingview.com/global/scan"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Length": "240",
    "Content-Type": "text/plain;charset=UTF-8",
    "Host": "scanner.tradingview.com",
    "Origin": "https://www.tradingview.com",
    "Referer": "https://www.tradingview.com/",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '""',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
    "Cookie": "sessionid=; sessionid_sign="
}

data = {
    "columns": [
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
    "range": [
        0,
        3
    ],
    "symbols": {
        "tickers": [
            "SP:SPX"
        ]
    }
}

response = requests.post(url, headers=headers, json=data)
data = response.json()

# Extracting the data
totalCount = data["totalCount"]
symbolData = data["data"][0]


symbol = symbolData["s"]
symbolValues = symbolData["d"]

print(f"Total Count: {totalCount}")
print(f"Symbol: {symbol}")
print(f"Data: {symbolValues}")
```

---




















---


This documentation provides information on how to use the TradingView Coin Scanner API to retrieve cryptocurrency data. The API allows you to send a POST request to the endpoint `https://scanner.tradingview.com/coin/scan` in order to scan for specific coins and retrieve relevant information.
## Get cryptocurrency data
### Request

The request should be made using the following parameters:

- **URL:** `https://scanner.tradingview.com/coin/scan`
- **Method:** POST

#### Headers

The following headers should be included in the request:

```http
Host: scanner.tradingview.com
Content-Length: 224
Sec-Ch-Ua: 
Accept: application/json
Content-Type: text/plain;charset=UTF-8
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36
Sec-Ch-Ua-Platform: \"\"
Origin: https://www.tradingview.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.tradingview.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Cookie: _sp_ses.cf1a=*; _sp_id.cf1a=
```

#### Data

The request body should contain the following JSON data:

```json
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
      2
   ],
   "markets":[
      "coin"
   ],
   "preset":"coin_market_cap_rank"
}
```

The `columns` field specifies the data fields you want to retrieve for each coin. In the example above, the requested fields include the base currency description, base currency logo ID, type, market capitalization, exchange, and typespecs.

The `ignore_unknown_fields` field is set to `false`, indicating that unknown fields should not be ignored.

The `options` field allows you to specify additional options. In this example, the `lang` option is set to "en" for English.

The `range` field specifies the range of data you want to retrieve. In the example above, it is set to `[0, 2]`, which means you want to retrieve data for the first 2 coins.

The `markets` field specifies the markets to scan. In this example, it scans the "coin" market.

The `preset` field is set to "coin_market_cap_rank", indicating that the data should be sorted based on the coin market capitalization rank.

### Response

The API will respond with a JSON object containing the requested data. Here's an example response:

```json
{
	"totalCount": 749,
	"data": [
		{
			"s": "CRYPTO:BTCUSD",
			"d": [
				"Bitcoin",
				"crypto/XTVCBTC",
				"spot",
        500857765687.17,
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
				208756093358.23952,
				"CRYPTO",
				[
					"crypto",
					"cryptoasset",
					"synthetic"
				]
			]
		}
	],
	"params": {
		"coin": {
			"symbols": {
				"query": {
					"typespecs": [
						"cryptoasset"
					]
				}
			},
			"sort": {
				"sortBy": "crypto_total_rank",
				"sortOrder": "asc",
				"nullsFirst": false
			},
			"options": {
				"lang": "en"
			}
		}
	}
}
```

The `totalCount` field indicates the total number of coins found in the scan. In this example, it is set to 749.

The `data` field contains an array of objects, where each object represents a coin and its corresponding data. Each object contains an `s` field representing the symbol of the coin and a `d` field containing an array of data values for the coin.

### Python Example

Here's an example Python code snippet to parse the response and extract the data:

```python
import requests
import json

url = "https://scanner.tradingview.com/coin/scan"
headers = {
    "Host": "scanner.tradingview.com",
    "Content-Length": "224",
    "Sec-Ch-Ua": "",
    "Accept": "application/json",
    "Content-Type": "text/plain;charset=UTF-8",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Sec-Ch-Ua-Platform": "\"\"",
    "Origin": "https://www.tradingview.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.tradingview.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close",
    "Cookie": "_sp_ses.cf1a=*; _sp_id.cf1a="
}

data = {
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
      2
   ],
   "markets":[
      "coin"
   ],
   "preset":"coin_market_cap_rank"
}

response = requests.post(url, headers=headers, json=data)
data = response.json()

totalCount = data["totalCount"]
coinData = data["data"]

for coin in coinData

:
    symbol = coin["s"]
    values = coin["d"]
    print("Symbol:", symbol)
    print("Values:", values)
    print()
```

This example uses the `requests` library to send the HTTP POST request to the API endpoint and retrieve the response. The response is then parsed as JSON, and the coin symbols and values are extracted and printed.


---
























---

This documentation provides information on how to use the TradingView Scanner API to perform a scan for stocks in the American market based on preset criteria.
## Get american stocks
### Request

The request should be made using the following parameters:

- **URL:** `https://scanner.tradingview.com/america/scan`
- **Method:** POST

#### Headers

The following headers should be included in the request:

```http
Accept: application/json
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Length: 151
Content-Type: text/plain;charset=UTF-8
Host: scanner.tradingview.com
Origin: https://www.tradingview.com
Referer: https://www.tradingview.com/
Sec-Ch-Ua:
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: ""
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36
```

#### Cookies

The following cookie should be included in the request:

```
Cookie: sessionid=; sessionid_sign=
```

#### Request Body

The request body should be a JSON object with the following fields:

- `columns`: An array of column names to include in the response. In the example, the columns are `["description", "logoid", "type"]`.
- `ignore_unknown_fields`: A boolean value indicating whether to ignore unknown fields. In the example, it's set to `false`.
- `options`: An object containing additional options. In the example, the `lang` option is set to `"en"`.
- `range`: An array specifying the range of results to retrieve. In the example, it's set to `[0, 9]`.
- `markets`: An array specifying the markets to scan. In the example, only the American market is specified.
- `preset`: A string specifying the preset criteria for the scan. In the example, the preset is set to `"losers"`.

### Response

The API will respond with a JSON object containing the scan results. The response includes the following fields:

- `totalCount`: The total count of results matching the scan criteria.
- `data`: An array of objects representing the scan results. Each object has the following fields:
  - `s`: The symbol of the stock.
  - `d`: An array containing data related to the stock, such as its description, logoid, and type.

Here's an example response:

```json
{
	"totalCount": 2566,
	"data": [
		{
			"s": "NASDAQ:BAOS",
			"d": [
				"Baosheng Media Group Holdings Limited",
				"baosheng-media-limited",
				"stock"
			]
		},
		{
			"s": "NYSE:PL",
			"d": [
				"Planet Labs PBC",
				"planet-labs",
				"stock"
			]
		},
		{
			"s": "NASDAQ:PEPG",
			"d": [
				"PepGen Inc.",


				"",
				"stock"
			]
		}
	]
}
```

This example shows three scan results, each represented by an object in the `data` array. Each object contains the symbol (`s`) and data (`d`) related to the stock.

---




























---
This documentation provides information on how to use the TradingView News Headlines API to retrieve news headlines related to financial markets. The API allows you to send a GET request to the endpoint `https://news-headlines.tradingview.com/v2/headlines` with specific parameters to filter the news articles.
## Get news headlines
### Request

The request should be made using the following parameters:

- **URL:** `https://news-headlines.tradingview.com/v2/headlines`
- **Method:** GET

#### Headers

The following headers should be included in the request:

```http
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Host: news-headlines.tradingview.com
Origin: https://www.tradingview.com
Referer: https://www.tradingview.com/
Sec-Ch-Ua: 
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: ""
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36
```

### Response

The API will respond with a JSON object containing the requested news headlines. Here's an example response:

```json
{
	"items": [
		{
			"id": "benzinga:83599eeec094b:0",
			"title": "Bitcoin Conference 2024: Swapping Miami Heat For Nashville Beats",
			"provider": "benzinga",
			"sourceLogoId": "benzinga",
			"published": 1686587469,
			"source": "Benzinga",
			"urgency": 2,
			"link": "https://www.benzinga.com/markets/cryptocurrency/23/06/32779449/bitcoin-conference-2024-swapping-miami-heat-for-nashville-beats",
			"permission": "preview",
			"storyPath": "/news/benzinga:83599eeec094b:0-bitcoin-conference-2024-swapping-miami-heat-for-nashville-beats/"
		}
	]
}
```

The `items` field contains an array of news articles, where each article is represented by an object. In the example above, there is one news article provided.

The fields within each news article object include:

- `id`: The unique identifier of the news article.
- `title`: The title of the news article.
- `provider`: The provider or source of the news article.
- `sourceLogoId`: The logo ID associated with the news source.
- `published`: The timestamp indicating when the article was published.
- `source`: The name of the news source.
- `urgency`: The urgency level of the news article.
- `link`: The URL link to the full article.
- `permission`: The permission level for accessing the article (e.g., "preview").
- `storyPath`: The path to the news story on the TradingView website.

#### Python Example

Here's an example Python code snippet to retrieve and parse the news headlines:

```python
import requests
import json

url = "https://news-headlines.tradingview.com/v2/headlines"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Host": "news

-headlines.tradingview.com",
    "Origin": "https://www.tradingview.com",
    "Referer": "https://www.tradingview.com/",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '""',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Cookie": "sessionid=; sessionid_sign="
}

response = requests.get(url, headers=headers)
data = response.json()

# Extracting the news headlines
items = data["items"]

for item in items:
    newsId = item["id"]
    title = item["title"]
    provider = item["provider"]
    sourceLogoId = item["sourceLogoId"]
    published = item["published"]
    source = item["source"]
    urgency = item["urgency"]
    link = item["link"]
    permission = item["permission"]
    storyPath = item["storyPath"]
    
    # Process the news data as needed
    print(f"News ID: {newsId}")
    print(f"Title: {title}")
    print(f"Provider: {provider}")
    print(f"Source Logo ID: {sourceLogoId}")
    print(f"Published: {published}")
    print(f"Source: {source}")
    print(f"Urgency: {urgency}")
    print(f"Link: {link}")
    print(f"Permission: {permission}")
    print(f"Story Path: {storyPath}")
    print()
```

This code sends a GET request to the API endpoint, retrieves the response, and extracts the relevant data from the JSON response.


---























---

This documentation provides information on how to use the TradingView Study Templates API to retrieve a list of standard study templates available on TradingView. Study templates are pre-configured sets of technical indicators and settings that can be applied to charts for analysis.
## study templates
### Request

The request should be made using the following parameters:

- **URL:** `https://www.tradingview.com/api/v1/study-templates`
- **Method:** GET

#### Headers

The following headers should be included in the request:

```http
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Host: www.tradingview.com
Referer: https://www.tradingview.com/chart/?symbol=SPX
Sec-Ch-Ua:
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: ""
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36
X-Language: en
X-Requested-With: XMLHttpRequest
```

#### Cookies

The following cookie should be included in the request:

```
Cookie: sessionid=; sessionid_sign=
```

### Response

The API will respond with a JSON object containing the list of standard study templates. Each template is represented as an object with the following fields:

- `id`: The unique identifier of the study template.
- `name`: The name of the study template.
- `meta_info`: Additional information about the study template, including the list of indicators and their descriptions, and the interval (if applicable).

Here's an example response:

```json
{
	"standard": [
		{
			"id": 1,
			"name": "Bill Williams' 3 Lines",
			"meta_info": {
				"indicators": [
					{
						"id": "Volume",
						"description": "Volume"
					},
					{
						"id": "MASimple",
						"description": "Moving Average"
					},
					{
						"id": "MASimple",
						"description": "Moving Average"
					},
					{
						"id": "MASimple",
						"description": "Moving Average"
					}
				],
				"interval": null
			}
		},
		{
			"id": 2,
			"name": "Displaced EMA",
			"meta_info": {
				"indicators": [
					{
						"id": "Volume",
						"description": "Volume"
					},
					{
						"id": "MAExp",
						"description": "Moving Average Exponential"
					}
				],
				"interval": null
			}
		},
		{
			"id": 3,
			"name": "MA Exp Ribbon",
			"meta_info": {
				"indicators": [
					{
						"id": "Volume",
						"description": "Volume"
					},
					{
						"id": "MAExp",
						"description": "Moving Average Exponential"
					}
				],
				"interval": null
			}
		},
		{
			"id": 6,
			"name": "Oscillators",
			"meta_info": {
				"indicators": [
					{
						"id": "Volume",
						"description": "Volume"
					}
						
				],
				"interval": null
			}
		},
		{
			"id": 5,
			"name": "Swing Trading",
			"meta_info": {
				"indicators": [
					{
						"id": "ZigZag@tv-basicstudies",
						"description": "Zig Zag"
					}
						
				],
				"interval": null
			}
		}
	]
}
```


---













---


This documentation provides an overview of the TradingView Brokers API and explains the requests and responses involved in retrieving broker information. It also includes simple example Python code to parse the data returned by the API.

## Get Brokers Trading Panel
### Request

**Payload:**
N/A (GET request does not include a payload.)

**Options:**
N/A (No specific options available for this endpoint.)


```python
import requests

url = "https://www.tradingview.com/api/v1/brokers/trading_panel"

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={\"analytics\":true,\"advertising\":true}; _gid=GA1.2.1046925617.1686023754; _sp_ses.cf1a=*; _ga=GA1.2.1116477781.1686022716; _gat_gtag_UA_24278967_1=1; _ga_YVVRYGL0E0=GS1.1.1686069076.2.1.1686071161.45.0.0; _sp_id.cf1a=01cd3c5e-82a2-4585-aca3-85196c82d85e.1686022716.2.1686071161.1686024878.40aed288-6693-47c5-94c2-9943ae540418',
    'Host': 'www.tradingview.com',
    'Referer': 'https://www.tradingview.com/chart/?symbol=SPX',
    'Sec-Ch-Ua': '',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '""',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36',
    'X-Language': 'en',
    'X-Requested-With': 'XMLHttpRequest',
    'cookie': 'sessionid=; sessionid_sign='
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
```

#### Response

```json
[
	{
		"id": 8,
		"flags": [
			"featured",
			"ba_of_the_year",
			"ba_innovative_tech",
			"ba_multi_asset",
			"ba_of_the_year_2021",
			"ba_multi_asset_2021",
			"ba_multi_asset_2022"
		],
		"flags_verbose": [
			"Featured",
			"Broker of the Year 2020",
			"Most Innovative Tech 2020",
			"Best Multi-Asset Broker 2020",
			"Broker of the Year 2021",
			"Best Multi-Asset Broker 2021",
			"Best Multi-Asset Broker 2022"
		],
		"country_info": {
			"countries_codes": [
				"US"
			],
			"countries": [
				"USA"
			],
			"about_ast": {
				"type": "root",
				"children": [
					"TradeStation pursues a singular vision; to offer the ultimate online trading platform and services for self-directed traders and investors across the equities, equity/index options, futures, futures options and cryptocurrencies markets. TradeStation is already a recognized industry leader and is on a mission to build something even better. Equities and Futures accounts are offered by TradeStation Securities, Inc. Crypto accounts are offered by TradeStation Crypto, Inc.\r\n\r\n",
					{
						"type": "url",
						"params": {
							"url": "https://www.tradestation.com/important-information/?utm_source=tradingview&utm_medium=referral&utm_content=Broker%2BPage%2B-%2BImportant%2BDocuments/",
							"linkText": "Important Documents",
							"relFollow": false
						}
					}
				]
			}
    }
  }
]

```


The response is a list of brokers with detailed information for each broker. Here are some key fields returned in the response:

- `id`: The ID of the broker.
- `flags`: Flags associated with the broker.
- `flags_verbose`: Descriptive names for the flags.
- `country_info`: Information about the country where the broker operates.
- `slug_name`: The slug name of the broker.
- `name`: The name of the broker.
- `hidden`: Indicates if the broker is hidden.
- `rating`: The rating of the broker.
- `username`: The username associated with the broker.
- `header_image`: URL of the header image for the broker.
- `logo_square`: URL of the square logo for the broker.
- `plan`: The plan ID of the broker.
- `plan_verbose`: Verbose name for the plan.

---























---


This documentation provides information on how to use the TradingView Symbols List API to retrieve a custom symbols list from TradingView. A symbols list contains a collection of symbols (e.g., stocks, cryptocurrencies, forex pairs) that can be used for analysis and tracking.
## Get your custom symbols list 
### Request

The request should be made using the following parameters:

- **URL:** `https://www.tradingview.com/api/v1/symbols_list/custom/`
- **Method:** POST

#### Headers

```http
Host: www.tradingview.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Language: en
X-Requested-With: XMLHttpRequest
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Cookie:
```

#### Cookies

The following cookie should be included in the request:

```
Cookie: sessionid=; sessionid_sign=
```

### Response

The API will respond with a JSON array containing the custom symbols list. Here's an example response:

```json
[
	{
		"id": 102259501,
		"type": "custom",
		"name": "Watchlist",
		"symbols": [
			"###MAINS",
			"BLACKBULL:SPX500",
			"FX:NAS100",
			"FOREXCOM:XAUUSD",
			"FX:GBPJPY",
			"OANDA:EURJPY",
			"FX:GBPUSD",
			"OANDA:EURUSD",
			"FX:USDJPY",
			"CAPITALCOM:UK100",
			"###INDICES",
			"CURRENCYCOM:EU50"
		],
		"active": true,
		"shared": false,
		"color": null,
		"description": null,
		"created": "2023-01-30T13:30:42.256580Z",
		"modified": "2023-05-26T13:29:00.902122Z"
	}
]
```

The response contains a single object representing the custom symbols list. The fields within the object include:

- `id`: The unique identifier of the symbols list.
- `type`: The type of symbols list (e.g., custom).
- `name`: The name of the symbols list.
- `symbols`: An array of symbols included in the list.
- `active`: Indicates whether the symbols list is active.
- `shared`: Indicates whether the symbols list is shared.
- `color`: The color associated with the symbols list.
- `description`: A description of the symbols list.
- `created`: The date and time when the symbols list was created.
- `modified`: The date and time when the symbols list was last modified.

Please note that the symbols listed in the `symbols` array are represented in different formats, such as exchange-specific symbols (e.g., "BLACKBULL:SPX500") and general market symbols (e.g., "FX:GBPJPY").

#### Python Example

Here's an example Python code snippet to retrieve and process the custom symbols list:

```python
import requests

url = "https://www.tradingview.com/api/v1/symbols_list/custom/"
cookies = {
    "Cookie": "sessionid=; sessionid_sign="
}

response = requests.post(url, cookies=cookies)
data = response.json()

# Extracting the symbols list
symbols_list = data[0]
symbols = symbols_list["symbols"]

# Process the symbols as needed
for symbol in symbols:
    print(symbol)
```

This code snippet uses the `requests` library to send a POST request to the TradingView Symbols List API with the provided cookies. The response is then parsed as JSON, and the symbols list and symbols are extracted and processed accordingly.

Please note that the provided cookies may require authentication or specific session data to work correctly. Adjust them accordingly to your requirements.

I hope this information helps! Let me know if you have any further questions.
---

















---

This documentation provides information on how to retrieve a list of colored symbols using the TradingView API. The API endpoint allows you to retrieve information about colored symbols, including their IDs, names, colors, and associated symbols.
## Get symbiol list colors
### Request

To retrieve the colored symbols list, make a `GET` request to the following endpoint:

```
https://www.tradingview.com/api/v1/symbols_list/colored
```

Include the following headers in your request:

```http
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.5
Dnt: 1
Host: www.tradingview.com
Referer: https://www.tradingview.com/chart/lf4zb40L/?symbol=BLACKBULL%3ASPX500
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0
X-Language: en
X-Requested-With: XMLHttpRequest
cookie: 
```


### Response

The API response will be a JSON array containing multiple colored symbols objects. Each object represents a colored symbol and contains the following properties:

- `id` (integer): The ID of the colored symbol.
- `type` (string): The type of the colored symbol, which is always "colored".
- `name` (string): The name of the colored symbol.
- `symbols` (array): An array of symbols associated with the colored symbol.
- `shared` (boolean): Indicates whether the colored symbol is shared or not.
- `color` (string): The color assigned to the colored symbol.
- `description` (string): The description of the colored symbol (nullable).
- `created` (string): The date and time when the colored symbol was created.
- `modified` (string): The date and time when the colored symbol was last modified.

#### Example Response

```json
[
  {
    "id": 102392177,
    "type": "colored",
    "name": "",
    "symbols": [
      "BLACKBULL:SPX500"
    ],
    "shared": false,
    "color": "red",
    "description": null,
    "created": "2023-01-31T15:58:06.743304Z",
    "modified": "2023-06-19T19:31:02.555269Z"
  },
  {
    "id": null,
    "type": "colored",
    "name": "",
    "active": false,
    "color": "orange",
    "created": null,
    "modified": null,
    "symbols": []
  },
  {
    "id": 115246003,
    "type": "colored",
    "name": "",
    "symbols": [
      "OANDA:EURJPY"
    ],
    "shared": false,
    "color": "green",
    "description": null,
    "created": "2023-06-19T19:31:01.003480Z",
    "modified": "2023-06-19T19:31:02.555269Z"
  },
  {
    "id": 115246004,
    "type": "colored",
    "name": "",
    "symbols": [
      "FX:GBPJPY"
    ],
    "shared": false,
    "color": "purple",
    "description": null,
    "created": "2023-06-19T19:31:02.554022Z",
    "modified": "2023-06-19T19:31:02.555269Z"
  },
  {
    "id": 115246002,
    "type": "colored",
    "name": "",
    "symbols": [
      "FX:GBPUSD"
    ],
    "shared": false,
    "color": "blue",
    "description": null,
    "created": "2023-06-19T19:30:59.786175Z",
    "modified": "2023-06-19T19:31:02.555269Z"
  },
  {
    "id": null,
    "type": "colored",
    "name": "",
    "active": false,
    "color": "cyan",
    "created": null,
    "modified": null,
    "symbols": []
  },
  {
    "id": null,
    "type": "colored",
    "name": "",
    "active": false,
    "color": "pink",
    "created": null,
    "modified": null,
    "symbols": []
  }
]
```

### Python Example

Here's a simple example Python code snippet to parse the response and extract relevant information:

```python
import requests

url = "https://www.tradingview.com/api/v1/symbols_list/colored"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Dnt": "1",
    "Host": "www.tradingview.com",
    "Referer": "https://www.tradingview.com/chart/lf4zb40L/?symbol=BLACKBULL%3ASPX500",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "X-Language": "en",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "sessionid=; sessionid_sign="
}

response = requests.get(url, headers=headers)
data = response.json()

# Extract relevant information
for colored_symbol in data:
    id = colored_symbol.get("id")
    type = colored_symbol.get("type")
    name = colored_symbol.get("name")
    symbols = colored_symbol.get("symbols")
    shared = colored_symbol.get("shared")
    color = colored_symbol.get("color")
    description = colored_symbol.get("description")
    created = colored_symbol.get("created")
    modified = colored_symbol.get("modified")

    # Do something with the extracted

 information (e.g., print)
    print(f"ID: {id}")
    print(f"Type: {type}")
    print(f"Name: {name}")
    print(f"Symbols: {symbols}")
    print(f"Shared: {shared}")
    print(f"Color: {color}")
    print(f"Description: {description}")
    print(f"Created: {created}")
    print(f"Modified: {modified}")
    print("\n")
```


---






















---


## Get scripts
### Request

The API endpoint for retrieving the list of scripts is:

- **URL:** `/pine-facade/list?filter=standard`
- **Method:** GET

### Request Headers

The following headers are required for making the request:

```http
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.5
Dnt: 1
Host: pine-facade.tradingview.com
Origin: https://www.tradingview.com
Referer: https://www.tradingview.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Te: trailers
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
Cookie: sessionid=; sessionid_sign=
```

### Response

The API will respond with a JSON array containing information about the scripts. Here is an example response:

```json
[
	{
		"userId": 605017,
		"scriptName": "24-hour Volume",
		"scriptSource": "",
		"scriptAccess": "open_no_auth",
		"scriptIdPart": "STD;24h%Volume",
		"version": "3.0",
		"extra": {
			"isAuto": false,
			"isBeta": false,
			"isBuiltIn": true,
			"isNew": false,
			"isPineEditorNewTemplate": true,
			"isUpdated": false,
			"kind": "study",
			"shortDescription": "24H Vol",
			"sourceInputsCount": 1,
			"tags": []
		}
	},
	{
		"userId": 605017,
		"scriptName": "Accumulation/Distribution",
		"scriptSource": "",
		"scriptAccess": "open_no_auth",
		"scriptIdPart": "STD;Accumulation_Distribution",
		"version": "27.0",
		"extra": {
			"isAuto": false,
			"isBeta": false,
			"isBuiltIn": true,
			"isMTFResolution": true,
			"isNew": false,
			"isPineEditorNewTemplate": true,
			"isUpdated": false,
			"kind": "study",
			"shortDescription": "Accum/Dist",
			"sourceInputsCount": 0,
			"tags": []
		}
	}
]
```

Each object in the array represents a script and provides the following information:

- `userId`: The ID of the user who created the script.
- `scriptName`: The name of the script.
- `scriptSource`: The source code of the script (empty in this case).
- `scriptAccess`: The access level of the script (e.g., "open_no_auth").
- `scriptIdPart`: The unique identifier for the script.
- `version`: The version of the script.
- `extra`: Additional details about the script, such as its type, description, and tags.

###

 Python Example

Here's a simple example Python code that demonstrates how to parse the data from the API response:

```python
import requests
import json

url = 'https://pine-facade.tradingview.com/pine-facade/list?filter=standard'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Dnt': '1',
    'Host': 'pine-facade.tradingview.com',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Te': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Cookie': 'sessionid=; sessionid_sign='
}

response = requests.get(url, headers=headers)
data = response.json()

for script in data:
    print("Script Name:", script["scriptName"])
    print("Script ID:", script["scriptIdPart"])
    print("Version:", script["version"])
    print("Access Level:", script["scriptAccess"])
    print("Description:", script["extra"]["shortDescription"])
    print("Tags:", script["extra"]["tags"])
    print()
```

---




























---


## Popular Scripts
### Request

- **URL**: `https://www.tradingview.com/pubscripts-library/editors-picks`
- **Method**: GET

#### Headers
```http
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.5
Dnt: 1
Host: www.tradingview.com
Referer: https://www.tradingview.com/chart/lf4zb40L/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
X-Language: en
X-Requested-With: XMLHttpRequest
Cookie: sessionid=; sessionid_sign=
```
### Response

```json
{
	"next": "/pubscripts-library/editors-picks/?c=Im8iOiItcGlja2VkX3RpbWUiLCJ2IjpbIjIwMjMtMDQtMjZUMTM6MDk6MTAuNjcwMTk5Il0",
	"results": [
		{
			"imageUrl": "0h0gKNcy",
			"scriptName": "120x ticker screener (composite tickers)",
			"scriptSource": "",
			"access": 1,
			"scriptIdPart": "PUB;005f1fe5ec46477c829e6bdb00543018",
			"version": "1",
			"extra": {
				"kind": "study",
				"sourceInputsCount": 0
			},
			"agreeCount": 142,
			"editorsPick": true,
			"author": {
				"id": 1052332,
				"username": "fikira",
				"is_broker": false
			}
		},
		{
			"imageUrl": "xGnUhodO",
			"scriptName": "Open Interest Chart [LuxAlgo]",
			"scriptSource": "",
			"access": 1,
			"scriptIdPart": "PUB;1a3525503519483996e955001638d6ac",
			"version": "1",
			"extra": {
				"kind": "study",
				"sourceInputsCount": 0
			},
			"agreeCount": 765,
			"editorsPick": true,
			"author": {
				"id": 1049752,
				"username": "LuxAlgo",
				"is_broker": false
			}
		}
	]
}
```

### Example Python Code

Here's an example code snippet in Python to parse the response data:

```python
import requests
import json

url = "https://www.tradingview.com/pubscripts-library/editors-picks"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Dnt": "1",
    "Host": "www.trading

view.com",
    "Referer": "https://www.tradingview.com/chart/lf4zb40L/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "X-Language": "en",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "sessionid=; sessionid_sign="
}

response = requests.get(url, headers=headers)
data = response.json()

for result in data["results"]:
    print("Script Name:", result["scriptName"])
    print("Author:", result["author"]["username"])
    print("Agree Count:", result["agreeCount"])
    print("---------------------------")
```

This Python code sends a GET request to the specified URL with the provided headers. It then parses the JSON response and prints the script name, author, and agree count for each result in the response.



---






















## Get symbol data

This documentation provides an overview of the TradingView Quote API and explains how to retrieve quote data for multiple symbols using a POST request. The API allows you to fetch various details about financial instruments, including their current session, type, update mode, names, descriptions, prices, and more.

### Request

To retrieve quote data for multiple symbols, make a POST request to the following endpoint:

```
POST https://quotes.tradingview.com/quote_cache_http/snapshot?fields=current_session%2Ctype%2Cupdate_mode%2Coriginal_name%2Cshort_name%2Cpro_name%2Cdescription%2Clocal_description%2Clanguage%2Cfractional%2Cpricescale%2Cminmov%2Cminmove2%2Csymbol_status%2Clp%2Cchp%2Cch%2Clp_time%2Clogoid%2Ccurrency-logoid%2Cbase-currency-logoid%2Crtc%2Crch%2Crchp
```

Include the following headers in your request:

```
origin: https://www.tradingview.com
cookie: sessionid=; sessionid_sign=
```

The `fields` parameter in the URL specifies the specific data fields you want to retrieve.

In the request body, provide an array of symbols for which you want to fetch quote data. Here's an example request body:

```json
[
  "BLACKBULL:SPX500",
  "FOREXCOM:XAUUSD",
  "FX:NAS100"
]
```

### Response

The API will respond with an array of objects, where each object represents the quote data for a symbol. Here's an example response:

```json
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
  },
  {
    "symbol": "FOREXCOM:XAUUSD",
    "s": "ok",
    "data": {
      "current_session": "out_of_session",
      "type": "commodity",
      "update_mode": "streaming",
      "original_name": "FOREXCOM:XAUUSD",
      "short_name": "XAUUSD",
      "pro_name": "FOREXCOM:XAUUSD",
      "description": "Gold / U.S.

 Dollar",
      "local_description": null,
      "language": null,
      "fractional": false,
      "pricescale": 100,
      "minmov": 1,
      "minmove2": 1,
      "symbol_status": "realtime",
      "lp": 1961.2699999999999818,
      "chp": -0.22000000000000000111,
      "ch": -4.2699999999999995737,
      "lp_time": 1686344378,
      "logoid": "metal/gold",
      "currency-logoid": null,
      "base-currency-logoid": null
    }
  }
]
```

For each symbol, the response includes the following details:

- `symbol`: The symbol identifier.
- `s`: Status of the response. In this example, it's set to "ok" indicating a successful response.
- `data`: An object containing the quote data for the symbol.
  - `current_session`: The current session of the symbol.
  - `type`: The type of the symbol (e.g., index, commodity).
  - `update_mode`: The update mode for the symbol's data.
  - `original_name`: The original name of the symbol.
  - `short_name`: A shortened version of the symbol's name.
  - `pro_name`: The professional name of the symbol.
  - `description`: A description of the symbol.
  - `local_description`: The local description of the symbol (if available).
  - `language`: The language of the symbol's data (if specified).
  - `fractional`: Indicates whether the symbol supports fractional values.
  - `pricescale`: The scale factor for prices.
  - `minmov`: The minimum movement for the symbol.
  - `minmove2`: The second minimum movement for the symbol.
  - `symbol_status`: The status of the symbol (e.g., realtime).
  - `lp`: The last price of the symbol.
  - `chp`: The change percentage of the symbol.
  - `ch`: The change value of the symbol.
  - `lp_time`: The timestamp of the last price update.
  - `logoid`: The identifier for the symbol's logo.
  - `currency-logoid`: The identifier for the symbol's currency logo (if available).
  - `base-currency-logoid`: The identifier for the base currency's logo (if available).

### Example Python Code

Here's an example Python code snippet to parse the response and extract the relevant information:

```python
import requests
import json

url = 'https://quotes.tradingview.com/quote_cache_http/snapshot?fields=current_session%2Ctype%2Cupdate_mode%2Coriginal_name%2Cshort_name%2Cpro_name%2Cdescription%2Clocal_description%2Clanguage%2Cfractional%2Cpricescale%2Cminmov%2Cminmove2%2Csymbol_status%2Clp%2Cchp%2Cch%2Clp_time%2Clogoid%2Ccurrency-logoid%2Cbase-currency-logoid%2Crtc%2Crch%2Crchp'
headers = {
    'origin': 'https://www.tradingview.com',
    'cookie': 'sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%2BjZNdIQ%

3D'
}
symbols = ["BLACKBULL:SPX500", "FOREXCOM:XAUUSD", "FX:NAS100"]
data = json.dumps(symbols)

response = requests.post(url, headers=headers, data=data)
response_data = response.json()

for quote in response_data:
    symbol = quote['symbol']
    data = quote['data']
    # Extract and use the required information from the 'data' object
    # For example:
    current_session = data['current_session']
    symbol_type = data['type']
    update_mode = data['update_mode']
    # ... and so on

    # Perform further processing or output the extracted data as needed
```























## Get conversations

Endpoint: `https://www.tradingview.com/conversation-status`

Method: GET

Headers:
```
Host: www.tradingview.com
Sec-Ch-Ua: 
Accept: */*
X-Language: en
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36
Sec-Ch-Ua-Platform: ""
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.tradingview.com/chart/?symbol=SPX
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={"analytics":true,"advertising":true}; _gid=GA1.2.1046925617.1686023754; _sp_ses.cf1a=*; _ga=GA1.2.1116477781.1686022716; _gat_gtag_UA_24278967_1=1; _ga_YVVRYGL0E0=GS1.1.1686069076.2.1.1686071161.45.0.0; _sp_id.cf1a=01cd3c5e-82a2-4585-aca3-85196c82d85e.1686022716.2.1686071161.1686024878.40aed288-6693-47c5-94c2-9943ae540418
```

Parameters:
```
_rand: 0.4846194512399544
offset: 0
room_id: general
stat_interval: D
stat_symbol: SPX
is_private
```

# Response

The response will be a JSON object with the following structure:

```json
{
	"messages": [
		{
			"id": "43036ed4-9041-4f96-80a4-5f5f8946f49a",
			"user_id": 14960951,
			"user_pic": "https://s3.tradingview.com/userpics/14960951-HpJH_mid.png",
			"username": "Honestcowboy",
			"badges": [
				{
					"name": "pro:pro_premium",
					"verbose_name": "Premium"
				}
			],
			"is_moderator": false,
			"text": "Mmm can't share as it can be interpreted as solicitation",
			"type": "",
			"meta": {
				"text": "",
				"interval": "1",
				"links": {},
				"version": "0.2"
			},
			"room_id": "general",
			"symbol": "BINANCE:BTCUSDT",
			"interval": "1",
			"time": "Sun Jun 11 20:32:49 2023 UTC"
		},
		{
			"id": "ef8578a0-982a-46e9-9e54-7b8aee87b4d9",
			"user_id": 14960951,
			"user_pic": "https://s3.tradingview.com/userpics/14960951-HpJH_mid.png",
			"username": "Honestcowboy",
			

	"badges": [
				{
					"name": "pro:pro_premium",
					"verbose_name": "Premium"
				}
			],
			"is_moderator": false,
			"text": "Let me go read house rules before I post a link to my track record",
			"type": "",
			"meta": {
				"text": "",
				"interval": "1",
				"links": {},
				"version": "0.2"
			},
			"room_id": "general",
			"symbol": "BINANCE:BTCUSDT",
			"interval": "1",
			"time": "Sun Jun 11 20:31:38 2023 UTC"
		}
	]
}
```

Example Python code to parse the data:
```python
import requests
import json

url = "https://www.tradingview.com/conversation-status"
headers = {
    "Host": "www.tradingview.com",
    "Sec-Ch-Ua": "",
    "Accept": "*/*",
    "X-Language": "en",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Sec-Ch-Ua-Platform": "",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.tradingview.com/chart/?symbol=SPX",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={\"analytics\":true,\"advertising\":true}; _gid=GA1.2.1046925617.1686023754; _sp_ses.cf1a=*; _ga=GA1.2.1116477781.1686022716; _gat_gtag_UA_24278967_1=1; _ga_YVVRYGL0E0=GS1.1.1686069076.2.1.1686071161.45.0.0; _sp_id.cf1a=01cd3c5e-82a2-4585-aca3-85196c82d85e.1686022716.2.1686071161.1686024878.40aed288-6693-47c5-94c2-9943ae540418"
}

params = {
    "_rand": "0.4846194512399544",
    "offset": "0",
    "room_id": "general",
    "stat_interval": "D",
    "stat_symbol": "SPX",
    "is_private": ""
}

response = requests.get(url, headers=headers, params=params)
data = json.loads(response.text)

# Accessing the messages
messages = data["messages"]
for message in messages:
    message_id = message["id"]
    user_id = message["user_id"]
    user_pic = message["user_pic"]
    username = message["username"]
    badges = message["badges"]
    is_moderator = message["is_moderator"]
    text = message["text"]
    room_id = message["room_id"]
    symbol = message["symbol"]
    interval = message["interval"]
   

 time = message["time"]
    # Process the message as needed
```























## Get notifications and settings

To retrieve user notifications and settings, you can make a GET request to the following URL:

```
https://www.tradingview.com/notifications-data?widget_type=user
```

### Request Headers

Include the following headers in your request:

```
Host: www.tradingview.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.tradingview.com/chart/lf4zb40L/?symbol=BLACKBULL%3ASPX500
X-Language: en
X-Requested-With: XMLHttpRequest
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Cookie: <your_cookie_here>
```

Make sure to replace `<your_cookie_here>` with the appropriate cookie value.

### Response

Upon successful request, you will receive a JSON response containing the user's notifications and settings.

```json
{
	"notifications": [],
	"settings": {
		"notification_follow_user": 3,
		"notification_comment": 3,
		"notification_comment_pine": null,
		"notification_vote": 3,
		"notification_vote_pine": null,
		"notification_mention_in_ideas_comment": 3,
		"notification_mention_in_script_comment": null,
		"notification_mention_in_chat": 3,
		"notification_access_to_script": 1,
		"notification_stream_start": 3,
		"notification_broker_review": null,
		"notification_broker_review_update": null,
		"notification_broker_reply": null,
		"notification_sound": true,
		"notification_popup": true
	}
}
```

The response will contain an empty array for the "notifications" field if there are no notifications. The "settings" field will provide information about various notification preferences and settings.

### Example Python Code

Here's an example Python code snippet that demonstrates how to parse the JSON response:

```python
import requests
import json

url = "https://www.tradingview.com/notifications-data?widget_type=user"
headers = {
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
    "Te": "trailers",
    "Cookie": "<your_cookie_here>"
}

response = requests.get(url, headers=headers)
data = response.json()

# Parsing the response
notifications = data["notifications"]
settings = data["settings"]

# Process the notifications and settings as needed
# ...

# Print the settings for example purposes
print(json.dumps(settings, indent=4))
```

Remember to replace `<your_cookie_here>`

with the appropriate cookie value in the `headers` dictionary before running the code.

This example code demonstrates how to send the request, retrieve the JSON response, and extract the "settings" field from the response for further processing. You can customize the code based on your specific requirements.

















## get drawing templates names

URL: `https://www.tradingview.com/drawing-templates/LineToolHorzRay`
TYPE: `GET`

This endpoint retrieves the names of the saved templates for a specific drawing tool in TradingView. The `LineToolHorzRay` parameter represents the name of the drawing/tool for which you want to retrieve the saved templates.

#### Request Headers:
```
Host: www.tradingview.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.tradingview.com/chart/lf4zb40L/
X-Language: en
X-Requested-With: XMLHttpRequest
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
```

#### Response:

The response is a JSON array containing the names of the saved templates for the specified drawing/tool. Here is an example response:

```json
[
    "1H Liq.",
    "Break Of Structure ",
    "CHoCH",
    "line",
    "Liquidity",
    "Previous Resistance",
    "Previous Supply",
    "Take profit 1",
    "Take profit 2",
    "Take profit 3"
]
```

#### Python Example:

You can use the following Python code to make a request to the TradingView API and parse the response:

```python
import requests

url = 'https://www.tradingview.com/drawing-templates/LineToolHorzRay'

headers = {
    'Host': 'www.tradingview.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.tradingview.com/chart/lf4zb40L/',
    'X-Language': 'en',
    'X-Requested-With': 'XMLHttpRequest',
    'Dnt': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'trailers'
}

response = requests.get(url, headers=headers)
data = response.json()

# Print the names of the saved templates
for template_name in data:
    print(template_name)
```

Remember to replace `'LineToolHorzRay'` in the URL with the actual name of the drawing/tool for which you want to retrieve the saved templates.















