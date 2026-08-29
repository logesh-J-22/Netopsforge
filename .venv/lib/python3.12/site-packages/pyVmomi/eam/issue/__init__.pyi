# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import Optional
from pyVmomi.eam import Agency
from pyVmomi.eam import Agent
from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder

from pyVmomi.vim import HostSystem

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.vmodl import MethodFault


class AgencyDisabled(AgencyIssue):
   pass


class AgencyIssue(Issue):
   agency: Agency
   agencyName: str
   solutionId: str
   solutionName: str


class AgentIssue(AgencyIssue):
   agent: Agent
   agentName: str
   host: HostSystem
   hostName: str

class CannotAccessAgentOVF(VmNotDeployed):
   downloadUrl: str

class CannotAccessAgentVib(VibNotInstalled):
   downloadUrl: str

class CertificateNotTrusted(AgentIssue):
   url: str


class ExtensibleIssue(Issue):
   typeId: str
   argument: list[KeyAnyValue] = []
   target: Optional[ManagedEntity] = None
   agent: Optional[Agent] = None
   agency: Optional[Agency] = None

class HostInMaintenanceMode(VmDeployed):
   pass


class HostInPartialMaintenanceMode(AgentIssue):
   vm: Optional[VirtualMachine] = None

class HostInStandbyMode(VmDeployed):
   pass


class HostIssue(Issue):
   host: HostSystem

class HostNotReachable(AgentIssue):
   pass

class HostPoweredOff(VmDeployed):
   pass

class ImmediateHostRebootRequired(VibIssue):
   pass

class IncompatibleHostVersion(VmNotDeployed):
   pass


class InsufficientIpAddresses(VmPoweredOff):
   network: Network

class InsufficientResources(VmNotDeployed):
   pass

class InsufficientSpace(VmNotDeployed):
   pass

class InvalidConfig(VmIssue):
   error: object


class Issue(DynamicData):
   key: int
   description: str
   time: datetime


class MissingAgentIpPool(VmPoweredOff):
   network: Network

class MissingDvFilterSwitch(AgentIssue):
   pass

class NoAgentVmDatastore(VmNotDeployed):
   pass

class NoAgentVmNetwork(VmNotDeployed):
   pass


class NoCustomAgentVmDatastore(NoAgentVmDatastore):
   customAgentVmDatastore: list[Datastore] = []
   customAgentVmDatastoreName: list[str] = []


class NoCustomAgentVmNetwork(NoAgentVmNetwork):
   customAgentVmNetwork: list[Network] = []
   customAgentVmNetworkName: list[str] = []

class NoDiscoverableAgentVmDatastore(VmNotDeployed):
   pass

class NoDiscoverableAgentVmNetwork(VmNotDeployed):
   pass

class OrphanedAgency(AgencyIssue):
   pass

class OrphanedDvFilterSwitch(HostIssue):
   pass


class OvfInvalidFormat(VmNotDeployed):
   error: list[MethodFault] = []


class OvfInvalidProperty(AgentIssue):
   error: list[MethodFault] = []

class TransitionFailed(AgentIssue):
   pass


class UnknownAgentVm(HostIssue):
   vm: VirtualMachine

class VibCannotPutHostInMaintenanceMode(VibIssue):
   pass

class VibCannotPutHostOutOfMaintenanceMode(VibIssue):
   pass

class VibDependenciesNotMetByHost(VibNotInstalled):
   pass

class VibInvalidFormat(VibNotInstalled):
   pass

class VibIssue(AgentIssue):
   pass

class VibNotInstalled(VibIssue):
   pass

class VibRequirementsNotMetByHost(VibNotInstalled):
   pass

class VibRequiresHostInMaintenanceMode(VibIssue):
   pass

class VibRequiresHostReboot(VibIssue):
   pass

class VibRequiresManualInstallation(VibIssue):
   bulletin: list[str] = []

class VibRequiresManualUninstallation(VibIssue):
   bulletin: list[str] = []


class VmCorrupted(VmIssue):
   missingFile: Optional[str] = None

class VmDeployed(VmIssue):
   pass

class VmHookFailed(VmIssue):
   pass

class VmHookTimedout(VmIssue):
   pass

class VmInaccessible(VmIssue):
   pass


class VmIssue(AgentIssue):
   vm: VirtualMachine

class VmMarkedAsTemplate(VmIssue):
   pass

class VmNotDeployed(AgentIssue):
   pass

class VmOrphaned(VmIssue):
   pass

class VmPoweredOff(VmIssue):
   pass

class VmPoweredOn(VmIssue):
   pass

class VmProtected(VmIssue):
   pass

class VmRequiresHostOutOfMaintenanceMode(VmNotDeployed):
   pass

class VmSuspended(VmIssue):
   pass


class VmWrongFolder(VmIssue):
   currentFolder: Folder
   requiredFolder: Folder


class VmWrongResourcePool(VmIssue):
   currentResourcePool: ResourcePool
   requiredResourcePool: ResourcePool
