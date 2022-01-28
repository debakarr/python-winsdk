# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.appservice
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
    import winsdk.windows.graphics.directx
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
    import winsdk.windows.storage
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class AudioBufferAccessMode(enum.IntEnum):
    READ = 0
    READ_WRITE = 1
    WRITE = 2

class AudioProcessing(enum.IntEnum):
    DEFAULT = 0
    RAW = 1

class MediaPlaybackAutoRepeatMode(enum.IntEnum):
    NONE = 0
    TRACK = 1
    LIST = 2

class MediaPlaybackStatus(enum.IntEnum):
    CLOSED = 0
    CHANGING = 1
    STOPPED = 2
    PLAYING = 3
    PAUSED = 4

class MediaPlaybackType(enum.IntEnum):
    UNKNOWN = 0
    MUSIC = 1
    VIDEO = 2
    IMAGE = 3

class MediaTimelineControllerState(enum.IntEnum):
    PAUSED = 0
    RUNNING = 1
    STALLED = 2
    ERROR = 3

class SoundLevel(enum.IntEnum):
    MUTED = 0
    LOW = 1
    FULL = 2

class SystemMediaTransportControlsButton(enum.IntEnum):
    PLAY = 0
    PAUSE = 1
    STOP = 2
    RECORD = 3
    FAST_FORWARD = 4
    REWIND = 5
    NEXT = 6
    PREVIOUS = 7
    CHANNEL_UP = 8
    CHANNEL_DOWN = 9

class SystemMediaTransportControlsProperty(enum.IntEnum):
    SOUND_LEVEL = 0

class MediaTimeRange:
    start: winsdk.windows.foundation.TimeSpan
    end: winsdk.windows.foundation.TimeSpan
    def __init__(self, start: winsdk.windows.foundation.TimeSpan, end: winsdk.windows.foundation.TimeSpan) -> None: ...

class AudioBuffer(winsdk.windows.foundation.IMemoryBuffer, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    length: _winrt.UInt32
    capacity: _winrt.UInt32
    def close() -> None:
        ...
    def create_reference() -> winsdk.windows.foundation.IMemoryBufferReference:
        ...

class AudioFrame(IMediaFrame, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    system_relative_time: typing.Optional[winsdk.windows.foundation.TimeSpan]
    relative_time: typing.Optional[winsdk.windows.foundation.TimeSpan]
    is_discontinuous: _winrt.Boolean
    duration: typing.Optional[winsdk.windows.foundation.TimeSpan]
    extended_properties: winsdk.windows.foundation.collections.IPropertySet
    is_read_only: _winrt.Boolean
    type: str
    def __init__(self, capacity: _winrt.UInt32) -> None:
        ...
    def close() -> None:
        ...
    def lock_buffer(mode: AudioBufferAccessMode) -> AudioBuffer:
        ...

class AutoRepeatModeChangeRequestedEventArgs(_winrt.Object):
    ...
    requested_auto_repeat_mode: MediaPlaybackAutoRepeatMode

class ImageDisplayProperties(_winrt.Object):
    ...
    title: str
    subtitle: str

class MediaExtensionManager(_winrt.Object):
    ...
    def __init__(self, ) -> None:
        ...
    def register_audio_decoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID) -> None:
        ...
    def register_audio_decoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID, configuration: winsdk.windows.foundation.collections.IPropertySet) -> None:
        ...
    def register_audio_encoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID) -> None:
        ...
    def register_audio_encoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID, configuration: winsdk.windows.foundation.collections.IPropertySet) -> None:
        ...
    def register_byte_stream_handler(activatable_class_id: str, file_extension: str, mime_type: str) -> None:
        ...
    def register_byte_stream_handler(activatable_class_id: str, file_extension: str, mime_type: str, configuration: winsdk.windows.foundation.collections.IPropertySet) -> None:
        ...
    def register_media_extension_for_app_service(extension: IMediaExtension, connection: winsdk.windows.applicationmodel.appservice.AppServiceConnection) -> None:
        ...
    def register_scheme_handler(activatable_class_id: str, scheme: str) -> None:
        ...
    def register_scheme_handler(activatable_class_id: str, scheme: str, configuration: winsdk.windows.foundation.collections.IPropertySet) -> None:
        ...
    def register_video_decoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID) -> None:
        ...
    def register_video_decoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID, configuration: winsdk.windows.foundation.collections.IPropertySet) -> None:
        ...
    def register_video_encoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID) -> None:
        ...
    def register_video_encoder(activatable_class_id: str, input_subtype: uuid.UUID, output_subtype: uuid.UUID, configuration: winsdk.windows.foundation.collections.IPropertySet) -> None:
        ...

