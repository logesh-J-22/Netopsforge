# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import binary

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.cluster import VsanConfigGeneration

from pyVmomi.vim.cluster import VsanUnicastAddressInfo

from pyVmomi.vim.encryption import KmipServerSpec

from pyVmomi.vim.host import DiskDimensions

from pyVmomi.vim.host import MaintenanceSpec
from pyVmomi.vim.host import MountInfo

from pyVmomi.vim.host import ScsiDisk

from pyVmomi.vim.vm import CertThumbprint

from pyVmomi.vim.vsan import AutoRAIDConfig
from pyVmomi.vim.vsan import DataEfficiencyConfig
from pyVmomi.vim.vsan import DataEncryptionConfig
from pyVmomi.vim.vsan import DatastoreConfig
from pyVmomi.vim.vsan import MetricsConfig
from pyVmomi.vim.vsan import RdmaConfig

from pyVmomi.vim.vsan import RepairTimerInfo
from pyVmomi.vim.vsan import ResyncIopsInfo

from pyVmomi.vim.vsan import ServerHostUnicastInfo
from pyVmomi.vim.vsan import SnapServiceConfig
from pyVmomi.vim.vsan import VbossConfig
from pyVmomi.vim.vsan import VsanDeconvergedNetConfig
from pyVmomi.vim.vsan import VsanExtendedConfig
from pyVmomi.vim.vsan import VsanInternalExtendedConfig
from pyVmomi.vim.vsan import VsanUnmapConfig
from pyVmomi.vim.vsan import WitnessHostConfig



class AbortWipeDiskStatus(DynamicData):
   disk: str
   success: bool
   reason: list[LocalizableMessage] = []


class AboutInfoEx(DynamicData):
   name: Optional[str] = None
   version: Optional[str] = None
   build: Optional[str] = None
   buildType: Optional[str] = None
   apiVersion: Optional[str] = None


class AddStoragePoolDiskSpec(DynamicData):
   host: HostSystem
   disks: list[StoragePoolDisk] = []


class ClientClusterUnicastConfig(DynamicData):
   remoteUnicastConfig: list[ClientClusterUnicastInfo] = []


class ClientClusterUnicastInfo(DynamicData):
   clusterUuid: str
   unicastInfo: list[ClientHostUnicastInfo] = []


class ClientHostUnicastInfo(DynamicData):
   hostUuid: str
   unicastSpec: list[VsanUnicastAddressInfo] = []
   thumbprintList: list[CertThumbprint] = []


class ClusterStatus(DynamicData):
   class State(DynamicData):
      class CompletionEstimate(DynamicData):
         completeTime: Optional[datetime] = None
         percentComplete: Optional[int] = None

      state: str
      completion: Optional[CompletionEstimate] = None

   uuid: Optional[str] = None
   nodeUuid: Optional[str] = None
   health: str
   nodeState: State
   memberUuid: list[str] = []


class ComplianceDetail(DynamicData):
   objectUUID: str
   complianceStatus: str
   objectHealth: int
   violatedPolicies: list[PolicyStatus] = []


class ComplianceResult(DynamicData):
   checkTime: datetime
   policyId: Optional[str] = None
   policyGen: Optional[int] = None
   objComplianceDetail: list[ComplianceDetail] = []

class ComplianceStatus:
   pass


class ConfigInfo(DynamicData):
   class StorageInfo(DynamicData):
      autoClaimStorage: Optional[bool] = None
      diskMapping: list[DiskMapping] = []
      diskMapInfo: list[DiskMapInfo] = []
      checksumEnabled: Optional[bool] = None

   class ClusterInfo(DynamicData):
      uuid: Optional[str] = None
      nodeUuid: Optional[str] = None

   class NetworkInfo(DynamicData):
      class PortConfig(DynamicData):
         ipConfig: Optional[IpConfig] = None
         device: str

      port: list[PortConfig] = []

   class FaultDomainInfo(DynamicData):
      name: str

   enabled: Optional[bool] = None
   hostSystem: Optional[HostSystem] = None
   clusterInfo: Optional[ClusterInfo] = None
   storageInfo: Optional[StorageInfo] = None
   networkInfo: Optional[NetworkInfo] = None
   faultDomainInfo: Optional[FaultDomainInfo] = None
   vsanEsaEnabled: Optional[bool] = None
   vsanCyberRecoveryEnabled: Optional[bool] = None


