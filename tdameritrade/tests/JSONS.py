TEST_BUY_MARKET_STOCK = '''
{
  "orderType": "MARKET",
  "session": "NORMAL",
  "duration": "DAY",
  "orderStrategyType": "SINGLE",
  "orderLegCollection": [
    {
      "instruction": "Buy",
      "quantity": 15,
      "instrument": {
        "symbol": "XYZ",
        "assetType": "EQUITY"
      }
    }
  ]
}
'''