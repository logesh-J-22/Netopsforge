# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedMethod

from pyVmomi.vmodl import DynamicData



class Action(DynamicData):
   class ActionParameter(Enum):
      targetName: ClassVar['ActionParameter'] = 'targetName'
      alarmName: ClassVar['ActionParameter'] = 'alarmName'
      oldStatus: ClassVar['ActionParameter'] = 'oldStatus'
      newStatus: ClassVar['ActionParameter'] = 'newStatus'
      triggeringSummary: ClassVar['ActionParameter'] = 'triggeringSummary'
      declaringSummary: ClassVar['ActionParameter'] = 'declaringSummary'
      eventDescription: ClassVar['ActionParameter'] = 'eventDescription'
      target: ClassVar['ActionParameter'] = 'target'
      alarm: ClassVar['ActionParameter'] = 'alarm'

class CreateTaskAction(Action):
   taskTypeId: str
   cancelable: bool


class MethodAction(Action):
   name: ManagedMethod
   argument: list[MethodActionArgument] = []


class MethodActionArgument(DynamicData):
   value: Optional[object] = None

class RunScriptAction(Action):
   script: str

class SendEmailAction(Action):
   toList: str
   ccList: str
   subject: str
   body: str

class SendSNMPAction(Action):
   pass
