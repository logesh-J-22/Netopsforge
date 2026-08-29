# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long
from pyVmomi.vim import AuthorizationManager
from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Datacenter
from pyVmomi.vim import Datastore
from pyVmomi.vim import DistributedVirtualSwitch

from pyVmomi.vim import ElementDescription
from pyVmomi.vim import EnumDescription
from pyVmomi.vim import Folder

from pyVmomi.vim import HistoryCollector
from pyVmomi.vim import HostSystem
from pyVmomi.vim import LicenseManager

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import TaskInfo
from pyVmomi.vim import TransitGateway
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import MethodFault
from pyVmomi.vim.alarm import Alarm

from pyVmomi.vim.dvs import DistributedVirtualPort

from pyVmomi.vim.dvs import DistributedVirtualPortgroup

from pyVmomi.vim.dvs import HostMember

from pyVmomi.vim.dvs import PortConnectee

from pyVmomi.vim.dvs import PortConnection
from pyVmomi.vim.dvs import ProductSpec
from pyVmomi.vim.host import LocalAccountManager
from pyVmomi.vim.profile import Profile

from pyVmomi.vim.scheduler import ScheduledTask

from pyVmomi.vim.vm import ConfigSpec

from pyVmomi.vim.vm import Message
from pyVmomi.vim.profile.host import HostSpecification
from pyVmomi.vim.profile.host import HostSubSpecification



class AccountCreatedEvent(HostEvent):
   spec: LocalAccountManager.AccountSpecification
   group: bool

class AccountRemovedEvent(HostEvent):
   account: str
   group: bool


class AccountUpdatedEvent(HostEvent):
   spec: LocalAccountManager.AccountSpecification
   group: bool
   prevDescription: Optional[str] = None

class AdminPasswordNotChangedEvent(HostEvent):
   pass

class AlarmAcknowledgedEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument

class AlarmActionTriggeredEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument

class AlarmClearedEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument
   # Reserved python keyword: commenting out.
   # from: str

class AlarmCreatedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument

class AlarmEmailCompletedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   to: str


class AlarmEmailFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   to: str
   reason: MethodFault

class AlarmEvent(Event):
   alarm: AlarmEventArgument


class AlarmEventArgument(EntityEventArgument):
   alarm: Alarm


class AlarmReconfiguredEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   configChanges: Optional[ChangesInfoEventArgument] = None

class AlarmRemovedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument

class AlarmScriptCompleteEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   script: str


class AlarmScriptFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   script: str
   reason: MethodFault

class AlarmSnmpCompletedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument


class AlarmSnmpFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   reason: MethodFault

class AlarmStatusChangedEvent(AlarmEvent):
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument
   # Reserved python keyword: commenting out.
   # from: str
   to: str

class AllVirtualMachinesLicensedEvent(LicenseEvent):
   pass

class AlreadyAuthenticatedSessionEvent(SessionEvent):
   pass

class AuthorizationEvent(Event):
   pass

class BadUsernameSessionEvent(SessionEvent):
   ipAddress: str

class CanceledHostOperationEvent(HostEvent):
   pass


class ChangesInfoEventArgument(DynamicData):
   modified: Optional[str] = None
   added: Optional[str] = None
   deleted: Optional[str] = None

class ClusterComplianceCheckedEvent(ClusterEvent):
   profile: ProfileEventArgument

class ClusterCreatedEvent(ClusterEvent):
   parent: FolderEventArgument

class ClusterDestroyedEvent(ClusterEvent):
   pass

class ClusterEvent(Event):
   pass

class ClusterOvercommittedEvent(ClusterEvent):
   pass


class ClusterReconfiguredEvent(ClusterEvent):
   configChanges: Optional[ChangesInfoEventArgument] = None

class ClusterStatusChangedEvent(ClusterEvent):
   oldStatus: str
   newStatus: str


class ComputeResourceEventArgument(EntityEventArgument):
   computeResource: ComputeResource

class CustomFieldDefAddedEvent(CustomFieldDefEvent):
   pass

class CustomFieldDefEvent(CustomFieldEvent):
   fieldKey: int
   name: str

class CustomFieldDefRemovedEvent(CustomFieldDefEvent):
   pass

class CustomFieldDefRenamedEvent(CustomFieldDefEvent):
   newName: str

class CustomFieldEvent(Event):
   pass


class CustomFieldValueChangedEvent(CustomFieldEvent):
   entity: ManagedEntityEventArgument
   fieldKey: int
   name: str
   value: str
   prevState: Optional[str] = None


class CustomizationEvent(VmEvent):
   logLocation: Optional[str] = None


class CustomizationFailed(CustomizationEvent):
   class ReasonCode(Enum):
      userDefinedScriptDisabled: ClassVar['ReasonCode'] = 'userDefinedScriptDisabled'
      customizationDisabled: ClassVar['ReasonCode'] = 'customizationDisabled'
      rawDataIsNotSupported: ClassVar['ReasonCode'] = 'rawDataIsNotSupported'
      wrongMetadataFormat: ClassVar['ReasonCode'] = 'wrongMetadataFormat'

   reason: Optional[str] = None

class CustomizationLinuxIdentityFailed(CustomizationFailed):
   pass

class CustomizationNetworkSetupFailed(CustomizationFailed):
   pass

class CustomizationStartedEvent(CustomizationEvent):
   pass

class CustomizationSucceeded(CustomizationEvent):
   pass

class CustomizationSysprepFailed(CustomizationFailed):
   sysprepVersion: str
   systemVersion: str

class CustomizationUnknownFailure(CustomizationFailed):
   pass

class DVPortgroupCreatedEvent(DVPortgroupEvent):
   pass

class DVPortgroupDestroyedEvent(DVPortgroupEvent):
   pass

class DVPortgroupEvent(Event):
   pass


class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
   configSpec: DistributedVirtualPortgroup.ConfigSpec
   configChanges: Optional[ChangesInfoEventArgument] = None

class DVPortgroupRenamedEvent(DVPortgroupEvent):
   oldName: str
   newName: str

class DasAdmissionControlDisabledEvent(ClusterEvent):
   pass

class DasAdmissionControlEnabledEvent(ClusterEvent):
   pass

class DasAgentFoundEvent(ClusterEvent):
   pass

class DasAgentUnavailableEvent(ClusterEvent):
   pass

