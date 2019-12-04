"Main interface for backup service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef",
    "ClientCreateBackupPlanBackupPlanRulesTypeDef",
    "ClientCreateBackupPlanBackupPlanTypeDef",
    "ClientCreateBackupPlanResponseTypeDef",
    "ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef",
    "ClientCreateBackupSelectionBackupSelectionTypeDef",
    "ClientCreateBackupSelectionResponseTypeDef",
    "ClientCreateBackupVaultResponseTypeDef",
    "ClientDeleteBackupPlanResponseTypeDef",
    "ClientDescribeBackupJobResponseCreatedByTypeDef",
    "ClientDescribeBackupJobResponseTypeDef",
    "ClientDescribeBackupVaultResponseTypeDef",
    "ClientDescribeProtectedResourceResponseTypeDef",
    "ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef",
    "ClientDescribeRecoveryPointResponseCreatedByTypeDef",
    "ClientDescribeRecoveryPointResponseLifecycleTypeDef",
    "ClientDescribeRecoveryPointResponseTypeDef",
    "ClientDescribeRestoreJobResponseTypeDef",
    "ClientExportBackupPlanTemplateResponseTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef",
    "ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef",
    "ClientGetBackupPlanFromJsonResponseTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef",
    "ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef",
    "ClientGetBackupPlanFromTemplateResponseTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef",
    "ClientGetBackupPlanResponseBackupPlanRulesTypeDef",
    "ClientGetBackupPlanResponseBackupPlanTypeDef",
    "ClientGetBackupPlanResponseTypeDef",
    "ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef",
    "ClientGetBackupSelectionResponseBackupSelectionTypeDef",
    "ClientGetBackupSelectionResponseTypeDef",
    "ClientGetBackupVaultAccessPolicyResponseTypeDef",
    "ClientGetBackupVaultNotificationsResponseTypeDef",
    "ClientGetRecoveryPointRestoreMetadataResponseTypeDef",
    "ClientGetSupportedResourceTypesResponseTypeDef",
    "ClientListBackupJobsResponseBackupJobsCreatedByTypeDef",
    "ClientListBackupJobsResponseBackupJobsTypeDef",
    "ClientListBackupJobsResponseTypeDef",
    "ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef",
    "ClientListBackupPlanTemplatesResponseTypeDef",
    "ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef",
    "ClientListBackupPlanVersionsResponseTypeDef",
    "ClientListBackupPlansResponseBackupPlansListTypeDef",
    "ClientListBackupPlansResponseTypeDef",
    "ClientListBackupSelectionsResponseBackupSelectionsListTypeDef",
    "ClientListBackupSelectionsResponseTypeDef",
    "ClientListBackupVaultsResponseBackupVaultListTypeDef",
    "ClientListBackupVaultsResponseTypeDef",
    "ClientListProtectedResourcesResponseResultsTypeDef",
    "ClientListProtectedResourcesResponseTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef",
    "ClientListRecoveryPointsByBackupVaultResponseTypeDef",
    "ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef",
    "ClientListRecoveryPointsByResourceResponseTypeDef",
    "ClientListRestoreJobsResponseRestoreJobsTypeDef",
    "ClientListRestoreJobsResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientStartBackupJobLifecycleTypeDef",
    "ClientStartBackupJobResponseTypeDef",
    "ClientStartRestoreJobResponseTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef",
    "ClientUpdateBackupPlanBackupPlanRulesTypeDef",
    "ClientUpdateBackupPlanBackupPlanTypeDef",
    "ClientUpdateBackupPlanResponseTypeDef",
    "ClientUpdateRecoveryPointLifecycleLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef",
    "ClientUpdateRecoveryPointLifecycleResponseTypeDef",
)


_ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef(
    _ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef
):
    pass


_ClientCreateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "_ClientCreateBackupPlanBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientCreateBackupPlanBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
    },
    total=False,
)


class ClientCreateBackupPlanBackupPlanRulesTypeDef(_ClientCreateBackupPlanBackupPlanRulesTypeDef):
    pass


_RequiredClientCreateBackupPlanBackupPlanTypeDef = TypedDict(
    "_RequiredClientCreateBackupPlanBackupPlanTypeDef", {"BackupPlanName": str}
)
_OptionalClientCreateBackupPlanBackupPlanTypeDef = TypedDict(
    "_OptionalClientCreateBackupPlanBackupPlanTypeDef",
    {"Rules": List[ClientCreateBackupPlanBackupPlanRulesTypeDef]},
    total=False,
)


