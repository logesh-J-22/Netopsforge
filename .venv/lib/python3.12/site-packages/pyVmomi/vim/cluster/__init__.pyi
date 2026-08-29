# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vim import ComputeResource

from pyVmomi.vim import Datastore
from pyVmomi.vim import EVCMode
from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim import HostSystem

from pyVmomi.vim import KeyValue
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import StoragePod

from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim import VsanUpgradeSystem

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import ConnectSpec
from pyVmomi.vim.host import CpuIdInfo
from pyVmomi.vim.host import FeatureCapability
from pyVmomi.vim.host import FeatureMask

from pyVmomi.vim.host import MaintenanceSpec

from pyVmomi.vim.host import ScsiDisk

from pyVmomi.vim.host import VSANStretchedClusterHostCapability

from pyVmomi.vim.host import VsanDitEncryptionHealthSummary

from pyVmomi.vim.host import VsanEncryptionHealthSummary

from pyVmomi.vim.host import VsanFailedRepairObjectResult

from pyVmomi.vim.host import VsanFileServiceHealthSummary

from pyVmomi.vim.host import VsanHostGlobalDedupConfigHealthSummary

from pyVmomi.vim.host import VsanHostHciMeshDitEncryptionHealthSummary

from pyVmomi.vim.host import VsanHostHclInfo

from pyVmomi.vim.host import VsanHostHealthSystemStatusResult

from pyVmomi.vim.host import VsanHostIoInsightInfo

from pyVmomi.vim.host import VsanHostVirtualApplianceInfo

from pyVmomi.vim.host import VsanHostVmdkLoadTestResult

from pyVmomi.vim.host import VsanKmsHealth

from pyVmomi.vim.host import VsanLimitHealthResult

from pyVmomi.vim.host import VsanNetworkHealthResult

from pyVmomi.vim.host import VsanNetworkLoadTestResult

from pyVmomi.vim.host import VsanObjectOverallHealth
from pyVmomi.vim.host import VsanPhysicalDiskHealthSummary
from pyVmomi.vim.host import VsanQueryResultHostInfo

from pyVmomi.vim.host import VsanSmartStatsHostSummary

from pyVmomi.vim.host import VsanVmdkLoadTestSpec

from pyVmomi.vim.host import VsanVsanPcapResult

from pyVmomi.vim.option import ArrayUpdateSpec

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vm import CertThumbprint

from pyVmomi.vim.vm import CloneSpec

from pyVmomi.vim.vm import ConfigSpec

from pyVmomi.vim.vm import FeatureRequirement

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vm import RelocateSpec

from pyVmomi.vim.vsan import AutoRAIDInfo

from pyVmomi.vim.vsan import CapacityReservationInfo

from pyVmomi.vim.vsan import ClusterRuntimeInfo
from pyVmomi.vim.vsan import ConfigInfoEx

from pyVmomi.vim.vsan import DataEfficiencyCapacityState

from pyVmomi.vim.vsan import DataEfficiencyConfig
from pyVmomi.vim.vsan import DataEncryptionConfig

from pyVmomi.vim.vsan import DatastoreSourcePrecheckResult

from pyVmomi.vim.vsan import DiskInfo
from pyVmomi.vim.vsan import HciMeshDatastoreSource

from pyVmomi.vim.vsan import IODiagnosticsInstance
from pyVmomi.vim.vsan import IODiagnosticsInstanceQuerySpec
from pyVmomi.vim.vsan import IODiagnosticsTarget
from pyVmomi.vim.vsan import IODiagnosticsTargetStats

from pyVmomi.vim.vsan import LifecycleConfigDetails
from pyVmomi.vim.vsan import LifecyclePreCheckResult
from pyVmomi.vim.vsan import MountPrecheckResult
from pyVmomi.vim.vsan import ReconfigSpec
from pyVmomi.vim.vsan import RemoteVcInfo
from pyVmomi.vim.vsan import RuntimeStatsHostMap
from pyVmomi.vim.vsan import SharedWitnessCompatibilityResult
from pyVmomi.vim.vsan import VcRemoteVsanServerClusterInfo

from pyVmomi.vim.vsan import VipConfigSpec

from pyVmomi.vim.vsan import VsanBurnInTestCheckResult
from pyVmomi.vim.vsan import VsanConfigCheckResult

from pyVmomi.vim.vsan import VsanDiskModelInfo
from pyVmomi.vim.vsan import VsanGenericClusterBestPracticeHealth
from pyVmomi.vim.vsan import VsanHclDiskConstraint
from pyVmomi.vim.vsan import VsanHclQuerySpec
from pyVmomi.vim.vsan import VsanHclReleaseConstraint
from pyVmomi.vim.vsan import VsanHealthThreshold
from pyVmomi.vim.vsan import VsanHwToVcgInfoMappingSpec
from pyVmomi.vim.vsan import VsanIOTripAnalyzerConfig
from pyVmomi.vim.vsan import VsanIOTripAnalyzerRecurrence
from pyVmomi.vim.vsan import VsanNetworkConfigBestPracticeHealth
from pyVmomi.vim.vsan import VsanPerfsvcHealthResult
from pyVmomi.vim.vsan import VsanSpaceEfficiencyRatio

from pyVmomi.vim.vsan import VsanUpdateItem
from pyVmomi.vim.vsan import VsanVcStretchedClusterConfigSpec
from pyVmomi.vim.vsan import XVCDatastoreInfo
from pyVmomi.vim.vsan import XvcQueryResultSet
from pyVmomi.vim.vsan import XvcQuerySpec

from pyVmomi.vim.vm.device import VirtualDiskId

from pyVmomi.vim.vsan.cluster import ConfigInfo
from pyVmomi.vim.vsan.cluster import CoreConfigInfo
from pyVmomi.vim.vsan.cluster import CoreConfigSpec

from pyVmomi.vim.vsan.host import AddStoragePoolDiskSpec

from pyVmomi.vim.vsan.host import ConfigInfo
from pyVmomi.vim.vsan.host import DeleteStoragePoolDiskSpec
from pyVmomi.vim.vsan.host import DiskMapInfoEx
from pyVmomi.vim.vsan.host import DiskMapping
from pyVmomi.vim.vsan.host import DiskMappingCreationSpec

from pyVmomi.vim.vsan.host import DrsStats
from pyVmomi.vim.vsan.host import QueryVsanDisksSpec

from pyVmomi.vim.vsan.host import StoragePoolDiskInfo
from pyVmomi.vim.vsan.host import VsanHostCapability
from pyVmomi.vim.vsan.host import VsanManagedDisksInfo

from pyVmomi.vim.vsan.host import VsanSyncingObjectQueryResult



class Action(DynamicData):
   class ActionType(Enum):
      MigrationV1: ClassVar['ActionType'] = 'MigrationV1'
      VmPowerV1: ClassVar['ActionType'] = 'VmPowerV1'
      HostPowerV1: ClassVar['ActionType'] = 'HostPowerV1'
      IncreaseLimitV1: ClassVar['ActionType'] = 'IncreaseLimitV1'
      IncreaseSizeV1: ClassVar['ActionType'] = 'IncreaseSizeV1'
      IncreaseSharesV1: ClassVar['ActionType'] = 'IncreaseSharesV1'
      IncreaseReservationV1: ClassVar['ActionType'] = 'IncreaseReservationV1'
      DecreaseOthersReservationV1: ClassVar['ActionType'] = 'DecreaseOthersReservationV1'
      IncreaseClusterCapacityV1: ClassVar['ActionType'] = 'IncreaseClusterCapacityV1'
      DecreaseMigrationThresholdV1: ClassVar['ActionType'] = 'DecreaseMigrationThresholdV1'
      HostMaintenanceV1: ClassVar['ActionType'] = 'HostMaintenanceV1'
      StorageMigrationV1: ClassVar['ActionType'] = 'StorageMigrationV1'
      StoragePlacementV1: ClassVar['ActionType'] = 'StoragePlacementV1'
      PlacementV1: ClassVar['ActionType'] = 'PlacementV1'
      HostInfraUpdateHaV1: ClassVar['ActionType'] = 'HostInfraUpdateHaV1'

   type: str
   target: Optional[ManagedObject] = None


class ActionHistory(DynamicData):
   action: Action
   time: datetime


class AffinityRuleSpec(RuleInfo):
   vm: list[VirtualMachine] = []


class AntiAffinityRuleSpec(RuleInfo):
   vm: list[VirtualMachine] = []


class AttemptedVmInfo(DynamicData):
   vm: VirtualMachine
   task: Optional[Task] = None


class ClusterInitialPlacementAction(Action):
   targetHost: Optional[HostSystem] = None
   pool: ResourcePool
   availableNetworks: list[Network] = []
   configSpec: Optional[ConfigSpec] = None


class ClusterPowerContext(DynamicData):
   currentClusterPowerStatus: str
   orderedClusterPowerStatus: list[str] = []
   trackingTask: Optional[Task] = None
   lastErrorMessage: Optional[LocalizableMessage] = None
   lastErrorMOs: list[ManagedObject] = []

class ClusterPowerStatus:
   pass


class ConfigInfo(DynamicData):
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []


class ConfigInfoEx(ComputeResource.ConfigInfo):
   systemVMsConfig: Optional[SystemVMsConfigInfo] = None
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []
   orchestration: Optional[OrchestrationInfo] = None
   vmOrchestration: list[VmOrchestrationInfo] = []
   dpmConfigInfo: Optional[DpmConfigInfo] = None
   dpmHostConfig: list[DpmHostConfigInfo] = []
   vsanConfigInfo: Optional[ConfigInfo] = None
   vsanHostConfig: list[ConfigInfo] = []
   group: list[GroupInfo] = []
   infraUpdateHaConfig: Optional[InfraUpdateHaConfigInfo] = None
   proactiveDrsConfig: Optional[ProactiveDrsConfigInfo] = None
   cryptoConfig: Optional[CryptoConfigInfo] = None
   vsanCoreConfig: Optional[CoreConfigInfo] = None


class ConfigSpec(DynamicData):
   dasConfig: Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []


class ConfigSpecEx(ComputeResource.ConfigSpec):
   systemVMsConfig: Optional[SystemVMsConfigSpec] = None
   dasConfig: Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []
   orchestration: Optional[OrchestrationInfo] = None
   vmOrchestrationSpec: list[VmOrchestrationSpec] = []
   dpmConfig: Optional[DpmConfigInfo] = None
   dpmHostConfigSpec: list[DpmHostConfigSpec] = []
   vsanConfig: Optional[ConfigInfo] = None
   vsanHostConfigSpec: list[ConfigInfo] = []
   groupSpec: list[GroupSpec] = []
   infraUpdateHaConfig: Optional[InfraUpdateHaConfigInfo] = None
   proactiveDrsConfig: Optional[ProactiveDrsConfigInfo] = None
   inHciWorkflow: Optional[bool] = None
   cryptoConfig: Optional[CryptoConfigInfo] = None
   vsanCoreConfigSpec: Optional[CoreConfigSpec] = None


class CryptoConfigInfo(DynamicData):
   class CryptoMode(Enum):
      onDemand: ClassVar['CryptoMode'] = 'onDemand'
      forceEnable: ClassVar['CryptoMode'] = 'forceEnable'

   cryptoMode: Optional[str] = None
   policy: Optional[ClusterComputeResource.CryptoModePolicy] = None


class DasAamHostInfo(DasHostInfo):
   hostDasState: list[DasAamNodeState] = []
   primaryHosts: list[str] = []


class DasAamNodeState(DynamicData):
   class DasState(Enum):
      uninitialized: ClassVar['DasState'] = 'uninitialized'
      initialized: ClassVar['DasState'] = 'initialized'
      configuring: ClassVar['DasState'] = 'configuring'
      unconfiguring: ClassVar['DasState'] = 'unconfiguring'
      running: ClassVar['DasState'] = 'running'
      error: ClassVar['DasState'] = 'error'
      agentShutdown: ClassVar['DasState'] = 'agentShutdown'
      nodeFailed: ClassVar['DasState'] = 'nodeFailed'

   host: HostSystem
   name: str
   configState: str
   runtimeState: str


class DasAdmissionControlInfo(DynamicData):
   pass


class DasAdmissionControlPolicy(DynamicData):
   resourceReductionToToleratePercent: Optional[int] = None
   pMemAdmissionControlEnabled: Optional[bool] = None


class DasAdvancedRuntimeInfo(DynamicData):
   class VmcpCapabilityInfo(DynamicData):
      storageAPDSupported: bool
      storagePDLSupported: bool

   class HeartbeatDatastoreInfo(DynamicData):
      datastore: Datastore
      hosts: list[HostSystem] = []

   dasHostInfo: Optional[DasHostInfo] = None
   vmcpSupported: Optional[VmcpCapabilityInfo] = None
   heartbeatDatastoreInfo: list[HeartbeatDatastoreInfo] = []


class DasConfigInfo(DynamicData):
   class ServiceState(Enum):
      disabled: ClassVar['ServiceState'] = 'disabled'
      enabled: ClassVar['ServiceState'] = 'enabled'

   class VmMonitoringState(Enum):
      vmMonitoringDisabled: ClassVar['VmMonitoringState'] = 'vmMonitoringDisabled'
      vmMonitoringOnly: ClassVar['VmMonitoringState'] = 'vmMonitoringOnly'
      vmAndAppMonitoring: ClassVar['VmMonitoringState'] = 'vmAndAppMonitoring'

   class HBDatastoreCandidate(Enum):
      userSelectedDs: ClassVar['HBDatastoreCandidate'] = 'userSelectedDs'
      allFeasibleDs: ClassVar['HBDatastoreCandidate'] = 'allFeasibleDs'
      allFeasibleDsWithUserPreference: ClassVar['HBDatastoreCandidate'] = 'allFeasibleDsWithUserPreference'

   enabled: Optional[bool] = None
   vmMonitoring: Optional[str] = None
   hostMonitoring: Optional[str] = None
   vmComponentProtecting: Optional[str] = None
   failoverLevel: Optional[int] = None
   admissionControlPolicy: Optional[DasAdmissionControlPolicy] = None
   admissionControlEnabled: Optional[bool] = None
   defaultVmSettings: Optional[DasVmSettings] = None
   option: list[OptionValue] = []
   heartbeatDatastore: list[Datastore] = []
   hBDatastoreCandidatePolicy: Optional[str] = None


