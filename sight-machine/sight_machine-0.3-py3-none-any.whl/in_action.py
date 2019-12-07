from datetime import datetime, timezone
import pickle

from sight_machine import BinaryLoggable, BinaryLoggerBis


class HelperBinaryLoggable(BinaryLoggable):
    def __init__(self):
        self.me = 'Test'
        self.idx = -1
        self.now = datetime.now(timezone.utc)

    def to_bytes(self) -> bytearray:
        return pickle.dumps(self)

    def from_bytes(self, byte_array: bytearray) -> None:
        instance = pickle.loads(byte_array)
        self.me = instance.me
        self.idx = instance.idx
        self.now = instance.now


class HelperBinaryLoggable1(HelperBinaryLoggable):
    def __init__(self):
        super().__init__()
        self.me = 'Test1'


class HelperBinaryLoggable2(HelperBinaryLoggable):
    def __init__(self):
        super().__init__()
        self.me = 'Test2'


filename = BinaryLoggerBis.file_for(HelperBinaryLoggable1, '/tmp/')
with BinaryLoggerBis(filename) as bl:
    for i in range(3):
        entry = HelperBinaryLoggable1()
        entry.idx = i
        bl.write(entry)

filename = BinaryLoggerBis.file_for(HelperBinaryLoggable2, '/tmp/')
with BinaryLoggerBis(filename) as bl:
    for i in range(3):
        entry = HelperBinaryLoggable2()
        entry.idx = i
        bl.write(entry)
    for entry in bl.read(HelperBinaryLoggable2):
        assert isinstance(entry, HelperBinaryLoggable2)
        print(entry.me, entry.idx, entry.now)

filename = BinaryLoggerBis.file_for(HelperBinaryLoggable1, '/tmp/')
with BinaryLoggerBis(filename) as bl:
    for entry in bl.read(HelperBinaryLoggable1):
        assert isinstance(entry, HelperBinaryLoggable1)
        print(entry.me, entry.idx, entry.now)
