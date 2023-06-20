# TradingView API (Unofficial)

### GitHub: im-kuro | Twitter: @devkuro
[Linktree](https://linktr.ee/devkuro) ❤️

No, i do not expect donations though they do help video quality and the kinds of content i make on ALL platforms. i currently have no real (consistent) income from the content i make, but when i do i put it all back into the content 100% of the time. Of course i appreciate all donos and if you dm me your btc/eth addy and a ss of you sending it i will gladly say thanks in the next YouTube video as you guys make it all happen.

**BTC: bc1qh9culj8vlk6qe36apkwcrvr6f37emg5dwa288r**

**ETH: 0x4afB2ACa7B111D572FD01FF7F78b3176305B31E3**

This repository provides unofficial documentation for the TradingView API. It serves as a collection of information about the TradingView API and includes various endpoints along with additional resources. Additionally, a Python wrapper is being developed to automate the process of retrieving data from TradingView. If you find this documentation helpful, you can support the project by following my social media accounts or joining my Discord community.

### API Authentication overveiw

From what ive found so far, the autherizion is just the cookie. It contains "sessionid" witch is a randomly generated string of numbers and letters.
I assume you get the session id when you login though have yet to contune testing that. I have found that the session id is not required for all
endpoints too. There are other things in the cookie that are interesting though not needed from what i know so far, other than that the cookie is
used for what i can only assume is google analytics and other things like that.



## Table of Contents

- [Public API Overview](#public-api-overview-apiv1)
    - [Scanner Endpoints](https://github.com/im-kuro/TradingveiwAPI/blob/main/PublicAPI.md#post---httpsscannertradingviewcomglobalscan)
    - [API Endpoints](https://github.com/im-kuro/TradingveiwAPI/blob/main/PublicAPI.md#post---httpsscannertradingviewcomglobalscan)
    - [News Endpoints](https://github.com/im-kuro/TradingveiwAPI/blob/main/PublicAPI.md#post---httpsscannertradingviewcomglobalscan)


- [Private API Overview](#private-api-overview-apiv1)
    - [Endpoints](#endpoints)


- [Miscellaneous/Non-API](#miscellaneousnon-api)

## Public API Overview /api/v1


### **Scanner Endpoints:**

- [POST /global/scan](https://github.com/im-kuro/TradingveiwAPI/tree/main#post-globalscan)
- [POST /coin/scan](https://github.com/im-kuro/TradingveiwAPI/tree/main#post-coinscan)
- [POST /america/scan](https://github.com/im-kuro/TradingveiwAPI/tree/main#post-americascan)

### **API Endpoints:**

- [GET /study-templates](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-study-templates)
- [GET /symbols_list/custom/](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-symbols-listcustom)
- [GET /symbols_list/active](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-symbols-listactive)
- [GET /symbols_list/colored](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-symbols-listcolored)

### **News Endpoints:**

- [GET /headlines](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-headlines)


## Private API Overview /api/v1



- [GET /unreads/get](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-unreadsget) - Retrieve the current unread notifications for your account.



## Miscellaneous/Non-API

- [GET https://www.tradingview.com/notifications-data](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-httpswwwtradingviewcomnotifications-data) - Retrieve the current number of notifications.

---

