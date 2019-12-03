"Main interface for appmesh service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateMeshResponsemeshmetadataTypeDef",
    "ClientCreateMeshResponsemeshspecegressFilterTypeDef",
    "ClientCreateMeshResponsemeshspecTypeDef",
    "ClientCreateMeshResponsemeshstatusTypeDef",
    "ClientCreateMeshResponsemeshTypeDef",
    "ClientCreateMeshResponseTypeDef",
    "ClientCreateMeshSpecegressFilterTypeDef",
    "ClientCreateMeshSpecTypeDef",
    "ClientCreateMeshTagsTypeDef",
    "ClientCreateRouteResponseroutemetadataTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteactionTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteactionTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteTypeDef",
    "ClientCreateRouteResponseroutespecTypeDef",
    "ClientCreateRouteResponseroutestatusTypeDef",
    "ClientCreateRouteResponserouteTypeDef",
    "ClientCreateRouteResponseTypeDef",
    "ClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpecgrpcRouteactionTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchTypeDef",
    "ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef",
    "ClientCreateRouteSpecgrpcRouteTypeDef",
    "ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpechttp2RouteactionTypeDef",
    "ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef",
    "ClientCreateRouteSpechttp2RoutematchheadersTypeDef",
    "ClientCreateRouteSpechttp2RoutematchTypeDef",
    "ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteSpechttp2RouteretryPolicyTypeDef",
    "ClientCreateRouteSpechttp2RouteTypeDef",
    "ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpechttpRouteactionTypeDef",
    "ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef",
    "ClientCreateRouteSpechttpRoutematchheadersTypeDef",
    "ClientCreateRouteSpechttpRoutematchTypeDef",
    "ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteSpechttpRouteretryPolicyTypeDef",
    "ClientCreateRouteSpechttpRouteTypeDef",
    "ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpectcpRouteactionTypeDef",
    "ClientCreateRouteSpectcpRouteTypeDef",
    "ClientCreateRouteSpecTypeDef",
    "ClientCreateRouteTagsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodeTypeDef",
    "ClientCreateVirtualNodeResponseTypeDef",
    "ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef",
    "ClientCreateVirtualNodeSpecbackendsTypeDef",
    "ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef",
    "ClientCreateVirtualNodeSpeclistenersportMappingTypeDef",
    "ClientCreateVirtualNodeSpeclistenersTypeDef",
    "ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef",
    "ClientCreateVirtualNodeSpecloggingaccessLogTypeDef",
    "ClientCreateVirtualNodeSpecloggingTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef",
    "ClientCreateVirtualNodeSpecTypeDef",
    "ClientCreateVirtualNodeTagsTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterTypeDef",
    "ClientCreateVirtualRouterResponseTypeDef",
    "ClientCreateVirtualRouterSpeclistenersportMappingTypeDef",
    "ClientCreateVirtualRouterSpeclistenersTypeDef",
    "ClientCreateVirtualRouterSpecTypeDef",
    "ClientCreateVirtualRouterTagsTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServiceTypeDef",
    "ClientCreateVirtualServiceResponseTypeDef",
    "ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef",
    "ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef",
    "ClientCreateVirtualServiceSpecproviderTypeDef",
    "ClientCreateVirtualServiceSpecTypeDef",
    "ClientCreateVirtualServiceTagsTypeDef",
    "ClientDeleteMeshResponsemeshmetadataTypeDef",
    "ClientDeleteMeshResponsemeshspecegressFilterTypeDef",
    "ClientDeleteMeshResponsemeshspecTypeDef",
    "ClientDeleteMeshResponsemeshstatusTypeDef",
    "ClientDeleteMeshResponsemeshTypeDef",
    "ClientDeleteMeshResponseTypeDef",
    "ClientDeleteRouteResponseroutemetadataTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteTypeDef",
    "ClientDeleteRouteResponseroutespecTypeDef",
    "ClientDeleteRouteResponseroutestatusTypeDef",
    "ClientDeleteRouteResponserouteTypeDef",
    "ClientDeleteRouteResponseTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodeTypeDef",
    "ClientDeleteVirtualNodeResponseTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterTypeDef",
    "ClientDeleteVirtualRouterResponseTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServiceTypeDef",
    "ClientDeleteVirtualServiceResponseTypeDef",
    "ClientDescribeMeshResponsemeshmetadataTypeDef",
    "ClientDescribeMeshResponsemeshspecegressFilterTypeDef",
    "ClientDescribeMeshResponsemeshspecTypeDef",
    "ClientDescribeMeshResponsemeshstatusTypeDef",
    "ClientDescribeMeshResponsemeshTypeDef",
    "ClientDescribeMeshResponseTypeDef",
    "ClientDescribeRouteResponseroutemetadataTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteTypeDef",
    "ClientDescribeRouteResponseroutespecTypeDef",
    "ClientDescribeRouteResponseroutestatusTypeDef",
    "ClientDescribeRouteResponserouteTypeDef",
    "ClientDescribeRouteResponseTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodeTypeDef",
    "ClientDescribeVirtualNodeResponseTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterTypeDef",
    "ClientDescribeVirtualRouterResponseTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServiceTypeDef",
    "ClientDescribeVirtualServiceResponseTypeDef",
    "ClientListMeshesResponsemeshesTypeDef",
    "ClientListMeshesResponseTypeDef",
    "ClientListRoutesResponseroutesTypeDef",
    "ClientListRoutesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListVirtualNodesResponsevirtualNodesTypeDef",
    "ClientListVirtualNodesResponseTypeDef",
    "ClientListVirtualRoutersResponsevirtualRoutersTypeDef",
    "ClientListVirtualRoutersResponseTypeDef",
    "ClientListVirtualServicesResponsevirtualServicesTypeDef",
    "ClientListVirtualServicesResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateMeshResponsemeshmetadataTypeDef",
    "ClientUpdateMeshResponsemeshspecegressFilterTypeDef",
    "ClientUpdateMeshResponsemeshspecTypeDef",
    "ClientUpdateMeshResponsemeshstatusTypeDef",
    "ClientUpdateMeshResponsemeshTypeDef",
    "ClientUpdateMeshResponseTypeDef",
    "ClientUpdateMeshSpecegressFilterTypeDef",
    "ClientUpdateMeshSpecTypeDef",
    "ClientUpdateRouteResponseroutemetadataTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteTypeDef",
    "ClientUpdateRouteResponseroutespecTypeDef",
    "ClientUpdateRouteResponseroutestatusTypeDef",
    "ClientUpdateRouteResponserouteTypeDef",
    "ClientUpdateRouteResponseTypeDef",
    "ClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpecgrpcRouteactionTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchTypeDef",
    "ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef",
    "ClientUpdateRouteSpecgrpcRouteTypeDef",
    "ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpechttp2RouteactionTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchheadersTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchTypeDef",
    "ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef",
    "ClientUpdateRouteSpechttp2RouteTypeDef",
    "ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpechttpRouteactionTypeDef",
    "ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef",
    "ClientUpdateRouteSpechttpRoutematchheadersTypeDef",
    "ClientUpdateRouteSpechttpRoutematchTypeDef",
    "ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteSpechttpRouteretryPolicyTypeDef",
    "ClientUpdateRouteSpechttpRouteTypeDef",
    "ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpectcpRouteactionTypeDef",
    "ClientUpdateRouteSpectcpRouteTypeDef",
    "ClientUpdateRouteSpecTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodeTypeDef",
    "ClientUpdateVirtualNodeResponseTypeDef",
    "ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef",
    "ClientUpdateVirtualNodeSpecbackendsTypeDef",
    "ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef",
    "ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef",
    "ClientUpdateVirtualNodeSpeclistenersTypeDef",
    "ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef",
    "ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef",
    "ClientUpdateVirtualNodeSpecloggingTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef",
    "ClientUpdateVirtualNodeSpecTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterTypeDef",
    "ClientUpdateVirtualRouterResponseTypeDef",
    "ClientUpdateVirtualRouterSpeclistenersportMappingTypeDef",
    "ClientUpdateVirtualRouterSpeclistenersTypeDef",
    "ClientUpdateVirtualRouterSpecTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServiceTypeDef",
    "ClientUpdateVirtualServiceResponseTypeDef",
    "ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef",
    "ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef",
    "ClientUpdateVirtualServiceSpecproviderTypeDef",
    "ClientUpdateVirtualServiceSpecTypeDef",
    "ListMeshesPaginatePaginationConfigTypeDef",
    "ListMeshesPaginateResponsemeshesTypeDef",
    "ListMeshesPaginateResponseTypeDef",
    "ListRoutesPaginatePaginationConfigTypeDef",
    "ListRoutesPaginateResponseroutesTypeDef",
    "ListRoutesPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponsetagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListVirtualNodesPaginatePaginationConfigTypeDef",
    "ListVirtualNodesPaginateResponsevirtualNodesTypeDef",
    "ListVirtualNodesPaginateResponseTypeDef",
    "ListVirtualRoutersPaginatePaginationConfigTypeDef",
    "ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef",
    "ListVirtualRoutersPaginateResponseTypeDef",
    "ListVirtualServicesPaginatePaginationConfigTypeDef",
    "ListVirtualServicesPaginateResponsevirtualServicesTypeDef",
    "ListVirtualServicesPaginateResponseTypeDef",
)


_ClientCreateMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientCreateMeshResponsemeshmetadataTypeDef(_ClientCreateMeshResponsemeshmetadataTypeDef):
    pass


_ClientCreateMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)


class ClientCreateMeshResponsemeshspecegressFilterTypeDef(
    _ClientCreateMeshResponsemeshspecegressFilterTypeDef
):
    pass


_ClientCreateMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientCreateMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientCreateMeshResponsemeshspecTypeDef(_ClientCreateMeshResponsemeshspecTypeDef):
    pass


_ClientCreateMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientCreateMeshResponsemeshstatusTypeDef(_ClientCreateMeshResponsemeshstatusTypeDef):
    pass


