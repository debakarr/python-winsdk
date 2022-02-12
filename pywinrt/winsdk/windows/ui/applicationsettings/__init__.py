# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.UI.ApplicationSettings")

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

try:
    import winsdk.windows.system
except Exception:
    pass

try:
    import winsdk.windows.ui.popups
except Exception:
    pass

class SupportedWebAccountActions(enum.IntFlag):
    NONE = 0
    RECONNECT = 0x1
    REMOVE = 0x2
    VIEW_DETAILS = 0x4
    MANAGE = 0x8
    MORE = 0x10

class WebAccountAction(enum.IntEnum):
    RECONNECT = 0
    REMOVE = 1
    VIEW_DETAILS = 2
    MANAGE = 3
    MORE = 4

AccountsSettingsPane = _ns_module.AccountsSettingsPane
AccountsSettingsPaneCommandsRequestedEventArgs = _ns_module.AccountsSettingsPaneCommandsRequestedEventArgs
AccountsSettingsPaneEventDeferral = _ns_module.AccountsSettingsPaneEventDeferral
CredentialCommand = _ns_module.CredentialCommand
SettingsCommand = _ns_module.SettingsCommand
WebAccountCommand = _ns_module.WebAccountCommand
WebAccountInvokedArgs = _ns_module.WebAccountInvokedArgs
WebAccountProviderCommand = _ns_module.WebAccountProviderCommand
