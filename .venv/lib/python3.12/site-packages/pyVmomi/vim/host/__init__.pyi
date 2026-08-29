# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import byte
from pyVmomi.VmomiSupport import long
from pyVmomi.VmomiSupport import short

from pyVmomi.vim import AboutInfo

from pyVmomi.vim import AuthorizationManager

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vim import ComputeResource
from pyVmomi.vim import CustomFieldsManager

from pyVmomi.vim import Datastore

from pyVmomi.vim import ElementDescription

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim import FaultsByHost
from pyVmomi.vim import FaultsByVM

from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import IoFilterManager

from pyVmomi.vim import KeyValue

from pyVmomi.vim import LicenseManager
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network

from pyVmomi.vim import OpaqueNetwork

from pyVmomi.vim import ResourceConfigSpec

from pyVmomi.vim import Task
from pyVmomi.vim import UserDirectory
from pyVmomi.vim import VasaStorageArray
from pyVmomi.vim import VimVasaProviderInfo

from pyVmomi.vim import VirtualDiskManager

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.cluster import DasFdmHostState

from pyVmomi.vim.cluster import StorageComplianceResult

from pyVmomi.vim.cluster import VsanHostCreateVmHealthTestResult

from pyVmomi.vim.dvs import HostMember

from pyVmomi.vim.dvs import PortConnection

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.encryption import CryptoManager

from pyVmomi.vim.option import ChoiceOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.option import OptionDef

from pyVmomi.vim.option import OptionManager
from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vm import DynamicPassthroughInfo

from pyVmomi.vim.vm import Summary
from pyVmomi.vim.vm import VendorDeviceGroupInfo

from pyVmomi.vim.vm import VgpuDeviceInfo
from pyVmomi.vim.vm import VgpuProfileInfo

from pyVmomi.vim.vsan import VsanDownloadItem

from pyVmomi.vim.vsan import VsanHclDriverInfo

from pyVmomi.vim.vsan import VsanPrepareVsanForVcsaSpec

from pyVmomi.vim.vsan import VsanSpaceEfficiencyMetadataSize
from pyVmomi.vim.vsan import VsanVcPostDeployConfigSpec
from pyVmomi.vim.vsan import VsanVcsaDeploymentProgress

from pyVmomi.vim.vsan import VsanVibInstallPreflightStatus
from pyVmomi.vim.vsan import VsanVibScanResult
from pyVmomi.vim.vsan import VsanVibSpec

from pyVmomi.vim.vm.device import VirtualDisk

from pyVmomi.vim.vsan.host import AbortWipeDiskStatus
from pyVmomi.vim.vsan.host import AboutInfoEx

from pyVmomi.vim.vsan.host import ClusterStatus
from pyVmomi.vim.vsan.host import ConfigInfo

from pyVmomi.vim.vsan.host import DataInTransitEncryptionInfo

from pyVmomi.vim.vsan.host import DecommissionMode
from pyVmomi.vim.vsan.host import DiskMapping
from pyVmomi.vim.vsan.host import DiskResult
from pyVmomi.vim.vsan.host import DrsStats

from pyVmomi.vim.vsan.host import EncryptionInfo
from pyVmomi.vim.vsan.host import RuntimeStats

from pyVmomi.vim.vsan.host import VsanDiskInfo

from pyVmomi.vim.vsan.host import VsanRuntimeInfo
from pyVmomi.vim.vsan.host import VsanSyncingObjectQueryResult
from pyVmomi.vim.vsan.host import VsanWhatIfEvacResult
from pyVmomi.vim.vsan.host import WipeDiskStatus



class ActiveDirectoryAuthentication(DirectoryStore):
   class CertificateDigest(Enum):
      SHA1: ClassVar['CertificateDigest'] = 'SHA1'

   def JoinDomain(self, domainName: str, userName: str, password: str) -> Task: ...
   def JoinDomainWithCAM(self, domainName: str, camServer: str) -> Task: ...
   def ImportCertificateForCAM(self, certPath: str, camServer: str) -> Task: ...
   def LeaveCurrentDomain(self, force: bool) -> Task: ...
   def EnableSmartCardAuthentication(self) -> None: ...
   def InstallSmartCardTrustAnchor(self, cert: str) -> None: ...
   def ReplaceSmartCardTrustAnchors(self, certs: list[str]) -> None: ...
   def RemoveSmartCardTrustAnchor(self, issuer: str, serial: str) -> None: ...
   def RemoveSmartCardTrustAnchorByFingerprint(self, fingerprint: str, digest: str) -> None: ...
   def RemoveSmartCardTrustAnchorCertificate(self, certificate: str) -> None: ...
   def ListSmartCardTrustAnchors(self) -> list[str]: ...
   def DisableSmartCardAuthentication(self) -> None: ...


class ActiveDirectoryInfo(DirectoryStoreInfo):
   class DomainMembershipStatus(Enum):
      unknown: ClassVar['DomainMembershipStatus'] = 'unknown'
      ok: ClassVar['DomainMembershipStatus'] = 'ok'
      noServers: ClassVar['DomainMembershipStatus'] = 'noServers'
      clientTrustBroken: ClassVar['DomainMembershipStatus'] = 'clientTrustBroken'
      serverTrustBroken: ClassVar['DomainMembershipStatus'] = 'serverTrustBroken'
      inconsistentTrust: ClassVar['DomainMembershipStatus'] = 'inconsistentTrust'
      otherProblem: ClassVar['DomainMembershipStatus'] = 'otherProblem'

   joinedDomain: Optional[str] = None
   trustedDomain: list[str] = []
   domainMembershipStatus: Optional[str] = None
   smartCardAuthenticationEnabled: Optional[bool] = None


class ActiveDirectorySpec(DynamicData):
   class Specification(DynamicData):
      domainName: Optional[str] = None
      userName: Optional[str] = None
      password: Optional[str] = None
      camServer: Optional[str] = None
      thumbprint: Optional[str] = None
      certificate: Optional[str] = None
      smartCardAuthenticationEnabled: Optional[bool] = None
      smartCardTrustAnchors: list[str] = []

   changeOperation: str
   spec: Optional[Specification] = None


class AssignableHardwareBinding(DynamicData):
   instanceId: str
   vm: VirtualMachine
   pciId: Optional[str] = None
   deviceKey: Optional[int] = None


class AssignableHardwareConfig(DynamicData):
   class AttributeOverride(DynamicData):
      instanceId: str
      name: str
      value: Optional[object] = None

   attributeOverride: list[AttributeOverride] = []


class AssignableHardwareManager(ManagedObject):
   @property
   def binding(self) -> list[AssignableHardwareBinding]: ...
   @property
   def config(self) -> AssignableHardwareConfig: ...

   def DownloadDescriptionTree(self) -> binary: ...
   def RetrieveDynamicPassthroughInfo(self) -> list[DynamicPassthroughInfo]: ...
   def RetrieveVendorDeviceGroupInfo(self) -> list[VendorDeviceGroupInfo]: ...
   def UpdateConfig(self, config: AssignableHardwareConfig) -> None: ...


class AuthenticationInfo(DynamicData):
   principal: str
   ownerTag: str
   sslCertificates: list[str] = []


class AuthenticationManager(ManagedObject):
   @property
   def info(self) -> AuthenticationManagerInfo: ...
   @property
   def supportedStore(self) -> list[AuthenticationStore]: ...


class AuthenticationManagerInfo(DynamicData):
   authConfig: list[AuthenticationStoreInfo] = []


class AuthenticationStore(ManagedObject):
   @property
   def info(self) -> AuthenticationStoreInfo: ...


class AuthenticationStoreInfo(DynamicData):
   enabled: bool


class AutoStartManager(ManagedObject):
   class Action(Enum):
      none: ClassVar['Action'] = 'none'
      systemDefault: ClassVar['Action'] = 'systemDefault'
      powerOn: ClassVar['Action'] = 'powerOn'
      powerOff: ClassVar['Action'] = 'powerOff'
      guestShutdown: ClassVar['Action'] = 'guestShutdown'
      suspend: ClassVar['Action'] = 'suspend'

   class SystemDefaults(DynamicData):
      enabled: Optional[bool] = None
      startDelay: Optional[int] = None
      stopDelay: Optional[int] = None
      waitForHeartbeat: Optional[bool] = None
      stopAction: Optional[str] = None

   class AutoPowerInfo(DynamicData):
      class WaitHeartbeatSetting(Enum):
         yes: ClassVar['WaitHeartbeatSetting'] = 'yes'
         no: ClassVar['WaitHeartbeatSetting'] = 'no'
         systemDefault: ClassVar['WaitHeartbeatSetting'] = 'systemDefault'

      key: VirtualMachine
      startOrder: int
      startDelay: int
      waitForHeartbeat: WaitHeartbeatSetting
      startAction: str
      stopDelay: int
      stopAction: str

   class Config(DynamicData):
      defaults: Optional[SystemDefaults] = None
      powerInfo: list[AutoPowerInfo] = []

   @property
   def config(self) -> Config: ...

   def Reconfigure(self, spec: Config) -> None: ...
   def AutoPowerOn(self) -> None: ...
   def AutoPowerOff(self) -> None: ...


class BIOSInfo(DynamicData):
   class FirmwareType(Enum):
      BIOS: ClassVar['FirmwareType'] = 'BIOS'
      UEFI: ClassVar['FirmwareType'] = 'UEFI'

   biosVersion: Optional[str] = None
   releaseDate: Optional[datetime] = None
   vendor: Optional[str] = None
   majorRelease: Optional[int] = None
   minorRelease: Optional[int] = None
   firmwareMajorRelease: Optional[int] = None
   firmwareMinorRelease: Optional[int] = None
   firmwareType: Optional[str] = None

class BlockAdapterTargetTransport(TargetTransport):
   pass

class BlockHba(HostBusAdapter):
   pass


class BootDeviceInfo(DynamicData):
   bootDevices: list[BootDeviceSystem.BootDevice] = []
   currentBootDeviceKey: Optional[str] = None


class BootDeviceSystem(ManagedObject):
   class BootDevice(DynamicData):
      key: str
      description: str

   def QueryBootDevices(self) -> Optional[BootDeviceInfo]: ...
   def UpdateBootDevice(self, key: str) -> None: ...


class CacheConfigurationManager(ManagedObject):
   class CacheConfigurationSpec(DynamicData):
      datastore: Datastore
      swapSize: long

   class CacheConfigurationInfo(DynamicData):
      key: Datastore
      swapSize: long

   @property
   def cacheConfigurationInfo(self) -> list[CacheConfigurationInfo]: ...

   def ConfigureCache(self, spec: CacheConfigurationSpec) -> Task: ...


class Capability(DynamicData):
   class ReplayUnsupportedReason(Enum):
      incompatibleProduct: ClassVar['ReplayUnsupportedReason'] = 'incompatibleProduct'
      incompatibleCpu: ClassVar['ReplayUnsupportedReason'] = 'incompatibleCpu'
      hvDisabled: ClassVar['ReplayUnsupportedReason'] = 'hvDisabled'
      cpuidLimitSet: ClassVar['ReplayUnsupportedReason'] = 'cpuidLimitSet'
      oldBIOS: ClassVar['ReplayUnsupportedReason'] = 'oldBIOS'
      unknown: ClassVar['ReplayUnsupportedReason'] = 'unknown'

   class FtUnsupportedReason(Enum):
      vMotionNotLicensed: ClassVar['FtUnsupportedReason'] = 'vMotionNotLicensed'
      missingVMotionNic: ClassVar['FtUnsupportedReason'] = 'missingVMotionNic'
      missingFTLoggingNic: ClassVar['FtUnsupportedReason'] = 'missingFTLoggingNic'
      ftNotLicensed: ClassVar['FtUnsupportedReason'] = 'ftNotLicensed'
      haAgentIssue: ClassVar['FtUnsupportedReason'] = 'haAgentIssue'
      unsupportedProduct: ClassVar['FtUnsupportedReason'] = 'unsupportedProduct'
      cpuHvUnsupported: ClassVar['FtUnsupportedReason'] = 'cpuHvUnsupported'
      cpuHwmmuUnsupported: ClassVar['FtUnsupportedReason'] = 'cpuHwmmuUnsupported'
      cpuHvDisabled: ClassVar['FtUnsupportedReason'] = 'cpuHvDisabled'

   class DRTMTypes(Enum):
      none: ClassVar['DRTMTypes'] = 'none'
      intelTxt: ClassVar['DRTMTypes'] = 'intelTxt'
      amdSkinit: ClassVar['DRTMTypes'] = 'amdSkinit'

   class VmDirectPathGen2UnsupportedReason(Enum):
      hostNptIncompatibleProduct: ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptIncompatibleProduct'
      hostNptIncompatibleHardware: ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptIncompatibleHardware'
      hostNptDisabled: ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptDisabled'

   class UnmapMethodSupported(Enum):
      priority: ClassVar['UnmapMethodSupported'] = 'priority'
      fixed: ClassVar['UnmapMethodSupported'] = 'fixed'
      dynamic: ClassVar['UnmapMethodSupported'] = 'dynamic'

   recursiveResourcePoolsSupported: bool
   cpuMemoryResourceConfigurationSupported: bool
   rebootSupported: bool
   shutdownSupported: bool
   vmotionSupported: bool
   standbySupported: bool
   ipmiSupported: Optional[bool] = None
   maxSupportedVMs: Optional[int] = None
   maxRunningVMs: Optional[int] = None
   maxSupportedVcpus: Optional[int] = None
   maxRegisteredVMs: Optional[int] = None
   datastorePrincipalSupported: bool
   sanSupported: bool
   nfsSupported: bool
   iscsiSupported: bool
   vlanTaggingSupported: bool
   nicTeamingSupported: bool
   highGuestMemSupported: bool
   maintenanceModeSupported: bool
   suspendedRelocateSupported: bool
   restrictedSnapshotRelocateSupported: bool
   perVmSwapFiles: bool
   localSwapDatastoreSupported: bool
   unsharedSwapVMotionSupported: bool
   backgroundSnapshotsSupported: bool
   preAssignedPCIUnitNumbersSupported: bool
   screenshotSupported: bool
   scaledScreenshotSupported: bool
   storageVMotionSupported: bool
   vmotionWithStorageVMotionSupported: bool
   vmotionAcrossNetworkSupported: Optional[bool] = None
   maxNumDisksSVMotion: Optional[int] = None
   maxVirtualDiskDescVersionSupported: Optional[int] = None
   hbrNicSelectionSupported: bool
   vrNfcNicSelectionSupported: bool
   recordReplaySupported: bool
   ftSupported: bool
   replayUnsupportedReason: Optional[str] = None
   replayCompatibilityIssues: list[str] = []
   smpFtSupported: bool
   ftCompatibilityIssues: list[str] = []
   smpFtCompatibilityIssues: list[str] = []
   maxVcpusPerFtVm: Optional[int] = None
   loginBySSLThumbprintSupported: Optional[bool] = None
   cloneFromSnapshotSupported: bool
   deltaDiskBackingsSupported: bool
   perVMNetworkTrafficShapingSupported: bool
   tpmSupported: bool
   tpmVersion: Optional[str] = None
   txtEnabled: Optional[bool] = None
   drtmType: Optional[str] = None
   supportedCpuFeature: list[CpuIdInfo] = []
   virtualExecUsageSupported: bool
   storageIORMSupported: bool
   vmDirectPathGen2Supported: Optional[bool] = None
   vmDirectPathGen2UnsupportedReason: list[str] = []
   vmDirectPathGen2UnsupportedReasonExtended: Optional[str] = None
   supportedVmfsMajorVersion: list[int] = []
   vStorageCapable: bool
   snapshotRelayoutSupported: bool
   firewallIpRulesSupported: Optional[bool] = None
   servicePackageInfoSupported: Optional[bool] = None
   maxHostRunningVms: Optional[int] = None
   maxHostSupportedVcpus: Optional[int] = None
   vmfsDatastoreMountCapable: bool
   eightPlusHostVmfsSharedAccessSupported: bool
   nestedHVSupported: bool
   vPMCSupported: bool
   interVMCommunicationThroughVMCISupported: bool
   scheduledHardwareUpgradeSupported: Optional[bool] = None
   featureCapabilitiesSupported: bool
   latencySensitivitySupported: bool
   storagePolicySupported: Optional[bool] = None
   accel3dSupported: bool
   reliableMemoryAware: Optional[bool] = None
   multipleNetworkStackInstanceSupported: Optional[bool] = None
   messageBusProxySupported: Optional[bool] = None
   vsanSupported: Optional[bool] = None
   vFlashSupported: Optional[bool] = None
   hostAccessManagerSupported: Optional[bool] = None
   provisioningNicSelectionSupported: bool
   nfs41Supported: Optional[bool] = None
   nfs41Krb5iSupported: Optional[bool] = None
   turnDiskLocatorLedSupported: Optional[bool] = None
   virtualVolumeDatastoreSupported: Optional[bool] = None
   markAsSsdSupported: Optional[bool] = None
   markAsLocalSupported: Optional[bool] = None
   smartCardAuthenticationSupported: Optional[bool] = None
   pMemSupported: Optional[bool] = None
   pMemSnapshotSupported: Optional[bool] = None
   cryptoSupported: Optional[bool] = None
   oneKVolumeAPIsSupported: Optional[bool] = None
   gatewayOnNicSupported: Optional[bool] = None
   upitSupported: Optional[bool] = None
   cpuHwMmuSupported: Optional[bool] = None
   encryptedVMotionSupported: Optional[bool] = None
   encryptionChangeOnAddRemoveSupported: Optional[bool] = None
   encryptionHotOperationSupported: Optional[bool] = None
   encryptionWithSnapshotsSupported: Optional[bool] = None
   encryptionFaultToleranceSupported: Optional[bool] = None
   encryptionMemorySaveSupported: Optional[bool] = None
   encryptionRDMSupported: Optional[bool] = None
   encryptionVFlashSupported: Optional[bool] = None
   encryptionCBRCSupported: Optional[bool] = None
   encryptionHBRSupported: Optional[bool] = None
   ftEfiSupported: Optional[bool] = None
   unmapMethodSupported: Optional[str] = None
   maxMemMBPerFtVm: Optional[int] = None
   virtualMmuUsageIgnored: Optional[bool] = None
   virtualExecUsageIgnored: Optional[bool] = None
   vmCreateDateSupported: Optional[bool] = None
   vmfs3EOLSupported: Optional[bool] = None
   ftVmcpSupported: Optional[bool] = None
   quickBootSupported: Optional[bool] = None
   encryptedFtSupported: Optional[bool] = None
   assignableHardwareSupported: Optional[bool] = None
   suspendToMemorySupported: Optional[bool] = None
   useFeatureReqsForOldHWv: Optional[bool] = None
   markPerenniallyReservedSupported: Optional[bool] = None
   hppPspSupported: Optional[bool] = None
   deviceRebindWithoutRebootSupported: Optional[bool] = None
   storagePolicyChangeSupported: Optional[bool] = None
   precisionTimeProtocolSupported: Optional[bool] = None
   remoteDeviceVMotionSupported: Optional[bool] = None
   maxSupportedVmMemory: Optional[int] = None
   ahDeviceHintsSupported: Optional[bool] = None
   nvmeOverTcpSupported: Optional[bool] = None
   nvmeStorageFabricServicesSupported: Optional[bool] = None
   assignHwPciConfigSupported: Optional[bool] = None
   timeConfigSupported: Optional[bool] = None
   nvmeBatchOperationsSupported: Optional[bool] = None
   pMemFailoverSupported: Optional[bool] = None
   hostConfigEncryptionSupported: Optional[bool] = None
   maxSupportedSimultaneousThreads: Optional[int] = None
   ptpConfigSupported: Optional[bool] = None
   maxSupportedPtpPorts: Optional[int] = None
   sgxRegistrationSupported: Optional[bool] = None
   pMemIndependentSnapshotSupported: Optional[bool] = None
   iommuSLDirtyCapable: Optional[bool] = None
   vmknicBindingSupported: Optional[bool] = None
   ultralowFixedUnmapSupported: Optional[bool] = None
   nvmeVvolSupported: Optional[bool] = None
   fptHotplugSupported: Optional[bool] = None
   mconnectSupported: Optional[bool] = None
   vsanNicMgmtSupported: Optional[bool] = None
   vvolNQNSupported: Optional[bool] = None
   stretchedSCSupported: Optional[bool] = None
   vmknicBindingOnNFSv41: Optional[bool] = None
   vpStatusCheckSupported: Optional[bool] = None
   e2e4knSupported: Optional[bool] = None
   vsanDedicatedVmkNicSupported: Optional[bool] = None
   nConnectSupported: Optional[bool] = None
   userKeySupported: Optional[bool] = None
   ndcmSupported: Optional[bool] = None
   uefiSecureBoot: Optional[bool] = None
   vpxdVmxGenerationSupported: Optional[bool] = None
   nfs41Krb5pSupported: Optional[bool] = None
   cimSupported: Optional[bool] = None
   npivSupported: Optional[bool] = None
   entitlementSupported: Optional[bool] = None
   monitorUnrestricted: Optional[bool] = None
   vnetworkingNicSelectionSupported: Optional[bool] = None
   directPathInfoSupported: Optional[bool] = None
   fcdLinkedCloneSupported: Optional[bool] = None
   ehvQuickBootSupported: Optional[bool] = None
   nestedHvTieringEnabled: Optional[bool] = None


class CertificateManager(ManagedObject):
   class CertificateKind(Enum):
      Machine: ClassVar['CertificateKind'] = 'Machine'
      VASAClient: ClassVar['CertificateKind'] = 'VASAClient'

   class CryptoAlgorithm(Enum):
      RSA_2048: ClassVar['CryptoAlgorithm'] = 'RSA_2048'
      RSA_3072: ClassVar['CryptoAlgorithm'] = 'RSA_3072'
      RSA_4096: ClassVar['CryptoAlgorithm'] = 'RSA_4096'

   class CertificateSpec(DynamicData):
      kind: str
      subjectAlternativeNames: list[str] = []
      cryptoAlgorithm: Optional[str] = None

   class CertificateInfo(DynamicData):
      class CertificateStatus(Enum):
         unknown: ClassVar['CertificateStatus'] = 'unknown'
         expired: ClassVar['CertificateStatus'] = 'expired'
         expiring: ClassVar['CertificateStatus'] = 'expiring'
         expiringShortly: ClassVar['CertificateStatus'] = 'expiringShortly'
         expirationImminent: ClassVar['CertificateStatus'] = 'expirationImminent'
         good: ClassVar['CertificateStatus'] = 'good'

      kind: Optional[str] = None
      issuer: Optional[str] = None
      notBefore: Optional[datetime] = None
      notAfter: Optional[datetime] = None
      subject: Optional[str] = None
      status: str

   @property
   def certificateInfo(self) -> CertificateInfo: ...

   def RetrieveCertificateInfoList(self) -> list[CertificateInfo]: ...
   def GenerateCertificateSigningRequest(self, useIpAddressAsCommonName: bool, spec: Optional[CertificateSpec]) -> str: ...
   def GenerateCertificateSigningRequestByDn(self, distinguishedName: str, spec: Optional[CertificateSpec]) -> str: ...
   def ProvisionServerPrivateKey(self, key: str) -> None: ...
   def InstallServerCertificate(self, cert: str) -> None: ...
   def ReplaceCACertificatesAndCRLs(self, caCert: list[str], caCrl: list[str]) -> None: ...
   def NotifyAffectedServices(self, services: list[str]) -> None: ...
   def ListCACertificates(self) -> list[str]: ...
   def ListCACertificateRevocationLists(self) -> list[str]: ...


class ConfigChange(DynamicData):
   class Mode(Enum):
      modify: ClassVar['Mode'] = 'modify'
      replace: ClassVar['Mode'] = 'replace'

   class Operation(Enum):
      add: ClassVar['Operation'] = 'add'
      remove: ClassVar['Operation'] = 'remove'
      edit: ClassVar['Operation'] = 'edit'
      ignore: ClassVar['Operation'] = 'ignore'

   class Owner(Enum):
      NSX: ClassVar['Owner'] = 'NSX'
      VSAN: ClassVar['Owner'] = 'VSAN'


