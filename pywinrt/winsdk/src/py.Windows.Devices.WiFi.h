// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Networking.Connectivity.h")
#include "py.Windows.Networking.Connectivity.h"
#endif

#if __has_include("py.Windows.Security.Credentials.h")
#include "py.Windows.Security.Credentials.h"
#endif

#include <winrt/Windows.Devices.WiFi.h>

namespace py::proj::Windows::Devices::WiFi
{}

namespace py::impl::Windows::Devices::WiFi
{}

namespace py::wrapper::Windows::Devices::WiFi
{
    using WiFiAdapter = py::winrt_wrapper<winrt::Windows::Devices::WiFi::WiFiAdapter>;
    using WiFiAvailableNetwork = py::winrt_wrapper<winrt::Windows::Devices::WiFi::WiFiAvailableNetwork>;
    using WiFiConnectionResult = py::winrt_wrapper<winrt::Windows::Devices::WiFi::WiFiConnectionResult>;
    using WiFiNetworkReport = py::winrt_wrapper<winrt::Windows::Devices::WiFi::WiFiNetworkReport>;
    using WiFiWpsConfigurationResult = py::winrt_wrapper<winrt::Windows::Devices::WiFi::WiFiWpsConfigurationResult>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::WiFi::WiFiAdapter>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFi::WiFiAvailableNetwork>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFi::WiFiConnectionResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFi::WiFiNetworkReport>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFi::WiFiWpsConfigurationResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
