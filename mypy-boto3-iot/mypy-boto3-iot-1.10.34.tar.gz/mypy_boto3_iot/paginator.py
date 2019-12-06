"Main interface for iot service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot.type_defs import (
    ListActiveViolationsPaginatePaginationConfigTypeDef,
    ListActiveViolationsPaginateResponseTypeDef,
    ListAttachedPoliciesPaginatePaginationConfigTypeDef,
    ListAttachedPoliciesPaginateResponseTypeDef,
    ListAuditFindingsPaginatePaginationConfigTypeDef,
    ListAuditFindingsPaginateResourceIdentifierTypeDef,
    ListAuditFindingsPaginateResponseTypeDef,
    ListAuditTasksPaginatePaginationConfigTypeDef,
    ListAuditTasksPaginateResponseTypeDef,
    ListAuthorizersPaginatePaginationConfigTypeDef,
    ListAuthorizersPaginateResponseTypeDef,
    ListBillingGroupsPaginatePaginationConfigTypeDef,
    ListBillingGroupsPaginateResponseTypeDef,
    ListCACertificatesPaginatePaginationConfigTypeDef,
    ListCACertificatesPaginateResponseTypeDef,
    ListCertificatesByCAPaginatePaginationConfigTypeDef,
    ListCertificatesByCAPaginateResponseTypeDef,
    ListCertificatesPaginatePaginationConfigTypeDef,
    ListCertificatesPaginateResponseTypeDef,
    ListIndicesPaginatePaginationConfigTypeDef,
    ListIndicesPaginateResponseTypeDef,
    ListJobExecutionsForJobPaginatePaginationConfigTypeDef,
    ListJobExecutionsForJobPaginateResponseTypeDef,
    ListJobExecutionsForThingPaginatePaginationConfigTypeDef,
    ListJobExecutionsForThingPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
    ListOTAUpdatesPaginatePaginationConfigTypeDef,
    ListOTAUpdatesPaginateResponseTypeDef,
    ListOutgoingCertificatesPaginatePaginationConfigTypeDef,
    ListOutgoingCertificatesPaginateResponseTypeDef,
    ListPoliciesPaginatePaginationConfigTypeDef,
    ListPoliciesPaginateResponseTypeDef,
    ListPolicyPrincipalsPaginatePaginationConfigTypeDef,
    ListPolicyPrincipalsPaginateResponseTypeDef,
    ListPrincipalPoliciesPaginatePaginationConfigTypeDef,
    ListPrincipalPoliciesPaginateResponseTypeDef,
    ListPrincipalThingsPaginatePaginationConfigTypeDef,
    ListPrincipalThingsPaginateResponseTypeDef,
    ListRoleAliasesPaginatePaginationConfigTypeDef,
    ListRoleAliasesPaginateResponseTypeDef,
    ListScheduledAuditsPaginatePaginationConfigTypeDef,
    ListScheduledAuditsPaginateResponseTypeDef,
    ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef,
    ListSecurityProfilesForTargetPaginateResponseTypeDef,
    ListSecurityProfilesPaginatePaginationConfigTypeDef,
    ListSecurityProfilesPaginateResponseTypeDef,
    ListStreamsPaginatePaginationConfigTypeDef,
    ListStreamsPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListTargetsForPolicyPaginatePaginationConfigTypeDef,
    ListTargetsForPolicyPaginateResponseTypeDef,
    ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef,
    ListTargetsForSecurityProfilePaginateResponseTypeDef,
    ListThingGroupsForThingPaginatePaginationConfigTypeDef,
    ListThingGroupsForThingPaginateResponseTypeDef,
    ListThingGroupsPaginatePaginationConfigTypeDef,
    ListThingGroupsPaginateResponseTypeDef,
    ListThingRegistrationTasksPaginatePaginationConfigTypeDef,
    ListThingRegistrationTasksPaginateResponseTypeDef,
    ListThingTypesPaginatePaginationConfigTypeDef,
    ListThingTypesPaginateResponseTypeDef,
    ListThingsInBillingGroupPaginatePaginationConfigTypeDef,
    ListThingsInBillingGroupPaginateResponseTypeDef,
    ListThingsInThingGroupPaginatePaginationConfigTypeDef,
    ListThingsInThingGroupPaginateResponseTypeDef,
    ListThingsPaginatePaginationConfigTypeDef,
    ListThingsPaginateResponseTypeDef,
    ListTopicRulesPaginatePaginationConfigTypeDef,
    ListTopicRulesPaginateResponseTypeDef,
    ListV2LoggingLevelsPaginatePaginationConfigTypeDef,
    ListV2LoggingLevelsPaginateResponseTypeDef,
    ListViolationEventsPaginatePaginationConfigTypeDef,
    ListViolationEventsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListActiveViolationsPaginator",
    "ListAttachedPoliciesPaginator",
    "ListAuditFindingsPaginator",
    "ListAuditTasksPaginator",
    "ListAuthorizersPaginator",
    "ListBillingGroupsPaginator",
    "ListCACertificatesPaginator",
    "ListCertificatesPaginator",
    "ListCertificatesByCAPaginator",
    "ListIndicesPaginator",
    "ListJobExecutionsForJobPaginator",
    "ListJobExecutionsForThingPaginator",
    "ListJobsPaginator",
    "ListOTAUpdatesPaginator",
    "ListOutgoingCertificatesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyPrincipalsPaginator",
    "ListPrincipalPoliciesPaginator",
    "ListPrincipalThingsPaginator",
    "ListRoleAliasesPaginator",
    "ListScheduledAuditsPaginator",
    "ListSecurityProfilesPaginator",
    "ListSecurityProfilesForTargetPaginator",
    "ListStreamsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
    "ListTargetsForSecurityProfilePaginator",
    "ListThingGroupsPaginator",
    "ListThingGroupsForThingPaginator",
    "ListThingRegistrationTasksPaginator",
    "ListThingTypesPaginator",
    "ListThingsPaginator",
    "ListThingsInBillingGroupPaginator",
    "ListThingsInThingGroupPaginator",
    "ListTopicRulesPaginator",
    "ListV2LoggingLevelsPaginator",
    "ListViolationEventsPaginator",
)


