// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Security.Authentication.Identity.Provider.h>

namespace py::proj::Windows::Security::Authentication::Identity::Provider
{}

namespace py::impl::Windows::Security::Authentication::Identity::Provider
{}

namespace py::wrapper::Windows::Security::Authentication::Identity::Provider
{
    using SecondaryAuthenticationFactorAuthentication = py::winrt_wrapper<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthentication>;
    using SecondaryAuthenticationFactorAuthenticationResult = py::winrt_wrapper<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthenticationResult>;
    using SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs = py::winrt_wrapper<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs>;
    using SecondaryAuthenticationFactorAuthenticationStageInfo = py::winrt_wrapper<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthenticationStageInfo>;
    using SecondaryAuthenticationFactorInfo = py::winrt_wrapper<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorInfo>;
    using SecondaryAuthenticationFactorRegistration = py::winrt_wrapper<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorRegistration>;
    using SecondaryAuthenticationFactorRegistrationResult = py::winrt_wrapper<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorRegistrationResult>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthentication>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthenticationResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthenticationStageChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorAuthenticationStageInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorRegistration>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Security::Authentication::Identity::Provider::SecondaryAuthenticationFactorRegistrationResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
