"Main interface for support service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientAddAttachmentsToSetAttachmentsTypeDef",
    "ClientAddAttachmentsToSetResponseTypeDef",
    "ClientAddCommunicationToCaseResponseTypeDef",
    "ClientCreateCaseResponseTypeDef",
    "ClientDescribeAttachmentResponseattachmentTypeDef",
    "ClientDescribeAttachmentResponseTypeDef",
    "ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    "ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef",
    "ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef",
    "ClientDescribeCasesResponsecasesTypeDef",
    "ClientDescribeCasesResponseTypeDef",
    "ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef",
    "ClientDescribeCommunicationsResponsecommunicationsTypeDef",
    "ClientDescribeCommunicationsResponseTypeDef",
    "ClientDescribeServicesResponseservicescategoriesTypeDef",
    "ClientDescribeServicesResponseservicesTypeDef",
    "ClientDescribeServicesResponseTypeDef",
    "ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef",
    "ClientDescribeSeverityLevelsResponseTypeDef",
    "ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef",
    "ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef",
    "ClientDescribeTrustedAdvisorCheckResultResponseTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef",
    "ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef",
    "ClientDescribeTrustedAdvisorChecksResponseTypeDef",
    "ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef",
    "ClientRefreshTrustedAdvisorCheckResponseTypeDef",
    "ClientResolveCaseResponseTypeDef",
    "DescribeCasesPaginatePaginationConfigTypeDef",
    "DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    "DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef",
    "DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef",
    "DescribeCasesPaginateResponsecasesTypeDef",
    "DescribeCasesPaginateResponseTypeDef",
    "DescribeCommunicationsPaginatePaginationConfigTypeDef",
    "DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef",
    "DescribeCommunicationsPaginateResponsecommunicationsTypeDef",
    "DescribeCommunicationsPaginateResponseTypeDef",
)


_ClientAddAttachmentsToSetAttachmentsTypeDef = TypedDict(
    "_ClientAddAttachmentsToSetAttachmentsTypeDef", {"fileName": str, "data": bytes}, total=False
)


class ClientAddAttachmentsToSetAttachmentsTypeDef(_ClientAddAttachmentsToSetAttachmentsTypeDef):
    """
    - *(dict) --*

      An attachment to a case communication. The attachment consists of the file name and the
      content of the file.
      - **fileName** *(string) --*

        The name of the attachment file.
    """


_ClientAddAttachmentsToSetResponseTypeDef = TypedDict(
    "_ClientAddAttachmentsToSetResponseTypeDef",
    {"attachmentSetId": str, "expiryTime": str},
    total=False,
)


class ClientAddAttachmentsToSetResponseTypeDef(_ClientAddAttachmentsToSetResponseTypeDef):
    """
    - *(dict) --*

      The ID and expiry time of the attachment set returned by the  AddAttachmentsToSet operation.
      - **attachmentSetId** *(string) --*

        The ID of the attachment set. If an ``attachmentSetId`` was not specified, a new attachment
        set is created, and the ID of the set is returned in the response. If an ``attachmentSetId``
        was specified, the attachments are added to the specified set, if it exists.
    """


_ClientAddCommunicationToCaseResponseTypeDef = TypedDict(
    "_ClientAddCommunicationToCaseResponseTypeDef", {"result": bool}, total=False
)


class ClientAddCommunicationToCaseResponseTypeDef(_ClientAddCommunicationToCaseResponseTypeDef):
    """
    - *(dict) --*

      The result of the  AddCommunicationToCase operation.
      - **result** *(boolean) --*

        True if  AddCommunicationToCase succeeds. Otherwise, returns an error.
    """


_ClientCreateCaseResponseTypeDef = TypedDict(
    "_ClientCreateCaseResponseTypeDef", {"caseId": str}, total=False
)


