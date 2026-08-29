# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import provider as provider
from . import types as types

from typing import Optional
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.pbm import ExtendedElementDescription
from pyVmomi.vmodl import DynamicData



class CapabilityInstance(DynamicData):
   id: CapabilityMetadata.UniqueId
   constraint: list[ConstraintInstance] = []


class CapabilityMetadata(DynamicData):
   class UniqueId(DynamicData):
      namespace: str
      id: str

   id: UniqueId
   summary: ExtendedElementDescription
   mandatory: Optional[bool] = None
   hint: Optional[bool] = None
   keyId: Optional[str] = None
   allowMultipleConstraints: Optional[bool] = None
   propertyMetadata: list[PropertyMetadata] = []


class CapabilityMetadataManager(ManagedObject):
   pass


class ConstraintInstance(DynamicData):
   propertyInstance: list[PropertyInstance] = []

class GenericTypeInfo(TypeInfo):
   genericTypeName: str

class Operator:
   pass


class PropertyInstance(DynamicData):
   id: str
   operator: Optional[str] = None
   value: object


class PropertyMetadata(DynamicData):
   id: str
   summary: ExtendedElementDescription
   mandatory: bool
   type: Optional[TypeInfo] = None
   defaultValue: Optional[object] = None
   allowedValue: Optional[object] = None
   requirementsTypeHint: Optional[str] = None


class TypeInfo(DynamicData):
   typeName: str
