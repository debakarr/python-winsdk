// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Devices.Adc.Provider.h"

PyTypeObject* py::winrt_type<winrt::Windows::Devices::Adc::Provider::IAdcControllerProvider>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Devices::Adc::Provider::IAdcProvider>::python_type;

namespace py::cpp::Windows::Devices::Adc::Provider
{
    // ----- IAdcControllerProvider interface --------------------
    constexpr const char* const _type_name_IAdcControllerProvider = "IAdcControllerProvider";

    static PyObject* _new_IAdcControllerProvider(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IAdcControllerProvider);
        return nullptr;
    }

    static void _dealloc_IAdcControllerProvider(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IAdcControllerProvider_AcquireChannel(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<int32_t>(args, 0);

                self->obj.AcquireChannel(param0);
                Py_RETURN_NONE;
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

    static PyObject* IAdcControllerProvider_IsChannelModeSupported(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Devices::Adc::Provider::ProviderAdcChannelMode>(args, 0);

                return py::convert(self->obj.IsChannelModeSupported(param0));
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

    static PyObject* IAdcControllerProvider_ReadValue(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<int32_t>(args, 0);

                return py::convert(self->obj.ReadValue(param0));
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

    static PyObject* IAdcControllerProvider_ReleaseChannel(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<int32_t>(args, 0);

                self->obj.ReleaseChannel(param0);
                Py_RETURN_NONE;
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

    static PyObject* IAdcControllerProvider_get_ChannelCount(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ChannelCount());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* IAdcControllerProvider_get_ChannelMode(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ChannelMode());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int IAdcControllerProvider_put_ChannelMode(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Devices::Adc::Provider::ProviderAdcChannelMode>(arg);

            self->obj.ChannelMode(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* IAdcControllerProvider_get_MaxValue(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MaxValue());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* IAdcControllerProvider_get_MinValue(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MinValue());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* IAdcControllerProvider_get_ResolutionInBits(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ResolutionInBits());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_IAdcControllerProvider(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Devices::Adc::Provider::IAdcControllerProvider>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IAdcControllerProvider[] = {
        { "acquire_channel", reinterpret_cast<PyCFunction>(IAdcControllerProvider_AcquireChannel), METH_VARARGS, nullptr },
        { "is_channel_mode_supported", reinterpret_cast<PyCFunction>(IAdcControllerProvider_IsChannelModeSupported), METH_VARARGS, nullptr },
        { "read_value", reinterpret_cast<PyCFunction>(IAdcControllerProvider_ReadValue), METH_VARARGS, nullptr },
        { "release_channel", reinterpret_cast<PyCFunction>(IAdcControllerProvider_ReleaseChannel), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IAdcControllerProvider), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IAdcControllerProvider[] = {
        { "channel_count", reinterpret_cast<getter>(IAdcControllerProvider_get_ChannelCount), nullptr, nullptr, nullptr },
        { "channel_mode", reinterpret_cast<getter>(IAdcControllerProvider_get_ChannelMode), reinterpret_cast<setter>(IAdcControllerProvider_put_ChannelMode), nullptr, nullptr },
        { "max_value", reinterpret_cast<getter>(IAdcControllerProvider_get_MaxValue), nullptr, nullptr, nullptr },
        { "min_value", reinterpret_cast<getter>(IAdcControllerProvider_get_MinValue), nullptr, nullptr, nullptr },
        { "resolution_in_bits", reinterpret_cast<getter>(IAdcControllerProvider_get_ResolutionInBits), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_IAdcControllerProvider[] = 
    {
        { Py_tp_new, _new_IAdcControllerProvider },
        { Py_tp_dealloc, _dealloc_IAdcControllerProvider },
        { Py_tp_methods, _methods_IAdcControllerProvider },
        { Py_tp_getset, _getset_IAdcControllerProvider },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_IAdcControllerProvider =
    {
        "_winsdk_Windows_Devices_Adc_Provider.IAdcControllerProvider",
        sizeof(py::wrapper::Windows::Devices::Adc::Provider::IAdcControllerProvider),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IAdcControllerProvider
    };

    // ----- IAdcProvider interface --------------------
    constexpr const char* const _type_name_IAdcProvider = "IAdcProvider";

    static PyObject* _new_IAdcProvider(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IAdcProvider);
        return nullptr;
    }

    static void _dealloc_IAdcProvider(py::wrapper::Windows::Devices::Adc::Provider::IAdcProvider* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IAdcProvider_GetControllers(py::wrapper::Windows::Devices::Adc::Provider::IAdcProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetControllers());
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

    static PyObject* _from_IAdcProvider(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Devices::Adc::Provider::IAdcProvider>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IAdcProvider[] = {
        { "get_controllers", reinterpret_cast<PyCFunction>(IAdcProvider_GetControllers), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IAdcProvider), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IAdcProvider[] = {
        { }
    };

    static PyType_Slot _type_slots_IAdcProvider[] = 
    {
        { Py_tp_new, _new_IAdcProvider },
        { Py_tp_dealloc, _dealloc_IAdcProvider },
        { Py_tp_methods, _methods_IAdcProvider },
        { Py_tp_getset, _getset_IAdcProvider },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_IAdcProvider =
    {
        "_winsdk_Windows_Devices_Adc_Provider.IAdcProvider",
        sizeof(py::wrapper::Windows::Devices::Adc::Provider::IAdcProvider),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IAdcProvider
    };

    // ----- Windows.Devices.Adc.Provider Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Devices::Adc::Provider::IAdcControllerProvider>::python_type = py::register_python_type(module, _type_name_IAdcControllerProvider, &_type_spec_IAdcControllerProvider, bases.get());
            py::winrt_type<winrt::Windows::Devices::Adc::Provider::IAdcProvider>::python_type = py::register_python_type(module, _type_name_IAdcProvider, &_type_spec_IAdcProvider, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Devices.Adc.Provider");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Devices_Adc_Provider",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Devices::Adc::Provider

PyMODINIT_FUNC
PyInit__winsdk_Windows_Devices_Adc_Provider (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Devices::Adc::Provider::module_def);
}
