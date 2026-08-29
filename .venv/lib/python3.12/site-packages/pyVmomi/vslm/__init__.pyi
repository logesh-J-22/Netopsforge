# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import auth as auth
from . import fault as fault
from . import vso as vso

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedMethod
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.vim import Datacenter
from pyVmomi.vim import Datastore

from pyVmomi.vim import ManagedEntity
from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.alarm import Alarm
from pyVmomi.vim.scheduler import ScheduledTask

from pyVmomi.vim.vslm import ID

from pyVmomi.vslm.auth import SessionManager

from pyVmomi.vslm.vso import VStorageObjectManager



class AboutInfo(DynamicData):
   name: str
   fullName: str
   vendor: str
   apiVersion: str
   instanceUuid: str


class QueryDatastoreInfoResult(DynamicData):
   datacenter: Datacenter
   datastore: Datastore


class ServiceInstance(ManagedObject):
   @property
   def content(self) -> ServiceInstanceContent: ...

   def RetrieveContent(self) -> ServiceInstanceContent: ...


class ServiceInstanceContent(DynamicData):
   aboutInfo: AboutInfo
   sessionManager: SessionManager
   vStorageObjectManager: VStorageObjectManager
   storageLifecycleManager: StorageLifecycleManager


class StorageLifecycleManager(ManagedObject):
   def SyncDatastore(self, datastoreUrl: str, fullSync: bool, fcdId: Optional[ID]) -> None: ...
   def QueryDatastoreInfo(self, datastoreUrl: str) -> list[QueryDatastoreInfoResult]: ...


class Task(ManagedObject):
   def QueryResult(self) -> Optional[object]: ...
   def QueryInfo(self) -> TaskInfo: ...
   def Cancel(self) -> None: ...


class TaskInfo(DynamicData):
   class State(Enum):
      queued: ClassVar['State'] = 'queued'
      running: ClassVar['State'] = 'running'
      success: ClassVar['State'] = 'success'
      error: ClassVar['State'] = 'error'

   key: str
   task: Task
   description: Optional[LocalizableMessage] = None
   name: Optional[ManagedMethod] = None
   descriptionId: str
   entity: Optional[ManagedEntity] = None
   entityName: Optional[str] = None
   locked: list[ManagedEntity] = []
   state: State
   cancelled: bool
   cancelable: bool
   error: Optional[MethodFault] = None
   result: Optional[object] = None
   progress: Optional[int] = None
   reason: TaskReason
   queueTime: datetime
   startTime: Optional[datetime] = None
   completeTime: Optional[datetime] = None
   eventChainId: int
   changeTag: Optional[str] = None
   parentTaskKey: Optional[str] = None
   rootTaskKey: Optional[str] = None
   activationId: Optional[str] = None


class TaskReason(DynamicData):
   pass


class TaskReasonAlarm(TaskReason):
   alarmName: str
   alarm: Alarm
   entityName: str
   entity: ManagedEntity


class TaskReasonSchedule(TaskReason):
   name: str
   scheduledTask: ScheduledTask

class TaskReasonSystem(TaskReason):
   pass

class TaskReasonUser(TaskReason):
   userName: str
