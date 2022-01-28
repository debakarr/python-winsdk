# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Media.DialProtocol")

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
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.ui.popups
except Exception:
    pass

class DialAppLaunchResult(enum.IntEnum):
    LAUNCHED = 0
    FAILED_TO_LAUNCH = 1
    NOT_FOUND = 2
    NETWORK_FAILURE = 3

class DialAppState(enum.IntEnum):
    UNKNOWN = 0
    STOPPED = 1
    RUNNING = 2
    NETWORK_FAILURE = 3

class DialAppStopResult(enum.IntEnum):
    STOPPED = 0
    STOP_FAILED = 1
    OPERATION_NOT_SUPPORTED = 2
    NETWORK_FAILURE = 3

class DialDeviceDisplayStatus(enum.IntEnum):
    NONE = 0
    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTING = 3
    DISCONNECTED = 4
    ERROR = 5

DialApp = _ns_module.DialApp
DialAppStateDetails = _ns_module.DialAppStateDetails
DialDevice = _ns_module.DialDevice
DialDevicePicker = _ns_module.DialDevicePicker
DialDevicePickerFilter = _ns_module.DialDevicePickerFilter
DialDeviceSelectedEventArgs = _ns_module.DialDeviceSelectedEventArgs
DialDisconnectButtonClickedEventArgs = _ns_module.DialDisconnectButtonClickedEventArgs
DialReceiverApp = _ns_module.DialReceiverApp
