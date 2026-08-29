# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import auth as auth
from . import fault as fault
from . import provider as provider
from . import storage as storage

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.sms.auth import SessionManager

from pyVmomi.sms.provider import Provider
from pyVmomi.sms.provider import ProviderSpec
from pyVmomi.sms.provider import VASAProviderUpgradeSpec

from pyVmomi.sms.storage import BackingStoragePool
from pyVmomi.sms.storage import DatastoreBackingPoolMapping
from pyVmomi.sms.storage import DrsMigrationCapabilityResult
from pyVmomi.sms.storage import StorageArray
from pyVmomi.sms.storage import StorageCapability
from pyVmomi.sms.storage import StorageContainerResult
from pyVmomi.sms.storage import StorageContainerSpec
from pyVmomi.sms.storage import StorageFileSystem
from pyVmomi.sms.storage import StorageLun
from pyVmomi.sms.storage import StoragePort
from pyVmomi.sms.storage import StorageProcessor

from pyVmomi.sms.storage.replication import GroupOperationResult

from pyVmomi.vim.vm.replication import FaultDomainId

from pyVmomi.vim.vm.replication import ReplicationGroupId



class AboutInfo(DynamicData):
   name: str
   fullName: str
   vendor: str
   apiVersion: str
   instanceUuid: str
   vasaApiVersion: Optional[str] = None


class EntityReference(DynamicData):
   class EntityType(Enum):
      datacenter: ClassVar['EntityType'] = 'datacenter'
      resourcePool: ClassVar['EntityType'] = 'resourcePool'
      storagePod: ClassVar['EntityType'] = 'storagePod'
      cluster: ClassVar['EntityType'] = 'cluster'
      vm: ClassVar['EntityType'] = 'vm'
      datastore: ClassVar['EntityType'] = 'datastore'
      host: ClassVar['EntityType'] = 'host'
      vmFile: ClassVar['EntityType'] = 'vmFile'
      scsiPath: ClassVar['EntityType'] = 'scsiPath'
      scsiTarget: ClassVar['EntityType'] = 'scsiTarget'
      scsiVolume: ClassVar['EntityType'] = 'scsiVolume'
      scsiAdapter: ClassVar['EntityType'] = 'scsiAdapter'
      nasMount: ClassVar['EntityType'] = 'nasMount'

   id: str
   type: Optional[EntityType] = None


class FaultDomainFilter(DynamicData):
   providerId: Optional[str] = None


class ReplicationGroupFilter(DynamicData):
   groupId: list[ReplicationGroupId] = []


class ServiceInstance(ManagedObject):
   def QueryStorageManager(self) -> StorageManager: ...
   def QuerySessionManager(self) -> SessionManager: ...
   def QueryAboutInfo(self) -> AboutInfo: ...


class StorageManager(ManagedObject):
   def RegisterProvider(self, providerSpec: ProviderSpec) -> Task: ...
   def UnregisterProvider(self, providerId: str) -> Task: ...
   def QueryProvider(self) -> list[Provider]: ...
   def QueryArray(self, providerId: list[str]) -> list[StorageArray]: ...
   def QueryProcessorAssociatedWithArray(self, arrayId: str) -> list[StorageProcessor]: ...
   def QueryPortAssociatedWithArray(self, arrayId: str) -> list[StoragePort]: ...
   def QueryPortAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> Optional[StoragePort]: ...
   def QueryLunAssociatedWithPort(self, portId: str, arrayId: str) -> list[StorageLun]: ...
   def QueryArrayAssociatedWithLun(self, canonicalName: str) -> Optional[StorageArray]: ...
   def QueryPortAssociatedWithProcessor(self, processorId: str, arrayId: str) -> list[StoragePort]: ...
   def QueryLunAssociatedWithArray(self, arrayId: str) -> list[StorageLun]: ...
   def QueryFileSystemAssociatedWithArray(self, arrayId: str) -> list[StorageFileSystem]: ...
   def QueryDatastoreCapability(self, datastore: Datastore) -> Optional[StorageCapability]: ...
   def QueryHostAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> list[HostSystem]: ...
   def QueryVmfsDatastoreAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> Optional[Datastore]: ...
   def QueryNfsDatastoreAssociatedWithFileSystem(self, fileSystemId: str, arrayId: str) -> Optional[Datastore]: ...
   def QueryDrsMigrationCapabilityForPerformance(self, srcDatastore: Datastore, dstDatastore: Datastore) -> bool: ...
   def QueryDrsMigrationCapabilityForPerformanceEx(self, datastore: list[Datastore]) -> DrsMigrationCapabilityResult: ...
   def QueryStorageContainer(self, containerSpec: Optional[StorageContainerSpec]) -> Optional[StorageContainerResult]: ...
   def QueryAssociatedBackingStoragePool(self, entityId: Optional[str], entityType: Optional[str]) -> list[BackingStoragePool]: ...
   def QueryDatastoreBackingPoolMapping(self, datastore: list[Datastore]) -> list[DatastoreBackingPoolMapping]: ...
   def RefreshCACertificatesAndCRLs(self, providerId: list[str]) -> Task: ...
   def QueryFaultDomain(self, filter: Optional[FaultDomainFilter]) -> list[FaultDomainId]: ...
   def QueryReplicationGroupInfo(self, rgFilter: ReplicationGroupFilter) -> list[GroupOperationResult]: ...
   def UpgradeVASAProvider(self, upgradeSpec: VASAProviderUpgradeSpec) -> Task: ...


class Task(ManagedObject):
   def QueryResult(self) -> Optional[object]: ...
   def QueryInfo(self) -> TaskInfo: ...


class TaskInfo(DynamicData):
   class State(Enum):
      queued: ClassVar['State'] = 'queued'
      running: ClassVar['State'] = 'running'
      success: ClassVar['State'] = 'success'
      error: ClassVar['State'] = 'error'

   key: str
   task: Task
   object: Optional[ManagedObject] = None
   error: Optional[MethodFault] = None
   result: Optional[object] = None
   startTime: Optional[datetime] = None
   completionTime: Optional[datetime] = None
   state: str
   progress: Optional[int] = None
