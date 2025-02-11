# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Media.Control")

try:
    import winsdk.windows.foundation
except ImportError:
    pass

try:
    import winsdk.windows.foundation.collections
except ImportError:
    pass

try:
    import winsdk.windows.media
except ImportError:
    pass

try:
    import winsdk.windows.storage.streams
except ImportError:
    pass

class GlobalSystemMediaTransportControlsSessionPlaybackStatus(enum.IntEnum):
    CLOSED = 0
    OPENED = 1
    CHANGING = 2
    STOPPED = 3
    PLAYING = 4
    PAUSED = 5

_ns_module._register_GlobalSystemMediaTransportControlsSessionPlaybackStatus(GlobalSystemMediaTransportControlsSessionPlaybackStatus)

CurrentSessionChangedEventArgs = _ns_module.CurrentSessionChangedEventArgs
GlobalSystemMediaTransportControlsSession = _ns_module.GlobalSystemMediaTransportControlsSession
GlobalSystemMediaTransportControlsSessionManager = _ns_module.GlobalSystemMediaTransportControlsSessionManager
GlobalSystemMediaTransportControlsSessionMediaProperties = _ns_module.GlobalSystemMediaTransportControlsSessionMediaProperties
GlobalSystemMediaTransportControlsSessionPlaybackControls = _ns_module.GlobalSystemMediaTransportControlsSessionPlaybackControls
GlobalSystemMediaTransportControlsSessionPlaybackInfo = _ns_module.GlobalSystemMediaTransportControlsSessionPlaybackInfo
GlobalSystemMediaTransportControlsSessionTimelineProperties = _ns_module.GlobalSystemMediaTransportControlsSessionTimelineProperties
MediaPropertiesChangedEventArgs = _ns_module.MediaPropertiesChangedEventArgs
PlaybackInfoChangedEventArgs = _ns_module.PlaybackInfoChangedEventArgs
SessionsChangedEventArgs = _ns_module.SessionsChangedEventArgs
TimelinePropertiesChangedEventArgs = _ns_module.TimelinePropertiesChangedEventArgs
