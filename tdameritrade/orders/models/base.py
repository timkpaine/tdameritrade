import json
from dataclasses import dataclass, asdict
from .json_encoder import EnhancedJSONEncoder


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
        order_dict = asdict(self, dict_factory=self._filtered_dict_factory)
        return order_dict

    @staticmethod
    def _filtered_dict_factory(list_of_tuples):
        filtered_dict = {key: value for key, value in list_of_tuples if value is not None}
        return dict(filtered_dict)
