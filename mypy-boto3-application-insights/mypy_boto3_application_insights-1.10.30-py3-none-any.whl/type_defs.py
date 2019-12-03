"Main interface for application-insights service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateApplicationResponseApplicationInfoTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientCreateLogPatternResponseLogPatternTypeDef",
    "ClientCreateLogPatternResponseTypeDef",
    "ClientDescribeApplicationResponseApplicationInfoTypeDef",
    "ClientDescribeApplicationResponseTypeDef",
    "ClientDescribeComponentConfigurationRecommendationResponseTypeDef",
    "ClientDescribeComponentConfigurationResponseTypeDef",
    "ClientDescribeComponentResponseApplicationComponentTypeDef",
    "ClientDescribeComponentResponseTypeDef",
    "ClientDescribeLogPatternResponseLogPatternTypeDef",
    "ClientDescribeLogPatternResponseTypeDef",
    "ClientDescribeObservationResponseObservationTypeDef",
    "ClientDescribeObservationResponseTypeDef",
    "ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef",
    "ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef",
    "ClientDescribeProblemObservationsResponseTypeDef",
    "ClientDescribeProblemResponseProblemTypeDef",
    "ClientDescribeProblemResponseTypeDef",
    "ClientListApplicationsResponseApplicationInfoListTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListComponentsResponseApplicationComponentListTypeDef",
    "ClientListComponentsResponseTypeDef",
    "ClientListLogPatternSetsResponseTypeDef",
    "ClientListLogPatternsResponseLogPatternsTypeDef",
    "ClientListLogPatternsResponseTypeDef",
    "ClientListProblemsResponseProblemListTypeDef",
    "ClientListProblemsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateApplicationResponseApplicationInfoTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ClientUpdateLogPatternResponseLogPatternTypeDef",
    "ClientUpdateLogPatternResponseTypeDef",
)


_ClientCreateApplicationResponseApplicationInfoTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationInfoTypeDef(
    _ClientCreateApplicationResponseApplicationInfoTypeDef
):
    """
    - **ApplicationInfo** *(dict) --*

      Information about the application.
      - **ResourceGroupName** *(string) --*

        The name of the resource group used for the application.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {"ApplicationInfo": ClientCreateApplicationResponseApplicationInfoTypeDef},
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationInfo** *(dict) --*

        Information about the application.
        - **ResourceGroupName** *(string) --*

          The name of the resource group used for the application.
    """


_RequiredClientCreateApplicationTagsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationTagsTypeDef", {"Key": str}
)
_OptionalClientCreateApplicationTagsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(
    _RequiredClientCreateApplicationTagsTypeDef, _OptionalClientCreateApplicationTagsTypeDef
):
    """
    - *(dict) --*

      An object that defines the tags associated with an application. A *tag* is a label that you
      optionally define and associate with an application. Tags can help you categorize and manage
      resources in different ways, such as by purpose, owner, environment, or other criteria.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientCreateLogPatternResponseLogPatternTypeDef = TypedDict(
    "_ClientCreateLogPatternResponseLogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)


class ClientCreateLogPatternResponseLogPatternTypeDef(
    _ClientCreateLogPatternResponseLogPatternTypeDef
):
    """
    - **LogPattern** *(dict) --*

      The successfully created log pattern.
      - **PatternSetName** *(string) --*

        The name of the log pattern. A log pattern name can contains at many as 30 characters, and
        it cannot be empty. The characters can be Unicode letters, digits or one of the following
        symbols: period, dash, underscore.
    """


_ClientCreateLogPatternResponseTypeDef = TypedDict(
    "_ClientCreateLogPatternResponseTypeDef",
    {"LogPattern": ClientCreateLogPatternResponseLogPatternTypeDef, "ResourceGroupName": str},
    total=False,
)


class ClientCreateLogPatternResponseTypeDef(_ClientCreateLogPatternResponseTypeDef):
    """
    - *(dict) --*

      - **LogPattern** *(dict) --*

        The successfully created log pattern.
        - **PatternSetName** *(string) --*

          The name of the log pattern. A log pattern name can contains at many as 30 characters, and
          it cannot be empty. The characters can be Unicode letters, digits or one of the following
          symbols: period, dash, underscore.
    """


_ClientDescribeApplicationResponseApplicationInfoTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationInfoTypeDef(
    _ClientDescribeApplicationResponseApplicationInfoTypeDef
):
    """
    - **ApplicationInfo** *(dict) --*

      Information about the application.
      - **ResourceGroupName** *(string) --*

        The name of the resource group used for the application.
    """


_ClientDescribeApplicationResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseTypeDef",
    {"ApplicationInfo": ClientDescribeApplicationResponseApplicationInfoTypeDef},
    total=False,
)


class ClientDescribeApplicationResponseTypeDef(_ClientDescribeApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationInfo** *(dict) --*

        Information about the application.
        - **ResourceGroupName** *(string) --*

          The name of the resource group used for the application.
    """