class DasClusterIsolatedEvent(ClusterEvent):
   pass

class DasDisabledEvent(ClusterEvent):
   pass

class DasEnabledEvent(ClusterEvent):
   pass

class DasHostFailedEvent(ClusterEvent):
   failedHost: HostEventArgument

class DasHostIsolatedEvent(ClusterEvent):
   isolatedHost: HostEventArgument

class DatacenterCreatedEvent(DatacenterEvent):
   parent: FolderEventArgument

class DatacenterEvent(Event):
   pass


class DatacenterEventArgument(EntityEventArgument):
   datacenter: Datacenter

class DatacenterRenamedEvent(DatacenterEvent):
   oldName: str
   newName: str


class DatastoreCapacityIncreasedEvent(DatastoreEvent):
   oldCapacity: long
   newCapacity: long

class DatastoreDestroyedEvent(DatastoreEvent):
   pass

class DatastoreDiscoveredEvent(HostEvent):
   datastore: DatastoreEventArgument

class DatastoreDuplicatedEvent(DatastoreEvent):
   pass


class DatastoreEvent(Event):
   datastore: Optional[DatastoreEventArgument] = None


class DatastoreEventArgument(EntityEventArgument):
   datastore: Datastore

class DatastoreFileCopiedEvent(DatastoreFileEvent):
   sourceDatastore: DatastoreEventArgument
   sourceFile: str

class DatastoreFileDeletedEvent(DatastoreFileEvent):
   pass


class DatastoreFileEvent(DatastoreEvent):
   targetFile: str
   sourceOfOperation: Optional[str] = None
   succeeded: Optional[bool] = None

class DatastoreFileMovedEvent(DatastoreFileEvent):
   sourceDatastore: DatastoreEventArgument
   sourceFile: str

class DatastoreIORMReconfiguredEvent(DatastoreEvent):
   pass

class DatastorePrincipalConfigured(HostEvent):
   datastorePrincipal: str

class DatastoreRemovedOnHostEvent(HostEvent):
   datastore: DatastoreEventArgument

class DatastoreRenamedEvent(DatastoreEvent):
   oldName: str
   newName: str

class DatastoreRenamedOnHostEvent(HostEvent):
   oldName: str
   newName: str

class DrsDisabledEvent(ClusterEvent):
   pass

class DrsEnabledEvent(ClusterEvent):
   behavior: str

class DrsEnteredStandbyModeEvent(EnteredStandbyModeEvent):
   pass

class DrsEnteringStandbyModeEvent(EnteringStandbyModeEvent):
   pass

class DrsExitStandbyModeFailedEvent(ExitStandbyModeFailedEvent):
   pass

class DrsExitedStandbyModeEvent(ExitedStandbyModeEvent):
   pass

class DrsExitingStandbyModeEvent(ExitingStandbyModeEvent):
   pass

class DrsInvocationFailedEvent(ClusterEvent):
   pass

class DrsRecoveredFromFailureEvent(ClusterEvent):
   pass


class DrsResourceConfigureFailedEvent(HostEvent):
   reason: MethodFault

class DrsResourceConfigureSyncedEvent(HostEvent):
   pass

class DrsRuleComplianceEvent(VmEvent):
   pass

class DrsRuleViolationEvent(VmEvent):
   pass

class DrsSoftRuleViolationEvent(VmEvent):
   pass

class DrsVmMigratedEvent(VmMigratedEvent):
   pass

class DrsVmPoweredOnEvent(VmPoweredOnEvent):
   pass

class DuplicateIpDetectedEvent(HostEvent):
   duplicateIP: str
   macAddress: str

class DvpgImportEvent(DVPortgroupEvent):
   importType: str

class DvpgRestoreEvent(DVPortgroupEvent):
   pass

class DvsCreatedEvent(DvsEvent):
   parent: FolderEventArgument

class DvsDestroyedEvent(DvsEvent):
   pass


class DvsEvent(Event):
   class PortBlockState(Enum):
      unset: ClassVar['PortBlockState'] = 'unset'
      blocked: ClassVar['PortBlockState'] = 'blocked'
      unblocked: ClassVar['PortBlockState'] = 'unblocked'
      unknown: ClassVar['PortBlockState'] = 'unknown'


class DvsEventArgument(EntityEventArgument):
   dvs: DistributedVirtualSwitch


class DvsHealthStatusChangeEvent(HostEvent):
   switchUuid: str
   healthResult: Optional[HostMember.HealthCheckResult] = None

class DvsHostBackInSyncEvent(DvsEvent):
   hostBackInSync: HostEventArgument

class DvsHostJoinedEvent(DvsEvent):
   hostJoined: HostEventArgument

class DvsHostLeftEvent(DvsEvent):
   hostLeft: HostEventArgument


class DvsHostStatusUpdated(DvsEvent):
   hostMember: HostEventArgument
   oldStatus: Optional[str] = None
   newStatus: Optional[str] = None
   oldStatusDetail: Optional[str] = None
   newStatusDetail: Optional[str] = None

class DvsHostWentOutOfSyncEvent(DvsEvent):
   hostOutOfSync: DvsOutOfSyncHostArgument

class DvsImportEvent(DvsEvent):
   importType: str

class DvsMergedEvent(DvsEvent):
   sourceDvs: DvsEventArgument
   destinationDvs: DvsEventArgument


class DvsOutOfSyncHostArgument(DynamicData):
   outOfSyncHost: HostEventArgument
   configParamters: list[str] = []


class DvsPortBlockedEvent(DvsEvent):
   portKey: str
   statusDetail: Optional[str] = None
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None
   prevBlockState: Optional[str] = None


class DvsPortConnectedEvent(DvsEvent):
   portKey: str
   connectee: Optional[PortConnectee] = None

class DvsPortCreatedEvent(DvsEvent):
   portKey: list[str] = []

class DvsPortDeletedEvent(DvsEvent):
   portKey: list[str] = []


class DvsPortDisconnectedEvent(DvsEvent):
   portKey: str
   connectee: Optional[PortConnectee] = None


class DvsPortEnteredPassthruEvent(DvsEvent):
   portKey: str
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None


class DvsPortExitedPassthruEvent(DvsEvent):
   portKey: str
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None

