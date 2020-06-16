import json
from dataclasses import dataclass, asdict
from .json_encoder import EnhancedJSONEncoder
from .filtered_dict_factory import filtered_dict_factory


@dataclass
class BaseOrder:
    """Base Order dataclass

    https://docs.python.org/3/library/dataclasses.html

    https://stackoverflow.com/questions/12118695/efficient-way-to-remove-keys-with-empty-strings-from-a-dict
    """

    def json(self):
        order_dict = self._filter()
        return json.dumps(order_dict, cls=EnhancedJSONEncoder)

    def asdict(self):
        # Dataclasses.asdict doesn't convert sub dataclasses to dict
        clean_order_dict = json.loads(self.json())
        return clean_order_dict

    def _filter(self):
        filtered_dict = asdict(self, dict_factory=filtered_dict_factory)
        order_dict = {k: v for k, v in filtered_dict.items() if v is not None}
        return order_dict
