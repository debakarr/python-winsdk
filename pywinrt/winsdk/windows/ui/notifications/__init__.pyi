# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.applicationmodel
except Exception:
    pass

try:
    import winsdk.windows.data.xml.dom
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
    import winsdk.windows.system
except Exception:
    pass

class AdaptiveNotificationContentKind(enum.IntEnum):
    TEXT = 0

class BadgeTemplateType(enum.IntEnum):
    BADGE_GLYPH = 0
    BADGE_NUMBER = 1

class NotificationKinds(enum.IntFlag):
    UNKNOWN = 0
    TOAST = 0x1

class NotificationMirroring(enum.IntEnum):
    ALLOWED = 0
    DISABLED = 1

class NotificationSetting(enum.IntEnum):
    ENABLED = 0
    DISABLED_FOR_APPLICATION = 1
    DISABLED_FOR_USER = 2
    DISABLED_BY_GROUP_POLICY = 3
    DISABLED_BY_MANIFEST = 4

class NotificationUpdateResult(enum.IntEnum):
    SUCCEEDED = 0
    FAILED = 1
    NOTIFICATION_NOT_FOUND = 2

class PeriodicUpdateRecurrence(enum.IntEnum):
    HALF_HOUR = 0
    HOUR = 1
    SIX_HOURS = 2
    TWELVE_HOURS = 3
    DAILY = 4

class TileFlyoutTemplateType(enum.IntEnum):
    TILE_FLYOUT_TEMPLATE01 = 0

