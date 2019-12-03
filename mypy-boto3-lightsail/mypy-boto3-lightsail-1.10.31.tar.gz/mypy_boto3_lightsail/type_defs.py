"Main interface for lightsail service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAllocateStaticIpResponseoperationslocationTypeDef",
    "ClientAllocateStaticIpResponseoperationsTypeDef",
    "ClientAllocateStaticIpResponseTypeDef",
    "ClientAttachDiskResponseoperationslocationTypeDef",
    "ClientAttachDiskResponseoperationsTypeDef",
    "ClientAttachDiskResponseTypeDef",
    "ClientAttachInstancesToLoadBalancerResponseoperationslocationTypeDef",
    "ClientAttachInstancesToLoadBalancerResponseoperationsTypeDef",
    "ClientAttachInstancesToLoadBalancerResponseTypeDef",
    "ClientAttachLoadBalancerTlsCertificateResponseoperationslocationTypeDef",
    "ClientAttachLoadBalancerTlsCertificateResponseoperationsTypeDef",
    "ClientAttachLoadBalancerTlsCertificateResponseTypeDef",
    "ClientAttachStaticIpResponseoperationslocationTypeDef",
    "ClientAttachStaticIpResponseoperationsTypeDef",
    "ClientAttachStaticIpResponseTypeDef",
    "ClientCloseInstancePublicPortsPortInfoTypeDef",
    "ClientCloseInstancePublicPortsResponseoperationlocationTypeDef",
    "ClientCloseInstancePublicPortsResponseoperationTypeDef",
    "ClientCloseInstancePublicPortsResponseTypeDef",
    "ClientCopySnapshotResponseoperationslocationTypeDef",
    "ClientCopySnapshotResponseoperationsTypeDef",
    "ClientCopySnapshotResponseTypeDef",
    "ClientCreateCloudFormationStackInstancesTypeDef",
    "ClientCreateCloudFormationStackResponseoperationslocationTypeDef",
    "ClientCreateCloudFormationStackResponseoperationsTypeDef",
    "ClientCreateCloudFormationStackResponseTypeDef",
    "ClientCreateDiskAddOnsautoSnapshotAddOnRequestTypeDef",
    "ClientCreateDiskAddOnsTypeDef",
    "ClientCreateDiskFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef",
    "ClientCreateDiskFromSnapshotAddOnsTypeDef",
    "ClientCreateDiskFromSnapshotResponseoperationslocationTypeDef",
    "ClientCreateDiskFromSnapshotResponseoperationsTypeDef",
    "ClientCreateDiskFromSnapshotResponseTypeDef",
    "ClientCreateDiskFromSnapshotTagsTypeDef",
    "ClientCreateDiskResponseoperationslocationTypeDef",
    "ClientCreateDiskResponseoperationsTypeDef",
    "ClientCreateDiskResponseTypeDef",
    "ClientCreateDiskSnapshotResponseoperationslocationTypeDef",
    "ClientCreateDiskSnapshotResponseoperationsTypeDef",
    "ClientCreateDiskSnapshotResponseTypeDef",
    "ClientCreateDiskSnapshotTagsTypeDef",
    "ClientCreateDiskTagsTypeDef",
    "ClientCreateDomainEntryDomainEntryTypeDef",
    "ClientCreateDomainEntryResponseoperationlocationTypeDef",
    "ClientCreateDomainEntryResponseoperationTypeDef",
    "ClientCreateDomainEntryResponseTypeDef",
    "ClientCreateDomainResponseoperationlocationTypeDef",
    "ClientCreateDomainResponseoperationTypeDef",
    "ClientCreateDomainResponseTypeDef",
    "ClientCreateDomainTagsTypeDef",
    "ClientCreateInstanceSnapshotResponseoperationslocationTypeDef",
    "ClientCreateInstanceSnapshotResponseoperationsTypeDef",
    "ClientCreateInstanceSnapshotResponseTypeDef",
    "ClientCreateInstanceSnapshotTagsTypeDef",
    "ClientCreateInstancesAddOnsautoSnapshotAddOnRequestTypeDef",
    "ClientCreateInstancesAddOnsTypeDef",
    "ClientCreateInstancesFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef",
    "ClientCreateInstancesFromSnapshotAddOnsTypeDef",
    "ClientCreateInstancesFromSnapshotAttachedDiskMappingTypeDef",
    "ClientCreateInstancesFromSnapshotResponseoperationslocationTypeDef",
    "ClientCreateInstancesFromSnapshotResponseoperationsTypeDef",
    "ClientCreateInstancesFromSnapshotResponseTypeDef",
    "ClientCreateInstancesFromSnapshotTagsTypeDef",
    "ClientCreateInstancesResponseoperationslocationTypeDef",
    "ClientCreateInstancesResponseoperationsTypeDef",
    "ClientCreateInstancesResponseTypeDef",
    "ClientCreateInstancesTagsTypeDef",
    "ClientCreateKeyPairResponsekeyPairlocationTypeDef",
    "ClientCreateKeyPairResponsekeyPairtagsTypeDef",
    "ClientCreateKeyPairResponsekeyPairTypeDef",
    "ClientCreateKeyPairResponseoperationlocationTypeDef",
    "ClientCreateKeyPairResponseoperationTypeDef",
    "ClientCreateKeyPairResponseTypeDef",
    "ClientCreateKeyPairTagsTypeDef",
    "ClientCreateLoadBalancerResponseoperationslocationTypeDef",
    "ClientCreateLoadBalancerResponseoperationsTypeDef",
    "ClientCreateLoadBalancerResponseTypeDef",
    "ClientCreateLoadBalancerTagsTypeDef",
    "ClientCreateLoadBalancerTlsCertificateResponseoperationslocationTypeDef",
    "ClientCreateLoadBalancerTlsCertificateResponseoperationsTypeDef",
    "ClientCreateLoadBalancerTlsCertificateResponseTypeDef",
    "ClientCreateLoadBalancerTlsCertificateTagsTypeDef",
    "ClientCreateRelationalDatabaseFromSnapshotResponseoperationslocationTypeDef",
    "ClientCreateRelationalDatabaseFromSnapshotResponseoperationsTypeDef",
    "ClientCreateRelationalDatabaseFromSnapshotResponseTypeDef",
    "ClientCreateRelationalDatabaseFromSnapshotTagsTypeDef",
    "ClientCreateRelationalDatabaseResponseoperationslocationTypeDef",
    "ClientCreateRelationalDatabaseResponseoperationsTypeDef",
    "ClientCreateRelationalDatabaseResponseTypeDef",
    "ClientCreateRelationalDatabaseSnapshotResponseoperationslocationTypeDef",
    "ClientCreateRelationalDatabaseSnapshotResponseoperationsTypeDef",
    "ClientCreateRelationalDatabaseSnapshotResponseTypeDef",
    "ClientCreateRelationalDatabaseSnapshotTagsTypeDef",
    "ClientCreateRelationalDatabaseTagsTypeDef",
    "ClientDeleteAutoSnapshotResponseoperationslocationTypeDef",
    "ClientDeleteAutoSnapshotResponseoperationsTypeDef",
    "ClientDeleteAutoSnapshotResponseTypeDef",
    "ClientDeleteDiskResponseoperationslocationTypeDef",
    "ClientDeleteDiskResponseoperationsTypeDef",
    "ClientDeleteDiskResponseTypeDef",
    "ClientDeleteDiskSnapshotResponseoperationslocationTypeDef",
    "ClientDeleteDiskSnapshotResponseoperationsTypeDef",
    "ClientDeleteDiskSnapshotResponseTypeDef",
    "ClientDeleteDomainEntryDomainEntryTypeDef",
    "ClientDeleteDomainEntryResponseoperationlocationTypeDef",
    "ClientDeleteDomainEntryResponseoperationTypeDef",
    "ClientDeleteDomainEntryResponseTypeDef",
    "ClientDeleteDomainResponseoperationlocationTypeDef",
    "ClientDeleteDomainResponseoperationTypeDef",
    "ClientDeleteDomainResponseTypeDef",
    "ClientDeleteInstanceResponseoperationslocationTypeDef",
    "ClientDeleteInstanceResponseoperationsTypeDef",
    "ClientDeleteInstanceResponseTypeDef",
    "ClientDeleteInstanceSnapshotResponseoperationslocationTypeDef",
    "ClientDeleteInstanceSnapshotResponseoperationsTypeDef",
    "ClientDeleteInstanceSnapshotResponseTypeDef",
    "ClientDeleteKeyPairResponseoperationlocationTypeDef",
    "ClientDeleteKeyPairResponseoperationTypeDef",
    "ClientDeleteKeyPairResponseTypeDef",
    "ClientDeleteKnownHostKeysResponseoperationslocationTypeDef",
    "ClientDeleteKnownHostKeysResponseoperationsTypeDef",
    "ClientDeleteKnownHostKeysResponseTypeDef",
    "ClientDeleteLoadBalancerResponseoperationslocationTypeDef",
    "ClientDeleteLoadBalancerResponseoperationsTypeDef",
    "ClientDeleteLoadBalancerResponseTypeDef",
    "ClientDeleteLoadBalancerTlsCertificateResponseoperationslocationTypeDef",
    "ClientDeleteLoadBalancerTlsCertificateResponseoperationsTypeDef",
    "ClientDeleteLoadBalancerTlsCertificateResponseTypeDef",
    "ClientDeleteRelationalDatabaseResponseoperationslocationTypeDef",
    "ClientDeleteRelationalDatabaseResponseoperationsTypeDef",
    "ClientDeleteRelationalDatabaseResponseTypeDef",
    "ClientDeleteRelationalDatabaseSnapshotResponseoperationslocationTypeDef",
    "ClientDeleteRelationalDatabaseSnapshotResponseoperationsTypeDef",
    "ClientDeleteRelationalDatabaseSnapshotResponseTypeDef",
    "ClientDetachDiskResponseoperationslocationTypeDef",
    "ClientDetachDiskResponseoperationsTypeDef",
    "ClientDetachDiskResponseTypeDef",
    "ClientDetachInstancesFromLoadBalancerResponseoperationslocationTypeDef",
    "ClientDetachInstancesFromLoadBalancerResponseoperationsTypeDef",
    "ClientDetachInstancesFromLoadBalancerResponseTypeDef",
    "ClientDetachStaticIpResponseoperationslocationTypeDef",
    "ClientDetachStaticIpResponseoperationsTypeDef",
    "ClientDetachStaticIpResponseTypeDef",
    "ClientDisableAddOnResponseoperationslocationTypeDef",
    "ClientDisableAddOnResponseoperationsTypeDef",
    "ClientDisableAddOnResponseTypeDef",
    "ClientDownloadDefaultKeyPairResponseTypeDef",
    "ClientEnableAddOnAddOnRequestautoSnapshotAddOnRequestTypeDef",
    "ClientEnableAddOnAddOnRequestTypeDef",
    "ClientEnableAddOnResponseoperationslocationTypeDef",
    "ClientEnableAddOnResponseoperationsTypeDef",
    "ClientEnableAddOnResponseTypeDef",
    "ClientExportSnapshotResponseoperationslocationTypeDef",
    "ClientExportSnapshotResponseoperationsTypeDef",
    "ClientExportSnapshotResponseTypeDef",
    "ClientGetActiveNamesResponseTypeDef",
    "ClientGetAutoSnapshotsResponseautoSnapshotsfromAttachedDisksTypeDef",
    "ClientGetAutoSnapshotsResponseautoSnapshotsTypeDef",
    "ClientGetAutoSnapshotsResponseTypeDef",
    "ClientGetBlueprintsResponseblueprintsTypeDef",
    "ClientGetBlueprintsResponseTypeDef",
    "ClientGetBundlesResponsebundlesTypeDef",
    "ClientGetBundlesResponseTypeDef",
    "ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsdestinationInfoTypeDef",
    "ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordslocationTypeDef",
    "ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordssourceInfoTypeDef",
    "ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsTypeDef",
    "ClientGetCloudFormationStackRecordsResponseTypeDef",
    "ClientGetDiskResponsediskaddOnsTypeDef",
    "ClientGetDiskResponsedisklocationTypeDef",
    "ClientGetDiskResponsedisktagsTypeDef",
    "ClientGetDiskResponsediskTypeDef",
    "ClientGetDiskResponseTypeDef",
    "ClientGetDiskSnapshotResponsediskSnapshotlocationTypeDef",
    "ClientGetDiskSnapshotResponsediskSnapshottagsTypeDef",
    "ClientGetDiskSnapshotResponsediskSnapshotTypeDef",
    "ClientGetDiskSnapshotResponseTypeDef",
    "ClientGetDiskSnapshotsResponsediskSnapshotslocationTypeDef",
    "ClientGetDiskSnapshotsResponsediskSnapshotstagsTypeDef",
    "ClientGetDiskSnapshotsResponsediskSnapshotsTypeDef",
    "ClientGetDiskSnapshotsResponseTypeDef",
    "ClientGetDisksResponsedisksaddOnsTypeDef",
    "ClientGetDisksResponsediskslocationTypeDef",
    "ClientGetDisksResponsediskstagsTypeDef",
    "ClientGetDisksResponsedisksTypeDef",
    "ClientGetDisksResponseTypeDef",
    "ClientGetDomainResponsedomaindomainEntriesTypeDef",
    "ClientGetDomainResponsedomainlocationTypeDef",
    "ClientGetDomainResponsedomaintagsTypeDef",
    "ClientGetDomainResponsedomainTypeDef",
    "ClientGetDomainResponseTypeDef",
    "ClientGetDomainsResponsedomainsdomainEntriesTypeDef",
    "ClientGetDomainsResponsedomainslocationTypeDef",
    "ClientGetDomainsResponsedomainstagsTypeDef",
    "ClientGetDomainsResponsedomainsTypeDef",
    "ClientGetDomainsResponseTypeDef",
    "ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsdestinationInfoTypeDef",
    "ClientGetExportSnapshotRecordsResponseexportSnapshotRecordslocationTypeDef",
    "ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef",
    "ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef",
    "ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef",
    "ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoTypeDef",
    "ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsTypeDef",
    "ClientGetExportSnapshotRecordsResponseTypeDef",
    "ClientGetInstanceAccessDetailsResponseaccessDetailshostKeysTypeDef",
    "ClientGetInstanceAccessDetailsResponseaccessDetailspasswordDataTypeDef",
    "ClientGetInstanceAccessDetailsResponseaccessDetailsTypeDef",
    "ClientGetInstanceAccessDetailsResponseTypeDef",
    "ClientGetInstanceMetricDataResponsemetricDataTypeDef",
    "ClientGetInstanceMetricDataResponseTypeDef",
    "ClientGetInstancePortStatesResponseportStatesTypeDef",
    "ClientGetInstancePortStatesResponseTypeDef",
    "ClientGetInstanceResponseinstanceaddOnsTypeDef",
    "ClientGetInstanceResponseinstancehardwaredisksaddOnsTypeDef",
    "ClientGetInstanceResponseinstancehardwarediskslocationTypeDef",
    "ClientGetInstanceResponseinstancehardwarediskstagsTypeDef",
    "ClientGetInstanceResponseinstancehardwaredisksTypeDef",
    "ClientGetInstanceResponseinstancehardwareTypeDef",
    "ClientGetInstanceResponseinstancelocationTypeDef",
    "ClientGetInstanceResponseinstancenetworkingmonthlyTransferTypeDef",
    "ClientGetInstanceResponseinstancenetworkingportsTypeDef",
    "ClientGetInstanceResponseinstancenetworkingTypeDef",
    "ClientGetInstanceResponseinstancestateTypeDef",
    "ClientGetInstanceResponseinstancetagsTypeDef",
    "ClientGetInstanceResponseinstanceTypeDef",
    "ClientGetInstanceResponseTypeDef",
    "ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksaddOnsTypeDef",
    "ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskslocationTypeDef",
    "ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskstagsTypeDef",
    "ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksTypeDef",
    "ClientGetInstanceSnapshotResponseinstanceSnapshotlocationTypeDef",
    "ClientGetInstanceSnapshotResponseinstanceSnapshottagsTypeDef",
    "ClientGetInstanceSnapshotResponseinstanceSnapshotTypeDef",
    "ClientGetInstanceSnapshotResponseTypeDef",
    "ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef",
    "ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef",
    "ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef",
    "ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksTypeDef",
    "ClientGetInstanceSnapshotsResponseinstanceSnapshotslocationTypeDef",
    "ClientGetInstanceSnapshotsResponseinstanceSnapshotstagsTypeDef",
    "ClientGetInstanceSnapshotsResponseinstanceSnapshotsTypeDef",
    "ClientGetInstanceSnapshotsResponseTypeDef",
    "ClientGetInstanceStateResponsestateTypeDef",
    "ClientGetInstanceStateResponseTypeDef",
    "ClientGetInstancesResponseinstancesaddOnsTypeDef",
    "ClientGetInstancesResponseinstanceshardwaredisksaddOnsTypeDef",
    "ClientGetInstancesResponseinstanceshardwarediskslocationTypeDef",
    "ClientGetInstancesResponseinstanceshardwarediskstagsTypeDef",
    "ClientGetInstancesResponseinstanceshardwaredisksTypeDef",
    "ClientGetInstancesResponseinstanceshardwareTypeDef",
    "ClientGetInstancesResponseinstanceslocationTypeDef",
    "ClientGetInstancesResponseinstancesnetworkingmonthlyTransferTypeDef",
    "ClientGetInstancesResponseinstancesnetworkingportsTypeDef",
    "ClientGetInstancesResponseinstancesnetworkingTypeDef",
    "ClientGetInstancesResponseinstancesstateTypeDef",
    "ClientGetInstancesResponseinstancestagsTypeDef",
    "ClientGetInstancesResponseinstancesTypeDef",
    "ClientGetInstancesResponseTypeDef",
    "ClientGetKeyPairResponsekeyPairlocationTypeDef",
    "ClientGetKeyPairResponsekeyPairtagsTypeDef",
    "ClientGetKeyPairResponsekeyPairTypeDef",
    "ClientGetKeyPairResponseTypeDef",
    "ClientGetKeyPairsResponsekeyPairslocationTypeDef",
    "ClientGetKeyPairsResponsekeyPairstagsTypeDef",
    "ClientGetKeyPairsResponsekeyPairsTypeDef",
    "ClientGetKeyPairsResponseTypeDef",
    "ClientGetLoadBalancerMetricDataResponsemetricDataTypeDef",
    "ClientGetLoadBalancerMetricDataResponseTypeDef",
    "ClientGetLoadBalancerResponseloadBalancerinstanceHealthSummaryTypeDef",
    "ClientGetLoadBalancerResponseloadBalancerlocationTypeDef",
    "ClientGetLoadBalancerResponseloadBalancertagsTypeDef",
    "ClientGetLoadBalancerResponseloadBalancertlsCertificateSummariesTypeDef",
    "ClientGetLoadBalancerResponseloadBalancerTypeDef",
    "ClientGetLoadBalancerResponseTypeDef",
    "ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesdomainValidationRecordsTypeDef",
    "ClientGetLoadBalancerTlsCertificatesResponsetlsCertificateslocationTypeDef",
    "ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummarydomainValidationOptionsTypeDef",
    "ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummaryTypeDef",
    "ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatestagsTypeDef",
    "ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesTypeDef",
    "ClientGetLoadBalancerTlsCertificatesResponseTypeDef",
    "ClientGetLoadBalancersResponseloadBalancersinstanceHealthSummaryTypeDef",
    "ClientGetLoadBalancersResponseloadBalancerslocationTypeDef",
    "ClientGetLoadBalancersResponseloadBalancerstagsTypeDef",
    "ClientGetLoadBalancersResponseloadBalancerstlsCertificateSummariesTypeDef",
    "ClientGetLoadBalancersResponseloadBalancersTypeDef",
    "ClientGetLoadBalancersResponseTypeDef",
    "ClientGetOperationResponseoperationlocationTypeDef",
    "ClientGetOperationResponseoperationTypeDef",
    "ClientGetOperationResponseTypeDef",
    "ClientGetOperationsForResourceResponseoperationslocationTypeDef",
    "ClientGetOperationsForResourceResponseoperationsTypeDef",
    "ClientGetOperationsForResourceResponseTypeDef",
    "ClientGetOperationsResponseoperationslocationTypeDef",
    "ClientGetOperationsResponseoperationsTypeDef",
    "ClientGetOperationsResponseTypeDef",
    "ClientGetRegionsResponseregionsavailabilityZonesTypeDef",
    "ClientGetRegionsResponseregionsrelationalDatabaseAvailabilityZonesTypeDef",
    "ClientGetRegionsResponseregionsTypeDef",
    "ClientGetRegionsResponseTypeDef",
    "ClientGetRelationalDatabaseBlueprintsResponseblueprintsTypeDef",
    "ClientGetRelationalDatabaseBlueprintsResponseTypeDef",
    "ClientGetRelationalDatabaseBundlesResponsebundlesTypeDef",
    "ClientGetRelationalDatabaseBundlesResponseTypeDef",
    "ClientGetRelationalDatabaseEventsResponserelationalDatabaseEventsTypeDef",
    "ClientGetRelationalDatabaseEventsResponseTypeDef",
    "ClientGetRelationalDatabaseLogEventsResponseresourceLogEventsTypeDef",
    "ClientGetRelationalDatabaseLogEventsResponseTypeDef",
    "ClientGetRelationalDatabaseLogStreamsResponseTypeDef",
    "ClientGetRelationalDatabaseMasterUserPasswordResponseTypeDef",
    "ClientGetRelationalDatabaseMetricDataResponsemetricDataTypeDef",
    "ClientGetRelationalDatabaseMetricDataResponseTypeDef",
    "ClientGetRelationalDatabaseParametersResponseparametersTypeDef",
    "ClientGetRelationalDatabaseParametersResponseTypeDef",
    "ClientGetRelationalDatabaseResponserelationalDatabasehardwareTypeDef",
    "ClientGetRelationalDatabaseResponserelationalDatabaselocationTypeDef",
    "ClientGetRelationalDatabaseResponserelationalDatabasemasterEndpointTypeDef",
    "ClientGetRelationalDatabaseResponserelationalDatabasependingMaintenanceActionsTypeDef",
    "ClientGetRelationalDatabaseResponserelationalDatabasependingModifiedValuesTypeDef",
    "ClientGetRelationalDatabaseResponserelationalDatabasetagsTypeDef",
    "ClientGetRelationalDatabaseResponserelationalDatabaseTypeDef",
    "ClientGetRelationalDatabaseResponseTypeDef",
    "ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotlocationTypeDef",
    "ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshottagsTypeDef",
    "ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotTypeDef",
    "ClientGetRelationalDatabaseSnapshotResponseTypeDef",
    "ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotslocationTypeDef",
    "ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotstagsTypeDef",
    "ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotsTypeDef",
    "ClientGetRelationalDatabaseSnapshotsResponseTypeDef",
    "ClientGetRelationalDatabasesResponserelationalDatabaseshardwareTypeDef",
    "ClientGetRelationalDatabasesResponserelationalDatabaseslocationTypeDef",
    "ClientGetRelationalDatabasesResponserelationalDatabasesmasterEndpointTypeDef",
    "ClientGetRelationalDatabasesResponserelationalDatabasespendingMaintenanceActionsTypeDef",
    "ClientGetRelationalDatabasesResponserelationalDatabasespendingModifiedValuesTypeDef",
    "ClientGetRelationalDatabasesResponserelationalDatabasestagsTypeDef",
    "ClientGetRelationalDatabasesResponserelationalDatabasesTypeDef",
    "ClientGetRelationalDatabasesResponseTypeDef",
    "ClientGetStaticIpResponsestaticIplocationTypeDef",
    "ClientGetStaticIpResponsestaticIpTypeDef",
    "ClientGetStaticIpResponseTypeDef",
    "ClientGetStaticIpsResponsestaticIpslocationTypeDef",
    "ClientGetStaticIpsResponsestaticIpsTypeDef",
    "ClientGetStaticIpsResponseTypeDef",
    "ClientImportKeyPairResponseoperationlocationTypeDef",
    "ClientImportKeyPairResponseoperationTypeDef",
    "ClientImportKeyPairResponseTypeDef",
    "ClientIsVpcPeeredResponseTypeDef",
    "ClientOpenInstancePublicPortsPortInfoTypeDef",
    "ClientOpenInstancePublicPortsResponseoperationlocationTypeDef",
    "ClientOpenInstancePublicPortsResponseoperationTypeDef",
    "ClientOpenInstancePublicPortsResponseTypeDef",
    "ClientPeerVpcResponseoperationlocationTypeDef",
    "ClientPeerVpcResponseoperationTypeDef",
    "ClientPeerVpcResponseTypeDef",
    "ClientPutInstancePublicPortsPortInfosTypeDef",
    "ClientPutInstancePublicPortsResponseoperationlocationTypeDef",
    "ClientPutInstancePublicPortsResponseoperationTypeDef",
    "ClientPutInstancePublicPortsResponseTypeDef",
    "ClientRebootInstanceResponseoperationslocationTypeDef",
    "ClientRebootInstanceResponseoperationsTypeDef",
    "ClientRebootInstanceResponseTypeDef",
    "ClientRebootRelationalDatabaseResponseoperationslocationTypeDef",
    "ClientRebootRelationalDatabaseResponseoperationsTypeDef",
    "ClientRebootRelationalDatabaseResponseTypeDef",
    "ClientReleaseStaticIpResponseoperationslocationTypeDef",
    "ClientReleaseStaticIpResponseoperationsTypeDef",
    "ClientReleaseStaticIpResponseTypeDef",
    "ClientStartInstanceResponseoperationslocationTypeDef",
    "ClientStartInstanceResponseoperationsTypeDef",
    "ClientStartInstanceResponseTypeDef",
    "ClientStartRelationalDatabaseResponseoperationslocationTypeDef",
    "ClientStartRelationalDatabaseResponseoperationsTypeDef",
    "ClientStartRelationalDatabaseResponseTypeDef",
    "ClientStopInstanceResponseoperationslocationTypeDef",
    "ClientStopInstanceResponseoperationsTypeDef",
    "ClientStopInstanceResponseTypeDef",
    "ClientStopRelationalDatabaseResponseoperationslocationTypeDef",
    "ClientStopRelationalDatabaseResponseoperationsTypeDef",
    "ClientStopRelationalDatabaseResponseTypeDef",
    "ClientTagResourceResponseoperationslocationTypeDef",
    "ClientTagResourceResponseoperationsTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUnpeerVpcResponseoperationlocationTypeDef",
    "ClientUnpeerVpcResponseoperationTypeDef",
    "ClientUnpeerVpcResponseTypeDef",
    "ClientUntagResourceResponseoperationslocationTypeDef",
    "ClientUntagResourceResponseoperationsTypeDef",
    "ClientUntagResourceResponseTypeDef",
    "ClientUpdateDomainEntryDomainEntryTypeDef",
    "ClientUpdateDomainEntryResponseoperationslocationTypeDef",
    "ClientUpdateDomainEntryResponseoperationsTypeDef",
    "ClientUpdateDomainEntryResponseTypeDef",
    "ClientUpdateLoadBalancerAttributeResponseoperationslocationTypeDef",
    "ClientUpdateLoadBalancerAttributeResponseoperationsTypeDef",
    "ClientUpdateLoadBalancerAttributeResponseTypeDef",
    "ClientUpdateRelationalDatabaseParametersParametersTypeDef",
    "ClientUpdateRelationalDatabaseParametersResponseoperationslocationTypeDef",
    "ClientUpdateRelationalDatabaseParametersResponseoperationsTypeDef",
    "ClientUpdateRelationalDatabaseParametersResponseTypeDef",
    "ClientUpdateRelationalDatabaseResponseoperationslocationTypeDef",
    "ClientUpdateRelationalDatabaseResponseoperationsTypeDef",
    "ClientUpdateRelationalDatabaseResponseTypeDef",
    "GetActiveNamesPaginatePaginationConfigTypeDef",
    "GetActiveNamesPaginateResponseTypeDef",
    "GetBlueprintsPaginatePaginationConfigTypeDef",
    "GetBlueprintsPaginateResponseblueprintsTypeDef",
    "GetBlueprintsPaginateResponseTypeDef",
    "GetBundlesPaginatePaginationConfigTypeDef",
    "GetBundlesPaginateResponsebundlesTypeDef",
    "GetBundlesPaginateResponseTypeDef",
    "GetCloudFormationStackRecordsPaginatePaginationConfigTypeDef",
    "GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsdestinationInfoTypeDef",
    "GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordslocationTypeDef",
    "GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordssourceInfoTypeDef",
    "GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsTypeDef",
    "GetCloudFormationStackRecordsPaginateResponseTypeDef",
    "GetDiskSnapshotsPaginatePaginationConfigTypeDef",
    "GetDiskSnapshotsPaginateResponsediskSnapshotslocationTypeDef",
    "GetDiskSnapshotsPaginateResponsediskSnapshotstagsTypeDef",
    "GetDiskSnapshotsPaginateResponsediskSnapshotsTypeDef",
    "GetDiskSnapshotsPaginateResponseTypeDef",
    "GetDisksPaginatePaginationConfigTypeDef",
    "GetDisksPaginateResponsedisksaddOnsTypeDef",
    "GetDisksPaginateResponsediskslocationTypeDef",
    "GetDisksPaginateResponsediskstagsTypeDef",
    "GetDisksPaginateResponsedisksTypeDef",
    "GetDisksPaginateResponseTypeDef",
    "GetDomainsPaginatePaginationConfigTypeDef",
    "GetDomainsPaginateResponsedomainsdomainEntriesTypeDef",
    "GetDomainsPaginateResponsedomainslocationTypeDef",
    "GetDomainsPaginateResponsedomainstagsTypeDef",
    "GetDomainsPaginateResponsedomainsTypeDef",
    "GetDomainsPaginateResponseTypeDef",
    "GetExportSnapshotRecordsPaginatePaginationConfigTypeDef",
    "GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsdestinationInfoTypeDef",
    "GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordslocationTypeDef",
    "GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef",
    "GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef",
    "GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef",
    "GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoTypeDef",
    "GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsTypeDef",
    "GetExportSnapshotRecordsPaginateResponseTypeDef",
    "GetInstanceSnapshotsPaginatePaginationConfigTypeDef",
    "GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef",
    "GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef",
    "GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef",
    "GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksTypeDef",
    "GetInstanceSnapshotsPaginateResponseinstanceSnapshotslocationTypeDef",
    "GetInstanceSnapshotsPaginateResponseinstanceSnapshotstagsTypeDef",
    "GetInstanceSnapshotsPaginateResponseinstanceSnapshotsTypeDef",
    "GetInstanceSnapshotsPaginateResponseTypeDef",
    "GetInstancesPaginatePaginationConfigTypeDef",
    "GetInstancesPaginateResponseinstancesaddOnsTypeDef",
    "GetInstancesPaginateResponseinstanceshardwaredisksaddOnsTypeDef",
    "GetInstancesPaginateResponseinstanceshardwarediskslocationTypeDef",
    "GetInstancesPaginateResponseinstanceshardwarediskstagsTypeDef",
    "GetInstancesPaginateResponseinstanceshardwaredisksTypeDef",
    "GetInstancesPaginateResponseinstanceshardwareTypeDef",
    "GetInstancesPaginateResponseinstanceslocationTypeDef",
    "GetInstancesPaginateResponseinstancesnetworkingmonthlyTransferTypeDef",
    "GetInstancesPaginateResponseinstancesnetworkingportsTypeDef",
    "GetInstancesPaginateResponseinstancesnetworkingTypeDef",
    "GetInstancesPaginateResponseinstancesstateTypeDef",
    "GetInstancesPaginateResponseinstancestagsTypeDef",
    "GetInstancesPaginateResponseinstancesTypeDef",
    "GetInstancesPaginateResponseTypeDef",
    "GetKeyPairsPaginatePaginationConfigTypeDef",
    "GetKeyPairsPaginateResponsekeyPairslocationTypeDef",
    "GetKeyPairsPaginateResponsekeyPairstagsTypeDef",
    "GetKeyPairsPaginateResponsekeyPairsTypeDef",
    "GetKeyPairsPaginateResponseTypeDef",
    "GetLoadBalancersPaginatePaginationConfigTypeDef",
    "GetLoadBalancersPaginateResponseloadBalancersinstanceHealthSummaryTypeDef",
    "GetLoadBalancersPaginateResponseloadBalancerslocationTypeDef",
    "GetLoadBalancersPaginateResponseloadBalancerstagsTypeDef",
    "GetLoadBalancersPaginateResponseloadBalancerstlsCertificateSummariesTypeDef",
    "GetLoadBalancersPaginateResponseloadBalancersTypeDef",
    "GetLoadBalancersPaginateResponseTypeDef",
    "GetOperationsPaginatePaginationConfigTypeDef",
    "GetOperationsPaginateResponseoperationslocationTypeDef",
    "GetOperationsPaginateResponseoperationsTypeDef",
    "GetOperationsPaginateResponseTypeDef",
    "GetRelationalDatabaseBlueprintsPaginatePaginationConfigTypeDef",
    "GetRelationalDatabaseBlueprintsPaginateResponseblueprintsTypeDef",
    "GetRelationalDatabaseBlueprintsPaginateResponseTypeDef",
    "GetRelationalDatabaseBundlesPaginatePaginationConfigTypeDef",
    "GetRelationalDatabaseBundlesPaginateResponsebundlesTypeDef",
    "GetRelationalDatabaseBundlesPaginateResponseTypeDef",
    "GetRelationalDatabaseEventsPaginatePaginationConfigTypeDef",
    "GetRelationalDatabaseEventsPaginateResponserelationalDatabaseEventsTypeDef",
    "GetRelationalDatabaseEventsPaginateResponseTypeDef",
    "GetRelationalDatabaseParametersPaginatePaginationConfigTypeDef",
    "GetRelationalDatabaseParametersPaginateResponseparametersTypeDef",
    "GetRelationalDatabaseParametersPaginateResponseTypeDef",
    "GetRelationalDatabaseSnapshotsPaginatePaginationConfigTypeDef",
    "GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotslocationTypeDef",
    "GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotstagsTypeDef",
    "GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotsTypeDef",
    "GetRelationalDatabaseSnapshotsPaginateResponseTypeDef",
    "GetRelationalDatabasesPaginatePaginationConfigTypeDef",
    "GetRelationalDatabasesPaginateResponserelationalDatabaseshardwareTypeDef",
    "GetRelationalDatabasesPaginateResponserelationalDatabaseslocationTypeDef",
    "GetRelationalDatabasesPaginateResponserelationalDatabasesmasterEndpointTypeDef",
    "GetRelationalDatabasesPaginateResponserelationalDatabasespendingMaintenanceActionsTypeDef",
    "GetRelationalDatabasesPaginateResponserelationalDatabasespendingModifiedValuesTypeDef",
    "GetRelationalDatabasesPaginateResponserelationalDatabasestagsTypeDef",
    "GetRelationalDatabasesPaginateResponserelationalDatabasesTypeDef",
    "GetRelationalDatabasesPaginateResponseTypeDef",
    "GetStaticIpsPaginatePaginationConfigTypeDef",
    "GetStaticIpsPaginateResponsestaticIpslocationTypeDef",
    "GetStaticIpsPaginateResponsestaticIpsTypeDef",
    "GetStaticIpsPaginateResponseTypeDef",
)


