// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.UI.Composition.h")
#include "py.Windows.UI.Composition.h"
#endif

#include <winrt/Windows.UI.Input.Inking.Preview.h>

namespace py::proj::Windows::UI::Input::Inking::Preview
{}

namespace py::impl::Windows::UI::Input::Inking::Preview
{}

namespace py::wrapper::Windows::UI::Input::Inking::Preview
{
    using PalmRejectionDelayZonePreview = py::winrt_wrapper<winrt::Windows::UI::Input::Inking::Preview::PalmRejectionDelayZonePreview>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::UI::Input::Inking::Preview::PalmRejectionDelayZonePreview>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
