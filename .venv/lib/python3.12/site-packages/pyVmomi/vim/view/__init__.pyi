# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity



class ContainerView(ManagedObjectView):
   @property
   def container(self) -> ManagedEntity: ...
   @property
   def type(self) -> list[type]: ...
   @property
   def recursive(self) -> bool: ...


class InventoryView(ManagedObjectView):
   def OpenFolder(self, entity: list[ManagedEntity]) -> list[ManagedEntity]: ...
   def CloseFolder(self, entity: list[ManagedEntity]) -> list[ManagedEntity]: ...


class ListView(ManagedObjectView):
   def Modify(self, add: list[ManagedObject], remove: list[ManagedObject]) -> list[ManagedObject]: ...
   def Reset(self, obj: list[ManagedObject]) -> list[ManagedObject]: ...
   def ResetFromView(self, view: View) -> None: ...


class ManagedObjectView(View):
   @property
   def view(self) -> list[ManagedObject]: ...


class View(ManagedObject):
   def Destroy(self) -> None: ...


class ViewManager(ManagedObject):
   @property
   def viewList(self) -> list[View]: ...

   def CreateInventoryView(self) -> InventoryView: ...
   def CreateContainerView(self, container: ManagedEntity, type: list[type], recursive: bool) -> ContainerView: ...
   def CreateListView(self, obj: list[ManagedObject]) -> ListView: ...
   def CreateListViewFromView(self, view: View) -> ListView: ...
