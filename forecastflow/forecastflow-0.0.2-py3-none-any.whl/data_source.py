from typing import TYPE_CHECKING

from forecastflow.util import wait_until_profile_done

if TYPE_CHECKING:
    from forecastflow import Project, User


class DataSource:
    """
    ForecastFlow data source class
    """

    def __init__(self, project: 'Project', data_source_id: str):
        """
        Instantiate object with given data source ID

        Args:
            project:
                Project which data source belong to.

            data_source_id:
                ID of data source you want to open.
        """
        self.project = project
        self.data_source_id = data_source_id
        self.is_ready = False

    @property
    def did(self) -> str:
        return self.data_source_id

    @property
    def user(self) -> 'User':
        return self.project.user

    def wait_until_done(self):
        """
        Wait until ForecastFlow profile data source.
        """
        if not self.is_ready:
            wait_until_profile_done(self.user.id_token, self.user.uid,
                                    self.project.project_id, self.data_source_id)
            self.is_ready = True
