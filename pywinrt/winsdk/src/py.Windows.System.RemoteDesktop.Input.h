// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#include <winrt/Windows.System.RemoteDesktop.Input.h>

namespace py::proj::Windows::System::RemoteDesktop::Input
{}

namespace py::impl::Windows::System::RemoteDesktop::Input
{
    struct RemoteTextConnectionDataHandler
    {
        static winrt::Windows::System::RemoteDesktop::Input::RemoteTextConnectionDataHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)](auto param0)
            {
                winrt::handle_type<py::gil_state_traits> gil_state{ PyGILState_Ensure() };

                py::pyobj_handle py_param0{ py::convert(param0) };

                py::pyobj_handle args{ PyTuple_Pack(1, py_param0.get()) };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_invalid_argument();
                }

                return py::convert<bool>(return_value.get());
            };
        };
    };
}

namespace py::wrapper::Windows::System::RemoteDesktop::Input
{
    using RemoteTextConnection = py::winrt_wrapper<winrt::Windows::System::RemoteDesktop::Input::RemoteTextConnection>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::System::RemoteDesktop::Input::RemoteTextConnection>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template <>
    struct delegate_python_type<winrt::Windows::System::RemoteDesktop::Input::RemoteTextConnectionDataHandler>
    {
        using type = py::impl::Windows::System::RemoteDesktop::Input::RemoteTextConnectionDataHandler;
    };

}
