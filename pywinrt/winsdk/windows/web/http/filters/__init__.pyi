# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.networking.sockets
import winsdk.windows.security.credentials
import winsdk.windows.security.cryptography.certificates
import winsdk.windows.system
import winsdk.windows.web.http

class HttpCacheReadBehavior(enum.IntEnum):
    DEFAULT = 0
    MOST_RECENT = 1
    ONLY_FROM_CACHE = 2
    NO_CACHE = 3

class HttpCacheWriteBehavior(enum.IntEnum):
    DEFAULT = 0
    NO_CACHE = 1

class HttpCookieUsageBehavior(enum.IntEnum):
    DEFAULT = 0
    NO_COOKIES = 1

Self = typing.TypeVar('Self')

class HttpBaseProtocolFilter(_winrt.Object):
    use_proxy: _winrt.Boolean
    server_credential: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]
    proxy_credential: typing.Optional[winsdk.windows.security.credentials.PasswordCredential]
    max_connections_per_server: _winrt.UInt32
    client_certificate: typing.Optional[winsdk.windows.security.cryptography.certificates.Certificate]
    automatic_decompression: _winrt.Boolean
    allow_u_i: _winrt.Boolean
    allow_auto_redirect: _winrt.Boolean
    cache_control: typing.Optional[HttpCacheControl]
    cookie_manager: typing.Optional[winsdk.windows.web.http.HttpCookieManager]
    ignorable_server_certificate_errors: typing.Optional[winsdk.windows.foundation.collections.IVector[winsdk.windows.security.cryptography.certificates.ChainValidationResult]]
    max_version: winsdk.windows.web.http.HttpVersion
    cookie_usage_behavior: HttpCookieUsageBehavior
    user: typing.Optional[winsdk.windows.system.User]
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> HttpBaseProtocolFilter: ...
    def __init__(self) -> None: ...
    def clear_authentication_cache(self) -> None: ...
    def close(self) -> None: ...
    @staticmethod
    def create_for_user(user: typing.Optional[winsdk.windows.system.User]) -> typing.Optional[HttpBaseProtocolFilter]: ...
    def send_request_async(self, request: typing.Optional[winsdk.windows.web.http.HttpRequestMessage]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[winsdk.windows.web.http.HttpResponseMessage, winsdk.windows.web.http.HttpProgress]: ...
    def add_server_custom_validation_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[HttpBaseProtocolFilter, HttpServerCustomValidationRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_server_custom_validation_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class HttpCacheControl(_winrt.Object):
    write_behavior: HttpCacheWriteBehavior
    read_behavior: HttpCacheReadBehavior
    @staticmethod
    def _from(obj: _winrt.Object) -> HttpCacheControl: ...

class HttpServerCustomValidationRequestedEventArgs(_winrt.Object):
    request_message: typing.Optional[winsdk.windows.web.http.HttpRequestMessage]
    server_certificate: typing.Optional[winsdk.windows.security.cryptography.certificates.Certificate]
    server_certificate_error_severity: winsdk.windows.networking.sockets.SocketSslErrorSeverity
    server_certificate_errors: typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.security.cryptography.certificates.ChainValidationResult]]
    server_intermediate_certificates: typing.Optional[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.security.cryptography.certificates.Certificate]]
    @staticmethod
    def _from(obj: _winrt.Object) -> HttpServerCustomValidationRequestedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...
    def reject(self) -> None: ...

class IHttpFilter(_winrt.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: _winrt.Object) -> IHttpFilter: ...
    def send_request_async(self, request: typing.Optional[winsdk.windows.web.http.HttpRequestMessage]) -> winsdk.windows.foundation.IAsyncOperationWithProgress[winsdk.windows.web.http.HttpResponseMessage, winsdk.windows.web.http.HttpProgress]: ...
    def close(self) -> None: ...

