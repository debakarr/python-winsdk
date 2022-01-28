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

try:
    import winsdk.windows.ui.popups
except Exception:
    pass

class ManeuverWarningKind(enum.IntEnum):
    NONE = 0
    ACCIDENT = 1
    ADMINISTRATIVE_DIVISION_CHANGE = 2
    ALERT = 3
    BLOCKED_ROAD = 4
    CHECK_TIMETABLE = 5
    CONGESTION = 6
    CONSTRUCTION = 7
    COUNTRY_CHANGE = 8
    DISABLED_VEHICLE = 9
    GATE_ACCESS = 10
    GET_OFF_TRANSIT = 11
    GET_ON_TRANSIT = 12
    ILLEGAL_U_TURN = 13
    MASS_TRANSIT = 14
    MISCELLANEOUS = 15
    NO_INCIDENT = 16
    OTHER = 17
    OTHER_NEWS = 18
    OTHER_TRAFFIC_INCIDENTS = 19
    PLANNED_EVENT = 20
    PRIVATE_ROAD = 21
    RESTRICTED_TURN = 22
    ROAD_CLOSURES = 23
    ROAD_HAZARD = 24
    SCHEDULED_CONSTRUCTION = 25
    SEASONAL_CLOSURES = 26
    TOLLBOOTH = 27
    TOLL_ROAD = 28
    TOLL_ZONE_ENTER = 29
    TOLL_ZONE_EXIT = 30
    TRAFFIC_FLOW = 31
    TRANSIT_LINE_CHANGE = 32
    UNPAVED_ROAD = 33
    UNSCHEDULED_CONSTRUCTION = 34
    WEATHER = 35

class ManeuverWarningSeverity(enum.IntEnum):
    NONE = 0
    LOW_IMPACT = 1
    MINOR = 2
    MODERATE = 3
    SERIOUS = 4

class MapLocationDesiredAccuracy(enum.IntEnum):
    HIGH = 0
    LOW = 1

class MapLocationFinderStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    BAD_LOCATION = 3
    INDEX_FAILURE = 4
    NETWORK_FAILURE = 5
    NOT_SUPPORTED = 6

class MapManeuverNotices(enum.IntFlag):
    NONE = 0
    TOLL = 0x1
    UNPAVED = 0x2

class MapRouteFinderStatus(enum.IntEnum):
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    INVALID_CREDENTIALS = 2
    NO_ROUTE_FOUND = 3
    NO_ROUTE_FOUND_WITH_GIVEN_OPTIONS = 4
    START_POINT_NOT_FOUND = 5
    END_POINT_NOT_FOUND = 6
    NO_PEDESTRIAN_ROUTE_FOUND = 7
    NETWORK_FAILURE = 8
    NOT_SUPPORTED = 9

class MapRouteManeuverKind(enum.IntEnum):
    NONE = 0
    START = 1
    STOPOVER = 2
    STOPOVER_RESUME = 3
    END = 4
    GO_STRAIGHT = 5
    U_TURN_LEFT = 6
    U_TURN_RIGHT = 7
    TURN_KEEP_LEFT = 8
    TURN_KEEP_RIGHT = 9
    TURN_LIGHT_LEFT = 10
    TURN_LIGHT_RIGHT = 11
    TURN_LEFT = 12
    TURN_RIGHT = 13
    TURN_HARD_LEFT = 14
    TURN_HARD_RIGHT = 15
    FREEWAY_ENTER_LEFT = 16
    FREEWAY_ENTER_RIGHT = 17
    FREEWAY_LEAVE_LEFT = 18
    FREEWAY_LEAVE_RIGHT = 19
    FREEWAY_CONTINUE_LEFT = 20
    FREEWAY_CONTINUE_RIGHT = 21
    TRAFFIC_CIRCLE_LEFT = 22
    TRAFFIC_CIRCLE_RIGHT = 23
    TAKE_FERRY = 24

class MapRouteOptimization(enum.IntEnum):
    TIME = 0
    DISTANCE = 1
    TIME_WITH_TRAFFIC = 2
    SCENIC = 3

class MapRouteRestrictions(enum.IntFlag):
    NONE = 0
    HIGHWAYS = 0x1
    TOLL_ROADS = 0x2
    FERRIES = 0x4
    TUNNELS = 0x8
    DIRT_ROADS = 0x10
    MOTORAIL = 0x20