_ClientCreateMeshResponsemeshTypeDef = TypedDict(
    "_ClientCreateMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateMeshResponsemeshmetadataTypeDef,
        "spec": ClientCreateMeshResponsemeshspecTypeDef,
        "status": ClientCreateMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientCreateMeshResponsemeshTypeDef(_ClientCreateMeshResponsemeshTypeDef):
    """
    - **mesh** *(dict) --*

      The full description of your service mesh following the create call.
      - **meshName** *(string) --*

        The name of the service mesh.
    """


_ClientCreateMeshResponseTypeDef = TypedDict(
    "_ClientCreateMeshResponseTypeDef", {"mesh": ClientCreateMeshResponsemeshTypeDef}, total=False
)


class ClientCreateMeshResponseTypeDef(_ClientCreateMeshResponseTypeDef):
    """
    - *(dict) --*

      - **mesh** *(dict) --*

        The full description of your service mesh following the create call.
        - **meshName** *(string) --*

          The name of the service mesh.
    """


_ClientCreateMeshSpecegressFilterTypeDef = TypedDict(
    "_ClientCreateMeshSpecegressFilterTypeDef", {"type": Literal["ALLOW_ALL", "DROP_ALL"]}
)


class ClientCreateMeshSpecegressFilterTypeDef(_ClientCreateMeshSpecegressFilterTypeDef):
    """
    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.
      - **type** *(string) --***[REQUIRED]**

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
        virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
        to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientCreateMeshSpecTypeDef = TypedDict(
    "_ClientCreateMeshSpecTypeDef",
    {"egressFilter": ClientCreateMeshSpecegressFilterTypeDef},
    total=False,
)


class ClientCreateMeshSpecTypeDef(_ClientCreateMeshSpecTypeDef):
    """
    The service mesh specification to apply.
    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.
      - **type** *(string) --***[REQUIRED]**

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
        virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
        to allow egress to any endpoint inside or outside of the service mesh.
    """


_RequiredClientCreateMeshTagsTypeDef = TypedDict(
    "_RequiredClientCreateMeshTagsTypeDef", {"key": str}
)
_OptionalClientCreateMeshTagsTypeDef = TypedDict(
    "_OptionalClientCreateMeshTagsTypeDef", {"value": str}, total=False
)


class ClientCreateMeshTagsTypeDef(
    _RequiredClientCreateMeshTagsTypeDef, _OptionalClientCreateMeshTagsTypeDef
):
    """
    - *(dict) --*

      Optional metadata that you apply to a resource to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Tag keys can have
      a maximum character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **key** *(string) --***[REQUIRED]**

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientCreateRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientCreateRouteResponseroutemetadataTypeDef(_ClientCreateRouteResponseroutemetadataTypeDef):
    pass


_ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    pass


_ClientCreateRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecgrpcRouteTypeDef(
    _ClientCreateRouteResponseroutespecgrpcRouteTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteactionTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientCreateRouteResponseroutespechttp2RoutematchTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttp2RouteTypeDef(
    _ClientCreateRouteResponseroutespechttp2RouteTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteactionTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteactionTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRoutematchTypeDef(
    _ClientCreateRouteResponseroutespechttpRoutematchTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    pass


_ClientCreateRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespechttpRouteTypeDef(
    _ClientCreateRouteResponseroutespechttpRouteTypeDef
):
    pass


_ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    pass


_ClientCreateRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientCreateRouteResponseroutespectcpRouteactionTypeDef(
    _ClientCreateRouteResponseroutespectcpRouteactionTypeDef
):
    pass


_ClientCreateRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientCreateRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientCreateRouteResponseroutespectcpRouteTypeDef(
    _ClientCreateRouteResponseroutespectcpRouteTypeDef
):
    pass


_ClientCreateRouteResponseroutespecTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientCreateRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientCreateRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientCreateRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientCreateRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientCreateRouteResponseroutespecTypeDef(_ClientCreateRouteResponseroutespecTypeDef):
    pass


_ClientCreateRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientCreateRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientCreateRouteResponseroutestatusTypeDef(_ClientCreateRouteResponseroutestatusTypeDef):
    pass


_ClientCreateRouteResponserouteTypeDef = TypedDict(
    "_ClientCreateRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientCreateRouteResponseroutespecTypeDef,
        "status": ClientCreateRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientCreateRouteResponserouteTypeDef(_ClientCreateRouteResponserouteTypeDef):
    """
    - **route** *(dict) --*

      The full description of your mesh following the create call.
      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.
    """


_ClientCreateRouteResponseTypeDef = TypedDict(
    "_ClientCreateRouteResponseTypeDef",
    {"route": ClientCreateRouteResponserouteTypeDef},
    total=False,
)


class ClientCreateRouteResponseTypeDef(_ClientCreateRouteResponseTypeDef):
    """
    - *(dict) --*

      - **route** *(dict) --*

        The full description of your mesh following the create call.
        - **meshName** *(string) --*

          The name of the service mesh that the route resides in.
    """


_RequiredClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_RequiredClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef", {"virtualNode": str}
)
_OptionalClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_OptionalClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    {"weight": int},
    total=False,
)


class ClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef(
    _RequiredClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
    _OptionalClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
):
    """
    - *(dict) --*

      An object that represents a target and its relative weight. Traffic is distributed across
      targets according to their relative weight. For example, a weighted target with a relative
      weight of 50 receives five times as much traffic as one with a relative weight of 10. The
      total weight for all targets combined must be less than or equal to 100.
      - **virtualNode** *(string) --***[REQUIRED]**

        The virtual node to associate with the weighted target.
    """


_ClientCreateRouteSpecgrpcRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteSpecgrpcRouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef]},
)


class ClientCreateRouteSpecgrpcRouteactionTypeDef(_ClientCreateRouteSpecgrpcRouteactionTypeDef):
    """
    - **action** *(dict) --***[REQUIRED]**

      An object that represents the action to take if a match is determined.
      - **weightedTargets** *(list) --***[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.
        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a relative
          weight of 50 receives five times as much traffic as one with a relative weight of 10. The
          total weight for all targets combined must be less than or equal to 100.
          - **virtualNode** *(string) --***[REQUIRED]**

            The virtual node to associate with the weighted target.
    """


_ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef
):
    pass


_ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef(
    _ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef
):
    pass


_ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef",
    {"invert": bool, "match": ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef, "name": str},
    total=False,
)


class ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef(
    _ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef
):
    pass


_ClientCreateRouteSpecgrpcRoutematchTypeDef = TypedDict(
    "_ClientCreateRouteSpecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientCreateRouteSpecgrpcRoutematchTypeDef(_ClientCreateRouteSpecgrpcRoutematchTypeDef):
    pass


_ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef(
    _ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef
):
    pass


_RequiredClientCreateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_RequiredClientCreateRouteSpecgrpcRouteTypeDef",
    {"action": ClientCreateRouteSpecgrpcRouteactionTypeDef},
)
_OptionalClientCreateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_OptionalClientCreateRouteSpecgrpcRouteTypeDef",
    {
        "match": ClientCreateRouteSpecgrpcRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteSpecgrpcRouteTypeDef(
    _RequiredClientCreateRouteSpecgrpcRouteTypeDef, _OptionalClientCreateRouteSpecgrpcRouteTypeDef
):
    """
    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.
      - **action** *(dict) --***[REQUIRED]**

        An object that represents the action to take if a match is determined.
        - **weightedTargets** *(list) --***[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.
          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.
            - **virtualNode** *(string) --***[REQUIRED]**

              The virtual node to associate with the weighted target.
    """


_ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef(
    _ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef
):
    pass


_ClientCreateRouteSpechttp2RouteactionTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef]},
    total=False,
)


class ClientCreateRouteSpechttp2RouteactionTypeDef(_ClientCreateRouteSpechttp2RouteactionTypeDef):
    pass


_ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef
):
    pass


_ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef(
    _ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef
):
    pass


_ClientCreateRouteSpechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RoutematchheadersTypeDef",
    {"invert": bool, "match": ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef, "name": str},
    total=False,
)


class ClientCreateRouteSpechttp2RoutematchheadersTypeDef(
    _ClientCreateRouteSpechttp2RoutematchheadersTypeDef
):
    pass


_ClientCreateRouteSpechttp2RoutematchTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteSpechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientCreateRouteSpechttp2RoutematchTypeDef(_ClientCreateRouteSpechttp2RoutematchTypeDef):
    pass


_ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientCreateRouteSpechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteSpechttp2RouteretryPolicyTypeDef(
    _ClientCreateRouteSpechttp2RouteretryPolicyTypeDef
):
    pass


_ClientCreateRouteSpechttp2RouteTypeDef = TypedDict(
    "_ClientCreateRouteSpechttp2RouteTypeDef",
    {
        "action": ClientCreateRouteSpechttp2RouteactionTypeDef,
        "match": ClientCreateRouteSpechttp2RoutematchTypeDef,
        "retryPolicy": ClientCreateRouteSpechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteSpechttp2RouteTypeDef(_ClientCreateRouteSpechttp2RouteTypeDef):
    pass


_ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef
):
    pass


_ClientCreateRouteSpechttpRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef]},
    total=False,
)


class ClientCreateRouteSpechttpRouteactionTypeDef(_ClientCreateRouteSpechttpRouteactionTypeDef):
    pass


_ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef(
    _ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef
):
    pass


_ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef(
    _ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef
):
    pass


_ClientCreateRouteSpechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRoutematchheadersTypeDef",
    {"invert": bool, "match": ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef, "name": str},
    total=False,
)


class ClientCreateRouteSpechttpRoutematchheadersTypeDef(
    _ClientCreateRouteSpechttpRoutematchheadersTypeDef
):
    pass


_ClientCreateRouteSpechttpRoutematchTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteSpechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientCreateRouteSpechttpRoutematchTypeDef(_ClientCreateRouteSpechttpRoutematchTypeDef):
    pass


_ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientCreateRouteSpechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientCreateRouteSpechttpRouteretryPolicyTypeDef(
    _ClientCreateRouteSpechttpRouteretryPolicyTypeDef
):
    pass


_ClientCreateRouteSpechttpRouteTypeDef = TypedDict(
    "_ClientCreateRouteSpechttpRouteTypeDef",
    {
        "action": ClientCreateRouteSpechttpRouteactionTypeDef,
        "match": ClientCreateRouteSpechttpRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteSpechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteSpechttpRouteTypeDef(_ClientCreateRouteSpechttpRouteTypeDef):
    pass


_ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef(
    _ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef
):
    pass


_ClientCreateRouteSpectcpRouteactionTypeDef = TypedDict(
    "_ClientCreateRouteSpectcpRouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef]},
    total=False,
)


class ClientCreateRouteSpectcpRouteactionTypeDef(_ClientCreateRouteSpectcpRouteactionTypeDef):
    pass


_ClientCreateRouteSpectcpRouteTypeDef = TypedDict(
    "_ClientCreateRouteSpectcpRouteTypeDef",
    {"action": ClientCreateRouteSpectcpRouteactionTypeDef},
    total=False,
)


class ClientCreateRouteSpectcpRouteTypeDef(_ClientCreateRouteSpectcpRouteTypeDef):
    pass


_ClientCreateRouteSpecTypeDef = TypedDict(
    "_ClientCreateRouteSpecTypeDef",
    {
        "grpcRoute": ClientCreateRouteSpecgrpcRouteTypeDef,
        "http2Route": ClientCreateRouteSpechttp2RouteTypeDef,
        "httpRoute": ClientCreateRouteSpechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientCreateRouteSpectcpRouteTypeDef,
    },
    total=False,
)


class ClientCreateRouteSpecTypeDef(_ClientCreateRouteSpecTypeDef):
    """
    The route specification to apply.
    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.
      - **action** *(dict) --***[REQUIRED]**

        An object that represents the action to take if a match is determined.
        - **weightedTargets** *(list) --***[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.
          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.
            - **virtualNode** *(string) --***[REQUIRED]**

              The virtual node to associate with the weighted target.
    """


_RequiredClientCreateRouteTagsTypeDef = TypedDict(
    "_RequiredClientCreateRouteTagsTypeDef", {"key": str}
)
_OptionalClientCreateRouteTagsTypeDef = TypedDict(
    "_OptionalClientCreateRouteTagsTypeDef", {"value": str}, total=False
)


class ClientCreateRouteTagsTypeDef(
    _RequiredClientCreateRouteTagsTypeDef, _OptionalClientCreateRouteTagsTypeDef
):
    """
    - *(dict) --*

      Optional metadata that you apply to a resource to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Tag keys can have
      a maximum character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **key** *(string) --***[REQUIRED]**

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {"virtualService": ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodespecTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef
):
    pass


_ClientCreateVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientCreateVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientCreateVirtualNodeResponsevirtualNodeTypeDef(
    _ClientCreateVirtualNodeResponsevirtualNodeTypeDef
):
    """
    - **virtualNode** *(dict) --*

      The full description of your virtual node following the create call.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.
    """


_ClientCreateVirtualNodeResponseTypeDef = TypedDict(
    "_ClientCreateVirtualNodeResponseTypeDef",
    {"virtualNode": ClientCreateVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientCreateVirtualNodeResponseTypeDef(_ClientCreateVirtualNodeResponseTypeDef):
    """
    - *(dict) --*

      - **virtualNode** *(dict) --*

        The full description of your virtual node following the create call.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual node resides in.
    """


_ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef", {"virtualServiceName": str}
)


class ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef(
    _ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef
):
    """
    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.
      - **virtualServiceName** *(string) --***[REQUIRED]**

        The name of the virtual service that is acting as a virtual node backend.
    """


_ClientCreateVirtualNodeSpecbackendsTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecbackendsTypeDef",
    {"virtualService": ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef},
    total=False,
)


class ClientCreateVirtualNodeSpecbackendsTypeDef(_ClientCreateVirtualNodeSpecbackendsTypeDef):
    """
    - *(dict) --*

      An object that represents the backends that a virtual node is expected to send outbound
      traffic to.
      - **virtualService** *(dict) --*

        Specifies a virtual service to use as a backend for a virtual node.
        - **virtualServiceName** *(string) --***[REQUIRED]**

          The name of the virtual service that is acting as a virtual node backend.
    """


_ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef(
    _ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef
):
    pass


_ClientCreateVirtualNodeSpeclistenersportMappingTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientCreateVirtualNodeSpeclistenersportMappingTypeDef(
    _ClientCreateVirtualNodeSpeclistenersportMappingTypeDef
):
    pass


_ClientCreateVirtualNodeSpeclistenersTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpeclistenersTypeDef",
    {
        "healthCheck": ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef,
        "portMapping": ClientCreateVirtualNodeSpeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeSpeclistenersTypeDef(_ClientCreateVirtualNodeSpeclistenersTypeDef):
    pass


_ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef", {"path": str}, total=False
)


class ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef(
    _ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef
):
    pass


_ClientCreateVirtualNodeSpecloggingaccessLogTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecloggingaccessLogTypeDef",
    {"file": ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientCreateVirtualNodeSpecloggingaccessLogTypeDef(
    _ClientCreateVirtualNodeSpecloggingaccessLogTypeDef
):
    pass


_ClientCreateVirtualNodeSpecloggingTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecloggingTypeDef",
    {"accessLog": ClientCreateVirtualNodeSpecloggingaccessLogTypeDef},
    total=False,
)


class ClientCreateVirtualNodeSpecloggingTypeDef(_ClientCreateVirtualNodeSpecloggingTypeDef):
    pass


_ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef
):
    pass


_ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef(
    _ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef
):
    pass


_ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef", {"hostname": str}, total=False
)


class ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef(
    _ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef
):
    pass


_ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef(
    _ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef
):
    pass


_ClientCreateVirtualNodeSpecTypeDef = TypedDict(
    "_ClientCreateVirtualNodeSpecTypeDef",
    {
        "backends": List[ClientCreateVirtualNodeSpecbackendsTypeDef],
        "listeners": List[ClientCreateVirtualNodeSpeclistenersTypeDef],
        "logging": ClientCreateVirtualNodeSpecloggingTypeDef,
        "serviceDiscovery": ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientCreateVirtualNodeSpecTypeDef(_ClientCreateVirtualNodeSpecTypeDef):
    """
    The virtual node specification to apply.
    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.
      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.
        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.
          - **virtualServiceName** *(string) --***[REQUIRED]**

            The name of the virtual service that is acting as a virtual node backend.
    """


_RequiredClientCreateVirtualNodeTagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualNodeTagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualNodeTagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualNodeTagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualNodeTagsTypeDef(
    _RequiredClientCreateVirtualNodeTagsTypeDef, _OptionalClientCreateVirtualNodeTagsTypeDef
):
    """
    - *(dict) --*

      Optional metadata that you apply to a resource to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Tag keys can have
      a maximum character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **key** *(string) --***[REQUIRED]**

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    pass


_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    pass


_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef},
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    pass


_ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef
):
    pass


_ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef
):
    pass


_ClientCreateVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientCreateVirtualRouterResponsevirtualRouterTypeDef(
    _ClientCreateVirtualRouterResponsevirtualRouterTypeDef
):
    """
    - **virtualRouter** *(dict) --*

      The full description of your virtual router following the create call.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.
    """


_ClientCreateVirtualRouterResponseTypeDef = TypedDict(
    "_ClientCreateVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientCreateVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientCreateVirtualRouterResponseTypeDef(_ClientCreateVirtualRouterResponseTypeDef):
    """
    - *(dict) --*

      - **virtualRouter** *(dict) --*

        The full description of your virtual router following the create call.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual router resides in.
    """


_RequiredClientCreateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_RequiredClientCreateVirtualRouterSpeclistenersportMappingTypeDef", {"port": int}
)
_OptionalClientCreateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_OptionalClientCreateVirtualRouterSpeclistenersportMappingTypeDef",
    {"protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientCreateVirtualRouterSpeclistenersportMappingTypeDef(
    _RequiredClientCreateVirtualRouterSpeclistenersportMappingTypeDef,
    _OptionalClientCreateVirtualRouterSpeclistenersportMappingTypeDef,
):
    """
    - **portMapping** *(dict) --***[REQUIRED]**

      An object that represents a port mapping.
      - **port** *(integer) --***[REQUIRED]**

        The port used for the port mapping.
    """


_ClientCreateVirtualRouterSpeclistenersTypeDef = TypedDict(
    "_ClientCreateVirtualRouterSpeclistenersTypeDef",
    {"portMapping": ClientCreateVirtualRouterSpeclistenersportMappingTypeDef},
)


class ClientCreateVirtualRouterSpeclistenersTypeDef(_ClientCreateVirtualRouterSpeclistenersTypeDef):
    """
    - *(dict) --*

      An object that represents a virtual router listener.
      - **portMapping** *(dict) --***[REQUIRED]**

        An object that represents a port mapping.
        - **port** *(integer) --***[REQUIRED]**

          The port used for the port mapping.
    """


_ClientCreateVirtualRouterSpecTypeDef = TypedDict(
    "_ClientCreateVirtualRouterSpecTypeDef",
    {"listeners": List[ClientCreateVirtualRouterSpeclistenersTypeDef]},
    total=False,
)


class ClientCreateVirtualRouterSpecTypeDef(_ClientCreateVirtualRouterSpecTypeDef):
    """
    The virtual router specification to apply.
    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You can
      specify one listener.
      - *(dict) --*

        An object that represents a virtual router listener.
        - **portMapping** *(dict) --***[REQUIRED]**

          An object that represents a port mapping.
          - **port** *(integer) --***[REQUIRED]**

            The port used for the port mapping.
    """


_RequiredClientCreateVirtualRouterTagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualRouterTagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualRouterTagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualRouterTagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualRouterTagsTypeDef(
    _RequiredClientCreateVirtualRouterTagsTypeDef, _OptionalClientCreateVirtualRouterTagsTypeDef
):
    """
    - *(dict) --*

      Optional metadata that you apply to a resource to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Tag keys can have
      a maximum character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **key** *(string) --***[REQUIRED]**

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef
):
    pass


_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    pass


_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    pass


_ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    pass


_ClientCreateVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicespecTypeDef
):
    pass


_ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef
):
    pass


_ClientCreateVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientCreateVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientCreateVirtualServiceResponsevirtualServiceTypeDef(
    _ClientCreateVirtualServiceResponsevirtualServiceTypeDef
):
    """
    - **virtualService** *(dict) --*

      The full description of your virtual service following the create call.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.
    """


_ClientCreateVirtualServiceResponseTypeDef = TypedDict(
    "_ClientCreateVirtualServiceResponseTypeDef",
    {"virtualService": ClientCreateVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientCreateVirtualServiceResponseTypeDef(_ClientCreateVirtualServiceResponseTypeDef):
    """
    - *(dict) --*

      - **virtualService** *(dict) --*

        The full description of your virtual service following the create call.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual service resides in.
    """


_ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef", {"virtualNodeName": str}
)


class ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef(
    _ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef
):
    """
    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.
      - **virtualNodeName** *(string) --***[REQUIRED]**

        The name of the virtual node that is acting as a service provider.
    """


_ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef(
    _ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef
):
    pass


_ClientCreateVirtualServiceSpecproviderTypeDef = TypedDict(
    "_ClientCreateVirtualServiceSpecproviderTypeDef",
    {
        "virtualNode": ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientCreateVirtualServiceSpecproviderTypeDef(_ClientCreateVirtualServiceSpecproviderTypeDef):
    """
    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify a
      single virtual node or virtual router.
      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.
        - **virtualNodeName** *(string) --***[REQUIRED]**

          The name of the virtual node that is acting as a service provider.
    """


_ClientCreateVirtualServiceSpecTypeDef = TypedDict(
    "_ClientCreateVirtualServiceSpecTypeDef",
    {"provider": ClientCreateVirtualServiceSpecproviderTypeDef},
    total=False,
)


class ClientCreateVirtualServiceSpecTypeDef(_ClientCreateVirtualServiceSpecTypeDef):
    """
    The virtual service specification to apply.
    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify a
      single virtual node or virtual router.
      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.
        - **virtualNodeName** *(string) --***[REQUIRED]**

          The name of the virtual node that is acting as a service provider.
    """


_RequiredClientCreateVirtualServiceTagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualServiceTagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualServiceTagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualServiceTagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualServiceTagsTypeDef(
    _RequiredClientCreateVirtualServiceTagsTypeDef, _OptionalClientCreateVirtualServiceTagsTypeDef
):
    """
    - *(dict) --*

      Optional metadata that you apply to a resource to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Tag keys can have
      a maximum character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **key** *(string) --***[REQUIRED]**

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientDeleteMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDeleteMeshResponsemeshmetadataTypeDef(_ClientDeleteMeshResponsemeshmetadataTypeDef):
    pass


_ClientDeleteMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)


class ClientDeleteMeshResponsemeshspecegressFilterTypeDef(
    _ClientDeleteMeshResponsemeshspecegressFilterTypeDef
):
    pass


_ClientDeleteMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientDeleteMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientDeleteMeshResponsemeshspecTypeDef(_ClientDeleteMeshResponsemeshspecTypeDef):
    pass


_ClientDeleteMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDeleteMeshResponsemeshstatusTypeDef(_ClientDeleteMeshResponsemeshstatusTypeDef):
    pass


_ClientDeleteMeshResponsemeshTypeDef = TypedDict(
    "_ClientDeleteMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteMeshResponsemeshmetadataTypeDef,
        "spec": ClientDeleteMeshResponsemeshspecTypeDef,
        "status": ClientDeleteMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientDeleteMeshResponsemeshTypeDef(_ClientDeleteMeshResponsemeshTypeDef):
    """
    - **mesh** *(dict) --*

      The service mesh that was deleted.
      - **meshName** *(string) --*

        The name of the service mesh.
    """


_ClientDeleteMeshResponseTypeDef = TypedDict(
    "_ClientDeleteMeshResponseTypeDef", {"mesh": ClientDeleteMeshResponsemeshTypeDef}, total=False
)


class ClientDeleteMeshResponseTypeDef(_ClientDeleteMeshResponseTypeDef):
    """
    - *(dict) --*

      - **mesh** *(dict) --*

        The service mesh that was deleted.
        - **meshName** *(string) --*

          The name of the service mesh.
    """


_ClientDeleteRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDeleteRouteResponseroutemetadataTypeDef(_ClientDeleteRouteResponseroutemetadataTypeDef):
    pass


_ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecgrpcRouteTypeDef(
    _ClientDeleteRouteResponseroutespecgrpcRouteTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttp2RouteTypeDef(
    _ClientDeleteRouteResponseroutespechttp2RouteTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteactionTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteactionTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRoutematchTypeDef(
    _ClientDeleteRouteResponseroutespechttpRoutematchTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    pass


_ClientDeleteRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespechttpRouteTypeDef(
    _ClientDeleteRouteResponseroutespechttpRouteTypeDef
):
    pass


_ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    pass


_ClientDeleteRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteRouteResponseroutespectcpRouteactionTypeDef(
    _ClientDeleteRouteResponseroutespectcpRouteactionTypeDef
):
    pass


_ClientDeleteRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientDeleteRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientDeleteRouteResponseroutespectcpRouteTypeDef(
    _ClientDeleteRouteResponseroutespectcpRouteTypeDef
):
    pass


_ClientDeleteRouteResponseroutespecTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientDeleteRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientDeleteRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientDeleteRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientDeleteRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientDeleteRouteResponseroutespecTypeDef(_ClientDeleteRouteResponseroutespecTypeDef):
    pass


_ClientDeleteRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientDeleteRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDeleteRouteResponseroutestatusTypeDef(_ClientDeleteRouteResponseroutestatusTypeDef):
    pass


_ClientDeleteRouteResponserouteTypeDef = TypedDict(
    "_ClientDeleteRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientDeleteRouteResponseroutespecTypeDef,
        "status": ClientDeleteRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDeleteRouteResponserouteTypeDef(_ClientDeleteRouteResponserouteTypeDef):
    """
    - **route** *(dict) --*

      The route that was deleted.
      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.
    """


_ClientDeleteRouteResponseTypeDef = TypedDict(
    "_ClientDeleteRouteResponseTypeDef",
    {"route": ClientDeleteRouteResponserouteTypeDef},
    total=False,
)


class ClientDeleteRouteResponseTypeDef(_ClientDeleteRouteResponseTypeDef):
    """
    - *(dict) --*

      - **route** *(dict) --*

        The route that was deleted.
        - **meshName** *(string) --*

          The name of the service mesh that the route resides in.
    """


_ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {"virtualService": ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef
):
    pass


_ClientDeleteVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientDeleteVirtualNodeResponsevirtualNodeTypeDef(
    _ClientDeleteVirtualNodeResponsevirtualNodeTypeDef
):
    """
    - **virtualNode** *(dict) --*

      The virtual node that was deleted.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.
    """


_ClientDeleteVirtualNodeResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualNodeResponseTypeDef",
    {"virtualNode": ClientDeleteVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientDeleteVirtualNodeResponseTypeDef(_ClientDeleteVirtualNodeResponseTypeDef):
    """
    - *(dict) --*

      - **virtualNode** *(dict) --*

        The virtual node that was deleted.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual node resides in.
    """


_ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    pass


_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    pass


_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef},
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    pass


_ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef
):
    pass


_ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef
):
    pass


_ClientDeleteVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDeleteVirtualRouterResponsevirtualRouterTypeDef(
    _ClientDeleteVirtualRouterResponsevirtualRouterTypeDef
):
    """
    - **virtualRouter** *(dict) --*

      The virtual router that was deleted.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.
    """


_ClientDeleteVirtualRouterResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientDeleteVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientDeleteVirtualRouterResponseTypeDef(_ClientDeleteVirtualRouterResponseTypeDef):
    """
    - *(dict) --*

      - **virtualRouter** *(dict) --*

        The virtual router that was deleted.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual router resides in.
    """


_ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef
):
    pass


_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    pass


_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    pass


_ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    pass


_ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef
):
    pass


_ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef
):
    pass


_ClientDeleteVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientDeleteVirtualServiceResponsevirtualServiceTypeDef(
    _ClientDeleteVirtualServiceResponsevirtualServiceTypeDef
):
    """
    - **virtualService** *(dict) --*

      The virtual service that was deleted.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.
    """


_ClientDeleteVirtualServiceResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualServiceResponseTypeDef",
    {"virtualService": ClientDeleteVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientDeleteVirtualServiceResponseTypeDef(_ClientDeleteVirtualServiceResponseTypeDef):
    """
    - *(dict) --*

      - **virtualService** *(dict) --*

        The virtual service that was deleted.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual service resides in.
    """


_ClientDescribeMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDescribeMeshResponsemeshmetadataTypeDef(_ClientDescribeMeshResponsemeshmetadataTypeDef):
    pass


_ClientDescribeMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)


class ClientDescribeMeshResponsemeshspecegressFilterTypeDef(
    _ClientDescribeMeshResponsemeshspecegressFilterTypeDef
):
    pass


_ClientDescribeMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientDescribeMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientDescribeMeshResponsemeshspecTypeDef(_ClientDescribeMeshResponsemeshspecTypeDef):
    pass


_ClientDescribeMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDescribeMeshResponsemeshstatusTypeDef(_ClientDescribeMeshResponsemeshstatusTypeDef):
    pass


