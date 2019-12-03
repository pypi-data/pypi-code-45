"Main interface for mturk service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitAssignmentReviewPolicyParametersTypeDef",
    "ClientCreateHitAssignmentReviewPolicyTypeDef",
    "ClientCreateHitHITLayoutParametersTypeDef",
    "ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitHITReviewPolicyParametersTypeDef",
    "ClientCreateHitHITReviewPolicyTypeDef",
    "ClientCreateHitQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitQualificationRequirementsTypeDef",
    "ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitResponseHITQualificationRequirementsTypeDef",
    "ClientCreateHitResponseHITTypeDef",
    "ClientCreateHitResponseTypeDef",
    "ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitTypeQualificationRequirementsTypeDef",
    "ClientCreateHitTypeResponseTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef",
    "ClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef",
    "ClientCreateHitWithHitTypeHITLayoutParametersTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef",
    "ClientCreateHitWithHitTypeHITReviewPolicyTypeDef",
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef",
    "ClientCreateHitWithHitTypeResponseHITTypeDef",
    "ClientCreateHitWithHitTypeResponseTypeDef",
    "ClientCreateQualificationTypeResponseQualificationTypeTypeDef",
    "ClientCreateQualificationTypeResponseTypeDef",
    "ClientGetAccountBalanceResponseTypeDef",
    "ClientGetAssignmentResponseAssignmentTypeDef",
    "ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientGetAssignmentResponseHITQualificationRequirementsTypeDef",
    "ClientGetAssignmentResponseHITTypeDef",
    "ClientGetAssignmentResponseTypeDef",
    "ClientGetFileUploadUrlResponseTypeDef",
    "ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    "ClientGetHitResponseHITQualificationRequirementsTypeDef",
    "ClientGetHitResponseHITTypeDef",
    "ClientGetHitResponseTypeDef",
    "ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef",
    "ClientGetQualificationScoreResponseQualificationTypeDef",
    "ClientGetQualificationScoreResponseTypeDef",
    "ClientGetQualificationTypeResponseQualificationTypeTypeDef",
    "ClientGetQualificationTypeResponseTypeDef",
    "ClientListAssignmentsForHitResponseAssignmentsTypeDef",
    "ClientListAssignmentsForHitResponseTypeDef",
    "ClientListBonusPaymentsResponseBonusPaymentsTypeDef",
    "ClientListBonusPaymentsResponseTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef",
    "ClientListHitsForQualificationTypeResponseHITsTypeDef",
    "ClientListHitsForQualificationTypeResponseTypeDef",
    "ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListHitsResponseHITsQualificationRequirementsTypeDef",
    "ClientListHitsResponseHITsTypeDef",
    "ClientListHitsResponseTypeDef",
    "ClientListQualificationRequestsResponseQualificationRequestsTypeDef",
    "ClientListQualificationRequestsResponseTypeDef",
    "ClientListQualificationTypesResponseQualificationTypesTypeDef",
    "ClientListQualificationTypesResponseTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef",
    "ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef",
    "ClientListReviewPolicyResultsForHitResponseTypeDef",
    "ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef",
    "ClientListReviewableHitsResponseHITsTypeDef",
    "ClientListReviewableHitsResponseTypeDef",
    "ClientListWorkerBlocksResponseWorkerBlocksTypeDef",
    "ClientListWorkerBlocksResponseTypeDef",
    "ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef",
    "ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef",
    "ClientListWorkersWithQualificationTypeResponseTypeDef",
    "ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef",
    "ClientNotifyWorkersResponseTypeDef",
    "ClientSendTestEventNotificationNotificationTypeDef",
    "ClientUpdateNotificationSettingsNotificationTypeDef",
    "ClientUpdateQualificationTypeResponseQualificationTypeTypeDef",
    "ClientUpdateQualificationTypeResponseTypeDef",
    "ListAssignmentsForHITPaginatePaginationConfigTypeDef",
    "ListAssignmentsForHITPaginateResponseAssignmentsTypeDef",
    "ListAssignmentsForHITPaginateResponseTypeDef",
    "ListBonusPaymentsPaginatePaginationConfigTypeDef",
    "ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef",
    "ListBonusPaymentsPaginateResponseTypeDef",
    "ListHITsForQualificationTypePaginatePaginationConfigTypeDef",
    "ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef",
    "ListHITsForQualificationTypePaginateResponseHITsTypeDef",
    "ListHITsForQualificationTypePaginateResponseTypeDef",
    "ListHITsPaginatePaginationConfigTypeDef",
    "ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ListHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    "ListHITsPaginateResponseHITsTypeDef",
    "ListHITsPaginateResponseTypeDef",
    "ListQualificationRequestsPaginatePaginationConfigTypeDef",
    "ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef",
    "ListQualificationRequestsPaginateResponseTypeDef",
    "ListQualificationTypesPaginatePaginationConfigTypeDef",
    "ListQualificationTypesPaginateResponseQualificationTypesTypeDef",
    "ListQualificationTypesPaginateResponseTypeDef",
    "ListReviewableHITsPaginatePaginationConfigTypeDef",
    "ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    "ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    "ListReviewableHITsPaginateResponseHITsTypeDef",
    "ListReviewableHITsPaginateResponseTypeDef",
    "ListWorkerBlocksPaginatePaginationConfigTypeDef",
    "ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef",
    "ListWorkerBlocksPaginateResponseTypeDef",
    "ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef",
    "ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef",
    "ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef",
    "ListWorkersWithQualificationTypePaginateResponseTypeDef",
)


_ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef
):
    pass


_ClientCreateHitAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[ClientCreateHitAssignmentReviewPolicyParametersMapEntriesTypeDef],
    },
    total=False,
)


class ClientCreateHitAssignmentReviewPolicyParametersTypeDef(
    _ClientCreateHitAssignmentReviewPolicyParametersTypeDef
):
    pass


_RequiredClientCreateHitAssignmentReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitAssignmentReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitAssignmentReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitAssignmentReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitAssignmentReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitAssignmentReviewPolicyTypeDef(
    _RequiredClientCreateHitAssignmentReviewPolicyTypeDef,
    _OptionalClientCreateHitAssignmentReviewPolicyTypeDef,
):
    """
    The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for
    Mechanical Turk to take various actions based on the policy.
    - **PolicyName** *(string) --***[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
    """


_RequiredClientCreateHitHITLayoutParametersTypeDef = TypedDict(
    "_RequiredClientCreateHitHITLayoutParametersTypeDef", {"Name": str}
)
_OptionalClientCreateHitHITLayoutParametersTypeDef = TypedDict(
    "_OptionalClientCreateHitHITLayoutParametersTypeDef", {"Value": str}, total=False
)


class ClientCreateHitHITLayoutParametersTypeDef(
    _RequiredClientCreateHitHITLayoutParametersTypeDef,
    _OptionalClientCreateHitHITLayoutParametersTypeDef,
):
    """
    - *(dict) --*

      The HITLayoutParameter data structure defines parameter values used with a HITLayout. A
      HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human
      Intelligence Task (HIT) question data for CreateHIT.
      - **Name** *(string) --***[REQUIRED]**

        The name of the parameter in the HITLayout.
    """


_ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef
):
    pass


_ClientCreateHitHITReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[ClientCreateHitHITReviewPolicyParametersMapEntriesTypeDef],
    },
    total=False,
)


class ClientCreateHitHITReviewPolicyParametersTypeDef(
    _ClientCreateHitHITReviewPolicyParametersTypeDef
):
    pass


_RequiredClientCreateHitHITReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitHITReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitHITReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitHITReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitHITReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitHITReviewPolicyTypeDef(
    _RequiredClientCreateHitHITReviewPolicyTypeDef, _OptionalClientCreateHitHITReviewPolicyTypeDef
):
    """
    The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take
    various actions based on the policy.
    - **PolicyName** *(string) --***[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
    """


_ClientCreateHitQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientCreateHitQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientCreateHitQualificationRequirementsLocaleValuesTypeDef(
    _ClientCreateHitQualificationRequirementsLocaleValuesTypeDef
):
    pass


_RequiredClientCreateHitQualificationRequirementsTypeDef = TypedDict(
    "_RequiredClientCreateHitQualificationRequirementsTypeDef", {"QualificationTypeId": str}
)
_OptionalClientCreateHitQualificationRequirementsTypeDef = TypedDict(
    "_OptionalClientCreateHitQualificationRequirementsTypeDef",
    {
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[ClientCreateHitQualificationRequirementsLocaleValuesTypeDef],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientCreateHitQualificationRequirementsTypeDef(
    _RequiredClientCreateHitQualificationRequirementsTypeDef,
    _OptionalClientCreateHitQualificationRequirementsTypeDef,
):
    """
    - *(dict) --*

      The QualificationRequirement data structure describes a Qualification that a Worker must have
      before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker
      must have the Qualification in order to preview the HIT, or see the HIT in search results.
      - **QualificationTypeId** *(string) --***[REQUIRED]**

        The ID of the Qualification type for the requirement.
    """


_ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ClientCreateHitResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientCreateHitResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientCreateHitResponseHITQualificationRequirementsTypeDef(
    _ClientCreateHitResponseHITQualificationRequirementsTypeDef
):
    pass


_ClientCreateHitResponseHITTypeDef = TypedDict(
    "_ClientCreateHitResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientCreateHitResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientCreateHitResponseHITTypeDef(_ClientCreateHitResponseHITTypeDef):
    """
    - **HIT** *(dict) --*

      Contains the newly created HIT data. For a description of the HIT data structure as it appears
      in responses, see the HIT Data Structure documentation.
      - **HITId** *(string) --*

        A unique identifier for the HIT.
    """


_ClientCreateHitResponseTypeDef = TypedDict(
    "_ClientCreateHitResponseTypeDef", {"HIT": ClientCreateHitResponseHITTypeDef}, total=False
)


class ClientCreateHitResponseTypeDef(_ClientCreateHitResponseTypeDef):
    """
    - *(dict) --*

      - **HIT** *(dict) --*

        Contains the newly created HIT data. For a description of the HIT data structure as it
        appears in responses, see the HIT Data Structure documentation.
        - **HITId** *(string) --*

          A unique identifier for the HIT.
    """


_ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef(
    _ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef
):
    pass


_RequiredClientCreateHitTypeQualificationRequirementsTypeDef = TypedDict(
    "_RequiredClientCreateHitTypeQualificationRequirementsTypeDef", {"QualificationTypeId": str}
)
_OptionalClientCreateHitTypeQualificationRequirementsTypeDef = TypedDict(
    "_OptionalClientCreateHitTypeQualificationRequirementsTypeDef",
    {
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[ClientCreateHitTypeQualificationRequirementsLocaleValuesTypeDef],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientCreateHitTypeQualificationRequirementsTypeDef(
    _RequiredClientCreateHitTypeQualificationRequirementsTypeDef,
    _OptionalClientCreateHitTypeQualificationRequirementsTypeDef,
):
    """
    - *(dict) --*

      The QualificationRequirement data structure describes a Qualification that a Worker must have
      before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker
      must have the Qualification in order to preview the HIT, or see the HIT in search results.
      - **QualificationTypeId** *(string) --***[REQUIRED]**

        The ID of the Qualification type for the requirement.
    """


_ClientCreateHitTypeResponseTypeDef = TypedDict(
    "_ClientCreateHitTypeResponseTypeDef", {"HITTypeId": str}, total=False
)


class ClientCreateHitTypeResponseTypeDef(_ClientCreateHitTypeResponseTypeDef):
    """
    - *(dict) --*

      - **HITTypeId** *(string) --*

        The ID of the newly registered HIT type.
    """


_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef
):
    pass


_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef(
    _ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef
):
    pass


_RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitWithHitTypeAssignmentReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef(
    _RequiredClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef,
    _OptionalClientCreateHitWithHitTypeAssignmentReviewPolicyTypeDef,
):
    """
    The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for
    Mechanical Turk to take various actions based on the policy.
    - **PolicyName** *(string) --***[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
    """


_RequiredClientCreateHitWithHitTypeHITLayoutParametersTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeHITLayoutParametersTypeDef", {"Name": str}
)
_OptionalClientCreateHitWithHitTypeHITLayoutParametersTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeHITLayoutParametersTypeDef", {"Value": str}, total=False
)


class ClientCreateHitWithHitTypeHITLayoutParametersTypeDef(
    _RequiredClientCreateHitWithHitTypeHITLayoutParametersTypeDef,
    _OptionalClientCreateHitWithHitTypeHITLayoutParametersTypeDef,
):
    """
    - *(dict) --*

      The HITLayoutParameter data structure defines parameter values used with a HITLayout. A
      HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human
      Intelligence Task (HIT) question data for CreateHIT.
      - **Name** *(string) --***[REQUIRED]**

        The name of the parameter in the HITLayout.
    """


_ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef(
    _ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef
):
    pass


_ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[ClientCreateHitWithHitTypeHITReviewPolicyParametersMapEntriesTypeDef],
    },
    total=False,
)


class ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef(
    _ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef
):
    pass


_RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef = TypedDict(
    "_RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef", {"PolicyName": str}
)
_OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef = TypedDict(
    "_OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef",
    {"Parameters": List[ClientCreateHitWithHitTypeHITReviewPolicyParametersTypeDef]},
    total=False,
)


class ClientCreateHitWithHitTypeHITReviewPolicyTypeDef(
    _RequiredClientCreateHitWithHitTypeHITReviewPolicyTypeDef,
    _OptionalClientCreateHitWithHitTypeHITReviewPolicyTypeDef,
):
    """
    The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take
    various actions based on the policy.
    - **PolicyName** *(string) --***[REQUIRED]**

      Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
    """


_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientCreateHitWithHitTypeResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef(
    _ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef
):
    pass


_ClientCreateHitWithHitTypeResponseHITTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientCreateHitWithHitTypeResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientCreateHitWithHitTypeResponseHITTypeDef(_ClientCreateHitWithHitTypeResponseHITTypeDef):
    """
    - **HIT** *(dict) --*

      Contains the newly created HIT data. For a description of the HIT data structure as it appears
      in responses, see the HIT Data Structure documentation.
      - **HITId** *(string) --*

        A unique identifier for the HIT.
    """


_ClientCreateHitWithHitTypeResponseTypeDef = TypedDict(
    "_ClientCreateHitWithHitTypeResponseTypeDef",
    {"HIT": ClientCreateHitWithHitTypeResponseHITTypeDef},
    total=False,
)


class ClientCreateHitWithHitTypeResponseTypeDef(_ClientCreateHitWithHitTypeResponseTypeDef):
    """
    - *(dict) --*

      - **HIT** *(dict) --*

        Contains the newly created HIT data. For a description of the HIT data structure as it
        appears in responses, see the HIT Data Structure documentation.
        - **HITId** *(string) --*

          A unique identifier for the HIT.
    """


_ClientCreateQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "_ClientCreateQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientCreateQualificationTypeResponseQualificationTypeTypeDef(
    _ClientCreateQualificationTypeResponseQualificationTypeTypeDef
):
    """
    - **QualificationType** *(dict) --*

      The created Qualification type, returned as a QualificationType data structure.
      - **QualificationTypeId** *(string) --*

        A unique identifier for the Qualification type. A Qualification type is given a
        Qualification type ID when you call the CreateQualificationType operation.
    """


_ClientCreateQualificationTypeResponseTypeDef = TypedDict(
    "_ClientCreateQualificationTypeResponseTypeDef",
    {"QualificationType": ClientCreateQualificationTypeResponseQualificationTypeTypeDef},
    total=False,
)


class ClientCreateQualificationTypeResponseTypeDef(_ClientCreateQualificationTypeResponseTypeDef):
    """
    - *(dict) --*

      - **QualificationType** *(dict) --*

        The created Qualification type, returned as a QualificationType data structure.
        - **QualificationTypeId** *(string) --*

          A unique identifier for the Qualification type. A Qualification type is given a
          Qualification type ID when you call the CreateQualificationType operation.
    """


_ClientGetAccountBalanceResponseTypeDef = TypedDict(
    "_ClientGetAccountBalanceResponseTypeDef",
    {"AvailableBalance": str, "OnHoldBalance": str},
    total=False,
)


class ClientGetAccountBalanceResponseTypeDef(_ClientGetAccountBalanceResponseTypeDef):
    """
    - *(dict) --*

      - **AvailableBalance** *(string) --*

        A string representing a currency amount.
    """


_ClientGetAssignmentResponseAssignmentTypeDef = TypedDict(
    "_ClientGetAssignmentResponseAssignmentTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": Literal["Submitted", "Approved", "Rejected"],
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)


class ClientGetAssignmentResponseAssignmentTypeDef(_ClientGetAssignmentResponseAssignmentTypeDef):
    """
    - **Assignment** *(dict) --*

      The assignment. The response includes one Assignment element.
      - **AssignmentId** *(string) --*

        A unique identifier for the assignment.
    """


_ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ClientGetAssignmentResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientGetAssignmentResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientGetAssignmentResponseHITQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientGetAssignmentResponseHITQualificationRequirementsTypeDef(
    _ClientGetAssignmentResponseHITQualificationRequirementsTypeDef
):
    pass


