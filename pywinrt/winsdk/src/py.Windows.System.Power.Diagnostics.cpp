// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.System.Power.Diagnostics.h"

PyTypeObject* py::winrt_type<winrt::Windows::System::Power::Diagnostics::BackgroundEnergyDiagnostics>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::System::Power::Diagnostics::ForegroundEnergyDiagnostics>::python_type;

namespace py::cpp::Windows::System::Power::Diagnostics
{
    // ----- BackgroundEnergyDiagnostics class --------------------
    constexpr const char* const _type_name_BackgroundEnergyDiagnostics = "BackgroundEnergyDiagnostics";

    static PyObject* _new_BackgroundEnergyDiagnostics(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_BackgroundEnergyDiagnostics);
        return nullptr;
    }

    static PyObject* BackgroundEnergyDiagnostics_ComputeTotalEnergyUsage(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::System::Power::Diagnostics::BackgroundEnergyDiagnostics::ComputeTotalEnergyUsage());
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

    static PyObject* BackgroundEnergyDiagnostics_ResetTotalEnergyUsage(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                winrt::Windows::System::Power::Diagnostics::BackgroundEnergyDiagnostics::ResetTotalEnergyUsage();
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

    static PyObject* BackgroundEnergyDiagnostics_get_DeviceSpecificConversionFactor(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::System::Power::Diagnostics::BackgroundEnergyDiagnostics::DeviceSpecificConversionFactor());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_BackgroundEnergyDiagnostics[] = {
        { "compute_total_energy_usage", reinterpret_cast<PyCFunction>(BackgroundEnergyDiagnostics_ComputeTotalEnergyUsage), METH_VARARGS | METH_STATIC, nullptr },
        { "reset_total_energy_usage", reinterpret_cast<PyCFunction>(BackgroundEnergyDiagnostics_ResetTotalEnergyUsage), METH_VARARGS | METH_STATIC, nullptr },
        { "get_device_specific_conversion_factor", reinterpret_cast<PyCFunction>(BackgroundEnergyDiagnostics_get_DeviceSpecificConversionFactor), METH_NOARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_BackgroundEnergyDiagnostics[] = {
        { }
    };

    static PyType_Slot _type_slots_BackgroundEnergyDiagnostics[] = 
    {
        { Py_tp_new, _new_BackgroundEnergyDiagnostics },
        { Py_tp_methods, _methods_BackgroundEnergyDiagnostics },
        { Py_tp_getset, _getset_BackgroundEnergyDiagnostics },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_BackgroundEnergyDiagnostics =
    {
        "_winsdk_Windows_System_Power_Diagnostics.BackgroundEnergyDiagnostics",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_BackgroundEnergyDiagnostics
    };

    // ----- ForegroundEnergyDiagnostics class --------------------
    constexpr const char* const _type_name_ForegroundEnergyDiagnostics = "ForegroundEnergyDiagnostics";

    static PyObject* _new_ForegroundEnergyDiagnostics(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_ForegroundEnergyDiagnostics);
        return nullptr;
    }

    static PyObject* ForegroundEnergyDiagnostics_ComputeTotalEnergyUsage(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::System::Power::Diagnostics::ForegroundEnergyDiagnostics::ComputeTotalEnergyUsage());
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

    static PyObject* ForegroundEnergyDiagnostics_ResetTotalEnergyUsage(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                winrt::Windows::System::Power::Diagnostics::ForegroundEnergyDiagnostics::ResetTotalEnergyUsage();
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

    static PyObject* ForegroundEnergyDiagnostics_get_DeviceSpecificConversionFactor(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::System::Power::Diagnostics::ForegroundEnergyDiagnostics::DeviceSpecificConversionFactor());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ForegroundEnergyDiagnostics[] = {
        { "compute_total_energy_usage", reinterpret_cast<PyCFunction>(ForegroundEnergyDiagnostics_ComputeTotalEnergyUsage), METH_VARARGS | METH_STATIC, nullptr },
        { "reset_total_energy_usage", reinterpret_cast<PyCFunction>(ForegroundEnergyDiagnostics_ResetTotalEnergyUsage), METH_VARARGS | METH_STATIC, nullptr },
        { "get_device_specific_conversion_factor", reinterpret_cast<PyCFunction>(ForegroundEnergyDiagnostics_get_DeviceSpecificConversionFactor), METH_NOARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ForegroundEnergyDiagnostics[] = {
        { }
    };

    static PyType_Slot _type_slots_ForegroundEnergyDiagnostics[] = 
    {
        { Py_tp_new, _new_ForegroundEnergyDiagnostics },
        { Py_tp_methods, _methods_ForegroundEnergyDiagnostics },
        { Py_tp_getset, _getset_ForegroundEnergyDiagnostics },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_ForegroundEnergyDiagnostics =
    {
        "_winsdk_Windows_System_Power_Diagnostics.ForegroundEnergyDiagnostics",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ForegroundEnergyDiagnostics
    };

    // ----- Windows.System.Power.Diagnostics Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::System::Power::Diagnostics::BackgroundEnergyDiagnostics>::python_type = py::register_python_type(module, _type_name_BackgroundEnergyDiagnostics, &_type_spec_BackgroundEnergyDiagnostics, nullptr);
            py::winrt_type<winrt::Windows::System::Power::Diagnostics::ForegroundEnergyDiagnostics>::python_type = py::register_python_type(module, _type_name_ForegroundEnergyDiagnostics, &_type_spec_ForegroundEnergyDiagnostics, nullptr);

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.System.Power.Diagnostics");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_System_Power_Diagnostics",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::System::Power::Diagnostics

PyMODINIT_FUNC
PyInit__winsdk_Windows_System_Power_Diagnostics (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::System::Power::Diagnostics::module_def);
}
