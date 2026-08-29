# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import replication as replication

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.sms import EntityReference

from pyVmomi.vmodl import MethodFault
from pyVmomi.vmodl import RuntimeFault

from pyVmomi.sms.storage import FaultDomainProviderMapping
from pyVmomi.vim.fault import NoPermission
from pyVmomi.vmodl.fault import InvalidArgument

from pyVmomi.sms.storage.replication import DeviceId



class AuthConnectionFailed(NoPermission):
   pass

class CertificateAuthorityFault(ProviderRegistrationFault):
   faultCode: int

class CertificateNotImported(ProviderRegistrationFault):
   pass

class CertificateNotTrusted(ProviderRegistrationFault):
   certificate: str


class CertificateRefreshFailed(MethodFault):
   providerId: list[str] = []


class CertificateRevocationFailed(MethodFault):
   pass


class DuplicateEntry(MethodFault):
   pass


class InactiveProvider(MethodFault):
   mapping: list[FaultDomainProviderMapping] = []

class IncorrectUsernamePassword(ProviderRegistrationFault):
   pass

class InvalidCertificate(ProviderRegistrationFault):
   certificate: str


class InvalidLogin(MethodFault):
   pass


class InvalidProfile(MethodFault):
   pass


class InvalidSession(NoPermission):
   sessionCookie: str

class InvalidUrl(ProviderRegistrationFault):
   url: str


class MultipleSortSpecsNotSupported(InvalidArgument):
   pass

class NoCommonProviderForAllBackings(QueryExecutionFault):
   pass


class NotSupportedByProvider(MethodFault):
   pass


class ProviderBusy(MethodFault):
   pass


class ProviderConnectionFailed(RuntimeFault):
   pass

class ProviderNotFound(QueryExecutionFault):
   pass


class ProviderOutOfProvisioningResource(MethodFault):
   provisioningResourceId: str
   availableBefore: Optional[long] = None
   availableAfter: Optional[long] = None
   total: Optional[long] = None
   isTransient: Optional[bool] = None


class ProviderOutOfResource(MethodFault):
   pass


class ProviderRegistrationFault(MethodFault):
   pass


class ProviderSyncFailed(MethodFault):
   pass


class ProviderUnavailable(MethodFault):
   pass


class ProviderUnregistrationFault(MethodFault):
   pass


class ProxyRegistrationFailed(RuntimeFault):
   pass


class QueryExecutionFault(MethodFault):
   pass


class QueryNotSupported(InvalidArgument):
   entityType: Optional[EntityReference.EntityType] = None
   relatedEntityType: EntityReference.EntityType


class ResourceInUse(ResourceInUse):
   deviceIds: list[DeviceId] = []


class ServiceNotInitialized(RuntimeFault):
   pass


class SmsFault(MethodFault):
   pass

class SyncInProgress(ProviderSyncFailed):
   pass


class TooMany(MethodFault):
   maxBatchSize: Optional[long] = None
