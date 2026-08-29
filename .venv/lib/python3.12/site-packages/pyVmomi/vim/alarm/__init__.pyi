# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import PropertyPath
from pyVmomi.vim import ElementDescription
from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim import PerformanceManager
from pyVmomi.vim import TypeDescription
from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.action import Action



class Alarm(ExtensibleManagedObject):
   @property
   def info(self) -> AlarmInfo: ...

   def Remove(self) -> None: ...
   def Reconfigure(self, spec: AlarmSpec) -> None: ...


class AlarmAction(DynamicData):
   pass


class AlarmDescription(DynamicData):
   expr: list[TypeDescription] = []
   stateOperator: list[ElementDescription] = []
   metricOperator: list[ElementDescription] = []
   hostSystemConnectionState: list[ElementDescription] = []
   virtualMachinePowerState: list[ElementDescription] = []
   datastoreConnectionState: list[ElementDescription] = []
   hostSystemPowerState: list[ElementDescription] = []
   virtualMachineGuestHeartbeatStatus: list[ElementDescription] = []
   entityStatus: list[ElementDescription] = []
   action: list[TypeDescription] = []


class AlarmExpression(DynamicData):
   pass


class AlarmFilterSpec(DynamicData):
   class AlarmTypeByEntity(Enum):
      entityTypeAll: ClassVar['AlarmTypeByEntity'] = 'entityTypeAll'
      entityTypeHost: ClassVar['AlarmTypeByEntity'] = 'entityTypeHost'
      entityTypeVm: ClassVar['AlarmTypeByEntity'] = 'entityTypeVm'

   class AlarmTypeByTrigger(Enum):
      triggerTypeAll: ClassVar['AlarmTypeByTrigger'] = 'triggerTypeAll'
      triggerTypeEvent: ClassVar['AlarmTypeByTrigger'] = 'triggerTypeEvent'
      triggerTypeMetric: ClassVar['AlarmTypeByTrigger'] = 'triggerTypeMetric'

   status: list[ManagedEntity.Status] = []
   typeEntity: Optional[str] = None
   typeTrigger: Optional[str] = None


class AlarmInfo(AlarmSpec):
   key: str
   alarm: Alarm
   entity: ManagedEntity
   lastModifiedTime: datetime
   lastModifiedUser: str
   creationEventId: int


class AlarmManager(ManagedObject):
   @property
   def defaultExpression(self) -> list[AlarmExpression]: ...
   @property
   def description(self) -> AlarmDescription: ...

   def Create(self, entity: ManagedEntity, spec: AlarmSpec) -> Alarm: ...
   def GetAlarm(self, entity: Optional[ManagedEntity]) -> list[Alarm]: ...
   def GetAlarmActionsEnabled(self, entity: ManagedEntity) -> bool: ...
   def SetAlarmActionsEnabled(self, entity: ManagedEntity, enabled: bool) -> None: ...
   def GetAlarmState(self, entity: ManagedEntity) -> list[AlarmState]: ...
   def AcknowledgeAlarm(self, alarm: Alarm, entity: ManagedEntity) -> None: ...
   def ClearTriggeredAlarms(self, filter: AlarmFilterSpec) -> None: ...
   def DisableAlarm(self, alarm: Alarm, entity: ManagedEntity) -> None: ...
   def EnableAlarm(self, alarm: Alarm, entity: ManagedEntity) -> None: ...


class AlarmSetting(DynamicData):
   toleranceRange: int
   reportingFrequency: int


class AlarmSpec(DynamicData):
   name: str
   systemName: Optional[str] = None
   description: str
   enabled: bool
   expression: AlarmExpression
   action: Optional[AlarmAction] = None
   actionFrequency: Optional[int] = None
   setting: Optional[AlarmSetting] = None


class AlarmState(DynamicData):
   key: str
   entity: ManagedEntity
   alarm: Alarm
   overallStatus: ManagedEntity.Status
   time: datetime
   acknowledged: Optional[bool] = None
   acknowledgedByUser: Optional[str] = None
   acknowledgedTime: Optional[datetime] = None
   eventKey: Optional[int] = None
   disabled: Optional[bool] = None


class AlarmTriggeringAction(AlarmAction):
   class TransitionSpec(DynamicData):
      startState: ManagedEntity.Status
      finalState: ManagedEntity.Status
      repeats: bool

   action: Action
   transitionSpecs: list[TransitionSpec] = []
   green2yellow: bool
   yellow2red: bool
   red2yellow: bool
   yellow2green: bool

class AndAlarmExpression(AlarmExpression):
   expression: list[AlarmExpression] = []


class EventAlarmExpression(AlarmExpression):
   class ComparisonOperator(Enum):
      equals: ClassVar['ComparisonOperator'] = 'equals'
      notEqualTo: ClassVar['ComparisonOperator'] = 'notEqualTo'
      startsWith: ClassVar['ComparisonOperator'] = 'startsWith'
      doesNotStartWith: ClassVar['ComparisonOperator'] = 'doesNotStartWith'
      endsWith: ClassVar['ComparisonOperator'] = 'endsWith'
      doesNotEndWith: ClassVar['ComparisonOperator'] = 'doesNotEndWith'

   class Comparison(DynamicData):
      attributeName: str
      operator: str
      value: str

   comparisons: list[Comparison] = []
   eventType: type
   eventTypeId: Optional[str] = None
   objectType: Optional[type] = None
   status: Optional[ManagedEntity.Status] = None

class GroupAlarmAction(AlarmAction):
   action: list[AlarmAction] = []


class MetricAlarmExpression(AlarmExpression):
   class MetricOperator(Enum):
      isAbove: ClassVar['MetricOperator'] = 'isAbove'
      isBelow: ClassVar['MetricOperator'] = 'isBelow'

   operator: MetricOperator
   type: type
   metric: PerformanceManager.MetricId
   yellow: Optional[int] = None
   yellowInterval: Optional[int] = None
   red: Optional[int] = None
   redInterval: Optional[int] = None

class OrAlarmExpression(AlarmExpression):
   expression: list[AlarmExpression] = []


class StateAlarmExpression(AlarmExpression):
   class StateOperator(Enum):
      isEqual: ClassVar['StateOperator'] = 'isEqual'
      isUnequal: ClassVar['StateOperator'] = 'isUnequal'

   operator: StateOperator
   type: type
   statePath: PropertyPath
   yellow: Optional[str] = None
   red: Optional[str] = None
