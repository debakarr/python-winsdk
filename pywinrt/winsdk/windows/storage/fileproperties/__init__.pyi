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
    import winsdk.windows.storage
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class PhotoOrientation(enum.IntEnum):
    UNSPECIFIED = 0
    NORMAL = 1
    FLIP_HORIZONTAL = 2
    ROTATE180 = 3
    FLIP_VERTICAL = 4
    TRANSPOSE = 5
    ROTATE270 = 6
    TRANSVERSE = 7
    ROTATE90 = 8

class PropertyPrefetchOptions(enum.IntFlag):
    NONE = 0
    MUSIC_PROPERTIES = 0x1
    VIDEO_PROPERTIES = 0x2
    IMAGE_PROPERTIES = 0x4
    DOCUMENT_PROPERTIES = 0x8
    BASIC_PROPERTIES = 0x10

class ThumbnailMode(enum.IntEnum):
    PICTURES_VIEW = 0
    VIDEOS_VIEW = 1
    MUSIC_VIEW = 2
    DOCUMENTS_VIEW = 3
    LIST_VIEW = 4
    SINGLE_ITEM = 5

class ThumbnailOptions(enum.IntFlag):
    NONE = 0
    RETURN_ONLY_IF_CACHED = 0x1
    RESIZE_THUMBNAIL = 0x2
    USE_CURRENT_SCALE = 0x4

class ThumbnailType(enum.IntEnum):
    IMAGE = 0
    ICON = 1

class VideoOrientation(enum.IntEnum):
    NORMAL = 0
    ROTATE90 = 90
    ROTATE180 = 180
    ROTATE270 = 270

class BasicProperties(IStorageItemExtraProperties, _winrt.Object):
    ...
    date_modified: winsdk.windows.foundation.DateTime
    item_date: winsdk.windows.foundation.DateTime
    size: _winrt.UInt64
    def retrieve_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]:
        ...
    def save_properties_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_properties_async(properties_to_save: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

class DocumentProperties(IStorageItemExtraProperties, _winrt.Object):
    ...
    title: str
    comment: str
    author: winsdk.windows.foundation.collections.IVector[str]
    keywords: winsdk.windows.foundation.collections.IVector[str]
    def retrieve_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]:
        ...
    def save_properties_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_properties_async(properties_to_save: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

class GeotagHelper(_winrt.Object):
    ...
    def get_geotag_async(file: winsdk.windows.storage.IStorageFile) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.devices.geolocation.Geopoint]:
        ...
    def set_geotag_async(file: winsdk.windows.storage.IStorageFile, geopoint: winsdk.windows.devices.geolocation.Geopoint) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def set_geotag_from_geolocator_async(file: winsdk.windows.storage.IStorageFile, geolocator: winsdk.windows.devices.geolocation.Geolocator) -> winsdk.windows.foundation.IAsyncAction:
        ...

