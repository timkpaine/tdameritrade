import json

from tdameritrade.orders import orders


def test_build_buy_market_stock_order():
    symbol = "AAPL"
    quantity = 123
    order = orders.build_buy_market_stock_order(symbol, quantity)
    assert order.json() == ""
