from tdameritrade.orders.constants import Session


def test_constant_list():
    for constant in Session.list():
        assert Session(constant) in Session
