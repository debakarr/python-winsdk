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
    import winsdk.windows.storage
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class PhotoImportAccessMode(enum.IntEnum):
    READ_WRITE = 0
    READ_ONLY = 1
    READ_AND_DELETE = 2

class PhotoImportConnectionTransport(enum.IntEnum):
    UNKNOWN = 0
    USB = 1
    I_P = 2
    BLUETOOTH = 3

class PhotoImportContentType(enum.IntEnum):
    UNKNOWN = 0
    IMAGE = 1
    VIDEO = 2

class PhotoImportContentTypeFilter(enum.IntEnum):
    ONLY_IMAGES = 0
    ONLY_VIDEOS = 1
    IMAGES_AND_VIDEOS = 2
    IMAGES_AND_VIDEOS_FROM_CAMERA_ROLL = 3

class PhotoImportImportMode(enum.IntEnum):
    IMPORT_EVERYTHING = 0
    IGNORE_SIDECARS = 1
    IGNORE_SIBLINGS = 2
    IGNORE_SIDECARS_AND_SIBLINGS = 3

class PhotoImportItemSelectionMode(enum.IntEnum):
    SELECT_ALL = 0
    SELECT_NONE = 1
    SELECT_NEW = 2

class PhotoImportPowerSource(enum.IntEnum):
    UNKNOWN = 0
    BATTERY = 1
    EXTERNAL = 2

class PhotoImportSourceType(enum.IntEnum):
    GENERIC = 0
    CAMERA = 1
    MEDIA_PLAYER = 2
    PHONE = 3
    VIDEO = 4
    PERSONAL_INFO_MANAGER = 5
    AUDIO_RECORDER = 6

class PhotoImportStage(enum.IntEnum):
    NOT_STARTED = 0
    FINDING_ITEMS = 1
    IMPORTING_ITEMS = 2
    DELETING_IMPORTED_ITEMS_FROM_SOURCE = 3

class PhotoImportStorageMediumType(enum.IntEnum):
    UNDEFINED = 0
    FIXED = 1
    REMOVABLE = 2

class PhotoImportSubfolderCreationMode(enum.IntEnum):
    DO_NOT_CREATE_SUBFOLDERS = 0
    CREATE_SUBFOLDERS_FROM_FILE_DATE = 1
    CREATE_SUBFOLDERS_FROM_EXIF_DATE = 2
    KEEP_ORIGINAL_FOLDER_STRUCTURE = 3

class PhotoImportSubfolderDateFormat(enum.IntEnum):
    YEAR = 0
    YEAR_MONTH = 1
    YEAR_MONTH_DAY = 2

class PhotoImportProgress:
    items_imported: _winrt.UInt32
    total_items_to_import: _winrt.UInt32
    bytes_imported: _winrt.UInt64
    total_bytes_to_import: _winrt.UInt64
    import_progress: _winrt.Double
    def __init__(self, items_imported: _winrt.UInt32, total_items_to_import: _winrt.UInt32, bytes_imported: _winrt.UInt64, total_bytes_to_import: _winrt.UInt64, import_progress: _winrt.Double) -> None: ...

class PhotoImportDeleteImportedItemsFromSourceResult(_winrt.Object):
    deleted_items: winsdk.windows.foundation.collections.IVectorView[PhotoImportItem]
    has_succeeded: _winrt.Boolean
    photos_count: _winrt.UInt32
    photos_size_in_bytes: _winrt.UInt64
    session: PhotoImportSession
    siblings_count: _winrt.UInt32
    siblings_size_in_bytes: _winrt.UInt64
    sidecars_count: _winrt.UInt32
    sidecars_size_in_bytes: _winrt.UInt64
    total_count: _winrt.UInt32
    total_size_in_bytes: _winrt.UInt64
    videos_count: _winrt.UInt32
    videos_size_in_bytes: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportDeleteImportedItemsFromSourceResult: ...

