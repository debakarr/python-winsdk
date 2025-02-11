# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.foundation.numerics
import winsdk.windows.graphics.directx
import winsdk.windows.perception.spatial
import winsdk.windows.storage.streams

Self = typing.TypeVar('Self')

class SpatialSurfaceInfo(_winrt.Object):
    id: uuid.UUID
    update_time: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceInfo: ...
    @typing.overload
    def try_compute_latest_mesh_async(self, max_triangles_per_cubic_meter: _winrt.Double) -> winsdk.windows.foundation.IAsyncOperation[SpatialSurfaceMesh]: ...
    @typing.overload
    def try_compute_latest_mesh_async(self, max_triangles_per_cubic_meter: _winrt.Double, options: typing.Optional[SpatialSurfaceMeshOptions]) -> winsdk.windows.foundation.IAsyncOperation[SpatialSurfaceMesh]: ...
    def try_get_bounds(self, coordinate_system: typing.Optional[winsdk.windows.perception.spatial.SpatialCoordinateSystem]) -> typing.Optional[typing.Optional[winsdk.windows.perception.spatial.SpatialBoundingOrientedBox]]: ...

class SpatialSurfaceMesh(_winrt.Object):
    coordinate_system: typing.Optional[winsdk.windows.perception.spatial.SpatialCoordinateSystem]
    surface_info: typing.Optional[SpatialSurfaceInfo]
    triangle_indices: typing.Optional[SpatialSurfaceMeshBuffer]
    vertex_normals: typing.Optional[SpatialSurfaceMeshBuffer]
    vertex_position_scale: winsdk.windows.foundation.numerics.Vector3
    vertex_positions: typing.Optional[SpatialSurfaceMeshBuffer]
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceMesh: ...

class SpatialSurfaceMeshBuffer(_winrt.Object):
    data: typing.Optional[winsdk.windows.storage.streams.IBuffer]
    element_count: _winrt.UInt32
    format: winsdk.windows.graphics.directx.DirectXPixelFormat
    stride: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceMeshBuffer: ...

class SpatialSurfaceMeshOptions(_winrt.Object):
    vertex_position_format: winsdk.windows.graphics.directx.DirectXPixelFormat
    vertex_normal_format: winsdk.windows.graphics.directx.DirectXPixelFormat
    triangle_index_format: winsdk.windows.graphics.directx.DirectXPixelFormat
    include_vertex_normals: _winrt.Boolean
    supported_triangle_index_formats: typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.graphics.directx.DirectXPixelFormat]]
    supported_vertex_normal_formats: typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.graphics.directx.DirectXPixelFormat]]
    supported_vertex_position_formats: typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.graphics.directx.DirectXPixelFormat]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceMeshOptions: ...
    def __init__(self) -> None: ...

class SpatialSurfaceObserver(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceObserver: ...
    def __init__(self) -> None: ...
    def get_observed_surfaces(self) -> typing.Optional[winsdk.windows.foundation.collections.IMapView[uuid.UUID, SpatialSurfaceInfo]]: ...
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    @staticmethod
    def request_access_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.perception.spatial.SpatialPerceptionAccessStatus]: ...
    def set_bounding_volume(self, bounds: typing.Optional[winsdk.windows.perception.spatial.SpatialBoundingVolume]) -> None: ...
    def set_bounding_volumes(self, bounds: typing.Iterable[winsdk.windows.perception.spatial.SpatialBoundingVolume]) -> None: ...
    def add_observed_surfaces_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[SpatialSurfaceObserver, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_observed_surfaces_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

