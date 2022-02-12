# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

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
    advertising_id: str
    @staticmethod
    def _from(obj: _winrt.Object) -> AdvertisingManager: ...
    @typing.overload
    @staticmethod
    def get_for_user(user: winsdk.windows.system.User) -> AdvertisingManagerForUser: ...

class AdvertisingManagerForUser(_winrt.Object):
    advertising_id: str
    user: winsdk.windows.system.User
    @staticmethod
    def _from(obj: _winrt.Object) -> AdvertisingManagerForUser: ...

class AssignedAccessSettings(_winrt.Object):
    is_enabled: _winrt.Boolean
    is_single_app_kiosk_mode: _winrt.Boolean
    user: winsdk.windows.system.User
    @staticmethod
    def _from(obj: _winrt.Object) -> AssignedAccessSettings: ...
    @typing.overload
    @staticmethod
    def get_default() -> AssignedAccessSettings: ...
    @typing.overload
    @staticmethod
    def get_for_user(user: winsdk.windows.system.User) -> AssignedAccessSettings: ...

class DiagnosticsSettings(_winrt.Object):
    can_use_diagnostics_to_tailor_experiences: _winrt.Boolean
    user: winsdk.windows.system.User
    @staticmethod
    def _from(obj: _winrt.Object) -> DiagnosticsSettings: ...
    @typing.overload
    @staticmethod
    def get_default() -> DiagnosticsSettings: ...
    @typing.overload
    @staticmethod
    def get_for_user(user: winsdk.windows.system.User) -> DiagnosticsSettings: ...

class FirstSignInSettings(winsdk.windows.foundation.collections.IMapView[str, _winrt.Object], winsdk.windows.foundation.collections.IIterable[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]], _winrt.Object):
    size: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> FirstSignInSettings: ...
    @typing.overload
    def first(self) -> winsdk.windows.foundation.collections.IIterator[winsdk.windows.foundation.collections.IKeyValuePair[str, _winrt.Object]]: ...
    @typing.overload
    @staticmethod
    def get_default() -> FirstSignInSettings: ...
    @typing.overload
    def has_key(self, key: str) -> _winrt.Boolean: ...
    @typing.overload
    def lookup(self, key: str) -> _winrt.Object: ...
    @typing.overload
    def split(self, ) -> typing.Tuple[winsdk.windows.foundation.collections.IMapView[str, _winrt.Object], winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]]: ...

class GlobalizationPreferences(_winrt.Object):
    calendars: winsdk.windows.foundation.collections.IVectorView[str]
    clocks: winsdk.windows.foundation.collections.IVectorView[str]
    currencies: winsdk.windows.foundation.collections.IVectorView[str]
    home_geographic_region: str
    languages: winsdk.windows.foundation.collections.IVectorView[str]
    week_starts_on: winsdk.windows.globalization.DayOfWeek
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalizationPreferences: ...
    @typing.overload
    @staticmethod
    def get_for_user(user: winsdk.windows.system.User) -> GlobalizationPreferencesForUser: ...
    @typing.overload
    @staticmethod
    def try_set_home_geographic_region(region: str) -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def try_set_languages(language_tags: typing.Iterable[str]) -> _winrt.Boolean: ...

class GlobalizationPreferencesForUser(_winrt.Object):
    calendars: winsdk.windows.foundation.collections.IVectorView[str]
    clocks: winsdk.windows.foundation.collections.IVectorView[str]
    currencies: winsdk.windows.foundation.collections.IVectorView[str]
    home_geographic_region: str
    languages: winsdk.windows.foundation.collections.IVectorView[str]
    user: winsdk.windows.system.User
    week_starts_on: winsdk.windows.globalization.DayOfWeek
    @staticmethod
    def _from(obj: _winrt.Object) -> GlobalizationPreferencesForUser: ...

class UserProfilePersonalizationSettings(_winrt.Object):
    current: UserProfilePersonalizationSettings
    @staticmethod
    def _from(obj: _winrt.Object) -> UserProfilePersonalizationSettings: ...
    @typing.overload
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    @typing.overload
    def try_set_lock_screen_image_async(self, image_file: winsdk.windows.storage.StorageFile) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def try_set_wallpaper_image_async(self, image_file: winsdk.windows.storage.StorageFile) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

