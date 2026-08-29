# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import Datastore

from pyVmomi.vim import KeyValue

from pyVmomi.vim import Task

from pyVmomi.vim import VirtualMachine
from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.encryption import CryptoSpec

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vsan import FileShareNetPermission

from pyVmomi.vim.vslm import DiskCryptoSpec



class AccessControlSpec(DynamicData):
   pass


class AsyncQueryResult(VolumeOperationResult):
   queryResult: Optional[QueryResult] = None


class BackingObjectDetails(DynamicData):
   capacityInMb: Optional[long] = None


class BaseCreateSpec(DynamicData):
   pass


class BlockBackingDetails(BackingObjectDetails):
   backingDiskId: Optional[str] = None
   backingDiskUrlPath: Optional[str] = None
   backingDiskPath: Optional[str] = None
   backingDiskObjectId: Optional[str] = None
   usedCapacityInMb: Optional[long] = None
   aggregatedSnapshotCapacityInMb: Optional[long] = None


class BlockCreateSpec(BaseCreateSpec):
   cryptoSpec: Optional[CryptoSpec] = None

class BlockVolumeRelocateSpec(VolumeRelocateSpec):
   pass


class CloneVolumeSource(VolumeSource):
   volumeId: VolumeId
   keepAfterDeleteVm: Optional[bool] = None

class ClusterFlavor:
   pass

class ClusterType:
   pass


class ContainerCluster(DynamicData):
   clusterType: str
   clusterId: str
   vSphereUser: str
   clusterFlavor: Optional[str] = None
   clusterDistribution: Optional[str] = None
   delete: Optional[bool] = None


class Cursor(DynamicData):
   offset: long
   limit: long
   totalRecords: Optional[long] = None


class EntityMetadata(DynamicData):
   entityName: str
   labels: list[KeyValue] = []
   delete: Optional[bool] = None
   clusterId: Optional[str] = None


class FileBackingDetails(BackingObjectDetails):
   backingFileId: Optional[str] = None

class FileCreateSpec(BaseCreateSpec):
   pass


class KubernetesEntityMetadata(EntityMetadata):
   entityType: str
   namespace: Optional[str] = None
   referredEntity: list[KubernetesEntityReference] = []


class KubernetesEntityReference(DynamicData):
   entityType: str
   entityName: str
   namespace: Optional[str] = None
   clusterId: Optional[str] = None

class KubernetesEntityType:
   pass


class KubernetesQueryFilter(QueryFilter):
   namespaces: list[str] = []
   podNames: list[str] = []
   pvcNames: list[str] = []
   pvNames: list[str] = []

class MetricFormat:
   pass

class MetricType:
   pass


class NFSAccessControlSpec(AccessControlSpec):
   netPermission: FileShareNetPermission
   delete: Optional[bool] = None


class PlacementResult(DynamicData):
   datastore: Datastore
   placementFaults: list[MethodFault] = []
   clusters: list[ClusterComputeResource] = []


class QueryFilter(DynamicData):
   volumeIds: list[VolumeId] = []
   names: list[str] = []
   containerClusterIds: list[str] = []
   storagePolicyId: Optional[str] = None
   datastores: list[Datastore] = []
   labels: list[KeyValue] = []
   complianceStatus: Optional[str] = None
   datastoreAccessibilityStatus: Optional[str] = None
   cursor: Optional[Cursor] = None
   healthStatus: Optional[str] = None


class QueryResult(DynamicData):
   volumes: list[Volume] = []
   cursor: Cursor


class QuerySelection(DynamicData):
   names: list[str] = []

class QuerySelectionNameType:
   pass


class SnapshotCreateSpec(DynamicData):
   volumeId: VolumeId
   description: str
   snapshotId: Optional[SnapshotId] = None


class SnapshotDeleteSpec(DynamicData):
   volumeId: VolumeId
   snapshotId: SnapshotId


class SnapshotId(DynamicData):
   id: str


class SnapshotVolumeSource(VolumeSource):
   volumeId: Optional[VolumeId] = None
   snapshotId: Optional[SnapshotId] = None
   linkedClone: Optional[bool] = None

class SyncVolumeMode:
   pass


class SyncVolumeSpec(DynamicData):
   volumeId: VolumeId
   datastore: Optional[Datastore] = None
   syncMode: list[str] = []

class UnregisterTargetVolumeType:
   pass


class UnregisterVolumeSpec(DynamicData):
   volumeId: VolumeId
   targetVolumeType: str


class VSANFileCreateSpec(FileCreateSpec):
   softQuotaInMb: Optional[long] = None
   permission: list[FileShareNetPermission] = []


