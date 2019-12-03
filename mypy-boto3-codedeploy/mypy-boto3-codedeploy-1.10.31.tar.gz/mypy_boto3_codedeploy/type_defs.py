"Main interface for codedeploy service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsToOnPremisesInstancesTagsTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsTypeDef",
    "ClientBatchGetApplicationRevisionsResponseTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsstringTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsTypeDef",
    "ClientBatchGetApplicationsResponseapplicationsInfoTypeDef",
    "ClientBatchGetApplicationsResponseTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef",
    "ClientBatchGetDeploymentGroupsResponseTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef",
    "ClientBatchGetDeploymentInstancesResponseTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef",
    "ClientBatchGetDeploymentTargetsResponseTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef",
    "ClientBatchGetDeploymentsResponseTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientCreateDeploymentAutoRollbackConfigurationTypeDef",
    "ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef",
    "ClientCreateDeploymentConfigResponseTypeDef",
    "ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef",
    "ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef",
    "ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef",
    "ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef",
    "ClientCreateDeploymentGroupAlarmConfigurationTypeDef",
    "ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    "ClientCreateDeploymentGroupDeploymentStyleTypeDef",
    "ClientCreateDeploymentGroupEc2TagFiltersTypeDef",
    "ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    "ClientCreateDeploymentGroupEc2TagSetTypeDef",
    "ClientCreateDeploymentGroupEcsServicesTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfoTypeDef",
    "ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    "ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientCreateDeploymentGroupOnPremisesTagSetTypeDef",
    "ClientCreateDeploymentGroupResponseTypeDef",
    "ClientCreateDeploymentGroupTagsTypeDef",
    "ClientCreateDeploymentGroupTriggerConfigurationsTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDeploymentRevisionappSpecContentTypeDef",
    "ClientCreateDeploymentRevisiongitHubLocationTypeDef",
    "ClientCreateDeploymentRevisions3LocationTypeDef",
    "ClientCreateDeploymentRevisionstringTypeDef",
    "ClientCreateDeploymentRevisionTypeDef",
    "ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientCreateDeploymentTargetInstancesec2TagSetTypeDef",
    "ClientCreateDeploymentTargetInstancestagFiltersTypeDef",
    "ClientCreateDeploymentTargetInstancesTypeDef",
    "ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    "ClientDeleteDeploymentGroupResponseTypeDef",
    "ClientDeleteGitHubAccountTokenResponseTypeDef",
    "ClientGetApplicationResponseapplicationTypeDef",
    "ClientGetApplicationResponseTypeDef",
    "ClientGetApplicationRevisionResponserevisionInfoTypeDef",
    "ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef",
    "ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef",
    "ClientGetApplicationRevisionResponserevisions3LocationTypeDef",
    "ClientGetApplicationRevisionResponserevisionstringTypeDef",
    "ClientGetApplicationRevisionResponserevisionTypeDef",
    "ClientGetApplicationRevisionResponseTypeDef",
    "ClientGetApplicationRevisionRevisionappSpecContentTypeDef",
    "ClientGetApplicationRevisionRevisiongitHubLocationTypeDef",
    "ClientGetApplicationRevisionRevisions3LocationTypeDef",
    "ClientGetApplicationRevisionRevisionstringTypeDef",
    "ClientGetApplicationRevisionRevisionTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef",
    "ClientGetDeploymentConfigResponseTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef",
    "ClientGetDeploymentGroupResponseTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef",
    "ClientGetDeploymentInstanceResponseTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef",
    "ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionTypeDef",
    "ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetTypeDef",
    "ClientGetDeploymentTargetResponseTypeDef",
    "ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef",
    "ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef",
    "ClientGetOnPremisesInstanceResponseTypeDef",
    "ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef",
    "ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef",
    "ClientListApplicationRevisionsResponserevisionss3LocationTypeDef",
    "ClientListApplicationRevisionsResponserevisionsstringTypeDef",
    "ClientListApplicationRevisionsResponserevisionsTypeDef",
    "ClientListApplicationRevisionsResponseTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListDeploymentConfigsResponseTypeDef",
    "ClientListDeploymentGroupsResponseTypeDef",
    "ClientListDeploymentInstancesResponseTypeDef",
    "ClientListDeploymentTargetsResponseTypeDef",
    "ClientListDeploymentsCreateTimeRangeTypeDef",
    "ClientListDeploymentsResponseTypeDef",
    "ClientListGitHubAccountTokenNamesResponseTypeDef",
    "ClientListOnPremisesInstancesResponseTypeDef",
    "ClientListOnPremisesInstancesTagFiltersTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLifecycleEventHookExecutionStatusResponseTypeDef",
    "ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef",
    "ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef",
    "ClientRegisterApplicationRevisionRevisions3LocationTypeDef",
    "ClientRegisterApplicationRevisionRevisionstringTypeDef",
    "ClientRegisterApplicationRevisionRevisionTypeDef",
    "ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef",
    "ClientStopDeploymentResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef",
    "ClientUpdateDeploymentGroupAlarmConfigurationTypeDef",
    "ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    "ClientUpdateDeploymentGroupDeploymentStyleTypeDef",
    "ClientUpdateDeploymentGroupEc2TagFiltersTypeDef",
    "ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    "ClientUpdateDeploymentGroupEc2TagSetTypeDef",
    "ClientUpdateDeploymentGroupEcsServicesTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef",
    "ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    "ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef",
    "ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    "ClientUpdateDeploymentGroupResponseTypeDef",
    "ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef",
    "DeploymentSuccessfulWaitWaiterConfigTypeDef",
    "ListApplicationRevisionsPaginatePaginationConfigTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsstringTypeDef",
    "ListApplicationRevisionsPaginateResponserevisionsTypeDef",
    "ListApplicationRevisionsPaginateResponseTypeDef",
    "ListApplicationsPaginatePaginationConfigTypeDef",
    "ListApplicationsPaginateResponseTypeDef",
    "ListDeploymentConfigsPaginatePaginationConfigTypeDef",
    "ListDeploymentConfigsPaginateResponseTypeDef",
    "ListDeploymentGroupsPaginatePaginationConfigTypeDef",
    "ListDeploymentGroupsPaginateResponseTypeDef",
    "ListDeploymentInstancesPaginatePaginationConfigTypeDef",
    "ListDeploymentInstancesPaginateResponseTypeDef",
    "ListDeploymentTargetsPaginatePaginationConfigTypeDef",
    "ListDeploymentTargetsPaginateResponseTypeDef",
    "ListDeploymentsPaginateCreateTimeRangeTypeDef",
    "ListDeploymentsPaginatePaginationConfigTypeDef",
    "ListDeploymentsPaginateResponseTypeDef",
    "ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef",
    "ListGitHubAccountTokenNamesPaginateResponseTypeDef",
    "ListOnPremisesInstancesPaginatePaginationConfigTypeDef",
    "ListOnPremisesInstancesPaginateResponseTypeDef",
    "ListOnPremisesInstancesPaginateTagFiltersTypeDef",
)


