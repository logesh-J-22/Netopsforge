# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ElementDescription

from pyVmomi.vmodl import DynamicData



class ArrayUpdateSpec(DynamicData):
   class Operation(Enum):
      add: ClassVar['Operation'] = 'add'
      remove: ClassVar['Operation'] = 'remove'
      edit: ClassVar['Operation'] = 'edit'

   operation: Operation
   removeKey: Optional[object] = None

class BoolOption(OptionType):
   supported: bool
   defaultValue: bool


class ChoiceOption(OptionType):
   choiceInfo: list[ElementDescription] = []
   defaultIndex: Optional[int] = None

class FloatOption(OptionType):
   min: float
   max: float
   defaultValue: float

class IntOption(OptionType):
   min: int
   max: int
   defaultValue: int


class LongOption(OptionType):
   min: long
   max: long
   defaultValue: long


class OptionDef(ElementDescription):
   optionType: OptionType


class OptionManager(ManagedObject):
   @property
   def supportedOption(self) -> list[OptionDef]: ...
   @property
   def setting(self) -> list[OptionValue]: ...

   def QueryView(self, name: Optional[str]) -> list[OptionValue]: ...
   def UpdateValues(self, changedValue: list[OptionValue]) -> None: ...


class OptionType(DynamicData):
   valueIsReadonly: Optional[bool] = None


class OptionValue(DynamicData):
   key: str
   value: Optional[object] = None


class StringOption(OptionType):
   defaultValue: str
   validCharacters: Optional[str] = None
