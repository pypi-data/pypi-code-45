"Main interface for batch service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef",
    "ClientCreateComputeEnvironmentComputeResourcesTypeDef",
    "ClientCreateComputeEnvironmentResponseTypeDef",
    "ClientCreateJobQueueComputeEnvironmentOrderTypeDef",
    "ClientCreateJobQueueResponseTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef",
    "ClientDescribeComputeEnvironmentsResponseTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef",
    "ClientDescribeJobDefinitionsResponseTypeDef",
    "ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef",
    "ClientDescribeJobQueuesResponsejobQueuesTypeDef",
    "ClientDescribeJobQueuesResponseTypeDef",
    "ClientDescribeJobsResponsejobsarrayPropertiesTypeDef",
    "ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef",
    "ClientDescribeJobsResponsejobsattemptscontainerTypeDef",
    "ClientDescribeJobsResponsejobsattemptsTypeDef",
    "ClientDescribeJobsResponsejobscontainerenvironmentTypeDef",
    "ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef",
    "ClientDescribeJobsResponsejobscontainermountPointsTypeDef",
    "ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef",
    "ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef",
    "ClientDescribeJobsResponsejobscontainerulimitsTypeDef",
    "ClientDescribeJobsResponsejobscontainervolumeshostTypeDef",
    "ClientDescribeJobsResponsejobscontainervolumesTypeDef",
    "ClientDescribeJobsResponsejobscontainerTypeDef",
    "ClientDescribeJobsResponsejobsdependsOnTypeDef",
    "ClientDescribeJobsResponsejobsnodeDetailsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesTypeDef",
    "ClientDescribeJobsResponsejobsretryStrategyTypeDef",
    "ClientDescribeJobsResponsejobstimeoutTypeDef",
    "ClientDescribeJobsResponsejobsTypeDef",
    "ClientDescribeJobsResponseTypeDef",
    "ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef",
    "ClientListJobsResponsejobSummaryListcontainerTypeDef",
    "ClientListJobsResponsejobSummaryListnodePropertiesTypeDef",
    "ClientListJobsResponsejobSummaryListTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef",
    "ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef",
    "ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesTypeDef",
    "ClientRegisterJobDefinitionResponseTypeDef",
    "ClientRegisterJobDefinitionRetryStrategyTypeDef",
    "ClientRegisterJobDefinitionTimeoutTypeDef",
    "ClientSubmitJobArrayPropertiesTypeDef",
    "ClientSubmitJobContainerOverridesenvironmentTypeDef",
    "ClientSubmitJobContainerOverridesresourceRequirementsTypeDef",
    "ClientSubmitJobContainerOverridesTypeDef",
    "ClientSubmitJobDependsOnTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef",
    "ClientSubmitJobNodeOverridesTypeDef",
    "ClientSubmitJobResponseTypeDef",
    "ClientSubmitJobRetryStrategyTypeDef",
    "ClientSubmitJobTimeoutTypeDef",
    "ClientUpdateComputeEnvironmentComputeResourcesTypeDef",
    "ClientUpdateComputeEnvironmentResponseTypeDef",
    "ClientUpdateJobQueueComputeEnvironmentOrderTypeDef",
    "ClientUpdateJobQueueResponseTypeDef",
    "DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef",
    "DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    "DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef",
    "DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef",
    "DescribeComputeEnvironmentsPaginateResponseTypeDef",
    "DescribeJobDefinitionsPaginatePaginationConfigTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef",
    "DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef",
    "DescribeJobDefinitionsPaginateResponseTypeDef",
    "DescribeJobQueuesPaginatePaginationConfigTypeDef",
    "DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef",
    "DescribeJobQueuesPaginateResponsejobQueuesTypeDef",
    "DescribeJobQueuesPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef",
    "ListJobsPaginateResponsejobSummaryListcontainerTypeDef",
    "ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef",
    "ListJobsPaginateResponsejobSummaryListTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef = TypedDict(
    "_ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)


class ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef(
    _ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef
):
    pass


