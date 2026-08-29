# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import long

from pyVmomi.pbm import ExtendedElementDescription

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.pbm.profile import CapabilityBasedProfileCreateSpec
from pyVmomi.pbm.profile import CapabilityConstraints
from pyVmomi.pbm.profile import ProfileId

from pyVmomi.vim.vm.replication import ReplicationGroupId



class CapabilityConstraintsRequirement(Requirement):
   constraints: CapabilityConstraints


class CapabilityProfileRequirement(Requirement):
   profileId: ProfileId


class CompatibilityResult(DynamicData):
   hub: PlacementHub
   hubInfo: Optional[PlacementHubInfo] = None
   matchingResources: list[MatchingResources] = []
   howMany: Optional[long] = None
   utilization: list[ResourceUtilization] = []
   warning: list[MethodFault] = []
   error: list[MethodFault] = []


class MatchingReplicationResources(MatchingResources):
   replicationGroup: list[ReplicationGroupId] = []


class MatchingResources(DynamicData):
   pass


class PlacementHub(DynamicData):
   hubType: str
   hubId: str


class PlacementHubInfo(DynamicData):
   zoneClusters: list[ServerObjectRef] = []


class PlacementSolver(ManagedObject):
   def QueryMatchingHub(self, hubsToSearch: list[PlacementHub], profile: ProfileId) -> list[PlacementHub]: ...
   def QueryMatchingHubWithSpec(self, hubsToSearch: list[PlacementHub], createSpec: CapabilityBasedProfileCreateSpec) -> list[PlacementHub]: ...
   def CheckCompatibility(self, hubsToSearch: list[PlacementHub], profile: ProfileId) -> list[CompatibilityResult]: ...
   def CheckCompatibilityWithSpec(self, hubsToSearch: list[PlacementHub], profileSpec: CapabilityBasedProfileCreateSpec) -> list[CompatibilityResult]: ...
   def CheckRequirements(self, hubsToSearch: list[PlacementHub], placementSubjectRef: Optional[ServerObjectRef], placementSubjectRequirement: list[Requirement]) -> list[CompatibilityResult]: ...


class Requirement(DynamicData):
   pass


class ResourceUtilization(DynamicData):
   name: ExtendedElementDescription
   description: ExtendedElementDescription
   availableBefore: Optional[long] = None
   availableAfter: Optional[long] = None
   total: Optional[long] = None


class ZoneTopologyRequirement(CapabilityProfileRequirement):
   clusters: list[ServerObjectRef] = []