class DasData(DynamicData):
   pass


class DasDataSummary(DasData):
   hostListVersion: long
   clusterConfigVersion: long
   compatListVersion: long


class DasFailoverLevelAdvancedRuntimeInfo(DasAdvancedRuntimeInfo):
   class SlotInfo(DynamicData):
      numVcpus: int
      cpuMHz: int
      memoryMB: int

   class HostSlots(DynamicData):
      host: HostSystem
      slots: int

   class VmSlots(DynamicData):
      vm: VirtualMachine
      slots: int

   slotInfo: SlotInfo
   totalSlots: int
   usedSlots: int
   unreservedSlots: int
   totalVms: int
   totalHosts: int
   totalGoodHosts: int
   hostSlots: list[HostSlots] = []
   vmsRequiringMultipleSlots: list[VmSlots] = []

class DasFdmAvailabilityState:
   pass


class DasFdmHostState(DynamicData):
   state: str
   stateReporter: Optional[HostSystem] = None


class DasHostInfo(DynamicData):
   pass


class DasHostRecommendation(DynamicData):
   host: HostSystem
   drsRating: Optional[int] = None


class DasVmConfigInfo(DynamicData):
   class Priority(Enum):
      disabled: ClassVar['Priority'] = 'disabled'
      low: ClassVar['Priority'] = 'low'
      medium: ClassVar['Priority'] = 'medium'
      high: ClassVar['Priority'] = 'high'

   key: VirtualMachine
   restartPriority: Optional[Priority] = None
   powerOffOnIsolation: Optional[bool] = None
   dasSettings: Optional[DasVmSettings] = None


class DasVmConfigSpec(ArrayUpdateSpec):
   info: Optional[DasVmConfigInfo] = None


class DasVmSettings(DynamicData):
   class RestartPriority(Enum):
      disabled: ClassVar['RestartPriority'] = 'disabled'
      lowest: ClassVar['RestartPriority'] = 'lowest'
      low: ClassVar['RestartPriority'] = 'low'
      medium: ClassVar['RestartPriority'] = 'medium'
      high: ClassVar['RestartPriority'] = 'high'
      highest: ClassVar['RestartPriority'] = 'highest'
      clusterRestartPriority: ClassVar['RestartPriority'] = 'clusterRestartPriority'

   class IsolationResponse(Enum):
      none: ClassVar['IsolationResponse'] = 'none'
      powerOff: ClassVar['IsolationResponse'] = 'powerOff'
      shutdown: ClassVar['IsolationResponse'] = 'shutdown'
      clusterIsolationResponse: ClassVar['IsolationResponse'] = 'clusterIsolationResponse'

   restartPriority: Optional[str] = None
   restartPriorityTimeout: Optional[int] = None
   isolationResponse: Optional[str] = None
   vmToolsMonitoringSettings: Optional[VmToolsMonitoringSettings] = None
   vmComponentProtectionSettings: Optional[VmComponentProtectionSettings] = None


class DatastoreUpdateSpec(ArrayUpdateSpec):
   datastore: Optional[Datastore] = None

class DependencyRuleInfo(RuleInfo):
   vmGroup: str
   dependsOnVmGroup: str


class DpmConfigInfo(DynamicData):
   class DpmBehavior(Enum):
      manual: ClassVar['DpmBehavior'] = 'manual'
      automated: ClassVar['DpmBehavior'] = 'automated'

   enabled: Optional[bool] = None
   defaultDpmBehavior: Optional[DpmBehavior] = None
   hostPowerActionRate: Optional[int] = None
   option: list[OptionValue] = []


class DpmHostConfigInfo(DynamicData):
   key: HostSystem
   enabled: Optional[bool] = None
   behavior: Optional[DpmConfigInfo.DpmBehavior] = None


class DpmHostConfigSpec(ArrayUpdateSpec):
   info: Optional[DpmHostConfigInfo] = None


class DrsConfigInfo(DynamicData):
   class DrsBehavior(Enum):
      manual: ClassVar['DrsBehavior'] = 'manual'
      partiallyAutomated: ClassVar['DrsBehavior'] = 'partiallyAutomated'
      fullyAutomated: ClassVar['DrsBehavior'] = 'fullyAutomated'

   enabled: Optional[bool] = None
   enableVmBehaviorOverrides: Optional[bool] = None
   defaultVmBehavior: Optional[DrsBehavior] = None
   vmotionRate: Optional[int] = None
   scaleDescendantsShares: Optional[str] = None
   option: list[OptionValue] = []


class DrsFaults(DynamicData):
   class FaultsByVm(DynamicData):
      vm: Optional[VirtualMachine] = None
      fault: list[MethodFault] = []

   class FaultsByVirtualDisk(FaultsByVm):
      disk: Optional[VirtualDiskId] = None

   reason: str
   faultsByVm: list[FaultsByVm] = []


class DrsMigration(DynamicData):
   key: str
   time: datetime
   vm: VirtualMachine
   cpuLoad: Optional[int] = None
   memoryLoad: Optional[long] = None
   source: HostSystem
   sourceCpuLoad: Optional[int] = None
   sourceMemoryLoad: Optional[long] = None
   destination: HostSystem
   destinationCpuLoad: Optional[int] = None
   destinationMemoryLoad: Optional[long] = None


class DrsRecommendation(DynamicData):
   class ReasonCode(Enum):
      fairnessCpuAvg: ClassVar['ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: ClassVar['ReasonCode'] = 'fairnessMemAvg'
      jointAffin: ClassVar['ReasonCode'] = 'jointAffin'
      antiAffin: ClassVar['ReasonCode'] = 'antiAffin'
      hostMaint: ClassVar['ReasonCode'] = 'hostMaint'

   key: str
   rating: int
   reason: str
   reasonText: str
   migrationList: list[DrsMigration] = []


class DrsVmConfigInfo(DynamicData):
   key: VirtualMachine
   enabled: Optional[bool] = None
   behavior: Optional[DrsConfigInfo.DrsBehavior] = None


class DrsVmConfigSpec(ArrayUpdateSpec):
   info: Optional[DrsVmConfigInfo] = None


class EVCManager(ExtensibleManagedObject):
   class EVCState(DynamicData):
      supportedEVCMode: list[EVCMode] = []
      currentEVCModeKey: Optional[str] = None
      guaranteedCPUFeatures: list[CpuIdInfo] = []
      featureCapability: list[FeatureCapability] = []
      featureMask: list[FeatureMask] = []
      featureRequirement: list[FeatureRequirement] = []

   class CheckResult(DynamicData):
      evcModeKey: str
      error: MethodFault
      host: list[HostSystem] = []

   @property
   def managedCluster(self) -> ClusterComputeResource: ...
   @property
   def evcState(self) -> EVCState: ...

   def ConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: Optional[str]) -> Task: ...
   def DisableEvc(self) -> Task: ...
   def CheckConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: Optional[str]) -> Task: ...
   def CheckAddHostEvc(self, cnxSpec: ConnectSpec) -> Task: ...


class EnterMaintenanceResult(DynamicData):
   recommendations: list[Recommendation] = []
   fault: Optional[DrsFaults] = None


class FailoverHostAdmissionControlInfo(DasAdmissionControlInfo):
   class HostStatus(DynamicData):
      host: HostSystem
      status: ManagedEntity.Status

   hostStatus: list[HostStatus] = []


class FailoverHostAdmissionControlPolicy(DasAdmissionControlPolicy):
   failoverHosts: list[HostSystem] = []
   failoverLevel: Optional[int] = None

class FailoverLevelAdmissionControlInfo(DasAdmissionControlInfo):
   currentFailoverLevel: int


class FailoverLevelAdmissionControlPolicy(DasAdmissionControlPolicy):
   failoverLevel: int
   slotPolicy: Optional[SlotPolicy] = None


class FailoverResourcesAdmissionControlInfo(DasAdmissionControlInfo):
   currentCpuFailoverResourcesPercent: int
   currentMemoryFailoverResourcesPercent: int
   currentPMemFailoverResourcesPercent: Optional[int] = None


class FailoverResourcesAdmissionControlPolicy(DasAdmissionControlPolicy):
   cpuFailoverResourcesPercent: int
   memoryFailoverResourcesPercent: int
   failoverLevel: Optional[int] = None
   autoComputePercentages: Optional[bool] = None
   pMemFailoverResourcesPercent: Optional[int] = None
   autoComputePMemFailoverResourcesPercent: Optional[bool] = None

class FaultDomainDestroySpec(VsanFaultDomainSpec):
   pass

class FaultDomainUpdateSpec(VsanFaultDomainSpec):
   operation: str

class FixedSizeSlotPolicy(SlotPolicy):
   cpu: int
   memory: int


class FtVmHostRuleInfo(RuleInfo):
   vmGroupName: str
   hostGroupName: list[str] = []


class GroupInfo(DynamicData):
   name: str
   userCreated: Optional[bool] = None
   uniqueID: Optional[str] = None


class GroupSpec(ArrayUpdateSpec):
   info: Optional[GroupInfo] = None


class HostGroup(GroupInfo):
   host: list[HostSystem] = []


class HostInfraUpdateHaModeAction(Action):
   class OperationType(Enum):
      enterQuarantine: ClassVar['OperationType'] = 'enterQuarantine'
      exitQuarantine: ClassVar['OperationType'] = 'exitQuarantine'
      enterMaintenance: ClassVar['OperationType'] = 'enterMaintenance'

   operationType: str


class HostPowerAction(Action):
   class OperationType(Enum):
      powerOn: ClassVar['OperationType'] = 'powerOn'
      powerOff: ClassVar['OperationType'] = 'powerOff'

   operationType: OperationType
   powerConsumptionWatt: Optional[int] = None
   cpuCapacityMHz: Optional[int] = None
   memCapacityMB: Optional[int] = None


class HostRecommendation(DynamicData):
   host: HostSystem
   rating: int


class InfraUpdateHaConfigInfo(DynamicData):
   class BehaviorType(Enum):
      Manual: ClassVar['BehaviorType'] = 'Manual'
      Automated: ClassVar['BehaviorType'] = 'Automated'

   class RemediationType(Enum):
      QuarantineMode: ClassVar['RemediationType'] = 'QuarantineMode'
      MaintenanceMode: ClassVar['RemediationType'] = 'MaintenanceMode'

   enabled: Optional[bool] = None
   behavior: Optional[str] = None
   moderateRemediation: Optional[str] = None
   severeRemediation: Optional[str] = None
   providers: list[str] = []


class InitialPlacementAction(Action):
   targetHost: HostSystem
   pool: Optional[ResourcePool] = None


class MigrationAction(Action):
   drsMigration: Optional[DrsMigration] = None


class NotAttemptedVmInfo(DynamicData):
   vm: VirtualMachine
   fault: MethodFault


class OrchestrationInfo(DynamicData):
   defaultVmReadiness: Optional[VmReadiness] = None


class PerformClusterPowerActionSpec(DynamicData):
   targetPowerStatus: str
   isOrchestration: Optional[bool] = None
   initialPowerStatus: Optional[str] = None
   powerOffReason: Optional[str] = None
   infraVMs: list[VirtualMachine] = []
   infraVMUuids: list[str] = []


class PlacementAction(Action):
   vm: Optional[VirtualMachine] = None
   targetHost: Optional[HostSystem] = None
   relocateSpec: Optional[RelocateSpec] = None


class PlacementResult(DynamicData):
   recommendations: list[Recommendation] = []
   drsFault: Optional[DrsFaults] = None


class PlacementSpec(DynamicData):
   class PlacementType(Enum):
      create: ClassVar['PlacementType'] = 'create'
      reconfigure: ClassVar['PlacementType'] = 'reconfigure'
      relocate: ClassVar['PlacementType'] = 'relocate'
      clone: ClassVar['PlacementType'] = 'clone'

   priority: Optional[VirtualMachine.MovePriority] = None
   vm: Optional[VirtualMachine] = None
   configSpec: Optional[ConfigSpec] = None
   relocateSpec: Optional[RelocateSpec] = None
   hosts: list[HostSystem] = []
   datastores: list[Datastore] = []
   storagePods: list[StoragePod] = []
   disallowPrerequisiteMoves: Optional[bool] = None
   rules: list[RuleInfo] = []
   key: Optional[str] = None
   placementType: Optional[str] = None
   cloneSpec: Optional[CloneSpec] = None
   cloneName: Optional[str] = None

class PowerOnVmOption:
   pass


class PowerOnVmResult(DynamicData):
   attempted: list[AttemptedVmInfo] = []
   notAttempted: list[NotAttemptedVmInfo] = []
   recommendations: list[Recommendation] = []


class PreemptibleVmPairInfo(DynamicData):
   id: Optional[int] = None
   monitoredVm: VirtualMachine
   preemptibleVm: VirtualMachine


class PreemptibleVmPairSpec(ArrayUpdateSpec):
   info: Optional[PreemptibleVmPairInfo] = None


class ProactiveDrsConfigInfo(DynamicData):
   enabled: Optional[bool] = None


class QueryVsanManagedStorageSpaceUsageSpec(DynamicData):
   datastoreTypes: list[str] = []


