# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.Wallet")

try:
    import winsdk.windows.devices.geolocation
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
    import winsdk.windows.ui
except Exception:
    pass

class WalletBarcodeSymbology(enum.IntEnum):
    INVALID = 0
    UPCA = 1
    UPCE = 2
    EAN13 = 3
    EAN8 = 4
    ITF = 5
    CODE39 = 6
    CODE128 = 7
    QR = 8
    PDF417 = 9
    AZTEC = 10
    CUSTOM = 100000

class WalletDetailViewPosition(enum.IntEnum):
    HIDDEN = 0
    HEADER_FIELD1 = 1
    HEADER_FIELD2 = 2
    PRIMARY_FIELD1 = 3
    PRIMARY_FIELD2 = 4
    SECONDARY_FIELD1 = 5
    SECONDARY_FIELD2 = 6
    SECONDARY_FIELD3 = 7
    SECONDARY_FIELD4 = 8
    SECONDARY_FIELD5 = 9
    CENTER_FIELD1 = 10
    FOOTER_FIELD1 = 11
    FOOTER_FIELD2 = 12
    FOOTER_FIELD3 = 13
    FOOTER_FIELD4 = 14

class WalletItemKind(enum.IntEnum):
    INVALID = 0
    DEAL = 1
    GENERAL = 2
    PAYMENT_INSTRUMENT = 3
    TICKET = 4
    BOARDING_PASS = 5
    MEMBERSHIP_CARD = 6

class WalletSummaryViewPosition(enum.IntEnum):
    HIDDEN = 0
    FIELD1 = 1
    FIELD2 = 2

WalletBarcode = _ns_module.WalletBarcode
WalletItem = _ns_module.WalletItem
WalletItemCustomProperty = _ns_module.WalletItemCustomProperty
WalletItemStore = _ns_module.WalletItemStore
WalletManager = _ns_module.WalletManager
WalletRelevantLocation = _ns_module.WalletRelevantLocation
WalletTransaction = _ns_module.WalletTransaction
WalletVerb = _ns_module.WalletVerb
