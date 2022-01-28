# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

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

class WalletBarcode(_winrt.Object):
    ...
    symbology: WalletBarcodeSymbology
    value: str
    def __init__(self, symbology: WalletBarcodeSymbology, value: str) -> None:
        ...
    def __init__(self, stream_to_barcode_image: winsdk.windows.storage.streams.IRandomAccessStreamReference) -> None:
        ...
    def get_image_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStreamReference]:
        ...

class WalletItem(_winrt.Object):
    ...
    display_name: str
    display_message: str
    logo_text: str
    body_font_color: winsdk.windows.ui.Color
    body_color: winsdk.windows.ui.Color
    body_background_image: winsdk.windows.storage.streams.IRandomAccessStreamReference
    is_display_message_launchable: _winrt.Boolean
    is_acknowledged: _winrt.Boolean
    is_more_transaction_history_launchable: _winrt.Boolean
    header_font_color: winsdk.windows.ui.Color
    header_color: winsdk.windows.ui.Color
    header_background_image: winsdk.windows.storage.streams.IRandomAccessStreamReference
    expiration_date: typing.Optional[winsdk.windows.foundation.DateTime]
    logo99x99: winsdk.windows.storage.streams.IRandomAccessStreamReference
    logo_image: winsdk.windows.storage.streams.IRandomAccessStreamReference
    promotional_image: winsdk.windows.storage.streams.IRandomAccessStreamReference
    logo159x159: winsdk.windows.storage.streams.IRandomAccessStreamReference
    last_updated: typing.Optional[winsdk.windows.foundation.DateTime]
    issuer_display_name: str
    barcode: WalletBarcode
    relevant_date_display_message: str
    relevant_date: typing.Optional[winsdk.windows.foundation.DateTime]
    logo336x336: winsdk.windows.storage.streams.IRandomAccessStreamReference
    kind: WalletItemKind
    display_properties: winsdk.windows.foundation.collections.IMap[str, WalletItemCustomProperty]
    id: str
    relevant_locations: winsdk.windows.foundation.collections.IMap[str, WalletRelevantLocation]
    transaction_history: winsdk.windows.foundation.collections.IMap[str, WalletTransaction]
    verbs: winsdk.windows.foundation.collections.IMap[str, WalletVerb]
    def __init__(self, kind: WalletItemKind, display_name: str) -> None:
        ...

class WalletItemCustomProperty(_winrt.Object):
    ...
    value: str
    summary_view_position: WalletSummaryViewPosition
    name: str
    detail_view_position: WalletDetailViewPosition
    auto_detect_links: _winrt.Boolean
    def __init__(self, name: str, value: str) -> None:
        ...

class WalletItemStore(_winrt.Object):
    ...
    def add_async(id: str, item: WalletItem) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def clear_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def delete_async(id: str) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def get_items_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[WalletItem]]:
        ...
    def get_items_async(kind: WalletItemKind) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[WalletItem]]:
        ...
    def get_wallet_item_async(id: str) -> winsdk.windows.foundation.IAsyncOperation[WalletItem]:
        ...
    def import_item_async(stream: winsdk.windows.storage.streams.IRandomAccessStreamReference) -> winsdk.windows.foundation.IAsyncOperation[WalletItem]:
        ...
    def show_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def show_async(id: str) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def update_async(item: WalletItem) -> winsdk.windows.foundation.IAsyncAction:
        ...

class WalletManager(_winrt.Object):
    ...
    def request_store_async() -> winsdk.windows.foundation.IAsyncOperation[WalletItemStore]:
        ...

class WalletRelevantLocation(_winrt.Object):
    ...
    position: winsdk.windows.devices.geolocation.BasicGeoposition
    display_message: str
    def __init__(self, ) -> None:
        ...

class WalletTransaction(_winrt.Object):
    ...
    transaction_date: typing.Optional[winsdk.windows.foundation.DateTime]
    is_launchable: _winrt.Boolean
    ignore_time_of_day: _winrt.Boolean
    display_location: str
    display_amount: str
    description: str
    def __init__(self, ) -> None:
        ...

class WalletVerb(_winrt.Object):
    ...
    name: str
    def __init__(self, name: str) -> None:
        ...

