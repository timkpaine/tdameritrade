import os
import requests
import urllib.parse as up
from .urls import ACCOUNTS, INSTRUMENTS, QUOTES, SEARCH, HISTORY, OPTIONCHAIN


class TDClient(object):
    def __init__(self, access_token=None, accountIds=None):
        self._token = access_token or os.environ['ACCESS_TOKEN']
        self.accountIds = accountIds or []

    def _headers(self):
        return {'Authorization': 'Bearer ' + self._token}

    def accounts(self):
        ret = {}
        if self.accountIds:
            for acc in self.accountIds:
                resp = requests.get(ACCOUNTS + str(acc), headers=self._headers())
                if resp.status_code == 200:
                    ret[acc] = resp.json()
                else:
                    raise Exception(resp.text)
        else:
            resp = requests.get(ACCOUNTS, headers=self._headers())
            if resp.status_code == 200:
                for account in resp.json():
                    ret[account['securitiesAccount']['accountId']] = account
            else:
                raise Exception(resp.text)
        return ret

    def search(self, symbol, projection='symbol-search'):
        return requests.get(SEARCH,
                            headers=self._headers(),
                            params={'symbol': symbol,
                                    'projection': projection}).json()

    def instrument(self, cusip):
        return requests.get(INSTRUMENTS + str(cusip),
                            headers=self._headers()).json()

    def quote(self, symbol):
        return requests.get(QUOTES,
                            headers=self._headers(),
                            params={'symbol': symbol.upper()}).json()

    def history(self, symbol):
        return requests.get(HISTORY % symbol,
                            headers=self._headers()).json()

    def options(self, symbol):
        return requests.get(OPTIONCHAIN,
                            headers=self._headers(),
                            params={'symbol': symbol.upper()}).json()
