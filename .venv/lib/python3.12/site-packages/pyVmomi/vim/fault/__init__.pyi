# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.VmomiSupport import long
from pyVmomi.vim import ComputeResource

from pyVmomi.vim import Datacenter

from pyVmomi.vim import Datastore

from pyVmomi.vim import HostSystem

from pyVmomi.vim import KeyValue
from pyVmomi.vim import LicenseManager

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim import Network
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine
from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault
from pyVmomi.vmodl import RuntimeFault

from pyVmomi.vim.cluster import RuleInfo

from pyVmomi.vim.cns import SnapshotId
from pyVmomi.vim.cns import VolumeId
from pyVmomi.vim.dvs import ProductSpec

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.event import Event

from pyVmomi.vim.profile import Profile

from pyVmomi.vim.profile import ProfilePropertyPath

from pyVmomi.vim.vm import FeatureRequirement

from pyVmomi.vmodl.fault import InvalidArgument

from pyVmomi.vmodl.fault import NotEnoughLicenses
from pyVmomi.vmodl.fault import NotSupported

from pyVmomi.vmodl.fault import SecurityError
from pyVmomi.vim.vm.device import VirtualCdrom

from pyVmomi.vim.vm.device import VirtualDevice

from pyVmomi.vim.vm.device import VirtualDeviceSpec

from pyVmomi.vim.vm.device import VirtualDiskId

from pyVmomi.vim.vm.guest import GuestAuthentication



class ActiveDirectoryFault(VimFault):
   errorCode: Optional[int] = None


class ActiveVMsBlockingEVC(EVCConfigFault):
   evcMode: Optional[str] = None
   host: list[HostSystem] = []
   hostName: list[str] = []

class AdminDisabled(HostConfigFault):
   pass

class AdminNotDisabled(HostConfigFault):
   pass


class AffinityConfigured(MigrationFault):
   class Affinity(Enum):
      memory: ClassVar['Affinity'] = 'memory'
      cpu: ClassVar['Affinity'] = 'cpu'

   configuredAffinity: list[str] = []


class AgentInstallFailed(HostConnectFault):
   class Reason(Enum):
      NotEnoughSpaceOnDevice: ClassVar['Reason'] = 'NotEnoughSpaceOnDevice'
      PrepareToUpgradeFailed: ClassVar['Reason'] = 'PrepareToUpgradeFailed'
      AgentNotRunning: ClassVar['Reason'] = 'AgentNotRunning'
      AgentNotReachable: ClassVar['Reason'] = 'AgentNotReachable'
      InstallTimedout: ClassVar['Reason'] = 'InstallTimedout'
      SignatureVerificationFailed: ClassVar['Reason'] = 'SignatureVerificationFailed'
      AgentUploadFailed: ClassVar['Reason'] = 'AgentUploadFailed'
      AgentUploadTimedout: ClassVar['Reason'] = 'AgentUploadTimedout'
      UnknownInstallerError: ClassVar['Reason'] = 'UnknownInstallerError'

   reason: Optional[str] = None
   statusCode: Optional[int] = None
   installerOutput: Optional[str] = None

class AlreadyBeingManaged(HostConnectFault):
   ipAddress: str

class AlreadyConnected(HostConnectFault):
   name: str


class AlreadyExists(VimFault):
   name: Optional[str] = None

class AlreadyUpgraded(VimFault):
   pass


class AnswerFileUpdateFailed(VimFault):
   class UpdateFailure(DynamicData):
      userInputPath: ProfilePropertyPath
      errMsg: LocalizableMessage

   failure: list[UpdateFailure] = []

class ApplicationQuiesceFault(SnapshotFault):
   pass

class AuthMinimumAdminPermission(VimFault):
   pass


class BackupBlobReadFailure(DvsFault):
   entityName: str
   entityType: str
   fault: MethodFault


class BackupBlobWriteFailure(DvsFault):
   entityName: str
   entityType: str
   fault: MethodFault

class BlockedByFirewall(HostConfigFault):
   pass

class CAMServerRefusedConnection(InvalidCAMServer):
   pass

class CannotAccessFile(FileFault):
   pass

class CannotAccessLocalSource(VimFault):
   pass


class CannotAccessNetwork(CannotAccessVmDevice):
   network: Optional[Network] = None

class CannotAccessVmComponent(VmConfigFault):
   pass


class CannotAccessVmConfig(CannotAccessVmComponent):
   reason: MethodFault

class CannotAccessVmDevice(CannotAccessVmComponent):
   device: str
   backing: str
   connected: bool


class CannotAccessVmDisk(CannotAccessVmDevice):
   fault: MethodFault

class CannotAddHostWithFTVmAsStandalone(HostConnectFault):
   pass

class CannotAddHostWithFTVmToDifferentCluster(HostConnectFault):
   pass

class CannotAddHostWithFTVmToNonHACluster(HostConnectFault):
   pass


class CannotChangeDrsBehaviorForFtSecondary(VmFaultToleranceIssue):
   vm: VirtualMachine
   vmName: str


class CannotChangeHaSettingsForFtSecondary(VmFaultToleranceIssue):
   vm: VirtualMachine
   vmName: str

class CannotChangeVsanClusterUuid(VsanFault):
   pass

class CannotChangeVsanNodeUuid(VsanFault):
   pass


class CannotComputeFTCompatibleHosts(VmFaultToleranceIssue):
   vm: VirtualMachine
   vmName: str

class CannotCreateFile(FileFault):
   pass

class CannotDecryptPasswords(CustomizationFault):
   pass

class CannotDeleteFile(FileFault):
   pass


class CannotDisableDrsOnClustersWithVApps(RuntimeFault):
   pass

class CannotDisableSnapshot(VmConfigFault):
   pass

class CannotDisconnectHostWithFaultToleranceVm(VimFault):
   hostName: str


class CannotEnableVmcpForCluster(VimFault):
   class Reason(Enum):
      APDTimeoutDisabled: ClassVar['Reason'] = 'APDTimeoutDisabled'

   host: Optional[HostSystem] = None
   hostName: Optional[str] = None
   reason: Optional[str] = None

class CannotModifyConfigCpuRequirements(MigrationFault):
   pass


class CannotMoveFaultToleranceVm(VimFault):
   class MoveType(Enum):
      resourcePool: ClassVar['MoveType'] = 'resourcePool'
      cluster: ClassVar['MoveType'] = 'cluster'

   moveType: str
   vmName: str

class CannotMoveHostWithFaultToleranceVm(VimFault):
   pass

class CannotMoveVmWithDeltaDisk(MigrationFault):
   device: str

class CannotMoveVmWithNativeDeltaDisk(MigrationFault):
   pass

class CannotMoveVsanEnabledHost(VsanFault):
   pass

class CannotPlaceWithoutPrerequisiteMoves(VimFault):
   pass


class CannotPowerOffVmInCluster(InvalidState):
   class Operation(Enum):
      suspend: ClassVar['Operation'] = 'suspend'
      powerOff: ClassVar['Operation'] = 'powerOff'
      guestShutdown: ClassVar['Operation'] = 'guestShutdown'
      guestSuspend: ClassVar['Operation'] = 'guestSuspend'

   operation: str
   vm: VirtualMachine
   vmName: str

class CannotReconfigureVsanWhenHaEnabled(VsanFault):
   pass


class CannotUseNetwork(VmConfigFault):
   class Reason(Enum):
      NetworkReservationNotSupported: ClassVar['Reason'] = 'NetworkReservationNotSupported'
      MismatchedNetworkPolicies: ClassVar['Reason'] = 'MismatchedNetworkPolicies'
      MismatchedDvsVersionOrVendor: ClassVar['Reason'] = 'MismatchedDvsVersionOrVendor'
      VMotionToUnsupportedNetworkType: ClassVar['Reason'] = 'VMotionToUnsupportedNetworkType'
      NetworkUnderMaintenance: ClassVar['Reason'] = 'NetworkUnderMaintenance'
      MismatchedEnsMode: ClassVar['Reason'] = 'MismatchedEnsMode'
      MismatchedRealTimeDvs: ClassVar['Reason'] = 'MismatchedRealTimeDvs'
      NsxNetworkAvailabilityDegraded: ClassVar['Reason'] = 'NsxNetworkAvailabilityDegraded'

   device: str
   backing: str
   connected: bool
   reason: str
   network: Optional[Network] = None

class ClockSkew(HostConfigFault):
   pass

class CloneFromSnapshotNotSupported(MigrationFault):
   pass


class CnsAlreadyRegisteredFault(CnsFault):
   volumeId: VolumeId

class CnsFault(VimFault):
   reason: str


class CnsInCompatibleFault(CnsPlacementFault):
   errors: list[MethodFault] = []

class CnsMissingControllerFault(CnsFault):
   pass


class CnsMissingPrivilegeFault(CnsPlacementFault):
   privileges: list[str] = []


class CnsNotRegisteredFault(CnsFault):
   volumeId: VolumeId

class CnsPlacementFault(CnsFault):
   pass

class CnsRankedLowerFault(CnsPlacementFault):
   pass


class CnsSnapshotNotFoundFault(CnsFault):
   volumeId: Optional[VolumeId] = None
   SnapshotId: SnapshotId


class CnsVolumeAlreadyExistsFault(CnsFault):
   volumeId: VolumeId
   datastore: Optional[Datastore] = None


class CnsVolumeNotFoundFault(CnsFault):
   volumeId: VolumeId

class CollectorAddressUnset(DvsFault):
   pass

class ConcurrentAccess(VimFault):
   pass


class ConflictingConfiguration(DvsFault):
   class Config(DynamicData):
      entity: Optional[ManagedEntity] = None
      propertyPath: str

   configInConflict: list[Config] = []


