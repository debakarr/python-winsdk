# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.applicationmodel
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.system
import winsdk.windows.system.remotesystems

class AppServiceClosedStatus(enum.IntEnum):
    COMPLETED = 0
    CANCELED = 1
    RESOURCE_LIMITS_EXCEEDED = 2
    UNKNOWN = 3

class AppServiceConnectionStatus(enum.IntEnum):
    SUCCESS = 0
    APP_NOT_INSTALLED = 1
    APP_UNAVAILABLE = 2
    APP_SERVICE_UNAVAILABLE = 3
    UNKNOWN = 4
    REMOTE_SYSTEM_UNAVAILABLE = 5
    REMOTE_SYSTEM_NOT_SUPPORTED_BY_APP = 6
    NOT_AUTHORIZED = 7
    AUTHENTICATION_ERROR = 8
    NETWORK_NOT_AVAILABLE = 9
    DISABLED_BY_POLICY = 10
    WEB_SERVICE_UNAVAILABLE = 11

class AppServiceResponseStatus(enum.IntEnum):
    SUCCESS = 0
    FAILURE = 1
    RESOURCE_LIMITS_EXCEEDED = 2
    UNKNOWN = 3
    REMOTE_SYSTEM_UNAVAILABLE = 4
    MESSAGE_SIZE_TOO_LARGE = 5
    APP_UNAVAILABLE = 6
    AUTHENTICATION_ERROR = 7
    NETWORK_NOT_AVAILABLE = 8
    DISABLED_BY_POLICY = 9
    WEB_SERVICE_UNAVAILABLE = 10

class StatelessAppServiceResponseStatus(enum.IntEnum):
    SUCCESS = 0
    APP_NOT_INSTALLED = 1
    APP_UNAVAILABLE = 2
    APP_SERVICE_UNAVAILABLE = 3
    REMOTE_SYSTEM_UNAVAILABLE = 4
    REMOTE_SYSTEM_NOT_SUPPORTED_BY_APP = 5
    NOT_AUTHORIZED = 6
    RESOURCE_LIMITS_EXCEEDED = 7
    MESSAGE_SIZE_TOO_LARGE = 8
    FAILURE = 9
    UNKNOWN = 10
    AUTHENTICATION_ERROR = 11
    NETWORK_NOT_AVAILABLE = 12
    DISABLED_BY_POLICY = 13
    WEB_SERVICE_UNAVAILABLE = 14

Self = typing.TypeVar('Self')

class AppServiceCatalog(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceCatalog: ...
    @staticmethod
    def find_app_service_providers_async(app_service_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.AppInfo]]: ...

class AppServiceClosedEventArgs(_winrt.Object):
    status: AppServiceClosedStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceClosedEventArgs: ...

class AppServiceConnection(_winrt.Object):
    package_family_name: str
    app_service_name: str
    user: typing.Optional[winsdk.windows.system.User]
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceConnection: ...
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def open_async(self) -> winsdk.windows.foundation.IAsyncOperation[AppServiceConnectionStatus]: ...
    def open_remote_async(self, remote_system_connection_request: typing.Optional[winsdk.windows.system.remotesystems.RemoteSystemConnectionRequest]) -> winsdk.windows.foundation.IAsyncOperation[AppServiceConnectionStatus]: ...
    def send_message_async(self, message: typing.Optional[winsdk.windows.foundation.collections.ValueSet]) -> winsdk.windows.foundation.IAsyncOperation[AppServiceResponse]: ...
    @staticmethod
    def send_stateless_message_async(connection: typing.Optional[AppServiceConnection], connection_request: typing.Optional[winsdk.windows.system.remotesystems.RemoteSystemConnectionRequest], message: typing.Optional[winsdk.windows.foundation.collections.ValueSet]) -> winsdk.windows.foundation.IAsyncOperation[StatelessAppServiceResponse]: ...
    def add_request_received(self, handler: winsdk.windows.foundation.TypedEventHandler[AppServiceConnection, AppServiceRequestReceivedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_request_received(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    def add_service_closed(self, handler: winsdk.windows.foundation.TypedEventHandler[AppServiceConnection, AppServiceClosedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_service_closed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class AppServiceDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceDeferral: ...
    def complete(self) -> None: ...

class AppServiceRequest(_winrt.Object):
    message: typing.Optional[winsdk.windows.foundation.collections.ValueSet]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceRequest: ...
    def send_response_async(self, message: typing.Optional[winsdk.windows.foundation.collections.ValueSet]) -> winsdk.windows.foundation.IAsyncOperation[AppServiceResponseStatus]: ...

class AppServiceRequestReceivedEventArgs(_winrt.Object):
    request: typing.Optional[AppServiceRequest]
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceRequestReceivedEventArgs: ...
    def get_deferral(self) -> typing.Optional[AppServiceDeferral]: ...

class AppServiceResponse(_winrt.Object):
    message: typing.Optional[winsdk.windows.foundation.collections.ValueSet]
    status: AppServiceResponseStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceResponse: ...

class AppServiceTriggerDetails(_winrt.Object):
    app_service_connection: typing.Optional[AppServiceConnection]
    caller_package_family_name: str
    name: str
    is_remote_system_connection: _winrt.Boolean
    caller_remote_connection_token: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AppServiceTriggerDetails: ...
    def check_caller_for_capability_async(self, capability_name: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class StatelessAppServiceResponse(_winrt.Object):
    message: typing.Optional[winsdk.windows.foundation.collections.ValueSet]
    status: StatelessAppServiceResponseStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> StatelessAppServiceResponse: ...

