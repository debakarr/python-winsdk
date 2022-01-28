# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.bluetooth
except Exception:
    pass

try:
    import winsdk.windows.devices.bluetooth.advertisement
except Exception:
    pass

try:
    import winsdk.windows.devices.bluetooth.genericattributeprofile
except Exception:
    pass

try:
    import winsdk.windows.devices.bluetooth.rfcomm
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
    import winsdk.windows.networking.sockets
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class BluetoothEventTriggeringMode(enum.IntEnum):
    SERIAL = 0
    BATCH = 1
    KEEP_LATEST = 2

class BluetoothLEAdvertisementPublisherTriggerDetails(_winrt.Object):
    ...
    error: winsdk.windows.devices.bluetooth.BluetoothError
    status: winsdk.windows.devices.bluetooth.advertisement.BluetoothLEAdvertisementPublisherStatus
    selected_transmit_power_level_in_d_bm: typing.Optional[_winrt.Int16]

class BluetoothLEAdvertisementWatcherTriggerDetails(_winrt.Object):
    ...
    advertisements: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.devices.bluetooth.advertisement.BluetoothLEAdvertisementReceivedEventArgs]
    error: winsdk.windows.devices.bluetooth.BluetoothError
    signal_strength_filter: winsdk.windows.devices.bluetooth.BluetoothSignalStrengthFilter

class GattCharacteristicNotificationTriggerDetails(_winrt.Object):
    ...
    characteristic: winsdk.windows.devices.bluetooth.genericattributeprofile.GattCharacteristic
    value: winsdk.windows.storage.streams.IBuffer
    error: winsdk.windows.devices.bluetooth.BluetoothError
    event_triggering_mode: BluetoothEventTriggeringMode
    value_changed_events: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.devices.bluetooth.genericattributeprofile.GattValueChangedEventArgs]

class GattServiceProviderConnection(_winrt.Object):
    ...
    service: winsdk.windows.devices.bluetooth.genericattributeprofile.GattLocalService
    trigger_id: str
    all_services: winsdk.windows.foundation.collections.IMapView[str, GattServiceProviderConnection]
    def start() -> None:
        ...

class GattServiceProviderTriggerDetails(_winrt.Object):
    ...
    connection: GattServiceProviderConnection

class RfcommConnectionTriggerDetails(_winrt.Object):
    ...
    incoming: _winrt.Boolean
    remote_device: winsdk.windows.devices.bluetooth.BluetoothDevice
    socket: winsdk.windows.networking.sockets.StreamSocket

class RfcommInboundConnectionInformation(_winrt.Object):
    ...
    service_capabilities: winsdk.windows.devices.bluetooth.BluetoothServiceCapabilities
    sdp_record: winsdk.windows.storage.streams.IBuffer
    local_service_id: winsdk.windows.devices.bluetooth.rfcomm.RfcommServiceId

class RfcommOutboundConnectionInformation(_winrt.Object):
    ...
    remote_service_id: winsdk.windows.devices.bluetooth.rfcomm.RfcommServiceId

