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

#if __has_include("py.Windows.Networking.h")
#include "py.Windows.Networking.h"
#endif

#if __has_include("py.Windows.Networking.Sockets.h")
#include "py.Windows.Networking.Sockets.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Devices.WiFiDirect.Services.h>

namespace py::proj::Windows::Devices::WiFiDirect::Services
{}

namespace py::impl::Windows::Devices::WiFiDirect::Services
{}

namespace py::wrapper::Windows::Devices::WiFiDirect::Services
{
    using WiFiDirectService = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectService>;
    using WiFiDirectServiceAdvertiser = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceAdvertiser>;
    using WiFiDirectServiceAutoAcceptSessionConnectedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceAutoAcceptSessionConnectedEventArgs>;
    using WiFiDirectServiceProvisioningInfo = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceProvisioningInfo>;
    using WiFiDirectServiceRemotePortAddedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceRemotePortAddedEventArgs>;
    using WiFiDirectServiceSession = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSession>;
    using WiFiDirectServiceSessionDeferredEventArgs = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSessionDeferredEventArgs>;
    using WiFiDirectServiceSessionRequest = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSessionRequest>;
    using WiFiDirectServiceSessionRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSessionRequestedEventArgs>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectService>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceAdvertiser>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceAutoAcceptSessionConnectedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceProvisioningInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceRemotePortAddedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSession>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSessionDeferredEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSessionRequest>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::WiFiDirect::Services::WiFiDirectServiceSessionRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
