"Main interface for health service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef",
    "ClientDescribeAffectedEntitiesFilterTypeDef",
    "ClientDescribeAffectedEntitiesResponseentitiesTypeDef",
    "ClientDescribeAffectedEntitiesResponseTypeDef",
    "ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef",
    "ClientDescribeEntityAggregatesResponseTypeDef",
    "ClientDescribeEventAggregatesFilterendTimesTypeDef",
    "ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef",
    "ClientDescribeEventAggregatesFilterstartTimesTypeDef",
    "ClientDescribeEventAggregatesFilterTypeDef",
    "ClientDescribeEventAggregatesResponseeventAggregatesTypeDef",
    "ClientDescribeEventAggregatesResponseTypeDef",
    "ClientDescribeEventDetailsResponsefailedSetTypeDef",
    "ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef",
    "ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef",
    "ClientDescribeEventDetailsResponsesuccessfulSetTypeDef",
    "ClientDescribeEventDetailsResponseTypeDef",
    "ClientDescribeEventTypesFilterTypeDef",
    "ClientDescribeEventTypesResponseeventTypesTypeDef",
    "ClientDescribeEventTypesResponseTypeDef",
    "ClientDescribeEventsFilterendTimesTypeDef",
    "ClientDescribeEventsFilterlastUpdatedTimesTypeDef",
    "ClientDescribeEventsFilterstartTimesTypeDef",
    "ClientDescribeEventsFilterTypeDef",
    "ClientDescribeEventsResponseeventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef",
    "DescribeAffectedEntitiesPaginateFilterTypeDef",
    "DescribeAffectedEntitiesPaginatePaginationConfigTypeDef",
    "DescribeAffectedEntitiesPaginateResponseentitiesTypeDef",
    "DescribeAffectedEntitiesPaginateResponseTypeDef",
    "DescribeEventAggregatesPaginateFilterendTimesTypeDef",
    "DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef",
    "DescribeEventAggregatesPaginateFilterstartTimesTypeDef",
    "DescribeEventAggregatesPaginateFilterTypeDef",
    "DescribeEventAggregatesPaginatePaginationConfigTypeDef",
    "DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef",
    "DescribeEventAggregatesPaginateResponseTypeDef",
    "DescribeEventTypesPaginateFilterTypeDef",
    "DescribeEventTypesPaginatePaginationConfigTypeDef",
    "DescribeEventTypesPaginateResponseeventTypesTypeDef",
    "DescribeEventTypesPaginateResponseTypeDef",
    "DescribeEventsPaginateFilterendTimesTypeDef",
    "DescribeEventsPaginateFilterlastUpdatedTimesTypeDef",
    "DescribeEventsPaginateFilterstartTimesTypeDef",
    "DescribeEventsPaginateFilterTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseeventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
)


_ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef = TypedDict(
    "_ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef(
    _ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef
):
    pass


_RequiredClientDescribeAffectedEntitiesFilterTypeDef = TypedDict(
    "_RequiredClientDescribeAffectedEntitiesFilterTypeDef", {"eventArns": List[str]}
)
_OptionalClientDescribeAffectedEntitiesFilterTypeDef = TypedDict(
    "_OptionalClientDescribeAffectedEntitiesFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[ClientDescribeAffectedEntitiesFilterlastUpdatedTimesTypeDef],
        "tags": List[Dict[str, str]],
        "statusCodes": List[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]],
    },
    total=False,
)


class ClientDescribeAffectedEntitiesFilterTypeDef(
    _RequiredClientDescribeAffectedEntitiesFilterTypeDef,
    _OptionalClientDescribeAffectedEntitiesFilterTypeDef,
):
    """
    Values to narrow the results returned. At least one event ARN is required.
    - **eventArns** *(list) --***[REQUIRED]**

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``
      - *(string) --*
    """