_ClientAllocateStaticIpResponseoperationslocationTypeDef = TypedDict(
    "_ClientAllocateStaticIpResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientAllocateStaticIpResponseoperationslocationTypeDef(
    _ClientAllocateStaticIpResponseoperationslocationTypeDef
):
    pass


_ClientAllocateStaticIpResponseoperationsTypeDef = TypedDict(
    "_ClientAllocateStaticIpResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientAllocateStaticIpResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientAllocateStaticIpResponseoperationsTypeDef(
    _ClientAllocateStaticIpResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientAllocateStaticIpResponseTypeDef = TypedDict(
    "_ClientAllocateStaticIpResponseTypeDef",
    {"operations": List[ClientAllocateStaticIpResponseoperationsTypeDef]},
    total=False,
)


class ClientAllocateStaticIpResponseTypeDef(_ClientAllocateStaticIpResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the static IP address you
        allocated.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientAttachDiskResponseoperationslocationTypeDef = TypedDict(
    "_ClientAttachDiskResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientAttachDiskResponseoperationslocationTypeDef(
    _ClientAttachDiskResponseoperationslocationTypeDef
):
    pass


_ClientAttachDiskResponseoperationsTypeDef = TypedDict(
    "_ClientAttachDiskResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientAttachDiskResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientAttachDiskResponseoperationsTypeDef(_ClientAttachDiskResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientAttachDiskResponseTypeDef = TypedDict(
    "_ClientAttachDiskResponseTypeDef",
    {"operations": List[ClientAttachDiskResponseoperationsTypeDef]},
    total=False,
)


class ClientAttachDiskResponseTypeDef(_ClientAttachDiskResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientAttachInstancesToLoadBalancerResponseoperationslocationTypeDef = TypedDict(
    "_ClientAttachInstancesToLoadBalancerResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientAttachInstancesToLoadBalancerResponseoperationslocationTypeDef(
    _ClientAttachInstancesToLoadBalancerResponseoperationslocationTypeDef
):
    pass


_ClientAttachInstancesToLoadBalancerResponseoperationsTypeDef = TypedDict(
    "_ClientAttachInstancesToLoadBalancerResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientAttachInstancesToLoadBalancerResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientAttachInstancesToLoadBalancerResponseoperationsTypeDef(
    _ClientAttachInstancesToLoadBalancerResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientAttachInstancesToLoadBalancerResponseTypeDef = TypedDict(
    "_ClientAttachInstancesToLoadBalancerResponseTypeDef",
    {"operations": List[ClientAttachInstancesToLoadBalancerResponseoperationsTypeDef]},
    total=False,
)


class ClientAttachInstancesToLoadBalancerResponseTypeDef(
    _ClientAttachInstancesToLoadBalancerResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object representing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientAttachLoadBalancerTlsCertificateResponseoperationslocationTypeDef = TypedDict(
    "_ClientAttachLoadBalancerTlsCertificateResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientAttachLoadBalancerTlsCertificateResponseoperationslocationTypeDef(
    _ClientAttachLoadBalancerTlsCertificateResponseoperationslocationTypeDef
):
    pass


_ClientAttachLoadBalancerTlsCertificateResponseoperationsTypeDef = TypedDict(
    "_ClientAttachLoadBalancerTlsCertificateResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientAttachLoadBalancerTlsCertificateResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientAttachLoadBalancerTlsCertificateResponseoperationsTypeDef(
    _ClientAttachLoadBalancerTlsCertificateResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientAttachLoadBalancerTlsCertificateResponseTypeDef = TypedDict(
    "_ClientAttachLoadBalancerTlsCertificateResponseTypeDef",
    {"operations": List[ClientAttachLoadBalancerTlsCertificateResponseoperationsTypeDef]},
    total=False,
)


class ClientAttachLoadBalancerTlsCertificateResponseTypeDef(
    _ClientAttachLoadBalancerTlsCertificateResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object representing the API operations.
        These SSL/TLS certificates are only usable by Lightsail load balancers. You can't get the
        certificate and use it for another purpose.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientAttachStaticIpResponseoperationslocationTypeDef = TypedDict(
    "_ClientAttachStaticIpResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientAttachStaticIpResponseoperationslocationTypeDef(
    _ClientAttachStaticIpResponseoperationslocationTypeDef
):
    pass


_ClientAttachStaticIpResponseoperationsTypeDef = TypedDict(
    "_ClientAttachStaticIpResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientAttachStaticIpResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientAttachStaticIpResponseoperationsTypeDef(_ClientAttachStaticIpResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientAttachStaticIpResponseTypeDef = TypedDict(
    "_ClientAttachStaticIpResponseTypeDef",
    {"operations": List[ClientAttachStaticIpResponseoperationsTypeDef]},
    total=False,
)


class ClientAttachStaticIpResponseTypeDef(_ClientAttachStaticIpResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about your API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCloseInstancePublicPortsPortInfoTypeDef = TypedDict(
    "_ClientCloseInstancePublicPortsPortInfoTypeDef",
    {"fromPort": int, "toPort": int, "protocol": Literal["tcp", "all", "udp"]},
    total=False,
)


class ClientCloseInstancePublicPortsPortInfoTypeDef(_ClientCloseInstancePublicPortsPortInfoTypeDef):
    """
    Information about the public port you are trying to close.
    - **fromPort** *(integer) --*

      The first port in the range.
    """


_ClientCloseInstancePublicPortsResponseoperationlocationTypeDef = TypedDict(
    "_ClientCloseInstancePublicPortsResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCloseInstancePublicPortsResponseoperationlocationTypeDef(
    _ClientCloseInstancePublicPortsResponseoperationlocationTypeDef
):
    pass


_ClientCloseInstancePublicPortsResponseoperationTypeDef = TypedDict(
    "_ClientCloseInstancePublicPortsResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCloseInstancePublicPortsResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCloseInstancePublicPortsResponseoperationTypeDef(
    _ClientCloseInstancePublicPortsResponseoperationTypeDef
):
    """
    - **operation** *(dict) --*

      An array of key-value pairs that contains information about the operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCloseInstancePublicPortsResponseTypeDef = TypedDict(
    "_ClientCloseInstancePublicPortsResponseTypeDef",
    {"operation": ClientCloseInstancePublicPortsResponseoperationTypeDef},
    total=False,
)


class ClientCloseInstancePublicPortsResponseTypeDef(_ClientCloseInstancePublicPortsResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs that contains information about the operation.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientCopySnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientCopySnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCopySnapshotResponseoperationslocationTypeDef(
    _ClientCopySnapshotResponseoperationslocationTypeDef
):
    pass


_ClientCopySnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientCopySnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCopySnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCopySnapshotResponseoperationsTypeDef(_ClientCopySnapshotResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCopySnapshotResponseTypeDef = TypedDict(
    "_ClientCopySnapshotResponseTypeDef",
    {"operations": List[ClientCopySnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientCopySnapshotResponseTypeDef(_ClientCopySnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        A list of objects describing the API operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_RequiredClientCreateCloudFormationStackInstancesTypeDef = TypedDict(
    "_RequiredClientCreateCloudFormationStackInstancesTypeDef", {"sourceName": str}
)
_OptionalClientCreateCloudFormationStackInstancesTypeDef = TypedDict(
    "_OptionalClientCreateCloudFormationStackInstancesTypeDef",
    {
        "instanceType": str,
        "portInfoSource": Literal["DEFAULT", "INSTANCE", "NONE", "CLOSED"],
        "userData": str,
        "availabilityZone": str,
    },
    total=False,
)


class ClientCreateCloudFormationStackInstancesTypeDef(
    _RequiredClientCreateCloudFormationStackInstancesTypeDef,
    _OptionalClientCreateCloudFormationStackInstancesTypeDef,
):
    """
    - *(dict) --*

      Describes the Amazon Elastic Compute Cloud instance and related resources to be created using
      the ``create cloud formation stack`` operation.
      - **sourceName** *(string) --***[REQUIRED]**

        The name of the export snapshot record, which contains the exported Lightsail instance
        snapshot that will be used as the source of the new Amazon EC2 instance.
        Use the ``get export snapshot records`` operation to get a list of export snapshot records
        that you can use to create a CloudFormation stack.
    """


_ClientCreateCloudFormationStackResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateCloudFormationStackResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateCloudFormationStackResponseoperationslocationTypeDef(
    _ClientCreateCloudFormationStackResponseoperationslocationTypeDef
):
    pass


_ClientCreateCloudFormationStackResponseoperationsTypeDef = TypedDict(
    "_ClientCreateCloudFormationStackResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateCloudFormationStackResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateCloudFormationStackResponseoperationsTypeDef(
    _ClientCreateCloudFormationStackResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateCloudFormationStackResponseTypeDef = TypedDict(
    "_ClientCreateCloudFormationStackResponseTypeDef",
    {"operations": List[ClientCreateCloudFormationStackResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateCloudFormationStackResponseTypeDef(
    _ClientCreateCloudFormationStackResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        A list of objects describing the API operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateDiskAddOnsautoSnapshotAddOnRequestTypeDef = TypedDict(
    "_ClientCreateDiskAddOnsautoSnapshotAddOnRequestTypeDef",
    {"snapshotTimeOfDay": str},
    total=False,
)


class ClientCreateDiskAddOnsautoSnapshotAddOnRequestTypeDef(
    _ClientCreateDiskAddOnsautoSnapshotAddOnRequestTypeDef
):
    pass


_ClientCreateDiskAddOnsTypeDef = TypedDict(
    "_ClientCreateDiskAddOnsTypeDef",
    {
        "addOnType": str,
        "autoSnapshotAddOnRequest": ClientCreateDiskAddOnsautoSnapshotAddOnRequestTypeDef,
    },
    total=False,
)


class ClientCreateDiskAddOnsTypeDef(_ClientCreateDiskAddOnsTypeDef):
    """
    - *(dict) --*

      Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.
      .. note::

        An additional cost may be associated with enabling add-ons. For more information, see the
        `Lightsail pricing page <https://aws.amazon.com/lightsail/pricing/>`__ .
    """


_ClientCreateDiskFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef = TypedDict(
    "_ClientCreateDiskFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef",
    {"snapshotTimeOfDay": str},
    total=False,
)


class ClientCreateDiskFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef(
    _ClientCreateDiskFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef
):
    pass


_ClientCreateDiskFromSnapshotAddOnsTypeDef = TypedDict(
    "_ClientCreateDiskFromSnapshotAddOnsTypeDef",
    {
        "addOnType": str,
        "autoSnapshotAddOnRequest": ClientCreateDiskFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef,
    },
    total=False,
)


class ClientCreateDiskFromSnapshotAddOnsTypeDef(_ClientCreateDiskFromSnapshotAddOnsTypeDef):
    """
    - *(dict) --*

      Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.
      .. note::

        An additional cost may be associated with enabling add-ons. For more information, see the
        `Lightsail pricing page <https://aws.amazon.com/lightsail/pricing/>`__ .
    """


_ClientCreateDiskFromSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateDiskFromSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateDiskFromSnapshotResponseoperationslocationTypeDef(
    _ClientCreateDiskFromSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientCreateDiskFromSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientCreateDiskFromSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateDiskFromSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateDiskFromSnapshotResponseoperationsTypeDef(
    _ClientCreateDiskFromSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateDiskFromSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateDiskFromSnapshotResponseTypeDef",
    {"operations": List[ClientCreateDiskFromSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateDiskFromSnapshotResponseTypeDef(_ClientCreateDiskFromSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateDiskFromSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDiskFromSnapshotTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateDiskFromSnapshotTagsTypeDef(_ClientCreateDiskFromSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateDiskResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateDiskResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateDiskResponseoperationslocationTypeDef(
    _ClientCreateDiskResponseoperationslocationTypeDef
):
    pass


_ClientCreateDiskResponseoperationsTypeDef = TypedDict(
    "_ClientCreateDiskResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateDiskResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateDiskResponseoperationsTypeDef(_ClientCreateDiskResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateDiskResponseTypeDef = TypedDict(
    "_ClientCreateDiskResponseTypeDef",
    {"operations": List[ClientCreateDiskResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateDiskResponseTypeDef(_ClientCreateDiskResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateDiskSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateDiskSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateDiskSnapshotResponseoperationslocationTypeDef(
    _ClientCreateDiskSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientCreateDiskSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientCreateDiskSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateDiskSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateDiskSnapshotResponseoperationsTypeDef(
    _ClientCreateDiskSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateDiskSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateDiskSnapshotResponseTypeDef",
    {"operations": List[ClientCreateDiskSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateDiskSnapshotResponseTypeDef(_ClientCreateDiskSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateDiskSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDiskSnapshotTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateDiskSnapshotTagsTypeDef(_ClientCreateDiskSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateDiskTagsTypeDef = TypedDict(
    "_ClientCreateDiskTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateDiskTagsTypeDef(_ClientCreateDiskTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateDomainEntryDomainEntryTypeDef = TypedDict(
    "_ClientCreateDomainEntryDomainEntryTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)


class ClientCreateDomainEntryDomainEntryTypeDef(_ClientCreateDomainEntryDomainEntryTypeDef):
    """
    An array of key-value pairs containing information about the domain entry request.
    - **id** *(string) --*

      The ID of the domain recordset entry.
    """


_ClientCreateDomainEntryResponseoperationlocationTypeDef = TypedDict(
    "_ClientCreateDomainEntryResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateDomainEntryResponseoperationlocationTypeDef(
    _ClientCreateDomainEntryResponseoperationlocationTypeDef
):
    pass


_ClientCreateDomainEntryResponseoperationTypeDef = TypedDict(
    "_ClientCreateDomainEntryResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateDomainEntryResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateDomainEntryResponseoperationTypeDef(
    _ClientCreateDomainEntryResponseoperationTypeDef
):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateDomainEntryResponseTypeDef = TypedDict(
    "_ClientCreateDomainEntryResponseTypeDef",
    {"operation": ClientCreateDomainEntryResponseoperationTypeDef},
    total=False,
)


class ClientCreateDomainEntryResponseTypeDef(_ClientCreateDomainEntryResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the operation.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientCreateDomainResponseoperationlocationTypeDef = TypedDict(
    "_ClientCreateDomainResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateDomainResponseoperationlocationTypeDef(
    _ClientCreateDomainResponseoperationlocationTypeDef
):
    pass


_ClientCreateDomainResponseoperationTypeDef = TypedDict(
    "_ClientCreateDomainResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateDomainResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateDomainResponseoperationTypeDef(_ClientCreateDomainResponseoperationTypeDef):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the domain resource you created.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateDomainResponseTypeDef = TypedDict(
    "_ClientCreateDomainResponseTypeDef",
    {"operation": ClientCreateDomainResponseoperationTypeDef},
    total=False,
)


class ClientCreateDomainResponseTypeDef(_ClientCreateDomainResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the domain resource you created.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientCreateDomainTagsTypeDef = TypedDict(
    "_ClientCreateDomainTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateDomainTagsTypeDef(_ClientCreateDomainTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateInstanceSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateInstanceSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateInstanceSnapshotResponseoperationslocationTypeDef(
    _ClientCreateInstanceSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientCreateInstanceSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientCreateInstanceSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateInstanceSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateInstanceSnapshotResponseoperationsTypeDef(
    _ClientCreateInstanceSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateInstanceSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateInstanceSnapshotResponseTypeDef",
    {"operations": List[ClientCreateInstanceSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateInstanceSnapshotResponseTypeDef(_ClientCreateInstanceSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your create
        instances snapshot request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateInstanceSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateInstanceSnapshotTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateInstanceSnapshotTagsTypeDef(_ClientCreateInstanceSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateInstancesAddOnsautoSnapshotAddOnRequestTypeDef = TypedDict(
    "_ClientCreateInstancesAddOnsautoSnapshotAddOnRequestTypeDef",
    {"snapshotTimeOfDay": str},
    total=False,
)


class ClientCreateInstancesAddOnsautoSnapshotAddOnRequestTypeDef(
    _ClientCreateInstancesAddOnsautoSnapshotAddOnRequestTypeDef
):
    pass


_ClientCreateInstancesAddOnsTypeDef = TypedDict(
    "_ClientCreateInstancesAddOnsTypeDef",
    {
        "addOnType": str,
        "autoSnapshotAddOnRequest": ClientCreateInstancesAddOnsautoSnapshotAddOnRequestTypeDef,
    },
    total=False,
)


class ClientCreateInstancesAddOnsTypeDef(_ClientCreateInstancesAddOnsTypeDef):
    """
    - *(dict) --*

      Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.
      .. note::

        An additional cost may be associated with enabling add-ons. For more information, see the
        `Lightsail pricing page <https://aws.amazon.com/lightsail/pricing/>`__ .
    """


_ClientCreateInstancesFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef = TypedDict(
    "_ClientCreateInstancesFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef",
    {"snapshotTimeOfDay": str},
    total=False,
)


class ClientCreateInstancesFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef(
    _ClientCreateInstancesFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef
):
    pass


_ClientCreateInstancesFromSnapshotAddOnsTypeDef = TypedDict(
    "_ClientCreateInstancesFromSnapshotAddOnsTypeDef",
    {
        "addOnType": str,
        "autoSnapshotAddOnRequest": ClientCreateInstancesFromSnapshotAddOnsautoSnapshotAddOnRequestTypeDef,
    },
    total=False,
)


class ClientCreateInstancesFromSnapshotAddOnsTypeDef(
    _ClientCreateInstancesFromSnapshotAddOnsTypeDef
):
    """
    - *(dict) --*

      Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.
      .. note::

        An additional cost may be associated with enabling add-ons. For more information, see the
        `Lightsail pricing page <https://aws.amazon.com/lightsail/pricing/>`__ .
    """


_ClientCreateInstancesFromSnapshotAttachedDiskMappingTypeDef = TypedDict(
    "_ClientCreateInstancesFromSnapshotAttachedDiskMappingTypeDef",
    {"originalDiskPath": str, "newDiskName": str},
    total=False,
)


class ClientCreateInstancesFromSnapshotAttachedDiskMappingTypeDef(
    _ClientCreateInstancesFromSnapshotAttachedDiskMappingTypeDef
):
    pass


_ClientCreateInstancesFromSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateInstancesFromSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateInstancesFromSnapshotResponseoperationslocationTypeDef(
    _ClientCreateInstancesFromSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientCreateInstancesFromSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientCreateInstancesFromSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateInstancesFromSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateInstancesFromSnapshotResponseoperationsTypeDef(
    _ClientCreateInstancesFromSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateInstancesFromSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateInstancesFromSnapshotResponseTypeDef",
    {"operations": List[ClientCreateInstancesFromSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateInstancesFromSnapshotResponseTypeDef(
    _ClientCreateInstancesFromSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your create
        instances from snapshot request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateInstancesFromSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateInstancesFromSnapshotTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateInstancesFromSnapshotTagsTypeDef(_ClientCreateInstancesFromSnapshotTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateInstancesResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateInstancesResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateInstancesResponseoperationslocationTypeDef(
    _ClientCreateInstancesResponseoperationslocationTypeDef
):
    pass


_ClientCreateInstancesResponseoperationsTypeDef = TypedDict(
    "_ClientCreateInstancesResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateInstancesResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateInstancesResponseoperationsTypeDef(
    _ClientCreateInstancesResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateInstancesResponseTypeDef = TypedDict(
    "_ClientCreateInstancesResponseTypeDef",
    {"operations": List[ClientCreateInstancesResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateInstancesResponseTypeDef(_ClientCreateInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your create
        instances request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateInstancesTagsTypeDef = TypedDict(
    "_ClientCreateInstancesTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateInstancesTagsTypeDef(_ClientCreateInstancesTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateKeyPairResponsekeyPairlocationTypeDef = TypedDict(
    "_ClientCreateKeyPairResponsekeyPairlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateKeyPairResponsekeyPairlocationTypeDef(
    _ClientCreateKeyPairResponsekeyPairlocationTypeDef
):
    pass


_ClientCreateKeyPairResponsekeyPairtagsTypeDef = TypedDict(
    "_ClientCreateKeyPairResponsekeyPairtagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateKeyPairResponsekeyPairtagsTypeDef(_ClientCreateKeyPairResponsekeyPairtagsTypeDef):
    pass


_ClientCreateKeyPairResponsekeyPairTypeDef = TypedDict(
    "_ClientCreateKeyPairResponsekeyPairTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientCreateKeyPairResponsekeyPairlocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientCreateKeyPairResponsekeyPairtagsTypeDef],
        "fingerprint": str,
    },
    total=False,
)


class ClientCreateKeyPairResponsekeyPairTypeDef(_ClientCreateKeyPairResponsekeyPairTypeDef):
    """
    - **keyPair** *(dict) --*

      An array of key-value pairs containing information about the new key pair you just created.
      - **name** *(string) --*

        The friendly name of the SSH key pair.
    """


_ClientCreateKeyPairResponseoperationlocationTypeDef = TypedDict(
    "_ClientCreateKeyPairResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateKeyPairResponseoperationlocationTypeDef(
    _ClientCreateKeyPairResponseoperationlocationTypeDef
):
    pass


_ClientCreateKeyPairResponseoperationTypeDef = TypedDict(
    "_ClientCreateKeyPairResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateKeyPairResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateKeyPairResponseoperationTypeDef(_ClientCreateKeyPairResponseoperationTypeDef):
    pass


_ClientCreateKeyPairResponseTypeDef = TypedDict(
    "_ClientCreateKeyPairResponseTypeDef",
    {
        "keyPair": ClientCreateKeyPairResponsekeyPairTypeDef,
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "operation": ClientCreateKeyPairResponseoperationTypeDef,
    },
    total=False,
)


class ClientCreateKeyPairResponseTypeDef(_ClientCreateKeyPairResponseTypeDef):
    """
    - *(dict) --*

      - **keyPair** *(dict) --*

        An array of key-value pairs containing information about the new key pair you just created.
        - **name** *(string) --*

          The friendly name of the SSH key pair.
    """


_ClientCreateKeyPairTagsTypeDef = TypedDict(
    "_ClientCreateKeyPairTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateKeyPairTagsTypeDef(_ClientCreateKeyPairTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateLoadBalancerResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateLoadBalancerResponseoperationslocationTypeDef(
    _ClientCreateLoadBalancerResponseoperationslocationTypeDef
):
    pass


_ClientCreateLoadBalancerResponseoperationsTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateLoadBalancerResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateLoadBalancerResponseoperationsTypeDef(
    _ClientCreateLoadBalancerResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseTypeDef",
    {"operations": List[ClientCreateLoadBalancerResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateLoadBalancerResponseTypeDef(_ClientCreateLoadBalancerResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object containing information about the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_ClientCreateLoadBalancerTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateLoadBalancerTagsTypeDef(_ClientCreateLoadBalancerTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateLoadBalancerTlsCertificateResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateLoadBalancerTlsCertificateResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateLoadBalancerTlsCertificateResponseoperationslocationTypeDef(
    _ClientCreateLoadBalancerTlsCertificateResponseoperationslocationTypeDef
):
    pass


_ClientCreateLoadBalancerTlsCertificateResponseoperationsTypeDef = TypedDict(
    "_ClientCreateLoadBalancerTlsCertificateResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateLoadBalancerTlsCertificateResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateLoadBalancerTlsCertificateResponseoperationsTypeDef(
    _ClientCreateLoadBalancerTlsCertificateResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateLoadBalancerTlsCertificateResponseTypeDef = TypedDict(
    "_ClientCreateLoadBalancerTlsCertificateResponseTypeDef",
    {"operations": List[ClientCreateLoadBalancerTlsCertificateResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateLoadBalancerTlsCertificateResponseTypeDef(
    _ClientCreateLoadBalancerTlsCertificateResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object containing information about the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateLoadBalancerTlsCertificateTagsTypeDef = TypedDict(
    "_ClientCreateLoadBalancerTlsCertificateTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateLoadBalancerTlsCertificateTagsTypeDef(
    _ClientCreateLoadBalancerTlsCertificateTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateRelationalDatabaseFromSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseFromSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateRelationalDatabaseFromSnapshotResponseoperationslocationTypeDef(
    _ClientCreateRelationalDatabaseFromSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientCreateRelationalDatabaseFromSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseFromSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateRelationalDatabaseFromSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateRelationalDatabaseFromSnapshotResponseoperationsTypeDef(
    _ClientCreateRelationalDatabaseFromSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateRelationalDatabaseFromSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseFromSnapshotResponseTypeDef",
    {"operations": List[ClientCreateRelationalDatabaseFromSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateRelationalDatabaseFromSnapshotResponseTypeDef(
    _ClientCreateRelationalDatabaseFromSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your create relational database from snapshot request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateRelationalDatabaseFromSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseFromSnapshotTagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateRelationalDatabaseFromSnapshotTagsTypeDef(
    _ClientCreateRelationalDatabaseFromSnapshotTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateRelationalDatabaseResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateRelationalDatabaseResponseoperationslocationTypeDef(
    _ClientCreateRelationalDatabaseResponseoperationslocationTypeDef
):
    pass


_ClientCreateRelationalDatabaseResponseoperationsTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateRelationalDatabaseResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateRelationalDatabaseResponseoperationsTypeDef(
    _ClientCreateRelationalDatabaseResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateRelationalDatabaseResponseTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseResponseTypeDef",
    {"operations": List[ClientCreateRelationalDatabaseResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateRelationalDatabaseResponseTypeDef(_ClientCreateRelationalDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your create relational database request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateRelationalDatabaseSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientCreateRelationalDatabaseSnapshotResponseoperationslocationTypeDef(
    _ClientCreateRelationalDatabaseSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientCreateRelationalDatabaseSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientCreateRelationalDatabaseSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientCreateRelationalDatabaseSnapshotResponseoperationsTypeDef(
    _ClientCreateRelationalDatabaseSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientCreateRelationalDatabaseSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseSnapshotResponseTypeDef",
    {"operations": List[ClientCreateRelationalDatabaseSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientCreateRelationalDatabaseSnapshotResponseTypeDef(
    _ClientCreateRelationalDatabaseSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your create relational database snapshot request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientCreateRelationalDatabaseSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseSnapshotTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateRelationalDatabaseSnapshotTagsTypeDef(
    _ClientCreateRelationalDatabaseSnapshotTagsTypeDef
):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientCreateRelationalDatabaseTagsTypeDef = TypedDict(
    "_ClientCreateRelationalDatabaseTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateRelationalDatabaseTagsTypeDef(_ClientCreateRelationalDatabaseTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientDeleteAutoSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteAutoSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteAutoSnapshotResponseoperationslocationTypeDef(
    _ClientDeleteAutoSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientDeleteAutoSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteAutoSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteAutoSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteAutoSnapshotResponseoperationsTypeDef(
    _ClientDeleteAutoSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteAutoSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteAutoSnapshotResponseTypeDef",
    {"operations": List[ClientDeleteAutoSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteAutoSnapshotResponseTypeDef(_ClientDeleteAutoSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of objects that describe the result of your request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteDiskResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteDiskResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteDiskResponseoperationslocationTypeDef(
    _ClientDeleteDiskResponseoperationslocationTypeDef
):
    pass


_ClientDeleteDiskResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteDiskResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteDiskResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteDiskResponseoperationsTypeDef(_ClientDeleteDiskResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteDiskResponseTypeDef = TypedDict(
    "_ClientDeleteDiskResponseTypeDef",
    {"operations": List[ClientDeleteDiskResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteDiskResponseTypeDef(_ClientDeleteDiskResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of objects that describe the result of your request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteDiskSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteDiskSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteDiskSnapshotResponseoperationslocationTypeDef(
    _ClientDeleteDiskSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientDeleteDiskSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteDiskSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteDiskSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteDiskSnapshotResponseoperationsTypeDef(
    _ClientDeleteDiskSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteDiskSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteDiskSnapshotResponseTypeDef",
    {"operations": List[ClientDeleteDiskSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteDiskSnapshotResponseTypeDef(_ClientDeleteDiskSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteDomainEntryDomainEntryTypeDef = TypedDict(
    "_ClientDeleteDomainEntryDomainEntryTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)


class ClientDeleteDomainEntryDomainEntryTypeDef(_ClientDeleteDomainEntryDomainEntryTypeDef):
    """
    An array of key-value pairs containing information about your domain entries.
    - **id** *(string) --*

      The ID of the domain recordset entry.
    """


_ClientDeleteDomainEntryResponseoperationlocationTypeDef = TypedDict(
    "_ClientDeleteDomainEntryResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteDomainEntryResponseoperationlocationTypeDef(
    _ClientDeleteDomainEntryResponseoperationlocationTypeDef
):
    pass


_ClientDeleteDomainEntryResponseoperationTypeDef = TypedDict(
    "_ClientDeleteDomainEntryResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteDomainEntryResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteDomainEntryResponseoperationTypeDef(
    _ClientDeleteDomainEntryResponseoperationTypeDef
):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the results of your delete domain
      entry request.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteDomainEntryResponseTypeDef = TypedDict(
    "_ClientDeleteDomainEntryResponseTypeDef",
    {"operation": ClientDeleteDomainEntryResponseoperationTypeDef},
    total=False,
)


class ClientDeleteDomainEntryResponseTypeDef(_ClientDeleteDomainEntryResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the results of your delete domain
        entry request.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientDeleteDomainResponseoperationlocationTypeDef = TypedDict(
    "_ClientDeleteDomainResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteDomainResponseoperationlocationTypeDef(
    _ClientDeleteDomainResponseoperationlocationTypeDef
):
    pass


_ClientDeleteDomainResponseoperationTypeDef = TypedDict(
    "_ClientDeleteDomainResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteDomainResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteDomainResponseoperationTypeDef(_ClientDeleteDomainResponseoperationTypeDef):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the results of your delete domain
      request.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteDomainResponseTypeDef = TypedDict(
    "_ClientDeleteDomainResponseTypeDef",
    {"operation": ClientDeleteDomainResponseoperationTypeDef},
    total=False,
)


class ClientDeleteDomainResponseTypeDef(_ClientDeleteDomainResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the results of your delete domain
        request.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientDeleteInstanceResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteInstanceResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteInstanceResponseoperationslocationTypeDef(
    _ClientDeleteInstanceResponseoperationslocationTypeDef
):
    pass


_ClientDeleteInstanceResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteInstanceResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteInstanceResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteInstanceResponseoperationsTypeDef(_ClientDeleteInstanceResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteInstanceResponseTypeDef = TypedDict(
    "_ClientDeleteInstanceResponseTypeDef",
    {"operations": List[ClientDeleteInstanceResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteInstanceResponseTypeDef(_ClientDeleteInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your delete instance
        request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteInstanceSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteInstanceSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteInstanceSnapshotResponseoperationslocationTypeDef(
    _ClientDeleteInstanceSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientDeleteInstanceSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteInstanceSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteInstanceSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteInstanceSnapshotResponseoperationsTypeDef(
    _ClientDeleteInstanceSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteInstanceSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteInstanceSnapshotResponseTypeDef",
    {"operations": List[ClientDeleteInstanceSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteInstanceSnapshotResponseTypeDef(_ClientDeleteInstanceSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your delete instance
        snapshot request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteKeyPairResponseoperationlocationTypeDef = TypedDict(
    "_ClientDeleteKeyPairResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteKeyPairResponseoperationlocationTypeDef(
    _ClientDeleteKeyPairResponseoperationlocationTypeDef
):
    pass


_ClientDeleteKeyPairResponseoperationTypeDef = TypedDict(
    "_ClientDeleteKeyPairResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteKeyPairResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteKeyPairResponseoperationTypeDef(_ClientDeleteKeyPairResponseoperationTypeDef):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the results of your delete key pair
      request.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteKeyPairResponseTypeDef = TypedDict(
    "_ClientDeleteKeyPairResponseTypeDef",
    {"operation": ClientDeleteKeyPairResponseoperationTypeDef},
    total=False,
)


class ClientDeleteKeyPairResponseTypeDef(_ClientDeleteKeyPairResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the results of your delete key pair
        request.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientDeleteKnownHostKeysResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteKnownHostKeysResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteKnownHostKeysResponseoperationslocationTypeDef(
    _ClientDeleteKnownHostKeysResponseoperationslocationTypeDef
):
    pass


_ClientDeleteKnownHostKeysResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteKnownHostKeysResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteKnownHostKeysResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteKnownHostKeysResponseoperationsTypeDef(
    _ClientDeleteKnownHostKeysResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteKnownHostKeysResponseTypeDef = TypedDict(
    "_ClientDeleteKnownHostKeysResponseTypeDef",
    {"operations": List[ClientDeleteKnownHostKeysResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteKnownHostKeysResponseTypeDef(_ClientDeleteKnownHostKeysResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        A list of objects describing the API operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteLoadBalancerResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteLoadBalancerResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteLoadBalancerResponseoperationslocationTypeDef(
    _ClientDeleteLoadBalancerResponseoperationslocationTypeDef
):
    pass


_ClientDeleteLoadBalancerResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteLoadBalancerResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteLoadBalancerResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteLoadBalancerResponseoperationsTypeDef(
    _ClientDeleteLoadBalancerResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteLoadBalancerResponseTypeDef = TypedDict(
    "_ClientDeleteLoadBalancerResponseTypeDef",
    {"operations": List[ClientDeleteLoadBalancerResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteLoadBalancerResponseTypeDef(_ClientDeleteLoadBalancerResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteLoadBalancerTlsCertificateResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteLoadBalancerTlsCertificateResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteLoadBalancerTlsCertificateResponseoperationslocationTypeDef(
    _ClientDeleteLoadBalancerTlsCertificateResponseoperationslocationTypeDef
):
    pass


_ClientDeleteLoadBalancerTlsCertificateResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteLoadBalancerTlsCertificateResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteLoadBalancerTlsCertificateResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteLoadBalancerTlsCertificateResponseoperationsTypeDef(
    _ClientDeleteLoadBalancerTlsCertificateResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteLoadBalancerTlsCertificateResponseTypeDef = TypedDict(
    "_ClientDeleteLoadBalancerTlsCertificateResponseTypeDef",
    {"operations": List[ClientDeleteLoadBalancerTlsCertificateResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteLoadBalancerTlsCertificateResponseTypeDef(
    _ClientDeleteLoadBalancerTlsCertificateResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteRelationalDatabaseResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteRelationalDatabaseResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteRelationalDatabaseResponseoperationslocationTypeDef(
    _ClientDeleteRelationalDatabaseResponseoperationslocationTypeDef
):
    pass


_ClientDeleteRelationalDatabaseResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteRelationalDatabaseResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteRelationalDatabaseResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteRelationalDatabaseResponseoperationsTypeDef(
    _ClientDeleteRelationalDatabaseResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteRelationalDatabaseResponseTypeDef = TypedDict(
    "_ClientDeleteRelationalDatabaseResponseTypeDef",
    {"operations": List[ClientDeleteRelationalDatabaseResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteRelationalDatabaseResponseTypeDef(_ClientDeleteRelationalDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your delete relational database request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDeleteRelationalDatabaseSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientDeleteRelationalDatabaseSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDeleteRelationalDatabaseSnapshotResponseoperationslocationTypeDef(
    _ClientDeleteRelationalDatabaseSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientDeleteRelationalDatabaseSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientDeleteRelationalDatabaseSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDeleteRelationalDatabaseSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDeleteRelationalDatabaseSnapshotResponseoperationsTypeDef(
    _ClientDeleteRelationalDatabaseSnapshotResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDeleteRelationalDatabaseSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteRelationalDatabaseSnapshotResponseTypeDef",
    {"operations": List[ClientDeleteRelationalDatabaseSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientDeleteRelationalDatabaseSnapshotResponseTypeDef(
    _ClientDeleteRelationalDatabaseSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your delete relational database snapshot request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDetachDiskResponseoperationslocationTypeDef = TypedDict(
    "_ClientDetachDiskResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDetachDiskResponseoperationslocationTypeDef(
    _ClientDetachDiskResponseoperationslocationTypeDef
):
    pass


_ClientDetachDiskResponseoperationsTypeDef = TypedDict(
    "_ClientDetachDiskResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDetachDiskResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDetachDiskResponseoperationsTypeDef(_ClientDetachDiskResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDetachDiskResponseTypeDef = TypedDict(
    "_ClientDetachDiskResponseTypeDef",
    {"operations": List[ClientDetachDiskResponseoperationsTypeDef]},
    total=False,
)


class ClientDetachDiskResponseTypeDef(_ClientDetachDiskResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDetachInstancesFromLoadBalancerResponseoperationslocationTypeDef = TypedDict(
    "_ClientDetachInstancesFromLoadBalancerResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDetachInstancesFromLoadBalancerResponseoperationslocationTypeDef(
    _ClientDetachInstancesFromLoadBalancerResponseoperationslocationTypeDef
):
    pass


_ClientDetachInstancesFromLoadBalancerResponseoperationsTypeDef = TypedDict(
    "_ClientDetachInstancesFromLoadBalancerResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDetachInstancesFromLoadBalancerResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDetachInstancesFromLoadBalancerResponseoperationsTypeDef(
    _ClientDetachInstancesFromLoadBalancerResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDetachInstancesFromLoadBalancerResponseTypeDef = TypedDict(
    "_ClientDetachInstancesFromLoadBalancerResponseTypeDef",
    {"operations": List[ClientDetachInstancesFromLoadBalancerResponseoperationsTypeDef]},
    total=False,
)


class ClientDetachInstancesFromLoadBalancerResponseTypeDef(
    _ClientDetachInstancesFromLoadBalancerResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDetachStaticIpResponseoperationslocationTypeDef = TypedDict(
    "_ClientDetachStaticIpResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDetachStaticIpResponseoperationslocationTypeDef(
    _ClientDetachStaticIpResponseoperationslocationTypeDef
):
    pass


_ClientDetachStaticIpResponseoperationsTypeDef = TypedDict(
    "_ClientDetachStaticIpResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDetachStaticIpResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDetachStaticIpResponseoperationsTypeDef(_ClientDetachStaticIpResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDetachStaticIpResponseTypeDef = TypedDict(
    "_ClientDetachStaticIpResponseTypeDef",
    {"operations": List[ClientDetachStaticIpResponseoperationsTypeDef]},
    total=False,
)


class ClientDetachStaticIpResponseTypeDef(_ClientDetachStaticIpResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your detach static
        IP request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDisableAddOnResponseoperationslocationTypeDef = TypedDict(
    "_ClientDisableAddOnResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientDisableAddOnResponseoperationslocationTypeDef(
    _ClientDisableAddOnResponseoperationslocationTypeDef
):
    pass


_ClientDisableAddOnResponseoperationsTypeDef = TypedDict(
    "_ClientDisableAddOnResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientDisableAddOnResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientDisableAddOnResponseoperationsTypeDef(_ClientDisableAddOnResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientDisableAddOnResponseTypeDef = TypedDict(
    "_ClientDisableAddOnResponseTypeDef",
    {"operations": List[ClientDisableAddOnResponseoperationsTypeDef]},
    total=False,
)


class ClientDisableAddOnResponseTypeDef(_ClientDisableAddOnResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of objects that describe the result of your request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientDownloadDefaultKeyPairResponseTypeDef = TypedDict(
    "_ClientDownloadDefaultKeyPairResponseTypeDef",
    {"publicKeyBase64": str, "privateKeyBase64": str},
    total=False,
)


class ClientDownloadDefaultKeyPairResponseTypeDef(_ClientDownloadDefaultKeyPairResponseTypeDef):
    """
    - *(dict) --*

      - **publicKeyBase64** *(string) --*

        A base64-encoded public key of the ``ssh-rsa`` type.
    """


_ClientEnableAddOnAddOnRequestautoSnapshotAddOnRequestTypeDef = TypedDict(
    "_ClientEnableAddOnAddOnRequestautoSnapshotAddOnRequestTypeDef",
    {"snapshotTimeOfDay": str},
    total=False,
)


class ClientEnableAddOnAddOnRequestautoSnapshotAddOnRequestTypeDef(
    _ClientEnableAddOnAddOnRequestautoSnapshotAddOnRequestTypeDef
):
    pass


_RequiredClientEnableAddOnAddOnRequestTypeDef = TypedDict(
    "_RequiredClientEnableAddOnAddOnRequestTypeDef", {"addOnType": str}
)
_OptionalClientEnableAddOnAddOnRequestTypeDef = TypedDict(
    "_OptionalClientEnableAddOnAddOnRequestTypeDef",
    {"autoSnapshotAddOnRequest": ClientEnableAddOnAddOnRequestautoSnapshotAddOnRequestTypeDef},
    total=False,
)


class ClientEnableAddOnAddOnRequestTypeDef(
    _RequiredClientEnableAddOnAddOnRequestTypeDef, _OptionalClientEnableAddOnAddOnRequestTypeDef
):
    """
    An array of strings representing the add-on to enable or modify.
    - **addOnType** *(string) --***[REQUIRED]**

      The add-on type.
    """


_ClientEnableAddOnResponseoperationslocationTypeDef = TypedDict(
    "_ClientEnableAddOnResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientEnableAddOnResponseoperationslocationTypeDef(
    _ClientEnableAddOnResponseoperationslocationTypeDef
):
    pass


_ClientEnableAddOnResponseoperationsTypeDef = TypedDict(
    "_ClientEnableAddOnResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientEnableAddOnResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientEnableAddOnResponseoperationsTypeDef(_ClientEnableAddOnResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientEnableAddOnResponseTypeDef = TypedDict(
    "_ClientEnableAddOnResponseTypeDef",
    {"operations": List[ClientEnableAddOnResponseoperationsTypeDef]},
    total=False,
)


class ClientEnableAddOnResponseTypeDef(_ClientEnableAddOnResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of objects that describe the result of your request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientExportSnapshotResponseoperationslocationTypeDef = TypedDict(
    "_ClientExportSnapshotResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientExportSnapshotResponseoperationslocationTypeDef(
    _ClientExportSnapshotResponseoperationslocationTypeDef
):
    pass


_ClientExportSnapshotResponseoperationsTypeDef = TypedDict(
    "_ClientExportSnapshotResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientExportSnapshotResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientExportSnapshotResponseoperationsTypeDef(_ClientExportSnapshotResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientExportSnapshotResponseTypeDef = TypedDict(
    "_ClientExportSnapshotResponseTypeDef",
    {"operations": List[ClientExportSnapshotResponseoperationsTypeDef]},
    total=False,
)


class ClientExportSnapshotResponseTypeDef(_ClientExportSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        A list of objects describing the API operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientGetActiveNamesResponseTypeDef = TypedDict(
    "_ClientGetActiveNamesResponseTypeDef",
    {"activeNames": List[str], "nextPageToken": str},
    total=False,
)


class ClientGetActiveNamesResponseTypeDef(_ClientGetActiveNamesResponseTypeDef):
    """
    - *(dict) --*

      - **activeNames** *(list) --*

        The list of active names returned by the get active names request.
        - *(string) --*
    """


_ClientGetAutoSnapshotsResponseautoSnapshotsfromAttachedDisksTypeDef = TypedDict(
    "_ClientGetAutoSnapshotsResponseautoSnapshotsfromAttachedDisksTypeDef",
    {"path": str, "sizeInGb": int},
    total=False,
)


class ClientGetAutoSnapshotsResponseautoSnapshotsfromAttachedDisksTypeDef(
    _ClientGetAutoSnapshotsResponseautoSnapshotsfromAttachedDisksTypeDef
):
    pass


_ClientGetAutoSnapshotsResponseautoSnapshotsTypeDef = TypedDict(
    "_ClientGetAutoSnapshotsResponseautoSnapshotsTypeDef",
    {
        "date": str,
        "createdAt": datetime,
        "status": Literal["Success", "Failed", "InProgress", "NotFound"],
        "fromAttachedDisks": List[
            ClientGetAutoSnapshotsResponseautoSnapshotsfromAttachedDisksTypeDef
        ],
    },
    total=False,
)


class ClientGetAutoSnapshotsResponseautoSnapshotsTypeDef(
    _ClientGetAutoSnapshotsResponseautoSnapshotsTypeDef
):
    pass


_ClientGetAutoSnapshotsResponseTypeDef = TypedDict(
    "_ClientGetAutoSnapshotsResponseTypeDef",
    {
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "autoSnapshots": List[ClientGetAutoSnapshotsResponseautoSnapshotsTypeDef],
    },
    total=False,
)


class ClientGetAutoSnapshotsResponseTypeDef(_ClientGetAutoSnapshotsResponseTypeDef):
    """
    - *(dict) --*

      - **resourceName** *(string) --*

        The name of the source resource for the automatic snapshots.
    """


_ClientGetBlueprintsResponseblueprintsTypeDef = TypedDict(
    "_ClientGetBlueprintsResponseblueprintsTypeDef",
    {
        "blueprintId": str,
        "name": str,
        "group": str,
        "type": Literal["os", "app"],
        "description": str,
        "isActive": bool,
        "minPower": int,
        "version": str,
        "versionCode": str,
        "productUrl": str,
        "licenseUrl": str,
        "platform": Literal["LINUX_UNIX", "WINDOWS"],
    },
    total=False,
)


class ClientGetBlueprintsResponseblueprintsTypeDef(_ClientGetBlueprintsResponseblueprintsTypeDef):
    """
    - *(dict) --*

      Describes a blueprint (a virtual private server image).
      - **blueprintId** *(string) --*

        The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0``
        ).
    """


_ClientGetBlueprintsResponseTypeDef = TypedDict(
    "_ClientGetBlueprintsResponseTypeDef",
    {"blueprints": List[ClientGetBlueprintsResponseblueprintsTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetBlueprintsResponseTypeDef(_ClientGetBlueprintsResponseTypeDef):
    """
    - *(dict) --*

      - **blueprints** *(list) --*

        An array of key-value pairs that contains information about the available blueprints.
        - *(dict) --*

          Describes a blueprint (a virtual private server image).
          - **blueprintId** *(string) --*

            The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or
            ``app_lamp_7_0`` ).
    """


_ClientGetBundlesResponsebundlesTypeDef = TypedDict(
    "_ClientGetBundlesResponsebundlesTypeDef",
    {
        "price": float,
        "cpuCount": int,
        "diskSizeInGb": int,
        "bundleId": str,
        "instanceType": str,
        "isActive": bool,
        "name": str,
        "power": int,
        "ramSizeInGb": Any,
        "transferPerMonthInGb": int,
        "supportedPlatforms": List[Literal["LINUX_UNIX", "WINDOWS"]],
    },
    total=False,
)


class ClientGetBundlesResponsebundlesTypeDef(_ClientGetBundlesResponsebundlesTypeDef):
    """
    - *(dict) --*

      Describes a bundle, which is a set of specs describing your virtual private server (or
      *instance* ).
      - **price** *(float) --*

        The price in US dollars (e.g., ``5.0`` ).
    """


_ClientGetBundlesResponseTypeDef = TypedDict(
    "_ClientGetBundlesResponseTypeDef",
    {"bundles": List[ClientGetBundlesResponsebundlesTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetBundlesResponseTypeDef(_ClientGetBundlesResponseTypeDef):
    """
    - *(dict) --*

      - **bundles** *(list) --*

        An array of key-value pairs that contains information about the available bundles.
        - *(dict) --*

          Describes a bundle, which is a set of specs describing your virtual private server (or
          *instance* ).
          - **price** *(float) --*

            The price in US dollars (e.g., ``5.0`` ).
    """


_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsdestinationInfoTypeDef = TypedDict(
    "_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsdestinationInfoTypeDef",
    {"id": str, "service": str},
    total=False,
)


class ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsdestinationInfoTypeDef(
    _ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsdestinationInfoTypeDef
):
    pass


_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordslocationTypeDef = TypedDict(
    "_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordslocationTypeDef(
    _ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordslocationTypeDef
):
    pass


_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordssourceInfoTypeDef = TypedDict(
    "_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordssourceInfoTypeDef",
    {"resourceType": str, "name": str, "arn": str},
    total=False,
)


class ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordssourceInfoTypeDef(
    _ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordssourceInfoTypeDef
):
    pass


_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsTypeDef = TypedDict(
    "_ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "state": Literal["Started", "Succeeded", "Failed"],
        "sourceInfo": List[
            ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordssourceInfoTypeDef
        ],
        "destinationInfo": ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsdestinationInfoTypeDef,
    },
    total=False,
)


class ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsTypeDef(
    _ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsTypeDef
):
    """
    - *(dict) --*

      Describes a CloudFormation stack record created as a result of the ``create cloud formation
      stack`` operation.
      A CloudFormation stack record provides information about the AWS CloudFormation stack used to
      create a new Amazon Elastic Compute Cloud instance from an exported Lightsail instance
      snapshot.
      - **name** *(string) --*

        The name of the CloudFormation stack record. It starts with ``CloudFormationStackRecord``
        followed by a GUID.
    """


_ClientGetCloudFormationStackRecordsResponseTypeDef = TypedDict(
    "_ClientGetCloudFormationStackRecordsResponseTypeDef",
    {
        "cloudFormationStackRecords": List[
            ClientGetCloudFormationStackRecordsResponsecloudFormationStackRecordsTypeDef
        ],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetCloudFormationStackRecordsResponseTypeDef(
    _ClientGetCloudFormationStackRecordsResponseTypeDef
):
    """
    - *(dict) --*

      - **cloudFormationStackRecords** *(list) --*

        A list of objects describing the CloudFormation stack records.
        - *(dict) --*

          Describes a CloudFormation stack record created as a result of the ``create cloud
          formation stack`` operation.
          A CloudFormation stack record provides information about the AWS CloudFormation stack used
          to create a new Amazon Elastic Compute Cloud instance from an exported Lightsail instance
          snapshot.
          - **name** *(string) --*

            The name of the CloudFormation stack record. It starts with
            ``CloudFormationStackRecord`` followed by a GUID.
    """


_ClientGetDiskResponsediskaddOnsTypeDef = TypedDict(
    "_ClientGetDiskResponsediskaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetDiskResponsediskaddOnsTypeDef(_ClientGetDiskResponsediskaddOnsTypeDef):
    pass


_ClientGetDiskResponsedisklocationTypeDef = TypedDict(
    "_ClientGetDiskResponsedisklocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetDiskResponsedisklocationTypeDef(_ClientGetDiskResponsedisklocationTypeDef):
    pass


_ClientGetDiskResponsedisktagsTypeDef = TypedDict(
    "_ClientGetDiskResponsedisktagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetDiskResponsedisktagsTypeDef(_ClientGetDiskResponsedisktagsTypeDef):
    pass


_ClientGetDiskResponsediskTypeDef = TypedDict(
    "_ClientGetDiskResponsediskTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetDiskResponsedisklocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetDiskResponsedisktagsTypeDef],
        "addOns": List[ClientGetDiskResponsediskaddOnsTypeDef],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class ClientGetDiskResponsediskTypeDef(_ClientGetDiskResponsediskTypeDef):
    """
    - **disk** *(dict) --*

      An object containing information about the disk.
      - **name** *(string) --*

        The unique name of the disk.
    """


_ClientGetDiskResponseTypeDef = TypedDict(
    "_ClientGetDiskResponseTypeDef", {"disk": ClientGetDiskResponsediskTypeDef}, total=False
)


class ClientGetDiskResponseTypeDef(_ClientGetDiskResponseTypeDef):
    """
    - *(dict) --*

      - **disk** *(dict) --*

        An object containing information about the disk.
        - **name** *(string) --*

          The unique name of the disk.
    """


_ClientGetDiskSnapshotResponsediskSnapshotlocationTypeDef = TypedDict(
    "_ClientGetDiskSnapshotResponsediskSnapshotlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetDiskSnapshotResponsediskSnapshotlocationTypeDef(
    _ClientGetDiskSnapshotResponsediskSnapshotlocationTypeDef
):
    pass


_ClientGetDiskSnapshotResponsediskSnapshottagsTypeDef = TypedDict(
    "_ClientGetDiskSnapshotResponsediskSnapshottagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetDiskSnapshotResponsediskSnapshottagsTypeDef(
    _ClientGetDiskSnapshotResponsediskSnapshottagsTypeDef
):
    pass


_ClientGetDiskSnapshotResponsediskSnapshotTypeDef = TypedDict(
    "_ClientGetDiskSnapshotResponsediskSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetDiskSnapshotResponsediskSnapshotlocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetDiskSnapshotResponsediskSnapshottagsTypeDef],
        "sizeInGb": int,
        "state": Literal["pending", "completed", "error", "unknown"],
        "progress": str,
        "fromDiskName": str,
        "fromDiskArn": str,
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "isFromAutoSnapshot": bool,
    },
    total=False,
)


class ClientGetDiskSnapshotResponsediskSnapshotTypeDef(
    _ClientGetDiskSnapshotResponsediskSnapshotTypeDef
):
    """
    - **diskSnapshot** *(dict) --*

      An object containing information about the disk snapshot.
      - **name** *(string) --*

        The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
    """


_ClientGetDiskSnapshotResponseTypeDef = TypedDict(
    "_ClientGetDiskSnapshotResponseTypeDef",
    {"diskSnapshot": ClientGetDiskSnapshotResponsediskSnapshotTypeDef},
    total=False,
)


class ClientGetDiskSnapshotResponseTypeDef(_ClientGetDiskSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **diskSnapshot** *(dict) --*

        An object containing information about the disk snapshot.
        - **name** *(string) --*

          The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
    """


_ClientGetDiskSnapshotsResponsediskSnapshotslocationTypeDef = TypedDict(
    "_ClientGetDiskSnapshotsResponsediskSnapshotslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetDiskSnapshotsResponsediskSnapshotslocationTypeDef(
    _ClientGetDiskSnapshotsResponsediskSnapshotslocationTypeDef
):
    pass


_ClientGetDiskSnapshotsResponsediskSnapshotstagsTypeDef = TypedDict(
    "_ClientGetDiskSnapshotsResponsediskSnapshotstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetDiskSnapshotsResponsediskSnapshotstagsTypeDef(
    _ClientGetDiskSnapshotsResponsediskSnapshotstagsTypeDef
):
    pass


_ClientGetDiskSnapshotsResponsediskSnapshotsTypeDef = TypedDict(
    "_ClientGetDiskSnapshotsResponsediskSnapshotsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetDiskSnapshotsResponsediskSnapshotslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetDiskSnapshotsResponsediskSnapshotstagsTypeDef],
        "sizeInGb": int,
        "state": Literal["pending", "completed", "error", "unknown"],
        "progress": str,
        "fromDiskName": str,
        "fromDiskArn": str,
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "isFromAutoSnapshot": bool,
    },
    total=False,
)


class ClientGetDiskSnapshotsResponsediskSnapshotsTypeDef(
    _ClientGetDiskSnapshotsResponsediskSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a block storage disk snapshot.
      - **name** *(string) --*

        The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
    """


_ClientGetDiskSnapshotsResponseTypeDef = TypedDict(
    "_ClientGetDiskSnapshotsResponseTypeDef",
    {
        "diskSnapshots": List[ClientGetDiskSnapshotsResponsediskSnapshotsTypeDef],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetDiskSnapshotsResponseTypeDef(_ClientGetDiskSnapshotsResponseTypeDef):
    """
    - *(dict) --*

      - **diskSnapshots** *(list) --*

        An array of objects containing information about all block storage disk snapshots.
        - *(dict) --*

          Describes a block storage disk snapshot.
          - **name** *(string) --*

            The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
    """


_ClientGetDisksResponsedisksaddOnsTypeDef = TypedDict(
    "_ClientGetDisksResponsedisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetDisksResponsedisksaddOnsTypeDef(_ClientGetDisksResponsedisksaddOnsTypeDef):
    pass


_ClientGetDisksResponsediskslocationTypeDef = TypedDict(
    "_ClientGetDisksResponsediskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetDisksResponsediskslocationTypeDef(_ClientGetDisksResponsediskslocationTypeDef):
    pass


_ClientGetDisksResponsediskstagsTypeDef = TypedDict(
    "_ClientGetDisksResponsediskstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetDisksResponsediskstagsTypeDef(_ClientGetDisksResponsediskstagsTypeDef):
    pass


_ClientGetDisksResponsedisksTypeDef = TypedDict(
    "_ClientGetDisksResponsedisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetDisksResponsediskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetDisksResponsediskstagsTypeDef],
        "addOns": List[ClientGetDisksResponsedisksaddOnsTypeDef],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class ClientGetDisksResponsedisksTypeDef(_ClientGetDisksResponsedisksTypeDef):
    """
    - *(dict) --*

      Describes a system disk or a block storage disk.
      - **name** *(string) --*

        The unique name of the disk.
    """


_ClientGetDisksResponseTypeDef = TypedDict(
    "_ClientGetDisksResponseTypeDef",
    {"disks": List[ClientGetDisksResponsedisksTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetDisksResponseTypeDef(_ClientGetDisksResponseTypeDef):
    """
    - *(dict) --*

      - **disks** *(list) --*

        An array of objects containing information about all block storage disks.
        - *(dict) --*

          Describes a system disk or a block storage disk.
          - **name** *(string) --*

            The unique name of the disk.
    """


_ClientGetDomainResponsedomaindomainEntriesTypeDef = TypedDict(
    "_ClientGetDomainResponsedomaindomainEntriesTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)


class ClientGetDomainResponsedomaindomainEntriesTypeDef(
    _ClientGetDomainResponsedomaindomainEntriesTypeDef
):
    pass


_ClientGetDomainResponsedomainlocationTypeDef = TypedDict(
    "_ClientGetDomainResponsedomainlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetDomainResponsedomainlocationTypeDef(_ClientGetDomainResponsedomainlocationTypeDef):
    pass


_ClientGetDomainResponsedomaintagsTypeDef = TypedDict(
    "_ClientGetDomainResponsedomaintagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetDomainResponsedomaintagsTypeDef(_ClientGetDomainResponsedomaintagsTypeDef):
    pass


_ClientGetDomainResponsedomainTypeDef = TypedDict(
    "_ClientGetDomainResponsedomainTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetDomainResponsedomainlocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetDomainResponsedomaintagsTypeDef],
        "domainEntries": List[ClientGetDomainResponsedomaindomainEntriesTypeDef],
    },
    total=False,
)


class ClientGetDomainResponsedomainTypeDef(_ClientGetDomainResponsedomainTypeDef):
    """
    - **domain** *(dict) --*

      An array of key-value pairs containing information about your get domain request.
      - **name** *(string) --*

        The name of the domain.
    """


_ClientGetDomainResponseTypeDef = TypedDict(
    "_ClientGetDomainResponseTypeDef", {"domain": ClientGetDomainResponsedomainTypeDef}, total=False
)


class ClientGetDomainResponseTypeDef(_ClientGetDomainResponseTypeDef):
    """
    - *(dict) --*

      - **domain** *(dict) --*

        An array of key-value pairs containing information about your get domain request.
        - **name** *(string) --*

          The name of the domain.
    """


_ClientGetDomainsResponsedomainsdomainEntriesTypeDef = TypedDict(
    "_ClientGetDomainsResponsedomainsdomainEntriesTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)


class ClientGetDomainsResponsedomainsdomainEntriesTypeDef(
    _ClientGetDomainsResponsedomainsdomainEntriesTypeDef
):
    pass


_ClientGetDomainsResponsedomainslocationTypeDef = TypedDict(
    "_ClientGetDomainsResponsedomainslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetDomainsResponsedomainslocationTypeDef(
    _ClientGetDomainsResponsedomainslocationTypeDef
):
    pass


_ClientGetDomainsResponsedomainstagsTypeDef = TypedDict(
    "_ClientGetDomainsResponsedomainstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetDomainsResponsedomainstagsTypeDef(_ClientGetDomainsResponsedomainstagsTypeDef):
    pass


_ClientGetDomainsResponsedomainsTypeDef = TypedDict(
    "_ClientGetDomainsResponsedomainsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetDomainsResponsedomainslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetDomainsResponsedomainstagsTypeDef],
        "domainEntries": List[ClientGetDomainsResponsedomainsdomainEntriesTypeDef],
    },
    total=False,
)


class ClientGetDomainsResponsedomainsTypeDef(_ClientGetDomainsResponsedomainsTypeDef):
    """
    - *(dict) --*

      Describes a domain where you are storing recordsets in Lightsail.
      - **name** *(string) --*

        The name of the domain.
    """


_ClientGetDomainsResponseTypeDef = TypedDict(
    "_ClientGetDomainsResponseTypeDef",
    {"domains": List[ClientGetDomainsResponsedomainsTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetDomainsResponseTypeDef(_ClientGetDomainsResponseTypeDef):
    """
    - *(dict) --*

      - **domains** *(list) --*

        An array of key-value pairs containing information about each of the domain entries in the
        user's account.
        - *(dict) --*

          Describes a domain where you are storing recordsets in Lightsail.
          - **name** *(string) --*

            The name of the domain.
    """


_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsdestinationInfoTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsdestinationInfoTypeDef",
    {"id": str, "service": str},
    total=False,
)


class ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsdestinationInfoTypeDef(
    _ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsdestinationInfoTypeDef
):
    pass


_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordslocationTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetExportSnapshotRecordsResponseexportSnapshotRecordslocationTypeDef(
    _ClientGetExportSnapshotRecordsResponseexportSnapshotRecordslocationTypeDef
):
    pass


_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef",
    {"sizeInGb": int},
    total=False,
)


class ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef(
    _ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef
):
    pass


_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef",
    {"name": str, "path": str, "sizeInGb": int, "isSystemDisk": bool},
    total=False,
)


class ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef(
    _ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef
):
    pass


_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef",
    {
        "fromBundleId": str,
        "fromBlueprintId": str,
        "fromDiskInfo": List[
            ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef
        ],
    },
    total=False,
)


class ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef(
    _ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef
):
    pass


_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoTypeDef",
    {
        "resourceType": Literal["InstanceSnapshot", "DiskSnapshot"],
        "createdAt": datetime,
        "name": str,
        "arn": str,
        "fromResourceName": str,
        "fromResourceArn": str,
        "instanceSnapshotInfo": ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef,
        "diskSnapshotInfo": ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef,
    },
    total=False,
)


class ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoTypeDef(
    _ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoTypeDef
):
    pass


_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": ClientGetExportSnapshotRecordsResponseexportSnapshotRecordslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "state": Literal["Started", "Succeeded", "Failed"],
        "sourceInfo": ClientGetExportSnapshotRecordsResponseexportSnapshotRecordssourceInfoTypeDef,
        "destinationInfo": ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsdestinationInfoTypeDef,
    },
    total=False,
)


class ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsTypeDef(
    _ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsTypeDef
):
    """
    - *(dict) --*

      Describes an export snapshot record.
      - **name** *(string) --*

        The export snapshot record name.
    """


_ClientGetExportSnapshotRecordsResponseTypeDef = TypedDict(
    "_ClientGetExportSnapshotRecordsResponseTypeDef",
    {
        "exportSnapshotRecords": List[
            ClientGetExportSnapshotRecordsResponseexportSnapshotRecordsTypeDef
        ],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetExportSnapshotRecordsResponseTypeDef(_ClientGetExportSnapshotRecordsResponseTypeDef):
    """
    - *(dict) --*

      - **exportSnapshotRecords** *(list) --*

        A list of objects describing the export snapshot records.
        - *(dict) --*

          Describes an export snapshot record.
          - **name** *(string) --*

            The export snapshot record name.
    """


_ClientGetInstanceAccessDetailsResponseaccessDetailshostKeysTypeDef = TypedDict(
    "_ClientGetInstanceAccessDetailsResponseaccessDetailshostKeysTypeDef",
    {
        "algorithm": str,
        "publicKey": str,
        "witnessedAt": datetime,
        "fingerprintSHA1": str,
        "fingerprintSHA256": str,
        "notValidBefore": datetime,
        "notValidAfter": datetime,
    },
    total=False,
)


class ClientGetInstanceAccessDetailsResponseaccessDetailshostKeysTypeDef(
    _ClientGetInstanceAccessDetailsResponseaccessDetailshostKeysTypeDef
):
    pass


_ClientGetInstanceAccessDetailsResponseaccessDetailspasswordDataTypeDef = TypedDict(
    "_ClientGetInstanceAccessDetailsResponseaccessDetailspasswordDataTypeDef",
    {"ciphertext": str, "keyPairName": str},
    total=False,
)


class ClientGetInstanceAccessDetailsResponseaccessDetailspasswordDataTypeDef(
    _ClientGetInstanceAccessDetailsResponseaccessDetailspasswordDataTypeDef
):
    pass


_ClientGetInstanceAccessDetailsResponseaccessDetailsTypeDef = TypedDict(
    "_ClientGetInstanceAccessDetailsResponseaccessDetailsTypeDef",
    {
        "certKey": str,
        "expiresAt": datetime,
        "ipAddress": str,
        "password": str,
        "passwordData": ClientGetInstanceAccessDetailsResponseaccessDetailspasswordDataTypeDef,
        "privateKey": str,
        "protocol": Literal["ssh", "rdp"],
        "instanceName": str,
        "username": str,
        "hostKeys": List[ClientGetInstanceAccessDetailsResponseaccessDetailshostKeysTypeDef],
    },
    total=False,
)


class ClientGetInstanceAccessDetailsResponseaccessDetailsTypeDef(
    _ClientGetInstanceAccessDetailsResponseaccessDetailsTypeDef
):
    """
    - **accessDetails** *(dict) --*

      An array of key-value pairs containing information about a get instance access request.
      - **certKey** *(string) --*

        For SSH access, the public key to use when accessing your instance For OpenSSH clients
        (e.g., command line SSH), you should save this value to ``tempkey-cert.pub`` .
    """


_ClientGetInstanceAccessDetailsResponseTypeDef = TypedDict(
    "_ClientGetInstanceAccessDetailsResponseTypeDef",
    {"accessDetails": ClientGetInstanceAccessDetailsResponseaccessDetailsTypeDef},
    total=False,
)


class ClientGetInstanceAccessDetailsResponseTypeDef(_ClientGetInstanceAccessDetailsResponseTypeDef):
    """
    - *(dict) --*

      - **accessDetails** *(dict) --*

        An array of key-value pairs containing information about a get instance access request.
        - **certKey** *(string) --*

          For SSH access, the public key to use when accessing your instance For OpenSSH clients
          (e.g., command line SSH), you should save this value to ``tempkey-cert.pub`` .
    """


_ClientGetInstanceMetricDataResponsemetricDataTypeDef = TypedDict(
    "_ClientGetInstanceMetricDataResponsemetricDataTypeDef",
    {
        "average": float,
        "maximum": float,
        "minimum": float,
        "sampleCount": float,
        "sum": float,
        "timestamp": datetime,
        "unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
    },
    total=False,
)


class ClientGetInstanceMetricDataResponsemetricDataTypeDef(
    _ClientGetInstanceMetricDataResponsemetricDataTypeDef
):
    pass


_ClientGetInstanceMetricDataResponseTypeDef = TypedDict(
    "_ClientGetInstanceMetricDataResponseTypeDef",
    {
        "metricName": Literal[
            "CPUUtilization",
            "NetworkIn",
            "NetworkOut",
            "StatusCheckFailed",
            "StatusCheckFailed_Instance",
            "StatusCheckFailed_System",
        ],
        "metricData": List[ClientGetInstanceMetricDataResponsemetricDataTypeDef],
    },
    total=False,
)


class ClientGetInstanceMetricDataResponseTypeDef(_ClientGetInstanceMetricDataResponseTypeDef):
    """
    - *(dict) --*

      - **metricName** *(string) --*

        The metric name to return data for.
    """


_ClientGetInstancePortStatesResponseportStatesTypeDef = TypedDict(
    "_ClientGetInstancePortStatesResponseportStatesTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": Literal["tcp", "all", "udp"],
        "state": Literal["open", "closed"],
    },
    total=False,
)


class ClientGetInstancePortStatesResponseportStatesTypeDef(
    _ClientGetInstancePortStatesResponseportStatesTypeDef
):
    """
    - *(dict) --*

      Describes the port state.
      - **fromPort** *(integer) --*

        The first port in the range.
    """


_ClientGetInstancePortStatesResponseTypeDef = TypedDict(
    "_ClientGetInstancePortStatesResponseTypeDef",
    {"portStates": List[ClientGetInstancePortStatesResponseportStatesTypeDef]},
    total=False,
)


class ClientGetInstancePortStatesResponseTypeDef(_ClientGetInstancePortStatesResponseTypeDef):
    """
    - *(dict) --*

      - **portStates** *(list) --*

        Information about the port states resulting from your request.
        - *(dict) --*

          Describes the port state.
          - **fromPort** *(integer) --*

            The first port in the range.
    """


_ClientGetInstanceResponseinstanceaddOnsTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstanceaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetInstanceResponseinstanceaddOnsTypeDef(
    _ClientGetInstanceResponseinstanceaddOnsTypeDef
):
    pass


_ClientGetInstanceResponseinstancehardwaredisksaddOnsTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancehardwaredisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetInstanceResponseinstancehardwaredisksaddOnsTypeDef(
    _ClientGetInstanceResponseinstancehardwaredisksaddOnsTypeDef
):
    pass


_ClientGetInstanceResponseinstancehardwarediskslocationTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancehardwarediskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstanceResponseinstancehardwarediskslocationTypeDef(
    _ClientGetInstanceResponseinstancehardwarediskslocationTypeDef
):
    pass


_ClientGetInstanceResponseinstancehardwarediskstagsTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancehardwarediskstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetInstanceResponseinstancehardwarediskstagsTypeDef(
    _ClientGetInstanceResponseinstancehardwarediskstagsTypeDef
):
    pass


_ClientGetInstanceResponseinstancehardwaredisksTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancehardwaredisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstanceResponseinstancehardwarediskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetInstanceResponseinstancehardwarediskstagsTypeDef],
        "addOns": List[ClientGetInstanceResponseinstancehardwaredisksaddOnsTypeDef],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class ClientGetInstanceResponseinstancehardwaredisksTypeDef(
    _ClientGetInstanceResponseinstancehardwaredisksTypeDef
):
    pass


_ClientGetInstanceResponseinstancehardwareTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancehardwareTypeDef",
    {
        "cpuCount": int,
        "disks": List[ClientGetInstanceResponseinstancehardwaredisksTypeDef],
        "ramSizeInGb": Any,
    },
    total=False,
)


class ClientGetInstanceResponseinstancehardwareTypeDef(
    _ClientGetInstanceResponseinstancehardwareTypeDef
):
    pass


_ClientGetInstanceResponseinstancelocationTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancelocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstanceResponseinstancelocationTypeDef(
    _ClientGetInstanceResponseinstancelocationTypeDef
):
    pass


_ClientGetInstanceResponseinstancenetworkingmonthlyTransferTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancenetworkingmonthlyTransferTypeDef",
    {"gbPerMonthAllocated": int},
    total=False,
)


class ClientGetInstanceResponseinstancenetworkingmonthlyTransferTypeDef(
    _ClientGetInstanceResponseinstancenetworkingmonthlyTransferTypeDef
):
    pass


_ClientGetInstanceResponseinstancenetworkingportsTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancenetworkingportsTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": Literal["tcp", "all", "udp"],
        "accessFrom": str,
        "accessType": Literal["Public", "Private"],
        "commonName": str,
        "accessDirection": Literal["inbound", "outbound"],
    },
    total=False,
)


class ClientGetInstanceResponseinstancenetworkingportsTypeDef(
    _ClientGetInstanceResponseinstancenetworkingportsTypeDef
):
    pass


_ClientGetInstanceResponseinstancenetworkingTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancenetworkingTypeDef",
    {
        "monthlyTransfer": ClientGetInstanceResponseinstancenetworkingmonthlyTransferTypeDef,
        "ports": List[ClientGetInstanceResponseinstancenetworkingportsTypeDef],
    },
    total=False,
)


class ClientGetInstanceResponseinstancenetworkingTypeDef(
    _ClientGetInstanceResponseinstancenetworkingTypeDef
):
    pass


_ClientGetInstanceResponseinstancestateTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancestateTypeDef", {"code": int, "name": str}, total=False
)


class ClientGetInstanceResponseinstancestateTypeDef(_ClientGetInstanceResponseinstancestateTypeDef):
    pass


_ClientGetInstanceResponseinstancetagsTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstancetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetInstanceResponseinstancetagsTypeDef(_ClientGetInstanceResponseinstancetagsTypeDef):
    pass


_ClientGetInstanceResponseinstanceTypeDef = TypedDict(
    "_ClientGetInstanceResponseinstanceTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstanceResponseinstancelocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetInstanceResponseinstancetagsTypeDef],
        "blueprintId": str,
        "blueprintName": str,
        "bundleId": str,
        "addOns": List[ClientGetInstanceResponseinstanceaddOnsTypeDef],
        "isStaticIp": bool,
        "privateIpAddress": str,
        "publicIpAddress": str,
        "ipv6Address": str,
        "hardware": ClientGetInstanceResponseinstancehardwareTypeDef,
        "networking": ClientGetInstanceResponseinstancenetworkingTypeDef,
        "state": ClientGetInstanceResponseinstancestateTypeDef,
        "username": str,
        "sshKeyName": str,
    },
    total=False,
)


class ClientGetInstanceResponseinstanceTypeDef(_ClientGetInstanceResponseinstanceTypeDef):
    """
    - **instance** *(dict) --*

      An array of key-value pairs containing information about the specified instance.
      - **name** *(string) --*

        The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
    """


_ClientGetInstanceResponseTypeDef = TypedDict(
    "_ClientGetInstanceResponseTypeDef",
    {"instance": ClientGetInstanceResponseinstanceTypeDef},
    total=False,
)


class ClientGetInstanceResponseTypeDef(_ClientGetInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **instance** *(dict) --*

        An array of key-value pairs containing information about the specified instance.
        - **name** *(string) --*

          The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
    """


_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksaddOnsTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksaddOnsTypeDef(
    _ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksaddOnsTypeDef
):
    pass


_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskslocationTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskslocationTypeDef(
    _ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskslocationTypeDef
):
    pass


_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskstagsTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskstagsTypeDef(
    _ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskstagsTypeDef
):
    pass


_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDiskstagsTypeDef],
        "addOns": List[
            ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksaddOnsTypeDef
        ],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksTypeDef(
    _ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksTypeDef
):
    pass


_ClientGetInstanceSnapshotResponseinstanceSnapshotlocationTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseinstanceSnapshotlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstanceSnapshotResponseinstanceSnapshotlocationTypeDef(
    _ClientGetInstanceSnapshotResponseinstanceSnapshotlocationTypeDef
):
    pass


_ClientGetInstanceSnapshotResponseinstanceSnapshottagsTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseinstanceSnapshottagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetInstanceSnapshotResponseinstanceSnapshottagsTypeDef(
    _ClientGetInstanceSnapshotResponseinstanceSnapshottagsTypeDef
):
    pass


_ClientGetInstanceSnapshotResponseinstanceSnapshotTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseinstanceSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstanceSnapshotResponseinstanceSnapshotlocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetInstanceSnapshotResponseinstanceSnapshottagsTypeDef],
        "state": Literal["pending", "error", "available"],
        "progress": str,
        "fromAttachedDisks": List[
            ClientGetInstanceSnapshotResponseinstanceSnapshotfromAttachedDisksTypeDef
        ],
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "fromBlueprintId": str,
        "fromBundleId": str,
        "isFromAutoSnapshot": bool,
        "sizeInGb": int,
    },
    total=False,
)


class ClientGetInstanceSnapshotResponseinstanceSnapshotTypeDef(
    _ClientGetInstanceSnapshotResponseinstanceSnapshotTypeDef
):
    """
    - **instanceSnapshot** *(dict) --*

      An array of key-value pairs containing information about the results of your get instance
      snapshot request.
      - **name** *(string) --*

        The name of the snapshot.
    """


_ClientGetInstanceSnapshotResponseTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotResponseTypeDef",
    {"instanceSnapshot": ClientGetInstanceSnapshotResponseinstanceSnapshotTypeDef},
    total=False,
)


class ClientGetInstanceSnapshotResponseTypeDef(_ClientGetInstanceSnapshotResponseTypeDef):
    """
    - *(dict) --*

      - **instanceSnapshot** *(dict) --*

        An array of key-value pairs containing information about the results of your get instance
        snapshot request.
        - **name** *(string) --*

          The name of the snapshot.
    """


_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef(
    _ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef
):
    pass


_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef(
    _ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef
):
    pass


_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef(
    _ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef
):
    pass


_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[
            ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef
        ],
        "addOns": List[
            ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef
        ],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksTypeDef(
    _ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksTypeDef
):
    pass


_ClientGetInstanceSnapshotsResponseinstanceSnapshotslocationTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseinstanceSnapshotslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstanceSnapshotsResponseinstanceSnapshotslocationTypeDef(
    _ClientGetInstanceSnapshotsResponseinstanceSnapshotslocationTypeDef
):
    pass


_ClientGetInstanceSnapshotsResponseinstanceSnapshotstagsTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseinstanceSnapshotstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetInstanceSnapshotsResponseinstanceSnapshotstagsTypeDef(
    _ClientGetInstanceSnapshotsResponseinstanceSnapshotstagsTypeDef
):
    pass


_ClientGetInstanceSnapshotsResponseinstanceSnapshotsTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseinstanceSnapshotsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstanceSnapshotsResponseinstanceSnapshotslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetInstanceSnapshotsResponseinstanceSnapshotstagsTypeDef],
        "state": Literal["pending", "error", "available"],
        "progress": str,
        "fromAttachedDisks": List[
            ClientGetInstanceSnapshotsResponseinstanceSnapshotsfromAttachedDisksTypeDef
        ],
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "fromBlueprintId": str,
        "fromBundleId": str,
        "isFromAutoSnapshot": bool,
        "sizeInGb": int,
    },
    total=False,
)


