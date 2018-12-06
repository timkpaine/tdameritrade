import os
import requests
import pandas as pd
from .urls import *


class TDClient(object):
    def __init__(self, access_token=None, refresh_token=None, accountIds=None):
        self._token = access_token or os.environ['ACCESS_TOKEN']
        self._refresh_token = refresh_token or os.environ['REFRESH_TOKEN']
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

    def accountsDF(self):
        return pd.io.json.json_normalize(self.accounts())

    def search(self, symbol, projection='symbol-search'):
        return requests.get(SEARCH,
                            headers=self._headers(),
                            params={'symbol': symbol,
                                    'projection': projection}).json()

    def searchDF(self, symbol, projection='symbol-search'):
        ret = []
        dat = self.search(symbol, projection)
        for symbol in dat:
            ret.append(dat[symbol])
        return pd.DataFrame(ret)

    def instrument(self, cusip):
        return requests.get(INSTRUMENTS + str(cusip),
                            headers=self._headers()).json()

    def instrumentDF(self, cusip):
        return pd.DataFrame(self.instrument(cusip))

    def quote(self, symbol):
        resp = requests.get(QUOTES,
                            headers=self._headers(),
                            params={'symbol': symbol.upper()})
        if resp.status_code == 200:
          return resp.json()
        else:
          if resp.status_code == 401:
            # unauthorized, refresh
            print("Unauthorized, refresh!")
            payload = {'grant_type': 'refresh_token',
                       'refresh_token': self._refresh_token,
                       'client_id': 'VIRGILM@AMER.OAUTHAP'}
            post_resp = requests.post(REFRESH, data = payload)
            print("Resp:", post_resp)
            if post_resp.status_code == 200:
              #token refreshed, update!
              print("New token:  Retrying.")
              self._token = post_resp.json()['access_token']
              resp = requests.get(QUOTES,
                                  headers=self._headers(),
                                  params={'symbol': symbol.upper()})
              if resp.status_code == 200:
                return resp.json()
              else:
                raise Exception(resp.text)
            else:
              raise Exception(post_resp.text)
          else:
            raise Exception(resp.text)

    def quoteDF(self, symbol):
        x = self.quote(symbol)
        return pd.DataFrame(x).T.reset_index(drop=True)

    def history(self, symbol):
        return requests.get(HISTORY % symbol,
                            headers=self._headers()).json()

    def historyDF(self, symbol):
        x = self.history(symbol)
        df = pd.DataFrame(x['candles'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        return df

    def options(self, symbol):
        return requests.get(OPTIONCHAIN,
                            headers=self._headers(),
                            params={'symbol': symbol.upper()}).json()

    def optionsDF(self, symbol):
        ret = []
        dat = self.options(symbol)
        for date in dat['callExpDateMap']:
            for strike in dat['callExpDateMap'][date]:
                ret.extend(dat['callExpDateMap'][date][strike])
        for date in dat['putExpDateMap']:
            for strike in dat['putExpDateMap'][date]:
                ret.extend(dat['putExpDateMap'][date][strike])

        df = pd.DataFrame(ret)
        for col in ('tradeTimeInLong', 'quoteTimeInLong', 'expirationDate', 'lastTradingDay'):
            df[col] = pd.to_datetime(df[col], unit='ms')
        return df
