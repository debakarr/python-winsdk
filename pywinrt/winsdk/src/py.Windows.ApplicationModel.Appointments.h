// WARNING: Please don't edit this file. It was generated by Python/WinRT v1.0.0-beta.1

#pragma once

#include "pybase.h"

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.System.h")
#include "py.Windows.System.h"
#endif

#if __has_include("py.Windows.UI.h")
#include "py.Windows.UI.h"
#endif

#if __has_include("py.Windows.UI.Popups.h")
#include "py.Windows.UI.Popups.h"
#endif

#include <winrt/Windows.ApplicationModel.Appointments.h>

namespace py::proj::Windows::ApplicationModel::Appointments
{}

namespace py::impl::Windows::ApplicationModel::Appointments
{}

namespace py::wrapper::Windows::ApplicationModel::Appointments
{
    using Appointment = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::Appointment>;
    using AppointmentCalendar = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentCalendar>;
    using AppointmentCalendarSyncManager = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentCalendarSyncManager>;
    using AppointmentConflictResult = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentConflictResult>;
    using AppointmentException = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentException>;
    using AppointmentInvitee = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentInvitee>;
    using AppointmentManager = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentManager>;
    using AppointmentManagerForUser = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentManagerForUser>;
    using AppointmentOrganizer = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentOrganizer>;
    using AppointmentProperties = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentProperties>;
    using AppointmentRecurrence = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentRecurrence>;
    using AppointmentStore = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentStore>;
    using AppointmentStoreChange = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChange>;
    using AppointmentStoreChangeReader = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangeReader>;
    using AppointmentStoreChangeTracker = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangeTracker>;
    using AppointmentStoreChangedDeferral = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangedDeferral>;
    using AppointmentStoreChangedEventArgs = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangedEventArgs>;
    using AppointmentStoreNotificationTriggerDetails = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreNotificationTriggerDetails>;
    using FindAppointmentsOptions = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::FindAppointmentsOptions>;
    using IAppointmentParticipant = py::winrt_wrapper<winrt::Windows::ApplicationModel::Appointments::IAppointmentParticipant>;
}

namespace py
{
    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::Appointment>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentCalendar>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentCalendarSyncManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentConflictResult>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentException>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentInvitee>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentManager>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentManagerForUser>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentOrganizer>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentProperties>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentRecurrence>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentStore>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChange>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangeReader>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangeTracker>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangedDeferral>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreChangedEventArgs>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::AppointmentStoreNotificationTriggerDetails>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::FindAppointmentsOptions>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

    template<>
    struct winrt_type<winrt::Windows::ApplicationModel::Appointments::IAppointmentParticipant>
    {
        static PyTypeObject* python_type;
        static PyTypeObject* get_python_type() { return python_type; }
    };

}