_RequiredClientCreateComputeEnvironmentComputeResourcesTypeDef = TypedDict(
    "_RequiredClientCreateComputeEnvironmentComputeResourcesTypeDef",
    {"type": Literal["EC2", "SPOT"]},
)
_OptionalClientCreateComputeEnvironmentComputeResourcesTypeDef = TypedDict(
    "_OptionalClientCreateComputeEnvironmentComputeResourcesTypeDef",
    {
        "allocationStrategy": Literal[
            "BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"
        ],
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)


class ClientCreateComputeEnvironmentComputeResourcesTypeDef(
    _RequiredClientCreateComputeEnvironmentComputeResourcesTypeDef,
    _OptionalClientCreateComputeEnvironmentComputeResourcesTypeDef,
):
    """
    Details of the compute resources managed by the compute environment. This parameter is required
    for managed compute environments. For more information, see `Compute Environments
    <https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`__ in the *AWS
    Batch User Guide* .
    - **type** *(string) --***[REQUIRED]**

      The type of compute environment: ``EC2`` or ``SPOT`` .
    """


_ClientCreateComputeEnvironmentResponseTypeDef = TypedDict(
    "_ClientCreateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)


class ClientCreateComputeEnvironmentResponseTypeDef(_ClientCreateComputeEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      - **computeEnvironmentName** *(string) --*

        The name of the compute environment.
    """


_RequiredClientCreateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_RequiredClientCreateJobQueueComputeEnvironmentOrderTypeDef", {"order": int}
)
_OptionalClientCreateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_OptionalClientCreateJobQueueComputeEnvironmentOrderTypeDef",
    {"computeEnvironment": str},
    total=False,
)


class ClientCreateJobQueueComputeEnvironmentOrderTypeDef(
    _RequiredClientCreateJobQueueComputeEnvironmentOrderTypeDef,
    _OptionalClientCreateJobQueueComputeEnvironmentOrderTypeDef,
):
    """
    - *(dict) --*

      The order in which compute environments are tried for job placement within a queue. Compute
      environments are tried in ascending order. For example, if two compute environments are
      associated with a job queue, the compute environment with a lower order integer value is tried
      for job placement first.
      - **order** *(integer) --***[REQUIRED]**

        The order of the compute environment.
    """


_ClientCreateJobQueueResponseTypeDef = TypedDict(
    "_ClientCreateJobQueueResponseTypeDef", {"jobQueueName": str, "jobQueueArn": str}, total=False
)


class ClientCreateJobQueueResponseTypeDef(_ClientCreateJobQueueResponseTypeDef):
    """
    - *(dict) --*

      - **jobQueueName** *(string) --*

        The name of the job queue.
    """


_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)


class ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef(
    _ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef
):
    pass


_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef",
    {
        "type": Literal["EC2", "SPOT"],
        "allocationStrategy": Literal[
            "BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"
        ],
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)


class ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef(
    _ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef
):
    pass


_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ecsClusterArn": str,
        "type": Literal["MANAGED", "UNMANAGED"],
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "computeResources": ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef,
        "serviceRole": str,
    },
    total=False,
)


class ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef(
    _ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef
):
    """
    - *(dict) --*

      An object representing an AWS Batch compute environment.
      - **computeEnvironmentName** *(string) --*

        The name of the compute environment.
    """


_ClientDescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientDescribeComputeEnvironmentsResponseTypeDef",
    {
        "computeEnvironments": List[
            ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeComputeEnvironmentsResponseTypeDef(
    _ClientDescribeComputeEnvironmentsResponseTypeDef
):
    """
    - *(dict) --*

      - **computeEnvironments** *(list) --*

        The list of compute environments.
        - *(dict) --*

          An object representing an AWS Batch compute environment.
          - **computeEnvironmentName** *(string) --*

            The name of the compute environment.
    """


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    {
        "host": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef",
    {"attempts": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef",
    {"attemptDurationSeconds": int},
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef
):
    pass


_ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "status": str,
        "type": str,
        "parameters": Dict[str, str],
        "retryStrategy": ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef,
        "containerProperties": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef,
        "timeout": ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef,
        "nodeProperties": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef(
    _ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef
):
    """
    - *(dict) --*

      An object representing an AWS Batch job definition.
      - **jobDefinitionName** *(string) --*

        The name of the job definition.
    """


_ClientDescribeJobDefinitionsResponseTypeDef = TypedDict(
    "_ClientDescribeJobDefinitionsResponseTypeDef",
    {
        "jobDefinitions": List[ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeJobDefinitionsResponseTypeDef(_ClientDescribeJobDefinitionsResponseTypeDef):
    """
    - *(dict) --*

      - **jobDefinitions** *(list) --*

        The list of job definitions.
        - *(dict) --*

          An object representing an AWS Batch job definition.
          - **jobDefinitionName** *(string) --*

            The name of the job definition.
    """


_ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef = TypedDict(
    "_ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef",
    {"order": int, "computeEnvironment": str},
    total=False,
)


class ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef(
    _ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef
):
    pass


_ClientDescribeJobQueuesResponsejobQueuesTypeDef = TypedDict(
    "_ClientDescribeJobQueuesResponsejobQueuesTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "priority": int,
        "computeEnvironmentOrder": List[
            ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobQueuesResponsejobQueuesTypeDef(
    _ClientDescribeJobQueuesResponsejobQueuesTypeDef
):
    """
    - *(dict) --*

      An object representing the details of an AWS Batch job queue.
      - **jobQueueName** *(string) --*

        The name of the job queue.
    """


_ClientDescribeJobQueuesResponseTypeDef = TypedDict(
    "_ClientDescribeJobQueuesResponseTypeDef",
    {"jobQueues": List[ClientDescribeJobQueuesResponsejobQueuesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeJobQueuesResponseTypeDef(_ClientDescribeJobQueuesResponseTypeDef):
    """
    - *(dict) --*

      - **jobQueues** *(list) --*

        The list of job queues.
        - *(dict) --*

          An object representing the details of an AWS Batch job queue.
          - **jobQueueName** *(string) --*

            The name of the job queue.
    """


_ClientDescribeJobsResponsejobsarrayPropertiesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsarrayPropertiesTypeDef",
    {"statusSummary": Dict[str, int], "size": int, "index": int},
    total=False,
)


class ClientDescribeJobsResponsejobsarrayPropertiesTypeDef(
    _ClientDescribeJobsResponsejobsarrayPropertiesTypeDef
):
    pass


_ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef",
    {"attachmentId": str, "ipv6Address": str, "privateIpv4Address": str},
    total=False,
)


class ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef(
    _ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef
):
    pass


_ClientDescribeJobsResponsejobsattemptscontainerTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsattemptscontainerTypeDef",
    {
        "containerInstanceArn": str,
        "taskArn": str,
        "exitCode": int,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List[
            ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobsResponsejobsattemptscontainerTypeDef(
    _ClientDescribeJobsResponsejobsattemptscontainerTypeDef
):
    pass


_ClientDescribeJobsResponsejobsattemptsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsattemptsTypeDef",
    {
        "container": ClientDescribeJobsResponsejobsattemptscontainerTypeDef,
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsattemptsTypeDef(_ClientDescribeJobsResponsejobsattemptsTypeDef):
    pass


_ClientDescribeJobsResponsejobscontainerenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerenvironmentTypeDef(
    _ClientDescribeJobsResponsejobscontainerenvironmentTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef(
    _ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef",
    {"devices": List[ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef]},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef(
    _ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainermountPointsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainermountPointsTypeDef(
    _ClientDescribeJobsResponsejobscontainermountPointsTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef",
    {"attachmentId": str, "ipv6Address": str, "privateIpv4Address": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef(
    _ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef(
    _ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainerulimitsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobsResponsejobscontainerulimitsTypeDef(
    _ClientDescribeJobsResponsejobscontainerulimitsTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainervolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainervolumeshostTypeDef", {"sourcePath": str}, total=False
)


class ClientDescribeJobsResponsejobscontainervolumeshostTypeDef(
    _ClientDescribeJobsResponsejobscontainervolumeshostTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainervolumesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainervolumesTypeDef",
    {"host": ClientDescribeJobsResponsejobscontainervolumeshostTypeDef, "name": str},
    total=False,
)


class ClientDescribeJobsResponsejobscontainervolumesTypeDef(
    _ClientDescribeJobsResponsejobscontainervolumesTypeDef
):
    pass


_ClientDescribeJobsResponsejobscontainerTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobscontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[ClientDescribeJobsResponsejobscontainervolumesTypeDef],
        "environment": List[ClientDescribeJobsResponsejobscontainerenvironmentTypeDef],
        "mountPoints": List[ClientDescribeJobsResponsejobscontainermountPointsTypeDef],
        "readonlyRootFilesystem": bool,
        "ulimits": List[ClientDescribeJobsResponsejobscontainerulimitsTypeDef],
        "privileged": bool,
        "user": str,
        "exitCode": int,
        "reason": str,
        "containerInstanceArn": str,
        "taskArn": str,
        "logStreamName": str,
        "instanceType": str,
        "networkInterfaces": List[ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef],
        "resourceRequirements": List[
            ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobscontainerTypeDef(
    _ClientDescribeJobsResponsejobscontainerTypeDef
):
    pass


_ClientDescribeJobsResponsejobsdependsOnTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsdependsOnTypeDef",
    {"jobId": str, "type": Literal["N_TO_N", "SEQUENTIAL"]},
    total=False,
)


class ClientDescribeJobsResponsejobsdependsOnTypeDef(
    _ClientDescribeJobsResponsejobsdependsOnTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodeDetailsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodeDetailsTypeDef",
    {"nodeIndex": int, "isMainNode": bool},
    total=False,
)


class ClientDescribeJobsResponsejobsnodeDetailsTypeDef(
    _ClientDescribeJobsResponsejobsnodeDetailsTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef
):
    pass


_ClientDescribeJobsResponsejobsnodePropertiesTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobsResponsejobsnodePropertiesTypeDef(
    _ClientDescribeJobsResponsejobsnodePropertiesTypeDef
):
    pass


_ClientDescribeJobsResponsejobsretryStrategyTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsretryStrategyTypeDef", {"attempts": int}, total=False
)


class ClientDescribeJobsResponsejobsretryStrategyTypeDef(
    _ClientDescribeJobsResponsejobsretryStrategyTypeDef
):
    pass


_ClientDescribeJobsResponsejobstimeoutTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobstimeoutTypeDef", {"attemptDurationSeconds": int}, total=False
)


class ClientDescribeJobsResponsejobstimeoutTypeDef(_ClientDescribeJobsResponsejobstimeoutTypeDef):
    pass


_ClientDescribeJobsResponsejobsTypeDef = TypedDict(
    "_ClientDescribeJobsResponsejobsTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "attempts": List[ClientDescribeJobsResponsejobsattemptsTypeDef],
        "statusReason": str,
        "createdAt": int,
        "retryStrategy": ClientDescribeJobsResponsejobsretryStrategyTypeDef,
        "startedAt": int,
        "stoppedAt": int,
        "dependsOn": List[ClientDescribeJobsResponsejobsdependsOnTypeDef],
        "jobDefinition": str,
        "parameters": Dict[str, str],
        "container": ClientDescribeJobsResponsejobscontainerTypeDef,
        "nodeDetails": ClientDescribeJobsResponsejobsnodeDetailsTypeDef,
        "nodeProperties": ClientDescribeJobsResponsejobsnodePropertiesTypeDef,
        "arrayProperties": ClientDescribeJobsResponsejobsarrayPropertiesTypeDef,
        "timeout": ClientDescribeJobsResponsejobstimeoutTypeDef,
    },
    total=False,
)


class ClientDescribeJobsResponsejobsTypeDef(_ClientDescribeJobsResponsejobsTypeDef):
    """
    - *(dict) --*

      An object representing an AWS Batch job.
      - **jobName** *(string) --*

        The name of the job.
    """


_ClientDescribeJobsResponseTypeDef = TypedDict(
    "_ClientDescribeJobsResponseTypeDef",
    {"jobs": List[ClientDescribeJobsResponsejobsTypeDef]},
    total=False,
)


class ClientDescribeJobsResponseTypeDef(_ClientDescribeJobsResponseTypeDef):
    """
    - *(dict) --*

      - **jobs** *(list) --*

        The list of jobs.
        - *(dict) --*

          An object representing an AWS Batch job.
          - **jobName** *(string) --*

            The name of the job.
    """


_ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef",
    {"size": int, "index": int},
    total=False,
)


class ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef(
    _ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef
):
    pass


_ClientListJobsResponsejobSummaryListcontainerTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListcontainerTypeDef",
    {"exitCode": int, "reason": str},
    total=False,
)


class ClientListJobsResponsejobSummaryListcontainerTypeDef(
    _ClientListJobsResponsejobSummaryListcontainerTypeDef
):
    pass


_ClientListJobsResponsejobSummaryListnodePropertiesTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListnodePropertiesTypeDef",
    {"isMainNode": bool, "numNodes": int, "nodeIndex": int},
    total=False,
)


class ClientListJobsResponsejobSummaryListnodePropertiesTypeDef(
    _ClientListJobsResponsejobSummaryListnodePropertiesTypeDef
):
    pass


_ClientListJobsResponsejobSummaryListTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummaryListTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "createdAt": int,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": ClientListJobsResponsejobSummaryListcontainerTypeDef,
        "arrayProperties": ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef,
        "nodeProperties": ClientListJobsResponsejobSummaryListnodePropertiesTypeDef,
    },
    total=False,
)


class ClientListJobsResponsejobSummaryListTypeDef(_ClientListJobsResponsejobSummaryListTypeDef):
    """
    - *(dict) --*

      An object representing summary details of a job.
      - **jobId** *(string) --*

        The ID of the job.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"jobSummaryList": List[ClientListJobsResponsejobSummaryListTypeDef], "nextToken": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      - **jobSummaryList** *(list) --*

        A list of job summaries that match the request.
        - *(dict) --*

          An object representing summary details of a job.
          - **jobId** *(string) --*

            The ID of the job.
    """


_ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef(
    _ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef(
    _ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef",
    {"devices": List[ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef]},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef(
    _ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef(
    _ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef(
    _ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef(
    _ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef(
    _ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef",
    {"host": ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef, "name": str},
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef(
    _ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef
):
    pass


_ClientRegisterJobDefinitionContainerPropertiesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionContainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef],
        "environment": List[ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef],
        "mountPoints": List[ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)


class ClientRegisterJobDefinitionContainerPropertiesTypeDef(
    _ClientRegisterJobDefinitionContainerPropertiesTypeDef
):
    """
    An object with various properties specific to single-node container-based jobs. If the job
    definition's ``type`` parameter is ``container`` , then you must specify either
    ``containerProperties`` or ``nodeProperties`` .
    - **image** *(string) --*

      The image used to start a container. This string is passed directly to the Docker daemon.
      Images in the Docker Hub registry are available by default. Other repositories are specified
      with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase),
      numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed.
      This parameter maps to ``Image`` in the `Create a container
      <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker
      Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``IMAGE`` parameter of
      `docker run <https://docs.docker.com/engine/reference/run/>`__ .
      * Images in Amazon ECR repositories use the full registry and repository URI (for example,
      ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).
      * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or
      ``mongo`` ).
      * Images in other repositories on Docker Hub are qualified with an organization name (for
      example, ``amazon/amazon-ecs-agent`` ).
      * Images in other online repositories are qualified further by a domain name (for example,
      ``quay.io/assemblyline/ubuntu`` ).
    """


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef
):
    pass


_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef(
    _ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef
):
    pass


_RequiredClientRegisterJobDefinitionNodePropertiesTypeDef = TypedDict(
    "_RequiredClientRegisterJobDefinitionNodePropertiesTypeDef", {"numNodes": int}
)
_OptionalClientRegisterJobDefinitionNodePropertiesTypeDef = TypedDict(
    "_OptionalClientRegisterJobDefinitionNodePropertiesTypeDef",
    {
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesTypeDef(
    _RequiredClientRegisterJobDefinitionNodePropertiesTypeDef,
    _OptionalClientRegisterJobDefinitionNodePropertiesTypeDef,
):
    """
    An object with various properties specific to multi-node parallel jobs. If you specify node
    properties for a job, it becomes a multi-node parallel job. For more information, see
    `Multi-node Parallel Jobs
    <https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html>`__ in the
    *AWS Batch User Guide* . If the job definition's ``type`` parameter is ``container`` , then you
    must specify either ``containerProperties`` or ``nodeProperties`` .
    - **numNodes** *(integer) --***[REQUIRED]**

      The number of nodes associated with a multi-node parallel job.
    """


_ClientRegisterJobDefinitionResponseTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionResponseTypeDef",
    {"jobDefinitionName": str, "jobDefinitionArn": str, "revision": int},
    total=False,
)


class ClientRegisterJobDefinitionResponseTypeDef(_ClientRegisterJobDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **jobDefinitionName** *(string) --*

        The name of the job definition.
    """


_ClientRegisterJobDefinitionRetryStrategyTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionRetryStrategyTypeDef", {"attempts": int}, total=False
)


