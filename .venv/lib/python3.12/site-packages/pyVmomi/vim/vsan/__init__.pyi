# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import cluster as cluster
from . import host as host
from . import upgradesystem as upgradesystem

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import long
from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vim import ComputeResource

from pyVmomi.vim import Datastore

from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import HostSystem

from pyVmomi.vim import KeyValue

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim import Network

from pyVmomi.vim import SDDCBase

from pyVmomi.vim import Task

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicArray
from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.cluster import SiteFaultDomainConfig

from pyVmomi.vim.cluster import VsanClusterHealthSummary

from pyVmomi.vim.cluster import VsanDiskMappingsConfigSpec
from pyVmomi.vim.cluster import VsanFaultDomainsConfigSpec
from pyVmomi.vim.cluster import VsanHistoricalHealthQuerySpec
from pyVmomi.vim.cluster import VsanIscsiTargetServiceConfig
from pyVmomi.vim.cluster import VsanIscsiTargetServiceSpec

from pyVmomi.vim.cluster import VsanObjectInformation
from pyVmomi.vim.cluster import VsanPerfNodeInformation
from pyVmomi.vim.cluster import VsanPerfsvcConfig

from pyVmomi.vim.cluster import VsanStretchedClusterConfig

from pyVmomi.vim.cluster import VsanUnicastAddressInfo

from pyVmomi.vim.dvs import DistributedVirtualPortgroup

from pyVmomi.vim.dvs import VmwareDistributedVirtualSwitch

from pyVmomi.vim.encryption import KeyProviderId

from pyVmomi.vim.host import ConnectSpec

from pyVmomi.vim.host import IpConfig

from pyVmomi.vim.host import MaintenanceSpec

from pyVmomi.vim.host import VsanBasicDeviceInfo

from pyVmomi.vim.host import VsanHclFirmwareUpdateSpec

from pyVmomi.vim.host import VsanHwToVcgInfoMapping

from pyVmomi.vim.vm import CertThumbprint

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vm.device import VirtualDevice

from pyVmomi.vim.vsan.cluster import ConfigInfo
from pyVmomi.vim.vsan.cluster import VbossClusterConfig

from pyVmomi.vim.vsan.host import AddStoragePoolDiskSpec

from pyVmomi.vim.vsan.host import ClientClusterUnicastInfo
from pyVmomi.vim.vsan.host import CreateNativeKeyProviderSpec
from pyVmomi.vim.vsan.host import DeleteStoragePoolDiskSpec
from pyVmomi.vim.vsan.host import DiskMapping
from pyVmomi.vim.vsan.host import DiskMappingCreationSpec
from pyVmomi.vim.vsan.host import EncryptionInfo

from pyVmomi.vim.vsan.host import RuntimeStats



class ActiveDirectoryServerConfig(DirectoryServerConfig):
   activeDirectoryDomainName: Optional[str] = None
   username: Optional[str] = None
   password: Optional[str] = None
   organizationalUnit: Optional[str] = None
   preferredADServers: list[str] = []


class AdvancedDatastoreConfig(DatastoreConfig):
   remoteDatastores: list[Datastore] = []


class AutoRAIDConfig(DynamicData):
   assumeAutoManagedRAID: bool


class AutoRAIDInfo(DynamicData):
   hostFailuresToTolerate: long
   subFailuresToTolerate: Optional[long] = None


class CapacityReservationInfo(DynamicData):
   hostRebuildThreshold: Optional[str] = None
   vsanOpSpaceThreshold: Optional[str] = None

class CapacityReservationState:
   pass


class ClientDatastoreConfig(DatastoreSpec):
   clusters: list[ClusterComputeResource] = []


class ClientUnicastConfig(DynamicData):
   unicastInfo: list[ClientClusterUnicastInfo] = []


class ClusterConfigPrecheckItem(ClusterComputeResource.ValidationResultBase):
   status: str
   description: Optional[LocalizableMessage] = None


class ClusterRuntimeInfo(DynamicData):
   clusterUuid: str
   totalComponentsCount: int
   cluster: Optional[ClusterComputeResource] = None


class CompatibilityCheckResult(DynamicData):
   status: str
   message: Optional[LocalizableMessage] = None


class ConfigInfoEx(ConfigInfo):
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   resyncIopsLimitConfig: Optional[ResyncIopsInfo] = None
   iscsiConfig: Optional[VsanIscsiTargetServiceConfig] = None
   dataEncryptionConfig: Optional[DataEncryptionConfig] = None
   extendedConfig: Optional[VsanExtendedConfig] = None
   datastoreConfig: Optional[DatastoreConfig] = None
   perfsvcConfig: Optional[VsanPerfsvcConfig] = None
   unmapConfig: Optional[VsanUnmapConfig] = None
   vumConfig: Optional[VsanVumConfig] = None
   fileServiceConfig: Optional[FileServiceConfig] = None
   metricsConfig: Optional[MetricsConfig] = None
   rdmaConfig: Optional[RdmaConfig] = None
   dataInTransitEncryptionConfig: Optional[DataInTransitEncryptionConfig] = None
   vsanHealthConfig: Optional[VsanHealthConfigSpec] = None
   mode: Optional[str] = None
   vsanPMemConfig: Optional[VsanPMemConfig] = None
   vsanEsaConfigInfo: Optional[VsanEsaConfigInfo] = None
   xvcDatastoreConfig: Optional[XVCDatastoreConfig] = None
   serverClusterConfig: Optional[VcRemoteVsanServerClusterConfig] = None
   datastoreDefaultPolicySelectionConfig: Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   snapServiceConfig: Optional[SnapServiceConfig] = None
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None
   siteFaultDomainConfig: Optional[SiteFaultDomainConfig] = None
   vbossClusterConfig: Optional[VbossClusterConfig] = None


class CyberRecoveryConfig(DynamicData):
   enabled: bool


class DataEfficiencyCapacityState(DynamicData):
   logicalCapacity: Optional[long] = None
   logicalCapacityUsed: Optional[long] = None
   physicalCapacity: Optional[long] = None
   physicalCapacityUsed: Optional[long] = None
   dedupMetadataSize: Optional[long] = None
   spaceEfficiencyMetadataSize: Optional[VsanSpaceEfficiencyMetadataSize] = None
   esaDedupSpaceSaving: Optional[long] = None
   esaCompressionSpaceSaving: Optional[long] = None
   totalSpaceUsedWithoutOverhead: Optional[long] = None
   dedupEnabledObjectSpaceUsed: Optional[long] = None


class DataEfficiencyConfig(DynamicData):
   dedupEnabled: bool
   compressionEnabled: Optional[bool] = None


