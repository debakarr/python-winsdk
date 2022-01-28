// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Security.Cryptography.DataProtection.h"

PyTypeObject* py::winrt_type<winrt::Windows::Security::Cryptography::DataProtection::DataProtectionProvider>::python_type;

namespace py::cpp::Windows::Security::Cryptography::DataProtection
{
    // ----- DataProtectionProvider class --------------------
    constexpr const char* const _type_name_DataProtectionProvider = "DataProtectionProvider";

    static PyObject* _new_DataProtectionProvider(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        Py_ssize_t arg_count = PyTuple_Size(args);
        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                winrt::Windows::Security::Cryptography::DataProtection::DataProtectionProvider instance{ param0 };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 0)
        {
            try
            {
                winrt::Windows::Security::Cryptography::DataProtection::DataProtectionProvider instance{  };
                return py::wrap(instance, type);
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

    static void _dealloc_DataProtectionProvider(py::wrapper::Windows::Security::Cryptography::DataProtection::DataProtectionProvider* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* DataProtectionProvider_ProtectAsync(py::wrapper::Windows::Security::Cryptography::DataProtection::DataProtectionProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);

                return py::convert(self->obj.ProtectAsync(param0));
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

    static PyObject* DataProtectionProvider_ProtectStreamAsync(py::wrapper::Windows::Security::Cryptography::DataProtection::DataProtectionProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IInputStream>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Storage::Streams::IOutputStream>(args, 1);

                return py::convert(self->obj.ProtectStreamAsync(param0, param1));
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

    static PyObject* DataProtectionProvider_UnprotectAsync(py::wrapper::Windows::Security::Cryptography::DataProtection::DataProtectionProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);

                return py::convert(self->obj.UnprotectAsync(param0));
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

    static PyObject* DataProtectionProvider_UnprotectStreamAsync(py::wrapper::Windows::Security::Cryptography::DataProtection::DataProtectionProvider* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IInputStream>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Storage::Streams::IOutputStream>(args, 1);

                return py::convert(self->obj.UnprotectStreamAsync(param0, param1));
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

    static PyObject* _from_DataProtectionProvider(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Security::Cryptography::DataProtection::DataProtectionProvider>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_DataProtectionProvider[] = {
        { "protect_async", reinterpret_cast<PyCFunction>(DataProtectionProvider_ProtectAsync), METH_VARARGS, nullptr },
        { "protect_stream_async", reinterpret_cast<PyCFunction>(DataProtectionProvider_ProtectStreamAsync), METH_VARARGS, nullptr },
        { "unprotect_async", reinterpret_cast<PyCFunction>(DataProtectionProvider_UnprotectAsync), METH_VARARGS, nullptr },
        { "unprotect_stream_async", reinterpret_cast<PyCFunction>(DataProtectionProvider_UnprotectStreamAsync), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_DataProtectionProvider), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_DataProtectionProvider[] = {
        { }
    };

    static PyType_Slot _type_slots_DataProtectionProvider[] = 
    {
        { Py_tp_new, _new_DataProtectionProvider },
        { Py_tp_dealloc, _dealloc_DataProtectionProvider },
        { Py_tp_methods, _methods_DataProtectionProvider },
        { Py_tp_getset, _getset_DataProtectionProvider },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_DataProtectionProvider =
    {
        "_winsdk_Windows_Security_Cryptography_DataProtection.DataProtectionProvider",
        sizeof(py::wrapper::Windows::Security::Cryptography::DataProtection::DataProtectionProvider),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_DataProtectionProvider
    };

    // ----- Windows.Security.Cryptography.DataProtection Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Security::Cryptography::DataProtection::DataProtectionProvider>::python_type = py::register_python_type(module, _type_name_DataProtectionProvider, &_type_spec_DataProtectionProvider, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Security.Cryptography.DataProtection");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Security_Cryptography_DataProtection",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Security::Cryptography::DataProtection

PyMODINIT_FUNC
PyInit__winsdk_Windows_Security_Cryptography_DataProtection (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Security::Cryptography::DataProtection::module_def);
}
