// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#include "pybase.h"
#include "py.Windows.Networking.PushNotifications.h"

PyTypeObject* py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannel>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannelsRevokedEventArgs>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Networking::PushNotifications::RawNotification>::python_type;

namespace py::cpp::Windows::Networking::PushNotifications
{
    // ----- PushNotificationChannel class --------------------
    constexpr const char* const _type_name_PushNotificationChannel = "PushNotificationChannel";

    static PyObject* _new_PushNotificationChannel(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PushNotificationChannel);
        return nullptr;
    }

    static void _dealloc_PushNotificationChannel(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannel* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PushNotificationChannel_Close(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannel* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.Close();
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

    static PyObject* PushNotificationChannel_get_ExpirationTime(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannel* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ExpirationTime());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationChannel_get_Uri(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannel* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Uri());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationChannel_add_PushNotificationReceived(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannel* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::Networking::PushNotifications::PushNotificationChannel, winrt::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs>>(arg);

            return py::convert(self->obj.PushNotificationReceived(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationChannel_remove_PushNotificationReceived(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannel* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.PushNotificationReceived(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_PushNotificationChannel(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Networking::PushNotifications::PushNotificationChannel>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PushNotificationChannel[] = {
        { "close", reinterpret_cast<PyCFunction>(PushNotificationChannel_Close), METH_VARARGS, nullptr },
        { "add_push_notification_received", reinterpret_cast<PyCFunction>(PushNotificationChannel_add_PushNotificationReceived), METH_O, nullptr },
        { "remove_push_notification_received", reinterpret_cast<PyCFunction>(PushNotificationChannel_remove_PushNotificationReceived), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_PushNotificationChannel), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PushNotificationChannel[] = {
        { "expiration_time", reinterpret_cast<getter>(PushNotificationChannel_get_ExpirationTime), nullptr, nullptr, nullptr },
        { "uri", reinterpret_cast<getter>(PushNotificationChannel_get_Uri), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PushNotificationChannel[] = 
    {
        { Py_tp_new, _new_PushNotificationChannel },
        { Py_tp_dealloc, _dealloc_PushNotificationChannel },
        { Py_tp_methods, _methods_PushNotificationChannel },
        { Py_tp_getset, _getset_PushNotificationChannel },
        { },
    };

    static PyType_Spec _type_spec_PushNotificationChannel =
    {
        "_winsdk_Windows_Networking_PushNotifications.PushNotificationChannel",
        sizeof(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannel),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PushNotificationChannel
    };

    // ----- PushNotificationChannelManager class --------------------
    constexpr const char* const _type_name_PushNotificationChannelManager = "PushNotificationChannelManager";

    static PyObject* _new_PushNotificationChannelManager(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PushNotificationChannelManager);
        return nullptr;
    }

    static PyObject* PushNotificationChannelManager_CreatePushNotificationChannelForApplicationAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager::CreatePushNotificationChannelForApplicationAsync());
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager::CreatePushNotificationChannelForApplicationAsync(param0));
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

    static PyObject* PushNotificationChannelManager_CreatePushNotificationChannelForSecondaryTileAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager::CreatePushNotificationChannelForSecondaryTileAsync(param0));
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

    static PyObject* PushNotificationChannelManager_GetDefault(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager::GetDefault());
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

    static PyObject* PushNotificationChannelManager_GetForUser(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::System::User>(args, 0);

                return py::convert(winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager::GetForUser(param0));
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

    static PyObject* PushNotificationChannelManager_add_ChannelsRevoked(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::EventHandler<winrt::Windows::Networking::PushNotifications::PushNotificationChannelsRevokedEventArgs>>(arg);

            return py::convert(winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager::ChannelsRevoked(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationChannelManager_remove_ChannelsRevoked(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager::ChannelsRevoked(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PushNotificationChannelManager[] = {
        { "create_push_notification_channel_for_application_async", reinterpret_cast<PyCFunction>(PushNotificationChannelManager_CreatePushNotificationChannelForApplicationAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "create_push_notification_channel_for_secondary_tile_async", reinterpret_cast<PyCFunction>(PushNotificationChannelManager_CreatePushNotificationChannelForSecondaryTileAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "get_default", reinterpret_cast<PyCFunction>(PushNotificationChannelManager_GetDefault), METH_VARARGS | METH_STATIC, nullptr },
        { "get_for_user", reinterpret_cast<PyCFunction>(PushNotificationChannelManager_GetForUser), METH_VARARGS | METH_STATIC, nullptr },
        { "add_channels_revoked", reinterpret_cast<PyCFunction>(PushNotificationChannelManager_add_ChannelsRevoked), METH_O | METH_STATIC, nullptr },
        { "remove_channels_revoked", reinterpret_cast<PyCFunction>(PushNotificationChannelManager_remove_ChannelsRevoked), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PushNotificationChannelManager[] = {
        { }
    };

    static PyType_Slot _type_slots_PushNotificationChannelManager[] = 
    {
        { Py_tp_new, _new_PushNotificationChannelManager },
        { Py_tp_methods, _methods_PushNotificationChannelManager },
        { Py_tp_getset, _getset_PushNotificationChannelManager },
        { },
    };

    static PyType_Spec _type_spec_PushNotificationChannelManager =
    {
        "_winsdk_Windows_Networking_PushNotifications.PushNotificationChannelManager",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PushNotificationChannelManager
    };

    // ----- PushNotificationChannelManagerForUser class --------------------
    constexpr const char* const _type_name_PushNotificationChannelManagerForUser = "PushNotificationChannelManagerForUser";

    static PyObject* _new_PushNotificationChannelManagerForUser(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PushNotificationChannelManagerForUser);
        return nullptr;
    }

    static void _dealloc_PushNotificationChannelManagerForUser(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PushNotificationChannelManagerForUser_CreatePushNotificationChannelForApplicationAsync(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.CreatePushNotificationChannelForApplicationAsync());
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.CreatePushNotificationChannelForApplicationAsync(param0));
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

    static PyObject* PushNotificationChannelManagerForUser_CreatePushNotificationChannelForSecondaryTileAsync(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.CreatePushNotificationChannelForSecondaryTileAsync(param0));
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

    static PyObject* PushNotificationChannelManagerForUser_CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsync(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);

                return py::convert(self->obj.CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsync(param0, param1));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 3)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);
                auto param2 = py::convert_to<winrt::hstring>(args, 2);

                return py::convert(self->obj.CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsync(param0, param1, param2));
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

    static PyObject* PushNotificationChannelManagerForUser_get_User(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.User());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_PushNotificationChannelManagerForUser(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PushNotificationChannelManagerForUser[] = {
        { "create_push_notification_channel_for_application_async", reinterpret_cast<PyCFunction>(PushNotificationChannelManagerForUser_CreatePushNotificationChannelForApplicationAsync), METH_VARARGS, nullptr },
        { "create_push_notification_channel_for_secondary_tile_async", reinterpret_cast<PyCFunction>(PushNotificationChannelManagerForUser_CreatePushNotificationChannelForSecondaryTileAsync), METH_VARARGS, nullptr },
        { "create_raw_push_notification_channel_with_alternate_key_for_application_async", reinterpret_cast<PyCFunction>(PushNotificationChannelManagerForUser_CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsync), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_PushNotificationChannelManagerForUser), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PushNotificationChannelManagerForUser[] = {
        { "user", reinterpret_cast<getter>(PushNotificationChannelManagerForUser_get_User), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PushNotificationChannelManagerForUser[] = 
    {
        { Py_tp_new, _new_PushNotificationChannelManagerForUser },
        { Py_tp_dealloc, _dealloc_PushNotificationChannelManagerForUser },
        { Py_tp_methods, _methods_PushNotificationChannelManagerForUser },
        { Py_tp_getset, _getset_PushNotificationChannelManagerForUser },
        { },
    };

    static PyType_Spec _type_spec_PushNotificationChannelManagerForUser =
    {
        "_winsdk_Windows_Networking_PushNotifications.PushNotificationChannelManagerForUser",
        sizeof(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PushNotificationChannelManagerForUser
    };

    // ----- PushNotificationChannelsRevokedEventArgs class --------------------
    constexpr const char* const _type_name_PushNotificationChannelsRevokedEventArgs = "PushNotificationChannelsRevokedEventArgs";

    static PyObject* _new_PushNotificationChannelsRevokedEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PushNotificationChannelsRevokedEventArgs);
        return nullptr;
    }

    static void _dealloc_PushNotificationChannelsRevokedEventArgs(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelsRevokedEventArgs* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* _from_PushNotificationChannelsRevokedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Networking::PushNotifications::PushNotificationChannelsRevokedEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PushNotificationChannelsRevokedEventArgs[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_PushNotificationChannelsRevokedEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PushNotificationChannelsRevokedEventArgs[] = {
        { }
    };

    static PyType_Slot _type_slots_PushNotificationChannelsRevokedEventArgs[] = 
    {
        { Py_tp_new, _new_PushNotificationChannelsRevokedEventArgs },
        { Py_tp_dealloc, _dealloc_PushNotificationChannelsRevokedEventArgs },
        { Py_tp_methods, _methods_PushNotificationChannelsRevokedEventArgs },
        { Py_tp_getset, _getset_PushNotificationChannelsRevokedEventArgs },
        { },
    };

    static PyType_Spec _type_spec_PushNotificationChannelsRevokedEventArgs =
    {
        "_winsdk_Windows_Networking_PushNotifications.PushNotificationChannelsRevokedEventArgs",
        sizeof(py::wrapper::Windows::Networking::PushNotifications::PushNotificationChannelsRevokedEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PushNotificationChannelsRevokedEventArgs
    };

    // ----- PushNotificationReceivedEventArgs class --------------------
    constexpr const char* const _type_name_PushNotificationReceivedEventArgs = "PushNotificationReceivedEventArgs";

    static PyObject* _new_PushNotificationReceivedEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PushNotificationReceivedEventArgs);
        return nullptr;
    }

    static void _dealloc_PushNotificationReceivedEventArgs(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PushNotificationReceivedEventArgs_get_Cancel(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Cancel());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PushNotificationReceivedEventArgs_put_Cancel(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.Cancel(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PushNotificationReceivedEventArgs_get_BadgeNotification(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.BadgeNotification());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationReceivedEventArgs_get_NotificationType(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.NotificationType());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationReceivedEventArgs_get_RawNotification(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.RawNotification());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationReceivedEventArgs_get_TileNotification(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TileNotification());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PushNotificationReceivedEventArgs_get_ToastNotification(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ToastNotification());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_PushNotificationReceivedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PushNotificationReceivedEventArgs[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_PushNotificationReceivedEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PushNotificationReceivedEventArgs[] = {
        { "cancel", reinterpret_cast<getter>(PushNotificationReceivedEventArgs_get_Cancel), reinterpret_cast<setter>(PushNotificationReceivedEventArgs_put_Cancel), nullptr, nullptr },
        { "badge_notification", reinterpret_cast<getter>(PushNotificationReceivedEventArgs_get_BadgeNotification), nullptr, nullptr, nullptr },
        { "notification_type", reinterpret_cast<getter>(PushNotificationReceivedEventArgs_get_NotificationType), nullptr, nullptr, nullptr },
        { "raw_notification", reinterpret_cast<getter>(PushNotificationReceivedEventArgs_get_RawNotification), nullptr, nullptr, nullptr },
        { "tile_notification", reinterpret_cast<getter>(PushNotificationReceivedEventArgs_get_TileNotification), nullptr, nullptr, nullptr },
        { "toast_notification", reinterpret_cast<getter>(PushNotificationReceivedEventArgs_get_ToastNotification), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PushNotificationReceivedEventArgs[] = 
    {
        { Py_tp_new, _new_PushNotificationReceivedEventArgs },
        { Py_tp_dealloc, _dealloc_PushNotificationReceivedEventArgs },
        { Py_tp_methods, _methods_PushNotificationReceivedEventArgs },
        { Py_tp_getset, _getset_PushNotificationReceivedEventArgs },
        { },
    };

    static PyType_Spec _type_spec_PushNotificationReceivedEventArgs =
    {
        "_winsdk_Windows_Networking_PushNotifications.PushNotificationReceivedEventArgs",
        sizeof(py::wrapper::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PushNotificationReceivedEventArgs
    };

    // ----- RawNotification class --------------------
    constexpr const char* const _type_name_RawNotification = "RawNotification";

    static PyObject* _new_RawNotification(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_RawNotification);
        return nullptr;
    }

    static void _dealloc_RawNotification(py::wrapper::Windows::Networking::PushNotifications::RawNotification* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* RawNotification_get_Content(py::wrapper::Windows::Networking::PushNotifications::RawNotification* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Content());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* RawNotification_get_ChannelId(py::wrapper::Windows::Networking::PushNotifications::RawNotification* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ChannelId());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* RawNotification_get_Headers(py::wrapper::Windows::Networking::PushNotifications::RawNotification* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Headers());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* RawNotification_get_ContentBytes(py::wrapper::Windows::Networking::PushNotifications::RawNotification* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ContentBytes());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_RawNotification(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Networking::PushNotifications::RawNotification>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_RawNotification[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_RawNotification), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_RawNotification[] = {
        { "content", reinterpret_cast<getter>(RawNotification_get_Content), nullptr, nullptr, nullptr },
        { "channel_id", reinterpret_cast<getter>(RawNotification_get_ChannelId), nullptr, nullptr, nullptr },
        { "headers", reinterpret_cast<getter>(RawNotification_get_Headers), nullptr, nullptr, nullptr },
        { "content_bytes", reinterpret_cast<getter>(RawNotification_get_ContentBytes), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_RawNotification[] = 
    {
        { Py_tp_new, _new_RawNotification },
        { Py_tp_dealloc, _dealloc_RawNotification },
        { Py_tp_methods, _methods_RawNotification },
        { Py_tp_getset, _getset_RawNotification },
        { },
    };

    static PyType_Spec _type_spec_RawNotification =
    {
        "_winsdk_Windows_Networking_PushNotifications.RawNotification",
        sizeof(py::wrapper::Windows::Networking::PushNotifications::RawNotification),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_RawNotification
    };

    // ----- Windows.Networking.PushNotifications Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannel>::python_type = py::register_python_type(module, _type_name_PushNotificationChannel, &_type_spec_PushNotificationChannel, bases.get());
            py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannelManager>::python_type = py::register_python_type(module, _type_name_PushNotificationChannelManager, &_type_spec_PushNotificationChannelManager, nullptr);
            py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannelManagerForUser>::python_type = py::register_python_type(module, _type_name_PushNotificationChannelManagerForUser, &_type_spec_PushNotificationChannelManagerForUser, bases.get());
            py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationChannelsRevokedEventArgs>::python_type = py::register_python_type(module, _type_name_PushNotificationChannelsRevokedEventArgs, &_type_spec_PushNotificationChannelsRevokedEventArgs, bases.get());
            py::winrt_type<winrt::Windows::Networking::PushNotifications::PushNotificationReceivedEventArgs>::python_type = py::register_python_type(module, _type_name_PushNotificationReceivedEventArgs, &_type_spec_PushNotificationReceivedEventArgs, bases.get());
            py::winrt_type<winrt::Windows::Networking::PushNotifications::RawNotification>::python_type = py::register_python_type(module, _type_name_RawNotification, &_type_spec_RawNotification, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Networking.PushNotifications");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Networking_PushNotifications",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Networking::PushNotifications

PyMODINIT_FUNC
PyInit__winsdk_Windows_Networking_PushNotifications (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Networking::PushNotifications::module_def);
}
