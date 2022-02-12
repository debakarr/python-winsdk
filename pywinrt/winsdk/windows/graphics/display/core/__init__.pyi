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

class HdmiDisplayColorSpace(enum.IntEnum):
    RGB_LIMITED = 0
    RGB_FULL = 1
    B_T2020 = 2
    B_T709 = 3

class HdmiDisplayHdrOption(enum.IntEnum):
    NONE = 0
    EOTF_SDR = 1
    EOTF2084 = 2
    DOLBY_VISION_LOW_LATENCY = 3

class HdmiDisplayPixelEncoding(enum.IntEnum):
    RGB444 = 0
    YCC444 = 1
    YCC422 = 2
    YCC420 = 3

class HdmiDisplayHdr2086Metadata:
    red_primary_x: _winrt.UInt16
    red_primary_y: _winrt.UInt16
    green_primary_x: _winrt.UInt16
    green_primary_y: _winrt.UInt16
    blue_primary_x: _winrt.UInt16
    blue_primary_y: _winrt.UInt16
    white_point_x: _winrt.UInt16
    white_point_y: _winrt.UInt16
    max_mastering_luminance: _winrt.UInt16
    min_mastering_luminance: _winrt.UInt16
    max_content_light_level: _winrt.UInt16
    max_frame_average_light_level: _winrt.UInt16
    def __init__(self, red_primary_x: _winrt.UInt16, red_primary_y: _winrt.UInt16, green_primary_x: _winrt.UInt16, green_primary_y: _winrt.UInt16, blue_primary_x: _winrt.UInt16, blue_primary_y: _winrt.UInt16, white_point_x: _winrt.UInt16, white_point_y: _winrt.UInt16, max_mastering_luminance: _winrt.UInt16, min_mastering_luminance: _winrt.UInt16, max_content_light_level: _winrt.UInt16, max_frame_average_light_level: _winrt.UInt16) -> None: ...

class HdmiDisplayInformation(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> HdmiDisplayInformation: ...
    @typing.overload
    def get_current_display_mode(self) -> HdmiDisplayMode: ...
    @typing.overload
    @staticmethod
    def get_for_current_view() -> HdmiDisplayInformation: ...
    @typing.overload
    def get_supported_display_modes(self) -> winsdk.windows.foundation.collections.IVectorView[HdmiDisplayMode]: ...
    @typing.overload
    def request_set_current_display_mode_async(self, mode: HdmiDisplayMode) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_set_current_display_mode_async(self, mode: HdmiDisplayMode, hdr_option: HdmiDisplayHdrOption) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_set_current_display_mode_async(self, mode: HdmiDisplayMode, hdr_option: HdmiDisplayHdrOption, hdr_metadata: HdmiDisplayHdr2086Metadata) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def set_default_display_mode_async(self) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def add_display_modes_changed(self, value: winsdk.windows.foundation.TypedEventHandler[HdmiDisplayInformation, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_display_modes_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class HdmiDisplayMode(_winrt.Object):
    bits_per_pixel: _winrt.UInt16
    color_space: HdmiDisplayColorSpace
    is2086_metadata_supported: _winrt.Boolean
    is_sdr_luminance_supported: _winrt.Boolean
    is_smpte2084_supported: _winrt.Boolean
    pixel_encoding: HdmiDisplayPixelEncoding
    refresh_rate: _winrt.Double
    resolution_height_in_raw_pixels: _winrt.UInt32
    resolution_width_in_raw_pixels: _winrt.UInt32
    stereo_enabled: _winrt.Boolean
    is_dolby_vision_low_latency_supported: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> HdmiDisplayMode: ...
    @typing.overload
    def is_equal(self, mode: HdmiDisplayMode) -> _winrt.Boolean: ...

