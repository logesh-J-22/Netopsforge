# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import action as action
from . import alarm as alarm
from . import cluster as cluster
from . import cns as cns
from . import dvs as dvs
from . import encryption as encryption
from . import event as event
from . import ext as ext
from . import fault as fault
from . import host as host
from . import net as net
from . import option as option
from . import profile as profile
from . import scheduler as scheduler
from . import storageDrs as storageDrs
from . import tenant as tenant
from . import vApp as vApp
from . import vcha as vcha
from . import view as view
from . import vm as vm
from . import vsan as vsan
from . import vslm as vslm

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedMethod

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import byte
from pyVmomi.VmomiSupport import double
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vmodl import DynamicData

from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.alarm import Alarm

from pyVmomi.vim.alarm import AlarmManager

from pyVmomi.vim.alarm import AlarmState

from pyVmomi.vim.cluster import ActionHistory
from pyVmomi.vim.cluster import ConfigInfo
from pyVmomi.vim.cluster import ConfigSpec
from pyVmomi.vim.cluster import ConfigSpecEx
from pyVmomi.vim.cluster import DasAdmissionControlInfo
from pyVmomi.vim.cluster import DasAdvancedRuntimeInfo
from pyVmomi.vim.cluster import DasData
from pyVmomi.vim.cluster import DrsFaults
from pyVmomi.vim.cluster import DrsMigration
from pyVmomi.vim.cluster import DrsRecommendation
from pyVmomi.vim.cluster import EVCManager
from pyVmomi.vim.cluster import EnterMaintenanceResult
from pyVmomi.vim.cluster import HostRecommendation
from pyVmomi.vim.cluster import PlacementResult
from pyVmomi.vim.cluster import PlacementSpec
from pyVmomi.vim.cluster import Recommendation
from pyVmomi.vim.cluster import ResourceUsageSummary
from pyVmomi.vim.cluster import RuleInfo
from pyVmomi.vim.cluster import UsageSummary

from pyVmomi.vim.cluster import VsanDiskFormatConversionCheckResult
from pyVmomi.vim.cluster import VsanDiskFormatConversionSpec
from pyVmomi.vim.cluster import VsanUpgradeStatusEx

from pyVmomi.vim.dvs import DistributedVirtualPort

from pyVmomi.vim.dvs import DistributedVirtualPortgroup

from pyVmomi.vim.dvs import DistributedVirtualSwitchManager
from pyVmomi.vim.dvs import EntityBackup
from pyVmomi.vim.dvs import HostMember
from pyVmomi.vim.dvs import HostProductSpec
from pyVmomi.vim.dvs import KeyedOpaqueBlob
from pyVmomi.vim.dvs import NetworkResourcePool
from pyVmomi.vim.dvs import PortCriteria
from pyVmomi.vim.dvs import ProductSpec
from pyVmomi.vim.dvs import VmVnicNetworkResourcePool

from pyVmomi.vim.encryption import CryptoKeyId
from pyVmomi.vim.encryption import CryptoKeyPlain

from pyVmomi.vim.encryption import CryptoManager

from pyVmomi.vim.encryption import CryptoSpec
from pyVmomi.vim.encryption import KeyProviderId

from pyVmomi.vim.event import Event

from pyVmomi.vim.event import EventManager

from pyVmomi.vim.ext import ExtendedProductInfo
from pyVmomi.vim.ext import ManagedEntityInfo
from pyVmomi.vim.ext import SolutionManagerInfo

from pyVmomi.vim.host import Capability
from pyVmomi.vim.host import ConfigInfo
from pyVmomi.vim.host import ConfigManager

from pyVmomi.vim.host import ConnectInfo

from pyVmomi.vim.host import ConnectSpec

from pyVmomi.vim.host import CpuIdInfo

from pyVmomi.vim.host import DatastoreBrowser
from pyVmomi.vim.host import DateTimeConfig

from pyVmomi.vim.host import DiskDimensions
from pyVmomi.vim.host import FeatureCapability
from pyVmomi.vim.host import FeatureMask
from pyVmomi.vim.host import FlagInfo
from pyVmomi.vim.host import HardwareInfo
from pyVmomi.vim.host import HostAccessManager
from pyVmomi.vim.host import IpmiInfo

from pyVmomi.vim.host import LocalAccountManager
from pyVmomi.vim.host import MaintenanceSpec
from pyVmomi.vim.host import MountInfo
from pyVmomi.vim.host import RuntimeInfo
from pyVmomi.vim.host import SnmpSystem
from pyVmomi.vim.host import Summary
from pyVmomi.vim.host import SystemResourceInfo
from pyVmomi.vim.host import SystemSwapConfiguration
from pyVmomi.vim.host import TpmAttestationReport
from pyVmomi.vim.host import VirtualNic
from pyVmomi.vim.option import ArrayUpdateSpec

from pyVmomi.vim.option import BoolOption

from pyVmomi.vim.option import IntOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.option import OptionManager

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.profile import ComplianceManager

from pyVmomi.vim.profile import ComplianceResult

from pyVmomi.vim.scheduler import ScheduledTask

from pyVmomi.vim.scheduler import ScheduledTaskManager

from pyVmomi.vim.storageDrs import ConfigInfo
from pyVmomi.vim.storageDrs import ConfigSpec

from pyVmomi.vim.storageDrs import StoragePlacementResult
from pyVmomi.vim.storageDrs import StoragePlacementSpec

from pyVmomi.vim.tenant import TenantManager

from pyVmomi.vim.vApp import CloneSpec

from pyVmomi.vim.vApp import EntityConfigInfo

from pyVmomi.vim.vApp import IpPool

from pyVmomi.vim.vApp import ProductInfo
from pyVmomi.vim.vApp import PropertyInfo
from pyVmomi.vim.vApp import VAppConfigInfo

from pyVmomi.vim.vApp import VAppConfigSpec

from pyVmomi.vim.vcha import FailoverClusterConfigurator
from pyVmomi.vim.vcha import FailoverClusterManager

from pyVmomi.vim.view import ViewManager

from pyVmomi.vim.vm import Capability

from pyVmomi.vim.vm import CertThumbprint
from pyVmomi.vim.vm import CloneSpec

from pyVmomi.vim.vm import ConfigInfo

from pyVmomi.vim.vm import ConfigOption

from pyVmomi.vim.vm import ConfigOptionDescriptor

from pyVmomi.vim.vm import ConfigSpec
from pyVmomi.vim.vm import ConfigTarget
from pyVmomi.vim.vm import FaultToleranceConfigSpec

from pyVmomi.vim.vm import FeatureRequirement
from pyVmomi.vim.vm import FileLayout
from pyVmomi.vim.vm import FileLayoutEx

from pyVmomi.vim.vm import GuestCustomizationManager
from pyVmomi.vim.vm import GuestInfo
from pyVmomi.vim.vm import GuestQuiesceSpec
from pyVmomi.vim.vm import InstantCloneSpec

from pyVmomi.vim.vm import ProfileSpec
from pyVmomi.vim.vm import RelocateSpec
from pyVmomi.vim.vm import RuntimeInfo

from pyVmomi.vim.vm import Snapshot
from pyVmomi.vim.vm import SnapshotInfo
from pyVmomi.vim.vm import SnapshotSelectionSpec
from pyVmomi.vim.vm import StorageInfo
from pyVmomi.vim.vm import Summary
from pyVmomi.vim.vm import UsbScanCodeSpec

from pyVmomi.vim.vsan import VsanCloudHealthStatus

from pyVmomi.vim.vslm import ID

from pyVmomi.vim.vslm import VStorageObjectManagerBase

from pyVmomi.vmodl.query import PropertyCollector

from pyVmomi.vim.profile.cluster import ProfileManager

from pyVmomi.vim.profile.host import AnswerFileStatusResult

from pyVmomi.vim.profile.host import HostSpecificationManager
from pyVmomi.vim.profile.host import ProfileManager

from pyVmomi.vim.vm.check import CompatibilityChecker
from pyVmomi.vim.vm.check import ProvisioningChecker

from pyVmomi.vim.vm.customization import Specification

from pyVmomi.vim.vm.device import VirtualDisk

from pyVmomi.vim.vm.device import VirtualDiskId

from pyVmomi.vim.vm.device import VirtualPCIPassthrough

from pyVmomi.vim.vm.guest import GuestOperationsManager

from pyVmomi.vim.vsan.host import DiskMapping



class AboutInfo(DynamicData):
   name: str
   fullName: str
   vendor: str
   version: str
   patchLevel: Optional[str] = None
   build: str
   localeVersion: Optional[str] = None
   localeBuild: Optional[str] = None
   osType: str
   productLineId: str
   apiType: str
   apiVersion: str
   instanceUuid: Optional[str] = None
   licenseProductName: Optional[str] = None
   licenseProductVersion: Optional[str] = None


class AuthorizationDescription(DynamicData):
   privilege: list[ElementDescription] = []
   privilegeGroup: list[ElementDescription] = []


class AuthorizationManager(ManagedObject):
   class Permission(DynamicData):
      entity: Optional[ManagedEntity] = None
      principal: str
      group: bool
      roleId: int
      propagate: bool

   class Role(DynamicData):
      roleId: int
      system: bool
      name: str
      info: Description
      privilege: list[str] = []

   class Privilege(DynamicData):
      privId: str
      onParent: bool
      name: str
      privGroupName: str

   class PrivilegeAvailability(DynamicData):
      privId: str
      isGranted: bool

   class EntityPrivilege(DynamicData):
      entity: ManagedEntity
      privAvailability: list[PrivilegeAvailability] = []

   class UserPrivilegeResult(DynamicData):
      entity: ManagedEntity
      privileges: list[str] = []

   @property
   def privilegeList(self) -> list[Privilege]: ...
   @property
   def roleList(self) -> list[Role]: ...
   @property
   def description(self) -> AuthorizationDescription: ...

   def AddRole(self, name: str, privIds: list[str]) -> int: ...
   def RemoveRole(self, roleId: int, failIfUsed: bool) -> None: ...
   def UpdateRole(self, roleId: int, newName: str, privIds: list[str]) -> None: ...
   def MergePermissions(self, srcRoleId: int, dstRoleId: int) -> None: ...
   def RetrieveRolePermissions(self, roleId: int) -> list[Permission]: ...
   def RetrieveEntityPermissions(self, entity: ManagedEntity, inherited: bool) -> list[Permission]: ...
   def RetrieveAllPermissions(self) -> list[Permission]: ...
   def SetEntityPermissions(self, entity: ManagedEntity, permission: list[Permission]) -> None: ...
   def ResetEntityPermissions(self, entity: ManagedEntity, permission: list[Permission]) -> None: ...
   def RemoveEntityPermission(self, entity: ManagedEntity, user: str, isGroup: bool) -> None: ...
   def HasPrivilegeOnEntity(self, entity: ManagedEntity, sessionId: str, privId: list[str]) -> list[bool]: ...
   def HasPrivilegeOnEntities(self, entity: list[ManagedEntity], sessionId: str, privId: list[str]) -> list[EntityPrivilege]: ...
   def HasUserPrivilegeOnEntities(self, entities: list[ManagedObject], userName: str, privId: list[str]) -> list[EntityPrivilege]: ...
   def FetchUserPrivilegeOnEntities(self, entities: list[ManagedEntity], userName: str) -> list[UserPrivilegeResult]: ...


class BatchResult(DynamicData):
   class Result(Enum):
      success: ClassVar['Result'] = 'success'
      fail: ClassVar['Result'] = 'fail'

   result: str
   hostKey: str
   ds: Optional[Datastore] = None
   fault: Optional[MethodFault] = None


class BoolPolicy(InheritablePolicy):
   value: Optional[bool] = None


class Capability(DynamicData):
   provisioningSupported: bool
   multiHostSupported: bool
   userShellAccessSupported: bool
   supportedEVCMode: list[EVCMode] = []
   supportedEVCGraphicsMode: list[FeatureEVCMode] = []
   networkBackupAndRestoreSupported: Optional[bool] = None
   ftDrsWithoutEvcSupported: Optional[bool] = None
   hciWorkflowSupported: Optional[bool] = None
   computePolicyVersion: Optional[int] = None
   clusterPlacementSupported: Optional[bool] = None
   lifecycleManagementSupported: Optional[bool] = None
   hostSeedingSupported: Optional[bool] = None
   scalableSharesSupported: Optional[bool] = None
   hadcsSupported: Optional[bool] = None
   configMgmtSupported: Optional[bool] = None


class CertificateManager(ManagedObject):
   def RefreshCACertificatesAndCRLs(self, host: list[HostSystem]) -> Task: ...
   def RefreshCertificates(self, host: list[HostSystem]) -> Task: ...
   def RevokeCertificates(self, host: list[HostSystem]) -> Task: ...


class ClusterComputeResource(ComputeResource):
   class Summary(ComputeResource.Summary):
      currentFailoverLevel: int
      admissionControlInfo: Optional[DasAdmissionControlInfo] = None
      numVmotions: int
      targetBalance: Optional[int] = None
      currentBalance: Optional[int] = None
      drsScore: Optional[int] = None
      numVmsPerDrsScoreBucket: list[int] = []
      usageSummary: Optional[UsageSummary] = None
      currentEVCModeKey: Optional[str] = None
      currentEVCGraphicsModeKey: Optional[str] = None
      dasData: Optional[DasData] = None
      clusterMaintenanceModeStatus: Optional[str] = None
      vcsHealthStatus: Optional[str] = None
      vcsSlots: list[VcsSlots] = []

   class DVSSetting(DynamicData):
      class DVPortgroupToServiceMapping(DynamicData):
         dvPortgroup: DistributedVirtualPortgroup
         service: str

      dvSwitch: DistributedVirtualSwitch
      pnicDevices: list[str] = []
      dvPortgroupSetting: list[DVPortgroupToServiceMapping] = []

   class HCIWorkflowState(Enum):
      in_progress: ClassVar['HCIWorkflowState'] = 'in_progress'
      done: ClassVar['HCIWorkflowState'] = 'done'
      invalid: ClassVar['HCIWorkflowState'] = 'invalid'

   class HostConfigurationProfile(DynamicData):
      dateTimeConfig: Optional[DateTimeConfig] = None
      lockdownMode: Optional[HostAccessManager.LockdownMode] = None

   class HCIConfigInfo(DynamicData):
      workflowState: str
      dvsSetting: list[DVSSetting] = []
      configuredHosts: list[HostSystem] = []
      hostConfigProfile: Optional[HostConfigurationProfile] = None

   class ClusterConfigResult(DynamicData):
      failedHosts: list[Folder.FailedHostResult] = []
      configuredHosts: list[HostSystem] = []

   class DvsProfile(DynamicData):
      class DVPortgroupSpecToServiceMapping(DynamicData):
         dvPortgroupSpec: Optional[DistributedVirtualPortgroup.ConfigSpec] = None
         dvPortgroup: Optional[DistributedVirtualPortgroup] = None
         service: str

      dvsName: Optional[str] = None
      dvSwitch: Optional[DistributedVirtualSwitch] = None
      pnicDevices: list[str] = []
      dvPortgroupMapping: list[DVPortgroupSpecToServiceMapping] = []

   class VCProfile(DynamicData):
      clusterSpec: Optional[ConfigSpecEx] = None
      evcModeKey: Optional[str] = None
      evcGraphicsModeKey: Optional[str] = None

   class HCIConfigSpec(DynamicData):
      dvsProf: list[DvsProfile] = []
      hostConfigProfile: Optional[HostConfigurationProfile] = None
      vSanConfigSpec: Optional[SDDCBase] = None
      vcProf: Optional[VCProfile] = None

   class HostVmkNicInfo(DynamicData):
      nicSpec: VirtualNic.Specification
      service: str

   class HostConfigurationInput(DynamicData):
      host: HostSystem
      hostVmkNics: list[HostVmkNicInfo] = []
      allowedInNonMaintenanceMode: Optional[bool] = None

   class ValidationResultBase(DynamicData):
      info: list[LocalizableMessage] = []

   class HostConfigurationValidation(ValidationResultBase):
      host: HostSystem
      isDvsSettingValid: Optional[bool] = None
      isVmknicSettingValid: Optional[bool] = None
      isNtpSettingValid: Optional[bool] = None
      isLockdownModeValid: Optional[bool] = None

   class DVSConfigurationValidation(ValidationResultBase):
      isDvsValid: bool
      isDvpgValid: bool

   class HostEvacuationInfo(DynamicData):
      host: HostSystem
      action: list[OptionValue] = []

   class MaintenanceInfo(DynamicData):
      partialMMId: Optional[str] = None
      hostEvacInfo: list[HostEvacuationInfo] = []

   class CryptoModePolicy(DynamicData):
      keyId: Optional[CryptoKeyId] = None
      providerId: Optional[KeyProviderId] = None

   class VcsHealthStatus(Enum):
      healthy: ClassVar['VcsHealthStatus'] = 'healthy'
      degraded: ClassVar['VcsHealthStatus'] = 'degraded'
      nonhealthy: ClassVar['VcsHealthStatus'] = 'nonhealthy'

   class VcsSlots(DynamicData):
      systemId: Optional[str] = None
      host: HostSystem
      datastore: list[Datastore] = []
      totalSlots: int

   @property
   def configuration(self) -> ConfigInfo: ...
   @property
   def recommendation(self) -> list[Recommendation]: ...
   @property
   def drsRecommendation(self) -> list[DrsRecommendation]: ...
   @property
   def summaryEx(self) -> Summary: ...
   @property
   def hciConfig(self) -> Optional[HCIConfigInfo]: ...
   @property
   def migrationHistory(self) -> list[DrsMigration]: ...
   @property
   def actionHistory(self) -> list[ActionHistory]: ...
   @property
   def drsFault(self) -> list[DrsFaults]: ...

   def ConfigureHCI(self, clusterSpec: HCIConfigSpec, hostInputs: list[HostConfigurationInput]) -> Task: ...
   def ExtendHCI(self, hostInputs: list[HostConfigurationInput], vSanConfigSpec: Optional[SDDCBase]) -> Task: ...
   def AbandonHciWorkflow(self) -> None: ...
   def ValidateHCIConfiguration(self, hciConfigSpec: Optional[HCIConfigSpec], hosts: list[HostSystem]) -> list[ValidationResultBase]: ...
   def Reconfigure(self, spec: ConfigSpec, modify: bool) -> Task: ...
   def ApplyRecommendation(self, key: str) -> None: ...
   def CancelRecommendation(self, key: str) -> None: ...
   def RecommendHostsForVm(self, vm: VirtualMachine, pool: Optional[ResourcePool]) -> list[HostRecommendation]: ...
   def AddHost(self, spec: ConnectSpec, asConnected: bool, resourcePool: Optional[ResourcePool], license: Optional[str]) -> Task: ...
   def MoveInto(self, host: list[HostSystem]) -> Task: ...
   def MoveHostInto(self, host: HostSystem, resourcePool: Optional[ResourcePool]) -> Task: ...
   def RefreshRecommendation(self) -> None: ...
   def EvcManager(self) -> Optional[EVCManager]: ...
   def RetrieveDasAdvancedRuntimeInfo(self) -> Optional[DasAdvancedRuntimeInfo]: ...
   def EnterMaintenanceMode(self, host: list[HostSystem], option: list[OptionValue], info: Optional[MaintenanceInfo]) -> EnterMaintenanceResult: ...
   def PlaceVm(self, placementSpec: PlacementSpec) -> PlacementResult: ...
   def FindRulesForVm(self, vm: VirtualMachine) -> list[RuleInfo]: ...
   def StampAllRulesWithUuid(self) -> Task: ...
   def GetResourceUsage(self) -> ResourceUsageSummary: ...
   def SetCryptoMode(self, cryptoMode: str, policy: Optional[CryptoModePolicy]) -> None: ...
   def GetSystemVMsRestrictedDatastores(self) -> list[Datastore]: ...


