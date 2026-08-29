# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import double

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vim import Datastore

from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool

from pyVmomi.vim import StoragePod

from pyVmomi.vim import Task

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.cluster import Action

from pyVmomi.vim.cluster import DrsFaults

from pyVmomi.vim.cluster import PlacementSpec
from pyVmomi.vim.cluster import Recommendation

from pyVmomi.vim.cluster import RuleInfo

from pyVmomi.vim.cluster import RuleSpec

from pyVmomi.vim.option import ArrayUpdateSpec
from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vm import CloneSpec
from pyVmomi.vim.vm import ConfigSpec

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vm import RelocateSpec

from pyVmomi.vim.vm.device import VirtualDevice



class ApplyRecommendationResult(DynamicData):
   vm: Optional[VirtualMachine] = None


class AutomationConfig(DynamicData):
   spaceLoadBalanceAutomationMode: Optional[str] = None
   ioLoadBalanceAutomationMode: Optional[str] = None
   ruleEnforcementAutomationMode: Optional[str] = None
   policyEnforcementAutomationMode: Optional[str] = None
   vmEvacuationAutomationMode: Optional[str] = None


class ConfigInfo(DynamicData):
   podConfig: PodConfigInfo
   vmConfig: list[VmConfigInfo] = []


class ConfigSpec(DynamicData):
   podConfigSpec: Optional[PodConfigSpec] = None
   vmConfigSpec: list[VmConfigSpec] = []


class HbrDiskMigrationAction(Action):
   collectionId: str
   collectionName: str
   diskIds: list[str] = []
   source: Datastore
   destination: Datastore
   sizeTransferred: long
   spaceUtilSrcBefore: Optional[float] = None
   spaceUtilDstBefore: Optional[float] = None
   spaceUtilSrcAfter: Optional[float] = None
   spaceUtilDstAfter: Optional[float] = None
   ioLatencySrcBefore: Optional[float] = None
   ioLatencyDstBefore: Optional[float] = None


class IoLoadBalanceConfig(DynamicData):
   reservablePercentThreshold: Optional[int] = None
   reservableIopsThreshold: Optional[int] = None
   reservableThresholdMode: Optional[str] = None
   ioLatencyThreshold: Optional[int] = None
   ioLoadImbalanceThreshold: Optional[int] = None


class OptionSpec(ArrayUpdateSpec):
   option: Optional[OptionValue] = None


class PlacementAffinityRule(DynamicData):
   class RuleType(Enum):
      affinity: ClassVar['RuleType'] = 'affinity'
      antiAffinity: ClassVar['RuleType'] = 'antiAffinity'
      softAffinity: ClassVar['RuleType'] = 'softAffinity'
      softAntiAffinity: ClassVar['RuleType'] = 'softAntiAffinity'

   class RuleScope(Enum):
      cluster: ClassVar['RuleScope'] = 'cluster'
      host: ClassVar['RuleScope'] = 'host'
      storagePod: ClassVar['RuleScope'] = 'storagePod'
      datastore: ClassVar['RuleScope'] = 'datastore'

   ruleType: str
   ruleScope: str
   vms: list[VirtualMachine] = []
   keys: list[str] = []


class PlacementRankResult(DynamicData):
   key: str
   candidate: ClusterComputeResource
   reservedSpaceMB: long
   usedSpaceMB: long
   totalSpaceMB: long
   utilization: double
   faults: list[MethodFault] = []


class PlacementRankSpec(DynamicData):
   specs: list[PlacementSpec] = []
   clusters: list[ClusterComputeResource] = []
   rules: list[PlacementAffinityRule] = []
   placementRankByVm: list[PlacementRankVmSpec] = []


class PlacementRankVmSpec(DynamicData):
   vmPlacementSpec: PlacementSpec
   vmClusters: list[ClusterComputeResource] = []


class PodConfigInfo(DynamicData):
   class Behavior(Enum):
      manual: ClassVar['Behavior'] = 'manual'
      automated: ClassVar['Behavior'] = 'automated'

   enabled: bool
   ioLoadBalanceEnabled: bool
   defaultVmBehavior: str
   loadBalanceInterval: Optional[int] = None
   defaultIntraVmAffinity: Optional[bool] = None
   spaceLoadBalanceConfig: Optional[SpaceLoadBalanceConfig] = None
   ioLoadBalanceConfig: Optional[IoLoadBalanceConfig] = None
   automationOverrides: Optional[AutomationConfig] = None
   rule: list[RuleInfo] = []
   option: list[OptionValue] = []


