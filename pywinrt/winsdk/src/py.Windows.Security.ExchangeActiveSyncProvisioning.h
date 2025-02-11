// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.Security.ExchangeActiveSyncProvisioning.h>

namespace py::proj::Windows::Security::ExchangeActiveSyncProvisioning
{}

namespace py::impl::Windows::Security::ExchangeActiveSyncProvisioning
{}

namespace py::wrapper::Windows::Security::ExchangeActiveSyncProvisioning
{
    using EasClientDeviceInformation = py::winrt_wrapper<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasClientDeviceInformation>;
    using EasClientSecurityPolicy = py::winrt_wrapper<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasClientSecurityPolicy>;
    using EasComplianceResults = py::winrt_wrapper<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasComplianceResults>;
}

namespace py
{

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasDisallowConvenienceLogonResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasEncryptionProviderType>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasMaxInactivityTimeLockResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasMaxPasswordFailedAttemptsResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasMinPasswordComplexCharactersResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasMinPasswordLengthResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasPasswordExpirationResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasPasswordHistoryResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct py_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasRequireEncryptionResult>
    {
        static PyObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasClientDeviceInformation>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasClientSecurityPolicy>
    {
        static PyTypeObject* get_python_type() noexcept;
    };

    template<>
    struct winrt_type<winrt::Windows::Security::ExchangeActiveSyncProvisioning::EasComplianceResults>
    {
        static PyTypeObject* get_python_type() noexcept;
    };
}
