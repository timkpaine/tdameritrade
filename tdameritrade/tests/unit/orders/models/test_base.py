from tdameritrade.orders.models import base


def test_base_order_json():
    base_order = base.BaseOrder()
    base_order.some_field = 123

    assert base_order.json() == '{}'
