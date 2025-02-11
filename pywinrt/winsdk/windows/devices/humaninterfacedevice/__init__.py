# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.HumanInterfaceDevice")

try:
    import winsdk.windows.foundation
except ImportError:
    pass

try:
    import winsdk.windows.foundation.collections
except ImportError:
    pass

try:
    import winsdk.windows.storage
except ImportError:
    pass

try:
    import winsdk.windows.storage.streams
except ImportError:
    pass

class HidCollectionType(enum.IntEnum):
    PHYSICAL = 0
    APPLICATION = 1
    LOGICAL = 2
    REPORT = 3
    NAMED_ARRAY = 4
    USAGE_SWITCH = 5
    USAGE_MODIFIER = 6
    OTHER = 7

class HidReportType(enum.IntEnum):
    INPUT = 0
    OUTPUT = 1
    FEATURE = 2

_ns_module._register_HidCollectionType(HidCollectionType)
_ns_module._register_HidReportType(HidReportType)

HidBooleanControl = _ns_module.HidBooleanControl
HidBooleanControlDescription = _ns_module.HidBooleanControlDescription
HidCollection = _ns_module.HidCollection
HidDevice = _ns_module.HidDevice
HidFeatureReport = _ns_module.HidFeatureReport
HidInputReport = _ns_module.HidInputReport
HidInputReportReceivedEventArgs = _ns_module.HidInputReportReceivedEventArgs
HidNumericControl = _ns_module.HidNumericControl
HidNumericControlDescription = _ns_module.HidNumericControlDescription
HidOutputReport = _ns_module.HidOutputReport
