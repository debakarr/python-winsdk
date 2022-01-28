// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.HumanInterfaceDevice.h")
#include "py.Windows.Devices.HumanInterfaceDevice.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#include <winrt/Windows.Devices.Input.Preview.h>

namespace py::proj::Windows::Devices::Input::Preview
{}

namespace py::impl::Windows::Devices::Input::Preview
{}

namespace py::wrapper::Windows::Devices::Input::Preview
{
    using GazeDevicePreview = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeDevicePreview>;
    using GazeDeviceWatcherAddedPreviewEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherAddedPreviewEventArgs>;
    using GazeDeviceWatcherPreview = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherPreview>;
    using GazeDeviceWatcherRemovedPreviewEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherRemovedPreviewEventArgs>;
    using GazeDeviceWatcherUpdatedPreviewEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherUpdatedPreviewEventArgs>;
    using GazeEnteredPreviewEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeEnteredPreviewEventArgs>;
    using GazeExitedPreviewEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeExitedPreviewEventArgs>;
    using GazeInputSourcePreview = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeInputSourcePreview>;
    using GazeMovedPreviewEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazeMovedPreviewEventArgs>;
    using GazePointPreview = py::winrt_wrapper<winrt::Windows::Devices::Input::Preview::GazePointPreview>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeDevicePreview>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherAddedPreviewEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherPreview>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherRemovedPreviewEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeDeviceWatcherUpdatedPreviewEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeEnteredPreviewEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeExitedPreviewEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeInputSourcePreview>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazeMovedPreviewEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Input::Preview::GazePointPreview>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
