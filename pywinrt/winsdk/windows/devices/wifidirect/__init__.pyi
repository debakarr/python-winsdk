# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.enumeration
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.networking
except Exception:
    pass

try:
    import winsdk.windows.security.credentials
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class WiFiDirectAdvertisementListenStateDiscoverability(enum.IntEnum):
    NONE = 0
    NORMAL = 1
    INTENSIVE = 2

class WiFiDirectAdvertisementPublisherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    STOPPED = 2
    ABORTED = 3

class WiFiDirectConfigurationMethod(enum.IntEnum):
    PROVIDE_PIN = 0
    DISPLAY_PIN = 1
    PUSH_BUTTON = 2

class WiFiDirectConnectionStatus(enum.IntEnum):
    DISCONNECTED = 0
    CONNECTED = 1

class WiFiDirectDeviceSelectorType(enum.IntEnum):
    DEVICE_INTERFACE = 0
    ASSOCIATION_ENDPOINT = 1

class WiFiDirectError(enum.IntEnum):
    SUCCESS = 0
    RADIO_NOT_AVAILABLE = 1
    RESOURCE_IN_USE = 2

class WiFiDirectPairingProcedure(enum.IntEnum):
    GROUP_OWNER_NEGOTIATION = 0
    INVITATION = 1

class WiFiDirectAdvertisement(_winrt.Object):
    ...
    listen_state_discoverability: WiFiDirectAdvertisementListenStateDiscoverability
    is_autonomous_group_owner_enabled: _winrt.Boolean
    information_elements: winsdk.windows.foundation.collections.IVector[WiFiDirectInformationElement]
    legacy_settings: WiFiDirectLegacySettings
    supported_configuration_methods: winsdk.windows.foundation.collections.IVector[WiFiDirectConfigurationMethod]

class WiFiDirectAdvertisementPublisher(_winrt.Object):
    ...
    advertisement: WiFiDirectAdvertisement
    status: WiFiDirectAdvertisementPublisherStatus
    def __init__(self, ) -> None:
        ...
    def start() -> None:
        ...
    def stop() -> None:
        ...
    def add_status_changed(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectAdvertisementPublisher, WiFiDirectAdvertisementPublisherStatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_status_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class WiFiDirectAdvertisementPublisherStatusChangedEventArgs(_winrt.Object):
    ...
    error: WiFiDirectError
    status: WiFiDirectAdvertisementPublisherStatus

class WiFiDirectConnectionListener(_winrt.Object):
    ...
    def __init__(self, ) -> None:
        ...
    def add_connection_requested(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectConnectionListener, WiFiDirectConnectionRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_connection_requested(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class WiFiDirectConnectionParameters(winsdk.windows.devices.enumeration.IDevicePairingSettings, _winrt.Object):
    ...
    group_owner_intent: _winrt.Int16
    preferred_pairing_procedure: WiFiDirectPairingProcedure
    preference_ordered_configuration_methods: winsdk.windows.foundation.collections.IVector[WiFiDirectConfigurationMethod]
    def __init__(self, ) -> None:
        ...
    def get_device_pairing_kinds(configuration_method: WiFiDirectConfigurationMethod) -> winsdk.windows.devices.enumeration.DevicePairingKinds:
        ...

class WiFiDirectConnectionRequest(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    device_information: winsdk.windows.devices.enumeration.DeviceInformation
    def close() -> None:
        ...

class WiFiDirectConnectionRequestedEventArgs(_winrt.Object):
    ...
    def get_connection_request() -> WiFiDirectConnectionRequest:
        ...

class WiFiDirectDevice(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    connection_status: WiFiDirectConnectionStatus
    device_id: str
    def close() -> None:
        ...
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectDevice]:
        ...
    def from_id_async(device_id: str, connection_parameters: WiFiDirectConnectionParameters) -> winsdk.windows.foundation.IAsyncOperation[WiFiDirectDevice]:
        ...
    def get_connection_endpoint_pairs() -> winsdk.windows.foundation.collections.IVectorView[winsdk.windows.networking.EndpointPair]:
        ...
    def get_device_selector() -> str:
        ...
    def get_device_selector(type: WiFiDirectDeviceSelectorType) -> str:
        ...
    def add_connection_status_changed(handler: winsdk.windows.foundation.TypedEventHandler[WiFiDirectDevice, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_connection_status_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class WiFiDirectInformationElement(_winrt.Object):
    ...
    value: winsdk.windows.storage.streams.IBuffer
    oui_type: _winrt.UInt8
    oui: winsdk.windows.storage.streams.IBuffer
    def __init__(self, ) -> None:
        ...
    def create_from_buffer(buffer: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.collections.IVector[WiFiDirectInformationElement]:
        ...
    def create_from_device_information(device_information: winsdk.windows.devices.enumeration.DeviceInformation) -> winsdk.windows.foundation.collections.IVector[WiFiDirectInformationElement]:
        ...

class WiFiDirectLegacySettings(_winrt.Object):
    ...
    ssid: str
    passphrase: winsdk.windows.security.credentials.PasswordCredential
    is_enabled: _winrt.Boolean

