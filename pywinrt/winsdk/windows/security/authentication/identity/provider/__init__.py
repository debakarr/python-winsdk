# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Security.Authentication.Identity.Provider")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class SecondaryAuthenticationFactorAuthenticationMessage(enum.IntEnum):
    INVALID = 0
    SWIPE_UP_WELCOME = 1
    TAP_WELCOME = 2
    DEVICE_NEEDS_ATTENTION = 3
    LOOKING_FOR_DEVICE = 4
    LOOKING_FOR_DEVICE_PLUGGEDIN = 5
    BLUETOOTH_IS_DISABLED = 6
    NFC_IS_DISABLED = 7
    WI_FI_IS_DISABLED = 8
    EXTRA_TAP_IS_REQUIRED = 9
    DISABLED_BY_POLICY = 10
    TAP_ON_DEVICE_REQUIRED = 11
    HOLD_FINGER = 12
    SCAN_FINGER = 13
    UNAUTHORIZED_USER = 14
    REREGISTER_REQUIRED = 15
    TRY_AGAIN = 16
    SAY_PASSPHRASE = 17
    READY_TO_SIGN_IN = 18
    USE_ANOTHER_SIGN_IN_OPTION = 19
    CONNECTION_REQUIRED = 20
    TIME_LIMIT_EXCEEDED = 21
    CANCELED_BY_USER = 22
    CENTER_HAND = 23
    MOVE_HAND_CLOSER = 24
    MOVE_HAND_FARTHER = 25
    PLACE_HAND_ABOVE = 26
    RECOGNITION_FAILED = 27
    DEVICE_UNAVAILABLE = 28

class SecondaryAuthenticationFactorAuthenticationScenario(enum.IntEnum):
    SIGN_IN = 0
    CREDENTIAL_PROMPT = 1

class SecondaryAuthenticationFactorAuthenticationStage(enum.IntEnum):
    NOT_STARTED = 0
    WAITING_FOR_USER_CONFIRMATION = 1
    COLLECTING_CREDENTIAL = 2
    SUSPENDING_AUTHENTICATION = 3
    CREDENTIAL_COLLECTED = 4
    CREDENTIAL_AUTHENTICATED = 5
    STOPPING_AUTHENTICATION = 6
    READY_FOR_LOCK = 7
    CHECKING_DEVICE_PRESENCE = 8

class SecondaryAuthenticationFactorAuthenticationStatus(enum.IntEnum):
    FAILED = 0
    STARTED = 1
    UNKNOWN_DEVICE = 2
    DISABLED_BY_POLICY = 3
    INVALID_AUTHENTICATION_STAGE = 4

class SecondaryAuthenticationFactorDeviceCapabilities(enum.IntFlag):
    NONE = 0
    SECURE_STORAGE = 0x1
    STORE_KEYS = 0x2
    CONFIRM_USER_INTENT_TO_AUTHENTICATE = 0x4
    SUPPORT_SECURE_USER_PRESENCE_CHECK = 0x8
    TRANSMITTED_DATA_IS_ENCRYPTED = 0x10
    H_MAC_SHA256 = 0x20
    CLOSE_RANGE_DATA_TRANSMISSION = 0x40

class SecondaryAuthenticationFactorDeviceFindScope(enum.IntEnum):
    USER = 0
    ALL_USERS = 1

class SecondaryAuthenticationFactorDevicePresence(enum.IntEnum):
    ABSENT = 0
    PRESENT = 1

class SecondaryAuthenticationFactorDevicePresenceMonitoringMode(enum.IntEnum):
    UNSUPPORTED = 0
    APP_MANAGED = 1
    SYSTEM_MANAGED = 2

class SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus(enum.IntEnum):
    UNSUPPORTED = 0
    SUCCEEDED = 1
    DISABLED_BY_POLICY = 2

class SecondaryAuthenticationFactorFinishAuthenticationStatus(enum.IntEnum):
    FAILED = 0
    COMPLETED = 1
    NONCE_EXPIRED = 2

class SecondaryAuthenticationFactorRegistrationStatus(enum.IntEnum):
    FAILED = 0
    STARTED = 1
    CANCELED_BY_USER = 2
    PIN_SETUP_REQUIRED = 3
    DISABLED_BY_POLICY = 4

SecondaryAuthenticationFactorAuthentication = _ns_module.SecondaryAuthenticationFactorAuthentication
SecondaryAuthenticationFactorAuthenticationResult = _ns_module.SecondaryAuthenticationFactorAuthenticationResult
SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs = _ns_module.SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs
SecondaryAuthenticationFactorAuthenticationStageInfo = _ns_module.SecondaryAuthenticationFactorAuthenticationStageInfo
SecondaryAuthenticationFactorInfo = _ns_module.SecondaryAuthenticationFactorInfo
SecondaryAuthenticationFactorRegistration = _ns_module.SecondaryAuthenticationFactorRegistration
SecondaryAuthenticationFactorRegistrationResult = _ns_module.SecondaryAuthenticationFactorRegistrationResult
