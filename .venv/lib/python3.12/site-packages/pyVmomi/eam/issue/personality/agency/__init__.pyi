# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ComputeResource
from pyVmomi.eam.issue import AgencyIssue



class CannotConfigureSolutions(PMIssue):
   cr: ComputeResource
   solutionsToModify: list[str] = []
   solutionsToRemove: list[str] = []

class CannotUploadDepot(DepotIssue):
   localDepotUrl: str

class DepotIssue(PMIssue):
   remoteDepotUrl: str

class InaccessibleDepot(DepotIssue):
   pass

class InvalidDepot(DepotIssue):
   pass


class PMIssue(AgencyIssue):
   pass

class PMUnavailable(PMIssue):
   pass
