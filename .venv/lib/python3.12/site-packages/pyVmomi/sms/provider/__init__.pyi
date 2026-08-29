# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.sms.storage import StorageAlarm

from pyVmomi.sms.storage.replication import FailoverParam
from pyVmomi.sms.storage.replication import GroupOperationResult
from pyVmomi.sms.storage.replication import PromoteParam
from pyVmomi.sms.storage.replication import QueryPointInTimeReplicaParam
from pyVmomi.sms.storage.replication import QueryReplicationPeerResult
from pyVmomi.sms.storage.replication import TestFailoverParam

from pyVmomi.vim.vm.replication import FaultDomainId
from pyVmomi.vim.vm.replication import ReplicationGroupId



class AlarmFilter(DynamicData):
   alarmStatus: Optional[str] = None
   alarmType: Optional[str] = None
   entityType: Optional[str] = None
   entityId: list[object] = []
   pageMarker: Optional[str] = None


class AlarmResult(DynamicData):
   storageAlarm: list[StorageAlarm] = []
   pageMarker: Optional[str] = None


class Provider(ManagedObject):
   def QueryProviderInfo(self) -> ProviderInfo: ...


class ProviderInfo(DynamicData):
   uid: str
   name: str
   description: Optional[str] = None
   version: Optional[str] = None


class ProviderSpec(DynamicData):
   name: str
   description: Optional[str] = None


class VASAProviderUpgradeSpec(DynamicData):
   providerUid: str
   username: str
   password: str


class VasaProvider(Provider):
   def Sync(self, arrayId: Optional[str]) -> Task: ...
   def RefreshCertificate(self) -> Task: ...
   def RevokeCertificate(self) -> Task: ...
   def Reconnect(self) -> Task: ...
   def QueryReplicationPeer(self, faultDomainId: list[FaultDomainId]) -> list[QueryReplicationPeerResult]: ...
   def QueryReplicationGroup(self, groupId: list[ReplicationGroupId]) -> list[GroupOperationResult]: ...
   def QueryPointInTimeReplica(self, groupId: list[ReplicationGroupId], queryParam: Optional[QueryPointInTimeReplicaParam]) -> list[GroupOperationResult]: ...
   def TestFailoverReplicationGroupStart(self, testFailoverParam: TestFailoverParam) -> Task: ...
   def TestFailoverReplicationGroupStop(self, groupId: list[ReplicationGroupId], force: bool) -> Task: ...
   def PromoteReplicationGroup(self, promoteParam: PromoteParam) -> Task: ...
   def SyncReplicationGroup(self, groupId: list[ReplicationGroupId], pitName: str) -> Task: ...
   def PrepareFailoverReplicationGroup(self, groupId: list[ReplicationGroupId]) -> Task: ...
   def FailoverReplicationGroup(self, failoverParam: FailoverParam) -> Task: ...
   def ReverseReplicateGroup(self, groupId: list[ReplicationGroupId]) -> Task: ...
   def QueryActiveAlarm(self, alarmFilter: Optional[AlarmFilter]) -> Optional[AlarmResult]: ...


class VasaProviderInfo(ProviderInfo):
   class CertificateStatus(Enum):
      valid: ClassVar['CertificateStatus'] = 'valid'
      expirySoftLimitReached: ClassVar['CertificateStatus'] = 'expirySoftLimitReached'
      expiryHardLimitReached: ClassVar['CertificateStatus'] = 'expiryHardLimitReached'
      expired: ClassVar['CertificateStatus'] = 'expired'
      invalid: ClassVar['CertificateStatus'] = 'invalid'

   class RelatedStorageArray(DynamicData):
      arrayId: str
      active: bool
      manageable: bool
      priority: int

   class SupportedVendorModelMapping(DynamicData):
      vendorId: Optional[str] = None
      modelId: Optional[str] = None

   class VasaProviderStatus(Enum):
      online: ClassVar['VasaProviderStatus'] = 'online'
      offline: ClassVar['VasaProviderStatus'] = 'offline'
      syncError: ClassVar['VasaProviderStatus'] = 'syncError'
      unknown: ClassVar['VasaProviderStatus'] = 'unknown'
      connected: ClassVar['VasaProviderStatus'] = 'connected'
      disconnected: ClassVar['VasaProviderStatus'] = 'disconnected'

   class VasaProviderProfile(Enum):
      blockDevice: ClassVar['VasaProviderProfile'] = 'blockDevice'
      fileSystem: ClassVar['VasaProviderProfile'] = 'fileSystem'
      capability: ClassVar['VasaProviderProfile'] = 'capability'

   class ProviderProfile(Enum):
      ProfileBasedManagement: ClassVar['ProviderProfile'] = 'ProfileBasedManagement'
      Replication: ClassVar['ProviderProfile'] = 'Replication'

   class Type(Enum):
      PERSISTENCE: ClassVar['Type'] = 'PERSISTENCE'
      DATASERVICE: ClassVar['Type'] = 'DATASERVICE'
      UNKNOWN: ClassVar['Type'] = 'UNKNOWN'

   class Category(Enum):
      internal: ClassVar['Category'] = 'internal'
      external: ClassVar['Category'] = 'external'

   url: str
   certificate: Optional[str] = None
   status: Optional[str] = None
   statusFault: Optional[MethodFault] = None
   vasaVersion: Optional[str] = None
   namespace: Optional[str] = None
   lastSyncTime: Optional[str] = None
   supportedVendorModelMapping: list[SupportedVendorModelMapping] = []
   supportedProfile: list[str] = []
   supportedProviderProfile: list[str] = []
   relatedStorageArray: list[RelatedStorageArray] = []
   providerId: Optional[str] = None
   certificateExpiryDate: Optional[str] = None
   certificateStatus: Optional[str] = None
   serviceLocation: Optional[str] = None
   needsExplicitActivation: Optional[bool] = None
   maxBatchSize: Optional[long] = None
   retainVasaProviderCertificate: Optional[bool] = None
   arrayIndependentProvider: Optional[bool] = None
   type: Optional[str] = None
   category: Optional[str] = None
   priority: Optional[int] = None
   failoverGroupId: Optional[str] = None


class VasaProviderSpec(ProviderSpec):
   username: str
   password: str
   url: str
   certificate: Optional[str] = None
