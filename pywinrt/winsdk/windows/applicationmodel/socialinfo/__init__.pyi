# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt
import winsdk.windows.foundation
import winsdk.windows.foundation.collections
import winsdk.windows.graphics.imaging
import winsdk.windows.storage.streams

class SocialFeedItemStyle(enum.IntEnum):
    DEFAULT = 0
    PHOTO = 1

class SocialFeedKind(enum.IntEnum):
    HOME_FEED = 0
    CONTACT_FEED = 1
    DASHBOARD = 2

class SocialFeedUpdateMode(enum.IntEnum):
    APPEND = 0
    REPLACE = 1

class SocialItemBadgeStyle(enum.IntEnum):
    HIDDEN = 0
    VISIBLE = 1
    VISIBLE_WITH_COUNT = 2

Self = typing.TypeVar('Self')

class SocialFeedChildItem(_winrt.Object):
    timestamp: winsdk.windows.foundation.DateTime
    target_uri: typing.Optional[winsdk.windows.foundation.Uri]
    shared_item: typing.Optional[SocialFeedSharedItem]
    author: typing.Optional[SocialUserInfo]
    primary_content: typing.Optional[SocialFeedContent]
    secondary_content: typing.Optional[SocialFeedContent]
    thumbnails: typing.Optional[winsdk.windows.foundation.collections.IVector[SocialItemThumbnail]]
    @staticmethod
    def _from(obj: _winrt.Object) -> SocialFeedChildItem: ...
    def __init__(self) -> None: ...

class SocialFeedContent(_winrt.Object):
    title: str
    target_uri: typing.Optional[winsdk.windows.foundation.Uri]
    message: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SocialFeedContent: ...

class SocialFeedItem(_winrt.Object):
    timestamp: winsdk.windows.foundation.DateTime
    target_uri: typing.Optional[winsdk.windows.foundation.Uri]
    style: SocialFeedItemStyle
    shared_item: typing.Optional[SocialFeedSharedItem]
    remote_id: str
    child_item: typing.Optional[SocialFeedChildItem]
    badge_style: SocialItemBadgeStyle
    badge_count_value: _winrt.Int32
    author: typing.Optional[SocialUserInfo]
    thumbnails: typing.Optional[winsdk.windows.foundation.collections.IVector[SocialItemThumbnail]]
    primary_content: typing.Optional[SocialFeedContent]
    secondary_content: typing.Optional[SocialFeedContent]
    @staticmethod
    def _from(obj: _winrt.Object) -> SocialFeedItem: ...
    def __init__(self) -> None: ...

class SocialFeedSharedItem(_winrt.Object):
    timestamp: winsdk.windows.foundation.DateTime
    thumbnail: typing.Optional[SocialItemThumbnail]
    target_uri: typing.Optional[winsdk.windows.foundation.Uri]
    original_source: typing.Optional[winsdk.windows.foundation.Uri]
    content: typing.Optional[SocialFeedContent]
    @staticmethod
    def _from(obj: _winrt.Object) -> SocialFeedSharedItem: ...
    def __init__(self) -> None: ...

class SocialItemThumbnail(_winrt.Object):
    target_uri: typing.Optional[winsdk.windows.foundation.Uri]
    image_uri: typing.Optional[winsdk.windows.foundation.Uri]
    bitmap_size: winsdk.windows.graphics.imaging.BitmapSize
    @staticmethod
    def _from(obj: _winrt.Object) -> SocialItemThumbnail: ...
    def __init__(self) -> None: ...
    def set_image_async(self, image: typing.Optional[winsdk.windows.storage.streams.IInputStream]) -> typing.Optional[winsdk.windows.foundation.IAsyncAction]: ...

class SocialUserInfo(_winrt.Object):
    user_name: str
    target_uri: typing.Optional[winsdk.windows.foundation.Uri]
    remote_id: str
    display_name: str
    @staticmethod
    def _from(obj: _winrt.Object) -> SocialUserInfo: ...

