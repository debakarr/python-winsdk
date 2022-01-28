// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Networking.h")
#include "py.Windows.Networking.h"
#endif

#if __has_include("py.Windows.Networking.Sockets.h")
#include "py.Windows.Networking.Sockets.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.Networking.Proximity.h>

namespace py::proj::Windows::Networking::Proximity
{}

namespace py::impl::Windows::Networking::Proximity
{
    struct DeviceArrivedEventHandler
    {
        static winrt::Windows::Networking::Proximity::DeviceArrivedEventHandler get(PyObject* callable)
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
            };
        };
    };

    struct DeviceDepartedEventHandler
    {
        static winrt::Windows::Networking::Proximity::DeviceDepartedEventHandler get(PyObject* callable)
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
            };
        };
    };

    struct MessageReceivedHandler
    {
        static winrt::Windows::Networking::Proximity::MessageReceivedHandler get(PyObject* callable)
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

    struct MessageTransmittedHandler
    {
        static winrt::Windows::Networking::Proximity::MessageTransmittedHandler get(PyObject* callable)
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

namespace py::wrapper::Windows::Networking::Proximity
{
    using ConnectionRequestedEventArgs = py::winrt_wrapper<winrt::Windows::Networking::Proximity::ConnectionRequestedEventArgs>;
    using PeerFinder = py::winrt_wrapper<winrt::Windows::Networking::Proximity::PeerFinder>;
    using PeerInformation = py::winrt_wrapper<winrt::Windows::Networking::Proximity::PeerInformation>;
    using PeerWatcher = py::winrt_wrapper<winrt::Windows::Networking::Proximity::PeerWatcher>;
    using ProximityDevice = py::winrt_wrapper<winrt::Windows::Networking::Proximity::ProximityDevice>;
    using ProximityMessage = py::winrt_wrapper<winrt::Windows::Networking::Proximity::ProximityMessage>;
    using TriggeredConnectionStateChangedEventArgs = py::winrt_wrapper<winrt::Windows::Networking::Proximity::TriggeredConnectionStateChangedEventArgs>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Networking::Proximity::ConnectionRequestedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Proximity::PeerFinder>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Proximity::PeerInformation>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Proximity::PeerWatcher>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Proximity::ProximityDevice>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Proximity::ProximityMessage>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Networking::Proximity::TriggeredConnectionStateChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template <>
    struct delegate_python_type<winrt::Windows::Networking::Proximity::DeviceArrivedEventHandler>
    {
        using type = py::impl::Windows::Networking::Proximity::DeviceArrivedEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::Networking::Proximity::DeviceDepartedEventHandler>
    {
        using type = py::impl::Windows::Networking::Proximity::DeviceDepartedEventHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::Networking::Proximity::MessageReceivedHandler>
    {
        using type = py::impl::Windows::Networking::Proximity::MessageReceivedHandler;
    };

    template <>
    struct delegate_python_type<winrt::Windows::Networking::Proximity::MessageTransmittedHandler>
    {
        using type = py::impl::Windows::Networking::Proximity::MessageTransmittedHandler;
    };

}
