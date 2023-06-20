# Here are all the private endpoints
(most of this was written by chatGPT lmao so if you see a issue lmk)


https://charts-storage.tradingview.com/
## Chart Info endpoints
- GET /charts-storage/get/layout/<UID>/sources







## JWT Tokens
Trading view uses JWT tokens to auth SOME requests. these tokens are used to auth users for the private api. They
use a base64 encoded JWT token that can be decoded to get the user id and other info. The token is passed in as a query param.
using RS512 they encrypt the token, The public key is used to decrypt the token. The public key is stored in the KID value aka (Key ID)

JWT token decoded json
{
2 items
"header":{
	3 items
	"alg":"RS512"
	"kid":"Ahwb"
	"typ":"JWT"
}
	"payload":{
		7 items
		"iss":"tv_chart"
		"iat":1686337200
		"exp":1687204800
		"type":"owner"
		"layoutId":"000000000"
		"ownerId":00000000
		"shared":false
	}
}
### Explanation

algRS512 = the algorithm used for signing the JWT

kid = the thumbprint for the public key used to verify this token

typ = always set to "JWT"

iss = the authorization server that issued the JWT

iat = the time at which the JWT was issued

exp = the expiration time after which JWT must not be accepted

type = owner

layoutI = unique id for the layout

ownerId = unique id for the owner

shared = unknown (boolean)






---


## GET /get/layout/<UID>/sources

This API endpoint retrieves all the items present on a chart, including lines, boxes, fib, and more.

### Request

```bash
GET /charts-storage/get/layout/<UID>/sources
```

### Response

The response is a JSON object with the following structure:

```json
{
  "success": true,
  "payload": {
    "sources": {
      "<source_id>": {
        "id": "<source_id>",
        "symbol": "<symbol>",
        "ownerSource": "<owner_source>",
        "currencyId": "<currency_id>",
        "serverUpdateTime": <server_update_time>,
        "state": {
          "type": "<tool_type>",
          "id": "<source_id>",
          "state": {
            "color": "<color>",
            "fillBackground": <fill_background>,
            "backgroundColor": "<background_color>",
            "linewidth": <linewidth>,
            "transparency": <transparency>,
            "showLabel": <show_label>,
            "horzLabelsAlign": "<horizontal_labels_alignment>",
            "vertLabelsAlign": "<vertical_labels_alignment>",
            "textColor": "<text_color>",
            "fontSize": <font_size>,
            "bold": <bold>,
            "italic": <italic>,
            "extendLeft": <extend_left>,
            "extendRight": <extend_right>,
            "symbolStateVersion": <symbol_state_version>,
            "zOrderVersion": <z_order_version>,
            "visible": <visible>,
            "frozen": <frozen>,
            "symbol": "<symbol>",
            "currencyId": "<currency_id>",
            "unitId": <unit_id>,
            "title": "<title>",
            "text": "<text>",
            "interval": "<interval>"
          },
          "points": [
            {
              "time_t": <timestamp_1>,
              "offset": <offset_1>,
              "price": <price_1>
            },
            {
              "time_t": <timestamp_2>,
              "offset": <offset_2>,
              "price": <price_2>
            },
            ...
          ],
          "zorder": <z_order>,
          "ownerSource": "<owner_source>",
          "linkKey": "<link_key>",
          "sharingMode": <sharing_mode>
        }
      },
      ...
    }
  }
}
```

**Response Breakdown:**
- `success` (boolean): Indicates whether the request was successful or not.
- `payload` (object): Contains the retrieved chart items.
  - `sources` (object): Contains the individual chart items.
    - `<source_id>`: An identifier for a specific chart item.
      - `id` (string): The same identifier as `<source_id>`.
      - `symbol` (string): The symbol associated with the chart item.
      - `ownerSource` (string): The owner source of the chart item.
      - `currencyId` (string): The currency ID associated with the chart item.
      - `serverUpdateTime` (integer): The timestamp of the server update time.
      - `state` (object): The state of the chart item.
        - `type` (string): The type of the tool used for the chart item.
        - `id` (string): The same identifier as `<source_id>`.
        - `state` (object): The specific state details of the chart item.
          - Various properties describing the chart item's appearance and characteristics.
        - `points` (array): An array of points representing the chart item's data.
          - `time_t` (integer): The timestamp of a point on the chart.
          - `offset` (integer): The offset

 of a point on the chart.
          - `price` (float): The price value of a point on the chart.
        - `zorder` (integer): The z-order value of the chart item.
        - `ownerSource` (string): The owner source of the chart item.
        - `linkKey` (string): The link key associated with the chart item.
        - `sharingMode` (integer): The sharing mode of the chart item.

Note: The response may contain multiple chart items under the `sources` object.

---