class ConfigInfo(DynamicData):
   host: HostSystem
   product: AboutInfo
   deploymentInfo: Optional[DeploymentInfo] = None
   hyperThread: Optional[CpuSchedulerSystem.HyperThreadScheduleInfo] = None
   cpuScheduler: Optional[CpuSchedulerSystem.CpuSchedulerInfo] = None
   consoleReservation: Optional[MemoryManagerSystem.ServiceConsoleReservationInfo] = None
   virtualMachineReservation: Optional[MemoryManagerSystem.VirtualMachineReservationInfo] = None
   storageDevice: Optional[StorageDeviceInfo] = None
   multipathState: Optional[MultipathStateInfo] = None
   fileSystemVolume: Optional[FileSystemVolumeInfo] = None
   systemFile: list[str] = []
   network: Optional[NetworkInfo] = None
   vmotion: Optional[VMotionInfo] = None
   virtualNicManagerInfo: Optional[VirtualNicManagerInfo] = None
   capabilities: Optional[NetCapabilities] = None
   datastoreCapabilities: Optional[DatastoreSystem.Capabilities] = None
   offloadCapabilities: Optional[NetOffloadCapabilities] = None
   service: Optional[ServiceInfo] = None
   firewall: Optional[FirewallInfo] = None
   autoStart: Optional[AutoStartManager.Config] = None
   activeDiagnosticPartition: Optional[DiagnosticPartition] = None
   option: list[OptionValue] = []
   optionDef: list[OptionDef] = []
   datastorePrincipal: Optional[str] = None
   localSwapDatastore: Optional[Datastore] = None
   systemSwapConfiguration: Optional[SystemSwapConfiguration] = None
   systemResources: Optional[SystemResourceInfo] = None
   dateTimeInfo: Optional[DateTimeInfo] = None
   flags: Optional[FlagInfo] = None
   adminDisabled: Optional[bool] = None
   lockdownMode: Optional[HostAccessManager.LockdownMode] = None
   ipmi: Optional[IpmiInfo] = None
   sslThumbprintInfo: Optional[SslThumbprintInfo] = None
   sslThumbprintData: list[SslThumbprintInfo] = []
   authenticationData: list[AuthenticationInfo] = []
   certificate: list[byte] = []
   pciPassthruInfo: list[PciPassthruInfo] = []
   authenticationManagerInfo: Optional[AuthenticationManagerInfo] = None
   featureVersion: list[FeatureVersionInfo] = []
   powerSystemCapability: Optional[PowerSystem.Capability] = None
   powerSystemInfo: Optional[PowerSystem.Info] = None
   cacheConfigurationInfo: list[CacheConfigurationManager.CacheConfigurationInfo] = []
   wakeOnLanCapable: Optional[bool] = None
   featureCapability: list[FeatureCapability] = []
   maskedFeatureCapability: list[FeatureCapability] = []
   vFlashConfigInfo: Optional[VFlashManager.VFlashConfigInfo] = None
   vsanHostConfig: Optional[ConfigInfo] = None
   domainList: list[str] = []
   scriptCheckSum: Optional[binary] = None
   hostConfigCheckSum: Optional[binary] = None
   descriptionTreeCheckSum: Optional[binary] = None
   graphicsInfo: list[GraphicsInfo] = []
   sharedPassthruGpuTypes: list[str] = []
   graphicsConfig: Optional[GraphicsConfig] = None
   sharedGpuCapabilities: list[SharedGpuCapabilities] = []
   ioFilterInfo: list[IoFilterManager.HostIoFilterInfo] = []
   sriovDevicePool: list[SriovDevicePoolInfo] = []
   assignableHardwareBinding: list[AssignableHardwareBinding] = []
   assignableHardwareConfig: Optional[AssignableHardwareConfig] = None


class ConfigManager(DynamicData):
   cpuScheduler: Optional[CpuSchedulerSystem] = None
   datastoreSystem: Optional[DatastoreSystem] = None
   memoryManager: Optional[MemoryManagerSystem] = None
   storageSystem: Optional[StorageSystem] = None
   networkSystem: Optional[NetworkSystem] = None
   vmotionSystem: Optional[VMotionSystem] = None
   virtualNicManager: Optional[VirtualNicManager] = None
   serviceSystem: Optional[ServiceSystem] = None
   firewallSystem: Optional[FirewallSystem] = None
   advancedOption: Optional[OptionManager] = None
   diagnosticSystem: Optional[DiagnosticSystem] = None
   autoStartManager: Optional[AutoStartManager] = None
   snmpSystem: Optional[SnmpSystem] = None
   dateTimeSystem: Optional[DateTimeSystem] = None
   patchManager: Optional[PatchManager] = None
   imageConfigManager: Optional[ImageConfigManager] = None
   bootDeviceSystem: Optional[BootDeviceSystem] = None
   firmwareSystem: Optional[FirmwareSystem] = None
   healthStatusSystem: Optional[HealthStatusSystem] = None
   pciPassthruSystem: Optional[PciPassthruSystem] = None
   licenseManager: Optional[LicenseManager] = None
   kernelModuleSystem: Optional[KernelModuleSystem] = None
   authenticationManager: Optional[AuthenticationManager] = None
   powerSystem: Optional[PowerSystem] = None
   cacheConfigurationManager: Optional[CacheConfigurationManager] = None
   esxAgentHostManager: Optional[EsxAgentHostManager] = None
   iscsiManager: Optional[IscsiManager] = None
   vFlashManager: Optional[VFlashManager] = None
   vsanSystem: Optional[VsanSystem] = None
   messageBusProxy: Optional[MessageBusProxy] = None
   userDirectory: Optional[UserDirectory] = None
   accountManager: Optional[LocalAccountManager] = None
   hostAccessManager: Optional[HostAccessManager] = None
   graphicsManager: Optional[GraphicsManager] = None
   vsanInternalSystem: Optional[VsanInternalSystem] = None
   certificateManager: Optional[CertificateManager] = None
   cryptoManager: Optional[CryptoManager] = None
   nvdimmSystem: Optional[NvdimmSystem] = None
   assignableHardwareManager: Optional[AssignableHardwareManager] = None


class ConfigSpec(DynamicData):
   nasDatastore: list[NasVolume.Config] = []
   network: Optional[NetworkConfig] = None
   nicTypeSelection: list[VirtualNicManager.NicTypeSelection] = []
   service: list[ServiceConfig] = []
   firewall: Optional[FirewallConfig] = None
   option: list[OptionValue] = []
   datastorePrincipal: Optional[str] = None
   datastorePrincipalPasswd: Optional[str] = None
   datetime: Optional[DateTimeConfig] = None
   storageDevice: Optional[StorageDeviceInfo] = None
   license: Optional[LicenseSpec] = None
   security: Optional[SecuritySpec] = None
   userAccount: list[LocalAccountManager.AccountSpecification] = []
   usergroupAccount: list[LocalAccountManager.AccountSpecification] = []
   memory: Optional[MemorySpec] = None
   activeDirectory: list[ActiveDirectorySpec] = []
   genericConfig: list[KeyAnyValue] = []
   graphicsConfig: Optional[GraphicsConfig] = None
   assignableHardwareConfig: Optional[AssignableHardwareConfig] = None


class ConnectInfo(DynamicData):
   class NetworkInfo(DynamicData):
      summary: Network.Summary

   class NewNetworkInfo(NetworkInfo):
      pass

   class DatastoreInfo(DynamicData):
      summary: Datastore.Summary

   class DatastoreExistsInfo(DatastoreInfo):
      newDatastoreName: str

   class DatastoreNameConflictInfo(DatastoreInfo):
      newDatastoreName: str

   class LicenseInfo(DynamicData):
      license: LicenseManager.LicenseInfo
      evaluation: LicenseManager.EvaluationInfo
      resource: Optional[LicenseManager.LicensableResourceInfo] = None

   serverIp: Optional[str] = None
   inDasCluster: Optional[bool] = None
   host: Summary
   vm: list[Summary] = []
   vimAccountNameRequired: Optional[bool] = None
   clusterSupported: Optional[bool] = None
   network: list[NetworkInfo] = []
   datastore: list[DatastoreInfo] = []
   license: Optional[LicenseInfo] = None
   capability: Optional[Capability] = None


class ConnectSpec(DynamicData):
   hostName: Optional[str] = None
   port: Optional[int] = None
   sslThumbprint: Optional[str] = None
   sslCertificate: Optional[str] = None
   userName: Optional[str] = None
   password: Optional[str] = None
   vmFolder: Optional[Folder] = None
   force: bool
   vimAccountName: Optional[str] = None
   vimAccountPassword: Optional[str] = None
   managementIp: Optional[str] = None
   lockdownMode: Optional[HostAccessManager.LockdownMode] = None
   hostGateway: Optional[GatewaySpec] = None


class CpuIdInfo(DynamicData):
   level: int
   vendor: Optional[str] = None
   eax: Optional[str] = None
   ebx: Optional[str] = None
   ecx: Optional[str] = None
   edx: Optional[str] = None


class CpuInfo(DynamicData):
   numCpuPackages: short
   numCpuCores: short
   numCpuThreads: short
   hz: long


class CpuPackage(DynamicData):
   class Vendor(Enum):
      unknown: ClassVar['Vendor'] = 'unknown'
      intel: ClassVar['Vendor'] = 'intel'
      amd: ClassVar['Vendor'] = 'amd'
      hygon: ClassVar['Vendor'] = 'hygon'
      arm: ClassVar['Vendor'] = 'arm'

   index: short
   vendor: str
   hz: long
   busHz: long
   description: str
   threadId: list[short] = []
   cpuFeature: list[CpuIdInfo] = []
   family: Optional[short] = None
   model: Optional[short] = None
   stepping: Optional[short] = None


class CpuPowerManagementInfo(DynamicData):
   class PolicyType(Enum):
      off: ClassVar['PolicyType'] = 'off'
      staticPolicy: ClassVar['PolicyType'] = 'staticPolicy'
      dynamicPolicy: ClassVar['PolicyType'] = 'dynamicPolicy'

   currentPolicy: Optional[str] = None
   hardwareSupport: Optional[str] = None


class CpuSchedulerSystem(ExtensibleManagedObject):
   class HyperThreadScheduleInfo(DynamicData):
      available: bool
      active: bool
      config: bool

   class CpuSchedulerInfo(DynamicData):
      class CpuSchedulerPolicyInfo(Enum):
         systemDefault: ClassVar['CpuSchedulerPolicyInfo'] = 'systemDefault'
         scav1: ClassVar['CpuSchedulerPolicyInfo'] = 'scav1'
         scav2: ClassVar['CpuSchedulerPolicyInfo'] = 'scav2'

      policy: str

   @property
   def cpuSchedulerInfo(self) -> Optional[CpuSchedulerInfo]: ...
   @property
   def hyperthreadInfo(self) -> Optional[HyperThreadScheduleInfo]: ...

   def EnableHyperThreading(self) -> None: ...
   def DisableHyperThreading(self) -> None: ...


class DataTransportConnectionInfo(DynamicData):
   staticMemoryConsumed: long


class DatastoreBrowser(ManagedObject):
   class FileInfo(DynamicData):
      class Details(DynamicData):
         fileType: bool
         fileSize: bool
         modification: bool
         fileOwner: bool

      path: str
      friendlyName: Optional[str] = None
      fileSize: Optional[long] = None
      modification: Optional[datetime] = None
      owner: Optional[str] = None

   class Query(DynamicData):
      pass

   class VmConfigQuery(Query):
      class Filter(DynamicData):
         matchConfigVersion: list[int] = []
         encrypted: Optional[bool] = None

      class Details(DynamicData):
         configVersion: bool
         encryption: Optional[bool] = None

      filter: Optional[Filter] = None
      details: Optional[Details] = None

   class TemplateVmConfigQuery(VmConfigQuery):
      pass

   class VmDiskQuery(Query):
      class Filter(DynamicData):
         diskType: list[type] = []
         matchHardwareVersion: list[int] = []
         controllerType: list[type] = []
         thin: Optional[bool] = None
         encrypted: Optional[bool] = None

      class Details(DynamicData):
         diskType: bool
         capacityKb: bool
         hardwareVersion: bool
         controllerType: Optional[bool] = None
         diskExtents: Optional[bool] = None
         thin: Optional[bool] = None
         encryption: Optional[bool] = None
         sectorFormat: Optional[bool] = None

      filter: Optional[Filter] = None
      details: Optional[Details] = None

   class FolderQuery(Query):
      pass

   class VmSnapshotQuery(Query):
      pass

   class IsoImageQuery(Query):
      pass

   class FloppyImageQuery(Query):
      pass

   class VmNvramQuery(Query):
      pass

   class VmLogQuery(Query):
      pass

   class VmConfigInfo(FileInfo):
      class VmConfigEncryptionInfo(DynamicData):
         keyId: Optional[CryptoKeyId] = None

      configVersion: Optional[int] = None
      encryption: Optional[VmConfigEncryptionInfo] = None

   class TemplateVmConfigInfo(VmConfigInfo):
      pass

   class VmDiskInfo(FileInfo):
      class VmDiskEncryptionInfo(DynamicData):
         keyId: Optional[CryptoKeyId] = None

      diskType: Optional[type] = None
      capacityKb: Optional[long] = None
      hardwareVersion: Optional[int] = None
      controllerType: Optional[type] = None
      diskExtents: list[str] = []
      thin: Optional[bool] = None
      encryption: Optional[VmDiskEncryptionInfo] = None
      sectorFormat: Optional[str] = None

   class FolderInfo(FileInfo):
      pass

   class VmSnapshotInfo(FileInfo):
      pass

   class IsoImageInfo(FileInfo):
      pass

   class FloppyImageInfo(FileInfo):
      pass

   class VmNvramInfo(FileInfo):
      pass

   class VmLogInfo(FileInfo):
      pass

   class SearchSpec(DynamicData):
      query: list[Query] = []
      details: Optional[FileInfo.Details] = None
      searchCaseInsensitive: Optional[bool] = None
      matchPattern: list[str] = []
      sortFoldersFirst: Optional[bool] = None

   class SearchResults(DynamicData):
      datastore: Optional[Datastore] = None
      folderPath: Optional[str] = None
      file: list[FileInfo] = []

   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def supportedType(self) -> list[Query]: ...

   def Search(self, datastorePath: str, searchSpec: Optional[SearchSpec]) -> Task: ...
   def SearchSubFolders(self, datastorePath: str, searchSpec: Optional[SearchSpec]) -> Task: ...
   def DeleteFile(self, datastorePath: str) -> None: ...


class DatastoreSystem(ManagedObject):
   class Capabilities(DynamicData):
      nfsMountCreationRequired: bool
      nfsMountCreationSupported: bool
      localDatastoreSupported: bool
      vmfsExtentExpansionSupported: bool

   class VvolDatastoreSpec(DynamicData):
      name: str
      scId: str

   class DatastoreResult(DynamicData):
      key: Datastore
      fault: Optional[MethodFault] = None

   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def capabilities(self) -> Capabilities: ...

   def UpdateLocalSwapDatastore(self, datastore: Optional[Datastore]) -> None: ...
   def QueryAvailableDisksForVmfs(self, datastore: Optional[Datastore]) -> list[ScsiDisk]: ...
   def QueryVmfsDatastoreCreateOptions(self, devicePath: str, vmfsMajorVersion: Optional[int]) -> list[VmfsDatastoreOption]: ...
   def CreateVmfsDatastore(self, spec: VmfsDatastoreCreateSpec) -> Datastore: ...
   def QueryVmfsDatastoreExtendOptions(self, datastore: Datastore, devicePath: str, suppressExpandCandidates: Optional[bool]) -> list[VmfsDatastoreOption]: ...
   def QueryVmfsDatastoreExpandOptions(self, datastore: Datastore) -> list[VmfsDatastoreOption]: ...
   def ExtendVmfsDatastore(self, datastore: Datastore, spec: VmfsDatastoreExtendSpec) -> Datastore: ...
   def EnableClusteredVmdkSupport(self, datastore: Datastore) -> None: ...
   def DisableClusteredVmdkSupport(self, datastore: Datastore) -> None: ...
   def ExpandVmfsDatastore(self, datastore: Datastore, spec: VmfsDatastoreExpandSpec) -> Datastore: ...
   def CreateNasDatastore(self, spec: NasVolume.Specification) -> Datastore: ...
   def CreateLocalDatastore(self, name: str, path: str) -> Datastore: ...
   def CreateVvolDatastore(self, spec: VvolDatastoreSpec) -> Datastore: ...
   def RemoveDatastore(self, datastore: Datastore) -> None: ...
   def SetMaxQueueDepth(self, datastore: Datastore, maxQdepth: long) -> None: ...
   def ResolveNfsServerHostName(self, hostName: str, volumeName: Optional[str], force: Optional[bool], isNFS41: Optional[bool]) -> None: ...
   def QueryMaxQueueDepth(self, datastore: Datastore) -> long: ...
   def RemoveDatastoreEx(self, datastore: list[Datastore]) -> Task: ...
   def ConfigureDatastorePrincipal(self, userName: str, password: Optional[str]) -> None: ...
   def QueryUnresolvedVmfsVolumes(self) -> list[UnresolvedVmfsVolume]: ...
   def ResignatureUnresolvedVmfsVolume(self, resolutionSpec: UnresolvedVmfsResignatureSpec) -> Task: ...


class DateTimeConfig(DynamicData):
   timeZone: Optional[str] = None
   ntpConfig: Optional[NtpConfig] = None
   ptpConfig: Optional[PtpConfig] = None
   protocol: Optional[str] = None
   enabled: Optional[bool] = None
   disableEvents: Optional[bool] = None
   disableFallback: Optional[bool] = None
   resetToFactoryDefaults: Optional[bool] = None


class DateTimeInfo(DynamicData):
   class Protocol(Enum):
      ntp: ClassVar['Protocol'] = 'ntp'
      ptp: ClassVar['Protocol'] = 'ptp'

   timeZone: DateTimeSystem.TimeZone
   systemClockProtocol: Optional[str] = None
   ntpConfig: Optional[NtpConfig] = None
   ptpConfig: Optional[PtpConfig] = None
   enabled: Optional[bool] = None
   disableEvents: Optional[bool] = None
   disableFallback: Optional[bool] = None
   inFallbackState: Optional[bool] = None
   serviceSync: Optional[bool] = None
   lastSyncTime: Optional[datetime] = None
   remoteNtpServer: Optional[str] = None
   ntpRunTime: Optional[long] = None
   ptpRunTime: Optional[long] = None
   ntpDuration: Optional[str] = None
   ptpDuration: Optional[str] = None


class DateTimeSystem(ManagedObject):
   class TimeZone(DynamicData):
      key: str
      name: str
      description: str
      gmtOffset: int

   class ServiceTestResult(DynamicData):
      workingNormally: bool
      report: list[str] = []

   @property
   def dateTimeInfo(self) -> DateTimeInfo: ...

   def UpdateConfig(self, config: DateTimeConfig) -> None: ...
   def QueryAvailableTimeZones(self) -> list[TimeZone]: ...
   def QueryDateTime(self) -> datetime: ...
   def UpdateDateTime(self, dateTime: datetime) -> None: ...
   def Refresh(self) -> None: ...
   def TestTimeService(self) -> Optional[ServiceTestResult]: ...


class DeploymentInfo(DynamicData):
   bootedFromStatelessCache: Optional[bool] = None


class Device(DynamicData):
   deviceName: str
   deviceType: str


class DevicePciId(DynamicData):
   vendorId: long
   deviceId: long
   subVendorId: long
   subDeviceId: long


class DhcpService(DynamicData):
   class Specification(DynamicData):
      virtualSwitch: str
      defaultLeaseDuration: int
      leaseBeginIp: str
      leaseEndIp: str
      maxLeaseDuration: int
      unlimitedLease: bool
      ipSubnetAddr: str
      ipSubnetMask: str

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      key: str
      spec: Specification

   key: str
   spec: Specification


class DiagnosticPartition(DynamicData):
   class StorageType(Enum):
      directAttached: ClassVar['StorageType'] = 'directAttached'
      networkAttached: ClassVar['StorageType'] = 'networkAttached'

   class DiagnosticType(Enum):
      singleHost: ClassVar['DiagnosticType'] = 'singleHost'
      multiHost: ClassVar['DiagnosticType'] = 'multiHost'

   class CreateOption(DynamicData):
      storageType: str
      diagnosticType: str
      disk: ScsiDisk

   class CreateSpec(DynamicData):
      storageType: str
      diagnosticType: str
      id: ScsiDisk.Partition
      partition: DiskPartitionInfo.Specification
      active: Optional[bool] = None

   class CreateDescription(DynamicData):
      layout: DiskPartitionInfo.Layout
      diskUuid: str
      spec: CreateSpec

   storageType: str
   diagnosticType: str
   slots: int
   id: ScsiDisk.Partition


class DiagnosticSystem(ManagedObject):
   @property
   def activePartition(self) -> Optional[DiagnosticPartition]: ...

   def QueryAvailablePartition(self) -> list[DiagnosticPartition]: ...
   def SelectActivePartition(self, partition: Optional[ScsiDisk.Partition]) -> None: ...
   def QueryPartitionCreateOptions(self, storageType: str, diagnosticType: str) -> list[DiagnosticPartition.CreateOption]: ...
   def QueryPartitionCreateDesc(self, diskUuid: str, diagnosticType: str) -> DiagnosticPartition.CreateDescription: ...
   def CreateDiagnosticPartition(self, spec: DiagnosticPartition.CreateSpec) -> None: ...


class DigestInfo(DynamicData):
   class DigestMethodType(Enum):
      SHA1: ClassVar['DigestMethodType'] = 'SHA1'
      MD5: ClassVar['DigestMethodType'] = 'MD5'
      SHA256: ClassVar['DigestMethodType'] = 'SHA256'
      SHA384: ClassVar['DigestMethodType'] = 'SHA384'
      SHA512: ClassVar['DigestMethodType'] = 'SHA512'
      SM3_256: ClassVar['DigestMethodType'] = 'SM3_256'

   digestMethod: str
   digestValue: list[byte] = []
   objectName: Optional[str] = None

class DigestVerificationSetting:
   pass

class DirectoryStore(AuthenticationStore):
   pass

class DirectoryStoreInfo(AuthenticationStoreInfo):
   pass


class DiskConfigurationResult(DynamicData):
   devicePath: Optional[str] = None
   success: Optional[bool] = None
   fault: Optional[MethodFault] = None


class DiskDimensions(DynamicData):
   class Chs(DynamicData):
      cylinder: long
      head: int
      sector: int

   class Lba(DynamicData):
      blockSize: int
      block: long


class DiskPartitionInfo(DynamicData):
   class PartitionFormat(Enum):
      gpt: ClassVar['PartitionFormat'] = 'gpt'
      mbr: ClassVar['PartitionFormat'] = 'mbr'
      unknown: ClassVar['PartitionFormat'] = 'unknown'

   class Type(Enum):
      none: ClassVar['Type'] = 'none'
      vmfs: ClassVar['Type'] = 'vmfs'
      linuxNative: ClassVar['Type'] = 'linuxNative'
      linuxSwap: ClassVar['Type'] = 'linuxSwap'
      extended: ClassVar['Type'] = 'extended'
      ntfs: ClassVar['Type'] = 'ntfs'
      vmkDiagnostic: ClassVar['Type'] = 'vmkDiagnostic'
      vffs: ClassVar['Type'] = 'vffs'

   class Partition(DynamicData):
      partition: int
      startSector: long
      endSector: long
      type: str
      guid: Optional[str] = None
      logical: bool
      attributes: byte
      partitionAlignment: Optional[long] = None

   class BlockRange(DynamicData):
      partition: Optional[int] = None
      type: str
      start: DiskDimensions.Lba
      end: DiskDimensions.Lba

   class Specification(DynamicData):
      partitionFormat: Optional[str] = None
      chs: Optional[DiskDimensions.Chs] = None
      totalSectors: Optional[long] = None
      partition: list[Partition] = []
      sectorSize: Optional[int] = None

   class Layout(DynamicData):
      total: Optional[DiskDimensions.Lba] = None
      partition: list[BlockRange] = []

   deviceName: str
   spec: Specification
   layout: Layout


class DnsConfig(DynamicData):
   dhcp: bool
   virtualNicDevice: Optional[str] = None
   ipv6VirtualNicDevice: Optional[str] = None
   hostName: str
   domainName: str
   address: list[str] = []
   searchDomain: list[str] = []


class DnsConfigSpec(DnsConfig):
   virtualNicConnection: Optional[VirtualNicConnection] = None
   virtualNicConnectionV6: Optional[VirtualNicConnection] = None


class DvxClass(DynamicData):
   deviceClass: str
   checkpointSupported: bool
   swDMATracingSupported: bool
   sriovNic: bool


class EnterMaintenanceResult(DynamicData):
   vmFaults: list[FaultsByVM] = []
   hostFaults: list[FaultsByHost] = []


class EsxAgentHostManager(ManagedObject):
   class ConfigInfo(DynamicData):
      agentVmDatastore: Optional[Datastore] = None
      agentVmNetwork: Optional[Network] = None

   @property
   def configInfo(self) -> ConfigInfo: ...

   def UpdateConfig(self, configInfo: ConfigInfo) -> None: ...


class FcoeConfig(DynamicData):
   class VlanRange(DynamicData):
      vlanLow: int
      vlanHigh: int

   class FcoeCapabilities(DynamicData):
      priorityClass: bool
      sourceMacAddress: bool
      vlanRange: bool

   class FcoeSpecification(DynamicData):
      underlyingPnic: str
      priorityClass: Optional[int] = None
      sourceMac: Optional[str] = None
      vlanRange: list[VlanRange] = []

   priorityClass: int
   sourceMac: str
   vlanRange: list[VlanRange] = []
   capabilities: FcoeCapabilities
   fcoeActive: bool


class FeatureCapability(DynamicData):
   key: str
   featureName: str
   value: str


class FeatureMask(DynamicData):
   key: str
   featureName: str
   value: str


class FeatureVersionInfo(DynamicData):
   class FeatureVersionKey(Enum):
      faultTolerance: ClassVar['FeatureVersionKey'] = 'faultTolerance'

   key: str
   value: str


class FibreChannelHba(HostBusAdapter):
   class PortType(Enum):
      fabric: ClassVar['PortType'] = 'fabric'
      loop: ClassVar['PortType'] = 'loop'
      pointToPoint: ClassVar['PortType'] = 'pointToPoint'
      unknown: ClassVar['PortType'] = 'unknown'

   portWorldWideName: long
   nodeWorldWideName: long
   portType: PortType
   speed: long


class FibreChannelOverEthernetHba(FibreChannelHba):
   class LinkInfo(DynamicData):
      vnportMac: str
      fcfMac: str
      vlanId: int

   underlyingNic: str
   linkInfo: LinkInfo
   isSoftwareFcoe: bool
   markedForRemoval: Optional[bool] = None

