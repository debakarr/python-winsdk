# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices")

try:
    import winsdk.windows.devices.adc.provider
except Exception:
    pass

try:
    import winsdk.windows.devices.gpio.provider
except Exception:
    pass

try:
    import winsdk.windows.devices.i2c.provider
except Exception:
    pass

try:
    import winsdk.windows.devices.pwm.provider
except Exception:
    pass

try:
    import winsdk.windows.devices.spi.provider
except Exception:
    pass

LowLevelDevicesAggregateProvider = _ns_module.LowLevelDevicesAggregateProvider
LowLevelDevicesController = _ns_module.LowLevelDevicesController
ILowLevelDevicesAggregateProvider = _ns_module.ILowLevelDevicesAggregateProvider
