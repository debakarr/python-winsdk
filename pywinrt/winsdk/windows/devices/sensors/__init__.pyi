# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

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

try:
    import winsdk.windows.graphics.display
except Exception:
    pass

class AccelerometerReadingType(enum.IntEnum):
    STANDARD = 0
    LINEAR = 1
    GRAVITY = 2

class ActivitySensorReadingConfidence(enum.IntEnum):
    HIGH = 0
    LOW = 1

class ActivityType(enum.IntEnum):
    UNKNOWN = 0
    IDLE = 1
    STATIONARY = 2
    FIDGETING = 3
    WALKING = 4
    RUNNING = 5
    IN_VEHICLE = 6
    BIKING = 7

class MagnetometerAccuracy(enum.IntEnum):
    UNKNOWN = 0
    UNRELIABLE = 1
    APPROXIMATE = 2
    HIGH = 3

class PedometerStepKind(enum.IntEnum):
    UNKNOWN = 0
    WALKING = 1
    RUNNING = 2

class SensorOptimizationGoal(enum.IntEnum):
    PRECISION = 0
    POWER_EFFICIENCY = 1

class SensorReadingType(enum.IntEnum):
    ABSOLUTE = 0
    RELATIVE = 1

class SensorType(enum.IntEnum):
    ACCELEROMETER = 0
    ACTIVITY_SENSOR = 1
    BAROMETER = 2
    COMPASS = 3
    CUSTOM_SENSOR = 4
    GYROSCOPE = 5
    PROXIMITY_SENSOR = 6
    INCLINOMETER = 7
    LIGHT_SENSOR = 8
    ORIENTATION_SENSOR = 9
    PEDOMETER = 10
    RELATIVE_INCLINOMETER = 11
    RELATIVE_ORIENTATION_SENSOR = 12
    SIMPLE_ORIENTATION_SENSOR = 13

class SimpleOrientation(enum.IntEnum):
    NOT_ROTATED = 0
    ROTATED90_DEGREES_COUNTERCLOCKWISE = 1
    ROTATED180_DEGREES_COUNTERCLOCKWISE = 2
    ROTATED270_DEGREES_COUNTERCLOCKWISE = 3
    FACEUP = 4
    FACEDOWN = 5

class Accelerometer(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    minimum_report_interval: _winrt.UInt32
    reading_transform: winsdk.windows.graphics.display.DisplayOrientations
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    reading_type: AccelerometerReadingType
    report_threshold: AccelerometerDataThreshold
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Accelerometer]:
        ...
    def get_current_reading() -> AccelerometerReading:
        ...
    def get_default() -> Accelerometer:
        ...
    def get_default(reading_type: AccelerometerReadingType) -> Accelerometer:
        ...
    def get_device_selector(reading_type: AccelerometerReadingType) -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Accelerometer, AccelerometerReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...
    def add_shaken(handler: winsdk.windows.foundation.TypedEventHandler[Accelerometer, AccelerometerShakenEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_shaken(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class AccelerometerDataThreshold(_winrt.Object):
    ...
    z_axis_in_g_force: _winrt.Double
    y_axis_in_g_force: _winrt.Double
    x_axis_in_g_force: _winrt.Double

class AccelerometerReading(_winrt.Object):
    ...
    acceleration_x: _winrt.Double
    acceleration_y: _winrt.Double
    acceleration_z: _winrt.Double
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]

class AccelerometerReadingChangedEventArgs(_winrt.Object):
    ...
    reading: AccelerometerReading

class AccelerometerShakenEventArgs(_winrt.Object):
    ...
    timestamp: winsdk.windows.foundation.DateTime

class ActivitySensor(_winrt.Object):
    ...
    device_id: str
    minimum_report_interval: _winrt.UInt32
    power_in_milliwatts: _winrt.Double
    subscribed_activities: winsdk.windows.foundation.collections.IVector[ActivityType]
    supported_activities: winsdk.windows.foundation.collections.IVectorView[ActivityType]
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[ActivitySensor]:
        ...
    def get_current_reading_async() -> winsdk.windows.foundation.IAsyncOperation[ActivitySensorReading]:
        ...
    def get_default_async() -> winsdk.windows.foundation.IAsyncOperation[ActivitySensor]:
        ...
    def get_device_selector() -> str:
        ...
    def get_system_history_async(from_time: winsdk.windows.foundation.DateTime) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[ActivitySensorReading]]:
        ...
    def get_system_history_async(from_time: winsdk.windows.foundation.DateTime, duration: winsdk.windows.foundation.TimeSpan) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[ActivitySensorReading]]:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[ActivitySensor, ActivitySensorReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ActivitySensorReading(_winrt.Object):
    ...
    activity: ActivityType
    confidence: ActivitySensorReadingConfidence
    timestamp: winsdk.windows.foundation.DateTime

class ActivitySensorReadingChangeReport(_winrt.Object):
    ...
    reading: ActivitySensorReading

class ActivitySensorReadingChangedEventArgs(_winrt.Object):
    ...
    reading: ActivitySensorReading

class ActivitySensorTriggerDetails(_winrt.Object):
    ...
    def read_reports() -> winsdk.windows.foundation.collections.IVectorView[ActivitySensorReadingChangeReport]:
        ...

class Altimeter(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    device_id: str
    minimum_report_interval: _winrt.UInt32
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    def get_current_reading() -> AltimeterReading:
        ...
    def get_default() -> Altimeter:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Altimeter, AltimeterReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class AltimeterReading(_winrt.Object):
    ...
    altitude_change_in_meters: _winrt.Double
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]

class AltimeterReadingChangedEventArgs(_winrt.Object):
    ...
    reading: AltimeterReading

class Barometer(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    device_id: str
    minimum_report_interval: _winrt.UInt32
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    report_threshold: BarometerDataThreshold
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Barometer]:
        ...
    def get_current_reading() -> BarometerReading:
        ...
    def get_default() -> Barometer:
        ...
    def get_device_selector() -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Barometer, BarometerReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class BarometerDataThreshold(_winrt.Object):
    ...
    hectopascals: _winrt.Double

class BarometerReading(_winrt.Object):
    ...
    station_pressure_in_hectopascals: _winrt.Double
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]