class ListActiveViolationsPaginator(Boto3Paginator):
    """
    Paginator for `list_active_violations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: ListActiveViolationsPaginatePaginationConfigTypeDef = None,
    ) -> ListActiveViolationsPaginateResponseTypeDef:
        """
        [ListActiveViolations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListActiveViolations.paginate)
        """


class ListAttachedPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_attached_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        target: str,
        recursive: bool = None,
        PaginationConfig: ListAttachedPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListAttachedPoliciesPaginateResponseTypeDef:
        """
        [ListAttachedPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies.paginate)
        """


class ListAuditFindingsPaginator(Boto3Paginator):
    """
    Paginator for `list_audit_findings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: ListAuditFindingsPaginateResourceIdentifierTypeDef = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: ListAuditFindingsPaginatePaginationConfigTypeDef = None,
    ) -> ListAuditFindingsPaginateResponseTypeDef:
        """
        [ListAuditFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuditFindings.paginate)
        """


class ListAuditTasksPaginator(Boto3Paginator):
    """
    Paginator for `list_audit_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"] = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        PaginationConfig: ListAuditTasksPaginatePaginationConfigTypeDef = None,
    ) -> ListAuditTasksPaginateResponseTypeDef:
        """
        [ListAuditTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuditTasks.paginate)
        """


class ListAuthorizersPaginator(Boto3Paginator):
    """
    Paginator for `list_authorizers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        PaginationConfig: ListAuthorizersPaginatePaginationConfigTypeDef = None,
    ) -> ListAuthorizersPaginateResponseTypeDef:
        """
        [ListAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListAuthorizers.paginate)
        """


class ListBillingGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_billing_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        namePrefixFilter: str = None,
        PaginationConfig: ListBillingGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListBillingGroupsPaginateResponseTypeDef:
        """
        [ListBillingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListBillingGroups.paginate)
        """


class ListCACertificatesPaginator(Boto3Paginator):
    """
    Paginator for `list_ca_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: ListCACertificatesPaginatePaginationConfigTypeDef = None,
    ) -> ListCACertificatesPaginateResponseTypeDef:
        """
        [ListCACertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCACertificates.paginate)
        """


class ListCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `list_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: ListCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> ListCertificatesPaginateResponseTypeDef:
        """
        [ListCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCertificates.paginate)
        """