class TileTemplateType(enum.IntEnum):
    TILE_SQUARE_IMAGE = 0
    TILE_SQUARE_BLOCK = 1
    TILE_SQUARE_TEXT01 = 2
    TILE_SQUARE_TEXT02 = 3
    TILE_SQUARE_TEXT03 = 4
    TILE_SQUARE_TEXT04 = 5
    TILE_SQUARE_PEEK_IMAGE_AND_TEXT01 = 6
    TILE_SQUARE_PEEK_IMAGE_AND_TEXT02 = 7
    TILE_SQUARE_PEEK_IMAGE_AND_TEXT03 = 8
    TILE_SQUARE_PEEK_IMAGE_AND_TEXT04 = 9
    TILE_WIDE_IMAGE = 10
    TILE_WIDE_IMAGE_COLLECTION = 11
    TILE_WIDE_IMAGE_AND_TEXT01 = 12
    TILE_WIDE_IMAGE_AND_TEXT02 = 13
    TILE_WIDE_BLOCK_AND_TEXT01 = 14
    TILE_WIDE_BLOCK_AND_TEXT02 = 15
    TILE_WIDE_PEEK_IMAGE_COLLECTION01 = 16
    TILE_WIDE_PEEK_IMAGE_COLLECTION02 = 17
    TILE_WIDE_PEEK_IMAGE_COLLECTION03 = 18
    TILE_WIDE_PEEK_IMAGE_COLLECTION04 = 19
    TILE_WIDE_PEEK_IMAGE_COLLECTION05 = 20
    TILE_WIDE_PEEK_IMAGE_COLLECTION06 = 21
    TILE_WIDE_PEEK_IMAGE_AND_TEXT01 = 22
    TILE_WIDE_PEEK_IMAGE_AND_TEXT02 = 23
    TILE_WIDE_PEEK_IMAGE01 = 24
    TILE_WIDE_PEEK_IMAGE02 = 25
    TILE_WIDE_PEEK_IMAGE03 = 26
    TILE_WIDE_PEEK_IMAGE04 = 27
    TILE_WIDE_PEEK_IMAGE05 = 28
    TILE_WIDE_PEEK_IMAGE06 = 29
    TILE_WIDE_SMALL_IMAGE_AND_TEXT01 = 30
    TILE_WIDE_SMALL_IMAGE_AND_TEXT02 = 31
    TILE_WIDE_SMALL_IMAGE_AND_TEXT03 = 32
    TILE_WIDE_SMALL_IMAGE_AND_TEXT04 = 33
    TILE_WIDE_SMALL_IMAGE_AND_TEXT05 = 34
    TILE_WIDE_TEXT01 = 35
    TILE_WIDE_TEXT02 = 36
    TILE_WIDE_TEXT03 = 37
    TILE_WIDE_TEXT04 = 38
    TILE_WIDE_TEXT05 = 39
    TILE_WIDE_TEXT06 = 40
    TILE_WIDE_TEXT07 = 41
    TILE_WIDE_TEXT08 = 42
    TILE_WIDE_TEXT09 = 43
    TILE_WIDE_TEXT10 = 44
    TILE_WIDE_TEXT11 = 45
    TILE_SQUARE150X150_IMAGE = 0
    TILE_SQUARE150X150_BLOCK = 1
    TILE_SQUARE150X150_TEXT01 = 2
    TILE_SQUARE150X150_TEXT02 = 3
    TILE_SQUARE150X150_TEXT03 = 4
    TILE_SQUARE150X150_TEXT04 = 5
    TILE_SQUARE150X150_PEEK_IMAGE_AND_TEXT01 = 6
    TILE_SQUARE150X150_PEEK_IMAGE_AND_TEXT02 = 7
    TILE_SQUARE150X150_PEEK_IMAGE_AND_TEXT03 = 8
    TILE_SQUARE150X150_PEEK_IMAGE_AND_TEXT04 = 9
    TILE_WIDE310X150_IMAGE = 10
    TILE_WIDE310X150_IMAGE_COLLECTION = 11
    TILE_WIDE310X150_IMAGE_AND_TEXT01 = 12
    TILE_WIDE310X150_IMAGE_AND_TEXT02 = 13
    TILE_WIDE310X150_BLOCK_AND_TEXT01 = 14
    TILE_WIDE310X150_BLOCK_AND_TEXT02 = 15
    TILE_WIDE310X150_PEEK_IMAGE_COLLECTION01 = 16
    TILE_WIDE310X150_PEEK_IMAGE_COLLECTION02 = 17
    TILE_WIDE310X150_PEEK_IMAGE_COLLECTION03 = 18
    TILE_WIDE310X150_PEEK_IMAGE_COLLECTION04 = 19
    TILE_WIDE310X150_PEEK_IMAGE_COLLECTION05 = 20
    TILE_WIDE310X150_PEEK_IMAGE_COLLECTION06 = 21
    TILE_WIDE310X150_PEEK_IMAGE_AND_TEXT01 = 22
    TILE_WIDE310X150_PEEK_IMAGE_AND_TEXT02 = 23
    TILE_WIDE310X150_PEEK_IMAGE01 = 24
    TILE_WIDE310X150_PEEK_IMAGE02 = 25
    TILE_WIDE310X150_PEEK_IMAGE03 = 26
    TILE_WIDE310X150_PEEK_IMAGE04 = 27
    TILE_WIDE310X150_PEEK_IMAGE05 = 28
    TILE_WIDE310X150_PEEK_IMAGE06 = 29
    TILE_WIDE310X150_SMALL_IMAGE_AND_TEXT01 = 30
    TILE_WIDE310X150_SMALL_IMAGE_AND_TEXT02 = 31
    TILE_WIDE310X150_SMALL_IMAGE_AND_TEXT03 = 32
    TILE_WIDE310X150_SMALL_IMAGE_AND_TEXT04 = 33
    TILE_WIDE310X150_SMALL_IMAGE_AND_TEXT05 = 34
    TILE_WIDE310X150_TEXT01 = 35
    TILE_WIDE310X150_TEXT02 = 36
    TILE_WIDE310X150_TEXT03 = 37
    TILE_WIDE310X150_TEXT04 = 38
    TILE_WIDE310X150_TEXT05 = 39
    TILE_WIDE310X150_TEXT06 = 40
    TILE_WIDE310X150_TEXT07 = 41
    TILE_WIDE310X150_TEXT08 = 42
    TILE_WIDE310X150_TEXT09 = 43
    TILE_WIDE310X150_TEXT10 = 44
    TILE_WIDE310X150_TEXT11 = 45
    TILE_SQUARE310X310_BLOCK_AND_TEXT01 = 46
    TILE_SQUARE310X310_BLOCK_AND_TEXT02 = 47
    TILE_SQUARE310X310_IMAGE = 48
    TILE_SQUARE310X310_IMAGE_AND_TEXT01 = 49
    TILE_SQUARE310X310_IMAGE_AND_TEXT02 = 50
    TILE_SQUARE310X310_IMAGE_AND_TEXT_OVERLAY01 = 51
    TILE_SQUARE310X310_IMAGE_AND_TEXT_OVERLAY02 = 52
    TILE_SQUARE310X310_IMAGE_AND_TEXT_OVERLAY03 = 53
    TILE_SQUARE310X310_IMAGE_COLLECTION_AND_TEXT01 = 54
    TILE_SQUARE310X310_IMAGE_COLLECTION_AND_TEXT02 = 55
    TILE_SQUARE310X310_IMAGE_COLLECTION = 56
    TILE_SQUARE310X310_SMALL_IMAGES_AND_TEXT_LIST01 = 57
    TILE_SQUARE310X310_SMALL_IMAGES_AND_TEXT_LIST02 = 58
    TILE_SQUARE310X310_SMALL_IMAGES_AND_TEXT_LIST03 = 59
    TILE_SQUARE310X310_SMALL_IMAGES_AND_TEXT_LIST04 = 60
    TILE_SQUARE310X310_TEXT01 = 61
    TILE_SQUARE310X310_TEXT02 = 62
    TILE_SQUARE310X310_TEXT03 = 63
    TILE_SQUARE310X310_TEXT04 = 64
    TILE_SQUARE310X310_TEXT05 = 65
    TILE_SQUARE310X310_TEXT06 = 66
    TILE_SQUARE310X310_TEXT07 = 67
    TILE_SQUARE310X310_TEXT08 = 68
    TILE_SQUARE310X310_TEXT_LIST01 = 69
    TILE_SQUARE310X310_TEXT_LIST02 = 70
    TILE_SQUARE310X310_TEXT_LIST03 = 71
    TILE_SQUARE310X310_SMALL_IMAGE_AND_TEXT01 = 72
    TILE_SQUARE310X310_SMALL_IMAGES_AND_TEXT_LIST05 = 73
    TILE_SQUARE310X310_TEXT09 = 74
    TILE_SQUARE71X71_ICON_WITH_BADGE = 75
    TILE_SQUARE150X150_ICON_WITH_BADGE = 76
    TILE_WIDE310X150_ICON_WITH_BADGE_AND_TEXT = 77
    TILE_SQUARE71X71_IMAGE = 78
    TILE_TALL150X310_IMAGE = 79

