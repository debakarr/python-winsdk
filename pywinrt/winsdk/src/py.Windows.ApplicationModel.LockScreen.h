// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

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

#include <winrt/Windows.ApplicationModel.LockScreen.h>

namespace py::proj::Windows::ApplicationModel::LockScreen
{}

namespace py::impl::Windows::ApplicationModel::LockScreen
{}

namespace py::wrapper::Windows::ApplicationModel::LockScreen
{
    using LockApplicationHost = py::winrt_wrapper<winrt::Windows::ApplicationModel::LockScreen::LockApplicationHost>;
    using LockScreenBadge = py::winrt_wrapper<winrt::Windows::ApplicationModel::LockScreen::LockScreenBadge>;
    using LockScreenInfo = py::winrt_wrapper<winrt::Windows::ApplicationModel::LockScreen::LockScreenInfo>;
    using LockScreenUnlockingDeferral = py::winrt_wrapper<winrt::Windows::ApplicationModel::LockScreen::LockScreenUnlockingDeferral>;
    using LockScreenUnlockingEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::LockScreen::LockScreenUnlockingEventArgs>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LockScreen::LockApplicationHost>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LockScreen::LockScreenBadge>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LockScreen::LockScreenInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LockScreen::LockScreenUnlockingDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::LockScreen::LockScreenUnlockingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
