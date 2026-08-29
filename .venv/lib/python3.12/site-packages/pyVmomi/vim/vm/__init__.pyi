# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import check as check
from . import customization as customization
from . import device as device
from . import guest as guest
from . import replication as replication

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import PropertyPath
from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim import CustomFieldsManager

from pyVmomi.vim import Datastore

from pyVmomi.vim import Description

from pyVmomi.vim import ElementDescription

from pyVmomi.vim import ExtensibleManagedObject
from pyVmomi.vim import Folder

from pyVmomi.vim import HostSystem
from pyVmomi.vim import HttpNfcLease

from pyVmomi.vim import ImportSpec

from pyVmomi.vim import KeyValue

from pyVmomi.vim import LatencySensitivity
from pyVmomi.vim import ManagedEntity

from pyVmomi.vim import Network

from pyVmomi.vim import OpaqueNetwork
from pyVmomi.vim import ResourceAllocationInfo

from pyVmomi.vim import ResourceConfigOption

from pyVmomi.vim import ResourcePool
from pyVmomi.vim import ServiceLocator

from pyVmomi.vim import TagId
from pyVmomi.vim import TagSpec

from pyVmomi.vim import Task

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import DynamicProperty
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.cluster import PowerOnVmResult

from pyVmomi.vim.dvs import DistributedVirtualPortgroupInfo
from pyVmomi.vim.dvs import DistributedVirtualSwitchInfo

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.encryption import CryptoSpec

from pyVmomi.vim.ext import ManagedByInfo

from pyVmomi.vim.host import CpuIdInfo

from pyVmomi.vim.host import FeatureMask
from pyVmomi.vim.host import PciDevice

from pyVmomi.vim.host import ScsiDisk
from pyVmomi.vim.host import VFlashManager

from pyVmomi.vim.net import DhcpConfigInfo
from pyVmomi.vim.net import DnsConfigInfo
from pyVmomi.vim.net import IpConfigInfo
from pyVmomi.vim.net import IpRouteConfigInfo
from pyVmomi.vim.net import NetBIOSConfigInfo

from pyVmomi.vim.option import ArrayUpdateSpec

from pyVmomi.vim.option import BoolOption

from pyVmomi.vim.option import ChoiceOption
from pyVmomi.vim.option import IntOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.option import OptionDef

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vApp import ProductInfo

from pyVmomi.vim.vApp import VmConfigInfo

from pyVmomi.vim.vApp import VmConfigSpec

from pyVmomi.vim.vm.customization import Specification

from pyVmomi.vim.vm.device import VirtualDevice

from pyVmomi.vim.vm.device import VirtualDeviceOption

from pyVmomi.vim.vm.device import VirtualDeviceSpec

from pyVmomi.vim.vm.guest import GuestAuthentication

from pyVmomi.vim.vm.replication import ReplicationSpec



class AffinityInfo(DynamicData):
   affinitySet: list[int] = []


class BaseIndependentFilterSpec(DynamicData):
   pass


class BootOptions(DynamicData):
   class NetworkBootProtocolType(Enum):
      ipv4: ClassVar['NetworkBootProtocolType'] = 'ipv4'
      ipv6: ClassVar['NetworkBootProtocolType'] = 'ipv6'

   class BootableDevice(DynamicData):
      pass

   class BootableDiskDevice(BootableDevice):
      deviceKey: int

   class BootableEthernetDevice(BootableDevice):
      deviceKey: int

   class BootableFloppyDevice(BootableDevice):
      pass

   class BootableCdromDevice(BootableDevice):
      pass

   bootDelay: Optional[long] = None
   enterBIOSSetup: Optional[bool] = None
   efiSecureBootEnabled: Optional[bool] = None
   bootRetryEnabled: Optional[bool] = None
   bootRetryDelay: Optional[long] = None
   bootOrder: list[BootableDevice] = []
   networkBootProtocol: Optional[str] = None


class Capability(DynamicData):
   snapshotOperationsSupported: bool
   multipleSnapshotsSupported: bool
   snapshotConfigSupported: bool
   poweredOffSnapshotsSupported: bool
   memorySnapshotsSupported: bool
   revertToSnapshotSupported: bool
   quiescedSnapshotsSupported: bool
   disableSnapshotsSupported: bool
   lockSnapshotsSupported: bool
   consolePreferencesSupported: bool
   cpuFeatureMaskSupported: bool
   s1AcpiManagementSupported: bool
   settingScreenResolutionSupported: bool
   toolsAutoUpdateSupported: bool
   vmNpivWwnSupported: bool
   npivWwnOnNonRdmVmSupported: bool
   vmNpivWwnDisableSupported: bool
   vmNpivWwnUpdateSupported: bool
   swapPlacementSupported: bool
   toolsSyncTimeSupported: bool
   virtualMmuUsageSupported: bool
   diskSharesSupported: bool
   bootOptionsSupported: bool
   bootRetryOptionsSupported: bool
   settingVideoRamSizeSupported: bool
   settingDisplayTopologySupported: bool
   recordReplaySupported: bool
   changeTrackingSupported: bool
   multipleCoresPerSocketSupported: bool
   hostBasedReplicationSupported: bool
   guestAutoLockSupported: bool
   memoryReservationLockSupported: bool
   featureRequirementSupported: bool
   poweredOnMonitorTypeChangeSupported: bool
   seSparseDiskSupported: bool
   nestedHVSupported: bool
   vPMCSupported: bool
   secureBootSupported: Optional[bool] = None
   perVmEvcSupported: Optional[bool] = None
   virtualMmuUsageIgnored: Optional[bool] = None
   virtualExecUsageIgnored: Optional[bool] = None
   diskOnlySnapshotOnSuspendedVMSupported: Optional[bool] = None
   suspendToMemorySupported: Optional[bool] = None
   toolsSyncTimeAllowSupported: Optional[bool] = None
   sevSupported: Optional[bool] = None
   pmemFailoverSupported: Optional[bool] = None
   requireSgxAttestationSupported: Optional[bool] = None
   changeModeDisksSupported: Optional[bool] = None
   vendorDeviceGroupSupported: Optional[bool] = None
   sevSnpSupported: Optional[bool] = None
   tdxSupported: Optional[bool] = None
   ehvSecureBootSupported: Optional[bool] = None


class CdromInfo(TargetInfo):
   description: Optional[str] = None


class CertThumbprint(DynamicData):
   class HashAlgorithm(Enum):
      sha256: ClassVar['HashAlgorithm'] = 'sha256'

   thumbprint: str
   hashAlgorithm: Optional[str] = None


class CloneSpec(DynamicData):
   class TpmProvisionPolicy(Enum):
      copy: ClassVar['TpmProvisionPolicy'] = 'copy'
      replace: ClassVar['TpmProvisionPolicy'] = 'replace'

   location: RelocateSpec
   template: bool
   config: Optional[ConfigSpec] = None
   customization: Optional[Specification] = None
   powerOn: bool
   snapshot: Optional[Snapshot] = None
   memory: Optional[bool] = None
   tpmProvisionPolicy: Optional[str] = None


class ConfigInfo(DynamicData):
   class NpivWwnType(Enum):
      vc: ClassVar['NpivWwnType'] = 'vc'
      host: ClassVar['NpivWwnType'] = 'host'
      external: ClassVar['NpivWwnType'] = 'external'

   class SwapPlacementType(Enum):
      inherit: ClassVar['SwapPlacementType'] = 'inherit'
      vmDirectory: ClassVar['SwapPlacementType'] = 'vmDirectory'
      hostLocal: ClassVar['SwapPlacementType'] = 'hostLocal'

   class DatastoreUrlPair(DynamicData):
      name: str
      url: str

   class OverheadInfo(DynamicData):
      initialMemoryReservation: Optional[long] = None
      initialSwapReservation: Optional[long] = None

   changeVersion: str
   modified: datetime
   name: str
   guestFullName: str
   version: str
   uuid: str
   createDate: Optional[datetime] = None
   instanceUuid: Optional[str] = None
   npivNodeWorldWideName: list[long] = []
   npivPortWorldWideName: list[long] = []
   npivWorldWideNameType: Optional[str] = None
   npivDesiredNodeWwns: Optional[short] = None
   npivDesiredPortWwns: Optional[short] = None
   npivTemporaryDisabled: Optional[bool] = None
   npivOnNonRdmDisks: Optional[bool] = None
   locationId: Optional[str] = None
   template: bool
   guestId: str
   alternateGuestName: str
   annotation: Optional[str] = None
   files: FileInfo
   tools: Optional[ToolsConfigInfo] = None
   flags: FlagInfo
   consolePreferences: Optional[ConsolePreferences] = None
   defaultPowerOps: DefaultPowerOpInfo
   rebootPowerOff: Optional[bool] = None
   hardware: VirtualHardware
   vcpuConfig: list[VcpuConfig] = []
   cpuAllocation: Optional[ResourceAllocationInfo] = None
   memoryAllocation: Optional[ResourceAllocationInfo] = None
   latencySensitivity: Optional[LatencySensitivity] = None
   memoryHotAddEnabled: Optional[bool] = None
   cpuHotAddEnabled: Optional[bool] = None
   cpuHotRemoveEnabled: Optional[bool] = None
   hotPlugMemoryLimit: Optional[long] = None
   hotPlugMemoryIncrementSize: Optional[long] = None
   cpuAffinity: Optional[AffinityInfo] = None
   memoryAffinity: Optional[AffinityInfo] = None
   networkShaper: Optional[NetworkShaperInfo] = None
   extraConfig: list[OptionValue] = []
   cpuFeatureMask: list[CpuIdInfo] = []
   datastoreUrl: list[DatastoreUrlPair] = []
   swapPlacement: Optional[str] = None
   bootOptions: Optional[BootOptions] = None
   ftInfo: Optional[FaultToleranceConfigInfo] = None
   repConfig: Optional[ReplicationConfigSpec] = None
   vAppConfig: Optional[VmConfigInfo] = None
   vAssertsEnabled: Optional[bool] = None
   changeTrackingEnabled: Optional[bool] = None
   firmware: Optional[str] = None
   maxMksConnections: Optional[int] = None
   guestAutoLockEnabled: Optional[bool] = None
   managedBy: Optional[ManagedByInfo] = None
   memoryReservationLockedToMax: Optional[bool] = None
   initialOverhead: Optional[OverheadInfo] = None
   nestedHVEnabled: Optional[bool] = None
   vPMCEnabled: Optional[bool] = None
   scheduledHardwareUpgradeInfo: Optional[ScheduledHardwareUpgradeInfo] = None
   forkConfigInfo: Optional[ForkConfigInfo] = None
   vFlashCacheReservation: Optional[long] = None
   vmxConfigChecksum: Optional[binary] = None
   messageBusTunnelEnabled: Optional[bool] = None
   vmStorageObjectId: Optional[str] = None
   swapStorageObjectId: Optional[str] = None
   keyId: Optional[CryptoKeyId] = None
   guestIntegrityInfo: Optional[GuestIntegrityInfo] = None
   migrateEncryption: Optional[str] = None
   sgxInfo: Optional[SgxInfo] = None
   contentLibItemInfo: Optional[ContentLibraryItemInfo] = None
   ftEncryptionMode: Optional[str] = None
   guestMonitoringModeInfo: Optional[GuestMonitoringModeInfo] = None
   sevEnabled: Optional[bool] = None
   numaInfo: Optional[VirtualNumaInfo] = None
   pmemFailoverEnabled: Optional[bool] = None
   vmxStatsCollectionEnabled: Optional[bool] = None
   vmOpNotificationToAppEnabled: Optional[bool] = None
   vmOpNotificationTimeout: Optional[long] = None
   deviceSwap: Optional[VirtualDeviceSwap] = None
   pmem: Optional[VirtualPMem] = None
   deviceGroups: Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: Optional[bool] = None
   metroFtEnabled: Optional[bool] = None
   vmxRuntimeConfig: list[OptionValue] = []
   metroFtHostGroup: Optional[str] = None
   tdxEnabled: Optional[bool] = None
   sevSnpEnabled: Optional[bool] = None
   guestArchitecture: Optional[str] = None


