// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#include "pybase.h"
#include "py.Windows.Perception.Spatial.Surfaces.h"

PyTypeObject* py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver>::python_type;

namespace py::cpp::Windows::Perception::Spatial::Surfaces
{
    // ----- SpatialSurfaceInfo class --------------------
    constexpr const char* const _type_name_SpatialSurfaceInfo = "SpatialSurfaceInfo";

    static PyObject* _new_SpatialSurfaceInfo(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_SpatialSurfaceInfo);
        return nullptr;
    }

    static void _dealloc_SpatialSurfaceInfo(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpatialSurfaceInfo_TryComputeLatestMeshAsync(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<double>(args, 0);

                return py::convert(self->obj.TryComputeLatestMeshAsync(param0));
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
                auto param0 = py::convert_to<double>(args, 0);
                auto param1 = py::convert_to<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions>(args, 1);

                return py::convert(self->obj.TryComputeLatestMeshAsync(param0, param1));
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

    static PyObject* SpatialSurfaceInfo_TryGetBounds(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Perception::Spatial::SpatialCoordinateSystem>(args, 0);

                return py::convert(self->obj.TryGetBounds(param0));
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

    static PyObject* SpatialSurfaceInfo_get_Id(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Id());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceInfo_get_UpdateTime(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.UpdateTime());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_SpatialSurfaceInfo(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_SpatialSurfaceInfo[] = {
        { "try_compute_latest_mesh_async", reinterpret_cast<PyCFunction>(SpatialSurfaceInfo_TryComputeLatestMeshAsync), METH_VARARGS, nullptr },
        { "try_get_bounds", reinterpret_cast<PyCFunction>(SpatialSurfaceInfo_TryGetBounds), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_SpatialSurfaceInfo), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpatialSurfaceInfo[] = {
        { "id", reinterpret_cast<getter>(SpatialSurfaceInfo_get_Id), nullptr, nullptr, nullptr },
        { "update_time", reinterpret_cast<getter>(SpatialSurfaceInfo_get_UpdateTime), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SpatialSurfaceInfo[] = 
    {
        { Py_tp_new, _new_SpatialSurfaceInfo },
        { Py_tp_dealloc, _dealloc_SpatialSurfaceInfo },
        { Py_tp_methods, _methods_SpatialSurfaceInfo },
        { Py_tp_getset, _getset_SpatialSurfaceInfo },
        { },
    };

    static PyType_Spec _type_spec_SpatialSurfaceInfo =
    {
        "_winsdk_Windows_Perception_Spatial_Surfaces.SpatialSurfaceInfo",
        sizeof(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpatialSurfaceInfo
    };

    // ----- SpatialSurfaceMesh class --------------------
    constexpr const char* const _type_name_SpatialSurfaceMesh = "SpatialSurfaceMesh";

    static PyObject* _new_SpatialSurfaceMesh(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_SpatialSurfaceMesh);
        return nullptr;
    }

    static void _dealloc_SpatialSurfaceMesh(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpatialSurfaceMesh_get_CoordinateSystem(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CoordinateSystem());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMesh_get_SurfaceInfo(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.SurfaceInfo());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMesh_get_TriangleIndices(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TriangleIndices());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMesh_get_VertexNormals(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.VertexNormals());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMesh_get_VertexPositionScale(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.VertexPositionScale());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMesh_get_VertexPositions(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.VertexPositions());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_SpatialSurfaceMesh(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_SpatialSurfaceMesh[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_SpatialSurfaceMesh), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpatialSurfaceMesh[] = {
        { "coordinate_system", reinterpret_cast<getter>(SpatialSurfaceMesh_get_CoordinateSystem), nullptr, nullptr, nullptr },
        { "surface_info", reinterpret_cast<getter>(SpatialSurfaceMesh_get_SurfaceInfo), nullptr, nullptr, nullptr },
        { "triangle_indices", reinterpret_cast<getter>(SpatialSurfaceMesh_get_TriangleIndices), nullptr, nullptr, nullptr },
        { "vertex_normals", reinterpret_cast<getter>(SpatialSurfaceMesh_get_VertexNormals), nullptr, nullptr, nullptr },
        { "vertex_position_scale", reinterpret_cast<getter>(SpatialSurfaceMesh_get_VertexPositionScale), nullptr, nullptr, nullptr },
        { "vertex_positions", reinterpret_cast<getter>(SpatialSurfaceMesh_get_VertexPositions), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SpatialSurfaceMesh[] = 
    {
        { Py_tp_new, _new_SpatialSurfaceMesh },
        { Py_tp_dealloc, _dealloc_SpatialSurfaceMesh },
        { Py_tp_methods, _methods_SpatialSurfaceMesh },
        { Py_tp_getset, _getset_SpatialSurfaceMesh },
        { },
    };

    static PyType_Spec _type_spec_SpatialSurfaceMesh =
    {
        "_winsdk_Windows_Perception_Spatial_Surfaces.SpatialSurfaceMesh",
        sizeof(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpatialSurfaceMesh
    };

    // ----- SpatialSurfaceMeshBuffer class --------------------
    constexpr const char* const _type_name_SpatialSurfaceMeshBuffer = "SpatialSurfaceMeshBuffer";

    static PyObject* _new_SpatialSurfaceMeshBuffer(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_SpatialSurfaceMeshBuffer);
        return nullptr;
    }

    static void _dealloc_SpatialSurfaceMeshBuffer(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpatialSurfaceMeshBuffer_get_Data(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Data());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMeshBuffer_get_ElementCount(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ElementCount());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMeshBuffer_get_Format(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Format());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMeshBuffer_get_Stride(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Stride());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_SpatialSurfaceMeshBuffer(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_SpatialSurfaceMeshBuffer[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_SpatialSurfaceMeshBuffer), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpatialSurfaceMeshBuffer[] = {
        { "data", reinterpret_cast<getter>(SpatialSurfaceMeshBuffer_get_Data), nullptr, nullptr, nullptr },
        { "element_count", reinterpret_cast<getter>(SpatialSurfaceMeshBuffer_get_ElementCount), nullptr, nullptr, nullptr },
        { "format", reinterpret_cast<getter>(SpatialSurfaceMeshBuffer_get_Format), nullptr, nullptr, nullptr },
        { "stride", reinterpret_cast<getter>(SpatialSurfaceMeshBuffer_get_Stride), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SpatialSurfaceMeshBuffer[] = 
    {
        { Py_tp_new, _new_SpatialSurfaceMeshBuffer },
        { Py_tp_dealloc, _dealloc_SpatialSurfaceMeshBuffer },
        { Py_tp_methods, _methods_SpatialSurfaceMeshBuffer },
        { Py_tp_getset, _getset_SpatialSurfaceMeshBuffer },
        { },
    };

    static PyType_Spec _type_spec_SpatialSurfaceMeshBuffer =
    {
        "_winsdk_Windows_Perception_Spatial_Surfaces.SpatialSurfaceMeshBuffer",
        sizeof(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpatialSurfaceMeshBuffer
    };

    // ----- SpatialSurfaceMeshOptions class --------------------
    constexpr const char* const _type_name_SpatialSurfaceMeshOptions = "SpatialSurfaceMeshOptions";

    static PyObject* _new_SpatialSurfaceMeshOptions(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions instance{  };
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

    static void _dealloc_SpatialSurfaceMeshOptions(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpatialSurfaceMeshOptions_get_VertexPositionFormat(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.VertexPositionFormat());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpatialSurfaceMeshOptions_put_VertexPositionFormat(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Graphics::DirectX::DirectXPixelFormat>(arg);

            self->obj.VertexPositionFormat(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpatialSurfaceMeshOptions_get_VertexNormalFormat(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.VertexNormalFormat());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpatialSurfaceMeshOptions_put_VertexNormalFormat(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Graphics::DirectX::DirectXPixelFormat>(arg);

            self->obj.VertexNormalFormat(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpatialSurfaceMeshOptions_get_TriangleIndexFormat(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TriangleIndexFormat());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpatialSurfaceMeshOptions_put_TriangleIndexFormat(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Graphics::DirectX::DirectXPixelFormat>(arg);

            self->obj.TriangleIndexFormat(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpatialSurfaceMeshOptions_get_IncludeVertexNormals(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeVertexNormals());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpatialSurfaceMeshOptions_put_IncludeVertexNormals(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.IncludeVertexNormals(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpatialSurfaceMeshOptions_get_SupportedTriangleIndexFormats(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions::SupportedTriangleIndexFormats());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMeshOptions_get_SupportedVertexNormalFormats(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions::SupportedVertexNormalFormats());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceMeshOptions_get_SupportedVertexPositionFormats(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions::SupportedVertexPositionFormats());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_SpatialSurfaceMeshOptions(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_SpatialSurfaceMeshOptions[] = {
        { "get_supported_triangle_index_formats", reinterpret_cast<PyCFunction>(SpatialSurfaceMeshOptions_get_SupportedTriangleIndexFormats), METH_NOARGS | METH_STATIC, nullptr },
        { "get_supported_vertex_normal_formats", reinterpret_cast<PyCFunction>(SpatialSurfaceMeshOptions_get_SupportedVertexNormalFormats), METH_NOARGS | METH_STATIC, nullptr },
        { "get_supported_vertex_position_formats", reinterpret_cast<PyCFunction>(SpatialSurfaceMeshOptions_get_SupportedVertexPositionFormats), METH_NOARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_SpatialSurfaceMeshOptions), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpatialSurfaceMeshOptions[] = {
        { "vertex_position_format", reinterpret_cast<getter>(SpatialSurfaceMeshOptions_get_VertexPositionFormat), reinterpret_cast<setter>(SpatialSurfaceMeshOptions_put_VertexPositionFormat), nullptr, nullptr },
        { "vertex_normal_format", reinterpret_cast<getter>(SpatialSurfaceMeshOptions_get_VertexNormalFormat), reinterpret_cast<setter>(SpatialSurfaceMeshOptions_put_VertexNormalFormat), nullptr, nullptr },
        { "triangle_index_format", reinterpret_cast<getter>(SpatialSurfaceMeshOptions_get_TriangleIndexFormat), reinterpret_cast<setter>(SpatialSurfaceMeshOptions_put_TriangleIndexFormat), nullptr, nullptr },
        { "include_vertex_normals", reinterpret_cast<getter>(SpatialSurfaceMeshOptions_get_IncludeVertexNormals), reinterpret_cast<setter>(SpatialSurfaceMeshOptions_put_IncludeVertexNormals), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SpatialSurfaceMeshOptions[] = 
    {
        { Py_tp_new, _new_SpatialSurfaceMeshOptions },
        { Py_tp_dealloc, _dealloc_SpatialSurfaceMeshOptions },
        { Py_tp_methods, _methods_SpatialSurfaceMeshOptions },
        { Py_tp_getset, _getset_SpatialSurfaceMeshOptions },
        { },
    };

    static PyType_Spec _type_spec_SpatialSurfaceMeshOptions =
    {
        "_winsdk_Windows_Perception_Spatial_Surfaces.SpatialSurfaceMeshOptions",
        sizeof(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpatialSurfaceMeshOptions
    };

    // ----- SpatialSurfaceObserver class --------------------
    constexpr const char* const _type_name_SpatialSurfaceObserver = "SpatialSurfaceObserver";

    static PyObject* _new_SpatialSurfaceObserver(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver instance{  };
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

    static void _dealloc_SpatialSurfaceObserver(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpatialSurfaceObserver_GetObservedSurfaces(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.GetObservedSurfaces());
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

    static PyObject* SpatialSurfaceObserver_IsSupported(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver::IsSupported());
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

    static PyObject* SpatialSurfaceObserver_RequestAccessAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver::RequestAccessAsync());
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

    static PyObject* SpatialSurfaceObserver_SetBoundingVolume(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Perception::Spatial::SpatialBoundingVolume>(args, 0);

                self->obj.SetBoundingVolume(param0);
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

    static PyObject* SpatialSurfaceObserver_SetBoundingVolumes(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Foundation::Collections::IIterable<winrt::Windows::Perception::Spatial::SpatialBoundingVolume>>(args, 0);

                self->obj.SetBoundingVolumes(param0);
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

    static PyObject* SpatialSurfaceObserver_add_ObservedSurfacesChanged(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver, winrt::Windows::Foundation::IInspectable>>(arg);

            return py::convert(self->obj.ObservedSurfacesChanged(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpatialSurfaceObserver_remove_ObservedSurfacesChanged(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver* self, PyObject* arg) noexcept
    {
        try
        {
            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.ObservedSurfacesChanged(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_SpatialSurfaceObserver(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_SpatialSurfaceObserver[] = {
        { "get_observed_surfaces", reinterpret_cast<PyCFunction>(SpatialSurfaceObserver_GetObservedSurfaces), METH_VARARGS, nullptr },
        { "is_supported", reinterpret_cast<PyCFunction>(SpatialSurfaceObserver_IsSupported), METH_VARARGS | METH_STATIC, nullptr },
        { "request_access_async", reinterpret_cast<PyCFunction>(SpatialSurfaceObserver_RequestAccessAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "set_bounding_volume", reinterpret_cast<PyCFunction>(SpatialSurfaceObserver_SetBoundingVolume), METH_VARARGS, nullptr },
        { "set_bounding_volumes", reinterpret_cast<PyCFunction>(SpatialSurfaceObserver_SetBoundingVolumes), METH_VARARGS, nullptr },
        { "add_observed_surfaces_changed", reinterpret_cast<PyCFunction>(SpatialSurfaceObserver_add_ObservedSurfacesChanged), METH_O, nullptr },
        { "remove_observed_surfaces_changed", reinterpret_cast<PyCFunction>(SpatialSurfaceObserver_remove_ObservedSurfacesChanged), METH_O, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_SpatialSurfaceObserver), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpatialSurfaceObserver[] = {
        { }
    };

    static PyType_Slot _type_slots_SpatialSurfaceObserver[] = 
    {
        { Py_tp_new, _new_SpatialSurfaceObserver },
        { Py_tp_dealloc, _dealloc_SpatialSurfaceObserver },
        { Py_tp_methods, _methods_SpatialSurfaceObserver },
        { Py_tp_getset, _getset_SpatialSurfaceObserver },
        { },
    };

    static PyType_Spec _type_spec_SpatialSurfaceObserver =
    {
        "_winsdk_Windows_Perception_Spatial_Surfaces.SpatialSurfaceObserver",
        sizeof(py::wrapper::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpatialSurfaceObserver
    };

    // ----- Windows.Perception.Spatial.Surfaces Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceInfo>::python_type = py::register_python_type(module, _type_name_SpatialSurfaceInfo, &_type_spec_SpatialSurfaceInfo, bases.get());
            py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMesh>::python_type = py::register_python_type(module, _type_name_SpatialSurfaceMesh, &_type_spec_SpatialSurfaceMesh, bases.get());
            py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshBuffer>::python_type = py::register_python_type(module, _type_name_SpatialSurfaceMeshBuffer, &_type_spec_SpatialSurfaceMeshBuffer, bases.get());
            py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceMeshOptions>::python_type = py::register_python_type(module, _type_name_SpatialSurfaceMeshOptions, &_type_spec_SpatialSurfaceMeshOptions, bases.get());
            py::winrt_type<winrt::Windows::Perception::Spatial::Surfaces::SpatialSurfaceObserver>::python_type = py::register_python_type(module, _type_name_SpatialSurfaceObserver, &_type_spec_SpatialSurfaceObserver, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Perception.Spatial.Surfaces");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Perception_Spatial_Surfaces",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Perception::Spatial::Surfaces

PyMODINIT_FUNC
PyInit__winsdk_Windows_Perception_Spatial_Surfaces (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Perception::Spatial::Surfaces::module_def);
}
