# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

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
    import winsdk.windows.security.credentials
except Exception:
    pass

class DeviceAccountAuthenticationType(enum.IntEnum):
    BASIC = 0
    O_AUTH = 1
    SINGLE_SIGN_ON = 2

class DeviceAccountIconId(enum.IntEnum):
    EXCHANGE = 0
    MSA = 1
    OUTLOOK = 2
    GENERIC = 3

class DeviceAccountMailAgeFilter(enum.IntEnum):
    ALL = 0
    LAST1_DAY = 1
    LAST3_DAYS = 2
    LAST7_DAYS = 3
    LAST14_DAYS = 4
    LAST30_DAYS = 5
    LAST90_DAYS = 6

class DeviceAccountServerType(enum.IntEnum):
    EXCHANGE = 0
    POP = 1
    IMAP = 2

class DeviceAccountSyncScheduleKind(enum.IntEnum):
    MANUAL = 0
    EVERY15_MINUTES = 1
    EVERY30_MINUTES = 2
    EVERY60_MINUTES = 3
    EVERY2_HOURS = 4
    DAILY = 5
    AS_ITEMS_ARRIVE = 6

class DeviceAccountConfiguration(_winrt.Object):
    email_address: str
    domain: str
    device_account_type_id: str
    outgoing_server_address: str
    contacts_sync_enabled: _winrt.Boolean
    calendar_sync_enabled: _winrt.Boolean
    account_name: str
    incoming_server_username: str
    incoming_server_requires_ssl: _winrt.Boolean
    incoming_server_port: _winrt.Int32
    incoming_server_address: str
    email_sync_enabled: _winrt.Boolean
    server_type: DeviceAccountServerType
    outgoing_server_username: str
    outgoing_server_requires_ssl: _winrt.Boolean
    outgoing_server_port: _winrt.Int32
    account_icon_id: DeviceAccountIconId
    cal_dav_server_url: winsdk.windows.foundation.Uri
    cal_dav_requires_ssl: _winrt.Boolean
    auto_select_authentication_certificate: _winrt.Boolean
    authentication_type: DeviceAccountAuthenticationType
    authentication_certificate_id: str
    is_outgoing_server_authentication_enabled: _winrt.Boolean
    is_client_authentication_certificate_required: _winrt.Boolean
    incoming_server_credential: winsdk.windows.security.credentials.PasswordCredential
    is_outgoing_server_authentication_required: _winrt.Boolean
    card_dav_sync_schedule_kind: DeviceAccountSyncScheduleKind
    always_download_full_message: _winrt.Boolean
    card_dav_server_url: winsdk.windows.foundation.Uri
    card_dav_requires_ssl: _winrt.Boolean
    cal_dav_sync_schedule_kind: DeviceAccountSyncScheduleKind
    incoming_server_certificate_hash: str
    was_outgoing_server_certificate_hash_confirmed: _winrt.Boolean
    was_modified_by_user: _winrt.Boolean
    sync_schedule_kind: DeviceAccountSyncScheduleKind
    sso_account_id: str
    was_incoming_server_certificate_hash_confirmed: _winrt.Boolean
    o_auth_refresh_token: str
    is_externally_managed: _winrt.Boolean
    mail_age_filter: DeviceAccountMailAgeFilter
    is_sync_schedule_managed_by_system: _winrt.Boolean
    outgoing_server_certificate_hash: str
    outgoing_server_credential: winsdk.windows.security.credentials.PasswordCredential
    does_policy_allow_mail_sync: _winrt.Boolean
    is_sso_authentication_supported: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> DeviceAccountConfiguration: ...
    @typing.overload
    def __init__(self) -> None: ...

class UserDataAccountSystemAccessManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountSystemAccessManager: ...
    @typing.overload
    @staticmethod
    def add_and_show_device_accounts_async(accounts: typing.Iterable[DeviceAccountConfiguration]) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[str]]: ...
    @typing.overload
    @staticmethod
    def create_device_account_async(account: DeviceAccountConfiguration) -> winsdk.windows.foundation.IAsyncOperation[str]: ...
    @typing.overload
    @staticmethod
    def delete_device_account_async(account_id: str) -> winsdk.windows.foundation.IAsyncAction: ...
    @typing.overload
    @staticmethod
    def get_device_account_configuration_async(account_id: str) -> winsdk.windows.foundation.IAsyncOperation[DeviceAccountConfiguration]: ...
    @typing.overload
    @staticmethod
    def suppress_local_account_with_account_async(user_data_account_id: str) -> winsdk.windows.foundation.IAsyncAction: ...