class ToastDismissalReason(enum.IntEnum):
    USER_CANCELED = 0
    APPLICATION_HIDDEN = 1
    TIMED_OUT = 2

class ToastHistoryChangedType(enum.IntEnum):
    CLEARED = 0
    REMOVED = 1
    EXPIRED = 2
    ADDED = 3

class ToastNotificationPriority(enum.IntEnum):
    DEFAULT = 0
    HIGH = 1

class ToastTemplateType(enum.IntEnum):
    TOAST_IMAGE_AND_TEXT01 = 0
    TOAST_IMAGE_AND_TEXT02 = 1
    TOAST_IMAGE_AND_TEXT03 = 2
    TOAST_IMAGE_AND_TEXT04 = 3
    TOAST_TEXT01 = 4
    TOAST_TEXT02 = 5
    TOAST_TEXT03 = 6
    TOAST_TEXT04 = 7

class UserNotificationChangedKind(enum.IntEnum):
    ADDED = 0
    REMOVED = 1

class AdaptiveNotificationText(IAdaptiveNotificationContent, _winrt.Object):
    ...
    hints: winsdk.windows.foundation.collections.IMap[str, str]
    kind: AdaptiveNotificationContentKind
    text: str
    language: str
    def __init__(self, ) -> None:
        ...