_ClientGetAssignmentResponseHITTypeDef = TypedDict(
    "_ClientGetAssignmentResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientGetAssignmentResponseHITQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientGetAssignmentResponseHITTypeDef(_ClientGetAssignmentResponseHITTypeDef):
    pass


_ClientGetAssignmentResponseTypeDef = TypedDict(
    "_ClientGetAssignmentResponseTypeDef",
    {
        "Assignment": ClientGetAssignmentResponseAssignmentTypeDef,
        "HIT": ClientGetAssignmentResponseHITTypeDef,
    },
    total=False,
)


class ClientGetAssignmentResponseTypeDef(_ClientGetAssignmentResponseTypeDef):
    """
    - *(dict) --*

      - **Assignment** *(dict) --*

        The assignment. The response includes one Assignment element.
        - **AssignmentId** *(string) --*

          A unique identifier for the assignment.
    """


_ClientGetFileUploadUrlResponseTypeDef = TypedDict(
    "_ClientGetFileUploadUrlResponseTypeDef", {"FileUploadURL": str}, total=False
)


class ClientGetFileUploadUrlResponseTypeDef(_ClientGetFileUploadUrlResponseTypeDef):
    """
    - *(dict) --*

      - **FileUploadURL** *(string) --*

        A temporary URL for the file that the Worker uploaded for the answer.
    """


_ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef(
    _ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ClientGetHitResponseHITQualificationRequirementsTypeDef = TypedDict(
    "_ClientGetHitResponseHITQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[ClientGetHitResponseHITQualificationRequirementsLocaleValuesTypeDef],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientGetHitResponseHITQualificationRequirementsTypeDef(
    _ClientGetHitResponseHITQualificationRequirementsTypeDef
):
    pass


_ClientGetHitResponseHITTypeDef = TypedDict(
    "_ClientGetHitResponseHITTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[ClientGetHitResponseHITQualificationRequirementsTypeDef],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientGetHitResponseHITTypeDef(_ClientGetHitResponseHITTypeDef):
    """
    - **HIT** *(dict) --*

      Contains the requested HIT data.
      - **HITId** *(string) --*

        A unique identifier for the HIT.
    """


_ClientGetHitResponseTypeDef = TypedDict(
    "_ClientGetHitResponseTypeDef", {"HIT": ClientGetHitResponseHITTypeDef}, total=False
)


class ClientGetHitResponseTypeDef(_ClientGetHitResponseTypeDef):
    """
    - *(dict) --*

      - **HIT** *(dict) --*

        Contains the requested HIT data.
        - **HITId** *(string) --*

          A unique identifier for the HIT.
    """


_ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef = TypedDict(
    "_ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef(
    _ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef
):
    pass


_ClientGetQualificationScoreResponseQualificationTypeDef = TypedDict(
    "_ClientGetQualificationScoreResponseQualificationTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ClientGetQualificationScoreResponseQualificationLocaleValueTypeDef,
        "Status": Literal["Granted", "Revoked"],
    },
    total=False,
)


class ClientGetQualificationScoreResponseQualificationTypeDef(
    _ClientGetQualificationScoreResponseQualificationTypeDef
):
    """
    - **Qualification** *(dict) --*

      The Qualification data structure of the Qualification assigned to a user, including the
      Qualification type and the value (score).
      - **QualificationTypeId** *(string) --*

        The ID of the Qualification type for the Qualification.
    """


_ClientGetQualificationScoreResponseTypeDef = TypedDict(
    "_ClientGetQualificationScoreResponseTypeDef",
    {"Qualification": ClientGetQualificationScoreResponseQualificationTypeDef},
    total=False,
)


class ClientGetQualificationScoreResponseTypeDef(_ClientGetQualificationScoreResponseTypeDef):
    """
    - *(dict) --*

      - **Qualification** *(dict) --*

        The Qualification data structure of the Qualification assigned to a user, including the
        Qualification type and the value (score).
        - **QualificationTypeId** *(string) --*

          The ID of the Qualification type for the Qualification.
    """


_ClientGetQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "_ClientGetQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientGetQualificationTypeResponseQualificationTypeTypeDef(
    _ClientGetQualificationTypeResponseQualificationTypeTypeDef
):
    """
    - **QualificationType** *(dict) --*

      The returned Qualification Type
      - **QualificationTypeId** *(string) --*

        A unique identifier for the Qualification type. A Qualification type is given a
        Qualification type ID when you call the CreateQualificationType operation.
    """


_ClientGetQualificationTypeResponseTypeDef = TypedDict(
    "_ClientGetQualificationTypeResponseTypeDef",
    {"QualificationType": ClientGetQualificationTypeResponseQualificationTypeTypeDef},
    total=False,
)


class ClientGetQualificationTypeResponseTypeDef(_ClientGetQualificationTypeResponseTypeDef):
    """
    - *(dict) --*

      - **QualificationType** *(dict) --*

        The returned Qualification Type
        - **QualificationTypeId** *(string) --*

          A unique identifier for the Qualification type. A Qualification type is given a
          Qualification type ID when you call the CreateQualificationType operation.
    """


_ClientListAssignmentsForHitResponseAssignmentsTypeDef = TypedDict(
    "_ClientListAssignmentsForHitResponseAssignmentsTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": Literal["Submitted", "Approved", "Rejected"],
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)


class ClientListAssignmentsForHitResponseAssignmentsTypeDef(
    _ClientListAssignmentsForHitResponseAssignmentsTypeDef
):
    pass


_ClientListAssignmentsForHitResponseTypeDef = TypedDict(
    "_ClientListAssignmentsForHitResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Assignments": List[ClientListAssignmentsForHitResponseAssignmentsTypeDef],
    },
    total=False,
)


class ClientListAssignmentsForHitResponseTypeDef(_ClientListAssignmentsForHitResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the previous response was incomplete (because there is more data to retrieve), Amazon
        Mechanical Turk returns a pagination token in the response. You can use this pagination
        token to retrieve the next set of results.
    """


_ClientListBonusPaymentsResponseBonusPaymentsTypeDef = TypedDict(
    "_ClientListBonusPaymentsResponseBonusPaymentsTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)


class ClientListBonusPaymentsResponseBonusPaymentsTypeDef(
    _ClientListBonusPaymentsResponseBonusPaymentsTypeDef
):
    pass


_ClientListBonusPaymentsResponseTypeDef = TypedDict(
    "_ClientListBonusPaymentsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "BonusPayments": List[ClientListBonusPaymentsResponseBonusPaymentsTypeDef],
    },
    total=False,
)


class ClientListBonusPaymentsResponseTypeDef(_ClientListBonusPaymentsResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of bonus payments on this page in the filtered results list, equivalent to the
        number of bonus payments being returned by this call.
    """


_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef(
    _ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef
):
    pass


_ClientListHitsForQualificationTypeResponseHITsTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListHitsForQualificationTypeResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientListHitsForQualificationTypeResponseHITsTypeDef(
    _ClientListHitsForQualificationTypeResponseHITsTypeDef
):
    pass


_ClientListHitsForQualificationTypeResponseTypeDef = TypedDict(
    "_ClientListHitsForQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[ClientListHitsForQualificationTypeResponseHITsTypeDef],
    },
    total=False,
)