class DataEfficiencyConfigEx(DataEfficiencyConfig):
   dedupStoreUuid: Optional[str] = None
   dedupPaused: Optional[bool] = None


class DataEncryptionConfig(DynamicData):
   encryptionEnabled: bool
   kmsProviderId: Optional[KeyProviderId] = None
   kekId: Optional[str] = None
   hostKeyId: Optional[str] = None
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


class DataInTransitEncryptionConfig(DynamicData):
   enabled: Optional[bool] = None
   rekeyInterval: Optional[int] = None
   state: Optional[str] = None


class DataProtectionHealthSystem(ManagedObject):
   def QueryHealthSummary(self, cluster: ClusterComputeResource) -> VsanClusterHealthSummary: ...
   def QueryHistoricalHealth(self, spec: VsanHistoricalHealthQuerySpec) -> list[VsanClusterHealthSummary]: ...
   def GetDpClusterSilentChecks(self, cluster: ClusterComputeResource) -> list[str]: ...
   def SetDpClusterSilentChecks(self, cluster: ClusterComputeResource, addSilentChecks: list[str], removeSilentChecks: list[str]) -> bool: ...


class DatastoreConfig(DynamicData):
   datastores: list[DatastoreSpec] = []

class DatastoreSourcePrecheckItem(MountPrecheckItem):
   pass

class DatastoreSourcePrecheckResult(MountPrecheckResult):
   pass


class DatastoreSpec(DynamicData):
   uuid: str
   name: str


class DefaultDatastorePolicySelectionInfo(DynamicData):
   enabled: bool
   defaultPolicyId: Optional[str] = None
   lastPolicySelectionTime: Optional[datetime] = None


class DirectoryServerConfig(DynamicData):
   pass


class DiskClaimConfiguration(DynamicData):
   diskType: str
   diskNamePrefix: Optional[str] = None
   numberOfDisks: Optional[int] = None
   diskModel: Optional[str] = None
   vendor: Optional[str] = None
   diskCapacity: Optional[long] = None


class DiskDataEvacuationResourceCheckTaskDetails(ResourceCheckTaskDetails):
   diskUuid: Optional[str] = None
   isCapacityTier: Optional[bool] = None


class DiskGroupResourceCheckResult(EntityResourceCheckDetails):
   cacheTierDisk: Optional[DiskResourceCheckResult] = None
   capacityTierDisks: list[DiskResourceCheckResult] = []


class DiskInfo(DynamicData):
   diskUuid: str
   diskName: str
   isSsd: Optional[bool] = None

class DiskResourceCheckResult(EntityResourceCheckDetails):
   pass


class DpDaemonHealth(DynamicData):
   host: HostSystem
   name: str
   status: str


class EntityCompatibilityResult(DynamicData):
   entity: ManagedEntity
   compatible: bool
   incompatibleReasons: list[LocalizableMessage] = []
   extendedAttributes: list[KeyAnyValue] = []


class EntityResourceCheckDetails(DynamicData):
   name: Optional[str] = None
   uuid: Optional[str] = None
   isNew: Optional[bool] = None
   capacity: Optional[long] = None
   postOperationCapacity: Optional[long] = None
   usedCapacity: Optional[long] = None
   postOperationUsedCapacity: Optional[long] = None
   additionalRequiredCapacity: Optional[long] = None
   maxComponents: Optional[long] = None
   components: Optional[long] = None


class FaultDomainResourceCheckResult(EntityResourceCheckDetails):
   hosts: list[HostResourceCheckResult] = []


class FileServiceConfig(DynamicData):
   enabled: bool
   fileServerMemoryMB: Optional[long] = None
   fileServerCPUMhz: Optional[long] = None
   fsvmMemoryMB: Optional[long] = None
   fsvmCPU: Optional[long] = None
   network: Optional[Network] = None
   domains: list[FileServiceDomainConfig] = []
   fileAnalyticsEnabled: Optional[bool] = None

class FileServiceConfigOpType:
   pass


class FileServiceDomain(DynamicData):
   uuid: str
   config: Optional[FileServiceDomainConfig] = None


class FileServiceDomainConfig(DynamicData):
   name: Optional[str] = None
   dnsServerAddresses: list[str] = []
   dnsSuffixes: list[str] = []
   fileServerIpConfig: list[FileServiceIpConfig] = []
   directoryServerConfig: Optional[DirectoryServerConfig] = None
   version: Optional[str] = None


class FileServiceDomainQuerySpec(DynamicData):
   uuids: list[str] = []
   names: list[str] = []


class FileServiceIpConfig(IpConfig):
   fqdn: Optional[str] = None
   isPrimary: Optional[bool] = None
   gateway: str
   affinityLocation: Optional[str] = None
   ipv6Gateway: Optional[str] = None

class FileServicePreflightCheckScope:
   pass

class FileServiceVMStatus:
   pass


class FileShare(DynamicData):
   uuid: str
   config: Optional[FileShareConfig] = None
   runtime: Optional[FileShareRuntimeInfo] = None

class FileShareAccessType:
   pass


class FileShareConfig(DynamicData):
   name: Optional[str] = None
   domainName: Optional[str] = None
   quota: Optional[str] = None
   softQuota: Optional[str] = None
   labels: list[KeyValue] = []
   storagePolicy: Optional[ProfileSpec] = None
   permission: list[FileShareNetPermission] = []
   protocols: list[str] = []
   smbOptions: Optional[FileShareSmbOptions] = None
   nfsSecType: Optional[str] = None
   affinityLocation: Optional[str] = None

class FileShareManagingEntity:
   pass


class FileShareNetPermission(DynamicData):
   ips: str
   permissions: Optional[str] = None
   allowRoot: Optional[bool] = None

class FileShareNfsSecType:
   pass

class FileShareProtocol:
   pass


class FileShareQueryProperties(DynamicData):
   includeBasic: Optional[bool] = None
   includeUsedCapacity: Optional[bool] = None
   includeVsanObjectUuids: Optional[bool] = None
   includeAllLabels: Optional[bool] = None
   labelKeys: list[str] = []


class FileShareQueryResult(DynamicData):
   fileShares: list[FileShare] = []
   nextOffset: Optional[str] = None
   totalShareCount: Optional[long] = None
   maxShareCount: Optional[long] = None


class FileShareQuerySpec(DynamicData):
   domainName: Optional[str] = None
   uuids: list[str] = []
   names: list[str] = []
   offset: Optional[str] = None
   limit: Optional[long] = None
   managedBy: list[str] = []
   protocols: list[str] = []
   pageNumber: Optional[long] = None
   properties: Optional[FileShareQueryProperties] = None


