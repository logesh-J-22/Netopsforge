# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.pbm import ExtendedElementDescription
from pyVmomi.vmodl import DynamicData

from pyVmomi.pbm.capability import CapabilityMetadata



class CapabilityObjectMetadataPerCategory(DynamicData):
   subCategory: str
   capabilityMetadata: list[CapabilityMetadata] = []


class CapabilityObjectSchema(DynamicData):
   class VendorInfo(DynamicData):
      vendorUuid: str
      info: ExtendedElementDescription

   class NamespaceInfo(DynamicData):
      version: str
      namespace: str
      info: Optional[ExtendedElementDescription] = None

   class VendorResourceTypeInfo(DynamicData):
      resourceType: str
      vendorNamespaceInfo: list[VendorNamespaceInfo] = []

   class VendorNamespaceInfo(DynamicData):
      vendorInfo: VendorInfo
      namespaceInfo: NamespaceInfo

   class CapabilityCategory(Enum):
      common: ClassVar['CapabilityCategory'] = 'common'
      datastoreSpecific: ClassVar['CapabilityCategory'] = 'datastoreSpecific'

   vendorInfo: VendorInfo
   namespaceInfo: NamespaceInfo
   lineOfService: Optional[LineOfServiceInfo] = None
   capabilityMetadataPerCategory: list[CapabilityObjectMetadataPerCategory] = []
   capabilityCategory: Optional[str] = None


class LineOfServiceInfo(DynamicData):
   class LineOfServiceEnum(Enum):
      INSPECTION: ClassVar['LineOfServiceEnum'] = 'INSPECTION'
      COMPRESSION: ClassVar['LineOfServiceEnum'] = 'COMPRESSION'
      ENCRYPTION: ClassVar['LineOfServiceEnum'] = 'ENCRYPTION'
      REPLICATION: ClassVar['LineOfServiceEnum'] = 'REPLICATION'
      CACHING: ClassVar['LineOfServiceEnum'] = 'CACHING'
      PERSISTENCE: ClassVar['LineOfServiceEnum'] = 'PERSISTENCE'
      DATA_PROVIDER: ClassVar['LineOfServiceEnum'] = 'DATA_PROVIDER'
      DATASTORE_IO_CONTROL: ClassVar['LineOfServiceEnum'] = 'DATASTORE_IO_CONTROL'
      DATA_PROTECTION: ClassVar['LineOfServiceEnum'] = 'DATA_PROTECTION'
      STRETCHED_CLUSTER: ClassVar['LineOfServiceEnum'] = 'STRETCHED_CLUSTER'

   lineOfService: str
   name: ExtendedElementDescription
   description: Optional[ExtendedElementDescription] = None


class PersistenceBasedDataServiceInfo(LineOfServiceInfo):
   compatiblePersistenceSchemaNamespace: list[str] = []

class VaioDataServiceInfo(LineOfServiceInfo):
   pass
