"Main interface for ecs service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateClusterResponseclustersettingsTypeDef",
    "ClientCreateClusterResponseclusterstatisticsTypeDef",
    "ClientCreateClusterResponseclustertagsTypeDef",
    "ClientCreateClusterResponseclusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterSettingsTypeDef",
    "ClientCreateClusterTagsTypeDef",
    "ClientCreateServiceDeploymentConfigurationTypeDef",
    "ClientCreateServiceDeploymentControllerTypeDef",
    "ClientCreateServiceLoadBalancersTypeDef",
    "ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceNetworkConfigurationTypeDef",
    "ClientCreateServicePlacementConstraintsTypeDef",
    "ClientCreateServicePlacementStrategyTypeDef",
    "ClientCreateServiceResponseservicedeploymentConfigurationTypeDef",
    "ClientCreateServiceResponseservicedeploymentControllerTypeDef",
    "ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    "ClientCreateServiceResponseservicedeploymentsTypeDef",
    "ClientCreateServiceResponseserviceeventsTypeDef",
    "ClientCreateServiceResponseserviceloadBalancersTypeDef",
    "ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceResponseservicenetworkConfigurationTypeDef",
    "ClientCreateServiceResponseserviceplacementConstraintsTypeDef",
    "ClientCreateServiceResponseserviceplacementStrategyTypeDef",
    "ClientCreateServiceResponseserviceserviceRegistriesTypeDef",
    "ClientCreateServiceResponseservicetagsTypeDef",
    "ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef",
    "ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    "ClientCreateServiceResponseservicetaskSetsscaleTypeDef",
    "ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    "ClientCreateServiceResponseservicetaskSetsTypeDef",
    "ClientCreateServiceResponseserviceTypeDef",
    "ClientCreateServiceResponseTypeDef",
    "ClientCreateServiceServiceRegistriesTypeDef",
    "ClientCreateServiceTagsTypeDef",
    "ClientCreateTaskSetLoadBalancersTypeDef",
    "ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateTaskSetNetworkConfigurationTypeDef",
    "ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientCreateTaskSetResponsetaskSetscaleTypeDef",
    "ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientCreateTaskSetResponsetaskSetTypeDef",
    "ClientCreateTaskSetResponseTypeDef",
    "ClientCreateTaskSetScaleTypeDef",
    "ClientCreateTaskSetServiceRegistriesTypeDef",
    "ClientDeleteAccountSettingResponsesettingTypeDef",
    "ClientDeleteAccountSettingResponseTypeDef",
    "ClientDeleteAttributesAttributesTypeDef",
    "ClientDeleteAttributesResponseattributesTypeDef",
    "ClientDeleteAttributesResponseTypeDef",
    "ClientDeleteClusterResponseclustersettingsTypeDef",
    "ClientDeleteClusterResponseclusterstatisticsTypeDef",
    "ClientDeleteClusterResponseclustertagsTypeDef",
    "ClientDeleteClusterResponseclusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef",
    "ClientDeleteServiceResponseservicedeploymentControllerTypeDef",
    "ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    "ClientDeleteServiceResponseservicedeploymentsTypeDef",
    "ClientDeleteServiceResponseserviceeventsTypeDef",
    "ClientDeleteServiceResponseserviceloadBalancersTypeDef",
    "ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteServiceResponseservicenetworkConfigurationTypeDef",
    "ClientDeleteServiceResponseserviceplacementConstraintsTypeDef",
    "ClientDeleteServiceResponseserviceplacementStrategyTypeDef",
    "ClientDeleteServiceResponseserviceserviceRegistriesTypeDef",
    "ClientDeleteServiceResponseservicetagsTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsscaleTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsTypeDef",
    "ClientDeleteServiceResponseserviceTypeDef",
    "ClientDeleteServiceResponseTypeDef",
    "ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientDeleteTaskSetResponsetaskSetscaleTypeDef",
    "ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientDeleteTaskSetResponsetaskSetTypeDef",
    "ClientDeleteTaskSetResponseTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef",
    "ClientDeregisterContainerInstanceResponseTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef",
    "ClientDeregisterTaskDefinitionResponseTypeDef",
    "ClientDescribeClustersResponseclusterssettingsTypeDef",
    "ClientDescribeClustersResponseclustersstatisticsTypeDef",
    "ClientDescribeClustersResponseclusterstagsTypeDef",
    "ClientDescribeClustersResponseclustersTypeDef",
    "ClientDescribeClustersResponsefailuresTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef",
    "ClientDescribeContainerInstancesResponsefailuresTypeDef",
    "ClientDescribeContainerInstancesResponseTypeDef",
    "ClientDescribeServicesResponsefailuresTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentControllerTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentsTypeDef",
    "ClientDescribeServicesResponseserviceseventsTypeDef",
    "ClientDescribeServicesResponseservicesloadBalancersTypeDef",
    "ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesplacementConstraintsTypeDef",
    "ClientDescribeServicesResponseservicesplacementStrategyTypeDef",
    "ClientDescribeServicesResponseservicesserviceRegistriesTypeDef",
    "ClientDescribeServicesResponseservicestagsTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsscaleTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsTypeDef",
    "ClientDescribeServicesResponseservicesTypeDef",
    "ClientDescribeServicesResponseTypeDef",
    "ClientDescribeTaskDefinitionResponsetagsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef",
    "ClientDescribeTaskDefinitionResponseTypeDef",
    "ClientDescribeTaskSetsResponsefailuresTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsTypeDef",
    "ClientDescribeTaskSetsResponseTypeDef",
    "ClientDescribeTasksResponsefailuresTypeDef",
    "ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef",
    "ClientDescribeTasksResponsetasksattachmentsTypeDef",
    "ClientDescribeTasksResponsetasksattributesTypeDef",
    "ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef",
    "ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef",
    "ClientDescribeTasksResponsetaskscontainersTypeDef",
    "ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef",
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef",
    "ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientDescribeTasksResponsetasksoverridesTypeDef",
    "ClientDescribeTasksResponsetaskstagsTypeDef",
    "ClientDescribeTasksResponsetasksTypeDef",
    "ClientDescribeTasksResponseTypeDef",
    "ClientDiscoverPollEndpointResponseTypeDef",
    "ClientListAccountSettingsResponsesettingsTypeDef",
    "ClientListAccountSettingsResponseTypeDef",
    "ClientListAttributesResponseattributesTypeDef",
    "ClientListAttributesResponseTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListContainerInstancesResponseTypeDef",
    "ClientListServicesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTaskDefinitionFamiliesResponseTypeDef",
    "ClientListTaskDefinitionsResponseTypeDef",
    "ClientListTasksResponseTypeDef",
    "ClientPutAccountSettingDefaultResponsesettingTypeDef",
    "ClientPutAccountSettingDefaultResponseTypeDef",
    "ClientPutAccountSettingResponsesettingTypeDef",
    "ClientPutAccountSettingResponseTypeDef",
    "ClientPutAttributesAttributesTypeDef",
    "ClientPutAttributesResponseattributesTypeDef",
    "ClientPutAttributesResponseTypeDef",
    "ClientRegisterContainerInstanceAttributesTypeDef",
    "ClientRegisterContainerInstancePlatformDevicesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef",
    "ClientRegisterContainerInstanceResponseTypeDef",
    "ClientRegisterContainerInstanceTagsTypeDef",
    "ClientRegisterContainerInstanceTotalResourcesTypeDef",
    "ClientRegisterContainerInstanceVersionInfoTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsTypeDef",
    "ClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef",
    "ClientRegisterTaskDefinitionPlacementConstraintsTypeDef",
    "ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef",
    "ClientRegisterTaskDefinitionProxyConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetagsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef",
    "ClientRegisterTaskDefinitionResponseTypeDef",
    "ClientRegisterTaskDefinitionTagsTypeDef",
    "ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef",
    "ClientRegisterTaskDefinitionVolumeshostTypeDef",
    "ClientRegisterTaskDefinitionVolumesTypeDef",
    "ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientRunTaskNetworkConfigurationTypeDef",
    "ClientRunTaskOverridescontainerOverridesenvironmentTypeDef",
    "ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientRunTaskOverridescontainerOverridesTypeDef",
    "ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef",
    "ClientRunTaskOverridesTypeDef",
    "ClientRunTaskPlacementConstraintsTypeDef",
    "ClientRunTaskPlacementStrategyTypeDef",
    "ClientRunTaskResponsefailuresTypeDef",
    "ClientRunTaskResponsetasksattachmentsdetailsTypeDef",
    "ClientRunTaskResponsetasksattachmentsTypeDef",
    "ClientRunTaskResponsetasksattributesTypeDef",
    "ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef",
    "ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    "ClientRunTaskResponsetaskscontainersTypeDef",
    "ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef",
    "ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    "ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef",
    "ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientRunTaskResponsetasksoverridesTypeDef",
    "ClientRunTaskResponsetaskstagsTypeDef",
    "ClientRunTaskResponsetasksTypeDef",
    "ClientRunTaskResponseTypeDef",
    "ClientRunTaskTagsTypeDef",
    "ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientStartTaskNetworkConfigurationTypeDef",
    "ClientStartTaskOverridescontainerOverridesenvironmentTypeDef",
    "ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientStartTaskOverridescontainerOverridesTypeDef",
    "ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef",
    "ClientStartTaskOverridesTypeDef",
    "ClientStartTaskResponsefailuresTypeDef",
    "ClientStartTaskResponsetasksattachmentsdetailsTypeDef",
    "ClientStartTaskResponsetasksattachmentsTypeDef",
    "ClientStartTaskResponsetasksattributesTypeDef",
    "ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef",
    "ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    "ClientStartTaskResponsetaskscontainersTypeDef",
    "ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef",
    "ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    "ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef",
    "ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientStartTaskResponsetasksoverridesTypeDef",
    "ClientStartTaskResponsetaskstagsTypeDef",
    "ClientStartTaskResponsetasksTypeDef",
    "ClientStartTaskResponseTypeDef",
    "ClientStartTaskTagsTypeDef",
    "ClientStopTaskResponsetaskattachmentsdetailsTypeDef",
    "ClientStopTaskResponsetaskattachmentsTypeDef",
    "ClientStopTaskResponsetaskattributesTypeDef",
    "ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef",
    "ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef",
    "ClientStopTaskResponsetaskcontainersTypeDef",
    "ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef",
    "ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef",
    "ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef",
    "ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientStopTaskResponsetaskoverridesTypeDef",
    "ClientStopTaskResponsetasktagsTypeDef",
    "ClientStopTaskResponsetaskTypeDef",
    "ClientStopTaskResponseTypeDef",
    "ClientSubmitAttachmentStateChangesAttachmentsTypeDef",
    "ClientSubmitAttachmentStateChangesResponseTypeDef",
    "ClientSubmitContainerStateChangeNetworkBindingsTypeDef",
    "ClientSubmitContainerStateChangeResponseTypeDef",
    "ClientSubmitTaskStateChangeAttachmentsTypeDef",
    "ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef",
    "ClientSubmitTaskStateChangeContainersTypeDef",
    "ClientSubmitTaskStateChangeResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateClusterSettingsResponseclustersettingsTypeDef",
    "ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef",
    "ClientUpdateClusterSettingsResponseclustertagsTypeDef",
    "ClientUpdateClusterSettingsResponseclusterTypeDef",
    "ClientUpdateClusterSettingsResponseTypeDef",
    "ClientUpdateClusterSettingsSettingsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceTypeDef",
    "ClientUpdateContainerAgentResponseTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef",
    "ClientUpdateContainerInstancesStateResponsefailuresTypeDef",
    "ClientUpdateContainerInstancesStateResponseTypeDef",
    "ClientUpdateServiceDeploymentConfigurationTypeDef",
    "ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceNetworkConfigurationTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponseTypeDef",
    "ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef",
    "ClientUpdateServiceResponseservicedeploymentControllerTypeDef",
    "ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    "ClientUpdateServiceResponseservicedeploymentsTypeDef",
    "ClientUpdateServiceResponseserviceeventsTypeDef",
    "ClientUpdateServiceResponseserviceloadBalancersTypeDef",
    "ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceResponseservicenetworkConfigurationTypeDef",
    "ClientUpdateServiceResponseserviceplacementConstraintsTypeDef",
    "ClientUpdateServiceResponseserviceplacementStrategyTypeDef",
    "ClientUpdateServiceResponseserviceserviceRegistriesTypeDef",
    "ClientUpdateServiceResponseservicetagsTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsscaleTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsTypeDef",
    "ClientUpdateServiceResponseserviceTypeDef",
    "ClientUpdateServiceResponseTypeDef",
    "ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientUpdateTaskSetResponsetaskSetscaleTypeDef",
    "ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientUpdateTaskSetResponsetaskSetTypeDef",
    "ClientUpdateTaskSetResponseTypeDef",
    "ClientUpdateTaskSetScaleTypeDef",
    "ListAccountSettingsPaginatePaginationConfigTypeDef",
    "ListAccountSettingsPaginateResponsesettingsTypeDef",
    "ListAccountSettingsPaginateResponseTypeDef",
    "ListAttributesPaginatePaginationConfigTypeDef",
    "ListAttributesPaginateResponseattributesTypeDef",
    "ListAttributesPaginateResponseTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListContainerInstancesPaginatePaginationConfigTypeDef",
    "ListContainerInstancesPaginateResponseTypeDef",
    "ListServicesPaginatePaginationConfigTypeDef",
    "ListServicesPaginateResponseTypeDef",
    "ListTaskDefinitionFamiliesPaginatePaginationConfigTypeDef",
    "ListTaskDefinitionFamiliesPaginateResponseTypeDef",
    "ListTaskDefinitionsPaginatePaginationConfigTypeDef",
    "ListTaskDefinitionsPaginateResponseTypeDef",
    "ListTasksPaginatePaginationConfigTypeDef",
    "ListTasksPaginateResponseTypeDef",
    "ServicesInactiveWaitWaiterConfigTypeDef",
    "ServicesStableWaitWaiterConfigTypeDef",
    "TasksRunningWaitWaiterConfigTypeDef",
    "TasksStoppedWaitWaiterConfigTypeDef",
)


_ClientCreateClusterResponseclustersettingsTypeDef = TypedDict(
    "_ClientCreateClusterResponseclustersettingsTypeDef", {"name": str, "value": str}, total=False
)


class ClientCreateClusterResponseclustersettingsTypeDef(
    _ClientCreateClusterResponseclustersettingsTypeDef
):
    pass


_ClientCreateClusterResponseclusterstatisticsTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterstatisticsTypeDef", {"name": str, "value": str}, total=False
)


class ClientCreateClusterResponseclusterstatisticsTypeDef(
    _ClientCreateClusterResponseclusterstatisticsTypeDef
):
    pass


_ClientCreateClusterResponseclustertagsTypeDef = TypedDict(
    "_ClientCreateClusterResponseclustertagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateClusterResponseclustertagsTypeDef(_ClientCreateClusterResponseclustertagsTypeDef):
    pass


_ClientCreateClusterResponseclusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientCreateClusterResponseclusterstatisticsTypeDef],
        "tags": List[ClientCreateClusterResponseclustertagsTypeDef],
        "settings": List[ClientCreateClusterResponseclustersettingsTypeDef],
    },
    total=False,
)


