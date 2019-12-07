import os
import unittest
from datetime import datetime, timezone
from time import monotonic
from unittest.mock import MagicMock, call

from sight_machine import BinaryLoggerBis, BinaryLoggable, InvalidClass


class TestBinaryLoggerBis(unittest.TestCase):
    log_file = '/tmp/test_binary_logger.log'

    def setUp(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test___init__(self):
        # the log file does NOT exist --> it is created
        self.assertFalse(os.path.exists(self.log_file))
        tested = BinaryLoggerBis(self.log_file)
        del tested
        self.assertTrue(os.path.exists(self.log_file))
        expected = 0
        result = os.path.getsize(self.log_file)
        self.assertEqual(expected, result)

        # the log file does exist --> it is unchanged
        with open(self.log_file, 'w') as f:
            for i in range(5):
                f.write(f'line #{i}')
        tested = BinaryLoggerBis(self.log_file)
        del tested
        self.assertTrue(os.path.exists(self.log_file))
        expected = 35
        result = os.path.getsize(self.log_file)
        self.assertEqual(expected, result)

    def test___del__(self):
        mock = MagicMock()
        tested = BinaryLoggerBis(self.log_file)
        tested.file_handle.close()
        # the file handle is correctly closed on instance destruction
        tested.file_handle = mock
        del tested
        expected = [
            call.__bool__(),
            call.close(),
        ]
        self.assertEqual(expected, mock.mock_calls)

    def test_write(self):
        # adding an entry that is NOT BinaryLoggable generates an error
        tested = BinaryLoggerBis(self.log_file)
        instance = datetime(2019, 11, 28, 12, 34, 55)
        self.assertRaises(InvalidClass, tested.write, instance)
        del tested

        #  adding the first entry adds the class name too
        tested = BinaryLoggerBis(self.log_file)
        instance = HelperBinaryLoggable1()
        instance.now = datetime(2019, 11, 28, 12, 34, 56)
        tested.write(instance)
        del tested
        with open(self.log_file, 'r') as f:
            result = f.readlines()
            expected = [
                ('HelperBinaryLoggable1'
                 '28|Test1+-1+2019-11-28T12:34:56'),
            ]
            self.assertEqual(expected, result)

        # adding an entry from a new class generates an error
        tested = BinaryLoggerBis(self.log_file)
        instance = HelperBinaryLoggable2()
        instance.now = datetime(2019, 11, 28, 12, 34, 55)
        self.assertRaises(InvalidClass, tested.write, instance)
        del tested
        with open(self.log_file, 'r') as f:
            result = f.readlines()
            expected = [
                ('HelperBinaryLoggable1'
                 '28|Test1+-1+2019-11-28T12:34:56'),
            ]
            self.assertEqual(expected, result)

        # adding an entry from the expected class is correctly written
        tested = BinaryLoggerBis(self.log_file)
        instance = HelperBinaryLoggable1()
        instance.now = datetime(2019, 11, 28, 12, 34, 54)
        tested.write(instance)
        del tested
        with open(self.log_file, 'r') as f:
            result = f.readlines()
            expected = [
                ('HelperBinaryLoggable1'
                 '28|Test1+-1+2019-11-28T12:34:56'
                 '28|Test1+-1+2019-11-28T12:34:54'),
            ]
            self.assertEqual(expected, result)

    def test_read(self):
        tested = BinaryLoggerBis(self.log_file)

        # there is NO entry of the class
        result = len([e for e in tested.read(HelperBinaryLoggable1)])
        expected = 0
        self.assertEqual(expected, result)

        # there are some entries of the class
        with open(self.log_file, 'w') as f:
            f.write('HelperBinaryLoggable1'
                    '28|Test1+-1+2019-11-28T12:34:56'
                    '28|Test1+-1+2019-11-28T12:34:54')
        count = 0
        for idx, entry in enumerate(tested.read(HelperBinaryLoggable1)):
            count += 1
            self.assertIsInstance(entry, HelperBinaryLoggable1)
            if idx == 0:
                self.assertEqual(datetime(2019, 11, 28, 12, 34, 56), entry.now)
            if idx == 1:
                self.assertEqual(datetime(2019, 11, 28, 12, 34, 54), entry.now)
        self.assertEqual(2, count)

        # the class is invalid --> exception
        self.assertRaises(InvalidClass, next, tested.read(HelperBinaryLoggable2))

    def test_performance(self):
        # check that the logger is less than 15 times slower than just keeping writing
        items = 10000
        start_time = monotonic()
        with open(self.log_file, 'wb') as f:
            for i in range(items):
                f.write(HelperBinaryLoggable1().to_bytes())
        base_time = monotonic() - start_time
        self.setUp()
        with BinaryLoggerBis(self.log_file) as tested:

            start_time = monotonic()
            for i in range(items):
                instance = HelperBinaryLoggable1()
                instance.idx = i
                tested.write(instance)
            end_time = monotonic()
            self.assertGreater(base_time * 1.5, end_time - start_time)

            count = 0
            for entry in tested.read(HelperBinaryLoggable1):
                self.assertIsInstance(entry, HelperBinaryLoggable1)
                self.assertEqual(count, entry.idx)
                count += 1
            self.assertEqual(items, count)


class HelperBinaryLoggable(BinaryLoggable):
    def __init__(self):
        self.me = 'Test'
        self.idx = -1
        self.now = datetime.now(timezone.utc)

    def to_bytes(self) -> bytearray:
        return bytearray(self.me + '+' + str(self.idx) + '+' + self.now.isoformat(), 'utf-8')

    def from_bytes(self, byte_array: bytearray) -> None:
        splits = byte_array.decode().split('+')
        self.me = splits[0]
        self.idx = int(splits[1])
        self.now = datetime.fromisoformat(splits[2])


class HelperBinaryLoggable1(HelperBinaryLoggable):
    def __init__(self):
        super().__init__()
        self.me = 'Test1'


class HelperBinaryLoggable2(HelperBinaryLoggable):
    def __init__(self):
        super().__init__()
        self.me = 'Test2'


if __name__ == '__main__':
    unittest.main()