class FibreChannelOverEthernetTargetTransport(FibreChannelTargetTransport):
   vnportMac: str
   fcfMac: str
   vlanId: int


class FibreChannelTargetTransport(TargetTransport):
   portWorldWideName: long
   nodeWorldWideName: long


class FileAccess(DynamicData):
   class Modes(DynamicData):
      browse: Optional[str] = None
      read: str
      modify: str
      use: str
      admin: Optional[str] = None
      full: str

   who: str
   what: str


class FileSystemMountInfo(DynamicData):
   class VStorageSupportStatus(Enum):
      vStorageSupported: ClassVar['VStorageSupportStatus'] = 'vStorageSupported'
      vStorageUnsupported: ClassVar['VStorageSupportStatus'] = 'vStorageUnsupported'
      vStorageUnknown: ClassVar['VStorageSupportStatus'] = 'vStorageUnknown'

   mountInfo: MountInfo
   volume: FileSystemVolume
   vStorageSupport: Optional[str] = None


class FileSystemVolume(DynamicData):
   class FileSystemType(Enum):
      VMFS: ClassVar['FileSystemType'] = 'VMFS'
      NFS: ClassVar['FileSystemType'] = 'NFS'
      NFS41: ClassVar['FileSystemType'] = 'NFS41'
      CIFS: ClassVar['FileSystemType'] = 'CIFS'
      vsan: ClassVar['FileSystemType'] = 'vsan'
      VFFS: ClassVar['FileSystemType'] = 'VFFS'
      VVOL: ClassVar['FileSystemType'] = 'VVOL'
      PMEM: ClassVar['FileSystemType'] = 'PMEM'
      vsanD: ClassVar['FileSystemType'] = 'vsanD'
      OTHER: ClassVar['FileSystemType'] = 'OTHER'

   type: str
   name: str
   capacity: long


class FileSystemVolumeInfo(DynamicData):
   volumeTypeList: list[str] = []
   mountInfo: list[FileSystemMountInfo] = []


class FirewallConfig(DynamicData):
   class RuleSetConfig(DynamicData):
      rulesetId: str
      enabled: bool
      allowedHosts: Optional[Ruleset.IpList] = None

   rule: list[RuleSetConfig] = []
   defaultBlockingPolicy: FirewallInfo.DefaultPolicy


class FirewallInfo(DynamicData):
   class DefaultPolicy(DynamicData):
      incomingBlocked: Optional[bool] = None
      outgoingBlocked: Optional[bool] = None

   defaultPolicy: DefaultPolicy
   ruleset: list[Ruleset] = []


class FirewallSystem(ExtensibleManagedObject):
   class ServiceName(Enum):
      vpxa: ClassVar['ServiceName'] = 'vpxa'

   class RuleSetId(Enum):
      faultTolerance: ClassVar['RuleSetId'] = 'faultTolerance'
      fdm: ClassVar['RuleSetId'] = 'fdm'
      updateManager: ClassVar['RuleSetId'] = 'updateManager'
      vpxHeartbeats: ClassVar['RuleSetId'] = 'vpxHeartbeats'

   @property
   def firewallInfo(self) -> Optional[FirewallInfo]: ...

   def UpdateDefaultPolicy(self, defaultPolicy: FirewallInfo.DefaultPolicy) -> None: ...
   def EnableRuleset(self, id: str) -> None: ...
   def DisableRuleset(self, id: str) -> None: ...
   def UpdateRuleset(self, id: str, spec: Ruleset.RulesetSpec) -> None: ...
   def Refresh(self) -> None: ...


class FirmwareSystem(ManagedObject):
   def ResetToFactoryDefaults(self) -> None: ...
   def BackupConfiguration(self) -> str: ...
   def QueryConfigUploadURL(self) -> str: ...
   def RestoreConfiguration(self, force: bool) -> None: ...


class FlagInfo(DynamicData):
   backgroundSnapshotsEnabled: Optional[bool] = None


class ForceMountedInfo(DynamicData):
   persist: bool
   mounted: bool


class Fru(DynamicData):
   class FruType(Enum):
      undefined: ClassVar['FruType'] = 'undefined'
      board: ClassVar['FruType'] = 'board'
      product: ClassVar['FruType'] = 'product'

   type: str
   partName: str
   partNumber: str
   manufacturer: str
   serialNumber: Optional[str] = None
   mfgTimeStamp: Optional[datetime] = None


class GatewaySpec(DynamicData):
   gatewayType: str
   gatewayId: Optional[str] = None
   trustVerificationToken: Optional[str] = None
   hostAuthParams: list[KeyValue] = []


class GraphicsConfig(DynamicData):
   class GraphicsType(Enum):
      shared: ClassVar['GraphicsType'] = 'shared'
      sharedDirect: ClassVar['GraphicsType'] = 'sharedDirect'

   class SharedPassthruAssignmentPolicy(Enum):
      performance: ClassVar['SharedPassthruAssignmentPolicy'] = 'performance'
      consolidation: ClassVar['SharedPassthruAssignmentPolicy'] = 'consolidation'

   class VgpuMode(Enum):
      sameSize: ClassVar['VgpuMode'] = 'sameSize'
      mixedSize: ClassVar['VgpuMode'] = 'mixedSize'

   class DeviceType(DynamicData):
      deviceId: str
      graphicsType: str
      vgpuMode: Optional[str] = None

   hostDefaultGraphicsType: str
   sharedPassthruAssignmentPolicy: str
   deviceType: list[DeviceType] = []


class GraphicsInfo(DynamicData):
   class GraphicsType(Enum):
      basic: ClassVar['GraphicsType'] = 'basic'
      shared: ClassVar['GraphicsType'] = 'shared'
      direct: ClassVar['GraphicsType'] = 'direct'
      sharedDirect: ClassVar['GraphicsType'] = 'sharedDirect'

   class VgpuMode(Enum):
      none: ClassVar['VgpuMode'] = 'none'
      sameSize: ClassVar['VgpuMode'] = 'sameSize'
      mixedSize: ClassVar['VgpuMode'] = 'mixedSize'
      multiInstanceGpu: ClassVar['VgpuMode'] = 'multiInstanceGpu'

   deviceName: str
   vendorName: str
   pciId: str
   graphicsType: str
   vgpuMode: Optional[str] = None
   memorySizeInKB: long
   vm: list[VirtualMachine] = []


class GraphicsManager(ExtensibleManagedObject):
   @property
   def graphicsInfo(self) -> list[GraphicsInfo]: ...
   @property
   def graphicsConfig(self) -> Optional[GraphicsConfig]: ...
   @property
   def sharedPassthruGpuTypes(self) -> list[str]: ...
   @property
   def sharedGpuCapabilities(self) -> list[SharedGpuCapabilities]: ...

   def RetrieveVgpuDeviceInfo(self) -> list[VgpuDeviceInfo]: ...
   def RetrieveVgpuProfileInfo(self) -> list[VgpuProfileInfo]: ...
   def Refresh(self) -> None: ...
   def IsSharedGraphicsActive(self) -> bool: ...
   def UpdateGraphicsConfig(self, config: GraphicsConfig) -> None: ...


class HardwareInfo(DynamicData):
   systemInfo: SystemInfo
   cpuPowerManagementInfo: Optional[CpuPowerManagementInfo] = None
   cpuInfo: CpuInfo
   cpuPkg: list[CpuPackage] = []
   memorySize: long
   numaInfo: Optional[NumaInfo] = None
   smcPresent: bool
   pciDevice: list[PciDevice] = []
   dvxClasses: list[DvxClass] = []
   cpuFeature: list[CpuIdInfo] = []
   biosInfo: Optional[BIOSInfo] = None
   reliableMemoryInfo: Optional[ReliableMemoryInfo] = None
   persistentMemoryInfo: Optional[PersistentMemoryInfo] = None
   sgxInfo: Optional[SgxInfo] = None
   sevInfo: Optional[SevInfo] = None
   memoryTieringType: Optional[str] = None
   memoryTierInfo: list[MemoryTierInfo] = []
   tdxInfo: Optional[TdxInfo] = None


class HardwareStatusInfo(DynamicData):
   class Status(Enum):
      Unknown: ClassVar['Status'] = 'Unknown'
      Green: ClassVar['Status'] = 'Green'
      Yellow: ClassVar['Status'] = 'Yellow'
      Red: ClassVar['Status'] = 'Red'

   class HardwareElementInfo(DynamicData):
      name: str
      status: ElementDescription

   class StorageStatusInfo(HardwareElementInfo):
      class OperationalInfo(DynamicData):
         property: str
         value: str

      operationalInfo: list[OperationalInfo] = []

   class DpuStatusInfo(HardwareElementInfo):
      class OperationalInfo(DynamicData):
         sensorId: str
         healthState: Optional[ElementDescription] = None
         reading: str
         units: Optional[str] = None
         timeStamp: Optional[datetime] = None

      dpuId: str
      fru: Optional[Fru] = None
      sensors: list[OperationalInfo] = []

   memoryStatusInfo: list[HardwareElementInfo] = []
   cpuStatusInfo: list[HardwareElementInfo] = []
   storageStatusInfo: list[StorageStatusInfo] = []
   dpuStatusInfo: list[DpuStatusInfo] = []


class HbaCreateSpec(DynamicData):
   pass


class HealthStatusSystem(ManagedObject):
   class Runtime(DynamicData):
      systemHealthInfo: Optional[SystemHealthInfo] = None
      hardwareStatusInfo: Optional[HardwareStatusInfo] = None

   @property
   def runtime(self) -> Runtime: ...

   def Refresh(self) -> None: ...
   def ResetSystemHealthInfo(self) -> None: ...
   def ClearSystemEventLog(self) -> None: ...
   def FetchSystemEventLog(self) -> list[SystemEventInfo]: ...


class HostAccessManager(ManagedObject):
   class AccessMode(Enum):
      accessNone: ClassVar['AccessMode'] = 'accessNone'
      accessAdmin: ClassVar['AccessMode'] = 'accessAdmin'
      accessNoAccess: ClassVar['AccessMode'] = 'accessNoAccess'
      accessReadOnly: ClassVar['AccessMode'] = 'accessReadOnly'
      accessOther: ClassVar['AccessMode'] = 'accessOther'

   class AccessEntry(DynamicData):
      principal: str
      group: bool
      accessMode: AccessMode

   class LockdownMode(Enum):
      lockdownDisabled: ClassVar['LockdownMode'] = 'lockdownDisabled'
      lockdownNormal: ClassVar['LockdownMode'] = 'lockdownNormal'
      lockdownStrict: ClassVar['LockdownMode'] = 'lockdownStrict'

   @property
   def lockdownMode(self) -> LockdownMode: ...

   def RetrieveAccessEntries(self) -> list[AccessEntry]: ...
   def ChangeAccessMode(self, principal: str, isGroup: bool, accessMode: AccessMode) -> None: ...
   def QuerySystemUsers(self) -> list[str]: ...
   def UpdateSystemUsers(self, users: list[str]) -> None: ...
   def QueryLockdownExceptions(self) -> list[str]: ...
   def UpdateLockdownExceptions(self, users: list[str]) -> None: ...
   def ChangeLockdownMode(self, mode: LockdownMode) -> None: ...


class HostBusAdapter(DynamicData):
   key: Optional[str] = None
   device: str
   bus: int
   status: str
   model: str
   driver: Optional[str] = None
   pci: Optional[str] = None
   storageProtocol: Optional[str] = None
   driverVersion: Optional[str] = None
   firmwareVersion: Optional[str] = None


class HostProxySwitch(DynamicData):
   class Specification(DynamicData):
      backing: Optional[HostMember.Backing] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      uuid: str
      spec: Optional[Specification] = None

   class HostLagConfig(DynamicData):
      lagKey: str
      lagName: Optional[str] = None
      uplinkPort: list[KeyValue] = []

   class EnsInfo(DynamicData):
      opsVersion: long
      numPSOps: long
      numLcoreOps: long
      errorStatus: long
      lcoreStatus: long

   dvsUuid: str
   dvsName: str
   key: str
   numPorts: int
   configNumPorts: Optional[int] = None
   numPortsAvailable: int
   uplinkPort: list[KeyValue] = []
   mtu: Optional[int] = None
   pnic: list[PhysicalNic] = []
   spec: Specification
   hostLag: list[HostLagConfig] = []
   networkReservationSupported: Optional[bool] = None
   nsxtEnabled: Optional[bool] = None
   ensEnabled: Optional[bool] = None
   ensInterruptEnabled: Optional[bool] = None
   transportZones: list[HostMember.TransportZoneInfo] = []
   nsxUsedUplinkPort: list[str] = []
   nsxtStatus: Optional[str] = None
   nsxtStatusDetail: Optional[str] = None
   ensInfo: Optional[EnsInfo] = None
   networkOffloadingEnabled: Optional[bool] = None
   hostUplinkState: list[HostMember.HostUplinkState] = []
   autoDeployOwned: Optional[bool] = None
   hostPerfNicOffloadState: Optional[HostMember.HostPerfNicOffloadState] = None
   teplessMode: Optional[bool] = None


class HostSpbm(ManagedObject):
   pass


class HostSpbmDatastoreInfo(DynamicData):
   datastoreUrl: str
   namespace: str
   defaultProfileId: str


class HostSpbmHashInfo(DynamicData):
   policyInfoHash: str
   datastoreInfoHash: str


class HostSpbmPolicyBlobInfo(DynamicData):
   policyBlob: str
   namespace: str


class HostSpbmPolicyInfo(DynamicData):
   profileId: str
   name: str
   description: Optional[str] = None
   generationId: long
   policyBlobInfo: list[HostSpbmPolicyBlobInfo] = []


class ImageConfigManager(ManagedObject):
   class AcceptanceLevel(Enum):
      vmware_certified: ClassVar['AcceptanceLevel'] = 'vmware_certified'
      vmware_accepted: ClassVar['AcceptanceLevel'] = 'vmware_accepted'
      partner: ClassVar['AcceptanceLevel'] = 'partner'
      community: ClassVar['AcceptanceLevel'] = 'community'

   class ImageProfileSummary(DynamicData):
      name: str
      vendor: str

   def QueryHostAcceptanceLevel(self) -> str: ...
   def QueryHostImageProfile(self) -> ImageProfileSummary: ...
   def UpdateAcceptanceLevel(self, newAcceptanceLevel: str) -> None: ...
   def FetchSoftwarePackages(self) -> list[SoftwarePackage]: ...
   def InstallDate(self) -> datetime: ...


class InternetScsiHba(HostBusAdapter):
   class ParamValue(OptionValue):
      isInherited: Optional[bool] = None

   class DiscoveryCapabilities(DynamicData):
      iSnsDiscoverySettable: bool
      slpDiscoverySettable: bool
      staticTargetDiscoverySettable: bool
      sendTargetsDiscoverySettable: bool

   class DiscoveryProperties(DynamicData):
      class ISnsDiscoveryMethod(Enum):
         isnsStatic: ClassVar['ISnsDiscoveryMethod'] = 'isnsStatic'
         isnsDhcp: ClassVar['ISnsDiscoveryMethod'] = 'isnsDhcp'
         isnsSlp: ClassVar['ISnsDiscoveryMethod'] = 'isnsSlp'

      class SlpDiscoveryMethod(Enum):
         slpDhcp: ClassVar['SlpDiscoveryMethod'] = 'slpDhcp'
         slpAutoUnicast: ClassVar['SlpDiscoveryMethod'] = 'slpAutoUnicast'
         slpAutoMulticast: ClassVar['SlpDiscoveryMethod'] = 'slpAutoMulticast'
         slpManual: ClassVar['SlpDiscoveryMethod'] = 'slpManual'

      iSnsDiscoveryEnabled: bool
      iSnsDiscoveryMethod: Optional[str] = None
      iSnsHost: Optional[str] = None
      slpDiscoveryEnabled: bool
      slpDiscoveryMethod: Optional[str] = None
      slpHost: Optional[str] = None
      staticTargetDiscoveryEnabled: bool
      sendTargetsDiscoveryEnabled: bool

   class ChapAuthenticationType(Enum):
      chapProhibited: ClassVar['ChapAuthenticationType'] = 'chapProhibited'
      chapDiscouraged: ClassVar['ChapAuthenticationType'] = 'chapDiscouraged'
      chapPreferred: ClassVar['ChapAuthenticationType'] = 'chapPreferred'
      chapRequired: ClassVar['ChapAuthenticationType'] = 'chapRequired'

   class AuthenticationCapabilities(DynamicData):
      chapAuthSettable: bool
      krb5AuthSettable: bool
      srpAuthSettable: bool
      spkmAuthSettable: bool
      mutualChapSettable: Optional[bool] = None
      targetChapSettable: Optional[bool] = None
      targetMutualChapSettable: Optional[bool] = None

   class AuthenticationProperties(DynamicData):
      chapAuthEnabled: bool
      chapName: Optional[str] = None
      chapSecret: Optional[str] = None
      chapAuthenticationType: Optional[str] = None
      chapInherited: Optional[bool] = None
      mutualChapName: Optional[str] = None
      mutualChapSecret: Optional[str] = None
      mutualChapAuthenticationType: Optional[str] = None
      mutualChapInherited: Optional[bool] = None

   class DigestType(Enum):
      digestProhibited: ClassVar['DigestType'] = 'digestProhibited'
      digestDiscouraged: ClassVar['DigestType'] = 'digestDiscouraged'
      digestPreferred: ClassVar['DigestType'] = 'digestPreferred'
      digestRequired: ClassVar['DigestType'] = 'digestRequired'

   class DigestCapabilities(DynamicData):
      headerDigestSettable: Optional[bool] = None
      dataDigestSettable: Optional[bool] = None
      targetHeaderDigestSettable: Optional[bool] = None
      targetDataDigestSettable: Optional[bool] = None

   class DigestProperties(DynamicData):
      headerDigestType: Optional[str] = None
      headerDigestInherited: Optional[bool] = None
      dataDigestType: Optional[str] = None
      dataDigestInherited: Optional[bool] = None

   class IPCapabilities(DynamicData):
      addressSettable: bool
      ipConfigurationMethodSettable: bool
      subnetMaskSettable: bool
      defaultGatewaySettable: bool
      primaryDnsServerAddressSettable: bool
      alternateDnsServerAddressSettable: bool
      ipv6Supported: Optional[bool] = None
      arpRedirectSettable: Optional[bool] = None
      mtuSettable: Optional[bool] = None
      hostNameAsTargetAddress: Optional[bool] = None
      nameAliasSettable: Optional[bool] = None
      ipv4EnableSettable: Optional[bool] = None
      ipv6EnableSettable: Optional[bool] = None
      ipv6PrefixLengthSettable: Optional[bool] = None
      ipv6PrefixLength: Optional[int] = None
      ipv6DhcpConfigurationSettable: Optional[bool] = None
      ipv6LinkLocalAutoConfigurationSettable: Optional[bool] = None
      ipv6RouterAdvertisementConfigurationSettable: Optional[bool] = None
      ipv6DefaultGatewaySettable: Optional[bool] = None
      ipv6MaxStaticAddressesSupported: Optional[int] = None

   class IscsiIpv6Address(DynamicData):
      class AddressConfigurationType(Enum):
         DHCP: ClassVar['AddressConfigurationType'] = 'DHCP'
         AutoConfigured: ClassVar['AddressConfigurationType'] = 'AutoConfigured'
         Static: ClassVar['AddressConfigurationType'] = 'Static'
         Other: ClassVar['AddressConfigurationType'] = 'Other'

      class IPv6AddressOperation(Enum):
         add: ClassVar['IPv6AddressOperation'] = 'add'
         remove: ClassVar['IPv6AddressOperation'] = 'remove'

      address: str
      prefixLength: int
      origin: str
      operation: Optional[str] = None

   class IPv6Properties(DynamicData):
      iscsiIpv6Address: list[IscsiIpv6Address] = []
      ipv6DhcpConfigurationEnabled: Optional[bool] = None
      ipv6LinkLocalAutoConfigurationEnabled: Optional[bool] = None
      ipv6RouterAdvertisementConfigurationEnabled: Optional[bool] = None
      ipv6DefaultGateway: Optional[str] = None

   class IPProperties(DynamicData):
      mac: Optional[str] = None
      address: Optional[str] = None
      dhcpConfigurationEnabled: bool
      subnetMask: Optional[str] = None
      defaultGateway: Optional[str] = None
      primaryDnsServerAddress: Optional[str] = None
      alternateDnsServerAddress: Optional[str] = None
      ipv6Address: Optional[str] = None
      ipv6SubnetMask: Optional[str] = None
      ipv6DefaultGateway: Optional[str] = None
      arpRedirectEnabled: Optional[bool] = None
      mtu: Optional[int] = None
      jumboFramesEnabled: Optional[bool] = None
      ipv4Enabled: Optional[bool] = None
      ipv6Enabled: Optional[bool] = None
      ipv6properties: Optional[IPv6Properties] = None

   class SendTarget(DynamicData):
      address: str
      port: Optional[int] = None
      authenticationProperties: Optional[AuthenticationProperties] = None
      digestProperties: Optional[DigestProperties] = None
      supportedAdvancedOptions: list[OptionDef] = []
      advancedOptions: list[ParamValue] = []
      parent: Optional[str] = None

   class StaticTarget(DynamicData):
      class TargetDiscoveryMethod(Enum):
         staticMethod: ClassVar['TargetDiscoveryMethod'] = 'staticMethod'
         sendTargetMethod: ClassVar['TargetDiscoveryMethod'] = 'sendTargetMethod'
         slpMethod: ClassVar['TargetDiscoveryMethod'] = 'slpMethod'
         isnsMethod: ClassVar['TargetDiscoveryMethod'] = 'isnsMethod'
         unknownMethod: ClassVar['TargetDiscoveryMethod'] = 'unknownMethod'

      address: str
      port: Optional[int] = None
      iScsiName: str
      discoveryMethod: Optional[str] = None
      authenticationProperties: Optional[AuthenticationProperties] = None
      digestProperties: Optional[DigestProperties] = None
      supportedAdvancedOptions: list[OptionDef] = []
      advancedOptions: list[ParamValue] = []
      parent: Optional[str] = None

   class TargetSet(DynamicData):
      staticTargets: list[StaticTarget] = []
      sendTargets: list[SendTarget] = []

   class NetworkBindingSupportType(Enum):
      notsupported: ClassVar['NetworkBindingSupportType'] = 'notsupported'
      optional: ClassVar['NetworkBindingSupportType'] = 'optional'
      required: ClassVar['NetworkBindingSupportType'] = 'required'

   isSoftwareBased: bool
   canBeDisabled: Optional[bool] = None
   networkBindingSupport: Optional[NetworkBindingSupportType] = None
   discoveryCapabilities: DiscoveryCapabilities
   discoveryProperties: DiscoveryProperties
   authenticationCapabilities: AuthenticationCapabilities
   authenticationProperties: AuthenticationProperties
   digestCapabilities: Optional[DigestCapabilities] = None
   digestProperties: Optional[DigestProperties] = None
   ipCapabilities: IPCapabilities
   ipProperties: IPProperties
   supportedAdvancedOptions: list[OptionDef] = []
   advancedOptions: list[ParamValue] = []
   iScsiName: str
   iScsiAlias: Optional[str] = None
   configuredSendTarget: list[SendTarget] = []
   configuredStaticTarget: list[StaticTarget] = []
   maxSpeedMb: Optional[int] = None
   currentSpeedMb: Optional[int] = None


class InternetScsiTargetTransport(TargetTransport):
   iScsiName: str
   iScsiAlias: str
   address: list[str] = []


class IpConfig(DynamicData):
   class IpV6AddressConfigType(Enum):
      other: ClassVar['IpV6AddressConfigType'] = 'other'
      manual: ClassVar['IpV6AddressConfigType'] = 'manual'
      dhcp: ClassVar['IpV6AddressConfigType'] = 'dhcp'
      linklayer: ClassVar['IpV6AddressConfigType'] = 'linklayer'
      random: ClassVar['IpV6AddressConfigType'] = 'random'

   class IpV6AddressStatus(Enum):
      preferred: ClassVar['IpV6AddressStatus'] = 'preferred'
      deprecated: ClassVar['IpV6AddressStatus'] = 'deprecated'
      invalid: ClassVar['IpV6AddressStatus'] = 'invalid'
      inaccessible: ClassVar['IpV6AddressStatus'] = 'inaccessible'
      unknown: ClassVar['IpV6AddressStatus'] = 'unknown'
      tentative: ClassVar['IpV6AddressStatus'] = 'tentative'
      duplicate: ClassVar['IpV6AddressStatus'] = 'duplicate'

   class IpV6Address(DynamicData):
      ipAddress: str
      prefixLength: int
      origin: Optional[str] = None
      dadState: Optional[str] = None
      lifetime: Optional[datetime] = None
      operation: Optional[str] = None

   class IpV6AddressConfiguration(DynamicData):
      ipV6Address: list[IpV6Address] = []
      autoConfigurationEnabled: Optional[bool] = None
      dhcpV6Enabled: Optional[bool] = None

   dhcp: bool
   ipAddress: Optional[str] = None
   subnetMask: Optional[str] = None
   ipV6Config: Optional[IpV6AddressConfiguration] = None


class IpRouteConfig(DynamicData):
   defaultGateway: Optional[str] = None
   gatewayDevice: Optional[str] = None
   ipV6DefaultGateway: Optional[str] = None
   ipV6GatewayDevice: Optional[str] = None


class IpRouteConfigSpec(IpRouteConfig):
   gatewayDeviceConnection: Optional[VirtualNicConnection] = None
   ipV6GatewayDeviceConnection: Optional[VirtualNicConnection] = None


