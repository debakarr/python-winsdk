// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#include "pybase.h"
#include "py.Windows.ApplicationModel.Wallet.System.h"

PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::ApplicationModel::Wallet::System::WalletManagerSystem>::python_type;

namespace py::cpp::Windows::ApplicationModel::Wallet::System
{
    // ----- WalletItemSystemStore class --------------------
    constexpr const char* const _type_name_WalletItemSystemStore = "WalletItemSystemStore";

    static PyObject* _new_WalletItemSystemStore(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_WalletItemSystemStore);
        return nullptr;
    }

    static void _dealloc_WalletItemSystemStore(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* WalletItemSystemStore_DeleteAsync(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::ApplicationModel::Wallet::WalletItem>(args, 0);

                return py::convert(self->obj.DeleteAsync(param0));
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

    static PyObject* WalletItemSystemStore_GetAppStatusForItem(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::ApplicationModel::Wallet::WalletItem>(args, 0);

                return py::convert(self->obj.GetAppStatusForItem(param0));
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

    static PyObject* WalletItemSystemStore_GetItemsAsync(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetItemsAsync());
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

    static PyObject* WalletItemSystemStore_ImportItemAsync(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IRandomAccessStreamReference>(args, 0);

                return py::convert(self->obj.ImportItemAsync(param0));
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

    static PyObject* WalletItemSystemStore_LaunchAppForItemAsync(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::ApplicationModel::Wallet::WalletItem>(args, 0);

                return py::convert(self->obj.LaunchAppForItemAsync(param0));
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

    static PyObject* WalletItemSystemStore_add_ItemsChanged(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore, winrt::Windows::Foundation::IInspectable>>(arg);

            return py::convert(self->obj.ItemsChanged(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* WalletItemSystemStore_remove_ItemsChanged(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.ItemsChanged(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_WalletItemSystemStore(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_WalletItemSystemStore[] = {
        { "delete_async", reinterpret_cast<PyCFunction>(WalletItemSystemStore_DeleteAsync), METH_VARARGS, nullptr },
        { "get_app_status_for_item", reinterpret_cast<PyCFunction>(WalletItemSystemStore_GetAppStatusForItem), METH_VARARGS, nullptr },
        { "get_items_async", reinterpret_cast<PyCFunction>(WalletItemSystemStore_GetItemsAsync), METH_VARARGS, nullptr },
        { "import_item_async", reinterpret_cast<PyCFunction>(WalletItemSystemStore_ImportItemAsync), METH_VARARGS, nullptr },
        { "launch_app_for_item_async", reinterpret_cast<PyCFunction>(WalletItemSystemStore_LaunchAppForItemAsync), METH_VARARGS, nullptr },
        { "add_items_changed", reinterpret_cast<PyCFunction>(WalletItemSystemStore_add_ItemsChanged), METH_O, nullptr },
        { "remove_items_changed", reinterpret_cast<PyCFunction>(WalletItemSystemStore_remove_ItemsChanged), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_WalletItemSystemStore), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_WalletItemSystemStore[] = {
        { }
    };

    static PyType_Slot _type_slots_WalletItemSystemStore[] = 
    {
        { Py_tp_new, _new_WalletItemSystemStore },
        { Py_tp_dealloc, _dealloc_WalletItemSystemStore },
        { Py_tp_methods, _methods_WalletItemSystemStore },
        { Py_tp_getset, _getset_WalletItemSystemStore },
        { },
    };

    static PyType_Spec _type_spec_WalletItemSystemStore =
    {
        "_winsdk_Windows_ApplicationModel_Wallet_System.WalletItemSystemStore",
        sizeof(py::wrapper::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_WalletItemSystemStore
    };

    // ----- WalletManagerSystem class --------------------
    constexpr const char* const _type_name_WalletManagerSystem = "WalletManagerSystem";

    static PyObject* _new_WalletManagerSystem(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_WalletManagerSystem);
        return nullptr;
    }

    static PyObject* WalletManagerSystem_RequestStoreAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::ApplicationModel::Wallet::System::WalletManagerSystem::RequestStoreAsync());
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

    static PyMethodDef _methods_WalletManagerSystem[] = {
        { "request_store_async", reinterpret_cast<PyCFunction>(WalletManagerSystem_RequestStoreAsync), METH_VARARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_WalletManagerSystem[] = {
        { }
    };

    static PyType_Slot _type_slots_WalletManagerSystem[] = 
    {
        { Py_tp_new, _new_WalletManagerSystem },
        { Py_tp_methods, _methods_WalletManagerSystem },
        { Py_tp_getset, _getset_WalletManagerSystem },
        { },
    };

    static PyType_Spec _type_spec_WalletManagerSystem =
    {
        "_winsdk_Windows_ApplicationModel_Wallet_System.WalletManagerSystem",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_WalletManagerSystem
    };

    // ----- Windows.ApplicationModel.Wallet.System Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::ApplicationModel::Wallet::System::WalletItemSystemStore>::python_type = py::register_python_type(module, _type_name_WalletItemSystemStore, &_type_spec_WalletItemSystemStore, bases.get());
            py::winrt_type<winrt::Windows::ApplicationModel::Wallet::System::WalletManagerSystem>::python_type = py::register_python_type(module, _type_name_WalletManagerSystem, &_type_spec_WalletManagerSystem, nullptr);

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.ApplicationModel.Wallet.System");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_ApplicationModel_Wallet_System",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::ApplicationModel::Wallet::System

PyMODINIT_FUNC
PyInit__winsdk_Windows_ApplicationModel_Wallet_System (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::ApplicationModel::Wallet::System::module_def);
}