class ListCertificatesByCAPaginator(Boto3Paginator):
    """
    Paginator for `list_certificates_by_ca`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caCertificateId: str,
        ascendingOrder: bool = None,
        PaginationConfig: ListCertificatesByCAPaginatePaginationConfigTypeDef = None,
    ) -> ListCertificatesByCAPaginateResponseTypeDef:
        """
        [ListCertificatesByCA.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA.paginate)
        """


class ListIndicesPaginator(Boto3Paginator):
    """
    Paginator for `list_indices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListIndicesPaginatePaginationConfigTypeDef = None
    ) -> ListIndicesPaginateResponseTypeDef:
        """
        [ListIndices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListIndices.paginate)
        """


class ListJobExecutionsForJobPaginator(Boto3Paginator):
    """
    Paginator for `list_job_executions_for_job`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        jobId: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        PaginationConfig: ListJobExecutionsForJobPaginatePaginationConfigTypeDef = None,
    ) -> ListJobExecutionsForJobPaginateResponseTypeDef:
        """
        [ListJobExecutionsForJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob.paginate)
        """


class ListJobExecutionsForThingPaginator(Boto3Paginator):
    """
    Paginator for `list_job_executions_for_thing`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingName: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        PaginationConfig: ListJobExecutionsForThingPaginatePaginationConfigTypeDef = None,
    ) -> ListJobExecutionsForThingPaginateResponseTypeDef:
        """
        [ListJobExecutionsForThing.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        status: Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListJobs.paginate)
        """


class ListOTAUpdatesPaginator(Boto3Paginator):
    """
    Paginator for `list_ota_updates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        otaUpdateStatus: Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ] = None,
        PaginationConfig: ListOTAUpdatesPaginatePaginationConfigTypeDef = None,
    ) -> ListOTAUpdatesPaginateResponseTypeDef:
        """
        [ListOTAUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListOTAUpdates.paginate)
        """


class ListOutgoingCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `list_outgoing_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: ListOutgoingCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> ListOutgoingCertificatesPaginateResponseTypeDef:
        """
        [ListOutgoingCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: ListPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListPoliciesPaginateResponseTypeDef:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPolicies.paginate)
        """


class ListPolicyPrincipalsPaginator(Boto3Paginator):
    """
    Paginator for `list_policy_principals`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        policyName: str,
        ascendingOrder: bool = None,
        PaginationConfig: ListPolicyPrincipalsPaginatePaginationConfigTypeDef = None,
    ) -> ListPolicyPrincipalsPaginateResponseTypeDef:
        """
        [ListPolicyPrincipals.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals.paginate)
        """


class ListPrincipalPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_principal_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        principal: str,
        ascendingOrder: bool = None,
        PaginationConfig: ListPrincipalPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListPrincipalPoliciesPaginateResponseTypeDef:
        """
        [ListPrincipalPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies.paginate)
        """


class ListPrincipalThingsPaginator(Boto3Paginator):
    """
    Paginator for `list_principal_things`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        principal: str,
        PaginationConfig: ListPrincipalThingsPaginatePaginationConfigTypeDef = None,
    ) -> ListPrincipalThingsPaginateResponseTypeDef:
        """
        [ListPrincipalThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListPrincipalThings.paginate)
        """


class ListRoleAliasesPaginator(Boto3Paginator):
    """
    Paginator for `list_role_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: ListRoleAliasesPaginatePaginationConfigTypeDef = None,
    ) -> ListRoleAliasesPaginateResponseTypeDef:
        """
        [ListRoleAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListRoleAliases.paginate)
        """


class ListScheduledAuditsPaginator(Boto3Paginator):
    """
    Paginator for `list_scheduled_audits`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListScheduledAuditsPaginatePaginationConfigTypeDef = None
    ) -> ListScheduledAuditsPaginateResponseTypeDef:
        """
        [ListScheduledAudits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListScheduledAudits.paginate)
        """


class ListSecurityProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_security_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSecurityProfilesPaginatePaginationConfigTypeDef = None
    ) -> ListSecurityProfilesPaginateResponseTypeDef:
        """
        [ListSecurityProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles.paginate)
        """


class ListSecurityProfilesForTargetPaginator(Boto3Paginator):
    """
    Paginator for `list_security_profiles_for_target`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        securityProfileTargetArn: str,
        recursive: bool = None,
        PaginationConfig: ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef = None,
    ) -> ListSecurityProfilesForTargetPaginateResponseTypeDef:
        """
        [ListSecurityProfilesForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    Paginator for `list_streams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: ListStreamsPaginatePaginationConfigTypeDef = None,
    ) -> ListStreamsPaginateResponseTypeDef:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListStreams.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTagsForResource.paginate)
        """


