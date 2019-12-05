import pytest

import json
import uuid
from datetime import date
from datetime import datetime
from datetime import timezone
from json_extended import dumps, loads

@pytest.fixture
def obj():
    #: test objcet to be json serialized
    obj = {
        'abc': 'hello world',
        'cdg': 9102,
        123: datetime.now(),
        'hello': [date(year=2020, month=2, day=22), 'eunchae', 'ks', {'nested': True}],
        True: datetime.now(),
        False: datetime.now(tz=timezone.utc),
        'uuid': uuid.uuid4(),
    }
    return obj

def recursive_convert(o):
    """pre-process a python ``dict`` or ``list`` by recursively
    converting ``datetime``, ``date`` and ``uuid`` elements in it. 
    This enables the default simplejson module to serialize the
    aforementioned objects in the same format as :mod:`json_extended`
    does.
    """
    if isinstance(o, dict):
        new_o = {}
        for k, v in o.items():
            if isinstance(v, (dict, list, datetime, date, uuid.UUID)):
                new_v = recursive_convert(v)
            else:
                new_v = v
            new_o[k] = new_v

        return new_o

    if isinstance(o, list):
        new_o = []
        for v in o:
            if isinstance(v, (dict, list, datetime, date, uuid.UUID)):
                new_v = recursive_convert(v)
            else:
                new_v = v
            new_o.append(new_v)

        return new_o
        
    if isinstance(o, datetime):
        if o.tzinfo is None:
            o = o.astimezone(timezone.utc)
        return o.isoformat()

    if isinstance(o, date):
        return o.isoformat()

    if isinstance(o, uuid.UUID):
        return str(o)

def test_dumps(obj):
    """test :func:`json_extended.dumps`"""
    new_obj = recursive_convert(obj)
    df = json.dumps(new_obj)

    assert df == dumps(obj)

def test_loads(obj):
    """test :func:`json_extended.loads`"""
    new_obj = recursive_convert(obj)
    df = json.dumps(new_obj)
    assert loads(df) == json.loads(df)