class ConfigOption(DynamicData):
   version: str
   description: str
   guestOSDescriptor: list[GuestOsDescriptor] = []
   guestOSDefaultIndex: int
   hardwareOptions: VirtualHardwareOption
   capabilities: Capability
   datastore: DatastoreOption
   defaultDevice: list[VirtualDevice] = []
   supportedMonitorType: list[str] = []
   supportedOvfEnvironmentTransport: list[str] = []
   supportedOvfInstallTransport: list[str] = []
   propertyRelations: list[PropertyRelation] = []


class ConfigOptionDescriptor(DynamicData):
   key: str
   description: Optional[str] = None
   host: list[HostSystem] = []
   createSupported: bool
   defaultConfigOption: bool
   runSupported: bool
   upgradeSupported: bool


class ConfigSpec(DynamicData):
   class NpivWwnOp(Enum):
      generate: ClassVar['NpivWwnOp'] = 'generate'
      set: ClassVar['NpivWwnOp'] = 'set'
      remove: ClassVar['NpivWwnOp'] = 'remove'
      extend: ClassVar['NpivWwnOp'] = 'extend'

   class EncryptedFtModes(Enum):
      ftEncryptionDisabled: ClassVar['EncryptedFtModes'] = 'ftEncryptionDisabled'
      ftEncryptionOpportunistic: ClassVar['EncryptedFtModes'] = 'ftEncryptionOpportunistic'
      ftEncryptionRequired: ClassVar['EncryptedFtModes'] = 'ftEncryptionRequired'

   class EncryptedVMotionModes(Enum):
      disabled: ClassVar['EncryptedVMotionModes'] = 'disabled'
      opportunistic: ClassVar['EncryptedVMotionModes'] = 'opportunistic'
      required: ClassVar['EncryptedVMotionModes'] = 'required'

   class CpuIdInfoSpec(ArrayUpdateSpec):
      info: Optional[CpuIdInfo] = None

   changeVersion: Optional[str] = None
   name: Optional[str] = None
   version: Optional[str] = None
   createDate: Optional[datetime] = None
   uuid: Optional[str] = None
   instanceUuid: Optional[str] = None
   npivNodeWorldWideName: list[long] = []
   npivPortWorldWideName: list[long] = []
   npivWorldWideNameType: Optional[str] = None
   npivDesiredNodeWwns: Optional[short] = None
   npivDesiredPortWwns: Optional[short] = None
   npivTemporaryDisabled: Optional[bool] = None
   npivOnNonRdmDisks: Optional[bool] = None
   npivWorldWideNameOp: Optional[str] = None
   locationId: Optional[str] = None
   guestId: Optional[str] = None
   alternateGuestName: Optional[str] = None
   annotation: Optional[str] = None
   files: Optional[FileInfo] = None
   tools: Optional[ToolsConfigInfo] = None
   flags: Optional[FlagInfo] = None
   consolePreferences: Optional[ConsolePreferences] = None
   powerOpInfo: Optional[DefaultPowerOpInfo] = None
   rebootPowerOff: Optional[bool] = None
   numCPUs: Optional[int] = None
   vcpuConfig: list[VcpuConfig] = []
   numCoresPerSocket: Optional[int] = None
   memoryMB: Optional[long] = None
   memoryHotAddEnabled: Optional[bool] = None
   cpuHotAddEnabled: Optional[bool] = None
   cpuHotRemoveEnabled: Optional[bool] = None
   virtualICH7MPresent: Optional[bool] = None
   virtualSMCPresent: Optional[bool] = None
   deviceChange: list[VirtualDeviceSpec] = []
   cpuAllocation: Optional[ResourceAllocationInfo] = None
   memoryAllocation: Optional[ResourceAllocationInfo] = None
   latencySensitivity: Optional[LatencySensitivity] = None
   cpuAffinity: Optional[AffinityInfo] = None
   memoryAffinity: Optional[AffinityInfo] = None
   networkShaper: Optional[NetworkShaperInfo] = None
   cpuFeatureMask: list[CpuIdInfoSpec] = []
   extraConfig: list[OptionValue] = []
   swapPlacement: Optional[str] = None
   bootOptions: Optional[BootOptions] = None
   vAppConfig: Optional[VmConfigSpec] = None
   ftInfo: Optional[FaultToleranceConfigInfo] = None
   repConfig: Optional[ReplicationConfigSpec] = None
   vAppConfigRemoved: Optional[bool] = None
   vAssertsEnabled: Optional[bool] = None
   changeTrackingEnabled: Optional[bool] = None
   firmware: Optional[str] = None
   maxMksConnections: Optional[int] = None
   guestAutoLockEnabled: Optional[bool] = None
   managedBy: Optional[ManagedByInfo] = None
   memoryReservationLockedToMax: Optional[bool] = None
   nestedHVEnabled: Optional[bool] = None
   vPMCEnabled: Optional[bool] = None
   scheduledHardwareUpgradeInfo: Optional[ScheduledHardwareUpgradeInfo] = None
   vmProfile: list[ProfileSpec] = []
   messageBusTunnelEnabled: Optional[bool] = None
   crypto: Optional[CryptoSpec] = None
   migrateEncryption: Optional[str] = None
   sgxInfo: Optional[SgxInfo] = None
   ftEncryptionMode: Optional[str] = None
   guestMonitoringModeInfo: Optional[GuestMonitoringModeInfo] = None
   sevEnabled: Optional[bool] = None
   virtualNuma: Optional[VirtualNuma] = None
   motherboardLayout: Optional[str] = None
   pmemFailoverEnabled: Optional[bool] = None
   vmxStatsCollectionEnabled: Optional[bool] = None
   vmOpNotificationToAppEnabled: Optional[bool] = None
   vmOpNotificationTimeout: Optional[long] = None
   deviceSwap: Optional[VirtualDeviceSwap] = None
   simultaneousThreads: Optional[int] = None
   pmem: Optional[VirtualPMem] = None
   deviceGroups: Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: Optional[bool] = None
   metroFtEnabled: Optional[bool] = None
   metroFtHostGroup: Optional[str] = None
   tdxEnabled: Optional[bool] = None
   sevSnpEnabled: Optional[bool] = None
   tagSpecs: list[TagSpec] = []
   vmPlacementPolicies: list[VmPlacementPolicy] = []


class ConfigTarget(DynamicData):
   numCpus: int
   numCpuCores: int
   numNumaNodes: int
   maxCpusPerHost: Optional[int] = None
   smcPresent: bool
   datastore: list[DatastoreInfo] = []
   network: list[NetworkInfo] = []
   opaqueNetwork: list[OpaqueNetworkInfo] = []
   distributedVirtualPortgroup: list[DistributedVirtualPortgroupInfo] = []
   distributedVirtualSwitch: list[DistributedVirtualSwitchInfo] = []
   subnetInfo: list[SubnetInfo] = []
   cdRom: list[CdromInfo] = []
   serial: list[SerialInfo] = []
   parallel: list[ParallelInfo] = []
   sound: list[SoundInfo] = []
   usb: list[UsbInfo] = []
   floppy: list[FloppyInfo] = []
   legacyNetworkInfo: list[LegacyNetworkSwitchInfo] = []
   scsiPassthrough: list[ScsiPassthroughInfo] = []
   scsiDisk: list[ScsiDiskDeviceInfo] = []
   ideDisk: list[IdeDiskDeviceInfo] = []
   maxMemMBOptimalPerf: int
   supportedMaxMemMB: Optional[int] = None
   resourcePool: Optional[ResourcePool.RuntimeInfo] = None
   autoVmotion: Optional[bool] = None
   pciPassthrough: list[PciPassthroughInfo] = []
   sriov: list[SriovInfo] = []
   vFlashModule: list[VFlashModuleInfo] = []
   sharedGpuPassthroughTypes: list[PciSharedGpuPassthroughInfo] = []
   availablePersistentMemoryReservationMB: Optional[long] = None
   dynamicPassthrough: list[DynamicPassthroughInfo] = []
   sgxTargetInfo: Optional[SgxTargetInfo] = None
   precisionClockInfo: list[PrecisionClockInfo] = []
   sevSupported: Optional[bool] = None
   vgpuDeviceInfo: list[VgpuDeviceInfo] = []
   vgpuProfileInfo: list[VgpuProfileInfo] = []
   vendorDeviceGroupInfo: list[VendorDeviceGroupInfo] = []
   maxSimultaneousThreads: Optional[int] = None
   dvxClassInfo: list[DvxClassInfo] = []
   sevSnpSupported: Optional[bool] = None
   tdxSupported: Optional[bool] = None
   vMotionBandwidth: list[long] = []


class ConsolePreferences(DynamicData):
   powerOnWhenOpened: Optional[bool] = None
   enterFullScreenOnPowerOn: Optional[bool] = None
   closeOnPowerOffOrSuspend: Optional[bool] = None


class ContentLibraryItemInfo(DynamicData):
   contentLibraryItemUuid: str
   contentLibraryItemVersion: Optional[str] = None


class DatastoreInfo(TargetInfo):
   datastore: Datastore.Summary
   capability: Datastore.Capability
   maxFileSize: long
   maxVirtualDiskCapacity: Optional[long] = None
   maxPhysicalRDMFileSize: Optional[long] = None
   maxVirtualRDMFileSize: Optional[long] = None
   mode: str
   vStorageSupport: Optional[str] = None
   supportedVDiskFormats: list[str] = []


class DatastoreOption(DynamicData):
   class FileSystemVolumeOption(DynamicData):
      fileSystemType: type
      majorVersion: Optional[int] = None

   unsupportedVolumes: list[FileSystemVolumeOption] = []


