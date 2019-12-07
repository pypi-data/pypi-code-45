import json
import uuid
import binascii
import datetime
import decimal
import bizerror
from functools import partial

default_simple_json_encoder_base = json.encoder.JSONEncoder

class JsonEncodeLibrary(object):

    def __init__(self, bases=tuple([default_simple_json_encoder_base])):
        self.bases = bases
        self.encoders = {}
        self.__encoder = None

    def get_encoder(self):
        if self.__encoder is not None:
            return self.__encoder
        def __default(encoder, o):
            for t, encoder in self.encoders.items():
                if isinstance(o, t):
                    return encoder(o)
            return super().default(o)
        self.__encoder = type("SimpleJsonEncoder", self.bases, {"default": __default})
        return self.__encoder

    def register(self, type, encode):
        self.encoders[type] = encode

    def unregister(self, type):
        if type in self.encoders:
            del self.encoders[type]

def encode_datetime(value):
    return value.isoformat()

def encode_bytes(value):
    return binascii.hexlify(value).decode()

def encode_decimal(value):
    return float(value)

def encode_complex(value):
    return [value.real, value.imag]

def encode_uuid(value):
    return str(value)

def encode_exception(error):
    return bizerror.BizError(str(error)).json

def encode_bizerror(error):
    return error.json

GLOBAL_ENCODERS = {}

def register_global_encoder(type, encoder):
    GLOBAL_ENCODERS[type] = encoder

def register_simple_encoders(library):
    for type, encoder in GLOBAL_ENCODERS.items():
        library.register(type, encoder)

register_global_encoder((datetime.datetime, datetime.date, datetime.time), encode_datetime)
register_global_encoder(bytes, encode_bytes)
register_global_encoder(decimal.Decimal, encode_decimal)
register_global_encoder(complex, encode_complex)
register_global_encoder(uuid.UUID, encode_uuid)
register_global_encoder(bizerror.BizError, encode_bizerror)
register_global_encoder(Exception, encode_exception)

def make_simple_json_encoder(bases=tuple([default_simple_json_encoder_base])):
    library = JsonEncodeLibrary()
    encoder = library.get_encoder()
    setattr(encoder, "library", library)
    register_simple_encoders(library)
    return encoder

SimpleJsonEncoder = make_simple_json_encoder()
simple_json_dumps = partial(json.dumps, cls=SimpleJsonEncoder)

