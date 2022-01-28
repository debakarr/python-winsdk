# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

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
    import winsdk.windows.graphics.directx.direct3d11
except Exception:
    pass

try:
    import winsdk.windows.storage.streams
except Exception:
    pass

class BitmapAlphaMode(enum.IntEnum):
    PREMULTIPLIED = 0
    STRAIGHT = 1
    IGNORE = 2

class BitmapBufferAccessMode(enum.IntEnum):
    READ = 0
    READ_WRITE = 1
    WRITE = 2

class BitmapFlip(enum.IntEnum):
    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2

class BitmapInterpolationMode(enum.IntEnum):
    NEAREST_NEIGHBOR = 0
    LINEAR = 1
    CUBIC = 2
    FANT = 3

class BitmapPixelFormat(enum.IntEnum):
    UNKNOWN = 0
    RGBA16 = 12
    RGBA8 = 30
    GRAY16 = 57
    GRAY8 = 62
    BGRA8 = 87
    NV12 = 103
    P010 = 104
    YUY2 = 107

class BitmapRotation(enum.IntEnum):
    NONE = 0
    CLOCKWISE90_DEGREES = 1
    CLOCKWISE180_DEGREES = 2
    CLOCKWISE270_DEGREES = 3

class ColorManagementMode(enum.IntEnum):
    DO_NOT_COLOR_MANAGE = 0
    COLOR_MANAGE_TO_S_RGB = 1

class ExifOrientationMode(enum.IntEnum):
    IGNORE_EXIF_ORIENTATION = 0
    RESPECT_EXIF_ORIENTATION = 1

class JpegSubsamplingMode(enum.IntEnum):
    DEFAULT = 0
    Y4_CB2_CR0 = 1
    Y4_CB2_CR2 = 2
    Y4_CB4_CR4 = 3

class PngFilterMode(enum.IntEnum):
    AUTOMATIC = 0
    NONE = 1
    SUB = 2
    UP = 3
    AVERAGE = 4
    PAETH = 5
    ADAPTIVE = 6

class TiffCompressionMode(enum.IntEnum):
    AUTOMATIC = 0
    NONE = 1
    CCITT3 = 2
    CCITT4 = 3
    LZW = 4
    RLE = 5
    ZIP = 6
    LZWH_DIFFERENCING = 7

class BitmapBounds:
    x: _winrt.UInt32
    y: _winrt.UInt32
    width: _winrt.UInt32
    height: _winrt.UInt32
    def __init__(self, x: _winrt.UInt32, y: _winrt.UInt32, width: _winrt.UInt32, height: _winrt.UInt32) -> None: ...

class BitmapPlaneDescription:
    start_index: _winrt.Int32
    width: _winrt.Int32
    height: _winrt.Int32
    stride: _winrt.Int32
    def __init__(self, start_index: _winrt.Int32, width: _winrt.Int32, height: _winrt.Int32, stride: _winrt.Int32) -> None: ...

class BitmapSize:
    width: _winrt.UInt32
    height: _winrt.UInt32
    def __init__(self, width: _winrt.UInt32, height: _winrt.UInt32) -> None: ...