_ClientAddTagsToOnPremisesInstancesTagsTypeDef = TypedDict(
    "_ClientAddTagsToOnPremisesInstancesTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToOnPremisesInstancesTagsTypeDef(_ClientAddTagsToOnPremisesInstancesTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef,
        "gitHubLocation": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef,
        "string": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef,
        "appSpecContent": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsResponserevisionsTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponserevisionsTypeDef",
    {
        "revisionLocation": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef,
        "genericRevisionInfo": ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponserevisionsTypeDef(
    _ClientBatchGetApplicationRevisionsResponserevisionsTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsResponseTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsResponseTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List[ClientBatchGetApplicationRevisionsResponserevisionsTypeDef],
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsResponseTypeDef(
    _ClientBatchGetApplicationRevisionsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a BatchGetApplicationRevisions operation.
      - **applicationName** *(string) --*

        The name of the application that corresponds to the revisions.
    """


_ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef(
    _ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef(
    _ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef(
    _ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsRevisionsstringTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsRevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetApplicationRevisionsRevisionsstringTypeDef(
    _ClientBatchGetApplicationRevisionsRevisionsstringTypeDef
):
    pass


_ClientBatchGetApplicationRevisionsRevisionsTypeDef = TypedDict(
    "_ClientBatchGetApplicationRevisionsRevisionsTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef,
        "gitHubLocation": ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef,
        "string": ClientBatchGetApplicationRevisionsRevisionsstringTypeDef,
        "appSpecContent": ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetApplicationRevisionsRevisionsTypeDef(
    _ClientBatchGetApplicationRevisionsRevisionsTypeDef
):
    """
    - *(dict) --*

      Information about the location of an application revision.
      - **revisionType** *(string) --*

        The type of application revision:
        * S3: An application revision stored in Amazon S3.
        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ClientBatchGetApplicationsResponseapplicationsInfoTypeDef = TypedDict(
    "_ClientBatchGetApplicationsResponseapplicationsInfoTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)


class ClientBatchGetApplicationsResponseapplicationsInfoTypeDef(
    _ClientBatchGetApplicationsResponseapplicationsInfoTypeDef
):
    """
    - *(dict) --*

      Information about an application.
      - **applicationId** *(string) --*

        The application ID.
    """


_ClientBatchGetApplicationsResponseTypeDef = TypedDict(
    "_ClientBatchGetApplicationsResponseTypeDef",
    {"applicationsInfo": List[ClientBatchGetApplicationsResponseapplicationsInfoTypeDef]},
    total=False,
)


class ClientBatchGetApplicationsResponseTypeDef(_ClientBatchGetApplicationsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a BatchGetApplications operation.
      - **applicationsInfo** *(list) --*

        Information about the applications.
        - *(dict) --*

          Information about an application.
          - **applicationId** *(string) --*

            The application ID.
    """


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[
                ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef
):
    pass


_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef
        ],
        "onPremisesInstanceTagFilters": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef
        ],
        "autoScalingGroups": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef
        ],
        "serviceRoleArn": str,
        "targetRevision": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef,
        "triggerConfigurations": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef
        ],
        "alarmConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef,
        "autoRollbackConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef,
        "deploymentStyle": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef,
        "blueGreenDeploymentConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef,
        "lastSuccessfulDeployment": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef,
        "lastAttemptedDeployment": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef,
        "ec2TagSet": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef,
        "onPremisesTagSet": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
        "ecsServices": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef(
    _ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef
):
    """
    - *(dict) --*

      Information about a deployment group.
      - **applicationName** *(string) --*

        The application name.
    """


_ClientBatchGetDeploymentGroupsResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentGroupsResponseTypeDef",
    {
        "deploymentGroupsInfo": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef
        ],
        "errorMessage": str,
    },
    total=False,
)


class ClientBatchGetDeploymentGroupsResponseTypeDef(_ClientBatchGetDeploymentGroupsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a BatchGetDeploymentGroups operation.
      - **deploymentGroupsInfo** *(list) --*

        Information about the deployment groups.
        - *(dict) --*

          Information about a deployment group.
          - **applicationName** *(string) --*

            The application name.
    """


_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef(
    _ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef
):
    pass


_ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef
        ],
        "instanceType": Literal["Blue", "Green"],
    },
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef(
    _ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef
):
    """
    - *(dict) --*

      Information about an instance in a deployment.
      - **deploymentId** *(string) --*

        The unique ID of a deployment.
    """


_ClientBatchGetDeploymentInstancesResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentInstancesResponseTypeDef",
    {
        "instancesSummary": List[ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef],
        "errorMessage": str,
    },
    total=False,
)


class ClientBatchGetDeploymentInstancesResponseTypeDef(
    _ClientBatchGetDeploymentInstancesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a BatchGetDeploymentInstances operation.
      - **instancesSummary** *(list) --*

        Information about the instance.
        - *(dict) --*

          Information about an instance in a deployment.
          - **deploymentId** *(string) --*

            The unique ID of a deployment.
    """


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef,
        "taskSetLabel": Literal["Blue", "Green"],
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef
        ],
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "taskSetsInfo": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef
        ],
        "instanceLabel": Literal["Blue", "Green"],
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef
        ],
        "lambdaFunctionInfo": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef
):
    pass


_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef",
    {
        "deploymentTargetType": Literal["InstanceTarget", "LambdaTarget", "ECSTarget"],
        "instanceTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef,
        "lambdaTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef,
        "ecsTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef(
    _ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef
):
    """
    - *(dict) --*

      Information about the deployment target.
      - **deploymentTargetType** *(string) --*

        The deployment type that is specific to the deployment's compute platform.
    """


_ClientBatchGetDeploymentTargetsResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentTargetsResponseTypeDef",
    {"deploymentTargets": List[ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef]},
    total=False,
)


class ClientBatchGetDeploymentTargetsResponseTypeDef(
    _ClientBatchGetDeploymentTargetsResponseTypeDef
):
    """
    - *(dict) --*

      - **deploymentTargets** *(list) --*

        A list of target objects for a deployment. Each target object contains details about the
        target, such as its status and lifecycle events. The type of the target objects depends on
        the deployment' compute platform.
        * **EC2/On-premises** : Each target object is an EC2 or on-premises instance.
        * **AWS Lambda** : The target object is a specific version of an AWS Lambda function.
        * **Amazon ECS** : The target object is an Amazon ECS service.
        - *(dict) --*

          Information about the deployment target.
          - **deploymentTargetType** *(string) --*

            The deployment type that is specific to the deployment's compute platform.
    """


_ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef",
    {
        "code": Literal[
            "AGENT_ISSUE",
            "ALARM_ACTIVE",
            "APPLICATION_MISSING",
            "AUTOSCALING_VALIDATION_ERROR",
            "AUTO_SCALING_CONFIGURATION",
            "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
            "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
            "CUSTOMER_APPLICATION_UNHEALTHY",
            "DEPLOYMENT_GROUP_MISSING",
            "ECS_UPDATE_ERROR",
            "ELASTIC_LOAD_BALANCING_INVALID",
            "ELB_INVALID_INSTANCE",
            "HEALTH_CONSTRAINTS",
            "HEALTH_CONSTRAINTS_INVALID",
            "HOOK_EXECUTION_FAILURE",
            "IAM_ROLE_MISSING",
            "IAM_ROLE_PERMISSIONS",
            "INTERNAL_ERROR",
            "INVALID_ECS_SERVICE",
            "INVALID_LAMBDA_CONFIGURATION",
            "INVALID_LAMBDA_FUNCTION",
            "INVALID_REVISION",
            "MANUAL_STOP",
            "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
            "MISSING_ELB_INFORMATION",
            "MISSING_GITHUB_TOKEN",
            "NO_EC2_SUBSCRIPTION",
            "NO_INSTANCES",
            "OVER_MAX_INSTANCES",
            "RESOURCE_LIMIT_EXCEEDED",
            "REVISION_MISSING",
            "THROTTLED",
            "TIMEOUT",
        ],
        "message": str,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef",
    {"rollbackDeploymentId": str, "rollbackTriggeringDeploymentId": str, "rollbackMessage": str},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef",
    {
        "tagFilters": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef
        ],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef,
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef
):
    pass


_ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef,
        "revision": ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "errorInformation": ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef,
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef,
        "description": str,
        "creator": Literal["user", "autoscaling", "codeDeployRollback"],
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef,
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef,
        "deploymentStyle": ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef,
        "targetInstances": ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef,
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef,
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": Literal["DISALLOW", "OVERWRITE", "RETAIN"],
        "deploymentStatusMessages": List[str],
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)


class ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef(
    _ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef
):
    """
    - *(dict) --*

      Information about a deployment.
      - **applicationName** *(string) --*

        The application name.
    """


_ClientBatchGetDeploymentsResponseTypeDef = TypedDict(
    "_ClientBatchGetDeploymentsResponseTypeDef",
    {"deploymentsInfo": List[ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef]},
    total=False,
)


class ClientBatchGetDeploymentsResponseTypeDef(_ClientBatchGetDeploymentsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a BatchGetDeployments operation.
      - **deploymentsInfo** *(list) --*

        Information about the deployments.
        - *(dict) --*

          Information about a deployment.
          - **applicationName** *(string) --*

            The application name.
    """


_ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef = TypedDict(
    "_ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef(
    _ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef
):
    pass


_ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef = TypedDict(
    "_ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List[ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef],
    },
    total=False,
)


class ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef(
    _ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef
):
    """
    - *(dict) --*

      Information about an on-premises instance.
      - **instanceName** *(string) --*

        The name of the on-premises instance.
    """


_ClientBatchGetOnPremisesInstancesResponseTypeDef = TypedDict(
    "_ClientBatchGetOnPremisesInstancesResponseTypeDef",
    {"instanceInfos": List[ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef]},
    total=False,
)


class ClientBatchGetOnPremisesInstancesResponseTypeDef(
    _ClientBatchGetOnPremisesInstancesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a BatchGetOnPremisesInstances operation.
      - **instanceInfos** *(list) --*

        Information about the on-premises instances.
        - *(dict) --*

          Information about an on-premises instance.
          - **instanceName** *(string) --*

            The name of the on-premises instance.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef", {"applicationId": str}, total=False
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a CreateApplication operation.
      - **applicationId** *(string) --*

        A unique application ID.
    """


_ClientCreateApplicationTagsTypeDef = TypedDict(
    "_ClientCreateApplicationTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(_ClientCreateApplicationTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateDeploymentAutoRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentAutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)


class ClientCreateDeploymentAutoRollbackConfigurationTypeDef(
    _ClientCreateDeploymentAutoRollbackConfigurationTypeDef
):
    """
    Configuration information for an automatic rollback that is added when a deployment is created.
    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.
    """


_ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef",
    {"value": int, "type": Literal["HOST_COUNT", "FLEET_PERCENT"]},
    total=False,
)


class ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef(
    _ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef
):
    """
    The minimum number of healthy instances that should be available at any time during the
    deployment. There are two parameters expected in the input: type and value.
    The type parameter takes either of the following values:
    * HOST_COUNT: The value parameter represents the minimum number of healthy instances as an
    absolute value.
    * FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a
    percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at
    the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of
    instance and rounds up fractional instances.
    The value parameter takes an integer.
    For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a
    value of 95.
    - **value** *(integer) --*

      The minimum healthy instance value.
    """


_ClientCreateDeploymentConfigResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigResponseTypeDef", {"deploymentConfigId": str}, total=False
)


class ClientCreateDeploymentConfigResponseTypeDef(_ClientCreateDeploymentConfigResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a CreateDeploymentConfig operation.
      - **deploymentConfigId** *(string) --*

        A unique deployment configuration ID.
    """


_ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef",
    {"canaryPercentage": int, "canaryInterval": int},
    total=False,
)


class ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef(
    _ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef
):
    pass


_ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef",
    {"linearPercentage": int, "linearInterval": int},
    total=False,
)


class ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef(
    _ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef
):
    pass


_ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef = TypedDict(
    "_ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef",
    {
        "type": Literal["TimeBasedCanary", "TimeBasedLinear", "AllAtOnce"],
        "timeBasedCanary": ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef,
        "timeBasedLinear": ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef(
    _ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef
):
    """
    The configuration that specifies how the deployment traffic is routed.
    - **type** *(string) --*

      The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a
      deployment configuration .
    """


_ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef", {"name": str}, total=False
)


class ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef(
    _ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef
):
    pass


_ClientCreateDeploymentGroupAlarmConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupAlarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef],
    },
    total=False,
)


