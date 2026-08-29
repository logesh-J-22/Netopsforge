# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import fault as fault
from . import query as query

from typing import Optional

from pyVmomi.VmomiSupport import DataObject
from pyVmomi.VmomiSupport import PropertyPath


class DataObject:
   pass


class DynamicArray(DataObject):
   dynamicType: Optional[str] = None
   val: list[object] = []


class DynamicData(DataObject):
   dynamicType: Optional[str] = None
   dynamicProperty: list[DynamicProperty] = []


class DynamicProperty(DataObject):
   name: PropertyPath
   val: object

class KeyAnyValue(DynamicData):
   key: str
   value: object


class LocalizableMessage(DynamicData):
   key: str
   arg: list[KeyAnyValue] = []
   message: Optional[str] = None


class LocalizedMethodFault(DynamicData):
   fault: MethodFault
   localizedMessage: Optional[str] = None

class ManagedObject:
   pass


class MethodFault(Exception):
   faultCause: Optional[MethodFault] = None
   faultMessage: list[LocalizableMessage] = []

class RuntimeFault(MethodFault):
   pass
