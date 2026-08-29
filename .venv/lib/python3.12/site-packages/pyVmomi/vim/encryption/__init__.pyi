# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime
from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import HostSystem
from pyVmomi.vim import KeyValue
from pyVmomi.vim import ManagedEntity

from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault



class CryptoKeyId(DynamicData):
   keyId: str
   providerId: Optional[KeyProviderId] = None


class CryptoKeyPlain(DynamicData):
   keyId: CryptoKeyId
   algorithm: str
   keyData: str


class CryptoKeyResult(DynamicData):
   keyId: CryptoKeyId
   success: bool
   reason: Optional[str] = None
   fault: Optional[MethodFault] = None


class CryptoManager(ManagedObject):
   @property
   def enabled(self) -> bool: ...

   def AddKey(self, key: CryptoKeyPlain) -> None: ...
   def AddKeys(self, keys: list[CryptoKeyPlain]) -> list[CryptoKeyResult]: ...
   def RemoveKey(self, key: CryptoKeyId, force: bool) -> None: ...
   def RemoveKeys(self, keys: list[CryptoKeyId], force: bool) -> list[CryptoKeyResult]: ...
   def ListKeys(self, limit: Optional[int]) -> list[CryptoKeyId]: ...


class CryptoManagerHost(CryptoManager):
   class KeyManagementType(Enum):
      unknown: ClassVar['KeyManagementType'] = 'unknown'
      internal: ClassVar['KeyManagementType'] = 'internal'
      external: ClassVar['KeyManagementType'] = 'external'

   class KeyStatus(DynamicData):
      keyId: CryptoKeyId
      present: bool
      managementType: Optional[str] = None
      accessGranted: Optional[bool] = None

   def Prepare(self) -> None: ...
   def Enable(self, initialKey: CryptoKeyPlain) -> None: ...
   def ChangeKey(self, newKey: CryptoKeyPlain) -> Task: ...
   def Disable(self) -> None: ...
   def GetCryptoKeyStatus(self, keys: list[CryptoKeyId]) -> list[KeyStatus]: ...

class CryptoManagerHostKMS(CryptoManagerHost):
   pass


class CryptoManagerKmip(CryptoManager):
   class CertificateInfo(DynamicData):
      subject: str
      issuer: str
      serialNumber: str
      notBefore: datetime
      notAfter: datetime
      fingerprint: str
      checkTime: datetime
      secondsSinceValid: Optional[int] = None
      secondsBeforeExpire: Optional[int] = None

   class ServerStatus(DynamicData):
      name: str
      status: ManagedEntity.Status
      connectionStatus: str
      certInfo: Optional[CertificateInfo] = None
      clientTrustServer: Optional[bool] = None
      serverTrustClient: Optional[bool] = None

   class ClusterStatus(DynamicData):
      clusterId: KeyProviderId
      overallStatus: Optional[ManagedEntity.Status] = None
      managementType: Optional[str] = None
      servers: list[ServerStatus] = []
      clientCertInfo: Optional[CertificateInfo] = None

   class GenerateKeySpec(DynamicData):
      keyType: Optional[str] = None

   class ServerCertInfo(DynamicData):
      certificate: str
      certInfo: Optional[CertificateInfo] = None
      clientTrustServer: Optional[bool] = None

   class CertSignRequest(DynamicData):
      commonName: Optional[str] = None
      organization: Optional[str] = None
      organizationUnit: Optional[str] = None
      locality: Optional[str] = None
      state: Optional[str] = None
      country: Optional[str] = None
      email: Optional[str] = None

   class CryptoKeyStatus(DynamicData):
      class KeyUnavailableReason(Enum):
         KeyStateMissingInCache: ClassVar['KeyUnavailableReason'] = 'KeyStateMissingInCache'
         KeyStateClusterInvalid: ClassVar['KeyUnavailableReason'] = 'KeyStateClusterInvalid'
         KeyStateClusterUnreachable: ClassVar['KeyUnavailableReason'] = 'KeyStateClusterUnreachable'
         KeyStateMissingInKMS: ClassVar['KeyUnavailableReason'] = 'KeyStateMissingInKMS'
         KeyStateNotActiveOrEnabled: ClassVar['KeyUnavailableReason'] = 'KeyStateNotActiveOrEnabled'
         KeyStateManagedByTrustAuthority: ClassVar['KeyUnavailableReason'] = 'KeyStateManagedByTrustAuthority'
         KeyStateManagedByNKP: ClassVar['KeyUnavailableReason'] = 'KeyStateManagedByNKP'
         NoPermissionToAccessKeyProvider: ClassVar['KeyUnavailableReason'] = 'NoPermissionToAccessKeyProvider'
         WrappingKeyMissingInKMS: ClassVar['KeyUnavailableReason'] = 'WrappingKeyMissingInKMS'
         WrappingKeyNotActiveOrEnabled: ClassVar['KeyUnavailableReason'] = 'WrappingKeyNotActiveOrEnabled'

      class KeyInfo(DynamicData):
         keyId: str

      class WrappingKeyIdKeyInfo(CryptoKeyStatus.KeyInfo):
         configuredTime: Optional[datetime] = None

      class WrappingRotationIntervalKeyInfo(CryptoKeyStatus.KeyInfo):
         createTime: Optional[datetime] = None
         rotateTime: Optional[datetime] = None

      keyId: CryptoKeyId
      keyAvailable: Optional[bool] = None
      reason: Optional[str] = None
      keyInfo: Optional[KeyInfo] = None
      encryptedVMs: list[VirtualMachine] = []
      affectedHosts: list[HostSystem] = []
      referencedByTags: list[str] = []

   class CustomAttributeSpec(DynamicData):
      attributes: list[KeyValue] = []

   @property
   def kmipServers(self) -> list[KmipClusterInfo]: ...

   def RegisterKmipServer(self, server: KmipServerSpec) -> None: ...
   def MarkDefault(self, clusterId: KeyProviderId) -> None: ...
   def UpdateKmipServer(self, server: KmipServerSpec) -> None: ...
   def RemoveKmipServer(self, clusterId: KeyProviderId, serverName: str) -> None: ...
   def ListKmipServers(self, limit: Optional[int]) -> list[KmipClusterInfo]: ...
   def RetrieveKmipServersStatus(self, clusters: list[KmipClusterInfo]) -> Task: ...
   def GenerateKey(self, keyProvider: Optional[KeyProviderId], spec: Optional[CustomAttributeSpec], keySpec: Optional[GenerateKeySpec]) -> CryptoKeyResult: ...
   def RetrieveKmipServerCert(self, keyProvider: KeyProviderId, server: KmipServerInfo) -> ServerCertInfo: ...
   def UploadKmipServerCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def GenerateSelfSignedClientCert(self, cluster: KeyProviderId, request: Optional[CertSignRequest]) -> str: ...
   def GenerateClientCsr(self, cluster: KeyProviderId, request: Optional[CertSignRequest]) -> str: ...
   def RetrieveSelfSignedClientCert(self, cluster: KeyProviderId) -> str: ...
   def RetrieveClientCsr(self, cluster: KeyProviderId) -> str: ...
   def RetrieveClientCert(self, cluster: KeyProviderId) -> str: ...
   def UpdateSelfSignedClientCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def UpdateKmsSignedCsrClientCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def UploadClientCert(self, cluster: KeyProviderId, certificate: str, privateKey: str) -> None: ...
   def IsKmsClusterActive(self, cluster: Optional[KeyProviderId]) -> bool: ...
   def SetDefaultKmsCluster(self, entity: Optional[ManagedEntity], clusterId: Optional[KeyProviderId]) -> None: ...
   def GetDefaultKmsCluster(self, entity: Optional[ManagedEntity], defaultsToParent: Optional[bool]) -> Optional[KeyProviderId]: ...
   def QueryCryptoKeyStatus(self, keyIds: list[CryptoKeyId], checkKeyBitMap: int) -> list[CryptoKeyStatus]: ...
   def RegisterKmsCluster(self, clusterId: KeyProviderId, managementType: Optional[str]) -> None: ...
   def UnregisterKmsCluster(self, clusterId: KeyProviderId) -> None: ...
   def ListKmsClusters(self, includeKmsServers: Optional[bool], managementTypeFilter: Optional[int], statusFilter: Optional[int]) -> list[KmipClusterInfo]: ...
   def SetKeyCustomAttributes(self, keyId: CryptoKeyId, spec: CustomAttributeSpec) -> CryptoKeyResult: ...


