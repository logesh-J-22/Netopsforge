# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import binary
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault



class AliasManager(ManagedObject):
   class GuestAuthSubject(DynamicData):
      pass

   class GuestAuthAnySubject(GuestAuthSubject):
      pass

   class GuestAuthNamedSubject(GuestAuthSubject):
      name: str

   class GuestAuthAliasInfo(DynamicData):
      subject: GuestAuthSubject
      comment: str

   class GuestAliases(DynamicData):
      base64Cert: str
      aliases: list[GuestAuthAliasInfo] = []

   class GuestMappedAliases(DynamicData):
      base64Cert: str
      username: str
      subjects: list[GuestAuthSubject] = []

   def AddAlias(self, vm: VirtualMachine, auth: GuestAuthentication, username: str, mapCert: bool, base64Cert: str, aliasInfo: GuestAuthAliasInfo) -> None: ...
   def RemoveAlias(self, vm: VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str, subject: GuestAuthSubject) -> None: ...
   def RemoveAliasByCert(self, vm: VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str) -> None: ...
   def ListAliases(self, vm: VirtualMachine, auth: GuestAuthentication, username: str) -> list[GuestAliases]: ...
   def ListMappedAliases(self, vm: VirtualMachine, auth: GuestAuthentication) -> list[GuestMappedAliases]: ...


class AuthManager(ManagedObject):
   def ValidateCredentials(self, vm: VirtualMachine, auth: GuestAuthentication) -> None: ...
   def AcquireCredentials(self, vm: VirtualMachine, requestedAuth: GuestAuthentication, sessionID: Optional[long]) -> GuestAuthentication: ...
   def ReleaseCredentials(self, vm: VirtualMachine, auth: GuestAuthentication) -> None: ...


class FileManager(ManagedObject):
   class FileAttributes(DynamicData):
      modificationTime: Optional[datetime] = None
      accessTime: Optional[datetime] = None
      symlinkTarget: Optional[str] = None

   class PosixFileAttributes(FileAttributes):
      ownerId: Optional[int] = None
      groupId: Optional[int] = None
      permissions: Optional[long] = None

   class WindowsFileAttributes(FileAttributes):
      hidden: Optional[bool] = None
      readOnly: Optional[bool] = None
      createTime: Optional[datetime] = None

   class FileInfo(DynamicData):
      class FileType(Enum):
         file: ClassVar['FileType'] = 'file'
         directory: ClassVar['FileType'] = 'directory'
         symlink: ClassVar['FileType'] = 'symlink'

      path: str
      type: str
      size: long
      attributes: FileAttributes

   class ListFileInfo(DynamicData):
      files: list[FileInfo] = []
      remaining: int

   class FileTransferInformation(DynamicData):
      attributes: FileAttributes
      size: long
      url: str

   def MakeDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, directoryPath: str, createParentDirectories: bool) -> None: ...
   def DeleteFile(self, vm: VirtualMachine, auth: GuestAuthentication, filePath: str) -> None: ...
   def DeleteDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, directoryPath: str, recursive: bool) -> None: ...
   def MoveDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, srcDirectoryPath: str, dstDirectoryPath: str) -> None: ...
   def MoveFile(self, vm: VirtualMachine, auth: GuestAuthentication, srcFilePath: str, dstFilePath: str, overwrite: bool) -> None: ...
   def CreateTemporaryFile(self, vm: VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: Optional[str]) -> str: ...
   def CreateTemporaryDirectory(self, vm: VirtualMachine, auth: GuestAuthentication, prefix: str, suffix: str, directoryPath: Optional[str]) -> str: ...
   def ListFiles(self, vm: VirtualMachine, auth: GuestAuthentication, filePath: str, index: Optional[int], maxResults: Optional[int], matchPattern: Optional[str]) -> ListFileInfo: ...
   def ChangeFileAttributes(self, vm: VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileAttributes) -> None: ...
   def InitiateFileTransferFromGuest(self, vm: VirtualMachine, auth: GuestAuthentication, guestFilePath: str) -> FileTransferInformation: ...
   def InitiateFileTransferToGuest(self, vm: VirtualMachine, auth: GuestAuthentication, guestFilePath: str, fileAttributes: FileAttributes, fileSize: long, overwrite: bool) -> str: ...


