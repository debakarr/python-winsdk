# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.applicationmodel.appointments
import winsdk.windows.applicationmodel.contacts
import winsdk.windows.applicationmodel.email
import winsdk.windows.applicationmodel.userdatatasks
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.storage.streams
import winsdk.windows.system

class UserDataAccountContentKinds(enum.IntFlag):
    EMAIL = 0x1
    CONTACT = 0x2
    APPOINTMENT = 0x4

class UserDataAccountOtherAppReadAccess(enum.IntEnum):
    SYSTEM_ONLY = 0
    FULL = 1
    NONE = 2

class UserDataAccountStoreAccessType(enum.IntEnum):
    ALL_ACCOUNTS_READ_ONLY = 0
    APP_ACCOUNTS_READ_WRITE = 1

Self = typing.TypeVar('Self')

class UserDataAccount(_winrt.Object):
    user_display_name: str
    other_app_read_access: UserDataAccountOtherAppReadAccess
    icon: typing.Optional[winsdk.windows.storage.streams.IRandomAccessStreamReference]
    device_account_type_id: str
    id: str
    package_family_name: str
    is_protected_under_lock: _winrt.Boolean
    enterprise_id: str
    display_name: str
    explict_read_access_package_family_names: typing.Optional[winsdk.windows.foundation.collections.IVector[str]]
    can_show_create_contact_group: _winrt.Boolean
    provider_properties: typing.Optional[winsdk.windows.foundation.collections.IPropertySet]
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccount: ...
    def delete_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def find_appointment_calendars_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.appointments.AppointmentCalendar]]: ...
    def find_contact_annotation_lists_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.contacts.ContactAnnotationList]]: ...
    def find_contact_groups_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.contacts.ContactGroup]]: ...
    def find_contact_lists_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.contacts.ContactList]]: ...
    def find_email_mailboxes_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.email.EmailMailbox]]: ...
    def find_user_data_task_lists_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[winsdk.windows.applicationmodel.userdatatasks.UserDataTaskList]]: ...
    def save_async(self) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    def try_show_create_contact_group_async(self) -> winsdk.windows.foundation.IAsyncOperation[str]: ...

class UserDataAccountManager(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountManager: ...
    @staticmethod
    def get_for_user(user: typing.Optional[winsdk.windows.system.User]) -> typing.Optional[UserDataAccountManagerForUser]: ...
    @staticmethod
    def request_store_async(store_access_type: UserDataAccountStoreAccessType) -> winsdk.windows.foundation.IAsyncOperation[UserDataAccountStore]: ...
    @staticmethod
    def show_account_error_resolver_async(id: str) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @staticmethod
    def show_account_settings_async(id: str) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...
    @staticmethod
    def show_add_account_async(content_kinds: UserDataAccountContentKinds) -> winsdk.windows.foundation.IAsyncOperation[str]: ...

class UserDataAccountManagerForUser(_winrt.Object):
    user: typing.Optional[winsdk.windows.system.User]
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountManagerForUser: ...
    def request_store_async(self, store_access_type: UserDataAccountStoreAccessType) -> winsdk.windows.foundation.IAsyncOperation[UserDataAccountStore]: ...

class UserDataAccountStore(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountStore: ...
    @typing.overload
    def create_account_async(self, user_display_name: str) -> winsdk.windows.foundation.IAsyncOperation[UserDataAccount]: ...
    @typing.overload
    def create_account_async(self, user_display_name: str, package_relative_app_id: str) -> winsdk.windows.foundation.IAsyncOperation[UserDataAccount]: ...
    @typing.overload
    def create_account_async(self, user_display_name: str, package_relative_app_id: str, enterprise_id: str) -> winsdk.windows.foundation.IAsyncOperation[UserDataAccount]: ...
    def find_accounts_async(self) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[UserDataAccount]]: ...
    def get_account_async(self, id: str) -> winsdk.windows.foundation.IAsyncOperation[UserDataAccount]: ...
    def add_store_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[UserDataAccountStore, UserDataAccountStoreChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    def remove_store_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class UserDataAccountStoreChangedEventArgs(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> UserDataAccountStoreChangedEventArgs: ...
    def get_deferral(self) -> typing.Optional[winsdk.windows.foundation.Deferral]: ...

