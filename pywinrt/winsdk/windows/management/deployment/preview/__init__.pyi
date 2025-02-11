# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

Self = typing.TypeVar('Self')

class ClassicAppManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> ClassicAppManager: ...
    @staticmethod
    def find_installed_app(app_uninstall_key: str) -> typing.Optional[InstalledClassicAppInfo]: ...

class InstalledClassicAppInfo(_winrt.Object):
    display_name: str
    display_version: str
    @staticmethod
    def _from(obj: _winrt.Object) -> InstalledClassicAppInfo: ...