class ClientCreateBackupPlanBackupPlanTypeDef(
    _RequiredClientCreateBackupPlanBackupPlanTypeDef,
    _OptionalClientCreateBackupPlanBackupPlanTypeDef,
):
    """
    Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
    ``Rules`` .
    - **BackupPlanName** *(string) --***[REQUIRED]**

      The display name of a backup plan.
    """


_ClientCreateBackupPlanResponseTypeDef = TypedDict(
    "_ClientCreateBackupPlanResponseTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "CreationDate": datetime, "VersionId": str},
    total=False,
)


class ClientCreateBackupPlanResponseTypeDef(_ClientCreateBackupPlanResponseTypeDef):
    """
    - *(dict) --*

      - **BackupPlanId** *(string) --*

        Uniquely identifies a backup plan.
    """


_ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef = TypedDict(
    "_ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef",
    {"ConditionType": str, "ConditionKey": str, "ConditionValue": str},
    total=False,
)


class ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef(
    _ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef
):
    pass


_RequiredClientCreateBackupSelectionBackupSelectionTypeDef = TypedDict(
    "_RequiredClientCreateBackupSelectionBackupSelectionTypeDef", {"SelectionName": str}
)
_OptionalClientCreateBackupSelectionBackupSelectionTypeDef = TypedDict(
    "_OptionalClientCreateBackupSelectionBackupSelectionTypeDef",
    {
        "IamRoleArn": str,
        "Resources": List[str],
        "ListOfTags": List[ClientCreateBackupSelectionBackupSelectionListOfTagsTypeDef],
    },
    total=False,
)


class ClientCreateBackupSelectionBackupSelectionTypeDef(
    _RequiredClientCreateBackupSelectionBackupSelectionTypeDef,
    _OptionalClientCreateBackupSelectionBackupSelectionTypeDef,
):
    """
    Specifies the body of a request to assign a set of resources to a backup plan.
    It includes an array of resources, an optional array of patterns to exclude resources, an
    optional role to provide access to the AWS service the resource belongs to, and an optional
    array of tags used to identify a set of resources.
    - **SelectionName** *(string) --***[REQUIRED]**

      The display name of a resource selection document.
    """


_ClientCreateBackupSelectionResponseTypeDef = TypedDict(
    "_ClientCreateBackupSelectionResponseTypeDef",
    {"SelectionId": str, "BackupPlanId": str, "CreationDate": datetime},
    total=False,
)


class ClientCreateBackupSelectionResponseTypeDef(_ClientCreateBackupSelectionResponseTypeDef):
    """
    - *(dict) --*

      - **SelectionId** *(string) --*

        Uniquely identifies the body of a request to assign a set of resources to a backup plan.
    """


_ClientCreateBackupVaultResponseTypeDef = TypedDict(
    "_ClientCreateBackupVaultResponseTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "CreationDate": datetime},
    total=False,
)


