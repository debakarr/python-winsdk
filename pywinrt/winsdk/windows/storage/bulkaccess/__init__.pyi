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

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.storage
except Exception:
    pass

try:
    import winsdk.windows.storage.fileproperties
except Exception:
    pass

try:
    import winsdk.windows.storage.search
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class FileInformation(IStorageItemInformation, winsdk.windows.storage.IStorageFile, winsdk.windows.storage.streams.IInputStreamReference, winsdk.windows.storage.streams.IRandomAccessStreamReference, winsdk.windows.storage.IStorageItem, winsdk.windows.storage.IStorageItemProperties, winsdk.windows.storage.IStorageItem2, winsdk.windows.storage.IStorageItemPropertiesWithProvider, winsdk.windows.storage.IStorageFilePropertiesWithAvailability, winsdk.windows.storage.IStorageFile2, _winrt.Object):
    ...
    basic_properties: winsdk.windows.storage.fileproperties.BasicProperties
    document_properties: winsdk.windows.storage.fileproperties.DocumentProperties
    image_properties: winsdk.windows.storage.fileproperties.ImageProperties
    music_properties: winsdk.windows.storage.fileproperties.MusicProperties
    thumbnail: winsdk.windows.storage.fileproperties.StorageItemThumbnail
    video_properties: winsdk.windows.storage.fileproperties.VideoProperties
    content_type: str
    file_type: str
    is_available: _winrt.Boolean
    attributes: winsdk.windows.storage.FileAttributes
    date_created: winsdk.windows.foundation.DateTime
    name: str
    path: str
    display_name: str
    display_type: str
    folder_relative_id: str
    properties: winsdk.windows.storage.fileproperties.StorageItemContentProperties
    provider: winsdk.windows.storage.StorageProvider
    def copy_and_replace_async(file_to_replace: winsdk.windows.storage.IStorageFile) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def copy_async(destination_folder: winsdk.windows.storage.IStorageFolder) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def copy_async(destination_folder: winsdk.windows.storage.IStorageFolder, desired_new_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def copy_async(destination_folder: winsdk.windows.storage.IStorageFolder, desired_new_name: str, option: winsdk.windows.storage.NameCollisionOption) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def delete_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def delete_async(option: winsdk.windows.storage.StorageDeleteOption) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def get_basic_properties_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.BasicProperties]:
        ...
    def get_parent_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]:
        ...
    def get_thumbnail_async(mode: winsdk.windows.storage.fileproperties.ThumbnailMode) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.StorageItemThumbnail]:
        ...
    def get_thumbnail_async(mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_size: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.StorageItemThumbnail]:
        ...
    def get_thumbnail_async(mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_size: _winrt.UInt32, options: winsdk.windows.storage.fileproperties.ThumbnailOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.StorageItemThumbnail]:
        ...
    def is_equal(item: winsdk.windows.storage.IStorageItem) -> _winrt.Boolean:
        ...
    def is_of_type(type: winsdk.windows.storage.StorageItemTypes) -> _winrt.Boolean:
        ...
    def move_and_replace_async(file_to_replace: winsdk.windows.storage.IStorageFile) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def move_async(destination_folder: winsdk.windows.storage.IStorageFolder) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def move_async(destination_folder: winsdk.windows.storage.IStorageFolder, desired_new_name: str) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def move_async(destination_folder: winsdk.windows.storage.IStorageFolder, desired_new_name: str, option: winsdk.windows.storage.NameCollisionOption) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def open_async(access_mode: winsdk.windows.storage.FileAccessMode) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]:
        ...
    def open_async(access_mode: winsdk.windows.storage.FileAccessMode, options: winsdk.windows.storage.StorageOpenOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStream]:
        ...
    def open_read_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IRandomAccessStreamWithContentType]:
        ...
    def open_sequential_read_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.streams.IInputStream]:
        ...
    def open_transacted_write_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageStreamTransaction]:
        ...
    def open_transacted_write_async(options: winsdk.windows.storage.StorageOpenOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageStreamTransaction]:
        ...
    def rename_async(desired_name: str) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def rename_async(desired_name: str, option: winsdk.windows.storage.NameCollisionOption) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def add_properties_updated(changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageItemInformation, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_properties_updated(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_thumbnail_updated(changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageItemInformation, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_thumbnail_updated(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class FileInformationFactory(_winrt.Object):
    ...
    def __init__(self, query_result: winsdk.windows.storage.search.IStorageQueryResultBase, mode: winsdk.windows.storage.fileproperties.ThumbnailMode) -> None:
        ...
    def __init__(self, query_result: winsdk.windows.storage.search.IStorageQueryResultBase, mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_thumbnail_size: _winrt.UInt32) -> None:
        ...
    def __init__(self, query_result: winsdk.windows.storage.search.IStorageQueryResultBase, mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_thumbnail_size: _winrt.UInt32, thumbnail_options: winsdk.windows.storage.fileproperties.ThumbnailOptions) -> None:
        ...
    def __init__(self, query_result: winsdk.windows.storage.search.IStorageQueryResultBase, mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_thumbnail_size: _winrt.UInt32, thumbnail_options: winsdk.windows.storage.fileproperties.ThumbnailOptions, delay_load: _winrt.Boolean) -> None:
        ...
    def get_files_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[FileInformation]]:
        ...
    def get_files_async(start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[FileInformation]]:
        ...
    def get_folders_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[FolderInformation]]:
        ...
    def get_folders_async(start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[FolderInformation]]:
        ...
    def get_items_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[IStorageItemInformation]]:
        ...
    def get_items_async(start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[IStorageItemInformation]]:
        ...
    def get_virtualized_files_vector() -> _winrt.Object:
        ...
    def get_virtualized_folders_vector() -> _winrt.Object:
        ...
    def get_virtualized_items_vector() -> _winrt.Object:
        ...

class FolderInformation(IStorageItemInformation, winsdk.windows.storage.IStorageFolder, winsdk.windows.storage.IStorageItem, winsdk.windows.storage.IStorageItemProperties, winsdk.windows.storage.search.IStorageFolderQueryOperations, winsdk.windows.storage.IStorageItem2, winsdk.windows.storage.IStorageFolder2, winsdk.windows.storage.IStorageItemPropertiesWithProvider, _winrt.Object):
    ...
    basic_properties: winsdk.windows.storage.fileproperties.BasicProperties
    document_properties: winsdk.windows.storage.fileproperties.DocumentProperties
    image_properties: winsdk.windows.storage.fileproperties.ImageProperties
    music_properties: winsdk.windows.storage.fileproperties.MusicProperties
    thumbnail: winsdk.windows.storage.fileproperties.StorageItemThumbnail
    video_properties: winsdk.windows.storage.fileproperties.VideoProperties
    attributes: winsdk.windows.storage.FileAttributes
    date_created: winsdk.windows.foundation.DateTime
    name: str
    path: str
    display_name: str
    display_type: str
    folder_relative_id: str
    properties: winsdk.windows.storage.fileproperties.StorageItemContentProperties
    provider: winsdk.windows.storage.StorageProvider
    def are_query_options_supported(query_options: winsdk.windows.storage.search.QueryOptions) -> _winrt.Boolean:
        ...
    def create_file_async(desired_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def create_file_async(desired_name: str, options: winsdk.windows.storage.CreationCollisionOption) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def create_file_query() -> winsdk.windows.storage.search.StorageFileQueryResult:
        ...
    def create_file_query(query: winsdk.windows.storage.search.CommonFileQuery) -> winsdk.windows.storage.search.StorageFileQueryResult:
        ...
    def create_file_query_with_options(query_options: winsdk.windows.storage.search.QueryOptions) -> winsdk.windows.storage.search.StorageFileQueryResult:
        ...
    def create_folder_async(desired_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]:
        ...
    def create_folder_async(desired_name: str, options: winsdk.windows.storage.CreationCollisionOption) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]:
        ...
    def create_folder_query() -> winsdk.windows.storage.search.StorageFolderQueryResult:
        ...
    def create_folder_query(query: winsdk.windows.storage.search.CommonFolderQuery) -> winsdk.windows.storage.search.StorageFolderQueryResult:
        ...
    def create_folder_query_with_options(query_options: winsdk.windows.storage.search.QueryOptions) -> winsdk.windows.storage.search.StorageFolderQueryResult:
        ...
    def create_item_query() -> winsdk.windows.storage.search.StorageItemQueryResult:
        ...
    def create_item_query_with_options(query_options: winsdk.windows.storage.search.QueryOptions) -> winsdk.windows.storage.search.StorageItemQueryResult:
        ...
    def delete_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def delete_async(option: winsdk.windows.storage.StorageDeleteOption) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def get_basic_properties_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.BasicProperties]:
        ...
    def get_file_async(name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFile]:
        ...
    def get_files_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFile]]:
        ...
    def get_files_async(query: winsdk.windows.storage.search.CommonFileQuery) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFile]]:
        ...
    def get_files_async(query: winsdk.windows.storage.search.CommonFileQuery, start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFile]]:
        ...
    def get_folder_async(name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]:
        ...
    def get_folders_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFolder]]:
        ...
    def get_folders_async(query: winsdk.windows.storage.search.CommonFolderQuery) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFolder]]:
        ...
    def get_folders_async(query: winsdk.windows.storage.search.CommonFolderQuery, start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.StorageFolder]]:
        ...
    def get_indexed_state_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.search.IndexedState]:
        ...
    def get_item_async(name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]:
        ...
    def get_items_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.IStorageItem]]:
        ...
    def get_items_async(start_index: _winrt.UInt32, max_items_to_retrieve: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.storage.IStorageItem]]:
        ...
    def get_parent_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.StorageFolder]:
        ...
    def get_thumbnail_async(mode: winsdk.windows.storage.fileproperties.ThumbnailMode) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.StorageItemThumbnail]:
        ...
    def get_thumbnail_async(mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_size: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.StorageItemThumbnail]:
        ...
    def get_thumbnail_async(mode: winsdk.windows.storage.fileproperties.ThumbnailMode, requested_size: _winrt.UInt32, options: winsdk.windows.storage.fileproperties.ThumbnailOptions) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.fileproperties.StorageItemThumbnail]:
        ...
    def is_common_file_query_supported(query: winsdk.windows.storage.search.CommonFileQuery) -> _winrt.Boolean:
        ...
    def is_common_folder_query_supported(query: winsdk.windows.storage.search.CommonFolderQuery) -> _winrt.Boolean:
        ...
    def is_equal(item: winsdk.windows.storage.IStorageItem) -> _winrt.Boolean:
        ...
    def is_of_type(type: winsdk.windows.storage.StorageItemTypes) -> _winrt.Boolean:
        ...
    def rename_async(desired_name: str) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def rename_async(desired_name: str, option: winsdk.windows.storage.NameCollisionOption) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def try_get_item_async(name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.storage.IStorageItem]:
        ...
    def add_properties_updated(changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageItemInformation, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_properties_updated(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_thumbnail_updated(changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageItemInformation, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_thumbnail_updated(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class IStorageItemInformation(_winrt.Object):
    ...
    basic_properties: winsdk.windows.storage.fileproperties.BasicProperties
    document_properties: winsdk.windows.storage.fileproperties.DocumentProperties
    image_properties: winsdk.windows.storage.fileproperties.ImageProperties
    music_properties: winsdk.windows.storage.fileproperties.MusicProperties
    thumbnail: winsdk.windows.storage.fileproperties.StorageItemThumbnail
    video_properties: winsdk.windows.storage.fileproperties.VideoProperties
    def add_properties_updated(changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageItemInformation, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_properties_updated(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_thumbnail_updated(changed_handler: winsdk.windows.foundation.TypedEventHandler[IStorageItemInformation, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_thumbnail_updated(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