class IpRouteEntry(DynamicData):
   network: str
   prefixLength: int
   gateway: str
   deviceName: Optional[str] = None


class IpRouteOp(DynamicData):
   changeOperation: str
   route: IpRouteEntry


class IpRouteTableConfig(DynamicData):
   ipRoute: list[IpRouteOp] = []
   ipv6Route: list[IpRouteOp] = []


class IpRouteTableInfo(DynamicData):
   ipRoute: list[IpRouteEntry] = []
   ipv6Route: list[IpRouteEntry] = []


class IpmiInfo(DynamicData):
   bmcIpAddress: Optional[str] = None
   bmcMacAddress: Optional[str] = None
   login: Optional[str] = None
   password: Optional[str] = None


class IscsiManager(ManagedObject):
   class IscsiStatus(DynamicData):
      reason: list[MethodFault] = []

   class IscsiPortInfo(DynamicData):
      class PathStatus(Enum):
         notUsed: ClassVar['PathStatus'] = 'notUsed'
         active: ClassVar['PathStatus'] = 'active'
         standBy: ClassVar['PathStatus'] = 'standBy'
         lastActive: ClassVar['PathStatus'] = 'lastActive'

      vnicDevice: Optional[str] = None
      vnic: Optional[VirtualNic] = None
      pnicDevice: Optional[str] = None
      pnic: Optional[PhysicalNic] = None
      switchName: Optional[str] = None
      switchUuid: Optional[str] = None
      portgroupName: Optional[str] = None
      portgroupKey: Optional[str] = None
      portKey: Optional[str] = None
      opaqueNetworkId: Optional[str] = None
      opaqueNetworkType: Optional[str] = None
      opaqueNetworkName: Optional[str] = None
      externalId: Optional[str] = None
      complianceStatus: Optional[IscsiStatus] = None
      pathStatus: Optional[str] = None

   class IscsiDependencyEntity(DynamicData):
      pnicDevice: str
      vnicDevice: str
      vmhbaName: str

   class IscsiMigrationDependency(DynamicData):
      migrationAllowed: bool
      disallowReason: Optional[IscsiStatus] = None
      dependency: list[IscsiDependencyEntity] = []

   def QueryVnicStatus(self, vnicDevice: str) -> IscsiStatus: ...
   def QueryPnicStatus(self, pnicDevice: str) -> IscsiStatus: ...
   def QueryBoundVnics(self, iScsiHbaName: str) -> list[IscsiPortInfo]: ...
   def QueryCandidateNics(self, iScsiHbaName: str) -> list[IscsiPortInfo]: ...
   def BindVnic(self, iScsiHbaName: str, vnicDevice: str) -> None: ...
   def UnbindVnic(self, iScsiHbaName: str, vnicDevice: str, force: bool) -> None: ...
   def QueryMigrationDependencies(self, pnicDevice: list[str]) -> IscsiMigrationDependency: ...


class KernelModuleSystem(ManagedObject):
   class ModuleInfo(DynamicData):
      class SectionInfo(DynamicData):
         address: long
         length: Optional[int] = None

      id: int
      name: str
      version: str
      filename: str
      optionString: str
      loaded: bool
      enabled: bool
      useCount: int
      readOnlySection: SectionInfo
      writableSection: SectionInfo
      textSection: SectionInfo
      dataSection: SectionInfo
      bssSection: SectionInfo

   def QueryModules(self) -> list[ModuleInfo]: ...
   def UpdateModuleOptionString(self, name: str, options: str) -> None: ...
   def QueryConfiguredModuleOptionString(self, name: str) -> str: ...


class LACPInfo(DynamicData):
   dvsName: str
   lags: list[LAGInfo] = []


class LAGInfo(DynamicData):
   lagName: str
   groupState: int
   vnics: list[str] = []
   uplinks: list[LAGUplinkInfo] = []


class LAGUplinkInfo(DynamicData):
   uplinkName: str
   portState: int
   bundleState: str


class LicenseSpec(DynamicData):
   source: Optional[LicenseManager.LicenseSource] = None
   editionKey: Optional[str] = None
   disabledFeatureKey: list[str] = []
   enabledFeatureKey: list[str] = []


class LinkDiscoveryProtocolConfig(DynamicData):
   class ProtocolType(Enum):
      cdp: ClassVar['ProtocolType'] = 'cdp'
      lldp: ClassVar['ProtocolType'] = 'lldp'

   class OperationType(Enum):
      none: ClassVar['OperationType'] = 'none'
      listen: ClassVar['OperationType'] = 'listen'
      advertise: ClassVar['OperationType'] = 'advertise'
      both: ClassVar['OperationType'] = 'both'

   protocol: str
   operation: str


class LocalAccountManager(ManagedObject):
   class AccountSpecification(DynamicData):
      id: str
      password: Optional[str] = None
      description: Optional[str] = None

   class PosixAccountSpecification(AccountSpecification):
      posixId: Optional[int] = None
      shellAccess: Optional[bool] = None

   def CreateUser(self, user: AccountSpecification) -> None: ...
   def UpdateUser(self, user: AccountSpecification) -> None: ...
   def CreateGroup(self, group: AccountSpecification) -> None: ...
   def RemoveUser(self, userName: str) -> None: ...
   def RemoveGroup(self, groupName: str) -> None: ...
   def AssignUserToGroup(self, user: str, group: str) -> None: ...
   def UnassignUserFromGroup(self, user: str, group: str) -> None: ...
   def ChangePassword(self, user: str, oldPassword: str, newPassword: str) -> None: ...

class LocalAuthentication(AuthenticationStore):
   pass

class LocalAuthenticationInfo(AuthenticationStoreInfo):
   pass


class LocalDatastoreInfo(Datastore.Info):
   path: Optional[str] = None


class LocalFileSystemVolume(FileSystemVolume):
   class Specification(DynamicData):
      device: str
      localPath: str

   device: str


class MaintenanceSpec(DynamicData):
   class Purpose(Enum):
      hostUpgrade: ClassVar['Purpose'] = 'hostUpgrade'

   class EvacuationMode(DynamicData):
      workloadNonDisruptive: bool

   vsanMode: Optional[DecommissionMode] = None
   purpose: Optional[str] = None
   evacMode: Optional[EvacuationMode] = None


class MemoryManagerSystem(ExtensibleManagedObject):
   class ServiceConsoleReservationInfo(DynamicData):
      serviceConsoleReservedCfg: long
      serviceConsoleReserved: long
      unreserved: long

   class VirtualMachineReservationInfo(DynamicData):
      class AllocationPolicy(Enum):
         swapNone: ClassVar['AllocationPolicy'] = 'swapNone'
         swapSome: ClassVar['AllocationPolicy'] = 'swapSome'
         swapMost: ClassVar['AllocationPolicy'] = 'swapMost'

      virtualMachineMin: long
      virtualMachineMax: long
      virtualMachineReserved: long
      allocationPolicy: str

   class VirtualMachineReservationSpec(DynamicData):
      virtualMachineReserved: Optional[long] = None
      allocationPolicy: Optional[str] = None

   @property
   def consoleReservationInfo(self) -> Optional[ServiceConsoleReservationInfo]: ...
   @property
   def virtualMachineReservationInfo(self) -> Optional[VirtualMachineReservationInfo]: ...

   def ReconfigureServiceConsoleReservation(self, cfgBytes: long) -> None: ...
   def ReconfigureVirtualMachineReservation(self, spec: VirtualMachineReservationSpec) -> None: ...


class MemorySpec(DynamicData):
   serviceConsoleReservation: Optional[long] = None

class MemoryTierFlags:
   pass


class MemoryTierInfo(DynamicData):
   name: str
   type: str
   flags: list[str] = []
   internalFlags: list[str] = []
   size: long

class MemoryTierType:
   pass

class MemoryTieringType:
   pass


class MessageBusProxy(ManagedObject):
   pass


class MountInfo(DynamicData):
   class AccessMode(Enum):
      readWrite: ClassVar['AccessMode'] = 'readWrite'
      readOnly: ClassVar['AccessMode'] = 'readOnly'

   class InaccessibleReason(Enum):
      AllPathsDown_Start: ClassVar['InaccessibleReason'] = 'AllPathsDown_Start'
      AllPathsDown_Timeout: ClassVar['InaccessibleReason'] = 'AllPathsDown_Timeout'
      PermanentDeviceLoss: ClassVar['InaccessibleReason'] = 'PermanentDeviceLoss'

   class MountFailedReason(Enum):
      CONNECT_FAILURE: ClassVar['MountFailedReason'] = 'CONNECT_FAILURE'
      MOUNT_NOT_SUPPORTED: ClassVar['MountFailedReason'] = 'MOUNT_NOT_SUPPORTED'
      NFS_NOT_SUPPORTED: ClassVar['MountFailedReason'] = 'NFS_NOT_SUPPORTED'
      MOUNT_DENIED: ClassVar['MountFailedReason'] = 'MOUNT_DENIED'
      MOUNT_NOT_DIR: ClassVar['MountFailedReason'] = 'MOUNT_NOT_DIR'
      VOLUME_LIMIT_EXCEEDED: ClassVar['MountFailedReason'] = 'VOLUME_LIMIT_EXCEEDED'
      CONN_LIMIT_EXCEEDED: ClassVar['MountFailedReason'] = 'CONN_LIMIT_EXCEEDED'
      MOUNT_EXISTS: ClassVar['MountFailedReason'] = 'MOUNT_EXISTS'
      OTHERS: ClassVar['MountFailedReason'] = 'OTHERS'

   path: Optional[str] = None
   accessMode: str
   mounted: Optional[bool] = None
   accessible: Optional[bool] = None
   inaccessibleReason: Optional[str] = None
   vmknicName: Optional[str] = None
   vmknicActive: Optional[bool] = None
   mountFailedReason: Optional[str] = None
   numTcpConnections: Optional[int] = None


class MultipathInfo(DynamicData):
   class PathState(Enum):
      standby: ClassVar['PathState'] = 'standby'
      active: ClassVar['PathState'] = 'active'
      disabled: ClassVar['PathState'] = 'disabled'
      dead: ClassVar['PathState'] = 'dead'
      unknown: ClassVar['PathState'] = 'unknown'

   class LogicalUnitPolicy(DynamicData):
      policy: str

   class HppLogicalUnitPolicy(LogicalUnitPolicy):
      bytes: Optional[long] = None
      iops: Optional[long] = None
      path: Optional[str] = None
      latencyEvalTime: Optional[long] = None
      samplingIosPerPath: Optional[long] = None

   class LogicalUnitStorageArrayTypePolicy(DynamicData):
      policy: str

   class FixedLogicalUnitPolicy(LogicalUnitPolicy):
      prefer: str

   class LogicalUnit(DynamicData):
      key: str
      id: str
      lun: ScsiLun
      path: list[Path] = []
      policy: LogicalUnitPolicy
      storageArrayTypePolicy: Optional[LogicalUnitStorageArrayTypePolicy] = None

   class Path(DynamicData):
      key: str
      name: str
      pathState: str
      state: Optional[str] = None
      isWorkingPath: Optional[bool] = None
      adapter: HostBusAdapter
      lun: LogicalUnit
      transport: Optional[TargetTransport] = None

   lun: list[LogicalUnit] = []


class MultipathStateInfo(DynamicData):
   class Path(DynamicData):
      name: str
      pathState: str

   path: list[Path] = []


class NasDatastoreInfo(Datastore.Info):
   nas: Optional[NasVolume] = None


class NasVolume(FileSystemVolume):
   class UserInfo(DynamicData):
      user: str

   class SecurityType(Enum):
      AUTH_SYS: ClassVar['SecurityType'] = 'AUTH_SYS'
      SEC_KRB5: ClassVar['SecurityType'] = 'SEC_KRB5'
      SEC_KRB5I: ClassVar['SecurityType'] = 'SEC_KRB5I'
      SEC_KRB5P: ClassVar['SecurityType'] = 'SEC_KRB5P'

   class Specification(DynamicData):
      remoteHost: str
      remotePath: str
      localPath: str
      accessMode: str
      type: Optional[str] = None
      userName: Optional[str] = None
      password: Optional[str] = None
      remoteHostNames: list[str] = []
      securityType: Optional[str] = None
      vmknicToBind: Optional[str] = None
      vmknicBound: Optional[bool] = None
      connections: Optional[int] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      spec: Optional[Specification] = None

   remoteHost: str
   remotePath: str
   userName: Optional[str] = None
   remoteHostNames: list[str] = []
   securityType: Optional[str] = None
   protocolEndpoint: Optional[bool] = None


class NatService(DynamicData):
   class PortForwardSpecification(DynamicData):
      type: str
      name: str
      hostPort: int
      guestPort: int
      guestIpAddress: str

   class NameServiceSpec(DynamicData):
      dnsAutoDetect: bool
      dnsPolicy: str
      dnsRetries: int
      dnsTimeout: int
      dnsNameServer: list[str] = []
      nbdsTimeout: int
      nbnsRetries: int
      nbnsTimeout: int

   class Specification(DynamicData):
      virtualSwitch: str
      activeFtp: bool
      allowAnyOui: bool
      configPort: bool
      ipGatewayAddress: str
      udpTimeout: int
      portForward: list[PortForwardSpecification] = []
      nameService: Optional[NameServiceSpec] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      key: str
      spec: Specification

   key: str
   spec: Specification


class NetCapabilities(DynamicData):
   canSetPhysicalNicLinkSpeed: bool
   supportsNicTeaming: bool
   nicTeamingPolicy: list[str] = []
   supportsVlan: bool
   usesServiceConsoleNic: bool
   supportsNetworkHints: bool
   maxPortGroupsPerVswitch: Optional[int] = None
   vswitchConfigSupported: bool
   vnicConfigSupported: bool
   ipRouteConfigSupported: bool
   dnsConfigSupported: bool
   dhcpOnVnicSupported: bool
   ipV6Supported: bool
   backupNfcNiocSupported: Optional[bool] = None


class NetOffloadCapabilities(DynamicData):
   csumOffload: Optional[bool] = None
   tcpSegmentation: Optional[bool] = None
   zeroCopyXmit: Optional[bool] = None


class NetStackInstance(DynamicData):
   class SystemStackKey(Enum):
      defaultTcpipStack: ClassVar['SystemStackKey'] = 'defaultTcpipStack'
      vmotion: ClassVar['SystemStackKey'] = 'vmotion'
      vSphereProvisioning: ClassVar['SystemStackKey'] = 'vSphereProvisioning'
      mirror: ClassVar['SystemStackKey'] = 'mirror'
      ops: ClassVar['SystemStackKey'] = 'ops'
      vnetworking: ClassVar['SystemStackKey'] = 'vnetworking'

   class CongestionControlAlgorithmType(Enum):
      newreno: ClassVar['CongestionControlAlgorithmType'] = 'newreno'
      cubic: ClassVar['CongestionControlAlgorithmType'] = 'cubic'

   key: Optional[str] = None
   name: Optional[str] = None
   dnsConfig: Optional[DnsConfig] = None
   ipRouteConfig: Optional[IpRouteConfig] = None
   requestedMaxNumberOfConnections: Optional[int] = None
   congestionControlAlgorithm: Optional[str] = None
   ipV6Enabled: Optional[bool] = None
   routeTableConfig: Optional[IpRouteTableConfig] = None
   owner: Optional[str] = None


class NetworkConfig(DynamicData):
   class Result(DynamicData):
      vnicDevice: list[str] = []
      consoleVnicDevice: list[str] = []

   class NetStackSpec(DynamicData):
      netStackInstance: NetStackInstance
      operation: Optional[str] = None

   vswitch: list[VirtualSwitch.Config] = []
   proxySwitch: list[HostProxySwitch.Config] = []
   portgroup: list[PortGroup.Config] = []
   pnic: list[PhysicalNic.Config] = []
   vnic: list[VirtualNic.Config] = []
   consoleVnic: list[VirtualNic.Config] = []
   dnsConfig: Optional[DnsConfig] = None
   ipRouteConfig: Optional[IpRouteConfig] = None
   consoleIpRouteConfig: Optional[IpRouteConfig] = None
   routeTableConfig: Optional[IpRouteTableConfig] = None
   dhcp: list[DhcpService.Config] = []
   nat: list[NatService.Config] = []
   ipV6Enabled: Optional[bool] = None
   netStackSpec: list[NetStackSpec] = []
   migrationStatus: Optional[str] = None


class NetworkInfo(DynamicData):
   vswitch: list[VirtualSwitch] = []
   proxySwitch: list[HostProxySwitch] = []
   portgroup: list[PortGroup] = []
   pnic: list[PhysicalNic] = []
   rdmaDevice: list[RdmaDevice] = []
   vnic: list[VirtualNic] = []
   consoleVnic: list[VirtualNic] = []
   dnsConfig: Optional[DnsConfig] = None
   ipRouteConfig: Optional[IpRouteConfig] = None
   consoleIpRouteConfig: Optional[IpRouteConfig] = None
   routeTableInfo: Optional[IpRouteTableInfo] = None
   dhcp: list[DhcpService] = []
   nat: list[NatService] = []
   ipV6Enabled: Optional[bool] = None
   atBootIpV6Enabled: Optional[bool] = None
   netStackInstance: list[NetStackInstance] = []
   opaqueSwitch: list[OpaqueSwitch] = []
   opaqueNetwork: list[OpaqueNetworkInfo] = []
   nsxTransportNodeId: Optional[str] = None
   nvdsToVdsMigrationRequired: Optional[bool] = None
   migrationStatus: Optional[str] = None


class NetworkPolicy(DynamicData):
   class SecurityPolicy(DynamicData):
      allowPromiscuous: Optional[bool] = None
      macChanges: Optional[bool] = None
      forgedTransmits: Optional[bool] = None

   class TrafficShapingPolicy(DynamicData):
      enabled: Optional[bool] = None
      averageBandwidth: Optional[long] = None
      peakBandwidth: Optional[long] = None
      burstSize: Optional[long] = None

   class NicFailureCriteria(DynamicData):
      checkSpeed: Optional[str] = None
      speed: Optional[int] = None
      checkDuplex: Optional[bool] = None
      fullDuplex: Optional[bool] = None
      checkErrorPercent: Optional[bool] = None
      percentage: Optional[int] = None
      checkBeacon: Optional[bool] = None

   class NicOrderPolicy(DynamicData):
      activeNic: list[str] = []
      standbyNic: list[str] = []

   class NicTeamingPolicy(DynamicData):
      policy: Optional[str] = None
      reversePolicy: Optional[bool] = None
      notifySwitches: Optional[bool] = None
      rollingOrder: Optional[bool] = None
      failureCriteria: Optional[NicFailureCriteria] = None
      nicOrder: Optional[NicOrderPolicy] = None

   security: Optional[SecurityPolicy] = None
   nicTeaming: Optional[NicTeamingPolicy] = None
   offloadPolicy: Optional[NetOffloadCapabilities] = None
   shapingPolicy: Optional[TrafficShapingPolicy] = None


class NetworkSystem(ExtensibleManagedObject):
   @property
   def capabilities(self) -> Optional[NetCapabilities]: ...
   @property
   def networkInfo(self) -> Optional[NetworkInfo]: ...
   @property
   def offloadCapabilities(self) -> Optional[NetOffloadCapabilities]: ...
   @property
   def networkConfig(self) -> Optional[NetworkConfig]: ...
   @property
   def dnsConfig(self) -> Optional[DnsConfig]: ...
   @property
   def ipRouteConfig(self) -> Optional[IpRouteConfig]: ...
   @property
   def consoleIpRouteConfig(self) -> Optional[IpRouteConfig]: ...

   def UpdateNetworkConfig(self, config: NetworkConfig, changeMode: str) -> NetworkConfig.Result: ...
   def UpdateDnsConfig(self, config: DnsConfig) -> None: ...
   def UpdateIpRouteConfig(self, config: IpRouteConfig) -> None: ...
   def UpdateConsoleIpRouteConfig(self, config: IpRouteConfig) -> None: ...
   def UpdateIpRouteTableConfig(self, config: IpRouteTableConfig) -> None: ...
   def AddVirtualSwitch(self, vswitchName: str, spec: Optional[VirtualSwitch.Specification]) -> None: ...
   def RemoveVirtualSwitch(self, vswitchName: str) -> None: ...
   def UpdateVirtualSwitch(self, vswitchName: str, spec: VirtualSwitch.Specification) -> None: ...
   def AddPortGroup(self, portgrp: PortGroup.Specification) -> None: ...
   def RemovePortGroup(self, pgName: str) -> None: ...
   def UpdatePortGroup(self, pgName: str, portgrp: PortGroup.Specification) -> None: ...
   def UpdatePhysicalNicLinkSpeed(self, device: str, linkSpeed: Optional[PhysicalNic.LinkSpeedDuplex]) -> None: ...
   def QueryNetworkHint(self, device: list[str]) -> list[PhysicalNic.NetworkHint]: ...
   def AddVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
   def RemoveVirtualNic(self, device: str) -> None: ...
   def UpdateVirtualNic(self, device: str, nic: VirtualNic.Specification) -> None: ...
   def AddServiceConsoleVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
   def RemoveServiceConsoleVirtualNic(self, device: str) -> None: ...
   def UpdateServiceConsoleVirtualNic(self, device: str, nic: VirtualNic.Specification) -> None: ...
   def RestartServiceConsoleVirtualNic(self, device: str) -> None: ...
   def Refresh(self) -> None: ...
   def StartDpuFailover(self, dvsName: str, targetDpuAlias: Optional[str]) -> None: ...


class NfcConnectionInfo(DataTransportConnectionInfo):
   streamingMemoryConsumed: Optional[long] = None


class NtpConfig(DynamicData):
   server: list[str] = []
   configFile: list[str] = []


class NumaInfo(DynamicData):
   type: str
   numNodes: int
   numaNode: list[NumaNode] = []


class NumaNode(DynamicData):
   typeId: byte
   cpuID: list[short] = []
   memorySize: Optional[long] = None
   memoryRangeBegin: long
   memoryRangeLength: long
   pciId: list[str] = []


class NumericSensorInfo(DynamicData):
   class HealthState(Enum):
      unknown: ClassVar['HealthState'] = 'unknown'
      green: ClassVar['HealthState'] = 'green'
      yellow: ClassVar['HealthState'] = 'yellow'
      red: ClassVar['HealthState'] = 'red'

   class SensorType(Enum):
      fan: ClassVar['SensorType'] = 'fan'
      power: ClassVar['SensorType'] = 'power'
      temperature: ClassVar['SensorType'] = 'temperature'
      voltage: ClassVar['SensorType'] = 'voltage'
      other: ClassVar['SensorType'] = 'other'
      processor: ClassVar['SensorType'] = 'processor'
      memory: ClassVar['SensorType'] = 'memory'
      storage: ClassVar['SensorType'] = 'storage'
      systemBoard: ClassVar['SensorType'] = 'systemBoard'
      battery: ClassVar['SensorType'] = 'battery'
      bios: ClassVar['SensorType'] = 'bios'
      cable: ClassVar['SensorType'] = 'cable'
      watchdog: ClassVar['SensorType'] = 'watchdog'

   name: str
   healthState: Optional[ElementDescription] = None
   currentReading: long
   unitModifier: int
   baseUnits: str
   rateUnits: Optional[str] = None
   sensorType: str
   id: Optional[str] = None
   sensorNumber: Optional[long] = None
   timeStamp: Optional[str] = None
   fru: Optional[Fru] = None


