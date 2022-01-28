# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

class PlatformTelemetryRegistrationStatus(enum.IntEnum):
    SUCCESS = 0
    SETTINGS_OUT_OF_RANGE = 1
    UNKNOWN_FAILURE = 2

class PlatformTelemetryClient(_winrt.Object):
    ...
    def register(id: str) -> PlatformTelemetryRegistrationResult:
        ...
    def register(id: str, settings: PlatformTelemetryRegistrationSettings) -> PlatformTelemetryRegistrationResult:
        ...

class PlatformTelemetryRegistrationResult(_winrt.Object):
    ...
    status: PlatformTelemetryRegistrationStatus

class PlatformTelemetryRegistrationSettings(_winrt.Object):
    ...
    upload_quota_size: _winrt.UInt32
    storage_size: _winrt.UInt32
    def __init__(self, ) -> None:
        ...