class ClientCreateBackupVaultResponseTypeDef(_ClientCreateBackupVaultResponseTypeDef):
    """
    - *(dict) --*

      - **BackupVaultName** *(string) --*

        The name of a logical container where backups are stored. Backup vaults are identified by
        names that are unique to the account used to create them and the Region where they are
        created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientDeleteBackupPlanResponseTypeDef = TypedDict(
    "_ClientDeleteBackupPlanResponseTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "DeletionDate": datetime, "VersionId": str},
    total=False,
)


class ClientDeleteBackupPlanResponseTypeDef(_ClientDeleteBackupPlanResponseTypeDef):
    """
    - *(dict) --*

      - **BackupPlanId** *(string) --*

        Uniquely identifies a backup plan.
    """


_ClientDescribeBackupJobResponseCreatedByTypeDef = TypedDict(
    "_ClientDescribeBackupJobResponseCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)


class ClientDescribeBackupJobResponseCreatedByTypeDef(
    _ClientDescribeBackupJobResponseCreatedByTypeDef
):
    pass


_ClientDescribeBackupJobResponseTypeDef = TypedDict(
    "_ClientDescribeBackupJobResponseTypeDef",
    {
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientDescribeBackupJobResponseCreatedByTypeDef,
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
    },
    total=False,
)


class ClientDescribeBackupJobResponseTypeDef(_ClientDescribeBackupJobResponseTypeDef):
    """
    - *(dict) --*

      - **BackupJobId** *(string) --*

        Uniquely identifies a request to AWS Backup to back up a resource.
    """


_ClientDescribeBackupVaultResponseTypeDef = TypedDict(
    "_ClientDescribeBackupVaultResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)


class ClientDescribeBackupVaultResponseTypeDef(_ClientDescribeBackupVaultResponseTypeDef):
    """
    - *(dict) --*

      - **BackupVaultName** *(string) --*

        The name of a logical container where backups are stored. Backup vaults are identified by
        names that are unique to the account used to create them and the Region where they are
        created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientDescribeProtectedResourceResponseTypeDef = TypedDict(
    "_ClientDescribeProtectedResourceResponseTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)


class ClientDescribeProtectedResourceResponseTypeDef(
    _ClientDescribeProtectedResourceResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceArn** *(string) --*

        An ARN that uniquely identifies a resource. The format of the ARN depends on the resource
        type.
    """


_ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)


class ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef(
    _ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef
):
    pass


_ClientDescribeRecoveryPointResponseCreatedByTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)


class ClientDescribeRecoveryPointResponseCreatedByTypeDef(
    _ClientDescribeRecoveryPointResponseCreatedByTypeDef
):
    pass


_ClientDescribeRecoveryPointResponseLifecycleTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientDescribeRecoveryPointResponseLifecycleTypeDef(
    _ClientDescribeRecoveryPointResponseLifecycleTypeDef
):
    pass


_ClientDescribeRecoveryPointResponseTypeDef = TypedDict(
    "_ClientDescribeRecoveryPointResponseTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": ClientDescribeRecoveryPointResponseCreatedByTypeDef,
        "IamRoleArn": str,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": ClientDescribeRecoveryPointResponseCalculatedLifecycleTypeDef,
        "Lifecycle": ClientDescribeRecoveryPointResponseLifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": Literal["WARM", "COLD", "DELETED"],
        "LastRestoreTime": datetime,
    },
    total=False,
)


class ClientDescribeRecoveryPointResponseTypeDef(_ClientDescribeRecoveryPointResponseTypeDef):
    """
    - *(dict) --*

      - **RecoveryPointArn** *(string) --*

        An ARN that uniquely identifies a recovery point; for example,
        ``arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45``
        .
    """


_ClientDescribeRestoreJobResponseTypeDef = TypedDict(
    "_ClientDescribeRestoreJobResponseTypeDef",
    {
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal["PENDING", "RUNNING", "COMPLETED", "ABORTED", "FAILED"],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
    },
    total=False,
)


class ClientDescribeRestoreJobResponseTypeDef(_ClientDescribeRestoreJobResponseTypeDef):
    """
    - *(dict) --*

      - **RestoreJobId** *(string) --*

        Uniquely identifies the job that restores a recovery point.
    """


_ClientExportBackupPlanTemplateResponseTypeDef = TypedDict(
    "_ClientExportBackupPlanTemplateResponseTypeDef", {"BackupPlanTemplateJson": str}, total=False
)


class ClientExportBackupPlanTemplateResponseTypeDef(_ClientExportBackupPlanTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **BackupPlanTemplateJson** *(string) --*

        The body of a backup plan template in JSON format.
        .. note::

          This is a signed JSON document that cannot be modified before being passed to
          ``GetBackupPlanFromJSON.``
    """


_ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef(
    _ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef
):
    pass


_ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanFromJsonResponseBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
    },
    total=False,
)


class ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef(
    _ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef
):
    pass


_ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientGetBackupPlanFromJsonResponseBackupPlanRulesTypeDef],
    },
    total=False,
)


class ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef(
    _ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef
):
    """
    - **BackupPlan** *(dict) --*

      Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
      ``Rules`` .
      - **BackupPlanName** *(string) --*

        The display name of a backup plan.
    """


_ClientGetBackupPlanFromJsonResponseTypeDef = TypedDict(
    "_ClientGetBackupPlanFromJsonResponseTypeDef",
    {"BackupPlan": ClientGetBackupPlanFromJsonResponseBackupPlanTypeDef},
    total=False,
)


class ClientGetBackupPlanFromJsonResponseTypeDef(_ClientGetBackupPlanFromJsonResponseTypeDef):
    """
    - *(dict) --*

      - **BackupPlan** *(dict) --*

        Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
        ``Rules`` .
        - **BackupPlanName** *(string) --*

          The display name of a backup plan.
    """


_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef(
    _ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef
):
    pass


_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
    },
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef(
    _ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef
):
    pass


_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentRulesTypeDef],
    },
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef(
    _ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef
):
    """
    - **BackupPlanDocument** *(dict) --*

      Returns the body of a backup plan based on the target template, including the name, rules, and
      backup vault of the plan.
      - **BackupPlanName** *(string) --*

        The display name of a backup plan.
    """


