"Main interface for budgets service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateBudgetBudgetBudgetLimitTypeDef",
    "ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef",
    "ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef",
    "ClientCreateBudgetBudgetCalculatedSpendTypeDef",
    "ClientCreateBudgetBudgetCostTypesTypeDef",
    "ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef",
    "ClientCreateBudgetBudgetTimePeriodTypeDef",
    "ClientCreateBudgetBudgetTypeDef",
    "ClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef",
    "ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef",
    "ClientCreateBudgetNotificationsWithSubscribersTypeDef",
    "ClientCreateNotificationNotificationTypeDef",
    "ClientCreateNotificationSubscribersTypeDef",
    "ClientCreateSubscriberNotificationTypeDef",
    "ClientCreateSubscriberSubscriberTypeDef",
    "ClientDeleteNotificationNotificationTypeDef",
    "ClientDeleteSubscriberNotificationTypeDef",
    "ClientDeleteSubscriberSubscriberTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef",
    "ClientDescribeBudgetPerformanceHistoryResponseTypeDef",
    "ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef",
    "ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef",
    "ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef",
    "ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef",
    "ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef",
    "ClientDescribeBudgetResponseBudgetCostTypesTypeDef",
    "ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef",
    "ClientDescribeBudgetResponseBudgetTimePeriodTypeDef",
    "ClientDescribeBudgetResponseBudgetTypeDef",
    "ClientDescribeBudgetResponseTypeDef",
    "ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef",
    "ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef",
    "ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef",
    "ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef",
    "ClientDescribeBudgetsResponseBudgetsTypeDef",
    "ClientDescribeBudgetsResponseTypeDef",
    "ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef",
    "ClientDescribeNotificationsForBudgetResponseTypeDef",
    "ClientDescribeSubscribersForNotificationNotificationTypeDef",
    "ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef",
    "ClientDescribeSubscribersForNotificationResponseTypeDef",
    "ClientUpdateBudgetNewBudgetBudgetLimitTypeDef",
    "ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef",
    "ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef",
    "ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef",
    "ClientUpdateBudgetNewBudgetCostTypesTypeDef",
    "ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef",
    "ClientUpdateBudgetNewBudgetTimePeriodTypeDef",
    "ClientUpdateBudgetNewBudgetTypeDef",
    "ClientUpdateNotificationNewNotificationTypeDef",
    "ClientUpdateNotificationOldNotificationTypeDef",
    "ClientUpdateSubscriberNewSubscriberTypeDef",
    "ClientUpdateSubscriberNotificationTypeDef",
    "ClientUpdateSubscriberOldSubscriberTypeDef",
    "DescribeBudgetsPaginatePaginationConfigTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef",
    "DescribeBudgetsPaginateResponseBudgetsTypeDef",
    "DescribeBudgetsPaginateResponseTypeDef",
    "DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef",
    "DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef",
    "DescribeNotificationsForBudgetPaginateResponseTypeDef",
    "DescribeSubscribersForNotificationPaginateNotificationTypeDef",
    "DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef",
    "DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef",
    "DescribeSubscribersForNotificationPaginateResponseTypeDef",
)


_ClientCreateBudgetBudgetBudgetLimitTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetBudgetLimitTypeDef", {"Amount": str, "Unit": str}, total=False
)


class ClientCreateBudgetBudgetBudgetLimitTypeDef(_ClientCreateBudgetBudgetBudgetLimitTypeDef):
    pass


_ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef(
    _ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef
):
    pass


_ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef(
    _ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef
):
    pass


_ClientCreateBudgetBudgetCalculatedSpendTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class ClientCreateBudgetBudgetCalculatedSpendTypeDef(
    _ClientCreateBudgetBudgetCalculatedSpendTypeDef
):
    pass


_ClientCreateBudgetBudgetCostTypesTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientCreateBudgetBudgetCostTypesTypeDef(_ClientCreateBudgetBudgetCostTypesTypeDef):
    pass


_ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef", {"Amount": str, "Unit": str}, total=False
)


class ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef(
    _ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef
):
    pass


_ClientCreateBudgetBudgetTimePeriodTypeDef = TypedDict(
    "_ClientCreateBudgetBudgetTimePeriodTypeDef", {"Start": datetime, "End": datetime}, total=False
)


class ClientCreateBudgetBudgetTimePeriodTypeDef(_ClientCreateBudgetBudgetTimePeriodTypeDef):
    pass


_RequiredClientCreateBudgetBudgetTypeDef = TypedDict(
    "_RequiredClientCreateBudgetBudgetTypeDef", {"BudgetName": str}
)
_OptionalClientCreateBudgetBudgetTypeDef = TypedDict(
    "_OptionalClientCreateBudgetBudgetTypeDef",
    {
        "BudgetLimit": ClientCreateBudgetBudgetBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[str, ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientCreateBudgetBudgetCostTypesTypeDef,
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "TimePeriod": ClientCreateBudgetBudgetTimePeriodTypeDef,
        "CalculatedSpend": ClientCreateBudgetBudgetCalculatedSpendTypeDef,
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientCreateBudgetBudgetTypeDef(
    _RequiredClientCreateBudgetBudgetTypeDef, _OptionalClientCreateBudgetBudgetTypeDef
):
    """
    The budget object that you want to create.
    - **BudgetName** *(string) --***[REQUIRED]**

      The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
      characters aren't allowed in ``BudgetName`` .
    """


_RequiredClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef = TypedDict(
    "_RequiredClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef = TypedDict(
    "_OptionalClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef(
    _RequiredClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef,
    _OptionalClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef,
):
    """
    - **Notification** *(dict) --***[REQUIRED]**

      The notification that is associated with a budget.
      - **NotificationType** *(string) --***[REQUIRED]**

        Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
        forecasted to spend (``FORECASTED`` ).
    """


_ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef = TypedDict(
    "_ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str},
    total=False,
)


class ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef(
    _ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef
):
    pass


_RequiredClientCreateBudgetNotificationsWithSubscribersTypeDef = TypedDict(
    "_RequiredClientCreateBudgetNotificationsWithSubscribersTypeDef",
    {"Notification": ClientCreateBudgetNotificationsWithSubscribersNotificationTypeDef},
)
_OptionalClientCreateBudgetNotificationsWithSubscribersTypeDef = TypedDict(
    "_OptionalClientCreateBudgetNotificationsWithSubscribersTypeDef",
    {"Subscribers": List[ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef]},
    total=False,
)


class ClientCreateBudgetNotificationsWithSubscribersTypeDef(
    _RequiredClientCreateBudgetNotificationsWithSubscribersTypeDef,
    _OptionalClientCreateBudgetNotificationsWithSubscribersTypeDef,
):
    """
    - *(dict) --*

      A notification with subscribers. A notification can have one SNS subscriber and up to 10 email
      subscribers, for a total of 11 subscribers.
      - **Notification** *(dict) --***[REQUIRED]**

        The notification that is associated with a budget.
        - **NotificationType** *(string) --***[REQUIRED]**

          Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much
          you're forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientCreateNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientCreateNotificationNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientCreateNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientCreateNotificationNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientCreateNotificationNotificationTypeDef(
    _RequiredClientCreateNotificationNotificationTypeDef,
    _OptionalClientCreateNotificationNotificationTypeDef,
):
    """
    The notification that you want to create.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientCreateNotificationSubscribersTypeDef = TypedDict(
    "_RequiredClientCreateNotificationSubscribersTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"]},
)
_OptionalClientCreateNotificationSubscribersTypeDef = TypedDict(
    "_OptionalClientCreateNotificationSubscribersTypeDef", {"Address": str}, total=False
)


class ClientCreateNotificationSubscribersTypeDef(
    _RequiredClientCreateNotificationSubscribersTypeDef,
    _OptionalClientCreateNotificationSubscribersTypeDef,
):
    """
    - *(dict) --*

      The subscriber to a budget notification. The subscriber consists of a subscription type and
      either an Amazon SNS topic or an email address.
      For example, an email subscriber would have the following parameters:
      * A ``subscriptionType`` of ``EMAIL``
      * An ``address`` of ``example@example.com``
      - **SubscriptionType** *(string) --***[REQUIRED]**

        The type of notification that AWS sends to a subscriber.
    """


_RequiredClientCreateSubscriberNotificationTypeDef = TypedDict(
    "_RequiredClientCreateSubscriberNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientCreateSubscriberNotificationTypeDef = TypedDict(
    "_OptionalClientCreateSubscriberNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientCreateSubscriberNotificationTypeDef(
    _RequiredClientCreateSubscriberNotificationTypeDef,
    _OptionalClientCreateSubscriberNotificationTypeDef,
):
    """
    The notification that you want to create a subscriber for.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientCreateSubscriberSubscriberTypeDef = TypedDict(
    "_RequiredClientCreateSubscriberSubscriberTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"]},
)
_OptionalClientCreateSubscriberSubscriberTypeDef = TypedDict(
    "_OptionalClientCreateSubscriberSubscriberTypeDef", {"Address": str}, total=False
)


class ClientCreateSubscriberSubscriberTypeDef(
    _RequiredClientCreateSubscriberSubscriberTypeDef,
    _OptionalClientCreateSubscriberSubscriberTypeDef,
):
    """
    The subscriber that you want to associate with a budget notification.
    - **SubscriptionType** *(string) --***[REQUIRED]**

      The type of notification that AWS sends to a subscriber.
    """


_RequiredClientDeleteNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientDeleteNotificationNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientDeleteNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientDeleteNotificationNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientDeleteNotificationNotificationTypeDef(
    _RequiredClientDeleteNotificationNotificationTypeDef,
    _OptionalClientDeleteNotificationNotificationTypeDef,
):
    """
    The notification that you want to delete.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientDeleteSubscriberNotificationTypeDef = TypedDict(
    "_RequiredClientDeleteSubscriberNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientDeleteSubscriberNotificationTypeDef = TypedDict(
    "_OptionalClientDeleteSubscriberNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientDeleteSubscriberNotificationTypeDef(
    _RequiredClientDeleteSubscriberNotificationTypeDef,
    _OptionalClientDeleteSubscriberNotificationTypeDef,
):
    """
    The notification whose subscriber you want to delete.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientDeleteSubscriberSubscriberTypeDef = TypedDict(
    "_RequiredClientDeleteSubscriberSubscriberTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"]},
)
_OptionalClientDeleteSubscriberSubscriberTypeDef = TypedDict(
    "_OptionalClientDeleteSubscriberSubscriberTypeDef", {"Address": str}, total=False
)


class ClientDeleteSubscriberSubscriberTypeDef(
    _RequiredClientDeleteSubscriberSubscriberTypeDef,
    _OptionalClientDeleteSubscriberSubscriberTypeDef,
):
    """
    The subscriber that you want to delete.
    - **SubscriptionType** *(string) --***[REQUIRED]**

      The type of notification that AWS sends to a subscriber.
    """


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef
):
    pass


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef
):
    pass


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef
):
    pass


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef",
    {
        "BudgetedAmount": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef,
        "ActualAmount": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef,
        "TimePeriod": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef,
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef
):
    pass


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef
):
    pass


_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": str,
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef,
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "BudgetedAndActualAmountsList": List[
            ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef
):
    """
    - **BudgetPerformanceHistory** *(dict) --*

      The history of how often the budget has gone into an ``ALARM`` state.
      For ``DAILY`` budgets, the history saves the state of the budget for the last 60 days. For
      ``MONTHLY`` budgets, the history saves the state of the budget for the current month plus the
      last 12 months. For ``QUARTERLY`` budgets, the history saves the state of the budget for the
      last four quarters.
      - **BudgetName** *(string) --*

        A string that represents the budget name. The ":" and "\\" characters aren't allowed.
    """


_ClientDescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryResponseTypeDef(
    _ClientDescribeBudgetPerformanceHistoryResponseTypeDef
):
    """
    - *(dict) --*

      - **BudgetPerformanceHistory** *(dict) --*

        The history of how often the budget has gone into an ``ALARM`` state.
        For ``DAILY`` budgets, the history saves the state of the budget for the last 60 days. For
        ``MONTHLY`` budgets, the history saves the state of the budget for the current month plus
        the last 12 months. For ``QUARTERLY`` budgets, the history saves the state of the budget for
        the last four quarters.
        - **BudgetName** *(string) --*

          A string that represents the budget name. The ":" and "\\" characters aren't allowed.
    """


_ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef(
    _ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef
):
    """
    Retrieves how often the budget went into an ``ALARM`` state for the specified time period.
    - **Start** *(datetime) --*

      The start date for a budget. If you created your budget and didn't specify a start date, AWS
      defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For
      example, if you created your budget on January 24, 2018, chose ``DAILY`` , and didn't set a
      start date, AWS set your start date to ``01/24/18 00:00 UTC`` . If you chose ``MONTHLY`` , AWS
      set your start date to ``01/01/18 00:00 UTC`` . The defaults are the same for the AWS Billing
      and Cost Management console and the API.
      You can change your start date with the ``UpdateBudget`` operation.
    """


_ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef(
    _ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef
):
    pass


_ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef(
    _ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef
):
    pass


_ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef(
    _ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef
):
    pass


_ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef(
    _ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef
):
    pass


_ClientDescribeBudgetResponseBudgetCostTypesTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientDescribeBudgetResponseBudgetCostTypesTypeDef(
    _ClientDescribeBudgetResponseBudgetCostTypesTypeDef
):
    pass


_ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef(
    _ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef
):
    pass


_ClientDescribeBudgetResponseBudgetTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetResponseBudgetTimePeriodTypeDef(
    _ClientDescribeBudgetResponseBudgetTimePeriodTypeDef
):
    pass


_ClientDescribeBudgetResponseBudgetTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseBudgetTypeDef",
    {
        "BudgetName": str,
        "BudgetLimit": ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientDescribeBudgetResponseBudgetCostTypesTypeDef,
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "TimePeriod": ClientDescribeBudgetResponseBudgetTimePeriodTypeDef,
        "CalculatedSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef,
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeBudgetResponseBudgetTypeDef(_ClientDescribeBudgetResponseBudgetTypeDef):
    """
    - **Budget** *(dict) --*

      The description of the budget.
      - **BudgetName** *(string) --*

        The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
        characters aren't allowed in ``BudgetName`` .
    """


_ClientDescribeBudgetResponseTypeDef = TypedDict(
    "_ClientDescribeBudgetResponseTypeDef",
    {"Budget": ClientDescribeBudgetResponseBudgetTypeDef},
    total=False,
)


class ClientDescribeBudgetResponseTypeDef(_ClientDescribeBudgetResponseTypeDef):
    """
    - *(dict) --*

      Response of DescribeBudget
      - **Budget** *(dict) --*

        The description of the budget.
        - **BudgetName** *(string) --*

          The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
          characters aren't allowed in ``BudgetName`` .
    """


_ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef(
    _ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef
):
    pass


_ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef
):
    pass


_ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef
):
    pass


_ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef
):
    pass


_ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef(
    _ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef
):
    pass


_ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef(
    _ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef
):
    pass


_ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef(
    _ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef
):
    pass


_ClientDescribeBudgetsResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseBudgetsTypeDef",
    {
        "BudgetName": str,
        "BudgetLimit": ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef,
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "TimePeriod": ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef,
        "CalculatedSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef,
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeBudgetsResponseBudgetsTypeDef(_ClientDescribeBudgetsResponseBudgetsTypeDef):
    """
    - *(dict) --*

      Represents the output of the ``CreateBudget`` operation. The content consists of the detailed
      metadata and data file information, and the current status of the ``budget`` object.
      This is the ARN pattern for a budget:

        ``arn:aws:budgetservice::AccountId:budget/budgetName``
    """


_ClientDescribeBudgetsResponseTypeDef = TypedDict(
    "_ClientDescribeBudgetsResponseTypeDef",
    {"Budgets": List[ClientDescribeBudgetsResponseBudgetsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBudgetsResponseTypeDef(_ClientDescribeBudgetsResponseTypeDef):
    """
    - *(dict) --*

      Response of DescribeBudgets
      - **Budgets** *(list) --*

        A list of budgets.
        - *(dict) --*

          Represents the output of the ``CreateBudget`` operation. The content consists of the
          detailed metadata and data file information, and the current status of the ``budget``
          object.
          This is the ARN pattern for a budget:

            ``arn:aws:budgetservice::AccountId:budget/budgetName``
    """


_ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef = TypedDict(
    "_ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef",
    {
        "NotificationType": Literal["ACTUAL", "FORECASTED"],
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef(
    _ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef
):
    """
    - *(dict) --*

      A notification that is associated with a budget. A budget can have up to five notifications.
      Each notification must have at least one subscriber. A notification can have one SNS
      subscriber and up to 10 email subscribers, for a total of 11 subscribers.
      For example, if you have a budget for 200 dollars and you want to be notified when you go over
      160 dollars, create a notification with the following parameters:
      * A notificationType of ``ACTUAL``
      * A ``thresholdType`` of ``PERCENTAGE``
      * A ``comparisonOperator`` of ``GREATER_THAN``
      * A notification ``threshold`` of ``80``
      - **NotificationType** *(string) --*

        Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
        forecasted to spend (``FORECASTED`` ).
    """


_ClientDescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List[ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeNotificationsForBudgetResponseTypeDef(
    _ClientDescribeNotificationsForBudgetResponseTypeDef
):
    """
    - *(dict) --*

      Response of GetNotificationsForBudget
      - **Notifications** *(list) --*

        A list of notifications that are associated with a budget.
        - *(dict) --*

          A notification that is associated with a budget. A budget can have up to five
          notifications.
          Each notification must have at least one subscriber. A notification can have one SNS
          subscriber and up to 10 email subscribers, for a total of 11 subscribers.
          For example, if you have a budget for 200 dollars and you want to be notified when you go
          over 160 dollars, create a notification with the following parameters:
          * A notificationType of ``ACTUAL``
          * A ``thresholdType`` of ``PERCENTAGE``
          * A ``comparisonOperator`` of ``GREATER_THAN``
          * A notification ``threshold`` of ``80``
          - **NotificationType** *(string) --*

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much
            you're forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientDescribeSubscribersForNotificationNotificationTypeDef = TypedDict(
    "_RequiredClientDescribeSubscribersForNotificationNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientDescribeSubscribersForNotificationNotificationTypeDef = TypedDict(
    "_OptionalClientDescribeSubscribersForNotificationNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientDescribeSubscribersForNotificationNotificationTypeDef(
    _RequiredClientDescribeSubscribersForNotificationNotificationTypeDef,
    _OptionalClientDescribeSubscribersForNotificationNotificationTypeDef,
):
    """
    The notification whose subscribers you want to list.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef = TypedDict(
    "_ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str},
    total=False,
)


class ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef(
    _ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef
):
    """
    - *(dict) --*

      The subscriber to a budget notification. The subscriber consists of a subscription type and
      either an Amazon SNS topic or an email address.
      For example, an email subscriber would have the following parameters:
      * A ``subscriptionType`` of ``EMAIL``
      * An ``address`` of ``example@example.com``
      - **SubscriptionType** *(string) --*

        The type of notification that AWS sends to a subscriber.
    """


_ClientDescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "_ClientDescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List[ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeSubscribersForNotificationResponseTypeDef(
    _ClientDescribeSubscribersForNotificationResponseTypeDef
):
    """
    - *(dict) --*

      Response of DescribeSubscribersForNotification
      - **Subscribers** *(list) --*

        A list of subscribers that are associated with a notification.
        - *(dict) --*

          The subscriber to a budget notification. The subscriber consists of a subscription type
          and either an Amazon SNS topic or an email address.
          For example, an email subscriber would have the following parameters:
          * A ``subscriptionType`` of ``EMAIL``
          * An ``address`` of ``example@example.com``
          - **SubscriptionType** *(string) --*

            The type of notification that AWS sends to a subscriber.
    """


_ClientUpdateBudgetNewBudgetBudgetLimitTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetBudgetLimitTypeDef", {"Amount": str, "Unit": str}, total=False
)


class ClientUpdateBudgetNewBudgetBudgetLimitTypeDef(_ClientUpdateBudgetNewBudgetBudgetLimitTypeDef):
    pass


_ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef(
    _ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef
):
    pass


_ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef(
    _ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef
):
    pass


_ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef(
    _ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef
):
    pass


_ClientUpdateBudgetNewBudgetCostTypesTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class ClientUpdateBudgetNewBudgetCostTypesTypeDef(_ClientUpdateBudgetNewBudgetCostTypesTypeDef):
    pass


_ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef(
    _ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef
):
    pass


_ClientUpdateBudgetNewBudgetTimePeriodTypeDef = TypedDict(
    "_ClientUpdateBudgetNewBudgetTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class ClientUpdateBudgetNewBudgetTimePeriodTypeDef(_ClientUpdateBudgetNewBudgetTimePeriodTypeDef):
    pass


_RequiredClientUpdateBudgetNewBudgetTypeDef = TypedDict(
    "_RequiredClientUpdateBudgetNewBudgetTypeDef", {"BudgetName": str}
)
_OptionalClientUpdateBudgetNewBudgetTypeDef = TypedDict(
    "_OptionalClientUpdateBudgetNewBudgetTypeDef",
    {
        "BudgetLimit": ClientUpdateBudgetNewBudgetBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[str, ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": ClientUpdateBudgetNewBudgetCostTypesTypeDef,
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "TimePeriod": ClientUpdateBudgetNewBudgetTimePeriodTypeDef,
        "CalculatedSpend": ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef,
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientUpdateBudgetNewBudgetTypeDef(
    _RequiredClientUpdateBudgetNewBudgetTypeDef, _OptionalClientUpdateBudgetNewBudgetTypeDef
):
    """
    The budget that you want to update your budget to.
    - **BudgetName** *(string) --***[REQUIRED]**

      The name of a budget. The name must be unique within an account. The ``:`` and ``\\``
      characters aren't allowed in ``BudgetName`` .
    """


_RequiredClientUpdateNotificationNewNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateNotificationNewNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientUpdateNotificationNewNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateNotificationNewNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientUpdateNotificationNewNotificationTypeDef(
    _RequiredClientUpdateNotificationNewNotificationTypeDef,
    _OptionalClientUpdateNotificationNewNotificationTypeDef,
):
    """
    The updated notification to be associated with a budget.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientUpdateNotificationOldNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateNotificationOldNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientUpdateNotificationOldNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateNotificationOldNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientUpdateNotificationOldNotificationTypeDef(
    _RequiredClientUpdateNotificationOldNotificationTypeDef,
    _OptionalClientUpdateNotificationOldNotificationTypeDef,
):
    """
    The previous notification that is associated with a budget.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientUpdateSubscriberNewSubscriberTypeDef = TypedDict(
    "_RequiredClientUpdateSubscriberNewSubscriberTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"]},
)
_OptionalClientUpdateSubscriberNewSubscriberTypeDef = TypedDict(
    "_OptionalClientUpdateSubscriberNewSubscriberTypeDef", {"Address": str}, total=False
)


class ClientUpdateSubscriberNewSubscriberTypeDef(
    _RequiredClientUpdateSubscriberNewSubscriberTypeDef,
    _OptionalClientUpdateSubscriberNewSubscriberTypeDef,
):
    """
    The updated subscriber that is associated with a budget notification.
    - **SubscriptionType** *(string) --***[REQUIRED]**

      The type of notification that AWS sends to a subscriber.
    """


_RequiredClientUpdateSubscriberNotificationTypeDef = TypedDict(
    "_RequiredClientUpdateSubscriberNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalClientUpdateSubscriberNotificationTypeDef = TypedDict(
    "_OptionalClientUpdateSubscriberNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class ClientUpdateSubscriberNotificationTypeDef(
    _RequiredClientUpdateSubscriberNotificationTypeDef,
    _OptionalClientUpdateSubscriberNotificationTypeDef,
):
    """
    The notification whose subscriber you want to update.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_RequiredClientUpdateSubscriberOldSubscriberTypeDef = TypedDict(
    "_RequiredClientUpdateSubscriberOldSubscriberTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"]},
)
_OptionalClientUpdateSubscriberOldSubscriberTypeDef = TypedDict(
    "_OptionalClientUpdateSubscriberOldSubscriberTypeDef", {"Address": str}, total=False
)


