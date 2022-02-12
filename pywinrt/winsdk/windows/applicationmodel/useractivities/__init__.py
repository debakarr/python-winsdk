# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.ApplicationModel.UserActivities")

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
    import winsdk.windows.ui
except Exception:
    pass

try:
    import winsdk.windows.ui.shell
except Exception:
    pass

class UserActivityState(enum.IntEnum):
    NEW = 0
    PUBLISHED = 1

UserActivity = _ns_module.UserActivity
UserActivityAttribution = _ns_module.UserActivityAttribution
UserActivityChannel = _ns_module.UserActivityChannel
UserActivityContentInfo = _ns_module.UserActivityContentInfo
UserActivityRequest = _ns_module.UserActivityRequest
UserActivityRequestManager = _ns_module.UserActivityRequestManager
UserActivityRequestedEventArgs = _ns_module.UserActivityRequestedEventArgs
UserActivitySession = _ns_module.UserActivitySession
UserActivitySessionHistoryItem = _ns_module.UserActivitySessionHistoryItem
UserActivityVisualElements = _ns_module.UserActivityVisualElements
IUserActivityContentInfo = _ns_module.IUserActivityContentInfo
