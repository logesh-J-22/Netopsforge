# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vim.vsan import VbossConfig


class ComplianceResourceCheckStatusType:
   pass


class ConfigInfo(DynamicData):
   class HostDefaultInfo(DynamicData):
      uuid: Optional[str] = None
      autoClaimStorage: Optional[bool] = None
      checksumEnabled: Optional[bool] = None

   enabled: Optional[bool] = None
   defaultConfig: Optional[HostDefaultInfo] = None
   vsanEsaEnabled: Optional[bool] = None
   vsanCyberRecoveryEnabled: Optional[bool] = None


class CoreConfigInfo(DynamicData):
   vsanMaxEnabled: Optional[bool] = None


class CoreConfigSpec(DynamicData):
   vsanMaxEnabled: Optional[bool] = None


class VbossClusterConfig(VbossConfig):
   pass

class VsanManagedStorageType:
   pass
