# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation

Self = typing.TypeVar('Self')

class BackPressedEventArgs(_winrt.Object):
    handled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> BackPressedEventArgs: ...

class CameraEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> CameraEventArgs: ...

class HardwareButtons(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> HardwareButtons: ...
    @staticmethod
    def add_back_pressed(handler: winsdk.windows.foundation.EventHandler[BackPressedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_back_pressed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @staticmethod
    def add_camera_half_pressed(handler: winsdk.windows.foundation.EventHandler[CameraEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_camera_half_pressed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @staticmethod
    def add_camera_pressed(handler: winsdk.windows.foundation.EventHandler[CameraEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_camera_pressed(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @staticmethod
    def add_camera_released(handler: winsdk.windows.foundation.EventHandler[CameraEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @staticmethod
    def remove_camera_released(token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