class Recommendation(DynamicData):
   class RecommendationType(Enum):
      V1: ClassVar['RecommendationType'] = 'V1'

   class ReasonCode(Enum):
      fairnessCpuAvg: ClassVar['ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: ClassVar['ReasonCode'] = 'fairnessMemAvg'
      jointAffin: ClassVar['ReasonCode'] = 'jointAffin'
      antiAffin: ClassVar['ReasonCode'] = 'antiAffin'
      hostMaint: ClassVar['ReasonCode'] = 'hostMaint'
      enterStandby: ClassVar['ReasonCode'] = 'enterStandby'
      reservationCpu: ClassVar['ReasonCode'] = 'reservationCpu'
      reservationMem: ClassVar['ReasonCode'] = 'reservationMem'
      powerOnVm: ClassVar['ReasonCode'] = 'powerOnVm'
      powerSaving: ClassVar['ReasonCode'] = 'powerSaving'
      increaseCapacity: ClassVar['ReasonCode'] = 'increaseCapacity'
      checkResource: ClassVar['ReasonCode'] = 'checkResource'
      unreservedCapacity: ClassVar['ReasonCode'] = 'unreservedCapacity'
      colocateCommunicatingVM: ClassVar['ReasonCode'] = 'colocateCommunicatingVM'
      balanceNetworkBandwidthUsage: ClassVar['ReasonCode'] = 'balanceNetworkBandwidthUsage'
      vmHostHardAffinity: ClassVar['ReasonCode'] = 'vmHostHardAffinity'
      vmHostSoftAffinity: ClassVar['ReasonCode'] = 'vmHostSoftAffinity'
      increaseAllocation: ClassVar['ReasonCode'] = 'increaseAllocation'
      balanceDatastoreSpaceUsage: ClassVar['ReasonCode'] = 'balanceDatastoreSpaceUsage'
      balanceDatastoreIOLoad: ClassVar['ReasonCode'] = 'balanceDatastoreIOLoad'
      balanceDatastoreIOPSReservation: ClassVar['ReasonCode'] = 'balanceDatastoreIOPSReservation'
      datastoreMaint: ClassVar['ReasonCode'] = 'datastoreMaint'
      virtualDiskJointAffin: ClassVar['ReasonCode'] = 'virtualDiskJointAffin'
      virtualDiskAntiAffin: ClassVar['ReasonCode'] = 'virtualDiskAntiAffin'
      datastoreSpaceOutage: ClassVar['ReasonCode'] = 'datastoreSpaceOutage'
      storagePlacement: ClassVar['ReasonCode'] = 'storagePlacement'
      iolbDisabledInternal: ClassVar['ReasonCode'] = 'iolbDisabledInternal'
      xvmotionPlacement: ClassVar['ReasonCode'] = 'xvmotionPlacement'
      networkBandwidthReservation: ClassVar['ReasonCode'] = 'networkBandwidthReservation'
      hostInDegradation: ClassVar['ReasonCode'] = 'hostInDegradation'
      hostExitDegradation: ClassVar['ReasonCode'] = 'hostExitDegradation'
      maxVmsConstraint: ClassVar['ReasonCode'] = 'maxVmsConstraint'
      ftConstraints: ClassVar['ReasonCode'] = 'ftConstraints'
      vmHostAffinityPolicy: ClassVar['ReasonCode'] = 'vmHostAffinityPolicy'
      vmHostAntiAffinityPolicy: ClassVar['ReasonCode'] = 'vmHostAntiAffinityPolicy'
      vmAntiAffinityPolicy: ClassVar['ReasonCode'] = 'vmAntiAffinityPolicy'
      balanceVsanUsage: ClassVar['ReasonCode'] = 'balanceVsanUsage'
      ahPlacementOptimization: ClassVar['ReasonCode'] = 'ahPlacementOptimization'
      vmxUpgrade: ClassVar['ReasonCode'] = 'vmxUpgrade'

   key: str
   type: str
   time: datetime
   rating: int
   reason: str
   reasonText: str
   warningText: Optional[str] = None
   warningDetails: Optional[LocalizableMessage] = None
   prerequisite: list[str] = []
   action: list[Action] = []
   target: Optional[ManagedObject] = None


class ResourceUsageSummary(DynamicData):
   cpuUsedMHz: int
   cpuCapacityMHz: int
   memUsedMB: int
   memCapacityMB: int
   pMemAvailableMB: Optional[long] = None
   pMemCapacityMB: Optional[long] = None
   storageUsedMB: long
   storageCapacityMB: long


class RuleInfo(DynamicData):
   key: Optional[int] = None
   status: Optional[ManagedEntity.Status] = None
   enabled: Optional[bool] = None
   name: Optional[str] = None
   mandatory: Optional[bool] = None
   userCreated: Optional[bool] = None
   inCompliance: Optional[bool] = None
   ruleUuid: Optional[str] = None


class RuleSpec(ArrayUpdateSpec):
   info: Optional[RuleInfo] = None


class SiteFaultDomain(DynamicData):
   hosts: list[HostSystem] = []
   name: str


class SiteFaultDomainConfig(DynamicData):
   siteFaultDomains: list[SiteFaultDomain] = []


class SlotPolicy(DynamicData):
   pass


class StorageComplianceResult(DynamicData):
   class StorageComplianceStatus(Enum):
      compliant: ClassVar['StorageComplianceStatus'] = 'compliant'
      nonCompliant: ClassVar['StorageComplianceStatus'] = 'nonCompliant'
      unknown: ClassVar['StorageComplianceStatus'] = 'unknown'
      notApplicable: ClassVar['StorageComplianceStatus'] = 'notApplicable'

   checkTime: Optional[datetime] = None
   profile: Optional[str] = None
   objectUUID: Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[StoragePolicyStatus] = []
   operationalStatus: Optional[StorageOperationalStatus] = None
   objPolicyGenerationId: Optional[str] = None


class StorageOperationalStatus(DynamicData):
   healthy: Optional[bool] = None
   operationETA: Optional[datetime] = None
   operationProgress: Optional[long] = None
   transitional: Optional[bool] = None


class StoragePolicyStatus(DynamicData):
   id: Optional[str] = None
   expectedValue: Optional[str] = None
   currentValue: Optional[str] = None


class SystemVMsConfigInfo(DynamicData):
   class DeploymentMode(Enum):
      SYSTEM_MANAGED: ClassVar['DeploymentMode'] = 'SYSTEM_MANAGED'
      ABSENT: ClassVar['DeploymentMode'] = 'ABSENT'

   allowedDatastores: list[Datastore] = []
   notAllowedDatastores: list[Datastore] = []
   dsTagCategoriesToExclude: list[str] = []
   deploymentMode: Optional[str] = None


class SystemVMsConfigSpec(DynamicData):
   allowedDatastores: list[DatastoreUpdateSpec] = []
   notAllowedDatastores: list[DatastoreUpdateSpec] = []
   dsTagCategoriesToExclude: list[TagCategoryUpdateSpec] = []
   deploymentMode: Optional[str] = None


class TagCategoryUpdateSpec(ArrayUpdateSpec):
   category: Optional[str] = None


class UsageSummary(DynamicData):
   totalCpuCapacityMhz: int
   totalMemCapacityMB: int
   cpuReservationMhz: int
   memReservationMB: int
   poweredOffCpuReservationMhz: Optional[int] = None
   poweredOffMemReservationMB: Optional[int] = None
   cpuDemandMhz: int
   memDemandMB: int
   statsGenNumber: long
   cpuEntitledMhz: int
   memEntitledMB: int
   poweredOffVmCount: int
   totalVmCount: int
   tier0MemCapacityMB: Optional[int] = None
   reservedTier0MemMB: Optional[int] = None
   unreservedTier0MemMB: Optional[int] = None


class VSANPreferredFaultDomainInfo(DynamicData):
   preferredFaultDomainName: Optional[str] = None
   preferredFaultDomainId: Optional[str] = None


class VSANStretchedClusterCapability(DynamicData):
   hostMoId: str
   connStatus: Optional[str] = None
   isSupported: Optional[bool] = None
   hostCapability: Optional[VSANStretchedClusterHostCapability] = None


class VSANStretchedClusterFaultDomainConfig(DynamicData):
   firstFdName: str
   firstFdHosts: list[HostSystem] = []
   secondFdName: str
   secondFdHosts: list[HostSystem] = []


class VSANStretchedClusterHostVirtualApplianceStatus(DynamicData):
   vcCluster: Optional[ClusterComputeResource] = None
   isVirtualApp: Optional[bool] = None
   vcClusters: list[ClusterComputeResource] = []
   isVirtualAppValid: Optional[bool] = None


class VSANWitnessHostInfo(DynamicData):
   nodeUuid: str
   faultDomainName: Optional[str] = None
   preferredFdName: Optional[str] = None
   preferredFdUuid: Optional[str] = None
   unicastAgentAddr: Optional[str] = None
   host: Optional[HostSystem] = None
   metadataMode: Optional[bool] = None


class VmComponentProtectionSettings(DynamicData):
   class StorageVmReaction(Enum):
      disabled: ClassVar['StorageVmReaction'] = 'disabled'
      warning: ClassVar['StorageVmReaction'] = 'warning'
      restartConservative: ClassVar['StorageVmReaction'] = 'restartConservative'
      restartAggressive: ClassVar['StorageVmReaction'] = 'restartAggressive'
      clusterDefault: ClassVar['StorageVmReaction'] = 'clusterDefault'

   class VmReactionOnAPDCleared(Enum):
      none: ClassVar['VmReactionOnAPDCleared'] = 'none'
      reset: ClassVar['VmReactionOnAPDCleared'] = 'reset'
      useClusterDefault: ClassVar['VmReactionOnAPDCleared'] = 'useClusterDefault'

   vmStorageProtectionForAPD: Optional[str] = None
   enableAPDTimeoutForHosts: Optional[bool] = None
   vmTerminateDelayForAPDSec: Optional[int] = None
   vmReactionOnAPDCleared: Optional[str] = None
   vmStorageProtectionForPDL: Optional[str] = None


class VmGroup(GroupInfo):
   vm: list[VirtualMachine] = []


class VmHostRuleInfo(RuleInfo):
   vmGroupName: Optional[str] = None
   affineHostGroupName: Optional[str] = None
   antiAffineHostGroupName: Optional[str] = None


class VmOrchestrationInfo(DynamicData):
   vm: VirtualMachine
   vmReadiness: VmReadiness


class VmOrchestrationSpec(ArrayUpdateSpec):
   info: Optional[VmOrchestrationInfo] = None


class VmReadiness(DynamicData):
   class ReadyCondition(Enum):
      none: ClassVar['ReadyCondition'] = 'none'
      poweredOn: ClassVar['ReadyCondition'] = 'poweredOn'
      guestHbStatusGreen: ClassVar['ReadyCondition'] = 'guestHbStatusGreen'
      appHbStatusGreen: ClassVar['ReadyCondition'] = 'appHbStatusGreen'
      useClusterDefault: ClassVar['ReadyCondition'] = 'useClusterDefault'

   readyCondition: Optional[str] = None
   postReadyDelay: Optional[int] = None


class VmToolsMonitoringSettings(DynamicData):
   enabled: Optional[bool] = None
   vmMonitoring: Optional[str] = None
   clusterSettings: Optional[bool] = None
   failureInterval: Optional[int] = None
   minUpTime: Optional[int] = None
   maxFailures: Optional[int] = None
   maxFailureWindow: Optional[int] = None


class VsanAttachToSrOperation(DynamicData):
   task: Optional[Task] = None
   success: Optional[bool] = None
   timestamp: Optional[datetime] = None
   srNumber: str

class VsanBaselinePreferenceType:
   pass


class VsanCapability(DynamicData):
   target: Optional[ManagedObject] = None
   capabilities: list[str] = []
   statuses: list[str] = []

class VsanCapabilityStatus:
   pass


class VsanCapabilitySystem(ManagedObject):
   def GetCapabilities(self, targets: list[ManagedObject]) -> list[VsanCapability]: ...

class VsanCapabilityType:
   pass

class VsanCapabilityType90:
   pass

class VsanCapabilityType91:
   pass


class VsanClientServerHciMeshDitEncryptionHealthSummary(DynamicData):
   clusterUuid: str
   clusterName: str
   ownerVc: Optional[str] = None
   isLocalOwnerVc: Optional[bool] = None
   health: str
   issues: list[str] = []


class VsanClusterAdvCfgSyncHostResult(DynamicData):
   hostname: str
   value: str
   isDefault: Optional[bool] = None


class VsanClusterAdvCfgSyncResult(DynamicData):
   inSync: bool
   name: str
   hostValues: list[VsanClusterAdvCfgSyncHostResult] = []


class VsanClusterBalancePerDiskInfo(DynamicData):
   uuid: Optional[str] = None
   fullness: long
   variance: long
   fullnessAboveThreshold: long
   dataToMoveB: long
   compFullness: Optional[long] = None
   compVariance: Optional[long] = None


class VsanClusterBalanceSummary(DynamicData):
   varianceThreshold: long
   disks: list[VsanClusterBalancePerDiskInfo] = []


class VsanClusterClomdLivenessResult(DynamicData):
   clomdLivenessResult: list[VsanHostClomdLivenessResult] = []
   issueFound: bool


class VsanClusterConfig(DynamicData):
   config: ConfigInfo
   name: str
   hosts: list[str] = []
   toBeDeleted: Optional[bool] = None


class VsanClusterCreateVmHealthTestResult(DynamicData):
   clusterResult: VsanClusterProactiveTestResult
   hostResults: list[VsanHostCreateVmHealthTestResult] = []


class VsanClusterDitEncryptionHealthSummary(DynamicData):
   overallHealth: str
   enabled: Optional[bool] = None
   hostResults: list[VsanDitEncryptionHealthSummary] = []


class VsanClusterEncryptionHealthSummary(DynamicData):
   overallHealth: Optional[str] = None
   configHealth: Optional[str] = None
   kmsHealth: Optional[str] = None
   vcKmsResult: Optional[VsanVcKmipServersHealth] = None
   hostResults: list[VsanEncryptionHealthSummary] = []
   aesniHealth: Optional[str] = None


class VsanClusterFileServiceHealthSummary(DynamicData):
   overallHealth: Optional[str] = None
   hostResults: list[VsanFileServiceHealthSummary] = []


class VsanClusterGlobalDedupHealthSummary(DynamicData):
   dedupConfigHealth: list[VsanHostGlobalDedupConfigHealthSummary] = []
   dedupStoreHealth: Optional[str] = None


class VsanClusterHciMeshDitEncryptionHealthSummary(DynamicData):
   overallHealth: str
   hostClientClusterSummary: list[VsanHostHciMeshDitEncryptionHealthSummary] = []
   hostServerClusterSummary: list[VsanHostHciMeshDitEncryptionHealthSummary] = []
   serverClusterSummary: list[VsanClientServerHciMeshDitEncryptionHealthSummary] = []


class VsanClusterHclInfo(DynamicData):
   hclDbLastUpdate: Optional[datetime] = None
   hclDbAgeHealth: Optional[str] = None
   hostResults: list[VsanHostHclInfo] = []
   updateItems: list[VsanUpdateItem] = []
   hclDbAbsent: Optional[bool] = None


class VsanClusterHealthAction(DynamicData):
   class VsanClusterHealthActionIdEnum(Enum):
      RepairClusterObjectsAction: ClassVar['VsanClusterHealthActionIdEnum'] = 'RepairClusterObjectsAction'
      UploadHclDb: ClassVar['VsanClusterHealthActionIdEnum'] = 'UploadHclDb'
      UpdateHclDbFromInternet: ClassVar['VsanClusterHealthActionIdEnum'] = 'UpdateHclDbFromInternet'
      EnableHealthService: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableHealthService'
      DiskBalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'DiskBalance'
      StopDiskBalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'StopDiskBalance'
      RemediateDedup: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateDedup'
      UpgradeVsanDiskFormat: ClassVar['VsanClusterHealthActionIdEnum'] = 'UpgradeVsanDiskFormat'
      CreateDVS: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateDVS'
      ConfigureHA: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureHA'
      ConfigureDRS: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureDRS'
      ConfigureVSAN: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureVSAN'
      ClaimVSANDisks: ClassVar['VsanClusterHealthActionIdEnum'] = 'ClaimVSANDisks'
      ClusterUpgrade: ClassVar['VsanClusterHealthActionIdEnum'] = 'ClusterUpgrade'
      CreateVMKnic: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateVMKnic'
      CreateVMKnicWithVMotion: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateVMKnicWithVMotion'
      RunBurnInTest: ClassVar['VsanClusterHealthActionIdEnum'] = 'RunBurnInTest'
      EnableIscsiTargetService: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableIscsiTargetService'
      EnablePerformanceServiceAction: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnablePerformanceServiceAction'
      RemediateClusterConfig: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateClusterConfig'
      EnableCeip: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableCeip'
      LoginVumIsoDepot: ClassVar['VsanClusterHealthActionIdEnum'] = 'LoginVumIsoDepot'
      PurgeInaccessSwapObjs: ClassVar['VsanClusterHealthActionIdEnum'] = 'PurgeInaccessSwapObjs'
      UploadReleaseCatalog: ClassVar['VsanClusterHealthActionIdEnum'] = 'UploadReleaseCatalog'
      ConfigureAutomaticRebalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureAutomaticRebalance'
      RemediateFileService: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateFileService'
      RelayoutVsanObjects: ClassVar['VsanClusterHealthActionIdEnum'] = 'RelayoutVsanObjects'
      RemediateFileServiceImbalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateFileServiceImbalance'
      SelectNvme: ClassVar['VsanClusterHealthActionIdEnum'] = 'SelectNvme'
      CreateFileServiceDomain: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateFileServiceDomain'
      RemediateIscsiLunsRuntimeStatus: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateIscsiLunsRuntimeStatus'
      ShallowRekey: ClassVar['VsanClusterHealthActionIdEnum'] = 'ShallowRekey'
      VsanClusterHealthActionIdEnum_Unknown: ClassVar['VsanClusterHealthActionIdEnum'] = 'VsanClusterHealthActionIdEnum_Unknown'

   actionId: str
   actionLabel: LocalizableMessage
   actionDescription: LocalizableMessage
   enabled: bool
   parameters: list[KeyValue] = []

class VsanClusterHealthCategoryEnum:
   pass


class VsanClusterHealthCheckInfo(DynamicData):
   testId: str
   testName: Optional[str] = None
   groupId: str
   groupName: Optional[str] = None


class VsanClusterHealthConfigs(DynamicData):
   enableVsanTelemetry: Optional[bool] = None
   vsanTelemetryInterval: Optional[int] = None
   vsanTelemetryProxy: Optional[VsanClusterTelemetryProxyConfig] = None
   configs: list[VsanClusterHealthResultKeyValuePair] = []


class VsanClusterHealthExternalLink(VsanClusterHealthLinkBase):
   url: str
   category: Optional[str] = None


class VsanClusterHealthGroup(DynamicData):
   groupId: str
   groupName: str
   groupHealth: str
   groupTests: list[VsanClusterHealthTest] = []
   groupDetails: list[VsanClusterHealthResultBase] = []
   inProgress: Optional[bool] = None


class VsanClusterHealthLinkBase(DynamicData):
   label: Optional[str] = None


class VsanClusterHealthQuerySpec(DynamicData):
   task: Optional[Task] = None
   diskNames: list[str] = []
   includeHealthRemediation: Optional[bool] = None
   excludeChecks: list[str] = []


class VsanClusterHealthResultBase(DynamicData):
   label: Optional[str] = None


class VsanClusterHealthResultColumnInfo(DynamicData):
   label: str
   type: str


class VsanClusterHealthResultKeyValuePair(DynamicData):
   key: Optional[str] = None
   value: Optional[str] = None


class VsanClusterHealthResultRow(DynamicData):
   values: list[str] = []
   nestedRows: list[VsanClusterHealthResultRow] = []
   actions: list[VsanHealthDataDrivenAction] = []


class VsanClusterHealthResultTable(VsanClusterHealthResultBase):
   columns: list[VsanClusterHealthResultColumnInfo] = []
   rows: list[VsanClusterHealthResultRow] = []


class VsanClusterHealthResultWithRemediation(VsanClusterHealthResultBase):
   issueDescription: Optional[str] = None
   issueDetail: list[VsanClusterHealthResultTable] = []
   troubleshooting: Optional[VsanHealthTroubleshooting] = None
   additionalResources: list[VsanClusterHealthExternalLink] = []


class VsanClusterHealthSummary(DynamicData):
   clusterStatus: Optional[VsanClusterHealthSystemStatusResult] = None
   timestamp: Optional[datetime] = None
   clusterVersions: Optional[VsanClusterHealthSystemVersionResult] = None
   objectHealth: Optional[VsanObjectOverallHealth] = None
   vmHealth: Optional[VsanClusterVMsHealthOverallResult] = None
   networkHealth: Optional[VsanClusterNetworkHealthResult] = None
   limitHealth: Optional[VsanClusterLimitHealthResult] = None
   advCfgSync: list[VsanClusterAdvCfgSyncResult] = []
   createVmHealth: list[VsanHostCreateVmHealthTestResult] = []
   physicalDisksHealth: list[VsanPhysicalDiskHealthSummary] = []
   encryptionHealth: Optional[VsanClusterEncryptionHealthSummary] = None
   hclInfo: Optional[VsanClusterHclInfo] = None
   groups: list[VsanClusterHealthGroup] = []
   overallHealth: str
   overallHealthDescription: str
   clomdLiveness: Optional[VsanClusterClomdLivenessResult] = None
   diskBalance: Optional[VsanClusterBalanceSummary] = None
   genericCluster: Optional[VsanGenericClusterBestPracticeHealth] = None
   networkConfig: Optional[VsanNetworkConfigBestPracticeHealth] = None
   vsanConfig: Optional[VsanConfigCheckResult] = None
   burnInTest: Optional[VsanBurnInTestCheckResult] = None
   perfsvcHealth: Optional[VsanPerfsvcHealthResult] = None
   cluster: Optional[ClusterComputeResource] = None
   fileServiceHealth: Optional[VsanClusterFileServiceHealthSummary] = None
   ditEncryptionHealth: Optional[VsanClusterDitEncryptionHealthSummary] = None
   healthScore: Optional[int] = None
   globalDedupHealth: Optional[VsanClusterGlobalDedupHealthSummary] = None
   hciMeshDitEncryptionHealth: Optional[VsanClusterHciMeshDitEncryptionHealthSummary] = None
   healthStatusCounts: Optional[VsanHealthStatusCounts] = None


class VsanClusterHealthSystem(ManagedObject):
   def QueryVerifyClusterNetworkSettings(self, hosts: list[str], esxRootPassword: str) -> VsanClusterNetworkHealthResult: ...
   def QueryCheckLimits(self, hosts: list[str], esxRootPassword: str) -> VsanClusterLimitHealthResult: ...
   def QueryPhysicalDiskHealthSummary(self, hosts: list[str], esxRootPassword: str) -> list[VsanPhysicalDiskHealthSummary]: ...
   def QueryAdvCfgSync(self, hosts: list[str], esxRootPassword: str, options: list[str]) -> list[VsanClusterAdvCfgSyncResult]: ...
   def QueryClusterCreateVmHealthTest(self, hosts: list[str], esxRootPassword: str, timeout: int) -> VsanClusterCreateVmHealthTestResult: ...
   def QueryClusterNetworkPerfTest(self, hosts: list[str], esxRootPassword: str, multicast: bool, durationSec: Optional[int]) -> VsanClusterNetworkLoadTestResult: ...
   def QueryCaptureVsanPcap(self, hosts: list[str], esxRootPassword: str, duration: int, vmknic: list[VsanClusterHostVmknicMapping], includeRawPcap: Optional[bool], includeIgmp: Optional[bool], cmmdsMsgTypeFilter: list[str], cmmdsPorts: list[int], clusterUuid: Optional[str]) -> VsanVsanClusterPcapResult: ...
   def QueryClusterHealthSystemVersions(self, hosts: list[str], esxRootPassword: str) -> VsanClusterHealthSystemVersionResult: ...
   def CheckClusterClomdLiveness(self, hosts: list[str], esxRootPassword: str) -> VsanClusterClomdLivenessResult: ...
   def RepairClusterImmediateObjects(self, hosts: list[str], esxRootPassword: str, uuids: list[str]) -> VsanClusterHealthSystemObjectsRepairResult: ...
   def GetClusterHclInfo(self, hosts: list[str], esxRootPassword: str) -> VsanClusterHclInfo: ...


class VsanClusterHealthSystemObjectsRepairResult(DynamicData):
   inRepairingQueueObjects: list[str] = []
   failedRepairObjects: list[VsanFailedRepairObjectResult] = []
   issueFound: bool


class VsanClusterHealthSystemStatusResult(DynamicData):
   status: str
   goalState: str
   untrackedHosts: list[str] = []
   trackedHostsStatus: list[VsanHostHealthSystemStatusResult] = []


class VsanClusterHealthSystemVersionResult(DynamicData):
   hostResults: list[VsanHostHealthSystemVersionResult] = []
   vcVersion: Optional[str] = None
   issueFound: bool
   upgradePossible: Optional[bool] = None
   vcBuild: Optional[str] = None


class VsanClusterHealthTest(DynamicData):
   testId: Optional[str] = None
   testName: Optional[str] = None
   testDescription: Optional[str] = None
   testShortDescription: Optional[str] = None
   testHealthyEntities: Optional[int] = None
   testAllEntities: Optional[int] = None
   testHealth: Optional[str] = None
   testDetails: list[VsanClusterHealthResultBase] = []
   testActions: list[VsanClusterHealthAction] = []
   historicalResults: list[VsanHistoricalHealthTest] = []
   testCorrelation: Optional[VsanHealthCorrelation] = None
   reducedScore: Optional[int] = None
   category: Optional[str] = None
   riskIfNotFix: Optional[str] = None
   lastStatusChangeTime: Optional[datetime] = None


class VsanClusterHostVmknicMapping(DynamicData):
   host: str
   vmknic: str


class VsanClusterLimitHealthResult(DynamicData):
   issueFound: bool
   componentLimitHealth: str
   diskFreeSpaceHealth: str
   rcFreeReservationHealth: str
   hostResults: list[VsanLimitHealthResult] = []
   whatifHostFailures: list[VsanClusterWhatifHostFailuresResult] = []
   hostsCommFailure: list[str] = []


class VsanClusterMgmtInternalSystem(ManagedObject):
   def RemediateVsanCluster(self, cluster: ClusterComputeResource) -> Task: ...
   def RemediateVsanHost(self, host: HostSystem) -> Task: ...


class VsanClusterNetworkHealthResult(DynamicData):
   hostResults: list[VsanNetworkHealthResult] = []
   issueFound: Optional[bool] = None
   vsanVmknicPresent: Optional[bool] = None
   matchingMulticastConfig: Optional[bool] = None
   matchingIpSubnets: Optional[bool] = None
   pingTestSuccess: Optional[bool] = None
   largePingTestSuccess: Optional[bool] = None
   hostLatencyCheckSuccess: Optional[bool] = None
   potentialMulticastIssue: Optional[bool] = None
   otherHostsInVsanCluster: list[str] = []
   partitions: list[VsanClusterNetworkPartitionInfo] = []
   hostsWithVsanDisabled: list[str] = []
   hostsDisconnected: list[str] = []
   hostsCommFailure: list[str] = []
   hostsInEsxMaintenanceMode: list[str] = []
   hostsInVsanMaintenanceMode: list[str] = []
   infoAboutUnexpectedHosts: list[VsanQueryResultHostInfo] = []
   clusterInUnicastMode: Optional[bool] = None
   clusterInRDMAMode: Optional[bool] = None


class VsanClusterNetworkLoadTestResult(DynamicData):
   clusterResult: VsanClusterProactiveTestResult
   hostResults: list[VsanNetworkLoadTestResult] = []


class VsanClusterNetworkPartitionInfo(DynamicData):
   hosts: list[str] = []
   partitionUnknown: Optional[bool] = None


class VsanClusterNetworkPerfTaskSpec(DynamicData):
   Cluster: Optional[ClusterComputeResource] = None
   DurationSec: Optional[int] = None
   ownerVc: Optional[str] = None


class VsanClusterPowerSystem(ManagedObject):
   def PerformClusterPowerAction(self, cluster: ComputeResource, spec: PerformClusterPowerActionSpec) -> Task: ...
   def QueryClusterPowerContext(self, cluster: ComputeResource) -> ClusterPowerContext: ...
   def UpdateClusterPowerStatus(self, cluster: ComputeResource, status: str) -> bool: ...


class VsanClusterProactiveTestResult(DynamicData):
   overallStatus: str
   overallStatusDescription: str
   timestamp: datetime
   healthTest: Optional[VsanClusterHealthTest] = None


class VsanClusterTelemetryProxyConfig(DynamicData):
   host: Optional[str] = None
   port: Optional[int] = None
   user: Optional[str] = None
   password: Optional[str] = None
   autoDiscovered: Optional[bool] = None


class VsanClusterVMsHealthOverallResult(DynamicData):
   healthStateList: list[VsanClusterVMsHealthSummaryResult] = []
   overallHealthState: Optional[str] = None


class VsanClusterVMsHealthSummaryResult(DynamicData):
   numVMs: int
   state: Optional[str] = None
   health: str
   vmInstanceUuids: list[str] = []


class VsanClusterVmdkLoadTestResult(DynamicData):
   task: Optional[Task] = None
   clusterResult: Optional[VsanClusterProactiveTestResult] = None
   hostResults: list[VsanHostVmdkLoadTestResult] = []


class VsanClusterWhatifHostFailuresResult(DynamicData):
   numFailures: long
   totalUsedCapacityB: long
   totalCapacityB: long
   totalRcReservationB: long
   totalRcSizeB: long
   usedComponents: long
   totalComponents: long
   componentLimitHealth: Optional[str] = None
   diskFreeSpaceHealth: Optional[str] = None
   rcFreeReservationHealth: Optional[str] = None
   slackSpaceCapRequired: Optional[long] = None
   diskSpaceThreshold: Optional[VsanHealthThreshold] = None
   capacityReservationInfo: Optional[CapacityReservationInfo] = None


class VsanComponentBasicInfo(DynamicData):
   uuid: str
   componentState: str
   hostName: str
   hostNodeUuid: str
   faultDomainUuid: Optional[str] = None
   faultDomainName: Optional[str] = None
   cacheDiskInfo: Optional[DiskInfo] = None
   capacityDiskInfo: Optional[DiskInfo] = None


class VsanComponentPlacement(DynamicData):
   type: str
   children: list[VsanComponentPlacement] = []
   basicInfo: Optional[VsanComponentBasicInfo] = None

class VsanComponentStates:
   pass


class VsanConfigGeneration(DynamicData):
   vcUuid: str
   genNum: long
   genTime: long


class VsanDataDrivenAPIAction(DynamicData):
   actionId: str
   actionLabel: LocalizableMessage
   actionDescription: LocalizableMessage
   enabled: bool
   parameters: list[KeyValue] = []

class VsanDatastoreType:
   pass


class VsanDiagnosticsSystem(ManagedObject):
   def QueryNetworkDiagnostics(self, cluster: ComputeResource, host: Optional[HostSystem]) -> list[VsanNetworkDiagnostics]: ...
   def GetThresholds(self, cluster: ComputeResource, entityType: Optional[str], metric: Optional[str]) -> list[VsanDiagnosticsThreshold]: ...
   def SetThresholds(self, cluster: ComputeResource, thresholds: list[VsanDiagnosticsThreshold]) -> None: ...
   def StartIODiagnosticsTask(self, targets: list[IODiagnosticsTarget], cluster: Optional[ClusterComputeResource], duration: Optional[long]) -> Task: ...
   def QueryIODiagnosticsInstances(self, querySpec: IODiagnosticsInstanceQuerySpec, cluster: Optional[ClusterComputeResource]) -> list[IODiagnosticsInstance]: ...
   def QueryIODiagnosticsStats(self, instanceName: str, cluster: Optional[ClusterComputeResource]) -> list[IODiagnosticsTargetStats]: ...
   def CreateIOTripAnalyzerRecurrences(self, cluster: ComputeResource, recurrences: list[VsanIOTripAnalyzerRecurrence]) -> list[VsanIOTripAnalyzerRecurrence]: ...
   def GetIOTripAnalyzerSchedulerConfig(self, cluster: ComputeResource) -> Optional[VsanIOTripAnalyzerConfig]: ...
   def EditIOTripAnalyzerRecurrences(self, cluster: ComputeResource, recurrences: list[VsanIOTripAnalyzerRecurrence]) -> list[VsanIOTripAnalyzerRecurrence]: ...
   def RemoveIOTripAnalyzerRecurrences(self, cluster: ComputeResource, names: list[str]) -> None: ...
   def SetTraceObjectPolicy(self, cluster: Optional[ComputeResource], traceObjectUuid: str, profile: Optional[ProfileSpec]) -> bool: ...


class VsanDiagnosticsThreshold(DynamicData):
   entityType: str
   metric: str
   yellow: Optional[int] = None
   red: Optional[int] = None


class VsanDiskFormatConversionCheckResult(VsanUpgradeSystem.PreflightCheckResult):
   isSupported: bool
   targetVersion: Optional[int] = None
   isDataMovementRequired: Optional[bool] = None
   storagePoolDisk: Optional[str] = None


class VsanDiskFormatConversionSpec(DynamicData):
   dataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   dataEncryptionConfig: Optional[DataEncryptionConfig] = None
   skipHostRemediation: Optional[bool] = None
   allowDataMovement: Optional[bool] = None


class VsanDiskMappingsConfigSpec(DynamicData):
   hostDiskMappings: list[VsanHostDiskMapping] = []


class VsanEffectiveSpaceUsage(DynamicData):
   totalUsableB: long
   freeUsableB: long
   actualWrittenB: Optional[long] = None
   overReservedB: Optional[long] = None
   totalProvisionB: Optional[long] = None
   snapshotSpace: Optional[VsanSnapshotSpace] = None


class VsanEntitySpaceUsage(DynamicData):
   entityId: Optional[str] = None
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []
   totalCapacityB: Optional[long] = None
   freeCapacityB: Optional[long] = None
   efficientCapacity: Optional[DataEfficiencyCapacityState] = None


class VsanFaultDomainSpec(DynamicData):
   hosts: list[HostSystem] = []
   name: str


class VsanFaultDomainsConfigSpec(DynamicData):
   faultDomains: list[VsanFaultDomainSpec] = []
   witness: Optional[VsanWitnessSpec] = None

class VsanHciMeshDitEncryptionIssue:
   pass


class VsanHealthActionBase(DynamicData):
   description: str


class VsanHealthActionSteps(VsanHealthActionBase):
   steps: list[VsanHealthActionBase] = []

class VsanHealthApiBasedAction(VsanHealthActionBase):
   apiAction: VsanClusterHealthAction

class VsanHealthCmdBasedAction(VsanHealthActionBase):
   commands: list[str] = []


class VsanHealthConfirmationDialog(DynamicData):
   title: str
   subTitle: Optional[str] = None
   content: str
   agreeLabel: Optional[str] = None
   closeLabel: Optional[str] = None
   isWarning: Optional[bool] = None


class VsanHealthCorrelation(DynamicData):
   primaryHealthTests: list[str] = []
   relatedHealthTests: list[str] = []
   skippedHealthTests: list[str] = []


class VsanHealthDataDrivenAction(VsanHealthActionBase):
   apiAction: VsanDataDrivenAPIAction
   confirmation: Optional[VsanHealthConfirmationDialog] = None


class VsanHealthExtMgmtPreCheckResult(DynamicData):
   overallResult: bool
   esxVersionCheckPassed: Optional[bool] = None
   drsCheckPassed: Optional[bool] = None
   eamConnectionCheckPassed: Optional[bool] = None
   installStateCheckPassed: Optional[bool] = None
   results: list[VsanClusterHealthTest] = []
   vumRegistered: Optional[bool] = None


class VsanHealthStatusCounts(DynamicData):
   error: int
   warning: int
   info: int


class VsanHealthTroubleshooting(DynamicData):
   diagnosticSteps: list[VsanHealthActionBase] = []
   remediations: list[VsanHealthActionBase] = []

class VsanHealthTxtBasedAction(VsanHealthActionBase):
   pass


class VsanHistoricalHealthQuerySpec(DynamicData):
   clusters: list[ClusterComputeResource] = []
   start: datetime
   end: Optional[datetime] = None
   testId: Optional[str] = None
   groupId: Optional[str] = None
   includeHealthRemediation: Optional[bool] = None


class VsanHistoricalHealthTest(DynamicData):
   timestamp: datetime
   health: str
   testDetails: list[VsanClusterHealthResultBase] = []
   testCorrelation: Optional[VsanHealthCorrelation] = None


class VsanHostClomdLivenessResult(DynamicData):
   hostname: str
   clomdStat: str
   error: Optional[MethodFault] = None


class VsanHostCreateVmHealthTestResult(DynamicData):
   hostname: str
   state: str
   fault: Optional[MethodFault] = None


class VsanHostDiskMapping(DynamicData):
   class VsanDiskGroupCreationType(Enum):
      allflash: ClassVar['VsanDiskGroupCreationType'] = 'allflash'
      hybrid: ClassVar['VsanDiskGroupCreationType'] = 'hybrid'
      vsandirect: ClassVar['VsanDiskGroupCreationType'] = 'vsandirect'
      pmem: ClassVar['VsanDiskGroupCreationType'] = 'pmem'
      VsanDiskGroupCreationType_Unknown: ClassVar['VsanDiskGroupCreationType'] = 'VsanDiskGroupCreationType_Unknown'

   host: HostSystem
   cacheDisks: list[ScsiDisk] = []
   capacityDisks: list[ScsiDisk] = []
   type: str


class VsanHostHealthSystemVersionResult(DynamicData):
   hostname: str
   version: Optional[str] = None
   error: Optional[MethodFault] = None
   build: Optional[str] = None


class VsanIoInsightInstance(DynamicData):
   runName: str
   state: Optional[str] = None
   startTime: Optional[datetime] = None
   endTime: Optional[datetime] = None
   hostsIoInsightInfo: list[VsanHostIoInsightInfo] = []
   hostUuids: list[str] = []
   vmUuids: list[str] = []


class VsanIoInsightInstanceQuerySpec(DynamicData):
   state: Optional[str] = None
   entityRefId: Optional[str] = None

class VsanIoInsightInstanceState:
   pass


class VsanIoInsightManager(ManagedObject):
   def StartIoInsight(self, cluster: Optional[ClusterComputeResource], runName: Optional[str], durationSec: Optional[long], targetHosts: list[HostSystem], targetVMs: list[VirtualMachine]) -> Task: ...
   def StopIoInsight(self, cluster: Optional[ClusterComputeResource], runName: Optional[str], hostsIoInsightInfos: list[VsanHostIoInsightInfo]) -> Task: ...
   def QueryIoInsightInstances(self, querySpec: VsanIoInsightInstanceQuerySpec, cluster: Optional[ClusterComputeResource]) -> list[VsanIoInsightInstance]: ...
   def DeleteIoInsightInstance(self, runName: str, cluster: Optional[ClusterComputeResource]) -> None: ...
   def RenameIoInsightInstance(self, oldRunName: str, newRunName: str, cluster: Optional[ClusterComputeResource]) -> None: ...


class VsanIscsiHomeObjectSpec(DynamicData):
   storagePolicy: Optional[ProfileSpec] = None
   defaultConfig: Optional[VsanIscsiTargetServiceDefaultConfigSpec] = None


class VsanIscsiInitiatorGroup(DynamicData):
   name: str
   initiators: list[str] = []
   targets: list[VsanIscsiTargetBasicInfo] = []


class VsanIscsiLUN(VsanIscsiLUNCommonInfo):
   targetAlias: str
   uuid: str
   actualSize: long
   objectInformation: Optional[VsanObjectInformation] = None


class VsanIscsiLUNCommonInfo(DynamicData):
   class VsanIscsiLUNStatus(Enum):
      Online: ClassVar['VsanIscsiLUNStatus'] = 'Online'
      Offline: ClassVar['VsanIscsiLUNStatus'] = 'Offline'
      VsanIscsiLUNStatus_Unknown: ClassVar['VsanIscsiLUNStatus'] = 'VsanIscsiLUNStatus_Unknown'

   lunId: Optional[int] = None
   alias: Optional[str] = None
   lunSize: long
   status: Optional[str] = None

class VsanIscsiLUNRuntimeStatusType:
   pass


class VsanIscsiLUNSpec(VsanIscsiLUNCommonInfo):
   storagePolicy: Optional[ProfileSpec] = None
   newLunId: Optional[int] = None


class VsanIscsiTarget(VsanIscsiTargetCommonInfo):
   lunCount: Optional[int] = None
   objectInformation: Optional[VsanObjectInformation] = None
   ioOwnerHost: Optional[str] = None
   initiators: list[str] = []
   initiatorGroups: list[str] = []


class VsanIscsiTargetAuthSpec(DynamicData):
   class VsanIscsiTargetAuthType(Enum):
      NoAuth: ClassVar['VsanIscsiTargetAuthType'] = 'NoAuth'
      CHAP: ClassVar['VsanIscsiTargetAuthType'] = 'CHAP'
      CHAP_Mutual: ClassVar['VsanIscsiTargetAuthType'] = 'CHAP_Mutual'
      VsanIscsiTargetAuthType_Unknown: ClassVar['VsanIscsiTargetAuthType'] = 'VsanIscsiTargetAuthType_Unknown'

   authType: Optional[str] = None
   userNameAttachToTarget: Optional[str] = None
   userSecretAttachToTarget: Optional[str] = None
   userNameAttachToInitiator: Optional[str] = None
   userSecretAttachToInitiator: Optional[str] = None


class VsanIscsiTargetBasicInfo(DynamicData):
   alias: str
   iqn: Optional[str] = None


class VsanIscsiTargetCommonInfo(VsanIscsiTargetBasicInfo):
   authSpec: Optional[VsanIscsiTargetAuthSpec] = None
   port: Optional[int] = None
   networkInterface: Optional[str] = None
   affinityLocation: Optional[str] = None


class VsanIscsiTargetServiceConfig(DynamicData):
   defaultConfig: Optional[VsanIscsiTargetServiceDefaultConfigSpec] = None
   enabled: Optional[bool] = None
   vipConfigs: list[VipConfigSpec] = []


class VsanIscsiTargetServiceDefaultConfigSpec(DynamicData):
   networkInterface: Optional[str] = None
   port: Optional[int] = None
   iscsiTargetAuthSpec: Optional[VsanIscsiTargetAuthSpec] = None

class VsanIscsiTargetServiceProcessStatus:
   pass


class VsanIscsiTargetServiceSpec(VsanIscsiTargetServiceConfig):
   homeObjectStoragePolicy: Optional[ProfileSpec] = None


class VsanIscsiTargetSpec(VsanIscsiTargetCommonInfo):
   storagePolicy: Optional[ProfileSpec] = None
   newAlias: Optional[str] = None


class VsanIscsiTargetSystem(ManagedObject):
   def QueryIscsiTargetServiceVersion(self) -> str: ...
   def GetHomeObject(self, cluster: ClusterComputeResource) -> VsanObjectInformation: ...
   def GetIscsiTargets(self, cluster: ClusterComputeResource) -> list[VsanIscsiTarget]: ...
   def GetIscsiTarget(self, cluster: ClusterComputeResource, targetAlias: str) -> Optional[VsanIscsiTarget]: ...
   def AddIscsiTarget(self, cluster: ClusterComputeResource, targetSpec: VsanIscsiTargetSpec) -> Optional[Task]: ...
   def EditIscsiTarget(self, cluster: ClusterComputeResource, targetSpec: VsanIscsiTargetSpec) -> Optional[Task]: ...
   def RemoveIscsiTarget(self, cluster: ClusterComputeResource, targetAlias: str) -> Optional[Task]: ...
   def GetIscsiLUNs(self, cluster: ClusterComputeResource, targetAliases: list[str]) -> list[VsanIscsiLUN]: ...
   def GetIscsiLUN(self, cluster: ClusterComputeResource, targetAlias: str, lunId: int) -> Optional[VsanIscsiLUN]: ...
   def AddIscsiLUN(self, cluster: ClusterComputeResource, targetAlias: str, lunSpec: VsanIscsiLUNSpec) -> Optional[Task]: ...
   def EditIscsiLUN(self, cluster: ClusterComputeResource, targetAlias: str, lunSpec: VsanIscsiLUNSpec) -> Optional[Task]: ...
   def RemoveIscsiLUN(self, cluster: ClusterComputeResource, targetAlias: str, lunId: int) -> Optional[Task]: ...
   def AddIscsiInitiatorsToTarget(self, cluster: ClusterComputeResource, targetAlias: str, initiatorNames: list[str]) -> None: ...
   def RemoveIscsiInitiatorsFromTarget(self, cluster: ClusterComputeResource, targetAlias: str, initiatorNames: list[str]) -> None: ...
   def GetIscsiInitiatorGroups(self, cluster: ClusterComputeResource) -> list[VsanIscsiInitiatorGroup]: ...
   def GetIscsiInitiatorGroup(self, cluster: ClusterComputeResource, initiatorGroupName: str) -> Optional[VsanIscsiInitiatorGroup]: ...
   def AddIscsiInitiatorGroup(self, cluster: ClusterComputeResource, initiatorGroupName: str) -> None: ...
   def RemoveIscsiInitiatorGroup(self, cluster: ClusterComputeResource, initiatorGroupName: str) -> None: ...
   def AddIscsiInitiatorsToGroup(self, cluster: ClusterComputeResource, initiatorGroupName: str, initiatorNames: list[str]) -> None: ...
   def RemoveIscsiInitiatorsFromGroup(self, cluster: ClusterComputeResource, initiatorGroupName: str, initiatorNames: list[str]) -> None: ...
   def AddIscsiTargetToGroup(self, cluster: ClusterComputeResource, initiatorGroupName: str, targetAlias: str) -> None: ...
   def RemoveIscsiTargetFromGroup(self, cluster: ClusterComputeResource, initiatorGroupName: str, targetAlias: str) -> None: ...
   def RemediateIscsiLunsRuntimeStatus(self, cluster: ClusterComputeResource) -> Task: ...


class VsanNetworkDiagnostics(DynamicData):
   host: HostSystem
   eventTypeId: str
   severity: str
   createdTime: datetime
   arguments: list[KeyAnyValue] = []


class VsanObjIdentityQuerySpec(DynamicData):
   knownSpbmProfileUuids: list[str] = []
   includeEffectiveCapacity: Optional[bool] = None


class VsanObjectExtAttrs(DynamicData):
   uuid: str
   objectType: Optional[str] = None
   objectPath: Optional[str] = None
   groupUuid: Optional[str] = None
   directoryName: Optional[str] = None


class VsanObjectExtraAttributes(DynamicData):
   uuid: str
   objPath: str
   objClass: int
   ufn: str
   isHbrCfg: bool
   ownerClusterUuid: Optional[str] = None


class VsanObjectIdentity(DynamicData):
   uuid: str
   type: str
   vmInstanceUuid: Optional[str] = None
   vmNsObjectUuid: Optional[str] = None
   vm: Optional[VirtualMachine] = None
   description: Optional[str] = None
   spbmProfileUuid: Optional[str] = None
   metadatas: list[KeyValue] = []
   typeExtId: Optional[str] = None
   spbmProfileName: Optional[str] = None


class VsanObjectIdentityAndHealth(DynamicData):
   identities: list[VsanObjectIdentity] = []
   health: Optional[VsanObjectOverallHealth] = None
   spaceSummary: list[VsanObjectSpaceSummary] = []
   rawData: Optional[str] = None


class VsanObjectInformation(DynamicData):
   directoryName: Optional[str] = None
   vsanObjectUuid: Optional[str] = None
   vsanHealth: Optional[str] = None
   policyAttributes: list[KeyValue] = []
   spbmProfileUuid: Optional[str] = None
   spbmProfileGenerationId: Optional[str] = None
   spbmComplianceResult: Optional[StorageComplianceResult] = None


class VsanObjectPlacement(DynamicData):
   details: list[VsanObjectPlacementDetails] = []


class VsanObjectPlacementDetails(DynamicData):
   uuid: str
   type: str
   name: Optional[str] = None
   isRemote: bool
   vm: Optional[VirtualMachine] = None
   spbmProfileUuid: Optional[str] = None
   spbmProfileName: Optional[str] = None
   isLocalPolicy: Optional[bool] = None
   remoteDatastoreUuid: Optional[str] = None
   remoteDatastoreName: Optional[str] = None
   remoteCluster: Optional[ClusterComputeResource] = None
   remoteClusterName: Optional[str] = None
   remoteVc: Optional[str] = None
   healthState: Optional[str] = None
   components: list[VsanComponentPlacement] = []


class VsanObjectQuerySpec(DynamicData):
   uuid: str
   spbmProfileGenerationId: Optional[str] = None


class VsanObjectSpaceSummary(DynamicData):
   class VsanObjectTypeEnum(Enum):
      vmswap: ClassVar['VsanObjectTypeEnum'] = 'vmswap'
      vdisk: ClassVar['VsanObjectTypeEnum'] = 'vdisk'
      namespace: ClassVar['VsanObjectTypeEnum'] = 'namespace'
      vmem: ClassVar['VsanObjectTypeEnum'] = 'vmem'
      statsdb: ClassVar['VsanObjectTypeEnum'] = 'statsdb'
      iscsiTarget: ClassVar['VsanObjectTypeEnum'] = 'iscsiTarget'
      iscsiLun: ClassVar['VsanObjectTypeEnum'] = 'iscsiLun'
      other: ClassVar['VsanObjectTypeEnum'] = 'other'
      fileSystemOverhead: ClassVar['VsanObjectTypeEnum'] = 'fileSystemOverhead'
      dedupOverhead: ClassVar['VsanObjectTypeEnum'] = 'dedupOverhead'
      spaceUnderDedupConsideration: ClassVar['VsanObjectTypeEnum'] = 'spaceUnderDedupConsideration'
      checksumOverhead: ClassVar['VsanObjectTypeEnum'] = 'checksumOverhead'
      improvedVirtualDisk: ClassVar['VsanObjectTypeEnum'] = 'improvedVirtualDisk'
      transientSpace: ClassVar['VsanObjectTypeEnum'] = 'transientSpace'
      slackSpaceCapRequiredForHost: ClassVar['VsanObjectTypeEnum'] = 'slackSpaceCapRequiredForHost'
      resynPauseThresholdForHost: ClassVar['VsanObjectTypeEnum'] = 'resynPauseThresholdForHost'
      minSpaceRequiredForVsanOp: ClassVar['VsanObjectTypeEnum'] = 'minSpaceRequiredForVsanOp'
      hostRebuildCapacity: ClassVar['VsanObjectTypeEnum'] = 'hostRebuildCapacity'
      physicalTransientSpace: ClassVar['VsanObjectTypeEnum'] = 'physicalTransientSpace'
      haMetadataObject: ClassVar['VsanObjectTypeEnum'] = 'haMetadataObject'
      fileServiceRoot: ClassVar['VsanObjectTypeEnum'] = 'fileServiceRoot'
      attachedCnsVolBlock: ClassVar['VsanObjectTypeEnum'] = 'attachedCnsVolBlock'
      detachedCnsVolBlock: ClassVar['VsanObjectTypeEnum'] = 'detachedCnsVolBlock'
      attachedCnsVolFile: ClassVar['VsanObjectTypeEnum'] = 'attachedCnsVolFile'
      detachedCnsVolFile: ClassVar['VsanObjectTypeEnum'] = 'detachedCnsVolFile'
      cnsVolFile: ClassVar['VsanObjectTypeEnum'] = 'cnsVolFile'
      fileShare: ClassVar['VsanObjectTypeEnum'] = 'fileShare'
      extension: ClassVar['VsanObjectTypeEnum'] = 'extension'
      hbrDisk: ClassVar['VsanObjectTypeEnum'] = 'hbrDisk'
      hbrCfg: ClassVar['VsanObjectTypeEnum'] = 'hbrCfg'
      hbrPersist: ClassVar['VsanObjectTypeEnum'] = 'hbrPersist'
      traceobject: ClassVar['VsanObjectTypeEnum'] = 'traceobject'
      esaObjectOverhead: ClassVar['VsanObjectTypeEnum'] = 'esaObjectOverhead'
      pgNamespace: ClassVar['VsanObjectTypeEnum'] = 'pgNamespace'
      clusterDBNamespace: ClassVar['VsanObjectTypeEnum'] = 'clusterDBNamespace'
      aggregatedSystemObjects: ClassVar['VsanObjectTypeEnum'] = 'aggregatedSystemObjects'
      nativeObjectStore: ClassVar['VsanObjectTypeEnum'] = 'nativeObjectStore'
      VsanObjectTypeEnum_Unknown: ClassVar['VsanObjectTypeEnum'] = 'VsanObjectTypeEnum_Unknown'

   class VsanObjectTypeEnum90(Enum):
      dedupSharedUserData: ClassVar['VsanObjectTypeEnum90'] = 'dedupSharedUserData'

   objType: Optional[str] = None
   overheadB: Optional[long] = None
   temporaryOverheadB: Optional[long] = None
   primaryCapacityB: Optional[long] = None
   provisionCapacityB: Optional[long] = None
   reservedCapacityB: Optional[long] = None
   overReservedB: Optional[long] = None
   physicalUsedB: Optional[long] = None
   usedB: Optional[long] = None
   objTypeExt: Optional[str] = None
   objTypeExtDesc: Optional[str] = None
   snapshotUsedB: Optional[long] = None


class VsanObjectSystem(ManagedObject):
   def SetVsanObjectPolicy(self, cluster: Optional[ComputeResource], vsanObjectUuid: str, profile: Optional[ProfileSpec]) -> bool: ...
   def QueryVsanObjectInformation(self, cluster: Optional[ComputeResource], vsanObjectQuerySpecs: list[VsanObjectQuerySpec]) -> list[VsanObjectInformation]: ...
   def QueryObjectIdentities(self, cluster: Optional[ComputeResource], objUuids: list[str], objTypes: list[str], includeHealth: Optional[bool], includeObjIdentity: Optional[bool], includeSpaceSummary: Optional[bool], extraQuerySpec: Optional[VsanObjIdentityQuerySpec]) -> Optional[VsanObjectIdentityAndHealth]: ...
   def DeleteObjects(self, cluster: Optional[ComputeResource], objUuids: list[str], force: Optional[bool]) -> Task: ...
   def QueryInaccessibleVmSwapObjects(self, cluster: Optional[ComputeResource]) -> list[str]: ...
   def QuerySyncingVsanObjectsSummary(self, cluster: ComputeResource, syncingObjectFilter: Optional[VsanSyncingObjectFilter]) -> VsanSyncingObjectQueryResult: ...
   def RelayoutObjects(self, cluster: ComputeResource) -> Task: ...
   def QueryPhysicalPlacements(self, cluster: ComputeResource, specs: Optional[VsanQueryPhysicalPlacementSpecs]) -> list[VsanObjectPlacement]: ...


class VsanPerfDiagnoseQuerySpec(DynamicData):
   startTime: datetime
   endTime: datetime
   queryType: str
   context: Optional[str] = None


class VsanPerfDiagnosticException(DynamicData):
   exceptionId: str
   exceptionMessage: str
   exceptionDetails: str
   exceptionUrl: str

class VsanPerfDiagnosticQueryType:
   pass


class VsanPerfDiagnosticResult(DynamicData):
   exceptionId: str
   recommendation: Optional[str] = None
   aggregationFunction: Optional[str] = None
   aggregationData: Optional[VsanPerfEntityMetricCSV] = None
   exceptionData: list[VsanPerfEntityMetricCSV] = []


class VsanPerfEntityMetricCSV(DynamicData):
   entityRefId: str
   sampleInfo: Optional[str] = None
   value: list[VsanPerfMetricSeriesCSV] = []


class VsanPerfEntityType(DynamicData):
   name: str
   id: str
   graphs: list[VsanPerfGraph] = []
   description: Optional[str] = None
   advancedGraphs: list[VsanPerfGraph] = []
   verboseGraphs: list[VsanPerfGraph] = []
   hotspotGraphs: list[VsanPerfGraph] = []


class VsanPerfGraph(DynamicData):
   class VsanPerfStatsUnitType(Enum):
      number: ClassVar['VsanPerfStatsUnitType'] = 'number'
      time_ms: ClassVar['VsanPerfStatsUnitType'] = 'time_ms'
      percentage: ClassVar['VsanPerfStatsUnitType'] = 'percentage'
      size_bytes: ClassVar['VsanPerfStatsUnitType'] = 'size_bytes'
      rate_bytes: ClassVar['VsanPerfStatsUnitType'] = 'rate_bytes'
      permille: ClassVar['VsanPerfStatsUnitType'] = 'permille'
      time_s: ClassVar['VsanPerfStatsUnitType'] = 'time_s'
      time_us: ClassVar['VsanPerfStatsUnitType'] = 'time_us'
      time_ns: ClassVar['VsanPerfStatsUnitType'] = 'time_ns'
      VsanPerfStatsUnitType_Unknown: ClassVar['VsanPerfStatsUnitType'] = 'VsanPerfStatsUnitType_Unknown'

   id: str
   metrics: list[VsanPerfMetricId] = []
   unit: str
   threshold: Optional[VsanPerfThreshold] = None
   name: Optional[str] = None
   description: Optional[str] = None
   secondGraph: Optional[VsanPerfGraph] = None


class VsanPerfHotspotEntitiesMetrics(DynamicData):
   entityRefId: str
   startTime: datetime
   endTime: datetime
   metricsValue: list[VsanPerfMetricSeriesCSV] = []


class VsanPerfHotspotEntityType(DynamicData):
   name: str
   id: str
   sortingMetrics: list[VsanPerfMetricId] = []
   originalEntityTypes: list[str] = []
   description: Optional[str] = None


class VsanPerfHotspotQuerySpec(DynamicData):
   startTime: datetime
   endTime: datetime
   entity: str
   metricId: str
   numEntities: Optional[int] = None


class VsanPerfMasterInformation(DynamicData):
   secSinceLastStatsWrite: Optional[long] = None
   secSinceLastStatsCollect: Optional[long] = None
   statsIntervalSec: long
   collectionFailureHostUuids: list[str] = []
   renamedStatsDirectories: list[str] = []
   statsDirectoryPercentFree: Optional[long] = None
   verboseMode: Optional[bool] = None
   verboseModeLastUpdate: Optional[datetime] = None


class VsanPerfMemberInfo(DynamicData):
   thumbprint: str
   thumbprintList: list[CertThumbprint] = []
   memberUuid: Optional[str] = None
   isSupportUnicast: Optional[bool] = None
   unicastAddressInfos: list[VsanUnicastAddressInfo] = []
   hostname: Optional[str] = None


class VsanPerfMetricId(DynamicData):
   class VsanPerfSummaryType(Enum):
      average: ClassVar['VsanPerfSummaryType'] = 'average'
      maximum: ClassVar['VsanPerfSummaryType'] = 'maximum'
      minimum: ClassVar['VsanPerfSummaryType'] = 'minimum'
      latest: ClassVar['VsanPerfSummaryType'] = 'latest'
      summation: ClassVar['VsanPerfSummaryType'] = 'summation'
      none: ClassVar['VsanPerfSummaryType'] = 'none'
      VsanPerfSummaryType_Unknown: ClassVar['VsanPerfSummaryType'] = 'VsanPerfSummaryType_Unknown'

   class VsanPerfStatsType(Enum):
      absolute: ClassVar['VsanPerfStatsType'] = 'absolute'
      delta: ClassVar['VsanPerfStatsType'] = 'delta'
      rate: ClassVar['VsanPerfStatsType'] = 'rate'
      VsanPerfStatsType_Unknown: ClassVar['VsanPerfStatsType'] = 'VsanPerfStatsType_Unknown'

   label: str
   group: Optional[str] = None
   rollupType: Optional[str] = None
   statsType: Optional[str] = None
   name: Optional[str] = None
   description: Optional[str] = None
   metricsCollectInterval: Optional[int] = None


class VsanPerfMetricSeriesCSV(DynamicData):
   metricId: VsanPerfMetricId
   threshold: Optional[VsanPerfThreshold] = None
   numExceptions: Optional[str] = None
   values: Optional[str] = None


class VsanPerfNodeInformation(DynamicData):
   version: str
   hostname: Optional[str] = None
   error: Optional[MethodFault] = None
   isCmmdsMaster: bool
   isStatsMaster: bool
   vsanMasterUuid: Optional[str] = None
   vsanNodeUuid: Optional[str] = None
   masterInfo: Optional[VsanPerfMasterInformation] = None
   diagnosticMode: Optional[bool] = None


class VsanPerfQuerySpec(DynamicData):
   entityRefId: str
   startTime: Optional[datetime] = None
   endTime: Optional[datetime] = None
   group: Optional[str] = None
   labels: list[str] = []
   interval: Optional[int] = None


class VsanPerfThreshold(DynamicData):
   class VsanPerfThresholdDirectionType(Enum):
      upper: ClassVar['VsanPerfThresholdDirectionType'] = 'upper'
      lower: ClassVar['VsanPerfThresholdDirectionType'] = 'lower'
      VsanPerfThresholdDirectionType_Unknown: ClassVar['VsanPerfThresholdDirectionType'] = 'VsanPerfThresholdDirectionType_Unknown'

   direction: str
   yellow: Optional[str] = None
   red: Optional[str] = None


class VsanPerfTimeRange(DynamicData):
   name: str
   startTime: datetime
   endTime: datetime


class VsanPerfTimeRangeQuerySpec(DynamicData):
   name: Optional[str] = None
   startTimeFrom: Optional[datetime] = None
   startTimeTo: Optional[datetime] = None
   endTimeFrom: Optional[datetime] = None
   endTimeTo: Optional[datetime] = None


class VsanPerfTopEntities(DynamicData):
   metricId: VsanPerfMetricId
   entities: list[VsanPerfTopEntity] = []


class VsanPerfTopEntity(DynamicData):
   entityRefId: str
   value: str


class VsanPerfTopQuerySpec(DynamicData):
   timeStamp: datetime
   entity: str
   metricId: str
   numEntities: Optional[int] = None


class VsanPerformanceManager(ManagedObject):
   def QueryVsanPerfTopEntities(self, cluster: Optional[ClusterComputeResource], querySpec: VsanPerfTopQuerySpec) -> list[VsanPerfEntityMetricCSV]: ...
   def QueryVsanPerfHotspotEntities(self, cluster: Optional[ClusterComputeResource], querySpec: VsanPerfHotspotQuerySpec) -> list[VsanPerfHotspotEntitiesMetrics]: ...
   def VsanPerfDiagnose(self, perfDiagnoseQuery: VsanPerfDiagnoseQuerySpec, cluster: Optional[ComputeResource]) -> list[VsanPerfDiagnosticResult]: ...
   def VsanPerfDiagnoseTask(self, perfDiagnoseQuery: VsanPerfDiagnoseQuerySpec, cluster: Optional[ComputeResource]) -> Task: ...
   def GetVsanPerfDiagnosisResult(self, task: Task, cluster: Optional[ComputeResource]) -> list[VsanPerfDiagnosticResult]: ...
   def QueryVsanPerf(self, querySpecs: list[VsanPerfQuerySpec], cluster: Optional[ComputeResource]) -> list[VsanPerfEntityMetricCSV]: ...
   def QueryNodeInformation(self, cluster: Optional[ComputeResource]) -> list[VsanPerfNodeInformation]: ...
   def CreateStatsObject(self, cluster: Optional[ComputeResource], profile: Optional[ProfileSpec]) -> str: ...
   def CreateStatsObjectTask(self, cluster: Optional[ComputeResource], profile: Optional[ProfileSpec]) -> Task: ...
   def DeleteStatsObject(self, cluster: Optional[ComputeResource]) -> bool: ...
   def DeleteStatsObjectTask(self, cluster: Optional[ComputeResource]) -> Task: ...
   def SetStatsObjectPolicy(self, cluster: Optional[ComputeResource], profile: Optional[ProfileSpec]) -> bool: ...
   def QueryStatsObjectInformation(self, cluster: Optional[ComputeResource]) -> VsanObjectInformation: ...
   def QueryClusterHealth(self, cluster: ClusterComputeResource) -> list[VsanClusterHealthGroup]: ...
   def QueryTimeRanges(self, cluster: Optional[ClusterComputeResource], querySpec: VsanPerfTimeRangeQuerySpec) -> list[VsanPerfTimeRange]: ...
   def SaveTimeRanges(self, cluster: Optional[ClusterComputeResource], timeRanges: list[VsanPerfTimeRange]) -> None: ...
   def DeleteTimeRange(self, cluster: Optional[ClusterComputeResource], name: str) -> None: ...
   def ToggleVerboseMode(self, cluster: Optional[ClusterComputeResource], verboseMode: bool) -> None: ...
   def GetSupportedEntityTypes(self, cluster: Optional[ComputeResource]) -> list[VsanPerfEntityType]: ...
   def GetSupportedHotspotEntityTypes(self, cluster: Optional[ComputeResource]) -> list[VsanPerfHotspotEntityType]: ...
   def GetSupportedDiagnosticExceptions(self) -> list[VsanPerfDiagnosticException]: ...
   def GetAggregatedEntityTypes(self) -> list[VsanPerfEntityType]: ...
   def QueryRemoteServerClusters(self, cluster: Optional[ClusterComputeResource], querySpec: Optional[VsanRemoteClusterQuerySpec]) -> list[str]: ...


class VsanPerfsvcConfig(DynamicData):
   enabled: bool
   profile: Optional[ProfileSpec] = None
   diagnosticMode: Optional[bool] = None
   verboseMode: Optional[bool] = None


class VsanQueryPhysicalPlacementSpecs(DynamicData):
   vms: list[VirtualMachine] = []

class VsanRelayoutObjectsErrorCode:
   pass


class VsanRemoteClusterQuerySpec(DynamicData):
   startTime: Optional[datetime] = None
   endTime: Optional[datetime] = None


class VsanRemoteDatastoreSystem(ManagedObject):
   def MountPrecheck(self, cluster: ClusterComputeResource, datastore: Datastore, serverClusterInfo: Optional[VcRemoteVsanServerClusterInfo]) -> MountPrecheckResult: ...
   def RemoteVcMountPrecheck(self, cluster: ClusterComputeResource, xvcDatastore: XVCDatastoreInfo, serverClusterInfo: Optional[VcRemoteVsanServerClusterInfo]) -> MountPrecheckResult: ...
   def QueryDatastoreSource(self, vcHosts: list[str]) -> list[HciMeshDatastoreSource]: ...
   def PrecheckDatastoreSource(self, datastoreSource: HciMeshDatastoreSource, operation: Optional[str]) -> DatastoreSourcePrecheckResult: ...
   def CreateDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def UpdateDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def DestroyDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def QueryHciMeshDatastores(self, querySpecs: list[XvcQuerySpec], extraVcInfos: list[RemoteVcInfo]) -> list[XvcQueryResultSet]: ...


class VsanSnapshotSpace(DynamicData):
   snapshotCount: Optional[int] = None
   actualSnapshotUsedB: Optional[long] = None
   fullyInflatedSnapshotUsedB: Optional[long] = None


class VsanSpaceQuerySpec(DynamicData):
   entityType: str
   entityIds: list[str] = []


class VsanSpaceReportSystem(ManagedObject):
   def QuerySpaceUsage(self, cluster: ComputeResource, storagePolicies: list[ProfileSpec], whatifCapacityOnly: Optional[bool]) -> VsanSpaceUsage: ...
   def QueryVsanManagedStorageSpaceUsage(self, cluster: ComputeResource, querySpec: QueryVsanManagedStorageSpaceUsageSpec) -> list[VsanSpaceUsageWithDatastoreType]: ...
   def QueryEntitySpaceUsage(self, cluster: ComputeResource, querySpec: VsanSpaceQuerySpec) -> list[VsanEntitySpaceUsage]: ...

class VsanSpaceReportingEntityType:
   pass


class VsanSpaceUsage(DynamicData):
   totalCapacityB: long
   freeCapacityB: Optional[long] = None
   spaceOverview: Optional[VsanObjectSpaceSummary] = None
   spaceDetail: Optional[VsanSpaceUsageDetailResult] = None
   efficientCapacity: Optional[DataEfficiencyCapacityState] = None
   whatifCapacities: list[VsanWhatifCapacity] = []
   uncommittedB: Optional[long] = None
   capacityHealthThreshold: Optional[VsanHealthThreshold] = None
   spaceEfficiencyRatio: Optional[VsanSpaceEfficiencyRatio] = None
   effectiveSpaceUsage: Optional[VsanEffectiveSpaceUsage] = None


class VsanSpaceUsageDetailResult(DynamicData):
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []


class VsanSpaceUsageWithDatastoreType(DynamicData):
   spaceUsage: Optional[VsanSpaceUsage] = None
   datastoreType: Optional[str] = None


class VsanStorageWorkloadType(DynamicData):
   specs: list[VsanVmdkLoadTestSpec] = []
   typeId: str
   name: str
   description: str
   duration: Optional[long] = None


class VsanStretchedClusterConfig(DynamicData):
   cluster: ClusterComputeResource
   preferredFdName: Optional[str] = None
   faultDomainConfig: Optional[VSANStretchedClusterFaultDomainConfig] = None


class VsanSyncingObjectFilter(DynamicData):
   resyncType: Optional[str] = None
   resyncStatus: Optional[str] = None
   numberOfObjects: Optional[long] = None
   offset: Optional[long] = None
   includeDedupObject: Optional[bool] = None


class VsanUnicastAddressInfo(DynamicData):
   address: str
   port: Optional[int] = None
   nicType: Optional[str] = None


class VsanUpgradeStatusEx(VsanUpgradeSystem.UpgradeStatus):
   isPrecheck: Optional[bool] = None
   precheckResult: Optional[VsanDiskFormatConversionCheckResult] = None


class VsanUpgradeSystemUpgradeHistoryStoragePoolOp(VsanUpgradeSystem.UpgradeHistoryItem):
   operation: str
   diskInfo: StoragePoolDiskInfo


class VsanVcClusterConfigSystem(ManagedObject):
   def ReconfigureEx(self, cluster: ClusterComputeResource, vsanReconfigSpec: ReconfigSpec) -> Task: ...
   def GetConfigInfoEx(self, cluster: ClusterComputeResource) -> ConfigInfoEx: ...
   def RekeyEncryptedCluster(self, encryptedCluster: ClusterComputeResource, deepRekey: Optional[bool], allowReducedRedundancy: Optional[bool]) -> Task: ...
   def GetRuntimeStats(self, cluster: ClusterComputeResource, stats: list[str]) -> list[RuntimeStatsHostMap]: ...
   def QueryClusterDrsStats(self, cluster: ClusterComputeResource, vms: list[VirtualMachine]) -> list[DrsStats]: ...
   def ValidateConfigSpec(self, cluster: ClusterComputeResource, vsanReconfigSpec: ReconfigSpec) -> list[ClusterComputeResource.ValidationResultBase]: ...
   def RunLifecycleCheck(self, cluster: ClusterComputeResource, vsanLifecycleCheckSpec: VsanVcLifecycleCheckSpec) -> VsanVcLifecycleCheckResult: ...
   def GetClaimedCapacity(self, cluster: ClusterComputeResource) -> long: ...
   def GetConfigurationLimits(self) -> list[KeyAnyValue]: ...
   def GetClusterAutoRAIDInfo(self, cluster: ClusterComputeResource) -> Optional[AutoRAIDInfo]: ...


class VsanVcClusterHealthSystem(ManagedObject):
   class VsanHealthLogLevelEnum(Enum):
      INFO: ClassVar['VsanHealthLogLevelEnum'] = 'INFO'
      WARNING: ClassVar['VsanHealthLogLevelEnum'] = 'WARNING'
      ERROR: ClassVar['VsanHealthLogLevelEnum'] = 'ERROR'
      DEBUG: ClassVar['VsanHealthLogLevelEnum'] = 'DEBUG'
      CRITICAL: ClassVar['VsanHealthLogLevelEnum'] = 'CRITICAL'
      VsanHealthLogLevelEnum_Unknown: ClassVar['VsanHealthLogLevelEnum'] = 'VsanHealthLogLevelEnum_Unknown'

   def QueryVerifyClusterHealthSystemVersions(self, cluster: ClusterComputeResource) -> VsanClusterHealthSystemVersionResult: ...
   def QueryFileServiceHealthSummary(self, cluster: ClusterComputeResource, includeFileServerHealth: Optional[bool], includeFileShareHealth: Optional[bool]) -> Optional[VsanClusterFileServiceHealthSummary]: ...
   def QueryClusterCreateVmHealthTest(self, cluster: ClusterComputeResource, timeout: int, datastore: Optional[Datastore]) -> VsanClusterCreateVmHealthTestResult: ...
   def QueryClusterHealthSummary(self, cluster: Optional[ClusterComputeResource], vmCreateTimeout: Optional[int], objUuids: list[str], includeObjUuids: Optional[bool], fields: list[str], fetchFromCache: Optional[bool], perspective: Optional[str], hosts: list[HostSystem], spec: Optional[VsanClusterHealthQuerySpec]) -> VsanClusterHealthSummary: ...
   def QueryClusterHealthSummaryTask(self, cluster: ClusterComputeResource, hosts: list[HostSystem], includeDataProtectionHealth: Optional[bool], includeOnlineHealth: Optional[bool]) -> Task: ...
   def QueryVsanObjExtAttrs(self, cluster: ClusterComputeResource, uuids: list[str]) -> list[VsanObjectExtAttrs]: ...
   def QueryAllSupportedHealthChecks(self) -> list[VsanClusterHealthCheckInfo]: ...
   def QueryClusterNetworkPerfTest(self, cluster: ClusterComputeResource, multicast: bool, durationSec: Optional[int]) -> VsanClusterNetworkLoadTestResult: ...
   def QueryClusterNetworkPerfTask(self, cluster: ClusterComputeResource, spec: Optional[VsanClusterNetworkPerfTaskSpec]) -> Task: ...
   def RunVmdkLoadTest(self, cluster: ClusterComputeResource, runname: str, durationSec: Optional[int], specs: list[VsanVmdkLoadTestSpec], action: Optional[str]) -> Task: ...
   def QueryVsanClusterHealthConfig(self, cluster: ClusterComputeResource) -> VsanClusterHealthConfigs: ...
   def QueryVsanClusterHealthCheckInterval(self, cluster: ClusterComputeResource) -> int: ...
   def SetVsanClusterHealthCheckInterval(self, cluster: ClusterComputeResource, vsanClusterHealthCheckInterval: int) -> None: ...
   def GetVsanClusterSilentChecks(self, cluster: ClusterComputeResource) -> list[str]: ...
   def SetVsanClusterSilentChecks(self, cluster: ClusterComputeResource, addSilentChecks: list[str], removeSilentChecks: list[str]) -> bool: ...
   def SetVsanClusterTelemetryConfig(self, cluster: ClusterComputeResource, vsanClusterHealthConfig: VsanClusterHealthConfigs) -> None: ...
   def TestVsanClusterTelemetryProxy(self, proxyConfig: VsanClusterTelemetryProxyConfig) -> bool: ...
   def SendVsanTelemetry(self, cluster: ClusterComputeResource) -> None: ...
   def RepairClusterObjectsImmediate(self, cluster: ClusterComputeResource, uuids: list[str]) -> Task: ...
   def UpdateDefaultDSPolicyRecommendation(self, cluster: ClusterComputeResource) -> Task: ...
   def QueryClusterCreateVmHealthHistoryTest(self, cluster: ClusterComputeResource, count: Optional[int], datastore: Optional[Datastore]) -> list[VsanClusterCreateVmHealthTestResult]: ...
   def QueryClusterNetworkPerfHistoryTest(self, cluster: ClusterComputeResource, count: Optional[int], spec: Optional[VsanClusterNetworkPerfTaskSpec]) -> list[VsanClusterNetworkLoadTestResult]: ...
   def QueryClusterVmdkLoadHistoryTest(self, cluster: ClusterComputeResource, count: Optional[int], taskId: Optional[str]) -> list[VsanClusterVmdkLoadTestResult]: ...
   def QueryClusterVmdkWorkloadTypes(self) -> list[VsanStorageWorkloadType]: ...
   def QueryAttachToSrHistory(self, cluster: ClusterComputeResource, count: Optional[int], taskId: Optional[str]) -> list[VsanAttachToSrOperation]: ...
   def AttachVsanSupportBundleToSr(self, cluster: ClusterComputeResource, srNumber: str) -> Task: ...
   def GetClusterHclInfo(self, cluster: Optional[ClusterComputeResource], includeHostsResult: Optional[bool], includeVendorInfo: Optional[bool], esxRelease: Optional[str], querySpec: Optional[VsanHclQuerySpec]) -> VsanClusterHclInfo: ...
   def GetHclInfoForVsanEligibleDisks(self, querySpec: VsanHclQuerySpec) -> VsanClusterHclInfo: ...
   def DownloadHclFile(self, sha1sums: list[str]) -> Task: ...
   def GetClusterHclConstraints(self, cluster: ClusterComputeResource, release: str) -> VsanHclReleaseConstraint: ...
   def GetDiskHclConstraints(self, release: Optional[str], diskModels: list[VsanDiskModelInfo]) -> list[VsanHclDiskConstraint]: ...
   def GetClusterReleaseRecommendation(self, cluster: ClusterComputeResource, minor: list[str], major: list[str]) -> list[VsanHclReleaseConstraint]: ...
   def PurgeHclFiles(self, sha1sums: list[str]) -> None: ...
   def DownloadAndInstallVendorTool(self, cluster: ClusterComputeResource) -> Task: ...
   def UploadHclDb(self, db: str) -> bool: ...
   def UpdateHclDbFromWeb(self, url: Optional[str]) -> bool: ...
   def RebalanceCluster(self, cluster: ClusterComputeResource, targetHosts: list[HostSystem]) -> Task: ...
   def StopRebalanceCluster(self, cluster: ClusterComputeResource, targetHosts: list[HostSystem]) -> Task: ...
   def IsRebalanceRunning(self, cluster: ClusterComputeResource, targetHosts: list[HostSystem]) -> bool: ...
   def SetLogLevel(self, level: Optional[str]) -> None: ...
   def QuerySmartStatsSummary(self, cluster: ClusterComputeResource) -> list[VsanSmartStatsHostSummary]: ...
   def QueryVsanProxyConfig(self) -> VsanClusterTelemetryProxyConfig: ...
   def QueryClusterHistoricalHealth(self, spec: VsanHistoricalHealthQuerySpec) -> list[VsanClusterHealthSummary]: ...
   def SetVsanVcgMappingForHwDevices(self, spec: VsanHwToVcgInfoMappingSpec) -> bool: ...


class VsanVcDiskManagementSystem(ManagedObject):
   def RetrieveAllFlashCapabilities(self, cluster: ClusterComputeResource) -> list[VsanHostCapability]: ...
   def InitializeDiskMappings(self, spec: DiskMappingCreationSpec) -> Task: ...
   def QueryDiskMappings(self, host: HostSystem) -> list[DiskMapInfoEx]: ...
   def QueryVsanManagedDisks(self, host: HostSystem, filterSpec: Optional[QueryVsanDisksSpec]) -> Optional[VsanManagedDisksInfo]: ...
   def QueryClusterDataEfficiencyCapacityState(self, cluster: ClusterComputeResource) -> DataEfficiencyCapacityState: ...
   def RebuildDiskMapping(self, host: HostSystem, mapping: DiskMapping, maintenanceSpec: MaintenanceSpec) -> Task: ...
   def UnmountDiskMappingEx(self, cluster: ClusterComputeResource, mappings: list[DiskMapping], maintenanceSpec: MaintenanceSpec) -> Task: ...
   def RemoveDiskMappingEx(self, cluster: ClusterComputeResource, mappings: list[DiskMapping], maintenanceSpec: MaintenanceSpec) -> Task: ...
   def RemoveDiskEx(self, cluster: ClusterComputeResource, disks: list[ScsiDisk], maintenanceSpec: MaintenanceSpec) -> Task: ...
   def AddStoragePoolDisks(self, specs: list[AddStoragePoolDiskSpec]) -> Task: ...
   def DeleteStoragePoolDisk(self, cluster: ClusterComputeResource, spec: DeleteStoragePoolDiskSpec) -> Task: ...
   def UnmountStoragePoolDisks(self, cluster: ClusterComputeResource, spec: DeleteStoragePoolDiskSpec) -> Task: ...


class VsanVcKmipServersHealth(DynamicData):
   health: Optional[str] = None
   error: Optional[MethodFault] = None
   kmsProviderId: Optional[str] = None
   kmsHealth: list[VsanKmsHealth] = []
   clientCertHealth: Optional[str] = None
   clientCertExpireDate: Optional[datetime] = None
   isAwsKms: Optional[bool] = None
   cmkHealth: Optional[str] = None
   kekExpireHealth: Optional[str] = None
   kekExpireDate: Optional[datetime] = None
   hostKeyExpireHealth: Optional[str] = None
   hostKeyExpireDate: Optional[datetime] = None


class VsanVcLifecycleCheckResult(DynamicData):
   status: str
   preCheckResults: list[LifecyclePreCheckResult] = []
   configDetails: LifecycleConfigDetails


class VsanVcLifecycleCheckSpec(DynamicData):
   operation: str


class VsanVcStretchedClusterSystem(ManagedObject):
   def AddWitnessHost(self, cluster: ClusterComputeResource, witnessHost: HostSystem, preferredFd: str, diskMapping: Optional[DiskMapping], metadataMode: Optional[bool], storagePoolSpec: Optional[AddStoragePoolDiskSpec]) -> Task: ...
   def RemoveWitnessHost(self, cluster: ClusterComputeResource, witnessHost: Optional[HostSystem], witnessAddress: Optional[str]) -> Task: ...
   def ConvertToStretchedCluster(self, cluster: ClusterComputeResource, faultDomainConfig: VSANStretchedClusterFaultDomainConfig, witnessHost: HostSystem, preferredFd: str, diskMapping: Optional[DiskMapping], storagePoolSpec: Optional[AddStoragePoolDiskSpec]) -> Task: ...
   def SetPreferredFaultDomain(self, cluster: ClusterComputeResource, preferredFd: str, witnessHost: Optional[HostSystem]) -> Task: ...
   def GetPreferredFaultDomain(self, cluster: ClusterComputeResource) -> Optional[VSANPreferredFaultDomainInfo]: ...
   def IsWitnessHost(self, host: HostSystem) -> bool: ...
   def GetWitnessHosts(self, cluster: ClusterComputeResource) -> list[VSANWitnessHostInfo]: ...
   def RetrieveStretchedClusterVcCapability(self, cluster: ClusterComputeResource, verifyAllConnected: Optional[bool]) -> list[VSANStretchedClusterCapability]: ...
   def IsWitnessVirtualAppliance(self, hosts: list[HostSystem]) -> list[VsanHostVirtualApplianceInfo]: ...
   def QuerySharedWitnessCompatibility(self, sharedWitnessHost: HostSystem, roboClusters: list[ClusterComputeResource]) -> SharedWitnessCompatibilityResult: ...
   def QueryWitnessHostClusterInfo(self, witnessHost: HostSystem, skipComponentsCount: Optional[bool]) -> list[ClusterRuntimeInfo]: ...
   def ReplaceWitnessHostForClusters(self, configSpec: VsanVcStretchedClusterConfigSpec) -> Task: ...
   def AddWitnessHostForClusters(self, configSpec: VsanVcStretchedClusterConfigSpec) -> Task: ...


class VsanVsanClusterPcapGroup(DynamicData):
   master: str
   members: list[str] = []


class VsanVsanClusterPcapResult(DynamicData):
   pkts: list[str] = []
   groups: list[VsanVsanClusterPcapGroup] = []
   issues: list[str] = []
   hostResults: list[VsanVsanPcapResult] = []


class VsanVumSystem(ManagedObject):
   def GetVsanVumConfig(self) -> VsanVumSystemConfig: ...
   def FetchIsoDepotCookie(self, username: str, password: str) -> None: ...
   def UpdateHostFirmware(self, host: HostSystem) -> Task: ...
   def UploadReleaseDb(self, db: str) -> None: ...


class VsanVumSystemConfig(DynamicData):
   enabled: Optional[bool] = None
   autoCheckInterval: Optional[int] = None
   metadataUpdateInterval: Optional[int] = None
   releaseDbLastUpdate: Optional[datetime] = None


class VsanWhatifCapacity(DynamicData):
   totalWhatifCapacityB: long
   freeWhatifCapacityB: long
   storagePolicy: ProfileSpec
   isSatisfiable: bool


class VsanWitnessSpec(DynamicData):
   host: HostSystem
   preferredFaultDomainName: str
   diskMapping: Optional[DiskMapping] = None
   storagePoolSpec: Optional[AddStoragePoolDiskSpec] = None