class ClientRegisterJobDefinitionRetryStrategyTypeDef(
    _ClientRegisterJobDefinitionRetryStrategyTypeDef
):
    """
    The retry strategy to use for failed jobs that are submitted with this job definition. Any retry
    strategy that is specified during a  SubmitJob operation overrides the retry strategy defined
    here. If a job is terminated due to a timeout, it is not retried.
    - **attempts** *(integer) --*

      The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10
      attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the
      same number of attempts as the value.
    """


_ClientRegisterJobDefinitionTimeoutTypeDef = TypedDict(
    "_ClientRegisterJobDefinitionTimeoutTypeDef", {"attemptDurationSeconds": int}, total=False
)


class ClientRegisterJobDefinitionTimeoutTypeDef(_ClientRegisterJobDefinitionTimeoutTypeDef):
    """
    The timeout configuration for jobs that are submitted with this job definition, after which AWS
    Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout,
    it is not retried. The minimum value for the timeout is 60 seconds. Any timeout configuration
    that is specified during a  SubmitJob operation overrides the timeout configuration defined
    here. For more information, see `Job Timeouts
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html>`__ in the
    *Amazon Elastic Container Service Developer Guide* .
    - **attemptDurationSeconds** *(integer) --*

      The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp) after
      which AWS Batch terminates your jobs if they have not finished.
    """


