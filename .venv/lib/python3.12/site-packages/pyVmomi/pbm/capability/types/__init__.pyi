# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.pbm import ExtendedElementDescription

from pyVmomi.vmodl import DynamicData


class BuiltinGenericTypesEnum:
   pass

class BuiltinTypesEnum:
   pass


class DescriptiveValue(DynamicData):
   description: ExtendedElementDescription
   value: object


class DiscreteSet(DynamicData):
   values: list[object] = []


class Range(DynamicData):
   min: object
   max: object


class TimeSpan(DynamicData):
   value: int
   unit: str

class TimeUnitEnum:
   pass