class ClientCreateDeploymentGroupAlarmConfigurationTypeDef(
    _ClientCreateDeploymentGroupAlarmConfigurationTypeDef
):
    """
    Information to add about Amazon CloudWatch alarms when the deployment group is created.
    - **enabled** *(boolean) --*

      Indicates whether the alarm configuration is enabled.
    """


_ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)


class ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef(
    _ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef
):
    """
    Configuration information for an automatic rollback that is added when a deployment group is
    created.
    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.
    """


_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)


class ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    pass


_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)


class ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    pass


_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a blue/green
      deployment.
      - **action** *(string) --*

        The action to take on instances in the original environment after a successful blue/green
        deployment.
        * TERMINATE: Instances are terminated after a specified wait time.
        * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
        and removed from the deployment group.
    """


_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef(
    _ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef
):
    """
    Information about blue/green deployment options for a deployment group.
    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a blue/green
      deployment.
      - **action** *(string) --*

        The action to take on instances in the original environment after a successful blue/green
        deployment.
        * TERMINATE: Instances are terminated after a specified wait time.
        * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
        and removed from the deployment group.
    """


_ClientCreateDeploymentGroupDeploymentStyleTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupDeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)


class ClientCreateDeploymentGroupDeploymentStyleTypeDef(
    _ClientCreateDeploymentGroupDeploymentStyleTypeDef
):
    """
    Information about the type of deployment, in-place or blue/green, that you want to run and
    whether to route deployment traffic behind a load balancer.
    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.
    """


_ClientCreateDeploymentGroupEc2TagFiltersTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupEc2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientCreateDeploymentGroupEc2TagFiltersTypeDef(
    _ClientCreateDeploymentGroupEc2TagFiltersTypeDef
):
    """
    - *(dict) --*

      Information about an EC2 tag filter.
      - **Key** *(string) --*

        The tag filter key.
    """


_ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef(
    _ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef
):
    """
    - *(dict) --*

      Information about an EC2 tag filter.
      - **Key** *(string) --*

        The tag filter key.
    """


_ClientCreateDeploymentGroupEc2TagSetTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupEc2TagSetTypeDef",
    {"ec2TagSetList": List[List[ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef]]},
    total=False,
)


class ClientCreateDeploymentGroupEc2TagSetTypeDef(_ClientCreateDeploymentGroupEc2TagSetTypeDef):
    """
    Information about groups of tags applied to EC2 instances. The deployment group includes only
    EC2 instances identified by all the tag groups. Cannot be used in the same call as
    ec2TagFilters.
    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be included in
      the deployment group, it must be identified by all of the tag groups in the list.
      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.
          - **Key** *(string) --*

            The tag filter key.
    """


_ClientCreateDeploymentGroupEcsServicesTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupEcsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientCreateDeploymentGroupEcsServicesTypeDef(_ClientCreateDeploymentGroupEcsServicesTypeDef):
    """
    - *(dict) --*

      Contains the service and cluster names used to identify an Amazon ECS deployment's target.
      - **serviceName** *(string) --*

        The name of the target Amazon ECS service.
    """


_ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef", {"name": str}, total=False
)


class ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef(
    _ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef
):
    pass


_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef(
    _ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef
):
    pass


_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    pass


_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    pass


_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    pass


_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef
):
    pass


_ClientCreateDeploymentGroupLoadBalancerInfoTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupLoadBalancerInfoTypeDef",
    {
        "elbInfoList": List[ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef],
        "targetGroupInfoList": List[
            ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientCreateDeploymentGroupLoadBalancerInfoTypeDef(
    _ClientCreateDeploymentGroupLoadBalancerInfoTypeDef
):
    """
    Information about the load balancer used in a deployment.
    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in a
      deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.
      .. note::

        Adding more than one load balancer to the array is not supported.
    """


_ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef(
    _ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef
):
    """
    - *(dict) --*

      Information about an on-premises instance tag filter.
      - **Key** *(string) --*

        The on-premises instance tag filter key.
    """


_ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef
):
    """
    - *(dict) --*

      Information about an on-premises instance tag filter.
      - **Key** *(string) --*

        The on-premises instance tag filter key.
    """


_ClientCreateDeploymentGroupOnPremisesTagSetTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupOnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientCreateDeploymentGroupOnPremisesTagSetTypeDef(
    _ClientCreateDeploymentGroupOnPremisesTagSetTypeDef
):
    """
    Information about groups of tags applied to on-premises instances. The deployment group includes
    only on-premises instances identified by all of the tag groups. Cannot be used in the same call
    as onPremisesInstanceTagFilters.
    - **onPremisesTagSetList** *(list) --*

      A list that contains other lists of on-premises instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in the list.
      - *(list) --*

        - *(dict) --*

          Information about an on-premises instance tag filter.
          - **Key** *(string) --*

            The on-premises instance tag filter key.
    """


_ClientCreateDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupResponseTypeDef", {"deploymentGroupId": str}, total=False
)


class ClientCreateDeploymentGroupResponseTypeDef(_ClientCreateDeploymentGroupResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a CreateDeploymentGroup operation.
      - **deploymentGroupId** *(string) --*

        A unique deployment group ID.
    """


_ClientCreateDeploymentGroupTagsTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDeploymentGroupTagsTypeDef(_ClientCreateDeploymentGroupTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientCreateDeploymentGroupTriggerConfigurationsTypeDef = TypedDict(
    "_ClientCreateDeploymentGroupTriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)


class ClientCreateDeploymentGroupTriggerConfigurationsTypeDef(
    _ClientCreateDeploymentGroupTriggerConfigurationsTypeDef
):
    """
    - *(dict) --*

      Information about notification triggers for the deployment group.
      - **triggerName** *(string) --*

        The name of the notification trigger.
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef", {"deploymentId": str}, total=False
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a CreateDeployment operation.
      - **deploymentId** *(string) --*

        The unique ID of a deployment.
    """


_ClientCreateDeploymentRevisionappSpecContentTypeDef = TypedDict(
    "_ClientCreateDeploymentRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientCreateDeploymentRevisionappSpecContentTypeDef(
    _ClientCreateDeploymentRevisionappSpecContentTypeDef
):
    pass


_ClientCreateDeploymentRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientCreateDeploymentRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientCreateDeploymentRevisiongitHubLocationTypeDef(
    _ClientCreateDeploymentRevisiongitHubLocationTypeDef
):
    pass


_ClientCreateDeploymentRevisions3LocationTypeDef = TypedDict(
    "_ClientCreateDeploymentRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientCreateDeploymentRevisions3LocationTypeDef(
    _ClientCreateDeploymentRevisions3LocationTypeDef
):
    pass


_ClientCreateDeploymentRevisionstringTypeDef = TypedDict(
    "_ClientCreateDeploymentRevisionstringTypeDef", {"content": str, "sha256": str}, total=False
)


class ClientCreateDeploymentRevisionstringTypeDef(_ClientCreateDeploymentRevisionstringTypeDef):
    pass


_ClientCreateDeploymentRevisionTypeDef = TypedDict(
    "_ClientCreateDeploymentRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientCreateDeploymentRevisions3LocationTypeDef,
        "gitHubLocation": ClientCreateDeploymentRevisiongitHubLocationTypeDef,
        "string": ClientCreateDeploymentRevisionstringTypeDef,
        "appSpecContent": ClientCreateDeploymentRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentRevisionTypeDef(_ClientCreateDeploymentRevisionTypeDef):
    """
    The type and location of the revision to deploy.
    - **revisionType** *(string) --*

      The type of application revision:
      * S3: An application revision stored in Amazon S3.
      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef(
    _ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef
):
    pass


_ClientCreateDeploymentTargetInstancesec2TagSetTypeDef = TypedDict(
    "_ClientCreateDeploymentTargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientCreateDeploymentTargetInstancesec2TagSetTypeDef(
    _ClientCreateDeploymentTargetInstancesec2TagSetTypeDef
):
    pass


_ClientCreateDeploymentTargetInstancestagFiltersTypeDef = TypedDict(
    "_ClientCreateDeploymentTargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientCreateDeploymentTargetInstancestagFiltersTypeDef(
    _ClientCreateDeploymentTargetInstancestagFiltersTypeDef
):
    """
    - *(dict) --*

      Information about an EC2 tag filter.
      - **Key** *(string) --*

        The tag filter key.
    """


_ClientCreateDeploymentTargetInstancesTypeDef = TypedDict(
    "_ClientCreateDeploymentTargetInstancesTypeDef",
    {
        "tagFilters": List[ClientCreateDeploymentTargetInstancestagFiltersTypeDef],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientCreateDeploymentTargetInstancesec2TagSetTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentTargetInstancesTypeDef(_ClientCreateDeploymentTargetInstancesTypeDef):
    """
    Information about the instances that belong to the replacement environment in a blue/green
    deployment.
    - **tagFilters** *(list) --*

      The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement
      environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet.
      - *(dict) --*

        Information about an EC2 tag filter.
        - **Key** *(string) --*

          The tag filter key.
    """


_ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef = TypedDict(
    "_ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef(
    _ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef
):
    """
    - *(dict) --*

      Information about an Auto Scaling group.
      - **name** *(string) --*

        The Auto Scaling group name.
    """


_ClientDeleteDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientDeleteDeploymentGroupResponseTypeDef",
    {"hooksNotCleanedUp": List[ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef]},
    total=False,
)


class ClientDeleteDeploymentGroupResponseTypeDef(_ClientDeleteDeploymentGroupResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a DeleteDeploymentGroup operation.
      - **hooksNotCleanedUp** *(list) --*

        If the output contains no data, and the corresponding deployment group contained at least
        one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling
        lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group. If the output
        contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from
        the Amazon EC2 instances in the Auto Scaling group.
        - *(dict) --*

          Information about an Auto Scaling group.
          - **name** *(string) --*

            The Auto Scaling group name.
    """


_ClientDeleteGitHubAccountTokenResponseTypeDef = TypedDict(
    "_ClientDeleteGitHubAccountTokenResponseTypeDef", {"tokenName": str}, total=False
)


class ClientDeleteGitHubAccountTokenResponseTypeDef(_ClientDeleteGitHubAccountTokenResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a DeleteGitHubAccountToken operation.
      - **tokenName** *(string) --*

        The name of the GitHub account connection that was deleted.
    """


_ClientGetApplicationResponseapplicationTypeDef = TypedDict(
    "_ClientGetApplicationResponseapplicationTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)


class ClientGetApplicationResponseapplicationTypeDef(
    _ClientGetApplicationResponseapplicationTypeDef
):
    """
    - **application** *(dict) --*

      Information about the application.
      - **applicationId** *(string) --*

        The application ID.
    """


_ClientGetApplicationResponseTypeDef = TypedDict(
    "_ClientGetApplicationResponseTypeDef",
    {"application": ClientGetApplicationResponseapplicationTypeDef},
    total=False,
)


class ClientGetApplicationResponseTypeDef(_ClientGetApplicationResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a GetApplication operation.
      - **application** *(dict) --*

        Information about the application.
        - **applicationId** *(string) --*

          The application ID.
    """


_ClientGetApplicationRevisionResponserevisionInfoTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)


class ClientGetApplicationRevisionResponserevisionInfoTypeDef(
    _ClientGetApplicationRevisionResponserevisionInfoTypeDef
):
    pass


_ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef(
    _ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef
):
    pass


_ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef(
    _ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef
):
    pass


_ClientGetApplicationRevisionResponserevisions3LocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientGetApplicationRevisionResponserevisions3LocationTypeDef(
    _ClientGetApplicationRevisionResponserevisions3LocationTypeDef
):
    pass


_ClientGetApplicationRevisionResponserevisionstringTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionResponserevisionstringTypeDef(
    _ClientGetApplicationRevisionResponserevisionstringTypeDef
):
    pass


_ClientGetApplicationRevisionResponserevisionTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponserevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetApplicationRevisionResponserevisions3LocationTypeDef,
        "gitHubLocation": ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef,
        "string": ClientGetApplicationRevisionResponserevisionstringTypeDef,
        "appSpecContent": ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetApplicationRevisionResponserevisionTypeDef(
    _ClientGetApplicationRevisionResponserevisionTypeDef
):
    pass


_ClientGetApplicationRevisionResponseTypeDef = TypedDict(
    "_ClientGetApplicationRevisionResponseTypeDef",
    {
        "applicationName": str,
        "revision": ClientGetApplicationRevisionResponserevisionTypeDef,
        "revisionInfo": ClientGetApplicationRevisionResponserevisionInfoTypeDef,
    },
    total=False,
)


class ClientGetApplicationRevisionResponseTypeDef(_ClientGetApplicationRevisionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a GetApplicationRevision operation.
      - **applicationName** *(string) --*

        The name of the application that corresponds to the revision.
    """


_ClientGetApplicationRevisionRevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetApplicationRevisionRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionRevisionappSpecContentTypeDef(
    _ClientGetApplicationRevisionRevisionappSpecContentTypeDef
):
    pass


_ClientGetApplicationRevisionRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetApplicationRevisionRevisiongitHubLocationTypeDef(
    _ClientGetApplicationRevisionRevisiongitHubLocationTypeDef
):
    pass


_ClientGetApplicationRevisionRevisions3LocationTypeDef = TypedDict(
    "_ClientGetApplicationRevisionRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientGetApplicationRevisionRevisions3LocationTypeDef(
    _ClientGetApplicationRevisionRevisions3LocationTypeDef
):
    pass


_ClientGetApplicationRevisionRevisionstringTypeDef = TypedDict(
    "_ClientGetApplicationRevisionRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetApplicationRevisionRevisionstringTypeDef(
    _ClientGetApplicationRevisionRevisionstringTypeDef
):
    pass


_ClientGetApplicationRevisionRevisionTypeDef = TypedDict(
    "_ClientGetApplicationRevisionRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetApplicationRevisionRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetApplicationRevisionRevisiongitHubLocationTypeDef,
        "string": ClientGetApplicationRevisionRevisionstringTypeDef,
        "appSpecContent": ClientGetApplicationRevisionRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetApplicationRevisionRevisionTypeDef(_ClientGetApplicationRevisionRevisionTypeDef):
    """
    Information about the application revision to get, including type and location.
    - **revisionType** *(string) --*

      The type of application revision:
      * S3: An application revision stored in Amazon S3.
      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef",
    {"value": int, "type": Literal["HOST_COUNT", "FLEET_PERCENT"]},
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef
):
    pass


_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef",
    {"canaryPercentage": int, "canaryInterval": int},
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef
):
    pass


_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef",
    {"linearPercentage": int, "linearInterval": int},
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef
):
    pass


_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef",
    {
        "type": Literal["TimeBasedCanary", "TimeBasedLinear", "AllAtOnce"],
        "timeBasedCanary": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef,
        "timeBasedLinear": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef,
    },
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef
):
    pass


_ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": str,
        "deploymentConfigName": str,
        "minimumHealthyHosts": ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef,
        "createTime": datetime,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
        "trafficRoutingConfig": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef,
    },
    total=False,
)


class ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef(
    _ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef
):
    """
    - **deploymentConfigInfo** *(dict) --*

      Information about the deployment configuration.
      - **deploymentConfigId** *(string) --*

        The deployment configuration ID.
    """


_ClientGetDeploymentConfigResponseTypeDef = TypedDict(
    "_ClientGetDeploymentConfigResponseTypeDef",
    {"deploymentConfigInfo": ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef},
    total=False,
)


class ClientGetDeploymentConfigResponseTypeDef(_ClientGetDeploymentConfigResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a GetDeploymentConfig operation.
      - **deploymentConfigInfo** *(dict) --*

        Information about the deployment configuration.
        - **deploymentConfigId** *(string) --*

          The deployment configuration ID.
    """


_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[
                ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef
):
    pass


_ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef
        ],
        "onPremisesInstanceTagFilters": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef
        ],
        "autoScalingGroups": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef
        ],
        "serviceRoleArn": str,
        "targetRevision": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef,
        "triggerConfigurations": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef
        ],
        "alarmConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef,
        "autoRollbackConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef,
        "deploymentStyle": ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef,
        "blueGreenDeploymentConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef,
        "lastSuccessfulDeployment": ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef,
        "lastAttemptedDeployment": ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef,
        "ec2TagSet": ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef,
        "onPremisesTagSet": ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
        "ecsServices": List[ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef],
    },
    total=False,
)


class ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef(
    _ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef
):
    """
    - **deploymentGroupInfo** *(dict) --*

      Information about the deployment group.
      - **applicationName** *(string) --*

        The application name.
    """


_ClientGetDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientGetDeploymentGroupResponseTypeDef",
    {"deploymentGroupInfo": ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef},
    total=False,
)


class ClientGetDeploymentGroupResponseTypeDef(_ClientGetDeploymentGroupResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a GetDeploymentGroup operation.
      - **deploymentGroupInfo** *(dict) --*

        Information about the deployment group.
        - **applicationName** *(string) --*

          The application name.
    """


_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef(
    _ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef
):
    pass


_ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef
        ],
        "instanceType": Literal["Blue", "Green"],
    },
    total=False,
)


class ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef(
    _ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef
):
    """
    - **instanceSummary** *(dict) --*

      Information about the instance.
      - **deploymentId** *(string) --*

        The unique ID of a deployment.
    """


_ClientGetDeploymentInstanceResponseTypeDef = TypedDict(
    "_ClientGetDeploymentInstanceResponseTypeDef",
    {"instanceSummary": ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef},
    total=False,
)


class ClientGetDeploymentInstanceResponseTypeDef(_ClientGetDeploymentInstanceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a GetDeploymentInstance operation.
      - **instanceSummary** *(dict) --*

        Information about the instance.
        - **deploymentId** *(string) --*

          The unique ID of a deployment.
    """


_ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef(
    _ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef(
    _ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef",
    {
        "code": Literal[
            "AGENT_ISSUE",
            "ALARM_ACTIVE",
            "APPLICATION_MISSING",
            "AUTOSCALING_VALIDATION_ERROR",
            "AUTO_SCALING_CONFIGURATION",
            "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
            "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
            "CUSTOMER_APPLICATION_UNHEALTHY",
            "DEPLOYMENT_GROUP_MISSING",
            "ECS_UPDATE_ERROR",
            "ELASTIC_LOAD_BALANCING_INVALID",
            "ELB_INVALID_INSTANCE",
            "HEALTH_CONSTRAINTS",
            "HEALTH_CONSTRAINTS_INVALID",
            "HOOK_EXECUTION_FAILURE",
            "IAM_ROLE_MISSING",
            "IAM_ROLE_PERMISSIONS",
            "INTERNAL_ERROR",
            "INVALID_ECS_SERVICE",
            "INVALID_LAMBDA_CONFIGURATION",
            "INVALID_LAMBDA_FUNCTION",
            "INVALID_REVISION",
            "MANUAL_STOP",
            "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
            "MISSING_ELB_INFORMATION",
            "MISSING_GITHUB_TOKEN",
            "NO_EC2_SUBSCRIPTION",
            "NO_INSTANCES",
            "OVER_MAX_INSTANCES",
            "RESOURCE_LIMIT_EXCEEDED",
            "REVISION_MISSING",
            "THROTTLED",
            "TIMEOUT",
        ],
        "message": str,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef(
    _ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInforevisionTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforevisionTypeDef(
    _ClientGetDeploymentResponsedeploymentInforevisionTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef",
    {"rollbackDeploymentId": str, "rollbackTriggeringDeploymentId": str, "rollbackMessage": str},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef(
    _ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef",
    {
        "tagFilters": List[
            ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef
        ],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef,
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef(
    _ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef
):
    pass


_ClientGetDeploymentResponsedeploymentInfoTypeDef = TypedDict(
    "_ClientGetDeploymentResponsedeploymentInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef,
        "revision": ClientGetDeploymentResponsedeploymentInforevisionTypeDef,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "errorInformation": ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef,
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef,
        "description": str,
        "creator": Literal["user", "autoscaling", "codeDeployRollback"],
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef,
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef,
        "deploymentStyle": ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef,
        "targetInstances": ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef,
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef,
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": Literal["DISALLOW", "OVERWRITE", "RETAIN"],
        "deploymentStatusMessages": List[str],
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)


class ClientGetDeploymentResponsedeploymentInfoTypeDef(
    _ClientGetDeploymentResponsedeploymentInfoTypeDef
):
    """
    - **deploymentInfo** *(dict) --*

      Information about the deployment.
      - **applicationName** *(string) --*

        The application name.
    """


_ClientGetDeploymentResponseTypeDef = TypedDict(
    "_ClientGetDeploymentResponseTypeDef",
    {"deploymentInfo": ClientGetDeploymentResponsedeploymentInfoTypeDef},
    total=False,
)


class ClientGetDeploymentResponseTypeDef(_ClientGetDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a GetDeployment operation.
      - **deploymentInfo** *(dict) --*

        Information about the deployment.
        - **applicationName** *(string) --*

          The application name.
    """


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef",
    {"name": str},
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef,
        "taskSetLabel": Literal["Blue", "Green"],
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef
        ],
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "taskSetsInfo": List[
            ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef
        ],
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef
        ],
        "instanceLabel": Literal["Blue", "Green"],
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef
        ],
        "lambdaFunctionInfo": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef
):
    pass


