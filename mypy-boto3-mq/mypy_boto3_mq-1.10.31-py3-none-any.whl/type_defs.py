"Main interface for mq service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateBrokerConfigurationTypeDef",
    "ClientCreateBrokerEncryptionOptionsTypeDef",
    "ClientCreateBrokerLogsTypeDef",
    "ClientCreateBrokerMaintenanceWindowStartTimeTypeDef",
    "ClientCreateBrokerResponseTypeDef",
    "ClientCreateBrokerUsersTypeDef",
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    "ClientCreateConfigurationResponseTypeDef",
    "ClientDeleteBrokerResponseTypeDef",
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef",
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef",
    "ClientDescribeBrokerEngineTypesResponseTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseTypeDef",
    "ClientDescribeBrokerResponseBrokerInstancesTypeDef",
    "ClientDescribeBrokerResponseConfigurationsCurrentTypeDef",
    "ClientDescribeBrokerResponseConfigurationsHistoryTypeDef",
    "ClientDescribeBrokerResponseConfigurationsPendingTypeDef",
    "ClientDescribeBrokerResponseConfigurationsTypeDef",
    "ClientDescribeBrokerResponseEncryptionOptionsTypeDef",
    "ClientDescribeBrokerResponseLogsPendingTypeDef",
    "ClientDescribeBrokerResponseLogsTypeDef",
    "ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef",
    "ClientDescribeBrokerResponseUsersTypeDef",
    "ClientDescribeBrokerResponseTypeDef",
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    "ClientDescribeConfigurationResponseTypeDef",
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    "ClientDescribeUserResponsePendingTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientListBrokersResponseBrokerSummariesTypeDef",
    "ClientListBrokersResponseTypeDef",
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    "ClientListConfigurationRevisionsResponseTypeDef",
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientUpdateBrokerConfigurationTypeDef",
    "ClientUpdateBrokerLogsTypeDef",
    "ClientUpdateBrokerResponseConfigurationTypeDef",
    "ClientUpdateBrokerResponseLogsTypeDef",
    "ClientUpdateBrokerResponseTypeDef",
    "ClientUpdateConfigurationResponseLatestRevisionTypeDef",
    "ClientUpdateConfigurationResponseWarningsTypeDef",
    "ClientUpdateConfigurationResponseTypeDef",
    "ListBrokersPaginatePaginationConfigTypeDef",
    "ListBrokersPaginateResponseBrokerSummariesTypeDef",
    "ListBrokersPaginateResponseTypeDef",
)


