# tdameritrade
Python interface to TD Ameritrade Api

[![Build Status](https://github.com/timkpaine/tdameritrade/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/timkpaine/tdameritrade/actions?query=workflow%3A%22Build+Status%22)
[![Coverage](https://codecov.io/gh/timkpaine/tdameritrade/branch/main/graph/badge.svg)](https://codecov.io/gh/timkpaine/tdameritrade)
[![License](https://img.shields.io/github/license/timkpaine/tdameritrade.svg)](https://pypi.python.org/pypi/tdameritrade/)
[![PyPI](https://img.shields.io/pypi/v/tdameritrade.svg)](https://pypi.python.org/pypi/tdameritrade/)
[![Docs](https://img.shields.io/readthedocs/tdameritrade.svg)](https://tdameritrade.readthedocs.io)



## Getting Started

### Install
Install from pip

`pip install tdameritrade`

or from source

`python setup.py install`


### Docs
Major changes in the v0.1.0 update to the way tokens are handled.  
You will still need the original authentication instructions, but the TDClient now takes the refresh token and client
id, not the access token. A new session class handles token expiration and will automatically call a new token as
needed. 

It is recommended that you store these as environmental variables.  

```
client_id = os.getenv('TDAMERITRADE_CLIENT_ID')
account_id = os.getenv('TDAMERITRADE_ACCOUNT_ID')
refresh_token = os.getenv('TDAMERITRADE_REFRESH_TOKEN')

tdclient = tdameritrade.TDClient(client_id=client_id, refresh_token=refresh_token, account_ids=[account_id])
``` 

See the tests\test_client.py file for examples on current usage. 

[Read the docs!](http://tdameritrade.readthedocs.io/en/latest/index.html)

All functionality is available as methods on the `TDClient` object. For most methods, there is a convenience method to return the result as a pandas DataFrame.

![](https://raw.githubusercontent.com/timkpaine/tdameritrade/main/docs/img/client/client.png)

Most data fetching methods accept the symbol as argument. For equities, this is just the ticker.

![](https://raw.githubusercontent.com/timkpaine/tdameritrade/main/docs/img/client/quote.png)

For different assets, utilize the `search` and `instrument` methods to lookup symbols. For options, you can utilize the options method.

![](https://raw.githubusercontent.com/timkpaine/tdameritrade/main/docs/img/options.png)