class ClientCreateClusterResponseclusterTypeDef(_ClientCreateClusterResponseclusterTypeDef):
    """
    - **cluster** *(dict) --*

      The full description of your new cluster.
      - **clusterArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of the
        cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
        ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef",
    {"cluster": ClientCreateClusterResponseclusterTypeDef},
    total=False,
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    - *(dict) --*

      - **cluster** *(dict) --*

        The full description of your new cluster.
        - **clusterArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
          ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of
          the cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
          ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientCreateClusterSettingsTypeDef = TypedDict(
    "_ClientCreateClusterSettingsTypeDef", {"name": str, "value": str}, total=False
)


class ClientCreateClusterSettingsTypeDef(_ClientCreateClusterSettingsTypeDef):
    """
    - *(dict) --*

      The settings to use when creating a cluster. This parameter is used to enable CloudWatch
      Container Insights for a cluster.
      - **name** *(string) --*

        The name of the cluster setting. The only supported value is ``containerInsights`` .
    """


_ClientCreateClusterTagsTypeDef = TypedDict(
    "_ClientCreateClusterTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateClusterTagsTypeDef(_ClientCreateClusterTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientCreateServiceDeploymentConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceDeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)


class ClientCreateServiceDeploymentConfigurationTypeDef(
    _ClientCreateServiceDeploymentConfigurationTypeDef
):
    """
    Optional deployment parameters that control how many tasks run during the deployment and the
    ordering of stopping and starting tasks.
    - **maximumPercent** *(integer) --*

      If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent**
      parameter represents an upper limit on the number of tasks in a service that are allowed in
      the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired
      number of tasks (rounded down to the nearest integer), and while any container instances are
      in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This
      parameter enables you to define the deployment batch size. For example, if your service has a
      desired number of four tasks and a maximum percent value of 200%, the scheduler may start four
      new tasks before stopping the four older tasks (provided that the cluster resources required
      to do this are available). The default value for maximum percent is 200%.
      If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and
      tasks that use the EC2 launch type, the **maximum percent** value is set to the default value
      and is used to define the upper limit on the number of the tasks in the service that remain in
      the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the
      tasks in the service use the Fargate launch type, the maximum percent value is not used,
      although it is returned when describing your service.
    """


_ClientCreateServiceDeploymentControllerTypeDef = TypedDict(
    "_ClientCreateServiceDeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
)


class ClientCreateServiceDeploymentControllerTypeDef(
    _ClientCreateServiceDeploymentControllerTypeDef
):
    """
    The deployment controller to use for the service.
    - **type** *(string) --***[REQUIRED]**

      The deployment controller type to use.
      There are three deployment controller types available:

        ECS
    """


_ClientCreateServiceLoadBalancersTypeDef = TypedDict(
    "_ClientCreateServiceLoadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateServiceLoadBalancersTypeDef(_ClientCreateServiceLoadBalancersTypeDef):
    """
    - *(dict) --*

      Details on the load balancer or load balancers to use with a service or task set.
      - **targetGroupArn** *(string) --*

        The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups
        associated with a service or task set.
        A target group ARN is only specified when using an Application Load Balancer or Network Load
        Balancer. If you are using a Classic Load Balancer this should be omitted.
        For services using the ``ECS`` deployment controller, you can specify one or multiple target
        groups. For more information, see `Registering Multiple Target Groups with a Service
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html>`__
        in the *Amazon Elastic Container Service Developer Guide* .
        For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two
        target groups for the load balancer. For more information, see `Blue/Green Deployment with
        CodeDeploy
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html>`__
        in the *Amazon Elastic Container Service Developer Guide* .
        .. warning::

          If your service's task definition uses the ``awsvpc`` network mode (which is required for
          the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` ,
          when creating your target groups because tasks that use the ``awsvpc`` network mode are
          associated with an elastic network interface, not an Amazon EC2 instance.
    """


_ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef
):
    """
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientCreateServiceNetworkConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)


class ClientCreateServiceNetworkConfigurationTypeDef(
    _ClientCreateServiceNetworkConfigurationTypeDef
):
    """
    The network configuration for the service. This parameter is required for task definitions that
    use the ``awsvpc`` network mode to receive their own elastic network interface, and it is not
    supported for other network modes. For more information, see `Task Networking
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the
    *Amazon Elastic Container Service Developer Guide* .
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientCreateServicePlacementConstraintsTypeDef = TypedDict(
    "_ClientCreateServicePlacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)


class ClientCreateServicePlacementConstraintsTypeDef(
    _ClientCreateServicePlacementConstraintsTypeDef
):
    """
    - *(dict) --*

      An object representing a constraint on task placement. For more information, see `Task
      Placement Constraints
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      .. note::

        If you are using the Fargate launch type, task placement constraints are not supported.
    """


_ClientCreateServicePlacementStrategyTypeDef = TypedDict(
    "_ClientCreateServicePlacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)


class ClientCreateServicePlacementStrategyTypeDef(_ClientCreateServicePlacementStrategyTypeDef):
    """
    - *(dict) --*

      The task placement strategy for a task or service. For more information, see `Task Placement
      Strategies
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **type** *(string) --*

        The type of placement strategy. The ``random`` placement strategy randomly places tasks on
        available candidates. The ``spread`` placement strategy spreads placement across available
        candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on
        available candidates that have the least available amount of the resource that is specified
        with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the
        instance with the least amount of remaining memory (but still enough to run the task).
    """


_ClientCreateServiceResponseservicedeploymentConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicedeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)


class ClientCreateServiceResponseservicedeploymentConfigurationTypeDef(
    _ClientCreateServiceResponseservicedeploymentConfigurationTypeDef
):
    pass


_ClientCreateServiceResponseservicedeploymentControllerTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicedeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)


class ClientCreateServiceResponseservicedeploymentControllerTypeDef(
    _ClientCreateServiceResponseservicedeploymentControllerTypeDef
):
    pass


_ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef(
    _ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef
):
    pass


_ClientCreateServiceResponseservicedeploymentsTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicedeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateServiceResponseservicedeploymentsTypeDef(
    _ClientCreateServiceResponseservicedeploymentsTypeDef
):
    pass


