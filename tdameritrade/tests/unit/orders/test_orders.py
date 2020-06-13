import json

from tdameritrade.orders import orders


def test_build_buy_market_stock_order():
    symbol = "AAPL"
    quantity = 123
    order = orders.build_buy_market_stock_order(symbol, quantity)
    json_str = order.json()
    actual_order_dict = json.loads(json_str)
    expected_order_dict = {
        "duration": "DAY",
        "orderLegCollection": [
            {
                "instruction": "BUY",
                "instrument": {"assetType": "EQUITY", "symbol": symbol},
                "quantity": quantity,
            }
        ],
        "orderStrategyType": "SINGLE",
        "orderType": "MARKET",
        "session": "NORMAL",
    }

    assert expected_order_dict == actual_order_dict
