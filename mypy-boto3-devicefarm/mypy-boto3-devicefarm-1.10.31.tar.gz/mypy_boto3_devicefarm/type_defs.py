"Main interface for devicefarm service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateDevicePoolResponsedevicePoolrulesTypeDef",
    "ClientCreateDevicePoolResponsedevicePoolTypeDef",
    "ClientCreateDevicePoolResponseTypeDef",
    "ClientCreateDevicePoolRulesTypeDef",
    "ClientCreateInstanceProfileResponseinstanceProfileTypeDef",
    "ClientCreateInstanceProfileResponseTypeDef",
    "ClientCreateNetworkProfileResponsenetworkProfileTypeDef",
    "ClientCreateNetworkProfileResponseTypeDef",
    "ClientCreateProjectResponseprojectTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateRemoteAccessSessionConfigurationTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    "ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    "ClientCreateRemoteAccessSessionResponseTypeDef",
    "ClientCreateUploadResponseuploadTypeDef",
    "ClientCreateUploadResponseTypeDef",
    "ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef",
    "ClientCreateVpceConfigurationResponseTypeDef",
    "ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef",
    "ClientGetAccountSettingsResponseaccountSettingsTypeDef",
    "ClientGetAccountSettingsResponseTypeDef",
    "ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    "ClientGetDeviceInstanceResponsedeviceInstanceTypeDef",
    "ClientGetDeviceInstanceResponseTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef",
    "ClientGetDevicePoolCompatibilityConfigurationTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef",
    "ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef",
    "ClientGetDevicePoolCompatibilityResponseTypeDef",
    "ClientGetDevicePoolCompatibilityTestTypeDef",
    "ClientGetDevicePoolResponsedevicePoolrulesTypeDef",
    "ClientGetDevicePoolResponsedevicePoolTypeDef",
    "ClientGetDevicePoolResponseTypeDef",
    "ClientGetDeviceResponsedevicecpuTypeDef",
    "ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef",
    "ClientGetDeviceResponsedeviceinstancesTypeDef",
    "ClientGetDeviceResponsedeviceresolutionTypeDef",
    "ClientGetDeviceResponsedeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetInstanceProfileResponseinstanceProfileTypeDef",
    "ClientGetInstanceProfileResponseTypeDef",
    "ClientGetJobResponsejobcountersTypeDef",
    "ClientGetJobResponsejobdeviceMinutesTypeDef",
    "ClientGetJobResponsejobdevicecpuTypeDef",
    "ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    "ClientGetJobResponsejobdeviceinstancesTypeDef",
    "ClientGetJobResponsejobdeviceresolutionTypeDef",
    "ClientGetJobResponsejobdeviceTypeDef",
    "ClientGetJobResponsejobTypeDef",
    "ClientGetJobResponseTypeDef",
    "ClientGetNetworkProfileResponsenetworkProfileTypeDef",
    "ClientGetNetworkProfileResponseTypeDef",
    "ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef",
    "ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef",
    "ClientGetOfferingStatusResponsecurrentofferingTypeDef",
    "ClientGetOfferingStatusResponsecurrentTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodofferingTypeDef",
    "ClientGetOfferingStatusResponsenextPeriodTypeDef",
    "ClientGetOfferingStatusResponseTypeDef",
    "ClientGetProjectResponseprojectTypeDef",
    "ClientGetProjectResponseTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    "ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    "ClientGetRemoteAccessSessionResponseTypeDef",
    "ClientGetRunResponseruncountersTypeDef",
    "ClientGetRunResponseruncustomerArtifactPathsTypeDef",
    "ClientGetRunResponserundeviceMinutesTypeDef",
    "ClientGetRunResponserundeviceSelectionResultfiltersTypeDef",
    "ClientGetRunResponserundeviceSelectionResultTypeDef",
    "ClientGetRunResponserunlocationTypeDef",
    "ClientGetRunResponserunnetworkProfileTypeDef",
    "ClientGetRunResponserunradiosTypeDef",
    "ClientGetRunResponserunTypeDef",
    "ClientGetRunResponseTypeDef",
    "ClientGetSuiteResponsesuitecountersTypeDef",
    "ClientGetSuiteResponsesuitedeviceMinutesTypeDef",
    "ClientGetSuiteResponsesuiteTypeDef",
    "ClientGetSuiteResponseTypeDef",
    "ClientGetTestResponsetestcountersTypeDef",
    "ClientGetTestResponsetestdeviceMinutesTypeDef",
    "ClientGetTestResponsetestTypeDef",
    "ClientGetTestResponseTypeDef",
    "ClientGetUploadResponseuploadTypeDef",
    "ClientGetUploadResponseTypeDef",
    "ClientGetVpceConfigurationResponsevpceConfigurationTypeDef",
    "ClientGetVpceConfigurationResponseTypeDef",
    "ClientInstallToRemoteAccessSessionResponseappUploadTypeDef",
    "ClientInstallToRemoteAccessSessionResponseTypeDef",
    "ClientListArtifactsResponseartifactsTypeDef",
    "ClientListArtifactsResponseTypeDef",
    "ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef",
    "ClientListDeviceInstancesResponsedeviceInstancesTypeDef",
    "ClientListDeviceInstancesResponseTypeDef",
    "ClientListDevicePoolsResponsedevicePoolsrulesTypeDef",
    "ClientListDevicePoolsResponsedevicePoolsTypeDef",
    "ClientListDevicePoolsResponseTypeDef",
    "ClientListDevicesFiltersTypeDef",
    "ClientListDevicesResponsedevicescpuTypeDef",
    "ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef",
    "ClientListDevicesResponsedevicesinstancesTypeDef",
    "ClientListDevicesResponsedevicesresolutionTypeDef",
    "ClientListDevicesResponsedevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListInstanceProfilesResponseinstanceProfilesTypeDef",
    "ClientListInstanceProfilesResponseTypeDef",
    "ClientListJobsResponsejobscountersTypeDef",
    "ClientListJobsResponsejobsdeviceMinutesTypeDef",
    "ClientListJobsResponsejobsdevicecpuTypeDef",
    "ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef",
    "ClientListJobsResponsejobsdeviceinstancesTypeDef",
    "ClientListJobsResponsejobsdeviceresolutionTypeDef",
    "ClientListJobsResponsejobsdeviceTypeDef",
    "ClientListJobsResponsejobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListNetworkProfilesResponsenetworkProfilesTypeDef",
    "ClientListNetworkProfilesResponseTypeDef",
    "ClientListOfferingPromotionsResponseofferingPromotionsTypeDef",
    "ClientListOfferingPromotionsResponseTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef",
    "ClientListOfferingTransactionsResponseofferingTransactionsTypeDef",
    "ClientListOfferingTransactionsResponseTypeDef",
    "ClientListOfferingsResponseofferingsrecurringChargescostTypeDef",
    "ClientListOfferingsResponseofferingsrecurringChargesTypeDef",
    "ClientListOfferingsResponseofferingsTypeDef",
    "ClientListOfferingsResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef",
    "ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef",
    "ClientListRemoteAccessSessionsResponseTypeDef",
    "ClientListRunsResponserunscountersTypeDef",
    "ClientListRunsResponserunscustomerArtifactPathsTypeDef",
    "ClientListRunsResponserunsdeviceMinutesTypeDef",
    "ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef",
    "ClientListRunsResponserunsdeviceSelectionResultTypeDef",
    "ClientListRunsResponserunslocationTypeDef",
    "ClientListRunsResponserunsnetworkProfileTypeDef",
    "ClientListRunsResponserunsradiosTypeDef",
    "ClientListRunsResponserunsTypeDef",
    "ClientListRunsResponseTypeDef",
    "ClientListSamplesResponsesamplesTypeDef",
    "ClientListSamplesResponseTypeDef",
    "ClientListSuitesResponsesuitescountersTypeDef",
    "ClientListSuitesResponsesuitesdeviceMinutesTypeDef",
    "ClientListSuitesResponsesuitesTypeDef",
    "ClientListSuitesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTestsResponsetestscountersTypeDef",
    "ClientListTestsResponsetestsdeviceMinutesTypeDef",
    "ClientListTestsResponsetestsTypeDef",
    "ClientListTestsResponseTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef",
    "ClientListUniqueProblemsResponseuniqueProblemsTypeDef",
    "ClientListUniqueProblemsResponseTypeDef",
    "ClientListUploadsResponseuploadsTypeDef",
    "ClientListUploadsResponseTypeDef",
    "ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef",
    "ClientListVpceConfigurationsResponseTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactioncostTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef",
    "ClientPurchaseOfferingResponseofferingTransactionTypeDef",
    "ClientPurchaseOfferingResponseTypeDef",
    "ClientRenewOfferingResponseofferingTransactioncostTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    "ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef",
    "ClientRenewOfferingResponseofferingTransactionTypeDef",
    "ClientRenewOfferingResponseTypeDef",
    "ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef",
    "ClientScheduleRunConfigurationlocationTypeDef",
    "ClientScheduleRunConfigurationradiosTypeDef",
    "ClientScheduleRunConfigurationTypeDef",
    "ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef",
    "ClientScheduleRunDeviceSelectionConfigurationTypeDef",
    "ClientScheduleRunExecutionConfigurationTypeDef",
    "ClientScheduleRunResponseruncountersTypeDef",
    "ClientScheduleRunResponseruncustomerArtifactPathsTypeDef",
    "ClientScheduleRunResponserundeviceMinutesTypeDef",
    "ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef",
    "ClientScheduleRunResponserundeviceSelectionResultTypeDef",
    "ClientScheduleRunResponserunlocationTypeDef",
    "ClientScheduleRunResponserunnetworkProfileTypeDef",
    "ClientScheduleRunResponserunradiosTypeDef",
    "ClientScheduleRunResponserunTypeDef",
    "ClientScheduleRunResponseTypeDef",
    "ClientScheduleRunTestTypeDef",
    "ClientStopJobResponsejobcountersTypeDef",
    "ClientStopJobResponsejobdeviceMinutesTypeDef",
    "ClientStopJobResponsejobdevicecpuTypeDef",
    "ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    "ClientStopJobResponsejobdeviceinstancesTypeDef",
    "ClientStopJobResponsejobdeviceresolutionTypeDef",
    "ClientStopJobResponsejobdeviceTypeDef",
    "ClientStopJobResponsejobTypeDef",
    "ClientStopJobResponseTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    "ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    "ClientStopRemoteAccessSessionResponseTypeDef",
    "ClientStopRunResponseruncountersTypeDef",
    "ClientStopRunResponseruncustomerArtifactPathsTypeDef",
    "ClientStopRunResponserundeviceMinutesTypeDef",
    "ClientStopRunResponserundeviceSelectionResultfiltersTypeDef",
    "ClientStopRunResponserundeviceSelectionResultTypeDef",
    "ClientStopRunResponserunlocationTypeDef",
    "ClientStopRunResponserunnetworkProfileTypeDef",
    "ClientStopRunResponserunradiosTypeDef",
    "ClientStopRunResponserunTypeDef",
    "ClientStopRunResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    "ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef",
    "ClientUpdateDeviceInstanceResponseTypeDef",
    "ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef",
    "ClientUpdateDevicePoolResponsedevicePoolTypeDef",
    "ClientUpdateDevicePoolResponseTypeDef",
    "ClientUpdateDevicePoolRulesTypeDef",
    "ClientUpdateInstanceProfileResponseinstanceProfileTypeDef",
    "ClientUpdateInstanceProfileResponseTypeDef",
    "ClientUpdateNetworkProfileResponsenetworkProfileTypeDef",
    "ClientUpdateNetworkProfileResponseTypeDef",
    "ClientUpdateProjectResponseprojectTypeDef",
    "ClientUpdateProjectResponseTypeDef",
    "ClientUpdateUploadResponseuploadTypeDef",
    "ClientUpdateUploadResponseTypeDef",
    "ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef",
    "ClientUpdateVpceConfigurationResponseTypeDef",
    "GetOfferingStatusPaginatePaginationConfigTypeDef",
    "GetOfferingStatusPaginateResponsecurrentofferingrecurringChargescostTypeDef",
    "GetOfferingStatusPaginateResponsecurrentofferingrecurringChargesTypeDef",
    "GetOfferingStatusPaginateResponsecurrentofferingTypeDef",
    "GetOfferingStatusPaginateResponsecurrentTypeDef",
    "GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargescostTypeDef",
    "GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargesTypeDef",
    "GetOfferingStatusPaginateResponsenextPeriodofferingTypeDef",
    "GetOfferingStatusPaginateResponsenextPeriodTypeDef",
    "GetOfferingStatusPaginateResponseTypeDef",
    "ListArtifactsPaginatePaginationConfigTypeDef",
    "ListArtifactsPaginateResponseartifactsTypeDef",
    "ListArtifactsPaginateResponseTypeDef",
    "ListDeviceInstancesPaginatePaginationConfigTypeDef",
    "ListDeviceInstancesPaginateResponsedeviceInstancesinstanceProfileTypeDef",
    "ListDeviceInstancesPaginateResponsedeviceInstancesTypeDef",
    "ListDeviceInstancesPaginateResponseTypeDef",
    "ListDevicePoolsPaginatePaginationConfigTypeDef",
    "ListDevicePoolsPaginateResponsedevicePoolsrulesTypeDef",
    "ListDevicePoolsPaginateResponsedevicePoolsTypeDef",
    "ListDevicePoolsPaginateResponseTypeDef",
    "ListDevicesPaginateFiltersTypeDef",
    "ListDevicesPaginatePaginationConfigTypeDef",
    "ListDevicesPaginateResponsedevicescpuTypeDef",
    "ListDevicesPaginateResponsedevicesinstancesinstanceProfileTypeDef",
    "ListDevicesPaginateResponsedevicesinstancesTypeDef",
    "ListDevicesPaginateResponsedevicesresolutionTypeDef",
    "ListDevicesPaginateResponsedevicesTypeDef",
    "ListDevicesPaginateResponseTypeDef",
    "ListInstanceProfilesPaginatePaginationConfigTypeDef",
    "ListInstanceProfilesPaginateResponseinstanceProfilesTypeDef",
    "ListInstanceProfilesPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponsejobscountersTypeDef",
    "ListJobsPaginateResponsejobsdeviceMinutesTypeDef",
    "ListJobsPaginateResponsejobsdevicecpuTypeDef",
    "ListJobsPaginateResponsejobsdeviceinstancesinstanceProfileTypeDef",
    "ListJobsPaginateResponsejobsdeviceinstancesTypeDef",
    "ListJobsPaginateResponsejobsdeviceresolutionTypeDef",
    "ListJobsPaginateResponsejobsdeviceTypeDef",
    "ListJobsPaginateResponsejobsTypeDef",
    "ListJobsPaginateResponseTypeDef",
    "ListNetworkProfilesPaginatePaginationConfigTypeDef",
    "ListNetworkProfilesPaginateResponsenetworkProfilesTypeDef",
    "ListNetworkProfilesPaginateResponseTypeDef",
    "ListOfferingPromotionsPaginatePaginationConfigTypeDef",
    "ListOfferingPromotionsPaginateResponseofferingPromotionsTypeDef",
    "ListOfferingPromotionsPaginateResponseTypeDef",
    "ListOfferingTransactionsPaginatePaginationConfigTypeDef",
    "ListOfferingTransactionsPaginateResponseofferingTransactionscostTypeDef",
    "ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef",
    "ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef",
    "ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingTypeDef",
    "ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusTypeDef",
    "ListOfferingTransactionsPaginateResponseofferingTransactionsTypeDef",
    "ListOfferingTransactionsPaginateResponseTypeDef",
    "ListOfferingsPaginatePaginationConfigTypeDef",
    "ListOfferingsPaginateResponseofferingsrecurringChargescostTypeDef",
    "ListOfferingsPaginateResponseofferingsrecurringChargesTypeDef",
    "ListOfferingsPaginateResponseofferingsTypeDef",
    "ListOfferingsPaginateResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseprojectsTypeDef",
    "ListProjectsPaginateResponseTypeDef",
    "ListRemoteAccessSessionsPaginatePaginationConfigTypeDef",
    "ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceMinutesTypeDef",
    "ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdevicecpuTypeDef",
    "ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef",
    "ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesTypeDef",
    "ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceresolutionTypeDef",
    "ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceTypeDef",
    "ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsTypeDef",
    "ListRemoteAccessSessionsPaginateResponseTypeDef",
    "ListRunsPaginatePaginationConfigTypeDef",
    "ListRunsPaginateResponserunscountersTypeDef",
    "ListRunsPaginateResponserunscustomerArtifactPathsTypeDef",
    "ListRunsPaginateResponserunsdeviceMinutesTypeDef",
    "ListRunsPaginateResponserunsdeviceSelectionResultfiltersTypeDef",
    "ListRunsPaginateResponserunsdeviceSelectionResultTypeDef",
    "ListRunsPaginateResponserunslocationTypeDef",
    "ListRunsPaginateResponserunsnetworkProfileTypeDef",
    "ListRunsPaginateResponserunsradiosTypeDef",
    "ListRunsPaginateResponserunsTypeDef",
    "ListRunsPaginateResponseTypeDef",
    "ListSamplesPaginatePaginationConfigTypeDef",
    "ListSamplesPaginateResponsesamplesTypeDef",
    "ListSamplesPaginateResponseTypeDef",
    "ListSuitesPaginatePaginationConfigTypeDef",
    "ListSuitesPaginateResponsesuitescountersTypeDef",
    "ListSuitesPaginateResponsesuitesdeviceMinutesTypeDef",
    "ListSuitesPaginateResponsesuitesTypeDef",
    "ListSuitesPaginateResponseTypeDef",
    "ListTestsPaginatePaginationConfigTypeDef",
    "ListTestsPaginateResponsetestscountersTypeDef",
    "ListTestsPaginateResponsetestsdeviceMinutesTypeDef",
    "ListTestsPaginateResponsetestsTypeDef",
    "ListTestsPaginateResponseTypeDef",
    "ListUniqueProblemsPaginatePaginationConfigTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdevicecpuTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceresolutionTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsjobTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsrunTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemssuiteTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemstestTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsproblemsTypeDef",
    "ListUniqueProblemsPaginateResponseuniqueProblemsTypeDef",
    "ListUniqueProblemsPaginateResponseTypeDef",
    "ListUploadsPaginatePaginationConfigTypeDef",
    "ListUploadsPaginateResponseuploadsTypeDef",
    "ListUploadsPaginateResponseTypeDef",
    "ListVPCEConfigurationsPaginatePaginationConfigTypeDef",
    "ListVPCEConfigurationsPaginateResponsevpceConfigurationsTypeDef",
    "ListVPCEConfigurationsPaginateResponseTypeDef",
)


