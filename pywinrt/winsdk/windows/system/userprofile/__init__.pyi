# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

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
    import winsdk.windows.globalization
except Exception:
    pass

try:
    import winsdk.windows.storage
except Exception:
    pass

try:
    import winsdk.windows.system
except Exception:
    pass

class AdvertisingManager(_winrt.Object):
    ...
    advertising_id: str
    def get_for_user(user: winsdk.windows.system.User) -> AdvertisingManagerForUser:
        ...

class AdvertisingManagerForUser(_winrt.Object):
    ...
    advertising_id: str
    user: winsdk.windows.system.User

class AssignedAccessSettings(_winrt.Object):
    ...
    is_enabled: _winrt.Boolean
    is_single_app_kiosk_mode: _winrt.Boolean
    user: winsdk.windows.system.User
    def get_default() -> AssignedAccessSettings:
        ...
    def get_for_user(user: winsdk.windows.system.User) -> AssignedAccessSettings:
        ...

class DiagnosticsSettings(_winrt.Object):
    ...
    can_use_diagnostics_to_tailor_experiences: _winrt.Boolean
    user: winsdk.windows.system.User
    def get_default() -> DiagnosticsSettings:
        ...
    def get_for_user(user: winsdk.windows.system.User) -> DiagnosticsSettings:
        ...

class FirstSignInSettings(winsdk.windows.foundation.collections.IMapView[str, _winrt.Object], winsdk.windows.foundation.collections.IIterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]], _winrt.Object):
    ...
    size: _winrt.UInt32
    def first() -> winsdk.windows.foundation.collections.IIterator[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]:
        ...
    def get_default() -> FirstSignInSettings:
        ...
    def has_key(key: str) -> _winrt.Boolean:
        ...
    def lookup(key: str) -> _winrt.Object:
        ...
    def split() -> typing.Tuple[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object], winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]:
        ...

class GlobalizationPreferences(_winrt.Object):
    ...
    calendars: winsdk.windows.foundation.collections.IVectorView[str]
    clocks: winsdk.windows.foundation.collections.IVectorView[str]
    currencies: winsdk.windows.foundation.collections.IVectorView[str]
    home_geographic_region: str
    languages: winsdk.windows.foundation.collections.IVectorView[str]
    week_starts_on: winsdk.windows.globalization.DayOfWeek
    def get_for_user(user: winsdk.windows.system.User) -> GlobalizationPreferencesForUser:
        ...
    def try_set_home_geographic_region(region: str) -> _winrt.Boolean:
        ...
    def try_set_languages(language_tags: typing.Iterable[str]) -> _winrt.Boolean:
        ...

class GlobalizationPreferencesForUser(_winrt.Object):
    ...
    calendars: winsdk.windows.foundation.collections.IVectorView[str]
    clocks: winsdk.windows.foundation.collections.IVectorView[str]
    currencies: winsdk.windows.foundation.collections.IVectorView[str]
    home_geographic_region: str
    languages: winsdk.windows.foundation.collections.IVectorView[str]
    user: winsdk.windows.system.User
    week_starts_on: winsdk.windows.globalization.DayOfWeek

class UserProfilePersonalizationSettings(_winrt.Object):
    ...
    current: UserProfilePersonalizationSettings
    def is_supported() -> _winrt.Boolean:
        ...
    def try_set_lock_screen_image_async(image_file: winsdk.windows.storage.StorageFile) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...
    def try_set_wallpaper_image_async(image_file: winsdk.windows.storage.StorageFile) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]:
        ...