class ClientListHitsForQualificationTypeResponseTypeDef(
    _ClientListHitsForQualificationTypeResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the previous response was incomplete (because there is more data to retrieve), Amazon
        Mechanical Turk returns a pagination token in the response. You can use this pagination
        token to retrieve the next set of results.
    """


_ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ClientListHitsResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ClientListHitsResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientListHitsResponseHITsQualificationRequirementsTypeDef(
    _ClientListHitsResponseHITsQualificationRequirementsTypeDef
):
    pass


_ClientListHitsResponseHITsTypeDef = TypedDict(
    "_ClientListHitsResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListHitsResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientListHitsResponseHITsTypeDef(_ClientListHitsResponseHITsTypeDef):
    pass


_ClientListHitsResponseTypeDef = TypedDict(
    "_ClientListHitsResponseTypeDef",
    {"NextToken": str, "NumResults": int, "HITs": List[ClientListHitsResponseHITsTypeDef]},
    total=False,
)


class ClientListHitsResponseTypeDef(_ClientListHitsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the previous response was incomplete (because there is more data to retrieve), Amazon
        Mechanical Turk returns a pagination token in the response. You can use this pagination
        token to retrieve the next set of results.
    """


_ClientListQualificationRequestsResponseQualificationRequestsTypeDef = TypedDict(
    "_ClientListQualificationRequestsResponseQualificationRequestsTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)


class ClientListQualificationRequestsResponseQualificationRequestsTypeDef(
    _ClientListQualificationRequestsResponseQualificationRequestsTypeDef
):
    pass


_ClientListQualificationRequestsResponseTypeDef = TypedDict(
    "_ClientListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationRequests": List[
            ClientListQualificationRequestsResponseQualificationRequestsTypeDef
        ],
    },
    total=False,
)


class ClientListQualificationRequestsResponseTypeDef(
    _ClientListQualificationRequestsResponseTypeDef
):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of Qualification requests on this page in the filtered results list, equivalent
        to the number of Qualification requests being returned by this call.
    """


_ClientListQualificationTypesResponseQualificationTypesTypeDef = TypedDict(
    "_ClientListQualificationTypesResponseQualificationTypesTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientListQualificationTypesResponseQualificationTypesTypeDef(
    _ClientListQualificationTypesResponseQualificationTypesTypeDef
):
    pass


_ClientListQualificationTypesResponseTypeDef = TypedDict(
    "_ClientListQualificationTypesResponseTypeDef",
    {
        "NumResults": int,
        "NextToken": str,
        "QualificationTypes": List[ClientListQualificationTypesResponseQualificationTypesTypeDef],
    },
    total=False,
)


class ClientListQualificationTypesResponseTypeDef(_ClientListQualificationTypesResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of Qualification types on this page in the filtered results list, equivalent to
        the number of types this operation returns.
    """


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyParametersTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": Literal["Intended", "Succeeded", "Failed", "Cancelled"],
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef",
    {
        "ReviewResults": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewResultsTypeDef
        ],
        "ReviewActions": List[
            ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportReviewActionsTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef(
    _ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MapEntries": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersMapEntriesTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewPolicyParametersTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef",
    {
        "ActionId": str,
        "ActionName": str,
        "TargetId": str,
        "TargetType": str,
        "Status": Literal["Intended", "Succeeded", "Failed", "Cancelled"],
        "CompleteTime": datetime,
        "Result": str,
        "ErrorCode": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef",
    {
        "ActionId": str,
        "SubjectId": str,
        "SubjectType": str,
        "QuestionId": str,
        "Key": str,
        "Value": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef",
    {
        "ReviewResults": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewResultsTypeDef
        ],
        "ReviewActions": List[
            ClientListReviewPolicyResultsForHitResponseHITReviewReportReviewActionsTypeDef
        ],
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef(
    _ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef
):
    pass


_ClientListReviewPolicyResultsForHitResponseTypeDef = TypedDict(
    "_ClientListReviewPolicyResultsForHitResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": ClientListReviewPolicyResultsForHitResponseAssignmentReviewPolicyTypeDef,
        "HITReviewPolicy": ClientListReviewPolicyResultsForHitResponseHITReviewPolicyTypeDef,
        "AssignmentReviewReport": ClientListReviewPolicyResultsForHitResponseAssignmentReviewReportTypeDef,
        "HITReviewReport": ClientListReviewPolicyResultsForHitResponseHITReviewReportTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientListReviewPolicyResultsForHitResponseTypeDef(
    _ClientListReviewPolicyResultsForHitResponseTypeDef
):
    """
    - *(dict) --*

      - **HITId** *(string) --*

        The HITId of the HIT for which results have been returned.
    """


_ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ClientListReviewableHitsResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef(
    _ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef
):
    pass


_ClientListReviewableHitsResponseHITsTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ClientListReviewableHitsResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ClientListReviewableHitsResponseHITsTypeDef(_ClientListReviewableHitsResponseHITsTypeDef):
    pass


_ClientListReviewableHitsResponseTypeDef = TypedDict(
    "_ClientListReviewableHitsResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "HITs": List[ClientListReviewableHitsResponseHITsTypeDef],
    },
    total=False,
)


class ClientListReviewableHitsResponseTypeDef(_ClientListReviewableHitsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the previous response was incomplete (because there is more data to retrieve), Amazon
        Mechanical Turk returns a pagination token in the response. You can use this pagination
        token to retrieve the next set of results.
    """


_ClientListWorkerBlocksResponseWorkerBlocksTypeDef = TypedDict(
    "_ClientListWorkerBlocksResponseWorkerBlocksTypeDef",
    {"WorkerId": str, "Reason": str},
    total=False,
)


class ClientListWorkerBlocksResponseWorkerBlocksTypeDef(
    _ClientListWorkerBlocksResponseWorkerBlocksTypeDef
):
    pass


_ClientListWorkerBlocksResponseTypeDef = TypedDict(
    "_ClientListWorkerBlocksResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "WorkerBlocks": List[ClientListWorkerBlocksResponseWorkerBlocksTypeDef],
    },
    total=False,
)


class ClientListWorkerBlocksResponseTypeDef(_ClientListWorkerBlocksResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the previous response was incomplete (because there is more data to retrieve), Amazon
        Mechanical Turk returns a pagination token in the response. You can use this pagination
        token to retrieve the next set of results.
    """


_ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef = TypedDict(
    "_ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef(
    _ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef
):
    pass


_ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef = TypedDict(
    "_ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ClientListWorkersWithQualificationTypeResponseQualificationsLocaleValueTypeDef,
        "Status": Literal["Granted", "Revoked"],
    },
    total=False,
)


class ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef(
    _ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef
):
    pass


_ClientListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "_ClientListWorkersWithQualificationTypeResponseTypeDef",
    {
        "NextToken": str,
        "NumResults": int,
        "Qualifications": List[ClientListWorkersWithQualificationTypeResponseQualificationsTypeDef],
    },
    total=False,
)


class ClientListWorkersWithQualificationTypeResponseTypeDef(
    _ClientListWorkersWithQualificationTypeResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the previous response was incomplete (because there is more data to retrieve), Amazon
        Mechanical Turk returns a pagination token in the response. You can use this pagination
        token to retrieve the next set of results.
    """


_ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef = TypedDict(
    "_ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef",
    {
        "NotifyWorkersFailureCode": Literal["SoftFailure", "HardFailure"],
        "NotifyWorkersFailureMessage": str,
        "WorkerId": str,
    },
    total=False,
)


class ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef(
    _ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef
):
    """
    - *(dict) --*

      When MTurk encounters an issue with notifying the Workers you specified, it returns back this
      object with failure details.
      - **NotifyWorkersFailureCode** *(string) --*

        Encoded value for the failure type.
    """


_ClientNotifyWorkersResponseTypeDef = TypedDict(
    "_ClientNotifyWorkersResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List[
            ClientNotifyWorkersResponseNotifyWorkersFailureStatusesTypeDef
        ]
    },
    total=False,
)


class ClientNotifyWorkersResponseTypeDef(_ClientNotifyWorkersResponseTypeDef):
    """
    - *(dict) --*

      - **NotifyWorkersFailureStatuses** *(list) --*

        When MTurk sends notifications to the list of Workers, it returns back any failures it
        encounters in this list of NotifyWorkersFailureStatus objects.
        - *(dict) --*

          When MTurk encounters an issue with notifying the Workers you specified, it returns back
          this object with failure details.
          - **NotifyWorkersFailureCode** *(string) --*

            Encoded value for the failure type.
    """


_RequiredClientSendTestEventNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientSendTestEventNotificationNotificationTypeDef", {"Destination": str}
)
_OptionalClientSendTestEventNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientSendTestEventNotificationNotificationTypeDef",
    {
        "Transport": Literal["Email", "SQS", "SNS"],
        "Version": str,
        "EventTypes": List[
            Literal[
                "AssignmentAccepted",
                "AssignmentAbandoned",
                "AssignmentReturned",
                "AssignmentSubmitted",
                "AssignmentRejected",
                "AssignmentApproved",
                "HITCreated",
                "HITExpired",
                "HITReviewable",
                "HITExtended",
                "HITDisposed",
                "Ping",
            ]
        ],
    },
    total=False,
)


class ClientSendTestEventNotificationNotificationTypeDef(
    _RequiredClientSendTestEventNotificationNotificationTypeDef,
    _OptionalClientSendTestEventNotificationNotificationTypeDef,
):
    """
    The notification specification to test. This value is identical to the value you would provide
    to the UpdateNotificationSettings operation when you establish the notification specification
    for a HIT type.
    - **Destination** *(string) --***[REQUIRED]**

      The target for notification messages. The Destination’s format is determined by the specified
      Transport:
      * When Transport is Email, the Destination is your email address.
      * When Transport is SQS, the Destination is your queue URL.
      * When Transport is SNS, the Destination is the ARN of your topic.
    """


_RequiredClientUpdateNotificationSettingsNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateNotificationSettingsNotificationTypeDef", {"Destination": str}
)
_OptionalClientUpdateNotificationSettingsNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateNotificationSettingsNotificationTypeDef",
    {
        "Transport": Literal["Email", "SQS", "SNS"],
        "Version": str,
        "EventTypes": List[
            Literal[
                "AssignmentAccepted",
                "AssignmentAbandoned",
                "AssignmentReturned",
                "AssignmentSubmitted",
                "AssignmentRejected",
                "AssignmentApproved",
                "HITCreated",
                "HITExpired",
                "HITReviewable",
                "HITExtended",
                "HITDisposed",
                "Ping",
            ]
        ],
    },
    total=False,
)


class ClientUpdateNotificationSettingsNotificationTypeDef(
    _RequiredClientUpdateNotificationSettingsNotificationTypeDef,
    _OptionalClientUpdateNotificationSettingsNotificationTypeDef,
):
    """
    The notification specification for the HIT type.
    - **Destination** *(string) --***[REQUIRED]**

      The target for notification messages. The Destination’s format is determined by the specified
      Transport:
      * When Transport is Email, the Destination is your email address.
      * When Transport is SQS, the Destination is your queue URL.
      * When Transport is SNS, the Destination is the ARN of your topic.
    """


_ClientUpdateQualificationTypeResponseQualificationTypeTypeDef = TypedDict(
    "_ClientUpdateQualificationTypeResponseQualificationTypeTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ClientUpdateQualificationTypeResponseQualificationTypeTypeDef(
    _ClientUpdateQualificationTypeResponseQualificationTypeTypeDef
):
    """
    - **QualificationType** *(dict) --*

      Contains a QualificationType data structure.
      - **QualificationTypeId** *(string) --*

        A unique identifier for the Qualification type. A Qualification type is given a
        Qualification type ID when you call the CreateQualificationType operation.
    """


_ClientUpdateQualificationTypeResponseTypeDef = TypedDict(
    "_ClientUpdateQualificationTypeResponseTypeDef",
    {"QualificationType": ClientUpdateQualificationTypeResponseQualificationTypeTypeDef},
    total=False,
)


class ClientUpdateQualificationTypeResponseTypeDef(_ClientUpdateQualificationTypeResponseTypeDef):
    """
    - *(dict) --*

      - **QualificationType** *(dict) --*

        Contains a QualificationType data structure.
        - **QualificationTypeId** *(string) --*

          A unique identifier for the Qualification type. A Qualification type is given a
          Qualification type ID when you call the CreateQualificationType operation.
    """


_ListAssignmentsForHITPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssignmentsForHITPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssignmentsForHITPaginatePaginationConfigTypeDef(
    _ListAssignmentsForHITPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssignmentsForHITPaginateResponseAssignmentsTypeDef = TypedDict(
    "_ListAssignmentsForHITPaginateResponseAssignmentsTypeDef",
    {
        "AssignmentId": str,
        "WorkerId": str,
        "HITId": str,
        "AssignmentStatus": Literal["Submitted", "Approved", "Rejected"],
        "AutoApprovalTime": datetime,
        "AcceptTime": datetime,
        "SubmitTime": datetime,
        "ApprovalTime": datetime,
        "RejectionTime": datetime,
        "Deadline": datetime,
        "Answer": str,
        "RequesterFeedback": str,
    },
    total=False,
)


class ListAssignmentsForHITPaginateResponseAssignmentsTypeDef(
    _ListAssignmentsForHITPaginateResponseAssignmentsTypeDef
):
    pass


_ListAssignmentsForHITPaginateResponseTypeDef = TypedDict(
    "_ListAssignmentsForHITPaginateResponseTypeDef",
    {
        "NumResults": int,
        "Assignments": List[ListAssignmentsForHITPaginateResponseAssignmentsTypeDef],
    },
    total=False,
)


class ListAssignmentsForHITPaginateResponseTypeDef(_ListAssignmentsForHITPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of assignments on the page in the filtered results list, equivalent to the number
        of assignments returned by this call.
    """


_ListBonusPaymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBonusPaymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBonusPaymentsPaginatePaginationConfigTypeDef(
    _ListBonusPaymentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef = TypedDict(
    "_ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "GrantTime": datetime,
    },
    total=False,
)


class ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef(
    _ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef
):
    pass


_ListBonusPaymentsPaginateResponseTypeDef = TypedDict(
    "_ListBonusPaymentsPaginateResponseTypeDef",
    {
        "NumResults": int,
        "BonusPayments": List[ListBonusPaymentsPaginateResponseBonusPaymentsTypeDef],
    },
    total=False,
)


class ListBonusPaymentsPaginateResponseTypeDef(_ListBonusPaymentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of bonus payments on this page in the filtered results list, equivalent to the
        number of bonus payments being returned by this call.
    """


_ListHITsForQualificationTypePaginatePaginationConfigTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHITsForQualificationTypePaginatePaginationConfigTypeDef(
    _ListHITsForQualificationTypePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef(
    _ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef
):
    pass


_ListHITsForQualificationTypePaginateResponseHITsTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ListHITsForQualificationTypePaginateResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ListHITsForQualificationTypePaginateResponseHITsTypeDef(
    _ListHITsForQualificationTypePaginateResponseHITsTypeDef
):
    pass


_ListHITsForQualificationTypePaginateResponseTypeDef = TypedDict(
    "_ListHITsForQualificationTypePaginateResponseTypeDef",
    {"NumResults": int, "HITs": List[ListHITsForQualificationTypePaginateResponseHITsTypeDef]},
    total=False,
)


class ListHITsForQualificationTypePaginateResponseTypeDef(
    _ListHITsForQualificationTypePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of HITs on this page in the filtered results list, equivalent to the number of
        HITs being returned by this call.
    """


_ListHITsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHITsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHITsPaginatePaginationConfigTypeDef(_ListHITsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ListHITsPaginateResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ListHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ListHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ListHITsPaginateResponseHITsQualificationRequirementsTypeDef(
    _ListHITsPaginateResponseHITsQualificationRequirementsTypeDef
):
    pass


_ListHITsPaginateResponseHITsTypeDef = TypedDict(
    "_ListHITsPaginateResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ListHITsPaginateResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ListHITsPaginateResponseHITsTypeDef(_ListHITsPaginateResponseHITsTypeDef):
    pass


_ListHITsPaginateResponseTypeDef = TypedDict(
    "_ListHITsPaginateResponseTypeDef",
    {"NumResults": int, "HITs": List[ListHITsPaginateResponseHITsTypeDef]},
    total=False,
)


class ListHITsPaginateResponseTypeDef(_ListHITsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of HITs on this page in the filtered results list, equivalent to the number of
        HITs being returned by this call.
    """


_ListQualificationRequestsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQualificationRequestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQualificationRequestsPaginatePaginationConfigTypeDef(
    _ListQualificationRequestsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef = TypedDict(
    "_ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef",
    {
        "QualificationRequestId": str,
        "QualificationTypeId": str,
        "WorkerId": str,
        "Test": str,
        "Answer": str,
        "SubmitTime": datetime,
    },
    total=False,
)


class ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef(
    _ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef
):
    pass


_ListQualificationRequestsPaginateResponseTypeDef = TypedDict(
    "_ListQualificationRequestsPaginateResponseTypeDef",
    {
        "NumResults": int,
        "QualificationRequests": List[
            ListQualificationRequestsPaginateResponseQualificationRequestsTypeDef
        ],
    },
    total=False,
)


class ListQualificationRequestsPaginateResponseTypeDef(
    _ListQualificationRequestsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of Qualification requests on this page in the filtered results list, equivalent
        to the number of Qualification requests being returned by this call.
    """


_ListQualificationTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQualificationTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQualificationTypesPaginatePaginationConfigTypeDef(
    _ListQualificationTypesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListQualificationTypesPaginateResponseQualificationTypesTypeDef = TypedDict(
    "_ListQualificationTypesPaginateResponseQualificationTypesTypeDef",
    {
        "QualificationTypeId": str,
        "CreationTime": datetime,
        "Name": str,
        "Description": str,
        "Keywords": str,
        "QualificationTypeStatus": Literal["Active", "Inactive"],
        "Test": str,
        "TestDurationInSeconds": int,
        "AnswerKey": str,
        "RetryDelayInSeconds": int,
        "IsRequestable": bool,
        "AutoGranted": bool,
        "AutoGrantedValue": int,
    },
    total=False,
)


class ListQualificationTypesPaginateResponseQualificationTypesTypeDef(
    _ListQualificationTypesPaginateResponseQualificationTypesTypeDef
):
    pass


_ListQualificationTypesPaginateResponseTypeDef = TypedDict(
    "_ListQualificationTypesPaginateResponseTypeDef",
    {
        "NumResults": int,
        "QualificationTypes": List[ListQualificationTypesPaginateResponseQualificationTypesTypeDef],
    },
    total=False,
)


class ListQualificationTypesPaginateResponseTypeDef(_ListQualificationTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of Qualification types on this page in the filtered results list, equivalent to
        the number of types this operation returns.
    """


_ListReviewableHITsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListReviewableHITsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListReviewableHITsPaginatePaginationConfigTypeDef(
    _ListReviewableHITsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef(
    _ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
):
    pass


_ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": Literal[
            "LessThan",
            "LessThanOrEqualTo",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "EqualTo",
            "NotEqualTo",
            "Exists",
            "DoesNotExist",
            "In",
            "NotIn",
        ],
        "IntegerValues": List[int],
        "LocaleValues": List[
            ListReviewableHITsPaginateResponseHITsQualificationRequirementsLocaleValuesTypeDef
        ],
        "RequiredToPreview": bool,
        "ActionsGuarded": Literal["Accept", "PreviewAndAccept", "DiscoverPreviewAndAccept"],
    },
    total=False,
)


class ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef(
    _ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef
):
    pass


_ListReviewableHITsPaginateResponseHITsTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseHITsTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
        "HITGroupId": str,
        "HITLayoutId": str,
        "CreationTime": datetime,
        "Title": str,
        "Description": str,
        "Question": str,
        "Keywords": str,
        "HITStatus": Literal["Assignable", "Unassignable", "Reviewable", "Reviewing", "Disposed"],
        "MaxAssignments": int,
        "Reward": str,
        "AutoApprovalDelayInSeconds": int,
        "Expiration": datetime,
        "AssignmentDurationInSeconds": int,
        "RequesterAnnotation": str,
        "QualificationRequirements": List[
            ListReviewableHITsPaginateResponseHITsQualificationRequirementsTypeDef
        ],
        "HITReviewStatus": Literal[
            "NotReviewed", "MarkedForReview", "ReviewedAppropriate", "ReviewedInappropriate"
        ],
        "NumberOfAssignmentsPending": int,
        "NumberOfAssignmentsAvailable": int,
        "NumberOfAssignmentsCompleted": int,
    },
    total=False,
)


class ListReviewableHITsPaginateResponseHITsTypeDef(_ListReviewableHITsPaginateResponseHITsTypeDef):
    pass


_ListReviewableHITsPaginateResponseTypeDef = TypedDict(
    "_ListReviewableHITsPaginateResponseTypeDef",
    {"NumResults": int, "HITs": List[ListReviewableHITsPaginateResponseHITsTypeDef]},
    total=False,
)


class ListReviewableHITsPaginateResponseTypeDef(_ListReviewableHITsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of HITs on this page in the filtered results list, equivalent to the number of
        HITs being returned by this call.
    """


_ListWorkerBlocksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListWorkerBlocksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWorkerBlocksPaginatePaginationConfigTypeDef(
    _ListWorkerBlocksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef = TypedDict(
    "_ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef",
    {"WorkerId": str, "Reason": str},
    total=False,
)


class ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef(
    _ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef
):
    pass


_ListWorkerBlocksPaginateResponseTypeDef = TypedDict(
    "_ListWorkerBlocksPaginateResponseTypeDef",
    {"NumResults": int, "WorkerBlocks": List[ListWorkerBlocksPaginateResponseWorkerBlocksTypeDef]},
    total=False,
)


class ListWorkerBlocksPaginateResponseTypeDef(_ListWorkerBlocksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of assignments on the page in the filtered results list, equivalent to the number
        of assignments returned by this call.
    """


_ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef(
    _ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef",
    {"Country": str, "Subdivision": str},
    total=False,
)


class ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef(
    _ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef
):
    pass


_ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "GrantTime": datetime,
        "IntegerValue": int,
        "LocaleValue": ListWorkersWithQualificationTypePaginateResponseQualificationsLocaleValueTypeDef,
        "Status": Literal["Granted", "Revoked"],
    },
    total=False,
)


class ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef(
    _ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef
):
    pass


_ListWorkersWithQualificationTypePaginateResponseTypeDef = TypedDict(
    "_ListWorkersWithQualificationTypePaginateResponseTypeDef",
    {
        "NumResults": int,
        "Qualifications": List[
            ListWorkersWithQualificationTypePaginateResponseQualificationsTypeDef
        ],
    },
    total=False,
)


class ListWorkersWithQualificationTypePaginateResponseTypeDef(
    _ListWorkersWithQualificationTypePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **NumResults** *(integer) --*

        The number of Qualifications on this page in the filtered results list, equivalent to the
        number of Qualifications being returned by this call.
    """