class ClientGetInstanceSnapshotsResponseinstanceSnapshotsTypeDef(
    _ClientGetInstanceSnapshotsResponseinstanceSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes an instance snapshot.
      - **name** *(string) --*

        The name of the snapshot.
    """


_ClientGetInstanceSnapshotsResponseTypeDef = TypedDict(
    "_ClientGetInstanceSnapshotsResponseTypeDef",
    {
        "instanceSnapshots": List[ClientGetInstanceSnapshotsResponseinstanceSnapshotsTypeDef],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetInstanceSnapshotsResponseTypeDef(_ClientGetInstanceSnapshotsResponseTypeDef):
    """
    - *(dict) --*

      - **instanceSnapshots** *(list) --*

        An array of key-value pairs containing information about the results of your get instance
        snapshots request.
        - *(dict) --*

          Describes an instance snapshot.
          - **name** *(string) --*

            The name of the snapshot.
    """


_ClientGetInstanceStateResponsestateTypeDef = TypedDict(
    "_ClientGetInstanceStateResponsestateTypeDef", {"code": int, "name": str}, total=False
)


class ClientGetInstanceStateResponsestateTypeDef(_ClientGetInstanceStateResponsestateTypeDef):
    """
    - **state** *(dict) --*

      The state of the instance.
      - **code** *(integer) --*

        The status code for the instance.
    """


_ClientGetInstanceStateResponseTypeDef = TypedDict(
    "_ClientGetInstanceStateResponseTypeDef",
    {"state": ClientGetInstanceStateResponsestateTypeDef},
    total=False,
)


class ClientGetInstanceStateResponseTypeDef(_ClientGetInstanceStateResponseTypeDef):
    """
    - *(dict) --*

      - **state** *(dict) --*

        The state of the instance.
        - **code** *(integer) --*

          The status code for the instance.
    """


_ClientGetInstancesResponseinstancesaddOnsTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstancesaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetInstancesResponseinstancesaddOnsTypeDef(
    _ClientGetInstancesResponseinstancesaddOnsTypeDef
):
    pass


_ClientGetInstancesResponseinstanceshardwaredisksaddOnsTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstanceshardwaredisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class ClientGetInstancesResponseinstanceshardwaredisksaddOnsTypeDef(
    _ClientGetInstancesResponseinstanceshardwaredisksaddOnsTypeDef
):
    pass


_ClientGetInstancesResponseinstanceshardwarediskslocationTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstanceshardwarediskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstancesResponseinstanceshardwarediskslocationTypeDef(
    _ClientGetInstancesResponseinstanceshardwarediskslocationTypeDef
):
    pass


_ClientGetInstancesResponseinstanceshardwarediskstagsTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstanceshardwarediskstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetInstancesResponseinstanceshardwarediskstagsTypeDef(
    _ClientGetInstancesResponseinstanceshardwarediskstagsTypeDef
):
    pass


_ClientGetInstancesResponseinstanceshardwaredisksTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstanceshardwaredisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstancesResponseinstanceshardwarediskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetInstancesResponseinstanceshardwarediskstagsTypeDef],
        "addOns": List[ClientGetInstancesResponseinstanceshardwaredisksaddOnsTypeDef],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class ClientGetInstancesResponseinstanceshardwaredisksTypeDef(
    _ClientGetInstancesResponseinstanceshardwaredisksTypeDef
):
    pass


_ClientGetInstancesResponseinstanceshardwareTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstanceshardwareTypeDef",
    {
        "cpuCount": int,
        "disks": List[ClientGetInstancesResponseinstanceshardwaredisksTypeDef],
        "ramSizeInGb": Any,
    },
    total=False,
)


class ClientGetInstancesResponseinstanceshardwareTypeDef(
    _ClientGetInstancesResponseinstanceshardwareTypeDef
):
    pass


_ClientGetInstancesResponseinstanceslocationTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstanceslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetInstancesResponseinstanceslocationTypeDef(
    _ClientGetInstancesResponseinstanceslocationTypeDef
):
    pass


_ClientGetInstancesResponseinstancesnetworkingmonthlyTransferTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstancesnetworkingmonthlyTransferTypeDef",
    {"gbPerMonthAllocated": int},
    total=False,
)


class ClientGetInstancesResponseinstancesnetworkingmonthlyTransferTypeDef(
    _ClientGetInstancesResponseinstancesnetworkingmonthlyTransferTypeDef
):
    pass


_ClientGetInstancesResponseinstancesnetworkingportsTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstancesnetworkingportsTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": Literal["tcp", "all", "udp"],
        "accessFrom": str,
        "accessType": Literal["Public", "Private"],
        "commonName": str,
        "accessDirection": Literal["inbound", "outbound"],
    },
    total=False,
)


class ClientGetInstancesResponseinstancesnetworkingportsTypeDef(
    _ClientGetInstancesResponseinstancesnetworkingportsTypeDef
):
    pass


_ClientGetInstancesResponseinstancesnetworkingTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstancesnetworkingTypeDef",
    {
        "monthlyTransfer": ClientGetInstancesResponseinstancesnetworkingmonthlyTransferTypeDef,
        "ports": List[ClientGetInstancesResponseinstancesnetworkingportsTypeDef],
    },
    total=False,
)


class ClientGetInstancesResponseinstancesnetworkingTypeDef(
    _ClientGetInstancesResponseinstancesnetworkingTypeDef
):
    pass


_ClientGetInstancesResponseinstancesstateTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstancesstateTypeDef", {"code": int, "name": str}, total=False
)


class ClientGetInstancesResponseinstancesstateTypeDef(
    _ClientGetInstancesResponseinstancesstateTypeDef
):
    pass


_ClientGetInstancesResponseinstancestagsTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstancestagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetInstancesResponseinstancestagsTypeDef(
    _ClientGetInstancesResponseinstancestagsTypeDef
):
    pass


_ClientGetInstancesResponseinstancesTypeDef = TypedDict(
    "_ClientGetInstancesResponseinstancesTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetInstancesResponseinstanceslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetInstancesResponseinstancestagsTypeDef],
        "blueprintId": str,
        "blueprintName": str,
        "bundleId": str,
        "addOns": List[ClientGetInstancesResponseinstancesaddOnsTypeDef],
        "isStaticIp": bool,
        "privateIpAddress": str,
        "publicIpAddress": str,
        "ipv6Address": str,
        "hardware": ClientGetInstancesResponseinstanceshardwareTypeDef,
        "networking": ClientGetInstancesResponseinstancesnetworkingTypeDef,
        "state": ClientGetInstancesResponseinstancesstateTypeDef,
        "username": str,
        "sshKeyName": str,
    },
    total=False,
)


class ClientGetInstancesResponseinstancesTypeDef(_ClientGetInstancesResponseinstancesTypeDef):
    """
    - *(dict) --*

      Describes an instance (a virtual private server).
      - **name** *(string) --*

        The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
    """


_ClientGetInstancesResponseTypeDef = TypedDict(
    "_ClientGetInstancesResponseTypeDef",
    {"instances": List[ClientGetInstancesResponseinstancesTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetInstancesResponseTypeDef(_ClientGetInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **instances** *(list) --*

        An array of key-value pairs containing information about your instances.
        - *(dict) --*

          Describes an instance (a virtual private server).
          - **name** *(string) --*

            The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
    """


_ClientGetKeyPairResponsekeyPairlocationTypeDef = TypedDict(
    "_ClientGetKeyPairResponsekeyPairlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetKeyPairResponsekeyPairlocationTypeDef(
    _ClientGetKeyPairResponsekeyPairlocationTypeDef
):
    pass


_ClientGetKeyPairResponsekeyPairtagsTypeDef = TypedDict(
    "_ClientGetKeyPairResponsekeyPairtagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetKeyPairResponsekeyPairtagsTypeDef(_ClientGetKeyPairResponsekeyPairtagsTypeDef):
    pass


_ClientGetKeyPairResponsekeyPairTypeDef = TypedDict(
    "_ClientGetKeyPairResponsekeyPairTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetKeyPairResponsekeyPairlocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetKeyPairResponsekeyPairtagsTypeDef],
        "fingerprint": str,
    },
    total=False,
)


class ClientGetKeyPairResponsekeyPairTypeDef(_ClientGetKeyPairResponsekeyPairTypeDef):
    """
    - **keyPair** *(dict) --*

      An array of key-value pairs containing information about the key pair.
      - **name** *(string) --*

        The friendly name of the SSH key pair.
    """


_ClientGetKeyPairResponseTypeDef = TypedDict(
    "_ClientGetKeyPairResponseTypeDef",
    {"keyPair": ClientGetKeyPairResponsekeyPairTypeDef},
    total=False,
)


class ClientGetKeyPairResponseTypeDef(_ClientGetKeyPairResponseTypeDef):
    """
    - *(dict) --*

      - **keyPair** *(dict) --*

        An array of key-value pairs containing information about the key pair.
        - **name** *(string) --*

          The friendly name of the SSH key pair.
    """


_ClientGetKeyPairsResponsekeyPairslocationTypeDef = TypedDict(
    "_ClientGetKeyPairsResponsekeyPairslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetKeyPairsResponsekeyPairslocationTypeDef(
    _ClientGetKeyPairsResponsekeyPairslocationTypeDef
):
    pass


_ClientGetKeyPairsResponsekeyPairstagsTypeDef = TypedDict(
    "_ClientGetKeyPairsResponsekeyPairstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetKeyPairsResponsekeyPairstagsTypeDef(_ClientGetKeyPairsResponsekeyPairstagsTypeDef):
    pass


_ClientGetKeyPairsResponsekeyPairsTypeDef = TypedDict(
    "_ClientGetKeyPairsResponsekeyPairsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetKeyPairsResponsekeyPairslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetKeyPairsResponsekeyPairstagsTypeDef],
        "fingerprint": str,
    },
    total=False,
)


class ClientGetKeyPairsResponsekeyPairsTypeDef(_ClientGetKeyPairsResponsekeyPairsTypeDef):
    """
    - *(dict) --*

      Describes the SSH key pair.
      - **name** *(string) --*

        The friendly name of the SSH key pair.
    """


_ClientGetKeyPairsResponseTypeDef = TypedDict(
    "_ClientGetKeyPairsResponseTypeDef",
    {"keyPairs": List[ClientGetKeyPairsResponsekeyPairsTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetKeyPairsResponseTypeDef(_ClientGetKeyPairsResponseTypeDef):
    """
    - *(dict) --*

      - **keyPairs** *(list) --*

        An array of key-value pairs containing information about the key pairs.
        - *(dict) --*

          Describes the SSH key pair.
          - **name** *(string) --*

            The friendly name of the SSH key pair.
    """


_ClientGetLoadBalancerMetricDataResponsemetricDataTypeDef = TypedDict(
    "_ClientGetLoadBalancerMetricDataResponsemetricDataTypeDef",
    {
        "average": float,
        "maximum": float,
        "minimum": float,
        "sampleCount": float,
        "sum": float,
        "timestamp": datetime,
        "unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
    },
    total=False,
)


class ClientGetLoadBalancerMetricDataResponsemetricDataTypeDef(
    _ClientGetLoadBalancerMetricDataResponsemetricDataTypeDef
):
    pass


_ClientGetLoadBalancerMetricDataResponseTypeDef = TypedDict(
    "_ClientGetLoadBalancerMetricDataResponseTypeDef",
    {
        "metricName": Literal[
            "ClientTLSNegotiationErrorCount",
            "HealthyHostCount",
            "UnhealthyHostCount",
            "HTTPCode_LB_4XX_Count",
            "HTTPCode_LB_5XX_Count",
            "HTTPCode_Instance_2XX_Count",
            "HTTPCode_Instance_3XX_Count",
            "HTTPCode_Instance_4XX_Count",
            "HTTPCode_Instance_5XX_Count",
            "InstanceResponseTime",
            "RejectedConnectionCount",
            "RequestCount",
        ],
        "metricData": List[ClientGetLoadBalancerMetricDataResponsemetricDataTypeDef],
    },
    total=False,
)


class ClientGetLoadBalancerMetricDataResponseTypeDef(
    _ClientGetLoadBalancerMetricDataResponseTypeDef
):
    """
    - *(dict) --*

      - **metricName** *(string) --*

        The metric about which you are receiving information. Valid values are listed below, along
        with the most useful ``statistics`` to include in your request.
        * **``ClientTLSNegotiationErrorCount`` ** - The number of TLS connections initiated by the
        client that did not establish a session with the load balancer. Possible causes include a
        mismatch of ciphers or protocols.  ``Statistics`` : The most useful statistic is ``Sum`` .
        * **``HealthyHostCount`` ** - The number of target instances that are considered healthy.
        ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and ``Maximum`` .
        * **``UnhealthyHostCount`` ** - The number of target instances that are considered
        unhealthy.  ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and
        ``Maximum`` .
        * **``HTTPCode_LB_4XX_Count`` ** - The number of HTTP 4XX client error codes that originate
        from the load balancer. Client errors are generated when requests are malformed or
        incomplete. These requests have not been received by the target instance. This count does
        not include any response codes generated by the target instances.  ``Statistics`` : The most
        useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all
        return ``1`` .
        * **``HTTPCode_LB_5XX_Count`` ** - The number of HTTP 5XX server error codes that originate
        from the load balancer. This count does not include any response codes generated by the
        target instances.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that
        ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . Note that ``Minimum`` ,
        ``Maximum`` , and ``Average`` all return ``1`` .
        * **``HTTPCode_Instance_2XX_Count`` ** - The number of HTTP response codes generated by the
        target instances. This does not include any response codes generated by the load balancer.
        ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum``
        , and ``Average`` all return ``1`` .
        * **``HTTPCode_Instance_3XX_Count`` ** - The number of HTTP response codes generated by the
        target instances. This does not include any response codes generated by the load balancer.
        ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum``
        , and ``Average`` all return ``1`` .
        * **``HTTPCode_Instance_4XX_Count`` ** - The number of HTTP response codes generated by the
        target instances. This does not include any response codes generated by the load balancer.
        ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum``
        , and ``Average`` all return ``1`` .
        * **``HTTPCode_Instance_5XX_Count`` ** - The number of HTTP response codes generated by the
        target instances. This does not include any response codes generated by the load balancer.
        ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum``
        , and ``Average`` all return ``1`` .
        * **``InstanceResponseTime`` ** - The time elapsed, in seconds, after the request leaves the
        load balancer until a response from the target instance is received.  ``Statistics`` : The
        most useful statistic is ``Average`` .
        * **``RejectedConnectionCount`` ** - The number of connections that were rejected because
        the load balancer had reached its maximum number of connections.  ``Statistics`` : The most
        useful statistic is ``Sum`` .
        * **``RequestCount`` ** - The number of requests processed over IPv4. This count includes
        only the requests with a response generated by a target instance of the load balancer.
        ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum``
        , and ``Average`` all return ``1`` .
    """


_ClientGetLoadBalancerResponseloadBalancerinstanceHealthSummaryTypeDef = TypedDict(
    "_ClientGetLoadBalancerResponseloadBalancerinstanceHealthSummaryTypeDef",
    {
        "instanceName": str,
        "instanceHealth": Literal[
            "initial", "healthy", "unhealthy", "unused", "draining", "unavailable"
        ],
        "instanceHealthReason": Literal[
            "Lb.RegistrationInProgress",
            "Lb.InitialHealthChecking",
            "Lb.InternalError",
            "Instance.ResponseCodeMismatch",
            "Instance.Timeout",
            "Instance.FailedHealthChecks",
            "Instance.NotRegistered",
            "Instance.NotInUse",
            "Instance.DeregistrationInProgress",
            "Instance.InvalidState",
            "Instance.IpUnusable",
        ],
    },
    total=False,
)


class ClientGetLoadBalancerResponseloadBalancerinstanceHealthSummaryTypeDef(
    _ClientGetLoadBalancerResponseloadBalancerinstanceHealthSummaryTypeDef
):
    pass


_ClientGetLoadBalancerResponseloadBalancerlocationTypeDef = TypedDict(
    "_ClientGetLoadBalancerResponseloadBalancerlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetLoadBalancerResponseloadBalancerlocationTypeDef(
    _ClientGetLoadBalancerResponseloadBalancerlocationTypeDef
):
    pass


_ClientGetLoadBalancerResponseloadBalancertagsTypeDef = TypedDict(
    "_ClientGetLoadBalancerResponseloadBalancertagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetLoadBalancerResponseloadBalancertagsTypeDef(
    _ClientGetLoadBalancerResponseloadBalancertagsTypeDef
):
    pass


_ClientGetLoadBalancerResponseloadBalancertlsCertificateSummariesTypeDef = TypedDict(
    "_ClientGetLoadBalancerResponseloadBalancertlsCertificateSummariesTypeDef",
    {"name": str, "isAttached": bool},
    total=False,
)


class ClientGetLoadBalancerResponseloadBalancertlsCertificateSummariesTypeDef(
    _ClientGetLoadBalancerResponseloadBalancertlsCertificateSummariesTypeDef
):
    pass


_ClientGetLoadBalancerResponseloadBalancerTypeDef = TypedDict(
    "_ClientGetLoadBalancerResponseloadBalancerTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetLoadBalancerResponseloadBalancerlocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetLoadBalancerResponseloadBalancertagsTypeDef],
        "dnsName": str,
        "state": Literal["active", "provisioning", "active_impaired", "failed", "unknown"],
        "protocol": Literal["HTTP_HTTPS", "HTTP"],
        "publicPorts": List[int],
        "healthCheckPath": str,
        "instancePort": int,
        "instanceHealthSummary": List[
            ClientGetLoadBalancerResponseloadBalancerinstanceHealthSummaryTypeDef
        ],
        "tlsCertificateSummaries": List[
            ClientGetLoadBalancerResponseloadBalancertlsCertificateSummariesTypeDef
        ],
        "configurationOptions": Dict[str, str],
    },
    total=False,
)


class ClientGetLoadBalancerResponseloadBalancerTypeDef(
    _ClientGetLoadBalancerResponseloadBalancerTypeDef
):
    """
    - **loadBalancer** *(dict) --*

      An object containing information about your load balancer.
      - **name** *(string) --*

        The name of the load balancer (e.g., ``my-load-balancer`` ).
    """


_ClientGetLoadBalancerResponseTypeDef = TypedDict(
    "_ClientGetLoadBalancerResponseTypeDef",
    {"loadBalancer": ClientGetLoadBalancerResponseloadBalancerTypeDef},
    total=False,
)


class ClientGetLoadBalancerResponseTypeDef(_ClientGetLoadBalancerResponseTypeDef):
    """
    - *(dict) --*

      - **loadBalancer** *(dict) --*

        An object containing information about your load balancer.
        - **name** *(string) --*

          The name of the load balancer (e.g., ``my-load-balancer`` ).
    """


_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesdomainValidationRecordsTypeDef = TypedDict(
    "_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesdomainValidationRecordsTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
        "validationStatus": Literal["PENDING_VALIDATION", "FAILED", "SUCCESS"],
        "domainName": str,
    },
    total=False,
)


class ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesdomainValidationRecordsTypeDef(
    _ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesdomainValidationRecordsTypeDef
):
    pass


_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificateslocationTypeDef = TypedDict(
    "_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificateslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetLoadBalancerTlsCertificatesResponsetlsCertificateslocationTypeDef(
    _ClientGetLoadBalancerTlsCertificatesResponsetlsCertificateslocationTypeDef
):
    pass


_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummarydomainValidationOptionsTypeDef = TypedDict(
    "_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummarydomainValidationOptionsTypeDef",
    {"domainName": str, "validationStatus": Literal["PENDING_VALIDATION", "FAILED", "SUCCESS"]},
    total=False,
)


class ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummarydomainValidationOptionsTypeDef(
    _ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummarydomainValidationOptionsTypeDef
):
    pass


_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummaryTypeDef = TypedDict(
    "_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummaryTypeDef",
    {
        "renewalStatus": Literal["PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "domainValidationOptions": List[
            ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummarydomainValidationOptionsTypeDef
        ],
    },
    total=False,
)


class ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummaryTypeDef(
    _ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummaryTypeDef
):
    pass


_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatestagsTypeDef = TypedDict(
    "_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatestagsTypeDef(
    _ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatestagsTypeDef
):
    pass


_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesTypeDef = TypedDict(
    "_ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetLoadBalancerTlsCertificatesResponsetlsCertificateslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatestagsTypeDef],
        "loadBalancerName": str,
        "isAttached": bool,
        "status": Literal[
            "PENDING_VALIDATION",
            "ISSUED",
            "INACTIVE",
            "EXPIRED",
            "VALIDATION_TIMED_OUT",
            "REVOKED",
            "FAILED",
            "UNKNOWN",
        ],
        "domainName": str,
        "domainValidationRecords": List[
            ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesdomainValidationRecordsTypeDef
        ],
        "failureReason": Literal[
            "NO_AVAILABLE_CONTACTS",
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "OTHER",
        ],
        "issuedAt": datetime,
        "issuer": str,
        "keyAlgorithm": str,
        "notAfter": datetime,
        "notBefore": datetime,
        "renewalSummary": ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesrenewalSummaryTypeDef,
        "revocationReason": Literal[
            "UNSPECIFIED",
            "KEY_COMPROMISE",
            "CA_COMPROMISE",
            "AFFILIATION_CHANGED",
            "SUPERCEDED",
            "CESSATION_OF_OPERATION",
            "CERTIFICATE_HOLD",
            "REMOVE_FROM_CRL",
            "PRIVILEGE_WITHDRAWN",
            "A_A_COMPROMISE",
        ],
        "revokedAt": datetime,
        "serial": str,
        "signatureAlgorithm": str,
        "subject": str,
        "subjectAlternativeNames": List[str],
    },
    total=False,
)


class ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesTypeDef(
    _ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesTypeDef
):
    """
    - *(dict) --*

      Describes a load balancer SSL/TLS certificate.
      TLS is just an updated, more secure version of Secure Socket Layer (SSL).
      - **name** *(string) --*

        The name of the SSL/TLS certificate (e.g., ``my-certificate`` ).
    """


_ClientGetLoadBalancerTlsCertificatesResponseTypeDef = TypedDict(
    "_ClientGetLoadBalancerTlsCertificatesResponseTypeDef",
    {"tlsCertificates": List[ClientGetLoadBalancerTlsCertificatesResponsetlsCertificatesTypeDef]},
    total=False,
)


class ClientGetLoadBalancerTlsCertificatesResponseTypeDef(
    _ClientGetLoadBalancerTlsCertificatesResponseTypeDef
):
    """
    - *(dict) --*

      - **tlsCertificates** *(list) --*

        An array of LoadBalancerTlsCertificate objects describing your SSL/TLS certificates.
        - *(dict) --*

          Describes a load balancer SSL/TLS certificate.
          TLS is just an updated, more secure version of Secure Socket Layer (SSL).
          - **name** *(string) --*

            The name of the SSL/TLS certificate (e.g., ``my-certificate`` ).
    """


_ClientGetLoadBalancersResponseloadBalancersinstanceHealthSummaryTypeDef = TypedDict(
    "_ClientGetLoadBalancersResponseloadBalancersinstanceHealthSummaryTypeDef",
    {
        "instanceName": str,
        "instanceHealth": Literal[
            "initial", "healthy", "unhealthy", "unused", "draining", "unavailable"
        ],
        "instanceHealthReason": Literal[
            "Lb.RegistrationInProgress",
            "Lb.InitialHealthChecking",
            "Lb.InternalError",
            "Instance.ResponseCodeMismatch",
            "Instance.Timeout",
            "Instance.FailedHealthChecks",
            "Instance.NotRegistered",
            "Instance.NotInUse",
            "Instance.DeregistrationInProgress",
            "Instance.InvalidState",
            "Instance.IpUnusable",
        ],
    },
    total=False,
)


class ClientGetLoadBalancersResponseloadBalancersinstanceHealthSummaryTypeDef(
    _ClientGetLoadBalancersResponseloadBalancersinstanceHealthSummaryTypeDef
):
    pass


_ClientGetLoadBalancersResponseloadBalancerslocationTypeDef = TypedDict(
    "_ClientGetLoadBalancersResponseloadBalancerslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetLoadBalancersResponseloadBalancerslocationTypeDef(
    _ClientGetLoadBalancersResponseloadBalancerslocationTypeDef
):
    pass


_ClientGetLoadBalancersResponseloadBalancerstagsTypeDef = TypedDict(
    "_ClientGetLoadBalancersResponseloadBalancerstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetLoadBalancersResponseloadBalancerstagsTypeDef(
    _ClientGetLoadBalancersResponseloadBalancerstagsTypeDef
):
    pass


_ClientGetLoadBalancersResponseloadBalancerstlsCertificateSummariesTypeDef = TypedDict(
    "_ClientGetLoadBalancersResponseloadBalancerstlsCertificateSummariesTypeDef",
    {"name": str, "isAttached": bool},
    total=False,
)


class ClientGetLoadBalancersResponseloadBalancerstlsCertificateSummariesTypeDef(
    _ClientGetLoadBalancersResponseloadBalancerstlsCertificateSummariesTypeDef
):
    pass


_ClientGetLoadBalancersResponseloadBalancersTypeDef = TypedDict(
    "_ClientGetLoadBalancersResponseloadBalancersTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetLoadBalancersResponseloadBalancerslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetLoadBalancersResponseloadBalancerstagsTypeDef],
        "dnsName": str,
        "state": Literal["active", "provisioning", "active_impaired", "failed", "unknown"],
        "protocol": Literal["HTTP_HTTPS", "HTTP"],
        "publicPorts": List[int],
        "healthCheckPath": str,
        "instancePort": int,
        "instanceHealthSummary": List[
            ClientGetLoadBalancersResponseloadBalancersinstanceHealthSummaryTypeDef
        ],
        "tlsCertificateSummaries": List[
            ClientGetLoadBalancersResponseloadBalancerstlsCertificateSummariesTypeDef
        ],
        "configurationOptions": Dict[str, str],
    },
    total=False,
)


