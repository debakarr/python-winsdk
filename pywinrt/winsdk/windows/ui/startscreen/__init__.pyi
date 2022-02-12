# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel.core
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
    import winsdk.windows.perception.spatial
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
    import winsdk.windows.ui.popups
except Exception:
    pass

class ForegroundText(enum.IntEnum):
    DARK = 0
    LIGHT = 1

class JumpListItemKind(enum.IntEnum):
    ARGUMENTS = 0
    SEPARATOR = 1

class JumpListSystemGroupKind(enum.IntEnum):
    NONE = 0
    FREQUENT = 1
    RECENT = 2

class TileMixedRealityModelActivationBehavior(enum.IntEnum):
    DEFAULT = 0
    NONE = 1

class TileOptions(enum.IntFlag):
    NONE = 0
    SHOW_NAME_ON_LOGO = 0x1
    SHOW_NAME_ON_WIDE_LOGO = 0x2
    COPY_ON_DEPLOYMENT = 0x4

class TileSize(enum.IntEnum):
    DEFAULT = 0
    SQUARE30X30 = 1
    SQUARE70X70 = 2
    SQUARE150X150 = 3
    WIDE310X150 = 4
    SQUARE310X310 = 5
    SQUARE71X71 = 6
    SQUARE44X44 = 7

class JumpList(_winrt.Object):
    system_group_kind: JumpListSystemGroupKind
    items: winsdk.windows.foundation.collections.IVector[JumpListItem]
    @staticmethod
    def _from(obj: _winrt.Object) -> JumpList: ...
    @typing.overload
    @staticmethod
    def is_supported() -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def load_current_async() -> winsdk.windows.foundation.IAsyncOperation[JumpList]: ...
    @typing.overload
    def save_async(self) -> winsdk.windows.foundation.IAsyncAction: ...

class JumpListItem(_winrt.Object):
    logo: winsdk.windows.foundation.Uri
    group_name: str
    display_name: str
    description: str
    arguments: str
    kind: JumpListItemKind
    removed_by_user: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> JumpListItem: ...
    @typing.overload
    @staticmethod
    def create_separator() -> JumpListItem: ...
    @typing.overload
    @staticmethod
    def create_with_arguments(arguments: str, display_name: str) -> JumpListItem: ...

