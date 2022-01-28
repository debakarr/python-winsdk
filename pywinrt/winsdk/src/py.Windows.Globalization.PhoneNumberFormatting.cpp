// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Globalization.PhoneNumberFormatting.h"

PyTypeObject* py::winrt_type<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo>::python_type;

namespace py::cpp::Windows::Globalization::PhoneNumberFormatting
{
    // ----- PhoneNumberFormatter class --------------------
    constexpr const char* const _type_name_PhoneNumberFormatter = "PhoneNumberFormatter";

    static PyObject* _new_PhoneNumberFormatter(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter instance{  };
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

    static void _dealloc_PhoneNumberFormatter(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PhoneNumberFormatter_Format(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo>(args, 0);

                return py::convert(self->obj.Format(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormat>(args, 1);

                return py::convert(self->obj.Format(param0, param1));
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

    static PyObject* PhoneNumberFormatter_FormatPartialString(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.FormatPartialString(param0));
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

    static PyObject* PhoneNumberFormatter_FormatString(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.FormatString(param0));
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

    static PyObject* PhoneNumberFormatter_FormatStringWithLeftToRightMarkers(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.FormatStringWithLeftToRightMarkers(param0));
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

    static PyObject* PhoneNumberFormatter_GetCountryCodeForRegion(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter::GetCountryCodeForRegion(param0));
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

    static PyObject* PhoneNumberFormatter_GetNationalDirectDialingPrefixForRegion(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<bool>(args, 1);

                return py::convert(winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter::GetNationalDirectDialingPrefixForRegion(param0, param1));
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

    static PyObject* PhoneNumberFormatter_TryCreate(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter param1 { nullptr };

                winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter::TryCreate(param0, param1);

                py::pyobj_handle out1{ py::convert(param1) };
                if (!out1)
                {
                    return nullptr;
                }
                return out1.detach();
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

    static PyObject* PhoneNumberFormatter_WrapWithLeftToRightMarkers(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter::WrapWithLeftToRightMarkers(param0));
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

    static PyObject* _from_PhoneNumberFormatter(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PhoneNumberFormatter[] = {
        { "format", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_Format), METH_VARARGS, nullptr },
        { "format_partial_string", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_FormatPartialString), METH_VARARGS, nullptr },
        { "format_string", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_FormatString), METH_VARARGS, nullptr },
        { "format_string_with_left_to_right_markers", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_FormatStringWithLeftToRightMarkers), METH_VARARGS, nullptr },
        { "get_country_code_for_region", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_GetCountryCodeForRegion), METH_VARARGS | METH_STATIC, nullptr },
        { "get_national_direct_dialing_prefix_for_region", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_GetNationalDirectDialingPrefixForRegion), METH_VARARGS | METH_STATIC, nullptr },
        { "try_create", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_TryCreate), METH_VARARGS | METH_STATIC, nullptr },
        { "wrap_with_left_to_right_markers", reinterpret_cast<PyCFunction>(PhoneNumberFormatter_WrapWithLeftToRightMarkers), METH_VARARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_PhoneNumberFormatter), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PhoneNumberFormatter[] = {
        { }
    };

    static PyType_Slot _type_slots_PhoneNumberFormatter[] = 
    {
        { Py_tp_new, _new_PhoneNumberFormatter },
        { Py_tp_dealloc, _dealloc_PhoneNumberFormatter },
        { Py_tp_methods, _methods_PhoneNumberFormatter },
        { Py_tp_getset, _getset_PhoneNumberFormatter },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_PhoneNumberFormatter =
    {
        "_winsdk_Windows_Globalization_PhoneNumberFormatting.PhoneNumberFormatter",
        sizeof(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PhoneNumberFormatter
    };

    // ----- PhoneNumberInfo class --------------------
    constexpr const char* const _type_name_PhoneNumberInfo = "PhoneNumberInfo";

    static PyObject* _new_PhoneNumberInfo(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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

                winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo instance{ param0 };
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

    static void _dealloc_PhoneNumberInfo(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* PhoneNumberInfo_CheckNumberMatch(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo>(args, 0);

                return py::convert(self->obj.CheckNumberMatch(param0));
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

    static PyObject* PhoneNumberInfo_GetGeographicRegionCode(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetGeographicRegionCode());
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

    static PyObject* PhoneNumberInfo_GetLengthOfGeographicalAreaCode(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetLengthOfGeographicalAreaCode());
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

    static PyObject* PhoneNumberInfo_GetLengthOfNationalDestinationCode(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetLengthOfNationalDestinationCode());
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

    static PyObject* PhoneNumberInfo_GetNationalSignificantNumber(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetNationalSignificantNumber());
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

    static PyObject* PhoneNumberInfo_PredictNumberKind(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.PredictNumberKind());
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

    static PyObject* PhoneNumberInfo_ToString(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.ToString());
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

    static PyObject* PhoneNumberInfo_TryParse(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo param1 { nullptr };

                auto return_value = winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo::TryParse(param0, param1);

                py::pyobj_handle out_return_value{ py::convert(return_value) };
                if (!out_return_value)
                {
                    return nullptr;
                }
                py::pyobj_handle out1{ py::convert(param1) };
                if (!out1)
                {
                    return nullptr;
                }
                return PyTuple_Pack(2, out_return_value.get(), out1.get());
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 2)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);
                winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo param2 { nullptr };

                auto return_value = winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo::TryParse(param0, param1, param2);

                py::pyobj_handle out_return_value{ py::convert(return_value) };
                if (!out_return_value)
                {
                    return nullptr;
                }
                py::pyobj_handle out2{ py::convert(param2) };
                if (!out2)
                {
                    return nullptr;
                }
                return PyTuple_Pack(2, out_return_value.get(), out2.get());
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

    static PyObject* PhoneNumberInfo_get_CountryCode(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CountryCode());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* PhoneNumberInfo_get_PhoneNumber(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.PhoneNumber());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_PhoneNumberInfo(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _str_PhoneNumberInfo(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo* self) noexcept
    {
        try
        {
            return py::convert(self->obj.ToString());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_PhoneNumberInfo[] = {
        { "check_number_match", reinterpret_cast<PyCFunction>(PhoneNumberInfo_CheckNumberMatch), METH_VARARGS, nullptr },
        { "get_geographic_region_code", reinterpret_cast<PyCFunction>(PhoneNumberInfo_GetGeographicRegionCode), METH_VARARGS, nullptr },
        { "get_length_of_geographical_area_code", reinterpret_cast<PyCFunction>(PhoneNumberInfo_GetLengthOfGeographicalAreaCode), METH_VARARGS, nullptr },
        { "get_length_of_national_destination_code", reinterpret_cast<PyCFunction>(PhoneNumberInfo_GetLengthOfNationalDestinationCode), METH_VARARGS, nullptr },
        { "get_national_significant_number", reinterpret_cast<PyCFunction>(PhoneNumberInfo_GetNationalSignificantNumber), METH_VARARGS, nullptr },
        { "predict_number_kind", reinterpret_cast<PyCFunction>(PhoneNumberInfo_PredictNumberKind), METH_VARARGS, nullptr },
        { "to_string", reinterpret_cast<PyCFunction>(PhoneNumberInfo_ToString), METH_VARARGS, nullptr },
        { "try_parse", reinterpret_cast<PyCFunction>(PhoneNumberInfo_TryParse), METH_VARARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_PhoneNumberInfo), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PhoneNumberInfo[] = {
        { "country_code", reinterpret_cast<getter>(PhoneNumberInfo_get_CountryCode), nullptr, nullptr, nullptr },
        { "phone_number", reinterpret_cast<getter>(PhoneNumberInfo_get_PhoneNumber), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PhoneNumberInfo[] = 
    {
        { Py_tp_new, _new_PhoneNumberInfo },
        { Py_tp_dealloc, _dealloc_PhoneNumberInfo },
        { Py_tp_methods, _methods_PhoneNumberInfo },
        { Py_tp_getset, _getset_PhoneNumberInfo },
        { Py_tp_str, _str_PhoneNumberInfo },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_PhoneNumberInfo =
    {
        "_winsdk_Windows_Globalization_PhoneNumberFormatting.PhoneNumberInfo",
        sizeof(py::wrapper::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PhoneNumberInfo
    };

    // ----- Windows.Globalization.PhoneNumberFormatting Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberFormatter>::python_type = py::register_python_type(module, _type_name_PhoneNumberFormatter, &_type_spec_PhoneNumberFormatter, bases.get());
            py::winrt_type<winrt::Windows::Globalization::PhoneNumberFormatting::PhoneNumberInfo>::python_type = py::register_python_type(module, _type_name_PhoneNumberInfo, &_type_spec_PhoneNumberInfo, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Globalization.PhoneNumberFormatting");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Globalization_PhoneNumberFormatting",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Globalization::PhoneNumberFormatting

PyMODINIT_FUNC
PyInit__winsdk_Windows_Globalization_PhoneNumberFormatting (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Globalization::PhoneNumberFormatting::module_def);
}