class ClientCreateCaseResponseTypeDef(_ClientCreateCaseResponseTypeDef):
    """
    - *(dict) --*

      The AWS Support case ID returned by a successful completion of the  CreateCase operation.
      - **caseId** *(string) --*

        The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
        string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_ClientDescribeAttachmentResponseattachmentTypeDef = TypedDict(
    "_ClientDescribeAttachmentResponseattachmentTypeDef",
    {"fileName": str, "data": bytes},
    total=False,
)


class ClientDescribeAttachmentResponseattachmentTypeDef(
    _ClientDescribeAttachmentResponseattachmentTypeDef
):
    """
    - **attachment** *(dict) --*

      The attachment content and file name.
      - **fileName** *(string) --*

        The name of the attachment file.
    """


_ClientDescribeAttachmentResponseTypeDef = TypedDict(
    "_ClientDescribeAttachmentResponseTypeDef",
    {"attachment": ClientDescribeAttachmentResponseattachmentTypeDef},
    total=False,
)


class ClientDescribeAttachmentResponseTypeDef(_ClientDescribeAttachmentResponseTypeDef):
    """
    - *(dict) --*

      The content and file name of the attachment returned by the  DescribeAttachment operation.
      - **attachment** *(dict) --*

        The attachment content and file name.
        - **fileName** *(string) --*

          The name of the attachment file.
    """


_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef(
    _ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
):
    pass


_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef(
    _ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef
):
    pass


_ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef",
    {
        "communications": List[
            ClientDescribeCasesResponsecasesrecentCommunicationscommunicationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef(
    _ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef
):
    pass


_ClientDescribeCasesResponsecasesTypeDef = TypedDict(
    "_ClientDescribeCasesResponsecasesTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": ClientDescribeCasesResponsecasesrecentCommunicationsTypeDef,
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)


class ClientDescribeCasesResponsecasesTypeDef(_ClientDescribeCasesResponsecasesTypeDef):
    """
    - *(dict) --*

      A JSON-formatted object that contains the metadata for a support case. It is contained the
      response from a  DescribeCases request. **CaseDetails** contains the following fields:
      * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an
      alphanumeric string formatted as shown in this example:
      case-*12345678910-2013-c4c1d2bf33c5cf47* .
      * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the
      CategoryCode values returned by a call to  DescribeServices .
      * **displayId.** The identifier for the case on pages in the AWS Support Center.
      * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS Support
      currently supports English ("en") and Japanese ("ja"). Language parameters must be passed
      explicitly for operations that take them.
      * **recentCommunications.** One or more  Communication objects. Fields of these objects are
      ``attachments`` , ``body`` , ``caseId`` , ``submittedBy`` , and ``timeCreated`` .
      * **nextToken.** A resumption point for pagination.
      * **serviceCode.** The identifier for the AWS service that corresponds to the service code
      defined in the call to  DescribeServices .
      * **severityCode.** The severity code assigned to the case. Contains one of the values
      returned by the call to  DescribeSeverityLevels . The possible values are: ``low`` ,
      ``normal`` , ``high`` , ``urgent`` , and ``critical`` .
      * **status.** The status of the case in the AWS Support Center. The possible values are:
      ``resolved`` , ``pending-customer-action`` , ``opened`` , ``unassigned`` , and
      ``work-in-progress`` .
      * **subject.** The subject line of the case.
      * **submittedBy.** The email address of the account that submitted the case.
      * **timeCreated.** The time the case was created, in ISO-8601 format.
      - **caseId** *(string) --*

        The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
        string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_ClientDescribeCasesResponseTypeDef = TypedDict(
    "_ClientDescribeCasesResponseTypeDef",
    {"cases": List[ClientDescribeCasesResponsecasesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeCasesResponseTypeDef(_ClientDescribeCasesResponseTypeDef):
    """
    - *(dict) --*

      Returns an array of  CaseDetails objects and a ``nextToken`` that defines a point for
      pagination in the result set.
      - **cases** *(list) --*

        The details for the cases that match the request.
        - *(dict) --*

          A JSON-formatted object that contains the metadata for a support case. It is contained the
          response from a  DescribeCases request. **CaseDetails** contains the following fields:
          * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an
          alphanumeric string formatted as shown in this example:
          case-*12345678910-2013-c4c1d2bf33c5cf47* .
          * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the
          CategoryCode values returned by a call to  DescribeServices .
          * **displayId.** The identifier for the case on pages in the AWS Support Center.
          * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS
          Support currently supports English ("en") and Japanese ("ja"). Language parameters must be
          passed explicitly for operations that take them.
          * **recentCommunications.** One or more  Communication objects. Fields of these objects
          are ``attachments`` , ``body`` , ``caseId`` , ``submittedBy`` , and ``timeCreated`` .
          * **nextToken.** A resumption point for pagination.
          * **serviceCode.** The identifier for the AWS service that corresponds to the service code
          defined in the call to  DescribeServices .
          * **severityCode.** The severity code assigned to the case. Contains one of the values
          returned by the call to  DescribeSeverityLevels . The possible values are: ``low`` ,
          ``normal`` , ``high`` , ``urgent`` , and ``critical`` .
          * **status.** The status of the case in the AWS Support Center. The possible values are:
          ``resolved`` , ``pending-customer-action`` , ``opened`` , ``unassigned`` , and
          ``work-in-progress`` .
          * **subject.** The subject line of the case.
          * **submittedBy.** The email address of the account that submitted the case.
          * **timeCreated.** The time the case was created, in ISO-8601 format.
          - **caseId** *(string) --*

            The AWS Support case ID requested or returned in the call. The case ID is an
            alphanumeric string formatted as shown in this example:
            case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef = TypedDict(
    "_ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef(
    _ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef
):
    pass


_ClientDescribeCommunicationsResponsecommunicationsTypeDef = TypedDict(
    "_ClientDescribeCommunicationsResponsecommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            ClientDescribeCommunicationsResponsecommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCommunicationsResponsecommunicationsTypeDef(
    _ClientDescribeCommunicationsResponsecommunicationsTypeDef
):
    """
    - *(dict) --*

      A communication associated with an AWS Support case. The communication consists of the case
      ID, the message body, attachment information, the submitter of the communication, and the date
      and time of the communication.
      - **caseId** *(string) --*

        The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
        string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_ClientDescribeCommunicationsResponseTypeDef = TypedDict(
    "_ClientDescribeCommunicationsResponseTypeDef",
    {
        "communications": List[ClientDescribeCommunicationsResponsecommunicationsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeCommunicationsResponseTypeDef(_ClientDescribeCommunicationsResponseTypeDef):
    """
    - *(dict) --*

      The communications returned by the  DescribeCommunications operation.
      - **communications** *(list) --*

        The communications for the case.
        - *(dict) --*

          A communication associated with an AWS Support case. The communication consists of the
          case ID, the message body, attachment information, the submitter of the communication, and
          the date and time of the communication.
          - **caseId** *(string) --*

            The AWS Support case ID requested or returned in the call. The case ID is an
            alphanumeric string formatted as shown in this example:
            case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_ClientDescribeServicesResponseservicescategoriesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicescategoriesTypeDef",
    {"code": str, "name": str},
    total=False,
)


class ClientDescribeServicesResponseservicescategoriesTypeDef(
    _ClientDescribeServicesResponseservicescategoriesTypeDef
):
    pass


_ClientDescribeServicesResponseservicesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesTypeDef",
    {
        "code": str,
        "name": str,
        "categories": List[ClientDescribeServicesResponseservicescategoriesTypeDef],
    },
    total=False,
)


class ClientDescribeServicesResponseservicesTypeDef(_ClientDescribeServicesResponseservicesTypeDef):
    """
    - *(dict) --*

      Information about an AWS service returned by the  DescribeServices operation.
      - **code** *(string) --*

        The code for an AWS service returned by the  DescribeServices response. The ``name`` element
        contains the corresponding friendly name.
    """


_ClientDescribeServicesResponseTypeDef = TypedDict(
    "_ClientDescribeServicesResponseTypeDef",
    {"services": List[ClientDescribeServicesResponseservicesTypeDef]},
    total=False,
)


class ClientDescribeServicesResponseTypeDef(_ClientDescribeServicesResponseTypeDef):
    """
    - *(dict) --*

      The list of AWS services returned by the  DescribeServices operation.
      - **services** *(list) --*

        A JSON-formatted list of AWS services.
        - *(dict) --*

          Information about an AWS service returned by the  DescribeServices operation.
          - **code** *(string) --*

            The code for an AWS service returned by the  DescribeServices response. The ``name``
            element contains the corresponding friendly name.
    """


_ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef = TypedDict(
    "_ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef",
    {"code": str, "name": str},
    total=False,
)


class ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef(
    _ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef
):
    """
    - *(dict) --*

      A code and name pair that represents the severity level of a support case. The available
      values depend on the support plan for the account. For more information, see `Choosing a
      Severity
      <https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity>`__
      .
      - **code** *(string) --*

        The code for case severity level.
        Valid values: ``low`` | ``normal`` | ``high`` | ``urgent`` | ``critical``
    """


_ClientDescribeSeverityLevelsResponseTypeDef = TypedDict(
    "_ClientDescribeSeverityLevelsResponseTypeDef",
    {"severityLevels": List[ClientDescribeSeverityLevelsResponseseverityLevelsTypeDef]},
    total=False,
)


class ClientDescribeSeverityLevelsResponseTypeDef(_ClientDescribeSeverityLevelsResponseTypeDef):
    """
    - *(dict) --*

      The list of severity levels returned by the  DescribeSeverityLevels operation.
      - **severityLevels** *(list) --*

        The available severity levels for the support case. Available severity levels are defined by
        your service level agreement with AWS.
        - *(dict) --*

          A code and name pair that represents the severity level of a support case. The available
          values depend on the support plan for the account. For more information, see `Choosing a
          Severity
          <https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity>`__
          .
          - **code** *(string) --*

            The code for case severity level.
            Valid values: ``low`` | ``normal`` | ``high`` | ``urgent`` | ``critical``
    """


_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef",
    {"checkId": str, "status": str, "millisUntilNextRefreshable": int},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef(
    _ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef
):
    """
    - *(dict) --*

      The refresh status of a Trusted Advisor check.
      - **checkId** *(string) --*

        The unique identifier for the Trusted Advisor check.
    """


_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    {"statuses": List[ClientDescribeTrustedAdvisorCheckRefreshStatusesResponsestatusesTypeDef]},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef(
    _ClientDescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef
):
    """
    - *(dict) --*

      The statuses of the Trusted Advisor checks returned by the
      DescribeTrustedAdvisorCheckRefreshStatuses operation.
      - **statuses** *(list) --*

        The refresh status of the specified Trusted Advisor checks.
        - *(dict) --*

          The refresh status of a Trusted Advisor check.
          - **checkId** *(string) --*

            The unique identifier for the Trusted Advisor check.
    """


_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef",
    {"estimatedMonthlySavings": float, "estimatedPercentMonthlySavings": float},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef
):
    pass


_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef",
    {
        "costOptimizing": ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummarycostOptimizingTypeDef
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef
):
    pass


_ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef",
    {"status": str, "region": str, "resourceId": str, "isSuppressed": bool, "metadata": List[str]},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef
):
    pass


_ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef
):
    pass


_ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": ClientDescribeTrustedAdvisorCheckResultResponseresultresourcesSummaryTypeDef,
        "categorySpecificSummary": ClientDescribeTrustedAdvisorCheckResultResponseresultcategorySpecificSummaryTypeDef,
        "flaggedResources": List[
            ClientDescribeTrustedAdvisorCheckResultResponseresultflaggedResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef
):
    """
    - **result** *(dict) --*

      The detailed results of the Trusted Advisor check.
      - **checkId** *(string) --*

        The unique identifier for the Trusted Advisor check.
    """


_ClientDescribeTrustedAdvisorCheckResultResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckResultResponseTypeDef",
    {"result": ClientDescribeTrustedAdvisorCheckResultResponseresultTypeDef},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckResultResponseTypeDef(
    _ClientDescribeTrustedAdvisorCheckResultResponseTypeDef
):
    """
    - *(dict) --*

      The result of the Trusted Advisor check returned by the  DescribeTrustedAdvisorCheckResult
      operation.
      - **result** *(dict) --*

        The detailed results of the Trusted Advisor check.
        - **checkId** *(string) --*

          The unique identifier for the Trusted Advisor check.
    """


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef",
    {"estimatedMonthlySavings": float, "estimatedPercentMonthlySavings": float},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef
):
    pass


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef",
    {
        "costOptimizing": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummarycostOptimizingTypeDef
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef
):
    pass


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef
):
    pass


_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "hasFlaggedResources": bool,
        "resourcesSummary": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesresourcesSummaryTypeDef,
        "categorySpecificSummary": ClientDescribeTrustedAdvisorCheckSummariesResponsesummariescategorySpecificSummaryTypeDef,
    },
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef
):
    """
    - *(dict) --*

      A summary of a Trusted Advisor check result, including the alert status, last refresh, and
      number of resources examined.
      - **checkId** *(string) --*

        The unique identifier for the Trusted Advisor check.
    """


_ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    {"summaries": List[ClientDescribeTrustedAdvisorCheckSummariesResponsesummariesTypeDef]},
    total=False,
)


class ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef(
    _ClientDescribeTrustedAdvisorCheckSummariesResponseTypeDef
):
    """
    - *(dict) --*

      The summaries of the Trusted Advisor checks returned by the
      DescribeTrustedAdvisorCheckSummaries operation.
      - **summaries** *(list) --*

        The summary information for the requested Trusted Advisor checks.
        - *(dict) --*

          A summary of a Trusted Advisor check result, including the alert status, last refresh, and
          number of resources examined.
          - **checkId** *(string) --*

            The unique identifier for the Trusted Advisor check.
    """


_ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef",
    {"id": str, "name": str, "description": str, "category": str, "metadata": List[str]},
    total=False,
)


class ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef(
    _ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef
):
    """
    - *(dict) --*

      The description and metadata for a Trusted Advisor check.
      - **id** *(string) --*

        The unique identifier for the Trusted Advisor check.
    """


_ClientDescribeTrustedAdvisorChecksResponseTypeDef = TypedDict(
    "_ClientDescribeTrustedAdvisorChecksResponseTypeDef",
    {"checks": List[ClientDescribeTrustedAdvisorChecksResponsechecksTypeDef]},
    total=False,
)


class ClientDescribeTrustedAdvisorChecksResponseTypeDef(
    _ClientDescribeTrustedAdvisorChecksResponseTypeDef
):
    """
    - *(dict) --*

      Information about the Trusted Advisor checks returned by the  DescribeTrustedAdvisorChecks
      operation.
      - **checks** *(list) --*

        Information about all available Trusted Advisor checks.
        - *(dict) --*

          The description and metadata for a Trusted Advisor check.
          - **id** *(string) --*

            The unique identifier for the Trusted Advisor check.
    """


_ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef = TypedDict(
    "_ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef",
    {"checkId": str, "status": str, "millisUntilNextRefreshable": int},
    total=False,
)


class ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef(
    _ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef
):
    """
    - **status** *(dict) --*

      The current refresh status for a check, including the amount of time until the check is
      eligible for refresh.
      - **checkId** *(string) --*

        The unique identifier for the Trusted Advisor check.
    """


_ClientRefreshTrustedAdvisorCheckResponseTypeDef = TypedDict(
    "_ClientRefreshTrustedAdvisorCheckResponseTypeDef",
    {"status": ClientRefreshTrustedAdvisorCheckResponsestatusTypeDef},
    total=False,
)


class ClientRefreshTrustedAdvisorCheckResponseTypeDef(
    _ClientRefreshTrustedAdvisorCheckResponseTypeDef
):
    """
    - *(dict) --*

      The current refresh status of a Trusted Advisor check.
      - **status** *(dict) --*

        The current refresh status for a check, including the amount of time until the check is
        eligible for refresh.
        - **checkId** *(string) --*

          The unique identifier for the Trusted Advisor check.
    """


_ClientResolveCaseResponseTypeDef = TypedDict(
    "_ClientResolveCaseResponseTypeDef",
    {"initialCaseStatus": str, "finalCaseStatus": str},
    total=False,
)


class ClientResolveCaseResponseTypeDef(_ClientResolveCaseResponseTypeDef):
    """
    - *(dict) --*

      The status of the case returned by the  ResolveCase operation.
      - **initialCaseStatus** *(string) --*

        The status of the case when the  ResolveCase request was sent.
    """


_DescribeCasesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCasesPaginatePaginationConfigTypeDef(_DescribeCasesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef(
    _DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
):
    pass


_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef(
    _DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef
):
    pass


_DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef",
    {
        "communications": List[
            DescribeCasesPaginateResponsecasesrecentCommunicationscommunicationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef(
    _DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef
):
    pass


_DescribeCasesPaginateResponsecasesTypeDef = TypedDict(
    "_DescribeCasesPaginateResponsecasesTypeDef",
    {
        "caseId": str,
        "displayId": str,
        "subject": str,
        "status": str,
        "serviceCode": str,
        "categoryCode": str,
        "severityCode": str,
        "submittedBy": str,
        "timeCreated": str,
        "recentCommunications": DescribeCasesPaginateResponsecasesrecentCommunicationsTypeDef,
        "ccEmailAddresses": List[str],
        "language": str,
    },
    total=False,
)


class DescribeCasesPaginateResponsecasesTypeDef(_DescribeCasesPaginateResponsecasesTypeDef):
    """
    - *(dict) --*

      A JSON-formatted object that contains the metadata for a support case. It is contained the
      response from a  DescribeCases request. **CaseDetails** contains the following fields:
      * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an
      alphanumeric string formatted as shown in this example:
      case-*12345678910-2013-c4c1d2bf33c5cf47* .
      * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the
      CategoryCode values returned by a call to  DescribeServices .
      * **displayId.** The identifier for the case on pages in the AWS Support Center.
      * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS Support
      currently supports English ("en") and Japanese ("ja"). Language parameters must be passed
      explicitly for operations that take them.
      * **recentCommunications.** One or more  Communication objects. Fields of these objects are
      ``attachments`` , ``body`` , ``caseId`` , ``submittedBy`` , and ``timeCreated`` .
      * **nextToken.** A resumption point for pagination.
      * **serviceCode.** The identifier for the AWS service that corresponds to the service code
      defined in the call to  DescribeServices .
      * **severityCode.** The severity code assigned to the case. Contains one of the values
      returned by the call to  DescribeSeverityLevels . The possible values are: ``low`` ,
      ``normal`` , ``high`` , ``urgent`` , and ``critical`` .
      * **status.** The status of the case in the AWS Support Center. The possible values are:
      ``resolved`` , ``pending-customer-action`` , ``opened`` , ``unassigned`` , and
      ``work-in-progress`` .
      * **subject.** The subject line of the case.
      * **submittedBy.** The email address of the account that submitted the case.
      * **timeCreated.** The time the case was created, in ISO-8601 format.
      - **caseId** *(string) --*

        The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
        string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_DescribeCasesPaginateResponseTypeDef = TypedDict(
    "_DescribeCasesPaginateResponseTypeDef",
    {"cases": List[DescribeCasesPaginateResponsecasesTypeDef], "NextToken": str},
    total=False,
)


class DescribeCasesPaginateResponseTypeDef(_DescribeCasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Returns an array of  CaseDetails objects and a ``nextToken`` that defines a point for
      pagination in the result set.
      - **cases** *(list) --*

        The details for the cases that match the request.
        - *(dict) --*

          A JSON-formatted object that contains the metadata for a support case. It is contained the
          response from a  DescribeCases request. **CaseDetails** contains the following fields:
          * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an
          alphanumeric string formatted as shown in this example:
          case-*12345678910-2013-c4c1d2bf33c5cf47* .
          * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the
          CategoryCode values returned by a call to  DescribeServices .
          * **displayId.** The identifier for the case on pages in the AWS Support Center.
          * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS
          Support currently supports English ("en") and Japanese ("ja"). Language parameters must be
          passed explicitly for operations that take them.
          * **recentCommunications.** One or more  Communication objects. Fields of these objects
          are ``attachments`` , ``body`` , ``caseId`` , ``submittedBy`` , and ``timeCreated`` .
          * **nextToken.** A resumption point for pagination.
          * **serviceCode.** The identifier for the AWS service that corresponds to the service code
          defined in the call to  DescribeServices .
          * **severityCode.** The severity code assigned to the case. Contains one of the values
          returned by the call to  DescribeSeverityLevels . The possible values are: ``low`` ,
          ``normal`` , ``high`` , ``urgent`` , and ``critical`` .
          * **status.** The status of the case in the AWS Support Center. The possible values are:
          ``resolved`` , ``pending-customer-action`` , ``opened`` , ``unassigned`` , and
          ``work-in-progress`` .
          * **subject.** The subject line of the case.
          * **submittedBy.** The email address of the account that submitted the case.
          * **timeCreated.** The time the case was created, in ISO-8601 format.
          - **caseId** *(string) --*

            The AWS Support case ID requested or returned in the call. The case ID is an
            alphanumeric string formatted as shown in this example:
            case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_DescribeCommunicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCommunicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCommunicationsPaginatePaginationConfigTypeDef(
    _DescribeCommunicationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef = TypedDict(
    "_DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef",
    {"attachmentId": str, "fileName": str},
    total=False,
)


class DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef(
    _DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef
):
    pass


_DescribeCommunicationsPaginateResponsecommunicationsTypeDef = TypedDict(
    "_DescribeCommunicationsPaginateResponsecommunicationsTypeDef",
    {
        "caseId": str,
        "body": str,
        "submittedBy": str,
        "timeCreated": str,
        "attachmentSet": List[
            DescribeCommunicationsPaginateResponsecommunicationsattachmentSetTypeDef
        ],
    },
    total=False,
)


class DescribeCommunicationsPaginateResponsecommunicationsTypeDef(
    _DescribeCommunicationsPaginateResponsecommunicationsTypeDef
):
    """
    - *(dict) --*

      A communication associated with an AWS Support case. The communication consists of the case
      ID, the message body, attachment information, the submitter of the communication, and the date
      and time of the communication.
      - **caseId** *(string) --*

        The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric
        string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*
    """


_DescribeCommunicationsPaginateResponseTypeDef = TypedDict(
    "_DescribeCommunicationsPaginateResponseTypeDef",
    {
        "communications": List[DescribeCommunicationsPaginateResponsecommunicationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeCommunicationsPaginateResponseTypeDef(_DescribeCommunicationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The communications returned by the  DescribeCommunications operation.
      - **communications** *(list) --*

        The communications for the case.
        - *(dict) --*

          A communication associated with an AWS Support case. The communication consists of the
          case ID, the message body, attachment information, the submitter of the communication, and
          the date and time of the communication.
          - **caseId** *(string) --*

            The AWS Support case ID requested or returned in the call. The case ID is an
            alphanumeric string formatted as shown in this example:
            case-*12345678910-2013-c4c1d2bf33c5cf47*
    """
