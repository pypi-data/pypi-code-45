"Main interface for workspaces service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAuthorizeIpRulesUserRulesTypeDef",
    "ClientCopyWorkspaceImageResponseTypeDef",
    "ClientCopyWorkspaceImageTagsTypeDef",
    "ClientCreateIpGroupResponseTypeDef",
    "ClientCreateIpGroupTagsTypeDef",
    "ClientCreateIpGroupUserRulesTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsTypeDef",
    "ClientCreateWorkspacesResponseTypeDef",
    "ClientCreateWorkspacesWorkspacesTagsTypeDef",
    "ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesWorkspacesTypeDef",
    "ClientDescribeAccountModificationsResponseAccountModificationsTypeDef",
    "ClientDescribeAccountModificationsResponseTypeDef",
    "ClientDescribeAccountResponseTypeDef",
    "ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef",
    "ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef",
    "ClientDescribeClientPropertiesResponseTypeDef",
    "ClientDescribeIpGroupsResponseResultuserRulesTypeDef",
    "ClientDescribeIpGroupsResponseResultTypeDef",
    "ClientDescribeIpGroupsResponseTypeDef",
    "ClientDescribeTagsResponseTagListTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesTypeDef",
    "ClientDescribeWorkspaceBundlesResponseTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseTypeDef",
    "ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef",
    "ClientDescribeWorkspaceImagesResponseImagesTypeDef",
    "ClientDescribeWorkspaceImagesResponseTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseTypeDef",
    "ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef",
    "ClientDescribeWorkspacesConnectionStatusResponseTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesTypeDef",
    "ClientDescribeWorkspacesResponseTypeDef",
    "ClientImportWorkspaceImageResponseTypeDef",
    "ClientImportWorkspaceImageTagsTypeDef",
    "ClientListAvailableManagementCidrRangesResponseTypeDef",
    "ClientModifyClientPropertiesClientPropertiesTypeDef",
    "ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef",
    "ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef",
    "ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef",
    "ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef",
    "ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef",
    "ClientRebootWorkspacesResponseFailedRequestsTypeDef",
    "ClientRebootWorkspacesResponseTypeDef",
    "ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef",
    "ClientRebuildWorkspacesResponseFailedRequestsTypeDef",
    "ClientRebuildWorkspacesResponseTypeDef",
    "ClientRegisterWorkspaceDirectoryTagsTypeDef",
    "ClientStartWorkspacesResponseFailedRequestsTypeDef",
    "ClientStartWorkspacesResponseTypeDef",
    "ClientStartWorkspacesStartWorkspaceRequestsTypeDef",
    "ClientStopWorkspacesResponseFailedRequestsTypeDef",
    "ClientStopWorkspacesResponseTypeDef",
    "ClientStopWorkspacesStopWorkspaceRequestsTypeDef",
    "ClientTerminateWorkspacesResponseFailedRequestsTypeDef",
    "ClientTerminateWorkspacesResponseTypeDef",
    "ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef",
    "ClientUpdateRulesOfIpGroupUserRulesTypeDef",
    "DescribeAccountModificationsPaginatePaginationConfigTypeDef",
    "DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef",
    "DescribeAccountModificationsPaginateResponseTypeDef",
    "DescribeIpGroupsPaginatePaginationConfigTypeDef",
    "DescribeIpGroupsPaginateResponseResultuserRulesTypeDef",
    "DescribeIpGroupsPaginateResponseResultTypeDef",
    "DescribeIpGroupsPaginateResponseTypeDef",
    "DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseTypeDef",
    "DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseTypeDef",
    "DescribeWorkspaceImagesPaginatePaginationConfigTypeDef",
    "DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef",
    "DescribeWorkspaceImagesPaginateResponseImagesTypeDef",
    "DescribeWorkspaceImagesPaginateResponseTypeDef",
    "DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef",
    "DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef",
    "DescribeWorkspacesConnectionStatusPaginateResponseTypeDef",
    "DescribeWorkspacesPaginatePaginationConfigTypeDef",
    "DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef",
    "DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef",
    "DescribeWorkspacesPaginateResponseWorkspacesTypeDef",
    "DescribeWorkspacesPaginateResponseTypeDef",
    "ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef",
    "ListAvailableManagementCidrRangesPaginateResponseTypeDef",
)


_ClientAuthorizeIpRulesUserRulesTypeDef = TypedDict(
    "_ClientAuthorizeIpRulesUserRulesTypeDef", {"ipRule": str, "ruleDesc": str}, total=False
)


class ClientAuthorizeIpRulesUserRulesTypeDef(_ClientAuthorizeIpRulesUserRulesTypeDef):
    """
    - *(dict) --*

      Describes a rule for an IP access control group.
      - **ipRule** *(string) --*

        The IP address range, in CIDR notation.
    """


_ClientCopyWorkspaceImageResponseTypeDef = TypedDict(
    "_ClientCopyWorkspaceImageResponseTypeDef", {"ImageId": str}, total=False
)


class ClientCopyWorkspaceImageResponseTypeDef(_ClientCopyWorkspaceImageResponseTypeDef):
    """
    - *(dict) --*

      - **ImageId** *(string) --*

        The identifier of the image.
    """