class ConfigInfoEx(ConfigInfo):
   encryptionInfo: Optional[EncryptionInfo] = None
   dataEfficiencyInfo: Optional[DataEfficiencyConfig] = None
   resyncIopsLimitInfo: Optional[ResyncIopsInfo] = None
   extendedConfig: Optional[VsanExtendedConfig] = None
   datastoreInfo: Optional[DatastoreConfig] = None
   unmapConfig: Optional[VsanUnmapConfig] = None
   witnessHostConfig: list[WitnessHostConfig] = []
   internalExtendedConfig: Optional[VsanInternalExtendedConfig] = None
   metricsConfig: Optional[MetricsConfig] = None
   unicastConfig: Optional[ServerClusterUnicastConfig] = None
   rdmaConfig: Optional[RdmaConfig] = None
   dataInTransitEncryptionInfo: Optional[DataInTransitEncryptionInfo] = None
   mode: Optional[str] = None
   serverClusterConfigs: list[RemoteVsanServerClusterConfig] = []
   snapServiceConfig: Optional[SnapServiceConfig] = None
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None
   remoteDITInfos: list[DataInTransitEncryptionInfo] = []
   clientUnicastConfig: Optional[ClientClusterUnicastConfig] = None
   siteTakeoverConfig: Optional[SiteTakeoverConfig] = None
   vbossHostConfig: Optional[VbossHostConfig] = None
   autoRAIDConfig: Optional[AutoRAIDConfig] = None


class CreateNativeKeyProviderSpec(DynamicData):
   provider: str
   keyId: Optional[str] = None
   keyDerivationKey: Optional[str] = None
   tpmRequired: Optional[bool] = None


class DataInTransitEncryptionInfo(DynamicData):
   enabled: Optional[bool] = None
   rekeyInterval: Optional[int] = None
   transitionState: Optional[str] = None
   serverClusterUuid: Optional[str] = None
   clientClusterUuid: Optional[str] = None


class DecommissionMode(DynamicData):
   class ObjectAction(Enum):
      noAction: ClassVar['ObjectAction'] = 'noAction'
      ensureObjectAccessibility: ClassVar['ObjectAction'] = 'ensureObjectAccessibility'
      evacuateAllData: ClassVar['ObjectAction'] = 'evacuateAllData'

   objectAction: str


class DeleteStoragePoolDiskSpec(DynamicData):
   diskUuids: list[str] = []
   maintenanceSpec: MaintenanceSpec


class DiskMapInfo(DynamicData):
   mapping: DiskMapping
   mounted: bool


class DiskMapInfoEx(DynamicData):
   mapping: DiskMapping
   isMounted: bool
   unlockedEncrypted: Optional[bool] = None
   isAllFlash: bool
   isDataEfficiency: Optional[bool] = None
   encryptionInfo: Optional[DataEncryptionConfig] = None
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   diskgroupCapability: list[str] = []


class DiskMapResult(DynamicData):
   mapping: DiskMapping
   diskResult: list[DiskResult] = []
   error: Optional[MethodFault] = None


class DiskMapping(DynamicData):
   ssd: ScsiDisk
   nonSsd: list[ScsiDisk] = []


class DiskMappingCreationSpec(DynamicData):
   class DiskMappingCreationType(Enum):
      hybrid: ClassVar['DiskMappingCreationType'] = 'hybrid'
      allFlash: ClassVar['DiskMappingCreationType'] = 'allFlash'
      vsandirect: ClassVar['DiskMappingCreationType'] = 'vsandirect'
      pmem: ClassVar['DiskMappingCreationType'] = 'pmem'
      DiskMappingCreationType_Unknown: ClassVar['DiskMappingCreationType'] = 'DiskMappingCreationType_Unknown'

   host: HostSystem
   cacheDisks: list[ScsiDisk] = []
   capacityDisks: list[ScsiDisk] = []
   creationType: str


class DiskResult(DynamicData):
   class State(Enum):
      inUse: ClassVar['State'] = 'inUse'
      eligible: ClassVar['State'] = 'eligible'
      ineligible: ClassVar['State'] = 'ineligible'

   disk: ScsiDisk
   state: str
   vsanUuid: Optional[str] = None
   error: Optional[MethodFault] = None
   degraded: Optional[bool] = None


class DiskResultEx(DiskResult):
   vsanDirectTagged: bool
   storagePoolDiskState: Optional[str] = None
   storagePoolDiskError: Optional[MethodFault] = None
   isCapacityFlash: Optional[bool] = None


class DrsStats(DynamicData):
   host: HostSystem
   stats: binary
   readLocalityPresented: Optional[bool] = None


