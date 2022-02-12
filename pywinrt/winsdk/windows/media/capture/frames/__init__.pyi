# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.enumeration
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
    import winsdk.windows.graphics.directx.direct3d11
except Exception:
    pass

try:
    import winsdk.windows.graphics.imaging
except Exception:
    pass

try:
    import winsdk.windows.media
except Exception:
    pass

try:
    import winsdk.windows.media.capture
except Exception:
    pass

try:
    import winsdk.windows.media.devices
except Exception:
    pass

try:
    import winsdk.windows.media.devices.core
except Exception:
    pass

try:
    import winsdk.windows.media.mediaproperties
except Exception:
    pass

try:
    import winsdk.windows.perception.spatial
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.ui.windowmanagement
except Exception:
    pass

class MediaFrameReaderAcquisitionMode(enum.IntEnum):
    REALTIME = 0
    BUFFERED = 1

class MediaFrameReaderStartStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_FAILURE = 1
    DEVICE_NOT_AVAILABLE = 2
    OUTPUT_FORMAT_NOT_SUPPORTED = 3
    EXCLUSIVE_CONTROL_NOT_AVAILABLE = 4

class MediaFrameSourceGetPropertyStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_FAILURE = 1
    NOT_SUPPORTED = 2
    DEVICE_NOT_AVAILABLE = 3
    MAX_PROPERTY_VALUE_SIZE_TOO_SMALL = 4
    MAX_PROPERTY_VALUE_SIZE_REQUIRED = 5

class MediaFrameSourceKind(enum.IntEnum):
    CUSTOM = 0
    COLOR = 1
    INFRARED = 2
    DEPTH = 3
    AUDIO = 4
    IMAGE = 5
    METADATA = 6

class MediaFrameSourceSetPropertyStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_FAILURE = 1
    NOT_SUPPORTED = 2
    INVALID_VALUE = 3
    DEVICE_NOT_AVAILABLE = 4
    NOT_IN_CONTROL = 5

class MultiSourceMediaFrameReaderStartStatus(enum.IntEnum):
    SUCCESS = 0
    NOT_SUPPORTED = 1
    INSUFFICIENT_RESOURCES = 2
    DEVICE_NOT_AVAILABLE = 3
    UNKNOWN_FAILURE = 4

class AudioMediaFrame(_winrt.Object):
    audio_encoding_properties: winsdk.windows.media.mediaproperties.AudioEncodingProperties
    frame_reference: MediaFrameReference
    @staticmethod
    def _from(obj: _winrt.Object) -> AudioMediaFrame: ...
    @typing.overload
    def get_audio_frame(self) -> winsdk.windows.media.AudioFrame: ...

class BufferMediaFrame(_winrt.Object):
    buffer: winsdk.windows.storage.streams.IBuffer
    frame_reference: MediaFrameReference
    @staticmethod
    def _from(obj: _winrt.Object) -> BufferMediaFrame: ...

class DepthMediaFrame(_winrt.Object):
    depth_format: DepthMediaFrameFormat
    frame_reference: MediaFrameReference
    video_media_frame: VideoMediaFrame
    max_reliable_depth: _winrt.UInt32
    min_reliable_depth: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> DepthMediaFrame: ...
    @typing.overload
    def try_create_coordinate_mapper(self, camera_intrinsics: winsdk.windows.media.devices.core.CameraIntrinsics, coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem) -> winsdk.windows.media.devices.core.DepthCorrelatedCoordinateMapper: ...

class DepthMediaFrameFormat(_winrt.Object):
    depth_scale_in_meters: _winrt.Double
    video_format: VideoMediaFrameFormat
    @staticmethod
    def _from(obj: _winrt.Object) -> DepthMediaFrameFormat: ...

class InfraredMediaFrame(_winrt.Object):
    frame_reference: MediaFrameReference
    is_illuminated: _winrt.Boolean
    video_media_frame: VideoMediaFrame
    @staticmethod
    def _from(obj: _winrt.Object) -> InfraredMediaFrame: ...

class MediaFrameArrivedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameArrivedEventArgs: ...

class MediaFrameFormat(_winrt.Object):
    frame_rate: winsdk.windows.media.mediaproperties.MediaRatio
    major_type: str
    properties: winsdk.windows.foundation.collections.IMapView[uuid.UUID, _winrt.Object]
    subtype: str
    video_format: VideoMediaFrameFormat
    audio_encoding_properties: winsdk.windows.media.mediaproperties.AudioEncodingProperties
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameFormat: ...