class DvsPortJoinPortgroupEvent(DvsEvent):
   portKey: str
   portgroupKey: str
   portgroupName: str

class DvsPortLeavePortgroupEvent(DvsEvent):
   portKey: str
   portgroupKey: str
   portgroupName: str


class DvsPortLinkDownEvent(DvsEvent):
   portKey: str
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None


class DvsPortLinkUpEvent(DvsEvent):
   portKey: str
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None


class DvsPortReconfiguredEvent(DvsEvent):
   portKey: list[str] = []
   configChanges: list[ChangesInfoEventArgument] = []


class DvsPortRuntimeChangeEvent(DvsEvent):
   portKey: str
   runtimeInfo: DistributedVirtualPort.RuntimeInfo


class DvsPortUnblockedEvent(DvsEvent):
   portKey: str
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None
   prevBlockState: Optional[str] = None

class DvsPortVendorSpecificStateChangeEvent(DvsEvent):
   portKey: str


class DvsReconfiguredEvent(DvsEvent):
   configSpec: DistributedVirtualSwitch.ConfigSpec
   configChanges: Optional[ChangesInfoEventArgument] = None

class DvsRenamedEvent(DvsEvent):
   oldName: str
   newName: str

class DvsRestoreEvent(DvsEvent):
   pass


class DvsUpgradeAvailableEvent(DvsEvent):
   productInfo: ProductSpec


class DvsUpgradeInProgressEvent(DvsEvent):
   productInfo: ProductSpec


class DvsUpgradeRejectedEvent(DvsEvent):
   productInfo: ProductSpec


class DvsUpgradedEvent(DvsEvent):
   productInfo: ProductSpec

class EnteredMaintenanceModeEvent(HostEvent):
   pass

class EnteredStandbyModeEvent(HostEvent):
   pass

class EnteringMaintenanceModeEvent(HostEvent):
   pass

class EnteringStandbyModeEvent(HostEvent):
   pass

class EntityEventArgument(EventArgument):
   name: str

class ErrorUpgradeEvent(UpgradeEvent):
   pass


class Event(DynamicData):
   class EventSeverity(Enum):
      error: ClassVar['EventSeverity'] = 'error'
      warning: ClassVar['EventSeverity'] = 'warning'
      info: ClassVar['EventSeverity'] = 'info'
      user: ClassVar['EventSeverity'] = 'user'

   key: int
   chainId: int
   createdTime: datetime
   userName: str
   datacenter: Optional[DatacenterEventArgument] = None
   computeResource: Optional[ComputeResourceEventArgument] = None
   host: Optional[HostEventArgument] = None
   vm: Optional[VmEventArgument] = None
   ds: Optional[DatastoreEventArgument] = None
   net: Optional[NetworkEventArgument] = None
   dvs: Optional[DvsEventArgument] = None
   tgw: Optional[TgwEventArgument] = None
   fullFormattedMessage: Optional[str] = None
   changeTag: Optional[str] = None
   auditId: Optional[str] = None


class EventArgument(DynamicData):
   pass


class EventDescription(DynamicData):
   class EventCategory(Enum):
      info: ClassVar['EventCategory'] = 'info'
      warning: ClassVar['EventCategory'] = 'warning'
      error: ClassVar['EventCategory'] = 'error'
      user: ClassVar['EventCategory'] = 'user'

   class EventArgDesc(DynamicData):
      name: str
      type: str
      description: Optional[ElementDescription] = None

   class EventDetail(DynamicData):
      key: type
      description: Optional[str] = None
      category: str
      formatOnDatacenter: str
      formatOnComputeResource: str
      formatOnHost: str
      formatOnVm: str
      fullFormat: str
      longDescription: Optional[str] = None

   category: list[ElementDescription] = []
   eventInfo: list[EventDetail] = []
   enumeratedTypes: list[EnumDescription] = []


class EventEx(Event):
   eventTypeId: str
   severity: Optional[str] = None
   message: Optional[str] = None
   arguments: list[KeyAnyValue] = []
   objectId: Optional[str] = None
   objectType: Optional[type] = None
   objectName: Optional[str] = None
   fault: Optional[MethodFault] = None


class EventFilterSpec(DynamicData):
   class RecursionOption(Enum):
      self: ClassVar['RecursionOption'] = 'self'
      children: ClassVar['RecursionOption'] = 'children'
      all: ClassVar['RecursionOption'] = 'all'

   class ByEntity(DynamicData):
      entity: ManagedEntity
      recursion: RecursionOption

   class ByTime(DynamicData):
      beginTime: Optional[datetime] = None
      endTime: Optional[datetime] = None

   class ByUsername(DynamicData):
      systemUser: bool
      userList: list[str] = []

   entity: Optional[ByEntity] = None
   time: Optional[ByTime] = None
   userName: Optional[ByUsername] = None
   eventChainId: Optional[int] = None
   alarm: Optional[Alarm] = None
   scheduledTask: Optional[ScheduledTask] = None
   disableFullMessage: Optional[bool] = None
   category: list[str] = []
   type: list[type] = []
   tag: list[str] = []
   eventTypeId: list[str] = []
   maxCount: Optional[int] = None
   delayedInit: Optional[bool] = None
   auditable: Optional[bool] = None
   auditId: list[str] = []


class EventHistoryCollector(HistoryCollector):
   @property
   def latestPage(self) -> list[Event]: ...
   @property
   def initialized(self) -> Optional[bool]: ...

   def ReadNext(self, maxCount: int) -> list[Event]: ...
   def ReadPrev(self, maxCount: int) -> list[Event]: ...


class EventManager(ManagedObject):
   class EventViewSpec(DynamicData):
      pass

   class ViewByStartId(EventViewSpec):
      startEventId: int
      isForward: bool

   @property
   def description(self) -> EventDescription: ...
   @property
   def latestEvent(self) -> Optional[Event]: ...
   @property
   def maxCollector(self) -> int: ...

   def RetrieveArgumentDescription(self, eventTypeId: str) -> list[EventDescription.EventArgDesc]: ...
   def CreateCollector(self, filter: EventFilterSpec) -> EventHistoryCollector: ...
   def LogUserEvent(self, entity: ManagedEntity, msg: str) -> None: ...
   def QueryEvent(self, filter: EventFilterSpec, eventViewSpec: Optional[EventViewSpec]) -> list[Event]: ...
   def PostEvent(self, eventToPost: Event, taskInfo: Optional[TaskInfo]) -> None: ...