class DefaultPowerOpInfo(DynamicData):
   class PowerOpType(Enum):
      soft: ClassVar['PowerOpType'] = 'soft'
      hard: ClassVar['PowerOpType'] = 'hard'
      preset: ClassVar['PowerOpType'] = 'preset'

   class StandbyActionType(Enum):
      checkpoint: ClassVar['StandbyActionType'] = 'checkpoint'
      powerOnSuspend: ClassVar['StandbyActionType'] = 'powerOnSuspend'

   powerOffType: Optional[str] = None
   suspendType: Optional[str] = None
   resetType: Optional[str] = None
   defaultPowerOffType: Optional[str] = None
   defaultSuspendType: Optional[str] = None
   defaultResetType: Optional[str] = None
   standbyAction: Optional[str] = None

class DefaultProfileSpec(ProfileSpec):
   pass


class DefinedProfileSpec(ProfileSpec):
   profileId: str
   replicationSpec: Optional[ReplicationSpec] = None
   profileData: Optional[ProfileRawData] = None
   profileParams: list[KeyValue] = []


class DeviceRuntimeInfo(DynamicData):
   class DeviceRuntimeState(DynamicData):
      pass

   class VirtualEthernetCardRuntimeState(DeviceRuntimeState):
      class VmDirectPathGen2InactiveReasonVm(Enum):
         vmNptIncompatibleGuest: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuest'
         vmNptIncompatibleGuestDriver: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuestDriver'
         vmNptIncompatibleAdapterType: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterType'
         vmNptDisabledOrDisconnectedAdapter: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptDisabledOrDisconnectedAdapter'
         vmNptIncompatibleAdapterFeatures: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterFeatures'
         vmNptIncompatibleBackingType: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleBackingType'
         vmNptInsufficientMemoryReservation: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptInsufficientMemoryReservation'
         vmNptFaultToleranceOrRecordReplayConfigured: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptFaultToleranceOrRecordReplayConfigured'
         vmNptConflictingIOChainConfigured: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingIOChainConfigured'
         vmNptMonitorBlocks: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptMonitorBlocks'
         vmNptConflictingOperationInProgress: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingOperationInProgress'
         vmNptRuntimeError: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptRuntimeError'
         vmNptOutOfIntrVector: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptOutOfIntrVector'
         vmNptVMCIActive: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptVMCIActive'

      class VmDirectPathGen2InactiveReasonOther(Enum):
         vmNptIncompatibleHost: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleHost'
         vmNptIncompatibleNetwork: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleNetwork'

      vmDirectPathGen2Active: Optional[bool] = None
      vmDirectPathGen2InactiveReasonVm: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: Optional[str] = None
      uptv2Active: Optional[bool] = None
      uptv2InactiveReasonVm: list[str] = []
      uptv2InactiveReasonOther: list[str] = []
      reservationStatus: Optional[str] = None
      attachmentStatus: Optional[str] = None
      featureRequirement: list[FeatureRequirement] = []

   runtimeState: DeviceRuntimeState
   key: int


class DiskDeviceInfo(TargetInfo):
   capacity: Optional[long] = None
   vm: list[VirtualMachine] = []


class DvxClassInfo(DynamicData):
   deviceClass: ElementDescription
   vendorName: str
   sriovNic: bool
   configParams: list[OptionDef] = []


class DynamicPassthroughInfo(TargetInfo):
   vendorName: str
   deviceName: str
   customLabel: Optional[str] = None
   vendorId: int
   deviceId: int

class EmptyIndependentFilterSpec(BaseIndependentFilterSpec):
   pass

class EmptyProfileSpec(ProfileSpec):
   pass


class FaultToleranceConfigInfo(DynamicData):
   role: int
   instanceUuids: list[str] = []
   configPaths: list[str] = []
   orphaned: Optional[bool] = None


class FaultToleranceConfigSpec(DynamicData):
   metaDataPath: Optional[FaultToleranceMetaSpec] = None
   secondaryVmSpec: Optional[FaultToleranceVMConfigSpec] = None
   metroFtEnabled: Optional[bool] = None
   metroFtHostGroup: Optional[str] = None


class FaultToleranceMetaSpec(DynamicData):
   metaDataDatastore: Datastore


class FaultTolerancePrimaryConfigInfo(FaultToleranceConfigInfo):
   secondaries: list[VirtualMachine] = []


class FaultToleranceSecondaryConfigInfo(FaultToleranceConfigInfo):
   primaryVM: VirtualMachine


class FaultToleranceSecondaryOpResult(DynamicData):
   vm: VirtualMachine
   powerOnAttempted: bool
   powerOnResult: Optional[PowerOnVmResult] = None


class FaultToleranceVMConfigSpec(DynamicData):
   class FaultToleranceDiskSpec(DynamicData):
      disk: VirtualDevice
      datastore: Datastore

   vmConfig: Optional[Datastore] = None
   disks: list[FaultToleranceDiskSpec] = []


class FeatureRequirement(DynamicData):
   key: str
   featureName: str
   value: str


class FileInfo(DynamicData):
   vmPathName: Optional[str] = None
   snapshotDirectory: Optional[str] = None
   suspendDirectory: Optional[str] = None
   logDirectory: Optional[str] = None
   ftMetadataDirectory: Optional[str] = None


class FileLayout(DynamicData):
   class DiskLayout(DynamicData):
      key: int
      diskFile: list[str] = []

   class SnapshotLayout(DynamicData):
      key: Snapshot
      snapshotFile: list[str] = []

   configFile: list[str] = []
   logFile: list[str] = []
   disk: list[DiskLayout] = []
   snapshot: list[SnapshotLayout] = []
   swapFile: Optional[str] = None


class FileLayoutEx(DynamicData):
   class FileType(Enum):
      config: ClassVar['FileType'] = 'config'
      extendedConfig: ClassVar['FileType'] = 'extendedConfig'
      diskDescriptor: ClassVar['FileType'] = 'diskDescriptor'
      diskExtent: ClassVar['FileType'] = 'diskExtent'
      digestDescriptor: ClassVar['FileType'] = 'digestDescriptor'
      digestExtent: ClassVar['FileType'] = 'digestExtent'
      diskReplicationState: ClassVar['FileType'] = 'diskReplicationState'
      log: ClassVar['FileType'] = 'log'
      stat: ClassVar['FileType'] = 'stat'
      namespaceData: ClassVar['FileType'] = 'namespaceData'
      dataSetsDiskModeStore: ClassVar['FileType'] = 'dataSetsDiskModeStore'
      dataSetsVmModeStore: ClassVar['FileType'] = 'dataSetsVmModeStore'
      nvram: ClassVar['FileType'] = 'nvram'
      snapshotData: ClassVar['FileType'] = 'snapshotData'
      snapshotMemory: ClassVar['FileType'] = 'snapshotMemory'
      snapshotList: ClassVar['FileType'] = 'snapshotList'
      snapshotManifestList: ClassVar['FileType'] = 'snapshotManifestList'
      suspend: ClassVar['FileType'] = 'suspend'
      suspendMemory: ClassVar['FileType'] = 'suspendMemory'
      swap: ClassVar['FileType'] = 'swap'
      uwswap: ClassVar['FileType'] = 'uwswap'
      core: ClassVar['FileType'] = 'core'
      screenshot: ClassVar['FileType'] = 'screenshot'
      ftMetadata: ClassVar['FileType'] = 'ftMetadata'
      guestCustomization: ClassVar['FileType'] = 'guestCustomization'

   class FileInfo(DynamicData):
      key: int
      name: str
      type: str
      size: long
      uniqueSize: Optional[long] = None
      backingObjectId: Optional[str] = None
      accessible: Optional[bool] = None

   class DiskUnit(DynamicData):
      fileKey: list[int] = []

   class DiskLayout(DynamicData):
      key: int
      virtualDiskFormat: Optional[str] = None
      chain: list[DiskUnit] = []

   class SnapshotLayout(DynamicData):
      key: Snapshot
      dataKey: int
      memoryKey: int
      disk: list[DiskLayout] = []

   file: list[FileInfo] = []
   disk: list[DiskLayout] = []
   snapshot: list[SnapshotLayout] = []
   timestamp: datetime


class FlagInfo(DynamicData):
   class HtSharing(Enum):
      any: ClassVar['HtSharing'] = 'any'
      none: ClassVar['HtSharing'] = 'none'
      internal: ClassVar['HtSharing'] = 'internal'

   class PowerOffBehavior(Enum):
      powerOff: ClassVar['PowerOffBehavior'] = 'powerOff'
      revert: ClassVar['PowerOffBehavior'] = 'revert'
      prompt: ClassVar['PowerOffBehavior'] = 'prompt'
      take: ClassVar['PowerOffBehavior'] = 'take'

   class MonitorType(Enum):
      release: ClassVar['MonitorType'] = 'release'
      debug: ClassVar['MonitorType'] = 'debug'
      stats: ClassVar['MonitorType'] = 'stats'

   class VirtualMmuUsage(Enum):
      automatic: ClassVar['VirtualMmuUsage'] = 'automatic'
      on: ClassVar['VirtualMmuUsage'] = 'on'
      off: ClassVar['VirtualMmuUsage'] = 'off'

   class VirtualExecUsage(Enum):
      hvAuto: ClassVar['VirtualExecUsage'] = 'hvAuto'
      hvOn: ClassVar['VirtualExecUsage'] = 'hvOn'
      hvOff: ClassVar['VirtualExecUsage'] = 'hvOff'

   disableAcceleration: Optional[bool] = None
   enableLogging: Optional[bool] = None
   useToe: Optional[bool] = None
   runWithDebugInfo: Optional[bool] = None
   monitorType: Optional[str] = None
   htSharing: Optional[str] = None
   snapshotDisabled: Optional[bool] = None
   snapshotLocked: Optional[bool] = None
   diskUuidEnabled: Optional[bool] = None
   virtualMmuUsage: Optional[str] = None
   virtualExecUsage: Optional[str] = None
   snapshotPowerOffBehavior: Optional[str] = None
   recordReplayEnabled: Optional[bool] = None
   faultToleranceType: Optional[str] = None
   cbrcCacheEnabled: Optional[bool] = None
   vvtdEnabled: Optional[bool] = None
   vbsEnabled: Optional[bool] = None

class FloppyInfo(TargetInfo):
   pass


class ForkConfigInfo(DynamicData):
   class ChildType(Enum):
      none: ClassVar['ChildType'] = 'none'
      persistent: ClassVar['ChildType'] = 'persistent'
      nonpersistent: ClassVar['ChildType'] = 'nonpersistent'

   parentEnabled: Optional[bool] = None
   childForkGroupId: Optional[str] = None
   parentForkGroupId: Optional[str] = None
   childType: Optional[str] = None


