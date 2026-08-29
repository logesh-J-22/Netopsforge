# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import cluster as cluster
from . import host as host

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vim import ExtendedDescription

from pyVmomi.vim import ExtendedElementDescription

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue
from pyVmomi.vmodl import LocalizableMessage



class ApplyProfile(DynamicData):
   enabled: bool
   policy: list[Policy] = []
   profileTypeName: Optional[str] = None
   profileVersion: Optional[str] = None
   property: list[ApplyProfileProperty] = []
   favorite: Optional[bool] = None
   toBeMerged: Optional[bool] = None
   toReplaceWith: Optional[bool] = None
   toBeDeleted: Optional[bool] = None
   copyEnableStatus: Optional[bool] = None
   hidden: Optional[bool] = None

class ApplyProfileElement(ApplyProfile):
   key: str


class ApplyProfileProperty(DynamicData):
   propertyName: str
   array: bool
   profile: list[ApplyProfile] = []


class ComplianceLocator(DynamicData):
   expressionName: str
   applyPath: ProfilePropertyPath


class ComplianceManager(ManagedObject):
   def CheckCompliance(self, profile: list[Profile], entity: list[ManagedEntity]) -> Task: ...
   def QueryComplianceStatus(self, profile: list[Profile], entity: list[ManagedEntity]) -> list[ComplianceResult]: ...
   def ClearComplianceStatus(self, profile: list[Profile], entity: list[ManagedEntity]) -> None: ...
   def QueryExpressionMetadata(self, expressionName: list[str], profile: Optional[Profile]) -> list[ExpressionMetadata]: ...


class ComplianceProfile(DynamicData):
   expression: list[Expression] = []
   rootExpression: str


class ComplianceResult(DynamicData):
   class Status(Enum):
      compliant: ClassVar['Status'] = 'compliant'
      nonCompliant: ClassVar['Status'] = 'nonCompliant'
      unknown: ClassVar['Status'] = 'unknown'
      running: ClassVar['Status'] = 'running'

   class ComplianceFailure(DynamicData):
      class ComplianceFailureValues(DynamicData):
         comparisonIdentifier: str
         profileInstance: Optional[str] = None
         hostValue: Optional[object] = None
         profileValue: Optional[object] = None

      failureType: str
      message: LocalizableMessage
      expressionName: Optional[str] = None
      failureValues: list[ComplianceFailureValues] = []

   profile: Optional[Profile] = None
   complianceStatus: str
   entity: Optional[ManagedEntity] = None
   checkTime: Optional[datetime] = None
   failure: list[ComplianceFailure] = []

class CompositeExpression(Expression):
   operator: str
   expressionName: list[str] = []


class CompositePolicyOption(PolicyOption):
   option: list[PolicyOption] = []

class CompositePolicyOptionMetadata(PolicyOptionMetadata):
   option: list[str] = []


class DeferredPolicyOptionParameter(DynamicData):
   inputPath: ProfilePropertyPath
   parameter: list[KeyAnyValue] = []


class Expression(DynamicData):
   id: str
   displayName: str
   negated: bool


class ExpressionMetadata(DynamicData):
   expressionId: ExtendedElementDescription
   parameter: list[ParameterMetadata] = []

class NumericComparator:
   pass


class ParameterMetadata(DynamicData):
   class RelationType(Enum):
      dynamic_relation: ClassVar['RelationType'] = 'dynamic_relation'
      extensible_relation: ClassVar['RelationType'] = 'extensible_relation'
      localizable_relation: ClassVar['RelationType'] = 'localizable_relation'
      static_relation: ClassVar['RelationType'] = 'static_relation'
      validation_relation: ClassVar['RelationType'] = 'validation_relation'

   class ParameterRelationMetadata(DynamicData):
      relationTypes: list[str] = []
      values: list[object] = []
      path: Optional[ProfilePropertyPath] = None
      minCount: int
      maxCount: int

   id: ExtendedElementDescription
   type: type
   optional: bool
   defaultValue: Optional[object] = None
   hidden: Optional[bool] = None
   securitySensitive: Optional[bool] = None
   readOnly: Optional[bool] = None
   parameterRelations: list[ParameterRelationMetadata] = []


class Policy(DynamicData):
   id: str
   policyOption: PolicyOption


class PolicyMetadata(DynamicData):
   id: ExtendedElementDescription
   possibleOption: list[PolicyOptionMetadata] = []


class PolicyOption(DynamicData):
   id: str
   parameter: list[KeyAnyValue] = []


class PolicyOptionMetadata(DynamicData):
   id: ExtendedElementDescription
   parameter: list[ParameterMetadata] = []


class Profile(ManagedObject):
   class CreateSpec(DynamicData):
      name: Optional[str] = None
      annotation: Optional[str] = None
      enabled: Optional[bool] = None

   class SerializedCreateSpec(CreateSpec):
      profileConfigString: str

   class ConfigInfo(DynamicData):
      name: str
      annotation: Optional[str] = None
      enabled: bool

   class Description(DynamicData):
      class Section(DynamicData):
         description: ExtendedElementDescription
         message: list[LocalizableMessage] = []

      section: list[Section] = []

   @property
   def config(self) -> ConfigInfo: ...
   @property
   def description(self) -> Optional[Description]: ...
   @property
   def name(self) -> str: ...
   @property
   def createdTime(self) -> datetime: ...
   @property
   def modifiedTime(self) -> datetime: ...
   @property
   def entity(self) -> list[ManagedEntity]: ...
   @property
   def complianceStatus(self) -> str: ...

   def RetrieveDescription(self) -> Optional[Description]: ...
   def Destroy(self) -> None: ...
   def AssociateEntities(self, entity: list[ManagedEntity]) -> None: ...
   def DissociateEntities(self, entity: list[ManagedEntity]) -> None: ...
   def CheckCompliance(self, entity: list[ManagedEntity]) -> Task: ...
   def ExportProfile(self) -> str: ...


class ProfileManager(ManagedObject):
   @property
   def profile(self) -> list[Profile]: ...

   def CreateProfile(self, createSpec: Profile.CreateSpec) -> Profile: ...
   def QueryPolicyMetadata(self, policyName: list[str], profile: Optional[Profile]) -> list[PolicyMetadata]: ...
   def FindAssociatedProfile(self, entity: ManagedEntity) -> list[Profile]: ...


class ProfileMetadata(DynamicData):
   class ProfileSortSpec(DynamicData):
      policyId: str
      parameter: str

   class ProfileOperationMessage(DynamicData):
      operationName: str
      message: LocalizableMessage

   key: type
   profileTypeName: Optional[str] = None
   description: Optional[ExtendedDescription] = None
   sortSpec: list[ProfileSortSpec] = []
   profileCategory: Optional[str] = None
   profileComponent: Optional[str] = None
   operationMessages: list[ProfileOperationMessage] = []


class ProfilePropertyPath(DynamicData):
   profilePath: PropertyPath
   policyId: Optional[str] = None
   parameterId: Optional[str] = None
   policyOptionId: Optional[str] = None


class ProfileStructure(DynamicData):
   profileTypeName: str
   child: list[ProfileStructureProperty] = []


class ProfileStructureProperty(DynamicData):
   propertyName: str
   array: bool
   element: ProfileStructure


class SimpleExpression(Expression):
   expressionType: str
   parameter: list[KeyAnyValue] = []


class UserInputRequiredParameterMetadata(PolicyOptionMetadata):
   userInputParameter: list[ParameterMetadata] = []