class ComputeResource(ManagedEntity):
   class Summary(DynamicData):
      totalCpu: int
      totalMemory: long
      numCpuCores: short
      numCpuThreads: short
      effectiveCpu: int
      effectiveMemory: long
      numHosts: int
      numEffectiveHosts: int
      overallStatus: ManagedEntity.Status

   class NetworkBootMode(Enum):
      bootstrap: ClassVar['NetworkBootMode'] = 'bootstrap'
      stateless: ClassVar['NetworkBootMode'] = 'stateless'

   class ConfigInfo(DynamicData):
      vmSwapPlacement: str
      spbmEnabled: Optional[bool] = None
      defaultHardwareVersionKey: Optional[str] = None
      maximumHardwareVersionKey: Optional[str] = None

   class HostSPBMLicenseInfo(DynamicData):
      class HostSPBMLicenseState(Enum):
         licensed: ClassVar['HostSPBMLicenseState'] = 'licensed'
         unlicensed: ClassVar['HostSPBMLicenseState'] = 'unlicensed'
         unknown: ClassVar['HostSPBMLicenseState'] = 'unknown'

      host: HostSystem
      licenseState: HostSPBMLicenseState

   class HostSeedSpec(DynamicData):
      class SingleHostSpec(DynamicData):
         newHostCnxSpec: Optional[ConnectSpec] = None
         existingHost: Optional[HostSystem] = None

      singleHostSpec: SingleHostSpec

   class ConfigSpec(DynamicData):
      vmSwapPlacement: Optional[str] = None
      spbmEnabled: Optional[bool] = None
      defaultHardwareVersionKey: Optional[str] = None
      desiredSoftwareSpec: Optional[DesiredSoftwareSpec] = None
      maximumHardwareVersionKey: Optional[str] = None
      enableConfigManager: Optional[bool] = None
      hostSeedSpec: Optional[HostSeedSpec] = None
      softwareSpecId: Optional[str] = None
      networkBootMode: Optional[str] = None

   @property
   def resourcePool(self) -> Optional[ResourcePool]: ...
   @property
   def host(self) -> list[HostSystem]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def environmentBrowser(self) -> Optional[EnvironmentBrowser]: ...
   @property
   def configurationEx(self) -> ConfigInfo: ...
   @property
   def lifecycleManaged(self) -> Optional[bool]: ...
   @property
   def configManagerEnabled(self) -> Optional[bool]: ...
   @property
   def networkBootMode(self) -> Optional[str]: ...

   def EnableNetworkBoot(self, networkBootMode: str) -> Task: ...
   def DisableNetworkBoot(self) -> Task: ...
   def ReconfigureEx(self, spec: ConfigSpec, modify: bool) -> Task: ...

class ConfigSpecOperation:
   pass


class CustomFieldsManager(ManagedObject):
   class FieldDef(DynamicData):
      key: int
      name: str
      type: type
      managedObjectType: Optional[type] = None
      fieldDefPrivileges: Optional[PrivilegePolicyDef] = None
      fieldInstancePrivileges: Optional[PrivilegePolicyDef] = None

   class Value(DynamicData):
      key: int

   class StringValue(Value):
      value: str

   @property
   def field(self) -> list[FieldDef]: ...

   def AddFieldDefinition(self, name: str, moType: Optional[type], fieldDefPolicy: Optional[PrivilegePolicyDef], fieldPolicy: Optional[PrivilegePolicyDef]) -> FieldDef: ...
   def RemoveFieldDefinition(self, key: int) -> None: ...
   def RenameFieldDefinition(self, key: int, name: str) -> None: ...
   def SetField(self, entity: ManagedEntity, key: int, value: str) -> None: ...


class CustomizationSpecInfo(DynamicData):
   name: str
   description: str
   type: str
   changeVersion: Optional[str] = None
   lastUpdateTime: Optional[datetime] = None


class CustomizationSpecItem(DynamicData):
   info: CustomizationSpecInfo
   spec: Specification


class CustomizationSpecManager(ManagedObject):
   @property
   def info(self) -> list[CustomizationSpecInfo]: ...
   @property
   def encryptionKey(self) -> list[byte]: ...

   def Exists(self, name: str) -> bool: ...
   def Get(self, name: str) -> CustomizationSpecItem: ...
   def Create(self, item: CustomizationSpecItem) -> None: ...
   def Overwrite(self, item: CustomizationSpecItem) -> None: ...
   def Delete(self, name: str) -> None: ...
   def Duplicate(self, name: str, newName: str) -> None: ...
   def Rename(self, name: str, newName: str) -> None: ...
   def SpecItemToXml(self, item: CustomizationSpecItem) -> str: ...
   def XmlToSpecItem(self, specItemXml: str) -> CustomizationSpecItem: ...
   def CheckResources(self, guestOs: str) -> None: ...
   def IsGuestOsCustomizable(self, guestId: str) -> bool: ...


class Datacenter(ManagedEntity):
   class BasicConnectInfo(DynamicData):
      hostname: Optional[str] = None
      error: Optional[MethodFault] = None
      serverIp: Optional[str] = None
      numVm: Optional[int] = None
      numPoweredOnVm: Optional[int] = None
      hostProductInfo: Optional[AboutInfo] = None
      hardwareVendor: Optional[str] = None
      hardwareModel: Optional[str] = None

   class ConfigInfo(DynamicData):
      defaultHardwareVersionKey: Optional[str] = None
      maximumHardwareVersionKey: Optional[str] = None

   class ConfigSpec(DynamicData):
      defaultHardwareVersionKey: Optional[str] = None
      maximumHardwareVersionKey: Optional[str] = None

   @property
   def vmFolder(self) -> Folder: ...
   @property
   def hostFolder(self) -> Folder: ...
   @property
   def datastoreFolder(self) -> Folder: ...
   @property
   def networkFolder(self) -> Folder: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def configuration(self) -> ConfigInfo: ...

   def BatchQueryConnectInfo(self, hostSpecs: list[ConnectSpec]) -> list[BasicConnectInfo]: ...
   def QueryConnectionInfo(self, hostname: str, port: int, username: str, password: str, sslThumbprint: Optional[str], sslCertificate: Optional[str]) -> ConnectInfo: ...
   def QueryConnectionInfoViaSpec(self, spec: ConnectSpec) -> ConnectInfo: ...
   def PowerOnVm(self, vm: list[VirtualMachine], option: list[OptionValue]) -> Task: ...
   def QueryConfigOptionDescriptor(self) -> list[ConfigOptionDescriptor]: ...
   def Reconfigure(self, spec: ConfigSpec, modify: bool) -> Task: ...


class Datastore(ManagedEntity):
   class Accessible(Enum):
      # Reserved python keyword: commenting out.
      # True: ClassVar['Accessible'] = 'True'
      # Reserved python keyword: commenting out.
      # False: ClassVar['Accessible'] = 'False'
      pass

   class SectorFormat(Enum):
      native_512: ClassVar['SectorFormat'] = 'native_512'
      emulated_512: ClassVar['SectorFormat'] = 'emulated_512'
      native_4k: ClassVar['SectorFormat'] = 'native_4k'

   class Summary(DynamicData):
      class MaintenanceModeState(Enum):
         normal: ClassVar['MaintenanceModeState'] = 'normal'
         enteringMaintenance: ClassVar['MaintenanceModeState'] = 'enteringMaintenance'
         inMaintenance: ClassVar['MaintenanceModeState'] = 'inMaintenance'

      datastore: Optional[Datastore] = None
      name: str
      url: str
      capacity: long
      freeSpace: long
      uncommitted: Optional[long] = None
      accessible: bool
      multipleHostAccess: Optional[bool] = None
      type: str
      maintenanceMode: Optional[str] = None

   class Info(DynamicData):
      name: str
      url: str
      freeSpace: long
      maxFileSize: long
      maxVirtualDiskCapacity: Optional[long] = None
      maxMemoryFileSize: long
      timestamp: Optional[datetime] = None
      containerId: Optional[str] = None
      aliasOf: Optional[str] = None
      supportedVDiskFormats: list[str] = []
      logicalSectorSize: Optional[int] = None
      physicalSectorSize: Optional[int] = None

   class Capability(DynamicData):
      directoryHierarchySupported: bool
      rawDiskMappingsSupported: bool
      perFileThinProvisioningSupported: bool
      storageIORMSupported: bool
      nativeSnapshotSupported: bool
      topLevelDirectoryCreateSupported: Optional[bool] = None
      seSparseSupported: Optional[bool] = None
      vmfsSparseSupported: Optional[bool] = None
      vsanSparseSupported: Optional[bool] = None
      upitSupported: Optional[bool] = None
      vmdkExpandSupported: Optional[bool] = None
      clusteredVmdkSupported: Optional[bool] = None

   class HostMount(DynamicData):
      key: HostSystem
      mountInfo: MountInfo

   class MountPathDatastorePair(DynamicData):
      oldMountPath: str
      datastore: Datastore

   class VVolContainerFailoverPair(DynamicData):
      srcContainer: Optional[str] = None
      tgtContainer: str
      vvolMapping: list[KeyValue] = []

   @property
   def info(self) -> Info: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def host(self) -> list[HostMount]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def browser(self) -> DatastoreBrowser: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def iormConfiguration(self) -> Optional[StorageResourceManager.IORMConfigInfo]: ...

   def Refresh(self) -> None: ...
   def RefreshStorageInfo(self) -> None: ...
   def UpdateVirtualMachineFiles(self, mountPathDatastoreMapping: list[MountPathDatastorePair]) -> Task: ...
   def RenameDatastore(self, newName: str) -> None: ...
   def DestroyDatastore(self) -> None: ...
   def EnterMaintenanceMode(self) -> StoragePlacementResult: ...
   def ExitMaintenanceMode(self) -> Task: ...
   def IsClusteredVmdkEnabled(self) -> bool: ...
   def UpdateVVolVirtualMachineFiles(self, failoverPair: list[VVolContainerFailoverPair]) -> Task: ...


class DatastoreNamespaceManager(ManagedObject):
   class DirectoryInfo(DynamicData):
      capacity: long
      used: long

   def CreateDirectory(self, datastore: Datastore, displayName: Optional[str], policy: Optional[str], size: Optional[long]) -> str: ...
   def DeleteDirectory(self, datacenter: Optional[Datacenter], datastorePath: str) -> None: ...
   def ConvertNamespacePathToUuidPath(self, datacenter: Optional[Datacenter], namespaceUrl: str) -> str: ...
   def IncreaseDirectorySize(self, datacenter: Optional[Datacenter], stableName: str, size: long) -> None: ...
   def QueryDirectoryInfo(self, datacenter: Optional[Datacenter], stableName: str) -> DirectoryInfo: ...


class Description(DynamicData):
   label: str
   summary: str


class DesiredSoftwareSpec(DynamicData):
   class BaseImageSpec(DynamicData):
      version: str

   class VendorAddOnSpec(DynamicData):
      name: str
      version: str

   class ComponentSpec(DynamicData):
      name: str
      version: Optional[str] = None

   baseImageSpec: BaseImageSpec
   vendorAddOnSpec: Optional[VendorAddOnSpec] = None
   components: list[ComponentSpec] = []
   removedComponents: list[str] = []


class DiagnosticManager(ManagedObject):
   class LogDescriptor(DynamicData):
      class Creator(Enum):
         vpxd: ClassVar['Creator'] = 'vpxd'
         vpxa: ClassVar['Creator'] = 'vpxa'
         hostd: ClassVar['Creator'] = 'hostd'
         serverd: ClassVar['Creator'] = 'serverd'
         install: ClassVar['Creator'] = 'install'
         vpxClient: ClassVar['Creator'] = 'vpxClient'
         recordLog: ClassVar['Creator'] = 'recordLog'

      class Format(Enum):
         plain: ClassVar['Format'] = 'plain'

      key: str
      fileName: str
      creator: str
      format: str
      mimeType: str
      info: Description

   class LogHeader(DynamicData):
      lineStart: int
      lineEnd: int
      lineText: list[str] = []

   class BundleInfo(DynamicData):
      system: Optional[HostSystem] = None
      url: str

   class AuditRecordResult(DynamicData):
      records: list[str] = []
      nextToken: str

   def QueryDescriptions(self, host: Optional[HostSystem]) -> list[LogDescriptor]: ...
   def Browse(self, host: Optional[HostSystem], key: str, start: Optional[int], lines: Optional[int]) -> LogHeader: ...
   def GenerateLogBundles(self, includeDefault: bool, host: list[HostSystem]) -> Task: ...
   def FetchAuditRecords(self, token: Optional[str]) -> AuditRecordResult: ...
   def EmitSyslogMark(self, message: str) -> None: ...


class DirectPathProfileManager(ManagedObject):
   class DirectPathConfig(DynamicData):
      pass

   class VmiopDirectPathConfig(DirectPathConfig):
      vgpuProfile: str

   class DvxDirectPathConfig(DirectPathConfig):
      dvxBacking: VirtualPCIPassthrough.DvxBackingInfo

   class DynamicDirectPathConfig(DirectPathConfig):
      dynamicDirectPathBacking: VirtualPCIPassthrough.DynamicBackingInfo

   class VirtualDeviceGroupDirectPathConfig(DirectPathConfig):
      deviceGroupName: str

   class CreateSpec(DynamicData):
      name: str
      description: Optional[str] = None
      deviceConfig: DirectPathConfig

   class UpdateSpec(DynamicData):
      name: Optional[str] = None
      description: Optional[str] = None

   class FilterSpec(DynamicData):
      ids: list[str] = []
      names: list[str] = []
      clusters: list[ClusterComputeResource] = []

   class DirectPathProfileInfo(DynamicData):
      id: str
      name: str
      description: Optional[str] = None
      vendorName: str
      deviceConfig: DirectPathConfig

   class TargetEntity(DynamicData):
      pass

   class TargetHost(TargetEntity):
      host: HostSystem

   class TargetCluster(TargetEntity):
      cluster: ClusterComputeResource

   class CapacityQuerySpec(DynamicData):
      pass

   class CapacityQueryById(CapacityQuerySpec):
      id: str

   class CapacityQueryByName(CapacityQuerySpec):
      name: str

   class CapacityQueryByDeviceConfig(CapacityQuerySpec):
      deviceConfig: DirectPathConfig

   class CapacityResult(DynamicData):
      pass

   class CapacityInfo(CapacityResult):
      profile: DirectPathProfileInfo
      consumed: int
      remaining: int
      max: int
      unusedReservation: int

   class CapacityUnknown(CapacityResult):
      querySpec: CapacityQuerySpec
      faultList: list[MethodFault] = []

   def CreateDirectPathProfile(self, spec: CreateSpec) -> str: ...
   def UpdateDirectPathProfile(self, id: str, spec: UpdateSpec) -> None: ...
   def DeleteDirectPathProfile(self, id: str) -> None: ...
   def ListDirectPathProfiles(self, filterSpec: FilterSpec) -> list[DirectPathProfileInfo]: ...
   def QueryDirectPathProfileCapacity(self, target: TargetEntity, querySpec: list[CapacityQuerySpec]) -> list[CapacityResult]: ...