class FileShareRuntimeInfo(DynamicData):
   usedCapacity: Optional[long] = None
   hostname: Optional[str] = None
   address: Optional[str] = None
   vsanObjectUuids: list[str] = []
   accessPoints: list[KeyValue] = []
   managedBy: Optional[str] = None
   fileServerFQDN: Optional[str] = None

class FileShareSmbEncryptionType:
   pass


class FileShareSmbOptions(DynamicData):
   encryption: Optional[str] = None
   accessBasedEnumeration: Optional[bool] = None


class FileShareSnapshot(DynamicData):
   config: Optional[FileShareSnapshotConfig] = None
   creationTime: Optional[datetime] = None
   usedCapacity: Optional[long] = None


class FileShareSnapshotConfig(DynamicData):
   shareUuid: Optional[str] = None
   name: Optional[str] = None


class FileShareSnapshotQueryResult(DynamicData):
   snapshots: list[FileShareSnapshot] = []
   totalCount: Optional[int] = None


class FileShareSnapshotQuerySpec(DynamicData):
   shareUuid: str
   snapshotNames: list[str] = []
   startTime: Optional[datetime] = None
   endTime: Optional[datetime] = None
   pageSize: Optional[int] = None
   pageNumber: Optional[int] = None

class HciMeshClientOperation:
   pass


class HciMeshDatastoreSource(DynamicData):
   vcInfo: RemoteVcInfo


class HostResourceCheckResult(EntityResourceCheckDetails):
   host: Optional[HostSystem] = None
   diskGroups: list[DiskGroupResourceCheckResult] = []
   storagePools: list[StoragePoolResourceCheckResult] = []


class HostSiteMaintenanceStatus(DynamicData):
   host: HostSystem
   state: Optional[str] = None
   startTime: Optional[datetime] = None
   hostCount: Optional[long] = None
   hosts: list[str] = []
   statusUpdateTime: Optional[long] = None


class IODiagnosticsFailedCheck(DynamicData):
   unsupportedType: str
   reason: LocalizableMessage

class IODiagnosticsFailedCheckType:
   pass


class IODiagnosticsInstance(DynamicData):
   name: str
   state: str
   events: list[IODiagnosticsInstanceEvent] = []
   targets: list[IODiagnosticsTarget] = []
   startTime: datetime
   endTime: datetime
   recurrenceName: Optional[str] = None


class IODiagnosticsInstanceEvent(DynamicData):
   eventType: str
   eventTime: datetime
   eventTargets: list[IODiagnosticsTarget] = []

class IODiagnosticsInstanceEventType:
   pass


class IODiagnosticsInstanceQuerySpec(DynamicData):
   targets: list[IODiagnosticsTarget] = []
   startTime: datetime
   endTime: Optional[datetime] = None

class IODiagnosticsInstanceState:
   pass


class IODiagnosticsObjectLayout(DynamicData):
   layout: str


class IODiagnosticsPrecheckResult(DynamicData):
   supported: bool
   failedChecks: list[IODiagnosticsFailedCheck] = []


class IODiagnosticsStats(DynamicData):
   objectsIOStats: list[ObjectIOStats] = []
   startTime: datetime
   endTime: datetime


class IODiagnosticsTarget(DynamicData):
   type: str
   entityId: str
   objUuids: list[str] = []


class IODiagnosticsTargetStats(DynamicData):
   target: IODiagnosticsTarget
   objectsIODiagnosticsStats: list[IODiagnosticsStats] = []

class IODiagnosticsTargetType:
   pass


class IOLatency(DynamicData):
   latencyType: str
   sourceEntityUuid: str
   destEntityUuid: str
   readLatencyStats: IOLatencyMetrics
   writeLatencyStats: IOLatencyMetrics
   detailedInfo: list[KeyAnyValue] = []


class IOLatencyMetrics(DynamicData):
   totalCount: int
   averageLatency: float
   stddevLatency: Optional[float] = None

class IOLatencyType:
   pass

class LifecycleCheckOperation:
   pass

class LifecycleClusterType:
   pass


class LifecycleConfigDetails(DynamicData):
   clusterType: str
   faultDomainsDetails: list[LifecycleFaultDomainDetails] = []
   witnessHostsDetails: list[LifecycleWitnessDetails] = []


class LifecycleFaultDomainDetails(DynamicData):
   isPreferredFaultDomain: Optional[bool] = None
   name: Optional[str] = None
   hosts: list[HostSystem] = []


class LifecyclePreCheckResult(DynamicData):
   type: Optional[str] = None
   description: Optional[LocalizableMessage] = None
   status: str
   reason: Optional[LocalizableMessage] = None

class LifecyclePreCheckType:
   pass


class LifecycleWitnessDetails(DynamicData):
   host: HostSystem
   isVirtualAppliance: bool
   sharedClusters: list[ClusterComputeResource] = []


class MetricProfile(DynamicData):
   authToken: str


class MetricsConfig(DynamicData):
   profiles: list[MetricProfile] = []

class Mode:
   pass


class MountPrecheckItem(DynamicData):
   type: str
   description: LocalizableMessage
   status: str
   reason: list[LocalizableMessage] = []
   ignoreMessage: list[LocalizableMessage] = []


class MountPrecheckNetworkConnectivity(DynamicData):
   host: HostSystem
   smallPingTestSuccessPct: int
   largePingTestSuccessPct: int
   status: str


class MountPrecheckNetworkConnectivityDetail(DynamicData):
   host: HostSystem
   networkConnectivity: list[MountPrecheckNetworkConnectivity] = []


class MountPrecheckNetworkConnectivityResult(MountPrecheckItem):
   details: list[MountPrecheckNetworkConnectivityDetail] = []


class MountPrecheckNetworkLatency(DynamicData):
   host: HostSystem
   networkLatency: long
   status: str


class MountPrecheckNetworkLatencyDetail(DynamicData):
   host: HostSystem
   networkLatencies: list[MountPrecheckNetworkLatency] = []

class MountPrecheckNetworkLatencyResult(MountPrecheckItem):
   details: list[MountPrecheckNetworkLatencyDetail] = []


class MountPrecheckResult(DynamicData):
   result: list[MountPrecheckItem] = []

class MountPrecheckType:
   pass

class MountPrecheckTypeDIT:
   pass


class ObjectHealthTelemetrySummary(DynamicData):
   healthyObjectCount: int
   inaccessibleObjectCount: int
   needRetryObjectCount: int
   pdlObjectCount: int
   clusterHostCount: int


class ObjectIOStats(DynamicData):
   backingObjectId: str
   ioLatencyStats: list[IOLatency] = []
   objectLayout: IODiagnosticsObjectLayout

class PerfsvcRemediateAction:
   pass

