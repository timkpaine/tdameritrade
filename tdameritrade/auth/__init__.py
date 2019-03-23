import os
import os.path
import sys
import requests
import time
from selenium import webdriver
from shutil import which
import urllib.parse as up


def authentication(client_id, redirect_uri):
    client_id = client_id + '@AMER.OAUTHAP'
    url = 'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=' + up.quote(redirect_uri) + '&client_id=' + up.quote(client_id)

    options = webdriver.ChromeOptions()

    if sys.platform == 'darwin':
        # MacOS
        if os.path.exists("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
            options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        elif os.path.exists("/Applications/Chrome.app/Contents/MacOS/Google Chrome"):
            options.binary_location = "/Applications/Chrome.app/Contents/MacOS/Google Chrome"
    elif 'linux' in sys.platform:
        # Linux
        options.binary_location = which('google-chrome') or which('chrome') or which('chromium')

    else:
        # Windows
        if os.path.exists('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'):
            options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        elif os.path.exists('C:/Program Files/Google/Chrome/Application/chrome.exe'):
            options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

    chrome_driver_binary = which('chromedriver') or "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    driver.get(url)

    # Setting TDAUSER and TDAPASS environment variables enables
    # fully automated oauth2 authentication
    if 'TDAUSER' in os.environ and 'TDAPASS' in os.environ:
        ubox = driver.find_element_by_id('username')
        pbox = driver.find_element_by_id('password')
        ubox.send_keys(os.environ['TDAUSER'])
        pbox.send_keys(os.environ['TDAPASS'])
        driver.find_element_by_id('accept').click()

        driver.find_element_by_id('accept').click()
        while 1:
            try:
                code = up.unquote(driver.current_url.split('code=')[1])
                if code != '':
                    break
                else:
                    time.sleep(2)
            except (TypeError, IndexError):
                pass
    else:
        input('after giving access, hit enter to continue')
        code = up.unquote(driver.current_url.split('code=')[1])

    driver.close()

    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'authorization_code',
                               'refresh_token': '',
                               'access_type': 'offline',
                               'code': code,
                               'client_id': client_id,
                               'redirect_uri': redirect_uri})
    if resp.status_code != 200:
        raise Exception('Could not authenticate!')
    return resp.json()


def refresh_token(refresh_token, client_id):
    resp = requests.post('https://api.tdameritrade.com/v1/oauth2/token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         json={'grant_type': 'refresh_token',
                               'refresh_token': up.quote(refresh_token),
                               'client_id': up.quote(client_id)})
    if resp.status_code != 200:
        raise Exception('Could not authenticate!')
    return resp.json()


def main():
    client_id = input('client id:')
    redirect_uri = input('redirect uri:')
    print(authentication(client_id, redirect_uri))
