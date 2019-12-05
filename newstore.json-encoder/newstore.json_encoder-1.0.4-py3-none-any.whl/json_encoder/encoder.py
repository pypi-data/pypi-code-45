import json
import logging

from uuid import UUID
from decimal import Decimal
from datetime import datetime, timedelta


logger = logging.getLogger(__name__)


class JSONEncoder(json.JSONEncoder):
    """ A JSONEncoder that knows how to serialize Decimal, datetime, timedelta, and UUID types.
    It will also serialize any object that has `to_dict` method. """

    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, timedelta):
            return int(obj.total_seconds())
        elif isinstance(obj, UUID):
            return str(obj)
        elif hasattr(obj, "to_dict"):
            # provide `to_dict` on the object and it will be serialized
            return obj.to_dict()
        return super().default(obj)


def serialize(val: dict, **kwargs) -> str:
    return json.dumps(val, cls=JSONEncoder, **kwargs)


def deserialize(val: str, **kwargs) -> dict:
    return json.loads(val, parse_float=Decimal, **kwargs)
