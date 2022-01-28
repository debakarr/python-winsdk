// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.UI.Text.h")
#include "py.Windows.UI.Text.h"
#endif

#include <winrt/Windows.Globalization.Fonts.h>

namespace py::proj::Windows::Globalization::Fonts
{}

namespace py::impl::Windows::Globalization::Fonts
{}

namespace py::wrapper::Windows::Globalization::Fonts
{
    using LanguageFont = py::winrt_wrapper<winrt::Windows::Globalization::Fonts::LanguageFont>;
    using LanguageFontGroup = py::winrt_wrapper<winrt::Windows::Globalization::Fonts::LanguageFontGroup>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Globalization::Fonts::LanguageFont>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Globalization::Fonts::LanguageFontGroup>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
