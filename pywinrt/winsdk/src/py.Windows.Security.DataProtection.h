// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Storage.h")
#include "py.Windows.Storage.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
#endif

#include <winrt/Windows.Security.DataProtection.h>

namespace py::proj::Windows::Security::DataProtection
{}

namespace py::impl::Windows::Security::DataProtection
{}

namespace py::wrapper::Windows::Security::DataProtection
{
    using UserDataAvailabilityStateChangedEventArgs = py::winrt_wrapper<winrt::Windows::Security::DataProtection::UserDataAvailabilityStateChangedEventArgs>;
    using UserDataBufferUnprotectResult = py::winrt_wrapper<winrt::Windows::Security::DataProtection::UserDataBufferUnprotectResult>;
    using UserDataProtectionManager = py::winrt_wrapper<winrt::Windows::Security::DataProtection::UserDataProtectionManager>;
    using UserDataStorageItemProtectionInfo = py::winrt_wrapper<winrt::Windows::Security::DataProtection::UserDataStorageItemProtectionInfo>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Security::DataProtection::UserDataAvailabilityStateChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::DataProtection::UserDataBufferUnprotectResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::DataProtection::UserDataProtectionManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::DataProtection::UserDataStorageItemProtectionInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