class EncryptionInfo(DynamicData):
   enabled: Optional[bool] = None
   kekId: Optional[str] = None
   hostKeyId: Optional[str] = None
   kmipServers: list[KmipServerSpec] = []
   kmsServerCerts: list[str] = []
   clientKey: Optional[str] = None
   clientCert: Optional[str] = None
   dekGenerationId: Optional[long] = None
   changing: Optional[bool] = None
   eraseDisksBeforeUse: Optional[bool] = None
   wrappedDek: Optional[str] = None
   dekId: Optional[str] = None
   oldWrappedDek: Optional[str] = None
   oldDekId: Optional[str] = None
   kekVerifier: Optional[str] = None
   dekVerifier: Optional[str] = None
   oldDekVerifier: Optional[str] = None
   iv: Optional[str] = None
   syncing: Optional[bool] = None

class EncryptionOperation:
   pass

class EncryptionTransitionState:
   pass

class HealthState:
   pass


class IpConfig(DynamicData):
   upstreamIpAddress: str
   downstreamIpAddress: str


class IpConfigEx(IpConfig):
   upstreamIpV6Address: Optional[str] = None
   downstreamIpV6Address: Optional[str] = None


class MembershipInfo(DynamicData):
   nodeUuid: str
   hostname: str

class NodeState:
   pass


class PolicyStatus(DynamicData):
   id: str
   expectedValue: str
   currentValue: str


class PortConfigEx(ConfigInfo.NetworkInfo.PortConfig):
   class TrafficType(Enum):
      vsan: ClassVar['TrafficType'] = 'vsan'
      witness: ClassVar['TrafficType'] = 'witness'
      TrafficType_Unknown: ClassVar['TrafficType'] = 'TrafficType_Unknown'

   class TrafficType90(Enum):
      vsanExternal: ClassVar['TrafficType90'] = 'vsanExternal'

   trafficTypes: list[str] = []


class QueryVsanDisksSpec(DynamicData):
   diskName: Optional[str] = None
   vsanDiskType: Optional[str] = None


class RemoteVsanServerClusterConfig(DynamicData):
   clusterUuid: str
   siteAffinity: Optional[SiteAffinityInfo] = None


class RuntimeStats(DynamicData):
   resyncIopsInfo: Optional[ResyncIopsInfo] = None
   configGeneration: Optional[VsanConfigGeneration] = None
   supportedClusterSize: Optional[int] = None
   repairTimerInfo: Optional[RepairTimerInfo] = None
   componentLimitPerCluster: Optional[int] = None
   maxWitnessClusters: Optional[int] = None


class ServerClusterUnicastConfig(DynamicData):
   remoteUnicastConfig: list[ServerClusterUnicastInfo] = []


class ServerClusterUnicastInfo(DynamicData):
   clusterUuid: str
   unicastInfo: list[ServerHostUnicastInfo] = []

class ServerNodeType:
   pass


class SiteAffinityInfo(DynamicData):
   name: str
   siteId: Optional[str] = None


class SiteTakeoverConfig(DynamicData):
   takeoverTimestamp: Optional[long] = None

class StatsType:
   pass


class StoragePoolDisk(DynamicData):
   diskName: str
   diskType: str


class StoragePoolDiskInfo(DynamicData):
   disk: ScsiDisk
   vsanUuid: Optional[str] = None
   error: Optional[MethodFault] = None
   isMounted: Optional[bool] = None
   isEncrypted: Optional[bool] = None
   dekId: Optional[str] = None
   diskType: Optional[str] = None

class StoragePoolDiskType:
   pass


class StoragePoolInfo(DynamicData):
   storagePoolDisks: list[StoragePoolDiskInfo] = []


class TrimDiskEntry(DynamicData):
   diskName: str
   diskType: Optional[str] = None


class TrimDiskSpec(DynamicData):
   disks: list[TrimDiskEntry] = []

class TrimDiskType:
   pass


class UpdateStoragePoolDiskSpec(DynamicData):
   diskUuids: list[str] = []
   diskFormatVersion: Optional[long] = None


class VbossHostConfig(VbossConfig):
   pass


class VsanAssociatedObjects(DynamicData):
   spbmProfileId: str
   spbmProfileGenerationNum: int
   vsanObjects: list[str] = []


class VsanAssociatedObjectsResult(DynamicData):
   data: list[VsanAssociatedObjects] = []
   offset: int
   limit: int


class VsanComplianceQuerySpec(DynamicData):
   uuids: list[str] = []
   spbmProfileId: Optional[str] = None
   spbmProfileGenerationId: Optional[int] = None