class ClientGetLoadBalancersResponseloadBalancersTypeDef(
    _ClientGetLoadBalancersResponseloadBalancersTypeDef
):
    """
    - *(dict) --*

      Describes the Lightsail load balancer.
      - **name** *(string) --*

        The name of the load balancer (e.g., ``my-load-balancer`` ).
    """


_ClientGetLoadBalancersResponseTypeDef = TypedDict(
    "_ClientGetLoadBalancersResponseTypeDef",
    {
        "loadBalancers": List[ClientGetLoadBalancersResponseloadBalancersTypeDef],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetLoadBalancersResponseTypeDef(_ClientGetLoadBalancersResponseTypeDef):
    """
    - *(dict) --*

      - **loadBalancers** *(list) --*

        An array of LoadBalancer objects describing your load balancers.
        - *(dict) --*

          Describes the Lightsail load balancer.
          - **name** *(string) --*

            The name of the load balancer (e.g., ``my-load-balancer`` ).
    """


_ClientGetOperationResponseoperationlocationTypeDef = TypedDict(
    "_ClientGetOperationResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetOperationResponseoperationlocationTypeDef(
    _ClientGetOperationResponseoperationlocationTypeDef
):
    pass


_ClientGetOperationResponseoperationTypeDef = TypedDict(
    "_ClientGetOperationResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientGetOperationResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientGetOperationResponseoperationTypeDef(_ClientGetOperationResponseoperationTypeDef):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the results of your get operation
      request.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientGetOperationResponseTypeDef = TypedDict(
    "_ClientGetOperationResponseTypeDef",
    {"operation": ClientGetOperationResponseoperationTypeDef},
    total=False,
)


class ClientGetOperationResponseTypeDef(_ClientGetOperationResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the results of your get operation
        request.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientGetOperationsForResourceResponseoperationslocationTypeDef = TypedDict(
    "_ClientGetOperationsForResourceResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetOperationsForResourceResponseoperationslocationTypeDef(
    _ClientGetOperationsForResourceResponseoperationslocationTypeDef
):
    pass


_ClientGetOperationsForResourceResponseoperationsTypeDef = TypedDict(
    "_ClientGetOperationsForResourceResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientGetOperationsForResourceResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientGetOperationsForResourceResponseoperationsTypeDef(
    _ClientGetOperationsForResourceResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientGetOperationsForResourceResponseTypeDef = TypedDict(
    "_ClientGetOperationsForResourceResponseTypeDef",
    {
        "operations": List[ClientGetOperationsForResourceResponseoperationsTypeDef],
        "nextPageCount": str,
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetOperationsForResourceResponseTypeDef(_ClientGetOperationsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your get operations
        for resource request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientGetOperationsResponseoperationslocationTypeDef = TypedDict(
    "_ClientGetOperationsResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetOperationsResponseoperationslocationTypeDef(
    _ClientGetOperationsResponseoperationslocationTypeDef
):
    pass


_ClientGetOperationsResponseoperationsTypeDef = TypedDict(
    "_ClientGetOperationsResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientGetOperationsResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientGetOperationsResponseoperationsTypeDef(_ClientGetOperationsResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientGetOperationsResponseTypeDef = TypedDict(
    "_ClientGetOperationsResponseTypeDef",
    {"operations": List[ClientGetOperationsResponseoperationsTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetOperationsResponseTypeDef(_ClientGetOperationsResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your get operations
        request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientGetRegionsResponseregionsavailabilityZonesTypeDef = TypedDict(
    "_ClientGetRegionsResponseregionsavailabilityZonesTypeDef",
    {"zoneName": str, "state": str},
    total=False,
)


class ClientGetRegionsResponseregionsavailabilityZonesTypeDef(
    _ClientGetRegionsResponseregionsavailabilityZonesTypeDef
):
    pass


_ClientGetRegionsResponseregionsrelationalDatabaseAvailabilityZonesTypeDef = TypedDict(
    "_ClientGetRegionsResponseregionsrelationalDatabaseAvailabilityZonesTypeDef",
    {"zoneName": str, "state": str},
    total=False,
)


class ClientGetRegionsResponseregionsrelationalDatabaseAvailabilityZonesTypeDef(
    _ClientGetRegionsResponseregionsrelationalDatabaseAvailabilityZonesTypeDef
):
    pass


_ClientGetRegionsResponseregionsTypeDef = TypedDict(
    "_ClientGetRegionsResponseregionsTypeDef",
    {
        "continentCode": str,
        "description": str,
        "displayName": str,
        "name": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
        "availabilityZones": List[ClientGetRegionsResponseregionsavailabilityZonesTypeDef],
        "relationalDatabaseAvailabilityZones": List[
            ClientGetRegionsResponseregionsrelationalDatabaseAvailabilityZonesTypeDef
        ],
    },
    total=False,
)


class ClientGetRegionsResponseregionsTypeDef(_ClientGetRegionsResponseregionsTypeDef):
    """
    - *(dict) --*

      Describes the AWS Region.
      - **continentCode** *(string) --*

        The continent code (e.g., ``NA`` , meaning North America).
    """


_ClientGetRegionsResponseTypeDef = TypedDict(
    "_ClientGetRegionsResponseTypeDef",
    {"regions": List[ClientGetRegionsResponseregionsTypeDef]},
    total=False,
)


class ClientGetRegionsResponseTypeDef(_ClientGetRegionsResponseTypeDef):
    """
    - *(dict) --*

      - **regions** *(list) --*

        An array of key-value pairs containing information about your get regions request.
        - *(dict) --*

          Describes the AWS Region.
          - **continentCode** *(string) --*

            The continent code (e.g., ``NA`` , meaning North America).
    """


_ClientGetRelationalDatabaseBlueprintsResponseblueprintsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseBlueprintsResponseblueprintsTypeDef",
    {
        "blueprintId": str,
        "engine": str,
        "engineVersion": str,
        "engineDescription": str,
        "engineVersionDescription": str,
        "isEngineDefault": bool,
    },
    total=False,
)


class ClientGetRelationalDatabaseBlueprintsResponseblueprintsTypeDef(
    _ClientGetRelationalDatabaseBlueprintsResponseblueprintsTypeDef
):
    """
    - *(dict) --*

      Describes a database image, or blueprint. A blueprint describes the major engine version of a
      database.
      - **blueprintId** *(string) --*

        The ID for the database blueprint.
    """


_ClientGetRelationalDatabaseBlueprintsResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseBlueprintsResponseTypeDef",
    {
        "blueprints": List[ClientGetRelationalDatabaseBlueprintsResponseblueprintsTypeDef],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseBlueprintsResponseTypeDef(
    _ClientGetRelationalDatabaseBlueprintsResponseTypeDef
):
    """
    - *(dict) --*

      - **blueprints** *(list) --*

        An object describing the result of your get relational database blueprints request.
        - *(dict) --*

          Describes a database image, or blueprint. A blueprint describes the major engine version
          of a database.
          - **blueprintId** *(string) --*

            The ID for the database blueprint.
    """


_ClientGetRelationalDatabaseBundlesResponsebundlesTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseBundlesResponsebundlesTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": Any,
        "ramSizeInGb": Any,
        "diskSizeInGb": int,
        "transferPerMonthInGb": int,
        "cpuCount": int,
        "isEncrypted": bool,
        "isActive": bool,
    },
    total=False,
)


class ClientGetRelationalDatabaseBundlesResponsebundlesTypeDef(
    _ClientGetRelationalDatabaseBundlesResponsebundlesTypeDef
):
    """
    - *(dict) --*

      Describes a database bundle. A bundle describes the performance specifications of the
      database.
      - **bundleId** *(string) --*

        The ID for the database bundle.
    """


_ClientGetRelationalDatabaseBundlesResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseBundlesResponseTypeDef",
    {
        "bundles": List[ClientGetRelationalDatabaseBundlesResponsebundlesTypeDef],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseBundlesResponseTypeDef(
    _ClientGetRelationalDatabaseBundlesResponseTypeDef
):
    """
    - *(dict) --*

      - **bundles** *(list) --*

        An object describing the result of your get relational database bundles request.
        - *(dict) --*

          Describes a database bundle. A bundle describes the performance specifications of the
          database.
          - **bundleId** *(string) --*

            The ID for the database bundle.
    """


_ClientGetRelationalDatabaseEventsResponserelationalDatabaseEventsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseEventsResponserelationalDatabaseEventsTypeDef",
    {"resource": str, "createdAt": datetime, "message": str, "eventCategories": List[str]},
    total=False,
)


class ClientGetRelationalDatabaseEventsResponserelationalDatabaseEventsTypeDef(
    _ClientGetRelationalDatabaseEventsResponserelationalDatabaseEventsTypeDef
):
    """
    - *(dict) --*

      Describes an event for a database.
      - **resource** *(string) --*

        The database that the database event relates to.
    """


_ClientGetRelationalDatabaseEventsResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseEventsResponseTypeDef",
    {
        "relationalDatabaseEvents": List[
            ClientGetRelationalDatabaseEventsResponserelationalDatabaseEventsTypeDef
        ],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseEventsResponseTypeDef(
    _ClientGetRelationalDatabaseEventsResponseTypeDef
):
    """
    - *(dict) --*

      - **relationalDatabaseEvents** *(list) --*

        An object describing the result of your get relational database events request.
        - *(dict) --*

          Describes an event for a database.
          - **resource** *(string) --*

            The database that the database event relates to.
    """


_ClientGetRelationalDatabaseLogEventsResponseresourceLogEventsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseLogEventsResponseresourceLogEventsTypeDef",
    {"createdAt": datetime, "message": str},
    total=False,
)


class ClientGetRelationalDatabaseLogEventsResponseresourceLogEventsTypeDef(
    _ClientGetRelationalDatabaseLogEventsResponseresourceLogEventsTypeDef
):
    """
    - *(dict) --*

      Describes a database log event.
      - **createdAt** *(datetime) --*

        The timestamp when the database log event was created.
    """


_ClientGetRelationalDatabaseLogEventsResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseLogEventsResponseTypeDef",
    {
        "resourceLogEvents": List[
            ClientGetRelationalDatabaseLogEventsResponseresourceLogEventsTypeDef
        ],
        "nextBackwardToken": str,
        "nextForwardToken": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseLogEventsResponseTypeDef(
    _ClientGetRelationalDatabaseLogEventsResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceLogEvents** *(list) --*

        An object describing the result of your get relational database log events request.
        - *(dict) --*

          Describes a database log event.
          - **createdAt** *(datetime) --*

            The timestamp when the database log event was created.
    """


_ClientGetRelationalDatabaseLogStreamsResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseLogStreamsResponseTypeDef", {"logStreams": List[str]}, total=False
)


class ClientGetRelationalDatabaseLogStreamsResponseTypeDef(
    _ClientGetRelationalDatabaseLogStreamsResponseTypeDef
):
    """
    - *(dict) --*

      - **logStreams** *(list) --*

        An object describing the result of your get relational database log streams request.
        - *(string) --*
    """


_ClientGetRelationalDatabaseMasterUserPasswordResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseMasterUserPasswordResponseTypeDef",
    {"masterUserPassword": str, "createdAt": datetime},
    total=False,
)


class ClientGetRelationalDatabaseMasterUserPasswordResponseTypeDef(
    _ClientGetRelationalDatabaseMasterUserPasswordResponseTypeDef
):
    """
    - *(dict) --*

      - **masterUserPassword** *(string) --*

        The master user password for the ``password version`` specified.
    """


_ClientGetRelationalDatabaseMetricDataResponsemetricDataTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseMetricDataResponsemetricDataTypeDef",
    {
        "average": float,
        "maximum": float,
        "minimum": float,
        "sampleCount": float,
        "sum": float,
        "timestamp": datetime,
        "unit": Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
    },
    total=False,
)


class ClientGetRelationalDatabaseMetricDataResponsemetricDataTypeDef(
    _ClientGetRelationalDatabaseMetricDataResponsemetricDataTypeDef
):
    pass


_ClientGetRelationalDatabaseMetricDataResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseMetricDataResponseTypeDef",
    {
        "metricName": Literal[
            "CPUUtilization",
            "DatabaseConnections",
            "DiskQueueDepth",
            "FreeStorageSpace",
            "NetworkReceiveThroughput",
            "NetworkTransmitThroughput",
        ],
        "metricData": List[ClientGetRelationalDatabaseMetricDataResponsemetricDataTypeDef],
    },
    total=False,
)


class ClientGetRelationalDatabaseMetricDataResponseTypeDef(
    _ClientGetRelationalDatabaseMetricDataResponseTypeDef
):
    """
    - *(dict) --*

      - **metricName** *(string) --*

        The name of the metric.
    """


_ClientGetRelationalDatabaseParametersResponseparametersTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseParametersResponseparametersTypeDef",
    {
        "allowedValues": str,
        "applyMethod": str,
        "applyType": str,
        "dataType": str,
        "description": str,
        "isModifiable": bool,
        "parameterName": str,
        "parameterValue": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseParametersResponseparametersTypeDef(
    _ClientGetRelationalDatabaseParametersResponseparametersTypeDef
):
    """
    - *(dict) --*

      Describes the parameters of a database.
      - **allowedValues** *(string) --*

        Specifies the valid range of values for the parameter.
    """


_ClientGetRelationalDatabaseParametersResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseParametersResponseTypeDef",
    {
        "parameters": List[ClientGetRelationalDatabaseParametersResponseparametersTypeDef],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseParametersResponseTypeDef(
    _ClientGetRelationalDatabaseParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **parameters** *(list) --*

        An object describing the result of your get relational database parameters request.
        - *(dict) --*

          Describes the parameters of a database.
          - **allowedValues** *(string) --*

            Specifies the valid range of values for the parameter.
    """


_ClientGetRelationalDatabaseResponserelationalDatabasehardwareTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponserelationalDatabasehardwareTypeDef",
    {"cpuCount": int, "diskSizeInGb": int, "ramSizeInGb": Any},
    total=False,
)


class ClientGetRelationalDatabaseResponserelationalDatabasehardwareTypeDef(
    _ClientGetRelationalDatabaseResponserelationalDatabasehardwareTypeDef
):
    pass


_ClientGetRelationalDatabaseResponserelationalDatabaselocationTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponserelationalDatabaselocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetRelationalDatabaseResponserelationalDatabaselocationTypeDef(
    _ClientGetRelationalDatabaseResponserelationalDatabaselocationTypeDef
):
    pass


_ClientGetRelationalDatabaseResponserelationalDatabasemasterEndpointTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponserelationalDatabasemasterEndpointTypeDef",
    {"port": int, "address": str},
    total=False,
)


class ClientGetRelationalDatabaseResponserelationalDatabasemasterEndpointTypeDef(
    _ClientGetRelationalDatabaseResponserelationalDatabasemasterEndpointTypeDef
):
    pass


_ClientGetRelationalDatabaseResponserelationalDatabasependingMaintenanceActionsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponserelationalDatabasependingMaintenanceActionsTypeDef",
    {"action": str, "description": str, "currentApplyDate": datetime},
    total=False,
)


class ClientGetRelationalDatabaseResponserelationalDatabasependingMaintenanceActionsTypeDef(
    _ClientGetRelationalDatabaseResponserelationalDatabasependingMaintenanceActionsTypeDef
):
    pass


_ClientGetRelationalDatabaseResponserelationalDatabasependingModifiedValuesTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponserelationalDatabasependingModifiedValuesTypeDef",
    {"masterUserPassword": str, "engineVersion": str, "backupRetentionEnabled": bool},
    total=False,
)


class ClientGetRelationalDatabaseResponserelationalDatabasependingModifiedValuesTypeDef(
    _ClientGetRelationalDatabaseResponserelationalDatabasependingModifiedValuesTypeDef
):
    pass


_ClientGetRelationalDatabaseResponserelationalDatabasetagsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponserelationalDatabasetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetRelationalDatabaseResponserelationalDatabasetagsTypeDef(
    _ClientGetRelationalDatabaseResponserelationalDatabasetagsTypeDef
):
    pass


_ClientGetRelationalDatabaseResponserelationalDatabaseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponserelationalDatabaseTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetRelationalDatabaseResponserelationalDatabaselocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetRelationalDatabaseResponserelationalDatabasetagsTypeDef],
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "hardware": ClientGetRelationalDatabaseResponserelationalDatabasehardwareTypeDef,
        "state": str,
        "secondaryAvailabilityZone": str,
        "backupRetentionEnabled": bool,
        "pendingModifiedValues": ClientGetRelationalDatabaseResponserelationalDatabasependingModifiedValuesTypeDef,
        "engine": str,
        "engineVersion": str,
        "latestRestorableTime": datetime,
        "masterUsername": str,
        "parameterApplyStatus": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "masterEndpoint": ClientGetRelationalDatabaseResponserelationalDatabasemasterEndpointTypeDef,
        "pendingMaintenanceActions": List[
            ClientGetRelationalDatabaseResponserelationalDatabasependingMaintenanceActionsTypeDef
        ],
    },
    total=False,
)


class ClientGetRelationalDatabaseResponserelationalDatabaseTypeDef(
    _ClientGetRelationalDatabaseResponserelationalDatabaseTypeDef
):
    """
    - **relationalDatabase** *(dict) --*

      An object describing the specified database.
      - **name** *(string) --*

        The unique name of the database resource in Lightsail.
    """


_ClientGetRelationalDatabaseResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseResponseTypeDef",
    {"relationalDatabase": ClientGetRelationalDatabaseResponserelationalDatabaseTypeDef},
    total=False,
)


class ClientGetRelationalDatabaseResponseTypeDef(_ClientGetRelationalDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **relationalDatabase** *(dict) --*

        An object describing the specified database.
        - **name** *(string) --*

          The unique name of the database resource in Lightsail.
    """


_ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotlocationTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotlocationTypeDef(
    _ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotlocationTypeDef
):
    pass


_ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshottagsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshottagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshottagsTypeDef(
    _ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshottagsTypeDef
):
    pass


_ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotlocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[
            ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshottagsTypeDef
        ],
        "engine": str,
        "engineVersion": str,
        "sizeInGb": int,
        "state": str,
        "fromRelationalDatabaseName": str,
        "fromRelationalDatabaseArn": str,
        "fromRelationalDatabaseBundleId": str,
        "fromRelationalDatabaseBlueprintId": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotTypeDef(
    _ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotTypeDef
):
    """
    - **relationalDatabaseSnapshot** *(dict) --*

      An object describing the specified database snapshot.
      - **name** *(string) --*

        The name of the database snapshot.
    """


_ClientGetRelationalDatabaseSnapshotResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotResponseTypeDef",
    {
        "relationalDatabaseSnapshot": ClientGetRelationalDatabaseSnapshotResponserelationalDatabaseSnapshotTypeDef
    },
    total=False,
)


class ClientGetRelationalDatabaseSnapshotResponseTypeDef(
    _ClientGetRelationalDatabaseSnapshotResponseTypeDef
):
    """
    - *(dict) --*

      - **relationalDatabaseSnapshot** *(dict) --*

        An object describing the specified database snapshot.
        - **name** *(string) --*

          The name of the database snapshot.
    """


_ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotslocationTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotslocationTypeDef(
    _ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotslocationTypeDef
):
    pass


_ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotstagsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotstagsTypeDef(
    _ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotstagsTypeDef
):
    pass


_ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotsTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[
            ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotstagsTypeDef
        ],
        "engine": str,
        "engineVersion": str,
        "sizeInGb": int,
        "state": str,
        "fromRelationalDatabaseName": str,
        "fromRelationalDatabaseArn": str,
        "fromRelationalDatabaseBundleId": str,
        "fromRelationalDatabaseBlueprintId": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotsTypeDef(
    _ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a database snapshot.
      - **name** *(string) --*

        The name of the database snapshot.
    """


_ClientGetRelationalDatabaseSnapshotsResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabaseSnapshotsResponseTypeDef",
    {
        "relationalDatabaseSnapshots": List[
            ClientGetRelationalDatabaseSnapshotsResponserelationalDatabaseSnapshotsTypeDef
        ],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetRelationalDatabaseSnapshotsResponseTypeDef(
    _ClientGetRelationalDatabaseSnapshotsResponseTypeDef
):
    """
    - *(dict) --*

      - **relationalDatabaseSnapshots** *(list) --*

        An object describing the result of your get relational database snapshots request.
        - *(dict) --*

          Describes a database snapshot.
          - **name** *(string) --*

            The name of the database snapshot.
    """


_ClientGetRelationalDatabasesResponserelationalDatabaseshardwareTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponserelationalDatabaseshardwareTypeDef",
    {"cpuCount": int, "diskSizeInGb": int, "ramSizeInGb": Any},
    total=False,
)


class ClientGetRelationalDatabasesResponserelationalDatabaseshardwareTypeDef(
    _ClientGetRelationalDatabasesResponserelationalDatabaseshardwareTypeDef
):
    pass


_ClientGetRelationalDatabasesResponserelationalDatabaseslocationTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponserelationalDatabaseslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetRelationalDatabasesResponserelationalDatabaseslocationTypeDef(
    _ClientGetRelationalDatabasesResponserelationalDatabaseslocationTypeDef
):
    pass


_ClientGetRelationalDatabasesResponserelationalDatabasesmasterEndpointTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponserelationalDatabasesmasterEndpointTypeDef",
    {"port": int, "address": str},
    total=False,
)


class ClientGetRelationalDatabasesResponserelationalDatabasesmasterEndpointTypeDef(
    _ClientGetRelationalDatabasesResponserelationalDatabasesmasterEndpointTypeDef
):
    pass


_ClientGetRelationalDatabasesResponserelationalDatabasespendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponserelationalDatabasespendingMaintenanceActionsTypeDef",
    {"action": str, "description": str, "currentApplyDate": datetime},
    total=False,
)


class ClientGetRelationalDatabasesResponserelationalDatabasespendingMaintenanceActionsTypeDef(
    _ClientGetRelationalDatabasesResponserelationalDatabasespendingMaintenanceActionsTypeDef
):
    pass


_ClientGetRelationalDatabasesResponserelationalDatabasespendingModifiedValuesTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponserelationalDatabasespendingModifiedValuesTypeDef",
    {"masterUserPassword": str, "engineVersion": str, "backupRetentionEnabled": bool},
    total=False,
)


class ClientGetRelationalDatabasesResponserelationalDatabasespendingModifiedValuesTypeDef(
    _ClientGetRelationalDatabasesResponserelationalDatabasespendingModifiedValuesTypeDef
):
    pass


_ClientGetRelationalDatabasesResponserelationalDatabasestagsTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponserelationalDatabasestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetRelationalDatabasesResponserelationalDatabasestagsTypeDef(
    _ClientGetRelationalDatabasesResponserelationalDatabasestagsTypeDef
):
    pass


_ClientGetRelationalDatabasesResponserelationalDatabasesTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponserelationalDatabasesTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetRelationalDatabasesResponserelationalDatabaseslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[ClientGetRelationalDatabasesResponserelationalDatabasestagsTypeDef],
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "hardware": ClientGetRelationalDatabasesResponserelationalDatabaseshardwareTypeDef,
        "state": str,
        "secondaryAvailabilityZone": str,
        "backupRetentionEnabled": bool,
        "pendingModifiedValues": ClientGetRelationalDatabasesResponserelationalDatabasespendingModifiedValuesTypeDef,
        "engine": str,
        "engineVersion": str,
        "latestRestorableTime": datetime,
        "masterUsername": str,
        "parameterApplyStatus": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "masterEndpoint": ClientGetRelationalDatabasesResponserelationalDatabasesmasterEndpointTypeDef,
        "pendingMaintenanceActions": List[
            ClientGetRelationalDatabasesResponserelationalDatabasespendingMaintenanceActionsTypeDef
        ],
    },
    total=False,
)


