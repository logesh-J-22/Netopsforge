# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.eam import Agent

from pyVmomi.vim import ComputeResource

from pyVmomi.vim import Datastore

from pyVmomi.vim import Network
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import MethodFault

from pyVmomi.eam.issue import AgencyIssue



class AgentIssue(AgencyIssue):
   agent: Agent
   cluster: Optional[ComputeResource] = None

class CertificateNotTrusted(VmNotDeployed):
   url: str

class HostInMaintenanceMode(VmIssue):
   pass

class HostInPartialMaintenanceMode(VmIssue):
   pass

class InsufficientClusterResources(VmPoweredOff):
   pass

class InsufficientClusterSpace(VmNotDeployed):
   pass

class InvalidConfig(VmIssue):
   error: object


class MissingClusterVmDatastore(VmNotDeployed):
   missingDatastores: list[Datastore] = []


class MissingClusterVmNetwork(VmNotDeployed):
   missingNetworks: list[Network] = []
   networkNames: list[str] = []


class OvfInvalidProperty(AgentIssue):
   error: list[MethodFault] = []

class TransitionFailed(AgentIssue):
   pass

class VmHookFailed(VmIssue):
   pass

class VmHookTimedout(VmIssue):
   pass

class VmInaccessible(VmIssue):
   pass


class VmIssue(AgentIssue):
   vm: VirtualMachine

class VmNotDeployed(AgentIssue):
   pass

class VmNotRemoved(VmIssue):
   pass

class VmPoweredOff(VmIssue):
   pass

class VmPoweredOn(VmIssue):
   pass

class VmProtected(VmIssue):
   pass

class VmSuspended(VmIssue):
   pass
