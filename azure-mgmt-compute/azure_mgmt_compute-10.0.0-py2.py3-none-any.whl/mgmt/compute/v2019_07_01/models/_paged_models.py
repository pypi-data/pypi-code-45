# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class ComputeOperationValuePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ComputeOperationValue <azure.mgmt.compute.v2019_07_01.models.ComputeOperationValue>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ComputeOperationValue]'}
    }

    def __init__(self, *args, **kwargs):

        super(ComputeOperationValuePaged, self).__init__(*args, **kwargs)
class AvailabilitySetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AvailabilitySet <azure.mgmt.compute.v2019_07_01.models.AvailabilitySet>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AvailabilitySet]'}
    }

    def __init__(self, *args, **kwargs):

        super(AvailabilitySetPaged, self).__init__(*args, **kwargs)
class VirtualMachineSizePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachineSize <azure.mgmt.compute.v2019_07_01.models.VirtualMachineSize>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachineSize]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachineSizePaged, self).__init__(*args, **kwargs)
class ProximityPlacementGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProximityPlacementGroup <azure.mgmt.compute.v2019_07_01.models.ProximityPlacementGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProximityPlacementGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProximityPlacementGroupPaged, self).__init__(*args, **kwargs)
class DedicatedHostGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DedicatedHostGroup <azure.mgmt.compute.v2019_07_01.models.DedicatedHostGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DedicatedHostGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(DedicatedHostGroupPaged, self).__init__(*args, **kwargs)
class DedicatedHostPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DedicatedHost <azure.mgmt.compute.v2019_07_01.models.DedicatedHost>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DedicatedHost]'}
    }

    def __init__(self, *args, **kwargs):

        super(DedicatedHostPaged, self).__init__(*args, **kwargs)
class UsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Usage <azure.mgmt.compute.v2019_07_01.models.Usage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Usage]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsagePaged, self).__init__(*args, **kwargs)
class VirtualMachinePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachine <azure.mgmt.compute.v2019_07_01.models.VirtualMachine>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachine]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachinePaged, self).__init__(*args, **kwargs)
class ImagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Image <azure.mgmt.compute.v2019_07_01.models.Image>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Image]'}
    }

    def __init__(self, *args, **kwargs):

        super(ImagePaged, self).__init__(*args, **kwargs)
class VirtualMachineScaleSetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachineScaleSet <azure.mgmt.compute.v2019_07_01.models.VirtualMachineScaleSet>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachineScaleSet]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachineScaleSetPaged, self).__init__(*args, **kwargs)
class VirtualMachineScaleSetSkuPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachineScaleSetSku <azure.mgmt.compute.v2019_07_01.models.VirtualMachineScaleSetSku>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachineScaleSetSku]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachineScaleSetSkuPaged, self).__init__(*args, **kwargs)
class UpgradeOperationHistoricalStatusInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`UpgradeOperationHistoricalStatusInfo <azure.mgmt.compute.v2019_07_01.models.UpgradeOperationHistoricalStatusInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[UpgradeOperationHistoricalStatusInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(UpgradeOperationHistoricalStatusInfoPaged, self).__init__(*args, **kwargs)
class VirtualMachineScaleSetExtensionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachineScaleSetExtension <azure.mgmt.compute.v2019_07_01.models.VirtualMachineScaleSetExtension>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachineScaleSetExtension]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachineScaleSetExtensionPaged, self).__init__(*args, **kwargs)
class VirtualMachineScaleSetVMPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualMachineScaleSetVM <azure.mgmt.compute.v2019_07_01.models.VirtualMachineScaleSetVM>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualMachineScaleSetVM]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualMachineScaleSetVMPaged, self).__init__(*args, **kwargs)
class DiskPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Disk <azure.mgmt.compute.v2019_07_01.models.Disk>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Disk]'}
    }

    def __init__(self, *args, **kwargs):

        super(DiskPaged, self).__init__(*args, **kwargs)
class SnapshotPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Snapshot <azure.mgmt.compute.v2019_07_01.models.Snapshot>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Snapshot]'}
    }

    def __init__(self, *args, **kwargs):

        super(SnapshotPaged, self).__init__(*args, **kwargs)
class DiskEncryptionSetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DiskEncryptionSet <azure.mgmt.compute.v2019_07_01.models.DiskEncryptionSet>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DiskEncryptionSet]'}
    }

    def __init__(self, *args, **kwargs):

        super(DiskEncryptionSetPaged, self).__init__(*args, **kwargs)
class GalleryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Gallery <azure.mgmt.compute.v2019_07_01.models.Gallery>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Gallery]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryPaged, self).__init__(*args, **kwargs)
class GalleryImagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryImage <azure.mgmt.compute.v2019_07_01.models.GalleryImage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryImage]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryImagePaged, self).__init__(*args, **kwargs)
class GalleryImageVersionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryImageVersion <azure.mgmt.compute.v2019_07_01.models.GalleryImageVersion>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryImageVersion]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryImageVersionPaged, self).__init__(*args, **kwargs)
class GalleryApplicationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryApplication <azure.mgmt.compute.v2019_07_01.models.GalleryApplication>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryApplication]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryApplicationPaged, self).__init__(*args, **kwargs)
class GalleryApplicationVersionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryApplicationVersion <azure.mgmt.compute.v2019_07_01.models.GalleryApplicationVersion>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryApplicationVersion]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryApplicationVersionPaged, self).__init__(*args, **kwargs)
class RunCommandDocumentBasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RunCommandDocumentBase <azure.mgmt.compute.v2019_07_01.models.RunCommandDocumentBase>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RunCommandDocumentBase]'}
    }

    def __init__(self, *args, **kwargs):

        super(RunCommandDocumentBasePaged, self).__init__(*args, **kwargs)
