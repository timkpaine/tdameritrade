# for Coverage
from mock import patch, MagicMock
import pytest



@pytest.fixture
def tdclient():
    from tdameritrade import TDClient
    tdc = TDClient('test', [1, 2])
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
        tdclient._headers()

    def test_request(self, tdclient):
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]
            tdclient._request("http://goodurl.com", None)

    def test_request_exception(self, tdclient):
        from tdameritrade.exceptions import InvalidAuthToken
        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 401
            # resp = [{"status_code": 401}]
            # #m.return_value = MagicMock()
            # #m.return_value.status_code = {"status_code": 401}
            # mock = MagicMock()
            # mock.return_value = resp
            # m.return_value = mock
            # #m.return_value.json.return_value = [MagicMock()]

            with pytest.raises(InvalidAuthToken):
                tdclient._request("http://goodurl.com", None)

    def test_accounts(self, tdclient):

        with patch('tdameritrade.session.TDASession.request') as m:

            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]
            tdclient.accounts()

            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]

            m.return_value.status_code = 200
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

    @pytest.fixture
    def json_order(cls):
        from tdameritrade.tests.JSONS import TEST_BUY_MARKET_STOCK

    def test_orders(self, json_order, tdclient):

        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 201
            m.return_value.json.return_value = [MagicMock()]
            tdclient.orders('1234567', json_order)

    def test_saved_orders(self, json_order, tdclient):

        with patch('tdameritrade.session.TDASession.request') as m:
            m.return_value.status_code = 201
            m.return_value.json.return_value = [MagicMock()]
            tdclient.saved_orders('1234567', json_order)

