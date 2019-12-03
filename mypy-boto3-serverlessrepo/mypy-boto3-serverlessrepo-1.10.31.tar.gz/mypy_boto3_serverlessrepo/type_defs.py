"Main interface for serverlessrepo service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef",
    "ClientCreateApplicationResponseVersionTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef",
    "ClientCreateApplicationVersionResponseTypeDef",
    "ClientCreateCloudFormationChangeSetParameterOverridesTypeDef",
    "ClientCreateCloudFormationChangeSetResponseTypeDef",
    "ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef",
    "ClientCreateCloudFormationChangeSetTagsTypeDef",
    "ClientCreateCloudFormationTemplateResponseTypeDef",
    "ClientGetApplicationPolicyResponseStatementsTypeDef",
    "ClientGetApplicationPolicyResponseTypeDef",
    "ClientGetApplicationResponseVersionParameterDefinitionsTypeDef",
    "ClientGetApplicationResponseVersionTypeDef",
    "ClientGetApplicationResponseTypeDef",
    "ClientGetCloudFormationTemplateResponseTypeDef",
    "ClientListApplicationDependenciesResponseDependenciesTypeDef",
    "ClientListApplicationDependenciesResponseTypeDef",
    "ClientListApplicationVersionsResponseVersionsTypeDef",
    "ClientListApplicationVersionsResponseTypeDef",
    "ClientListApplicationsResponseApplicationsTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientPutApplicationPolicyResponseStatementsTypeDef",
    "ClientPutApplicationPolicyResponseTypeDef",
    "ClientPutApplicationPolicyStatementsTypeDef",
    "ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef",
    "ClientUpdateApplicationResponseVersionTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ListApplicationDependenciesPaginatePaginationConfigTypeDef",
    "ListApplicationDependenciesPaginateResponseDependenciesTypeDef",
    "ListApplicationDependenciesPaginateResponseTypeDef",
    "ListApplicationVersionsPaginatePaginationConfigTypeDef",
    "ListApplicationVersionsPaginateResponseVersionsTypeDef",
    "ListApplicationVersionsPaginateResponseTypeDef",
    "ListApplicationsPaginatePaginationConfigTypeDef",
    "ListApplicationsPaginateResponseApplicationsTypeDef",
    "ListApplicationsPaginateResponseTypeDef",
)


_ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "_ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef(
    _ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef
):
    pass


_ClientCreateApplicationResponseVersionTypeDef = TypedDict(
    "_ClientCreateApplicationResponseVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[
            Literal[
                "CAPABILITY_IAM",
                "CAPABILITY_NAMED_IAM",
                "CAPABILITY_AUTO_EXPAND",
                "CAPABILITY_RESOURCE_POLICY",
            ]
        ],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientCreateApplicationResponseVersionTypeDef(_ClientCreateApplicationResponseVersionTypeDef):
    pass


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": ClientCreateApplicationResponseVersionTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef(
    _ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef
):
    pass


_ClientCreateApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[
            Literal[
                "CAPABILITY_IAM",
                "CAPABILITY_NAMED_IAM",
                "CAPABILITY_AUTO_EXPAND",
                "CAPABILITY_RESOURCE_POLICY",
            ]
        ],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientCreateApplicationVersionResponseTypeDef(_ClientCreateApplicationVersionResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_RequiredClientCreateCloudFormationChangeSetParameterOverridesTypeDef = TypedDict(
    "_RequiredClientCreateCloudFormationChangeSetParameterOverridesTypeDef", {"Name": str}
)
_OptionalClientCreateCloudFormationChangeSetParameterOverridesTypeDef = TypedDict(
    "_OptionalClientCreateCloudFormationChangeSetParameterOverridesTypeDef",
    {"Value": str},
    total=False,
)


class ClientCreateCloudFormationChangeSetParameterOverridesTypeDef(
    _RequiredClientCreateCloudFormationChangeSetParameterOverridesTypeDef,
    _OptionalClientCreateCloudFormationChangeSetParameterOverridesTypeDef,
):
    """
    - *(dict) --*

      Parameter value of the application.
      - **Name** *(string) --***[REQUIRED]**

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_ClientCreateCloudFormationChangeSetResponseTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetResponseTypeDef",
    {"ApplicationId": str, "ChangeSetId": str, "SemanticVersion": str, "StackId": str},
    total=False,
)


class ClientCreateCloudFormationChangeSetResponseTypeDef(
    _ClientCreateCloudFormationChangeSetResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef(
    _ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef
):
    pass


_ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef",
    {
        "MonitoringTimeInMinutes": int,
        "RollbackTriggers": List[
            ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef
        ],
    },
    total=False,
)


class ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef(
    _ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef
):
    """
    This property corresponds to the parameter of the same name for the *AWS CloudFormation
    `CreateChangeSet
    <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet>`__ * API.
    - **MonitoringTimeInMinutes** *(integer) --*

      This property corresponds to the content of the same name for the *AWS CloudFormation
      `RollbackConfiguration
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration>`__ *
      Data Type.
    """


_RequiredClientCreateCloudFormationChangeSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateCloudFormationChangeSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateCloudFormationChangeSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateCloudFormationChangeSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateCloudFormationChangeSetTagsTypeDef(
    _RequiredClientCreateCloudFormationChangeSetTagsTypeDef,
    _OptionalClientCreateCloudFormationChangeSetTagsTypeDef,
):
    """
    - *(dict) --*

      This property corresponds to the *AWS CloudFormation `Tag
      <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__ * Data Type.
      - **Key** *(string) --***[REQUIRED]**

        This property corresponds to the content of the same name for the *AWS CloudFormation `Tag
        <https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag>`__ * Data Type.
    """


_ClientCreateCloudFormationTemplateResponseTypeDef = TypedDict(
    "_ClientCreateCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": Literal["PREPARING", "ACTIVE", "EXPIRED"],
        "TemplateId": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientCreateCloudFormationTemplateResponseTypeDef(
    _ClientCreateCloudFormationTemplateResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ClientGetApplicationPolicyResponseStatementsTypeDef = TypedDict(
    "_ClientGetApplicationPolicyResponseStatementsTypeDef",
    {"Actions": List[str], "Principals": List[str], "StatementId": str},
    total=False,
)


class ClientGetApplicationPolicyResponseStatementsTypeDef(
    _ClientGetApplicationPolicyResponseStatementsTypeDef
):
    """
    - *(dict) --*

      Policy statement applied to the application.
      - **Actions** *(list) --*

        For the list of actions supported for this operation, see `Application Permissions
        <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
        .
        - *(string) --*
    """


_ClientGetApplicationPolicyResponseTypeDef = TypedDict(
    "_ClientGetApplicationPolicyResponseTypeDef",
    {"Statements": List[ClientGetApplicationPolicyResponseStatementsTypeDef]},
    total=False,
)


class ClientGetApplicationPolicyResponseTypeDef(_ClientGetApplicationPolicyResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Statements** *(list) --*

        An array of policy statements applied to the application.
        - *(dict) --*

          Policy statement applied to the application.
          - **Actions** *(list) --*

            For the list of actions supported for this operation, see `Application Permissions
            <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
            .
            - *(string) --*
    """


_ClientGetApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "_ClientGetApplicationResponseVersionParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientGetApplicationResponseVersionParameterDefinitionsTypeDef(
    _ClientGetApplicationResponseVersionParameterDefinitionsTypeDef
):
    pass


_ClientGetApplicationResponseVersionTypeDef = TypedDict(
    "_ClientGetApplicationResponseVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientGetApplicationResponseVersionParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[
            Literal[
                "CAPABILITY_IAM",
                "CAPABILITY_NAMED_IAM",
                "CAPABILITY_AUTO_EXPAND",
                "CAPABILITY_RESOURCE_POLICY",
            ]
        ],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientGetApplicationResponseVersionTypeDef(_ClientGetApplicationResponseVersionTypeDef):
    pass


_ClientGetApplicationResponseTypeDef = TypedDict(
    "_ClientGetApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": ClientGetApplicationResponseVersionTypeDef,
    },
    total=False,
)


