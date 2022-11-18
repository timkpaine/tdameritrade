import requests
import time
from . import auth


class TDASession(requests.Session):
    def __init__(self, refresh_token=None, client_id=None):
        super().__init__()
        self._refreshToken = {"token": refresh_token}
        self._accessToken = {
            "token": "",
            "created_at": time.time(),
            "expires_in": -1,
        }  # Set to -1 so that it gets refreshed immediately and its age tracked.
        self._client_id = client_id
        self._headers = {}

    def _set_header_auth(self):
        self._headers.update({"Authorization": "Bearer " + self._accessToken["token"]})

    def request(self, *args, **kwargs):
        self._refresh_token_if_invalid()
        return super().request(headers=self._headers, *args, **kwargs)

    def _is_token_invalid(self):
        if (
            not self._accessToken["token"]
            or self._access_token_age_secs() >= self._accessToken["expires_in"] - 60
        ):
            return True
        else:
            return False

    def _refresh_token_if_invalid(self):
        # Expire the token one minute before its expiration time to be safe
        if self._is_token_invalid():
            token = auth.access_token(self._refreshToken["token"], self._client_id)
            self._set_access_token(token)

    def _set_access_token(self, token):
        self._accessToken["token"] = token["access_token"]
        self._accessToken["created_at"] = time.time()
        self._accessToken["expires_in"] = token["expires_in"]
        self._set_header_auth()

    def _access_token_age_secs(self):
        return time.time() - self._accessToken["created_at"]