_ClientDescribeMeshResponsemeshTypeDef = TypedDict(
    "_ClientDescribeMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeMeshResponsemeshmetadataTypeDef,
        "spec": ClientDescribeMeshResponsemeshspecTypeDef,
        "status": ClientDescribeMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientDescribeMeshResponsemeshTypeDef(_ClientDescribeMeshResponsemeshTypeDef):
    """
    - **mesh** *(dict) --*

      The full description of your service mesh.
      - **meshName** *(string) --*

        The name of the service mesh.
    """


_ClientDescribeMeshResponseTypeDef = TypedDict(
    "_ClientDescribeMeshResponseTypeDef",
    {"mesh": ClientDescribeMeshResponsemeshTypeDef},
    total=False,
)


class ClientDescribeMeshResponseTypeDef(_ClientDescribeMeshResponseTypeDef):
    """
    - *(dict) --*

      - **mesh** *(dict) --*

        The full description of your service mesh.
        - **meshName** *(string) --*

          The name of the service mesh.
    """


_ClientDescribeRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDescribeRouteResponseroutemetadataTypeDef(
    _ClientDescribeRouteResponseroutemetadataTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecgrpcRouteTypeDef(
    _ClientDescribeRouteResponseroutespecgrpcRouteTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttp2RouteTypeDef(
    _ClientDescribeRouteResponseroutespechttp2RouteTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteactionTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteactionTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRoutematchTypeDef(
    _ClientDescribeRouteResponseroutespechttpRoutematchTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    pass


_ClientDescribeRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespechttpRouteTypeDef(
    _ClientDescribeRouteResponseroutespechttpRouteTypeDef
):
    pass


_ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    pass


_ClientDescribeRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRouteResponseroutespectcpRouteactionTypeDef(
    _ClientDescribeRouteResponseroutespectcpRouteactionTypeDef
):
    pass


_ClientDescribeRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientDescribeRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientDescribeRouteResponseroutespectcpRouteTypeDef(
    _ClientDescribeRouteResponseroutespectcpRouteTypeDef
):
    pass


_ClientDescribeRouteResponseroutespecTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientDescribeRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientDescribeRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientDescribeRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientDescribeRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientDescribeRouteResponseroutespecTypeDef(_ClientDescribeRouteResponseroutespecTypeDef):
    pass


_ClientDescribeRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientDescribeRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDescribeRouteResponseroutestatusTypeDef(_ClientDescribeRouteResponseroutestatusTypeDef):
    pass


_ClientDescribeRouteResponserouteTypeDef = TypedDict(
    "_ClientDescribeRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientDescribeRouteResponseroutespecTypeDef,
        "status": ClientDescribeRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDescribeRouteResponserouteTypeDef(_ClientDescribeRouteResponserouteTypeDef):
    """
    - **route** *(dict) --*

      The full description of your route.
      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.
    """


_ClientDescribeRouteResponseTypeDef = TypedDict(
    "_ClientDescribeRouteResponseTypeDef",
    {"route": ClientDescribeRouteResponserouteTypeDef},
    total=False,
)


class ClientDescribeRouteResponseTypeDef(_ClientDescribeRouteResponseTypeDef):
    """
    - *(dict) --*

      - **route** *(dict) --*

        The full description of your route.
        - **meshName** *(string) --*

          The name of the service mesh that the route resides in.
    """


_ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {
        "virtualService": ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef
):
    pass


_ClientDescribeVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientDescribeVirtualNodeResponsevirtualNodeTypeDef(
    _ClientDescribeVirtualNodeResponsevirtualNodeTypeDef
):
    """
    - **virtualNode** *(dict) --*

      The full description of your virtual node.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.
    """


_ClientDescribeVirtualNodeResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualNodeResponseTypeDef",
    {"virtualNode": ClientDescribeVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientDescribeVirtualNodeResponseTypeDef(_ClientDescribeVirtualNodeResponseTypeDef):
    """
    - *(dict) --*

      - **virtualNode** *(dict) --*

        The full description of your virtual node.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual node resides in.
    """


_ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    pass


_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    pass


_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {
        "portMapping": ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
    },
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    pass


_ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef
):
    pass


_ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef
):
    pass


_ClientDescribeVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientDescribeVirtualRouterResponsevirtualRouterTypeDef(
    _ClientDescribeVirtualRouterResponsevirtualRouterTypeDef
):
    """
    - **virtualRouter** *(dict) --*

      The full description of your virtual router.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.
    """


_ClientDescribeVirtualRouterResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientDescribeVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientDescribeVirtualRouterResponseTypeDef(_ClientDescribeVirtualRouterResponseTypeDef):
    """
    - *(dict) --*

      - **virtualRouter** *(dict) --*

        The full description of your virtual router.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual router resides in.
    """


_ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef
):
    pass


_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    pass


_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    pass


_ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    pass


_ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef
):
    pass


_ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef
):
    pass


_ClientDescribeVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientDescribeVirtualServiceResponsevirtualServiceTypeDef(
    _ClientDescribeVirtualServiceResponsevirtualServiceTypeDef
):
    """
    - **virtualService** *(dict) --*

      The full description of your virtual service.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.
    """


_ClientDescribeVirtualServiceResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualServiceResponseTypeDef",
    {"virtualService": ClientDescribeVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientDescribeVirtualServiceResponseTypeDef(_ClientDescribeVirtualServiceResponseTypeDef):
    """
    - *(dict) --*

      - **virtualService** *(dict) --*

        The full description of your virtual service.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual service resides in.
    """


_ClientListMeshesResponsemeshesTypeDef = TypedDict(
    "_ClientListMeshesResponsemeshesTypeDef", {"arn": str, "meshName": str}, total=False
)


class ClientListMeshesResponsemeshesTypeDef(_ClientListMeshesResponsemeshesTypeDef):
    """
    - *(dict) --*

      An object that represents a service mesh returned by a list operation.
      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) of the service mesh.
    """


_ClientListMeshesResponseTypeDef = TypedDict(
    "_ClientListMeshesResponseTypeDef",
    {"meshes": List[ClientListMeshesResponsemeshesTypeDef], "nextToken": str},
    total=False,
)


class ClientListMeshesResponseTypeDef(_ClientListMeshesResponseTypeDef):
    """
    - *(dict) --*

      - **meshes** *(list) --*

        The list of existing service meshes.
        - *(dict) --*

          An object that represents a service mesh returned by a list operation.
          - **arn** *(string) --*

            The full Amazon Resource Name (ARN) of the service mesh.
    """


_ClientListRoutesResponseroutesTypeDef = TypedDict(
    "_ClientListRoutesResponseroutesTypeDef",
    {"arn": str, "meshName": str, "routeName": str, "virtualRouterName": str},
    total=False,
)


class ClientListRoutesResponseroutesTypeDef(_ClientListRoutesResponseroutesTypeDef):
    pass


_ClientListRoutesResponseTypeDef = TypedDict(
    "_ClientListRoutesResponseTypeDef",
    {"nextToken": str, "routes": List[ClientListRoutesResponseroutesTypeDef]},
    total=False,
)


class ClientListRoutesResponseTypeDef(_ClientListRoutesResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        The ``nextToken`` value to include in a future ``ListRoutes`` request. When the results of a
        ``ListRoutes`` request exceed ``limit`` , you can use this value to retrieve the next page
        of results. This value is ``null`` when there are no more results to return.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    pass


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"nextToken": str, "tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        The ``nextToken`` value to include in a future ``ListTagsForResource`` request. When the
        results of a ``ListTagsForResource`` request exceed ``limit`` , you can use this value to
        retrieve the next page of results. This value is ``null`` when there are no more results to
        return.
    """


_ClientListVirtualNodesResponsevirtualNodesTypeDef = TypedDict(
    "_ClientListVirtualNodesResponsevirtualNodesTypeDef",
    {"arn": str, "meshName": str, "virtualNodeName": str},
    total=False,
)


class ClientListVirtualNodesResponsevirtualNodesTypeDef(
    _ClientListVirtualNodesResponsevirtualNodesTypeDef
):
    pass


_ClientListVirtualNodesResponseTypeDef = TypedDict(
    "_ClientListVirtualNodesResponseTypeDef",
    {"nextToken": str, "virtualNodes": List[ClientListVirtualNodesResponsevirtualNodesTypeDef]},
    total=False,
)


class ClientListVirtualNodesResponseTypeDef(_ClientListVirtualNodesResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        The ``nextToken`` value to include in a future ``ListVirtualNodes`` request. When the
        results of a ``ListVirtualNodes`` request exceed ``limit`` , you can use this value to
        retrieve the next page of results. This value is ``null`` when there are no more results to
        return.
    """


_ClientListVirtualRoutersResponsevirtualRoutersTypeDef = TypedDict(
    "_ClientListVirtualRoutersResponsevirtualRoutersTypeDef",
    {"arn": str, "meshName": str, "virtualRouterName": str},
    total=False,
)


class ClientListVirtualRoutersResponsevirtualRoutersTypeDef(
    _ClientListVirtualRoutersResponsevirtualRoutersTypeDef
):
    pass


_ClientListVirtualRoutersResponseTypeDef = TypedDict(
    "_ClientListVirtualRoutersResponseTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List[ClientListVirtualRoutersResponsevirtualRoutersTypeDef],
    },
    total=False,
)


class ClientListVirtualRoutersResponseTypeDef(_ClientListVirtualRoutersResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        The ``nextToken`` value to include in a future ``ListVirtualRouters`` request. When the
        results of a ``ListVirtualRouters`` request exceed ``limit`` , you can use this value to
        retrieve the next page of results. This value is ``null`` when there are no more results to
        return.
    """


_ClientListVirtualServicesResponsevirtualServicesTypeDef = TypedDict(
    "_ClientListVirtualServicesResponsevirtualServicesTypeDef",
    {"arn": str, "meshName": str, "virtualServiceName": str},
    total=False,
)


class ClientListVirtualServicesResponsevirtualServicesTypeDef(
    _ClientListVirtualServicesResponsevirtualServicesTypeDef
):
    pass


_ClientListVirtualServicesResponseTypeDef = TypedDict(
    "_ClientListVirtualServicesResponseTypeDef",
    {
        "nextToken": str,
        "virtualServices": List[ClientListVirtualServicesResponsevirtualServicesTypeDef],
    },
    total=False,
)


class ClientListVirtualServicesResponseTypeDef(_ClientListVirtualServicesResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        The ``nextToken`` value to include in a future ``ListVirtualServices`` request. When the
        results of a ``ListVirtualServices`` request exceed ``limit`` , you can use this value to
        retrieve the next page of results. This value is ``null`` when there are no more results to
        return.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      Optional metadata that you apply to a resource to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Tag keys can have
      a maximum character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **key** *(string) --***[REQUIRED]**

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientUpdateMeshResponsemeshmetadataTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientUpdateMeshResponsemeshmetadataTypeDef(_ClientUpdateMeshResponsemeshmetadataTypeDef):
    pass


_ClientUpdateMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)


class ClientUpdateMeshResponsemeshspecegressFilterTypeDef(
    _ClientUpdateMeshResponsemeshspecegressFilterTypeDef
):
    pass


_ClientUpdateMeshResponsemeshspecTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientUpdateMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)


class ClientUpdateMeshResponsemeshspecTypeDef(_ClientUpdateMeshResponsemeshspecTypeDef):
    pass


_ClientUpdateMeshResponsemeshstatusTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientUpdateMeshResponsemeshstatusTypeDef(_ClientUpdateMeshResponsemeshstatusTypeDef):
    pass


_ClientUpdateMeshResponsemeshTypeDef = TypedDict(
    "_ClientUpdateMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateMeshResponsemeshmetadataTypeDef,
        "spec": ClientUpdateMeshResponsemeshspecTypeDef,
        "status": ClientUpdateMeshResponsemeshstatusTypeDef,
    },
    total=False,
)


class ClientUpdateMeshResponsemeshTypeDef(_ClientUpdateMeshResponsemeshTypeDef):
    """
    - **mesh** *(dict) --*

      An object that represents a service mesh returned by a describe operation.
      - **meshName** *(string) --*

        The name of the service mesh.
    """


_ClientUpdateMeshResponseTypeDef = TypedDict(
    "_ClientUpdateMeshResponseTypeDef", {"mesh": ClientUpdateMeshResponsemeshTypeDef}, total=False
)


class ClientUpdateMeshResponseTypeDef(_ClientUpdateMeshResponseTypeDef):
    """
    - *(dict) --*

      - **mesh** *(dict) --*

        An object that represents a service mesh returned by a describe operation.
        - **meshName** *(string) --*

          The name of the service mesh.
    """


_ClientUpdateMeshSpecegressFilterTypeDef = TypedDict(
    "_ClientUpdateMeshSpecegressFilterTypeDef", {"type": Literal["ALLOW_ALL", "DROP_ALL"]}
)


class ClientUpdateMeshSpecegressFilterTypeDef(_ClientUpdateMeshSpecegressFilterTypeDef):
    """
    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.
      - **type** *(string) --***[REQUIRED]**

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
        virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
        to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientUpdateMeshSpecTypeDef = TypedDict(
    "_ClientUpdateMeshSpecTypeDef",
    {"egressFilter": ClientUpdateMeshSpecegressFilterTypeDef},
    total=False,
)


class ClientUpdateMeshSpecTypeDef(_ClientUpdateMeshSpecTypeDef):
    """
    The service mesh specification to apply.
    - **egressFilter** *(dict) --*

      The egress filter rules for the service mesh.
      - **type** *(string) --***[REQUIRED]**

        The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
        virtual nodes to other defined resources in the service mesh (and any traffic to
        ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
        to allow egress to any endpoint inside or outside of the service mesh.
    """


_ClientUpdateRouteResponseroutemetadataTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientUpdateRouteResponseroutemetadataTypeDef(_ClientUpdateRouteResponseroutemetadataTypeDef):
    pass


_ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecgrpcRouteTypeDef(
    _ClientUpdateRouteResponseroutespecgrpcRouteTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttp2RouteTypeDef(
    _ClientUpdateRouteResponseroutespechttp2RouteTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteactionTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteactionTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRoutematchTypeDef(
    _ClientUpdateRouteResponseroutespechttpRoutematchTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef
):
    pass


_ClientUpdateRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespechttpRouteTypeDef(
    _ClientUpdateRouteResponseroutespechttpRouteTypeDef
):
    pass


_ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
):
    pass


_ClientUpdateRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateRouteResponseroutespectcpRouteactionTypeDef(
    _ClientUpdateRouteResponseroutespectcpRouteactionTypeDef
):
    pass


_ClientUpdateRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientUpdateRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)


class ClientUpdateRouteResponseroutespectcpRouteTypeDef(
    _ClientUpdateRouteResponseroutespectcpRouteTypeDef
):
    pass


_ClientUpdateRouteResponseroutespecTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientUpdateRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientUpdateRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientUpdateRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientUpdateRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)


class ClientUpdateRouteResponseroutespecTypeDef(_ClientUpdateRouteResponseroutespecTypeDef):
    pass


_ClientUpdateRouteResponseroutestatusTypeDef = TypedDict(
    "_ClientUpdateRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientUpdateRouteResponseroutestatusTypeDef(_ClientUpdateRouteResponseroutestatusTypeDef):
    pass


_ClientUpdateRouteResponserouteTypeDef = TypedDict(
    "_ClientUpdateRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientUpdateRouteResponseroutespecTypeDef,
        "status": ClientUpdateRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientUpdateRouteResponserouteTypeDef(_ClientUpdateRouteResponserouteTypeDef):
    """
    - **route** *(dict) --*

      A full description of the route that was updated.
      - **meshName** *(string) --*

        The name of the service mesh that the route resides in.
    """


_ClientUpdateRouteResponseTypeDef = TypedDict(
    "_ClientUpdateRouteResponseTypeDef",
    {"route": ClientUpdateRouteResponserouteTypeDef},
    total=False,
)


class ClientUpdateRouteResponseTypeDef(_ClientUpdateRouteResponseTypeDef):
    """
    - *(dict) --*

      - **route** *(dict) --*

        A full description of the route that was updated.
        - **meshName** *(string) --*

          The name of the service mesh that the route resides in.
    """


_RequiredClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_RequiredClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef", {"virtualNode": str}
)
_OptionalClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_OptionalClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    {"weight": int},
    total=False,
)


class ClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef(
    _RequiredClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
    _OptionalClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
):
    """
    - *(dict) --*

      An object that represents a target and its relative weight. Traffic is distributed across
      targets according to their relative weight. For example, a weighted target with a relative
      weight of 50 receives five times as much traffic as one with a relative weight of 10. The
      total weight for all targets combined must be less than or equal to 100.
      - **virtualNode** *(string) --***[REQUIRED]**

        The virtual node to associate with the weighted target.
    """


_ClientUpdateRouteSpecgrpcRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteSpecgrpcRouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef]},
)


