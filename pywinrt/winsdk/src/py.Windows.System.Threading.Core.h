// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.System.Threading.h")
#include "py.Windows.System.Threading.h"
#endif

#include <winrt/Windows.System.Threading.Core.h>

namespace py::proj::Windows::System::Threading::Core
{}

namespace py::impl::Windows::System::Threading::Core
{
    struct SignalHandler
    {
        static winrt::Windows::System::Threading::Core::SignalHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0, auto param1)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };
                py::pyobj_handle py_param1{ py::convert(param1) };

                py::pyobj_handle args{ PyTuple_Pack(2, py_param0.get(), py_param1.get()) };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_invalid_argument();
                }
            };
        };
    };
}

namespace py::wrapper::Windows::System::Threading::Core
{
    using PreallocatedWorkItem = py::winrt_wrapper<winrt::Windows::System::Threading::Core::PreallocatedWorkItem>;
    using SignalNotifier = py::winrt_wrapper<winrt::Windows::System::Threading::Core::SignalNotifier>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::System::Threading::Core::PreallocatedWorkItem>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::System::Threading::Core::SignalNotifier>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template <>
    struct delegate_python_type<winrt::Windows::System::Threading::Core::SignalHandler>
    {
        using type = py::impl::Windows::System::Threading::Core::SignalHandler;
    };

}
