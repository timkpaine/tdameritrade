import requests

from tdameritrade.auth.auth_form_executioner import FormExecutioner
from tdameritrade.auth.tda_config_provider import TDAConfigProvider, TDAConfig
from tdameritrade.auth.web_driver_provider import WebDriverProvider


def authentication(
        client_id=None,
        redirect_uri=None,
        tdauser=None,
        tdapass=None):
    # handles arguments or loading config from .env
    if client_id is None:
        tda_config = TDAConfigProvider.get_config()
    else:
        tda_config = TDAConfig(
            client_id,
            redirect_uri,
            tdauser,
            tdapass
        )

    return FormExecutioner(
        tda_config,
        WebDriverProvider.get_web_driver()).get_token()


def access_token(refresh_token, client_id):
    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'refresh_token',
                               'refresh_token': refresh_token,
                               'client_id': client_id})
    if resp.status_code != 200:

        # Attempt to refresh token via web flow
        token = authentication()
        if token == "" or token is None:
            raise Exception('Could not authenticate!')
        else:
            return token
    return resp.json()


def main():
    client_id = input('client id:')
    redirect_uri = input('redirect uri:')
    print(authentication(client_id, redirect_uri))
