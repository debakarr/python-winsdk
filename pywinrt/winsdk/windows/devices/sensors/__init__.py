# WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

import enum

import winsdk

_ns_module = winsdk._import_ns_module("Windows.Devices.Sensors")

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

Accelerometer = _ns_module.Accelerometer
AccelerometerDataThreshold = _ns_module.AccelerometerDataThreshold
AccelerometerReading = _ns_module.AccelerometerReading
AccelerometerReadingChangedEventArgs = _ns_module.AccelerometerReadingChangedEventArgs
AccelerometerShakenEventArgs = _ns_module.AccelerometerShakenEventArgs
ActivitySensor = _ns_module.ActivitySensor
ActivitySensorReading = _ns_module.ActivitySensorReading
ActivitySensorReadingChangeReport = _ns_module.ActivitySensorReadingChangeReport
ActivitySensorReadingChangedEventArgs = _ns_module.ActivitySensorReadingChangedEventArgs
ActivitySensorTriggerDetails = _ns_module.ActivitySensorTriggerDetails
Altimeter = _ns_module.Altimeter
AltimeterReading = _ns_module.AltimeterReading
AltimeterReadingChangedEventArgs = _ns_module.AltimeterReadingChangedEventArgs
Barometer = _ns_module.Barometer
BarometerDataThreshold = _ns_module.BarometerDataThreshold
BarometerReading = _ns_module.BarometerReading
BarometerReadingChangedEventArgs = _ns_module.BarometerReadingChangedEventArgs
Compass = _ns_module.Compass
CompassDataThreshold = _ns_module.CompassDataThreshold
CompassReading = _ns_module.CompassReading
CompassReadingChangedEventArgs = _ns_module.CompassReadingChangedEventArgs
Gyrometer = _ns_module.Gyrometer
GyrometerDataThreshold = _ns_module.GyrometerDataThreshold
GyrometerReading = _ns_module.GyrometerReading
GyrometerReadingChangedEventArgs = _ns_module.GyrometerReadingChangedEventArgs
HingeAngleReading = _ns_module.HingeAngleReading
HingeAngleSensor = _ns_module.HingeAngleSensor
HingeAngleSensorReadingChangedEventArgs = _ns_module.HingeAngleSensorReadingChangedEventArgs
Inclinometer = _ns_module.Inclinometer
InclinometerDataThreshold = _ns_module.InclinometerDataThreshold
InclinometerReading = _ns_module.InclinometerReading
InclinometerReadingChangedEventArgs = _ns_module.InclinometerReadingChangedEventArgs
LightSensor = _ns_module.LightSensor
LightSensorDataThreshold = _ns_module.LightSensorDataThreshold
LightSensorReading = _ns_module.LightSensorReading
LightSensorReadingChangedEventArgs = _ns_module.LightSensorReadingChangedEventArgs
Magnetometer = _ns_module.Magnetometer
MagnetometerDataThreshold = _ns_module.MagnetometerDataThreshold
MagnetometerReading = _ns_module.MagnetometerReading
MagnetometerReadingChangedEventArgs = _ns_module.MagnetometerReadingChangedEventArgs
OrientationSensor = _ns_module.OrientationSensor
OrientationSensorReading = _ns_module.OrientationSensorReading
OrientationSensorReadingChangedEventArgs = _ns_module.OrientationSensorReadingChangedEventArgs
Pedometer = _ns_module.Pedometer
PedometerDataThreshold = _ns_module.PedometerDataThreshold
PedometerReading = _ns_module.PedometerReading
PedometerReadingChangedEventArgs = _ns_module.PedometerReadingChangedEventArgs
ProximitySensor = _ns_module.ProximitySensor
ProximitySensorDataThreshold = _ns_module.ProximitySensorDataThreshold
ProximitySensorDisplayOnOffController = _ns_module.ProximitySensorDisplayOnOffController
ProximitySensorReading = _ns_module.ProximitySensorReading
ProximitySensorReadingChangedEventArgs = _ns_module.ProximitySensorReadingChangedEventArgs
SensorDataThresholdTriggerDetails = _ns_module.SensorDataThresholdTriggerDetails
SensorQuaternion = _ns_module.SensorQuaternion
SensorRotationMatrix = _ns_module.SensorRotationMatrix
SimpleOrientationSensor = _ns_module.SimpleOrientationSensor
SimpleOrientationSensorOrientationChangedEventArgs = _ns_module.SimpleOrientationSensorOrientationChangedEventArgs
ISensorDataThreshold = _ns_module.ISensorDataThreshold