class PhotoImportFindItemsResult(_winrt.Object):
    found_items: winsdk.windows.foundation.collections.IVectorView[PhotoImportItem]
    has_succeeded: _winrt.Boolean
    import_mode: PhotoImportImportMode
    photos_count: _winrt.UInt32
    photos_size_in_bytes: _winrt.UInt64
    selected_photos_count: _winrt.UInt32
    selected_photos_size_in_bytes: _winrt.UInt64
    selected_siblings_count: _winrt.UInt32
    selected_siblings_size_in_bytes: _winrt.UInt64
    selected_sidecars_count: _winrt.UInt32
    selected_sidecars_size_in_bytes: _winrt.UInt64
    selected_total_count: _winrt.UInt32
    selected_total_size_in_bytes: _winrt.UInt64
    selected_videos_count: _winrt.UInt32
    selected_videos_size_in_bytes: _winrt.UInt64
    session: PhotoImportSession
    siblings_count: _winrt.UInt32
    siblings_size_in_bytes: _winrt.UInt64
    sidecars_count: _winrt.UInt32
    sidecars_size_in_bytes: _winrt.UInt64
    total_count: _winrt.UInt32
    total_size_in_bytes: _winrt.UInt64
    videos_count: _winrt.UInt32
    videos_size_in_bytes: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportFindItemsResult: ...
    @typing.overload
    def add_items_in_date_range_to_selection(self, range_start: winsdk.windows.foundation.DateTime, range_length: winsdk.windows.foundation.TimeSpan) -> None: ...
    @typing.overload
    def import_items_async(self) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PhotoImportImportItemsResult, PhotoImportProgress]: ...
    @typing.overload
    def select_all(self) -> None: ...
    @typing.overload
    def select_new_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def select_none(self) -> None: ...
    @typing.overload
    def set_import_mode(self, value: PhotoImportImportMode) -> None: ...
    @typing.overload
    def add_item_imported(self, value: winsdk.windows.foundation.TypedEventHandler[PhotoImportFindItemsResult, PhotoImportItemImportedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_item_imported(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_selection_changed(self, value: winsdk.windows.foundation.TypedEventHandler[PhotoImportFindItemsResult, PhotoImportSelectionChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_selection_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class PhotoImportImportItemsResult(_winrt.Object):
    has_succeeded: _winrt.Boolean
    imported_items: winsdk.windows.foundation.collections.IVectorView[PhotoImportItem]
    photos_count: _winrt.UInt32
    photos_size_in_bytes: _winrt.UInt64
    session: PhotoImportSession
    siblings_count: _winrt.UInt32
    siblings_size_in_bytes: _winrt.UInt64
    sidecars_count: _winrt.UInt32
    sidecars_size_in_bytes: _winrt.UInt64
    total_count: _winrt.UInt32
    total_size_in_bytes: _winrt.UInt64
    videos_count: _winrt.UInt32
    videos_size_in_bytes: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportImportItemsResult: ...
    @typing.overload
    def delete_imported_items_from_source_async(self) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PhotoImportDeleteImportedItemsFromSourceResult, _winrt.Double]: ...

class PhotoImportItem(_winrt.Object):
    is_selected: _winrt.Boolean
    content_type: PhotoImportContentType
    date: winsdk.windows.foundation.DateTime
    deleted_file_names: winsdk.windows.foundation.collections.IVectorView[str]
    imported_file_names: winsdk.windows.foundation.collections.IVectorView[str]
    item_key: _winrt.UInt64
    name: str
    sibling: PhotoImportSidecar
    sidecars: winsdk.windows.foundation.collections.IVectorView[PhotoImportSidecar]
    size_in_bytes: _winrt.UInt64
    thumbnail: winsdk.windows.storage.streams.IRandomAccessStreamReference
    video_segments: winsdk.windows.foundation.collections.IVectorView[PhotoImportVideoSegment]
    path: str
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportItem: ...

class PhotoImportItemImportedEventArgs(_winrt.Object):
    imported_item: PhotoImportItem
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportItemImportedEventArgs: ...

class PhotoImportManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportManager: ...
    @typing.overload
    @staticmethod
    def find_all_sources_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[PhotoImportSource]]: ...
    @typing.overload
    @staticmethod
    def get_pending_operations() -> winsdk.windows.foundation.collections.IVectorView[PhotoImportOperation]: ...
    @typing.overload
    @staticmethod
    def is_supported_async() -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class PhotoImportOperation(_winrt.Object):
    continue_deleting_imported_items_from_source_async: winsdk.windows.foundation.IAsyncOperationWithProgress[PhotoImportDeleteImportedItemsFromSourceResult, _winrt.Double]
    continue_finding_items_async: winsdk.windows.foundation.IAsyncOperationWithProgress[PhotoImportFindItemsResult, _winrt.UInt32]
    continue_importing_items_async: winsdk.windows.foundation.IAsyncOperationWithProgress[PhotoImportImportItemsResult, PhotoImportProgress]
    session: PhotoImportSession
    stage: PhotoImportStage
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportOperation: ...

class PhotoImportSelectionChangedEventArgs(_winrt.Object):
    is_selection_empty: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportSelectionChangedEventArgs: ...

class PhotoImportSession(winsdk.windows.foundation.IClosable, _winrt.Object):
    subfolder_creation_mode: PhotoImportSubfolderCreationMode
    destination_folder: winsdk.windows.storage.IStorageFolder
    destination_file_name_prefix: str
    append_session_date_to_destination_folder: _winrt.Boolean
    session_id: uuid.UUID
    source: PhotoImportSource
    subfolder_date_format: PhotoImportSubfolderDateFormat
    remember_deselected_items: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportSession: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    def find_items_async(self, content_type_filter: PhotoImportContentTypeFilter, item_selection_mode: PhotoImportItemSelectionMode) -> winsdk.windows.foundation.IAsyncOperationWithProgress[PhotoImportFindItemsResult, _winrt.UInt32]: ...

class PhotoImportSidecar(_winrt.Object):
    date: winsdk.windows.foundation.DateTime
    name: str
    size_in_bytes: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportSidecar: ...

class PhotoImportSource(_winrt.Object):
    battery_level_percent: typing.Optional[_winrt.UInt32]
    connection_protocol: str
    connection_transport: PhotoImportConnectionTransport
    date_time: typing.Optional[winsdk.windows.foundation.DateTime]
    description: str
    display_name: str
    id: str
    is_locked: typing.Optional[_winrt.Boolean]
    is_mass_storage: _winrt.Boolean
    manufacturer: str
    model: str
    power_source: PhotoImportPowerSource
    serial_number: str
    storage_media: winsdk.windows.foundation.collections.IVectorView[PhotoImportStorageMedium]
    thumbnail: winsdk.windows.storage.streams.IRandomAccessStreamReference
    type: PhotoImportSourceType
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportSource: ...
    @typing.overload
    def create_import_session(self) -> PhotoImportSession: ...
    @typing.overload
    @staticmethod
    def from_folder_async(source_root_folder: winsdk.windows.storage.IStorageFolder) -> winsdk.windows.foundation.IAsyncOperation[PhotoImportSource]: ...
    @typing.overload
    @staticmethod
    def from_id_async(source_id: str) -> winsdk.windows.foundation.IAsyncOperation[PhotoImportSource]: ...

class PhotoImportStorageMedium(_winrt.Object):
    available_space_in_bytes: _winrt.UInt64
    capacity_in_bytes: _winrt.UInt64
    description: str
    name: str
    serial_number: str
    storage_medium_type: PhotoImportStorageMediumType
    supported_access_mode: PhotoImportAccessMode
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportStorageMedium: ...
    @typing.overload
    def refresh(self) -> None: ...

class PhotoImportVideoSegment(_winrt.Object):
    date: winsdk.windows.foundation.DateTime
    name: str
    sibling: PhotoImportSidecar
    sidecars: winsdk.windows.foundation.collections.IVectorView[PhotoImportSidecar]
    size_in_bytes: _winrt.UInt64
    @staticmethod
    def _from(obj: _winrt.Object) -> PhotoImportVideoSegment: ...