_ClientGetBackupPlanFromTemplateResponseTypeDef = TypedDict(
    "_ClientGetBackupPlanFromTemplateResponseTypeDef",
    {"BackupPlanDocument": ClientGetBackupPlanFromTemplateResponseBackupPlanDocumentTypeDef},
    total=False,
)


class ClientGetBackupPlanFromTemplateResponseTypeDef(
    _ClientGetBackupPlanFromTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **BackupPlanDocument** *(dict) --*

        Returns the body of a backup plan based on the target template, including the name, rules,
        and backup vault of the plan.
        - **BackupPlanName** *(string) --*

          The display name of a backup plan.
    """


_ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef(
    _ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef
):
    pass


_ClientGetBackupPlanResponseBackupPlanRulesTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientGetBackupPlanResponseBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
    },
    total=False,
)


class ClientGetBackupPlanResponseBackupPlanRulesTypeDef(
    _ClientGetBackupPlanResponseBackupPlanRulesTypeDef
):
    pass


_ClientGetBackupPlanResponseBackupPlanTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseBackupPlanTypeDef",
    {"BackupPlanName": str, "Rules": List[ClientGetBackupPlanResponseBackupPlanRulesTypeDef]},
    total=False,
)


class ClientGetBackupPlanResponseBackupPlanTypeDef(_ClientGetBackupPlanResponseBackupPlanTypeDef):
    """
    - **BackupPlan** *(dict) --*

      Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
      ``Rules`` .
      - **BackupPlanName** *(string) --*

        The display name of a backup plan.
    """


_ClientGetBackupPlanResponseTypeDef = TypedDict(
    "_ClientGetBackupPlanResponseTypeDef",
    {
        "BackupPlan": ClientGetBackupPlanResponseBackupPlanTypeDef,
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
    },
    total=False,
)


class ClientGetBackupPlanResponseTypeDef(_ClientGetBackupPlanResponseTypeDef):
    """
    - *(dict) --*

      - **BackupPlan** *(dict) --*

        Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
        ``Rules`` .
        - **BackupPlanName** *(string) --*

          The display name of a backup plan.
    """


_ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef = TypedDict(
    "_ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef",
    {"ConditionType": str, "ConditionKey": str, "ConditionValue": str},
    total=False,
)


class ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef(
    _ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef
):
    pass


_ClientGetBackupSelectionResponseBackupSelectionTypeDef = TypedDict(
    "_ClientGetBackupSelectionResponseBackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
        "Resources": List[str],
        "ListOfTags": List[ClientGetBackupSelectionResponseBackupSelectionListOfTagsTypeDef],
    },
    total=False,
)


class ClientGetBackupSelectionResponseBackupSelectionTypeDef(
    _ClientGetBackupSelectionResponseBackupSelectionTypeDef
):
    """
    - **BackupSelection** *(dict) --*

      Specifies the body of a request to assign a set of resources to a backup plan.
      It includes an array of resources, an optional array of patterns to exclude resources, an
      optional role to provide access to the AWS service that the resource belongs to, and an
      optional array of tags used to identify a set of resources.
      - **SelectionName** *(string) --*

        The display name of a resource selection document.
    """


_ClientGetBackupSelectionResponseTypeDef = TypedDict(
    "_ClientGetBackupSelectionResponseTypeDef",
    {
        "BackupSelection": ClientGetBackupSelectionResponseBackupSelectionTypeDef,
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientGetBackupSelectionResponseTypeDef(_ClientGetBackupSelectionResponseTypeDef):
    """
    - *(dict) --*

      - **BackupSelection** *(dict) --*

        Specifies the body of a request to assign a set of resources to a backup plan.
        It includes an array of resources, an optional array of patterns to exclude resources, an
        optional role to provide access to the AWS service that the resource belongs to, and an
        optional array of tags used to identify a set of resources.
        - **SelectionName** *(string) --*

          The display name of a resource selection document.
    """


_ClientGetBackupVaultAccessPolicyResponseTypeDef = TypedDict(
    "_ClientGetBackupVaultAccessPolicyResponseTypeDef",
    {"BackupVaultName": str, "BackupVaultArn": str, "Policy": str},
    total=False,
)


class ClientGetBackupVaultAccessPolicyResponseTypeDef(
    _ClientGetBackupVaultAccessPolicyResponseTypeDef
):
    """
    - *(dict) --*

      - **BackupVaultName** *(string) --*

        The name of a logical container where backups are stored. Backup vaults are identified by
        names that are unique to the account used to create them and the Region where they are
        created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientGetBackupVaultNotificationsResponseTypeDef = TypedDict(
    "_ClientGetBackupVaultNotificationsResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[
            Literal[
                "BACKUP_JOB_STARTED",
                "BACKUP_JOB_COMPLETED",
                "RESTORE_JOB_STARTED",
                "RESTORE_JOB_COMPLETED",
                "RECOVERY_POINT_MODIFIED",
                "BACKUP_PLAN_CREATED",
                "BACKUP_PLAN_MODIFIED",
            ]
        ],
    },
    total=False,
)