class GuestCustomizationManager(ManagedObject):
   def Customize(self, vm: VirtualMachine, auth: GuestAuthentication, spec: Specification, configParams: list[OptionValue]) -> Task: ...
   def StartNetwork(self, vm: VirtualMachine, auth: GuestAuthentication) -> Task: ...
   def AbortCustomization(self, vm: VirtualMachine, auth: GuestAuthentication) -> Task: ...


class GuestInfo(DynamicData):
   class ToolsStatus(Enum):
      toolsNotInstalled: ClassVar['ToolsStatus'] = 'toolsNotInstalled'
      toolsNotRunning: ClassVar['ToolsStatus'] = 'toolsNotRunning'
      toolsOld: ClassVar['ToolsStatus'] = 'toolsOld'
      toolsOk: ClassVar['ToolsStatus'] = 'toolsOk'

   class ToolsVersionStatus(Enum):
      guestToolsNotInstalled: ClassVar['ToolsVersionStatus'] = 'guestToolsNotInstalled'
      guestToolsNeedUpgrade: ClassVar['ToolsVersionStatus'] = 'guestToolsNeedUpgrade'
      guestToolsCurrent: ClassVar['ToolsVersionStatus'] = 'guestToolsCurrent'
      guestToolsUnmanaged: ClassVar['ToolsVersionStatus'] = 'guestToolsUnmanaged'
      guestToolsTooOld: ClassVar['ToolsVersionStatus'] = 'guestToolsTooOld'
      guestToolsSupportedOld: ClassVar['ToolsVersionStatus'] = 'guestToolsSupportedOld'
      guestToolsSupportedNew: ClassVar['ToolsVersionStatus'] = 'guestToolsSupportedNew'
      guestToolsTooNew: ClassVar['ToolsVersionStatus'] = 'guestToolsTooNew'
      guestToolsBlacklisted: ClassVar['ToolsVersionStatus'] = 'guestToolsBlacklisted'

   class ToolsRunningStatus(Enum):
      guestToolsNotRunning: ClassVar['ToolsRunningStatus'] = 'guestToolsNotRunning'
      guestToolsRunning: ClassVar['ToolsRunningStatus'] = 'guestToolsRunning'
      guestToolsExecutingScripts: ClassVar['ToolsRunningStatus'] = 'guestToolsExecutingScripts'

   class ToolsInstallType(Enum):
      guestToolsTypeUnknown: ClassVar['ToolsInstallType'] = 'guestToolsTypeUnknown'
      guestToolsTypeMSI: ClassVar['ToolsInstallType'] = 'guestToolsTypeMSI'
      guestToolsTypeTar: ClassVar['ToolsInstallType'] = 'guestToolsTypeTar'
      guestToolsTypeOSP: ClassVar['ToolsInstallType'] = 'guestToolsTypeOSP'
      guestToolsTypeOpenVMTools: ClassVar['ToolsInstallType'] = 'guestToolsTypeOpenVMTools'

   class GuestRebootStatus(DynamicData):
      rebootRequested: bool
      requestingComponents: list[str] = []
      requestTimestamp: Optional[datetime] = None

   class VirtualDiskMapping(DynamicData):
      key: int

   class DiskInfo(DynamicData):
      diskPath: Optional[str] = None
      capacity: Optional[long] = None
      freeSpace: Optional[long] = None
      filesystemType: Optional[str] = None
      mappings: list[VirtualDiskMapping] = []

   class NicInfo(DynamicData):
      network: Optional[str] = None
      ipAddress: list[str] = []
      macAddress: Optional[str] = None
      connected: bool
      deviceConfigId: int
      dnsConfig: Optional[DnsConfigInfo] = None
      ipConfig: Optional[IpConfigInfo] = None
      netBIOSConfig: Optional[NetBIOSConfigInfo] = None

   class StackInfo(DynamicData):
      dnsConfig: Optional[DnsConfigInfo] = None
      ipRouteConfig: Optional[IpRouteConfigInfo] = None
      ipStackConfig: list[KeyValue] = []
      dhcpConfig: Optional[DhcpConfigInfo] = None

   class ScreenInfo(DynamicData):
      width: int
      height: int

   class GuestState(Enum):
      running: ClassVar['GuestState'] = 'running'
      shuttingDown: ClassVar['GuestState'] = 'shuttingDown'
      resetting: ClassVar['GuestState'] = 'resetting'
      standby: ClassVar['GuestState'] = 'standby'
      notRunning: ClassVar['GuestState'] = 'notRunning'
      unknown: ClassVar['GuestState'] = 'unknown'

   class AppStateType(Enum):
      none: ClassVar['AppStateType'] = 'none'
      appStateOk: ClassVar['AppStateType'] = 'appStateOk'
      appStateNeedReset: ClassVar['AppStateType'] = 'appStateNeedReset'

   class NamespaceGenerationInfo(DynamicData):
      key: str
      generationNo: int

   class CustomizationStatus(Enum):
      TOOLSDEPLOYPKG_IDLE: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_IDLE'
      TOOLSDEPLOYPKG_PENDING: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_PENDING'
      TOOLSDEPLOYPKG_RUNNING: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_RUNNING'
      TOOLSDEPLOYPKG_SUCCEEDED: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_SUCCEEDED'
      TOOLSDEPLOYPKG_FAILED: ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_FAILED'

   class CustomizationInfo(DynamicData):
      customizationStatus: str
      startTime: Optional[datetime] = None
      endTime: Optional[datetime] = None
      errorMsg: Optional[str] = None

   toolsStatus: Optional[ToolsStatus] = None
   toolsVersionStatus: Optional[str] = None
   toolsVersionStatus2: Optional[str] = None
   toolsRunningStatus: Optional[str] = None
   toolsVersion: Optional[str] = None
   toolsInstallType: Optional[str] = None
   guestId: Optional[str] = None
   guestFamily: Optional[str] = None
   guestFullName: Optional[str] = None
   guestRebootStatus: Optional[GuestRebootStatus] = None
   guestDetailedData: Optional[str] = None
   hostName: Optional[str] = None
   ipAddress: Optional[str] = None
   net: list[NicInfo] = []
   ipStack: list[StackInfo] = []
   disk: list[DiskInfo] = []
   screen: Optional[ScreenInfo] = None
   guestState: str
   appHeartbeatStatus: Optional[str] = None
   guestKernelCrashed: Optional[bool] = None
   appState: Optional[str] = None
   guestOperationsReady: Optional[bool] = None
   interactiveGuestOperationsReady: Optional[bool] = None
   guestStateChangeSupported: Optional[bool] = None
   generationInfo: list[NamespaceGenerationInfo] = []
   hwVersion: Optional[str] = None
   customizationInfo: Optional[CustomizationInfo] = None


class GuestIntegrityInfo(DynamicData):
   enabled: Optional[bool] = None


class GuestMonitoringModeInfo(DynamicData):
   gmmFile: Optional[str] = None
   gmmAppliance: Optional[str] = None


