// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Enumeration.h")
#include "py.Windows.Devices.Enumeration.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.UI.Popups.h")
#include "py.Windows.UI.Popups.h"
#endif

#include <winrt/Windows.Media.Casting.h>

namespace py::proj::Windows::Media::Casting
{}

namespace py::impl::Windows::Media::Casting
{}

namespace py::wrapper::Windows::Media::Casting
{
    using CastingConnection = py::winrt_wrapper<winrt::Windows::Media::Casting::CastingConnection>;
    using CastingConnectionErrorOccurredEventArgs = py::winrt_wrapper<winrt::Windows::Media::Casting::CastingConnectionErrorOccurredEventArgs>;
    using CastingDevice = py::winrt_wrapper<winrt::Windows::Media::Casting::CastingDevice>;
    using CastingDevicePicker = py::winrt_wrapper<winrt::Windows::Media::Casting::CastingDevicePicker>;
    using CastingDevicePickerFilter = py::winrt_wrapper<winrt::Windows::Media::Casting::CastingDevicePickerFilter>;
    using CastingDeviceSelectedEventArgs = py::winrt_wrapper<winrt::Windows::Media::Casting::CastingDeviceSelectedEventArgs>;
    using CastingSource = py::winrt_wrapper<winrt::Windows::Media::Casting::CastingSource>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Media::Casting::CastingConnection>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Casting::CastingConnectionErrorOccurredEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Casting::CastingDevice>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Casting::CastingDevicePicker>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Casting::CastingDevicePickerFilter>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Casting::CastingDeviceSelectedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Media::Casting::CastingSource>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
