# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.UserDataAccounts")

try:
    import winsdk.windows.applicationmodel.appointments
except Exception:
    pass

try:
    import winsdk.windows.applicationmodel.contacts
except Exception:
    pass

try:
    import winsdk.windows.applicationmodel.email
except Exception:
    pass

try:
    import winsdk.windows.applicationmodel.userdatatasks
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
    import winsdk.windows.storage.streams
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

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

UserDataAccount = _ns_module.UserDataAccount
UserDataAccountManager = _ns_module.UserDataAccountManager
UserDataAccountManagerForUser = _ns_module.UserDataAccountManagerForUser
UserDataAccountStore = _ns_module.UserDataAccountStore
UserDataAccountStoreChangedEventArgs = _ns_module.UserDataAccountStoreChangedEventArgs
