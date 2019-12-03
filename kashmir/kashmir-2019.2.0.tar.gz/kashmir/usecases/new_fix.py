from dataclasses import dataclass

from kashmir.core.data import Id, Release
from kashmir.core.protocols import PRepository


@dataclass
class NewFix:
    repository: PRepository

    def __call__(self, project_id: Id, release: Release):
        project = self.repository.get(project_id)
        new_release = project.new_fix(release)
        self.repository.new_fix(new_release)
        return new_release
