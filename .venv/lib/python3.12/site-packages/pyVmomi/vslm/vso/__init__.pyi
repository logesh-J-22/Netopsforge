# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar

from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import KeyValue
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.encryption import CryptoSpec

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vslm import CloneSpec
from pyVmomi.vim.vslm import CreateSpec
from pyVmomi.vim.vslm import DiskCryptoSpec

from pyVmomi.vim.vslm import ID
from pyVmomi.vim.vslm import InfrastructureObjectPolicy
from pyVmomi.vim.vslm import InfrastructureObjectPolicySpec
from pyVmomi.vim.vslm import RelocateSpec
from pyVmomi.vim.vslm import StateInfo
from pyVmomi.vim.vslm import TagEntry
from pyVmomi.vim.vslm import VStorageObject
from pyVmomi.vim.vslm import VStorageObjectSnapshotDetails
from pyVmomi.vim.vslm import VStorageObjectSnapshotInfo



class DatastoreSyncStatus(DynamicData):
   datastoreURL: str
   objectVClock: long
   syncVClock: long
   syncTime: Optional[datetime] = None
   numberOfRetries: Optional[int] = None
   error: Optional[MethodFault] = None


class VStorageObjectAssociations(DynamicData):
   class VmDiskAssociation(DynamicData):
      vmId: str
      diskKey: int

   id: ID
   vmDiskAssociation: list[VmDiskAssociation] = []
   fault: Optional[MethodFault] = None


class VStorageObjectManager(ManagedObject):
   def CreateDisk(self, spec: CreateSpec) -> Task: ...
   def RegisterDisk(self, path: str, name: Optional[str]) -> VStorageObject: ...
   def ExtendDisk(self, id: ID, newCapacityInMB: long) -> Task: ...
   def InflateDisk(self, id: ID) -> Task: ...
   def RenameVStorageObject(self, id: ID, name: str) -> None: ...
   def UpdateVStorageObjectPolicy(self, id: ID, profile: list[ProfileSpec]) -> Task: ...
   def UpdateVStorageObjectCrypto(self, id: ID, profile: list[ProfileSpec], disksCrypto: Optional[DiskCryptoSpec]) -> Task: ...
   def UpdateVStorageInfrastructureObjectPolicy(self, spec: InfrastructureObjectPolicySpec) -> Task: ...
   def RetrieveVStorageInfrastructureObjectPolicy(self, datastore: Datastore) -> list[InfrastructureObjectPolicy]: ...
   def DeleteVStorageObject(self, id: ID) -> Task: ...
   def RetrieveVStorageObject(self, id: ID) -> VStorageObject: ...
   def RetrieveVStorageObjectState(self, id: ID) -> StateInfo: ...
   def RetrieveVStorageObjectAssociations(self, ids: list[ID]) -> list[VStorageObjectAssociations]: ...
   def ListVStorageObjectsForSpec(self, query: list[VStorageObjectQuerySpec], maxResult: int) -> Optional[VStorageObjectQueryResult]: ...
   def CloneVStorageObject(self, id: ID, spec: CloneSpec) -> Task: ...
   def RelocateVStorageObject(self, id: ID, spec: RelocateSpec) -> Task: ...
   def SetVStorageObjectControlFlags(self, id: ID, controlFlags: list[str]) -> None: ...
   def ClearVStorageObjectControlFlags(self, id: ID, controlFlags: list[str]) -> None: ...
   def AttachTagToVStorageObject(self, id: ID, category: str, tag: str) -> None: ...
   def DetachTagFromVStorageObject(self, id: ID, category: str, tag: str) -> None: ...
   def ListVStorageObjectsAttachedToTag(self, category: str, tag: str) -> list[ID]: ...
   def ListTagsAttachedToVStorageObject(self, id: ID) -> list[TagEntry]: ...
   def ReconcileDatastoreInventory(self, datastore: Datastore) -> Task: ...
   def ScheduleReconcileDatastoreInventory(self, datastore: Datastore) -> None: ...
   def CreateSnapshot(self, id: ID, description: str) -> Task: ...
   def DeleteSnapshot(self, id: ID, snapshotId: ID) -> Task: ...
   def RetrieveSnapshotInfo(self, id: ID) -> VStorageObjectSnapshotInfo: ...
   def CreateDiskFromSnapshot(self, id: ID, snapshotId: ID, name: str, profile: list[ProfileSpec], crypto: Optional[CryptoSpec], path: Optional[str]) -> Task: ...
   def RevertVStorageObject(self, id: ID, snapshotId: ID) -> Task: ...
   def RetrieveSnapshotDetails(self, id: ID, snapshotId: ID) -> VStorageObjectSnapshotDetails: ...
   def QueryChangedDiskAreas(self, id: ID, snapshotId: ID, startOffset: long, changeId: str) -> VirtualMachine.DiskChangeInfo: ...
   def QueryGlobalCatalogSyncStatus(self) -> list[DatastoreSyncStatus]: ...
   def QueryGlobalCatalogSyncStatusForDatastore(self, datastoreURL: str) -> Optional[DatastoreSyncStatus]: ...
   def UpdateVStorageObjectMetadata(self, id: ID, metadata: list[KeyValue], deleteKeys: list[str]) -> Task: ...
   def RetrieveVStorageObjectMetadata(self, id: ID, snapshotId: Optional[ID], prefix: Optional[str]) -> list[KeyValue]: ...
   def RetrieveVStorageObjectMetadataValue(self, id: ID, snapshotId: Optional[ID], key: str) -> str: ...
   def RetrieveVStorageObjects(self, ids: list[ID]) -> list[VStorageObjectResult]: ...
   def AttachDisk(self, id: ID, vm: VirtualMachine, controllerKey: Optional[int], unitNumber: Optional[int]) -> Task: ...


