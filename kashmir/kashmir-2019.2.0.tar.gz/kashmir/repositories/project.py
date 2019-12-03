from kashmir.core.data import Id, Release
from kashmir.core.entities import Project
from kashmir.core.protocols import PRepository
from kashmir.core.providers import SCMProvider


class ProjectRepository(PRepository):

    def __init__(self, scm: SCMProvider):
        self.scm = scm

    def get(self, id: Id) -> Project:
        return Project(
            id=self.scm.project.id,
            version=self.scm.version,
            releases=self.scm.releases
        )

    def new_release(self, release: Release) -> Release:
        return self.scm.new_release(release)

    def new_fix(self, release: Release) -> Release:
        return self.scm.new_fix(release)
