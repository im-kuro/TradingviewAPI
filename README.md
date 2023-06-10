# TradingveiwAPI
### GH: im-kuro  --  TT: @devkuro
https://linktr.ee/devkuro <3


This is **NOT** an offical API documentation. It's just **a collection of information about TradingView API.** If people are interested
in this, I will continue to update this document along with making a python wrapper to automate the process of getting data from TradingView. 
if you like this you can support me with following my socials or joining my discord.


## Public API overveiw /api/v1

### Endpoints 
 **POST /america/scan**
- This endpoint is used to scan the american market for stocks.  it takes diffrent args to return diffrent types of info

 **POST /coin/scan**
- This endpoint is used to scan the crypto market for coins. it takes diffrent args to return diffrent types of info

 **GET /v2/headlines**
- This will return the top latest news headlines from tradingview

 **GET /symbols_list/colored**
- unsure what this does yet

 


## Pricate API overveiw /api/v1

### Endpoints 

 GET /unreads/get
- get the current unread notifications for your account


## misc/non api

 **GET https://www.tradingview.com/notifications-data**
- gets the current amount notifications 





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





