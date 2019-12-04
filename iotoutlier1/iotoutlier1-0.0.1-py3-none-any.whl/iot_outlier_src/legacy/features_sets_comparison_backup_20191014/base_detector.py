"""Base detector abstract class

"""
# Author: kun.bj@outlook.com
# license: xxx
from abc import ABC, abstractmethod


class BaseDetector(ABC):

    # @abstractmethod
    # def __init__(self):
    #     pass

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def test(self, X, y):
        pass
