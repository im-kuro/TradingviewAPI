# Here are all the private endpoints
(most of this was written by chatGPT lmao so if you see a issue lmk)


https://charts-storage.tradingview.com/
## Chart Info endpoints
- GET /charts-storage/get/layout/<UID>/sources







## JWT Tokens

Trading View uses JWT tokens to authenticate certain requests. These tokens are utilized for authorizing users for the private API. The JWT token is in a base64-encoded format and can be decoded to retrieve the user ID and other relevant information. The token is passed as a query parameter.

### Encryption and Decryption

Trading View encrypts the JWT token using the RS512 algorithm. The public key is required to decrypt the token. The public key is stored in the Key ID (KID) value.

### Decoded JWT Token

The decoded JSON structure of the JWT token consists of two main sections: the header and the payload.

#### Header:

- `alg`: RS512 (the algorithm used for signing the JWT)
- `kid`: Ahwb (the thumbprint for the public key used to verify this token)
- `typ`: JWT (always set to "JWT")

#### Payload:

- `iss`: tv_chart (the authorization server that issued the JWT)
- `iat`: 1686337200 (the time at which the JWT was issued)
- `exp`: 1687204800 (the expiration time after which the JWT must not be accepted)
- `type`: owner (type of user)
- `layoutId`: 000000000 (unique ID for the layout)
- `ownerId`: 00000000 (unique ID for the owner)
- `shared`: false (unknown boolean value)

Please note that the "shared" field's purpose is unknown and requires further clarification.

## Explanation

- `alg`: RS512 is the algorithm used for signing the JWT.
- `kid`: The KID is the thumbprint for the public key used to verify this token.
- `typ`: The typ field is always set to "JWT".
- `iss`: The iss field represents the authorization server that issued the JWT.
- `iat`: The iat field indicates the time at which the JWT was issued.
- `exp`: The exp field represents the expiration time after which the JWT must not be accepted.
- `type`: The type field specifies the type of user (in this case, "owner").
- `layoutId`: The layoutId field contains a unique ID for the layout.
- `ownerId`: The ownerId field contains a unique ID for the owner.
- `shared`: The shared field's purpose is unknown, and further information is required for clarification.




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

          - `offset` (integer): The offset of a point on the chart.

          - `price` (float): The price value of a point on the chart.

        - `zorder` (integer): The z-order value of the chart item.

        - `ownerSource` (string): The owner source of the chart item.

        - `linkKey` (string): The link key associated with the chart item.

        - `sharingMode` (integer): The sharing mode of the chart item.


Note: The response may contain multiple chart items under the `sources` object.

---

