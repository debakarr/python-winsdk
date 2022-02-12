// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Graphics.Display.h")
#include "py.Windows.Graphics.Display.h"
#endif

#include <winrt/Windows.Devices.Sensors.h>

namespace py::proj::Windows::Devices::Sensors
{}

namespace py::impl::Windows::Devices::Sensors
{}

namespace py::wrapper::Windows::Devices::Sensors
{
    using Accelerometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Accelerometer>;
    using AccelerometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerDataThreshold>;
    using AccelerometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerReading>;
    using AccelerometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerReadingChangedEventArgs>;
    using AccelerometerShakenEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerShakenEventArgs>;
    using ActivitySensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensor>;
    using ActivitySensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorReading>;
    using ActivitySensorReadingChangeReport = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangeReport>;
    using ActivitySensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangedEventArgs>;
    using ActivitySensorTriggerDetails = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorTriggerDetails>;
    using Altimeter = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Altimeter>;
    using AltimeterReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AltimeterReading>;
    using AltimeterReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AltimeterReadingChangedEventArgs>;
    using Barometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Barometer>;
    using BarometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::BarometerDataThreshold>;
    using BarometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::BarometerReading>;
    using BarometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::BarometerReadingChangedEventArgs>;
    using Compass = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Compass>;
    using CompassDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::CompassDataThreshold>;
    using CompassReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::CompassReading>;
    using CompassReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::CompassReadingChangedEventArgs>;
    using Gyrometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Gyrometer>;
    using GyrometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::GyrometerDataThreshold>;
    using GyrometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::GyrometerReading>;
    using GyrometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::GyrometerReadingChangedEventArgs>;
    using HingeAngleReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HingeAngleReading>;
    using HingeAngleSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HingeAngleSensor>;
    using HingeAngleSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HingeAngleSensorReadingChangedEventArgs>;
    using Inclinometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Inclinometer>;
    using InclinometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::InclinometerDataThreshold>;
    using InclinometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::InclinometerReading>;
    using InclinometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::InclinometerReadingChangedEventArgs>;
    using LightSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensor>;
    using LightSensorDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensorDataThreshold>;
    using LightSensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensorReading>;
    using LightSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensorReadingChangedEventArgs>;
    using Magnetometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Magnetometer>;
    using MagnetometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::MagnetometerDataThreshold>;
    using MagnetometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::MagnetometerReading>;
    using MagnetometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::MagnetometerReadingChangedEventArgs>;
    using OrientationSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::OrientationSensor>;
    using OrientationSensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::OrientationSensorReading>;
    using OrientationSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::OrientationSensorReadingChangedEventArgs>;
    using Pedometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Pedometer>;
    using PedometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::PedometerDataThreshold>;
    using PedometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::PedometerReading>;
    using PedometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::PedometerReadingChangedEventArgs>;
    using ProximitySensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensor>;
    using ProximitySensorDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorDataThreshold>;
    using ProximitySensorDisplayOnOffController = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorDisplayOnOffController>;
    using ProximitySensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorReading>;
    using ProximitySensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorReadingChangedEventArgs>;
    using SensorDataThresholdTriggerDetails = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SensorDataThresholdTriggerDetails>;
    using SensorQuaternion = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SensorQuaternion>;
    using SensorRotationMatrix = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SensorRotationMatrix>;
    using SimpleOrientationSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SimpleOrientationSensor>;
    using SimpleOrientationSensorOrientationChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SimpleOrientationSensorOrientationChangedEventArgs>;
    using ISensorDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ISensorDataThreshold>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Accelerometer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::AccelerometerDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::AccelerometerReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::AccelerometerReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::AccelerometerShakenEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ActivitySensor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ActivitySensorReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangeReport>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ActivitySensorTriggerDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Altimeter>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::AltimeterReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::AltimeterReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Barometer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::BarometerDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::BarometerReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::BarometerReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Compass>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::CompassDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::CompassReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::CompassReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Gyrometer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::GyrometerDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::GyrometerReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::GyrometerReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::HingeAngleReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::HingeAngleSensor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::HingeAngleSensorReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Inclinometer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::InclinometerDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::InclinometerReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::InclinometerReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::LightSensor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::LightSensorDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::LightSensorReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::LightSensorReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Magnetometer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::MagnetometerDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::MagnetometerReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::MagnetometerReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::OrientationSensor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::OrientationSensorReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::OrientationSensorReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Pedometer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::PedometerDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::PedometerReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::PedometerReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ProximitySensor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ProximitySensorDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ProximitySensorDisplayOnOffController>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ProximitySensorReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ProximitySensorReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::SensorDataThresholdTriggerDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::SensorQuaternion>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::SensorRotationMatrix>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::SimpleOrientationSensor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::SimpleOrientationSensorOrientationChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::ISensorDataThreshold>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
