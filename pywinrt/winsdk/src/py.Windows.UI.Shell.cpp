// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#include "pybase.h"
#include "py.Windows.UI.Shell.h"

PyTypeObject* py::winrt_type<winrt::Windows::UI::Shell::AdaptiveCardBuilder>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::UI::Shell::ShareWindowCommandEventArgs>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::UI::Shell::ShareWindowCommandSource>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::UI::Shell::TaskbarManager>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::UI::Shell::IAdaptiveCard>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::UI::Shell::IAdaptiveCardBuilderStatics>::python_type;

namespace py::cpp::Windows::UI::Shell
{
    // ----- AdaptiveCardBuilder class --------------------
    constexpr const char* const _type_name_AdaptiveCardBuilder = "AdaptiveCardBuilder";

    static PyObject* _new_AdaptiveCardBuilder(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_AdaptiveCardBuilder);
        return nullptr;
    }

    static PyObject* AdaptiveCardBuilder_CreateAdaptiveCardFromJson(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Windows::UI::Shell::AdaptiveCardBuilder::CreateAdaptiveCardFromJson(param0));
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

    static PyMethodDef _methods_AdaptiveCardBuilder[] = {
        { "create_adaptive_card_from_json", reinterpret_cast<PyCFunction>(AdaptiveCardBuilder_CreateAdaptiveCardFromJson), METH_VARARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_AdaptiveCardBuilder[] = {
        { }
    };

    static PyType_Slot _type_slots_AdaptiveCardBuilder[] = 
    {
        { Py_tp_new, _new_AdaptiveCardBuilder },
        { Py_tp_methods, _methods_AdaptiveCardBuilder },
        { Py_tp_getset, _getset_AdaptiveCardBuilder },
        { },
    };

    static PyType_Spec _type_spec_AdaptiveCardBuilder =
    {
        "_winsdk_Windows_UI_Shell.AdaptiveCardBuilder",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_AdaptiveCardBuilder
    };

    // ----- ShareWindowCommandEventArgs class --------------------
    constexpr const char* const _type_name_ShareWindowCommandEventArgs = "ShareWindowCommandEventArgs";

    static PyObject* _new_ShareWindowCommandEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_ShareWindowCommandEventArgs);
        return nullptr;
    }

    static void _dealloc_ShareWindowCommandEventArgs(py::wrapper::Windows::UI::Shell::ShareWindowCommandEventArgs* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* ShareWindowCommandEventArgs_get_Command(py::wrapper::Windows::UI::Shell::ShareWindowCommandEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Command());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int ShareWindowCommandEventArgs_put_Command(py::wrapper::Windows::UI::Shell::ShareWindowCommandEventArgs* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::UI::Shell::ShareWindowCommand>(arg);

            self->obj.Command(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* ShareWindowCommandEventArgs_get_WindowId(py::wrapper::Windows::UI::Shell::ShareWindowCommandEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.WindowId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_ShareWindowCommandEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::UI::Shell::ShareWindowCommandEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ShareWindowCommandEventArgs[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_ShareWindowCommandEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ShareWindowCommandEventArgs[] = {
        { "command", reinterpret_cast<getter>(ShareWindowCommandEventArgs_get_Command), reinterpret_cast<setter>(ShareWindowCommandEventArgs_put_Command), nullptr, nullptr },
        { "window_id", reinterpret_cast<getter>(ShareWindowCommandEventArgs_get_WindowId), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_ShareWindowCommandEventArgs[] = 
    {
        { Py_tp_new, _new_ShareWindowCommandEventArgs },
        { Py_tp_dealloc, _dealloc_ShareWindowCommandEventArgs },
        { Py_tp_methods, _methods_ShareWindowCommandEventArgs },
        { Py_tp_getset, _getset_ShareWindowCommandEventArgs },
        { },
    };

    static PyType_Spec _type_spec_ShareWindowCommandEventArgs =
    {
        "_winsdk_Windows_UI_Shell.ShareWindowCommandEventArgs",
        sizeof(py::wrapper::Windows::UI::Shell::ShareWindowCommandEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ShareWindowCommandEventArgs
    };

    // ----- ShareWindowCommandSource class --------------------
    constexpr const char* const _type_name_ShareWindowCommandSource = "ShareWindowCommandSource";

    static PyObject* _new_ShareWindowCommandSource(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_ShareWindowCommandSource);
        return nullptr;
    }

    static void _dealloc_ShareWindowCommandSource(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* ShareWindowCommandSource_GetForCurrentView(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::UI::Shell::ShareWindowCommandSource::GetForCurrentView());
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

    static PyObject* ShareWindowCommandSource_ReportCommandChanged(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.ReportCommandChanged();
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

    static PyObject* ShareWindowCommandSource_Start(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.Start();
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

    static PyObject* ShareWindowCommandSource_Stop(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.Stop();
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

    static PyObject* ShareWindowCommandSource_add_CommandInvoked(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::UI::Shell::ShareWindowCommandSource, winrt::Windows::UI::Shell::ShareWindowCommandEventArgs>>(arg);

            return py::convert(self->obj.CommandInvoked(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ShareWindowCommandSource_remove_CommandInvoked(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.CommandInvoked(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ShareWindowCommandSource_add_CommandRequested(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::UI::Shell::ShareWindowCommandSource, winrt::Windows::UI::Shell::ShareWindowCommandEventArgs>>(arg);

            return py::convert(self->obj.CommandRequested(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ShareWindowCommandSource_remove_CommandRequested(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.CommandRequested(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_ShareWindowCommandSource(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::UI::Shell::ShareWindowCommandSource>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ShareWindowCommandSource[] = {
        { "get_for_current_view", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_GetForCurrentView), METH_VARARGS | METH_STATIC, nullptr },
        { "report_command_changed", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_ReportCommandChanged), METH_VARARGS, nullptr },
        { "start", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_Start), METH_VARARGS, nullptr },
        { "stop", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_Stop), METH_VARARGS, nullptr },
        { "add_command_invoked", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_add_CommandInvoked), METH_O, nullptr },
        { "remove_command_invoked", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_remove_CommandInvoked), METH_O, nullptr },
        { "add_command_requested", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_add_CommandRequested), METH_O, nullptr },
        { "remove_command_requested", reinterpret_cast<PyCFunction>(ShareWindowCommandSource_remove_CommandRequested), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ShareWindowCommandSource), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ShareWindowCommandSource[] = {
        { }
    };

    static PyType_Slot _type_slots_ShareWindowCommandSource[] = 
    {
        { Py_tp_new, _new_ShareWindowCommandSource },
        { Py_tp_dealloc, _dealloc_ShareWindowCommandSource },
        { Py_tp_methods, _methods_ShareWindowCommandSource },
        { Py_tp_getset, _getset_ShareWindowCommandSource },
        { },
    };

    static PyType_Spec _type_spec_ShareWindowCommandSource =
    {
        "_winsdk_Windows_UI_Shell.ShareWindowCommandSource",
        sizeof(py::wrapper::Windows::UI::Shell::ShareWindowCommandSource),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ShareWindowCommandSource
    };

    // ----- TaskbarManager class --------------------
    constexpr const char* const _type_name_TaskbarManager = "TaskbarManager";

    static PyObject* _new_TaskbarManager(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_TaskbarManager);
        return nullptr;
    }

    static void _dealloc_TaskbarManager(py::wrapper::Windows::UI::Shell::TaskbarManager* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* TaskbarManager_GetDefault(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::UI::Shell::TaskbarManager::GetDefault());
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

    static PyObject* TaskbarManager_IsAppListEntryPinnedAsync(py::wrapper::Windows::UI::Shell::TaskbarManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::ApplicationModel::Core::AppListEntry>(args, 0);

                return py::convert(self->obj.IsAppListEntryPinnedAsync(param0));
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

    static PyObject* TaskbarManager_IsCurrentAppPinnedAsync(py::wrapper::Windows::UI::Shell::TaskbarManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.IsCurrentAppPinnedAsync());
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

    static PyObject* TaskbarManager_IsSecondaryTilePinnedAsync(py::wrapper::Windows::UI::Shell::TaskbarManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.IsSecondaryTilePinnedAsync(param0));
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

    static PyObject* TaskbarManager_RequestPinAppListEntryAsync(py::wrapper::Windows::UI::Shell::TaskbarManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::ApplicationModel::Core::AppListEntry>(args, 0);

                return py::convert(self->obj.RequestPinAppListEntryAsync(param0));
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

    static PyObject* TaskbarManager_RequestPinCurrentAppAsync(py::wrapper::Windows::UI::Shell::TaskbarManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.RequestPinCurrentAppAsync());
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

    static PyObject* TaskbarManager_RequestPinSecondaryTileAsync(py::wrapper::Windows::UI::Shell::TaskbarManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::UI::StartScreen::SecondaryTile>(args, 0);

                return py::convert(self->obj.RequestPinSecondaryTileAsync(param0));
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

    static PyObject* TaskbarManager_TryUnpinSecondaryTileAsync(py::wrapper::Windows::UI::Shell::TaskbarManager* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.TryUnpinSecondaryTileAsync(param0));
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

    static PyObject* TaskbarManager_get_IsPinningAllowed(py::wrapper::Windows::UI::Shell::TaskbarManager* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IsPinningAllowed());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* TaskbarManager_get_IsSupported(py::wrapper::Windows::UI::Shell::TaskbarManager* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IsSupported());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_TaskbarManager(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::UI::Shell::TaskbarManager>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_TaskbarManager[] = {
        { "get_default", reinterpret_cast<PyCFunction>(TaskbarManager_GetDefault), METH_VARARGS | METH_STATIC, nullptr },
        { "is_app_list_entry_pinned_async", reinterpret_cast<PyCFunction>(TaskbarManager_IsAppListEntryPinnedAsync), METH_VARARGS, nullptr },
        { "is_current_app_pinned_async", reinterpret_cast<PyCFunction>(TaskbarManager_IsCurrentAppPinnedAsync), METH_VARARGS, nullptr },
        { "is_secondary_tile_pinned_async", reinterpret_cast<PyCFunction>(TaskbarManager_IsSecondaryTilePinnedAsync), METH_VARARGS, nullptr },
        { "request_pin_app_list_entry_async", reinterpret_cast<PyCFunction>(TaskbarManager_RequestPinAppListEntryAsync), METH_VARARGS, nullptr },
        { "request_pin_current_app_async", reinterpret_cast<PyCFunction>(TaskbarManager_RequestPinCurrentAppAsync), METH_VARARGS, nullptr },
        { "request_pin_secondary_tile_async", reinterpret_cast<PyCFunction>(TaskbarManager_RequestPinSecondaryTileAsync), METH_VARARGS, nullptr },
        { "try_unpin_secondary_tile_async", reinterpret_cast<PyCFunction>(TaskbarManager_TryUnpinSecondaryTileAsync), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_TaskbarManager), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_TaskbarManager[] = {
        { "is_pinning_allowed", reinterpret_cast<getter>(TaskbarManager_get_IsPinningAllowed), nullptr, nullptr, nullptr },
        { "is_supported", reinterpret_cast<getter>(TaskbarManager_get_IsSupported), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_TaskbarManager[] = 
    {
        { Py_tp_new, _new_TaskbarManager },
        { Py_tp_dealloc, _dealloc_TaskbarManager },
        { Py_tp_methods, _methods_TaskbarManager },
        { Py_tp_getset, _getset_TaskbarManager },
        { },
    };

    static PyType_Spec _type_spec_TaskbarManager =
    {
        "_winsdk_Windows_UI_Shell.TaskbarManager",
        sizeof(py::wrapper::Windows::UI::Shell::TaskbarManager),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_TaskbarManager
    };

    // ----- IAdaptiveCard interface --------------------
    constexpr const char* const _type_name_IAdaptiveCard = "IAdaptiveCard";

    static PyObject* _new_IAdaptiveCard(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IAdaptiveCard);
        return nullptr;
    }

    static void _dealloc_IAdaptiveCard(py::wrapper::Windows::UI::Shell::IAdaptiveCard* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IAdaptiveCard_ToJson(py::wrapper::Windows::UI::Shell::IAdaptiveCard* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.ToJson());
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

    static PyObject* _from_IAdaptiveCard(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::UI::Shell::IAdaptiveCard>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IAdaptiveCard[] = {
        { "to_json", reinterpret_cast<PyCFunction>(IAdaptiveCard_ToJson), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IAdaptiveCard), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IAdaptiveCard[] = {
        { }
    };

    static PyType_Slot _type_slots_IAdaptiveCard[] = 
    {
        { Py_tp_new, _new_IAdaptiveCard },
        { Py_tp_dealloc, _dealloc_IAdaptiveCard },
        { Py_tp_methods, _methods_IAdaptiveCard },
        { Py_tp_getset, _getset_IAdaptiveCard },
        { },
    };

    static PyType_Spec _type_spec_IAdaptiveCard =
    {
        "_winsdk_Windows_UI_Shell.IAdaptiveCard",
        sizeof(py::wrapper::Windows::UI::Shell::IAdaptiveCard),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IAdaptiveCard
    };

    // ----- IAdaptiveCardBuilderStatics interface --------------------
    constexpr const char* const _type_name_IAdaptiveCardBuilderStatics = "IAdaptiveCardBuilderStatics";

    static PyObject* _new_IAdaptiveCardBuilderStatics(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IAdaptiveCardBuilderStatics);
        return nullptr;
    }

    static void _dealloc_IAdaptiveCardBuilderStatics(py::wrapper::Windows::UI::Shell::IAdaptiveCardBuilderStatics* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IAdaptiveCardBuilderStatics_CreateAdaptiveCardFromJson(py::wrapper::Windows::UI::Shell::IAdaptiveCardBuilderStatics* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.CreateAdaptiveCardFromJson(param0));
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

    static PyObject* _from_IAdaptiveCardBuilderStatics(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::UI::Shell::IAdaptiveCardBuilderStatics>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IAdaptiveCardBuilderStatics[] = {
        { "create_adaptive_card_from_json", reinterpret_cast<PyCFunction>(IAdaptiveCardBuilderStatics_CreateAdaptiveCardFromJson), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IAdaptiveCardBuilderStatics), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IAdaptiveCardBuilderStatics[] = {
        { }
    };

    static PyType_Slot _type_slots_IAdaptiveCardBuilderStatics[] = 
    {
        { Py_tp_new, _new_IAdaptiveCardBuilderStatics },
        { Py_tp_dealloc, _dealloc_IAdaptiveCardBuilderStatics },
        { Py_tp_methods, _methods_IAdaptiveCardBuilderStatics },
        { Py_tp_getset, _getset_IAdaptiveCardBuilderStatics },
        { },
    };

    static PyType_Spec _type_spec_IAdaptiveCardBuilderStatics =
    {
        "_winsdk_Windows_UI_Shell.IAdaptiveCardBuilderStatics",
        sizeof(py::wrapper::Windows::UI::Shell::IAdaptiveCardBuilderStatics),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IAdaptiveCardBuilderStatics
    };

    // ----- Windows.UI.Shell Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::UI::Shell::AdaptiveCardBuilder>::python_type = py::register_python_type(module, _type_name_AdaptiveCardBuilder, &_type_spec_AdaptiveCardBuilder, nullptr);
            py::winrt_type<winrt::Windows::UI::Shell::ShareWindowCommandEventArgs>::python_type = py::register_python_type(module, _type_name_ShareWindowCommandEventArgs, &_type_spec_ShareWindowCommandEventArgs, bases.get());
            py::winrt_type<winrt::Windows::UI::Shell::ShareWindowCommandSource>::python_type = py::register_python_type(module, _type_name_ShareWindowCommandSource, &_type_spec_ShareWindowCommandSource, bases.get());
            py::winrt_type<winrt::Windows::UI::Shell::TaskbarManager>::python_type = py::register_python_type(module, _type_name_TaskbarManager, &_type_spec_TaskbarManager, bases.get());
            py::winrt_type<winrt::Windows::UI::Shell::IAdaptiveCard>::python_type = py::register_python_type(module, _type_name_IAdaptiveCard, &_type_spec_IAdaptiveCard, bases.get());
            py::winrt_type<winrt::Windows::UI::Shell::IAdaptiveCardBuilderStatics>::python_type = py::register_python_type(module, _type_name_IAdaptiveCardBuilderStatics, &_type_spec_IAdaptiveCardBuilderStatics, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.UI.Shell");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_UI_Shell",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::UI::Shell

PyMODINIT_FUNC
PyInit__winsdk_Windows_UI_Shell (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::UI::Shell::module_def);
}