_ClientDescribeAffectedEntitiesResponseentitiesTypeDef = TypedDict(
    "_ClientDescribeAffectedEntitiesResponseentitiesTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeAffectedEntitiesResponseentitiesTypeDef(
    _ClientDescribeAffectedEntitiesResponseentitiesTypeDef
):
    """
    - *(dict) --*

      Information about an entity that is affected by a Health event.
      - **entityArn** *(string) --*

        The unique identifier for the entity. Format: ``arn:aws:health:*entity-region*
        :*aws-account* :entity/*entity-id* `` . Example:
        ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K``
    """


_ClientDescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "_ClientDescribeAffectedEntitiesResponseTypeDef",
    {"entities": List[ClientDescribeAffectedEntitiesResponseentitiesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeAffectedEntitiesResponseTypeDef(_ClientDescribeAffectedEntitiesResponseTypeDef):
    """
    - *(dict) --*

      - **entities** *(list) --*

        The entities that match the filter criteria.
        - *(dict) --*

          Information about an entity that is affected by a Health event.
          - **entityArn** *(string) --*

            The unique identifier for the entity. Format: ``arn:aws:health:*entity-region*
            :*aws-account* :entity/*entity-id* `` . Example:
            ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K``
    """


_ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef = TypedDict(
    "_ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef",
    {"eventArn": str, "count": int},
    total=False,
)


class ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef(
    _ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef
):
    """
    - *(dict) --*

      The number of entities that are affected by one or more events. Returned by the
      DescribeEntityAggregates operation.
      - **eventArn** *(string) --*

        The unique identifier for the event. Format: ``arn:aws:health:*event-region*
        ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
        arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_ClientDescribeEntityAggregatesResponseTypeDef = TypedDict(
    "_ClientDescribeEntityAggregatesResponseTypeDef",
    {"entityAggregates": List[ClientDescribeEntityAggregatesResponseentityAggregatesTypeDef]},
    total=False,
)


class ClientDescribeEntityAggregatesResponseTypeDef(_ClientDescribeEntityAggregatesResponseTypeDef):
    """
    - *(dict) --*

      - **entityAggregates** *(list) --*

        The number of entities that are affected by each of the specified events.
        - *(dict) --*

          The number of entities that are affected by one or more events. Returned by the
          DescribeEntityAggregates operation.
          - **eventArn** *(string) --*

            The unique identifier for the event. Format: ``arn:aws:health:*event-region*
            ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
            arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_ClientDescribeEventAggregatesFilterendTimesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesFilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventAggregatesFilterendTimesTypeDef(
    _ClientDescribeEventAggregatesFilterendTimesTypeDef
):
    pass


_ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef(
    _ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef
):
    pass


_ClientDescribeEventAggregatesFilterstartTimesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesFilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventAggregatesFilterstartTimesTypeDef(
    _ClientDescribeEventAggregatesFilterstartTimesTypeDef
):
    pass


_ClientDescribeEventAggregatesFilterTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventAggregatesFilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventAggregatesFilterendTimesTypeDef],
        "lastUpdatedTimes": List[ClientDescribeEventAggregatesFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)


class ClientDescribeEventAggregatesFilterTypeDef(_ClientDescribeEventAggregatesFilterTypeDef):
    """
    Values to narrow the results returned.
    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``
      - *(string) --*
    """


_ClientDescribeEventAggregatesResponseeventAggregatesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesResponseeventAggregatesTypeDef",
    {"aggregateValue": str, "count": int},
    total=False,
)


class ClientDescribeEventAggregatesResponseeventAggregatesTypeDef(
    _ClientDescribeEventAggregatesResponseeventAggregatesTypeDef
):
    """
    - *(dict) --*

      The number of events of each issue type. Returned by the  DescribeEventAggregates operation.
      - **aggregateValue** *(string) --*

        The issue type for the associated count.
    """


_ClientDescribeEventAggregatesResponseTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesResponseTypeDef",
    {
        "eventAggregates": List[ClientDescribeEventAggregatesResponseeventAggregatesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeEventAggregatesResponseTypeDef(_ClientDescribeEventAggregatesResponseTypeDef):
    """
    - *(dict) --*

      - **eventAggregates** *(list) --*

        The number of events in each category that meet the optional filter criteria.
        - *(dict) --*

          The number of events of each issue type. Returned by the  DescribeEventAggregates
          operation.
          - **aggregateValue** *(string) --*

            The issue type for the associated count.
    """


_ClientDescribeEventDetailsResponsefailedSetTypeDef = TypedDict(
    "_ClientDescribeEventDetailsResponsefailedSetTypeDef",
    {"eventArn": str, "errorName": str, "errorMessage": str},
    total=False,
)


class ClientDescribeEventDetailsResponsefailedSetTypeDef(
    _ClientDescribeEventDetailsResponsefailedSetTypeDef
):
    pass


_ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef = TypedDict(
    "_ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef",
    {"latestDescription": str},
    total=False,
)


class ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef(
    _ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef
):
    pass


_ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef = TypedDict(
    "_ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)


class ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef(
    _ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef
):
    """
    - **event** *(dict) --*

      Summary information about the event.
      - **arn** *(string) --*

        The unique identifier for the event. Format: ``arn:aws:health:*event-region*
        ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
        arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_ClientDescribeEventDetailsResponsesuccessfulSetTypeDef = TypedDict(
    "_ClientDescribeEventDetailsResponsesuccessfulSetTypeDef",
    {
        "event": ClientDescribeEventDetailsResponsesuccessfulSeteventTypeDef,
        "eventDescription": ClientDescribeEventDetailsResponsesuccessfulSeteventDescriptionTypeDef,
        "eventMetadata": Dict[str, str],
    },
    total=False,
)


class ClientDescribeEventDetailsResponsesuccessfulSetTypeDef(
    _ClientDescribeEventDetailsResponsesuccessfulSetTypeDef
):
    """
    - *(dict) --*

      Detailed information about an event. A combination of an  Event object, an  EventDescription
      object, and additional metadata about the event. Returned by the  DescribeEventDetails
      operation.
      - **event** *(dict) --*

        Summary information about the event.
        - **arn** *(string) --*

          The unique identifier for the event. Format: ``arn:aws:health:*event-region*
          ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
          arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_ClientDescribeEventDetailsResponseTypeDef = TypedDict(
    "_ClientDescribeEventDetailsResponseTypeDef",
    {
        "successfulSet": List[ClientDescribeEventDetailsResponsesuccessfulSetTypeDef],
        "failedSet": List[ClientDescribeEventDetailsResponsefailedSetTypeDef],
    },
    total=False,
)


class ClientDescribeEventDetailsResponseTypeDef(_ClientDescribeEventDetailsResponseTypeDef):
    """
    - *(dict) --*

      - **successfulSet** *(list) --*

        Information about the events that could be retrieved.
        - *(dict) --*

          Detailed information about an event. A combination of an  Event object, an
          EventDescription object, and additional metadata about the event. Returned by the
          DescribeEventDetails operation.
          - **event** *(dict) --*

            Summary information about the event.
            - **arn** *(string) --*

              The unique identifier for the event. Format: ``arn:aws:health:*event-region*
              ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
              arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_ClientDescribeEventTypesFilterTypeDef = TypedDict(
    "_ClientDescribeEventTypesFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
    },
    total=False,
)


class ClientDescribeEventTypesFilterTypeDef(_ClientDescribeEventTypesFilterTypeDef):
    """
    Values to narrow the results returned.
    - **eventTypeCodes** *(list) --*

      A list of event type codes.
      - *(string) --*
    """


_ClientDescribeEventTypesResponseeventTypesTypeDef = TypedDict(
    "_ClientDescribeEventTypesResponseeventTypesTypeDef",
    {
        "service": str,
        "code": str,
        "category": Literal["issue", "accountNotification", "scheduledChange", "investigation"],
    },
    total=False,
)


class ClientDescribeEventTypesResponseeventTypesTypeDef(
    _ClientDescribeEventTypesResponseeventTypesTypeDef
):
    """
    - *(dict) --*

      Metadata about a type of event that is reported by AWS Health. Data consists of the category
      (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type code (for
      example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
      - **service** *(string) --*

        The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .
    """


_ClientDescribeEventTypesResponseTypeDef = TypedDict(
    "_ClientDescribeEventTypesResponseTypeDef",
    {"eventTypes": List[ClientDescribeEventTypesResponseeventTypesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeEventTypesResponseTypeDef(_ClientDescribeEventTypesResponseTypeDef):
    """
    - *(dict) --*

      - **eventTypes** *(list) --*

        A list of event types that match the filter criteria. Event types have a category (``issue``
        , ``accountNotification`` , or ``scheduledChange`` ), a service (for example, ``EC2`` ,
        ``RDS`` , ``DATAPIPELINE`` , ``BILLING`` ), and a code (in the format ``AWS_*SERVICE*
        _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
        - *(dict) --*

          Metadata about a type of event that is reported by AWS Health. Data consists of the
          category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event
          type code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
          - **service** *(string) --*

            The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .
    """


_ClientDescribeEventsFilterendTimesTypeDef = TypedDict(
    "_ClientDescribeEventsFilterendTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)


class ClientDescribeEventsFilterendTimesTypeDef(_ClientDescribeEventsFilterendTimesTypeDef):
    pass


_ClientDescribeEventsFilterlastUpdatedTimesTypeDef = TypedDict(
    "_ClientDescribeEventsFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventsFilterlastUpdatedTimesTypeDef(
    _ClientDescribeEventsFilterlastUpdatedTimesTypeDef
):
    pass


_ClientDescribeEventsFilterstartTimesTypeDef = TypedDict(
    "_ClientDescribeEventsFilterstartTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)


class ClientDescribeEventsFilterstartTimesTypeDef(_ClientDescribeEventsFilterstartTimesTypeDef):
    pass


_ClientDescribeEventsFilterTypeDef = TypedDict(
    "_ClientDescribeEventsFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventsFilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventsFilterendTimesTypeDef],
        "lastUpdatedTimes": List[ClientDescribeEventsFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)


class ClientDescribeEventsFilterTypeDef(_ClientDescribeEventsFilterTypeDef):
    """
    Values to narrow the results returned.
    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``
      - *(string) --*
    """


_ClientDescribeEventsResponseeventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseeventsTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)


class ClientDescribeEventsResponseeventsTypeDef(_ClientDescribeEventsResponseeventsTypeDef):
    """
    - *(dict) --*

      Summary information about an event, returned by the  DescribeEvents operation. The
      DescribeEventDetails operation also returns this information, as well as the  EventDescription
      and additional event metadata.
      - **arn** *(string) --*

        The unique identifier for the event. Format: ``arn:aws:health:*event-region*
        ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
        arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"events": List[ClientDescribeEventsResponseeventsTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    - *(dict) --*

      - **events** *(list) --*

        The events that match the specified filter criteria.
        - *(dict) --*

          Summary information about an event, returned by the  DescribeEvents operation. The
          DescribeEventDetails operation also returns this information, as well as the
          EventDescription and additional event metadata.
          - **arn** *(string) --*

            The unique identifier for the event. Format: ``arn:aws:health:*event-region*
            ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
            arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef = TypedDict(
    "_DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef(
    _DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef
):
    pass


_RequiredDescribeAffectedEntitiesPaginateFilterTypeDef = TypedDict(
    "_RequiredDescribeAffectedEntitiesPaginateFilterTypeDef", {"eventArns": List[str]}
)
_OptionalDescribeAffectedEntitiesPaginateFilterTypeDef = TypedDict(
    "_OptionalDescribeAffectedEntitiesPaginateFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[DescribeAffectedEntitiesPaginateFilterlastUpdatedTimesTypeDef],
        "tags": List[Dict[str, str]],
        "statusCodes": List[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]],
    },
    total=False,
)


class DescribeAffectedEntitiesPaginateFilterTypeDef(
    _RequiredDescribeAffectedEntitiesPaginateFilterTypeDef,
    _OptionalDescribeAffectedEntitiesPaginateFilterTypeDef,
):
    """
    Values to narrow the results returned. At least one event ARN is required.
    - **eventArns** *(list) --***[REQUIRED]**

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``
      - *(string) --*
    """


_DescribeAffectedEntitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAffectedEntitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAffectedEntitiesPaginatePaginationConfigTypeDef(
    _DescribeAffectedEntitiesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAffectedEntitiesPaginateResponseentitiesTypeDef = TypedDict(
    "_DescribeAffectedEntitiesPaginateResponseentitiesTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)


class DescribeAffectedEntitiesPaginateResponseentitiesTypeDef(
    _DescribeAffectedEntitiesPaginateResponseentitiesTypeDef
):
    """
    - *(dict) --*

      Information about an entity that is affected by a Health event.
      - **entityArn** *(string) --*

        The unique identifier for the entity. Format: ``arn:aws:health:*entity-region*
        :*aws-account* :entity/*entity-id* `` . Example:
        ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K``
    """


_DescribeAffectedEntitiesPaginateResponseTypeDef = TypedDict(
    "_DescribeAffectedEntitiesPaginateResponseTypeDef",
    {"entities": List[DescribeAffectedEntitiesPaginateResponseentitiesTypeDef], "NextToken": str},
    total=False,
)


class DescribeAffectedEntitiesPaginateResponseTypeDef(
    _DescribeAffectedEntitiesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **entities** *(list) --*

        The entities that match the filter criteria.
        - *(dict) --*

          Information about an entity that is affected by a Health event.
          - **entityArn** *(string) --*

            The unique identifier for the entity. Format: ``arn:aws:health:*entity-region*
            :*aws-account* :entity/*entity-id* `` . Example:
            ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K``
    """


_DescribeEventAggregatesPaginateFilterendTimesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateFilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventAggregatesPaginateFilterendTimesTypeDef(
    _DescribeEventAggregatesPaginateFilterendTimesTypeDef
):
    pass


_DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef(
    _DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef
):
    pass


_DescribeEventAggregatesPaginateFilterstartTimesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateFilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventAggregatesPaginateFilterstartTimesTypeDef(
    _DescribeEventAggregatesPaginateFilterstartTimesTypeDef
):
    pass


_DescribeEventAggregatesPaginateFilterTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DescribeEventAggregatesPaginateFilterstartTimesTypeDef],
        "endTimes": List[DescribeEventAggregatesPaginateFilterendTimesTypeDef],
        "lastUpdatedTimes": List[DescribeEventAggregatesPaginateFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)


class DescribeEventAggregatesPaginateFilterTypeDef(_DescribeEventAggregatesPaginateFilterTypeDef):
    """
    Values to narrow the results returned.
    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``
      - *(string) --*
    """


_DescribeEventAggregatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventAggregatesPaginatePaginationConfigTypeDef(
    _DescribeEventAggregatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef",
    {"aggregateValue": str, "count": int},
    total=False,
)


class DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef(
    _DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef
):
    """
    - *(dict) --*

      The number of events of each issue type. Returned by the  DescribeEventAggregates operation.
      - **aggregateValue** *(string) --*

        The issue type for the associated count.
    """


_DescribeEventAggregatesPaginateResponseTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateResponseTypeDef",
    {
        "eventAggregates": List[DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeEventAggregatesPaginateResponseTypeDef(
    _DescribeEventAggregatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **eventAggregates** *(list) --*

        The number of events in each category that meet the optional filter criteria.
        - *(dict) --*

          The number of events of each issue type. Returned by the  DescribeEventAggregates
          operation.
          - **aggregateValue** *(string) --*

            The issue type for the associated count.
    """


_DescribeEventTypesPaginateFilterTypeDef = TypedDict(
    "_DescribeEventTypesPaginateFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
    },
    total=False,
)


class DescribeEventTypesPaginateFilterTypeDef(_DescribeEventTypesPaginateFilterTypeDef):
    """
    Values to narrow the results returned.
    - **eventTypeCodes** *(list) --*

      A list of event type codes.
      - *(string) --*
    """


_DescribeEventTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventTypesPaginatePaginationConfigTypeDef(
    _DescribeEventTypesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventTypesPaginateResponseeventTypesTypeDef = TypedDict(
    "_DescribeEventTypesPaginateResponseeventTypesTypeDef",
    {
        "service": str,
        "code": str,
        "category": Literal["issue", "accountNotification", "scheduledChange", "investigation"],
    },
    total=False,
)


class DescribeEventTypesPaginateResponseeventTypesTypeDef(
    _DescribeEventTypesPaginateResponseeventTypesTypeDef
):
    """
    - *(dict) --*

      Metadata about a type of event that is reported by AWS Health. Data consists of the category
      (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type code (for
      example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
      - **service** *(string) --*

        The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .
    """


_DescribeEventTypesPaginateResponseTypeDef = TypedDict(
    "_DescribeEventTypesPaginateResponseTypeDef",
    {"eventTypes": List[DescribeEventTypesPaginateResponseeventTypesTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventTypesPaginateResponseTypeDef(_DescribeEventTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **eventTypes** *(list) --*

        A list of event types that match the filter criteria. Event types have a category (``issue``
        , ``accountNotification`` , or ``scheduledChange`` ), a service (for example, ``EC2`` ,
        ``RDS`` , ``DATAPIPELINE`` , ``BILLING`` ), and a code (in the format ``AWS_*SERVICE*
        _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
        - *(dict) --*

          Metadata about a type of event that is reported by AWS Health. Data consists of the
          category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event
          type code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).
          - **service** *(string) --*

            The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .
    """


_DescribeEventsPaginateFilterendTimesTypeDef = TypedDict(
    "_DescribeEventsPaginateFilterendTimesTypeDef", {"from": datetime, "to": datetime}, total=False
)


class DescribeEventsPaginateFilterendTimesTypeDef(_DescribeEventsPaginateFilterendTimesTypeDef):
    pass


_DescribeEventsPaginateFilterlastUpdatedTimesTypeDef = TypedDict(
    "_DescribeEventsPaginateFilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventsPaginateFilterlastUpdatedTimesTypeDef(
    _DescribeEventsPaginateFilterlastUpdatedTimesTypeDef
):
    pass


_DescribeEventsPaginateFilterstartTimesTypeDef = TypedDict(
    "_DescribeEventsPaginateFilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventsPaginateFilterstartTimesTypeDef(_DescribeEventsPaginateFilterstartTimesTypeDef):
    pass


_DescribeEventsPaginateFilterTypeDef = TypedDict(
    "_DescribeEventsPaginateFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DescribeEventsPaginateFilterstartTimesTypeDef],
        "endTimes": List[DescribeEventsPaginateFilterendTimesTypeDef],
        "lastUpdatedTimes": List[DescribeEventsPaginateFilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)


class DescribeEventsPaginateFilterTypeDef(_DescribeEventsPaginateFilterTypeDef):
    """
    Values to narrow the results returned.
    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``
      - *(string) --*
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(_DescribeEventsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventsPaginateResponseeventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseeventsTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)


class DescribeEventsPaginateResponseeventsTypeDef(_DescribeEventsPaginateResponseeventsTypeDef):
    """
    - *(dict) --*

      Summary information about an event, returned by the  DescribeEvents operation. The
      DescribeEventDetails operation also returns this information, as well as the  EventDescription
      and additional event metadata.
      - **arn** *(string) --*

        The unique identifier for the event. Format: ``arn:aws:health:*event-region*
        ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
        arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"events": List[DescribeEventsPaginateResponseeventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **events** *(list) --*

        The events that match the specified filter criteria.
        - *(dict) --*

          Summary information about an event, returned by the  DescribeEvents operation. The
          DescribeEventDetails operation also returns this information, as well as the
          EventDescription and additional event metadata.
          - **arn** *(string) --*

            The unique identifier for the event. Format: ``arn:aws:health:*event-region*
            ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example:
            arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456``
    """
