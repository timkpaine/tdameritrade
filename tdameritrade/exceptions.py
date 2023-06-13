import json


def handle_error_response(resp):
    codes = {
        429: TooManyRequestsError,
        400: ValidationError,
        401: InvalidAuthToken,
        500: ServerError,
        403: Forbidden,
        404: NotFound,
        -1: TDAAPIError,
    }

    try:
        body = resp.content.decode("utf-8")
        data = json.loads(body)
        message = data.get("error", body)
    except Exception:
        raise codes[resp.status_code](resp)
    raise codes[resp.status_code](
        message=message, code=resp.status_code, data=data, response=resp
    )


class TDAAPIError(Exception):
    response = None
    data = {}
    code = -1
    message = "An unknown error occurred"

    def __init__(self, message=None, code=None, data={}, response=None):
        self.response = response
        if message:
            self.message = message
        if code:
            self.code = code
        if data:
            self.data = data

    def __str__(self):
        if self.code:
            return "{}: {}".format(self.code, self.message)
        return self.data


class TooManyRequestsError(TDAAPIError):
    pass


class ValidationError(TDAAPIError):
    pass


class InvalidAuthToken(TDAAPIError):
    pass


class ServerError(TDAAPIError):
    pass


class Forbidden(TDAAPIError):
    pass


class NotFound(TDAAPIError):
    pass
