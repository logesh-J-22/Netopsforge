# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar

from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import byte

from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import ProfileUpdateFailed

from pyVmomi.vim.host import ConfigSpec
from pyVmomi.vim.profile import ApplyProfile

from pyVmomi.vim.profile import ComplianceLocator
from pyVmomi.vim.profile import ComplianceProfile

from pyVmomi.vim.profile import DeferredPolicyOptionParameter
from pyVmomi.vim.profile import Profile
from pyVmomi.vim.profile import ProfileMetadata

from pyVmomi.vim.profile import ProfilePropertyPath
from pyVmomi.vim.profile import ProfileStructure



class ActiveDirectoryProfile(ApplyProfile):
   pass


class AnswerFile(DynamicData):
   userInput: list[DeferredPolicyOptionParameter] = []
   createdTime: datetime
   modifiedTime: datetime


class AnswerFileStatusResult(DynamicData):
   class AnswerFileStatusError(DynamicData):
      userInputPath: ProfilePropertyPath
      errMsg: LocalizableMessage

   checkedTime: datetime
   host: HostSystem
   status: str
   error: list[AnswerFileStatusError] = []


class AuthenticationProfile(ApplyProfile):
   activeDirectory: Optional[ActiveDirectoryProfile] = None


class DateTimeProfile(ApplyProfile):
   pass

class DvsHostVNicProfile(DvsVNicProfile):
   pass


class DvsProfile(ApplyProfile):
   key: str
   name: str
   uplink: list[PnicUplinkProfile] = []

class DvsServiceConsoleVNicProfile(DvsVNicProfile):
   pass


class DvsVNicProfile(ApplyProfile):
   key: str
   ipConfig: IpAddressProfile


class ExecuteResult(DynamicData):
   class Status(Enum):
      success: ClassVar['Status'] = 'success'
      needInput: ClassVar['Status'] = 'needInput'
      error: ClassVar['Status'] = 'error'

   class ExecuteError(DynamicData):
      path: Optional[ProfilePropertyPath] = None
      message: LocalizableMessage

   status: str
   configSpec: Optional[ConfigSpec] = None
   inapplicablePath: list[PropertyPath] = []
   requireInput: list[DeferredPolicyOptionParameter] = []
   error: list[ExecuteError] = []


class FirewallProfile(ApplyProfile):
   class RulesetProfile(ApplyProfile):
      key: str

   ruleset: list[RulesetProfile] = []


class HostApplyProfile(ApplyProfile):
   memory: Optional[HostMemoryProfile] = None
   storage: Optional[StorageProfile] = None
   network: Optional[NetworkProfile] = None
   datetime: Optional[DateTimeProfile] = None
   firewall: Optional[FirewallProfile] = None
   security: Optional[SecurityProfile] = None
   service: list[ServiceProfile] = []
   option: list[OptionProfile] = []
   userAccount: list[UserProfile] = []
   usergroupAccount: list[UserGroupProfile] = []
   authentication: Optional[AuthenticationProfile] = None


class HostMemoryProfile(ApplyProfile):
   pass

class HostPortGroupProfile(PortGroupProfile):
   ipConfig: IpAddressProfile