_ClientSubmitJobArrayPropertiesTypeDef = TypedDict(
    "_ClientSubmitJobArrayPropertiesTypeDef", {"size": int}, total=False
)


class ClientSubmitJobArrayPropertiesTypeDef(_ClientSubmitJobArrayPropertiesTypeDef):
    """
    The array properties for the submitted job, such as the size of the array. The array size can be
    between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For
    more information, see `Array Jobs
    <https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html>`__ in the *AWS Batch User
    Guide* .
    - **size** *(integer) --*

      The size of the array job.
    """


_ClientSubmitJobContainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientSubmitJobContainerOverridesenvironmentTypeDef", {"name": str, "value": str}, total=False
)


class ClientSubmitJobContainerOverridesenvironmentTypeDef(
    _ClientSubmitJobContainerOverridesenvironmentTypeDef
):
    pass


_ClientSubmitJobContainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientSubmitJobContainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientSubmitJobContainerOverridesresourceRequirementsTypeDef(
    _ClientSubmitJobContainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientSubmitJobContainerOverridesTypeDef = TypedDict(
    "_ClientSubmitJobContainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List[ClientSubmitJobContainerOverridesenvironmentTypeDef],
        "resourceRequirements": List[ClientSubmitJobContainerOverridesresourceRequirementsTypeDef],
    },
    total=False,
)


