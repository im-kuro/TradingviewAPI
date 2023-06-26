

# Here are all the public endpoint with limited access to data and functionality.
(most of this was written by chatGPT lmao so if you see a issue lmk)


https://scanner.tradingview.com/
## Scanner Endpoints
- POST /global/scan
- POST /coin/scan
- POST /america/scan



https://news-headlines.tradingview.com/v2/
## News Endpoints
- GET /headlines
-
-



https://www.tradingview.com/api/v1/
## API Endpoints
- GET /study-templates
- GET /symbols_list/custom/
- GET /symbols_list/active
- GET /symbols_list/colored
- GET /brokers/trading_panel






## Endpoints documentation

- Please note some requests do not need headers. in fact im sure most public endpoints dont need headers, so have fun with that.

---

### Request

The request should be made using the following parameters:

- **URL:** `https://scanner.tradingview.com/global/scan`
- **Method:** POST

#### Headers

The following headers should be included in the request:

```
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

This code sends a POST request to the API endpoint, retrieves the response, and extracts the relevant data from the JSON response.
---




















---


This documentation provides information on how to use the TradingView Coin Scanner API to retrieve cryptocurrency data. The API allows you to send a POST request to the endpoint `https://scanner.tradingview.com/coin/scan` in order to scan for specific coins and retrieve relevant information.

### Request

The request should be made using the following parameters:

- **URL:** `https://scanner.tradingview.com/coin/scan`
- **Method:** POST

#### Headers

The following headers should be included in the request:

```
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

### Request

The request should be made using the following parameters:

- **URL:** `https://scanner.tradingview.com/america/scan`
- **Method:** POST

#### Headers

The following headers should be included in the request:

```
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
Cookie: sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%2BjZNdIQ%3D
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

### Request

The request should be made using the following parameters:

- **URL:** `https://news-headlines.tradingview.com/v2/headlines`
- **Method:** GET

#### Headers

The following headers should be included in the request:

```
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
    "Cookie": "sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%2BjZNdIQ%3D"
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

### Request

The request should be made using the following parameters:

- **URL:** `https://www.tradingview.com/api/v1/study-templates`
- **Method:** GET

#### Headers

The following headers should be included in the request:

```
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
Cookie: sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%2BjZNdIQ%3D
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
					},
						...
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
					},
						...
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

### Get Brokers Trading Panel

Retrieve information about brokers available on TradingView's trading panel.

#### Request

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
    'cookie': 'sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%2BjZNdIQ%3D'
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

## TradingView Symbols List API Documentation

This documentation provides information on how to use the TradingView Symbols List API to retrieve a custom symbols list from TradingView. A symbols list contains a collection of symbols (e.g., stocks, cryptocurrencies, forex pairs) that can be used for analysis and tracking.

### Request

The request should be made using the following parameters:

- **URL:** `https://www.tradingview.com/api/v1/symbols_list/custom/`
- **Method:** POST

#### Headers

No specific headers are required for this request.

#### Cookies

The following cookie should be included in the request:

```
Cookie: sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%2BjZNdIQ%3D
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
    "Cookie": "sessionid=zn6h0b7vl3jk6m0ktqf5ox85aga2i57l; sessionid_sign=v1%3AFvYQ99BUyRHVIg9Tv6GcLWIrOnSNpN3wA0Nj%

2BjZNdIQ%3D"
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


## GET /symbols_list/active (same as /symbols_list/custom/ but not in an array, more testing to be done)


Retrieves the list of symbols for a custom watchlist.

### Request

```bash
GET /api/v1/symbols_list/active
```

### Response

```json
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
```

**Response Breakdown:**

- `id` (integer): The unique identifier of the watchlist.

- `type` (string): The type of the watchlist.

- `name` (string): The name of the watchlist.

- `symbols` (array): An array of symbols in the watchlist.

- `active` (boolean): Indicates if the watchlist is active.

- `shared` (boolean): Indicates if the watchlist is shared.

- `color` (null): The color associated with the watchlist.

- `description` (null): The description of the watchlist.

- `created` (string): The timestamp of when the watchlist was created.

- `modified` (string): The timestamp of when the watchlist was last modified.


---




---


## GET /symbols_list/colored

For each symbol you have saved that has a colored marker, this endpoint will return the symbol and the color associated with it.
(no real use for this endpoint tbh lol)

### Request

```bash
GET /api/v1/symbols_list/colored
```

### Response

```json
{
[
   {
      "id":102392177,
      "type":"colored",
      "name":"",
      "symbols":[
         "BLACKBULL:SPX500"
      ],
      "shared":false,
      "color":"red",
      "description":null,
      "created":"2023-01-31T15:58:06.743304Z",
      "modified":"2023-06-19T19:31:02.555269Z"
   },
   {
      "id":115246003,
      "type":"colored",
      "name":"",
      "symbols":[
         "OANDA:EURJPY"
      ],
      "shared":false,
      "color":"green",
      "description":null,
      "created":"2023-06-19T19:31:01.003480Z",
      "modified":"2023-06-19T19:31:02.555269Z"
   },
   {
      "id":115246004,
      "type":"colored",
      "name":"",
      "symbols":[
         "FX:GBPJPY"
      ],
      "shared":false,
      "color":"purple",
      "description":null,
      "created":"2023-06-19T19:31:02.554022Z",
      "modified":"2023-06-19T19:31:02.555269Z"
   },
   {
      "id":115246002,
      "type":"colored",
      "name":"",
      "symbols":[
         "FX:GBPUSD"
      ],
      "shared":false,
      "color":"blue",
      "description":null,
      "created":"2023-06-19T19:30:59.786175Z",
      "modified":"2023-06-19T19:31:02.555269Z"
   }
}
```

**Response Breakdown:**
- `id` (integer): The unique identifier of the watchlist.

- `type` (string): The type of the watchlist.

- `name` (string): The name of the watchlist.

- `symbols` (array): An array of symbols with that color.

- `shared` (boolean): Indicates if the watchlist is shared.

- `color` (string): The color associated with the watchlist.

- `description` (string): The description of the watchlist.

- `created` (string): The timestamp of when the watchlist was created.

- `modified` (string): The timestamp of when the watchlist was last modified.

---



---


## 



### Request

```bash

```

### Response

```json

```

**Response Breakdown:**
- `id` (integer): The unique identifier of the watchlist.


---
