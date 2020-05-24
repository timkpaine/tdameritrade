import json


class OrderEncoder(json.JSONEncoder):
    def default(self, o):
        return o.kwargs


class BaseOrder:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def json(self):
        return json.dumps(self.kwargs, cls=OrderEncoder)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {str(self)}>"

    def __str__(self):
        return str(self.kwargs)