class GuestOsDescriptor(DynamicData):
   class GuestOsFamily(Enum):
      windowsGuest: ClassVar['GuestOsFamily'] = 'windowsGuest'
      linuxGuest: ClassVar['GuestOsFamily'] = 'linuxGuest'
      netwareGuest: ClassVar['GuestOsFamily'] = 'netwareGuest'
      solarisGuest: ClassVar['GuestOsFamily'] = 'solarisGuest'
      darwinGuestFamily: ClassVar['GuestOsFamily'] = 'darwinGuestFamily'
      otherGuestFamily: ClassVar['GuestOsFamily'] = 'otherGuestFamily'

   class GuestArchitecture(Enum):
      x86: ClassVar['GuestArchitecture'] = 'x86'
      arm: ClassVar['GuestArchitecture'] = 'arm'

   class GuestOsIdentifier(Enum):
      dosGuest: ClassVar['GuestOsIdentifier'] = 'dosGuest'
      win31Guest: ClassVar['GuestOsIdentifier'] = 'win31Guest'
      win95Guest: ClassVar['GuestOsIdentifier'] = 'win95Guest'
      win98Guest: ClassVar['GuestOsIdentifier'] = 'win98Guest'
      winMeGuest: ClassVar['GuestOsIdentifier'] = 'winMeGuest'
      winNTGuest: ClassVar['GuestOsIdentifier'] = 'winNTGuest'
      win2000ProGuest: ClassVar['GuestOsIdentifier'] = 'win2000ProGuest'
      win2000ServGuest: ClassVar['GuestOsIdentifier'] = 'win2000ServGuest'
      win2000AdvServGuest: ClassVar['GuestOsIdentifier'] = 'win2000AdvServGuest'
      winXPHomeGuest: ClassVar['GuestOsIdentifier'] = 'winXPHomeGuest'
      winXPProGuest: ClassVar['GuestOsIdentifier'] = 'winXPProGuest'
      winXPPro64Guest: ClassVar['GuestOsIdentifier'] = 'winXPPro64Guest'
      winNetWebGuest: ClassVar['GuestOsIdentifier'] = 'winNetWebGuest'
      winNetStandardGuest: ClassVar['GuestOsIdentifier'] = 'winNetStandardGuest'
      winNetEnterpriseGuest: ClassVar['GuestOsIdentifier'] = 'winNetEnterpriseGuest'
      winNetDatacenterGuest: ClassVar['GuestOsIdentifier'] = 'winNetDatacenterGuest'
      winNetBusinessGuest: ClassVar['GuestOsIdentifier'] = 'winNetBusinessGuest'
      winNetStandard64Guest: ClassVar['GuestOsIdentifier'] = 'winNetStandard64Guest'
      winNetEnterprise64Guest: ClassVar['GuestOsIdentifier'] = 'winNetEnterprise64Guest'
      winLonghornGuest: ClassVar['GuestOsIdentifier'] = 'winLonghornGuest'
      winLonghorn64Guest: ClassVar['GuestOsIdentifier'] = 'winLonghorn64Guest'
      winNetDatacenter64Guest: ClassVar['GuestOsIdentifier'] = 'winNetDatacenter64Guest'
      winVistaGuest: ClassVar['GuestOsIdentifier'] = 'winVistaGuest'
      winVista64Guest: ClassVar['GuestOsIdentifier'] = 'winVista64Guest'
      windows7Guest: ClassVar['GuestOsIdentifier'] = 'windows7Guest'
      windows7_64Guest: ClassVar['GuestOsIdentifier'] = 'windows7_64Guest'
      windows7Server64Guest: ClassVar['GuestOsIdentifier'] = 'windows7Server64Guest'
      windows8Guest: ClassVar['GuestOsIdentifier'] = 'windows8Guest'
      windows8_64Guest: ClassVar['GuestOsIdentifier'] = 'windows8_64Guest'
      windows8Server64Guest: ClassVar['GuestOsIdentifier'] = 'windows8Server64Guest'
      windows9Guest: ClassVar['GuestOsIdentifier'] = 'windows9Guest'
      windows9_64Guest: ClassVar['GuestOsIdentifier'] = 'windows9_64Guest'
      windows9Server64Guest: ClassVar['GuestOsIdentifier'] = 'windows9Server64Guest'
      windows11_64Guest: ClassVar['GuestOsIdentifier'] = 'windows11_64Guest'
      windows12_64Guest: ClassVar['GuestOsIdentifier'] = 'windows12_64Guest'
      windowsHyperVGuest: ClassVar['GuestOsIdentifier'] = 'windowsHyperVGuest'
      windows2019srv_64Guest: ClassVar['GuestOsIdentifier'] = 'windows2019srv_64Guest'
      windows2019srvNext_64Guest: ClassVar['GuestOsIdentifier'] = 'windows2019srvNext_64Guest'
      windows2022srvNext_64Guest: ClassVar['GuestOsIdentifier'] = 'windows2022srvNext_64Guest'
      freebsdGuest: ClassVar['GuestOsIdentifier'] = 'freebsdGuest'
      freebsd64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd64Guest'
      freebsd11Guest: ClassVar['GuestOsIdentifier'] = 'freebsd11Guest'
      freebsd11_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd11_64Guest'
      freebsd12Guest: ClassVar['GuestOsIdentifier'] = 'freebsd12Guest'
      freebsd12_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd12_64Guest'
      freebsd13Guest: ClassVar['GuestOsIdentifier'] = 'freebsd13Guest'
      freebsd13_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd13_64Guest'
      freebsd14Guest: ClassVar['GuestOsIdentifier'] = 'freebsd14Guest'
      freebsd14_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd14_64Guest'
      freebsd15Guest: ClassVar['GuestOsIdentifier'] = 'freebsd15Guest'
      freebsd15_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd15_64Guest'
      redhatGuest: ClassVar['GuestOsIdentifier'] = 'redhatGuest'
      rhel2Guest: ClassVar['GuestOsIdentifier'] = 'rhel2Guest'
      rhel3Guest: ClassVar['GuestOsIdentifier'] = 'rhel3Guest'
      rhel3_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel3_64Guest'
      rhel4Guest: ClassVar['GuestOsIdentifier'] = 'rhel4Guest'
      rhel4_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel4_64Guest'
      rhel5Guest: ClassVar['GuestOsIdentifier'] = 'rhel5Guest'
      rhel5_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel5_64Guest'
      rhel6Guest: ClassVar['GuestOsIdentifier'] = 'rhel6Guest'
      rhel6_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel6_64Guest'
      rhel7Guest: ClassVar['GuestOsIdentifier'] = 'rhel7Guest'
      rhel7_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel7_64Guest'
      rhel8_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel8_64Guest'
      rhel9_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel9_64Guest'
      rhel10_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel10_64Guest'
      centosGuest: ClassVar['GuestOsIdentifier'] = 'centosGuest'
      centos64Guest: ClassVar['GuestOsIdentifier'] = 'centos64Guest'
      centos6Guest: ClassVar['GuestOsIdentifier'] = 'centos6Guest'
      centos6_64Guest: ClassVar['GuestOsIdentifier'] = 'centos6_64Guest'
      centos7Guest: ClassVar['GuestOsIdentifier'] = 'centos7Guest'
      centos7_64Guest: ClassVar['GuestOsIdentifier'] = 'centos7_64Guest'
      centos8_64Guest: ClassVar['GuestOsIdentifier'] = 'centos8_64Guest'
      centos9_64Guest: ClassVar['GuestOsIdentifier'] = 'centos9_64Guest'
      oracleLinuxGuest: ClassVar['GuestOsIdentifier'] = 'oracleLinuxGuest'
      oracleLinux64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux64Guest'
      oracleLinux6Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux6Guest'
      oracleLinux6_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux6_64Guest'
      oracleLinux7Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux7Guest'
      oracleLinux7_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux7_64Guest'
      oracleLinux8_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux8_64Guest'
      oracleLinux9_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux9_64Guest'
      oracleLinux10_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux10_64Guest'
      suseGuest: ClassVar['GuestOsIdentifier'] = 'suseGuest'
      suse64Guest: ClassVar['GuestOsIdentifier'] = 'suse64Guest'
      slesGuest: ClassVar['GuestOsIdentifier'] = 'slesGuest'
      sles64Guest: ClassVar['GuestOsIdentifier'] = 'sles64Guest'
      sles10Guest: ClassVar['GuestOsIdentifier'] = 'sles10Guest'
      sles10_64Guest: ClassVar['GuestOsIdentifier'] = 'sles10_64Guest'
      sles11Guest: ClassVar['GuestOsIdentifier'] = 'sles11Guest'
      sles11_64Guest: ClassVar['GuestOsIdentifier'] = 'sles11_64Guest'
      sles12Guest: ClassVar['GuestOsIdentifier'] = 'sles12Guest'
      sles12_64Guest: ClassVar['GuestOsIdentifier'] = 'sles12_64Guest'
      sles15_64Guest: ClassVar['GuestOsIdentifier'] = 'sles15_64Guest'
      sles16_64Guest: ClassVar['GuestOsIdentifier'] = 'sles16_64Guest'
      nld9Guest: ClassVar['GuestOsIdentifier'] = 'nld9Guest'
      oesGuest: ClassVar['GuestOsIdentifier'] = 'oesGuest'
      sjdsGuest: ClassVar['GuestOsIdentifier'] = 'sjdsGuest'
      mandrakeGuest: ClassVar['GuestOsIdentifier'] = 'mandrakeGuest'
      mandrivaGuest: ClassVar['GuestOsIdentifier'] = 'mandrivaGuest'
      mandriva64Guest: ClassVar['GuestOsIdentifier'] = 'mandriva64Guest'
      turboLinuxGuest: ClassVar['GuestOsIdentifier'] = 'turboLinuxGuest'
      turboLinux64Guest: ClassVar['GuestOsIdentifier'] = 'turboLinux64Guest'
      ubuntuGuest: ClassVar['GuestOsIdentifier'] = 'ubuntuGuest'
      ubuntu64Guest: ClassVar['GuestOsIdentifier'] = 'ubuntu64Guest'
      debian4Guest: ClassVar['GuestOsIdentifier'] = 'debian4Guest'
      debian4_64Guest: ClassVar['GuestOsIdentifier'] = 'debian4_64Guest'
      debian5Guest: ClassVar['GuestOsIdentifier'] = 'debian5Guest'
      debian5_64Guest: ClassVar['GuestOsIdentifier'] = 'debian5_64Guest'
      debian6Guest: ClassVar['GuestOsIdentifier'] = 'debian6Guest'
      debian6_64Guest: ClassVar['GuestOsIdentifier'] = 'debian6_64Guest'
      debian7Guest: ClassVar['GuestOsIdentifier'] = 'debian7Guest'
      debian7_64Guest: ClassVar['GuestOsIdentifier'] = 'debian7_64Guest'
      debian8Guest: ClassVar['GuestOsIdentifier'] = 'debian8Guest'
      debian8_64Guest: ClassVar['GuestOsIdentifier'] = 'debian8_64Guest'
      debian9Guest: ClassVar['GuestOsIdentifier'] = 'debian9Guest'
      debian9_64Guest: ClassVar['GuestOsIdentifier'] = 'debian9_64Guest'
      debian10Guest: ClassVar['GuestOsIdentifier'] = 'debian10Guest'
      debian10_64Guest: ClassVar['GuestOsIdentifier'] = 'debian10_64Guest'
      debian11Guest: ClassVar['GuestOsIdentifier'] = 'debian11Guest'
      debian11_64Guest: ClassVar['GuestOsIdentifier'] = 'debian11_64Guest'
      debian12Guest: ClassVar['GuestOsIdentifier'] = 'debian12Guest'
      debian12_64Guest: ClassVar['GuestOsIdentifier'] = 'debian12_64Guest'
      debian13Guest: ClassVar['GuestOsIdentifier'] = 'debian13Guest'
      debian13_64Guest: ClassVar['GuestOsIdentifier'] = 'debian13_64Guest'
      asianux3Guest: ClassVar['GuestOsIdentifier'] = 'asianux3Guest'
      asianux3_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux3_64Guest'
      asianux4Guest: ClassVar['GuestOsIdentifier'] = 'asianux4Guest'
      asianux4_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux4_64Guest'
      asianux5_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux5_64Guest'
      asianux7_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux7_64Guest'
      asianux8_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux8_64Guest'
      asianux9_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux9_64Guest'
      miraclelinux_64Guest: ClassVar['GuestOsIdentifier'] = 'miraclelinux_64Guest'
      pardus_64Guest: ClassVar['GuestOsIdentifier'] = 'pardus_64Guest'
      opensuseGuest: ClassVar['GuestOsIdentifier'] = 'opensuseGuest'
      opensuse64Guest: ClassVar['GuestOsIdentifier'] = 'opensuse64Guest'
      fedoraGuest: ClassVar['GuestOsIdentifier'] = 'fedoraGuest'
      fedora64Guest: ClassVar['GuestOsIdentifier'] = 'fedora64Guest'
      coreos64Guest: ClassVar['GuestOsIdentifier'] = 'coreos64Guest'
      vmwarePhoton64Guest: ClassVar['GuestOsIdentifier'] = 'vmwarePhoton64Guest'
      other24xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other24xLinuxGuest'
      other26xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other26xLinuxGuest'
      otherLinuxGuest: ClassVar['GuestOsIdentifier'] = 'otherLinuxGuest'
      other3xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other3xLinuxGuest'
      other4xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other4xLinuxGuest'
      other5xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other5xLinuxGuest'
      other6xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other6xLinuxGuest'
      other7xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other7xLinuxGuest'
      genericLinuxGuest: ClassVar['GuestOsIdentifier'] = 'genericLinuxGuest'
      other24xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other24xLinux64Guest'
      other26xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other26xLinux64Guest'
      other3xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other3xLinux64Guest'
      other4xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other4xLinux64Guest'
      other5xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other5xLinux64Guest'
      other6xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other6xLinux64Guest'
      other7xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other7xLinux64Guest'
      otherLinux64Guest: ClassVar['GuestOsIdentifier'] = 'otherLinux64Guest'
      solaris6Guest: ClassVar['GuestOsIdentifier'] = 'solaris6Guest'
      solaris7Guest: ClassVar['GuestOsIdentifier'] = 'solaris7Guest'
      solaris8Guest: ClassVar['GuestOsIdentifier'] = 'solaris8Guest'
      solaris9Guest: ClassVar['GuestOsIdentifier'] = 'solaris9Guest'
      solaris10Guest: ClassVar['GuestOsIdentifier'] = 'solaris10Guest'
      solaris10_64Guest: ClassVar['GuestOsIdentifier'] = 'solaris10_64Guest'
      solaris11_64Guest: ClassVar['GuestOsIdentifier'] = 'solaris11_64Guest'
      fusionos_64Guest: ClassVar['GuestOsIdentifier'] = 'fusionos_64Guest'
      prolinux_64Guest: ClassVar['GuestOsIdentifier'] = 'prolinux_64Guest'
      kylinlinux_64Guest: ClassVar['GuestOsIdentifier'] = 'kylinlinux_64Guest'
      flatcar_64Guest: ClassVar['GuestOsIdentifier'] = 'flatcar_64Guest'
      os2Guest: ClassVar['GuestOsIdentifier'] = 'os2Guest'
      eComStationGuest: ClassVar['GuestOsIdentifier'] = 'eComStationGuest'
      eComStation2Guest: ClassVar['GuestOsIdentifier'] = 'eComStation2Guest'
      netware4Guest: ClassVar['GuestOsIdentifier'] = 'netware4Guest'
      netware5Guest: ClassVar['GuestOsIdentifier'] = 'netware5Guest'
      netware6Guest: ClassVar['GuestOsIdentifier'] = 'netware6Guest'
      openServer5Guest: ClassVar['GuestOsIdentifier'] = 'openServer5Guest'
      openServer6Guest: ClassVar['GuestOsIdentifier'] = 'openServer6Guest'
      unixWare7Guest: ClassVar['GuestOsIdentifier'] = 'unixWare7Guest'
      darwinGuest: ClassVar['GuestOsIdentifier'] = 'darwinGuest'
      darwin64Guest: ClassVar['GuestOsIdentifier'] = 'darwin64Guest'
      darwin10Guest: ClassVar['GuestOsIdentifier'] = 'darwin10Guest'
      darwin10_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin10_64Guest'
      darwin11Guest: ClassVar['GuestOsIdentifier'] = 'darwin11Guest'
      darwin11_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin11_64Guest'
      darwin12_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin12_64Guest'
      darwin13_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin13_64Guest'
      darwin14_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin14_64Guest'
      darwin15_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin15_64Guest'
      darwin16_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin16_64Guest'
      darwin17_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin17_64Guest'
      darwin18_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin18_64Guest'
      darwin19_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin19_64Guest'
      darwin20_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin20_64Guest'
      darwin21_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin21_64Guest'
      darwin22_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin22_64Guest'
      darwin23_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin23_64Guest'
      vmkernelGuest: ClassVar['GuestOsIdentifier'] = 'vmkernelGuest'
      vmkernel5Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel5Guest'
      vmkernel6Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel6Guest'
      vmkernel65Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel65Guest'
      vmkernel7Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel7Guest'
      vmkernel8Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel8Guest'
      vmkernel9Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel9Guest'
      amazonlinux2_64Guest: ClassVar['GuestOsIdentifier'] = 'amazonlinux2_64Guest'
      amazonlinux3_64Guest: ClassVar['GuestOsIdentifier'] = 'amazonlinux3_64Guest'
      crxPod1Guest: ClassVar['GuestOsIdentifier'] = 'crxPod1Guest'
      crxSys1Guest: ClassVar['GuestOsIdentifier'] = 'crxSys1Guest'
      rockylinux_64Guest: ClassVar['GuestOsIdentifier'] = 'rockylinux_64Guest'
      almalinux_64Guest: ClassVar['GuestOsIdentifier'] = 'almalinux_64Guest'
      otherGuest: ClassVar['GuestOsIdentifier'] = 'otherGuest'
      otherGuest64: ClassVar['GuestOsIdentifier'] = 'otherGuest64'

   class FirmwareType(Enum):
      bios: ClassVar['FirmwareType'] = 'bios'
      efi: ClassVar['FirmwareType'] = 'efi'
      csm: ClassVar['FirmwareType'] = 'csm'

   class SupportLevel(Enum):
      experimental: ClassVar['SupportLevel'] = 'experimental'
      legacy: ClassVar['SupportLevel'] = 'legacy'
      terminated: ClassVar['SupportLevel'] = 'terminated'
      supported: ClassVar['SupportLevel'] = 'supported'
      unsupported: ClassVar['SupportLevel'] = 'unsupported'
      deprecated: ClassVar['SupportLevel'] = 'deprecated'
      techPreview: ClassVar['SupportLevel'] = 'techPreview'

   id: str
   family: str
   fullName: str
   supportedMaxCPUs: int
   numSupportedPhysicalSockets: int
   numSupportedCoresPerSocket: int
   supportedMinMemMB: int
   supportedMaxMemMB: int
   recommendedMemMB: int
   recommendedColorDepth: int
   supportedDiskControllerList: list[type] = []
   recommendedSCSIController: Optional[type] = None
   recommendedDiskController: type
   supportedNumDisks: int
   recommendedDiskSizeMB: int
   recommendedCdromController: type
   supportedEthernetCard: list[type] = []
   recommendedEthernetCard: Optional[type] = None
   supportsSlaveDisk: Optional[bool] = None
   cpuFeatureMask: list[CpuIdInfo] = []
   smcRequired: bool
   supportsWakeOnLan: bool
   supportsVMI: bool
   supportsMemoryHotAdd: bool
   supportsCpuHotAdd: bool
   supportsCpuHotRemove: bool
   supportedFirmware: list[str] = []
   recommendedFirmware: str
   supportedUSBControllerList: list[type] = []
   recommendedUSBController: Optional[type] = None
   supports3D: bool
   recommended3D: bool
   smcRecommended: bool
   ich7mRecommended: bool
   usbRecommended: bool
   supportLevel: str
   supportedForCreate: bool
   vRAMSizeInKB: IntOption
   numSupportedFloppyDevices: int
   wakeOnLanEthernetCard: list[type] = []
   supportsPvscsiControllerForBoot: bool
   diskUuidEnabled: bool
   supportsHotPlugPCI: bool
   supportsSecureBoot: Optional[bool] = None
   defaultSecureBoot: Optional[bool] = None
   persistentMemorySupported: Optional[bool] = None
   supportedMinPersistentMemoryMB: Optional[long] = None
   supportedMaxPersistentMemoryMB: Optional[long] = None
   recommendedPersistentMemoryMB: Optional[long] = None
   persistentMemoryHotAddSupported: Optional[bool] = None
   persistentMemoryHotRemoveSupported: Optional[bool] = None
   persistentMemoryColdGrowthSupported: Optional[bool] = None
   persistentMemoryColdGrowthGranularityMB: Optional[long] = None
   persistentMemoryHotGrowthSupported: Optional[bool] = None
   persistentMemoryHotGrowthGranularityMB: Optional[long] = None
   numRecommendedPhysicalSockets: Optional[int] = None
   numRecommendedCoresPerSocket: Optional[int] = None
   vvtdSupported: Optional[BoolOption] = None
   vbsSupported: Optional[BoolOption] = None
   vsgxSupported: Optional[BoolOption] = None
   vsgxRemoteAttestationSupported: Optional[bool] = None
   supportsTPM20: Optional[bool] = None
   recommendedTPM20: Optional[bool] = None
   vwdtSupported: Optional[bool] = None