class NvdimmSystem(ManagedObject):
   class RangeType(Enum):
      volatileRange: ClassVar['RangeType'] = 'volatileRange'
      persistentRange: ClassVar['RangeType'] = 'persistentRange'
      controlRange: ClassVar['RangeType'] = 'controlRange'
      blockRange: ClassVar['RangeType'] = 'blockRange'
      volatileVirtualDiskRange: ClassVar['RangeType'] = 'volatileVirtualDiskRange'
      volatileVirtualCDRange: ClassVar['RangeType'] = 'volatileVirtualCDRange'
      persistentVirtualDiskRange: ClassVar['RangeType'] = 'persistentVirtualDiskRange'
      persistentVirtualCDRange: ClassVar['RangeType'] = 'persistentVirtualCDRange'

   class NamespaceType(Enum):
      blockNamespace: ClassVar['NamespaceType'] = 'blockNamespace'
      persistentNamespace: ClassVar['NamespaceType'] = 'persistentNamespace'

   class HealthInfo(DynamicData):
      class StateFlag(Enum):
         normal: ClassVar['StateFlag'] = 'normal'
         error: ClassVar['StateFlag'] = 'error'

      healthStatus: str
      healthInformation: str
      stateFlagInfo: list[str] = []
      dimmTemperature: int
      dimmTemperatureThreshold: int
      spareBlocksPercentage: int
      spareBlockThreshold: int
      dimmLifespanPercentage: int
      esTemperature: Optional[int] = None
      esTemperatureThreshold: Optional[int] = None
      esLifespanPercentage: Optional[int] = None

   class RegionInfo(DynamicData):
      regionId: int
      setId: int
      rangeType: str
      startAddr: long
      size: long
      offset: long

   class Summary(DynamicData):
      numDimms: int
      healthStatus: str
      totalCapacity: long
      persistentCapacity: long
      blockCapacity: long
      availableCapacity: long
      numInterleavesets: int
      numNamespaces: int

   class DimmInfo(DynamicData):
      dimmHandle: int
      healthInfo: HealthInfo
      totalCapacity: long
      persistentCapacity: long
      availablePersistentCapacity: long
      volatileCapacity: long
      availableVolatileCapacity: long
      blockCapacity: long
      regionInfo: list[RegionInfo] = []
      representationString: str

   class InterleaveSetInfo(DynamicData):
      class InterleaveSetState(Enum):
         invalid: ClassVar['InterleaveSetState'] = 'invalid'
         active: ClassVar['InterleaveSetState'] = 'active'

      setId: int
      rangeType: str
      baseAddress: long
      size: long
      availableSize: long
      deviceList: list[int] = []
      state: str

   class Guid(DynamicData):
      uuid: str

   class NamespaceInfo(DynamicData):
      class NamespaceHealthStatus(Enum):
         normal: ClassVar['NamespaceHealthStatus'] = 'normal'
         missing: ClassVar['NamespaceHealthStatus'] = 'missing'
         labelMissing: ClassVar['NamespaceHealthStatus'] = 'labelMissing'
         interleaveBroken: ClassVar['NamespaceHealthStatus'] = 'interleaveBroken'
         labelInconsistent: ClassVar['NamespaceHealthStatus'] = 'labelInconsistent'
         bttCorrupt: ClassVar['NamespaceHealthStatus'] = 'bttCorrupt'
         badBlockSize: ClassVar['NamespaceHealthStatus'] = 'badBlockSize'

      class NamespaceState(Enum):
         invalid: ClassVar['NamespaceState'] = 'invalid'
         notInUse: ClassVar['NamespaceState'] = 'notInUse'
         inUse: ClassVar['NamespaceState'] = 'inUse'

      uuid: str
      friendlyName: str
      blockSize: long
      blockCount: long
      type: str
      namespaceHealthStatus: str
      locationID: int
      state: str

   class NamespaceDetails(DynamicData):
      class NamespaceHealthStatus(Enum):
         normal: ClassVar['NamespaceHealthStatus'] = 'normal'
         missing: ClassVar['NamespaceHealthStatus'] = 'missing'
         labelMissing: ClassVar['NamespaceHealthStatus'] = 'labelMissing'
         interleaveBroken: ClassVar['NamespaceHealthStatus'] = 'interleaveBroken'
         labelInconsistent: ClassVar['NamespaceHealthStatus'] = 'labelInconsistent'

      class NamespaceState(Enum):
         invalid: ClassVar['NamespaceState'] = 'invalid'
         notInUse: ClassVar['NamespaceState'] = 'notInUse'
         inUse: ClassVar['NamespaceState'] = 'inUse'

      uuid: str
      friendlyName: str
      size: long
      type: str
      namespaceHealthStatus: str
      interleavesetID: int
      state: str

   class NamespaceCreateSpec(DynamicData):
      friendlyName: Optional[str] = None
      blockSize: long
      blockCount: long
      type: str
      locationID: int

   class PMemNamespaceCreateSpec(DynamicData):
      friendlyName: Optional[str] = None
      size: long
      interleavesetID: int

   class NamespaceDeleteSpec(DynamicData):
      uuid: str

   class NvdimmSystemInfo(DynamicData):
      summary: Optional[Summary] = None
      dimms: list[int] = []
      dimmInfo: list[DimmInfo] = []
      interleaveSet: list[int] = []
      iSetInfo: list[InterleaveSetInfo] = []
      namespace: list[Guid] = []
      nsInfo: list[NamespaceInfo] = []
      nsDetails: list[NamespaceDetails] = []

   @property
   def nvdimmSystemInfo(self) -> NvdimmSystemInfo: ...

   def CreateNamespace(self, createSpec: NamespaceCreateSpec) -> Task: ...
   def CreatePMemNamespace(self, createSpec: PMemNamespaceCreateSpec) -> Task: ...
   def DeleteNamespace(self, deleteSpec: NamespaceDeleteSpec) -> Task: ...
   def DeleteBlockNamespaces(self) -> Task: ...


class NvmeConnectSpec(NvmeSpec):
   subnqn: str
   controllerId: Optional[int] = None
   adminQueueSize: Optional[int] = None
   keepAliveTimeout: Optional[int] = None


class NvmeController(DynamicData):
   key: str
   controllerNumber: int
   subnqn: str
   name: str
   associatedAdapter: HostBusAdapter
   transportType: str
   fusedOperationSupported: bool
   numberOfQueues: int
   queueSize: int
   attachedNamespace: list[NvmeNamespace] = []
   vendorId: Optional[str] = None
   model: Optional[str] = None
   serialNumber: Optional[str] = None
   firmwareVersion: Optional[str] = None


class NvmeDisconnectSpec(DynamicData):
   hbaName: str
   subnqn: Optional[str] = None
   controllerNumber: Optional[int] = None


class NvmeDiscoverSpec(NvmeSpec):
   autoConnect: Optional[bool] = None
   rootDiscoveryController: Optional[bool] = None


class NvmeDiscoveryLog(DynamicData):
   class SubsystemType(Enum):
      discovery: ClassVar['SubsystemType'] = 'discovery'
      nvm: ClassVar['SubsystemType'] = 'nvm'

   class TransportRequirements(Enum):
      secureChannelRequired: ClassVar['TransportRequirements'] = 'secureChannelRequired'
      secureChannelNotRequired: ClassVar['TransportRequirements'] = 'secureChannelNotRequired'
      requirementsNotSpecified: ClassVar['TransportRequirements'] = 'requirementsNotSpecified'

   class Entry(DynamicData):
      subnqn: str
      subsystemType: str
      subsystemPortId: int
      controllerId: int
      adminQueueMaxSize: int
      transportParameters: NvmeTransportParameters
      transportRequirements: str
      connected: bool

   entry: list[Entry] = []
   complete: bool


class NvmeNamespace(DynamicData):
   key: str
   name: str
   id: int
   blockSize: int
   capacityInBlocks: long


class NvmeOpaqueTransportParameters(NvmeTransportParameters):
   trtype: str
   traddr: str
   adrfam: str
   trsvcid: str
   tsas: binary


class NvmeOverFibreChannelParameters(NvmeTransportParameters):
   nodeWorldWideName: long
   portWorldWideName: long


class NvmeOverRdmaParameters(NvmeTransportParameters):
   address: str
   addressFamily: Optional[str] = None
   portNumber: Optional[int] = None


class NvmeOverTcpParameters(NvmeTransportParameters):
   address: str
   portNumber: Optional[int] = None
   digestVerification: Optional[str] = None


class NvmeSpec(DynamicData):
   hbaName: str
   transportParameters: NvmeTransportParameters


class NvmeTopology(DynamicData):
   class Interface(DynamicData):
      key: str
      adapter: HostBusAdapter
      connectedController: list[NvmeController] = []

   adapter: list[Interface] = []


class NvmeTransportParameters(DynamicData):
   class NvmeAddressFamily(Enum):
      ipv4: ClassVar['NvmeAddressFamily'] = 'ipv4'
      ipv6: ClassVar['NvmeAddressFamily'] = 'ipv6'
      infiniBand: ClassVar['NvmeAddressFamily'] = 'infiniBand'
      fc: ClassVar['NvmeAddressFamily'] = 'fc'
      loopback: ClassVar['NvmeAddressFamily'] = 'loopback'
      unknown: ClassVar['NvmeAddressFamily'] = 'unknown'

class NvmeTransportType:
   pass


class OpaqueNetworkInfo(DynamicData):
   opaqueNetworkId: str
   opaqueNetworkName: str
   opaqueNetworkType: str
   pnicZone: list[str] = []
   capability: Optional[OpaqueNetwork.Capability] = None
   extraConfig: list[OptionValue] = []


class OpaqueSwitch(DynamicData):
   class OpaqueSwitchState(Enum):
      up: ClassVar['OpaqueSwitchState'] = 'up'
      warning: ClassVar['OpaqueSwitchState'] = 'warning'
      down: ClassVar['OpaqueSwitchState'] = 'down'
      maintenance: ClassVar['OpaqueSwitchState'] = 'maintenance'

   class PhysicalNicZone(DynamicData):
      key: str
      pnicDevice: list[str] = []

   key: str
   name: Optional[str] = None
   pnic: list[PhysicalNic] = []
   pnicZone: list[PhysicalNicZone] = []
   status: Optional[str] = None
   vtep: list[VirtualNic] = []
   extraConfig: list[OptionValue] = []
   featureCapability: list[FeatureCapability] = []


class PMemDatastoreInfo(Datastore.Info):
   pmem: PMemVolume

class PMemVolume(FileSystemVolume):
   uuid: str
   version: str

class ParallelScsiHba(HostBusAdapter):
   pass

class ParallelScsiTargetTransport(TargetTransport):
   pass

class PartialMaintenanceModeId:
   pass


class PartialMaintenanceModeRuntimeInfo(DynamicData):
   key: str
   hostStatus: str

class PartialMaintenanceModeStatus:
   pass


