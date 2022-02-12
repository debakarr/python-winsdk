# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

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
    import winsdk.windows.services.maps
except Exception:
    pass

try:
    import winsdk.windows.ui
except Exception:
    pass

class GuidanceAudioMeasurementSystem(enum.IntEnum):
    METERS = 0
    MILES_AND_YARDS = 1
    MILES_AND_FEET = 2

class GuidanceAudioNotificationKind(enum.IntEnum):
    MANEUVER = 0
    ROUTE = 1
    GPS = 2
    SPEED_LIMIT = 3
    TRAFFIC = 4
    TRAFFIC_CAMERA = 5

class GuidanceAudioNotifications(enum.IntFlag):
    NONE = 0
    MANEUVER = 0x1
    ROUTE = 0x2
    GPS = 0x4
    SPEED_LIMIT = 0x8
    TRAFFIC = 0x10
    TRAFFIC_CAMERA = 0x20

class GuidanceLaneMarkers(enum.IntFlag):
    NONE = 0
    LIGHT_RIGHT = 0x1
    RIGHT = 0x2
    HARD_RIGHT = 0x4
    STRAIGHT = 0x8
    U_TURN_LEFT = 0x10
    HARD_LEFT = 0x20
    LEFT = 0x40
    LIGHT_LEFT = 0x80
    U_TURN_RIGHT = 0x100
    UNKNOWN = 0xffffffff

class GuidanceManeuverKind(enum.IntEnum):
    NONE = 0
    GO_STRAIGHT = 1
    U_TURN_RIGHT = 2
    U_TURN_LEFT = 3
    TURN_KEEP_RIGHT = 4
    TURN_LIGHT_RIGHT = 5
    TURN_RIGHT = 6
    TURN_HARD_RIGHT = 7
    KEEP_MIDDLE = 8
    TURN_KEEP_LEFT = 9
    TURN_LIGHT_LEFT = 10
    TURN_LEFT = 11
    TURN_HARD_LEFT = 12
    FREEWAY_ENTER_RIGHT = 13
    FREEWAY_ENTER_LEFT = 14
    FREEWAY_LEAVE_RIGHT = 15
    FREEWAY_LEAVE_LEFT = 16
    FREEWAY_KEEP_RIGHT = 17
    FREEWAY_KEEP_LEFT = 18
    TRAFFIC_CIRCLE_RIGHT1 = 19
    TRAFFIC_CIRCLE_RIGHT2 = 20
    TRAFFIC_CIRCLE_RIGHT3 = 21
    TRAFFIC_CIRCLE_RIGHT4 = 22
    TRAFFIC_CIRCLE_RIGHT5 = 23
    TRAFFIC_CIRCLE_RIGHT6 = 24
    TRAFFIC_CIRCLE_RIGHT7 = 25
    TRAFFIC_CIRCLE_RIGHT8 = 26
    TRAFFIC_CIRCLE_RIGHT9 = 27
    TRAFFIC_CIRCLE_RIGHT10 = 28
    TRAFFIC_CIRCLE_RIGHT11 = 29
    TRAFFIC_CIRCLE_RIGHT12 = 30
    TRAFFIC_CIRCLE_LEFT1 = 31
    TRAFFIC_CIRCLE_LEFT2 = 32
    TRAFFIC_CIRCLE_LEFT3 = 33
    TRAFFIC_CIRCLE_LEFT4 = 34
    TRAFFIC_CIRCLE_LEFT5 = 35
    TRAFFIC_CIRCLE_LEFT6 = 36
    TRAFFIC_CIRCLE_LEFT7 = 37
    TRAFFIC_CIRCLE_LEFT8 = 38
    TRAFFIC_CIRCLE_LEFT9 = 39
    TRAFFIC_CIRCLE_LEFT10 = 40
    TRAFFIC_CIRCLE_LEFT11 = 41
    TRAFFIC_CIRCLE_LEFT12 = 42
    START = 43
    END = 44
    TAKE_FERRY = 45
    PASS_TRANSIT_STATION = 46
    LEAVE_TRANSIT_STATION = 47

class GuidanceMode(enum.IntEnum):
    NONE = 0
    SIMULATION = 1
    NAVIGATION = 2
    TRACKING = 3

class GuidanceAudioNotificationRequestedEventArgs(_winrt.Object):
    audio_file_paths: winsdk.windows.foundation.collections.IVectorView[str]
    audio_notification: GuidanceAudioNotificationKind
    audio_text: str
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceAudioNotificationRequestedEventArgs: ...

class GuidanceLaneInfo(_winrt.Object):
    is_on_route: _winrt.Boolean
    lane_markers: GuidanceLaneMarkers
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceLaneInfo: ...

class GuidanceManeuver(_winrt.Object):
    departure_road_name: str
    departure_short_road_name: str
    distance_from_previous_maneuver: _winrt.Int32
    distance_from_route_start: _winrt.Int32
    end_angle: _winrt.Int32
    instruction_text: str
    kind: GuidanceManeuverKind
    next_road_name: str
    next_short_road_name: str
    road_signpost: GuidanceRoadSignpost
    start_angle: _winrt.Int32
    start_location: winsdk.windows.devices.geolocation.Geopoint
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceManeuver: ...

class GuidanceMapMatchedCoordinate(_winrt.Object):
    current_heading: _winrt.Double
    current_speed: _winrt.Double
    is_on_street: _winrt.Boolean
    location: winsdk.windows.devices.geolocation.Geopoint
    road: GuidanceRoadSegment
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceMapMatchedCoordinate: ...

