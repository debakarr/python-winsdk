// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Haptics.h")
#include "py.Windows.Devices.Haptics.h"
#endif

#if __has_include("py.Windows.Devices.Input.h")
#include "py.Windows.Devices.Input.h"
#endif

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
#endif

#if __has_include("py.Windows.UI.Core.h")
#include "py.Windows.UI.Core.h"
#endif

#include <winrt/Windows.UI.Input.h>

namespace py::proj::Windows::UI::Input
{}

namespace py::impl::Windows::UI::Input
{}

namespace py::wrapper::Windows::UI::Input
{
    using AttachableInputObject = py::winrt_wrapper<winrt::Windows::UI::Input::AttachableInputObject>;
    using CrossSlidingEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::CrossSlidingEventArgs>;
    using DraggingEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::DraggingEventArgs>;
    using EdgeGesture = py::winrt_wrapper<winrt::Windows::UI::Input::EdgeGesture>;
    using EdgeGestureEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::EdgeGestureEventArgs>;
    using GestureRecognizer = py::winrt_wrapper<winrt::Windows::UI::Input::GestureRecognizer>;
    using HoldingEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::HoldingEventArgs>;
    using InputActivationListener = py::winrt_wrapper<winrt::Windows::UI::Input::InputActivationListener>;
    using InputActivationListenerActivationChangedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::InputActivationListenerActivationChangedEventArgs>;
    using KeyboardDeliveryInterceptor = py::winrt_wrapper<winrt::Windows::UI::Input::KeyboardDeliveryInterceptor>;
    using ManipulationCompletedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::ManipulationCompletedEventArgs>;
    using ManipulationInertiaStartingEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::ManipulationInertiaStartingEventArgs>;
    using ManipulationStartedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::ManipulationStartedEventArgs>;
    using ManipulationUpdatedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::ManipulationUpdatedEventArgs>;
    using MouseWheelParameters = py::winrt_wrapper<winrt::Windows::UI::Input::MouseWheelParameters>;
    using PointerPoint = py::winrt_wrapper<winrt::Windows::UI::Input::PointerPoint>;
    using PointerPointProperties = py::winrt_wrapper<winrt::Windows::UI::Input::PointerPointProperties>;
    using PointerVisualizationSettings = py::winrt_wrapper<winrt::Windows::UI::Input::PointerVisualizationSettings>;
    using RadialController = py::winrt_wrapper<winrt::Windows::UI::Input::RadialController>;
    using RadialControllerButtonClickedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerButtonClickedEventArgs>;
    using RadialControllerButtonHoldingEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerButtonHoldingEventArgs>;
    using RadialControllerButtonPressedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerButtonPressedEventArgs>;
    using RadialControllerButtonReleasedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerButtonReleasedEventArgs>;
    using RadialControllerConfiguration = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerConfiguration>;
    using RadialControllerControlAcquiredEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerControlAcquiredEventArgs>;
    using RadialControllerMenu = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerMenu>;
    using RadialControllerMenuItem = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerMenuItem>;
    using RadialControllerRotationChangedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerRotationChangedEventArgs>;
    using RadialControllerScreenContact = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerScreenContact>;
    using RadialControllerScreenContactContinuedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerScreenContactContinuedEventArgs>;
    using RadialControllerScreenContactEndedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerScreenContactEndedEventArgs>;
    using RadialControllerScreenContactStartedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RadialControllerScreenContactStartedEventArgs>;
    using RightTappedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::RightTappedEventArgs>;
    using SystemButtonEventController = py::winrt_wrapper<winrt::Windows::UI::Input::SystemButtonEventController>;
    using SystemFunctionButtonEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::SystemFunctionButtonEventArgs>;
    using SystemFunctionLockChangedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::SystemFunctionLockChangedEventArgs>;
    using SystemFunctionLockIndicatorChangedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::SystemFunctionLockIndicatorChangedEventArgs>;
    using TappedEventArgs = py::winrt_wrapper<winrt::Windows::UI::Input::TappedEventArgs>;
    using IPointerPointTransform = py::winrt_wrapper<winrt::Windows::UI::Input::IPointerPointTransform>;
    using CrossSlideThresholds = py::winrt_struct_wrapper<winrt::Windows::UI::Input::CrossSlideThresholds>;
    using ManipulationDelta = py::winrt_struct_wrapper<winrt::Windows::UI::Input::ManipulationDelta>;
    using ManipulationVelocities = py::winrt_struct_wrapper<winrt::Windows::UI::Input::ManipulationVelocities>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::UI::Input::AttachableInputObject>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::CrossSlidingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::DraggingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::EdgeGesture>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::EdgeGestureEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::GestureRecognizer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::HoldingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::InputActivationListener>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::InputActivationListenerActivationChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::KeyboardDeliveryInterceptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::ManipulationCompletedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::ManipulationInertiaStartingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::ManipulationStartedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::ManipulationUpdatedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::MouseWheelParameters>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::PointerPoint>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::PointerPointProperties>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::PointerVisualizationSettings>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialController>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerButtonClickedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerButtonHoldingEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerButtonPressedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerButtonReleasedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerConfiguration>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerControlAcquiredEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerMenu>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerMenuItem>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerRotationChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerScreenContact>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerScreenContactContinuedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerScreenContactEndedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RadialControllerScreenContactStartedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::RightTappedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::SystemButtonEventController>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::SystemFunctionButtonEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::SystemFunctionLockChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::SystemFunctionLockIndicatorChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::TappedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::IPointerPointTransform>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::CrossSlideThresholds>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::ManipulationDelta>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::UI::Input::ManipulationVelocities>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct converter<winrt::Windows::UI::Input::CrossSlideThresholds>
    {
        static PyObject* convert(winrt::Windows::UI::Input::CrossSlideThresholds instance) noexcept;
        static winrt::Windows::UI::Input::CrossSlideThresholds convert_to(PyObject* obj);
    };

    template<>
    struct converter<winrt::Windows::UI::Input::ManipulationDelta>
    {
        static PyObject* convert(winrt::Windows::UI::Input::ManipulationDelta instance) noexcept;
        static winrt::Windows::UI::Input::ManipulationDelta convert_to(PyObject* obj);
    };

    template<>
    struct converter<winrt::Windows::UI::Input::ManipulationVelocities>
    {
        static PyObject* convert(winrt::Windows::UI::Input::ManipulationVelocities instance) noexcept;
        static winrt::Windows::UI::Input::ManipulationVelocities convert_to(PyObject* obj);
    };

}
