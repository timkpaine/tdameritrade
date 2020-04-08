import pytest
from mock import MagicMock


class TestExceptions:

    def test_can_call(self):
        from tdameritrade.exceptions import TDAAPIError
        TDAAPIError()

    def test_handle_error_response(self):
        from tdameritrade.exceptions import handle_error_response, InvalidAuthToken
        resp = MagicMock(status_code=401)

        with pytest.raises(InvalidAuthToken):
            handle_error_response(resp)