class ClientGetBackupVaultNotificationsResponseTypeDef(
    _ClientGetBackupVaultNotificationsResponseTypeDef
):
    """
    - *(dict) --*

      - **BackupVaultName** *(string) --*

        The name of a logical container where backups are stored. Backup vaults are identified by
        names that are unique to the account used to create them and the Region where they are
        created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientGetRecoveryPointRestoreMetadataResponseTypeDef = TypedDict(
    "_ClientGetRecoveryPointRestoreMetadataResponseTypeDef",
    {"BackupVaultArn": str, "RecoveryPointArn": str, "RestoreMetadata": Dict[str, str]},
    total=False,
)


class ClientGetRecoveryPointRestoreMetadataResponseTypeDef(
    _ClientGetRecoveryPointRestoreMetadataResponseTypeDef
):
    """
    - *(dict) --*

      - **BackupVaultArn** *(string) --*

        An ARN that uniquely identifies a backup vault; for example,
        ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
    """


_ClientGetSupportedResourceTypesResponseTypeDef = TypedDict(
    "_ClientGetSupportedResourceTypesResponseTypeDef", {"ResourceTypes": List[str]}, total=False
)


class ClientGetSupportedResourceTypesResponseTypeDef(
    _ClientGetSupportedResourceTypesResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceTypes** *(list) --*

        Contains a string with the supported AWS resource types:
        * ``EBS`` for Amazon Elastic Block Store
        * ``SGW`` for AWS Storage Gateway
        * ``RDS`` for Amazon Relational Database Service
        * ``DDB`` for Amazon DynamoDB
        * ``EFS`` for Amazon Elastic File System
        - *(string) --*
    """


_ClientListBackupJobsResponseBackupJobsCreatedByTypeDef = TypedDict(
    "_ClientListBackupJobsResponseBackupJobsCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)


class ClientListBackupJobsResponseBackupJobsCreatedByTypeDef(
    _ClientListBackupJobsResponseBackupJobsCreatedByTypeDef
):
    pass


_ClientListBackupJobsResponseBackupJobsTypeDef = TypedDict(
    "_ClientListBackupJobsResponseBackupJobsTypeDef",
    {
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": ClientListBackupJobsResponseBackupJobsCreatedByTypeDef,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "ResourceType": str,
        "BytesTransferred": int,
    },
    total=False,
)


class ClientListBackupJobsResponseBackupJobsTypeDef(_ClientListBackupJobsResponseBackupJobsTypeDef):
    """
    - *(dict) --*

      Contains detailed information about a backup job.
      - **BackupJobId** *(string) --*

        Uniquely identifies a request to AWS Backup to back up a resource.
    """


_ClientListBackupJobsResponseTypeDef = TypedDict(
    "_ClientListBackupJobsResponseTypeDef",
    {"BackupJobs": List[ClientListBackupJobsResponseBackupJobsTypeDef], "NextToken": str},
    total=False,
)


class ClientListBackupJobsResponseTypeDef(_ClientListBackupJobsResponseTypeDef):
    """
    - *(dict) --*

      - **BackupJobs** *(list) --*

        An array of structures containing metadata about your backup jobs returned in JSON format.
        - *(dict) --*

          Contains detailed information about a backup job.
          - **BackupJobId** *(string) --*

            Uniquely identifies a request to AWS Backup to back up a resource.
    """


_ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef = TypedDict(
    "_ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef",
    {"BackupPlanTemplateId": str, "BackupPlanTemplateName": str},
    total=False,
)


class ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef(
    _ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef
):
    pass


_ClientListBackupPlanTemplatesResponseTypeDef = TypedDict(
    "_ClientListBackupPlanTemplatesResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanTemplatesList": List[
            ClientListBackupPlanTemplatesResponseBackupPlanTemplatesListTypeDef
        ],
    },
    total=False,
)