class GuestQuiesceSpec(DynamicData):
   timeout: Optional[int] = None


class IdeDiskDeviceInfo(DiskDeviceInfo):
   class PartitionInfo(DynamicData):
      id: int
      capacity: int

   partitionTable: list[PartitionInfo] = []


class IndependentFilterSpec(BaseIndependentFilterSpec):
   filterName: str
   filterClass: Optional[str] = None
   filterCapabilities: list[KeyValue] = []


class InstantCloneSpec(DynamicData):
   name: str
   location: RelocateSpec
   config: list[OptionValue] = []
   biosUuid: Optional[str] = None


class LegacyNetworkSwitchInfo(DynamicData):
   name: str


class Message(DynamicData):
   id: str
   argument: list[object] = []
   text: Optional[str] = None


class NetworkInfo(TargetInfo):
   network: Network.Summary
   vswitch: Optional[str] = None


class NetworkShaperInfo(DynamicData):
   enabled: Optional[bool] = None
   peakBps: Optional[long] = None
   averageBps: Optional[long] = None
   burstSize: Optional[long] = None


class OpaqueNetworkInfo(TargetInfo):
   network: OpaqueNetwork.Summary
   networkReservationSupported: Optional[bool] = None

class ParallelInfo(TargetInfo):
   pass


class PciPassthroughInfo(TargetInfo):
   pciDevice: PciDevice
   systemId: str

class PciSharedGpuPassthroughInfo(TargetInfo):
   vgpu: str


class PrecisionClockInfo(TargetInfo):
   systemClockProtocol: Optional[str] = None


class ProfileDetails(DynamicData):
   class DiskProfileDetails(DynamicData):
      diskId: int
      profile: list[ProfileSpec] = []

   profile: list[ProfileSpec] = []
   diskProfileDetails: list[DiskProfileDetails] = []


class ProfileRawData(DynamicData):
   extensionKey: str
   objectData: Optional[str] = None


class ProfileSpec(DynamicData):
   pass


class PropertyRelation(DynamicData):
   key: DynamicProperty
   relations: list[DynamicProperty] = []


class QuestionInfo(DynamicData):
   id: str
   text: str
   choice: ChoiceOption
   message: list[Message] = []


class RelocateSpec(DynamicData):
   class Transformation(Enum):
      flat: ClassVar['Transformation'] = 'flat'
      sparse: ClassVar['Transformation'] = 'sparse'

   class DiskLocator(DynamicData):
      class BackingSpec(DynamicData):
         parent: Optional[BackingSpec] = None
         crypto: Optional[CryptoSpec] = None

      diskId: int
      datastore: Datastore
      diskMoveType: Optional[str] = None
      diskBackingInfo: Optional[VirtualDevice.BackingInfo] = None
      profile: list[ProfileSpec] = []
      backing: Optional[BackingSpec] = None
      filterSpec: list[BaseIndependentFilterSpec] = []

   class DiskMoveOptions(Enum):
      moveAllDiskBackingsAndAllowSharing: ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndAllowSharing'
      moveAllDiskBackingsAndDisallowSharing: ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndDisallowSharing'
      moveChildMostDiskBacking: ClassVar['DiskMoveOptions'] = 'moveChildMostDiskBacking'
      createNewChildDiskBacking: ClassVar['DiskMoveOptions'] = 'createNewChildDiskBacking'
      moveAllDiskBackingsAndConsolidate: ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndConsolidate'

   service: Optional[ServiceLocator] = None
   folder: Optional[Folder] = None
   datastore: Optional[Datastore] = None
   diskMoveType: Optional[str] = None
   pool: Optional[ResourcePool] = None
   host: Optional[HostSystem] = None
   disk: list[DiskLocator] = []
   transform: Optional[Transformation] = None
   deviceChange: list[VirtualDeviceSpec] = []
   profile: list[ProfileSpec] = []
   cryptoSpec: Optional[CryptoSpec] = None
   tagSpecs: list[TagSpec] = []
   vmPlacementPolicies: list[VmPlacementPolicy] = []


