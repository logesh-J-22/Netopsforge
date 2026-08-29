# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VsanUpgradeSystem

from pyVmomi.vmodl import KeyAnyValue



class BrokenDiskChainIssue(VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class DisallowDataMovementIssue(VsanUpgradeSystem.PreflightCheckIssue):
   pass


class DisallowEvacuateDataIssue(VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[HostSystem] = []


class DiskUnhealthIssue(VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class HigherObjectsPresentDuringDowngradeIssue(VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class HostPropertyRetrieveIssue(VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[HostSystem] = []


class HostWithHybridDiskgroupIssue(VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[HostSystem] = []


class HostsCompressionOnlyNotSupported(VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[HostSystem] = []


class MixedEsxVersionInClientIssue(VsanUpgradeSystem.PreflightCheckIssue):
   clusterName: str


class MixedEsxVersionIssue(VsanUpgradeSystem.PreflightCheckIssue):
   pass


class ObjectInaccessibleIssue(VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class ObjectPolicyIssue(VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class RemoteClusterNotCompatible(VsanUpgradeSystem.PreflightCheckIssue):
   compatibilityInfo: list[KeyAnyValue] = []


class UnknownScanIssue(VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class UnsupportedHighDiskVersionIssue(VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[HostSystem] = []