_ClientCreateDevicePoolResponsedevicePoolrulesTypeDef = TypedDict(
    "_ClientCreateDevicePoolResponsedevicePoolrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)


class ClientCreateDevicePoolResponsedevicePoolrulesTypeDef(
    _ClientCreateDevicePoolResponsedevicePoolrulesTypeDef
):
    pass


_ClientCreateDevicePoolResponsedevicePoolTypeDef = TypedDict(
    "_ClientCreateDevicePoolResponsedevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientCreateDevicePoolResponsedevicePoolrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)


class ClientCreateDevicePoolResponsedevicePoolTypeDef(
    _ClientCreateDevicePoolResponsedevicePoolTypeDef
):
    """
    - **devicePool** *(dict) --*

      The newly created device pool.
      - **arn** *(string) --*

        The device pool's ARN.
    """


_ClientCreateDevicePoolResponseTypeDef = TypedDict(
    "_ClientCreateDevicePoolResponseTypeDef",
    {"devicePool": ClientCreateDevicePoolResponsedevicePoolTypeDef},
    total=False,
)


class ClientCreateDevicePoolResponseTypeDef(_ClientCreateDevicePoolResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a create device pool request.
      - **devicePool** *(dict) --*

        The newly created device pool.
        - **arn** *(string) --*

          The device pool's ARN.
    """


_ClientCreateDevicePoolRulesTypeDef = TypedDict(
    "_ClientCreateDevicePoolRulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)


class ClientCreateDevicePoolRulesTypeDef(_ClientCreateDevicePoolRulesTypeDef):
    """
    - *(dict) --*

      Represents a condition for a device pool.
      - **attribute** *(string) --*

        The rule's stringified attribute. For example, specify the value as ``"\\"abc\\""`` .
        The supported operators for each attribute are provided in the following list.

          APPIUM_VERSION
    """


_ClientCreateInstanceProfileResponseinstanceProfileTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientCreateInstanceProfileResponseinstanceProfileTypeDef(
    _ClientCreateInstanceProfileResponseinstanceProfileTypeDef
):
    """
    - **instanceProfile** *(dict) --*

      An object containing information about your instance profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientCreateInstanceProfileResponseTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseTypeDef",
    {"instanceProfile": ClientCreateInstanceProfileResponseinstanceProfileTypeDef},
    total=False,
)


class ClientCreateInstanceProfileResponseTypeDef(_ClientCreateInstanceProfileResponseTypeDef):
    """
    - *(dict) --*

      - **instanceProfile** *(dict) --*

        An object containing information about your instance profile.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientCreateNetworkProfileResponsenetworkProfileTypeDef = TypedDict(
    "_ClientCreateNetworkProfileResponsenetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientCreateNetworkProfileResponsenetworkProfileTypeDef(
    _ClientCreateNetworkProfileResponsenetworkProfileTypeDef
):
    """
    - **networkProfile** *(dict) --*

      The network profile that is returned by the create network profile request.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the network profile.
    """


_ClientCreateNetworkProfileResponseTypeDef = TypedDict(
    "_ClientCreateNetworkProfileResponseTypeDef",
    {"networkProfile": ClientCreateNetworkProfileResponsenetworkProfileTypeDef},
    total=False,
)


class ClientCreateNetworkProfileResponseTypeDef(_ClientCreateNetworkProfileResponseTypeDef):
    """
    - *(dict) --*

      - **networkProfile** *(dict) --*

        The network profile that is returned by the create network profile request.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the network profile.
    """


_ClientCreateProjectResponseprojectTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)


class ClientCreateProjectResponseprojectTypeDef(_ClientCreateProjectResponseprojectTypeDef):
    """
    - **project** *(dict) --*

      The newly created project.
      - **arn** *(string) --*

        The project's ARN.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef",
    {"project": ClientCreateProjectResponseprojectTypeDef},
    total=False,
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a create project request.
      - **project** *(dict) --*

        The newly created project.
        - **arn** *(string) --*

          The project's ARN.
    """


_ClientCreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionConfigurationTypeDef",
    {"billingMethod": Literal["METERED", "UNMETERED"], "vpceConfigurationArns": List[str]},
    total=False,
)


class ClientCreateRemoteAccessSessionConfigurationTypeDef(
    _ClientCreateRemoteAccessSessionConfigurationTypeDef
):
    """
    The configuration information for the remote access session request.
    - **billingMethod** *(string) --*

      The billing method for the remote access session.
    """


_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef(
    _ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef
):
    pass


_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef(
    _ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef
):
    pass


_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef(
    _ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef(
    _ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
):
    pass


_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef(
    _ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef
):
    pass


_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef,
        "resolution": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef(
    _ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef
):
    pass


_ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientCreateRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)


class ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef(
    _ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef
):
    """
    - **remoteAccessSession** *(dict) --*

      A container that describes the remote access session when the request to create a remote
      access session is sent.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientCreateRemoteAccessSessionResponseTypeDef = TypedDict(
    "_ClientCreateRemoteAccessSessionResponseTypeDef",
    {"remoteAccessSession": ClientCreateRemoteAccessSessionResponseremoteAccessSessionTypeDef},
    total=False,
)


class ClientCreateRemoteAccessSessionResponseTypeDef(
    _ClientCreateRemoteAccessSessionResponseTypeDef
):
    """
    - *(dict) --*

      Represents the server response from a request to create a remote access session.
      - **remoteAccessSession** *(dict) --*

        A container that describes the remote access session when the request to create a remote
        access session is sent.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientCreateUploadResponseuploadTypeDef = TypedDict(
    "_ClientCreateUploadResponseuploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)


class ClientCreateUploadResponseuploadTypeDef(_ClientCreateUploadResponseuploadTypeDef):
    """
    - **upload** *(dict) --*

      The newly created upload.
      - **arn** *(string) --*

        The upload's ARN.
    """


_ClientCreateUploadResponseTypeDef = TypedDict(
    "_ClientCreateUploadResponseTypeDef",
    {"upload": ClientCreateUploadResponseuploadTypeDef},
    total=False,
)


class ClientCreateUploadResponseTypeDef(_ClientCreateUploadResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a create upload request.
      - **upload** *(dict) --*

        The newly created upload.
        - **arn** *(string) --*

          The upload's ARN.
    """


_ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef = TypedDict(
    "_ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)


class ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef(
    _ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef
):
    """
    - **vpceConfiguration** *(dict) --*

      An object containing information about your VPC endpoint configuration.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ClientCreateVpceConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateVpceConfigurationResponseTypeDef",
    {"vpceConfiguration": ClientCreateVpceConfigurationResponsevpceConfigurationTypeDef},
    total=False,
)


class ClientCreateVpceConfigurationResponseTypeDef(_ClientCreateVpceConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **vpceConfiguration** *(dict) --*

        An object containing information about your VPC endpoint configuration.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef",
    {"total": float, "remaining": float},
    total=False,
)


class ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef(
    _ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef
):
    pass


_ClientGetAccountSettingsResponseaccountSettingsTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseaccountSettingsTypeDef",
    {
        "awsAccountNumber": str,
        "unmeteredDevices": Dict[str, int],
        "unmeteredRemoteAccessDevices": Dict[str, int],
        "maxJobTimeoutMinutes": int,
        "trialMinutes": ClientGetAccountSettingsResponseaccountSettingstrialMinutesTypeDef,
        "maxSlots": Dict[str, int],
        "defaultJobTimeoutMinutes": int,
        "skipAppResign": bool,
    },
    total=False,
)


class ClientGetAccountSettingsResponseaccountSettingsTypeDef(
    _ClientGetAccountSettingsResponseaccountSettingsTypeDef
):
    """
    - **accountSettings** *(dict) --*

      The account settings.
      - **awsAccountNumber** *(string) --*

        The AWS account number specified in the ``AccountSettings`` container.
    """


_ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseTypeDef",
    {"accountSettings": ClientGetAccountSettingsResponseaccountSettingsTypeDef},
    total=False,
)


class ClientGetAccountSettingsResponseTypeDef(_ClientGetAccountSettingsResponseTypeDef):
    """
    - *(dict) --*

      Represents the account settings return values from the ``GetAccountSettings`` request.
      - **accountSettings** *(dict) --*

        The account settings.
        - **awsAccountNumber** *(string) --*

          The AWS account number specified in the ``AccountSettings`` container.
    """


_ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef = TypedDict(
    "_ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef(
    _ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef
):
    pass


_ClientGetDeviceInstanceResponsedeviceInstanceTypeDef = TypedDict(
    "_ClientGetDeviceInstanceResponsedeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef,
    },
    total=False,
)


class ClientGetDeviceInstanceResponsedeviceInstanceTypeDef(
    _ClientGetDeviceInstanceResponsedeviceInstanceTypeDef
):
    """
    - **deviceInstance** *(dict) --*

      An object containing information about your device instance.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the device instance.
    """


_ClientGetDeviceInstanceResponseTypeDef = TypedDict(
    "_ClientGetDeviceInstanceResponseTypeDef",
    {"deviceInstance": ClientGetDeviceInstanceResponsedeviceInstanceTypeDef},
    total=False,
)


class ClientGetDeviceInstanceResponseTypeDef(_ClientGetDeviceInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **deviceInstance** *(dict) --*

        An object containing information about your device instance.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the device instance.
    """


_ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)


class ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef(
    _ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)


class ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef(
    _ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)


class ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef(
    _ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityConfigurationTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": ClientGetDevicePoolCompatibilityConfigurationlocationTypeDef,
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": ClientGetDevicePoolCompatibilityConfigurationcustomerArtifactPathsTypeDef,
        "radios": ClientGetDevicePoolCompatibilityConfigurationradiosTypeDef,
        "auxiliaryApps": List[str],
        "billingMethod": Literal["METERED", "UNMETERED"],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityConfigurationTypeDef(
    _ClientGetDevicePoolCompatibilityConfigurationTypeDef
):
    """
    An object containing information about the settings for a run.
    - **extraDataPackageArn** *(string) --*

      The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will
      extract to external data for Android or the app's sandbox for iOS.
    """


_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef(
    _ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef(
    _ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef(
    _ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef(
    _ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdevicecpuTypeDef,
        "resolution": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef(
    _ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef
):
    """
    - **device** *(dict) --*

      The device (phone or tablet) that you wish to return information about.
      - **arn** *(string) --*

        The device's ARN.
    """


_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef",
    {
        "message": str,
        "type": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef(
    _ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef",
    {
        "device": ClientGetDevicePoolCompatibilityResponsecompatibleDevicesdeviceTypeDef,
        "compatible": bool,
        "incompatibilityMessages": List[
            ClientGetDevicePoolCompatibilityResponsecompatibleDevicesincompatibilityMessagesTypeDef
        ],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef(
    _ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef
):
    """
    - *(dict) --*

      Represents a device pool compatibility result.
      - **device** *(dict) --*

        The device (phone or tablet) that you wish to return information about.
        - **arn** *(string) --*

          The device's ARN.
    """


_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef(
    _ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef(
    _ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef(
    _ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef(
    _ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdevicecpuTypeDef,
        "resolution": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef(
    _ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef",
    {
        "message": str,
        "type": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef(
    _ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef",
    {
        "device": ClientGetDevicePoolCompatibilityResponseincompatibleDevicesdeviceTypeDef,
        "compatible": bool,
        "incompatibilityMessages": List[
            ClientGetDevicePoolCompatibilityResponseincompatibleDevicesincompatibilityMessagesTypeDef
        ],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef(
    _ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef
):
    pass


_ClientGetDevicePoolCompatibilityResponseTypeDef = TypedDict(
    "_ClientGetDevicePoolCompatibilityResponseTypeDef",
    {
        "compatibleDevices": List[ClientGetDevicePoolCompatibilityResponsecompatibleDevicesTypeDef],
        "incompatibleDevices": List[
            ClientGetDevicePoolCompatibilityResponseincompatibleDevicesTypeDef
        ],
    },
    total=False,
)


class ClientGetDevicePoolCompatibilityResponseTypeDef(
    _ClientGetDevicePoolCompatibilityResponseTypeDef
):
    """
    - *(dict) --*

      Represents the result of describe device pool compatibility request.
      - **compatibleDevices** *(list) --*

        Information about compatible devices.
        - *(dict) --*

          Represents a device pool compatibility result.
          - **device** *(dict) --*

            The device (phone or tablet) that you wish to return information about.
            - **arn** *(string) --*

              The device's ARN.
    """


_RequiredClientGetDevicePoolCompatibilityTestTypeDef = TypedDict(
    "_RequiredClientGetDevicePoolCompatibilityTestTypeDef",
    {
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ]
    },
)
_OptionalClientGetDevicePoolCompatibilityTestTypeDef = TypedDict(
    "_OptionalClientGetDevicePoolCompatibilityTestTypeDef",
    {"testPackageArn": str, "testSpecArn": str, "filter": str, "parameters": Dict[str, str]},
    total=False,
)


class ClientGetDevicePoolCompatibilityTestTypeDef(
    _RequiredClientGetDevicePoolCompatibilityTestTypeDef,
    _OptionalClientGetDevicePoolCompatibilityTestTypeDef,
):
    """
    Information about the uploaded test to be run against the device pool.
    - **type** *(string) --***[REQUIRED]**

      The test's type.
      Must be one of the following values:
      * BUILTIN_FUZZ: The built-in fuzz type.
      * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app,
      interacting with it and capturing screenshots at the same time.
      * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
      * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
      * APPIUM_PYTHON: The Appium Python type.
      * APPIUM_NODE: The Appium Node.js type.
      * APPIUM_RUBY: The Appium Ruby type.
      * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
      * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
      * APPIUM_WEB_PYTHON: The Appium Python type for web apps.
      * APPIUM_WEB_NODE: The Appium Node.js type for web apps.
      * APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
      * CALABASH: The Calabash type.
      * INSTRUMENTATION: The Instrumentation type.
      * UIAUTOMATION: The uiautomation type.
      * UIAUTOMATOR: The uiautomator type.
      * XCTEST: The Xcode test type.
      * XCTEST_UI: The Xcode UI test type.
    """


_ClientGetDevicePoolResponsedevicePoolrulesTypeDef = TypedDict(
    "_ClientGetDevicePoolResponsedevicePoolrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)


class ClientGetDevicePoolResponsedevicePoolrulesTypeDef(
    _ClientGetDevicePoolResponsedevicePoolrulesTypeDef
):
    pass


_ClientGetDevicePoolResponsedevicePoolTypeDef = TypedDict(
    "_ClientGetDevicePoolResponsedevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientGetDevicePoolResponsedevicePoolrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)


class ClientGetDevicePoolResponsedevicePoolTypeDef(_ClientGetDevicePoolResponsedevicePoolTypeDef):
    """
    - **devicePool** *(dict) --*

      An object containing information about the requested device pool.
      - **arn** *(string) --*

        The device pool's ARN.
    """


_ClientGetDevicePoolResponseTypeDef = TypedDict(
    "_ClientGetDevicePoolResponseTypeDef",
    {"devicePool": ClientGetDevicePoolResponsedevicePoolTypeDef},
    total=False,
)


class ClientGetDevicePoolResponseTypeDef(_ClientGetDevicePoolResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get device pool request.
      - **devicePool** *(dict) --*

        An object containing information about the requested device pool.
        - **arn** *(string) --*

          The device pool's ARN.
    """


_ClientGetDeviceResponsedevicecpuTypeDef = TypedDict(
    "_ClientGetDeviceResponsedevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientGetDeviceResponsedevicecpuTypeDef(_ClientGetDeviceResponsedevicecpuTypeDef):
    pass


_ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef(
    _ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientGetDeviceResponsedeviceinstancesTypeDef = TypedDict(
    "_ClientGetDeviceResponsedeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetDeviceResponsedeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientGetDeviceResponsedeviceinstancesTypeDef(_ClientGetDeviceResponsedeviceinstancesTypeDef):
    pass


_ClientGetDeviceResponsedeviceresolutionTypeDef = TypedDict(
    "_ClientGetDeviceResponsedeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)


class ClientGetDeviceResponsedeviceresolutionTypeDef(
    _ClientGetDeviceResponsedeviceresolutionTypeDef
):
    pass


_ClientGetDeviceResponsedeviceTypeDef = TypedDict(
    "_ClientGetDeviceResponsedeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetDeviceResponsedevicecpuTypeDef,
        "resolution": ClientGetDeviceResponsedeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientGetDeviceResponsedeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientGetDeviceResponsedeviceTypeDef(_ClientGetDeviceResponsedeviceTypeDef):
    """
    - **device** *(dict) --*

      An object containing information about the requested device.
      - **arn** *(string) --*

        The device's ARN.
    """


_ClientGetDeviceResponseTypeDef = TypedDict(
    "_ClientGetDeviceResponseTypeDef", {"device": ClientGetDeviceResponsedeviceTypeDef}, total=False
)


class ClientGetDeviceResponseTypeDef(_ClientGetDeviceResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get device request.
      - **device** *(dict) --*

        An object containing information about the requested device.
        - **arn** *(string) --*

          The device's ARN.
    """


_ClientGetInstanceProfileResponseinstanceProfileTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientGetInstanceProfileResponseinstanceProfileTypeDef(
    _ClientGetInstanceProfileResponseinstanceProfileTypeDef
):
    """
    - **instanceProfile** *(dict) --*

      An object containing information about your instance profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientGetInstanceProfileResponseTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseTypeDef",
    {"instanceProfile": ClientGetInstanceProfileResponseinstanceProfileTypeDef},
    total=False,
)


class ClientGetInstanceProfileResponseTypeDef(_ClientGetInstanceProfileResponseTypeDef):
    """
    - *(dict) --*

      - **instanceProfile** *(dict) --*

        An object containing information about your instance profile.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientGetJobResponsejobcountersTypeDef = TypedDict(
    "_ClientGetJobResponsejobcountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientGetJobResponsejobcountersTypeDef(_ClientGetJobResponsejobcountersTypeDef):
    pass


_ClientGetJobResponsejobdeviceMinutesTypeDef = TypedDict(
    "_ClientGetJobResponsejobdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientGetJobResponsejobdeviceMinutesTypeDef(_ClientGetJobResponsejobdeviceMinutesTypeDef):
    pass


_ClientGetJobResponsejobdevicecpuTypeDef = TypedDict(
    "_ClientGetJobResponsejobdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientGetJobResponsejobdevicecpuTypeDef(_ClientGetJobResponsejobdevicecpuTypeDef):
    pass


_ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef(
    _ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientGetJobResponsejobdeviceinstancesTypeDef = TypedDict(
    "_ClientGetJobResponsejobdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetJobResponsejobdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientGetJobResponsejobdeviceinstancesTypeDef(_ClientGetJobResponsejobdeviceinstancesTypeDef):
    pass


_ClientGetJobResponsejobdeviceresolutionTypeDef = TypedDict(
    "_ClientGetJobResponsejobdeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)


class ClientGetJobResponsejobdeviceresolutionTypeDef(
    _ClientGetJobResponsejobdeviceresolutionTypeDef
):
    pass


_ClientGetJobResponsejobdeviceTypeDef = TypedDict(
    "_ClientGetJobResponsejobdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetJobResponsejobdevicecpuTypeDef,
        "resolution": ClientGetJobResponsejobdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientGetJobResponsejobdeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientGetJobResponsejobdeviceTypeDef(_ClientGetJobResponsejobdeviceTypeDef):
    pass


_ClientGetJobResponsejobTypeDef = TypedDict(
    "_ClientGetJobResponsejobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetJobResponsejobcountersTypeDef,
        "message": str,
        "device": ClientGetJobResponsejobdeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": ClientGetJobResponsejobdeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)


class ClientGetJobResponsejobTypeDef(_ClientGetJobResponsejobTypeDef):
    """
    - **job** *(dict) --*

      An object containing information about the requested job.
      - **arn** *(string) --*

        The job's ARN.
    """


_ClientGetJobResponseTypeDef = TypedDict(
    "_ClientGetJobResponseTypeDef", {"job": ClientGetJobResponsejobTypeDef}, total=False
)


class ClientGetJobResponseTypeDef(_ClientGetJobResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get job request.
      - **job** *(dict) --*

        An object containing information about the requested job.
        - **arn** *(string) --*

          The job's ARN.
    """


_ClientGetNetworkProfileResponsenetworkProfileTypeDef = TypedDict(
    "_ClientGetNetworkProfileResponsenetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientGetNetworkProfileResponsenetworkProfileTypeDef(
    _ClientGetNetworkProfileResponsenetworkProfileTypeDef
):
    """
    - **networkProfile** *(dict) --*

      The network profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the network profile.
    """


_ClientGetNetworkProfileResponseTypeDef = TypedDict(
    "_ClientGetNetworkProfileResponseTypeDef",
    {"networkProfile": ClientGetNetworkProfileResponsenetworkProfileTypeDef},
    total=False,
)


class ClientGetNetworkProfileResponseTypeDef(_ClientGetNetworkProfileResponseTypeDef):
    """
    - *(dict) --*

      - **networkProfile** *(dict) --*

        The network profile.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the network profile.
    """


_ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef(
    _ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef
):
    pass


_ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef",
    {
        "cost": ClientGetOfferingStatusResponsecurrentofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef(
    _ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef
):
    pass


_ClientGetOfferingStatusResponsecurrentofferingTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsecurrentofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientGetOfferingStatusResponsecurrentofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientGetOfferingStatusResponsecurrentofferingTypeDef(
    _ClientGetOfferingStatusResponsecurrentofferingTypeDef
):
    pass


_ClientGetOfferingStatusResponsecurrentTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsecurrentTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientGetOfferingStatusResponsecurrentofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class ClientGetOfferingStatusResponsecurrentTypeDef(_ClientGetOfferingStatusResponsecurrentTypeDef):
    pass


_ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef(
    _ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef
):
    pass


_ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef",
    {
        "cost": ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef(
    _ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef
):
    pass


_ClientGetOfferingStatusResponsenextPeriodofferingTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsenextPeriodofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientGetOfferingStatusResponsenextPeriodofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientGetOfferingStatusResponsenextPeriodofferingTypeDef(
    _ClientGetOfferingStatusResponsenextPeriodofferingTypeDef
):
    pass


_ClientGetOfferingStatusResponsenextPeriodTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponsenextPeriodTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientGetOfferingStatusResponsenextPeriodofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class ClientGetOfferingStatusResponsenextPeriodTypeDef(
    _ClientGetOfferingStatusResponsenextPeriodTypeDef
):
    pass


_ClientGetOfferingStatusResponseTypeDef = TypedDict(
    "_ClientGetOfferingStatusResponseTypeDef",
    {
        "current": Dict[str, ClientGetOfferingStatusResponsecurrentTypeDef],
        "nextPeriod": Dict[str, ClientGetOfferingStatusResponsenextPeriodTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetOfferingStatusResponseTypeDef(_ClientGetOfferingStatusResponseTypeDef):
    """
    - *(dict) --*

      Returns the status result for a device offering.
      - **current** *(dict) --*

        When specified, gets the offering status for the current period.
        - *(string) --*

          - *(dict) --*

            The status of the offering.
            - **type** *(string) --*

              The type specified for the offering status.
    """


_ClientGetProjectResponseprojectTypeDef = TypedDict(
    "_ClientGetProjectResponseprojectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)


class ClientGetProjectResponseprojectTypeDef(_ClientGetProjectResponseprojectTypeDef):
    """
    - **project** *(dict) --*

      The project you wish to get information about.
      - **arn** *(string) --*

        The project's ARN.
    """


_ClientGetProjectResponseTypeDef = TypedDict(
    "_ClientGetProjectResponseTypeDef",
    {"project": ClientGetProjectResponseprojectTypeDef},
    total=False,
)


class ClientGetProjectResponseTypeDef(_ClientGetProjectResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get project request.
      - **project** *(dict) --*

        The project you wish to get information about.
        - **arn** *(string) --*

          The project's ARN.
    """


_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef(
    _ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef
):
    pass


_ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef(
    _ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef
):
    pass


_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef(
    _ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef(
    _ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
):
    pass


_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef(
    _ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef
):
    pass


_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientGetRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef,
        "resolution": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef(
    _ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef
):
    pass


_ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientGetRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)


class ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef(
    _ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef
):
    """
    - **remoteAccessSession** *(dict) --*

      A container that lists detailed information about the remote access session.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientGetRemoteAccessSessionResponseTypeDef = TypedDict(
    "_ClientGetRemoteAccessSessionResponseTypeDef",
    {"remoteAccessSession": ClientGetRemoteAccessSessionResponseremoteAccessSessionTypeDef},
    total=False,
)


class ClientGetRemoteAccessSessionResponseTypeDef(_ClientGetRemoteAccessSessionResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server that lists detailed information about the remote
      access session.
      - **remoteAccessSession** *(dict) --*

        A container that lists detailed information about the remote access session.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientGetRunResponseruncountersTypeDef = TypedDict(
    "_ClientGetRunResponseruncountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientGetRunResponseruncountersTypeDef(_ClientGetRunResponseruncountersTypeDef):
    pass


_ClientGetRunResponseruncustomerArtifactPathsTypeDef = TypedDict(
    "_ClientGetRunResponseruncustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)


class ClientGetRunResponseruncustomerArtifactPathsTypeDef(
    _ClientGetRunResponseruncustomerArtifactPathsTypeDef
):
    pass


_ClientGetRunResponserundeviceMinutesTypeDef = TypedDict(
    "_ClientGetRunResponserundeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientGetRunResponserundeviceMinutesTypeDef(_ClientGetRunResponserundeviceMinutesTypeDef):
    pass


_ClientGetRunResponserundeviceSelectionResultfiltersTypeDef = TypedDict(
    "_ClientGetRunResponserundeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientGetRunResponserundeviceSelectionResultfiltersTypeDef(
    _ClientGetRunResponserundeviceSelectionResultfiltersTypeDef
):
    pass


_ClientGetRunResponserundeviceSelectionResultTypeDef = TypedDict(
    "_ClientGetRunResponserundeviceSelectionResultTypeDef",
    {
        "filters": List[ClientGetRunResponserundeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)


class ClientGetRunResponserundeviceSelectionResultTypeDef(
    _ClientGetRunResponserundeviceSelectionResultTypeDef
):
    pass


_ClientGetRunResponserunlocationTypeDef = TypedDict(
    "_ClientGetRunResponserunlocationTypeDef", {"latitude": float, "longitude": float}, total=False
)


class ClientGetRunResponserunlocationTypeDef(_ClientGetRunResponserunlocationTypeDef):
    pass


_ClientGetRunResponserunnetworkProfileTypeDef = TypedDict(
    "_ClientGetRunResponserunnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientGetRunResponserunnetworkProfileTypeDef(_ClientGetRunResponserunnetworkProfileTypeDef):
    pass


_ClientGetRunResponserunradiosTypeDef = TypedDict(
    "_ClientGetRunResponserunradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)


class ClientGetRunResponserunradiosTypeDef(_ClientGetRunResponserunradiosTypeDef):
    pass


_ClientGetRunResponserunTypeDef = TypedDict(
    "_ClientGetRunResponserunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetRunResponseruncountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientGetRunResponserundeviceMinutesTypeDef,
        "networkProfile": ClientGetRunResponserunnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientGetRunResponserunradiosTypeDef,
        "location": ClientGetRunResponserunlocationTypeDef,
        "customerArtifactPaths": ClientGetRunResponseruncustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientGetRunResponserundeviceSelectionResultTypeDef,
    },
    total=False,
)


class ClientGetRunResponserunTypeDef(_ClientGetRunResponserunTypeDef):
    """
    - **run** *(dict) --*

      The run you wish to get results from.
      - **arn** *(string) --*

        The run's ARN.
    """


_ClientGetRunResponseTypeDef = TypedDict(
    "_ClientGetRunResponseTypeDef", {"run": ClientGetRunResponserunTypeDef}, total=False
)


class ClientGetRunResponseTypeDef(_ClientGetRunResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get run request.
      - **run** *(dict) --*

        The run you wish to get results from.
        - **arn** *(string) --*

          The run's ARN.
    """


_ClientGetSuiteResponsesuitecountersTypeDef = TypedDict(
    "_ClientGetSuiteResponsesuitecountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientGetSuiteResponsesuitecountersTypeDef(_ClientGetSuiteResponsesuitecountersTypeDef):
    pass


_ClientGetSuiteResponsesuitedeviceMinutesTypeDef = TypedDict(
    "_ClientGetSuiteResponsesuitedeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientGetSuiteResponsesuitedeviceMinutesTypeDef(
    _ClientGetSuiteResponsesuitedeviceMinutesTypeDef
):
    pass


_ClientGetSuiteResponsesuiteTypeDef = TypedDict(
    "_ClientGetSuiteResponsesuiteTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetSuiteResponsesuitecountersTypeDef,
        "message": str,
        "deviceMinutes": ClientGetSuiteResponsesuitedeviceMinutesTypeDef,
    },
    total=False,
)


class ClientGetSuiteResponsesuiteTypeDef(_ClientGetSuiteResponsesuiteTypeDef):
    """
    - **suite** *(dict) --*

      A collection of one or more tests.
      - **arn** *(string) --*

        The suite's ARN.
    """


_ClientGetSuiteResponseTypeDef = TypedDict(
    "_ClientGetSuiteResponseTypeDef", {"suite": ClientGetSuiteResponsesuiteTypeDef}, total=False
)


class ClientGetSuiteResponseTypeDef(_ClientGetSuiteResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get suite request.
      - **suite** *(dict) --*

        A collection of one or more tests.
        - **arn** *(string) --*

          The suite's ARN.
    """


_ClientGetTestResponsetestcountersTypeDef = TypedDict(
    "_ClientGetTestResponsetestcountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientGetTestResponsetestcountersTypeDef(_ClientGetTestResponsetestcountersTypeDef):
    pass


_ClientGetTestResponsetestdeviceMinutesTypeDef = TypedDict(
    "_ClientGetTestResponsetestdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientGetTestResponsetestdeviceMinutesTypeDef(_ClientGetTestResponsetestdeviceMinutesTypeDef):
    pass


_ClientGetTestResponsetestTypeDef = TypedDict(
    "_ClientGetTestResponsetestTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientGetTestResponsetestcountersTypeDef,
        "message": str,
        "deviceMinutes": ClientGetTestResponsetestdeviceMinutesTypeDef,
    },
    total=False,
)


class ClientGetTestResponsetestTypeDef(_ClientGetTestResponsetestTypeDef):
    """
    - **test** *(dict) --*

      A test condition that is evaluated.
      - **arn** *(string) --*

        The test's ARN.
    """


_ClientGetTestResponseTypeDef = TypedDict(
    "_ClientGetTestResponseTypeDef", {"test": ClientGetTestResponsetestTypeDef}, total=False
)


class ClientGetTestResponseTypeDef(_ClientGetTestResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get test request.
      - **test** *(dict) --*

        A test condition that is evaluated.
        - **arn** *(string) --*

          The test's ARN.
    """


_ClientGetUploadResponseuploadTypeDef = TypedDict(
    "_ClientGetUploadResponseuploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)


class ClientGetUploadResponseuploadTypeDef(_ClientGetUploadResponseuploadTypeDef):
    """
    - **upload** *(dict) --*

      An app or a set of one or more tests to upload or that have been uploaded.
      - **arn** *(string) --*

        The upload's ARN.
    """


_ClientGetUploadResponseTypeDef = TypedDict(
    "_ClientGetUploadResponseTypeDef", {"upload": ClientGetUploadResponseuploadTypeDef}, total=False
)


class ClientGetUploadResponseTypeDef(_ClientGetUploadResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a get upload request.
      - **upload** *(dict) --*

        An app or a set of one or more tests to upload or that have been uploaded.
        - **arn** *(string) --*

          The upload's ARN.
    """


_ClientGetVpceConfigurationResponsevpceConfigurationTypeDef = TypedDict(
    "_ClientGetVpceConfigurationResponsevpceConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)


class ClientGetVpceConfigurationResponsevpceConfigurationTypeDef(
    _ClientGetVpceConfigurationResponsevpceConfigurationTypeDef
):
    """
    - **vpceConfiguration** *(dict) --*

      An object containing information about your VPC endpoint configuration.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ClientGetVpceConfigurationResponseTypeDef = TypedDict(
    "_ClientGetVpceConfigurationResponseTypeDef",
    {"vpceConfiguration": ClientGetVpceConfigurationResponsevpceConfigurationTypeDef},
    total=False,
)


class ClientGetVpceConfigurationResponseTypeDef(_ClientGetVpceConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **vpceConfiguration** *(dict) --*

        An object containing information about your VPC endpoint configuration.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ClientInstallToRemoteAccessSessionResponseappUploadTypeDef = TypedDict(
    "_ClientInstallToRemoteAccessSessionResponseappUploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)


class ClientInstallToRemoteAccessSessionResponseappUploadTypeDef(
    _ClientInstallToRemoteAccessSessionResponseappUploadTypeDef
):
    """
    - **appUpload** *(dict) --*

      An app to upload or that has been uploaded.
      - **arn** *(string) --*

        The upload's ARN.
    """


_ClientInstallToRemoteAccessSessionResponseTypeDef = TypedDict(
    "_ClientInstallToRemoteAccessSessionResponseTypeDef",
    {"appUpload": ClientInstallToRemoteAccessSessionResponseappUploadTypeDef},
    total=False,
)


class ClientInstallToRemoteAccessSessionResponseTypeDef(
    _ClientInstallToRemoteAccessSessionResponseTypeDef
):
    """
    - *(dict) --*

      Represents the response from the server after AWS Device Farm makes a request to install to a
      remote access session.
      - **appUpload** *(dict) --*

        An app to upload or that has been uploaded.
        - **arn** *(string) --*

          The upload's ARN.
    """


_ClientListArtifactsResponseartifactsTypeDef = TypedDict(
    "_ClientListArtifactsResponseartifactsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "UNKNOWN",
            "SCREENSHOT",
            "DEVICE_LOG",
            "MESSAGE_LOG",
            "VIDEO_LOG",
            "RESULT_LOG",
            "SERVICE_LOG",
            "WEBKIT_LOG",
            "INSTRUMENTATION_OUTPUT",
            "EXERCISER_MONKEY_OUTPUT",
            "CALABASH_JSON_OUTPUT",
            "CALABASH_PRETTY_OUTPUT",
            "CALABASH_STANDARD_OUTPUT",
            "CALABASH_JAVA_XML_OUTPUT",
            "AUTOMATION_OUTPUT",
            "APPIUM_SERVER_OUTPUT",
            "APPIUM_JAVA_OUTPUT",
            "APPIUM_JAVA_XML_OUTPUT",
            "APPIUM_PYTHON_OUTPUT",
            "APPIUM_PYTHON_XML_OUTPUT",
            "EXPLORER_EVENT_LOG",
            "EXPLORER_SUMMARY_LOG",
            "APPLICATION_CRASH_REPORT",
            "XCTEST_LOG",
            "VIDEO",
            "CUSTOMER_ARTIFACT",
            "CUSTOMER_ARTIFACT_LOG",
            "TESTSPEC_OUTPUT",
        ],
        "extension": str,
        "url": str,
    },
    total=False,
)


class ClientListArtifactsResponseartifactsTypeDef(_ClientListArtifactsResponseartifactsTypeDef):
    """
    - *(dict) --*

      Represents the output of a test. Examples of artifacts include logs and screenshots.
      - **arn** *(string) --*

        The artifact's ARN.
    """


_ClientListArtifactsResponseTypeDef = TypedDict(
    "_ClientListArtifactsResponseTypeDef",
    {"artifacts": List[ClientListArtifactsResponseartifactsTypeDef], "nextToken": str},
    total=False,
)


class ClientListArtifactsResponseTypeDef(_ClientListArtifactsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list artifacts operation.
      - **artifacts** *(list) --*

        Information about the artifacts.
        - *(dict) --*

          Represents the output of a test. Examples of artifacts include logs and screenshots.
          - **arn** *(string) --*

            The artifact's ARN.
    """


_ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef = TypedDict(
    "_ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef(
    _ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef
):
    pass


_ClientListDeviceInstancesResponsedeviceInstancesTypeDef = TypedDict(
    "_ClientListDeviceInstancesResponsedeviceInstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListDeviceInstancesResponsedeviceInstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientListDeviceInstancesResponsedeviceInstancesTypeDef(
    _ClientListDeviceInstancesResponsedeviceInstancesTypeDef
):
    """
    - *(dict) --*

      Represents the device instance.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the device instance.
    """


_ClientListDeviceInstancesResponseTypeDef = TypedDict(
    "_ClientListDeviceInstancesResponseTypeDef",
    {
        "deviceInstances": List[ClientListDeviceInstancesResponsedeviceInstancesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDeviceInstancesResponseTypeDef(_ClientListDeviceInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **deviceInstances** *(list) --*

        An object containing information about your device instances.
        - *(dict) --*

          Represents the device instance.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the device instance.
    """


_ClientListDevicePoolsResponsedevicePoolsrulesTypeDef = TypedDict(
    "_ClientListDevicePoolsResponsedevicePoolsrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)


class ClientListDevicePoolsResponsedevicePoolsrulesTypeDef(
    _ClientListDevicePoolsResponsedevicePoolsrulesTypeDef
):
    pass


_ClientListDevicePoolsResponsedevicePoolsTypeDef = TypedDict(
    "_ClientListDevicePoolsResponsedevicePoolsTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientListDevicePoolsResponsedevicePoolsrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)


class ClientListDevicePoolsResponsedevicePoolsTypeDef(
    _ClientListDevicePoolsResponsedevicePoolsTypeDef
):
    """
    - *(dict) --*

      Represents a collection of device types.
      - **arn** *(string) --*

        The device pool's ARN.
    """


_ClientListDevicePoolsResponseTypeDef = TypedDict(
    "_ClientListDevicePoolsResponseTypeDef",
    {"devicePools": List[ClientListDevicePoolsResponsedevicePoolsTypeDef], "nextToken": str},
    total=False,
)


class ClientListDevicePoolsResponseTypeDef(_ClientListDevicePoolsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list device pools request.
      - **devicePools** *(list) --*

        Information about the device pools.
        - *(dict) --*

          Represents a collection of device types.
          - **arn** *(string) --*

            The device pool's ARN.
    """


_ClientListDevicesFiltersTypeDef = TypedDict(
    "_ClientListDevicesFiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientListDevicesFiltersTypeDef(_ClientListDevicesFiltersTypeDef):
    pass


_ClientListDevicesResponsedevicescpuTypeDef = TypedDict(
    "_ClientListDevicesResponsedevicescpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientListDevicesResponsedevicescpuTypeDef(_ClientListDevicesResponsedevicescpuTypeDef):
    pass


_ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef(
    _ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef
):
    pass


_ClientListDevicesResponsedevicesinstancesTypeDef = TypedDict(
    "_ClientListDevicesResponsedevicesinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListDevicesResponsedevicesinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientListDevicesResponsedevicesinstancesTypeDef(
    _ClientListDevicesResponsedevicesinstancesTypeDef
):
    pass


_ClientListDevicesResponsedevicesresolutionTypeDef = TypedDict(
    "_ClientListDevicesResponsedevicesresolutionTypeDef", {"width": int, "height": int}, total=False
)


class ClientListDevicesResponsedevicesresolutionTypeDef(
    _ClientListDevicesResponsedevicesresolutionTypeDef
):
    pass


_ClientListDevicesResponsedevicesTypeDef = TypedDict(
    "_ClientListDevicesResponsedevicesTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListDevicesResponsedevicescpuTypeDef,
        "resolution": ClientListDevicesResponsedevicesresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientListDevicesResponsedevicesinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientListDevicesResponsedevicesTypeDef(_ClientListDevicesResponsedevicesTypeDef):
    """
    - *(dict) --*

      Represents a device type that an app is tested against.
      - **arn** *(string) --*

        The device's ARN.
    """


_ClientListDevicesResponseTypeDef = TypedDict(
    "_ClientListDevicesResponseTypeDef",
    {"devices": List[ClientListDevicesResponsedevicesTypeDef], "nextToken": str},
    total=False,
)


class ClientListDevicesResponseTypeDef(_ClientListDevicesResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list devices operation.
      - **devices** *(list) --*

        Information about the devices.
        - *(dict) --*

          Represents a device type that an app is tested against.
          - **arn** *(string) --*

            The device's ARN.
    """


_ClientListInstanceProfilesResponseinstanceProfilesTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseinstanceProfilesTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientListInstanceProfilesResponseinstanceProfilesTypeDef(
    _ClientListInstanceProfilesResponseinstanceProfilesTypeDef
):
    """
    - *(dict) --*

      Represents the instance profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientListInstanceProfilesResponseTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseTypeDef",
    {
        "instanceProfiles": List[ClientListInstanceProfilesResponseinstanceProfilesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListInstanceProfilesResponseTypeDef(_ClientListInstanceProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **instanceProfiles** *(list) --*

        An object containing information about your instance profiles.
        - *(dict) --*

          Represents the instance profile.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientListJobsResponsejobscountersTypeDef = TypedDict(
    "_ClientListJobsResponsejobscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientListJobsResponsejobscountersTypeDef(_ClientListJobsResponsejobscountersTypeDef):
    pass


_ClientListJobsResponsejobsdeviceMinutesTypeDef = TypedDict(
    "_ClientListJobsResponsejobsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientListJobsResponsejobsdeviceMinutesTypeDef(
    _ClientListJobsResponsejobsdeviceMinutesTypeDef
):
    pass


_ClientListJobsResponsejobsdevicecpuTypeDef = TypedDict(
    "_ClientListJobsResponsejobsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientListJobsResponsejobsdevicecpuTypeDef(_ClientListJobsResponsejobsdevicecpuTypeDef):
    pass


_ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef(
    _ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientListJobsResponsejobsdeviceinstancesTypeDef = TypedDict(
    "_ClientListJobsResponsejobsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListJobsResponsejobsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientListJobsResponsejobsdeviceinstancesTypeDef(
    _ClientListJobsResponsejobsdeviceinstancesTypeDef
):
    pass


_ClientListJobsResponsejobsdeviceresolutionTypeDef = TypedDict(
    "_ClientListJobsResponsejobsdeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)


class ClientListJobsResponsejobsdeviceresolutionTypeDef(
    _ClientListJobsResponsejobsdeviceresolutionTypeDef
):
    pass


_ClientListJobsResponsejobsdeviceTypeDef = TypedDict(
    "_ClientListJobsResponsejobsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListJobsResponsejobsdevicecpuTypeDef,
        "resolution": ClientListJobsResponsejobsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientListJobsResponsejobsdeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientListJobsResponsejobsdeviceTypeDef(_ClientListJobsResponsejobsdeviceTypeDef):
    pass


_ClientListJobsResponsejobsTypeDef = TypedDict(
    "_ClientListJobsResponsejobsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListJobsResponsejobscountersTypeDef,
        "message": str,
        "device": ClientListJobsResponsejobsdeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": ClientListJobsResponsejobsdeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)


class ClientListJobsResponsejobsTypeDef(_ClientListJobsResponsejobsTypeDef):
    """
    - *(dict) --*

      Represents a device.
      - **arn** *(string) --*

        The job's ARN.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"jobs": List[ClientListJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list jobs request.
      - **jobs** *(list) --*

        Information about the jobs.
        - *(dict) --*

          Represents a device.
          - **arn** *(string) --*

            The job's ARN.
    """


_ClientListNetworkProfilesResponsenetworkProfilesTypeDef = TypedDict(
    "_ClientListNetworkProfilesResponsenetworkProfilesTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientListNetworkProfilesResponsenetworkProfilesTypeDef(
    _ClientListNetworkProfilesResponsenetworkProfilesTypeDef
):
    """
    - *(dict) --*

      An array of settings that describes characteristics of a network profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the network profile.
    """


_ClientListNetworkProfilesResponseTypeDef = TypedDict(
    "_ClientListNetworkProfilesResponseTypeDef",
    {
        "networkProfiles": List[ClientListNetworkProfilesResponsenetworkProfilesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListNetworkProfilesResponseTypeDef(_ClientListNetworkProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **networkProfiles** *(list) --*

        A list of the available network profiles.
        - *(dict) --*

          An array of settings that describes characteristics of a network profile.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the network profile.
    """


_ClientListOfferingPromotionsResponseofferingPromotionsTypeDef = TypedDict(
    "_ClientListOfferingPromotionsResponseofferingPromotionsTypeDef",
    {"id": str, "description": str},
    total=False,
)


class ClientListOfferingPromotionsResponseofferingPromotionsTypeDef(
    _ClientListOfferingPromotionsResponseofferingPromotionsTypeDef
):
    """
    - *(dict) --*

      Represents information about an offering promotion.
      - **id** *(string) --*

        The ID of the offering promotion.
    """


_ClientListOfferingPromotionsResponseTypeDef = TypedDict(
    "_ClientListOfferingPromotionsResponseTypeDef",
    {
        "offeringPromotions": List[ClientListOfferingPromotionsResponseofferingPromotionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListOfferingPromotionsResponseTypeDef(_ClientListOfferingPromotionsResponseTypeDef):
    """
    - *(dict) --*

      - **offeringPromotions** *(list) --*

        Information about the offering promotions.
        - *(dict) --*

          Represents information about an offering promotion.
          - **id** *(string) --*

            The ID of the offering promotion.
    """


_ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef = TypedDict(
    "_ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef(
    _ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef
):
    pass


_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef = TypedDict(
    "_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef(
    _ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef
):
    pass


_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef = TypedDict(
    "_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef",
    {
        "cost": ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef(
    _ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef
):
    pass


_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef = TypedDict(
    "_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef(
    _ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef
):
    pass


_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef = TypedDict(
    "_ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef(
    _ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef
):
    """
    - **offeringStatus** *(dict) --*

      The status of an offering transaction.
      - **type** *(string) --*

        The type specified for the offering status.
    """


_ClientListOfferingTransactionsResponseofferingTransactionsTypeDef = TypedDict(
    "_ClientListOfferingTransactionsResponseofferingTransactionsTypeDef",
    {
        "offeringStatus": ClientListOfferingTransactionsResponseofferingTransactionsofferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": ClientListOfferingTransactionsResponseofferingTransactionscostTypeDef,
    },
    total=False,
)


class ClientListOfferingTransactionsResponseofferingTransactionsTypeDef(
    _ClientListOfferingTransactionsResponseofferingTransactionsTypeDef
):
    """
    - *(dict) --*

      Represents the metadata of an offering transaction.
      - **offeringStatus** *(dict) --*

        The status of an offering transaction.
        - **type** *(string) --*

          The type specified for the offering status.
    """


_ClientListOfferingTransactionsResponseTypeDef = TypedDict(
    "_ClientListOfferingTransactionsResponseTypeDef",
    {
        "offeringTransactions": List[
            ClientListOfferingTransactionsResponseofferingTransactionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListOfferingTransactionsResponseTypeDef(_ClientListOfferingTransactionsResponseTypeDef):
    """
    - *(dict) --*

      Returns the transaction log of the specified offerings.
      - **offeringTransactions** *(list) --*

        The audit log of subscriptions you have purchased and modified through AWS Device Farm.
        - *(dict) --*

          Represents the metadata of an offering transaction.
          - **offeringStatus** *(dict) --*

            The status of an offering transaction.
            - **type** *(string) --*

              The type specified for the offering status.
    """


_ClientListOfferingsResponseofferingsrecurringChargescostTypeDef = TypedDict(
    "_ClientListOfferingsResponseofferingsrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientListOfferingsResponseofferingsrecurringChargescostTypeDef(
    _ClientListOfferingsResponseofferingsrecurringChargescostTypeDef
):
    pass


_ClientListOfferingsResponseofferingsrecurringChargesTypeDef = TypedDict(
    "_ClientListOfferingsResponseofferingsrecurringChargesTypeDef",
    {"cost": ClientListOfferingsResponseofferingsrecurringChargescostTypeDef, "frequency": str},
    total=False,
)


class ClientListOfferingsResponseofferingsrecurringChargesTypeDef(
    _ClientListOfferingsResponseofferingsrecurringChargesTypeDef
):
    pass


_ClientListOfferingsResponseofferingsTypeDef = TypedDict(
    "_ClientListOfferingsResponseofferingsTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[ClientListOfferingsResponseofferingsrecurringChargesTypeDef],
    },
    total=False,
)


class ClientListOfferingsResponseofferingsTypeDef(_ClientListOfferingsResponseofferingsTypeDef):
    """
    - *(dict) --*

      Represents the metadata of a device offering.
      - **id** *(string) --*

        The ID that corresponds to a device offering.
    """


_ClientListOfferingsResponseTypeDef = TypedDict(
    "_ClientListOfferingsResponseTypeDef",
    {"offerings": List[ClientListOfferingsResponseofferingsTypeDef], "nextToken": str},
    total=False,
)


class ClientListOfferingsResponseTypeDef(_ClientListOfferingsResponseTypeDef):
    """
    - *(dict) --*

      Represents the return values of the list of offerings.
      - **offerings** *(list) --*

        A value representing the list offering results.
        - *(dict) --*

          Represents the metadata of a device offering.
          - **id** *(string) --*

            The ID that corresponds to a device offering.
    """


_ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientListProjectsResponseprojectsTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)


class ClientListProjectsResponseprojectsTypeDef(_ClientListProjectsResponseprojectsTypeDef):
    """
    - *(dict) --*

      Represents an operating-system neutral workspace for running and managing tests.
      - **arn** *(string) --*

        The project's ARN.
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list projects request.
      - **projects** *(list) --*

        Information about the projects.
        - *(dict) --*

          Represents an operating-system neutral workspace for running and managing tests.
          - **arn** *(string) --*

            The project's ARN.
    """


_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef(
    _ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef
):
    pass


_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef(
    _ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef
):
    pass


_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef(
    _ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef(
    _ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef
):
    pass


_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef(
    _ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef
):
    pass


_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdevicecpuTypeDef,
        "resolution": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef(
    _ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef
):
    pass


_ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientListRemoteAccessSessionsResponseremoteAccessSessionsdeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)


class ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef(
    _ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef
):
    """
    - *(dict) --*

      Represents information about the remote access session.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientListRemoteAccessSessionsResponseTypeDef = TypedDict(
    "_ClientListRemoteAccessSessionsResponseTypeDef",
    {
        "remoteAccessSessions": List[
            ClientListRemoteAccessSessionsResponseremoteAccessSessionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListRemoteAccessSessionsResponseTypeDef(_ClientListRemoteAccessSessionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server after AWS Device Farm makes a request to return
      information about the remote access session.
      - **remoteAccessSessions** *(list) --*

        A container representing the metadata from the service about each remote access session you
        are requesting.
        - *(dict) --*

          Represents information about the remote access session.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientListRunsResponserunscountersTypeDef = TypedDict(
    "_ClientListRunsResponserunscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientListRunsResponserunscountersTypeDef(_ClientListRunsResponserunscountersTypeDef):
    pass


_ClientListRunsResponserunscustomerArtifactPathsTypeDef = TypedDict(
    "_ClientListRunsResponserunscustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)


class ClientListRunsResponserunscustomerArtifactPathsTypeDef(
    _ClientListRunsResponserunscustomerArtifactPathsTypeDef
):
    pass


_ClientListRunsResponserunsdeviceMinutesTypeDef = TypedDict(
    "_ClientListRunsResponserunsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientListRunsResponserunsdeviceMinutesTypeDef(
    _ClientListRunsResponserunsdeviceMinutesTypeDef
):
    pass


_ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef = TypedDict(
    "_ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef(
    _ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef
):
    pass


_ClientListRunsResponserunsdeviceSelectionResultTypeDef = TypedDict(
    "_ClientListRunsResponserunsdeviceSelectionResultTypeDef",
    {
        "filters": List[ClientListRunsResponserunsdeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)


class ClientListRunsResponserunsdeviceSelectionResultTypeDef(
    _ClientListRunsResponserunsdeviceSelectionResultTypeDef
):
    pass


_ClientListRunsResponserunslocationTypeDef = TypedDict(
    "_ClientListRunsResponserunslocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)


class ClientListRunsResponserunslocationTypeDef(_ClientListRunsResponserunslocationTypeDef):
    pass


_ClientListRunsResponserunsnetworkProfileTypeDef = TypedDict(
    "_ClientListRunsResponserunsnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientListRunsResponserunsnetworkProfileTypeDef(
    _ClientListRunsResponserunsnetworkProfileTypeDef
):
    pass


_ClientListRunsResponserunsradiosTypeDef = TypedDict(
    "_ClientListRunsResponserunsradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)


class ClientListRunsResponserunsradiosTypeDef(_ClientListRunsResponserunsradiosTypeDef):
    pass


_ClientListRunsResponserunsTypeDef = TypedDict(
    "_ClientListRunsResponserunsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListRunsResponserunscountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientListRunsResponserunsdeviceMinutesTypeDef,
        "networkProfile": ClientListRunsResponserunsnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientListRunsResponserunsradiosTypeDef,
        "location": ClientListRunsResponserunslocationTypeDef,
        "customerArtifactPaths": ClientListRunsResponserunscustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientListRunsResponserunsdeviceSelectionResultTypeDef,
    },
    total=False,
)


class ClientListRunsResponserunsTypeDef(_ClientListRunsResponserunsTypeDef):
    """
    - *(dict) --*

      Represents a test run on a set of devices with a given app package, test parameters, etc.
      - **arn** *(string) --*

        The run's ARN.
    """


_ClientListRunsResponseTypeDef = TypedDict(
    "_ClientListRunsResponseTypeDef",
    {"runs": List[ClientListRunsResponserunsTypeDef], "nextToken": str},
    total=False,
)


class ClientListRunsResponseTypeDef(_ClientListRunsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list runs request.
      - **runs** *(list) --*

        Information about the runs.
        - *(dict) --*

          Represents a test run on a set of devices with a given app package, test parameters, etc.
          - **arn** *(string) --*

            The run's ARN.
    """


_ClientListSamplesResponsesamplesTypeDef = TypedDict(
    "_ClientListSamplesResponsesamplesTypeDef",
    {
        "arn": str,
        "type": Literal[
            "CPU",
            "MEMORY",
            "THREADS",
            "RX_RATE",
            "TX_RATE",
            "RX",
            "TX",
            "NATIVE_FRAMES",
            "NATIVE_FPS",
            "NATIVE_MIN_DRAWTIME",
            "NATIVE_AVG_DRAWTIME",
            "NATIVE_MAX_DRAWTIME",
            "OPENGL_FRAMES",
            "OPENGL_FPS",
            "OPENGL_MIN_DRAWTIME",
            "OPENGL_AVG_DRAWTIME",
            "OPENGL_MAX_DRAWTIME",
        ],
        "url": str,
    },
    total=False,
)


class ClientListSamplesResponsesamplesTypeDef(_ClientListSamplesResponsesamplesTypeDef):
    """
    - *(dict) --*

      Represents a sample of performance data.
      - **arn** *(string) --*

        The sample's ARN.
    """


_ClientListSamplesResponseTypeDef = TypedDict(
    "_ClientListSamplesResponseTypeDef",
    {"samples": List[ClientListSamplesResponsesamplesTypeDef], "nextToken": str},
    total=False,
)


class ClientListSamplesResponseTypeDef(_ClientListSamplesResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list samples request.
      - **samples** *(list) --*

        Information about the samples.
        - *(dict) --*

          Represents a sample of performance data.
          - **arn** *(string) --*

            The sample's ARN.
    """


_ClientListSuitesResponsesuitescountersTypeDef = TypedDict(
    "_ClientListSuitesResponsesuitescountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientListSuitesResponsesuitescountersTypeDef(_ClientListSuitesResponsesuitescountersTypeDef):
    pass


_ClientListSuitesResponsesuitesdeviceMinutesTypeDef = TypedDict(
    "_ClientListSuitesResponsesuitesdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientListSuitesResponsesuitesdeviceMinutesTypeDef(
    _ClientListSuitesResponsesuitesdeviceMinutesTypeDef
):
    pass


_ClientListSuitesResponsesuitesTypeDef = TypedDict(
    "_ClientListSuitesResponsesuitesTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListSuitesResponsesuitescountersTypeDef,
        "message": str,
        "deviceMinutes": ClientListSuitesResponsesuitesdeviceMinutesTypeDef,
    },
    total=False,
)


class ClientListSuitesResponsesuitesTypeDef(_ClientListSuitesResponsesuitesTypeDef):
    """
    - *(dict) --*

      Represents a collection of one or more tests.
      - **arn** *(string) --*

        The suite's ARN.
    """


_ClientListSuitesResponseTypeDef = TypedDict(
    "_ClientListSuitesResponseTypeDef",
    {"suites": List[ClientListSuitesResponsesuitesTypeDef], "nextToken": str},
    total=False,
)


class ClientListSuitesResponseTypeDef(_ClientListSuitesResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list suites request.
      - **suites** *(list) --*

        Information about the suites.
        - *(dict) --*

          Represents a collection of one or more tests.
          - **arn** *(string) --*

            The suite's ARN.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize it. Each tag
      consists of a key and an optional value, both of which you define. Tag keys can have a maximum
      character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
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

        The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a
        maximum character length of 128 characters, and tag values can have a maximum length of 256
        characters.
        - *(dict) --*

          The metadata that you apply to a resource to help you categorize and organize it. Each tag
          consists of a key and an optional value, both of which you define. Tag keys can have a
          maximum character length of 128 characters, and tag values can have a maximum length of
          256 characters.
          - **Key** *(string) --*

            One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
            like a category for more specific tag values.
    """


_ClientListTestsResponsetestscountersTypeDef = TypedDict(
    "_ClientListTestsResponsetestscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientListTestsResponsetestscountersTypeDef(_ClientListTestsResponsetestscountersTypeDef):
    pass


_ClientListTestsResponsetestsdeviceMinutesTypeDef = TypedDict(
    "_ClientListTestsResponsetestsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientListTestsResponsetestsdeviceMinutesTypeDef(
    _ClientListTestsResponsetestsdeviceMinutesTypeDef
):
    pass


_ClientListTestsResponsetestsTypeDef = TypedDict(
    "_ClientListTestsResponsetestsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientListTestsResponsetestscountersTypeDef,
        "message": str,
        "deviceMinutes": ClientListTestsResponsetestsdeviceMinutesTypeDef,
    },
    total=False,
)


class ClientListTestsResponsetestsTypeDef(_ClientListTestsResponsetestsTypeDef):
    """
    - *(dict) --*

      Represents a condition that is evaluated.
      - **arn** *(string) --*

        The test's ARN.
    """


_ClientListTestsResponseTypeDef = TypedDict(
    "_ClientListTestsResponseTypeDef",
    {"tests": List[ClientListTestsResponsetestsTypeDef], "nextToken": str},
    total=False,
)


class ClientListTestsResponseTypeDef(_ClientListTestsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list tests request.
      - **tests** *(list) --*

        Information about the tests.
        - *(dict) --*

          Represents a condition that is evaluated.
          - **arn** *(string) --*

            The test's ARN.
    """


_ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientListUniqueProblemsResponseuniqueProblemsproblemsdevicecpuTypeDef,
        "resolution": ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef",
    {
        "run": ClientListUniqueProblemsResponseuniqueProblemsproblemsrunTypeDef,
        "job": ClientListUniqueProblemsResponseuniqueProblemsproblemsjobTypeDef,
        "suite": ClientListUniqueProblemsResponseuniqueProblemsproblemssuiteTypeDef,
        "test": ClientListUniqueProblemsResponseuniqueProblemsproblemstestTypeDef,
        "device": ClientListUniqueProblemsResponseuniqueProblemsproblemsdeviceTypeDef,
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
    },
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef
):
    pass


_ClientListUniqueProblemsResponseuniqueProblemsTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseuniqueProblemsTypeDef",
    {
        "message": str,
        "problems": List[ClientListUniqueProblemsResponseuniqueProblemsproblemsTypeDef],
    },
    total=False,
)


class ClientListUniqueProblemsResponseuniqueProblemsTypeDef(
    _ClientListUniqueProblemsResponseuniqueProblemsTypeDef
):
    pass


_ClientListUniqueProblemsResponseTypeDef = TypedDict(
    "_ClientListUniqueProblemsResponseTypeDef",
    {
        "uniqueProblems": Dict[str, List[ClientListUniqueProblemsResponseuniqueProblemsTypeDef]],
        "nextToken": str,
    },
    total=False,
)


class ClientListUniqueProblemsResponseTypeDef(_ClientListUniqueProblemsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list unique problems request.
      - **uniqueProblems** *(dict) --*

        Information about the unique problems.
        Allowed values include:
        * PENDING: A pending condition.
        * PASSED: A passing condition.
        * WARNED: A warning condition.
        * FAILED: A failed condition.
        * SKIPPED: A skipped condition.
        * ERRORED: An error condition.
        * STOPPED: A stopped condition.
        - *(string) --*

          - *(list) --*

            - *(dict) --*

              A collection of one or more problems, grouped by their result.
              - **message** *(string) --*

                A message about the unique problems' result.
    """


_ClientListUploadsResponseuploadsTypeDef = TypedDict(
    "_ClientListUploadsResponseuploadsTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)


class ClientListUploadsResponseuploadsTypeDef(_ClientListUploadsResponseuploadsTypeDef):
    """
    - *(dict) --*

      An app or a set of one or more tests to upload or that have been uploaded.
      - **arn** *(string) --*

        The upload's ARN.
    """


_ClientListUploadsResponseTypeDef = TypedDict(
    "_ClientListUploadsResponseTypeDef",
    {"uploads": List[ClientListUploadsResponseuploadsTypeDef], "nextToken": str},
    total=False,
)


class ClientListUploadsResponseTypeDef(_ClientListUploadsResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list uploads request.
      - **uploads** *(list) --*

        Information about the uploads.
        - *(dict) --*

          An app or a set of one or more tests to upload or that have been uploaded.
          - **arn** *(string) --*

            The upload's ARN.
    """


_ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef = TypedDict(
    "_ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)


class ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef(
    _ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef
):
    """
    - *(dict) --*

      Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ClientListVpceConfigurationsResponseTypeDef = TypedDict(
    "_ClientListVpceConfigurationsResponseTypeDef",
    {
        "vpceConfigurations": List[ClientListVpceConfigurationsResponsevpceConfigurationsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListVpceConfigurationsResponseTypeDef(_ClientListVpceConfigurationsResponseTypeDef):
    """
    - *(dict) --*

      - **vpceConfigurations** *(list) --*

        An array of ``VPCEConfiguration`` objects containing information about your VPC endpoint
        configuration.
        - *(dict) --*

          Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ClientPurchaseOfferingResponseofferingTransactioncostTypeDef = TypedDict(
    "_ClientPurchaseOfferingResponseofferingTransactioncostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientPurchaseOfferingResponseofferingTransactioncostTypeDef(
    _ClientPurchaseOfferingResponseofferingTransactioncostTypeDef
):
    pass


_ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef = TypedDict(
    "_ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef(
    _ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef
):
    pass


_ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef = TypedDict(
    "_ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    {
        "cost": ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef(
    _ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef
):
    pass


_ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef = TypedDict(
    "_ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef(
    _ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef
):
    pass


_ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef = TypedDict(
    "_ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientPurchaseOfferingResponseofferingTransactionofferingStatusofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef(
    _ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef
):
    """
    - **offeringStatus** *(dict) --*

      The status of an offering transaction.
      - **type** *(string) --*

        The type specified for the offering status.
    """


_ClientPurchaseOfferingResponseofferingTransactionTypeDef = TypedDict(
    "_ClientPurchaseOfferingResponseofferingTransactionTypeDef",
    {
        "offeringStatus": ClientPurchaseOfferingResponseofferingTransactionofferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": ClientPurchaseOfferingResponseofferingTransactioncostTypeDef,
    },
    total=False,
)


class ClientPurchaseOfferingResponseofferingTransactionTypeDef(
    _ClientPurchaseOfferingResponseofferingTransactionTypeDef
):
    """
    - **offeringTransaction** *(dict) --*

      Represents the offering transaction for the purchase result.
      - **offeringStatus** *(dict) --*

        The status of an offering transaction.
        - **type** *(string) --*

          The type specified for the offering status.
    """


_ClientPurchaseOfferingResponseTypeDef = TypedDict(
    "_ClientPurchaseOfferingResponseTypeDef",
    {"offeringTransaction": ClientPurchaseOfferingResponseofferingTransactionTypeDef},
    total=False,
)


class ClientPurchaseOfferingResponseTypeDef(_ClientPurchaseOfferingResponseTypeDef):
    """
    - *(dict) --*

      The result of the purchase offering (e.g., success or failure).
      - **offeringTransaction** *(dict) --*

        Represents the offering transaction for the purchase result.
        - **offeringStatus** *(dict) --*

          The status of an offering transaction.
          - **type** *(string) --*

            The type specified for the offering status.
    """


_ClientRenewOfferingResponseofferingTransactioncostTypeDef = TypedDict(
    "_ClientRenewOfferingResponseofferingTransactioncostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientRenewOfferingResponseofferingTransactioncostTypeDef(
    _ClientRenewOfferingResponseofferingTransactioncostTypeDef
):
    pass


_ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef = TypedDict(
    "_ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef(
    _ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef
):
    pass


_ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef = TypedDict(
    "_ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef",
    {
        "cost": ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef(
    _ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef
):
    pass


_ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef = TypedDict(
    "_ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ClientRenewOfferingResponseofferingTransactionofferingStatusofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef(
    _ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef
):
    pass


_ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef = TypedDict(
    "_ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ClientRenewOfferingResponseofferingTransactionofferingStatusofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef(
    _ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef
):
    """
    - **offeringStatus** *(dict) --*

      The status of an offering transaction.
      - **type** *(string) --*

        The type specified for the offering status.
    """


_ClientRenewOfferingResponseofferingTransactionTypeDef = TypedDict(
    "_ClientRenewOfferingResponseofferingTransactionTypeDef",
    {
        "offeringStatus": ClientRenewOfferingResponseofferingTransactionofferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": ClientRenewOfferingResponseofferingTransactioncostTypeDef,
    },
    total=False,
)


class ClientRenewOfferingResponseofferingTransactionTypeDef(
    _ClientRenewOfferingResponseofferingTransactionTypeDef
):
    """
    - **offeringTransaction** *(dict) --*

      Represents the status of the offering transaction for the renewal.
      - **offeringStatus** *(dict) --*

        The status of an offering transaction.
        - **type** *(string) --*

          The type specified for the offering status.
    """


_ClientRenewOfferingResponseTypeDef = TypedDict(
    "_ClientRenewOfferingResponseTypeDef",
    {"offeringTransaction": ClientRenewOfferingResponseofferingTransactionTypeDef},
    total=False,
)


class ClientRenewOfferingResponseTypeDef(_ClientRenewOfferingResponseTypeDef):
    """
    - *(dict) --*

      The result of a renewal offering.
      - **offeringTransaction** *(dict) --*

        Represents the status of the offering transaction for the renewal.
        - **offeringStatus** *(dict) --*

          The status of an offering transaction.
          - **type** *(string) --*

            The type specified for the offering status.
    """


_ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef = TypedDict(
    "_ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)


class ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef(
    _ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef
):
    pass


_ClientScheduleRunConfigurationlocationTypeDef = TypedDict(
    "_ClientScheduleRunConfigurationlocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)


class ClientScheduleRunConfigurationlocationTypeDef(_ClientScheduleRunConfigurationlocationTypeDef):
    pass


_ClientScheduleRunConfigurationradiosTypeDef = TypedDict(
    "_ClientScheduleRunConfigurationradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)


class ClientScheduleRunConfigurationradiosTypeDef(_ClientScheduleRunConfigurationradiosTypeDef):
    pass


_ClientScheduleRunConfigurationTypeDef = TypedDict(
    "_ClientScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": ClientScheduleRunConfigurationlocationTypeDef,
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": ClientScheduleRunConfigurationcustomerArtifactPathsTypeDef,
        "radios": ClientScheduleRunConfigurationradiosTypeDef,
        "auxiliaryApps": List[str],
        "billingMethod": Literal["METERED", "UNMETERED"],
    },
    total=False,
)


class ClientScheduleRunConfigurationTypeDef(_ClientScheduleRunConfigurationTypeDef):
    """
    Information about the settings for the run to be scheduled.
    - **extraDataPackageArn** *(string) --*

      The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will
      extract to external data for Android or the app's sandbox for iOS.
    """


_ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef = TypedDict(
    "_ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef(
    _ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef
):
    pass


_RequiredClientScheduleRunDeviceSelectionConfigurationTypeDef = TypedDict(
    "_RequiredClientScheduleRunDeviceSelectionConfigurationTypeDef",
    {"filters": List[ClientScheduleRunDeviceSelectionConfigurationfiltersTypeDef]},
)
_OptionalClientScheduleRunDeviceSelectionConfigurationTypeDef = TypedDict(
    "_OptionalClientScheduleRunDeviceSelectionConfigurationTypeDef",
    {"maxDevices": int},
    total=False,
)


class ClientScheduleRunDeviceSelectionConfigurationTypeDef(
    _RequiredClientScheduleRunDeviceSelectionConfigurationTypeDef,
    _OptionalClientScheduleRunDeviceSelectionConfigurationTypeDef,
):
    """
    The filter criteria used to dynamically select a set of devices for a test run, as well as the
    maximum number of devices to be included in the run.
    Either ** ``devicePoolArn`` ** or ** ``deviceSelectionConfiguration`` ** is required in a
    request.
    - **filters** *(list) --***[REQUIRED]**

      Used to dynamically select a set of devices for a test run. A filter is made up of an
      attribute, an operator, and one or more values.
      * **Attribute**   The aspect of a device such as platform or model used as the selection
      criteria in a device filter. Allowed values include:

        * ARN: The Amazon Resource Name (ARN) of the device. For example,
        "arn:aws:devicefarm:us-west-2::device:12345Example".
        * PLATFORM: The device platform. Valid values are "ANDROID" or "IOS".
        * OS_VERSION: The operating system version. For example, "10.3.2".
        * MODEL: The device model. For example, "iPad 5th Gen".
        * AVAILABILITY: The current availability of the device. Valid values are "AVAILABLE",
        "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
        * FORM_FACTOR: The device form factor. Valid values are "PHONE" or "TABLET".
        * MANUFACTURER: The device manufacturer. For example, "Apple".
        * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are
        "TRUE" or "FALSE".
        * REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are
        "TRUE" or "FALSE". *This filter will be ignored, as remote debugging is `no longer supported
        <https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html>`__ .*
        * INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
        * INSTANCE_LABELS: The label of the device instance.
        * FLEET_TYPE: The fleet type. Valid values are "PUBLIC" or "PRIVATE".
    """


_ClientScheduleRunExecutionConfigurationTypeDef = TypedDict(
    "_ClientScheduleRunExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": int,
        "accountsCleanup": bool,
        "appPackagesCleanup": bool,
        "videoCapture": bool,
        "skipAppResign": bool,
    },
    total=False,
)


class ClientScheduleRunExecutionConfigurationTypeDef(
    _ClientScheduleRunExecutionConfigurationTypeDef
):
    """
    Specifies configuration information about a test run, such as the execution timeout (in
    minutes).
    - **jobTimeoutMinutes** *(integer) --*

      The number of minutes a test run will execute before it times out.
    """


_ClientScheduleRunResponseruncountersTypeDef = TypedDict(
    "_ClientScheduleRunResponseruncountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientScheduleRunResponseruncountersTypeDef(_ClientScheduleRunResponseruncountersTypeDef):
    pass


_ClientScheduleRunResponseruncustomerArtifactPathsTypeDef = TypedDict(
    "_ClientScheduleRunResponseruncustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)


class ClientScheduleRunResponseruncustomerArtifactPathsTypeDef(
    _ClientScheduleRunResponseruncustomerArtifactPathsTypeDef
):
    pass


_ClientScheduleRunResponserundeviceMinutesTypeDef = TypedDict(
    "_ClientScheduleRunResponserundeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientScheduleRunResponserundeviceMinutesTypeDef(
    _ClientScheduleRunResponserundeviceMinutesTypeDef
):
    pass


_ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef = TypedDict(
    "_ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef(
    _ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef
):
    pass


_ClientScheduleRunResponserundeviceSelectionResultTypeDef = TypedDict(
    "_ClientScheduleRunResponserundeviceSelectionResultTypeDef",
    {
        "filters": List[ClientScheduleRunResponserundeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)


class ClientScheduleRunResponserundeviceSelectionResultTypeDef(
    _ClientScheduleRunResponserundeviceSelectionResultTypeDef
):
    pass


_ClientScheduleRunResponserunlocationTypeDef = TypedDict(
    "_ClientScheduleRunResponserunlocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)


class ClientScheduleRunResponserunlocationTypeDef(_ClientScheduleRunResponserunlocationTypeDef):
    pass


_ClientScheduleRunResponserunnetworkProfileTypeDef = TypedDict(
    "_ClientScheduleRunResponserunnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientScheduleRunResponserunnetworkProfileTypeDef(
    _ClientScheduleRunResponserunnetworkProfileTypeDef
):
    pass


_ClientScheduleRunResponserunradiosTypeDef = TypedDict(
    "_ClientScheduleRunResponserunradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)


class ClientScheduleRunResponserunradiosTypeDef(_ClientScheduleRunResponserunradiosTypeDef):
    pass


_ClientScheduleRunResponserunTypeDef = TypedDict(
    "_ClientScheduleRunResponserunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientScheduleRunResponseruncountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientScheduleRunResponserundeviceMinutesTypeDef,
        "networkProfile": ClientScheduleRunResponserunnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientScheduleRunResponserunradiosTypeDef,
        "location": ClientScheduleRunResponserunlocationTypeDef,
        "customerArtifactPaths": ClientScheduleRunResponseruncustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientScheduleRunResponserundeviceSelectionResultTypeDef,
    },
    total=False,
)


class ClientScheduleRunResponserunTypeDef(_ClientScheduleRunResponserunTypeDef):
    """
    - **run** *(dict) --*

      Information about the scheduled run.
      - **arn** *(string) --*

        The run's ARN.
    """


_ClientScheduleRunResponseTypeDef = TypedDict(
    "_ClientScheduleRunResponseTypeDef", {"run": ClientScheduleRunResponserunTypeDef}, total=False
)


class ClientScheduleRunResponseTypeDef(_ClientScheduleRunResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a schedule run request.
      - **run** *(dict) --*

        Information about the scheduled run.
        - **arn** *(string) --*

          The run's ARN.
    """


_RequiredClientScheduleRunTestTypeDef = TypedDict(
    "_RequiredClientScheduleRunTestTypeDef",
    {
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ]
    },
)
_OptionalClientScheduleRunTestTypeDef = TypedDict(
    "_OptionalClientScheduleRunTestTypeDef",
    {"testPackageArn": str, "testSpecArn": str, "filter": str, "parameters": Dict[str, str]},
    total=False,
)


class ClientScheduleRunTestTypeDef(
    _RequiredClientScheduleRunTestTypeDef, _OptionalClientScheduleRunTestTypeDef
):
    """
    Information about the test for the run to be scheduled.
    - **type** *(string) --***[REQUIRED]**

      The test's type.
      Must be one of the following values:
      * BUILTIN_FUZZ: The built-in fuzz type.
      * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app,
      interacting with it and capturing screenshots at the same time.
      * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
      * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
      * APPIUM_PYTHON: The Appium Python type.
      * APPIUM_NODE: The Appium Node.js type.
      * APPIUM_RUBY: The Appium Ruby type.
      * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
      * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
      * APPIUM_WEB_PYTHON: The Appium Python type for web apps.
      * APPIUM_WEB_NODE: The Appium Node.js type for web apps.
      * APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
      * CALABASH: The Calabash type.
      * INSTRUMENTATION: The Instrumentation type.
      * UIAUTOMATION: The uiautomation type.
      * UIAUTOMATOR: The uiautomator type.
      * XCTEST: The Xcode test type.
      * XCTEST_UI: The Xcode UI test type.
    """


_ClientStopJobResponsejobcountersTypeDef = TypedDict(
    "_ClientStopJobResponsejobcountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientStopJobResponsejobcountersTypeDef(_ClientStopJobResponsejobcountersTypeDef):
    pass


_ClientStopJobResponsejobdeviceMinutesTypeDef = TypedDict(
    "_ClientStopJobResponsejobdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientStopJobResponsejobdeviceMinutesTypeDef(_ClientStopJobResponsejobdeviceMinutesTypeDef):
    pass


_ClientStopJobResponsejobdevicecpuTypeDef = TypedDict(
    "_ClientStopJobResponsejobdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientStopJobResponsejobdevicecpuTypeDef(_ClientStopJobResponsejobdevicecpuTypeDef):
    pass


_ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef(
    _ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientStopJobResponsejobdeviceinstancesTypeDef = TypedDict(
    "_ClientStopJobResponsejobdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientStopJobResponsejobdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientStopJobResponsejobdeviceinstancesTypeDef(
    _ClientStopJobResponsejobdeviceinstancesTypeDef
):
    pass


_ClientStopJobResponsejobdeviceresolutionTypeDef = TypedDict(
    "_ClientStopJobResponsejobdeviceresolutionTypeDef", {"width": int, "height": int}, total=False
)


class ClientStopJobResponsejobdeviceresolutionTypeDef(
    _ClientStopJobResponsejobdeviceresolutionTypeDef
):
    pass


_ClientStopJobResponsejobdeviceTypeDef = TypedDict(
    "_ClientStopJobResponsejobdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientStopJobResponsejobdevicecpuTypeDef,
        "resolution": ClientStopJobResponsejobdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ClientStopJobResponsejobdeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientStopJobResponsejobdeviceTypeDef(_ClientStopJobResponsejobdeviceTypeDef):
    pass


_ClientStopJobResponsejobTypeDef = TypedDict(
    "_ClientStopJobResponsejobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientStopJobResponsejobcountersTypeDef,
        "message": str,
        "device": ClientStopJobResponsejobdeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": ClientStopJobResponsejobdeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)


class ClientStopJobResponsejobTypeDef(_ClientStopJobResponsejobTypeDef):
    """
    - **job** *(dict) --*

      The job that was stopped.
      - **arn** *(string) --*

        The job's ARN.
    """


_ClientStopJobResponseTypeDef = TypedDict(
    "_ClientStopJobResponseTypeDef", {"job": ClientStopJobResponsejobTypeDef}, total=False
)


class ClientStopJobResponseTypeDef(_ClientStopJobResponseTypeDef):
    """
    - *(dict) --*

      - **job** *(dict) --*

        The job that was stopped.
        - **arn** *(string) --*

          The job's ARN.
    """


_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef(
    _ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef
):
    pass


_ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef(
    _ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef
):
    pass


_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef(
    _ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef
):
    pass


_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef(
    _ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
):
    pass


_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef(
    _ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef
):
    pass


_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ClientStopRemoteAccessSessionResponseremoteAccessSessiondevicecpuTypeDef,
        "resolution": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef(
    _ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef
):
    pass


_ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientStopRemoteAccessSessionResponseremoteAccessSessiondeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)


class ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef(
    _ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef
):
    """
    - **remoteAccessSession** *(dict) --*

      A container representing the metadata from the service about the remote access session you are
      stopping.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientStopRemoteAccessSessionResponseTypeDef = TypedDict(
    "_ClientStopRemoteAccessSessionResponseTypeDef",
    {"remoteAccessSession": ClientStopRemoteAccessSessionResponseremoteAccessSessionTypeDef},
    total=False,
)


class ClientStopRemoteAccessSessionResponseTypeDef(_ClientStopRemoteAccessSessionResponseTypeDef):
    """
    - *(dict) --*

      Represents the response from the server that describes the remote access session when AWS
      Device Farm stops the session.
      - **remoteAccessSession** *(dict) --*

        A container representing the metadata from the service about the remote access session you
        are stopping.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the remote access session.
    """


_ClientStopRunResponseruncountersTypeDef = TypedDict(
    "_ClientStopRunResponseruncountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ClientStopRunResponseruncountersTypeDef(_ClientStopRunResponseruncountersTypeDef):
    pass


_ClientStopRunResponseruncustomerArtifactPathsTypeDef = TypedDict(
    "_ClientStopRunResponseruncustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)


class ClientStopRunResponseruncustomerArtifactPathsTypeDef(
    _ClientStopRunResponseruncustomerArtifactPathsTypeDef
):
    pass


_ClientStopRunResponserundeviceMinutesTypeDef = TypedDict(
    "_ClientStopRunResponserundeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ClientStopRunResponserundeviceMinutesTypeDef(_ClientStopRunResponserundeviceMinutesTypeDef):
    pass


_ClientStopRunResponserundeviceSelectionResultfiltersTypeDef = TypedDict(
    "_ClientStopRunResponserundeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientStopRunResponserundeviceSelectionResultfiltersTypeDef(
    _ClientStopRunResponserundeviceSelectionResultfiltersTypeDef
):
    pass


_ClientStopRunResponserundeviceSelectionResultTypeDef = TypedDict(
    "_ClientStopRunResponserundeviceSelectionResultTypeDef",
    {
        "filters": List[ClientStopRunResponserundeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)


class ClientStopRunResponserundeviceSelectionResultTypeDef(
    _ClientStopRunResponserundeviceSelectionResultTypeDef
):
    pass


_ClientStopRunResponserunlocationTypeDef = TypedDict(
    "_ClientStopRunResponserunlocationTypeDef", {"latitude": float, "longitude": float}, total=False
)


class ClientStopRunResponserunlocationTypeDef(_ClientStopRunResponserunlocationTypeDef):
    pass


_ClientStopRunResponserunnetworkProfileTypeDef = TypedDict(
    "_ClientStopRunResponserunnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientStopRunResponserunnetworkProfileTypeDef(_ClientStopRunResponserunnetworkProfileTypeDef):
    pass


_ClientStopRunResponserunradiosTypeDef = TypedDict(
    "_ClientStopRunResponserunradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)


class ClientStopRunResponserunradiosTypeDef(_ClientStopRunResponserunradiosTypeDef):
    pass


_ClientStopRunResponserunTypeDef = TypedDict(
    "_ClientStopRunResponserunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ClientStopRunResponseruncountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ClientStopRunResponserundeviceMinutesTypeDef,
        "networkProfile": ClientStopRunResponserunnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ClientStopRunResponserunradiosTypeDef,
        "location": ClientStopRunResponserunlocationTypeDef,
        "customerArtifactPaths": ClientStopRunResponseruncustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ClientStopRunResponserundeviceSelectionResultTypeDef,
    },
    total=False,
)


class ClientStopRunResponserunTypeDef(_ClientStopRunResponserunTypeDef):
    """
    - **run** *(dict) --*

      The run that was stopped.
      - **arn** *(string) --*

        The run's ARN.
    """


_ClientStopRunResponseTypeDef = TypedDict(
    "_ClientStopRunResponseTypeDef", {"run": ClientStopRunResponserunTypeDef}, total=False
)


class ClientStopRunResponseTypeDef(_ClientStopRunResponseTypeDef):
    """
    - *(dict) --*

      Represents the results of your stop run attempt.
      - **run** *(dict) --*

        The run that was stopped.
        - **arn** *(string) --*

          The run's ARN.
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

      The metadata that you apply to a resource to help you categorize and organize it. Each tag
      consists of a key and an optional value, both of which you define. Tag keys can have a maximum
      character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef = TypedDict(
    "_ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef(
    _ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef
):
    pass


_ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef = TypedDict(
    "_ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ClientUpdateDeviceInstanceResponsedeviceInstanceinstanceProfileTypeDef,
    },
    total=False,
)


class ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef(
    _ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef
):
    """
    - **deviceInstance** *(dict) --*

      An object containing information about your device instance.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the device instance.
    """


_ClientUpdateDeviceInstanceResponseTypeDef = TypedDict(
    "_ClientUpdateDeviceInstanceResponseTypeDef",
    {"deviceInstance": ClientUpdateDeviceInstanceResponsedeviceInstanceTypeDef},
    total=False,
)


class ClientUpdateDeviceInstanceResponseTypeDef(_ClientUpdateDeviceInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **deviceInstance** *(dict) --*

        An object containing information about your device instance.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the device instance.
    """


_ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef = TypedDict(
    "_ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)


class ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef(
    _ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef
):
    pass


_ClientUpdateDevicePoolResponsedevicePoolTypeDef = TypedDict(
    "_ClientUpdateDevicePoolResponsedevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ClientUpdateDevicePoolResponsedevicePoolrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)


class ClientUpdateDevicePoolResponsedevicePoolTypeDef(
    _ClientUpdateDevicePoolResponsedevicePoolTypeDef
):
    """
    - **devicePool** *(dict) --*

      The device pool you just updated.
      - **arn** *(string) --*

        The device pool's ARN.
    """


_ClientUpdateDevicePoolResponseTypeDef = TypedDict(
    "_ClientUpdateDevicePoolResponseTypeDef",
    {"devicePool": ClientUpdateDevicePoolResponsedevicePoolTypeDef},
    total=False,
)


class ClientUpdateDevicePoolResponseTypeDef(_ClientUpdateDevicePoolResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of an update device pool request.
      - **devicePool** *(dict) --*

        The device pool you just updated.
        - **arn** *(string) --*

          The device pool's ARN.
    """


_ClientUpdateDevicePoolRulesTypeDef = TypedDict(
    "_ClientUpdateDevicePoolRulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)


class ClientUpdateDevicePoolRulesTypeDef(_ClientUpdateDevicePoolRulesTypeDef):
    """
    - *(dict) --*

      Represents a condition for a device pool.
      - **attribute** *(string) --*

        The rule's stringified attribute. For example, specify the value as ``"\\"abc\\""`` .
        The supported operators for each attribute are provided in the following list.

          APPIUM_VERSION
    """


_ClientUpdateInstanceProfileResponseinstanceProfileTypeDef = TypedDict(
    "_ClientUpdateInstanceProfileResponseinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ClientUpdateInstanceProfileResponseinstanceProfileTypeDef(
    _ClientUpdateInstanceProfileResponseinstanceProfileTypeDef
):
    """
    - **instanceProfile** *(dict) --*

      An object containing information about your instance profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientUpdateInstanceProfileResponseTypeDef = TypedDict(
    "_ClientUpdateInstanceProfileResponseTypeDef",
    {"instanceProfile": ClientUpdateInstanceProfileResponseinstanceProfileTypeDef},
    total=False,
)


class ClientUpdateInstanceProfileResponseTypeDef(_ClientUpdateInstanceProfileResponseTypeDef):
    """
    - *(dict) --*

      - **instanceProfile** *(dict) --*

        An object containing information about your instance profile.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the instance profile.
    """


_ClientUpdateNetworkProfileResponsenetworkProfileTypeDef = TypedDict(
    "_ClientUpdateNetworkProfileResponsenetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ClientUpdateNetworkProfileResponsenetworkProfileTypeDef(
    _ClientUpdateNetworkProfileResponsenetworkProfileTypeDef
):
    """
    - **networkProfile** *(dict) --*

      A list of the available network profiles.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the network profile.
    """


_ClientUpdateNetworkProfileResponseTypeDef = TypedDict(
    "_ClientUpdateNetworkProfileResponseTypeDef",
    {"networkProfile": ClientUpdateNetworkProfileResponsenetworkProfileTypeDef},
    total=False,
)


class ClientUpdateNetworkProfileResponseTypeDef(_ClientUpdateNetworkProfileResponseTypeDef):
    """
    - *(dict) --*

      - **networkProfile** *(dict) --*

        A list of the available network profiles.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the network profile.
    """


_ClientUpdateProjectResponseprojectTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)


class ClientUpdateProjectResponseprojectTypeDef(_ClientUpdateProjectResponseprojectTypeDef):
    """
    - **project** *(dict) --*

      The project you wish to update.
      - **arn** *(string) --*

        The project's ARN.
    """


_ClientUpdateProjectResponseTypeDef = TypedDict(
    "_ClientUpdateProjectResponseTypeDef",
    {"project": ClientUpdateProjectResponseprojectTypeDef},
    total=False,
)


class ClientUpdateProjectResponseTypeDef(_ClientUpdateProjectResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of an update project request.
      - **project** *(dict) --*

        The project you wish to update.
        - **arn** *(string) --*

          The project's ARN.
    """


_ClientUpdateUploadResponseuploadTypeDef = TypedDict(
    "_ClientUpdateUploadResponseuploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)


class ClientUpdateUploadResponseuploadTypeDef(_ClientUpdateUploadResponseuploadTypeDef):
    """
    - **upload** *(dict) --*

      A test spec uploaded to Device Farm.
      - **arn** *(string) --*

        The upload's ARN.
    """


_ClientUpdateUploadResponseTypeDef = TypedDict(
    "_ClientUpdateUploadResponseTypeDef",
    {"upload": ClientUpdateUploadResponseuploadTypeDef},
    total=False,
)


class ClientUpdateUploadResponseTypeDef(_ClientUpdateUploadResponseTypeDef):
    """
    - *(dict) --*

      - **upload** *(dict) --*

        A test spec uploaded to Device Farm.
        - **arn** *(string) --*

          The upload's ARN.
    """


_ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef = TypedDict(
    "_ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)


class ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef(
    _ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef
):
    """
    - **vpceConfiguration** *(dict) --*

      An object containing information about your VPC endpoint configuration.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ClientUpdateVpceConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateVpceConfigurationResponseTypeDef",
    {"vpceConfiguration": ClientUpdateVpceConfigurationResponsevpceConfigurationTypeDef},
    total=False,
)


class ClientUpdateVpceConfigurationResponseTypeDef(_ClientUpdateVpceConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **vpceConfiguration** *(dict) --*

        An object containing information about your VPC endpoint configuration.
        - **arn** *(string) --*

          The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_GetOfferingStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_GetOfferingStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetOfferingStatusPaginatePaginationConfigTypeDef(
    _GetOfferingStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetOfferingStatusPaginateResponsecurrentofferingrecurringChargescostTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsecurrentofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class GetOfferingStatusPaginateResponsecurrentofferingrecurringChargescostTypeDef(
    _GetOfferingStatusPaginateResponsecurrentofferingrecurringChargescostTypeDef
):
    pass


_GetOfferingStatusPaginateResponsecurrentofferingrecurringChargesTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsecurrentofferingrecurringChargesTypeDef",
    {
        "cost": GetOfferingStatusPaginateResponsecurrentofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class GetOfferingStatusPaginateResponsecurrentofferingrecurringChargesTypeDef(
    _GetOfferingStatusPaginateResponsecurrentofferingrecurringChargesTypeDef
):
    pass


_GetOfferingStatusPaginateResponsecurrentofferingTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsecurrentofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            GetOfferingStatusPaginateResponsecurrentofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class GetOfferingStatusPaginateResponsecurrentofferingTypeDef(
    _GetOfferingStatusPaginateResponsecurrentofferingTypeDef
):
    pass


_GetOfferingStatusPaginateResponsecurrentTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsecurrentTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": GetOfferingStatusPaginateResponsecurrentofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class GetOfferingStatusPaginateResponsecurrentTypeDef(
    _GetOfferingStatusPaginateResponsecurrentTypeDef
):
    pass


_GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargescostTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargescostTypeDef(
    _GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargescostTypeDef
):
    pass


_GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargesTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargesTypeDef",
    {
        "cost": GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargesTypeDef(
    _GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargesTypeDef
):
    pass


_GetOfferingStatusPaginateResponsenextPeriodofferingTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsenextPeriodofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            GetOfferingStatusPaginateResponsenextPeriodofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class GetOfferingStatusPaginateResponsenextPeriodofferingTypeDef(
    _GetOfferingStatusPaginateResponsenextPeriodofferingTypeDef
):
    pass


_GetOfferingStatusPaginateResponsenextPeriodTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponsenextPeriodTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": GetOfferingStatusPaginateResponsenextPeriodofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class GetOfferingStatusPaginateResponsenextPeriodTypeDef(
    _GetOfferingStatusPaginateResponsenextPeriodTypeDef
):
    pass


_GetOfferingStatusPaginateResponseTypeDef = TypedDict(
    "_GetOfferingStatusPaginateResponseTypeDef",
    {
        "current": Dict[str, GetOfferingStatusPaginateResponsecurrentTypeDef],
        "nextPeriod": Dict[str, GetOfferingStatusPaginateResponsenextPeriodTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetOfferingStatusPaginateResponseTypeDef(_GetOfferingStatusPaginateResponseTypeDef):
    """
    - *(dict) --*

      Returns the status result for a device offering.
      - **current** *(dict) --*

        When specified, gets the offering status for the current period.
        - *(string) --*

          - *(dict) --*

            The status of the offering.
            - **type** *(string) --*

              The type specified for the offering status.
    """


_ListArtifactsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListArtifactsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListArtifactsPaginatePaginationConfigTypeDef(_ListArtifactsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListArtifactsPaginateResponseartifactsTypeDef = TypedDict(
    "_ListArtifactsPaginateResponseartifactsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "UNKNOWN",
            "SCREENSHOT",
            "DEVICE_LOG",
            "MESSAGE_LOG",
            "VIDEO_LOG",
            "RESULT_LOG",
            "SERVICE_LOG",
            "WEBKIT_LOG",
            "INSTRUMENTATION_OUTPUT",
            "EXERCISER_MONKEY_OUTPUT",
            "CALABASH_JSON_OUTPUT",
            "CALABASH_PRETTY_OUTPUT",
            "CALABASH_STANDARD_OUTPUT",
            "CALABASH_JAVA_XML_OUTPUT",
            "AUTOMATION_OUTPUT",
            "APPIUM_SERVER_OUTPUT",
            "APPIUM_JAVA_OUTPUT",
            "APPIUM_JAVA_XML_OUTPUT",
            "APPIUM_PYTHON_OUTPUT",
            "APPIUM_PYTHON_XML_OUTPUT",
            "EXPLORER_EVENT_LOG",
            "EXPLORER_SUMMARY_LOG",
            "APPLICATION_CRASH_REPORT",
            "XCTEST_LOG",
            "VIDEO",
            "CUSTOMER_ARTIFACT",
            "CUSTOMER_ARTIFACT_LOG",
            "TESTSPEC_OUTPUT",
        ],
        "extension": str,
        "url": str,
    },
    total=False,
)


class ListArtifactsPaginateResponseartifactsTypeDef(_ListArtifactsPaginateResponseartifactsTypeDef):
    """
    - *(dict) --*

      Represents the output of a test. Examples of artifacts include logs and screenshots.
      - **arn** *(string) --*

        The artifact's ARN.
    """


_ListArtifactsPaginateResponseTypeDef = TypedDict(
    "_ListArtifactsPaginateResponseTypeDef",
    {"artifacts": List[ListArtifactsPaginateResponseartifactsTypeDef], "NextToken": str},
    total=False,
)


class ListArtifactsPaginateResponseTypeDef(_ListArtifactsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list artifacts operation.
      - **artifacts** *(list) --*

        Information about the artifacts.
        - *(dict) --*

          Represents the output of a test. Examples of artifacts include logs and screenshots.
          - **arn** *(string) --*

            The artifact's ARN.
    """


_ListDeviceInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceInstancesPaginatePaginationConfigTypeDef(
    _ListDeviceInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeviceInstancesPaginateResponsedeviceInstancesinstanceProfileTypeDef = TypedDict(
    "_ListDeviceInstancesPaginateResponsedeviceInstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ListDeviceInstancesPaginateResponsedeviceInstancesinstanceProfileTypeDef(
    _ListDeviceInstancesPaginateResponsedeviceInstancesinstanceProfileTypeDef
):
    pass


_ListDeviceInstancesPaginateResponsedeviceInstancesTypeDef = TypedDict(
    "_ListDeviceInstancesPaginateResponsedeviceInstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ListDeviceInstancesPaginateResponsedeviceInstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ListDeviceInstancesPaginateResponsedeviceInstancesTypeDef(
    _ListDeviceInstancesPaginateResponsedeviceInstancesTypeDef
):
    """
    - *(dict) --*

      Represents the device instance.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the device instance.
    """


_ListDeviceInstancesPaginateResponseTypeDef = TypedDict(
    "_ListDeviceInstancesPaginateResponseTypeDef",
    {
        "deviceInstances": List[ListDeviceInstancesPaginateResponsedeviceInstancesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDeviceInstancesPaginateResponseTypeDef(_ListDeviceInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **deviceInstances** *(list) --*

        An object containing information about your device instances.
        - *(dict) --*

          Represents the device instance.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the device instance.
    """


_ListDevicePoolsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDevicePoolsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDevicePoolsPaginatePaginationConfigTypeDef(
    _ListDevicePoolsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDevicePoolsPaginateResponsedevicePoolsrulesTypeDef = TypedDict(
    "_ListDevicePoolsPaginateResponsedevicePoolsrulesTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)


class ListDevicePoolsPaginateResponsedevicePoolsrulesTypeDef(
    _ListDevicePoolsPaginateResponsedevicePoolsrulesTypeDef
):
    pass


_ListDevicePoolsPaginateResponsedevicePoolsTypeDef = TypedDict(
    "_ListDevicePoolsPaginateResponsedevicePoolsTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List[ListDevicePoolsPaginateResponsedevicePoolsrulesTypeDef],
        "maxDevices": int,
    },
    total=False,
)


class ListDevicePoolsPaginateResponsedevicePoolsTypeDef(
    _ListDevicePoolsPaginateResponsedevicePoolsTypeDef
):
    """
    - *(dict) --*

      Represents a collection of device types.
      - **arn** *(string) --*

        The device pool's ARN.
    """


_ListDevicePoolsPaginateResponseTypeDef = TypedDict(
    "_ListDevicePoolsPaginateResponseTypeDef",
    {"devicePools": List[ListDevicePoolsPaginateResponsedevicePoolsTypeDef], "NextToken": str},
    total=False,
)


class ListDevicePoolsPaginateResponseTypeDef(_ListDevicePoolsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list device pools request.
      - **devicePools** *(list) --*

        Information about the device pools.
        - *(dict) --*

          Represents a collection of device types.
          - **arn** *(string) --*

            The device pool's ARN.
    """


_ListDevicesPaginateFiltersTypeDef = TypedDict(
    "_ListDevicesPaginateFiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ListDevicesPaginateFiltersTypeDef(_ListDevicesPaginateFiltersTypeDef):
    pass


_ListDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDevicesPaginatePaginationConfigTypeDef(_ListDevicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDevicesPaginateResponsedevicescpuTypeDef = TypedDict(
    "_ListDevicesPaginateResponsedevicescpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ListDevicesPaginateResponsedevicescpuTypeDef(_ListDevicesPaginateResponsedevicescpuTypeDef):
    pass


_ListDevicesPaginateResponsedevicesinstancesinstanceProfileTypeDef = TypedDict(
    "_ListDevicesPaginateResponsedevicesinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ListDevicesPaginateResponsedevicesinstancesinstanceProfileTypeDef(
    _ListDevicesPaginateResponsedevicesinstancesinstanceProfileTypeDef
):
    pass


_ListDevicesPaginateResponsedevicesinstancesTypeDef = TypedDict(
    "_ListDevicesPaginateResponsedevicesinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ListDevicesPaginateResponsedevicesinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ListDevicesPaginateResponsedevicesinstancesTypeDef(
    _ListDevicesPaginateResponsedevicesinstancesTypeDef
):
    pass


_ListDevicesPaginateResponsedevicesresolutionTypeDef = TypedDict(
    "_ListDevicesPaginateResponsedevicesresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ListDevicesPaginateResponsedevicesresolutionTypeDef(
    _ListDevicesPaginateResponsedevicesresolutionTypeDef
):
    pass


_ListDevicesPaginateResponsedevicesTypeDef = TypedDict(
    "_ListDevicesPaginateResponsedevicesTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ListDevicesPaginateResponsedevicescpuTypeDef,
        "resolution": ListDevicesPaginateResponsedevicesresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ListDevicesPaginateResponsedevicesinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ListDevicesPaginateResponsedevicesTypeDef(_ListDevicesPaginateResponsedevicesTypeDef):
    """
    - *(dict) --*

      Represents a device type that an app is tested against.
      - **arn** *(string) --*

        The device's ARN.
    """


_ListDevicesPaginateResponseTypeDef = TypedDict(
    "_ListDevicesPaginateResponseTypeDef",
    {"devices": List[ListDevicesPaginateResponsedevicesTypeDef], "NextToken": str},
    total=False,
)


class ListDevicesPaginateResponseTypeDef(_ListDevicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list devices operation.
      - **devices** *(list) --*

        Information about the devices.
        - *(dict) --*

          Represents a device type that an app is tested against.
          - **arn** *(string) --*

            The device's ARN.
    """


_ListInstanceProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInstanceProfilesPaginatePaginationConfigTypeDef(
    _ListInstanceProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInstanceProfilesPaginateResponseinstanceProfilesTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseinstanceProfilesTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseinstanceProfilesTypeDef(
    _ListInstanceProfilesPaginateResponseinstanceProfilesTypeDef
):
    """
    - *(dict) --*

      Represents the instance profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the instance profile.
    """


_ListInstanceProfilesPaginateResponseTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseTypeDef",
    {
        "instanceProfiles": List[ListInstanceProfilesPaginateResponseinstanceProfilesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseTypeDef(_ListInstanceProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **instanceProfiles** *(list) --*

        An object containing information about your instance profiles.
        - *(dict) --*

          Represents the instance profile.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the instance profile.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsPaginateResponsejobscountersTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ListJobsPaginateResponsejobscountersTypeDef(_ListJobsPaginateResponsejobscountersTypeDef):
    pass


_ListJobsPaginateResponsejobsdeviceMinutesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ListJobsPaginateResponsejobsdeviceMinutesTypeDef(
    _ListJobsPaginateResponsejobsdeviceMinutesTypeDef
):
    pass


_ListJobsPaginateResponsejobsdevicecpuTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ListJobsPaginateResponsejobsdevicecpuTypeDef(_ListJobsPaginateResponsejobsdevicecpuTypeDef):
    pass


_ListJobsPaginateResponsejobsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ListJobsPaginateResponsejobsdeviceinstancesinstanceProfileTypeDef(
    _ListJobsPaginateResponsejobsdeviceinstancesinstanceProfileTypeDef
):
    pass


_ListJobsPaginateResponsejobsdeviceinstancesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ListJobsPaginateResponsejobsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ListJobsPaginateResponsejobsdeviceinstancesTypeDef(
    _ListJobsPaginateResponsejobsdeviceinstancesTypeDef
):
    pass


_ListJobsPaginateResponsejobsdeviceresolutionTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ListJobsPaginateResponsejobsdeviceresolutionTypeDef(
    _ListJobsPaginateResponsejobsdeviceresolutionTypeDef
):
    pass


_ListJobsPaginateResponsejobsdeviceTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ListJobsPaginateResponsejobsdevicecpuTypeDef,
        "resolution": ListJobsPaginateResponsejobsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[ListJobsPaginateResponsejobsdeviceinstancesTypeDef],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ListJobsPaginateResponsejobsdeviceTypeDef(_ListJobsPaginateResponsejobsdeviceTypeDef):
    pass


_ListJobsPaginateResponsejobsTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ListJobsPaginateResponsejobscountersTypeDef,
        "message": str,
        "device": ListJobsPaginateResponsejobsdeviceTypeDef,
        "instanceArn": str,
        "deviceMinutes": ListJobsPaginateResponsejobsdeviceMinutesTypeDef,
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)


class ListJobsPaginateResponsejobsTypeDef(_ListJobsPaginateResponsejobsTypeDef):
    """
    - *(dict) --*

      Represents a device.
      - **arn** *(string) --*

        The job's ARN.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"jobs": List[ListJobsPaginateResponsejobsTypeDef], "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list jobs request.
      - **jobs** *(list) --*

        Information about the jobs.
        - *(dict) --*

          Represents a device.
          - **arn** *(string) --*

            The job's ARN.
    """


_ListNetworkProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNetworkProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListNetworkProfilesPaginatePaginationConfigTypeDef(
    _ListNetworkProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNetworkProfilesPaginateResponsenetworkProfilesTypeDef = TypedDict(
    "_ListNetworkProfilesPaginateResponsenetworkProfilesTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ListNetworkProfilesPaginateResponsenetworkProfilesTypeDef(
    _ListNetworkProfilesPaginateResponsenetworkProfilesTypeDef
):
    """
    - *(dict) --*

      An array of settings that describes characteristics of a network profile.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the network profile.
    """


_ListNetworkProfilesPaginateResponseTypeDef = TypedDict(
    "_ListNetworkProfilesPaginateResponseTypeDef",
    {
        "networkProfiles": List[ListNetworkProfilesPaginateResponsenetworkProfilesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListNetworkProfilesPaginateResponseTypeDef(_ListNetworkProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **networkProfiles** *(list) --*

        A list of the available network profiles.
        - *(dict) --*

          An array of settings that describes characteristics of a network profile.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the network profile.
    """


_ListOfferingPromotionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOfferingPromotionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListOfferingPromotionsPaginatePaginationConfigTypeDef(
    _ListOfferingPromotionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOfferingPromotionsPaginateResponseofferingPromotionsTypeDef = TypedDict(
    "_ListOfferingPromotionsPaginateResponseofferingPromotionsTypeDef",
    {"id": str, "description": str},
    total=False,
)


class ListOfferingPromotionsPaginateResponseofferingPromotionsTypeDef(
    _ListOfferingPromotionsPaginateResponseofferingPromotionsTypeDef
):
    """
    - *(dict) --*

      Represents information about an offering promotion.
      - **id** *(string) --*

        The ID of the offering promotion.
    """


_ListOfferingPromotionsPaginateResponseTypeDef = TypedDict(
    "_ListOfferingPromotionsPaginateResponseTypeDef",
    {
        "offeringPromotions": List[ListOfferingPromotionsPaginateResponseofferingPromotionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListOfferingPromotionsPaginateResponseTypeDef(_ListOfferingPromotionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **offeringPromotions** *(list) --*

        Information about the offering promotions.
        - *(dict) --*

          Represents information about an offering promotion.
          - **id** *(string) --*

            The ID of the offering promotion.
    """


_ListOfferingTransactionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListOfferingTransactionsPaginatePaginationConfigTypeDef(
    _ListOfferingTransactionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOfferingTransactionsPaginateResponseofferingTransactionscostTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginateResponseofferingTransactionscostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ListOfferingTransactionsPaginateResponseofferingTransactionscostTypeDef(
    _ListOfferingTransactionsPaginateResponseofferingTransactionscostTypeDef
):
    pass


_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef(
    _ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef
):
    pass


_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef",
    {
        "cost": ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargescostTypeDef,
        "frequency": str,
    },
    total=False,
)


class ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef(
    _ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef
):
    pass


_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[
            ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingrecurringChargesTypeDef
        ],
    },
    total=False,
)


class ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingTypeDef(
    _ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingTypeDef
):
    pass


_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusofferingTypeDef,
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)


class ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusTypeDef(
    _ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusTypeDef
):
    """
    - **offeringStatus** *(dict) --*

      The status of an offering transaction.
      - **type** *(string) --*

        The type specified for the offering status.
    """


_ListOfferingTransactionsPaginateResponseofferingTransactionsTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginateResponseofferingTransactionsTypeDef",
    {
        "offeringStatus": ListOfferingTransactionsPaginateResponseofferingTransactionsofferingStatusTypeDef,
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": ListOfferingTransactionsPaginateResponseofferingTransactionscostTypeDef,
    },
    total=False,
)


class ListOfferingTransactionsPaginateResponseofferingTransactionsTypeDef(
    _ListOfferingTransactionsPaginateResponseofferingTransactionsTypeDef
):
    """
    - *(dict) --*

      Represents the metadata of an offering transaction.
      - **offeringStatus** *(dict) --*

        The status of an offering transaction.
        - **type** *(string) --*

          The type specified for the offering status.
    """


_ListOfferingTransactionsPaginateResponseTypeDef = TypedDict(
    "_ListOfferingTransactionsPaginateResponseTypeDef",
    {
        "offeringTransactions": List[
            ListOfferingTransactionsPaginateResponseofferingTransactionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListOfferingTransactionsPaginateResponseTypeDef(
    _ListOfferingTransactionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Returns the transaction log of the specified offerings.
      - **offeringTransactions** *(list) --*

        The audit log of subscriptions you have purchased and modified through AWS Device Farm.
        - *(dict) --*

          Represents the metadata of an offering transaction.
          - **offeringStatus** *(dict) --*

            The status of an offering transaction.
            - **type** *(string) --*

              The type specified for the offering status.
    """


_ListOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListOfferingsPaginatePaginationConfigTypeDef(_ListOfferingsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOfferingsPaginateResponseofferingsrecurringChargescostTypeDef = TypedDict(
    "_ListOfferingsPaginateResponseofferingsrecurringChargescostTypeDef",
    {"amount": float, "currencyCode": str},
    total=False,
)


class ListOfferingsPaginateResponseofferingsrecurringChargescostTypeDef(
    _ListOfferingsPaginateResponseofferingsrecurringChargescostTypeDef
):
    pass


_ListOfferingsPaginateResponseofferingsrecurringChargesTypeDef = TypedDict(
    "_ListOfferingsPaginateResponseofferingsrecurringChargesTypeDef",
    {"cost": ListOfferingsPaginateResponseofferingsrecurringChargescostTypeDef, "frequency": str},
    total=False,
)


class ListOfferingsPaginateResponseofferingsrecurringChargesTypeDef(
    _ListOfferingsPaginateResponseofferingsrecurringChargesTypeDef
):
    pass


_ListOfferingsPaginateResponseofferingsTypeDef = TypedDict(
    "_ListOfferingsPaginateResponseofferingsTypeDef",
    {
        "id": str,
        "description": str,
        "type": str,
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List[ListOfferingsPaginateResponseofferingsrecurringChargesTypeDef],
    },
    total=False,
)


class ListOfferingsPaginateResponseofferingsTypeDef(_ListOfferingsPaginateResponseofferingsTypeDef):
    """
    - *(dict) --*

      Represents the metadata of a device offering.
      - **id** *(string) --*

        The ID that corresponds to a device offering.
    """


_ListOfferingsPaginateResponseTypeDef = TypedDict(
    "_ListOfferingsPaginateResponseTypeDef",
    {"offerings": List[ListOfferingsPaginateResponseofferingsTypeDef], "NextToken": str},
    total=False,
)


class ListOfferingsPaginateResponseTypeDef(_ListOfferingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the return values of the list of offerings.
      - **offerings** *(list) --*

        A value representing the list offering results.
        - *(dict) --*

          Represents the metadata of a device offering.
          - **id** *(string) --*

            The ID that corresponds to a device offering.
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListProjectsPaginatePaginationConfigTypeDef(_ListProjectsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "_ListProjectsPaginateResponseprojectsTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)


class ListProjectsPaginateResponseprojectsTypeDef(_ListProjectsPaginateResponseprojectsTypeDef):
    """
    - *(dict) --*

      Represents an operating-system neutral workspace for running and managing tests.
      - **arn** *(string) --*

        The project's ARN.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list projects request.
      - **projects** *(list) --*

        Information about the projects.
        - *(dict) --*

          Represents an operating-system neutral workspace for running and managing tests.
          - **arn** *(string) --*

            The project's ARN.
    """


_ListRemoteAccessSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListRemoteAccessSessionsPaginatePaginationConfigTypeDef(
    _ListRemoteAccessSessionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceMinutesTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceMinutesTypeDef(
    _ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceMinutesTypeDef
):
    pass


_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdevicecpuTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdevicecpuTypeDef(
    _ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdevicecpuTypeDef
):
    pass


_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef(
    _ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef
):
    pass


_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesTypeDef(
    _ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesTypeDef
):
    pass


_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceresolutionTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceresolutionTypeDef(
    _ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceresolutionTypeDef
):
    pass


_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdevicecpuTypeDef,
        "resolution": ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceTypeDef(
    _ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceTypeDef
):
    pass


_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceTypeDef,
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsdeviceMinutesTypeDef,
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsTypeDef(
    _ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsTypeDef
):
    """
    - *(dict) --*

      Represents information about the remote access session.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the remote access session.
    """


_ListRemoteAccessSessionsPaginateResponseTypeDef = TypedDict(
    "_ListRemoteAccessSessionsPaginateResponseTypeDef",
    {
        "remoteAccessSessions": List[
            ListRemoteAccessSessionsPaginateResponseremoteAccessSessionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListRemoteAccessSessionsPaginateResponseTypeDef(
    _ListRemoteAccessSessionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the response from the server after AWS Device Farm makes a request to return
      information about the remote access session.
      - **remoteAccessSessions** *(list) --*

        A container representing the metadata from the service about each remote access session you
        are requesting.
        - *(dict) --*

          Represents information about the remote access session.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the remote access session.
    """


_ListRunsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRunsPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)


class ListRunsPaginatePaginationConfigTypeDef(_ListRunsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRunsPaginateResponserunscountersTypeDef = TypedDict(
    "_ListRunsPaginateResponserunscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ListRunsPaginateResponserunscountersTypeDef(_ListRunsPaginateResponserunscountersTypeDef):
    pass


_ListRunsPaginateResponserunscustomerArtifactPathsTypeDef = TypedDict(
    "_ListRunsPaginateResponserunscustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)


class ListRunsPaginateResponserunscustomerArtifactPathsTypeDef(
    _ListRunsPaginateResponserunscustomerArtifactPathsTypeDef
):
    pass


_ListRunsPaginateResponserunsdeviceMinutesTypeDef = TypedDict(
    "_ListRunsPaginateResponserunsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ListRunsPaginateResponserunsdeviceMinutesTypeDef(
    _ListRunsPaginateResponserunsdeviceMinutesTypeDef
):
    pass


_ListRunsPaginateResponserunsdeviceSelectionResultfiltersTypeDef = TypedDict(
    "_ListRunsPaginateResponserunsdeviceSelectionResultfiltersTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)


class ListRunsPaginateResponserunsdeviceSelectionResultfiltersTypeDef(
    _ListRunsPaginateResponserunsdeviceSelectionResultfiltersTypeDef
):
    pass


_ListRunsPaginateResponserunsdeviceSelectionResultTypeDef = TypedDict(
    "_ListRunsPaginateResponserunsdeviceSelectionResultTypeDef",
    {
        "filters": List[ListRunsPaginateResponserunsdeviceSelectionResultfiltersTypeDef],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)


class ListRunsPaginateResponserunsdeviceSelectionResultTypeDef(
    _ListRunsPaginateResponserunsdeviceSelectionResultTypeDef
):
    pass


_ListRunsPaginateResponserunslocationTypeDef = TypedDict(
    "_ListRunsPaginateResponserunslocationTypeDef",
    {"latitude": float, "longitude": float},
    total=False,
)


class ListRunsPaginateResponserunslocationTypeDef(_ListRunsPaginateResponserunslocationTypeDef):
    pass


_ListRunsPaginateResponserunsnetworkProfileTypeDef = TypedDict(
    "_ListRunsPaginateResponserunsnetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class ListRunsPaginateResponserunsnetworkProfileTypeDef(
    _ListRunsPaginateResponserunsnetworkProfileTypeDef
):
    pass


_ListRunsPaginateResponserunsradiosTypeDef = TypedDict(
    "_ListRunsPaginateResponserunsradiosTypeDef",
    {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool},
    total=False,
)


class ListRunsPaginateResponserunsradiosTypeDef(_ListRunsPaginateResponserunsradiosTypeDef):
    pass


_ListRunsPaginateResponserunsTypeDef = TypedDict(
    "_ListRunsPaginateResponserunsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ListRunsPaginateResponserunscountersTypeDef,
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": ListRunsPaginateResponserunsdeviceMinutesTypeDef,
        "networkProfile": ListRunsPaginateResponserunsnetworkProfileTypeDef,
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": ListRunsPaginateResponserunsradiosTypeDef,
        "location": ListRunsPaginateResponserunslocationTypeDef,
        "customerArtifactPaths": ListRunsPaginateResponserunscustomerArtifactPathsTypeDef,
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": ListRunsPaginateResponserunsdeviceSelectionResultTypeDef,
    },
    total=False,
)


class ListRunsPaginateResponserunsTypeDef(_ListRunsPaginateResponserunsTypeDef):
    """
    - *(dict) --*

      Represents a test run on a set of devices with a given app package, test parameters, etc.
      - **arn** *(string) --*

        The run's ARN.
    """


_ListRunsPaginateResponseTypeDef = TypedDict(
    "_ListRunsPaginateResponseTypeDef",
    {"runs": List[ListRunsPaginateResponserunsTypeDef], "NextToken": str},
    total=False,
)


class ListRunsPaginateResponseTypeDef(_ListRunsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list runs request.
      - **runs** *(list) --*

        Information about the runs.
        - *(dict) --*

          Represents a test run on a set of devices with a given app package, test parameters, etc.
          - **arn** *(string) --*

            The run's ARN.
    """


_ListSamplesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSamplesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSamplesPaginatePaginationConfigTypeDef(_ListSamplesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSamplesPaginateResponsesamplesTypeDef = TypedDict(
    "_ListSamplesPaginateResponsesamplesTypeDef",
    {
        "arn": str,
        "type": Literal[
            "CPU",
            "MEMORY",
            "THREADS",
            "RX_RATE",
            "TX_RATE",
            "RX",
            "TX",
            "NATIVE_FRAMES",
            "NATIVE_FPS",
            "NATIVE_MIN_DRAWTIME",
            "NATIVE_AVG_DRAWTIME",
            "NATIVE_MAX_DRAWTIME",
            "OPENGL_FRAMES",
            "OPENGL_FPS",
            "OPENGL_MIN_DRAWTIME",
            "OPENGL_AVG_DRAWTIME",
            "OPENGL_MAX_DRAWTIME",
        ],
        "url": str,
    },
    total=False,
)


class ListSamplesPaginateResponsesamplesTypeDef(_ListSamplesPaginateResponsesamplesTypeDef):
    """
    - *(dict) --*

      Represents a sample of performance data.
      - **arn** *(string) --*

        The sample's ARN.
    """


_ListSamplesPaginateResponseTypeDef = TypedDict(
    "_ListSamplesPaginateResponseTypeDef",
    {"samples": List[ListSamplesPaginateResponsesamplesTypeDef], "NextToken": str},
    total=False,
)


class ListSamplesPaginateResponseTypeDef(_ListSamplesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list samples request.
      - **samples** *(list) --*

        Information about the samples.
        - *(dict) --*

          Represents a sample of performance data.
          - **arn** *(string) --*

            The sample's ARN.
    """


_ListSuitesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSuitesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListSuitesPaginatePaginationConfigTypeDef(_ListSuitesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSuitesPaginateResponsesuitescountersTypeDef = TypedDict(
    "_ListSuitesPaginateResponsesuitescountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ListSuitesPaginateResponsesuitescountersTypeDef(
    _ListSuitesPaginateResponsesuitescountersTypeDef
):
    pass


_ListSuitesPaginateResponsesuitesdeviceMinutesTypeDef = TypedDict(
    "_ListSuitesPaginateResponsesuitesdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ListSuitesPaginateResponsesuitesdeviceMinutesTypeDef(
    _ListSuitesPaginateResponsesuitesdeviceMinutesTypeDef
):
    pass


_ListSuitesPaginateResponsesuitesTypeDef = TypedDict(
    "_ListSuitesPaginateResponsesuitesTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ListSuitesPaginateResponsesuitescountersTypeDef,
        "message": str,
        "deviceMinutes": ListSuitesPaginateResponsesuitesdeviceMinutesTypeDef,
    },
    total=False,
)


class ListSuitesPaginateResponsesuitesTypeDef(_ListSuitesPaginateResponsesuitesTypeDef):
    """
    - *(dict) --*

      Represents a collection of one or more tests.
      - **arn** *(string) --*

        The suite's ARN.
    """


_ListSuitesPaginateResponseTypeDef = TypedDict(
    "_ListSuitesPaginateResponseTypeDef",
    {"suites": List[ListSuitesPaginateResponsesuitesTypeDef], "NextToken": str},
    total=False,
)


class ListSuitesPaginateResponseTypeDef(_ListSuitesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list suites request.
      - **suites** *(list) --*

        Information about the suites.
        - *(dict) --*

          Represents a collection of one or more tests.
          - **arn** *(string) --*

            The suite's ARN.
    """


_ListTestsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTestsPaginatePaginationConfigTypeDef(_ListTestsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTestsPaginateResponsetestscountersTypeDef = TypedDict(
    "_ListTestsPaginateResponsetestscountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)


class ListTestsPaginateResponsetestscountersTypeDef(_ListTestsPaginateResponsetestscountersTypeDef):
    pass


_ListTestsPaginateResponsetestsdeviceMinutesTypeDef = TypedDict(
    "_ListTestsPaginateResponsetestsdeviceMinutesTypeDef",
    {"total": float, "metered": float, "unmetered": float},
    total=False,
)


class ListTestsPaginateResponsetestsdeviceMinutesTypeDef(
    _ListTestsPaginateResponsetestsdeviceMinutesTypeDef
):
    pass


_ListTestsPaginateResponsetestsTypeDef = TypedDict(
    "_ListTestsPaginateResponsetestsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": ListTestsPaginateResponsetestscountersTypeDef,
        "message": str,
        "deviceMinutes": ListTestsPaginateResponsetestsdeviceMinutesTypeDef,
    },
    total=False,
)


class ListTestsPaginateResponsetestsTypeDef(_ListTestsPaginateResponsetestsTypeDef):
    """
    - *(dict) --*

      Represents a condition that is evaluated.
      - **arn** *(string) --*

        The test's ARN.
    """


_ListTestsPaginateResponseTypeDef = TypedDict(
    "_ListTestsPaginateResponseTypeDef",
    {"tests": List[ListTestsPaginateResponsetestsTypeDef], "NextToken": str},
    total=False,
)


class ListTestsPaginateResponseTypeDef(_ListTestsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list tests request.
      - **tests** *(list) --*

        Information about the tests.
        - *(dict) --*

          Represents a condition that is evaluated.
          - **arn** *(string) --*

            The test's ARN.
    """


_ListUniqueProblemsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUniqueProblemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListUniqueProblemsPaginatePaginationConfigTypeDef(
    _ListUniqueProblemsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdevicecpuTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdevicecpuTypeDef",
    {"frequency": str, "architecture": str, "clock": float},
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdevicecpuTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdevicecpuTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesinstanceProfileTypeDef,
    },
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceresolutionTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceresolutionTypeDef",
    {"width": int, "height": int},
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceresolutionTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceresolutionTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdevicecpuTypeDef,
        "resolution": ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceresolutionTypeDef,
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List[
            ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceinstancesTypeDef
        ],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsjobTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsjobTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsjobTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsjobTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsrunTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsrunTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsrunTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsrunTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemssuiteTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemssuiteTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemssuiteTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemssuiteTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemstestTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemstestTypeDef",
    {"arn": str, "name": str},
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemstestTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemstestTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsproblemsTypeDef",
    {
        "run": ListUniqueProblemsPaginateResponseuniqueProblemsproblemsrunTypeDef,
        "job": ListUniqueProblemsPaginateResponseuniqueProblemsproblemsjobTypeDef,
        "suite": ListUniqueProblemsPaginateResponseuniqueProblemsproblemssuiteTypeDef,
        "test": ListUniqueProblemsPaginateResponseuniqueProblemsproblemstestTypeDef,
        "device": ListUniqueProblemsPaginateResponseuniqueProblemsproblemsdeviceTypeDef,
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
    },
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsproblemsTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsproblemsTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseuniqueProblemsTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseuniqueProblemsTypeDef",
    {
        "message": str,
        "problems": List[ListUniqueProblemsPaginateResponseuniqueProblemsproblemsTypeDef],
    },
    total=False,
)


class ListUniqueProblemsPaginateResponseuniqueProblemsTypeDef(
    _ListUniqueProblemsPaginateResponseuniqueProblemsTypeDef
):
    pass


_ListUniqueProblemsPaginateResponseTypeDef = TypedDict(
    "_ListUniqueProblemsPaginateResponseTypeDef",
    {
        "uniqueProblems": Dict[str, List[ListUniqueProblemsPaginateResponseuniqueProblemsTypeDef]],
        "NextToken": str,
    },
    total=False,
)


class ListUniqueProblemsPaginateResponseTypeDef(_ListUniqueProblemsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list unique problems request.
      - **uniqueProblems** *(dict) --*

        Information about the unique problems.
        Allowed values include:
        * PENDING: A pending condition.
        * PASSED: A passing condition.
        * WARNED: A warning condition.
        * FAILED: A failed condition.
        * SKIPPED: A skipped condition.
        * ERRORED: An error condition.
        * STOPPED: A stopped condition.
        - *(string) --*

          - *(list) --*

            - *(dict) --*

              A collection of one or more problems, grouped by their result.
              - **message** *(string) --*

                A message about the unique problems' result.
    """


_ListUploadsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUploadsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListUploadsPaginatePaginationConfigTypeDef(_ListUploadsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUploadsPaginateResponseuploadsTypeDef = TypedDict(
    "_ListUploadsPaginateResponseuploadsTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)


class ListUploadsPaginateResponseuploadsTypeDef(_ListUploadsPaginateResponseuploadsTypeDef):
    """
    - *(dict) --*

      An app or a set of one or more tests to upload or that have been uploaded.
      - **arn** *(string) --*

        The upload's ARN.
    """


_ListUploadsPaginateResponseTypeDef = TypedDict(
    "_ListUploadsPaginateResponseTypeDef",
    {"uploads": List[ListUploadsPaginateResponseuploadsTypeDef], "NextToken": str},
    total=False,
)


class ListUploadsPaginateResponseTypeDef(_ListUploadsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the result of a list uploads request.
      - **uploads** *(list) --*

        Information about the uploads.
        - *(dict) --*

          An app or a set of one or more tests to upload or that have been uploaded.
          - **arn** *(string) --*

            The upload's ARN.
    """


_ListVPCEConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVPCEConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVPCEConfigurationsPaginatePaginationConfigTypeDef(
    _ListVPCEConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVPCEConfigurationsPaginateResponsevpceConfigurationsTypeDef = TypedDict(
    "_ListVPCEConfigurationsPaginateResponsevpceConfigurationsTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)


class ListVPCEConfigurationsPaginateResponsevpceConfigurationsTypeDef(
    _ListVPCEConfigurationsPaginateResponsevpceConfigurationsTypeDef
):
    """
    - *(dict) --*

      Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """


_ListVPCEConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListVPCEConfigurationsPaginateResponseTypeDef",
    {
        "vpceConfigurations": List[ListVPCEConfigurationsPaginateResponsevpceConfigurationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListVPCEConfigurationsPaginateResponseTypeDef(_ListVPCEConfigurationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **vpceConfigurations** *(list) --*

        An array of ``VPCEConfiguration`` objects containing information about your VPC endpoint
        configuration.
        - *(dict) --*

          Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    """
