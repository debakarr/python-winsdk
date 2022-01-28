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

try:
    import winsdk.windows.foundation.collections
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

class CredentialPromptType(enum.IntEnum):
    PROMPT_IF_NEEDED = 0
    RETYPE_CREDENTIALS = 1
    DO_NOT_PROMPT = 2

class OnlineIdSystemTicketStatus(enum.IntEnum):
    SUCCESS = 0
    ERROR = 1
    SERVICE_CONNECTION_ERROR = 2

class OnlineIdAuthenticator(_winrt.Object):
    ...
    application_id: uuid.UUID
    authenticated_safe_customer_id: str
    can_sign_out: _winrt.Boolean
    def __init__(self, ) -> None:
        ...
    def authenticate_user_async(request: OnlineIdServiceTicketRequest) -> UserAuthenticationOperation:
        ...
    def authenticate_user_async(requests: typing.Iterable[OnlineIdServiceTicketRequest], credential_prompt_type: CredentialPromptType) -> UserAuthenticationOperation:
        ...
    def sign_out_user_async() -> SignOutUserOperation:
        ...

class OnlineIdServiceTicket(_winrt.Object):
    ...
    error_code: _winrt.Int32
    request: OnlineIdServiceTicketRequest
    value: str

class OnlineIdServiceTicketRequest(_winrt.Object):
    ...
    policy: str
    service: str
    def __init__(self, service: str, policy: str) -> None:
        ...
    def __init__(self, service: str) -> None:
        ...

class OnlineIdSystemAuthenticator(_winrt.Object):
    ...
    default: OnlineIdSystemAuthenticatorForUser
    def get_for_user(user: winsdk.windows.system.User) -> OnlineIdSystemAuthenticatorForUser:
        ...

class OnlineIdSystemAuthenticatorForUser(_winrt.Object):
    ...
    application_id: uuid.UUID
    user: winsdk.windows.system.User
    def get_ticket_async(request: OnlineIdServiceTicketRequest) -> winsdk.windows.foundation.IAsyncOperation[OnlineIdSystemTicketResult]:
        ...

class OnlineIdSystemIdentity(_winrt.Object):
    ...
    id: str
    ticket: OnlineIdServiceTicket

class OnlineIdSystemTicketResult(_winrt.Object):
    ...
    extended_error: winsdk.windows.foundation.HResult
    identity: OnlineIdSystemIdentity
    status: OnlineIdSystemTicketStatus

class SignOutUserOperation(winsdk.windows.foundation.IAsyncAction, winsdk.windows.foundation.IAsyncInfo, _winrt.Object):
    ...
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    completed: winsdk.windows.foundation.AsyncActionCompletedHandler
    def cancel() -> None:
        ...
    def close() -> None:
        ...
    def get_results() -> None:
        ...

class UserAuthenticationOperation(winsdk.windows.foundation.IAsyncOperation[UserIdentity], winsdk.windows.foundation.IAsyncInfo, _winrt.Object):
    ...
    error_code: winsdk.windows.foundation.HResult
    id: _winrt.UInt32
    status: winsdk.windows.foundation.AsyncStatus
    completed: winsdk.windows.foundation.AsyncOperationCompletedHandler[UserIdentity]
    def cancel() -> None:
        ...
    def close() -> None:
        ...
    def get_results() -> UserIdentity:
        ...

class UserIdentity(_winrt.Object):
    ...
    first_name: str
    id: str
    is_beta_account: _winrt.Boolean
    is_confirmed_p_c: _winrt.Boolean
    last_name: str
    safe_customer_id: str
    sign_in_name: str
    tickets: winsdk.windows.foundation.collections.IVectorView[OnlineIdServiceTicket]

