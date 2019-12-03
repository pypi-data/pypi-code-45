"Main interface for eks service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateClusterLoggingclusterLoggingTypeDef",
    "ClientCreateClusterLoggingTypeDef",
    "ClientCreateClusterResourcesVpcConfigTypeDef",
    "ClientCreateClusterResponseclustercertificateAuthorityTypeDef",
    "ClientCreateClusterResponseclusteridentityoidcTypeDef",
    "ClientCreateClusterResponseclusteridentityTypeDef",
    "ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientCreateClusterResponseclusterloggingTypeDef",
    "ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientCreateClusterResponseclusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef",
    "ClientCreateFargateProfileResponsefargateProfileTypeDef",
    "ClientCreateFargateProfileResponseTypeDef",
    "ClientCreateFargateProfileSelectorsTypeDef",
    "ClientCreateNodegroupRemoteAccessTypeDef",
    "ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientCreateNodegroupResponsenodegrouphealthTypeDef",
    "ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientCreateNodegroupResponsenodegroupresourcesTypeDef",
    "ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientCreateNodegroupResponsenodegroupTypeDef",
    "ClientCreateNodegroupResponseTypeDef",
    "ClientCreateNodegroupScalingConfigTypeDef",
    "ClientDeleteClusterResponseclustercertificateAuthorityTypeDef",
    "ClientDeleteClusterResponseclusteridentityoidcTypeDef",
    "ClientDeleteClusterResponseclusteridentityTypeDef",
    "ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientDeleteClusterResponseclusterloggingTypeDef",
    "ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientDeleteClusterResponseclusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef",
    "ClientDeleteFargateProfileResponsefargateProfileTypeDef",
    "ClientDeleteFargateProfileResponseTypeDef",
    "ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientDeleteNodegroupResponsenodegrouphealthTypeDef",
    "ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientDeleteNodegroupResponsenodegroupresourcesTypeDef",
    "ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientDeleteNodegroupResponsenodegroupTypeDef",
    "ClientDeleteNodegroupResponseTypeDef",
    "ClientDescribeClusterResponseclustercertificateAuthorityTypeDef",
    "ClientDescribeClusterResponseclusteridentityoidcTypeDef",
    "ClientDescribeClusterResponseclusteridentityTypeDef",
    "ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientDescribeClusterResponseclusterloggingTypeDef",
    "ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientDescribeClusterResponseclusterTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef",
    "ClientDescribeFargateProfileResponsefargateProfileTypeDef",
    "ClientDescribeFargateProfileResponseTypeDef",
    "ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientDescribeNodegroupResponsenodegrouphealthTypeDef",
    "ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientDescribeNodegroupResponsenodegroupresourcesTypeDef",
    "ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientDescribeNodegroupResponsenodegroupTypeDef",
    "ClientDescribeNodegroupResponseTypeDef",
    "ClientDescribeUpdateResponseupdateerrorsTypeDef",
    "ClientDescribeUpdateResponseupdateparamsTypeDef",
    "ClientDescribeUpdateResponseupdateTypeDef",
    "ClientDescribeUpdateResponseTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListFargateProfilesResponseTypeDef",
    "ClientListNodegroupsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUpdatesResponseTypeDef",
    "ClientUpdateClusterConfigLoggingclusterLoggingTypeDef",
    "ClientUpdateClusterConfigLoggingTypeDef",
    "ClientUpdateClusterConfigResourcesVpcConfigTypeDef",
    "ClientUpdateClusterConfigResponseupdateerrorsTypeDef",
    "ClientUpdateClusterConfigResponseupdateparamsTypeDef",
    "ClientUpdateClusterConfigResponseupdateTypeDef",
    "ClientUpdateClusterConfigResponseTypeDef",
    "ClientUpdateClusterVersionResponseupdateerrorsTypeDef",
    "ClientUpdateClusterVersionResponseupdateparamsTypeDef",
    "ClientUpdateClusterVersionResponseupdateTypeDef",
    "ClientUpdateClusterVersionResponseTypeDef",
    "ClientUpdateNodegroupConfigLabelsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateparamsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateTypeDef",
    "ClientUpdateNodegroupConfigResponseTypeDef",
    "ClientUpdateNodegroupConfigScalingConfigTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateparamsTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateTypeDef",
    "ClientUpdateNodegroupVersionResponseTypeDef",
    "ClusterActiveWaitWaiterConfigTypeDef",
    "ClusterDeletedWaitWaiterConfigTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListFargateProfilesPaginatePaginationConfigTypeDef",
    "ListFargateProfilesPaginateResponseTypeDef",
    "ListNodegroupsPaginatePaginationConfigTypeDef",
    "ListNodegroupsPaginateResponseTypeDef",
    "ListUpdatesPaginatePaginationConfigTypeDef",
    "ListUpdatesPaginateResponseTypeDef",
    "NodegroupActiveWaitWaiterConfigTypeDef",
    "NodegroupDeletedWaitWaiterConfigTypeDef",
)


