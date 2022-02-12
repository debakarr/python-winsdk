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
    import winsdk.windows.media
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class GlobalSystemMediaTransportControlsSessionPlaybackStatus(enum.IntEnum):
    CLOSED = 0
    OPENED = 1
    CHANGING = 2
    STOPPED = 3
    PLAYING = 4
    PAUSED = 5

class CurrentSessionChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> CurrentSessionChangedEventArgs: ...

class GlobalSystemMediaTransportControlsSession(_winrt.Object):
    source_app_user_model_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalSystemMediaTransportControlsSession: ...
    @typing.overload
    def get_playback_info(self) -> GlobalSystemMediaTransportControlsSessionPlaybackInfo: ...
    @typing.overload
    def get_timeline_properties(self) -> GlobalSystemMediaTransportControlsSessionTimelineProperties: ...
    @typing.overload
    def try_change_auto_repeat_mode_async(self, requested_auto_repeat_mode: winsdk.windows.media.MediaPlaybackAutoRepeatMode) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_change_channel_down_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_change_channel_up_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_change_playback_position_async(self, requested_playback_position: _winrt.Int64) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_change_playback_rate_async(self, requested_playback_rate: _winrt.Double) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_change_shuffle_active_async(self, requested_shuffle_state: _winrt.Boolean) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_fast_forward_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_get_media_properties_async(self) -> winsdk.windows.foundation.IAsyncOperation[GlobalSystemMediaTransportControlsSessionMediaProperties]: ...
    @typing.overload
    def try_pause_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_play_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_record_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_rewind_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_skip_next_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_skip_previous_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_stop_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_toggle_play_pause_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def add_media_properties_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSession, MediaPropertiesChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_media_properties_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_playback_info_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSession, PlaybackInfoChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_playback_info_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_timeline_properties_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSession, TimelinePropertiesChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_timeline_properties_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GlobalSystemMediaTransportControlsSessionManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalSystemMediaTransportControlsSessionManager: ...
    @typing.overload
    def get_current_session(self) -> GlobalSystemMediaTransportControlsSession: ...
    @typing.overload
    def get_sessions(self) -> winsdk.windows.foundation.collections.IVectorView[GlobalSystemMediaTransportControlsSession]: ...
    @typing.overload
    @staticmethod
    def request_async() -> winsdk.windows.foundation.IAsyncOperation[GlobalSystemMediaTransportControlsSessionManager]: ...
    @typing.overload
    def add_current_session_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSessionManager, CurrentSessionChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_current_session_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_sessions_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GlobalSystemMediaTransportControlsSessionManager, SessionsChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_sessions_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GlobalSystemMediaTransportControlsSessionMediaProperties(_winrt.Object):
    album_artist: str
    album_title: str
    album_track_count: _winrt.Int32
    artist: str
    genres: winsdk.windows.foundation.collections.IVectorView[str]
    playback_type: typing.Optional[winsdk.windows.media.MediaPlaybackType]
    subtitle: str
    thumbnail: winsdk.windows.storage.streams.IRandomAccessStreamReference
    title: str
    track_number: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalSystemMediaTransportControlsSessionMediaProperties: ...

class GlobalSystemMediaTransportControlsSessionPlaybackControls(_winrt.Object):
    is_channel_down_enabled: _winrt.Boolean
    is_channel_up_enabled: _winrt.Boolean
    is_fast_forward_enabled: _winrt.Boolean
    is_next_enabled: _winrt.Boolean
    is_pause_enabled: _winrt.Boolean
    is_play_enabled: _winrt.Boolean
    is_play_pause_toggle_enabled: _winrt.Boolean
    is_playback_position_enabled: _winrt.Boolean
    is_playback_rate_enabled: _winrt.Boolean
    is_previous_enabled: _winrt.Boolean
    is_record_enabled: _winrt.Boolean
    is_repeat_enabled: _winrt.Boolean
    is_rewind_enabled: _winrt.Boolean
    is_shuffle_enabled: _winrt.Boolean
    is_stop_enabled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalSystemMediaTransportControlsSessionPlaybackControls: ...

class GlobalSystemMediaTransportControlsSessionPlaybackInfo(_winrt.Object):
    auto_repeat_mode: typing.Optional[winsdk.windows.media.MediaPlaybackAutoRepeatMode]
    controls: GlobalSystemMediaTransportControlsSessionPlaybackControls
    is_shuffle_active: typing.Optional[_winrt.Boolean]
    playback_rate: typing.Optional[_winrt.Double]
    playback_status: GlobalSystemMediaTransportControlsSessionPlaybackStatus
    playback_type: typing.Optional[winsdk.windows.media.MediaPlaybackType]
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalSystemMediaTransportControlsSessionPlaybackInfo: ...

class GlobalSystemMediaTransportControlsSessionTimelineProperties(_winrt.Object):
    end_time: winsdk.windows.foundation.TimeSpan
    last_updated_time: winsdk.windows.foundation.DateTime
    max_seek_time: winsdk.windows.foundation.TimeSpan
    min_seek_time: winsdk.windows.foundation.TimeSpan
    position: winsdk.windows.foundation.TimeSpan
    start_time: winsdk.windows.foundation.TimeSpan
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalSystemMediaTransportControlsSessionTimelineProperties: ...

class MediaPropertiesChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> MediaPropertiesChangedEventArgs: ...

class PlaybackInfoChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> PlaybackInfoChangedEventArgs: ...

class SessionsChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SessionsChangedEventArgs: ...

class TimelinePropertiesChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> TimelinePropertiesChangedEventArgs: ...

