// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.2

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Media.Audio.h")
#include "py.Windows.Media.Audio.h"
#endif

#if __has_include("py.Windows.Storage.Streams.h")
#include "py.Windows.Storage.Streams.h"
#endif

#include <winrt/Windows.ApplicationModel.ConversationalAgent.h>

namespace py::proj::Windows::ApplicationModel::ConversationalAgent
{}

namespace py::impl::Windows::ApplicationModel::ConversationalAgent
{}

namespace py::wrapper::Windows::ApplicationModel::ConversationalAgent
{
    using ActivationSignalDetectionConfiguration = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ActivationSignalDetectionConfiguration>;
    using ActivationSignalDetectionConfigurationCreationResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ActivationSignalDetectionConfigurationCreationResult>;
    using ActivationSignalDetector = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ActivationSignalDetector>;
    using ConversationalAgentDetectorManager = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentDetectorManager>;
    using ConversationalAgentSession = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSession>;
    using ConversationalAgentSessionInterruptedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSessionInterruptedEventArgs>;
    using ConversationalAgentSignal = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSignal>;
    using ConversationalAgentSignalDetectedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSignalDetectedEventArgs>;
    using ConversationalAgentSystemStateChangedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSystemStateChangedEventArgs>;
    using DetectionConfigurationAvailabilityChangedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::DetectionConfigurationAvailabilityChangedEventArgs>;
    using DetectionConfigurationAvailabilityInfo = py::winrt_wrapper<winrt::Windows::ApplicationModel::ConversationalAgent::DetectionConfigurationAvailabilityInfo>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ActivationSignalDetectionConfiguration>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ActivationSignalDetectionConfigurationCreationResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ActivationSignalDetector>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentDetectorManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSession>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSessionInterruptedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSignal>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSignalDetectedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::ConversationalAgentSystemStateChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::DetectionConfigurationAvailabilityChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::ConversationalAgent::DetectionConfigurationAvailabilityInfo>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
