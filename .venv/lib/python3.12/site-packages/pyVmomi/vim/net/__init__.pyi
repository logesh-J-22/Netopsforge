# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData



class DhcpConfigInfo(DynamicData):
   class DhcpOptions(DynamicData):
      enable: bool
      config: list[KeyValue] = []

   ipv6: Optional[DhcpOptions] = None
   ipv4: Optional[DhcpOptions] = None


class DhcpConfigSpec(DynamicData):
   class DhcpOptionsSpec(DynamicData):
      enable: Optional[bool] = None
      config: list[KeyValue] = []
      operation: str

   ipv6: Optional[DhcpOptionsSpec] = None
   ipv4: Optional[DhcpOptionsSpec] = None


class DnsConfigInfo(DynamicData):
   dhcp: bool
   hostName: str
   domainName: str
   ipAddress: list[str] = []
   searchDomain: list[str] = []


class DnsConfigSpec(DynamicData):
   dhcp: Optional[bool] = None
   hostName: Optional[str] = None
   domainName: Optional[str] = None
   ipAddress: list[str] = []
   searchDomain: list[str] = []


class IpConfigInfo(DynamicData):
   class IpAddressOrigin(Enum):
      other: ClassVar['IpAddressOrigin'] = 'other'
      manual: ClassVar['IpAddressOrigin'] = 'manual'
      dhcp: ClassVar['IpAddressOrigin'] = 'dhcp'
      linklayer: ClassVar['IpAddressOrigin'] = 'linklayer'
      random: ClassVar['IpAddressOrigin'] = 'random'

   class IpAddressStatus(Enum):
      preferred: ClassVar['IpAddressStatus'] = 'preferred'
      deprecated: ClassVar['IpAddressStatus'] = 'deprecated'
      invalid: ClassVar['IpAddressStatus'] = 'invalid'
      inaccessible: ClassVar['IpAddressStatus'] = 'inaccessible'
      unknown: ClassVar['IpAddressStatus'] = 'unknown'
      tentative: ClassVar['IpAddressStatus'] = 'tentative'
      duplicate: ClassVar['IpAddressStatus'] = 'duplicate'

   class IpAddress(DynamicData):
      ipAddress: str
      prefixLength: int
      origin: Optional[str] = None
      state: Optional[str] = None
      lifetime: Optional[datetime] = None

   ipAddress: list[IpAddress] = []
   dhcp: Optional[DhcpConfigInfo] = None
   autoConfigurationEnabled: Optional[bool] = None


class IpConfigSpec(DynamicData):
   class IpAddressSpec(DynamicData):
      ipAddress: str
      prefixLength: int
      operation: str

   ipAddress: list[IpAddressSpec] = []
   dhcp: Optional[DhcpConfigSpec] = None
   autoConfigurationEnabled: Optional[bool] = None


class IpRouteConfigInfo(DynamicData):
   class Gateway(DynamicData):
      ipAddress: Optional[str] = None
      device: Optional[str] = None

   class IpRoute(DynamicData):
      network: str
      prefixLength: int
      gateway: Gateway

   ipRoute: list[IpRoute] = []


class IpRouteConfigSpec(DynamicData):
   class GatewaySpec(DynamicData):
      ipAddress: Optional[str] = None
      device: Optional[str] = None

   class IpRouteSpec(DynamicData):
      network: str
      prefixLength: int
      gateway: GatewaySpec
      operation: str

   ipRoute: list[IpRouteSpec] = []


class IpStackInfo(DynamicData):
   class EntryType(Enum):
      other: ClassVar['EntryType'] = 'other'
      invalid: ClassVar['EntryType'] = 'invalid'
      dynamic: ClassVar['EntryType'] = 'dynamic'
      manual: ClassVar['EntryType'] = 'manual'

   class Preference(Enum):
      reserved: ClassVar['Preference'] = 'reserved'
      low: ClassVar['Preference'] = 'low'
      medium: ClassVar['Preference'] = 'medium'
      high: ClassVar['Preference'] = 'high'

   class NetToMedia(DynamicData):
      ipAddress: str
      physicalAddress: str
      device: str
      type: str

   class DefaultRouter(DynamicData):
      ipAddress: str
      device: str
      lifetime: datetime
      preference: str

   neighbor: list[NetToMedia] = []
   defaultRouter: list[DefaultRouter] = []


class NetBIOSConfigInfo(DynamicData):
   class Mode(Enum):
      unknown: ClassVar['Mode'] = 'unknown'
      enabled: ClassVar['Mode'] = 'enabled'
      disabled: ClassVar['Mode'] = 'disabled'
      enabledViaDHCP: ClassVar['Mode'] = 'enabledViaDHCP'

   mode: str


class WinNetBIOSConfigInfo(NetBIOSConfigInfo):
   primaryWINS: str
   secondaryWINS: Optional[str] = None