class DistributedVirtualSwitch(ManagedEntity):
   class ProductSpecOperationType(Enum):
      preInstall: ClassVar['ProductSpecOperationType'] = 'preInstall'
      upgrade: ClassVar['ProductSpecOperationType'] = 'upgrade'
      notifyAvailableUpgrade: ClassVar['ProductSpecOperationType'] = 'notifyAvailableUpgrade'
      proceedWithUpgrade: ClassVar['ProductSpecOperationType'] = 'proceedWithUpgrade'
      updateBundleInfo: ClassVar['ProductSpecOperationType'] = 'updateBundleInfo'

   class ContactInfo(DynamicData):
      name: Optional[str] = None
      contact: Optional[str] = None

   class NicTeamingPolicyMode(Enum):
      loadbalance_ip: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_ip'
      loadbalance_srcmac: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_srcmac'
      loadbalance_srcid: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_srcid'
      failover_explicit: ClassVar['NicTeamingPolicyMode'] = 'failover_explicit'
      loadbalance_loadbased: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_loadbased'

   class NetworkResourceManagementCapability(DynamicData):
      networkResourceManagementSupported: bool
      networkResourcePoolHighShareValue: int
      qosSupported: bool
      userDefinedNetworkResourcePoolsSupported: bool
      networkResourceControlVersion3Supported: Optional[bool] = None
      userDefinedInfraTrafficPoolSupported: Optional[bool] = None

   class RollbackCapability(DynamicData):
      rollbackSupported: bool

   class BackupRestoreCapability(DynamicData):
      backupRestoreSupported: bool

   class FeatureCapability(DynamicData):
      networkResourceManagementSupported: bool
      vmDirectPathGen2Supported: Optional[bool] = None
      nicTeamingPolicy: list[str] = []
      networkResourcePoolHighShareValue: Optional[int] = None
      networkResourceManagementCapability: Optional[NetworkResourceManagementCapability] = None
      healthCheckCapability: Optional[HealthCheckFeatureCapability] = None
      rollbackCapability: Optional[RollbackCapability] = None
      backupRestoreCapability: Optional[BackupRestoreCapability] = None
      networkFilterSupported: Optional[bool] = None
      macLearningSupported: Optional[bool] = None

   class HealthCheckFeatureCapability(DynamicData):
      pass

   class Capability(DynamicData):
      dvsOperationSupported: Optional[bool] = None
      dvPortGroupOperationSupported: Optional[bool] = None
      dvPortOperationSupported: Optional[bool] = None
      compatibleHostComponentProductInfo: list[HostProductSpec] = []
      featuresSupported: Optional[FeatureCapability] = None

   class Summary(DynamicData):
      name: str
      uuid: str
      numPorts: int
      productInfo: Optional[ProductSpec] = None
      hostMember: list[HostSystem] = []
      vm: list[VirtualMachine] = []
      host: list[HostSystem] = []
      portgroupName: list[str] = []
      description: Optional[str] = None
      contact: Optional[ContactInfo] = None
      numHosts: Optional[int] = None

   class SwitchPolicy(DynamicData):
      autoPreInstallAllowed: Optional[bool] = None
      autoUpgradeAllowed: Optional[bool] = None
      partialUpgradeAllowed: Optional[bool] = None

   class UplinkPortPolicy(DynamicData):
      pass

   class NameArrayUplinkPortPolicy(UplinkPortPolicy):
      uplinkPortName: list[str] = []

   class ConfigSpec(DynamicData):
      configVersion: Optional[str] = None
      name: Optional[str] = None
      numStandalonePorts: Optional[int] = None
      maxPorts: Optional[int] = None
      uplinkPortPolicy: Optional[UplinkPortPolicy] = None
      uplinkPortgroup: list[DistributedVirtualPortgroup] = []
      defaultPortConfig: Optional[DistributedVirtualPort.Setting] = None
      host: list[HostMember.ConfigSpec] = []
      extensionKey: Optional[str] = None
      description: Optional[str] = None
      policy: Optional[SwitchPolicy] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      contact: Optional[ContactInfo] = None
      switchIpAddress: Optional[str] = None
      defaultProxySwitchMaxNumPorts: Optional[int] = None
      infrastructureTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      netResourcePoolTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      networkResourceControlVersion: Optional[str] = None

   class CreateSpec(DynamicData):
      configSpec: ConfigSpec
      productInfo: Optional[ProductSpec] = None
      capability: Optional[Capability] = None

   class ConfigInfo(DynamicData):
      uuid: str
      name: str
      numStandalonePorts: int
      numPorts: int
      maxPorts: int
      uplinkPortPolicy: UplinkPortPolicy
      uplinkPortgroup: list[DistributedVirtualPortgroup] = []
      defaultPortConfig: DistributedVirtualPort.Setting
      host: list[HostMember] = []
      productInfo: ProductSpec
      targetInfo: Optional[ProductSpec] = None
      extensionKey: Optional[str] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      policy: Optional[SwitchPolicy] = None
      description: Optional[str] = None
      configVersion: str
      contact: ContactInfo
      switchIpAddress: Optional[str] = None
      createTime: datetime
      networkResourceManagementEnabled: bool
      defaultProxySwitchMaxNumPorts: Optional[int] = None
      healthCheckConfig: list[HealthCheckConfig] = []
      infrastructureTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      netResourcePoolTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      networkResourceControlVersion: Optional[str] = None
      vmVnicNetworkResourcePool: list[VmVnicNetworkResourcePool] = []
      pnicCapacityRatioForReservation: Optional[int] = None

   class NetworkResourceControlVersion(Enum):
      version2: ClassVar['NetworkResourceControlVersion'] = 'version2'
      version3: ClassVar['NetworkResourceControlVersion'] = 'version3'

   class HostInfrastructureTrafficClass(Enum):
      management: ClassVar['HostInfrastructureTrafficClass'] = 'management'
      faultTolerance: ClassVar['HostInfrastructureTrafficClass'] = 'faultTolerance'
      vmotion: ClassVar['HostInfrastructureTrafficClass'] = 'vmotion'
      virtualMachine: ClassVar['HostInfrastructureTrafficClass'] = 'virtualMachine'
      iSCSI: ClassVar['HostInfrastructureTrafficClass'] = 'iSCSI'
      nfs: ClassVar['HostInfrastructureTrafficClass'] = 'nfs'
      hbr: ClassVar['HostInfrastructureTrafficClass'] = 'hbr'
      vsan: ClassVar['HostInfrastructureTrafficClass'] = 'vsan'
      vdp: ClassVar['HostInfrastructureTrafficClass'] = 'vdp'
      backupNfc: ClassVar['HostInfrastructureTrafficClass'] = 'backupNfc'
      nvmetcp: ClassVar['HostInfrastructureTrafficClass'] = 'nvmetcp'
      provisioning: ClassVar['HostInfrastructureTrafficClass'] = 'provisioning'
      vSANiSCSI: ClassVar['HostInfrastructureTrafficClass'] = 'vSANiSCSI'

   class HostInfrastructureTrafficResource(DynamicData):
      class ResourceAllocation(DynamicData):
         limit: Optional[long] = None
         shares: Optional[SharesInfo] = None
         reservation: Optional[long] = None

      key: str
      description: Optional[str] = None
      allocationInfo: ResourceAllocation

   class HealthCheckConfig(DynamicData):
      enable: Optional[bool] = None
      interval: Optional[int] = None

   class ResourceRuntimeInfo(DynamicData):
      capacity: Optional[int] = None
      usage: Optional[int] = None
      available: Optional[int] = None
      allocatedResource: list[VmVnicNetworkResourcePool.VnicAllocatedResource] = []
      vmVnicNetworkResourcePoolRuntime: list[VmVnicNetworkResourcePool.RuntimeInfo] = []

   class RuntimeInfo(DynamicData):
      hostMemberRuntime: list[HostMember.RuntimeInfo] = []
      resourceRuntimeInfo: Optional[ResourceRuntimeInfo] = None

   @property
   def uuid(self) -> str: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def networkResourcePool(self) -> list[NetworkResourcePool]: ...
   @property
   def portgroup(self) -> list[DistributedVirtualPortgroup]: ...
   @property
   def runtime(self) -> Optional[RuntimeInfo]: ...

   def FetchPortKeys(self, criteria: Optional[PortCriteria]) -> list[str]: ...
   def FetchPorts(self, criteria: Optional[PortCriteria]) -> list[DistributedVirtualPort]: ...
   def QueryUsedVlanId(self) -> list[int]: ...
   def Reconfigure(self, spec: ConfigSpec) -> Task: ...
   def PerformProductSpecOperation(self, operation: str, productSpec: Optional[ProductSpec]) -> Task: ...
   def Merge(self, dvs: DistributedVirtualSwitch) -> Task: ...
   def AddPortgroups(self, spec: list[DistributedVirtualPortgroup.ConfigSpec]) -> Task: ...
   def MovePort(self, portKey: list[str], destinationPortgroupKey: Optional[str]) -> Task: ...
   def UpdateCapability(self, capability: Capability) -> None: ...
   def ReconfigurePort(self, port: list[DistributedVirtualPort.ConfigSpec]) -> Task: ...
   def RefreshPortState(self, portKeys: list[str]) -> None: ...
   def RectifyHost(self, hosts: list[HostSystem]) -> Task: ...
   def UpdateNetworkResourcePool(self, configSpec: list[NetworkResourcePool.ConfigSpec]) -> None: ...
   def AddNetworkResourcePool(self, configSpec: list[NetworkResourcePool.ConfigSpec]) -> None: ...
   def RemoveNetworkResourcePool(self, key: list[str]) -> None: ...
   def ReconfigureVmVnicNetworkResourcePool(self, configSpec: list[VmVnicNetworkResourcePool.ConfigSpec]) -> Task: ...
   def EnableNetworkResourceManagement(self, enable: bool) -> None: ...
   def Rollback(self, entityBackup: Optional[EntityBackup.Config]) -> Task: ...
   def AddPortgroup(self, spec: DistributedVirtualPortgroup.ConfigSpec) -> Task: ...
   def UpdateHealthCheckConfig(self, healthCheckConfig: list[HealthCheckConfig]) -> Task: ...
   def LookupPortgroup(self, portgroupKey: str) -> Optional[DistributedVirtualPortgroup]: ...


class EVCMode(ElementDescription):
   guaranteedCPUFeatures: list[CpuIdInfo] = []
   featureCapability: list[FeatureCapability] = []
   featureMask: list[FeatureMask] = []
   featureRequirement: list[FeatureRequirement] = []
   vendor: str
   track: list[str] = []
   vendorTier: int

class ElementDescription(Description):
   key: str


class EnumDescription(DynamicData):
   key: type
   tags: list[ElementDescription] = []


class EnvironmentBrowser(ManagedObject):
   class ConfigOptionQuerySpec(DynamicData):
      key: Optional[str] = None
      host: Optional[HostSystem] = None
      guestId: list[str] = []

   @property
   def datastoreBrowser(self) -> Optional[DatastoreBrowser]: ...

   def QueryConfigOptionDescriptor(self) -> list[ConfigOptionDescriptor]: ...
   def QueryConfigOption(self, key: Optional[str], host: Optional[HostSystem]) -> Optional[ConfigOption]: ...
   def QueryConfigOptionEx(self, spec: Optional[ConfigOptionQuerySpec]) -> Optional[ConfigOption]: ...
   def QueryConfigTarget(self, host: Optional[HostSystem]) -> Optional[ConfigTarget]: ...
   def QueryTargetCapabilities(self, host: Optional[HostSystem]) -> Optional[Capability]: ...


class ExtendedDescription(Description):
   messageCatalogKeyPrefix: str
   messageArg: list[KeyAnyValue] = []


class ExtendedElementDescription(ElementDescription):
   messageCatalogKeyPrefix: str
   messageArg: list[KeyAnyValue] = []


class ExtensibleManagedObject(ManagedObject):
   @property
   def value(self) -> list[CustomFieldsManager.Value]: ...
   @property
   def availableField(self) -> list[CustomFieldsManager.FieldDef]: ...

   def SetCustomValue(self, key: str, value: str) -> None: ...


class Extension(DynamicData):
   class ServerInfo(DynamicData):
      url: str
      description: Description
      company: str
      type: str
      adminEmail: list[str] = []
      serverThumbprint: Optional[str] = None
      serverCertificate: Optional[str] = None

   class ClientInfo(DynamicData):
      version: str
      description: Description
      company: str
      type: str
      url: str

   class TaskTypeInfo(DynamicData):
      taskID: str

   class EventTypeInfo(DynamicData):
      eventID: str
      eventTypeSchema: Optional[str] = None

   class FaultTypeInfo(DynamicData):
      faultID: str

   class PrivilegeInfo(DynamicData):
      privID: str
      privGroupName: str

   class ResourceInfo(DynamicData):
      locale: str
      module: str
      data: list[KeyValue] = []

   class HealthInfo(DynamicData):
      url: str

   class OvfConsumerInfo(DynamicData):
      callbackUrl: str
      sectionType: list[str] = []

   description: Description
   key: str
   company: Optional[str] = None
   type: Optional[str] = None
   version: str
   subjectName: Optional[str] = None
   server: list[ServerInfo] = []
   client: list[ClientInfo] = []
   taskList: list[TaskTypeInfo] = []
   eventList: list[EventTypeInfo] = []
   faultList: list[FaultTypeInfo] = []
   privilegeList: list[PrivilegeInfo] = []
   resourceList: list[ResourceInfo] = []
   lastHeartbeatTime: datetime
   healthInfo: Optional[HealthInfo] = None
   ovfConsumerInfo: Optional[OvfConsumerInfo] = None
   extendedProductInfo: Optional[ExtendedProductInfo] = None
   managedEntityInfo: list[ManagedEntityInfo] = []
   shownInSolutionManager: Optional[bool] = None
   solutionManagerInfo: Optional[SolutionManagerInfo] = None


class ExtensionManager(ManagedObject):
   class IpAllocationUsage(DynamicData):
      extensionKey: str
      numAddresses: int

   @property
   def extensionList(self) -> list[Extension]: ...

   def UnregisterExtension(self, extensionKey: str) -> None: ...
   def FindExtension(self, extensionKey: str) -> Optional[Extension]: ...
   def RegisterExtension(self, extension: Extension) -> None: ...
   def UpdateExtension(self, extension: Extension) -> None: ...
   def GetPublicKey(self) -> str: ...
   def SetPublicKey(self, extensionKey: str, publicKey: str) -> None: ...
   def SetCertificate(self, extensionKey: str, certificatePem: Optional[str]) -> None: ...
   def SetServiceAccount(self, extensionKey: str, serviceAccount: str) -> None: ...
   def QueryManagedBy(self, extensionKey: str) -> list[ManagedEntity]: ...
   def QueryExtensionIpAllocationUsage(self, extensionKeys: list[str]) -> list[IpAllocationUsage]: ...


class FaultsByHost(DynamicData):
   host: HostSystem
   faults: list[MethodFault] = []


class FaultsByVM(DynamicData):
   vm: VirtualMachine
   faults: list[MethodFault] = []


class FeatureEVCMode(ElementDescription):
   mask: list[FeatureMask] = []
   capability: list[FeatureCapability] = []
   requirement: list[FeatureRequirement] = []


