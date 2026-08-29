# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.VmomiSupport import binary

from pyVmomi.VmomiSupport import long

from pyVmomi.VmomiSupport import short

from pyVmomi.vim import Datastore
from pyVmomi.vim import Description

from pyVmomi.vim import Network

from pyVmomi.vim import SharesInfo
from pyVmomi.vim import StorageResourceManager
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import PortConnection

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.encryption import CryptoSpec
from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import ChoiceOption

from pyVmomi.vim.option import IntOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.option import OptionValue
from pyVmomi.vim.option import StringOption

from pyVmomi.vim.vm import BaseIndependentFilterSpec
from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vslm import ID



class HostDiskMappingInfo(DynamicData):
   class PartitionInfo(DynamicData):
      name: str
      fileSystem: str
      capacityInKb: long

   physicalPartition: Optional[PartitionInfo] = None
   name: str
   exclusive: Optional[bool] = None


class HostDiskMappingOption(DynamicData):
   class PartitionOption(DynamicData):
      name: str
      fileSystem: str
      capacityInKb: long

   physicalPartition: list[PartitionOption] = []
   name: str

class ParaVirtualSCSIController(VirtualSCSIController):
   pass

class ParaVirtualSCSIControllerOption(VirtualSCSIControllerOption):
   pass

class VirtualAHCIController(VirtualSATAController):
   pass

class VirtualAHCIControllerOption(VirtualSATAControllerOption):
   pass

class VirtualBusLogicController(VirtualSCSIController):
   pass

class VirtualBusLogicControllerOption(VirtualSCSIControllerOption):
   pass

class VirtualCdrom(VirtualDevice):
   class IsoBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class PassthroughBackingInfo(VirtualDevice.DeviceBackingInfo):
      exclusive: bool

   class RemotePassthroughBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      exclusive: bool

   class AtapiBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteAtapiBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      pass


class VirtualCdromOption(VirtualDeviceOption):
   class IsoBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class PassthroughBackingOption(VirtualDeviceOption.DeviceBackingOption):
      exclusive: BoolOption

   class RemotePassthroughBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      exclusive: BoolOption

   class AtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteAtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass


class VirtualController(VirtualDevice):
   busNumber: int
   device: list[int] = []


class VirtualControllerOption(VirtualDeviceOption):
   devices: IntOption
   supportedDevice: list[type] = []


class VirtualDevice(DynamicData):
   class BackingInfo(DynamicData):
      pass

   class FileBackingInfo(BackingInfo):
      fileName: str
      datastore: Optional[Datastore] = None
      backingObjectId: Optional[str] = None

   class DeviceBackingInfo(BackingInfo):
      deviceName: str
      useAutoDetect: Optional[bool] = None

   class RemoteDeviceBackingInfo(BackingInfo):
      deviceName: str
      useAutoDetect: Optional[bool] = None

   class PipeBackingInfo(BackingInfo):
      pipeName: str

   class URIBackingInfo(BackingInfo):
      serviceURI: str
      direction: str
      proxyURI: Optional[str] = None

   class ConnectInfo(DynamicData):
      class Status(Enum):
         ok: ClassVar['Status'] = 'ok'
         recoverableError: ClassVar['Status'] = 'recoverableError'
         unrecoverableError: ClassVar['Status'] = 'unrecoverableError'
         untried: ClassVar['Status'] = 'untried'

      class MigrateConnectOp(Enum):
         connect: ClassVar['MigrateConnectOp'] = 'connect'
         disconnect: ClassVar['MigrateConnectOp'] = 'disconnect'
         unset: ClassVar['MigrateConnectOp'] = 'unset'

      migrateConnect: Optional[str] = None
      startConnected: bool
      allowGuestControl: bool
      connected: bool
      status: Optional[str] = None

   class BusSlotInfo(DynamicData):
      pass

   class PciBusSlotInfo(BusSlotInfo):
      pciSlotNumber: int

   class DeviceGroupInfo(DynamicData):
      groupInstanceKey: int
      sequenceId: int

   key: int
   deviceInfo: Optional[Description] = None
   backing: Optional[BackingInfo] = None
   connectable: Optional[ConnectInfo] = None
   slotInfo: Optional[BusSlotInfo] = None
   controllerKey: Optional[int] = None
   unitNumber: Optional[int] = None
   numaNode: Optional[int] = None
   deviceGroupInfo: Optional[DeviceGroupInfo] = None


