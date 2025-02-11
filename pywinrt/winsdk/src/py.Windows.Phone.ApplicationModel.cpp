// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.5

#include "pybase.h"
#include "py.Windows.Phone.ApplicationModel.h"


namespace py::cpp::Windows::Phone::ApplicationModel
{
    struct module_state
    {
        PyObject* type_ApplicationProfileModes;
        PyTypeObject* type_ApplicationProfile;
    };

    static PyObject* register_ApplicationProfileModes(PyObject* module, PyObject* type)
    {
        auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));
        assert(state);

        if (state->type_ApplicationProfileModes)
        {
            PyErr_SetString(PyExc_RuntimeError, "type has already been registered");
            return nullptr;
        }

        if (!PyType_Check(type))
        {
            PyErr_SetString(PyExc_TypeError, "argument is not a type");
            return nullptr;
        }

        state->type_ApplicationProfileModes = type;
        Py_INCREF(state->type_ApplicationProfileModes);


        Py_RETURN_NONE;
    }

    // ----- ApplicationProfile class --------------------
    constexpr const char* const type_name_ApplicationProfile = "ApplicationProfile";

    static PyObject* _new_ApplicationProfile(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(type_name_ApplicationProfile);
        return nullptr;
    }

    static PyObject* ApplicationProfile_get_Modes(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Phone::ApplicationModel::ApplicationProfile::Modes());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ApplicationProfile[] = {
        { "get_modes", reinterpret_cast<PyCFunction>(ApplicationProfile_get_Modes), METH_NOARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ApplicationProfile[] = {
        { }
    };

    static PyType_Slot _type_slots_ApplicationProfile[] = 
    {
        { Py_tp_new, _new_ApplicationProfile },
        { Py_tp_methods, _methods_ApplicationProfile },
        { Py_tp_getset, _getset_ApplicationProfile },
        { },
    };

    static PyType_Spec type_spec_ApplicationProfile =
    {
        "_winsdk_Windows_Phone_ApplicationModel.ApplicationProfile",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ApplicationProfile
    };

    // ----- Windows.Phone.ApplicationModel Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::Phone::ApplicationModel");

    static PyMethodDef module_methods[] = {
        {"_register_ApplicationProfileModes", register_ApplicationProfileModes, METH_O, "registers type"},
        {}};


    static int module_traverse(PyObject* module, visitproc visit, void* arg) noexcept
    {
        auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));

        if (!state)
        {
            return 0;
        }

        Py_VISIT(state->type_ApplicationProfileModes);
        Py_VISIT(state->type_ApplicationProfile);

        return 0;
    }

    static int module_clear(PyObject* module) noexcept
    {
        auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));

        if (!state)
        {
            return 0;
        }

        Py_CLEAR(state->type_ApplicationProfileModes);
        Py_CLEAR(state->type_ApplicationProfile);

        return 0;
    }


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Phone_ApplicationModel",
           module_doc,
           sizeof(module_state),
           module_methods,
           nullptr,
           module_traverse,
           module_clear,
           nullptr};

} // py::cpp::Windows::Phone::ApplicationModel

PyMODINIT_FUNC PyInit__winsdk_Windows_Phone_ApplicationModel(void) noexcept
{
    using namespace py::cpp::Windows::Phone::ApplicationModel;

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

    state->type_ApplicationProfile = py::register_python_type(module.get(), type_name_ApplicationProfile, &type_spec_ApplicationProfile, nullptr);
    if (!state->type_ApplicationProfile)
    {
        return nullptr;
    }

    Py_INCREF(state->type_ApplicationProfile);


    return module.detach();
}

PyObject* py::py_type<winrt::Windows::Phone::ApplicationModel::ApplicationProfileModes>::get_python_type() noexcept {
    using namespace py::cpp::Windows::Phone::ApplicationModel;

    PyObject* module = PyState_FindModule(&module_def);

    if (!module) {
        PyErr_SetString(PyExc_RuntimeError, "could not find module for Windows::Phone::ApplicationModel");
        return nullptr;
    }

    auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));
    assert(state);

    auto python_type = state->type_ApplicationProfileModes;

    if (!python_type) {
        PyErr_SetString(PyExc_RuntimeError, "type winrt::Windows::Phone::ApplicationModel::ApplicationProfileModes is not registered");
        return nullptr;
    }

    return python_type;
}

PyTypeObject* py::winrt_type<winrt::Windows::Phone::ApplicationModel::ApplicationProfile>::get_python_type() noexcept {
    using namespace py::cpp::Windows::Phone::ApplicationModel;

    PyObject* module = PyState_FindModule(&module_def);

    if (!module) {
        PyErr_SetString(PyExc_RuntimeError, "could not find module for Windows::Phone::ApplicationModel");
        return nullptr;
    }

    auto state = reinterpret_cast<module_state*>(PyModule_GetState(module));
    assert(state);

    auto python_type = state->type_ApplicationProfile;

    if (!python_type) {
        PyErr_SetString(PyExc_RuntimeError, "type winrt::Windows::Phone::ApplicationModel::ApplicationProfile is not registered");
        return nullptr;
    }

    return python_type;
}
