# TradingView API (Unofficial)

### GitHub: im-kuro | Twitter: @devkuro
[Linktree](https://linktr.ee/devkuro) ❤️

This repository provides unofficial documentation for the TradingView API. It serves as a collection of information about the TradingView API and includes various endpoints along with additional resources. Additionally, a Python wrapper is being developed to automate the process of retrieving data from TradingView. If you find this documentation helpful, you can support the project by following my social media accounts or joining my Discord community.

## Table of Contents

- [Public API Overview](#public-api-overview-apiv1)
    - [Scanner Endpoints](#scanner-endpoints)
    - [API Endpoints](#api-endpoints)
    - [News Endpoints](#news-endpoints)
- [Private API Overview](#private-api-overview-apiv1)
    - [Endpoints](#endpoints)
- [Miscellaneous/Non-API](#miscellaneousnon-api)

## Public API Overview /api/v1

### Endpoints

**Scanner Endpoints:**

- [POST /global/scan](https://github.com/im-kuro/TradingveiwAPI/tree/main#post-globalscan)
- [POST /coin/scan](https://github.com/im-kuro/TradingveiwAPI/tree/main#post-coinscan)
- [POST /america/scan](https://github.com/im-kuro/TradingveiwAPI/tree/main#post-americascan)

**API Endpoints:**

- [GET /study-templates](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-study-templates)
- [GET /symbols_list/custom/](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-symbols-listcustom)
- [GET /symbols_list/active](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-symbols-listactive)
- [GET /symbols_list/colored](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-symbols-listcolored)

**News Endpoints:**

- [GET /headlines](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-headlines)

## Private API Overview /api/v1

### Endpoints

- [GET /unreads/get](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-unreadsget) - Retrieve the current unread notifications for your account.

## Miscellaneous/Non-API

- [GET https://www.tradingview.com/notifications-data](https://github.com/im-kuro/TradingveiwAPI/tree/main#get-httpswwwtradingviewcomnotifications-data) - Retrieve the current number of notifications.

---
