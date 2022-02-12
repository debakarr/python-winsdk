# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum
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

class AltitudeReferenceSystem(enum.IntEnum):
    UNSPECIFIED = 0
    TERRAIN = 1
    ELLIPSOID = 2
    GEOID = 3
    SURFACE = 4

class GeolocationAccessStatus(enum.IntEnum):
    UNSPECIFIED = 0
    ALLOWED = 1
    DENIED = 2

class GeoshapeType(enum.IntEnum):
    GEOPOINT = 0
    GEOCIRCLE = 1
    GEOPATH = 2
    GEOBOUNDING_BOX = 3

class PositionAccuracy(enum.IntEnum):
    DEFAULT = 0
    HIGH = 1

class PositionSource(enum.IntEnum):
    CELLULAR = 0
    SATELLITE = 1
    WI_FI = 2
    IP_ADDRESS = 3
    UNKNOWN = 4
    DEFAULT = 5
    OBFUSCATED = 6

class PositionStatus(enum.IntEnum):
    READY = 0
    INITIALIZING = 1
    NO_DATA = 2
    DISABLED = 3
    NOT_INITIALIZED = 4
    NOT_AVAILABLE = 5

class VisitMonitoringScope(enum.IntEnum):
    VENUE = 0
    CITY = 1

class VisitStateChange(enum.IntEnum):
    TRACKING_LOST = 0
    ARRIVED = 1
    DEPARTED = 2
    OTHER_MOVEMENT = 3

class BasicGeoposition:
    latitude: _winrt.Double
    longitude: _winrt.Double
    altitude: _winrt.Double
    def __init__(self, latitude: _winrt.Double, longitude: _winrt.Double, altitude: _winrt.Double) -> None: ...

class CivicAddress(_winrt.Object):
    city: str
    country: str
    postal_code: str
    state: str
    timestamp: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> CivicAddress: ...

class GeoboundingBox(IGeoshape, _winrt.Object):
    center: BasicGeoposition
    max_altitude: _winrt.Double
    min_altitude: _winrt.Double
    northwest_corner: BasicGeoposition
    southeast_corner: BasicGeoposition
    altitude_reference_system: AltitudeReferenceSystem
    geoshape_type: GeoshapeType
    spatial_reference_id: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> GeoboundingBox: ...
    @typing.overload
    def __init__(self, northwest_corner: BasicGeoposition, southeast_corner: BasicGeoposition) -> None: ...
    @typing.overload
    def __init__(self, northwest_corner: BasicGeoposition, southeast_corner: BasicGeoposition, altitude_reference_system: AltitudeReferenceSystem) -> None: ...
    @typing.overload
    def __init__(self, northwest_corner: BasicGeoposition, southeast_corner: BasicGeoposition, altitude_reference_system: AltitudeReferenceSystem, spatial_reference_id: _winrt.UInt32) -> None: ...
    @typing.overload
    @staticmethod
    def try_compute(positions: typing.Iterable[BasicGeoposition]) -> GeoboundingBox: ...
    @typing.overload
    @staticmethod
    def try_compute(positions: typing.Iterable[BasicGeoposition], altitude_ref_system: AltitudeReferenceSystem) -> GeoboundingBox: ...
    @typing.overload
    @staticmethod
    def try_compute(positions: typing.Iterable[BasicGeoposition], altitude_ref_system: AltitudeReferenceSystem, spatial_reference_id: _winrt.UInt32) -> GeoboundingBox: ...

class Geocircle(IGeoshape, _winrt.Object):
    center: BasicGeoposition
    radius: _winrt.Double
    altitude_reference_system: AltitudeReferenceSystem
    geoshape_type: GeoshapeType
    spatial_reference_id: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> Geocircle: ...
    @typing.overload
    def __init__(self, position: BasicGeoposition, radius: _winrt.Double) -> None: ...
    @typing.overload
    def __init__(self, position: BasicGeoposition, radius: _winrt.Double, altitude_reference_system: AltitudeReferenceSystem) -> None: ...
    @typing.overload
    def __init__(self, position: BasicGeoposition, radius: _winrt.Double, altitude_reference_system: AltitudeReferenceSystem, spatial_reference_id: _winrt.UInt32) -> None: ...

class Geocoordinate(_winrt.Object):
    accuracy: _winrt.Double
    altitude: typing.Optional[_winrt.Double]
    altitude_accuracy: typing.Optional[_winrt.Double]
    heading: typing.Optional[_winrt.Double]
    latitude: _winrt.Double
    longitude: _winrt.Double
    speed: typing.Optional[_winrt.Double]
    timestamp: winsdk.windows.foundation.DateTime
    point: Geopoint
    position_source: PositionSource
    satellite_data: GeocoordinateSatelliteData
    position_source_timestamp: typing.Optional[winsdk.windows.foundation.DateTime]
    is_remote_source: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> Geocoordinate: ...

class GeocoordinateSatelliteData(_winrt.Object):
    horizontal_dilution_of_precision: typing.Optional[_winrt.Double]
    position_dilution_of_precision: typing.Optional[_winrt.Double]
    vertical_dilution_of_precision: typing.Optional[_winrt.Double]
    geometric_dilution_of_precision: typing.Optional[_winrt.Double]
    time_dilution_of_precision: typing.Optional[_winrt.Double]
    @staticmethod
    def _from(obj: _winrt.Object) -> GeocoordinateSatelliteData: ...

