# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.security.enterprisedata
except Exception:
    pass

try:
    import winsdk.windows.storage
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

class ClipboardHistoryItemsResultStatus(enum.IntEnum):
    SUCCESS = 0
    ACCESS_DENIED = 1
    CLIPBOARD_HISTORY_DISABLED = 2

class DataPackageOperation(enum.IntFlag):
    NONE = 0
    COPY = 0x1
    MOVE = 0x2
    LINK = 0x4

class SetHistoryItemAsContentStatus(enum.IntEnum):
    SUCCESS = 0
    ACCESS_DENIED = 1
    ITEM_DELETED = 2

class ShareUITheme(enum.IntEnum):
    DEFAULT = 0
    LIGHT = 1
    DARK = 2

class Clipboard(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> Clipboard: ...
    @typing.overload
    @staticmethod
    def clear() -> None: ...
    @typing.overload
    @staticmethod
    def clear_history() -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def delete_item_from_history(item: ClipboardHistoryItem) -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def flush() -> None: ...
    @typing.overload
    @staticmethod
    def get_content() -> DataPackageView: ...
    @typing.overload
    @staticmethod
    def get_history_items_async() -> winsdk.windows.foundation.IAsyncOperation[ClipboardHistoryItemsResult]: ...
    @typing.overload
    @staticmethod
    def is_history_enabled() -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def is_roaming_enabled() -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def set_content(content: DataPackage) -> None: ...
    @typing.overload
    @staticmethod
    def set_content_with_options(content: DataPackage, options: ClipboardContentOptions) -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def set_history_item_as_content(item: ClipboardHistoryItem) -> SetHistoryItemAsContentStatus: ...
    @typing.overload
    @staticmethod
    def add_history_changed(handler: winsdk.windows.foundation.EventHandler[ClipboardHistoryChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    @staticmethod
    def remove_history_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    @staticmethod
    def add_history_enabled_changed(handler: winsdk.windows.foundation.EventHandler[_winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    @staticmethod
    def remove_history_enabled_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    @staticmethod
    def add_roaming_enabled_changed(handler: winsdk.windows.foundation.EventHandler[_winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    @staticmethod
    def remove_roaming_enabled_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    @staticmethod
    def add_content_changed(handler: winsdk.windows.foundation.EventHandler[_winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    @staticmethod
    def remove_content_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class ClipboardContentOptions(_winrt.Object):
    is_roamable: _winrt.Boolean
    is_allowed_in_history: _winrt.Boolean
    history_formats: winsdk.windows.foundation.collections.IVector[str]
    roaming_formats: winsdk.windows.foundation.collections.IVector[str]
    @staticmethod
    def _from(obj: _winrt.Object) -> ClipboardContentOptions: ...
    @typing.overload
    def __init__(self) -> None: ...

class ClipboardHistoryChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ClipboardHistoryChangedEventArgs: ...

class ClipboardHistoryItem(_winrt.Object):
    content: DataPackageView
    id: str
    timestamp: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> ClipboardHistoryItem: ...

class ClipboardHistoryItemsResult(_winrt.Object):
    items: winsdk.windows.foundation.collections.IVectorView[ClipboardHistoryItem]
    status: ClipboardHistoryItemsResultStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> ClipboardHistoryItemsResult: ...

class DataPackage(_winrt.Object):
    requested_operation: DataPackageOperation
    properties: DataPackagePropertySet
    resource_map: winsdk.windows.foundation.collections.IMap[str, winsdk.windows.storage.streams.RandomAccessStreamReference]
    @staticmethod
    def _from(obj: _winrt.Object) -> DataPackage: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def get_view(self) -> DataPackageView: ...
    @typing.overload
    def set_application_link(self, value: winsdk.windows.foundation.Uri) -> None: ...
    @typing.overload
    def set_bitmap(self, value: winsdk.windows.storage.streams.RandomAccessStreamReference) -> None: ...
    @typing.overload
    def set_data(self, format_id: str, value: _winrt.Object) -> None: ...
    @typing.overload
    def set_data_provider(self, format_id: str, delay_renderer: DataProviderHandler) -> None: ...
    @typing.overload
    def set_html_format(self, value: str) -> None: ...
    @typing.overload
    def set_rtf(self, value: str) -> None: ...
    @typing.overload
    def set_storage_items(self, value: typing.Iterable[winsdk.windows.storage.IStorageItem]) -> None: ...
    @typing.overload
    def set_storage_items(self, value: typing.Iterable[winsdk.windows.storage.IStorageItem], read_only: _winrt.Boolean) -> None: ...
    @typing.overload
    def set_text(self, value: str) -> None: ...
    @typing.overload
    def set_uri(self, value: winsdk.windows.foundation.Uri) -> None: ...
    @typing.overload
    def set_web_link(self, value: winsdk.windows.foundation.Uri) -> None: ...
    @typing.overload
    def add_destroyed(self, handler: winsdk.windows.foundation.TypedEventHandler[DataPackage, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_destroyed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_operation_completed(self, handler: winsdk.windows.foundation.TypedEventHandler[DataPackage, OperationCompletedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_operation_completed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_share_completed(self, handler: winsdk.windows.foundation.TypedEventHandler[DataPackage, ShareCompletedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_share_completed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_share_canceled(self, handler: winsdk.windows.foundation.TypedEventHandler[DataPackage, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_share_canceled(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class DataPackagePropertySet(winsdk.windows.foundation.collections.IMap[str, _winrt.Object], winsdk.windows.foundation.collections.IIterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]], _winrt.Object):
    title: str
    thumbnail: winsdk.windows.storage.streams.IRandomAccessStreamReference
    description: str
    application_name: str
    application_listing_uri: winsdk.windows.foundation.Uri
    file_types: winsdk.windows.foundation.collections.IVector[str]
    square30x30_logo: winsdk.windows.storage.streams.IRandomAccessStreamReference
    package_family_name: str
    logo_background_color: winsdk.windows.ui.Color
    content_source_web_link: winsdk.windows.foundation.Uri
    content_source_application_link: winsdk.windows.foundation.Uri
    enterprise_id: str
    content_source_user_activity_json: str
    size: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> DataPackagePropertySet: ...
    @typing.overload
    def clear(self) -> None: ...
    @typing.overload
    def first(self) -> winsdk.windows.foundation.collections.IIterator[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]: ...
    @typing.overload
    def get_view(self) -> winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]: ...
    @typing.overload
    def has_key(self, key: str) -> _winrt.Boolean: ...
    @typing.overload
    def insert(self, key: str, value: _winrt.Object) -> _winrt.Boolean: ...
    @typing.overload
    def lookup(self, key: str) -> _winrt.Object: ...
    @typing.overload
    def remove(self, key: str) -> None: ...

class DataPackagePropertySetView(winsdk.windows.foundation.collections.IMapView[str, _winrt.Object], winsdk.windows.foundation.collections.IIterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]], _winrt.Object):
    application_listing_uri: winsdk.windows.foundation.Uri
    application_name: str
    description: str
    file_types: winsdk.windows.foundation.collections.IVectorView[str]
    thumbnail: winsdk.windows.storage.streams.RandomAccessStreamReference
    title: str
    content_source_application_link: winsdk.windows.foundation.Uri
    content_source_web_link: winsdk.windows.foundation.Uri
    logo_background_color: winsdk.windows.ui.Color
    package_family_name: str
    square30x30_logo: winsdk.windows.storage.streams.IRandomAccessStreamReference
    enterprise_id: str
    content_source_user_activity_json: str
    is_from_roaming_clipboard: _winrt.Boolean
    size: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> DataPackagePropertySetView: ...
    @typing.overload
    def first(self) -> winsdk.windows.foundation.collections.IIterator[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]: ...
    @typing.overload
    def has_key(self, key: str) -> _winrt.Boolean: ...
    @typing.overload
    def lookup(self, key: str) -> _winrt.Object: ...
    @typing.overload
    def split(self, ) -> typing.Tuple[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object], winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]: ...

class DataPackageView(_winrt.Object):
    available_formats: winsdk.windows.foundation.collections.IVectorView[str]
    properties: DataPackagePropertySetView
    requested_operation: DataPackageOperation
    @staticmethod
    def _from(obj: _winrt.Object) -> DataPackageView: ...
    @typing.overload
    def contains(self, format_id: str) -> _winrt.Boolean: ...
    @typing.overload
    def get_application_link_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.Uri]: ...
    @typing.overload
    def get_bitmap_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.RandomAccessStreamReference]: ...
    @typing.overload
    def get_data_async(self, format_id: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Object]: ...
    @typing.overload
    def get_html_format_async(self) -> winsdk.windows.foundation.IAsyncOperation[str]: ...
    @typing.overload
    def get_resource_map_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMapView[str, winsdk.windows.storage.streams.RandomAccessStreamReference]]: ...
    @typing.overload
    def get_rtf_async(self) -> winsdk.windows.foundation.IAsyncOperation[str]: ...
    @typing.overload
    def get_storage_items_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.IStorageItem]]: ...
    @typing.overload
    def get_text_async(self) -> winsdk.windows.foundation.IAsyncOperation[str]: ...
    @typing.overload
    def get_text_async(self, format_id: str) -> winsdk.windows.foundation.IAsyncOperation[str]: ...
    @typing.overload
    def get_uri_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.Uri]: ...
    @typing.overload
    def get_web_link_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.Uri]: ...
    @typing.overload
    def report_operation_completed(self, value: DataPackageOperation) -> None: ...
    @typing.overload
    def request_access_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.security.enterprisedata.ProtectionPolicyEvaluationResult]: ...
    @typing.overload
    def request_access_async(self, enterprise_id: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.security.enterprisedata.ProtectionPolicyEvaluationResult]: ...
    @typing.overload
    def set_accepted_format_id(self, format_id: str) -> None: ...
    @typing.overload
    def unlock_and_assume_enterprise_identity(self) -> winsdk.windows.security.enterprisedata.ProtectionPolicyEvaluationResult: ...

class DataProviderDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> DataProviderDeferral: ...
    @typing.overload
    def complete(self) -> None: ...

class DataProviderRequest(_winrt.Object):
    deadline: winsdk.windows.foundation.DateTime
    format_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> DataProviderRequest: ...
    @typing.overload
    def get_deferral(self) -> DataProviderDeferral: ...
    @typing.overload
    def set_data(self, value: _winrt.Object) -> None: ...

class DataRequest(_winrt.Object):
    data: DataPackage
    deadline: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> DataRequest: ...
    @typing.overload
    def fail_with_display_text(self, value: str) -> None: ...
    @typing.overload
    def get_deferral(self) -> DataRequestDeferral: ...

class DataRequestDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> DataRequestDeferral: ...
    @typing.overload
    def complete(self) -> None: ...

class DataRequestedEventArgs(_winrt.Object):
    request: DataRequest
    @staticmethod
    def _from(obj: _winrt.Object) -> DataRequestedEventArgs: ...

class DataTransferManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> DataTransferManager: ...
    @typing.overload
    @staticmethod
    def get_for_current_view() -> DataTransferManager: ...
    @typing.overload
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def show_share_u_i() -> None: ...
    @typing.overload
    @staticmethod
    def show_share_u_i(options: ShareUIOptions) -> None: ...
    @typing.overload
    def add_data_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[DataTransferManager, DataRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_data_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_target_application_chosen(self, handler: winsdk.windows.foundation.TypedEventHandler[DataTransferManager, TargetApplicationChosenEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_target_application_chosen(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_share_providers_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[DataTransferManager, ShareProvidersRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_share_providers_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class HtmlFormatHelper(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> HtmlFormatHelper: ...
    @typing.overload
    @staticmethod
    def create_html_format(html_fragment: str) -> str: ...
    @typing.overload
    @staticmethod
    def get_static_fragment(html_format: str) -> str: ...

class OperationCompletedEventArgs(_winrt.Object):
    operation: DataPackageOperation
    accepted_format_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> OperationCompletedEventArgs: ...

class ShareCompletedEventArgs(_winrt.Object):
    share_target: ShareTargetInfo
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareCompletedEventArgs: ...

class ShareProvider(_winrt.Object):
    tag: _winrt.Object
    background_color: winsdk.windows.ui.Color
    display_icon: winsdk.windows.storage.streams.RandomAccessStreamReference
    title: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareProvider: ...
    @typing.overload
    def __init__(self, title: str, display_icon: winsdk.windows.storage.streams.RandomAccessStreamReference, background_color: winsdk.windows.ui.Color, handler: ShareProviderHandler) -> None: ...

class ShareProviderOperation(_winrt.Object):
    data: DataPackageView
    provider: ShareProvider
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareProviderOperation: ...
    @typing.overload
    def report_completed(self) -> None: ...

class ShareProvidersRequestedEventArgs(_winrt.Object):
    data: DataPackageView
    providers: winsdk.windows.foundation.collections.IVector[ShareProvider]
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareProvidersRequestedEventArgs: ...
    @typing.overload
    def get_deferral(self) -> winsdk.windows.foundation.Deferral: ...

class ShareTargetInfo(_winrt.Object):
    app_user_model_id: str
    share_provider: ShareProvider
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareTargetInfo: ...

class ShareUIOptions(_winrt.Object):
    theme: ShareUITheme
    selection_rect: typing.Optional[winsdk.windows.foundation.Rect]
    @staticmethod
    def _from(obj: _winrt.Object) -> ShareUIOptions: ...
    @typing.overload
    def __init__(self) -> None: ...

class SharedStorageAccessManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SharedStorageAccessManager: ...
    @typing.overload
    @staticmethod
    def add_file(file: winsdk.windows.storage.IStorageFile) -> str: ...
    @typing.overload
    @staticmethod
    def redeem_token_for_file_async(token: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]: ...
    @typing.overload
    @staticmethod
    def remove_file(token: str) -> None: ...

class StandardDataFormats(_winrt.Object):
    bitmap: str
    html: str
    rtf: str
    storage_items: str
    text: str
    uri: str
    application_link: str
    web_link: str
    user_activity_json_array: str
    @staticmethod
    def _from(obj: _winrt.Object) -> StandardDataFormats: ...

class TargetApplicationChosenEventArgs(_winrt.Object):
    application_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> TargetApplicationChosenEventArgs: ...

DataProviderHandler = typing.Callable[[DataProviderRequest], None]

ShareProviderHandler = typing.Callable[[ShareProviderOperation], None]