class BadgeNotification(_winrt.Object):
    ...
    expiration_time: typing.Optional[winsdk.windows.foundation.DateTime]
    content: winsdk.windows.data.xml.dom.XmlDocument
    def __init__(self, content: winsdk.windows.data.xml.dom.XmlDocument) -> None:
        ...

class BadgeUpdateManager(_winrt.Object):
    ...
    def create_badge_updater_for_application() -> BadgeUpdater:
        ...
    def create_badge_updater_for_application(application_id: str) -> BadgeUpdater:
        ...
    def create_badge_updater_for_secondary_tile(tile_id: str) -> BadgeUpdater:
        ...
    def get_for_user(user: winsdk.windows.system.User) -> BadgeUpdateManagerForUser:
        ...
    def get_template_content(type: BadgeTemplateType) -> winsdk.windows.data.xml.dom.XmlDocument:
        ...

class BadgeUpdateManagerForUser(_winrt.Object):
    ...
    user: winsdk.windows.system.User
    def create_badge_updater_for_application() -> BadgeUpdater:
        ...
    def create_badge_updater_for_application(application_id: str) -> BadgeUpdater:
        ...
    def create_badge_updater_for_secondary_tile(tile_id: str) -> BadgeUpdater:
        ...

class BadgeUpdater(_winrt.Object):
    ...
    def clear() -> None:
        ...
    def start_periodic_update(badge_content: winsdk.windows.foundation.Uri, requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def start_periodic_update(badge_content: winsdk.windows.foundation.Uri, start_time: winsdk.windows.foundation.DateTime, requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def stop_periodic_update() -> None:
        ...
    def update(notification: BadgeNotification) -> None:
        ...

class KnownAdaptiveNotificationHints(_winrt.Object):
    ...
    align: str
    max_lines: str
    min_lines: str
    style: str
    text_stacking: str
    wrap: str

class KnownAdaptiveNotificationTextStyles(_winrt.Object):
    ...
    base: str
    base_subtle: str
    body: str
    body_subtle: str
    caption: str
    caption_subtle: str
    header: str
    header_numeral: str
    header_numeral_subtle: str
    header_subtle: str
    subheader: str
    subheader_numeral: str
    subheader_numeral_subtle: str
    subheader_subtle: str
    subtitle: str
    subtitle_subtle: str
    title: str
    title_numeral: str
    title_subtle: str

class KnownNotificationBindings(_winrt.Object):
    ...
    toast_generic: str

class Notification(_winrt.Object):
    ...
    visual: NotificationVisual
    expiration_time: typing.Optional[winsdk.windows.foundation.DateTime]
    def __init__(self, ) -> None:
        ...

class NotificationBinding(_winrt.Object):
    ...
    template: str
    language: str
    hints: winsdk.windows.foundation.collections.IMap[str, str]
    def get_text_elements() -> winsdk.windows.foundation.collections.IVectorView[AdaptiveNotificationText]:
        ...

class NotificationData(_winrt.Object):
    ...
    sequence_number: _winrt.UInt32
    values: winsdk.windows.foundation.collections.IMap[str, str]
    def __init__(self, initial_values: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, str]], sequence_number: _winrt.UInt32) -> None:
        ...
    def __init__(self, initial_values: typing.Iterable[winsdk.windows.foundation.collections.IKeyValuePair[str, str]]) -> None:
        ...
    def __init__(self, ) -> None:
        ...

class NotificationVisual(_winrt.Object):
    ...
    language: str
    bindings: winsdk.windows.foundation.collections.IVector[NotificationBinding]
    def get_binding(template_name: str) -> NotificationBinding:
        ...

