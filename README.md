# tdameritrade
Python interface to TD Ameritrade Api

[![Build Status](https://dev.azure.com/tpaine154/tdameritrade/_apis/build/status/timkpaine.tdameritrade?branchName=master)](https://dev.azure.com/tpaine154/tdameritrade/_build/latest?definitionId=8&branchName=master)
[![Coverage](https://img.shields.io/azure-devops/coverage/tpaine154/tdameritrade/8)]()
[![BCH compliance](https://bettercodehub.com/edge/badge/timkpaine/tdameritrade?branch=master)](https://bettercodehub.com/)
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
[Read the docs!](http://tdameritrade.readthedocs.io/en/latest/index.html)

The main interface is the `TDClient` object. You can pass the token to this object, or put it in an environment variable `ACCESS_TOKEN`.

All functionality is available as methods on the `TDClient` object. For most methods, there is a convenience method to return the result as a pandas DataFrame.

![](https://raw.githubusercontent.com/timkpaine/tdameritrade/master/docs/img/client/client.png)

Most data fetching methods accept the symbol as argument. For equities, this is just the ticker.

![](https://raw.githubusercontent.com/timkpaine/tdameritrade/master/docs/img/client/quote.png)

For different assets, utilize the `search` and `instrument` methods to lookup symbols. For options, you can utilize the options method.

![](https://raw.githubusercontent.com/timkpaine/tdameritrade/master/docs/img/options.png)

