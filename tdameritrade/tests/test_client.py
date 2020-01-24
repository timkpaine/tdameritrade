# for Coverage
import unittest

from mock import MagicMock, patch


class TestClient(unittest.TestCase):
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

    def test_init(self):
        from tdameritrade import TDClient
        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])
        self.assertEqual(tdc._accessToken['token'], 'accesstoken')

    @patch('tdameritrade.TDClient._refreshTokenIfExpired')
    def test_accounts(self, mock_rtie):
        from tdameritrade import TDClient

        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]
            tdc.accounts()

        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [{'test': 1, 'test2': 2}]
            tdc.accountsDF()

    @patch('tdameritrade.TDClient._refreshTokenIfExpired')
    def test_search(self, mock_rtie):
        from tdameritrade import TDClient

        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdc.search('aapl')
            tdc.searchDF('aapl')

    @patch('tdameritrade.TDClient._refreshTokenIfExpired')
    def test_instrument(self, mock_rtie):
        from tdameritrade import TDClient

        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdc.instrument('aapl')
            tdc.instrumentDF('aapl')

    @patch('tdameritrade.TDClient._refreshTokenIfExpired')
    def test_quote(self, mock_rtie):
        from tdameritrade import TDClient

        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdc.quote('aapl')
            tdc.quoteDF('aapl')

    @patch('tdameritrade.TDClient._refreshTokenIfExpired')
    def test_history(self, mock_rtie):
        from tdameritrade import TDClient

        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'candles': [{'datetime': 1, 'test2': 2}]}
            tdc.history('aapl')
            tdc.historyDF('aapl')

    def test_movers(self):
        from tdameritrade import TDClient

        tdc = TDClient(clientId=123, refreshToken='reftoken',
                       accessToken='accesstoken', accountIds=[1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test'}}
