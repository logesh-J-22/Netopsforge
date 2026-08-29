# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import provider as provider

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.pbm.capability import CapabilityInstance

from pyVmomi.pbm.placement import PlacementHub

from pyVmomi.pbm.capability.provider import CapabilityObjectMetadataPerCategory
from pyVmomi.pbm.capability.provider import CapabilityObjectSchema

from pyVmomi.pbm.profile.provider import DatastoreSpaceStatistics



class CapabilityBasedProfile(Profile):
   class ProfileCategoryEnum(Enum):
      REQUIREMENT: ClassVar['ProfileCategoryEnum'] = 'REQUIREMENT'
      RESOURCE: ClassVar['ProfileCategoryEnum'] = 'RESOURCE'
      DATA_SERVICE_POLICY: ClassVar['ProfileCategoryEnum'] = 'DATA_SERVICE_POLICY'

   class SystemCreatedProfileType(Enum):
      VsanDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'VsanDefaultProfile'
      VVolDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'VVolDefaultProfile'
      PmemDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'PmemDefaultProfile'
      VmcManagementProfile: ClassVar['SystemCreatedProfileType'] = 'VmcManagementProfile'
      VsanMaxDefaultProfile: ClassVar['SystemCreatedProfileType'] = 'VsanMaxDefaultProfile'
      VsanEsaAutoManagedRaidProfile: ClassVar['SystemCreatedProfileType'] = 'VsanEsaAutoManagedRaidProfile'

   profileCategory: str
   resourceType: ResourceType
   constraints: CapabilityConstraints
   generationId: Optional[long] = None
   isDefault: bool
   systemCreatedProfileType: Optional[str] = None
   lineOfService: Optional[str] = None
   k8sCompliantName: Optional[str] = None
   otherK8sCompliantNames: list[str] = []


class CapabilityBasedProfileCreateSpec(DynamicData):
   name: str
   description: Optional[str] = None
   category: Optional[str] = None
   resourceType: ResourceType
   constraints: CapabilityConstraints
   k8sCompliantName: Optional[str] = None


class CapabilityBasedProfileUpdateSpec(DynamicData):
   name: Optional[str] = None
   description: Optional[str] = None
   constraints: Optional[CapabilityConstraints] = None


class CapabilityConstraints(DynamicData):
   pass


class DataServiceToPoliciesMap(DynamicData):
   dataServicePolicy: ProfileId
   parentStoragePolicies: list[ProfileId] = []
   fault: Optional[MethodFault] = None

class DefaultCapabilityBasedProfile(CapabilityBasedProfile):
   vvolType: list[str] = []
   containerId: str


class DefaultProfileInfo(DynamicData):
   datastores: list[PlacementHub] = []
   defaultProfile: Optional[Profile] = None
   methodFault: Optional[MethodFault] = None


class Profile(DynamicData):
   profileId: ProfileId
   name: str
   description: Optional[str] = None
   creationTime: datetime
   createdBy: str
   lastUpdatedTime: datetime
   lastUpdatedBy: str


class ProfileId(DynamicData):
   uniqueId: str


class ProfileK8sCompliantNameSpec(DynamicData):
   profileId: str
   k8sCompliantName: str
   otherK8sCompliantNames: list[str] = []


class ProfileManager(ManagedObject):
   def FetchResourceType(self) -> list[ResourceType]: ...
   def FetchVendorInfo(self, resourceType: Optional[ResourceType]) -> list[CapabilityObjectSchema.VendorResourceTypeInfo]: ...
   def FetchCapabilityMetadata(self, resourceType: Optional[ResourceType], vendorUuid: Optional[str]) -> list[CapabilityObjectMetadataPerCategory]: ...
   def FetchCapabilitySchema(self, vendorUuid: Optional[str], lineOfService: list[str]) -> list[CapabilityObjectSchema]: ...
   def Create(self, createSpec: CapabilityBasedProfileCreateSpec) -> ProfileId: ...
   def Update(self, profileId: ProfileId, updateSpec: CapabilityBasedProfileUpdateSpec) -> None: ...
   def Delete(self, profileId: list[ProfileId]) -> list[ProfileOperationOutcome]: ...
   def QueryProfile(self, resourceType: ResourceType, profileCategory: Optional[str]) -> list[ProfileId]: ...
   def RetrieveContent(self, profileIds: list[ProfileId]) -> list[Profile]: ...
   def QueryAssociatedProfiles(self, entities: list[ServerObjectRef]) -> list[QueryProfileResult]: ...
   def QueryAssociatedProfile(self, entity: ServerObjectRef) -> list[ProfileId]: ...
   def QueryAssociatedEntity(self, profile: ProfileId, entityType: Optional[str]) -> list[ServerObjectRef]: ...
   def QueryDefaultRequirementProfile(self, hub: PlacementHub) -> Optional[ProfileId]: ...
   def ResetDefaultRequirementProfile(self, profile: Optional[ProfileId]) -> None: ...
   def AssignDefaultRequirementProfile(self, profile: ProfileId, datastores: list[PlacementHub]) -> None: ...
   def FindApplicableDefaultProfile(self, datastores: list[PlacementHub]) -> list[Profile]: ...
   def QueryDefaultRequirementProfiles(self, datastores: list[PlacementHub]) -> list[DefaultProfileInfo]: ...
   def ResetVSanDefaultProfile(self) -> None: ...
   def QuerySpaceStatsForStorageContainer(self, datastore: ServerObjectRef, capabilityProfileId: list[ProfileId]) -> list[DatastoreSpaceStatistics]: ...
   def QueryAssociatedEntities(self, profiles: list[ProfileId]) -> list[QueryProfileResult]: ...


class ProfileOperationOutcome(DynamicData):
   profileId: ProfileId
   fault: Optional[MethodFault] = None


class ProfileType(DynamicData):
   uniqueId: str


class QueryProfileResult(DynamicData):
   object: ServerObjectRef
   profileId: list[ProfileId] = []
   fault: Optional[MethodFault] = None


class ResourceType(DynamicData):
   resourceType: str

class ResourceTypeEnum:
   pass


class SubProfileCapabilityConstraints(CapabilityConstraints):
   class SubProfile(DynamicData):
      name: str
      capability: list[CapabilityInstance] = []
      forceProvision: Optional[bool] = None

   subProfiles: list[SubProfile] = []