class BarometerReadingChangedEventArgs(_winrt.Object):
    ...
    reading: BarometerReading

class Compass(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    minimum_report_interval: _winrt.UInt32
    reading_transform: winsdk.windows.graphics.display.DisplayOrientations
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    report_threshold: CompassDataThreshold
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Compass]:
        ...
    def get_current_reading() -> CompassReading:
        ...
    def get_default() -> Compass:
        ...
    def get_device_selector() -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Compass, CompassReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class CompassDataThreshold(_winrt.Object):
    ...
    degrees: _winrt.Double

class CompassReading(_winrt.Object):
    ...
    heading_magnetic_north: _winrt.Double
    heading_true_north: typing.Optional[_winrt.Double]
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]
    heading_accuracy: MagnetometerAccuracy

class CompassReadingChangedEventArgs(_winrt.Object):
    ...
    reading: CompassReading

class Gyrometer(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    minimum_report_interval: _winrt.UInt32
    reading_transform: winsdk.windows.graphics.display.DisplayOrientations
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    report_threshold: GyrometerDataThreshold
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Gyrometer]:
        ...
    def get_current_reading() -> GyrometerReading:
        ...
    def get_default() -> Gyrometer:
        ...
    def get_device_selector() -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Gyrometer, GyrometerReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class GyrometerDataThreshold(_winrt.Object):
    ...
    z_axis_in_degrees_per_second: _winrt.Double
    y_axis_in_degrees_per_second: _winrt.Double
    x_axis_in_degrees_per_second: _winrt.Double

class GyrometerReading(_winrt.Object):
    ...
    angular_velocity_x: _winrt.Double
    angular_velocity_y: _winrt.Double
    angular_velocity_z: _winrt.Double
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]

class GyrometerReadingChangedEventArgs(_winrt.Object):
    ...
    reading: GyrometerReading

class HingeAngleReading(_winrt.Object):
    ...
    angle_in_degrees: _winrt.Double
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]
    timestamp: winsdk.windows.foundation.DateTime

class HingeAngleSensor(_winrt.Object):
    ...
    report_threshold_in_degrees: _winrt.Double
    device_id: str
    min_report_threshold_in_degrees: _winrt.Double
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[HingeAngleSensor]:
        ...
    def get_current_reading_async() -> winsdk.windows.foundation.IAsyncOperation[HingeAngleReading]:
        ...
    def get_default_async() -> winsdk.windows.foundation.IAsyncOperation[HingeAngleSensor]:
        ...
    def get_device_selector() -> str:
        ...
    def get_related_to_adjacent_panels_async(first_panel_id: str, second_panel_id: str) -> winsdk.windows.foundation.IAsyncOperation[HingeAngleSensor]:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[HingeAngleSensor, HingeAngleSensorReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class HingeAngleSensorReadingChangedEventArgs(_winrt.Object):
    ...
    reading: HingeAngleReading

class Inclinometer(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    minimum_report_interval: _winrt.UInt32
    reading_transform: winsdk.windows.graphics.display.DisplayOrientations
    reading_type: SensorReadingType
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    report_threshold: InclinometerDataThreshold
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Inclinometer]:
        ...
    def get_current_reading() -> InclinometerReading:
        ...
    def get_default() -> Inclinometer:
        ...
    def get_default(sensor_readingtype: SensorReadingType) -> Inclinometer:
        ...
    def get_default_for_relative_readings() -> Inclinometer:
        ...
    def get_device_selector(reading_type: SensorReadingType) -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Inclinometer, InclinometerReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class InclinometerDataThreshold(_winrt.Object):
    ...
    yaw_in_degrees: _winrt.Single
    roll_in_degrees: _winrt.Single
    pitch_in_degrees: _winrt.Single

class InclinometerReading(_winrt.Object):
    ...
    pitch_degrees: _winrt.Single
    roll_degrees: _winrt.Single
    timestamp: winsdk.windows.foundation.DateTime
    yaw_degrees: _winrt.Single
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]
    yaw_accuracy: MagnetometerAccuracy

