from abc import abstractmethod
from typing_extensions import Protocol

from kashmir.core.protocols import Entity
from kashmir.core.data import Id


class PRepository(Protocol):

    @abstractmethod
    def get(self, id: Id) -> Entity:
        raise NotImplementedError
