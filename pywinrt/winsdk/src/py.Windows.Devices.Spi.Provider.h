// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.Devices.Spi.Provider.h>

namespace py::proj::Windows::Devices::Spi::Provider
{}

namespace py::impl::Windows::Devices::Spi::Provider
{}

namespace py::wrapper::Windows::Devices::Spi::Provider
{
    using ProviderSpiConnectionSettings = py::winrt_wrapper<winrt::Windows::Devices::Spi::Provider::ProviderSpiConnectionSettings>;
    using ISpiControllerProvider = py::winrt_wrapper<winrt::Windows::Devices::Spi::Provider::ISpiControllerProvider>;
    using ISpiDeviceProvider = py::winrt_wrapper<winrt::Windows::Devices::Spi::Provider::ISpiDeviceProvider>;
    using ISpiProvider = py::winrt_wrapper<winrt::Windows::Devices::Spi::Provider::ISpiProvider>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Spi::Provider::ProviderSpiConnectionSettings>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Spi::Provider::ISpiControllerProvider>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Spi::Provider::ISpiDeviceProvider>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Spi::Provider::ISpiProvider>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