class ExitMaintenanceModeEvent(HostEvent):
   pass

class ExitStandbyModeFailedEvent(HostEvent):
   pass

class ExitedStandbyModeEvent(HostEvent):
   pass

class ExitingStandbyModeEvent(HostEvent):
   pass


class ExtendedEvent(GeneralEvent):
   class Pair(DynamicData):
      key: str
      value: str

   eventTypeId: str
   managedObject: ManagedObject
   data: list[Pair] = []

class FailoverLevelRestored(ClusterEvent):
   pass


class FolderEventArgument(EntityEventArgument):
   folder: Folder

class GeneralEvent(Event):
   message: str

class GeneralHostErrorEvent(GeneralEvent):
   pass

class GeneralHostInfoEvent(GeneralEvent):
   pass

class GeneralHostWarningEvent(GeneralEvent):
   pass


class GeneralUserEvent(GeneralEvent):
   entity: Optional[ManagedEntityEventArgument] = None

class GeneralVmErrorEvent(GeneralEvent):
   pass

class GeneralVmInfoEvent(GeneralEvent):
   pass

class GeneralVmWarningEvent(GeneralEvent):
   pass

class GhostDvsProxySwitchDetectedEvent(HostEvent):
   switchUuid: list[str] = []

class GhostDvsProxySwitchRemovedEvent(HostEvent):
   switchUuid: list[str] = []


class GlobalMessageChangedEvent(SessionEvent):
   message: str
   prevMessage: Optional[str] = None


class HealthStatusChangedEvent(Event):
   componentId: str
   oldStatus: str
   newStatus: str
   componentName: str
   serviceId: Optional[str] = None

class HostAddFailedEvent(HostEvent):
   hostname: str

class HostAddedEvent(HostEvent):
   pass

class HostAdminDisableEvent(HostEvent):
   pass

class HostAdminEnableEvent(HostEvent):
   pass

class HostCnxFailedAccountFailedEvent(HostEvent):
   pass

class HostCnxFailedAlreadyManagedEvent(HostEvent):
   serverName: str

class HostCnxFailedBadCcagentEvent(HostEvent):
   pass

class HostCnxFailedBadUsernameEvent(HostEvent):
   pass

class HostCnxFailedBadVersionEvent(HostEvent):
   pass

class HostCnxFailedCcagentUpgradeEvent(HostEvent):
   pass

class HostCnxFailedEvent(HostEvent):
   pass

class HostCnxFailedNetworkErrorEvent(HostEvent):
   pass

class HostCnxFailedNoAccessEvent(HostEvent):
   pass

class HostCnxFailedNoConnectionEvent(HostEvent):
   pass

class HostCnxFailedNoLicenseEvent(HostEvent):
   pass

class HostCnxFailedNotFoundEvent(HostEvent):
   pass

class HostCnxFailedTimeoutEvent(HostEvent):
   pass

class HostComplianceCheckedEvent(HostEvent):
   profile: ProfileEventArgument

class HostCompliantEvent(HostEvent):
   pass

class HostConfigAppliedEvent(HostEvent):
   pass

class HostConnectedEvent(HostEvent):
   pass

class HostConnectionLostEvent(HostEvent):
   pass

class HostDasDisabledEvent(HostEvent):
   pass

class HostDasDisablingEvent(HostEvent):
   pass

class HostDasEnabledEvent(HostEvent):
   pass

class HostDasEnablingEvent(HostEvent):
   pass


class HostDasErrorEvent(HostEvent):
   class HostDasErrorReason(Enum):
      configFailed: ClassVar['HostDasErrorReason'] = 'configFailed'
      timeout: ClassVar['HostDasErrorReason'] = 'timeout'
      communicationInitFailed: ClassVar['HostDasErrorReason'] = 'communicationInitFailed'
      healthCheckScriptFailed: ClassVar['HostDasErrorReason'] = 'healthCheckScriptFailed'
      agentFailed: ClassVar['HostDasErrorReason'] = 'agentFailed'
      agentShutdown: ClassVar['HostDasErrorReason'] = 'agentShutdown'
      isolationAddressUnpingable: ClassVar['HostDasErrorReason'] = 'isolationAddressUnpingable'
      other: ClassVar['HostDasErrorReason'] = 'other'

   message: Optional[str] = None
   reason: Optional[str] = None

class HostDasEvent(HostEvent):
   pass

class HostDasOkEvent(HostEvent):
   pass


class HostDisconnectedEvent(HostEvent):
   class ReasonCode(Enum):
      sslThumbprintVerifyFailed: ClassVar['ReasonCode'] = 'sslThumbprintVerifyFailed'
      licenseExpired: ClassVar['ReasonCode'] = 'licenseExpired'
      agentUpgrade: ClassVar['ReasonCode'] = 'agentUpgrade'
      userRequest: ClassVar['ReasonCode'] = 'userRequest'
      insufficientLicenses: ClassVar['ReasonCode'] = 'insufficientLicenses'
      agentOutOfDate: ClassVar['ReasonCode'] = 'agentOutOfDate'
      passwordDecryptFailure: ClassVar['ReasonCode'] = 'passwordDecryptFailure'
      unknown: ClassVar['ReasonCode'] = 'unknown'
      vcVRAMCapacityExceeded: ClassVar['ReasonCode'] = 'vcVRAMCapacityExceeded'

   reason: Optional[str] = None


class HostEnableAdminFailedEvent(HostEvent):
   permissions: list[AuthorizationManager.Permission] = []

class HostEvent(Event):
   pass


class HostEventArgument(EntityEventArgument):
   host: HostSystem


class HostExtraNetworksEvent(HostDasEvent):
   ips: Optional[str] = None

class HostGetShortNameFailedEvent(HostEvent):
   pass

class HostInAuditModeEvent(HostEvent):
   pass

class HostInventoryFullEvent(LicenseEvent):
   capacity: int

class HostInventoryUnreadableEvent(Event):
   pass

class HostIpChangedEvent(HostEvent):
   oldIP: str
   newIP: str

class HostIpInconsistentEvent(HostEvent):
   ipAddress: str
   ipAddress2: str

class HostIpToShortNameFailedEvent(HostEvent):
   pass