class VirtualDeviceOption(DynamicData):
   class BackingOption(DynamicData):
      type: type

   class FileBackingOption(BackingOption):
      class FileExtension(Enum):
         iso: ClassVar['FileExtension'] = 'iso'
         flp: ClassVar['FileExtension'] = 'flp'
         vmdk: ClassVar['FileExtension'] = 'vmdk'
         dsk: ClassVar['FileExtension'] = 'dsk'
         rdm: ClassVar['FileExtension'] = 'rdm'

      fileNameExtensions: Optional[ChoiceOption] = None

   class DeviceBackingOption(BackingOption):
      autoDetectAvailable: BoolOption

   class RemoteDeviceBackingOption(BackingOption):
      autoDetectAvailable: BoolOption

   class PipeBackingOption(BackingOption):
      pass

   class URIBackingOption(BackingOption):
      class Direction(Enum):
         server: ClassVar['Direction'] = 'server'
         client: ClassVar['Direction'] = 'client'

      directions: ChoiceOption

   class ConnectOption(DynamicData):
      startConnected: BoolOption
      allowGuestControl: BoolOption

   class BusSlotOption(DynamicData):
      type: type

   type: type
   connectOption: Optional[ConnectOption] = None
   busSlotOption: Optional[BusSlotOption] = None
   controllerType: Optional[type] = None
   autoAssignController: Optional[BoolOption] = None
   backingOption: list[BackingOption] = []
   defaultBackingOptionIndex: Optional[int] = None
   licensingLimit: list[PropertyPath] = []
   deprecated: bool
   plugAndPlay: bool
   hotRemoveSupported: bool
   numaSupported: Optional[bool] = None


class VirtualDeviceSpec(DynamicData):
   class Operation(Enum):
      add: ClassVar['Operation'] = 'add'
      remove: ClassVar['Operation'] = 'remove'
      edit: ClassVar['Operation'] = 'edit'

   class FileOperation(Enum):
      create: ClassVar['FileOperation'] = 'create'
      destroy: ClassVar['FileOperation'] = 'destroy'
      replace: ClassVar['FileOperation'] = 'replace'

   class BackingSpec(DynamicData):
      parent: Optional[BackingSpec] = None
      crypto: Optional[CryptoSpec] = None

   class ChangeMode(Enum):
      fail: ClassVar['ChangeMode'] = 'fail'
      skip: ClassVar['ChangeMode'] = 'skip'

   operation: Optional[Operation] = None
   fileOperation: Optional[FileOperation] = None
   device: VirtualDevice
   profile: list[ProfileSpec] = []
   backing: Optional[BackingSpec] = None
   filterSpec: list[BaseIndependentFilterSpec] = []
   changeMode: Optional[str] = None