_ClientCreateServiceResponseserviceeventsTypeDef = TypedDict(
    "_ClientCreateServiceResponseserviceeventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)


class ClientCreateServiceResponseserviceeventsTypeDef(
    _ClientCreateServiceResponseserviceeventsTypeDef
):
    pass


_ClientCreateServiceResponseserviceloadBalancersTypeDef = TypedDict(
    "_ClientCreateServiceResponseserviceloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateServiceResponseserviceloadBalancersTypeDef(
    _ClientCreateServiceResponseserviceloadBalancersTypeDef
):
    pass


_ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientCreateServiceResponseservicenetworkConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicenetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientCreateServiceResponseservicenetworkConfigurationTypeDef(
    _ClientCreateServiceResponseservicenetworkConfigurationTypeDef
):
    pass


_ClientCreateServiceResponseserviceplacementConstraintsTypeDef = TypedDict(
    "_ClientCreateServiceResponseserviceplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)


class ClientCreateServiceResponseserviceplacementConstraintsTypeDef(
    _ClientCreateServiceResponseserviceplacementConstraintsTypeDef
):
    pass


_ClientCreateServiceResponseserviceplacementStrategyTypeDef = TypedDict(
    "_ClientCreateServiceResponseserviceplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)


class ClientCreateServiceResponseserviceplacementStrategyTypeDef(
    _ClientCreateServiceResponseserviceplacementStrategyTypeDef
):
    pass


_ClientCreateServiceResponseserviceserviceRegistriesTypeDef = TypedDict(
    "_ClientCreateServiceResponseserviceserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateServiceResponseserviceserviceRegistriesTypeDef(
    _ClientCreateServiceResponseserviceserviceRegistriesTypeDef
):
    pass


_ClientCreateServiceResponseservicetagsTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateServiceResponseservicetagsTypeDef(_ClientCreateServiceResponseservicetagsTypeDef):
    pass


_ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef(
    _ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef
):
    pass


_ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef(
    _ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef
):
    pass


_ClientCreateServiceResponseservicetaskSetsscaleTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicetaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)


class ClientCreateServiceResponseservicetaskSetsscaleTypeDef(
    _ClientCreateServiceResponseservicetaskSetsscaleTypeDef
):
    pass


_ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef(
    _ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef
):
    pass


_ClientCreateServiceResponseservicetaskSetsTypeDef = TypedDict(
    "_ClientCreateServiceResponseservicetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientCreateServiceResponseservicetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientCreateServiceResponseservicetaskSetsTypeDef(
    _ClientCreateServiceResponseservicetaskSetsTypeDef
):
    pass


_ClientCreateServiceResponseserviceTypeDef = TypedDict(
    "_ClientCreateServiceResponseserviceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientCreateServiceResponseserviceloadBalancersTypeDef],
        "serviceRegistries": List[ClientCreateServiceResponseserviceserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientCreateServiceResponseservicedeploymentConfigurationTypeDef,
        "taskSets": List[ClientCreateServiceResponseservicetaskSetsTypeDef],
        "deployments": List[ClientCreateServiceResponseservicedeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientCreateServiceResponseserviceeventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[ClientCreateServiceResponseserviceplacementConstraintsTypeDef],
        "placementStrategy": List[ClientCreateServiceResponseserviceplacementStrategyTypeDef],
        "networkConfiguration": ClientCreateServiceResponseservicenetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientCreateServiceResponseservicedeploymentControllerTypeDef,
        "tags": List[ClientCreateServiceResponseservicetagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)


class ClientCreateServiceResponseserviceTypeDef(_ClientCreateServiceResponseserviceTypeDef):
    """
    - **service** *(dict) --*

      The full description of your service following the create call.
      If a service is using the ``ECS`` deployment controller, the ``deploymentController`` and
      ``taskSets`` parameters will not be returned.
      If the service is using the ``CODE_DEPLOY`` deployment controller, the
      ``deploymentController`` , ``taskSets`` and ``deployments`` parameters will be returned,
      however the ``deployments`` parameter will be an empty list.
      - **serviceArn** *(string) --*

        The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
        followed by the Region of the service, the AWS account ID of the service owner, the
        ``service`` namespace, and then the service name. For example,
        ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientCreateServiceResponseTypeDef = TypedDict(
    "_ClientCreateServiceResponseTypeDef",
    {"service": ClientCreateServiceResponseserviceTypeDef},
    total=False,
)


class ClientCreateServiceResponseTypeDef(_ClientCreateServiceResponseTypeDef):
    """
    - *(dict) --*

      - **service** *(dict) --*

        The full description of your service following the create call.
        If a service is using the ``ECS`` deployment controller, the ``deploymentController`` and
        ``taskSets`` parameters will not be returned.
        If the service is using the ``CODE_DEPLOY`` deployment controller, the
        ``deploymentController`` , ``taskSets`` and ``deployments`` parameters will be returned,
        however the ``deployments`` parameter will be an empty list.
        - **serviceArn** *(string) --*

          The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
          followed by the Region of the service, the AWS account ID of the service owner, the
          ``service`` namespace, and then the service name. For example,
          ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientCreateServiceServiceRegistriesTypeDef = TypedDict(
    "_ClientCreateServiceServiceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateServiceServiceRegistriesTypeDef(_ClientCreateServiceServiceRegistriesTypeDef):
    pass


_ClientCreateServiceTagsTypeDef = TypedDict(
    "_ClientCreateServiceTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateServiceTagsTypeDef(_ClientCreateServiceTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientCreateTaskSetLoadBalancersTypeDef = TypedDict(
    "_ClientCreateTaskSetLoadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateTaskSetLoadBalancersTypeDef(_ClientCreateTaskSetLoadBalancersTypeDef):
    """
    - *(dict) --*

      Details on the load balancer or load balancers to use with a service or task set.
      - **targetGroupArn** *(string) --*

        The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups
        associated with a service or task set.
        A target group ARN is only specified when using an Application Load Balancer or Network Load
        Balancer. If you are using a Classic Load Balancer this should be omitted.
        For services using the ``ECS`` deployment controller, you can specify one or multiple target
        groups. For more information, see `Registering Multiple Target Groups with a Service
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html>`__
        in the *Amazon Elastic Container Service Developer Guide* .
        For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two
        target groups for the load balancer. For more information, see `Blue/Green Deployment with
        CodeDeploy
        <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html>`__
        in the *Amazon Elastic Container Service Developer Guide* .
        .. warning::

          If your service's task definition uses the ``awsvpc`` network mode (which is required for
          the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` ,
          when creating your target groups because tasks that use the ``awsvpc`` network mode are
          associated with an elastic network interface, not an Amazon EC2 instance.
    """


_ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef
):
    """
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientCreateTaskSetNetworkConfigurationTypeDef = TypedDict(
    "_ClientCreateTaskSetNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)


class ClientCreateTaskSetNetworkConfigurationTypeDef(
    _ClientCreateTaskSetNetworkConfigurationTypeDef
):
    """
    An object representing the network configuration for a task or service.
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "_ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef(
    _ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef
):
    pass


_ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "_ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef(
    _ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef
):
    pass


_ClientCreateTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "_ClientCreateTaskSetResponsetaskSetscaleTypeDef", {"value": float, "unit": str}, total=False
)


class ClientCreateTaskSetResponsetaskSetscaleTypeDef(
    _ClientCreateTaskSetResponsetaskSetscaleTypeDef
):
    pass


_ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "_ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef(
    _ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef
):
    pass


_ClientCreateTaskSetResponsetaskSetTypeDef = TypedDict(
    "_ClientCreateTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef],
        "scale": ClientCreateTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientCreateTaskSetResponsetaskSetTypeDef(_ClientCreateTaskSetResponsetaskSetTypeDef):
    """
    - **taskSet** *(dict) --*

      Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
      deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
      many tasks are running, and whether the task set serves production traffic.
      - **id** *(string) --*

        The ID of the task set.
    """


_ClientCreateTaskSetResponseTypeDef = TypedDict(
    "_ClientCreateTaskSetResponseTypeDef",
    {"taskSet": ClientCreateTaskSetResponsetaskSetTypeDef},
    total=False,
)


class ClientCreateTaskSetResponseTypeDef(_ClientCreateTaskSetResponseTypeDef):
    """
    - *(dict) --*

      - **taskSet** *(dict) --*

        Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
        deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
        many tasks are running, and whether the task set serves production traffic.
        - **id** *(string) --*

          The ID of the task set.
    """


_ClientCreateTaskSetScaleTypeDef = TypedDict(
    "_ClientCreateTaskSetScaleTypeDef", {"value": float, "unit": str}, total=False
)


class ClientCreateTaskSetScaleTypeDef(_ClientCreateTaskSetScaleTypeDef):
    """
    A floating-point percentage of the desired number of tasks to place and keep running in the task
    set.
    - **value** *(float) --*

      The value, specified as a percent total of a service's ``desiredCount`` , to scale the task
      set. Accepted values are numbers between 0 and 100.
    """


_ClientCreateTaskSetServiceRegistriesTypeDef = TypedDict(
    "_ClientCreateTaskSetServiceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientCreateTaskSetServiceRegistriesTypeDef(_ClientCreateTaskSetServiceRegistriesTypeDef):
    """
    - *(dict) --*

      Details of the service registry.
      - **registryArn** *(string) --*

        The Amazon Resource Name (ARN) of the service registry. The currently supported service
        registry is AWS Cloud Map. For more information, see `CreateService
        <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
    """


_ClientDeleteAccountSettingResponsesettingTypeDef = TypedDict(
    "_ClientDeleteAccountSettingResponsesettingTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)


class ClientDeleteAccountSettingResponsesettingTypeDef(
    _ClientDeleteAccountSettingResponsesettingTypeDef
):
    """
    - **setting** *(dict) --*

      The account setting for the specified principal ARN.
      - **name** *(string) --*

        The Amazon ECS resource name.
    """


_ClientDeleteAccountSettingResponseTypeDef = TypedDict(
    "_ClientDeleteAccountSettingResponseTypeDef",
    {"setting": ClientDeleteAccountSettingResponsesettingTypeDef},
    total=False,
)


class ClientDeleteAccountSettingResponseTypeDef(_ClientDeleteAccountSettingResponseTypeDef):
    """
    - *(dict) --*

      - **setting** *(dict) --*

        The account setting for the specified principal ARN.
        - **name** *(string) --*

          The Amazon ECS resource name.
    """


_RequiredClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientDeleteAttributesAttributesTypeDef", {"name": str}
)
_OptionalClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientDeleteAttributesAttributesTypeDef",
    {"value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDeleteAttributesAttributesTypeDef(
    _RequiredClientDeleteAttributesAttributesTypeDef,
    _OptionalClientDeleteAttributesAttributesTypeDef,
):
    """
    - *(dict) --*

      An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you
      to extend the Amazon ECS data model by adding custom metadata to your resources. For more
      information, see `Attributes
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **name** *(string) --***[REQUIRED]**

        The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens,
        underscores, and periods are allowed.
    """


_ClientDeleteAttributesResponseattributesTypeDef = TypedDict(
    "_ClientDeleteAttributesResponseattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDeleteAttributesResponseattributesTypeDef(
    _ClientDeleteAttributesResponseattributesTypeDef
):
    """
    - *(dict) --*

      An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you
      to extend the Amazon ECS data model by adding custom metadata to your resources. For more
      information, see `Attributes
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **name** *(string) --*

        The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens,
        underscores, and periods are allowed.
    """


_ClientDeleteAttributesResponseTypeDef = TypedDict(
    "_ClientDeleteAttributesResponseTypeDef",
    {"attributes": List[ClientDeleteAttributesResponseattributesTypeDef]},
    total=False,
)


class ClientDeleteAttributesResponseTypeDef(_ClientDeleteAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **attributes** *(list) --*

        A list of attribute objects that were successfully deleted from your resource.
        - *(dict) --*

          An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable
          you to extend the Amazon ECS data model by adding custom metadata to your resources. For
          more information, see `Attributes
          <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
          in the *Amazon Elastic Container Service Developer Guide* .
          - **name** *(string) --*

            The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers,
            hyphens, underscores, and periods are allowed.
    """


_ClientDeleteClusterResponseclustersettingsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclustersettingsTypeDef", {"name": str, "value": str}, total=False
)


class ClientDeleteClusterResponseclustersettingsTypeDef(
    _ClientDeleteClusterResponseclustersettingsTypeDef
):
    pass


_ClientDeleteClusterResponseclusterstatisticsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterstatisticsTypeDef", {"name": str, "value": str}, total=False
)


class ClientDeleteClusterResponseclusterstatisticsTypeDef(
    _ClientDeleteClusterResponseclusterstatisticsTypeDef
):
    pass


_ClientDeleteClusterResponseclustertagsTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclustertagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDeleteClusterResponseclustertagsTypeDef(_ClientDeleteClusterResponseclustertagsTypeDef):
    pass


_ClientDeleteClusterResponseclusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientDeleteClusterResponseclusterstatisticsTypeDef],
        "tags": List[ClientDeleteClusterResponseclustertagsTypeDef],
        "settings": List[ClientDeleteClusterResponseclustersettingsTypeDef],
    },
    total=False,
)


class ClientDeleteClusterResponseclusterTypeDef(_ClientDeleteClusterResponseclusterTypeDef):
    """
    - **cluster** *(dict) --*

      The full description of the deleted cluster.
      - **clusterArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of the
        cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
        ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientDeleteClusterResponseTypeDef = TypedDict(
    "_ClientDeleteClusterResponseTypeDef",
    {"cluster": ClientDeleteClusterResponseclusterTypeDef},
    total=False,
)


class ClientDeleteClusterResponseTypeDef(_ClientDeleteClusterResponseTypeDef):
    """
    - *(dict) --*

      - **cluster** *(dict) --*

        The full description of the deleted cluster.
        - **clusterArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
          ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of
          the cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
          ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)


class ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef(
    _ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef
):
    pass


_ClientDeleteServiceResponseservicedeploymentControllerTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicedeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)


class ClientDeleteServiceResponseservicedeploymentControllerTypeDef(
    _ClientDeleteServiceResponseservicedeploymentControllerTypeDef
):
    pass


_ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef(
    _ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef
):
    pass


_ClientDeleteServiceResponseservicedeploymentsTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicedeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)


class ClientDeleteServiceResponseservicedeploymentsTypeDef(
    _ClientDeleteServiceResponseservicedeploymentsTypeDef
):
    pass


_ClientDeleteServiceResponseserviceeventsTypeDef = TypedDict(
    "_ClientDeleteServiceResponseserviceeventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)


class ClientDeleteServiceResponseserviceeventsTypeDef(
    _ClientDeleteServiceResponseserviceeventsTypeDef
):
    pass


_ClientDeleteServiceResponseserviceloadBalancersTypeDef = TypedDict(
    "_ClientDeleteServiceResponseserviceloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDeleteServiceResponseserviceloadBalancersTypeDef(
    _ClientDeleteServiceResponseserviceloadBalancersTypeDef
):
    pass


_ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDeleteServiceResponseservicenetworkConfigurationTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicenetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDeleteServiceResponseservicenetworkConfigurationTypeDef(
    _ClientDeleteServiceResponseservicenetworkConfigurationTypeDef
):
    pass


_ClientDeleteServiceResponseserviceplacementConstraintsTypeDef = TypedDict(
    "_ClientDeleteServiceResponseserviceplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)


class ClientDeleteServiceResponseserviceplacementConstraintsTypeDef(
    _ClientDeleteServiceResponseserviceplacementConstraintsTypeDef
):
    pass


_ClientDeleteServiceResponseserviceplacementStrategyTypeDef = TypedDict(
    "_ClientDeleteServiceResponseserviceplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)


class ClientDeleteServiceResponseserviceplacementStrategyTypeDef(
    _ClientDeleteServiceResponseserviceplacementStrategyTypeDef
):
    pass


_ClientDeleteServiceResponseserviceserviceRegistriesTypeDef = TypedDict(
    "_ClientDeleteServiceResponseserviceserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDeleteServiceResponseserviceserviceRegistriesTypeDef(
    _ClientDeleteServiceResponseserviceserviceRegistriesTypeDef
):
    pass


_ClientDeleteServiceResponseservicetagsTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDeleteServiceResponseservicetagsTypeDef(_ClientDeleteServiceResponseservicetagsTypeDef):
    pass


_ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef(
    _ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef
):
    pass


_ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef(
    _ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef
):
    pass


_ClientDeleteServiceResponseservicetaskSetsscaleTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicetaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)


class ClientDeleteServiceResponseservicetaskSetsscaleTypeDef(
    _ClientDeleteServiceResponseservicetaskSetsscaleTypeDef
):
    pass


_ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef(
    _ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef
):
    pass


_ClientDeleteServiceResponseservicetaskSetsTypeDef = TypedDict(
    "_ClientDeleteServiceResponseservicetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientDeleteServiceResponseservicetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientDeleteServiceResponseservicetaskSetsTypeDef(
    _ClientDeleteServiceResponseservicetaskSetsTypeDef
):
    pass


_ClientDeleteServiceResponseserviceTypeDef = TypedDict(
    "_ClientDeleteServiceResponseserviceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientDeleteServiceResponseserviceloadBalancersTypeDef],
        "serviceRegistries": List[ClientDeleteServiceResponseserviceserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef,
        "taskSets": List[ClientDeleteServiceResponseservicetaskSetsTypeDef],
        "deployments": List[ClientDeleteServiceResponseservicedeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientDeleteServiceResponseserviceeventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[ClientDeleteServiceResponseserviceplacementConstraintsTypeDef],
        "placementStrategy": List[ClientDeleteServiceResponseserviceplacementStrategyTypeDef],
        "networkConfiguration": ClientDeleteServiceResponseservicenetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientDeleteServiceResponseservicedeploymentControllerTypeDef,
        "tags": List[ClientDeleteServiceResponseservicetagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)


class ClientDeleteServiceResponseserviceTypeDef(_ClientDeleteServiceResponseserviceTypeDef):
    """
    - **service** *(dict) --*

      The full description of the deleted service.
      - **serviceArn** *(string) --*

        The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
        followed by the Region of the service, the AWS account ID of the service owner, the
        ``service`` namespace, and then the service name. For example,
        ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientDeleteServiceResponseTypeDef = TypedDict(
    "_ClientDeleteServiceResponseTypeDef",
    {"service": ClientDeleteServiceResponseserviceTypeDef},
    total=False,
)


class ClientDeleteServiceResponseTypeDef(_ClientDeleteServiceResponseTypeDef):
    """
    - *(dict) --*

      - **service** *(dict) --*

        The full description of the deleted service.
        - **serviceArn** *(string) --*

          The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
          followed by the Region of the service, the AWS account ID of the service owner, the
          ``service`` namespace, and then the service name. For example,
          ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "_ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef(
    _ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef
):
    pass


_ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "_ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef(
    _ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef
):
    pass


_ClientDeleteTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "_ClientDeleteTaskSetResponsetaskSetscaleTypeDef", {"value": float, "unit": str}, total=False
)


class ClientDeleteTaskSetResponsetaskSetscaleTypeDef(
    _ClientDeleteTaskSetResponsetaskSetscaleTypeDef
):
    pass


_ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "_ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef(
    _ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef
):
    pass


_ClientDeleteTaskSetResponsetaskSetTypeDef = TypedDict(
    "_ClientDeleteTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef],
        "scale": ClientDeleteTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientDeleteTaskSetResponsetaskSetTypeDef(_ClientDeleteTaskSetResponsetaskSetTypeDef):
    """
    - **taskSet** *(dict) --*

      Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
      deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
      many tasks are running, and whether the task set serves production traffic.
      - **id** *(string) --*

        The ID of the task set.
    """


_ClientDeleteTaskSetResponseTypeDef = TypedDict(
    "_ClientDeleteTaskSetResponseTypeDef",
    {"taskSet": ClientDeleteTaskSetResponsetaskSetTypeDef},
    total=False,
)


class ClientDeleteTaskSetResponseTypeDef(_ClientDeleteTaskSetResponseTypeDef):
    """
    - *(dict) --*

      - **taskSet** *(dict) --*

        Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
        deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
        many tasks are running, and whether the task set serves production traffic.
        - **id** *(string) --*

          The ID of the task set.
    """


_ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef
):
    pass


_ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef
        ],
    },
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef
):
    pass


_ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef
):
    pass


_ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef
):
    pass


_ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef
):
    pass


_ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef
):
    pass


_ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef
):
    pass


_ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "version": int,
        "versionInfo": ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef,
        "remainingResources": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef
        ],
        "tags": List[ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef],
    },
    total=False,
)


class ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef(
    _ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef
):
    """
    - **containerInstance** *(dict) --*

      The container instance that was deregistered.
      - **containerInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the container instance. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account
        ID of the container instance owner, the ``container-instance`` namespace, and then the
        container instance ID. For example,
        ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientDeregisterContainerInstanceResponseTypeDef = TypedDict(
    "_ClientDeregisterContainerInstanceResponseTypeDef",
    {"containerInstance": ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef},
    total=False,
)


class ClientDeregisterContainerInstanceResponseTypeDef(
    _ClientDeregisterContainerInstanceResponseTypeDef
):
    """
    - *(dict) --*

      - **containerInstance** *(dict) --*

        The container instance that was deregistered.
        - **containerInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the container instance. The ARN contains the
          ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS
          account ID of the container instance owner, the ``container-instance`` namespace, and then
          the container instance ID. For example,
          ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
        ],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
        ],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
        ],
        "volumesFrom": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
        ],
        "linuxParameters": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef,
        "secrets": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
        ],
        "dependsOn": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
        ],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
        ],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
        ],
        "logConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    {
        "name": str,
        "host": ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef,
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef
):
    pass


_ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
        ],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": Literal["bridge", "host", "awsvpc", "none"],
        "revision": int,
        "volumes": List[ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef],
        "status": Literal["ACTIVE", "INACTIVE"],
        "requiresAttributes": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
        ],
        "placementConstraints": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
        ],
        "compatibilities": List[Literal["EC2", "FARGATE"]],
        "requiresCompatibilities": List[Literal["EC2", "FARGATE"]],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
        ],
        "pidMode": Literal["host", "task"],
        "ipcMode": Literal["host", "task", "none"],
        "proxyConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef,
    },
    total=False,
)


class ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef(
    _ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef
):
    """
    - **taskDefinition** *(dict) --*

      The full description of the deregistered task.
      - **taskDefinitionArn** *(string) --*

        The full Amazon Resource Name (ARN) of the task definition.
    """


_ClientDeregisterTaskDefinitionResponseTypeDef = TypedDict(
    "_ClientDeregisterTaskDefinitionResponseTypeDef",
    {"taskDefinition": ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef},
    total=False,
)


class ClientDeregisterTaskDefinitionResponseTypeDef(_ClientDeregisterTaskDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **taskDefinition** *(dict) --*

        The full description of the deregistered task.
        - **taskDefinitionArn** *(string) --*

          The full Amazon Resource Name (ARN) of the task definition.
    """


_ClientDescribeClustersResponseclusterssettingsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseclusterssettingsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeClustersResponseclusterssettingsTypeDef(
    _ClientDescribeClustersResponseclusterssettingsTypeDef
):
    pass


_ClientDescribeClustersResponseclustersstatisticsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseclustersstatisticsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeClustersResponseclustersstatisticsTypeDef(
    _ClientDescribeClustersResponseclustersstatisticsTypeDef
):
    pass


_ClientDescribeClustersResponseclusterstagsTypeDef = TypedDict(
    "_ClientDescribeClustersResponseclusterstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDescribeClustersResponseclusterstagsTypeDef(
    _ClientDescribeClustersResponseclusterstagsTypeDef
):
    pass


_ClientDescribeClustersResponseclustersTypeDef = TypedDict(
    "_ClientDescribeClustersResponseclustersTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientDescribeClustersResponseclustersstatisticsTypeDef],
        "tags": List[ClientDescribeClustersResponseclusterstagsTypeDef],
        "settings": List[ClientDescribeClustersResponseclusterssettingsTypeDef],
    },
    total=False,
)


class ClientDescribeClustersResponseclustersTypeDef(_ClientDescribeClustersResponseclustersTypeDef):
    """
    - *(dict) --*

      A regional grouping of one or more container instances on which you can run task requests.
      Each account receives a default cluster the first time you use the Amazon ECS service, but you
      may also create other clusters. Clusters may contain more than one instance type
      simultaneously.
      - **clusterArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of the
        cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
        ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientDescribeClustersResponsefailuresTypeDef = TypedDict(
    "_ClientDescribeClustersResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)


class ClientDescribeClustersResponsefailuresTypeDef(_ClientDescribeClustersResponsefailuresTypeDef):
    pass


_ClientDescribeClustersResponseTypeDef = TypedDict(
    "_ClientDescribeClustersResponseTypeDef",
    {
        "clusters": List[ClientDescribeClustersResponseclustersTypeDef],
        "failures": List[ClientDescribeClustersResponsefailuresTypeDef],
    },
    total=False,
)


class ClientDescribeClustersResponseTypeDef(_ClientDescribeClustersResponseTypeDef):
    """
    - *(dict) --*

      - **clusters** *(list) --*

        The list of clusters.
        - *(dict) --*

          A regional grouping of one or more container instances on which you can run task requests.
          Each account receives a default cluster the first time you use the Amazon ECS service, but
          you may also create other clusters. Clusters may contain more than one instance type
          simultaneously.
          - **clusterArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
            ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of
            the cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
            ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef
):
    pass


_ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef
):
    pass


_ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef
):
    pass


_ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef
):
    pass


_ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef
):
    pass


_ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef
):
    pass


_ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef
):
    pass


_ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "version": int,
        "versionInfo": ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef,
        "remainingResources": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef
        ],
        "tags": List[ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef],
    },
    total=False,
)


class ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef(
    _ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef
):
    """
    - *(dict) --*

      An EC2 instance that is running the Amazon ECS agent and has been registered with a cluster.
      - **containerInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the container instance. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account
        ID of the container instance owner, the ``container-instance`` namespace, and then the
        container instance ID. For example,
        ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientDescribeContainerInstancesResponsefailuresTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)


class ClientDescribeContainerInstancesResponsefailuresTypeDef(
    _ClientDescribeContainerInstancesResponsefailuresTypeDef
):
    pass


_ClientDescribeContainerInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeContainerInstancesResponseTypeDef",
    {
        "containerInstances": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef
        ],
        "failures": List[ClientDescribeContainerInstancesResponsefailuresTypeDef],
    },
    total=False,
)


class ClientDescribeContainerInstancesResponseTypeDef(
    _ClientDescribeContainerInstancesResponseTypeDef
):
    """
    - *(dict) --*

      - **containerInstances** *(list) --*

        The list of container instances.
        - *(dict) --*

          An EC2 instance that is running the Amazon ECS agent and has been registered with a
          cluster.
          - **containerInstanceArn** *(string) --*

            The Amazon Resource Name (ARN) of the container instance. The ARN contains the
            ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS
            account ID of the container instance owner, the ``container-instance`` namespace, and
            then the container instance ID. For example,
            ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientDescribeServicesResponsefailuresTypeDef = TypedDict(
    "_ClientDescribeServicesResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)


class ClientDescribeServicesResponsefailuresTypeDef(_ClientDescribeServicesResponsefailuresTypeDef):
    pass


_ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)


class ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef(
    _ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef
):
    pass


_ClientDescribeServicesResponseservicesdeploymentControllerTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesdeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)


class ClientDescribeServicesResponseservicesdeploymentControllerTypeDef(
    _ClientDescribeServicesResponseservicesdeploymentControllerTypeDef
):
    pass


_ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef(
    _ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef
):
    pass


_ClientDescribeServicesResponseservicesdeploymentsTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesdeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeServicesResponseservicesdeploymentsTypeDef(
    _ClientDescribeServicesResponseservicesdeploymentsTypeDef
):
    pass


_ClientDescribeServicesResponseserviceseventsTypeDef = TypedDict(
    "_ClientDescribeServicesResponseserviceseventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)


class ClientDescribeServicesResponseserviceseventsTypeDef(
    _ClientDescribeServicesResponseserviceseventsTypeDef
):
    pass


_ClientDescribeServicesResponseservicesloadBalancersTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDescribeServicesResponseservicesloadBalancersTypeDef(
    _ClientDescribeServicesResponseservicesloadBalancersTypeDef
):
    pass


_ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef(
    _ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef
):
    pass


_ClientDescribeServicesResponseservicesplacementConstraintsTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)


class ClientDescribeServicesResponseservicesplacementConstraintsTypeDef(
    _ClientDescribeServicesResponseservicesplacementConstraintsTypeDef
):
    pass


_ClientDescribeServicesResponseservicesplacementStrategyTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)


class ClientDescribeServicesResponseservicesplacementStrategyTypeDef(
    _ClientDescribeServicesResponseservicesplacementStrategyTypeDef
):
    pass


_ClientDescribeServicesResponseservicesserviceRegistriesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDescribeServicesResponseservicesserviceRegistriesTypeDef(
    _ClientDescribeServicesResponseservicesserviceRegistriesTypeDef
):
    pass


_ClientDescribeServicesResponseservicestagsTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicestagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDescribeServicesResponseservicestagsTypeDef(
    _ClientDescribeServicesResponseservicestagsTypeDef
):
    pass


_ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef(
    _ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef
):
    pass


_ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef(
    _ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef
):
    pass


_ClientDescribeServicesResponseservicestaskSetsscaleTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicestaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)


class ClientDescribeServicesResponseservicestaskSetsscaleTypeDef(
    _ClientDescribeServicesResponseservicestaskSetsscaleTypeDef
):
    pass


_ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef(
    _ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef
):
    pass


_ClientDescribeServicesResponseservicestaskSetsTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicestaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientDescribeServicesResponseservicestaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientDescribeServicesResponseservicestaskSetsTypeDef(
    _ClientDescribeServicesResponseservicestaskSetsTypeDef
):
    pass


_ClientDescribeServicesResponseservicesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseservicesTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientDescribeServicesResponseservicesloadBalancersTypeDef],
        "serviceRegistries": List[ClientDescribeServicesResponseservicesserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef,
        "taskSets": List[ClientDescribeServicesResponseservicestaskSetsTypeDef],
        "deployments": List[ClientDescribeServicesResponseservicesdeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientDescribeServicesResponseserviceseventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[
            ClientDescribeServicesResponseservicesplacementConstraintsTypeDef
        ],
        "placementStrategy": List[ClientDescribeServicesResponseservicesplacementStrategyTypeDef],
        "networkConfiguration": ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientDescribeServicesResponseservicesdeploymentControllerTypeDef,
        "tags": List[ClientDescribeServicesResponseservicestagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)


class ClientDescribeServicesResponseservicesTypeDef(_ClientDescribeServicesResponseservicesTypeDef):
    """
    - *(dict) --*

      Details on a service within a cluster
      - **serviceArn** *(string) --*

        The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
        followed by the Region of the service, the AWS account ID of the service owner, the
        ``service`` namespace, and then the service name. For example,
        ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientDescribeServicesResponseTypeDef = TypedDict(
    "_ClientDescribeServicesResponseTypeDef",
    {
        "services": List[ClientDescribeServicesResponseservicesTypeDef],
        "failures": List[ClientDescribeServicesResponsefailuresTypeDef],
    },
    total=False,
)


class ClientDescribeServicesResponseTypeDef(_ClientDescribeServicesResponseTypeDef):
    """
    - *(dict) --*

      - **services** *(list) --*

        The list of services described.
        - *(dict) --*

          Details on a service within a cluster
          - **serviceArn** *(string) --*

            The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
            followed by the Region of the service, the AWS account ID of the service owner, the
            ``service`` namespace, and then the service name. For example,
            ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientDescribeTaskDefinitionResponsetagsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDescribeTaskDefinitionResponsetagsTypeDef(
    _ClientDescribeTaskDefinitionResponsetagsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
        ],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
        ],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
        ],
        "volumesFrom": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
        ],
        "linuxParameters": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef,
        "secrets": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
        ],
        "dependsOn": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
        ],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
        ],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
        ],
        "logConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    {
        "name": str,
        "host": ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef
):
    pass


_ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
        ],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": Literal["bridge", "host", "awsvpc", "none"],
        "revision": int,
        "volumes": List[ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef],
        "status": Literal["ACTIVE", "INACTIVE"],
        "requiresAttributes": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
        ],
        "placementConstraints": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
        ],
        "compatibilities": List[Literal["EC2", "FARGATE"]],
        "requiresCompatibilities": List[Literal["EC2", "FARGATE"]],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
        ],
        "pidMode": Literal["host", "task"],
        "ipcMode": Literal["host", "task", "none"],
        "proxyConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef(
    _ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef
):
    """
    - **taskDefinition** *(dict) --*

      The full task definition description.
      - **taskDefinitionArn** *(string) --*

        The full Amazon Resource Name (ARN) of the task definition.
    """


_ClientDescribeTaskDefinitionResponseTypeDef = TypedDict(
    "_ClientDescribeTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef,
        "tags": List[ClientDescribeTaskDefinitionResponsetagsTypeDef],
    },
    total=False,
)


class ClientDescribeTaskDefinitionResponseTypeDef(_ClientDescribeTaskDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **taskDefinition** *(dict) --*

        The full task definition description.
        - **taskDefinitionArn** *(string) --*

          The full Amazon Resource Name (ARN) of the task definition.
    """


_ClientDescribeTaskSetsResponsefailuresTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)


class ClientDescribeTaskSetsResponsefailuresTypeDef(_ClientDescribeTaskSetsResponsefailuresTypeDef):
    pass


_ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef(
    _ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef
):
    pass


_ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef(
    _ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef
):
    pass


_ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)


class ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef(
    _ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef
):
    pass


_ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef(
    _ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef
):
    pass


_ClientDescribeTaskSetsResponsetaskSetsTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponsetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef],
        "scale": ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientDescribeTaskSetsResponsetaskSetsTypeDef(_ClientDescribeTaskSetsResponsetaskSetsTypeDef):
    """
    - *(dict) --*

      Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
      deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
      many tasks are running, and whether the task set serves production traffic.
      - **id** *(string) --*

        The ID of the task set.
    """


_ClientDescribeTaskSetsResponseTypeDef = TypedDict(
    "_ClientDescribeTaskSetsResponseTypeDef",
    {
        "taskSets": List[ClientDescribeTaskSetsResponsetaskSetsTypeDef],
        "failures": List[ClientDescribeTaskSetsResponsefailuresTypeDef],
    },
    total=False,
)


class ClientDescribeTaskSetsResponseTypeDef(_ClientDescribeTaskSetsResponseTypeDef):
    """
    - *(dict) --*

      - **taskSets** *(list) --*

        The list of task sets described.
        - *(dict) --*

          Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
          deployment. An Amazon ECS task set includes details such as the desired number of tasks,
          how many tasks are running, and whether the task set serves production traffic.
          - **id** *(string) --*

            The ID of the task set.
    """


_ClientDescribeTasksResponsefailuresTypeDef = TypedDict(
    "_ClientDescribeTasksResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)


class ClientDescribeTasksResponsefailuresTypeDef(_ClientDescribeTasksResponsefailuresTypeDef):
    pass


_ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef(
    _ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef
):
    pass


_ClientDescribeTasksResponsetasksattachmentsTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef],
    },
    total=False,
)


class ClientDescribeTasksResponsetasksattachmentsTypeDef(
    _ClientDescribeTasksResponsetasksattachmentsTypeDef
):
    """
    - *(dict) --*

      An object representing a container instance or task attachment.
      - **id** *(string) --*

        The unique identifier for the attachment.
    """


_ClientDescribeTasksResponsetasksattributesTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDescribeTasksResponsetasksattributesTypeDef(
    _ClientDescribeTasksResponsetasksattributesTypeDef
):
    pass


_ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef(
    _ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef
):
    pass


_ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)


class ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef(
    _ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef
):
    pass


_ClientDescribeTasksResponsetaskscontainersTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetaskscontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[
            ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef
        ],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)


class ClientDescribeTasksResponsetaskscontainersTypeDef(
    _ClientDescribeTasksResponsetaskscontainersTypeDef
):
    pass


_ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef(
    _ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef
):
    pass


_ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef(
    _ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef
):
    pass


_ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef(
    _ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef
):
    pass


_ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef(
    _ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
):
    pass


_ClientDescribeTasksResponsetasksoverridesTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksoverridesTypeDef",
    {
        "containerOverrides": List[
            ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef
        ],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)


class ClientDescribeTasksResponsetasksoverridesTypeDef(
    _ClientDescribeTasksResponsetasksoverridesTypeDef
):
    pass


_ClientDescribeTasksResponsetaskstagsTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetaskstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDescribeTasksResponsetaskstagsTypeDef(_ClientDescribeTasksResponsetaskstagsTypeDef):
    pass


_ClientDescribeTasksResponsetasksTypeDef = TypedDict(
    "_ClientDescribeTasksResponsetasksTypeDef",
    {
        "attachments": List[ClientDescribeTasksResponsetasksattachmentsTypeDef],
        "attributes": List[ClientDescribeTasksResponsetasksattributesTypeDef],
        "availabilityZone": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientDescribeTasksResponsetaskscontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientDescribeTasksResponsetasksoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientDescribeTasksResponsetaskstagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)


class ClientDescribeTasksResponsetasksTypeDef(_ClientDescribeTasksResponsetasksTypeDef):
    """
    - *(dict) --*

      Details on a task in a cluster.
      - **attachments** *(list) --*

        The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network
        mode.
        - *(dict) --*

          An object representing a container instance or task attachment.
          - **id** *(string) --*

            The unique identifier for the attachment.
    """


_ClientDescribeTasksResponseTypeDef = TypedDict(
    "_ClientDescribeTasksResponseTypeDef",
    {
        "tasks": List[ClientDescribeTasksResponsetasksTypeDef],
        "failures": List[ClientDescribeTasksResponsefailuresTypeDef],
    },
    total=False,
)


class ClientDescribeTasksResponseTypeDef(_ClientDescribeTasksResponseTypeDef):
    """
    - *(dict) --*

      - **tasks** *(list) --*

        The list of tasks.
        - *(dict) --*

          Details on a task in a cluster.
          - **attachments** *(list) --*

            The Elastic Network Adapter associated with the task if the task uses the ``awsvpc``
            network mode.
            - *(dict) --*

              An object representing a container instance or task attachment.
              - **id** *(string) --*

                The unique identifier for the attachment.
    """


_ClientDiscoverPollEndpointResponseTypeDef = TypedDict(
    "_ClientDiscoverPollEndpointResponseTypeDef",
    {"endpoint": str, "telemetryEndpoint": str},
    total=False,
)


class ClientDiscoverPollEndpointResponseTypeDef(_ClientDiscoverPollEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **endpoint** *(string) --*

        The endpoint for the Amazon ECS agent to poll.
    """


_ClientListAccountSettingsResponsesettingsTypeDef = TypedDict(
    "_ClientListAccountSettingsResponsesettingsTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)


class ClientListAccountSettingsResponsesettingsTypeDef(
    _ClientListAccountSettingsResponsesettingsTypeDef
):
    """
    - *(dict) --*

      The current account setting for a resource.
      - **name** *(string) --*

        The Amazon ECS resource name.
    """


_ClientListAccountSettingsResponseTypeDef = TypedDict(
    "_ClientListAccountSettingsResponseTypeDef",
    {"settings": List[ClientListAccountSettingsResponsesettingsTypeDef], "nextToken": str},
    total=False,
)


class ClientListAccountSettingsResponseTypeDef(_ClientListAccountSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **settings** *(list) --*

        The account settings for the resource.
        - *(dict) --*

          The current account setting for a resource.
          - **name** *(string) --*

            The Amazon ECS resource name.
    """


_ClientListAttributesResponseattributesTypeDef = TypedDict(
    "_ClientListAttributesResponseattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientListAttributesResponseattributesTypeDef(_ClientListAttributesResponseattributesTypeDef):
    """
    - *(dict) --*

      An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you
      to extend the Amazon ECS data model by adding custom metadata to your resources. For more
      information, see `Attributes
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **name** *(string) --*

        The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens,
        underscores, and periods are allowed.
    """


_ClientListAttributesResponseTypeDef = TypedDict(
    "_ClientListAttributesResponseTypeDef",
    {"attributes": List[ClientListAttributesResponseattributesTypeDef], "nextToken": str},
    total=False,
)


class ClientListAttributesResponseTypeDef(_ClientListAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **attributes** *(list) --*

        A list of attribute objects that meet the criteria of the request.
        - *(dict) --*

          An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable
          you to extend the Amazon ECS data model by adding custom metadata to your resources. For
          more information, see `Attributes
          <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
          in the *Amazon Elastic Container Service Developer Guide* .
          - **name** *(string) --*

            The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers,
            hyphens, underscores, and periods are allowed.
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef", {"clusterArns": List[str], "nextToken": str}, total=False
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    - *(dict) --*

      - **clusterArns** *(list) --*

        The list of full Amazon Resource Name (ARN) entries for each cluster associated with your
        account.
        - *(string) --*
    """


_ClientListContainerInstancesResponseTypeDef = TypedDict(
    "_ClientListContainerInstancesResponseTypeDef",
    {"containerInstanceArns": List[str], "nextToken": str},
    total=False,
)


class ClientListContainerInstancesResponseTypeDef(_ClientListContainerInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **containerInstanceArns** *(list) --*

        The list of container instances with full ARN entries for each container instance associated
        with the specified cluster.
        - *(string) --*
    """


_ClientListServicesResponseTypeDef = TypedDict(
    "_ClientListServicesResponseTypeDef", {"serviceArns": List[str], "nextToken": str}, total=False
)


class ClientListServicesResponseTypeDef(_ClientListServicesResponseTypeDef):
    """
    - *(dict) --*

      - **serviceArns** *(list) --*

        The list of full ARN entries for each service associated with the specified cluster.
        - *(string) --*
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The tags for the resource.
        - *(dict) --*

          The metadata that you apply to a resource to help you categorize and organize them. Each
          tag consists of a key and an optional value, both of which you define.
          The following basic restrictions apply to tags:
          * Maximum number of tags per resource - 50
          * For each resource, each tag key must be unique, and each tag key can have only one
          value.
          * Maximum key length - 128 Unicode characters in UTF-8
          * Maximum value length - 256 Unicode characters in UTF-8
          * If your tagging schema is used across multiple services and resources, remember that
          other services may have restrictions on allowed characters. Generally allowed characters
          are: letters, numbers, and spaces representable in UTF-8, and the following characters: +
          - = . _ : / @.
          * Tag keys and values are case-sensitive.
          * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a
          prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete
          tag keys or values with this prefix. Tags with this prefix do not count against your tags
          per resource limit.
          - **key** *(string) --*

            One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
            like a category for more specific tag values.
    """


_ClientListTaskDefinitionFamiliesResponseTypeDef = TypedDict(
    "_ClientListTaskDefinitionFamiliesResponseTypeDef",
    {"families": List[str], "nextToken": str},
    total=False,
)


class ClientListTaskDefinitionFamiliesResponseTypeDef(
    _ClientListTaskDefinitionFamiliesResponseTypeDef
):
    """
    - *(dict) --*

      - **families** *(list) --*

        The list of task definition family names that match the ``ListTaskDefinitionFamilies``
        request.
        - *(string) --*
    """


_ClientListTaskDefinitionsResponseTypeDef = TypedDict(
    "_ClientListTaskDefinitionsResponseTypeDef",
    {"taskDefinitionArns": List[str], "nextToken": str},
    total=False,
)


class ClientListTaskDefinitionsResponseTypeDef(_ClientListTaskDefinitionsResponseTypeDef):
    """
    - *(dict) --*

      - **taskDefinitionArns** *(list) --*

        The list of task definition Amazon Resource Name (ARN) entries for the
        ``ListTaskDefinitions`` request.
        - *(string) --*
    """


_ClientListTasksResponseTypeDef = TypedDict(
    "_ClientListTasksResponseTypeDef", {"taskArns": List[str], "nextToken": str}, total=False
)


class ClientListTasksResponseTypeDef(_ClientListTasksResponseTypeDef):
    """
    - *(dict) --*

      - **taskArns** *(list) --*

        The list of task ARN entries for the ``ListTasks`` request.
        - *(string) --*
    """


_ClientPutAccountSettingDefaultResponsesettingTypeDef = TypedDict(
    "_ClientPutAccountSettingDefaultResponsesettingTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)


class ClientPutAccountSettingDefaultResponsesettingTypeDef(
    _ClientPutAccountSettingDefaultResponsesettingTypeDef
):
    """
    - **setting** *(dict) --*

      The current account setting for a resource.
      - **name** *(string) --*

        The Amazon ECS resource name.
    """


_ClientPutAccountSettingDefaultResponseTypeDef = TypedDict(
    "_ClientPutAccountSettingDefaultResponseTypeDef",
    {"setting": ClientPutAccountSettingDefaultResponsesettingTypeDef},
    total=False,
)


class ClientPutAccountSettingDefaultResponseTypeDef(_ClientPutAccountSettingDefaultResponseTypeDef):
    """
    - *(dict) --*

      - **setting** *(dict) --*

        The current account setting for a resource.
        - **name** *(string) --*

          The Amazon ECS resource name.
    """


_ClientPutAccountSettingResponsesettingTypeDef = TypedDict(
    "_ClientPutAccountSettingResponsesettingTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)


class ClientPutAccountSettingResponsesettingTypeDef(_ClientPutAccountSettingResponsesettingTypeDef):
    """
    - **setting** *(dict) --*

      The current account setting for a resource.
      - **name** *(string) --*

        The Amazon ECS resource name.
    """


_ClientPutAccountSettingResponseTypeDef = TypedDict(
    "_ClientPutAccountSettingResponseTypeDef",
    {"setting": ClientPutAccountSettingResponsesettingTypeDef},
    total=False,
)


class ClientPutAccountSettingResponseTypeDef(_ClientPutAccountSettingResponseTypeDef):
    """
    - *(dict) --*

      - **setting** *(dict) --*

        The current account setting for a resource.
        - **name** *(string) --*

          The Amazon ECS resource name.
    """


_RequiredClientPutAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientPutAttributesAttributesTypeDef", {"name": str}
)
_OptionalClientPutAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientPutAttributesAttributesTypeDef",
    {"value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientPutAttributesAttributesTypeDef(
    _RequiredClientPutAttributesAttributesTypeDef, _OptionalClientPutAttributesAttributesTypeDef
):
    """
    - *(dict) --*

      An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you
      to extend the Amazon ECS data model by adding custom metadata to your resources. For more
      information, see `Attributes
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **name** *(string) --***[REQUIRED]**

        The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens,
        underscores, and periods are allowed.
    """


_ClientPutAttributesResponseattributesTypeDef = TypedDict(
    "_ClientPutAttributesResponseattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientPutAttributesResponseattributesTypeDef(_ClientPutAttributesResponseattributesTypeDef):
    """
    - *(dict) --*

      An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you
      to extend the Amazon ECS data model by adding custom metadata to your resources. For more
      information, see `Attributes
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **name** *(string) --*

        The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens,
        underscores, and periods are allowed.
    """


_ClientPutAttributesResponseTypeDef = TypedDict(
    "_ClientPutAttributesResponseTypeDef",
    {"attributes": List[ClientPutAttributesResponseattributesTypeDef]},
    total=False,
)


class ClientPutAttributesResponseTypeDef(_ClientPutAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **attributes** *(list) --*

        The attributes applied to your resource.
        - *(dict) --*

          An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable
          you to extend the Amazon ECS data model by adding custom metadata to your resources. For
          more information, see `Attributes
          <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
          in the *Amazon Elastic Container Service Developer Guide* .
          - **name** *(string) --*

            The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers,
            hyphens, underscores, and periods are allowed.
    """


_RequiredClientRegisterContainerInstanceAttributesTypeDef = TypedDict(
    "_RequiredClientRegisterContainerInstanceAttributesTypeDef", {"name": str}
)
_OptionalClientRegisterContainerInstanceAttributesTypeDef = TypedDict(
    "_OptionalClientRegisterContainerInstanceAttributesTypeDef",
    {"value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientRegisterContainerInstanceAttributesTypeDef(
    _RequiredClientRegisterContainerInstanceAttributesTypeDef,
    _OptionalClientRegisterContainerInstanceAttributesTypeDef,
):
    """
    - *(dict) --*

      An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you
      to extend the Amazon ECS data model by adding custom metadata to your resources. For more
      information, see `Attributes
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **name** *(string) --***[REQUIRED]**

        The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens,
        underscores, and periods are allowed.
    """


_RequiredClientRegisterContainerInstancePlatformDevicesTypeDef = TypedDict(
    "_RequiredClientRegisterContainerInstancePlatformDevicesTypeDef", {"id": str}
)
_OptionalClientRegisterContainerInstancePlatformDevicesTypeDef = TypedDict(
    "_OptionalClientRegisterContainerInstancePlatformDevicesTypeDef", {"type": str}, total=False
)


class ClientRegisterContainerInstancePlatformDevicesTypeDef(
    _RequiredClientRegisterContainerInstancePlatformDevicesTypeDef,
    _OptionalClientRegisterContainerInstancePlatformDevicesTypeDef,
):
    """
    - *(dict) --*

      The devices that are available on the container instance. The only supported device type is a
      GPU.
      - **id** *(string) --***[REQUIRED]**

        The ID for the GPU(s) on the container instance. The available GPU IDs can also be obtained
        on the container instance in the ``/var/lib/ecs/gpu/nvidia_gpu_info.json`` file.
    """


_ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef
):
    pass


_ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef
        ],
    },
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef
):
    pass


_ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef
):
    pass


_ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef
):
    pass


_ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef
):
    pass


_ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef
):
    pass


_ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef
):
    pass


_ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "version": int,
        "versionInfo": ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef,
        "remainingResources": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef
        ],
        "tags": List[ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef],
    },
    total=False,
)


class ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef(
    _ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef
):
    """
    - **containerInstance** *(dict) --*

      The container instance that was registered.
      - **containerInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the container instance. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account
        ID of the container instance owner, the ``container-instance`` namespace, and then the
        container instance ID. For example,
        ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientRegisterContainerInstanceResponseTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceResponseTypeDef",
    {"containerInstance": ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef},
    total=False,
)


class ClientRegisterContainerInstanceResponseTypeDef(
    _ClientRegisterContainerInstanceResponseTypeDef
):
    """
    - *(dict) --*

      - **containerInstance** *(dict) --*

        The container instance that was registered.
        - **containerInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the container instance. The ARN contains the
          ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS
          account ID of the container instance owner, the ``container-instance`` namespace, and then
          the container instance ID. For example,
          ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientRegisterContainerInstanceTagsTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientRegisterContainerInstanceTagsTypeDef(_ClientRegisterContainerInstanceTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientRegisterContainerInstanceTotalResourcesTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceTotalResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientRegisterContainerInstanceTotalResourcesTypeDef(
    _ClientRegisterContainerInstanceTotalResourcesTypeDef
):
    """
    - *(dict) --*

      Describes the resources available for a container instance.
      - **name** *(string) --*

        The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a
        user-defined resource.
    """


_ClientRegisterContainerInstanceVersionInfoTypeDef = TypedDict(
    "_ClientRegisterContainerInstanceVersionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)


class ClientRegisterContainerInstanceVersionInfoTypeDef(
    _ClientRegisterContainerInstanceVersionInfoTypeDef
):
    """
    The version information for the Amazon ECS container agent and Docker daemon running on the
    container instance.
    - **agentVersion** *(string) --*

      The version number of the Amazon ECS container agent.
    """


_ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef
):
    pass


_ClientRegisterTaskDefinitionContainerDefinitionsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionContainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef],
        "mountPoints": List[ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef],
        "volumesFrom": List[ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef],
        "linuxParameters": ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef,
        "secrets": List[ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef],
        "dependsOn": List[ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef],
        "logConfiguration": ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)


