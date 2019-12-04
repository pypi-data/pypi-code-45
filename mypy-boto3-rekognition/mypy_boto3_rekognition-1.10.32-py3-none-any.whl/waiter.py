"Main interface for rekognition service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_rekognition.type_defs import (
    ProjectVersionRunningWaitWaiterConfigTypeDef,
    ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef,
)


__all__ = ("ProjectVersionRunningWaiter", "ProjectVersionTrainingCompletedWaiter")


class ProjectVersionRunningWaiter(Boto3Waiter):
    """
    Waiter for `project_version_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: ProjectVersionRunningWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`Rekognition.Client.describe_project_versions` every 30 seconds until a
        successful state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeProjectVersions>`_

        **Request Syntax**
        ::

          waiter.wait(
              ProjectArn='string',
              VersionNames=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ProjectArn: string
        :param ProjectArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the project that contains the models you want to
          describe.

        :type VersionNames: list
        :param VersionNames:

          A list of model version names that you want to describe. You can add up to 10 model
          version names to the list. If you don't specify a value, all model descriptions are
          returned.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more results to retrieve),
          Amazon Rekognition Custom Labels returns a pagination token in the response. You can use
          this pagination token to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return per paginated call. The largest value you can
          specify is 100. If you specify a value greater than 100, a ValidationException error
          occurs. The default value is 100.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class ProjectVersionTrainingCompletedWaiter(Boto3Waiter):
    """
    Waiter for `project_version_training_completed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`Rekognition.Client.describe_project_versions` every 120 seconds until a
        successful state is reached. An error is returned after 360 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeProjectVersions>`_

        **Request Syntax**
        ::

          waiter.wait(
              ProjectArn='string',
              VersionNames=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ProjectArn: string
        :param ProjectArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the project that contains the models you want to
          describe.

        :type VersionNames: list
        :param VersionNames:

          A list of model version names that you want to describe. You can add up to 10 model
          version names to the list. If you don't specify a value, all model descriptions are
          returned.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more results to retrieve),
          Amazon Rekognition Custom Labels returns a pagination token in the response. You can use
          this pagination token to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return per paginated call. The largest value you can
          specify is 100. If you specify a value greater than 100, a ValidationException error
          occurs. The default value is 100.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 120

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 360

        :returns: None
        """
