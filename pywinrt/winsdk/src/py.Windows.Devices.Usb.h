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

#include <winrt/Windows.Devices.Usb.h>

namespace py::proj::Windows::Devices::Usb
{}

namespace py::impl::Windows::Devices::Usb
{}

namespace py::wrapper::Windows::Devices::Usb
{
    using UsbBulkInEndpointDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbBulkInEndpointDescriptor>;
    using UsbBulkInPipe = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbBulkInPipe>;
    using UsbBulkOutEndpointDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbBulkOutEndpointDescriptor>;
    using UsbBulkOutPipe = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbBulkOutPipe>;
    using UsbConfiguration = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbConfiguration>;
    using UsbConfigurationDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbConfigurationDescriptor>;
    using UsbControlRequestType = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbControlRequestType>;
    using UsbDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbDescriptor>;
    using UsbDevice = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbDevice>;
    using UsbDeviceClass = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbDeviceClass>;
    using UsbDeviceClasses = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbDeviceClasses>;
    using UsbDeviceDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbDeviceDescriptor>;
    using UsbEndpointDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbEndpointDescriptor>;
    using UsbInterface = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterface>;
    using UsbInterfaceDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterfaceDescriptor>;
    using UsbInterfaceSetting = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterfaceSetting>;
    using UsbInterruptInEndpointDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterruptInEndpointDescriptor>;
    using UsbInterruptInEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterruptInEventArgs>;
    using UsbInterruptInPipe = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterruptInPipe>;
    using UsbInterruptOutEndpointDescriptor = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterruptOutEndpointDescriptor>;
    using UsbInterruptOutPipe = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbInterruptOutPipe>;
    using UsbSetupPacket = py::winrt_wrapper<winrt::Windows::Devices::Usb::UsbSetupPacket>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbBulkInEndpointDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbBulkInPipe>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbBulkOutEndpointDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbBulkOutPipe>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbConfiguration>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbConfigurationDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbControlRequestType>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbDevice>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbDeviceClass>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbDeviceClasses>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbDeviceDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbEndpointDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterface>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterfaceDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterfaceSetting>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterruptInEndpointDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterruptInEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterruptInPipe>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterruptOutEndpointDescriptor>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbInterruptOutPipe>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Usb::UsbSetupPacket>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