class PrecheckDatastoreSourceOperation:
   pass


class ProactiveRebalanceInfo(DynamicData):
   enabled: Optional[bool] = None
   threshold: Optional[int] = None


class RdmaConfig(DynamicData):
   rdmaEnabled: bool


class ReconfigSpec(SDDCBase):
   vsanClusterConfig: Optional[ConfigInfo] = None
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   diskMappingSpec: Optional[VsanDiskMappingsConfigSpec] = None
   faultDomainsSpec: Optional[VsanFaultDomainsConfigSpec] = None
   modify: bool
   allowReducedRedundancy: Optional[bool] = None
   resyncIopsLimitConfig: Optional[ResyncIopsInfo] = None
   iscsiSpec: Optional[VsanIscsiTargetServiceSpec] = None
   dataEncryptionConfig: Optional[DataEncryptionConfig] = None
   extendedConfig: Optional[VsanExtendedConfig] = None
   datastoreConfig: Optional[DatastoreConfig] = None
   perfsvcConfig: Optional[VsanPerfsvcConfig] = None
   unmapConfig: Optional[VsanUnmapConfig] = None
   vumConfig: Optional[VsanVumConfig] = None
   metricsConfig: Optional[MetricsConfig] = None
   fileServiceConfig: Optional[FileServiceConfig] = None
   rdmaConfig: Optional[RdmaConfig] = None
   dataInTransitEncryptionConfig: Optional[DataInTransitEncryptionConfig] = None
   mode: Optional[str] = None
   vsanHealthConfig: Optional[VsanHealthConfigSpec] = None
   vsanEsaConfig: Optional[VsanEsaConfig] = None
   xvcDatastoreConfig: Optional[XVCDatastoreConfig] = None
   serverClusterConfig: Optional[VcRemoteVsanServerClusterConfig] = None
   snapServiceConfig: Optional[SnapServiceConfig] = None
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None
   vbossClusterConfig: Optional[VbossClusterConfig] = None


class RemoteVcInfo(DynamicData):
   linkType: Optional[str] = None
   vcHost: str


class RemoteVcInfoStandalone(RemoteVcInfo):
   user: Optional[str] = None
   password: Optional[str] = None
   cert: Optional[str] = None

class RemoteVcLinkType:
   pass

class RemoteVsanNetworkTopology:
   pass


class RemoteVsanSite(DynamicData):
   name: str


class RemoteVsanSiteAffinity(DynamicData):
   clientSite: Optional[RemoteVsanSite] = None
   serverSite: RemoteVsanSite


class RepairTimerInfo(DynamicData):
   maxTimeToRepair: int
   minTimeToRepair: int
   objectCount: int
   objectCountWithRepairTimer: Optional[int] = None

class ResourceCheckComponentResult(ResourceCheckResult):
   type: str

class ResourceCheckComponentType:
   pass


class ResourceCheckDataPersistenceResult(ResourceCheckComponentResult):
   dataToRebuild: Optional[long] = None
   inaccessibleInstances: list[str] = []
   reducedAvailabilityInstances: list[str] = []
   rebuildInstances: list[str] = []


class ResourceCheckResult(EntityResourceCheckDetails):
   class ResourceCheckDedupStoreHealthState(Enum):
      Inaccessible: ClassVar['ResourceCheckDedupStoreHealthState'] = 'Inaccessible'
      Noncompliant: ClassVar['ResourceCheckDedupStoreHealthState'] = 'Noncompliant'

   timestamp: datetime
   status: str
   messages: list[LocalizableMessage] = []
   faultDomains: list[FaultDomainResourceCheckResult] = []
   dataToMove: Optional[long] = None
   nonCompliantObjects: list[str] = []
   inaccessibleObjects: list[str] = []
   capacityThreshold: Optional[VsanHealthThreshold] = None
   health: Optional[VsanClusterHealthSummary] = None
   dataToResync: Optional[long] = None
   dedupStoreHealth: Optional[str] = None


class ResourceCheckSpec(DynamicData):
   operation: str
   entities: list[str] = []
   maintenanceSpec: Optional[MaintenanceSpec] = None
   parent: Optional[Task] = None


class ResourceCheckStatus(DynamicData):
   status: str
   result: Optional[ResourceCheckResult] = None
   task: Optional[ResourceCheckTaskDetails] = None
   parentTask: Optional[ResourceCheckTaskDetails] = None
   componentResults: list[ResourceCheckComponentResult] = []

class ResourceCheckStatusType:
   pass


class ResourceCheckTaskDetails(DynamicData):
   task: Task
   host: Optional[HostSystem] = None
   hostUuid: Optional[str] = None
   maintenanceSpec: Optional[MaintenanceSpec] = None

class ResourceCheckVsanResult(ResourceCheckComponentResult):
   pass


class ResyncIopsInfo(DynamicData):
   resyncIops: int


class RuntimeStatsHostMap(DynamicData):
   host: HostSystem
   stats: Optional[RuntimeStats] = None


class SSDEnduranceThresholdSpec(DynamicData):
   clustername: str
   clusternameop: Optional[str] = None
   hostname: Optional[str] = None
   hostnameop: Optional[str] = None
   diskname: Optional[str] = None
   disknameop: Optional[str] = None
   diskvendorname: Optional[str] = None
   diskvendorop: Optional[str] = None
   ssdEndurancePtg: float
   severity: str


class ServerHostUnicastInfo(DynamicData):
   hostUuid: str
   nodeType: Optional[str] = None
   unicastSpec: list[VsanUnicastAddressInfo] = []
   thumbprintList: list[CertThumbprint] = []


class SharedWitnessCompatibilityResult(DynamicData):
   witnessHostCompatibility: EntityCompatibilityResult
   roboClusterCompatibility: list[EntityCompatibilityResult] = []


class SiteMaintenanceCheckTaskDetails(ResourceCheckTaskDetails):
   cluster: ClusterComputeResource
   siteMaintenanceSpec: SiteMaintenanceSpec


class SiteMaintenanceInfo(DynamicData):
   faultDomainName: str
   state: str
   trackingTask: Optional[Task] = None
   hostStatus: list[HostSiteMaintenanceStatus] = []
   statusUpdateTime: Optional[long] = None


class SiteMaintenancePrecheckDetail(DynamicData):
   testName: str
   testStatus: str
   message: Optional[LocalizableMessage] = None


class SiteMaintenancePrecheckStatus(DynamicData):
   timestamp: datetime
   status: str
   taskDetails: Optional[SiteMaintenanceCheckTaskDetails] = None
   resourceCheckResult: Optional[SiteMaintenanceResourceCheckResult] = None


