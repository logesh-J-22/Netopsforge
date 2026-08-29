# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import byte

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionValue



class AdapterMapping(DynamicData):
   macAddress: Optional[str] = None
   adapter: IPSettings

class AutoIpV6Generator(IpV6Generator):
   pass


class CloudinitPrep(IdentitySettings):
   metadata: str
   userdata: Optional[str] = None


class CustomIpGenerator(IpGenerator):
   argument: Optional[str] = None


class CustomIpV6Generator(IpV6Generator):
   argument: Optional[str] = None


class CustomNameGenerator(NameGenerator):
   argument: Optional[str] = None

class DhcpIpGenerator(IpGenerator):
   pass

class DhcpIpV6Generator(IpV6Generator):
   pass

class DisableIpV4(IpGenerator):
   pass

class FixedIp(IpGenerator):
   ipAddress: str

class FixedIpV6(IpV6Generator):
   ipAddress: str
   subnetMask: int

class FixedName(NameGenerator):
   name: str


class GlobalIPSettings(DynamicData):
   dnsSuffixList: list[str] = []
   dnsServerList: list[str] = []


class GuiRunOnce(DynamicData):
   commandList: list[str] = []


class GuiUnattended(DynamicData):
   password: Optional[Password] = None
   timeZone: int
   autoLogon: bool
   autoLogonCount: int


class IPSettings(DynamicData):
   class IpV6AddressSpec(DynamicData):
      ip: list[IpV6Generator] = []
      gateway: list[str] = []

   class NetBIOSMode(Enum):
      enableNetBIOSViaDhcp: ClassVar['NetBIOSMode'] = 'enableNetBIOSViaDhcp'
      enableNetBIOS: ClassVar['NetBIOSMode'] = 'enableNetBIOS'
      disableNetBIOS: ClassVar['NetBIOSMode'] = 'disableNetBIOS'

   ip: IpGenerator
   subnetMask: Optional[str] = None
   gateway: list[str] = []
   ipV6Spec: Optional[IpV6AddressSpec] = None
   dnsServerList: list[str] = []
   dnsDomain: Optional[str] = None
   primaryWINS: Optional[str] = None
   secondaryWINS: Optional[str] = None
   netBIOS: Optional[NetBIOSMode] = None


class Identification(DynamicData):
   joinWorkgroup: Optional[str] = None
   joinDomain: Optional[str] = None
   domainAdmin: Optional[str] = None
   domainAdminPassword: Optional[Password] = None
   domainOU: Optional[str] = None


class IdentitySettings(DynamicData):
   pass


class IpGenerator(DynamicData):
   pass


class IpV6Generator(DynamicData):
   pass


class LicenseFilePrintData(DynamicData):
   class AutoMode(Enum):
      perServer: ClassVar['AutoMode'] = 'perServer'
      perSeat: ClassVar['AutoMode'] = 'perSeat'

   autoMode: AutoMode
   autoUsers: Optional[int] = None

class LinuxFlexPrep(IdentitySettings):
   pass

class LinuxOptions(Options):
   pass


class LinuxPrep(IdentitySettings):
   hostName: NameGenerator
   domain: str
   timeZone: Optional[str] = None
   hwClockUTC: Optional[bool] = None
   scriptText: Optional[str] = None
   compatibleCustomizationMethod: Optional[str] = None
   resetPassword: Optional[bool] = None
   password: Optional[Password] = None
   extraConfig: list[OptionValue] = []


class NameGenerator(DynamicData):
   pass


class Options(DynamicData):
   pass


class Password(DynamicData):
   value: str
   plainText: bool

class PrefixNameGenerator(NameGenerator):
   base: str


class Specification(DynamicData):
   options: Optional[Options] = None
   identity: IdentitySettings
   globalIPSettings: GlobalIPSettings
   nicSettingMap: list[AdapterMapping] = []
   encryptionKey: list[byte] = []

class StatelessIpV6Generator(IpV6Generator):
   pass


class Sysprep(IdentitySettings):
   guiUnattended: GuiUnattended
   userData: UserData
   guiRunOnce: Optional[GuiRunOnce] = None
   identification: Identification
   licenseFilePrintData: Optional[LicenseFilePrintData] = None
   scriptText: Optional[str] = None
   resetPassword: Optional[bool] = None
   extraConfig: list[OptionValue] = []

class SysprepText(IdentitySettings):
   value: str

class UnknownIpGenerator(IpGenerator):
   pass

class UnknownIpV6Generator(IpV6Generator):
   pass

class UnknownNameGenerator(NameGenerator):
   pass


class UserData(DynamicData):
   fullName: str
   orgName: str
   computerName: NameGenerator
   productId: str

class VirtualMachineNameGenerator(NameGenerator):
   pass


class WinOptions(Options):
   class SysprepRebootOption(Enum):
      reboot: ClassVar['SysprepRebootOption'] = 'reboot'
      noreboot: ClassVar['SysprepRebootOption'] = 'noreboot'
      shutdown: ClassVar['SysprepRebootOption'] = 'shutdown'

   changeSID: bool
   deleteAccounts: bool
   reboot: Optional[SysprepRebootOption] = None

class WindowsFlexPrep(IdentitySettings):
   pass