class ClientRegisterTaskDefinitionContainerDefinitionsTypeDef(
    _ClientRegisterTaskDefinitionContainerDefinitionsTypeDef
):
    """
    - *(dict) --*

      Container definitions are used in task definitions to describe the different containers that
      are launched as part of a task.
      - **name** *(string) --*

        The name of a container. If you are linking multiple containers together in a task
        definition, the ``name`` of one container can be entered in the ``links`` of another
        container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers,
        and hyphens are allowed. This parameter maps to ``name`` in the `Create a container
        <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the
        `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--name`` option
        to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
    """


_RequiredClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef = TypedDict(
    "_RequiredClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef", {"deviceName": str}
)
_OptionalClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef = TypedDict(
    "_OptionalClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef",
    {"deviceType": str},
    total=False,
)


class ClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef(
    _RequiredClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef,
    _OptionalClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef,
):
    """
    - *(dict) --*

      Details on a Elastic Inference accelerator. For more information, see `Working with Amazon
      Elastic Inference on Amazon ECS
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-eia.html>`__ in the *Amazon
      Elastic Container Service Developer Guide* .
      - **deviceName** *(string) --***[REQUIRED]**

        The Elastic Inference accelerator device name. The ``deviceName`` must also be referenced in
        a container definition as a  ResourceRequirement .
    """


_ClientRegisterTaskDefinitionPlacementConstraintsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionPlacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)


class ClientRegisterTaskDefinitionPlacementConstraintsTypeDef(
    _ClientRegisterTaskDefinitionPlacementConstraintsTypeDef
):
    """
    - *(dict) --*

      An object representing a constraint on task placement in the task definition. For more
      information, see `Task Placement Constraints
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      .. note::

        If you are using the Fargate launch type, task placement constraints are not supported.
    """


_ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef(
    _ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef
):
    pass


_ClientRegisterTaskDefinitionProxyConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionProxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef],
    },
    total=False,
)


class ClientRegisterTaskDefinitionProxyConfigurationTypeDef(
    _ClientRegisterTaskDefinitionProxyConfigurationTypeDef
):
    """
    The configuration details for the App Mesh proxy.
    For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of
    the container agent and at least version 1.26.0-1 of the ``ecs-init`` package to enable a proxy
    configuration. If your container instances are launched from the Amazon ECS-optimized AMI
    version ``20190301`` or later, then they contain the required versions of the container agent
    and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the
    *Amazon Elastic Container Service Developer Guide* .
    For tasks using the Fargate launch type, the task or service requires platform version 1.3.0 or
    later.
    - **type** *(string) --*

      The proxy type. The only supported value is ``APPMESH`` .
    """