_ClientDescribeComponentConfigurationRecommendationResponseTypeDef = TypedDict(
    "_ClientDescribeComponentConfigurationRecommendationResponseTypeDef",
    {"ComponentConfiguration": str},
    total=False,
)


class ClientDescribeComponentConfigurationRecommendationResponseTypeDef(
    _ClientDescribeComponentConfigurationRecommendationResponseTypeDef
):
    """
    - *(dict) --*

      - **ComponentConfiguration** *(string) --*

        The recommended configuration settings of the component. The value is the escaped JSON of
        the configuration.
    """


_ClientDescribeComponentConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeComponentConfigurationResponseTypeDef",
    {
        "Monitor": bool,
        "Tier": Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
        "ComponentConfiguration": str,
    },
    total=False,
)


class ClientDescribeComponentConfigurationResponseTypeDef(
    _ClientDescribeComponentConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **Monitor** *(boolean) --*

        Indicates whether the application component is monitored.
    """


_ClientDescribeComponentResponseApplicationComponentTypeDef = TypedDict(
    "_ClientDescribeComponentResponseApplicationComponentTypeDef",
    {
        "ComponentName": str,
        "ResourceType": str,
        "Tier": Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
        "Monitor": bool,
    },
    total=False,
)


class ClientDescribeComponentResponseApplicationComponentTypeDef(
    _ClientDescribeComponentResponseApplicationComponentTypeDef
):
    """
    - **ApplicationComponent** *(dict) --*

      Describes a standalone resource or similarly grouped resources that the application is made up
      of.
      - **ComponentName** *(string) --*

        The name of the component.
    """


_ClientDescribeComponentResponseTypeDef = TypedDict(
    "_ClientDescribeComponentResponseTypeDef",
    {
        "ApplicationComponent": ClientDescribeComponentResponseApplicationComponentTypeDef,
        "ResourceList": List[str],
    },
    total=False,
)


class ClientDescribeComponentResponseTypeDef(_ClientDescribeComponentResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationComponent** *(dict) --*

        Describes a standalone resource or similarly grouped resources that the application is made
        up of.
        - **ComponentName** *(string) --*

          The name of the component.
    """


_ClientDescribeLogPatternResponseLogPatternTypeDef = TypedDict(
    "_ClientDescribeLogPatternResponseLogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)


class ClientDescribeLogPatternResponseLogPatternTypeDef(
    _ClientDescribeLogPatternResponseLogPatternTypeDef
):
    pass


_ClientDescribeLogPatternResponseTypeDef = TypedDict(
    "_ClientDescribeLogPatternResponseTypeDef",
    {"ResourceGroupName": str, "LogPattern": ClientDescribeLogPatternResponseLogPatternTypeDef},
    total=False,
)


class ClientDescribeLogPatternResponseTypeDef(_ClientDescribeLogPatternResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceGroupName** *(string) --*

        The name of the resource group.
    """


_ClientDescribeObservationResponseObservationTypeDef = TypedDict(
    "_ClientDescribeObservationResponseObservationTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": Literal["ERROR", "WARN", "INFO"],
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
    },
    total=False,
)


class ClientDescribeObservationResponseObservationTypeDef(
    _ClientDescribeObservationResponseObservationTypeDef
):
    """
    - **Observation** *(dict) --*

      Information about the observation.
      - **Id** *(string) --*

        The ID of the observation type.
    """


_ClientDescribeObservationResponseTypeDef = TypedDict(
    "_ClientDescribeObservationResponseTypeDef",
    {"Observation": ClientDescribeObservationResponseObservationTypeDef},
    total=False,
)


class ClientDescribeObservationResponseTypeDef(_ClientDescribeObservationResponseTypeDef):
    """
    - *(dict) --*

      - **Observation** *(dict) --*

        Information about the observation.
        - **Id** *(string) --*

          The ID of the observation type.
    """


_ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef = TypedDict(
    "_ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": Literal["ERROR", "WARN", "INFO"],
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
    },
    total=False,
)


class ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef(
    _ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef
):
    """
    - *(dict) --*

      Describes an anomaly or error with the application.
      - **Id** *(string) --*

        The ID of the observation type.
    """


_ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef = TypedDict(
    "_ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef",
    {
        "ObservationList": List[
            ClientDescribeProblemObservationsResponseRelatedObservationsObservationListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef(
    _ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef
):
    """
    - **RelatedObservations** *(dict) --*

      Observations related to the problem.
      - **ObservationList** *(list) --*

        The list of observations related to the problem.
        - *(dict) --*

          Describes an anomaly or error with the application.
          - **Id** *(string) --*

            The ID of the observation type.
    """


_ClientDescribeProblemObservationsResponseTypeDef = TypedDict(
    "_ClientDescribeProblemObservationsResponseTypeDef",
    {"RelatedObservations": ClientDescribeProblemObservationsResponseRelatedObservationsTypeDef},
    total=False,
)


class ClientDescribeProblemObservationsResponseTypeDef(
    _ClientDescribeProblemObservationsResponseTypeDef
):
    """
    - *(dict) --*

      - **RelatedObservations** *(dict) --*

        Observations related to the problem.
        - **ObservationList** *(list) --*

          The list of observations related to the problem.
          - *(dict) --*

            Describes an anomaly or error with the application.
            - **Id** *(string) --*

              The ID of the observation type.
    """


_ClientDescribeProblemResponseProblemTypeDef = TypedDict(
    "_ClientDescribeProblemResponseProblemTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": Literal["IGNORE", "RESOLVED", "PENDING"],
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": Literal["Low", "Medium", "High"],
        "ResourceGroupName": str,
        "Feedback": Dict[str, Literal["NOT_SPECIFIED", "USEFUL", "NOT_USEFUL"]],
    },
    total=False,
)


class ClientDescribeProblemResponseProblemTypeDef(_ClientDescribeProblemResponseProblemTypeDef):
    """
    - **Problem** *(dict) --*

      Information about the problem.
      - **Id** *(string) --*

        The ID of the problem.
    """


_ClientDescribeProblemResponseTypeDef = TypedDict(
    "_ClientDescribeProblemResponseTypeDef",
    {"Problem": ClientDescribeProblemResponseProblemTypeDef},
    total=False,
)


class ClientDescribeProblemResponseTypeDef(_ClientDescribeProblemResponseTypeDef):
    """
    - *(dict) --*

      - **Problem** *(dict) --*

        Information about the problem.
        - **Id** *(string) --*

          The ID of the problem.
    """


_ClientListApplicationsResponseApplicationInfoListTypeDef = TypedDict(
    "_ClientListApplicationsResponseApplicationInfoListTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)


class ClientListApplicationsResponseApplicationInfoListTypeDef(
    _ClientListApplicationsResponseApplicationInfoListTypeDef
):
    """
    - *(dict) --*

      Describes the status of the application.
      - **ResourceGroupName** *(string) --*

        The name of the resource group used for the application.
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {
        "ApplicationInfoList": List[ClientListApplicationsResponseApplicationInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationInfoList** *(list) --*

        The list of applications.
        - *(dict) --*

          Describes the status of the application.
          - **ResourceGroupName** *(string) --*

            The name of the resource group used for the application.
    """


_ClientListComponentsResponseApplicationComponentListTypeDef = TypedDict(
    "_ClientListComponentsResponseApplicationComponentListTypeDef",
    {
        "ComponentName": str,
        "ResourceType": str,
        "Tier": Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
        "Monitor": bool,
    },
    total=False,
)


class ClientListComponentsResponseApplicationComponentListTypeDef(
    _ClientListComponentsResponseApplicationComponentListTypeDef
):
    """
    - *(dict) --*

      Describes a standalone resource or similarly grouped resources that the application is made up
      of.
      - **ComponentName** *(string) --*

        The name of the component.
    """


_ClientListComponentsResponseTypeDef = TypedDict(
    "_ClientListComponentsResponseTypeDef",
    {
        "ApplicationComponentList": List[
            ClientListComponentsResponseApplicationComponentListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListComponentsResponseTypeDef(_ClientListComponentsResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationComponentList** *(list) --*

        The list of application components.
        - *(dict) --*

          Describes a standalone resource or similarly grouped resources that the application is
          made up of.
          - **ComponentName** *(string) --*

            The name of the component.
    """


_ClientListLogPatternSetsResponseTypeDef = TypedDict(
    "_ClientListLogPatternSetsResponseTypeDef",
    {"ResourceGroupName": str, "LogPatternSets": List[str], "NextToken": str},
    total=False,
)


class ClientListLogPatternSetsResponseTypeDef(_ClientListLogPatternSetsResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceGroupName** *(string) --*

        The name of the resource group.
    """


_ClientListLogPatternsResponseLogPatternsTypeDef = TypedDict(
    "_ClientListLogPatternsResponseLogPatternsTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)


class ClientListLogPatternsResponseLogPatternsTypeDef(
    _ClientListLogPatternsResponseLogPatternsTypeDef
):
    pass


_ClientListLogPatternsResponseTypeDef = TypedDict(
    "_ClientListLogPatternsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatterns": List[ClientListLogPatternsResponseLogPatternsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListLogPatternsResponseTypeDef(_ClientListLogPatternsResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceGroupName** *(string) --*

        The name of the resource group.
    """


_ClientListProblemsResponseProblemListTypeDef = TypedDict(
    "_ClientListProblemsResponseProblemListTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": Literal["IGNORE", "RESOLVED", "PENDING"],
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": Literal["Low", "Medium", "High"],
        "ResourceGroupName": str,
        "Feedback": Dict[str, Literal["NOT_SPECIFIED", "USEFUL", "NOT_USEFUL"]],
    },
    total=False,
)


class ClientListProblemsResponseProblemListTypeDef(_ClientListProblemsResponseProblemListTypeDef):
    """
    - *(dict) --*

      Describes a problem that is detected by correlating observations.
      - **Id** *(string) --*

        The ID of the problem.
    """


_ClientListProblemsResponseTypeDef = TypedDict(
    "_ClientListProblemsResponseTypeDef",
    {"ProblemList": List[ClientListProblemsResponseProblemListTypeDef], "NextToken": str},
    total=False,
)


class ClientListProblemsResponseTypeDef(_ClientListProblemsResponseTypeDef):
    """
    - *(dict) --*

      - **ProblemList** *(list) --*

        The list of problems.
        - *(dict) --*

          Describes a problem that is detected by correlating observations.
          - **Id** *(string) --*

            The ID of the problem.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      An object that defines the tags associated with an application. A *tag* is a label that you
      optionally define and associate with an application. Tags can help you categorize and manage
      resources in different ways, such as by purpose, owner, environment, or other criteria.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix.
      - **Key** *(string) --*

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        An array that lists all the tags that are associated with the application. Each tag consists
        of a required tag key (``Key`` ) and an associated tag value (``Value`` ).
        - *(dict) --*

          An object that defines the tags associated with an application. A *tag* is a label that
          you optionally define and associate with an application. Tags can help you categorize and
          manage resources in different ways, such as by purpose, owner, environment, or other
          criteria.
          Each tag consists of a required *tag key* and an associated *tag value* , both of which
          you define. A tag key is a general label that acts as a category for a more specific tag
          value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as
          128 characters. A tag value can contain as many as 256 characters. The characters can be
          Unicode letters, digits, white space, or one of the following symbols: _ . : / =
               + -. The
          following additional restrictions apply to tags:
          * Tag keys and values are case sensitive.
          * For each associated resource, each tag key must be unique and it can have only one
          value.
          * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
          values that you define. In addition, you can't edit or remove tag keys or values that use
          this prefix.
          - **Key** *(string) --*

            One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
            characters. The minimum length is 1 character.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      An object that defines the tags associated with an application. A *tag* is a label that you
      optionally define and associate with an application. Tags can help you categorize and manage
      resources in different ways, such as by purpose, owner, environment, or other criteria.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientUpdateApplicationResponseApplicationInfoTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "Remarks": str,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationInfoTypeDef(
    _ClientUpdateApplicationResponseApplicationInfoTypeDef
):
    """
    - **ApplicationInfo** *(dict) --*

      Information about the application.
      - **ResourceGroupName** *(string) --*

        The name of the resource group used for the application.
    """


_ClientUpdateApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseTypeDef",
    {"ApplicationInfo": ClientUpdateApplicationResponseApplicationInfoTypeDef},
    total=False,
)


class ClientUpdateApplicationResponseTypeDef(_ClientUpdateApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationInfo** *(dict) --*

        Information about the application.
        - **ResourceGroupName** *(string) --*

          The name of the resource group used for the application.
    """


_ClientUpdateLogPatternResponseLogPatternTypeDef = TypedDict(
    "_ClientUpdateLogPatternResponseLogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)


class ClientUpdateLogPatternResponseLogPatternTypeDef(
    _ClientUpdateLogPatternResponseLogPatternTypeDef
):
    pass


_ClientUpdateLogPatternResponseTypeDef = TypedDict(
    "_ClientUpdateLogPatternResponseTypeDef",
    {"ResourceGroupName": str, "LogPattern": ClientUpdateLogPatternResponseLogPatternTypeDef},
    total=False,
)


class ClientUpdateLogPatternResponseTypeDef(_ClientUpdateLogPatternResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceGroupName** *(string) --*

        The name of the resource group.
    """
