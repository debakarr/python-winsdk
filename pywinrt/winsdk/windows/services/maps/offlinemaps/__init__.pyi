# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

import enum
import sys
import types
import typing
import uuid

import winsdk._winrt as _winrt

try:
    import winsdk.windows.devices.geolocation
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

class OfflineMapPackageQueryStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    NETWORK_FAILURE = 3

class OfflineMapPackageStartDownloadStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    DENIED_WITHOUT_CAPABILITY = 3

class OfflineMapPackageStatus(enum.IntEnum):
    NOT_DOWNLOADED = 0
    DOWNLOADING = 1
    DOWNLOADED = 2
    DELETING = 3

class OfflineMapPackage(_winrt.Object):
    ...
    display_name: str
    enclosing_region_name: str
    estimated_size_in_bytes: _winrt.UInt64
    status: OfflineMapPackageStatus
    def find_packages_async(query_point: winsdk.windows.devices.geolocation.Geopoint) -> winsdk.windows.foundation.IAsyncOperation[OfflineMapPackageQueryResult]:
        ...
    def find_packages_in_bounding_box_async(query_bounding_box: winsdk.windows.devices.geolocation.GeoboundingBox) -> winsdk.windows.foundation.IAsyncOperation[OfflineMapPackageQueryResult]:
        ...
    def find_packages_in_geocircle_async(query_circle: winsdk.windows.devices.geolocation.Geocircle) -> winsdk.windows.foundation.IAsyncOperation[OfflineMapPackageQueryResult]:
        ...
    def request_start_download_async() -> winsdk.windows.foundation.IAsyncOperation[OfflineMapPackageStartDownloadResult]:
        ...
    def add_status_changed(value: winsdk.windows.foundation.TypedEventHandler[OfflineMapPackage, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_status_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class OfflineMapPackageQueryResult(_winrt.Object):
    ...
    packages: winsdk.windows.foundation.collections.IVectorView[OfflineMapPackage]
    status: OfflineMapPackageQueryStatus

class OfflineMapPackageStartDownloadResult(_winrt.Object):
    ...
    status: OfflineMapPackageStartDownloadStatus