class VirtualDisk(VirtualDevice):
   class DeltaDiskFormat(Enum):
      redoLogFormat: ClassVar['DeltaDiskFormat'] = 'redoLogFormat'
      nativeFormat: ClassVar['DeltaDiskFormat'] = 'nativeFormat'
      seSparseFormat: ClassVar['DeltaDiskFormat'] = 'seSparseFormat'

   class DeltaDiskFormatVariant(Enum):
      vmfsSparseVariant: ClassVar['DeltaDiskFormatVariant'] = 'vmfsSparseVariant'
      vsanSparseVariant: ClassVar['DeltaDiskFormatVariant'] = 'vsanSparseVariant'

   class DiskChainBrokenIssue(Enum):
      noIssue: ClassVar['DiskChainBrokenIssue'] = 'noIssue'
      cidMismatch: ClassVar['DiskChainBrokenIssue'] = 'cidMismatch'

   class Sharing(Enum):
      sharingNone: ClassVar['Sharing'] = 'sharingNone'
      sharingMultiWriter: ClassVar['Sharing'] = 'sharingMultiWriter'

   class SparseVer1BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      spaceUsedInKB: Optional[long] = None
      contentId: Optional[str] = None
      parent: Optional[SparseVer1BackingInfo] = None

   class SparseVer2BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      spaceUsedInKB: Optional[long] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[SparseVer2BackingInfo] = None
      keyId: Optional[CryptoKeyId] = None

   class FlatVer1BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      contentId: Optional[str] = None
      parent: Optional[FlatVer1BackingInfo] = None

   class FlatVer2BackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      split: Optional[bool] = None
      writeThrough: Optional[bool] = None
      thinProvisioned: Optional[bool] = None
      eagerlyScrub: Optional[bool] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[FlatVer2BackingInfo] = None
      deltaDiskFormat: Optional[str] = None
      digestEnabled: Optional[bool] = None
      deltaGrainSize: Optional[int] = None
      deltaDiskFormatVariant: Optional[str] = None
      sharing: Optional[str] = None
      keyId: Optional[CryptoKeyId] = None

   class SeSparseBackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      writeThrough: Optional[bool] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[SeSparseBackingInfo] = None
      deltaDiskFormat: Optional[str] = None
      digestEnabled: Optional[bool] = None
      grainSize: Optional[int] = None
      keyId: Optional[CryptoKeyId] = None

   class RawDiskVer2BackingInfo(VirtualDevice.DeviceBackingInfo):
      descriptorFileName: str
      uuid: Optional[str] = None
      changeId: Optional[str] = None
      sharing: Optional[str] = None

   class PartitionedRawDiskVer2BackingInfo(RawDiskVer2BackingInfo):
      partition: list[int] = []

   class RawDiskMappingVer1BackingInfo(VirtualDevice.FileBackingInfo):
      lunUuid: Optional[str] = None
      deviceName: Optional[str] = None
      compatibilityMode: Optional[str] = None
      diskMode: Optional[str] = None
      uuid: Optional[str] = None
      contentId: Optional[str] = None
      changeId: Optional[str] = None
      parent: Optional[RawDiskMappingVer1BackingInfo] = None
      deltaDiskFormat: Optional[str] = None
      deltaGrainSize: Optional[int] = None
      sharing: Optional[str] = None

   class LocalPMemBackingInfo(VirtualDevice.FileBackingInfo):
      diskMode: str
      uuid: Optional[str] = None
      volumeUUID: Optional[str] = None
      contentId: Optional[str] = None

   class VFlashCacheConfigInfo(DynamicData):
      class CacheConsistencyType(Enum):
         strong: ClassVar['CacheConsistencyType'] = 'strong'
         weak: ClassVar['CacheConsistencyType'] = 'weak'

      class CacheMode(Enum):
         write_thru: ClassVar['CacheMode'] = 'write_thru'
         write_back: ClassVar['CacheMode'] = 'write_back'

      vFlashModule: Optional[str] = None
      reservationInMB: Optional[long] = None
      cacheConsistencyType: Optional[str] = None
      cacheMode: Optional[str] = None
      blockSizeInKB: Optional[long] = None

   capacityInKB: long
   capacityInBytes: Optional[long] = None
   shares: Optional[SharesInfo] = None
   storageIOAllocation: Optional[StorageResourceManager.IOAllocationInfo] = None
   diskObjectId: Optional[str] = None
   vFlashCacheConfigInfo: Optional[VFlashCacheConfigInfo] = None
   iofilter: list[str] = []
   vDiskId: Optional[ID] = None
   vDiskVersion: Optional[int] = None
   virtualDiskFormat: Optional[str] = None
   nativeUnmanagedLinkedClone: Optional[bool] = None
   independentFilters: list[BaseIndependentFilterSpec] = []
   guestReadOnly: Optional[bool] = None
   diskChainBrokenIssue: Optional[str] = None


class VirtualDiskId(DynamicData):
   vm: VirtualMachine
   diskId: int