class PatchManager(ManagedObject):
   class Result(DynamicData):
      version: str
      status: list[Status] = []
      xmlResult: Optional[str] = None

   class Status(DynamicData):
      class Reason(Enum):
         obsoleted: ClassVar['Reason'] = 'obsoleted'
         missingPatch: ClassVar['Reason'] = 'missingPatch'
         missingLib: ClassVar['Reason'] = 'missingLib'
         hasDependentPatch: ClassVar['Reason'] = 'hasDependentPatch'
         conflictPatch: ClassVar['Reason'] = 'conflictPatch'
         conflictLib: ClassVar['Reason'] = 'conflictLib'

      class Integrity(Enum):
         validated: ClassVar['Integrity'] = 'validated'
         keyNotFound: ClassVar['Integrity'] = 'keyNotFound'
         keyRevoked: ClassVar['Integrity'] = 'keyRevoked'
         keyExpired: ClassVar['Integrity'] = 'keyExpired'
         digestMismatch: ClassVar['Integrity'] = 'digestMismatch'
         notEnoughSignatures: ClassVar['Integrity'] = 'notEnoughSignatures'
         validationError: ClassVar['Integrity'] = 'validationError'

      class InstallState(Enum):
         hostRestarted: ClassVar['InstallState'] = 'hostRestarted'
         imageActive: ClassVar['InstallState'] = 'imageActive'

      class PrerequisitePatch(DynamicData):
         id: str
         installState: list[str] = []

      id: str
      applicable: bool
      reason: list[str] = []
      integrity: Optional[str] = None
      installed: bool
      installState: list[str] = []
      prerequisitePatch: list[PrerequisitePatch] = []
      restartRequired: bool
      reconnectRequired: bool
      vmOffRequired: bool
      supersededPatchIds: list[str] = []

   class Locator(DynamicData):
      url: str
      proxy: Optional[str] = None

   class PatchManagerOperationSpec(DynamicData):
      proxy: Optional[str] = None
      port: Optional[int] = None
      userName: Optional[str] = None
      password: Optional[str] = None
      cmdOption: Optional[str] = None

   def Check(self, metaUrls: list[str], bundleUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Scan(self, repository: Locator, updateID: list[str]) -> Task: ...
   def ScanV2(self, metaUrls: list[str], bundleUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Stage(self, metaUrls: list[str], bundleUrls: list[str], vibUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Install(self, repository: Locator, updateID: str, force: Optional[bool]) -> Task: ...
   def InstallV2(self, metaUrls: list[str], bundleUrls: list[str], vibUrls: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Uninstall(self, bulletinIds: list[str], spec: Optional[PatchManagerOperationSpec]) -> Task: ...
   def Query(self, spec: Optional[PatchManagerOperationSpec]) -> Task: ...


class PathSelectionPolicyOption(DynamicData):
   policy: ElementDescription


class PciDevice(DynamicData):
   class DirectPathInfo(DynamicData):
      interconnectType: Optional[str] = None
      driverName: Optional[str] = None
      driverVersion: Optional[str] = None
      availableMemory: Optional[int] = None

   id: str
   classId: short
   bus: byte
   slot: byte
   physicalSlot: Optional[int] = None
   slotDescription: Optional[str] = None
   function: byte
   vendorId: short
   subVendorId: short
   vendorName: str
   deviceId: short
   subDeviceId: short
   parentBridge: Optional[str] = None
   deviceName: str
   deviceClassName: Optional[str] = None
   directPathInfo: Optional[DirectPathInfo] = None


class PciPassthruConfig(DynamicData):
   id: str
   passthruEnabled: bool
   applyNow: Optional[bool] = None
   hardwareLabel: Optional[str] = None


class PciPassthruInfo(DynamicData):
   class DirectPathDeviceMode(Enum):
      none: ClassVar['DirectPathDeviceMode'] = 'none'
      host: ClassVar['DirectPathDeviceMode'] = 'host'
      directPath: ClassVar['DirectPathDeviceMode'] = 'directPath'
      enhancedDirectPath: ClassVar['DirectPathDeviceMode'] = 'enhancedDirectPath'
      vGpuSameSize: ClassVar['DirectPathDeviceMode'] = 'vGpuSameSize'
      vGpuMixedSize: ClassVar['DirectPathDeviceMode'] = 'vGpuMixedSize'
      systemSelect: ClassVar['DirectPathDeviceMode'] = 'systemSelect'

   class DirectPathState(DynamicData):
      mode: str
      configurableModes: list[str] = []
      usedMemory: Optional[int] = None

   id: str
   dependentDevice: str
   passthruEnabled: bool
   passthruCapable: bool
   passthruActive: bool
   hardwareLabel: Optional[str] = None
   directPathState: Optional[DirectPathState] = None


class PciPassthruSystem(ExtensibleManagedObject):
   @property
   def pciPassthruInfo(self) -> list[PciPassthruInfo]: ...
   @property
   def sriovDevicePoolInfo(self) -> list[SriovDevicePoolInfo]: ...

   def Refresh(self) -> None: ...
   def UpdatePassthruConfig(self, config: list[PciPassthruConfig]) -> None: ...

class PcieHba(HostBusAdapter):
   pass

class PcieTargetTransport(TargetTransport):
   pass


class PersistentMemoryInfo(DynamicData):
   capacityInMB: Optional[long] = None
   volumeUUID: Optional[str] = None


class PhysicalNic(DynamicData):
   class Specification(DynamicData):
      ip: Optional[IpConfig] = None
      linkSpeed: Optional[LinkSpeedDuplex] = None
      enableEnhancedNetworkingStack: Optional[bool] = None
      ensInterruptEnabled: Optional[bool] = None

   class Config(DynamicData):
      device: str
      spec: Specification

   class LinkSpeedDuplex(DynamicData):
      speedMb: int
      duplex: bool

   class NetworkHint(DynamicData):
      class HintElement(DynamicData):
         vlanId: Optional[int] = None

      class IpNetwork(NetworkHint.HintElement):
         ipSubnet: str

      class NamedNetwork(NetworkHint.HintElement):
         network: str

      device: str
      subnet: list[IpNetwork] = []
      network: list[NamedNetwork] = []
      connectedSwitchPort: Optional[CdpInfo] = None
      lldpInfo: Optional[LldpInfo] = None

   class CdpDeviceCapability(DynamicData):
      router: bool
      transparentBridge: bool
      sourceRouteBridge: bool
      networkSwitch: bool
      host: bool
      igmpEnabled: bool
      repeater: bool

   class CdpInfo(DynamicData):
      cdpVersion: Optional[int] = None
      timeout: Optional[int] = None
      ttl: Optional[int] = None
      samples: Optional[int] = None
      devId: Optional[str] = None
      address: Optional[str] = None
      portId: Optional[str] = None
      deviceCapability: Optional[CdpDeviceCapability] = None
      softwareVersion: Optional[str] = None
      hardwarePlatform: Optional[str] = None
      ipPrefix: Optional[str] = None
      ipPrefixLen: Optional[int] = None
      vlan: Optional[int] = None
      fullDuplex: Optional[bool] = None
      mtu: Optional[int] = None
      systemName: Optional[str] = None
      systemOID: Optional[str] = None
      mgmtAddr: Optional[str] = None
      location: Optional[str] = None

   class LldpInfo(DynamicData):
      chassisId: str
      portId: str
      timeToLive: int
      parameter: list[KeyAnyValue] = []

   class VmDirectPathGen2SupportedMode(Enum):
      upt: ClassVar['VmDirectPathGen2SupportedMode'] = 'upt'

   class ResourcePoolSchedulerDisallowedReason(Enum):
      userOptOut: ClassVar['ResourcePoolSchedulerDisallowedReason'] = 'userOptOut'
      hardwareUnsupported: ClassVar['ResourcePoolSchedulerDisallowedReason'] = 'hardwareUnsupported'

   key: Optional[str] = None
   device: str
   pci: str
   driver: Optional[str] = None
   driverVersion: Optional[str] = None
   firmwareVersion: Optional[str] = None
   linkSpeed: Optional[LinkSpeedDuplex] = None
   validLinkSpecification: list[LinkSpeedDuplex] = []
   spec: Specification
   wakeOnLanSupported: bool
   mac: str
   fcoeConfiguration: Optional[FcoeConfig] = None
   vmDirectPathGen2Supported: Optional[bool] = None
   vmDirectPathGen2SupportedMode: Optional[str] = None
   resourcePoolSchedulerAllowed: Optional[bool] = None
   resourcePoolSchedulerDisallowedReason: list[str] = []
   autoNegotiateSupported: Optional[bool] = None
   enhancedNetworkingStackSupported: Optional[bool] = None
   ensInterruptSupported: Optional[bool] = None
   rdmaDevice: Optional[RdmaDevice] = None
   dpuId: Optional[str] = None
   perfNicOffloadSupported: Optional[bool] = None


class PlugStoreTopology(DynamicData):
   class Adapter(DynamicData):
      key: str
      adapter: HostBusAdapter
      path: list[Path] = []

   class Path(DynamicData):
      key: str
      name: str
      channelNumber: Optional[int] = None
      targetNumber: Optional[int] = None
      lunNumber: Optional[int] = None
      adapter: Optional[Adapter] = None
      target: Optional[Target] = None
      device: Optional[Device] = None

   class Device(DynamicData):
      key: str
      lun: ScsiLun
      path: list[Path] = []

   class Plugin(DynamicData):
      key: str
      name: str
      device: list[Device] = []
      claimedPath: list[Path] = []

   class Target(DynamicData):
      key: str
      transport: Optional[TargetTransport] = None

   adapter: list[Adapter] = []
   path: list[Path] = []
   target: list[Target] = []
   device: list[Device] = []
   plugin: list[Plugin] = []


class PnicTSOInfo(DynamicData):
   nicName: str
   isSupported: bool
   isEnabled: bool


class PodVMInfo(DynamicData):
   hasPageSharingPodVM: bool
   podVMOverheadInfo: PodVMOverheadInfo


class PodVMOverheadInfo(DynamicData):
   crxPageSharingSupported: bool
   podVMOverheadWithoutPageSharing: int
   podVMOverheadWithPageSharing: int


class PortGroup(DynamicData):
   class PortConnecteeType(Enum):
      virtualMachine: ClassVar['PortConnecteeType'] = 'virtualMachine'
      systemManagement: ClassVar['PortConnecteeType'] = 'systemManagement'
      host: ClassVar['PortConnecteeType'] = 'host'
      unknown: ClassVar['PortConnecteeType'] = 'unknown'

   class Specification(DynamicData):
      name: str
      vlanId: int
      vswitchName: str
      policy: NetworkPolicy

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      spec: Optional[Specification] = None

   class Port(DynamicData):
      key: Optional[str] = None
      mac: list[str] = []
      type: str

   key: Optional[str] = None
   port: list[Port] = []
   vswitch: Optional[VirtualSwitch] = None
   computedPolicy: NetworkPolicy
   spec: Specification


class PowerSystem(ManagedObject):
   class PowerPolicy(DynamicData):
      key: int
      name: str
      shortName: str
      description: str

   class Capability(DynamicData):
      availablePolicy: list[PowerPolicy] = []

   class Info(DynamicData):
      currentPolicy: PowerPolicy

   @property
   def capability(self) -> Capability: ...
   @property
   def info(self) -> Info: ...

   def ConfigurePolicy(self, key: int) -> None: ...


class ProtocolEndpoint(DynamicData):
   class PEType(Enum):
      block: ClassVar['PEType'] = 'block'
      nas: ClassVar['PEType'] = 'nas'

   class ProtocolEndpointType(Enum):
      scsi: ClassVar['ProtocolEndpointType'] = 'scsi'
      nfs: ClassVar['ProtocolEndpointType'] = 'nfs'
      nfs4x: ClassVar['ProtocolEndpointType'] = 'nfs4x'

   peType: str
   type: Optional[str] = None
   uuid: str
   hostKey: list[HostSystem] = []
   storageArray: Optional[str] = None
   nfsServer: Optional[str] = None
   nfsDir: Optional[str] = None
   nfsServerScope: Optional[str] = None
   nfsServerMajor: Optional[str] = None
   nfsServerAuthType: Optional[str] = None
   nfsServerUser: Optional[str] = None
   deviceId: Optional[str] = None
   usedByStretchedContainer: Optional[bool] = None


class PtpConfig(DynamicData):
   class DeviceType(Enum):
      none: ClassVar['DeviceType'] = 'none'
      virtualNic: ClassVar['DeviceType'] = 'virtualNic'
      pciPassthruNic: ClassVar['DeviceType'] = 'pciPassthruNic'

   class PtpPort(DynamicData):
      index: int
      deviceType: Optional[str] = None
      device: Optional[str] = None
      ipConfig: Optional[IpConfig] = None

   domain: Optional[int] = None
   port: list[PtpPort] = []


class QualifiedName(DynamicData):
   class Type(Enum):
      nvmeQualifiedName: ClassVar['Type'] = 'nvmeQualifiedName'
      vvolNvmeQualifiedName: ClassVar['Type'] = 'vvolNvmeQualifiedName'

   value: str
   type: str


class RdmaDevice(DynamicData):
   class Backing(DynamicData):
      pass

   class PnicBacking(Backing):
      pairedUplink: PhysicalNic

   class ConnectionState(Enum):
      unknown: ClassVar['ConnectionState'] = 'unknown'
      down: ClassVar['ConnectionState'] = 'down'
      init: ClassVar['ConnectionState'] = 'init'
      armed: ClassVar['ConnectionState'] = 'armed'
      active: ClassVar['ConnectionState'] = 'active'
      activeDefer: ClassVar['ConnectionState'] = 'activeDefer'

   class ConnectionInfo(DynamicData):
      state: str
      mtu: int
      speedInMbps: int

   class Capability(DynamicData):
      roceV1Capable: bool
      roceV2Capable: bool
      iWarpCapable: bool

   key: str
   device: str
   driver: Optional[str] = None
   description: Optional[str] = None
   backing: Optional[Backing] = None
   connectionInfo: ConnectionInfo
   capability: Capability


class RdmaHba(HostBusAdapter):
   associatedRdmaDevice: Optional[str] = None

class RdmaProtocol:
   pass

class RdmaTargetTransport(TargetTransport):
   pass


class ReliableMemoryInfo(DynamicData):
   memorySize: long


class ResignatureRescanResult(DynamicData):
   rescan: list[VmfsRescanResult] = []
   result: Datastore


class Ruleset(DynamicData):
   class IpNetwork(DynamicData):
      network: str
      prefixLength: int

   class IpList(DynamicData):
      ipAddress: list[str] = []
      ipNetwork: list[IpNetwork] = []
      allIp: bool

   class RulesetSpec(DynamicData):
      allowedHosts: IpList

   class Rule(DynamicData):
      class Direction(Enum):
         inbound: ClassVar['Direction'] = 'inbound'
         outbound: ClassVar['Direction'] = 'outbound'

      class PortType(Enum):
         src: ClassVar['PortType'] = 'src'
         dst: ClassVar['PortType'] = 'dst'

      class Protocol(Enum):
         tcp: ClassVar['Protocol'] = 'tcp'
         udp: ClassVar['Protocol'] = 'udp'

      port: int
      endPort: Optional[int] = None
      direction: Direction
      portType: Optional[PortType] = None
      protocol: str

   key: str
   label: str
   required: bool
   rule: list[Rule] = []
   service: Optional[str] = None
   enabled: bool
   allowedHosts: Optional[IpList] = None
   userControllable: Optional[bool] = None
   ipListUserConfigurable: Optional[bool] = None


class RuntimeInfo(DynamicData):
   class NetStackInstanceRuntimeInfo(DynamicData):
      class State(Enum):
         inactive: ClassVar['State'] = 'inactive'
         active: ClassVar['State'] = 'active'
         deactivating: ClassVar['State'] = 'deactivating'
         activating: ClassVar['State'] = 'activating'

      netStackInstanceKey: str
      state: Optional[str] = None
      vmknicKeys: list[str] = []
      maxNumberOfConnections: Optional[int] = None
      currentIpV6Enabled: Optional[bool] = None

   class PlacedVirtualNicIdentifier(DynamicData):
      vm: VirtualMachine
      vnicKey: str
      reservation: Optional[int] = None

   class PnicNetworkResourceInfo(DynamicData):
      pnicDevice: str
      availableBandwidthForVMTraffic: Optional[long] = None
      unusedBandwidthForVMTraffic: Optional[long] = None
      placedVirtualNics: list[PlacedVirtualNicIdentifier] = []

   class NetworkResourceRuntimeInfo(DynamicData):
      pnicResourceInfo: list[PnicNetworkResourceInfo] = []

   class NetworkRuntimeInfo(DynamicData):
      netStackInstanceRuntimeInfo: list[NetStackInstanceRuntimeInfo] = []
      networkResourceRuntime: Optional[NetworkResourceRuntimeInfo] = None

   class StatelessNvdsMigrationState(Enum):
      ready: ClassVar['StatelessNvdsMigrationState'] = 'ready'
      notNeeded: ClassVar['StatelessNvdsMigrationState'] = 'notNeeded'
      unknown: ClassVar['StatelessNvdsMigrationState'] = 'unknown'

   class StateEncryptionInfo(DynamicData):
      class ProtectionMode(Enum):
         none: ClassVar['ProtectionMode'] = 'none'
         tpm: ClassVar['ProtectionMode'] = 'tpm'

      protectionMode: str
      requireSecureBoot: Optional[bool] = None
      requireExecInstalledOnly: Optional[bool] = None

   connectionState: HostSystem.ConnectionState
   powerState: HostSystem.PowerState
   standbyMode: Optional[str] = None
   inMaintenanceMode: bool
   inQuarantineMode: Optional[bool] = None
   bootTime: Optional[datetime] = None
   healthSystemRuntime: Optional[HealthStatusSystem.Runtime] = None
   dasHostState: Optional[DasFdmHostState] = None
   tpmPcrValues: list[TpmDigestInfo] = []
   vsanRuntimeInfo: Optional[VsanRuntimeInfo] = None
   networkRuntimeInfo: Optional[NetworkRuntimeInfo] = None
   vFlashResourceRuntimeInfo: Optional[VFlashManager.VFlashResourceRunTimeInfo] = None
   hostMaxVirtualDiskCapacity: Optional[long] = None
   cryptoState: Optional[str] = None
   cryptoKeyId: Optional[CryptoKeyId] = None
   statelessNvdsMigrationReady: Optional[str] = None
   partialMaintenanceMode: list[PartialMaintenanceModeRuntimeInfo] = []
   stateEncryption: Optional[StateEncryptionInfo] = None
   podVMInfo: Optional[PodVMInfo] = None


class ScsiDisk(ScsiLun):
   class Partition(DynamicData):
      diskName: str
      partition: int

   class ScsiDiskType(Enum):
      native512: ClassVar['ScsiDiskType'] = 'native512'
      emulated512: ClassVar['ScsiDiskType'] = 'emulated512'
      native4k: ClassVar['ScsiDiskType'] = 'native4k'
      SoftwareEmulated4k: ClassVar['ScsiDiskType'] = 'SoftwareEmulated4k'
      unknown: ClassVar['ScsiDiskType'] = 'unknown'

   capacity: DiskDimensions.Lba
   devicePath: str
   ssd: Optional[bool] = None
   localDisk: Optional[bool] = None
   physicalLocation: list[str] = []
   emulatedDIXDIFEnabled: Optional[bool] = None
   vsanDiskInfo: Optional[VsanDiskInfo] = None
   scsiDiskType: Optional[str] = None
   usedByMemoryTiering: Optional[bool] = None


class ScsiLun(Device):
   class ScsiLunType(Enum):
      disk: ClassVar['ScsiLunType'] = 'disk'
      tape: ClassVar['ScsiLunType'] = 'tape'
      printer: ClassVar['ScsiLunType'] = 'printer'
      processor: ClassVar['ScsiLunType'] = 'processor'
      worm: ClassVar['ScsiLunType'] = 'worm'
      cdrom: ClassVar['ScsiLunType'] = 'cdrom'
      scanner: ClassVar['ScsiLunType'] = 'scanner'
      opticalDevice: ClassVar['ScsiLunType'] = 'opticalDevice'
      mediaChanger: ClassVar['ScsiLunType'] = 'mediaChanger'
      communications: ClassVar['ScsiLunType'] = 'communications'
      storageArrayController: ClassVar['ScsiLunType'] = 'storageArrayController'
      enclosure: ClassVar['ScsiLunType'] = 'enclosure'
      unknown: ClassVar['ScsiLunType'] = 'unknown'

   class DeviceProtocol(Enum):
      NVMe: ClassVar['DeviceProtocol'] = 'NVMe'
      SCSI: ClassVar['DeviceProtocol'] = 'SCSI'

   class Capabilities(DynamicData):
      updateDisplayNameSupported: bool

   class DurableName(DynamicData):
      namespace: str
      namespaceId: byte
      data: list[byte] = []

   class State(Enum):
      unknownState: ClassVar['State'] = 'unknownState'
      ok: ClassVar['State'] = 'ok'
      error: ClassVar['State'] = 'error'
      off: ClassVar['State'] = 'off'
      quiesced: ClassVar['State'] = 'quiesced'
      degraded: ClassVar['State'] = 'degraded'
      lostCommunication: ClassVar['State'] = 'lostCommunication'
      timeout: ClassVar['State'] = 'timeout'

   class DescriptorQuality(Enum):
      highQuality: ClassVar['DescriptorQuality'] = 'highQuality'
      mediumQuality: ClassVar['DescriptorQuality'] = 'mediumQuality'
      lowQuality: ClassVar['DescriptorQuality'] = 'lowQuality'
      unknownQuality: ClassVar['DescriptorQuality'] = 'unknownQuality'

   class Descriptor(DynamicData):
      quality: str
      id: str

   class VStorageSupportStatus(Enum):
      vStorageSupported: ClassVar['VStorageSupportStatus'] = 'vStorageSupported'
      vStorageUnsupported: ClassVar['VStorageSupportStatus'] = 'vStorageUnsupported'
      vStorageUnknown: ClassVar['VStorageSupportStatus'] = 'vStorageUnknown'

   class LunReservationStatus(Enum):
      LUN_RESERVED_UNKNOWN: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_UNKNOWN'
      LUN_RESERVED_YES: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_YES'
      LUN_RESERVED_NO: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_NO'
      LUN_RESERVED_NOT_SUPPORTED: ClassVar['LunReservationStatus'] = 'LUN_RESERVED_NOT_SUPPORTED'

   key: Optional[str] = None
   uuid: str
   descriptor: list[Descriptor] = []
   canonicalName: Optional[str] = None
   displayName: Optional[str] = None
   lunType: str
   vendor: Optional[str] = None
   model: Optional[str] = None
   revision: Optional[str] = None
   scsiLevel: Optional[int] = None
   serialNumber: Optional[str] = None
   durableName: Optional[DurableName] = None
   alternateName: list[DurableName] = []
   standardInquiry: list[byte] = []
   queueDepth: Optional[int] = None
   operationalState: list[str] = []
   capabilities: Optional[Capabilities] = None
   vStorageSupport: Optional[str] = None
   protocolEndpoint: Optional[bool] = None
   perenniallyReserved: Optional[bool] = None
   clusteredVmdkSupported: Optional[bool] = None
   applicationProtocol: Optional[str] = None
   dispersedNs: Optional[bool] = None
   deviceReservation: Optional[str] = None


class ScsiTopology(DynamicData):
   class Interface(DynamicData):
      key: str
      adapter: HostBusAdapter
      target: list[Target] = []

   class Target(DynamicData):
      key: str
      target: int
      lun: list[Lun] = []
      transport: Optional[TargetTransport] = None

   class Lun(DynamicData):
      key: str
      lun: int
      scsiLun: ScsiLun

   adapter: list[Interface] = []


class SecuritySpec(DynamicData):
   adminPassword: Optional[str] = None
   removePermission: list[AuthorizationManager.Permission] = []
   addPermission: list[AuthorizationManager.Permission] = []

class SerialAttachedHba(HostBusAdapter):
   nodeWorldWideName: str

class SerialAttachedTargetTransport(TargetTransport):
   pass


class Service(DynamicData):
   class Policy(Enum):
      on: ClassVar['Policy'] = 'on'
      automatic: ClassVar['Policy'] = 'automatic'
      off: ClassVar['Policy'] = 'off'

   class SourcePackage(DynamicData):
      sourcePackageName: str
      description: str

   key: str
   label: str
   required: bool
   uninstallable: bool
   running: bool
   ruleset: list[str] = []
   policy: str
   sourcePackage: Optional[SourcePackage] = None


class ServiceConfig(DynamicData):
   serviceId: str
   startupPolicy: str


class ServiceInfo(DynamicData):
   service: list[Service] = []


class ServiceSystem(ExtensibleManagedObject):
   @property
   def serviceInfo(self) -> ServiceInfo: ...

   def UpdatePolicy(self, id: str, policy: str) -> None: ...
   def Start(self, id: str) -> None: ...
   def Stop(self, id: str) -> None: ...
   def Restart(self, id: str) -> None: ...
   def Uninstall(self, id: str) -> None: ...
   def Refresh(self) -> None: ...


class SevInfo(DynamicData):
   class SevState(Enum):
      uninitialized: ClassVar['SevState'] = 'uninitialized'
      initialized: ClassVar['SevState'] = 'initialized'
      working: ClassVar['SevState'] = 'working'
      disabledBios: ClassVar['SevState'] = 'disabledBios'

   sevState: str
   maxSevEsGuests: long
   snpState: Optional[str] = None
   snpSupported: Optional[bool] = None


class SgxInfo(DynamicData):
   class SgxStates(Enum):
      notPresent: ClassVar['SgxStates'] = 'notPresent'
      disabledBIOS: ClassVar['SgxStates'] = 'disabledBIOS'
      disabledCFW101: ClassVar['SgxStates'] = 'disabledCFW101'
      disabledCPUMismatch: ClassVar['SgxStates'] = 'disabledCPUMismatch'
      disabledNoFLC: ClassVar['SgxStates'] = 'disabledNoFLC'
      disabledNUMAUnsup: ClassVar['SgxStates'] = 'disabledNUMAUnsup'
      disabledMaxEPCRegs: ClassVar['SgxStates'] = 'disabledMaxEPCRegs'
      enabled: ClassVar['SgxStates'] = 'enabled'

   class FlcModes(Enum):
      off: ClassVar['FlcModes'] = 'off'
      locked: ClassVar['FlcModes'] = 'locked'
      unlocked: ClassVar['FlcModes'] = 'unlocked'

   sgxState: str
   totalEpcMemory: long
   flcMode: str
   lePubKeyHash: Optional[str] = None
   registrationInfo: Optional[SgxRegistrationInfo] = None


class SgxRegistrationInfo(DynamicData):
   class RegistrationStatus(Enum):
      notApplicable: ClassVar['RegistrationStatus'] = 'notApplicable'
      incomplete: ClassVar['RegistrationStatus'] = 'incomplete'
      complete: ClassVar['RegistrationStatus'] = 'complete'

   class RegistrationType(Enum):
      manifest: ClassVar['RegistrationType'] = 'manifest'
      addPackage: ClassVar['RegistrationType'] = 'addPackage'

   status: Optional[str] = None
   biosError: Optional[int] = None
   registrationUrl: Optional[str] = None
   type: Optional[str] = None
   ppid: Optional[str] = None
   lastRegisteredTime: Optional[datetime] = None


class SharedGpuCapabilities(DynamicData):
   vgpu: str
   diskSnapshotSupported: bool
   memorySnapshotSupported: bool
   suspendSupported: bool
   migrateSupported: bool


class SnmpSystem(ManagedObject):
   class SnmpConfigSpec(DynamicData):
      class Destination(DynamicData):
         hostName: str
         port: int
         community: str

      enabled: Optional[bool] = None
      port: Optional[int] = None
      readOnlyCommunities: list[str] = []
      trapTargets: list[Destination] = []
      option: list[KeyValue] = []

   class AgentLimits(DynamicData):
      class Capability(Enum):
         COMPLETE: ClassVar['Capability'] = 'COMPLETE'
         DIAGNOSTICS: ClassVar['Capability'] = 'DIAGNOSTICS'
         CONFIGURATION: ClassVar['Capability'] = 'CONFIGURATION'

      maxReadOnlyCommunities: int
      maxTrapDestinations: int
      maxCommunityLength: int
      maxBufferSize: int
      capability: Capability

   @property
   def configuration(self) -> SnmpConfigSpec: ...
   @property
   def limits(self) -> AgentLimits: ...

   def ReconfigureSnmpAgent(self, spec: SnmpConfigSpec) -> None: ...
   def SendTestNotification(self) -> None: ...


class SoftwarePackage(DynamicData):
   class VibType(Enum):
      bootbank: ClassVar['VibType'] = 'bootbank'
      tools: ClassVar['VibType'] = 'tools'
      meta: ClassVar['VibType'] = 'meta'

   class Capability(DynamicData):
      liveInstallAllowed: Optional[bool] = None
      liveRemoveAllowed: Optional[bool] = None
      statelessReady: Optional[bool] = None
      overlay: Optional[bool] = None

   class Constraint(Enum):
      equals: ClassVar['Constraint'] = 'equals'
      lessThan: ClassVar['Constraint'] = 'lessThan'
      lessThanEqual: ClassVar['Constraint'] = 'lessThanEqual'
      greaterThanEqual: ClassVar['Constraint'] = 'greaterThanEqual'
      greaterThan: ClassVar['Constraint'] = 'greaterThan'

   class Relation(DynamicData):
      constraint: Optional[str] = None
      name: str
      version: Optional[str] = None

   name: str
   version: str
   type: str
   vendor: str
   acceptanceLevel: str
   summary: str
   description: str
   referenceURL: list[str] = []
   creationDate: Optional[datetime] = None
   depends: list[Relation] = []
   conflicts: list[Relation] = []
   replaces: list[Relation] = []
   provides: list[str] = []
   maintenanceModeRequired: Optional[bool] = None
   hardwarePlatformsRequired: list[str] = []
   capability: Capability
   tag: list[str] = []
   payload: list[str] = []

class SriovConfig(PciPassthruConfig):
   sriovEnabled: bool
   numVirtualFunction: int


class SriovDevicePoolInfo(DynamicData):
   key: str

class SriovInfo(PciPassthruInfo):
   sriovEnabled: bool
   sriovCapable: bool
   sriovActive: bool
   numVirtualFunctionRequested: int
   numVirtualFunction: int
   maxVirtualFunctionSupported: int


class SriovNetworkDevicePoolInfo(SriovDevicePoolInfo):
   switchKey: Optional[str] = None
   switchUuid: Optional[str] = None
   pnic: list[PhysicalNic] = []


class SslThumbprintInfo(DynamicData):
   principal: str
   ownerTag: str
   sslThumbprints: list[str] = []


class StorageArrayTypePolicyOption(DynamicData):
   policy: ElementDescription


class StorageDeviceInfo(DynamicData):
   hostBusAdapter: list[HostBusAdapter] = []
   scsiLun: list[ScsiLun] = []
   scsiTopology: Optional[ScsiTopology] = None
   nvmeTopology: Optional[NvmeTopology] = None
   multipathInfo: Optional[MultipathInfo] = None
   plugStoreTopology: Optional[PlugStoreTopology] = None
   softwareInternetScsiEnabled: bool

class StorageProtocol:
   pass


class StorageSystem(ExtensibleManagedObject):
   class VmfsVolumeResult(DynamicData):
      key: str
      fault: Optional[MethodFault] = None

   class ScsiLunResult(DynamicData):
      key: str
      fault: Optional[MethodFault] = None

   class DiskLocatorLedResult(DynamicData):
      key: str
      fault: MethodFault

   @property
   def storageDeviceInfo(self) -> Optional[StorageDeviceInfo]: ...
   @property
   def fileSystemVolumeInfo(self) -> FileSystemVolumeInfo: ...
   @property
   def systemFile(self) -> list[str]: ...
   @property
   def multipathStateInfo(self) -> Optional[MultipathStateInfo]: ...

   def RetrieveDiskPartitionInfo(self, devicePath: list[str]) -> list[DiskPartitionInfo]: ...
   def ComputeDiskPartitionInfo(self, devicePath: str, layout: DiskPartitionInfo.Layout, partitionFormat: Optional[str]) -> DiskPartitionInfo: ...
   def ComputeDiskPartitionInfoForResize(self, partition: ScsiDisk.Partition, blockRange: DiskPartitionInfo.BlockRange, partitionFormat: Optional[str]) -> DiskPartitionInfo: ...
   def UpdateDiskPartitions(self, devicePath: str, spec: DiskPartitionInfo.Specification) -> None: ...
   def FormatVmfs(self, createSpec: VmfsVolume.Specification) -> VmfsVolume: ...
   def MountVmfsVolume(self, vmfsUuid: str) -> None: ...
   def UnmountVmfsVolume(self, vmfsUuid: str) -> None: ...
   def UnmountVmfsVolumeEx(self, vmfsUuid: list[str]) -> Task: ...
   def MountVmfsVolumeEx(self, vmfsUuid: list[str]) -> Task: ...
   def UnmapVmfsVolumeEx(self, vmfsUuid: list[str]) -> Task: ...
   def DeleteVmfsVolumeState(self, vmfsUuid: str) -> None: ...
   def RescanVmfs(self) -> None: ...
   def AttachVmfsExtent(self, vmfsPath: str, extent: ScsiDisk.Partition) -> None: ...
   def ExpandVmfsExtent(self, vmfsPath: str, extent: ScsiDisk.Partition) -> None: ...
   def UpgradeVmfs(self, vmfsPath: str) -> None: ...
   def UpgradeVmLayout(self) -> None: ...
   def QueryUnresolvedVmfsVolume(self) -> list[UnresolvedVmfsVolume]: ...
   def ResolveMultipleUnresolvedVmfsVolumes(self, resolutionSpec: list[UnresolvedVmfsResolutionSpec]) -> list[UnresolvedVmfsResolutionResult]: ...
   def ResolveMultipleUnresolvedVmfsVolumesEx(self, resolutionSpec: list[UnresolvedVmfsResolutionSpec]) -> Task: ...
   def UnmountForceMountedVmfsVolume(self, vmfsUuid: str) -> None: ...
   def RescanHba(self, hbaDevice: str) -> None: ...
   def RescanAllHba(self) -> None: ...
   def UpdateSoftwareInternetScsiEnabled(self, enabled: bool) -> None: ...
   def UpdateInternetScsiDiscoveryProperties(self, iScsiHbaDevice: str, discoveryProperties: InternetScsiHba.DiscoveryProperties) -> None: ...
   def UpdateInternetScsiAuthenticationProperties(self, iScsiHbaDevice: str, authenticationProperties: InternetScsiHba.AuthenticationProperties, targetSet: Optional[InternetScsiHba.TargetSet]) -> None: ...
   def UpdateInternetScsiDigestProperties(self, iScsiHbaDevice: str, targetSet: Optional[InternetScsiHba.TargetSet], digestProperties: InternetScsiHba.DigestProperties) -> None: ...
   def UpdateInternetScsiAdvancedOptions(self, iScsiHbaDevice: str, targetSet: Optional[InternetScsiHba.TargetSet], options: list[InternetScsiHba.ParamValue]) -> None: ...
   def UpdateInternetScsiIPProperties(self, iScsiHbaDevice: str, ipProperties: InternetScsiHba.IPProperties) -> None: ...
   def UpdateInternetScsiName(self, iScsiHbaDevice: str, iScsiName: str) -> None: ...
   def UpdateInternetScsiAlias(self, iScsiHbaDevice: str, iScsiAlias: str) -> None: ...
   def AddInternetScsiSendTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.SendTarget]) -> None: ...
   def RemoveInternetScsiSendTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.SendTarget], force: Optional[bool]) -> None: ...
   def AddInternetScsiStaticTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.StaticTarget]) -> None: ...
   def RemoveInternetScsiStaticTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.StaticTarget]) -> None: ...
   def EnableMultipathPath(self, pathName: str) -> None: ...
   def DisableMultipathPath(self, pathName: str) -> None: ...
   def SetMultipathLunPolicy(self, lunId: str, policy: MultipathInfo.LogicalUnitPolicy) -> None: ...
   def UpdateHppMultipathLunPolicy(self, lunId: str, policy: MultipathInfo.HppLogicalUnitPolicy) -> None: ...
   def QueryPathSelectionPolicyOptions(self) -> list[PathSelectionPolicyOption]: ...
   def QueryStorageArrayTypePolicyOptions(self) -> list[StorageArrayTypePolicyOption]: ...
   def UpdateScsiLunDisplayName(self, lunUuid: str, displayName: str) -> None: ...
   def DetachScsiLun(self, lunUuid: str) -> None: ...
   def DetachScsiLunEx(self, lunUuid: list[str]) -> Task: ...
   def DeleteScsiLunState(self, lunCanonicalName: str) -> None: ...
   def AttachScsiLun(self, lunUuid: str) -> None: ...
   def AttachScsiLunEx(self, lunUuid: list[str]) -> Task: ...
   def Refresh(self) -> None: ...
   def DiscoverFcoeHbas(self, fcoeSpec: FcoeConfig.FcoeSpecification) -> None: ...
   def MarkForRemoval(self, hbaName: str, remove: bool) -> None: ...
   def FormatVffs(self, createSpec: VffsVolume.Specification) -> VffsVolume: ...
   def ExtendVffs(self, vffsPath: str, devicePath: str, spec: Optional[DiskPartitionInfo.Specification]) -> None: ...
   def DestroyVffs(self, vffsPath: str) -> None: ...
   def MountVffsVolume(self, vffsUuid: str) -> None: ...
   def UnmountVffsVolume(self, vffsUuid: str) -> None: ...
   def DeleteVffsVolumeState(self, vffsUuid: str) -> None: ...
   def RescanVffs(self) -> None: ...
   def QueryAvailableSsds(self, vffsPath: Optional[str]) -> list[ScsiDisk]: ...
   def SetNFSUser(self, user: str, password: str) -> None: ...
   def ChangeNFSUserPassword(self, password: str) -> None: ...
   def QueryNFSUser(self) -> Optional[NasVolume.UserInfo]: ...
   def ClearNFSUser(self) -> None: ...
   def TurnDiskLocatorLedOn(self, scsiDiskUuids: list[str]) -> Task: ...
   def TurnDiskLocatorLedOff(self, scsiDiskUuids: list[str]) -> Task: ...
   def MarkAsSsd(self, scsiDiskUuid: str) -> Task: ...
   def MarkAsNonSsd(self, scsiDiskUuid: str) -> Task: ...
   def MarkAsLocal(self, scsiDiskUuid: str) -> Task: ...
   def MarkAsNonLocal(self, scsiDiskUuid: str) -> Task: ...
   def UpdateVmfsUnmapPriority(self, vmfsUuid: str, unmapPriority: str) -> None: ...
   def UpdateVmfsUnmapBandwidth(self, vmfsUuid: str, unmapBandwidthSpec: VmfsVolume.UnmapBandwidthSpec) -> None: ...
   def QueryVmfsConfigOption(self) -> list[VmfsVolume.ConfigOption]: ...
   def MarkPerenniallyReserved(self, lunUuid: str, state: bool) -> None: ...
   def MarkPerenniallyReservedEx(self, lunUuid: list[str], state: bool) -> Task: ...
   def CreateNvmeOverRdmaAdapter(self, rdmaDeviceName: str) -> None: ...
   def RemoveNvmeOverRdmaAdapter(self, hbaDeviceName: str) -> None: ...
   def CreateSoftwareAdapter(self, spec: HbaCreateSpec) -> None: ...
   def RemoveSoftwareAdapter(self, hbaDeviceName: str) -> None: ...
   def DiscoverNvmeControllers(self, discoverSpec: NvmeDiscoverSpec) -> NvmeDiscoveryLog: ...
   def ConnectNvmeController(self, connectSpec: NvmeConnectSpec) -> None: ...
   def DisconnectNvmeController(self, disconnectSpec: NvmeDisconnectSpec) -> None: ...
   def ConnectNvmeControllerEx(self, connectSpec: list[NvmeConnectSpec]) -> Task: ...
   def DisconnectNvmeControllerEx(self, disconnectSpec: list[NvmeDisconnectSpec]) -> Task: ...


class Summary(DynamicData):
   class HardwareSummary(DynamicData):
      vendor: str
      model: str
      family: Optional[str] = None
      uuid: str
      otherIdentifyingInfo: list[SystemIdentificationInfo] = []
      memorySize: long
      cpuModel: str
      cpuMhz: int
      numCpuPkgs: short
      numCpuCores: short
      numCpuThreads: short
      numNics: int
      numHBAs: int

   class QuickStats(DynamicData):
      overallCpuUsage: Optional[int] = None
      overallMemoryUsage: Optional[int] = None
      distributedCpuFairness: Optional[int] = None
      distributedMemoryFairness: Optional[int] = None
      availablePMemCapacity: Optional[int] = None
      uptime: Optional[int] = None

   class ConfigSummary(DynamicData):
      name: str
      port: int
      sslThumbprint: Optional[str] = None
      sslCertificate: Optional[str] = None
      product: Optional[AboutInfo] = None
      vmotionEnabled: bool
      faultToleranceEnabled: bool
      featureVersion: list[FeatureVersionInfo] = []
      agentVmDatastore: Optional[Datastore] = None
      agentVmNetwork: Optional[Network] = None

   class GatewaySummary(DynamicData):
      gatewayType: str
      gatewayId: str

   host: Optional[HostSystem] = None
   hardware: Optional[HardwareSummary] = None
   runtime: Optional[RuntimeInfo] = None
   config: ConfigSummary
   quickStats: QuickStats
   overallStatus: ManagedEntity.Status
   rebootRequired: bool
   rebootRequiredReason: list[LocalizableMessage] = []
   maintenanceModeRequired: Optional[bool] = None
   customValue: list[CustomFieldsManager.Value] = []
   managementServerIp: Optional[str] = None
   maxEVCModeKey: Optional[str] = None
   currentEVCModeKey: Optional[str] = None
   currentEVCGraphicsModeKey: Optional[str] = None
   gateway: Optional[GatewaySummary] = None
   tpmAttestation: Optional[TpmAttestationInfo] = None
   trustAuthorityAttestationInfos: list[TrustAuthorityAttestationInfo] = []


