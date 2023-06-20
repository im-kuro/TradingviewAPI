

# Here are all the public endpoint with limited access to data and functionality.
(most of this was written by chatGPT lmao so if you see a issue lmk)


https://scanner.tradingview.com/
## Scanner Endpoints
- POST /global/scan
- POST /coin/scan
- POST /america/scan



https://www.tradingview.com/api/v1/
## API Endpoints
- GET /study-templates
- GET /symbols_list/custom/
- GET /symbols_list/active
- GET /symbols_list/colored
- GET /brokers/trading_panel

https://news-headlines.tradingview.com/v2/
## News Endpoints
- GET /headlines
-
-





## Endpoints documentation



---

### POST - https://scanner.tradingview.com/global/scan

**Payload:**

```json
{
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
  "range": [0, 3],
  "symbols": {
    "tickers": ["SP:SPX"]
  }
}
```

**Options:**
- None

**Payload Breakdown:**

- `columns`: An array of column names to retrieve in the response.

- `range`: A range specifying the start and end index of the result set.

- `symbols`: An object containing ticker symbols.



**Response:**

```json
{
  "totalCount": 1,
  "data": [
    {
      "s": "SP:SPX",
      "d": [
        4325.28,
        3491.58,
        null,
        null,
        4099.12,
        4322.62,
        1.36429766,
        3.74371944,
        9.86768964,
        8.71737937,
        4.80830885,
        11.56362485,
        0.39685315,
        2569400000
      ]
    }
  ]
}
```

**Response Breakdown:**

- `totalCount`: The total count of results returned in the response.

- `data`: An array containing the data for each symbol.

  - `s`: The symbol for which data is provided.

  - `d`: An array containing the data values for the symbol.


---






---

### POST - /america/scan

**Payload:**

```json
{
  "columns": ["description", "logoid", "type"],
  "ignore_unknown_fields": false,
  "options": {
    "lang": "en"
  },
  "range": [0, 6],
  "markets": ["america"],
  "preset": "volume_leaders"
}
```

**Options:**

- `lang`: Language option (in this case, set to "en").

**Payload Breakdown:**

- `columns`: An array of column names to retrieve in the response.

- `ignore_unknown_fields`: A boolean value indicating whether to ignore unknown fields in the payload.

- `options`: An object containing additional options.

- `range`: A range specifying the start and end index of the result set.

- `markets`: An array specifying the market to scan.

- `preset`: The preset to use for the scan.

**Response:**

```json
{
  "totalCount": 4848,
  "data": [
    {
      "s": "AMEX:TMBR",
      "d": [
        "Timber Pharmaceuticals, Inc.",
        "timber-pharmaceuticals",
        "stock"
      ]
    }
  ],
  "params": {
    "america": {
      "symbols": {
        "query": {
          "types": [
            "stock",
            "fund",
            "dr",
            "structured"
          ]
        }
      },
      "filter": [
        {
          "left": "exchange",
          "operation": "in_range",
          "right": [
            "AMEX",
            "NASDAQ",
            "NYSE"
          ]
        },
        {
          "left": "is_primary",
          "operation": "equal",
          "right": true
        },
        {
          "left": "typespecs",
          "operation": "has",
          "right": "common"
        },
        {
          "left": "typespecs",
          "operation": "has_none_of",
          "right": "preferred"
        },
        {
          "left": "type",
          "operation": "equal",
          "right": "stock"
        },
        {
          "left": "active_symbol",
          "operation": "equal",
          "right": true
        }
      ],
      "sort": {
        "sortBy": "relative_volume_10d_calc",
        "sortOrder": "desc",
        "nullsFirst": false
      },
      "options": {
        "lang": "en"
      }
    }
  }
}
```

**Response Breakdown:**

- `totalCount`: The total count of results returned in the response.

- `data`: An array containing the data for each symbol.

  - `s`: The symbol for which data is provided.

  - `d`: An array containing the data values for the symbol.

- `params`: Additional parameters related to the query and filtering.


---






---

### POST - /coin/scan

**Payload:**

```json
{
  "columns": [
    "base_currency_desc",
    "base_currency_logoid",
    "type",
    "market_cap_calc",
    "exchange",
    "typespecs"
  ],
  "ignore_unknown_fields": false,
  "options": {
    "lang": "en"
  },
  "range": [0, 9],
  "markets": ["coin"],
  "preset": "coin_market_cap_rank"
}
```

