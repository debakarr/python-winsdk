// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.h")
#include "py.Windows.ApplicationModel.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
#endif

#if __has_include("py.Windows.System.RemoteSystems.h")
#include "py.Windows.System.RemoteSystems.h"
#endif

#include <winrt/Windows.ApplicationModel.AppService.h>

namespace py::proj::Windows::ApplicationModel::AppService
{}

namespace py::impl::Windows::ApplicationModel::AppService
{}

namespace py::wrapper::Windows::ApplicationModel::AppService
{
    using AppServiceCatalog = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceCatalog>;
    using AppServiceClosedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceClosedEventArgs>;
    using AppServiceConnection = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceConnection>;
    using AppServiceDeferral = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceDeferral>;
    using AppServiceRequest = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceRequest>;
    using AppServiceRequestReceivedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceRequestReceivedEventArgs>;
    using AppServiceResponse = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceResponse>;
    using AppServiceTriggerDetails = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::AppServiceTriggerDetails>;
    using StatelessAppServiceResponse = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppService::StatelessAppServiceResponse>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceCatalog>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceClosedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceConnection>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceRequest>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceRequestReceivedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceResponse>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::AppServiceTriggerDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppService::StatelessAppServiceResponse>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
