# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vslm import ID



class SyncFault(VslmFault):
   id: Optional[ID] = None


class VslmFault(MethodFault):
   msg: Optional[str] = None
