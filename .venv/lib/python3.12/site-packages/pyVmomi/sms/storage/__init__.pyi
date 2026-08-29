# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import replication as replication

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore

from pyVmomi.vim import VasaStorageArray

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.provider import Provider

from pyVmomi.sms.provider import ProviderInfo

from pyVmomi.vim.host import HostBusAdapter

from pyVmomi.vim.vm.replication import FaultDomainId


class AlarmStatus:
   pass

class AlarmType:
   pass


class BackingConfig(DynamicData):
   thinProvisionBackingIdentifier: Optional[str] = None
   deduplicationBackingIdentifier: Optional[str] = None
   autoTieringEnabled: Optional[bool] = None
   deduplicationEfficiency: Optional[long] = None
   performanceOptimizationInterval: Optional[long] = None


class BackingStoragePool(DynamicData):
   class BackingStoragePoolType(Enum):
      thinProvisioningPool: ClassVar['BackingStoragePoolType'] = 'thinProvisioningPool'
      deduplicationPool: ClassVar['BackingStoragePoolType'] = 'deduplicationPool'
      thinAndDeduplicationCombinedPool: ClassVar['BackingStoragePoolType'] = 'thinAndDeduplicationCombinedPool'

   uuid: str
   type: str
   capacityInMB: long
   usedSpaceInMB: long


class DatastoreBackingPoolMapping(DynamicData):
   datastore: list[Datastore] = []
   backingStoragePool: list[BackingStoragePool] = []


class DatastorePair(DynamicData):
   datastore1: Datastore
   datastore2: Datastore


class DrsMigrationCapabilityResult(DynamicData):
   recommendedDatastorePair: list[DatastorePair] = []
   nonRecommendedDatastorePair: list[DatastorePair] = []

class EntityType:
   pass


class FaultDomainProviderMapping(DynamicData):
   activeProvider: Provider
   faultDomainId: list[FaultDomainId] = []

class FcStoragePort(StoragePort):
   portWwn: str
   nodeWwn: str

class FcoeStoragePort(StoragePort):
   portWwn: str
   nodeWwn: str


class FileSystemInfo(DynamicData):
   fileServerName: str
   fileSystemPath: str
   ipAddress: Optional[str] = None

class IscsiStoragePort(StoragePort):
   identifier: str


class LunHbaAssociation(DynamicData):
   canonicalName: str
   hba: list[HostBusAdapter] = []


class NameValuePair(DynamicData):
   parameterName: str
   parameterValue: str


class StorageAlarm(DynamicData):
   alarmId: long
   alarmType: str
   containerId: Optional[str] = None
   objectId: Optional[str] = None
   objectType: str
   status: str
   alarmTimeStamp: datetime
   messageId: str
   parameterList: list[NameValuePair] = []
   alarmObject: Optional[object] = None


class StorageArray(DynamicData):
   class BlockDeviceInterface(Enum):
      fc: ClassVar['BlockDeviceInterface'] = 'fc'
      iscsi: ClassVar['BlockDeviceInterface'] = 'iscsi'
      fcoe: ClassVar['BlockDeviceInterface'] = 'fcoe'
      otherBlock: ClassVar['BlockDeviceInterface'] = 'otherBlock'

   class FileSystemInterface(Enum):
      nfs: ClassVar['FileSystemInterface'] = 'nfs'
      otherFileSystem: ClassVar['FileSystemInterface'] = 'otherFileSystem'

   class VasaProfile(Enum):
      blockDevice: ClassVar['VasaProfile'] = 'blockDevice'
      fileSystem: ClassVar['VasaProfile'] = 'fileSystem'
      capability: ClassVar['VasaProfile'] = 'capability'
      policy: ClassVar['VasaProfile'] = 'policy'
      object: ClassVar['VasaProfile'] = 'object'
      statistics: ClassVar['VasaProfile'] = 'statistics'
      storageDrsBlockDevice: ClassVar['VasaProfile'] = 'storageDrsBlockDevice'
      storageDrsFileSystem: ClassVar['VasaProfile'] = 'storageDrsFileSystem'

   name: str
   uuid: str
   vendorId: str
   modelId: str
   firmware: Optional[str] = None
   alternateName: list[str] = []
   supportedBlockInterface: list[str] = []
   supportedFileSystemInterface: list[str] = []
   supportedProfile: list[str] = []
   priority: Optional[int] = None
   discoverySvc: list[VasaStorageArray.DiscoverySvcInfo] = []


class StorageCapability(DynamicData):
   uuid: str
   name: str
   description: str


class StorageContainer(DynamicData):
   class VvolContainerTypeEnum(Enum):
      NFS: ClassVar['VvolContainerTypeEnum'] = 'NFS'
      NFS4x: ClassVar['VvolContainerTypeEnum'] = 'NFS4x'
      SCSI: ClassVar['VvolContainerTypeEnum'] = 'SCSI'
      NVMe: ClassVar['VvolContainerTypeEnum'] = 'NVMe'

   uuid: str
   name: str
   maxVvolSizeInMB: long
   providerId: list[str] = []
   arrayId: list[str] = []
   vvolContainerType: Optional[str] = None
   stretched: Optional[bool] = None


class StorageContainerResult(DynamicData):
   storageContainer: list[StorageContainer] = []
   providerInfo: list[ProviderInfo] = []


class StorageContainerSpec(DynamicData):
   containerId: list[str] = []


class StorageFileSystem(DynamicData):
   class FileSystemInterfaceVersion(Enum):
      NFSV3_0: ClassVar['FileSystemInterfaceVersion'] = 'NFSV3_0'

   uuid: str
   info: list[FileSystemInfo] = []
   nativeSnapshotSupported: bool
   thinProvisioningStatus: str
   type: str
   version: str
   backingConfig: Optional[BackingConfig] = None


class StorageLun(DynamicData):
   uuid: str
   vSphereLunIdentifier: str
   vendorDisplayName: str
   capacityInMB: long
   usedSpaceInMB: long
   lunThinProvisioned: bool
   alternateIdentifier: list[str] = []
   drsManagementPermitted: bool
   thinProvisioningStatus: str
   backingConfig: Optional[BackingConfig] = None


class StoragePort(DynamicData):
   uuid: str
   type: str
   alternateName: list[str] = []


class StorageProcessor(DynamicData):
   uuid: str
   alternateIdentifer: list[str] = []

class ThinProvisioningStatus:
   pass