class ClientUpdateRouteSpecgrpcRouteactionTypeDef(_ClientUpdateRouteSpecgrpcRouteactionTypeDef):
    """
    - **action** *(dict) --***[REQUIRED]**

      An object that represents the action to take if a match is determined.
      - **weightedTargets** *(list) --***[REQUIRED]**

        An object that represents the targets that traffic is routed to when a request matches the
        route.
        - *(dict) --*

          An object that represents a target and its relative weight. Traffic is distributed across
          targets according to their relative weight. For example, a weighted target with a relative
          weight of 50 receives five times as much traffic as one with a relative weight of 10. The
          total weight for all targets combined must be less than or equal to 100.
          - **virtualNode** *(string) --***[REQUIRED]**

            The virtual node to associate with the weighted target.
    """


_ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef(
    _ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef
):
    pass


_ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "_ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef(
    _ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef
):
    pass


_ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef = TypedDict(
    "_ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef",
    {"invert": bool, "match": ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef, "name": str},
    total=False,
)


class ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef(
    _ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef
):
    pass


_ClientUpdateRouteSpecgrpcRoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteSpecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientUpdateRouteSpecgrpcRoutematchTypeDef(_ClientUpdateRouteSpecgrpcRoutematchTypeDef):
    pass


_ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef(
    _ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef
):
    pass


_RequiredClientUpdateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_RequiredClientUpdateRouteSpecgrpcRouteTypeDef",
    {"action": ClientUpdateRouteSpecgrpcRouteactionTypeDef},
)
_OptionalClientUpdateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_OptionalClientUpdateRouteSpecgrpcRouteTypeDef",
    {
        "match": ClientUpdateRouteSpecgrpcRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteSpecgrpcRouteTypeDef(
    _RequiredClientUpdateRouteSpecgrpcRouteTypeDef, _OptionalClientUpdateRouteSpecgrpcRouteTypeDef
):
    """
    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.
      - **action** *(dict) --***[REQUIRED]**

        An object that represents the action to take if a match is determined.
        - **weightedTargets** *(list) --***[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.
          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.
            - **virtualNode** *(string) --***[REQUIRED]**

              The virtual node to associate with the weighted target.
    """


_ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef
):
    pass


_ClientUpdateRouteSpechttp2RouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef]},
    total=False,
)


class ClientUpdateRouteSpechttp2RouteactionTypeDef(_ClientUpdateRouteSpechttp2RouteactionTypeDef):
    pass


_ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef
):
    pass


_ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef(
    _ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef
):
    pass


_ClientUpdateRouteSpechttp2RoutematchheadersTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RoutematchheadersTypeDef",
    {"invert": bool, "match": ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef, "name": str},
    total=False,
)


