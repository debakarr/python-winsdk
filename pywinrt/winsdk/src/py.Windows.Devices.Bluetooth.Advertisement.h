// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Devices.Bluetooth.h")
#include "py.Windows.Devices.Bluetooth.h"
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

#include <winrt/Windows.Devices.Bluetooth.Advertisement.h>

namespace py::proj::Windows::Devices::Bluetooth::Advertisement
{}

namespace py::impl::Windows::Devices::Bluetooth::Advertisement
{}

namespace py::wrapper::Windows::Devices::Bluetooth::Advertisement
{
    using BluetoothLEAdvertisement = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisement>;
    using BluetoothLEAdvertisementBytePattern = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementBytePattern>;
    using BluetoothLEAdvertisementDataSection = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataSection>;
    using BluetoothLEAdvertisementDataTypes = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataTypes>;
    using BluetoothLEAdvertisementFilter = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementFilter>;
    using BluetoothLEAdvertisementPublisher = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisher>;
    using BluetoothLEAdvertisementPublisherStatusChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisherStatusChangedEventArgs>;
    using BluetoothLEAdvertisementReceivedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementReceivedEventArgs>;
    using BluetoothLEAdvertisementWatcher = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcher>;
    using BluetoothLEAdvertisementWatcherStoppedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcherStoppedEventArgs>;
    using BluetoothLEManufacturerData = py::winrt_wrapper<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEManufacturerData>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisement>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementBytePattern>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataSection>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementDataTypes>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementFilter>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisher>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementPublisherStatusChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementReceivedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcher>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEAdvertisementWatcherStoppedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::Devices::Bluetooth::Advertisement::BluetoothLEManufacturerData>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
