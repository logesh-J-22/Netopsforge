# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import long

from pyVmomi.pbm import ExtendedElementDescription

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.pbm.capability import CapabilityInstance

from pyVmomi.pbm.profile import ProfileId



class ComplianceManager(ManagedObject):
   def CheckCompliance(self, entities: list[ServerObjectRef], profile: Optional[ProfileId]) -> list[ComplianceResult]: ...
   def FetchComplianceResult(self, entities: list[ServerObjectRef], profile: Optional[ProfileId]) -> list[ComplianceResult]: ...
   def CheckRollupCompliance(self, entity: list[ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def FetchRollupComplianceResult(self, entity: list[ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def QueryByRollupComplianceStatus(self, status: str) -> list[ServerObjectRef]: ...


class ComplianceResult(DynamicData):
   class ComplianceStatus(Enum):
      compliant: ClassVar['ComplianceStatus'] = 'compliant'
      nonCompliant: ClassVar['ComplianceStatus'] = 'nonCompliant'
      unknown: ClassVar['ComplianceStatus'] = 'unknown'
      notApplicable: ClassVar['ComplianceStatus'] = 'notApplicable'
      outOfDate: ClassVar['ComplianceStatus'] = 'outOfDate'

   class ComplianceTaskStatus(Enum):
      inProgress: ClassVar['ComplianceTaskStatus'] = 'inProgress'
      success: ClassVar['ComplianceTaskStatus'] = 'success'
      failed: ClassVar['ComplianceTaskStatus'] = 'failed'

   checkTime: datetime
   entity: ServerObjectRef
   profile: Optional[ProfileId] = None
   complianceTaskStatus: Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[PolicyStatus] = []
   errorCause: list[MethodFault] = []
   operationalStatus: Optional[OperationalStatus] = None
   info: Optional[ExtendedElementDescription] = None


class FetchEntityHealthStatusSpec(DynamicData):
   objectRef: ServerObjectRef
   backingId: Optional[str] = None


class OperationalStatus(DynamicData):
   healthy: Optional[bool] = None
   operationETA: Optional[datetime] = None
   operationProgress: Optional[long] = None
   transitional: Optional[bool] = None


class PolicyStatus(DynamicData):
   expectedValue: CapabilityInstance
   currentValue: Optional[CapabilityInstance] = None


class RollupComplianceResult(DynamicData):
   oldestCheckTime: datetime
   entity: ServerObjectRef
   overallComplianceStatus: str
   overallComplianceTaskStatus: Optional[str] = None
   result: list[ComplianceResult] = []
   errorCause: list[MethodFault] = []
   profileMismatch: bool
