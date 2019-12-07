import os
import tempfile
from typing import Iterable, List, Type, Optional

from sight_machine import BinaryLoggable


class InvalidClass(Exception):
    pass


class BinaryLoggerBis:
    PIPE = b'|'

    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            with open(file_path, 'wb+') as f:
                f.write(b'')
        self.file_handle = open(file_path, 'rb+')
        self.class_name = None

    def __del__(self):
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def write(self, binary_log: BinaryLoggable) -> None:
        # check that the class of the instance provided is valid for the log
        encoded_class_name = binary_log.__class__.__name__.encode()
        if self.class_name:
            if self.class_name != encoded_class_name:
                raise InvalidClass('the provided instance is not valid for the file')
        else:
            self.file_handle.seek(0)
            read = self.file_handle.read(len(encoded_class_name))
            if read and encoded_class_name != read:
                raise InvalidClass('the provided instance is not valid for the file')
            if not isinstance(binary_log, BinaryLoggable):
                raise InvalidClass('the provided instance is not valid for the file')
            # if the file is empty, add the name of the class at the beginning
            if self.file_handle.tell() == 0:
                self.file_handle.write(encoded_class_name)
            # move to the end
            self.file_handle.seek(0, os.SEEK_END)
            # memoize the class name
            self.class_name = encoded_class_name

        # add the entry
        entry = binary_log.to_bytes()
        self.file_handle.write(str(len(entry)).encode() + self.PIPE + entry)

    def _next_entry(self) -> Optional[bytes]:
        buffer: List = []
        char = self.file_handle.read(1)
        while char and char != self.PIPE:
            buffer.append(char)
            char = self.file_handle.read(1)
        if buffer:
            size = int(b''.join(buffer).decode())
            return self.file_handle.read(size)

    def read(self, binary_loggable_clazz: Type[BinaryLoggable]) -> Iterable[BinaryLoggable]:
        # check that the class of the instance provided is valid for the log
        encoded_class_name = binary_loggable_clazz.__name__.encode()
        self.file_handle.seek(0)
        file_class_name = self.file_handle.read(len(encoded_class_name))
        if file_class_name and encoded_class_name != file_class_name:
            raise InvalidClass('the provided instance is not valid for the file')
        # the cursor is after the name of the class
        while True:
            entry = self._next_entry()
            if entry:
                instance = binary_loggable_clazz()
                instance.from_bytes(bytearray(entry))
                yield instance
            else:
                break

    @staticmethod
    def file_for(binary_loggable_clazz: Type[BinaryLoggable], directory: str) -> str:
        """
        Retrieve the log file for the specified BinaryLoggable class.
        If the file doesn't exist, a random name is returned
        """
        if not (os.path.exists(directory) and os.path.isdir(directory)):
            raise FileNotFoundError(f'The directory {directory} is incorrect')

        class_name = binary_loggable_clazz.__name__
        class_len = len(class_name)
        for name in os.listdir(directory):
            file_path = os.path.join(directory, name)
            if os.path.isfile(file_path):
                with open(file_path, 'rb+') as fh:
                    if fh.read(class_len) == class_name.encode():
                        return file_path
        return tempfile.NamedTemporaryFile(delete=False, dir=directory, suffix='.sm').name