class CryptoSpec(DynamicData):
   pass

class CryptoSpecDecrypt(CryptoSpec):
   pass

class CryptoSpecDeepRecrypt(CryptoSpec):
   newKeyId: CryptoKeyId

class CryptoSpecEncrypt(CryptoSpec):
   cryptoKeyId: CryptoKeyId

class CryptoSpecNoOp(CryptoSpec):
   pass

class CryptoSpecRegister(CryptoSpecNoOp):
   cryptoKeyId: CryptoKeyId

class CryptoSpecShallowRecrypt(CryptoSpec):
   newKeyId: CryptoKeyId


class KeyProviderId(DynamicData):
   id: str


class KmipClusterInfo(DynamicData):
   class KmsManagementType(Enum):
      unknown: ClassVar['KmsManagementType'] = 'unknown'
      vCenter: ClassVar['KmsManagementType'] = 'vCenter'
      trustAuthority: ClassVar['KmsManagementType'] = 'trustAuthority'
      nativeProvider: ClassVar['KmsManagementType'] = 'nativeProvider'

   class KeyType(Enum):
      rawKey: ClassVar['KeyType'] = 'rawKey'
      wrappedKey: ClassVar['KeyType'] = 'wrappedKey'

   class KeyInfo(DynamicData):
      pass

   class WrappingKeyIdKeyInfo(KeyInfo):
      keyId: str
      configuredTime: datetime

   class WrappingRotationIntervalKeyInfo(KeyInfo):
      keyId: Optional[str] = None
      rotationInterval: Optional[int] = None
      lastRotation: Optional[datetime] = None

   clusterId: KeyProviderId
   servers: list[KmipServerInfo] = []
   useAsDefault: bool
   managementType: Optional[str] = None
   useAsEntityDefault: list[ManagedEntity] = []
   hasBackup: Optional[bool] = None
   tpmRequired: Optional[bool] = None
   keyId: Optional[str] = None
   defaultKeyType: Optional[str] = None
   keyInfo: Optional[KeyInfo] = None


class KmipServerInfo(DynamicData):
   name: str
   address: str
   port: int
   proxyAddress: Optional[str] = None
   proxyPort: Optional[int] = None
   reconnect: Optional[int] = None
   protocol: Optional[str] = None
   nbio: Optional[int] = None
   timeout: Optional[int] = None
   userName: Optional[str] = None


class KmipServerSpec(DynamicData):
   class KeySpec(DynamicData):
      pass

   class WrappingKeyIdKeySpec(KeySpec):
      keyId: str

   class WrappingRotationIntervalKeySpec(KeySpec):
      rotationInterval: Optional[int] = None

   clusterId: KeyProviderId
   info: KmipServerInfo
   password: Optional[str] = None
   defaultKeyType: Optional[str] = None
   keySpec: Optional[KeySpec] = None


class KmipServerStatus(DynamicData):
   clusterId: KeyProviderId
   name: str
   status: ManagedEntity.Status
   description: str
