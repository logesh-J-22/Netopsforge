# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import DynamicData



class DeviceGroupId(DynamicData):
   id: str


class FaultDomainId(DynamicData):
   id: str


class ReplicationGroupId(DynamicData):
   faultDomainId: FaultDomainId
   deviceGroupId: DeviceGroupId


class ReplicationSpec(DynamicData):
   replicationGroupId: ReplicationGroupId