_ClientCreateClusterLoggingclusterLoggingTypeDef = TypedDict(
    "_ClientCreateClusterLoggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)


class ClientCreateClusterLoggingclusterLoggingTypeDef(
    _ClientCreateClusterLoggingclusterLoggingTypeDef
):
    pass


_ClientCreateClusterLoggingTypeDef = TypedDict(
    "_ClientCreateClusterLoggingTypeDef",
    {"clusterLogging": List[ClientCreateClusterLoggingclusterLoggingTypeDef]},
    total=False,
)


class ClientCreateClusterLoggingTypeDef(_ClientCreateClusterLoggingTypeDef):
    """
    Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch
    Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more
    information, see `Amazon EKS Cluster Control Plane Logs
    <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon
    EKS User Guide* * .
    .. note::

      CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control
      plane logs. For more information, see `Amazon CloudWatch Pricing
      <http://aws.amazon.com/cloudwatch/pricing/>`__ .
    """


_ClientCreateClusterResourcesVpcConfigTypeDef = TypedDict(
    "_ClientCreateClusterResourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientCreateClusterResourcesVpcConfigTypeDef(_ClientCreateClusterResourcesVpcConfigTypeDef):
    """
    The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific
    requirements to work properly with Kubernetes. For more information, see `Cluster VPC
    Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and
    `Cluster Security Group Considerations
    <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS
    User Guide* . You must specify at least two subnets. You can specify up to five security groups,
    but we recommend that you use a dedicated security group for your cluster control plane.
    - **subnetIds** *(list) --*

      Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic
      network interfaces in these subnets to allow communication between your worker nodes and the
      Kubernetes control plane.
      - *(string) --*
    """


_ClientCreateClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "_ClientCreateClusterResponseclustercertificateAuthorityTypeDef", {"data": str}, total=False
)


class ClientCreateClusterResponseclustercertificateAuthorityTypeDef(
    _ClientCreateClusterResponseclustercertificateAuthorityTypeDef
):
    pass


_ClientCreateClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusteridentityoidcTypeDef", {"issuer": str}, total=False
)


class ClientCreateClusterResponseclusteridentityoidcTypeDef(
    _ClientCreateClusterResponseclusteridentityoidcTypeDef
):
    pass


_ClientCreateClusterResponseclusteridentityTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusteridentityTypeDef",
    {"oidc": ClientCreateClusterResponseclusteridentityoidcTypeDef},
    total=False,
)


class ClientCreateClusterResponseclusteridentityTypeDef(
    _ClientCreateClusterResponseclusteridentityTypeDef
):
    pass


_ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)


class ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef(
    _ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef
):
    pass


_ClientCreateClusterResponseclusterloggingTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterloggingTypeDef",
    {"clusterLogging": List[ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef]},
    total=False,
)


class ClientCreateClusterResponseclusterloggingTypeDef(
    _ClientCreateClusterResponseclusterloggingTypeDef
):
    pass


_ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef(
    _ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef
):
    pass


