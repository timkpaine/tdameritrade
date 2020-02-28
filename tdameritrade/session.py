import requests


class TDASession(requests.Session):

    def set_token(self, token):
        self.headers.update({'Authorization': 'Bearer ' + token})
