import dataclasses
import json


class EnhancedJSONEncoder(json.JSONEncoder):
    """
    Dataclasses make it hard to encode
    Nested dataclasses aren't JSON serializable by default.

    https://stackoverflow.com/questions/5160077/encoding-nested-python-object-in-json/5165421#5165421
    """

    def default(self, obj):
        if dataclasses.is_dataclass(obj) and hasattr(obj, "json"):
            return obj.json()
        return super().default(obj)