_ClientCreateClusterResponseclusterTypeDef = TypedDict(
    "_ClientCreateClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientCreateClusterResponseclusterloggingTypeDef,
        "identity": ClientCreateClusterResponseclusteridentityTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": ClientCreateClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateClusterResponseclusterTypeDef(_ClientCreateClusterResponseclusterTypeDef):
    """
    - **cluster** *(dict) --*

      The full description of your new cluster.
      - **name** *(string) --*

        The name of the cluster.
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
        - **name** *(string) --*

          The name of the cluster.
    """


_ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef = TypedDict(
    "_ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)


class ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef(
    _ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef
):
    pass


_ClientCreateFargateProfileResponsefargateProfileTypeDef = TypedDict(
    "_ClientCreateFargateProfileResponsefargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List[ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateFargateProfileResponsefargateProfileTypeDef(
    _ClientCreateFargateProfileResponsefargateProfileTypeDef
):
    """
    - **fargateProfile** *(dict) --*

      The full description of your new Fargate profile.
      - **fargateProfileName** *(string) --*

        The name of the Fargate profile.
    """


_ClientCreateFargateProfileResponseTypeDef = TypedDict(
    "_ClientCreateFargateProfileResponseTypeDef",
    {"fargateProfile": ClientCreateFargateProfileResponsefargateProfileTypeDef},
    total=False,
)


class ClientCreateFargateProfileResponseTypeDef(_ClientCreateFargateProfileResponseTypeDef):
    """
    - *(dict) --*

      - **fargateProfile** *(dict) --*

        The full description of your new Fargate profile.
        - **fargateProfileName** *(string) --*

          The name of the Fargate profile.
    """


_ClientCreateFargateProfileSelectorsTypeDef = TypedDict(
    "_ClientCreateFargateProfileSelectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)


class ClientCreateFargateProfileSelectorsTypeDef(_ClientCreateFargateProfileSelectorsTypeDef):
    """
    - *(dict) --*

      An object representing an AWS Fargate profile selector.
      - **namespace** *(string) --*

        The Kubernetes namespace that the selector should match.
    """


_ClientCreateNodegroupRemoteAccessTypeDef = TypedDict(
    "_ClientCreateNodegroupRemoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientCreateNodegroupRemoteAccessTypeDef(_ClientCreateNodegroupRemoteAccessTypeDef):
    """
    The remote access (SSH) configuration to use with your node group.
    - **ec2SshKey** *(string) --*

      The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the
      managed node group. For more information, see `Amazon EC2 Key Pairs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon
      Elastic Compute Cloud User Guide for Linux Instances* .
    """


_ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "IamInstanceProfileNotFound",
            "IamNodeRoleNotFound",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef(
    _ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef
):
    pass


_ClientCreateNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)


class ClientCreateNodegroupResponsenodegrouphealthTypeDef(
    _ClientCreateNodegroupResponsenodegrouphealthTypeDef
):
    pass


_ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef(
    _ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef
):
    pass


_ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef(
    _ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
):
    pass


_ClientCreateNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)


class ClientCreateNodegroupResponsenodegroupresourcesTypeDef(
    _ClientCreateNodegroupResponsenodegroupresourcesTypeDef
):
    pass


_ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef(
    _ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef
):
    pass


_ClientCreateNodegroupResponsenodegroupTypeDef = TypedDict(
    "_ClientCreateNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "scalingConfig": ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientCreateNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientCreateNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateNodegroupResponsenodegroupTypeDef(_ClientCreateNodegroupResponsenodegroupTypeDef):
    """
    - **nodegroup** *(dict) --*

      The full description of your new node group.
      - **nodegroupName** *(string) --*

        The name associated with an Amazon EKS managed node group.
    """


_ClientCreateNodegroupResponseTypeDef = TypedDict(
    "_ClientCreateNodegroupResponseTypeDef",
    {"nodegroup": ClientCreateNodegroupResponsenodegroupTypeDef},
    total=False,
)


class ClientCreateNodegroupResponseTypeDef(_ClientCreateNodegroupResponseTypeDef):
    """
    - *(dict) --*

      - **nodegroup** *(dict) --*

        The full description of your new node group.
        - **nodegroupName** *(string) --*

          The name associated with an Amazon EKS managed node group.
    """


_ClientCreateNodegroupScalingConfigTypeDef = TypedDict(
    "_ClientCreateNodegroupScalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientCreateNodegroupScalingConfigTypeDef(_ClientCreateNodegroupScalingConfigTypeDef):
    """
    The scaling configuration details for the Auto Scaling group that is created for your node
    group.
    - **minSize** *(integer) --*

      The minimum number of worker nodes that the managed node group can scale in to. This number
      must be greater than zero.
    """


_ClientDeleteClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclustercertificateAuthorityTypeDef", {"data": str}, total=False
)


class ClientDeleteClusterResponseclustercertificateAuthorityTypeDef(
    _ClientDeleteClusterResponseclustercertificateAuthorityTypeDef
):
    pass


_ClientDeleteClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusteridentityoidcTypeDef", {"issuer": str}, total=False
)


class ClientDeleteClusterResponseclusteridentityoidcTypeDef(
    _ClientDeleteClusterResponseclusteridentityoidcTypeDef
):
    pass


_ClientDeleteClusterResponseclusteridentityTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusteridentityTypeDef",
    {"oidc": ClientDeleteClusterResponseclusteridentityoidcTypeDef},
    total=False,
)


class ClientDeleteClusterResponseclusteridentityTypeDef(
    _ClientDeleteClusterResponseclusteridentityTypeDef
):
    pass


_ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)


class ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef(
    _ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef
):
    pass


_ClientDeleteClusterResponseclusterloggingTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterloggingTypeDef",
    {"clusterLogging": List[ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef]},
    total=False,
)


class ClientDeleteClusterResponseclusterloggingTypeDef(
    _ClientDeleteClusterResponseclusterloggingTypeDef
):
    pass


_ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef(
    _ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef
):
    pass


_ClientDeleteClusterResponseclusterTypeDef = TypedDict(
    "_ClientDeleteClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientDeleteClusterResponseclusterloggingTypeDef,
        "identity": ClientDeleteClusterResponseclusteridentityTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": ClientDeleteClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDeleteClusterResponseclusterTypeDef(_ClientDeleteClusterResponseclusterTypeDef):
    """
    - **cluster** *(dict) --*

      The full description of the cluster to delete.
      - **name** *(string) --*

        The name of the cluster.
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

        The full description of the cluster to delete.
        - **name** *(string) --*

          The name of the cluster.
    """


_ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef = TypedDict(
    "_ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)


class ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef(
    _ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef
):
    pass


_ClientDeleteFargateProfileResponsefargateProfileTypeDef = TypedDict(
    "_ClientDeleteFargateProfileResponsefargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List[ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDeleteFargateProfileResponsefargateProfileTypeDef(
    _ClientDeleteFargateProfileResponsefargateProfileTypeDef
):
    """
    - **fargateProfile** *(dict) --*

      The deleted Fargate profile.
      - **fargateProfileName** *(string) --*

        The name of the Fargate profile.
    """


_ClientDeleteFargateProfileResponseTypeDef = TypedDict(
    "_ClientDeleteFargateProfileResponseTypeDef",
    {"fargateProfile": ClientDeleteFargateProfileResponsefargateProfileTypeDef},
    total=False,
)


class ClientDeleteFargateProfileResponseTypeDef(_ClientDeleteFargateProfileResponseTypeDef):
    """
    - *(dict) --*

      - **fargateProfile** *(dict) --*

        The deleted Fargate profile.
        - **fargateProfileName** *(string) --*

          The name of the Fargate profile.
    """


_ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "IamInstanceProfileNotFound",
            "IamNodeRoleNotFound",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef(
    _ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef
):
    pass


_ClientDeleteNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)


class ClientDeleteNodegroupResponsenodegrouphealthTypeDef(
    _ClientDeleteNodegroupResponsenodegrouphealthTypeDef
):
    pass


_ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef(
    _ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef
):
    pass


_ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef(
    _ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
):
    pass


_ClientDeleteNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupresourcesTypeDef(
    _ClientDeleteNodegroupResponsenodegroupresourcesTypeDef
):
    pass


_ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef(
    _ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef
):
    pass


_ClientDeleteNodegroupResponsenodegroupTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "scalingConfig": ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientDeleteNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientDeleteNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDeleteNodegroupResponsenodegroupTypeDef(_ClientDeleteNodegroupResponsenodegroupTypeDef):
    """
    - **nodegroup** *(dict) --*

      The full description of your deleted node group.
      - **nodegroupName** *(string) --*

        The name associated with an Amazon EKS managed node group.
    """


_ClientDeleteNodegroupResponseTypeDef = TypedDict(
    "_ClientDeleteNodegroupResponseTypeDef",
    {"nodegroup": ClientDeleteNodegroupResponsenodegroupTypeDef},
    total=False,
)


class ClientDeleteNodegroupResponseTypeDef(_ClientDeleteNodegroupResponseTypeDef):
    """
    - *(dict) --*

      - **nodegroup** *(dict) --*

        The full description of your deleted node group.
        - **nodegroupName** *(string) --*

          The name associated with an Amazon EKS managed node group.
    """


_ClientDescribeClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclustercertificateAuthorityTypeDef", {"data": str}, total=False
)


class ClientDescribeClusterResponseclustercertificateAuthorityTypeDef(
    _ClientDescribeClusterResponseclustercertificateAuthorityTypeDef
):
    pass


_ClientDescribeClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusteridentityoidcTypeDef", {"issuer": str}, total=False
)


class ClientDescribeClusterResponseclusteridentityoidcTypeDef(
    _ClientDescribeClusterResponseclusteridentityoidcTypeDef
):
    pass


_ClientDescribeClusterResponseclusteridentityTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusteridentityTypeDef",
    {"oidc": ClientDescribeClusterResponseclusteridentityoidcTypeDef},
    total=False,
)


class ClientDescribeClusterResponseclusteridentityTypeDef(
    _ClientDescribeClusterResponseclusteridentityTypeDef
):
    pass


_ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)


class ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef(
    _ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef
):
    pass


_ClientDescribeClusterResponseclusterloggingTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterloggingTypeDef",
    {"clusterLogging": List[ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef]},
    total=False,
)


class ClientDescribeClusterResponseclusterloggingTypeDef(
    _ClientDescribeClusterResponseclusterloggingTypeDef
):
    pass


_ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef(
    _ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef
):
    pass


_ClientDescribeClusterResponseclusterTypeDef = TypedDict(
    "_ClientDescribeClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientDescribeClusterResponseclusterloggingTypeDef,
        "identity": ClientDescribeClusterResponseclusteridentityTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": ClientDescribeClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeClusterResponseclusterTypeDef(_ClientDescribeClusterResponseclusterTypeDef):
    """
    - **cluster** *(dict) --*

      The full description of your specified cluster.
      - **name** *(string) --*

        The name of the cluster.
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"cluster": ClientDescribeClusterResponseclusterTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    - *(dict) --*

      - **cluster** *(dict) --*

        The full description of your specified cluster.
        - **name** *(string) --*

          The name of the cluster.
    """


_ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef = TypedDict(
    "_ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)


class ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef(
    _ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef
):
    pass


_ClientDescribeFargateProfileResponsefargateProfileTypeDef = TypedDict(
    "_ClientDescribeFargateProfileResponsefargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List[ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeFargateProfileResponsefargateProfileTypeDef(
    _ClientDescribeFargateProfileResponsefargateProfileTypeDef
):
    """
    - **fargateProfile** *(dict) --*

      The full description of your Fargate profile.
      - **fargateProfileName** *(string) --*

        The name of the Fargate profile.
    """


_ClientDescribeFargateProfileResponseTypeDef = TypedDict(
    "_ClientDescribeFargateProfileResponseTypeDef",
    {"fargateProfile": ClientDescribeFargateProfileResponsefargateProfileTypeDef},
    total=False,
)


class ClientDescribeFargateProfileResponseTypeDef(_ClientDescribeFargateProfileResponseTypeDef):
    """
    - *(dict) --*

      - **fargateProfile** *(dict) --*

        The full description of your Fargate profile.
        - **fargateProfileName** *(string) --*

          The name of the Fargate profile.
    """


_ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "IamInstanceProfileNotFound",
            "IamNodeRoleNotFound",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef(
    _ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef
):
    pass


_ClientDescribeNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)


class ClientDescribeNodegroupResponsenodegrouphealthTypeDef(
    _ClientDescribeNodegroupResponsenodegrouphealthTypeDef
):
    pass


_ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef(
    _ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef
):
    pass


_ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef(
    _ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
):
    pass


_ClientDescribeNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupresourcesTypeDef(
    _ClientDescribeNodegroupResponsenodegroupresourcesTypeDef
):
    pass


_ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef(
    _ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef
):
    pass


_ClientDescribeNodegroupResponsenodegroupTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "scalingConfig": ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientDescribeNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientDescribeNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeNodegroupResponsenodegroupTypeDef(
    _ClientDescribeNodegroupResponsenodegroupTypeDef
):
    """
    - **nodegroup** *(dict) --*

      The full description of your node group.
      - **nodegroupName** *(string) --*

        The name associated with an Amazon EKS managed node group.
    """


_ClientDescribeNodegroupResponseTypeDef = TypedDict(
    "_ClientDescribeNodegroupResponseTypeDef",
    {"nodegroup": ClientDescribeNodegroupResponsenodegroupTypeDef},
    total=False,
)


class ClientDescribeNodegroupResponseTypeDef(_ClientDescribeNodegroupResponseTypeDef):
    """
    - *(dict) --*

      - **nodegroup** *(dict) --*

        The full description of your node group.
        - **nodegroupName** *(string) --*

          The name associated with an Amazon EKS managed node group.
    """


_ClientDescribeUpdateResponseupdateerrorsTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientDescribeUpdateResponseupdateerrorsTypeDef(
    _ClientDescribeUpdateResponseupdateerrorsTypeDef
):
    pass


_ClientDescribeUpdateResponseupdateparamsTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
        ],
        "value": str,
    },
    total=False,
)


