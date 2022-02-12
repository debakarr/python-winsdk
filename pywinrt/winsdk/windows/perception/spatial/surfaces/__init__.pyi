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
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.foundation.numerics
except Exception:
    pass

try:
    import winsdk.windows.graphics.directx
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

class SpatialSurfaceInfo(_winrt.Object):
    id: uuid.UUID
    update_time: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceInfo: ...
    @typing.overload
    def try_compute_latest_mesh_async(self, max_triangles_per_cubic_meter: _winrt.Double) -> winsdk.windows.foundation.IAsyncOperation[SpatialSurfaceMesh]: ...
    @typing.overload
    def try_compute_latest_mesh_async(self, max_triangles_per_cubic_meter: _winrt.Double, options: SpatialSurfaceMeshOptions) -> winsdk.windows.foundation.IAsyncOperation[SpatialSurfaceMesh]: ...
    @typing.overload
    def try_get_bounds(self, coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem) -> typing.Optional[winsdk.windows.perception.spatial.SpatialBoundingOrientedBox]: ...

class SpatialSurfaceMesh(_winrt.Object):
    coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem
    surface_info: SpatialSurfaceInfo
    triangle_indices: SpatialSurfaceMeshBuffer
    vertex_normals: SpatialSurfaceMeshBuffer
    vertex_position_scale: winsdk.windows.foundation.numerics.Vector3
    vertex_positions: SpatialSurfaceMeshBuffer
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceMesh: ...

class SpatialSurfaceMeshBuffer(_winrt.Object):
    data: winsdk.windows.storage.streams.IBuffer
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
    supported_triangle_index_formats: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.graphics.directx.DirectXPixelFormat]
    supported_vertex_normal_formats: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.graphics.directx.DirectXPixelFormat]
    supported_vertex_position_formats: winsdk.windows.foundation.collections.IVectorView[winsdk.windows.graphics.directx.DirectXPixelFormat]
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceMeshOptions: ...
    @typing.overload
    def __init__(self) -> None: ...

class SpatialSurfaceObserver(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> SpatialSurfaceObserver: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def get_observed_surfaces(self) -> winsdk.windows.foundation.collections.IMapView[uuid.UUID, SpatialSurfaceInfo]: ...
    @typing.overload
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def request_access_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.perception.spatial.SpatialPerceptionAccessStatus]: ...
    @typing.overload
    def set_bounding_volume(self, bounds: winsdk.windows.perception.spatial.SpatialBoundingVolume) -> None: ...
    @typing.overload
    def set_bounding_volumes(self, bounds: typing.Iterable[winsdk.windows.perception.spatial.SpatialBoundingVolume]) -> None: ...
    @typing.overload
    def add_observed_surfaces_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[SpatialSurfaceObserver, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_observed_surfaces_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

