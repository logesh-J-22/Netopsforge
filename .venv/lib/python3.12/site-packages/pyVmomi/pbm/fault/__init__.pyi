# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault
from pyVmomi.pbm.capability import CapabilityMetadata
from pyVmomi.pbm.capability import PropertyInstance
from pyVmomi.pbm.placement import PlacementHub

from pyVmomi.pbm.profile import ProfileId

from pyVmomi.vmodl.fault import SecurityError



class AlreadyExists(PBMFault):
   name: Optional[str] = None


class CapabilityProfilePropertyMismatchFault(PropertyMismatchFault):
   resourcePropertyInstance: PropertyInstance


class CompatibilityCheckFault(PBMFault):
   hub: PlacementHub

class DefaultProfileAppliesFault(CompatibilityCheckFault):
   pass

class DuplicateName(PBMFault):
   name: str

class IncompatibleVendorSpecificRuleSet(CapabilityProfilePropertyMismatchFault):
   pass

class InvalidLogin(PBMFault):
   pass


class LegacyHubsNotSupported(PBMFault):
   hubs: list[PlacementHub] = []


class NoPermission(SecurityError):
   class EntityPrivileges(DynamicData):
      profileId: Optional[ProfileId] = None
      privilegeIds: list[str] = []

   missingPrivileges: list[EntityPrivileges] = []


class NonExistentHubs(PBMFault):
   hubs: list[PlacementHub] = []

class NotFound(PBMFault):
   pass


class PBMFault(MethodFault):
   pass

class ProfileStorageFault(PBMFault):
   pass


class PropertyMismatchFault(CompatibilityCheckFault):
   capabilityInstanceId: CapabilityMetadata.UniqueId
   requirementPropertyInstance: PropertyInstance


class ResourceInUse(PBMFault):
   type: Optional[type] = None
   name: Optional[str] = None
