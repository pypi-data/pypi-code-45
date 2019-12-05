import logging
from typing import TYPE_CHECKING
from forecastflow.firebase_api import cloud_firestore

import forecastflow
from forecastflow.firebase_api import auth

if TYPE_CHECKING:
    from forecastflow import Project
    from typing import List

logger = logging.getLogger(__name__)


class User:
    """
    ForecastFlow user class
    """

    def __init__(self, email: str, password: str):
        """
        Instantiate object with e-mail and password.

        Args:
            email:
                e-mail to sign in.

            password:
                password for sign in.
        """
        res = auth.sign_in_with_password(email, password)
        self.id_token = res['idToken']
        self.user_id = res['localId']
        self._projects = {}

    @property
    def _document(self) -> dict:
        doc = cloud_firestore.get(f"users/{self.user_id}", self.id_token)
        return doc

    def get_project(self, project_id) -> 'Project':
        """
        Get project with given pid.

        Args:
            project_id:
                Project ID you want to open.

        Returns:
            ForecastFlow Project object with given pid.
        """
        if project_id not in self._projects:
            p = forecastflow.Project(self, project_id)
            self._projects[project_id] = p
        return self._projects[project_id]

    @property
    def uid(self) -> str:
        return self.user_id