class ClientListBackupPlanTemplatesResponseTypeDef(_ClientListBackupPlanTemplatesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The next item following a partial list of returned items. For example, if a request is made
        to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
        your list starting at the location pointed to by the next token.
    """


_ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef = TypedDict(
    "_ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
    },
    total=False,
)


class ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef(
    _ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef
):
    pass


_ClientListBackupPlanVersionsResponseTypeDef = TypedDict(
    "_ClientListBackupPlanVersionsResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanVersionsList": List[
            ClientListBackupPlanVersionsResponseBackupPlanVersionsListTypeDef
        ],
    },
    total=False,
)


class ClientListBackupPlanVersionsResponseTypeDef(_ClientListBackupPlanVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The next item following a partial list of returned items. For example, if a request is made
        to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
        your list starting at the location pointed to by the next token.
    """


_ClientListBackupPlansResponseBackupPlansListTypeDef = TypedDict(
    "_ClientListBackupPlansResponseBackupPlansListTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
    },
    total=False,
)


class ClientListBackupPlansResponseBackupPlansListTypeDef(
    _ClientListBackupPlansResponseBackupPlansListTypeDef
):
    pass


_ClientListBackupPlansResponseTypeDef = TypedDict(
    "_ClientListBackupPlansResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlansList": List[ClientListBackupPlansResponseBackupPlansListTypeDef],
    },
    total=False,
)


class ClientListBackupPlansResponseTypeDef(_ClientListBackupPlansResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The next item following a partial list of returned items. For example, if a request is made
        to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
        your list starting at the location pointed to by the next token.
    """


_ClientListBackupSelectionsResponseBackupSelectionsListTypeDef = TypedDict(
    "_ClientListBackupSelectionsResponseBackupSelectionsListTypeDef",
    {
        "SelectionId": str,
        "SelectionName": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "IamRoleArn": str,
    },
    total=False,
)


class ClientListBackupSelectionsResponseBackupSelectionsListTypeDef(
    _ClientListBackupSelectionsResponseBackupSelectionsListTypeDef
):
    pass


_ClientListBackupSelectionsResponseTypeDef = TypedDict(
    "_ClientListBackupSelectionsResponseTypeDef",
    {
        "NextToken": str,
        "BackupSelectionsList": List[ClientListBackupSelectionsResponseBackupSelectionsListTypeDef],
    },
    total=False,
)


class ClientListBackupSelectionsResponseTypeDef(_ClientListBackupSelectionsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The next item following a partial list of returned items. For example, if a request is made
        to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
        your list starting at the location pointed to by the next token.
    """


_ClientListBackupVaultsResponseBackupVaultListTypeDef = TypedDict(
    "_ClientListBackupVaultsResponseBackupVaultListTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)


class ClientListBackupVaultsResponseBackupVaultListTypeDef(
    _ClientListBackupVaultsResponseBackupVaultListTypeDef
):
    """
    - *(dict) --*

      Contains metadata about a backup vault.
      - **BackupVaultName** *(string) --*

        The name of a logical container where backups are stored. Backup vaults are identified by
        names that are unique to the account used to create them and the AWS Region where they are
        created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientListBackupVaultsResponseTypeDef = TypedDict(
    "_ClientListBackupVaultsResponseTypeDef",
    {
        "BackupVaultList": List[ClientListBackupVaultsResponseBackupVaultListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListBackupVaultsResponseTypeDef(_ClientListBackupVaultsResponseTypeDef):
    """
    - *(dict) --*

      - **BackupVaultList** *(list) --*

        An array of backup vault list members containing vault metadata, including Amazon Resource
        Name (ARN), display name, creation date, number of saved recovery points, and encryption
        information if the resources saved in the backup vault are encrypted.
        - *(dict) --*

          Contains metadata about a backup vault.
          - **BackupVaultName** *(string) --*

            The name of a logical container where backups are stored. Backup vaults are identified
            by names that are unique to the account used to create them and the AWS Region where
            they are created. They consist of lowercase letters, numbers, and hyphens.
    """


_ClientListProtectedResourcesResponseResultsTypeDef = TypedDict(
    "_ClientListProtectedResourcesResponseResultsTypeDef",
    {"ResourceArn": str, "ResourceType": str, "LastBackupTime": datetime},
    total=False,
)


class ClientListProtectedResourcesResponseResultsTypeDef(
    _ClientListProtectedResourcesResponseResultsTypeDef
):
    """
    - *(dict) --*

      A structure that contains information about a backed-up resource.
      - **ResourceArn** *(string) --*

        An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
        depends on the resource type.
    """


_ClientListProtectedResourcesResponseTypeDef = TypedDict(
    "_ClientListProtectedResourcesResponseTypeDef",
    {"Results": List[ClientListProtectedResourcesResponseResultsTypeDef], "NextToken": str},
    total=False,
)


class ClientListProtectedResourcesResponseTypeDef(_ClientListProtectedResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **Results** *(list) --*

        An array of resources successfully backed up by AWS Backup including the time the resource
        was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.
        - *(dict) --*

          A structure that contains information about a backed-up resource.
          - **ResourceArn** *(string) --*

            An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
            depends on the resource type.
    """


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef
):
    pass


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "BackupPlanVersion": str, "BackupRuleId": str},
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef
):
    pass


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef
):
    pass


