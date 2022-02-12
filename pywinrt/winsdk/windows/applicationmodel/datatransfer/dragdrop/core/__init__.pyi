# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.datatransfer
except Exception:
    pass

try:
    import winsdk.windows.applicationmodel.datatransfer.dragdrop
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.graphics.imaging
except Exception:
    pass

class CoreDragUIContentMode(enum.IntFlag):
    AUTO = 0
    DEFERRED = 0x1

class CoreDragDropManager(_winrt.Object):
    are_concurrent_operations_enabled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreDragDropManager: ...
    @typing.overload
    @staticmethod
    def get_for_current_view() -> CoreDragDropManager: ...
    @typing.overload
    def add_target_requested(self, value: winsdk.windows.foundation.TypedEventHandler[CoreDragDropManager, CoreDropOperationTargetRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_target_requested(self, value: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class CoreDragInfo(_winrt.Object):
    data: winsdk.windows.applicationmodel.datatransfer.DataPackageView
    modifiers: winsdk.windows.applicationmodel.datatransfer.dragdrop.DragDropModifiers
    position: winsdk.windows.foundation.Point
    allowed_operations: winsdk.windows.applicationmodel.datatransfer.DataPackageOperation
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreDragInfo: ...

class CoreDragOperation(_winrt.Object):
    drag_u_i_content_mode: CoreDragUIContentMode
    data: winsdk.windows.applicationmodel.datatransfer.DataPackage
    allowed_operations: winsdk.windows.applicationmodel.datatransfer.DataPackageOperation
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreDragOperation: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def set_drag_u_i_content_from_software_bitmap(self, software_bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap) -> None: ...
    @typing.overload
    def set_drag_u_i_content_from_software_bitmap(self, software_bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap, anchor_point: winsdk.windows.foundation.Point) -> None: ...
    @typing.overload
    def set_pointer_id(self, pointer_id: _winrt.UInt32) -> None: ...
    @typing.overload
    def start_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.applicationmodel.datatransfer.DataPackageOperation]: ...

class CoreDragUIOverride(_winrt.Object):
    is_glyph_visible: _winrt.Boolean
    is_content_visible: _winrt.Boolean
    is_caption_visible: _winrt.Boolean
    caption: str
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreDragUIOverride: ...
    @typing.overload
    def clear(self) -> None: ...
    @typing.overload
    def set_content_from_software_bitmap(self, software_bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap) -> None: ...
    @typing.overload
    def set_content_from_software_bitmap(self, software_bitmap: winsdk.windows.graphics.imaging.SoftwareBitmap, anchor_point: winsdk.windows.foundation.Point) -> None: ...

class CoreDropOperationTargetRequestedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> CoreDropOperationTargetRequestedEventArgs: ...
    @typing.overload
    def set_target(self, target: ICoreDropOperationTarget) -> None: ...

class ICoreDropOperationTarget(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ICoreDropOperationTarget: ...
    @typing.overload
    def drop_async(self, drag_info: CoreDragInfo) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.applicationmodel.datatransfer.DataPackageOperation]: ...
    @typing.overload
    def enter_async(self, drag_info: CoreDragInfo, drag_u_i_override: CoreDragUIOverride) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.applicationmodel.datatransfer.DataPackageOperation]: ...
    @typing.overload
    def leave_async(self, drag_info: CoreDragInfo) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    def over_async(self, drag_info: CoreDragInfo, drag_u_i_override: CoreDragUIOverride) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.applicationmodel.datatransfer.DataPackageOperation]: ...