_ClientGetDeploymentTargetResponsedeploymentTargetTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponsedeploymentTargetTypeDef",
    {
        "deploymentTargetType": Literal["InstanceTarget", "LambdaTarget", "ECSTarget"],
        "instanceTarget": ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef,
        "lambdaTarget": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef,
        "ecsTarget": ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef,
    },
    total=False,
)


class ClientGetDeploymentTargetResponsedeploymentTargetTypeDef(
    _ClientGetDeploymentTargetResponsedeploymentTargetTypeDef
):
    """
    - **deploymentTarget** *(dict) --*

      A deployment target that contains information about a deployment such as its status, lifecyle
      events, and when it was last updated. It also contains metadata about the deployment target.
      The deployment target metadata depends on the deployment target's type (``instanceTarget`` ,
      ``lambdaTarget`` , or ``ecsTarget`` ).
      - **deploymentTargetType** *(string) --*

        The deployment type that is specific to the deployment's compute platform.
    """


_ClientGetDeploymentTargetResponseTypeDef = TypedDict(
    "_ClientGetDeploymentTargetResponseTypeDef",
    {"deploymentTarget": ClientGetDeploymentTargetResponsedeploymentTargetTypeDef},
    total=False,
)


class ClientGetDeploymentTargetResponseTypeDef(_ClientGetDeploymentTargetResponseTypeDef):
    """
    - *(dict) --*

      - **deploymentTarget** *(dict) --*

        A deployment target that contains information about a deployment such as its status,
        lifecyle events, and when it was last updated. It also contains metadata about the
        deployment target. The deployment target metadata depends on the deployment target's type
        (``instanceTarget`` , ``lambdaTarget`` , or ``ecsTarget`` ).
        - **deploymentTargetType** *(string) --*

          The deployment type that is specific to the deployment's compute platform.
    """


_ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef = TypedDict(
    "_ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef(
    _ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef
):
    pass


_ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef = TypedDict(
    "_ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List[ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef],
    },
    total=False,
)


class ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef(
    _ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef
):
    """
    - **instanceInfo** *(dict) --*

      Information about the on-premises instance.
      - **instanceName** *(string) --*

        The name of the on-premises instance.
    """


_ClientGetOnPremisesInstanceResponseTypeDef = TypedDict(
    "_ClientGetOnPremisesInstanceResponseTypeDef",
    {"instanceInfo": ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef},
    total=False,
)


