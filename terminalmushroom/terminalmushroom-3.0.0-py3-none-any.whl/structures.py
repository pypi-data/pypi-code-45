import enum
from typing import List, Optional, Iterable


class Node(object):
    """A generic entry in a forest."""

    def __init__(self,
                 key: int,
                 identifier: str):
        self.key: int = key
        self.identifier: str = identifier


class Tree(Node):
    """A node containing references to other nodes."""

    def __init__(self,
                 key: int,
                 identifier: str,
                 branches: Optional[Iterable[int]] = None):
        super(Tree, self).__init__(key, identifier)

        self.branches: List[int] = list(branches or [])

    def __repr__(self) -> str:
        return '{self.__class__.__name__}({self.key}, {self.identifier!r}, ' \
               '{self.branches!r})'.format(
                self=self)


class Entity(Node):
    """A named entity with incidence count."""

    class CountType(enum.Enum):
        INCREMENT = 'increment'
        SET = 'set'

    def __init__(self,
                 key: int,
                 identifier: str,
                 alias: Optional[str] = None,
                 count_type: Optional[CountType] = None,
                 count: Optional[int] = None):
        super(Entity, self).__init__(key, identifier)
        self.alias: str = alias or ''
        self.count_type: Entity.CountType = count_type or Entity.CountType.INCREMENT
        self.count: int = count or 1

    def __repr__(self) -> str:
        return '{self.__class__.__name__}({self.key}, {self.identifier!r}, {self.alias!r}, ' \
               '{count_type}, {self.count!r})'.format(
                self=self, count_type='None' if self.count_type is None
                else 'Entity.CountType.' + self.count_type.name)


class Literal(Node):
    """A string literal."""

    def __init__(self, key: int, identifier: str):
        super(Literal, self).__init__(key, identifier)

    def __repr__(self) -> str:
        return '{self.__class__.__name__}({self.key}, {self.identifier!r})'.format(self=self)


class Metadata(Node):
    """A metadata tag."""

    def __init__(self, key: int, identifier: str):
        super(Metadata, self).__init__(key, identifier)

    def __repr__(self) -> str:
        return '{self.__class__.__name__}({self.key}, {self.identifier!r})'.format(self=self)
