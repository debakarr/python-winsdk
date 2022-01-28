// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Globalization.DateTimeFormatting.h"

PyTypeObject* py::winrt_type<winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter>::python_type;

namespace py::cpp::Windows::Globalization::DateTimeFormatting
{
    // ----- DateTimeFormatter class --------------------
    constexpr const char* const _type_name_DateTimeFormatter = "DateTimeFormatter";

    static PyObject* _new_DateTimeFormatter(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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

                winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter instance{ param0 };
                return py::wrap(instance, type);
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
                auto param1 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::hstring>>(args, 1);

                winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter instance{ param0, param1 };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 5)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::hstring>>(args, 1);
                auto param2 = py::convert_to<winrt::hstring>(args, 2);
                auto param3 = py::convert_to<winrt::hstring>(args, 3);
                auto param4 = py::convert_to<winrt::hstring>(args, 4);

                winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter instance{ param0, param1, param2, param3, param4 };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 4)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::YearFormat>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::MonthFormat>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::DayFormat>(args, 2);
                auto param3 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::DayOfWeekFormat>(args, 3);

                winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter instance{ param0, param1, param2, param3 };
                return py::wrap(instance, type);
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
                auto param0 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::HourFormat>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::MinuteFormat>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::SecondFormat>(args, 2);

                winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter instance{ param0, param1, param2 };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 8)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::YearFormat>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::MonthFormat>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::DayFormat>(args, 2);
                auto param3 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::DayOfWeekFormat>(args, 3);
                auto param4 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::HourFormat>(args, 4);
                auto param5 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::MinuteFormat>(args, 5);
                auto param6 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::SecondFormat>(args, 6);
                auto param7 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::hstring>>(args, 7);

                winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter instance{ param0, param1, param2, param3, param4, param5, param6, param7 };
                return py::wrap(instance, type);
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else if (arg_count == 11)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::YearFormat>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::MonthFormat>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::DayFormat>(args, 2);
                auto param3 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::DayOfWeekFormat>(args, 3);
                auto param4 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::HourFormat>(args, 4);
                auto param5 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::MinuteFormat>(args, 5);
                auto param6 = py::convert_to<winrt::Windows::Globalization::DateTimeFormatting::SecondFormat>(args, 6);
                auto param7 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::hstring>>(args, 7);
                auto param8 = py::convert_to<winrt::hstring>(args, 8);
                auto param9 = py::convert_to<winrt::hstring>(args, 9);
                auto param10 = py::convert_to<winrt::hstring>(args, 10);

                winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter instance{ param0, param1, param2, param3, param4, param5, param6, param7, param8, param9, param10 };
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

    static void _dealloc_DateTimeFormatter(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* DateTimeFormatter_Format(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::DateTime>(args, 0);

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
                auto param0 = py::convert_to<winrt::Windows::Foundation::DateTime>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);

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

    static PyObject* DateTimeFormatter_get_NumeralSystem(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.NumeralSystem());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int DateTimeFormatter_put_NumeralSystem(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::hstring>(arg);

            self->obj.NumeralSystem(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* DateTimeFormatter_get_Clock(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Clock());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_GeographicRegion(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.GeographicRegion());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_IncludeDay(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeDay());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_IncludeDayOfWeek(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeDayOfWeek());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_IncludeHour(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeHour());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_IncludeMinute(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeMinute());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_IncludeMonth(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeMonth());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_IncludeSecond(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeSecond());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_IncludeYear(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeYear());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_Languages(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Languages());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_Calendar(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Calendar());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_Patterns(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Patterns());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_ResolvedGeographicRegion(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ResolvedGeographicRegion());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_ResolvedLanguage(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ResolvedLanguage());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_Template(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Template());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_LongDate(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter::LongDate());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_LongTime(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter::LongTime());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_ShortDate(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter::ShortDate());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* DateTimeFormatter_get_ShortTime(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter::ShortTime());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_DateTimeFormatter(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_DateTimeFormatter[] = {
        { "format", reinterpret_cast<PyCFunction>(DateTimeFormatter_Format), METH_VARARGS, nullptr },
        { "get_long_date", reinterpret_cast<PyCFunction>(DateTimeFormatter_get_LongDate), METH_NOARGS | METH_STATIC, nullptr },
        { "get_long_time", reinterpret_cast<PyCFunction>(DateTimeFormatter_get_LongTime), METH_NOARGS | METH_STATIC, nullptr },
        { "get_short_date", reinterpret_cast<PyCFunction>(DateTimeFormatter_get_ShortDate), METH_NOARGS | METH_STATIC, nullptr },
        { "get_short_time", reinterpret_cast<PyCFunction>(DateTimeFormatter_get_ShortTime), METH_NOARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_DateTimeFormatter), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_DateTimeFormatter[] = {
        { "numeral_system", reinterpret_cast<getter>(DateTimeFormatter_get_NumeralSystem), reinterpret_cast<setter>(DateTimeFormatter_put_NumeralSystem), nullptr, nullptr },
        { "clock", reinterpret_cast<getter>(DateTimeFormatter_get_Clock), nullptr, nullptr, nullptr },
        { "geographic_region", reinterpret_cast<getter>(DateTimeFormatter_get_GeographicRegion), nullptr, nullptr, nullptr },
        { "include_day", reinterpret_cast<getter>(DateTimeFormatter_get_IncludeDay), nullptr, nullptr, nullptr },
        { "include_day_of_week", reinterpret_cast<getter>(DateTimeFormatter_get_IncludeDayOfWeek), nullptr, nullptr, nullptr },
        { "include_hour", reinterpret_cast<getter>(DateTimeFormatter_get_IncludeHour), nullptr, nullptr, nullptr },
        { "include_minute", reinterpret_cast<getter>(DateTimeFormatter_get_IncludeMinute), nullptr, nullptr, nullptr },
        { "include_month", reinterpret_cast<getter>(DateTimeFormatter_get_IncludeMonth), nullptr, nullptr, nullptr },
        { "include_second", reinterpret_cast<getter>(DateTimeFormatter_get_IncludeSecond), nullptr, nullptr, nullptr },
        { "include_year", reinterpret_cast<getter>(DateTimeFormatter_get_IncludeYear), nullptr, nullptr, nullptr },
        { "languages", reinterpret_cast<getter>(DateTimeFormatter_get_Languages), nullptr, nullptr, nullptr },
        { "calendar", reinterpret_cast<getter>(DateTimeFormatter_get_Calendar), nullptr, nullptr, nullptr },
        { "patterns", reinterpret_cast<getter>(DateTimeFormatter_get_Patterns), nullptr, nullptr, nullptr },
        { "resolved_geographic_region", reinterpret_cast<getter>(DateTimeFormatter_get_ResolvedGeographicRegion), nullptr, nullptr, nullptr },
        { "resolved_language", reinterpret_cast<getter>(DateTimeFormatter_get_ResolvedLanguage), nullptr, nullptr, nullptr },
        { "template", reinterpret_cast<getter>(DateTimeFormatter_get_Template), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_DateTimeFormatter[] = 
    {
        { Py_tp_new, _new_DateTimeFormatter },
        { Py_tp_dealloc, _dealloc_DateTimeFormatter },
        { Py_tp_methods, _methods_DateTimeFormatter },
        { Py_tp_getset, _getset_DateTimeFormatter },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_DateTimeFormatter =
    {
        "_winsdk_Windows_Globalization_DateTimeFormatting.DateTimeFormatter",
        sizeof(py::wrapper::Windows::Globalization::DateTimeFormatting::DateTimeFormatter),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_DateTimeFormatter
    };

    // ----- Windows.Globalization.DateTimeFormatting Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Globalization::DateTimeFormatting::DateTimeFormatter>::python_type = py::register_python_type(module, _type_name_DateTimeFormatter, &_type_spec_DateTimeFormatter, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Globalization.DateTimeFormatting");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Globalization_DateTimeFormatting",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Globalization::DateTimeFormatting

PyMODINIT_FUNC
PyInit__winsdk_Windows_Globalization_DateTimeFormatting (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Globalization::DateTimeFormatting::module_def);
}
