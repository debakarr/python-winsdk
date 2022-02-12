# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.contacts
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

class AddContactResult(enum.IntEnum):
    ADDED = 0
    ALREADY_ADDED = 1
    UNAVAILABLE = 2

class ContactPickerUI(_winrt.Object):
    desired_fields: winsdk.windows.foundation.collections.IVectorView[str]
    selection_mode: winsdk.windows.applicationmodel.contacts.ContactSelectionMode
    desired_fields_with_contact_field_type: winsdk.windows.foundation.collections.IVector[winsdk.windows.applicationmodel.contacts.ContactFieldType]
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactPickerUI: ...
    @typing.overload
    def add_contact(self, contact: winsdk.windows.applicationmodel.contacts.Contact) -> AddContactResult: ...
    @typing.overload
    def add_contact(self, id: str, contact: winsdk.windows.applicationmodel.contacts.Contact) -> AddContactResult: ...
    @typing.overload
    def contains_contact(self, id: str) -> _winrt.Boolean: ...
    @typing.overload
    def remove_contact(self, id: str) -> None: ...
    @typing.overload
    def add_contact_removed(self, handler: winsdk.windows.foundation.TypedEventHandler[ContactPickerUI, ContactRemovedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_contact_removed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class ContactRemovedEventArgs(_winrt.Object):
    id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> ContactRemovedEventArgs: ...

