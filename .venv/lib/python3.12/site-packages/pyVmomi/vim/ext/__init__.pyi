# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData



class ExtendedProductInfo(DynamicData):
   companyUrl: Optional[str] = None
   productUrl: Optional[str] = None
   managementUrl: Optional[str] = None
   self: Optional[ManagedEntity] = None


class ManagedByInfo(DynamicData):
   extensionKey: str
   type: str


class ManagedEntityInfo(DynamicData):
   type: str
   smallIconUrl: Optional[str] = None
   iconUrl: Optional[str] = None
   description: Optional[str] = None


class SolutionManagerInfo(DynamicData):
   class TabInfo(DynamicData):
      label: str
      url: str

   tab: list[TabInfo] = []
   smallIconUrl: Optional[str] = None
