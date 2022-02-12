// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#include "pybase.h"
#include "py.Windows.Devices.Sensors.Custom.h"

PyTypeObject* py::winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensor>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensorReading>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs>::python_type;

namespace py::cpp::Windows::Devices::Sensors::Custom
{
    // ----- CustomSensor class --------------------
    constexpr const char* const _type_name_CustomSensor = "CustomSensor";

    static PyObject* _new_CustomSensor(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_CustomSensor);
        return nullptr;
    }

    static void _dealloc_CustomSensor(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* CustomSensor_FromIdAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Windows::Devices::Sensors::Custom::CustomSensor::FromIdAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* CustomSensor_GetCurrentReading(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetCurrentReading());
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* CustomSensor_GetDeviceSelector(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::guid>(args, 0);

                return py::convert(winrt::Windows::Devices::Sensors::Custom::CustomSensor::GetDeviceSelector(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* CustomSensor_get_ReportInterval(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ReportInterval());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int CustomSensor_put_ReportInterval(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<uint32_t>(arg);

            self->obj.ReportInterval(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* CustomSensor_get_DeviceId(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.DeviceId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* CustomSensor_get_MinimumReportInterval(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MinimumReportInterval());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* CustomSensor_get_ReportLatency(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ReportLatency());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int CustomSensor_put_ReportLatency(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<uint32_t>(arg);

            self->obj.ReportLatency(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* CustomSensor_get_MaxBatchSize(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MaxBatchSize());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* CustomSensor_add_ReadingChanged(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::Devices::Sensors::Custom::CustomSensor, winrt::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs>>(arg);

            return py::convert(self->obj.ReadingChanged(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* CustomSensor_remove_ReadingChanged(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.ReadingChanged(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_CustomSensor(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Devices::Sensors::Custom::CustomSensor>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_CustomSensor[] = {
        { "from_id_async", reinterpret_cast<PyCFunction>(CustomSensor_FromIdAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "get_current_reading", reinterpret_cast<PyCFunction>(CustomSensor_GetCurrentReading), METH_VARARGS, nullptr },
        { "get_device_selector", reinterpret_cast<PyCFunction>(CustomSensor_GetDeviceSelector), METH_VARARGS | METH_STATIC, nullptr },
        { "add_reading_changed", reinterpret_cast<PyCFunction>(CustomSensor_add_ReadingChanged), METH_O, nullptr },
        { "remove_reading_changed", reinterpret_cast<PyCFunction>(CustomSensor_remove_ReadingChanged), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_CustomSensor), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_CustomSensor[] = {
        { "report_interval", reinterpret_cast<getter>(CustomSensor_get_ReportInterval), reinterpret_cast<setter>(CustomSensor_put_ReportInterval), nullptr, nullptr },
        { "device_id", reinterpret_cast<getter>(CustomSensor_get_DeviceId), nullptr, nullptr, nullptr },
        { "minimum_report_interval", reinterpret_cast<getter>(CustomSensor_get_MinimumReportInterval), nullptr, nullptr, nullptr },
        { "report_latency", reinterpret_cast<getter>(CustomSensor_get_ReportLatency), reinterpret_cast<setter>(CustomSensor_put_ReportLatency), nullptr, nullptr },
        { "max_batch_size", reinterpret_cast<getter>(CustomSensor_get_MaxBatchSize), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_CustomSensor[] = 
    {
        { Py_tp_new, _new_CustomSensor },
        { Py_tp_dealloc, _dealloc_CustomSensor },
        { Py_tp_methods, _methods_CustomSensor },
        { Py_tp_getset, _getset_CustomSensor },
        { },
    };

    static PyType_Spec _type_spec_CustomSensor =
    {
        "_winsdk_Windows_Devices_Sensors_Custom.CustomSensor",
        sizeof(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensor),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_CustomSensor
    };

    // ----- CustomSensorReading class --------------------
    constexpr const char* const _type_name_CustomSensorReading = "CustomSensorReading";

    static PyObject* _new_CustomSensorReading(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_CustomSensorReading);
        return nullptr;
    }

    static void _dealloc_CustomSensorReading(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReading* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* CustomSensorReading_get_Properties(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Properties());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* CustomSensorReading_get_Timestamp(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Timestamp());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* CustomSensorReading_get_PerformanceCount(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReading* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.PerformanceCount());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_CustomSensorReading(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Devices::Sensors::Custom::CustomSensorReading>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_CustomSensorReading[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_CustomSensorReading), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_CustomSensorReading[] = {
        { "properties", reinterpret_cast<getter>(CustomSensorReading_get_Properties), nullptr, nullptr, nullptr },
        { "timestamp", reinterpret_cast<getter>(CustomSensorReading_get_Timestamp), nullptr, nullptr, nullptr },
        { "performance_count", reinterpret_cast<getter>(CustomSensorReading_get_PerformanceCount), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_CustomSensorReading[] = 
    {
        { Py_tp_new, _new_CustomSensorReading },
        { Py_tp_dealloc, _dealloc_CustomSensorReading },
        { Py_tp_methods, _methods_CustomSensorReading },
        { Py_tp_getset, _getset_CustomSensorReading },
        { },
    };

    static PyType_Spec _type_spec_CustomSensorReading =
    {
        "_winsdk_Windows_Devices_Sensors_Custom.CustomSensorReading",
        sizeof(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReading),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_CustomSensorReading
    };

    // ----- CustomSensorReadingChangedEventArgs class --------------------
    constexpr const char* const _type_name_CustomSensorReadingChangedEventArgs = "CustomSensorReadingChangedEventArgs";

    static PyObject* _new_CustomSensorReadingChangedEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_CustomSensorReadingChangedEventArgs);
        return nullptr;
    }

    static void _dealloc_CustomSensorReadingChangedEventArgs(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* CustomSensorReadingChangedEventArgs_get_Reading(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Reading());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_CustomSensorReadingChangedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_CustomSensorReadingChangedEventArgs[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_CustomSensorReadingChangedEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_CustomSensorReadingChangedEventArgs[] = {
        { "reading", reinterpret_cast<getter>(CustomSensorReadingChangedEventArgs_get_Reading), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_CustomSensorReadingChangedEventArgs[] = 
    {
        { Py_tp_new, _new_CustomSensorReadingChangedEventArgs },
        { Py_tp_dealloc, _dealloc_CustomSensorReadingChangedEventArgs },
        { Py_tp_methods, _methods_CustomSensorReadingChangedEventArgs },
        { Py_tp_getset, _getset_CustomSensorReadingChangedEventArgs },
        { },
    };

    static PyType_Spec _type_spec_CustomSensorReadingChangedEventArgs =
    {
        "_winsdk_Windows_Devices_Sensors_Custom.CustomSensorReadingChangedEventArgs",
        sizeof(py::wrapper::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_CustomSensorReadingChangedEventArgs
    };

    // ----- Windows.Devices.Sensors.Custom Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensor>::python_type = py::register_python_type(module, _type_name_CustomSensor, &_type_spec_CustomSensor, bases.get());
            py::winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensorReading>::python_type = py::register_python_type(module, _type_name_CustomSensorReading, &_type_spec_CustomSensorReading, bases.get());
            py::winrt_type<winrt::Windows::Devices::Sensors::Custom::CustomSensorReadingChangedEventArgs>::python_type = py::register_python_type(module, _type_name_CustomSensorReadingChangedEventArgs, &_type_spec_CustomSensorReadingChangedEventArgs, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Devices.Sensors.Custom");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Devices_Sensors_Custom",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Devices::Sensors::Custom

PyMODINIT_FUNC
PyInit__winsdk_Windows_Devices_Sensors_Custom (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Devices::Sensors::Custom::module_def);
}
