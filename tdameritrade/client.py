import os
import time

import pandas as pd
import requests

from tdameritrade import auth

from .urls import (ACCOUNTS, HISTORY, INSTRUMENTS, MOVERS, OPTIONCHAIN, QUOTES,
                   SEARCH)

class TDClient(object):

    def __init__(self, clientId=None, refreshToken=None,
                 accessToken=None, accountIds=[]):
        self._clientId = clientId
        self._refreshToken = {'token': refreshToken}
        self._accessToken = {'token': accessToken}
        if not accessToken and 'ACCESS_TOKEN' in os.environ:
            self._accessToken['token'] = os.environ['ACCESS_TOKEN']
        self._accessToken['created_at'] = time.time()
        # Set to -1 so that it gets refreshed immediately and its age tracked.
        self._accessToken['expires_in'] = -1
        self._accountIds = accountIds

    def _headers(self):
        return {'Authorization': 'Bearer ' + self._accessToken['token']}

    def _refreshTokenIfExpired(self):
        # Expire the token one minute before its expiration time to
        # be safe
        if not self._accessToken['token'] or \
                self._accessTokenAgeSecs() >= self._accessToken['expires_in'] - 60:
            token = auth.access_token(self._refreshToken['token'],
                                      self._clientId)
            self._accessToken['token'] = token['access_token']
            self._accessToken['created_at'] = time.time()
            self._accessToken['expires_in'] = token['expires_in']

    def _accessTokenAgeSecs(self):
        return time.time() - self._accessToken['created_at']

    def accounts(self, positions=False, orders=False):
        ret = {}

        if positions or orders:
            fields = '?fields='
            if positions:
                fields += 'positions'
                if orders:
                    fields += ',orders'
            elif orders:
                fields += 'orders'
        else:
            fields = ''

        if self._accountIds:
            for acc in self._accountIds:
                self._refreshTokenIfExpired()
                resp = requests.get(ACCOUNTS + str(acc) + fields,
                                    headers=self._headers())
                if resp.status_code == 200:
                    ret[acc] = resp.json()
                else:
                    raise Exception(resp.text)
        else:
            self._refreshTokenIfExpired()
            resp = requests.get(ACCOUNTS + fields, headers=self._headers())
            if resp.status_code == 200:
                for account in resp.json():
                    ret[account['securitiesAccount']['accountId']] = account
            else:
                raise Exception(resp.text)

        return ret

    def accountsDF(self):
        return pd.io.json.json_normalize(self.accounts())

    def search(self, symbol, projection='symbol-search'):
        self._refreshTokenIfExpired()

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

    def fundamental(self, symbol):
        return self.search(symbol, 'fundamental')

    def fundamentalDF(self, symbol):
        return self.searchDF(symbol, 'fundamental')

    def instrument(self, cusip):
        self._refreshTokenIfExpired()

        return requests.get(INSTRUMENTS + str(cusip),
                            headers=self._headers()).json()

    def instrumentDF(self, cusip):
        return pd.DataFrame(self.instrument(cusip))

    def quote(self, symbol):
        self._refreshTokenIfExpired()

        return requests.get(QUOTES,
                            headers=self._headers(),
                            params={'symbol': symbol.upper()}).json()

    def quoteDF(self, symbol):
        x = self.quote(symbol)

        return pd.DataFrame(x).T.reset_index(drop=True)

    def history(self, symbol, **kwargs):
        self._refreshTokenIfExpired()
        return requests.get(HISTORY % symbol,
                            headers=self._headers(),
                            params=kwargs).json()

    def historyDF(self, symbol, **kwargs):
        x = self.history(symbol, **kwargs)
        df = pd.DataFrame(x['candles'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')

        return df

    def options(self, symbol, **kwargs):
        self._refreshTokenIfExpired()

        return requests.get(OPTIONCHAIN,
                            headers=self._headers(),
                            params={'symbol': symbol.upper(), **kwargs}).json()

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
        for col in ('tradeTimeInLong', 'quoteTimeInLong',
                    'expirationDate', 'lastTradingDay'):
            df[col] = pd.to_datetime(df[col], unit='ms')

        return df

    def movers(self, index, direction='up', change_type='percent'):
        self._refreshTokenIfExpired()
        return requests.get(MOVERS % index,
                            headers=self._headers(),
                            params={'direction': direction,
                                    'change_type': change_type}).json()