class ClientUpdateRouteSpechttp2RoutematchheadersTypeDef(
    _ClientUpdateRouteSpechttp2RoutematchheadersTypeDef
):
    pass


_ClientUpdateRouteSpechttp2RoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteSpechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientUpdateRouteSpechttp2RoutematchTypeDef(_ClientUpdateRouteSpechttp2RoutematchTypeDef):
    pass


_ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef(
    _ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef
):
    pass


_ClientUpdateRouteSpechttp2RouteTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttp2RouteTypeDef",
    {
        "action": ClientUpdateRouteSpechttp2RouteactionTypeDef,
        "match": ClientUpdateRouteSpechttp2RoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteSpechttp2RouteTypeDef(_ClientUpdateRouteSpechttp2RouteTypeDef):
    pass


_ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef
):
    pass


_ClientUpdateRouteSpechttpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef]},
    total=False,
)


class ClientUpdateRouteSpechttpRouteactionTypeDef(_ClientUpdateRouteSpechttpRouteactionTypeDef):
    pass


_ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)


class ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef(
    _ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef
):
    pass


_ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)


class ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef(
    _ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef
):
    pass


_ClientUpdateRouteSpechttpRoutematchheadersTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRoutematchheadersTypeDef",
    {"invert": bool, "match": ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef, "name": str},
    total=False,
)


class ClientUpdateRouteSpechttpRoutematchheadersTypeDef(
    _ClientUpdateRouteSpechttpRoutematchheadersTypeDef
):
    pass


_ClientUpdateRouteSpechttpRoutematchTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteSpechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class ClientUpdateRouteSpechttpRoutematchTypeDef(_ClientUpdateRouteSpechttpRoutematchTypeDef):
    pass


_ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)


class ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef(
    _ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef
):
    pass


_ClientUpdateRouteSpechttpRouteretryPolicyTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)


class ClientUpdateRouteSpechttpRouteretryPolicyTypeDef(
    _ClientUpdateRouteSpechttpRouteretryPolicyTypeDef
):
    pass


_ClientUpdateRouteSpechttpRouteTypeDef = TypedDict(
    "_ClientUpdateRouteSpechttpRouteTypeDef",
    {
        "action": ClientUpdateRouteSpechttpRouteactionTypeDef,
        "match": ClientUpdateRouteSpechttpRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteSpechttpRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteSpechttpRouteTypeDef(_ClientUpdateRouteSpechttpRouteTypeDef):
    pass


_ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "_ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)


class ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef(
    _ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef
):
    pass


_ClientUpdateRouteSpectcpRouteactionTypeDef = TypedDict(
    "_ClientUpdateRouteSpectcpRouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef]},
    total=False,
)


class ClientUpdateRouteSpectcpRouteactionTypeDef(_ClientUpdateRouteSpectcpRouteactionTypeDef):
    pass


_ClientUpdateRouteSpectcpRouteTypeDef = TypedDict(
    "_ClientUpdateRouteSpectcpRouteTypeDef",
    {"action": ClientUpdateRouteSpectcpRouteactionTypeDef},
    total=False,
)


class ClientUpdateRouteSpectcpRouteTypeDef(_ClientUpdateRouteSpectcpRouteTypeDef):
    pass


_ClientUpdateRouteSpecTypeDef = TypedDict(
    "_ClientUpdateRouteSpecTypeDef",
    {
        "grpcRoute": ClientUpdateRouteSpecgrpcRouteTypeDef,
        "http2Route": ClientUpdateRouteSpechttp2RouteTypeDef,
        "httpRoute": ClientUpdateRouteSpechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientUpdateRouteSpectcpRouteTypeDef,
    },
    total=False,
)


class ClientUpdateRouteSpecTypeDef(_ClientUpdateRouteSpecTypeDef):
    """
    The new route specification to apply. This overwrites the existing data.
    - **grpcRoute** *(dict) --*

      An object that represents the specification of a GRPC route.
      - **action** *(dict) --***[REQUIRED]**

        An object that represents the action to take if a match is determined.
        - **weightedTargets** *(list) --***[REQUIRED]**

          An object that represents the targets that traffic is routed to when a request matches the
          route.
          - *(dict) --*

            An object that represents a target and its relative weight. Traffic is distributed
            across targets according to their relative weight. For example, a weighted target with a
            relative weight of 50 receives five times as much traffic as one with a relative weight
            of 10. The total weight for all targets combined must be less than or equal to 100.
            - **virtualNode** *(string) --***[REQUIRED]**

              The virtual node to associate with the weighted target.
    """


_ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {"virtualService": ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef
):
    pass


_ClientUpdateVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)


class ClientUpdateVirtualNodeResponsevirtualNodeTypeDef(
    _ClientUpdateVirtualNodeResponsevirtualNodeTypeDef
):
    """
    - **virtualNode** *(dict) --*

      A full description of the virtual node that was updated.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual node resides in.
    """


_ClientUpdateVirtualNodeResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeResponseTypeDef",
    {"virtualNode": ClientUpdateVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeResponseTypeDef(_ClientUpdateVirtualNodeResponseTypeDef):
    """
    - *(dict) --*

      - **virtualNode** *(dict) --*

        A full description of the virtual node that was updated.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual node resides in.
    """


_ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef", {"virtualServiceName": str}
)


class ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef(
    _ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef
):
    """
    - **virtualService** *(dict) --*

      Specifies a virtual service to use as a backend for a virtual node.
      - **virtualServiceName** *(string) --***[REQUIRED]**

        The name of the virtual service that is acting as a virtual node backend.
    """


_ClientUpdateVirtualNodeSpecbackendsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecbackendsTypeDef",
    {"virtualService": ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeSpecbackendsTypeDef(_ClientUpdateVirtualNodeSpecbackendsTypeDef):
    """
    - *(dict) --*

      An object that represents the backends that a virtual node is expected to send outbound
      traffic to.
      - **virtualService** *(dict) --*

        Specifies a virtual service to use as a backend for a virtual node.
        - **virtualServiceName** *(string) --***[REQUIRED]**

          The name of the virtual service that is acting as a virtual node backend.
    """


_ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)


class ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef(
    _ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef
):
    pass


_ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef(
    _ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef
):
    pass


_ClientUpdateVirtualNodeSpeclistenersTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpeclistenersTypeDef",
    {
        "healthCheck": ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef,
        "portMapping": ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeSpeclistenersTypeDef(_ClientUpdateVirtualNodeSpeclistenersTypeDef):
    pass


_ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef", {"path": str}, total=False
)


class ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef(
    _ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef
):
    pass


_ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef",
    {"file": ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef(
    _ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef
):
    pass


_ClientUpdateVirtualNodeSpecloggingTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecloggingTypeDef",
    {"accessLog": ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef},
    total=False,
)


class ClientUpdateVirtualNodeSpecloggingTypeDef(_ClientUpdateVirtualNodeSpecloggingTypeDef):
    pass


_ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef(
    _ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef
):
    pass


_ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)


class ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef(
    _ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef
):
    pass


_ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef", {"hostname": str}, total=False
)


class ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef(
    _ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef
):
    pass


_ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef(
    _ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef
):
    pass


_ClientUpdateVirtualNodeSpecTypeDef = TypedDict(
    "_ClientUpdateVirtualNodeSpecTypeDef",
    {
        "backends": List[ClientUpdateVirtualNodeSpecbackendsTypeDef],
        "listeners": List[ClientUpdateVirtualNodeSpeclistenersTypeDef],
        "logging": ClientUpdateVirtualNodeSpecloggingTypeDef,
        "serviceDiscovery": ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualNodeSpecTypeDef(_ClientUpdateVirtualNodeSpecTypeDef):
    """
    The new virtual node specification to apply. This overwrites the existing data.
    - **backends** *(list) --*

      The backends that the virtual node is expected to send outbound traffic to.
      - *(dict) --*

        An object that represents the backends that a virtual node is expected to send outbound
        traffic to.
        - **virtualService** *(dict) --*

          Specifies a virtual service to use as a backend for a virtual node.
          - **virtualServiceName** *(string) --***[REQUIRED]**

            The name of the virtual service that is acting as a virtual node backend.
    """


_ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef
):
    pass


_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
):
    pass


_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef},
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef
):
    pass


_ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef
):
    pass


_ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef
):
    pass


_ClientUpdateVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)


class ClientUpdateVirtualRouterResponsevirtualRouterTypeDef(
    _ClientUpdateVirtualRouterResponsevirtualRouterTypeDef
):
    """
    - **virtualRouter** *(dict) --*

      A full description of the virtual router that was updated.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual router resides in.
    """


_ClientUpdateVirtualRouterResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientUpdateVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)


class ClientUpdateVirtualRouterResponseTypeDef(_ClientUpdateVirtualRouterResponseTypeDef):
    """
    - *(dict) --*

      - **virtualRouter** *(dict) --*

        A full description of the virtual router that was updated.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual router resides in.
    """


_RequiredClientUpdateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_RequiredClientUpdateVirtualRouterSpeclistenersportMappingTypeDef", {"port": int}
)
_OptionalClientUpdateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_OptionalClientUpdateVirtualRouterSpeclistenersportMappingTypeDef",
    {"protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientUpdateVirtualRouterSpeclistenersportMappingTypeDef(
    _RequiredClientUpdateVirtualRouterSpeclistenersportMappingTypeDef,
    _OptionalClientUpdateVirtualRouterSpeclistenersportMappingTypeDef,
):
    """
    - **portMapping** *(dict) --***[REQUIRED]**

      An object that represents a port mapping.
      - **port** *(integer) --***[REQUIRED]**

        The port used for the port mapping.
    """


_ClientUpdateVirtualRouterSpeclistenersTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterSpeclistenersTypeDef",
    {"portMapping": ClientUpdateVirtualRouterSpeclistenersportMappingTypeDef},
)