class VirtualDiskOption(VirtualDeviceOption):
   class DiskMode(Enum):
      persistent: ClassVar['DiskMode'] = 'persistent'
      nonpersistent: ClassVar['DiskMode'] = 'nonpersistent'
      undoable: ClassVar['DiskMode'] = 'undoable'
      independent_persistent: ClassVar['DiskMode'] = 'independent_persistent'
      independent_nonpersistent: ClassVar['DiskMode'] = 'independent_nonpersistent'
      append: ClassVar['DiskMode'] = 'append'

   class CompatibilityMode(Enum):
      virtualMode: ClassVar['CompatibilityMode'] = 'virtualMode'
      physicalMode: ClassVar['CompatibilityMode'] = 'physicalMode'

   class SparseVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      diskModes: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool

   class SparseVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      virtualDiskFormat: Optional[ChoiceOption] = None

   class FlatVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool

   class DeltaDiskFormatsSupported(DynamicData):
      datastoreType: type
      deltaDiskFormat: ChoiceOption

   class FlatVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      split: BoolOption
      writeThrough: BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      thinProvisioned: BoolOption
      eagerlyScrub: BoolOption
      deltaDiskFormat: ChoiceOption
      deltaDiskFormatsSupported: list[DeltaDiskFormatsSupported] = []
      virtualDiskFormat: Optional[ChoiceOption] = None

   class SeSparseBackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      writeThrough: BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      deltaDiskFormatsSupported: list[DeltaDiskFormatsSupported] = []
      virtualDiskFormat: Optional[ChoiceOption] = None

   class RawDiskVer2BackingOption(VirtualDeviceOption.DeviceBackingOption):
      descriptorFileNameExtensions: ChoiceOption
      uuid: bool

   class PartitionedRawDiskVer2BackingOption(RawDiskVer2BackingOption):
      pass

   class RawDiskMappingVer1BackingOption(VirtualDeviceOption.DeviceBackingOption):
      descriptorFileNameExtensions: Optional[ChoiceOption] = None
      compatibilityMode: ChoiceOption
      diskMode: ChoiceOption
      uuid: bool
      virtualDiskFormat: Optional[ChoiceOption] = None

   class LocalPMemBackingOption(VirtualDeviceOption.FileBackingOption):
      diskMode: ChoiceOption
      growable: bool
      hotGrowable: bool
      uuid: bool

   class VFlashCacheConfigOption(DynamicData):
      cacheConsistencyType: ChoiceOption
      cacheMode: ChoiceOption
      reservationInMB: LongOption
      blockSizeInKB: LongOption

   capacityInKB: LongOption
   ioAllocationOption: StorageResourceManager.IOAllocationOption
   vFlashCacheConfigOption: Optional[VFlashCacheConfigOption] = None


class VirtualDiskSpec(VirtualDeviceSpec):
   diskMoveType: Optional[str] = None
   migrateCache: Optional[bool] = None

class VirtualE1000(VirtualEthernetCard):
   pass

class VirtualE1000Option(VirtualEthernetCardOption):
   pass

class VirtualE1000e(VirtualEthernetCard):
   pass

class VirtualE1000eOption(VirtualEthernetCardOption):
   pass

class VirtualEnsoniq1371(VirtualSoundCard):
   pass

class VirtualEnsoniq1371Option(VirtualSoundCardOption):
   pass


class VirtualEthernetCard(VirtualDevice):
   class NetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      network: Optional[Network] = None
      inPassthroughMode: Optional[bool] = None

   class LegacyNetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class DistributedVirtualPortBackingInfo(VirtualDevice.BackingInfo):
      port: PortConnection

   class OpaqueNetworkBackingInfo(VirtualDevice.BackingInfo):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class ResourceAllocation(DynamicData):
      reservation: Optional[long] = None
      share: SharesInfo
      limit: Optional[long] = None

   addressType: Optional[str] = None
   macAddress: Optional[str] = None
   wakeOnLanEnabled: Optional[bool] = None
   resourceAllocation: Optional[ResourceAllocation] = None
   externalId: Optional[str] = None
   uptCompatibilityEnabled: Optional[bool] = None
   subnetId: Optional[str] = None