class MapServiceDataUsagePreference(enum.IntEnum):
    DEFAULT = 0
    OFFLINE_MAP_DATA_ONLY = 1

class TrafficCongestion(enum.IntEnum):
    UNKNOWN = 0
    LIGHT = 1
    MILD = 2
    MEDIUM = 3
    HEAVY = 4

class WaypointKind(enum.IntEnum):
    STOP = 0
    VIA = 1

class EnhancedWaypoint(_winrt.Object):
    ...
    kind: WaypointKind
    point: winsdk.windows.devices.geolocation.Geopoint
    def __init__(self, point: winsdk.windows.devices.geolocation.Geopoint, kind: WaypointKind) -> None:
        ...

class ManeuverWarning(_winrt.Object):
    ...
    kind: ManeuverWarningKind
    severity: ManeuverWarningSeverity

class MapAddress(_winrt.Object):
    ...
    building_floor: str
    building_name: str
    building_room: str
    building_wing: str
    continent: str
    country: str
    country_code: str
    district: str
    neighborhood: str
    post_code: str
    region: str
    region_code: str
    street: str
    street_number: str
    town: str
    formatted_address: str

class MapLocation(_winrt.Object):
    ...
    address: MapAddress
    description: str
    display_name: str
    point: winsdk.windows.devices.geolocation.Geopoint

class MapLocationFinder(_winrt.Object):
    ...
    def find_locations_async(search_text: str, reference_point: winsdk.windows.devices.geolocation.Geopoint) -> winsdk.windows.foundation.IAsyncOperation[MapLocationFinderResult]:
        ...
    def find_locations_async(search_text: str, reference_point: winsdk.windows.devices.geolocation.Geopoint, max_count: _winrt.UInt32) -> winsdk.windows.foundation.IAsyncOperation[MapLocationFinderResult]:
        ...
    def find_locations_at_async(query_point: winsdk.windows.devices.geolocation.Geopoint) -> winsdk.windows.foundation.IAsyncOperation[MapLocationFinderResult]:
        ...
    def find_locations_at_async(query_point: winsdk.windows.devices.geolocation.Geopoint, accuracy: MapLocationDesiredAccuracy) -> winsdk.windows.foundation.IAsyncOperation[MapLocationFinderResult]:
        ...

class MapLocationFinderResult(_winrt.Object):
    ...
    locations: winsdk.windows.foundation.collections.IVectorView[MapLocation]
    status: MapLocationFinderStatus

class MapManager(_winrt.Object):
    ...
    def show_downloaded_maps_u_i() -> None:
        ...
    def show_maps_update_u_i() -> None:
        ...

class MapRoute(_winrt.Object):
    ...
    bounding_box: winsdk.windows.devices.geolocation.GeoboundingBox
    estimated_duration: winsdk.windows.foundation.TimeSpan
    is_traffic_based: _winrt.Boolean
    legs: winsdk.windows.foundation.collections.IVectorView[MapRouteLeg]
    length_in_meters: _winrt.Double
    path: winsdk.windows.devices.geolocation.Geopath
    has_blocked_roads: _winrt.Boolean
    violated_restrictions: MapRouteRestrictions
    duration_without_traffic: winsdk.windows.foundation.TimeSpan
    traffic_congestion: TrafficCongestion
    is_scenic: _winrt.Boolean

class MapRouteDrivingOptions(_winrt.Object):
    ...
    route_restrictions: MapRouteRestrictions
    route_optimization: MapRouteOptimization
    max_alternate_route_count: _winrt.UInt32
    initial_heading: typing.Optional[_winrt.Double]
    departure_time: typing.Optional[winsdk.windows.foundation.DateTime]
    def __init__(self, ) -> None:
        ...

