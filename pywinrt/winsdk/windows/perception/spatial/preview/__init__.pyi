# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation.numerics
except Exception:
    pass

try:
    import winsdk.windows.perception.spatial
except Exception:
    pass

class SpatialGraphInteropFrameOfReferencePreview(_winrt.Object):
    ...
    coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem
    coordinate_system_to_node_transform: winsdk.windows.foundation.numerics.Matrix4x4
    node_id: uuid.UUID

class SpatialGraphInteropPreview(_winrt.Object):
    ...
    def create_coordinate_system_for_node(node_id: uuid.UUID) -> winsdk.windows.perception.spatial.SpatialCoordinateSystem:
        ...
    def create_coordinate_system_for_node(node_id: uuid.UUID, relative_position: winsdk.windows.foundation.numerics.Vector3) -> winsdk.windows.perception.spatial.SpatialCoordinateSystem:
        ...
    def create_coordinate_system_for_node(node_id: uuid.UUID, relative_position: winsdk.windows.foundation.numerics.Vector3, relative_orientation: winsdk.windows.foundation.numerics.Quaternion) -> winsdk.windows.perception.spatial.SpatialCoordinateSystem:
        ...
    def create_locator_for_node(node_id: uuid.UUID) -> winsdk.windows.perception.spatial.SpatialLocator:
        ...
    def try_create_frame_of_reference(coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem) -> SpatialGraphInteropFrameOfReferencePreview:
        ...
    def try_create_frame_of_reference(coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem, relative_position: winsdk.windows.foundation.numerics.Vector3) -> SpatialGraphInteropFrameOfReferencePreview:
        ...
    def try_create_frame_of_reference(coordinate_system: winsdk.windows.perception.spatial.SpatialCoordinateSystem, relative_position: winsdk.windows.foundation.numerics.Vector3, relative_orientation: winsdk.windows.foundation.numerics.Quaternion) -> SpatialGraphInteropFrameOfReferencePreview:
        ...

