// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Web.Http.Filters.h"

PyTypeObject* py::winrt_type<winrt::Windows::Web::Http::Filters::HttpBaseProtocolFilter>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Web::Http::Filters::HttpCacheControl>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Web::Http::Filters::IHttpFilter>::python_type;

namespace py::cpp::Windows::Web::Http::Filters
{
    // ----- HttpBaseProtocolFilter class --------------------
    constexpr const char* const _type_name_HttpBaseProtocolFilter = "HttpBaseProtocolFilter";

    static PyObject* _new_HttpBaseProtocolFilter(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        Py_ssize_t arg_count = PyTuple_Size(args);
        if (arg_count == 0)
        {
            try
            {
                winrt::Windows::Web::Http::Filters::HttpBaseProtocolFilter instance{  };
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

    static void _dealloc_HttpBaseProtocolFilter(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* HttpBaseProtocolFilter_ClearAuthenticationCache(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.ClearAuthenticationCache();
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

    static PyObject* HttpBaseProtocolFilter_Close(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* args) noexcept
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

    static PyObject* HttpBaseProtocolFilter_CreateForUser(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::System::User>(args, 0);

                return py::convert(winrt::Windows::Web::Http::Filters::HttpBaseProtocolFilter::CreateForUser(param0));
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

    static PyObject* HttpBaseProtocolFilter_SendRequestAsync(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Web::Http::HttpRequestMessage>(args, 0);

                return py::convert(self->obj.SendRequestAsync(param0));
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

    static PyObject* HttpBaseProtocolFilter_get_UseProxy(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.UseProxy());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_UseProxy(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.UseProxy(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_ServerCredential(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServerCredential());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_ServerCredential(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Security::Credentials::PasswordCredential>(arg);

            self->obj.ServerCredential(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_ProxyCredential(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ProxyCredential());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_ProxyCredential(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Security::Credentials::PasswordCredential>(arg);

            self->obj.ProxyCredential(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_MaxConnectionsPerServer(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MaxConnectionsPerServer());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_MaxConnectionsPerServer(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<uint32_t>(arg);

            self->obj.MaxConnectionsPerServer(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_ClientCertificate(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ClientCertificate());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_ClientCertificate(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Security::Cryptography::Certificates::Certificate>(arg);

            self->obj.ClientCertificate(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_AutomaticDecompression(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AutomaticDecompression());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_AutomaticDecompression(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.AutomaticDecompression(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_AllowUI(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AllowUI());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_AllowUI(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.AllowUI(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_AllowAutoRedirect(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AllowAutoRedirect());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_AllowAutoRedirect(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.AllowAutoRedirect(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_CacheControl(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CacheControl());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_CookieManager(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CookieManager());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_IgnorableServerCertificateErrors(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IgnorableServerCertificateErrors());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_MaxVersion(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MaxVersion());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_MaxVersion(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Web::Http::HttpVersion>(arg);

            self->obj.MaxVersion(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_CookieUsageBehavior(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CookieUsageBehavior());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpBaseProtocolFilter_put_CookieUsageBehavior(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Web::Http::Filters::HttpCookieUsageBehavior>(arg);

            self->obj.CookieUsageBehavior(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpBaseProtocolFilter_get_User(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, void* /*unused*/) noexcept
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

    static PyObject* HttpBaseProtocolFilter_add_ServerCustomValidationRequested(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::Web::Http::Filters::HttpBaseProtocolFilter, winrt::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs>>(arg);

            return py::convert(self->obj.ServerCustomValidationRequested(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpBaseProtocolFilter_remove_ServerCustomValidationRequested(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.ServerCustomValidationRequested(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_HttpBaseProtocolFilter(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Web::Http::Filters::HttpBaseProtocolFilter>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_HttpBaseProtocolFilter(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_HttpBaseProtocolFilter(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter* self) noexcept
    {
        try
        {
            self->obj.Close();
            Py_RETURN_FALSE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_HttpBaseProtocolFilter[] = {
        { "clear_authentication_cache", reinterpret_cast<PyCFunction>(HttpBaseProtocolFilter_ClearAuthenticationCache), METH_VARARGS, nullptr },
        { "close", reinterpret_cast<PyCFunction>(HttpBaseProtocolFilter_Close), METH_VARARGS, nullptr },
        { "create_for_user", reinterpret_cast<PyCFunction>(HttpBaseProtocolFilter_CreateForUser), METH_VARARGS | METH_STATIC, nullptr },
        { "send_request_async", reinterpret_cast<PyCFunction>(HttpBaseProtocolFilter_SendRequestAsync), METH_VARARGS, nullptr },
        { "add_server_custom_validation_requested", reinterpret_cast<PyCFunction>(HttpBaseProtocolFilter_add_ServerCustomValidationRequested), METH_O, nullptr },
        { "remove_server_custom_validation_requested", reinterpret_cast<PyCFunction>(HttpBaseProtocolFilter_remove_ServerCustomValidationRequested), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_HttpBaseProtocolFilter), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_HttpBaseProtocolFilter), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_HttpBaseProtocolFilter), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_HttpBaseProtocolFilter[] = {
        { "use_proxy", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_UseProxy), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_UseProxy), nullptr, nullptr },
        { "server_credential", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_ServerCredential), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_ServerCredential), nullptr, nullptr },
        { "proxy_credential", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_ProxyCredential), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_ProxyCredential), nullptr, nullptr },
        { "max_connections_per_server", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_MaxConnectionsPerServer), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_MaxConnectionsPerServer), nullptr, nullptr },
        { "client_certificate", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_ClientCertificate), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_ClientCertificate), nullptr, nullptr },
        { "automatic_decompression", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_AutomaticDecompression), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_AutomaticDecompression), nullptr, nullptr },
        { "allow_u_i", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_AllowUI), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_AllowUI), nullptr, nullptr },
        { "allow_auto_redirect", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_AllowAutoRedirect), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_AllowAutoRedirect), nullptr, nullptr },
        { "cache_control", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_CacheControl), nullptr, nullptr, nullptr },
        { "cookie_manager", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_CookieManager), nullptr, nullptr, nullptr },
        { "ignorable_server_certificate_errors", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_IgnorableServerCertificateErrors), nullptr, nullptr, nullptr },
        { "max_version", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_MaxVersion), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_MaxVersion), nullptr, nullptr },
        { "cookie_usage_behavior", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_CookieUsageBehavior), reinterpret_cast<setter>(HttpBaseProtocolFilter_put_CookieUsageBehavior), nullptr, nullptr },
        { "user", reinterpret_cast<getter>(HttpBaseProtocolFilter_get_User), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_HttpBaseProtocolFilter[] = 
    {
        { Py_tp_new, _new_HttpBaseProtocolFilter },
        { Py_tp_dealloc, _dealloc_HttpBaseProtocolFilter },
        { Py_tp_methods, _methods_HttpBaseProtocolFilter },
        { Py_tp_getset, _getset_HttpBaseProtocolFilter },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_HttpBaseProtocolFilter =
    {
        "_winsdk_Windows_Web_Http_Filters.HttpBaseProtocolFilter",
        sizeof(py::wrapper::Windows::Web::Http::Filters::HttpBaseProtocolFilter),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_HttpBaseProtocolFilter
    };

    // ----- HttpCacheControl class --------------------
    constexpr const char* const _type_name_HttpCacheControl = "HttpCacheControl";

    static PyObject* _new_HttpCacheControl(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_HttpCacheControl);
        return nullptr;
    }

    static void _dealloc_HttpCacheControl(py::wrapper::Windows::Web::Http::Filters::HttpCacheControl* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* HttpCacheControl_get_WriteBehavior(py::wrapper::Windows::Web::Http::Filters::HttpCacheControl* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.WriteBehavior());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpCacheControl_put_WriteBehavior(py::wrapper::Windows::Web::Http::Filters::HttpCacheControl* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Web::Http::Filters::HttpCacheWriteBehavior>(arg);

            self->obj.WriteBehavior(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* HttpCacheControl_get_ReadBehavior(py::wrapper::Windows::Web::Http::Filters::HttpCacheControl* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ReadBehavior());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int HttpCacheControl_put_ReadBehavior(py::wrapper::Windows::Web::Http::Filters::HttpCacheControl* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Web::Http::Filters::HttpCacheReadBehavior>(arg);

            self->obj.ReadBehavior(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* _from_HttpCacheControl(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Web::Http::Filters::HttpCacheControl>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_HttpCacheControl[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_HttpCacheControl), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_HttpCacheControl[] = {
        { "write_behavior", reinterpret_cast<getter>(HttpCacheControl_get_WriteBehavior), reinterpret_cast<setter>(HttpCacheControl_put_WriteBehavior), nullptr, nullptr },
        { "read_behavior", reinterpret_cast<getter>(HttpCacheControl_get_ReadBehavior), reinterpret_cast<setter>(HttpCacheControl_put_ReadBehavior), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_HttpCacheControl[] = 
    {
        { Py_tp_new, _new_HttpCacheControl },
        { Py_tp_dealloc, _dealloc_HttpCacheControl },
        { Py_tp_methods, _methods_HttpCacheControl },
        { Py_tp_getset, _getset_HttpCacheControl },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_HttpCacheControl =
    {
        "_winsdk_Windows_Web_Http_Filters.HttpCacheControl",
        sizeof(py::wrapper::Windows::Web::Http::Filters::HttpCacheControl),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_HttpCacheControl
    };

    // ----- HttpServerCustomValidationRequestedEventArgs class --------------------
    constexpr const char* const _type_name_HttpServerCustomValidationRequestedEventArgs = "HttpServerCustomValidationRequestedEventArgs";

    static PyObject* _new_HttpServerCustomValidationRequestedEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_HttpServerCustomValidationRequestedEventArgs);
        return nullptr;
    }

    static void _dealloc_HttpServerCustomValidationRequestedEventArgs(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* HttpServerCustomValidationRequestedEventArgs_GetDeferral(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetDeferral());
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

    static PyObject* HttpServerCustomValidationRequestedEventArgs_Reject(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.Reject();
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

    static PyObject* HttpServerCustomValidationRequestedEventArgs_get_RequestMessage(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.RequestMessage());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpServerCustomValidationRequestedEventArgs_get_ServerCertificate(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServerCertificate());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpServerCustomValidationRequestedEventArgs_get_ServerCertificateErrorSeverity(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServerCertificateErrorSeverity());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpServerCustomValidationRequestedEventArgs_get_ServerCertificateErrors(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServerCertificateErrors());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* HttpServerCustomValidationRequestedEventArgs_get_ServerIntermediateCertificates(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ServerIntermediateCertificates());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_HttpServerCustomValidationRequestedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_HttpServerCustomValidationRequestedEventArgs[] = {
        { "get_deferral", reinterpret_cast<PyCFunction>(HttpServerCustomValidationRequestedEventArgs_GetDeferral), METH_VARARGS, nullptr },
        { "reject", reinterpret_cast<PyCFunction>(HttpServerCustomValidationRequestedEventArgs_Reject), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_HttpServerCustomValidationRequestedEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_HttpServerCustomValidationRequestedEventArgs[] = {
        { "request_message", reinterpret_cast<getter>(HttpServerCustomValidationRequestedEventArgs_get_RequestMessage), nullptr, nullptr, nullptr },
        { "server_certificate", reinterpret_cast<getter>(HttpServerCustomValidationRequestedEventArgs_get_ServerCertificate), nullptr, nullptr, nullptr },
        { "server_certificate_error_severity", reinterpret_cast<getter>(HttpServerCustomValidationRequestedEventArgs_get_ServerCertificateErrorSeverity), nullptr, nullptr, nullptr },
        { "server_certificate_errors", reinterpret_cast<getter>(HttpServerCustomValidationRequestedEventArgs_get_ServerCertificateErrors), nullptr, nullptr, nullptr },
        { "server_intermediate_certificates", reinterpret_cast<getter>(HttpServerCustomValidationRequestedEventArgs_get_ServerIntermediateCertificates), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_HttpServerCustomValidationRequestedEventArgs[] = 
    {
        { Py_tp_new, _new_HttpServerCustomValidationRequestedEventArgs },
        { Py_tp_dealloc, _dealloc_HttpServerCustomValidationRequestedEventArgs },
        { Py_tp_methods, _methods_HttpServerCustomValidationRequestedEventArgs },
        { Py_tp_getset, _getset_HttpServerCustomValidationRequestedEventArgs },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_HttpServerCustomValidationRequestedEventArgs =
    {
        "_winsdk_Windows_Web_Http_Filters.HttpServerCustomValidationRequestedEventArgs",
        sizeof(py::wrapper::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_HttpServerCustomValidationRequestedEventArgs
    };

    // ----- IHttpFilter interface --------------------
    constexpr const char* const _type_name_IHttpFilter = "IHttpFilter";

    static PyObject* _new_IHttpFilter(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IHttpFilter);
        return nullptr;
    }

    static void _dealloc_IHttpFilter(py::wrapper::Windows::Web::Http::Filters::IHttpFilter* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IHttpFilter_Close(py::wrapper::Windows::Web::Http::Filters::IHttpFilter* self, PyObject* args) noexcept
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

    static PyObject* IHttpFilter_SendRequestAsync(py::wrapper::Windows::Web::Http::Filters::IHttpFilter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Web::Http::HttpRequestMessage>(args, 0);

                return py::convert(self->obj.SendRequestAsync(param0));
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

    static PyObject* _from_IHttpFilter(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Web::Http::Filters::IHttpFilter>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_IHttpFilter(py::wrapper::Windows::Web::Http::Filters::IHttpFilter* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_IHttpFilter(py::wrapper::Windows::Web::Http::Filters::IHttpFilter* self) noexcept
    {
        try
        {
            self->obj.Close();
            Py_RETURN_FALSE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IHttpFilter[] = {
        { "send_request_async", reinterpret_cast<PyCFunction>(IHttpFilter_SendRequestAsync), METH_VARARGS, nullptr },
        { "close", reinterpret_cast<PyCFunction>(IHttpFilter_Close), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IHttpFilter), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_IHttpFilter), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_IHttpFilter), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_IHttpFilter[] = {
        { }
    };

    static PyType_Slot _type_slots_IHttpFilter[] = 
    {
        { Py_tp_new, _new_IHttpFilter },
        { Py_tp_dealloc, _dealloc_IHttpFilter },
        { Py_tp_methods, _methods_IHttpFilter },
        { Py_tp_getset, _getset_IHttpFilter },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_IHttpFilter =
    {
        "_winsdk_Windows_Web_Http_Filters.IHttpFilter",
        sizeof(py::wrapper::Windows::Web::Http::Filters::IHttpFilter),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IHttpFilter
    };

    // ----- Windows.Web.Http.Filters Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Web::Http::Filters::HttpBaseProtocolFilter>::python_type = py::register_python_type(module, _type_name_HttpBaseProtocolFilter, &_type_spec_HttpBaseProtocolFilter, bases.get());
            py::winrt_type<winrt::Windows::Web::Http::Filters::HttpCacheControl>::python_type = py::register_python_type(module, _type_name_HttpCacheControl, &_type_spec_HttpCacheControl, bases.get());
            py::winrt_type<winrt::Windows::Web::Http::Filters::HttpServerCustomValidationRequestedEventArgs>::python_type = py::register_python_type(module, _type_name_HttpServerCustomValidationRequestedEventArgs, &_type_spec_HttpServerCustomValidationRequestedEventArgs, bases.get());
            py::winrt_type<winrt::Windows::Web::Http::Filters::IHttpFilter>::python_type = py::register_python_type(module, _type_name_IHttpFilter, &_type_spec_IHttpFilter, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Web.Http.Filters");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Web_Http_Filters",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Web::Http::Filters

PyMODINIT_FUNC
PyInit__winsdk_Windows_Web_Http_Filters (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Web::Http::Filters::module_def);
}