class HostIsolationIpPingFailedEvent(HostDasEvent):
   isolationIp: str

class HostLicenseExpiredEvent(LicenseEvent):
   pass


class HostLocalPortCreatedEvent(DvsEvent):
   hostLocalPort: DistributedVirtualPort.HostLocalPortInfo


class HostMissingNetworksEvent(HostDasEvent):
   ips: Optional[str] = None


class HostMonitoringStateChangedEvent(ClusterEvent):
   state: str
   prevState: Optional[str] = None


class HostNoAvailableNetworksEvent(HostDasEvent):
   ips: Optional[str] = None

class HostNoHAEnabledPortGroupsEvent(HostDasEvent):
   pass

class HostNoRedundantManagementNetworkEvent(HostDasEvent):
   pass

class HostNonCompliantEvent(HostEvent):
   pass

class HostNotInClusterEvent(HostDasEvent):
   pass

class HostOvercommittedEvent(ClusterOvercommittedEvent):
   pass

class HostPrimaryAgentNotShortNameEvent(HostDasEvent):
   primaryAgent: str

class HostProfileAppliedEvent(HostEvent):
   profile: ProfileEventArgument

class HostReconnectionFailedEvent(HostEvent):
   pass

class HostRemovedEvent(HostEvent):
   pass

class HostShortNameInconsistentEvent(HostDasEvent):
   shortName: str
   shortName2: str

class HostShortNameToIpFailedEvent(HostEvent):
   shortName: str

class HostShutdownEvent(HostEvent):
   reason: str

class HostSpecificationChangedEvent(HostEvent):
   pass

class HostSpecificationRequireEvent(HostEvent):
   pass


class HostSpecificationUpdateEvent(HostEvent):
   hostSpec: HostSpecification

class HostStatusChangedEvent(ClusterStatusChangedEvent):
   pass

class HostSubSpecificationDeleteEvent(HostEvent):
   subSpecName: str


class HostSubSpecificationUpdateEvent(HostEvent):
   hostSubSpec: HostSubSpecification


class HostSyncFailedEvent(HostEvent):
   reason: MethodFault

class HostUpgradeFailedEvent(HostEvent):
   pass

class HostUserWorldSwapNotEnabledEvent(HostEvent):
   pass


class HostVnicConnectedToCustomizedDVPortEvent(HostEvent):
   vnic: VnicPortArgument
   prevPortKey: Optional[str] = None


class HostWwnChangedEvent(HostEvent):
   oldNodeWwns: list[long] = []
   oldPortWwns: list[long] = []
   newNodeWwns: list[long] = []
   newPortWwns: list[long] = []


class HostWwnConflictEvent(HostEvent):
   conflictedVms: list[VmEventArgument] = []
   conflictedHosts: list[HostEventArgument] = []
   wwn: long

class IncorrectHostInformationEvent(LicenseEvent):
   pass

class InfoUpgradeEvent(UpgradeEvent):
   pass

class InsufficientFailoverResourcesEvent(ClusterEvent):
   pass

class InvalidEditionEvent(LicenseEvent):
   feature: str

class LicenseEvent(Event):
   pass


class LicenseExpiredEvent(Event):
   feature: LicenseManager.FeatureInfo

class LicenseNonComplianceEvent(LicenseEvent):
   url: str

class LicenseRestrictedEvent(LicenseEvent):
   pass

class LicenseServerAvailableEvent(LicenseEvent):
   licenseServer: str

class LicenseServerUnavailableEvent(LicenseEvent):
   licenseServer: str


class LocalDatastoreCreatedEvent(HostEvent):
   datastore: DatastoreEventArgument
   datastoreUrl: Optional[str] = None

class LocalTSMEnabledEvent(HostEvent):
   pass

class LockerMisconfiguredEvent(Event):
   datastore: DatastoreEventArgument


class LockerReconfiguredEvent(Event):
   oldDatastore: Optional[DatastoreEventArgument] = None
   newDatastore: Optional[DatastoreEventArgument] = None


class ManagedEntityEventArgument(EntityEventArgument):
   entity: ManagedEntity

class MigrationErrorEvent(MigrationEvent):
   pass


class MigrationEvent(VmEvent):
   fault: MethodFault

class MigrationHostErrorEvent(MigrationEvent):
   dstHost: HostEventArgument

class MigrationHostWarningEvent(MigrationEvent):
   dstHost: HostEventArgument

class MigrationResourceErrorEvent(MigrationEvent):
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument

class MigrationResourceWarningEvent(MigrationEvent):
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument

class MigrationWarningEvent(MigrationEvent):
   pass

class MtuMatchEvent(DvsHealthStatusChangeEvent):
   pass

class MtuMismatchEvent(DvsHealthStatusChangeEvent):
   pass


class NASDatastoreCreatedEvent(HostEvent):
   datastore: DatastoreEventArgument
   datastoreUrl: Optional[str] = None


class NetworkEventArgument(EntityEventArgument):
   network: Network

class NetworkRollbackEvent(Event):
   methodName: str
   transactionId: str

class NoAccessUserEvent(SessionEvent):
   ipAddress: str

class NoDatastoresConfiguredEvent(HostEvent):
   pass


class NoLicenseEvent(LicenseEvent):
   feature: LicenseManager.FeatureInfo

class NoMaintenanceModeDrsRecommendationForVM(VmEvent):
   pass

class NonVIWorkloadDetectedOnDatastoreEvent(DatastoreEvent):
   pass

class NotEnoughResourcesToStartVmEvent(VmEvent):
   reason: str

class OutOfSyncDvsHost(DvsEvent):
   hostOutOfSync: list[DvsOutOfSyncHostArgument] = []

class PermissionAddedEvent(PermissionEvent):
   role: RoleEventArgument
   propagate: bool

class PermissionEvent(AuthorizationEvent):
   entity: ManagedEntityEventArgument
   principal: str
   group: bool

class PermissionRemovedEvent(PermissionEvent):
   pass


class PermissionUpdatedEvent(PermissionEvent):
   role: RoleEventArgument
   propagate: bool
   prevRole: Optional[RoleEventArgument] = None
   prevPropagate: Optional[bool] = None

class ProfileAssociatedEvent(ProfileEvent):
   pass

class ProfileChangedEvent(ProfileEvent):
   pass

class ProfileCreatedEvent(ProfileEvent):
   pass

class ProfileDissociatedEvent(ProfileEvent):
   pass

class ProfileEvent(Event):
   profile: ProfileEventArgument


class ProfileEventArgument(EventArgument):
   profile: Profile
   name: str


class ProfileReferenceHostChangedEvent(ProfileEvent):
   referenceHost: Optional[HostSystem] = None
   referenceHostName: Optional[str] = None
   prevReferenceHostName: Optional[str] = None

class ProfileRemovedEvent(ProfileEvent):
   pass


class RecoveryEvent(DvsEvent):
   hostName: str
   portKey: str
   dvsUuid: Optional[str] = None
   vnic: Optional[str] = None

class RemoteTSMEnabledEvent(HostEvent):
   pass

class ResourcePoolCreatedEvent(ResourcePoolEvent):
   parent: ResourcePoolEventArgument

class ResourcePoolDestroyedEvent(ResourcePoolEvent):
   pass

class ResourcePoolEvent(Event):
   resourcePool: ResourcePoolEventArgument


class ResourcePoolEventArgument(EntityEventArgument):
   resourcePool: ResourcePool

class ResourcePoolMovedEvent(ResourcePoolEvent):
   oldParent: ResourcePoolEventArgument
   newParent: ResourcePoolEventArgument


class ResourcePoolReconfiguredEvent(ResourcePoolEvent):
   configChanges: Optional[ChangesInfoEventArgument] = None

class ResourceViolatedEvent(ResourcePoolEvent):
   pass


class RoleAddedEvent(RoleEvent):
   privilegeList: list[str] = []

class RoleEvent(AuthorizationEvent):
   role: RoleEventArgument

class RoleEventArgument(EventArgument):
   roleId: int
   name: str

class RoleRemovedEvent(RoleEvent):
   pass


class RoleUpdatedEvent(RoleEvent):
   privilegeList: list[str] = []
   prevRoleName: Optional[str] = None
   privilegesAdded: list[str] = []
   privilegesRemoved: list[str] = []


class RollbackEvent(DvsEvent):
   hostName: str
   methodName: Optional[str] = None

class ScheduledTaskCompletedEvent(ScheduledTaskEvent):
   pass

class ScheduledTaskCreatedEvent(ScheduledTaskEvent):
   pass

class ScheduledTaskEmailCompletedEvent(ScheduledTaskEvent):
   to: str


class ScheduledTaskEmailFailedEvent(ScheduledTaskEvent):
   to: str
   reason: MethodFault

class ScheduledTaskEvent(Event):
   scheduledTask: ScheduledTaskEventArgument
   entity: ManagedEntityEventArgument


class ScheduledTaskEventArgument(EntityEventArgument):
   scheduledTask: ScheduledTask


class ScheduledTaskFailedEvent(ScheduledTaskEvent):
   reason: MethodFault


class ScheduledTaskReconfiguredEvent(ScheduledTaskEvent):
   configChanges: Optional[ChangesInfoEventArgument] = None

class ScheduledTaskRemovedEvent(ScheduledTaskEvent):
   pass

class ScheduledTaskStartedEvent(ScheduledTaskEvent):
   pass

class ServerLicenseExpiredEvent(LicenseEvent):
   product: str

class ServerStartedSessionEvent(SessionEvent):
   pass

class SessionEvent(Event):
   pass

class SessionTerminatedEvent(SessionEvent):
   sessionId: str
   terminatedUsername: str


class TaskEvent(Event):
   info: TaskInfo

class TaskTimeoutEvent(TaskEvent):
   pass

class TeamingMatchEvent(DvsHealthStatusChangeEvent):
   pass

class TeamingMisMatchEvent(DvsHealthStatusChangeEvent):
   pass

class TemplateBeingUpgradedEvent(TemplateUpgradeEvent):
   pass

class TemplateUpgradeEvent(Event):
   legacyTemplate: str


class TemplateUpgradeFailedEvent(TemplateUpgradeEvent):
   reason: MethodFault

class TemplateUpgradedEvent(TemplateUpgradeEvent):
   pass


class TgwEventArgument(EntityEventArgument):
   tgw: TransitGateway

class TimedOutHostOperationEvent(HostEvent):
   pass

class UnlicensedVirtualMachinesEvent(LicenseEvent):
   unlicensed: int
   available: int

class UnlicensedVirtualMachinesFoundEvent(LicenseEvent):
   available: int

class UpdatedAgentBeingRestartedEvent(HostEvent):
   pass

class UpgradeEvent(Event):
   message: str

class UplinkPortMtuNotSupportEvent(DvsHealthStatusChangeEvent):
   pass

class UplinkPortMtuSupportEvent(DvsHealthStatusChangeEvent):
   pass

class UplinkPortVlanTrunkedEvent(DvsHealthStatusChangeEvent):
   pass

class UplinkPortVlanUntrunkedEvent(DvsHealthStatusChangeEvent):
   pass

class UserAssignedToGroup(HostEvent):
   userLogin: str
   group: str


class UserLoginSessionEvent(SessionEvent):
   ipAddress: str
   userAgent: Optional[str] = None
   locale: str
   sessionId: str


class UserLogoutSessionEvent(SessionEvent):
   ipAddress: Optional[str] = None
   userAgent: Optional[str] = None
   callCount: Optional[long] = None
   sessionId: Optional[str] = None
   loginTime: Optional[datetime] = None

class UserPasswordChanged(HostEvent):
   userLogin: str

class UserUnassignedFromGroup(HostEvent):
   userLogin: str
   group: str

class UserUpgradeEvent(UpgradeEvent):
   pass


class VMFSDatastoreCreatedEvent(HostEvent):
   datastore: DatastoreEventArgument
   datastoreUrl: Optional[str] = None

class VMFSDatastoreExpandedEvent(HostEvent):
   datastore: DatastoreEventArgument

class VMFSDatastoreExtendedEvent(HostEvent):
   datastore: DatastoreEventArgument

class VMotionLicenseExpiredEvent(LicenseEvent):
   pass


class VcAgentUninstallFailedEvent(HostEvent):
   reason: Optional[str] = None

class VcAgentUninstalledEvent(HostEvent):
   pass


class VcAgentUpgradeFailedEvent(HostEvent):
   reason: Optional[str] = None

class VcAgentUpgradedEvent(HostEvent):
   pass