class ReplicationConfigSpec(DynamicData):
   class DiskSettings(DynamicData):
      key: int
      diskReplicationId: str

   generation: long
   vmReplicationId: str
   destination: str
   port: int
   rpo: long
   quiesceGuestEnabled: bool
   paused: bool
   oppUpdatesEnabled: bool
   netCompressionEnabled: Optional[bool] = None
   netEncryptionEnabled: Optional[bool] = None
   encryptionDestination: Optional[str] = None
   additionalEncryptionDestination: list[str] = []
   encryptionPort: Optional[int] = None
   remoteCertificateThumbprint: Optional[str] = None
   dataSetsReplicationEnabled: Optional[bool] = None
   useHbrProxyHttpPreamble: Optional[bool] = None
   disk: list[DiskSettings] = []


class RuntimeInfo(DynamicData):
   class DasProtectionState(DynamicData):
      dasProtected: bool

   device: list[DeviceRuntimeInfo] = []
   host: Optional[HostSystem] = None
   connectionState: VirtualMachine.ConnectionState
   powerState: VirtualMachine.PowerState
   vmFailoverInProgress: Optional[bool] = None
   faultToleranceState: VirtualMachine.FaultToleranceState
   dasVmProtection: Optional[DasProtectionState] = None
   toolsInstallerMounted: bool
   suspendTime: Optional[datetime] = None
   bootTime: Optional[datetime] = None
   suspendInterval: Optional[long] = None
   question: Optional[QuestionInfo] = None
   memoryOverhead: Optional[long] = None
   maxCpuUsage: Optional[int] = None
   maxMemoryUsage: Optional[int] = None
   numMksConnections: int
   recordReplayState: VirtualMachine.RecordReplayState
   cleanPowerOff: Optional[bool] = None
   needSecondaryReason: Optional[str] = None
   onlineStandby: bool
   minRequiredEVCModeKey: Optional[str] = None
   consolidationNeeded: bool
   offlineFeatureRequirement: list[FeatureRequirement] = []
   featureRequirement: list[FeatureRequirement] = []
   featureMask: list[FeatureMask] = []
   vFlashCacheAllocation: Optional[long] = None
   paused: Optional[bool] = None
   snapshotInBackground: Optional[bool] = None
   quiescedForkParent: Optional[bool] = None
   instantCloneFrozen: Optional[bool] = None
   cryptoState: Optional[str] = None
   suspendedToMemory: Optional[bool] = None
   opNotificationTimeout: Optional[long] = None
   iommuActive: Optional[bool] = None
   consolidateWorkTotal: Optional[long] = None
   consolidateWorkDone: Optional[long] = None
   diskChainBroken: Optional[bool] = None


class ScheduledHardwareUpgradeInfo(DynamicData):
   class HardwareUpgradePolicy(Enum):
      never: ClassVar['HardwareUpgradePolicy'] = 'never'
      onSoftPowerOff: ClassVar['HardwareUpgradePolicy'] = 'onSoftPowerOff'
      always: ClassVar['HardwareUpgradePolicy'] = 'always'

   class HardwareUpgradeStatus(Enum):
      none: ClassVar['HardwareUpgradeStatus'] = 'none'
      pending: ClassVar['HardwareUpgradeStatus'] = 'pending'
      success: ClassVar['HardwareUpgradeStatus'] = 'success'
      failed: ClassVar['HardwareUpgradeStatus'] = 'failed'

   upgradePolicy: Optional[str] = None
   versionKey: Optional[str] = None
   scheduledHardwareUpgradeStatus: Optional[str] = None
   fault: Optional[MethodFault] = None


class ScsiDiskDeviceInfo(DiskDeviceInfo):
   disk: Optional[ScsiDisk] = None
   transportHint: Optional[str] = None
   lunNumber: Optional[int] = None


class ScsiPassthroughInfo(TargetInfo):
   class ScsiClass(Enum):
      disk: ClassVar['ScsiClass'] = 'disk'
      tape: ClassVar['ScsiClass'] = 'tape'
      printer: ClassVar['ScsiClass'] = 'printer'
      processor: ClassVar['ScsiClass'] = 'processor'
      worm: ClassVar['ScsiClass'] = 'worm'
      cdrom: ClassVar['ScsiClass'] = 'cdrom'
      scanner: ClassVar['ScsiClass'] = 'scanner'
      optical: ClassVar['ScsiClass'] = 'optical'
      media: ClassVar['ScsiClass'] = 'media'
      com: ClassVar['ScsiClass'] = 'com'
      raid: ClassVar['ScsiClass'] = 'raid'
      unknown: ClassVar['ScsiClass'] = 'unknown'

   scsiClass: str
   vendor: str
   physicalUnitNumber: int

class SerialInfo(TargetInfo):
   pass


class SgxInfo(DynamicData):
   class FlcModes(Enum):
      locked: ClassVar['FlcModes'] = 'locked'
      unlocked: ClassVar['FlcModes'] = 'unlocked'

   epcSize: long
   flcMode: Optional[str] = None
   lePubKeyHash: Optional[str] = None
   requireAttestation: Optional[bool] = None


class SgxTargetInfo(TargetInfo):
   maxEpcSize: long
   flcModes: list[str] = []
   lePubKeyHashes: list[str] = []
   requireAttestationSupported: Optional[bool] = None


class Snapshot(ExtensibleManagedObject):
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def childSnapshot(self) -> list[Snapshot]: ...
   @property
   def vm(self) -> VirtualMachine: ...

   def Revert(self, host: Optional[HostSystem], suppressPowerOn: Optional[bool]) -> Task: ...
   def Remove(self, removeChildren: bool, consolidate: Optional[bool]) -> Task: ...
   def Rename(self, name: Optional[str], description: Optional[str]) -> None: ...
   def ExportSnapshot(self) -> HttpNfcLease: ...


class SnapshotInfo(DynamicData):
   currentSnapshot: Optional[Snapshot] = None
   rootSnapshotList: list[SnapshotTree] = []


class SnapshotSelectionSpec(DynamicData):
   retentionDays: Optional[int] = None


class SnapshotTree(DynamicData):
   snapshot: Snapshot
   vm: VirtualMachine
   name: str
   description: str
   id: int
   createTime: datetime
   state: VirtualMachine.PowerState
   quiesced: bool
   backupManifest: Optional[str] = None
   childSnapshotList: list[SnapshotTree] = []
   replaySupported: Optional[bool] = None

class SoundInfo(TargetInfo):
   pass


class SriovDevicePoolInfo(DynamicData):
   key: str


class SriovInfo(PciPassthroughInfo):
   virtualFunction: bool
   pnic: Optional[str] = None
   devicePool: Optional[SriovDevicePoolInfo] = None


class SriovNetworkDevicePoolInfo(SriovDevicePoolInfo):
   switchKey: Optional[str] = None
   switchUuid: Optional[str] = None


class StorageInfo(DynamicData):
   class UsageOnDatastore(DynamicData):
      datastore: Datastore
      committed: long
      uncommitted: long
      unshared: long

   perDatastoreUsage: list[UsageOnDatastore] = []
   timestamp: datetime


class SubnetInfo(TargetInfo):
   class FolderInfo(DynamicData):
      name: str
      folder: Folder

   id: str
   subnetFolderInfo: FolderInfo
   vpcFolderInfo: FolderInfo
   projectFolderInfo: Optional[FolderInfo] = None
   rootFolderInfo: FolderInfo


class Summary(DynamicData):
   class ConfigSummary(DynamicData):
      name: str
      template: bool
      vmPathName: str
      memorySizeMB: Optional[int] = None
      cpuReservation: Optional[int] = None
      memoryReservation: Optional[int] = None
      numCpu: Optional[int] = None
      numEthernetCards: Optional[int] = None
      numVirtualDisks: Optional[int] = None
      uuid: Optional[str] = None
      instanceUuid: Optional[str] = None
      guestId: Optional[str] = None
      guestFullName: Optional[str] = None
      annotation: Optional[str] = None
      product: Optional[ProductInfo] = None
      installBootRequired: Optional[bool] = None
      ftInfo: Optional[FaultToleranceConfigInfo] = None
      managedBy: Optional[ManagedByInfo] = None
      tpmPresent: Optional[bool] = None
      numVmiopBackings: Optional[int] = None
      hwVersion: Optional[str] = None

   class QuickStats(DynamicData):
      class MemoryTierStats(DynamicData):
         memoryTierType: str
         readBandwidth: long

      overallCpuUsage: Optional[int] = None
      overallCpuDemand: Optional[int] = None
      overallCpuReadiness: Optional[int] = None
      guestMemoryUsage: Optional[int] = None
      hostMemoryUsage: Optional[int] = None
      guestHeartbeatStatus: ManagedEntity.Status
      distributedCpuEntitlement: Optional[int] = None
      distributedMemoryEntitlement: Optional[int] = None
      staticCpuEntitlement: Optional[int] = None
      staticMemoryEntitlement: Optional[int] = None
      grantedMemory: Optional[int] = None
      privateMemory: Optional[int] = None
      sharedMemory: Optional[int] = None
      swappedMemory: Optional[int] = None
      balloonedMemory: Optional[int] = None
      consumedOverheadMemory: Optional[int] = None
      ftLogBandwidth: Optional[int] = None
      ftSecondaryLatency: Optional[int] = None
      ftLatencyStatus: Optional[ManagedEntity.Status] = None
      compressedMemory: Optional[long] = None
      uptimeSeconds: Optional[int] = None
      ssdSwappedMemory: Optional[long] = None
      activeMemory: Optional[int] = None
      memoryTierStats: list[MemoryTierStats] = []

   class GuestSummary(DynamicData):
      guestId: Optional[str] = None
      guestFullName: Optional[str] = None
      toolsStatus: Optional[GuestInfo.ToolsStatus] = None
      toolsVersionStatus: Optional[str] = None
      toolsVersionStatus2: Optional[str] = None
      toolsRunningStatus: Optional[str] = None
      hostName: Optional[str] = None
      ipAddress: Optional[str] = None
      hwVersion: Optional[str] = None

   class StorageSummary(DynamicData):
      committed: long
      uncommitted: long
      unshared: long
      timestamp: datetime

   vm: Optional[VirtualMachine] = None
   runtime: RuntimeInfo
   guest: Optional[GuestSummary] = None
   config: ConfigSummary
   storage: Optional[StorageSummary] = None
   quickStats: QuickStats
   overallStatus: ManagedEntity.Status
   customValue: list[CustomFieldsManager.Value] = []


class TargetInfo(DynamicData):
   class ConfigurationTag(Enum):
      compliant: ClassVar['ConfigurationTag'] = 'compliant'
      clusterWide: ClassVar['ConfigurationTag'] = 'clusterWide'

   name: str
   configurationTag: list[str] = []


