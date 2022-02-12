# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

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
    import winsdk.windows.media
except Exception:
    pass

class SoundLevelBroker(_winrt.Object):
    sound_level: winsdk.windows.media.SoundLevel
    @staticmethod
    def _from(obj: _winrt.Object) -> SoundLevelBroker: ...
    @typing.overload
    @staticmethod
    def add_sound_level_changed(handler: winsdk.windows.foundation.EventHandler[_winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    @staticmethod
    def remove_sound_level_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

