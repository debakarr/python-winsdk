# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.i2c.provider
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

class I2cBusSpeed(enum.IntEnum):
    STANDARD_MODE = 0
    FAST_MODE = 1

class I2cSharingMode(enum.IntEnum):
    EXCLUSIVE = 0
    SHARED = 1

class I2cTransferStatus(enum.IntEnum):
    FULL_TRANSFER = 0
    PARTIAL_TRANSFER = 1
    SLAVE_ADDRESS_NOT_ACKNOWLEDGED = 2
    CLOCK_STRETCH_TIMEOUT = 3
    UNKNOWN_ERROR = 4

class I2cTransferResult:
    status: I2cTransferStatus
    bytes_transferred: _winrt.UInt32
    def __init__(self, status: I2cTransferStatus, bytes_transferred: _winrt.UInt32) -> None: ...

class I2cConnectionSettings(_winrt.Object):
    ...
    slave_address: _winrt.Int32
    sharing_mode: I2cSharingMode
    bus_speed: I2cBusSpeed
    def __init__(self, slave_address: _winrt.Int32) -> None:
        ...

class I2cController(_winrt.Object):
    ...
    def get_controllers_async(provider: winsdk.windows.devices.i2c.provider.II2cProvider) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[I2cController]]:
        ...
    def get_default_async() -> winsdk.windows.foundation.IAsyncOperation[I2cController]:
        ...
    def get_device(settings: I2cConnectionSettings) -> I2cDevice:
        ...

class I2cDevice(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    connection_settings: I2cConnectionSettings
    device_id: str
    def close() -> None:
        ...
    def from_id_async(device_id: str, settings: I2cConnectionSettings) -> winsdk.windows.foundation.IAsyncOperation[I2cDevice]:
        ...
    def get_device_selector() -> str:
        ...
    def get_device_selector(friendly_name: str) -> str:
        ...
    def read(buffer_size: _winrt.UInt32) -> typing.List[_winrt.UInt8]:
        ...
    def read_partial(buffer_size: _winrt.UInt32) -> typing.Tuple[I2cTransferResult, typing.List[_winrt.UInt8]]:
        ...
    def write(buffer: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def write_partial(buffer: typing.Sequence[_winrt.UInt8]) -> I2cTransferResult:
        ...
    def write_read(write_buffer: typing.Sequence[_winrt.UInt8], read_buffer_size: _winrt.UInt32) -> typing.List[_winrt.UInt8]:
        ...
    def write_read_partial(write_buffer: typing.Sequence[_winrt.UInt8], read_buffer_size: _winrt.UInt32) -> typing.Tuple[I2cTransferResult, typing.List[_winrt.UInt8]]:
        ...

class II2cDeviceStatics(_winrt.Object):
    ...
    def from_id_async(device_id: str, settings: I2cConnectionSettings) -> winsdk.windows.foundation.IAsyncOperation[I2cDevice]:
        ...
    def get_device_selector() -> str:
        ...
    def get_device_selector(friendly_name: str) -> str:
        ...

