import json
from dataclasses import dataclass


@dataclass
class BaseOrder:
    def json(self):
        return json.dumps(self.__dict__)
