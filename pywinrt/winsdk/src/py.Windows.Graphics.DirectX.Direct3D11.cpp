// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#include "pybase.h"
#include "py.Windows.Graphics.DirectX.Direct3D11.h"

PyTypeObject* py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>::python_type;

PyObject* py::converter<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>::convert(winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription instance) noexcept
{
    return py::wrap_struct(instance, py::get_python_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>());
}
winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription py::converter<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>::convert_to(PyObject* obj)
{
    throw_if_pyobj_null(obj);

    if (Py_TYPE(obj) == py::get_python_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>())
    {
        return reinterpret_cast<py::winrt_struct_wrapper<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>*>(obj)->obj;
    }

    if (!PyDict_Check(obj))
    {
        throw winrt::hresult_invalid_argument();
    }

    winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription return_value{};

    PyObject* py_Count = PyDict_GetItemString(obj, "count");
    if (!py_Count) { throw winrt::hresult_invalid_argument(); }
    return_value.Count = converter<int32_t>::convert_to(py_Count);

    PyObject* py_Quality = PyDict_GetItemString(obj, "quality");
    if (!py_Quality) { throw winrt::hresult_invalid_argument(); }
    return_value.Quality = converter<int32_t>::convert_to(py_Quality);

    return return_value;
}

PyObject* py::converter<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>::convert(winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription instance) noexcept
{
    return py::wrap_struct(instance, py::get_python_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>());
}
winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription py::converter<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>::convert_to(PyObject* obj)
{
    throw_if_pyobj_null(obj);

    if (Py_TYPE(obj) == py::get_python_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>())
    {
        return reinterpret_cast<py::winrt_struct_wrapper<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>*>(obj)->obj;
    }

    if (!PyDict_Check(obj))
    {
        throw winrt::hresult_invalid_argument();
    }

    winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription return_value{};

    PyObject* py_Width = PyDict_GetItemString(obj, "width");
    if (!py_Width) { throw winrt::hresult_invalid_argument(); }
    return_value.Width = converter<int32_t>::convert_to(py_Width);

    PyObject* py_Height = PyDict_GetItemString(obj, "height");
    if (!py_Height) { throw winrt::hresult_invalid_argument(); }
    return_value.Height = converter<int32_t>::convert_to(py_Height);

    PyObject* py_Format = PyDict_GetItemString(obj, "format");
    if (!py_Format) { throw winrt::hresult_invalid_argument(); }
    return_value.Format = converter<winrt::Windows::Graphics::DirectX::DirectXPixelFormat>::convert_to(py_Format);

    PyObject* py_MultisampleDescription = PyDict_GetItemString(obj, "multisample_description");
    if (!py_MultisampleDescription) { throw winrt::hresult_invalid_argument(); }
    return_value.MultisampleDescription = converter<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>::convert_to(py_MultisampleDescription);

    return return_value;
}

namespace py::cpp::Windows::Graphics::DirectX::Direct3D11
{
    // ----- IDirect3DDevice interface --------------------
    constexpr const char* const _type_name_IDirect3DDevice = "IDirect3DDevice";