class PodConfigSpec(DynamicData):
   enabled: Optional[bool] = None
   ioLoadBalanceEnabled: Optional[bool] = None
   defaultVmBehavior: Optional[str] = None
   loadBalanceInterval: Optional[int] = None
   defaultIntraVmAffinity: Optional[bool] = None
   spaceLoadBalanceConfig: Optional[SpaceLoadBalanceConfig] = None
   ioLoadBalanceConfig: Optional[IoLoadBalanceConfig] = None
   automationOverrides: Optional[AutomationConfig] = None
   rule: list[RuleSpec] = []
   option: list[OptionSpec] = []


class PodSelectionSpec(DynamicData):
   class VmPodConfig(DynamicData):
      storagePod: StoragePod
      disk: list[DiskLocator] = []
      vmConfig: Optional[VmConfigInfo] = None
      interVmRule: list[RuleInfo] = []

   class DiskLocator(DynamicData):
      diskId: int
      diskMoveType: Optional[str] = None
      diskBackingInfo: Optional[VirtualDevice.BackingInfo] = None
      profile: list[ProfileSpec] = []

   initialVmConfig: list[VmPodConfig] = []
   storagePod: Optional[StoragePod] = None


class SpaceLoadBalanceConfig(DynamicData):
   class SpaceThresholdMode(Enum):
      utilization: ClassVar['SpaceThresholdMode'] = 'utilization'
      freeSpace: ClassVar['SpaceThresholdMode'] = 'freeSpace'

   spaceThresholdMode: Optional[str] = None
   spaceUtilizationThreshold: Optional[int] = None
   freeSpaceThresholdGB: Optional[int] = None
   minSpaceUtilizationDifference: Optional[int] = None


class StorageMigrationAction(Action):
   vm: VirtualMachine
   relocateSpec: RelocateSpec
   source: Datastore
   destination: Datastore
   sizeTransferred: long
   spaceUtilSrcBefore: Optional[float] = None
   spaceUtilDstBefore: Optional[float] = None
   spaceUtilSrcAfter: Optional[float] = None
   spaceUtilDstAfter: Optional[float] = None
   ioLatencySrcBefore: Optional[float] = None
   ioLatencyDstBefore: Optional[float] = None


class StoragePlacementAction(Action):
   vm: Optional[VirtualMachine] = None
   relocateSpec: RelocateSpec
   destination: Datastore
   spaceUtilBefore: Optional[float] = None
   spaceDemandBefore: Optional[float] = None
   spaceUtilAfter: Optional[float] = None
   spaceDemandAfter: Optional[float] = None
   ioLatencyBefore: Optional[float] = None


class StoragePlacementResult(DynamicData):
   recommendations: list[Recommendation] = []
   drsFault: Optional[DrsFaults] = None
   task: Optional[Task] = None


class StoragePlacementSpec(DynamicData):
   class PlacementType(Enum):
      create: ClassVar['PlacementType'] = 'create'
      reconfigure: ClassVar['PlacementType'] = 'reconfigure'
      relocate: ClassVar['PlacementType'] = 'relocate'
      clone: ClassVar['PlacementType'] = 'clone'

   type: str
   priority: Optional[VirtualMachine.MovePriority] = None
   vm: Optional[VirtualMachine] = None
   podSelectionSpec: PodSelectionSpec
   cloneSpec: Optional[CloneSpec] = None
   cloneName: Optional[str] = None
   configSpec: Optional[ConfigSpec] = None
   relocateSpec: Optional[RelocateSpec] = None
   resourcePool: Optional[ResourcePool] = None
   host: Optional[HostSystem] = None
   folder: Optional[Folder] = None
   disallowPrerequisiteMoves: Optional[bool] = None
   resourceLeaseDurationSec: Optional[int] = None


class VirtualDiskAntiAffinityRuleSpec(RuleInfo):
   diskId: list[int] = []


class VirtualDiskRuleSpec(RuleInfo):
   class RuleType(Enum):
      affinity: ClassVar['RuleType'] = 'affinity'
      antiAffinity: ClassVar['RuleType'] = 'antiAffinity'
      disabled: ClassVar['RuleType'] = 'disabled'

   diskRuleType: str
   diskId: list[int] = []


class VmConfigInfo(DynamicData):
   vm: Optional[VirtualMachine] = None
   enabled: Optional[bool] = None
   behavior: Optional[str] = None
   intraVmAffinity: Optional[bool] = None
   intraVmAntiAffinity: Optional[VirtualDiskAntiAffinityRuleSpec] = None
   virtualDiskRules: list[VirtualDiskRuleSpec] = []


class VmConfigSpec(ArrayUpdateSpec):
   info: Optional[VmConfigInfo] = None