class InclinometerReadingChangedEventArgs(_winrt.Object):
    ...
    reading: InclinometerReading

class LightSensor(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    minimum_report_interval: _winrt.UInt32
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    report_threshold: LightSensorDataThreshold
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[LightSensor]:
        ...
    def get_current_reading() -> LightSensorReading:
        ...
    def get_default() -> LightSensor:
        ...
    def get_device_selector() -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[LightSensor, LightSensorReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class LightSensorDataThreshold(_winrt.Object):
    ...
    lux_percentage: _winrt.Single
    absolute_lux: _winrt.Single

class LightSensorReading(_winrt.Object):
    ...
    illuminance_in_lux: _winrt.Single
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]

class LightSensorReadingChangedEventArgs(_winrt.Object):
    ...
    reading: LightSensorReading

class Magnetometer(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    minimum_report_interval: _winrt.UInt32
    reading_transform: winsdk.windows.graphics.display.DisplayOrientations
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    report_threshold: MagnetometerDataThreshold
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Magnetometer]:
        ...
    def get_current_reading() -> MagnetometerReading:
        ...
    def get_default() -> Magnetometer:
        ...
    def get_device_selector() -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Magnetometer, MagnetometerReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class MagnetometerDataThreshold(_winrt.Object):
    ...
    z_axis_microteslas: _winrt.Single
    y_axis_microteslas: _winrt.Single
    x_axis_microteslas: _winrt.Single

class MagnetometerReading(_winrt.Object):
    ...
    directional_accuracy: MagnetometerAccuracy
    magnetic_field_x: _winrt.Single
    magnetic_field_y: _winrt.Single
    magnetic_field_z: _winrt.Single
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]

class MagnetometerReadingChangedEventArgs(_winrt.Object):
    ...
    reading: MagnetometerReading

