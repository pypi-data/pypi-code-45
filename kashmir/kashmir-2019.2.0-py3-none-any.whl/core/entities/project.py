from dataclasses import dataclass
from datetime import datetime
from typing import List

from kashmir.core.data import Version, Release, Id
from kashmir.core.protocols import Entity


class Project(Entity):

    def __init__(self, id: Id, version: Version, releases: List[Release]):
        self.id = id
        self.version = version
        self.releases = releases

    def new_release(self) -> Release:
        current_year = datetime.now().year
        if self.version and self.version.year == current_year:
            year, release, fix = self.version.year, self.version.release + 1, 0
        else:
            year, release, fix = current_year, 1, 0
        new_version = Version(year, release, fix)
        return Release(self.id, new_version)

    def new_fix(self, release: Release) -> Release:
        last_fix = self.get_last_fix_for_release(release)
        new_version = Version(last_fix.version.year,
                              last_fix.version.release,
                              last_fix.version.fix + 1)
        return Release(last_fix.project, new_version)

    def get_last_fix_for_release(self, release: Release) -> Release:
        try:
            return sorted(filter(lambda r, release=release: release.is_same_major(r), self.releases))[-1]
        except IndexError:
            raise ValueError('This project does not have this release.', release)

    def __str__(self):
        return f"Project<{self.id}> {self.version}"