_ClientRegisterTaskDefinitionResponsetagsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientRegisterTaskDefinitionResponsetagsTypeDef(
    _ClientRegisterTaskDefinitionResponsetagsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
        ],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
        ],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
        ],
        "volumesFrom": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
        ],
        "linuxParameters": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef,
        "secrets": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
        ],
        "dependsOn": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
        ],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
        ],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
        ],
        "logConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
        ],
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    {
        "name": str,
        "host": ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef,
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef
):
    pass


_ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
        ],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": Literal["bridge", "host", "awsvpc", "none"],
        "revision": int,
        "volumes": List[ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef],
        "status": Literal["ACTIVE", "INACTIVE"],
        "requiresAttributes": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
        ],
        "placementConstraints": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
        ],
        "compatibilities": List[Literal["EC2", "FARGATE"]],
        "requiresCompatibilities": List[Literal["EC2", "FARGATE"]],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
        ],
        "pidMode": Literal["host", "task"],
        "ipcMode": Literal["host", "task", "none"],
        "proxyConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef,
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef(
    _ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef
):
    """
    - **taskDefinition** *(dict) --*

      The full description of the registered task definition.
      - **taskDefinitionArn** *(string) --*

        The full Amazon Resource Name (ARN) of the task definition.
    """


_ClientRegisterTaskDefinitionResponseTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef,
        "tags": List[ClientRegisterTaskDefinitionResponsetagsTypeDef],
    },
    total=False,
)


class ClientRegisterTaskDefinitionResponseTypeDef(_ClientRegisterTaskDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **taskDefinition** *(dict) --*

        The full description of the registered task definition.
        - **taskDefinitionArn** *(string) --*

          The full Amazon Resource Name (ARN) of the task definition.
    """


_ClientRegisterTaskDefinitionTagsTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientRegisterTaskDefinitionTagsTypeDef(_ClientRegisterTaskDefinitionTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)


class ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef(
    _ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef
):
    pass


_ClientRegisterTaskDefinitionVolumeshostTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionVolumeshostTypeDef", {"sourcePath": str}, total=False
)


class ClientRegisterTaskDefinitionVolumeshostTypeDef(
    _ClientRegisterTaskDefinitionVolumeshostTypeDef
):
    pass


_ClientRegisterTaskDefinitionVolumesTypeDef = TypedDict(
    "_ClientRegisterTaskDefinitionVolumesTypeDef",
    {
        "name": str,
        "host": ClientRegisterTaskDefinitionVolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef,
    },
    total=False,
)


class ClientRegisterTaskDefinitionVolumesTypeDef(_ClientRegisterTaskDefinitionVolumesTypeDef):
    """
    - *(dict) --*

      A data volume used in a task definition. For tasks that use a Docker volume, specify a
      ``DockerVolumeConfiguration`` . For tasks that use a bind mount host volume, specify a
      ``host`` and optional ``sourcePath`` . For more information, see `Using Data Volumes in Tasks
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html>`__ .
      - **name** *(string) --*

        The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, and hyphens
        are allowed. This name is referenced in the ``sourceVolume`` parameter of container
        definition ``mountPoints`` .
    """


_ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef
):
    """
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientRunTaskNetworkConfigurationTypeDef = TypedDict(
    "_ClientRunTaskNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)


class ClientRunTaskNetworkConfigurationTypeDef(_ClientRunTaskNetworkConfigurationTypeDef):
    """
    The network configuration for the task. This parameter is required for task definitions that use
    the ``awsvpc`` network mode to receive their own elastic network interface, and it is not
    supported for other network modes. For more information, see `Task Networking
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the
    *Amazon Elastic Container Service Developer Guide* .
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientRunTaskOverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientRunTaskOverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRunTaskOverridescontainerOverridesenvironmentTypeDef(
    _ClientRunTaskOverridescontainerOverridesenvironmentTypeDef
):
    pass


_ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientRunTaskOverridescontainerOverridesTypeDef = TypedDict(
    "_ClientRunTaskOverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[ClientRunTaskOverridescontainerOverridesenvironmentTypeDef],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientRunTaskOverridescontainerOverridesTypeDef(
    _ClientRunTaskOverridescontainerOverridesTypeDef
):
    pass


_ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "_ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef(
    _ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef
):
    pass


_ClientRunTaskOverridesTypeDef = TypedDict(
    "_ClientRunTaskOverridesTypeDef",
    {
        "containerOverrides": List[ClientRunTaskOverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)


class ClientRunTaskOverridesTypeDef(_ClientRunTaskOverridesTypeDef):
    """
    A list of container overrides in JSON format that specify the name of a container in the
    specified task definition and the overrides it should receive. You can override the default
    command for a container (that is specified in the task definition or Docker image) with a
    ``command`` override. You can also override existing environment variables (that are specified
    in the task definition or Docker image) on a container or add new environment variables to it
    with an ``environment`` override.
    .. note::

      A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting
      characters of the override structure.
    """


_ClientRunTaskPlacementConstraintsTypeDef = TypedDict(
    "_ClientRunTaskPlacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)


class ClientRunTaskPlacementConstraintsTypeDef(_ClientRunTaskPlacementConstraintsTypeDef):
    """
    - *(dict) --*

      An object representing a constraint on task placement. For more information, see `Task
      Placement Constraints
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      .. note::

        If you are using the Fargate launch type, task placement constraints are not supported.
    """


_ClientRunTaskPlacementStrategyTypeDef = TypedDict(
    "_ClientRunTaskPlacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)


class ClientRunTaskPlacementStrategyTypeDef(_ClientRunTaskPlacementStrategyTypeDef):
    """
    - *(dict) --*

      The task placement strategy for a task or service. For more information, see `Task Placement
      Strategies
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **type** *(string) --*

        The type of placement strategy. The ``random`` placement strategy randomly places tasks on
        available candidates. The ``spread`` placement strategy spreads placement across available
        candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on
        available candidates that have the least available amount of the resource that is specified
        with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the
        instance with the least amount of remaining memory (but still enough to run the task).
    """


_ClientRunTaskResponsefailuresTypeDef = TypedDict(
    "_ClientRunTaskResponsefailuresTypeDef", {"arn": str, "reason": str, "detail": str}, total=False
)


class ClientRunTaskResponsefailuresTypeDef(_ClientRunTaskResponsefailuresTypeDef):
    pass


_ClientRunTaskResponsetasksattachmentsdetailsTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksattachmentsdetailsTypeDef", {"name": str, "value": str}, total=False
)


class ClientRunTaskResponsetasksattachmentsdetailsTypeDef(
    _ClientRunTaskResponsetasksattachmentsdetailsTypeDef
):
    pass


_ClientRunTaskResponsetasksattachmentsTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientRunTaskResponsetasksattachmentsdetailsTypeDef],
    },
    total=False,
)


class ClientRunTaskResponsetasksattachmentsTypeDef(_ClientRunTaskResponsetasksattachmentsTypeDef):
    """
    - *(dict) --*

      An object representing a container instance or task attachment.
      - **id** *(string) --*

        The unique identifier for the attachment.
    """


_ClientRunTaskResponsetasksattributesTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientRunTaskResponsetasksattributesTypeDef(_ClientRunTaskResponsetasksattributesTypeDef):
    pass


_ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef = TypedDict(
    "_ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef(
    _ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef
):
    pass


_ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef = TypedDict(
    "_ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)


class ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef(
    _ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef
):
    pass


_ClientRunTaskResponsetaskscontainersTypeDef = TypedDict(
    "_ClientRunTaskResponsetaskscontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)


class ClientRunTaskResponsetaskscontainersTypeDef(_ClientRunTaskResponsetaskscontainersTypeDef):
    pass


_ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef(
    _ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef
):
    pass


_ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef(
    _ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef
):
    pass


_ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef(
    _ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef
):
    pass


_ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef(
    _ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
):
    pass


_ClientRunTaskResponsetasksoverridesTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksoverridesTypeDef",
    {
        "containerOverrides": List[ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)


class ClientRunTaskResponsetasksoverridesTypeDef(_ClientRunTaskResponsetasksoverridesTypeDef):
    pass


_ClientRunTaskResponsetaskstagsTypeDef = TypedDict(
    "_ClientRunTaskResponsetaskstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientRunTaskResponsetaskstagsTypeDef(_ClientRunTaskResponsetaskstagsTypeDef):
    pass


_ClientRunTaskResponsetasksTypeDef = TypedDict(
    "_ClientRunTaskResponsetasksTypeDef",
    {
        "attachments": List[ClientRunTaskResponsetasksattachmentsTypeDef],
        "attributes": List[ClientRunTaskResponsetasksattributesTypeDef],
        "availabilityZone": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientRunTaskResponsetaskscontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientRunTaskResponsetasksoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientRunTaskResponsetaskstagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)


class ClientRunTaskResponsetasksTypeDef(_ClientRunTaskResponsetasksTypeDef):
    """
    - *(dict) --*

      Details on a task in a cluster.
      - **attachments** *(list) --*

        The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network
        mode.
        - *(dict) --*

          An object representing a container instance or task attachment.
          - **id** *(string) --*

            The unique identifier for the attachment.
    """


_ClientRunTaskResponseTypeDef = TypedDict(
    "_ClientRunTaskResponseTypeDef",
    {
        "tasks": List[ClientRunTaskResponsetasksTypeDef],
        "failures": List[ClientRunTaskResponsefailuresTypeDef],
    },
    total=False,
)


class ClientRunTaskResponseTypeDef(_ClientRunTaskResponseTypeDef):
    """
    - *(dict) --*

      - **tasks** *(list) --*

        A full description of the tasks that were run. The tasks that were successfully placed on
        your cluster are described here.
        - *(dict) --*

          Details on a task in a cluster.
          - **attachments** *(list) --*

            The Elastic Network Adapter associated with the task if the task uses the ``awsvpc``
            network mode.
            - *(dict) --*

              An object representing a container instance or task attachment.
              - **id** *(string) --*

                The unique identifier for the attachment.
    """


_ClientRunTaskTagsTypeDef = TypedDict(
    "_ClientRunTaskTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientRunTaskTagsTypeDef(_ClientRunTaskTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef
):
    """
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientStartTaskNetworkConfigurationTypeDef = TypedDict(
    "_ClientStartTaskNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)


class ClientStartTaskNetworkConfigurationTypeDef(_ClientStartTaskNetworkConfigurationTypeDef):
    """
    The VPC subnet and security group configuration for tasks that receive their own elastic network
    interface by using the ``awsvpc`` networking mode.
    - **awsvpcConfiguration** *(dict) --*

      The VPC subnets and security groups associated with a task.
      .. note::

        All specified subnets and security groups must be from the same VPC.
    """


_ClientStartTaskOverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientStartTaskOverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStartTaskOverridescontainerOverridesenvironmentTypeDef(
    _ClientStartTaskOverridescontainerOverridesenvironmentTypeDef
):
    pass


_ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientStartTaskOverridescontainerOverridesTypeDef = TypedDict(
    "_ClientStartTaskOverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[ClientStartTaskOverridescontainerOverridesenvironmentTypeDef],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientStartTaskOverridescontainerOverridesTypeDef(
    _ClientStartTaskOverridescontainerOverridesTypeDef
):
    pass


_ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "_ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef(
    _ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef
):
    pass


_ClientStartTaskOverridesTypeDef = TypedDict(
    "_ClientStartTaskOverridesTypeDef",
    {
        "containerOverrides": List[ClientStartTaskOverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)


class ClientStartTaskOverridesTypeDef(_ClientStartTaskOverridesTypeDef):
    """
    A list of container overrides in JSON format that specify the name of a container in the
    specified task definition and the overrides it should receive. You can override the default
    command for a container (that is specified in the task definition or Docker image) with a
    ``command`` override. You can also override existing environment variables (that are specified
    in the task definition or Docker image) on a container or add new environment variables to it
    with an ``environment`` override.
    .. note::

      A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting
      characters of the override structure.
    """


_ClientStartTaskResponsefailuresTypeDef = TypedDict(
    "_ClientStartTaskResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)


class ClientStartTaskResponsefailuresTypeDef(_ClientStartTaskResponsefailuresTypeDef):
    pass


_ClientStartTaskResponsetasksattachmentsdetailsTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStartTaskResponsetasksattachmentsdetailsTypeDef(
    _ClientStartTaskResponsetasksattachmentsdetailsTypeDef
):
    pass


_ClientStartTaskResponsetasksattachmentsTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientStartTaskResponsetasksattachmentsdetailsTypeDef],
    },
    total=False,
)


class ClientStartTaskResponsetasksattachmentsTypeDef(
    _ClientStartTaskResponsetasksattachmentsTypeDef
):
    """
    - *(dict) --*

      An object representing a container instance or task attachment.
      - **id** *(string) --*

        The unique identifier for the attachment.
    """


_ClientStartTaskResponsetasksattributesTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientStartTaskResponsetasksattributesTypeDef(_ClientStartTaskResponsetasksattributesTypeDef):
    pass


_ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef = TypedDict(
    "_ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef(
    _ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef
):
    pass


_ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef = TypedDict(
    "_ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)


class ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef(
    _ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef
):
    pass


_ClientStartTaskResponsetaskscontainersTypeDef = TypedDict(
    "_ClientStartTaskResponsetaskscontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)


class ClientStartTaskResponsetaskscontainersTypeDef(_ClientStartTaskResponsetaskscontainersTypeDef):
    pass


_ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef(
    _ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef
):
    pass


_ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef(
    _ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef
):
    pass


_ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef(
    _ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef
):
    pass


_ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef(
    _ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
):
    pass


_ClientStartTaskResponsetasksoverridesTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksoverridesTypeDef",
    {
        "containerOverrides": List[ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)


class ClientStartTaskResponsetasksoverridesTypeDef(_ClientStartTaskResponsetasksoverridesTypeDef):
    pass


_ClientStartTaskResponsetaskstagsTypeDef = TypedDict(
    "_ClientStartTaskResponsetaskstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientStartTaskResponsetaskstagsTypeDef(_ClientStartTaskResponsetaskstagsTypeDef):
    pass


_ClientStartTaskResponsetasksTypeDef = TypedDict(
    "_ClientStartTaskResponsetasksTypeDef",
    {
        "attachments": List[ClientStartTaskResponsetasksattachmentsTypeDef],
        "attributes": List[ClientStartTaskResponsetasksattributesTypeDef],
        "availabilityZone": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientStartTaskResponsetaskscontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientStartTaskResponsetasksoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientStartTaskResponsetaskstagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)


class ClientStartTaskResponsetasksTypeDef(_ClientStartTaskResponsetasksTypeDef):
    """
    - *(dict) --*

      Details on a task in a cluster.
      - **attachments** *(list) --*

        The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network
        mode.
        - *(dict) --*

          An object representing a container instance or task attachment.
          - **id** *(string) --*

            The unique identifier for the attachment.
    """


_ClientStartTaskResponseTypeDef = TypedDict(
    "_ClientStartTaskResponseTypeDef",
    {
        "tasks": List[ClientStartTaskResponsetasksTypeDef],
        "failures": List[ClientStartTaskResponsefailuresTypeDef],
    },
    total=False,
)


class ClientStartTaskResponseTypeDef(_ClientStartTaskResponseTypeDef):
    """
    - *(dict) --*

      - **tasks** *(list) --*

        A full description of the tasks that were started. Each task that was successfully placed on
        your container instances is described.
        - *(dict) --*

          Details on a task in a cluster.
          - **attachments** *(list) --*

            The Elastic Network Adapter associated with the task if the task uses the ``awsvpc``
            network mode.
            - *(dict) --*

              An object representing a container instance or task attachment.
              - **id** *(string) --*

                The unique identifier for the attachment.
    """


_ClientStartTaskTagsTypeDef = TypedDict(
    "_ClientStartTaskTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientStartTaskTagsTypeDef(_ClientStartTaskTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientStopTaskResponsetaskattachmentsdetailsTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskattachmentsdetailsTypeDef", {"name": str, "value": str}, total=False
)


class ClientStopTaskResponsetaskattachmentsdetailsTypeDef(
    _ClientStopTaskResponsetaskattachmentsdetailsTypeDef
):
    pass


_ClientStopTaskResponsetaskattachmentsTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientStopTaskResponsetaskattachmentsdetailsTypeDef],
    },
    total=False,
)


class ClientStopTaskResponsetaskattachmentsTypeDef(_ClientStopTaskResponsetaskattachmentsTypeDef):
    """
    - *(dict) --*

      An object representing a container instance or task attachment.
      - **id** *(string) --*

        The unique identifier for the attachment.
    """


_ClientStopTaskResponsetaskattributesTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientStopTaskResponsetaskattributesTypeDef(_ClientStopTaskResponsetaskattributesTypeDef):
    pass


_ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef(
    _ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef
):
    pass


_ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)


class ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef(
    _ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef
):
    pass


_ClientStopTaskResponsetaskcontainersTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskcontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)


class ClientStopTaskResponsetaskcontainersTypeDef(_ClientStopTaskResponsetaskcontainersTypeDef):
    pass


_ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef(
    _ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef
):
    pass


_ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef(
    _ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef
):
    pass


_ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)


class ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef(
    _ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef
):
    pass


_ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)


class ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef(
    _ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef
):
    pass


_ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)


class ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef(
    _ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef
):
    pass


_ClientStopTaskResponsetaskoverridesTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskoverridesTypeDef",
    {
        "containerOverrides": List[ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)


class ClientStopTaskResponsetaskoverridesTypeDef(_ClientStopTaskResponsetaskoverridesTypeDef):
    pass


_ClientStopTaskResponsetasktagsTypeDef = TypedDict(
    "_ClientStopTaskResponsetasktagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientStopTaskResponsetasktagsTypeDef(_ClientStopTaskResponsetasktagsTypeDef):
    pass


_ClientStopTaskResponsetaskTypeDef = TypedDict(
    "_ClientStopTaskResponsetaskTypeDef",
    {
        "attachments": List[ClientStopTaskResponsetaskattachmentsTypeDef],
        "attributes": List[ClientStopTaskResponsetaskattributesTypeDef],
        "availabilityZone": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientStopTaskResponsetaskcontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientStopTaskResponsetaskoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientStopTaskResponsetasktagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)


class ClientStopTaskResponsetaskTypeDef(_ClientStopTaskResponsetaskTypeDef):
    """
    - **task** *(dict) --*

      The task that was stopped.
      - **attachments** *(list) --*

        The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network
        mode.
        - *(dict) --*

          An object representing a container instance or task attachment.
          - **id** *(string) --*

            The unique identifier for the attachment.
    """


_ClientStopTaskResponseTypeDef = TypedDict(
    "_ClientStopTaskResponseTypeDef", {"task": ClientStopTaskResponsetaskTypeDef}, total=False
)


class ClientStopTaskResponseTypeDef(_ClientStopTaskResponseTypeDef):
    """
    - *(dict) --*

      - **task** *(dict) --*

        The task that was stopped.
        - **attachments** *(list) --*

          The Elastic Network Adapter associated with the task if the task uses the ``awsvpc``
          network mode.
          - *(dict) --*

            An object representing a container instance or task attachment.
            - **id** *(string) --*

              The unique identifier for the attachment.
    """


_RequiredClientSubmitAttachmentStateChangesAttachmentsTypeDef = TypedDict(
    "_RequiredClientSubmitAttachmentStateChangesAttachmentsTypeDef", {"attachmentArn": str}
)
_OptionalClientSubmitAttachmentStateChangesAttachmentsTypeDef = TypedDict(
    "_OptionalClientSubmitAttachmentStateChangesAttachmentsTypeDef", {"status": str}, total=False
)


class ClientSubmitAttachmentStateChangesAttachmentsTypeDef(
    _RequiredClientSubmitAttachmentStateChangesAttachmentsTypeDef,
    _OptionalClientSubmitAttachmentStateChangesAttachmentsTypeDef,
):
    """
    - *(dict) --*

      An object representing a change in state for a task attachment.
      - **attachmentArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the attachment.
    """


_ClientSubmitAttachmentStateChangesResponseTypeDef = TypedDict(
    "_ClientSubmitAttachmentStateChangesResponseTypeDef", {"acknowledgment": str}, total=False
)


class ClientSubmitAttachmentStateChangesResponseTypeDef(
    _ClientSubmitAttachmentStateChangesResponseTypeDef
):
    """
    - *(dict) --*

      - **acknowledgment** *(string) --*

        Acknowledgement of the state change.
    """


_ClientSubmitContainerStateChangeNetworkBindingsTypeDef = TypedDict(
    "_ClientSubmitContainerStateChangeNetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientSubmitContainerStateChangeNetworkBindingsTypeDef(
    _ClientSubmitContainerStateChangeNetworkBindingsTypeDef
):
    """
    - *(dict) --*

      Details on the network bindings between a container and its host container instance. After a
      task reaches the ``RUNNING`` status, manual and automatic host and container port assignments
      are visible in the ``networkBindings`` section of  DescribeTasks API responses.
      - **bindIP** *(string) --*

        The IP address that the container is bound to on the container instance.
    """


_ClientSubmitContainerStateChangeResponseTypeDef = TypedDict(
    "_ClientSubmitContainerStateChangeResponseTypeDef", {"acknowledgment": str}, total=False
)


class ClientSubmitContainerStateChangeResponseTypeDef(
    _ClientSubmitContainerStateChangeResponseTypeDef
):
    """
    - *(dict) --*

      - **acknowledgment** *(string) --*

        Acknowledgement of the state change.
    """


_RequiredClientSubmitTaskStateChangeAttachmentsTypeDef = TypedDict(
    "_RequiredClientSubmitTaskStateChangeAttachmentsTypeDef", {"attachmentArn": str}
)
_OptionalClientSubmitTaskStateChangeAttachmentsTypeDef = TypedDict(
    "_OptionalClientSubmitTaskStateChangeAttachmentsTypeDef", {"status": str}, total=False
)


class ClientSubmitTaskStateChangeAttachmentsTypeDef(
    _RequiredClientSubmitTaskStateChangeAttachmentsTypeDef,
    _OptionalClientSubmitTaskStateChangeAttachmentsTypeDef,
):
    """
    - *(dict) --*

      An object representing a change in state for a task attachment.
      - **attachmentArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the attachment.
    """


_ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef = TypedDict(
    "_ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)


class ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef(
    _ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef
):
    pass


_ClientSubmitTaskStateChangeContainersTypeDef = TypedDict(
    "_ClientSubmitTaskStateChangeContainersTypeDef",
    {
        "containerName": str,
        "imageDigest": str,
        "runtimeId": str,
        "exitCode": int,
        "networkBindings": List[ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef],
        "reason": str,
        "status": str,
    },
    total=False,
)


class ClientSubmitTaskStateChangeContainersTypeDef(_ClientSubmitTaskStateChangeContainersTypeDef):
    """
    - *(dict) --*

      An object representing a change in state for a container.
      - **containerName** *(string) --*

        The name of the container.
    """


_ClientSubmitTaskStateChangeResponseTypeDef = TypedDict(
    "_ClientSubmitTaskStateChangeResponseTypeDef", {"acknowledgment": str}, total=False
)


class ClientSubmitTaskStateChangeResponseTypeDef(_ClientSubmitTaskStateChangeResponseTypeDef):
    """
    - *(dict) --*

      - **acknowledgment** *(string) --*

        Acknowledgement of the state change.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define.
      The following basic restrictions apply to tags:
      * Maximum number of tags per resource - 50
      * For each resource, each tag key must be unique, and each tag key can have only one value.
      * Maximum key length - 128 Unicode characters in UTF-8
      * Maximum value length - 256 Unicode characters in UTF-8
      * If your tagging schema is used across multiple services and resources, remember that other
      services may have restrictions on allowed characters. Generally allowed characters are:
      letters, numbers, and spaces representable in UTF-8, and the following characters: + - =
           . _ :
      / @.
      * Tag keys and values are case-sensitive.
      * Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix
      for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or
      values with this prefix. Tags with this prefix do not count against your tags per resource
      limit.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientUpdateClusterSettingsResponseclustersettingsTypeDef = TypedDict(
    "_ClientUpdateClusterSettingsResponseclustersettingsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientUpdateClusterSettingsResponseclustersettingsTypeDef(
    _ClientUpdateClusterSettingsResponseclustersettingsTypeDef
):
    pass


_ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef = TypedDict(
    "_ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef(
    _ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef
):
    pass


_ClientUpdateClusterSettingsResponseclustertagsTypeDef = TypedDict(
    "_ClientUpdateClusterSettingsResponseclustertagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateClusterSettingsResponseclustertagsTypeDef(
    _ClientUpdateClusterSettingsResponseclustertagsTypeDef
):
    pass


_ClientUpdateClusterSettingsResponseclusterTypeDef = TypedDict(
    "_ClientUpdateClusterSettingsResponseclusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef],
        "tags": List[ClientUpdateClusterSettingsResponseclustertagsTypeDef],
        "settings": List[ClientUpdateClusterSettingsResponseclustersettingsTypeDef],
    },
    total=False,
)


class ClientUpdateClusterSettingsResponseclusterTypeDef(
    _ClientUpdateClusterSettingsResponseclusterTypeDef
):
    """
    - **cluster** *(dict) --*

      A regional grouping of one or more container instances on which you can run task requests.
      Each account receives a default cluster the first time you use the Amazon ECS service, but you
      may also create other clusters. Clusters may contain more than one instance type
      simultaneously.
      - **clusterArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of the
        cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
        ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientUpdateClusterSettingsResponseTypeDef = TypedDict(
    "_ClientUpdateClusterSettingsResponseTypeDef",
    {"cluster": ClientUpdateClusterSettingsResponseclusterTypeDef},
    total=False,
)


class ClientUpdateClusterSettingsResponseTypeDef(_ClientUpdateClusterSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **cluster** *(dict) --*

        A regional grouping of one or more container instances on which you can run task requests.
        Each account receives a default cluster the first time you use the Amazon ECS service, but
        you may also create other clusters. Clusters may contain more than one instance type
        simultaneously.
        - **clusterArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the
          ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of
          the cluster owner, the ``cluster`` namespace, and then the cluster name. For example,
          ``arn:aws:ecs:region:012345678910:cluster/test`` .
    """


_ClientUpdateClusterSettingsSettingsTypeDef = TypedDict(
    "_ClientUpdateClusterSettingsSettingsTypeDef", {"name": str, "value": str}, total=False
)


class ClientUpdateClusterSettingsSettingsTypeDef(_ClientUpdateClusterSettingsSettingsTypeDef):
    """
    - *(dict) --*

      The settings to use when creating a cluster. This parameter is used to enable CloudWatch
      Container Insights for a cluster.
      - **name** *(string) --*

        The name of the cluster setting. The only supported value is ``containerInsights`` .
    """


_ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef
):
    pass


_ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef
):
    pass


_ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef
):
    pass


_ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef
):
    pass


_ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef
):
    pass


_ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef
):
    pass


_ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef
):
    pass


_ClientUpdateContainerAgentResponsecontainerInstanceTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponsecontainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "version": int,
        "versionInfo": ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef,
        "remainingResources": List[
            ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef],
        "registeredAt": datetime,
        "attachments": List[ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef],
        "tags": List[ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef],
    },
    total=False,
)


class ClientUpdateContainerAgentResponsecontainerInstanceTypeDef(
    _ClientUpdateContainerAgentResponsecontainerInstanceTypeDef
):
    """
    - **containerInstance** *(dict) --*

      The container instance for which the container agent was updated.
      - **containerInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the container instance. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account
        ID of the container instance owner, the ``container-instance`` namespace, and then the
        container instance ID. For example,
        ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientUpdateContainerAgentResponseTypeDef = TypedDict(
    "_ClientUpdateContainerAgentResponseTypeDef",
    {"containerInstance": ClientUpdateContainerAgentResponsecontainerInstanceTypeDef},
    total=False,
)


class ClientUpdateContainerAgentResponseTypeDef(_ClientUpdateContainerAgentResponseTypeDef):
    """
    - *(dict) --*

      - **containerInstance** *(dict) --*

        The container instance for which the container agent was updated.
        - **containerInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the container instance. The ARN contains the
          ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS
          account ID of the container instance owner, the ``container-instance`` namespace, and then
          the container instance ID. For example,
          ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "version": int,
        "versionInfo": ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef,
        "remainingResources": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef
        ],
        "tags": List[ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef],
    },
    total=False,
)


class ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef(
    _ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef
):
    """
    - *(dict) --*

      An EC2 instance that is running the Amazon ECS agent and has been registered with a cluster.
      - **containerInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the container instance. The ARN contains the
        ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account
        ID of the container instance owner, the ``container-instance`` namespace, and then the
        container instance ID. For example,
        ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientUpdateContainerInstancesStateResponsefailuresTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)


class ClientUpdateContainerInstancesStateResponsefailuresTypeDef(
    _ClientUpdateContainerInstancesStateResponsefailuresTypeDef
):
    pass


_ClientUpdateContainerInstancesStateResponseTypeDef = TypedDict(
    "_ClientUpdateContainerInstancesStateResponseTypeDef",
    {
        "containerInstances": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef
        ],
        "failures": List[ClientUpdateContainerInstancesStateResponsefailuresTypeDef],
    },
    total=False,
)


class ClientUpdateContainerInstancesStateResponseTypeDef(
    _ClientUpdateContainerInstancesStateResponseTypeDef
):
    """
    - *(dict) --*

      - **containerInstances** *(list) --*

        The list of container instances.
        - *(dict) --*

          An EC2 instance that is running the Amazon ECS agent and has been registered with a
          cluster.
          - **containerInstanceArn** *(string) --*

            The Amazon Resource Name (ARN) of the container instance. The ARN contains the
            ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS
            account ID of the container instance owner, the ``container-instance`` namespace, and
            then the container instance ID. For example,
            ``arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID`` .
    """


_ClientUpdateServiceDeploymentConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceDeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)


class ClientUpdateServiceDeploymentConfigurationTypeDef(
    _ClientUpdateServiceDeploymentConfigurationTypeDef
):
    """
    Optional deployment parameters that control how many tasks run during the deployment and the
    ordering of stopping and starting tasks.
    - **maximumPercent** *(integer) --*

      If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent**
      parameter represents an upper limit on the number of tasks in a service that are allowed in
      the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired
      number of tasks (rounded down to the nearest integer), and while any container instances are
      in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This
      parameter enables you to define the deployment batch size. For example, if your service has a
      desired number of four tasks and a maximum percent value of 200%, the scheduler may start four
      new tasks before stopping the four older tasks (provided that the cluster resources required
      to do this are available). The default value for maximum percent is 200%.
      If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and
      tasks that use the EC2 launch type, the **maximum percent** value is set to the default value
      and is used to define the upper limit on the number of the tasks in the service that remain in
      the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the
      tasks in the service use the Fargate launch type, the maximum percent value is not used,
      although it is returned when describing your service.
    """


_ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientUpdateServiceNetworkConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)


class ClientUpdateServiceNetworkConfigurationTypeDef(
    _ClientUpdateServiceNetworkConfigurationTypeDef
):
    """
    The network configuration for the service. This parameter is required for task definitions that
    use the ``awsvpc`` network mode to receive their own elastic network interface, and it is not
    supported for other network modes. For more information, see `Task Networking
    <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the
    *Amazon Elastic Container Service Developer Guide* .
    .. note::

      Updating a service to add a subnet to a list of existing subnets does not trigger a service
      deployment. For example, if your network configuration change is to keep the existing subnets
      and simply add another subnet to the network configuration, this does not trigger a new
      service deployment.
    """


_ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "_ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef(
    _ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef
):
    pass


_ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "_ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef(
    _ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef
):
    pass


_ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "_ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)


class ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef(
    _ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef
):
    pass


_ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "_ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef(
    _ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef
):
    pass


_ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef = TypedDict(
    "_ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef
        ],
        "scale": ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef(
    _ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef
):
    """
    - **taskSet** *(dict) --*

      Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
      deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
      many tasks are running, and whether the task set serves production traffic.
      - **id** *(string) --*

        The ID of the task set.
    """


_ClientUpdateServicePrimaryTaskSetResponseTypeDef = TypedDict(
    "_ClientUpdateServicePrimaryTaskSetResponseTypeDef",
    {"taskSet": ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef},
    total=False,
)


class ClientUpdateServicePrimaryTaskSetResponseTypeDef(
    _ClientUpdateServicePrimaryTaskSetResponseTypeDef
):
    """
    - *(dict) --*

      - **taskSet** *(dict) --*

        Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
        deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
        many tasks are running, and whether the task set serves production traffic.
        - **id** *(string) --*

          The ID of the task set.
    """


_ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)


class ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef(
    _ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef
):
    pass


_ClientUpdateServiceResponseservicedeploymentControllerTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicedeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)


class ClientUpdateServiceResponseservicedeploymentControllerTypeDef(
    _ClientUpdateServiceResponseservicedeploymentControllerTypeDef
):
    pass


_ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef(
    _ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef
):
    pass


_ClientUpdateServiceResponseservicedeploymentsTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicedeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateServiceResponseservicedeploymentsTypeDef(
    _ClientUpdateServiceResponseservicedeploymentsTypeDef
):
    pass


_ClientUpdateServiceResponseserviceeventsTypeDef = TypedDict(
    "_ClientUpdateServiceResponseserviceeventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)


class ClientUpdateServiceResponseserviceeventsTypeDef(
    _ClientUpdateServiceResponseserviceeventsTypeDef
):
    pass


_ClientUpdateServiceResponseserviceloadBalancersTypeDef = TypedDict(
    "_ClientUpdateServiceResponseserviceloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateServiceResponseserviceloadBalancersTypeDef(
    _ClientUpdateServiceResponseserviceloadBalancersTypeDef
):
    pass


_ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientUpdateServiceResponseservicenetworkConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicenetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateServiceResponseservicenetworkConfigurationTypeDef(
    _ClientUpdateServiceResponseservicenetworkConfigurationTypeDef
):
    pass


_ClientUpdateServiceResponseserviceplacementConstraintsTypeDef = TypedDict(
    "_ClientUpdateServiceResponseserviceplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)


class ClientUpdateServiceResponseserviceplacementConstraintsTypeDef(
    _ClientUpdateServiceResponseserviceplacementConstraintsTypeDef
):
    pass


_ClientUpdateServiceResponseserviceplacementStrategyTypeDef = TypedDict(
    "_ClientUpdateServiceResponseserviceplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)


class ClientUpdateServiceResponseserviceplacementStrategyTypeDef(
    _ClientUpdateServiceResponseserviceplacementStrategyTypeDef
):
    pass


_ClientUpdateServiceResponseserviceserviceRegistriesTypeDef = TypedDict(
    "_ClientUpdateServiceResponseserviceserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateServiceResponseserviceserviceRegistriesTypeDef(
    _ClientUpdateServiceResponseserviceserviceRegistriesTypeDef
):
    pass


_ClientUpdateServiceResponseservicetagsTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateServiceResponseservicetagsTypeDef(_ClientUpdateServiceResponseservicetagsTypeDef):
    pass


_ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef(
    _ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef
):
    pass


_ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef(
    _ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef
):
    pass


_ClientUpdateServiceResponseservicetaskSetsscaleTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicetaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)


class ClientUpdateServiceResponseservicetaskSetsscaleTypeDef(
    _ClientUpdateServiceResponseservicetaskSetsscaleTypeDef
):
    pass


_ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef(
    _ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef
):
    pass


_ClientUpdateServiceResponseservicetaskSetsTypeDef = TypedDict(
    "_ClientUpdateServiceResponseservicetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientUpdateServiceResponseservicetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientUpdateServiceResponseservicetaskSetsTypeDef(
    _ClientUpdateServiceResponseservicetaskSetsTypeDef
):
    pass


_ClientUpdateServiceResponseserviceTypeDef = TypedDict(
    "_ClientUpdateServiceResponseserviceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientUpdateServiceResponseserviceloadBalancersTypeDef],
        "serviceRegistries": List[ClientUpdateServiceResponseserviceserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef,
        "taskSets": List[ClientUpdateServiceResponseservicetaskSetsTypeDef],
        "deployments": List[ClientUpdateServiceResponseservicedeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientUpdateServiceResponseserviceeventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[ClientUpdateServiceResponseserviceplacementConstraintsTypeDef],
        "placementStrategy": List[ClientUpdateServiceResponseserviceplacementStrategyTypeDef],
        "networkConfiguration": ClientUpdateServiceResponseservicenetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientUpdateServiceResponseservicedeploymentControllerTypeDef,
        "tags": List[ClientUpdateServiceResponseservicetagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)


class ClientUpdateServiceResponseserviceTypeDef(_ClientUpdateServiceResponseserviceTypeDef):
    """
    - **service** *(dict) --*

      The full description of your service following the update call.
      - **serviceArn** *(string) --*

        The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
        followed by the Region of the service, the AWS account ID of the service owner, the
        ``service`` namespace, and then the service name. For example,
        ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientUpdateServiceResponseTypeDef = TypedDict(
    "_ClientUpdateServiceResponseTypeDef",
    {"service": ClientUpdateServiceResponseserviceTypeDef},
    total=False,
)


class ClientUpdateServiceResponseTypeDef(_ClientUpdateServiceResponseTypeDef):
    """
    - *(dict) --*

      - **service** *(dict) --*

        The full description of your service following the update call.
        - **serviceArn** *(string) --*

          The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace,
          followed by the Region of the service, the AWS account ID of the service owner, the
          ``service`` namespace, and then the service name. For example,
          ``arn:aws:ecs:region:012345678910:service/my-service`` .
    """


_ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "_ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef(
    _ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef
):
    pass


_ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "_ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef(
    _ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef
):
    pass


_ClientUpdateTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "_ClientUpdateTaskSetResponsetaskSetscaleTypeDef", {"value": float, "unit": str}, total=False
)


class ClientUpdateTaskSetResponsetaskSetscaleTypeDef(
    _ClientUpdateTaskSetResponsetaskSetscaleTypeDef
):
    pass


_ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "_ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)


class ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef(
    _ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef
):
    pass


_ClientUpdateTaskSetResponsetaskSetTypeDef = TypedDict(
    "_ClientUpdateTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef],
        "scale": ClientUpdateTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
    },
    total=False,
)


class ClientUpdateTaskSetResponsetaskSetTypeDef(_ClientUpdateTaskSetResponsetaskSetTypeDef):
    """
    - **taskSet** *(dict) --*

      Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
      deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
      many tasks are running, and whether the task set serves production traffic.
      - **id** *(string) --*

        The ID of the task set.
    """


_ClientUpdateTaskSetResponseTypeDef = TypedDict(
    "_ClientUpdateTaskSetResponseTypeDef",
    {"taskSet": ClientUpdateTaskSetResponsetaskSetTypeDef},
    total=False,
)


class ClientUpdateTaskSetResponseTypeDef(_ClientUpdateTaskSetResponseTypeDef):
    """
    - *(dict) --*

      - **taskSet** *(dict) --*

        Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL``
        deployment. An Amazon ECS task set includes details such as the desired number of tasks, how
        many tasks are running, and whether the task set serves production traffic.
        - **id** *(string) --*

          The ID of the task set.
    """


_ClientUpdateTaskSetScaleTypeDef = TypedDict(
    "_ClientUpdateTaskSetScaleTypeDef", {"value": float, "unit": str}, total=False
)


class ClientUpdateTaskSetScaleTypeDef(_ClientUpdateTaskSetScaleTypeDef):
    """
    A floating-point percentage of the desired number of tasks to place and keep running in the task
    set.
    - **value** *(float) --*

      The value, specified as a percent total of a service's ``desiredCount`` , to scale the task
      set. Accepted values are numbers between 0 and 100.
    """


_ListAccountSettingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountSettingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountSettingsPaginatePaginationConfigTypeDef(
    _ListAccountSettingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAccountSettingsPaginateResponsesettingsTypeDef = TypedDict(
    "_ListAccountSettingsPaginateResponsesettingsTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)


class ListAccountSettingsPaginateResponsesettingsTypeDef(
    _ListAccountSettingsPaginateResponsesettingsTypeDef
):
    """
    - *(dict) --*

      The current account setting for a resource.
      - **name** *(string) --*

        The Amazon ECS resource name.
    """


_ListAccountSettingsPaginateResponseTypeDef = TypedDict(
    "_ListAccountSettingsPaginateResponseTypeDef",
    {"settings": List[ListAccountSettingsPaginateResponsesettingsTypeDef], "NextToken": str},
    total=False,
)


class ListAccountSettingsPaginateResponseTypeDef(_ListAccountSettingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **settings** *(list) --*

        The account settings for the resource.
        - *(dict) --*

          The current account setting for a resource.
          - **name** *(string) --*

            The Amazon ECS resource name.
    """


_ListAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttributesPaginatePaginationConfigTypeDef(_ListAttributesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAttributesPaginateResponseattributesTypeDef = TypedDict(
    "_ListAttributesPaginateResponseattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)


class ListAttributesPaginateResponseattributesTypeDef(
    _ListAttributesPaginateResponseattributesTypeDef
):
    """
    - *(dict) --*

      An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you
      to extend the Amazon ECS data model by adding custom metadata to your resources. For more
      information, see `Attributes
      <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
      in the *Amazon Elastic Container Service Developer Guide* .
      - **name** *(string) --*

        The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens,
        underscores, and periods are allowed.
    """


_ListAttributesPaginateResponseTypeDef = TypedDict(
    "_ListAttributesPaginateResponseTypeDef",
    {"attributes": List[ListAttributesPaginateResponseattributesTypeDef], "NextToken": str},
    total=False,
)


class ListAttributesPaginateResponseTypeDef(_ListAttributesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **attributes** *(list) --*

        A list of attribute objects that meet the criteria of the request.
        - *(dict) --*

          An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable
          you to extend the Amazon ECS data model by adding custom metadata to your resources. For
          more information, see `Attributes
          <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__
          in the *Amazon Elastic Container Service Developer Guide* .
          - **name** *(string) --*

            The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers,
            hyphens, underscores, and periods are allowed.
    """


_ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClustersPaginatePaginationConfigTypeDef(_ListClustersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"clusterArns": List[str], "NextToken": str},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **clusterArns** *(list) --*

        The list of full Amazon Resource Name (ARN) entries for each cluster associated with your
        account.
        - *(string) --*
    """


_ListContainerInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListContainerInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListContainerInstancesPaginatePaginationConfigTypeDef(
    _ListContainerInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListContainerInstancesPaginateResponseTypeDef = TypedDict(
    "_ListContainerInstancesPaginateResponseTypeDef",
    {"containerInstanceArns": List[str], "NextToken": str},
    total=False,
)


class ListContainerInstancesPaginateResponseTypeDef(_ListContainerInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **containerInstanceArns** *(list) --*

        The list of container instances with full ARN entries for each container instance associated
        with the specified cluster.
        - *(string) --*
    """


_ListServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServicesPaginatePaginationConfigTypeDef(_ListServicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServicesPaginateResponseTypeDef = TypedDict(
    "_ListServicesPaginateResponseTypeDef",
    {"serviceArns": List[str], "NextToken": str},
    total=False,
)


class ListServicesPaginateResponseTypeDef(_ListServicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **serviceArns** *(list) --*

        The list of full ARN entries for each service associated with the specified cluster.
        - *(string) --*
    """


_ListTaskDefinitionFamiliesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTaskDefinitionFamiliesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTaskDefinitionFamiliesPaginatePaginationConfigTypeDef(
    _ListTaskDefinitionFamiliesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTaskDefinitionFamiliesPaginateResponseTypeDef = TypedDict(
    "_ListTaskDefinitionFamiliesPaginateResponseTypeDef",
    {"families": List[str], "NextToken": str},
    total=False,
)


class ListTaskDefinitionFamiliesPaginateResponseTypeDef(
    _ListTaskDefinitionFamiliesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **families** *(list) --*

        The list of task definition family names that match the ``ListTaskDefinitionFamilies``
        request.
        - *(string) --*
    """


_ListTaskDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTaskDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTaskDefinitionsPaginatePaginationConfigTypeDef(
    _ListTaskDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTaskDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListTaskDefinitionsPaginateResponseTypeDef",
    {"taskDefinitionArns": List[str], "NextToken": str},
    total=False,
)


class ListTaskDefinitionsPaginateResponseTypeDef(_ListTaskDefinitionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **taskDefinitionArns** *(list) --*

        The list of task definition Amazon Resource Name (ARN) entries for the
        ``ListTaskDefinitions`` request.
        - *(string) --*
    """


_ListTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTasksPaginatePaginationConfigTypeDef(_ListTasksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTasksPaginateResponseTypeDef = TypedDict(
    "_ListTasksPaginateResponseTypeDef", {"taskArns": List[str], "NextToken": str}, total=False
)


class ListTasksPaginateResponseTypeDef(_ListTasksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **taskArns** *(list) --*

        The list of task ARN entries for the ``ListTasks`` request.
        - *(string) --*
    """


_ServicesInactiveWaitWaiterConfigTypeDef = TypedDict(
    "_ServicesInactiveWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ServicesInactiveWaitWaiterConfigTypeDef(_ServicesInactiveWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_ServicesStableWaitWaiterConfigTypeDef = TypedDict(
    "_ServicesStableWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ServicesStableWaitWaiterConfigTypeDef(_ServicesStableWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_TasksRunningWaitWaiterConfigTypeDef = TypedDict(
    "_TasksRunningWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class TasksRunningWaitWaiterConfigTypeDef(_TasksRunningWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 6
    """


_TasksStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_TasksStoppedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class TasksStoppedWaitWaiterConfigTypeDef(_TasksStoppedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 6
    """
