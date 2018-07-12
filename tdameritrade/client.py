import os
import requests
from .urls import ACCOUNTS


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
            resp = requests.get(ACCOUNTS, headers=self._headers())
            if resp.status_code == 200:
                for account in resp.json():
                    ret[account['securitiesAccount']['accountId']] = account
        return ret
