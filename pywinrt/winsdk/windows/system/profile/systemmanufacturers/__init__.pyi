# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation
except Exception:
    pass

class OemSupportInfo(_winrt.Object):
    ...
    support_app_link: winsdk.windows.foundation.Uri
    support_link: winsdk.windows.foundation.Uri
    support_provider: str

class SmbiosInformation(_winrt.Object):
    ...
    serial_number: str

class SystemSupportDeviceInfo(_winrt.Object):
    ...
    friendly_name: str
    operating_system: str
    system_firmware_version: str
    system_hardware_version: str
    system_manufacturer: str
    system_product_name: str
    system_sku: str

class SystemSupportInfo(_winrt.Object):
    ...
    local_system_edition: str
    oem_support_info: OemSupportInfo
    local_device_info: SystemSupportDeviceInfo