class MediaFrameReader(winsdk.windows.foundation.IClosable, _winrt.Object):
    acquisition_mode: MediaFrameReaderAcquisitionMode
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameReader: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    def start_async(self) -> winsdk.windows.foundation.IAsyncOperation[MediaFrameReaderStartStatus]: ...
    @typing.overload
    def stop_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def try_acquire_latest_frame(self) -> MediaFrameReference: ...
    @typing.overload
    def add_frame_arrived(self, handler: winsdk.windows.foundation.TypedEventHandler[MediaFrameReader, MediaFrameArrivedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_frame_arrived(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class MediaFrameReference(winsdk.windows.foundation.IClosable, _winrt.Object):
    buffer_media_frame: BufferMediaFrame
    coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem
    duration: winsdk.windows.foundation.TimeSpan
    format: MediaFrameFormat
    properties: winsdk.windows.foundation.collections.IMapView[uuid.UUID, _winrt.Object]
    source_kind: MediaFrameSourceKind
    system_relative_time: typing.Optional[winsdk.windows.foundation.TimeSpan]
    video_media_frame: VideoMediaFrame
    audio_media_frame: AudioMediaFrame
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameReference: ...
    @typing.overload
    def close(self) -> None: ...

class MediaFrameSource(_winrt.Object):
    controller: MediaFrameSourceController
    current_format: MediaFrameFormat
    info: MediaFrameSourceInfo
    supported_formats: winsdk.windows.foundation.collections.IVectorView[MediaFrameFormat]
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameSource: ...
    @typing.overload
    def set_format_async(self, format: MediaFrameFormat) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def try_get_camera_intrinsics(self, format: MediaFrameFormat) -> winsdk.windows.media.devices.core.CameraIntrinsics: ...
    @typing.overload
    def add_format_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[MediaFrameSource, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_format_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class MediaFrameSourceController(_winrt.Object):
    video_device_controller: winsdk.windows.media.devices.VideoDeviceController
    audio_device_controller: winsdk.windows.media.devices.AudioDeviceController
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameSourceController: ...
    @typing.overload
    def get_property_async(self, property_id: str) -> winsdk.windows.foundation.IAsyncOperation[MediaFrameSourceGetPropertyResult]: ...
    @typing.overload
    def get_property_by_extended_id_async(self, extended_property_id: typing.Sequence[_winrt.UInt8], max_property_value_size: typing.Optional[_winrt.UInt32]) -> winsdk.windows.foundation.IAsyncOperation[MediaFrameSourceGetPropertyResult]: ...
    @typing.overload
    def set_property_async(self, property_id: str, property_value: _winrt.Object) -> winsdk.windows.foundation.IAsyncOperation[MediaFrameSourceSetPropertyStatus]: ...
    @typing.overload
    def set_property_by_extended_id_async(self, extended_property_id: typing.Sequence[_winrt.UInt8], property_value: typing.Sequence[_winrt.UInt8]) -> winsdk.windows.foundation.IAsyncOperation[MediaFrameSourceSetPropertyStatus]: ...

class MediaFrameSourceGetPropertyResult(_winrt.Object):
    status: MediaFrameSourceGetPropertyStatus
    value: _winrt.Object
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameSourceGetPropertyResult: ...

class MediaFrameSourceGroup(_winrt.Object):
    display_name: str
    id: str
    source_infos: winsdk.windows.foundation.collections.IVectorView[MediaFrameSourceInfo]
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameSourceGroup: ...
    @typing.overload
    @staticmethod
    def find_all_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[MediaFrameSourceGroup]]: ...
    @typing.overload
    @staticmethod
    def from_id_async(id: str) -> winsdk.windows.foundation.IAsyncOperation[MediaFrameSourceGroup]: ...
    @typing.overload
    @staticmethod
    def get_device_selector() -> str: ...

class MediaFrameSourceInfo(_winrt.Object):
    coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem
    device_information: winsdk.windows.devices.enumeration.DeviceInformation
    id: str
    media_stream_type: winsdk.windows.media.capture.MediaStreamType
    properties: winsdk.windows.foundation.collections.IMapView[uuid.UUID, _winrt.Object]
    source_group: MediaFrameSourceGroup
    source_kind: MediaFrameSourceKind
    profile_id: str
    video_profile_media_description: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.media.capture.MediaCaptureVideoProfileMediaDescription]
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaFrameSourceInfo: ...
    @typing.overload
    def get_relative_panel(self, display_region: winsdk.windows.ui.windowmanagement.DisplayRegion) -> winsdk.windows.devices.enumeration.Panel: ...

class MultiSourceMediaFrameArrivedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> MultiSourceMediaFrameArrivedEventArgs: ...

class MultiSourceMediaFrameReader(winsdk.windows.foundation.IClosable, _winrt.Object):
    acquisition_mode: MediaFrameReaderAcquisitionMode
    @staticmethod
    def _from(obj: _winrt.Object) -> MultiSourceMediaFrameReader: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    def start_async(self) -> winsdk.windows.foundation.IAsyncOperation[MultiSourceMediaFrameReaderStartStatus]: ...
    @typing.overload
    def stop_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def try_acquire_latest_frame(self) -> MultiSourceMediaFrameReference: ...
    @typing.overload
    def add_frame_arrived(self, handler: winsdk.windows.foundation.TypedEventHandler[MultiSourceMediaFrameReader, MultiSourceMediaFrameArrivedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_frame_arrived(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class MultiSourceMediaFrameReference(winsdk.windows.foundation.IClosable, _winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> MultiSourceMediaFrameReference: ...
    @typing.overload
    def close(self) -> None: ...
    @typing.overload
    def try_get_frame_reference_by_source_id(self, source_id: str) -> MediaFrameReference: ...

class VideoMediaFrame(_winrt.Object):
    camera_intrinsics: winsdk.windows.media.devices.core.CameraIntrinsics
    depth_media_frame: DepthMediaFrame
    direct3_d_surface: winsdk.windows.graphics.directx.direct3d11.IDirect3DSurface
    frame_reference: MediaFrameReference
    infrared_media_frame: InfraredMediaFrame
    software_bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap
    video_format: VideoMediaFrameFormat
    @staticmethod
    def _from(obj: _winrt.Object) -> VideoMediaFrame: ...
    @typing.overload
    def get_video_frame(self) -> winsdk.windows.media.VideoFrame: ...

class VideoMediaFrameFormat(_winrt.Object):
    depth_format: DepthMediaFrameFormat
    height: _winrt.UInt32
    media_frame_format: MediaFrameFormat
    width: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> VideoMediaFrameFormat: ...

