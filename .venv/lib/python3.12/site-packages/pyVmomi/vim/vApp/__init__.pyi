# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem

from pyVmomi.vim import ImportSpec
from pyVmomi.vim import KeyValue
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import ResourceConfigSpec
from pyVmomi.vim import ResourcePool

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.ext import ManagedByInfo

from pyVmomi.vim.option import ArrayUpdateSpec



class CloneSpec(DynamicData):
   class NetworkMappingPair(DynamicData):
      source: Network
      destination: Network

   class ResourceMap(DynamicData):
      source: ManagedEntity
      parent: Optional[ResourcePool] = None
      resourceSpec: Optional[ResourceConfigSpec] = None
      location: Optional[Datastore] = None

   class ProvisioningType(Enum):
      sameAsSource: ClassVar['ProvisioningType'] = 'sameAsSource'
      thin: ClassVar['ProvisioningType'] = 'thin'
      thick: ClassVar['ProvisioningType'] = 'thick'

   location: Datastore
   host: Optional[HostSystem] = None
   resourceSpec: Optional[ResourceConfigSpec] = None
   vmFolder: Optional[Folder] = None
   networkMapping: list[NetworkMappingPair] = []
   property: list[KeyValue] = []
   resourceMapping: list[ResourceMap] = []
   provisioning: Optional[str] = None


class EntityConfigInfo(DynamicData):
   class Action(Enum):
      none: ClassVar['Action'] = 'none'
      powerOn: ClassVar['Action'] = 'powerOn'
      powerOff: ClassVar['Action'] = 'powerOff'
      guestShutdown: ClassVar['Action'] = 'guestShutdown'
      suspend: ClassVar['Action'] = 'suspend'

   key: Optional[ManagedEntity] = None
   tag: Optional[str] = None
   startOrder: Optional[int] = None
   startDelay: Optional[int] = None
   waitingForGuest: Optional[bool] = None
   startAction: Optional[str] = None
   stopDelay: Optional[int] = None
   stopAction: Optional[str] = None
   destroyWithParent: Optional[bool] = None


class IPAssignmentInfo(DynamicData):
   class IpAllocationPolicy(Enum):
      dhcpPolicy: ClassVar['IpAllocationPolicy'] = 'dhcpPolicy'
      transientPolicy: ClassVar['IpAllocationPolicy'] = 'transientPolicy'
      fixedPolicy: ClassVar['IpAllocationPolicy'] = 'fixedPolicy'
      fixedAllocatedPolicy: ClassVar['IpAllocationPolicy'] = 'fixedAllocatedPolicy'

   class AllocationSchemes(Enum):
      dhcp: ClassVar['AllocationSchemes'] = 'dhcp'
      ovfenv: ClassVar['AllocationSchemes'] = 'ovfenv'

   class Protocols(Enum):
      IPv4: ClassVar['Protocols'] = 'IPv4'
      IPv6: ClassVar['Protocols'] = 'IPv6'

   supportedAllocationScheme: list[str] = []
   ipAllocationPolicy: Optional[str] = None
   supportedIpProtocol: list[str] = []
   ipProtocol: Optional[str] = None


class IpPool(DynamicData):
   class IpPoolConfigInfo(DynamicData):
      subnetAddress: Optional[str] = None
      netmask: Optional[str] = None
      gateway: Optional[str] = None
      range: Optional[str] = None
      dns: list[str] = []
      dhcpServerAvailable: Optional[bool] = None
      ipPoolEnabled: Optional[bool] = None

   class Association(DynamicData):
      network: Optional[Network] = None
      networkName: str

   id: Optional[int] = None
   name: Optional[str] = None
   ipv4Config: Optional[IpPoolConfigInfo] = None
   ipv6Config: Optional[IpPoolConfigInfo] = None
   dnsDomain: Optional[str] = None
   dnsSearchPath: Optional[str] = None
   hostPrefix: Optional[str] = None
   httpProxy: Optional[str] = None
   networkAssociation: list[Association] = []
   availableIpv4Addresses: Optional[int] = None
   availableIpv6Addresses: Optional[int] = None
   allocatedIpv4Addresses: Optional[int] = None
   allocatedIpv6Addresses: Optional[int] = None


class OvfSectionInfo(DynamicData):
   key: Optional[int] = None
   namespace: Optional[str] = None
   type: Optional[str] = None
   atEnvelopeLevel: Optional[bool] = None
   contents: Optional[str] = None


class OvfSectionSpec(ArrayUpdateSpec):
   info: Optional[OvfSectionInfo] = None


class ProductInfo(DynamicData):
   key: int
   classId: Optional[str] = None
   instanceId: Optional[str] = None
   name: Optional[str] = None
   vendor: Optional[str] = None
   version: Optional[str] = None
   fullVersion: Optional[str] = None
   vendorUrl: Optional[str] = None
   productUrl: Optional[str] = None
   appUrl: Optional[str] = None


class ProductSpec(ArrayUpdateSpec):
   info: Optional[ProductInfo] = None


class PropertyInfo(DynamicData):
   key: int
   classId: Optional[str] = None
   instanceId: Optional[str] = None
   id: Optional[str] = None
   category: Optional[str] = None
   label: Optional[str] = None
   type: Optional[str] = None
   typeReference: Optional[str] = None
   userConfigurable: Optional[bool] = None
   defaultValue: Optional[str] = None
   value: Optional[str] = None
   description: Optional[str] = None


class PropertySpec(ArrayUpdateSpec):
   info: Optional[PropertyInfo] = None


class VAppConfigInfo(VmConfigInfo):
   entityConfig: list[EntityConfigInfo] = []
   annotation: str
   instanceUuid: Optional[str] = None
   managedBy: Optional[ManagedByInfo] = None


class VAppConfigSpec(VmConfigSpec):
   entityConfig: list[EntityConfigInfo] = []
   annotation: Optional[str] = None
   instanceUuid: Optional[str] = None
   managedBy: Optional[ManagedByInfo] = None


class VAppImportSpec(ImportSpec):
   name: str
   vAppConfigSpec: VAppConfigSpec
   resourcePoolSpec: ResourceConfigSpec
   child: list[ImportSpec] = []


class VmConfigInfo(DynamicData):
   product: list[ProductInfo] = []
   property: list[PropertyInfo] = []
   ipAssignment: IPAssignmentInfo
   eula: list[str] = []
   ovfSection: list[OvfSectionInfo] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: bool
   installBootStopDelay: int


class VmConfigSpec(DynamicData):
   product: list[ProductSpec] = []
   property: list[PropertySpec] = []
   ipAssignment: Optional[IPAssignmentInfo] = None
   eula: list[str] = []
   ovfSection: list[OvfSectionSpec] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: Optional[bool] = None
   installBootStopDelay: Optional[int] = None
