import os
from dotenv import load_dotenv

load_dotenv()


class TDAConfig:

    def __init__(
            self,
            api_key,
            callback_uri,
            tda_username,
            tda_password,
            tda_security_questions,
            tda_security_question_answers
    ):
        self.api_key = api_key
        self.callback_uri = callback_uri
        self.tda_username = tda_username
        self.tda_password = tda_password
        self.tda_security_questions = tda_security_questions
        self.tda_security_question_answers = tda_security_question_answers


class TDAConfigProvider:

    @staticmethod
    def get_config():
        tda_security_questions = [
            os.getenv('TDA_SECURITY_QUESTION_1'),
            os.getenv('TDA_SECURITY_QUESTION_2'),
            os.getenv('TDA_SECURITY_QUESTION_3'),
            os.getenv('TDA_SECURITY_QUESTION_4')
        ]

        tda_security_question_answers = [
            os.getenv('TDA_SECURITY_QUESTION_ANSWER_1'),
            os.getenv('TDA_SECURITY_QUESTION_ANSWER_2'),
            os.getenv('TDA_SECURITY_QUESTION_ANSWER_3'),
            os.getenv('TDA_SECURITY_QUESTION_ANSWER_4')
        ]

        return TDAConfig(
            api_key=os.getenv('TDA_API_KEY'),
            callback_uri=os.getenv('TDA_CALLBACK_URI'),
            tda_username=os.getenv('TDA_USERNAME'),
            tda_password=os.getenv('TDA_PASSWORD'),
            tda_security_questions=tda_security_questions,
            tda_security_question_answers=tda_security_question_answers
        )