class VStorageObjectQueryResult(DynamicData):
   allRecordsReturned: bool
   id: list[ID] = []
   queryResults: list[VStorageObjectResult] = []


class VStorageObjectQuerySpec(DynamicData):
   class QueryOperatorEnum(Enum):
      equals: ClassVar['QueryOperatorEnum'] = 'equals'
      notEquals: ClassVar['QueryOperatorEnum'] = 'notEquals'
      lessThan: ClassVar['QueryOperatorEnum'] = 'lessThan'
      greaterThan: ClassVar['QueryOperatorEnum'] = 'greaterThan'
      lessThanOrEqual: ClassVar['QueryOperatorEnum'] = 'lessThanOrEqual'
      greaterThanOrEqual: ClassVar['QueryOperatorEnum'] = 'greaterThanOrEqual'
      contains: ClassVar['QueryOperatorEnum'] = 'contains'
      startsWith: ClassVar['QueryOperatorEnum'] = 'startsWith'
      endsWith: ClassVar['QueryOperatorEnum'] = 'endsWith'

   class QueryFieldEnum(Enum):
      id: ClassVar['QueryFieldEnum'] = 'id'
      name: ClassVar['QueryFieldEnum'] = 'name'
      capacity: ClassVar['QueryFieldEnum'] = 'capacity'
      createTime: ClassVar['QueryFieldEnum'] = 'createTime'
      backingObjectId: ClassVar['QueryFieldEnum'] = 'backingObjectId'
      datastoreMoId: ClassVar['QueryFieldEnum'] = 'datastoreMoId'
      metadataKey: ClassVar['QueryFieldEnum'] = 'metadataKey'
      metadataValue: ClassVar['QueryFieldEnum'] = 'metadataValue'

   queryField: str
   queryOperator: str
   queryValue: list[str] = []


class VStorageObjectResult(DynamicData):
   id: ID
   name: Optional[str] = None
   capacityInMB: long
   createTime: Optional[datetime] = None
   datastoreUrl: Optional[str] = None
   diskPath: Optional[str] = None
   usedCapacityInMB: Optional[long] = None
   backingObjectId: Optional[ID] = None
   snapshotInfo: list[VStorageObjectSnapshotResult] = []
   metadata: list[KeyValue] = []
   error: Optional[MethodFault] = None


class VStorageObjectSnapshotResult(DynamicData):
   backingObjectId: ID
   description: Optional[str] = None
   snapshotId: Optional[ID] = None
   diskPath: Optional[str] = None