class BitmapBuffer(winsdk.windows.foundation.IMemoryBuffer, winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    def close() -> None:
        ...
    def create_reference() -> winsdk.windows.foundation.IMemoryBufferReference:
        ...
    def get_plane_count() -> _winrt.Int32:
        ...
    def get_plane_description(index: _winrt.Int32) -> BitmapPlaneDescription:
        ...

class BitmapCodecInformation(_winrt.Object):
    ...
    codec_id: uuid.UUID
    file_extensions: winsdk.windows.foundation.collections.IVectorView[str]
    friendly_name: str
    mime_types: winsdk.windows.foundation.collections.IVectorView[str]

class BitmapDecoder(IBitmapFrame, IBitmapFrameWithSoftwareBitmap, _winrt.Object):
    ...
    bitmap_container_properties: BitmapPropertiesView
    decoder_information: BitmapCodecInformation
    frame_count: _winrt.UInt32
    bitmap_alpha_mode: BitmapAlphaMode
    bitmap_pixel_format: BitmapPixelFormat
    bitmap_properties: BitmapPropertiesView
    dpi_x: _winrt.Double
    dpi_y: _winrt.Double
    oriented_pixel_height: _winrt.UInt32
    oriented_pixel_width: _winrt.UInt32
    pixel_height: _winrt.UInt32
    pixel_width: _winrt.UInt32
    bmp_decoder_id: uuid.UUID
    gif_decoder_id: uuid.UUID
    ico_decoder_id: uuid.UUID
    jpeg_decoder_id: uuid.UUID
    jpeg_x_r_decoder_id: uuid.UUID
    png_decoder_id: uuid.UUID
    tiff_decoder_id: uuid.UUID
    heif_decoder_id: uuid.UUID
    webp_decoder_id: uuid.UUID
    def create_async(stream: winsdk.windows.storage.streams.IRandomAccessStream) -> winsdk.windows.foundation.IAsyncOperation[BitmapDecoder]:
        ...
    def create_async(decoder_id: uuid.UUID, stream: winsdk.windows.storage.streams.IRandomAccessStream) -> winsdk.windows.foundation.IAsyncOperation[BitmapDecoder]:
        ...
    def get_decoder_information_enumerator() -> winsdk.windows.foundation.collections.IVectorView[BitmapCodecInformation]:
        ...
    def get_frame_async(frame_index: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[BitmapFrame]:
        ...
    def get_pixel_data_async() -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_pixel_data_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: BitmapTransform, exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode) -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_preview_async() -> winsdk.windows.foundation.IAsyncOperation[ImageStream]:
        ...
    def get_software_bitmap_async() -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_software_bitmap_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_software_bitmap_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: BitmapTransform, exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_thumbnail_async() -> winsdk.windows.foundation.IAsyncOperation[ImageStream]:
        ...

class BitmapEncoder(_winrt.Object):
    ...
    is_thumbnail_generated: _winrt.Boolean
    generated_thumbnail_width: _winrt.UInt32
    generated_thumbnail_height: _winrt.UInt32
    bitmap_container_properties: BitmapProperties
    bitmap_properties: BitmapProperties
    bitmap_transform: BitmapTransform
    encoder_information: BitmapCodecInformation
    bmp_encoder_id: uuid.UUID
    gif_encoder_id: uuid.UUID
    jpeg_encoder_id: uuid.UUID
    jpeg_x_r_encoder_id: uuid.UUID
    png_encoder_id: uuid.UUID
    tiff_encoder_id: uuid.UUID
    heif_encoder_id: uuid.UUID
    def create_async(encoder_id: uuid.UUID, stream: winsdk.windows.storage.streams.IRandomAccessStream) -> winsdk.windows.foundation.IAsyncOperation[BitmapEncoder]:
        ...
    def create_async(encoder_id: uuid.UUID, stream: winsdk.windows.storage.streams.IRandomAccessStream, encoding_options: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, BitmapTypedValue]]) -> winsdk.windows.foundation.IAsyncOperation[BitmapEncoder]:
        ...
    def create_for_in_place_property_encoding_async(bitmap_decoder: BitmapDecoder) -> winsdk.windows.foundation.IAsyncOperation[BitmapEncoder]:
        ...
    def create_for_transcoding_async(stream: winsdk.windows.storage.streams.IRandomAccessStream, bitmap_decoder: BitmapDecoder) -> winsdk.windows.foundation.IAsyncOperation[BitmapEncoder]:
        ...
    def flush_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def get_encoder_information_enumerator() -> winsdk.windows.foundation.collections.IVectorView[BitmapCodecInformation]:
        ...
    def go_to_next_frame_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def go_to_next_frame_async(encoding_options: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, BitmapTypedValue]]) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def set_pixel_data(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, width: _winrt.UInt32, height: _winrt.UInt32, dpi_x: _winrt.Double, dpi_y: _winrt.Double, pixels: typing.Sequence[_winrt.UInt8]) -> None:
        ...
    def set_software_bitmap(bitmap: SoftwareBitmap) -> None:
        ...