class SiteMaintenanceResourceCheckResult(ResourceCheckVsanResult):
   vmToMigrate: list[ManagedObject] = []
   vmToPowerOffInfo: list[VMPowerOffInfo] = []
   checkDetails: list[SiteMaintenancePrecheckDetail] = []


class SiteMaintenanceSpec(DynamicData):
   faultDomainName: str

class SiteMaintenanceState:
   pass


class SnapServiceConfig(DynamicData):
   enabled: bool

class SnapshotCreator:
   pass

class SnapshotType:
   pass


class StoragePoolDiskResourceCheckResult(DiskResourceCheckResult):
   diskType: Optional[str] = None


class StoragePoolResourceCheckResult(EntityResourceCheckDetails):
   disks: list[StoragePoolDiskResourceCheckResult] = []


class VMPowerOffInfo(DynamicData):
   vmToPowerOff: list[ManagedObject] = []
   reason: Optional[LocalizableMessage] = None


class VbossConfig(DynamicData):
   enabled: bool
   configs: list[VbossObjectStoreConfig] = []


class VbossObjectStoreConfig(DynamicData):
   id: str
   secretKey: Optional[str] = None
   volumeUuids: list[str] = []
   properties: Optional[str] = None


class VcRemoteVsanServerClusterConfig(DynamicData):
   serverClusters: list[VcRemoteVsanServerClusterInfo] = []


class VcRemoteVsanServerClusterInfo(DynamicData):
   clusterUuid: str
   networkTopology: Optional[str] = None
   siteAffinity: list[RemoteVsanSiteAffinity] = []
   ownerVc: Optional[str] = None
   ditConfig: Optional[DataInTransitEncryptionConfig] = None


class VipConfig(VipConfigSpec):
   vmknicName: Optional[str] = None
   owner: Optional[HostSystem] = None
   ownerHostUuid: Optional[str] = None


class VipConfigSpec(DynamicData):
   enabled: Optional[bool] = None
   v4NetworkConfig: Optional[VipNetworkConfig] = None
   v6NetworkConfig: Optional[VipNetworkConfig] = None
   vswitchConfig: Optional[VipVswitchConfig] = None
   distributedSwitchConfig: Optional[VipDVswitchConfig] = None


class VipDVswitchConfig(DynamicData):
   portGroup: Optional[DistributedVirtualPortgroup] = None
   dvsUuid: Optional[str] = None


class VipNetworkConfig(DynamicData):
   ipAddress: str
   subnet: str
   gateway: Optional[str] = None


class VipVswitchConfig(DynamicData):
   vswitchName: str
   vlanId: Optional[int] = None

class VsanAnalyticsEventLocationType:
   pass

class VsanAnalyticsEventSnapshotType:
   pass

class VsanAnalyticsEventType:
   pass


class VsanBurnInTest(DynamicData):
   testname: str
   workload: Optional[str] = None
   duration: long
   result: str


class VsanBurnInTestCheckResult(DynamicData):
   passedTests: list[VsanBurnInTest] = []
   notPerformedTests: list[VsanBurnInTest] = []
   failedTests: list[VsanBurnInTest] = []


class VsanCloudHealthStatus(DynamicData):
   collectorRunning: Optional[bool] = None
   lastSentTimestamp: Optional[str] = None
   internetConnectivity: Optional[bool] = None


class VsanClusterBurnInTestResultList(DynamicData):
   items: list[VsanBurnInTest] = []
   hosts: list[str] = []


class VsanCompliantDriver(DynamicData):
   driverName: str
   driverVersion: str
   supportedFeatures: list[str] = []


class VsanCompliantFirmware(DynamicData):
   firmwareVersion: str
   compliantDrivers: list[VsanCompliantDriver] = []


class VsanConfigBaseIssue(DynamicData):
   pass


class VsanConfigCheckResult(DynamicData):
   vsanEnabled: bool
   issues: list[VsanConfigBaseIssue] = []


class VsanConfigNotAllDisksClaimedIssue(VsanConfigBaseIssue):
   host: HostSystem
   disks: list[str] = []

class VsanConfigType:
   pass


class VsanDatastoreDefaultPolicySelectionConfig(DynamicData):
   enabled: bool


class VsanDeconvergedNetConfig(DynamicData):
   enabled: bool

class VsanDiskCompatibilityType:
   pass


class VsanDiskModelInfo(DynamicData):
   productId: str
   vendor: str
   partNumber: Optional[str] = None


class VsanDownloadItem(DynamicData):
   url: str
   sha1sum: str
   formatType: Optional[str] = None
   itemId: Optional[str] = None


class VsanEsaConfig(DynamicData):
   storagePoolSpecs: list[AddStoragePoolDiskSpec] = []
   hclDiskClaimEnabled: Optional[bool] = None
   datastoreDefaultPolicySelectionConfig: Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   diskConfiguration: Optional[VsanEsaDiskConfiguration] = None
   autoRAIDConfig: Optional[AutoRAIDConfig] = None
   deleteStoragePoolDiskSpec: Optional[DeleteStoragePoolDiskSpec] = None


class VsanEsaConfigInfo(DynamicData):
   hclDiskClaimEnabled: Optional[bool] = None
   datastoreDefaultPolicySelectionConfig: Optional[VsanDatastoreDefaultPolicySelectionConfig] = None
   diskConfiguration: Optional[VsanEsaDiskConfiguration] = None
   autoRAIDConfig: Optional[AutoRAIDConfig] = None


class VsanEsaDiskConfiguration(DynamicData):
   diskClaimConfiguration: list[DiskClaimConfiguration] = []


class VsanExtendedConfig(DynamicData):
   objectRepairTimer: Optional[long] = None
   disableSiteReadLocality: Optional[bool] = None
   enableCustomizedSwapObject: Optional[bool] = None
   largeScaleClusterSupport: Optional[bool] = None
   proactiveRebalanceInfo: Optional[ProactiveRebalanceInfo] = None
   capacityReservationInfo: Optional[CapacityReservationInfo] = None


class VsanFileServiceOvfSpec(DynamicData):
   version: Optional[str] = None
   updateTime: Optional[datetime] = None
   task: Optional[Task] = None


class VsanFileServicePreflightCheckResult(DynamicData):
   ovfInstalled: Optional[str] = None
   fsvmVersion: Optional[str] = None
   lastUpgradeDate: Optional[datetime] = None
   ovfMixedModeIssue: Optional[str] = None
   hostVersion: Optional[str] = None
   mixedModeIssue: Optional[str] = None
   networkPartitionIssue: Optional[str] = None
   vsanDatastoreIssue: Optional[str] = None
   domainConfigIssue: Optional[str] = None
   fileServiceVersion: Optional[str] = None
   dvsConfigIssue: Optional[str] = None
   domainConfigWarning: Optional[str] = None
   ntpConfigWarning: Optional[str] = None
   svsConfigIssue: Optional[str] = None
   nsxConfigIssue: Optional[str] = None