class Geolocator(_winrt.Object):
    report_interval: _winrt.UInt32
    movement_threshold: _winrt.Double
    desired_accuracy: PositionAccuracy
    location_status: PositionStatus
    desired_accuracy_in_meters: typing.Optional[_winrt.UInt32]
    default_geoposition: typing.Optional[BasicGeoposition]
    is_default_geoposition_recommended: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> Geolocator: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def allow_fallback_to_consentless_positions(self) -> None: ...
    @typing.overload
    def get_geoposition_async(self) -> winsdk.windows.foundation.IAsyncOperation[Geoposition]: ...
    @typing.overload
    def get_geoposition_async(self, maximum_age: winsdk.windows.foundation.TimeSpan, timeout: winsdk.windows.foundation.TimeSpan) -> winsdk.windows.foundation.IAsyncOperation[Geoposition]: ...
    @typing.overload
    @staticmethod
    def get_geoposition_history_async(start_time: winsdk.windows.foundation.DateTime) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[Geoposition]]: ...
    @typing.overload
    @staticmethod
    def get_geoposition_history_async(start_time: winsdk.windows.foundation.DateTime, duration: winsdk.windows.foundation.TimeSpan) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[Geoposition]]: ...
    @typing.overload
    @staticmethod
    def request_access_async() -> winsdk.windows.foundation.IAsyncOperation[GeolocationAccessStatus]: ...
    @typing.overload
    def add_position_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[Geolocator, PositionChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_position_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_status_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[Geolocator, StatusChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_status_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class Geopath(IGeoshape, _winrt.Object):
    positions: winsdk.windows.foundation.collections.IVectorView[BasicGeoposition]
    altitude_reference_system: AltitudeReferenceSystem
    geoshape_type: GeoshapeType
    spatial_reference_id: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> Geopath: ...
    @typing.overload
    def __init__(self, positions: typing.Iterable[BasicGeoposition]) -> None: ...
    @typing.overload
    def __init__(self, positions: typing.Iterable[BasicGeoposition], altitude_reference_system: AltitudeReferenceSystem) -> None: ...
    @typing.overload
    def __init__(self, positions: typing.Iterable[BasicGeoposition], altitude_reference_system: AltitudeReferenceSystem, spatial_reference_id: _winrt.UInt32) -> None: ...

class Geopoint(IGeoshape, _winrt.Object):
    position: BasicGeoposition
    altitude_reference_system: AltitudeReferenceSystem
    geoshape_type: GeoshapeType
    spatial_reference_id: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> Geopoint: ...
    @typing.overload
    def __init__(self, position: BasicGeoposition) -> None: ...
    @typing.overload
    def __init__(self, position: BasicGeoposition, altitude_reference_system: AltitudeReferenceSystem) -> None: ...
    @typing.overload
    def __init__(self, position: BasicGeoposition, altitude_reference_system: AltitudeReferenceSystem, spatial_reference_id: _winrt.UInt32) -> None: ...

class Geoposition(_winrt.Object):
    civic_address: CivicAddress
    coordinate: Geocoordinate
    venue_data: VenueData
    @staticmethod
    def _from(obj: _winrt.Object) -> Geoposition: ...

class Geovisit(_winrt.Object):
    position: Geoposition
    state_change: VisitStateChange
    timestamp: winsdk.windows.foundation.DateTime
    @staticmethod
    def _from(obj: _winrt.Object) -> Geovisit: ...

class GeovisitMonitor(_winrt.Object):
    monitoring_scope: VisitMonitoringScope
    @staticmethod
    def _from(obj: _winrt.Object) -> GeovisitMonitor: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    @staticmethod
    def get_last_report_async() -> winsdk.windows.foundation.IAsyncOperation[Geovisit]: ...
    @typing.overload
    def start(self, value: VisitMonitoringScope) -> None: ...
    @typing.overload
    def stop(self) -> None: ...
    @typing.overload
    def add_visit_state_changed(self, handler: winsdk.windows.foundation.TypedEventHandler[GeovisitMonitor, GeovisitStateChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_visit_state_changed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GeovisitStateChangedEventArgs(_winrt.Object):
    visit: Geovisit
    @staticmethod
    def _from(obj: _winrt.Object) -> GeovisitStateChangedEventArgs: ...

class GeovisitTriggerDetails(_winrt.Object):
    @staticmethod
    def _from(obj: _winrt.Object) -> GeovisitTriggerDetails: ...
    @typing.overload
    def read_reports(self) -> winsdk.windows.foundation.collections.IVectorView[Geovisit]: ...

class PositionChangedEventArgs(_winrt.Object):
    position: Geoposition
    @staticmethod
    def _from(obj: _winrt.Object) -> PositionChangedEventArgs: ...

class StatusChangedEventArgs(_winrt.Object):
    status: PositionStatus
    @staticmethod
    def _from(obj: _winrt.Object) -> StatusChangedEventArgs: ...

class VenueData(_winrt.Object):
    id: str
    level: str
    @staticmethod
    def _from(obj: _winrt.Object) -> VenueData: ...

class IGeoshape(_winrt.Object):
    altitude_reference_system: AltitudeReferenceSystem
    geoshape_type: GeoshapeType
    spatial_reference_id: _winrt.UInt32
    @staticmethod
    def _from(obj: _winrt.Object) -> IGeoshape: ...