class GuestAuthentication(DynamicData):
   interactiveSession: bool


class GuestOperationsManager(ManagedObject):
   @property
   def authManager(self) -> Optional[AuthManager]: ...
   @property
   def fileManager(self) -> Optional[FileManager]: ...
   @property
   def processManager(self) -> Optional[ProcessManager]: ...
   @property
   def guestWindowsRegistryManager(self) -> Optional[WindowsRegistryManager]: ...
   @property
   def aliasManager(self) -> Optional[AliasManager]: ...

class NamePasswordAuthentication(GuestAuthentication):
   username: str
   password: str


class ProcessManager(ManagedObject):
   class ProgramSpec(DynamicData):
      programPath: str
      arguments: str
      workingDirectory: Optional[str] = None
      envVariables: list[str] = []

   class WindowsProgramSpec(ProgramSpec):
      startMinimized: bool

   class ProcessInfo(DynamicData):
      name: str
      pid: long
      owner: str
      cmdLine: str
      startTime: datetime
      endTime: Optional[datetime] = None
      exitCode: Optional[int] = None

   def StartProgram(self, vm: VirtualMachine, auth: GuestAuthentication, spec: ProgramSpec) -> long: ...
   def ListProcesses(self, vm: VirtualMachine, auth: GuestAuthentication, pids: list[long]) -> list[ProcessInfo]: ...
   def TerminateProcess(self, vm: VirtualMachine, auth: GuestAuthentication, pid: long) -> None: ...
   def ReadEnvironmentVariable(self, vm: VirtualMachine, auth: GuestAuthentication, names: list[str]) -> list[str]: ...


class SAMLTokenAuthentication(GuestAuthentication):
   token: str
   username: Optional[str] = None

class SSPIAuthentication(GuestAuthentication):
   sspiToken: str

class TicketedSessionAuthentication(GuestAuthentication):
   ticket: str


class WindowsRegistryManager(ManagedObject):
   class RegistryKeyName(DynamicData):
      class RegistryKeyWowBitness(Enum):
         WOWNative: ClassVar['RegistryKeyWowBitness'] = 'WOWNative'
         WOW32: ClassVar['RegistryKeyWowBitness'] = 'WOW32'
         WOW64: ClassVar['RegistryKeyWowBitness'] = 'WOW64'

      registryPath: str
      wowBitness: str

   class RegistryKey(DynamicData):
      keyName: RegistryKeyName
      classType: str
      lastWritten: datetime

   class RegistryKeyRecord(DynamicData):
      key: RegistryKey
      fault: Optional[MethodFault] = None

   class RegistryValueName(DynamicData):
      keyName: RegistryKeyName
      name: str

   class RegistryValueData(DynamicData):
      pass

   class RegistryValueDword(RegistryValueData):
      value: int

   class RegistryValueQword(RegistryValueData):
      value: long

   class RegistryValueString(RegistryValueData):
      value: Optional[str] = None

   class RegistryValueExpandString(RegistryValueData):
      value: Optional[str] = None

   class RegistryValueMultiString(RegistryValueData):
      value: list[str] = []

   class RegistryValueBinary(RegistryValueData):
      value: Optional[binary] = None

   class RegistryValue(DynamicData):
      name: RegistryValueName
      data: RegistryValueData

   def CreateRegistryKey(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, isVolatile: bool, classType: Optional[str]) -> None: ...
   def ListRegistryKeys(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, recursive: bool, matchPattern: Optional[str]) -> list[RegistryKeyRecord]: ...
   def DeleteRegistryKey(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, recursive: bool) -> None: ...
   def SetRegistryValue(self, vm: VirtualMachine, auth: GuestAuthentication, value: RegistryValue) -> None: ...
   def ListRegistryValues(self, vm: VirtualMachine, auth: GuestAuthentication, keyName: RegistryKeyName, expandStrings: bool, matchPattern: Optional[str]) -> list[RegistryValue]: ...
   def DeleteRegistryValue(self, vm: VirtualMachine, auth: GuestAuthentication, valueName: RegistryValueName) -> None: ...
