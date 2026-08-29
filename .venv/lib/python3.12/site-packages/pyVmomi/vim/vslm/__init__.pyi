# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import host as host
from . import vcenter as vcenter

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import KeyValue

from pyVmomi.vim import ServiceLocator
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.encryption import CryptoSpec

from pyVmomi.vim.vm import ProfileSpec



class BaseConfigInfo(DynamicData):
   class BackingInfo(DynamicData):
      datastore: Datastore

   class FileBackingInfo(BackingInfo):
      filePath: str
      backingObjectId: Optional[str] = None
      parent: Optional[FileBackingInfo] = None
      deltaSizeInMB: Optional[long] = None
      keyId: Optional[CryptoKeyId] = None
      sharedFileBacking: Optional[bool] = None

   class DiskFileBackingInfo(FileBackingInfo):
      class ProvisioningType(Enum):
         thin: ClassVar['ProvisioningType'] = 'thin'
         eagerZeroedThick: ClassVar['ProvisioningType'] = 'eagerZeroedThick'
         lazyZeroedThick: ClassVar['ProvisioningType'] = 'lazyZeroedThick'

      provisioningType: str

   class RawDiskMappingBackingInfo(FileBackingInfo):
      lunUuid: str
      compatibilityMode: str

   id: ID
   name: str
   createTime: datetime
   keepAfterDeleteVm: Optional[bool] = None
   relocationDisabled: Optional[bool] = None
   nativeSnapshotSupported: Optional[bool] = None
   changedBlockTrackingEnabled: Optional[bool] = None
   backing: BackingInfo
   metadata: list[KeyValue] = []
   vclock: Optional[VClockInfo] = None
   iofilter: list[str] = []


class CloneSpec(MigrateSpec):
   name: str
   keepAfterDeleteVm: Optional[bool] = None
   metadata: list[KeyValue] = []


class CreateSpec(DynamicData):
   class BackingSpec(DynamicData):
      datastore: Datastore
      path: Optional[str] = None

   class DiskFileBackingSpec(BackingSpec):
      provisioningType: Optional[str] = None

   class RawDiskMappingBackingSpec(BackingSpec):
      lunUuid: str
      compatibilityMode: str

   id: Optional[ID] = None
   name: str
   keepAfterDeleteVm: Optional[bool] = None
   backingSpec: BackingSpec
   capacityInMB: long
   profile: list[ProfileSpec] = []
   crypto: Optional[CryptoSpec] = None
   metadata: list[KeyValue] = []


class DiskCryptoSpec(DynamicData):
   parent: Optional[DiskCryptoSpec] = None
   crypto: CryptoSpec

class DiskInfoFlag:
   pass


class ID(DynamicData):
   id: str


class InfrastructureObjectPolicy(DynamicData):
   name: str
   backingObjectId: str
   profileId: str
   error: Optional[MethodFault] = None


class InfrastructureObjectPolicySpec(DynamicData):
   datastore: Datastore
   profile: list[ProfileSpec] = []


class MigrateSpec(DynamicData):
   backingSpec: CreateSpec.BackingSpec
   profile: list[ProfileSpec] = []
   consolidate: Optional[bool] = None
   disksCrypto: Optional[DiskCryptoSpec] = None
   service: Optional[ServiceLocator] = None


class ReconcileResult(DynamicData):
   class InvalidDiskPath(DynamicData):
      path: str
      reason: str

   class ReconcileDetail(DynamicData):
      hostName: Optional[str] = None
      reconcileReportPath: Optional[str] = None
      isReconciled: Optional[bool] = None
      isDeepScanned: Optional[bool] = None
      numberOfReconcileIssues: Optional[int] = None
      numberOfFcdsBeforeReconcile: Optional[int] = None
      numberOfFcdsAfterReconcile: Optional[int] = None
      invalidDiskPaths: list[InvalidDiskPath] = []

   reconcileDetails: list[ReconcileDetail] = []


class ReconcileSpec(DynamicData):
   datastore: Datastore
   includeDiskPaths: list[str] = []
   excludeDiskPaths: list[str] = []
   deepScan: Optional[bool] = None
   dryRun: Optional[bool] = None
   generateReport: Optional[int] = None

class RelocateSpec(MigrateSpec):
   pass


class StateInfo(DynamicData):
   tentative: Optional[bool] = None


class TagEntry(DynamicData):
   tagName: str
   parentCategoryName: str


class VClockInfo(DynamicData):
   vClockTime: long


class VStorageObject(DynamicData):
   class ConsumptionType(Enum):
      disk: ClassVar['ConsumptionType'] = 'disk'

   class ConfigInfo(BaseConfigInfo):
      descriptorVersion: Optional[int] = None
      capacityInMB: long
      consumptionType: list[str] = []
      consumerId: list[ID] = []
      virtualDiskFormat: Optional[str] = None
      linkedCloneBasePath: Optional[str] = None
      linkedCloneParentId: Optional[ID] = None

   config: ConfigInfo


class VStorageObjectAttachResult(DynamicData):
   volumeId: ID
   diskUUID: Optional[str] = None
   fault: Optional[MethodFault] = None


class VStorageObjectAttachSpec(DynamicData):
   volumeId: ID
   datastore: Datastore
   diskMode: Optional[str] = None
   sharing: Optional[str] = None
   controllerKey: Optional[int] = None
   unitNumber: Optional[int] = None

class VStorageObjectControlFlag:
   pass


class VStorageObjectManagerBase(ManagedObject):
   def ExtendDiskEx(self, id: ID, datastore: Datastore, newCapacityInMB: long) -> Task: ...
   def RenameVStorageObjectEx(self, id: ID, datastore: Datastore, name: str) -> VClockInfo: ...
   def CreateSnapshotEx(self, id: ID, datastore: Datastore, description: str, snapshotId: Optional[ID]) -> Task: ...
   def DeleteSnapshotEx(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
   def DeleteSnapshotEx2(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
   def RevertVStorageObjectEx(self, id: ID, datastore: Datastore, snapshotId: ID) -> Task: ...
   def RepairDiskChain(self, id: ID, datastore: Datastore) -> Task: ...
   def UnregisterDisk(self, id: ID, datastore: Datastore) -> Task: ...


class VStorageObjectSnapshot(DynamicData):
   id: ID
   vclock: VClockInfo
   usedCapacity: Optional[long] = None


class VStorageObjectSnapshotDetails(DynamicData):
   path: Optional[str] = None
   changedBlockTrackingId: Optional[str] = None


class VStorageObjectSnapshotInfo(DynamicData):
   class VStorageObjectSnapshot(DynamicData):
      id: Optional[ID] = None
      backingObjectId: Optional[str] = None
      createTime: datetime
      description: str

   snapshots: list[VStorageObjectSnapshot] = []