class VsanFileServiceSystem(ManagedObject):
   def DownloadFileServiceOvf(self, downloadUrl: str) -> Task: ...
   def QueryFileServiceOvfs(self) -> list[VsanFileServiceOvfSpec]: ...
   def FindOvfDownloadUrl(self, cluster: ClusterComputeResource) -> str: ...
   def PerformFileServicePreflightCheck(self, cluster: ClusterComputeResource, domainConfig: Optional[FileServiceDomainConfig], network: Optional[Network], scope: Optional[str], domainUuid: Optional[str]) -> VsanFileServicePreflightCheckResult: ...
   def CreateFileServiceDomain(self, domainConfig: FileServiceDomainConfig, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def ReconfigureFileServiceDomain(self, domainUuid: str, domainConfig: FileServiceDomainConfig, cluster: Optional[ClusterComputeResource], deleteDomainConfigFields: list[str]) -> Task: ...
   def RemoveFileServiceDomain(self, domainUuid: str, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def QueryFileServiceDomains(self, querySpec: Optional[FileServiceDomainQuerySpec], cluster: Optional[ClusterComputeResource]) -> list[FileServiceDomain]: ...
   def CreateFileShare(self, config: FileShareConfig, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def ReconfigureFileShare(self, shareUuid: str, config: FileShareConfig, cluster: Optional[ClusterComputeResource], deleteLabelKeys: list[str], force: Optional[bool]) -> Task: ...
   def RemoveFileShare(self, shareUuid: str, cluster: Optional[ClusterComputeResource], force: Optional[bool]) -> Task: ...
   def QueryFileShares(self, querySpec: FileShareQuerySpec, cluster: Optional[ClusterComputeResource]) -> Optional[FileShareQueryResult]: ...
   def UpgradeFsvm(self, cluster: ClusterComputeResource) -> Task: ...
   def RebalanceFileService(self, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def CreateFileShareSnapshot(self, config: FileShareSnapshotConfig, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def RemoveFileShareSnapshot(self, shareUuid: str, snapshotName: str, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def QueryFileShareSnapshots(self, querySpec: FileShareSnapshotQuerySpec, cluster: Optional[ClusterComputeResource]) -> Optional[FileShareSnapshotQueryResult]: ...


class VsanGenericClusterBaseIssue(DynamicData):
   pass


class VsanGenericClusterBestPracticeHealth(DynamicData):
   drsEnabled: bool
   haEnabled: bool
   issues: list[VsanGenericClusterBaseIssue] = []

class VsanHciMeshConfigLimits:
   pass


class VsanHclDeviceConstraint(DynamicData):
   pciId: str
   vcgLink: Optional[str] = None
   similarVcgLinks: list[str] = []
   compliantFirmwares: list[VsanCompliantFirmware] = []
   vcgId: Optional[int] = None
   model: Optional[str] = None
   partner: Optional[str] = None
   partNumber: Optional[str] = None
   release: Optional[str] = None


class VsanHclDiskConstraint(DynamicData):
   productId: str
   vendor: str
   constraints: list[VsanHclMinFwConstraint] = []
   pcieConstraints: list[VsanHclDeviceConstraint] = []
   partNumber: Optional[str] = None


class VsanHclDriverInfo(DynamicData):
   driverVersion: Optional[str] = None
   driverLink: Optional[VsanDownloadItem] = None
   fwVersion: Optional[str] = None
   fwLinks: list[VsanDownloadItem] = []
   toolsLinks: list[VsanDownloadItem] = []
   eula: Optional[str] = None
   driverType: Optional[str] = None
   driverName: Optional[str] = None
   diskModes: list[str] = []
   supportedFeatures: list[str] = []


class VsanHclMinFwConstraint(DynamicData):
   vcgId: int
   vcgLink: str
   model: str
   partner: str
   partNumber: Optional[str] = None
   release: str
   firmware: str


class VsanHclQuerySpec(DynamicData):
   includeOnlyVsanControllers: Optional[bool] = None
   cluster: Optional[ComputeResource] = None
   hosts: list[HostSystem] = []
   vsanStoragePoolEligibleDisksOnly: Optional[bool] = None


class VsanHclReleaseConstraint(DynamicData):
   cluster: ClusterComputeResource
   release: str
   hostDevices: list[VsanHostDeviceInfo] = []
   constraints: list[VsanHclDeviceConstraint] = []


class VsanHealthConfigSpec(DynamicData):
   healthCheckThresholdSpec: list[VsanHealthThreshold] = []
   historicalHealthConfig: Optional[VsanHistoricalHealthConfig] = None


class VsanHealthCustomizationSpec(DynamicData):
   ssdEnduranceSpec: list[SSDEnduranceThresholdSpec] = []

class VsanHealthPerspective:
   pass

class VsanHealthPerspective90:
   pass

class VsanHealthStatusType:
   pass


class VsanHealthThreshold(DynamicData):
   yellowValue: long
   redValue: long
   target: Optional[str] = None
   enabled: Optional[bool] = None

class VsanHealthThresholdTarget:
   pass


class VsanHistoricalHealthConfig(DynamicData):
   enabled: bool


class VsanHostDeviceInfo(DynamicData):
   hostname: str
   devices: list[VsanBasicDeviceInfo] = []


class VsanHostVdsSystem(ManagedObject):
   def VsanMigrateVmsToVds(self, vmConfigSpecs: list[VsanVmVdsMigrationSpec], vdsUuid: str, timeoutSec: long, revert: Optional[bool]) -> str: ...
   def VsanCompleteMigrateVmsToVds(self, jobId: str, newState: str) -> None: ...


class VsanHwToVcgInfoMappingSpec(DynamicData):
   entity: str
   vsanHwToVcgInfoMappings: list[VsanHwToVcgInfoMapping] = []


class VsanIOTripAnalyzerConfig(DynamicData):
   recurrences: list[VsanIOTripAnalyzerRecurrence] = []


class VsanIOTripAnalyzerRecurrence(DynamicData):
   name: Optional[str] = None
   targets: list[IODiagnosticsTarget] = []
   startTime: datetime
   endTime: Optional[datetime] = None
   duration: long
   interval: long
   status: str

class VsanIOTripAnalyzerRecurrenceStatus:
   pass


class VsanInternalExtendedConfig(DynamicData):
   vcMaxDiskVersion: Optional[int] = None
   stretchedClient: Optional[bool] = None


class VsanNetworkConfigBaseIssue(DynamicData):
   pass


class VsanNetworkConfigBestPracticeHealth(DynamicData):
   vdsPresent: bool
   issues: list[VsanNetworkConfigBaseIssue] = []


class VsanNetworkConfigPnicSpeedInconsistencyIssue(VsanNetworkConfigBaseIssue):
   host: HostSystem
   vswitchName: Optional[str] = None
   vds: Optional[DistributedVirtualSwitch] = None
   speedsMb: list[long] = []


class VsanNetworkConfigPortgroupWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   host: HostSystem
   portgroupName: Optional[str] = None
   vds: Optional[DistributedVirtualSwitch] = None
   pg: Optional[Network] = None
   numPnics: long


class VsanNetworkConfigVdsScopeIssue(VsanNetworkConfigBaseIssue):
   vds: DistributedVirtualSwitch
   memberHosts: list[HostSystem] = []
   nonMemberHosts: list[HostSystem] = []


class VsanNetworkConfigVsanNotOnVdsIssue(VsanNetworkConfigBaseIssue):
   host: HostSystem
   vmknic: str


class VsanNetworkConfigVswitchWithNoRedundancyIssue(VsanNetworkConfigBaseIssue):
   host: HostSystem
   vswitchName: Optional[str] = None
   vds: Optional[DistributedVirtualSwitch] = None
   numPnics: long


class VsanNetworkVMotionVmknicNotFountIssue(VsanNetworkConfigBaseIssue):
   hostWithoutVmotionVmknic: HostSystem


class VsanObjSnapParams(DynamicData):
   uuid: str
   creator: Optional[str] = None
   snapshotType: Optional[str] = None
   cookie: Optional[str] = None
   immutableTag: Optional[str] = None


class VsanObjectDetail(DynamicData):
   uuid: str
   objectPath: Optional[str] = None
   snapshots: list[VsanSnapshotDetail] = []


class VsanObjectManager(ManagedObject):
   pass


class VsanObjectSnapshotId(DynamicData):
   uuid: str
   snapshotId: int
   cookie: Optional[str] = None


class VsanPMemConfig(DynamicData):
   enabled: bool


class VsanPerfsvcHealthResult(DynamicData):
   statsObjectInfo: Optional[VsanObjectInformation] = None
   statsObjectConsistent: Optional[bool] = None
   statsObjectPolicyConsistent: Optional[bool] = None
   datastoreCompatible: Optional[bool] = None
   enoughFreeSpace: Optional[bool] = None
   remediateAction: Optional[str] = None
   hostResults: list[VsanPerfNodeInformation] = []
   verboseModeStatus: Optional[bool] = None


class VsanPolicyManager(ManagedObject):
   pass

class VsanPolicyRegulationCheckOpEnum:
   pass


class VsanPrepareVsanForVcsaSpec(DynamicData):
   vsanDiskMappingCreationSpec: Optional[DiskMappingCreationSpec] = None
   vsanDataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   taskId: Optional[str] = None
   vsanDataEncryptionConfig: Optional[EncryptionInfo] = None
   vsanAddStoragePoolDiskSpec: Optional[AddStoragePoolDiskSpec] = None
   createNativeKeyProviderSpec: Optional[CreateNativeKeyProviderSpec] = None


class VsanResourceCheckSystem(ManagedObject):
   def PerformResourceCheck(self, resourceCheckSpec: ResourceCheckSpec, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def GetResourceCheckStatus(self, resourceCheckSpec: Optional[ResourceCheckSpec], cluster: Optional[ClusterComputeResource]) -> ResourceCheckStatus: ...
   def PerformResourceCheckOnHost(self, resourceCheckSpec: ResourceCheckSpec) -> Task: ...
   def CancelResourceCheckOnHost(self) -> bool: ...

class VsanServiceStatus:
   pass

class VsanSiteLocationType:
   pass


class VsanSiteMaintenanceSystem(ManagedObject):
   def EnterSiteMaintenanceMode(self, faultDomainName: str, cluster: ClusterComputeResource) -> Task: ...
   def ExitSiteMaintenanceMode(self, faultDomainName: str, cluster: ClusterComputeResource) -> Task: ...
   def PerformSiteMaintenancePrecheck(self, cluster: ClusterComputeResource, spec: SiteMaintenanceSpec) -> Task: ...
   def GetSiteMaintenancePrecheckStatus(self, cluster: ClusterComputeResource, faultDomainName: str) -> SiteMaintenancePrecheckStatus: ...
   def QueryClusterSiteMaintenanceState(self, cluster: ClusterComputeResource) -> list[SiteMaintenanceInfo]: ...

class VsanSnapHealthType:
   pass

class VsanSnapStatsExpirationType:
   pass

class VsanSnapVmMembershipChangeStatus:
   pass


class VsanSnapshotDetail(DynamicData):
   snapshotId: int
   snapshotType: str
   snapshotPath: Optional[str] = None
   snapshotTagsInfo: list[KeyValue] = []


class VsanSnapshotQueryResult(DynamicData):
   objects: list[VsanObjectDetail] = []


class VsanSnapshotQuerySpec(DynamicData):
   datastoreUuid: str
   objectUuids: list[str] = []
   snapshotType: Optional[str] = None
   creator: Optional[str] = None
   includeDescriptorPath: Optional[bool] = None
   snapshotTagMask: Optional[int] = None


class VsanSpaceEfficiencyMetadataSize(DynamicData):
   dedupMetadataSize: Optional[long] = None
   compressionMetadataSize: Optional[long] = None


class VsanSpaceEfficiencyRatio(DynamicData):
   overallRatio: Optional[float] = None
   compressionRatio: Optional[float] = None
   dedupRatio: Optional[float] = None
   dedupEnabledRatio: Optional[float] = None
   thinProvisionRatio: Optional[float] = None
   snapshotSavingRatio: Optional[float] = None

class VsanSyncReason:
   pass

class VsanSyncStatus:
   pass


class VsanUnmapConfig(DynamicData):
   enable: bool


class VsanUpdateItem(DynamicData):
   host: HostSystem
   type: str
   name: str
   version: str
   existingVersion: Optional[str] = None
   present: bool
   vibSpec: list[VsanVibSpec] = []
   vibType: Optional[str] = None
   firmwareSpec: Optional[VsanHclFirmwareUpdateSpec] = None
   downloadInfo: list[VsanDownloadItem] = []
   eula: Optional[str] = None
   adapter: Optional[str] = None
   key: Optional[str] = None
   impact: Optional[str] = None
   firmwareUnknown: Optional[bool] = None

class VsanUpdateItemImpactType:
   pass

class VsanUpdateItemType:
   pass


class VsanValidationItem(ClusterComputeResource.ValidationResultBase):
   pass


class VsanVcPostDeployConfigSpec(DynamicData):
   dcName: Optional[str] = None
   clusterName: Optional[str] = None
   firstHost: Optional[ConnectSpec] = None
   hostsToAdd: list[ConnectSpec] = []
   vsanDataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   vsanLicenseKey: Optional[str] = None
   hostLicenseKey: Optional[str] = None
   taskId: Optional[str] = None
   vsanDataEncryptionConfig: Optional[EncryptionInfo] = None
   createNativeKeyProviderSpec: Optional[CreateNativeKeyProviderSpec] = None
   vsanClusterMode: Optional[str] = None
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None


class VsanVcStretchedClusterConfigSpec(DynamicData):
   witnessHost: HostSystem
   clusters: list[VsanStretchedClusterConfig] = []
   witnessDiskMappings: list[DiskMapping] = []
   witnessStoragePoolSpecs: list[AddStoragePoolDiskSpec] = []

class VsanVcsaDeploymentPhase:
   pass


class VsanVcsaDeploymentProgress(DynamicData):
   phase: str
   progressPct: long
   message: str
   success: bool
   error: Optional[MethodFault] = None
   updateCounter: long
   taskId: Optional[str] = None
   vm: Optional[VirtualMachine] = None


class VsanVdsMigrationPlan(DynamicData):
   vdsSpec: DistributedVirtualSwitch.CreateSpec
   pgs: list[VsanVdsPgMigrationSpec] = []
   inaccessibleVms: list[VirtualMachine] = []
   infraVms: list[VirtualMachine] = []


class VsanVdsPgMigrationHostInfo(DynamicData):
   host: HostSystem
   hostname: str
   vmknicDevices: list[str] = []
   vmVnics: list[VsanVdsPgMigrationVmInfo] = []


class VsanVdsPgMigrationSpec(DynamicData):
   vssPgName: str
   dvPgName: str
   vdsPgSetting: VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy
   vdsPgType: str
   hosts: list[VsanVdsPgMigrationHostInfo] = []
   collisionRename: bool


class VsanVdsPgMigrationVmInfo(DynamicData):
   vm: VirtualMachine
   vnicLabel: list[str] = []


class VsanVdsSystem(ManagedObject):
   def VsanVdsGetMigrationPlan(self, cluster: ComputeResource, vswitchName: Optional[str], vdsName: Optional[str], vmnicDevices: list[str], infraVm: list[VirtualMachine], vds: Optional[VmwareDistributedVirtualSwitch], hosts: list[HostSystem]) -> VsanVdsMigrationPlan: ...
   def VsanVdsMigrateVss(self, cluster: ComputeResource, migrationPlan: Optional[VsanVdsMigrationPlan], vswitchName: Optional[str], vdsName: Optional[str], vmnicDevices: list[str], infraVm: list[VirtualMachine], vds: Optional[VmwareDistributedVirtualSwitch], hosts: list[HostSystem]) -> Task: ...
   def VsanVssMigrateVds(self, cluster: Optional[ComputeResource], hosts: list[HostSystem], vds: VmwareDistributedVirtualSwitch, vswitchName: Optional[str], vmnicDevices: list[str], infraVm: list[VirtualMachine]) -> Task: ...
   def RollbackVdsToVss(self, task: Task) -> bool: ...


class VsanVibInstallPreflightStatus(DynamicData):
   manualVmotionRequired: bool
   rollingRequired: bool


class VsanVibScanResult(DynamicData):
   host: HostSystem
   vibName: str
   vibVersion: str
   existingVersion: Optional[str] = None
   maintenanceModeRequired: bool
   rebootRequired: bool
   meetsSystemReq: bool
   pkgDepsMetByHost: bool


class VsanVibSpec(DynamicData):
   host: HostSystem
   metaUrl: Optional[str] = None
   metaSha1Sum: Optional[str] = None
   vibUrl: str
   vibSha1Sum: str

class VsanVibType:
   pass


class VsanVmVdsMigrationSpec(DynamicData):
   vmInstanceUuid: str
   vnics: list[VsanVnicVdsMigrationSpec] = []


class VsanVnicVdsMigrationSpec(DynamicData):
   key: int
   vdsBacking: VirtualDevice.BackingInfo


class VsanVumConfig(DynamicData):
   baselinePreferenceType: str


class WitnessHostConfig(DynamicData):
   subClusterUuid: str
   preferredFaultDomainName: str
   metadataMode: Optional[bool] = None


class XVCClientInfo(DynamicData):
   cluster: ClusterComputeResource
   clusterName: str
   vsanFormatVersion: str
   ownerVc: str
   vcUuid: Optional[str] = None
   clusterUuid: Optional[str] = None


class XVCDatastoreConfig(DynamicData):
   xvcDatastores: list[XVCDatastoreInfo] = []


class XVCDatastoreInfo(DynamicData):
   datastore: Datastore
   ownerVc: str


class XvcClientConfig(DatastoreSpec):
   xvcClusters: list[XVCClientInfo] = []


class XvcClientInfoSpec(DynamicData):
   clientVc: str
   vcUuid: Optional[str] = None
   vcVersion: Optional[str] = None
   cluster: Optional[ClusterComputeResource] = None
   clusterName: Optional[str] = None
   clusterUuid: Optional[str] = None
   vsanFormatVersion: Optional[str] = None
   minVsanFormatVersion: Optional[str] = None
   datastore: list[Datastore] = []
   unicastInfo: Optional[ClientClusterUnicastInfo] = None
   saGeneration: Optional[long] = None


class XvcQueryCriteria(DynamicData):
   property: str
   operator: Optional[str] = None
   comparableValue: Optional[object] = None
   comparableList: Optional[DynamicArray] = None
   ignoreCase: Optional[bool] = None

class XvcQueryCriteriaOperator:
   pass


class XvcQueryFilter(DynamicData):
   criterias: list[XvcQueryCriteria] = []
   operator: Optional[str] = None

class XvcQueryFilterOperator:
   pass


class XvcQueryPropertyValue(DynamicData):
   value: Optional[object] = None


class XvcQueryResultSet(DynamicData):
   properties: list[str] = []
   resultItems: list[XvcResultItem] = []
   totalCount: Optional[long] = None


class XvcQuerySpec(DynamicData):
   objectModel: Optional[str] = None
   properties: list[str] = []
   filter: Optional[XvcQueryFilter] = None
   offset: Optional[int] = None
   limit: Optional[int] = None
   returnTotalCount: Optional[bool] = None


class XvcResultItem(DynamicData):
   propertyValues: list[XvcQueryPropertyValue] = []

class clusterPowerState:
   pass