class HostProfile(Profile):
   class ConfigInfo(Profile.ConfigInfo):
      applyProfile: Optional[HostApplyProfile] = None
      defaultComplyProfile: Optional[ComplianceProfile] = None
      defaultComplyLocator: list[ComplianceLocator] = []
      customComplyProfile: Optional[ComplianceProfile] = None
      disabledExpressionList: list[str] = []
      description: Optional[Profile.Description] = None

   class ConfigSpec(Profile.CreateSpec):
      pass

   class SerializedHostProfileSpec(Profile.SerializedCreateSpec):
      validatorHost: Optional[HostSystem] = None
      validating: Optional[bool] = None

   class CompleteConfigSpec(ConfigSpec):
      applyProfile: Optional[HostApplyProfile] = None
      customComplyProfile: Optional[ComplianceProfile] = None
      disabledExpressionListChanged: bool
      disabledExpressionList: list[str] = []
      validatorHost: Optional[HostSystem] = None
      validating: Optional[bool] = None
      hostConfig: Optional[ConfigInfo] = None

   class HostBasedConfigSpec(ConfigSpec):
      host: HostSystem
      useHostProfileEngine: Optional[bool] = None

   class ValidationState(Enum):
      Ready: ClassVar['ValidationState'] = 'Ready'
      Running: ClassVar['ValidationState'] = 'Running'
      Failed: ClassVar['ValidationState'] = 'Failed'

   class ValidationFailureInfo(DynamicData):
      class UpdateType(Enum):
         HostBased: ClassVar['UpdateType'] = 'HostBased'
         Import: ClassVar['UpdateType'] = 'Import'
         Edit: ClassVar['UpdateType'] = 'Edit'
         Compose: ClassVar['UpdateType'] = 'Compose'

      name: str
      annotation: str
      updateType: str
      host: Optional[HostSystem] = None
      applyProfile: Optional[HostApplyProfile] = None
      failures: list[ProfileUpdateFailed.UpdateFailure] = []
      faults: list[MethodFault] = []

   @property
   def validationState(self) -> Optional[str]: ...
   @property
   def validationStateUpdateTime(self) -> Optional[datetime]: ...
   @property
   def validationFailureInfo(self) -> Optional[ValidationFailureInfo]: ...
   @property
   def complianceCheckTime(self) -> Optional[datetime]: ...
   @property
   def referenceHost(self) -> Optional[HostSystem]: ...

   def ResetValidationState(self) -> None: ...
   def UpdateReferenceHost(self, host: Optional[HostSystem]) -> None: ...
   def Update(self, config: ConfigSpec) -> None: ...
   def Execute(self, host: HostSystem, deferredParam: list[DeferredPolicyOptionParameter]) -> ExecuteResult: ...


class HostSpecification(DynamicData):
   createdTime: datetime
   lastModified: Optional[datetime] = None
   host: HostSystem
   subSpecs: list[HostSubSpecification] = []
   changeID: Optional[str] = None


class HostSpecificationManager(ManagedObject):
   def UpdateHostSpecification(self, host: HostSystem, hostSpec: HostSpecification) -> None: ...
   def UpdateHostSubSpecification(self, host: HostSystem, hostSubSpec: HostSubSpecification) -> None: ...
   def RetrieveHostSpecification(self, host: HostSystem, fromHost: bool) -> HostSpecification: ...
   def DeleteHostSubSpecification(self, host: HostSystem, subSpecName: str) -> None: ...
   def DeleteHostSpecification(self, host: HostSystem) -> None: ...
   def GetUpdatedHosts(self, startChangeID: Optional[str], endChangeID: Optional[str]) -> list[HostSystem]: ...


class HostSubSpecification(DynamicData):
   name: str
   createdTime: datetime
   data: list[byte] = []
   binaryData: Optional[binary] = None


class IpAddressProfile(ApplyProfile):
   pass


class IpRouteProfile(ApplyProfile):
   staticRoute: list[StaticRouteProfile] = []


class NasStorageProfile(ApplyProfile):
   key: str


class NetStackInstanceProfile(ApplyProfile):
   key: str
   dnsConfig: NetworkProfile.DnsConfigProfile
   ipRouteConfig: IpRouteProfile


class NetworkPolicyProfile(ApplyProfile):
   pass


class NetworkProfile(ApplyProfile):
   class DnsConfigProfile(ApplyProfile):
      pass

   vswitch: list[VirtualSwitchProfile] = []
   vmPortGroup: list[VmPortGroupProfile] = []
   hostPortGroup: list[HostPortGroupProfile] = []
   serviceConsolePortGroup: list[ServiceConsolePortGroupProfile] = []
   dnsConfig: Optional[DnsConfigProfile] = None
   ipRouteConfig: Optional[IpRouteProfile] = None
   consoleIpRouteConfig: Optional[IpRouteProfile] = None
   pnic: list[PhysicalNicProfile] = []
   dvswitch: list[DvsProfile] = []
   dvsServiceConsoleNic: list[DvsServiceConsoleVNicProfile] = []
   dvsHostNic: list[DvsHostVNicProfile] = []
   nsxHostNic: list[NsxHostVNicProfile] = []
   netStackInstance: list[NetStackInstanceProfile] = []
   opaqueSwitch: Optional[OpaqueSwitchProfile] = None


