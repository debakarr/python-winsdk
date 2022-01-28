# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel
except Exception:
    pass

try:
    import winsdk.windows.foundation
except Exception:
    pass

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

try:
    import winsdk.windows.system.remotesystems
except Exception:
    pass

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

class AppServiceCatalog(_winrt.Object):
    ...
    def find_app_service_providers_async(app_service_name: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.AppInfo]]:
        ...

class AppServiceClosedEventArgs(_winrt.Object):
    ...
    status: AppServiceClosedStatus

class AppServiceConnection(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    package_family_name: str
    app_service_name: str
    user: winsdk.windows.system.User
    def __init__(self, ) -> None:
        ...
    def close() -> None:
        ...
    def open_async() -> winsdk.windows.foundation.IAsyncOperation[AppServiceConnectionStatus]:
        ...
    def open_remote_async(remote_system_connection_request: winsdk.windows.system.remotesystems.RemoteSystemConnectionRequest) -> winsdk.windows.foundation.IAsyncOperation[AppServiceConnectionStatus]:
        ...
    def send_message_async(message: winsdk.windows.foundation.collections.ValueSet) -> winsdk.windows.foundation.IAsyncOperation[AppServiceResponse]:
        ...
    def send_stateless_message_async(connection: AppServiceConnection, connection_request: winsdk.windows.system.remotesystems.RemoteSystemConnectionRequest, message: winsdk.windows.foundation.collections.ValueSet) -> winsdk.windows.foundation.IAsyncOperation[StatelessAppServiceResponse]:
        ...
    def add_request_received(handler: winsdk.windows.foundation.TypedEventHandler[AppServiceConnection, AppServiceRequestReceivedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_request_received(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_service_closed(handler: winsdk.windows.foundation.TypedEventHandler[AppServiceConnection, AppServiceClosedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_service_closed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class AppServiceDeferral(_winrt.Object):
    ...
    def complete() -> None:
        ...

class AppServiceRequest(_winrt.Object):
    ...
    message: winsdk.windows.foundation.collections.ValueSet
    def send_response_async(message: winsdk.windows.foundation.collections.ValueSet) -> winsdk.windows.foundation.IAsyncOperation[AppServiceResponseStatus]:
        ...

class AppServiceRequestReceivedEventArgs(_winrt.Object):
    ...
    request: AppServiceRequest
    def get_deferral() -> AppServiceDeferral:
        ...

class AppServiceResponse(_winrt.Object):
    ...
    message: winsdk.windows.foundation.collections.ValueSet
    status: AppServiceResponseStatus

class AppServiceTriggerDetails(_winrt.Object):
    ...
    app_service_connection: AppServiceConnection
    caller_package_family_name: str
    name: str
    is_remote_system_connection: _winrt.Boolean
    caller_remote_connection_token: str
    def check_caller_for_capability_async(capability_name: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...

class StatelessAppServiceResponse(_winrt.Object):
    ...
    message: winsdk.windows.foundation.collections.ValueSet
    status: StatelessAppServiceResponseStatus