class ConflictingDatastoreFound(RuntimeFault):
   name: str
   url: str


class ConnectedIso(OvfExport):
   cdrom: VirtualCdrom
   filename: str

class CpuCompatibilityUnknown(CpuIncompatible):
   pass

class CpuHotPlugNotSupported(VmConfigFault):
   pass


class CpuIncompatible(VirtualHardwareCompatibilityIssue):
   level: int
   registerName: str
   registerBits: Optional[str] = None
   desiredBits: Optional[str] = None
   host: Optional[HostSystem] = None

class CpuIncompatible1ECX(CpuIncompatible):
   sse3: bool
   pclmulqdq: bool
   ssse3: bool
   sse41: bool
   sse42: bool
   aes: bool
   other: bool
   otherOnly: bool

class CpuIncompatible81EDX(CpuIncompatible):
   nx: bool
   ffxsr: bool
   rdtscp: bool
   lm: bool
   other: bool
   otherOnly: bool

class CustomizationFault(VimFault):
   pass

class CustomizationPending(CustomizationFault):
   pass

class DVPortNotSupported(DeviceBackingNotSupported):
   pass


class DasConfigFault(VimFault):
   class DasConfigFaultReason(Enum):
      HostNetworkMisconfiguration: ClassVar['DasConfigFaultReason'] = 'HostNetworkMisconfiguration'
      HostMisconfiguration: ClassVar['DasConfigFaultReason'] = 'HostMisconfiguration'
      InsufficientPrivileges: ClassVar['DasConfigFaultReason'] = 'InsufficientPrivileges'
      NoPrimaryAgentAvailable: ClassVar['DasConfigFaultReason'] = 'NoPrimaryAgentAvailable'
      Other: ClassVar['DasConfigFaultReason'] = 'Other'
      NoDatastoresConfigured: ClassVar['DasConfigFaultReason'] = 'NoDatastoresConfigured'
      CreateConfigVvolFailed: ClassVar['DasConfigFaultReason'] = 'CreateConfigVvolFailed'
      VSanNotSupportedOnHost: ClassVar['DasConfigFaultReason'] = 'VSanNotSupportedOnHost'
      DasNetworkMisconfiguration: ClassVar['DasConfigFaultReason'] = 'DasNetworkMisconfiguration'
      SetDesiredImageSpecFailed: ClassVar['DasConfigFaultReason'] = 'SetDesiredImageSpecFailed'
      ApplyHAVibsOnClusterFailed: ClassVar['DasConfigFaultReason'] = 'ApplyHAVibsOnClusterFailed'

   reason: Optional[str] = None
   output: Optional[str] = None
   event: list[Event] = []


class DatabaseError(RuntimeFault):
   pass


class DatacenterMismatch(MigrationFault):
   class Argument(DynamicData):
      entity: ManagedEntity
      inputDatacenter: Optional[Datacenter] = None

   invalidArgument: list[Argument] = []
   expectedDatacenter: Datacenter


class DatastoreNotWritableOnHost(InvalidDatastore):
   host: HostSystem


class DeltaDiskFormatNotSupported(VmConfigFault):
   datastore: list[Datastore] = []
   deltaDiskFormat: str

class DestinationSwitchFull(CannotAccessNetwork):
   pass

class DestinationVsanDisabled(CannotMoveVsanEnabledHost):
   destinationCluster: str

class DeviceBackingNotSupported(DeviceNotSupported):
   backing: str

class DeviceControllerNotSupported(DeviceNotSupported):
   controller: str

class DeviceHotPlugNotSupported(InvalidDeviceSpec):
   pass

class DeviceNotFound(InvalidDeviceSpec):
   pass


class DeviceNotSupported(VirtualHardwareCompatibilityIssue):
   class Reason(Enum):
      host: ClassVar['Reason'] = 'host'
      guest: ClassVar['Reason'] = 'guest'
      ft: ClassVar['Reason'] = 'ft'

   device: str
   reason: Optional[str] = None

class DeviceUnsupportedForVmPlatform(InvalidDeviceSpec):
   pass

class DeviceUnsupportedForVmVersion(InvalidDeviceSpec):
   currentVersion: str
   expectedVersion: str

class DigestNotSupported(DeviceNotSupported):
   pass

class DirectoryNotEmpty(FileFault):
   pass

class DisableAdminNotSupported(HostConfigFault):
   pass


class DisallowedChangeByService(RuntimeFault):
   class DisallowedChange(Enum):
      hotExtendDisk: ClassVar['DisallowedChange'] = 'hotExtendDisk'

   serviceName: str
   disallowedChange: Optional[str] = None

class DisallowedDiskModeChange(InvalidDeviceSpec):
   pass


class DisallowedMigrationDeviceAttached(MigrationFault):
   fault: MethodFault


class DisallowedOperationOnFailoverHost(RuntimeFault):
   host: HostSystem
   hostname: str

class DisconnectedHostsBlockingEVC(EVCConfigFault):
   pass

class DiskHasPartitions(VsanDiskFault):
   pass

class DiskIsLastRemainingNonSSD(VsanDiskFault):
   pass

class DiskIsNonLocal(VsanDiskFault):
   pass

class DiskIsUSB(VsanDiskFault):
   pass

class DiskMoveTypeNotSupported(MigrationFault):
   pass

class DiskNotSupported(VirtualHardwareCompatibilityIssue):
   disk: int

class DiskTooSmall(VsanDiskFault):
   pass

class DomainNotFound(ActiveDirectoryFault):
   domainName: str

class DrsDisabledOnVm(VimFault):
   pass


class DrsVmotionIncompatibleFault(VirtualHardwareCompatibilityIssue):
   host: HostSystem

class DuplicateDisks(VsanDiskFault):
   pass


class DuplicateName(VimFault):
   name: str
   object: ManagedObject

class DuplicateVsanNetworkInterface(VsanFault):
   device: str


class DvsApplyOperationFault(DvsFault):
   class FaultOnObject(DynamicData):
      objectId: str
      type: type
      fault: MethodFault

   objectFault: list[FaultOnObject] = []

class DvsFault(VimFault):
   pass


class DvsNotAuthorized(DvsFault):
   sessionExtensionKey: Optional[str] = None
   dvsExtensionKey: Optional[str] = None


class DvsOperationBulkFault(DvsFault):
   class FaultOnHost(DynamicData):
      host: HostSystem
      fault: MethodFault

   hostFault: list[FaultOnHost] = []


class DvsScopeViolated(DvsFault):
   scope: list[ManagedEntity] = []
   entity: ManagedEntity


class EVCAdmissionFailed(NotSupportedHostInCluster):
   faults: list[MethodFault] = []

class EVCAdmissionFailedCPUFeaturesForMode(EVCAdmissionFailed):
   currentEVCModeKey: str

