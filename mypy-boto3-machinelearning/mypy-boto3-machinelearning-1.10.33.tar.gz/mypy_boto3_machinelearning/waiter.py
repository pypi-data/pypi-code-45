"Main interface for machinelearning service Waiters"
from __future__ import annotations

import sys
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_machinelearning.type_defs import (
    BatchPredictionAvailableWaitWaiterConfigTypeDef,
    DataSourceAvailableWaitWaiterConfigTypeDef,
    EvaluationAvailableWaitWaiterConfigTypeDef,
    MlModelAvailableWaitWaiterConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchPredictionAvailableWaiter",
    "DataSourceAvailableWaiter",
    "EvaluationAvailableWaiter",
    "MLModelAvailableWaiter",
)


class BatchPredictionAvailableWaiter(Boto3Waiter):
    """
    Waiter for `batch_prediction_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "MLModelId",
            "DataSourceId",
            "DataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: BatchPredictionAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [batch_prediction_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/machinelearning.html#MachineLearning.Waiter.batch_prediction_available.wait)
        """


class DataSourceAvailableWaiter(Boto3Waiter):
    """
    Waiter for `data_source_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        FilterVariable: Literal[
            "CreatedAt", "LastUpdatedAt", "Status", "Name", "DataLocationS3", "IAMUser"
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: DataSourceAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [data_source_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/machinelearning.html#MachineLearning.Waiter.data_source_available.wait)
        """


class EvaluationAvailableWaiter(Boto3Waiter):
    """
    Waiter for `evaluation_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "MLModelId",
            "DataSourceId",
            "DataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: EvaluationAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [evaluation_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/machinelearning.html#MachineLearning.Waiter.evaluation_available.wait)
        """


class MLModelAvailableWaiter(Boto3Waiter):
    """
    Waiter for `ml_model_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "TrainingDataSourceId",
            "RealtimeEndpointStatus",
            "MLModelType",
            "Algorithm",
            "TrainingDataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: MlModelAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [ml_model_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/machinelearning.html#MachineLearning.Waiter.ml_model_available.wait)
        """