class ClientDescribeUpdateResponseupdateparamsTypeDef(
    _ClientDescribeUpdateResponseupdateparamsTypeDef
):
    pass


_ClientDescribeUpdateResponseupdateTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientDescribeUpdateResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientDescribeUpdateResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientDescribeUpdateResponseupdateTypeDef(_ClientDescribeUpdateResponseupdateTypeDef):
    """
    - **update** *(dict) --*

      The full description of the specified update.
      - **id** *(string) --*

        A UUID that is used to track the update.
    """


_ClientDescribeUpdateResponseTypeDef = TypedDict(
    "_ClientDescribeUpdateResponseTypeDef",
    {"update": ClientDescribeUpdateResponseupdateTypeDef},
    total=False,
)


class ClientDescribeUpdateResponseTypeDef(_ClientDescribeUpdateResponseTypeDef):
    """
    - *(dict) --*

      - **update** *(dict) --*

        The full description of the specified update.
        - **id** *(string) --*

          A UUID that is used to track the update.
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef", {"clusters": List[str], "nextToken": str}, total=False
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    - *(dict) --*

      - **clusters** *(list) --*

        A list of all of the clusters for your account in the specified Region.
        - *(string) --*
    """


_ClientListFargateProfilesResponseTypeDef = TypedDict(
    "_ClientListFargateProfilesResponseTypeDef",
    {"fargateProfileNames": List[str], "nextToken": str},
    total=False,
)


