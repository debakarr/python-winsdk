// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.ApplicationModel.Activation.h")
#include "py.Windows.ApplicationModel.Activation.h"
#endif

#if __has_include("py.Windows.ApplicationModel.Core.h")
#include "py.Windows.ApplicationModel.Core.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
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

#include <winrt/Windows.ApplicationModel.h>

namespace py::proj::Windows::ApplicationModel
{}

namespace py::impl::Windows::ApplicationModel
{}

namespace py::wrapper::Windows::ApplicationModel
{
    using AppDisplayInfo = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppDisplayInfo>;
    using AppInfo = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppInfo>;
    using AppInstallerInfo = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppInstallerInfo>;
    using AppInstance = py::winrt_wrapper<winrt::Windows::ApplicationModel::AppInstance>;
    using DesignMode = py::winrt_wrapper<winrt::Windows::ApplicationModel::DesignMode>;
    using EnteredBackgroundEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::EnteredBackgroundEventArgs>;
    using LeavingBackgroundEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::LeavingBackgroundEventArgs>;
    using LimitedAccessFeatureRequestResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::LimitedAccessFeatureRequestResult>;
    using LimitedAccessFeatures = py::winrt_wrapper<winrt::Windows::ApplicationModel::LimitedAccessFeatures>;
    using Package = py::winrt_wrapper<winrt::Windows::ApplicationModel::Package>;
    using PackageCatalog = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageCatalog>;
    using PackageCatalogAddOptionalPackageResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageCatalogAddOptionalPackageResult>;
    using PackageCatalogAddResourcePackageResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageCatalogAddResourcePackageResult>;
    using PackageCatalogRemoveOptionalPackagesResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageCatalogRemoveOptionalPackagesResult>;
    using PackageCatalogRemoveResourcePackagesResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageCatalogRemoveResourcePackagesResult>;
    using PackageContentGroup = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageContentGroup>;
    using PackageContentGroupStagingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageContentGroupStagingEventArgs>;
    using PackageId = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageId>;
    using PackageInstallingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageInstallingEventArgs>;
    using PackageStagingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageStagingEventArgs>;
    using PackageStatus = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageStatus>;
    using PackageStatusChangedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageStatusChangedEventArgs>;
    using PackageUninstallingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageUninstallingEventArgs>;
    using PackageUpdateAvailabilityResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageUpdateAvailabilityResult>;
    using PackageUpdatingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::PackageUpdatingEventArgs>;
    using StartupTask = py::winrt_wrapper<winrt::Windows::ApplicationModel::StartupTask>;
    using SuspendingDeferral = py::winrt_wrapper<winrt::Windows::ApplicationModel::SuspendingDeferral>;
    using SuspendingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::SuspendingEventArgs>;
    using SuspendingOperation = py::winrt_wrapper<winrt::Windows::ApplicationModel::SuspendingOperation>;
    using IEnteredBackgroundEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::IEnteredBackgroundEventArgs>;
    using ILeavingBackgroundEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::ILeavingBackgroundEventArgs>;
    using ISuspendingDeferral = py::winrt_wrapper<winrt::Windows::ApplicationModel::ISuspendingDeferral>;
    using ISuspendingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::ISuspendingEventArgs>;
    using ISuspendingOperation = py::winrt_wrapper<winrt::Windows::ApplicationModel::ISuspendingOperation>;
    using PackageInstallProgress = py::winrt_struct_wrapper<winrt::Windows::ApplicationModel::PackageInstallProgress>;
    using PackageVersion = py::winrt_struct_wrapper<winrt::Windows::ApplicationModel::PackageVersion>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppDisplayInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppInstallerInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::AppInstance>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::DesignMode>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::EnteredBackgroundEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LeavingBackgroundEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LimitedAccessFeatureRequestResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LimitedAccessFeatures>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Package>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageCatalog>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageCatalogAddOptionalPackageResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageCatalogAddResourcePackageResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageCatalogRemoveOptionalPackagesResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageCatalogRemoveResourcePackagesResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageContentGroup>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageContentGroupStagingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageId>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageInstallingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageStagingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageStatus>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageStatusChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageUninstallingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageUpdateAvailabilityResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageUpdatingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::StartupTask>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::SuspendingDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::SuspendingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::SuspendingOperation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::IEnteredBackgroundEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ILeavingBackgroundEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ISuspendingDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ISuspendingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ISuspendingOperation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageInstallProgress>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::PackageVersion>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct converter<winrt::Windows::ApplicationModel::PackageInstallProgress>
    {
        static PyObject* convert(winrt::Windows::ApplicationModel::PackageInstallProgress instance) noexcept;
        static winrt::Windows::ApplicationModel::PackageInstallProgress convert_to(PyObject* obj);
    };

    template<>
    struct converter<winrt::Windows::ApplicationModel::PackageVersion>
    {
        static PyObject* convert(winrt::Windows::ApplicationModel::PackageVersion instance) noexcept;
        static winrt::Windows::ApplicationModel::PackageVersion convert_to(PyObject* obj);
    };

}