class BitmapFrame(IBitmapFrame, IBitmapFrameWithSoftwareBitmap, _winrt.Object):
    ...
    bitmap_alpha_mode: BitmapAlphaMode
    bitmap_pixel_format: BitmapPixelFormat
    bitmap_properties: BitmapPropertiesView
    dpi_x: _winrt.Double
    dpi_y: _winrt.Double
    oriented_pixel_height: _winrt.UInt32
    oriented_pixel_width: _winrt.UInt32
    pixel_height: _winrt.UInt32
    pixel_width: _winrt.UInt32
    def get_pixel_data_async() -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_pixel_data_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: BitmapTransform, exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode) -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_software_bitmap_async() -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_software_bitmap_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_software_bitmap_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: BitmapTransform, exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_thumbnail_async() -> winsdk.windows.foundation.IAsyncOperation[ImageStream]:
        ...

class BitmapProperties(IBitmapPropertiesView, _winrt.Object):
    ...
    def get_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[BitmapPropertySet]:
        ...
    def set_properties_async(properties_to_set: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, BitmapTypedValue]]) -> winsdk.windows.foundation.IAsyncAction:
        ...

class BitmapPropertiesView(IBitmapPropertiesView, _winrt.Object):
    ...
    def get_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[BitmapPropertySet]:
        ...

class BitmapPropertySet(winsdk.windows.foundation.collections.IMap[str, BitmapTypedValue], winsdk.windows.foundation.collections.IIterable[winsdk.windows.foundation.collections.IKeyValuePair[str, BitmapTypedValue]], _winrt.Object):
    ...
    size: _winrt.UInt32
    def __init__(self, ) -> None:
        ...
    def clear() -> None:
        ...
    def first() -> winsdk.windows.foundation.collections.IIterator[winsdk.windows.foundation.collections.IKeyValuePair[str, BitmapTypedValue]]:
        ...
    def get_view() -> winsdk.windows.foundation.collections.IMapView[str, BitmapTypedValue]:
        ...
    def has_key(key: str) -> _winrt.Boolean:
        ...
    def insert(key: str, value: BitmapTypedValue) -> _winrt.Boolean:
        ...
    def lookup(key: str) -> BitmapTypedValue:
        ...
    def remove(key: str) -> None:
        ...

class BitmapTransform(_winrt.Object):
    ...
    scaled_width: _winrt.UInt32
    scaled_height: _winrt.UInt32
    rotation: BitmapRotation
    interpolation_mode: BitmapInterpolationMode
    flip: BitmapFlip
    bounds: BitmapBounds
    def __init__(self, ) -> None:
        ...

class BitmapTypedValue(_winrt.Object):
    ...
    type: winsdk.windows.foundation.PropertyType
    value: _winrt.Object
    def __init__(self, value: _winrt.Object, type: winsdk.windows.foundation.PropertyType) -> None:
        ...

class ImageStream(winsdk.windows.storage.streams.IRandomAccessStreamWithContentType, winsdk.windows.storage.streams.IContentTypeProvider, winsdk.windows.storage.streams.IRandomAccessStream, winsdk.windows.storage.streams.IOutputStream, winsdk.windows.foundation.IClosable, winsdk.windows.storage.streams.IInputStream, _winrt.Object):
    ...
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

class PixelDataProvider(_winrt.Object):
    ...
    def detach_pixel_data() -> _winrt.UInt8:
        ...