class SystemEventInfo(DynamicData):
   recordId: long
   when: str
   selType: long
   message: str
   sensorNumber: long


class SystemHealthInfo(DynamicData):
   numericSensorInfo: list[NumericSensorInfo] = []


class SystemIdentificationInfo(DynamicData):
   class Identifier(Enum):
      AssetTag: ClassVar['Identifier'] = 'AssetTag'
      ServiceTag: ClassVar['Identifier'] = 'ServiceTag'
      OemSpecificString: ClassVar['Identifier'] = 'OemSpecificString'
      EnclosureSerialNumberTag: ClassVar['Identifier'] = 'EnclosureSerialNumberTag'
      SerialNumberTag: ClassVar['Identifier'] = 'SerialNumberTag'

   identifierValue: str
   identifierType: ElementDescription


class SystemInfo(DynamicData):
   vendor: str
   model: str
   family: Optional[str] = None
   uuid: str
   otherIdentifyingInfo: list[SystemIdentificationInfo] = []
   serialNumber: Optional[str] = None
   qualifiedName: list[QualifiedName] = []
   vvolHostNQN: Optional[QualifiedName] = None
   vvolHostId: Optional[str] = None
   bootCommandLine: Optional[str] = None


class SystemResourceInfo(DynamicData):
   key: str
   config: Optional[ResourceConfigSpec] = None
   child: list[SystemResourceInfo] = []


class SystemSwapConfiguration(DynamicData):
   class SystemSwapOption(DynamicData):
      key: int

   class DisabledOption(SystemSwapOption):
      pass

   class HostCacheOption(SystemSwapOption):
      pass

   class HostLocalSwapOption(SystemSwapOption):
      pass

   class DatastoreOption(SystemSwapOption):
      datastore: str

   option: list[SystemSwapOption] = []


class TargetTransport(DynamicData):
   pass


class TcpHba(HostBusAdapter):
   associatedPnic: Optional[str] = None

class TcpHbaCreateSpec(HbaCreateSpec):
   pnic: str

class TcpTargetTransport(TargetTransport):
   pass


class TdxInfo(DynamicData):
   class TdxState(Enum):
      initializing: ClassVar['TdxState'] = 'initializing'
      initialized: ClassVar['TdxState'] = 'initialized'
      configured: ClassVar['TdxState'] = 'configured'
      ready: ClassVar['TdxState'] = 'ready'
      disabledBios: ClassVar['TdxState'] = 'disabledBios'

   tdxState: str
   numTDXPrivateKeyIDs: int


class TpmAttestationInfo(DynamicData):
   class AcceptanceStatus(Enum):
      notAccepted: ClassVar['AcceptanceStatus'] = 'notAccepted'
      accepted: ClassVar['AcceptanceStatus'] = 'accepted'

   time: datetime
   status: AcceptanceStatus
   message: Optional[LocalizableMessage] = None


class TpmAttestationReport(DynamicData):
   tpmPcrValues: list[TpmDigestInfo] = []
   tpmEvents: list[TpmEventLogEntry] = []
   tpmLogReliable: bool

class TpmBootCompleteEventDetails(TpmEventDetails):
   pass

class TpmBootSecurityOptionEventDetails(TpmEventDetails):
   bootSecurityOption: str

class TpmCommandEventDetails(TpmEventDetails):
   commandLine: str

class TpmDigestInfo(DigestInfo):
   pcrNumber: int


class TpmEventDetails(DynamicData):
   dataHash: list[byte] = []
   dataHashMethod: Optional[str] = None


class TpmEventLogEntry(DynamicData):
   pcrIndex: int
   eventDetails: TpmEventDetails

class TpmNvTagEventDetails(TpmBootSecurityOptionEventDetails):
   pass


class TpmOptionEventDetails(TpmEventDetails):
   optionsFileName: str
   bootOptions: list[byte] = []

class TpmSignerEventDetails(TpmBootSecurityOptionEventDetails):
   pass

class TpmSoftwareComponentEventDetails(TpmEventDetails):
   componentName: str
   vibName: str
   vibVersion: str
   vibVendor: str

class TpmSystemVersionEventDetails(TpmEventDetails):
   systemVersion: str


class TpmVersionEventDetails(TpmEventDetails):
   version: binary


class TrustAuthorityAttestationInfo(DynamicData):
   class AttestationStatus(Enum):
      attested: ClassVar['AttestationStatus'] = 'attested'
      notAttested: ClassVar['AttestationStatus'] = 'notAttested'
      unknown: ClassVar['AttestationStatus'] = 'unknown'

   attestationStatus: str
   serviceId: Optional[str] = None
   attestedAt: Optional[datetime] = None
   attestedUntil: Optional[datetime] = None
   messages: list[LocalizableMessage] = []


class UnresolvedVmfsExtent(DynamicData):
   class UnresolvedReason(Enum):
      diskIdMismatch: ClassVar['UnresolvedReason'] = 'diskIdMismatch'
      uuidConflict: ClassVar['UnresolvedReason'] = 'uuidConflict'

   device: ScsiDisk.Partition
   devicePath: str
   vmfsUuid: str
   isHeadExtent: bool
   ordinal: int
   startBlock: int
   endBlock: int
   reason: str


class UnresolvedVmfsResignatureSpec(DynamicData):
   extentDevicePath: list[str] = []


class UnresolvedVmfsResolutionResult(DynamicData):
   spec: UnresolvedVmfsResolutionSpec
   vmfs: Optional[VmfsVolume] = None
   fault: Optional[MethodFault] = None


class UnresolvedVmfsResolutionSpec(DynamicData):
   class VmfsUuidResolution(Enum):
      resignature: ClassVar['VmfsUuidResolution'] = 'resignature'
      forceMount: ClassVar['VmfsUuidResolution'] = 'forceMount'

   extentDevicePath: list[str] = []
   uuidResolution: str


class UnresolvedVmfsVolume(DynamicData):
   class ResolveStatus(DynamicData):
      resolvable: bool
      incompleteExtents: Optional[bool] = None
      multipleCopies: Optional[bool] = None

   extent: list[UnresolvedVmfsExtent] = []
   vmfsLabel: str
   vmfsUuid: str
   totalBlocks: int
   resolveStatus: ResolveStatus


class VFlashManager(ManagedObject):
   class VFlashResourceConfigSpec(DynamicData):
      vffsUuid: str

   class VFlashResourceConfigInfo(DynamicData):
      vffs: Optional[VffsVolume] = None
      capacity: long

   class VFlashResourceRunTimeInfo(DynamicData):
      usage: long
      capacity: long
      accessible: bool
      capacityForVmCache: long
      freeForVmCache: long

   class VFlashCacheConfigSpec(DynamicData):
      defaultVFlashModule: str
      swapCacheReservationInGB: long

   class VFlashCacheConfigInfo(DynamicData):
      class VFlashModuleConfigOption(DynamicData):
         vFlashModule: str
         vFlashModuleVersion: str
         minSupportedModuleVersion: str
         cacheConsistencyType: ChoiceOption
         cacheMode: ChoiceOption
         blockSizeInKBOption: LongOption
         reservationInMBOption: LongOption
         maxDiskSizeInKB: long

      vFlashModuleConfigOption: list[VFlashModuleConfigOption] = []
      defaultVFlashModule: Optional[str] = None
      swapCacheReservationInGB: Optional[long] = None

   class VFlashConfigInfo(DynamicData):
      vFlashResourceConfigInfo: Optional[VFlashResourceConfigInfo] = None
      vFlashCacheConfigInfo: Optional[VFlashCacheConfigInfo] = None

   @property
   def vFlashConfigInfo(self) -> Optional[VFlashConfigInfo]: ...

   def ConfigureVFlashResourceEx(self, devicePath: list[str]) -> Task: ...
   def ConfigureVFlashResource(self, spec: VFlashResourceConfigSpec) -> None: ...
   def RemoveVFlashResource(self) -> None: ...
   def ConfigureHostVFlashCache(self, spec: VFlashCacheConfigSpec) -> None: ...
   def GetVFlashModuleDefaultConfig(self, vFlashModule: str) -> VirtualDisk.VFlashCacheConfigInfo: ...


class VFlashResourceConfigurationResult(DynamicData):
   devicePath: list[str] = []
   vffs: Optional[VffsVolume] = None
   diskConfigurationResult: list[DiskConfigurationResult] = []


class VMotionConfig(DynamicData):
   vmotionNicKey: Optional[str] = None
   enabled: bool


class VMotionInfo(DynamicData):
   netConfig: Optional[VMotionSystem.NetConfig] = None
   ipConfig: Optional[IpConfig] = None


class VMotionSystem(ExtensibleManagedObject):
   class NetConfig(DynamicData):
      candidateVnic: list[VirtualNic] = []
      selectedVnic: Optional[VirtualNic] = None

   @property
   def netConfig(self) -> Optional[NetConfig]: ...
   @property
   def ipConfig(self) -> Optional[IpConfig]: ...

   def UpdateIpConfig(self, ipConfig: IpConfig) -> None: ...
   def SelectVnic(self, device: str) -> None: ...
   def DeselectVnic(self) -> None: ...


class VSANStretchedClusterHostCapability(DynamicData):
   featureVersion: str

class VfatVolume(FileSystemVolume):
   pass


class VffsVolume(FileSystemVolume):
   class Specification(DynamicData):
      devicePath: str
      partition: Optional[DiskPartitionInfo.Specification] = None
      majorVersion: int
      volumeName: str

   majorVersion: int
   version: str
   uuid: str
   extent: list[ScsiDisk.Partition] = []


class VirtualNic(DynamicData):
   class Specification(DynamicData):
      ip: Optional[IpConfig] = None
      mac: Optional[str] = None
      distributedVirtualPort: Optional[PortConnection] = None
      portgroup: Optional[str] = None
      mtu: Optional[int] = None
      tsoEnabled: Optional[bool] = None
      netStackInstanceKey: Optional[str] = None
      opaqueNetwork: Optional[OpaqueNetworkSpec] = None
      externalId: Optional[str] = None
      pinnedPnic: Optional[str] = None
      ipRouteSpec: Optional[IpRouteSpec] = None
      systemOwned: Optional[bool] = None
      dpuId: Optional[str] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      device: Optional[str] = None
      portgroup: str
      spec: Optional[Specification] = None

   class OpaqueNetworkSpec(DynamicData):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class IpRouteSpec(DynamicData):
      ipRouteConfig: Optional[IpRouteConfig] = None

   device: str
   key: str
   portgroup: str
   spec: Specification
   port: Optional[PortGroup.Port] = None
   owner: Optional[str] = None


class VirtualNicConnection(DynamicData):
   portgroup: Optional[str] = None
   dvPort: Optional[PortConnection] = None
   opNetwork: Optional[VirtualNic.OpaqueNetworkSpec] = None


class VirtualNicManager(ExtensibleManagedObject):
   class NicType(Enum):
      vmotion: ClassVar['NicType'] = 'vmotion'
      faultToleranceLogging: ClassVar['NicType'] = 'faultToleranceLogging'
      vSphereReplication: ClassVar['NicType'] = 'vSphereReplication'
      vSphereReplicationNFC: ClassVar['NicType'] = 'vSphereReplicationNFC'
      management: ClassVar['NicType'] = 'management'
      vsan: ClassVar['NicType'] = 'vsan'
      vSphereProvisioning: ClassVar['NicType'] = 'vSphereProvisioning'
      vsanWitness: ClassVar['NicType'] = 'vsanWitness'
      vSphereBackupNFC: ClassVar['NicType'] = 'vSphereBackupNFC'
      ptp: ClassVar['NicType'] = 'ptp'
      vsanReplication: ClassVar['NicType'] = 'vsanReplication'
      nvmeTcp: ClassVar['NicType'] = 'nvmeTcp'
      nvmeRdma: ClassVar['NicType'] = 'nvmeRdma'
      vsanExternal: ClassVar['NicType'] = 'vsanExternal'
      vnetworking: ClassVar['NicType'] = 'vnetworking'

   class NicTypeSelection(DynamicData):
      vnic: VirtualNicConnection
      nicType: list[str] = []

   class NetConfig(DynamicData):
      nicType: str
      multiSelectAllowed: bool
      candidateVnic: list[VirtualNic] = []
      selectedVnic: list[VirtualNic] = []

   @property
   def info(self) -> VirtualNicManagerInfo: ...

   def QueryNetConfig(self, nicType: str) -> Optional[NetConfig]: ...
   def SelectVnic(self, nicType: str, device: str) -> None: ...
   def DeselectVnic(self, nicType: str, device: str) -> None: ...


class VirtualNicManagerInfo(DynamicData):
   netConfig: list[VirtualNicManager.NetConfig] = []


class VirtualSwitch(DynamicData):
   class Bridge(DynamicData):
      pass

   class AutoBridge(Bridge):
      excludedNicDevice: list[str] = []

   class SimpleBridge(Bridge):
      nicDevice: str

   class BondBridge(Bridge):
      nicDevice: list[str] = []
      beacon: Optional[BeaconConfig] = None
      linkDiscoveryProtocolConfig: Optional[LinkDiscoveryProtocolConfig] = None

   class BeaconConfig(DynamicData):
      interval: int

   class Specification(DynamicData):
      numPorts: int
      bridge: Optional[Bridge] = None
      policy: Optional[NetworkPolicy] = None
      mtu: Optional[int] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      name: str
      spec: Optional[Specification] = None

   name: str
   key: str
   numPorts: int
   numPortsAvailable: int
   mtu: Optional[int] = None
   portgroup: list[PortGroup] = []
   pnic: list[PhysicalNic] = []
   spec: Specification


class VmfsDatastoreCreateSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   vmfs: VmfsVolume.Specification
   extent: list[ScsiDisk.Partition] = []

class VmfsDatastoreExpandSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   extent: ScsiDisk.Partition

class VmfsDatastoreExtendSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   extent: list[ScsiDisk.Partition] = []


class VmfsDatastoreInfo(Datastore.Info):
   maxPhysicalRDMFileSize: long
   maxVirtualRDMFileSize: long
   vmfs: Optional[VmfsVolume] = None


class VmfsDatastoreOption(DynamicData):
   class Info(DynamicData):
      layout: DiskPartitionInfo.Layout
      partitionFormatChange: Optional[bool] = None

   class SingleExtentInfo(Info):
      vmfsExtent: DiskPartitionInfo.BlockRange

   class AllExtentInfo(SingleExtentInfo):
      pass

   class MultipleExtentInfo(Info):
      vmfsExtent: list[DiskPartitionInfo.BlockRange] = []

   info: Info
   spec: VmfsDatastoreSpec


class VmfsDatastoreSpec(DynamicData):
   diskUuid: str


class VmfsRescanResult(DynamicData):
   host: HostSystem
   fault: Optional[MethodFault] = None


class VmfsVolume(FileSystemVolume):
   class Specification(DynamicData):
      extent: ScsiDisk.Partition
      blockSizeMb: Optional[int] = None
      majorVersion: int
      volumeName: str
      blockSize: Optional[int] = None
      unmapGranularity: Optional[int] = None
      unmapPriority: Optional[str] = None
      unmapBandwidthSpec: Optional[UnmapBandwidthSpec] = None

   class UnmapBandwidthSpec(DynamicData):
      policy: str
      fixedValue: long
      dynamicMin: long
      dynamicMax: long

   class UnmapPriority(Enum):
      none: ClassVar['UnmapPriority'] = 'none'
      low: ClassVar['UnmapPriority'] = 'low'

   class UnmapBandwidthPolicy(Enum):
      fixed: ClassVar['UnmapBandwidthPolicy'] = 'fixed'
      dynamic: ClassVar['UnmapBandwidthPolicy'] = 'dynamic'

   class ConfigOption(DynamicData):
      blockSizeOption: int
      unmapGranularityOption: list[int] = []
      unmapBandwidthFixedValue: Optional[LongOption] = None
      unmapBandwidthDynamicMin: Optional[LongOption] = None
      unmapBandwidthDynamicMax: Optional[LongOption] = None
      unmapBandwidthIncrement: Optional[long] = None
      unmapBandwidthUltraLow: Optional[long] = None

   blockSizeMb: int
   blockSize: Optional[int] = None
   unmapGranularity: Optional[int] = None
   unmapPriority: Optional[str] = None
   unmapBandwidthSpec: Optional[UnmapBandwidthSpec] = None
   maxBlocks: int
   majorVersion: int
   version: str
   uuid: str
   extent: list[ScsiDisk.Partition] = []
   vmfsUpgradable: bool
   forceMountedInfo: Optional[ForceMountedInfo] = None
   ssd: Optional[bool] = None
   local: Optional[bool] = None
   scsiDiskType: Optional[str] = None


class VsanBasicDeviceInfo(DynamicData):
   deviceName: str
   pciId: Optional[str] = None
   fwVersion: Optional[str] = None
   features: list[str] = []


class VsanClusterMembershipInfo(DynamicData):
   clusterUuid: Optional[str] = None
   health: Optional[str] = None
   membershipUuid: Optional[str] = None
   memberUuid: list[str] = []

class VsanControllerType:
   pass


class VsanDaemonHealth(DynamicData):
   name: str
   alive: bool
   error: Optional[MethodFault] = None


class VsanDatastoreInfo(Datastore.Info):
   membershipUuid: Optional[str] = None
   accessGenNo: Optional[int] = None

class VsanDiskBalanceState:
   pass


class VsanDiskEncryptionHealth(DynamicData):
   diskHealth: Optional[VsanPhysicalDiskHealth] = None
   encryptionIssues: list[str] = []


class VsanDiskRebalanceResult(DynamicData):
   status: str
   bytesMoving: Optional[long] = None
   remainingBytesToMove: Optional[long] = None
   diskUsage: Optional[float] = None
   maxDiskUsage: Optional[float] = None
   minDiskUsage: Optional[float] = None
   avgDiskUsage: Optional[float] = None
   diskCompUsage: Optional[float] = None
   maxDiskCompUsage: Optional[float] = None
   minDiskCompUsage: Optional[float] = None
   avgDiskCompUsage: Optional[float] = None


class VsanDitEncryptionHealthSummary(DynamicData):
   hostname: Optional[str] = None
   health: Optional[str] = None
   reason: Optional[LocalizableMessage] = None
   ditEncryptionInfo: Optional[DataInTransitEncryptionInfo] = None


class VsanEncryptionHealthSummary(DynamicData):
   hostname: Optional[str] = None
   encryptionInfo: Optional[EncryptionInfo] = None
   overallKmsHealth: str
   kmsHealth: list[VsanKmsHealth] = []
   encryptionIssues: list[str] = []
   diskResults: list[VsanDiskEncryptionHealth] = []
   error: Optional[MethodFault] = None
   aesniEnabled: Optional[bool] = None
   inconsistentlyEncryptedObjectCount: Optional[long] = None
   hostEncryptionDekId: Optional[str] = None
   kekVerifierHealth: Optional[bool] = None
   dekVerifierHealth: Optional[bool] = None

class VsanEncryptionIssue:
   pass


class VsanFailedRepairObjectResult(DynamicData):
   uuid: str
   errMessage: Optional[str] = None


class VsanFileServerHealthSummary(DynamicData):
   domainName: Optional[str] = None
   fileServerIp: Optional[str] = None
   nfsdHealth: Optional[str] = None
   networkHealth: Optional[str] = None
   rootfsHealth: Optional[str] = None
   description: Optional[str] = None
   smbConnections: Optional[int] = None
   smbDaemonHealth: Optional[str] = None
   adTestJoinHealth: Optional[str] = None
   dnsLookupHealth: Optional[str] = None


class VsanFileServiceBalanceHealth(DynamicData):
   health: Optional[str] = None
   description: Optional[str] = None


class VsanFileServiceHealthSummary(DynamicData):
   hostname: Optional[str] = None
   overallHealth: Optional[str] = None
   enabled: Optional[bool] = None
   vdfsdStatus: Optional[VsanResourceHealth] = None
   fsvmStatus: Optional[VsanResourceHealth] = None
   rootFsStatus: Optional[VsanFileServiceRootFsHealth] = None
   fileServerHealth: list[VsanFileServerHealthSummary] = []
   fileShareHealth: list[VsanFileServiceShareHealthSummary] = []
   balanceStatus: Optional[VsanFileServiceBalanceHealth] = None
   hostLoadStatus: Optional[VsanResourceHealth] = None


class VsanFileServiceRootFsHealth(DynamicData):
   created: Optional[bool] = None
   health: Optional[str] = None
   description: Optional[str] = None


class VsanFileServiceShareHealthSummary(DynamicData):
   overallHealth: Optional[str] = None
   domainName: Optional[str] = None
   shareUuid: Optional[str] = None
   shareName: Optional[str] = None
   objectHealth: Optional[VsanObjectOverallHealth] = None
   description: Optional[str] = None
   extensible: Optional[bool] = None
   spbmProfileUuid: Optional[str] = None
   spbmProfileGenerationId: Optional[str] = None
   sharePolicyMismatch: Optional[bool] = None


class VsanHclCommonDeviceInfo(DynamicData):
   deviceName: str
   displayName: Optional[str] = None
   driverName: Optional[str] = None
   driverVersion: Optional[str] = None
   vendorId: Optional[long] = None
   deviceId: Optional[long] = None
   subVendorId: Optional[long] = None
   subDeviceId: Optional[long] = None
   extraInfo: list[KeyValue] = []
   deviceOnHcl: Optional[bool] = None
   releaseSupported: Optional[bool] = None
   releasesOnHcl: list[str] = []
   driverVersionsOnHcl: list[str] = []
   driverVersionSupported: Optional[bool] = None
   fwVersionSupported: Optional[bool] = None
   fwVersionOnHcl: list[str] = []
   fwVersion: Optional[str] = None
   driversOnHcl: list[VsanHclDriverInfo] = []


class VsanHclComputeResource(DynamicData):
   memory: VsanHclMemInfo


class VsanHclControllerInfo(DynamicData):
   deviceName: str
   deviceDisplayName: Optional[str] = None
   driverName: Optional[str] = None
   driverVersion: Optional[str] = None
   vendorId: Optional[long] = None
   deviceId: Optional[long] = None
   subVendorId: Optional[long] = None
   subDeviceId: Optional[long] = None
   extraInfo: list[KeyValue] = []
   deviceOnHcl: Optional[bool] = None
   releaseSupported: Optional[bool] = None
   releasesOnHcl: list[str] = []
   driverVersionsOnHcl: list[str] = []
   driverVersionSupported: Optional[bool] = None
   fwVersionSupported: Optional[bool] = None
   fwVersionOnHcl: list[str] = []
   cacheConfigSupported: Optional[bool] = None
   cacheConfigOnHcl: list[str] = []
   raidConfigSupported: Optional[bool] = None
   raidConfigOnHcl: list[str] = []
   fwVersion: Optional[str] = None
   raidConfig: Optional[str] = None
   cacheConfig: Optional[str] = None
   cimProviderInfo: Optional[VsanHostCimProviderInfo] = None
   usedByVsan: Optional[bool] = None
   disks: list[VsanHclDiskInfo] = []
   issues: list[MethodFault] = []
   remediableIssues: list[str] = []
   driversOnHcl: list[VsanHclDriverInfo] = []
   fwAuxVersion: Optional[str] = None
   queueDepth: Optional[long] = None
   queueDepthOnHcl: Optional[long] = None
   queueDepthSupported: Optional[bool] = None
   diskMode: Optional[str] = None
   diskModeOnHcl: list[str] = []
   diskModeSupported: Optional[bool] = None
   toolName: Optional[str] = None
   toolVersion: Optional[str] = None
   productId: Optional[str] = None
   diskCapacity: Optional[long] = None
   vcgEntryInfo: list[VsanVcgDeviceInfo] = []
   controllerType: Optional[str] = None
   userSelectedVcgId: Optional[int] = None
   vsanCompatibility: list[str] = []


class VsanHclDiskInfo(DynamicData):
   deviceName: str
   model: Optional[str] = None
   isSsd: Optional[bool] = None
   vsanDisk: bool
   issues: list[MethodFault] = []
   remediableIssues: list[str] = []
   uuid: Optional[str] = None
   capacity: Optional[long] = None
   vsanCompatibility: list[str] = []


class VsanHclFirmwareFile(DynamicData):
   fileType: str
   filenameOrUrl: str
   sha1sum: str


class VsanHclFirmwareUpdateSpec(DynamicData):
   host: HostSystem
   hbaDevice: str
   fwFiles: list[VsanHclFirmwareFile] = []
   allowDowngrade: Optional[bool] = None
   firmwareComponent: list[VsanHostFwComponent] = []


class VsanHclMemInfo(DynamicData):
   memorySize: Optional[long] = None
   vsanHostCompatibility: list[str] = []


class VsanHclNicInfo(VsanHclCommonDeviceInfo):
   vmknic: Optional[str] = None
   useByVsan: Optional[bool] = None
   rdmaConfig: Optional[VsanNicRdmaInfo] = None
   vsanHostCompatibility: list[str] = []
   nicLinkSpeedInMbps: Optional[int] = None


class VsanHealthObjectStats(DynamicData):
   numAutoManagedObjects: long
   numFTT3ManagedObjects: long


class VsanHealthQuerySpec(DynamicData):
   includeAllRemoteClusters: Optional[bool] = None
   remoteClusterUuids: list[str] = []
   latencyOnly: Optional[bool] = None
   mode: Optional[str] = None


