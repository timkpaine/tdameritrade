# for Coverage
from mock import patch, MagicMock


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

    def test_init(self):
        from tdameritrade import TDClient
        tdc = TDClient('test')
        tdc._headers()

    def test_accounts(self):
        from tdameritrade import TDClient

        tdc = TDClient('test', [1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]
            tdc.accounts()

        tdc = TDClient('test', [1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [MagicMock()]

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = [{'test': 1, 'test2': 2}]
            tdc.accountsDF()

    def test_search(self):
        from tdameritrade import TDClient

        tdc = TDClient('test', [1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdc.search('aapl')
            tdc.searchDF('aapl')

    def test_instrument(self):
        from tdameritrade import TDClient

        tdc = TDClient('test', [1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdc.instrument('aapl')
            tdc.instrumentDF('aapl')

    def test_quote(self):
        from tdameritrade import TDClient

        tdc = TDClient('test', [1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test': 1, 'test2': 2}}
            tdc.quote('aapl')
            tdc.quoteDF('aapl')

    def test_history(self):
        from tdameritrade import TDClient

        tdc = TDClient('test', [1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'candles': [{'datetime': 1, 'test2': 2}]}
            tdc.history('aapl')
            tdc.historyDF('aapl')

    def test_movers(self):
        from tdameritrade import TDClient

        tdc = TDClient('test', [1, 2])

        with patch('requests.get') as m:
            m.return_value.status_code = 200
            m.return_value.json.return_value = {'aapl': {'test'}}