class NsxHostVNicProfile(ApplyProfile):
   key: str
   ipConfig: IpAddressProfile


class OpaqueSwitchProfile(ApplyProfile):
   pass


class OptionProfile(ApplyProfile):
   key: str


class PermissionProfile(ApplyProfile):
   key: str


class PhysicalNicProfile(ApplyProfile):
   key: str


class PnicUplinkProfile(ApplyProfile):
   key: str


class PortGroupProfile(ApplyProfile):
   class VlanProfile(ApplyProfile):
      pass

   class VirtualSwitchSelectionProfile(ApplyProfile):
      pass

   key: str
   name: str
   vlan: VlanProfile
   vswitch: VirtualSwitchSelectionProfile
   networkPolicy: NetworkPolicyProfile


class ProfileManager(ProfileManager):
   class TaskListRequirement(Enum):
      maintenanceModeRequired: ClassVar['TaskListRequirement'] = 'maintenanceModeRequired'
      rebootRequired: ClassVar['TaskListRequirement'] = 'rebootRequired'

   class ConfigTaskList(DynamicData):
      configSpec: Optional[ConfigSpec] = None
      taskDescription: list[LocalizableMessage] = []
      taskListRequirement: list[str] = []

   class AnswerFileCreateSpec(DynamicData):
      validating: Optional[bool] = None

   class AnswerFileOptionsCreateSpec(AnswerFileCreateSpec):
      userInput: list[DeferredPolicyOptionParameter] = []

   class AnswerFileSerializedCreateSpec(AnswerFileCreateSpec):
      answerFileConfigString: str

   class AnswerFileStatus(Enum):
      valid: ClassVar['AnswerFileStatus'] = 'valid'
      invalid: ClassVar['AnswerFileStatus'] = 'invalid'
      unknown: ClassVar['AnswerFileStatus'] = 'unknown'

   class EntityCustomizations(DynamicData):
      pass

   class StructuredCustomizations(EntityCustomizations):
      entity: ManagedEntity
      customizations: Optional[AnswerFile] = None

   class HostToConfigSpecMap(DynamicData):
      host: HostSystem
      configSpec: AnswerFileCreateSpec

   class ApplyHostConfigSpec(ExecuteResult):
      host: HostSystem
      taskListRequirement: list[str] = []
      taskDescription: list[LocalizableMessage] = []
      rebootStateless: Optional[bool] = None
      rebootHost: Optional[bool] = None
      faultData: Optional[MethodFault] = None

   class ApplyHostConfigResult(DynamicData):
      class Status(Enum):
         success: ClassVar['Status'] = 'success'
         failed: ClassVar['Status'] = 'failed'
         reboot_failed: ClassVar['Status'] = 'reboot_failed'
         stateless_reboot_failed: ClassVar['Status'] = 'stateless_reboot_failed'
         check_compliance_failed: ClassVar['Status'] = 'check_compliance_failed'
         state_not_satisfied: ClassVar['Status'] = 'state_not_satisfied'
         exit_maintenancemode_failed: ClassVar['Status'] = 'exit_maintenancemode_failed'
         canceled: ClassVar['Status'] = 'canceled'

      startTime: datetime
      completeTime: datetime
      host: HostSystem
      status: str
      errors: list[MethodFault] = []

   class CompositionValidationResult(DynamicData):
      class ResultElement(DynamicData):
         class Status(Enum):
            success: ClassVar['Status'] = 'success'
            error: ClassVar['Status'] = 'error'

         target: Profile
         status: str
         errors: list[LocalizableMessage] = []
         sourceDiffForToBeMerged: Optional[HostApplyProfile] = None
         targetDiffForToBeMerged: Optional[HostApplyProfile] = None
         toBeAdded: Optional[HostApplyProfile] = None
         toBeDeleted: Optional[HostApplyProfile] = None
         toBeDisabled: Optional[HostApplyProfile] = None
         toBeEnabled: Optional[HostApplyProfile] = None
         toBeReenableCC: Optional[HostApplyProfile] = None

      results: list[ResultElement] = []
      errors: list[LocalizableMessage] = []

   class CompositionResult(DynamicData):
      class ResultElement(DynamicData):
         class Status(Enum):
            success: ClassVar['Status'] = 'success'
            error: ClassVar['Status'] = 'error'

         target: Profile
         status: str
         errors: list[LocalizableMessage] = []

      errors: list[LocalizableMessage] = []
      results: list[ResultElement] = []

   def ApplyHostConfiguration(self, host: HostSystem, configSpec: ConfigSpec, userInput: list[DeferredPolicyOptionParameter]) -> Task: ...
   def GenerateConfigTaskList(self, configSpec: ConfigSpec, host: HostSystem) -> ConfigTaskList: ...
   def GenerateTaskList(self, configSpec: ConfigSpec, host: HostSystem) -> Task: ...
   def QueryProfileMetadata(self, profileName: list[type], profile: Optional[Profile]) -> list[ProfileMetadata]: ...
   def QueryProfileStructure(self, profile: Optional[Profile]) -> ProfileStructure: ...
   def CreateDefaultProfile(self, profileType: type, profileTypeName: Optional[str], profile: Optional[Profile]) -> ApplyProfile: ...
   def UpdateAnswerFile(self, host: HostSystem, configSpec: AnswerFileCreateSpec) -> Task: ...
   def RetrieveAnswerFile(self, host: HostSystem) -> Optional[AnswerFile]: ...
   def RetrieveAnswerFileForProfile(self, host: HostSystem, applyProfile: HostApplyProfile) -> Optional[AnswerFile]: ...
   def ExportAnswerFile(self, host: HostSystem) -> Task: ...
   def CheckAnswerFileStatus(self, host: list[HostSystem]) -> Task: ...
   def QueryAnswerFileStatus(self, host: list[HostSystem]) -> list[AnswerFileStatusResult]: ...
   def RetrieveHostCustomizations(self, hosts: list[HostSystem]) -> list[StructuredCustomizations]: ...
   def RetrieveHostCustomizationsForProfile(self, hosts: list[HostSystem], applyProfile: HostApplyProfile) -> list[StructuredCustomizations]: ...
   def GenerateHostConfigTaskSpec(self, hostsInfo: list[StructuredCustomizations]) -> Task: ...
   def ApplyEntitiesConfiguration(self, applyConfigSpecs: list[ApplyHostConfigSpec]) -> Task: ...
   def ValidateComposition(self, source: Profile, targets: list[Profile], toBeMerged: Optional[HostApplyProfile], toReplaceWith: Optional[HostApplyProfile], toBeDeleted: Optional[HostApplyProfile], enableStatusToBeCopied: Optional[HostApplyProfile], errorOnly: Optional[bool]) -> Task: ...
   def CompositeProfile(self, source: Profile, targets: list[Profile], toBeMerged: Optional[HostApplyProfile], toBeReplacedWith: Optional[HostApplyProfile], toBeDeleted: Optional[HostApplyProfile], enableStatusToBeCopied: Optional[HostApplyProfile]) -> Task: ...


class SecurityProfile(ApplyProfile):
   permission: list[PermissionProfile] = []

class ServiceConsolePortGroupProfile(PortGroupProfile):
   ipConfig: IpAddressProfile


class ServiceProfile(ApplyProfile):
   key: str


class StaticRouteProfile(ApplyProfile):
   key: Optional[str] = None


class StorageProfile(ApplyProfile):
   nasStorage: list[NasStorageProfile] = []


class UserGroupProfile(ApplyProfile):
   key: str


class UserProfile(ApplyProfile):
   key: str


class VirtualSwitchProfile(ApplyProfile):
   class LinkProfile(ApplyProfile):
      pass

   class NumPortsProfile(ApplyProfile):
      pass

   key: str
   name: str
   link: LinkProfile
   numPorts: NumPortsProfile
   networkPolicy: NetworkPolicyProfile

class VmPortGroupProfile(PortGroupProfile):
   pass
