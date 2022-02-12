# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.core
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

try:
    import winsdk.windows.ui.core
except Exception:
    pass

try:
    import winsdk.windows.ui.input
except Exception:
    pass

class RadialControllerIndependentInputSource(_winrt.Object):
    controller: winsdk.windows.ui.input.RadialController
    dispatcher: winsdk.windows.ui.core.CoreDispatcher
    dispatcher_queue: winsdk.windows.system.DispatcherQueue
    @staticmethod
    def _from(obj: _winrt.Object) -> RadialControllerIndependentInputSource: ...
    @typing.overload
    @staticmethod
    def create_for_view(view: winsdk.windows.applicationmodel.core.CoreApplicationView) -> RadialControllerIndependentInputSource: ...

