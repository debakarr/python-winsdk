// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.Devices.Background.h>

namespace py::proj::Windows::Devices::Background
{}

namespace py::impl::Windows::Devices::Background
{}

namespace py::wrapper::Windows::Devices::Background
{
    using DeviceServicingDetails = py::winrt_wrapper<winrt::Windows::Devices::Background::DeviceServicingDetails>;
    using DeviceUseDetails = py::winrt_wrapper<winrt::Windows::Devices::Background::DeviceUseDetails>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Background::DeviceServicingDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Background::DeviceUseDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
