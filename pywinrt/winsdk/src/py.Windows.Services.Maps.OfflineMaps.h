// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Geolocation.h")
#include "py.Windows.Devices.Geolocation.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.Services.Maps.OfflineMaps.h>

namespace py::proj::Windows::Services::Maps::OfflineMaps
{}

namespace py::impl::Windows::Services::Maps::OfflineMaps
{}

namespace py::wrapper::Windows::Services::Maps::OfflineMaps
{
    using OfflineMapPackage = py::winrt_wrapper<winrt::Windows::Services::Maps::OfflineMaps::OfflineMapPackage>;
    using OfflineMapPackageQueryResult = py::winrt_wrapper<winrt::Windows::Services::Maps::OfflineMaps::OfflineMapPackageQueryResult>;
    using OfflineMapPackageStartDownloadResult = py::winrt_wrapper<winrt::Windows::Services::Maps::OfflineMaps::OfflineMapPackageStartDownloadResult>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Services::Maps::OfflineMaps::OfflineMapPackage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::OfflineMaps::OfflineMapPackageQueryResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Services::Maps::OfflineMaps::OfflineMapPackageStartDownloadResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
