# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.eam import Agent

from pyVmomi.vim import ComputeResource
from pyVmomi.vmodl import MethodFault
from pyVmomi.vmodl import RuntimeFault



class CertificateNotTrustedFault(EamAppFault):
   url: Optional[str] = None


class DisabledClusterFault(EamAppFault):
   disabledComputeResource: list[ComputeResource] = []

class EamAppFault(EamRuntimeFault):
   pass


class EamFault(MethodFault):
   pass

class EamIOFault(EamRuntimeFault):
   pass


class EamRuntimeFault(RuntimeFault):
   pass

class EamServiceNotInitialized(EamRuntimeFault):
   pass

class EamSystemFault(EamRuntimeFault):
   pass


class InvalidAgencyScope(EamFault):
   unknownComputeResource: list[ComputeResource] = []


class InvalidAgentConfiguration(EamFault):
   invalidAgentConfiguration: Optional[Agent.ConfigInfo] = None
   invalidField: Optional[str] = None

class InvalidLogin(EamRuntimeFault):
   pass

class InvalidState(EamAppFault):
   pass


class InvalidUrl(EamFault):
   url: str
   malformedUrl: bool
   unknownHost: bool
   connectionRefused: bool
   responseCode: Optional[int] = None

class InvalidVibPackage(EamRuntimeFault):
   pass

class NoConnectionToVCenter(EamRuntimeFault):
   pass

class NotAuthorized(EamRuntimeFault):
   pass