**Options:**

- `lang`: Language option (in this case, set to "en").

**Payload Breakdown:**

- `columns`: An array of column names to retrieve in the response.

- `ignore_unknown_fields`: A boolean value indicating whether to ignore unknown fields in the payload.

- `options`: An object containing additional options.

- `range`: A range specifying the start and end index of the result set.

- `markets`: An array specifying the market to scan.

- `preset`: The preset to use for the scan.


**Response:**

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
        499283284255.42,
        "CRYPTO",
        ["crypto", "cryptoasset", "synthetic"]
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
        ["crypto", "cryptoasset", "synthetic"]
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
        ["crypto", "cryptoasset", "synthetic"]
      ]
    }
  ]
}
```

**Response Breakdown:**

- `totalCount`: The total count of results returned in the response.
- `data`: An array containing the data for each symbol.
  - `s`: The symbol for which data is provided.
  - `d`: An array containing the data values for the symbol.

---



---

### GET - /v2/headlines

**Endpoint:**
```
https://news-headlines.tradingview.com/v2/headlines?category=base&client=overview&lang=en
```

**Description:**
This endpoint retrieves headlines from TradingView's news service. It allows you to filter headlines by category, client, and language.

**Payload:**
N/A (GET request does not include a payload.)

**Options:**
- `category`: Specifies the category of the headlines. In this example, the value is set to `base`.

- `client`: Specifies the client for which the headlines are requested. In this example, the value is set to `overview`.

- `lang`: Specifies the language of the headlines. In this example, the value is set to `en`.


**Response:**


The response will contain an array of headline items. Each item has the following properties:

- `id`: The unique identifier of the headline (`benzinga:83599eeec094b:0` in the example).

- `title`: The title of the headline (`Bitcoin Conference 2024: Swapping Miami Heat For Nashville Beats` in the example).

- `provider`: The provider of the headline (`benzinga` in the example).

- `sourceLogoId`: The ID of the source's logo (`benzinga` in the example).

- `published`: The timestamp of when the headline was published (1686587469 in the example).

- `source`: The source of the headline (`Benzinga` in the example).

- `urgency`: The urgency level of the headline (2 in the example).

- `link`: The URL of the full article (`https://www.benzinga.com/markets/cryptocurrency/23/06/32779449/
bitcoin-conference-2024-swapping-miami-heat-for-nashville-beats` in the example).

- `permission`: The permission level for accessing the headline (`preview` in the example).

- `storyPath`: The path to the news story (`/news/benzinga:83599eeec094b:0-bitcoin-conference-2024-swapping-miami-heat-for-nashville-beats/` in the example).
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
Please note that the provided JSON response represents a single headline item. The actual response may contain multiple items in the `items` array.

---



---

### GET - /api/v1/study-templates

**Endpoint:**
```
https://www.tradingview.com/api/v1/study-templates
```

**Description:**
This endpoint retrieves a list of study templates from TradingView's API. Study templates are pre-configured sets of indicators that can be applied to charts for technical analysis.

**Payload:**
N/A (GET request does not include a payload.)

**Options:**
N/A (No specific options available for this endpoint.)


**Response:**



The response will contain an object with a `standard` property, which holds an array of study templates. Each study template has the following properties:
- `id`: The unique identifier of the study template.

- `name`: The name of the study template.

- `meta_info`: Additional metadata for the study template, including the following properties:

  - `indicators`: An array of indicators used in the study template, where each indicator has the following properties:

    - `id`: The identifier of the indicator.

    - `description`: The description of the indicator.

  - `interval`: The interval for which the study template is applicable (if specified).


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
    }
  ]
}
```

In the example response, there are two study templates: "Bill Williams' 3 Lines" and "Displaced EMA". Each template includes a list of indicators used in the study template, along with their respective descriptions.

---


---

### GET - /api/v1/brokers/trading_panel

**Endpoint:**
```
https://www.tradingview.com/api/v1/brokers/trading_panel
```

**Description:**
This endpoint retrieves information about a specific broker's trading panel. The trading panel provides details about the broker, including contact information, trading instruments offered, fees, regulations, promotions, and more.

