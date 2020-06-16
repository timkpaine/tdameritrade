from tdameritrade.orders import orders


def test_build_buy_market_stock_order():
    symbol = "XYZ"
    quantity = 15
    order = orders.build_buy_market_stock_order(symbol, quantity).asdict()

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

    assert expected_order_dict == order


def test_build_buy_limit_option_order():
    symbol = "XYZ_032015C49"
    quantity = 10
    price = "6.45"
    order = orders.build_buy_limit_option_order(symbol, quantity, price).asdict()

    expected_order_dict = {
        "complexOrderStrategyType": "NONE",
        "orderType": "LIMIT",
        "session": "NORMAL",
        "price": price,
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegCollection": [
            {
            "instruction": "BUY_TO_OPEN",
            "quantity": quantity,
            "instrument": {
                "symbol": symbol,
                "assetType": "OPTION"
                }
            }
        ]
    }
    assert expected_order_dict == order


def test_build_buy_limit_vertical_call_spread_order():
    buy_symbol = "XYZ_011516C40"
    sell_symbol = "XYZ_011516C42.5"
    quantity = 10
    price = "1.20"

    order = orders.build_buy_limit_vertical_call_spread_order(
        buy_symbol,
        sell_symbol,
        quantity,
        price
    )

    order_dict = order.asdict()

    expected_order_dict = {
        "orderType": "NET_DEBIT",
        "session": "NORMAL",
        "price": "1.20",
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegCollection": [
            {
                "instruction": "BUY_TO_OPEN",
                "quantity": 10,
                "instrument": {
                    "symbol": "XYZ_011516C40",
                    "assetType": "OPTION"
                }
            },
            {
                "instruction": "SELL_TO_OPEN",
                "quantity": 10,
                "instrument": {
                    "symbol": "XYZ_011516C42.5",
                    "assetType": "OPTION"
                }
            }
        ]
    }

    assert expected_order_dict == order_dict


def test_build_custom_option_spread_order():
    buy_quantity = 2
    buy_symbol = "XYZ_011720P43"
    
    sell_quantity = 1
    sell_symbol = "XYZ_011819P45"  

    order = orders.build_custom_option_spread_order(buy_symbol, sell_symbol, buy_quantity, sell_quantity)

    order_dict = order.asdict()

    expected_dict = {    
        "orderStrategyType": "SINGLE",
        "orderType": "MARKET",
        "orderLegCollection": [
            {
                "instrument": {
                    "assetType": "OPTION",
                    "symbol": "XYZ_011819P45"
                },
                "instruction": "SELL_TO_OPEN",
                "quantity": 1
            },
            {
                "instrument": {
                    "assetType": "OPTION",
                    "symbol": "XYZ_011720P43"
                },
                "instruction": "BUY_TO_OPEN",
                "quantity": 2
            }
        ],
        "complexOrderStrategyType": "CUSTOM",
        "duration": "DAY",
        "session": "NORMAL"
    }
    assert expected_dict == order_dict