class VirtualEthernetCardOption(VirtualDeviceOption):
   class NetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class OpaqueNetworkBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class LegacyNetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      class LegacyNetworkDeviceName(Enum):
         bridged: ClassVar['LegacyNetworkDeviceName'] = 'bridged'
         nat: ClassVar['LegacyNetworkDeviceName'] = 'nat'
         hostonly: ClassVar['LegacyNetworkDeviceName'] = 'hostonly'

   class DistributedVirtualPortBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class MacTypes(Enum):
      manual: ClassVar['MacTypes'] = 'manual'
      generated: ClassVar['MacTypes'] = 'generated'
      assigned: ClassVar['MacTypes'] = 'assigned'

   supportedOUI: ChoiceOption
   macType: ChoiceOption
   wakeOnLanEnabled: BoolOption
   vmDirectPathGen2Supported: Optional[bool] = None
   uptCompatibilityEnabled: Optional[BoolOption] = None

class VirtualFloppy(VirtualDevice):
   class ImageBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteDeviceBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      pass

class VirtualFloppyOption(VirtualDeviceOption):
   class ImageBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteDeviceBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      pass

class VirtualHdAudioCard(VirtualSoundCard):
   pass

class VirtualHdAudioCardOption(VirtualSoundCardOption):
   pass

class VirtualIDEController(VirtualController):
   pass


class VirtualIDEControllerOption(VirtualControllerOption):
   numIDEDisks: IntOption
   numIDECdroms: IntOption

class VirtualKeyboard(VirtualDevice):
   pass

class VirtualKeyboardOption(VirtualDeviceOption):
   pass

class VirtualLsiLogicController(VirtualSCSIController):
   pass

class VirtualLsiLogicControllerOption(VirtualSCSIControllerOption):
   pass

class VirtualLsiLogicSASController(VirtualSCSIController):
   pass

class VirtualLsiLogicSASControllerOption(VirtualSCSIControllerOption):
   pass


class VirtualNVDIMM(VirtualDevice):
   class BackingInfo(VirtualDevice.FileBackingInfo):
      parent: Optional[BackingInfo] = None
      changeId: Optional[str] = None

   capacityInMB: long
   configuredCapacityInMB: Optional[long] = None

class VirtualNVDIMMController(VirtualController):
   pass


class VirtualNVDIMMControllerOption(VirtualControllerOption):
   numNVDIMMControllers: IntOption


class VirtualNVDIMMOption(VirtualDeviceOption):
   capacityInMB: LongOption
   growable: bool
   hotGrowable: bool
   granularityInMB: long


class VirtualNVMEController(VirtualController):
   class Sharing(Enum):
      noSharing: ClassVar['Sharing'] = 'noSharing'
      physicalSharing: ClassVar['Sharing'] = 'physicalSharing'

   sharedBus: Optional[str] = None


class VirtualNVMEControllerOption(VirtualControllerOption):
   numNVMEDisks: IntOption
   sharing: list[str] = []

class VirtualPCIController(VirtualController):
   pass


class VirtualPCIControllerOption(VirtualControllerOption):
   numSCSIControllers: IntOption
   numEthernetCards: IntOption
   numVideoCards: IntOption
   numSoundCards: IntOption
   numVmiRoms: IntOption
   numVmciDevices: IntOption
   numPCIPassthroughDevices: IntOption
   numSasSCSIControllers: IntOption
   numVmxnet3EthernetCards: IntOption
   numParaVirtualSCSIControllers: IntOption
   numSATAControllers: IntOption
   numNVMEControllers: Optional[IntOption] = None
   numVmxnet3VrdmaEthernetCards: Optional[IntOption] = None