**Payload:**
N/A (GET request does not include a payload.)

**Options:**
N/A (No specific options available for this endpoint.)

**Response:**
The response will contain an array of objects, each representing a broker's trading panel. Each trading panel object has the following properties:

- `id`: The unique identifier of the broker's trading panel.

- `flags`: An array of flags representing the features or awards associated with the broker.

- `flags_verbose`: An array of verbose descriptions for the flags.

- `country_info`: Information about the country where the broker is located, including address, phone number, website, tradable instruments types, 
minimum deposit, maximum leverage, fees, promotions, regulations, and more.

- `slug_name`: The slug name of the broker.

- `name`: The name of the broker.

- `hidden`: Indicates whether the broker is hidden or not.

- `rating`: The rating of the broker.

- `username`: The username associated with the broker.

- `header_image`: The URL of the header image for the broker.

- `logo_square`: The URL of the square logo for the broker.

- `plan`: The plan ID of the broker.

- `plan_verbose`: The verbose description of the plan.

- `reviews_count`: The total number of reviews for the broker.

- `user_review_status`: Indicates whether the user has reviewed the broker or not.



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
      },
      "site": {
        "link": "https://www.tradestation.com/?utm_source=tradingview&utm_medium=referral&utm_content=Broker+Page+-+Contacts",
        "text": "www.tradestation.com"
      },
      "address": "8050 SW 10th Street,  Plantation, FL 33324, US",
      "phone": "+1 800-328-9861",
      "twitter": "TradeStation",
      "tradable_instruments_types": [
        [
          "stock",
          "Stocks"
        ],
        [
          "crypto",
          "Crypto"
        ],
        [
          "futures",
          "Futures"
        ]
      ],
      "min_deposit": "0.00",
      "max_leverage": null,
      "fees": "Micro futures: $0.25 per contract\r\nFutures: $0.75 per contract\r\nStocks: $0\r\nOptions: $0.60 per contract",
      "fees_short": null,
      "promotion": "$0.25 on micros and $0.75 on standard contracts",
      "promotion_link": {
        "link": "https://www.tradestation.com/promo/tradingview-pricing-focused-7/",
        "text": "www.tradestation.com"
      },
      "promotion_short": "New futures pricing!",
      "spread": null,
      "regulation": [
        {
          "abbreviation": "CFTC",
          "name": "Commodity Futures Trading Commission",
          "territory": "USA"
        },
        {
          "abbreviation": "FinCEN",
          "name": "Financial Crimes Enforcement Network",
          "territory": "USA"
        },
        {
          "abbreviation": "FINRA",
          "name": "Financial Industry Regulatory Authority, Inc.",
          "territory": "USA"
        },
        {
          "abbreviation": "NFA",
          "name": "National Futures Association",
          "territory": "USA"
        },
        {
          "abbreviation": "SEC",
          "name": "U.S. Securities and Exchange Commission",
          "territory": "USA"
        },
        {
          "abbreviation": "FCA",
          "name": "Financial Conduct Authority ",
          "territory": "United Kingdom"
        },
        {
          "abbreviation": "State MSB",
          "name": "Money Services Business",
          "territory": "USA"
        }
      ],
      "flags": [
        "open_account"
      ],
      "referral_link": {
        "link": "https://www.tradestation.com/",
        "text": "www.tradestation.com"
      }
    },
    "slug_name": "TRADESTATION",
    "name": "TradeStation",
    "hidden": false,
    "rating": 4.45,
    "username": "TradeStation",
    "header_image": "https://s3.tradingview.com/brokers/headers/TS-TradingView-Hero.svg",
    "logo_square": "https://s3.tradingview.com/brokers/logo/TradeStation_logo_square.svg",
    "plan": 3,
    "plan_verbose": "platinum",
    "reviews_count": 8926,
    "user_review_status": false
  }
]
```

In the example response, there is a single trading panel object for TradeStation. It includes various information about the broker, such as flags, country info, address, phone number, website, tradable instrument types, fees, promotions, regulations, and more.

---



---

## GET - /symbols_list/custom/

Retrieves the list of symbols for a custom watchlist.

### Request

```bash
GET /api/v1/symbols_list/custom/
```

### Response

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
