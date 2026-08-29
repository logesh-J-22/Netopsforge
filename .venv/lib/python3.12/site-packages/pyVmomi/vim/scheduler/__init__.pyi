# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar

from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.vim import ElementDescription
from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task
from pyVmomi.vim import TaskInfo
from pyVmomi.vim import TypeDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.action import Action


class AfterStartupTaskScheduler(TaskScheduler):
   minute: int

class DailyTaskScheduler(HourlyTaskScheduler):
   hour: int

class HourlyTaskScheduler(RecurrentTaskScheduler):
   minute: int

class MonthlyByDayTaskScheduler(MonthlyTaskScheduler):
   day: int


class MonthlyByWeekdayTaskScheduler(MonthlyTaskScheduler):
   class DayOfWeek(Enum):
      sunday: ClassVar['DayOfWeek'] = 'sunday'
      monday: ClassVar['DayOfWeek'] = 'monday'
      tuesday: ClassVar['DayOfWeek'] = 'tuesday'
      wednesday: ClassVar['DayOfWeek'] = 'wednesday'
      thursday: ClassVar['DayOfWeek'] = 'thursday'
      friday: ClassVar['DayOfWeek'] = 'friday'
      saturday: ClassVar['DayOfWeek'] = 'saturday'

   class WeekOfMonth(Enum):
      first: ClassVar['WeekOfMonth'] = 'first'
      second: ClassVar['WeekOfMonth'] = 'second'
      third: ClassVar['WeekOfMonth'] = 'third'
      fourth: ClassVar['WeekOfMonth'] = 'fourth'
      last: ClassVar['WeekOfMonth'] = 'last'

   offset: WeekOfMonth
   weekday: DayOfWeek

class MonthlyTaskScheduler(DailyTaskScheduler):
   pass


class OnceTaskScheduler(TaskScheduler):
   runAt: Optional[datetime] = None

class RecurrentTaskScheduler(TaskScheduler):
   interval: int


class ScheduledTask(ExtensibleManagedObject):
   @property
   def info(self) -> ScheduledTaskInfo: ...

   def Remove(self) -> None: ...
   def Reconfigure(self, spec: ScheduledTaskSpec) -> None: ...
   def Run(self) -> None: ...


class ScheduledTaskDescription(DynamicData):
   class SchedulerDetail(TypeDescription):
      frequency: str

   action: list[TypeDescription] = []
   schedulerInfo: list[SchedulerDetail] = []
   state: list[ElementDescription] = []
   dayOfWeek: list[ElementDescription] = []
   weekOfMonth: list[ElementDescription] = []


class ScheduledTaskInfo(ScheduledTaskSpec):
   scheduledTask: ScheduledTask
   entity: ManagedEntity
   lastModifiedTime: datetime
   lastModifiedUser: str
   nextRunTime: Optional[datetime] = None
   prevRunTime: Optional[datetime] = None
   state: TaskInfo.State
   error: Optional[MethodFault] = None
   result: Optional[object] = None
   progress: Optional[int] = None
   activeTask: Optional[Task] = None
   taskObject: ManagedObject


class ScheduledTaskManager(ManagedObject):
   @property
   def scheduledTask(self) -> list[ScheduledTask]: ...
   @property
   def description(self) -> ScheduledTaskDescription: ...

   def Create(self, entity: ManagedEntity, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveEntityScheduledTask(self, entity: Optional[ManagedEntity]) -> list[ScheduledTask]: ...
   def CreateObjectScheduledTask(self, obj: ManagedObject, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveObjectScheduledTask(self, obj: Optional[ManagedObject]) -> list[ScheduledTask]: ...


class ScheduledTaskSpec(DynamicData):
   name: str
   description: str
   enabled: bool
   scheduler: TaskScheduler
   action: Action
   notification: Optional[str] = None


class TaskScheduler(DynamicData):
   activeTime: Optional[datetime] = None
   expireTime: Optional[datetime] = None

class WeeklyTaskScheduler(DailyTaskScheduler):
   sunday: bool
   monday: bool
   tuesday: bool
   wednesday: bool
   thursday: bool
   friday: bool
   saturday: bool
