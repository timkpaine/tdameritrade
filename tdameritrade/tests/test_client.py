# for Coverage
from mock import patch, MagicMock
import pytest

from mock import MagicMock, patch


@pytest.fixture
def tdclient():
    from tdameritrade import TDClient
    tdc = TDClient(client_id=123,
                   refresh_token='reftoken',
                   account_ids=[1, 2])
    return tdc


class TestExtension:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_init(self, tdclient):
        assert (tdclient._refreshToken == 'reftoken')

    def test_request(self, tdclient):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]
            tdclient._request("http://goodurl.com", None)

    def test_request_exception(self, tdclient):
        from tdameritrade.exceptions import InvalidAuthToken
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 401
            with pytest.raises(InvalidAuthToken):
                tdclient._request("http://goodurl.com", None)

    def test_accounts(self, tdclient):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]
            tdclient.accounts()
            m.return_value.json.return_value = [{'test': 1, 'test2': 2}]
            tdclient.accountsDF()

    def test_search(self, tdclient):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdclient.search('aapl')
            tdclient.searchDF('aapl')

    def test_instrument(self, tdclient):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdclient.instrument('aapl')
            tdclient.instrumentDF('aapl')

    def test_quote(self, tdclient):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdclient.quote('aapl')
            tdclient.quoteDF('aapl')

    def test_history(self, tdclient):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'candles': [{'datetime': 1, 'test2': 2}]}
            tdclient.history('aapl')
            tdclient.historyDF('aapl')

    def test_movers(self):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test'}}

#    @pytest.fixture
#    def json_order(self):
#        from tdameritrade.tests.JSONS import TEST_BUY_MARKET_STOCK

#    def test_place_order(self, json_order, tdclient):
#        with patch('tdameritrade.session.TDASession.request') as m:
#            m.return_value.status_code = 201
#            m.return_value.json.return_value = [MagicMock()]
#            tdclient.place_order('1234567', json_order)
#            m.assert_called_with('POST',
#                                 'https://api.tdameritrade.com/v1/accounts/1234567/orders',
#                                 params=None,
#                                 json=None)

#    def test_post_saved_orders(self, json_order, tdclient):
#        with patch('tdameritrade.session.TDASession.request') as m:
#            m.return_value.status_code = 201
#            m.return_value.json.return_value = [MagicMock()]
#            tdclient.create_saved_order('1234567', json_order)
#            m.assert_called_with('POST',
#                                 'https://api.tdameritrade.com/v1/accounts/1234567/savedorders',
#                                 params=None,
#                                 json=json_order)
