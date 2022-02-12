// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#include <winrt/Windows.Graphics.Effects.h>

namespace py::proj::Windows::Graphics::Effects
{}

namespace py::impl::Windows::Graphics::Effects
{}

namespace py::wrapper::Windows::Graphics::Effects
{
    using IGraphicsEffect = py::winrt_wrapper<winrt::Windows::Graphics::Effects::IGraphicsEffect>;
    using IGraphicsEffectSource = py::winrt_wrapper<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Graphics::Effects::IGraphicsEffect>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
