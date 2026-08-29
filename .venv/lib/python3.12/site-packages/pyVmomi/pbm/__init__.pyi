# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import auth as auth
from . import capability as capability
from . import compliance as compliance
from . import fault as fault
from . import placement as placement
from . import profile as profile
from . import provider as provider
from . import replication as replication

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.pbm.auth import SessionManager

from pyVmomi.pbm.capability import CapabilityMetadataManager

from pyVmomi.pbm.compliance import ComplianceManager

from pyVmomi.pbm.placement import PlacementSolver

from pyVmomi.pbm.profile import ProfileManager

from pyVmomi.pbm.replication import ReplicationManager



class AboutInfo(DynamicData):
   name: str
   version: str
   instanceUuid: str


class ExtendedElementDescription(DynamicData):
   label: str
   summary: str
   key: str
   messageCatalogKeyPrefix: str
   messageArg: list[KeyAnyValue] = []


class LoggingConfiguration(DynamicData):
   class Component(Enum):
      pbm: ClassVar['Component'] = 'pbm'
      vslm: ClassVar['Component'] = 'vslm'
      sms: ClassVar['Component'] = 'sms'
      spbm: ClassVar['Component'] = 'spbm'
      sps: ClassVar['Component'] = 'sps'
      httpclient_header: ClassVar['Component'] = 'httpclient_header'
      httpclient_content: ClassVar['Component'] = 'httpclient_content'
      vmomi: ClassVar['Component'] = 'vmomi'

   class LogLevel(Enum):
      INFO: ClassVar['LogLevel'] = 'INFO'
      DEBUG: ClassVar['LogLevel'] = 'DEBUG'
      TRACE: ClassVar['LogLevel'] = 'TRACE'

   component: str
   logLevel: str


class ServerObjectRef(DynamicData):
   class VvolType(Enum):
      Config: ClassVar['VvolType'] = 'Config'
      Data: ClassVar['VvolType'] = 'Data'
      Swap: ClassVar['VvolType'] = 'Swap'

   class ObjectType(Enum):
      virtualMachine: ClassVar['ObjectType'] = 'virtualMachine'
      virtualMachineAndDisks: ClassVar['ObjectType'] = 'virtualMachineAndDisks'
      virtualDiskId: ClassVar['ObjectType'] = 'virtualDiskId'
      virtualDiskUUID: ClassVar['ObjectType'] = 'virtualDiskUUID'
      datastore: ClassVar['ObjectType'] = 'datastore'
      vsanObjectId: ClassVar['ObjectType'] = 'vsanObjectId'
      fileShareId: ClassVar['ObjectType'] = 'fileShareId'
      host: ClassVar['ObjectType'] = 'host'
      cluster: ClassVar['ObjectType'] = 'cluster'
      unknown: ClassVar['ObjectType'] = 'unknown'

   objectType: str
   key: str
   serverUuid: Optional[str] = None


class ServiceInstance(ManagedObject):
   @property
   def content(self) -> ServiceInstanceContent: ...

   def RetrieveContent(self) -> ServiceInstanceContent: ...


class ServiceInstanceContent(DynamicData):
   aboutInfo: AboutInfo
   sessionManager: SessionManager
   capabilityMetadataManager: CapabilityMetadataManager
   profileManager: ProfileManager
   complianceManager: ComplianceManager
   placementSolver: PlacementSolver
   replicationManager: Optional[ReplicationManager] = None
