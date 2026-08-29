# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import Optional

from pyVmomi.vim import Datastore
from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.sms.provider import Provider
from pyVmomi.vim.vm.replication import DeviceGroupId

from pyVmomi.vim.vm.replication import FaultDomainId

from pyVmomi.vim.vm.replication import ReplicationGroupId



class DeviceId(DynamicData):
   pass


class FailoverParam(DynamicData):
   class ReplicationGroupData(DynamicData):
      groupId: ReplicationGroupId
      pitId: Optional[PointInTimeReplicaId] = None

   class PolicyAssociation(DynamicData):
      id: DeviceId
      policyId: str
      datastore: Datastore

   isPlanned: bool
   checkOnly: bool
   replicationGroupsToFailover: list[ReplicationGroupData] = []
   policyAssociations: list[PolicyAssociation] = []


class FailoverSuccessResult(GroupOperationResult):
   class RecoveredDiskInfo(DynamicData):
      deviceKey: int
      dsUrl: str
      diskPath: str

   class RecoveredDevice(DynamicData):
      targetDeviceId: Optional[ReplicaId] = None
      recoveredDeviceId: Optional[DeviceId] = None
      sourceDeviceId: DeviceId
      info: list[str] = []
      datastore: Datastore
      recoveredDiskInfo: list[RecoveredDiskInfo] = []
      error: Optional[MethodFault] = None
      warnings: list[MethodFault] = []

   newState: str
   pitId: Optional[PointInTimeReplicaId] = None
   pitIdBeforeFailover: Optional[PointInTimeReplicaId] = None
   recoveredDeviceInfo: list[RecoveredDevice] = []
   timeStamp: Optional[datetime] = None


class FaultDomainInfo(FaultDomainId):
   name: Optional[str] = None
   description: Optional[str] = None
   storageArrayId: Optional[str] = None
   children: list[FaultDomainId] = []
   provider: Optional[Provider] = None


class GroupErrorResult(GroupOperationResult):
   error: list[MethodFault] = []


class GroupInfo(DynamicData):
   groupId: ReplicationGroupId


class GroupOperationResult(DynamicData):
   groupId: ReplicationGroupId
   warning: list[MethodFault] = []


class PointInTimeReplicaId(DynamicData):
   id: str


class PromoteParam(DynamicData):
   isPlanned: bool
   replicationGroupsToPromote: list[ReplicationGroupId] = []


class QueryPointInTimeReplicaParam(DynamicData):
   class ReplicaQueryIntervalParam(DynamicData):
      fromDate: Optional[datetime] = None
      toDate: Optional[datetime] = None
      number: Optional[int] = None

   replicaTimeQueryParam: Optional[ReplicaQueryIntervalParam] = None
   pitName: Optional[str] = None
   tags: list[str] = []
   preferDetails: Optional[bool] = None


class QueryPointInTimeReplicaSuccessResult(GroupOperationResult):
   class PointInTimeReplicaInfo(DynamicData):
      id: PointInTimeReplicaId
      pitName: str
      timeStamp: datetime
      tags: list[str] = []

   replicaInfo: list[PointInTimeReplicaInfo] = []


class QueryPointInTimeReplicaSummaryResult(GroupOperationResult):
   class ReplicaIntervalQueryResult(DynamicData):
      fromDate: datetime
      toDate: datetime
      number: int

   intervalResults: list[ReplicaIntervalQueryResult] = []

class QueryReplicationGroupSuccessResult(GroupOperationResult):
   rgInfo: GroupInfo


class QueryReplicationPeerResult(DynamicData):
   sourceDomain: FaultDomainId
   targetDomain: list[FaultDomainId] = []
   error: list[MethodFault] = []
   warning: list[MethodFault] = []


class RecoveredTargetGroupMemberInfo(TargetGroupMemberInfo):
   recoveredDeviceId: Optional[DeviceId] = None


class ReplicaId(DynamicData):
   id: str

class ReplicationState:
   pass


class ReverseReplicationSuccessResult(GroupOperationResult):
   newGroupId: DeviceGroupId


class SourceGroupInfo(GroupInfo):
   class ReplicationTargetInfo(DynamicData):
      targetGroupId: ReplicationGroupId
      replicationAgreementDescription: Optional[str] = None

   name: Optional[str] = None
   description: Optional[str] = None
   state: str
   replica: list[ReplicationTargetInfo] = []
   memberInfo: list[SourceGroupMemberInfo] = []


class SourceGroupMemberInfo(DynamicData):
   class TargetDeviceId(DynamicData):
      domainId: FaultDomainId
      deviceId: ReplicaId

   deviceId: DeviceId
   targetId: list[TargetDeviceId] = []


class SyncReplicationGroupSuccessResult(GroupOperationResult):
   timeStamp: datetime
   pitId: Optional[PointInTimeReplicaId] = None
   pitName: Optional[str] = None


class TargetGroupInfo(GroupInfo):
   class TargetToSourceInfo(DynamicData):
      sourceGroupId: ReplicationGroupId
      replicationAgreementDescription: Optional[str] = None

   sourceInfo: TargetToSourceInfo
   state: str
   devices: list[TargetGroupMemberInfo] = []
   isPromoteCapable: Optional[bool] = None
   name: Optional[str] = None


class TargetGroupMemberInfo(DynamicData):
   replicaId: ReplicaId
   sourceId: DeviceId
   targetDatastore: Datastore

class TestFailoverParam(FailoverParam):
   pass

class VVolId(DeviceId):
   id: str

class VirtualDiskId(DeviceId):
   diskId: str

class VirtualDiskKey(DeviceId):
   vmInstanceUUID: str
   deviceKey: int


class VirtualDiskMoId(DeviceId):
   vcUuid: Optional[str] = None
   vmMoid: str
   diskKey: str


class VirtualMachineFilePath(VirtualMachineId):
   vcUuid: Optional[str] = None
   dsUrl: str
   vmxPath: str

class VirtualMachineId(DeviceId):
   pass


class VirtualMachineMoId(VirtualMachineId):
   vcUuid: Optional[str] = None
   vmMoid: str

class VirtualMachineUUID(VirtualMachineId):
   vmInstanceUUID: str
