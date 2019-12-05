"Main interface for serverlessrepo service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "ClientCreateApplicationResponseVersionParameterDefinitionsTypeDef",
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

ClientCreateApplicationResponseVersionTypeDef = TypedDict(
    "ClientCreateApplicationResponseVersionTypeDef",
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

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef",
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

ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef = TypedDict(
    "ClientCreateApplicationVersionResponseParameterDefinitionsTypeDef",
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

ClientCreateApplicationVersionResponseTypeDef = TypedDict(
    "ClientCreateApplicationVersionResponseTypeDef",
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
    pass


ClientCreateCloudFormationChangeSetResponseTypeDef = TypedDict(
    "ClientCreateCloudFormationChangeSetResponseTypeDef",
    {"ApplicationId": str, "ChangeSetId": str, "SemanticVersion": str, "StackId": str},
    total=False,
)

ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)

ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef = TypedDict(
    "ClientCreateCloudFormationChangeSetRollbackConfigurationTypeDef",
    {
        "MonitoringTimeInMinutes": int,
        "RollbackTriggers": List[
            ClientCreateCloudFormationChangeSetRollbackConfigurationRollbackTriggersTypeDef
        ],
    },
    total=False,
)

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
    pass


ClientCreateCloudFormationTemplateResponseTypeDef = TypedDict(
    "ClientCreateCloudFormationTemplateResponseTypeDef",
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

ClientGetApplicationPolicyResponseStatementsTypeDef = TypedDict(
    "ClientGetApplicationPolicyResponseStatementsTypeDef",
    {"Actions": List[str], "Principals": List[str], "StatementId": str},
    total=False,
)

ClientGetApplicationPolicyResponseTypeDef = TypedDict(
    "ClientGetApplicationPolicyResponseTypeDef",
    {"Statements": List[ClientGetApplicationPolicyResponseStatementsTypeDef]},
    total=False,
)

ClientGetApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "ClientGetApplicationResponseVersionParameterDefinitionsTypeDef",
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

ClientGetApplicationResponseVersionTypeDef = TypedDict(
    "ClientGetApplicationResponseVersionTypeDef",
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

ClientGetApplicationResponseTypeDef = TypedDict(
    "ClientGetApplicationResponseTypeDef",
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

ClientGetCloudFormationTemplateResponseTypeDef = TypedDict(
    "ClientGetCloudFormationTemplateResponseTypeDef",
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

ClientListApplicationDependenciesResponseDependenciesTypeDef = TypedDict(
    "ClientListApplicationDependenciesResponseDependenciesTypeDef",
    {"ApplicationId": str, "SemanticVersion": str},
    total=False,
)

ClientListApplicationDependenciesResponseTypeDef = TypedDict(
    "ClientListApplicationDependenciesResponseTypeDef",
    {
        "Dependencies": List[ClientListApplicationDependenciesResponseDependenciesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListApplicationVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListApplicationVersionsResponseVersionsTypeDef",
    {"ApplicationId": str, "CreationTime": str, "SemanticVersion": str, "SourceCodeUrl": str},
    total=False,
)

ClientListApplicationVersionsResponseTypeDef = TypedDict(
    "ClientListApplicationVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListApplicationVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListApplicationsResponseApplicationsTypeDef = TypedDict(
    "ClientListApplicationsResponseApplicationsTypeDef",
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

ClientListApplicationsResponseTypeDef = TypedDict(
    "ClientListApplicationsResponseTypeDef",
    {"Applications": List[ClientListApplicationsResponseApplicationsTypeDef], "NextToken": str},
    total=False,
)

ClientPutApplicationPolicyResponseStatementsTypeDef = TypedDict(
    "ClientPutApplicationPolicyResponseStatementsTypeDef",
    {"Actions": List[str], "Principals": List[str], "StatementId": str},
    total=False,
)

ClientPutApplicationPolicyResponseTypeDef = TypedDict(
    "ClientPutApplicationPolicyResponseTypeDef",
    {"Statements": List[ClientPutApplicationPolicyResponseStatementsTypeDef]},
    total=False,
)

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
    pass


ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef = TypedDict(
    "ClientUpdateApplicationResponseVersionParameterDefinitionsTypeDef",
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

ClientUpdateApplicationResponseVersionTypeDef = TypedDict(
    "ClientUpdateApplicationResponseVersionTypeDef",
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

ClientUpdateApplicationResponseTypeDef = TypedDict(
    "ClientUpdateApplicationResponseTypeDef",
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

ListApplicationDependenciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListApplicationDependenciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListApplicationDependenciesPaginateResponseDependenciesTypeDef = TypedDict(
    "ListApplicationDependenciesPaginateResponseDependenciesTypeDef",
    {"ApplicationId": str, "SemanticVersion": str},
    total=False,
)

ListApplicationDependenciesPaginateResponseTypeDef = TypedDict(
    "ListApplicationDependenciesPaginateResponseTypeDef",
    {"Dependencies": List[ListApplicationDependenciesPaginateResponseDependenciesTypeDef]},
    total=False,
)

ListApplicationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListApplicationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListApplicationVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListApplicationVersionsPaginateResponseVersionsTypeDef",
    {"ApplicationId": str, "CreationTime": str, "SemanticVersion": str, "SourceCodeUrl": str},
    total=False,
)

ListApplicationVersionsPaginateResponseTypeDef = TypedDict(
    "ListApplicationVersionsPaginateResponseTypeDef",
    {"Versions": List[ListApplicationVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListApplicationsPaginateResponseApplicationsTypeDef = TypedDict(
    "ListApplicationsPaginateResponseApplicationsTypeDef",
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

ListApplicationsPaginateResponseTypeDef = TypedDict(
    "ListApplicationsPaginateResponseTypeDef",
    {"Applications": List[ListApplicationsPaginateResponseApplicationsTypeDef]},
    total=False,
)