class VimAccountPasswordChangedEvent(HostEvent):
   pass

class VmAcquiredMksTicketEvent(VmEvent):
   pass

class VmAcquiredTicketEvent(VmEvent):
   ticketType: str

class VmAutoRenameEvent(VmEvent):
   oldName: str
   newName: str

class VmBeingClonedEvent(VmCloneEvent):
   destFolder: FolderEventArgument
   destName: str
   destHost: HostEventArgument

class VmBeingClonedNoFolderEvent(VmCloneEvent):
   destName: str
   destHost: HostEventArgument


class VmBeingCreatedEvent(VmEvent):
   configSpec: Optional[ConfigSpec] = None

class VmBeingDeployedEvent(VmEvent):
   srcTemplate: VmEventArgument


class VmBeingHotMigratedEvent(VmEvent):
   destHost: HostEventArgument
   destDatacenter: Optional[DatacenterEventArgument] = None
   destDatastore: Optional[DatastoreEventArgument] = None


class VmBeingMigratedEvent(VmEvent):
   destHost: HostEventArgument
   destDatacenter: Optional[DatacenterEventArgument] = None
   destDatastore: Optional[DatastoreEventArgument] = None


class VmBeingRelocatedEvent(VmRelocateSpecEvent):
   destHost: HostEventArgument
   destDatacenter: Optional[DatacenterEventArgument] = None
   destDatastore: Optional[DatastoreEventArgument] = None

class VmCloneEvent(VmEvent):
   pass


class VmCloneFailedEvent(VmCloneEvent):
   destFolder: FolderEventArgument
   destName: str
   destHost: HostEventArgument
   reason: MethodFault

class VmClonedEvent(VmCloneEvent):
   sourceVm: VmEventArgument

class VmConfigMissingEvent(VmEvent):
   pass

class VmConnectedEvent(VmEvent):
   pass

class VmCreatedEvent(VmEvent):
   pass


class VmDasBeingResetEvent(VmEvent):
   class ReasonCode(Enum):
      vmtoolsHeartbeatFailure: ClassVar['ReasonCode'] = 'vmtoolsHeartbeatFailure'
      appHeartbeatFailure: ClassVar['ReasonCode'] = 'appHeartbeatFailure'
      appImmediateResetRequest: ClassVar['ReasonCode'] = 'appImmediateResetRequest'
      vmcpResetApdCleared: ClassVar['ReasonCode'] = 'vmcpResetApdCleared'
      guestOsCrashFailure: ClassVar['ReasonCode'] = 'guestOsCrashFailure'

   reason: Optional[str] = None

class VmDasBeingResetWithScreenshotEvent(VmDasBeingResetEvent):
   screenshotFilePath: str

class VmDasResetFailedEvent(VmEvent):
   pass

class VmDasUpdateErrorEvent(VmEvent):
   pass

class VmDasUpdateOkEvent(VmEvent):
   pass

class VmDateRolledBackEvent(VmEvent):
   pass


class VmDeployFailedEvent(VmEvent):
   destDatastore: EntityEventArgument
   reason: MethodFault

class VmDeployedEvent(VmEvent):
   srcTemplate: VmEventArgument

class VmDisconnectedEvent(VmEvent):
   pass

class VmDiscoveredEvent(VmEvent):
   pass


class VmDiskFailedEvent(VmEvent):
   disk: str
   reason: MethodFault

class VmEmigratingEvent(VmEvent):
   pass

class VmEndRecordingEvent(VmEvent):
   pass

class VmEndReplayingEvent(VmEvent):
   pass

class VmEvent(Event):
   template: bool


class VmEventArgument(EntityEventArgument):
   vm: VirtualMachine


class VmFailedMigrateEvent(VmEvent):
   destHost: HostEventArgument
   reason: MethodFault
   destDatacenter: Optional[DatacenterEventArgument] = None
   destDatastore: Optional[DatastoreEventArgument] = None


class VmFailedRelayoutEvent(VmEvent):
   reason: MethodFault

class VmFailedRelayoutOnVmfs2DatastoreEvent(VmEvent):
   pass


class VmFailedStartingSecondaryEvent(VmEvent):
   class FailureReason(Enum):
      incompatibleHost: ClassVar['FailureReason'] = 'incompatibleHost'
      loginFailed: ClassVar['FailureReason'] = 'loginFailed'
      registerVmFailed: ClassVar['FailureReason'] = 'registerVmFailed'
      migrateFailed: ClassVar['FailureReason'] = 'migrateFailed'

   reason: Optional[str] = None


class VmFailedToPowerOffEvent(VmEvent):
   reason: MethodFault


class VmFailedToPowerOnEvent(VmEvent):
   reason: MethodFault


class VmFailedToRebootGuestEvent(VmEvent):
   reason: MethodFault


class VmFailedToResetEvent(VmEvent):
   reason: MethodFault


class VmFailedToShutdownGuestEvent(VmEvent):
   reason: MethodFault


class VmFailedToStandbyGuestEvent(VmEvent):
   reason: MethodFault


class VmFailedToSuspendEvent(VmEvent):
   reason: MethodFault

class VmFailedUpdatingSecondaryConfig(VmEvent):
   pass


class VmFailoverFailed(VmEvent):
   reason: Optional[MethodFault] = None


class VmFaultToleranceStateChangedEvent(VmEvent):
   oldState: VirtualMachine.FaultToleranceState
   newState: VirtualMachine.FaultToleranceState

class VmFaultToleranceTurnedOffEvent(VmEvent):
   pass


class VmFaultToleranceVmTerminatedEvent(VmEvent):
   reason: Optional[str] = None

class VmGuestOSCrashedEvent(VmEvent):
   pass

class VmGuestRebootEvent(VmEvent):
   pass

class VmGuestShutdownEvent(VmEvent):
   pass

class VmGuestStandbyEvent(VmEvent):
   pass


class VmHealthMonitoringStateChangedEvent(ClusterEvent):
   state: str
   prevState: Optional[str] = None

class VmInstanceUuidAssignedEvent(VmEvent):
   instanceUuid: str

class VmInstanceUuidChangedEvent(VmEvent):
   oldInstanceUuid: str
   newInstanceUuid: str

class VmInstanceUuidConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   instanceUuid: str

class VmMacAssignedEvent(VmEvent):
   adapter: str
   mac: str

class VmMacChangedEvent(VmEvent):
   adapter: str
   oldMac: str
   newMac: str

class VmMacConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   mac: str

class VmMaxFTRestartCountReached(VmEvent):
   pass

class VmMaxRestartCountReached(VmEvent):
   pass


class VmMessageErrorEvent(VmEvent):
   message: str
   messageInfo: list[Message] = []


class VmMessageEvent(VmEvent):
   message: str
   messageInfo: list[Message] = []


class VmMessageWarningEvent(VmEvent):
   message: str
   messageInfo: list[Message] = []


class VmMigratedEvent(VmEvent):
   sourceHost: HostEventArgument
   sourceDatacenter: Optional[DatacenterEventArgument] = None
   sourceDatastore: Optional[DatastoreEventArgument] = None

class VmNoCompatibleHostForSecondaryEvent(VmEvent):
   pass

class VmNoNetworkAccessEvent(VmEvent):
   destHost: HostEventArgument

class VmOrphanedEvent(VmEvent):
   pass

class VmPowerOffOnIsolationEvent(VmPoweredOffEvent):
   isolatedHost: HostEventArgument

class VmPoweredOffEvent(VmEvent):
   pass

class VmPoweredOnEvent(VmEvent):
   pass

class VmPoweringOnWithCustomizedDVPortEvent(VmEvent):
   vnic: list[VnicPortArgument] = []


class VmPrimaryFailoverEvent(VmEvent):
   reason: Optional[str] = None


class VmReconfiguredEvent(VmEvent):
   configSpec: ConfigSpec
   configChanges: Optional[ChangesInfoEventArgument] = None

class VmRegisteredEvent(VmEvent):
   pass

class VmRelayoutSuccessfulEvent(VmEvent):
   pass

class VmRelayoutUpToDateEvent(VmEvent):
   pass

class VmReloadFromPathEvent(VmEvent):
   configPath: str

class VmReloadFromPathFailedEvent(VmEvent):
   configPath: str


class VmRelocateFailedEvent(VmRelocateSpecEvent):
   destHost: HostEventArgument
   reason: MethodFault
   destDatacenter: Optional[DatacenterEventArgument] = None
   destDatastore: Optional[DatastoreEventArgument] = None

class VmRelocateSpecEvent(VmEvent):
   pass


class VmRelocatedEvent(VmRelocateSpecEvent):
   sourceHost: HostEventArgument
   sourceDatacenter: Optional[DatacenterEventArgument] = None
   sourceDatastore: Optional[DatastoreEventArgument] = None

class VmRemoteConsoleConnectedEvent(VmEvent):
   pass

class VmRemoteConsoleDisconnectedEvent(VmEvent):
   pass

class VmRemovedEvent(VmEvent):
   pass

class VmRenamedEvent(VmEvent):
   oldName: str
   newName: str

class VmRequirementsExceedCurrentEVCModeEvent(VmEvent):
   pass

class VmResettingEvent(VmEvent):
   pass

class VmResourcePoolMovedEvent(VmEvent):
   oldParent: ResourcePoolEventArgument
   newParent: ResourcePoolEventArgument


class VmResourceReallocatedEvent(VmEvent):
   configChanges: Optional[ChangesInfoEventArgument] = None

class VmRestartedOnAlternateHostEvent(VmPoweredOnEvent):
   sourceHost: HostEventArgument

class VmResumingEvent(VmEvent):
   pass

class VmSecondaryAddedEvent(VmEvent):
   pass


class VmSecondaryDisabledBySystemEvent(VmEvent):
   reason: Optional[MethodFault] = None

class VmSecondaryDisabledEvent(VmEvent):
   pass

class VmSecondaryEnabledEvent(VmEvent):
   pass

class VmSecondaryStartedEvent(VmEvent):
   pass


class VmShutdownOnIsolationEvent(VmPoweredOffEvent):
   class Operation(Enum):
      shutdown: ClassVar['Operation'] = 'shutdown'
      poweredOff: ClassVar['Operation'] = 'poweredOff'

   isolatedHost: HostEventArgument
   shutdownResult: Optional[str] = None

class VmStartRecordingEvent(VmEvent):
   pass

class VmStartReplayingEvent(VmEvent):
   pass

class VmStartingEvent(VmEvent):
   pass

class VmStartingSecondaryEvent(VmEvent):
   pass

class VmStaticMacConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   mac: str

class VmStoppingEvent(VmEvent):
   pass

class VmSuspendedEvent(VmEvent):
   pass

class VmSuspendingEvent(VmEvent):
   pass


class VmTimedoutStartingSecondaryEvent(VmEvent):
   timeout: Optional[long] = None

class VmUnsupportedStartingEvent(VmStartingEvent):
   guestId: str

class VmUpgradeCompleteEvent(VmEvent):
   version: str

class VmUpgradeFailedEvent(VmEvent):
   pass

class VmUpgradingEvent(VmEvent):
   version: str

class VmUuidAssignedEvent(VmEvent):
   uuid: str

class VmUuidChangedEvent(VmEvent):
   oldUuid: str
   newUuid: str

class VmUuidConflictEvent(VmEvent):
   conflictedVm: VmEventArgument
   uuid: str


class VmVnicPoolReservationViolationClearEvent(DvsEvent):
   vmVnicResourcePoolKey: str
   vmVnicResourcePoolName: Optional[str] = None


class VmVnicPoolReservationViolationRaiseEvent(DvsEvent):
   vmVnicResourcePoolKey: str
   vmVnicResourcePoolName: Optional[str] = None


class VmWwnAssignedEvent(VmEvent):
   nodeWwns: list[long] = []
   portWwns: list[long] = []


class VmWwnChangedEvent(VmEvent):
   oldNodeWwns: list[long] = []
   oldPortWwns: list[long] = []
   newNodeWwns: list[long] = []
   newPortWwns: list[long] = []


class VmWwnConflictEvent(VmEvent):
   conflictedVms: list[VmEventArgument] = []
   conflictedHosts: list[HostEventArgument] = []
   wwn: long


class VnicPortArgument(DynamicData):
   vnic: str
   port: PortConnection

class WarningUpgradeEvent(UpgradeEvent):
   pass

class iScsiBootFailureEvent(HostEvent):
   pass