class ClientGetRelationalDatabasesResponserelationalDatabasesTypeDef(
    _ClientGetRelationalDatabasesResponserelationalDatabasesTypeDef
):
    """
    - *(dict) --*

      Describes a database.
      - **name** *(string) --*

        The unique name of the database resource in Lightsail.
    """


_ClientGetRelationalDatabasesResponseTypeDef = TypedDict(
    "_ClientGetRelationalDatabasesResponseTypeDef",
    {
        "relationalDatabases": List[ClientGetRelationalDatabasesResponserelationalDatabasesTypeDef],
        "nextPageToken": str,
    },
    total=False,
)


class ClientGetRelationalDatabasesResponseTypeDef(_ClientGetRelationalDatabasesResponseTypeDef):
    """
    - *(dict) --*

      - **relationalDatabases** *(list) --*

        An object describing the result of your get relational databases request.
        - *(dict) --*

          Describes a database.
          - **name** *(string) --*

            The unique name of the database resource in Lightsail.
    """


_ClientGetStaticIpResponsestaticIplocationTypeDef = TypedDict(
    "_ClientGetStaticIpResponsestaticIplocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetStaticIpResponsestaticIplocationTypeDef(
    _ClientGetStaticIpResponsestaticIplocationTypeDef
):
    pass


