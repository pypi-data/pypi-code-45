"Main interface for robomaker service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsTypeDef",
    "ClientBatchDescribeSimulationJobResponseTypeDef",
    "ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef",
    "ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef",
    "ClientCreateDeploymentJobDeploymentConfigTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientCreateDeploymentJobResponseTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationResponsesourcesTypeDef",
    "ClientCreateRobotApplicationResponseTypeDef",
    "ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationSourcesTypeDef",
    "ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationVersionResponsesourcesTypeDef",
    "ClientCreateRobotApplicationVersionResponseTypeDef",
    "ClientCreateRobotResponseTypeDef",
    "ClientCreateSimulationApplicationRenderingEngineTypeDef",
    "ClientCreateSimulationApplicationResponserenderingEngineTypeDef",
    "ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationResponsesourcesTypeDef",
    "ClientCreateSimulationApplicationResponseTypeDef",
    "ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationSourcesTypeDef",
    "ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef",
    "ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationVersionResponsesourcesTypeDef",
    "ClientCreateSimulationApplicationVersionResponseTypeDef",
    "ClientCreateSimulationJobDataSourcesTypeDef",
    "ClientCreateSimulationJobLoggingConfigTypeDef",
    "ClientCreateSimulationJobOutputLocationTypeDef",
    "ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef",
    "ClientCreateSimulationJobResponsedataSourcesTypeDef",
    "ClientCreateSimulationJobResponseloggingConfigTypeDef",
    "ClientCreateSimulationJobResponseoutputLocationTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationsTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationsTypeDef",
    "ClientCreateSimulationJobResponsevpcConfigTypeDef",
    "ClientCreateSimulationJobResponseTypeDef",
    "ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobRobotApplicationsTypeDef",
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobSimulationApplicationsTypeDef",
    "ClientCreateSimulationJobVpcConfigTypeDef",
    "ClientDeregisterRobotResponseTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef",
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef",
    "ClientDescribeDeploymentJobResponseTypeDef",
    "ClientDescribeFleetResponserobotsTypeDef",
    "ClientDescribeFleetResponseTypeDef",
    "ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientDescribeRobotApplicationResponsesourcesTypeDef",
    "ClientDescribeRobotApplicationResponseTypeDef",
    "ClientDescribeRobotResponseTypeDef",
    "ClientDescribeSimulationApplicationResponserenderingEngineTypeDef",
    "ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientDescribeSimulationApplicationResponsesourcesTypeDef",
    "ClientDescribeSimulationApplicationResponseTypeDef",
    "ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef",
    "ClientDescribeSimulationJobResponsedataSourcesTypeDef",
    "ClientDescribeSimulationJobResponseloggingConfigTypeDef",
    "ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef",
    "ClientDescribeSimulationJobResponseoutputLocationTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationsTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef",
    "ClientDescribeSimulationJobResponsevpcConfigTypeDef",
    "ClientDescribeSimulationJobResponseTypeDef",
    "ClientListDeploymentJobsFiltersTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsTypeDef",
    "ClientListDeploymentJobsResponseTypeDef",
    "ClientListFleetsFiltersTypeDef",
    "ClientListFleetsResponsefleetDetailsTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListRobotApplicationsFiltersTypeDef",
    "ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef",
    "ClientListRobotApplicationsResponseTypeDef",
    "ClientListRobotsFiltersTypeDef",
    "ClientListRobotsResponserobotsTypeDef",
    "ClientListRobotsResponseTypeDef",
    "ClientListSimulationApplicationsFiltersTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef",
    "ClientListSimulationApplicationsResponseTypeDef",
    "ClientListSimulationJobsFiltersTypeDef",
    "ClientListSimulationJobsResponsesimulationJobSummariesTypeDef",
    "ClientListSimulationJobsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRegisterRobotResponseTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientSyncDeploymentJobResponseTypeDef",
    "ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientUpdateRobotApplicationResponsesourcesTypeDef",
    "ClientUpdateRobotApplicationResponseTypeDef",
    "ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef",
    "ClientUpdateRobotApplicationSourcesTypeDef",
    "ClientUpdateSimulationApplicationRenderingEngineTypeDef",
    "ClientUpdateSimulationApplicationResponserenderingEngineTypeDef",
    "ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationResponsesourcesTypeDef",
    "ClientUpdateSimulationApplicationResponseTypeDef",
    "ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationSourcesTypeDef",
    "ListDeploymentJobsPaginateFiltersTypeDef",
    "ListDeploymentJobsPaginatePaginationConfigTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef",
    "ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef",
    "ListDeploymentJobsPaginateResponseTypeDef",
    "ListFleetsPaginateFiltersTypeDef",
    "ListFleetsPaginatePaginationConfigTypeDef",
    "ListFleetsPaginateResponsefleetDetailsTypeDef",
    "ListFleetsPaginateResponseTypeDef",
    "ListRobotApplicationsPaginateFiltersTypeDef",
    "ListRobotApplicationsPaginatePaginationConfigTypeDef",
    "ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef",
    "ListRobotApplicationsPaginateResponseTypeDef",
    "ListRobotsPaginateFiltersTypeDef",
    "ListRobotsPaginatePaginationConfigTypeDef",
    "ListRobotsPaginateResponserobotsTypeDef",
    "ListRobotsPaginateResponseTypeDef",
    "ListSimulationApplicationsPaginateFiltersTypeDef",
    "ListSimulationApplicationsPaginatePaginationConfigTypeDef",
    "ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    "ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef",
    "ListSimulationApplicationsPaginateResponseTypeDef",
    "ListSimulationJobsPaginateFiltersTypeDef",
    "ListSimulationJobsPaginatePaginationConfigTypeDef",
    "ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef",
    "ListSimulationJobsPaginateResponseTypeDef",
)


_ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef],
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef
):
    pass


_ClientBatchDescribeSimulationJobResponsejobsTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponsejobsTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef,
        "loggingConfig": ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[
            ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef,
        "networkInterface": ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef,
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponsejobsTypeDef(
    _ClientBatchDescribeSimulationJobResponsejobsTypeDef
):
    """
    - *(dict) --*

      Information about a simulation job.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the simulation job.
    """


_ClientBatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "_ClientBatchDescribeSimulationJobResponseTypeDef",
    {
        "jobs": List[ClientBatchDescribeSimulationJobResponsejobsTypeDef],
        "unprocessedJobs": List[str],
    },
    total=False,
)


class ClientBatchDescribeSimulationJobResponseTypeDef(
    _ClientBatchDescribeSimulationJobResponseTypeDef
):
    """
    - *(dict) --*

      - **jobs** *(list) --*

        A list of simulation jobs.
        - *(dict) --*

          Information about a simulation job.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the simulation job.
    """


_ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef
):
    pass


_RequiredClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef = TypedDict(
    "_RequiredClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef", {"application": str}
)
_OptionalClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef = TypedDict(
    "_OptionalClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef",
    {
        "applicationVersion": str,
        "launchConfig": ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef(
    _RequiredClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef,
    _OptionalClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef,
):
    """
    - *(dict) --*

      Information about a deployment application configuration.
      - **application** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the robot application.
    """


_ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef(
    _ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef
):
    pass


_ClientCreateDeploymentJobDeploymentConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentJobDeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobDeploymentConfigTypeDef(
    _ClientCreateDeploymentJobDeploymentConfigTypeDef
):
    """
    The requested deployment configuration.
    - **concurrentDeploymentPercentage** *(integer) --*

      The percentage of robots receiving the deployment at the same time.
    """


_ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef
):
    pass


_ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef
):
    pass


_ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef
):
    pass


_ClientCreateDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobResponsedeploymentConfigTypeDef(
    _ClientCreateDeploymentJobResponsedeploymentConfigTypeDef
):
    pass


_ClientCreateDeploymentJobResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[
            ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "deploymentConfig": ClientCreateDeploymentJobResponsedeploymentConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateDeploymentJobResponseTypeDef(_ClientCreateDeploymentJobResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the deployment job.
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef",
    {"arn": str, "name": str, "createdAt": datetime, "tags": Dict[str, str]},
    total=False,
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the fleet.
    """


_ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientCreateRobotApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientCreateRobotApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientCreateRobotApplicationResponsesourcesTypeDef(
    _ClientCreateRobotApplicationResponsesourcesTypeDef
):
    pass


_ClientCreateRobotApplicationResponseTypeDef = TypedDict(
    "_ClientCreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateRobotApplicationResponseTypeDef(_ClientCreateRobotApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot application.
    """


_ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef(
    _ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef
):
    """
    The robot software suite used by the robot application.
    - **name** *(string) --*

      The name of the robot software suite.
    """


_ClientCreateRobotApplicationSourcesTypeDef = TypedDict(
    "_ClientCreateRobotApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)


class ClientCreateRobotApplicationSourcesTypeDef(_ClientCreateRobotApplicationSourcesTypeDef):
    """
    - *(dict) --*

      Information about a source configuration.
      - **s3Bucket** *(string) --*

        The Amazon S3 bucket name.
    """


_ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef(
    _ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientCreateRobotApplicationVersionResponsesourcesTypeDef = TypedDict(
    "_ClientCreateRobotApplicationVersionResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientCreateRobotApplicationVersionResponsesourcesTypeDef(
    _ClientCreateRobotApplicationVersionResponsesourcesTypeDef
):
    pass


_ClientCreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateRobotApplicationVersionResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientCreateRobotApplicationVersionResponseTypeDef(
    _ClientCreateRobotApplicationVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot application.
    """


_ClientCreateRobotResponseTypeDef = TypedDict(
    "_ClientCreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateRobotResponseTypeDef(_ClientCreateRobotResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot.
    """


_ClientCreateSimulationApplicationRenderingEngineTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationRenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationRenderingEngineTypeDef(
    _ClientCreateSimulationApplicationRenderingEngineTypeDef
):
    """
    The rendering engine for the simulation application.
    - **name** *(string) --*

      The name of the rendering engine.
    """


_ClientCreateSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationResponserenderingEngineTypeDef(
    _ClientCreateSimulationApplicationResponserenderingEngineTypeDef
):
    pass


_ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef
):
    pass


_ClientCreateSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientCreateSimulationApplicationResponsesourcesTypeDef(
    _ClientCreateSimulationApplicationResponsesourcesTypeDef
):
    pass


_ClientCreateSimulationApplicationResponseTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientCreateSimulationApplicationResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateSimulationApplicationResponseTypeDef(
    _ClientCreateSimulationApplicationResponseTypeDef
):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the simulation application.
    """


_ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef
):
    """
    The robot software suite of the simulation application.
    - **name** *(string) --*

      The name of the robot software suite.
    """


_ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef
):
    """
    The simulation software suite used by the simulation application.
    - **name** *(string) --*

      The name of the simulation software suite.
    """


_ClientCreateSimulationApplicationSourcesTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)


class ClientCreateSimulationApplicationSourcesTypeDef(
    _ClientCreateSimulationApplicationSourcesTypeDef
):
    """
    - *(dict) --*

      Information about a source configuration.
      - **s3Bucket** *(string) --*

        The Amazon S3 bucket name.
    """


_ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef(
    _ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef
):
    pass


_ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef(
    _ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef
):
    pass


_ClientCreateSimulationApplicationVersionResponsesourcesTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientCreateSimulationApplicationVersionResponsesourcesTypeDef(
    _ClientCreateSimulationApplicationVersionResponsesourcesTypeDef
):
    pass


_ClientCreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateSimulationApplicationVersionResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientCreateSimulationApplicationVersionResponseTypeDef(
    _ClientCreateSimulationApplicationVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the simulation application.
    """


_ClientCreateSimulationJobDataSourcesTypeDef = TypedDict(
    "_ClientCreateSimulationJobDataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
    total=False,
)


class ClientCreateSimulationJobDataSourcesTypeDef(_ClientCreateSimulationJobDataSourcesTypeDef):
    pass


_ClientCreateSimulationJobLoggingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobLoggingConfigTypeDef", {"recordAllRosTopics": bool}
)


class ClientCreateSimulationJobLoggingConfigTypeDef(_ClientCreateSimulationJobLoggingConfigTypeDef):
    """
    The logging configuration.
    - **recordAllRosTopics** *(boolean) --***[REQUIRED]**

      A boolean indicating whether to record all ROS topics.
    """


_ClientCreateSimulationJobOutputLocationTypeDef = TypedDict(
    "_ClientCreateSimulationJobOutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientCreateSimulationJobOutputLocationTypeDef(
    _ClientCreateSimulationJobOutputLocationTypeDef
):
    """
    Location for output files generated by the simulation job.
    - **s3Bucket** *(string) --*

      The S3 bucket for output.
    """


_ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)


class ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef(
    _ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef
):
    pass


_ClientCreateSimulationJobResponsedataSourcesTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsedataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef],
    },
    total=False,
)


class ClientCreateSimulationJobResponsedataSourcesTypeDef(
    _ClientCreateSimulationJobResponsedataSourcesTypeDef
):
    pass


_ClientCreateSimulationJobResponseloggingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponseloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)


class ClientCreateSimulationJobResponseloggingConfigTypeDef(
    _ClientCreateSimulationJobResponseloggingConfigTypeDef
):
    pass


_ClientCreateSimulationJobResponseoutputLocationTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponseoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientCreateSimulationJobResponseoutputLocationTypeDef(
    _ClientCreateSimulationJobResponseoutputLocationTypeDef
):
    pass


_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef
):
    pass


_ClientCreateSimulationJobResponserobotApplicationsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponserobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponserobotApplicationsTypeDef(
    _ClientCreateSimulationJobResponserobotApplicationsTypeDef
):
    pass


_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef
):
    pass


_ClientCreateSimulationJobResponsesimulationApplicationsTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsesimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponsesimulationApplicationsTypeDef(
    _ClientCreateSimulationJobResponsesimulationApplicationsTypeDef
):
    pass


_ClientCreateSimulationJobResponsevpcConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponsevpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobResponsevpcConfigTypeDef(
    _ClientCreateSimulationJobResponsevpcConfigTypeDef
):
    pass