class VsanHealthSystem(ManagedObject):
   def QueryVerifyNetworkSettings(self, peers: list[str], ROBOStretchedClusterWitnesses: list[str], vMotionPeers: list[str], spec: Optional[VsanHealthQuerySpec]) -> VsanNetworkHealthResult: ...
   def QueryCheckLimits(self, spec: Optional[VsanHostQueryCheckLimitsSpec]) -> VsanLimitHealthResult: ...
   def QueryHostInfoByUuids(self, uuids: list[str]) -> list[VsanQueryResultHostInfo]: ...
   def QueryAdvCfg(self, options: list[str], includeAllAdvOptions: Optional[bool], nonDefaultOnly: Optional[bool]) -> list[OptionValue]: ...
   def QueryRunIperfServer(self, multicast: bool, serverIp: Optional[str], durationSec: Optional[int]) -> VsanNetworkLoadTestResult: ...
   def QueryRunIperfClient(self, multicast: bool, serverIp: str, durationSec: Optional[int], spec: Optional[VsanIperfClientSpec]) -> VsanNetworkLoadTestResult: ...
   def QueryObjectHealthSummary(self, objUuids: list[str], includeObjUuids: Optional[bool], localHostOnly: Optional[bool], includeNonComplianceObjDetail: Optional[bool], spec: Optional[VsanHealthQuerySpec]) -> VsanObjectOverallHealth: ...
   def QueryPhysicalDiskHealthSummary(self) -> VsanPhysicalDiskHealthSummary: ...
   def QueryEncryptionHealthSummary(self) -> VsanEncryptionHealthSummary: ...
   def QueryFileServiceHealthSummary(self) -> VsanFileServiceHealthSummary: ...
   def PrepareVmdkLoadTest(self, runname: str, specs: list[VsanVmdkLoadTestSpec]) -> str: ...
   def RunVmdkLoadTest(self, runname: str, durationSec: int, specs: list[VsanVmdkLoadTestSpec]) -> list[VsanVmdkLoadTestResult]: ...
   def CleanupVmdkLoadTest(self, runname: str, specs: list[VsanVmdkLoadTestSpec]) -> str: ...
   def QueryVersion(self, displayVersion: Optional[bool]) -> str: ...
   def CheckClomdLiveness(self) -> bool: ...
   def RepairImmediateObjects(self, uuids: list[str], repairType: Optional[str]) -> VsanRepairObjectsResult: ...
   def GetHclInfo(self, includeVendorInfo: Optional[bool], vsanEsaEligibleDisksOnly: Optional[bool]) -> VsanHostHclInfo: ...
   def StartProactiveRebalance(self, timeSpan: Optional[int], varianceThreshold: Optional[float], timeThreshold: Optional[int], rateThreshold: Optional[int]) -> bool: ...
   def StopProactiveRebalance(self) -> bool: ...
   def GetProactiveRebalanceInfo(self) -> VsanProactiveRebalanceInfoEx: ...
   def WaitForVsanHealthGenerationIdChange(self, timeout: int) -> bool: ...
   def FlashScsiControllerFirmware(self, spec: VsanHclFirmwareUpdateSpec) -> Task: ...
   def CreateVmHealthTest(self, timeout: int) -> VsanHostCreateVmHealthTestResult: ...
   def QuerySmartStats(self, disks: list[str], includeAllDisks: Optional[bool]) -> VsanSmartStatsHostSummary: ...
   def QueryHostEMMState(self) -> VsanHostEMMSummary: ...
   def GetNetworkDiagnosticsHealthInfo(self) -> VsanNetworkDiagnosticsHealthInfo: ...


class VsanHostCimProviderInfo(DynamicData):
   cimProviderSupported: Optional[bool] = None
   installedCIMProvider: Optional[str] = None
   cimProviderOnHcl: list[str] = []
   cimProviderLinksOnHcl: list[VsanDownloadItem] = []


class VsanHostEMMSummary(DynamicData):
   hostname: Optional[str] = None
   inMaintenanceMode: Optional[bool] = None
   inDecomState: Optional[bool] = None


class VsanHostFwComponent(DynamicData):
   name: str
   url: Optional[str] = None
   sha1sum: Optional[str] = None
   currentVersion: Optional[str] = None
   suggestedVersion: Optional[str] = None
   componentID: list[str] = []


class VsanHostGlobalDedupConfigHealthSummary(DynamicData):
   hostname: Optional[str] = None
   health: Optional[str] = None


class VsanHostHciMeshDitEncryptionHealth(DynamicData):
   clusterUuid: str
   clusterName: str
   ownerVc: Optional[str] = None
   isLocalOwnerVc: Optional[bool] = None
   health: str
   issues: list[str] = []


class VsanHostHciMeshDitEncryptionHealthSummary(DynamicData):
   hostname: str
   clusterUuid: str
   clusterName: str
   ownerVc: str
   isLocalOwnerVc: Optional[bool] = None
   capable: Optional[bool] = None
   clusterHealths: list[VsanHostHciMeshDitEncryptionHealth] = []


class VsanHostHclInfo(DynamicData):
   hostname: str
   hclChecked: bool
   releaseName: Optional[str] = None
   error: Optional[MethodFault] = None
   controllers: list[VsanHclControllerInfo] = []
   pnics: list[VsanHclNicInfo] = []
   host: Optional[HostSystem] = None
   computeResource: Optional[VsanHclComputeResource] = None
   vsanHostCompatibility: list[str] = []


class VsanHostHealthSystemStatusResult(DynamicData):
   hostname: str
   status: str
   issues: list[str] = []


class VsanHostHwDeviceId(DynamicData):
   pciId: DevicePciId
   productId: Optional[str] = None
   diskCapacity: Optional[long] = None


class VsanHostIoInsightInfo(DynamicData):
   host: HostSystem
   ioinsightWorldId: Optional[long] = None
   faultMessage: Optional[str] = None
   ioinsightInfo: Optional[VsanIoInsightInfo] = None

class VsanHostQueryCheckLimitsOptionType:
   pass


class VsanHostQueryCheckLimitsSpec(DynamicData):
   optionTypes: list[str] = []
   fetchAll: bool


class VsanHostReference(DynamicData):
   hostname: str


class VsanHostVirtualApplianceInfo(DynamicData):
   hostKey: HostSystem
   isVirtualApp: bool
   isDeployedFromOVF: Optional[bool] = None


class VsanHostVmdkLoadTestResult(DynamicData):
   hostname: str
   issueFound: bool
   faultMessage: Optional[str] = None
   vmdkResults: list[VsanVmdkLoadTestResult] = []


class VsanHwToVcgInfoMapping(DynamicData):
   vsanHostHwDeviceId: VsanHostHwDeviceId
   vcgId: int


class VsanInternalSystem(ManagedObject):
   class CmmdsQuery(DynamicData):
      type: Optional[str] = None
      uuid: Optional[str] = None
      owner: Optional[str] = None

   class PolicyCost(DynamicData):
      changeDataSize: Optional[long] = None
      currentDataSize: Optional[long] = None
      tempDataSize: Optional[long] = None
      copyDataSize: Optional[long] = None
      changeFlashReadCacheSize: Optional[long] = None
      currentFlashReadCacheSize: Optional[long] = None
      currentDiskSpaceToAddressSpaceRatio: Optional[float] = None
      diskSpaceToAddressSpaceRatio: Optional[float] = None

   class PolicySatisfiability(DynamicData):
      uuid: Optional[str] = None
      isSatisfiable: bool
      reason: Optional[LocalizableMessage] = None
      cost: Optional[PolicyCost] = None

   class PolicyChangeBatch(DynamicData):
      uuid: list[str] = []
      policy: Optional[str] = None

   class NewPolicyBatch(DynamicData):
      size: list[long] = []
      policy: Optional[str] = None

   class VsanPhysicalDiskDiagnosticsResult(DynamicData):
      diskUuid: str
      success: bool
      failureReason: Optional[str] = None

   class DeleteVsanObjectsResult(DynamicData):
      uuid: str
      success: bool
      failureReason: list[LocalizableMessage] = []

   class VsanObjectOperationResult(DynamicData):
      uuid: str
      failureReason: list[LocalizableMessage] = []

   def QueryCmmds(self, queries: list[CmmdsQuery]) -> str: ...
   def QueryPhysicalVsanDisks(self, props: list[str]) -> str: ...
   def QueryVsanObjects(self, uuids: list[str]) -> str: ...
   def QueryObjectsOnPhysicalVsanDisk(self, disks: list[str]) -> str: ...
   def AbdicateDomOwnership(self, uuids: list[str]) -> list[str]: ...
   def QueryVsanStatistics(self, labels: list[str]) -> str: ...
   def ReconfigureDomObject(self, uuid: str, policy: str) -> None: ...
   def QuerySyncingVsanObjects(self, uuids: list[str]) -> str: ...
   def RunVsanPhysicalDiskDiagnostics(self, disks: list[str]) -> list[VsanPhysicalDiskDiagnosticsResult]: ...
   def GetVsanObjExtAttrs(self, uuids: list[str]) -> str: ...
   def ReconfigurationSatisfiable(self, pcbs: list[PolicyChangeBatch], ignoreSatisfiability: Optional[bool]) -> list[PolicySatisfiability]: ...
   def CanProvisionObjects(self, npbs: list[NewPolicyBatch], ignoreSatisfiability: Optional[bool]) -> list[PolicySatisfiability]: ...
   def DeleteVsanObjects(self, uuids: list[str], force: Optional[bool]) -> list[DeleteVsanObjectsResult]: ...
   def UpgradeVsanObjects(self, uuids: list[str], newVersion: int) -> list[VsanObjectOperationResult]: ...
   def QueryVsanObjectUuidsByFilter(self, uuids: list[str], limit: Optional[int], version: Optional[int]) -> list[str]: ...


class VsanIoInsightInfo(DynamicData):
   state: Optional[str] = None
   monitoredVMs: list[VirtualMachine] = []

class VsanIoInsightState:
   pass


class VsanIperfClientSpec(DynamicData):
   Reverse: bool


class VsanKmsHealth(DynamicData):
   serverName: str
   health: str
   error: Optional[MethodFault] = None
   trustHealth: Optional[str] = None
   certHealth: Optional[str] = None
   certExpireDate: Optional[datetime] = None


class VsanLicensedDiskResult(DynamicData):
   uuid: str
   name: str
   capacity: long


class VsanLimitHealthResult(DynamicData):
   hostname: Optional[str] = None
   issueFound: bool
   maxComponents: int
   freeComponents: int
   componentLimitHealth: str
   lowestFreeDiskSpacePct: int
   usedDiskSpaceB: long
   totalDiskSpaceB: long
   diskFreeSpaceHealth: str
   reservedRcSizeB: long
   totalRcSizeB: long
   rcFreeReservationHealth: str
   totalLogicalSpaceB: Optional[long] = None
   logicalSpaceUsedB: Optional[long] = None
   dedupMetadataSizeB: Optional[long] = None
   diskTransientCapacityUsedB: Optional[long] = None
   dgTransientCapacityUsedB: Optional[long] = None
   slackSpaceCapRequired: Optional[long] = None
   resyncPauseThreshold: Optional[long] = None
   spaceEfficiencyMetadataSizeB: Optional[VsanSpaceEfficiencyMetadataSize] = None
   hostRebuildCapacity: Optional[long] = None
   minSpaceRequiredForVsanOp: Optional[long] = None
   enforceCapResrvSpace: Optional[long] = None
   cdReservedSizeB: Optional[long] = None


class VsanNetworkDiagnosticsHealthInfo(DynamicData):
   vnicInfo: list[VirtualNic] = []
   pnicTSOInfo: list[PnicTSOInfo] = []
   LACPInfo: list[LACPInfo] = []


class VsanNetworkHealthResult(DynamicData):
   host: Optional[HostSystem] = None
   hostname: Optional[str] = None
   vsanVmknicPresent: Optional[bool] = None
   ipSubnets: list[str] = []
   issueFound: Optional[bool] = None
   peerHealth: list[VsanNetworkPeerHealthResult] = []
   vMotionHealth: list[VsanNetworkPeerHealthResult] = []
   multicastConfig: Optional[str] = None
   unicastConfig: Optional[str] = None
   inUnicast: Optional[bool] = None
   rdmaEnabled: Optional[bool] = None
   rdtConnProtocol: Optional[str] = None
   serverClusters: list[VsanServerClusterInfo] = []
   externalPeerHealth: list[VsanNetworkPeerHealthResult] = []


class VsanNetworkLoadTestResult(DynamicData):
   hostname: str
   status: Optional[str] = None
   client: bool
   bandwidthBps: long
   totalBytes: long
   lostDatagrams: Optional[long] = None
   lossPct: Optional[long] = None
   sentDatagrams: Optional[long] = None
   jitterMs: Optional[float] = None


class VsanNetworkPeerHealthResult(DynamicData):
   peer: Optional[str] = None
   peerHostname: Optional[str] = None
   peerVmknicName: Optional[str] = None
   smallPingTestSuccessPct: Optional[int] = None
   largePingTestSuccessPct: Optional[int] = None
   maxLatencyUs: Optional[long] = None
   onSameIpSubnet: Optional[bool] = None
   sourceVmknicName: Optional[str] = None
   connectivityHealthState: Optional[str] = None
   missingHeartBeatCount: Optional[int] = None


class VsanNicRdmaInfo(DynamicData):
   rdmaCapable: Optional[bool] = None
   rdmaProtocolCapable: Optional[str] = None
   dcbEnabled: Optional[bool] = None
   dcbMode: Optional[str] = None
   pfcEnabled: Optional[bool] = None
   pfcConfig: Optional[str] = None


class VsanObjectHealth(DynamicData):
   class VsanObjectHealthState(Enum):
      inaccessible: ClassVar['VsanObjectHealthState'] = 'inaccessible'
      reducedavailabilitywithnorebuild: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithnorebuild'
      reducedavailabilitywithnorebuilddelaytimer: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithnorebuilddelaytimer'
      reducedavailabilitywithactiverebuild: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithactiverebuild'
      datamove: ClassVar['VsanObjectHealthState'] = 'datamove'
      nonavailabilityrelatedreconfig: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedreconfig'
      nonavailabilityrelatedincompliance: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliance'
      healthy: ClassVar['VsanObjectHealthState'] = 'healthy'
      reducedavailabilitywithpolicypending: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpolicypending'
      reducedavailabilitywithpolicypendingfailed: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpolicypendingfailed'
      reducedavailabilitywithpausedrebuild: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpausedrebuild'
      nonavailabilityrelatedincompliancewithpolicypending: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpolicypending'
      nonavailabilityrelatedincompliancewithpolicypendingfailed: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpolicypendingfailed'
      nonavailabilityrelatedincompliancewithpausedrebuild: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpausedrebuild'
      remoteAccessible: ClassVar['VsanObjectHealthState'] = 'remoteAccessible'
      VsanObjectHealthState_Unknown: ClassVar['VsanObjectHealthState'] = 'VsanObjectHealthState_Unknown'

   numObjects: int
   health: Optional[str] = None
   objUuids: list[str] = []
   vsanClusterUuid: Optional[str] = None


class VsanObjectOverallHealth(DynamicData):
   objectHealthDetail: list[VsanObjectHealth] = []
   objectsComplianceDetail: list[StorageComplianceResult] = []
   objectVersionCompliance: Optional[bool] = None
   objectFormatChangeRequiredUuids: list[str] = []
   objectsRelayoutBytes: Optional[long] = None
   globalDedupStoreHealth: Optional[str] = None
   objectStats: Optional[VsanHealthObjectStats] = None
   vsanObjectsForObjectStoreVolumes: list[str] = []

class VsanPeerHostConnectivityHealthState:
   pass


class VsanPhysicalDiskHealth(DynamicData):
   name: str
   uuid: str
   inCmmds: bool
   inVsi: bool
   dedupScope: Optional[long] = None
   formatVersion: Optional[int] = None
   isAllFlash: Optional[int] = None
   congestionValue: Optional[int] = None
   congestionArea: Optional[str] = None
   congestionHealth: Optional[str] = None
   metadataHealth: Optional[str] = None
   operationalHealthDescription: Optional[str] = None
   operationalHealth: Optional[str] = None
   dedupUsageHealth: Optional[str] = None
   capacityHealth: Optional[str] = None
   summaryHealth: str
   capacity: Optional[long] = None
   usedCapacity: Optional[long] = None
   reservedCapacity: Optional[long] = None
   totalBytes: Optional[long] = None
   freeBytes: Optional[long] = None
   hashedBytes: Optional[long] = None
   dedupedBytes: Optional[long] = None
   scsiDisk: Optional[ScsiDisk] = None
   usedComponents: Optional[long] = None
   maxComponents: Optional[long] = None
   compLimitHealth: Optional[str] = None
   encryptionEnabled: Optional[bool] = None
   kmsProviderId: Optional[str] = None
   kekId: Optional[str] = None
   dekGenerationId: Optional[long] = None
   encryptedUnlocked: Optional[bool] = None
   rebalanceResult: Optional[VsanDiskRebalanceResult] = None
   dekId: Optional[str] = None
   kekVerifierHealth: Optional[bool] = None
   dekVerifierHealth: Optional[bool] = None
   logicalCapacity: Optional[long] = None
   logicalCapacityUsed: Optional[long] = None
   logicalCapacityHealth: Optional[str] = None
   vsanDiskGroupUuid: Optional[str] = None
   dgLayoutIssue: Optional[bool] = None
   usedMetadataComponents: Optional[long] = None
   maxMetadataComponents: Optional[long] = None
   pendingClusterDekId: Optional[str] = None
   dmekVerifierHealth: Optional[bool] = None


class VsanPhysicalDiskHealthSummary(DynamicData):
   overallHealth: str
   heapsWithIssues: list[VsanResourceHealth] = []
   slabsWithIssues: list[VsanResourceHealth] = []
   disks: list[VsanPhysicalDiskHealth] = []
   componentsWithIssues: list[VsanResourceHealth] = []
   hostname: Optional[str] = None
   hostDedupScope: Optional[int] = None
   error: Optional[MethodFault] = None
   licensedDisks: list[VsanLicensedDiskResult] = []


class VsanProactiveRebalanceInfoEx(DynamicData):
   running: Optional[bool] = None
   startTs: Optional[datetime] = None
   stopTs: Optional[datetime] = None
   varianceThreshold: Optional[float] = None
   timeThreshold: Optional[int] = None
   rateThreshold: Optional[int] = None
   hostname: Optional[str] = None
   error: Optional[MethodFault] = None


class VsanQueryResultHostInfo(DynamicData):
   uuid: Optional[str] = None
   hostnameInCmmds: Optional[str] = None
   vsanIpv4Addresses: list[str] = []


class VsanRepairObjectsResult(DynamicData):
   inQueueObjects: list[str] = []
   failedRepairObjects: list[VsanFailedRepairObjectResult] = []
   notInQueueObjects: list[str] = []


class VsanResourceHealth(DynamicData):
   resource: str
   health: str
   description: Optional[str] = None


class VsanServerClusterInfo(DynamicData):
   cluster: Optional[ClusterComputeResource] = None
   peerHealth: list[VsanNetworkPeerHealthResult] = []
   membership: Optional[VsanClusterMembershipInfo] = None


class VsanSmartDiskStats(DynamicData):
   disk: str
   stats: list[VsanSmartParameter] = []
   error: Optional[MethodFault] = None


class VsanSmartParameter(DynamicData):
   parameter: Optional[str] = None
   value: Optional[int] = None
   threshold: Optional[int] = None
   worst: Optional[int] = None

class VsanSmartParameterType:
   pass


class VsanSmartStatsHostSummary(DynamicData):
   hostname: Optional[str] = None
   smartStats: list[VsanSmartDiskStats] = []


class VsanSystem(ManagedObject):
   @property
   def config(self) -> ConfigInfo: ...

   def QueryDisksForVsan(self, canonicalName: list[str]) -> list[DiskResult]: ...
   def AddDisks(self, disk: list[ScsiDisk]) -> Task: ...
   def InitializeDisks(self, mapping: list[DiskMapping]) -> Task: ...
   def RemoveDisk(self, disk: list[ScsiDisk], maintenanceSpec: Optional[MaintenanceSpec], timeout: Optional[int]) -> Task: ...
   def RemoveDiskMapping(self, mapping: list[DiskMapping], maintenanceSpec: Optional[MaintenanceSpec], timeout: Optional[int]) -> Task: ...
   def UnmountDiskMapping(self, mapping: list[DiskMapping]) -> Task: ...
   def Update(self, config: ConfigInfo) -> Task: ...
   def QueryHostStatus(self) -> ClusterStatus: ...
   def EvacuateNode(self, maintenanceSpec: MaintenanceSpec, timeout: int) -> Task: ...
   def RecommissionNode(self) -> Task: ...


class VsanSystemEx(ManagedObject):
   def QueryWhatIfEvacuationResult(self, evacEntityUuid: str) -> VsanWhatIfEvacResult: ...
   def GetRuntimeStats(self, stats: list[str], clusterUuid: Optional[str]) -> RuntimeStats: ...
   def GetAboutInfoEx(self) -> AboutInfoEx: ...
   def QuerySyncingVsanObjects(self, uuids: list[str], start: Optional[int], limit: Optional[int], includeSummary: Optional[bool]) -> VsanSyncingObjectQueryResult: ...
   def QueryHostDrsStats(self, hostUuids: list[str], vms: list[str], hostIndex: Optional[int]) -> DrsStats: ...
   def UnmountDiskMappingEx(self, mappings: list[DiskMapping], maintenanceSpec: Optional[MaintenanceSpec], timeout: Optional[int], evacReason: Optional[str]) -> Task: ...
   def QueryHostStatusEx(self, clusterUuids: list[str]) -> list[ClusterStatus]: ...
   def WipeDisk(self, disks: list[str]) -> Task: ...
   def QueryWipeDiskStatus(self, disks: list[str]) -> list[WipeDiskStatus]: ...
   def AbortWipeDisk(self, disks: list[str]) -> list[AbortWipeDiskStatus]: ...


class VsanUpdateManager(ManagedObject):
   def VsanVibScan(self, cluster: Optional[ComputeResource], vibSpecs: list[VsanVibSpec]) -> list[VsanVibScanResult]: ...
   def VsanVibInstall(self, cluster: Optional[ComputeResource], vibSpecs: list[VsanVibSpec], scanResults: list[VsanVibScanResult], firmwareSpecs: list[VsanHclFirmwareUpdateSpec], maintenanceSpec: Optional[MaintenanceSpec], rolling: Optional[bool], noSigCheck: Optional[bool]) -> Task: ...
   def VsanVibInstallPreflightCheck(self, cluster: Optional[ComputeResource]) -> VsanVibInstallPreflightStatus: ...


class VsanVcgDeviceInfo(DynamicData):
   vcgId: int
   vcgModelName: Optional[str] = None


class VsanVcsaDeployerSystem(ManagedObject):
   def PrepareVsanForVcsa(self, spec: VsanPrepareVsanForVcsaSpec) -> Optional[str]: ...
   def PostConfigForVcsa(self, spec: VsanVcPostDeployConfigSpec) -> Optional[str]: ...
   def VcsaGetBootstrapProgress(self, taskId: list[str]) -> list[VsanVcsaDeploymentProgress]: ...


class VsanVmdkIOLoadSpec(DynamicData):
   readPct: int
   oio: int
   iosizeB: int
   dataSizeMb: long
   random: bool
   startOffsetB: Optional[long] = None


class VsanVmdkLoadTestResult(DynamicData):
   success: bool
   faultMessage: Optional[str] = None
   spec: VsanVmdkLoadTestSpec
   actualDurationSec: Optional[int] = None
   totalBytes: Optional[long] = None
   iops: Optional[long] = None
   tputBps: Optional[long] = None
   avgLatencyUs: Optional[long] = None
   maxLatencyUs: Optional[long] = None
   numIoAboveLatencyThreshold: Optional[long] = None


class VsanVmdkLoadTestSpec(DynamicData):
   vmdkCreateSpec: Optional[VirtualDiskManager.FileBackedVirtualDiskSpec] = None
   vmdkIOSpec: Optional[VsanVmdkIOLoadSpec] = None
   vmdkIOSpecSequence: list[VsanVmdkIOLoadSpec] = []
   stepDurationSec: Optional[long] = None


class VsanVsanPcapResult(DynamicData):
   calltime: float
   vmknic: str
   tcpdumpFilter: str
   snaplen: int
   pkts: list[str] = []
   pcap: Optional[str] = None
   error: Optional[MethodFault] = None
   hostname: Optional[str] = None


class VvolDatastoreInfo(Datastore.Info):
   vvolDS: Optional[VvolVolume] = None


class VvolNQN(DynamicData):
   targetNQN: str
   storageArray: str
   online: bool


class VvolVolume(FileSystemVolume):
   class Specification(DynamicData):
      maxSizeInMB: long
      volumeName: str
      vasaProviderInfo: list[VimVasaProviderInfo] = []
      storageArray: list[VasaStorageArray] = []
      uuid: str
      stretched: Optional[bool] = None

   class HostProtocolEndpoint(DynamicData):
      key: HostSystem
      protocolEndpoint: list[ProtocolEndpoint] = []

   class HostVvolNQN(DynamicData):
      host: Optional[HostSystem] = None
      vvolNQN: list[VvolNQN] = []

   scId: str
   hostPE: list[HostProtocolEndpoint] = []
   hostVvolNQN: list[HostVvolNQN] = []
   vasaProviderInfo: list[VimVasaProviderInfo] = []
   storageArray: list[VasaStorageArray] = []
   protocolEndpointType: Optional[str] = None
   vvolNQNFieldsAvailable: Optional[bool] = None
   stretched: Optional[bool] = None