_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCreatedByTypeDef,
        "IamRoleArn": str,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsCalculatedLifecycleTypeDef,
        "Lifecycle": ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsLifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": datetime,
    },
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef
):
    pass


_ClientListRecoveryPointsByBackupVaultResponseTypeDef = TypedDict(
    "_ClientListRecoveryPointsByBackupVaultResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[ClientListRecoveryPointsByBackupVaultResponseRecoveryPointsTypeDef],
    },
    total=False,
)


class ClientListRecoveryPointsByBackupVaultResponseTypeDef(
    _ClientListRecoveryPointsByBackupVaultResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The next item following a partial list of returned items. For example, if a request is made
        to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
        your list starting at the location pointed to by the next token.
    """


_ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef = TypedDict(
    "_ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef",
    {
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "Status": Literal["COMPLETED", "PARTIAL", "DELETING", "EXPIRED"],
        "EncryptionKeyArn": str,
        "BackupSizeBytes": int,
        "BackupVaultName": str,
    },
    total=False,
)


class ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef(
    _ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef
):
    pass


_ClientListRecoveryPointsByResourceResponseTypeDef = TypedDict(
    "_ClientListRecoveryPointsByResourceResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List[ClientListRecoveryPointsByResourceResponseRecoveryPointsTypeDef],
    },
    total=False,
)


class ClientListRecoveryPointsByResourceResponseTypeDef(
    _ClientListRecoveryPointsByResourceResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The next item following a partial list of returned items. For example, if a request is made
        to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
        your list starting at the location pointed to by the next token.
    """


_ClientListRestoreJobsResponseRestoreJobsTypeDef = TypedDict(
    "_ClientListRestoreJobsResponseRestoreJobsTypeDef",
    {
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": Literal["PENDING", "RUNNING", "COMPLETED", "ABORTED", "FAILED"],
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
    },
    total=False,
)


class ClientListRestoreJobsResponseRestoreJobsTypeDef(
    _ClientListRestoreJobsResponseRestoreJobsTypeDef
):
    """
    - *(dict) --*

      Contains metadata about a restore job.
      - **RestoreJobId** *(string) --*

        Uniquely identifies the job that restores a recovery point.
    """


_ClientListRestoreJobsResponseTypeDef = TypedDict(
    "_ClientListRestoreJobsResponseTypeDef",
    {"RestoreJobs": List[ClientListRestoreJobsResponseRestoreJobsTypeDef], "NextToken": str},
    total=False,
)


class ClientListRestoreJobsResponseTypeDef(_ClientListRestoreJobsResponseTypeDef):
    """
    - *(dict) --*

      - **RestoreJobs** *(list) --*

        An array of objects that contain detailed information about jobs to restore saved resources.
        - *(dict) --*

          Contains metadata about a restore job.
          - **RestoreJobId** *(string) --*

            Uniquely identifies the job that restores a recovery point.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef", {"NextToken": str, "Tags": Dict[str, str]}, total=False
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        The next item following a partial list of returned items. For example, if a request is made
        to return ``maxResults`` number of items, ``NextToken`` allows you to return more items in
        your list starting at the location pointed to by the next token.
    """


_ClientStartBackupJobLifecycleTypeDef = TypedDict(
    "_ClientStartBackupJobLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientStartBackupJobLifecycleTypeDef(_ClientStartBackupJobLifecycleTypeDef):
    """
    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup will transition and expire backups automatically according to the lifecycle
    that you define.
    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
    Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold
    after days” setting. The “transition to cold after days” setting cannot be changed after a
    backup has been transitioned to cold.
    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold storage.
    """


_ClientStartBackupJobResponseTypeDef = TypedDict(
    "_ClientStartBackupJobResponseTypeDef",
    {"BackupJobId": str, "RecoveryPointArn": str, "CreationDate": datetime},
    total=False,
)


class ClientStartBackupJobResponseTypeDef(_ClientStartBackupJobResponseTypeDef):
    """
    - *(dict) --*

      - **BackupJobId** *(string) --*

        Uniquely identifies a request to AWS Backup to back up a resource.
    """


_ClientStartRestoreJobResponseTypeDef = TypedDict(
    "_ClientStartRestoreJobResponseTypeDef", {"RestoreJobId": str}, total=False
)


class ClientStartRestoreJobResponseTypeDef(_ClientStartRestoreJobResponseTypeDef):
    """
    - *(dict) --*

      - **RestoreJobId** *(string) --*

        Uniquely identifies the job that restores a recovery point.
    """


_ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef = TypedDict(
    "_ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef(
    _ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef
):
    pass


_ClientUpdateBackupPlanBackupPlanRulesTypeDef = TypedDict(
    "_ClientUpdateBackupPlanBackupPlanRulesTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": ClientUpdateBackupPlanBackupPlanRulesLifecycleTypeDef,
        "RecoveryPointTags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateBackupPlanBackupPlanRulesTypeDef(_ClientUpdateBackupPlanBackupPlanRulesTypeDef):
    pass


_RequiredClientUpdateBackupPlanBackupPlanTypeDef = TypedDict(
    "_RequiredClientUpdateBackupPlanBackupPlanTypeDef", {"BackupPlanName": str}
)
_OptionalClientUpdateBackupPlanBackupPlanTypeDef = TypedDict(
    "_OptionalClientUpdateBackupPlanBackupPlanTypeDef",
    {"Rules": List[ClientUpdateBackupPlanBackupPlanRulesTypeDef]},
    total=False,
)


class ClientUpdateBackupPlanBackupPlanTypeDef(
    _RequiredClientUpdateBackupPlanBackupPlanTypeDef,
    _OptionalClientUpdateBackupPlanBackupPlanTypeDef,
):
    """
    Specifies the body of a backup plan. Includes a ``BackupPlanName`` and one or more sets of
    ``Rules`` .
    - **BackupPlanName** *(string) --***[REQUIRED]**

      The display name of a backup plan.
    """


_ClientUpdateBackupPlanResponseTypeDef = TypedDict(
    "_ClientUpdateBackupPlanResponseTypeDef",
    {"BackupPlanId": str, "BackupPlanArn": str, "CreationDate": datetime, "VersionId": str},
    total=False,
)


class ClientUpdateBackupPlanResponseTypeDef(_ClientUpdateBackupPlanResponseTypeDef):
    """
    - *(dict) --*

      - **BackupPlanId** *(string) --*

        Uniquely identifies a backup plan.
    """


_ClientUpdateRecoveryPointLifecycleLifecycleTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientUpdateRecoveryPointLifecycleLifecycleTypeDef(
    _ClientUpdateRecoveryPointLifecycleLifecycleTypeDef
):
    """
    The lifecycle defines when a protected resource is transitioned to cold storage and when it
    expires. AWS Backup transitions and expires backups automatically according to the lifecycle
    that you define.
    Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.
    Therefore, the “expire after days” setting must be 90 days greater than the “transition to cold
    after days” setting. The “transition to cold after days” setting cannot be changed after a
    backup has been transitioned to cold.
    - **MoveToColdStorageAfterDays** *(integer) --*

      Specifies the number of days after creation that a recovery point is moved to cold storage.
    """


_ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef",
    {"MoveToColdStorageAt": datetime, "DeleteAt": datetime},
    total=False,
)


class ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef(
    _ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef
):
    pass


_ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef",
    {"MoveToColdStorageAfterDays": int, "DeleteAfterDays": int},
    total=False,
)


class ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef(
    _ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef
):
    pass


_ClientUpdateRecoveryPointLifecycleResponseTypeDef = TypedDict(
    "_ClientUpdateRecoveryPointLifecycleResponseTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": ClientUpdateRecoveryPointLifecycleResponseLifecycleTypeDef,
        "CalculatedLifecycle": ClientUpdateRecoveryPointLifecycleResponseCalculatedLifecycleTypeDef,
    },
    total=False,
)


class ClientUpdateRecoveryPointLifecycleResponseTypeDef(
    _ClientUpdateRecoveryPointLifecycleResponseTypeDef
):
    """
    - *(dict) --*

      - **BackupVaultArn** *(string) --*

        An ARN that uniquely identifies a backup vault; for example,
        ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault`` .
    """