class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    Paginator for `list_targets_for_policy`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        policyName: str,
        PaginationConfig: ListTargetsForPolicyPaginatePaginationConfigTypeDef = None,
    ) -> ListTargetsForPolicyPaginateResponseTypeDef:
        """
        [ListTargetsForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy.paginate)
        """


class ListTargetsForSecurityProfilePaginator(Boto3Paginator):
    """
    Paginator for `list_targets_for_security_profile`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        securityProfileName: str,
        PaginationConfig: ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef = None,
    ) -> ListTargetsForSecurityProfilePaginateResponseTypeDef:
        """
        [ListTargetsForSecurityProfile.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile.paginate)
        """


class ListThingGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_thing_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
        PaginationConfig: ListThingGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListThingGroupsPaginateResponseTypeDef:
        """
        [ListThingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingGroups.paginate)
        """


class ListThingGroupsForThingPaginator(Boto3Paginator):
    """
    Paginator for `list_thing_groups_for_thing`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingName: str,
        PaginationConfig: ListThingGroupsForThingPaginatePaginationConfigTypeDef = None,
    ) -> ListThingGroupsForThingPaginateResponseTypeDef:
        """
        [ListThingGroupsForThing.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing.paginate)
        """


class ListThingRegistrationTasksPaginator(Boto3Paginator):
    """
    Paginator for `list_thing_registration_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        status: Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"] = None,
        PaginationConfig: ListThingRegistrationTasksPaginatePaginationConfigTypeDef = None,
    ) -> ListThingRegistrationTasksPaginateResponseTypeDef:
        """
        [ListThingRegistrationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks.paginate)
        """


class ListThingTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_thing_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingTypeName: str = None,
        PaginationConfig: ListThingTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListThingTypesPaginateResponseTypeDef:
        """
        [ListThingTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingTypes.paginate)
        """


class ListThingsPaginator(Boto3Paginator):
    """
    Paginator for `list_things`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        PaginationConfig: ListThingsPaginatePaginationConfigTypeDef = None,
    ) -> ListThingsPaginateResponseTypeDef:
        """
        [ListThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThings.paginate)
        """


class ListThingsInBillingGroupPaginator(Boto3Paginator):
    """
    Paginator for `list_things_in_billing_group`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        billingGroupName: str,
        PaginationConfig: ListThingsInBillingGroupPaginatePaginationConfigTypeDef = None,
    ) -> ListThingsInBillingGroupPaginateResponseTypeDef:
        """
        [ListThingsInBillingGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup.paginate)
        """


class ListThingsInThingGroupPaginator(Boto3Paginator):
    """
    Paginator for `list_things_in_thing_group`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        thingGroupName: str,
        recursive: bool = None,
        PaginationConfig: ListThingsInThingGroupPaginatePaginationConfigTypeDef = None,
    ) -> ListThingsInThingGroupPaginateResponseTypeDef:
        """
        [ListThingsInThingGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup.paginate)
        """


class ListTopicRulesPaginator(Boto3Paginator):
    """
    Paginator for `list_topic_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        topic: str = None,
        ruleDisabled: bool = None,
        PaginationConfig: ListTopicRulesPaginatePaginationConfigTypeDef = None,
    ) -> ListTopicRulesPaginateResponseTypeDef:
        """
        [ListTopicRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListTopicRules.paginate)
        """


class ListV2LoggingLevelsPaginator(Boto3Paginator):
    """
    Paginator for `list_v2_logging_levels`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        targetType: Literal["DEFAULT", "THING_GROUP"] = None,
        PaginationConfig: ListV2LoggingLevelsPaginatePaginationConfigTypeDef = None,
    ) -> ListV2LoggingLevelsPaginateResponseTypeDef:
        """
        [ListV2LoggingLevels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels.paginate)
        """


class ListViolationEventsPaginator(Boto3Paginator):
    """
    Paginator for `list_violation_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: ListViolationEventsPaginatePaginationConfigTypeDef = None,
    ) -> ListViolationEventsPaginateResponseTypeDef:
        """
        [ListViolationEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iot.html#IoT.Paginator.ListViolationEvents.paginate)
        """
