# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vmodl import DynamicData

from pyVmomi.vmodl import MethodFault
from pyVmomi.vmodl import RuntimeFault



class AuthenticationRequired(RuntimeFault):
   class AuthenticationScheme(Enum):
      Basic: ClassVar['AuthenticationScheme'] = 'Basic'
      Bearer: ClassVar['AuthenticationScheme'] = 'Bearer'

   class ErrorType(Enum):
      invalid_request: ClassVar['ErrorType'] = 'invalid_request'
      invalid_token: ClassVar['ErrorType'] = 'invalid_token'
      insufficient_scope: ClassVar['ErrorType'] = 'insufficient_scope'
      registration_required: ClassVar['ErrorType'] = 'registration_required'

   class Challenge(DynamicData):
      scheme: str
      realm: Optional[str] = None
      error: Optional[str] = None
      errorDescription: Optional[str] = None
      ovl: Optional[str] = None
      oidcConfigUrl: Optional[str] = None

   authenticate: list[Challenge] = []


class HostCommunication(RuntimeFault):
   pass

class HostNotConnected(HostCommunication):
   pass

class HostNotReachable(HostCommunication):
   pass


class InvalidArgument(RuntimeFault):
   invalidProperty: Optional[PropertyPath] = None


class InvalidRequest(RuntimeFault):
   pass


class InvalidToken(RuntimeFault):
   pass


class InvalidType(InvalidRequest):
   argument: Optional[PropertyPath] = None


class ManagedObjectNotFound(RuntimeFault):
   obj: ManagedObject


class MethodNotFound(InvalidRequest):
   receiver: ManagedObject
   method: str


class NotEnoughLicenses(RuntimeFault):
   pass


class NotImplemented(RuntimeFault):
   pass


class NotSupported(RuntimeFault):
   pass


class RequestCanceled(RuntimeFault):
   pass


class SecurityError(RuntimeFault):
   pass


class SessionNotFound(RuntimeFault):
   pass


class SystemError(RuntimeFault):
   reason: str


class UnexpectedFault(RuntimeFault):
   faultName: type
   fault: Optional[MethodFault] = None