class VirtualPCIPassthrough(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      id: str
      deviceId: str
      systemId: str
      vendorId: short

   class AllowedDevice(DynamicData):
      vendorId: int
      deviceId: int
      subVendorId: Optional[int] = None
      subDeviceId: Optional[int] = None
      revisionId: Optional[short] = None

   class DynamicBackingInfo(VirtualDevice.DeviceBackingInfo):
      allowedDevice: list[AllowedDevice] = []
      customLabel: Optional[str] = None
      assignedId: Optional[str] = None

   class PluginBackingInfo(VirtualDevice.BackingInfo):
      pass

   class VmiopBackingInfo(PluginBackingInfo):
      vgpu: Optional[str] = None
      vgpuMigrateDataSizeMB: Optional[int] = None
      migrateSupported: Optional[bool] = None
      enhancedMigrateCapability: Optional[bool] = None

   class DvxBackingInfo(VirtualDevice.BackingInfo):
      deviceClass: Optional[str] = None
      configParams: list[OptionValue] = []


class VirtualPCIPassthroughOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class PluginBackingOption(VirtualDeviceOption.BackingOption):
      pass

   class VmiopBackingOption(PluginBackingOption):
      vgpu: StringOption
      maxInstances: int

   class DynamicBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class DvxBackingOption(VirtualDeviceOption.BackingOption):
      pass

class VirtualPCNet32(VirtualEthernetCard):
   pass

class VirtualPCNet32Option(VirtualEthernetCardOption):
   supportsMorphing: bool

class VirtualPS2Controller(VirtualController):
   pass


class VirtualPS2ControllerOption(VirtualControllerOption):
   numKeyboards: IntOption
   numPointingDevices: IntOption

class VirtualParallelPort(VirtualDevice):
   class FileBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

class VirtualParallelPortOption(VirtualDeviceOption):
   class FileBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

class VirtualPointingDevice(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      hostPointingDevice: str


class VirtualPointingDeviceOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      class HostPointingDeviceChoice(Enum):
         autodetect: ClassVar['HostPointingDeviceChoice'] = 'autodetect'
         intellimouseExplorer: ClassVar['HostPointingDeviceChoice'] = 'intellimouseExplorer'
         intellimousePs2: ClassVar['HostPointingDeviceChoice'] = 'intellimousePs2'
         logitechMouseman: ClassVar['HostPointingDeviceChoice'] = 'logitechMouseman'
         microsoft_serial: ClassVar['HostPointingDeviceChoice'] = 'microsoft_serial'
         mouseSystems: ClassVar['HostPointingDeviceChoice'] = 'mouseSystems'
         mousemanSerial: ClassVar['HostPointingDeviceChoice'] = 'mousemanSerial'
         ps2: ClassVar['HostPointingDeviceChoice'] = 'ps2'

      hostPointingDevice: ChoiceOption


class VirtualPrecisionClock(VirtualDevice):
   class SystemClockBackingInfo(VirtualDevice.BackingInfo):
      protocol: Optional[str] = None


class VirtualPrecisionClockOption(VirtualDeviceOption):
   class SystemClockBackingOption(VirtualDeviceOption.BackingOption):
      protocol: ChoiceOption

class VirtualSATAController(VirtualController):
   pass


class VirtualSATAControllerOption(VirtualControllerOption):
   numSATADisks: IntOption
   numSATACdroms: IntOption


class VirtualSCSIController(VirtualController):
   class Sharing(Enum):
      noSharing: ClassVar['Sharing'] = 'noSharing'
      virtualSharing: ClassVar['Sharing'] = 'virtualSharing'
      physicalSharing: ClassVar['Sharing'] = 'physicalSharing'

   hotAddRemove: Optional[bool] = None
   sharedBus: Sharing
   scsiCtlrUnitNumber: Optional[int] = None


class VirtualSCSIControllerOption(VirtualControllerOption):
   numSCSIDisks: IntOption
   numSCSICdroms: IntOption
   numSCSIPassthrough: IntOption
   sharing: list[VirtualSCSIController.Sharing] = []
   defaultSharedIndex: int
   hotAddRemove: BoolOption
   scsiCtlrUnitNumber: int

class VirtualSCSIPassthrough(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

class VirtualSCSIPassthroughOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

class VirtualSIOController(VirtualController):
   pass


class VirtualSIOControllerOption(VirtualControllerOption):
   numFloppyDrives: IntOption
   numSerialPorts: IntOption
   numParallelPorts: IntOption


class VirtualSerialPort(VirtualDevice):
   class FileBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class PipeBackingInfo(VirtualDevice.PipeBackingInfo):
      endpoint: str
      noRxLoss: Optional[bool] = None

   class URIBackingInfo(VirtualDevice.URIBackingInfo):
      pass

   class ThinPrintBackingInfo(VirtualDevice.BackingInfo):
      pass

   yieldOnPoll: bool


class VirtualSerialPortOption(VirtualDeviceOption):
   class EndPoint(Enum):
      client: ClassVar['EndPoint'] = 'client'
      server: ClassVar['EndPoint'] = 'server'

   class FileBackingOption(VirtualDeviceOption.FileBackingOption):
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class PipeBackingOption(VirtualDeviceOption.PipeBackingOption):
      endpoint: ChoiceOption
      noRxLoss: BoolOption

   class URIBackingOption(VirtualDeviceOption.URIBackingOption):
      pass

   class ThinPrintBackingOption(VirtualDeviceOption.BackingOption):
      pass

   yieldOnPoll: BoolOption

class VirtualSoundBlaster16(VirtualSoundCard):
   pass

class VirtualSoundBlaster16Option(VirtualSoundCardOption):
   pass

class VirtualSoundCard(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

class VirtualSoundCardOption(VirtualDeviceOption):
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass


class VirtualSriovEthernetCard(VirtualEthernetCard):
   class SriovBackingInfo(VirtualDevice.BackingInfo):
      physicalFunctionBacking: Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionBacking: Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionIndex: Optional[int] = None

   allowGuestOSMtuChange: Optional[bool] = None
   sriovBacking: Optional[SriovBackingInfo] = None
   dvxBackingInfo: Optional[VirtualPCIPassthrough.DvxBackingInfo] = None

class VirtualSriovEthernetCardOption(VirtualEthernetCardOption):
   class SriovBackingOption(VirtualDeviceOption.BackingOption):
      pass


class VirtualTPM(VirtualDevice):
   endorsementKeyCertificateSigningRequest: list[binary] = []
   endorsementKeyCertificate: list[binary] = []


class VirtualTPMOption(VirtualDeviceOption):
   supportedFirmware: list[str] = []


class VirtualUSB(VirtualDevice):
   class USBBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteHostBackingInfo(VirtualDevice.DeviceBackingInfo):
      hostname: str

   class RemoteClientBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      hostname: str

   connected: bool
   vendor: Optional[int] = None
   product: Optional[int] = None
   family: list[str] = []
   speed: list[str] = []


class VirtualUSBController(VirtualController):
   class PciBusSlotInfo(VirtualDevice.PciBusSlotInfo):
      ehciPciSlotNumber: Optional[int] = None

   autoConnectDevices: Optional[bool] = None
   ehciEnabled: Optional[bool] = None


class VirtualUSBControllerOption(VirtualControllerOption):
   autoConnectDevices: BoolOption
   ehciSupported: BoolOption
   supportedSpeeds: list[str] = []

class VirtualUSBOption(VirtualDeviceOption):
   class USBBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteHostBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteClientBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      pass


class VirtualUSBXHCIController(VirtualController):
   autoConnectDevices: Optional[bool] = None


class VirtualUSBXHCIControllerOption(VirtualControllerOption):
   autoConnectDevices: BoolOption
   supportedSpeeds: list[str] = []


class VirtualVMCIDevice(VirtualDevice):
   class Action(Enum):
      allow: ClassVar['Action'] = 'allow'
      deny: ClassVar['Action'] = 'deny'

   class Protocol(Enum):
      hypervisor: ClassVar['Protocol'] = 'hypervisor'
      doorbell: ClassVar['Protocol'] = 'doorbell'
      queuepair: ClassVar['Protocol'] = 'queuepair'
      datagram: ClassVar['Protocol'] = 'datagram'
      stream: ClassVar['Protocol'] = 'stream'
      anyProtocol: ClassVar['Protocol'] = 'anyProtocol'

   class Direction(Enum):
      guest: ClassVar['Direction'] = 'guest'
      host: ClassVar['Direction'] = 'host'
      anyDirection: ClassVar['Direction'] = 'anyDirection'

   class FilterSpec(DynamicData):
      rank: long
      action: str
      protocol: str
      direction: str
      lowerDstPortBoundary: Optional[long] = None
      upperDstPortBoundary: Optional[long] = None

   class FilterInfo(DynamicData):
      filters: list[FilterSpec] = []

   id: Optional[long] = None
   allowUnrestrictedCommunication: Optional[bool] = None
   filterEnable: Optional[bool] = None
   filterInfo: Optional[FilterInfo] = None


class VirtualVMCIDeviceOption(VirtualDeviceOption):
   class FilterSpecOption(DynamicData):
      action: ChoiceOption
      protocol: ChoiceOption
      direction: ChoiceOption
      lowerDstPortBoundary: LongOption
      upperDstPortBoundary: LongOption

   allowUnrestrictedCommunication: BoolOption
   filterSpecOption: Optional[FilterSpecOption] = None
   filterSupported: Optional[BoolOption] = None

class VirtualVMIROM(VirtualDevice):
   pass

class VirtualVMIROMOption(VirtualDeviceOption):
   pass


class VirtualVideoCard(VirtualDevice):
   class Use3dRenderer(Enum):
      automatic: ClassVar['Use3dRenderer'] = 'automatic'
      software: ClassVar['Use3dRenderer'] = 'software'
      hardware: ClassVar['Use3dRenderer'] = 'hardware'

   videoRamSizeInKB: Optional[long] = None
   numDisplays: Optional[int] = None
   useAutoDetect: Optional[bool] = None
   enable3DSupport: Optional[bool] = None
   use3dRenderer: Optional[str] = None
   graphicsMemorySizeInKB: Optional[long] = None


class VirtualVideoCardOption(VirtualDeviceOption):
   videoRamSizeInKB: Optional[LongOption] = None
   numDisplays: Optional[IntOption] = None
   useAutoDetect: Optional[BoolOption] = None
   support3D: Optional[BoolOption] = None
   use3dRendererSupported: Optional[BoolOption] = None
   graphicsMemorySizeInKB: Optional[LongOption] = None
   graphicsMemorySizeSupported: Optional[BoolOption] = None

class VirtualVmxnet(VirtualEthernetCard):
   pass

class VirtualVmxnet2(VirtualVmxnet):
   pass

class VirtualVmxnet2Option(VirtualVmxnetOption):
   pass


class VirtualVmxnet3(VirtualVmxnet):
   class StrictLatencyConfig(DynamicData):
      class DisableOffload(Enum):
         NONE: ClassVar['DisableOffload'] = 'NONE'
         TSO: ClassVar['DisableOffload'] = 'TSO'
         LRO: ClassVar['DisableOffload'] = 'LRO'
         TSO_LRO: ClassVar['DisableOffload'] = 'TSO_LRO'

      allowed: Optional[bool] = None
      measureLatency: Optional[bool] = None
      maxTxQueues: Optional[int] = None
      maxRxQueues: Optional[int] = None
      txDataRingDescSize: Optional[int] = None
      rxDataRingDescSize: Optional[int] = None
      disableOffload: Optional[str] = None

   uptv2Enabled: Optional[bool] = None
   strictLatencyConfig: Optional[StrictLatencyConfig] = None


class VirtualVmxnet3Option(VirtualVmxnetOption):
   class StrictLatencyConfigOption(DynamicData):
      allowed: BoolOption
      measureLatency: BoolOption
      maxTxQueues: IntOption
      maxRxQueues: IntOption
      txDataRingDescSize: IntOption
      rxDataRingDescSize: IntOption
      disableOffload: ChoiceOption

   uptv2Enabled: Optional[BoolOption] = None
   strictLatencyConfigOption: Optional[StrictLatencyConfigOption] = None


class VirtualVmxnet3Vrdma(VirtualVmxnet3):
   deviceProtocol: Optional[str] = None


class VirtualVmxnet3VrdmaOption(VirtualVmxnet3Option):
   class DeviceProtocols(Enum):
      rocev1: ClassVar['DeviceProtocols'] = 'rocev1'
      rocev2: ClassVar['DeviceProtocols'] = 'rocev2'

   deviceProtocol: Optional[ChoiceOption] = None

class VirtualVmxnetOption(VirtualEthernetCardOption):
   pass

class VirtualWDT(VirtualDevice):
   runOnBoot: bool
   running: bool


class VirtualWDTOption(VirtualDeviceOption):
   runOnBoot: BoolOption