class ToolsConfigInfo(DynamicData):
   class UpgradePolicy(Enum):
      manual: ClassVar['UpgradePolicy'] = 'manual'
      upgradeAtPowerCycle: ClassVar['UpgradePolicy'] = 'upgradeAtPowerCycle'

   class ToolsLastInstallInfo(DynamicData):
      counter: int
      fault: Optional[MethodFault] = None

   toolsVersion: Optional[int] = None
   toolsInstallType: Optional[str] = None
   afterPowerOn: Optional[bool] = None
   afterResume: Optional[bool] = None
   beforeGuestStandby: Optional[bool] = None
   beforeGuestShutdown: Optional[bool] = None
   beforeGuestReboot: Optional[bool] = None
   toolsUpgradePolicy: Optional[str] = None
   pendingCustomization: Optional[str] = None
   customizationKeyId: Optional[CryptoKeyId] = None
   syncTimeWithHostAllowed: Optional[bool] = None
   syncTimeWithHost: Optional[bool] = None
   lastInstallInfo: Optional[ToolsLastInstallInfo] = None


class UsbInfo(TargetInfo):
   class Speed(Enum):
      low: ClassVar['Speed'] = 'low'
      full: ClassVar['Speed'] = 'full'
      high: ClassVar['Speed'] = 'high'
      superSpeed: ClassVar['Speed'] = 'superSpeed'
      superSpeedPlus: ClassVar['Speed'] = 'superSpeedPlus'
      superSpeed20Gbps: ClassVar['Speed'] = 'superSpeed20Gbps'
      unknownSpeed: ClassVar['Speed'] = 'unknownSpeed'

   class Family(Enum):
      audio: ClassVar['Family'] = 'audio'
      hid: ClassVar['Family'] = 'hid'
      hid_bootable: ClassVar['Family'] = 'hid_bootable'
      physical: ClassVar['Family'] = 'physical'
      communication: ClassVar['Family'] = 'communication'
      imaging: ClassVar['Family'] = 'imaging'
      printer: ClassVar['Family'] = 'printer'
      storage: ClassVar['Family'] = 'storage'
      hub: ClassVar['Family'] = 'hub'
      smart_card: ClassVar['Family'] = 'smart_card'
      security: ClassVar['Family'] = 'security'
      video: ClassVar['Family'] = 'video'
      wireless: ClassVar['Family'] = 'wireless'
      bluetooth: ClassVar['Family'] = 'bluetooth'
      wusb: ClassVar['Family'] = 'wusb'
      pda: ClassVar['Family'] = 'pda'
      vendor_specific: ClassVar['Family'] = 'vendor_specific'
      other: ClassVar['Family'] = 'other'
      unknownFamily: ClassVar['Family'] = 'unknownFamily'

   description: str
   vendor: int
   product: int
   physicalPath: str
   family: list[str] = []
   speed: list[str] = []
   summary: Optional[Summary] = None


class UsbScanCodeSpec(DynamicData):
   class ModifierType(DynamicData):
      leftControl: Optional[bool] = None
      leftShift: Optional[bool] = None
      leftAlt: Optional[bool] = None
      leftGui: Optional[bool] = None
      rightControl: Optional[bool] = None
      rightShift: Optional[bool] = None
      rightAlt: Optional[bool] = None
      rightGui: Optional[bool] = None

   class KeyEvent(DynamicData):
      usbHidCode: int
      modifiers: Optional[ModifierType] = None

   keyEvents: list[KeyEvent] = []


class VFlashModuleInfo(TargetInfo):
   vFlashModule: VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption


class VMotionStunTimeInfo(TargetInfo):
   migrationBW: long
   stunTime: long


class VcpuConfig(DynamicData):
   latencySensitivity: Optional[LatencySensitivity] = None


class VendorDeviceGroupInfo(TargetInfo):
   class ComponentDeviceInfo(DynamicData):
      class ComponentType(Enum):
         pciPassthru: ClassVar['ComponentType'] = 'pciPassthru'
         nvidiaVgpu: ClassVar['ComponentType'] = 'nvidiaVgpu'
         sriovNic: ClassVar['ComponentType'] = 'sriovNic'
         dvx: ClassVar['ComponentType'] = 'dvx'

      type: str
      vendorName: str
      deviceName: str
      isConfigurable: bool
      device: VirtualDevice

   deviceGroupName: str
   deviceGroupDescription: Optional[str] = None
   componentDeviceInfo: list[ComponentDeviceInfo] = []


class VgpuDeviceInfo(TargetInfo):
   deviceName: str
   deviceVendorId: long
   maxFbSizeInGib: long
   timeSlicedCapable: bool
   migCapable: bool
   computeProfileCapable: bool
   quadroProfileCapable: bool


class VgpuProfileInfo(TargetInfo):
   class ProfileSharing(Enum):
      timeSliced: ClassVar['ProfileSharing'] = 'timeSliced'
      mig: ClassVar['ProfileSharing'] = 'mig'

   class ProfileClass(Enum):
      compute: ClassVar['ProfileClass'] = 'compute'
      quadro: ClassVar['ProfileClass'] = 'quadro'

   profileName: str
   deviceVendorId: long
   fbSizeInGib: long
   profileSharing: str
   profileClass: str
   stunTimeEstimates: list[VMotionStunTimeInfo] = []


class VirtualDeviceGroups(DynamicData):
   class DeviceGroup(DynamicData):
      groupInstanceKey: int
      deviceInfo: Optional[Description] = None

   class VendorDeviceGroup(DeviceGroup):
      deviceGroupName: str

   deviceGroup: list[DeviceGroup] = []


class VirtualDeviceSwap(DynamicData):
   class DeviceSwapStatus(Enum):
      none: ClassVar['DeviceSwapStatus'] = 'none'
      scheduled: ClassVar['DeviceSwapStatus'] = 'scheduled'
      inprogress: ClassVar['DeviceSwapStatus'] = 'inprogress'
      failed: ClassVar['DeviceSwapStatus'] = 'failed'
      completed: ClassVar['DeviceSwapStatus'] = 'completed'

   class DeviceSwapInfo(DynamicData):
      enabled: Optional[bool] = None
      applicable: Optional[bool] = None
      status: Optional[str] = None

   lsiToPvscsi: Optional[DeviceSwapInfo] = None


class VirtualHardware(DynamicData):
   class MotherboardLayout(Enum):
      i440bxHostBridge: ClassVar['MotherboardLayout'] = 'i440bxHostBridge'
      acpiHostBridges: ClassVar['MotherboardLayout'] = 'acpiHostBridges'

   numCPU: int
   numCoresPerSocket: Optional[int] = None
   autoCoresPerSocket: Optional[bool] = None
   memoryMB: int
   virtualICH7MPresent: Optional[bool] = None
   virtualSMCPresent: Optional[bool] = None
   device: list[VirtualDevice] = []
   motherboardLayout: Optional[str] = None
   simultaneousThreads: Optional[int] = None


class VirtualHardwareOption(DynamicData):
   hwVersion: int
   virtualDeviceOption: list[VirtualDeviceOption] = []
   deviceListReadonly: bool
   numCPU: list[int] = []
   numCoresPerSocket: IntOption
   autoCoresPerSocket: Optional[BoolOption] = None
   numCpuReadonly: bool
   memoryMB: LongOption
   numPCIControllers: IntOption
   numIDEControllers: IntOption
   numUSBControllers: IntOption
   numUSBXHCIControllers: IntOption
   numSIOControllers: IntOption
   numPS2Controllers: IntOption
   licensingLimit: list[PropertyPath] = []
   numSupportedWwnPorts: Optional[IntOption] = None
   numSupportedWwnNodes: Optional[IntOption] = None
   resourceConfigOption: ResourceConfigOption
   numNVDIMMControllers: Optional[IntOption] = None
   numTPMDevices: Optional[IntOption] = None
   numWDTDevices: Optional[IntOption] = None
   numPrecisionClockDevices: Optional[IntOption] = None
   epcMemoryMB: Optional[LongOption] = None
   acpiHostBridgesFirmware: list[str] = []
   numCpuSimultaneousThreads: Optional[IntOption] = None
   numNumaNodes: Optional[IntOption] = None
   numDeviceGroups: Optional[IntOption] = None
   deviceGroupTypes: list[type] = []


class VirtualNuma(DynamicData):
   coresPerNumaNode: Optional[int] = None
   exposeVnumaOnCpuHotadd: Optional[bool] = None


class VirtualNumaInfo(DynamicData):
   coresPerNumaNode: Optional[int] = None
   autoCoresPerNumaNode: Optional[bool] = None
   vnumaOnCpuHotaddExposed: Optional[bool] = None


class VirtualPMem(DynamicData):
   class SnapshotMode(Enum):
      independent_persistent: ClassVar['SnapshotMode'] = 'independent_persistent'
      independent_eraseonrevert: ClassVar['SnapshotMode'] = 'independent_eraseonrevert'

   snapshotMode: Optional[str] = None


class VmImportSpec(ImportSpec):
   configSpec: ConfigSpec
   resPoolEntity: Optional[ResourcePool] = None


class VmPlacementPolicy(DynamicData):
   class VmPlacementPolicyStrictness(Enum):
      PreferredDuringPlacementPreferredDuringExecution: ClassVar['VmPlacementPolicyStrictness'] = 'PreferredDuringPlacementPreferredDuringExecution'
      RequiredDuringPlacementPreferredDuringExecution: ClassVar['VmPlacementPolicyStrictness'] = 'RequiredDuringPlacementPreferredDuringExecution'

   class VmPlacementPolicyTopology(Enum):
      Host: ClassVar['VmPlacementPolicyTopology'] = 'Host'
      ClusterComputeResource: ClassVar['VmPlacementPolicyTopology'] = 'ClusterComputeResource'
      VSphereZone: ClassVar['VmPlacementPolicyTopology'] = 'VSphereZone'


class VmToVmGroupsAntiAffinity(VmPlacementPolicy):
   selfTag: Optional[TagId] = None
   antiAffinedVmGroupTags: list[TagId] = []
   policyStrictness: Optional[str] = None
   policyTopology: Optional[str] = None


class VmVmAffinity(VmPlacementPolicy):
   affinedVmsTag: TagId
   policyStrictness: Optional[str] = None
   policyTopology: Optional[str] = None


class VmVmAntiAffinity(VmPlacementPolicy):
   antiAffinedVmsTag: TagId
   policyStrictness: Optional[str] = None
   policyTopology: Optional[str] = None


class WindowsQuiesceSpec(GuestQuiesceSpec):
   class VssBackupContext(Enum):
      ctx_auto: ClassVar['VssBackupContext'] = 'ctx_auto'
      ctx_backup: ClassVar['VssBackupContext'] = 'ctx_backup'
      ctx_file_share_backup: ClassVar['VssBackupContext'] = 'ctx_file_share_backup'

   vssBackupType: Optional[int] = None
   vssBootableSystemState: Optional[bool] = None
   vssPartialFileSupport: Optional[bool] = None
   vssBackupContext: Optional[str] = None