_ClientCreateSimulationJobResponseTypeDef = TypedDict(
    "_ClientCreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "clientRequestToken": str,
        "outputLocation": ClientCreateSimulationJobResponseoutputLocationTypeDef,
        "loggingConfig": ClientCreateSimulationJobResponseloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[ClientCreateSimulationJobResponserobotApplicationsTypeDef],
        "simulationApplications": List[
            ClientCreateSimulationJobResponsesimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientCreateSimulationJobResponsedataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientCreateSimulationJobResponsevpcConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobResponseTypeDef(_ClientCreateSimulationJobResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the simulation job.
    """


_ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef(
    _ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef
):
    pass


_RequiredClientCreateSimulationJobRobotApplicationsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobRobotApplicationsTypeDef", {"application": str}
)
_OptionalClientCreateSimulationJobRobotApplicationsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobRobotApplicationsTypeDef",
    {
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobRobotApplicationsTypeDef(
    _RequiredClientCreateSimulationJobRobotApplicationsTypeDef,
    _OptionalClientCreateSimulationJobRobotApplicationsTypeDef,
):
    """
    - *(dict) --*

      Application configuration information for a robot.
      - **application** *(string) --***[REQUIRED]**

        The application information for the robot application.
    """


_ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef(
    _ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef
):
    pass


_RequiredClientCreateSimulationJobSimulationApplicationsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobSimulationApplicationsTypeDef", {"application": str}
)
_OptionalClientCreateSimulationJobSimulationApplicationsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobSimulationApplicationsTypeDef",
    {
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobSimulationApplicationsTypeDef(
    _RequiredClientCreateSimulationJobSimulationApplicationsTypeDef,
    _OptionalClientCreateSimulationJobSimulationApplicationsTypeDef,
):
    """
    - *(dict) --*

      Information about a simulation application configuration.
      - **application** *(string) --***[REQUIRED]**

        The application information for the simulation application.
    """


_RequiredClientCreateSimulationJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobVpcConfigTypeDef", {"subnets": List[str]}
)
_OptionalClientCreateSimulationJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobVpcConfigTypeDef",
    {"securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobVpcConfigTypeDef(
    _RequiredClientCreateSimulationJobVpcConfigTypeDef,
    _OptionalClientCreateSimulationJobVpcConfigTypeDef,
):
    """
    If your simulation job accesses resources in a VPC, you provide this parameter identifying the
    list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide
    at least one security group and one subnet ID.
    - **subnets** *(list) --***[REQUIRED]**

      A list of one or more subnet IDs in your VPC.
      - *(string) --*
    """


_ClientDeregisterRobotResponseTypeDef = TypedDict(
    "_ClientDeregisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)


class ClientDeregisterRobotResponseTypeDef(_ClientDeregisterRobotResponseTypeDef):
    """
    - *(dict) --*

      - **fleet** *(string) --*

        The Amazon Resource Name (ARN) of the fleet.
    """


_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef
):
    pass


_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef
):
    pass


_ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef
):
    pass


_ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef(
    _ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef
):
    pass


_ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef",
    {
        "currentProgress": Literal[
            "Validating",
            "DownloadingExtracting",
            "ExecutingDownloadCondition",
            "ExecutingPreLaunch",
            "Launching",
            "ExecutingPostLaunch",
            "Finished",
        ],
        "percentDone": Any,
        "estimatedTimeRemainingSeconds": int,
        "targetResource": str,
    },
    total=False,
)


class ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef(
    _ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef
):
    pass


_ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef",
    {
        "arn": str,
        "deploymentStartTime": datetime,
        "deploymentFinishTime": datetime,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "progressDetail": ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
    },
    total=False,
)


class ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef(
    _ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef
):
    pass


_ClientDescribeDeploymentJobResponseTypeDef = TypedDict(
    "_ClientDescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[
            ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "robotDeploymentSummary": List[
            ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef
        ],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDeploymentJobResponseTypeDef(_ClientDescribeDeploymentJobResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the deployment job.
    """


_ClientDescribeFleetResponserobotsTypeDef = TypedDict(
    "_ClientDescribeFleetResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ClientDescribeFleetResponserobotsTypeDef(_ClientDescribeFleetResponserobotsTypeDef):
    pass


_ClientDescribeFleetResponseTypeDef = TypedDict(
    "_ClientDescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List[ClientDescribeFleetResponserobotsTypeDef],
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeFleetResponseTypeDef(_ClientDescribeFleetResponseTypeDef):
    """
    - *(dict) --*

      - **name** *(string) --*

        The name of the fleet.
    """


_ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientDescribeRobotApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientDescribeRobotApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientDescribeRobotApplicationResponsesourcesTypeDef(
    _ClientDescribeRobotApplicationResponsesourcesTypeDef
):
    pass


_ClientDescribeRobotApplicationResponseTypeDef = TypedDict(
    "_ClientDescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientDescribeRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeRobotApplicationResponseTypeDef(_ClientDescribeRobotApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot application.
    """


_ClientDescribeRobotResponseTypeDef = TypedDict(
    "_ClientDescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeRobotResponseTypeDef(_ClientDescribeRobotResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot.
    """


_ClientDescribeSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientDescribeSimulationApplicationResponserenderingEngineTypeDef(
    _ClientDescribeSimulationApplicationResponserenderingEngineTypeDef
):
    pass


_ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef(
    _ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef
):
    pass


_ClientDescribeSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientDescribeSimulationApplicationResponsesourcesTypeDef(
    _ClientDescribeSimulationApplicationResponsesourcesTypeDef
):
    pass


_ClientDescribeSimulationApplicationResponseTypeDef = TypedDict(
    "_ClientDescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientDescribeSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientDescribeSimulationApplicationResponserenderingEngineTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeSimulationApplicationResponseTypeDef(
    _ClientDescribeSimulationApplicationResponseTypeDef
):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot simulation application.
    """


_ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)


class ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef(
    _ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef
):
    pass


_ClientDescribeSimulationJobResponsedataSourcesTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsedataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef],
    },
    total=False,
)


class ClientDescribeSimulationJobResponsedataSourcesTypeDef(
    _ClientDescribeSimulationJobResponsedataSourcesTypeDef
):
    pass


_ClientDescribeSimulationJobResponseloggingConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponseloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)


class ClientDescribeSimulationJobResponseloggingConfigTypeDef(
    _ClientDescribeSimulationJobResponseloggingConfigTypeDef
):
    pass


_ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)


class ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef(
    _ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef
):
    pass


_ClientDescribeSimulationJobResponseoutputLocationTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponseoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)


class ClientDescribeSimulationJobResponseoutputLocationTypeDef(
    _ClientDescribeSimulationJobResponseoutputLocationTypeDef
):
    pass


_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef
):
    pass


_ClientDescribeSimulationJobResponserobotApplicationsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponserobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponserobotApplicationsTypeDef(
    _ClientDescribeSimulationJobResponserobotApplicationsTypeDef
):
    pass


_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
):
    pass


_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef
):
    pass


_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef
):
    pass


_ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef(
    _ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef
):
    pass


_ClientDescribeSimulationJobResponsevpcConfigTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponsevpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)


class ClientDescribeSimulationJobResponsevpcConfigTypeDef(
    _ClientDescribeSimulationJobResponsevpcConfigTypeDef
):
    pass


_ClientDescribeSimulationJobResponseTypeDef = TypedDict(
    "_ClientDescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": ClientDescribeSimulationJobResponseoutputLocationTypeDef,
        "loggingConfig": ClientDescribeSimulationJobResponseloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[ClientDescribeSimulationJobResponserobotApplicationsTypeDef],
        "simulationApplications": List[
            ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientDescribeSimulationJobResponsedataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientDescribeSimulationJobResponsevpcConfigTypeDef,
        "networkInterface": ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef,
    },
    total=False,
)


class ClientDescribeSimulationJobResponseTypeDef(_ClientDescribeSimulationJobResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the simulation job.
    """


_ClientListDeploymentJobsFiltersTypeDef = TypedDict(
    "_ClientListDeploymentJobsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ClientListDeploymentJobsFiltersTypeDef(_ClientListDeploymentJobsFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef
):
    pass


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
):
    pass


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef
):
    pass


_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef
):
    pass


_ClientListDeploymentJobsResponsedeploymentJobsTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponsedeploymentJobsTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[
            ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
        ],
        "deploymentConfig": ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)


class ClientListDeploymentJobsResponsedeploymentJobsTypeDef(
    _ClientListDeploymentJobsResponsedeploymentJobsTypeDef
):
    """
    - *(dict) --*

      Information about a deployment job.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the deployment job.
    """


_ClientListDeploymentJobsResponseTypeDef = TypedDict(
    "_ClientListDeploymentJobsResponseTypeDef",
    {
        "deploymentJobs": List[ClientListDeploymentJobsResponsedeploymentJobsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDeploymentJobsResponseTypeDef(_ClientListDeploymentJobsResponseTypeDef):
    """
    - *(dict) --*

      - **deploymentJobs** *(list) --*

        A list of deployment jobs that meet the criteria of the request.
        - *(dict) --*

          Information about a deployment job.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the deployment job.
    """


_ClientListFleetsFiltersTypeDef = TypedDict(
    "_ClientListFleetsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ClientListFleetsFiltersTypeDef(_ClientListFleetsFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ClientListFleetsResponsefleetDetailsTypeDef = TypedDict(
    "_ClientListFleetsResponsefleetDetailsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ClientListFleetsResponsefleetDetailsTypeDef(_ClientListFleetsResponsefleetDetailsTypeDef):
    """
    - *(dict) --*

      Information about a fleet.
      - **name** *(string) --*

        The name of the fleet.
    """


_ClientListFleetsResponseTypeDef = TypedDict(
    "_ClientListFleetsResponseTypeDef",
    {"fleetDetails": List[ClientListFleetsResponsefleetDetailsTypeDef], "nextToken": str},
    total=False,
)


class ClientListFleetsResponseTypeDef(_ClientListFleetsResponseTypeDef):
    """
    - *(dict) --*

      - **fleetDetails** *(list) --*

        A list of fleet details meeting the request criteria.
        - *(dict) --*

          Information about a fleet.
          - **name** *(string) --*

            The name of the fleet.
    """


_ClientListRobotApplicationsFiltersTypeDef = TypedDict(
    "_ClientListRobotApplicationsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ClientListRobotApplicationsFiltersTypeDef(_ClientListRobotApplicationsFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef
):
    pass


_ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef = TypedDict(
    "_ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef,
    },
    total=False,
)


class ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef(
    _ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information for a robot application.
      - **name** *(string) --*

        The name of the robot application.
    """


_ClientListRobotApplicationsResponseTypeDef = TypedDict(
    "_ClientListRobotApplicationsResponseTypeDef",
    {
        "robotApplicationSummaries": List[
            ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListRobotApplicationsResponseTypeDef(_ClientListRobotApplicationsResponseTypeDef):
    """
    - *(dict) --*

      - **robotApplicationSummaries** *(list) --*

        A list of robot application summaries that meet the criteria of the request.
        - *(dict) --*

          Summary information for a robot application.
          - **name** *(string) --*

            The name of the robot application.
    """


_ClientListRobotsFiltersTypeDef = TypedDict(
    "_ClientListRobotsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ClientListRobotsFiltersTypeDef(_ClientListRobotsFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ClientListRobotsResponserobotsTypeDef = TypedDict(
    "_ClientListRobotsResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ClientListRobotsResponserobotsTypeDef(_ClientListRobotsResponserobotsTypeDef):
    """
    - *(dict) --*

      Information about a robot.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot.
    """


_ClientListRobotsResponseTypeDef = TypedDict(
    "_ClientListRobotsResponseTypeDef",
    {"robots": List[ClientListRobotsResponserobotsTypeDef], "nextToken": str},
    total=False,
)


class ClientListRobotsResponseTypeDef(_ClientListRobotsResponseTypeDef):
    """
    - *(dict) --*

      - **robots** *(list) --*

        A list of robots that meet the criteria of the request.
        - *(dict) --*

          Information about a robot.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the robot.
    """


_ClientListSimulationApplicationsFiltersTypeDef = TypedDict(
    "_ClientListSimulationApplicationsFiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ClientListSimulationApplicationsFiltersTypeDef(
    _ClientListSimulationApplicationsFiltersTypeDef
):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef
):
    pass


_ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef(
    _ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef
):
    pass


_ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef,
        "simulationSoftwareSuite": ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef,
    },
    total=False,
)


class ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef(
    _ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information for a simulation application.
      - **name** *(string) --*

        The name of the simulation application.
    """


_ClientListSimulationApplicationsResponseTypeDef = TypedDict(
    "_ClientListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List[
            ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSimulationApplicationsResponseTypeDef(
    _ClientListSimulationApplicationsResponseTypeDef
):
    """
    - *(dict) --*

      - **simulationApplicationSummaries** *(list) --*

        A list of simulation application summaries that meet the criteria of the request.
        - *(dict) --*

          Summary information for a simulation application.
          - **name** *(string) --*

            The name of the simulation application.
    """


_ClientListSimulationJobsFiltersTypeDef = TypedDict(
    "_ClientListSimulationJobsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ClientListSimulationJobsFiltersTypeDef(_ClientListSimulationJobsFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ClientListSimulationJobsResponsesimulationJobSummariesTypeDef = TypedDict(
    "_ClientListSimulationJobsResponsesimulationJobSummariesTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)


class ClientListSimulationJobsResponsesimulationJobSummariesTypeDef(
    _ClientListSimulationJobsResponsesimulationJobSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information for a simulation job.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the simulation job.
    """


_ClientListSimulationJobsResponseTypeDef = TypedDict(
    "_ClientListSimulationJobsResponseTypeDef",
    {
        "simulationJobSummaries": List[
            ClientListSimulationJobsResponsesimulationJobSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSimulationJobsResponseTypeDef(_ClientListSimulationJobsResponseTypeDef):
    """
    - *(dict) --*

      - **simulationJobSummaries** *(list) --*

        A list of simulation job summaries that meet the criteria of the request.
        - *(dict) --*

          Summary information for a simulation job.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the simulation job.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        The list of all tags added to the specified resource.
        - *(string) --*

          - *(string) --*
    """


_ClientRegisterRobotResponseTypeDef = TypedDict(
    "_ClientRegisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)


class ClientRegisterRobotResponseTypeDef(_ClientRegisterRobotResponseTypeDef):
    """
    - *(dict) --*

      - **fleet** *(string) --*

        The Amazon Resource Name (ARN) of the fleet that the robot will join.
    """


_ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef
):
    pass


_ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef
):
    pass


_ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef
):
    pass


_ClientSyncDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ClientSyncDeploymentJobResponsedeploymentConfigTypeDef(
    _ClientSyncDeploymentJobResponsedeploymentConfigTypeDef
):
    pass


_ClientSyncDeploymentJobResponseTypeDef = TypedDict(
    "_ClientSyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": ClientSyncDeploymentJobResponsedeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[
            ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)


class ClientSyncDeploymentJobResponseTypeDef(_ClientSyncDeploymentJobResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the synchronization request.
    """


_ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientUpdateRobotApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientUpdateRobotApplicationResponsesourcesTypeDef(
    _ClientUpdateRobotApplicationResponsesourcesTypeDef
):
    pass


_ClientUpdateRobotApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientUpdateRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientUpdateRobotApplicationResponseTypeDef(_ClientUpdateRobotApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the updated robot application.
    """


_ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef(
    _ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef
):
    """
    The robot software suite used by the robot application.
    - **name** *(string) --*

      The name of the robot software suite.
    """


_ClientUpdateRobotApplicationSourcesTypeDef = TypedDict(
    "_ClientUpdateRobotApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)


class ClientUpdateRobotApplicationSourcesTypeDef(_ClientUpdateRobotApplicationSourcesTypeDef):
    """
    - *(dict) --*

      Information about a source configuration.
      - **s3Bucket** *(string) --*

        The Amazon S3 bucket name.
    """


_ClientUpdateSimulationApplicationRenderingEngineTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationRenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationRenderingEngineTypeDef(
    _ClientUpdateSimulationApplicationRenderingEngineTypeDef
):
    """
    The rendering engine for the simulation application.
    - **name** *(string) --*

      The name of the rendering engine.
    """


_ClientUpdateSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationResponserenderingEngineTypeDef(
    _ClientUpdateSimulationApplicationResponserenderingEngineTypeDef
):
    pass


_ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef
):
    pass


_ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef
):
    pass


_ClientUpdateSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)


class ClientUpdateSimulationApplicationResponsesourcesTypeDef(
    _ClientUpdateSimulationApplicationResponsesourcesTypeDef
):
    pass


_ClientUpdateSimulationApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientUpdateSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientUpdateSimulationApplicationResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)


class ClientUpdateSimulationApplicationResponseTypeDef(
    _ClientUpdateSimulationApplicationResponseTypeDef
):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the updated simulation application.
    """


_ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef
):
    """
    Information about the robot software suite.
    - **name** *(string) --*

      The name of the robot software suite.
    """


_ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef(
    _ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef
):
    """
    The simulation software suite used by the simulation application.
    - **name** *(string) --*

      The name of the simulation software suite.
    """


_ClientUpdateSimulationApplicationSourcesTypeDef = TypedDict(
    "_ClientUpdateSimulationApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)


class ClientUpdateSimulationApplicationSourcesTypeDef(
    _ClientUpdateSimulationApplicationSourcesTypeDef
):
    """
    - *(dict) --*

      Information about a source configuration.
      - **s3Bucket** *(string) --*

        The Amazon S3 bucket name.
    """


_ListDeploymentJobsPaginateFiltersTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ListDeploymentJobsPaginateFiltersTypeDef(_ListDeploymentJobsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ListDeploymentJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeploymentJobsPaginatePaginationConfigTypeDef(
    _ListDeploymentJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef
):
    pass


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
):
    pass


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef
):
    pass


_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef
):
    pass


_ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[
            ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
        ],
        "deploymentConfig": ListDeploymentJobsPaginateResponsedeploymentJobsdeploymentConfigTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef(
    _ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef
):
    """
    - *(dict) --*

      Information about a deployment job.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the deployment job.
    """


_ListDeploymentJobsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentJobsPaginateResponseTypeDef",
    {
        "deploymentJobs": List[ListDeploymentJobsPaginateResponsedeploymentJobsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDeploymentJobsPaginateResponseTypeDef(_ListDeploymentJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **deploymentJobs** *(list) --*

        A list of deployment jobs that meet the criteria of the request.
        - *(dict) --*

          Information about a deployment job.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the deployment job.
    """


_ListFleetsPaginateFiltersTypeDef = TypedDict(
    "_ListFleetsPaginateFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ListFleetsPaginateFiltersTypeDef(_ListFleetsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ListFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFleetsPaginatePaginationConfigTypeDef(_ListFleetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFleetsPaginateResponsefleetDetailsTypeDef = TypedDict(
    "_ListFleetsPaginateResponsefleetDetailsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ListFleetsPaginateResponsefleetDetailsTypeDef(_ListFleetsPaginateResponsefleetDetailsTypeDef):
    """
    - *(dict) --*

      Information about a fleet.
      - **name** *(string) --*

        The name of the fleet.
    """


_ListFleetsPaginateResponseTypeDef = TypedDict(
    "_ListFleetsPaginateResponseTypeDef",
    {"fleetDetails": List[ListFleetsPaginateResponsefleetDetailsTypeDef], "NextToken": str},
    total=False,
)


class ListFleetsPaginateResponseTypeDef(_ListFleetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **fleetDetails** *(list) --*

        A list of fleet details meeting the request criteria.
        - *(dict) --*

          Information about a fleet.
          - **name** *(string) --*

            The name of the fleet.
    """


_ListRobotApplicationsPaginateFiltersTypeDef = TypedDict(
    "_ListRobotApplicationsPaginateFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ListRobotApplicationsPaginateFiltersTypeDef(_ListRobotApplicationsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ListRobotApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRobotApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRobotApplicationsPaginatePaginationConfigTypeDef(
    _ListRobotApplicationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef
):
    pass


_ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef = TypedDict(
    "_ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ListRobotApplicationsPaginateResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef,
    },
    total=False,
)


class ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef(
    _ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information for a robot application.
      - **name** *(string) --*

        The name of the robot application.
    """


_ListRobotApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListRobotApplicationsPaginateResponseTypeDef",
    {
        "robotApplicationSummaries": List[
            ListRobotApplicationsPaginateResponserobotApplicationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListRobotApplicationsPaginateResponseTypeDef(_ListRobotApplicationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **robotApplicationSummaries** *(list) --*

        A list of robot application summaries that meet the criteria of the request.
        - *(dict) --*

          Summary information for a robot application.
          - **name** *(string) --*

            The name of the robot application.
    """


_ListRobotsPaginateFiltersTypeDef = TypedDict(
    "_ListRobotsPaginateFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ListRobotsPaginateFiltersTypeDef(_ListRobotsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ListRobotsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRobotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRobotsPaginatePaginationConfigTypeDef(_ListRobotsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRobotsPaginateResponserobotsTypeDef = TypedDict(
    "_ListRobotsPaginateResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)


class ListRobotsPaginateResponserobotsTypeDef(_ListRobotsPaginateResponserobotsTypeDef):
    """
    - *(dict) --*

      Information about a robot.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the robot.
    """


_ListRobotsPaginateResponseTypeDef = TypedDict(
    "_ListRobotsPaginateResponseTypeDef",
    {"robots": List[ListRobotsPaginateResponserobotsTypeDef], "NextToken": str},
    total=False,
)


class ListRobotsPaginateResponseTypeDef(_ListRobotsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **robots** *(list) --*

        A list of robots that meet the criteria of the request.
        - *(dict) --*

          Information about a robot.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the robot.
    """


_ListSimulationApplicationsPaginateFiltersTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateFiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)


class ListSimulationApplicationsPaginateFiltersTypeDef(
    _ListSimulationApplicationsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ListSimulationApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSimulationApplicationsPaginatePaginationConfigTypeDef(
    _ListSimulationApplicationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)


class ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef(
    _ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef
):
    pass


_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)


class ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef(
    _ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef
):
    pass


_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef,
        "simulationSoftwareSuite": ListSimulationApplicationsPaginateResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef,
    },
    total=False,
)


class ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef(
    _ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information for a simulation application.
      - **name** *(string) --*

        The name of the simulation application.
    """


_ListSimulationApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListSimulationApplicationsPaginateResponseTypeDef",
    {
        "simulationApplicationSummaries": List[
            ListSimulationApplicationsPaginateResponsesimulationApplicationSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSimulationApplicationsPaginateResponseTypeDef(
    _ListSimulationApplicationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **simulationApplicationSummaries** *(list) --*

        A list of simulation application summaries that meet the criteria of the request.
        - *(dict) --*

          Summary information for a simulation application.
          - **name** *(string) --*

            The name of the simulation application.
    """


_ListSimulationJobsPaginateFiltersTypeDef = TypedDict(
    "_ListSimulationJobsPaginateFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)


class ListSimulationJobsPaginateFiltersTypeDef(_ListSimulationJobsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The name of the filter.
    """


_ListSimulationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSimulationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSimulationJobsPaginatePaginationConfigTypeDef(
    _ListSimulationJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef = TypedDict(
    "_ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)


class ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef(
    _ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information for a simulation job.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the simulation job.
    """


_ListSimulationJobsPaginateResponseTypeDef = TypedDict(
    "_ListSimulationJobsPaginateResponseTypeDef",
    {
        "simulationJobSummaries": List[
            ListSimulationJobsPaginateResponsesimulationJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSimulationJobsPaginateResponseTypeDef(_ListSimulationJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **simulationJobSummaries** *(list) --*

        A list of simulation job summaries that meet the criteria of the request.
        - *(dict) --*

          Summary information for a simulation job.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the simulation job.
    """