class OrientationSensor(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    minimum_report_interval: _winrt.UInt32
    reading_transform: winsdk.windows.graphics.display.DisplayOrientations
    reading_type: SensorReadingType
    report_latency: _winrt.UInt32
    max_batch_size: _winrt.UInt32
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[OrientationSensor]:
        ...
    def get_current_reading() -> OrientationSensorReading:
        ...
    def get_default() -> OrientationSensor:
        ...
    def get_default(sensor_readingtype: SensorReadingType) -> OrientationSensor:
        ...
    def get_default(sensor_reading_type: SensorReadingType, optimization_goal: SensorOptimizationGoal) -> OrientationSensor:
        ...
    def get_default_for_relative_readings() -> OrientationSensor:
        ...
    def get_device_selector(reading_type: SensorReadingType) -> str:
        ...
    def get_device_selector(reading_type: SensorReadingType, optimization_goal: SensorOptimizationGoal) -> str:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[OrientationSensor, OrientationSensorReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class OrientationSensorReading(_winrt.Object):
    ...
    quaternion: SensorQuaternion
    rotation_matrix: SensorRotationMatrix
    timestamp: winsdk.windows.foundation.DateTime
    performance_count: typing.Optional[winsdk.windows.foundation.TimeSpan]
    properties: winsdk.windows.foundation.collections.IMapView[str, _winrt.Object]
    yaw_accuracy: MagnetometerAccuracy

class OrientationSensorReadingChangedEventArgs(_winrt.Object):
    ...
    reading: OrientationSensorReading

class Pedometer(_winrt.Object):
    ...
    report_interval: _winrt.UInt32
    device_id: str
    minimum_report_interval: _winrt.UInt32
    power_in_milliwatts: _winrt.Double
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[Pedometer]:
        ...
    def get_current_readings() -> winsdk.windows.foundation.collections.IMapView[PedometerStepKind, PedometerReading]:
        ...
    def get_default_async() -> winsdk.windows.foundation.IAsyncOperation[Pedometer]:
        ...
    def get_device_selector() -> str:
        ...
    def get_readings_from_trigger_details(trigger_details: SensorDataThresholdTriggerDetails) -> winsdk.windows.foundation.collections.IVectorView[PedometerReading]:
        ...
    def get_system_history_async(from_time: winsdk.windows.foundation.DateTime) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[PedometerReading]]:
        ...
    def get_system_history_async(from_time: winsdk.windows.foundation.DateTime, duration: winsdk.windows.foundation.TimeSpan) -> winsdk.windows.foundation.IAsyncOperation[winsdk.windows.foundation.collections.IVectorView[PedometerReading]]:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[Pedometer, PedometerReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class PedometerDataThreshold(ISensorDataThreshold, _winrt.Object):
    ...
    def __init__(self, sensor: Pedometer, step_goal: _winrt.Int32) -> None:
        ...

class PedometerReading(_winrt.Object):
    ...
    cumulative_steps: _winrt.Int32
    cumulative_steps_duration: winsdk.windows.foundation.TimeSpan
    step_kind: PedometerStepKind
    timestamp: winsdk.windows.foundation.DateTime

class PedometerReadingChangedEventArgs(_winrt.Object):
    ...
    reading: PedometerReading

class ProximitySensor(_winrt.Object):
    ...
    device_id: str
    max_distance_in_millimeters: typing.Optional[_winrt.UInt32]
    min_distance_in_millimeters: typing.Optional[_winrt.UInt32]
    def create_display_on_off_controller() -> ProximitySensorDisplayOnOffController:
        ...
    def from_id(sensor_id: str) -> ProximitySensor:
        ...
    def get_current_reading() -> ProximitySensorReading:
        ...
    def get_device_selector() -> str:
        ...
    def get_readings_from_trigger_details(trigger_details: SensorDataThresholdTriggerDetails) -> winsdk.windows.foundation.collections.IVectorView[ProximitySensorReading]:
        ...
    def add_reading_changed(handler: winsdk.windows.foundation.TypedEventHandler[ProximitySensor, ProximitySensorReadingChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_reading_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class ProximitySensorDataThreshold(ISensorDataThreshold, _winrt.Object):
    ...
    def __init__(self, sensor: ProximitySensor) -> None:
        ...

class ProximitySensorDisplayOnOffController(winsdk.windows.foundation.IClosable, _winrt.Object):
    ...
    def close() -> None:
        ...

class ProximitySensorReading(_winrt.Object):
    ...
    distance_in_millimeters: typing.Optional[_winrt.UInt32]
    is_detected: _winrt.Boolean
    timestamp: winsdk.windows.foundation.DateTime

class ProximitySensorReadingChangedEventArgs(_winrt.Object):
    ...
    reading: ProximitySensorReading

class SensorDataThresholdTriggerDetails(_winrt.Object):
    ...
    device_id: str
    sensor_type: SensorType

class SensorQuaternion(_winrt.Object):
    ...
    w: _winrt.Single
    x: _winrt.Single
    y: _winrt.Single
    z: _winrt.Single

class SensorRotationMatrix(_winrt.Object):
    ...
    m11: _winrt.Single
    m12: _winrt.Single
    m13: _winrt.Single
    m21: _winrt.Single
    m22: _winrt.Single
    m23: _winrt.Single
    m31: _winrt.Single
    m32: _winrt.Single
    m33: _winrt.Single

class SimpleOrientationSensor(_winrt.Object):
    ...
    reading_transform: winsdk.windows.graphics.display.DisplayOrientations
    device_id: str
    def from_id_async(device_id: str) -> winsdk.windows.foundation.IAsyncOperation[SimpleOrientationSensor]:
        ...
    def get_current_orientation() -> SimpleOrientation:
        ...
    def get_default() -> SimpleOrientationSensor:
        ...
    def get_device_selector() -> str:
        ...
    def add_orientation_changed(handler: winsdk.windows.foundation.TypedEventHandler[SimpleOrientationSensor, SimpleOrientationSensorOrientationChangedEventArgs]) -> winsdk.windows.foundation.EventRegistrationToken:
        ...
    def remove_orientation_changed(token: winsdk.windows.foundation.EventRegistrationToken) -> None:
        ...

class SimpleOrientationSensorOrientationChangedEventArgs(_winrt.Object):
    ...
    orientation: SimpleOrientation
    timestamp: winsdk.windows.foundation.DateTime

class ISensorDataThreshold(_winrt.Object):
    ...