_RequiredClientCopyWorkspaceImageTagsTypeDef = TypedDict(
    "_RequiredClientCopyWorkspaceImageTagsTypeDef", {"Key": str}
)
_OptionalClientCopyWorkspaceImageTagsTypeDef = TypedDict(
    "_OptionalClientCopyWorkspaceImageTagsTypeDef", {"Value": str}, total=False
)


class ClientCopyWorkspaceImageTagsTypeDef(
    _RequiredClientCopyWorkspaceImageTagsTypeDef, _OptionalClientCopyWorkspaceImageTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientCreateIpGroupResponseTypeDef = TypedDict(
    "_ClientCreateIpGroupResponseTypeDef", {"GroupId": str}, total=False
)


class ClientCreateIpGroupResponseTypeDef(_ClientCreateIpGroupResponseTypeDef):
    """
    - *(dict) --*

      - **GroupId** *(string) --*

        The identifier of the group.
    """


_RequiredClientCreateIpGroupTagsTypeDef = TypedDict(
    "_RequiredClientCreateIpGroupTagsTypeDef", {"Key": str}
)
_OptionalClientCreateIpGroupTagsTypeDef = TypedDict(
    "_OptionalClientCreateIpGroupTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateIpGroupTagsTypeDef(
    _RequiredClientCreateIpGroupTagsTypeDef, _OptionalClientCreateIpGroupTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientCreateIpGroupUserRulesTypeDef = TypedDict(
    "_ClientCreateIpGroupUserRulesTypeDef", {"ipRule": str, "ruleDesc": str}, total=False
)


class ClientCreateIpGroupUserRulesTypeDef(_ClientCreateIpGroupUserRulesTypeDef):
    """
    - *(dict) --*

      Describes a rule for an IP access control group.
      - **ipRule** *(string) --*

        The IP address range, in CIDR notation.
    """


_RequiredClientCreateTagsTagsTypeDef = TypedDict(
    "_RequiredClientCreateTagsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTagsTagsTypeDef = TypedDict(
    "_OptionalClientCreateTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(
    _RequiredClientCreateTagsTagsTypeDef, _OptionalClientCreateTagsTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef
):
    pass


_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef
):
    pass


_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef,
        "Tags": List[ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef],
    },
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef
):
    """
    - **WorkspaceRequest** *(dict) --*

      Information about the WorkSpace.
      - **DirectoryId** *(string) --*

        The identifier of the AWS Directory Service directory for the WorkSpace. You can use
        DescribeWorkspaceDirectories to list the available directories.
    """


_ClientCreateWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsTypeDef",
    {
        "WorkspaceRequest": ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace that cannot be created.
      - **WorkspaceRequest** *(dict) --*

        Information about the WorkSpace.
        - **DirectoryId** *(string) --*

          The identifier of the AWS Directory Service directory for the WorkSpace. You can use
          DescribeWorkspaceDirectories to list the available directories.
    """


_ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef",
    {
        "Resource": Literal["ROOT_VOLUME", "USER_VOLUME", "COMPUTE_TYPE"],
        "State": Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"],
    },
    total=False,
)


class ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef(
    _ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef
):
    pass


_ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)


class ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef(
    _ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef
):
    pass


_ClientCreateWorkspacesResponsePendingRequestsTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponsePendingRequestsTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": Literal[
            "PENDING",
            "AVAILABLE",
            "IMPAIRED",
            "UNHEALTHY",
            "REBOOTING",
            "STARTING",
            "REBUILDING",
            "RESTORING",
            "MAINTENANCE",
            "ADMIN_MAINTENANCE",
            "TERMINATING",
            "TERMINATED",
            "SUSPENDED",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
        ],
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef
        ],
    },
    total=False,
)


class ClientCreateWorkspacesResponsePendingRequestsTypeDef(
    _ClientCreateWorkspacesResponsePendingRequestsTypeDef
):
    pass


_ClientCreateWorkspacesResponseTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseTypeDef",
    {
        "FailedRequests": List[ClientCreateWorkspacesResponseFailedRequestsTypeDef],
        "PendingRequests": List[ClientCreateWorkspacesResponsePendingRequestsTypeDef],
    },
    total=False,
)


class ClientCreateWorkspacesResponseTypeDef(_ClientCreateWorkspacesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedRequests** *(list) --*

        Information about the WorkSpaces that could not be created.
        - *(dict) --*

          Describes a WorkSpace that cannot be created.
          - **WorkspaceRequest** *(dict) --*

            Information about the WorkSpace.
            - **DirectoryId** *(string) --*

              The identifier of the AWS Directory Service directory for the WorkSpace. You can use
              DescribeWorkspaceDirectories to list the available directories.
    """


_ClientCreateWorkspacesWorkspacesTagsTypeDef = TypedDict(
    "_ClientCreateWorkspacesWorkspacesTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateWorkspacesWorkspacesTagsTypeDef(_ClientCreateWorkspacesWorkspacesTagsTypeDef):
    pass


_ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "_ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)


class ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef(
    _ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef
):
    pass


_RequiredClientCreateWorkspacesWorkspacesTypeDef = TypedDict(
    "_RequiredClientCreateWorkspacesWorkspacesTypeDef", {"DirectoryId": str}
)
_OptionalClientCreateWorkspacesWorkspacesTypeDef = TypedDict(
    "_OptionalClientCreateWorkspacesWorkspacesTypeDef",
    {
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef,
        "Tags": List[ClientCreateWorkspacesWorkspacesTagsTypeDef],
    },
    total=False,
)


class ClientCreateWorkspacesWorkspacesTypeDef(
    _RequiredClientCreateWorkspacesWorkspacesTypeDef,
    _OptionalClientCreateWorkspacesWorkspacesTypeDef,
):
    """
    - *(dict) --*

      Describes the information used to create a WorkSpace.
      - **DirectoryId** *(string) --***[REQUIRED]**

        The identifier of the AWS Directory Service directory for the WorkSpace. You can use
        DescribeWorkspaceDirectories to list the available directories.
    """


_ClientDescribeAccountModificationsResponseAccountModificationsTypeDef = TypedDict(
    "_ClientDescribeAccountModificationsResponseAccountModificationsTypeDef",
    {
        "ModificationState": Literal["PENDING", "COMPLETED", "FAILED"],
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeAccountModificationsResponseAccountModificationsTypeDef(
    _ClientDescribeAccountModificationsResponseAccountModificationsTypeDef
):
    """
    - *(dict) --*

      Describes a modification to the configuration of Bring Your Own License (BYOL) for the
      specified account.
      - **ModificationState** *(string) --*

        The state of the modification to the configuration of BYOL.
    """


_ClientDescribeAccountModificationsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountModificationsResponseTypeDef",
    {
        "AccountModifications": List[
            ClientDescribeAccountModificationsResponseAccountModificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAccountModificationsResponseTypeDef(
    _ClientDescribeAccountModificationsResponseTypeDef
):
    """
    - *(dict) --*

      - **AccountModifications** *(list) --*

        The list of modifications to the configuration of BYOL.
        - *(dict) --*

          Describes a modification to the configuration of Bring Your Own License (BYOL) for the
          specified account.
          - **ModificationState** *(string) --*

            The state of the modification to the configuration of BYOL.
    """


_ClientDescribeAccountResponseTypeDef = TypedDict(
    "_ClientDescribeAccountResponseTypeDef",
    {
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
    },
    total=False,
)


class ClientDescribeAccountResponseTypeDef(_ClientDescribeAccountResponseTypeDef):
    """
    - *(dict) --*

      - **DedicatedTenancySupport** *(string) --*

        The status of BYOL (whether BYOL is enabled or disabled).
    """


_ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef = TypedDict(
    "_ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef",
    {"ReconnectEnabled": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef(
    _ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef
):
    pass


_ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef = TypedDict(
    "_ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef,
    },
    total=False,
)


class ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef(
    _ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef
):
    """
    - *(dict) --*

      Information about the Amazon WorkSpaces client.
      - **ResourceId** *(string) --*

        The resource identifier, in the form of a directory ID.
    """


_ClientDescribeClientPropertiesResponseTypeDef = TypedDict(
    "_ClientDescribeClientPropertiesResponseTypeDef",
    {
        "ClientPropertiesList": List[
            ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeClientPropertiesResponseTypeDef(_ClientDescribeClientPropertiesResponseTypeDef):
    """
    - *(dict) --*

      - **ClientPropertiesList** *(list) --*

        Information about the specified Amazon WorkSpaces clients.
        - *(dict) --*

          Information about the Amazon WorkSpaces client.
          - **ResourceId** *(string) --*

            The resource identifier, in the form of a directory ID.
    """


_ClientDescribeIpGroupsResponseResultuserRulesTypeDef = TypedDict(
    "_ClientDescribeIpGroupsResponseResultuserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)


class ClientDescribeIpGroupsResponseResultuserRulesTypeDef(
    _ClientDescribeIpGroupsResponseResultuserRulesTypeDef
):
    pass


_ClientDescribeIpGroupsResponseResultTypeDef = TypedDict(
    "_ClientDescribeIpGroupsResponseResultTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "groupDesc": str,
        "userRules": List[ClientDescribeIpGroupsResponseResultuserRulesTypeDef],
    },
    total=False,
)


class ClientDescribeIpGroupsResponseResultTypeDef(_ClientDescribeIpGroupsResponseResultTypeDef):
    """
    - *(dict) --*

      Describes an IP access control group.
      - **groupId** *(string) --*

        The identifier of the group.
    """


_ClientDescribeIpGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeIpGroupsResponseTypeDef",
    {"Result": List[ClientDescribeIpGroupsResponseResultTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeIpGroupsResponseTypeDef(_ClientDescribeIpGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **Result** *(list) --*

        Information about the IP access control groups.
        - *(dict) --*

          Describes an IP access control group.
          - **groupId** *(string) --*

            The identifier of the group.
    """


_ClientDescribeTagsResponseTagListTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTagListTypeDef(_ClientDescribeTagsResponseTagListTypeDef):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"TagList": List[ClientDescribeTagsResponseTagListTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      - **TagList** *(list) --*

        The tags.
        - *(dict) --*

          Describes a tag.
          - **Key** *(string) --*

            The key of the tag.
    """


_ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef",
    {
        "Name": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ]
    },
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef
):
    pass


_ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef
):
    pass


_ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef
):
    pass


_ClientDescribeWorkspaceBundlesResponseBundlesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "ImageId": str,
        "RootStorage": ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef,
        "UserStorage": ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef,
        "ComputeType": ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace bundle.
      - **BundleId** *(string) --*

        The bundle identifier.
    """


_ClientDescribeWorkspaceBundlesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseTypeDef",
    {"Bundles": List[ClientDescribeWorkspaceBundlesResponseBundlesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseTypeDef(_ClientDescribeWorkspaceBundlesResponseTypeDef):
    """
    - *(dict) --*

      - **Bundles** *(list) --*

        Information about the bundles.
        - *(dict) --*

          Describes a WorkSpace bundle.
          - **BundleId** *(string) --*

            The bundle identifier.
    """


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": Literal["ENABLED", "DISABLED"],
        "IncreaseVolumeSize": Literal["ENABLED", "DISABLED"],
        "ChangeComputeType": Literal["ENABLED", "DISABLED"],
        "SwitchRunningMode": Literal["ENABLED", "DISABLED"],
        "RebuildWorkspace": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef
):
    pass


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": Literal["ALLOW", "DENY"],
        "DeviceTypeOsx": Literal["ALLOW", "DENY"],
        "DeviceTypeWeb": Literal["ALLOW", "DENY"],
        "DeviceTypeIos": Literal["ALLOW", "DENY"],
        "DeviceTypeAndroid": Literal["ALLOW", "DENY"],
        "DeviceTypeChromeOs": Literal["ALLOW", "DENY"],
        "DeviceTypeZeroClient": Literal["ALLOW", "DENY"],
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef
):
    pass


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef
):
    pass


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": Literal["SIMPLE_AD", "AD_CONNECTOR"],
        "WorkspaceSecurityGroupId": str,
        "State": Literal["REGISTERING", "REGISTERED", "DEREGISTERING", "DEREGISTERED", "ERROR"],
        "WorkspaceCreationProperties": ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef,
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef,
        "Tenancy": Literal["DEDICATED", "SHARED"],
        "SelfservicePermissions": ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef
):
    """
    - *(dict) --*

      Describes a directory that is used with Amazon WorkSpaces.
      - **DirectoryId** *(string) --*

        The directory identifier.
    """


_ClientDescribeWorkspaceDirectoriesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseTypeDef",
    {
        "Directories": List[ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseTypeDef
):
    """
    - *(dict) --*

      - **Directories** *(list) --*

        Information about the directories.
        - *(dict) --*

          Describes a directory that is used with Amazon WorkSpaces.
          - **DirectoryId** *(string) --*

            The directory identifier.
    """


_ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef = TypedDict(
    "_ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef",
    {"Type": Literal["WINDOWS", "LINUX"]},
    total=False,
)


class ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef(
    _ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef
):
    pass


_ClientDescribeWorkspaceImagesResponseImagesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceImagesResponseImagesTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef,
        "State": Literal["AVAILABLE", "PENDING", "ERROR"],
        "RequiredTenancy": Literal["DEFAULT", "DEDICATED"],
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeWorkspaceImagesResponseImagesTypeDef(
    _ClientDescribeWorkspaceImagesResponseImagesTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace image.
      - **ImageId** *(string) --*

        The identifier of the image.
    """


_ClientDescribeWorkspaceImagesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceImagesResponseTypeDef",
    {"Images": List[ClientDescribeWorkspaceImagesResponseImagesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeWorkspaceImagesResponseTypeDef(_ClientDescribeWorkspaceImagesResponseTypeDef):
    """
    - *(dict) --*

      - **Images** *(list) --*

        Information about the images.
        - *(dict) --*

          Describes a WorkSpace image.
          - **ImageId** *(string) --*

            The identifier of the image.
    """


_ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef = TypedDict(
    "_ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef",
    {"SnapshotTime": datetime},
    total=False,
)


class ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef(
    _ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a snapshot.
      - **SnapshotTime** *(datetime) --*

        The time when the snapshot was created.
    """


_ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef = TypedDict(
    "_ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef",
    {"SnapshotTime": datetime},
    total=False,
)


class ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef(
    _ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef
):
    pass


_ClientDescribeWorkspaceSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceSnapshotsResponseTypeDef",
    {
        "RebuildSnapshots": List[ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef],
        "RestoreSnapshots": List[ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef],
    },
    total=False,
)


class ClientDescribeWorkspaceSnapshotsResponseTypeDef(
    _ClientDescribeWorkspaceSnapshotsResponseTypeDef
):
    """
    - *(dict) --*

      - **RebuildSnapshots** *(list) --*

        Information about the snapshots that can be used to rebuild a WorkSpace. These snapshots
        include the user volume.
        - *(dict) --*

          Describes a snapshot.
          - **SnapshotTime** *(datetime) --*

            The time when the snapshot was created.
    """


_ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef = TypedDict(
    "_ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"],
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef(
    _ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef
):
    """
    - *(dict) --*

      Describes the connection status of a WorkSpace.
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientDescribeWorkspacesConnectionStatusResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspacesConnectionStatusResponseTypeDef",
    {
        "WorkspacesConnectionStatus": List[
            ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeWorkspacesConnectionStatusResponseTypeDef(
    _ClientDescribeWorkspacesConnectionStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **WorkspacesConnectionStatus** *(list) --*

        Information about the connection status of the WorkSpace.
        - *(dict) --*

          Describes the connection status of a WorkSpace.
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef",
    {
        "Resource": Literal["ROOT_VOLUME", "USER_VOLUME", "COMPUTE_TYPE"],
        "State": Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"],
    },
    total=False,
)


class ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef(
    _ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef
):
    pass


_ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)


class ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef(
    _ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef
):
    pass


_ClientDescribeWorkspacesResponseWorkspacesTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseWorkspacesTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": Literal[
            "PENDING",
            "AVAILABLE",
            "IMPAIRED",
            "UNHEALTHY",
            "REBOOTING",
            "STARTING",
            "REBUILDING",
            "RESTORING",
            "MAINTENANCE",
            "ADMIN_MAINTENANCE",
            "TERMINATING",
            "TERMINATED",
            "SUSPENDED",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
        ],
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeWorkspacesResponseWorkspacesTypeDef(
    _ClientDescribeWorkspacesResponseWorkspacesTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace.
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientDescribeWorkspacesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseTypeDef",
    {"Workspaces": List[ClientDescribeWorkspacesResponseWorkspacesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeWorkspacesResponseTypeDef(_ClientDescribeWorkspacesResponseTypeDef):
    """
    - *(dict) --*

      - **Workspaces** *(list) --*

        Information about the WorkSpaces.
        Because  CreateWorkspaces is an asynchronous operation, some of the returned information
        could be incomplete.
        - *(dict) --*

          Describes a WorkSpace.
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_ClientImportWorkspaceImageResponseTypeDef = TypedDict(
    "_ClientImportWorkspaceImageResponseTypeDef", {"ImageId": str}, total=False
)


class ClientImportWorkspaceImageResponseTypeDef(_ClientImportWorkspaceImageResponseTypeDef):
    """
    - *(dict) --*

      - **ImageId** *(string) --*

        The identifier of the WorkSpace image.
    """


_RequiredClientImportWorkspaceImageTagsTypeDef = TypedDict(
    "_RequiredClientImportWorkspaceImageTagsTypeDef", {"Key": str}
)
_OptionalClientImportWorkspaceImageTagsTypeDef = TypedDict(
    "_OptionalClientImportWorkspaceImageTagsTypeDef", {"Value": str}, total=False
)


class ClientImportWorkspaceImageTagsTypeDef(
    _RequiredClientImportWorkspaceImageTagsTypeDef, _OptionalClientImportWorkspaceImageTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientListAvailableManagementCidrRangesResponseTypeDef = TypedDict(
    "_ClientListAvailableManagementCidrRangesResponseTypeDef",
    {"ManagementCidrRanges": List[str], "NextToken": str},
    total=False,
)


class ClientListAvailableManagementCidrRangesResponseTypeDef(
    _ClientListAvailableManagementCidrRangesResponseTypeDef
):
    """
    - *(dict) --*

      - **ManagementCidrRanges** *(list) --*

        The list of available IP address ranges, specified as IPv4 CIDR blocks.
        - *(string) --*
    """


_ClientModifyClientPropertiesClientPropertiesTypeDef = TypedDict(
    "_ClientModifyClientPropertiesClientPropertiesTypeDef",
    {"ReconnectEnabled": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientModifyClientPropertiesClientPropertiesTypeDef(
    _ClientModifyClientPropertiesClientPropertiesTypeDef
):
    """
    Information about the Amazon WorkSpaces client.
    - **ReconnectEnabled** *(string) --*

      Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When
      enabled, users can choose to reconnect to their WorkSpaces without re-entering their
      credentials.
    """


_ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef = TypedDict(
    "_ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": Literal["ENABLED", "DISABLED"],
        "IncreaseVolumeSize": Literal["ENABLED", "DISABLED"],
        "ChangeComputeType": Literal["ENABLED", "DISABLED"],
        "SwitchRunningMode": Literal["ENABLED", "DISABLED"],
        "RebuildWorkspace": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef(
    _ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef
):
    """
    The permissions to enable or disable self-service capabilities.
    - **RestartWorkspace** *(string) --*

      Specifies whether users can restart their WorkSpace.
    """


_ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "_ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": Literal["ALLOW", "DENY"],
        "DeviceTypeOsx": Literal["ALLOW", "DENY"],
        "DeviceTypeWeb": Literal["ALLOW", "DENY"],
        "DeviceTypeIos": Literal["ALLOW", "DENY"],
        "DeviceTypeAndroid": Literal["ALLOW", "DENY"],
        "DeviceTypeChromeOs": Literal["ALLOW", "DENY"],
        "DeviceTypeZeroClient": Literal["ALLOW", "DENY"],
    },
    total=False,
)


class ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef(
    _ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef
):
    """
    The device types and operating systems to enable or disable for access.
    - **DeviceTypeWindows** *(string) --*

      Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
      WorkSpaces access to trusted devices (also known as managed devices) with valid certificates,
      specify a value of ``TRUST`` . For more information, see `Restrict WorkSpaces Access to
      Trusted Devices
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .
    """


_ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "_ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)


class ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef(
    _ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef
):
    """
    The default properties for creating WorkSpaces.
    - **EnableInternetAccess** *(boolean) --*

      Indicates whether internet access is enabled for your WorkSpaces.
    """


_ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef = TypedDict(
    "_ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)


class ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef(
    _ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef
):
    """
    The properties of the WorkSpace.
    - **RunningMode** *(string) --*

      The running mode. For more information, see `Manage the WorkSpace Running Mode
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .
    """


_ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef = TypedDict(
    "_ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)


class ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef(
    _ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef
):
    """
    - *(dict) --*

      Describes the information used to reboot a WorkSpace.
      - **WorkspaceId** *(string) --***[REQUIRED]**

        The identifier of the WorkSpace.
    """


_ClientRebootWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientRebootWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientRebootWorkspacesResponseFailedRequestsTypeDef(
    _ClientRebootWorkspacesResponseFailedRequestsTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
      RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
      started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientRebootWorkspacesResponseTypeDef = TypedDict(
    "_ClientRebootWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientRebootWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientRebootWorkspacesResponseTypeDef(_ClientRebootWorkspacesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedRequests** *(list) --*

        Information about the WorkSpaces that could not be rebooted.
        - *(dict) --*

          Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
          RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
          started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef = TypedDict(
    "_ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)


class ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef(
    _ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef
):
    """
    - *(dict) --*

      Describes the information used to rebuild a WorkSpace.
      - **WorkspaceId** *(string) --***[REQUIRED]**

        The identifier of the WorkSpace.
    """


_ClientRebuildWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientRebuildWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientRebuildWorkspacesResponseFailedRequestsTypeDef(
    _ClientRebuildWorkspacesResponseFailedRequestsTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
      RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
      started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientRebuildWorkspacesResponseTypeDef = TypedDict(
    "_ClientRebuildWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientRebuildWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientRebuildWorkspacesResponseTypeDef(_ClientRebuildWorkspacesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedRequests** *(list) --*

        Information about the WorkSpace that could not be rebuilt.
        - *(dict) --*

          Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
          RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
          started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_RequiredClientRegisterWorkspaceDirectoryTagsTypeDef = TypedDict(
    "_RequiredClientRegisterWorkspaceDirectoryTagsTypeDef", {"Key": str}
)
_OptionalClientRegisterWorkspaceDirectoryTagsTypeDef = TypedDict(
    "_OptionalClientRegisterWorkspaceDirectoryTagsTypeDef", {"Value": str}, total=False
)


class ClientRegisterWorkspaceDirectoryTagsTypeDef(
    _RequiredClientRegisterWorkspaceDirectoryTagsTypeDef,
    _OptionalClientRegisterWorkspaceDirectoryTagsTypeDef,
):
    """
    - *(dict) --*

      Describes a tag.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientStartWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientStartWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientStartWorkspacesResponseFailedRequestsTypeDef(
    _ClientStartWorkspacesResponseFailedRequestsTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
      RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
      started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientStartWorkspacesResponseTypeDef = TypedDict(
    "_ClientStartWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientStartWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientStartWorkspacesResponseTypeDef(_ClientStartWorkspacesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedRequests** *(list) --*

        Information about the WorkSpaces that could not be started.
        - *(dict) --*

          Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
          RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
          started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_ClientStartWorkspacesStartWorkspaceRequestsTypeDef = TypedDict(
    "_ClientStartWorkspacesStartWorkspaceRequestsTypeDef", {"WorkspaceId": str}, total=False
)


class ClientStartWorkspacesStartWorkspaceRequestsTypeDef(
    _ClientStartWorkspacesStartWorkspaceRequestsTypeDef
):
    """
    - *(dict) --*

      Information used to start a WorkSpace.
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientStopWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientStopWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientStopWorkspacesResponseFailedRequestsTypeDef(
    _ClientStopWorkspacesResponseFailedRequestsTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
      RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
      started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientStopWorkspacesResponseTypeDef = TypedDict(
    "_ClientStopWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientStopWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientStopWorkspacesResponseTypeDef(_ClientStopWorkspacesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedRequests** *(list) --*

        Information about the WorkSpaces that could not be stopped.
        - *(dict) --*

          Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
          RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
          started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_ClientStopWorkspacesStopWorkspaceRequestsTypeDef = TypedDict(
    "_ClientStopWorkspacesStopWorkspaceRequestsTypeDef", {"WorkspaceId": str}, total=False
)


class ClientStopWorkspacesStopWorkspaceRequestsTypeDef(
    _ClientStopWorkspacesStopWorkspaceRequestsTypeDef
):
    """
    - *(dict) --*

      Describes the information used to stop a WorkSpace.
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientTerminateWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientTerminateWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientTerminateWorkspacesResponseFailedRequestsTypeDef(
    _ClientTerminateWorkspacesResponseFailedRequestsTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
      RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
      started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_ClientTerminateWorkspacesResponseTypeDef = TypedDict(
    "_ClientTerminateWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientTerminateWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientTerminateWorkspacesResponseTypeDef(_ClientTerminateWorkspacesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedRequests** *(list) --*

        Information about the WorkSpaces that could not be terminated.
        - *(dict) --*

          Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
          RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
          started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef = TypedDict(
    "_ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)


class ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef(
    _ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef
):
    """
    - *(dict) --*

      Describes the information used to terminate a WorkSpace.
      - **WorkspaceId** *(string) --***[REQUIRED]**

        The identifier of the WorkSpace.
    """


_ClientUpdateRulesOfIpGroupUserRulesTypeDef = TypedDict(
    "_ClientUpdateRulesOfIpGroupUserRulesTypeDef", {"ipRule": str, "ruleDesc": str}, total=False
)


class ClientUpdateRulesOfIpGroupUserRulesTypeDef(_ClientUpdateRulesOfIpGroupUserRulesTypeDef):
    """
    - *(dict) --*

      Describes a rule for an IP access control group.
      - **ipRule** *(string) --*

        The IP address range, in CIDR notation.
    """


_DescribeAccountModificationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAccountModificationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeAccountModificationsPaginatePaginationConfigTypeDef(
    _DescribeAccountModificationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef = TypedDict(
    "_DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef",
    {
        "ModificationState": Literal["PENDING", "COMPLETED", "FAILED"],
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef(
    _DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef
):
    """
    - *(dict) --*

      Describes a modification to the configuration of Bring Your Own License (BYOL) for the
      specified account.
      - **ModificationState** *(string) --*

        The state of the modification to the configuration of BYOL.
    """


_DescribeAccountModificationsPaginateResponseTypeDef = TypedDict(
    "_DescribeAccountModificationsPaginateResponseTypeDef",
    {
        "AccountModifications": List[
            DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef
        ]
    },
    total=False,
)


class DescribeAccountModificationsPaginateResponseTypeDef(
    _DescribeAccountModificationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **AccountModifications** *(list) --*

        The list of modifications to the configuration of BYOL.
        - *(dict) --*

          Describes a modification to the configuration of Bring Your Own License (BYOL) for the
          specified account.
          - **ModificationState** *(string) --*

            The state of the modification to the configuration of BYOL.
    """


_DescribeIpGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeIpGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeIpGroupsPaginatePaginationConfigTypeDef(
    _DescribeIpGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeIpGroupsPaginateResponseResultuserRulesTypeDef = TypedDict(
    "_DescribeIpGroupsPaginateResponseResultuserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)


class DescribeIpGroupsPaginateResponseResultuserRulesTypeDef(
    _DescribeIpGroupsPaginateResponseResultuserRulesTypeDef
):
    pass


_DescribeIpGroupsPaginateResponseResultTypeDef = TypedDict(
    "_DescribeIpGroupsPaginateResponseResultTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "groupDesc": str,
        "userRules": List[DescribeIpGroupsPaginateResponseResultuserRulesTypeDef],
    },
    total=False,
)


class DescribeIpGroupsPaginateResponseResultTypeDef(_DescribeIpGroupsPaginateResponseResultTypeDef):
    """
    - *(dict) --*

      Describes an IP access control group.
      - **groupId** *(string) --*

        The identifier of the group.
    """


_DescribeIpGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeIpGroupsPaginateResponseTypeDef",
    {"Result": List[DescribeIpGroupsPaginateResponseResultTypeDef]},
    total=False,
)


class DescribeIpGroupsPaginateResponseTypeDef(_DescribeIpGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Result** *(list) --*

        Information about the IP access control groups.
        - *(dict) --*

          Describes an IP access control group.
          - **groupId** *(string) --*

            The identifier of the group.
    """


_DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef(
    _DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef",
    {
        "Name": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ]
    },
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef
):
    pass


_DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef
):
    pass


_DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef
):
    pass


_DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "ImageId": str,
        "RootStorage": DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef,
        "UserStorage": DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef,
        "ComputeType": DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace bundle.
      - **BundleId** *(string) --*

        The bundle identifier.
    """


_DescribeWorkspaceBundlesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseTypeDef",
    {"Bundles": List[DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef]},
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Bundles** *(list) --*

        Information about the bundles.
        - *(dict) --*

          Describes a WorkSpace bundle.
          - **BundleId** *(string) --*

            The bundle identifier.
    """


_DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef(
    _DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": Literal["ENABLED", "DISABLED"],
        "IncreaseVolumeSize": Literal["ENABLED", "DISABLED"],
        "ChangeComputeType": Literal["ENABLED", "DISABLED"],
        "SwitchRunningMode": Literal["ENABLED", "DISABLED"],
        "RebuildWorkspace": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef
):
    pass


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": Literal["ALLOW", "DENY"],
        "DeviceTypeOsx": Literal["ALLOW", "DENY"],
        "DeviceTypeWeb": Literal["ALLOW", "DENY"],
        "DeviceTypeIos": Literal["ALLOW", "DENY"],
        "DeviceTypeAndroid": Literal["ALLOW", "DENY"],
        "DeviceTypeChromeOs": Literal["ALLOW", "DENY"],
        "DeviceTypeZeroClient": Literal["ALLOW", "DENY"],
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef
):
    pass


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef
):
    pass


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": Literal["SIMPLE_AD", "AD_CONNECTOR"],
        "WorkspaceSecurityGroupId": str,
        "State": Literal["REGISTERING", "REGISTERED", "DEREGISTERING", "DEREGISTERED", "ERROR"],
        "WorkspaceCreationProperties": DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef,
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef,
        "Tenancy": Literal["DEDICATED", "SHARED"],
        "SelfservicePermissions": DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef,
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef
):
    """
    - *(dict) --*

      Describes a directory that is used with Amazon WorkSpaces.
      - **DirectoryId** *(string) --*

        The directory identifier.
    """


_DescribeWorkspaceDirectoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseTypeDef",
    {"Directories": List[DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef]},
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Directories** *(list) --*

        Information about the directories.
        - *(dict) --*

          Describes a directory that is used with Amazon WorkSpaces.
          - **DirectoryId** *(string) --*

            The directory identifier.
    """


_DescribeWorkspaceImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspaceImagesPaginatePaginationConfigTypeDef(
    _DescribeWorkspaceImagesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef",
    {"Type": Literal["WINDOWS", "LINUX"]},
    total=False,
)


class DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef(
    _DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef
):
    pass


_DescribeWorkspaceImagesPaginateResponseImagesTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginateResponseImagesTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef,
        "State": Literal["AVAILABLE", "PENDING", "ERROR"],
        "RequiredTenancy": Literal["DEFAULT", "DEDICATED"],
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class DescribeWorkspaceImagesPaginateResponseImagesTypeDef(
    _DescribeWorkspaceImagesPaginateResponseImagesTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace image.
      - **ImageId** *(string) --*

        The identifier of the image.
    """


_DescribeWorkspaceImagesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginateResponseTypeDef",
    {"Images": List[DescribeWorkspaceImagesPaginateResponseImagesTypeDef]},
    total=False,
)


class DescribeWorkspaceImagesPaginateResponseTypeDef(
    _DescribeWorkspaceImagesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Images** *(list) --*

        Information about the images.
        - *(dict) --*

          Describes a WorkSpace image.
          - **ImageId** *(string) --*

            The identifier of the image.
    """


_DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef(
    _DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef = TypedDict(
    "_DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"],
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)


class DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef(
    _DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef
):
    """
    - *(dict) --*

      Describes the connection status of a WorkSpace.
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_DescribeWorkspacesConnectionStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspacesConnectionStatusPaginateResponseTypeDef",
    {
        "WorkspacesConnectionStatus": List[
            DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef
        ]
    },
    total=False,
)


class DescribeWorkspacesConnectionStatusPaginateResponseTypeDef(
    _DescribeWorkspacesConnectionStatusPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **WorkspacesConnectionStatus** *(list) --*

        Information about the connection status of the WorkSpace.
        - *(dict) --*

          Describes the connection status of a WorkSpace.
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_DescribeWorkspacesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspacesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspacesPaginatePaginationConfigTypeDef(
    _DescribeWorkspacesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef",
    {
        "Resource": Literal["ROOT_VOLUME", "USER_VOLUME", "COMPUTE_TYPE"],
        "State": Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"],
    },
    total=False,
)


class DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef(
    _DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef
):
    pass


_DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)


class DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef(
    _DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef
):
    pass


_DescribeWorkspacesPaginateResponseWorkspacesTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseWorkspacesTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": Literal[
            "PENDING",
            "AVAILABLE",
            "IMPAIRED",
            "UNHEALTHY",
            "REBOOTING",
            "STARTING",
            "REBUILDING",
            "RESTORING",
            "MAINTENANCE",
            "ADMIN_MAINTENANCE",
            "TERMINATING",
            "TERMINATED",
            "SUSPENDED",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
        ],
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef
        ],
    },
    total=False,
)


class DescribeWorkspacesPaginateResponseWorkspacesTypeDef(
    _DescribeWorkspacesPaginateResponseWorkspacesTypeDef
):
    """
    - *(dict) --*

      Describes a WorkSpace.
      - **WorkspaceId** *(string) --*

        The identifier of the WorkSpace.
    """


_DescribeWorkspacesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseTypeDef",
    {"Workspaces": List[DescribeWorkspacesPaginateResponseWorkspacesTypeDef]},
    total=False,
)


class DescribeWorkspacesPaginateResponseTypeDef(_DescribeWorkspacesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Workspaces** *(list) --*

        Information about the WorkSpaces.
        Because  CreateWorkspaces is an asynchronous operation, some of the returned information
        could be incomplete.
        - *(dict) --*

          Describes a WorkSpace.
          - **WorkspaceId** *(string) --*

            The identifier of the WorkSpace.
    """


_ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef(
    _ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAvailableManagementCidrRangesPaginateResponseTypeDef = TypedDict(
    "_ListAvailableManagementCidrRangesPaginateResponseTypeDef",
    {"ManagementCidrRanges": List[str]},
    total=False,
)


class ListAvailableManagementCidrRangesPaginateResponseTypeDef(
    _ListAvailableManagementCidrRangesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ManagementCidrRanges** *(list) --*

        The list of available IP address ranges, specified as IPv4 CIDR blocks.
        - *(string) --*
    """
