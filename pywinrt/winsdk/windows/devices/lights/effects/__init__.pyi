# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.lights
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
    import winsdk.windows.graphics.imaging
except Exception:
    pass

try:
    import winsdk.windows.ui
except Exception:
    pass

class LampArrayEffectCompletionBehavior(enum.IntEnum):
    CLEAR_STATE = 0
    KEEP_STATE = 1

class LampArrayEffectStartMode(enum.IntEnum):
    SEQUENTIAL = 0
    SIMULTANEOUS = 1

class LampArrayRepetitionMode(enum.IntEnum):
    OCCURRENCES = 0
    FOREVER = 1

class LampArrayBitmapEffect(ILampArrayEffect, _winrt.Object):
    update_interval: winsdk.windows.foundation.TimeSpan
    start_delay: winsdk.windows.foundation.TimeSpan
    duration: winsdk.windows.foundation.TimeSpan
    suggested_bitmap_size: winsdk.windows.foundation.Size
    z_index: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArrayBitmapEffect: ...
    @typing.overload
    def __init__(self, lamp_array: winsdk.windows.devices.lights.LampArray, lamp_indexes: typing.Sequence[_winrt.Int32]) -> None: ...
    @typing.overload
    def add_bitmap_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[LampArrayBitmapEffect, LampArrayBitmapRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_bitmap_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class LampArrayBitmapRequestedEventArgs(_winrt.Object):
    since_started: winsdk.windows.foundation.TimeSpan
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArrayBitmapRequestedEventArgs: ...
    @typing.overload
    def update_bitmap(self, bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap) -> None: ...

class LampArrayBlinkEffect(ILampArrayEffect, _winrt.Object):
    sustain_duration: winsdk.windows.foundation.TimeSpan
    start_delay: winsdk.windows.foundation.TimeSpan
    repetition_mode: LampArrayRepetitionMode
    repetition_delay: winsdk.windows.foundation.TimeSpan
    occurrences: _winrt.Int32
    decay_duration: winsdk.windows.foundation.TimeSpan
    color: winsdk.windows.ui.Color
    attack_duration: winsdk.windows.foundation.TimeSpan
    z_index: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArrayBlinkEffect: ...
    @typing.overload
    def __init__(self, lamp_array: winsdk.windows.devices.lights.LampArray, lamp_indexes: typing.Sequence[_winrt.Int32]) -> None: ...

class LampArrayColorRampEffect(ILampArrayEffect, _winrt.Object):
    start_delay: winsdk.windows.foundation.TimeSpan
    ramp_duration: winsdk.windows.foundation.TimeSpan
    completion_behavior: LampArrayEffectCompletionBehavior
    color: winsdk.windows.ui.Color
    z_index: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArrayColorRampEffect: ...
    @typing.overload
    def __init__(self, lamp_array: winsdk.windows.devices.lights.LampArray, lamp_indexes: typing.Sequence[_winrt.Int32]) -> None: ...

class LampArrayCustomEffect(ILampArrayEffect, _winrt.Object):
    update_interval: winsdk.windows.foundation.TimeSpan
    duration: winsdk.windows.foundation.TimeSpan
    z_index: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArrayCustomEffect: ...
    @typing.overload
    def __init__(self, lamp_array: winsdk.windows.devices.lights.LampArray, lamp_indexes: typing.Sequence[_winrt.Int32]) -> None: ...
    @typing.overload
    def add_update_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[LampArrayCustomEffect, LampArrayUpdateRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_update_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class LampArrayEffectPlaylist(winsdk.windows.foundation.collections.IVectorView[ILampArrayEffect], winsdk.windows.foundation.collections.IIterable[ILampArrayEffect], _winrt.Object):
    repetition_mode: LampArrayRepetitionMode
    occurrences: _winrt.Int32
    effect_start_mode: LampArrayEffectStartMode
    size: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArrayEffectPlaylist: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def append(self, effect: ILampArrayEffect) -> None: ...
    @typing.overload
    def first(self) -> winsdk.windows.foundation.collections.IIterator[ILampArrayEffect]: ...
    @typing.overload
    def get_at(self, index: _winrt.UInt32) -> ILampArrayEffect: ...
    @typing.overload
    def get_many(self, start_index: _winrt.UInt32, items_size: _winrt.UInt32) -> typing.Tuple[_winrt.UInt32, typing.List[ILampArrayEffect]]: ...
    @typing.overload
    def index_of(self, value: ILampArrayEffect) -> typing.Tuple[_winrt.Boolean, _winrt.UInt32]: ...
    @typing.overload
    def override_z_index(self, z_index: _winrt.Int32) -> None: ...
    @typing.overload
    def pause(self) -> None: ...
    @typing.overload
    @staticmethod
    def pause_all(value: typing.Iterable[LampArrayEffectPlaylist]) -> None: ...
    @typing.overload
    def start(self) -> None: ...
    @typing.overload
    @staticmethod
    def start_all(value: typing.Iterable[LampArrayEffectPlaylist]) -> None: ...
    @typing.overload
    def stop(self) -> None: ...
    @typing.overload
    @staticmethod
    def stop_all(value: typing.Iterable[LampArrayEffectPlaylist]) -> None: ...

class LampArraySolidEffect(ILampArrayEffect, _winrt.Object):
    z_index: _winrt.Int32
    start_delay: winsdk.windows.foundation.TimeSpan
    duration: winsdk.windows.foundation.TimeSpan
    completion_behavior: LampArrayEffectCompletionBehavior
    color: winsdk.windows.ui.Color
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArraySolidEffect: ...
    @typing.overload
    def __init__(self, lamp_array: winsdk.windows.devices.lights.LampArray, lamp_indexes: typing.Sequence[_winrt.Int32]) -> None: ...

class LampArrayUpdateRequestedEventArgs(_winrt.Object):
    since_started: winsdk.windows.foundation.TimeSpan
    @staticmethod
    def _from(obj: _winrt.Object) -> LampArrayUpdateRequestedEventArgs: ...
    @typing.overload
    def set_color(self, desired_color: winsdk.windows.ui.Color) -> None: ...
    @typing.overload
    def set_color_for_index(self, lamp_index: _winrt.Int32, desired_color: winsdk.windows.ui.Color) -> None: ...
    @typing.overload
    def set_colors_for_indices(self, desired_colors: typing.Sequence[winsdk.windows.ui.Color], lamp_indexes: typing.Sequence[_winrt.Int32]) -> None: ...
    @typing.overload
    def set_single_color_for_indices(self, desired_color: winsdk.windows.ui.Color, lamp_indexes: typing.Sequence[_winrt.Int32]) -> None: ...

class ILampArrayEffect(_winrt.Object):
    z_index: _winrt.Int32
    @staticmethod
    def _from(obj: _winrt.Object) -> ILampArrayEffect: ...

