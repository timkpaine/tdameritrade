import time

import requests_oauthlib


class FormExecutioner:
    tda_auth_url = 'https://auth.tdameritrade.com/auth'
    tda_refresh_token_url = 'https://api.tdameritrade.com/v1/oauth2/token'

    def __init__(
            self,
            config,
            web_driver
    ):
        self.tda_config = config
        self.web_driver = web_driver

    def complete_form_login(self):

        # Fill in credentials on login page
        input_username = self.web_driver.find_element_by_id("username")
        input_username.send_keys(self.tda_config.tda_username)

        input_password = self.web_driver.find_element_by_id("password")
        input_password.send_keys(self.tda_config.tda_password)

        button = self.web_driver.find_element_by_id("accept")
        button.click()

    def complete_selection_alternate_2fa(self):

        # Navigate to alternate 2FA option and select "security question" option
        button_alternates = self.web_driver.find_elements_by_class_name("alternates")[0]
        button_alternates.click()

        button_use_security_question = self.web_driver.find_elements_by_name("init_secretquestion")[0]
        button_use_security_question.click()

    def complete_form_security_question(self):

        # Navigate to security question page and enter security question
        # 1. Get security question from form
        text_security_question_p_tag = self.web_driver.find_elements_by_css_selector("div.row.description")[0].text
        text_security_question = text_security_question_p_tag.split("Question: ")[1]
        idx_security_question = 0

        # 2. Find index of question to grab the answer for that idx from tda_config
        for idx, question in enumerate(self.tda_config.tda_security_questions):
            if text_security_question.find(question) != -1:
                idx_security_question = idx

        security_question_answer = self.tda_config.tda_security_question_answers[idx_security_question]

        # 3. Fill in security question answer
        input_security_question = self.web_driver.find_element_by_id("secretquestion")
        input_security_question.send_keys(security_question_answer)

        # 4. Submit form
        button_submit_security_question_form = self.web_driver.find_element_by_id("accept")
        button_submit_security_question_form.click()

    def complete_form_authorize(self):

        # Hit allow on "TD Ameritrade Authorization" screen
        button_submit_allow = self.web_driver.find_element_by_id("accept")
        button_submit_allow.click()

    def get_token(self, wait_time_seconds=1.5):

        oauth = requests_oauthlib.OAuth2Session(
            self.tda_config.api_key,
            redirect_uri=self.tda_config.callback_uri)
        authorization_url, state = oauth.authorization_url(self.tda_auth_url)

        # Open the login page and wait for the redirect
        # It will redirect once the form has been completed
        self.web_driver.get(authorization_url)
        callback_url = ''

        while not callback_url.startswith(self.tda_config.callback_uri):
            # 1. Go through login form
            self.complete_form_login()

            time.sleep(wait_time_seconds)

            # 2. Hit alternate 2fa option to use security questions
            self.complete_selection_alternate_2fa()

            time.sleep(wait_time_seconds)

            # 3. Fill in security question
            self.complete_form_security_question()

            time.sleep(wait_time_seconds)

            # 4. Hit authorize and complete
            self.complete_form_authorize()

            callback_url = self.web_driver.current_url

            self.web_driver.close()

        return oauth.fetch_token(
            self.tda_refresh_token_url,
            authorization_response=callback_url,
            access_type='offline',
            client_id=self.tda_config.api_key,
            include_client_id=True)