class ClientSubmitJobContainerOverridesTypeDef(_ClientSubmitJobContainerOverridesTypeDef):
    """
    A list of container overrides in JSON format that specify the name of a container in the
    specified job definition and the overrides it should receive. You can override the default
    command for a container (that is specified in the job definition or the Docker image) with a
    ``command`` override. You can also override existing environment variables (that are specified
    in the job definition or Docker image) on a container or add new environment variables to it
    with an ``environment`` override.
    - **vcpus** *(integer) --*

      The number of vCPUs to reserve for the container. This value overrides the value set in the
      job definition.
    """


_ClientSubmitJobDependsOnTypeDef = TypedDict(
    "_ClientSubmitJobDependsOnTypeDef",
    {"jobId": str, "type": Literal["N_TO_N", "SEQUENTIAL"]},
    total=False,
)


class ClientSubmitJobDependsOnTypeDef(_ClientSubmitJobDependsOnTypeDef):
    """
    - *(dict) --*

      An object representing an AWS Batch job dependency.
      - **jobId** *(string) --*

        The job ID of the AWS Batch job associated with this dependency.
    """


_ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef(
    _ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef
):
    pass


_ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef = TypedDict(
    "_ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List[
            ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef
        ],
        "resourceRequirements": List[
            ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef(
    _ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef
):
    pass


_ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef = TypedDict(
    "_ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef",
    {
        "targetNodes": str,
        "containerOverrides": ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef,
    },
    total=False,
)


class ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef(
    _ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef
):
    pass


_ClientSubmitJobNodeOverridesTypeDef = TypedDict(
    "_ClientSubmitJobNodeOverridesTypeDef",
    {
        "numNodes": int,
        "nodePropertyOverrides": List[ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef],
    },
    total=False,
)


class ClientSubmitJobNodeOverridesTypeDef(_ClientSubmitJobNodeOverridesTypeDef):
    """
    A list of node overrides in JSON format that specify the node range to target and the container
    overrides for that node range.
    - **numNodes** *(integer) --*

      The number of nodes to use with a multi-node parallel job. This value overrides the number of
      nodes that are specified in the job definition. To use this override:
      * There must be at least one node range in your job definition that has an open upper boundary
      (such as ``:`` or ``n:`` ).
      * The lower boundary of the node range specified in the job definition must be fewer than the
      number of nodes specified in the override.
      * The main node index specified in the job definition must be fewer than the number of nodes
      specified in the override.
    """


_ClientSubmitJobResponseTypeDef = TypedDict(
    "_ClientSubmitJobResponseTypeDef", {"jobName": str, "jobId": str}, total=False
)


class ClientSubmitJobResponseTypeDef(_ClientSubmitJobResponseTypeDef):
    """
    - *(dict) --*

      - **jobName** *(string) --*

        The name of the job.
    """


_ClientSubmitJobRetryStrategyTypeDef = TypedDict(
    "_ClientSubmitJobRetryStrategyTypeDef", {"attempts": int}, total=False
)


class ClientSubmitJobRetryStrategyTypeDef(_ClientSubmitJobRetryStrategyTypeDef):
    """
    The retry strategy to use for failed jobs from this  SubmitJob operation. When a retry strategy
    is specified here, it overrides the retry strategy defined in the job definition.
    - **attempts** *(integer) --*

      The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10
      attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the
      same number of attempts as the value.
    """


_ClientSubmitJobTimeoutTypeDef = TypedDict(
    "_ClientSubmitJobTimeoutTypeDef", {"attemptDurationSeconds": int}, total=False
)


class ClientSubmitJobTimeoutTypeDef(_ClientSubmitJobTimeoutTypeDef):
    """
    The timeout configuration for this  SubmitJob operation. You can specify a timeout duration
    after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due
    to a timeout, it is not retried. The minimum value for the timeout is 60 seconds. This
    configuration overrides any timeout configuration specified in the job definition. For array
    jobs, child jobs have the same timeout configuration as the parent job. For more information,
    see `Job Timeouts
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html>`__ in the
    *Amazon Elastic Container Service Developer Guide* .
    - **attemptDurationSeconds** *(integer) --*

      The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp) after
      which AWS Batch terminates your jobs if they have not finished.
    """


_ClientUpdateComputeEnvironmentComputeResourcesTypeDef = TypedDict(
    "_ClientUpdateComputeEnvironmentComputeResourcesTypeDef",
    {"minvCpus": int, "maxvCpus": int, "desiredvCpus": int},
    total=False,
)


class ClientUpdateComputeEnvironmentComputeResourcesTypeDef(
    _ClientUpdateComputeEnvironmentComputeResourcesTypeDef
):
    """
    Details of the compute resources managed by the compute environment. Required for a managed
    compute environment.
    - **minvCpus** *(integer) --*

      The minimum number of Amazon EC2 vCPUs that an environment should maintain.
    """


_ClientUpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "_ClientUpdateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)


class ClientUpdateComputeEnvironmentResponseTypeDef(_ClientUpdateComputeEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      - **computeEnvironmentName** *(string) --*

        The name of the compute environment.
    """


_RequiredClientUpdateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_RequiredClientUpdateJobQueueComputeEnvironmentOrderTypeDef", {"order": int}
)
_OptionalClientUpdateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_OptionalClientUpdateJobQueueComputeEnvironmentOrderTypeDef",
    {"computeEnvironment": str},
    total=False,
)


class ClientUpdateJobQueueComputeEnvironmentOrderTypeDef(
    _RequiredClientUpdateJobQueueComputeEnvironmentOrderTypeDef,
    _OptionalClientUpdateJobQueueComputeEnvironmentOrderTypeDef,
):
    """
    - *(dict) --*

      The order in which compute environments are tried for job placement within a queue. Compute
      environments are tried in ascending order. For example, if two compute environments are
      associated with a job queue, the compute environment with a lower order integer value is tried
      for job placement first.
      - **order** *(integer) --***[REQUIRED]**

        The order of the compute environment.
    """


_ClientUpdateJobQueueResponseTypeDef = TypedDict(
    "_ClientUpdateJobQueueResponseTypeDef", {"jobQueueName": str, "jobQueueArn": str}, total=False
)


class ClientUpdateJobQueueResponseTypeDef(_ClientUpdateJobQueueResponseTypeDef):
    """
    - *(dict) --*

      - **jobQueueName** *(string) --*

        The name of the job queue.
    """


_DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef(
    _DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef(
    _DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef
):
    pass


_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef",
    {
        "type": Literal["EC2", "SPOT"],
        "allocationStrategy": Literal[
            "BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"
        ],
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef(
    _DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef
):
    pass


_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ecsClusterArn": str,
        "type": Literal["MANAGED", "UNMANAGED"],
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "computeResources": DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentscomputeResourcesTypeDef,
        "serviceRole": str,
    },
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef(
    _DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef
):
    """
    - *(dict) --*

      An object representing an AWS Batch compute environment.
      - **computeEnvironmentName** *(string) --*

        The name of the compute environment.
    """


_DescribeComputeEnvironmentsPaginateResponseTypeDef = TypedDict(
    "_DescribeComputeEnvironmentsPaginateResponseTypeDef",
    {
        "computeEnvironments": List[
            DescribeComputeEnvironmentsPaginateResponsecomputeEnvironmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeComputeEnvironmentsPaginateResponseTypeDef(
    _DescribeComputeEnvironmentsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **computeEnvironments** *(list) --*

        The list of compute environments.
        - *(dict) --*

          An object representing an AWS Batch compute environment.
          - **computeEnvironmentName** *(string) --*

            The name of the compute environment.
    """


_DescribeJobDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeJobDefinitionsPaginatePaginationConfigTypeDef(
    _DescribeJobDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    {
        "devices": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    {
        "host": DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesvolumesTypeDef
        ],
        "environment": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
        ],
        "mountPoints": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef",
    {"attempts": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef",
    {"attemptDurationSeconds": int},
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef
):
    pass


_DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "status": str,
        "type": str,
        "parameters": Dict[str, str],
        "retryStrategy": DescribeJobDefinitionsPaginateResponsejobDefinitionsretryStrategyTypeDef,
        "containerProperties": DescribeJobDefinitionsPaginateResponsejobDefinitionscontainerPropertiesTypeDef,
        "timeout": DescribeJobDefinitionsPaginateResponsejobDefinitionstimeoutTypeDef,
        "nodeProperties": DescribeJobDefinitionsPaginateResponsejobDefinitionsnodePropertiesTypeDef,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef(
    _DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef
):
    """
    - *(dict) --*

      An object representing an AWS Batch job definition.
      - **jobDefinitionName** *(string) --*

        The name of the job definition.
    """


_DescribeJobDefinitionsPaginateResponseTypeDef = TypedDict(
    "_DescribeJobDefinitionsPaginateResponseTypeDef",
    {
        "jobDefinitions": List[DescribeJobDefinitionsPaginateResponsejobDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeJobDefinitionsPaginateResponseTypeDef(_DescribeJobDefinitionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **jobDefinitions** *(list) --*

        The list of job definitions.
        - *(dict) --*

          An object representing an AWS Batch job definition.
          - **jobDefinitionName** *(string) --*

            The name of the job definition.
    """


_DescribeJobQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeJobQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeJobQueuesPaginatePaginationConfigTypeDef(
    _DescribeJobQueuesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef = TypedDict(
    "_DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef",
    {"order": int, "computeEnvironment": str},
    total=False,
)


class DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef(
    _DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef
):
    pass


_DescribeJobQueuesPaginateResponsejobQueuesTypeDef = TypedDict(
    "_DescribeJobQueuesPaginateResponsejobQueuesTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "priority": int,
        "computeEnvironmentOrder": List[
            DescribeJobQueuesPaginateResponsejobQueuescomputeEnvironmentOrderTypeDef
        ],
    },
    total=False,
)


class DescribeJobQueuesPaginateResponsejobQueuesTypeDef(
    _DescribeJobQueuesPaginateResponsejobQueuesTypeDef
):
    """
    - *(dict) --*

      An object representing the details of an AWS Batch job queue.
      - **jobQueueName** *(string) --*

        The name of the job queue.
    """


_DescribeJobQueuesPaginateResponseTypeDef = TypedDict(
    "_DescribeJobQueuesPaginateResponseTypeDef",
    {"jobQueues": List[DescribeJobQueuesPaginateResponsejobQueuesTypeDef], "NextToken": str},
    total=False,
)


class DescribeJobQueuesPaginateResponseTypeDef(_DescribeJobQueuesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **jobQueues** *(list) --*

        The list of job queues.
        - *(dict) --*

          An object representing the details of an AWS Batch job queue.
          - **jobQueueName** *(string) --*

            The name of the job queue.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef",
    {"size": int, "index": int},
    total=False,
)


class ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef(
    _ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef
):
    pass


_ListJobsPaginateResponsejobSummaryListcontainerTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListcontainerTypeDef",
    {"exitCode": int, "reason": str},
    total=False,
)


class ListJobsPaginateResponsejobSummaryListcontainerTypeDef(
    _ListJobsPaginateResponsejobSummaryListcontainerTypeDef
):
    pass


_ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef",
    {"isMainNode": bool, "numNodes": int, "nodeIndex": int},
    total=False,
)


class ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef(
    _ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef
):
    pass


_ListJobsPaginateResponsejobSummaryListTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummaryListTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "createdAt": int,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": ListJobsPaginateResponsejobSummaryListcontainerTypeDef,
        "arrayProperties": ListJobsPaginateResponsejobSummaryListarrayPropertiesTypeDef,
        "nodeProperties": ListJobsPaginateResponsejobSummaryListnodePropertiesTypeDef,
    },
    total=False,
)


class ListJobsPaginateResponsejobSummaryListTypeDef(_ListJobsPaginateResponsejobSummaryListTypeDef):
    """
    - *(dict) --*

      An object representing summary details of a job.
      - **jobId** *(string) --*

        The ID of the job.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"jobSummaryList": List[ListJobsPaginateResponsejobSummaryListTypeDef], "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **jobSummaryList** *(list) --*

        A list of job summaries that match the request.
        - *(dict) --*

          An object representing summary details of a job.
          - **jobId** *(string) --*

            The ID of the job.
    """