_ClientGetStaticIpResponsestaticIpTypeDef = TypedDict(
    "_ClientGetStaticIpResponsestaticIpTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetStaticIpResponsestaticIplocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "ipAddress": str,
        "attachedTo": str,
        "isAttached": bool,
    },
    total=False,
)


class ClientGetStaticIpResponsestaticIpTypeDef(_ClientGetStaticIpResponsestaticIpTypeDef):
    """
    - **staticIp** *(dict) --*

      An array of key-value pairs containing information about the requested static IP.
      - **name** *(string) --*

        The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
    """


_ClientGetStaticIpResponseTypeDef = TypedDict(
    "_ClientGetStaticIpResponseTypeDef",
    {"staticIp": ClientGetStaticIpResponsestaticIpTypeDef},
    total=False,
)


class ClientGetStaticIpResponseTypeDef(_ClientGetStaticIpResponseTypeDef):
    """
    - *(dict) --*

      - **staticIp** *(dict) --*

        An array of key-value pairs containing information about the requested static IP.
        - **name** *(string) --*

          The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
    """


_ClientGetStaticIpsResponsestaticIpslocationTypeDef = TypedDict(
    "_ClientGetStaticIpsResponsestaticIpslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientGetStaticIpsResponsestaticIpslocationTypeDef(
    _ClientGetStaticIpsResponsestaticIpslocationTypeDef
):
    pass


_ClientGetStaticIpsResponsestaticIpsTypeDef = TypedDict(
    "_ClientGetStaticIpsResponsestaticIpsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": ClientGetStaticIpsResponsestaticIpslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "ipAddress": str,
        "attachedTo": str,
        "isAttached": bool,
    },
    total=False,
)


class ClientGetStaticIpsResponsestaticIpsTypeDef(_ClientGetStaticIpsResponsestaticIpsTypeDef):
    """
    - *(dict) --*

      Describes the static IP.
      - **name** *(string) --*

        The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
    """


_ClientGetStaticIpsResponseTypeDef = TypedDict(
    "_ClientGetStaticIpsResponseTypeDef",
    {"staticIps": List[ClientGetStaticIpsResponsestaticIpsTypeDef], "nextPageToken": str},
    total=False,
)


class ClientGetStaticIpsResponseTypeDef(_ClientGetStaticIpsResponseTypeDef):
    """
    - *(dict) --*

      - **staticIps** *(list) --*

        An array of key-value pairs containing information about your get static IPs request.
        - *(dict) --*

          Describes the static IP.
          - **name** *(string) --*

            The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
    """


_ClientImportKeyPairResponseoperationlocationTypeDef = TypedDict(
    "_ClientImportKeyPairResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientImportKeyPairResponseoperationlocationTypeDef(
    _ClientImportKeyPairResponseoperationlocationTypeDef
):
    pass


_ClientImportKeyPairResponseoperationTypeDef = TypedDict(
    "_ClientImportKeyPairResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientImportKeyPairResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientImportKeyPairResponseoperationTypeDef(_ClientImportKeyPairResponseoperationTypeDef):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the request operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientImportKeyPairResponseTypeDef = TypedDict(
    "_ClientImportKeyPairResponseTypeDef",
    {"operation": ClientImportKeyPairResponseoperationTypeDef},
    total=False,
)