class EVCAdmissionFailedCPUModel(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedCPUModelForMode(EVCAdmissionFailed):
   currentEVCModeKey: str

class EVCAdmissionFailedCPUVendor(EVCAdmissionFailed):
   clusterCPUVendor: str
   hostCPUVendor: str

class EVCAdmissionFailedCPUVendorUnknown(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedHostDisconnected(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedHostSoftware(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedHostSoftwareForMode(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedVmActive(EVCAdmissionFailed):
   pass


class EVCConfigFault(VimFault):
   faults: list[MethodFault] = []

class EVCModeIllegalByVendor(EVCConfigFault):
   clusterCPUVendor: str
   modeCPUVendor: str


class EVCModeUnsupportedByHosts(EVCConfigFault):
   evcMode: Optional[str] = None
   host: list[HostSystem] = []
   hostName: list[str] = []


class EVCUnsupportedByHostHardware(EVCConfigFault):
   host: list[HostSystem] = []
   hostName: list[str] = []


class EVCUnsupportedByHostSoftware(EVCConfigFault):
   host: list[HostSystem] = []
   hostName: list[str] = []

class EightHostLimitViolated(VmConfigFault):
   pass


class EncryptionKeyRequired(InvalidState):
   requiredKey: list[CryptoKeyId] = []

class ExpiredAddonLicense(ExpiredFeatureLicense):
   pass

class ExpiredEditionLicense(ExpiredFeatureLicense):
   pass


class ExpiredFeatureLicense(NotEnoughLicenses):
   feature: str
   count: int
   expirationDate: datetime


class ExtendedFault(VimFault):
   faultTypeId: str
   data: list[KeyValue] = []


class FailToEnableSPBM(NotEnoughLicenses):
   cs: ComputeResource
   csName: str
   hostLicenseStates: list[ComputeResource.HostSPBMLicenseInfo] = []


class FailToLockFaultToleranceVMs(RuntimeFault):
   vmName: str
   vm: VirtualMachine
   alreadyLockedVm: VirtualMachine


class FaultToleranceAntiAffinityViolated(MigrationFault):
   hostName: str
   host: HostSystem


class FaultToleranceCannotEditMem(VmConfigFault):
   vmName: str
   vm: VirtualMachine

class FaultToleranceCpuIncompatible(CpuIncompatible):
   model: bool
   family: bool
   stepping: bool

class FaultToleranceNeedsThickDisk(MigrationFault):
   vmName: str


class FaultToleranceNotLicensed(VmFaultToleranceIssue):
   hostName: Optional[str] = None

class FaultToleranceNotSameBuild(MigrationFault):
   build: str


class FaultTolerancePrimaryPowerOnNotAttempted(VmFaultToleranceIssue):
   secondaryVm: VirtualMachine
   primaryVm: VirtualMachine


class FaultToleranceVmNotDasProtected(VimFault):
   vm: VirtualMachine
   vmName: str

class FcoeFault(VimFault):
   pass

class FcoeFaultPnicHasNoPortSet(FcoeFault):
   nicDevice: str


class FeatureRequirementsNotMet(VirtualHardwareCompatibilityIssue):
   featureRequirement: list[FeatureRequirement] = []
   vm: Optional[VirtualMachine] = None
   host: Optional[HostSystem] = None

class FileAlreadyExists(FileFault):
   pass

class FileBackedPortNotSupported(DeviceNotSupported):
   pass

class FileFault(VimFault):
   file: str

class FileLocked(FileFault):
   pass

class FileNameTooLong(FileFault):
   pass

class FileNotFound(FileFault):
   pass

class FileNotWritable(FileFault):
   pass


class FileTooLarge(FileFault):
   datastore: str
   fileSize: long
   maxFileSize: Optional[long] = None

class FilesystemQuiesceFault(SnapshotFault):
   pass


class FilterInUse(ResourceInUse):
   disk: list[VirtualDiskId] = []


class FtIssuesOnHost(VmFaultToleranceIssue):
   class HostSelectionType(Enum):
      user: ClassVar['HostSelectionType'] = 'user'
      vc: ClassVar['HostSelectionType'] = 'vc'
      drs: ClassVar['HostSelectionType'] = 'drs'

   host: HostSystem
   hostName: str
   errors: list[MethodFault] = []

class FtVmHostRuleViolation(VmConfigFault):
   vmName: str
   hostName: str
   hostGroup: str

class FullStorageVMotionNotSupported(MigrationFeatureNotSupported):
   pass


class GatewayConnectFault(HostConnectFault):
   gatewayType: str
   gatewayId: str
   gatewayInfo: str
   details: Optional[LocalizableMessage] = None

class GatewayHostNotReachable(GatewayToHostConnectFault):
   pass

class GatewayNotFound(GatewayConnectFault):
   pass

class GatewayNotReachable(GatewayConnectFault):
   pass

class GatewayOperationRefused(GatewayConnectFault):
   pass

class GatewayToHostAuthFault(GatewayToHostConnectFault):
   invalidProperties: list[str] = []
   missingProperties: list[str] = []


class GatewayToHostConnectFault(GatewayConnectFault):
   hostname: str
   port: Optional[int] = None


class GatewayToHostTrustVerifyFault(GatewayToHostConnectFault):
   verificationToken: str
   propertiesToVerify: list[KeyValue] = []


class GenericDrsFault(VimFault):
   hostFaults: list[MethodFault] = []

class GenericVmConfigFault(VmConfigFault):
   reason: str


class GuestAuthenticationChallenge(GuestOperationsFault):
   serverChallenge: GuestAuthentication
   sessionID: long

class GuestComponentsOutOfDate(GuestOperationsFault):
   pass

class GuestMultipleMappings(GuestOperationsFault):
   pass

class GuestOperationsFault(VimFault):
   pass

class GuestOperationsUnavailable(GuestOperationsFault):
   pass

class GuestPermissionDenied(GuestOperationsFault):
   pass


class GuestProcessNotFound(GuestOperationsFault):
   pid: long


class GuestRegistryFault(GuestOperationsFault):
   windowsSystemErrorCode: long

class GuestRegistryKeyAlreadyExists(GuestRegistryKeyFault):
   pass

class GuestRegistryKeyFault(GuestRegistryFault):
   keyName: str

class GuestRegistryKeyHasSubkeys(GuestRegistryKeyFault):
   pass

class GuestRegistryKeyInvalid(GuestRegistryKeyFault):
   pass

class GuestRegistryKeyParentVolatile(GuestRegistryKeyFault):
   pass

class GuestRegistryValueFault(GuestRegistryFault):
   keyName: str
   valueName: str

class GuestRegistryValueNotFound(GuestRegistryValueFault):
   pass

class HAErrorsAtDest(MigrationFault):
   pass

class HeterogenousHostsBlockingEVC(EVCConfigFault):
   pass


class HostAccessRestrictedToManagementServer(NotSupported):
   managementServer: str


class HostConfigFailed(HostConfigFault):
   failure: list[MethodFault] = []

class HostConfigFault(VimFault):
   pass

class HostConnectFault(VimFault):
   pass


class HostHasComponentFailure(VimFault):
   class HostComponentType(Enum):
      Datastore: ClassVar['HostComponentType'] = 'Datastore'

   hostName: str
   componentType: str
   componentName: str

class HostInDomain(HostConfigFault):
   pass


class HostIncompatibleForFaultTolerance(VmFaultToleranceIssue):
   class Reason(Enum):
      product: ClassVar['Reason'] = 'product'
      processor: ClassVar['Reason'] = 'processor'

   hostName: Optional[str] = None
   reason: Optional[str] = None


class HostIncompatibleForRecordReplay(VimFault):
   class Reason(Enum):
      product: ClassVar['Reason'] = 'product'
      processor: ClassVar['Reason'] = 'processor'

   hostName: Optional[str] = None
   reason: Optional[str] = None


class HostInventoryFull(NotEnoughLicenses):
   capacity: int

class HostPowerOpFailed(VimFault):
   pass


class HostSpecificationOperationFailed(VimFault):
   host: HostSystem

class HotSnapshotMoveNotSupported(SnapshotCopyNotSupported):
   pass

class HttpFault(VimFault):
   statusCode: int
   statusMessage: str

class IDEDiskNotSupported(DiskNotSupported):
   pass


class IORMNotSupportedHostOnDatastore(VimFault):
   datastore: Datastore
   datastoreName: str
   host: list[HostSystem] = []

class ImportHostAddFailure(DvsFault):
   hostIp: list[str] = []


class ImportOperationBulkFault(DvsFault):
   class FaultOnImport(DynamicData):
      entityType: Optional[str] = None
      key: Optional[str] = None
      fault: MethodFault

   importFaults: list[FaultOnImport] = []


class InUseFeatureManipulationDisallowed(NotEnoughLicenses):
   pass


class InaccessibleDatastore(InvalidDatastore):
   detail: Optional[str] = None

class InaccessibleFTMetadataDatastore(InaccessibleDatastore):
   pass

class InaccessibleVFlashSource(VimFault):
   hostName: str

class IncompatibleDefaultDevice(MigrationFault):
   device: str


class IncompatibleHostForFtSecondary(VmFaultToleranceIssue):
   host: HostSystem
   error: list[MethodFault] = []


class IncompatibleHostForVmReplication(ReplicationFault):
   class IncompatibleReason(Enum):
      rpo: ClassVar['IncompatibleReason'] = 'rpo'
      netCompression: ClassVar['IncompatibleReason'] = 'netCompression'

   vmName: str
   hostName: str
   reason: str


class IncompatibleSetting(InvalidArgument):
   conflictingProperty: PropertyPath

class IncorrectFileType(FileFault):
   pass


class IncorrectHostInformation(NotEnoughLicenses):
   pass

class IndependentDiskVMotionNotSupported(MigrationFeatureNotSupported):
   pass

class InsufficientAgentVmsDeployed(InsufficientResourcesFault):
   hostName: str
   requiredNumAgentVms: int
   currentNumAgentVms: int


class InsufficientCpuResourcesFault(InsufficientResourcesFault):
   unreserved: long
   requested: long

class InsufficientDisks(VsanDiskFault):
   pass

class InsufficientFailoverResourcesFault(InsufficientResourcesFault):
   pass

class InsufficientGraphicsResourcesFault(InsufficientResourcesFault):
   pass


class InsufficientHostCapacityFault(InsufficientResourcesFault):
   host: Optional[HostSystem] = None


class InsufficientHostCpuCapacityFault(InsufficientHostCapacityFault):
   unreserved: long
   requested: long


class InsufficientHostMemoryCapacityFault(InsufficientHostCapacityFault):
   unreserved: long
   requested: long


class InsufficientMemoryResourcesFault(InsufficientResourcesFault):
   unreserved: long
   requested: long

class InsufficientNetworkCapacity(InsufficientResourcesFault):
   pass


class InsufficientNetworkResourcePoolCapacity(InsufficientResourcesFault):
   dvsName: str
   dvsUuid: str
   resourcePoolKey: str
   available: long
   requested: long
   device: list[str] = []

class InsufficientPerCpuCapacity(InsufficientHostCapacityFault):
   pass

class InsufficientResourcesFault(VimFault):
   pass


class InsufficientStandbyCpuResource(InsufficientStandbyResource):
   available: long
   requested: long


class InsufficientStandbyMemoryResource(InsufficientStandbyResource):
   available: long
   requested: long

class InsufficientStandbyResource(InsufficientResourcesFault):
   pass


class InsufficientStorageIops(VimFault):
   unreservedIops: long
   requestedIops: long
   datastoreName: str

class InsufficientStorageSpace(InsufficientResourcesFault):
   pass


class InsufficientVFlashResourcesFault(InsufficientResourcesFault):
   freeSpaceInMB: Optional[long] = None
   freeSpace: long
   requestedSpaceInMB: Optional[long] = None
   requestedSpace: long

class InvalidAffinitySettingFault(VimFault):
   pass

class InvalidBmcRole(VimFault):
   pass

class InvalidBundle(PlatformConfigFault):
   pass

class InvalidCAMCertificate(InvalidCAMServer):
   pass

class InvalidCAMServer(ActiveDirectoryFault):
   camServer: str

class InvalidClientCertificate(InvalidLogin):
   pass

class InvalidController(InvalidDeviceSpec):
   controllerKey: int


class InvalidDasConfigArgument(InvalidArgument):
   class EntryForInvalidArgument(Enum):
      admissionControl: ClassVar['EntryForInvalidArgument'] = 'admissionControl'
      userHeartbeatDs: ClassVar['EntryForInvalidArgument'] = 'userHeartbeatDs'
      vmConfig: ClassVar['EntryForInvalidArgument'] = 'vmConfig'

   entry: Optional[str] = None
   clusterName: Optional[str] = None


class InvalidDasRestartPriorityForFtVm(InvalidArgument):
   vm: VirtualMachine
   vmName: str


class InvalidDatastore(VimFault):
   datastore: Optional[Datastore] = None
   name: Optional[str] = None

class InvalidDatastorePath(InvalidDatastore):
   datastorePath: str


class InvalidDatastoreState(InvalidState):
   datastoreName: Optional[str] = None

class InvalidDeviceBacking(InvalidDeviceSpec):
   pass


class InvalidDeviceOperation(InvalidDeviceSpec):
   badOp: Optional[VirtualDeviceSpec.Operation] = None
   badFileOp: Optional[VirtualDeviceSpec.FileOperation] = None

class InvalidDeviceSpec(InvalidVmConfig):
   deviceIndex: int

class InvalidDiskFormat(InvalidFormat):
   pass


class InvalidDrsBehaviorForFtVm(InvalidArgument):
   vm: VirtualMachine
   vmName: str


class InvalidEditionLicense(NotEnoughLicenses):
   feature: str

class InvalidEvent(VimFault):
   pass


class InvalidFolder(VimFault):
   target: ManagedEntity

class InvalidFormat(VmConfigFault):
   pass

class InvalidGuestLogin(GuestOperationsFault):
   pass

class InvalidHostConnectionState(InvalidHostState):
   pass

class InvalidHostName(HostConfigFault):
   pass


class InvalidHostState(InvalidState):
   host: Optional[HostSystem] = None


class InvalidIndexArgument(InvalidArgument):
   key: str


class InvalidIpfixConfig(DvsFault):
   property: Optional[PropertyPath] = None

class InvalidIpmiLoginInfo(VimFault):
   pass

class InvalidIpmiMacAddress(VimFault):
   userProvidedMacAddress: str
   observedMacAddress: str

class InvalidLicense(VimFault):
   licenseContent: str

class InvalidLocale(VimFault):
   pass

class InvalidLogin(VimFault):
   pass


class InvalidName(VimFault):
   name: str
   entity: Optional[ManagedEntity] = None

class InvalidNasCredentials(NasConfigFault):
   userName: str

class InvalidNetworkInType(VAppPropertyFault):
   pass

class InvalidNetworkResource(NasConfigFault):
   remoteHost: str
   remotePath: str

class InvalidOperationOnSecondaryVm(VmFaultToleranceIssue):
   instanceUuid: str


class InvalidPowerState(InvalidState):
   requestedState: Optional[VirtualMachine.PowerState] = None
   existingState: VirtualMachine.PowerState

class InvalidPrivilege(VimFault):
   privilege: str


class InvalidProfileReferenceHost(RuntimeFault):
   class Reason(Enum):
      incompatibleVersion: ClassVar['Reason'] = 'incompatibleVersion'
      missingReferenceHost: ClassVar['Reason'] = 'missingReferenceHost'

   reason: Optional[str] = None
   host: Optional[HostSystem] = None
   profile: Optional[Profile] = None
   profileName: Optional[str] = None

class InvalidPropertyType(VAppPropertyFault):
   pass

class InvalidPropertyValue(VAppPropertyFault):
   pass

class InvalidResourcePoolStructureFault(InsufficientResourcesFault):
   pass


class InvalidScheduledTask(RuntimeFault):
   pass

class InvalidSnapshotFormat(InvalidFormat):
   pass

class InvalidState(VimFault):
   pass


class InvalidVmConfig(VmConfigFault):
   property: Optional[PropertyPath] = None


class InvalidVmState(InvalidState):
   vm: VirtualMachine


class InventoryHasStandardAloneHosts(NotEnoughLicenses):
   hosts: list[str] = []

class IpHostnameGeneratorError(CustomizationFault):
   pass

class IscsiFault(VimFault):
   pass

class IscsiFaultInvalidVnic(IscsiFault):
   vnicDevice: str

class IscsiFaultPnicInUse(IscsiFault):
   pnicDevice: str

class IscsiFaultVnicAlreadyBound(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasActivePaths(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasMultipleUplinks(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasNoUplinks(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasWrongUplink(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicInUse(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicIsLastPath(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicNotBound(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicNotFound(IscsiFault):
   vnicDevice: str

class KeyNotFound(VimFault):
   key: str

class LargeRDMConversionNotSupported(MigrationFault):
   device: str


class LargeRDMNotSupportedOnDatastore(VmConfigFault):
   device: str
   datastore: Datastore
   datastoreName: str

class LegacyNetworkInterfaceInUse(CannotAccessNetwork):
   pass


class LicenseAssignmentFailed(RuntimeFault):
   class Reason(Enum):
      keyEntityMismatch: ClassVar['Reason'] = 'keyEntityMismatch'
      downgradeDisallowed: ClassVar['Reason'] = 'downgradeDisallowed'
      inventoryNotManageableByVirtualCenter: ClassVar['Reason'] = 'inventoryNotManageableByVirtualCenter'
      hostsUnmanageableByVirtualCenterWithoutLicenseServer: ClassVar['Reason'] = 'hostsUnmanageableByVirtualCenterWithoutLicenseServer'

   reason: Optional[str] = None


class LicenseDowngradeDisallowed(NotEnoughLicenses):
   edition: str
   entityId: str
   features: list[KeyAnyValue] = []

class LicenseEntityNotFound(VimFault):
   entityId: str


class LicenseExpired(NotEnoughLicenses):
   licenseKey: str


class LicenseKeyEntityMismatch(NotEnoughLicenses):
   pass


class LicenseRestricted(NotEnoughLicenses):
   pass

class LicenseServerUnavailable(VimFault):
   licenseServer: str


class LicenseSourceUnavailable(NotEnoughLicenses):
   licenseSource: LicenseManager.LicenseSource


class LimitExceeded(VimFault):
   property: Optional[PropertyPath] = None
   limit: Optional[int] = None

class LinuxVolumeNotClean(CustomizationFault):
   pass

class LogBundlingFailed(VimFault):
   pass

class MaintenanceModeFileMove(MigrationFault):
   pass

class MemoryFileFormatNotSupportedByDatastore(UnsupportedDatastore):
   datastoreName: str
   type: str

class MemoryHotPlugNotSupported(VmConfigFault):
   pass

class MemorySizeNotRecommended(VirtualHardwareCompatibilityIssue):
   memorySizeMB: int
   minMemorySizeMB: int
   maxMemorySizeMB: int

class MemorySizeNotSupported(VirtualHardwareCompatibilityIssue):
   memorySizeMB: int
   minMemorySizeMB: int
   maxMemorySizeMB: int


class MemorySizeNotSupportedByDatastore(VirtualHardwareCompatibilityIssue):
   datastore: Datastore
   memorySizeMB: int
   maxMemorySizeMB: int

class MemorySnapshotOnIndependentDisk(SnapshotFault):
   pass


class MethodAlreadyDisabledFault(RuntimeFault):
   sourceId: str


class MethodDisabled(RuntimeFault):
   source: Optional[str] = None

class MigrationDisabled(MigrationFault):
   pass

class MigrationFault(VimFault):
   pass


class MigrationFeatureNotSupported(MigrationFault):
   atSourceHost: bool
   failedHostName: str
   failedHost: HostSystem

class MigrationNotReady(MigrationFault):
   reason: str

class MismatchedBundle(VimFault):
   bundleUuid: str
   hostUuid: str
   bundleBuildNumber: int
   hostBuildNumber: int

class MismatchedNetworkPolicies(MigrationFault):
   device: str
   backing: str
   connected: bool

class MismatchedVMotionNetworkNames(MigrationFault):
   sourceNetwork: str
   destNetwork: str

class MissingBmcSupport(VimFault):
   pass

class MissingController(InvalidDeviceSpec):
   pass

class MissingIpPool(VAppPropertyFault):
   pass

class MissingLinuxCustResources(CustomizationFault):
   pass

class MissingNetworkIpConfig(VAppPropertyFault):
   pass

class MissingPowerOffConfiguration(VAppConfigFault):
   pass

class MissingPowerOnConfiguration(VAppConfigFault):
   pass

class MissingWindowsCustResources(CustomizationFault):
   pass

class MksConnectionLimitReached(InvalidState):
   connectionLimit: int


class MountError(CustomizationFault):
   vm: VirtualMachine
   diskIndex: int

class MultiWriterNotSupported(DeviceNotSupported):
   pass


class MultipleCertificatesVerifyFault(HostConnectFault):
   class ThumbprintData(DynamicData):
      port: int
      thumbprint: str

   thumbprintData: list[ThumbprintData] = []

class MultipleSnapshotsNotSupported(SnapshotFault):
   pass


class NamespaceFull(VimFault):
   name: str
   currentMaxSize: long
   requiredSize: Optional[long] = None


class NamespaceLimitReached(VimFault):
   limit: Optional[int] = None

class NamespaceWriteProtected(VimFault):
   name: str

class NasConfigFault(HostConfigFault):
   name: str

class NasConnectionLimitReached(NasConfigFault):
   remoteHost: str
   remotePath: str

class NasSessionCredentialConflict(NasConfigFault):
   remoteHost: str
   remotePath: str
   userName: str

class NasVolumeNotMounted(NasConfigFault):
   remoteHost: str
   remotePath: str

class NetworkCopyFault(FileFault):
   pass

class NetworkDisruptedAndConfigRolledBack(VimFault):
   host: str

class NetworkInaccessible(NasConfigFault):
   pass


class NetworksMayNotBeTheSame(MigrationFault):
   name: Optional[str] = None

class NicSettingMismatch(CustomizationFault):
   numberOfNicsInSpec: int
   numberOfNicsInVM: int


class NoActiveHostInCluster(InvalidState):
   computeResource: ComputeResource


class NoAvailableIp(VAppPropertyFault):
   network: Network

class NoClientCertificate(VimFault):
   pass

class NoCompatibleDatastore(VimFault):
   pass

class NoCompatibleHardAffinityHost(VmConfigFault):
   vmName: str


class NoCompatibleHost(VimFault):
   host: list[HostSystem] = []
   error: list[MethodFault] = []

class NoCompatibleHostWithAccessToDevice(NoCompatibleHost):
   pass

class NoCompatibleSoftAffinityHost(VmConfigFault):
   vmName: str

class NoConnectedDatastore(VimFault):
   pass

class NoDiskFound(VimFault):
   pass

class NoDiskSpace(FileFault):
   datastore: str

class NoDisksToCustomize(CustomizationFault):
   pass

class NoGateway(HostConfigFault):
   pass

class NoGuestHeartbeat(MigrationFault):
   pass


class NoHost(HostConnectFault):
   name: Optional[str] = None


class NoHostSuitableForFtSecondary(VmFaultToleranceIssue):
   vm: VirtualMachine
   vmName: str


class NoLicenseServerConfigured(NotEnoughLicenses):
   pass

class NoPeerHostFound(HostPowerOpFailed):
   pass


class NoPermission(SecurityError):
   class EntityPrivileges(DynamicData):
      entity: ManagedObject
      privilegeIds: list[str] = []

   object: Optional[ManagedObject] = None
   privilegeId: Optional[str] = None
   missingPrivileges: list[EntityPrivileges] = []

class NoPermissionOnAD(ActiveDirectoryFault):
   pass

class NoPermissionOnHost(HostConnectFault):
   pass


class NoPermissionOnNasVolume(NasConfigFault):
   userName: Optional[str] = None

class NoSubjectName(VimFault):
   pass

class NoVcManagedIpConfigured(VAppPropertyFault):
   pass

class NoVirtualNic(HostConfigFault):
   pass

class NoVmInVApp(VAppConfigFault):
   pass

class NonADUserRequired(ActiveDirectoryFault):
   pass

class NonHomeRDMVMotionNotSupported(MigrationFeatureNotSupported):
   device: str

class NonPersistentDisksNotSupported(DeviceNotSupported):
   pass

class NonVmwareOuiMacNotSupportedHost(NotSupportedHost):
   hostName: str

class NotADirectory(FileFault):
   pass

class NotAFile(FileFault):
   pass

class NotAuthenticated(NoPermission):
   pass

class NotEnoughCpus(VirtualHardwareCompatibilityIssue):
   numCpuDest: int
   numCpuVm: int


class NotEnoughLogicalCpus(NotEnoughCpus):
   host: Optional[HostSystem] = None

class NotFound(VimFault):
   pass


class NotSupportedDeviceForFT(VmFaultToleranceIssue):
   class DeviceType(Enum):
      virtualVmxnet3: ClassVar['DeviceType'] = 'virtualVmxnet3'
      paraVirtualSCSIController: ClassVar['DeviceType'] = 'paraVirtualSCSIController'

   host: HostSystem
   hostName: Optional[str] = None
   vm: VirtualMachine
   vmName: Optional[str] = None
   deviceType: str
   deviceLabel: Optional[str] = None


class NotSupportedHost(HostConnectFault):
   productName: Optional[str] = None
   productVersion: Optional[str] = None

class NotSupportedHostForChecksum(VimFault):
   pass

class NotSupportedHostForVFlash(NotSupportedHost):
   hostName: str

class NotSupportedHostForVmcp(NotSupportedHost):
   hostName: str

class NotSupportedHostForVmemFile(NotSupportedHost):
   hostName: str

class NotSupportedHostForVsan(NotSupportedHost):
   hostName: str

class NotSupportedHostInCluster(NotSupportedHost):
   pass


class NotSupportedHostInDvs(NotSupportedHost):
   switchProductSpec: ProductSpec

class NotSupportedHostInHACluster(NotSupportedHost):
   hostName: str
   build: str

class NotUserConfigurableProperty(VAppPropertyFault):
   pass

class NumVirtualCoresPerSocketNotSupported(VirtualHardwareCompatibilityIssue):
   maxSupportedCoresPerSocketDest: int
   numCoresPerSocketVm: int

class NumVirtualCpusExceedsLimit(InsufficientResourcesFault):
   maxSupportedVcpus: int


class NumVirtualCpusIncompatible(VmConfigFault):
   class Reason(Enum):
      recordReplay: ClassVar['Reason'] = 'recordReplay'
      faultTolerance: ClassVar['Reason'] = 'faultTolerance'

   reason: str
   numCpu: int

class NumVirtualCpusNotSupported(VirtualHardwareCompatibilityIssue):
   maxSupportedVcpusDest: int
   numCpuVm: int

class OperationDisabledByGuest(GuestOperationsFault):
   pass


class OperationDisallowedOnHost(RuntimeFault):
   pass

class OperationNotSupportedByGuest(GuestOperationsFault):
   pass


class OutOfBounds(VimFault):
   argumentName: PropertyPath

class OvfAttribute(OvfInvalidPackage):
   elementName: str
   attributeName: str

class OvfConnectedDevice(OvfHardwareExport):
   pass

class OvfConnectedDeviceFloppy(OvfConnectedDevice):
   filename: str

class OvfConnectedDeviceIso(OvfConnectedDevice):
   filename: str

class OvfConstraint(OvfInvalidPackage):
   name: str

class OvfConsumerCallbackFault(OvfFault):
   extensionKey: str
   extensionName: str

class OvfConsumerCommunicationError(OvfConsumerCallbackFault):
   description: str


class OvfConsumerFault(OvfConsumerCallbackFault):
   errorKey: str
   message: str
   params: list[KeyValue] = []

class OvfConsumerInvalidSection(OvfConsumerCallbackFault):
   lineNumber: int
   description: str

class OvfConsumerPowerOnFault(InvalidState):
   extensionKey: str
   extensionName: str
   description: str

class OvfConsumerUndeclaredSection(OvfConsumerCallbackFault):
   qualifiedSectionType: str

class OvfConsumerUndefinedPrefix(OvfConsumerCallbackFault):
   prefix: str

class OvfConsumerValidationFault(VmConfigFault):
   extensionKey: str
   extensionName: str
   message: str

class OvfCpuCompatibility(OvfImport):
   registerName: str
   level: int
   registerValue: str
   desiredRegisterValue: str

class OvfCpuCompatibilityCheckNotSupported(OvfImport):
   pass

class OvfDiskMappingNotFound(OvfSystemFault):
   diskName: str
   vmName: str

class OvfDiskOrderConstraint(OvfConstraint):
   pass

class OvfDuplicateElement(OvfElement):
   pass

class OvfDuplicatedElementBoundary(OvfElement):
   boundary: str

class OvfDuplicatedPropertyIdExport(OvfExport):
   fqid: str

class OvfDuplicatedPropertyIdImport(OvfExport):
   pass

class OvfElement(OvfInvalidPackage):
   name: str

class OvfElementInvalidValue(OvfElement):
   value: str

class OvfExport(OvfFault):
   pass

class OvfExportFailed(OvfExport):
   pass

class OvfFault(VimFault):
   pass

class OvfHardwareCheck(OvfImport):
   pass


class OvfHardwareExport(OvfExport):
   device: Optional[VirtualDevice] = None
   vmPath: str

class OvfHostResourceConstraint(OvfConstraint):
   value: str

class OvfHostValueNotParsed(OvfSystemFault):
   property: str
   value: str

class OvfImport(OvfFault):
   pass

class OvfImportFailed(OvfImport):
   pass

class OvfInternalError(OvfSystemFault):
   pass

class OvfInvalidPackage(OvfFault):
   lineNumber: int

class OvfInvalidValue(OvfAttribute):
   value: str

class OvfInvalidValueConfiguration(OvfInvalidValue):
   pass

class OvfInvalidValueEmpty(OvfInvalidValue):
   pass

class OvfInvalidValueFormatMalformed(OvfInvalidValue):
   pass

class OvfInvalidValueReference(OvfInvalidValue):
   pass

class OvfInvalidVmName(OvfUnsupportedPackage):
   name: str

class OvfMappedOsId(OvfImport):
   ovfId: int
   ovfDescription: str
   targetDescription: str

class OvfMissingAttribute(OvfAttribute):
   pass

class OvfMissingElement(OvfElement):
   pass

class OvfMissingElementNormalBoundary(OvfMissingElement):
   boundary: str

class OvfMissingHardware(OvfImport):
   name: str
   resourceType: int

class OvfNetworkMappingNotSupported(OvfImport):
   pass

class OvfNoHostNic(OvfUnsupportedPackage):
   pass

class OvfNoSpaceOnController(OvfUnsupportedElement):
   parent: str

class OvfNoSupportedHardwareFamily(OvfUnsupportedPackage):
   version: str

class OvfProperty(OvfInvalidPackage):
   type: str
   value: str

class OvfPropertyExport(OvfExport):
   type: str
   value: str

class OvfPropertyNetwork(OvfProperty):
   pass

class OvfPropertyNetworkExport(OvfExport):
   network: str

class OvfPropertyQualifier(OvfProperty):
   qualifier: str

class OvfPropertyQualifierDuplicate(OvfProperty):
   qualifier: str

class OvfPropertyQualifierIgnored(OvfProperty):
   qualifier: str

class OvfPropertyType(OvfProperty):
   pass

class OvfPropertyValue(OvfProperty):
   pass

class OvfSystemFault(OvfFault):
   pass


class OvfToXmlUnsupportedElement(OvfSystemFault):
   name: Optional[str] = None

class OvfUnableToExportDisk(OvfHardwareExport):
   diskName: str

class OvfUnexpectedElement(OvfElement):
   pass


class OvfUnknownDevice(OvfSystemFault):
   device: Optional[VirtualDevice] = None
   vmName: str


class OvfUnknownDeviceBacking(OvfHardwareExport):
   backing: VirtualDevice.BackingInfo

class OvfUnknownEntity(OvfSystemFault):
   lineNumber: int

class OvfUnsupportedAttribute(OvfUnsupportedPackage):
   elementName: str
   attributeName: str

class OvfUnsupportedAttributeValue(OvfUnsupportedAttribute):
   value: str


class OvfUnsupportedDeviceBackingInfo(OvfSystemFault):
   elementName: Optional[str] = None
   instanceId: Optional[str] = None
   deviceName: str
   backingName: Optional[str] = None


class OvfUnsupportedDeviceBackingOption(OvfSystemFault):
   elementName: Optional[str] = None
   instanceId: Optional[str] = None
   deviceName: str
   backingName: Optional[str] = None

class OvfUnsupportedDeviceExport(OvfHardwareExport):
   pass

class OvfUnsupportedDiskProvisioning(OvfImport):
   diskProvisioning: str
   supportedDiskProvisioning: str

class OvfUnsupportedElement(OvfUnsupportedPackage):
   name: str

class OvfUnsupportedElementValue(OvfUnsupportedElement):
   value: str


class OvfUnsupportedPackage(OvfFault):
   lineNumber: Optional[int] = None

class OvfUnsupportedSection(OvfUnsupportedElement):
   info: str

class OvfUnsupportedSubType(OvfUnsupportedPackage):
   elementName: str
   instanceId: str
   deviceType: int
   deviceSubType: str

class OvfUnsupportedType(OvfUnsupportedPackage):
   name: str
   instanceId: str
   deviceType: int

class OvfWrongElement(OvfElement):
   pass

class OvfWrongNamespace(OvfInvalidPackage):
   namespaceName: str

class OvfXmlFormat(OvfInvalidPackage):
   description: str

class PasswordExpired(InvalidLogin):
   pass

class PatchAlreadyInstalled(PatchNotApplicable):
   pass


class PatchBinariesNotFound(VimFault):
   patchID: str
   binary: list[str] = []

class PatchInstallFailed(PlatformConfigFault):
   rolledBack: bool

class PatchIntegrityError(PlatformConfigFault):
   pass

class PatchMetadataCorrupted(PatchMetadataInvalid):
   pass


class PatchMetadataInvalid(VimFault):
   patchID: str
   metaData: list[str] = []

class PatchMetadataNotFound(PatchMetadataInvalid):
   pass


class PatchMissingDependencies(PatchNotApplicable):
   prerequisitePatch: list[str] = []
   prerequisiteLib: list[str] = []

class PatchNotApplicable(VimFault):
   patchID: str


class PatchSuperseded(PatchNotApplicable):
   supersede: list[str] = []

class PhysCompatRDMNotSupported(RDMNotSupported):
   pass

class PlatformConfigFault(HostConfigFault):
   text: str


class PowerOnFtSecondaryFailed(VmFaultToleranceIssue):
   vm: VirtualMachine
   vmName: str
   hostSelectionBy: FtIssuesOnHost.HostSelectionType
   hostErrors: list[MethodFault] = []
   rootCause: MethodFault


class PowerOnFtSecondaryTimedout(Timedout):
   vm: VirtualMachine
   vmName: str
   timeout: int


class ProfileUpdateFailed(VimFault):
   class UpdateFailure(DynamicData):
      profilePath: ProfilePropertyPath
      errMsg: LocalizableMessage

   failure: list[UpdateFailure] = []
   warnings: list[UpdateFailure] = []


class QuarantineModeFault(VmConfigFault):
   class FaultType(Enum):
      NoCompatibleNonQuarantinedHost: ClassVar['FaultType'] = 'NoCompatibleNonQuarantinedHost'
      CorrectionDisallowed: ClassVar['FaultType'] = 'CorrectionDisallowed'
      CorrectionImpact: ClassVar['FaultType'] = 'CorrectionImpact'

   vmName: str
   faultType: str

class QuestionPending(InvalidState):
   text: str


class QuiesceDatastoreIOForHAFailed(ResourceInUse):
   host: HostSystem
   hostName: str
   ds: Datastore
   dsName: str

class RDMConversionNotSupported(MigrationFault):
   device: str

class RDMNotPreserved(MigrationFault):
   device: str

class RDMNotSupported(DeviceNotSupported):
   pass


class RDMNotSupportedOnDatastore(VmConfigFault):
   device: str
   datastore: Datastore
   datastoreName: str

class RDMPointsToInaccessibleDisk(CannotAccessVmDisk):
   pass

class RawDiskNotSupported(DeviceNotSupported):
   pass

class ReadHostResourcePoolTreeFailed(HostConnectFault):
   pass

class ReadOnlyDisksWithLegacyDestination(MigrationFault):
   roDiskCount: int
   timeoutDanger: bool


class RebootRequired(VimFault):
   patch: Optional[str] = None

class RecordReplayDisabled(VimFault):
   pass

class RemoteDeviceNotSupported(DeviceNotSupported):
   pass

class RemoveFailed(VimFault):
   pass

class ReplicationConfigFault(ReplicationFault):
   pass


class ReplicationDiskConfigFault(ReplicationConfigFault):
   class ReasonForFault(Enum):
      diskNotFound: ClassVar['ReasonForFault'] = 'diskNotFound'
      diskTypeNotSupported: ClassVar['ReasonForFault'] = 'diskTypeNotSupported'
      invalidDiskKey: ClassVar['ReasonForFault'] = 'invalidDiskKey'
      invalidDiskReplicationId: ClassVar['ReasonForFault'] = 'invalidDiskReplicationId'
      duplicateDiskReplicationId: ClassVar['ReasonForFault'] = 'duplicateDiskReplicationId'
      invalidPersistentFilePath: ClassVar['ReasonForFault'] = 'invalidPersistentFilePath'
      reconfigureDiskReplicationIdNotAllowed: ClassVar['ReasonForFault'] = 'reconfigureDiskReplicationIdNotAllowed'

   reason: Optional[str] = None
   vmRef: Optional[VirtualMachine] = None
   key: Optional[int] = None

class ReplicationFault(VimFault):
   pass

class ReplicationIncompatibleWithFT(ReplicationFault):
   pass


class ReplicationInvalidOptions(ReplicationFault):
   options: str
   entity: Optional[ManagedEntity] = None

class ReplicationNotSupportedOnHost(ReplicationFault):
   pass


class ReplicationVmConfigFault(ReplicationConfigFault):
   class ReasonForFault(Enum):
      incompatibleHwVersion: ClassVar['ReasonForFault'] = 'incompatibleHwVersion'
      invalidVmReplicationId: ClassVar['ReasonForFault'] = 'invalidVmReplicationId'
      invalidGenerationNumber: ClassVar['ReasonForFault'] = 'invalidGenerationNumber'
      outOfBoundsRpoValue: ClassVar['ReasonForFault'] = 'outOfBoundsRpoValue'
      invalidDestinationIpAddress: ClassVar['ReasonForFault'] = 'invalidDestinationIpAddress'
      invalidDestinationPort: ClassVar['ReasonForFault'] = 'invalidDestinationPort'
      invalidExtraVmOptions: ClassVar['ReasonForFault'] = 'invalidExtraVmOptions'
      staleGenerationNumber: ClassVar['ReasonForFault'] = 'staleGenerationNumber'
      reconfigureVmReplicationIdNotAllowed: ClassVar['ReasonForFault'] = 'reconfigureVmReplicationIdNotAllowed'
      cannotRetrieveVmReplicationConfiguration: ClassVar['ReasonForFault'] = 'cannotRetrieveVmReplicationConfiguration'
      replicationAlreadyEnabled: ClassVar['ReasonForFault'] = 'replicationAlreadyEnabled'
      invalidPriorConfiguration: ClassVar['ReasonForFault'] = 'invalidPriorConfiguration'
      replicationNotEnabled: ClassVar['ReasonForFault'] = 'replicationNotEnabled'
      replicationConfigurationFailed: ClassVar['ReasonForFault'] = 'replicationConfigurationFailed'
      encryptedVm: ClassVar['ReasonForFault'] = 'encryptedVm'
      invalidThumbprint: ClassVar['ReasonForFault'] = 'invalidThumbprint'
      incompatibleDevice: ClassVar['ReasonForFault'] = 'incompatibleDevice'

   reason: Optional[str] = None
   vmRef: Optional[VirtualMachine] = None


class ReplicationVmFault(ReplicationFault):
   class ReasonForFault(Enum):
      notConfigured: ClassVar['ReasonForFault'] = 'notConfigured'
      poweredOff: ClassVar['ReasonForFault'] = 'poweredOff'
      suspended: ClassVar['ReasonForFault'] = 'suspended'
      poweredOn: ClassVar['ReasonForFault'] = 'poweredOn'
      offlineReplicating: ClassVar['ReasonForFault'] = 'offlineReplicating'
      invalidState: ClassVar['ReasonForFault'] = 'invalidState'
      invalidInstanceId: ClassVar['ReasonForFault'] = 'invalidInstanceId'
      closeDiskError: ClassVar['ReasonForFault'] = 'closeDiskError'
      groupExist: ClassVar['ReasonForFault'] = 'groupExist'

   reason: str
   state: Optional[str] = None
   instanceId: Optional[str] = None
   vm: VirtualMachine


class ReplicationVmInProgressFault(ReplicationVmFault):
   class Activity(Enum):
      fullSync: ClassVar['Activity'] = 'fullSync'
      delta: ClassVar['Activity'] = 'delta'

   requestedActivity: str
   inProgressActivity: str


class ResourceInUse(VimFault):
   type: Optional[type] = None
   name: Optional[str] = None


class ResourceNotAvailable(VimFault):
   containerType: Optional[type] = None
   containerName: Optional[str] = None
   type: Optional[type] = None


class RestrictedByAdministrator(RuntimeFault):
   details: str


class RestrictedVersion(SecurityError):
   pass

class RollbackFailure(DvsFault):
   entityName: str
   entityType: str


class RuleViolation(VmConfigFault):
   host: Optional[HostSystem] = None
   rule: RuleInfo

class SSLDisabledFault(HostConnectFault):
   pass


class SSLVerifyFault(HostConnectFault):
   selfSigned: bool
   thumbprint: Optional[str] = None
   certificate: Optional[str] = None

class SSPIChallenge(VimFault):
   base64Token: str

class SecondaryVmAlreadyDisabled(VmFaultToleranceIssue):
   instanceUuid: str

class SecondaryVmAlreadyEnabled(VmFaultToleranceIssue):
   instanceUuid: str

class SecondaryVmAlreadyRegistered(VmFaultToleranceIssue):
   instanceUuid: str

class SecondaryVmNotRegistered(VmFaultToleranceIssue):
   instanceUuid: str

class SharedBusControllerNotSupported(DeviceNotSupported):
   pass


class ShrinkDiskFault(VimFault):
   diskId: Optional[int] = None

class SnapshotCloneNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotCopyNotSupported(MigrationFault):
   pass

class SnapshotDisabled(SnapshotFault):
   pass

class SnapshotFault(VimFault):
   pass


class SnapshotIncompatibleDeviceInVm(SnapshotFault):
   fault: MethodFault

class SnapshotLocked(SnapshotFault):
   pass

class SnapshotMoveFromNonHomeNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotMoveNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotMoveToNonHomeNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotNoChange(SnapshotFault):
   pass


class SnapshotRevertIssue(MigrationFault):
   snapshotName: Optional[str] = None
   event: list[Event] = []
   errors: bool

class SoftRuleVioCorrectionDisallowed(VmConfigFault):
   vmName: str

class SoftRuleVioCorrectionImpact(VmConfigFault):
   vmName: str


class SolutionUserRequired(SecurityError):
   pass

class SsdDiskNotAvailable(VimFault):
   devicePath: str

class StorageDrsCannotMoveDiskInMultiWriterMode(VimFault):
   pass

class StorageDrsCannotMoveFTVm(VimFault):
   pass

class StorageDrsCannotMoveIndependentDisk(VimFault):
   pass

class StorageDrsCannotMoveManuallyPlacedSwapFile(VimFault):
   pass

class StorageDrsCannotMoveManuallyPlacedVm(VimFault):
   pass

class StorageDrsCannotMoveSharedDisk(VimFault):
   pass

class StorageDrsCannotMoveTemplate(VimFault):
   pass

class StorageDrsCannotMoveVmInUserFolder(VimFault):
   pass

class StorageDrsCannotMoveVmWithMountedCDROM(VimFault):
   pass

class StorageDrsCannotMoveVmWithNoFilesInLayout(VimFault):
   pass

class StorageDrsDatacentersCannotShareDatastore(VimFault):
   pass

class StorageDrsDisabledOnVm(VimFault):
   pass

class StorageDrsHbrDiskNotMovable(VimFault):
   nonMovableDiskIds: str

class StorageDrsHmsMoveInProgress(VimFault):
   pass

class StorageDrsHmsUnreachable(VimFault):
   pass

class StorageDrsIolbDisabledInternally(VimFault):
   pass

class StorageDrsRelocateDisabled(VimFault):
   pass

class StorageDrsStaleHmsCollection(VimFault):
   pass

class StorageDrsUnableToMoveFiles(VimFault):
   pass

class StorageVMotionNotSupported(MigrationFeatureNotSupported):
   pass


class StorageVmotionIncompatible(VirtualHardwareCompatibilityIssue):
   datastore: Optional[Datastore] = None

class SuspendedRelocateNotSupported(MigrationFault):
   pass

class SwapDatastoreNotWritableOnHost(DatastoreNotWritableOnHost):
   pass

class SwapDatastoreUnset(VimFault):
   pass

class SwapPlacementOverrideNotSupported(InvalidVmConfig):
   pass

class SwitchIpUnset(DvsFault):
   pass

class SwitchNotInUpgradeMode(DvsFault):
   pass


class TaskInProgress(VimFault):
   task: Task


class ThirdPartyLicenseAssignmentFailed(RuntimeFault):
   class Reason(Enum):
      licenseAssignmentFailed: ClassVar['Reason'] = 'licenseAssignmentFailed'
      moduleNotInstalled: ClassVar['Reason'] = 'moduleNotInstalled'

   host: HostSystem
   module: str
   reason: Optional[str] = None

class Timedout(VimFault):
   pass

class TooManyConcurrentNativeClones(FileFault):
   pass

class TooManyConsecutiveOverrides(VimFault):
   pass

class TooManyDevices(InvalidVmConfig):
   pass

class TooManyDisksOnLegacyHost(MigrationFault):
   diskCount: int
   timeoutDanger: bool

class TooManyGuestLogons(GuestOperationsFault):
   pass

class TooManyHosts(HostConnectFault):
   pass

class TooManyNativeCloneLevels(FileFault):
   pass

class TooManyNativeClonesOnFile(FileFault):
   pass

class TooManySnapshotLevels(SnapshotFault):
   pass

class ToolsAlreadyUpgraded(VmToolsUpgradeFault):
   pass

class ToolsAutoUpgradeNotSupported(VmToolsUpgradeFault):
   pass

class ToolsImageCopyFailed(VmToolsUpgradeFault):
   pass

class ToolsImageNotAvailable(VmToolsUpgradeFault):
   pass

class ToolsImageSignatureCheckFailed(VmToolsUpgradeFault):
   pass

class ToolsInstallationInProgress(MigrationFault):
   pass

class ToolsUnavailable(VimFault):
   pass

class ToolsUpgradeCancelled(VmToolsUpgradeFault):
   pass

class UnSupportedDatastoreForVFlash(UnsupportedDatastore):
   datastoreName: str
   type: str

class UncommittedUndoableDisk(MigrationFault):
   pass

class UnconfiguredPropertyValue(InvalidPropertyValue):
   pass

class UncustomizableGuest(CustomizationFault):
   uncustomizableGuestOS: str

class UnexpectedCustomizationFault(CustomizationFault):
   pass

class UnrecognizedHost(VimFault):
   hostName: str

class UnsharedSwapVMotionNotSupported(MigrationFeatureNotSupported):
   pass


class UnsupportedDatastore(VmConfigFault):
   datastore: Optional[Datastore] = None

class UnsupportedGuest(InvalidVmConfig):
   unsupportedGuestOS: str


class UnsupportedVimApiVersion(VimFault):
   version: Optional[str] = None

class UnsupportedVmxLocation(VmConfigFault):
   pass

class UnusedVirtualDiskBlocksNotScrubbed(DeviceBackingNotSupported):
   pass

class UserNotFound(VimFault):
   principal: str
   unresolved: bool

class VAppConfigFault(VimFault):
   pass

class VAppNotRunning(VmConfigFault):
   pass


class VAppOperationInProgress(RuntimeFault):
   pass

class VAppPropertyFault(VmConfigFault):
   id: str
   category: str
   label: str
   type: str
   value: str

class VAppTaskInProgress(TaskInProgress):
   pass

class VFlashCacheHotConfigNotSupported(VmConfigFault):
   pass


class VFlashModuleNotSupported(VmConfigFault):
   class Reason(Enum):
      CacheModeNotSupported: ClassVar['Reason'] = 'CacheModeNotSupported'
      CacheConsistencyTypeNotSupported: ClassVar['Reason'] = 'CacheConsistencyTypeNotSupported'
      CacheBlockSizeNotSupported: ClassVar['Reason'] = 'CacheBlockSizeNotSupported'
      CacheReservationNotSupported: ClassVar['Reason'] = 'CacheReservationNotSupported'
      DiskSizeNotSupported: ClassVar['Reason'] = 'DiskSizeNotSupported'

   vmName: str
   moduleName: str
   reason: str
   hostName: str

class VFlashModuleVersionIncompatible(VimFault):
   moduleName: str
   vmRequestModuleVersion: str
   hostMinSupportedVerson: str
   hostModuleVersion: str

class VMINotSupported(DeviceNotSupported):
   pass

class VMOnConflictDVPort(CannotAccessNetwork):
   pass

class VMOnVirtualIntranet(CannotAccessNetwork):
   pass

class VMotionAcrossNetworkNotSupported(MigrationFeatureNotSupported):
   pass


class VMotionInterfaceIssue(MigrationFault):
   atSourceHost: bool
   failedHost: str
   failedHostEntity: Optional[HostSystem] = None

class VMotionLinkCapacityLow(VMotionInterfaceIssue):
   network: str

class VMotionLinkDown(VMotionInterfaceIssue):
   network: str

class VMotionNotConfigured(VMotionInterfaceIssue):
   pass

class VMotionNotLicensed(VMotionInterfaceIssue):
   pass

class VMotionNotSupported(VMotionInterfaceIssue):
   pass

class VMotionProtocolIncompatible(MigrationFault):
   pass


class VimFault(MethodFault):
   pass

class VirtualDiskBlocksNotFullyProvisioned(DeviceBackingNotSupported):
   pass

class VirtualDiskModeNotSupported(DeviceNotSupported):
   mode: str

class VirtualEthernetCardNotSupported(DeviceNotSupported):
   pass

class VirtualHardwareCompatibilityIssue(VmConfigFault):
   pass


class VirtualHardwareVersionNotSupported(VirtualHardwareCompatibilityIssue):
   hostName: str
   host: HostSystem


class VmAlreadyExistsInDatacenter(InvalidFolder):
   host: HostSystem
   hostname: str
   vm: list[VirtualMachine] = []

class VmConfigFault(VimFault):
   pass


class VmConfigIncompatibleForFaultTolerance(VmConfigFault):
   fault: Optional[MethodFault] = None


class VmConfigIncompatibleForRecordReplay(VmConfigFault):
   fault: Optional[MethodFault] = None


class VmFaultToleranceConfigIssue(VmFaultToleranceIssue):
   class ReasonForIssue(Enum):
      haNotEnabled: ClassVar['ReasonForIssue'] = 'haNotEnabled'
      moreThanOneSecondary: ClassVar['ReasonForIssue'] = 'moreThanOneSecondary'
      recordReplayNotSupported: ClassVar['ReasonForIssue'] = 'recordReplayNotSupported'
      replayNotSupported: ClassVar['ReasonForIssue'] = 'replayNotSupported'
      templateVm: ClassVar['ReasonForIssue'] = 'templateVm'
      multipleVCPU: ClassVar['ReasonForIssue'] = 'multipleVCPU'
      hostInactive: ClassVar['ReasonForIssue'] = 'hostInactive'
      ftUnsupportedHardware: ClassVar['ReasonForIssue'] = 'ftUnsupportedHardware'
      ftUnsupportedProduct: ClassVar['ReasonForIssue'] = 'ftUnsupportedProduct'
      missingVMotionNic: ClassVar['ReasonForIssue'] = 'missingVMotionNic'
      missingFTLoggingNic: ClassVar['ReasonForIssue'] = 'missingFTLoggingNic'
      thinDisk: ClassVar['ReasonForIssue'] = 'thinDisk'
      verifySSLCertificateFlagNotSet: ClassVar['ReasonForIssue'] = 'verifySSLCertificateFlagNotSet'
      hasSnapshots: ClassVar['ReasonForIssue'] = 'hasSnapshots'
      noConfig: ClassVar['ReasonForIssue'] = 'noConfig'
      ftSecondaryVm: ClassVar['ReasonForIssue'] = 'ftSecondaryVm'
      hasLocalDisk: ClassVar['ReasonForIssue'] = 'hasLocalDisk'
      esxAgentVm: ClassVar['ReasonForIssue'] = 'esxAgentVm'
      video3dEnabled: ClassVar['ReasonForIssue'] = 'video3dEnabled'
      hasUnsupportedDisk: ClassVar['ReasonForIssue'] = 'hasUnsupportedDisk'
      insufficientBandwidth: ClassVar['ReasonForIssue'] = 'insufficientBandwidth'
      hasNestedHVConfiguration: ClassVar['ReasonForIssue'] = 'hasNestedHVConfiguration'
      hasVFlashConfiguration: ClassVar['ReasonForIssue'] = 'hasVFlashConfiguration'
      unsupportedProduct: ClassVar['ReasonForIssue'] = 'unsupportedProduct'
      cpuHvUnsupported: ClassVar['ReasonForIssue'] = 'cpuHvUnsupported'
      cpuHwmmuUnsupported: ClassVar['ReasonForIssue'] = 'cpuHwmmuUnsupported'
      cpuHvDisabled: ClassVar['ReasonForIssue'] = 'cpuHvDisabled'
      hasEFIFirmware: ClassVar['ReasonForIssue'] = 'hasEFIFirmware'
      tooManyVCPUs: ClassVar['ReasonForIssue'] = 'tooManyVCPUs'
      tooMuchMemory: ClassVar['ReasonForIssue'] = 'tooMuchMemory'
      vMotionNotLicensed: ClassVar['ReasonForIssue'] = 'vMotionNotLicensed'
      ftNotLicensed: ClassVar['ReasonForIssue'] = 'ftNotLicensed'
      haAgentIssue: ClassVar['ReasonForIssue'] = 'haAgentIssue'
      unsupportedSPBM: ClassVar['ReasonForIssue'] = 'unsupportedSPBM'
      hasLinkedCloneDisk: ClassVar['ReasonForIssue'] = 'hasLinkedCloneDisk'
      unsupportedPMemHAFailOver: ClassVar['ReasonForIssue'] = 'unsupportedPMemHAFailOver'
      unsupportedEncryptedDisk: ClassVar['ReasonForIssue'] = 'unsupportedEncryptedDisk'
      ftMetroClusterNotEditable: ClassVar['ReasonForIssue'] = 'ftMetroClusterNotEditable'
      noHostGroupConfigured: ClassVar['ReasonForIssue'] = 'noHostGroupConfigured'

   reason: Optional[str] = None
   entityName: Optional[str] = None
   entity: Optional[ManagedEntity] = None


class VmFaultToleranceConfigIssueWrapper(VmFaultToleranceIssue):
   entityName: Optional[str] = None
   entity: Optional[ManagedEntity] = None
   error: Optional[MethodFault] = None


class VmFaultToleranceInvalidFileBacking(VmFaultToleranceIssue):
   class DeviceType(Enum):
      virtualFloppy: ClassVar['DeviceType'] = 'virtualFloppy'
      virtualCdrom: ClassVar['DeviceType'] = 'virtualCdrom'
      virtualSerialPort: ClassVar['DeviceType'] = 'virtualSerialPort'
      virtualParallelPort: ClassVar['DeviceType'] = 'virtualParallelPort'
      virtualDisk: ClassVar['DeviceType'] = 'virtualDisk'

   backingType: Optional[str] = None
   backingFilename: Optional[str] = None

class VmFaultToleranceIssue(VimFault):
   pass


class VmFaultToleranceOpIssuesList(VmFaultToleranceIssue):
   errors: list[MethodFault] = []
   warnings: list[MethodFault] = []


class VmFaultToleranceTooManyFtVcpusOnHost(InsufficientResourcesFault):
   hostName: Optional[str] = None
   maxNumFtVcpus: int


class VmFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
   hostName: Optional[str] = None
   maxNumFtVms: int

class VmHostAffinityRuleViolation(VmConfigFault):
   vmName: str
   hostName: str


class VmLimitLicense(NotEnoughLicenses):
   limit: int

class VmMetadataManagerFault(VimFault):
   pass

class VmMonitorIncompatibleForFaultTolerance(VimFault):
   pass

class VmPowerOnDisabled(InvalidState):
   pass


class VmSmpFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
   hostName: Optional[str] = None
   maxNumSmpFtVms: int

class VmToolsUpgradeFault(VimFault):
   pass

class VmValidateMaxDevice(VimFault):
   device: str
   max: int
   count: int


class VmWwnConflict(InvalidVmConfig):
   vm: Optional[VirtualMachine] = None
   host: Optional[HostSystem] = None
   name: Optional[str] = None
   wwn: Optional[long] = None

class VmfsAlreadyMounted(VmfsMountFault):
   pass

class VmfsAmbiguousMount(VmfsMountFault):
   pass

class VmfsMountFault(HostConfigFault):
   uuid: str

class VmotionInterfaceNotEnabled(HostPowerOpFailed):
   pass

class VolumeEditorError(CustomizationFault):
   pass


class VramLimitLicense(NotEnoughLicenses):
   limit: int

class VsanClusterUuidMismatch(CannotMoveVsanEnabledHost):
   hostClusterUuid: str
   destinationClusterUuid: str


class VsanDiskFault(VsanFault):
   device: Optional[str] = None

class VsanFault(VimFault):
   pass

class VsanIncompatibleDiskMapping(VsanDiskFault):
   pass


class VsanNodeNotMaster(VimFault):
   vsanMasterUuid: Optional[str] = None
   cmmdsMasterButNotStatsMaster: Optional[bool] = None

class VsanSslVerifyCertFault(SSLVerifyFault):
   cert: str

class VspanDestPortConflict(DvsFault):
   vspanSessionKey1: str
   vspanSessionKey2: str
   portKey: str

class VspanPortConflict(DvsFault):
   vspanSessionKey1: str
   vspanSessionKey2: str
   portKey: str

class VspanPortMoveFault(DvsFault):
   srcPortgroupName: str
   destPortgroupName: str
   portKey: str

class VspanPortPromiscChangeFault(DvsFault):
   portKey: str

class VspanPortgroupPromiscChangeFault(DvsFault):
   portgroupName: str

class VspanPortgroupTypeChangeFault(DvsFault):
   portgroupName: str

class VspanPromiscuousPortNotSupported(DvsFault):
   vspanSessionKey: str
   portKey: str

class VspanSameSessionPortConflict(DvsFault):
   vspanSessionKey: str
   portKey: str

class WakeOnLanNotSupported(VirtualHardwareCompatibilityIssue):
   pass

class WakeOnLanNotSupportedByVmotionNIC(HostPowerOpFailed):
   pass


class WillLoseHAProtection(MigrationFault):
   class Resolution(Enum):
      svmotion: ClassVar['Resolution'] = 'svmotion'
      relocate: ClassVar['Resolution'] = 'relocate'

   resolution: str

class WillModifyConfigCpuRequirements(MigrationFault):
   pass

class WillResetSnapshotDirectory(MigrationFault):
   pass

class WipeDiskFault(VimFault):
   pass