class ClientGetOnPremisesInstanceResponseTypeDef(_ClientGetOnPremisesInstanceResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a GetOnPremisesInstance operation.
      - **instanceInfo** *(dict) --*

        Information about the on-premises instance.
        - **instanceName** *(string) --*

          The name of the on-premises instance.
    """


_ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef(
    _ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef
):
    pass


_ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef(
    _ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef
):
    pass


_ClientListApplicationRevisionsResponserevisionss3LocationTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionss3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientListApplicationRevisionsResponserevisionss3LocationTypeDef(
    _ClientListApplicationRevisionsResponserevisionss3LocationTypeDef
):
    pass


_ClientListApplicationRevisionsResponserevisionsstringTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsstringTypeDef(
    _ClientListApplicationRevisionsResponserevisionsstringTypeDef
):
    pass


_ClientListApplicationRevisionsResponserevisionsTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponserevisionsTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientListApplicationRevisionsResponserevisionss3LocationTypeDef,
        "gitHubLocation": ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef,
        "string": ClientListApplicationRevisionsResponserevisionsstringTypeDef,
        "appSpecContent": ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef,
    },
    total=False,
)


class ClientListApplicationRevisionsResponserevisionsTypeDef(
    _ClientListApplicationRevisionsResponserevisionsTypeDef
):
    """
    - *(dict) --*

      Information about the location of an application revision.
      - **revisionType** *(string) --*

        The type of application revision:
        * S3: An application revision stored in Amazon S3.
        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ClientListApplicationRevisionsResponseTypeDef = TypedDict(
    "_ClientListApplicationRevisionsResponseTypeDef",
    {"revisions": List[ClientListApplicationRevisionsResponserevisionsTypeDef], "nextToken": str},
    total=False,
)


class ClientListApplicationRevisionsResponseTypeDef(_ClientListApplicationRevisionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListApplicationRevisions operation.
      - **revisions** *(list) --*

        A list of locations that contain the matching revisions.
        - *(dict) --*

          Information about the location of an application revision.
          - **revisionType** *(string) --*

            The type of application revision:
            * S3: An application revision stored in Amazon S3.
            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {"applications": List[str], "nextToken": str},
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListApplications operation.
      - **applications** *(list) --*

        A list of application names.
        - *(string) --*
    """


_ClientListDeploymentConfigsResponseTypeDef = TypedDict(
    "_ClientListDeploymentConfigsResponseTypeDef",
    {"deploymentConfigsList": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentConfigsResponseTypeDef(_ClientListDeploymentConfigsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListDeploymentConfigs operation.
      - **deploymentConfigsList** *(list) --*

        A list of deployment configurations, including built-in configurations such as
        CodeDeployDefault.OneAtATime.
        - *(string) --*
    """


_ClientListDeploymentGroupsResponseTypeDef = TypedDict(
    "_ClientListDeploymentGroupsResponseTypeDef",
    {"applicationName": str, "deploymentGroups": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentGroupsResponseTypeDef(_ClientListDeploymentGroupsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListDeploymentGroups operation.
      - **applicationName** *(string) --*

        The application name.
    """


_ClientListDeploymentInstancesResponseTypeDef = TypedDict(
    "_ClientListDeploymentInstancesResponseTypeDef",
    {"instancesList": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentInstancesResponseTypeDef(_ClientListDeploymentInstancesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListDeploymentInstances operation.
      - **instancesList** *(list) --*

        A list of instance IDs.
        - *(string) --*
    """


_ClientListDeploymentTargetsResponseTypeDef = TypedDict(
    "_ClientListDeploymentTargetsResponseTypeDef",
    {"targetIds": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentTargetsResponseTypeDef(_ClientListDeploymentTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **targetIds** *(list) --*

        The unique IDs of deployment targets.
        - *(string) --*
    """


_ClientListDeploymentsCreateTimeRangeTypeDef = TypedDict(
    "_ClientListDeploymentsCreateTimeRangeTypeDef",
    {"start": datetime, "end": datetime},
    total=False,
)


class ClientListDeploymentsCreateTimeRangeTypeDef(_ClientListDeploymentsCreateTimeRangeTypeDef):
    """
    A time range (start and end) for returning a subset of the list of deployments.
    - **start** *(datetime) --*

      The start time of the time range.
      .. note::

        Specify null to leave the start time open-ended.
    """


_ClientListDeploymentsResponseTypeDef = TypedDict(
    "_ClientListDeploymentsResponseTypeDef",
    {"deployments": List[str], "nextToken": str},
    total=False,
)


class ClientListDeploymentsResponseTypeDef(_ClientListDeploymentsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListDeployments operation.
      - **deployments** *(list) --*

        A list of deployment IDs.
        - *(string) --*
    """


_ClientListGitHubAccountTokenNamesResponseTypeDef = TypedDict(
    "_ClientListGitHubAccountTokenNamesResponseTypeDef",
    {"tokenNameList": List[str], "nextToken": str},
    total=False,
)


class ClientListGitHubAccountTokenNamesResponseTypeDef(
    _ClientListGitHubAccountTokenNamesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ListGitHubAccountTokenNames operation.
      - **tokenNameList** *(list) --*

        A list of names of connections to GitHub accounts.
        - *(string) --*
    """


_ClientListOnPremisesInstancesResponseTypeDef = TypedDict(
    "_ClientListOnPremisesInstancesResponseTypeDef",
    {"instanceNames": List[str], "nextToken": str},
    total=False,
)


class ClientListOnPremisesInstancesResponseTypeDef(_ClientListOnPremisesInstancesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of the list on-premises instances operation.
      - **instanceNames** *(list) --*

        The list of matching on-premises instance names.
        - *(string) --*
    """


_ClientListOnPremisesInstancesTagFiltersTypeDef = TypedDict(
    "_ClientListOnPremisesInstancesTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientListOnPremisesInstancesTagFiltersTypeDef(
    _ClientListOnPremisesInstancesTagFiltersTypeDef
):
    """
    - *(dict) --*

      Information about an on-premises instance tag filter.
      - **Key** *(string) --*

        The on-premises instance tag filter key.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        A list of tags returned by ``ListTagsForResource`` . The tags are associated with the
        resource identified by the input ``ResourceArn`` parameter.
        - *(dict) --*

          Information about a tag.
          - **Key** *(string) --*

            The tag's key.
    """


_ClientPutLifecycleEventHookExecutionStatusResponseTypeDef = TypedDict(
    "_ClientPutLifecycleEventHookExecutionStatusResponseTypeDef",
    {"lifecycleEventHookExecutionId": str},
    total=False,
)


class ClientPutLifecycleEventHookExecutionStatusResponseTypeDef(
    _ClientPutLifecycleEventHookExecutionStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **lifecycleEventHookExecutionId** *(string) --*

        The execution ID of the lifecycle event hook. A hook is specified in the ``hooks`` section
        of the deployment's AppSpec file.
    """


_ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef(
    _ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef
):
    pass


_ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef(
    _ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef
):
    pass


_ClientRegisterApplicationRevisionRevisions3LocationTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ClientRegisterApplicationRevisionRevisions3LocationTypeDef(
    _ClientRegisterApplicationRevisionRevisions3LocationTypeDef
):
    pass


_ClientRegisterApplicationRevisionRevisionstringTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ClientRegisterApplicationRevisionRevisionstringTypeDef(
    _ClientRegisterApplicationRevisionRevisionstringTypeDef
):
    pass


_ClientRegisterApplicationRevisionRevisionTypeDef = TypedDict(
    "_ClientRegisterApplicationRevisionRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientRegisterApplicationRevisionRevisions3LocationTypeDef,
        "gitHubLocation": ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef,
        "string": ClientRegisterApplicationRevisionRevisionstringTypeDef,
        "appSpecContent": ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef,
    },
    total=False,
)


class ClientRegisterApplicationRevisionRevisionTypeDef(
    _ClientRegisterApplicationRevisionRevisionTypeDef
):
    """
    Information about the application revision to register, including type and location.
    - **revisionType** *(string) --*

      The type of application revision:
      * S3: An application revision stored in Amazon S3.
      * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
      * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef = TypedDict(
    "_ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef(
    _ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientStopDeploymentResponseTypeDef = TypedDict(
    "_ClientStopDeploymentResponseTypeDef",
    {"status": Literal["Pending", "Succeeded"], "statusMessage": str},
    total=False,
)


class ClientStopDeploymentResponseTypeDef(_ClientStopDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a StopDeployment operation.
      - **status** *(string) --*

        The status of the stop deployment operation:
        * Pending: The stop operation is pending.
        * Succeeded: The stop operation was successful.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag.
      - **Key** *(string) --*

        The tag's key.
    """


_ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef", {"name": str}, total=False
)


class ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef(
    _ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef
):
    pass


_ClientUpdateDeploymentGroupAlarmConfigurationTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupAlarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef],
    },
    total=False,
)


class ClientUpdateDeploymentGroupAlarmConfigurationTypeDef(
    _ClientUpdateDeploymentGroupAlarmConfigurationTypeDef
):
    """
    Information to add or change about Amazon CloudWatch alarms when the deployment group is
    updated.
    - **enabled** *(boolean) --*

      Indicates whether the alarm configuration is enabled.
    """


_ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)


class ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef(
    _ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef
):
    """
    Information for an automatic rollback configuration that is added or changed when a deployment
    group is updated.
    - **enabled** *(boolean) --*

      Indicates whether a defined automatic rollback configuration is currently enabled.
    """


_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)


class ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef(
    _ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef
):
    pass


_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)


class ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef(
    _ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef
):
    pass


_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)


class ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef(
    _ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef
):
    """
    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a blue/green
      deployment.
      - **action** *(string) --*

        The action to take on instances in the original environment after a successful blue/green
        deployment.
        * TERMINATE: Instances are terminated after a specified wait time.
        * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
        and removed from the deployment group.
    """


_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)


class ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef(
    _ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef
):
    """
    Information about blue/green deployment options for a deployment group.
    - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

      Information about whether to terminate instances in the original fleet during a blue/green
      deployment.
      - **action** *(string) --*

        The action to take on instances in the original environment after a successful blue/green
        deployment.
        * TERMINATE: Instances are terminated after a specified wait time.
        * KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer
        and removed from the deployment group.
    """


_ClientUpdateDeploymentGroupDeploymentStyleTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupDeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)


class ClientUpdateDeploymentGroupDeploymentStyleTypeDef(
    _ClientUpdateDeploymentGroupDeploymentStyleTypeDef
):
    """
    Information about the type of deployment, either in-place or blue/green, you want to run and
    whether to route deployment traffic behind a load balancer.
    - **deploymentType** *(string) --*

      Indicates whether to run an in-place deployment or a blue/green deployment.
    """


_ClientUpdateDeploymentGroupEc2TagFiltersTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupEc2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientUpdateDeploymentGroupEc2TagFiltersTypeDef(
    _ClientUpdateDeploymentGroupEc2TagFiltersTypeDef
):
    """
    - *(dict) --*

      Information about an EC2 tag filter.
      - **Key** *(string) --*

        The tag filter key.
    """


_ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef(
    _ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef
):
    """
    - *(dict) --*

      Information about an EC2 tag filter.
      - **Key** *(string) --*

        The tag filter key.
    """


_ClientUpdateDeploymentGroupEc2TagSetTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupEc2TagSetTypeDef",
    {"ec2TagSetList": List[List[ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef]]},
    total=False,
)


class ClientUpdateDeploymentGroupEc2TagSetTypeDef(_ClientUpdateDeploymentGroupEc2TagSetTypeDef):
    """
    Information about groups of tags applied to on-premises instances. The deployment group includes
    only EC2 instances identified by all the tag groups.
    - **ec2TagSetList** *(list) --*

      A list that contains other lists of EC2 instance tag groups. For an instance to be included in
      the deployment group, it must be identified by all of the tag groups in the list.
      - *(list) --*

        - *(dict) --*

          Information about an EC2 tag filter.
          - **Key** *(string) --*

            The tag filter key.
    """


_ClientUpdateDeploymentGroupEcsServicesTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupEcsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)


class ClientUpdateDeploymentGroupEcsServicesTypeDef(_ClientUpdateDeploymentGroupEcsServicesTypeDef):
    """
    - *(dict) --*

      Contains the service and cluster names used to identify an Amazon ECS deployment's target.
      - **serviceName** *(string) --*

        The name of the target Amazon ECS service.
    """


_ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef", {"name": str}, total=False
)


class ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef(
    _ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef
):
    pass


_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef(
    _ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef
):
    pass


_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef(
    _ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef
):
    pass


_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef(
    _ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
):
    pass


_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)


class ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef(
    _ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef
):
    pass


_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)


class ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef(
    _ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef
):
    pass


_ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef",
    {
        "elbInfoList": List[ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef],
        "targetGroupInfoList": List[
            ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef(
    _ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef
):
    """
    Information about the load balancer used in a deployment.
    - **elbInfoList** *(list) --*

      An array that contains information about the load balancer to use for load balancing in a
      deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.
      .. note::

        Adding more than one load balancer to the array is not supported.
    """


_ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef(
    _ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef
):
    """
    - *(dict) --*

      Information about an on-premises instance tag filter.
      - **Key** *(string) --*

        The on-premises instance tag filter key.
    """


_ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef(
    _ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef
):
    """
    - *(dict) --*

      Information about an on-premises instance tag filter.
      - **Key** *(string) --*

        The on-premises instance tag filter key.
    """


_ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef]
        ]
    },
    total=False,
)


class ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef(
    _ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef
):
    """
    Information about an on-premises instance tag set. The deployment group includes only
    on-premises instances identified by all the tag groups.
    - **onPremisesTagSetList** *(list) --*

      A list that contains other lists of on-premises instance tag groups. For an instance to be
      included in the deployment group, it must be identified by all of the tag groups in the list.
      - *(list) --*

        - *(dict) --*

          Information about an on-premises instance tag filter.
          - **Key** *(string) --*

            The on-premises instance tag filter key.
    """


_ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    {"name": str, "hook": str},
    total=False,
)


class ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef(
    _ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef
):
    """
    - *(dict) --*

      Information about an Auto Scaling group.
      - **name** *(string) --*

        The Auto Scaling group name.
    """


_ClientUpdateDeploymentGroupResponseTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupResponseTypeDef",
    {"hooksNotCleanedUp": List[ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef]},
    total=False,
)


class ClientUpdateDeploymentGroupResponseTypeDef(_ClientUpdateDeploymentGroupResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an UpdateDeploymentGroup operation.
      - **hooksNotCleanedUp** *(list) --*

        If the output contains no data, and the corresponding deployment group contained at least
        one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling
        lifecycle event hooks from the AWS account. If the output contains data, AWS CodeDeploy
        could not remove some Auto Scaling lifecycle event hooks from the AWS account.
        - *(dict) --*

          Information about an Auto Scaling group.
          - **name** *(string) --*

            The Auto Scaling group name.
    """


_ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef = TypedDict(
    "_ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)


class ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef(
    _ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef
):
    """
    - *(dict) --*

      Information about notification triggers for the deployment group.
      - **triggerName** *(string) --*

        The name of the notification trigger.
    """


_DeploymentSuccessfulWaitWaiterConfigTypeDef = TypedDict(
    "_DeploymentSuccessfulWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DeploymentSuccessfulWaitWaiterConfigTypeDef(_DeploymentSuccessfulWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_ListApplicationRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListApplicationRevisionsPaginatePaginationConfigTypeDef(
    _ListApplicationRevisionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef
):
    pass


_ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef
):
    pass


_ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef
):
    pass


_ListApplicationRevisionsPaginateResponserevisionsstringTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsstringTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsstringTypeDef
):
    pass


_ListApplicationRevisionsPaginateResponserevisionsTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponserevisionsTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ListApplicationRevisionsPaginateResponserevisionss3LocationTypeDef,
        "gitHubLocation": ListApplicationRevisionsPaginateResponserevisionsgitHubLocationTypeDef,
        "string": ListApplicationRevisionsPaginateResponserevisionsstringTypeDef,
        "appSpecContent": ListApplicationRevisionsPaginateResponserevisionsappSpecContentTypeDef,
    },
    total=False,
)


class ListApplicationRevisionsPaginateResponserevisionsTypeDef(
    _ListApplicationRevisionsPaginateResponserevisionsTypeDef
):
    """
    - *(dict) --*

      Information about the location of an application revision.
      - **revisionType** *(string) --*

        The type of application revision:
        * S3: An application revision stored in Amazon S3.
        * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
        * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ListApplicationRevisionsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationRevisionsPaginateResponseTypeDef",
    {"revisions": List[ListApplicationRevisionsPaginateResponserevisionsTypeDef], "NextToken": str},
    total=False,
)


class ListApplicationRevisionsPaginateResponseTypeDef(
    _ListApplicationRevisionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ListApplicationRevisions operation.
      - **revisions** *(list) --*

        A list of locations that contain the matching revisions.
        - *(dict) --*

          Information about the location of an application revision.
          - **revisionType** *(string) --*

            The type of application revision:
            * S3: An application revision stored in Amazon S3.
            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    """


_ListApplicationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApplicationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListApplicationsPaginatePaginationConfigTypeDef(
    _ListApplicationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListApplicationsPaginateResponseTypeDef = TypedDict(
    "_ListApplicationsPaginateResponseTypeDef",
    {"applications": List[str], "NextToken": str},
    total=False,
)


class ListApplicationsPaginateResponseTypeDef(_ListApplicationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListApplications operation.
      - **applications** *(list) --*

        A list of application names.
        - *(string) --*
    """


_ListDeploymentConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentConfigsPaginatePaginationConfigTypeDef(
    _ListDeploymentConfigsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeploymentConfigsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentConfigsPaginateResponseTypeDef",
    {"deploymentConfigsList": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentConfigsPaginateResponseTypeDef(_ListDeploymentConfigsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListDeploymentConfigs operation.
      - **deploymentConfigsList** *(list) --*

        A list of deployment configurations, including built-in configurations such as
        CodeDeployDefault.OneAtATime.
        - *(string) --*
    """


_ListDeploymentGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentGroupsPaginatePaginationConfigTypeDef(
    _ListDeploymentGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeploymentGroupsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentGroupsPaginateResponseTypeDef",
    {"applicationName": str, "deploymentGroups": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentGroupsPaginateResponseTypeDef(_ListDeploymentGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListDeploymentGroups operation.
      - **applicationName** *(string) --*

        The application name.
    """


_ListDeploymentInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentInstancesPaginatePaginationConfigTypeDef(
    _ListDeploymentInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeploymentInstancesPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentInstancesPaginateResponseTypeDef",
    {"instancesList": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentInstancesPaginateResponseTypeDef(
    _ListDeploymentInstancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ListDeploymentInstances operation.
      - **instancesList** *(list) --*

        A list of instance IDs.
        - *(string) --*
    """


_ListDeploymentTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentTargetsPaginatePaginationConfigTypeDef(
    _ListDeploymentTargetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeploymentTargetsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentTargetsPaginateResponseTypeDef",
    {"targetIds": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentTargetsPaginateResponseTypeDef(_ListDeploymentTargetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **targetIds** *(list) --*

        The unique IDs of deployment targets.
        - *(string) --*
    """


_ListDeploymentsPaginateCreateTimeRangeTypeDef = TypedDict(
    "_ListDeploymentsPaginateCreateTimeRangeTypeDef",
    {"start": datetime, "end": datetime},
    total=False,
)


class ListDeploymentsPaginateCreateTimeRangeTypeDef(_ListDeploymentsPaginateCreateTimeRangeTypeDef):
    """
    A time range (start and end) for returning a subset of the list of deployments.
    - **start** *(datetime) --*

      The start time of the time range.
      .. note::

        Specify null to leave the start time open-ended.
    """


_ListDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListDeploymentsPaginatePaginationConfigTypeDef(
    _ListDeploymentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeploymentsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentsPaginateResponseTypeDef",
    {"deployments": List[str], "NextToken": str},
    total=False,
)


class ListDeploymentsPaginateResponseTypeDef(_ListDeploymentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ListDeployments operation.
      - **deployments** *(list) --*

        A list of deployment IDs.
        - *(string) --*
    """


_ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef(
    _ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGitHubAccountTokenNamesPaginateResponseTypeDef = TypedDict(
    "_ListGitHubAccountTokenNamesPaginateResponseTypeDef",
    {"tokenNameList": List[str], "NextToken": str},
    total=False,
)


class ListGitHubAccountTokenNamesPaginateResponseTypeDef(
    _ListGitHubAccountTokenNamesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ListGitHubAccountTokenNames operation.
      - **tokenNameList** *(list) --*

        A list of names of connections to GitHub accounts.
        - *(string) --*
    """


_ListOnPremisesInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOnPremisesInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListOnPremisesInstancesPaginatePaginationConfigTypeDef(
    _ListOnPremisesInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOnPremisesInstancesPaginateResponseTypeDef = TypedDict(
    "_ListOnPremisesInstancesPaginateResponseTypeDef",
    {"instanceNames": List[str], "NextToken": str},
    total=False,
)


class ListOnPremisesInstancesPaginateResponseTypeDef(
    _ListOnPremisesInstancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of the list on-premises instances operation.
      - **instanceNames** *(list) --*

        The list of matching on-premises instance names.
        - *(string) --*
    """


_ListOnPremisesInstancesPaginateTagFiltersTypeDef = TypedDict(
    "_ListOnPremisesInstancesPaginateTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)


class ListOnPremisesInstancesPaginateTagFiltersTypeDef(
    _ListOnPremisesInstancesPaginateTagFiltersTypeDef
):
    """
    - *(dict) --*

      Information about an on-premises instance tag filter.
      - **Key** *(string) --*

        The on-premises instance tag filter key.
    """
