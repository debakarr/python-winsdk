# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Services.Cortana")

try:
    import winsdk.windows.applicationmodel.datatransfer
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

class CortanaPermission(enum.IntEnum):
    BROWSING_HISTORY = 0
    CALENDAR = 1
    CALL_HISTORY = 2
    CONTACTS = 3
    EMAIL = 4
    INPUT_PERSONALIZATION = 5
    LOCATION = 6
    MESSAGING = 7
    MICROPHONE = 8
    PERSONALIZATION = 9
    PHONE_CALL = 10

class CortanaPermissionsChangeResult(enum.IntEnum):
    SUCCESS = 0
    UNAVAILABLE = 1
    DISABLED_BY_POLICY = 2

CortanaActionableInsights = _ns_module.CortanaActionableInsights
CortanaActionableInsightsOptions = _ns_module.CortanaActionableInsightsOptions
CortanaPermissionsManager = _ns_module.CortanaPermissionsManager
CortanaSettings = _ns_module.CortanaSettings