class VsanComponentSyncState(DynamicData):
   uuid: str
   diskUuid: str
   hostUuid: str
   bytesToSync: long
   recoveryETA: Optional[long] = None
   reasons: list[str] = []


class VsanDirectStorage(DynamicData):
   scsiDisks: list[VsanScsiDisk] = []
   tier: Optional[str] = None

class VsanDiskEvacReason:
   pass


class VsanDiskInfo(DynamicData):
   vsanUuid: str
   formatVersion: int


class VsanDiskManagementSystemCapability(DynamicData):
   version: str

class VsanDiskTrimOption:
   pass

class VsanDiskType:
   pass

class VsanDiskgroupCapability:
   pass


class VsanHostCapability(DynamicData):
   host: HostSystem
   isSupported: bool
   isLicensed: bool


class VsanManagedDisksInfo(DynamicData):
   vSANDirectDisks: list[VsanDirectStorage] = []
   vSANDiskMapInfo: list[DiskMapInfoEx] = []
   vSANPMemInfo: Optional[VsanManagedPMemInfo] = None
   storagePools: list[StoragePoolInfo] = []


class VsanManagedPMemInfo(DynamicData):
   localPMemDatastores: list[Datastore] = []


class VsanObjectProfileInfo(DynamicData):
   vsanObjectUuid: str
   spbmProfileId: str
   spbmProfileGenerationNum: int


class VsanObjectSyncState(DynamicData):
   uuid: str
   components: list[VsanComponentSyncState] = []


class VsanRuntimeInfo(DynamicData):
   class DiskIssueType(Enum):
      nonExist: ClassVar['DiskIssueType'] = 'nonExist'
      stampMismatch: ClassVar['DiskIssueType'] = 'stampMismatch'
      unknown: ClassVar['DiskIssueType'] = 'unknown'

   class DiskIssue(DynamicData):
      diskId: str
      issue: str

   membershipList: list[MembershipInfo] = []
   diskIssues: list[DiskIssue] = []
   accessGenNo: Optional[int] = None


class VsanScsiDisk(DynamicData):
   capacity: DiskDimensions.Lba
   usedCapacity: Optional[long] = None
   devicePath: str
   ssd: Optional[bool] = None
   localDisk: Optional[bool] = None
   scsiDiskType: Optional[str] = None
   uuid: str
   operationalState: list[str] = []
   canonicalName: Optional[str] = None
   displayName: Optional[str] = None
   lunType: str
   vendor: Optional[str] = None
   model: Optional[str] = None
   mountInfo: Optional[MountInfo] = None


class VsanSyncingObjectQueryResult(DynamicData):
   totalObjectsToSync: Optional[long] = None
   totalBytesToSync: Optional[long] = None
   totalRecoveryETA: Optional[long] = None
   objects: list[VsanObjectSyncState] = []
   syncingObjectRecoveryDetails: Optional[VsanSyncingObjectRecoveryDetails] = None


class VsanSyncingObjectRecoveryDetails(DynamicData):
   activelySyncingObjectRecoveryETA: Optional[long] = None
   queuedForSyncObjectRecoveryETA: Optional[long] = None
   suspendedObjectRecoveryETA: Optional[long] = None
   activeObjectsToSync: Optional[long] = None
   queuedObjectsToSync: Optional[long] = None
   suspendedObjectsToSync: Optional[long] = None
   bytesToSyncForActiveObjects: Optional[long] = None
   bytesToSyncForQueuedObjects: Optional[long] = None
   bytesToSyncForSuspendedObjects: Optional[long] = None


class VsanWhatIfEvacDetail(DynamicData):
   success: Optional[bool] = None
   bytesToSync: Optional[long] = None
   inaccessibleObjects: list[str] = []
   incompliantObjects: list[str] = []
   extraSpaceNeeded: Optional[long] = None
   failedDueToInaccessibleObjects: Optional[bool] = None


class VsanWhatIfEvacResult(DynamicData):
   noAction: VsanWhatIfEvacDetail
   ensureAccess: VsanWhatIfEvacDetail
   evacAllData: VsanWhatIfEvacDetail

class WipeDiskEligible:
   pass

class WipeDiskState:
   pass


class WipeDiskStatus(DynamicData):
   disk: str
   eligible: str
   ineligibleReason: list[LocalizableMessage] = []
   wipeState: Optional[str] = None
   percentageCompleted: Optional[int] = None
   estimatedTime: Optional[long] = None
   wipeStartTime: Optional[datetime] = None
   wipeCompleteTime: Optional[datetime] = None