class FileManager(ManagedObject):
   class FileLockInfo(DynamicData):
      filePath: str
      host: str
      mac: str
      id: str
      worldName: str
      ownerId: Optional[str] = None
      lockMode: str
      acquired: Optional[datetime] = None
      heartbeat: Optional[datetime] = None
      refCount: Optional[int] = None

   class FileLockInfoResult(DynamicData):
      lockInfo: list[FileLockInfo] = []
      fault: Optional[MethodFault] = None

   def MoveFile(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destinationName: str, destinationDatacenter: Optional[Datacenter], force: Optional[bool]) -> Task: ...
   def CopyFile(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destinationName: str, destinationDatacenter: Optional[Datacenter], force: Optional[bool]) -> Task: ...
   def DeleteFile(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def MakeDirectory(self, name: str, datacenter: Optional[Datacenter], createParentDirectories: Optional[bool]) -> None: ...
   def ChangeOwner(self, name: str, datacenter: Optional[Datacenter], owner: str) -> None: ...
   def QueryFileLockInfo(self, path: str, host: Optional[HostSystem]) -> FileLockInfoResult: ...


class Folder(ManagedEntity):
   class DesiredHostState(Enum):
      maintenance: ClassVar['DesiredHostState'] = 'maintenance'
      non_maintenance: ClassVar['DesiredHostState'] = 'non_maintenance'

   class NewHostSpec(DynamicData):
      hostCnxSpec: ConnectSpec
      esxLicense: Optional[str] = None

   class FailedHostResult(DynamicData):
      hostName: Optional[str] = None
      host: Optional[HostSystem] = None
      context: LocalizableMessage
      fault: MethodFault

   class BatchAddStandaloneHostsResult(DynamicData):
      addedHosts: list[HostSystem] = []
      hostsFailedInventoryAdd: list[FailedHostResult] = []

   class BatchAddHostsToClusterResult(DynamicData):
      hostsAddedToCluster: list[HostSystem] = []
      hostsFailedInventoryAdd: list[FailedHostResult] = []
      hostsFailedMoveToCluster: list[FailedHostResult] = []

   class ExternallyManagedFolderType(Enum):
      PROJECT_ROOT: ClassVar['ExternallyManagedFolderType'] = 'PROJECT_ROOT'
      PROJECT: ClassVar['ExternallyManagedFolderType'] = 'PROJECT'
      VPC_ROOT: ClassVar['ExternallyManagedFolderType'] = 'VPC_ROOT'
      VPC: ClassVar['ExternallyManagedFolderType'] = 'VPC'
      SUBNET: ClassVar['ExternallyManagedFolderType'] = 'SUBNET'
      SEGMENT: ClassVar['ExternallyManagedFolderType'] = 'SEGMENT'
      SUPERVISOR: ClassVar['ExternallyManagedFolderType'] = 'SUPERVISOR'
      VSPHERE_POD: ClassVar['ExternallyManagedFolderType'] = 'VSPHERE_POD'

   class ExternallyManagedFolderInfo(DynamicData):
      id: str
      type: str

   @property
   def childType(self) -> list[type]: ...
   @property
   def childEntity(self) -> list[ManagedEntity]: ...
   @property
   def namespace(self) -> Optional[str]: ...
   @property
   def externallyManagedFolderInfo(self) -> Optional[ExternallyManagedFolderInfo]: ...

   def CreateFolder(self, name: str) -> Folder: ...
   def MoveInto(self, list: list[ManagedEntity]) -> Task: ...
   def CreateVm(self, config: ConfigSpec, pool: ResourcePool, host: Optional[HostSystem]) -> Task: ...
   def RegisterVm(self, path: str, name: Optional[str], asTemplate: bool, pool: Optional[ResourcePool], host: Optional[HostSystem]) -> Task: ...
   def CreateCluster(self, name: str, spec: ConfigSpec) -> ClusterComputeResource: ...
   def CreateClusterEx(self, name: str, spec: ConfigSpecEx) -> ClusterComputeResource: ...
   def AddStandaloneHost(self, spec: ConnectSpec, compResSpec: Optional[ComputeResource.ConfigSpec], addConnected: bool, license: Optional[str]) -> Task: ...
   def CreateDatacenter(self, name: str) -> Datacenter: ...
   def UnregisterAndDestroy(self) -> Task: ...
   def CreateDistributedVirtualSwitch(self, spec: DistributedVirtualSwitch.CreateSpec) -> Task: ...
   def CreateStoragePod(self, name: str) -> StoragePod: ...
   def BatchAddStandaloneHosts(self, newHosts: list[NewHostSpec], compResSpec: Optional[ComputeResource.ConfigSpec], addConnected: bool) -> Task: ...
   def BatchAddHostsToCluster(self, cluster: ClusterComputeResource, newHosts: list[NewHostSpec], existingHosts: list[HostSystem], compResSpec: Optional[ComputeResource.ConfigSpec], desiredState: Optional[str]) -> Task: ...


class HbrReplicationTargetSpec(DynamicData):
   pass


class HbrTargetSpec(DynamicData):
   targetIP: str
   certificate: str


class HbrTargetSpecReplacement(HbrReplicationTargetSpec):
   spec: list[HbrTargetSpec] = []


class HealthUpdate(DynamicData):
   entity: ManagedEntity
   healthUpdateInfoId: str
   id: str
   status: ManagedEntity.Status
   remediation: str


class HealthUpdateInfo(DynamicData):
   class ComponentType(Enum):
      Memory: ClassVar['ComponentType'] = 'Memory'
      Power: ClassVar['ComponentType'] = 'Power'
      Fan: ClassVar['ComponentType'] = 'Fan'
      Network: ClassVar['ComponentType'] = 'Network'
      Storage: ClassVar['ComponentType'] = 'Storage'

   id: str
   componentType: str
   description: str


class HealthUpdateManager(ManagedObject):
   def RegisterProvider(self, name: str, healthUpdateInfo: list[HealthUpdateInfo]) -> str: ...
   def UnregisterProvider(self, providerId: str) -> None: ...
   def QueryProviderList(self) -> list[str]: ...
   def HasProvider(self, id: str) -> bool: ...
   def QueryProviderName(self, id: str) -> str: ...
   def QueryHealthUpdateInfos(self, providerId: str) -> list[HealthUpdateInfo]: ...
   def AddMonitoredEntities(self, providerId: str, entities: list[ManagedEntity]) -> None: ...
   def RemoveMonitoredEntities(self, providerId: str, entities: list[ManagedEntity]) -> None: ...
   def QueryMonitoredEntities(self, providerId: str) -> list[ManagedEntity]: ...
   def HasMonitoredEntity(self, providerId: str, entity: ManagedEntity) -> bool: ...
   def QueryUnmonitoredHosts(self, providerId: str, cluster: ClusterComputeResource) -> list[HostSystem]: ...
   def PostHealthUpdates(self, providerId: str, updates: list[HealthUpdate]) -> None: ...
   def QueryHealthUpdates(self, providerId: str) -> list[HealthUpdate]: ...
   def AddFilter(self, providerId: str, filterName: str, infoIds: list[str]) -> str: ...
   def QueryFilterList(self, providerId: str) -> list[str]: ...
   def QueryFilterName(self, filterId: str) -> str: ...
   def QueryFilterInfoIds(self, filterId: str) -> list[str]: ...
   def QueryFilterEntities(self, filterId: str) -> list[ManagedEntity]: ...
   def AddFilterEntities(self, filterId: str, entities: list[ManagedEntity]) -> None: ...
   def RemoveFilterEntities(self, filterId: str, entities: list[ManagedEntity]) -> None: ...
   def RemoveFilter(self, filterId: str) -> None: ...


class HistoricalInterval(DynamicData):
   key: int
   samplingPeriod: int
   name: str
   length: int
   level: Optional[int] = None
   enabled: bool


class HistoryCollector(ManagedObject):
   @property
   def filter(self) -> object: ...

   def SetLatestPageSize(self, maxCount: int) -> None: ...
   def Rewind(self) -> None: ...
   def Reset(self) -> None: ...
   def Remove(self) -> None: ...


class HostServiceTicket(DynamicData):
   host: Optional[str] = None
   port: Optional[int] = None
   sslThumbprint: Optional[str] = None
   sslCertificate: Optional[str] = None
   service: str
   serviceVersion: str
   sessionId: str


class HostSystem(ManagedEntity):
   class ConnectionState(Enum):
      connected: ClassVar['ConnectionState'] = 'connected'
      notResponding: ClassVar['ConnectionState'] = 'notResponding'
      disconnected: ClassVar['ConnectionState'] = 'disconnected'

   class PowerState(Enum):
      poweredOn: ClassVar['PowerState'] = 'poweredOn'
      poweredOff: ClassVar['PowerState'] = 'poweredOff'
      standBy: ClassVar['PowerState'] = 'standBy'
      unknown: ClassVar['PowerState'] = 'unknown'

   class StandbyMode(Enum):
      entering: ClassVar['StandbyMode'] = 'entering'
      exiting: ClassVar['StandbyMode'] = 'exiting'
      # Reserved python keyword: commenting out.
      # in: ClassVar['StandbyMode'] = 'in'
      none: ClassVar['StandbyMode'] = 'none'

   class CryptoState(Enum):
      incapable: ClassVar['CryptoState'] = 'incapable'
      prepared: ClassVar['CryptoState'] = 'prepared'
      safe: ClassVar['CryptoState'] = 'safe'
      pendingIncapable: ClassVar['CryptoState'] = 'pendingIncapable'

   class RemediationState(DynamicData):
      class State(Enum):
         remediationReady: ClassVar['State'] = 'remediationReady'
         precheckRemediationRunning: ClassVar['State'] = 'precheckRemediationRunning'
         precheckRemediationComplete: ClassVar['State'] = 'precheckRemediationComplete'
         precheckRemediationFailed: ClassVar['State'] = 'precheckRemediationFailed'
         remediationRunning: ClassVar['State'] = 'remediationRunning'
         remediationFailed: ClassVar['State'] = 'remediationFailed'

      state: str
      operationTime: datetime

   class ComplianceCheckState(DynamicData):
      state: str
      checkTime: datetime

   class ReconnectSpec(DynamicData):
      syncState: Optional[bool] = None

   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def hardware(self) -> Optional[HardwareInfo]: ...
   @property
   def capability(self) -> Optional[Capability]: ...
   @property
   def licensableResource(self) -> LicenseManager.LicensableResourceInfo: ...
   @property
   def remediationState(self) -> Optional[RemediationState]: ...
   @property
   def precheckRemediationResult(self) -> Optional[ProfileManager.ApplyHostConfigSpec]: ...
   @property
   def remediationResult(self) -> Optional[ProfileManager.ApplyHostConfigResult]: ...
   @property
   def complianceCheckState(self) -> Optional[ComplianceCheckState]: ...
   @property
   def complianceCheckResult(self) -> Optional[ComplianceResult]: ...
   @property
   def configManager(self) -> ConfigManager: ...
   @property
   def config(self) -> Optional[ConfigInfo]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def datastoreBrowser(self) -> DatastoreBrowser: ...
   @property
   def systemResources(self) -> Optional[SystemResourceInfo]: ...
   @property
   def answerFileValidationState(self) -> Optional[AnswerFileStatusResult]: ...
   @property
   def answerFileValidationResult(self) -> Optional[AnswerFileStatusResult]: ...

   def QueryTpmAttestationReport(self) -> Optional[TpmAttestationReport]: ...
   def QueryConnectionInfo(self) -> ConnectInfo: ...
   def UpdateSystemResources(self, resourceInfo: SystemResourceInfo) -> None: ...
   def UpdateSystemSwapConfiguration(self, sysSwapConfig: SystemSwapConfiguration) -> None: ...
   def Reconnect(self, cnxSpec: Optional[ConnectSpec], reconnectSpec: Optional[ReconnectSpec]) -> Task: ...
   def Disconnect(self) -> Task: ...
   def EnterMaintenanceMode(self, timeout: int, evacuatePoweredOffVms: Optional[bool], maintenanceSpec: Optional[MaintenanceSpec]) -> Task: ...
   def ExitMaintenanceMode(self, timeout: int) -> Task: ...
   def Reboot(self, force: bool) -> Task: ...
   def Shutdown(self, force: bool) -> Task: ...
   def EnterStandbyMode(self, timeoutSec: int, evacuatePoweredOffVms: Optional[bool]) -> Task: ...
   def ExitStandbyMode(self, timeoutSec: int) -> Task: ...
   def QueryOverhead(self, memorySize: long, videoRamSize: Optional[int], numVcpus: int) -> long: ...
   def QueryOverheadEx(self, vmConfigInfo: ConfigInfo) -> long: ...
   def ReconfigureDAS(self) -> Task: ...
   def UpdateFlags(self, flagInfo: FlagInfo) -> None: ...
   def EnterLockdownMode(self) -> None: ...
   def ExitLockdownMode(self) -> None: ...
   def AcquireCimServicesTicket(self) -> HostServiceTicket: ...
   def UpdateIpmi(self, ipmiInfo: IpmiInfo) -> None: ...
   def RetrieveHardwareUptime(self) -> long: ...
   def PrepareCrypto(self) -> None: ...
   def EnableCrypto(self, keyPlain: CryptoKeyPlain) -> None: ...
   def ConfigureCryptoKey(self, keyId: Optional[CryptoKeyId]) -> None: ...
   def QueryProductLockerLocation(self) -> str: ...
   def UpdateProductLockerLocation(self, path: str) -> Task: ...
   def RetrieveFreeEpcMemory(self) -> long: ...


class HttpNfcLease(ManagedObject):
   class State(Enum):
      initializing: ClassVar['State'] = 'initializing'
      ready: ClassVar['State'] = 'ready'
      done: ClassVar['State'] = 'done'
      error: ClassVar['State'] = 'error'

   class Mode(Enum):
      pushOrGet: ClassVar['Mode'] = 'pushOrGet'
      pull: ClassVar['Mode'] = 'pull'

   class DatastoreLeaseInfo(DynamicData):
      datastoreKey: str
      hosts: list[HostInfo] = []

   class HostInfo(DynamicData):
      url: str
      sslThumbprint: str

   class Info(DynamicData):
      lease: HttpNfcLease
      entity: ManagedEntity
      deviceUrl: list[DeviceUrl] = []
      totalDiskCapacityInKB: long
      leaseTimeout: int
      hostMap: list[DatastoreLeaseInfo] = []

   class DeviceUrl(DynamicData):
      key: str
      importKey: str
      url: str
      sslThumbprint: str
      sslCertificate: Optional[str] = None
      disk: Optional[bool] = None
      targetId: Optional[str] = None
      datastoreKey: Optional[str] = None
      fileSize: Optional[long] = None

   class ManifestEntry(DynamicData):
      class ChecksumType(Enum):
         sha1: ClassVar['ChecksumType'] = 'sha1'
         sha256: ClassVar['ChecksumType'] = 'sha256'

      key: str
      sha1: str
      checksum: Optional[str] = None
      checksumType: Optional[str] = None
      size: long
      disk: bool
      capacity: Optional[long] = None
      populatedSize: Optional[long] = None

   class SourceFile(DynamicData):
      targetDeviceId: str
      url: str
      memberName: Optional[str] = None
      create: bool
      sslThumbprint: Optional[str] = None
      sslCertificate: Optional[str] = None
      httpHeaders: list[KeyValue] = []
      size: Optional[long] = None

   class Capabilities(DynamicData):
      pullModeSupported: bool
      corsSupported: bool

   class ProbeResult(DynamicData):
      serverAccessible: bool

   @property
   def initializeProgress(self) -> int: ...
   @property
   def transferProgress(self) -> int: ...
   @property
   def mode(self) -> str: ...
   @property
   def capabilities(self) -> Capabilities: ...
   @property
   def info(self) -> Optional[Info]: ...
   @property
   def state(self) -> State: ...
   @property
   def error(self) -> Optional[MethodFault]: ...

   def GetManifest(self) -> list[ManifestEntry]: ...
   def SetManifestChecksumType(self, deviceUrlsToChecksumTypes: list[KeyValue]) -> None: ...
   def Complete(self) -> None: ...
   def Abort(self, fault: Optional[MethodFault]) -> None: ...
   def Progress(self, percent: int) -> None: ...
   def PullFromUrls(self, files: list[SourceFile]) -> Task: ...
   def ProbeUrls(self, files: list[SourceFile], timeout: Optional[int]) -> list[ProbeResult]: ...


class ImportSpec(DynamicData):
   entityConfig: Optional[EntityConfigInfo] = None
   instantiationOst: Optional[OvfConsumer.OstNode] = None


class InheritablePolicy(DynamicData):
   inherited: bool


class IntExpression(NegatableExpression):
   value: Optional[int] = None


class IntPolicy(InheritablePolicy):
   value: Optional[int] = None


class IoFilterManager(ManagedObject):
   class IoFilterInfo(DynamicData):
      id: str
      name: str
      vendor: str
      version: str
      type: Optional[str] = None
      summary: Optional[str] = None
      releaseDate: Optional[str] = None

   class HostIoFilterInfo(IoFilterInfo):
      available: bool

   class OperationType(Enum):
      install: ClassVar['OperationType'] = 'install'
      uninstall: ClassVar['OperationType'] = 'uninstall'
      upgrade: ClassVar['OperationType'] = 'upgrade'

   class ClusterIoFilterInfo(IoFilterInfo):
      opType: str
      vibUrl: Optional[str] = None

   class IoFilterType(Enum):
      cache: ClassVar['IoFilterType'] = 'cache'
      replication: ClassVar['IoFilterType'] = 'replication'
      encryption: ClassVar['IoFilterType'] = 'encryption'
      compression: ClassVar['IoFilterType'] = 'compression'
      inspection: ClassVar['IoFilterType'] = 'inspection'
      datastoreIoControl: ClassVar['IoFilterType'] = 'datastoreIoControl'
      dataProvider: ClassVar['IoFilterType'] = 'dataProvider'
      dataCapture: ClassVar['IoFilterType'] = 'dataCapture'

   class SslTrust(DynamicData):
      pass

   class PinnedCertificate(SslTrust):
      sslCertificate: str

   class UntrustedCertificate(SslTrust):
      pass

   class QueryIssueResult(DynamicData):
      class HostIssue(DynamicData):
         host: HostSystem
         issue: list[MethodFault] = []

      opType: str
      hostIssue: list[HostIssue] = []

   def InstallIoFilter(self, vibUrl: str, compRes: ComputeResource, vibSslTrust: Optional[SslTrust]) -> Task: ...
   def UninstallIoFilter(self, filterId: str, compRes: ComputeResource) -> Task: ...
   def UpgradeIoFilter(self, filterId: str, compRes: ComputeResource, vibUrl: str, vibSslTrust: Optional[SslTrust]) -> Task: ...
   def QueryIssue(self, filterId: str, compRes: ComputeResource) -> QueryIssueResult: ...
   def QueryIoFilterInfo(self, compRes: ComputeResource) -> list[ClusterIoFilterInfo]: ...
   def ResolveInstallationErrorsOnHost(self, filterId: str, host: HostSystem) -> Task: ...
   def ResolveInstallationErrorsOnCluster(self, filterId: str, cluster: ClusterComputeResource) -> Task: ...
   def QueryDisksUsingFilter(self, filterId: str, compRes: ComputeResource) -> list[VirtualDiskId]: ...
   def InitiateTransitionToVLCM(self, cluster: ClusterComputeResource) -> Task: ...

class IpAddress(NegatableExpression):
   pass


class IpPoolManager(ManagedObject):
   class IpAllocation(DynamicData):
      ipAddress: str
      allocationId: str

   def QueryIpPools(self, dc: Datacenter) -> list[IpPool]: ...
   def CreateIpPool(self, dc: Datacenter, pool: IpPool) -> int: ...
   def UpdateIpPool(self, dc: Datacenter, pool: IpPool) -> None: ...
   def DestroyIpPool(self, dc: Datacenter, id: int, force: bool) -> None: ...
   def AllocateIpv4Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
   def AllocateIpv6Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
   def ReleaseIpAllocation(self, dc: Datacenter, poolId: int, allocationId: str) -> None: ...
   def QueryIPAllocations(self, dc: Datacenter, poolId: int, extensionKey: str) -> list[IpAllocation]: ...


class IpRange(IpAddress):
   addressPrefix: str
   prefixLength: Optional[int] = None


class KeyValue(DynamicData):
   key: str
   value: str


class LatencySensitivity(DynamicData):
   class SensitivityLevel(Enum):
      low: ClassVar['SensitivityLevel'] = 'low'
      normal: ClassVar['SensitivityLevel'] = 'normal'
      medium: ClassVar['SensitivityLevel'] = 'medium'
      high: ClassVar['SensitivityLevel'] = 'high'
      custom: ClassVar['SensitivityLevel'] = 'custom'

   level: SensitivityLevel
   sensitivity: Optional[int] = None


class LicenseAssignmentManager(ManagedObject):
   class LicenseAssignment(DynamicData):
      entityId: str
      scope: Optional[str] = None
      entityDisplayName: Optional[str] = None
      assignedLicense: LicenseManager.LicenseInfo
      properties: list[KeyAnyValue] = []

   def UpdateAssignedLicense(self, entity: str, licenseKey: str, entityDisplayName: Optional[str]) -> LicenseManager.LicenseInfo: ...
   def RemoveAssignedLicense(self, entityId: str) -> None: ...
   def QueryAssignedLicenses(self, entityId: Optional[str]) -> list[LicenseAssignment]: ...


class LicenseManager(ManagedObject):
   class LicenseState(Enum):
      initializing: ClassVar['LicenseState'] = 'initializing'
      normal: ClassVar['LicenseState'] = 'normal'
      marginal: ClassVar['LicenseState'] = 'marginal'
      fault: ClassVar['LicenseState'] = 'fault'

   class LicenseKey(Enum):
      esxFull: ClassVar['LicenseKey'] = 'esxFull'
      esxVmtn: ClassVar['LicenseKey'] = 'esxVmtn'
      esxExpress: ClassVar['LicenseKey'] = 'esxExpress'
      san: ClassVar['LicenseKey'] = 'san'
      iscsi: ClassVar['LicenseKey'] = 'iscsi'
      nas: ClassVar['LicenseKey'] = 'nas'
      vsmp: ClassVar['LicenseKey'] = 'vsmp'
      backup: ClassVar['LicenseKey'] = 'backup'
      vc: ClassVar['LicenseKey'] = 'vc'
      vcExpress: ClassVar['LicenseKey'] = 'vcExpress'
      esxHost: ClassVar['LicenseKey'] = 'esxHost'
      gsxHost: ClassVar['LicenseKey'] = 'gsxHost'
      serverHost: ClassVar['LicenseKey'] = 'serverHost'
      drsPower: ClassVar['LicenseKey'] = 'drsPower'
      vmotion: ClassVar['LicenseKey'] = 'vmotion'
      drs: ClassVar['LicenseKey'] = 'drs'
      das: ClassVar['LicenseKey'] = 'das'

   class LicenseSource(DynamicData):
      pass

   class LicenseServer(LicenseSource):
      licenseServer: str

   class LocalLicense(LicenseSource):
      licenseKeys: str

   class EvaluationLicense(LicenseSource):
      remainingHours: Optional[long] = None

   class FeatureInfo(DynamicData):
      class CostUnit(Enum):
         host: ClassVar['CostUnit'] = 'host'
         cpuCore: ClassVar['CostUnit'] = 'cpuCore'
         cpuPackage: ClassVar['CostUnit'] = 'cpuPackage'
         server: ClassVar['CostUnit'] = 'server'
         vm: ClassVar['CostUnit'] = 'vm'

      class State(Enum):
         enabled: ClassVar['State'] = 'enabled'
         disabled: ClassVar['State'] = 'disabled'
         optional: ClassVar['State'] = 'optional'

      class SourceRestriction(Enum):
         unrestricted: ClassVar['SourceRestriction'] = 'unrestricted'
         served: ClassVar['SourceRestriction'] = 'served'
         file: ClassVar['SourceRestriction'] = 'file'

      key: str
      featureName: str
      featureDescription: Optional[str] = None
      state: Optional[State] = None
      costUnit: str
      sourceRestriction: Optional[str] = None
      dependentKey: list[str] = []
      edition: Optional[bool] = None
      expiresOn: Optional[datetime] = None

   class ReservationInfo(DynamicData):
      class State(Enum):
         notUsed: ClassVar['State'] = 'notUsed'
         noLicense: ClassVar['State'] = 'noLicense'
         unlicensedUse: ClassVar['State'] = 'unlicensedUse'
         licensed: ClassVar['State'] = 'licensed'

      key: str
      state: State
      required: int

   class AvailabilityInfo(DynamicData):
      feature: FeatureInfo
      total: int
      available: int

   class DiagnosticInfo(DynamicData):
      sourceLastChanged: datetime
      sourceLost: str
      sourceLatency: float
      licenseRequests: str
      licenseRequestFailures: str
      licenseFeatureUnknowns: str
      opState: LicenseState
      lastStatusUpdate: datetime
      opFailureMessage: str

   class LicenseUsageInfo(DynamicData):
      source: LicenseSource
      sourceAvailable: bool
      reservationInfo: list[ReservationInfo] = []
      featureInfo: list[FeatureInfo] = []

   class EvaluationInfo(DynamicData):
      properties: list[KeyAnyValue] = []

   class LicensableResourceInfo(DynamicData):
      class ResourceKey(Enum):
         numCpuPackages: ClassVar['ResourceKey'] = 'numCpuPackages'
         numCpuCores: ClassVar['ResourceKey'] = 'numCpuCores'
         memorySize: ClassVar['ResourceKey'] = 'memorySize'
         memoryForVms: ClassVar['ResourceKey'] = 'memoryForVms'
         numVmsStarted: ClassVar['ResourceKey'] = 'numVmsStarted'
         numVmsStarting: ClassVar['ResourceKey'] = 'numVmsStarting'
         vsanCapacity: ClassVar['ResourceKey'] = 'vsanCapacity'

      resource: list[KeyAnyValue] = []

   class LicenseInfo(DynamicData):
      licenseKey: str
      editionKey: str
      name: str
      total: int
      used: Optional[int] = None
      costUnit: str
      properties: list[KeyAnyValue] = []
      labels: list[KeyValue] = []

   @property
   def source(self) -> LicenseSource: ...
   @property
   def sourceAvailable(self) -> bool: ...
   @property
   def diagnostics(self) -> Optional[DiagnosticInfo]: ...
   @property
   def featureInfo(self) -> list[FeatureInfo]: ...
   @property
   def licensedEdition(self) -> str: ...
   @property
   def licenses(self) -> list[LicenseInfo]: ...
   @property
   def licenseAssignmentManager(self) -> Optional[LicenseAssignmentManager]: ...
   @property
   def evaluation(self) -> EvaluationInfo: ...

   def QuerySupportedFeatures(self, host: Optional[HostSystem]) -> list[FeatureInfo]: ...
   def QuerySourceAvailability(self, host: Optional[HostSystem]) -> list[AvailabilityInfo]: ...
   def QueryUsage(self, host: Optional[HostSystem]) -> LicenseUsageInfo: ...
   def SetEdition(self, host: Optional[HostSystem], featureKey: Optional[str]) -> None: ...
   def CheckFeature(self, host: Optional[HostSystem], featureKey: str) -> bool: ...
   def Enable(self, host: Optional[HostSystem], featureKey: str) -> bool: ...
   def Disable(self, host: Optional[HostSystem], featureKey: str) -> bool: ...
   def ConfigureSource(self, host: Optional[HostSystem], licenseSource: LicenseSource) -> None: ...
   def UpdateLicense(self, licenseKey: str, labels: list[KeyValue]) -> LicenseInfo: ...
   def AddLicense(self, licenseKey: str, labels: list[KeyValue]) -> LicenseInfo: ...
   def RemoveLicense(self, licenseKey: str) -> None: ...
   def DecodeLicense(self, licenseKey: str) -> LicenseInfo: ...
   def UpdateLabel(self, licenseKey: str, labelKey: str, labelValue: str) -> None: ...
   def RemoveLabel(self, licenseKey: str, labelKey: str) -> None: ...


class LocalizationManager(ManagedObject):
   class MessageCatalog(DynamicData):
      moduleName: str
      catalogName: str
      locale: str
      catalogUri: str
      lastModified: Optional[datetime] = None
      md5sum: Optional[str] = None
      version: Optional[str] = None

   @property
   def catalog(self) -> list[MessageCatalog]: ...


class LongPolicy(InheritablePolicy):
   value: Optional[long] = None

class MacAddress(NegatableExpression):
   pass

class MacRange(MacAddress):
   address: str
   mask: str


class ManagedEntity(ExtensibleManagedObject):
   class Status(Enum):
      gray: ClassVar['Status'] = 'gray'
      green: ClassVar['Status'] = 'green'
      yellow: ClassVar['Status'] = 'yellow'
      red: ClassVar['Status'] = 'red'

   @property
   def parent(self) -> Optional[ManagedEntity]: ...
   @property
   def customValue(self) -> list[CustomFieldsManager.Value]: ...
   @property
   def overallStatus(self) -> Status: ...
   @property
   def configStatus(self) -> Status: ...
   @property
   def configIssue(self) -> list[Event]: ...
   @property
   def effectiveRole(self) -> list[int]: ...
   @property
   def permission(self) -> list[AuthorizationManager.Permission]: ...
   @property
   def name(self) -> str: ...
   @property
   def disabledMethod(self) -> list[ManagedMethod]: ...
   @property
   def recentTask(self) -> list[Task]: ...
   @property
   def declaredAlarmState(self) -> list[AlarmState]: ...
   @property
   def triggeredAlarmState(self) -> list[AlarmState]: ...
   @property
   def alarmActionsEnabled(self) -> Optional[bool]: ...
   @property
   def tag(self) -> list[Tag]: ...

   def Reload(self) -> None: ...
   def Rename(self, newName: str) -> Task: ...
   def Destroy(self) -> Task: ...


class MethodDescription(Description):
   key: ManagedMethod


class NegatableExpression(DynamicData):
   negate: Optional[bool] = None


class Network(ManagedEntity):
   class Summary(DynamicData):
      network: Optional[Network] = None
      name: str
      accessible: bool
      ipPoolName: str
      ipPoolId: Optional[int] = None

   @property
   def summary(self) -> Summary: ...
   @property
   def host(self) -> list[HostSystem]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...

   def DestroyNetwork(self) -> None: ...


class NumericRange(DynamicData):
   start: int
   end: int


class OpaqueNetwork(Network):
   class Summary(Network.Summary):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class Capability(DynamicData):
      networkReservationSupported: bool

   @property
   def capability(self) -> Optional[Capability]: ...
   @property
   def extraConfig(self) -> list[OptionValue]: ...


class OverheadMemoryManager(ManagedObject):
   def LookupVmOverheadMemory(self, vm: VirtualMachine, host: HostSystem) -> long: ...


class OvfManager(ManagedObject):
   class OvfOptionInfo(DynamicData):
      option: str
      description: LocalizableMessage

   class DeploymentOption(DynamicData):
      key: str
      label: str
      description: str

   class CommonParams(DynamicData):
      locale: str
      deploymentOption: str
      msgBundle: list[KeyValue] = []
      importOption: list[str] = []

   class ValidateHostParams(CommonParams):
      pass

   class ValidateHostResult(DynamicData):
      downloadSize: Optional[long] = None
      flatDeploymentSize: Optional[long] = None
      sparseDeploymentSize: Optional[long] = None
      error: list[MethodFault] = []
      warning: list[MethodFault] = []
      supportedDiskProvisioning: list[str] = []

   class ParseDescriptorParams(CommonParams):
      pass

   class ParseDescriptorResult(DynamicData):
      eula: list[str] = []
      network: list[NetworkInfo] = []
      ipAllocationScheme: list[str] = []
      ipProtocols: list[str] = []
      property: list[PropertyInfo] = []
      productInfo: Optional[ProductInfo] = None
      annotation: str
      approximateDownloadSize: Optional[long] = None
      approximateFlatDeploymentSize: Optional[long] = None
      approximateSparseDeploymentSize: Optional[long] = None
      defaultEntityName: str
      virtualApp: bool
      deploymentOption: list[DeploymentOption] = []
      defaultDeploymentOption: str
      entityName: list[KeyValue] = []
      annotatedOst: Optional[OvfConsumer.OstNode] = None
      error: list[MethodFault] = []
      warning: list[MethodFault] = []

   class NetworkInfo(DynamicData):
      name: str
      description: str

   class CreateImportSpecParams(CommonParams):
      class DiskProvisioningType(Enum):
         monolithicSparse: ClassVar['DiskProvisioningType'] = 'monolithicSparse'
         monolithicFlat: ClassVar['DiskProvisioningType'] = 'monolithicFlat'
         twoGbMaxExtentSparse: ClassVar['DiskProvisioningType'] = 'twoGbMaxExtentSparse'
         twoGbMaxExtentFlat: ClassVar['DiskProvisioningType'] = 'twoGbMaxExtentFlat'
         thin: ClassVar['DiskProvisioningType'] = 'thin'
         thick: ClassVar['DiskProvisioningType'] = 'thick'
         seSparse: ClassVar['DiskProvisioningType'] = 'seSparse'
         eagerZeroedThick: ClassVar['DiskProvisioningType'] = 'eagerZeroedThick'
         sparse: ClassVar['DiskProvisioningType'] = 'sparse'
         flat: ClassVar['DiskProvisioningType'] = 'flat'

      entityName: str
      hostSystem: Optional[HostSystem] = None
      networkMapping: list[NetworkMapping] = []
      ipAllocationPolicy: Optional[str] = None
      ipProtocol: Optional[str] = None
      propertyMapping: list[KeyValue] = []
      resourceMapping: list[ResourceMap] = []
      diskProvisioning: Optional[str] = None
      instantiationOst: Optional[OvfConsumer.OstNode] = None

   class ResourceMap(DynamicData):
      source: str
      parent: Optional[ResourcePool] = None
      resourceSpec: Optional[ResourceConfigSpec] = None
      datastore: Optional[Datastore] = None

   class NetworkMapping(DynamicData):
      name: str
      network: Network

   class DatastoreMapping(DynamicData):
      diskId: str
      datastore: Datastore

   class StorageProfileMapping(DynamicData):
      diskId: str
      storageProfileId: str

   class CreateImportSpecResult(DynamicData):
      importSpec: Optional[ImportSpec] = None
      fileItem: list[FileItem] = []
      warning: list[MethodFault] = []
      error: list[MethodFault] = []

   class FileItem(DynamicData):
      deviceId: str
      path: str
      compressionMethod: Optional[str] = None
      chunkSize: Optional[long] = None
      size: Optional[long] = None
      cimType: int
      create: bool

   class CreateDescriptorParams(DynamicData):
      ovfFiles: list[OvfFile] = []
      name: Optional[str] = None
      description: Optional[str] = None
      includeImageFiles: Optional[bool] = None
      exportOption: list[str] = []
      snapshot: Optional[Snapshot] = None

   class CreateDescriptorResult(DynamicData):
      ovfDescriptor: str
      error: list[MethodFault] = []
      warning: list[MethodFault] = []
      includeImageFiles: Optional[bool] = None

   class OvfFile(DynamicData):
      deviceId: str
      path: str
      compressionMethod: Optional[str] = None
      chunkSize: Optional[long] = None
      size: long
      capacity: Optional[long] = None
      populatedSize: Optional[long] = None

   class OvfImportParams(CreateImportSpecParams):
      pushMode: Optional[bool] = None
      signatureRequired: Optional[bool] = None
      skipManifestCheck: Optional[bool] = None
      powerOn: Optional[bool] = None
      customHttpHeaders: list[KeyValue] = []
      sourceCertificate: Optional[str] = None
      datastoreMappings: list[DatastoreMapping] = []
      vmProfile: Optional[str] = None
      diskProfiles: list[StorageProfileMapping] = []

   @property
   def ovfImportOption(self) -> list[OvfOptionInfo]: ...
   @property
   def ovfExportOption(self) -> list[OvfOptionInfo]: ...

   def ValidateHost(self, ovfDescriptor: str, host: HostSystem, vhp: ValidateHostParams) -> ValidateHostResult: ...
   def ParseDescriptor(self, ovfDescriptor: str, pdp: ParseDescriptorParams) -> ParseDescriptorResult: ...
   def CreateImportSpec(self, ovfDescriptor: str, resourcePool: ResourcePool, datastore: Datastore, cisp: CreateImportSpecParams) -> CreateImportSpecResult: ...
   def CreateDescriptor(self, obj: ManagedEntity, cdp: CreateDescriptorParams) -> CreateDescriptorResult: ...


class PasswordField(DynamicData):
   value: str


class PerformanceDescription(DynamicData):
   counterType: list[ElementDescription] = []
   statsType: list[ElementDescription] = []


class PerformanceManager(ManagedObject):
   class Format(Enum):
      normal: ClassVar['Format'] = 'normal'
      csv: ClassVar['Format'] = 'csv'

   class ProviderSummary(DynamicData):
      entity: ManagedObject
      currentSupported: bool
      summarySupported: bool
      refreshRate: Optional[int] = None

   class CounterInfo(DynamicData):
      class RollupType(Enum):
         average: ClassVar['RollupType'] = 'average'
         maximum: ClassVar['RollupType'] = 'maximum'
         minimum: ClassVar['RollupType'] = 'minimum'
         latest: ClassVar['RollupType'] = 'latest'
         summation: ClassVar['RollupType'] = 'summation'
         none: ClassVar['RollupType'] = 'none'

      class StatsType(Enum):
         absolute: ClassVar['StatsType'] = 'absolute'
         delta: ClassVar['StatsType'] = 'delta'
         rate: ClassVar['StatsType'] = 'rate'

      class Unit(Enum):
         percent: ClassVar['Unit'] = 'percent'
         kiloBytes: ClassVar['Unit'] = 'kiloBytes'
         megaBytes: ClassVar['Unit'] = 'megaBytes'
         gigaBytes: ClassVar['Unit'] = 'gigaBytes'
         megaHertz: ClassVar['Unit'] = 'megaHertz'
         number: ClassVar['Unit'] = 'number'
         microsecond: ClassVar['Unit'] = 'microsecond'
         millisecond: ClassVar['Unit'] = 'millisecond'
         second: ClassVar['Unit'] = 'second'
         kiloBytesPerSecond: ClassVar['Unit'] = 'kiloBytesPerSecond'
         megaBytesPerSecond: ClassVar['Unit'] = 'megaBytesPerSecond'
         watt: ClassVar['Unit'] = 'watt'
         joule: ClassVar['Unit'] = 'joule'
         teraBytes: ClassVar['Unit'] = 'teraBytes'
         celsius: ClassVar['Unit'] = 'celsius'
         nanosecond: ClassVar['Unit'] = 'nanosecond'

      key: int
      nameInfo: ElementDescription
      groupInfo: ElementDescription
      unitInfo: ElementDescription
      rollupType: RollupType
      statsType: StatsType
      level: Optional[int] = None
      perDeviceLevel: Optional[int] = None
      associatedCounterId: list[int] = []

   class MetricId(DynamicData):
      counterId: int
      instance: str

   class QuerySpec(DynamicData):
      entity: ManagedObject
      startTime: Optional[datetime] = None
      endTime: Optional[datetime] = None
      maxSample: Optional[int] = None
      metricId: list[MetricId] = []
      intervalId: Optional[int] = None
      format: Optional[str] = None

   class SampleInfo(DynamicData):
      timestamp: datetime
      interval: int

   class MetricSeries(DynamicData):
      id: MetricId

   class IntSeries(MetricSeries):
      value: list[long] = []

   class MetricSeriesCSV(MetricSeries):
      value: Optional[str] = None

   class EntityMetricBase(DynamicData):
      entity: ManagedObject

   class EntityMetric(EntityMetricBase):
      sampleInfo: list[SampleInfo] = []
      value: list[MetricSeries] = []

   class EntityMetricCSV(EntityMetricBase):
      sampleInfoCSV: str
      value: list[MetricSeriesCSV] = []

   class CompositeEntityMetric(DynamicData):
      entity: Optional[EntityMetricBase] = None
      childEntity: list[EntityMetricBase] = []

   class CounterLevelMapping(DynamicData):
      counterId: int
      aggregateLevel: Optional[int] = None
      perDeviceLevel: Optional[int] = None

   @property
   def description(self) -> PerformanceDescription: ...
   @property
   def historicalInterval(self) -> list[HistoricalInterval]: ...
   @property
   def perfCounter(self) -> list[CounterInfo]: ...

   def QueryProviderSummary(self, entity: ManagedObject) -> ProviderSummary: ...
   def QueryAvailableMetric(self, entity: ManagedObject, beginTime: Optional[datetime], endTime: Optional[datetime], intervalId: Optional[int]) -> list[MetricId]: ...
   def QueryCounter(self, counterId: list[int]) -> list[CounterInfo]: ...
   def QueryCounterByLevel(self, level: int) -> list[CounterInfo]: ...
   def QueryStats(self, querySpec: list[QuerySpec]) -> list[EntityMetricBase]: ...
   def QueryCompositeStats(self, querySpec: QuerySpec) -> CompositeEntityMetric: ...
   def CreateHistoricalInterval(self, intervalId: HistoricalInterval) -> None: ...
   def RemoveHistoricalInterval(self, samplePeriod: int) -> None: ...
   def UpdateHistoricalInterval(self, interval: HistoricalInterval) -> None: ...
   def UpdateCounterLevelMapping(self, counterLevelMap: list[CounterLevelMapping]) -> None: ...
   def ResetCounterLevelMapping(self, counters: list[int]) -> None: ...


class PosixUserSearchResult(UserSearchResult):
   id: int
   shellAccess: Optional[bool] = None
   lastPasswordChange: Optional[long] = None
   maximumPasswordAge: Optional[long] = None


class PrivilegePolicyDef(DynamicData):
   createPrivilege: str
   readPrivilege: str
   updatePrivilege: str
   deletePrivilege: str


class ResourceAllocationInfo(DynamicData):
   reservation: Optional[long] = None
   expandableReservation: Optional[bool] = None
   limit: Optional[long] = None
   shares: Optional[SharesInfo] = None
   overheadLimit: Optional[long] = None


class ResourceAllocationOption(DynamicData):
   sharesOption: SharesOption


class ResourceConfigOption(DynamicData):
   cpuAllocationOption: ResourceAllocationOption
   memoryAllocationOption: ResourceAllocationOption


class ResourceConfigSpec(DynamicData):
   class ScaleSharesBehavior(Enum):
      disabled: ClassVar['ScaleSharesBehavior'] = 'disabled'
      scaleCpuAndMemoryShares: ClassVar['ScaleSharesBehavior'] = 'scaleCpuAndMemoryShares'

   entity: Optional[ManagedEntity] = None
   changeVersion: Optional[str] = None
   lastModified: Optional[datetime] = None
   cpuAllocation: ResourceAllocationInfo
   memoryAllocation: ResourceAllocationInfo
   scaleDescendantsShares: Optional[str] = None


class ResourcePlanningManager(ManagedObject):
   class DatabaseSizeParam(DynamicData):
      inventoryDesc: InventoryDescription
      perfStatsDesc: Optional[PerfStatsDescription] = None

   class InventoryDescription(DynamicData):
      numHosts: int
      numVirtualMachines: int
      numResourcePools: Optional[int] = None
      numClusters: Optional[int] = None
      numCpuDev: Optional[int] = None
      numNetDev: Optional[int] = None
      numDiskDev: Optional[int] = None
      numvCpuDev: Optional[int] = None
      numvNetDev: Optional[int] = None
      numvDiskDev: Optional[int] = None

   class PerfStatsDescription(DynamicData):
      intervals: list[HistoricalInterval] = []

   class DatabaseSizeEstimate(DynamicData):
      size: long

   def EstimateDatabaseSize(self, dbSizeParam: DatabaseSizeParam) -> DatabaseSizeEstimate: ...


class ResourcePool(ManagedEntity):
   class ResourceUsage(DynamicData):
      reservationUsed: long
      reservationUsedForVm: long
      unreservedForPool: long
      unreservedForVm: long
      overallUsage: long
      maxUsage: long

   class RuntimeInfo(DynamicData):
      memory: ResourceUsage
      cpu: ResourceUsage
      overallStatus: ManagedEntity.Status
      sharesScalable: Optional[str] = None

   class Summary(DynamicData):
      class QuickStats(DynamicData):
         overallCpuUsage: Optional[long] = None
         overallCpuDemand: Optional[long] = None
         guestMemoryUsage: Optional[long] = None
         hostMemoryUsage: Optional[long] = None
         distributedCpuEntitlement: Optional[long] = None
         distributedMemoryEntitlement: Optional[long] = None
         staticCpuEntitlement: Optional[int] = None
         staticMemoryEntitlement: Optional[int] = None
         privateMemory: Optional[long] = None
         sharedMemory: Optional[long] = None
         swappedMemory: Optional[long] = None
         balloonedMemory: Optional[long] = None
         overheadMemory: Optional[long] = None
         consumedOverheadMemory: Optional[long] = None
         compressedMemory: Optional[long] = None

      name: str
      config: ResourceConfigSpec
      runtime: RuntimeInfo
      quickStats: Optional[QuickStats] = None
      configuredMemoryMB: Optional[int] = None

   @property
   def summary(self) -> Summary: ...
   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def owner(self) -> ComputeResource: ...
   @property
   def resourcePool(self) -> list[ResourcePool]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def config(self) -> ResourceConfigSpec: ...
   @property
   def namespace(self) -> Optional[str]: ...
   @property
   def childConfiguration(self) -> list[ResourceConfigSpec]: ...

   def UpdateConfig(self, name: Optional[str], config: Optional[ResourceConfigSpec]) -> None: ...
   def MoveInto(self, list: list[ManagedEntity]) -> None: ...
   def UpdateChildResourceConfiguration(self, spec: list[ResourceConfigSpec]) -> None: ...
   def CreateResourcePool(self, name: str, spec: ResourceConfigSpec) -> ResourcePool: ...
   def DestroyChildren(self) -> None: ...
   def CreateVApp(self, name: str, resSpec: ResourceConfigSpec, configSpec: VAppConfigSpec, vmFolder: Optional[Folder]) -> VirtualApp: ...
   def CreateVm(self, config: ConfigSpec, host: Optional[HostSystem]) -> Task: ...
   def RegisterVm(self, path: str, name: Optional[str], host: Optional[HostSystem]) -> Task: ...
   def ImportVApp(self, spec: ImportSpec, folder: Optional[Folder], host: Optional[HostSystem]) -> HttpNfcLease: ...
   def QueryResourceConfigOption(self) -> ResourceConfigOption: ...
   def RefreshRuntime(self) -> None: ...


class SDDCBase(DynamicData):
   pass


class SearchIndex(ManagedObject):
   class QuerySpec(DynamicData):
      class ResourceType(Enum):
         ClusterComputeResource: ClassVar['ResourceType'] = 'ClusterComputeResource'
         ComputeResource: ClassVar['ResourceType'] = 'ComputeResource'
         Datacenter: ClassVar['ResourceType'] = 'Datacenter'
         Datastore: ClassVar['ResourceType'] = 'Datastore'
         DistributedVirtualPortgroup: ClassVar['ResourceType'] = 'DistributedVirtualPortgroup'
         DistributedVirtualSwitch: ClassVar['ResourceType'] = 'DistributedVirtualSwitch'
         Folder: ClassVar['ResourceType'] = 'Folder'
         HostSystem: ClassVar['ResourceType'] = 'HostSystem'
         Network: ClassVar['ResourceType'] = 'Network'
         OpaqueNetwork: ClassVar['ResourceType'] = 'OpaqueNetwork'
         ResourcePool: ClassVar['ResourceType'] = 'ResourcePool'
         ServiceInstance: ClassVar['ResourceType'] = 'ServiceInstance'
         StoragePod: ClassVar['ResourceType'] = 'StoragePod'
         VirtualApp: ClassVar['ResourceType'] = 'VirtualApp'
         VirtualMachine: ClassVar['ResourceType'] = 'VirtualMachine'
         VmwareDistributedVirtualSwitch: ClassVar['ResourceType'] = 'VmwareDistributedVirtualSwitch'

      properties: list[str] = []
      resourceType: str
      filters: list[Filter] = []
      returnTotalCount: Optional[bool] = None
      limit: Optional[int] = None

   class IterationSpec(DynamicData):
      marker: Optional[str] = None
      limit: Optional[int] = None

   class Filter(DynamicData):
      predicates: list[Predicate] = []

   class Predicate(DynamicData):
      class ComparisonOperator(Enum):
         Equal: ClassVar['ComparisonOperator'] = 'Equal'
         NotEqual: ClassVar['ComparisonOperator'] = 'NotEqual'
         Greater: ClassVar['ComparisonOperator'] = 'Greater'
         GreaterOrEqual: ClassVar['ComparisonOperator'] = 'GreaterOrEqual'
         Less: ClassVar['ComparisonOperator'] = 'Less'
         LessOrEqual: ClassVar['ComparisonOperator'] = 'LessOrEqual'
         In: ClassVar['ComparisonOperator'] = 'In'
         NotIn: ClassVar['ComparisonOperator'] = 'NotIn'
         Like: ClassVar['ComparisonOperator'] = 'Like'
         NotLike: ClassVar['ComparisonOperator'] = 'NotLike'

      class ArrayOperator(Enum):
         AllElements: ClassVar['ArrayOperator'] = 'AllElements'
         AnyElement: ClassVar['ArrayOperator'] = 'AnyElement'

      propertyPath: str
      operator: str
      arrayOperator: Optional[str] = None
      comparableValue: Optional[object] = None
      comparableList: list[object] = []

   class ResultSet(DynamicData):
      properties: list[str] = []
      items: list[ResourceItem] = []
      totalCount: Optional[int] = None
      marker: Optional[str] = None

   class ResourceItem(DynamicData):
      propertyValues: list[OptionalValue] = []

   class OptionalValue(DynamicData):
      value: Optional[object] = None

   def FindByUuid(self, datacenter: Optional[Datacenter], uuid: str, vmSearch: bool, instanceUuid: Optional[bool]) -> Optional[ManagedEntity]: ...
   def FindByDatastorePath(self, datacenter: Datacenter, path: str) -> Optional[VirtualMachine]: ...
   def FindByDnsName(self, datacenter: Optional[Datacenter], dnsName: str, vmSearch: bool) -> Optional[ManagedEntity]: ...
   def FindByIp(self, datacenter: Optional[Datacenter], ip: str, vmSearch: bool) -> Optional[ManagedEntity]: ...
   def FindByInventoryPath(self, inventoryPath: str) -> Optional[ManagedEntity]: ...
   def FindChild(self, entity: ManagedEntity, name: str) -> Optional[ManagedEntity]: ...
   def FindAllByUuid(self, datacenter: Optional[Datacenter], uuid: str, vmSearch: bool, instanceUuid: Optional[bool]) -> list[ManagedEntity]: ...
   def FindAllByDnsName(self, datacenter: Optional[Datacenter], dnsName: str, vmSearch: bool) -> list[ManagedEntity]: ...
   def FindAllByIp(self, datacenter: Optional[Datacenter], ip: str, vmSearch: bool) -> list[ManagedEntity]: ...
   def Query(self, querySpec: QuerySpec) -> ResultSet: ...
   def QueryNext(self, iterationSpec: IterationSpec) -> ResultSet: ...


class SelectionSet(DynamicData):
   pass


class ServiceInstance(ManagedObject):
   class ValidateMigrationTestType(Enum):
      sourceTests: ClassVar['ValidateMigrationTestType'] = 'sourceTests'
      compatibilityTests: ClassVar['ValidateMigrationTestType'] = 'compatibilityTests'
      diskAccessibilityTests: ClassVar['ValidateMigrationTestType'] = 'diskAccessibilityTests'
      resourceTests: ClassVar['ValidateMigrationTestType'] = 'resourceTests'

   class VMotionCompatibilityType(Enum):
      cpu: ClassVar['VMotionCompatibilityType'] = 'cpu'
      software: ClassVar['VMotionCompatibilityType'] = 'software'

   class HostVMotionCompatibility(DynamicData):
      host: HostSystem
      compatibility: list[str] = []

   class ProductComponentInfo(DynamicData):
      id: str
      name: str
      version: str
      release: int

   @property
   def serverClock(self) -> datetime: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def content(self) -> ServiceInstanceContent: ...

   def CurrentTime(self) -> datetime: ...
   def RetrieveContent(self) -> ServiceInstanceContent: ...
   def ValidateMigration(self, vm: list[VirtualMachine], state: Optional[VirtualMachine.PowerState], testType: list[str], pool: Optional[ResourcePool], host: Optional[HostSystem]) -> list[Event]: ...
   def QueryVMotionCompatibility(self, vm: VirtualMachine, host: list[HostSystem], compatibility: list[str]) -> list[HostVMotionCompatibility]: ...
   def RetrieveProductComponents(self) -> list[ProductComponentInfo]: ...


class ServiceInstanceContent(DynamicData):
   rootFolder: Folder
   propertyCollector: PropertyCollector
   viewManager: Optional[ViewManager] = None
   about: AboutInfo
   setting: Optional[OptionManager] = None
   userDirectory: Optional[UserDirectory] = None
   sessionManager: Optional[SessionManager] = None
   authorizationManager: Optional[AuthorizationManager] = None
   serviceManager: Optional[ServiceManager] = None
   perfManager: Optional[PerformanceManager] = None
   scheduledTaskManager: Optional[ScheduledTaskManager] = None
   alarmManager: Optional[AlarmManager] = None
   eventManager: Optional[EventManager] = None
   taskManager: Optional[TaskManager] = None
   extensionManager: Optional[ExtensionManager] = None
   customizationSpecManager: Optional[CustomizationSpecManager] = None
   guestCustomizationManager: Optional[GuestCustomizationManager] = None
   customFieldsManager: Optional[CustomFieldsManager] = None
   accountManager: Optional[LocalAccountManager] = None
   diagnosticManager: Optional[DiagnosticManager] = None
   licenseManager: Optional[LicenseManager] = None
   searchIndex: Optional[SearchIndex] = None
   fileManager: Optional[FileManager] = None
   datastoreNamespaceManager: Optional[DatastoreNamespaceManager] = None
   virtualDiskManager: Optional[VirtualDiskManager] = None
   virtualizationManager: Optional[VirtualizationManager] = None
   snmpSystem: Optional[SnmpSystem] = None
   vmProvisioningChecker: Optional[ProvisioningChecker] = None
   vmCompatibilityChecker: Optional[CompatibilityChecker] = None
   ovfManager: Optional[OvfManager] = None
   ipPoolManager: Optional[IpPoolManager] = None
   dvSwitchManager: Optional[DistributedVirtualSwitchManager] = None
   hostProfileManager: Optional[ProfileManager] = None
   clusterProfileManager: Optional[ProfileManager] = None
   complianceManager: Optional[ComplianceManager] = None
   localizationManager: Optional[LocalizationManager] = None
   storageResourceManager: Optional[StorageResourceManager] = None
   guestOperationsManager: Optional[GuestOperationsManager] = None
   overheadMemoryManager: Optional[OverheadMemoryManager] = None
   certificateManager: Optional[CertificateManager] = None
   ioFilterManager: Optional[IoFilterManager] = None
   vStorageObjectManager: Optional[VStorageObjectManagerBase] = None
   hostSpecManager: Optional[HostSpecificationManager] = None
   cryptoManager: Optional[CryptoManager] = None
   healthUpdateManager: Optional[HealthUpdateManager] = None
   failoverClusterConfigurator: Optional[FailoverClusterConfigurator] = None
   failoverClusterManager: Optional[FailoverClusterManager] = None
   tenantManager: Optional[TenantManager] = None
   siteInfoManager: Optional[SiteInfoManager] = None
   storageQueryManager: Optional[StorageQueryManager] = None
   directPathProfileManager: Optional[DirectPathProfileManager] = None


class ServiceLocator(DynamicData):
   class Credential(DynamicData):
      pass

   class NamePassword(Credential):
      username: str
      password: str

   class SAMLCredential(Credential):
      token: Optional[str] = None

   instanceUuid: str
   url: str
   credential: Credential
   sslThumbprint: Optional[str] = None
   sslCertificate: Optional[str] = None


class ServiceManager(ManagedObject):
   class ServiceInfo(DynamicData):
      serviceName: str
      location: list[str] = []
      service: ManagedObject
      description: str

   @property
   def service(self) -> list[ServiceInfo]: ...

   def QueryServiceList(self, serviceName: Optional[str], location: list[str]) -> list[ServiceInfo]: ...


class SessionManager(ManagedObject):
   class LocalTicket(DynamicData):
      userName: str
      passwordFilePath: str

   class GenericServiceTicket(DynamicData):
      class TicketType(Enum):
         HttpNfcServiceTicket: ClassVar['TicketType'] = 'HttpNfcServiceTicket'
         HostServiceTicket: ClassVar['TicketType'] = 'HostServiceTicket'
         VcServiceTicket: ClassVar['TicketType'] = 'VcServiceTicket'

      id: str
      hostName: Optional[str] = None
      sslThumbprint: Optional[str] = None
      certThumbprintList: list[CertThumbprint] = []
      sslCertificate: Optional[str] = None
      ticketType: Optional[str] = None

   class ServiceRequestSpec(DynamicData):
      pass

   class VmomiServiceRequestSpec(ServiceRequestSpec):
      method: ManagedMethod

   class HttpServiceRequestSpec(ServiceRequestSpec):
      class Method(Enum):
         httpOptions: ClassVar['Method'] = 'httpOptions'
         httpGet: ClassVar['Method'] = 'httpGet'
         httpHead: ClassVar['Method'] = 'httpHead'
         httpPost: ClassVar['Method'] = 'httpPost'
         httpPut: ClassVar['Method'] = 'httpPut'
         httpDelete: ClassVar['Method'] = 'httpDelete'
         httpTrace: ClassVar['Method'] = 'httpTrace'
         httpConnect: ClassVar['Method'] = 'httpConnect'

      method: Optional[str] = None
      url: str

   @property
   def sessionList(self) -> list[UserSession]: ...
   @property
   def currentSession(self) -> Optional[UserSession]: ...
   @property
   def message(self) -> Optional[str]: ...
   @property
   def messageLocaleList(self) -> list[str]: ...
   @property
   def supportedLocaleList(self) -> list[str]: ...
   @property
   def defaultLocale(self) -> str: ...

   def UpdateMessage(self, message: str) -> None: ...
   def LoginByToken(self, locale: Optional[str]) -> UserSession: ...
   def Login(self, userName: str, password: str, locale: Optional[str]) -> UserSession: ...
   def LoginBySSPI(self, base64Token: str, locale: Optional[str]) -> UserSession: ...
   def Logout(self) -> None: ...
   def AcquireLocalTicket(self, userName: str) -> LocalTicket: ...
   def AcquireGenericServiceTicket(self, spec: ServiceRequestSpec) -> GenericServiceTicket: ...
   def Terminate(self, sessionId: list[str]) -> None: ...
   def SetLocale(self, locale: str) -> None: ...
   def LoginExtensionBySubjectName(self, extensionKey: str, locale: Optional[str]) -> UserSession: ...
   def LoginExtensionByCertificate(self, extensionKey: str, locale: Optional[str]) -> UserSession: ...
   def ImpersonateUser(self, userName: str, locale: Optional[str]) -> UserSession: ...
   def SessionIsActive(self, sessionID: str, userName: str) -> bool: ...
   def AcquireCloneTicket(self) -> str: ...
   def CloneSession(self, cloneTicket: str) -> UserSession: ...


class SharesInfo(DynamicData):
   class Level(Enum):
      low: ClassVar['Level'] = 'low'
      normal: ClassVar['Level'] = 'normal'
      high: ClassVar['Level'] = 'high'
      custom: ClassVar['Level'] = 'custom'

   shares: int
   level: Level


class SharesOption(DynamicData):
   sharesOption: IntOption
   defaultLevel: SharesInfo.Level


class SimpleCommand(ManagedObject):
   class Encoding(Enum):
      CSV: ClassVar['Encoding'] = 'CSV'
      HEX: ClassVar['Encoding'] = 'HEX'
      STRING: ClassVar['Encoding'] = 'STRING'

   @property
   def encodingType(self) -> Encoding: ...
   @property
   def entity(self) -> ServiceManager.ServiceInfo: ...

   def Execute(self, arguments: list[str]) -> str: ...

class SingleIp(IpAddress):
   address: str

class SingleMac(MacAddress):
   address: str


class SiteInfo(DynamicData):
   pass


class SiteInfoManager(ManagedObject):
   def GetSiteInfo(self) -> SiteInfo: ...


class StoragePod(Folder):
   class Summary(DynamicData):
      name: str
      capacity: long
      freeSpace: long

   @property
   def summary(self) -> Optional[Summary]: ...
   @property
   def podStorageDrsEntry(self) -> Optional[StorageResourceManager.PodStorageDrsEntry]: ...


class StorageQueryManager(ManagedObject):
   def QueryHostsWithAttachedLun(self, lunUuid: str) -> list[HostSystem]: ...


class StorageResourceManager(ManagedObject):
   class IOAllocationInfo(DynamicData):
      limit: Optional[long] = None
      shares: Optional[SharesInfo] = None
      reservation: Optional[int] = None

   class IOAllocationOption(DynamicData):
      limitOption: LongOption
      sharesOption: SharesOption

   class CongestionThresholdMode(Enum):
      automatic: ClassVar['CongestionThresholdMode'] = 'automatic'
      manual: ClassVar['CongestionThresholdMode'] = 'manual'

   class IORMConfigInfo(DynamicData):
      enabled: bool
      congestionThresholdMode: str
      congestionThreshold: int
      percentOfPeakThroughput: Optional[int] = None
      statsCollectionEnabled: bool
      reservationEnabled: bool
      statsAggregationDisabled: Optional[bool] = None
      reservableIopsThreshold: Optional[int] = None

   class IORMConfigSpec(DynamicData):
      enabled: Optional[bool] = None
      congestionThresholdMode: Optional[str] = None
      congestionThreshold: Optional[int] = None
      percentOfPeakThroughput: Optional[int] = None
      statsCollectionEnabled: Optional[bool] = None
      reservationEnabled: Optional[bool] = None
      statsAggregationDisabled: Optional[bool] = None
      reservableIopsThreshold: Optional[int] = None

   class IORMConfigOption(DynamicData):
      enabledOption: BoolOption
      congestionThresholdOption: IntOption
      statsCollectionEnabledOption: BoolOption
      reservationEnabledOption: BoolOption

   class StoragePerformanceSummary(DynamicData):
      interval: int
      percentile: list[int] = []
      datastoreReadLatency: list[double] = []
      datastoreWriteLatency: list[double] = []
      datastoreVmLatency: list[double] = []
      datastoreReadIops: list[double] = []
      datastoreWriteIops: list[double] = []
      siocActivityDuration: int

   class PodStorageDrsEntry(DynamicData):
      storageDrsConfig: ConfigInfo
      recommendation: list[Recommendation] = []
      drsFault: list[DrsFaults] = []
      actionHistory: list[ActionHistory] = []

   class StorageProfileStatistics(DynamicData):
      profileId: str
      totalSpaceMB: long
      usedSpaceMB: long

   def ConfigureDatastoreIORM(self, datastore: Datastore, spec: IORMConfigSpec) -> Task: ...
   def QueryIORMConfigOption(self, host: HostSystem) -> IORMConfigOption: ...
   def QueryDatastorePerformanceSummary(self, datastore: Datastore) -> list[StoragePerformanceSummary]: ...
   def ApplyRecommendationToPod(self, pod: StoragePod, key: str) -> Task: ...
   def ApplyRecommendation(self, key: list[str]) -> Task: ...
   def CancelRecommendation(self, key: list[str]) -> None: ...
   def RefreshRecommendation(self, pod: StoragePod) -> None: ...
   def RefreshRecommendationsForPod(self, pod: StoragePod) -> Task: ...
   def ConfigureStorageDrsForPod(self, pod: StoragePod, spec: ConfigSpec, modify: bool) -> Task: ...
   def ValidateStoragePodConfig(self, pod: StoragePod, spec: ConfigSpec) -> Optional[MethodFault]: ...
   def RecommendDatastores(self, storageSpec: StoragePlacementSpec) -> StoragePlacementResult: ...


class StringExpression(NegatableExpression):
   value: Optional[str] = None


class StringPolicy(InheritablePolicy):
   value: Optional[str] = None


class Tag(DynamicData):
   key: str


class TagId(DynamicData):
   class NameId(DynamicData):
      tag: str
      category: str

   nameId: Optional[NameId] = None
   uuid: Optional[str] = None


class TagSpec(ArrayUpdateSpec):
   id: TagId


class Task(ExtensibleManagedObject):
   @property
   def info(self) -> TaskInfo: ...

   def Cancel(self) -> None: ...
   def UpdateProgress(self, percentDone: int) -> None: ...
   def SetState(self, state: TaskInfo.State, result: Optional[object], fault: Optional[MethodFault]) -> None: ...
   def UpdateDescription(self, description: LocalizableMessage) -> None: ...


class TaskDescription(DynamicData):
   methodInfo: list[ElementDescription] = []
   state: list[ElementDescription] = []
   reason: list[TypeDescription] = []


class TaskFilterSpec(DynamicData):
   class RecursionOption(Enum):
      self: ClassVar['RecursionOption'] = 'self'
      children: ClassVar['RecursionOption'] = 'children'
      all: ClassVar['RecursionOption'] = 'all'

   class TimeOption(Enum):
      queuedTime: ClassVar['TimeOption'] = 'queuedTime'
      startedTime: ClassVar['TimeOption'] = 'startedTime'
      completedTime: ClassVar['TimeOption'] = 'completedTime'

   class ByEntity(DynamicData):
      entity: ManagedEntity
      recursion: RecursionOption

   class ByTime(DynamicData):
      timeType: TimeOption
      beginTime: Optional[datetime] = None
      endTime: Optional[datetime] = None

   class ByUsername(DynamicData):
      systemUser: bool
      userList: list[str] = []

   entity: Optional[ByEntity] = None
   time: Optional[ByTime] = None
   userName: Optional[ByUsername] = None
   activationId: list[str] = []
   state: list[TaskInfo.State] = []
   alarm: Optional[Alarm] = None
   scheduledTask: Optional[ScheduledTask] = None
   eventChainId: list[int] = []
   tag: list[str] = []
   parentTaskKey: list[str] = []
   rootTaskKey: list[str] = []


class TaskHistoryCollector(HistoryCollector):
   @property
   def latestPage(self) -> list[TaskInfo]: ...

   def ReadNext(self, maxCount: int) -> list[TaskInfo]: ...
   def ReadPrev(self, maxCount: int) -> list[TaskInfo]: ...


class TaskInfo(DynamicData):
   class State(Enum):
      queued: ClassVar['State'] = 'queued'
      running: ClassVar['State'] = 'running'
      success: ClassVar['State'] = 'success'
      error: ClassVar['State'] = 'error'

   key: str
   task: Task
   description: Optional[LocalizableMessage] = None
   name: Optional[ManagedMethod] = None
   descriptionId: str
   entity: Optional[ManagedEntity] = None
   entityName: Optional[str] = None
   locked: list[ManagedEntity] = []
   state: State
   cancelled: bool
   cancelable: bool
   error: Optional[MethodFault] = None
   result: Optional[object] = None
   progress: Optional[int] = None
   progressDetails: list[KeyAnyValue] = []
   reason: TaskReason
   queueTime: datetime
   startTime: Optional[datetime] = None
   completeTime: Optional[datetime] = None
   eventChainId: int
   changeTag: Optional[str] = None
   parentTaskKey: Optional[str] = None
   rootTaskKey: Optional[str] = None
   activationId: Optional[str] = None


class TaskInfoFilterSpec(DynamicData):
   class FilterTaskResults(DynamicData):
      removeAll: Optional[bool] = None
      descriptionIds: list[str] = []
      filterIn: Optional[bool] = None

   filterTaskResults: Optional[FilterTaskResults] = None


class TaskManager(ManagedObject):
   class TaskViewSpec(DynamicData):
      pass

   class ViewByStartId(TaskViewSpec):
      count: int
      startId: str

   @property
   def recentTask(self) -> list[Task]: ...
   @property
   def description(self) -> TaskDescription: ...
   @property
   def maxCollector(self) -> int: ...

   def CreateCollector(self, filter: TaskFilterSpec) -> TaskHistoryCollector: ...
   def CreateCollectorWithInfoFilter(self, filter: TaskFilterSpec, infoFilter: Optional[TaskInfoFilterSpec]) -> TaskHistoryCollector: ...
   def CreateTask(self, obj: ManagedObject, taskTypeId: str, initiatedBy: Optional[str], cancelable: bool, parentTaskKey: Optional[str], activationId: Optional[str]) -> TaskInfo: ...
   def ReadNextTasksByViewSpec(self, viewSpec: TaskViewSpec, filterSpec: TaskFilterSpec, infoFilterSpec: Optional[TaskInfoFilterSpec]) -> list[TaskInfo]: ...


class TaskReason(DynamicData):
   pass


class TaskReasonAlarm(TaskReason):
   alarmName: str
   alarm: Alarm
   entityName: str
   entity: ManagedEntity


class TaskReasonSchedule(TaskReason):
   name: str
   scheduledTask: ScheduledTask

class TaskReasonSystem(TaskReason):
   pass

class TaskReasonUser(TaskReason):
   userName: str


class TransitGateway(ManagedEntity):
   class CreateSpec(DynamicData):
      ID: str
      name: str

   class ConfigInfo(DynamicData):
      ID: str
      name: str

   class ConfigSpec(DynamicData):
      name: Optional[str] = None

   @property
   def config(self) -> ConfigInfo: ...

class TypeDescription(Description):
   key: type


class UpdateVirtualMachineFilesResult(DynamicData):
   class FailedVmFileInfo(DynamicData):
      vmFile: str
      fault: MethodFault

   failedVmFile: list[FailedVmFileInfo] = []


class UserDirectory(ManagedObject):
   @property
   def domainList(self) -> list[str]: ...

   def RetrieveUserGroups(self, domain: Optional[str], searchStr: str, belongsToGroup: Optional[str], belongsToUser: Optional[str], exactMatch: bool, findUsers: bool, findGroups: bool) -> list[UserSearchResult]: ...


class UserSearchResult(DynamicData):
   principal: str
   fullName: Optional[str] = None
   group: bool


class UserSession(DynamicData):
   key: str
   userName: str
   fullName: str
   loginTime: datetime
   lastActiveTime: datetime
   locale: str
   messageLocale: str
   extensionSession: bool
   ipAddress: str
   userAgent: str
   callCount: long


class VVolVmConfigFileUpdateResult(DynamicData):
   class FailedVmConfigFileInfo(DynamicData):
      targetConfigVVolId: str
      dsPath: Optional[str] = None
      fault: MethodFault

   succeededVmConfigFile: list[KeyValue] = []
   failedVmConfigFile: list[FailedVmConfigFileInfo] = []


class VasaStorageArray(DynamicData):
   class DiscoverySvcInfo(DynamicData):
      portType: str
      svcNqn: str
      ipInfo: Optional[DiscoveryIpTransport] = None
      fcInfo: Optional[DiscoveryFcTransport] = None

   class DiscoveryFcTransport(DynamicData):
      nodeWwn: str
      portWwn: str

   class DiscoveryIpTransport(DynamicData):
      ipAddress: str
      portNumber: Optional[str] = None

   name: str
   uuid: str
   vendorId: str
   modelId: str
   discoverySvcInfo: list[DiscoverySvcInfo] = []


class VimVasaProvider(DynamicData):
   class StatePerArray(DynamicData):
      priority: int
      arrayId: str
      active: bool

   class VirtualHostConfig(DynamicData):
      vhostName: Optional[str] = None
      serviceHost: str
      servicePort: Optional[int] = None

   uid: Optional[str] = None
   url: str
   name: Optional[str] = None
   selfSignedCertificate: Optional[str] = None
   vhostConfig: Optional[VirtualHostConfig] = None
   versionId: Optional[int] = None


class VimVasaProviderInfo(DynamicData):
   provider: VimVasaProvider
   arrayState: list[VimVasaProvider.StatePerArray] = []


class VirtualApp(ResourcePool):
   class VAppState(Enum):
      started: ClassVar['VAppState'] = 'started'
      stopped: ClassVar['VAppState'] = 'stopped'
      starting: ClassVar['VAppState'] = 'starting'
      stopping: ClassVar['VAppState'] = 'stopping'

   class Summary(ResourcePool.Summary):
      product: Optional[ProductInfo] = None
      vAppState: Optional[VAppState] = None
      suspended: Optional[bool] = None
      installBootRequired: Optional[bool] = None
      instanceUuid: Optional[str] = None

   class LinkInfo(DynamicData):
      key: ManagedEntity
      destroyWithParent: Optional[bool] = None

   @property
   def parentFolder(self) -> Optional[Folder]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def vAppConfig(self) -> Optional[VAppConfigInfo]: ...
   @property
   def parentVApp(self) -> Optional[ManagedEntity]: ...
   @property
   def childLink(self) -> list[LinkInfo]: ...

   def UpdateVAppConfig(self, spec: VAppConfigSpec) -> None: ...
   def UpdateLinkedChildren(self, addChangeSet: list[LinkInfo], removeSet: list[ManagedEntity]) -> None: ...
   def Clone(self, name: str, target: ResourcePool, spec: CloneSpec) -> Task: ...
   def ExportVApp(self) -> HttpNfcLease: ...
   def PowerOn(self) -> Task: ...
   def PowerOff(self, force: bool) -> Task: ...
   def Suspend(self) -> Task: ...
   def Unregister(self) -> Task: ...


class VirtualDiskManager(ManagedObject):
   class VirtualDiskType(Enum):
      preallocated: ClassVar['VirtualDiskType'] = 'preallocated'
      thin: ClassVar['VirtualDiskType'] = 'thin'
      seSparse: ClassVar['VirtualDiskType'] = 'seSparse'
      rdm: ClassVar['VirtualDiskType'] = 'rdm'
      rdmp: ClassVar['VirtualDiskType'] = 'rdmp'
      raw: ClassVar['VirtualDiskType'] = 'raw'
      delta: ClassVar['VirtualDiskType'] = 'delta'
      sparse2Gb: ClassVar['VirtualDiskType'] = 'sparse2Gb'
      thick2Gb: ClassVar['VirtualDiskType'] = 'thick2Gb'
      eagerZeroedThick: ClassVar['VirtualDiskType'] = 'eagerZeroedThick'
      sparseMonolithic: ClassVar['VirtualDiskType'] = 'sparseMonolithic'
      flatMonolithic: ClassVar['VirtualDiskType'] = 'flatMonolithic'
      thick: ClassVar['VirtualDiskType'] = 'thick'

   class VirtualDiskAdapterType(Enum):
      ide: ClassVar['VirtualDiskAdapterType'] = 'ide'
      busLogic: ClassVar['VirtualDiskAdapterType'] = 'busLogic'
      lsiLogic: ClassVar['VirtualDiskAdapterType'] = 'lsiLogic'

   class VirtualDiskSpec(DynamicData):
      diskType: str
      adapterType: str

   class FileBackedVirtualDiskSpec(VirtualDiskSpec):
      capacityKb: long
      profile: list[ProfileSpec] = []
      crypto: Optional[CryptoSpec] = None
      sectorFormat: Optional[str] = None

   class SeSparseVirtualDiskSpec(FileBackedVirtualDiskSpec):
      grainSizeKb: Optional[int] = None

   class DeviceBackedVirtualDiskSpec(VirtualDiskSpec):
      device: str

   def CreateVirtualDisk(self, name: str, datacenter: Optional[Datacenter], spec: VirtualDiskSpec) -> Task: ...
   def DeleteVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def MoveVirtualDisk(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destName: str, destDatacenter: Optional[Datacenter], force: Optional[bool], profile: list[ProfileSpec]) -> Task: ...
   def CopyVirtualDisk(self, sourceName: str, sourceDatacenter: Optional[Datacenter], destName: str, destDatacenter: Optional[Datacenter], destSpec: Optional[VirtualDiskSpec], force: Optional[bool]) -> Task: ...
   def ExtendVirtualDisk(self, name: str, datacenter: Optional[Datacenter], newCapacityKb: long, eagerZero: Optional[bool]) -> Task: ...
   def QueryVirtualDiskFragmentation(self, name: str, datacenter: Optional[Datacenter]) -> int: ...
   def DefragmentVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def ShrinkVirtualDisk(self, name: str, datacenter: Optional[Datacenter], copy: Optional[bool]) -> Task: ...
   def InflateVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def EagerZeroVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def ZeroFillVirtualDisk(self, name: str, datacenter: Optional[Datacenter]) -> Task: ...
   def SetVirtualDiskUuid(self, name: str, datacenter: Optional[Datacenter], uuid: str) -> None: ...
   def QueryVirtualDiskUuid(self, name: str, datacenter: Optional[Datacenter]) -> str: ...
   def QueryVirtualDiskGeometry(self, name: str, datacenter: Optional[Datacenter]) -> DiskDimensions.Chs: ...
   def ImportUnmanagedSnapshot(self, vdisk: str, datacenter: Optional[Datacenter], vvolId: str) -> None: ...
   def ReleaseManagedSnapshot(self, vdisk: str, datacenter: Optional[Datacenter]) -> None: ...


class VirtualMachine(ManagedEntity):
   class StorageRequirement(DynamicData):
      datastore: Datastore
      freeSpaceRequiredInKb: long

   class PowerState(Enum):
      poweredOff: ClassVar['PowerState'] = 'poweredOff'
      poweredOn: ClassVar['PowerState'] = 'poweredOn'
      suspended: ClassVar['PowerState'] = 'suspended'

   class AppHeartbeatStatusType(Enum):
      appStatusGray: ClassVar['AppHeartbeatStatusType'] = 'appStatusGray'
      appStatusGreen: ClassVar['AppHeartbeatStatusType'] = 'appStatusGreen'
      appStatusRed: ClassVar['AppHeartbeatStatusType'] = 'appStatusRed'

   class ConnectionState(Enum):
      connected: ClassVar['ConnectionState'] = 'connected'
      disconnected: ClassVar['ConnectionState'] = 'disconnected'
      orphaned: ClassVar['ConnectionState'] = 'orphaned'
      inaccessible: ClassVar['ConnectionState'] = 'inaccessible'
      invalid: ClassVar['ConnectionState'] = 'invalid'

   class CryptoState(Enum):
      unlocked: ClassVar['CryptoState'] = 'unlocked'
      locked: ClassVar['CryptoState'] = 'locked'

   class MovePriority(Enum):
      lowPriority: ClassVar['MovePriority'] = 'lowPriority'
      highPriority: ClassVar['MovePriority'] = 'highPriority'
      defaultPriority: ClassVar['MovePriority'] = 'defaultPriority'

   class Ticket(DynamicData):
      ticket: str
      cfgFile: str
      host: Optional[str] = None
      port: Optional[int] = None
      sslThumbprint: Optional[str] = None
      certThumbprintList: list[CertThumbprint] = []
      sslCertificate: Optional[str] = None
      url: Optional[str] = None

   class MksTicket(DynamicData):
      ticket: str
      cfgFile: str
      host: Optional[str] = None
      port: Optional[int] = None
      sslThumbprint: Optional[str] = None

   class FaultToleranceState(Enum):
      notConfigured: ClassVar['FaultToleranceState'] = 'notConfigured'
      disabled: ClassVar['FaultToleranceState'] = 'disabled'
      enabled: ClassVar['FaultToleranceState'] = 'enabled'
      needSecondary: ClassVar['FaultToleranceState'] = 'needSecondary'
      starting: ClassVar['FaultToleranceState'] = 'starting'
      running: ClassVar['FaultToleranceState'] = 'running'

   class RecordReplayState(Enum):
      recording: ClassVar['RecordReplayState'] = 'recording'
      replaying: ClassVar['RecordReplayState'] = 'replaying'
      inactive: ClassVar['RecordReplayState'] = 'inactive'

   class NeedSecondaryReason(Enum):
      initializing: ClassVar['NeedSecondaryReason'] = 'initializing'
      divergence: ClassVar['NeedSecondaryReason'] = 'divergence'
      lostConnection: ClassVar['NeedSecondaryReason'] = 'lostConnection'
      partialHardwareFailure: ClassVar['NeedSecondaryReason'] = 'partialHardwareFailure'
      userAction: ClassVar['NeedSecondaryReason'] = 'userAction'
      checkpointError: ClassVar['NeedSecondaryReason'] = 'checkpointError'
      other: ClassVar['NeedSecondaryReason'] = 'other'

   class FaultToleranceType(Enum):
      unset: ClassVar['FaultToleranceType'] = 'unset'
      recordReplay: ClassVar['FaultToleranceType'] = 'recordReplay'
      checkpointing: ClassVar['FaultToleranceType'] = 'checkpointing'

   class Connection(DynamicData):
      label: str
      client: str
      userName: str

   class MksConnection(Connection):
      pass

   class TicketType(Enum):
      mks: ClassVar['TicketType'] = 'mks'
      device: ClassVar['TicketType'] = 'device'
      guestControl: ClassVar['TicketType'] = 'guestControl'
      dnd: ClassVar['TicketType'] = 'dnd'
      webmks: ClassVar['TicketType'] = 'webmks'
      guestIntegrity: ClassVar['TicketType'] = 'guestIntegrity'
      webRemoteDevice: ClassVar['TicketType'] = 'webRemoteDevice'

   class DisplayTopology(DynamicData):
      x: int
      y: int
      width: int
      height: int

   class DiskChangeInfo(DynamicData):
      class DiskChangeExtent(DynamicData):
         start: long
         length: long

      startOffset: long
      length: long
      changedArea: list[DiskChangeExtent] = []

   class WipeResult(DynamicData):
      diskId: int
      shrinkableDiskSpace: long

   @property
   def capability(self) -> Capability: ...
   @property
   def config(self) -> Optional[ConfigInfo]: ...
   @property
   def layout(self) -> Optional[FileLayout]: ...
   @property
   def layoutEx(self) -> Optional[FileLayoutEx]: ...
   @property
   def storage(self) -> Optional[StorageInfo]: ...
   @property
   def environmentBrowser(self) -> EnvironmentBrowser: ...
   @property
   def resourcePool(self) -> Optional[ResourcePool]: ...
   @property
   def parentVApp(self) -> Optional[ManagedEntity]: ...
   @property
   def resourceConfig(self) -> Optional[ResourceConfigSpec]: ...
   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def guest(self) -> Optional[GuestInfo]: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def snapshot(self) -> Optional[SnapshotInfo]: ...
   @property
   def rootSnapshot(self) -> list[Snapshot]: ...
   @property
   def guestHeartbeatStatus(self) -> ManagedEntity.Status: ...

   def RefreshStorageInfo(self) -> None: ...
   def CreateSnapshot(self, name: str, description: Optional[str], memory: bool, quiesce: bool) -> Task: ...
   def CreateSnapshotEx(self, name: str, description: Optional[str], memory: bool, quiesceSpec: Optional[GuestQuiesceSpec]) -> Task: ...
   def RevertToCurrentSnapshot(self, host: Optional[HostSystem], suppressPowerOn: Optional[bool]) -> Task: ...
   def RemoveAllSnapshots(self, consolidate: Optional[bool], spec: Optional[SnapshotSelectionSpec]) -> Task: ...
   def ConsolidateDisks(self) -> Task: ...
   def EstimateStorageRequirementForConsolidate(self) -> Task: ...
   def Reconfigure(self, spec: ConfigSpec) -> Task: ...
   def UpgradeVirtualHardware(self, version: Optional[str]) -> Task: ...
   def ExtractOvfEnvironment(self) -> str: ...
   def PowerOn(self, host: Optional[HostSystem]) -> Task: ...
   def PowerOff(self) -> Task: ...
   def Suspend(self) -> Task: ...
   def Reset(self) -> Task: ...
   def ShutdownGuest(self) -> None: ...
   def RebootGuest(self) -> None: ...
   def StandbyGuest(self) -> None: ...
   def Answer(self, questionId: str, answerChoice: str) -> None: ...
   def Customize(self, spec: Specification) -> Task: ...
   def CheckCustomizationSpec(self, spec: Specification) -> None: ...
   def Migrate(self, pool: Optional[ResourcePool], host: Optional[HostSystem], priority: MovePriority, state: Optional[PowerState]) -> Task: ...
   def Relocate(self, spec: RelocateSpec, priority: Optional[MovePriority]) -> Task: ...
   def Clone(self, folder: Folder, name: str, spec: CloneSpec) -> Task: ...
   def InstantClone(self, spec: InstantCloneSpec) -> Task: ...
   def ExportVm(self) -> HttpNfcLease: ...
   def MarkAsTemplate(self) -> None: ...
   def MarkAsVirtualMachine(self, pool: ResourcePool, host: Optional[HostSystem]) -> None: ...
   def Unregister(self) -> None: ...
   def ResetGuestInformation(self) -> None: ...
   def MountToolsInstaller(self) -> None: ...
   def UnmountToolsInstaller(self) -> None: ...
   def UpgradeTools(self, installerOptions: Optional[str]) -> Task: ...
   def AcquireMksTicket(self) -> MksTicket: ...
   def QueryConnections(self) -> list[Connection]: ...
   def DropConnections(self, listOfConnections: list[Connection]) -> bool: ...
   def AcquireTicket(self, ticketType: str) -> Ticket: ...
   def SetScreenResolution(self, width: int, height: int) -> None: ...
   def DefragmentAllDisks(self) -> None: ...
   def CreateSecondary(self, host: Optional[HostSystem]) -> Task: ...
   def CreateSecondaryEx(self, host: Optional[HostSystem], spec: Optional[FaultToleranceConfigSpec]) -> Task: ...
   def TurnOffFaultTolerance(self) -> Task: ...
   def MakePrimary(self, vm: VirtualMachine) -> Task: ...
   def TerminateFaultTolerantVM(self, vm: Optional[VirtualMachine]) -> Task: ...
   def DisableSecondary(self, vm: VirtualMachine) -> Task: ...
   def EnableSecondary(self, vm: VirtualMachine, host: Optional[HostSystem]) -> Task: ...
   def SetDisplayTopology(self, displays: list[DisplayTopology]) -> None: ...
   def StartRecording(self, name: str, description: Optional[str]) -> Task: ...
   def StopRecording(self) -> Task: ...
   def StartReplaying(self, replaySnapshot: Snapshot) -> Task: ...
   def StopReplaying(self) -> Task: ...
   def PromoteDisks(self, unlink: bool, disks: list[VirtualDisk]) -> Task: ...
   def CreateScreenshot(self) -> Task: ...
   def PutUsbScanCodes(self, spec: UsbScanCodeSpec) -> int: ...
   def QueryChangedDiskAreas(self, snapshot: Optional[Snapshot], deviceKey: int, startOffset: long, changeId: str) -> DiskChangeInfo: ...
   def QueryUnownedFiles(self) -> list[str]: ...
   def ReloadFromPath(self, configurationPath: str) -> Task: ...
   def QueryFaultToleranceCompatibility(self) -> list[MethodFault]: ...
   def QueryFaultToleranceCompatibilityEx(self, forLegacyFt: Optional[bool]) -> list[MethodFault]: ...
   def Terminate(self) -> None: ...
   def SendNMI(self) -> None: ...
   def AttachDisk(self, diskId: ID, datastore: Datastore, controllerKey: Optional[int], unitNumber: Optional[int]) -> Task: ...
   def DetachDisk(self, diskId: ID) -> Task: ...
   def ApplyEvcMode(self, mask: list[FeatureMask], completeMasks: Optional[bool]) -> Task: ...
   def CryptoUnlock(self) -> Task: ...
   def RepairVmDiskChains(self) -> Task: ...


class VirtualizationManager(ManagedObject):
   pass


class VsanComparator(DynamicData):
   pass


class VsanCompositeConstraint(VsanResourceConstraint):
   nestedConstraints: list[VsanResourceConstraint] = []
   conjoiner: Optional[str] = None

class VsanCompositeConstraintConjoinerEnum:
   pass


class VsanDataObfuscationRule(DynamicData):
   pass


class VsanJsonComparator(VsanComparator):
   comparator: Optional[str] = None
   comparableValue: Optional[KeyAnyValue] = None


class VsanJsonFilterRule(DynamicData):
   filterComparator: Optional[VsanComparator] = None
   comparablePath: list[str] = []
   keysWithStrVal: list[str] = []
   propertyName: Optional[str] = None


class VsanMassCollector(ManagedObject):
   def VsanRetrieveProperties(self, massCollectorSpecs: list[VsanMassCollectorSpec]) -> list[PropertyCollector.ObjectContent]: ...

class VsanMassCollectorObjectCollectionEnum:
   pass


class VsanMassCollectorPropertyParams(DynamicData):
   propertyName: Optional[str] = None
   propertyParams: list[KeyAnyValue] = []


class VsanMassCollectorSpec(DynamicData):
   objects: list[ManagedObject] = []
   objectCollection: Optional[str] = None
   properties: list[str] = []
   propertiesParams: list[VsanMassCollectorPropertyParams] = []
   constraint: Optional[VsanResourceConstraint] = None


class VsanNestJsonComparator(VsanComparator):
   nestedComparators: list[VsanJsonComparator] = []
   conjoiner: Optional[str] = None


class VsanObjectTypeRule(DynamicData):
   objectType: Optional[str] = None
   attributes: list[str] = []


class VsanPhoneHomeSystem(ManagedObject):
   def VsanPerformOnlineHealthCheck(self, cluster: ClusterComputeResource) -> Task: ...
   def QueryVsanCloudHealthStatus(self) -> Optional[VsanCloudHealthStatus]: ...
   def VsanQueryObjectSnapshotsInfo(self, cluster: ClusterComputeResource) -> Optional[str]: ...
   def VsanQueryNvmeCriticalWarningStats(self, cluster: ClusterComputeResource) -> Optional[str]: ...
   def VsanQueryZdomScrubberData(self, cluster: ClusterComputeResource) -> Optional[str]: ...
   def VsanQueryLSOMwbsize(self, cluster: ClusterComputeResource) -> Optional[str]: ...


class VsanPropertyConstraint(VsanResourceConstraint):
   propertyName: Optional[str] = None
   comparator: Optional[str] = None
   comparableValue: Optional[KeyAnyValue] = None

class VsanPropertyConstraintComparatorEnum:
   pass


class VsanRegexBasedRule(DynamicData):
   rules: list[str] = []


class VsanResourceConstraint(DynamicData):
   targetType: Optional[str] = None


class VsanUpgradeSystem(ManagedObject):
   class PreflightCheckIssue(DynamicData):
      msg: str

   class HostsDisconnectedIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class MissingHostsInClusterIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class RogueHostsInClusterIssue(PreflightCheckIssue):
      uuids: list[str] = []

   class WrongEsxVersionIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class AutoClaimEnabledOnHostsIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class APIBrokenIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class V2ObjectsPresentDuringDowngradeIssue(PreflightCheckIssue):
      uuids: list[str] = []

   class NotEnoughFreeCapacityIssue(PreflightCheckIssue):
      reducedRedundancyUpgradePossible: bool

   class NetworkPartitionInfo(DynamicData):
      hosts: list[HostSystem] = []

   class NetworkPartitionIssue(PreflightCheckIssue):
      partitions: list[NetworkPartitionInfo] = []

   class PreflightCheckResult(DynamicData):
      issues: list[PreflightCheckIssue] = []
      diskMappingToRestore: Optional[DiskMapping] = None

   class UpgradeHistoryItem(DynamicData):
      timestamp: datetime
      host: Optional[HostSystem] = None
      message: str
      task: Optional[Task] = None

   class UpgradeHistoryDiskGroupOpType(Enum):
      add: ClassVar['UpgradeHistoryDiskGroupOpType'] = 'add'
      remove: ClassVar['UpgradeHistoryDiskGroupOpType'] = 'remove'

   class UpgradeHistoryDiskGroupOp(UpgradeHistoryItem):
      operation: str
      diskMapping: DiskMapping

   class UpgradeHistoryPreflightFail(UpgradeHistoryItem):
      preflightResult: PreflightCheckResult

   class UpgradeStatus(DynamicData):
      inProgress: bool
      history: list[UpgradeHistoryItem] = []
      aborted: Optional[bool] = None
      completed: Optional[bool] = None
      progress: Optional[int] = None

   def PerformUpgradePreflightCheck(self, cluster: ClusterComputeResource, downgradeFormat: Optional[bool]) -> PreflightCheckResult: ...
   def QueryUpgradeStatus(self, cluster: ClusterComputeResource) -> UpgradeStatus: ...
   def PerformUpgrade(self, cluster: ClusterComputeResource, performObjectUpgrade: Optional[bool], downgradeFormat: Optional[bool], allowReducedRedundancy: Optional[bool], excludeHosts: list[HostSystem]) -> Task: ...


class VsanUpgradeSystemEx(ManagedObject):
   def PerformUpgrade(self, cluster: ClusterComputeResource, performObjectUpgrade: Optional[bool], downgradeFormat: Optional[bool], allowReducedRedundancy: Optional[bool], excludeHosts: list[HostSystem], spec: Optional[VsanDiskFormatConversionSpec]) -> Task: ...
   def PerformUpgradePreflightAsyncCheck(self, cluster: ClusterComputeResource, downgradeFormat: Optional[bool], spec: Optional[VsanDiskFormatConversionSpec]) -> Task: ...
   def PerformUpgradePreflightCheck(self, cluster: ClusterComputeResource, downgradeFormat: Optional[bool], spec: Optional[VsanDiskFormatConversionSpec]) -> VsanDiskFormatConversionCheckResult: ...
   def RetrieveSupportedFormatVersion(self, cluster: ClusterComputeResource) -> int: ...
   def QueryUpgradeStatus(self, cluster: ClusterComputeResource) -> VsanUpgradeStatusEx: ...
