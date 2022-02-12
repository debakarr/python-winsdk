// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#include "pybase.h"
#include "py.Windows.Services.Maps.LocalSearch.h"

PyTypeObject* py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalCategories>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocation>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationFinder>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationFinderResult>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::PlaceInfoHelper>::python_type;

namespace py::cpp::Windows::Services::Maps::LocalSearch
{
    // ----- LocalCategories class --------------------
    constexpr const char* const _type_name_LocalCategories = "LocalCategories";

    static PyObject* _new_LocalCategories(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_LocalCategories);
        return nullptr;
    }

    static PyObject* LocalCategories_get_All(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::All());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalCategories_get_BankAndCreditUnions(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::BankAndCreditUnions());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalCategories_get_EatDrink(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::EatDrink());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalCategories_get_Hospitals(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::Hospitals());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalCategories_get_HotelsAndMotels(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::HotelsAndMotels());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalCategories_get_Parking(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::Parking());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalCategories_get_SeeDo(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::SeeDo());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalCategories_get_Shop(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalCategories::Shop());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_LocalCategories[] = {
        { "get_all", reinterpret_cast<PyCFunction>(LocalCategories_get_All), METH_NOARGS | METH_STATIC, nullptr },
        { "get_bank_and_credit_unions", reinterpret_cast<PyCFunction>(LocalCategories_get_BankAndCreditUnions), METH_NOARGS | METH_STATIC, nullptr },
        { "get_eat_drink", reinterpret_cast<PyCFunction>(LocalCategories_get_EatDrink), METH_NOARGS | METH_STATIC, nullptr },
        { "get_hospitals", reinterpret_cast<PyCFunction>(LocalCategories_get_Hospitals), METH_NOARGS | METH_STATIC, nullptr },
        { "get_hotels_and_motels", reinterpret_cast<PyCFunction>(LocalCategories_get_HotelsAndMotels), METH_NOARGS | METH_STATIC, nullptr },
        { "get_parking", reinterpret_cast<PyCFunction>(LocalCategories_get_Parking), METH_NOARGS | METH_STATIC, nullptr },
        { "get_see_do", reinterpret_cast<PyCFunction>(LocalCategories_get_SeeDo), METH_NOARGS | METH_STATIC, nullptr },
        { "get_shop", reinterpret_cast<PyCFunction>(LocalCategories_get_Shop), METH_NOARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_LocalCategories[] = {
        { }
    };

    static PyType_Slot _type_slots_LocalCategories[] = 
    {
        { Py_tp_new, _new_LocalCategories },
        { Py_tp_methods, _methods_LocalCategories },
        { Py_tp_getset, _getset_LocalCategories },
        { },
    };

    static PyType_Spec _type_spec_LocalCategories =
    {
        "_winsdk_Windows_Services_Maps_LocalSearch.LocalCategories",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_LocalCategories
    };

    // ----- LocalLocation class --------------------
    constexpr const char* const _type_name_LocalLocation = "LocalLocation";

    static PyObject* _new_LocalLocation(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_LocalLocation);
        return nullptr;
    }

    static void _dealloc_LocalLocation(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* LocalLocation_get_Address(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Address());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocation_get_DataAttribution(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.DataAttribution());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocation_get_Description(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
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

    static PyObject* LocalLocation_get_DisplayName(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.DisplayName());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocation_get_Identifier(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Identifier());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocation_get_PhoneNumber(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
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

    static PyObject* LocalLocation_get_Point(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Point());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocation_get_Category(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Category());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocation_get_HoursOfOperation(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.HoursOfOperation());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocation_get_RatingInfo(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.RatingInfo());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_LocalLocation(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Services::Maps::LocalSearch::LocalLocation>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_LocalLocation[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_LocalLocation), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_LocalLocation[] = {
        { "address", reinterpret_cast<getter>(LocalLocation_get_Address), nullptr, nullptr, nullptr },
        { "data_attribution", reinterpret_cast<getter>(LocalLocation_get_DataAttribution), nullptr, nullptr, nullptr },
        { "description", reinterpret_cast<getter>(LocalLocation_get_Description), nullptr, nullptr, nullptr },
        { "display_name", reinterpret_cast<getter>(LocalLocation_get_DisplayName), nullptr, nullptr, nullptr },
        { "identifier", reinterpret_cast<getter>(LocalLocation_get_Identifier), nullptr, nullptr, nullptr },
        { "phone_number", reinterpret_cast<getter>(LocalLocation_get_PhoneNumber), nullptr, nullptr, nullptr },
        { "point", reinterpret_cast<getter>(LocalLocation_get_Point), nullptr, nullptr, nullptr },
        { "category", reinterpret_cast<getter>(LocalLocation_get_Category), nullptr, nullptr, nullptr },
        { "hours_of_operation", reinterpret_cast<getter>(LocalLocation_get_HoursOfOperation), nullptr, nullptr, nullptr },
        { "rating_info", reinterpret_cast<getter>(LocalLocation_get_RatingInfo), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_LocalLocation[] = 
    {
        { Py_tp_new, _new_LocalLocation },
        { Py_tp_dealloc, _dealloc_LocalLocation },
        { Py_tp_methods, _methods_LocalLocation },
        { Py_tp_getset, _getset_LocalLocation },
        { },
    };

    static PyType_Spec _type_spec_LocalLocation =
    {
        "_winsdk_Windows_Services_Maps_LocalSearch.LocalLocation",
        sizeof(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocation),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_LocalLocation
    };

    // ----- LocalLocationFinder class --------------------
    constexpr const char* const _type_name_LocalLocationFinder = "LocalLocationFinder";

    static PyObject* _new_LocalLocationFinder(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_LocalLocationFinder);
        return nullptr;
    }

    static PyObject* LocalLocationFinder_FindLocalLocationsAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 4)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Devices::Geolocation::Geocircle>(args, 1);
                auto param2 = py::convert_to<winrt::hstring>(args, 2);
                auto param3 = py::convert_to<uint32_t>(args, 3);

                return py::convert(winrt::Windows::Services::Maps::LocalSearch::LocalLocationFinder::FindLocalLocationsAsync(param0, param1, param2, param3));
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

    static PyMethodDef _methods_LocalLocationFinder[] = {
        { "find_local_locations_async", reinterpret_cast<PyCFunction>(LocalLocationFinder_FindLocalLocationsAsync), METH_VARARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_LocalLocationFinder[] = {
        { }
    };

    static PyType_Slot _type_slots_LocalLocationFinder[] = 
    {
        { Py_tp_new, _new_LocalLocationFinder },
        { Py_tp_methods, _methods_LocalLocationFinder },
        { Py_tp_getset, _getset_LocalLocationFinder },
        { },
    };

    static PyType_Spec _type_spec_LocalLocationFinder =
    {
        "_winsdk_Windows_Services_Maps_LocalSearch.LocalLocationFinder",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_LocalLocationFinder
    };

    // ----- LocalLocationFinderResult class --------------------
    constexpr const char* const _type_name_LocalLocationFinderResult = "LocalLocationFinderResult";

    static PyObject* _new_LocalLocationFinderResult(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_LocalLocationFinderResult);
        return nullptr;
    }

    static void _dealloc_LocalLocationFinderResult(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationFinderResult* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* LocalLocationFinderResult_get_LocalLocations(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationFinderResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.LocalLocations());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocationFinderResult_get_Status(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationFinderResult* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Status());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_LocalLocationFinderResult(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Services::Maps::LocalSearch::LocalLocationFinderResult>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_LocalLocationFinderResult[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_LocalLocationFinderResult), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_LocalLocationFinderResult[] = {
        { "local_locations", reinterpret_cast<getter>(LocalLocationFinderResult_get_LocalLocations), nullptr, nullptr, nullptr },
        { "status", reinterpret_cast<getter>(LocalLocationFinderResult_get_Status), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_LocalLocationFinderResult[] = 
    {
        { Py_tp_new, _new_LocalLocationFinderResult },
        { Py_tp_dealloc, _dealloc_LocalLocationFinderResult },
        { Py_tp_methods, _methods_LocalLocationFinderResult },
        { Py_tp_getset, _getset_LocalLocationFinderResult },
        { },
    };

    static PyType_Spec _type_spec_LocalLocationFinderResult =
    {
        "_winsdk_Windows_Services_Maps_LocalSearch.LocalLocationFinderResult",
        sizeof(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationFinderResult),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_LocalLocationFinderResult
    };

    // ----- LocalLocationHoursOfOperationItem class --------------------
    constexpr const char* const _type_name_LocalLocationHoursOfOperationItem = "LocalLocationHoursOfOperationItem";

    static PyObject* _new_LocalLocationHoursOfOperationItem(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_LocalLocationHoursOfOperationItem);
        return nullptr;
    }

    static void _dealloc_LocalLocationHoursOfOperationItem(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* LocalLocationHoursOfOperationItem_get_Day(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Day());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocationHoursOfOperationItem_get_Span(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Span());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocationHoursOfOperationItem_get_Start(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Start());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_LocalLocationHoursOfOperationItem(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_LocalLocationHoursOfOperationItem[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_LocalLocationHoursOfOperationItem), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_LocalLocationHoursOfOperationItem[] = {
        { "day", reinterpret_cast<getter>(LocalLocationHoursOfOperationItem_get_Day), nullptr, nullptr, nullptr },
        { "span", reinterpret_cast<getter>(LocalLocationHoursOfOperationItem_get_Span), nullptr, nullptr, nullptr },
        { "start", reinterpret_cast<getter>(LocalLocationHoursOfOperationItem_get_Start), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_LocalLocationHoursOfOperationItem[] = 
    {
        { Py_tp_new, _new_LocalLocationHoursOfOperationItem },
        { Py_tp_dealloc, _dealloc_LocalLocationHoursOfOperationItem },
        { Py_tp_methods, _methods_LocalLocationHoursOfOperationItem },
        { Py_tp_getset, _getset_LocalLocationHoursOfOperationItem },
        { },
    };

    static PyType_Spec _type_spec_LocalLocationHoursOfOperationItem =
    {
        "_winsdk_Windows_Services_Maps_LocalSearch.LocalLocationHoursOfOperationItem",
        sizeof(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_LocalLocationHoursOfOperationItem
    };

    // ----- LocalLocationRatingInfo class --------------------
    constexpr const char* const _type_name_LocalLocationRatingInfo = "LocalLocationRatingInfo";

    static PyObject* _new_LocalLocationRatingInfo(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_LocalLocationRatingInfo);
        return nullptr;
    }

    static void _dealloc_LocalLocationRatingInfo(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* LocalLocationRatingInfo_get_AggregateRating(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AggregateRating());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocationRatingInfo_get_ProviderIdentifier(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ProviderIdentifier());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* LocalLocationRatingInfo_get_RatingCount(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.RatingCount());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_LocalLocationRatingInfo(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_LocalLocationRatingInfo[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_LocalLocationRatingInfo), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_LocalLocationRatingInfo[] = {
        { "aggregate_rating", reinterpret_cast<getter>(LocalLocationRatingInfo_get_AggregateRating), nullptr, nullptr, nullptr },
        { "provider_identifier", reinterpret_cast<getter>(LocalLocationRatingInfo_get_ProviderIdentifier), nullptr, nullptr, nullptr },
        { "rating_count", reinterpret_cast<getter>(LocalLocationRatingInfo_get_RatingCount), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_LocalLocationRatingInfo[] = 
    {
        { Py_tp_new, _new_LocalLocationRatingInfo },
        { Py_tp_dealloc, _dealloc_LocalLocationRatingInfo },
        { Py_tp_methods, _methods_LocalLocationRatingInfo },
        { Py_tp_getset, _getset_LocalLocationRatingInfo },
        { },
    };

    static PyType_Spec _type_spec_LocalLocationRatingInfo =
    {
        "_winsdk_Windows_Services_Maps_LocalSearch.LocalLocationRatingInfo",
        sizeof(py::wrapper::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_LocalLocationRatingInfo
    };

    // ----- PlaceInfoHelper class --------------------
    constexpr const char* const _type_name_PlaceInfoHelper = "PlaceInfoHelper";

    static PyObject* _new_PlaceInfoHelper(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_PlaceInfoHelper);
        return nullptr;
    }

    static PyObject* PlaceInfoHelper_CreateFromLocalLocation(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Services::Maps::LocalSearch::LocalLocation>(args, 0);

                return py::convert(winrt::Windows::Services::Maps::LocalSearch::PlaceInfoHelper::CreateFromLocalLocation(param0));
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

    static PyMethodDef _methods_PlaceInfoHelper[] = {
        { "create_from_local_location", reinterpret_cast<PyCFunction>(PlaceInfoHelper_CreateFromLocalLocation), METH_VARARGS | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_PlaceInfoHelper[] = {
        { }
    };

    static PyType_Slot _type_slots_PlaceInfoHelper[] = 
    {
        { Py_tp_new, _new_PlaceInfoHelper },
        { Py_tp_methods, _methods_PlaceInfoHelper },
        { Py_tp_getset, _getset_PlaceInfoHelper },
        { },
    };

    static PyType_Spec _type_spec_PlaceInfoHelper =
    {
        "_winsdk_Windows_Services_Maps_LocalSearch.PlaceInfoHelper",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PlaceInfoHelper
    };

    // ----- Windows.Services.Maps.LocalSearch Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalCategories>::python_type = py::register_python_type(module, _type_name_LocalCategories, &_type_spec_LocalCategories, nullptr);
            py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocation>::python_type = py::register_python_type(module, _type_name_LocalLocation, &_type_spec_LocalLocation, bases.get());
            py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationFinder>::python_type = py::register_python_type(module, _type_name_LocalLocationFinder, &_type_spec_LocalLocationFinder, nullptr);
            py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationFinderResult>::python_type = py::register_python_type(module, _type_name_LocalLocationFinderResult, &_type_spec_LocalLocationFinderResult, bases.get());
            py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationHoursOfOperationItem>::python_type = py::register_python_type(module, _type_name_LocalLocationHoursOfOperationItem, &_type_spec_LocalLocationHoursOfOperationItem, bases.get());
            py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::LocalLocationRatingInfo>::python_type = py::register_python_type(module, _type_name_LocalLocationRatingInfo, &_type_spec_LocalLocationRatingInfo, bases.get());
            py::winrt_type<winrt::Windows::Services::Maps::LocalSearch::PlaceInfoHelper>::python_type = py::register_python_type(module, _type_name_PlaceInfoHelper, &_type_spec_PlaceInfoHelper, nullptr);

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Services.Maps.LocalSearch");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Services_Maps_LocalSearch",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Services::Maps::LocalSearch

PyMODINIT_FUNC
PyInit__winsdk_Windows_Services_Maps_LocalSearch (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Services::Maps::LocalSearch::module_def);
}