class ClientUpdateVirtualRouterSpeclistenersTypeDef(_ClientUpdateVirtualRouterSpeclistenersTypeDef):
    """
    - *(dict) --*

      An object that represents a virtual router listener.
      - **portMapping** *(dict) --***[REQUIRED]**

        An object that represents a port mapping.
        - **port** *(integer) --***[REQUIRED]**

          The port used for the port mapping.
    """


_ClientUpdateVirtualRouterSpecTypeDef = TypedDict(
    "_ClientUpdateVirtualRouterSpecTypeDef",
    {"listeners": List[ClientUpdateVirtualRouterSpeclistenersTypeDef]},
    total=False,
)


class ClientUpdateVirtualRouterSpecTypeDef(_ClientUpdateVirtualRouterSpecTypeDef):
    """
    The new virtual router specification to apply. This overwrites the existing data.
    - **listeners** *(list) --*

      The listeners that the virtual router is expected to receive inbound traffic from. You can
      specify one listener.
      - *(dict) --*

        An object that represents a virtual router listener.
        - **portMapping** *(dict) --***[REQUIRED]**

          An object that represents a port mapping.
          - **port** *(integer) --***[REQUIRED]**

            The port used for the port mapping.
    """


_ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef
):
    pass


_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef
):
    pass


_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef
):
    pass


_ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef
):
    pass


_ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef
):
    pass


_ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef
):
    pass


_ClientUpdateVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)


class ClientUpdateVirtualServiceResponsevirtualServiceTypeDef(
    _ClientUpdateVirtualServiceResponsevirtualServiceTypeDef
):
    """
    - **virtualService** *(dict) --*

      A full description of the virtual service that was updated.
      - **meshName** *(string) --*

        The name of the service mesh that the virtual service resides in.
    """


_ClientUpdateVirtualServiceResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceResponseTypeDef",
    {"virtualService": ClientUpdateVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)


class ClientUpdateVirtualServiceResponseTypeDef(_ClientUpdateVirtualServiceResponseTypeDef):
    """
    - *(dict) --*

      - **virtualService** *(dict) --*

        A full description of the virtual service that was updated.
        - **meshName** *(string) --*

          The name of the service mesh that the virtual service resides in.
    """


_ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef", {"virtualNodeName": str}
)


class ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef(
    _ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef
):
    """
    - **virtualNode** *(dict) --*

      The virtual node associated with a virtual service.
      - **virtualNodeName** *(string) --***[REQUIRED]**

        The name of the virtual node that is acting as a service provider.
    """


_ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)


class ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef(
    _ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef
):
    pass


_ClientUpdateVirtualServiceSpecproviderTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceSpecproviderTypeDef",
    {
        "virtualNode": ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef,
    },
    total=False,
)


class ClientUpdateVirtualServiceSpecproviderTypeDef(_ClientUpdateVirtualServiceSpecproviderTypeDef):
    """
    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify a
      single virtual node or virtual router.
      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.
        - **virtualNodeName** *(string) --***[REQUIRED]**

          The name of the virtual node that is acting as a service provider.
    """


_ClientUpdateVirtualServiceSpecTypeDef = TypedDict(
    "_ClientUpdateVirtualServiceSpecTypeDef",
    {"provider": ClientUpdateVirtualServiceSpecproviderTypeDef},
    total=False,
)


class ClientUpdateVirtualServiceSpecTypeDef(_ClientUpdateVirtualServiceSpecTypeDef):
    """
    The new virtual service specification to apply. This overwrites the existing data.
    - **provider** *(dict) --*

      The App Mesh object that is acting as the provider for a virtual service. You can specify a
      single virtual node or virtual router.
      - **virtualNode** *(dict) --*

        The virtual node associated with a virtual service.
        - **virtualNodeName** *(string) --***[REQUIRED]**

          The name of the virtual node that is acting as a service provider.
    """


_ListMeshesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMeshesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMeshesPaginatePaginationConfigTypeDef(_ListMeshesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMeshesPaginateResponsemeshesTypeDef = TypedDict(
    "_ListMeshesPaginateResponsemeshesTypeDef", {"arn": str, "meshName": str}, total=False
)


class ListMeshesPaginateResponsemeshesTypeDef(_ListMeshesPaginateResponsemeshesTypeDef):
    """
    - *(dict) --*

      An object that represents a service mesh returned by a list operation.
      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) of the service mesh.
    """


_ListMeshesPaginateResponseTypeDef = TypedDict(
    "_ListMeshesPaginateResponseTypeDef",
    {"meshes": List[ListMeshesPaginateResponsemeshesTypeDef], "NextToken": str},
    total=False,
)


class ListMeshesPaginateResponseTypeDef(_ListMeshesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **meshes** *(list) --*

        The list of existing service meshes.
        - *(dict) --*

          An object that represents a service mesh returned by a list operation.
          - **arn** *(string) --*

            The full Amazon Resource Name (ARN) of the service mesh.
    """


_ListRoutesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRoutesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRoutesPaginatePaginationConfigTypeDef(_ListRoutesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRoutesPaginateResponseroutesTypeDef = TypedDict(
    "_ListRoutesPaginateResponseroutesTypeDef",
    {"arn": str, "meshName": str, "routeName": str, "virtualRouterName": str},
    total=False,
)


class ListRoutesPaginateResponseroutesTypeDef(_ListRoutesPaginateResponseroutesTypeDef):
    """
    - *(dict) --*

      An object that represents a route returned by a list operation.
      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the route.
    """


_ListRoutesPaginateResponseTypeDef = TypedDict(
    "_ListRoutesPaginateResponseTypeDef",
    {"routes": List[ListRoutesPaginateResponseroutesTypeDef], "NextToken": str},
    total=False,
)


class ListRoutesPaginateResponseTypeDef(_ListRoutesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **routes** *(list) --*

        The list of existing routes for the specified service mesh and virtual router.
        - *(dict) --*

          An object that represents a route returned by a list operation.
          - **arn** *(string) --*

            The full Amazon Resource Name (ARN) for the route.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    - *(dict) --*

      Optional metadata that you apply to a resource to assist with categorization and organization.
      Each tag consists of a key and an optional value, both of which you define. Tag keys can have
      a maximum character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The tags for the resource.
        - *(dict) --*

          Optional metadata that you apply to a resource to assist with categorization and
          organization. Each tag consists of a key and an optional value, both of which you define.
          Tag keys can have a maximum character length of 128 characters, and tag values can have a
          maximum length of 256 characters.
          - **key** *(string) --*

            One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
            like a category for more specific tag values.
    """


_ListVirtualNodesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualNodesPaginatePaginationConfigTypeDef(
    _ListVirtualNodesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVirtualNodesPaginateResponsevirtualNodesTypeDef = TypedDict(
    "_ListVirtualNodesPaginateResponsevirtualNodesTypeDef",
    {"arn": str, "meshName": str, "virtualNodeName": str},
    total=False,
)


class ListVirtualNodesPaginateResponsevirtualNodesTypeDef(
    _ListVirtualNodesPaginateResponsevirtualNodesTypeDef
):
    """
    - *(dict) --*

      An object that represents a virtual node returned by a list operation.
      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the virtual node.
    """


_ListVirtualNodesPaginateResponseTypeDef = TypedDict(
    "_ListVirtualNodesPaginateResponseTypeDef",
    {"virtualNodes": List[ListVirtualNodesPaginateResponsevirtualNodesTypeDef], "NextToken": str},
    total=False,
)


class ListVirtualNodesPaginateResponseTypeDef(_ListVirtualNodesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **virtualNodes** *(list) --*

        The list of existing virtual nodes for the specified service mesh.
        - *(dict) --*

          An object that represents a virtual node returned by a list operation.
          - **arn** *(string) --*

            The full Amazon Resource Name (ARN) for the virtual node.
    """


_ListVirtualRoutersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualRoutersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualRoutersPaginatePaginationConfigTypeDef(
    _ListVirtualRoutersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef = TypedDict(
    "_ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef",
    {"arn": str, "meshName": str, "virtualRouterName": str},
    total=False,
)


class ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef(
    _ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef
):
    """
    - *(dict) --*

      An object that represents a virtual router returned by a list operation.
      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the virtual router.
    """


_ListVirtualRoutersPaginateResponseTypeDef = TypedDict(
    "_ListVirtualRoutersPaginateResponseTypeDef",
    {
        "virtualRouters": List[ListVirtualRoutersPaginateResponsevirtualRoutersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListVirtualRoutersPaginateResponseTypeDef(_ListVirtualRoutersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **virtualRouters** *(list) --*

        The list of existing virtual routers for the specified service mesh.
        - *(dict) --*

          An object that represents a virtual router returned by a list operation.
          - **arn** *(string) --*

            The full Amazon Resource Name (ARN) for the virtual router.
    """


_ListVirtualServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualServicesPaginatePaginationConfigTypeDef(
    _ListVirtualServicesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVirtualServicesPaginateResponsevirtualServicesTypeDef = TypedDict(
    "_ListVirtualServicesPaginateResponsevirtualServicesTypeDef",
    {"arn": str, "meshName": str, "virtualServiceName": str},
    total=False,
)


class ListVirtualServicesPaginateResponsevirtualServicesTypeDef(
    _ListVirtualServicesPaginateResponsevirtualServicesTypeDef
):
    """
    - *(dict) --*

      An object that represents a virtual service returned by a list operation.
      - **arn** *(string) --*

        The full Amazon Resource Name (ARN) for the virtual service.
    """


_ListVirtualServicesPaginateResponseTypeDef = TypedDict(
    "_ListVirtualServicesPaginateResponseTypeDef",
    {
        "virtualServices": List[ListVirtualServicesPaginateResponsevirtualServicesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListVirtualServicesPaginateResponseTypeDef(_ListVirtualServicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **virtualServices** *(list) --*

        The list of existing virtual services for the specified service mesh.
        - *(dict) --*

          An object that represents a virtual service returned by a list operation.
          - **arn** *(string) --*

            The full Amazon Resource Name (ARN) for the virtual service.
    """