class ClientUpdateSubscriberOldSubscriberTypeDef(
    _RequiredClientUpdateSubscriberOldSubscriberTypeDef,
    _OptionalClientUpdateSubscriberOldSubscriberTypeDef,
):
    """
    The previous subscriber that is associated with a budget notification.
    - **SubscriptionType** *(string) --***[REQUIRED]**

      The type of notification that AWS sends to a subscriber.
    """


_DescribeBudgetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeBudgetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeBudgetsPaginatePaginationConfigTypeDef(
    _DescribeBudgetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef
):
    pass


_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef
):
    pass


_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef
):
    pass


_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef",
    {
        "ActualSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef
):
    pass


_DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef
):
    pass


_DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef
):
    pass


_DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef(
    _DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef
):
    pass


_DescribeBudgetsPaginateResponseBudgetsTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseBudgetsTypeDef",
    {
        "BudgetName": str,
        "BudgetLimit": DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef,
        "PlannedBudgetLimits": Dict[
            str, DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef,
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "TimePeriod": DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef,
        "CalculatedSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef,
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class DescribeBudgetsPaginateResponseBudgetsTypeDef(_DescribeBudgetsPaginateResponseBudgetsTypeDef):
    """
    - *(dict) --*

      Represents the output of the ``CreateBudget`` operation. The content consists of the detailed
      metadata and data file information, and the current status of the ``budget`` object.
      This is the ARN pattern for a budget:

        ``arn:aws:budgetservice::AccountId:budget/budgetName``
    """


_DescribeBudgetsPaginateResponseTypeDef = TypedDict(
    "_DescribeBudgetsPaginateResponseTypeDef",
    {"Budgets": List[DescribeBudgetsPaginateResponseBudgetsTypeDef]},
    total=False,
)


class DescribeBudgetsPaginateResponseTypeDef(_DescribeBudgetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Response of DescribeBudgets
      - **Budgets** *(list) --*

        A list of budgets.
        - *(dict) --*

          Represents the output of the ``CreateBudget`` operation. The content consists of the
          detailed metadata and data file information, and the current status of the ``budget``
          object.
          This is the ARN pattern for a budget:

            ``arn:aws:budgetservice::AccountId:budget/budgetName``
    """


_DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef(
    _DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef = TypedDict(
    "_DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef",
    {
        "NotificationType": Literal["ACTUAL", "FORECASTED"],
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef(
    _DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef
):
    """
    - *(dict) --*

      A notification that is associated with a budget. A budget can have up to five notifications.
      Each notification must have at least one subscriber. A notification can have one SNS
      subscriber and up to 10 email subscribers, for a total of 11 subscribers.
      For example, if you have a budget for 200 dollars and you want to be notified when you go over
      160 dollars, create a notification with the following parameters:
      * A notificationType of ``ACTUAL``
      * A ``thresholdType`` of ``PERCENTAGE``
      * A ``comparisonOperator`` of ``GREATER_THAN``
      * A notification ``threshold`` of ``80``
      - **NotificationType** *(string) --*

        Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
        forecasted to spend (``FORECASTED`` ).
    """


_DescribeNotificationsForBudgetPaginateResponseTypeDef = TypedDict(
    "_DescribeNotificationsForBudgetPaginateResponseTypeDef",
    {"Notifications": List[DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef]},
    total=False,
)


class DescribeNotificationsForBudgetPaginateResponseTypeDef(
    _DescribeNotificationsForBudgetPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Response of GetNotificationsForBudget
      - **Notifications** *(list) --*

        A list of notifications that are associated with a budget.
        - *(dict) --*

          A notification that is associated with a budget. A budget can have up to five
          notifications.
          Each notification must have at least one subscriber. A notification can have one SNS
          subscriber and up to 10 email subscribers, for a total of 11 subscribers.
          For example, if you have a budget for 200 dollars and you want to be notified when you go
          over 160 dollars, create a notification with the following parameters:
          * A notificationType of ``ACTUAL``
          * A ``thresholdType`` of ``PERCENTAGE``
          * A ``comparisonOperator`` of ``GREATER_THAN``
          * A notification ``threshold`` of ``80``
          - **NotificationType** *(string) --*

            Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much
            you're forecasted to spend (``FORECASTED`` ).
    """


_RequiredDescribeSubscribersForNotificationPaginateNotificationTypeDef = TypedDict(
    "_RequiredDescribeSubscribersForNotificationPaginateNotificationTypeDef",
    {"NotificationType": Literal["ACTUAL", "FORECASTED"]},
)
_OptionalDescribeSubscribersForNotificationPaginateNotificationTypeDef = TypedDict(
    "_OptionalDescribeSubscribersForNotificationPaginateNotificationTypeDef",
    {
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class DescribeSubscribersForNotificationPaginateNotificationTypeDef(
    _RequiredDescribeSubscribersForNotificationPaginateNotificationTypeDef,
    _OptionalDescribeSubscribersForNotificationPaginateNotificationTypeDef,
):
    """
    The notification whose subscribers you want to list.
    - **NotificationType** *(string) --***[REQUIRED]**

      Whether the notification is for how much you have spent (``ACTUAL`` ) or for how much you're
      forecasted to spend (``FORECASTED`` ).
    """


_DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef(
    _DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef = TypedDict(
    "_DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str},
    total=False,
)


class DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef(
    _DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef
):
    """
    - *(dict) --*

      The subscriber to a budget notification. The subscriber consists of a subscription type and
      either an Amazon SNS topic or an email address.
      For example, an email subscriber would have the following parameters:
      * A ``subscriptionType`` of ``EMAIL``
      * An ``address`` of ``example@example.com``
      - **SubscriptionType** *(string) --*

        The type of notification that AWS sends to a subscriber.
    """


_DescribeSubscribersForNotificationPaginateResponseTypeDef = TypedDict(
    "_DescribeSubscribersForNotificationPaginateResponseTypeDef",
    {"Subscribers": List[DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef]},
    total=False,
)


class DescribeSubscribersForNotificationPaginateResponseTypeDef(
    _DescribeSubscribersForNotificationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Response of DescribeSubscribersForNotification
      - **Subscribers** *(list) --*

        A list of subscribers that are associated with a notification.
        - *(dict) --*

          The subscriber to a budget notification. The subscriber consists of a subscription type
          and either an Amazon SNS topic or an email address.
          For example, an email subscriber would have the following parameters:
          * A ``subscriptionType`` of ``EMAIL``
          * An ``address`` of ``example@example.com``
          - **SubscriptionType** *(string) --*

            The type of notification that AWS sends to a subscriber.
    """