class SoftwareBitmap(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    dpi_y: _winrt.Double
    dpi_x: _winrt.Double
    bitmap_alpha_mode: BitmapAlphaMode
    bitmap_pixel_format: BitmapPixelFormat
    is_read_only: _winrt.Boolean
    pixel_height: _winrt.Int32
    pixel_width: _winrt.Int32
    def __init__(self, format: BitmapPixelFormat, width: _winrt.Int32, height: _winrt.Int32) -> None:
        ...
    def __init__(self, format: BitmapPixelFormat, width: _winrt.Int32, height: _winrt.Int32, alpha: BitmapAlphaMode) -> None:
        ...
    def close() -> None:
        ...
    def convert(source: SoftwareBitmap, format: BitmapPixelFormat) -> SoftwareBitmap:
        ...
    def convert(source: SoftwareBitmap, format: BitmapPixelFormat, alpha: BitmapAlphaMode) -> SoftwareBitmap:
        ...
    def copy(source: SoftwareBitmap) -> SoftwareBitmap:
        ...
    def copy_from_buffer(buffer: winsdk.windows.storage.streams.IBuffer) -> None:
        ...
    def copy_to(bitmap: SoftwareBitmap) -> None:
        ...
    def copy_to_buffer(buffer: winsdk.windows.storage.streams.IBuffer) -> None:
        ...
    def create_copy_from_buffer(source: winsdk.windows.storage.streams.IBuffer, format: BitmapPixelFormat, width: _winrt.Int32, height: _winrt.Int32) -> SoftwareBitmap:
        ...
    def create_copy_from_buffer(source: winsdk.windows.storage.streams.IBuffer, format: BitmapPixelFormat, width: _winrt.Int32, height: _winrt.Int32, alpha: BitmapAlphaMode) -> SoftwareBitmap:
        ...
    def create_copy_from_surface_async(surface: winsdk.windows.graphics.directx.direct3d11.IDirect3DSurface) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def create_copy_from_surface_async(surface: winsdk.windows.graphics.directx.direct3d11.IDirect3DSurface, alpha: BitmapAlphaMode) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_read_only_view() -> SoftwareBitmap:
        ...
    def lock_buffer(mode: BitmapBufferAccessMode) -> BitmapBuffer:
        ...

class IBitmapFrame(_winrt.Object):
    ...
    bitmap_alpha_mode: BitmapAlphaMode
    bitmap_pixel_format: BitmapPixelFormat
    bitmap_properties: BitmapPropertiesView
    dpi_x: _winrt.Double
    dpi_y: _winrt.Double
    oriented_pixel_height: _winrt.UInt32
    oriented_pixel_width: _winrt.UInt32
    pixel_height: _winrt.UInt32
    pixel_width: _winrt.UInt32
    def get_pixel_data_async() -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_pixel_data_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: BitmapTransform, exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode) -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_thumbnail_async() -> winsdk.windows.foundation.IAsyncOperation[ImageStream]:
        ...

class IBitmapFrameWithSoftwareBitmap(IBitmapFrame, _winrt.Object):
    ...
    bitmap_alpha_mode: BitmapAlphaMode
    bitmap_pixel_format: BitmapPixelFormat
    bitmap_properties: BitmapPropertiesView
    dpi_x: _winrt.Double
    dpi_y: _winrt.Double
    oriented_pixel_height: _winrt.UInt32
    oriented_pixel_width: _winrt.UInt32
    pixel_height: _winrt.UInt32
    pixel_width: _winrt.UInt32
    def get_software_bitmap_async() -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_software_bitmap_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_software_bitmap_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: BitmapTransform, exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode) -> winsdk.windows.foundation.IAsyncOperation[SoftwareBitmap]:
        ...
    def get_pixel_data_async() -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_pixel_data_async(pixel_format: BitmapPixelFormat, alpha_mode: BitmapAlphaMode, transform: BitmapTransform, exif_orientation_mode: ExifOrientationMode, color_management_mode: ColorManagementMode) -> winsdk.windows.foundation.IAsyncOperation[PixelDataProvider]:
        ...
    def get_thumbnail_async() -> winsdk.windows.foundation.IAsyncOperation[ImageStream]:
        ...

class IBitmapPropertiesView(_winrt.Object):
    ...
    def get_properties_async(properties_to_retrieve: typing.Iterable[str]) -> winsdk.windows.foundation.IAsyncOperation[BitmapPropertySet]:
        ...