class MediaMarkerTypes(_winrt.Object):
    ...
    bookmark: str

class MediaProcessingTriggerDetails(_winrt.Object):
    ...
    arguments: winsdk.windows.foundation.collections.ValueSet

class MediaTimelineController(_winrt.Object):
    ...
    position: winsdk.windows.foundation.TimeSpan
    clock_rate: _winrt.Double
    state: MediaTimelineControllerState
    is_looping_enabled: _winrt.Boolean
    duration: typing.Optional[winsdk.windows.foundation.TimeSpan]
    def __init__(self, ) -> None:
        ...
    def pause() -> None:
        ...
    def resume() -> None:
        ...
    def start() -> None:
        ...
    def add_position_changed(position_changed_event_handler: winsdk.windows.foundation.TypedEventHandler[MediaTimelineController, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_position_changed(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_state_changed(state_changed_event_handler: winsdk.windows.foundation.TypedEventHandler[MediaTimelineController, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_state_changed(event_cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_ended(event_handler: winsdk.windows.foundation.TypedEventHandler[MediaTimelineController, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_ended(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_failed(event_handler: winsdk.windows.foundation.TypedEventHandler[MediaTimelineController, MediaTimelineControllerFailedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_failed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class MediaTimelineControllerFailedEventArgs(_winrt.Object):
    ...
    extended_error: winsdk.windows.foundation.HResult

class MusicDisplayProperties(_winrt.Object):
    ...
    title: str
    artist: str
    album_artist: str
    track_number: _winrt.UInt32
    album_title: str
    genres: winsdk.windows.foundation.collections.IVector[str]
    album_track_count: _winrt.UInt32

class PlaybackPositionChangeRequestedEventArgs(_winrt.Object):
    ...
    requested_playback_position: winsdk.windows.foundation.TimeSpan

class PlaybackRateChangeRequestedEventArgs(_winrt.Object):
    ...
    requested_playback_rate: _winrt.Double

class ShuffleEnabledChangeRequestedEventArgs(_winrt.Object):
    ...
    requested_shuffle_enabled: _winrt.Boolean

class SystemMediaTransportControls(_winrt.Object):
    ...
    is_play_enabled: _winrt.Boolean
    is_pause_enabled: _winrt.Boolean
    is_next_enabled: _winrt.Boolean
    is_previous_enabled: _winrt.Boolean
    is_enabled: _winrt.Boolean
    is_channel_down_enabled: _winrt.Boolean
    is_fast_forward_enabled: _winrt.Boolean
    is_channel_up_enabled: _winrt.Boolean
    playback_status: MediaPlaybackStatus
    is_stop_enabled: _winrt.Boolean
    is_rewind_enabled: _winrt.Boolean
    is_record_enabled: _winrt.Boolean
    display_updater: SystemMediaTransportControlsDisplayUpdater
    sound_level: SoundLevel
    shuffle_enabled: _winrt.Boolean
    playback_rate: _winrt.Double
    auto_repeat_mode: MediaPlaybackAutoRepeatMode
    def get_for_current_view() -> SystemMediaTransportControls:
        ...
    def update_timeline_properties(timeline_properties: SystemMediaTransportControlsTimelineProperties) -> None:
        ...
    def add_button_pressed(handler: winsdk.windows.foundation.TypedEventHandler[SystemMediaTransportControls, SystemMediaTransportControlsButtonPressedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_button_pressed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_property_changed(handler: winsdk.windows.foundation.TypedEventHandler[SystemMediaTransportControls, SystemMediaTransportControlsPropertyChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_property_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_auto_repeat_mode_change_requested(handler: winsdk.windows.foundation.TypedEventHandler[SystemMediaTransportControls, AutoRepeatModeChangeRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_auto_repeat_mode_change_requested(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_playback_position_change_requested(handler: winsdk.windows.foundation.TypedEventHandler[SystemMediaTransportControls, PlaybackPositionChangeRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_playback_position_change_requested(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_playback_rate_change_requested(handler: winsdk.windows.foundation.TypedEventHandler[SystemMediaTransportControls, PlaybackRateChangeRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_playback_rate_change_requested(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_shuffle_enabled_change_requested(handler: winsdk.windows.foundation.TypedEventHandler[SystemMediaTransportControls, ShuffleEnabledChangeRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_shuffle_enabled_change_requested(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class SystemMediaTransportControlsButtonPressedEventArgs(_winrt.Object):
    ...
    button: SystemMediaTransportControlsButton

class SystemMediaTransportControlsDisplayUpdater(_winrt.Object):
    ...
    type: MediaPlaybackType
    thumbnail: winsdk.windows.storage.streams.RandomAccessStreamReference
    app_media_id: str
    image_properties: ImageDisplayProperties
    music_properties: MusicDisplayProperties
    video_properties: VideoDisplayProperties
    def clear_all() -> None:
        ...
    def copy_from_file_async(type: MediaPlaybackType, source: winsdk.windows.storage.StorageFile) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def update() -> None:
        ...

class SystemMediaTransportControlsPropertyChangedEventArgs(_winrt.Object):
    ...
    property: SystemMediaTransportControlsProperty

class SystemMediaTransportControlsTimelineProperties(_winrt.Object):
    ...
    start_time: winsdk.windows.foundation.TimeSpan
    position: winsdk.windows.foundation.TimeSpan
    min_seek_time: winsdk.windows.foundation.TimeSpan
    max_seek_time: winsdk.windows.foundation.TimeSpan
    end_time: winsdk.windows.foundation.TimeSpan
    def __init__(self, ) -> None:
        ...

class VideoDisplayProperties(_winrt.Object):
    ...
    title: str
    subtitle: str
    genres: winsdk.windows.foundation.collections.IVector[str]

class VideoEffects(_winrt.Object):
    ...
    video_stabilization: str

class VideoFrame(IMediaFrame, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    system_relative_time: typing.Optional[winsdk.windows.foundation.TimeSpan]
    relative_time: typing.Optional[winsdk.windows.foundation.TimeSpan]
    is_discontinuous: _winrt.Boolean
    duration: typing.Optional[winsdk.windows.foundation.TimeSpan]
    extended_properties: winsdk.windows.foundation.collections.IPropertySet
    is_read_only: _winrt.Boolean
    type: str
    direct3_d_surface: winsdk.windows.graphics.directx.direct3d11.IDirect3DSurface
    software_bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap
    def __init__(self, format: winsdk.windows.graphics.imaging.BitmapPixelFormat, width: _winrt.Int32, height: _winrt.Int32) -> None:
        ...
    def __init__(self, format: winsdk.windows.graphics.imaging.BitmapPixelFormat, width: _winrt.Int32, height: _winrt.Int32, alpha: winsdk.windows.graphics.imaging.BitmapAlphaMode) -> None:
        ...
    def close() -> None:
        ...
    def copy_to_async(frame: VideoFrame) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def copy_to_async(frame: VideoFrame, source_bounds: typing.Optional[winsdk.windows.graphics.imaging.BitmapBounds], destination_bounds: typing.Optional[winsdk.windows.graphics.imaging.BitmapBounds]) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def create_as_direct3_d11_surface_backed(format: winsdk.windows.graphics.directx.DirectXPixelFormat, width: _winrt.Int32, height: _winrt.Int32) -> VideoFrame:
        ...
    def create_as_direct3_d11_surface_backed(format: winsdk.windows.graphics.directx.DirectXPixelFormat, width: _winrt.Int32, height: _winrt.Int32, device: winsdk.windows.graphics.directx.direct3d11.IDirect3DDevice) -> VideoFrame:
        ...
    def create_with_direct3_d11_surface(surface: winsdk.windows.graphics.directx.direct3d11.IDirect3DSurface) -> VideoFrame:
        ...
    def create_with_software_bitmap(bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap) -> VideoFrame:
        ...

class IMediaExtension(_winrt.Object):
    ...
    def set_properties(configuration: winsdk.windows.foundation.collections.IPropertySet) -> None:
        ...

class IMediaFrame(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    duration: typing.Optional[winsdk.windows.foundation.TimeSpan]
    extended_properties: winsdk.windows.foundation.collections.IPropertySet
    is_discontinuous: _winrt.Boolean
    is_read_only: _winrt.Boolean
    relative_time: typing.Optional[winsdk.windows.foundation.TimeSpan]
    system_relative_time: typing.Optional[winsdk.windows.foundation.TimeSpan]
    type: str
    def close() -> None:
        ...

class IMediaMarker(_winrt.Object):
    ...
    media_marker_type: str
    text: str
    time: winsdk.windows.foundation.TimeSpan

class IMediaMarkers(_winrt.Object):
    ...
    markers: winsdk.windows.foundation.collections.IVectorView[IMediaMarker]

