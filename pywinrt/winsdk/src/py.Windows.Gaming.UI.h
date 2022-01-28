// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.Gaming.UI.h>

namespace py::proj::Windows::Gaming::UI
{}

namespace py::impl::Windows::Gaming::UI
{}

namespace py::wrapper::Windows::Gaming::UI
{
    using GameBar = py::winrt_wrapper<winrt::Windows::Gaming::UI::GameBar>;
    using GameChatOverlay = py::winrt_wrapper<winrt::Windows::Gaming::UI::GameChatOverlay>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Gaming::UI::GameBar>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Gaming::UI::GameChatOverlay>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
