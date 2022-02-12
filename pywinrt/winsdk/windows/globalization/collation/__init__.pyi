# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

class CharacterGrouping(_winrt.Object):
    first: str
    label: str
    @staticmethod
    def _from(obj: _winrt.Object) -> CharacterGrouping: ...

class CharacterGroupings(winsdk.windows.foundation.collections.IVectorView[CharacterGrouping], winsdk.windows.foundation.collections.IIterable[CharacterGrouping], _winrt.Object):
    size: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> CharacterGroupings: ...
    @typing.overload
    def __init__(self, language: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def first(self) -> winsdk.windows.foundation.collections.IIterator[CharacterGrouping]: ...
    @typing.overload
    def get_at(self, index: _winrt.UInt32) -> CharacterGrouping: ...
    @typing.overload
    def get_many(self, start_index: _winrt.UInt32, items_size: _winrt.UInt32) -> typing.Tuple[_winrt.UInt32, typing.List[CharacterGrouping]]: ...
    @typing.overload
    def index_of(self, value: CharacterGrouping) -> typing.Tuple[_winrt.Boolean, _winrt.UInt32]: ...
    @typing.overload
    def lookup(self, text: str) -> str: ...

