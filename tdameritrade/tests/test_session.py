from mock import patch
import time


@patch('tdameritrade.auth.access_token')
class TestSession:

    def test_init(self, mocked_auth):
        from tdameritrade import session
        s = session.TDASession()
        assert s._accessToken['expires_in'] == -1

    def test_request_headers(self, mocked_auth):
        from tdameritrade import session
        s = session.TDASession()
        s._accessToken['token'] = "testToken"
        s._set_header_auth()
        assert s._headers['Authorization'] == 'Bearer testToken'

    def test_token_age(self, mocked_auth):
        from tdameritrade import session
        s = session.TDASession()
        s._accessToken['created_at'] = time.time() - 60
        assert s._access_token_age_secs() > 59
        assert s._access_token_age_secs() < 61

    def test_is_token_invalid_returns_true(self, mocked_auth):
        from tdameritrade import session
        s = session.TDASession()
        assert s._is_token_invalid()
        s._accessToken['token'] = "testToken"
        s._accessToken['created_at'] = time.time() - 61
        s._accessToken['expires_in'] = 60
        assert s._is_token_invalid()

    def test_is_token_invalid_returns_false(self, mocked_auth):
        from tdameritrade import session
        s = session.TDASession()
        s._accessToken['token'] = "testToken"
        s._accessToken['created_at'] = time.time() - 60
        s._accessToken['expires_in'] = time.time() + 1
        assert s._is_token_invalid() == 0

    def test_update_access_token_if_expired(self, mocked_auth):
        from tdameritrade import session
        s = session.TDASession()
        with patch('tdameritrade.auth.access_token') as mock:
            s._refresh_token_if_invalid()
            mock.assert_called_with(s._refreshToken['token'], s._client_id)
