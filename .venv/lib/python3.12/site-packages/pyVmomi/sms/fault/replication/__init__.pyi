# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional
from pyVmomi.sms import Task
from pyVmomi.vmodl import MethodFault

from pyVmomi.sms.storage.replication import DeviceId


class AlreadyDone(ReplicationFault):
   pass

class InvalidFunctionTarget(ReplicationFault):
   pass


class InvalidReplicationState(ReplicationFault):
   desiredState: list[str] = []
   currentState: str

class NoReplicationTarget(ReplicationFault):
   pass


class NoValidReplica(ReplicationFault):
   deviceId: Optional[DeviceId] = None

class PeerNotReachable(ReplicationFault):
   pass


class ReplicationFault(MethodFault):
   pass


class SyncOngoing(ReplicationFault):
   task: Task
