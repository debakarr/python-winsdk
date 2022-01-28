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
    import winsdk.windows.foundation.numerics
except Exception:
    pass

try:
    import winsdk.windows.ui.composition
except Exception:
    pass

try:
    import winsdk.windows.ui.core
except Exception:
    pass

try:
    import winsdk.windows.ui.input.inking
except Exception:
    pass

class CoreWetStrokeDisposition(enum.IntEnum):
    INKING = 0
    COMPLETED = 1
    CANCELED = 2

class CoreIncrementalInkStroke(_winrt.Object):
    ...
    bounding_rect: winsdk.windows.foundation.Rect
    drawing_attributes: winsdk.windows.ui.input.inking.InkDrawingAttributes
    point_transform: winsdk.windows.foundation.numerics.Matrix3x2
    def __init__(self, drawing_attributes: winsdk.windows.ui.input.inking.InkDrawingAttributes, point_transform: winsdk.windows.foundation.numerics.Matrix3x2) -> None:
        ...
    def append_ink_points(ink_points: typing.Iterable[winsdk.windows.ui.input.inking.InkPoint]) -> winsdk.windows.foundation.Rect:
        ...
    def create_ink_stroke() -> winsdk.windows.ui.input.inking.InkStroke:
        ...

class CoreInkIndependentInputSource(_winrt.Object):
    ...
    ink_presenter: winsdk.windows.ui.input.inking.InkPresenter
    pointer_cursor: winsdk.windows.ui.core.CoreCursor
    def create(ink_presenter: winsdk.windows.ui.input.inking.InkPresenter) -> CoreInkIndependentInputSource:
        ...
    def add_pointer_entering(handler: winsdk.windows.foundation.TypedEventHandler[CoreInkIndependentInputSource, winsdk.windows.ui.core.PointerEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_pointer_entering(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_pointer_exiting(handler: winsdk.windows.foundation.TypedEventHandler[CoreInkIndependentInputSource, winsdk.windows.ui.core.PointerEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_pointer_exiting(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_pointer_hovering(handler: winsdk.windows.foundation.TypedEventHandler[CoreInkIndependentInputSource, winsdk.windows.ui.core.PointerEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_pointer_hovering(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_pointer_lost(handler: winsdk.windows.foundation.TypedEventHandler[CoreInkIndependentInputSource, winsdk.windows.ui.core.PointerEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_pointer_lost(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_pointer_moving(handler: winsdk.windows.foundation.TypedEventHandler[CoreInkIndependentInputSource, winsdk.windows.ui.core.PointerEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_pointer_moving(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_pointer_pressing(handler: winsdk.windows.foundation.TypedEventHandler[CoreInkIndependentInputSource, winsdk.windows.ui.core.PointerEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_pointer_pressing(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_pointer_releasing(handler: winsdk.windows.foundation.TypedEventHandler[CoreInkIndependentInputSource, winsdk.windows.ui.core.PointerEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_pointer_releasing(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class CoreInkPresenterHost(_winrt.Object):
    ...
    root_visual: winsdk.windows.ui.composition.ContainerVisual
    ink_presenter: winsdk.windows.ui.input.inking.InkPresenter
    def __init__(self, ) -> None:
        ...

class CoreWetStrokeUpdateEventArgs(_winrt.Object):
    ...
    disposition: CoreWetStrokeDisposition
    new_ink_points: winsdk.windows.foundation.collections.IVector[winsdk.windows.ui.input.inking.InkPoint]
    pointer_id: _winrt.UInt32

class CoreWetStrokeUpdateSource(_winrt.Object):
    ...
    ink_presenter: winsdk.windows.ui.input.inking.InkPresenter
    def create(ink_presenter: winsdk.windows.ui.input.inking.InkPresenter) -> CoreWetStrokeUpdateSource:
        ...
    def add_wet_stroke_canceled(handler: winsdk.windows.foundation.TypedEventHandler[CoreWetStrokeUpdateSource, CoreWetStrokeUpdateEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_wet_stroke_canceled(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_wet_stroke_completed(handler: winsdk.windows.foundation.TypedEventHandler[CoreWetStrokeUpdateSource, CoreWetStrokeUpdateEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_wet_stroke_completed(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_wet_stroke_continuing(handler: winsdk.windows.foundation.TypedEventHandler[CoreWetStrokeUpdateSource, CoreWetStrokeUpdateEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_wet_stroke_continuing(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_wet_stroke_starting(handler: winsdk.windows.foundation.TypedEventHandler[CoreWetStrokeUpdateSource, CoreWetStrokeUpdateEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_wet_stroke_starting(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_wet_stroke_stopping(handler: winsdk.windows.foundation.TypedEventHandler[CoreWetStrokeUpdateSource, CoreWetStrokeUpdateEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_wet_stroke_stopping(cookie: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

