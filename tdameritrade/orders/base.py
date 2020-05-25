import json
from dataclasses import dataclass


@dataclass
class BaseOrder:
    """Base Order dataclass

    https://docs.python.org/3/library/dataclasses.html
    """
    def json(self):
        return json.dumps(self.__dict__)