_ClientCreateBrokerConfigurationTypeDef = TypedDict(
    "_ClientCreateBrokerConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)


class ClientCreateBrokerConfigurationTypeDef(_ClientCreateBrokerConfigurationTypeDef):
    """
    - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the configuration.
    - **Revision** *(integer) --*The revision number of the configuration.
    """


_RequiredClientCreateBrokerEncryptionOptionsTypeDef = TypedDict(
    "_RequiredClientCreateBrokerEncryptionOptionsTypeDef", {"UseAwsOwnedKey": bool}
)
_OptionalClientCreateBrokerEncryptionOptionsTypeDef = TypedDict(
    "_OptionalClientCreateBrokerEncryptionOptionsTypeDef", {"KmsKeyId": str}, total=False
)


class ClientCreateBrokerEncryptionOptionsTypeDef(
    _RequiredClientCreateBrokerEncryptionOptionsTypeDef,
    _OptionalClientCreateBrokerEncryptionOptionsTypeDef,
):
    """
    - **KmsKeyId** *(string) --*The customer master key (CMK) to use for the AWS Key Management
    Service (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will
    use a default CMK to encrypt your data.
    - **UseAwsOwnedKey** *(boolean) --***[REQUIRED]** Enables the use of an AWS owned CMK using AWS
    Key Management Service (KMS).
    """


_ClientCreateBrokerLogsTypeDef = TypedDict(
    "_ClientCreateBrokerLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)


class ClientCreateBrokerLogsTypeDef(_ClientCreateBrokerLogsTypeDef):
    """
    - **Audit** *(boolean) --*Enables audit logging. Every user management action made using JMX or
    the ActiveMQ Web Console is logged.
    - **General** *(boolean) --*Enables general logging.
    """


_ClientCreateBrokerMaintenanceWindowStartTimeTypeDef = TypedDict(
    "_ClientCreateBrokerMaintenanceWindowStartTimeTypeDef",
    {
        "DayOfWeek": Literal[
            "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
        ],
        "TimeOfDay": str,
        "TimeZone": str,
    },
    total=False,
)


class ClientCreateBrokerMaintenanceWindowStartTimeTypeDef(
    _ClientCreateBrokerMaintenanceWindowStartTimeTypeDef
):
    """
    - **DayOfWeek** *(string) --*Required. The day of the week.
    - **TimeOfDay** *(string) --*Required. The time, in 24-hour format.
    - **TimeZone** *(string) --*The time zone, UTC by default, in either the Country/City format, or
    the UTC offset format.
    """


_ClientCreateBrokerResponseTypeDef = TypedDict(
    "_ClientCreateBrokerResponseTypeDef", {"BrokerArn": str, "BrokerId": str}, total=False
)


class ClientCreateBrokerResponseTypeDef(_ClientCreateBrokerResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerArn** *(string) --*The Amazon Resource Name (ARN) of the broker.
      - **BrokerId** *(string) --*The unique ID that Amazon MQ generates for the broker.
    """


_ClientCreateBrokerUsersTypeDef = TypedDict(
    "_ClientCreateBrokerUsersTypeDef",
    {"ConsoleAccess": bool, "Groups": List[str], "Password": str, "Username": str},
    total=False,
)


class ClientCreateBrokerUsersTypeDef(_ClientCreateBrokerUsersTypeDef):
    """
    - *(dict) --*An ActiveMQ user associated with the broker.

      - **ConsoleAccess** *(boolean) --*Enables access to the the ActiveMQ Web Console for the
      ActiveMQ user.
      - **Groups** *(list) --*The list of groups (20 maximum) to which the ActiveMQ user belongs.
      This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes
      (- . _ ~). This value must be 2-100 characters long.

        - *(string) --*
    """


_ClientCreateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientCreateConfigurationResponseLatestRevisionTypeDef(
    _ClientCreateConfigurationResponseLatestRevisionTypeDef
):
    """
    - **LatestRevision** *(dict) --*The latest revision of the configuration.

      - **Created** *(datetime) --*Required. The date and time of the configuration revision.
      - **Description** *(string) --*The description of the configuration revision.
      - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientCreateConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ClientCreateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientCreateConfigurationResponseTypeDef(_ClientCreateConfigurationResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **Arn** *(string) --*Required. The Amazon Resource Name (ARN) of the configuration.
      - **Created** *(datetime) --*Required. The date and time of the configuration.
      - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the configuration.
      - **LatestRevision** *(dict) --*The latest revision of the configuration.

        - **Created** *(datetime) --*Required. The date and time of the configuration revision.
        - **Description** *(string) --*The description of the configuration revision.
        - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientDeleteBrokerResponseTypeDef = TypedDict(
    "_ClientDeleteBrokerResponseTypeDef", {"BrokerId": str}, total=False
)


class ClientDeleteBrokerResponseTypeDef(_ClientDeleteBrokerResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerId** *(string) --*The unique ID that Amazon MQ generates for the broker.
    """


_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef = TypedDict(
    "_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef(
    _ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef
):
    """
    - *(dict) --*Id of the engine version.

      - **Name** *(string) --*Id for the version.
    """


_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef = TypedDict(
    "_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef",
    {
        "EngineType": str,
        "EngineVersions": List[
            ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef(
    _ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef
):
    """
    - *(dict) --*Types of broker engines.

      - **EngineType** *(string) --*The type of broker engine.
      - **EngineVersions** *(list) --*The list of engine versions.

        - *(dict) --*Id of the engine version.

          - **Name** *(string) --*Id for the version.
    """


_ClientDescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "_ClientDescribeBrokerEngineTypesResponseTypeDef",
    {
        "BrokerEngineTypes": List[ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeBrokerEngineTypesResponseTypeDef(
    _ClientDescribeBrokerEngineTypesResponseTypeDef
):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerEngineTypes** *(list) --*List of available engine types and versions.

        - *(dict) --*Types of broker engines.

          - **EngineType** *(string) --*The type of broker engine.
          - **EngineVersions** *(list) --*The list of engine versions.

            - *(dict) --*Id of the engine version.

              - **Name** *(string) --*Id for the version.
    """


_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef(
    _ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef
):
    """
    - *(dict) --*Name of the availability zone.

      - **Name** *(string) --*Id for the availability zone.
    """


_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef = TypedDict(
    "_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef",
    {
        "AvailabilityZones": List[
            ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef
        ],
        "EngineType": str,
        "HostInstanceType": str,
        "SupportedEngineVersions": List[str],
    },
    total=False,
)


class ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef(
    _ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef
):
    """
    - *(dict) --*Option for host instance type.

      - **AvailabilityZones** *(list) --*The list of available az.

        - *(dict) --*Name of the availability zone.

          - **Name** *(string) --*Id for the availability zone.
    """


_ClientDescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List[
            ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef
        ],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeBrokerInstanceOptionsResponseTypeDef(
    _ClientDescribeBrokerInstanceOptionsResponseTypeDef
):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerInstanceOptions** *(list) --*List of available broker instance options.

        - *(dict) --*Option for host instance type.

          - **AvailabilityZones** *(list) --*The list of available az.

            - *(dict) --*Name of the availability zone.

              - **Name** *(string) --*Id for the availability zone.
    """


_ClientDescribeBrokerResponseBrokerInstancesTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseBrokerInstancesTypeDef",
    {"ConsoleURL": str, "Endpoints": List[str], "IpAddress": str},
    total=False,
)


class ClientDescribeBrokerResponseBrokerInstancesTypeDef(
    _ClientDescribeBrokerResponseBrokerInstancesTypeDef
):
    """
    - *(dict) --*Returns information about all brokers.

      - **ConsoleURL** *(string) --*The URL of the broker's ActiveMQ Web Console.
      - **Endpoints** *(list) --*The broker's wire-level protocol endpoints.

        - *(string) --*
    """


_ClientDescribeBrokerResponseConfigurationsCurrentTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsCurrentTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsCurrentTypeDef(
    _ClientDescribeBrokerResponseConfigurationsCurrentTypeDef
):
    pass


_ClientDescribeBrokerResponseConfigurationsHistoryTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsHistoryTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsHistoryTypeDef(
    _ClientDescribeBrokerResponseConfigurationsHistoryTypeDef
):
    pass


_ClientDescribeBrokerResponseConfigurationsPendingTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsPendingTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsPendingTypeDef(
    _ClientDescribeBrokerResponseConfigurationsPendingTypeDef
):
    pass


_ClientDescribeBrokerResponseConfigurationsTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsTypeDef",
    {
        "Current": ClientDescribeBrokerResponseConfigurationsCurrentTypeDef,
        "History": List[ClientDescribeBrokerResponseConfigurationsHistoryTypeDef],
        "Pending": ClientDescribeBrokerResponseConfigurationsPendingTypeDef,
    },
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsTypeDef(
    _ClientDescribeBrokerResponseConfigurationsTypeDef
):
    pass


_ClientDescribeBrokerResponseEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseEncryptionOptionsTypeDef",
    {"KmsKeyId": str, "UseAwsOwnedKey": bool},
    total=False,
)


class ClientDescribeBrokerResponseEncryptionOptionsTypeDef(
    _ClientDescribeBrokerResponseEncryptionOptionsTypeDef
):
    pass


_ClientDescribeBrokerResponseLogsPendingTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseLogsPendingTypeDef", {"Audit": bool, "General": bool}, total=False
)


class ClientDescribeBrokerResponseLogsPendingTypeDef(
    _ClientDescribeBrokerResponseLogsPendingTypeDef
):
    pass


_ClientDescribeBrokerResponseLogsTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseLogsTypeDef",
    {
        "Audit": bool,
        "AuditLogGroup": str,
        "General": bool,
        "GeneralLogGroup": str,
        "Pending": ClientDescribeBrokerResponseLogsPendingTypeDef,
    },
    total=False,
)


class ClientDescribeBrokerResponseLogsTypeDef(_ClientDescribeBrokerResponseLogsTypeDef):
    pass


_ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef",
    {
        "DayOfWeek": Literal[
            "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
        ],
        "TimeOfDay": str,
        "TimeZone": str,
    },
    total=False,
)


class ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef(
    _ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef
):
    pass


_ClientDescribeBrokerResponseUsersTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseUsersTypeDef",
    {"PendingChange": Literal["CREATE", "UPDATE", "DELETE"], "Username": str},
    total=False,
)


class ClientDescribeBrokerResponseUsersTypeDef(_ClientDescribeBrokerResponseUsersTypeDef):
    pass


_ClientDescribeBrokerResponseTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List[ClientDescribeBrokerResponseBrokerInstancesTypeDef],
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Configurations": ClientDescribeBrokerResponseConfigurationsTypeDef,
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"],
        "EncryptionOptions": ClientDescribeBrokerResponseEncryptionOptionsTypeDef,
        "EngineType": str,
        "EngineVersion": str,
        "HostInstanceType": str,
        "Logs": ClientDescribeBrokerResponseLogsTypeDef,
        "MaintenanceWindowStartTime": ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef,
        "PendingEngineVersion": str,
        "PendingSecurityGroups": List[str],
        "PendingHostInstanceType": str,
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List[ClientDescribeBrokerResponseUsersTypeDef],
    },
    total=False,
)


class ClientDescribeBrokerResponseTypeDef(_ClientDescribeBrokerResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **AutoMinorVersionUpgrade** *(boolean) --*Required. Enables automatic upgrades to new minor
      versions for brokers, as Apache releases the versions. The automatic upgrades occur during the
      maintenance window of the broker or after a manual broker reboot.
      - **BrokerArn** *(string) --*The Amazon Resource Name (ARN) of the broker.
      - **BrokerId** *(string) --*The unique ID that Amazon MQ generates for the broker.
      - **BrokerInstances** *(list) --*A list of information about allocated brokers.

        - *(dict) --*Returns information about all brokers.

          - **ConsoleURL** *(string) --*The URL of the broker's ActiveMQ Web Console.
          - **Endpoints** *(list) --*The broker's wire-level protocol endpoints.

            - *(string) --*
    """


_ClientDescribeConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientDescribeConfigurationResponseLatestRevisionTypeDef(
    _ClientDescribeConfigurationResponseLatestRevisionTypeDef
):
    """
    - **LatestRevision** *(dict) --*Required. The latest revision of the configuration.

      - **Created** *(datetime) --*Required. The date and time of the configuration revision.
      - **Description** *(string) --*The description of the configuration revision.
      - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientDescribeConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "EngineType": str,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ClientDescribeConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeConfigurationResponseTypeDef(_ClientDescribeConfigurationResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **Arn** *(string) --*Required. The ARN of the configuration.
      - **Created** *(datetime) --*Required. The date and time of the configuration revision.
      - **Description** *(string) --*Required. The description of the configuration.
      - **EngineType** *(string) --*Required. The type of broker engine. Note: Currently, Amazon MQ
      supports only ACTIVEMQ.
      - **EngineVersion** *(string) --*Required. The version of the broker engine. For a list of
      supported engine versions, see
      https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html
      - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the configuration.
      - **LatestRevision** *(dict) --*Required. The latest revision of the configuration.

        - **Created** *(datetime) --*Required. The date and time of the configuration revision.
        - **Description** *(string) --*The description of the configuration revision.
        - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientDescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRevisionResponseTypeDef",
    {"ConfigurationId": str, "Created": datetime, "Data": str, "Description": str},
    total=False,
)


class ClientDescribeConfigurationRevisionResponseTypeDef(
    _ClientDescribeConfigurationRevisionResponseTypeDef
):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **ConfigurationId** *(string) --*Required. The unique ID that Amazon MQ generates for the
      configuration.
      - **Created** *(datetime) --*Required. The date and time of the configuration.
      - **Data** *(string) --*Required. The base64-encoded XML configuration.
      - **Description** *(string) --*The description of the configuration.
    """


_ClientDescribeUserResponsePendingTypeDef = TypedDict(
    "_ClientDescribeUserResponsePendingTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "PendingChange": Literal["CREATE", "UPDATE", "DELETE"],
    },
    total=False,
)


class ClientDescribeUserResponsePendingTypeDef(_ClientDescribeUserResponsePendingTypeDef):
    pass


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Pending": ClientDescribeUserResponsePendingTypeDef,
        "Username": str,
    },
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerId** *(string) --*Required. The unique ID that Amazon MQ generates for the broker.
      - **ConsoleAccess** *(boolean) --*Enables access to the the ActiveMQ Web Console for the
      ActiveMQ user.
      - **Groups** *(list) --*The list of groups (20 maximum) to which the ActiveMQ user belongs.
      This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes
      (- . _ ~). This value must be 2-100 characters long.

        - *(string) --*
    """


_ClientListBrokersResponseBrokerSummariesTypeDef = TypedDict(
    "_ClientListBrokersResponseBrokerSummariesTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"],
        "HostInstanceType": str,
    },
    total=False,
)


class ClientListBrokersResponseBrokerSummariesTypeDef(
    _ClientListBrokersResponseBrokerSummariesTypeDef
):
    """
    - *(dict) --*The Amazon Resource Name (ARN) of the broker.

      - **BrokerArn** *(string) --*The Amazon Resource Name (ARN) of the broker.
      - **BrokerId** *(string) --*The unique ID that Amazon MQ generates for the broker.
      - **BrokerName** *(string) --*The name of the broker. This value must be unique in your AWS
      account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores,
      and must not contain whitespaces, brackets, wildcard characters, or special characters.
      - **BrokerState** *(string) --*The status of the broker.
      - **Created** *(datetime) --*The time when the broker was created.
      - **DeploymentMode** *(string) --*Required. The deployment mode of the broker.
      - **HostInstanceType** *(string) --*The broker's instance type.
    """


_ClientListBrokersResponseTypeDef = TypedDict(
    "_ClientListBrokersResponseTypeDef",
    {"BrokerSummaries": List[ClientListBrokersResponseBrokerSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListBrokersResponseTypeDef(_ClientListBrokersResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerSummaries** *(list) --*A list of information about all brokers.

        - *(dict) --*The Amazon Resource Name (ARN) of the broker.

          - **BrokerArn** *(string) --*The Amazon Resource Name (ARN) of the broker.
          - **BrokerId** *(string) --*The unique ID that Amazon MQ generates for the broker.
          - **BrokerName** *(string) --*The name of the broker. This value must be unique in your
          AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and
          underscores, and must not contain whitespaces, brackets, wildcard characters, or special
          characters.
          - **BrokerState** *(string) --*The status of the broker.
          - **Created** *(datetime) --*The time when the broker was created.
          - **DeploymentMode** *(string) --*Required. The deployment mode of the broker.
          - **HostInstanceType** *(string) --*The broker's instance type.
    """


_ClientListConfigurationRevisionsResponseRevisionsTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationRevisionsResponseRevisionsTypeDef(
    _ClientListConfigurationRevisionsResponseRevisionsTypeDef
):
    """
    - *(dict) --*Returns information about the specified configuration revision.

      - **Created** *(datetime) --*Required. The date and time of the configuration revision.
      - **Description** *(string) --*The description of the configuration revision.
      - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientListConfigurationRevisionsResponseTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "NextToken": str,
        "Revisions": List[ClientListConfigurationRevisionsResponseRevisionsTypeDef],
    },
    total=False,
)


class ClientListConfigurationRevisionsResponseTypeDef(
    _ClientListConfigurationRevisionsResponseTypeDef
):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **ConfigurationId** *(string) --*The unique ID that Amazon MQ generates for the
      configuration.
      - **MaxResults** *(integer) --*The maximum number of configuration revisions that can be
      returned per page (20 by default). This value must be an integer from 5 to 100.
      - **NextToken** *(string) --*The token that specifies the next page of results Amazon MQ
      should return. To request the first page, leave nextToken empty.
      - **Revisions** *(list) --*The list of all revisions for the specified configuration.

        - *(dict) --*Returns information about the specified configuration revision.

          - **Created** *(datetime) --*Required. The date and time of the configuration revision.
          - **Description** *(string) --*The description of the configuration revision.
          - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef(
    _ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef
):
    """
    - **LatestRevision** *(dict) --*Required. The latest revision of the configuration.

      - **Created** *(datetime) --*Required. The date and time of the configuration revision.
      - **Description** *(string) --*The description of the configuration revision.
      - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientListConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "EngineType": str,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListConfigurationsResponseConfigurationsTypeDef(
    _ClientListConfigurationsResponseConfigurationsTypeDef
):
    """
    - *(dict) --*Returns information about all configurations.

      - **Arn** *(string) --*Required. The ARN of the configuration.
      - **Created** *(datetime) --*Required. The date and time of the configuration revision.
      - **Description** *(string) --*Required. The description of the configuration.
      - **EngineType** *(string) --*Required. The type of broker engine. Note: Currently, Amazon MQ
      supports only ACTIVEMQ.
      - **EngineVersion** *(string) --*Required. The version of the broker engine. For a list of
      supported engine versions, see
      https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html
      - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the configuration.
      - **LatestRevision** *(dict) --*Required. The latest revision of the configuration.

        - **Created** *(datetime) --*Required. The date and time of the configuration revision.
        - **Description** *(string) --*The description of the configuration revision.
        - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientListConfigurationsResponseTypeDef = TypedDict(
    "_ClientListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ClientListConfigurationsResponseConfigurationsTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientListConfigurationsResponseTypeDef(_ClientListConfigurationsResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **Configurations** *(list) --*The list of all revisions for the specified configuration.

        - *(dict) --*Returns information about all configurations.

          - **Arn** *(string) --*Required. The ARN of the configuration.
          - **Created** *(datetime) --*Required. The date and time of the configuration revision.
          - **Description** *(string) --*Required. The description of the configuration.
          - **EngineType** *(string) --*Required. The type of broker engine. Note: Currently, Amazon
          MQ supports only ACTIVEMQ.
          - **EngineVersion** *(string) --*Required. The version of the broker engine. For a list of
          supported engine versions, see
          https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html
          - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the
          configuration.
          - **LatestRevision** *(dict) --*Required. The latest revision of the configuration.

            - **Created** *(datetime) --*Required. The date and time of the configuration revision.
            - **Description** *(string) --*The description of the configuration revision.
            - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **Tags** *(dict) --*The key-value pair for the resource tag.

        - *(string) --*

          - *(string) --*
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {"PendingChange": Literal["CREATE", "UPDATE", "DELETE"], "Username": str},
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    - *(dict) --*Returns a list of all ActiveMQ users.

      - **PendingChange** *(string) --*The type of change pending for the ActiveMQ user.
      - **Username** *(string) --*Required. The username of the ActiveMQ user. This value can
      contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This
      value must be 2-100 characters long.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {
        "BrokerId": str,
        "MaxResults": int,
        "NextToken": str,
        "Users": List[ClientListUsersResponseUsersTypeDef],
    },
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerId** *(string) --*Required. The unique ID that Amazon MQ generates for the broker.
      - **MaxResults** *(integer) --*Required. The maximum number of ActiveMQ users that can be
      returned per page (20 by default). This value must be an integer from 5 to 100.
      - **NextToken** *(string) --*The token that specifies the next page of results Amazon MQ
      should return. To request the first page, leave nextToken empty.
      - **Users** *(list) --*Required. The list of all ActiveMQ usernames for the specified broker.

        - *(dict) --*Returns a list of all ActiveMQ users.

          - **PendingChange** *(string) --*The type of change pending for the ActiveMQ user.
          - **Username** *(string) --*Required. The username of the ActiveMQ user. This value can
          contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~).
          This value must be 2-100 characters long.
    """


_ClientUpdateBrokerConfigurationTypeDef = TypedDict(
    "_ClientUpdateBrokerConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)


class ClientUpdateBrokerConfigurationTypeDef(_ClientUpdateBrokerConfigurationTypeDef):
    """
    - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the configuration.
    - **Revision** *(integer) --*The revision number of the configuration.
    """


_ClientUpdateBrokerLogsTypeDef = TypedDict(
    "_ClientUpdateBrokerLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)


class ClientUpdateBrokerLogsTypeDef(_ClientUpdateBrokerLogsTypeDef):
    """
    - **Audit** *(boolean) --*Enables audit logging. Every user management action made using JMX or
    the ActiveMQ Web Console is logged.
    - **General** *(boolean) --*Enables general logging.
    """


_ClientUpdateBrokerResponseConfigurationTypeDef = TypedDict(
    "_ClientUpdateBrokerResponseConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)


class ClientUpdateBrokerResponseConfigurationTypeDef(
    _ClientUpdateBrokerResponseConfigurationTypeDef
):
    """
    - **Configuration** *(dict) --*The ID of the updated configuration.

      - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the configuration.
      - **Revision** *(integer) --*The revision number of the configuration.
    """


_ClientUpdateBrokerResponseLogsTypeDef = TypedDict(
    "_ClientUpdateBrokerResponseLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)


class ClientUpdateBrokerResponseLogsTypeDef(_ClientUpdateBrokerResponseLogsTypeDef):
    pass


_ClientUpdateBrokerResponseTypeDef = TypedDict(
    "_ClientUpdateBrokerResponseTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": ClientUpdateBrokerResponseConfigurationTypeDef,
        "EngineVersion": str,
        "HostInstanceType": str,
        "Logs": ClientUpdateBrokerResponseLogsTypeDef,
        "SecurityGroups": List[str],
    },
    total=False,
)


class ClientUpdateBrokerResponseTypeDef(_ClientUpdateBrokerResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **AutoMinorVersionUpgrade** *(boolean) --*The new value of automatic upgrades to new minor
      version for brokers.
      - **BrokerId** *(string) --*Required. The unique ID that Amazon MQ generates for the broker.
      - **Configuration** *(dict) --*The ID of the updated configuration.

        - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the
        configuration.
        - **Revision** *(integer) --*The revision number of the configuration.
    """


_ClientUpdateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientUpdateConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientUpdateConfigurationResponseLatestRevisionTypeDef(
    _ClientUpdateConfigurationResponseLatestRevisionTypeDef
):
    """
    - **LatestRevision** *(dict) --*The latest revision of the configuration.

      - **Created** *(datetime) --*Required. The date and time of the configuration revision.
      - **Description** *(string) --*The description of the configuration revision.
      - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ClientUpdateConfigurationResponseWarningsTypeDef = TypedDict(
    "_ClientUpdateConfigurationResponseWarningsTypeDef",
    {
        "AttributeName": str,
        "ElementName": str,
        "Reason": Literal[
            "DISALLOWED_ELEMENT_REMOVED",
            "DISALLOWED_ATTRIBUTE_REMOVED",
            "INVALID_ATTRIBUTE_VALUE_REMOVED",
        ],
    },
    total=False,
)


class ClientUpdateConfigurationResponseWarningsTypeDef(
    _ClientUpdateConfigurationResponseWarningsTypeDef
):
    pass


_ClientUpdateConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ClientUpdateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
        "Warnings": List[ClientUpdateConfigurationResponseWarningsTypeDef],
    },
    total=False,
)


class ClientUpdateConfigurationResponseTypeDef(_ClientUpdateConfigurationResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **Arn** *(string) --*Required. The Amazon Resource Name (ARN) of the configuration.
      - **Created** *(datetime) --*Required. The date and time of the configuration.
      - **Id** *(string) --*Required. The unique ID that Amazon MQ generates for the configuration.
      - **LatestRevision** *(dict) --*The latest revision of the configuration.

        - **Created** *(datetime) --*Required. The date and time of the configuration revision.
        - **Description** *(string) --*The description of the configuration revision.
        - **Revision** *(integer) --*Required. The revision number of the configuration.
    """


_ListBrokersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBrokersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBrokersPaginatePaginationConfigTypeDef(_ListBrokersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBrokersPaginateResponseBrokerSummariesTypeDef = TypedDict(
    "_ListBrokersPaginateResponseBrokerSummariesTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"],
        "HostInstanceType": str,
    },
    total=False,
)


class ListBrokersPaginateResponseBrokerSummariesTypeDef(
    _ListBrokersPaginateResponseBrokerSummariesTypeDef
):
    """
    - *(dict) --*The Amazon Resource Name (ARN) of the broker.

      - **BrokerArn** *(string) --*The Amazon Resource Name (ARN) of the broker.
      - **BrokerId** *(string) --*The unique ID that Amazon MQ generates for the broker.
      - **BrokerName** *(string) --*The name of the broker. This value must be unique in your AWS
      account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores,
      and must not contain whitespaces, brackets, wildcard characters, or special characters.
      - **BrokerState** *(string) --*The status of the broker.
      - **Created** *(datetime) --*The time when the broker was created.
      - **DeploymentMode** *(string) --*Required. The deployment mode of the broker.
      - **HostInstanceType** *(string) --*The broker's instance type.
    """


_ListBrokersPaginateResponseTypeDef = TypedDict(
    "_ListBrokersPaginateResponseTypeDef",
    {"BrokerSummaries": List[ListBrokersPaginateResponseBrokerSummariesTypeDef]},
    total=False,
)


class ListBrokersPaginateResponseTypeDef(_ListBrokersPaginateResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **BrokerSummaries** *(list) --*A list of information about all brokers.

        - *(dict) --*The Amazon Resource Name (ARN) of the broker.

          - **BrokerArn** *(string) --*The Amazon Resource Name (ARN) of the broker.
          - **BrokerId** *(string) --*The unique ID that Amazon MQ generates for the broker.
          - **BrokerName** *(string) --*The name of the broker. This value must be unique in your
          AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and
          underscores, and must not contain whitespaces, brackets, wildcard characters, or special
          characters.
          - **BrokerState** *(string) --*The status of the broker.
          - **Created** *(datetime) --*The time when the broker was created.
          - **DeploymentMode** *(string) --*Required. The deployment mode of the broker.
          - **HostInstanceType** *(string) --*The broker's instance type.
    """