class ScheduledTileNotification(_winrt.Object):
    ...
    tag: str
    id: str
    expiration_time: typing.Optional[winsdk.windows.foundation.DateTime]
    content: winsdk.windows.data.xml.dom.XmlDocument
    delivery_time: winsdk.windows.foundation.DateTime
    def __init__(self, content: winsdk.windows.data.xml.dom.XmlDocument, delivery_time: winsdk.windows.foundation.DateTime) -> None:
        ...

class ScheduledToastNotification(_winrt.Object):
    ...
    id: str
    content: winsdk.windows.data.xml.dom.XmlDocument
    delivery_time: winsdk.windows.foundation.DateTime
    maximum_snooze_count: _winrt.UInt32
    snooze_interval: typing.Optional[winsdk.windows.foundation.TimeSpan]
    tag: str
    suppress_popup: _winrt.Boolean
    group: str
    remote_id: str
    notification_mirroring: NotificationMirroring
    expiration_time: typing.Optional[winsdk.windows.foundation.DateTime]
    def __init__(self, content: winsdk.windows.data.xml.dom.XmlDocument, delivery_time: winsdk.windows.foundation.DateTime) -> None:
        ...
    def __init__(self, content: winsdk.windows.data.xml.dom.XmlDocument, delivery_time: winsdk.windows.foundation.DateTime, snooze_interval: winsdk.windows.foundation.TimeSpan, maximum_snooze_count: _winrt.UInt32) -> None:
        ...

class ScheduledToastNotificationShowingEventArgs(_winrt.Object):
    ...
    cancel: _winrt.Boolean
    scheduled_toast_notification: ScheduledToastNotification
    def get_deferral() -> winsdk.windows.foundation.Deferral:
        ...

class ShownTileNotification(_winrt.Object):
    ...
    arguments: str

class TileFlyoutNotification(_winrt.Object):
    ...
    expiration_time: typing.Optional[winsdk.windows.foundation.DateTime]
    content: winsdk.windows.data.xml.dom.XmlDocument
    def __init__(self, content: winsdk.windows.data.xml.dom.XmlDocument) -> None:
        ...

class TileFlyoutUpdateManager(_winrt.Object):
    ...
    def create_tile_flyout_updater_for_application() -> TileFlyoutUpdater:
        ...
    def create_tile_flyout_updater_for_application(application_id: str) -> TileFlyoutUpdater:
        ...
    def create_tile_flyout_updater_for_secondary_tile(tile_id: str) -> TileFlyoutUpdater:
        ...
    def get_template_content(type: TileFlyoutTemplateType) -> winsdk.windows.data.xml.dom.XmlDocument:
        ...