class ClientListFargateProfilesResponseTypeDef(_ClientListFargateProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **fargateProfileNames** *(list) --*

        A list of all of the Fargate profiles associated with the specified cluster.
        - *(string) --*
    """


_ClientListNodegroupsResponseTypeDef = TypedDict(
    "_ClientListNodegroupsResponseTypeDef", {"nodegroups": List[str], "nextToken": str}, total=False
)


class ClientListNodegroupsResponseTypeDef(_ClientListNodegroupsResponseTypeDef):
    """
    - *(dict) --*

      - **nodegroups** *(list) --*

        A list of all of the node groups associated with the specified cluster.
        - *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        The tags for the resource.
        - *(string) --*

          - *(string) --*
    """


_ClientListUpdatesResponseTypeDef = TypedDict(
    "_ClientListUpdatesResponseTypeDef", {"updateIds": List[str], "nextToken": str}, total=False
)


class ClientListUpdatesResponseTypeDef(_ClientListUpdatesResponseTypeDef):
    """
    - *(dict) --*

      - **updateIds** *(list) --*

        A list of all the updates for the specified cluster and Region.
        - *(string) --*
    """


_ClientUpdateClusterConfigLoggingclusterLoggingTypeDef = TypedDict(
    "_ClientUpdateClusterConfigLoggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)


class ClientUpdateClusterConfigLoggingclusterLoggingTypeDef(
    _ClientUpdateClusterConfigLoggingclusterLoggingTypeDef
):
    pass


_ClientUpdateClusterConfigLoggingTypeDef = TypedDict(
    "_ClientUpdateClusterConfigLoggingTypeDef",
    {"clusterLogging": List[ClientUpdateClusterConfigLoggingclusterLoggingTypeDef]},
    total=False,
)


class ClientUpdateClusterConfigLoggingTypeDef(_ClientUpdateClusterConfigLoggingTypeDef):
    """
    Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch
    Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more
    information, see `Amazon EKS Cluster Control Plane Logs
    <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon
    EKS User Guide* * .
    .. note::

      CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control
      plane logs. For more information, see `Amazon CloudWatch Pricing
      <http://aws.amazon.com/cloudwatch/pricing/>`__ .
    """


_ClientUpdateClusterConfigResourcesVpcConfigTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)


class ClientUpdateClusterConfigResourcesVpcConfigTypeDef(
    _ClientUpdateClusterConfigResourcesVpcConfigTypeDef
):
    """
    An object representing the VPC configuration to use for an Amazon EKS cluster.
    - **subnetIds** *(list) --*

      Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic
      network interfaces in these subnets to allow communication between your worker nodes and the
      Kubernetes control plane.
      - *(string) --*
    """


_ClientUpdateClusterConfigResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientUpdateClusterConfigResponseupdateerrorsTypeDef(
    _ClientUpdateClusterConfigResponseupdateerrorsTypeDef
):
    pass


_ClientUpdateClusterConfigResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
        ],
        "value": str,
    },
    total=False,
)


class ClientUpdateClusterConfigResponseupdateparamsTypeDef(
    _ClientUpdateClusterConfigResponseupdateparamsTypeDef
):
    pass


_ClientUpdateClusterConfigResponseupdateTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateClusterConfigResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateClusterConfigResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateClusterConfigResponseupdateTypeDef(
    _ClientUpdateClusterConfigResponseupdateTypeDef
):
    """
    - **update** *(dict) --*

      An object representing an asynchronous update.
      - **id** *(string) --*

        A UUID that is used to track the update.
    """


_ClientUpdateClusterConfigResponseTypeDef = TypedDict(
    "_ClientUpdateClusterConfigResponseTypeDef",
    {"update": ClientUpdateClusterConfigResponseupdateTypeDef},
    total=False,
)


class ClientUpdateClusterConfigResponseTypeDef(_ClientUpdateClusterConfigResponseTypeDef):
    """
    - *(dict) --*

      - **update** *(dict) --*

        An object representing an asynchronous update.
        - **id** *(string) --*

          A UUID that is used to track the update.
    """


_ClientUpdateClusterVersionResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientUpdateClusterVersionResponseupdateerrorsTypeDef(
    _ClientUpdateClusterVersionResponseupdateerrorsTypeDef
):
    pass


_ClientUpdateClusterVersionResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
        ],
        "value": str,
    },
    total=False,
)


class ClientUpdateClusterVersionResponseupdateparamsTypeDef(
    _ClientUpdateClusterVersionResponseupdateparamsTypeDef
):
    pass


_ClientUpdateClusterVersionResponseupdateTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateClusterVersionResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateClusterVersionResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateClusterVersionResponseupdateTypeDef(
    _ClientUpdateClusterVersionResponseupdateTypeDef
):
    """
    - **update** *(dict) --*

      The full description of the specified update
      - **id** *(string) --*

        A UUID that is used to track the update.
    """


_ClientUpdateClusterVersionResponseTypeDef = TypedDict(
    "_ClientUpdateClusterVersionResponseTypeDef",
    {"update": ClientUpdateClusterVersionResponseupdateTypeDef},
    total=False,
)


class ClientUpdateClusterVersionResponseTypeDef(_ClientUpdateClusterVersionResponseTypeDef):
    """
    - *(dict) --*

      - **update** *(dict) --*

        The full description of the specified update
        - **id** *(string) --*

          A UUID that is used to track the update.
    """


_ClientUpdateNodegroupConfigLabelsTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigLabelsTypeDef",
    {"addOrUpdateLabels": Dict[str, str], "removeLabels": List[str]},
    total=False,
)


class ClientUpdateNodegroupConfigLabelsTypeDef(_ClientUpdateNodegroupConfigLabelsTypeDef):
    """
    The Kubernetes labels to be applied to the nodes in the node group after the update.
    - **addOrUpdateLabels** *(dict) --*

      Kubernetes labels to be added or updated.
      - *(string) --*

        - *(string) --*
    """


_ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef(
    _ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef
):
    pass


_ClientUpdateNodegroupConfigResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
        ],
        "value": str,
    },
    total=False,
)


class ClientUpdateNodegroupConfigResponseupdateparamsTypeDef(
    _ClientUpdateNodegroupConfigResponseupdateparamsTypeDef
):
    pass


_ClientUpdateNodegroupConfigResponseupdateTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateNodegroupConfigResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateNodegroupConfigResponseupdateTypeDef(
    _ClientUpdateNodegroupConfigResponseupdateTypeDef
):
    """
    - **update** *(dict) --*

      An object representing an asynchronous update.
      - **id** *(string) --*

        A UUID that is used to track the update.
    """


_ClientUpdateNodegroupConfigResponseTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigResponseTypeDef",
    {"update": ClientUpdateNodegroupConfigResponseupdateTypeDef},
    total=False,
)


class ClientUpdateNodegroupConfigResponseTypeDef(_ClientUpdateNodegroupConfigResponseTypeDef):
    """
    - *(dict) --*

      - **update** *(dict) --*

        An object representing an asynchronous update.
        - **id** *(string) --*

          A UUID that is used to track the update.
    """


_ClientUpdateNodegroupConfigScalingConfigTypeDef = TypedDict(
    "_ClientUpdateNodegroupConfigScalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)


class ClientUpdateNodegroupConfigScalingConfigTypeDef(
    _ClientUpdateNodegroupConfigScalingConfigTypeDef
):
    """
    The scaling configuration details for the Auto Scaling group after the update.
    - **minSize** *(integer) --*

      The minimum number of worker nodes that the managed node group can scale in to. This number
      must be greater than zero.
    """


_ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)


class ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef(
    _ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef
):
    pass


_ClientUpdateNodegroupVersionResponseupdateparamsTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
        ],
        "value": str,
    },
    total=False,
)


class ClientUpdateNodegroupVersionResponseupdateparamsTypeDef(
    _ClientUpdateNodegroupVersionResponseupdateparamsTypeDef
):
    pass


_ClientUpdateNodegroupVersionResponseupdateTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateNodegroupVersionResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef],
    },
    total=False,
)


class ClientUpdateNodegroupVersionResponseupdateTypeDef(
    _ClientUpdateNodegroupVersionResponseupdateTypeDef
):
    """
    - **update** *(dict) --*

      An object representing an asynchronous update.
      - **id** *(string) --*

        A UUID that is used to track the update.
    """


_ClientUpdateNodegroupVersionResponseTypeDef = TypedDict(
    "_ClientUpdateNodegroupVersionResponseTypeDef",
    {"update": ClientUpdateNodegroupVersionResponseupdateTypeDef},
    total=False,
)


class ClientUpdateNodegroupVersionResponseTypeDef(_ClientUpdateNodegroupVersionResponseTypeDef):
    """
    - *(dict) --*

      - **update** *(dict) --*

        An object representing an asynchronous update.
        - **id** *(string) --*

          A UUID that is used to track the update.
    """


_ClusterActiveWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterActiveWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ClusterActiveWaitWaiterConfigTypeDef(_ClusterActiveWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ClusterDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ClusterDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ClusterDeletedWaitWaiterConfigTypeDef(_ClusterDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
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
    "_ListClustersPaginateResponseTypeDef", {"clusters": List[str], "NextToken": str}, total=False
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **clusters** *(list) --*

        A list of all of the clusters for your account in the specified Region.
        - *(string) --*
    """


_ListFargateProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFargateProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFargateProfilesPaginatePaginationConfigTypeDef(
    _ListFargateProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFargateProfilesPaginateResponseTypeDef = TypedDict(
    "_ListFargateProfilesPaginateResponseTypeDef",
    {"fargateProfileNames": List[str], "NextToken": str},
    total=False,
)


class ListFargateProfilesPaginateResponseTypeDef(_ListFargateProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **fargateProfileNames** *(list) --*

        A list of all of the Fargate profiles associated with the specified cluster.
        - *(string) --*
    """


_ListNodegroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNodegroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNodegroupsPaginatePaginationConfigTypeDef(_ListNodegroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNodegroupsPaginateResponseTypeDef = TypedDict(
    "_ListNodegroupsPaginateResponseTypeDef",
    {"nodegroups": List[str], "NextToken": str},
    total=False,
)


class ListNodegroupsPaginateResponseTypeDef(_ListNodegroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **nodegroups** *(list) --*

        A list of all of the node groups associated with the specified cluster.
        - *(string) --*
    """


_ListUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUpdatesPaginatePaginationConfigTypeDef(_ListUpdatesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUpdatesPaginateResponseTypeDef = TypedDict(
    "_ListUpdatesPaginateResponseTypeDef", {"updateIds": List[str], "NextToken": str}, total=False
)


class ListUpdatesPaginateResponseTypeDef(_ListUpdatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **updateIds** *(list) --*

        A list of all the updates for the specified cluster and Region.
        - *(string) --*
    """


_NodegroupActiveWaitWaiterConfigTypeDef = TypedDict(
    "_NodegroupActiveWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class NodegroupActiveWaitWaiterConfigTypeDef(_NodegroupActiveWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_NodegroupDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_NodegroupDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class NodegroupDeletedWaitWaiterConfigTypeDef(_NodegroupDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """
