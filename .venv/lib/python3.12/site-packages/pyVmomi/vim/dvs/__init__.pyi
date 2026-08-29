# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import binary

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import BoolPolicy

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import HostSystem
from pyVmomi.vim import InheritablePolicy

from pyVmomi.vim import IntExpression
from pyVmomi.vim import IntPolicy
from pyVmomi.vim import IpAddress
from pyVmomi.vim import LongPolicy
from pyVmomi.vim import MacAddress
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import NegatableExpression
from pyVmomi.vim import Network
from pyVmomi.vim import NumericRange
from pyVmomi.vim import SelectionSet

from pyVmomi.vim import SharesInfo
from pyVmomi.vim import SingleIp
from pyVmomi.vim import StringExpression
from pyVmomi.vim import StringPolicy
from pyVmomi.vim import Task

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import ImportOperationBulkFault

from pyVmomi.vim.host import LinkDiscoveryProtocolConfig

from pyVmomi.vim.host import PhysicalNic



class DistributedVirtualPort(DynamicData):
   class ConfigSpec(DynamicData):
      operation: str
      key: Optional[str] = None
      name: Optional[str] = None
      scope: list[ManagedEntity] = []
      description: Optional[str] = None
      setting: Optional[Setting] = None
      configVersion: Optional[str] = None

   class ConfigInfo(DynamicData):
      name: Optional[str] = None
      scope: list[ManagedEntity] = []
      description: Optional[str] = None
      setting: Optional[Setting] = None
      configVersion: str

   class TrafficShapingPolicy(InheritablePolicy):
      enabled: Optional[BoolPolicy] = None
      averageBandwidth: Optional[LongPolicy] = None
      peakBandwidth: Optional[LongPolicy] = None
      burstSize: Optional[LongPolicy] = None

   class HostLocalPortInfo(DynamicData):
      switchUuid: str
      portKey: str
      setting: Setting
      vnic: str

   class VendorSpecificConfig(InheritablePolicy):
      keyValue: list[KeyedOpaqueBlob] = []

   class FilterParameter(DynamicData):
      parameters: list[str] = []

   class FilterOnFailure(Enum):
      failOpen: ClassVar['FilterOnFailure'] = 'failOpen'
      failClosed: ClassVar['FilterOnFailure'] = 'failClosed'

   class FilterConfig(InheritablePolicy):
      key: Optional[str] = None
      agentName: Optional[str] = None
      slotNumber: Optional[str] = None
      parameters: Optional[FilterParameter] = None
      onFailure: Optional[str] = None

   class TrafficFilterConfig(FilterConfig):
      trafficRuleset: Optional[TrafficRuleset] = None

   class FilterConfigSpec(FilterConfig):
      operation: str

   class TrafficFilterConfigSpec(TrafficFilterConfig):
      operation: str

   class FilterPolicy(InheritablePolicy):
      filterConfig: list[FilterConfig] = []

   class Setting(DynamicData):
      blocked: Optional[BoolPolicy] = None
      vmDirectPathGen2Allowed: Optional[BoolPolicy] = None
      inShapingPolicy: Optional[TrafficShapingPolicy] = None
      outShapingPolicy: Optional[TrafficShapingPolicy] = None
      vendorSpecificConfig: Optional[VendorSpecificConfig] = None
      networkResourcePoolKey: Optional[StringPolicy] = None
      filterPolicy: Optional[FilterPolicy] = None

   class RuntimeInfo(DynamicData):
      class VmDirectPathGen2InactiveReasonNetwork(Enum):
         portNptIncompatibleDvs: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptIncompatibleDvs'
         portNptNoCompatibleNics: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoCompatibleNics'
         portNptNoVirtualFunctionsAvailable: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoVirtualFunctionsAvailable'
         portNptDisabledForPort: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptDisabledForPort'

      class VmDirectPathGen2InactiveReasonOther(Enum):
         portNptIncompatibleHost: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleHost'
         portNptIncompatibleConnectee: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleConnectee'

      linkUp: bool
      blocked: bool
      vlanIds: list[NumericRange] = []
      trunkingMode: Optional[bool] = None
      mtu: Optional[int] = None
      linkPeer: Optional[str] = None
      macAddress: Optional[str] = None
      statusDetail: Optional[str] = None
      vmDirectPathGen2Active: Optional[bool] = None
      vmDirectPathGen2InactiveReasonNetwork: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: Optional[str] = None

   class State(DynamicData):
      runtimeInfo: Optional[RuntimeInfo] = None
      stats: PortStatistics
      vendorSpecificState: list[KeyedOpaqueBlob] = []

   key: str
   config: ConfigInfo
   dvsUuid: str
   portgroupKey: Optional[str] = None
   proxyHost: Optional[HostSystem] = None
   connectee: Optional[PortConnectee] = None
   conflict: bool
   conflictPortKey: Optional[str] = None
   state: Optional[State] = None
   connectionCookie: Optional[int] = None
   lastStatusChange: datetime
   hostLocalPort: Optional[bool] = None
   externalId: Optional[str] = None
   segmentPortId: Optional[str] = None


class DistributedVirtualPortgroup(Network):
   class PortgroupType(Enum):
      earlyBinding: ClassVar['PortgroupType'] = 'earlyBinding'
      lateBinding: ClassVar['PortgroupType'] = 'lateBinding'
      ephemeral: ClassVar['PortgroupType'] = 'ephemeral'

   class BackingType(Enum):
      standard: ClassVar['BackingType'] = 'standard'
      nsx: ClassVar['BackingType'] = 'nsx'

   class PortgroupPolicy(DynamicData):
      blockOverrideAllowed: bool
      shapingOverrideAllowed: bool
      vendorConfigOverrideAllowed: bool
      livePortMovingAllowed: bool
      portConfigResetAtDisconnect: bool
      networkResourcePoolOverrideAllowed: Optional[bool] = None
      trafficFilterOverrideAllowed: Optional[bool] = None

   class MetaTagName(Enum):
      dvsName: ClassVar['MetaTagName'] = 'dvsName'
      portgroupName: ClassVar['MetaTagName'] = 'portgroupName'
      portIndex: ClassVar['MetaTagName'] = 'portIndex'

   class SubnetAddressInfo(DynamicData):
      cidr: list[str] = []

   class NsxConfig(DynamicData):
      vlanIdExtended: Optional[int] = None
      subnetAddresses: Optional[SubnetAddressInfo] = None
      spanIds: list[str] = []

   class ConfigSpec(DynamicData):
      configVersion: Optional[str] = None
      name: Optional[str] = None
      numPorts: Optional[int] = None
      portNameFormat: Optional[str] = None
      defaultPortConfig: Optional[DistributedVirtualPort.Setting] = None
      description: Optional[str] = None
      type: Optional[str] = None
      backingType: Optional[str] = None
      scope: list[ManagedEntity] = []
      policy: Optional[PortgroupPolicy] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      autoExpand: Optional[bool] = None
      vmVnicNetworkResourcePoolKey: Optional[str] = None
      transportZoneUuid: Optional[str] = None
      transportZoneName: Optional[str] = None
      logicalSwitchUuid: Optional[str] = None
      segmentId: Optional[str] = None
      subnetId: Optional[str] = None
      nsxConfig: Optional[NsxConfig] = None

   class ConfigInfo(DynamicData):
      key: str
      name: str
      numPorts: int
      distributedVirtualSwitch: Optional[DistributedVirtualSwitch] = None
      defaultPortConfig: Optional[DistributedVirtualPort.Setting] = None
      description: Optional[str] = None
      type: str
      backingType: Optional[str] = None
      policy: PortgroupPolicy
      portNameFormat: Optional[str] = None
      scope: list[ManagedEntity] = []
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      configVersion: Optional[str] = None
      autoExpand: Optional[bool] = None
      vmVnicNetworkResourcePoolKey: Optional[str] = None
      uplink: Optional[bool] = None
      transportZoneUuid: Optional[str] = None
      transportZoneName: Optional[str] = None
      logicalSwitchUuid: Optional[str] = None
      segmentId: Optional[str] = None
      subnetId: Optional[str] = None
      nsxConfig: Optional[NsxConfig] = None

   class Problem(DynamicData):
      logicalSwitchUuid: str
      fault: MethodFault

   class NsxPortgroupOperationResult(DynamicData):
      portgroups: list[DistributedVirtualPortgroup] = []
      problems: list[Problem] = []

   @property
   def key(self) -> str: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def portKeys(self) -> list[str]: ...

   def Reconfigure(self, spec: ConfigSpec) -> Task: ...
   def Rollback(self, entityBackup: Optional[EntityBackup.Config]) -> Task: ...


class DistributedVirtualPortgroupInfo(DynamicData):
   switchName: str
   switchUuid: str
   portgroupName: str
   portgroupKey: str
   portgroupType: str
   uplinkPortgroup: bool
   portgroup: DistributedVirtualPortgroup
   networkReservationSupported: Optional[bool] = None
   backingType: Optional[str] = None
   logicalSwitchUuid: Optional[str] = None
   segmentId: Optional[str] = None
   subnetId: Optional[str] = None


class DistributedVirtualPortgroupSelection(SelectionSet):
   dvsUuid: str
   portgroupKey: list[str] = []


class DistributedVirtualSwitchInfo(DynamicData):
   switchName: str
   switchUuid: str
   distributedVirtualSwitch: DistributedVirtualSwitch
   networkReservationSupported: Optional[bool] = None


class DistributedVirtualSwitchManager(ManagedObject):
   class PhysicalNicsList(DynamicData):
      host: HostSystem
      physicalNics: list[PhysicalNic] = []

   class DvsConfigTarget(DynamicData):
      distributedVirtualPortgroup: list[DistributedVirtualPortgroupInfo] = []
      distributedVirtualSwitch: list[DistributedVirtualSwitchInfo] = []

   class CompatibilityResult(DynamicData):
      host: HostSystem
      error: list[MethodFault] = []

   class HostContainer(DynamicData):
      container: ManagedEntity
      recursive: bool

   class HostDvsFilterSpec(DynamicData):
      inclusive: bool

   class HostArrayFilter(HostDvsFilterSpec):
      host: list[HostSystem] = []

   class HostContainerFilter(HostDvsFilterSpec):
      hostContainer: HostContainer

   class HostDvsMembershipFilter(HostDvsFilterSpec):
      distributedVirtualSwitch: DistributedVirtualSwitch

   class DvsProductSpec(DynamicData):
      newSwitchProductSpec: Optional[ProductSpec] = None
      distributedVirtualSwitch: Optional[DistributedVirtualSwitch] = None

   class ImportResult(DynamicData):
      distributedVirtualSwitch: list[DistributedVirtualSwitch] = []
      distributedVirtualPortgroup: list[DistributedVirtualPortgroup] = []
      importFault: list[ImportOperationBulkFault.FaultOnImport] = []

   class SpanInfo(DynamicData):
      ID: str
      clusters: list[ClusterComputeResource] = []
      exclusive: Optional[bool] = None

   def QuerySupportedSwitchSpec(self, recommended: Optional[bool]) -> list[ProductSpec]: ...
   def QuerySupportedNetworkOffloadSpec(self, switchProductSpec: ProductSpec) -> list[NetworkOffloadSpec]: ...
   def QueryCompatibleVmnicsFromHosts(self, hosts: list[HostSystem], dvs: DistributedVirtualSwitch) -> list[PhysicalNicsList]: ...
   def QueryCompatibleHostForNewDvs(self, container: ManagedEntity, recursive: bool, switchProductSpec: Optional[ProductSpec]) -> list[HostSystem]: ...
   def QueryCompatibleHostForExistingDvs(self, container: ManagedEntity, recursive: bool, dvs: DistributedVirtualSwitch) -> list[HostSystem]: ...
   def QueryCompatibleHostSpec(self, switchProductSpec: Optional[ProductSpec]) -> list[HostProductSpec]: ...
   def QueryFeatureCapability(self, switchProductSpec: Optional[ProductSpec]) -> Optional[DistributedVirtualSwitch.FeatureCapability]: ...
   def QuerySwitchByUuid(self, uuid: str) -> Optional[DistributedVirtualSwitch]: ...
   def QueryDvsConfigTarget(self, host: Optional[HostSystem], dvs: Optional[DistributedVirtualSwitch]) -> DvsConfigTarget: ...
   def CheckCompatibility(self, hostContainer: HostContainer, dvsProductSpec: Optional[DvsProductSpec], hostFilterSpec: list[HostDvsFilterSpec]) -> list[CompatibilityResult]: ...
   def RectifyHost(self, hosts: list[HostSystem]) -> Task: ...
   def ExportEntity(self, selectionSet: list[SelectionSet]) -> Task: ...
   def ImportEntity(self, entityBackup: list[EntityBackup.Config], importType: str) -> Task: ...
   def LookupPortgroup(self, switchUuid: str, portgroupKey: str) -> Optional[DistributedVirtualPortgroup]: ...
   def GetVpcNetworkSpan(self, spanId: Optional[str]) -> list[SpanInfo]: ...


class DistributedVirtualSwitchSelection(SelectionSet):
   dvsUuid: str


class EntityBackup(DynamicData):
   class Config(DynamicData):
      entityType: str
      configBlob: binary
      key: Optional[str] = None
      name: Optional[str] = None
      container: Optional[ManagedEntity] = None
      configVersion: Optional[str] = None

   class EntityType(Enum):
      distributedVirtualSwitch: ClassVar['EntityType'] = 'distributedVirtualSwitch'
      distributedVirtualPortgroup: ClassVar['EntityType'] = 'distributedVirtualPortgroup'

   class ImportType(Enum):
      createEntityWithNewIdentifier: ClassVar['ImportType'] = 'createEntityWithNewIdentifier'
      createEntityWithOriginalIdentifier: ClassVar['ImportType'] = 'createEntityWithOriginalIdentifier'
      applyToEntitySpecified: ClassVar['ImportType'] = 'applyToEntitySpecified'


class HostMember(DynamicData):
   class HostComponentState(Enum):
      up: ClassVar['HostComponentState'] = 'up'
      pending: ClassVar['HostComponentState'] = 'pending'
      outOfSync: ClassVar['HostComponentState'] = 'outOfSync'
      warning: ClassVar['HostComponentState'] = 'warning'
      disconnected: ClassVar['HostComponentState'] = 'disconnected'
      down: ClassVar['HostComponentState'] = 'down'

   class ConfigSpec(DynamicData):
      operation: str
      host: HostSystem
      backing: Optional[Backing] = None
      maxProxySwitchPorts: Optional[int] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []

   class PnicSpec(DynamicData):
      pnicDevice: str
      uplinkPortKey: Optional[str] = None
      uplinkPortgroupKey: Optional[str] = None
      connectionCookie: Optional[int] = None

   class Backing(DynamicData):
      pass

   class PnicBacking(Backing):
      pnicSpec: list[PnicSpec] = []

   class RuntimeState(DynamicData):
      currentMaxProxySwitchPorts: int

   class TransportZoneType(Enum):
      vlan: ClassVar['TransportZoneType'] = 'vlan'
      overlay: ClassVar['TransportZoneType'] = 'overlay'

   class TransportZoneInfo(DynamicData):
      uuid: str
      type: str

   class ConfigInfo(DynamicData):
      host: Optional[HostSystem] = None
      maxProxySwitchPorts: int
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      backing: Backing
      nsxSwitch: Optional[bool] = None
      ensEnabled: Optional[bool] = None
      ensInterruptEnabled: Optional[bool] = None
      transportZones: list[TransportZoneInfo] = []
      nsxtUsedUplinkNames: list[str] = []
      networkOffloadingEnabled: Optional[bool] = None
      teplessMode: Optional[bool] = None

   class HostUplinkState(DynamicData):
      class State(Enum):
         active: ClassVar['State'] = 'active'
         standby: ClassVar['State'] = 'standby'

      uplinkName: str
      state: str

   class HostPerfNicOffloadState(DynamicData):
      class Status(Enum):
         SUCCEEDED: ClassVar['Status'] = 'SUCCEEDED'
         IN_PROGRESS: ClassVar['Status'] = 'IN_PROGRESS'
         FAILED: ClassVar['Status'] = 'FAILED'

      enabled: bool
      runtimeStatus: Optional[str] = None
      statusDescription: Optional[str] = None

   class RuntimeInfo(DynamicData):
      host: HostSystem
      status: Optional[str] = None
      statusDetail: Optional[str] = None
      nsxtStatus: Optional[str] = None
      nsxtStatusDetail: Optional[str] = None
      healthCheckResult: list[HealthCheckResult] = []
      hostUplinkState: list[HostUplinkState] = []
      hostPerfNicOffloadState: Optional[HostPerfNicOffloadState] = None

   class HealthCheckResult(DynamicData):
      summary: Optional[str] = None

   class UplinkHealthCheckResult(HealthCheckResult):
      uplinkPortKey: str

   runtimeState: Optional[RuntimeState] = None
   config: ConfigInfo
   productInfo: Optional[ProductSpec] = None
   uplinkPortKey: list[str] = []
   status: str
   statusDetail: Optional[str] = None


class HostProductSpec(DynamicData):
   productLineId: Optional[str] = None
   version: Optional[str] = None


class KeyedOpaqueBlob(DynamicData):
   key: str
   opaqueData: str


class NetworkOffloadSpec(DynamicData):
   id: str
   name: Optional[str] = None
   types: list[str] = []
   dpuCapability: Optional[VmwareDistributedVirtualSwitch.DpuFeatureCapability] = None


class NetworkResourcePool(DynamicData):
   class AllocationInfo(DynamicData):
      limit: Optional[long] = None
      shares: Optional[SharesInfo] = None
      priorityTag: Optional[int] = None

   class ConfigSpec(DynamicData):
      key: str
      configVersion: Optional[str] = None
      allocationInfo: Optional[AllocationInfo] = None
      name: Optional[str] = None
      description: Optional[str] = None

   key: str
   name: Optional[str] = None
   description: Optional[str] = None
   configVersion: str
   allocationInfo: AllocationInfo


class PortConnectee(DynamicData):
   class ConnecteeType(Enum):
      pnic: ClassVar['ConnecteeType'] = 'pnic'
      vmVnic: ClassVar['ConnecteeType'] = 'vmVnic'
      hostConsoleVnic: ClassVar['ConnecteeType'] = 'hostConsoleVnic'
      hostVmkVnic: ClassVar['ConnecteeType'] = 'hostVmkVnic'
      systemCrxVnic: ClassVar['ConnecteeType'] = 'systemCrxVnic'

   connectedEntity: Optional[ManagedEntity] = None
   nicKey: Optional[str] = None
   type: Optional[str] = None
   addressHint: Optional[str] = None


class PortConnection(DynamicData):
   switchUuid: str
   portgroupKey: Optional[str] = None
   portKey: Optional[str] = None
   connectionCookie: Optional[int] = None


class PortCriteria(DynamicData):
   connected: Optional[bool] = None
   active: Optional[bool] = None
   uplinkPort: Optional[bool] = None
   nsxPort: Optional[bool] = None
   scope: Optional[ManagedEntity] = None
   portgroupKey: list[str] = []
   inside: Optional[bool] = None
   portKey: list[str] = []
   host: list[HostSystem] = []


class PortStatistics(DynamicData):
   packetsInMulticast: long
   packetsOutMulticast: long
   bytesInMulticast: long
   bytesOutMulticast: long
   packetsInUnicast: long
   packetsOutUnicast: long
   bytesInUnicast: long
   bytesOutUnicast: long
   packetsInBroadcast: long
   packetsOutBroadcast: long
   bytesInBroadcast: long
   bytesOutBroadcast: long
   packetsInDropped: long
   packetsOutDropped: long
   packetsInException: long
   packetsOutException: long
   bytesInFromPnic: Optional[long] = None
   bytesOutToPnic: Optional[long] = None


class ProductSpec(DynamicData):
   name: Optional[str] = None
   vendor: Optional[str] = None
   version: Optional[str] = None
   build: Optional[str] = None
   forwardingClass: Optional[str] = None
   bundleId: Optional[str] = None
   bundleUrl: Optional[str] = None


class TrafficRule(DynamicData):
   class Qualifier(DynamicData):
      key: Optional[str] = None

   class Action(DynamicData):
      pass

   class RuleDirectionType(Enum):
      incomingPackets: ClassVar['RuleDirectionType'] = 'incomingPackets'
      outgoingPackets: ClassVar['RuleDirectionType'] = 'outgoingPackets'
      both: ClassVar['RuleDirectionType'] = 'both'

   class IpQualifier(Qualifier):
      sourceAddress: Optional[IpAddress] = None
      destinationAddress: Optional[IpAddress] = None
      protocol: Optional[IntExpression] = None
      sourceIpPort: Optional[IpPort] = None
      destinationIpPort: Optional[IpPort] = None
      tcpFlags: Optional[IntExpression] = None

   class IpPort(NegatableExpression):
      pass

   class SingleIpPort(IpPort):
      portNumber: int

   class IpPortRange(IpPort):
      startPortNumber: int
      endPortNumber: int

   class MacQualifier(Qualifier):
      sourceAddress: Optional[MacAddress] = None
      destinationAddress: Optional[MacAddress] = None
      protocol: Optional[IntExpression] = None
      vlanId: Optional[IntExpression] = None

   class SystemTrafficQualifier(Qualifier):
      typeOfSystemTraffic: Optional[StringExpression] = None

   class DropAction(Action):
      pass

   class AcceptAction(Action):
      pass

   class UpdateTagAction(Action):
      qosTag: Optional[int] = None
      dscpTag: Optional[int] = None

   class RateLimitAction(Action):
      packetsPerSecond: int

   class LogAction(Action):
      pass

   class GreAction(Action):
      encapsulationIp: SingleIp

   class MacRewriteAction(Action):
      rewriteMac: str

   class PuntAction(Action):
      pass

   class CopyAction(Action):
      pass

   key: Optional[str] = None
   description: Optional[str] = None
   sequence: Optional[int] = None
   qualifier: list[Qualifier] = []
   action: Optional[Action] = None
   direction: Optional[str] = None


class TrafficRuleset(DynamicData):
   key: Optional[str] = None
   enabled: Optional[bool] = None
   precedence: Optional[int] = None
   rules: list[TrafficRule] = []


class VmVnicNetworkResourcePool(DynamicData):
   class ResourceAllocation(DynamicData):
      reservationQuota: Optional[long] = None

   class ConfigSpec(DynamicData):
      operation: str
      key: Optional[str] = None
      configVersion: Optional[str] = None
      allocationInfo: Optional[ResourceAllocation] = None
      name: Optional[str] = None
      description: Optional[str] = None

   class VnicAllocatedResource(DynamicData):
      vm: VirtualMachine
      vnicKey: str
      reservation: Optional[long] = None

   class RuntimeInfo(DynamicData):
      key: str
      name: Optional[str] = None
      capacity: Optional[int] = None
      usage: Optional[int] = None
      available: Optional[int] = None
      status: str
      allocatedResource: list[VnicAllocatedResource] = []

   key: str
   name: Optional[str] = None
   description: Optional[str] = None
   configVersion: str
   allocationInfo: Optional[ResourceAllocation] = None


class VmwareDistributedVirtualSwitch(DistributedVirtualSwitch):
   class FeatureCapability(DistributedVirtualSwitch.FeatureCapability):
      vspanSupported: Optional[bool] = None
      lldpSupported: Optional[bool] = None
      ipfixSupported: Optional[bool] = None
      ipfixCapability: Optional[IpfixFeatureCapability] = None
      multicastSnoopingSupported: Optional[bool] = None
      vspanCapability: Optional[VspanFeatureCapability] = None
      lacpCapability: Optional[LacpFeatureCapability] = None
      dpuCapability: Optional[DpuFeatureCapability] = None
      nsxSupported: Optional[bool] = None
      mtuCapability: Optional[MtuCapability] = None
      realTimeConfigSupported: Optional[bool] = None
      perfNicOffloadCapability: Optional[PerfNicOffloadFeatureCapability] = None
      systemTrafficCapabilities: Optional[SystemTrafficCapabilities] = None

   class IpfixFeatureCapability(DynamicData):
      ipfixSupported: Optional[bool] = None
      ipv6ForIpfixSupported: Optional[bool] = None
      observationDomainIdSupported: Optional[bool] = None

   class LacpFeatureCapability(DynamicData):
      lacpSupported: Optional[bool] = None
      multiLacpGroupSupported: Optional[bool] = None
      lacpFastModeSupported: Optional[bool] = None

   class DpuFeatureCapability(DynamicData):
      networkOffloadSupported: Optional[bool] = None
      activeStandbyModeSupported: Optional[bool] = None

   class PerfNicOffloadFeatureCapability(DynamicData):
      supported: Optional[bool] = None

   class SystemTrafficCapabilities(DynamicData):
      systemTrafficQualifiers: list[str] = []

   class VmwareHealthCheckFeatureCapability(DistributedVirtualSwitch.HealthCheckFeatureCapability):
      vlanMtuSupported: bool
      teamingSupported: bool

   class VspanFeatureCapability(DynamicData):
      mixedDestSupported: bool
      dvportSupported: bool
      remoteSourceSupported: bool
      remoteDestSupported: bool
      encapRemoteSourceSupported: bool
      erspanProtocolSupported: Optional[bool] = None
      mirrorNetstackSupported: Optional[bool] = None

   class MtuCapability(DynamicData):
      minMtuSupported: int
      maxMtuSupported: int

   class VspanPorts(DynamicData):
      portKey: list[str] = []
      uplinkPortName: list[str] = []
      wildcardPortConnecteeType: list[str] = []
      vlans: list[int] = []
      ipAddress: list[str] = []

   class VspanSession(DynamicData):
      key: Optional[str] = None
      name: Optional[str] = None
      description: Optional[str] = None
      enabled: bool
      sourcePortTransmitted: Optional[VspanPorts] = None
      sourcePortReceived: Optional[VspanPorts] = None
      destinationPort: Optional[VspanPorts] = None
      encapsulationVlanId: Optional[int] = None
      stripOriginalVlan: bool
      mirroredPacketLength: Optional[int] = None
      normalTrafficAllowed: bool
      sessionType: Optional[str] = None
      samplingRate: Optional[int] = None
      encapType: Optional[str] = None
      erspanId: Optional[int] = None
      erspanCOS: Optional[int] = None
      erspanGraNanosec: Optional[bool] = None
      netstack: Optional[str] = None

   class IpfixConfig(DynamicData):
      collectorIpAddress: Optional[str] = None
      collectorPort: Optional[int] = None
      observationDomainId: Optional[long] = None
      activeFlowTimeout: int
      idleFlowTimeout: Optional[int] = None
      samplingRate: int
      internalFlowsOnly: bool

   class DpuFailoverPolicy(DynamicData):
      activeUplink: list[str] = []
      standbyUplink: list[str] = []

   class NetworkOffloadConfig(DynamicData):
      dpuFailoverPolicy: Optional[DpuFailoverPolicy] = None

   class RealTimeLanAnnotation(DynamicData):
      lanAUplink: list[str] = []
      lanBUplink: list[str] = []

   class RealTimeConfig(DynamicData):
      allowed: Optional[bool] = None
      lanAnnotation: Optional[RealTimeLanAnnotation] = None

   class ConfigInfo(DistributedVirtualSwitch.ConfigInfo):
      vspanSession: list[VspanSession] = []
      pvlanConfig: list[PvlanMapEntry] = []
      maxMtu: int
      linkDiscoveryProtocolConfig: Optional[LinkDiscoveryProtocolConfig] = None
      ipfixConfig: Optional[IpfixConfig] = None
      lacpGroupConfig: list[LacpGroupConfig] = []
      lacpApiVersion: Optional[str] = None
      multicastFilteringMode: Optional[str] = None
      networkOffloadSpecId: Optional[str] = None
      networkOffloadConfig: Optional[NetworkOffloadConfig] = None
      realTimeConfig: Optional[RealTimeConfig] = None

   class ConfigSpec(DistributedVirtualSwitch.ConfigSpec):
      pvlanConfigSpec: list[PvlanConfigSpec] = []
      vspanConfigSpec: list[VspanConfigSpec] = []
      maxMtu: Optional[int] = None
      linkDiscoveryProtocolConfig: Optional[LinkDiscoveryProtocolConfig] = None
      ipfixConfig: Optional[IpfixConfig] = None
      lacpApiVersion: Optional[str] = None
      multicastFilteringMode: Optional[str] = None
      networkOffloadSpecId: Optional[str] = None
      networkOffloadConfig: Optional[NetworkOffloadConfig] = None
      realTimeConfig: Optional[RealTimeConfig] = None

   class UplinkPortOrderPolicy(InheritablePolicy):
      activeUplinkPort: list[str] = []
      standbyUplinkPort: list[str] = []

   class FailureCriteria(InheritablePolicy):
      checkSpeed: Optional[StringPolicy] = None
      speed: Optional[IntPolicy] = None
      checkDuplex: Optional[BoolPolicy] = None
      fullDuplex: Optional[BoolPolicy] = None
      checkErrorPercent: Optional[BoolPolicy] = None
      percentage: Optional[IntPolicy] = None
      checkBeacon: Optional[BoolPolicy] = None

   class UplinkPortTeamingPolicy(InheritablePolicy):
      policy: Optional[StringPolicy] = None
      reversePolicy: Optional[BoolPolicy] = None
      notifySwitches: Optional[BoolPolicy] = None
      rollingOrder: Optional[BoolPolicy] = None
      failureCriteria: Optional[FailureCriteria] = None
      uplinkPortOrder: Optional[UplinkPortOrderPolicy] = None

   class VlanSpec(InheritablePolicy):
      pass

   class PvlanSpec(VlanSpec):
      pvlanId: int

   class VlanIdSpec(VlanSpec):
      vlanId: int

   class TrunkVlanSpec(VlanSpec):
      vlanId: list[NumericRange] = []

   class SecurityPolicy(InheritablePolicy):
      allowPromiscuous: Optional[BoolPolicy] = None
      macChanges: Optional[BoolPolicy] = None
      forgedTransmits: Optional[BoolPolicy] = None

   class MacLimitPolicyType(Enum):
      allow: ClassVar['MacLimitPolicyType'] = 'allow'
      drop: ClassVar['MacLimitPolicyType'] = 'drop'

   class MacLearningPolicy(InheritablePolicy):
      enabled: bool
      allowUnicastFlooding: Optional[bool] = None
      limit: Optional[int] = None
      limitPolicy: Optional[str] = None

   class MacManagementPolicy(InheritablePolicy):
      allowPromiscuous: Optional[bool] = None
      macChanges: Optional[bool] = None
      forgedTransmits: Optional[bool] = None
      macLearningPolicy: Optional[MacLearningPolicy] = None

   class VmwarePortConfigPolicy(DistributedVirtualPort.Setting):
      vlan: Optional[VlanSpec] = None
      qosTag: Optional[IntPolicy] = None
      uplinkTeamingPolicy: Optional[UplinkPortTeamingPolicy] = None
      securityPolicy: Optional[SecurityPolicy] = None
      ipfixEnabled: Optional[BoolPolicy] = None
      txUplink: Optional[BoolPolicy] = None
      lacpPolicy: Optional[UplinkLacpPolicy] = None
      macManagementPolicy: Optional[MacManagementPolicy] = None
      VNI: Optional[IntPolicy] = None

   class VMwarePortgroupPolicy(DistributedVirtualPortgroup.PortgroupPolicy):
      vlanOverrideAllowed: bool
      uplinkTeamingOverrideAllowed: bool
      securityPolicyOverrideAllowed: bool
      ipfixOverrideAllowed: Optional[bool] = None
      macManagementOverrideAllowed: Optional[bool] = None

   class PvlanPortType(Enum):
      promiscuous: ClassVar['PvlanPortType'] = 'promiscuous'
      isolated: ClassVar['PvlanPortType'] = 'isolated'
      community: ClassVar['PvlanPortType'] = 'community'

   class PvlanConfigSpec(DynamicData):
      pvlanEntry: PvlanMapEntry
      operation: str

   class PvlanMapEntry(DynamicData):
      primaryVlanId: int
      secondaryVlanId: int
      pvlanType: str

   class VspanConfigSpec(DynamicData):
      vspanSession: VspanSession
      operation: str

   class VspanSessionEncapType(Enum):
      gre: ClassVar['VspanSessionEncapType'] = 'gre'
      erspan2: ClassVar['VspanSessionEncapType'] = 'erspan2'
      erspan3: ClassVar['VspanSessionEncapType'] = 'erspan3'

   class VspanSessionType(Enum):
      mixedDestMirror: ClassVar['VspanSessionType'] = 'mixedDestMirror'
      dvPortMirror: ClassVar['VspanSessionType'] = 'dvPortMirror'
      remoteMirrorSource: ClassVar['VspanSessionType'] = 'remoteMirrorSource'
      remoteMirrorDest: ClassVar['VspanSessionType'] = 'remoteMirrorDest'
      encapsulatedRemoteMirrorSource: ClassVar['VspanSessionType'] = 'encapsulatedRemoteMirrorSource'

   class VmwareHealthCheckConfig(DistributedVirtualSwitch.HealthCheckConfig):
      pass

   class VlanMtuHealthCheckConfig(VmwareHealthCheckConfig):
      pass

   class TeamingHealthCheckConfig(VmwareHealthCheckConfig):
      pass

   class VlanHealthCheckResult(HostMember.UplinkHealthCheckResult):
      trunkedVlan: list[NumericRange] = []
      untrunkedVlan: list[NumericRange] = []

   class MtuHealthCheckResult(HostMember.UplinkHealthCheckResult):
      mtuMismatch: bool
      vlanSupportSwitchMtu: list[NumericRange] = []
      vlanNotSupportSwitchMtu: list[NumericRange] = []

   class TeamingMatchStatus(Enum):
      iphashMatch: ClassVar['TeamingMatchStatus'] = 'iphashMatch'
      nonIphashMatch: ClassVar['TeamingMatchStatus'] = 'nonIphashMatch'
      iphashMismatch: ClassVar['TeamingMatchStatus'] = 'iphashMismatch'
      nonIphashMismatch: ClassVar['TeamingMatchStatus'] = 'nonIphashMismatch'

   class TeamingHealthCheckResult(HostMember.HealthCheckResult):
      teamingStatus: str

   class UplinkLacpPolicy(InheritablePolicy):
      enable: Optional[BoolPolicy] = None
      mode: Optional[StringPolicy] = None

   class LacpGroupConfig(DynamicData):
      key: Optional[str] = None
      name: Optional[str] = None
      mode: Optional[str] = None
      uplinkNum: Optional[int] = None
      loadbalanceAlgorithm: Optional[str] = None
      vlan: Optional[LagVlanConfig] = None
      ipfix: Optional[LagIpfixConfig] = None
      uplinkName: list[str] = []
      uplinkPortKey: list[str] = []
      timeoutMode: Optional[str] = None

   class LagVlanConfig(DynamicData):
      vlanId: list[NumericRange] = []

   class LagIpfixConfig(DynamicData):
      ipfixEnabled: Optional[bool] = None

   class UplinkLacpMode(Enum):
      active: ClassVar['UplinkLacpMode'] = 'active'
      passive: ClassVar['UplinkLacpMode'] = 'passive'

   class UplinkLacpTimeoutMode(Enum):
      fast: ClassVar['UplinkLacpTimeoutMode'] = 'fast'
      slow: ClassVar['UplinkLacpTimeoutMode'] = 'slow'

   class LacpGroupSpec(DynamicData):
      lacpGroupConfig: LacpGroupConfig
      operation: str

   class LacpLoadBalanceAlgorithm(Enum):
      srcMac: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcMac'
      destMac: ClassVar['LacpLoadBalanceAlgorithm'] = 'destMac'
      srcDestMac: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestMac'
      destIpVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpVlan'
      srcIpVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpVlan'
      srcDestIpVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpVlan'
      destTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'destTcpUdpPort'
      srcTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcTcpUdpPort'
      srcDestTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestTcpUdpPort'
      destIpTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPort'
      srcIpTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPort'
      srcDestIpTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPort'
      destIpTcpUdpPortVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPortVlan'
      srcIpTcpUdpPortVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPortVlan'
      srcDestIpTcpUdpPortVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPortVlan'
      destIp: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIp'
      srcIp: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIp'
      srcDestIp: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIp'
      vlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'vlan'
      srcPortId: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcPortId'

   class LacpApiVersion(Enum):
      singleLag: ClassVar['LacpApiVersion'] = 'singleLag'
      multipleLag: ClassVar['LacpApiVersion'] = 'multipleLag'

   class MulticastFilteringMode(Enum):
      legacyFiltering: ClassVar['MulticastFilteringMode'] = 'legacyFiltering'
      snooping: ClassVar['MulticastFilteringMode'] = 'snooping'

   def UpdateLacpGroupConfig(self, lacpGroupSpec: list[LacpGroupSpec]) -> Task: ...