    static PyObject* _new_IDirect3DDevice(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IDirect3DDevice);
        return nullptr;
    }

    static void _dealloc_IDirect3DDevice(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IDirect3DDevice_Close(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice* self, PyObject* args) noexcept
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

    static PyObject* IDirect3DDevice_Trim(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                self->obj.Trim();
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

    static PyObject* _from_IDirect3DDevice(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_IDirect3DDevice(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_IDirect3DDevice(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice* self) noexcept
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

    static PyMethodDef _methods_IDirect3DDevice[] = {
        { "trim", reinterpret_cast<PyCFunction>(IDirect3DDevice_Trim), METH_VARARGS, nullptr },
        { "close", reinterpret_cast<PyCFunction>(IDirect3DDevice_Close), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IDirect3DDevice), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_IDirect3DDevice), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_IDirect3DDevice), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_IDirect3DDevice[] = {
        { }
    };

    static PyType_Slot _type_slots_IDirect3DDevice[] = 
    {
        { Py_tp_new, _new_IDirect3DDevice },
        { Py_tp_dealloc, _dealloc_IDirect3DDevice },
        { Py_tp_methods, _methods_IDirect3DDevice },
        { Py_tp_getset, _getset_IDirect3DDevice },
        { },
    };

    static PyType_Spec _type_spec_IDirect3DDevice =
    {
        "_winsdk_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice",
        sizeof(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IDirect3DDevice
    };

    // ----- IDirect3DSurface interface --------------------
    constexpr const char* const _type_name_IDirect3DSurface = "IDirect3DSurface";

    static PyObject* _new_IDirect3DSurface(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IDirect3DSurface);
        return nullptr;
    }

    static void _dealloc_IDirect3DSurface(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IDirect3DSurface_Close(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface* self, PyObject* args) noexcept
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

    static PyObject* IDirect3DSurface_get_Description(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Description());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_IDirect3DSurface(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_IDirect3DSurface(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_IDirect3DSurface(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface* self) noexcept
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

    static PyMethodDef _methods_IDirect3DSurface[] = {
        { "close", reinterpret_cast<PyCFunction>(IDirect3DSurface_Close), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IDirect3DSurface), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_IDirect3DSurface), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_IDirect3DSurface), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_IDirect3DSurface[] = {
        { "description", reinterpret_cast<getter>(IDirect3DSurface_get_Description), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_IDirect3DSurface[] = 
    {
        { Py_tp_new, _new_IDirect3DSurface },
        { Py_tp_dealloc, _dealloc_IDirect3DSurface },
        { Py_tp_methods, _methods_IDirect3DSurface },
        { Py_tp_getset, _getset_IDirect3DSurface },
        { },
    };

    static PyType_Spec _type_spec_IDirect3DSurface =
    {
        "_winsdk_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface",
        sizeof(py::wrapper::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IDirect3DSurface
    };

    // ----- Direct3DMultisampleDescription struct --------------------
    constexpr const char* const _type_name_Direct3DMultisampleDescription = "Direct3DMultisampleDescription";

    PyObject* _new_Direct3DMultisampleDescription(PyTypeObject* type, PyObject* args, PyObject* kwds)
    {
        auto tuple_size = PyTuple_Size(args);

        if ((tuple_size == 0) && (kwds == nullptr))
        {
            try
            {
                winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription return_value{};
                return py::convert(return_value);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }

        if ((tuple_size == 1) && (kwds == nullptr))
        {
            auto arg = PyTuple_GetItem(args, 0);
            if (PyDict_Check(arg))
            {
                try
                {
                    auto return_value = py::convert_to<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>(arg);
                    return py::convert(return_value);
                }
                catch (...)
                {
                    py::to_PyErr();
                    return nullptr;
                }
            }
        }

        int32_t _Count{};
        int32_t _Quality{};

        static const char* kwlist[] = {"count", "quality", nullptr};
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "ii", const_cast<char**>(kwlist), &_Count, &_Quality))
        {
            return nullptr;
        }

        try
        {
            winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription return_value{ _Count, _Quality };
            return py::convert(return_value);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static void _dealloc_Direct3DMultisampleDescription(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription* self)
    {
    }

    static PyObject* Direct3DMultisampleDescription_get_Count(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Count);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int Direct3DMultisampleDescription_set_Count(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            self->obj.Count = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* Direct3DMultisampleDescription_get_Quality(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Quality);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int Direct3DMultisampleDescription_set_Quality(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            self->obj.Quality = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyGetSetDef _getset_Direct3DMultisampleDescription[] = {
        { "count", reinterpret_cast<getter>(Direct3DMultisampleDescription_get_Count), reinterpret_cast<setter>(Direct3DMultisampleDescription_set_Count), nullptr, nullptr },
        { "quality", reinterpret_cast<getter>(Direct3DMultisampleDescription_get_Quality), reinterpret_cast<setter>(Direct3DMultisampleDescription_set_Quality), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_Direct3DMultisampleDescription[] = 
    {
        { Py_tp_new, _new_Direct3DMultisampleDescription },
        { Py_tp_dealloc, _dealloc_Direct3DMultisampleDescription },
        { Py_tp_getset, _getset_Direct3DMultisampleDescription },
        { },
    };

    static PyType_Spec _type_spec_Direct3DMultisampleDescription =
    {
        "_winsdk_Windows_Graphics_DirectX_Direct3D11.Direct3DMultisampleDescription",
        sizeof(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_Direct3DMultisampleDescription
    };

    // ----- Direct3DSurfaceDescription struct --------------------
    constexpr const char* const _type_name_Direct3DSurfaceDescription = "Direct3DSurfaceDescription";

    PyObject* _new_Direct3DSurfaceDescription(PyTypeObject* type, PyObject* args, PyObject* kwds)
    {
        auto tuple_size = PyTuple_Size(args);

        if ((tuple_size == 0) && (kwds == nullptr))
        {
            try
            {
                winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription return_value{};
                return py::convert(return_value);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }

        if ((tuple_size == 1) && (kwds == nullptr))
        {
            auto arg = PyTuple_GetItem(args, 0);
            if (PyDict_Check(arg))
            {
                try
                {
                    auto return_value = py::convert_to<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>(arg);
                    return py::convert(return_value);
                }
                catch (...)
                {
                    py::to_PyErr();
                    return nullptr;
                }
            }
        }

        int32_t _Width{};
        int32_t _Height{};
        int32_t _Format{};
        PyObject* _MultisampleDescription{};

        static const char* kwlist[] = {"width", "height", "format", "multisample_description", nullptr};
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "iiiO", const_cast<char**>(kwlist), &_Width, &_Height, &_Format, &_MultisampleDescription))
        {
            return nullptr;
        }

        try
        {
            winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription return_value{ _Width, _Height, static_cast<winrt::Windows::Graphics::DirectX::DirectXPixelFormat>(_Format), py::converter<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>::convert_to(_MultisampleDescription) };
            return py::convert(return_value);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static void _dealloc_Direct3DSurfaceDescription(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self)
    {
    }

    static PyObject* Direct3DSurfaceDescription_get_Width(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Width);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int Direct3DSurfaceDescription_set_Width(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            self->obj.Width = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* Direct3DSurfaceDescription_get_Height(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Height);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int Direct3DSurfaceDescription_set_Height(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            self->obj.Height = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* Direct3DSurfaceDescription_get_Format(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Format);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int Direct3DSurfaceDescription_set_Format(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            self->obj.Format = py::converter<winrt::Windows::Graphics::DirectX::DirectXPixelFormat>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* Direct3DSurfaceDescription_get_MultisampleDescription(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.MultisampleDescription);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int Direct3DSurfaceDescription_set_MultisampleDescription(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            self->obj.MultisampleDescription = py::converter<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyGetSetDef _getset_Direct3DSurfaceDescription[] = {
        { "width", reinterpret_cast<getter>(Direct3DSurfaceDescription_get_Width), reinterpret_cast<setter>(Direct3DSurfaceDescription_set_Width), nullptr, nullptr },
        { "height", reinterpret_cast<getter>(Direct3DSurfaceDescription_get_Height), reinterpret_cast<setter>(Direct3DSurfaceDescription_set_Height), nullptr, nullptr },
        { "format", reinterpret_cast<getter>(Direct3DSurfaceDescription_get_Format), reinterpret_cast<setter>(Direct3DSurfaceDescription_set_Format), nullptr, nullptr },
        { "multisample_description", reinterpret_cast<getter>(Direct3DSurfaceDescription_get_MultisampleDescription), reinterpret_cast<setter>(Direct3DSurfaceDescription_set_MultisampleDescription), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_Direct3DSurfaceDescription[] = 
    {
        { Py_tp_new, _new_Direct3DSurfaceDescription },
        { Py_tp_dealloc, _dealloc_Direct3DSurfaceDescription },
        { Py_tp_getset, _getset_Direct3DSurfaceDescription },
        { },
    };

    static PyType_Spec _type_spec_Direct3DSurfaceDescription =
    {
        "_winsdk_Windows_Graphics_DirectX_Direct3D11.Direct3DSurfaceDescription",
        sizeof(py::wrapper::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_Direct3DSurfaceDescription
    };

    // ----- Windows.Graphics.DirectX.Direct3D11 Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::IDirect3DDevice>::python_type = py::register_python_type(module, _type_name_IDirect3DDevice, &_type_spec_IDirect3DDevice, bases.get());
            py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::IDirect3DSurface>::python_type = py::register_python_type(module, _type_name_IDirect3DSurface, &_type_spec_IDirect3DSurface, bases.get());
            py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DMultisampleDescription>::python_type = py::register_python_type(module, _type_name_Direct3DMultisampleDescription, &_type_spec_Direct3DMultisampleDescription, bases.get());
            py::winrt_type<winrt::Windows::Graphics::DirectX::Direct3D11::Direct3DSurfaceDescription>::python_type = py::register_python_type(module, _type_name_Direct3DSurfaceDescription, &_type_spec_Direct3DSurfaceDescription, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Graphics.DirectX.Direct3D11");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Graphics_DirectX_Direct3D11",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Graphics::DirectX::Direct3D11

PyMODINIT_FUNC
PyInit__winsdk_Windows_Graphics_DirectX_Direct3D11 (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Graphics::DirectX::Direct3D11::module_def);
}
