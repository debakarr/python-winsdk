// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#include "pybase.h"
#include "py.Windows.System.RemoteDesktop.h"


namespace py::cpp::Windows::System::RemoteDesktop
{
    struct module_state
    {
        PyTypeObject* type_InteractiveSession;
    };

    // ----- InteractiveSession class --------------------
    constexpr const char* const type_name_InteractiveSession = "InteractiveSession";

    static PyObject* _new_InteractiveSession(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(type_name_InteractiveSession);
        return nullptr;
    }

    static PyObject* InteractiveSession_get_IsRemote(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::System::RemoteDesktop::InteractiveSession::IsRemote());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_InteractiveSession[] = {
        { "get_is_remote", reinterpret_cast<PyCFunction>(InteractiveSession_get_IsRemote), METH_NOARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_InteractiveSession[] = {
        { }
    };

    static PyType_Slot _type_slots_InteractiveSession[] = 
    {
        { Py_tp_new, _new_InteractiveSession },
        { Py_tp_methods, _methods_InteractiveSession },
        { Py_tp_getset, _getset_InteractiveSession },
        { },
    };

    static PyType_Spec type_spec_InteractiveSession =
    {
        "_winsdk_Windows_System_RemoteDesktop.InteractiveSession",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_InteractiveSession
    };

    // ----- Windows.System.RemoteDesktop Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::System::RemoteDesktop");

    static PyMethodDef module_methods[] = {
        {}};


    static int module_traverse(PyObject* module, visitproc visit, void* arg) noexcept
    {
        auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));

        if (!state)
        {
            return 0;
        }

        Py_VISIT(state->type_InteractiveSession);

        return 0;
    }

    static int module_clear(PyObject* module) noexcept
    {
        auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));

        if (!state)
        {
            return 0;
        }

        Py_CLEAR(state->type_InteractiveSession);

        return 0;
    }


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_System_RemoteDesktop",
           module_doc,
           sizeof(module_state),
           module_methods,
           nullptr,
           module_traverse,
           module_clear,
           nullptr};

} // py::cpp::Windows::System::RemoteDesktop

PyMODINIT_FUNC PyInit__winsdk_Windows_System_RemoteDesktop(void) noexcept
{
    using namespace py::cpp::Windows::System::RemoteDesktop;

    py::pyobj_handle module{PyModule_Create(&module_def)};

    if (!module)
    {
        return nullptr;
    }

    auto object_type = py::get_python_type<py::Object>();
    if (!object_type)
    {
        return nullptr;
    }

    py::pyobj_handle bases{PyTuple_Pack(1, object_type)};

    if (!bases)
    {
        return nullptr;
    }

    py::pyobj_handle collections_abc_module{PyImport_ImportModule("collections.abc")};

    if (!collections_abc_module)
    {
        return nullptr;
    }

    py::pyobj_handle sequence_type{PyObject_GetAttrString(collections_abc_module.get(), "Sequence")};

    if (!sequence_type)
    {
        return nullptr;
    }

    py::pyobj_handle sequence_bases{PyTuple_Pack(2, object_type, sequence_type.get())};

    if (!sequence_bases)
    {
        return nullptr;
    }

    py::pyobj_handle mutable_sequence_type{PyObject_GetAttrString(collections_abc_module.get(), "MutableSequence")};

    if (!mutable_sequence_type)
    {
        return nullptr;
    }

    py::pyobj_handle mutable_sequence_bases{PyTuple_Pack(2, object_type, mutable_sequence_type.get())};

    if (!mutable_sequence_bases)
    {
        return nullptr;
    }

    py::pyobj_handle mapping_type{PyObject_GetAttrString(collections_abc_module.get(), "Mapping")};

    if (!mapping_type)
    {
        return nullptr;
    }

    py::pyobj_handle mapping_bases{PyTuple_Pack(2, object_type, mapping_type.get())};

    if (!mapping_bases)
    {
        return nullptr;
    }

    py::pyobj_handle mutable_mapping_type{PyObject_GetAttrString(collections_abc_module.get(), "MutableMapping")};

    if (!mutable_mapping_type)
    {
        return nullptr;
    }

    py::pyobj_handle mutable_mapping_bases{PyTuple_Pack(2, object_type, mutable_mapping_type.get())};

    if (!mutable_mapping_bases)
    {
        return nullptr;
    }

    auto state = reinterpret_cast<module_state*>(PyModule_GetState(module.get()));
    assert(state);

    state->type_InteractiveSession = py::register_python_type(module.get(), type_name_InteractiveSession, &type_spec_InteractiveSession, nullptr);
    if (!state->type_InteractiveSession)
    {
        return nullptr;
    }

    Py_INCREF(state->type_InteractiveSession);


    return module.detach();
}

PyTypeObject* py::winrt_type<winrt::Windows::System::RemoteDesktop::InteractiveSession>::get_python_type() noexcept {
    using namespace py::cpp::Windows::System::RemoteDesktop;

    PyObject* module = PyState_FindModule(&module_def);

    if (!module) {
        PyErr_SetString(PyExc_RuntimeError, "could not find module for Windows::System::RemoteDesktop");
        return nullptr;
    }

    auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));
    assert(state);

    auto python_type = state->type_InteractiveSession;

    if (!python_type) {
        PyErr_SetString(PyExc_RuntimeError, "type winrt::Windows::System::RemoteDesktop::InteractiveSession is not registered");
        return nullptr;
    }

    return python_type;
}
