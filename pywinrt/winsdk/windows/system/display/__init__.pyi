# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

class DisplayRequest(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> DisplayRequest: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def request_active(self) -> None: ...
    @typing.overload
    def request_release(self) -> None: ...

