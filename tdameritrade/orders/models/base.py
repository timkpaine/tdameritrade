import json
from dataclasses import asdict, dataclass

from .json_encoder import EnhancedJSONEncoder


class OrderValidationError(Exception):
    pass


@dataclass
class BaseOrder:
    """Base Order dataclass

    https://docs.python.org/3/library/dataclasses.html

    https://stackoverflow.com/questions/12118695/efficient-way-to-remove-keys-with-empty-strings-from-a-dict
    """

    def __post_init__(self):
        self.validate()

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
        filtered_dict = {
            key: value for key, value in list_of_tuples if value is not None
        }
        return dict(filtered_dict)

    def validate(self):
        error_list = self.check_for_errors()
        if len(error_list) > 0:
            raise OrderValidationError(error_list)

    def check_for_errors(self):
        """
        Using dataclasses' __annotations__ field to get labels and types for validation
        """
        validation_errors = []
        # https://github.com/python/cpython/blob/0d57db27f2c563b6433a220b646b50bdeff8a1f2/Lib/dataclasses.py#L856
        try:
            annotations = self.__annotations__
        except Exception:
            return validation_errors
        if annotations:
            for label, label_type in annotations.items():
                value = self.__dict__.get(label)
                try:
                    if value is not None and not isinstance(value, label_type):
                        message = f"{value} is not valid value for {label}"
                        validation_errors.append(message)
                except Exception as err:
                    print(value, label_type)
                    raise err

        return validation_errors
