from dataclasses import dataclass
from datetime import datetime
from typing import Union

Id = Union[int]


@dataclass(frozen=True)
class Version:
    year: int  # AAAA
    release: int  # Non-negative integer
    fix: int  # Non-negative integer

    def __str__(self):
        return f"{self.year}.{self.release}.{self.fix}"

    def __eq__(self, other):
        return (self.year == other.year and
                self.release == other.release and
                self.fix == other.fix)

    def __gt__(self, other):
        if self.year > other.year:
            return True
        if self.year == other.year and self.release > other.release:
            return True
        if self.year == other.year and self.release == other.release and self.fix > other.fix:
            return True
        return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        if self.year == other.year and self.release < other.release:
            return True
        if self.year == other.year and self.release == other.release and self.fix < other.fix:
            return True
        return False

    @classmethod
    def new(cls) -> 'Version':
        return cls(datetime.now().year, 1, 0)

    @classmethod
    def from_str(cls, str_version: str):
        try:
            year, release, fix = map(int, str_version.split('.'))
            return cls(year, release, fix)
        except ValueError:
            raise ValueError('The version string is not in the correct format.', str_version)


@dataclass(frozen=True)
class Release:
    project: Id
    version: Version

    def __str__(self):
        return f"Release {self.version}"

    def __lt__(self, other):
        if not self.project == other.project:
            raise ValueError('Those release are not from the same project.')
        return self.version < other.version

    def __gt__(self, other):
        if not self.project == other.project:
            raise ValueError('Those release are not from the same project.')
        return self.version > other.version

    @property
    def ref(self):
        year, release, fix = self.version.year, self.version.release, 0
        return f"release-{year}.{release}.{fix}"

    def is_same_major(self, other) -> bool:
        if not self.project == other.project:
            raise ValueError('Those releases are not from the same project')
        return (self.version.year == other.version.year and
                self.version.release == other.version.release)
