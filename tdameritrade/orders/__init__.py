"""Orders Submodule

This module is used to construct valid json for the place orders endpoint.
https://developer.tdameritrade.com/account-access/apis/post/accounts/%7BaccountId%7D/orders-0

The validation is done by the orders.models.base.BaseOrder class

The order_builder file incudes sample order builder functions created from
https://developer.tdameritrade.com/content/place-order-samples
"""

from . import order_builder

__all__ = ["order_builder"]
