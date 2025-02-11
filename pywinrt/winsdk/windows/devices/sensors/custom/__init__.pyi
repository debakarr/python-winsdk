# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections

Self = typing.TypeVar('Self')

class CustomSensor(_winrt.Object):
    report_interval: _winrt.UInt32
    device_id: str
    minimum_report_interval: _winrt.UInt32
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> CustomSensor: ...
    @staticmethod
    def from_id_async(sensor_id: str) -> winsdk.windows.foundation.IAsyncOperation[CustomSensor]: ...
    def get_current_reading(self) -> typing.Optional[CustomSensorReading]: ...
    @staticmethod
    def get_device_selector(interface_id: uuid.UUID) -> str: ...
    def add_reading_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[CustomSensor, CustomSensorReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_reading_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class CustomSensorReading(_winrt.Object):
    properties: typing.Optional[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[typing.Optional[winsdk.windows.foundation.TimeSpan]]
    @staticmethod
    def _from(obj: _winrt.Object) -> CustomSensorReading: ...

class CustomSensorReadingChangedEventArgs(_winrt.Object):
    reading: typing.Optional[CustomSensorReading]
    @staticmethod
    def _from(obj: _winrt.Object) -> CustomSensorReadingChangedEventArgs: ...

