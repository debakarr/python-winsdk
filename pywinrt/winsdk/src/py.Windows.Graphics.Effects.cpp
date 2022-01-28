// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Graphics.Effects.h"

PyTypeObject* py::winrt_type<winrt::Windows::Graphics::Effects::IGraphicsEffect>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>::python_type;

namespace py::cpp::Windows::Graphics::Effects
{
    // ----- IGraphicsEffect interface --------------------
    constexpr const char* const _type_name_IGraphicsEffect = "IGraphicsEffect";

    static PyObject* _new_IGraphicsEffect(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IGraphicsEffect);
        return nullptr;
    }

    static void _dealloc_IGraphicsEffect(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* IGraphicsEffect_get_Name(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Name());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int IGraphicsEffect_put_Name(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.Name(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* _from_IGraphicsEffect(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Graphics::Effects::IGraphicsEffect>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IGraphicsEffect[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_IGraphicsEffect), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IGraphicsEffect[] = {
        { "name", reinterpret_cast<getter>(IGraphicsEffect_get_Name), reinterpret_cast<setter>(IGraphicsEffect_put_Name), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_IGraphicsEffect[] = 
    {
        { Py_tp_new, _new_IGraphicsEffect },
        { Py_tp_dealloc, _dealloc_IGraphicsEffect },
        { Py_tp_methods, _methods_IGraphicsEffect },
        { Py_tp_getset, _getset_IGraphicsEffect },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_IGraphicsEffect =
    {
        "_winsdk_Windows_Graphics_Effects.IGraphicsEffect",
        sizeof(py::wrapper::Windows::Graphics::Effects::IGraphicsEffect),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IGraphicsEffect
    };

    // ----- IGraphicsEffectSource interface --------------------
    constexpr const char* const _type_name_IGraphicsEffectSource = "IGraphicsEffectSource";

    static PyObject* _new_IGraphicsEffectSource(PyTypeObject* /* unused */, PyObject* /* unused */, PyObject* /* unused */)
    {
        py::set_invalid_activation_error(_type_name_IGraphicsEffectSource);
        return nullptr;
    }

    static void _dealloc_IGraphicsEffectSource(py::wrapper::Windows::Graphics::Effects::IGraphicsEffectSource* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* _from_IGraphicsEffectSource(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IGraphicsEffectSource[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_IGraphicsEffectSource), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IGraphicsEffectSource[] = {
        { }
    };

    static PyType_Slot _type_slots_IGraphicsEffectSource[] = 
    {
        { Py_tp_new, _new_IGraphicsEffectSource },
        { Py_tp_dealloc, _dealloc_IGraphicsEffectSource },
        { Py_tp_methods, _methods_IGraphicsEffectSource },
        { Py_tp_getset, _getset_IGraphicsEffectSource },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_IGraphicsEffectSource =
    {
        "_winsdk_Windows_Graphics_Effects.IGraphicsEffectSource",
        sizeof(py::wrapper::Windows::Graphics::Effects::IGraphicsEffectSource),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IGraphicsEffectSource
    };

    // ----- Windows.Graphics.Effects Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Graphics::Effects::IGraphicsEffect>::python_type = py::register_python_type(module, _type_name_IGraphicsEffect, &_type_spec_IGraphicsEffect, bases.get());
            py::winrt_type<winrt::Windows::Graphics::Effects::IGraphicsEffectSource>::python_type = py::register_python_type(module, _type_name_IGraphicsEffectSource, &_type_spec_IGraphicsEffectSource, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Graphics.Effects");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Graphics_Effects",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Graphics::Effects

PyMODINIT_FUNC
PyInit__winsdk_Windows_Graphics_Effects (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Graphics::Effects::module_def);
}