class GuidanceNavigator(_winrt.Object):
    audio_notifications: GuidanceAudioNotifications
    audio_measurement_system: GuidanceAudioMeasurementSystem
    is_guidance_audio_muted: _winrt.Boolean
    use_app_provided_voice: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceNavigator: ...
    @typing.overload
    @staticmethod
    def get_current() -> GuidanceNavigator: ...
    @typing.overload
    def pause(self) -> None: ...
    @typing.overload
    def repeat_last_audio_notification(self) -> None: ...
    @typing.overload
    def resume(self) -> None: ...
    @typing.overload
    def set_guidance_voice(self, voice_id: _winrt.Int32, voice_folder: str) -> None: ...
    @typing.overload
    def start_navigating(self, route: GuidanceRoute) -> None: ...
    @typing.overload
    def start_simulating(self, route: GuidanceRoute, speed_in_meters_per_second: _winrt.Int32) -> None: ...
    @typing.overload
    def start_tracking(self) -> None: ...
    @typing.overload
    def stop(self) -> None: ...
    @typing.overload
    def update_user_location(self, user_location: winsdk.windows.devices.geolocation.Geocoordinate) -> None: ...
    @typing.overload
    def update_user_location(self, user_location: winsdk.windows.devices.geolocation.Geocoordinate, position_override: winsdk.windows.devices.geolocation.BasicGeoposition) -> None: ...
    @typing.overload
    def add_destination_reached(self, handler: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_destination_reached(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_guidance_updated(self, handler: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, GuidanceUpdatedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_guidance_updated(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_reroute_failed(self, handler: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_reroute_failed(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_rerouted(self, handler: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, GuidanceReroutedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_rerouted(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_rerouting(self, handler: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_rerouting(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_user_location_lost(self, handler: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_user_location_lost(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_user_location_restored(self, handler: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, _winrt.Object]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_user_location_restored(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...
    @typing.overload
    def add_audio_notification_requested(self, value: winsdk.windows.foundation.TypedEventHandler[GuidanceNavigator, GuidanceAudioNotificationRequestedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken: ...
    @typing.overload
    def remove_audio_notification_requested(self, token: winsdk.windows.foundation.EventRegistrationToken) -> None: ...

class GuidanceReroutedEventArgs(_winrt.Object):
    route: GuidanceRoute
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceReroutedEventArgs: ...

class GuidanceRoadSegment(_winrt.Object):
    id: str
    is_highway: _winrt.Boolean
    is_toll_road: _winrt.Boolean
    is_tunnel: _winrt.Boolean
    path: winsdk.windows.devices.geolocation.Geopath
    road_name: str
    short_road_name: str
    speed_limit: _winrt.Double
    travel_time: winsdk.windows.foundation.TimeSpan
    is_scenic: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceRoadSegment: ...

class GuidanceRoadSignpost(_winrt.Object):
    background_color: winsdk.windows.ui.Color
    exit: str
    exit_directions: winsdk.windows.foundation.collections.IVectorView[str]
    exit_number: str
    foreground_color: winsdk.windows.ui.Color
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceRoadSignpost: ...

class GuidanceRoute(_winrt.Object):
    bounding_box: winsdk.windows.devices.geolocation.GeoboundingBox
    distance: _winrt.Int32
    duration: winsdk.windows.foundation.TimeSpan
    maneuvers: winsdk.windows.foundation.collections.IVectorView[GuidanceManeuver]
    path: winsdk.windows.devices.geolocation.Geopath
    road_segments: winsdk.windows.foundation.collections.IVectorView[GuidanceRoadSegment]
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceRoute: ...
    @typing.overload
    @staticmethod
    def can_create_from_map_route(map_route: winsdk.windows.services.maps.MapRoute) -> _winrt.Boolean: ...
    @typing.overload
    def convert_to_map_route(self) -> winsdk.windows.services.maps.MapRoute: ...
    @typing.overload
    @staticmethod
    def try_create_from_map_route(map_route: winsdk.windows.services.maps.MapRoute) -> GuidanceRoute: ...

class GuidanceTelemetryCollector(_winrt.Object):
    upload_frequency: _winrt.Int32
    speed_trigger: _winrt.Double
    enabled: _winrt.Boolean
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceTelemetryCollector: ...
    @typing.overload
    def clear_local_data(self) -> None: ...
    @typing.overload
    @staticmethod
    def get_current() -> GuidanceTelemetryCollector: ...

class GuidanceUpdatedEventArgs(_winrt.Object):
    after_next_maneuver: GuidanceManeuver
    after_next_maneuver_distance: _winrt.Int32
    current_location: GuidanceMapMatchedCoordinate
    distance_to_destination: _winrt.Int32
    elapsed_distance: _winrt.Int32
    elapsed_time: winsdk.windows.foundation.TimeSpan
    is_new_maneuver: _winrt.Boolean
    lane_info: winsdk.windows.foundation.collections.IVectorView[GuidanceLaneInfo]
    mode: GuidanceMode
    next_maneuver: GuidanceManeuver
    next_maneuver_distance: _winrt.Int32
    road_name: str
    route: GuidanceRoute
    time_to_destination: winsdk.windows.foundation.TimeSpan
    @staticmethod
    def _from(obj: _winrt.Object) -> GuidanceUpdatedEventArgs: ...

