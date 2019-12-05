from io import BytesIO
from typing import TYPE_CHECKING

import pandas as pd

from forecastflow.firebase_api import storage
from forecastflow.util import wait_until_prediction_done

if TYPE_CHECKING:
    from forecastflow import Model, Project, User


class Prediction:
    """
    ForecastFlow prediction object
    """

    def __init__(self, model: 'Model', prediction_id: str):
        """
        Instantiate object with given prediction ID.

        Args:
            model:
                Model which makes this predict.

            prediction_id:
                ID of prediction you want to open.
        """
        self.model = model
        self.prediction_id = prediction_id
        self.is_ready = False

    def get_result(self) -> pd.DataFrame:
        """
        Download the result from ForecastFlow.

        Returns:
            result with primary key and predicted values.
        """
        self.wait_until_done()
        f = BytesIO()
        storage.download(f"{self.user.user_id}/predict/{self.prediction_id}/predict_proba.csv",
                         f, self.user.id_token)
        f.seek(0)
        result = pd.read_csv(f)
        return result

    @property
    def project(self) -> 'Project':
        return self.model.project

    @property
    def rid(self) -> str:
        return self.prediction_id

    @property
    def user(self) -> 'User':
        return self.model.project.user

    def wait_until_done(self):
        """
        Wait until ForecastFlow finish predict.
        """
        if not self.is_ready:
            wait_until_prediction_done(self.user.id_token, self.user.user_id,
                                       self.project.project_id, self.prediction_id)
            self.is_ready = True
