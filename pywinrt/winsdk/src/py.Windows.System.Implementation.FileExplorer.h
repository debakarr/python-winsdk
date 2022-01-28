// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Web.Http.h")
#include "py.Windows.Web.Http.h"
#endif

#include <winrt/Windows.System.Implementation.FileExplorer.h>

namespace py::proj::Windows::System::Implementation::FileExplorer
{}

namespace py::impl::Windows::System::Implementation::FileExplorer
{}

namespace py::wrapper::Windows::System::Implementation::FileExplorer
{
    using SysStorageProviderEventReceivedEventArgs = py::winrt_wrapper<winrt::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs>;
    using ISysStorageProviderEventSource = py::winrt_wrapper<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource>;
    using ISysStorageProviderHandlerFactory = py::winrt_wrapper<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory>;
    using ISysStorageProviderHttpRequestProvider = py::winrt_wrapper<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