class ClientImportKeyPairResponseTypeDef(_ClientImportKeyPairResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the request operation.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientIsVpcPeeredResponseTypeDef = TypedDict(
    "_ClientIsVpcPeeredResponseTypeDef", {"isPeered": bool}, total=False
)


class ClientIsVpcPeeredResponseTypeDef(_ClientIsVpcPeeredResponseTypeDef):
    """
    - *(dict) --*

      - **isPeered** *(boolean) --*

        Returns ``true`` if the Lightsail VPC is peered; otherwise, ``false`` .
    """


_ClientOpenInstancePublicPortsPortInfoTypeDef = TypedDict(
    "_ClientOpenInstancePublicPortsPortInfoTypeDef",
    {"fromPort": int, "toPort": int, "protocol": Literal["tcp", "all", "udp"]},
    total=False,
)


class ClientOpenInstancePublicPortsPortInfoTypeDef(_ClientOpenInstancePublicPortsPortInfoTypeDef):
    """
    An array of key-value pairs containing information about the port mappings.
    - **fromPort** *(integer) --*

      The first port in the range.
    """


_ClientOpenInstancePublicPortsResponseoperationlocationTypeDef = TypedDict(
    "_ClientOpenInstancePublicPortsResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientOpenInstancePublicPortsResponseoperationlocationTypeDef(
    _ClientOpenInstancePublicPortsResponseoperationlocationTypeDef
):
    pass


_ClientOpenInstancePublicPortsResponseoperationTypeDef = TypedDict(
    "_ClientOpenInstancePublicPortsResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientOpenInstancePublicPortsResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientOpenInstancePublicPortsResponseoperationTypeDef(
    _ClientOpenInstancePublicPortsResponseoperationTypeDef
):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the request operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientOpenInstancePublicPortsResponseTypeDef = TypedDict(
    "_ClientOpenInstancePublicPortsResponseTypeDef",
    {"operation": ClientOpenInstancePublicPortsResponseoperationTypeDef},
    total=False,
)


class ClientOpenInstancePublicPortsResponseTypeDef(_ClientOpenInstancePublicPortsResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the request operation.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientPeerVpcResponseoperationlocationTypeDef = TypedDict(
    "_ClientPeerVpcResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientPeerVpcResponseoperationlocationTypeDef(_ClientPeerVpcResponseoperationlocationTypeDef):
    pass


_ClientPeerVpcResponseoperationTypeDef = TypedDict(
    "_ClientPeerVpcResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientPeerVpcResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientPeerVpcResponseoperationTypeDef(_ClientPeerVpcResponseoperationTypeDef):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the request operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientPeerVpcResponseTypeDef = TypedDict(
    "_ClientPeerVpcResponseTypeDef",
    {"operation": ClientPeerVpcResponseoperationTypeDef},
    total=False,
)


class ClientPeerVpcResponseTypeDef(_ClientPeerVpcResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the request operation.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientPutInstancePublicPortsPortInfosTypeDef = TypedDict(
    "_ClientPutInstancePublicPortsPortInfosTypeDef",
    {"fromPort": int, "toPort": int, "protocol": Literal["tcp", "all", "udp"]},
    total=False,
)


class ClientPutInstancePublicPortsPortInfosTypeDef(_ClientPutInstancePublicPortsPortInfosTypeDef):
    """
    - *(dict) --*

      Describes information about the ports on your virtual private server (or *instance* ).
      - **fromPort** *(integer) --*

        The first port in the range.
    """


_ClientPutInstancePublicPortsResponseoperationlocationTypeDef = TypedDict(
    "_ClientPutInstancePublicPortsResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientPutInstancePublicPortsResponseoperationlocationTypeDef(
    _ClientPutInstancePublicPortsResponseoperationlocationTypeDef
):
    pass


_ClientPutInstancePublicPortsResponseoperationTypeDef = TypedDict(
    "_ClientPutInstancePublicPortsResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientPutInstancePublicPortsResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientPutInstancePublicPortsResponseoperationTypeDef(
    _ClientPutInstancePublicPortsResponseoperationTypeDef
):
    """
    - **operation** *(dict) --*

      Describes metadata about the operation you just executed.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientPutInstancePublicPortsResponseTypeDef = TypedDict(
    "_ClientPutInstancePublicPortsResponseTypeDef",
    {"operation": ClientPutInstancePublicPortsResponseoperationTypeDef},
    total=False,
)


class ClientPutInstancePublicPortsResponseTypeDef(_ClientPutInstancePublicPortsResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        Describes metadata about the operation you just executed.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientRebootInstanceResponseoperationslocationTypeDef = TypedDict(
    "_ClientRebootInstanceResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientRebootInstanceResponseoperationslocationTypeDef(
    _ClientRebootInstanceResponseoperationslocationTypeDef
):
    pass


_ClientRebootInstanceResponseoperationsTypeDef = TypedDict(
    "_ClientRebootInstanceResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientRebootInstanceResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientRebootInstanceResponseoperationsTypeDef(_ClientRebootInstanceResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientRebootInstanceResponseTypeDef = TypedDict(
    "_ClientRebootInstanceResponseTypeDef",
    {"operations": List[ClientRebootInstanceResponseoperationsTypeDef]},
    total=False,
)


class ClientRebootInstanceResponseTypeDef(_ClientRebootInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the request operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientRebootRelationalDatabaseResponseoperationslocationTypeDef = TypedDict(
    "_ClientRebootRelationalDatabaseResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientRebootRelationalDatabaseResponseoperationslocationTypeDef(
    _ClientRebootRelationalDatabaseResponseoperationslocationTypeDef
):
    pass


_ClientRebootRelationalDatabaseResponseoperationsTypeDef = TypedDict(
    "_ClientRebootRelationalDatabaseResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientRebootRelationalDatabaseResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientRebootRelationalDatabaseResponseoperationsTypeDef(
    _ClientRebootRelationalDatabaseResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientRebootRelationalDatabaseResponseTypeDef = TypedDict(
    "_ClientRebootRelationalDatabaseResponseTypeDef",
    {"operations": List[ClientRebootRelationalDatabaseResponseoperationsTypeDef]},
    total=False,
)


class ClientRebootRelationalDatabaseResponseTypeDef(_ClientRebootRelationalDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your reboot relational database request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientReleaseStaticIpResponseoperationslocationTypeDef = TypedDict(
    "_ClientReleaseStaticIpResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientReleaseStaticIpResponseoperationslocationTypeDef(
    _ClientReleaseStaticIpResponseoperationslocationTypeDef
):
    pass


_ClientReleaseStaticIpResponseoperationsTypeDef = TypedDict(
    "_ClientReleaseStaticIpResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientReleaseStaticIpResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientReleaseStaticIpResponseoperationsTypeDef(
    _ClientReleaseStaticIpResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientReleaseStaticIpResponseTypeDef = TypedDict(
    "_ClientReleaseStaticIpResponseTypeDef",
    {"operations": List[ClientReleaseStaticIpResponseoperationsTypeDef]},
    total=False,
)


class ClientReleaseStaticIpResponseTypeDef(_ClientReleaseStaticIpResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the request operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientStartInstanceResponseoperationslocationTypeDef = TypedDict(
    "_ClientStartInstanceResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientStartInstanceResponseoperationslocationTypeDef(
    _ClientStartInstanceResponseoperationslocationTypeDef
):
    pass


_ClientStartInstanceResponseoperationsTypeDef = TypedDict(
    "_ClientStartInstanceResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientStartInstanceResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientStartInstanceResponseoperationsTypeDef(_ClientStartInstanceResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientStartInstanceResponseTypeDef = TypedDict(
    "_ClientStartInstanceResponseTypeDef",
    {"operations": List[ClientStartInstanceResponseoperationsTypeDef]},
    total=False,
)


class ClientStartInstanceResponseTypeDef(_ClientStartInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the request operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientStartRelationalDatabaseResponseoperationslocationTypeDef = TypedDict(
    "_ClientStartRelationalDatabaseResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientStartRelationalDatabaseResponseoperationslocationTypeDef(
    _ClientStartRelationalDatabaseResponseoperationslocationTypeDef
):
    pass


_ClientStartRelationalDatabaseResponseoperationsTypeDef = TypedDict(
    "_ClientStartRelationalDatabaseResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientStartRelationalDatabaseResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientStartRelationalDatabaseResponseoperationsTypeDef(
    _ClientStartRelationalDatabaseResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientStartRelationalDatabaseResponseTypeDef = TypedDict(
    "_ClientStartRelationalDatabaseResponseTypeDef",
    {"operations": List[ClientStartRelationalDatabaseResponseoperationsTypeDef]},
    total=False,
)


class ClientStartRelationalDatabaseResponseTypeDef(_ClientStartRelationalDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your start relational database request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientStopInstanceResponseoperationslocationTypeDef = TypedDict(
    "_ClientStopInstanceResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientStopInstanceResponseoperationslocationTypeDef(
    _ClientStopInstanceResponseoperationslocationTypeDef
):
    pass


_ClientStopInstanceResponseoperationsTypeDef = TypedDict(
    "_ClientStopInstanceResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientStopInstanceResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientStopInstanceResponseoperationsTypeDef(_ClientStopInstanceResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientStopInstanceResponseTypeDef = TypedDict(
    "_ClientStopInstanceResponseTypeDef",
    {"operations": List[ClientStopInstanceResponseoperationsTypeDef]},
    total=False,
)


class ClientStopInstanceResponseTypeDef(_ClientStopInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the request operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientStopRelationalDatabaseResponseoperationslocationTypeDef = TypedDict(
    "_ClientStopRelationalDatabaseResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientStopRelationalDatabaseResponseoperationslocationTypeDef(
    _ClientStopRelationalDatabaseResponseoperationslocationTypeDef
):
    pass


_ClientStopRelationalDatabaseResponseoperationsTypeDef = TypedDict(
    "_ClientStopRelationalDatabaseResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientStopRelationalDatabaseResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientStopRelationalDatabaseResponseoperationsTypeDef(
    _ClientStopRelationalDatabaseResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientStopRelationalDatabaseResponseTypeDef = TypedDict(
    "_ClientStopRelationalDatabaseResponseTypeDef",
    {"operations": List[ClientStopRelationalDatabaseResponseoperationsTypeDef]},
    total=False,
)


class ClientStopRelationalDatabaseResponseTypeDef(_ClientStopRelationalDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your stop relational database request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientTagResourceResponseoperationslocationTypeDef = TypedDict(
    "_ClientTagResourceResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientTagResourceResponseoperationslocationTypeDef(
    _ClientTagResourceResponseoperationslocationTypeDef
):
    pass


_ClientTagResourceResponseoperationsTypeDef = TypedDict(
    "_ClientTagResourceResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientTagResourceResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientTagResourceResponseoperationsTypeDef(_ClientTagResourceResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientTagResourceResponseTypeDef = TypedDict(
    "_ClientTagResourceResponseTypeDef",
    {"operations": List[ClientTagResourceResponseoperationsTypeDef]},
    total=False,
)


class ClientTagResourceResponseTypeDef(_ClientTagResourceResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        A list of objects describing the API operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag key and optional value assigned to an Amazon Lightsail resource.
      For more information about tags in Lightsail, see the `Lightsail Dev Guide
      <https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags>`__ .
      - **key** *(string) --*

        The key of the tag.
        Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the
        following characters: + - = . _ : / @
    """


_ClientUnpeerVpcResponseoperationlocationTypeDef = TypedDict(
    "_ClientUnpeerVpcResponseoperationlocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientUnpeerVpcResponseoperationlocationTypeDef(
    _ClientUnpeerVpcResponseoperationlocationTypeDef
):
    pass


_ClientUnpeerVpcResponseoperationTypeDef = TypedDict(
    "_ClientUnpeerVpcResponseoperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientUnpeerVpcResponseoperationlocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientUnpeerVpcResponseoperationTypeDef(_ClientUnpeerVpcResponseoperationTypeDef):
    """
    - **operation** *(dict) --*

      An array of key-value pairs containing information about the request operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientUnpeerVpcResponseTypeDef = TypedDict(
    "_ClientUnpeerVpcResponseTypeDef",
    {"operation": ClientUnpeerVpcResponseoperationTypeDef},
    total=False,
)


class ClientUnpeerVpcResponseTypeDef(_ClientUnpeerVpcResponseTypeDef):
    """
    - *(dict) --*

      - **operation** *(dict) --*

        An array of key-value pairs containing information about the request operation.
        - **id** *(string) --*

          The ID of the operation.
    """


_ClientUntagResourceResponseoperationslocationTypeDef = TypedDict(
    "_ClientUntagResourceResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientUntagResourceResponseoperationslocationTypeDef(
    _ClientUntagResourceResponseoperationslocationTypeDef
):
    pass


_ClientUntagResourceResponseoperationsTypeDef = TypedDict(
    "_ClientUntagResourceResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientUntagResourceResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientUntagResourceResponseoperationsTypeDef(_ClientUntagResourceResponseoperationsTypeDef):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientUntagResourceResponseTypeDef = TypedDict(
    "_ClientUntagResourceResponseTypeDef",
    {"operations": List[ClientUntagResourceResponseoperationsTypeDef]},
    total=False,
)


class ClientUntagResourceResponseTypeDef(_ClientUntagResourceResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        A list of objects describing the API operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientUpdateDomainEntryDomainEntryTypeDef = TypedDict(
    "_ClientUpdateDomainEntryDomainEntryTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)


class ClientUpdateDomainEntryDomainEntryTypeDef(_ClientUpdateDomainEntryDomainEntryTypeDef):
    """
    An array of key-value pairs containing information about the domain entry.
    - **id** *(string) --*

      The ID of the domain recordset entry.
    """


_ClientUpdateDomainEntryResponseoperationslocationTypeDef = TypedDict(
    "_ClientUpdateDomainEntryResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientUpdateDomainEntryResponseoperationslocationTypeDef(
    _ClientUpdateDomainEntryResponseoperationslocationTypeDef
):
    pass


_ClientUpdateDomainEntryResponseoperationsTypeDef = TypedDict(
    "_ClientUpdateDomainEntryResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientUpdateDomainEntryResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientUpdateDomainEntryResponseoperationsTypeDef(
    _ClientUpdateDomainEntryResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientUpdateDomainEntryResponseTypeDef = TypedDict(
    "_ClientUpdateDomainEntryResponseTypeDef",
    {"operations": List[ClientUpdateDomainEntryResponseoperationsTypeDef]},
    total=False,
)


class ClientUpdateDomainEntryResponseTypeDef(_ClientUpdateDomainEntryResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the request operation.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientUpdateLoadBalancerAttributeResponseoperationslocationTypeDef = TypedDict(
    "_ClientUpdateLoadBalancerAttributeResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientUpdateLoadBalancerAttributeResponseoperationslocationTypeDef(
    _ClientUpdateLoadBalancerAttributeResponseoperationslocationTypeDef
):
    pass


_ClientUpdateLoadBalancerAttributeResponseoperationsTypeDef = TypedDict(
    "_ClientUpdateLoadBalancerAttributeResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientUpdateLoadBalancerAttributeResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientUpdateLoadBalancerAttributeResponseoperationsTypeDef(
    _ClientUpdateLoadBalancerAttributeResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientUpdateLoadBalancerAttributeResponseTypeDef = TypedDict(
    "_ClientUpdateLoadBalancerAttributeResponseTypeDef",
    {"operations": List[ClientUpdateLoadBalancerAttributeResponseoperationsTypeDef]},
    total=False,
)


class ClientUpdateLoadBalancerAttributeResponseTypeDef(
    _ClientUpdateLoadBalancerAttributeResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the API operations.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientUpdateRelationalDatabaseParametersParametersTypeDef = TypedDict(
    "_ClientUpdateRelationalDatabaseParametersParametersTypeDef",
    {
        "allowedValues": str,
        "applyMethod": str,
        "applyType": str,
        "dataType": str,
        "description": str,
        "isModifiable": bool,
        "parameterName": str,
        "parameterValue": str,
    },
    total=False,
)


class ClientUpdateRelationalDatabaseParametersParametersTypeDef(
    _ClientUpdateRelationalDatabaseParametersParametersTypeDef
):
    """
    - *(dict) --*

      Describes the parameters of a database.
      - **allowedValues** *(string) --*

        Specifies the valid range of values for the parameter.
    """


_ClientUpdateRelationalDatabaseParametersResponseoperationslocationTypeDef = TypedDict(
    "_ClientUpdateRelationalDatabaseParametersResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientUpdateRelationalDatabaseParametersResponseoperationslocationTypeDef(
    _ClientUpdateRelationalDatabaseParametersResponseoperationslocationTypeDef
):
    pass


_ClientUpdateRelationalDatabaseParametersResponseoperationsTypeDef = TypedDict(
    "_ClientUpdateRelationalDatabaseParametersResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientUpdateRelationalDatabaseParametersResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientUpdateRelationalDatabaseParametersResponseoperationsTypeDef(
    _ClientUpdateRelationalDatabaseParametersResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientUpdateRelationalDatabaseParametersResponseTypeDef = TypedDict(
    "_ClientUpdateRelationalDatabaseParametersResponseTypeDef",
    {"operations": List[ClientUpdateRelationalDatabaseParametersResponseoperationsTypeDef]},
    total=False,
)


class ClientUpdateRelationalDatabaseParametersResponseTypeDef(
    _ClientUpdateRelationalDatabaseParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your update relational database parameters request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_ClientUpdateRelationalDatabaseResponseoperationslocationTypeDef = TypedDict(
    "_ClientUpdateRelationalDatabaseResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class ClientUpdateRelationalDatabaseResponseoperationslocationTypeDef(
    _ClientUpdateRelationalDatabaseResponseoperationslocationTypeDef
):
    pass


_ClientUpdateRelationalDatabaseResponseoperationsTypeDef = TypedDict(
    "_ClientUpdateRelationalDatabaseResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": ClientUpdateRelationalDatabaseResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class ClientUpdateRelationalDatabaseResponseoperationsTypeDef(
    _ClientUpdateRelationalDatabaseResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_ClientUpdateRelationalDatabaseResponseTypeDef = TypedDict(
    "_ClientUpdateRelationalDatabaseResponseTypeDef",
    {"operations": List[ClientUpdateRelationalDatabaseResponseoperationsTypeDef]},
    total=False,
)


class ClientUpdateRelationalDatabaseResponseTypeDef(_ClientUpdateRelationalDatabaseResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An object describing the result of your update relational database request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_GetActiveNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetActiveNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetActiveNamesPaginatePaginationConfigTypeDef(_GetActiveNamesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetActiveNamesPaginateResponseTypeDef = TypedDict(
    "_GetActiveNamesPaginateResponseTypeDef",
    {"activeNames": List[str], "NextToken": str},
    total=False,
)


class GetActiveNamesPaginateResponseTypeDef(_GetActiveNamesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **activeNames** *(list) --*

        The list of active names returned by the get active names request.
        - *(string) --*
    """


_GetBlueprintsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBlueprintsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetBlueprintsPaginatePaginationConfigTypeDef(_GetBlueprintsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBlueprintsPaginateResponseblueprintsTypeDef = TypedDict(
    "_GetBlueprintsPaginateResponseblueprintsTypeDef",
    {
        "blueprintId": str,
        "name": str,
        "group": str,
        "type": Literal["os", "app"],
        "description": str,
        "isActive": bool,
        "minPower": int,
        "version": str,
        "versionCode": str,
        "productUrl": str,
        "licenseUrl": str,
        "platform": Literal["LINUX_UNIX", "WINDOWS"],
    },
    total=False,
)


class GetBlueprintsPaginateResponseblueprintsTypeDef(
    _GetBlueprintsPaginateResponseblueprintsTypeDef
):
    """
    - *(dict) --*

      Describes a blueprint (a virtual private server image).
      - **blueprintId** *(string) --*

        The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0``
        ).
    """


_GetBlueprintsPaginateResponseTypeDef = TypedDict(
    "_GetBlueprintsPaginateResponseTypeDef",
    {"blueprints": List[GetBlueprintsPaginateResponseblueprintsTypeDef], "NextToken": str},
    total=False,
)


class GetBlueprintsPaginateResponseTypeDef(_GetBlueprintsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **blueprints** *(list) --*

        An array of key-value pairs that contains information about the available blueprints.
        - *(dict) --*

          Describes a blueprint (a virtual private server image).
          - **blueprintId** *(string) --*

            The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or
            ``app_lamp_7_0`` ).
    """


_GetBundlesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBundlesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetBundlesPaginatePaginationConfigTypeDef(_GetBundlesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBundlesPaginateResponsebundlesTypeDef = TypedDict(
    "_GetBundlesPaginateResponsebundlesTypeDef",
    {
        "price": float,
        "cpuCount": int,
        "diskSizeInGb": int,
        "bundleId": str,
        "instanceType": str,
        "isActive": bool,
        "name": str,
        "power": int,
        "ramSizeInGb": Any,
        "transferPerMonthInGb": int,
        "supportedPlatforms": List[Literal["LINUX_UNIX", "WINDOWS"]],
    },
    total=False,
)


class GetBundlesPaginateResponsebundlesTypeDef(_GetBundlesPaginateResponsebundlesTypeDef):
    """
    - *(dict) --*

      Describes a bundle, which is a set of specs describing your virtual private server (or
      *instance* ).
      - **price** *(float) --*

        The price in US dollars (e.g., ``5.0`` ).
    """


_GetBundlesPaginateResponseTypeDef = TypedDict(
    "_GetBundlesPaginateResponseTypeDef",
    {"bundles": List[GetBundlesPaginateResponsebundlesTypeDef], "NextToken": str},
    total=False,
)


class GetBundlesPaginateResponseTypeDef(_GetBundlesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **bundles** *(list) --*

        An array of key-value pairs that contains information about the available bundles.
        - *(dict) --*

          Describes a bundle, which is a set of specs describing your virtual private server (or
          *instance* ).
          - **price** *(float) --*

            The price in US dollars (e.g., ``5.0`` ).
    """


_GetCloudFormationStackRecordsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetCloudFormationStackRecordsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetCloudFormationStackRecordsPaginatePaginationConfigTypeDef(
    _GetCloudFormationStackRecordsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsdestinationInfoTypeDef = TypedDict(
    "_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsdestinationInfoTypeDef",
    {"id": str, "service": str},
    total=False,
)


class GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsdestinationInfoTypeDef(
    _GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsdestinationInfoTypeDef
):
    pass


_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordslocationTypeDef = TypedDict(
    "_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordslocationTypeDef(
    _GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordslocationTypeDef
):
    pass


_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordssourceInfoTypeDef = TypedDict(
    "_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordssourceInfoTypeDef",
    {"resourceType": str, "name": str, "arn": str},
    total=False,
)


class GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordssourceInfoTypeDef(
    _GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordssourceInfoTypeDef
):
    pass


_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsTypeDef = TypedDict(
    "_GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "state": Literal["Started", "Succeeded", "Failed"],
        "sourceInfo": List[
            GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordssourceInfoTypeDef
        ],
        "destinationInfo": GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsdestinationInfoTypeDef,
    },
    total=False,
)


class GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsTypeDef(
    _GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsTypeDef
):
    """
    - *(dict) --*

      Describes a CloudFormation stack record created as a result of the ``create cloud formation
      stack`` operation.
      A CloudFormation stack record provides information about the AWS CloudFormation stack used to
      create a new Amazon Elastic Compute Cloud instance from an exported Lightsail instance
      snapshot.
      - **name** *(string) --*

        The name of the CloudFormation stack record. It starts with ``CloudFormationStackRecord``
        followed by a GUID.
    """


_GetCloudFormationStackRecordsPaginateResponseTypeDef = TypedDict(
    "_GetCloudFormationStackRecordsPaginateResponseTypeDef",
    {
        "cloudFormationStackRecords": List[
            GetCloudFormationStackRecordsPaginateResponsecloudFormationStackRecordsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetCloudFormationStackRecordsPaginateResponseTypeDef(
    _GetCloudFormationStackRecordsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **cloudFormationStackRecords** *(list) --*

        A list of objects describing the CloudFormation stack records.
        - *(dict) --*

          Describes a CloudFormation stack record created as a result of the ``create cloud
          formation stack`` operation.
          A CloudFormation stack record provides information about the AWS CloudFormation stack used
          to create a new Amazon Elastic Compute Cloud instance from an exported Lightsail instance
          snapshot.
          - **name** *(string) --*

            The name of the CloudFormation stack record. It starts with
            ``CloudFormationStackRecord`` followed by a GUID.
    """


_GetDiskSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDiskSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetDiskSnapshotsPaginatePaginationConfigTypeDef(
    _GetDiskSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDiskSnapshotsPaginateResponsediskSnapshotslocationTypeDef = TypedDict(
    "_GetDiskSnapshotsPaginateResponsediskSnapshotslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetDiskSnapshotsPaginateResponsediskSnapshotslocationTypeDef(
    _GetDiskSnapshotsPaginateResponsediskSnapshotslocationTypeDef
):
    pass


_GetDiskSnapshotsPaginateResponsediskSnapshotstagsTypeDef = TypedDict(
    "_GetDiskSnapshotsPaginateResponsediskSnapshotstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetDiskSnapshotsPaginateResponsediskSnapshotstagsTypeDef(
    _GetDiskSnapshotsPaginateResponsediskSnapshotstagsTypeDef
):
    pass


_GetDiskSnapshotsPaginateResponsediskSnapshotsTypeDef = TypedDict(
    "_GetDiskSnapshotsPaginateResponsediskSnapshotsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetDiskSnapshotsPaginateResponsediskSnapshotslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetDiskSnapshotsPaginateResponsediskSnapshotstagsTypeDef],
        "sizeInGb": int,
        "state": Literal["pending", "completed", "error", "unknown"],
        "progress": str,
        "fromDiskName": str,
        "fromDiskArn": str,
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "isFromAutoSnapshot": bool,
    },
    total=False,
)


class GetDiskSnapshotsPaginateResponsediskSnapshotsTypeDef(
    _GetDiskSnapshotsPaginateResponsediskSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a block storage disk snapshot.
      - **name** *(string) --*

        The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
    """


_GetDiskSnapshotsPaginateResponseTypeDef = TypedDict(
    "_GetDiskSnapshotsPaginateResponseTypeDef",
    {"diskSnapshots": List[GetDiskSnapshotsPaginateResponsediskSnapshotsTypeDef], "NextToken": str},
    total=False,
)


class GetDiskSnapshotsPaginateResponseTypeDef(_GetDiskSnapshotsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **diskSnapshots** *(list) --*

        An array of objects containing information about all block storage disk snapshots.
        - *(dict) --*

          Describes a block storage disk snapshot.
          - **name** *(string) --*

            The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
    """


_GetDisksPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDisksPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)


class GetDisksPaginatePaginationConfigTypeDef(_GetDisksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDisksPaginateResponsedisksaddOnsTypeDef = TypedDict(
    "_GetDisksPaginateResponsedisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class GetDisksPaginateResponsedisksaddOnsTypeDef(_GetDisksPaginateResponsedisksaddOnsTypeDef):
    pass


_GetDisksPaginateResponsediskslocationTypeDef = TypedDict(
    "_GetDisksPaginateResponsediskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetDisksPaginateResponsediskslocationTypeDef(_GetDisksPaginateResponsediskslocationTypeDef):
    pass


_GetDisksPaginateResponsediskstagsTypeDef = TypedDict(
    "_GetDisksPaginateResponsediskstagsTypeDef", {"key": str, "value": str}, total=False
)


class GetDisksPaginateResponsediskstagsTypeDef(_GetDisksPaginateResponsediskstagsTypeDef):
    pass


_GetDisksPaginateResponsedisksTypeDef = TypedDict(
    "_GetDisksPaginateResponsedisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetDisksPaginateResponsediskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetDisksPaginateResponsediskstagsTypeDef],
        "addOns": List[GetDisksPaginateResponsedisksaddOnsTypeDef],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class GetDisksPaginateResponsedisksTypeDef(_GetDisksPaginateResponsedisksTypeDef):
    """
    - *(dict) --*

      Describes a system disk or a block storage disk.
      - **name** *(string) --*

        The unique name of the disk.
    """


_GetDisksPaginateResponseTypeDef = TypedDict(
    "_GetDisksPaginateResponseTypeDef",
    {"disks": List[GetDisksPaginateResponsedisksTypeDef], "NextToken": str},
    total=False,
)


class GetDisksPaginateResponseTypeDef(_GetDisksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **disks** *(list) --*

        An array of objects containing information about all block storage disks.
        - *(dict) --*

          Describes a system disk or a block storage disk.
          - **name** *(string) --*

            The unique name of the disk.
    """


_GetDomainsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDomainsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetDomainsPaginatePaginationConfigTypeDef(_GetDomainsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDomainsPaginateResponsedomainsdomainEntriesTypeDef = TypedDict(
    "_GetDomainsPaginateResponsedomainsdomainEntriesTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)


class GetDomainsPaginateResponsedomainsdomainEntriesTypeDef(
    _GetDomainsPaginateResponsedomainsdomainEntriesTypeDef
):
    pass


_GetDomainsPaginateResponsedomainslocationTypeDef = TypedDict(
    "_GetDomainsPaginateResponsedomainslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetDomainsPaginateResponsedomainslocationTypeDef(
    _GetDomainsPaginateResponsedomainslocationTypeDef
):
    pass


_GetDomainsPaginateResponsedomainstagsTypeDef = TypedDict(
    "_GetDomainsPaginateResponsedomainstagsTypeDef", {"key": str, "value": str}, total=False
)


class GetDomainsPaginateResponsedomainstagsTypeDef(_GetDomainsPaginateResponsedomainstagsTypeDef):
    pass


_GetDomainsPaginateResponsedomainsTypeDef = TypedDict(
    "_GetDomainsPaginateResponsedomainsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetDomainsPaginateResponsedomainslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetDomainsPaginateResponsedomainstagsTypeDef],
        "domainEntries": List[GetDomainsPaginateResponsedomainsdomainEntriesTypeDef],
    },
    total=False,
)


class GetDomainsPaginateResponsedomainsTypeDef(_GetDomainsPaginateResponsedomainsTypeDef):
    """
    - *(dict) --*

      Describes a domain where you are storing recordsets in Lightsail.
      - **name** *(string) --*

        The name of the domain.
    """


_GetDomainsPaginateResponseTypeDef = TypedDict(
    "_GetDomainsPaginateResponseTypeDef",
    {"domains": List[GetDomainsPaginateResponsedomainsTypeDef], "NextToken": str},
    total=False,
)


class GetDomainsPaginateResponseTypeDef(_GetDomainsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **domains** *(list) --*

        An array of key-value pairs containing information about each of the domain entries in the
        user's account.
        - *(dict) --*

          Describes a domain where you are storing recordsets in Lightsail.
          - **name** *(string) --*

            The name of the domain.
    """


_GetExportSnapshotRecordsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetExportSnapshotRecordsPaginatePaginationConfigTypeDef(
    _GetExportSnapshotRecordsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsdestinationInfoTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsdestinationInfoTypeDef",
    {"id": str, "service": str},
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsdestinationInfoTypeDef(
    _GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsdestinationInfoTypeDef
):
    pass


_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordslocationTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordslocationTypeDef(
    _GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordslocationTypeDef
):
    pass


_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef",
    {"sizeInGb": int},
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef(
    _GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef
):
    pass


_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef",
    {"name": str, "path": str, "sizeInGb": int, "isSystemDisk": bool},
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef(
    _GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef
):
    pass


_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef",
    {
        "fromBundleId": str,
        "fromBlueprintId": str,
        "fromDiskInfo": List[
            GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfofromDiskInfoTypeDef
        ],
    },
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef(
    _GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef
):
    pass


_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoTypeDef",
    {
        "resourceType": Literal["InstanceSnapshot", "DiskSnapshot"],
        "createdAt": datetime,
        "name": str,
        "arn": str,
        "fromResourceName": str,
        "fromResourceArn": str,
        "instanceSnapshotInfo": GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoinstanceSnapshotInfoTypeDef,
        "diskSnapshotInfo": GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfodiskSnapshotInfoTypeDef,
    },
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoTypeDef(
    _GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoTypeDef
):
    pass


_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "state": Literal["Started", "Succeeded", "Failed"],
        "sourceInfo": GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordssourceInfoTypeDef,
        "destinationInfo": GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsdestinationInfoTypeDef,
    },
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsTypeDef(
    _GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsTypeDef
):
    """
    - *(dict) --*

      Describes an export snapshot record.
      - **name** *(string) --*

        The export snapshot record name.
    """


_GetExportSnapshotRecordsPaginateResponseTypeDef = TypedDict(
    "_GetExportSnapshotRecordsPaginateResponseTypeDef",
    {
        "exportSnapshotRecords": List[
            GetExportSnapshotRecordsPaginateResponseexportSnapshotRecordsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetExportSnapshotRecordsPaginateResponseTypeDef(
    _GetExportSnapshotRecordsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **exportSnapshotRecords** *(list) --*

        A list of objects describing the export snapshot records.
        - *(dict) --*

          Describes an export snapshot record.
          - **name** *(string) --*

            The export snapshot record name.
    """


_GetInstanceSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetInstanceSnapshotsPaginatePaginationConfigTypeDef(
    _GetInstanceSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef(
    _GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef
):
    pass


_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef(
    _GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef
):
    pass


_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef(
    _GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef
):
    pass


_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[
            GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDiskstagsTypeDef
        ],
        "addOns": List[
            GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksaddOnsTypeDef
        ],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksTypeDef(
    _GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksTypeDef
):
    pass


_GetInstanceSnapshotsPaginateResponseinstanceSnapshotslocationTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseinstanceSnapshotslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetInstanceSnapshotsPaginateResponseinstanceSnapshotslocationTypeDef(
    _GetInstanceSnapshotsPaginateResponseinstanceSnapshotslocationTypeDef
):
    pass


_GetInstanceSnapshotsPaginateResponseinstanceSnapshotstagsTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseinstanceSnapshotstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetInstanceSnapshotsPaginateResponseinstanceSnapshotstagsTypeDef(
    _GetInstanceSnapshotsPaginateResponseinstanceSnapshotstagsTypeDef
):
    pass


_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseinstanceSnapshotsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetInstanceSnapshotsPaginateResponseinstanceSnapshotslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetInstanceSnapshotsPaginateResponseinstanceSnapshotstagsTypeDef],
        "state": Literal["pending", "error", "available"],
        "progress": str,
        "fromAttachedDisks": List[
            GetInstanceSnapshotsPaginateResponseinstanceSnapshotsfromAttachedDisksTypeDef
        ],
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "fromBlueprintId": str,
        "fromBundleId": str,
        "isFromAutoSnapshot": bool,
        "sizeInGb": int,
    },
    total=False,
)


class GetInstanceSnapshotsPaginateResponseinstanceSnapshotsTypeDef(
    _GetInstanceSnapshotsPaginateResponseinstanceSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes an instance snapshot.
      - **name** *(string) --*

        The name of the snapshot.
    """


_GetInstanceSnapshotsPaginateResponseTypeDef = TypedDict(
    "_GetInstanceSnapshotsPaginateResponseTypeDef",
    {
        "instanceSnapshots": List[GetInstanceSnapshotsPaginateResponseinstanceSnapshotsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetInstanceSnapshotsPaginateResponseTypeDef(_GetInstanceSnapshotsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **instanceSnapshots** *(list) --*

        An array of key-value pairs containing information about the results of your get instance
        snapshots request.
        - *(dict) --*

          Describes an instance snapshot.
          - **name** *(string) --*

            The name of the snapshot.
    """


_GetInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetInstancesPaginatePaginationConfigTypeDef(_GetInstancesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetInstancesPaginateResponseinstancesaddOnsTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstancesaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class GetInstancesPaginateResponseinstancesaddOnsTypeDef(
    _GetInstancesPaginateResponseinstancesaddOnsTypeDef
):
    pass


_GetInstancesPaginateResponseinstanceshardwaredisksaddOnsTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstanceshardwaredisksaddOnsTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)


class GetInstancesPaginateResponseinstanceshardwaredisksaddOnsTypeDef(
    _GetInstancesPaginateResponseinstanceshardwaredisksaddOnsTypeDef
):
    pass


_GetInstancesPaginateResponseinstanceshardwarediskslocationTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstanceshardwarediskslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetInstancesPaginateResponseinstanceshardwarediskslocationTypeDef(
    _GetInstancesPaginateResponseinstanceshardwarediskslocationTypeDef
):
    pass


_GetInstancesPaginateResponseinstanceshardwarediskstagsTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstanceshardwarediskstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetInstancesPaginateResponseinstanceshardwarediskstagsTypeDef(
    _GetInstancesPaginateResponseinstanceshardwarediskstagsTypeDef
):
    pass


_GetInstancesPaginateResponseinstanceshardwaredisksTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstanceshardwaredisksTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetInstancesPaginateResponseinstanceshardwarediskslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetInstancesPaginateResponseinstanceshardwarediskstagsTypeDef],
        "addOns": List[GetInstancesPaginateResponseinstanceshardwaredisksaddOnsTypeDef],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": Literal["pending", "error", "available", "in-use", "unknown"],
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)


class GetInstancesPaginateResponseinstanceshardwaredisksTypeDef(
    _GetInstancesPaginateResponseinstanceshardwaredisksTypeDef
):
    pass


_GetInstancesPaginateResponseinstanceshardwareTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstanceshardwareTypeDef",
    {
        "cpuCount": int,
        "disks": List[GetInstancesPaginateResponseinstanceshardwaredisksTypeDef],
        "ramSizeInGb": Any,
    },
    total=False,
)


class GetInstancesPaginateResponseinstanceshardwareTypeDef(
    _GetInstancesPaginateResponseinstanceshardwareTypeDef
):
    pass


_GetInstancesPaginateResponseinstanceslocationTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstanceslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetInstancesPaginateResponseinstanceslocationTypeDef(
    _GetInstancesPaginateResponseinstanceslocationTypeDef
):
    pass


_GetInstancesPaginateResponseinstancesnetworkingmonthlyTransferTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstancesnetworkingmonthlyTransferTypeDef",
    {"gbPerMonthAllocated": int},
    total=False,
)


class GetInstancesPaginateResponseinstancesnetworkingmonthlyTransferTypeDef(
    _GetInstancesPaginateResponseinstancesnetworkingmonthlyTransferTypeDef
):
    pass


_GetInstancesPaginateResponseinstancesnetworkingportsTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstancesnetworkingportsTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": Literal["tcp", "all", "udp"],
        "accessFrom": str,
        "accessType": Literal["Public", "Private"],
        "commonName": str,
        "accessDirection": Literal["inbound", "outbound"],
    },
    total=False,
)


class GetInstancesPaginateResponseinstancesnetworkingportsTypeDef(
    _GetInstancesPaginateResponseinstancesnetworkingportsTypeDef
):
    pass


_GetInstancesPaginateResponseinstancesnetworkingTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstancesnetworkingTypeDef",
    {
        "monthlyTransfer": GetInstancesPaginateResponseinstancesnetworkingmonthlyTransferTypeDef,
        "ports": List[GetInstancesPaginateResponseinstancesnetworkingportsTypeDef],
    },
    total=False,
)


class GetInstancesPaginateResponseinstancesnetworkingTypeDef(
    _GetInstancesPaginateResponseinstancesnetworkingTypeDef
):
    pass


_GetInstancesPaginateResponseinstancesstateTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstancesstateTypeDef", {"code": int, "name": str}, total=False
)


class GetInstancesPaginateResponseinstancesstateTypeDef(
    _GetInstancesPaginateResponseinstancesstateTypeDef
):
    pass


_GetInstancesPaginateResponseinstancestagsTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstancestagsTypeDef", {"key": str, "value": str}, total=False
)


class GetInstancesPaginateResponseinstancestagsTypeDef(
    _GetInstancesPaginateResponseinstancestagsTypeDef
):
    pass


_GetInstancesPaginateResponseinstancesTypeDef = TypedDict(
    "_GetInstancesPaginateResponseinstancesTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetInstancesPaginateResponseinstanceslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetInstancesPaginateResponseinstancestagsTypeDef],
        "blueprintId": str,
        "blueprintName": str,
        "bundleId": str,
        "addOns": List[GetInstancesPaginateResponseinstancesaddOnsTypeDef],
        "isStaticIp": bool,
        "privateIpAddress": str,
        "publicIpAddress": str,
        "ipv6Address": str,
        "hardware": GetInstancesPaginateResponseinstanceshardwareTypeDef,
        "networking": GetInstancesPaginateResponseinstancesnetworkingTypeDef,
        "state": GetInstancesPaginateResponseinstancesstateTypeDef,
        "username": str,
        "sshKeyName": str,
    },
    total=False,
)


class GetInstancesPaginateResponseinstancesTypeDef(_GetInstancesPaginateResponseinstancesTypeDef):
    """
    - *(dict) --*

      Describes an instance (a virtual private server).
      - **name** *(string) --*

        The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
    """


_GetInstancesPaginateResponseTypeDef = TypedDict(
    "_GetInstancesPaginateResponseTypeDef",
    {"instances": List[GetInstancesPaginateResponseinstancesTypeDef], "NextToken": str},
    total=False,
)


class GetInstancesPaginateResponseTypeDef(_GetInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **instances** *(list) --*

        An array of key-value pairs containing information about your instances.
        - *(dict) --*

          Describes an instance (a virtual private server).
          - **name** *(string) --*

            The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
    """


_GetKeyPairsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetKeyPairsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetKeyPairsPaginatePaginationConfigTypeDef(_GetKeyPairsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetKeyPairsPaginateResponsekeyPairslocationTypeDef = TypedDict(
    "_GetKeyPairsPaginateResponsekeyPairslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetKeyPairsPaginateResponsekeyPairslocationTypeDef(
    _GetKeyPairsPaginateResponsekeyPairslocationTypeDef
):
    pass


_GetKeyPairsPaginateResponsekeyPairstagsTypeDef = TypedDict(
    "_GetKeyPairsPaginateResponsekeyPairstagsTypeDef", {"key": str, "value": str}, total=False
)


class GetKeyPairsPaginateResponsekeyPairstagsTypeDef(
    _GetKeyPairsPaginateResponsekeyPairstagsTypeDef
):
    pass


_GetKeyPairsPaginateResponsekeyPairsTypeDef = TypedDict(
    "_GetKeyPairsPaginateResponsekeyPairsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetKeyPairsPaginateResponsekeyPairslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetKeyPairsPaginateResponsekeyPairstagsTypeDef],
        "fingerprint": str,
    },
    total=False,
)


class GetKeyPairsPaginateResponsekeyPairsTypeDef(_GetKeyPairsPaginateResponsekeyPairsTypeDef):
    """
    - *(dict) --*

      Describes the SSH key pair.
      - **name** *(string) --*

        The friendly name of the SSH key pair.
    """


_GetKeyPairsPaginateResponseTypeDef = TypedDict(
    "_GetKeyPairsPaginateResponseTypeDef",
    {"keyPairs": List[GetKeyPairsPaginateResponsekeyPairsTypeDef], "NextToken": str},
    total=False,
)


class GetKeyPairsPaginateResponseTypeDef(_GetKeyPairsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **keyPairs** *(list) --*

        An array of key-value pairs containing information about the key pairs.
        - *(dict) --*

          Describes the SSH key pair.
          - **name** *(string) --*

            The friendly name of the SSH key pair.
    """


_GetLoadBalancersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetLoadBalancersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetLoadBalancersPaginatePaginationConfigTypeDef(
    _GetLoadBalancersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetLoadBalancersPaginateResponseloadBalancersinstanceHealthSummaryTypeDef = TypedDict(
    "_GetLoadBalancersPaginateResponseloadBalancersinstanceHealthSummaryTypeDef",
    {
        "instanceName": str,
        "instanceHealth": Literal[
            "initial", "healthy", "unhealthy", "unused", "draining", "unavailable"
        ],
        "instanceHealthReason": Literal[
            "Lb.RegistrationInProgress",
            "Lb.InitialHealthChecking",
            "Lb.InternalError",
            "Instance.ResponseCodeMismatch",
            "Instance.Timeout",
            "Instance.FailedHealthChecks",
            "Instance.NotRegistered",
            "Instance.NotInUse",
            "Instance.DeregistrationInProgress",
            "Instance.InvalidState",
            "Instance.IpUnusable",
        ],
    },
    total=False,
)


class GetLoadBalancersPaginateResponseloadBalancersinstanceHealthSummaryTypeDef(
    _GetLoadBalancersPaginateResponseloadBalancersinstanceHealthSummaryTypeDef
):
    pass


_GetLoadBalancersPaginateResponseloadBalancerslocationTypeDef = TypedDict(
    "_GetLoadBalancersPaginateResponseloadBalancerslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetLoadBalancersPaginateResponseloadBalancerslocationTypeDef(
    _GetLoadBalancersPaginateResponseloadBalancerslocationTypeDef
):
    pass


_GetLoadBalancersPaginateResponseloadBalancerstagsTypeDef = TypedDict(
    "_GetLoadBalancersPaginateResponseloadBalancerstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetLoadBalancersPaginateResponseloadBalancerstagsTypeDef(
    _GetLoadBalancersPaginateResponseloadBalancerstagsTypeDef
):
    pass


_GetLoadBalancersPaginateResponseloadBalancerstlsCertificateSummariesTypeDef = TypedDict(
    "_GetLoadBalancersPaginateResponseloadBalancerstlsCertificateSummariesTypeDef",
    {"name": str, "isAttached": bool},
    total=False,
)


class GetLoadBalancersPaginateResponseloadBalancerstlsCertificateSummariesTypeDef(
    _GetLoadBalancersPaginateResponseloadBalancerstlsCertificateSummariesTypeDef
):
    pass


_GetLoadBalancersPaginateResponseloadBalancersTypeDef = TypedDict(
    "_GetLoadBalancersPaginateResponseloadBalancersTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetLoadBalancersPaginateResponseloadBalancerslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetLoadBalancersPaginateResponseloadBalancerstagsTypeDef],
        "dnsName": str,
        "state": Literal["active", "provisioning", "active_impaired", "failed", "unknown"],
        "protocol": Literal["HTTP_HTTPS", "HTTP"],
        "publicPorts": List[int],
        "healthCheckPath": str,
        "instancePort": int,
        "instanceHealthSummary": List[
            GetLoadBalancersPaginateResponseloadBalancersinstanceHealthSummaryTypeDef
        ],
        "tlsCertificateSummaries": List[
            GetLoadBalancersPaginateResponseloadBalancerstlsCertificateSummariesTypeDef
        ],
        "configurationOptions": Dict[str, str],
    },
    total=False,
)


class GetLoadBalancersPaginateResponseloadBalancersTypeDef(
    _GetLoadBalancersPaginateResponseloadBalancersTypeDef
):
    """
    - *(dict) --*

      Describes the Lightsail load balancer.
      - **name** *(string) --*

        The name of the load balancer (e.g., ``my-load-balancer`` ).
    """


_GetLoadBalancersPaginateResponseTypeDef = TypedDict(
    "_GetLoadBalancersPaginateResponseTypeDef",
    {"loadBalancers": List[GetLoadBalancersPaginateResponseloadBalancersTypeDef], "NextToken": str},
    total=False,
)


class GetLoadBalancersPaginateResponseTypeDef(_GetLoadBalancersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **loadBalancers** *(list) --*

        An array of LoadBalancer objects describing your load balancers.
        - *(dict) --*

          Describes the Lightsail load balancer.
          - **name** *(string) --*

            The name of the load balancer (e.g., ``my-load-balancer`` ).
    """


_GetOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetOperationsPaginatePaginationConfigTypeDef(_GetOperationsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetOperationsPaginateResponseoperationslocationTypeDef = TypedDict(
    "_GetOperationsPaginateResponseoperationslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetOperationsPaginateResponseoperationslocationTypeDef(
    _GetOperationsPaginateResponseoperationslocationTypeDef
):
    pass


_GetOperationsPaginateResponseoperationsTypeDef = TypedDict(
    "_GetOperationsPaginateResponseoperationsTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "createdAt": datetime,
        "location": GetOperationsPaginateResponseoperationslocationTypeDef,
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": Literal[
            "DeleteKnownHostKeys",
            "DeleteInstance",
            "CreateInstance",
            "StopInstance",
            "StartInstance",
            "RebootInstance",
            "OpenInstancePublicPorts",
            "PutInstancePublicPorts",
            "CloseInstancePublicPorts",
            "AllocateStaticIp",
            "ReleaseStaticIp",
            "AttachStaticIp",
            "DetachStaticIp",
            "UpdateDomainEntry",
            "DeleteDomainEntry",
            "CreateDomain",
            "DeleteDomain",
            "CreateInstanceSnapshot",
            "DeleteInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "DeleteLoadBalancer",
            "AttachInstancesToLoadBalancer",
            "DetachInstancesFromLoadBalancer",
            "UpdateLoadBalancerAttribute",
            "CreateLoadBalancerTlsCertificate",
            "DeleteLoadBalancerTlsCertificate",
            "AttachLoadBalancerTlsCertificate",
            "CreateDisk",
            "DeleteDisk",
            "AttachDisk",
            "DetachDisk",
            "CreateDiskSnapshot",
            "DeleteDiskSnapshot",
            "CreateDiskFromSnapshot",
            "CreateRelationalDatabase",
            "UpdateRelationalDatabase",
            "DeleteRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteRelationalDatabaseSnapshot",
            "UpdateRelationalDatabaseParameters",
            "StartRelationalDatabase",
            "RebootRelationalDatabase",
            "StopRelationalDatabase",
            "EnableAddOn",
            "DisableAddOn",
        ],
        "status": Literal["NotStarted", "Started", "Failed", "Completed", "Succeeded"],
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class GetOperationsPaginateResponseoperationsTypeDef(
    _GetOperationsPaginateResponseoperationsTypeDef
):
    """
    - *(dict) --*

      Describes the API operation.
      - **id** *(string) --*

        The ID of the operation.
    """


_GetOperationsPaginateResponseTypeDef = TypedDict(
    "_GetOperationsPaginateResponseTypeDef",
    {"operations": List[GetOperationsPaginateResponseoperationsTypeDef], "NextToken": str},
    total=False,
)


class GetOperationsPaginateResponseTypeDef(_GetOperationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **operations** *(list) --*

        An array of key-value pairs containing information about the results of your get operations
        request.
        - *(dict) --*

          Describes the API operation.
          - **id** *(string) --*

            The ID of the operation.
    """


_GetRelationalDatabaseBlueprintsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRelationalDatabaseBlueprintsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetRelationalDatabaseBlueprintsPaginatePaginationConfigTypeDef(
    _GetRelationalDatabaseBlueprintsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRelationalDatabaseBlueprintsPaginateResponseblueprintsTypeDef = TypedDict(
    "_GetRelationalDatabaseBlueprintsPaginateResponseblueprintsTypeDef",
    {
        "blueprintId": str,
        "engine": str,
        "engineVersion": str,
        "engineDescription": str,
        "engineVersionDescription": str,
        "isEngineDefault": bool,
    },
    total=False,
)


class GetRelationalDatabaseBlueprintsPaginateResponseblueprintsTypeDef(
    _GetRelationalDatabaseBlueprintsPaginateResponseblueprintsTypeDef
):
    """
    - *(dict) --*

      Describes a database image, or blueprint. A blueprint describes the major engine version of a
      database.
      - **blueprintId** *(string) --*

        The ID for the database blueprint.
    """


_GetRelationalDatabaseBlueprintsPaginateResponseTypeDef = TypedDict(
    "_GetRelationalDatabaseBlueprintsPaginateResponseTypeDef",
    {
        "blueprints": List[GetRelationalDatabaseBlueprintsPaginateResponseblueprintsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetRelationalDatabaseBlueprintsPaginateResponseTypeDef(
    _GetRelationalDatabaseBlueprintsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **blueprints** *(list) --*

        An object describing the result of your get relational database blueprints request.
        - *(dict) --*

          Describes a database image, or blueprint. A blueprint describes the major engine version
          of a database.
          - **blueprintId** *(string) --*

            The ID for the database blueprint.
    """


_GetRelationalDatabaseBundlesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRelationalDatabaseBundlesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetRelationalDatabaseBundlesPaginatePaginationConfigTypeDef(
    _GetRelationalDatabaseBundlesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRelationalDatabaseBundlesPaginateResponsebundlesTypeDef = TypedDict(
    "_GetRelationalDatabaseBundlesPaginateResponsebundlesTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": Any,
        "ramSizeInGb": Any,
        "diskSizeInGb": int,
        "transferPerMonthInGb": int,
        "cpuCount": int,
        "isEncrypted": bool,
        "isActive": bool,
    },
    total=False,
)


class GetRelationalDatabaseBundlesPaginateResponsebundlesTypeDef(
    _GetRelationalDatabaseBundlesPaginateResponsebundlesTypeDef
):
    """
    - *(dict) --*

      Describes a database bundle. A bundle describes the performance specifications of the
      database.
      - **bundleId** *(string) --*

        The ID for the database bundle.
    """


_GetRelationalDatabaseBundlesPaginateResponseTypeDef = TypedDict(
    "_GetRelationalDatabaseBundlesPaginateResponseTypeDef",
    {"bundles": List[GetRelationalDatabaseBundlesPaginateResponsebundlesTypeDef], "NextToken": str},
    total=False,
)


class GetRelationalDatabaseBundlesPaginateResponseTypeDef(
    _GetRelationalDatabaseBundlesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **bundles** *(list) --*

        An object describing the result of your get relational database bundles request.
        - *(dict) --*

          Describes a database bundle. A bundle describes the performance specifications of the
          database.
          - **bundleId** *(string) --*

            The ID for the database bundle.
    """


_GetRelationalDatabaseEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRelationalDatabaseEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetRelationalDatabaseEventsPaginatePaginationConfigTypeDef(
    _GetRelationalDatabaseEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRelationalDatabaseEventsPaginateResponserelationalDatabaseEventsTypeDef = TypedDict(
    "_GetRelationalDatabaseEventsPaginateResponserelationalDatabaseEventsTypeDef",
    {"resource": str, "createdAt": datetime, "message": str, "eventCategories": List[str]},
    total=False,
)


class GetRelationalDatabaseEventsPaginateResponserelationalDatabaseEventsTypeDef(
    _GetRelationalDatabaseEventsPaginateResponserelationalDatabaseEventsTypeDef
):
    """
    - *(dict) --*

      Describes an event for a database.
      - **resource** *(string) --*

        The database that the database event relates to.
    """


_GetRelationalDatabaseEventsPaginateResponseTypeDef = TypedDict(
    "_GetRelationalDatabaseEventsPaginateResponseTypeDef",
    {
        "relationalDatabaseEvents": List[
            GetRelationalDatabaseEventsPaginateResponserelationalDatabaseEventsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetRelationalDatabaseEventsPaginateResponseTypeDef(
    _GetRelationalDatabaseEventsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **relationalDatabaseEvents** *(list) --*

        An object describing the result of your get relational database events request.
        - *(dict) --*

          Describes an event for a database.
          - **resource** *(string) --*

            The database that the database event relates to.
    """


_GetRelationalDatabaseParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRelationalDatabaseParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetRelationalDatabaseParametersPaginatePaginationConfigTypeDef(
    _GetRelationalDatabaseParametersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRelationalDatabaseParametersPaginateResponseparametersTypeDef = TypedDict(
    "_GetRelationalDatabaseParametersPaginateResponseparametersTypeDef",
    {
        "allowedValues": str,
        "applyMethod": str,
        "applyType": str,
        "dataType": str,
        "description": str,
        "isModifiable": bool,
        "parameterName": str,
        "parameterValue": str,
    },
    total=False,
)


class GetRelationalDatabaseParametersPaginateResponseparametersTypeDef(
    _GetRelationalDatabaseParametersPaginateResponseparametersTypeDef
):
    """
    - *(dict) --*

      Describes the parameters of a database.
      - **allowedValues** *(string) --*

        Specifies the valid range of values for the parameter.
    """


_GetRelationalDatabaseParametersPaginateResponseTypeDef = TypedDict(
    "_GetRelationalDatabaseParametersPaginateResponseTypeDef",
    {
        "parameters": List[GetRelationalDatabaseParametersPaginateResponseparametersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetRelationalDatabaseParametersPaginateResponseTypeDef(
    _GetRelationalDatabaseParametersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **parameters** *(list) --*

        An object describing the result of your get relational database parameters request.
        - *(dict) --*

          Describes the parameters of a database.
          - **allowedValues** *(string) --*

            Specifies the valid range of values for the parameter.
    """


_GetRelationalDatabaseSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRelationalDatabaseSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetRelationalDatabaseSnapshotsPaginatePaginationConfigTypeDef(
    _GetRelationalDatabaseSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotslocationTypeDef = TypedDict(
    "_GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotslocationTypeDef(
    _GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotslocationTypeDef
):
    pass


_GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotstagsTypeDef = TypedDict(
    "_GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotstagsTypeDef(
    _GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotstagsTypeDef
):
    pass


_GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotsTypeDef = TypedDict(
    "_GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[
            GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotstagsTypeDef
        ],
        "engine": str,
        "engineVersion": str,
        "sizeInGb": int,
        "state": str,
        "fromRelationalDatabaseName": str,
        "fromRelationalDatabaseArn": str,
        "fromRelationalDatabaseBundleId": str,
        "fromRelationalDatabaseBlueprintId": str,
    },
    total=False,
)


class GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotsTypeDef(
    _GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a database snapshot.
      - **name** *(string) --*

        The name of the database snapshot.
    """


_GetRelationalDatabaseSnapshotsPaginateResponseTypeDef = TypedDict(
    "_GetRelationalDatabaseSnapshotsPaginateResponseTypeDef",
    {
        "relationalDatabaseSnapshots": List[
            GetRelationalDatabaseSnapshotsPaginateResponserelationalDatabaseSnapshotsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetRelationalDatabaseSnapshotsPaginateResponseTypeDef(
    _GetRelationalDatabaseSnapshotsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **relationalDatabaseSnapshots** *(list) --*

        An object describing the result of your get relational database snapshots request.
        - *(dict) --*

          Describes a database snapshot.
          - **name** *(string) --*

            The name of the database snapshot.
    """


_GetRelationalDatabasesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetRelationalDatabasesPaginatePaginationConfigTypeDef(
    _GetRelationalDatabasesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRelationalDatabasesPaginateResponserelationalDatabaseshardwareTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponserelationalDatabaseshardwareTypeDef",
    {"cpuCount": int, "diskSizeInGb": int, "ramSizeInGb": Any},
    total=False,
)


class GetRelationalDatabasesPaginateResponserelationalDatabaseshardwareTypeDef(
    _GetRelationalDatabasesPaginateResponserelationalDatabaseshardwareTypeDef
):
    pass


_GetRelationalDatabasesPaginateResponserelationalDatabaseslocationTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponserelationalDatabaseslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetRelationalDatabasesPaginateResponserelationalDatabaseslocationTypeDef(
    _GetRelationalDatabasesPaginateResponserelationalDatabaseslocationTypeDef
):
    pass


_GetRelationalDatabasesPaginateResponserelationalDatabasesmasterEndpointTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponserelationalDatabasesmasterEndpointTypeDef",
    {"port": int, "address": str},
    total=False,
)


class GetRelationalDatabasesPaginateResponserelationalDatabasesmasterEndpointTypeDef(
    _GetRelationalDatabasesPaginateResponserelationalDatabasesmasterEndpointTypeDef
):
    pass


_GetRelationalDatabasesPaginateResponserelationalDatabasespendingMaintenanceActionsTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponserelationalDatabasespendingMaintenanceActionsTypeDef",
    {"action": str, "description": str, "currentApplyDate": datetime},
    total=False,
)


class GetRelationalDatabasesPaginateResponserelationalDatabasespendingMaintenanceActionsTypeDef(
    _GetRelationalDatabasesPaginateResponserelationalDatabasespendingMaintenanceActionsTypeDef
):
    pass


_GetRelationalDatabasesPaginateResponserelationalDatabasespendingModifiedValuesTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponserelationalDatabasespendingModifiedValuesTypeDef",
    {"masterUserPassword": str, "engineVersion": str, "backupRetentionEnabled": bool},
    total=False,
)


class GetRelationalDatabasesPaginateResponserelationalDatabasespendingModifiedValuesTypeDef(
    _GetRelationalDatabasesPaginateResponserelationalDatabasespendingModifiedValuesTypeDef
):
    pass


_GetRelationalDatabasesPaginateResponserelationalDatabasestagsTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponserelationalDatabasestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetRelationalDatabasesPaginateResponserelationalDatabasestagsTypeDef(
    _GetRelationalDatabasesPaginateResponserelationalDatabasestagsTypeDef
):
    pass


_GetRelationalDatabasesPaginateResponserelationalDatabasesTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponserelationalDatabasesTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetRelationalDatabasesPaginateResponserelationalDatabaseslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "tags": List[GetRelationalDatabasesPaginateResponserelationalDatabasestagsTypeDef],
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "hardware": GetRelationalDatabasesPaginateResponserelationalDatabaseshardwareTypeDef,
        "state": str,
        "secondaryAvailabilityZone": str,
        "backupRetentionEnabled": bool,
        "pendingModifiedValues": GetRelationalDatabasesPaginateResponserelationalDatabasespendingModifiedValuesTypeDef,
        "engine": str,
        "engineVersion": str,
        "latestRestorableTime": datetime,
        "masterUsername": str,
        "parameterApplyStatus": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "masterEndpoint": GetRelationalDatabasesPaginateResponserelationalDatabasesmasterEndpointTypeDef,
        "pendingMaintenanceActions": List[
            GetRelationalDatabasesPaginateResponserelationalDatabasespendingMaintenanceActionsTypeDef
        ],
    },
    total=False,
)


class GetRelationalDatabasesPaginateResponserelationalDatabasesTypeDef(
    _GetRelationalDatabasesPaginateResponserelationalDatabasesTypeDef
):
    """
    - *(dict) --*

      Describes a database.
      - **name** *(string) --*

        The unique name of the database resource in Lightsail.
    """


_GetRelationalDatabasesPaginateResponseTypeDef = TypedDict(
    "_GetRelationalDatabasesPaginateResponseTypeDef",
    {
        "relationalDatabases": List[
            GetRelationalDatabasesPaginateResponserelationalDatabasesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetRelationalDatabasesPaginateResponseTypeDef(_GetRelationalDatabasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **relationalDatabases** *(list) --*

        An object describing the result of your get relational databases request.
        - *(dict) --*

          Describes a database.
          - **name** *(string) --*

            The unique name of the database resource in Lightsail.
    """


_GetStaticIpsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetStaticIpsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetStaticIpsPaginatePaginationConfigTypeDef(_GetStaticIpsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetStaticIpsPaginateResponsestaticIpslocationTypeDef = TypedDict(
    "_GetStaticIpsPaginateResponsestaticIpslocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
    },
    total=False,
)


class GetStaticIpsPaginateResponsestaticIpslocationTypeDef(
    _GetStaticIpsPaginateResponsestaticIpslocationTypeDef
):
    pass


_GetStaticIpsPaginateResponsestaticIpsTypeDef = TypedDict(
    "_GetStaticIpsPaginateResponsestaticIpsTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": GetStaticIpsPaginateResponsestaticIpslocationTypeDef,
        "resourceType": Literal[
            "Instance",
            "StaticIp",
            "KeyPair",
            "InstanceSnapshot",
            "Domain",
            "PeeredVpc",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "Disk",
            "DiskSnapshot",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "ExportSnapshotRecord",
            "CloudFormationStackRecord",
        ],
        "ipAddress": str,
        "attachedTo": str,
        "isAttached": bool,
    },
    total=False,
)


class GetStaticIpsPaginateResponsestaticIpsTypeDef(_GetStaticIpsPaginateResponsestaticIpsTypeDef):
    """
    - *(dict) --*

      Describes the static IP.
      - **name** *(string) --*

        The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
    """


_GetStaticIpsPaginateResponseTypeDef = TypedDict(
    "_GetStaticIpsPaginateResponseTypeDef",
    {"staticIps": List[GetStaticIpsPaginateResponsestaticIpsTypeDef], "NextToken": str},
    total=False,
)


class GetStaticIpsPaginateResponseTypeDef(_GetStaticIpsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **staticIps** *(list) --*

        An array of key-value pairs containing information about your get static IPs request.
        - *(dict) --*

          Describes the static IP.
          - **name** *(string) --*

            The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
    """
