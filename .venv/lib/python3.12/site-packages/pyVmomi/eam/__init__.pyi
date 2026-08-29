# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import fault as fault
from . import issue as issue
from . import vib as vib

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Datacenter
from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.eam.issue import Issue

from pyVmomi.eam.vib import VibInfo

from pyVmomi.vim.vApp import IpPool



class Agency(EamObject):
   class VMResourcePool(DynamicData):
      resourcePoolId: ResourcePool
      computeResourceId: ComputeResource

   class VMFolder(DynamicData):
      folderId: Folder
      datacenterId: Datacenter

   class ConfigInfo(DynamicData):
      agentConfig: list[Agent.ConfigInfo] = []
      scope: Optional[Scope] = None
      manuallyMarkAgentVmAvailableAfterProvisioning: Optional[bool] = None
      manuallyMarkAgentVmAvailableAfterPowerOn: Optional[bool] = None
      optimizedDeploymentEnabled: Optional[bool] = None
      agentName: Optional[str] = None
      agencyName: Optional[str] = None
      useUuidVmName: Optional[bool] = None
      manuallyProvisioned: Optional[bool] = None
      manuallyMonitored: Optional[bool] = None
      bypassVumEnabled: Optional[bool] = None
      agentVmNetwork: list[Network] = []
      agentVmDatastore: list[Datastore] = []
      preferHostConfiguration: Optional[bool] = None
      ipPool: Optional[IpPool] = None
      resourcePools: list[VMResourcePool] = []
      folders: list[VMFolder] = []

   class Scope(DynamicData):
      pass

   class ComputeResourceScope(Scope):
      computeResource: list[ComputeResource] = []

   @property
   def solutionId(self) -> str: ...
   @property
   def owner(self) -> Optional[str]: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def runtime(self) -> EamObject.RuntimeInfo: ...
   @property
   def agent(self) -> list[Agent]: ...

   def QuerySolutionId(self) -> str: ...
   def QueryConfig(self) -> ConfigInfo: ...
   def Update(self, config: ConfigInfo) -> None: ...
   def QueryRuntime(self) -> EamObject.RuntimeInfo: ...
   def QueryAgent(self) -> list[Agent]: ...
   def RegisterAgentVm(self, agentVm: VirtualMachine) -> Agent: ...
   def UnregisterAgentVm(self, agentVm: VirtualMachine) -> None: ...
   def Enable(self) -> None: ...
   def Disable(self) -> None: ...
   def Uninstall(self) -> None: ...
   def DestroyAgency(self) -> None: ...
   def AddIssue(self, issue: Issue) -> Issue: ...


class Agent(EamObject):
   class RuntimeInfo(EamObject.RuntimeInfo):
      vmPowerState: VirtualMachine.PowerState
      receivingHeartBeat: bool
      host: Optional[HostSystem] = None
      vm: Optional[VirtualMachine] = None
      vmIp: Optional[str] = None
      vmName: str
      esxAgentResourcePool: Optional[ResourcePool] = None
      esxAgentFolder: Optional[Folder] = None
      installedBulletin: list[str] = []
      installedVibs: list[VibInfo] = []
      agency: Optional[Agency] = None
      vmHook: Optional[VmHook] = None

   class VmHook(DynamicData):
      class VmState(Enum):
         provisioned: ClassVar['VmState'] = 'provisioned'
         poweredOn: ClassVar['VmState'] = 'poweredOn'
         prePowerOn: ClassVar['VmState'] = 'prePowerOn'

      vm: VirtualMachine
      vmState: str

   class StoragePolicy(DynamicData):
      pass

   class VsanStoragePolicy(StoragePolicy):
      profileId: str

   class SslTrust(DynamicData):
      pass

   class PinnedPemCertificate(SslTrust):
      sslCertificate: str

   class AnyCertificate(SslTrust):
      pass

   class ConfigInfo(DynamicData):
      class OvfDiskProvisioning(Enum):
         none: ClassVar['OvfDiskProvisioning'] = 'none'
         thin: ClassVar['OvfDiskProvisioning'] = 'thin'
         thick: ClassVar['OvfDiskProvisioning'] = 'thick'

      class AuthenticationScheme(Enum):
         NONE: ClassVar['AuthenticationScheme'] = 'NONE'
         VMWARE_SESSION_ID: ClassVar['AuthenticationScheme'] = 'VMWARE_SESSION_ID'

      productLineId: Optional[str] = None
      hostVersion: Optional[str] = None
      ovfPackageUrl: Optional[str] = None
      authenticationScheme: Optional[str] = None
      ovfSslTrust: Optional[SslTrust] = None
      ovfEnvironment: Optional[OvfEnvironmentInfo] = None
      vibUrl: Optional[str] = None
      vibSslTrust: Optional[SslTrust] = None
      vibMatchingRules: list[VibMatchingRule] = []
      vibName: Optional[str] = None
      dvFilterEnabled: Optional[bool] = None
      rebootHostAfterVibUninstall: Optional[bool] = None
      vmciService: list[str] = []
      ovfDiskProvisioning: Optional[str] = None
      vmStoragePolicies: list[StoragePolicy] = []
      vmResourceConfiguration: Optional[str] = None

   class OvfEnvironmentInfo(DynamicData):
      class OvfProperty(DynamicData):
         key: str
         value: str

      ovfProperty: list[OvfProperty] = []

   class VibMatchingRule(DynamicData):
      vibNameRegex: str
      vibVersionRegex: str

   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def config(self) -> ConfigInfo: ...

   def QueryRuntime(self) -> RuntimeInfo: ...
   def MarkAsAvailable(self) -> None: ...
   def QueryConfig(self) -> ConfigInfo: ...


class EamObject(ManagedObject):
   class RuntimeInfo(DynamicData):
      class Status(Enum):
         green: ClassVar['Status'] = 'green'
         yellow: ClassVar['Status'] = 'yellow'
         red: ClassVar['Status'] = 'red'

      class GoalState(Enum):
         enabled: ClassVar['GoalState'] = 'enabled'
         disabled: ClassVar['GoalState'] = 'disabled'
         uninstalled: ClassVar['GoalState'] = 'uninstalled'

      status: str
      issue: list[Issue] = []
      goalState: str
      entity: EamObject

   def Resolve(self, issueKey: list[int]) -> list[int]: ...
   def ResolveAll(self) -> None: ...
   def QueryIssue(self, issueKey: list[int]) -> list[Issue]: ...


class EsxAgentManager(EamObject):
   class MaintenanceModePolicy(Enum):
      singleHost: ClassVar['MaintenanceModePolicy'] = 'singleHost'
      multipleHosts: ClassVar['MaintenanceModePolicy'] = 'multipleHosts'

   @property
   def agency(self) -> list[Agency]: ...
   @property
   def issue(self) -> list[Issue]: ...

   def QueryAgency(self) -> list[Agency]: ...
   def CreateAgency(self, agencyConfigInfo: Agency.ConfigInfo, initialGoalState: str) -> Agency: ...
   def ScanForUnknownAgentVm(self) -> None: ...
   def SetMaintenanceModePolicy(self, policy: str) -> None: ...
   def GetMaintenanceModePolicy(self) -> str: ...


class Task(ManagedObject):
   pass
