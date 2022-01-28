// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.Devices.Sensors.Custom.h>

namespace py::proj::Windows::Devices::Sensors::Custom
{}

namespace py::impl::Windows::Devices::Sensors::Custom
{}

namespace py::wrapper::Windows::Devices::Sensors::Custom
{
    using CustomSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Custom::CustomSensor>;
    using CustomSensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Custom::CustomSensorReading>;
    using CustomSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensorReading>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
