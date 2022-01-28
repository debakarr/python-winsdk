// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#include "pybase.h"
#include "py.Windows.Media.SpeechSynthesis.h"

PyTypeObject* py::winrt_type<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesisStream>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizer>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions>::python_type;
PyTypeObject* py::winrt_type<winrt::Windows::Media::SpeechSynthesis::VoiceInformation>::python_type;

namespace py::cpp::Windows::Media::SpeechSynthesis
{
    // ----- SpeechSynthesisStream class --------------------
    constexpr const char* const _type_name_SpeechSynthesisStream = "SpeechSynthesisStream";

    static PyObject* _new_SpeechSynthesisStream(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_SpeechSynthesisStream);
        return nullptr;
    }

    static void _dealloc_SpeechSynthesisStream(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpeechSynthesisStream_CloneStream(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.CloneStream());
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

    static PyObject* SpeechSynthesisStream_Close(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
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

    static PyObject* SpeechSynthesisStream_FlushAsync(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 0)
        {
            try
            {
                return py::convert(self->obj.FlushAsync());
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

    static PyObject* SpeechSynthesisStream_GetInputStreamAt(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<uint64_t>(args, 0);

                return py::convert(self->obj.GetInputStreamAt(param0));
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

    static PyObject* SpeechSynthesisStream_GetOutputStreamAt(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<uint64_t>(args, 0);

                return py::convert(self->obj.GetOutputStreamAt(param0));
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

    static PyObject* SpeechSynthesisStream_ReadAsync(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 3)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);
                auto param1 = py::convert_to<uint32_t>(args, 1);
                auto param2 = py::convert_to<winrt::Windows::Storage::Streams::InputStreamOptions>(args, 2);

                return py::convert(self->obj.ReadAsync(param0, param1, param2));
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

    static PyObject* SpeechSynthesisStream_Seek(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<uint64_t>(args, 0);

                self->obj.Seek(param0);
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

    static PyObject* SpeechSynthesisStream_WriteAsync(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Storage::Streams::IBuffer>(args, 0);

                return py::convert(self->obj.WriteAsync(param0));
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

    static PyObject* SpeechSynthesisStream_get_TimedMetadataTracks(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.TimedMetadataTracks());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpeechSynthesisStream_get_Markers(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Markers());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpeechSynthesisStream_get_ContentType(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.ContentType());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpeechSynthesisStream_get_Size(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Size());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesisStream_put_Size(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<uint64_t>(arg);

            self->obj.Size(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesisStream_get_CanRead(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CanRead());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpeechSynthesisStream_get_CanWrite(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.CanWrite());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpeechSynthesisStream_get_Position(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Position());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_SpeechSynthesisStream(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesisStream>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_SpeechSynthesisStream(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_SpeechSynthesisStream(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream* self) noexcept
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

    static PyMethodDef _methods_SpeechSynthesisStream[] = {
        { "clone_stream", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_CloneStream), METH_VARARGS, nullptr },
        { "close", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_Close), METH_VARARGS, nullptr },
        { "flush_async", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_FlushAsync), METH_VARARGS, nullptr },
        { "get_input_stream_at", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_GetInputStreamAt), METH_VARARGS, nullptr },
        { "get_output_stream_at", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_GetOutputStreamAt), METH_VARARGS, nullptr },
        { "read_async", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_ReadAsync), METH_VARARGS, nullptr },
        { "seek", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_Seek), METH_VARARGS, nullptr },
        { "write_async", reinterpret_cast<PyCFunction>(SpeechSynthesisStream_WriteAsync), METH_VARARGS, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_SpeechSynthesisStream), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_SpeechSynthesisStream), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_SpeechSynthesisStream), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpeechSynthesisStream[] = {
        { "timed_metadata_tracks", reinterpret_cast<getter>(SpeechSynthesisStream_get_TimedMetadataTracks), nullptr, nullptr, nullptr },
        { "markers", reinterpret_cast<getter>(SpeechSynthesisStream_get_Markers), nullptr, nullptr, nullptr },
        { "content_type", reinterpret_cast<getter>(SpeechSynthesisStream_get_ContentType), nullptr, nullptr, nullptr },
        { "size", reinterpret_cast<getter>(SpeechSynthesisStream_get_Size), reinterpret_cast<setter>(SpeechSynthesisStream_put_Size), nullptr, nullptr },
        { "can_read", reinterpret_cast<getter>(SpeechSynthesisStream_get_CanRead), nullptr, nullptr, nullptr },
        { "can_write", reinterpret_cast<getter>(SpeechSynthesisStream_get_CanWrite), nullptr, nullptr, nullptr },
        { "position", reinterpret_cast<getter>(SpeechSynthesisStream_get_Position), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SpeechSynthesisStream[] = 
    {
        { Py_tp_new, _new_SpeechSynthesisStream },
        { Py_tp_dealloc, _dealloc_SpeechSynthesisStream },
        { Py_tp_methods, _methods_SpeechSynthesisStream },
        { Py_tp_getset, _getset_SpeechSynthesisStream },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_SpeechSynthesisStream =
    {
        "_winsdk_Windows_Media_SpeechSynthesis.SpeechSynthesisStream",
        sizeof(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesisStream),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpeechSynthesisStream
    };

    // ----- SpeechSynthesizer class --------------------
    constexpr const char* const _type_name_SpeechSynthesizer = "SpeechSynthesizer";

    static PyObject* _new_SpeechSynthesizer(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
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
                winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizer instance{  };
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

    static void _dealloc_SpeechSynthesizer(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpeechSynthesizer_Close(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self, PyObject* args) noexcept
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

    static PyObject* SpeechSynthesizer_SynthesizeSsmlToStreamAsync(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.SynthesizeSsmlToStreamAsync(param0));
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

    static PyObject* SpeechSynthesizer_SynthesizeTextToStreamAsync(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.SynthesizeTextToStreamAsync(param0));
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

    static PyObject* SpeechSynthesizer_TrySetDefaultVoiceAsync(PyObject* /*unused*/, PyObject* args) noexcept
    {
        Py_ssize_t arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::Windows::Media::SpeechSynthesis::VoiceInformation>(args, 0);

                return py::convert(winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizer::TrySetDefaultVoiceAsync(param0));
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

    static PyObject* SpeechSynthesizer_get_Voice(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Voice());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizer_put_Voice(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Media::SpeechSynthesis::VoiceInformation>(arg);

            self->obj.Voice(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesizer_get_Options(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Options());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpeechSynthesizer_get_AllVoices(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizer::AllVoices());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* SpeechSynthesizer_get_DefaultVoice(PyObject* /*unused*/, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizer::DefaultVoice());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_SpeechSynthesizer(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizer>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _enter_SpeechSynthesizer(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self) noexcept
    {
        Py_INCREF(self);
        return reinterpret_cast<PyObject*>(self);
    }

    static PyObject* _exit_SpeechSynthesizer(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer* self) noexcept
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

    static PyMethodDef _methods_SpeechSynthesizer[] = {
        { "close", reinterpret_cast<PyCFunction>(SpeechSynthesizer_Close), METH_VARARGS, nullptr },
        { "synthesize_ssml_to_stream_async", reinterpret_cast<PyCFunction>(SpeechSynthesizer_SynthesizeSsmlToStreamAsync), METH_VARARGS, nullptr },
        { "synthesize_text_to_stream_async", reinterpret_cast<PyCFunction>(SpeechSynthesizer_SynthesizeTextToStreamAsync), METH_VARARGS, nullptr },
        { "try_set_default_voice_async", reinterpret_cast<PyCFunction>(SpeechSynthesizer_TrySetDefaultVoiceAsync), METH_VARARGS | METH_STATIC, nullptr },
        { "get_all_voices", reinterpret_cast<PyCFunction>(SpeechSynthesizer_get_AllVoices), METH_NOARGS | METH_STATIC, nullptr },
        { "get_default_voice", reinterpret_cast<PyCFunction>(SpeechSynthesizer_get_DefaultVoice), METH_NOARGS | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_SpeechSynthesizer), METH_O | METH_STATIC, nullptr },
        { "__enter__", reinterpret_cast<PyCFunction>(_enter_SpeechSynthesizer), METH_NOARGS, nullptr },
        { "__exit__",  reinterpret_cast<PyCFunction>(_exit_SpeechSynthesizer), METH_VARARGS, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpeechSynthesizer[] = {
        { "voice", reinterpret_cast<getter>(SpeechSynthesizer_get_Voice), reinterpret_cast<setter>(SpeechSynthesizer_put_Voice), nullptr, nullptr },
        { "options", reinterpret_cast<getter>(SpeechSynthesizer_get_Options), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SpeechSynthesizer[] = 
    {
        { Py_tp_new, _new_SpeechSynthesizer },
        { Py_tp_dealloc, _dealloc_SpeechSynthesizer },
        { Py_tp_methods, _methods_SpeechSynthesizer },
        { Py_tp_getset, _getset_SpeechSynthesizer },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_SpeechSynthesizer =
    {
        "_winsdk_Windows_Media_SpeechSynthesis.SpeechSynthesizer",
        sizeof(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizer),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpeechSynthesizer
    };

    // ----- SpeechSynthesizerOptions class --------------------
    constexpr const char* const _type_name_SpeechSynthesizerOptions = "SpeechSynthesizerOptions";

    static PyObject* _new_SpeechSynthesizerOptions(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_SpeechSynthesizerOptions);
        return nullptr;
    }

    static void _dealloc_SpeechSynthesizerOptions(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* SpeechSynthesizerOptions_get_IncludeWordBoundaryMetadata(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeWordBoundaryMetadata());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizerOptions_put_IncludeWordBoundaryMetadata(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.IncludeWordBoundaryMetadata(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesizerOptions_get_IncludeSentenceBoundaryMetadata(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.IncludeSentenceBoundaryMetadata());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizerOptions_put_IncludeSentenceBoundaryMetadata(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<bool>(arg);

            self->obj.IncludeSentenceBoundaryMetadata(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesizerOptions_get_SpeakingRate(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.SpeakingRate());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizerOptions_put_SpeakingRate(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<double>(arg);

            self->obj.SpeakingRate(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesizerOptions_get_AudioVolume(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AudioVolume());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizerOptions_put_AudioVolume(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<double>(arg);

            self->obj.AudioVolume(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesizerOptions_get_AudioPitch(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AudioPitch());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizerOptions_put_AudioPitch(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<double>(arg);

            self->obj.AudioPitch(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesizerOptions_get_PunctuationSilence(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.PunctuationSilence());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizerOptions_put_PunctuationSilence(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Media::SpeechSynthesis::SpeechPunctuationSilence>(arg);

            self->obj.PunctuationSilence(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SpeechSynthesizerOptions_get_AppendedSilence(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.AppendedSilence());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SpeechSynthesizerOptions_put_AppendedSilence(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_TypeError, "property delete not supported");
            return -1;
        }

        try
        {
            auto param0 = py::convert_to<winrt::Windows::Media::SpeechSynthesis::SpeechAppendedSilence>(arg);

            self->obj.AppendedSilence(param0);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* _from_SpeechSynthesizerOptions(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_SpeechSynthesizerOptions[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_SpeechSynthesizerOptions), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_SpeechSynthesizerOptions[] = {
        { "include_word_boundary_metadata", reinterpret_cast<getter>(SpeechSynthesizerOptions_get_IncludeWordBoundaryMetadata), reinterpret_cast<setter>(SpeechSynthesizerOptions_put_IncludeWordBoundaryMetadata), nullptr, nullptr },
        { "include_sentence_boundary_metadata", reinterpret_cast<getter>(SpeechSynthesizerOptions_get_IncludeSentenceBoundaryMetadata), reinterpret_cast<setter>(SpeechSynthesizerOptions_put_IncludeSentenceBoundaryMetadata), nullptr, nullptr },
        { "speaking_rate", reinterpret_cast<getter>(SpeechSynthesizerOptions_get_SpeakingRate), reinterpret_cast<setter>(SpeechSynthesizerOptions_put_SpeakingRate), nullptr, nullptr },
        { "audio_volume", reinterpret_cast<getter>(SpeechSynthesizerOptions_get_AudioVolume), reinterpret_cast<setter>(SpeechSynthesizerOptions_put_AudioVolume), nullptr, nullptr },
        { "audio_pitch", reinterpret_cast<getter>(SpeechSynthesizerOptions_get_AudioPitch), reinterpret_cast<setter>(SpeechSynthesizerOptions_put_AudioPitch), nullptr, nullptr },
        { "punctuation_silence", reinterpret_cast<getter>(SpeechSynthesizerOptions_get_PunctuationSilence), reinterpret_cast<setter>(SpeechSynthesizerOptions_put_PunctuationSilence), nullptr, nullptr },
        { "appended_silence", reinterpret_cast<getter>(SpeechSynthesizerOptions_get_AppendedSilence), reinterpret_cast<setter>(SpeechSynthesizerOptions_put_AppendedSilence), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SpeechSynthesizerOptions[] = 
    {
        { Py_tp_new, _new_SpeechSynthesizerOptions },
        { Py_tp_dealloc, _dealloc_SpeechSynthesizerOptions },
        { Py_tp_methods, _methods_SpeechSynthesizerOptions },
        { Py_tp_getset, _getset_SpeechSynthesizerOptions },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_SpeechSynthesizerOptions =
    {
        "_winsdk_Windows_Media_SpeechSynthesis.SpeechSynthesizerOptions",
        sizeof(py::wrapper::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SpeechSynthesizerOptions
    };

    // ----- VoiceInformation class --------------------
    constexpr const char* const _type_name_VoiceInformation = "VoiceInformation";

    static PyObject* _new_VoiceInformation(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        py::set_invalid_activation_error(_type_name_VoiceInformation);
        return nullptr;
    }

    static void _dealloc_VoiceInformation(py::wrapper::Windows::Media::SpeechSynthesis::VoiceInformation* self)
    {
        auto hash_value = std::hash<winrt::Windows::Foundation::IInspectable>{}(self->obj);
        py::wrapped_instance(hash_value, nullptr);
        self->obj = nullptr;
    }

    static PyObject* VoiceInformation_get_Description(py::wrapper::Windows::Media::SpeechSynthesis::VoiceInformation* self, void* /*unused*/) noexcept
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

    static PyObject* VoiceInformation_get_DisplayName(py::wrapper::Windows::Media::SpeechSynthesis::VoiceInformation* self, void* /*unused*/) noexcept
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

    static PyObject* VoiceInformation_get_Gender(py::wrapper::Windows::Media::SpeechSynthesis::VoiceInformation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Gender());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* VoiceInformation_get_Id(py::wrapper::Windows::Media::SpeechSynthesis::VoiceInformation* self, void* /*unused*/) noexcept
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

    static PyObject* VoiceInformation_get_Language(py::wrapper::Windows::Media::SpeechSynthesis::VoiceInformation* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Language());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _from_VoiceInformation(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Media::SpeechSynthesis::VoiceInformation>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_VoiceInformation[] = {
        { "_from", reinterpret_cast<PyCFunction>(_from_VoiceInformation), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_VoiceInformation[] = {
        { "description", reinterpret_cast<getter>(VoiceInformation_get_Description), nullptr, nullptr, nullptr },
        { "display_name", reinterpret_cast<getter>(VoiceInformation_get_DisplayName), nullptr, nullptr, nullptr },
        { "gender", reinterpret_cast<getter>(VoiceInformation_get_Gender), nullptr, nullptr, nullptr },
        { "id", reinterpret_cast<getter>(VoiceInformation_get_Id), nullptr, nullptr, nullptr },
        { "language", reinterpret_cast<getter>(VoiceInformation_get_Language), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_VoiceInformation[] = 
    {
        { Py_tp_new, _new_VoiceInformation },
        { Py_tp_dealloc, _dealloc_VoiceInformation },
        { Py_tp_methods, _methods_VoiceInformation },
        { Py_tp_getset, _getset_VoiceInformation },
        { 0, nullptr },
    };

    static PyType_Spec _type_spec_VoiceInformation =
    {
        "_winsdk_Windows_Media_SpeechSynthesis.VoiceInformation",
        sizeof(py::wrapper::Windows::Media::SpeechSynthesis::VoiceInformation),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_VoiceInformation
    };

    // ----- Windows.Media.SpeechSynthesis Initialization --------------------
    static int module_exec(PyObject* module) noexcept
    {
        try
        {
            py::pyobj_handle bases { PyTuple_Pack(1, py::winrt_type<py::Object>::python_type) };

            py::winrt_type<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesisStream>::python_type = py::register_python_type(module, _type_name_SpeechSynthesisStream, &_type_spec_SpeechSynthesisStream, bases.get());
            py::winrt_type<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizer>::python_type = py::register_python_type(module, _type_name_SpeechSynthesizer, &_type_spec_SpeechSynthesizer, bases.get());
            py::winrt_type<winrt::Windows::Media::SpeechSynthesis::SpeechSynthesizerOptions>::python_type = py::register_python_type(module, _type_name_SpeechSynthesizerOptions, &_type_spec_SpeechSynthesizerOptions, bases.get());
            py::winrt_type<winrt::Windows::Media::SpeechSynthesis::VoiceInformation>::python_type = py::register_python_type(module, _type_name_VoiceInformation, &_type_spec_VoiceInformation, bases.get());

            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyModuleDef_Slot module_slots[] = {{Py_mod_exec, module_exec}, {}};

    PyDoc_STRVAR(module_doc, "Windows.Media.SpeechSynthesis");

    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winsdk_Windows_Media_SpeechSynthesis",
           module_doc,
           0,
           nullptr,
           module_slots,
           nullptr,
           nullptr,
           nullptr};
} // py::cpp::Windows::Media::SpeechSynthesis

PyMODINIT_FUNC
PyInit__winsdk_Windows_Media_SpeechSynthesis (void) noexcept
{
    return PyModuleDef_Init(&py::cpp::Windows::Media::SpeechSynthesis::module_def);
}