class Volume(DynamicData):
   volumeId: VolumeId
   datastoreUrl: Optional[str] = None
   name: Optional[str] = None
   volumeType: Optional[str] = None
   storagePolicyId: Optional[str] = None
   metadata: Optional[VolumeMetadata] = None
   backingObjectDetails: Optional[BackingObjectDetails] = None
   complianceStatus: Optional[str] = None
   datastoreAccessibilityStatus: Optional[str] = None
   healthStatus: Optional[str] = None


class VolumeACLConfigureSpec(DynamicData):
   volumeId: VolumeId
   accessControlSpecList: list[AccessControlSpec] = []


class VolumeAttachDetachSpec(DynamicData):
   volumeId: VolumeId
   vm: VirtualMachine
   diskMode: Optional[str] = None
   sharing: Optional[str] = None
   controllerKey: Optional[int] = None
   unitNumber: Optional[int] = None
   backingTypeName: Optional[str] = None
   volumeEncrypted: Optional[bool] = None


class VolumeAttachResult(VolumeOperationResult):
   diskUUID: Optional[str] = None

class VolumeBackingType:
   pass


class VolumeCreateResult(VolumeOperationResult):
   name: Optional[str] = None
   placementResults: list[PlacementResult] = []


class VolumeCreateSpec(DynamicData):
   name: str
   volumeType: str
   volumeId: Optional[VolumeId] = None
   datastores: list[Datastore] = []
   metadata: Optional[VolumeMetadata] = None
   backingObjectDetails: BackingObjectDetails
   profile: list[ProfileSpec] = []
   activeClusters: list[ClusterComputeResource] = []
   createSpec: Optional[BaseCreateSpec] = None
   volumeSource: Optional[VolumeSource] = None


class VolumeCryptoUpdateSpec(DynamicData):
   volumeId: VolumeId
   profile: list[ProfileSpec] = []
   disksCrypto: Optional[DiskCryptoSpec] = None


class VolumeExtendSpec(DynamicData):
   volumeId: VolumeId
   capacityInMb: long


class VolumeId(DynamicData):
   id: str


class VolumeManager(ManagedObject):
   def Create(self, createSpecs: list[VolumeCreateSpec]) -> Task: ...
   def UpdateVolumeMetadata(self, updateSpecs: list[VolumeMetadataUpdateSpec]) -> Task: ...
   def Delete(self, volumeIds: list[VolumeId], deleteDisk: bool) -> Task: ...
   def Attach(self, attachSpecs: list[VolumeAttachDetachSpec]) -> Task: ...
   def Detach(self, detachSpecs: list[VolumeAttachDetachSpec]) -> Task: ...
   def QueryAsync(self, filter: QueryFilter, selection: Optional[QuerySelection]) -> Task: ...
   def Query(self, filter: QueryFilter, selection: Optional[QuerySelection]) -> QueryResult: ...
   def ConfigureVolumeACLs(self, ACLConfigSpecs: list[VolumeACLConfigureSpec]) -> Task: ...
   def Extend(self, extendSpecs: list[VolumeExtendSpec]) -> Task: ...
   def CreateSnapshots(self, snapshotSpecs: list[SnapshotCreateSpec]) -> Task: ...
   def DeleteSnapshots(self, snapshotDeleteSpecs: list[SnapshotDeleteSpec]) -> Task: ...
   def Relocate(self, relocateSpecs: list[VolumeRelocateSpec]) -> Task: ...
   def ReconfigPolicy(self, volumePolicyReconfigSpecs: list[VolumePolicyReconfigSpec]) -> Task: ...
   def UpdateVolumeCrypto(self, updateSpecs: list[VolumeCryptoUpdateSpec]) -> Task: ...
   def UnregisterVolume(self, unregisterSpec: list[UnregisterVolumeSpec]) -> Task: ...
   def SyncVolume(self, syncSpecs: list[SyncVolumeSpec]) -> Task: ...


class VolumeMetadata(DynamicData):
   containerCluster: ContainerCluster
   entityMetadata: list[EntityMetadata] = []
   containerClusterArray: list[ContainerCluster] = []


class VolumeMetadataUpdateSpec(DynamicData):
   volumeId: VolumeId
   metadata: VolumeMetadata


class VolumeOperationBatchResult(DynamicData):
   volumeResults: list[VolumeOperationResult] = []


class VolumeOperationResult(DynamicData):
   volumeId: Optional[VolumeId] = None
   fault: Optional[MethodFault] = None


class VolumePolicyReconfigSpec(DynamicData):
   volumeId: VolumeId
   profile: list[ProfileSpec] = []


class VolumeRelocateSpec(DynamicData):
   volumeId: VolumeId
   datastore: Datastore
   profile: list[ProfileSpec] = []


class VolumeSource(DynamicData):
   pass

class VolumeType:
   pass


class VsanFileShareBackingDetails(FileBackingDetails):
   name: Optional[str] = None
   accessPoints: list[KeyValue] = []
   permission: list[FileShareNetPermission] = []