class MapRouteFinder(_winrt.Object):
    ...
    def get_driving_route_async(start_point: winsdk.windows.devices.geolocation.Geopoint, end_point: winsdk.windows.devices.geolocation.Geopoint) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_async(start_point: winsdk.windows.devices.geolocation.Geopoint, end_point: winsdk.windows.devices.geolocation.Geopoint, options: MapRouteDrivingOptions) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_async(start_point: winsdk.windows.devices.geolocation.Geopoint, end_point: winsdk.windows.devices.geolocation.Geopoint, optimization: MapRouteOptimization, restrictions: MapRouteRestrictions) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_async(start_point: winsdk.windows.devices.geolocation.Geopoint, end_point: winsdk.windows.devices.geolocation.Geopoint, optimization: MapRouteOptimization, restrictions: MapRouteRestrictions, heading_in_degrees: _winrt.Double) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_from_enhanced_waypoints_async(waypoints: typing.Iterable[EnhancedWaypoint]) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_from_enhanced_waypoints_async(waypoints: typing.Iterable[EnhancedWaypoint], options: MapRouteDrivingOptions) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_from_waypoints_async(way_points: typing.Iterable[winsdk.windows.devices.geolocation.Geopoint]) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_from_waypoints_async(way_points: typing.Iterable[winsdk.windows.devices.geolocation.Geopoint], optimization: MapRouteOptimization) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_from_waypoints_async(way_points: typing.Iterable[winsdk.windows.devices.geolocation.Geopoint], optimization: MapRouteOptimization, restrictions: MapRouteRestrictions) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_driving_route_from_waypoints_async(way_points: typing.Iterable[winsdk.windows.devices.geolocation.Geopoint], optimization: MapRouteOptimization, restrictions: MapRouteRestrictions, heading_in_degrees: _winrt.Double) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_walking_route_async(start_point: winsdk.windows.devices.geolocation.Geopoint, end_point: winsdk.windows.devices.geolocation.Geopoint) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...
    def get_walking_route_from_waypoints_async(way_points: typing.Iterable[winsdk.windows.devices.geolocation.Geopoint]) -> winsdk.windows.foundation.IAsyncOperation[MapRouteFinderResult]:
        ...

class MapRouteFinderResult(_winrt.Object):
    ...
    route: MapRoute
    status: MapRouteFinderStatus
    alternate_routes: winsdk.windows.foundation.collections.IVectorView[MapRoute]

class MapRouteLeg(_winrt.Object):
    ...
    bounding_box: winsdk.windows.devices.geolocation.GeoboundingBox
    estimated_duration: winsdk.windows.foundation.TimeSpan
    length_in_meters: _winrt.Double
    maneuvers: winsdk.windows.foundation.collections.IVectorView[MapRouteManeuver]
    path: winsdk.windows.devices.geolocation.Geopath
    duration_without_traffic: winsdk.windows.foundation.TimeSpan
    traffic_congestion: TrafficCongestion

class MapRouteManeuver(_winrt.Object):
    ...
    exit_number: str
    instruction_text: str
    kind: MapRouteManeuverKind
    length_in_meters: _winrt.Double
    maneuver_notices: MapManeuverNotices
    starting_point: winsdk.windows.devices.geolocation.Geopoint
    end_heading: _winrt.Double
    start_heading: _winrt.Double
    street_name: str
    warnings: winsdk.windows.foundation.collections.IVectorView[ManeuverWarning]

class MapService(_winrt.Object):
    ...
    service_token: str
    world_view_region_code: str
    data_attributions: str
    data_usage_preference: MapServiceDataUsagePreference

class PlaceInfo(_winrt.Object):
    ...
    display_address: str
    display_name: str
    geoshape: winsdk.windows.devices.geolocation.IGeoshape
    identifier: str
    is_show_supported: _winrt.Boolean
    def create(reference_point: winsdk.windows.devices.geolocation.Geopoint) -> PlaceInfo:
        ...
    def create(reference_point: winsdk.windows.devices.geolocation.Geopoint, options: PlaceInfoCreateOptions) -> PlaceInfo:
        ...
    def create_from_address(display_address: str) -> PlaceInfo:
        ...
    def create_from_address(display_address: str, display_name: str) -> PlaceInfo:
        ...
    def create_from_identifier(identifier: str) -> PlaceInfo:
        ...
    def create_from_identifier(identifier: str, default_point: winsdk.windows.devices.geolocation.Geopoint, options: PlaceInfoCreateOptions) -> PlaceInfo:
        ...
    def create_from_map_location(location: MapLocation) -> PlaceInfo:
        ...
    def show(selection: winsdk.windows.foundation.Rect) -> None:
        ...
    def show(selection: winsdk.windows.foundation.Rect, preferred_placement: winsdk.windows.ui.popups.Placement) -> None:
        ...

class PlaceInfoCreateOptions(_winrt.Object):
    ...
    display_name: str
    display_address: str
    def __init__(self, ) -> None:
        ...

