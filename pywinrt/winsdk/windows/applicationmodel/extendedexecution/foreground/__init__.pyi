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

class ExtendedExecutionForegroundReason(enum.IntEnum):
    UNSPECIFIED = 0
    SAVING_DATA = 1
    BACKGROUND_AUDIO = 2
    UNCONSTRAINED = 3

class ExtendedExecutionForegroundResult(enum.IntEnum):
    ALLOWED = 0
    DENIED = 1

class ExtendedExecutionForegroundRevokedReason(enum.IntEnum):
    RESUMED = 0
    SYSTEM_POLICY = 1

class ExtendedExecutionForegroundRevokedEventArgs(_winrt.Object):
    ...
    reason: ExtendedExecutionForegroundRevokedReason

class ExtendedExecutionForegroundSession(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    reason: ExtendedExecutionForegroundReason
    description: str
    def __init__(self, ) -> None:
        ...
    def close() -> None:
        ...
    def request_extension_async() -> winsdk.windows.foundation.IAsyncOperation[ExtendedExecutionForegroundResult]:
        ...
    def add_revoked(handler: winsdk.windows.foundation.TypedEventHandler[_winrt.Object, ExtendedExecutionForegroundRevokedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_revoked(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

