"Main interface for budgets service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateBudgetBudgetBudgetLimitTypeDef = TypedDict(
    "ClientCreateBudgetBudgetBudgetLimitTypeDef", {"Amount": str, "Unit": str}, total=False
)

ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientCreateBudgetBudgetCalculatedSpendTypeDef = TypedDict(
    "ClientCreateBudgetBudgetCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientCreateBudgetBudgetCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientCreateBudgetBudgetCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)

ClientCreateBudgetBudgetCostTypesTypeDef = TypedDict(
    "ClientCreateBudgetBudgetCostTypesTypeDef",
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

ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "ClientCreateBudgetBudgetPlannedBudgetLimitsTypeDef", {"Amount": str, "Unit": str}, total=False
)

ClientCreateBudgetBudgetTimePeriodTypeDef = TypedDict(
    "ClientCreateBudgetBudgetTimePeriodTypeDef", {"Start": datetime, "End": datetime}, total=False
)

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
    pass


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
    pass


ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef = TypedDict(
    "ClientCreateBudgetNotificationsWithSubscribersSubscribersTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str},
    total=False,
)

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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)

ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTypeDef",
    {
        "BudgetedAmount": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListBudgetedAmountTypeDef,
        "ActualAmount": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListActualAmountTypeDef,
        "TimePeriod": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryBudgetedAndActualAmountsListTimePeriodTypeDef,
    },
    total=False,
)

ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryCostTypesTypeDef",
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

ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef",
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

ClientDescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": ClientDescribeBudgetPerformanceHistoryResponseBudgetPerformanceHistoryTypeDef,
        "NextToken": str,
    },
    total=False,
)

ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef = TypedDict(
    "ClientDescribeBudgetPerformanceHistoryTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)

ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientDescribeBudgetResponseBudgetCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)

ClientDescribeBudgetResponseBudgetCostTypesTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetCostTypesTypeDef",
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

ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetResponseBudgetTimePeriodTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)

ClientDescribeBudgetResponseBudgetTypeDef = TypedDict(
    "ClientDescribeBudgetResponseBudgetTypeDef",
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

ClientDescribeBudgetResponseTypeDef = TypedDict(
    "ClientDescribeBudgetResponseTypeDef",
    {"Budget": ClientDescribeBudgetResponseBudgetTypeDef},
    total=False,
)

ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientDescribeBudgetsResponseBudgetsCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)

ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsCostTypesTypeDef",
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

ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)

ClientDescribeBudgetsResponseBudgetsTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseBudgetsTypeDef",
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

ClientDescribeBudgetsResponseTypeDef = TypedDict(
    "ClientDescribeBudgetsResponseTypeDef",
    {"Budgets": List[ClientDescribeBudgetsResponseBudgetsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef = TypedDict(
    "ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef",
    {
        "NotificationType": Literal["ACTUAL", "FORECASTED"],
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)

ClientDescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "ClientDescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List[ClientDescribeNotificationsForBudgetResponseNotificationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

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
    pass


ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef = TypedDict(
    "ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str},
    total=False,
)

ClientDescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "ClientDescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List[ClientDescribeSubscribersForNotificationResponseSubscribersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientUpdateBudgetNewBudgetBudgetLimitTypeDef = TypedDict(
    "ClientUpdateBudgetNewBudgetBudgetLimitTypeDef", {"Amount": str, "Unit": str}, total=False
)

ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef = TypedDict(
    "ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef = TypedDict(
    "ClientUpdateBudgetNewBudgetCalculatedSpendTypeDef",
    {
        "ActualSpend": ClientUpdateBudgetNewBudgetCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": ClientUpdateBudgetNewBudgetCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)

ClientUpdateBudgetNewBudgetCostTypesTypeDef = TypedDict(
    "ClientUpdateBudgetNewBudgetCostTypesTypeDef",
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

ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef = TypedDict(
    "ClientUpdateBudgetNewBudgetPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

ClientUpdateBudgetNewBudgetTimePeriodTypeDef = TypedDict(
    "ClientUpdateBudgetNewBudgetTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)

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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


DescribeBudgetsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeBudgetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsBudgetLimitTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsCalculatedSpendTypeDef",
    {
        "ActualSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendActualSpendTypeDef,
        "ForecastedSpend": DescribeBudgetsPaginateResponseBudgetsCalculatedSpendForecastedSpendTypeDef,
    },
    total=False,
)

DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsCostTypesTypeDef",
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

DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsPlannedBudgetLimitsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)

DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsTimePeriodTypeDef",
    {"Start": datetime, "End": datetime},
    total=False,
)

DescribeBudgetsPaginateResponseBudgetsTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseBudgetsTypeDef",
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

DescribeBudgetsPaginateResponseTypeDef = TypedDict(
    "DescribeBudgetsPaginateResponseTypeDef",
    {"Budgets": List[DescribeBudgetsPaginateResponseBudgetsTypeDef]},
    total=False,
)

DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeNotificationsForBudgetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef = TypedDict(
    "DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef",
    {
        "NotificationType": Literal["ACTUAL", "FORECASTED"],
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)

DescribeNotificationsForBudgetPaginateResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetPaginateResponseTypeDef",
    {"Notifications": List[DescribeNotificationsForBudgetPaginateResponseNotificationsTypeDef]},
    total=False,
)

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
    pass


DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeSubscribersForNotificationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef = TypedDict(
    "DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef",
    {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str},
    total=False,
)

DescribeSubscribersForNotificationPaginateResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationPaginateResponseTypeDef",
    {"Subscribers": List[DescribeSubscribersForNotificationPaginateResponseSubscribersTypeDef]},
    total=False,
)
