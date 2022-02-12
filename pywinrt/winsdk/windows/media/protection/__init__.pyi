# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.media.playback
except Exception:
    pass

class GraphicsTrustStatus(enum.IntEnum):
    TRUST_NOT_REQUIRED = 0
    TRUST_ESTABLISHED = 1
    ENVIRONMENT_NOT_SUPPORTED = 2
    DRIVER_NOT_SUPPORTED = 3
    DRIVER_SIGNING_FAILURE = 4
    UNKNOWN_FAILURE = 5

class HdcpProtection(enum.IntEnum):
    OFF = 0
    ON = 1
    ON_WITH_TYPE_ENFORCEMENT = 2

class HdcpSetProtectionResult(enum.IntEnum):
    SUCCESS = 0
    TIMED_OUT = 1
    NOT_SUPPORTED = 2
    UNKNOWN_FAILURE = 3

class ProtectionCapabilityResult(enum.IntEnum):
    NOT_SUPPORTED = 0
    MAYBE = 1
    PROBABLY = 2

class RevocationAndRenewalReasons(enum.IntFlag):
    USER_MODE_COMPONENT_LOAD = 0x1
    KERNEL_MODE_COMPONENT_LOAD = 0x2
    APP_COMPONENT = 0x4
    GLOBAL_REVOCATION_LIST_LOAD_FAILED = 0x10
    INVALID_GLOBAL_REVOCATION_LIST_SIGNATURE = 0x20
    GLOBAL_REVOCATION_LIST_ABSENT = 0x1000
    COMPONENT_REVOKED = 0x2000
    INVALID_COMPONENT_CERTIFICATE_EXTENDED_KEY_USE = 0x4000
    COMPONENT_CERTIFICATE_REVOKED = 0x8000
    INVALID_COMPONENT_CERTIFICATE_ROOT = 0x10000
    COMPONENT_HIGH_SECURITY_CERTIFICATE_REVOKED = 0x20000
    COMPONENT_LOW_SECURITY_CERTIFICATE_REVOKED = 0x40000
    BOOT_DRIVER_VERIFICATION_FAILED = 0x100000
    COMPONENT_SIGNED_WITH_TEST_CERTIFICATE = 0x1000000
    ENCRYPTION_FAILURE = 0x10000000

class ComponentLoadFailedEventArgs(_winrt.Object):
    completion: MediaProtectionServiceCompletion
    information: RevocationAndRenewalInformation
    @staticmethod
    def _from(obj: _winrt.Object) -> ComponentLoadFailedEventArgs: ...

class HdcpSession(winsdk.windows.foundation.IClosable, _winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> HdcpSession: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    def get_effective_protection(self) -> typing.Optional[HdcpProtection]: ...
    @typing.overload
    def is_effective_protection_at_least(self, protection: HdcpProtection) -> _winrt.Boolean: ...
    @typing.overload
    def set_desired_min_protection_async(self, protection: HdcpProtection) -> winsdk.windows.foundation.IAsyncOperation[HdcpSetProtectionResult]: ...
    @typing.overload
    def add_protection_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[HdcpSession, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_protection_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class MediaProtectionManager(_winrt.Object):
    properties: winsdk.windows.foundation.collections.IPropertySet
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaProtectionManager: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def add_component_load_failed(self, handler: ComponentLoadFailedEventHandler) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_component_load_failed(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_reboot_needed(self, handler: RebootNeededEventHandler) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_reboot_needed(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_service_requested(self, handler: ServiceRequestedEventHandler) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_service_requested(self, cookie: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class MediaProtectionPMPServer(_winrt.Object):
    properties: winsdk.windows.foundation.collections.IPropertySet
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaProtectionPMPServer: ...
    @typing.overload
    def __init__(self, p_properties: winsdk.windows.foundation.collections.IPropertySet) -> None: ...

class MediaProtectionServiceCompletion(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaProtectionServiceCompletion: ...
    @typing.overload
    def complete(self, success: _winrt.Boolean) -> None: ...

class ProtectionCapabilities(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ProtectionCapabilities: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def is_type_supported(self, type: str, key_system: str) -> ProtectionCapabilityResult: ...

class RevocationAndRenewalInformation(_winrt.Object):
    items: winsdk.windows.foundation.collections.IVector[RevocationAndRenewalItem]
    @staticmethod
    def _from(obj: _winrt.Object) -> RevocationAndRenewalInformation: ...

class RevocationAndRenewalItem(_winrt.Object):
    header_hash: str
    name: str
    public_key_hash: str
    reasons: RevocationAndRenewalReasons
    renewal_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> RevocationAndRenewalItem: ...

class ServiceRequestedEventArgs(_winrt.Object):
    completion: MediaProtectionServiceCompletion
    request: IMediaProtectionServiceRequest
    media_playback_item: winsdk.windows.media.playback.MediaPlaybackItem
    @staticmethod
    def _from(obj: _winrt.Object) -> ServiceRequestedEventArgs: ...

class IMediaProtectionServiceRequest(_winrt.Object):
    protection_system: uuid.UUID
    type: uuid.UUID
    @staticmethod
    def _from(obj: _winrt.Object) -> IMediaProtectionServiceRequest: ...

ComponentLoadFailedEventHandler = typing.Callable[[MediaProtectionManager, ComponentLoadFailedEventArgs], None]

RebootNeededEventHandler = typing.Callable[[MediaProtectionManager], None]

ServiceRequestedEventHandler = typing.Callable[[MediaProtectionManager, ServiceRequestedEventArgs], None]