class SecondaryTile(_winrt.Object):
    short_name: str
    logo: winsdk.windows.foundation.Uri
    tile_id: str
    lock_screen_display_badge_and_tile_text: _winrt.Boolean
    lock_screen_badge_logo: winsdk.windows.foundation.Uri
    arguments: str
    foreground_text: ForegroundText
    display_name: str
    background_color: winsdk.windows.ui.Color
    wide_logo: winsdk.windows.foundation.Uri
    tile_options: TileOptions
    small_logo: winsdk.windows.foundation.Uri
    roaming_enabled: _winrt.Boolean
    phonetic_name: str
    visual_elements: SecondaryTileVisualElements
    @staticmethod
    def _from(obj: _winrt.Object) -> SecondaryTile: ...
    @typing.overload
    def __init__(self, tile_id: str, display_name: str, arguments: str, square150x150_logo: winsdk.windows.foundation.Uri, desired_size: TileSize) -> None: ...
    @typing.overload
    def __init__(self, tile_id: str, short_name: str, display_name: str, arguments: str, tile_options: TileOptions, logo_reference: winsdk.windows.foundation.Uri) -> None: ...
    @typing.overload
    def __init__(self, tile_id: str, short_name: str, display_name: str, arguments: str, tile_options: TileOptions, logo_reference: winsdk.windows.foundation.Uri, wide_logo_reference: winsdk.windows.foundation.Uri) -> None: ...
    @typing.overload
    def __init__(self, tile_id: str) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    @staticmethod
    def exists(tile_id: str) -> _winrt.Boolean: ...
    @typing.overload
    @staticmethod
    def find_all_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[SecondaryTile]]: ...
    @typing.overload
    @staticmethod
    def find_all_async(application_id: str) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[SecondaryTile]]: ...
    @typing.overload
    @staticmethod
    def find_all_for_package_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[SecondaryTile]]: ...
    @typing.overload
    def request_create_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_create_async(self, invocation_point: winsdk.windows.foundation.Point) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_create_for_selection_async(self, selection: winsdk.windows.foundation.Rect) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_create_for_selection_async(self, selection: winsdk.windows.foundation.Rect, preferred_placement: winsdk.windows.ui.popups.Placement) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_delete_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_delete_async(self, invocation_point: winsdk.windows.foundation.Point) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_delete_for_selection_async(self, selection: winsdk.windows.foundation.Rect) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def request_delete_for_selection_async(self, selection: winsdk.windows.foundation.Rect, preferred_placement: winsdk.windows.ui.popups.Placement) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def update_async(self) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def add_visual_elements_requested(self, handler: winsdk.windows.foundation.TypedEventHandler[SecondaryTile, VisualElementsRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_visual_elements_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class SecondaryTileVisualElements(_winrt.Object):
    square150x150_logo: winsdk.windows.foundation.Uri
    show_name_on_wide310x150_logo: _winrt.Boolean
    show_name_on_square310x310_logo: _winrt.Boolean
    show_name_on_square150x150_logo: _winrt.Boolean
    foreground_text: ForegroundText
    background_color: winsdk.windows.ui.Color
    wide310x150_logo: winsdk.windows.foundation.Uri
    square70x70_logo: winsdk.windows.foundation.Uri
    square310x310_logo: winsdk.windows.foundation.Uri
    square30x30_logo: winsdk.windows.foundation.Uri
    square71x71_logo: winsdk.windows.foundation.Uri
    square44x44_logo: winsdk.windows.foundation.Uri
    mixed_reality_model: TileMixedRealityModel
    @staticmethod
    def _from(obj: _winrt.Object) -> SecondaryTileVisualElements: ...

class StartScreenManager(_winrt.Object):
    user: winsdk.windows.system.User
    @staticmethod
    def _from(obj: _winrt.Object) -> StartScreenManager: ...
    @typing.overload
    def contains_app_list_entry_async(self, app_list_entry: winsdk.windows.applicationmodel.core.AppListEntry) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def contains_secondary_tile_async(self, tile_id: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    @staticmethod
    def get_default() -> StartScreenManager: ...
    @typing.overload
    @staticmethod
    def get_for_user(user: winsdk.windows.system.User) -> StartScreenManager: ...
    @typing.overload
    def request_add_app_list_entry_async(self, app_list_entry: winsdk.windows.applicationmodel.core.AppListEntry) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...
    @typing.overload
    def supports_app_list_entry(self, app_list_entry: winsdk.windows.applicationmodel.core.AppListEntry) -> _winrt.Boolean: ...
    @typing.overload
    def try_remove_secondary_tile_async(self, tile_id: str) -> winsdk.windows.foundation.IAsyncOperation[_winrt.Boolean]: ...

class TileMixedRealityModel(_winrt.Object):
    uri: winsdk.windows.foundation.Uri
    bounding_box: typing.Optional[winsdk.windows.perception.spatial.SpatialBoundingBox]
    activation_behavior: TileMixedRealityModelActivationBehavior
    @staticmethod
    def _from(obj: _winrt.Object) -> TileMixedRealityModel: ...

class VisualElementsRequest(_winrt.Object):
    alternate_visual_elements: winsdk.windows.foundation.collections.IVectorView[SecondaryTileVisualElements]
    deadline: winsdk.windows.foundation.DateTime
    visual_elements: SecondaryTileVisualElements
    @staticmethod
    def _from(obj: _winrt.Object) -> VisualElementsRequest: ...
    @typing.overload
    def get_deferral(self) -> VisualElementsRequestDeferral: ...

class VisualElementsRequestDeferral(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> VisualElementsRequestDeferral: ...
    @typing.overload
    def complete(self) -> None: ...

class VisualElementsRequestedEventArgs(_winrt.Object):
    request: VisualElementsRequest
    @staticmethod
    def _from(obj: _winrt.Object) -> VisualElementsRequestedEventArgs: ...