class ClientGetApplicationResponseTypeDef(_ClientGetApplicationResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ClientGetCloudFormationTemplateResponseTypeDef = TypedDict(
    "_ClientGetCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": Literal["PREPARING", "ACTIVE", "EXPIRED"],
        "TemplateId": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientGetCloudFormationTemplateResponseTypeDef(
    _ClientGetCloudFormationTemplateResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ClientListApplicationDependenciesResponseDependenciesTypeDef = TypedDict(
    "_ClientListApplicationDependenciesResponseDependenciesTypeDef",
    {"ApplicationId": str, "SemanticVersion": str},
    total=False,
)


class ClientListApplicationDependenciesResponseDependenciesTypeDef(
    _ClientListApplicationDependenciesResponseDependenciesTypeDef
):
    """
    - *(dict) --*

      A nested application summary.
      - **ApplicationId** *(string) --*

        The Amazon Resource Name (ARN) of the nested application.
    """


_ClientListApplicationDependenciesResponseTypeDef = TypedDict(
    "_ClientListApplicationDependenciesResponseTypeDef",
    {
        "Dependencies": List[ClientListApplicationDependenciesResponseDependenciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListApplicationDependenciesResponseTypeDef(
    _ClientListApplicationDependenciesResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **Dependencies** *(list) --*

        An array of application summaries nested in the application.
        - *(dict) --*

          A nested application summary.
          - **ApplicationId** *(string) --*

            The Amazon Resource Name (ARN) of the nested application.
    """


_ClientListApplicationVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListApplicationVersionsResponseVersionsTypeDef",
    {"ApplicationId": str, "CreationTime": str, "SemanticVersion": str, "SourceCodeUrl": str},
    total=False,
)


class ClientListApplicationVersionsResponseVersionsTypeDef(
    _ClientListApplicationVersionsResponseVersionsTypeDef
):
    pass


_ClientListApplicationVersionsResponseTypeDef = TypedDict(
    "_ClientListApplicationVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListApplicationVersionsResponseVersionsTypeDef]},
    total=False,
)


class ClientListApplicationVersionsResponseTypeDef(_ClientListApplicationVersionsResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **NextToken** *(string) --*

        The token to request the next page of results.
    """


_ClientListApplicationsResponseApplicationsTypeDef = TypedDict(
    "_ClientListApplicationsResponseApplicationsTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "Name": str,
        "SpdxLicenseId": str,
    },
    total=False,
)


class ClientListApplicationsResponseApplicationsTypeDef(
    _ClientListApplicationsResponseApplicationsTypeDef
):
    """
    - *(dict) --*

      Summary of details about the application.
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {"Applications": List[ClientListApplicationsResponseApplicationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Applications** *(list) --*

        An array of application summaries.
        - *(dict) --*

          Summary of details about the application.
          - **ApplicationId** *(string) --*

            The application Amazon Resource Name (ARN).
    """


_ClientPutApplicationPolicyResponseStatementsTypeDef = TypedDict(
    "_ClientPutApplicationPolicyResponseStatementsTypeDef",
    {"Actions": List[str], "Principals": List[str], "StatementId": str},
    total=False,
)


class ClientPutApplicationPolicyResponseStatementsTypeDef(
    _ClientPutApplicationPolicyResponseStatementsTypeDef
):
    """
    - *(dict) --*

      Policy statement applied to the application.
      - **Actions** *(list) --*

        For the list of actions supported for this operation, see `Application Permissions
        <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
        .
        - *(string) --*
    """


_ClientPutApplicationPolicyResponseTypeDef = TypedDict(
    "_ClientPutApplicationPolicyResponseTypeDef",
    {"Statements": List[ClientPutApplicationPolicyResponseStatementsTypeDef]},
    total=False,
)


class ClientPutApplicationPolicyResponseTypeDef(_ClientPutApplicationPolicyResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Statements** *(list) --*

        An array of policy statements applied to the application.
        - *(dict) --*

          Policy statement applied to the application.
          - **Actions** *(list) --*

            For the list of actions supported for this operation, see `Application Permissions
            <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
            .
            - *(string) --*
    """


_RequiredClientPutApplicationPolicyStatementsTypeDef = TypedDict(
    "_RequiredClientPutApplicationPolicyStatementsTypeDef", {"Actions": List[str]}
)
_OptionalClientPutApplicationPolicyStatementsTypeDef = TypedDict(
    "_OptionalClientPutApplicationPolicyStatementsTypeDef",
    {"Principals": List[str], "StatementId": str},
    total=False,
)


class ClientPutApplicationPolicyStatementsTypeDef(
    _RequiredClientPutApplicationPolicyStatementsTypeDef,
    _OptionalClientPutApplicationPolicyStatementsTypeDef,
):
    """
    - *(dict) --*

      Policy statement applied to the application.
      - **Actions** *(list) --***[REQUIRED]**

        For the list of actions supported for this operation, see `Application Permissions
        <https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions>`__
        .
        - *(string) --*
    """


_ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "Name": str,
        "NoEcho": bool,
        "ReferencedByResources": List[str],
        "Type": str,
    },
    total=False,
)


class ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef(
    _ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef
):
    pass


_ClientUpdateApplicationResponseVersionTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[
            ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef
        ],
        "RequiredCapabilities": List[
            Literal[
                "CAPABILITY_IAM",
                "CAPABILITY_NAMED_IAM",
                "CAPABILITY_AUTO_EXPAND",
                "CAPABILITY_RESOURCE_POLICY",
            ]
        ],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
    },
    total=False,
)


class ClientUpdateApplicationResponseVersionTypeDef(_ClientUpdateApplicationResponseVersionTypeDef):
    pass


_ClientUpdateApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": ClientUpdateApplicationResponseVersionTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseTypeDef(_ClientUpdateApplicationResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ListApplicationDependenciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationDependenciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationDependenciesPaginatePaginationConfigTypeDef(
    _ListApplicationDependenciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListApplicationDependenciesPaginateResponseDependenciesTypeDef = TypedDict(
    "_ListApplicationDependenciesPaginateResponseDependenciesTypeDef",
    {"ApplicationId": str, "SemanticVersion": str},
    total=False,
)


class ListApplicationDependenciesPaginateResponseDependenciesTypeDef(
    _ListApplicationDependenciesPaginateResponseDependenciesTypeDef
):
    """
    - *(dict) --*

      A nested application summary.
      - **ApplicationId** *(string) --*

        The Amazon Resource Name (ARN) of the nested application.
    """


_ListApplicationDependenciesPaginateResponseTypeDef = TypedDict(
    "_ListApplicationDependenciesPaginateResponseTypeDef",
    {"Dependencies": List[ListApplicationDependenciesPaginateResponseDependenciesTypeDef]},
    total=False,
)


class ListApplicationDependenciesPaginateResponseTypeDef(
    _ListApplicationDependenciesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **Dependencies** *(list) --*

        An array of application summaries nested in the application.
        - *(dict) --*

          A nested application summary.
          - **ApplicationId** *(string) --*

            The Amazon Resource Name (ARN) of the nested application.
    """


_ListApplicationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationVersionsPaginatePaginationConfigTypeDef(
    _ListApplicationVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListApplicationVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListApplicationVersionsPaginateResponseVersionsTypeDef",
    {"ApplicationId": str, "CreationTime": str, "SemanticVersion": str, "SourceCodeUrl": str},
    total=False,
)


class ListApplicationVersionsPaginateResponseVersionsTypeDef(
    _ListApplicationVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*

      An application version summary.
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ListApplicationVersionsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationVersionsPaginateResponseTypeDef",
    {"Versions": List[ListApplicationVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListApplicationVersionsPaginateResponseTypeDef(
    _ListApplicationVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **Versions** *(list) --*

        An array of version summaries for the application.
        - *(dict) --*

          An application version summary.
          - **ApplicationId** *(string) --*

            The application Amazon Resource Name (ARN).
    """


_ListApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApplicationsPaginatePaginationConfigTypeDef(
    _ListApplicationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListApplicationsPaginateResponseApplicationsTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseApplicationsTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "Name": str,
        "SpdxLicenseId": str,
    },
    total=False,
)


class ListApplicationsPaginateResponseApplicationsTypeDef(
    _ListApplicationsPaginateResponseApplicationsTypeDef
):
    """
    - *(dict) --*

      Summary of details about the application.
      - **ApplicationId** *(string) --*

        The application Amazon Resource Name (ARN).
    """


_ListApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseTypeDef",
    {"Applications": List[ListApplicationsPaginateResponseApplicationsTypeDef]},
    total=False,
)


class ListApplicationsPaginateResponseTypeDef(_ListApplicationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Applications** *(list) --*

        An array of application summaries.
        - *(dict) --*

          Summary of details about the application.
          - **ApplicationId** *(string) --*

            The application Amazon Resource Name (ARN).
    """
