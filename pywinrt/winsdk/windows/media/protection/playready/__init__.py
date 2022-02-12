# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Media.Protection.PlayReady")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.media.core
except Exception:
    pass

try:
    import winsdk.windows.media.protection
except Exception:
    pass

try:
    import winsdk.windows.storage
except Exception:
    pass

class NDCertificateFeature(enum.IntEnum):
    TRANSMITTER = 1
    RECEIVER = 2
    SHARED_CERTIFICATE = 3
    SECURE_CLOCK = 4
    ANTI_ROLL_BACK_CLOCK = 5
    C_R_L_S = 9
    PLAY_READY3_FEATURES = 13

class NDCertificatePlatformID(enum.IntEnum):
    WINDOWS = 0
    O_S_X = 1
    WINDOWS_ON_A_R_M = 2
    WINDOWS_MOBILE7 = 5
    I_O_S_ON_A_R_M = 6
    X_BOX_ON_P_P_C = 7
    WINDOWS_PHONE8_ON_A_R_M = 8
    WINDOWS_PHONE8_ON_X86 = 9
    XBOX_ONE = 10
    ANDROID_ON_A_R_M = 11
    WINDOWS_PHONE81_ON_A_R_M = 12
    WINDOWS_PHONE81_ON_X86 = 13

class NDCertificateType(enum.IntEnum):
    UNKNOWN = 0
    P_C = 1
    DEVICE = 2
    DOMAIN = 3
    ISSUER = 4
    CRL_SIGNER = 5
    SERVICE = 6
    SILVERLIGHT = 7
    APPLICATION = 8
    METERING = 9
    KEY_FILE_SIGNER = 10
    SERVER = 11
    LICENSE_SIGNER = 12

class NDClosedCaptionFormat(enum.IntEnum):
    A_T_S_C = 0
    S_C_T_E20 = 1
    UNKNOWN = 2

class NDContentIDType(enum.IntEnum):
    KEY_I_D = 1
    PLAY_READY_OBJECT = 2
    CUSTOM = 3

class NDMediaStreamType(enum.IntEnum):
    AUDIO = 1
    VIDEO = 2

class NDProximityDetectionType(enum.IntEnum):
    U_D_P = 1
    T_C_P = 2
    TRANSPORT_AGNOSTIC = 4

class NDStartAsyncOptions(enum.IntEnum):
    MUTUAL_AUTHENTICATION = 1
    WAIT_FOR_LICENSE_DESCRIPTOR = 2

class PlayReadyDecryptorSetup(enum.IntEnum):
    UNINITIALIZED = 0
    ON_DEMAND = 1

class PlayReadyEncryptionAlgorithm(enum.IntEnum):
    UNPROTECTED = 0
    AES128_CTR = 1
    COCKTAIL = 4
    AES128_CBC = 5
    UNSPECIFIED = 65535
    UNINITIALIZED = 2147483647

class PlayReadyHardwareDRMFeatures(enum.IntEnum):
    HARDWARE_D_R_M = 1
    H_E_V_C = 2
    AES128_CBC = 3

class PlayReadyITADataFormat(enum.IntEnum):
    SERIALIZED_PROPERTIES = 0
    SERIALIZED_PROPERTIES_WITH_CONTENT_PROTECTION_WRAPPER = 1

NDClient = _ns_module.NDClient
NDCustomData = _ns_module.NDCustomData
NDDownloadEngineNotifier = _ns_module.NDDownloadEngineNotifier
NDLicenseFetchDescriptor = _ns_module.NDLicenseFetchDescriptor
NDStorageFileHelper = _ns_module.NDStorageFileHelper
NDStreamParserNotifier = _ns_module.NDStreamParserNotifier
NDTCPMessenger = _ns_module.NDTCPMessenger
PlayReadyContentHeader = _ns_module.PlayReadyContentHeader
PlayReadyContentResolver = _ns_module.PlayReadyContentResolver
PlayReadyDomain = _ns_module.PlayReadyDomain
PlayReadyDomainIterable = _ns_module.PlayReadyDomainIterable
PlayReadyDomainIterator = _ns_module.PlayReadyDomainIterator
PlayReadyDomainJoinServiceRequest = _ns_module.PlayReadyDomainJoinServiceRequest
PlayReadyDomainLeaveServiceRequest = _ns_module.PlayReadyDomainLeaveServiceRequest
PlayReadyITADataGenerator = _ns_module.PlayReadyITADataGenerator
PlayReadyIndividualizationServiceRequest = _ns_module.PlayReadyIndividualizationServiceRequest
PlayReadyLicense = _ns_module.PlayReadyLicense
PlayReadyLicenseAcquisitionServiceRequest = _ns_module.PlayReadyLicenseAcquisitionServiceRequest
PlayReadyLicenseIterable = _ns_module.PlayReadyLicenseIterable
PlayReadyLicenseIterator = _ns_module.PlayReadyLicenseIterator
PlayReadyLicenseManagement = _ns_module.PlayReadyLicenseManagement
PlayReadyLicenseSession = _ns_module.PlayReadyLicenseSession
PlayReadyMeteringReportServiceRequest = _ns_module.PlayReadyMeteringReportServiceRequest
PlayReadyRevocationServiceRequest = _ns_module.PlayReadyRevocationServiceRequest
PlayReadySecureStopIterable = _ns_module.PlayReadySecureStopIterable
PlayReadySecureStopIterator = _ns_module.PlayReadySecureStopIterator
PlayReadySecureStopServiceRequest = _ns_module.PlayReadySecureStopServiceRequest
PlayReadySoapMessage = _ns_module.PlayReadySoapMessage
PlayReadyStatics = _ns_module.PlayReadyStatics
INDClosedCaptionDataReceivedEventArgs = _ns_module.INDClosedCaptionDataReceivedEventArgs
INDCustomData = _ns_module.INDCustomData
INDDownloadEngine = _ns_module.INDDownloadEngine
INDDownloadEngineNotifier = _ns_module.INDDownloadEngineNotifier
INDLicenseFetchCompletedEventArgs = _ns_module.INDLicenseFetchCompletedEventArgs
INDLicenseFetchDescriptor = _ns_module.INDLicenseFetchDescriptor
INDLicenseFetchResult = _ns_module.INDLicenseFetchResult
INDMessenger = _ns_module.INDMessenger
INDProximityDetectionCompletedEventArgs = _ns_module.INDProximityDetectionCompletedEventArgs
INDRegistrationCompletedEventArgs = _ns_module.INDRegistrationCompletedEventArgs
INDSendResult = _ns_module.INDSendResult
INDStartResult = _ns_module.INDStartResult
INDStorageFileHelper = _ns_module.INDStorageFileHelper
INDStreamParser = _ns_module.INDStreamParser
INDStreamParserNotifier = _ns_module.INDStreamParserNotifier
INDTransmitterProperties = _ns_module.INDTransmitterProperties
IPlayReadyDomain = _ns_module.IPlayReadyDomain
IPlayReadyLicense = _ns_module.IPlayReadyLicense
IPlayReadyLicenseAcquisitionServiceRequest = _ns_module.IPlayReadyLicenseAcquisitionServiceRequest
IPlayReadyLicenseSession = _ns_module.IPlayReadyLicenseSession
IPlayReadyLicenseSession2 = _ns_module.IPlayReadyLicenseSession2
IPlayReadySecureStopServiceRequest = _ns_module.IPlayReadySecureStopServiceRequest
IPlayReadyServiceRequest = _ns_module.IPlayReadyServiceRequest
