# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vm.replication import ReplicationGroupId



class QueryReplicationGroupResult(DynamicData):
   object: ServerObjectRef
   replicationGroupId: Optional[ReplicationGroupId] = None
   fault: Optional[MethodFault] = None


class ReplicationManager(ManagedObject):
   def QueryReplicationGroups(self, entities: list[ServerObjectRef]) -> list[QueryReplicationGroupResult]: ...
