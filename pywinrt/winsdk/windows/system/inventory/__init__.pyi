# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

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

class InstalledDesktopApp(winsdk.windows.foundation.IStringable, _winrt.Object):
    ...
    display_name: str
    display_version: str
    id: str
    publisher: str
    def get_inventory_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[InstalledDesktopApp]]:
        ...
    def to_string() -> str:
        ...