class TileFlyoutUpdater(_winrt.Object):
    ...
    setting: NotificationSetting
    def clear() -> None:
        ...
    def start_periodic_update(tile_flyout_content: winsdk.windows.foundation.Uri, requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def start_periodic_update(tile_flyout_content: winsdk.windows.foundation.Uri, start_time: winsdk.windows.foundation.DateTime, requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def stop_periodic_update() -> None:
        ...
    def update(notification: TileFlyoutNotification) -> None:
        ...

class TileNotification(_winrt.Object):
    ...
    tag: str
    expiration_time: typing.Optional[winsdk.windows.foundation.DateTime]
    content: winsdk.windows.data.xml.dom.XmlDocument
    def __init__(self, content: winsdk.windows.data.xml.dom.XmlDocument) -> None:
        ...

class TileUpdateManager(_winrt.Object):
    ...
    def create_tile_updater_for_application() -> TileUpdater:
        ...
    def create_tile_updater_for_application(application_id: str) -> TileUpdater:
        ...
    def create_tile_updater_for_secondary_tile(tile_id: str) -> TileUpdater:
        ...
    def get_for_user(user: winsdk.windows.system.User) -> TileUpdateManagerForUser:
        ...
    def get_template_content(type: TileTemplateType) -> winsdk.windows.data.xml.dom.XmlDocument:
        ...

class TileUpdateManagerForUser(_winrt.Object):
    ...
    user: winsdk.windows.system.User
    def create_tile_updater_for_application(application_id: str) -> TileUpdater:
        ...
    def create_tile_updater_for_application_for_user() -> TileUpdater:
        ...
    def create_tile_updater_for_secondary_tile(tile_id: str) -> TileUpdater:
        ...

class TileUpdater(_winrt.Object):
    ...
    setting: NotificationSetting
    def add_to_schedule(scheduled_tile: ScheduledTileNotification) -> None:
        ...
    def clear() -> None:
        ...
    def enable_notification_queue(enable: _winrt.Boolean) -> None:
        ...
    def enable_notification_queue_for_square150x150(enable: _winrt.Boolean) -> None:
        ...
    def enable_notification_queue_for_square310x310(enable: _winrt.Boolean) -> None:
        ...
    def enable_notification_queue_for_wide310x150(enable: _winrt.Boolean) -> None:
        ...
    def get_scheduled_tile_notifications() -> winsdk.windows.foundation.collections.IVectorView[ScheduledTileNotification]:
        ...
    def remove_from_schedule(scheduled_tile: ScheduledTileNotification) -> None:
        ...
    def start_periodic_update(tile_content: winsdk.windows.foundation.Uri, requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def start_periodic_update(tile_content: winsdk.windows.foundation.Uri, start_time: winsdk.windows.foundation.DateTime, requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def start_periodic_update_batch(tile_contents: typing.Iterable[winsdk.windows.foundation.Uri], requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def start_periodic_update_batch(tile_contents: typing.Iterable[winsdk.windows.foundation.Uri], start_time: winsdk.windows.foundation.DateTime, requested_interval: PeriodicUpdateRecurrence) -> None:
        ...
    def stop_periodic_update() -> None:
        ...
    def update(notification: TileNotification) -> None:
        ...

class ToastActivatedEventArgs(_winrt.Object):
    ...
    arguments: str
    user_input: winsdk.windows.foundation.collections.ValueSet

class ToastCollection(_winrt.Object):
    ...
    launch_args: str
    icon: winsdk.windows.foundation.Uri
    display_name: str
    id: str
    def __init__(self, collection_id: str, display_name: str, launch_args: str, icon_uri: winsdk.windows.foundation.Uri) -> None:
        ...

class ToastCollectionManager(_winrt.Object):
    ...
    app_id: str
    user: winsdk.windows.system.User
    def find_all_toast_collections_async() -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[ToastCollection]]:
        ...
    def get_toast_collection_async(collection_id: str) -> winsdk.windows.foundation.IAsyncOperation[ToastCollection]:
        ...
    def remove_all_toast_collections_async() -> winsdk.windows.foundation.IAsyncAction:
        ...
    def remove_toast_collection_async(collection_id: str) -> winsdk.windows.foundation.IAsyncAction:
        ...
    def save_toast_collection_async(collection: ToastCollection) -> winsdk.windows.foundation.IAsyncAction:
        ...

class ToastDismissedEventArgs(_winrt.Object):
    ...
    reason: ToastDismissalReason

class ToastFailedEventArgs(_winrt.Object):
    ...
    error_code: winsdk.windows.foundation.HResult

class ToastNotification(_winrt.Object):
    ...
    expiration_time: typing.Optional[winsdk.windows.foundation.DateTime]
    content: winsdk.windows.data.xml.dom.XmlDocument
    tag: str
    suppress_popup: _winrt.Boolean
    group: str
    remote_id: str
    notification_mirroring: NotificationMirroring
    priority: ToastNotificationPriority
    data: NotificationData
    expires_on_reboot: _winrt.Boolean
    def __init__(self, content: winsdk.windows.data.xml.dom.XmlDocument) -> None:
        ...
    def add_activated(handler: winsdk.windows.foundation.TypedEventHandler[ToastNotification, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_activated(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_dismissed(handler: winsdk.windows.foundation.TypedEventHandler[ToastNotification, ToastDismissedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_dismissed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_failed(handler: winsdk.windows.foundation.TypedEventHandler[ToastNotification, ToastFailedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_failed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ToastNotificationActionTriggerDetail(_winrt.Object):
    ...
    argument: str
    user_input: winsdk.windows.foundation.collections.ValueSet

class ToastNotificationHistory(_winrt.Object):
    ...
    def clear() -> None:
        ...
    def clear(application_id: str) -> None:
        ...
    def get_history() -> winsdk.windows.foundation.collections.IVectorView[ToastNotification]:
        ...
    def get_history(application_id: str) -> winsdk.windows.foundation.collections.IVectorView[ToastNotification]:
        ...
    def remove(tag: str) -> None:
        ...
    def remove(tag: str, group: str) -> None:
        ...
    def remove(tag: str, group: str, application_id: str) -> None:
        ...
    def remove_group(group: str) -> None:
        ...
    def remove_group(group: str, application_id: str) -> None:
        ...

class ToastNotificationHistoryChangedTriggerDetail(_winrt.Object):
    ...
    change_type: ToastHistoryChangedType
    collection_id: str

class ToastNotificationManager(_winrt.Object):
    ...
    history: ToastNotificationHistory
    def configure_notification_mirroring(value: NotificationMirroring) -> None:
        ...
    def create_toast_notifier() -> ToastNotifier:
        ...
    def create_toast_notifier(application_id: str) -> ToastNotifier:
        ...
    def get_default() -> ToastNotificationManagerForUser:
        ...
    def get_for_user(user: winsdk.windows.system.User) -> ToastNotificationManagerForUser:
        ...
    def get_template_content(type: ToastTemplateType) -> winsdk.windows.data.xml.dom.XmlDocument:
        ...

class ToastNotificationManagerForUser(_winrt.Object):
    ...
    history: ToastNotificationHistory
    user: winsdk.windows.system.User
    def create_toast_notifier() -> ToastNotifier:
        ...
    def create_toast_notifier(application_id: str) -> ToastNotifier:
        ...
    def get_history_for_toast_collection_id_async(collection_id: str) -> winsdk.windows.foundation.IAsyncOperation[ToastNotificationHistory]:
        ...
    def get_toast_collection_manager() -> ToastCollectionManager:
        ...
    def get_toast_collection_manager(app_id: str) -> ToastCollectionManager:
        ...
    def get_toast_notifier_for_toast_collection_id_async(collection_id: str) -> winsdk.windows.foundation.IAsyncOperation[ToastNotifier]:
        ...

class ToastNotifier(_winrt.Object):
    ...
    setting: NotificationSetting
    def add_to_schedule(scheduled_toast: ScheduledToastNotification) -> None:
        ...
    def get_scheduled_toast_notifications() -> winsdk.windows.foundation.collections.IVectorView[ScheduledToastNotification]:
        ...
    def hide(notification: ToastNotification) -> None:
        ...
    def remove_from_schedule(scheduled_toast: ScheduledToastNotification) -> None:
        ...
    def show(notification: ToastNotification) -> None:
        ...
    def update(data: NotificationData, tag: str) -> NotificationUpdateResult:
        ...
    def update(data: NotificationData, tag: str, group: str) -> NotificationUpdateResult:
        ...
    def add_scheduled_toast_notification_showing(handler: winsdk.windows.foundation.TypedEventHandler[ToastNotifier, ScheduledToastNotificationShowingEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_scheduled_toast_notification_showing(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class UserNotification(_winrt.Object):
    ...
    app_info: winsdk.windows.applicationmodel.AppInfo
    creation_time: winsdk.windows.foundation.DateTime
    id: _winrt.UInt32
    notification: Notification

class UserNotificationChangedEventArgs(_winrt.Object):
    ...
    change_kind: UserNotificationChangedKind
    user_notification_id: _winrt.UInt32

class IAdaptiveNotificationContent(_winrt.Object):
    ...
    hints: winsdk.windows.foundation.collections.IMap[str, str]
    kind: AdaptiveNotificationContentKind