class ImageProperties(IStorageItemExtraProperties, _winrt.Object):
    ...
    title: str
    rating: _winrt.UInt32
    date_taken: winsdk.windows.foundation.DateTime
    camera_model: str
    camera_manufacturer: str
    height: _winrt.UInt32
    keywords: winsdk.windows.foundation.collections.IVector[str]
    latitude: typing.Optional[_winrt.Double]
    longitude: typing.Optional[_winrt.Double]
    orientation: PhotoOrientation
    people_names: winsdk.windows.foundation.collections.IVectorView[str]
    width: _winrt.UInt32
    def retrieve_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]:
        ...
    def save_properties_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_properties_async(properties_to_save: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

class MusicProperties(IStorageItemExtraProperties, _winrt.Object):
    ...
    year: _winrt.UInt32
    track_number: _winrt.UInt32
    title: str
    subtitle: str
    rating: _winrt.UInt32
    publisher: str
    artist: str
    album_artist: str
    album: str
    bitrate: _winrt.UInt32
    composers: winsdk.windows.foundation.collections.IVector[str]
    conductors: winsdk.windows.foundation.collections.IVector[str]
    duration: winsdk.windows.foundation.TimeSpan
    genre: winsdk.windows.foundation.collections.IVector[str]
    producers: winsdk.windows.foundation.collections.IVector[str]
    writers: winsdk.windows.foundation.collections.IVector[str]
    def retrieve_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]:
        ...
    def save_properties_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_properties_async(properties_to_save: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

class StorageItemContentProperties(IStorageItemExtraProperties, _winrt.Object):
    ...
    def get_document_properties_async() -> winsdk.windows.foundation.IAsyncOperation[DocumentProperties]:
        ...
    def get_image_properties_async() -> winsdk.windows.foundation.IAsyncOperation[ImageProperties]:
        ...
    def get_music_properties_async() -> winsdk.windows.foundation.IAsyncOperation[MusicProperties]:
        ...
    def get_video_properties_async() -> winsdk.windows.foundation.IAsyncOperation[VideoProperties]:
        ...
    def retrieve_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]:
        ...
    def save_properties_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_properties_async(properties_to_save: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

class StorageItemThumbnail(winsdk.windows.storage.streams.IRandomAccessStreamWithContentType, winsdk.windows.storage.streams.IContentTypeProvider, winsdk.windows.storage.streams.IRandomAccessStream, winsdk.windows.storage.streams.IOutputStream, winsdk.windows.foundation.IClosable, winsdk.windows.storage.streams.IInputStream, _winrt.Object):
    ...
    original_height: _winrt.UInt32
    original_width: _winrt.UInt32
    returned_smaller_cached_size: _winrt.Boolean
    type: ThumbnailType
    content_type: str
    size: _winrt.UInt64
    can_read: _winrt.Boolean
    can_write: _winrt.Boolean
    position: _winrt.UInt64
    def clone_stream() -> winsdk.windows.storage.streams.IRandomAccessStream:
        ...
    def close() -> None:
        ...
    def flush_async() -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def get_input_stream_at(position: _winrt.UInt64) -> winsdk.windows.storage.streams.IInputStream:
        ...
    def get_output_stream_at(position: _winrt.UInt64) -> winsdk.windows.storage.streams.IOutputStream:
        ...
    def read_async(buffer: winsdk.windows.storage.streams.IBuffer, count: _winrt.UInt32, options: winsdk.windows.storage.streams.InputStreamOptions) -> winsdk.windows.foundation.IAsyncOperationWithProgress[winsdk.windows.storage.streams.IBuffer, _winrt.UInt32]:
        ...
    def seek(position: _winrt.UInt64) -> None:
        ...
    def write_async(buffer: winsdk.windows.storage.streams.IBuffer) -> winsdk.windows.foundation.IAsyncOperationWithProgress[_winrt.UInt32, _winrt.UInt32]:
        ...

class VideoProperties(IStorageItemExtraProperties, _winrt.Object):
    ...
    year: _winrt.UInt32
    title: str
    subtitle: str
    rating: _winrt.UInt32
    publisher: str
    bitrate: _winrt.UInt32
    directors: winsdk.windows.foundation.collections.IVector[str]
    duration: winsdk.windows.foundation.TimeSpan
    height: _winrt.UInt32
    keywords: winsdk.windows.foundation.collections.IVector[str]
    latitude: typing.Optional[_winrt.Double]
    longitude: typing.Optional[_winrt.Double]
    orientation: VideoOrientation
    producers: winsdk.windows.foundation.collections.IVector[str]
    width: _winrt.UInt32
    writers: winsdk.windows.foundation.collections.IVector[str]
    def retrieve_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]:
        ...
    def save_properties_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_properties_async(properties_to_save: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

class IStorageItemExtraProperties(_winrt.Object):
    ...
    def retrieve_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IMap[str, _winrt.Object]]:
        ...
    def save_properties_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_properties_async(properties_to_save: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

