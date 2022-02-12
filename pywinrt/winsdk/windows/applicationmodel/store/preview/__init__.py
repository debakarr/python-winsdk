# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.Store.Preview")

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.security.authentication.web.core
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

try:
    import winsdk.windows.system
except Exception:
    pass

try:
    import winsdk.windows.ui.xaml
except Exception:
    pass

class DeliveryOptimizationDownloadMode(enum.IntEnum):
    SIMPLE = 0
    HTTP_ONLY = 1
    LAN = 2
    GROUP = 3
    INTERNET = 4
    BYPASS = 5

class DeliveryOptimizationDownloadModeSource(enum.IntEnum):
    DEFAULT = 0
    POLICY = 1

class StoreLogOptions(enum.IntFlag):
    NONE = 0
    TRY_ELEVATE = 0x1

class StorePreviewProductPurchaseStatus(enum.IntEnum):
    SUCCEEDED = 0
    ALREADY_PURCHASED = 1
    NOT_FULFILLED = 2
    NOT_PURCHASED = 3

class StoreSystemFeature(enum.IntEnum):
    ARCHITECTURE_X86 = 0
    ARCHITECTURE_X64 = 1
    ARCHITECTURE_ARM = 2
    DIRECT_X9 = 3
    DIRECT_X10 = 4
    DIRECT_X11 = 5
    D3_D12_HARDWARE_F_L11 = 6
    D3_D12_HARDWARE_F_L12 = 7
    MEMORY300_M_B = 8
    MEMORY750_M_B = 9
    MEMORY1_G_B = 10
    MEMORY2_G_B = 11
    CAMERA_FRONT = 12
    CAMERA_REAR = 13
    GYROSCOPE = 14
    HOVER = 15
    MAGNETOMETER = 16
    NFC = 17
    RESOLUTION720_P = 18
    RESOLUTION_WVGA = 19
    RESOLUTION_WVGA_OR720_P = 20
    RESOLUTION_WXGA = 21
    RESOLUTION_WVGA_OR_WXGA = 22
    RESOLUTION_WXGA_OR720_P = 23
    MEMORY4_G_B = 24
    MEMORY6_G_B = 25
    MEMORY8_G_B = 26
    MEMORY12_G_B = 27
    MEMORY16_G_B = 28
    MEMORY20_G_B = 29
    VIDEO_MEMORY2_G_B = 30
    VIDEO_MEMORY4_G_B = 31
    VIDEO_MEMORY6_G_B = 32
    VIDEO_MEMORY1_G_B = 33
    ARCHITECTURE_ARM64 = 34

DeliveryOptimizationSettings = _ns_module.DeliveryOptimizationSettings
StoreConfiguration = _ns_module.StoreConfiguration
StoreHardwareManufacturerInfo = _ns_module.StoreHardwareManufacturerInfo
StorePreview = _ns_module.StorePreview
StorePreviewProductInfo = _ns_module.StorePreviewProductInfo
StorePreviewPurchaseResults = _ns_module.StorePreviewPurchaseResults
StorePreviewSkuInfo = _ns_module.StorePreviewSkuInfo
WebAuthenticationCoreManagerHelper = _ns_module.WebAuthenticationCoreManagerHelper
