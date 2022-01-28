# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Media.ContentRestrictions")

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

class ContentAccessRestrictionLevel(enum.IntEnum):
    ALLOW = 0
    WARN = 1
    BLOCK = 2
    HIDE = 3

class RatedContentCategory(enum.IntEnum):
    GENERAL = 0
    APPLICATION = 1
    GAME = 2
    MOVIE = 3
    TELEVISION = 4
    MUSIC = 5

ContentRestrictionsBrowsePolicy = _ns_module.ContentRestrictionsBrowsePolicy
RatedContentDescription = _ns_module.RatedContentDescription
RatedContentRestrictions = _ns_module.RatedContentRestrictions
